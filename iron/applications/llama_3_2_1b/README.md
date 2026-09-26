<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Llama 3.2 1B

Llama 3.2 1B inference on the NPU, in bfloat16. The model is one IRON graph
function, compiled once for the prompt's shape and once for a decode step,
over one set of weights and KV caches that stay on the device. The NPU path
needs no torch: the checkpoint is memory-mapped with numpy and uploaded
directly into device buffers. Only the accuracy check's CPU reference uses
torch.

## Requirements

1. The IRON environment from the repository root, with XRT sourced
   (`source /opt/xilinx/xrt/setup.sh`).
2. The application's extra Python packages (the tokenizer, `tiktoken`):
   ```bash
   python3 -m pip install -r requirements_examples.txt
   ```
3. The weights and tokenizer of
   [meta-llama/Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B):
   [`model.safetensors`](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main)
   and [`tokenizer.model`](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main/original).
   The command line takes their paths, so they can live anywhere; the tests
   look for them in `$IRON_EXAMPLE_WEIGHTS_DIR/llama3.2-1b/` (default
   `/srv/llama3.2-1b/`).

The tests run on NPU2 (Strix and Krackan) only.

## Running

Run from the repository root, as a module:

```bash
python -m iron.applications.llama_3_2_1b.npu /path/to/model.safetensors /path/to/tokenizer.model
```

The prompt is the first `--prompt-len` characters of `prompt.txt` (default
2048); `--num-tokens` tokens are generated after it (default 40). The prompt's
tokens and the generated ones together must fit in 2048 positions. Sampling is
temperature 0.7, top-k 50, from a fixed seed, so a run's text is reproducible.
The first run compiles every design before generating. Timings are printed to
stderr after the text.

Generation runs one of two ways:

- **Host loop** (default): the host calls the prompt and then each decode step,
  reads back the logits, and draws the next token on the CPU
  (`sampling.Sampler`).
- **Device loop** (`--device-loop`): every token is drawn on the NPU by the
  `Sample` operator at the end of each step, and each step starts the next
  with no host involvement beyond restarting runs. The host writes the random
  draw for every token to be generated before the prompt runs, and reads the
  tokens back at the end. `--compare-host` then generates again with the host loop from the
  same seed and prints how many tokens differ; the draws are bit-exact, so
  the expected count is 0.

```bash
python -m iron.applications.llama_3_2_1b.npu /path/to/model.safetensors /path/to/tokenizer.model \
    --device-loop --compare-host --num-tokens 100 --prompt-len 1024
```

