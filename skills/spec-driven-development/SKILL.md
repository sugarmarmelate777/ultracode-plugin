---
name: Spec-Driven Development (Blueprint Mode)
version: "1.0.0"
depends_on: []
description: Forces the creation of a specification (spec.md) detailing edge cases and business logic before any code is planned or written.
---

# Spec-Driven Development (Blueprint Mode)

## Directives

1. **Complexity Threshold:**
   - A `spec.md` is MANDATORY only when a task meets ANY of these criteria:
     - Modifies 4 or more files (>=4)
     - Introduces a new architectural component (e.g., new database table, new API endpoint, new state management)
     - The user explicitly requests a spec or blueprint
   - For simple tasks (e.g., "add a button", "fix this CSS", "rename a variable"), skip `spec.md` and proceed directly to `implementation_plan.md` or inline execution.

2. **Spec Structure (when required):**
   - The `spec.md` must clearly define:
     - **Business Logic / Intent:** What exactly are we building and why?
     - **Inputs & Outputs:** Data structures, API contracts, or UI states.
     - **Edge Cases & Error Handling:** What happens on null inputs, network failures, or invalid states?
     - **Out of Scope:** Explicitly list what this feature will NOT do.

3. **Approval Gate:**
   - The USER must approve the `spec.md` before you proceed to the technical implementation plan. (Subject to Global CI Gate)

4. **Versioning (CRITICAL):**
   - If a `spec.md` already exists, do NOT silently overwrite it. Version it (e.g. `spec_v2.md`) to maintain a clean history.

5. **Spec Template (MANDATORY sections):**
   - Every `spec.md` MUST contain these sections in order:
     - `## Goal` — One sentence: what we are building and why.
     - `## Business Logic / Intent` — Detailed user stories or functional requirements.
     - `## API Surface / Data Contracts` — Input/output schemas, endpoints, or data structures affected.
     - `## Edge Cases & Error Handling` — Null inputs, network failures, invalid states, race conditions.
     - `## Out of Scope` — Explicitly what this feature will NOT do or touch.
   - Missing any section makes the spec incomplete — return it for revision, do not proceed to planning.

---

## Ready-Made Solutions (Cross-Reference: MCP Mastery)

Before designing custom data extraction, API integration, or document parsing in your spec, check whether an **MCP server** already solves the problem. Writing a custom integration spec for something an MCP server handles out-of-the-box is wasted specification effort.

### When to reference MCP Mastery in your spec

| If your spec involves... | Check MCP Mastery for... |
|---|---|
| Reading/writing Google Docs, Sheets, Slides | Google Drive MCP (Directive 2.1) |
| Parsing PDFs, Word docs, or large documents | NotebookLM MCP or Puppeteer MCP (Directive 3) |
| Geocoding, routing, or distance calculations | Google Maps MCP (Directive 2.3) |
| Extracting data from websites or portals | Puppeteer MCP or Fetch MCP (Directive 2.2) |
| Querying databases (Postgres, MySQL, BigQuery, etc.) | Database MCP servers (Directive 2.5) |
| CRM data extraction (HubSpot, Salesforce) | Business MCP Integrations (Directive 2.6) |
| Payment/finance reconciliation (Stripe, QuickBooks) | Finance MCP servers (Directive 2.6.3) |
| ERP data extraction (SAP, NetSuite, Odoo) | ERP MCP servers (Directive 2.6.2) |
| Searching documentation or doing deep research | Perplexity MCP, Context7 MCP, Firecrawl MCP (Directive 2.6) |

**Rule**: If an MCP server covers the integration, your spec does NOT need to define custom API contracts or parsing logic. Simply reference the MCP server in your spec as the implementation vehicle. This keeps specs lean and avoids reinventing maintained, battle-tested solutions.

**Anti-pattern**: Specifying a custom Python script to parse a Google Sheet when Google Drive MCP already handles auth, formatting, and structured data extraction.

Cross-reference: See `mcp-mastery/SKILL.md` for the full MCP server catalog and integration directives.
