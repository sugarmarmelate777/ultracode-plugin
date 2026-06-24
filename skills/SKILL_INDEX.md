# Ultracode Skill Index — v11.2.0 (Elder of Earth)

| # | Skill | Version | Council | Category | Depends On | Description |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | cicd-mode | 1.0.0 | WATER | Resilience | [] | Non-interactive CI/CD mode. Suppresses all user prompts when CI=true. |
| 2 | token-economy | 1.0.0 | EARTH | Efficiency | [] | Minimal diffs, JIT file reading, RCA on debug, no filler text. |
| 3 | deep-planning | 1.0.0 | FIRE | Planning | [] | Architect Mode: Phase 1 research, Phase 2 implementation_plan.md. |
| 4 | spec-driven-development | 1.0.0 | FIRE | Planning | [] | Spec-first development for complex tasks (>=4 files or new component). Cross-ref: mcp-mastery. |
| 5 | confidence-scoring | 1.0.0 | WATER | Planning | [] | 5-point binary checklist before writing code. |
| 6 | deterministic-verification | 1.0.0 | EARTH | Quality | [] | No "vibe coding" -- mandatory tests and walkthrough.md. |
| 7 | anti-loop-protocol | 1.0.0 | WATER | Resilience | [] | Max 2 attempts per bug. Stop and escalate after. |
| 8 | auto-rollback-healing | 1.0.0 | WATER | Resilience | [agentic-checkpointing] | Auto git-revert on failed attempts. Dead-Letter Queue for review. |
| 9 | agentic-checkpointing | 1.0.0 | EARTH | Resilience | [] | Safe git commits before risky changes. |
| 10 | security-guard | 1.0.0 | WATER | Security | [] | Blocks destructive commands (rm -rf, DROP TABLE, etc.). |
| 11 | prompt-injection-guard | 1.0.0 | WATER | Security | [] | Detects and blocks prompt injection from external sources. |
| 12 | immutable-core-directives | 1.0.0 | WATER | Security | [] | "Laws of Robotics" -- protects security-critical skills from modification. |
| 13 | zero-trust-orchestration | 1.0.0 | EARTH | Security | [] | Validates sub-agent outputs before merging. |
| 14 | agent-orchestration | 1.0.0 | FIRE | Swarm | [] | Delegates tasks to sub-agents. |
| 15 | swarm-context-isolation | 1.0.0 | EARTH | Swarm | [] | Least-privilege context for each sub-agent. |
| 16 | structured-swarm-artifacts | 1.0.0 | EARTH | Swarm | [] | JSON protocols for inter-agent communication. |
| 17 | parallel-tdd-swarm | 1.0.0 | FIRE | Swarm | [] | Parallel code and test writing with Staging Isolation. |
| 18 | agent-pool-manager | 1.0.0 | EARTH | Swarm | [] | Manages agent lifecycle, concurrency limits, and pool health. |
| 19 | session-lifecycle-manager | 1.0.0 | WIND | State | [] | Session startup, resume, teardown, and background-daemon coordination. |
| 20 | knowledge-persistence | 1.0.0 | EARTH | State | [] | Long-term memory between sessions (.ultracode/memory.md). |
| 21 | stateful-rehydration | 1.0.0 | EARTH | State | [unified-state-persistence] | Restores prior session state from persisted snapshots. |
| 22 | unified-state-persistence | 1.0.0 | EARTH | State | [] | Single source of truth for all agent state persistence. |
| 23 | working-memory-state | 1.0.0 | EARTH | State | [unified-state-persistence] | Active-session working memory with TTL-based rotation. |
| 24 | workspace-auto-config | 1.0.0 | EARTH | State | [] | Automatic workspace setup and configuration detection. |
| 25 | environment-doctor | 1.0.0 | EARTH | Resilience | [] | Pre-flight environment diagnostics (servers, ports, configs). |
| 26 | background-daemon | 1.0.0 | FIRE | Resilience | [] | Background monitoring via scheduling tools. CI/CD forbidden. |
| 27 | mcp-mastery | 2.1.0 | WIND | Efficiency | [] | MCP-first architecture: business-domain catalog, never-write-parsers rule, user-instruction protocol. Includes mcp-business-integrations enhancement with chain-context tagging and OSINT consumption path. |
| 28 | recursive-self-improvement | 1.0.0 | EARTH | Self-Evolution | [] | Agent can improve its own skills (user-approved). |
| 29 | cloud-deployment | 1.0.0 | WIND | Infrastructure | [] | Dockerfile, docker-compose, server init scripts. Security-guard gated. |
| 30 | interactive-interview-mode | 1.0.0 | WIND | Planning | [] | 5-round interview protocol for vague/greenfield requests. |
| 31 | skill-hunter | 1.0.0 | WIND | Efficiency | [] | Exhaustive registry search before custom code. |
| 32 | native-tools-mapping | 1.0.0 | WIND | Efficiency | [] | Maps native agent tools to MCP servers for capability discovery. |
| 33 | tool-translation-layer | 1.0.0 | WIND | Efficiency | [] | Translates between agent tool formats and MCP tool schemas. |
| 34 | ponytail-yagni | 1.0.0 | EARTH | Efficiency | [] | Install only needed MCP servers; defer non-critical integrations. |
| 35 | context-engineering | 1.0.0 | EARTH | Efficiency | [] | Prompt composition and context window optimization strategies. |
| 36 | context-rotation | 1.0.0 | EARTH | Efficiency | [knowledge-persistence] | Rotates stale context out; keeps active context lean. |
| 37 | context-budget-manager | 1.0.0 | EARTH | Efficiency | [token-economy] | Tracks and enforces token budgets per operation. |
| 38 | cryptographic-integrity-monitor | 1.0.0 | WATER | Security | [] | Hash-chain verification of all inter-agent data flows. |
| 39 | injection-sanitizer | 1.0.0 | WATER | Security | [] | Sanitizes external inputs before they reach agent decision loops. |
| 40 | supply-chain-verifier | 1.0.0 | WATER | Security | [] | Validates external dependencies, packages, and MCP server integrity. |
| 41 | browser-use-agent | 1.0.0 | WIND | Reconnaissance | [] | Physical browser automation (Puppeteer/Playwright) with self-healing selectors, session replay, and login wall traversal. |
| 42 | web-devourer | 1.0.0 | WIND | Reconnaissance | [] | Bulk site crawling and LLM-optimized content extraction into structured knowledge bases. |
| 43 | osint-detectives | 1.0.0 | WATER | Intelligence | [] | Cross-platform entity resolution, social network graph construction, and intelligence report generation. |
| 44 | magic-deduction-swarm | 1.0.0 | WATER | Intelligence | [] | Multi-agent adversarial debate protocol with confidence-weighted voting and minority report preservation. |
| 45 | anomaly-lens | 1.0.0 | WATER | Security Operations | [] | Live metric stream anomaly detection with multi-metric correlation and baseline auto-calibration. |
| 46 | seek-and-destroy | 1.0.0 | WATER | Security Operations | [] | Automated vulnerability scanning and auto-patch generation for OWN CODE only (defensive). |
| 47 | legal-expert-swarm | 1.0.0 | EARTH | Industry Expertise | [] | 3-agent adversarial court (Judge/Prosecutor/Lawyer) for Canadian law analysis and contract review. |
| 48 | real-estate-agent | 1.0.0 | EARTH | Industry Expertise | [] | Property audit, cadastral analysis, zoning analysis, and comparable sales research via land registries. |
| 49 | finance-accounting-agent | 1.0.0 | EARTH | Industry Expertise | [] | P&L generation, tax analysis, cash flow forecasting, and government contract audit with audit trail construction. |
| 50 | omni-profiler-swarm | 1.0.0 | EARTH | Profiling | [agent-orchestration, swarm-context-isolation, structured-swarm-artifacts] | **NEW v11.2.0** -- 5-agent behavioral profiling swarm (psych, financial, social, temporal, geospatial) producing unified subject dossiers. |
| 51 | forensic-audio-transcriber | 1.0.0 | EARTH | Forensics | [mcp-mastery, cryptographic-integrity-monitor, token-economy] | **NEW v11.2.0** -- Multi-engine audio forensic analysis with speaker diarization, tampering detection, voice biometrics, and chain-of-custody transcripts. |
| 52 | clinical-diagnostician | 1.0.0 | EARTH | Healthcare | [magic-deduction-swarm, confidence-scoring, knowledge-persistence] | **NEW v11.2.0** -- Multi-specialist differential diagnosis swarm with evidence-based reasoning, Bayesian updating, and ranked diagnostic hypotheses. |
| 53 | financial-forensics-agent | 2.0.0 | EARTH | Forensics | [finance-accounting-agent, magic-deduction-swarm, cryptographic-integrity-monitor, deterministic-verification] | **ENHANCED v11.2.0** -- Tax Sovereign Boost: detects tax evasion patterns, sovereign citizen schemes, offshore concealment structures, and money-trail reconstruction with adversarial forensic review. |
| 54 | session-state-management | 1.0.0 | EARTH | State | [] | Working memory across sessions: read, rehydrate, rotate. || 55 | syndicate-router | 1.0.0 | EARTH | Swarm | [agent-orchestration, swarm-context-isolation] | **NEW v11.3.0** -- Advanced routing protocol for O(log N) navigation through the Syndicate-30000 hierarchy (75 Macro-Sectors). |
| 56 | preflight-solution-hunter | 1.0.0 | WIND | Efficiency | [skill-hunter] | **NEW v11.3.0** -- Mandates pre-flight internet search for ready-made MCP servers and open-source packages before writing code from scratch. |
| 57 | trading-terminal-blueprint | 1.0.0 | EARTH | Industry Expertise | [] | **NEW v11.3.0** -- Architectural blueprint for building advanced trading terminals without paid subscriptions (TradingView alternative). |
| 58 | omni-parser-extractor | 1.0.0 | WIND | Reconnaissance | [preflight-solution-hunter] | **NEW v11.3.0** -- Advanced data extraction tools for websites, social media, and audio/video files. |
| 59 | cline-memory-bank-sync | 1.0.0 | EARTH | State | [session-state-management] | **NEW v11.3.0** -- Implements the Cline Memory Bank pattern for maintaining persistent cross-session context via Markdown files. |

