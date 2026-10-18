<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Phi-4-mini-instruct on the NPU

Microsoft's Phi-4-mini-instruct, `Phi4` in `model.py`, whose docstring
says how it differs from Llama: fused projections, partial rotary and
LongRoPE at its native 131072 positions. How to run, test and tune it is the README's [Models](../../../README.md#models); the shared library is [AGENTS.md](../../../AGENTS.md#language-models).

## Weights and tokenizer

From Hugging Face
([`microsoft/Phi-4-mini-instruct`](https://huggingface.co/microsoft/Phi-4-mini-instruct)):
`model.safetensors` (or a sharded checkpoint's
`model.safetensors.index.json` and its shards), `tokenizer.json` and
`config.json`.

## Running

Pass `--no-full-elf`, the form its tests run: the full-ELF link is
impractically slow at its depth (32 layers).

## Testing

`tests/applications/phi3/reference/test.py` needs no checkpoint and no NPU:
it compares the graph on the host over random toy weights with
transformers' Phi-3, from an empty cache, across a chunk boundary, and past
LongRoPE's original context.
