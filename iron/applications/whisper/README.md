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
Slaney Mel projection, log, global maximum, dynamic clamp and scale/shift
on the NPU. Only sample padding/reflection and WAV decoding stay on the
host. Long-form normalization uses the complete recording plus 30 seconds
of silence, before slicing its decoder windows.

Token selection also runs on the NPU. The host writes one small Sample
draw row per step: history-dependent suppression ranges and the
timestamp/text split. Static scattered suppression tokens are a resident
negative-infinity bias. Sample applies the forced-timestamp probability
rule and returns the selected token; transcription does not read back the
vocabulary-sized logits. `Whisper.logits` retains full readback for
teacher-forced accuracy checks.

Audio up to 30 s is transcribed in one window without timestamps. Audio
longer than 30 s (or with `--long-form`) runs OpenAI Whisper's sequential
long-form algorithm with `ApplyTimestampRules`: each 30 s window is decoded
with paired non-decreasing timestamps, advancing the next window to the last
complete timestamp pair. When it rewinds, unfinished trailing text is discarded
so the next window does not duplicate it.

- `model.py`: `WhisperConfig`, `WhisperEncoder`, `WhisperDecoder`,
  `Whisper`, `TokenPolicy` and the CLI
- `audio.py`: 16 kHz mono WAV loading and the NumPy log-Mel reference
- `hugging_face.py`: Hugging Face's `WhisperForConditionalGeneration` in
  float32, used only when recording goldens or running `--check-reference`
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

The revised NPU log-Mel and Sample path was measured on Phoenix (`npu1`),
with the complete `whisper-small` checkpoint and five local LibriSpeech
clips. Mel error is maximum absolute error against the NumPy reference;
short-window encoder and token comparisons use the Hugging Face float32
reference. Long-form word/timestamp comparisons are per window; each
timestamp tick is 0.02 s:

| Clip | Audio | Windows | Mel max error | Encoder NRMSE / cosine | HF comparison | WER | Total time |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| 5.9 s test clip | 5.9 s | 1 | 0.01339 | 4.33% / 0.99906 | exact tokens (`23`) | — | 17.9 s |
| `1919-142785-0007` | 26.6 s | 1 | 0.00946 | 3.05% / 0.99953 | exact tokens (`85`) | 0.0% | 34.4 s |
| `3170-137482-0000` | 28.0 s | 1 | 0.00971 | 2.30% / 0.99973 | exact tokens (`84`) | 1.5% | 31.6 s |
| `422-122949-0013` | 32.6 s | 2 | 0.00970 | — | words exact; timestamp deltas `4, 0` ticks | 6.0% | 89.4 s |
| 96 s LibriSpeech clip | 97.0 s | 4 | 0.00940 | — | words exact; timestamp deltas `5, 0, 1, 0` ticks | 2.3% | 323.7 s |

These are full-checkpoint Phoenix measurements of the revised NPU frontend
and token-selection path, not the earlier host-preprocessing baseline. The
table was collected before the final unfinished-segment trimming correction.

After that correction, all eight fixed-input Phoenix device tests passed,
including the 35 s two-window utterance `4507-16021-0047`: its per-window
text and timestamps matched the float32 reference, with zero timestamp
delta. Teacher-forced decoding over the short and medium clips had zero
top-1 mismatches, mean KL at most `0.000213`, and maximum KL at most
`0.000724`. Alternating pretrained-weight calls were bit-identical.
The 2 s short-clip encoder/decoder window measured 4.48 s Latency
(excluding frontend extraction, compilation and weight loading).

### Chained-xclbin diagnostic

The original Windows prototype timed out on the first two designs of a
ten-design encoder chain. That used an older runtime and is not evidence
of an eight-kernel hardware limit. A checkpoint-free reconstruction using
the current APIs is available from the repository root:

```bash
python -m utils.probe_xclbin_chain --kernels-per-image 10 --output chain-ten.json
python -m utils.probe_xclbin_chain --kernels-per-image 8 --output chain-eight.json
```

Source XRT as described in the installation guide, and run only one NPU
process at a time. The probe builds five GEMMs, LayerNorm, Softmax, GELU
and two additions at the encoder's 1536/768/3072 dimensions. It records
kernel names, image/instruction paths, dispatch failures and reference
comparisons as JSON, returning a nonzero exit status for a failure.
`--compile-only` builds without dispatching; the rows, width and hidden
dimensions can be reduced to multiples of 256 for a quicker smoke check.

On Phoenix with `mlir-aie` `1.4.5.dev119`, all ten full-size designs passed
in a single image, both with an explicit ten-kernel batch and the wheel's
default batch size of 32. The historical timeout was **not reproduced**
on this stack. The script is a current-API reconstruction, not the original
obsolete-API probe, and no Linux or NPU2 result is claimed.

## Testing

```bash
pytest tests/applications/whisper/reference/   # device-free toy graph vs Hugging Face
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
