<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Operator model: annotated designs, inferred specialization, per-op tuning

Draft plan. Input to a plan-refining session, not a finished plan.

Branch `operator-model-argspec`. Baselines (always `source /opt/xilinx/xrt/setup.sh`
first): `iron/tests` 745 passed / 13 skipped; `iron/operators` 3165 passed with 5
known `mem_copy` 16-core timeouts.

---

## 1. Priorities driving this

In roughly the order they were raised:

1. **General purpose.** LLMs, CNNs, anything composed of IRON operators. Not a
   llama-shaped abstraction, and specifically *not* a `forward()` method.
2. **No string names.** Buffers, weights, and runtime scalars addressed by
   handles and by parameter identity, not by hand-typed strings.
3. **Library quality.** Other people write models against this: stability, docs,
   a real test surface per operator.
4. **Prefill is in scope**, not just decode.
5. **Per-operator tuning, easy to override** by a user who wants something else.
6. **Tuning may fail.** Some operators legitimately have no legal config for a
   given shape/device. Per-device decisions must come from the target model's
   numbers, not hard-coded constants.
7. **Minimal duplicated spec logic**, to shrink the surface for typos.
8. **Static and build-time checking for new operators, including untested ones.**
9. **Fix the operators that flatten** real 2-D shapes into one dimension. Believed
   to be an artifact of old mlir-aie limits that have since been lifted.
10. Coverage checks **run on every build unless disabled**.
11. pyright suppression lives in **pyrightconfig, not per-file**.
12. `Tuning[T]` is **IRON-local** (not upstreamed for now).

---

## 2. Diagnosis: what `llama_npu.py`'s 1182 lines actually are

| chunk | lines | what |
|---|---:|---|
| operator construction | ~370 | `GEMV(M=..., K=..., num_aie_columns=8, tile_size_output=dim//8, ...)` x30 |
| runlist + sequence | ~140 | string-threaded `(op, "x", f"layers.{i}...", "x_norm")` |
| buffers + weight upload | ~160 | `XRTTensor`, `_upload`, subviews |
| prefill host glue | ~300 | CPU/NPU ping-pong: softmax, `torch.matmul`, `torch.cat` on host |
| decode glue + main | ~90 | |

`capture()` as it stands attacks only the ~140-line runlist. **Operator
construction is the biggest chunk**, which is why the work centres on the
operator model rather than on the graph recorder.

Note the prefill ~300 is a *different* problem — missing/unfused operators, not
authoring. No annotation scheme fixes it. See open question O5.

---

## 3. The core shape of the proposal

### 3.1 The design signature is the single declaration

mlir-aie already ships the vocabulary and the introspection, and IRON does not
use any of it: `In` / `Out` / `InOut`, `CompileTime[T]`, `DispatchTime[T]`
(`aie/utils/compile/jit/markers.py:51-113`) and `split_params()`
(`aie/utils/compile/jit/_introspect.py:127`). IRON's designs are plain
unannotated Python, which is *why* `bind()` exists (guessing parameter roles by
name) and why `arg_spec` exists (hand-declaring direction and order).

IRON adds one marker upstream lacks — `Tuning[T]` — and one thing upstream's
bare `In` cannot carry: a shape.

```python
# pyright: suppression lives in pyrightconfig, scoped to iron/operators/**
from __future__ import annotations
from iron.shapes import In, Out, CompileTime, Tuning


def my_matvec(A: In[num_batches, M, K],
              B: In[num_batches, K],
              C: Out[num_batches, M],
              *, M: CompileTime[int], K: CompileTime[int],
                 num_batches: CompileTime[int] = 1,
                 num_aie_columns: Tuning[int] = 8,
                 tile_size_input: Tuning[int] = 4): ...


def my_matmul(A: In[M, K],
              B: In[(N, K) if b_col_maj else (K, N)],      # conditional, plainly
              C: Out[(N, M) if c_col_maj else (M, N)],
              *, M: CompileTime[int], K: CompileTime[int], N: CompileTime[int],
                 b_col_maj: CompileTime[bool] = False,
                 c_col_maj: CompileTime[bool] = False,
                 tile_m: Tuning[int] = 64): ...
```

Dim names are this design's own parameters, deliberately not in lexical scope.
`from __future__ import annotations` makes each annotation a string; the resolver
evaluates it with `localns` bound to **symbols** (to infer) or **ints** (to
generate). This is operationally a lambda over a namespace — Python writes it.

The design body then builds its L3 types *from the annotation* and forwards the
tensor params to `Runtime` directly:

```python
    rt = Runtime(sequence, [A, B, C, *fifo_endpoints])   # not re-declared L3 types
```

