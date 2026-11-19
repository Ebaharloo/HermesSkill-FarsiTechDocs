# Persian Tech Term Usage (observed)

Goal: match how Persian tech writers actually write (faradars.org, maktabkhooneh.org, nikamooz.com), not literal translation. Rule of thumb: use established Persian for general concepts; keep English for branded/modern architecture terms, acronyms, and jargon readers expect in English.

## Observed patterns

- **First mention, bilingual:** `دریاچه داده (Data Lake)` or `داده خام (Raw Data)` or `پردازش بلادرنگ (Real-Time Processing)` — common in Nikamooz articles/titles; after that text may use Persian, English, or both.
- **English term dominant:** `معماری Data Lakehouse` (kept English in headings/body even when explained as ترکیب Data Lake و Data Warehouse).
- **Product/tool names always English:** Kafka, Spark, Airflow, Flink, Iceberg, Delta Lake, Trino, Keycloak, MongoDB, Elasticsearch, ClickHouse, NiFi, Hadoop, Debezium.
- **Acronyms/protocol names English:** ETL, ELT, OLAP, OLTP, ACID, CDC, SQL, NoSQL, BI, ML, AI, IoT, API, JSON, XML, S3, HDFS.
- **General concepts often Persian:** مهندسی داده، معماری داده، انبار داده، پایگاه داده، متاداده، داده خام، حکمرانی داده، کیفیت داده، مقیاس‌پذیری، دسترس‌پذیری، پردازش دسته‌ای، پردازش جریان داده، یکپارچه‌سازی داده.

## Usage guide

| Term / type | Preferred usage in Persian tech docs | Notes / evidence |
|---|---|---|
| Data Lake | `دریاچه داده (Data Lake)` first mention; later `دریاچه داده` or `Data Lake` acceptable if consistent | Nikamooz uses bilingual title and both forms in text |
| Data Warehouse | `انبار داده (Data Warehouse)` / `انبار داده` | common Persian form widely used |
| Data Lakehouse | keep `Data Lakehouse` (English); optionally explain once: `معماری Data Lakehouse (ترکیب دریاچه داده و انبار داده)` | Nikamooz keeps English term dominant |
| Data Swamp | `باتلاق داده (Data Swamp)` or `Data Swamp` | explain on first mention |
| Data Catalog | `کاتالوگ داده (Data Catalog)` | Nikamooz |
| Metadata | `متاداده` | common |
| Schema-on-Write / Schema-on-Read | keep English; can add Persian explanation in parens | Nikamooz uses English terms |
| ETL / ELT | keep English | universal |
| ACID / BASE | keep English | universal |
| OLAP / OLTP | keep English | universal |
| Big Data | `کلان‌داده` or `Big Data`; often mixed | maktabkhooneh title uses Big Data, text uses کلان‌داده/Big Data |
| Stream processing | `پردازش جریان داده` | maktabkhooneh course syllabus |
| Batch processing | `پردازش دسته‌ای` | common |
| Event Sourcing | keep `Event Sourcing` | maktabkhooneh keeps English |
| Data Pipeline | usually keep `Data Pipeline` / `پایپلاین داده` depending audience; explain if needed | sources often keep English |
| CDC | keep `CDC`; explain `Change Data Capture (ثبت تغییرات داده)` once if audience needs | rarely translated fully |
| Watermark / Checkpoint / Exactly-once / Upsert | keep English; add short Persian explanation at first mention when helpful | streaming jargon kept in English in practice |
| Backpressure | `فشار بازگشتی` seen in Faradars blog; keep English term in parens for clarity: `فشار بازگشتی (Backpressure)` | context-dependent |
| Real-time | `بلادرنگ` or `Real-time` | Nikamooz uses `پردازش بلادرنگ (Real-Time Processing)` |
| Object storage | `ذخیره‌سازی اشیا` | Nikamooz |
| Columnar / Row-based | `ستونی (Columnar)` / `سطری (Row-based)` | Nikamooz bilingual |
| Machine learning / Data science / AI | `یادگیری ماشین`، `علم داده`، `هوش مصنوعی` common; acronyms ML/AI also common | use audience-appropriate form consistently |

## How to decide for a new term

1. Search actual usage, not translation:
   - `site:nikamooz.com "<term>"`
   - `site:faradars.org "<term>"`
   - `site:maktabkhooneh.org "<term>"`
   - also try `site:nikamooz.com "<candidate Persian>"`
2. Read 2-3 real usages (`web_extract` article/course page). Check: English only? Persian only? bilingual `فارسی (English)`?
3. Pick the dominant convention. If mixed, prefer bilingual first mention then the dominant short form.
4. Do not invent Persian for terms practitioners keep in English. Do not keep English when a stable Persian term is standard (`انبار داده`, `متاداده`, `پردازش دسته‌ای`).
5. Record chosen form in document's term table for consistency.

## Anti-patterns

- Literal translation of branded concepts: avoid making up `خانه دریاچه داده` for Data Lakehouse.
- Over-Persianizing jargon: avoid replacing ETL/CDC/watermark/checkpoint with unfamiliar Persian when readers expect English.
- Over-English: avoid leaving general concepts English when Persian is standard (`دریاچه داده`, `انبار داده`, `پردازش دسته‌ای`).
- Inconsistency: switching between `انبار داده` and `Data Warehouse` and `داده‌انبار` in same doc without reason.
- English in parens repeated every sentence: use bilingual form at first mention/definition, then one consistent form.
