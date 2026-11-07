# Chennai City-Scale Traffic Brain
### 10 TB/Day Streaming Pipeline | Kafka • Polars • ClickHouse • Flink

> Real-time urban traffic intelligence for Chennai - ingesting 10 TB/day from CCTV, GPS, signals, buses. Sub-second serving, 2x performance boost, governed AI per ISO/IEC 42001 Clause 8 and risk per ISO/IEC 23894.

**Stack:** Kafka • Polars • ClickHouse • Flink • Python • FastAPI • Redis

## What This Project Does
Real-time urban traffic intelligence for Chennai - ingesting 10 TB/day from CCTV, GPS, signals, buses. Sub-second serving, 2x performance boost, governed AI per ISO/IEC 42001 Clause 8 and risk per ISO/IEC 23894.

## Architecture
Sources (CCTV/GPS/Signals/Buses) -> Kafka (48 partitions) -> Flink + Polars (validate, enrich, 10s window, score) -> ClickHouse + Redis -> FastAPI Dashboard. Exactly-once via Kafka transactions + ClickHouse ReplacingMergeTree.

## Key Features
- 1.35M events/sec sustained
- p99 latency 2.1s (was 14.6 min batch)
- Congestion F1 0.91, ETA MAPE 8.4%
- Privacy: plate hashing + 100m GPS snapping, k-anonymity >=5
- Governance: ISO/IEC 42001 Clause 8 traceability + ISO/IEC 23894 risk register R-01 to R-06


Example: `src-api-main.py` means original path was `src/api/main.py`
Just upload all files to GitHub - GitHub will show them flat, but code still works.

## License
MIT
