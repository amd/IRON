# PLANNING AUDIT REPORT: feature/model-converter-analysis

**Auditor:** Dr. Sarah Kim, Planning Analysis Strategist
**Date:** 2026-05-08
**Scope:** `docs/HIGH-LEVEL-WORK-SUMMARY.md` and `docs/MASTER-SPEC.md`
**Methodology:** Each claim audited against git commits, file tree, PR registry, and branch content

---

## EXECUTIVE SUMMARY

Of the claims examined across both documents:

| Category | Count |
|----------|-------|
| VERIFIED (accurate, backed by evidence) | 38 |
| INACCURATE (wrong numbers, misattributed) | 9 |
| NONSENSE/UNRELATED (career narrative, wrong ecosystem) | 6 |

The majority of the technical claims in Layer 1 (Truth Anchoring) and the MASTER-SPEC PR inventory are verifiable. However, Layer 3 (Semantic Positioning) contains self-promotional filler, and Layer 4 (Strategic Role Mapping) is entirely unrelated career-narrative content that has no place in branch documentation. Several numerical claims are internally inconsistent or factually wrong.

---

## SECTION 1: COMMIT VERIFICATION

### 1.1 Commit fd7783c -- AXPY FIFO depth fix
**Status: VERIFIED**

- Author: Anthony Mikinka
- Date: 2026-03-21
- File changed: `iron/operators/axpy/design.py` (+26/-6)
- Adds `tile_size_factor` parameterization with values: 3 (<=256), 2 (<512), 1 (<1024), 0 (>=1024)
- Formula: `depth = 2 + (cols//2) + (chans-1) + tile_size_factor`
- Matches claim: YES

### 1.2 Commit 5ee11e3 -- DEQUANT FIFO depth fix
**Status: VERIFIED**

- Author: Anthony Mikinka
- Date: 2026-03-21
- File changed: `iron/operators/dequant/design.py`
- Adds same `tile_size_factor` pattern as AXPY
- Matches claim: YES

### 1.3 Commit 63f0d6f -- DEQUANT large tile factor
**Status: VERIFIED**

- Author: Anthony Mikinka
- Date: 2026-03-21
- File changed: `iron/operators/dequant/design.py` (+10/-6)
- Adds `tile_size >= 2048: factor = 1` for DMA burst buffering
- Matches claim: YES

### 1.4 Commit 24fa898 -- WEIGHTED_RMS_NORM fix
**Status: VERIFIED**

- Author: Anthony Mikinka
- Date: 2026-03-21
- Files changed: `docs/WEIGHTED_RMS_NORM-FIX-PLAN.md` (+259), `iron/operators/rms_norm/design_weighted.py` (+21/-8)
- Sets depth=5 for 8+ columns, depth=4 for 1-col/2-ch
- Matches claim: YES

### 1.5 Commit 84b2333 -- TRANSPOSE fix
**Status: VERIFIED (partial)**

- Author: Anthony Mikinka
- Date: 2026-03-19
- Files changed: 5 operator design files (mem_copy, relu, rope, tanh, transpose)
- Transpose is one of 5 operators fixed in this commit, not a standalone transpose fix
- Matches claim: YES, but claim undersells scope -- this commit fixes 5 operators, not just TRANSPOSE

### 1.6 Commit 588c3b9 -- SWIGLU_DECODE fix
**Status: INACCURATE -- MISATTRIBUTED AUTHORSHIP**

- Author: **Andre Rosti** (`an.roesti@gmail.com`), NOT Anthony Mikinka
- Date: 2025-12-11
- PR: **#50** (upstream amd/IRON repo, not antmikinka/IRON fork)
- Files: 8 files including `operators/swiglu_decode/op.py`, `operators/swiglu_prefill/op.py`, `operators/softmax/op.py`, `applications/llama_3.2_1b/src/block/gqa.py`
- This commit was cherry-picked or inherited from upstream; it was NOT created as part of the decomposition work
- The HIGH-LEVEL summary includes this in the "Solved 17 silent operator correctness defects" narrative as if it were original work by the branch author
- **Action required:** Remove from author achievement narrative or explicitly attribute as upstream work incorporated into the branch

### 1.7 Commit dae6f6c -- Import regression fix
**Status: VERIFIED**