Both loops use the same compiled images, so `--cost-table` (see
[Tuning the Decode Step](#tuning-the-decode-step)) applies to either.

Two checks have their own modes:

- `npu.py --check-determinism ROUNDS` generates greedily from two prompts,
  alternating, `ROUNDS` times each, and counts the runs whose logits differ
  bitwise from the first run of the same prompt.
- `accuracy.py` compares each step's logits against a float32 torch CPU
  reference, feeding both the reference's greedy token, and prints the mean,
  p90 and max KL divergence and the top-1 mismatches:
  ```bash
  python -m iron.applications.llama_3_2_1b.accuracy /path/to/model.safetensors /path/to/tokenizer.model
  ```

For example, with the weights in `/some/dir/llama3.2-1b/`:

```bash
export IRON_EXAMPLE_WEIGHTS_DIR=/some/dir
python -m iron.applications.llama_3_2_1b.npu \
    $IRON_EXAMPLE_WEIGHTS_DIR/llama3.2-1b/model.safetensors \
    $IRON_EXAMPLE_WEIGHTS_DIR/llama3.2-1b/tokenizer.model --device-loop
```

## Tuning the Decode Step

`npu.py --cost-table TABLE` narrows the decode step's designs (fewer columns
where a design gains little from more) and packs them into shared device
configurations, choosing by what each design costs on the device. The costs
come from a table that `tune.py` measures:

```bash
python -m iron.applications.llama_3_2_1b.tune /path/to/model.safetensors /path/to/tokenizer.model
python -m iron.applications.llama_3_2_1b.npu /path/to/model.safetensors /path/to/tokenizer.model \
    --cost-table iron/applications/llama_3_2_1b/decode_costs_npu2.json
```

`decode_costs_npu2.json` is an example table, measured on a Strix Halo NPU
(8 columns) in turbo power mode. Its entries are keyed by each design's
identity -- its code and parameters -- so a design changed since the table was
measured is not in it, and the tuner leaves that design as written (the
`[Tuning]` report lists it as unmeasured). Run `tune.py` again after changing
a design; it keeps the entries that are still current, measures only the rest,
and drops designs the graph no longer has (`--remeasure` measures everything
again). `tune.py` updates `decode_costs_npu2.json` in place unless given
`--table PATH`; to measure for another NPU, pass a new path, since entries
already in a table are kept, not remeasured. Run it with the NPU otherwise
idle, and note the power mode it prints.

## Testing

```bash
pytest iron/applications/llama_3_2_1b/
```

`test.py` runs the application end to end on the NPU: generation at two
prompt lengths and two token counts (recording time to first token and decode
tokens per second), the accuracy check against bounds on its KL, the
determinism check, and the device loop against the host loop (no token may
differ). Outside CI, the tests skip when the weights are not found.

Host-side tests that need no NPU cover the checkpoint reader, weight tree,
RoPE table and sampler, and the graph's wiring against the torch model
(operator by operator through each operator's CPU reference):

```bash
pytest iron/tests/infrastructure/llama_host.py iron/tests/infrastructure/llama_weights.py \
    iron/tests/common/llama_reference.py
```

The tests that read the real checkpoint skip when it is absent.

## Structure

| File | Contents |
|---|---|
| `npu.py` | Entry point: compiles and loads the model, runs the host or device loop |
| `graphs.py` | `LlamaGraph`: the model as one graph function |
| `harness.py` | Configuration, tokenizer, host generation loop, command-line arguments, timings |
| `weights.py` | Memory-mapped safetensors reader, weight tree, RoPE table (Llama 3 frequency scaling) |
| `sampling.py` | `Sampler`: temperature and top-k sampling, bit-exact with the device |
| `tune.py` | Measures the decode step's cost table |
| `decode_costs_npu2.json` | Example cost table (Strix Halo, turbo) |
| `accuracy.py` | Entry point: NPU logits against the CPU reference |
| `model.py`, `reference.py` | The torch CPU reference and its adapter to the harness |
| `test.py` | NPU tests |

`LlamaGraph.forward(x=None, *, token, position)` is one function traced at two
shapes:

- **Prompt** (`x` given, padded to 2048 rows): GEMM projections, RoPE, MHA,
  the KV caches written from row zero, then RMS norm and the output head for
  the last prompt row only.
- **Decode step** (no `x`): the token's embedding row and the position's RoPE
  row gathered on the device (`StridedCopy`), GEMV projections, the new K/V row
  written into the caches at `position`, attention against the caches (GEMV,
  `Softmax` masked to `position + 1` keys), then the same norm and head.

Both versions end in `Sample` (`iron/operators/sample.py`), which draws the
next token from the logits on the device. Its draw is the one
`aie.iron.kernels.sample.sample_ref` defines, bit for bit, and `Sampler` calls
the same function on the host, so the two loops pick the same token from the
same logits and the same random number. The device's top-k is bounded at 64.
Each call returns the logits and carries the drawn token and `position + 1`
into the next call; the device loop (`DeviceGeneration`, built on
`iron.CarriedLoop`) chains runs through that carry, keeping two decode runs in
flight.

Both versions share the graph function's scratch arena, so the weights are
uploaded once and the caches the prompt writes are the ones decode reads. The
checkpoint's pages are released as each weight reaches the device.

## Performance

Measured 2026-09-26 on Strix Halo (NPU2, 8 columns) in turbo power mode, with
the device loop: decode ran at 9.20 tokens/s (108.7 ms per step) tuned with
`decode_costs_npu2.json`, against 8.15 tokens/s untuned. The logits were
bit-identical tuned and untuned.
