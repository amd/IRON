<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Llama 3 on the NPU

Prefill and decode of Llama 3 as one IRON graph, `Llama`, a version
compiled per input shape, and the float32 numpy forward pass it is checked
against, `LlamaOracle`, its `oracle`. Both are built from the same config
and weights, Llama 3.2 1B's here; nothing here needs torch.

What is Llama's own is short, and all of it is in `model.py`: its layer
and head on the NPU and in numpy, its shape, where its checkpoint keeps
each weight and its tokenizer; its knobs are in `profiles/`. The rest is
`iron.applications.common`, which a new model reuses the same way:

- `CausalLM`: the body over prefill and decode, the key and value caches,
  attention over them (`attend`) and `logits(tokens)`; a model subclasses
  it with `layer(step, i, weights, x)` and `head(x)`
- `Oracle`: the same model's float32 forward pass on the host, attention
  and RoPE shared; a model subclasses it with `layer(angles, weights, x)`
  and `head(x)` in numpy, and names it as its `CausalLM`'s `oracle`
- `Config`, and a checkpoint `Layout`: each weight's place in the model,
  its name in the checkpoint and its shape, which `load_weights` checks
  strictly
- `Runner`: the checkpoint, the tokenizer, the model and its oracle, and
  `main`, the command line below; a model names its `config`, `layout`,
  `model`, `open_tokenizer` and `bos`
- `generation`: sampling, the generation loop and the accuracy and
  determinism checks; `testing`: what `test.py` checks with them

## Weights and tokenizer

From Hugging Face:

- [`model.safetensors`](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main)
- [`tokenizer.model`](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main/original)

The tests look for them in `$IRON_EXAMPLE_WEIGHTS_DIR/llama3.2-1b/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`); on the command line they
can be anywhere.

## Setup

Set up IRON as the repository root describes, then:

```bash
python3 -m pip install -r requirements_examples.txt
```

## Running

From the repository root:

```bash
python -m iron.applications.llama3.model \
    /path/to/model.safetensors /path/to/tokenizer.model \
    --prompt-len 2048 --num-tokens 40
```

- `--prompt-len`: characters of `common/prompt.txt` to use as the prompt (default 2048)
- `--num-tokens`: tokens to generate (default 40)
- `--temperature`, `--top-k`: the sampler's (default 0.7 and 50)
- `--check-accuracy`: instead of sampling, compare each step's logits with a
  float32 numpy forward pass (`LlamaOracle`) and print the KL divergence
  and top-1 agreement
- `--check-determinism ROUNDS`: instead of sampling, run two prompts
  `ROUNDS` times each and count the runs whose logits differ bitwise

`pytest iron/applications/llama3/` loads the model once and runs
all three in-process through `model.Runner`, recording the throughput and
accuracy figures.
