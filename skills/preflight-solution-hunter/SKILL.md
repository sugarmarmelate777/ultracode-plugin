---
name: "Preflight Solution Hunter (No-Reinvent Protocol)"
description: "Mandates agents to search for ready-made MCP servers, Apify actors, GitHub repos, and pre-built solutions across Top-100 IT platforms before writing code from scratch, saving millions of tokens."
---

# Preflight Solution Hunter (No-Reinvent Protocol)

**Version:** 1.0.0
**Author:** AI Architect & Ultracode Core
**Status:** ACTIVE

## 1. Core Directive (The "No-Reinvent" Rule)
Before writing **ANY** code from scratch for a new feature, integration, data parsing task, or complex functionality, you **MUST** perform a "Pre-flight Web Search" to find existing, ready-made solutions.

*DO NOT waste token budget and computational time inventing bicycles. The global IT and AI community has already built thousands of MCP servers, plugins, and open-source scripts.*

## 2. Supported Search Mechanisms (Cost Efficiency)
When you need a new component, use the `search_web` tool (or local custom tools like `DUCKDUCKGO_SEARCH` / `WEB_HARVESTER` if available in the context) to search the top IT platforms.

**CRITICAL COST RULE:** Do not use paid APIs (like Perplexity API, OpenAI web search, or Apify paid runs) for routine pre-flight checks. The goal is to *save* money. Use native `search_web` or free scraping libraries to find the links, and then `read_url_content` to read the docs.

## 3. The "Golden 100" Target Sites (Top Platforms for AI/IT Solutions)
You must explicitly add `site:<domain>` parameters or mention these platforms in your search queries to find the most advanced solutions.

### 🧩 MCP Servers (Model Context Protocol)
*The absolute priority. If an MCP server exists, use it instead of writing custom API wrappers.*
- `site:mcpservers.org`
- `site:mcpmarket.com`
- `site:smith.langchain.com/hub`
- `site:github.com` (use query `topic:mcp-server` or `mcp server <topic>`)
- `site:glif.app`

### 🕸️ Scrapers, Parsers & Automations
- `site:apify.com/store` (Apify Actors for parsing any social media, e-commerce, or web platform)
- `site:browserless.io`

### 🧠 AI Models & Workflows
- `site:huggingface.co/spaces`
- `site:replicate.com`
- `site:flowiseai.com`
- `site:n8n.io`

### 🛠️ Open-Source Ecosystems & Packages
- `site:github.com`
- `site:npmjs.com`
- `site:pypi.org`
- `site:crates.io`

### 📈 Business, Analytics & Marketing Templates
- `site:supabase.com/docs/guides`
- `site:stripe.com/docs`
- `site:vercel.com/templates`

## 4. Execution Workflow
1. **Analyze Task**: Identify the core capability needed (e.g., "Parse Facebook Reels", "Generate PDFs", "Analyze Stock Data").
2. **Search Phrase**: Construct 2-3 search queries targeting the platforms above. (e.g. `facebook reels transcript scraper site:apify.com` or `pdf generator mcp server site:github.com`).
3. **Evaluate**: Review the top 3-5 ready-made solutions.
4. **Download/Integrate**: Download the pre-built code/actor/MCP server and integrate it into the user's project.
5. **Fallback**: ONLY if no viable ready-made solution exists, or if the user explicitly demands a custom local implementation, you may write the code from scratch.

## 5. Defense Mechanism
If a sub-agent attempts to write a large, complex block of code from scratch (e.g., a custom web scraper with Playwright, or a complex API wrapper) without evidence of a prior search, you must **HALT** the execution and instruct the sub-agent to invoke the Preflight Solution Hunter first.