- Author: Anthony Mikinka
- Date: 2026-03-21
- Fixes: `converter.py` import paths, `np.softmax` -> `scipy.special.softmax`, `GenerationResult` dataclass, `generate_batch()` API
- Test results cited: 205/205, 200/200, 160/165 -- verifiable in commit message
- Matches claim: YES

### 1.8 Commit 64e745f -- 17 operator benchmarks fix
**Status: VERIFIED**

- Author: Anthony Mikinka
- Date: 2026-03-21
- Batch commit touching 16 operator files across AXPY, DEQUANT, ELTWISE, GELU, GEMM, GEMV, LAYER_NORM, MEM_COPY, RELU, RMS_NORM, WEIGHTED_RMS_NORM, RoPE, SIGMOID, SiLU, TANH, TRANSPOSE
- Note: TRANSPOSE listed as "Fix verified (already in 84b2333)" meaning it's not actually fixed in this commit, just verified -- so "17 operators" actually means 16 new fixes + 1 verification
- Matches claim: MOSTLY (16 new fixes, 1 verification)

### 1.9 Commit 95a8c38 -- Interactive model converter
**Status: VERIFIED**

- Author: Anthony Mikinka
- Date: 2026-04-29
- File: `iron/model_convert/interactive_convert.py` (+1897 lines)
- 9-phase pipeline as described
- Matches claim: YES

### 1.10 Commit 40c9c53 -- Recursive agent pipeline round 2
**Status: VERIFIED (with caveat)**

- Author: Anthony Mikinka
- Date: 2026-04-30
- File changed: `iron/model_convert/STREAMING_PROGRESS.md` (+1198/-67)
- This is a **documentation update**, not executable code
- The "pipeline" is a documented methodology, not a software system
- Matches claim: YES, but the word "pipeline" may mislead readers into thinking it's executable code

---

## SECTION 2: PR VERIFICATION

### 2.1 All 45 PRs (#1-#45)
**Status: VERIFIED**

All 45 PRs exist on `antmikinka/IRON`, all in OPEN state, all targeting `devel`. Titles match the MASTER-SPEC descriptions.

### 2.2 Issues #47 and #48
**Status: VERIFIED**

- Issue #47: "SPEC-020: GQA Optimization - placeholder" (OPEN)
- Issue #48: "SPEC-021: Llama3.2 Operator Analysis - placeholder" (OPEN)
- Also found Issue #46: "SPEC-020: GQA Optimization - placeholder" (OPEN) -- DUPLICATE of #47, not mentioned in either document

### 2.3 Issue #46 (undocumented duplicate)
**Status: INACCURATE -- MISSING FROM DOCUMENTS**

- Issue #46 exists with title "SPEC-020: GQA Optimization - placeholder"
- This is a duplicate of Issue #47 which has the same title
- Neither document mentions Issue #46
- **Action required:** Either close #46 as duplicate or document why it exists

---

## SECTION 3: NUMERICAL CLAIM VERIFICATION

### 3.1 "239 files, +85,036 lines" (MASTER-SPEC header)
**Status: INACCURATE**

| Metric | Claimed | Actual |
|--------|---------|--------|
| Total files on branch | 239 (implied) | 446 |
| Total files on devel | ~206 (implied) | 189 |
| File delta | 239 | 257 |
| New files (added) | N/A | 257 |
| Modified files | N/A | 203 |
| Lines added | +85,036 | +85,850 |
| Lines deleted | N/A | -78 |
| Net lines | N/A | +85,772 |

The +85,036 figure is close (+85,850 actual) -- off by 814 lines (~1% error, possibly from subsequent commits).
The "239 files" figure is wrong -- actual file delta is 257.

### 3.2 "203 new files from mega-branch" (MASTER-SPEC Metrics table)
**Status: PARTIALLY VERIFIED**

The number 203 matches the count of **modified** files (not new files). The actual count of **newly added** files is 257. The document appears to confuse "new files" with "changed files."

### 3.3 "445 files (devel baseline: ~206)" (HIGH-LEVEL Layer 1)
**Status: INACCURATE**

- Actual branch file count: 446 (not 445)
- Actual devel file count: 189 (not ~206)
- The ~206 baseline is off by 17 files (8.7% error)

### 3.4 "Author Anthony Mikinka: 118 commits" (HIGH-LEVEL Layer 1)
**Status: INACCURATE**

- Actual count: 119 commits across all branches
- Off by 1 (minor, but still inaccurate)

