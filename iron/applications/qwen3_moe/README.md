<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Qwen3-30B-A3B on the NPU

Qwen3-30B-A3B, `Qwen3Moe` in `model.py`, whose docstring says how it
differs from Qwen3: a mixture of 128 experts, 8 a token, in place of the
feed-forward. The shared library is [AGENTS.md](../../../AGENTS.md#language-models).

The experts' feed-forwards are `Experts`, an operator with a reference and
no kernel yet, so the model has no device run until one lands: its test is
the device-free `tests/applications/qwen3_moe/reference/`. Its weights are
61 GB in bf16, every expert held, and stacked into one copy as they load.

## Weights and tokenizer

From Hugging Face
([`Qwen/Qwen3-30B-A3B`](https://huggingface.co/Qwen/Qwen3-30B-A3B),
Apache-2.0), in one directory: `model.safetensors.index.json` and its
shards, `tokenizer.json` and `config.json`.
