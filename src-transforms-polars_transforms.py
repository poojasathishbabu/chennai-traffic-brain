import polars as pl
def clean_and_enrich(df: pl.DataFrame) -> pl.DataFrame:
    return (df.filter(pl.col("speed_kmh").is_between(0,180))
        .filter(pl.col("lat").is_between(12.9,13.35))
        .with_columns([(pl.col("lat").round(3)).alias("lat_grid"),(pl.col("lon").round(3)).alias("lon_grid"),
        pl.when(pl.col("speed_kmh")<10).then(pl.lit("jam")).when(pl.col("speed_kmh")<25).then(pl.lit("slow")).when(pl.col("speed_kmh")<45).then(pl.lit("moderate")).otherwise(pl.lit("free")).alias("flow_state"),
        (pl.col("ts")//10000*10000).alias("window_10s")]))
def aggregate_10s(df: pl.DataFrame) -> pl.DataFrame:
    return (df.group_by(["corridor","window_10s","flow_state"]).agg([pl.len().alias("vehicle_count"),pl.col("speed_kmh").mean().alias("avg_speed")]).sort(["corridor","window_10s"]))
def congestion_score(avg_speed: float, volume: int, free_flow: float=55.0) -> float:
    return round((1-max(0,min(1,avg_speed/free_flow)))*70 + min(30, volume/1000*30),1)
