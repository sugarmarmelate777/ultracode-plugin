import sys
import asyncio
import io
import argparse
import requests

# Fix unicode print issues on Windows
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)

from crawl4ai import AsyncWebCrawler

DEEPSEEK_URL = "http://localhost:8082/v1/chat/completions"

def summarize_text(raw_text):
    """Summarizes text using local DeepSeek Engine to save tokens."""
    print("--- SUMMARIZING EXTRACTED TEXT VIA DEEPSEEK ---")
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "deepseek-coder",
        "messages": [
            {"role": "system", "content": "You are a professional text summarizer. Summarize the following web content, extracting key information, code snippets, and main points. Do not lose technical details."},
            {"role": "user", "content": raw_text[:25000]} # Limit to 25k chars for safety
        ],
        "temperature": 0.3
    }
    
    try:
        response = requests.post(DEEPSEEK_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Summarization failed: {e}. Falling back to raw text.")
        return raw_text

async def extract_webpage(url, summarize=False):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url=url,
        )
        
        if result.success:
            print("--- EXTRACTION SUCCESSFUL ---")
            if summarize:
                summary = summarize_text(result.markdown)
                print(summary)
            else:
                print(result.markdown)
        else:
            print(f"--- EXTRACTION FAILED ---\n{result.error_message}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Omni-Extractor Web Scraper")
    parser.add_argument("url", help="URL to scrape")
    parser.add_argument("--summarize", action="store_true", help="Pass extracted text through LLM summarizer")
    args = parser.add_argument() if not len(sys.argv) > 1 else parser.parse_args()
    
    target_url = args.url
    print(f"Starting extraction for URL: {target_url}")
    asyncio.run(extract_webpage(target_url, args.summarize))
