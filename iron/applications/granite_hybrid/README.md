<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Granite 4.0-H

IBM's Granite 4.0-H, `GraniteHybrid` in `model.py`, whose docstring says how
it differs from Granite: Mamba2 mixers in most layers' place of attention,
a shared MLP, and a mixture of experts in the MoE sizes. The shared library
is [AGENTS.md](../../../AGENTS.md#language-models).

The Mamba2 scan is `SelectiveScan`, an operator with a reference and no
kernel yet, so the model has no device run until one lands. Its test is the device-free
`tests/applications/granite_hybrid/reference/`, at an MoE toy and a dense
one.

## Weights and tokenizer

From Hugging Face (Apache-2.0): the dense
[`ibm-granite/granite-4.0-h-1b`](https://huggingface.co/ibm-granite/granite-4.0-h-1b)
and the MoE
[`ibm-granite/granite-4.0-h-tiny`](https://huggingface.co/ibm-granite/granite-4.0-h-tiny),
each in one directory: `config.json`, `model.safetensors` or
`model.safetensors.index.json` and its shards, and `tokenizer.json`. The
checkpoint holds the experts stacked, as `Experts` takes them.
