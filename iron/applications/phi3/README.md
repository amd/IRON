<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Phi-4-mini-instruct on the NPU

Prefill and decode of Phi-4-mini-instruct as one IRON graph, `Phi4`, a
version compiled per input shape, judged against transformers as Llama is
(see `iron/applications/llama/README.md`).

What is Phi-4-mini-instruct's own is in `iron/applications/phi3/model.py`:
its shape (`Phi4Config.from_checkpoint`, from `config.json`), its
checkpoint's names (`Phi4.sanitize`) and its tokenizer's lead token; its
tunables are in `iron/applications/phi3/profiles/`. The rest is `iron.lm`,
shared with every other model.

## Phi-4-mini-instruct vs. Llama 3

Three differences, none needing an operator of its own:

- **Fused projections.** Its checkpoint holds one `qkv_proj` and one
  `mlp.gate_up_proj` (`gate` first, then `up`), which `Phi4.sanitize`
  cuts by rows at load, each piece a view of the checkpoint's own array.
- **Partial rotary.** Only the first `rotary_dim` (96 of 128) dimensions
  of each head rotate; the rest pass through unrotated
  (`partial_rotary_factor` in `config.json`, from which
  `Phi4Config.__post_init__` derives `rotary_dim`, which `Attention`
  takes).
- **LongRoPE.** It serves the native 131072 positions. Hugging Face
  rotates a forward call by the `long_factor` frequencies when its
  sequence passes `original_max_position_embeddings` (4096), else by the
  `short_factor` ones (every entry 1.0), each with LongRoPE's constant
  amplitude scale; rows a cache holds keep the rotation they were written
  with. The model holds both tables (`Phi4Config.angles`, short below 4096
  and long from it, which a decode step reads at its position, and
  `long_angles`, stacked after it): a prompt whose sequence passes 4096
  reads the long one through its per-call `rope_start`. A turn runs from
  its first new token (decision 50), so no cached row is rotated again.

Every other shape is Llama's: GQA, RMSNorm, a gated SiLU feed-forward, a
tied output head.

## Weights and tokenizer

From Hugging Face
([`microsoft/Phi-4-mini-instruct`](https://huggingface.co/microsoft/Phi-4-mini-instruct)):

- `model.safetensors` (or a sharded checkpoint's
  `model.safetensors.index.json` and its shards)
- `tokenizer.json`
- `config.json`: the model's shape (`Phi4Config.from_checkpoint`), read
  from beside the checkpoint rather than hand-copied

The tests look for all of these in
`$IRON_EXAMPLE_WEIGHTS_DIR/phi-4-mini-instruct/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`); on the command line they
can be anywhere, with `config.json` beside the checkpoint.

## Setup

Set up IRON as the repository root describes, then:

```bash
python3 -m pip install -r requirements_examples.txt
```

## Running

From the repository root:

```bash
python -m iron.applications.phi3.model \
    /path/to/model.safetensors /path/to/tokenizer.json \
    --prompt-len 2048 --num-tokens 40 --no-full-elf
```

The options are `iron.applications.llama.model`'s own (see its README):
`--random-weights`, `--prompt-len`, `--num-tokens`, `--max-seq-len`,
`--temperature`, `--top-k`, `--check-accuracy`, `--check-determinism`,
`--compare-host`, `--cost-table` and `--full-elf`/`--no-full-elf`.
`--no-full-elf` is the form this model's tests run it in: the full-ELF
link is impractically slow at this model's depth (32 layers), the same
finding Qwen 2.5 1.5B Instruct's own port made.

## Testing

```bash
pytest tests/applications/phi3/
```

`test.py` loads the real checkpoint once and runs the throughput,
sampling, accuracy and determinism checks above in-process through
`model.Runner`. `reference/test.py` needs no checkpoint and no NPU: it runs
the graph on the host over random toy weights against transformers' Phi-3
on the same weights, its logits recorded in `reference/goldens/` (`pytest
--record-goldens -p no:xdist` records them), from an empty cache, across a
chunk boundary, and past LongRoPE's original context.