## Category Summary

| Category | Count | Skills |
| --- | --- | --- |
| Security | 7 | security-guard, prompt-injection-guard, immutable-core-directives, zero-trust-orchestration, cryptographic-integrity-monitor, injection-sanitizer, supply-chain-verifier |
| Resilience | 5 | cicd-mode, anti-loop-protocol, auto-rollback-healing, agentic-checkpointing, environment-doctor |
| Planning | 4 | deep-planning, spec-driven-development, confidence-scoring, interactive-interview-mode |
| Quality | 1 | deterministic-verification |
| Efficiency | 9 | token-economy, mcp-mastery, skill-hunter, native-tools-mapping, tool-translation-layer, ponytail-yagni, context-engineering, context-rotation, context-budget-manager, preflight-solution-hunter |
| Swarm | 6 | agent-orchestration, swarm-context-isolation, structured-swarm-artifacts, parallel-tdd-swarm, agent-pool-manager, syndicate-router |
| State | 7 | session-lifecycle-manager, knowledge-persistence, stateful-rehydration, unified-state-persistence, working-memory-state, workspace-auto-config, session-state-management, cline-memory-bank-sync |
| Self-Evolution | 1 | recursive-self-improvement |
| Infrastructure | 2 | background-daemon, cloud-deployment |
| Reconnaissance | 3 | browser-use-agent, web-devourer, omni-parser-extractor |
| Intelligence | 2 | osint-detectives, magic-deduction-swarm |
| Security Operations | 2 | anomaly-lens, seek-and-destroy |
| Industry Expertise | 4 | legal-expert-swarm, real-estate-agent, finance-accounting-agent, trading-terminal-blueprint |
| Profiling | 1 | omni-profiler-swarm |
| Forensics | 2 | forensic-audio-transcriber, financial-forensics-agent |
| Healthcare | 1 | clinical-diagnostician |

