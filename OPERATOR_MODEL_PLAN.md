<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Operator model: overlays, operators, and derived sequences

Design, agreed in a review of the 2026-09-20 draft. Supersedes the
`OPERATOR_MODEL_PLAN.md` on branch `operator-model-argspec` (PR 215). Nothing
here is built. §12 lists the spikes that gate the parts that need hardware.

The previous draft's diagnosis of today's tree stands and is not repeated:
every file and line it cites was checked and lands where it says. What changed
is the design built on top of that diagnosis. §1 is the summary of what moved
and why; the rest is the design as agreed.

---

## 1. What changed from the previous draft

| previous draft | now | why |
|---|---|---|
| one `interface()` method per operator, declaring host buffers | two classes: an **Overlay** declares what configures the array, an **Operator** declares the host buffers against it | the overlay depends on data movement *into* the array (tile shapes, columns, dtypes); the sequence depends on host extents. One declaration conflated them, so nothing could be reused by construction and everything had to be checked by comparison. flm/gemm already lives this split by hand |
| shapes are arbitrary Python over compile-time fields | a shape dimension is a **bare field or an integer**; a conditional may only test a field with a default | inference becomes a lookup instead of a solver. The draft's own examples (`size // tile_size`, `if b_col_maj`) needed the resolver it claimed to have dissolved |
| declaration in a method body, names recovered by a `__setattr__` hook | declaration **at class level**, names from the descriptor protocol, fields usable by bare name | once shapes are field references there is nothing left for a method body to do; the hook and its three guard checks go |
| `tuning()` on the operator, deriving overlay tunables from the extent (`tile_size_output = M // cols`) | `tuning(dev)` on the **overlay**, from the device only; `for_extent(...)` is the explicit opt-out | tuning from `M` makes the overlay depend on the extent, which defeats reuse. The operator author chooses reuse or per-shape performance, per call site |
| the design restates the ABI (`L3_*_ty`, `Runtime(seq, fn_args=[...])`) and E7 checks identity | the **library owns `Runtime` and `Program`**; a buffer names its stream (`to=`/`from_=`) and the fill/drain sequence is **derived**; `design(rt)` is an override for irregular operators | deletes the second spelling and the checks that policed it. Most sequence designs in the tree are "tile this buffer over that stream across the columns" |
| three runtime tiers named by what rebuilds (`HostResident`, `SequenceResident`, a plain field) | two author-named markers, **`Scratchpad`** and upstream's **`DispatchTime`** | the third tier is a plain field and needs no name; reusing upstream's name avoids two vocabularies for one mechanism |
| four packaging constructors (`Overlay`, `StaticSequence`/`GeneratedSequence`, `Elf`/`Xclbin`) | **`compile(dev, boundaries=, image=)`**, everything else derived from the declaration and reported | with author-named markers the sequence kind is already declared, and the image follows from device, boundaries and markers. Only boundaries and an image override were ever the user's to choose |
| `Overlay` ABI (bindings, residents, sizes) read back from files and compared (E23) | agreement **by construction** for overlays IRON builds; read-back kept only for a foreign xclbin (`Overlay.from_xclbin`) | the sequence is built from the overlay's typed stream declarations, so there is nothing to compare except divisibility |
| llama four ways as the acceptance gate | **one configuration at parity**, NPU1 fallback contingent on a spike, the rest measured as experiments | the four-way matrix multiplied hardware test time for configurations two spikes may rule out |
| 31 enforcement rows | the checks that trace to an observed failure or to a mechanism this design introduces (§10) | six of the 31 guarded the hook this design removes; the coverage rows guarded hand-written sequences this design derives |
| a recorder: `g.input(shape)`, `g.param`, `g.state`, `g(Op, ...)`, outputs read by handle | a **graph function**: inputs are parameters, outputs are return values, weights are closed-over tensors, state is a closed-over `iron.state`; several graphs compile together as a **module** sharing one buffer plan | declaring inputs by shape and reading outputs by handle predates tracing; the function form is also upstream's `@iron.jit` convention, so IRON stops diverging from it |

---

## 2. Goals

Kept from the previous draft, in its numbering: 1 general purpose, 2 no string
names, 3 library quality, 4 prefill in scope, 5 per-operator tuning easy to
override, 6 tuning may fail, 7 minimal duplicated spec logic, 8 static and
build-time checking, 9 un-flatten real 2-D shapes, 11 pyright config not
per-file, 12 `Tuning` is IRON-local.

Rewritten:

- **13 (nothing works by accident)** now has a stopping rule: a check exists
  because a failure was observed in this tree, or because a mechanism this
  design introduces would otherwise fail silently. Not because a mistake is
  imaginable.
- **14 (overlay and sequence are separable)** is now the *structure* of the
  operator model (§3), not a packaging option.
- **15 (types not strings; primitives not strategies)** is narrowed back to
  priority 2. A validated enum never caused a bug here; strings for buffers did.
- **10 (coverage checks on every build)** is retired. A derived sequence covers
  its buffers by construction; an overridden one gets the checks in §10.

Added:

- **Performance is measured, and does not regress.** Parity on the llama token
  stream is the gate; per-token latency is recorded before and after.
- **Build time has a budget.** Anything that runs on every build is measured
  against it.
- **One PR demonstrates the whole thing.** Upstream changes are prototyped in
  IRON by extension where possible (§11), so the PR runs end to end before
  anything lands upstream.
- **The operator author decides reuse versus performance.** The library makes
  reuse the default and specialisation explicit, and never chooses silently.

Dropped: designing now for CNNs. No CNN operator exists; the design does not
block one and does not shape itself around one.

---

## 3. The layering

An operator's fields sort by what a change rebuilds:

| tier | lives in | examples (GEMV) | changing it rebuilds |
|---|---|---|---|
| **overlay** | the `Overlay` class | `K` (baked into the kernel), `cols`, `tile_out`, `vec`, dtypes, fifo depths, shim pins | cores, routing, PDI |
| **sequence** | the `Operator` class | `M`, `num_batches`, offsets, strides | the instruction stream only |
| **per-call** | a marker on the `Operator` | `n_rows`, `cache_offset` | nothing (`Scratchpad`) or the stream (`DispatchTime`) |

Each layer has an ABI. The overlay's is the **streams** that enter and leave
the array, in tile units, with their shim bindings. The operator's is the
**host buffers**, in extents, each naming the stream it feeds or drains. A
sequence is written against the overlay's stream declarations, so direction,
dtype, tile shape and shim binding agree by construction. The only thing left
to check is divisibility (`compatible()`, §5).

Upstream's own seam already matches this: `Program(dev, rt)` takes workers and
fifos on one side and a `Runtime` on the other. Today every IRON design builds
both in one function.

### The discipline that makes reuse real

A core program must not bake a host extent into its loop trip count, or the
overlay silently depends on `M`. **A core's trip count is either unbounded or
supplied by the sequence through a resident parameter, never a compile-time
constant derived from a host extent.** Both patterns exist in the tree: gemv
and mha loop forever; gemm, mha and flm/gemm read their counts from runtime
parameters the sequence writes before the first DMA. Every other design today
computes its count from `size` or `M` at compile time, so the migration in
§14 rewrites each of those loops. This is checkable: **build the overlay at
two extents and require the core ELFs to be byte-identical** (the trick from
the flm/gemm migration commit). It runs once per overlay class in the test
suite, not on every build.

### What it buys

flm/gemm's one-xclbin-many-shapes, for every operator. In the fused llama
graph the q, k, v and o projections are GEMVs at different `M`; today each is
a separate design, under this design they are one overlay and four sequences.
Whether the current fusion pass skips a reconfiguration when consecutive steps
share a device is **unverified** (O5) and is not counted until it is.

---

## 4. Declaring an overlay

