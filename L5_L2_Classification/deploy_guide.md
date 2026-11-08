# Deploy Guide — L_RAGSECSCAN
**Tier:** TIER_6_SECURITY_EVAL | **Stack:** Python 3.11, PAX 27B, KAMELOT_SEARCH analysis, AIOSS_FORMAT
**Air-gap capable after initial setup.**

## Prerequisites
Python 3.11+, PAX 27B, KAMELOT_SEARCH index access (read). T4 GPU.

## Environment
T4 GPU. KAMELOT_SEARCH index required. Read-only access to all indexed documents.

## AIOSS Integration
```bash
aioss init --module L_RAGSECSCAN --output ./l_ragsecscan.aioss
aioss append --chain ./l_ragsecscan.aioss --payload ./output.bin --module L_RAGSECSCAN
aioss verify --chain ./l_ragsecscan.aioss
```

## Air-Gap Setup
```bash
pip download -r requirements.txt -d ./wheels/
pip install --no-index --find-links ./wheels/ -r requirements.txt
```

## PAX 27B Harness Wiring
```python
from anticloud_pax import PAXHarness
harness = PAXHarness(
    model_path="./pax-27b-q4.gguf",
    module="L_RAGSECSCAN",
    aioss_chain="./L_RAGSECSCAN.aioss",
    classification="L5_NARROW_L2_GENERAL"
)
result = harness.process(input_data)
```

## Verification
```bash
aioss verify --chain ./L_RAGSECSCAN.aioss --verbose
python -m L_RAGSECSCAN.tests.smoke
```
