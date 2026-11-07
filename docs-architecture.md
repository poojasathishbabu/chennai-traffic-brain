# Architecture
Sources -> Kafka (48p) -> Flink + Polars -> ClickHouse + Redis -> FastAPI
Exactly-once, checkpoint 60s, recovery 42s, watermark 5s.
