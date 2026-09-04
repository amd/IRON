# W4A8 llama-3.2-1B on XDNA2 (NPU i8xi4 GEMMs)

Full-model W4A8 (INT4 weights, INT8 activations) llama-3.2-1B running on the
Strix Halo XDNA2 NPU through IRON's asymmetric i8xi4 GEMMs. The NPU does all
7 heavy GEMMs per layer (attn q/k/v/o + ffn gate/up/down); the host does
embedding, RMSNorm, RoPE, attention math, SiLU and the tied lm_head.

## Reproduction

```bash
cd ~/amd-oss/iron
PYTHONPATH=/usr/lib/python3/dist-packages \
  ~/amd-oss/iron-venv/bin/python llama_w4a8_npu.py "The capital of France is"
```

Config knobs (env):
- `W4A8_GROUPS=N` — i4 weight K-groups (Q4_K-style per-group scales). 16 = best quality.
- `W4A8_MIX_LEN=N` — first N layers keep i8 weights (near-exact). 8 recommended.
- `W4A8_GROUP_ACTS=1` — per-group activation scales (marginal).
- `W4A8_OPS_MIX=ffn_i8|attn_i8` — FFN or attention weights stay i8 (**ffn_i8 is the quality win**).
- `W4A8_ZP=1` — asymmetric zero-point i4 (measured no gain on llama; disabled).
- `W4A8_TRACE_ZERO=1` — trace all-zero activation rows.

Recommended: `W4A8_OPS_MIX=ffn_i8 W4A8_GROUPS=8` — FFN i8 + attention i4 G8:
corr 0.992-0.993, top1 exact, decode 554 ms/token.

## Results (llama-3.2-1B, vs bf16 CPU reference)

### Prefill quality (logits corr)

| config | corr |
|---|---|
| i4 per-column (G=1) | 0.937 |
| i4 G=8 | 0.966 |
| i4 G=16 | 0.973 |
| i4 G=16 + group acts | 0.974 |
| mix 8 + G=16 | 0.977–0.979 |
| **FFN i8 + attn i4 G8** | **0.983–0.990** | recommended |
| all i8 weights | 0.9965 (bound) |

Top-1 is exact on both test prompts for every config >= G=8.

### Decode (KV-cached, mix 8)

| config | ms/token | sample output |
|---|---|---|
| G=4 | 593 | "Paris is a city of art, history, and culture." |
| G=8 | 730 | "a lot of things to do in Paris. The city is" |
| G=16 | 903 | "Paris is the most visited city in the world. It is" |

### Components

- `llama_w4a8_npu.py` — prefill + KV-cached decode harness.
- `llama_w4a8_validate.py` — single-layer W4A8 validation (q/k/gate on real weights).
- The GEMM wrapper (`NPU_W4A8_GEMM` / `_Bound` / `_BoundGroup`) compiles the
  iron i8xi4 GEMM once per (K, N, G) shape and binds per-weight buffers.

## Bugs found & fixed (all root-caused, all committed)

1. **Shape-keyed op pool overwrote B bindings** — every op in a (K,N) shape
   group used the last-bound weights. Fix: per-weight buffer sets.
2. **XRT coherence-map write trap** — `.numpy()[:]` writes are unmediated;
   the buffer is never marked dirty, so the kernel runs on stale A.
   Fix: `with tensor.overwrite() as buf:`. Filed upstream: amd/iron#181.
3. **XRT first-dispatch readback flake** — same class; warmup + sync.
4. **float64 full-buffer dequant** — ~10 ms/call x G groups. Fix: float32,
   real rows only (3.5x decode speedup).
5. **Per-group buffer race** — shared A/C across group GEMMs read stale C.
   Fix: per-group buffers.

DESCENT.md parts 28-37 carry the full log; the fork is ~15 commits ahead of
amd/iron upstream.