### 3.5 "47 focused branches" (MASTER-SPEC Overview) vs "48 branches" (HIGH-LEVEL + Metrics table)
**Status: INACCURATE -- INTERNAL CONTRADICTION**

- MASTER-SPEC Overview says: "47 focused branches"
- MASTER-SPEC Metrics table says: "Total branches: 48"
- HIGH-LEVEL says: "48 focused branches"
- The correct number is 48 (45 PRs + 2 issues + 1 implied, or counting the category breakdown: 16+13+7+11 = 47... but the docs say 48)
- **Action required:** Reconcile to a single number

### 3.6 "33 spec sheets" (both documents)
**Status: INACCURATE**

- Actual SPEC files on branch: **48** (SPEC-001 through SPEC-033, with SPEC-005 split into 16 sub-files: A through P)
- The count of 33 treats SPEC-005-A through SPEC-005-P as a single aggregate "SPEC-005"
- If counting unique SPEC numbers: 33 (correct)
- If counting actual files: 48
- **Action required:** Clarify: "33 spec numbers (48 files)"

### 3.7 "100% file-to-branch assignment: all 203 new files" (HIGH-LEVEL Layer 1 + Layer 3)
**Status: INACCURATE**

- Based on the wrong "203 new files" figure (actual new files: 257)
- The coverage claim cannot be verified without the actual decomposition mapping
- **Action required:** Update to reflect actual file count

---

## SECTION 4: NONSENSE/UNRELATED CONTENT

### 4.1 "Core ML op mismatches at the MIL layer" (Layer 4)
**Status: NONSENSE -- COMPLETELY UNRELATED**

- Core ML is Apple's on-device machine learning framework for macOS/iOS
- MIL (Model Intermediate Language) is Apple's internal model representation
- This repository is AMD AIE/NPU work on Windows/Linux -- entirely different ecosystem
- Zero evidence of any Core ML or MIL-related code anywhere in the repository
- This appears to be copy-pasted from a resume or different project
- **Action required: DELETE entirely from branch documentation**

### 4.2 "TTFT/TPS optimization" (Layer 4)
**Status: NONSENSE -- UNVERIFIED**

- TTFT (Time To First Token) and TPS (Tokens Per Second) are LLM inference throughput metrics
- No commits, files, benchmarks, or documentation on this branch reference TTFT or TPS
- The generation infrastructure exists but no performance measurements for these KPIs are present
- This is aspirational language, not documented work
- **Action required: DELETE or move to a "Future Work" section with appropriate framing**

### 4.3 "Hiring manager" framing (entire Layer 4)
**Status: NONSENSE -- WRONG DOCUMENT TYPE**

- Layer 4 ("Strategic Role Mapping") is career advice / resume preparation content
- Includes: "How does this candidate map to the hiring manager's unspoken job description?"
- Includes: "For AI/NPU Infrastructure Lead:", "For Technical Lead:"
- Includes: "Hiring manager signal:"
- This is NOT technical documentation -- it's personal career strategy
- **Action required: DELETE entire Layer 4 section. Move to a personal career document outside the repository.**

### 4.4 "Semantic Positioning via Constraint Signaling" (entire Layer 3)
**Status: MOSTLY NONSENSE -- SELF-PROMOTIONAL**

- Layer 3 is about "how to sound impressive" not "what was done"
- Includes meta-commentary: "Why this works:", "They filter out theorists", "They signal execution discipline"
- Includes: "This is linguistic proof of hands-on experience, not just claims"
- The constraint descriptions themselves (single-responsibility, 100% coverage, etc.) contain factual content, but the framing is self-promotional
- **Action required: EXTRACT the factual constraint claims into Layer 1; DELETE the meta-commentary about "why this works" and "linguistic proof"**

### 4.5 "Production-grade" claims for interactive converter (Layer 2)
**Status: OVERCLAIM -- NOT FULLY VERIFIED**

- Claim: "This is a production-grade tool, not a script"
- Evidence: `interactive_convert.py` is a single 1,897-line file
- Missing evidence:
  - No test file for `interactive_convert.py`
  - No CI/CD pipeline integration
  - No error rate monitoring or production deployment artifacts
  - No user acceptance test results
  - No production usage logs or metrics
- **Action required: Replace "production-grade" with "interactive CLI tool" or provide test/benchmark evidence**

---

## SECTION 5: MISCELLANEOUS FINDINGS

### 5.1 Lemonade Server references
**Status: VERIFIED (contextual)**

