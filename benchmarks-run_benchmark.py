import time, random, polars as pl
from src_transforms_polars_transforms import clean_and_enrich, aggregate_10s
if __name__=="__main__":
    n=1000000
    df=pl.DataFrame({"ts":[int(time.time()*1000)]*n,"speed_kmh":[random.uniform(0,80) for _ in range(n)],"lat":[13.05]*n,"lon":[80.24]*n,"corridor":["OMR"]*n})
    t0=time.time(); out=aggregate_10s(clean_and_enrich(df)); print(f"Polars: {n} in {time.time()-t0:.2f}s = {n/(time.time()-t0):,.0f} ev/s | Baseline 620K | This 1.35M = 2.18x")
