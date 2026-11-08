# Pylint_Quality_Lab_Results
**Project:** `L_RAGSECSCAN` | **Status:** `FAIL` | **Run:** `2026-09-30T17:14:20.030944+00:00`

**Framework:** [Pylint — Python Code Quality Analyzer](https://pylint.readthedocs.io/)

## Key Metrics

- **files_analyzed:** `5`
- **pylint_score:** `3.04`
- **pylint_score_max:** `10.0`

## Raw Output (first 50 lines)
```
************* Module run
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:1:0: C0114: Missing module docstring (missing-module-docstring)
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:10:0: E0401: Unable to import 'llm_guard' (import-error)
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:11:0: E0401: Unable to import 'llm_guard.input_scanners.anonymize_helpers' (import-error)
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:12:0: E0401: Unable to import 'llm_guard.input_scanners.ban_substrings' (import-error)
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:13:0: E0401: Unable to import 'llm_guard.input_scanners.base' (import-error)
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:14:0: E0401: Unable to import 'llm_guard.output_scanners.base' (import-error)
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:15:0: E0401: Unable to import 'llm_guard.vault' (import-error)
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:19:0: C0413: Import "import torch._inductor.config" should be placed at the top of the module (wrong-import-position)
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:21:0: W0212: Access to a protected member _inductor of a client class (protected-access)
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:26:0: R0911: Too many return statements (15/6) (too-many-return-statements)
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:26:0: R0912: Too many branches (15/12) (too-many-branches)
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:84:0: C0116: Missing function or method docstring (missing-function-docstring)
TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py:84:0: R0911: Too many return statements (22/6) (too-many-return-statements)
TIER_6_SECURITY_EVAL\L_RAGSEC
```

---
_Anticloud Independent Benchmark — 2026-09-30T17:14:20.030944+00:00_