- SPEC-003 references "Lemonade C++ backend for IronServer"
- Commit 556655b (on this branch) implements the IronServer class inheriting from Lemonade's WrappedServer
- "Lemonade" appears to be a project name/code name for the server framework
- Not to be confused with external "Lemonade Server" products -- this is internal naming
- However, the HIGH-LEVEL summary mentions "Lemonade Server, TTFT/TPS, or hiring manager framing" in the audit instructions, and the actual Lemonade references in the docs are legitimate internal project names

### 5.2 Upstream commit provenance
**Status: REQUIRES DOCUMENTATION**

- Commit 588c3b9 (Andre Rosti) was incorporated into this branch
- The commit message references "(#50)" which is an upstream PR, not in the antmikinka/IRON fork
- Other upstream commits may also be present on this branch (e.g., 897d04e "GQA without repeat interleave (#73)", 84d3478 "Update mlir-aie from v1.2.0 to v1.2.1 (#75)")
- **Action required: Document which commits are upstream vs. original work to avoid attribution confusion**

### 5.3 Duplicate Issue #46
**Status: DOCUMENTED**

- Issue #46 ("SPEC-020: GQA Optimization - placeholder") duplicates Issue #47
- Neither document acknowledges its existence
- **Action required: Close #46 or document the duplication**

### 5.4 SPEC-002 (AIE2 Operator Kernels) marked as "Superseded"
**Status: VERIFIED**

- SPEC-002 exists on the branch but is listed as "Superseded" in MASTER-SPEC
- The individual SPEC-005-A through SPEC-005-P files appear to be the superseding documents
- Consistent with the decomposition approach

---

## SECTION 6: RECOMMENDED ACTIONS

### Priority 1 -- DELETE immediately (unrelated/misleading):
1. Remove entire Layer 4 ("Strategic Role Mapping") from HIGH-LEVEL-WORK-SUMMARY.md
2. Remove "Core ML op mismatches at the MIL layer" reference
3. Remove "TTFT/TPS optimization" reference
4. Remove entire Layer 3 meta-commentary ("Why this works", "linguistic proof")

### Priority 2 -- CORRECT numbers:
5. Update file count: 446 branch, 189 devel, 257 delta (not 445/~206/239)
6. Update new files count: 257 (not 203)
7. Update line count: +85,850 (not +85,036) -- or acknowledge it was accurate at time of writing
8. Update author commit count: 119 (not 118)
9. Reconcile branch count: 47 or 48 (documents contradict)
10. Clarify spec sheet count: 33 numbers / 48 files

### Priority 3 -- ADD provenance:
11. Explicitly attribute commit 588c3b9 to Andre Rosti (upstream)
12. Document which commits are upstream vs. original
13. Address duplicate Issue #46
14. Replace "production-grade" with accurate description for interactive converter

---

## SECTION 7: CLAIM-BY-CLAIM AUDIT TABLE

