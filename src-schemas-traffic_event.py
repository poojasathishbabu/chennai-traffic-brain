from pydantic import BaseModel
from typing import Optional
import hashlib
class TrafficEvent(BaseModel):
    event_id: str; ts: int; source: str; camera_id: Optional[str]=None
    lat: float; lon: float; speed_kmh: float; heading: float=0.0
    vehicle_hash: str; corridor: str
    @staticmethod
    def hash_plate(plate: str, salt: str) -> str:
        return hashlib.sha256(f"{plate}:{salt}".encode()).hexdigest()[:16]
    def snap(self): return round(self.lat,3), round(self.lon,3)