That deletes `arg_spec` and `bind()` outright. Everything falls out of one
signature: order, direction, shapes, dtypes, which params the author supplies,
which the graph may choose, which vary per dispatch.

### 3.2 Per-operator tuning

Two tiers. A constant knob is just a default; a knob derived from shape gets a
policy:

```python
@tuning_for(my_matvec)
def matvec_tuning(dev, M, K, num_batches=1, *, num_aie_columns=None):
    cols = num_aie_columns or dev.cols          # target model, not a constant
    if M % cols:
        raise Untunable(f"M={M} does not divide across {cols} columns on {dev}")
    return dict(num_aie_columns=cols, tile_size_input=4, tile_size_output=M // cols)
```

A call-site override is fed **into** the policy, so dependent knobs re-derive
rather than silently keeping values computed for a different `cols`. `Untunable`
is an expected outcome — better than defaulting into a config that compiles and
then hangs (cf. `mem_copy` 16-core).

Retires a live FIXME in `iron/operators/gemv/op.py` (`MAX_WRAP = 1023`, "pull
these shim BD bounds from the MLIR-AIE target model rather than hard-coding").

**Unverified:** what mlir-aie's target model actually exposes (cols, rows, L1
bytes, shim BD wrap/stride caps). Needs checking before `dev.cols` is promised.

### 3.3 Resolution, and the shape/tuning invariant

```
operand shapes -> unify -> CompileTime params -> tuning policy -> Tuning params -> construct
```

**A shape annotation may reference `CompileTime` params only, never `Tuning`.**
Otherwise the pipeline is a cycle. This holds naturally for all 12 operators, and
it *forces the right taxonomy*: `RMSNorm`'s `tile_size` is shape-bearing
(`rows = (size // tile_size, tile_size)`), so it must become a `CompileTime` dim,
which is also the un-flattening.

Call forms, all one mechanism:

```python
g(GEMV, w, x)                                       # infer shapes, default tuning
g(GEMV.tuned(num_aie_columns=2), w, x)              # override a knob
g(GEMV(M=2048, K=2048, num_aie_columns=2), w, x)    # explicit -- works today
```

### 3.4 `@operator` unifies the design with the dataclass

Today every operator declares its parameters three times: dataclass fields, the
design function signature, and `arg_spec`. `@operator` collapses that:

```python
@operator(my_matvec)
class GEMV(MLIROperator):
    """Matrix-vector product ``C = A @ B``, optionally batched."""

    M: int                      # see O1 -- hand-written or generated
    K: int
    num_batches: int = 1
    num_aie_columns: int = 8
    tile_size_input: int = 4

    @staticmethod
    def tuning(dev, M, K, num_batches=1, *, num_aie_columns=None): ...

    def reference(self, A, B):
        return A @ B
```

`@operator` reads the design signature once and: verifies the field list against
it; wires `get_arg_spec()` to the shape annotations; wires `get_mlir_artifact()`
to the design; runs the tier-2 checks below; registers the operator.

The class keeps only what is genuinely its own — docstring, `tuning`,
`reference`, `design_key`, one-offs like GEMM's `partition_B`. The big design
function stays module-level under its existing banner (see O2).

### 3.5 Authoring

```python
with capture(model) as g:
    x      = g.input((1, cfg.emb_dim))
    angles = g.input((1, cfg.head_dim))
    offset = g.param(np.int32)
    kc = [g.state((cfg.n_kv_groups, MAX, cfg.head_dim)) for _ in range(cfg.n_layers)]

    for i, blk in enumerate(model.layers):
        h = g(RMSNorm, x, blk.norm1.weight)
        q = g(RoPE, g(GEMV, blk.attn.q.weight, h), angles)
        ...
    logits = g(GEMV, model.out_head.weight, g(RMSNorm, x, model.norm.weight))

net = g.build("llama_decode").compile()
net[x] = embed(token)
net[offset] = n * cfg.head_dim
net()
probs = net[logits]
```

No strings. `capture(model)` learns `id(tensor) -> name` from
`named_parameters()`, so a parameter *is* its handle. Every intermediate is
undeclared — `infer_buffer_offsets` already pools by live range, which deletes
`AIEPrefillBuffers` (~70 lines of `XRTTensor`/`subview`).

Prefill differs by passing the matmul class in (`def ffn(g, blk, x, mm=GEMV)`),
which also turns the `.T` layout disagreement into `GEMM.tuned(b_col_maj=True)`
and deletes `_upload(k_major=...)`.

Not llama-shaped — a CNN is `g(Conv2D, net.conv1.weight, x)` in the same graph,
same allocator, same handles.

---

## 4. Verification for a new operator with no tests

