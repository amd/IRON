<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# The operator API, redesigned

Branch `claude/iron-pr221-api-simplify`, off amd/IRON PR 221 (`26ce43f`).
Toolchain: mlir-aie branch `aie2p-kernel-peano-opt`, built from source (see
Step 0). This file is the plan and its progress log; it travels with the
branch and is updated as steps land.

## Why

PR 221 lands the declared operator model (`declare/`, `design/`, `graph/`,
`image/`). The model is sound; the surface is dense, and the density falls on
performance engineers and ML programmers. On `applications/llama_3_2_1b/
graphs.py` (276 lines): **46** tunable kwargs at call sites, **18**
hand-written DMA size/stride/offset fields, **13** rank-plumbing reshapes,
**32** names exported from `iron.common.declare`; and every operator is two
classes and two decorators.

Goals: fewer concepts, with everything inferable inferred (the
`aie.iron.algorithms` style); friendly authoring, where a newcomer customises
a hello-world by inheritance, in one file, with an inlined C++ kernel; a
design that leaves the door open to autotuning, profiles and per-kernel L1 /
tile tuning without implementing them; dynamic sequences and full-ELF assumed
to coexist one day; flm kept, as an export. Typed throughout: pyright and ruff
run in CI with mlir-aie's configuration.

## Decisions

- **One class per operator; one organizing axis: when a value resolves.**
  Compile-time = baked into the artifact (array *or* sequence; which one is
  derived from where the field is used); dispatch-time = never baked.
- **1A** The array's dependency set is *declared*: a field is array-tier iff
  it appears in an operand's `tile=`/`per=`, in a stream's dtype, or is
  marked `param(..., array=True)`/`auto(..., array=True)`.
  `array(target)` receives a view exposing only those and raises on any other
  read. No learned read-sets.
- **2B** `In(*shape, dtype=, tile=, per=, depth=, via=)` absorbs `StreamIn`:
  one declaration per operand; `op.A[view]` a region, `op.A.lane(i)` a shim
  endpoint, `op.A.tile` the fifo type. Shape args stay extent-only; `tile=`/
  `per=` may be knobs.
- **3B** `Value(dtype, derive=..., address=, lock=)` replaces `Resident`: a
  resident when derived, a per-call value when a graph binds it;
  `Scratchpad[T]`/`DispatchTime[T]` remain the graph's per-call annotations
  (a `DispatchTime` value is never compiled in). `design_key` carries the
  bound values and `explain()` prints how each value reaches the device.
- **4B** `Shipped(GEMM, image=Xclbin(url=, sha256=))`: the shipped binary is
  a subclass; `image=` is consumed by `__init_subclass__` (replaces
  `External`, the `Xclbin` member, `prebuilt()`/`build()`; every operand needs
  `via=`, `array()` forbidden). flm moves to `iron/exports/flm`.
- Factories may carry more kernel/profiling data (legality and L1 footprint
  move onto `KernelContract`); compilation is cheap, so `legal=` may be a
  compile probe and the C11 check runs per class in the device-free suite.
- Autotuning: a content-keyed **tuning digest** (below). Door open, not built.

## The API

Hello world (rung 1: the template owns array and sequence):

```python
import numpy as np
from iron.common import BinaryElementwise

VADD = """
extern "C" void vadd(bfloat16 *a, bfloat16 *b, bfloat16 *y, int n) {
    for (int i = 0; i < n; i++) y[i] = a[i] + b[i];
}"""

class VectorAdd(BinaryElementwise):
    """y = a + b."""

    def kernel(self, target):
        tiles = [self.a.tile, self.b.tile, self.y.tile, np.int32]
        return target.kernel("vadd", tiles, source_text=VADD)

    def reference(self, a, b):
        return a + b
# onto a shipped factory: return eltwise.add_sized(self.line_size)
```

Rung 2 overrides `array(target)`; rung 3 overrides `sequence(rt)`. Each rung
is additive.

GEMV (rung 3):

The header as shipped (`iron/operators/gemv/op.py`):

```python
class GEMV(Operator):
    M: int = param()                    # sequence-tier: only in a shape
    K: int = param()                    # array-tier: in A's tile
    num_batches: int = param(default=1)
    num_aie_columns: int = auto()       # the most the shim budget allows that divide M
    tile_size_input: int = auto(2)
    tile_size_output: int = auto()      # None: tile_size_input
    kernel_vector_size: int = auto(repr=False, array=True)
    epilogue: str = param(default="none", repr=False, array=True)

    A = In(optional(num_batches), M, K, tile=(tile_size_input, K), per=(num_aie_columns,), depth=2)
    B = In(optional(num_batches), K, tile=(K,), per=(num_aie_columns,), depth=1)
    C = Out(optional(num_batches), M, tile=(tile_size_output,), per=(num_aie_columns,), depth=2)
    tiles = Value(np.int32, derive=lambda op: op.M // (op.num_aie_columns * op.tile_size_output))

    def validate(self): ...             # the knobs against each other, at construction
    def resolve(self, dev): ...         # the device and the extents: every auto() filled
    def compatible(self): ...           # the extents against the resolved knobs
    def array(self, target): ...        # sees the array tier alone
    def sequence(self, rt): ...         # fills and drains per lane
    def reference(self, A, B): ...
```

A field is declared by a specifier, not an annotation alone: `M: int` binds
no name for a shape to use, and `In(M, K)` needs one. `param` is a field
specifier to a checker (`default=` is keyword-only, so a `param()` without one
is a required constructor argument, and `GEMV(K="4")` is an error); `auto` is
not listed, since it always has a default and gives it positionally, which
pyright does not read. Both are compile-time; a `Value` bound to a
`DispatchTime` graph parameter is the dispatch-time side.

