<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Qwen3 1.7B on the NPU

Qwen3 1.7B and 0.6B, `Qwen3` in `model.py`, whose docstring says how it
differs from Llama: a per-head RMSNorm on q and k before RoPE, and an
unread `lm_head.weight` beside its tied head. How to run, test and tune it is the README's [Models](../../../README.md#models); the shared library is [AGENTS.md](../../../AGENTS.md#language-models).

## Weights and tokenizer

From Hugging Face ([`Qwen/Qwen3-1.7B`](https://huggingface.co/Qwen/Qwen3-1.7B), Apache-2.0),
in one directory: `model-00001-of-00002.safetensors`,
`model-00002-of-00002.safetensors`, `model.safetensors.index.json`,
`tokenizer.json` and `config.json`. Qwen3 0.6B is the same model at another shape: its
`model.safetensors`, `tokenizer.json` and `config.json` from
[`Qwen/Qwen3-0.6B`](https://huggingface.co/Qwen/Qwen3-0.6B).

## NPU1's profile

Qwen3's `head_dim` is 128, twice Llama 3.2 1B's: MHA's block-size search
picks a smaller block, which at `num_pipelines=1` pushes a prompt chunk's
K/V fill past the DMA descriptor's 64-iteration cap. `profiles/npu1.json`
pins `num_pipelines=4` for the prompt-chunk shape to stay under it.

Open on NPU1: 1.7B's deepest prompt chunk at its native 40960 positions
differs from the graph's reference by KL 0.148 (`long_context`'s
`test_prompt_deep_in_the_cache`, bound 0.1). It passes at 34816 positions
(4.8e-6), 32768 (2.0e-5) and 16384 (2.1e-6), its deepest decode step
passes at 40960, and the prompt's MHA alone, given its inputs, is as
accurate at 40959 as at 2047.

## Testing

`tests/applications/qwen3/` runs 1.7B's checkpoint and 0.6B's, each also
in the each-step form, over a two-chunk prompt and a chat turn, and checks
that the unread `lm_head.weight` is the tied embedding.
