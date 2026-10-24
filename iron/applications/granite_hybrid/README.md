<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Granite 4.0-H

IBM's Granite 4.0-H, `GraniteHybrid` in `model.py`, whose docstring says how
it differs from Granite: Mamba2 mixers in most layers' place of attention,
a shared MLP, and a mixture of experts in the MoE sizes. The shared library
is [AGENTS.md](../../../AGENTS.md#language-models).

The dense 1B runs on the NPU from its real checkpoint: every layer, the
Mamba2 scan (`SelectiveScan`) and causal convolution included, one compile
serving every prompt length and its native 131072 positions, the scan's
state checkpointed at each 2048-position chunk boundary so a chat turn
reruns only its last chunk. `tests/applications/granite_hybrid/test.py`
checks it against Hugging Face's float32 model, and `reference/` the graph
at an MoE toy and a dense one, device-free.

## Weights and tokenizer

From Hugging Face (Apache-2.0, ungated), over plain https, with no account:

```bash
D=/path/to/granite-4.0-h-1b
REV=d18cca4c121edb87d022116d281ce212c9136f57  # the revision every KL figure here is against
for f in config.json generation_config.json tokenizer_config.json \
    special_tokens_map.json tokenizer.json chat_template.jinja model.safetensors; do
  curl -fL -o "$D/$f" \
    "https://huggingface.co/ibm-granite/granite-4.0-h-1b/resolve/$REV/$f"
done
```

The weights are 2.9 GB. At its native context the Mamba2 states'
checkpoints (float32, 36 layers by 65 chunk boundaries, 3.4 GiB) and the 4
attention layers' caches (1 GiB) make the model 7.2 GiB on the device.

## Precision

Its projections run at `Precision.HIGH` (Granite's config's): bf16 macs,
each K tile's partial sums rounded once. On the checks below, against
MEDIUM (bfp16 macs):

| Precision | KL over 40 steps (mean / p90 / max) | 2 chunks, 3 steps (mean / max) | TTFT, 1024 chars | TPS |
|---|---|---|---|---|
| HIGH | 0.0029 / 0.0051 / 0.0105 | 0.0098 / 0.025 | 3.7 s | 6.7 |
| MEDIUM | 0.0040 / 0.0066 / 0.0186 | 0.0063 / 0.0099 | 3.35 s | 6.7 |

HIGH holds the 40 steps closer, at 10% of the first token's time; a
decode step is a GEMV, which sums in float32 whatever the precision.
HIGHEST (float32 partial sums) is not measured yet.

## Accuracy and speed

On Strix Halo (npu2, xcoradaie220), one compile at the native context,
against the float32 golden recorded beside the checkpoint (`golden.npz`):
KL over 40 teacher-forced steps after 292 tokens, mean 0.0024, p90 0.0048,
max 0.0063; over a prompt of 3261 tokens, two chunks, and two decode steps
after it, max 0.0049. A chat turn rerun from the states checkpointed at the
chunk boundary is bit for bit the run from scratch, and repeated runs are
bitwise identical. The first token takes 2.9 s after a 13-character
prompt (a prompt chunk's scan streams all 2048 rows whatever the prompt's
length), 3.6 s after 292 tokens and 8.0 s after 2048, and decode runs at
6.7 tokens a second; none of it is tuned.

## The mixture-of-experts sizes

[`granite-4.0-h-tiny`](https://huggingface.co/ibm-granite/granite-4.0-h-tiny)
(64 experts of width 512, 6 a token, in all 40 layers, 13.9 GB) builds, but
does not run at a usable rate: `Experts` streams every expert's weights for
each row through one core, 59.8 ms a row a layer at its shape on npu2
(checked against its numpy reference), so about 2.4 s a decoded token and
80 minutes a 2048-row prompt chunk, and its runtime sequence unrolls every
row's every expert. It waits for a sparse, token-grouped prompt path and a
gathered decode GEMV.
