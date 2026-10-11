<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Whisper-large-v3-turbo on the NPU

**Status: in progress, not yet a passing test suite.** This README says
plainly what works, what is verified, and what is still open, rather than
presenting an unfinished port as done. See
`$ESHARE/iron-next-shared/skill-ports/whisper-large-v3-turbo/{stats,skill-gaps}.md`
for the full, timestamped record this summarizes.

Whisper-large-v3-turbo is the first encoder-decoder (as opposed to
decoder-only) model on IRON: a 32-layer bidirectional audio encoder
(`WhisperEncoder`) feeding a 4-layer causal text decoder
(`WhisperDecoder`, an `iron.lm.CausalLM`) through cross-attention. Both
towers are a plain pre-norm transformer: `LayerNorm` with a learned
weight and bias (not `RMSNorm`), a plain GELU feed-forward (not SwiGLU
gating), and every projection but `k_proj` carries a bias. The encoder's
position embedding is a fixed sinusoidal table (stored in the checkpoint,
loaded as a plain weight) and the decoder's a learned one, both added
once rather than rotated per layer the way RoPE is elsewhere in `iron.lm`.

## What is verified

- **The checkpoint layout** (`encoder_layout`/`decoder_layout`): loads
  byte-for-byte against the real `model.safetensors` -- every one of its
  587 tensor names, shapes and the strict count, nothing missing or extra.
- **The oracle vs. Hugging Face** (skill step 6.1): a from-scratch numpy
  reimplementation of this model's architecture (not composed from the
  operators' own references) matches the real `openai/whisper-large-v3-turbo`
  (`transformers` 5.19.0) end to end on a synthetic clip: encoder hidden
  state mean abs error 9.9e-6; decoder logits (4 teacher-forced prompt
  positions) KL(HF||oracle) ~1e-7 per position, 4/4 top-1.
- **The feature extraction formula**: a from-scratch numpy
  reimplementation of Hugging Face's `WhisperFeatureExtractor` (Slaney mel
  scale, a power not magnitude spectrum, `log10`, the per-clip clamp and
  affine) checked against the real extractor directly: the mel filterbank
  bit-exact, the full formula within 2.1e-6.
- **Both towers trace and compile device-free at full scale** (32 encoder
  layers, 4 decoder layers), and run on real NPU2 hardware end to end:
  the encoder's log-mel-through-`log10` stage, its conv front end, its
  32-layer stack and its per-decoder-layer cross-attention k/v projection
  all on the device; the decoder's cross-attention k/v crossing from the
  encoder's compiled graph via one host round-trip a clip (`.write()`,
  the same mechanism `CausalLM.generate` already uses for its draws), its
  self-attention via the inherited cache/`attend` machinery, 4 real decode
  steps run against the real checkpoint.

## What is NOT yet verified: the accuracy gate (skill step 6.2)

Running the whole pipeline on real hardware against the real checkpoint
and comparing to Hugging Face directly (not through the oracle) gives:

- encoder hidden state: mean abs error ~0.165 (not bf16 noise)
- decoder logits (4 positions): KL(HF||device) 0.07 / 1e-6 / 0.04 / 0.28,
  3/4 top-1

This traces to a real, measured library limit, not a wiring bug in this
model (confirmed device-free, via `graph.reference()`, before any
hardware was involved): **`MHA`'s `kv_len` must itself be a whole 64-row
block at least `seq_pad` long**, so a model whose valid key count (here,
1500, which has no factor of 8) is narrower than its padded buffer cannot
bound the extra rows out of attention the way a dynamic cache span can.
Both the encoder's self-attention and every decoder layer's
cross-attention currently attend over the full `hidden_rows` (1536)
positions, 36 of them (2.3%) tile padding, unmasked. Isolating by layer
count shows this costs real accuracy (not a negligible rounding effect):
one layer alone matches an independent oracle to ordinary bf16 noise
(~0.004 mean abs error); the full 32-layer stack, still device-free,
differs from an oracle that *also* carries this same gap by ~0.047
(plausible depth-accumulated bf16 noise on top); the real device differs
from that gap-matching oracle by a further ~0.107. Fixing this needs
either a genuine bound-extent mechanism for a *literal* (not
`Scratchpad`-driven) slice, or a real additive mask in `MHA`, and is a
shared-library change (`iron/operators/mha.py`) deliberately left for
whoever owns that mechanism next rather than built ad hoc by this port --
see `skill-gaps.md` for the full reasoning.

Also still open: the remaining real-hardware-vs-`reference()` gap beyond
even the kv-bound gap is not yet separated out (more real bf16 rounding
than the operator-level references model, or a second issue not yet
found).

## What is not built at all yet

- A `Runner` (checkpoint -> tokenizer -> model, `iron.lm.Runner`'s own
  pattern) tying the pieces above together, including the vocab padding
  (51866 -> 51872, `Sample` needs an *even* vocab slice per core, not just
  a divisible one -- the real checkpoint's 587-tensor embedding loads at
  51866 and is padded with 6 zero rows by hand afterward) and the
  encoder-to-decoder `encode()`/`.write()` handoff, both exercised so far
  only by hand in `scratch/whisper/device_{encoder,decoder}_check.py`
  (outside the IRON tree).
- A device test (`test.py`), a tuning profile beyond the placeholder
  `profiles/npu2.json` (empty, every tunable left to resolve on its own),
  and `tune.py`.
- A tokenizer wrapper and the special-token prompt convention
  (`<|startoftranscript|>`, a language token, `<|transcribe|>`,
  `<|notimestamps|>`) as a first-class part of the model rather than
  values read by hand from `generation_config.json` in a scratch script.

## Library changes this port made

See `$ESHARE/iron-next-shared/skill-ports/LIBRARY.md` (search
`whisper-port`) for the full reasoning and verification of each:

- `RowwiseAdd` (`iron/operators/elementwise_add.py`) and
  `project(bias=)` (`iron/lm/blocks.py`): a linear projection's bias,
  reconciled with qwen2.5-port's own prior claim of the same need
  (byte-identical `RowwiseAdd`; `project(bias=)` keeps an explicit
  row-count computation rather than a `.reshape(-1, ...)` both ports
  independently found broken).
- `project(k_tile=)`: `flm.GEMM`'s own K tiling, for `emb_dim` (1280), not
  a multiple of its default.
- `Conv1d` (`iron/lm/blocks.py`): a 1-D convolution over rows (time) of a
  full-channel-depth input, for the encoder's conv front end --
  `Conv2d`'s square, two-axis kernel has no path for a shape with no
  spatial width axis at all.
- `feed_forward()`'s own wide-`ffn_dim` split (not a library change: a
  model-level technique, splitting `fc1`/`fc2`'s plain numpy weight
  arrays into whole pieces once and summing partial, cap-respecting
  projections) for `RowwiseAdd`'s 4096-element `tile_cap`, which
  `ffn_dim` (5120) exceeds. An earlier attempt folded this with a shared
  `iron.state()` allocated inside a traced call rather than a graph's own
  `__init__`; it compiled clean device-free at every scale tried while
  giving wrong numbers on real hardware -- see `skill-gaps.md` for what
  that means for any future library helper called from inside `body()`.

## Setup

Set up IRON as the repository root describes. Weights:
`openai/whisper-large-v3-turbo`'s `model.safetensors`, at
`$IRON_EXAMPLE_WEIGHTS_DIR/whisper-large-v3-turbo/` (`IRON_EXAMPLE_WEIGHTS_DIR`
defaults to `/srv`).
