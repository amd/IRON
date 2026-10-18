<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Granite 4.2 3B on the NPU

IBM's Granite 4.2 3B, `Granite` in `model.py`, whose docstring says what is
its own: Llama's layer with four scalars from its `config.json`, an untied
head and a sharded checkpoint. How to run, test and tune it is the README's [Models](../../../README.md#models); the shared library is [AGENTS.md](../../../AGENTS.md#language-models).

## Weights and tokenizer

From Hugging Face
([`ibm-granite/granite-4.2-3b`](https://huggingface.co/ibm-granite/granite-4.2-3b),
Apache-2.0, ungated), over plain https, with no account:

```bash
D=/path/to/granite-4.2-3b
REV=e459acceac81e5fe67c07d9cfc72329a332e7eb1  # the revision every KL figure here is against
for f in config.json generation_config.json tokenizer_config.json \
    special_tokens_map.json tokenizer.json model.safetensors.index.json \
    model-00001-of-00002.safetensors model-00002-of-00002.safetensors; do
  curl -fL -o "$D/$f" \
    "https://huggingface.co/ibm-granite/granite-4.2-3b/resolve/$REV/$f"
done
```

The checkpoint argument is `model.safetensors.index.json`. Its native
context, 131072 positions, holds 10 GiB of caches beside the weights' 6.8
GiB, the default where the host has room for both (`Runner.fit`).

## Testing

`tests/applications/granite/` also runs the each-step form
(`TestEachStep`, `--no-full-elf`), a two-chunk prompt and a chat turn.
