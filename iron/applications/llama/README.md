<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Llama 3 on the NPU

Prefill and decode of Llama 3 as one IRON graph, `Llama`, a version
compiled per input shape, and the float32 numpy forward pass it is checked
against, `LlamaOracle`. Both are built from the same config and weights,
Llama 3.2 1B's here; nothing here needs torch.

The model is a package of `iron.lm` (its shared decoder, attention and
layer, `Layer`), `iron/applications/llama/`:

- [`model.py`](model.py): its head on the NPU and in numpy, its
  shape, where its checkpoint keeps each weight, its tokenizer, and the
  command line below
- [`profiles/`](profiles): its tunables, one file per device

`python -m iron.lm.tune llama --checkpoint /path/to/model.safetensors`
measures the cost table its designs can be narrowed and packed by (below).

## Weights and tokenizer

From Hugging Face (meta-llama's repository is gated: accept its license
and pass a Hugging Face token to download any of these):

- [`model.safetensors`](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main)
- [`tokenizer.model`](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main/original)
- [`config.json`](https://huggingface.co/meta-llama/Llama-3.2-1B/blob/main/config.json):
  the model's shape (`LlamaConfig.from_checkpoint`), read from beside the
  checkpoint rather than hand-copied

The tests look for all three in `$IRON_EXAMPLE_WEIGHTS_DIR/llama3.2-1b/`
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
python -m iron.applications.llama.model \
    /path/to/model.safetensors /path/to/tokenizer.model \
    --prompt-len 2048 --num-tokens 40
```

The NPU draws every token and writes the next decode step's values itself;
the host only restarts each step and reads the tokens back at the end. The
top-k must be at most 64.

- `--random-weights SEED`: in place of the checkpoint's weights and the
  tokenizer, weights drawn at `SEED` in the checkpoint's shapes (only its
  header is read) and prompts of random tokens, for the speed, accuracy
  against the oracle and determinism of the real checkpoint's shape
- `--prompt-len`, `--num-tokens`: characters of `iron/lm/prompt.txt` to use
  as the prompt (default 2048) and tokens to generate (default 40)
- `--max-seq-len`: the longest context served, prompt and generated tokens
  together, up to the checkpoint's own `max_position_embeddings` (131072,
  4 GiB of caches, the default where it fits the host; a log line says
  what was chosen); the compile is the same at any of them.
  XRT maps every device buffer locked, and the weights and the caches are
  banks of at most 3.76 GB (`iron.common.image.allocator.BANK`), so `ulimit
  -l` must cover one bank. A prompt past about
  48k tokens runs chunks longer than the amdxdna driver's watchdog allows
  (`tdr_timeout_ms`, 4 to 6 s a dispatch by default); with `options amdxdna
  tdr_timeout_ms=10000` in `/etc/modprobe.d/` a 131008-token prompt runs
  (315 s to the first token, then 5 tokens a second)
- `--temperature`, `--top-k`: the sampler's (default 0.7 and 50)
- `--check-accuracy`: instead of sampling, compare each step's logits with
  `LlamaOracle` and print the KL divergence and top-1 agreement
- `--check-determinism ROUNDS`: instead of sampling, run two prompts
  `ROUNDS` times each and count the runs whose logits differ bitwise
- `--compare-host`: then generate again drawing on the host from each
  step's logits, from the same seed, and count the tokens that differ (the
  text is the same, token for token)
- `--cost-table TABLE`: narrow and pack the decode step's and prompt
  chunk's designs by a measured cost table (below)
- `--no-full-elf`: dispatch every step of each version on its own from one
  xclbin, the form NPU1 runs (below); `--full-elf` asks for one full ELF

## NPU1, and `--no-full-elf`

NPU1 has no full-ELF dispatch, so there both versions are xclbins whose
steps are dispatched one at a time: there is no device loop. Each step
still draws its token on the NPU, and the host reads that token alone and
dispatches the next step on it. A prompt chunk gathers its tokens' rows of
the embedding table on the NPU too, and attends with MHA placed on NPU1's
four columns as on NPU2's eight (`MHA.COLUMNS`), so a prompt runs a chunk
at a time there too. `--no-full-elf` builds the same form on NPU2, which is
how `test_llama_3_2_1b_each_step_accuracy` checks it there.

## Tuning

`--cost-table TABLE` folds steps into the step producing their input (the
gate projection's SiLU into its GEMV), narrows the designs of the decode
step and the prompt chunk and packs them into shared device configurations,
by what each design costs on the device
(`iron.tune.narrowing`). No table is checked in: one is measured on
the NPU it is used on.

```bash
python -m iron.lm.tune llama --checkpoint /path/to/model.safetensors
python -m iron.applications.llama.model /path/to/model.safetensors /path/to/tokenizer.model \
    --cost-table iron/applications/llama/costs_npu2.json
```

On NPU1, where each step is its own dispatch, nothing is packed: a
narrower design is chosen where it is cheaper to switch into. There a
table measured on a Phoenix NPU (4 columns) narrowed the elementwise
steps, moved several GEMVs between columns and lanes, put Sample on two
cores and kept MHA at the profile's width: with random weights and the
default caches, a token went from 362 to 338 ms (20 tokens after a
16-token prompt, medians of 8 interleaved runs).

## Testing

```bash
pytest tests/applications/llama/
```

Loads the model once and runs the accuracy, determinism and throughput
checks above in-process through `model.Runner`.
