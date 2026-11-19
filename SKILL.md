---
name: farsi-tech-docs
description: Polish Persian tech documents for natural terminology.
version: 0.1.0
author: Ebrahim, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [persian, farsi, technical-writing, rtl, terminology, docx]
    related_skills: [docx, ssis-package-technical-review]
---

# Persian Tech Documents Skill

Write and polish Persian/Farsi technical documents — reports, design docs, wikis,
READMEs, and Word deliverables — so they read as natural Persian and match how
Persian tech writers actually choose terms (keep English, use Persian, or write
`فارسی (English)` on first mention). This skill does not replace subject-matter
review and does not translate English prose word-for-word or force Persian
equivalents for terms practitioners keep in English.

## When to Use

- The user asks for a Persian/Farsi technical document, report, wiki page, README, or design doc.
- An existing Persian tech text reads stiff, literal, or over-translated (English jargon replaced by uncommon Persian).
- The document covers software, data, infrastructure, databases, cloud, or AI/ML topics.
- The user names Persian tech references (faradars.org, maktabkhooneh.org, nikamooz.com) as terminology sources.
- Not for: marketing copy, literary translation, or English AI-ism removal (`avoid-ai-writing`).

## Core Rules

1. **Write Persian directly.** Do not translate English sentence by sentence. Restructure for Persian: short sentences, active voice, one idea per sentence, definition at first mention.
2. **Term usage (not translation).** Match how Persian tech writers use terms on faradars.org, maktabkhooneh.org, nikamooz.com (see `references/term-usage.md`).
   - Check actual usage first: English-only, Persian-only, or bilingual `فارسی (English)` on first mention.
   - Keep English when practitioners keep it: branded architectures, acronyms, protocol/jargon terms (e.g. `Data Lakehouse`, `ETL`, `CDC`, `Schema-on-Read`, `watermark`, `checkpoint`, `exactly-once`).
   - Use established Persian when it is standard: `انبار داده`, `دریاچه داده`, `مهندسی داده`, `متاداده`, `پردازش دسته‌ای`, `پردازش جریان داده`.
   - First mention of important terms: prefer bilingual form `فارسی (English)` or `English (توضیح کوتاه فارسی)` if readers may need it; then use one consistent short form.
   - Never invent a Persian equivalent for a term kept in English by sources. Never force English for a term with stable Persian usage.
   - Keep product names, code, commands, paths, identifiers, URLs, and log messages in English LTR.
   - Use `references/persian-tech-glossary.md` only as candidate forms, not proof of usage.
3. **Language hygiene.**
   - Fix clear Arabic typing forms: `ى→ی`, `ك→ک`, `ة→ه`, `ؤ→و`. Treat `أ/إ` cautiously: fold only when the Persian form is established (for example `إنشاء` → `ایجاد`); keep standard Persian spellings such as `تأخیر`، `مسئله`، `سؤال`. Strip tatweel and Arabic harakat.
   - Normalize ZWNJ: keep it in compounds such as `می‌شود`, `نیمه‌ساختاریافته`, `کلان‌داده`, `دریاچه‌داده`; remove it where it incorrectly splits a word. Never fold `آ` (U+0622) into `ا`.
   - Persian punctuation: `،` `؛` `؟` `«»`. Use Persian digits in prose (`۰۱۲۳۴۵۶۷۸۹`); keep ASCII digits in code, config keys, versions, and SQL literals.
4. **RTL formatting.** For `.docx`, use the `docx` skill and apply the RTL OOXML recipe from `ssis-package-technical-review`: `w:bidi` per paragraph/run, `w:bidiVisual` for tables, right alignment, Tahoma font. Keep code blocks and identifiers LTR.
5. **Structure.** Title, one-paragraph summary, prerequisites, numbered steps, notes/warnings, references. Use tables for term mappings and comparisons. Use «نکته»، «هشدار»، «پیش‌نیاز».
6. **Consistency.** One chosen form per term across the whole document. Do not alternate between `انبار داده` and `انبارداده`, or between `کوئری` and `پرس‌وجو`, unless the glossary says both are valid in different contexts.

## Terminology Sources

Use in this order:

1. `references/term-usage.md` — observed conventions (English vs Persian vs bilingual) from Persian tech sites.
2. `references/persian-tech-glossary.md` — candidate Persian forms; verify against real usage before choosing.
3. `references/style-examples.md` — before/after samples for translationese, ZWNJ, and term consistency.
4. Live usage evidence for contested or new terms. Query patterns:
   - `<English term> site:nikamooz.com`
   - `<English term> site:faradars.org`
   - `<English term> site:maktabkhooneh.org`
   - `<candidate Persian term> site:nikamooz.com`
   If search returns nothing useful, `web_extract` a relevant course/article page and read actual usage in headings/body.
