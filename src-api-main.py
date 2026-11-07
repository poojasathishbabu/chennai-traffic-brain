from fastapi import FastAPI
import random
app=FastAPI(title="Chennai Traffic Brain API", version="1.0.0")
@app.get("/health")
def health(): return {"status":"ok","pipeline":"kafka->flink->clickhouse","latency_p99_ms":2100}
@app.get("/v1/corridors/{corridor}/congestion")
def congestion(corridor: str, window: str="5m"):
    speed=round(random.uniform(12,48),1)
    return {"corridor":corridor,"window":window,"avg_speed_kmh":speed,"vehicle_count":random.randint(800,4200),"congestion_score":round(max(0,100-speed*1.4),1),"flow_state":"slow" if speed<25 else "moderate"}
@app.get("/v1/incidents")
def incidents(): return {"incidents":[{"id":"INC-1021","corridor":"OMR","type":"breakdown","severity":"medium","lat":13.02,"lon":80.24}]}
@app.get("/v1/signals/advisory")
def advisory(signal_id: str="SIG-OMR-042"): return {"signal_id":signal_id,"recommended_cycle_s":110,"current_cycle_s":140,"requires_human_approval":True}
