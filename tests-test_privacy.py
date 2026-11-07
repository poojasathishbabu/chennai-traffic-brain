from src_schemas_traffic_event import TrafficEvent
def test_hash():
    h=TrafficEvent.hash_plate('TN01AB1234','salt1'); assert 'TN01' not in h
