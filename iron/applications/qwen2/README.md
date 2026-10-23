<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Qwen 2.5 1.5B Instruct on the NPU

Qwen 2.5 1.5B Instruct, `Qwen2` in `model.py`, whose docstring says how it
differs from Llama: a bias on the q, k and v projections. How to run, test and tune it is the README's [Models](../../../README.md#models); the shared library is [AGENTS.md](../../../AGENTS.md#language-models).

## Weights and tokenizer

From Hugging Face
([`Qwen/Qwen2.5-1.5B-Instruct`](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)):
`model.safetensors`, `tokenizer.json` and `config.json`.

## Running

Pass `--no-full-elf`, the form its tests run: the full-ELF link does not
finish in a practical time at this shape.
