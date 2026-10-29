---
tags:
  - vault-support
---

# Vault Guide

This vault is organized around source-driven course notes. Use this file as the top-level orientation note when working in Obsidian or asking Codex to generate new study material.

## Folder Map

| Folder | Purpose |
|---|---|
| `Sources/` | Original PDFs, slide decks, archives, and other uploaded source material. Do not edit these when generating notes. |
| `Courses/` | Generated and maintained Markdown study notes, study aids, flashcards, formula sheets, and mock exams. |
| `Templates/` | Reusable note templates for new generated notes. |
| `_agents/` | Codex agent instructions for generating notes and slides. |
| `_skills/` | Vault-specific Codex skills and note-taking standards. |
| `diagrams/` | SVG diagrams grouped by course, optional unit, and lecture; shared image assets referenced by notes. |
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

Every source-backed note should preserve the standard section order:

1. Topic header
2. Contents with clickable links to the note's sections and Core Content subsections
3. Core Content

Do not include dedicated Summary / Cheat Sheet, Practice Questions, Worked Examples, or Common Mistakes / Gotchas sections. Source examples, essential qualifications, and algorithm mechanics belong beside the relevant concept in Core Content.

All future notes must also follow the readable writing style in `_skills/NOTE_TAKING_PHILOSOPHY.md`: short paragraphs, direct explanations, numbered processes, bullets for properties, and tables for comparisons. Use the existing Networks, Operating Systems, and Automated Planning notes as models. Keep source details in the note header rather than narrating slides in the body.

## Graph and Diagram Standard

Whenever creating or recreating a graph or diagram, read and apply `_skills/svg-graph-creation/SKILL.md`. Hand-authored SVG is the default for both source visuals and existing note diagrams, unless the user explicitly requests another format. Store SVGs under `diagrams/[Course]/[Optional Unit]/[NoteName]/`. Embed each SVG beside its explanation with a relative image link and a short caption. Use the approved coloured style in that skill, with Introduction I as the reference: meaningful accents, subdued dark fills, and layouts suited to the concept. Verify every render for legibility and faithful technical relationships.

## Course Navigation

Use course folders and Obsidian search to find notes. Do not create or maintain course INDEX files unless explicitly requested by the user.

Every study note must have its course tag in the YAML `tags` list at the top of the file, including study aids, mock exams, and flashcard decks:

| Course | Tag |
|---|---|
| CSC3001F Networks | `networks` |
| CSC3002F Operating Systems | `operating-systems` |
| CSC3003S Advanced Programming | `advanced-programming` |
| CSC3041F Automated Planning | `automated-planning` |
| CSC3043S Reasoning in AI | `reasoning-in-ai` |
| CSC3044S AI Systems, including its Qard files | `ai-systems` |

Vault guides, templates, agent instructions, and skill instructions use `vault-support`. When generating a study note from a template, replace the template's `vault-support` tag with the appropriate course tag. Preserve any other existing tags and metadata. Keep Tags enabled in graph settings to display course connections.

All Markdown file links should be filesystem-relative, not vault-absolute. Use Obsidian heading links such as `[[#Core Content|Core Content]]` for section navigation.

## Maintenance Checks

Run this after large note-generation sessions or structural edits:

```sh
node .tools/audit-vault-links.js
```

The audit checks Markdown links using filesystem-relative resolution and reports broken links.
