<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Qwen 2.5 1.5B Instruct on the NPU

Prefill and decode of Qwen 2.5 as one IRON graph, `Qwen2`, a version
compiled per input shape, and the float32 numpy forward pass it is checked
against, `Qwen2Oracle`, its `oracle`. Both are built from the same config
and weights, Qwen 2.5 1.5B Instruct's here; nothing here needs torch.

Qwen 2 is Llama's layer (`iron.lm.Layer`) with one difference a Llama
checkpoint has no place for: its q/k/v projections each carry a bias, which
`Layer` reads from the checkpoint and adds once per output column across
every row (`project(..., bias=...)`, folded with `RowwiseAdd`). It ties its
embedding and output head, as Llama does, and takes no RoPE frequency
scaling.

What is Qwen 2's own is short, and all of it is in
`iron/applications/qwen2/model.py`: its head on the NPU and in numpy, its
shape (`DecoderConfig.from_checkpoint`, from `config.json`),
where its checkpoint keeps each weight by its own name, and its tokenizer;
its tunables are in `iron/applications/qwen2/profiles/`. The rest is
`iron.lm`, shared with every other model (see
`iron/applications/llama/README.md`'s description of `CausalLM`, `Oracle`,
`Checkpoint`/`DecoderConfig`, `Runner` and `generation`/`testing`).

`python -m iron.lm.tune qwen2 --checkpoint /path/to/model.safetensors`
measures the cost table its designs can be narrowed and packed by (below).

## Weights and tokenizer

From Hugging Face:

- [`model.safetensors`](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)
- [`tokenizer.json`](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)
- [`config.json`](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct/blob/main/config.json):
  the model's shape (`DecoderConfig.from_checkpoint`), read from beside the
  checkpoint rather than hand-copied

The tests look for all three in
`$IRON_EXAMPLE_WEIGHTS_DIR/qwen2.5-1.5b-instruct/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`); on the command line the
checkpoint and tokenizer can be anywhere, with `config.json` beside the
checkpoint.

## Setup

Set up IRON as the repository root describes, then:

```bash
python3 -m pip install -r requirements_examples.txt
```

## Running

From the repository root:

```bash
python -m iron.applications.qwen2.model \
    /path/to/model.safetensors /path/to/tokenizer.json \
    --prompt-len 2048 --num-tokens 40 --no-full-elf
```

The options are `iron.applications.llama.model`'s own (see its README):
`--random-weights`, `--prompt-len`, `--num-tokens`, `--max-seq-len`,
`--temperature`, `--top-k`, `--check-accuracy`, `--check-determinism`,
`--compare-host`, `--cost-table` and `--full-elf`/`--no-full-elf`.
`--no-full-elf` is the form this model's tests run it in: the full-ELF
link does not finish in a practical time at this shape (see
`skill-ports/qwen2.5-1.5b/skill-gaps.md`).

## Testing

```bash
pytest tests/applications/qwen2/
```

Loads the model once and runs the accuracy, determinism and throughput
checks above in-process through `model.Runner`.
