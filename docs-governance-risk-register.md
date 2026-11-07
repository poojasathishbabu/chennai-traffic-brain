# ISO/IEC 23894 Risk Register
R-01 Drift -> wrong signal timing | Mitigation: drift monitor + human approval
R-02 PII re-identification | Hashing + 100m snapping + k>=5
R-03 Kafka outage | RF=3, tiered, DLQ replay
R-04 Spoofed probes | Anomaly filter + provenance
R-05 Bias under-served corridors | Coverage audit
R-06 False incident | Dual-model + operator confirm
