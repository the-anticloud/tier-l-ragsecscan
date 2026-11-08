# HF_Leaderboard_Lab_Results

**Project:** `L_RAGSECSCAN`  
**Tier:** `TIER_6_SECURITY_EVAL`  
**Slug:** `protectai/llm-guard`  
**Commit:** `168c1034ffdb`  
**Run:** `2026-09-30T15:07:07.146295+00:00`  

## Isolation Environment

| Field | Value |
| ----- | ----- |
| Platform | `win32` |
| Python | `3.12.10` |
| HF model | `distilbert-base-uncased` |
| HF load time | `4.42s` |
| Inference device | `cpu` |

## Results

**Framework:** [HuggingFace Open LLM Leaderboard (proxy via distilbert-base-uncased)](https://huggingface.co/docs/leaderboards/en/open_llm_leaderboard/archive)

**Model used:** `distilbert-base-uncased`

### Inference Latency (Classification)

| Metric | Value |
| ------ | ----- |
| Avg latency | **48.61 ms** |
| Min latency | 43.03 ms |
| Max latency | 54.02 ms |
| Samples | 5 |

### Real Tokenization Results

| Field | Value |
| ----- | ----- |
| Token count | **36** |
| Tokenization latency | 2.0 ms |
| Classification label | `LABEL_0` |
| Classification score | 0.5847 |
| Classification latency | 102.51 ms |
| Status | **PASS** |

**Input text tokenized:**
```
L_RAGSECSCAN (protectai/llm-guard) — 320 files, 14299 source lines, licence MIT, primary language ['Python']
```

**First 20 tokens:**
```
['[CLS]', 'l', '_', 'rags', '##ec', '##scan', '(', 'protect', '##ai', '/', 'll', '##m', '-', 'guard', ')', '—', '320', 'files', ',', '142']
```

> Full MMLU/HellaSwag/TruthfulQA/ARC/Winogrande/GSM8K require dedicated GPU.
> These results are CPU inference proxy metrics using distilbert-base-uncased.

---
_Anticloud Benchmark Suite — isolation log — 2026-09-30T15:07:07.146295+00:00_