import random, time, uuid, json
CORRIDORS=["OMR","Anna Salai","ECR","Mount Road","GST Road","Inner Ring Road"]
def gen_event():
    return {"event_id":str(uuid.uuid4()),"ts":int(time.time()*1000),"source":random.choice(["cctv","gps","signal","loop","bus"]),"lat":13.0+random.random()*0.25,"lon":80.2+random.random()*0.25,"speed_kmh":max(0,random.gauss(32,18)),"vehicle_hash":f"v{random.randint(1,100000)}","corridor":random.choice(CORRIDORS)}
if __name__=="__main__":
    for _ in range(5): print(gen_event())
