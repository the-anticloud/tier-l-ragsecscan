# Radon_Complexity_Lab_Results
**Project:** `L_RAGSECSCAN` | **Status:** `PASS` | **Run:** `2026-09-30T17:14:20.030944+00:00`

**Framework:** [Radon — Cyclomatic Complexity & Maintainability Index](https://radon.readthedocs.io/)

## Key Metrics

- **files_analyzed:** `10`
- **average_complexity:** `{'grade': 'A', 'score': 3.6923076923076925}`
- **complexity_grade:** `A`
- **complexity_score:** `3.6923076923076925`
- **mi_output:** `E:\fenta\Downloads\The Anticloud\TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py - A (31.56)
E:\fenta\Downl`

## Raw Output (first 50 lines)
```
E:\fenta\Downloads\The Anticloud\TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\benchmarks\run.py
    F 84:0 build_output_scanner - D (23)
    F 26:0 build_input_scanner - C (16)
    F 218:0 main - A (3)
    F 170:0 get_output_test_data - A (2)
    F 164:0 get_input_test_data - A (1)
    F 177:0 benchmark_input_scanner - A (1)
    F 187:0 benchmark_output_scanner - A (1)
    F 199:0 get_output - A (1)
E:\fenta\Downloads\The Anticloud\TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\examples\amazon_bedrock.py
    F 15:0 invoke_agent - A (2)
E:\fenta\Downloads\The Anticloud\TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\examples\emotion_detection_example.py
    F 48:0 test_input_scanning - A (4)
    F 75:0 test_output_scanning - A (4)
    F 104:0 test_custom_emotion_blocking - A (4)
    F 135:0 test_no_emotion_blocking - A (4)
    F 165:0 test_full_emotion_analysis - A (3)
    F 198:0 test_output_full_emotion_analysis - A (3)
E:\fenta\Downloads\The Anticloud\TIER_6_SECURITY_EVAL\L_RAGSECSCAN\UPSTREAM\examples\langchain.py
    M 38:4 LLMGuardPromptChain.init_scanners - B (6)
    C 180:0 LLMGuardOutputChain - B (6)
    M 196:4 LLMGuardOutputChain.init_scanners - B (6)
    M 110:4 LLMGuardPromptChain._check_result - A (5)
    C 23:0 LLMGuardPromptChain - A (4)
    M 231:4 LLMGuardOutputChain._check_result - A (4)
    M 252:4 LLMGuardOutputChain.scan - A (4)
    M 142:4 LLMGuardPromptChain._call - A (3)
    C 19:0 LLMGuardPromptException - A (1)
    M 74:4 LLMGuardPromptChain.input_keys - A (1)
```

---
_Anticloud Independent Benchmark — 2026-09-30T17:14:20.030944+00:00_