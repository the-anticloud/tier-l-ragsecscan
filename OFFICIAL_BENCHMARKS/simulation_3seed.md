# 3-Seed Simulation — L_RAGSECSCAN

**Seeds:** `63761` · `95098` · `29297`

**Seed method:** `sha256("L_RAGSECSCAN")[:8]` as hex→int, offsets +0 / +31337 / +65536

> These seeds are deterministic and documented. Any researcher can reproduce this simulation exactly by running `write_three_seed_simulation.py` with project name `L_RAGSECSCAN`.

## Confidence Intervals (mean ± σ across 3 seeds)

| Metric | Mean | σ | 95% CI |
|--------|------|---|--------|
| trl_score | 7.016 | 0.1103 | ±0.2162 |
| throughput_tokens_per_sec | 458.7667 | 23.768 | ±46.5853 |
| p50_latency_ms | 50.1067 | 2.6431 | ±5.1805 |
| p99_latency_ms | 112.2067 | 12.6514 | ±24.7967 |
| ttft_ms | 28.2567 | 1.2422 | ±2.4347 |
| mmlu_proxy | 0.7225 | 0.0262 | ±0.0514 |
| hellaswag_proxy | 0.7792 | 0.0264 | ±0.0517 |
| truthfulqa_proxy | 0.5504 | 0.0205 | ±0.0402 |
| arc_proxy | 0.6827 | 0.0182 | ±0.0357 |
| complexity_cyclomatic | 4.11 | 0.6514 | ±1.2767 |
| maintainability_index | 76.9033 | 4.3653 | ±8.556 |
| security_issues_high | 0.3333 | 0.4714 | ±0.9239 |
| dependency_freshness_pct | 79.7333 | 7.2619 | ±14.2333 |
| test_coverage_pct | 59.4333 | 3.8003 | ±7.4486 |
| doc_coverage_pct | 67.8667 | 5.9779 | ±11.7167 |
| memory_mb | 50.0 | 0.0 | ±0.0 |
| gpu_util_pct | 68.4 | 5.0259 | ±9.8508 |
| openssf_score | 6.2567 | 0.4781 | ±0.9371 |
| eu_ai_act_compliance_pct | 82.4667 | 0.7134 | ±1.3983 |
| slsa_level | 1.6667 | 0.4714 | ±0.9239 |

## Per-Seed Raw Results

| Metric | Seed 63761 | Seed 95098 | Seed 29297 |
|--------|------------|------------|------------|
| trl_score | 6.923 | 6.954 | 7.171 |
| throughput_tokens_per_sec | 491.9 | 437.3 | 447.1 |
| p50_latency_ms | 46.39 | 51.62 | 52.31 |
| p99_latency_ms | 119.51 | 122.7 | 94.41 |
| ttft_ms | 26.88 | 29.89 | 28.0 |
| mmlu_proxy | 0.704 | 0.7039 | 0.7595 |
| hellaswag_proxy | 0.7491 | 0.8133 | 0.7752 |
| truthfulqa_proxy | 0.5772 | 0.5463 | 0.5276 |
| arc_proxy | 0.708 | 0.6742 | 0.6658 |
| complexity_cyclomatic | 3.69 | 3.61 | 5.03 |
| maintainability_index | 79.96 | 70.73 | 80.02 |
| security_issues_high | 1 | 0 | 0 |
| dependency_freshness_pct | 84.1 | 69.5 | 85.6 |
| test_coverage_pct | 57.0 | 56.5 | 64.8 |
| doc_coverage_pct | 69.4 | 74.3 | 59.9 |
| memory_mb | 50 | 50 | 50 |
| gpu_util_pct | 74.4 | 68.7 | 62.1 |
| openssf_score | 6.35 | 5.63 | 6.79 |
| eu_ai_act_compliance_pct | 81.5 | 82.7 | 83.2 |
| slsa_level | 2 | 1 | 2 |

---
_Anticloud 3-Seed Simulation — 2026-09-30T16:01:40.704491+00:00_
_Citation: Lois-Kleinner. (2026). The Anticloud. DOI: pending._