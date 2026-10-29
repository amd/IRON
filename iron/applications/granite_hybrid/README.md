<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Granite 4.0-H

IBM's Granite 4.0-H, `GraniteHybrid` in `model.py`, whose docstring says how
it differs from Granite: Mamba2 mixers in most layers' place of attention,
and a shared MLP. This package ships the dense 1B; a checkpoint with
experts is refused. The shared library is
[AGENTS.md](../../../AGENTS.md#language-models).

The dense 1B runs on the NPU from its real checkpoint: every layer, the
Mamba2 scan (`SelectiveScan`) and causal convolution included, one compile
serving every prompt length and its native 131072 positions, the scan's
state checkpointed at each 2048-position chunk boundary so a chat turn
reruns only its last chunk. `tests/applications/granite_hybrid/test.py`
checks it against Hugging Face's float32 model, and `reference/` the graph
at a dense toy, device-free.

## Weights and tokenizer

From Hugging Face (Apache-2.0, ungated), over plain https, with no account:

```bash
D=/path/to/granite-4.0-h-1b
REV=d18cca4c121edb87d022116d281ce212c9136f57  # the revision the tests' bounds were set against
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

Its prompt chunk's projections run at `Precision.HIGH`, `GraniteConfig`'s
default: bf16 macs, each K tile's partial sums rounded once. Against
MEDIUM (bfp16 macs), HIGH held the 40 teacher-forced steps closer to the
float32 model, and MEDIUM the two-chunk prompt. A decode step's projections are GEMVs, which sum in float32 at
any precision. HIGHEST (float32 partial sums) has not been measured.

## Testing

`tests/applications/granite_hybrid/test.py` holds the device, at one compile
for the native context, to the float32 golden recorded beside the checkpoint
(`golden.npz`): the KL over 40 teacher-forced steps, and over a prompt of
two chunks and the decode steps after it, within its `MAX_KL`. A chat turn
rerun from the states checkpointed at the chunk boundary must match the run
from scratch bit for bit, and repeated runs must be bitwise identical. A
prompt chunk's scan streams all 2048 rows whatever the prompt's length.
Time to first token and tokens per second are recorded to CI
([benchmarks](https://amd.github.io/IRON/benchmarks/)).

On NPU1 the each-step tests (`TestEachStep`) and `long_context`'s are
enabled, with an empty `profiles/npu1.json` (every operator's device
defaults), but have not run on an NPU1 device yet.
