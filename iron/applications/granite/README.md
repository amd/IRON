<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Granite 4.2 3B on the NPU

Prefill and decode of IBM's Granite 4.2 3B as one IRON graph, `Granite`, a
version compiled per input shape, judged against transformers as Llama is
(see `iron/applications/llama/README.md`). `GraniteForCausalLM` is pure
dense attention: Llama 3's layer plus four scalars from its `config.json`,
so what is Granite's own is short, all of it in
`iron/applications/granite/model.py`:

- its `GraniteConfig` (`DecoderConfig` plus `attention_multiplier`,
  `residual_multiplier`, `embedding_multiplier` and `logits_scaling`), whose
  `attention(i)` sets `Attention`'s logit scale and `layer(i)`
  `DecoderLayer`'s residual scale
- the embedding rows scaled by `embedding_multiplier` in `embed()`, and the
  logits divided by `logits_scaling` in `head()`, the divisor folded into
  the final norm's weight as `iron.lm.Derived`; each is skipped at 1.0, as
  this checkpoint's are
- its own output head, untied from its embedding (`lm_head.weight`)
- its tokenizer's lead token, `<s>`
- its checkpoint, which ships as two shards (`Checkpoint` maps the
  `.safetensors.index.json` beside them)

Everything else is `iron.lm`, shared with Llama 3
(`iron/applications/llama/`).

## A note on scale: the full-ELF arena

Granite's ~7.3 GB of weights pushes a device buffer offset in the full-ELF
decode step's arena past aiebu's 32-bit relocation addend range (Llama 3.2
1B and EmbeddingGemma 2 are both well under 4 GB total, so this was not hit
before). The arena is banks of at most 3.5 GiB, each its own buffer object
and argument (`iron/common/image/allocator.py`'s `BANK`), so the decode
step links as a full ELF again, with the device loop, at Granite's scale.
`--no-full-elf` (the per-step xclbin-chain packaging, the form NPU1
always runs) still works and is still tested (`TestEachStep`), but is no
longer the default.

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
can be anywhere, with `config.json` beside the checkpoint. Its native
context, 131072 positions, holds 10 GiB of caches beside the weights' 6.8
GiB, the default where the host has room for both (`Runner.fit`);
`ulimit -l` must cover one of the arena's banks
(`iron.common.image.allocator.BANK`, 3.5 GiB).

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

The options are `iron.applications.llama.model`'s own (see its README):
`--random-weights`, `--prompt-len`, `--num-tokens`, `--max-seq-len`,
`--temperature`, `--top-k`, `--check-accuracy`, `--check-determinism`,
`--compare-host`, `--cost-table` and `--full-elf`/`--no-full-elf`.

## Tuning

`python -m iron.lm.tune granite --checkpoint /path/to/model.safetensors.index.json`
measures the cost table its designs can be narrowed and packed by, as
`iron/applications/llama/README.md`'s "Tuning" section describes.

## Testing

```bash
pytest tests/applications/granite/
```

Loads the model once and runs in-process through `model.Runner` the
throughput, accuracy and determinism checks above, again in the each-step
form (`TestEachStep`), and over a two-chunk prompt and a chat turn.