## Council Distribution

| Council | Elder | Domain | Count | Skills |
| --- | --- | --- | --- | --- |
| FIRE | Elder of Fire | Will & Execution | 5 | deep-planning, spec-driven-development, agent-orchestration, parallel-tdd-swarm, background-daemon |
| WATER | Elder of Water | Wisdom & Caution | 14 | cicd-mode, anti-loop-protocol, auto-rollback-healing, security-guard, prompt-injection-guard, immutable-core-directives, confidence-scoring, cryptographic-integrity-monitor, injection-sanitizer, supply-chain-verifier, osint-detectives, magic-deduction-swarm, anomaly-lens, seek-and-destroy |
| WIND | Elder of Wind | Harmony & Connection | 11 | mcp-mastery, session-lifecycle-manager, cloud-deployment, interactive-interview-mode, skill-hunter, native-tools-mapping, tool-translation-layer, browser-use-agent, web-devourer, preflight-solution-hunter, omni-parser-extractor |
| EARTH | Elder of Earth | Crystal & Structure | 29 | token-economy, deterministic-verification, agentic-checkpointing, zero-trust-orchestration, swarm-context-isolation, structured-swarm-artifacts, agent-pool-manager, knowledge-persistence, stateful-rehydration, unified-state-persistence, working-memory-state, workspace-auto-config, environment-doctor, recursive-self-improvement, ponytail-yagni, context-engineering, context-rotation, context-budget-manager, legal-expert-swarm, real-estate-agent, finance-accounting-agent, session-state-management, omni-profiler-swarm, forensic-audio-transcriber, clinical-diagnostician, financial-forensics-agent, syndicate-router, trading-terminal-blueprint, cline-memory-bank-sync |