llama decode block as shipped (`iron/applications/llama_3_2_1b/graphs.py`;
46 knob keywords at call sites → 8, with the tuned values in a `Profile`
keyed by shape; 12 hand-written stride fields → 0; `cols` and
`get_current_device()` leave the graph):

```python
def decode_block(i, lw, x, angles, cache_offset, vector_size):
    h = RMSNorm(x, lw.norm1)
    q, k, v = (GEMV(w, h, tile_size_output=D // 2) for w in (lw.q, lw.k, lw.v))
    q = RoPE(q.reshape(H, D), angles)
    k = RoPE(k.reshape(G, D), angles)
    Copy(k, keys[i][:, cache_offset])
    Copy(v.reshape(G, D), values[i][:, cache_offset])
    k_all = Repeat(keys[i], repeat=H // G)
    v_all = Repeat(values[i], repeat=H // G)
    scores = ElementwiseMul(GEMV(k_all, q), scale, tile_size=L // cols)
    weights = Softmax(scores, vector_size=vector_size)   # per call: never baked
    ctx = GEMV(Transpose(v_all), weights)
    o = GEMV(lw.o, ctx.reshape(H * D))
    x = ElementwiseAdd(x, o)
    h = RMSNorm(x, lw.norm2)
    act = ElementwiseMul(SiLU(GEMV(lw.gate, h)), GEMV(lw.up, h))
    return ElementwiseAdd(x, GEMV(lw.down, act))
```

flm (`iron/exports/flm`): `class Shipped(GEMM, image=Xclbin(...))` pins every
knob, redeclares operands with `via=`, keeps `sequence()`.

## Resolution, profiles, digest

Precedence, once, before identity is taken: **explicit call-site value >
profile entry > `resolve(dev)` proposal > `auto(default)`**. Proposals apply
only to still-`auto` fields, so an explicit knob can never be overridden;
identity is taken after resolution, so two descriptions of one array build
one image.
Profile entries name compile-time knobs only; dispatch fields never enter a
key; a miss never searches; search never runs inside `array()`/`sequence()`
or a build.

A profile is data applied in a scope: shipped, as `Profile`. Not built: a
`GEMV.Tuning` synthesised from the `auto()` fields (`choices=` and `legal=`
are accepted and recorded; nothing reads them yet).

Not built. Per-kernel budget: the kernel declares `stack_bytes`/`static_bytes`/`lanes`
(optional; upstream `KernelContract.stack_bytes`); the template sums against
the *resolved* device's `core_memory_bytes`, chooses tile/depth, and checks
with a breakdown in the error. One legality predicate validates a pin, bounds
a default, prunes a search.

Not built. Tuning digest, two content-keyed tiers: kernel tier (slow, once per kernel
digest × knob point × device type × toolchain; built on upstream
`kernel_design` + `run_iters`; records metrics, L1 bytes, and the tolerance
it was judged at) and operator/graph tier (fast: `design_key` minus tuned
knobs; candidates from `auto()`, pruned by legality, ranked by the kernel
tier, top-k measured in situ). `iron.tune(graph, dev, level=, budget=,
digest=)` measures only what is missing; entries record their level so runs
extend, not restart; a kernel edit invalidates only that kernel. Per-model
profiles are exported slices. Nothing in an operator class knows it exists.

## Steps

Every step below is done; the Progress log records each, and this text
stays as the rationale. Each step is separately reviewable and ends with the
full device-free run compared against its baseline (80 failed / 1680 passed
/ 38 skipped on `26ce43f`: 40 need `pyxrt`, 35 need a device, 5 re-bind a
device after clearing it) and the toolchain run compared against its
(`iron/tests/toolchain`, its own conftest; 4 failures on `26ce43f`, all
needing a device). Each fix is minimal. `pyright` and `ruff check` are
clean at every commit.

