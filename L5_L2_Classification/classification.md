# L5 Narrow / L2 General Classification — L_RAGSECSCAN
**Platform:** Anticloud | **Tier:** TIER_6_SECURITY_EVAL | **PAX:** 27B
**IP:** USPTO pending 2026, Anticloud FZ LLE, 0-1.gg | **License:** Apache-2.0

## L5 Narrow
L_RAGSECSCAN evaluates security risks specific to Anticloud RAG pipelines: prompt injection via malicious documents in the index, retrieval manipulation attacks, and chunk poisoning. Narrow scope: Anticloud KAMELOT_SEARCH and K_GRAPHRAG security.

## L2 General
L2 General: L_RAGSECSCAN protects all tiers' RAG pipelines. TIER_7 clinical RAG and TIER_6 security RAG both undergo L_RAGSECSCAN evaluation.

## PAX 27B Integration
PAX 27B tests RAG security by attempting to extract injected instructions from the KAMELOT_SEARCH index: 'This evaluation confirms that no injected instructions survived indexing.'

## AIOSS Audit Chain
Every RAG security scan (index hash + injection test results hash + vulnerability findings hash) is chained: H_n = SHA3-256(H_{n-1} || entry_hash_n || timestamp_n).
Offline-verifiable, tamper-evident, zero cloud dependency.

## Regulatory / Compliance
OWASP LLM Top 10 (LLM07: prompt injection via RAG). NIST AI RMF 1.0.