```python
@operator
class GEMVOverlay(Overlay):
    """Array configuration for C = A @ B. Row-blocks of A per column, B broadcast."""

    K: int = dim()                       # baked into the kernel: -DDIM_K
    cols: int = tunable(None)               # None: tuning fills it from the device
    tile_out: int = tunable(64)             # rows of C one core produces per acquire
    vec: int = tunable(None)                # kernel vector width

    a = StreamIn(tile_out, K, per_column=True)
    b = StreamIn(K, broadcast=True)
    c = StreamOut(tile_out, per_column=True)

    def tuning(self, dev) -> "GEMVOverlay":
        cols = self.cols or dev.columns()
        vec = self.vec or next((w for w in (64, 32, 16) if self.K % w == 0 and self.K >= 2 * w), None)
        if vec is None:
            raise Untunable(f"K={self.K}: no vector width in (64, 32, 16) divides it")
        return replace(self, cols=cols, vec=vec)

    def design(self, dev):
        matvec = declare_kernel(
            f"matvec_{self.vec}", [np.int32, np.int32, self.a.tile, self.b.tile, self.c.tile],
            source=dev.kernels_dir / "generic" / "mv.cc",
            compile_flags=[f"-DDIM_K={self.K}", f"-DVEC_SIZE={self.vec}"],
        )
        of_b = ObjectFifo(self.b.tile, name="B")
        self.b.bind(of_b.prod())
        workers = []
        for col in range(self.cols):
            of_a = ObjectFifo(self.a.tile, name=f"A{col}")
            of_c = ObjectFifo(self.c.tile, name=f"C{col}")
            self.a[col].bind(of_a.prod())
            self.c[col].bind(of_c.cons())
            workers.append(Worker(_core, [of_a.cons(), of_b.cons(), of_c.prod(), matvec, self.K, self.tile_out]))
        return workers


def _core(of_a, of_b, of_c, matvec, K, tile_out):
    for _ in range_(sys.maxsize):            # forever: the sequence decides how much flows
        b = of_b.acquire(1)
        a = of_a.acquire(1)
        c = of_c.acquire(1)
        matvec(K, tile_out, a, b, c)
        of_c.release(1); of_a.release(1); of_b.release(1)
```

**`dim()` and `tunable()`** return dataclass field specifiers. Pyright sees
`K: int` as a required constructor argument and `cols: int` as optional. In the
class body the name `K` is bound to the specifier, so the stream declarations
below it use the bare name. After the class is built, `@operator` re-attaches
each field as a class attribute, so `GEMVOverlay.K` names the dimension from
outside and `ov.K` is the integer on an instance. A `tunable` is what the
previous draft called `Tuning[T]`: a field `tuning()` may set, and pyright
checks `replace()` against the real field list.

**Streams** are declared unannotated, so the dataclass machinery ignores them
and the descriptor supplies the type. `per_column=True` makes the stream a list
indexed by column; `broadcast=True` makes it one fifo with every core as a
consumer. A stream's shim binding is the placer's unless pinned with `via=`
(§9). Direction is not spelled: `StreamIn` is a shim producer, `StreamOut` a
shim consumer.

**`tuning(dev)`** sees the device and nothing else, so a tuned overlay serves
every extent. `Untunable` is an expected outcome. An author who wants today's
one-configuration-per-shape behaviour asks for it at the call site:

```python
ov = GEMVOverlay(K=2048).tuned(dev)                        # reusable across every M
ov = GEMVOverlay(K=2048).tuned(dev).for_extent(M=1024)     # specialised, explicit
```

`for_extent` produces a distinct overlay. The graph builder warns when a
specialisation stops two operators sharing one, so per-extent overlays never
multiply silently.

**`design(dev)`** builds the array and binds each declared stream to the shim
end of a fifo. It returns the workers. It never constructs `Runtime` or
`Program`; the library does (§5). An overlay built by someone else has no
`design()` and is declared with `Overlay.from_xclbin` (§9).

**Sharing** keys off `design_key()`, which already exists, not off dataclass
hashing. Two overlays with equal keys are one build.

---

## 5. Declaring an operator

```python
@operator
class GEMV(Operator[GEMVOverlay]):
    """C = A @ B, optionally batched."""

    M: int = dim()
    num_batches: int = dim(1)

    A = In(num_batches, M, GEMVOverlay.K, to=GEMVOverlay.a)
    B = In(num_batches, GEMVOverlay.K,    to=GEMVOverlay.b)
    C = Out(num_batches, M,               from_=GEMVOverlay.c)

    def compatible(self):
        unit = self.ov.cols * self.ov.tile_out
        if self.M % unit:
            raise Incompatible(f"M={self.M} is not a multiple of the {unit} rows the overlay drains per pass")

    def reference(self, A, B):
        return A @ B
```

That is the whole operator. Each dimension is written once as a field and once
per shape it appears in; that is the floor for a pyright-checked constructor,
and it was chosen over a one-mention form (`In("num_batches", "M", "K")`)
because that form needs strings and, as the previous draft measured, makes
pyright reject valid constructor calls.

**The sequence is derived** from `to=` and `from_=`. A's `M` axis is split
across the overlay's columns and fed in `tile_out`-row tiles, B is filled once
per batch, C is drained per column. Splitting a run that exceeds the BD wrap
limit is the library's job, once, instead of GEMV's, repeat's and mha's.

