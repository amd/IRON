<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# IRON models in FastFlowLM

On an NPU2 machine, install [IRON](../../../README.md#installation-linux) and
[the build dependencies](../../../ci/docker-based/Dockerfile)
(the IRON CI container includes them). `make flm` builds FastFlowLM and this
plugin against its installed extension SDK. Run from this directory:

```bash
source /opt/xilinx/xrt/setup.sh
source /path/to/ironenv/bin/activate
make flm
model_path=${FLM_MODEL_PATH:-$HOME/.cache/fastflowlm}
source build/install/flm_env.sh
export FLM_MODEL_PATH="$model_path"

read -rsp 'Hugging Face token: ' HF_TOKEN; echo
export HF_TOKEN
flm serve llama3.2-iron:1b --ctx-len 2048 --model-extension "$PWD/build/plugin/extension.json"
```

For Llama, first accept the [model license](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
and create a **Read** token in [Hugging Face settings](https://huggingface.co/settings/tokens).
`flm serve` downloads missing weights automatically. IRON reuses compiled
artifacts in `$NPU_CACHE_HOME` (default `~/.npu/cache`).

Replace `llama3.2-iron:1b` with `embeddinggemma-2:740m` to serve embeddings,
or use `flm run` for interactive chat. Models must be registered in both
[IRON](../__init__.py) and the
[plugin catalog](model-list.json).
The plugin reuses FLM's Llama frontend and exchanges tokens/logits or
text/embeddings with the IRON server. Its C++ sources and catalog live here;
FastFlowLM needs only the generic plugin interfaces.

To add a model, register it in [model_extension.cpp](model_extension.cpp) and
add its pinned weight records to the catalog; `iron_model` selects the IRON
registry entry. The bundle is `extension.json`, `model-list.json`, and the shared
library in `build/plugin/`. `make flm` also runs its C++ contract/pipe tests.

The [integration test](../../../tests/applications/fastflowlm_iron/test.py) checks
Llama chat and EmbeddingGemma-2 through the HTTP API on NPU2. CI needs
`config.json`, `model.safetensors`, `tokenizer.json` and `tokenizer_config.json`
in each of `/srv/fastflowlm/models/llama3.2-1b-instruct/` and
`/srv/embeddinggemma-2/` (shared with the standalone IRON tests). The test
also accepts checkpoints under `$FLM_MODEL_PATH/models/`. Set `FLM_MODEL_PATH` to another directory
containing `models/` to reuse local weights. No token is needed when weights
are already present.

## Embedding requests

`embeddinggemma-2:740m` accepts a string `input` (or a batch of strings), an
optional `task`, document `title`, and `dimensions` (768, 512, 256, or 128;
default 768). Each output is normalized. Options stay in the request JSON;
IRON formats and tokenizes the text, and reports processed tokens including
prefixes and special tokens. Unknown options or unsupported values return 400.
A title is accepted only for document tasks and defaults to `none`.

Task names are case-sensitive and specific to this model:

| Names | Prompt |
|---|---|
| Omitted, empty, `query`, `SearchQuery`, `Retrieval-query`, `Retrieval`, `BitextMining`, `Reranking` | `task: search result \| query: ` |
| `document`, `Document`, `Retrieval-document` | `title: <title> \| text: ` |
| `Classification`, `MultilabelClassification` | `task: classification \| query: ` |
| `Clustering` | `task: clustering \| query: ` |
| `CodeRetrieval`, `InstructionRetrieval` | `task: code retrieval \| query: ` |
| `FactChecking` | `task: fact checking \| query: ` |
| `QuestionAnswering` | `task: question answering \| query: ` |
| `SentenceSimilarity`, `STS`, `PairClassification`, `Summarization` | `task: sentence similarity \| query: ` |

These aliases select prompts, not downstream scoring or classification operations.
For example, `Reranking` uses the query prompt; embed candidate documents with
`document`. Other models can define different tasks and options.

```json
{"model":"embeddinggemma-2:740m","input":"Paris is in France.","task":"document","title":"France","dimensions":128}
```

To keep chat and embedding engines loaded in the same server:

```bash
flm serve llama3.2-iron:1b -e embeddinggemma-2:740m --ctx-len 2048 --model-extension "$PWD/build/plugin/extension.json"
```

Chat and embedding requests use their respective engines; the client connects
them into a retrieval workflow. The integration test embeds documents between
two chat turns, checking that chat state survives. The plugin requires the IRON
server's JSON embedding request capability; rebuild/update both together.
