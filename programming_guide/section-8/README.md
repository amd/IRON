<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 8 - From Graphs to a Language Model

Every primitive this guide covered — `body`, handles and `.step(...)`
(Section 2), per-call bounds (Section 3), weights and state (Section 4),
carried values (Section 5), the host reference and `check=True` (Section 6),
profiles (Section 7) — is what [`iron/lm/`](../../iron/lm/) is built from. A
language model is not a new layer of machinery on top of `iron.Graph`; it is
a `Graph` recorded the same way the rest of this guide's graphs were, over a
module tree of weights that load from a checkpoint by name instead of being
constructed as plain numpy arrays.

## A whole model, named

[`iron/applications/llama/model.py`](../../iron/applications/llama/model.py)
is the whole of Llama 3 on top of the shared decoder:

```python
class Llama(CausalLM):
    """Llama 3 on ``config``'s shape and a checkpoint's ``weights``."""

    config = LlamaConfig
    profile = Path(__file__).with_name("profiles")
```

Everything Llama-specific is `LlamaConfig` (RoPE frequency scaling, and the
precision its wider GEMMs need — Section 4 and 7's territory) and a
directory of profiles (Section 7). The rest — the decoder's layers, its
attention and feed-forward blocks, its KV cache, sampling, chat turns — is
[`CausalLM`](../../iron/lm/causal.py), one shared graph every text decoder
(`Llama`, `Gemma4`) composes.

## Walkthrough of [toy_decoder.py](./toy_decoder.py)

A real checkpoint's weights are gated on Hugging Face and are more setup
than a guide should ask for. `toy_decoder.py` instead draws Llama's own
`Llama` class a tiny, one-layer config and random weights, the same way
`tests/applications/llama/reference/test.py` and
[`iron/tests/support/llama_model.py`](../../iron/tests/support/llama_model.py)
build toy-sized decoders for their own device-free and device tests:

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

`Checkpoint(path).tree("random", seed)` is what a model's own `load`
reads from a real checkpoint directory; given a sparse file (a header and a
hole, `toy_checkpoint`'s), it draws every weight at `seed` instead, reading
nothing past the header. `Llama(config, weights)` then runs exactly what the
real `Llama.load` does under the hood: `CausalLM.__init__` builds the module
tree and calls `Graph.load_state_dict` (Section 4) to bind it.

### `CausalLM.body`, in the vocabulary this guide taught

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

* `ids`, an optional positional input (Section 2): a prompt chunk's token
  ids when given, `None` for a decode step, which instead reads the last
  sampled `token`.
* `token` and `position`, **carried** (Section 5): the host seeds them once
  per conversation; after that, each call carries forward the token it just
  sampled and the position one past what it just ran.
  [`Session`](../../iron/lm/session.py) is what manages one conversation's
  carried values and caches across many calls; `toy_decoder.py` drives the
  compiled versions directly, the same way Section 5's `Walk` did, to show
  the values themselves rather than `Session`'s bookkeeping.
* `start`, `rows` and `rope_start`, **scratchpad** (Section 3): `rows`
  bounds how much of a prompt chunk's compiled capacity this call actually
  runs, the same `x[:n]` mechanism Section 3's `BoundedRelu` used, here
  reaching every layer's attention and KV cache writes through `Call`.

Each layer's attention keeps its KV cache in `iron.state` (Section 4), one
`KVCache` per layer, sized by `max_seq_len` once and read only up to the
current position every call ("one compile, any context",
[AGENTS.md](../../AGENTS.md#design-rationale-and-known-limits)).

### Compiling its two versions and running a prompt plus a few decode steps

```python
decode = model.compile(**model.shapes()[0])          # no input: the decode step
prompt = model.compile(feeds=decode, **model.shapes()[1])   # ids: a prompt chunk

_, carry = prompt(ids, token=..., position=..., start=0, rows=8, rope_start=0)
for _ in range(decode_steps):
    _, carry = decode(**carry)                       # carry is exactly decode's kwargs
```

`model.shapes()` names each version's input shape, the decode step first
(none); `feeds=decode` sizes the decode step's Emit to start from the
prompt chunk's carried values, on NPU2. The prompt call's `carry` comes back
as exactly the keyword arguments the decode step's `body` takes, so
`decode(**carry)` chains one call into the next — the pattern
[`iron/lm/session.py`](../../iron/lm/session.py)'s `host_draws` uses to walk
a device decoder the same way, and that CausalLM is built to support once
dispatched end-to-end on the full-ELF device loop (`CarriedLoop`, Section 5).

### Checking it

```python
_, ref_carry = model.reference(ids, token=..., position=..., ...)
for _ in range(decode_steps):
    _, ref_carry = model.reference(**ref_carry)
```

`graph.reference(...)` (Section 6) runs the identical `body` on the host.
Greedy sampling is deterministic, so a correct device run draws the exact
same tokens as the host reference — `toy_decoder.py` checks the drawn token
sequences for equality, which needs no tolerance at all: either the device
drew the same token or it did not.

A whole decoder has dozens of chained rounding steps (every projection,
norm, activation), so no single step's tolerance covers its logits the way
one did in Sections 2 and 4. `compile(check=True)` is what verifies a graph
like this: each step checked against its own operator's `reference()` and
`tolerance()`, on its own dispatch, raising at the first one that misses.
Most of a prompt chunk's steps are bounded per call (`rows`, Section 3), and
a per-call bound's reference is not known until the call, so `check=True`
logs those as skipped rather than silently passing them:

```
[check step 3] ProjectionGEMM not checked: ['valid'] bounded per call
```

— an honest limit, not a gap in the guide: a per-call-bounded step still
runs and still produces a result, just one `check=True` cannot judge
without the bound it receives only at the call it is checking.

## <u>Exercises</u>

1. Run `python3 toy_decoder.py` on an attached NPU2; it compiles both
   versions, runs a prompt and a few decode steps, checks the drawn tokens
   against the host reference, and recompiles with `check=True` to verify
   every step that can be.
2. Raise `--decode-steps` and watch how many tokens still agree with the
   host reference — a toy model's random weights make for an arbitrary
   sequence, but correctness never depends on what the weights mean.
3. Read the quick start in the top-level [README](../../README.md#quick-start)
   again:

   ```python
   from iron.applications.llama import Llama

   model = Llama.load("meta-llama/Llama-3.2-1B")
   print(model.generate("The capital of France is", 8))
   ```

   `load` does what `toy_decoder.py` did by hand — build the model, compile
   its versions, `use` them — over a real checkpoint's weights instead of
   drawn ones; `generate` drives a `Session` the way this section's loop
   drove the compiled versions directly.

-----
[Prev](../section-7/) &middot; [Top](..) &middot; [Next](../section-9/)