The derived sequence has a fixed shape: a **preamble** that writes every
resident parameter the overlay declares (trip counts, RTPs) and sets the
worker barriers; then every fill; then every drain, each waited. Two fill
options cover what the regular operators need beyond plain tiling: a
**broadcast** fill to a per-channel fifo (weighted rms_norm's weight), and a
**repeated** re-read of a buffer through a stride-zero outer dimension
(repeat, gemv's B, flm/gemm's B).

Surveyed against every design on the PR 215 branch: **14 operators are
derivable** as they stand (relu, gelu, silu, sigmoid, tanh, layer_norm,
elementwise_add, elementwise_mul, axpy, leaky_relu, dequant, rms_norm both
designs, rope) plus softmax once the preamble exists; **eight need
`design(rt)`** (strided_copy, transpose, mem_copy, gemv, gemm, mha, flm/gemm,
mm_prebuilt); repeat is borderline and is treated as an override; the two
swiglu composites become graph functions (§8). The eight are mostly about
TaskGroup and wait structure (an outer group held across batches, one wait
per batch, queue-depth retirement, drain issued before fill) and the tiler
does not learn any of that.

**An operator overrides `design(rt)`** when the derivation cannot express its
pattern. This is what the derived one is equivalent to:

```python
    def design(self, rt):
        rows = self.M // self.ov.cols
        rt.fill(self.ov.b, self.B)
        for col in range(self.ov.cols):
            rt.fill(self.ov.a[col], self.A[:, col * rows:(col + 1) * rows, :])
            rt.drain(self.ov.c[col], self.C[:, col * rows:(col + 1) * rows], wait=True)
```

Slicing a declared buffer yields the access pattern; there is no
`TensorAccessPattern` to hand-build for the regular cases. `rt` is opened by
the library from the buffer members in declaration order, so `fn_args` and
`rt.sequence(...)` are not written, and the preamble above runs before the
override's body.

**`compatible()`** is the only cross-layer check an author writes, and it is
where the overlay's tile granularity meets the operator's extent. The library
calls it when the operator is bound to a tuned overlay.

**`reference()`** takes the `In` members in declaration order and is the only
oracle for the math.

**`InOut`** exists for in-place operators (RoPE, residual add), matching
upstream's marker.

---

## 6. Per-call values

Two markers, author-named, declared in the class body beside the buffers:

```python
@operator
class StridedCopy(Operator[CopyOverlay]):
    n: int = dim()
    src = In(n, to=CopyOverlay.s)
    dst = Out(MAX, from_=CopyOverlay.d)

    dst_offset = Scratchpad(np.int32)        # patched into the BD; free per call; works under full ELF
    n_live     = DispatchTime(np.int32)      # regenerates the stream per call; xclbin only

    def design(self, rt):
        rt.fill(self.ov.s, self.src[:self.n_live])
        rt.drain(self.ov.d, self.dst[self.dst_offset:], wait=True)
```

| marker | can | cannot | cost per call | packaging |
|---|---|---|---|---|
| `Scratchpad(T)` | move a DMA base address; be read by a core | change a size or stride | a few words plus a sync | any |
| `DispatchTime(T)` | change sizes, strides, offsets | be read by a core on its own | stream regeneration plus a buffer allocation | xclbin only |

Misuse is a build error naming the marker. A `Scratchpad` used at a size
position, or a `DispatchTime` member in a sequence packaged as a full ELF,
each says which member, what it does, and the two ways out.

**A value belongs to the operator instance, and reuse means sharing.** A
`Scratchpad` is one device symbol per design; the strided copy llama reuses
across 32 layers has one, written once per token. Binding one handle at many
call sites is explicit sharing. Binding different handles to one instance is
an error.

**Shapes never reference a per-call value**, a `tunable`, or anything but a
`dim()` or an integer. A per-dispatch extent is a `DispatchTime` member next
to a buffer declared at its maximum:

```python
    max_rows: int = dim()
    x = In(max_rows, tile, to=...)
    n_rows = DispatchTime(np.int32)         # how much of x is live on this call
```

The bound `n_rows <= max_rows` is enforced on the handle at write time.
Scratchpad values are limited to 30 bits and `float32` is unsupported; the
marker says so.

### Lowering on a path without a scratchpad

On NPU1 the packaging is per-step xclbin (§8). Whether an xclbin dispatch has
a control scratchpad at all is **unverified** (spike S2). If it does not, the
library lowers as follows and reports it:

```
llama decode, npu1, per-step xclbin:
  StridedCopy.cache_offset: scratchpad unavailable on this path; lowered as DispatchTime
      (stream regenerated per call)
  Softmax.vector_size: scratchpad unavailable and the core reads it; no lowering exists.
      Make it a compile-time field or package for NPU2.
```

The first is automatic because an offset-only use is provably equivalent and
each step is one design with one sequence and no PDI load, which is the shape
the dispatch bridge accepts today. The second is an error because nothing
equivalent exists, unless the sequence can write a dispatch value into tile
memory with a register write, which is **unverified** (spike S3).

---

## 7. The shape rule, and inference

**A shape dimension is a `dim()` field or an integer literal.** A conditional
may only test a field that has a default or is passed explicitly, never one
being inferred. GEMM's layout flags are the only conditional in the tree:

```python
    B = In.select(b_col_maj, (N, K), (K, N), to=GEMMOverlay.b)
```

An operator whose host shape is genuinely an expression of its fields
re-expresses itself with the expression's result as the field. RMSNorm's
`(size // tile_size, tile_size)` becomes `rows: int = dim()` with `size`
derived. That is priority 9's un-flattening, and it is a constructor change
for every such operator, listed in §14.

**Inference is a lookup.** `GEMV(wk, x)` in a graph walks each `In`'s dimensions,
pairs position with operand dimension, binds the field or checks the literal,
and raises on conflict naming both operands. Overlay-tier fields (`K`) and
sequence-tier fields (`M`) are inferred the same way; the builder constructs
the overlay, deduplicates it by `design_key()`, tunes it once, then constructs
the operator against it. Tunable overrides in inferred form are passed through:
`GEMV(wk, x, cols=2)`.

```python
ov = GEMVOverlay(K=2048)                   # explicit
q  = GEMV(ov, M=2048)
kv = GEMV(ov, M=512)                       # same overlay, different extent

@iron.graph
def step(x):
    hq = q(wq, x)                          # explicit instance
    hk = GEMV(wk, x)                       # inferred; overlay deduplicated with ov
    return hq, hk
```

Because a bare field name in a shape is already the symbolic form, there is no probe run.
"This dimension names a tunable or a per-call value" is checked once at class
creation.

---

## 8. Graphs, modules, and packaging

### A graph is a function

Inputs are its parameters, outputs are its return values, constants are what
it closes over, and tracing supplies the shapes. This is upstream's
`@iron.jit` convention, tensors positional and per-call scalars keyword-only.

```python
kv = [iron.state((cfg.n_kv_groups, MAX, cfg.head_dim)) for _ in range(cfg.n_layers)]

@iron.graph
def decode(x, angles, *, pos: Scratchpad[np.int32]):
    for i, blk in enumerate(model.layers):
        h = RMSNorm(x, blk.norm1.weight)                  # a bare tensor is a weight
        q = RoPE(GEMV(blk.attn.q.weight, h), angles)      # RoPE is InOut: q is h's buffer
        k = RoPE(GEMV(blk.attn.k.weight, h), angles)
        StridedCopy(k, kv[i], dst_offset=pos)             # writes state; returns nothing
        scores = [Softmax(GEMV(kv[i][g], q[g])) for g in range(cfg.n_kv_groups)]
        ...
        x = ElementwiseAdd(x, o)
    return GEMV(model.out_head.weight, RMSNorm(x, model.norm.weight))

net = decode.compile(dev, x=(1, cfg.emb_dim), angles=(1, cfg.head_dim))
logits = net(x_tok, angles_tok, pos=n * cfg.head_dim)
```

| role | spelling |
|---|---|
| input | a positional parameter |
| output | a return value; a tuple for several; returned as device tensors with `.numpy()` |
| weight | any tensor the function closes over; identity is the tensor, uploaded once |
| state | an `iron.state(...)` created outside and closed over; persists on the device |
| per-call scalar | a keyword-only parameter with a marker, bound to an operator's `Scratchpad` or `DispatchTime` member; one handle at many call sites is sharing (§6) |
| intermediate | a local; pooled by live range |
| slice | indexing a handle; static slices are views, a per-call offset is the operator's marker |
| in-place | invisible; an `InOut` operator returns the handle it was given |

**Operators are called on handles.** `GEMV(w, h)` infers the overlay and the
extent from its arguments (§7); an explicit instance is `GEMV(ov, M=2048)` and
is then called the same way. The class tells the two apart by whether it
received handles. That overloading is the one wart in this form, and torch
lives with the same one between `nn.Linear` and `F.linear` (O9).

**Names come from the model if one is offered**, and only for diagnostics
and the upload log: `iron.graph(names_from=model)` maps parameter identity to
its `named_parameters()` name. A tensor that is not a registered parameter
(a RoPE table, a packed weight) is still a weight; it is named by where it
was used.

**Composites are graph functions.** swiglu_prefill and swiglu_decode are
today `OperatorSequence`s of children; they become functions that call GEMM,
SiLU and ElementwiseMul, and `CompositeOperator` goes.

**Shapes come from `compile()` or from the first call.** `compile(dev, ...)`
with shapes is the documented path. Calling an uncompiled graph with real
tensors compiles for those shapes, says so once, and dispatches. A new input
shape on a compiled graph is an error, not a recompile.

**`reference`** is the same function traced against each operator's
`reference()`; `compare` runs both with a boundary after every step.

### A module is several graphs over one buffer plan

llama has prefill and decode, and today they are unrelated: prefill runs
per-operator xclbins on its own tensors in its own weight layout, decode runs
a fused ELF with the weights uploaded into its arena. Weights are uploaded
twice, in two layouts, and the KV cache is threaded by hand. Two graph
functions that close over the same tensors and the same state objects compile
together as a **module**: one allocation for weights, state and intermediates
across both, weights uploaded once, state shared because it is the same
bytes, one image with one entry point per graph.

```python
llama = iron.compile(dev, prefill=prefill, decode=decode,
                     prefill=dict(tokens=(MAX, cfg.emb_dim), angles=(MAX, cfg.head_dim)),
                     decode=dict(x=(1, cfg.emb_dim), angles=(1, cfg.head_dim)))
llama.prefill(tok, ang, n=len(prompt))
logits = llama.decode(x, ang, pos=p)
```

Under **xclbin** a module is what `SeparateDispatch` already builds: one
chained image, one kernel per entry point, one hardware context because the
runtime keys contexts on the xclbin path. User tensors are allocated against
the device with a fixed memory group, not against a kernel, so a weight
uploaded once is a valid argument to both kernels. Nothing new is needed.

Under **full ELF** a module needs one ELF carrying two runtime sequences.
The kernel naming convention (`<device>:<sequence>`) suggests it was designed
for, but nothing in IRON or upstream's Python does it (**spike S4**). If it
cannot, the fallback is one ELF per graph with an upload per graph, which is
today's behaviour made explicit; sharing device buffers across two hardware
contexts is consistent with how IRON allocates them but is unexercised.

### The image is chosen per module

One buffer plan means one image, so the rules below apply to the whole
module, not to each graph. For llama that decides the shape of the two
targets:

- **NPU2: an ELF module.** prefill pads its length to a compile-time maximum
  and masks, as softmax already does for its vector size, so no `DispatchTime`
  member forces the module to xclbin. decode keeps `Scratchpad` on the path
  where it is known to work. One ELF with two sequences if S4 passes, two ELFs
  otherwise.
- **NPU1: an xclbin module**, built from the same source. Per-step kernels,
  `cache_offset` lowered per §6 unless S2 passes, prefill's length as a
  `DispatchTime` value if it wants one. The same build is the S1 experiment
  on NPU2, where a fused decode kernel in an xclbin has never been run.

### Boundaries and image override

Two arguments, both optional. Everything else is derived and printed under
`verbose`.

```python
net = decode.compile(dev)                                  # full ELF on NPU2, per-step xclbin on NPU1
net = decode.compile(dev, image=Xclbin)                    # one fused sequence in an xclbin (spike S1)
net = decode.compile(dev, boundaries=chunks(8))            # four dispatches of eight layers
net = decode.compile(dev, boundaries=each_step)            # today's "separate"
```

| rule | consequence |
|---|---|
| a `DispatchTime` member anywhere in the module | that graph's sequence is generated per call; the image is `Xclbin` |
| the device is NPU1 | `Xclbin`; NPU1 has no full-ELF dispatch |
| more than one boundary in any graph | `Xclbin`; one image, N kernels, one shared hardware context |
| otherwise | `Elf` |
| a sequence spans more than one device configuration | its PDI loads are expanded inline (`--expand-load-pdis`); a multi-configuration sequence cannot run otherwise |

Asking for `image=Elf` when a rule forbids it is an error that names the
member, the graph, or the device.

**Overlays are compiled once per module** and shared by every sequence that
declares against them. Today `aiecc` emits both halves from one invocation, so
sharing saves reconfigurations and hardware contexts but not compile time. An
instructions-only compile exists in `aiecc` (the instruction branch roots on
the placed-and-routed module) and is exposed to IRON as described in §11; it
does not apply to a sequence whose PDI loads are expanded inline, since that
flag forces per-core compilation back on. So compile-time reuse is real for
per-step and chunked builds and not for a single fused sequence.

**A sequence is not image-agnostic.** Full-ELF instruction streams are emitted
with DDR address folding forced off; xclbin streams fold. The library compiles
the sequence for the image it will live in, and never moves one between them.

---

## 9. The three operators that do not declare a shape function today

**flm/gemm fits.** Its dtype depends on the bfp16 packing, which is an overlay
tunable, and a buffer's dtype can reference a field the same way a dimension
does. Its config-versus-shape split is what §3 was modelled on:

```python
@operator
class FLMGEMMOverlay(Overlay):
    K: int = dim()
    N: int = dim()
    b_format: str = tunable("bfp16ebs8")

    a = StreamIn(64, K)
    b = StreamIn(K, 64, dtype=b_format)
    c = StreamOut(64, 64)


@operator
class FLMGEMM(Operator[FLMGEMMOverlay]):
    M: int = dim()
    A = In(M, FLMGEMMOverlay.K, to=FLMGEMMOverlay.a)
    B = In(FLMGEMMOverlay.K, FLMGEMMOverlay.N, dtype=FLMGEMMOverlay.b_format, to=FLMGEMMOverlay.b)
    C = Out(M, FLMGEMMOverlay.N, from_=FLMGEMMOverlay.c)
```

**mm_prebuilt fits, and is why `Overlay` has a second constructor.** Its array
is downloaded, so it has no `design()`. Its streams carry the shim pins that
today are hand-matched in comments, and its runtime parameters are resident
symbols:

```python
@operator
class MMPrebuiltOverlay(Overlay, source=Xclbin.download(URL)):
    a = StreamIn(128, 128, per_row=True,    via=[Shim(col=2 * r, channel=0) for r in range(4)])
    b = StreamIn(128, 128, per_column=True, via=[Shim(col=c, channel=1) for c in range(8)])
    c = StreamOut(128, 128, per_column=True, via=[Shim(col=c, channel=0) for c in range(8)])
    rtp = Resident(np.int32, address=4096, lock=10)
```

This is the one case that keeps the previous draft's post-compile read-back:
an overlay IRON did not build gets its declared bindings checked against
`input_with_addresses.mlir`, and a sequence declared against it that cannot
drive it gets a message naming the binding. That is the flm/gemm-against-
mm_prebuilt mismatch that is currently a comment.

`via=` pins a shim column and channel. `channel` is validated against the
two-per-direction limit from the target model at class creation; nothing
validates it today at any layer. Pinning constrains routing for everything
else, so it is a tool for foreign overlays and not a default.

**swiglu_prefill_stream does not fit.** Its shapes come from a graph that
stream-dse exports at build time. It gets a dynamic escape, private to the
stream package: `Operator.from_spec(...)` builds the members from the exported
description at class-creation time, and gives up pyright for that one
operator, which already skips its tests when stream-dse is absent.

---

## 10. Checks

Each row names the failure or mechanism that justifies it. **T1** pyright,
**T2** class creation, **T3** tune/bind, **T4** build, **T5** hardware.

| id | mistake | when | because |
|---|---|---|---|
| C1 | wrong type, missing argument, bogus kwarg at construction | T1 | real dataclass fields; the most valuable static check the previous draft measured |
| C2 | `tuning()` sets a field that is not a `tunable` | T1 | `replace()` against the real field list |
| C3 | a shape dimension is a `tunable`, a per-call value, or an expression | T2 | the shape rule (§7); the pipeline would cycle |
| C4 | a member declared with an annotation | T2 | it would become a constructor argument |
| C5 | a `Scratchpad` used at a size position; a `DispatchTime` read by a core | T4 | the hardware rule in §6 |
| C6 | a `DispatchTime` member in a full-ELF sequence | T4 | no instruction-buffer argument to swap; upstream raises the same |
| C7 | `via=Shim(channel=2)` | T2 | two per direction per shim tile; unvalidated today |
| C8 | more shim endpoints than the device has | T3 | `get_shim_dma_limit` exists; extend to the graph |
| C9 | no legal tuning for this `K` on this device | T3 | `Untunable`; the mem_copy 16-core hang compiled fine |
| C10 | extent not a multiple of the overlay's tile unit | T3 | `compatible()` |
| C11 | an overlay's core ELFs differ between two extents | test suite | the reuse discipline (§3), byte-identity; fails today for every design with a compile-time trip count |
| C12 | a foreign overlay's declared bindings disagree with its file | T4 | the mm_prebuilt case (§9) |
| C13 | a declared buffer never filled or drained in an overridden `design(rt)` | T4 | the derived sequence cannot make this mistake; an override can |
| C14 | DMA addresses past the end of a buffer in an overridden `design(rt)` | T4 | bounds from the slice, cheap; the coverage checks beyond this are opt-in test utilities |
| C15 | a `Scratchpad` never written before dispatch | T5 | sync-time check on the handle |
| C16 | one instance bound to two per-call handles | graph build | one symbol per design (§6) |
| C17 | `n_rows > max_rows` | write time | the bound is declared beside the buffer |
| C18 | the kernel computes the wrong thing | T5 | `reference()`; the only oracle |
| C19 | `image=Elf` requested for a module a rule forbids | compile | names the `DispatchTime` member, the graph with several boundaries, or the device |
| C20 | a compiled graph called with a new input shape | call | no silent recompile; the message names the parameter and both shapes |

Retired from the previous draft: E1, E2, E6, E14 (guarded the `__setattr__`
hook), E3, E7, E15 (guarded the design's restatement of the ABI), E16–E20 as
every-build checks (the derived sequence covers by construction; kept as test
utilities for overrides), E23 as a general check (agreement by construction;
kept for foreign overlays as C12), E25, E27, E28 (packaging choices the user
no longer makes).

Access *order* is still not checkable without a test: coverage can be
complete while the permutation is wrong.

---

## 11. Upstream dependencies, prototyped in IRON

Three upstream changes are needed. Each is prototyped in IRON by extension so
the PR runs end to end, and filed upstream as its own change.

| need | upstream state | IRON prototype |
|---|---|---|
| **instructions-only compile** against an already-built overlay | `aiecc --get-npu-insts [--sequence-name=]` already skips per-core compilation; `CompilableDesign.compile()` refuses an insts-only call | call `compile_mlir_module(insts_path=...)` directly, bypassing the guard |
| **dispatch bridge on a fused graph** | `aie-materialize-runtime-sequences` inlines callee sequences but does not erase them, so any fused graph leaves more than one `aie.runtime_sequence` in `npu_lowered.mlir` and the bridge's check rejects it; `aiecc` itself prunes non-selected sequences on its own C++ edge | prune the callee sequences from the lowered module before the check reads it |
| **scratchpad on the xclbin path** | `ParameterScratchpad` reads a run handle's control-scratchpad buffer, wired only to the full-ELF flow | **spike S2** first; if the buffer exists on an xclbin run, wrap it in IRON; if not, the lowering rule in §6 applies and no prototype is possible |

Also upstream: a builder for `aiex.configure`/`aiex.run` (IRON emits them by
rewriting MLIR text today), and multiple runtime sequences per device
(upstream hardcodes one device `main` with one sequence `sequence`). The
second is what an ELF module with two entry points needs (S4); until it
exists, IRON emits the second sequence by the same text rewriting the fusion
pass already does. Neither blocks the decode-only PR.

---

## 12. Spikes, before any model code

| id | question | how | if no |
|---|---|---|---|
| **S1** | does one fused, multi-configuration sequence dispatch correctly from an xclbin via the opcode-3 path, with PDI loads expanded inline? | two-operator fused graph, `full_elf=False`, `--expand-load-pdis --get-xclbin --get-npu-insts`; it runs or it hangs | `image=Xclbin` with one boundary has no legal construction; NPU1 is per-step only; `chunks(n)` still works (each chunk is its own kernel) |
| **S2** | does an xclbin dispatch have a control scratchpad? | XRT run handle on an xclbin kernel; try `get_ctrl_scratchpad_bo()` | §6's lowering rule; `Scratchpad` is full-ELF only; softmax's `vector_size` needs S3 or a compile-time field on NPU1 |
| **S3** | can a `DispatchTime` value be written into tile memory by the sequence? | one design with a register write whose value is a dispatch parameter; read it back from the core | core-read per-call values are `Scratchpad` only |
| **S4** | can one full ELF carry two runtime sequences, dispatched by name? | a device with two `aie.runtime_sequence` ops through `--get-full-elf`; load and run each | an ELF module is one ELF per graph with an upload per graph (§8) |

An afternoon each. S1 needs the device; S2 and S3 need a device and no design
work; S4 needs only `aiecc`. None of §4–§7 depends on any of them, and S4
matters only once prefill joins the module.

---

## 13. Acceptance

The PR is done when:

1. **Every operator is on the new declaration.** All 22, including the three
   in §9. `arg_spec`, `bind()`, the snapshot, the `*_parameter="..."` kwargs
   and the dispatch hierarchy are deleted, not left beside their replacements.
2. **llama decode is rewritten as a graph function** and runs fully fused
   on NPU2 as an ELF module of one graph, with the **same token stream** as
   the snapshot taken before the rewrite, and per-token latency within noise
   of today's, measured interleaved over at least eight rounds. Prefill stays
   as it is today and feeds the same state objects.
3. **NPU1 per-step xclbin runs llama decode**, contingent on S2 or on the §6
   lowering rule plus S3 for softmax. If neither route exists for softmax, the
   PR says so and NPU1 llama is a follow-up.
4. **`iron/tests` and `iron/operators` baselines hold** (745 / 13 skipped and
   3165 with the five known mem_copy timeouts, on the PR 215 branch).
5. **`chunks(n)` works** on the llama graph, since it costs nothing extra to
   express and is the case the packaging layer exists for.

Measured as experiments, not gates: `image=Xclbin` with one boundary (S1),
per-token latency across boundary choices, and the host-side regeneration cost
of a `DispatchTime` step against a `Scratchpad` write.

Prefill stays out. Its ~300 lines are missing operators, not authoring, and no
declaration scheme fixes that. It is the next plan, and it is where the
module (§8) and S4 become load-bearing.

---

## 14. Sequencing

| step | what | needs |
|---|---|---|
| 0 | spikes S1–S3 | device |
| 1 | `Overlay`, `Operator`, `dim`/`tunable`, streams, `In`/`Out`/`InOut`, `Scratchpad`/`DispatchTime`, `@operator`, the tiler, library-owned `Runtime`/`Program`; GEMV alone, byte-identical object to today's | — |
| 2 | the derivable operators: the two elementwise bases (eight operators), axpy, leaky_relu, dequant, rms_norm, rope, softmax; each finite core loop rewritten to read its count from a resident (§3) | 1 |
| 3 | the overrides: strided_copy, transpose, mem_copy, repeat, gemm, mha, flm/gemm, mm_prebuilt (`from_xclbin`), swiglu_prefill_stream (`from_spec`); the two swiglu composites as graph functions | 1, 6 |
| 4 | delete `arg_spec`, `bind()`, the snapshot test, `L3_*_ty`, `*_parameter=` | 2, 3 |
| 5 | packaging: `compile(dev, boundaries=, image=)`, the derivation rules, modules, harnesses; delete the dispatch hierarchy; the §11 prototypes | 1, S1 |
| 6 | `@iron.graph`: tracing, handles, `iron.state`, weights by identity, inference, `chunks`; replaces the recorder | 1 |
| 7 | llama decode as a graph function; parity against the snapshot; NPU1 per S2/S3 | 4, 5, 6 |

Constructor changes forced by the shape rule, to list in the PR description:
RMSNorm (`size, tile_size` → `rows, tile_size`), and any other operator whose
arg_spec today computes a dimension rather than naming one (to be enumerated
in step 2).

---

## 15. What this deletes

From today's tree: `arg_spec` (14 shape functions), `bind()` and its 15
`bind_from=` sites, `arg_spec_snapshot.json` and its three tests, the `L3_*_ty`
restatements, `output_offset_parameter`/`vector_size_parameter` and their
string spellings in llama, `SequenceDispatch` and its five subclasses,
`_DISPATCH_ALIASES`, `full_elf_path()`, one of the two `infer_buffer_offsets`
implementations, `CompositeOperator` and the two swiglu `OperatorSequence`
composites, the recorder's `g.named()`/`g.slice()` string surface, and GEMV's,
repeat's and mha's private copies of the BD wrap split.

From the previous draft: `interface()`, the `__setattr__` hook and its replay,
the symbolic probe, `specialize()` on the operator, `HostResident`/
`SequenceResident`/`OverlayResident`, `StaticSequence`/`GeneratedSequence`,
`Elf`/`Xclbin` as user constructors, `Overlay.bindings/residents/sizes` as a
general mechanism, `via=` on host buffers, `Compare`/`Reference` as classes,
and E1–E3, E6, E7, E14–E20, E23, E25, E27, E28.

Kept throughout: `Untunable` and per-device numbers from the target model,
the un-flattening, `Tuning` (as `tunable`) IRON-local, the capture surface as the
authoring layer, and the decode-drift snapshot (§18).

---

## 16. Open questions

- **O1. Resolved.** Tiler scope is sized in §5: 14 derivable plus softmax,
  eight overrides, repeat treated as an override.
- **O2. Tunable overrides in inferred form.** `GEMV(wk, x, cols=2)` reaches the
  overlay; is that the spelling, or `GEMV.with_(cols=2)(wk, x)`?
- **O3. Resolved.** Upstream's tile placer and channel allocator both use
  stable sorts keyed on constraint level and channel demand, so **op order is
  the final tiebreak for shim tile and channel**, and op order is the
  fifo-name sort. A rename can move an unpinned shim endpoint. For overlays
  IRON builds this is reproducibility only, since the sequence binds to the
  fifo it got: the library names a per-column stream's fifos from declaration
  position and column, zero-padded, never from the attribute name. For
  foreign overlays every stream is pinned and pinned endpoints place first.
  A `per_column` stream does not guarantee column `c`'s shim is in physical
  column `c`; the placer picks by flow centroid and load. An author who needs
  a physical column pins it.
- **O4. Resolved.** Five library sites consumed arg_spec, all wanting
  direction, shape and dtype per buffer, which the declared members carry.
  Only `share_designs` consumed arg_spec *agreement*, and under the new model
  that check inverts: two operators sharing an overlay are expected to differ
  in extent, so the check is "same overlay key, and each `compatible()`
  passes."
- **O9. The class-call overloading.** `GEMV(w, h)` records a step and
  `GEMV(ov, M=2048)` constructs. Accepted as the default; the alternative is
  a lowercase functional namespace (`iron.ops.gemv`) beside the classes.
- **O10. State semantics.** How `iron.state` is reset, read back to the host,
  and sized when the module has two graphs writing it. Decided in step 6.
- **O11. Host work between boundaries.** `chunks(n)` returns control to the
  host between dispatches; whether a graph function can express host compute
  at a boundary, or whether that is two graphs in a module, is prefill's
  problem and is deferred with it.
- **O5. Reconfiguration skipping.** Whether the fusion pass skips a PDI load
  when consecutive steps share an overlay. If not, the shared-overlay win in §3
  is hardware contexts only until it does.
- **O6. `chunks(n)` placement.** A method on the build or a free function over
  the steps.
- **O7. Verbose report format.** What `compile(dev, verbose=True)` prints: the
  image, each sequence's kind and boundaries, each per-call value's lowering.
- **O8. The `MAX_WRAP` FIXME.** `iron/common/utils.py` already has
  `DMA_BD_MAX_WRAP` and a shared `split_run`, with a comment arguing the wrap
  is identical across every target model IRON builds for. The tiler uses the
  shared helper; the FIXME closes by deletion, not by `dev.max_wrap`.

---

## 17. Corrections to the previous draft's claims about upstream

For the record, so nobody re-derives them:

- `aie-materialize-runtime-sequences` **does not erase** inlined callee
  sequences; an upstream test asserts the callee device survives. The previous
  draft's spike 0b would fail on its first grep. This is why §11 prunes before
  the bridge's check.
- The instruction branch in `aiecc` roots on the placed-and-routed module, not
  on the module with compiled ELFs, so an instructions-only compile already
  exists in the toolchain. `--expand-load-pdis` forces it back onto compiled
  cores. The previous draft's L2 was near, and unavailable for exactly the
  mode it called load-bearing.
- `ParameterScratchpad` is wired only to the full-ELF dispatch flow. The
  previous draft's configs B, Ca and Cb could not carry `cache_offset` as
  written.
- Full-ELF instruction streams are emitted with DDR address folding forced
  off; xclbin streams fold. A sequence is not interchangeable between images.
- `requires_pdi_resources` is a local flag inside the bridge's check, not an
  attribute. `_check_runtime_sequence_abi` is a module function in
  `_dispatch_compile.py`, not a method. `split_params` and
  `_TensorPlaceholder` live in `_introspect.py` and `_serialization.py`.
- Upstream already has `specialize(**overrides)` meaning "bind a dispatch
  parameter"; the previous draft's `op.specialize(dev)` reused the name for a
  different operation.
- `InOut` exists upstream and was omitted.
- `schedule=` never existed in the tree; the previous draft was deleting it
  from its own earlier version.
- IRON never passes `dispatch_params` to anything; the previous draft's §11
  critique of `has_dispatch` describes upstream code.

---

## 19. Status

What is on this branch, and how far each piece has been verified. Three
environments are distinguished: **sandbox**, a session with no device,
where the pure-Python layers run under pytest against a stub of the
upstream module names; **lowering**, the same session with the pinned
mlir-aie wheel, Peano and `aiebu-asm` installed but no device, where
every design generates real MLIR, `aiecc` places, routes, assigns
addresses, lowers the DMAs and emits the instruction stream, the kernels
compile, and a traced graph builds to the fused ELF `xrt::module`
loads; and **device**, a machine with hardware, where nothing here has
run. How the toolchain was obtained without a device is worth a line,
since the index pages that name the assets are what a sandbox cannot
reach: the mlir-aie wheel and the Peano wheel are release assets whose
download URLs resolve directly (Peano's name and version are spelled out
in mlir-aie's `utils/update_peano_version.py`), `aiebu-asm` builds from
`Xilinx/aiebu` with its three submodules and Boost, and `xclbinutil` is
the Boost-free one mlir-aie vendors under `tools/hrx-xclbinutil`, built
standalone with one fix (below). No XRT is installed, so nothing loads.

### The lowering gate

`iron/tests/toolchain/lowering.py` lowers every case of the construction
table on npu2 and npu1 shapes (116 runs, 12 skipped as incompatible with
the narrow device), and `lowering_graph.py` lowers what the table does
not cover: every operator the decode graph traces, with its bound
per-call values as scratchpad parameters; flm/gemm's three sequence
shapes and its configuration-only module at the reference shape; the
foreign mm_prebuilt sequence (raw-dialect emission, no cores); and the
swiglu graphs' operators. All lower. The fused module `swiglu_decode`
builds through `OperatorSequence` (five devices: four configurations and
the dispatch sequence with `aiex.configure`) places and routes and emits
one instruction stream per device, the main one included.

### The full ELF

`iron/tests/toolchain/full_elf.py` goes the rest of the way on two
graphs, through the same path `CompiledGraph` takes
(`TracedGraph.sequence` → `OperatorSequence` → `compile_sequence`): the
kernels compile with Peano, every core links, each design's PDI is
generated, and `aiebu-asm` assembles the streams and PDIs into one ELF.
The swiglu decode graph builds in about 17 s (four PDIs, an empty
parameter table). The llama decode graph at the scaled test config (two
blocks, 50 steps, 6 bound values) builds in about a minute to a 6.3 MB
ELF whose scratchpad parameter table, emitted only on this path, has
exactly two rows:

| parameter | kind | written where |
|---|---|---|
| `StridedCopy_..._out_offset` | `addr` | patched into the sequence's descriptors |
| `Softmax_r16_n256_c1_ch1_npu2_vector_size` | `core` | read by the core behind its barrier |

Six bindings, two rows, and that is the sharing the graph intends: the
key and value copies of every block are one design, so one
`cache_offset` write reaches them all, and likewise the softmax's
vector size. The test asserts each bound value's symbol is in the table.

The same build at Llama 3.2 1B's real configuration (16 blocks, 386
steps, 48 bindings, 19 distinct designs) takes about three minutes and
produces a 13.3 MB ELF with the same two-row table. That is the image
`llama_npu.py` would load; only the load and the token snapshot are
left.

### The xclbin gate

`iron/tests/toolchain/xclbin.py` builds the other image, one xclbin per
design, on each path that lowers that way: a graph's separate dispatch
on npu2 and npu1 (the swiglu decode graph: five steps, four designs,
the gate and up projections sharing one kernel instance and one
instruction stream), flm/gemm's two compiles (the configuration's xclbin
at the reference shape plus this shape's instructions), mm_prebuilt's
instruction stream against its foreign overlay (and the download of the
image itself, which this session's network allowed), and a plain
operator's `compile()` on npu1. All pass.

Two things were wrong on the way. `SeparateDispatch.link_xclbins`
linked one xclbin per operator instance where the fused path built one
per design, so a graph with shared designs paid a chained compile per
step; it now iterates `unique_designs()` and maps every operator onto
its design's artifacts. And the vendored `xclbinutil` could not link a
chain at all: its property-tree shim split an empty path into one empty
key, so the `put("", v)` every section uses for array elements dumped
each element one level too deep (`"start_columns": [["0"]]`), and
aiecc's `--xclbin-input` step, which re-adds the dumped partition,
failed on the empty value. The fix (an empty path names the node
itself, as in boost) and a round-trip step for the tool's smoke test
are in `iron/tests/toolchain/patches/hrx-xclbinutil-empty-path.patch`,
against mlir-aie's `third_party/hrx-xclbinutil`; the smoke test fails
without it and passes with it. It belongs upstream.

The GEMV object gate is satisfied by construction: no kernel source
differs from the PR 215 tree and GEMV's MLIR is byte-identical, so the
same aiecc run produces the same object.

The device-free suites were also run against the real package instead of
the stub. `iron/tests/common` passes, with the design probe skipping
itself (its fakes would have to stand in for a runtime the package
refuses to enter outside a placed program, and the lowering gate runs the
same cases for real). In `iron/tests/infrastructure`, `lazy_imports.py`
needed its notion of a composite updated (a graph function's factory,
not an `OperatorSequence` subclass) and passes; what fails there fails
for want of hardware: `sequence.py` and `graph_dispatch.py` need
`pyxrt` and a bound device, and one test in `jit_compile_path.py`
asserts that binding the device inside the cache stamp reproduces the
hash a bound compile computes, which needs a device to bind (the rest
of that file, the xclbin and ELF compiles included, passes). Those are
the on-device list below.

Against the PR 215 tree, generated MLIR for the same constructions:

| operators | result |
|---|---|
| GEMV (plain and batched), GEMM (all four cases), MemCopy, StridedCopy (all three) | **byte-identical** |
| the elementwise families (ReLU, GELU, SiLU, Sigmoid, Tanh, LayerNorm, LeakyReLU, AXPY, ElementwiseAdd/Mul), Dequant, Transpose, Softmax | differ only by the resident count read behind a barrier (a buffer, a lock, `rtp_write` + `set_lock` in the sequence, `memref.load` in the core) and the SSA renumbering that follows |
| Repeat, RoPE | that, plus flat host argument types (`memref<512xbf16>` for `memref<8x64xbf16>`); descriptors identical |
| MHA | flat host argument types and linear Q/K/V/O descriptors (`[1,1,1,4096]` for `[1,1,64,64]`): same offsets, lengths and order |
| WeightedRMSNorm | no old counterpart with these keywords |

Three things were made identical along the way: residents are written
one buffer at a time in word order (the old sequences' order), GEMM's
parameter buffers keep their zero initializer, and leaky_relu's object
keeps its old name. Two case-table entries turned out to be invalid in
the old tree as well (a stride-1 transpose the hardware refuses, an f32
GEMM that overflows a core's memory) and are now valid configurations.

What the gate cannot check: the kernels (Peano), the numbers (hardware),
and the decode graph's parity against the token snapshot (§18).

| piece | file | sandbox | toolchain |
|---|---|---|---|
| declaration layer (§4–§7) | `iron/common/declare.py` | 34 tests: rules, binding, tuning, inference | — |
| access patterns and slicing (§5) | `iron/common/tiling.py` | 21 tests, reproducing today's unary, binary and GEMV taps; encoder follows the verifier's slot rules | — |
| library-owned build (§5, §6) | `iron/common/build.py` | 6 tests: derived order and patterns, override slicing, preamble | **needs a run**: Runtime/Program construction, resident writes, barrier sets |
| GEMV (§14 step 1) | `iron/operators/gemv/op.py` | classic construction, arg specs, tuning, compatibility, override transfers | **needs the gate**: byte-identical `matvec_vectorized_bf16_bf16.o` |
| unary and binary bases, ten operators (§14 step 2, part) | `iron/common/operator_bases.py`, ten `op.py` | classic construction, arg specs, resident counts, transfers per core | **needs a run**: resident-driven core loops are new code; C11 byte-identity now expected to pass |
| dequant, rms_norm (two pairs), rope, softmax (two overlays) (§14 step 2, rest) | four `op.py` | legacy spellings, arg specs, tuning, resident values, transfers per slot, rejections | **needs a run**; softmax's snapshot entry is now `rows x cols` and was re-pinned by hand |
| repeat, strided_copy, transpose, gemm (§14 step 3, part) | four `op.py` | construction, arg specs, tuning geometry, residents, transfers issued, rejections | **needs a run**; gemm's sequence body needs the real tiler |
| mha (§14 step 3, part) | `iron/operators/mha/op.py` | eight-pipeline sequence checked transfer by transfer (two shims, K/V per head, waited drains); inference from shapes | **needs a run**; Q/O descriptors are now linear runs rather than `(rows, d)` tiles, same bytes in the same order |
| flm/gemm (§14 step 3, part) | `iron/operators/flm/gemm/op.py`, `design.py` (constants only) | legacy defaults reproduced (tile_n by K, m_chunk fallback), config/name stems unchanged, B's packed spec, residents, unsplit and split sequences transfer by transfer | **needs a run**: the two-compile `link_xclbin` now builds the configuration module from a copy at the reference shape; `dev.arch`/target-model calls are faked here |
| mem_copy (§14 step 3, part) | `iron/operators/mem_copy/op.py` | whole, partial and tiny sizes: elements filled equal elements drained, padding groups awaited | **needs a run**: idle-fifo placement moved from the design into `build_design` (`RuntimeEndpoint(AnyShimTile)`) |
| swiglu_prefill_stream (§9 `from_spec`) | `iron/common/declare.py`, `iron/operators/swiglu_prefill_stream/op.py` | a class from literal shapes, params, key and a custom artifact; the stream group built on it (import only: stream-dse is absent here) | **needs a run** with stream-dse |
| step 4 deletions | `iron/common/base.py`, `compilation/base.py`, `build.py`, tests | `bind()`, `bind_from`, the `arg_spec` fallback, `same_shape_*`, the snapshot and its cases, the binding tests: gone; GEMM's layout flags and MHA's padding re-pinned on the declared classes | **needs a run**: `build_design` now receives `dev` and `kernels_dir` as explicit generator kwargs (they reach the cache key by identity and path) |
| swiglu composites as graph functions (§14 step 3, last) | `swiglu_decode/op.py`, `swiglu_prefill/op.py` | traced: five steps, gate and up on one array with one design key, extents from the input shape; the no-padding rule at trace time | **needs a run**: the two hardware tests were rewritten onto `compile()`/call and read intermediates through `net.buffer(handle)` |
| lowering gate (see above) | `iron/tests/toolchain/lowering.py`, `lowering_graph.py` | 116 + 12 lowerings to instruction streams; MLIR diffed against PR 215 per case | kernels compile (the full ELF, next row); **needs a device**: numbers |
| full ELF (see above) | `iron/tests/toolchain/full_elf.py` | — | swiglu decode and the scaled decode graph build to fused ELFs; the parameter table names both bound values; the real-size decode graph builds too (13.3 MB) | **needs a device**: loading, `params.write`, numbers |
| xclbin (see above) | `iron/tests/toolchain/xclbin.py`, `patches/` | — | separate dispatch on both devices, one kernel per design; flm/gemm's two compiles; mm_prebuilt's instructions and image; a plain operator on npu1 | **needs a device**: running the chain |
| design probe | `iron/tests/common/designs_run.py`, `cases.py` | every overlay's `design(target)` and every operator's sequence executed for 58 constructions on npu2 and npu1 shapes (116 runs, 2 skipped as incompatible), with upstream stubbed to no-ops: fifo and worker construction, every stream and resident bound, the preamble, the transfers | what it cannot check: that the calls are what upstream accepts |
| recorder retired, legacy value spellings gone, declared-operators net | `iron/common/graph.py` (`TracedGraph.sequence`), `iron/tests/infrastructure/graph_dispatch.py`, `iron/tests/common/operators_declared.py` | the four recorder tests ported onto graph functions (three need a device); every exported operator checked to be declared | **needs a run**: `graph_dispatch.py`, `jit_compile_path.py`, `mlir_cache_poisoning.py` |
| packaging surface (§14 step 5, part) | `iron/common/packaging.py` | 12 tests: the four rules, the named refusals (S1, S2), argument checks, the verbose report | **needs a run**: only `elf` (fused) and `xclbin` with `each_step` (separate) lower today; a fused sequence in an xclbin and `chunks(n)` wait on spike S1, modules on S4 |
| llama decode as a graph function (§14 step 7) | `iron/applications/llama_3.2_1b/decode_graph.py`, `llama_npu.py` | traced at a scaled-down config: 24 steps per block, weights named from the model, caches as state, both values bound (the softmax's on its overlay), like projections on one array, every operator tuned on an 8-column fake device | builds to a fused ELF at the scaled config, both values in the parameter table (full-ELF gate) | **needs a device**: parity against the token snapshot (§18) is the gate |
| graph functions (§14 step 6) | `iron/common/graph.py`, `iron/__init__.py`, `declare.py` hooks | 22 tests: runlist and names from roles, overlays shared by key, values bound and enabling, states, byte slices, instance calls, rank and shape rules, refused returns; every traced operator tunes from a fake device | the build path (`TracedGraph.sequence` → `OperatorSequence` → the fused ELF, and → the chained xclbins) verified by the full-ELF and xclbin gates; **needs a device**: writing values through `params` and calling |
| mm_prebuilt, foreign overlays (§9) | `iron/common/foreign.py`, `iron/operators/flm/mm_prebuilt/op.py` | pins and parameter block declared; 32 cores' words then locks before any DMA; consume-order transfers and per-slot queue bound checked against the old emitter's arithmetic | **needs a run**: the raw-dialect emission (`aiex.runtime_sequence(*types)` with `*args`, `shim_dma_single_bd_task`) has only been exercised against a recorder |

Step 2 is complete. Step 3 so far: repeat, strided_copy, transpose, gemm
and mha are declared overrides (`design(rt)` over the same `Sequence`), with
their access patterns kept as explicit descriptors (mha's as buffer slices)
and their RTP values as residents; `select()` carries gemm's layout
transposes and `Overlay.device()` its NPU1 column variants. mha's four
per-worker RTP words are four residents bound at an index into the same
buffers, and its `legalize_tas` hack is `tiling.legalize` through a slice.
The snapshot test, run under the stub for the first time, caught two
losses: SiLU's fixed single channel (`tunable(1, init=False)` now) and a
StridedCopy case the old design would have asserted on (now a real
gather).

flm/gemm is the model's showcase: `FLMGEMMOverlay` is exactly what the
xclbin depends on (its `config_name` is the stem), `GEMM` is the shape and
activation as residents, and `tuning(dev)` no longer looks at K; the legacy
constructor reproduces the old K-dependent `tile_n` default by passing it
explicitly. mem_copy's array was already extent-free. mm_prebuilt is the
foreign case: an `Xclbin` class attribute in place of `design()`, streams
pinned with `via=Shim(col, channel)`, a `Resident(address=, lock=)` block,
and `iron.common.foreign` emitting the raw-dialect sequence the old
`design.py` hand-wrote; task groups are no-ops there and the per-slot
queue bound comes from the stream's `depth`. The C12 read-back against
`input_with_addresses.mlir` is not done: a downloaded xclbin has no such
file, so the check is structural (every stream pinned, every resident
addressed) at class creation. swiglu_prefill_stream's group is
`Operator.from_spec`: a class built at run time from the exported shapes,
with the group digest as its sharing key and the stream-dse loader as its
artifact; the `OperatorSequence` composite around it stays until step 6.

Step 4 is done; the two legacy value spellings (strided_copy's
`*_offset_parameter` fields, softmax's `vector_size_parameter`) went once
the decode graph bound its values by handle. The recorder
(`iron.common.capture`) is gone too: `@iron.graph` is the authoring
layer, and `TracedGraph.sequence()` is the one seam onto the image
builder that both `CompiledGraph` and the infrastructure tests use. The snapshot test is gone with its
purpose; the shape regression net is now the per-operator device-free
tests in `iron/tests/common`, which pin shapes, tuning, residents and
transfers rather than a recorded table.

Step 6 is in: `@iron.graph` traces a function on handles, where a class
call on handles (`GEMV(w, h)`) infers, deduplicates the overlay by
`design_key()` and records, an instance call records against that
instance, a bare tensor is a weight, `iron.state(...)` is a pinned buffer
the graph writes into by passing it as an output, keyword-only parameters
annotated `Scratchpad[T]`/`DispatchTime[T]` are per-call values bound to
an operator's members (`use_value` enables them; two handles on one
instance is an error), and `h[a:b]` is a byte-range view. Three rules the
tracing forced: a flat declared buffer (`In(size)`) takes an operand of any
rank; every overlay tunable has a device default (elementwise tiles of
256, every column the shim budget allows, RMSNorm one core, transpose 64 x
64 x 8) so inferred construction needs no tuning arguments, and a call site
that knows its extent passes better ones; construction goes through each
class's `_classic` translation so derived overlay fields (a transfer size)
are filled the same way on both paths. Lowering targets `OperatorSequence`
as it stands (a fused ELF on NPU2, per-step xclbins on NPU1); `compile(dev,
boundaries=, image=)` and the image rules are step 5. O2 is settled as the
kwargs spelling (`GEMV(wk, x, num_aie_columns=8)`). O9 stands: the class
tells the two calls apart by receiving handles. O10: state is zero at
upload, read and written through `CompiledGraph.buffer(state)`, and sized
by its declaration; a module with two graphs over one state is step 5.

Step 3 is complete: `swiglu_decode(w_gate, w_up, w_down)` and
`swiglu_prefill(...)` return graph functions closing over the weights;
`CompositeOperator` and the two `OperatorSequence` composites are gone.
Two more graph rules came with them: a flat-declared output (an
elementwise operator) keeps the shape of the operand it is the size of,
and `h.reshape(...)` is a free view. `Operator.design_key()` is now the
class, the overlay's key and every compared field, so a sequence builds
two identical projections once (`share_designs`).

Step 7 is written: `DecodeGraph` (in the application, importable without
a device) closes over the module tree, keeps the per-layer caches as
`iron.state((n_kv_groups, max_seq_len * head_dim))`, and takes
`cache_offset` and `vector_size` as `Scratchpad[np.int32]` parameters; the
per-head transposes are one batched `Transpose`, and each value binds to
the operator's own member or, for the softmax, to the dynamic overlay's
core-read member (the tracer looks on both). `llama_npu.py` compiles it
against `build_elf`, calls it per token, and seeds the caches after
prefill through `CompiledGraph.write(state, tensor)`, which also pushes
the bytes to the device. Prefill is unchanged (per-operator xclbins,
O11).

Step 5 is started at the surface: `compile(dev, boundaries=, image=,
verbose=)` derives the image by the §8 rules, refuses `image=elf` where a
rule forbids it (naming the value, the boundaries or the device), reports
each value's lowering, and lowers `elf` to the fused ELF and `xclbin` +
`each_step` to the chained per-operator xclbin that exist today. The rest
of step 5 needs a device: a fused sequence in an xclbin (S1) is what
`chunks(n)` and `image="xclbin"` alone would build; modules over several
graphs (S4); the §11 prototypes (instructions-only compile against a
shared overlay, the callee-sequence pruning); and deleting the dispatch
hierarchy, which the graph lowering still stands on. O6 is settled as
free functions (`iron.chunks`, `iron.each_step`); O7 by `Plan.report`.

The sandbox verification now reaches every `design()` body: the design
probe runs each converted overlay's array construction and each
operator's sequence with the upstream API stubbed to no-ops, on both
device widths. That is the closest a device-free run gets; the remaining
gap is whether the calls are what upstream accepts, which only the
toolchain says.

What to run first on a device, in order: `pytest iron/tests/toolchain`
(it is what the lowering environment already passes; a device changes
nothing there), `pytest iron/tests/infrastructure` (the three ported
recorder tests that need a run), the GEMV and ReLU operator tests, then
the llama application against the token snapshot, with §18's two
candidates the first things to try if it drifts. The snapshot
entries for Softmax and Transpose were re-pinned to their 2-D shapes and
WeightedRMSNorm added to the case matrix. Every operator now serves
`get_arg_spec()` from its declared buffers.

Two findings while building, both now stated in the code:

- **The descriptor slot rules are not one wrap limit.** Read from
  `AIEX::verifyStridesWraps`: the innermost size is 1023 *granules*
  unless the transfer is linear or contiguous, the next is 1023 elements,
  the third has no wrap field, and the outermost is the iteration count,
  at most 64 and the only slot whose stride may be zero. GEMV's coalesced
  descriptor and repeat's re-read follow from this; `tiling.py` encodes by
  the rules rather than by example. Upstream also has an
  `aie-decompose-large-dma-bd` pass now, so an oversize pattern may lower
  without IRON splitting it; the encoder still emits legal descriptors so
  the instruction stream does not depend on that.
- **taplib is used for what it has.** `TensorAccessPattern` is the output,
  `TensorTiler2D` describes 2-D tilings for overrides, and
  `TensorAccessSequence` is the coverage check. It has no notion of
  descriptor legality, so `tiling.legalize()` takes any tap and returns
  legal ones; it is the general form of mha's `legalize_tap` and a natural
  upstream contribution.

`pytest iron/tests/common` passes without the stub, against the real
bindings, and the GEMV object gate is settled above; what remains of the
original toolchain list is the on-device half: `pytest
iron/operators/gemv iron/operators/relu`, then the rest of the ten.

---

## 18. Carried risk, unrelated to this work

**NPU decode output degrades after a few tokens** versus `llama_cpu.py` on the
same prompt and seed. Prefill reproduces exactly and the first tokens agree,
then the NPU drifts. Not the weight-naming refactor; uploaded bytes are
`torch.equal` for all 146 parameters. `iron/applications/llama_3.2_1b/test.py`
asserts only `returncode == 0`, so it does not catch this, and **a rewritten
llama will inherit it and look guilty.**

Decision: snapshot the current token stream before step 7 and make parity
against that snapshot the gate, not parity against the CPU. Cheapest real
probe if revisited: compare NPU versus CPU *logits* for one decode step rather
than sampled tokens.

Two things the rewrite kept as they were, because they may be the drift
and a rewrite is not the place to find out:

- **The softmax's valid length is written cumulatively.** The old decode
  wrote `softmax_vector_size_cum += context_len` into the parameter each
  token, so after k tokens the mask length is the sum of the context
  lengths so far, not the context length; it passes `max_seq_len` within a
  few tokens. If the scratchpad write is absolute (the overlay's core reads
  the slot directly), that is the drift. `decode_graph.py` and
  `llama_forward_pass_decode` reproduce it and say so; the one-line probe
  is to write `context_len` instead.
- **The caches copied after prefill were never pushed.** The old handoff
  wrote the prompt's keys and values into the fused arena's host view and
  then called `scratch_buffer.to("cpu")`; nothing synced that arena to the
  device afterwards, so whether the first decode token saw the prompt
  depended on the coherence semantics of that call. The rewrite seeds the
  state through `CompiledGraph.write`, which pushes the buffer.