0. **Toolchain from source** — done. mlir-aie `aie2p-kernel-peano-opt` (the
   only ref with `linalg.mv(output_rows=)`, which PR 221's GEMV calls) per
   `docs/Building.md`: cmake ≥ 3.30, lit, all submodules, `nanobind==2.12.0`,
   psutil; `aie.extras` vendored from `llvm/eudsl` `4853bb0`; the mlir wheel's
   `_mlir/*.pyi` stubs copied into `install/python/aie/_mlir_libs/_mlir/`
   (the build leaves them out; pyright needs them). Notes for the PR:
   `requirements.txt` pins `1d7b9ea` (2026-09-23), which has `output_rows`
   (#3624) but not the `trace_to_json(colshift=, kernel=)` signature that
   `iron/common/tracing.py` calls (#3805, 2026-09-25): device runs need no
   pin change unless tracing is on; the pin moves once a wheel past #3805
   is published.
1. **`@operator` → `__init_subclass__`** — done. Dead `pre_fields` gone; the
   nine jobs on the base hooks; `@dataclass_transform()` on both bases;
   `ABCMeta` dropped; pyright and ruff configured after mlir-aie's and run
   in the lint workflow.
2. **Field vocabulary**: `param()`/`auto()` (done: a rename on the two-class
   model, `auto(choices=, legal=)` recorded for a tuner); then `In(..., tile=,
   per=, depth=, via=)` (2B), `Value` (3B) and `array=True`/the restricted view
   (1A). Those three are one-class concepts (an operand's `tile=` is the
   stream the overlay owns today), so they land with the merge, operator by
   operator: a merged class answers as its own `ov`, so the graph, sequence
   and image layers keep working while both forms coexist.
3. **One resolution point** (`resolve(dev)` with extents, before
   `unique_designs()`); retire `overlay_defaults`, `tuning`, `for_extent`;
   `None`-guarded device defaults for gemv/softmax/rope/gemm. Gate: two
   spellings of one array → one design; llama image count before/after; the
   first profile registered is `llama_decode` with today's 46 values, and
   `applications/llama_3_2_1b/test.py`'s bit-identical-logits check runs
   against it before any inferred default is trusted.
4. **Views and `Copy`.** The pin test first (done: `tests/common/copy_taps.
   py`). Then:
   - A graph handle takes numpy basic indexing, `h[..., a:b]`, `h[i]`,
     `h.transpose(1, 0, 2)`, and a per-call `Scratchpad` value as the index
     on one axis, `keys[i][:, pos]`. A view is metadata: the base buffer and
     a `Walk` (offset, sizes, strides over it), plus the axis stride the
     per-call index scales. A contiguous static view is a sub-buffer, as
     today; any other view is an operand of `Copy` alone.
   - `Copy(src, dst=None)` replaces `StridedCopy`: two `Walk` params in
     place of eight sizes/strides/offset fields; its sequence legalizes each
     walk per channel (`_taps`' split of the highest non-unit axis, as
     pinned). `in_offset`/`out_offset` stay its per-call values; a per-call
     index binds to them with the axis stride as its scale, applied where
     the host writes the value (upstream's scratchpad offset is a raw
     element offset). The class declares which params take a view
     (`accept_views`), the one hook.
   - llama: caches become `(G, L, D)`; `Copy(k, keys[i][:, pos])`, `Copy(v.
     reshape(G, D), values[i][:, pos])`, prefill `Copy(k.reshape(n, G, D).
     transpose(1, 0, 2), keys[i][:, :n])`, `Copy(x[last]).reshape(1, E)`;
     the host passes row indices (`pos`, `n - 1`), not element offsets.
     Rank flattening in `infer.py` stays until the merge.
5. **Collapse the four one-purpose templates**; land `inline()` and the
   hello-world operator (`source_text=` on `declare_kernel`, hashing the
   string; `arg_types` from operands).
6. **C11 device-free**: build each class's array at two extents, require
   byte-identical core ELFs. Gates the merge.
7. **Merge** each operator onto one class. The mechanics, so both forms
   coexist and operators migrate one at a time with the suites green:
   - The merged base carries both surfaces. `Operator` gains what `Overlay`
     has (`resolve`/`resolved`, `array` (was `array(target)`), `streams`,
     `values`, `residents`, `design_key`, `tolerance`, `device`, `copy`,
     `name_parts`, `external`/`prebuilt`/`build`), and `op.ov` is `self`
     on a merged class (no `ov` field, no `_split_kwargs`, no `__init__`
     wrapper); a two-class operator keeps its separate `ov`. The graph,
     sequence and image layers keep reading `op.ov` until the last operator
     has moved, then `ov` goes.
   - `In(*shape, dtype=, tile=, per=, depth=, via=, replicate=)`: an operand
     with `tile=` is its own stream; `op.A` answers as a buffer (shape,
     elements, nbytes, views) and as a stream (`tile`, `lane(i)`/`[i]`,
     `bind`, `handles`, `count`). The array tier is declared: every field
     named in a `tile=`/`per=`/`depth=` or declared `param(..., array=True)`. `design_key`
     is the class and those fields, resolved; `array(target)` receives a
     view that raises on any other field, naming the rule.
   - `Value(dtype, derive=..., address=, lock=)`: a resident when it is
     derived or given a number (the preamble writes it), a per-call value
     when a graph binds it (`Scratchpad`'s lowering), `DispatchTime` when
     declared so. `residents()` goes: the derivation is on the member.
   - `array(self, target)`: the old overlay `design`; `sequence(self, rt)`:
     the old operator `sequence(rt)`; `reference` unchanged.
   - Rungs: the elementwise family (the four templates collapse to one
     `Elementwise` base whose operands say how many streams there are),
     then gemv/softmax/rope/transpose/repeat/mem_copy, then gemm/mha, then
     flm (→ `iron/exports/flm`; `Shipped(GEMM, image=Xclbin(...))`). Rename
     collisions first: flm `epilogue` resident → `mode`, dequant `qw`/`out`,
     `config_name`.
   - Open, noted: a per-call value given at a graph call site
     (`MV(a, b, start=pos)`) is not a constructor parameter a checker
     knows. Making a `Value` a field whose default is "unbound" would type
     it, and give the call site the tier choice (a number binds once per
     build, a handle per call); decide with the graph-layer rung.
   - Gates per rung: both suites identical to baseline; the C11 gate
     (GEMV's xfail turns strict-pass when `rows` becomes a `Value`); the
     design counts of step 3's test; llama's reference tests.
   - After the last rung: delete `Overlay`, `_overlay_class_of`, the tier
     guards, the `residents()` bridge; pyright's scope widens to
     `iron/operators`, `iron/applications` and the rest of `iron/tests`,
     since an operator's constructor is the dataclass one.
8. **Exports**: `declare` 32 → ~15; delete the dead re-exports in
   `iron/common/__init__.py`.

## Verification

Device-free net, in the order it catches things: `tests/common/graph.py`,
`tests/common/tiling.py`, `tests/common/declare.py`, `tests/operators/
rejected_shapes.py`, `tests/toolchain/lowering.py`, the compile-path tests
runnable with the built `aiecc`. Hardware only: `iron/operators/test.py` at
`Tolerance.exact()`, `strided_copy_offset.py`, `applications/llama_3_2_1b/
test.py`. Headline: 46/18/13 → ~4/0/3 on the llama graph; concepts 27 → ~15;
**no explicit knob resolves differently; no graph builds more images than
today**.

## Progress

- `7026f7f` Before review. Copy's channel split is one function,
  `_shares()`, read by the descriptors, the reference and the check; the
  split axis is the innermost, as it always was, and the prose now says
  so. MHA's array takes its shim columns from the operands' `via=` pins,
  so the pins are load-bearing on a built image and the columns are
  spelled once. `WeightedRMSNorm` and `MemCopy` keep their own arrays for
  reasons their docstrings now give: a two-core pipeline, and a bypass
  copy with no core. The toolchain note in Step 0 is corrected: the pinned
  wheel `1d7b9ea` has `output_rows`; only `trace_to_json`'s new signature
  (#3805) is past it, and only tracing calls it. This plan's decode block
  is the shipped one, with the shipped counts. Both suites identical to
  baseline.

- `3e2b5b1` Tests right-sized from coverage data. Per-test line
  coverage of `iron/tests/common` (161 tests, 4588 library lines reached)
  and per-file coverage of the toolchain suite, each test's reach compared
  with its siblings'. Coverage overlaps heavily by construction (every
  class-creation test runs the same `declare()`), so the data picked the
  candidates and the assertions decided: a test went only when a sibling
  reached the same lines and made the same claim. Five tests in
  `iron/tests/common/declare.py` folded into the ones that subsumed them
  (the knob-in-tile case into the knob-in-shape rejection, the leading
  optional dimension into the any-position test, `infer()` on tuples into
  `from_operands`, the two graph-bound-value tests into one, the private
  field-tuple check dropped for the array-key test that prints the same
  tier). The ReLU lines `iron/tests/common/elementwise.py` and
  `iron/tests/operators/rejected_shapes.py` both carried live in the
  template's file only; the tile-cap and column-set assertions the new
  files repeated from `rejected_shapes.py` and `testing.py` are gone.
  `array_identity.py` compiles RMSNorm no more, since it shares ReLU's
  template and array. Kept, with the numbers: the three new files
  (`elementwise`, `harness`, `testing`) reach 45 lines nothing else does
  and run in under a second; `test_llama_names_only_the_knobs_that_matter`
  and `test_two_spellings_of_one_array_are_one_design` are the two
  load-bearing gates and reach 55 lines of their own; the toolchain suite
  reaches 754 lines the device-free suite cannot (the operators' `array()`
  bodies), `array_identity.py` costing 60 of its 260 seconds for two lines
  of its own and the one claim no other test makes. Tests: 283 functions
  and 7195 lines at `26ce43f`, 305 and 7811 now, against a library that
  held flat (20535 to 20492 lines). Both suites identical to baseline.
- `5f414d3` Prose pass. Every docstring, comment and Markdown paragraph
  the branch changed, read as a person would: history narration replaced
  by the present, connective flourishes and section-number
  cross-references into this plan cut, the plan's Decisions, API,
  Resolution and Progress sections shorter with every fact and commit id
  kept. No code, error message, test assertion or SPDX header changed.

- `9d59de7` Audit, batch E: docs and tests. README names paths that
  exist (`iron/operators/test.py -k AXPY`, the packages under
  `iron/common`). AGENTS states the elementwise divisibility rule with the
  channel count and the cap, and how to bind a device on a host without
  one. This plan's GEMV listing matches the shipped header, its decisions
  use the shipped vocabulary, and the tuning paragraphs are marked "not
  built". Fifteen docstrings and comments that narrated history now
  describe the present. One `npu2` fixture in `iron/tests/conftest.py`
  replaces nine copies; the two tests that bound a device without
  restoring it use it. The lowering cases list each class once. Three new
  test files cover public surface that had none: the elementwise template
  (default split, the two refusals, the resident count, a sweep inherited
  by a subclass), `vectors`/`verify_buffer`, and the case sweeps. Writing
  the harness test found that `vectors()` drew bfloat16 inputs as small
  integers (ml_dtypes' bfloat16 has no numpy float kind), so `centered=`
  did nothing and ReLU's device test never saw a negative input; bfloat16
  now draws as a float. That changes every device test's inputs, which no
  host here can run; the tolerances are the kernels' contracts, judged
  the same way. Both suites identical to baseline.
- `f14f212` Audit, batch D, second half: names and tests. One name per
  concept: Copy's `num_aie_channels` becomes `num_channels`, Copy's and
  Repeat's `transfer_size` becomes `tile_size` (it is the tile), MHA's
  `num_of_pipelines` becomes `num_pipelines`. A `Testing` sweep is a
  callable of the operator class, so the shared sweeps read the class's
  `tile_cap` and shim budget and the elementwise templates carry the
  default sweep: ReLU, GELU, LayerNorm, ElementwiseAdd and ElementwiseMul
  declare no test of their own (a hello-world operator inherits one),
  Dequant and AXPY use the shared sweeps instead of byte-identical copies,
  and the length list is written once. `WeightedRMSNorm.tile_cap = 4096`
  states what its sweep hardcoded. The `aie.iron` imports inside eleven
  `array()` bodies are module-level, as the template's are. Both suites
  identical to baseline; the case sets on NPU2 are unchanged. Noted and
  left: `WeightedRMSNorm.array` and `MemCopy.array` restate the template's
  array, Copy writes its channel split three times, MHA's `via=` pins are
  inert on a built image, and the int32 RTP word type is written nine
  ways.
- `04c3b6a` Audit, batch D, first half: structure. A `param()` may have
  a callable default, computed from the operator when neither the caller
  nor an operand's shape gives it (`out_rows = rows * repeat`), and
  `check_derived(name)` checks that a value given as well agrees. This
  removes the seven None-then-fill-in-`validate()` blocks (Repeat,
  Dequant, RoPE, Copy's two walks and output size, MHA's three lengths,
  flm's packed sizes): their fields are plain `int`/`Walk`, and the asserts
  that guarded them (Copy's `walks`, MHA's `_lengths`) are gone. A checker
  reads a callable default as a default; it would not have read a
  `derive=` keyword. `compatible()` runs at construction once every knob
  is given, so an operator states each extent rule once: GEMM's M and K
  rules live in `validate()` alone and N waits for the column count; MHA's
  padding rule is one `check_derived`; flm's `_check_shape(error)`, which
  was parametrised over `ValueError` against `Incompatible` (itself a
  `ValueError`), takes no argument. One `tiling.fifo_depth(elements,
  dtype)` replaces the bank rule four operators wrote out (Transpose's as a
  literal 4096). The llama profile's transpose tile fits a context shorter
  than 256. Both suites identical to baseline; real-shape equivalence
  unchanged.
- `aec8ed7` Audit, batch C: the rest of the verified items. A
  profile's scope token lives in the context, not on the profile, so one
  profile entered from several threads is safe. The top-level `iron`
  module is typed (`TYPE_CHECKING` imports beside the lazy table, a
  literal `__all__`), `iron.graph` is overloaded for both decorator forms
  and a graph function's call returns `Any`, so a user's graph code is
  checked; `Scratchpad`, `DispatchTime` and `Profile` are reachable as
  `iron.X`. Construction is keyword-only at runtime as it is to the
  checker (`MV(3, M=..)` bound a field by position), and a positional
  call outside a graph reports where operands go. Compare mode runs each
  step as the xclbin path does, dispatch scalars included. A slice's
  layout is `(type, offset, length)` as its docstring says, so a
  full-ELF view of a slice is sized right. An operator whose streams are
  all replicated spans the device. A host without an NPU skips the
  device tests instead of aborting the session, and `--iterations`
  repeats only the tests that take `npu_runtime` (before, the device-free
  tree ran five times over). One `device_name()`; a standalone xclbin is
  built for the xclbin image. Gates compare failure sets with the
  iteration ids stripped: identical.
- `dd395e4` Audit, batch B: the newcomer bugs. One
  `Operator.resolve_columns(dev, given, num_channels, fits=)` is the
  column-budget rule everywhere: the count given, checked against the
  shim budget; otherwise the most the budget allows that leaves whole
  tiles by the operator's own `fits`; otherwise one, with `compatible()`
  naming the rule. Elementwise, Softmax, RoPE, GEMV, Transpose and GEMM
  use it. Six copies of the rule are gone, and with them Softmax's bare
  `max()` on an empty sequence and Transpose resolving to a count it then
  refused. The knob-free hello world resolves at 1024 elements. GEMM's
  column count is a knob the device fills (it was `auto(8)`, a constant
  no device could change, so every GEMM failed on NPU1); its M and K
  rules stay at construction and N waits for the count; the llama profile
  no longer states what GEMM picks on its own. Overriding an inherited
  field without an annotation is a `DeclarationError` naming the fix,
  where dataclass silently kept the base's default. Toolchain: four
  GEMM-on-NPU1 cases that skipped now pass; both suites otherwise
  identical to baseline. At the scaled-down test shape each GEMM takes
  the width its own N fills (8 or 4) where the profile gave all of them
  4; the real shape is unchanged.
- `ca956de` Audit, batch A: the silent-wrong-answer bugs. A per-call
  value's graph binding is part of what is built: `use_value(name,
  bound_to)` records the graph value, and `design_key` and the device
  symbol carry it, so two instances alike in every field but reading
  different graph values are two designs with two symbols (they were one,
  and the later value won). An elementwise tile past the line one core
  holds is refused at resolution instead of halved (`line_size` is gone:
  the tile is the line; the RMSNorm, LayerNorm and Dequant references
  used the whole row while the device saw half of it), and Dequant checks
  that its group size divides the line. An explicit instance called in a
  graph checks its operands' shapes at equal rank, not only their element
  counts (a transposed weight passed). `resolve()` returning `self` is an
  error, not a silent mutation of the caller's instance. The llama
  profile's prompt FFN lines state the cap they always had. Both suites
  identical to baseline; the real-shape equivalence check unchanged.
- `dcfe49c` `explain()` (decision 3B's last item) and rank-3 Repeat.
  `op.explain()` prints the array tier, the sequence tier and how each
  value reaches the device: written once per build (with its number once
  resolved), per call as a scratchpad word or a regenerated stream, or
  unused. `optional()` may sit on any axis of a declaration (one per
  declaration; the rank says whether it is present), so `Repeat` declares
  `In(rows, optional(seq), cols)` and takes the cache `(G, L, D)` as it
  is. The four reshapes around llama's two repeats are gone (17 → 13; the
  rest split heads out of a projection's flat output, which is the
  projection's rank, not the graph's), and so is the profile's
  `transfer_size=D` line, since a row's last axis is the default. The
  real-shape equivalence check against the explicit graph stays
  identical. Both suites identical to baseline.
- `dcfe49c` Review of the open typing item (Step 7, "open, noted": a
  per-call value at a graph call site is not a parameter a checker knows),
  probed with pyright. The constructor form can be typed: a `Value` that
  is a descriptor-typed dataclass field (`__set__` takes `T | Handle`,
  `__get__` returns the bound value) makes `MV(M=, K=, start="x")` and
  `MV(..., strat=5)` errors and `op.start` a typed read, at the price of
  an annotation on every `Value` line (`start: Value[np.int32] =
  Value(np.int32)`, since an unannotated class attribute is not a field to
  a checker). The graph-call form cannot: `MV(a, b, start=pos)` goes
  through the metaclass `__call__`, whose `**kwargs` no annotation can tie
  to the class's own fields, so a misspelled or mistyped value there is
  caught at trace time only (it is: `TypeError: has no per-call value`).
  Recommendation: leave it. The constructor form is the rarer one for a
  value (a number there is a resident, which `derive=` already covers),
  and the annotation would land on every operator for a check the graph
  form, where values are actually bound, cannot get.
- `8738ce5` Profiles. `Profile` (`declare/profile.py`, exported from
  `iron.common`) is data: `add(cls, **fields)` entries whose `param()`
  fields select operators by shape (one left out matches any value) and
  whose `auto()` fields are the knobs given. Applied in a `with` scope, the
  operator metaclass fills the knobs a call leaves open before
  construction, so the precedence the plan asks for holds by
  construction: explicit call-site value, then the most specific matching
  entry per knob (equal specificity that disagrees is an error at the
  call), then the declared default or what `resolve(dev)` proposes.
  Nothing in an operator class knows a profile exists. The llama graph's
  knobs are `graphs.py::profile(config, max_seq_len)`: every tile decode
  and prefill were tuned with, keyed by shape, plus the GEMMs' width and
  row tile and MHA's pipelines, now derived from the model's shape and
  `max_seq_len` (the three `LlamaGraph` parameters are gone; the
  scaled-down test shape needs nothing given). The graph function carries
  the profile (`iron.graph(profile=)`), so a trace, a compile and a host
  reference run all see it. The call sites still give, each load-bearing:
  the projections' half-head output tile (q's shape is o's when H·D = E),
  the score row's tile (its size is the FFN's when H·L = F), the prefill
  cache copies' transfer size, and the layout flags and dimensions that
  are not knobs. Knob keywords at the graph's call sites 37 → 6.
  **Unverified on hardware:** a device-free check traces the graph at the
  real shape on NPU2 and NPU1 (decode) and at 512 and 2048 prompt rows
  (NPU2) with the profile against the explicit graph at `9c546fa`, and
  every resolved operator is identical; at the scaled-down test shape the
  prompt norms now span the device's eight columns where they inherited
  GEMM's four. The bit-identical-logits run on a device
  (`applications/llama_3_2_1b/test.py`) has not been done. Both suites
  identical to baseline.
- `6a4f30e` Step 8, last: `iron.common.image`, `.design` and `.graph`
  re-export what something imports through them and nothing else (image 29
  → 6, design 9 → 7, graph 12 → 10); everything else is imported from its
  module. Both suites identical to baseline.
- `cb3a6f1` The llama graph names only the knobs that matter. A
  device-free check traces the graph at the model's real shape with the
  graph's own defaults (a decode step on NPU2 and NPU1, a 512-row prompt
  on NPU2) and at the scaled-down shape the host tests use, drops each
  keyword the graph passes one (class, name) at a time, and requires every
  one to change some resolved operator or fail somewhere
  (`tests/common/graph.py::test_llama_names_only_the_knobs_that_matter`,
  0.2 s). Removed as redundant: `num_aie_columns=cols` on every GEMV,
  elementwise op and RoPE (their own resolution spans the device, which
  is what `cols` is); `num_channels=1` and `s=8` on Transpose,
  `tile_k=64`/`tile_n=64` on GEMM and `num_channels=1` on the prompt norm
  (the defaults restated); the attention-context GEMV's `tile_out=4` (its
  input tile). Kept, each proven load-bearing: the tile choices decode
  ran with (`tile_out=`, `tile_size=`, Transpose's `m`/`n`), Repeat's
  transfer size, and the graph's three parameters (`num_aie_columns`,
  `num_of_pipelines`, `tile_m`), which the GEMMs and the prompt norms take
  and the scaled-down shape needs. Knob keywords in the graph 53 → 37;
  the remaining tile choices can retire only into a measured profile,
  which needs the device. Both suites identical to baseline.
- `a50cbc7` Step 8: exports. `iron.common.declare` exports the sixteen
  names an operator is written with (`Operator`, `In`, `Out`, `Value`,
  `Scratchpad`, `DispatchTime`, `Shim`, `Xclbin`, `param`, `auto`,
  `optional`, `select`, `from_spec` and the three errors), down from 25 (32
  before the merge); the bound members, `BufferView`, `DimRef`,
  `ValueSpec`, `infer`/`infer_kwargs` and `get_shim_dma_limit` are the
  library's and are imported from their modules. `iron.common` is the one
  import an author needs: those sixteen plus the elementwise templates and
  `DesignGenerator`. `Artifacts`/`Design`/`Step` re-exports with no user
  are gone, and with them the import-order workaround they existed for
  (`image/fusion.py` now imports `DesignGenerator` from its module, where
  the design-image cycle closes). Every file outside `iron/common` imports
  from `iron.common`, none from `.declare`. RMSNorm's device sweep asks
  its class for the shim budget instead of re-deriving it. pyright: 0
  errors, 0 warnings. Both suites identical to baseline. Measured and
  left: `iron.common.image/design/graph` each re-export names nothing
  outside the package imports (image: 25 of 29); they are
  library-internal, and can be pruned in a step of their own.
- `7f8575b` Step 7, last: ruff and pyright cover the whole `iron`
  package (operators, exports, applications, every test), not only
  `iron/common`; both are clean (pyright: 0 errors). What it took: a
  metaclass `__call__` typed under `TYPE_CHECKING` so a positional operand
  constructs a `Handle` and a keyword-only call the operator; `auto()`
  fields annotated with their resolved type; `artifacts` that raises
  instead of returning `None`; `bound_device()`/`device_name()` in
  `iron/common/device.py` for the places that read the device by hand.
  Both suites identical to baseline.
- `e7529ee` Step 7, rung 5: the two-class form is gone. `Overlay`,
  `Operator[OV]`, the `ov` field and its `__init__` wrapper,
  `_split_kwargs`, the tier guards, `Resident`/`BoundResident`,
  `StreamIn`/`StreamOut` and `to=`/`from_=` as declarations, `InOut`, the
  `residents()` bridge, `per_call_values` and `Overlay.prebuilt/build`
  are deleted (−420 lines net in `iron/common`); the shim budget is
  `declare/shim.py`. A sequence is `Sequence(op, data)`; a build hashes
  every declared base of the operator's class into its cache key (the
  elementwise base counted for nothing before). `Traced.overlays` is
  `Traced.arrays`, one operator per distinct array. The declaration tests
  are one file on a one-class `MV` (`tests/common/merged.py` folded into
  `declare.py`); the docs describe one class. Both suites identical to
  baseline; pyright and ruff clean on the same scope.
- `0f6fd26` Step 7, rung 4b: `iron/operators/flm` → `iron/exports/flm`
  (`git mv`; every import and path rewritten; `iron.operators` lists
  IRON's own operators alone, its `_SUBPACKAGES` gone; `iron/exports` is
  a pytest testpath). Both suites identical to baseline.
- `21eddaa` Step 7, rung 4a: flm's GEMM, its shipped binary and
  DequantBFP are one class each, so every shipped operator now is. The
  shipped binary is a subclass declared with the image, `class
  Shipped(GEMM, image=Xclbin(...))`: it pins the knobs (`init=False`),
  redeclares the operands with `via=`, hides the port's values and lays
  the image's parameter block out as one `Value(address=, lock=)`; the
  library drives the image itself (`External`, `Overlay.prebuilt()` and
  `Overlay.build()` are gone), and a class declared with an image may not
  define `array()`, must pin every stream and place every value. flm's
  `epilogue` resident is `mode`, beside the `epilogue` parameter. Call
  sites: `Shipped(M=, K=, N=)` for `GEMM(Shipped(), M=, K=, N=)`. Both
  suites identical to baseline.
- `45364a2` Step 7, rung 3: GEMM and MHA are one class each (−75
  lines net). Their reduction and tile counts are derived `Value`s; the
  tiles GEMM bakes beyond what its L2 streams name (`tile_m/k/n`, the
  layout flags, the accuracy and rounding flags) are declared array-tier;
  MHA's `B_q` and pipeline count likewise. A sequence may hand a lane any
  descriptor alone (an `Access` or an upstream `TensorAccessPattern`).
  `GEMM(M=, K=, N=, b_col_maj=True)` and `MHA(num_heads=, seq_len=)` are
  the whole constructions. Both suites identical to baseline.
- `702cca1` Step 7, rung 2: GEMV, Softmax, RoPE, Transpose, Repeat,
  MemCopy and Copy are one class each (7 files, −177 lines net). Their
  trip counts are derived `Value`s; GEMV's `tiles` replaces the rows per
  column it compiled into its core loop, so the C11 gate now passes for
  it too (the strict xfail is gone), and Softmax's `vector_size` is one
  `Value` that is the whole row unless a graph binds a per-call handle:
  `DynamicSoftmax` and its overlay are gone, `resolve_class` with them.
  What an array bakes beyond its tiles is declared (`kernel_vector_size`,
  `epilogue`, `method_type`, `s`, `tile_size`, `bypass`); a tile's dtype
  field is array-tier too. In a sequence an operand is its own stream:
  `rt.fill(self.A.lane(col), access)`, the buffer implied. The per-call
  values an instance binds are part of its `design_key`, and a derived
  value a graph binds is not written as a resident (the toolchain gate
  caught that on llama's decode graph). Both suites identical to
  baseline.
- `08e1f7a` Step 7, rung 1: the elementwise family is one class per
  operator. `iron/common/elementwise.py` is `Elementwise` (the array over
  lines, its `count` a derived `Value`) with `UnaryElementwise` and
  `BinaryElementwise` declaring the operand shapes as their own streams;
  the twelve elementwise operators (axpy, dequant, elementwise_add/mul,
  gelu, layer_norm, leaky_relu, relu, rms_norm and its weighted form,
  sigmoid, silu, tanh) and the inline-kernel hello world are each one
  subclass naming a kernel (12 files, −133 lines net). What a kernel call
  bakes (axpy's scalar, leaky_relu's alpha, rms_norm's epsilon, dequant's
  group size) is `param(..., array=True)`; the view `array()` runs on
  binds the operator's methods and properties too, so a `kernel()` that
  reads an extent is caught, and `super()` works inside it. `auto()`
  fields are annotated with their resolved type. Both suites identical to
  baseline; the C11 gate passes for the merged ReLU, ElementwiseAdd and
  RMSNorm.
- `404c939` Step 7, rung 0: the mechanics of the one-class operator,
  with every shipped operator still two-class and both suites identical to
  baseline. `Operator` carries the array surface (`resolve`, `array`,
  `build_array`, `streams`, `residents`, `tolerance`, `array_key`), and on
  a class declared without an overlay `op.ov` is the operator itself.
  `In(*shape, tile=, per=, depth=, via=, replicate=, broadcast=)`: an
  operand with a tile is its own stream (`op.A.tile`, `op.A.lane(i)`,
  `op.A.bind`, `op.A.count`). `Value(dtype, derive=, address=, lock=)`: a
  resident when derived, per-call when a graph binds it. The array tier
  is `_array_fields`: whatever a `tile=`/`per=` names plus
  `param(..., array=True)`; `array(target)` runs on a view that raises on
  any other field; `array_key()` is the class and those fields, so two
  extents of one array share a build. `tests/common/merged.py` exercises
  it on a GEMV-shaped operator: fields, lanes, a derived value, a per-call
  value in a graph, the two keys, the guard, resolution errors, inference.
- `d25f00a` Step 1: drop the pre-dataclass Field snapshot.
- `fd3ba37` Step 1: the bases process their subclasses; `@operator` is gone
  (38 files, +390/−509). Failure set identical to baseline.
- `610c926` Step 1: the bases are dataclasses to a checker; pyright in CI on
  the declare package. Members generic in their bound form; `Self` returns.
- `d782c44` Step 6: the C11 gate, `tests/toolchain/array_identity.py`:
  each operator built at two extents with the same knobs must leave
  byte-identical per-core ELFs (the real build; an insts-only lowering
  compiles no core). ReLU, ElementwiseAdd, Softmax, RoPE, RMSNorm and GEMM
  pass on both device widths; GEMV is a strict xfail, since it compiles the
  rows per column into its core loop (the `rows` `Value` of the merge
  fixes it); Repeat and Copy have no core.
- `a99ced5` Step 5a: `declare_kernel(source_text=)`: a kernel written
  in the operator's own file, its recipe digest over the text; the
  hello-world `VectorAdd` (`tests/toolchain/inline_kernel.py`) lowers
  through the toolchain with its `vadd` compiled from the text. The four
  elementwise templates collapse with the merge (step 7's first rung),
  where an operator's operands say how many streams there are.
- `6aa37f2` Step 4: views and `Copy`. A graph handle takes numpy's
  basic indexing plus a per-call `Scratchpad` index on one axis, and
  `transpose`; a contiguous static region is a sub-buffer as before, any
  other view a `Walk` over the parent that `Copy` alone takes (its
  `accept_views`). `Copy(src, dst=None)` replaces `StridedCopy`'s eight
  fields with two walks; the per-call index binds `in_offset`/`out_offset`
  with the axis stride as its scale, applied where the host writes the
  value. States are viewed inside a graph function (a handle when tracing,
  a remembered key over the host tensor in the reference). llama: caches
  `(G, L, D)`, `Copy(k, keys[i][:, cache_offset])`, prefill through a
  transpose view, `Copy(x[last]).reshape(1, E)`; the host passes rows.
  Descriptors identical to the pinned ones; llama's reference tests pass;
  both suites identical to baseline. Reshapes in the llama graph: 13 → 11
  (the two `Repeat` reshapes wait on rank-3 operands).
- `51e807f` `Operator.copy()` re-records what `compatible()` writes
  (GEMV's rows per column, an `init=False` field a `replace()` resets):
  the toolchain run caught the core loop running zero times, which the
  device-free run cannot see, so the toolchain run is now a gate of every
  step. Step 4's first item: `tests/common/copy_taps.py` pins the exact
  descriptors StridedCopy issues for llama's three copies and the KV slot.
- `5d63876` Step 3b: the column knob defaults from the device on GEMV,
  Softmax and RoPE (`auto()`; the operator's `resolve` picks the most
  columns the shim budget allows that divide its extents; RMSNorm keeps one
  core per row; GEMM keeps its given eight, since its host buffers are
  padded by it). An operator's `name` is the resolved operator's, so the
  per-call value symbols a graph names at trace time and the kernel
  instances a build names agree. Every device test gives the knob, so
  nothing measured changes. Failure set identical to baseline.
- `4bb8f82` Step 3a: one resolution point. `Operator.resolve(dev)` is
  the hook that sees the device and the extents (`overlay_defaults` gone;
  StridedCopy's transfer size is its one override); `Overlay.resolve(dev)`
  (was `tuning`) sees the device and its own fields; `resolved(dev)` on
  both is idempotent and the only caller of `resolve`. The sequence
  resolves every operator in `prepare()`, before `unique_designs()` takes
  identity, so two descriptions of one array are one design (test added;
  ffn 6 designs / swiglu 4, as before). `for_extent`, `specialised` gone;
  `Untunable` → `Unresolvable`. Failure set identical to baseline.
- `da31c8b` Step 2a: `dim()`/`tunable()` → `param()`/`auto()`. `param`
  is a field specifier with keyword `default=`, so a missing required field
  is now a checker error too; `auto(choices=, legal=)` is accepted and
  recorded. Failure set identical to baseline.
- `e04956f` + `b9aaecb` ruff after mlir-aie's `ruff.toml` (D205/D401 off, for the codebase's
  sentence summaries); `pyrightconfig.json` after mlir-aie's; both scoped to
  all of `iron/common` and `iron/tests/common` (three tests wait on step 7),
  both clean with and without mlir-aie on the path. The ~95 findings fixed
  were narrowings of "None until prepared" state, `Transfers`' abstract
  surface, `ElementwiseOperator` typed over its own overlay, pyxrt behind
  `TYPE_CHECKING`, and one accessor (`jit_compile.cache_entry`) for "a
  compiled design has its entry". Upstream typing gaps worked around inline:
  `Device.resolve() -> None`, `region_op` decorators, `_aie.pyi` missing
  `get_target_model`, `_mlir/*.pyi` not installed by the build.
