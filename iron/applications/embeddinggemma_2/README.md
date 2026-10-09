<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# EmbeddingGemma 2 on the NPU

EmbeddingGemma 2's text encoder as one IRON graph, `EmbeddingGemma`,
compiled once at `max_tokens` rows (2048 by default) with the prompt's
length bound per call, and the float32
numpy encoder it is checked against, `EmbeddingGemmaOracle`. Text goes in
behind its task's prompt and a unit-length embedding of 768 comes out, or
its first 512, 256 or 128 renormalized.

The model is a package of `iron.lm`, `iron/lm/embeddinggemma2/`:

- `model.py`: its shape (`Config`), where its checkpoint keeps each weight
  (`layout`) and the graph
- `oracle.py`: the float32 encoder on the host, and the tokenizer
- `encoder.py`: `Encoder`, the tokenizer, the weights and the graph of a
  checkpoint directory, and the command line below
- `tune.py`: measures the cost table its designs can be narrowed and packed
  by

## Weights and tokenizer

The checkpoint directory holds `model.safetensors` and `tokenizer.json`.
The tests look for it at `$IRON_EXAMPLE_WEIGHTS_DIR/embeddinggemma-2/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`); on the command line it can
be anywhere.

## Setup

Set up IRON as the repository root describes, then:

```bash
python3 -m pip install -r requirements_examples.txt
```

## Running

From the repository root, a query ranked against documents:

```bash
python -m iron.lm.embeddinggemma2.encoder /path/to/embeddinggemma-2 \
    --query "What causes the northern lights?" \
    --document "Charged particles from the sun." "Photosynthesis in plants."
```

`--dims` truncates the embeddings, and `--costs` narrows and packs the
designs by the tables `python -m iron.lm.embeddinggemma2.tune` (the text)
and `python -m iron.lm.embeddinggemma2.vision.tune` (the vision tower)
measured, merged.

## Testing

```bash
pytest iron/applications/embeddinggemma_2/
```

Each embedding against the oracle's (its cosine and its norm), the
truncations, a query ranking two documents, and the latency of a query,
a long document and one past the sliding window. NPU2 only.
