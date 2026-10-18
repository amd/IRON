<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Qwen 2.5 1.5B Instruct on the NPU

Prefill and decode of Qwen 2.5 as one IRON graph, `Qwen2`, a version
compiled per input shape, from Qwen 2.5 1.5B Instruct's config and weights,
judged against transformers as Llama is (see
`iron/applications/llama/README.md`).

Qwen 2 is Llama's layer with one difference a Llama checkpoint has no
place for: its q/k/v projections each carry a bias, which `Attention`
(`iron/lm/blocks.py`) adds wherever the checkpoint holds one. It ties its
embedding and output head, as Llama does, and takes no RoPE frequency
scaling.

What is Qwen 2's own is short, and all of it is in
`iron/applications/qwen2/model.py`: its shape
(`DecoderConfig.from_checkpoint`, from `config.json`) and its tokenizer's
lead token; its tunables are in `iron/applications/qwen2/profiles/`. The
rest is `iron.lm`, shared with every other model.

`python -m iron.lm.tune qwen2 --checkpoint /path/to/model.safetensors`
rewrites its profile for the NPU it runs on, as
`iron/applications/llama/README.md`'s "Tuning" section describes.

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
`--compare-host` and `--full-elf`/`--no-full-elf`.
`--no-full-elf` is the form this model's tests run it in: the full-ELF
link does not finish in a practical time at this shape (see
`skill-ports/qwen2.5-1.5b/skill-gaps.md`).

## Testing

```bash
pytest tests/applications/qwen2/
```

Loads the model once and runs the throughput, device-sampling, accuracy
and determinism checks above in-process through `model.Runner`.
