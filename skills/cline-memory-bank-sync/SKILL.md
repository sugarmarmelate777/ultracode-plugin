---
name: Cline Memory Bank Sync (Self-Documenting Context)
description: Implements the "Cline Memory Bank" pattern, enabling agents to maintain persistent project context across sessions through a structured Markdown memory folder.
depends_on: [session-state-management, structured-swarm-artifacts]
---

# Cline Memory Bank Sync

You are an expert agent equipped with the **Memory Bank** capability, identical to the pattern used by Cline. Because agent sessions reset (or context windows get cleared to save tokens), you must rely ENTIRELY on your Memory Bank to understand the project and continue work effectively.

## Memory Bank Structure
The Memory Bank consists of required core files in a `memory-bank/` directory at the project root. If this directory exists, you MUST read all of its files at the start of your task.

### Core Files (Required)
1. `projectbrief.md` - Foundation document that shapes all other files. Defines core requirements and goals.
2. `productContext.md` - Why this project exists, problems it solves, user experience goals.
3. `activeContext.md` - Current work focus, recent changes, next steps, active decisions.
4. `systemPatterns.md` - System architecture, key technical decisions, design patterns in use.
5. `techContext.md` - Technologies used, development setup, technical constraints.
6. `progress.md` - What works, what's left to build, current status, known issues.

### Project Intelligence (.clinerules)
The `.clinerules` file (or `.cursorrules`) is your learning journal. It captures important patterns, preferences, and project intelligence. Read it to understand how the user wants you to behave in this specific repository.

## Core Workflows

### 1. Initialization ("initialize memory bank")
If the user asks you to initialize the memory bank, you should:
- Create the `memory-bank/` directory.
- Create the 6 core files based on your current understanding of the project.
- *Alternatively, run the `init_memory_bank.ps1` script if available in the Ultracode tools.*

### 2. Plan Mode (Start of Task)
1. **Read Memory Bank:** If `memory-bank/` exists, read `projectbrief.md`, `activeContext.md`, and `systemPatterns.md`.
2. **Create Plan:** Base your strategy strictly on the established patterns and the current active context.

### 3. Act Mode (Executing Task)
1. **Update Documentation:** When you implement significant changes, discover new patterns, or finish a milestone, you MUST update `activeContext.md` and `progress.md`.
2. **Update Rules:** If you learn a new preference or architectural constraint, document it in `systemPatterns.md` or `.clinerules`.

### 4. Explicit Update ("update memory bank")
When triggered by the command "update memory bank", you MUST review ALL memory bank files and update them to accurately reflect the current state of the codebase. Focus particularly on `activeContext.md` and `progress.md`.

REMEMBER: The Memory Bank is your only link to previous work. It must be maintained with precision and clarity. Always update it when you hit a major checkpoint!
