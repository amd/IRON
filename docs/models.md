<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Models

Each model is a package under
[`iron/applications/`](https://github.com/amd/IRON/tree/devel/iron/applications),
built over `iron/lm/`, the library every model shares (see
[AGENTS.md](agents.md#language-models)). Each model's README says which code
is specific to it and where its files come from.

| Model | Application | Checkpoint |
|---|---|---|
| Llama 3.2 1B, 3B | [llama](https://github.com/amd/IRON/blob/devel/iron/applications/llama/README.md) | `llama3.2-1b`, `llama3.2-3b` |
| Gemma 4 E2B text decoder | [gemma4](https://github.com/amd/IRON/blob/devel/iron/applications/gemma4/README.md) | `gemma-4-e2b-it` |
| EmbeddingGemma 2 | [embedding_gemma2](https://github.com/amd/IRON/blob/devel/iron/applications/embedding_gemma2/README.md) | `embeddinggemma-2` |
| Gemma 4 E2B in FastFlowLM | [gemma4_engine](https://github.com/amd/IRON/tree/devel/iron/operators/flm/gemma4_engine) | `$FLM_MODEL_PATH` (the tests default to `fastflowlm`) |

What the text decoders (Llama and Gemma 4 above) share, and how to run, test
and tune any of them, is in the [Models section](installation.md#models) of
the installation guide.
