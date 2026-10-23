<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# SmolLM3 3B on the NPU

Hugging Face's SmolLM3 3B, `SmolLM3` in `model.py`, whose docstring says
how it differs from Llama: no RoPE on every fourth layer. How to run, test and tune it is the README's [Models](../../../README.md#models); the shared library is [AGENTS.md](../../../AGENTS.md#language-models).

It has no `profiles/` yet: its tunables are the operators' defaults until
`python -m iron.lm.tune smollm3` is run on an NPU.

## Weights and tokenizer

From Hugging Face
([`HuggingFaceTB/SmolLM3-3B`](https://huggingface.co/HuggingFaceTB/SmolLM3-3B),
Apache-2.0), in one directory: `model.safetensors.index.json` and its two
shards, `tokenizer.json`, `chat_template.jinja` and `config.json`.
