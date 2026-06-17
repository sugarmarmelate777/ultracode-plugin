---
name: MCP Mastery (Protocol Utilization)
version: "1.0.0"
depends_on: []
description: Mandates prioritizing built-in Model Context Protocol (MCP) servers and native IDE tools over custom scripts.
---

# MCP Mastery (Protocol Utilization)

## Directives

1. **Protocol First:**
   - Check your tool list for any tools with MCP-related prefixes or descriptions indicating they are MCP-provided. If no MCP tools are detected, skip this skill entirely.
   - Before attempting to use terminal commands for complex data retrieval, web searching, or external API interaction, you MUST check the available `<mcp_servers>` block in your system prompt.

2. **Tool Selection Priority:**
   - Always prioritize a native MCP tool (e.g., your environment's equivalent of an MCP tool caller) over generic command-line execution. If multiple MCP tools overlap, always prioritize local tools that do not require network requests over remote tools.
   - Example: If you need to search documentation, check if a `docs` or `context7` MCP server is available rather than curling a webpage.

3. **Lazy Loading Awareness:**
   - Remember that some MCP tools are Lazy loaded. Read their schemas before calling them.
