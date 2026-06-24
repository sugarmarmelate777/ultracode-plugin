---
name: Omni-Parser Extractor (Web & Media Data)
description: Advanced data extraction tools for websites, social media, and audio/video files.
depends_on: [preflight-solution-hunter]
---

# Omni-Parser Extractor

When the user asks to "extract information from a website," "transcribe a video," or "parse social media data," DO NOT write custom Beautifulsoup or requests parsers from scratch, as they often fail on modern JS-rendered sites or Cloudflare-protected pages.

Instead, leverage the built-in **Omni-Extractor** tools located in the plugin's `extractors/` directory.

## 1. Web Parsing (Crawl4AI)
For standard or JS-heavy websites, use the `web_extractor.py` tool. It utilizes the open-source Crawl4AI library to bypass bot protections and return clean Markdown optimized for LLM reading.
- **Usage:** Execute `python <plugin_path>/extractors/web_extractor.py <URL>`
- **Output:** Clean Markdown representation of the page content.

## 2. Social Media Parsing (Apify Bridge)
For closed ecosystems (Instagram, Facebook Reels, TikTok, Amazon, Google Maps), use the `apify_bridge.py` tool. It connects to ready-made Apify Actors.
- **Requirement:** Ensure `APIFY_API_TOKEN` is set in your `.env` or system environment.
- **Usage:** Execute `python <plugin_path>/extractors/apify_bridge.py <ACTOR_ID> '<INPUT_JSON>'`
- **Example:** `python <plugin_path>/extractors/apify_bridge.py apify/instagram-scraper '{"username": ["nike"]}'`

## 3. Audio / Video Transcription (yt-dlp + Whisper)
To transcribe media (YouTube videos, Facebook Reels audio, podcasts), use the `media_transcriber.py` tool. It first attempts to fetch official subtitles via `yt-dlp`. If none exist, it downloads the audio and uses local `Whisper` AI for transcription.
- **Usage:** Execute `python <plugin_path>/extractors/media_transcriber.py <MEDIA_URL>`
- **Note:** This process might take several minutes depending on the audio length. Be patient and wait for the output.

## Guidelines
- Always use these extractors as a *first step* before attempting any custom scraping.
- Never hardcode API keys in the scripts; always rely on environment variables.
