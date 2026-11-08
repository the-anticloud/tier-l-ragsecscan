# Developer Cookbook — L_RAGSECSCAN
**Stack:** Python 3.11, PAX 27B, KAMELOT_SEARCH analysis, AIOSS_FORMAT
**Domain:** RAGSecScan: security scanning specifically for RAG pipelines in Anticloud

## Scan RAG pipeline for injection
```python
from l_ragsecscan import RAGSecScanner

scanner = RAGSecScanner(
    pax_model="./pax-27b-q4.gguf",
    kamelot_index="./kamelot_index/",
    aioss_chain="./ragsecscan.aioss"
)

result = scanner.scan()
print(f"Injected instructions found: {result.injection_found}")
print(f"Poisoned chunks: {result.poisoned_chunks}")
print(f"Retrieval manipulation: {result.manipulation_detected}")
print(f"Safe to deploy: {result.safe}")
print(f"Chain: {result.chain_hash}")
```

## AIOSS Chain Append
```python
import hashlib, time

def aioss_append(chain_path, payload: bytes, module_id: str):
    entry_hash = hashlib.sha3_256(payload).digest()
    ts = int(time.time_ns()).to_bytes(8, 'big')
    with open(chain_path, 'rb') as f:
        f.seek(-32, 2); prev_hash = f.read(32)
    new_hash = hashlib.sha3_256(prev_hash + entry_hash + ts).digest()
    with open(chain_path, 'ab') as f:
        f.write(ts + entry_hash + new_hash)
    return new_hash.hex()
```
