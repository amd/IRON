<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Qwen3 1.7B on the NPU

Prefill and decode of Qwen3 1.7B as one IRON graph, `Qwen3`, a version
compiled per input shape, and the float32 numpy forward pass it is checked
against, `Qwen3Oracle`, its `oracle`. Both are built from the same config
and weights; nothing here needs torch.

What is Qwen3's own is short, and all of it is in `iron/applications/qwen3/model.py`:
its layer and head on the NPU and in numpy, its shape, where its checkpoint
keeps each weight and its tokenizer; its tunables are in
`iron/applications/qwen3/profiles/`. The rest is `iron.lm`, shared with Llama 3:

- `CausalLM`: the body over a prompt chunk and a decode step, the key and
  value caches, attention over them (`attend`) and `logits(tokens)`; a model
  subclasses it with `layer(step, i, weights, x)` and `head(x)`
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

## Qwen3 vs. Llama 3

Two differences from Llama's own layer and head (`iron.lm.Block`, `iron/applications/llama/model.py`):

- **Per-head RMSNorm on Q and K, before RoPE** (`q_norm`/`k_norm`, one
  weight row of `head_dim`, shared by every head and every position): a
  composition of the existing weighted `RMSNorm` operator at a new shape,
  not a new operator.
- **`rms_norm_eps` of 1e-6**, not Llama's 1e-5, passed explicitly to every
  `RMSNorm` call (`epsilon=`), since it is a `param`, not an `auto()`
  tunable a profile can fill.

Its output head is the input embedding, tied (`tie_word_embeddings: true`
in its `config.json`); its checkpoint also ships `lm_head.weight`,
confirmed byte-identical to `model.embed_tokens.weight` by sha256, which
the layout maps (so `load_weights`'s strict check accepts it) but `head()`
never reads.

Its checkpoint is sharded (two `.safetensors` files and a
`model.safetensors.index.json`); `iron.lm.Checkpoint` reads the index
directly (passed as `weights_path`, in place of a single `.safetensors`
file), mapping every shard the index names.

## Weights and tokenizer

From Hugging Face ([`Qwen/Qwen3-1.7B`](https://huggingface.co/Qwen/Qwen3-1.7B), Apache-2.0):

- `model-00001-of-00002.safetensors`, `model-00002-of-00002.safetensors`,
  `model.safetensors.index.json`
- `tokenizer.json`

The tests look for them in `$IRON_EXAMPLE_WEIGHTS_DIR/qwen3-1.7b/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`); on the command line they
can be anywhere. The tokenizer loads through the `tokenizers` package
(already a dependency of `requirements_examples.txt`), not `transformers`:
nothing here needs torch.

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

The NPU draws every token and writes the next decode step's values itself;
the host only restarts each step and reads the tokens back at the end. On
NPU1 and with `--each-step` the NPU draws each token too, and the host
reads that token alone and starts the next step on it (below). The top-k
must be at most 64.

- `--random-weights SEED`: in place of the two files, weights drawn at
  `SEED` and prompts of random tokens; the speed, the accuracy against the
  oracle and the determinism are those of the real checkpoint's shape, on a
  host without it
- `--prompt-len`: characters of `iron/lm/prompt.txt` to use as the prompt,
  or with `--random-weights` a third as many random tokens (default 2048)
- `--num-tokens`: tokens to generate (default 40)
- `--max-seq-len`: the rows the key and value caches hold, prompt and
  generated tokens together, a multiple of 2048 (default 32768, matching
  Qwen3-1.7B's trained `max_position_embeddings`); the compile is the same
  at any of them
- `--temperature`, `--top-k`: the sampler's (default 0.7 and 50)
- `--check-accuracy`: instead of sampling, compare each step's logits with a
  float32 numpy forward pass (`Qwen3Oracle`) and print the KL divergence
  and top-1 agreement
- `--check-determinism ROUNDS`: instead of sampling, run two prompts
  `ROUNDS` times each and count the runs whose logits differ bitwise
- `--compare-host`: then generate again drawing on the host from each
  step's logits, from the same seed, and count the tokens that differ (the
  text is the same, token for token)
- `--cost-table TABLE`: fold the steps of the decode step and the prompt
  chunk, narrow their designs and pack them into shared device
  configurations by a measured cost table (`iron.applications.qwen3.tune`)
- `--each-step`: dispatch every step of a decode step on its own from one
  xclbin, the form NPU1 runs (below)

## NPU1, and `--each-step`

NPU1 has no full-ELF dispatch, so there both versions are xclbins whose
steps are dispatched one at a time: there is no device loop. Each step
still draws its token on the NPU, and the host reads that token alone, not
the logits, and dispatches the next step on it. `--each-step` builds the same form on NPU2, which is how
`test_qwen3_1_7b_each_step_accuracy` checks it there. See
`iron/applications/llama/README.md` for the fuller account (shared,
since nothing about this is Qwen3-specific): the versions share one copy of
the weights and the caches, a prompt chunk attends with MHA placed on
NPU1's four columns, and decode attends with MHA of one query, reading the
caches in place.

Qwen3's `d` (`head_dim`) is 128, twice Llama 3.2 1B's 64: MHA's block-size
search (the largest block whose cores fit L1 at this head size) picks a
smaller block there, which at the default `num_pipelines=1` pushes a
prompt chunk's K/V fill past the DMA descriptor's 64-iteration cap.
`profiles/npu1.json` pins `num_pipelines=4` for the prompt-chunk shape
(the same value Llama's own NPU1 profile uses), which keeps the block
count the fill repeats under the cap.

## Tuning

See `iron/applications/llama/README.md`'s "Tuning" section; the
mechanism (`iron.lm.tune`, `iron.applications.qwen3.tune`) is shared. No table is
checked in at present: one is measured on the NPU it is used on.

```bash
python -m iron.applications.qwen3.tune
python -m iron.applications.qwen3.model /path/to/model.safetensors.index.json /path/to/tokenizer.json \
    --cost-table iron/applications/qwen3/costs_npu2.json
```

`pytest iron/applications/qwen3/` loads the model once and runs all of
these in-process through `model.Runner`, recording the throughput and
accuracy figures.
