<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Whisper on the NPU

OpenAI Whisper (`openai/whisper-small`) speech-to-text on `iron.lm`,
compiled as one `Whisper` graph with three versions sharing a single device
arena:

- `encode`: the 2-layer Conv1d frontend (`conv1`, `GELU`, `conv2`, `GELU`
  and learned `embed_positions`), 12 bidirectional `EncoderLayer` blocks,
  the final `LayerNorm`, and every decoder layer's cross-attention `K` and
  `V` projections written directly into shared `iron.state` buffers;
- `prompt_chunk`: a 64-row decoder prefill chunk over `KVCache`
  self-attention, cross-attention `MHA` over the encoder's `K` and `V`
  states, `MLP`, final `LayerNorm`, `lm_head` and `Sample`;
- `decode_step`: a single-token decoder step with `GEMV` projections,
  packed self-attention and cross-attention `MHA`, `GELU`, `lm_head` (padded
  to 51,968 rows across 8 lanes) and `Sample`.

The shared `iron.lm.blocks.LogMel` runs the windowed DFT, power spectrum,
Slaney Mel projection, and fused log10/clamp/affine normalization on the NPU.
The fused kernel reduces Mel energies in float32 and rounds the normalized
features once to `bfloat16`. Only sample padding/reflection and WAV decoding
stay on the host. Long-form normalization uses the complete recording plus
30 seconds of silence, before slicing its decoder windows.

The extensive long-form test records Hugging Face's own whole-clip
timestamped generation, keyed by the fixed audio clip rather than the NPU's
window seeks. It allows at most one substituted word (WER also capped at
2%) and 0.5 s of word-aligned timing drift. These bounds cover the observed
Strix timestamp near-tie (one word, up to 0.4 s) while requiring equal word
counts and rejecting missing or duplicated speech, reversed timestamps and
missing interior segment endpoints. An unclosed final segment is bounded by
the clip duration, and a final HF timestamp past the clip edge is clamped to
that edge because the last window includes padding.

Token selection also runs on the NPU. The host writes one small Sample
draw row per step: history-dependent suppression ranges and the
timestamp/text split. Static scattered suppression tokens are a resident
negative-infinity bias. Sample applies the forced-timestamp probability
rule and returns the selected token; transcription does not read back the
vocabulary-sized logits. `Whisper.logits` retains full readback for
teacher-forced accuracy checks. The pinned Sample kernel accepts per-draw
ranges, not token-history state, so timestamp-rule history is still prepared
on the host. The static suppression bias also remains separate from
`lm_head`: the same decoder versions return unmodified logits for diagnostics
and feed the sampler, so folding the bias into the head would change those
logits. Fusing it without that behavior change requires a sampling-specific
head path or a Sample-kernel extension.

Audio up to 30 s is transcribed in one window without timestamps. Audio
longer than 30 s (or with `--long-form`) runs OpenAI Whisper's sequential
long-form algorithm with `ApplyTimestampRules`: each 30 s window is decoded
with paired non-decreasing timestamps, advancing the next window to the last
complete timestamp pair. When it rewinds, unfinished trailing text is discarded
so the next window does not duplicate it.

- `model.py`: `WhisperConfig`, `WhisperEncoder`, `WhisperDecoder`,
  `Whisper`, `TokenPolicy` and the CLI
- `audio.py`: 16 kHz mono WAV loading
- `hugging_face.py`: Hugging Face's `WhisperForConditionalGeneration` in
  float32 and `WhisperFeatureExtractor`, used only when recording goldens or
  running `--check-reference`
- `profiles/`: per-device operator tunables (`npu1.json`, `npu2.json`)

## Weights and tokenizer

