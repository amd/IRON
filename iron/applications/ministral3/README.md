<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Ministral 3

Mistral AI's Ministral 3 3B Base's text decoder, `Ministral3` in
`model.py`, whose docstring says how it differs from Llama: YaRN's RoPE
and Llama 4's query temperature past the 16384 positions it was trained
at. The shared library is [AGENTS.md](../../../AGENTS.md#language-models).

## Weights and tokenizer

[`mistralai/Ministral-3-3B-Base-2512`](https://huggingface.co/mistralai/Ministral-3-3B-Base-2512)
(Apache-2.0, ungated), over plain https, with no account; the Hugging Face
format only (not `consolidated.safetensors`):

```bash
D=/path/to/ministral-3-3b-base-2512
REV=6f9c4b12a95b139af68670a6713616b757923735  # the revision every KL figure here is against
for f in config.json generation_config.json processor_config.json \
    tokenizer_config.json special_tokens_map.json tokenizer.json \
    model.safetensors.index.json model-00001-of-00002.safetensors \
    model-00002-of-00002.safetensors; do
  curl -fL -o "$D/$f" \
    "https://huggingface.co/mistralai/Ministral-3-3B-Base-2512/resolve/$REV/$f"
done
```

The checkpoint is Mistral 3's vision-language model, the text decoder
nested under it (`text_weights` reads transformers 4's and 5's nestings),
its head tied to the embedding. Its native context is 262144 positions,
whose caches (26 GiB) do not fit beside the 7.7 GB of weights on a 27 GB
host, so `Model.fit` serves the longest whole number of chunks that does
(124928 positions on xcoradaie211) and says so.

The Instruct checkpoints are FP8 (`weight_scale_inv`), which `Ministral3`
refuses: reading them is a TODO.

## Precision

Its prompt chunks' projections run at flm.ProjectionGEMM's default,
`Precision.MEDIUM` (bfp16 macs); a decode step is a GEMV, which sums in
float32 whatever the precision. HIGH and HIGHEST are not measured yet.

## Accuracy and speed

On Strix (npu2, xcoradaie211), one compile at 124928 positions, against
the float32 golden recorded beside the checkpoint (`golden.npz`): KL over
40 teacher-forced steps after 301 tokens, mean 0.0049, p90 0.0071, max
0.093 (one top-1 swap); over a prompt of 3349 tokens, two chunks, and two
decode steps after it, max 0.0063; and a prompt of 17000 tokens, past the
trained context, KL 2e-8 (the text repeats there, so the distributions are
peaked: the test also holds the logits to `assert_close`). A chat turn is
bit for bit the run from scratch. The first token takes 0.58 s after 13
tokens.