5. Decision rule: prefer the dominant observed form (2+ examples). If forms are mixed, use bilingual first mention then the dominant short form consistently. If no Persian usage exists, keep English (optionally with short Persian explanation). Record the chosen form and source/evidence in the document's term table.

## Procedure

1. **Classify.** Identify document type, audience, and output format. If `.docx`, load the `docx` skill. If the text contains SQL or code, mark code blocks LTR before editing.
2. **Inventory terms.** List every repeated English technical term in the source. Completion: the list covers all headings, table headers, and recurring nouns.
3. **Observe usage.** For each term, check `references/term-usage.md`; if not covered or uncertain, collect 2-3 real usages from nikamooz/faradars/maktabkhooneh (`web_search`/`web_extract`). Completion: every term labeled English/Persian/bilingual with evidence or "keep English, no Persian usage found".
4. **Assign forms.** Choose one form per term for this document (bilingual first mention allowed). Completion: term table exists with chosen form + rationale/evidence for contested terms.
5. **Rewrite.** Write the Persian text directly, using the chosen forms. Completion: no forced translation of English-kept terms; no unnecessary English for standard Persian terms; bilingual terms introduced once.
6. **Hygiene pass.** Apply glyph folds, ZWNJ, punctuation, and digit rules. Completion: no Arabic glyphs, no double ZWNJ, no mixed digit systems in one numeric context.
7. **Format.** For `.docx`, apply RTL OOXML and verify code blocks stay LTR. Completion: paragraphs right-aligned, tables `bidiVisual`, code paragraphs left-aligned.
8. **Verify.** Read the output back. Completion: term usage matches observed convention, terminology is consistent, sample paragraphs read naturally, and verification checks below pass.

## Pitfalls

- Do not treat the glossary as ground truth for usage; it lists candidate Persian forms. Real usage decides.
- Do not invent Persian for terms sources keep in English: `Data Lakehouse`, `CDC`, `ETL/ELT`, `Schema-on-Read/Write`, `Event Sourcing`, `Data Pipeline`, `watermark`, `checkpoint`, `exactly-once`, `upsert`.
- Do not force English for terms with stable Persian usage: `انبار داده`, `دریاچه داده`, `متاداده`, `مهندسی داده`, `پردازش دسته‌ای`, `پردازش جریان داده`.
- Do not repeat bilingual parentheticals every sentence; introduce once, then stay consistent.
- Do not translate product names: Kafka, Flink, Iceberg, Trino, Keycloak, Spark, Hadoop, Delta Lake.
- Do not remove ZWNJ from `می‌شود` or `نیمه‌ساختاریافته`; do not insert it inside a word.
- Do not mix English and Persian digits in the same number, sentence, or table column.
- Persian text pasted into terminals or SQL clients can be corrupted; write from a file, never from interactive paste.
- `python-docx` has no RTL switch; use raw OOXML as in `ssis-package-technical-review`.
- Machine-translation tells: «با توجه به این که»، «از آنجا که»، «به منظور»، «در حالی که» overused; prefer shorter Persian connectives.

## Auto-Improvement Loop

Goal: improve term-usage understanding from real Persian tech documents over time (English vs Persian vs bilingual), not add translations.

Artifacts:
- `references/term-queue.md` — terms/domains to research next.
- `references/research-log.md` — append-only evidence (date, term, observed form, usage type, source URL, snippet).
- `references/term-usage.md` — current conventions; update only with clear evidence (prefer 2+ examples).

Manual/agent run:
1. Pick 3-5 unchecked queue items (or terms encountered in real work).
2. Collect evidence from nikamooz/faradars/maktabkhooneh via `web_search` + `web_extract`; read actual usage, not dictionary translations.
3. Append evidence rows to `research-log.md`; update `term-usage.md` when convention is clear; mark queue items done.
4. If a term appears often in user work, promote it to queue and research soon.

Scheduled run: optional cron job `farsi-tech-usage-research` (weekly) researches queue items and patches these references. Review its report before trusting new conventions broadly.

## Verification

- Run `python scripts/fa_lint.py <file>` on extracted prose or Markdown. It skips fenced code blocks and reports Arabic glyphs, inverted hamza, double ZWNJ, missing ZWNJ in common compounds, mixed digits, and replacement characters as JSON. Exit code 1 means errors. For `.docx`, extract text first with `docx_read.py --text` and lint that output.
- `search_files` the produced text for `[ىكؤ]` and `ة`; expect no matches. Check `إ` only where `ا` is expected; do not flag `تأخیر`، `مسئله`، `سؤال`.
- Check that ZWNJ count is greater than zero and no double ZWNJ exists.
- For `.docx`: run `docx_read.py --text` and confirm Persian strings render and code blocks remain LTR.
- Term consistency: every glossary term appears in its chosen form; every English jargon term has a first-mention explanation.
- Read three consecutive paragraphs aloud; if a sentence needs a second read, rewrite it shorter.