**Duplication and verification pull in opposite directions.** A second
declaration catches *drift*, never *wrongness* — a matching typo passes. IRON
proves this today: `GEMV.arg_spec` says `(M,K),(K,),(M,)`, the design forty lines
later says `(num_batches*M*K,),(num_batches*K,),(num_batches*M,)`, and
`arg_spec_snapshot.json` (a third restatement, 22 classes) has blessed the
disagreement. Green. So verification must come from *structure and behaviour*,
not restatement.

**Tier 1 — static, pyright, nothing runs.** *Measured.* Wrong type for a
`CompileTime` param, missing argument, kwarg matching no parameter, missing
tensor. 6 of 8 seeded mistakes caught.

**Tier 2 — import, annotations only, no build.** *Mostly measured.*

| mistake | mechanism |
|---|---|
| shape names a nonexistent param | free names checked against the param list, with did-you-mean |
| shape names a `Tuning` knob | same check, explains the cycle |
| a `CompileTime` param in no shape and with no default | can never be inferred; flagged at import, not at first use |
| `tuning()` names a param that doesn't exist | signature vs param list |
| `tuning()` returns a key that isn't a `Tuning` param | returned keys checked |
| malformed shape annotation | evaluated against a canonical symbolic binding |
| forgot `from __future__ import annotations` | `NameError` at import, immediately |

**Tier 3 — build the MLIR, no hardware. Runs on every build unless disabled.**
`TensorAccessPattern` exposes `tensor_dims`, `offset`, `sizes`, `strides`,
`access_order()`, `access_count()` (per-element touch count) and
`compare_access_orders()` (`aie/helpers/taplib/tap.py`).

| mistake | mechanism |
|---|---|
| declared tensor never forwarded to `Runtime` | `fn_args` inspection |
| an `Out` never drained, an `In` never filled | sequence inspection |
| DMA addresses past the end of the declared buffer | `access_order()` max vs `prod(shape)` |
| part of an output never written | `access_count() == 0` on an `Out` — silent garbage |
| part of an input never read | `access_count() == 0` on an `In` |
| an output written twice | `access_count() > 1` on an `Out` |

These are only *possible* because of the single declaration: today the shape in
`arg_spec` and the `tensor_dims` in the TAPs come from different places, so
comparing them proves nothing.

**What still needs a test.** The math (only `reference()` answers that), and
access *order* — coverage can be complete while the permutation is wrong.

**Separately:** `run_test` currently uses the arg spec for direction and order
only and never checks `spec.shape`/`spec.dtype`, while tests feed it
pre-flattened data. That is why the GEMV rank disagreement is invisible. Worth
tightening independently of this plan; expect some currently-green failures.

---

## 5. Measurements taken

Probe at `/scratch/ehunhoff/spelling_probe/` (separate venv; `ironenv` untouched,
per requirements.txt drift risk).

**Spelling vs type checkers.** mlir-aie uses pyright,
`typeCheckingMode: "standard"`; IRON configures no checker today.

| spelling | pyright std | pyright strict | mypy --strict |
|---|---|---|---|
| `In[M, K]`, free names | 7 errors | — | — |
| `Annotated[Tensor, Shape[M,K]]`, free names | 7 errors | — | — |
| `In[M, K]`, module-level Dims | clean | clean | 33 errors |
| `Annotated[In, Shape[M,K]]`, module Dims | clean | clean | clean |
| **`In[M, K]` + config suppression** | **clean** | **clean** | n/a |

Suppression does **not** leak: a normal module still reports undefined names.
Strict is *better* than standard here — same result, more call-site checking.

**Resolver.** ~90 lines; classification, evaluation, inference, error messages.

```
concrete              A: in[1, 2048, 2048]  B: in[1, 2048]  C: out[1, 2048]
b_col_maj=True        A: in[256, 64]        B: in[512, 64]  <- flipped
INFER matvec          {'num_batches': 1, 'M': 2048, 'K': 2048}
INFER b_col_maj=True  {'b_col_maj': True, 'M': 256, 'K': 64, 'N': 512}
conflict   my_matmul: K=64 from 'A' but 99 from 'B'
rank       my_matmul: operand 'A' has rank 3 (256, 64, 7), declares rank 2 in[?M, ?K]
typo       shape of 'A' refers to 'KK' ... Did you mean 'K'? Valid dims: ['M', 'K']
tuning-ref shape of 'A' refers to 'num_aie_columns' ... is a Tuning knob; a shape
           may not depend on one.
```

Two findings from building it, both of which would have bitten later:

- **Annotations must be evaluated one at a time.** Evaluating them together forces
  `(N,K) if b_col_maj else (K,N)` while `b_col_maj` is still symbolic.
- **A param a shape *branches* on cannot be symbolic.** Discovered rather than
  annotated: a forced symbol names itself, so it drops to its default and retries.

