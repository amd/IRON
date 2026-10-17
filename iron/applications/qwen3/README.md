<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Qwen3 1.7B on the NPU

Prefill and decode of Qwen3 1.7B as one IRON graph, `Qwen3`, a version
compiled per input shape, and the float32 numpy forward pass it is checked
against, `Qwen3Oracle`, its `oracle`. Both are built from the same config
and weights; nothing here needs torch.

What is Qwen3's own is short, and all of it is in
`iron/applications/qwen3/model.py`: its head on the NPU and in numpy, its
shape (`DecoderConfig.from_checkpoint`, from `config.json`),
where its checkpoint keeps each weight by its own name, and its tokenizer;
its tunables are in `iron/applications/qwen3/profiles/`. The rest is
`iron.lm`, shared with every other model, its layers `iron.lm.Layer` (see
`iron/applications/llama/README.md`'s description of `CausalLM`, `Oracle`,
`Checkpoint`/`DecoderConfig`, `Runner` and `generation`/`testing`).

## Qwen3 vs. Llama 3

One difference from Llama's own layer: **per-head RMSNorm on Q and K,
before RoPE** (`q_norm`/`k_norm`, one weight row of `head_dim`, shared by
every head and every position), which `Layer` reads from the checkpoint's
`self_attn`, at its config's `rms_norm_eps` (1e-6).

Its output head is the input embedding, tied (`tie_word_embeddings: true`
in its `config.json`); its checkpoint also ships `lm_head.weight`,
confirmed byte-identical to `model.embed_tokens.weight` by sha256, which
sits unread in its checkpoint tree (`Checkpoint.tree()` maps every tensor
the checkpoint has; nothing here reads this one).

Its checkpoint is sharded (two `.safetensors` files and a
`model.safetensors.index.json`); `Checkpoint` reads the index directly
(passed as `weights_path`, in place of a single `.safetensors` file),
mapping every shard the index names.

## Weights and tokenizer

From Hugging Face ([`Qwen/Qwen3-1.7B`](https://huggingface.co/Qwen/Qwen3-1.7B), Apache-2.0):

- `model-00001-of-00002.safetensors`, `model-00002-of-00002.safetensors`,
  `model.safetensors.index.json`
- `tokenizer.json`
- `config.json`: the model's shape (`DecoderConfig.from_checkpoint`), read
  from beside the checkpoint rather than hand-copied

The tests look for all of these in `$IRON_EXAMPLE_WEIGHTS_DIR/qwen3-1.7b/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`); on the command line they
can be anywhere, with `config.json` beside the checkpoint.

Qwen3 0.6B is the same model at another shape, read from its own
`config.json`: its `model.safetensors`, `tokenizer.json` and `config.json`
from [`Qwen/Qwen3-0.6B`](https://huggingface.co/Qwen/Qwen3-0.6B), in
`$IRON_EXAMPLE_WEIGHTS_DIR/qwen3-0.6b/`; the tests run each checkpoint. The tokenizer
loads through the `tokenizers` package (already a dependency of
`requirements_examples.txt`), not `transformers`: nothing here needs torch.

## Setup

Set up IRON as the repository root describes, then:

```bash
python3 -m pip install -r requirements_examples.txt
```

## Running

From the repository root:

```bash
python -m iron.applications.qwen3.model \
    /path/to/model.safetensors.index.json /path/to/tokenizer.json \
    --prompt-len 2048 --num-tokens 40
```

The options are `iron.applications.llama.model`'s own (see its README):
`--random-weights`, `--prompt-len`, `--num-tokens`, `--max-seq-len`,
`--temperature`, `--top-k`, `--check-accuracy`, `--check-determinism`,
`--compare-host`, `--cost-table` and `--full-elf`/`--no-full-elf`.

Qwen3's `head_dim` is 128, twice Llama 3.2 1B's 64: MHA's block-size
search (the largest block whose cores fit L1 at this head size) picks a
smaller block there, which at the default `num_pipelines=1` pushes a
prompt chunk's K/V fill past the DMA descriptor's 64-iteration cap.
`profiles/npu1.json` pins `num_pipelines=4` for the prompt-chunk shape
(the same value Llama's own NPU1 profile uses), which keeps the block
count the fill repeats under the cap.

## Tuning

`python -m iron.lm.tune qwen3 --checkpoint /path/to/model.safetensors.index.json`
measures the cost table its designs can be narrowed and packed by, as
`iron/applications/llama/README.md`'s "Tuning" section describes.

## Testing

```bash
pytest tests/applications/qwen3/
```

Loads the model once and runs the accuracy, determinism and chunk-boundary
checks above in-process through `model.Runner`.
