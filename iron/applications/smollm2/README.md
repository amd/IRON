<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# SmolLM2 1.7B Instruct on the NPU

Hugging Face's SmolLM2 1.7B Instruct is Llama 3's architecture at its own
shape, run on Llama's model with a `tokenizer.json` and its own tunables
(`profiles/`); `model.py`'s docstring gives the shape. How to run, test and tune it is the README's [Models](../../../README.md#models); the shared library is [AGENTS.md](../../../AGENTS.md#language-models).

Full multi-head attention has no KV groups to share, so a prompt chunk's
attention over the whole context streams about four times the keys and
values a grouped-query model of its width does: the deepest prompt chunk
(`tests/applications/long_context`) is the longest dispatch it makes.

## Weights and tokenizer

From Hugging Face
([`HuggingFaceTB/SmolLM2-1.7B-Instruct`](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct),
Apache-2.0): `model.safetensors`, `tokenizer.json` and `config.json`.
