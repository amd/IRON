<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# SmolLM3 3B on the NPU

Hugging Face's SmolLM3 3B, `SmolLM3` in `model.py`, whose docstring says
how it differs from Llama: no RoPE on every fourth layer. Its projections
are at `Precision.HIGH`, as 3B's other dense decoder (Llama 3.2 3B) and
Granite 4.2 3B are. How to run, test and tune it is the README's [Models](../../../README.md#models); the shared library is [AGENTS.md](../../../AGENTS.md#language-models).

`profiles/npu2.json` holds its attention's pipeline count, four, which its
deep contexts need; `profiles/npu1.json` is empty, so NPU1 runs every
operator at its default. The generation, accuracy and determinism checks
of its full-ELF form are in `tests/applications/decoders` and
`tests/applications/long_context`, beside Gemma 3, Gemma 4, Qwen3.5 and
Qwen3-MoE; its own `test.py` holds only the per-step form NPU1 runs.

## Weights and tokenizer

From Hugging Face
([`HuggingFaceTB/SmolLM3-3B`](https://huggingface.co/HuggingFaceTB/SmolLM3-3B),
Apache-2.0), in one directory: `model.safetensors.index.json` and its two
shards, `tokenizer.json`, `chat_template.jinja` and `config.json`.
