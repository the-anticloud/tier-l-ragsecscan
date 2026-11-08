# Ledger Status

**Project:** `L_RAGSECSCAN`  
**Tier:** TIER_6_SECURITY_EVAL  
**Identity:** Upstream `protectai/llm-guard` @ `168c1034ffdb` (MIT)

## Chain state

| Fact | Value |
| --- | --- |
| Upstream | `protectai/llm-guard` |
| Commit | `168c1034ffdb33837e7ae6fd6a16b80567c1be03` |
| Upstream licence | MIT |
| Licence class | permissive |
| Clone size | 1.25 MB |
| Ledger | 0 blocks, chain verified |
| Current TRL | NOT YET MEASURED |
| Post-optimisation TRL | NOT YET MEASURED |
| II budget cap | 1500.0 IIU |
| Verified upstream edits | 1 |

- Blocks: **0**
- Head digest: `None`
- Chain verification: **verified**

## Independent verification

The chain is verifiable without trusting this project's tooling:

```
anticloud ledger verify
anticloud ledger export > ledger.jsonl
```

Each block carries the previous block's digest, so removing or reordering an
entry invalidates every block after it. That property is the reason the
ledger can stand in for a claim of what happened.