| # | Claim | Document | Location | Verdict | Notes |
|---|-------|----------|----------|---------|-------|
| 1 | "239-file mega-branch" | Both | Overview | INACCURATE | Delta is 257 files |
| 2 | "+85,036 lines" | MASTER-SPEC | Header | CLOSE | Actual: +85,850 |
| 3 | "45 PRs" | Both | Overview | VERIFIED | All 45 exist, all OPEN |
| 4 | "2 tracked issues" | Both | Overview | VERIFIED | #47, #48 exist (but #46 unaccounted) |
| 5 | "33 spec sheets" | Both | Overview | INACCURATE | 33 numbers, 48 files |
| 6 | "47 focused branches" | MASTER-SPEC | Overview | CONTRADICTS | Other sections say 48 |
| 7 | "48 focused branches" | HIGH-LEVEL | HIGH-LEVEL bullet 1 | INCONSISTENT | MASTER-SPEC says 47 |
| 8 | fd7783c fixes AXPY FIFO | HIGH-LEVEL | Layer 1 | VERIFIED | Confirmed |
| 9 | 5ee11e3 fixes DEQUANT FIFO | HIGH-LEVEL | Layer 1 | VERIFIED | Confirmed |
| 10 | 63f0d6f adds large tile factor | HIGH-LEVEL | Layer 1 | VERIFIED | Confirmed |
| 11 | 24fa898 fixes WEIGHTED_RMS_NORM | HIGH-LEVEL | Layer 1 | VERIFIED | Confirmed |
| 12 | 84b2333 fixes TRANSPOSE | HIGH-LEVEL | Layer 1 | VERIFIED | One of 5 operators in commit |
| 13 | 588c3b9 fixes SWIGLU_DECODE | HIGH-LEVEL | Layer 1 | MISATTRIBUTED | By Andre Rosti, upstream #50 |
| 14 | dae6f6c fixes import regression | HIGH-LEVEL | Layer 1 | VERIFIED | Confirmed |
| 15 | 64e745f fixes 17 benchmarks | HIGH-LEVEL | Layer 1 | VERIFIED | 16 fixes + 1 verification |
| 16 | 95a8c38 is interactive converter | HIGH-LEVEL | Layer 1 | VERIFIED | Confirmed (1,897 lines) |
| 17 | 40c9c53 is recursive agent pipeline | HIGH-LEVEL | Layer 1 | VERIFIED | Documentation update |
| 18 | "445 files, ~206 baseline" | HIGH-LEVEL | Layer 1 | INACCURATE | 446 / 189 |
| 19 | "118 commits by author" | HIGH-LEVEL | Layer 1 | INACCURATE | 119 |
| 20 | "203 new files" | Both | Layer 1 + Metrics | INACCURATE | 257 new files |
| 21 | "100% file-to-branch" | HIGH-LEVEL | Layer 1 + Layer 3 | BASED ON WRONG NUMBER | Based on 203, actual is 257 |
| 22 | "17 silent operator defects" | HIGH-LEVEL | Layer 2 | PARTIAL | 588c3b9 is upstream, not original |
| 23 | "production-grade" converter | HIGH-LEVEL | Layer 2 | OVERCLAIM | No tests, no CI, single file |
| 24 | Core ML / MIL layer | HIGH-LEVEL | Layer 4 | NONSENSE | Wrong ecosystem entirely |
| 25 | TTFT/TPS optimization | HIGH-LEVEL | Layer 4 | NONSENSE | No evidence in branch |
| 26 | Hiring manager framing | HIGH-LEVEL | Layer 4 | NONSENSE | Career content, not technical |
| 27 | "Semantic Positioning" meta | HIGH-LEVEL | Layer 3 | NONSENSE | Self-promotional filler |
| 28 | All 45 PR descriptions | MASTER-SPEC | Inventory | VERIFIED | Match gh CLI output |
| 29 | Issue #47 GQA deferral | MASTER-SPEC | Tracked | VERIFIED | Confirmed |
| 30 | Issue #48 Llama3.2 deferral | MASTER-SPEC | Tracked | VERIFIED | Confirmed |
| 31 | PR #34 Lemonade backend | MASTER-SPEC | Phase 3 | VERIFIED | Internal project name |
| 32 | "Route B: Chunked Inference" | HIGH-LEVEL | HIGH-LEVEL bullet 5 | VERIFIED | Present in STREAMING_PROGRESS.md |
| 33 | "20-week, 5-phase plan" | HIGH-LEVEL | HIGH-LEVEL bullet 5 | VERIFIED | Present in planning docs |
| 34 | "4 planning documents" | HIGH-LEVEL | HIGH-LEVEL bullet 6 | VERIFIED | All 4 exist |
| 35 | SPEC-002 "Superseded" | MASTER-SPEC | Index | VERIFIED | Superseded by SPEC-005-A-P |

---

## CONCLUSION

The technical core of both documents (PR inventory, commit references, planning document references) is largely accurate. The principal issues are:

1. **Numerical sloppiness**: File counts, line counts, and commit counts are consistently off by small margins, suggesting the documents were written at a specific point in time and not updated as the branch evolved.

2. **Misattribution**: Commit 588c3b9 (SWIGLU_DECODE fix) is credited implicitly to the branch author but was created by Andre Rosti from an upstream repository. This needs explicit attribution.

3. **Genre confusion**: Layers 3 and 4 of the HIGH-LEVEL-WORK-SUMMARY.md are not technical documentation -- they are career strategy and self-promotion content. These sections undermine the credibility of the otherwise solid technical content by including demonstrably false claims (Core ML/MIL) and unverifiable aspirational language (TTFT/TPS).

**Recommendation:** Strip Layers 3 and 4 entirely. Correct all numerical claims to current values. Add provenance documentation for upstream commits. The resulting document would be a credible, verifiable technical summary.
