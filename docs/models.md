<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Models

Each model is a package under
[`iron/applications/`](https://github.com/amd/IRON/tree/devel/iron/applications),
built on `iron/lm/`, the library every model shares (see
[AGENTS.md](agents.md#language-models)). Each model's README says what is
specific to it and where to get its weights.

This table is also [README.md](installation.md#models)'s, with relative links
in place of these GitHub-absolute ones; a new row goes in both.

| Model | Application | Checkpoint | NPU1 (Phoenix, Hawk Point) | NPU2 (Strix, Strix Halo, Krackan) |
|---|---|---|---|---|
| Llama 3.2 1B, 3B | [llama](https://github.com/amd/IRON/blob/devel/iron/applications/llama/README.md) | `llama3.2-1b`, `llama3.2-3b` | Yes, a dispatch per step | Yes |
| Granite 4.2 3B | [granite](https://github.com/amd/IRON/blob/devel/iron/applications/granite/README.md) | `granite-4.2-3b` | Yes, a dispatch per step | Yes |
| Granite 4.0-H 1B | [granite_hybrid](https://github.com/amd/IRON/blob/devel/iron/applications/granite_hybrid/README.md) | `granite-4.0-h-1b` | Not yet run; its tests are enabled | Yes |
| Gemma 4 E2B: text decoder, vision and audio towers | [gemma4](https://github.com/amd/IRON/blob/devel/iron/applications/gemma4/README.md) | `gemma-4-e2b-it` | Text decoder, a dispatch per step; towers untested | Yes |
| EmbeddingGemma 2 | [embedding_gemma2](https://github.com/amd/IRON/blob/devel/iron/applications/embedding_gemma2/README.md) | `embeddinggemma-2` | Yes, a dispatch per step; the widest images are refused | Yes |
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

What the text decoders (Llama, Granite and Gemma 4 above) share, and how to run,
test and tune any of them, is in the [Models section](installation.md#models)
of the installation guide. Their performance is measured by CI; see
[Benchmarks](benchmarks.md).
