---
tags:
  - advanced-programming
  - flashcards
qard-deck: "Advanced Programming"
qard-topic: "FP 15 — Interactive Fiction And Inform 7"
---

# FP 15 — Interactive Fiction And Inform 7

**Source note:** [Interactive Fiction And Inform 7](../../FP/15_Interactive_Fiction.md)

Exam recall cards: definitions, mechanisms, comparisons and key facts. Source-specific examples are left out.

## Contents

- [[#Core Content|Core Content]]
  - [[#Interactive Fiction|Interactive Fiction]]
  - [[#Inform 7|Inform 7]]
  - [[#Design|Design]]

## Core Content

### Interactive Fiction

<!-- qard-id: ap-448d0fe4f2f281cac8d9 -->
> [!qard]- What is interactive fiction?
> Software where players control a character with natural-language text commands; text in, mostly text out, focused on narrative and puzzles.

<!-- qard-id: ap-ea2b12db33ca109f0015 -->
> [!qard]- What form do IF input and output take?
> Input: simple imperative sentences. Output: present tense, second person.

<!-- qard-id: ap-8f418c55231be2aac573 -->
> [!qard]- Name three flavours of interactive fiction.
> Text adventures, MUDs (multi-user dungeons), Choose Your Own Adventure books.

### Inform 7

<!-- qard-id: ap-41a23a218b330da3ab47 -->
> [!qard]- What is Inform 7?
> A declarative, natural-language domain-specific language and IDE for writing interactive fiction.

<!-- qard-id: ap-d6952adcedfec9e9e469 -->
> [!qard]- What is Graham Nelson's design philosophy for Inform 7?
> "The natural language in which to write interactive fiction is natural language" — readable by a casual reader, economical, modelled on books.

<!-- qard-id: ap-989c1655adf5ae955f61 -->
> [!qard]- What are the two parts of an Inform 7 program?
> Assertions creating things and starting conditions, and rules modifying state and behaviour.

<!-- qard-id: ap-662d07949e34000cc281 -->
> [!qard]- How are maps represented in Inform 7?
> As graphs: rooms are nodes and connections (compass directions, up/down, inside/outside) are edges.

<!-- qard-id: ap-540b0cb2c423ac305881 -->
> [!qard]- Are Inform 7 connections symmetric?
> By default yes; they can be made asymmetric, or one-way using `nowhere`.

<!-- qard-id: ap-5acc9234ab0dd1781bdf -->
> [!qard]- What is a region?
> A named group of rooms; regions may nest but not overlap, and rules can target them.

<!-- qard-id: ap-fbb3c5da9ea5e53753b6 -->
> [!qard]- What is a kind in Inform 7?
> An object type such as room, thing, container, supporter or person — often inferred from the text.

<!-- qard-id: ap-01c9b6652d52a5ccb2d3 -->
> [!qard]- What is an either/or property?
> A two-valued property like open/closed, lockable, portable/fixed in place.

<!-- qard-id: ap-6fd18b29b368ef544259 -->
> [!qard]- What three descriptions can an object have?
> Its first-appearance text, its examine description, and its printed (inventory) name.

<!-- qard-id: ap-c7bcbf2b0aa0872ad003 -->
> [!qard]- What defaults do doors have?
> Fixed in place, closed and openable; they can be lockable with a matching key.

<!-- qard-id: ap-04f567937caa46bf9fe4 -->
> [!qard]- What is a scene?
> A stretch of play with a begin condition, an end condition and rules that run when it ends.

### Design

<!-- qard-id: ap-97445ac9fdcdb6eb6e52 -->
> [!qard]- What is the Player's Bill of Rights?
> Not to be killed without warning; no horribly unclear hints; win without past lives or knowledge of future events; not closed off without warning.

<!-- qard-id: ap-ddc9f56bec5d96284a4a -->
> [!qard]- Give three tips for designing interactive fiction.
> Avoid linearity, keep internal consistency, be descriptive but not excessive (and beware exponential content growth).

<!-- qard-id: ap-3fddefd8f0d2a790b739 -->
> [!qard]- Name six common interactive-fiction commands.
> LOOK (L), EXAMINE (X), TAKE/DROP, INVENTORY (I), OPEN/CLOSE, UNLOCK…WITH (also compass moves N/S/E/W, U/D, and WAIT (Z)).

<!-- qard-id: ap-3ad88f7c6711fead7e05 -->
> [!qard]- What are devices, vehicles and people in Inform 7?
> Devices switch on/off; vehicles are enterable containers (optionally pushable); people (men, women, animals) are kinds of person.
