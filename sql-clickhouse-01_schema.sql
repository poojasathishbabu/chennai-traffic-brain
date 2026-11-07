CREATE DATABASE IF NOT EXISTS traffic;
CREATE TABLE IF NOT EXISTS traffic.traffic_raw (event_id String, ts DateTime64(3), source LowCardinality(String), lat Float64, lon Float64, speed_kmh Float32, vehicle_hash String, corridor LowCardinality(String)) ENGINE = ReplacingMergeTree(ts) PARTITION BY toDate(ts) ORDER BY (corridor, ts, event_id);
CREATE TABLE IF NOT EXISTS traffic.traffic_agg_10s (corridor LowCardinality(String), window_ts DateTime, flow_state LowCardinality(String), vehicle_count UInt32, avg_speed Float32) ENGINE = SummingMergeTree() PARTITION BY toDate(window_ts) ORDER BY (corridor, window_ts, flow_state);
-- Serving: SELECT corridor, avg(avg_speed), sum(vehicle_count) FROM traffic_agg_10s WHERE window_ts >= now() - INTERVAL 5 MINUTE GROUP BY corridor;
