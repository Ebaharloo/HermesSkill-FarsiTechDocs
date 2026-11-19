# HermesSkill-FarsiTechDocs

A [Hermes Agent](https://hermes-agent.nousresearch.com/docs) skill for writing and
polishing **Persian/Farsi technical documents** — reports, design docs, wiki pages,
READMEs and Word deliverables — so they read as natural Persian and use terms the
way Persian tech writers actually use them.

It is a term-usage skill, not a translator. It decides per term whether to keep
English, use Persian, or write `فارسی (English)` on first mention, and it never
invents Persian equivalents for jargon practitioners keep in English.

## What it does

- **Term usage over translation.** Evidence-based choices from real Persian tech
  sources (nikamooz.com, faradars.org, maktabkhooneh.org), recorded in a term table.
- **Keeps English** for `Data Lakehouse`, `ETL`, `CDC`, `Schema-on-Read`, `watermark`,
  `checkpoint`, `exactly-once`, `upsert`, product names (Kafka, Flink, Iceberg, Trino, Keycloak).
- **Uses standard Persian** for `انبار داده`, `دریاچه داده`, `متاداده`, `مهندسی داده`,
  `پردازش دسته‌ای`, `پردازش جریان داده`.
- **Language hygiene.** Arabic glyph folds (`ى→ی`, `ك→ک`, `ة→ه`), ZWNJ normalization,
  Persian punctuation (`، ؛ ؟ «»`) and Persian digits in prose only.
- **RTL `.docx`.** `w:bidi` paragraphs, `w:bidiVisual` tables, Tahoma, code blocks kept LTR.
- **Self-improving glossary.** A queue of terms to research, an append-only evidence log,
  and a conventions file updated only on 2+ observed examples.
- **Linter.** `scripts/fa_lint.py` reports Arabic glyphs, inverted hamza, double ZWNJ,
  missing ZWNJ in common compounds, mixed digit systems and replacement characters as JSON.

## Contents

```
SKILL.md                              main instructions (rules, procedure, pitfalls, verification)
references/term-usage.md              observed English vs Persian vs bilingual conventions
references/persian-tech-glossary.md   candidate Persian forms (not proof of usage)
references/style-examples.md          before/after samples: translationese, ZWNJ, consistency
references/term-queue.md              terms/domains to research next
references/research-log.md            append-only evidence log (term, form, source, snippet)
scripts/fa_lint.py                    Persian text linter, JSON output, exit 1 on errors
```

## Install

Hermes loads skills from its skills directory. Copy the folder and keep `SKILL.md`
at the top level of a directory named `farsi-tech-docs`:

```bash
git clone https://github.com/fireproof-e/HermesSkill-FarsiTechDocs.git
cp -r HermesSkill-FarsiTechDocs "$LOCALAPPDATA/hermes/skills/writing/farsi-tech-docs"   # Windows
# cp -r HermesSkill-FarsiTechDocs ~/.hermes/skills/writing/farsi-tech-docs              # Linux/macOS
```

Then `skill_view(name='farsi-tech-docs')` in Hermes, or just ask for a Persian
technical document — the skill's description makes it load on its own.

## Usage

Ask for the document in Persian or English, e.g.:

- «این گزارش فنی را به فارسی روان بازنویسی کن»
- "Write a Persian design doc for this Flink pipeline."
- "Polish this Persian README — it reads like machine translation."

For `.docx` output the skill delegates formatting to the `docx` skill and applies
the RTL OOXML recipe.

## Lint a document

```bash
python scripts/fa_lint.py path/to/doc.md
```

Output is JSON with a list of findings and their line numbers. Exit code `1` means
errors (Arabic glyphs, double ZWNJ, mixed digits). Fenced code blocks are skipped.
For `.docx`, extract text first, then lint the extracted text.

## Extending the term corpus

1. Pick 3–5 items from `references/term-queue.md`.
2. Collect real usage from the Persian tech sites (`web_search` + `web_extract`) —
   read headings and body text, not dictionary translations.
3. Append evidence rows to `references/research-log.md`.
4. Update `references/term-usage.md` only when the convention is clear (2+ examples).

## Credits

Author: Ebrahim, with Hermes Agent. License: MIT — see [LICENSE](LICENSE).