Total: 59 skills across 4 councils (FIRE: 5, WATER: 14, WIND: 11, EARTH: 29)

## v11.3.0 Changelog -- THE SYNDICATE EXPANSION

### New Skills (1)

- **syndicate-router** (v1.0.0): Advanced routing protocol for navigating the Syndicate-30000 hierarchy. Prevents context window collapse by enforcing O(log N) tree traversal (Macro-Sector -> Micro-Domain -> Skill). Council: EARTH.
- **preflight-solution-hunter** (v1.0.0): Pre-flight mandatory search protocol. Searches Top-100 IT and AI platforms for existing MCP servers and ready code before starting implementation from scratch. Council: WIND.
- **trading-terminal-blueprint** (v1.0.0): Architectural blueprint for building advanced trading terminals with free premium indicators (FVG, Volume Profile, unlimited layouts) and zero-cost data feeds. Council: EARTH.
- **omni-parser-extractor** (v1.0.0): Advanced tools integration (Crawl4AI, Apify, yt-dlp, Whisper) for parsing JS websites, closed social media platforms, and transcribing media. Council: WIND.
- **cline-memory-bank-sync** (v1.0.0): Official integration of the Cline Memory Bank architecture, enforcing persistent context documentation via projectbrief, activeContext, and systemPatterns. Council: EARTH.

## v11.2.0 Changelog -- ELDER OF EARTH

### New Skills (3)

- **omni-profiler-swarm** (v1.0.0): Five-dimensional behavioral profiling swarm producing unified subject dossiers. Council: EARTH.
- **forensic-audio-transcriber** (v1.0.0): Multi-engine audio forensic analysis with speaker diarization, tampering detection, voice biometrics, and chain-of-custody transcripts. Council: EARTH.
- **clinical-diagnostician** (v1.0.0): Multi-specialist differential diagnosis swarm with evidence-based reasoning and Bayesian diagnostic updating. Council: EARTH.

### Enhanced Skills (1)

- **financial-forensics-agent** (v1.0.0 -> v2.0.0): Tax Sovereign Boost -- adds detection of tax evasion patterns, sovereign citizen/freeman schemes, offshore concealment structures, digital asset forensics, and GST/HST carousel fraud detection. Enhanced with 3-agent adversarial forensic review panel and referral-ready report generation for CRA/IRS/FINTRAC.

### Domain Summary

All 4 additions strengthen the EARTH council (Crystal & Structure), expanding from 22 to 26 earth-domain skills. The Elder of Earth now governs profiling, forensics, healthcare diagnostics, and financial investigation capabilities -- anchoring the syndicate's analytical depth in evidence-based, structurally rigorous methodologies.