**Synthesised dataclass fields.** Measured: pyright reports
`No parameter named "M"` on **valid** calls. `@dataclass_transform` does not help
(PEP 681 infers from class-body annotations). Worse than unchecked — see O1.

---

## 6. Looked at and dismissed

| option | why not |
|---|---|
| `Layer` + backend + `using()` + `infer` (exists on `ehunhoff/graph-capture-frontend`, incl. a 67-line `llama_model.py` and `iron/nn/`) | too much machinery; indirection the annotation model removes |
| `forward()` on the model tree | llama-shaped; `iron/models/llama.py` is deliberately parameters-only |
| Central `iron.shapes` registry of dim names | a global namespace of every dim any operator might use, edited per new operator |
| Module-level `M, K = dims(...)` per design module | works (measured clean) but names each dim three times |
| `Annotated[In, Shape[M,K]]` | only buys mypy, which nobody here runs; keep as a mechanical fallback if that changes |
| Per-arg lambda `In[lambda p: (p.M, p.K)]` / `@shapes` decorator | noisy; and a deferred annotation *is* a lambda over a namespace, so this was the same mechanism spelled explicitly |
| `declare()` in the body + sentinel exception | control flow by exception |
| String dim names `In["M", "K"]` | conditionals inexpressible; strings |
| Reading `A.shape` inside the design | upstream `_TensorPlaceholder` poisons attribute access on purpose |
| A general inverse shape solver | no precedent in torch/JAX/ONNX/MLIR — all go params->shapes. Reframed as lazy specialization (`LazyLinear`, `flax.linen.Dense`) |
| Symbolic unification of the existing `arg_spec` | superseded: the annotation *is* the symbolic form |
| `DispatchTime[T]` for llama's `cache_offset` | upstream forbids `full_elf=True` with unbound dispatch params; llama decode is full-ELF. Adopt the *annotation*, map to `ScratchpadParameter`. See memory note `project-dispatch-bridge-not-applicable` |
| Einops-style shape DSL | GEMM's own docstring: "any shape-expression language able to express it would have become Python again" |
| Killing GEMV's `num_batches` conditional | unnecessary — conditionals work. See O4 |

Not dismissed, never got a verdict: **ports-then-`yield`** — declare `A = In(...)`
at the top of the body where the params *are* in scope, `yield` as a signature
barrier. Only real cost is one unusual idiom.

---

## 7. Open questions

- **O1. Field list: hand-written-and-verified, or generated into the source?**
  Synthesis is ruled out by measurement. `@operator` verifies either way and
  prints a diff on mismatch. A `--fix` mode that writes the block removes the
  hand-typing without losing pyright. ~30 lines on top of the verifier.
- **O2. Design function module-level or an in-class `design` staticmethod?**
  Module-level preserves the current file structure and keeps a 300-line function
  out of the class body; in-class makes `@operator` argument-free.
- **O3. Where does the tier-3 opt-out live?** Per-operator attribute, env var, or
  both. `access_count()` materialises a buffer-sized array — llama's 2048-padded
  attention buffers x32 heads is real build time. Possibly: bounds-check always,
  full coverage below a size threshold.
- **O4. `num_batches` — confirm rank-directed branch resolution.** It is both
  branched on *and* the thing we want to infer. Options: pin it; delete the
  conditional; or resolve the branch from operand rank first (recommended — keeps
  the conditional *and* infers, two deterministic passes).
- **O5. Prefill scope.** ~300 lines of CPU/NPU ping-pong need real operators
  (masked softmax, attention context matmul, cache concat). Larger than the
  authoring rewrite. Sequence it after decode?
- **O6. Which operators convert, in what order?** GEMV first as the pilot. Then?
- **O7. Branch or worktree**, to keep the 745 / 3165 baselines undisturbed.
- **O8. Upstreaming.** `Tuning[T]` is IRON-local for now, but it is a genuine gap
  in mlir-aie next to `CompileTime`. Revisit once it has proven itself.

---

## 8. Carried risk, unrelated to this work

**NPU decode output degrades after a few tokens** vs `llama_cpu.py` on the same
prompt and seed. Prefill reproduces exactly and the first tokens agree, then the
NPU drifts. Not the weight-naming refactor — uploaded bytes are `torch.equal` for
all 146 parameters. Predates observation; `llama_npu.py` could not run on this
host until XRT 2.26. `iron/applications/llama_3.2_1b/test.py` asserts only
`returncode == 0`, so it does not catch this, and **a rewritten llama will inherit
it and look guilty**. Decision taken: snapshot the current token stream as a
before/after artifact and proceed. Cheapest real probe if revisited: compare NPU
vs CPU *logits* for one decode step rather than sampled tokens.
