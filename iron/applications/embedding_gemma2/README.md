<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# EmbeddingGemma 2 on the NPU

EmbeddingGemma 2's text encoder, `EmbeddingGemma`, an `iron.lm.Encoder`
compiled once at `max_tokens` rows with the prompt's length bound per call,
and its audio and vision towers, whose soft tokens take their placeholders'
places in the text (`Multimodal`). Text goes in behind its task's prefix
and a unit-length embedding of 768 comes out, or its first 512, 256 or 128
renormalized. Each graph is checked against Hugging Face's own model of the
same part in float32. The shared library is [AGENTS.md](../../../AGENTS.md#language-models).

- `model.py`: the text encoder's shape, the largest call each graph is
  compiled for, the encoder (which `python -m iron.lm.tune
  embedding_gemma2` times), `Multimodal`, the tokenizer and the command line
- `hugging_face.py`: Hugging Face's processors and model, what the goldens
  are recorded from

Its audio and vision towers are Gemma 4's, in
[`gemma4/audio.py` and `gemma4/vision.py`](../gemma4/), each an
`iron.lm.Tower` tuned by this application's profiles.

## Weights and tokenizer

The checkpoint directory holds `model.safetensors`, `tokenizer.json` and
`config.json`. Install `requirements_examples.txt` as the README's
[Models](../../../README.md#models) says.

## Running

```bash
python -m iron.applications.embedding_gemma2.model /path/to/embeddinggemma-2 \
    --query "What causes the northern lights?" \
    --document "Charged particles from the sun." "Photosynthesis in plants."
```

`--dims` truncates the embeddings.

## Testing

```bash
pytest tests/applications/embedding_gemma2/
```

The text encoder's embeddings against Hugging Face's, the truncations, a
query ranking two documents, text with a clip and an image, each tower's
soft tokens, the audio features and image patches against Hugging Face's
processors', determinism and latency, on NPU1 and NPU2; `TestEachStep`
checks NPU1's form, an xclbin per step, on NPU2. The vision tests fetch
four COCO val2017 photos and the audio tests five LibriSpeech test-clean
utterances (CC BY 4.0) into IRON's cache, each pinned by its sha256.
Hugging Face's outputs are recorded once in `golden.npz` beside the
checkpoint by `pytest <test> --record-goldens -p no:xdist`; a test whose golden is missing
fails.

On NPU1 an image wider than Resample's per-core budget is refused
(`test_image_processor_refuses_on_npu1`), and
`TestAudio::test_audio_accuracy[passage]` is known to land just under
`AUDIO_MIN_COSINE`, a bound set from NPU2. The tower tracks its operators'
references through its first 11 layers; the last layer is ill-conditioned
at a few of passage's tokens (`AUDIO_MIN_COSINE`'s comment), which NPU1's
rounding tips under the bound.
