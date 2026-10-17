<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# LFM2-1.2B on the NPU

LiquidAI's LFM2-1.2B: a hybrid decoder, sixteen layers of which only six
(`full_attn_idxs`, from `config.json`) are full attention; the rest are a
gated short causal convolution (`conv_L_cache=3` taps, depth-wise, one tap
row a channel) in place of attention. Every layer still ends in the same
SwiGLU feed-forward. `Lfm2` is the NPU graph, over the shared decoder
(`iron.lm`); `Lfm2Oracle` its float32 numpy forward pass, which it is
judged by; both are in `model.py`.

`layer()` dispatches on which the checkpoint gives a layer, per index
(`"self_attn" in vars(w)`): an attention layer is `iron.lm.Layer`'s, which
reads LFM2's own names (`operator_norm`/`ffn_norm`, `q_layernorm`/
`k_layernorm` before RoPE, `out_proj`, `feed_forward.w1`/`w3`/`w2`); a
conv layer is its short conv in attention's place, then `Layer`'s
feed-forward block (`Layer.feed_forward`). A conv layer's three per-channel taps, a row each derived
once at load (`iron.lm.Derived`), read a window spanning the current call
and the `conv_kernel - 1` gated rows before it. Those rows are the layer's
`iron.lm.Checkpoints` state, a slot per prompt-chunk boundary: a prompt
chunk reads its boundary's slot and writes the next, a decode step its
chunk's own, so a prompt may resume from any chunk (a chat turn) after
positions decode steps wrote. Slot 0, never written, is zero: "before the
sequence". A call assembles its window in a `(2, prefill_chunk, conv_dim)`
scratch state before three `RowwiseMul`s (one a tap) and two
`ElementwiseAdd`s sum it (`Lfm2.conv`, parallel to the base class's
`attend`). Only the six attention layers hold key and value caches
(`CausalLM` allocates them where a layer holds `self_attn`).

## Weights and tokenizer

From Hugging Face: [`LiquidAI/LFM2-1.2B`](https://huggingface.co/LiquidAI/LFM2-1.2B)
(`model.safetensors`, `tokenizer.json`, `config.json`), ungated.

The tests look for all three in `$IRON_EXAMPLE_WEIGHTS_DIR/lfm2-1.2b/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`); on the command line they
can be anywhere, with `config.json` beside the checkpoint.

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

The options are `iron.applications.llama.model`'s own (see its README):
`--random-weights`, `--prompt-len`, `--num-tokens`, `--max-seq-len`,
`--temperature`, `--top-k`, `--check-accuracy`, `--check-determinism`,
`--compare-host`, `--cost-table` and `--full-elf`/`--no-full-elf`.

## The arena past one bank

At its native 128000 positions, LFM2-1.2B's weights, six attention
layers' key/value caches and ten conv layers' checkpointed rows pin 3.68
GiB before the activations. The arena is banks of at most 3.5 GiB, each
its own buffer object and argument (`iron/common/image/allocator.py`'s
`BANK`), inside what one buffer object can address within `aiebu`'s
32-bit relocation addend, the limit Granite 4.2 3B's port found; so both
the decode step and the prompt chunk link as a full ELF (device loop) on
NPU2.

## Tuning

`python -m iron.lm.tune lfm2 --checkpoint /path/to/model.safetensors`
measures the cost table its designs can be narrowed and packed by, as
`iron/applications/llama/README.md`'s "Tuning" section describes.

## Testing

```bash
pytest tests/applications/lfm2/
```

Loads the model once and runs the accuracy, determinism and chunk-boundary
checks above in-process through `model.Runner`.
