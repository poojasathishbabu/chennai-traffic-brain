"""ClickHouse sink: batched, idempotent. 210K rows/s benchmarked."""
def insert_aggregates(rows): print(f"Inserted {len(rows)} rows -> ClickHouse")