The checkpoint directory holds `model.safetensors`, `config.json`,
`tokenizer.json` and `preprocessor_config.json`. Install
`requirements_examples.txt` as
[Models](../../../docs/models.md#running-testing-and-tuning-a-text-decoder)
describes.

## Running

```bash
python -m iron.applications.whisper.model /path/to/whisper-small --wav clip.wav
```

Pass `--long-form` to force timestamped decoding on clips under 30 s,
`--reference-text transcript.txt` to report word error rate (WER), and
`--check-reference` to compare the encoder output and decoded tokens against
Hugging Face's float32 model.

## Validation on Phoenix (NPU1)

With `mlir-aie` `1.4.5.dev119`, `GELU(approximate="none")` (`gelu_erf`) is
exact (0 of 48,853 normal-output finite `bfloat16` inputs misrounded on
`npu1`). `Softmax(input_dtype=np.float32)` measured a `0.00159` maximum
absolute error and `0.00208` NRMSE against its NumPy reference. `LayerNorm`
(`layer_norm_eps`) keeps its statistics in 3-limb `float32` (within 1
`bfloat16` ULP on `npu1`). All projections and attention matmuls run at
`Precision.HIGHEST`.

The following Phoenix measurements were collected before the fused
`log10_clamp_f32` frontend change and are historical only; they are not
validation evidence for the current frontend. Current-branch measurements
against `WhisperFeatureExtractor` are reported below.
Long-form word/timestamp comparisons were per window; each timestamp tick is
0.02 s:

| Clip | Audio | Windows | Mel max error | Encoder NRMSE / cosine | HF comparison | WER | Total time |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| 5.9 s test clip | 5.9 s | 1 | 0.01339 | 4.33% / 0.99906 | exact tokens (`23`) | — | 17.9 s |
| `1919-142785-0007` | 26.6 s | 1 | 0.00946 | 3.05% / 0.99953 | exact tokens (`85`) | 0.0% | 34.4 s |
| `3170-137482-0000` | 28.0 s | 1 | 0.00971 | 2.30% / 0.99973 | exact tokens (`84`) | 1.5% | 31.6 s |
| `422-122949-0013` | 32.6 s | 2 | 0.00970 | — | words exact; timestamp deltas `4, 0` ticks | 6.0% | 89.4 s |
| 96 s LibriSpeech clip | 97.0 s | 4 | 0.00940 | — | words exact; timestamp deltas `5, 0, 1, 0` ticks | 2.3% | 323.7 s |

These are full-checkpoint Phoenix measurements of the earlier NPU frontend
and token-selection path, not the current fused frontend.

With the current fused frontend and one-call Hugging Face window reference,
both 64-frame Phoenix frontend probes pass the `0.008` maximum-absolute-error
bound: silence is exact and the non-silent probe measures `0.00390`. The
current fixed-input Whisper application suite passes all eight tests on
Phoenix, including the 35 s two-window utterance `4507-16021-0047`; its
independently generated Hugging Face per-window words and timestamps match
with zero tick difference. The long-form Mel error is `0.003906`, and the
short application clip measures `0.003890`. Teacher-forced decoding over
the short and medium clips has zero top-1 mismatches, mean KL at most
`0.000187`, and maximum KL at most `0.00103`. Alternating pretrained-weight
calls are bit-identical.

The 5.86 s real Phoenix probe
(`whisper-test-librispeech.wav`) passes `--check-reference`: Mel max error
`0.00390`, encoder NRMSE `3.621%`, and exact HF token match. This CLI check
uses the checkpoint's independent Hugging Face feature extractor and
generation path, not IRON's audio frontend or timestamp-rule implementation.

## Testing

```bash
pytest tests/applications/whisper/reference/   # device-free toy graph
pytest tests/applications/whisper/             # hardware tests on NPU1 and NPU2
```

Hardware tests use fixed LibriSpeech utterances and
`weights_dir("whisper-small")` (by default `/srv/whisper-small`). Set
`IRON_EXAMPLE_WEIGHTS_DIR` to the parent of your local `whisper-small`
checkpoint directory; tests do not search the Hugging Face cache or allow
environment overrides for the audio. The short benchmark records the
whole encoder/decoder window as Latency, not time to first token.

NPU2 profiles resolve device-free, but Krackan hardware validation is
pending; only Phoenix hardware is available locally.

Record missing goldens where `torch` and `transformers` are installed with
`pytest <test> --record-goldens -p no:xdist`.
Golden keys include the Mel input's contents, shape and dtype; label-only
goldens from the initial port must be re-recorded. With `--random-weights`,
pretrained-golden accuracy checks are skipped; determinism still runs.
