<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Qwen3.5 0.8B on the NPU

Qwen3.5's text decoder, `Qwen35` in `model.py`, whose docstring says how it
differs from Llama: most layers' attention a Gated DeltaNet, the attention
layers gated and partially rotated, every norm scaling by `1 + weight`. The
shared library is [AGENTS.md](../../../AGENTS.md#language-models).

## The multi-token prediction head

The checkpoint also holds `mtp.*`, a multi-token prediction head: one more
layer and a projection that guess the token after next from the last hidden
state and the next token's embedding. It is a speculative-decoding add-on:
it proposes draft tokens that the model itself then checks, so it changes
how fast a sequence is drawn, never which tokens are drawn. transformers
does not run it (`Qwen3_5ForConditionalGeneration` drops `mtp.*` as it
loads, `_keys_to_ignore_on_load_unexpected`), so neither does this port,
and the logits it is judged by are the model's own.

## Weights and tokenizer

From Hugging Face
([`Qwen/Qwen3.5-0.8B`](https://huggingface.co/Qwen/Qwen3.5-0.8B)):
`model.safetensors.index.json` and its shard, `tokenizer.json`,
`chat_template.jinja` and `config.json`.

## Testing

```bash
pytest tests/applications/decoders/ -k qwen3_5
pytest tests/applications/qwen3_5/
```

The decoders suite checks generation, accuracy against transformers' float32
model and determinism on the NPU; `reference/` checks the decoder
device-free at a toy shape over random weights.
