"""Flink Job: Kafka -> Validate -> Enrich(Polars) -> Window 10s -> Score -> ClickHouse. Checkpoint 60s, Watermark 5s, Lateness 30s, Parallelism 8. Exactly-once via Kafka transactions + ClickHouse ReplacingMergeTree dedup on event_id."""
from src_transforms_polars_transforms import clean_and_enrich, aggregate_10s
import polars as pl
def run_local(events):
    df=pl.DataFrame(events); return aggregate_10s(clean_and_enrich(df))
if __name__=="__main__": print("Deploy via Flink SQL in deploy-flink-traffic_job.sql")
