<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Llama 3 on the NPU

Prefill and decode of Llama 3 as one IRON graph, `Llama`, a version
compiled per input shape, built from a checkpoint's own `config.json` and
weights: Llama 3.2 1B's or 3B's here. It is judged by Hugging Face
transformers' float32 logits for the same checkpoint, recorded once to
`golden.npz` beside it (`Model.cpu_reference`), so running and testing need
no torch.

Llama's own part, Llama 3's RoPE scaling, is in
[`model.py`](model.py); its tunables are in
[`profiles/`](profiles). How to run, test and tune a model is the README's
[Models](../../../README.md#models); the shared library is
[AGENTS.md](../../../AGENTS.md#language-models).

## Weights and tokenizer

From Hugging Face (meta-llama's repository is gated: accept its license
and pass a Hugging Face token to download any of these), in one directory,
or downloaded by the repository's id, `meta-llama/Llama-3.2-1B`:

- [`model.safetensors`](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main)
- [`tokenizer.json`](https://huggingface.co/meta-llama/Llama-3.2-1B/blob/main/tokenizer.json)
- [`config.json`](https://huggingface.co/meta-llama/Llama-3.2-1B/blob/main/config.json):
  the model's shape (`LlamaConfig.from_checkpoint`), read from beside the
  checkpoint rather than hand-copied

Llama 3.2 3B is the same model at another shape: its two shards, their
`model.safetensors.index.json`, `config.json` and `tokenizer.json` from
[`meta-llama/Llama-3.2-3B`](https://huggingface.co/meta-llama/Llama-3.2-3B),
in its own directory. On NPU2 its projections take
flm.ProjectionGEMM's bf16 macs rather than bfp16's (its profile), which its accuracy
needs: about 13 times the prompt chunk's GEMM cost, a path to optimise.

## Running

From Python, see the [quick start](../../../README.md#quick-start).

From the repository root, on the command line:

```bash
python -m iron.applications.llama.model meta-llama/Llama-3.2-1B \
    --prompt "The capital of France is" --num-tokens 40
```

The positional argument is the repository's id or a directory holding
`config.json`, the checkpoint and `tokenizer.json`.

The NPU draws every token and writes the next decode step's values itself;
the host only restarts each step and reads the tokens back at the end. The
top-k must be at most 64.

- `--random-weights SEED`: in place of the checkpoint's weights and the
  tokenizer, weights drawn at `SEED` in the checkpoint's shapes (only its
  header is read) and prompts of random tokens, for the speed, accuracy
  against the graph's own host reference and determinism of the real
  checkpoint's shape
- `--prompt TEXT`: the text to continue
- `--prompt-len`, `--num-tokens`: without `--prompt`, characters of
  `iron/lm/prompt.txt` to use as the prompt (default 2048); tokens to
  generate (default 40)
- `--max-seq-len`: the longest context served, prompt and generated tokens
  together, up to the checkpoint's own `max_position_embeddings` (131072,
  4 GiB of caches, the default where it fits the host; a log line says
  what was chosen); the compile is the same at any of them. A prompt chunk
  is one command, the deepest the longest, which the driver's timeout must
  cover ([installation](../../../README.md#installation-linux))
- `--temperature`, `--top-k`: the sampler's, at `Sampler`'s defaults
- `--check-accuracy`: instead of sampling, compare each step's logits with
  the reference's and print the KL divergence and top-1 agreement
- `--check-determinism ROUNDS`: instead of sampling, run two prompts
  `ROUNDS` times each and count the runs whose logits differ bitwise
- `--compare-host`: then generate again drawing on the host from each
  step's logits, from the same seed, and count the tokens that differ (the
  text is the same, token for token)
- `--no-full-elf`: dispatch every step of each version on its own from one
  xclbin, the form NPU1 runs (below); `--full-elf` asks for one full ELF
- `-v`: log iron's INFO lines, such as each compile's

## NPU1, and `--no-full-elf`

NPU1 has no full-ELF dispatch, so there both versions are xclbins whose
steps are dispatched one at a time: there is no device loop. Each step
still draws its token on the NPU, and the host reads that token alone and
dispatches the next step on it. A prompt chunk gathers its tokens' rows of
the embedding table on the NPU too, and attends with MHA placed on NPU1's
four columns as on NPU2's eight (`MHA.PACKED_PIPELINES`), so a prompt runs a chunk
at a time there too. `--no-full-elf` builds the same form on NPU2, which is
how `test_llama_3_2_each_step_accuracy` checks it there.

## Testing

`tests/applications/llama/` runs 1B's checkpoint and then 3B's, each also
in the each-step form, over a two-chunk prompt and a chat turn.
