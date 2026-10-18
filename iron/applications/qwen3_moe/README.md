<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Qwen3-30B-A3B on the NPU

Qwen3-30B-A3B, `Qwen3Moe` in `model.py`, whose docstring says how it
differs from Qwen3: a mixture of 128 experts, 8 a token, in place of the
feed-forward. How to run, test and tune it is the README's [Models](../../../README.md#models); the shared library is [AGENTS.md](../../../AGENTS.md#language-models).

The experts' feed-forwards are `Experts`, an operator with a reference and
no kernel yet: the model runs on the host (`OnHost`) and refuses to
compile until one lands. Its weights are 61 GB in bf16, every expert held.

## Weights and tokenizer

From Hugging Face
([`Qwen/Qwen3-30B-A3B`](https://huggingface.co/Qwen/Qwen3-30B-A3B),
Apache-2.0), in one directory: `model.safetensors.index.json` and its
shards, `tokenizer.json` and `config.json`.
