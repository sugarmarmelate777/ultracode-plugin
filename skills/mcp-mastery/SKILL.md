---
name: MCP Mastery (Protocol Utilization)
version: "2.1.0"
depends_on: []
description: MCP-first architecture — business-domain catalog, never-write-parsers rule, user-instruction protocol, large-document analysis, business MCP integrations (CRM/ERP/Finance/HR). ALWAYS use MCP servers over custom scripts. Cross-ref: ponytail-yagni (only install servers your domain actually needs), skill-hunter (exhaustive registry search before custom code).
---

# MCP Mastery (Protocol Utilization)

## GOLDEN RULE: NEVER Write Custom Parsers or Scrapers

**ABSOLUTE. NON-NEGOTIABLE.** If you are about to write a Python/Node/Bash script that parses HTML, scrapes a webpage, extracts text from a PDF, reads a spreadsheet, pulls messages from a chat app, or geocodes an address — STOP. You are violating MCP Mastery. There is an MCP server for that. Find it in the catalog below. Use it.

Why:
- Custom scrapers break on DOM changes. MCP servers are maintained.
- Custom parsers miss edge cases. MCP servers handle encoding, auth, rate-limiting.
- Custom scripts waste tokens and time. MCP servers are one tool call.
- Every minute spent maintaining a scraper is a minute not building the actual product.

