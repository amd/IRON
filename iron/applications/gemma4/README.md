<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Gemma 4 E2B on the NPU

Gemma 4 E2B whole: its text decoder (`Gemma4`, an `iron.lm.CausalLM`) and
its vision and audio towers (`vision.py`, `audio.py`, each an
`iron.lm.Tower`), as one `iron.lm.Multimodal`, `Gemma4Multimodal`, whose
image and audio placeholders take the towers' soft tokens as transformers'
`masked_scatter` places them. One compile serves every prompt length,
image size and clip length. The shared library is
[AGENTS.md](../../../AGENTS.md#language-models).

- `model.py`: the text decoder, `Gemma4Multimodal`, its config (the towers'
  shapes and the markers around a run of placeholders) and
  `Gemma4MultimodalConfig.expand`, which lays a prompt's image and clip out
  as `Gemma4Processor` does.
- `vision.py`, `audio.py`: the towers, shared with EmbeddingGemma 2. E2B's
  vision projections are clipped (`use_clipped_linears`), EmbeddingGemma
  2's are not.
- `hugging_face.py`: transformers' model and processors, what the goldens
  are recorded from.

As transformers' `Gemma4Model` does, the per-layer inputs read a
placeholder as the padding token: its per-layer table holds the padding
token's row at the image, audio and video placeholders.

## Images and clips

An image is decoded `(height, width, 3)` uint8 of up to 12.6 MP either way
up, resized, cut into patches and embedded on the NPU at the processor's
280 soft tokens; a clip is 16 kHz mono of up to 30 s, its log-mel
features computed on the NPU. `Gemma4Multimodal.logits(tokens, raw)` and
`generate(tokens, n, raw=raw)` take them by placeholder, `raw =
{image_token_id: (image, 280), audio_token_id: (waveform,)}`, the tokens
laid out by `expand`.

## Precision

The towers' projections run at `Precision.HIGHEST` (their configs'): float32
partial sums, rounded once. The text decoder's are its config's. Measured on
npu2 over the tests' cases, KL(float32 transformers || device) is 0.00005
to 0.0053 on average over a case's eight steps, 0.042 at the worst step.
Cheaper tower precisions were not measured.

## Weights and tokenizer

From Hugging Face
([`google/gemma-4-E2B-it`](https://huggingface.co/google/gemma-4-E2B-it)):
`model.safetensors`, `tokenizer.json`, `config.json` and
`chat_template.jinja`.

## Testing

```bash
pytest tests/applications/gemma4/
```

On the NPU, one compile serves chat turns over COCO val2017 photos of two
sizes, LibriSpeech test-clean clips of two lengths and one with both: the
next-token distribution after the prompt and after seven decode steps,
teacher-forced, against transformers' float32 model over its own
processors' inputs. The photos and clips are fetched from their
maintainers' hosts by URL and sha256 into IRON's cache. Hugging Face's
logits are recorded once in `golden.npz` beside the checkpoint, device-free;
the recorder keeps the per-layer token table bfloat16 (its lookup widens
exactly and its scale, 16, is a power of two, so the per-layer inputs are
float32's), which saves 11 GB. `reference/` checks the text decoder
device-free at a toy shape over random weights.
