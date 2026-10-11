<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# SmolLM2 1.7B Instruct on the NPU

Prefill and decode of SmolLM2 1.7B Instruct as one IRON graph, a version
compiled per input shape, and the float32 numpy forward pass it is checked
against. Both are Llama's (`iron/applications/llama/model.py`), built from
SmolLM2's config and weights; nothing here needs torch.

SmolLM2 is the plain Llama architecture (`"model_type": "llama"` in its
checkpoint's `config.json`): RMSNorm, RoPE with no frequency scaling, SwiGLU,
no projection bias and a tied output head, the same as Llama 3's. It
differs only in shape -- full MHA (`num_key_value_heads == num_attention_heads`,
a KV group of one, not Llama 3's grouped-query eight), its RoPE base
(130000) and its tokenizer -- so it is a `Config` of the Llama application,
`SMOLLM2_1_7B`, run by Llama's layer and head (`iron.lm.Block`).

What is SmolLM2's own is short: in `iron/applications/llama/model.py`, its
shape, `SmolLM2` (Llama with its own profiles, `profiles/smollm2/`, since
its operator shapes overlap 1B's at other tunables) and `SmolLM2Runner`
(its `tokenizer.json` and BOS); and here, its test, this README and
`tune.py`. The rest is `iron.lm`, which every model reuses the same way
(see `iron/applications/llama/README.md` for the full description).

## Weights and tokenizer

From Hugging Face:

- [`model.safetensors`](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct/tree/main)
- [`tokenizer.json`](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct/tree/main)

The tests look for them in `$IRON_EXAMPLE_WEIGHTS_DIR/smollm2-1.7b-instruct/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`); on the command line they can
be anywhere.

## Setup

Set up IRON as the repository root describes, then:

```bash
python3 -m pip install -r requirements_examples.txt
```

## Running

From the repository root:

```bash
python -m iron.applications.llama.smollm2 \
    /path/to/model.safetensors /path/to/tokenizer.json \
    --prompt-len 2048 --num-tokens 40
```

The NPU draws every token and writes the next decode step's values itself;
the host only restarts each step and reads the tokens back at the end. On
NPU1 and with `--each-step` the NPU draws each token too, and the host reads
that token alone and starts the next step on it. The top-k must be at most
64.

- `--random-weights SEED`: in place of the two files, weights drawn at
  `SEED` and prompts of random tokens; the speed, the accuracy against the
  oracle and the determinism are those of the real checkpoint's shape, on a
  host without it
- `--prompt-len`: characters of `iron/lm/prompt.txt` to use as the prompt,
  or with `--random-weights` a third as many random tokens (default 2048)
- `--num-tokens`: tokens to generate (default 40)
- `--max-seq-len`: the rows the key and value caches hold, prompt and
  generated tokens together, a multiple of 2048 (default 8192); the compile
  is the same at any of them
- `--temperature`, `--top-k`: the sampler's (default 0.7 and 50)
- `--check-accuracy`: instead of sampling, compare each step's logits with a
  float32 numpy forward pass (`SmolLM2Oracle`) and print the KL divergence
  and top-1 agreement
- `--check-determinism ROUNDS`: instead of sampling, run two prompts
  `ROUNDS` times each and count the runs whose logits differ bitwise
- `--compare-host`: then generate again drawing on the host from each
  step's logits, from the same seed, and count the tokens that differ (the
  text is the same, token for token)
- `--cost-table TABLE`: fold the steps of the decode step and the prompt
  chunk, narrow their designs and pack them into shared device
  configurations by a measured cost table (below)
- `--each-step`: dispatch every step of a decode step on its own from one
  xclbin, the form NPU1 runs

## Full MHA, and the prompt chunk's watchdog cost

SmolLM2's `num_key_value_heads` equals its `num_attention_heads` (32, a KV
group of one): every query head attends its own K and V, with none of
Llama 3's eightfold grouped-query sharing. A prompt chunk's attention
therefore streams about four times the K and V blocks a same-context
grouped-query model's does, and at `max_seq_len` (8192) that dispatch can
run past the amdxdna watchdog's default timeout
(`ert_cmd_state.ERT_CMD_STATE_TIMEOUT`); see AGENTS.md's "Not built, or
limited" for the watchdog's own figures and how to raise it
(`tdr_timeout_ms` or `timeout_in_sec`, depending on the `amdxdna` version).
A shorter `--max-seq-len` keeps a prompt chunk's deepest dispatch under the
default.

## Tuning

`--cost-table TABLE` folds steps into the step producing their input,
narrows the designs of the decode step and the prompt chunk and packs them
into shared device configurations, choosing by what each design costs on
the device. The costs come from a table that `tune.py` measures:

```bash
python -m iron.applications.llama.smollm2.tune
python -m iron.applications.llama.smollm2 /path/to/model.safetensors /path/to/tokenizer.json \
    --cost-table iron/applications/llama/smollm2/costs_npu2.json
```

No table is checked in at present: one is measured on the NPU it is used
on. See `iron/applications/llama/README.md`'s "Tuning" section for
the full description of how a table folds and narrows designs.

`pytest iron/applications/llama/smollm2/` loads the model once and
runs all of these in-process through `SmolLM2Runner`, recording the
throughput and accuracy figures.
