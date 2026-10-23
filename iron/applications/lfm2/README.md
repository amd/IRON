<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# LFM2-1.2B on the NPU

LiquidAI's LFM2-1.2B, a hybrid decoder: six of its sixteen layers are full
attention and the rest a gated short convolution, whose last rows are
carried from chunk to chunk as `iron.lm.Checkpoints` state. `Lfm2` in
`model.py`, whose docstring describes the layers. How to run, test and tune it is the README's [Models](../../../README.md#models); the shared library is [AGENTS.md](../../../AGENTS.md#language-models).

## Weights and tokenizer

From Hugging Face: [`LiquidAI/LFM2-1.2B`](https://huggingface.co/LiquidAI/LFM2-1.2B)
(`model.safetensors`, `tokenizer.json`, `config.json`), ungated.

At its native 128000 positions, the weights, six attention layers' caches
and ten conv layers' carried rows pin 3.68 GiB before the activations, more
than one of the arena's banks (`iron.common.image.allocator.BANK`, 3.5
GiB); both versions still link as a full ELF on NPU2.

## Testing

`tests/applications/lfm2/test.py` also runs a two-chunk prompt and a chat
turn. `reference/test.py` needs no checkpoint and no NPU: it compares the
graph on the host over random toy weights with transformers' LFM2, across
prompt chunks, decode steps and chat turns resumed from a boundary.
