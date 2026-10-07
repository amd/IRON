<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Llama 3 on the NPU

Prefill and decode of Llama 3 as one IRON graph, `Llama`, a version
compiled per input shape, and the float32 numpy forward pass it is checked
against, `LlamaOracle`, its `oracle`. Both are built from the same config
and weights, Llama 3.2 1B's here; nothing here needs torch.

What is Llama's own is short, and all of it is in `iron/lm/llama3/model.py`:
its layer and head on the NPU and in numpy, its shape, where its checkpoint
keeps each weight and its tokenizer; its tunables are in
`iron/lm/llama3/profiles/`. The rest is `iron.lm`, which a new model reuses
the same way:

- `CausalLM`: the body over a prompt chunk and a decode step, the key and
  value caches,
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
python -m iron.lm.llama3.model \
    /path/to/model.safetensors /path/to/tokenizer.model \
    --prompt-len 2048 --num-tokens 40
```

- `--random-weights SEED`: in place of the two files, weights drawn at
  `SEED` and prompts of random tokens; the speed, the accuracy against the
  oracle and the determinism are those of the real checkpoint's shape, on a
  host without it
- `--prompt-len`: characters of `iron/lm/prompt.txt` to use as the prompt,
  or with `--random-weights` a third as many random tokens (default 2048)
- `--num-tokens`: tokens to generate (default 40)
- `--max-seq-len`: the rows the key and value caches hold, prompt and
  generated tokens together, a multiple of 2048 (default 32768, 1 GB of
  caches); the compile is the same at any of them. XRT locks every device
  buffer, so the locked-memory limit (`ulimit -l`) must hold the weights
  and the caches: about 3.7 GB at 32768 and 7 GB at 131072 (a
  `memlock unlimited` line in `/etc/security/limits.d/`). A prompt past
  about 48k tokens runs chunks longer than the amdxdna driver's watchdog
  allows (`tdr_timeout_ms`, 4 to 6 s a dispatch by default); with
  `options amdxdna tdr_timeout_ms=10000` in `/etc/modprobe.d/` a
  131008-token prompt runs (315 s to the first token, then 5 tokens a
  second)
- `--temperature`, `--top-k`: the sampler's (default 0.7 and 50)
- `--check-accuracy`: instead of sampling, compare each step's logits with a
  float32 numpy forward pass (`LlamaOracle`) and print the KL divergence
  and top-1 agreement
- `--check-determinism ROUNDS`: instead of sampling, run two prompts
  `ROUNDS` times each and count the runs whose logits differ bitwise
- `--device-loop`: draw every token on the device, each decode step started
  by the one before it, instead of on the host from each step's logits; the
  top-k must be at most 64
- `--compare-host`: with `--device-loop`, then generate again on the host
  from the same seed and count the tokens that differ (the text is the same,
  token for token)
- `--cost-table TABLE`: narrow the decode step's designs and pack them
  into shared device configurations by a measured cost table (below)
- `--each-step`: dispatch every step of a decode step on its own from one
  xclbin, the form NPU1 runs (below)

## NPU1, and `--each-step`

NPU1 has no full-ELF dispatch, so there both versions are xclbins whose
steps are dispatched one at a time, and the host draws each token: there is
no `--device-loop`. The versions still share one copy of the weights and the
caches, the views of one buffer object. A prompt chunk attends with MHA,
placed on NPU1's four columns as on NPU2's eight (`MHA.COLUMNS`), so a
prompt runs a chunk at a time there too. `--each-step` builds the same
form on NPU2, which is how `test_llama_3_2_1b_each_step_accuracy` checks it
there.

Decode attends with MHA of one query there too. Where MHA does not fit (an
array narrower than four columns), decode attention is `"gqa"`
(`CausalLM.decode_attention`, `iron/operators/gqa.py`): `GQAScores` against
the key cache, a `Softmax` bounded to the context, and `GQAContext` over the
value cache. Both read the caches in place, a block of positions at a time,
and only the blocks the context covers, so a step's cost follows the
context. Their cores do not depend on the cache's length, so every
`--max-seq-len` runs the same cores, and one compile serves every position
below it.

## Tuning the decode step

`--cost-table TABLE` narrows the decode step's designs (fewer columns where
a design gains little from more) and packs them into shared device
configurations, choosing by what each design costs on the device
(`iron.common.graph.narrowing`). A narrower width is only a candidate if it
was measured bit-identical to the profile's. The costs come from a table
that `tune.py` measures:

```bash
python -m iron.lm.llama3.tune /path/to/model.safetensors /path/to/tokenizer.model
python -m iron.lm.llama3.model /path/to/model.safetensors /path/to/tokenizer.model \
    --cost-table iron/lm/llama3/decode_costs_npu2.json
```

`decode_costs_npu2.json` is such a table, measured on a Strix Halo NPU (8
columns), and `decode_costs_npu1.json` one measured on a Phoenix NPU (4
columns); `tune.py` fills the current device's by default. On NPU1, where
each step is its own dispatch, nothing is packed: a narrower design is
chosen where it is cheaper to switch into. There the table narrows the
elementwise steps, moves several GEMVs between columns and lanes, puts
Sample on two cores and keeps MHA at the profile's width: with random
weights and the default caches, a token went from 362 to 338 ms (20
tokens after a 16-token prompt, medians of 8 interleaved runs). Its entries are keyed by
each design's identity -- its fields -- so a design changed since the
table was measured is not in it, and the
tuner leaves that design as the profile gives it (the `[Tuning]` report
counts it as unmeasured). Run `tune.py` again after changing a design, or
to measure for another NPU; it keeps the entries still current and measures
only the rest.

`pytest iron/applications/llama_3.2_1b/` loads the model once and runs
all of these in-process through `model.Runner`, recording the throughput and
accuracy figures.
