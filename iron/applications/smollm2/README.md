<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# SmolLM2 1.7B Instruct on the NPU

Hugging Face's SmolLM2 1.7B Instruct is Llama 3's architecture at its own
shape: full multi-head attention (32 heads, each its own KV group), 24
layers, an unscaled RoPE base of 130000, a tied head and an 8192-position
context. `iron/applications/smollm2/model.py` runs it on Llama's model
(`iron.applications.llama`), read from its `config.json`; what is its own
is its tokenizer (`tokenizer.json`, BPE, BOS `<|im_start|>`) and its
tunables (`profiles/`).

Full multi-head attention has no KV groups to share, so a prompt chunk's
attention over the whole context streams about four times the keys and
values a grouped-query model of its width does: the deepest prompt chunk
(`tests/applications/long_context`) is the longest dispatch it makes.

## Weights and tokenizer

From Hugging Face
([`HuggingFaceTB/SmolLM2-1.7B-Instruct`](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct),
Apache-2.0): `model.safetensors`, `tokenizer.json` and `config.json`. The
tests look for them in `$IRON_EXAMPLE_WEIGHTS_DIR/smollm2-1.7b-instruct/`.

## Running

```bash
python -m iron.applications.smollm2.model \
    /path/to/model.safetensors /path/to/tokenizer.json \
    --prompt-len 2048 --num-tokens 40
```

The options are `iron.applications.llama.model`'s own (see its README).

## Testing

```bash
pytest tests/applications/smollm2/
```
