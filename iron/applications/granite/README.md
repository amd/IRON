<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Granite 4.2 3B on the NPU

Prefill and decode of IBM's Granite 4.2 3B as one IRON graph, `Granite`, a
version compiled per input shape, and the float32 numpy forward pass it is
checked against, `GraniteOracle`, its `oracle`. `GraniteForCausalLM` is
pure dense attention (no Mamba, MoE or hybrid layers): Llama 3's layer
plus four multipliers, so `Granite` and `GraniteOracle` mix in
`iron.lm.blocks`' `Block`/`BlockOracle`, the same attention and SwiGLU
math Llama 3 runs, and add only:

- its `Config` (2560/40/40/8/64/8192, vocab 100352, RoPE base 1e7, no scaling)
- the q-scale fold: Granite's `attention_multiplier` (1/64) replaces the
  usual `1/sqrt(head_dim)` (1/8) the library's `MHA`/`attend` hardcode, so
  `Runner` multiplies every layer's `q` by `0.125` once after loading --
  `0.125 * 0.125 = 1/64`, and exact, since a power of two only shifts bf16
  exponents
- its own output head, untied from its embedding (`lm_head.weight`)
- its tokenizer, `tokenizers.Tokenizer` over `tokenizer.json`, which adds
  no BOS of its own -- `Runner.encode` prepends it, as the library default
  does
- its checkpoint, which ships as two shards (`Checkpoint` maps the
  `.safetensors.index.json` beside them)

What is Granite's own is in `iron/applications/granite/model.py`; its
tunables are in `profiles/`. Everything else -- `CausalLM`, `Oracle`,
`Block`/`BlockOracle`, `Config`, the checkpoint `Layout`, `Runner`,
`generation` and `testing` -- is `iron.lm`, shared with Llama 3
(`iron/applications/llama/`).

## A note on scale: the full-ELF arena

Granite's ~7.3 GB of weights pushes a device buffer offset in the full-ELF
decode step's arena past aiebu's 32-bit relocation addend range (Llama 3.2
1B and EmbeddingGemma 2 are both well under 4 GB total, so this was not hit
before). The arena is now banks of at most 3.5 GiB, each its own buffer
object and argument (`iron/common/image/allocator.py`'s `BANK`), so the
decode step links as a full ELF again, with the device loop, at Granite's
scale. Before that fix, `--each-step` (the library's existing per-step xclbin-chain packaging,
the form NPU1 always runs) was the only way to run Granite at all; it still
works and is still tested (`TestEachStep`), but is no longer the default.

## Weights and tokenizer

From Hugging Face
([`ibm-granite/granite-4.2-3b`](https://huggingface.co/ibm-granite/granite-4.2-3b),
Apache-2.0, ungated), over plain https, with no account:

```bash
D=/path/to/granite-4.2-3b
REV=e459acceac81e5fe67c07d9cfc72329a332e7eb1  # the revision every KL figure here is against
for f in config.json generation_config.json tokenizer_config.json \
    special_tokens_map.json tokenizer.json model.safetensors.index.json \
    model-00001-of-00002.safetensors model-00002-of-00002.safetensors; do
  curl -fL -o "$D/$f" \
    "https://huggingface.co/ibm-granite/granite-4.2-3b/resolve/$REV/$f"
done
```

The tests look for them in `$IRON_EXAMPLE_WEIGHTS_DIR/granite-4.2-3b/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`); on the command line they
can be anywhere. `ulimit -l` must cover the weights (about 7.3 GB) plus the
caches (2.7 GB at `max_seq_len` 32768, 0.7 GB at 8192).

## Setup

Set up IRON as the repository root describes, then:

```bash
python3 -m pip install -r requirements_examples.txt
```

## Running

From the repository root:

```bash
python -m iron.applications.granite.model \
    /path/to/model.safetensors.index.json /path/to/tokenizer.json \
    --prompt-len 2048 --num-tokens 40 --compare-host
```

The flags are `iron.lm.base`'s, shared with every model --
`--random-weights SEED`, `--max-seq-len`, `--check-accuracy`,
`--check-determinism`, `--compare-host`, `--cost-table`, `--each-step`
(the per-step form, still available); see
`iron/applications/llama/README.md` for what each does.

## Tuning

`iron.applications.granite.tune` measures Granite's cost table the way
`iron.applications.llama.tune` does Llama's:

```bash
python -m iron.applications.granite.tune
python -m iron.applications.granite.model /path/to/model.safetensors.index.json \
    /path/to/tokenizer.json \
    --cost-table iron/applications/granite/costs_npu2.json
```

`pytest iron/applications/granite/` loads the model once and runs
accuracy, determinism and generation checks in-process through
`model.Runner`, recording the throughput and accuracy figures.
