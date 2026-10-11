<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# LFM2-1.2B on the NPU

LiquidAI's LFM2-1.2B: a hybrid decoder, sixteen layers of which only six
(`full_attn_idxs`) are full attention; the rest are a gated short causal
convolution (`conv_L_cache=3` taps, depth-wise, one tap row a channel) in
place of attention. Every layer still ends in the same SwiGLU
feed-forward. `Lfm2` is the NPU graph, over the shared decoder
(`iron.lm`); `Lfm2Oracle` its float32 numpy forward pass, which it is
judged by; both are in `model.py`, about 290 lines.

An attention layer is `iron.lm`'s usual shape (`project`, `RoPE`, the
shared `attend`/`MHA`), plus a per-head RMSNorm on `q` and `k`
(`q_layernorm`/`k_layernorm` in the checkpoint) before RoPE -- no library
change: `RMSNorm(q.reshape(n * H, D), weight=w.q_norm)` normalizes each
head's own `head_dim`-wide row, the same operator Llama's model norms a
whole token's row with. EmbeddingGemma 2 already does this for its own
per-head norm, which is the precedent this followed.

A conv layer's three per-channel taps read a window spanning the current
call and the one before it, so each conv layer keeps a cache the same
shape convention as attention's key/value caches
(`(max_seq_len, conv_dim)`), with one extra leading block that is never
written and so stays zero -- standing in for "before the sequence" -- and
a small `(prefill_chunk + conv_kernel - 1, conv_dim)` scratch state a
prompt chunk assembles its window in before three `RowwiseMul`s (one a
tap) and two `ElementwiseAdd`s sum it; no new operator, only new wiring
(`Lfm2.conv`, parallel to the base class's `attend`).

## Weights and tokenizer

From Hugging Face: [`LiquidAI/LFM2-1.2B`](https://huggingface.co/LiquidAI/LFM2-1.2B)
(`model.safetensors`, `tokenizer.json`), ungated.

The tests look for them in `$IRON_EXAMPLE_WEIGHTS_DIR/lfm2-1.2b/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`); on the command line they
can be anywhere.

## Setup

Set up IRON as the repository root describes, then:

```bash
python3 -m pip install -r requirements_examples.txt
```

## Running

From the repository root:

```bash
python -m iron.applications.lfm2.model \
    /path/to/model.safetensors /path/to/tokenizer.json \
    --prompt-len 2048 --num-tokens 40
```

The flags are `iron.lm.runner`'s, shared with every model here
(`--random-weights SEED`, `--check-accuracy`, `--check-determinism`,
`--device-loop`, `--cost-table`, `--each-step`; see
`iron/applications/llama_3.2_1b/README.md` for what each does).

## The arena past 4 GiB

LFM2-1.2B's prompt chunk (weights, six attention layers' key/value caches
and ten conv layers' window and scratch caches) pushes the full-ELF
scratch arena past 4 GiB, the same `aiebu` 32-bit relocation addend limit
Granite 4.2 3B's port found; this port cherry-picked that fix
(`iron/common/image/fusion.py`'s windows onto the arena) rather than
reimplement it. Both the decode step and the prompt chunk link as a full
ELF (device loop) on NPU2 with it.

## Status

The numpy oracle matches Hugging Face's own forward pass (KL(HF||oracle)
mean 6.6e-12, max 1.1e-10, 0/64 top-1 mismatches over 64 teacher-forced
positions of a real prompt). `pytest iron/applications/lfm2/` passes
in full on real NPU2 hardware (xcoradaie220, 2026-10-10): generation,
accuracy, determinism, across two chunks, a chat turn, and both the
decode step and a prompt chunk deep in the caches (`max_seq_len - 1`) --
see `test.py`'s `MAX_KL`/`DEEP_KL` comments for the measured figures.
`skill-ports/lfm2-1.2b/` (not under this tree) has the full write-up,
including one testing-infrastructure fix this port needed
(`iron/lm/testing.py`'s `_fill_caches`, which assumed every layer's
key/value cache is a list -- true of every dense model so far, not of a
hybrid one) and a real environment gotcha that looked exactly like NPU
lock contention until isolated (`export PYTHONPATH=.` must extend, not
overwrite, the `pyxrt` path `xrt/setup.sh` sets).

A context-length sweep (`deck/MEASUREMENT_PROTOCOL.md`, 1024 to 32640
tokens, greedy, full-ELF device loop, 5 iterations + 1 discarded
warm-up) is in `skill-ports/lfm2-1.2b/stats.md` and summarized in
`strix-halo-220/validation-sweep.md`: decode tok/s falls gently from
14.38 to 12.38 over the full range (~14%), prefill tok/s rises with
context as dispatch overhead amortizes. KL(oracle||device) is measured
at 1024/2048 tokens of context only -- the teacher-forced accuracy
check's oracle cost scales worse than linearly with context and became
intractable (not guessed: timed) past about 2048 tokens in one session's
budget; points beyond it are performance-only, labeled as such.