The ONLY exception: if you exhaustively check the catalog below AND search the MCP registry (https://github.com/modelcontextprotocol/servers) and confirm no server exists, then — and only then — may you write a minimal extraction script. But you must document why no MCP server sufficed.

---

## Directive 1: Protocol First

Before ANY of these actions, check `<mcp_servers>` in your system prompt for available tools:

| You want to... | Instead of... | Use MCP server... |
|---|---|---|
| Fetch a webpage | `curl` / `wget` | `@anthropic/mcp-server-puppeteer` or `@anthropic/mcp-server-fetch` |
| Scrape dynamic JS content | Selenium / Playwright script | `@anthropic/mcp-server-puppeteer` |
| Read a Google Doc / Sheet | Google API script | `@anthropic/mcp-server-google-drive` |
| Parse a PDF | `PyPDF2` / `pdfplumber` script | `@anthropic/mcp-server-google-drive` (if in Drive) or `@anthropic/mcp-server-puppeteer` (render to text) |
| Geocode / route optimize | Custom `requests` to API | `@anthropic/mcp-server-google-maps` |
| Read Telegram messages | Telethon / MTProto script | `mcp-server-telegram` |
| Search documentation | `curl` + grep | `@anthropic/mcp-server-context7` or `docs-mcp-server` |
| Deep research | Manual web searches | `mcp-server-perplexity` or `notebooklm-mcp-server` |
| SQL queries | `psql` / `mysql` CLI | `@anthropic/mcp-server-postgres` / `@anthropic/mcp-server-mysql` |
| File system ops | `find` / `grep` shell commands | `@anthropic/mcp-server-filesystem` |

**Tool selection priority**: local/offline MCP tools > remote MCP tools > CLI commands. If overlapping tools exist, prefer the one requiring no network round-trip.

---

## Directive 2: MCP Server Catalog (by Business Domain)

### 2.1 DOCUMENTS / OFFICE SUITE

| MCP Server | npm/install | Use Case |
|---|---|---|
| **Google Drive MCP** | `@anthropic/mcp-server-google-drive` | Read/write Google Docs, Sheets, Slides. Parse spreadsheets into structured data. Search Drive. Export to PDF/CSV. |
| **Microsoft Graph / SharePoint MCP** | `@anthropic/mcp-server-microsoft-graph` | Read/write Office 365 docs, SharePoint lists, OneDrive files. Extract tables from Word docs. |
| **Notion MCP** | `@anthropic/mcp-server-notion` | Read/write Notion pages and databases. Query structured data. |
| **Box MCP** | `mcp-server-box` | Enterprise file storage. Read/write/search Box documents. |

**When to use**: Business plans, government contracts, financial spreadsheets, legal documents, meeting notes. If a file lives in Google Drive, SharePoint, Notion, or Box — DO NOT download and parse manually. Use the MCP server.

### 2.2 WEB SCRAPING / BROWSER AUTOMATION

| MCP Server | npm/install | Use Case |
|---|---|---|
| **Puppeteer MCP** | `@anthropic/mcp-server-puppeteer` | Full browser automation. Render JavaScript SPAs. Screenshot pages. Fill forms. Click buttons. Extract dynamic content. Navigate multi-page flows. |
| **Fetch MCP** | `@anthropic/mcp-server-fetch` | Lightweight HTTP fetch. Good for static HTML, JSON APIs, RSS feeds. Faster than Puppeteer for simple GET requests. |

**Puppeteer MCP Specific Capabilities**:
- **YouTube**: Navigate to video page, extract title, description, transcript, comments, view count, channel info.
- **Facebook**: Extract public page posts, comments, event details (public data only — respect ToS).
- **Social media parsing**: Instagram public posts, Twitter/X public timelines, LinkedIn public profiles.
- **Government portals**: Navigate contract portals, extract PDF links, fill search forms, paginate through results.
- **E-commerce**: Product listings, prices, availability from public pages.

**When to use Puppeteer vs Fetch**:
- Static HTML / API endpoint? Use Fetch MCP (faster, fewer resources).
- JavaScript-rendered content / form interaction / multi-page flow? Use Puppeteer MCP.

### 2.3 MAPS / LOGISTICS / GEOSPATIAL

| MCP Server | npm/install | Use Case |
|---|---|---|
| **Google Maps MCP** | `@anthropic/mcp-server-google-maps` | Geocoding, reverse geocoding, directions, distance matrix, places search, route optimization. |

**When to use**: Government logistics contracts, delivery route planning, site selection for construction projects, disaster response coordination, field service territory optimization, proximity analysis for business locations.

**Key capabilities**:
- Geocode addresses to lat/lng (batch, single)
- Calculate travel time/distance between N points (Distance Matrix)
- Optimize multi-stop routes (Directions API with waypoints)
- Search for businesses/landmarks near a location (Places API)
- Validate addresses and get structured components
- Elevation data for terrain analysis

**Documentation**: https://developers.google.com/maps/documentation

### 2.4 MESSAGING / COMMUNICATION

| MCP Server | npm/install | Use Case |
|---|---|---|
| **Telegram MCP** | `mcp-server-telegram` | Read messages from chats/channels/groups. Send messages. Download media/files. Search message history. Extract user lists. |
| **Slack MCP** | `@anthropic/mcp-server-slack` | Read channel history, send messages, search messages, list users, upload files. |
| **Discord MCP** | `mcp-server-discord` | Read server channels, send messages, manage roles (bot permission required). |
| **WhatsApp MCP** | `mcp-server-whatsapp` (via Baileys) | Send/receive WhatsApp messages. Extract chat history (requires phone pairing). |

**When to use**: Extracting business intelligence from Telegram groups, pulling customer support logs from Slack, archiving project discussions, mining competitor public channels for market research.

**Telegram MCP specifics**: Can read from public channels without user account. For private chats, requires a Telegram API app (api_id/api_hash from https://my.telegram.org). Supports message search by keyword, date range, and sender.

**IMPORTANT**: Always respect privacy laws (GDPR, CCPA). Only extract data from channels you own or have explicit permission to access. Never use for surveillance.

### 2.5 DATABASES / DATA STORES

| MCP Server | npm/install | Use Case |
|---|---|---|
| **PostgreSQL MCP** | `@anthropic/mcp-server-postgres` | Query Postgres databases. List schemas/tables. Execute read-only queries. |
| **MySQL MCP** | `@anthropic/mcp-server-mysql` | Query MySQL databases. List schemas/tables. |
| **SQLite MCP** | `@anthropic/mcp-server-sqlite` | Query local SQLite files. No server needed. |
| **BigQuery MCP** | `@anthropic/mcp-server-bigquery` | Query Google BigQuery datasets. Run analytical queries. |
| **Snowflake MCP** | `@anthropic/mcp-server-snowflake` | Query Snowflake data warehouse. |
| **Redis MCP** | `mcp-server-redis` | Read/write Redis keys. Cache inspection. |
| **Elasticsearch MCP** | `mcp-server-elasticsearch` | Full-text search, log analysis, aggregations. |

**When to use**: Data extraction for business intelligence, report generation, data validation, schema exploration. ALWAYS use read-only credentials when possible.

### 2.6 AI / RESEARCH / DEEP ANALYSIS

| MCP Server | npm/install | Use Case |
|---|---|---|
| **Perplexity MCP** | `mcp-server-perplexity` | Deep web research with citations. Current events. Fact-checking. Market research. Competitor analysis. |
| **NotebookLM MCP** | `notebooklm-mcp-server` | Upload documents, get AI-generated summaries, audio overviews, Q&A against document corpus. Deep document analysis. |
| **Brave Search MCP** | `@anthropic/mcp-server-brave-search` | Web search with privacy focus. Good for general research. |
| **Exa MCP** | `mcp-server-exa` | Semantic search. Find similar content. Search by meaning, not keywords. |
| **Context7 MCP** | `@anthropic/mcp-server-context7` | Up-to-date library/framework documentation search. Never read outdated docs. |
| **Firecrawl MCP** | `mcp-server-firecrawl` | Crawl entire websites. Extract structured data from multiple pages. Sitemap-aware. |

**When to use what**:
- Need cited, current web research? Perplexity MCP.
- Need to analyze a 200-page government RFP? NotebookLM MCP (upload docs, query them).
- Need to find similar companies/technologies? Exa MCP (semantic search).
- Need to check latest API docs for a framework? Context7 MCP.
- Need to crawl an entire documentation site? Firecrawl MCP.

### 2.7 FILE SYSTEM / DEVELOPMENT TOOLS

| MCP Server | npm/install | Use Case |
|---|---|---|
| **Filesystem MCP** | `@anthropic/mcp-server-filesystem` | Read/write files in allowed directories. List directories. Get file metadata. |
| **GitHub MCP** | `@anthropic/mcp-server-github` | Repo management, issues, PRs, search code, read files. |
| **GitLab MCP** | `mcp-server-gitlab` | Same as GitHub but for GitLab instances. |
| **Git MCP** | `mcp-server-git` | Local git operations: log, diff, blame, branch management. |

### 2.8 ADDITIONAL DOMAINS

| Domain | MCP Server | Use Case |
|---|---|---|
| **Calendar** | `@anthropic/mcp-server-google-calendar` | Schedule meetings, check availability, create events for deadlines/milestones. |
| **Email** | `@anthropic/mcp-server-gmail` | Read/search/send emails. Extract meeting invites, track email threads. |
| **CRM** | `mcp-server-hubspot` / `mcp-server-salesforce` | Customer data, deal pipelines, contact management. |
| **Finance** | `mcp-server-stripe` / `mcp-server-plaid` | Payment data, transaction history, financial reporting. |
| **Cloud/AWS** | `mcp-server-aws` / `mcp-server-gcloud` | Cloud resource management, log retrieval, cost analysis. |
| **Jira/Linear** | `mcp-server-jira` / `mcp-server-linear` | Issue tracking, sprint management, bug tracking. |

---

## Directive 3: Large Document Analysis Protocol

When dealing with government contracts, RFPs, legal documents, or any document over 50 pages:

### Step 1: Identify the document source
- **Google Drive**? Use Google Drive MCP to access it directly.
- **URL / web portal**? Use Puppeteer MCP to navigate and download.
- **Local file**? Use Filesystem MCP to read it.

### Step 2: Choose the analysis tool
- **Structured data (spreadsheet, tables)**? Google Drive MCP can parse into structured JSON.
- **Long-form text (PDF, Word doc)**? NotebookLM MCP: upload the document, then query it with natural language.
- **Need to compare multiple documents**? Upload all to NotebookLM MCP and ask cross-document questions.
- **Need to extract specific clauses/provisions**? Query the document through the MCP server with targeted questions.

### Step 3: NEVER do this
- DO NOT download the file to disk and write a Python script to parse it.
- DO NOT use `pdftotext` / `pdfplumber` / `python-docx` / `openpyxl` directly.
- DO NOT read the entire file into context (use MCP tools to query it selectively).

### Step 4: Example workflow for a government RFP
```
1. Puppeteer MCP: Navigate to procurement portal, search for RFP #XYZ, download PDF.
2. NotebookLM MCP: Upload the PDF, ask "What are the mandatory requirements?"
3. NotebookLM MCP: Ask "What is the submission deadline and format?"
4. NotebookLM MCP: Ask "What are the evaluation criteria and their weights?"
5. Google Docs MCP: Create a compliance matrix spreadsheet from extracted requirements.
```

---

## Directive 4: User Instruction Protocol

When a user needs to install an MCP server, provide this exact guidance:

### For Claude Desktop users:
```json
// Add to claude_desktop_config.json (~/Library/Application Support/Claude/claude_desktop_config.json on macOS,
// %APPDATA%\Claude\claude_desktop_config.json on Windows)
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-SERVERNAME"],
      "env": {
        "API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### For Antigravity IDE / Gemini CLI users:
```json
// Add to .gemini/config/mcp.json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-SERVERNAME"],
      "env": {
        "API_KEY": "${ENV_VAR_NAME}"
      }
    }
  }
}
```

### For Claude Code / VS Code / Cursor users:
```json
// Add to .claude/mcp.json or project-level MCP config
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-SERVERNAME"],
      "env": {
        "API_KEY": "${ENV_VAR_NAME}"
      }
    }
  }
}
```

### Installation checklist (tell the user):
1. **Install Node.js** (v18+): `node --version` — if missing, install from https://nodejs.org
2. **Get API key**: from the service's developer console (Google Cloud Console, Telegram my.telegram.org, Perplexity dashboard, etc.)
3. **Set environment variable**: `export GOOGLE_DRIVE_API_KEY="..."` or add to config env block
4. **Run once to test**: `npx -y @anthropic/mcp-server-SERVERNAME` — should start without errors
5. **Restart IDE / Claude**: MCP servers load on startup

### Common error messages and fixes:
| Error | Cause | Fix |
|---|---|---|
| `command not found: npx` | Node.js not installed | Install Node.js v18+ |
| `EACCES: permission denied` | Port in use or no file access | Check port, check file permissions |
| `401 Unauthorized` | Bad/missing API key | Verify key, check env var is set |
| `ERR_MODULE_NOT_FOUND` | npm package not published | Check exact package name in catalog above |
| `connect ECONNREFUSED` | Server crashed or not started | Run manually first to see crash logs |

---

## Directive 5: Lazy Loading Awareness

Some MCP tools are lazy-loaded. Before calling any MCP tool:
1. Check if it appears in `<mcp_servers>` or your tool list.
2. Read the tool's input schema (parameters, required fields).
3. If the tool is not listed, it may need to be triggered by a related action first (e.g., opening a file may lazy-load filesystem MCP).

Do NOT assume an MCP tool is unavailable just because it is not immediately visible in your tool list. Some platforms (Antigravity, Claude Code) lazy-load MCP servers based on context.

---

## Directive 6: Business MCP Integrations (CRM / ERP / Finance / HR)

Beyond the standard catalog above, MCP servers exist for enterprise business systems. BEFORE building a custom integration, check these:

### 6.1 Customer Relationship Management (CRM)

| MCP Server | npm/install | Use Case |
|---|---|---|
| **HubSpot MCP** | `mcp-server-hubspot` | Contacts, deals, tickets, companies. Pipeline reporting. Marketing email data. |
| **Salesforce MCP** | `mcp-server-salesforce` | Accounts, opportunities, cases, custom objects. SOQL queries. Apex execution. |
| **Zoho CRM MCP** | `mcp-server-zoho` | Leads, contacts, potentials. Workflow automation data. |

### 6.2 Enterprise Resource Planning (ERP)

| MCP Server | npm/install | Use Case |
|---|---|---|
| **SAP MCP** | `mcp-server-sap` | Read/write SAP BAPI/RFC. Extract financial postings, material masters, purchase orders. |
| **Oracle NetSuite MCP** | `mcp-server-netsuite` | SuiteTalk SOAP/web services. Saved searches, transaction data, inventory levels. |
| **Odoo MCP** | `mcp-server-odoo` | CRM, accounting, inventory, HR modules via XML-RPC. |

### 6.3 Finance / Payments / Banking

| MCP Server | npm/install | Use Case |
|---|---|---|
| **Stripe MCP** | `mcp-server-stripe` | Payment intents, invoices, subscriptions, refunds. Revenue reporting. |
| **Plaid MCP** | `mcp-server-plaid` | Bank account linking, transaction history, balance checks. |
| **QuickBooks MCP** | `mcp-server-quickbooks` | Invoices, expenses, chart of accounts, profit & loss reports. |

### 6.4 Human Resources / Payroll

| MCP Server | npm/install | Use Case |
|---|---|---|
| **BambooHR MCP** | `mcp-server-bamboohr` | Employee directory, time-off balances, performance reviews. |
| **Workday MCP** | `mcp-server-workday` | Worker data, compensation, org charts, recruiting pipelines. |
| **Gusto MCP** | `mcp-server-gusto` | Payroll, benefits, contractor payments, tax filings. |

### 6.5 Supply Chain / Logistics

| MCP Server | npm/install | Use Case |
|---|---|---|
| **ShipBob MCP** | `mcp-server-shipbob` | Order fulfillment, inventory across warehouses, shipment tracking. |
| **Shippo MCP** | `mcp-server-shippo` | Multi-carrier shipping rates, label generation, tracking. |
| **Flexport MCP** | `mcp-server-flexport` | Ocean/air freight quotes, customs documentation, shipment visibility. |

**When to use**: Any task involving CRM data extraction, ERP reporting, financial reconciliation, payroll audits, supply chain visibility. NEVER write custom API wrappers when an MCP server covers the integration.

---

## Directive 7: Ponytail-Yagni — Install Only What Your Domain Needs

**Cross-reference: ponytail-yagni.** The MCP catalog above is comprehensive but not exhaustive. You do NOT need every server installed. Apply YAGNI ("You Aren't Gonna Need It"):

1. **Audit your domain**: Are you building government contracts? Install Google Drive + Puppeteer + NotebookLM. Are you building e-commerce? Install Stripe + Shippo + Puppeteer. Are you a DevOps team? Install GitHub + Postgres + AWS.
2. **Install incrementally**: Start with the 2-3 servers your immediate task requires. Add more only when a task demands it.
3. **Remove unused servers**: Every installed MCP server consumes startup time and memory. If you haven't used a server in the last 5 sessions, uninstall it.
4. **One server per domain**: If two MCP servers overlap (e.g., two web scraping servers), keep the one with broader capability and remove the other.

The ponytail-yagni directive prevents MCP server bloat. A lean MCP configuration is a fast configuration.

---

## Directive 8: Skill-Hunter — Exhaustive Registry Search

**Cross-reference: skill-hunter.** When the catalog above (Sections 2 + 6) does not list a server for your use case, you MUST exhaustively search before writing custom code:

1. **GitHub registry**: https://github.com/modelcontextprotocol/servers — official MCP server listing
2. **npm search**: `npm search mcp-server` — community packages
3. **Pip search**: `pip search mcp-server` (Python MCP implementations exist too)
4. **GitHub code search**: `mcp-server <your-tool> language:typescript` — unlisted repos
5. **MCP marketplace**: Check https://mcp.so and https://glama.ai/mcp for curated listings

Only after ALL five sources return nothing may you document "No MCP server exists for <task>" and write a minimal extraction script. The skill-hunter directive ensures you never miss a pre-built solution.

---

## Directive 9: Self-Check Before Writing Code

Before writing ANY data extraction, parsing, or API interaction code, run this checklist:

1. **Is there an MCP server in the catalog for this?** (Check Section 2 and Section 6 above. Be thorough.)
2. **Is the MCP server already connected?** (Check `<mcp_servers>` in system prompt.)
3. **Can the user install it?** (If not connected, use the User Instruction Protocol — Section 4.)
4. **Would a combination of MCP servers work better?** (e.g., Puppeteer to download + NotebookLM to analyze.)
5. **Apply ponytail-yagni**: Do you actually need this server for your domain? (Directive 7.)
6. **Apply skill-hunter**: If catalog misses it, search all 5 registries exhaustively. (Directive 8.)
7. **If NO MCP server exists anywhere** — document this fact, then (and only then) write a minimal script.

If you answer NO to all of the above and write code anyway, you are in violation of MCP Mastery. Go back to step 1.

---

## Quick Reference: Common Tasks Mapped to MCP Servers

| Task | MCP Server | Why Not Manual |
|---|---|---|
| Extract text from a YouTube video | Puppeteer MCP | Handles YouTube's anti-bot measures, cookie consent, dynamic DOM |
| Parse a 200-page government RFP PDF | NotebookLM MCP | AI-powered extraction of requirements, deadlines, evaluation criteria |
| Read financial data from a Google Sheet | Google Drive MCP | Direct API access, handles auth, preserves formulas and formatting |
| Find optimal delivery routes for 50 stops | Google Maps MCP | Uses Google's routing engine with live traffic, no reinventing the wheel |
| Extract all messages from a Telegram group | Telegram MCP | Handles MTProto protocol, rate limits, media downloads |
| Research competitors' latest funding rounds | Perplexity MCP | Cited, current web research with sources |
| Crawl a documentation site for API references | Firecrawl MCP | Sitemap-aware, handles rate limiting, extracts structured Markdown |
| Geocode 500 addresses for a field service map | Google Maps MCP | Batch geocoding with rate limit handling and validation |
| Compare two versions of a legal contract | NotebookLM MCP | Upload both, ask "what changed between version A and version B?" |
| Extract product listings from an e-commerce site | Puppeteer MCP | Handles pagination, lazy loading, A/B test variants, bot detection |
| Extract CRM pipeline data for a sales report | HubSpot MCP / Salesforce MCP | Direct API access, handles auth, preserves custom fields |
| Reconcile monthly Stripe payments against QuickBooks | Stripe MCP + QuickBooks MCP | No custom CSV export/import — MCP servers speak directly |
| Generate payroll audit report from Workday | Workday MCP | Worker data, compensation, org charts — all via MCP |
| Shipment tracking across 3 carriers | Shippo MCP | Multi-carrier rates, labels, tracking in one MCP server |
| Extract SAP financial postings for tax audit | SAP MCP | BAPI/RFC calls, material masters, purchase orders |
