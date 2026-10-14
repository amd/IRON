<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# EmbeddingGemma 2 on the NPU

EmbeddingGemma 2's text encoder as one IRON graph, `EmbeddingGemma`,
compiled once at `max_tokens` rows (2048 by default) with the prompt's
length bound per call, and its audio and vision towers, whose soft tokens
take their placeholders' places in the text (`Multimodal`). Text goes in
behind its task's prefix and a unit-length embedding of 768 comes out, or
its first 512, 256 or 128 renormalized. Each graph is checked against a
float32 numpy oracle of the same part.

The application is one package over `iron.lm`:

- `config.py`: each part's shape (`Config`, `AudioConfig`, `VisionConfig`)
  and the largest call each graph is compiled for
- `weights.py`: where the checkpoint keeps each weight, a layout per part,
  and `Weights`, the trees of a checkpoint directory
- `model.py`: the text encoder and `Multimodal` on the NPU, the
  `Tokenizer` (each task's prefix, the placeholders), and the command line
- `audio.py`, `vision.py`: the towers, each a graph of its own that
  `Multimodal` calls in its body
- `oracle.py`: the float32 oracles, with the host feature extractor and
  image processor
- `tune.py`: measures the cost table every graph's designs can be narrowed
  and packed by
- `profiles/`: the tunables per device, where an operator's own resolution
  falls short, and the cost tables `tune.py` writes

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
python -m iron.applications.embedding_gemma2.model /path/to/embeddinggemma-2 \
    --query "What causes the northern lights?" \
    --document "Charged particles from the sun." "Photosynthesis in plants."
```

`--dims` truncates the embeddings, and `--costs` narrows and packs the
designs by the table `python -m iron.applications.embedding_gemma2.tune`
measured.

## Testing

```bash
pytest iron/applications/embedding_gemma2/
```

The text encoder's embeddings against the oracle's (their cosine and
norm), the truncations, a query ranking two documents, text with a clip
and an image, each tower's soft tokens, the audio features and image
patches against the host's, and the latency of each, on NPU1 and NPU2. On
NPU1 each step is its own dispatch of an xclbin; `TestEachStep` checks that
form on NPU2.

The vision tests run on four COCO val2017 photos, fetched from COCO's own
host by their sha256 into the checkpoint's directory the first time.

The float32 oracles are checked against Hugging Face's own processors and
model (`hugging_face.py`), computed as the tests run. They need torch,
torchvision and transformers, which are not IRON's requirements; without
them those tests skip.
