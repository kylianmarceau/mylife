# Vault Guide

This vault is organized around source-driven course notes. Use this file as the top-level orientation note when working in Obsidian or asking Codex to generate new study material.

## Folder Map

| Folder | Purpose |
|---|---|
| `Sources/` | Original PDFs, slide decks, archives, and other uploaded source material. Do not edit these when generating notes. |
| `Courses/` | Generated and maintained Markdown study notes, course indexes, study aids, flashcards, formula sheets, and mock exams. |
| `Templates/` | Reusable note templates for new generated notes. |
| `_agents/` | Codex agent instructions for generating notes and slides. |
| `_skills/` | Vault-specific Codex skills and note-taking standards. |
| `diagrams/` | Standalone diagrams and image assets referenced by notes. |
| `.obsidian/` | Obsidian configuration and plugin state. |

## Source-To-Note Rule

Each source file in `Sources/` should normally produce exactly one corresponding note file under `Courses/`, unless you explicitly ask Codex to combine sources.

Recommended path pattern:

```text
Sources/[Course]/[Optional Unit]/[Source File]
Courses/[Course]/[Optional Unit]/[Generated Note].md
```

Examples:

| Source | Note |
|---|---|
| `Sources/CSC3001F-networks/Transport_v2025.pptx` | `Courses/CSC3001F-networks/Lecture_Notes/Transport_Layer.md` |
| `Sources/CSC3002F-Operating Systems/ASLAM/Operating Systems 1 Ch1.pdf` | `Courses/CSC3002F-Operating Systems/ASLAM/01_Introduction_And_Computer_System_Structure.md` |
| `Sources/CSC3041F-Automated Planning/RL/1RL_3041F.pdf` | `Courses/CSC3041F-Automated Planning/Reinforcement Learning/01_RL_Introduction.md` |

## Note Standard

Generated course notes should follow:

1. `_skills/NOTE_TAKING_PHILOSOPHY.md`
2. `Templates/NOTE_TEMPLATE.md`
3. The relevant course `INDEX.md`

Every source-backed note should preserve the standard section order:

1. Topic header
2. Core Content
3. Worked Examples
4. Common Mistakes / Gotchas
5. Summary / Cheat Sheet
6. Practice Questions

## Course Index Standard

Every course folder should have an `INDEX.md` containing:

- Subject and source-folder metadata
- A linked table of contents with relative links
- Source coverage table mapping source files to generated notes
- Study aids, formula sheets, flashcards, and mock exams where relevant
- Suggested study order

All Markdown links should be filesystem-relative, not vault-absolute. This keeps notes valid in Obsidian, GitHub, and plain editors.

## Maintenance Checks

Run this after large note-generation sessions or structural edits:

```sh
node .tools/audit-vault-links.js
```

The audit checks Markdown links using filesystem-relative resolution and reports broken links.
