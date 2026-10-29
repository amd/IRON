<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 8 - From Graphs to a Language Model

[`iron/lm/`](../../iron/lm/) is built from the pieces this guide has
covered: `body`, handles and `.step(...)` (Section 2), per-call bounds
(Section 3), weights and state (Section 4), carried values (Section 5), the
host reference and `check=True` (Section 6), and profiles (Section 7). A
language model is an `iron.Graph` like the others. The difference is that
its weights are a module tree loaded from a checkpoint by name, rather than
numpy arrays you build yourself.

## A whole model

[`iron/applications/llama/model.py`](../../iron/applications/llama/model.py)
defines Llama 3 on top of the shared decoder:

```python
class Llama(CausalLM):
    """Llama 3 on ``config``'s shape and a checkpoint's ``weights``."""

    config = LlamaConfig
    profile = Path(__file__).with_name("profiles")
```

What is specific to Llama is `LlamaConfig` (Llama 3's RoPE frequency
scaling and the precision of its projections) and a directory of profiles
(Section 7). The decoder's layers, attention, feed-forward blocks, KV caches
and on-device sampling come from [`CausalLM`](../../iron/lm/causal.py),
which `Gemma4` builds on too. A conversation's chat turns and cache
bookkeeping live in [`Session`](../../iron/lm/session.py).

## Walkthrough of [toy_decoder.py](./toy_decoder.py)

Llama's real checkpoints are gated on Hugging Face, so `toy_decoder.py`
uses the real `Llama` class with a tiny one-layer config and random
weights instead. The tests build toy decoders the same way
(`tests/applications/llama/reference/test.py` and
[`iron/tests/support/llama_model.py`](../../iron/tests/support/llama_model.py)).

```python
TOY = LlamaConfig(
    vocab_size=1024, hidden_size=512, num_hidden_layers=1,
    num_attention_heads=16, num_key_value_heads=4, head_dim=64,
    intermediate_size=2048, rope_theta=500000.0,
    max_seq_len=256, prefill_chunk=256,
)

checkpoint = toy_checkpoint(TOY, directory)        # a sparse .safetensors file
model = Llama(TOY, checkpoint.tree("random", seed=0))
```

`toy_checkpoint` writes a sparse `.safetensors` file: a header naming every
tensor and its shape, and no data. `Checkpoint.tree("random", seed)` reads
only that header and draws each weight from `seed`. A real load uses
`tree("read")` instead, which reads the weights. Either way,
`Llama(config, weights)` runs `CausalLM.__init__`, which builds the module
tree and binds the weights with `Graph.load_state_dict` (Section 4).

### `CausalLM.body`

```python
def body(
    self,
    ids: Handle | None = None,
    *,
    token: Carried[np.int32],
    position: Carried[np.int32],
    start: Scratchpad[np.int32] = np.int32(0),
    rows: Scratchpad[np.int32] = np.int32(1),
    rope_start: Scratchpad[np.int32] = np.int32(0),
):
    ...
```

* `ids` is an optional positional input (Section 2). A prompt chunk passes
  its token ids. A decode step passes nothing and embeds the carried
  `token`.
* `token` and `position` are **carried** values (Section 5). The host seeds
  them at the start. Each call then carries forward the token it drew and
  the next position.
* `start`, `rows` and `rope_start` are **scratchpad** values (Section 3).
  `rows` bounds how many of the prompt chunk's compiled rows a call runs,
  the same `x[:n]` mechanism as Section 3's `BoundedRelu`.

Each call ends with a `Sample` step that draws the next token on the NPU
from the logits. The host writes only the sampling settings; with none
written, the draw is greedy.

Each layer keeps its KV cache in `iron.state` (Section 4), one `KVCache`
per layer. The cache is sized once by `max_seq_len`, and each call reads it
only up to the current position. See "One compile, any context" in
[AGENTS.md](../../AGENTS.md#design-rationale-and-known-limits).

### Two versions: a prompt chunk and a decode step

```python
decode = model.compile(**model.shapes()[0])          # no input: the decode step
prompt = model.compile(feeds=decode, **model.shapes()[1])   # ids: a prompt chunk

_, carry = prompt(ids, token=..., position=..., start=0, rows=8, rope_start=0)
for _ in range(decode_steps):
    _, carry = decode(**carry)                       # carry is exactly decode's kwargs
```

`model.shapes()` lists each version's input shapes, the decode step first
(it takes no input). On NPU2, `feeds=decode` lets the prompt chunk's carried
values start the decode step. The prompt call's `carry` holds exactly the
keyword arguments the decode step takes, so `decode(**carry)` chains one
call into the next.

`Session` drives a model the same way. Where each decode step is started
from the host, it uses this loop (`host_draws` in `session.py`). On NPU2,
where the decode step is a full ELF, it instead runs the decode steps as a
device loop, `CausalLM.loop`, which is the `CarriedLoop` from Section 5.

### Checking it

```python
_, ref_carry = model.reference(ids, token=..., position=..., ...)
for _ in range(decode_steps):
    _, ref_carry = model.reference(**ref_carry)
```

`model.reference(...)` runs the same `body` on the host (Section 6). With
no sampling settings, the draw is greedy and deterministic, so a correct
device run draws exactly the same tokens as the reference.
`toy_decoder.py` asserts that the two token sequences are equal.

A decoder chains many rounding steps: every projection, norm and
activation. No single step's tolerance covers its logits, so
`compile(check=True)` is the way to check each step. The example
recompiles both versions with it. A prompt chunk's steps are mostly bounded
per call by `rows`, and `check=True` skips those with a warning such as:

```
[check step 3] ProjectionGEMM not checked: ['valid'] bounded per call
```

Those steps still run. The token comparison above covers them end to end.

## <u>Exercises</u>

1. Run `python3 toy_decoder.py` on an attached NPU2. It compiles both
   versions, runs a prompt and a few decode steps, checks the drawn tokens
   against the host reference, and then reruns with `check=True`.
2. Raise `--decode-steps`. The device and the reference should still agree
   on every token. Random weights make the sequence meaningless, but the
   two must still match.
3. Reread the quick start in the top-level [README](../../README.md#quick-start):

   ```python
   from iron.applications.llama import Llama

   model = Llama.load("meta-llama/Llama-3.2-1B")
   print(model.generate("The capital of France is", 8))
   ```

   `Llama.load` does what `toy_decoder.py` did by hand, with a real
   checkpoint: it builds the model, compiles both versions and loads them.
   `generate` tokenizes the prompt on the host and hands the tokens to a
   `Session`, which drives the compiled versions as above.

-----
[Prev](../section-7/) &middot; [Top](..)
