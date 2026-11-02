<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Models

Each model is a package under
[`iron/applications/`](https://github.com/amd/IRON/tree/devel/iron/applications),
built on `iron/lm/`, the library every model shares (see
[AGENTS.md](agents.md#language-models)). Each model's README says what is
specific to it and where to get its weights. The tests find a checkpoint at
`$IRON_EXAMPLE_WEIGHTS_DIR/<checkpoint>`, default `/srv`
(`iron.lm.testing.weights_dir`).

| Model | Application | Checkpoint | NPU1 (Phoenix, Hawk Point) | NPU2 (Strix, Strix Halo, Krackan) |
|---|---|---|---|---|
| Llama 3.2 1B, 3B | [llama](https://github.com/amd/IRON/blob/devel/iron/applications/llama/README.md) | `llama3.2-1b`, `llama3.2-3b` | Yes, a dispatch per step | Yes |
| Granite 4.2 3B | [granite](https://github.com/amd/IRON/blob/devel/iron/applications/granite/README.md) | `granite-4.2-3b` | Yes, a dispatch per step | Yes |
| Granite 4.0-H 1B | [granite_hybrid](https://github.com/amd/IRON/blob/devel/iron/applications/granite_hybrid/README.md) | `granite-4.0-h-1b` | Yes, a dispatch per step | Yes |
| Gemma 4 E2B: text decoder, vision and audio towers | [gemma4](https://github.com/amd/IRON/blob/devel/iron/applications/gemma4/README.md) | `gemma-4-e2b-it` | Text decoder, a dispatch per step; towers untested | Yes |
| EmbeddingGemma 2 | [embedding_gemma2](https://github.com/amd/IRON/blob/devel/iron/applications/embedding_gemma2/README.md) | `embeddinggemma-2` | Yes, a dispatch per step; the widest images are refused | Yes |
| Whisper-small | [whisper](https://github.com/amd/IRON/blob/devel/iron/applications/whisper/README.md) | `whisper-small` | Yes, a dispatch per step | Yes |
| Gemma 4 E2B in FastFlowLM | [gemma4_engine](https://github.com/amd/IRON/tree/devel/iron/operators/flm/gemma4_engine) | `$FLM_MODEL_PATH` (the tests default to `fastflowlm`) | No | Yes |

For the `iron/lm` models (all but the FastFlowLM engine), every step of
the model's graph runs on the NPU: embeddings, layers, the LM head, and for
the text decoders the next token's draw (the `Sample` operator). Gemma 4's
image resize and patching, and its log-mel spectrogram, run on the NPU too.

The host:

- turns text into token ids and back;
- decodes an image file and packs its pixels, and pads an audio clip
  (clips past 30 s are truncated);
- draws the sampler's random numbers ahead of generation;
- writes each call's per-call values;
- on NPU1, or with `--no-full-elf`, starts each decode step and reads its
  token back, where NPU2 runs the whole loop on the device;
- prepares weights once at load (RoPE tables, layouts).

The FastFlowLM engine runs IRON's operators inside FastFlowLM's own runtime,
which keeps its tokenizer, sampling, serving, and the vision and audio
towers' own operators.

NPU1 has no full-ELF dispatch, so each step is its own xclbin dispatch and
the host starts each decode step on the token the last one drew; NPU2 runs
the decode loop on the device. Each model's README says what its NPU1 tests
cover.

## Running, testing and tuning a text decoder

What the text decoders (Llama, Granite and Gemma 4 above) share:

- **Setup**: `requirements_examples.txt`, as [installing](installation.md) says. XRT maps every device buffer locked, and a model's weights and caches are banks of at most 3.5 GiB (`iron.common.image.allocator.BANK`), so `ulimit -l` must cover one bank.
- **Run**: `python -m iron.applications.<application>.model <directory or repository id> [--prompt TEXT]`, the directory holding `config.json`, the checkpoint and the tokenizer; `-v` logs each compile; `--help` lists the options, and [Llama's README](https://github.com/amd/IRON/blob/devel/iron/applications/llama/README.md#running) explains them.
- **Test**: `pytest tests/applications/<application>/` (or `tests/applications/decoders/ -k <application>` for the decoders that share one test) loads the model once, records its time to first token and tokens per second (CI publishes them, and the nightly run fails on a regression; see [Performance Checks](performance-checks.md)), and checks accuracy against transformers' logits recorded in `golden.npz` beside the checkpoint, and determinism. `pytest <test> --record-goldens -p no:xdist` records missing logits where torch and transformers are installed; they are not IRON's requirements.
- **Tune**: `python -m iron.lm.tune <application> --checkpoint <directory>` times each operator at every setting of its tunables and rewrites the application's `profiles/<device>.json`; review it with `git diff` and commit it.
