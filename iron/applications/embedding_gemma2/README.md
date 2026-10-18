<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# EmbeddingGemma 2 on the NPU

EmbeddingGemma 2's text encoder as one IRON graph, `EmbeddingGemma`,
compiled once at `max_tokens` rows (2048 by default) with the prompt's
length bound per call, and its audio and vision towers, whose soft tokens
take their placeholders' places in the text (`Multimodal`, an
`iron.lm.Multimodal`). Text goes in
behind its task's prefix and a unit-length embedding of 768 comes out, or
its first 512, 256 or 128 renormalized. Each graph is checked against
Hugging Face's own model of the same part in float32.

The application is one package over `iron.lm`:

- `config.py`: each part's shape (`Config`, `AudioConfig`, `VisionConfig`)
  and the largest call each graph is compiled for
- `model.py`: the text encoder and `Multimodal` on the NPU, the
  `Tokenizer` (each task's prefix, the placeholders), the command line, and
  `Runner`, what `python -m iron.lm.tune embedding_gemma2` measures: every
  version of `Multimodal`, so every graph's designs, in one cost table
- `audio.py`, `vision.py`: the towers, each an `iron.lm.Tower`, a graph
  of its own that `Multimodal` calls in its body
- `blocks.py`: the layer parts its own, over `iron.lm`'s: Gemma's
  sandwich-normed layer and the audio tower's clipped projections
- `hugging_face.py`: Hugging Face's own processors, model and towers, what
  the tests' goldens are recorded from
- `profiles/`: the tunables per device, where an operator's own resolution
  falls short, and the cost tables `iron.lm.tune` writes

## Weights and tokenizer

The checkpoint directory holds `model.safetensors`, `tokenizer.json` and
`config.json` (each part's shape: `Config.from_checkpoint`,
`AudioConfig.from_checkpoint`, `VisionConfig.from_checkpoint`, checked
against it in `iron/tests/common/config.py`).
Every graph reads the weights by the checkpoint's own names
(`iron.lm.Checkpoint.tree`: `language_model`, `audio_tower`,
`vision_tower`, ...); tracing and tuning read only the header, for the
shapes.
The tests look for them at `$IRON_EXAMPLE_WEIGHTS_DIR/embeddinggemma-2/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`); on the command line they
can be anywhere.

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
designs by the table `python -m iron.lm.tune embedding_gemma2` measured.

## Testing

```bash
pytest tests/applications/embedding_gemma2/
```

The text encoder's embeddings against Hugging Face's (their cosine and
norm), the truncations, a query ranking two documents, text with a clip
and an image, each tower's soft tokens, the audio features and image
patches against Hugging Face's processors', determinism, and the latency
of each, on NPU1 and NPU2. On
NPU1 each step is its own dispatch of an xclbin; `TestEachStep` checks that
form on NPU2.

The vision tests run on four COCO val2017 photos, and the audio tests on
five LibriSpeech test-clean utterances (CC BY 4.0), each fetched from where
it is published (COCO's host, openslr's archive) by its sha256 into the
checkpoint's directory the first time.

What Hugging Face's processors and model give is recorded once in
`golden.npz` in the checkpoint's directory, where torch, torchvision and
transformers are installed (they are not IRON's requirements), and read back
from it elsewhere; a test whose golden is missing there skips.
