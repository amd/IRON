<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Operator model: interfaces on both sides — the operator's host ABI, the overlay's device ABI

Draft plan. Input to a plan-refining session, not approved work.

Branch `operator-model-argspec`. Baselines (always
`source /opt/xilinx/xrt/setup.sh` first, or 40–100 tests fail in a way that
impersonates a toolchain regression): `iron/tests` 745 passed / 13 skipped;
`iron/operators` 3165 passed with 5 known `mem_copy` 16-core timeouts.

This consolidates two earlier drafts. The superseded one proposed shape
annotations on the design function's signature; §21 records why that lost and
what was measured to establish it.

**Nothing here is built. §19 step 0 gates all of it**, because the one
load-bearing unverified claim fails as a device hang rather than a build error.

---

## 1. Priorities driving this

In roughly the order they were raised:

1. **General purpose.** LLMs, CNNs, anything composed of IRON operators. Not a
   llama-shaped abstraction, and specifically *not* a `forward()` method.
2. **No string names.** Buffers, weights, and runtime values addressed by handles
   and by parameter identity, not by hand-typed strings.
3. **Library quality.** Other people write models against this: stability, docs,
   a real test surface per operator.
4. **Prefill is in scope**, not just decode.
5. **Per-operator tuning, easy to override** by a user who wants something else.
6. **Tuning may fail.** Some operators legitimately have no legal config for a
   given shape/device. Per-device decisions must come from the target model's
   numbers, not hard-coded constants.
7. **Minimal duplicated spec logic**, to shrink the surface for typos.
8. **Static and build-time checking for new operators, including untested ones.**
9. **Fix the operators that flatten** real 2-D shapes into one dimension.
   Believed to be an artifact of old mlir-aie limits since lifted.
10. Coverage checks **run on every build unless disabled**.
11. pyright suppression lives in **pyrightconfig, not per-file**.
12. `Tuning[T]` is **IRON-local** (not upstreamed for now).

Three more were added while drafting, and they shape the whole document:

13. **Nothing works by accident.** Every contract is enforced by a check that
    names the mistake, the operator, and the fix. Where the hardware forces a
    restriction, the error explains the hardware reason.
14. **Overlay and runtime sequence are separable, and the model must say so.**
    A full ELF is one packaging option among several, not the shape of the
    system. llama must run with and without it, and with and without separately
    reusable sequences — by composing different objects, not by rewriting the
    model.
15. **Types, not strings; primitives, not strategies.** Priority 2 applies to
    every value the model carries, not just buffers. A packaging choice is a
    *class*, not a string compared in an if-tree. A tuning result is a typed
    instance, not a `dict` of names. And the library ships the *tools* to say
    what happens at each dispatch boundary and each compile — not a menu of
    blessed strategies with names like `"fused"`.

### Vocabulary warning

IRON and mlir-aie use **overlay** for different things. Here an *overlay* is the
configured array — per-core ELFs plus the CDO/PDI that loads them — which is the
FPGA sense of the word. mlir-aie uses it narrowly, for the *control-packet
routing* overlay (`--generate-ctrl-pkt-overlay`, `@ctrl_pkt_overlay`, pass
`aie-generate-column-control-overlay`). Where this plan means that one it says
**control route**. Decision taken: keep `Overlay` for the IRON noun.

---

## 2. Diagnosis: what `llama_npu.py`'s 1182 lines actually are

| chunk | lines | what |
|---|---:|---|
| operator construction | ~370 | `GEMV(M=..., K=..., num_aie_columns=8, tile_size_output=dim//8, ...)` ×30 |
| runlist + sequence | ~140 | string-threaded `(op, "x", f"layers.{i}...", "x_norm")` |
| buffers + weight upload | ~160 | `XRTTensor`, `_upload`, subviews |
| prefill host glue | ~300 | CPU/NPU ping-pong: softmax, `torch.matmul`, `torch.cat` on host |
| decode glue + main | ~90 | |

`capture()` as it stands attacks only the ~140-line runlist. **Operator
construction is the biggest chunk**, which is why this work centres on the
operator model rather than on the graph recorder.

The prefill ~300 is a *different* problem — missing and unfused operators, not
authoring. No declaration scheme fixes it. See O5.

---

## 3. The core idea: the declaration lives in a method body

The superseded draft's entire spelling problem — deferred annotations,
`localns`, free names, module-level `Dim`s, pyright suppression, evaluating one
annotation at a time, branch-parameter retry — existed to get a design's
**parameter names into annotation scope**. Python evaluates annotations in the
*enclosing* scope.

A method body doesn't have that problem. `self.M` is simply in scope.

```python
@dataclass
class GEMV(MLIROperator):
    """Matrix-vector product ``C = A @ B``, optionally batched."""

    M: int
    K: int
    num_batches: int = 1
    num_aie_columns: Tuning[int] = 8
    tile_size_input: Tuning[int] = 4
    tile_size_output: Tuning[int] | None = None

    def interface(self):
        """The host-visible ABI: buffers in call order, then runtime values."""
        self.A = In(self.num_batches, self.M, self.K)
        self.B = In(self.num_batches, self.K)
        self.C = Out(self.num_batches, self.M)

    def tuning(self, dev) -> "GEMV":
        cols = self.num_aie_columns or dev.cols
        if self.M % cols:
            raise Untunable(f"M={self.M} does not divide across {cols} columns on {dev}")
        return replace(self, num_aie_columns=cols, tile_size_output=self.M // cols)

    def reference(self, A, B):
        return A @ B
```

Conditional shapes are ordinary Python:

```python
        self.B = In(self.N, self.K) if self.b_col_maj else In(self.K, self.N)
```

**Field annotations still carry meaning.** A plain field is compile-time;
`Tuning[T]` marks a knob. Both are real dataclass fields, so pyright checks
`GEMV(M="2048")`, missing arguments and bogus kwargs — measured in §16 as the
most valuable static checks, and the ones synthesised fields destroy.

**`tuning()` returns an instance, not a `dict`.** `dataclasses.replace` is
checked by pyright against the real field list, so "tuning set a knob that
doesn't exist" and "tuning set a compile-time field it has no business setting"
are both static errors (E9) rather than runtime dict-key checks.

### Names without strings

`MLIROperator.__setattr__` records interface assignments in declaration order, as
`nn.Module` does for parameters. **The attribute name becomes the name**, so
diagnostics say `'A'` and `'output_offset'` without anyone typing a string, and
`output_offset_parameter="cache_offset"` disappears.

This is the one piece of magic in the plan. It is paid for by E1–E3.

---

## 4. Per-operator tuning

Two tiers. A constant knob is just a field default; a knob derived from shape
gets the `tuning()` method above. A call-site override is fed **into** it, so
dependent knobs re-derive rather than silently keeping values computed for a
different `cols`:

```python
g(GEMV, w, x)                                       # infer shapes, default tuning
g(GEMV.tuned(num_aie_columns=2), w, x)              # override a knob, dependents re-derive
g(GEMV(M=2048, K=2048, num_aie_columns=2), w, x)    # fully explicit -- works today
```

`Untunable` is an expected outcome, not a bug — better than defaulting into a
config that compiles and then hangs (cf. the `mem_copy` 16-core failures, which
compile fine and fail at runtime on the 8-column box).

This retires a live FIXME in `iron/operators/gemv/op.py` (`MAX_WRAP = 1023`,
"pull these shim BD bounds from the MLIR-AIE target model rather than
hard-coding").

**What the target model actually exposes**, checked rather than assumed:

| wanted | available | how |
|---|---|---|
| columns, rows, memtile rows | **yes** | `tm.columns()`, `tm.rows()`, `tm.get_num_mem_tile_rows()` |
| BDs per shim tile | **yes** | `tm.get_num_bds(0, 0)` — 16; `flm/gemm/design.py:277` already reads it |
| shim DMA channels per direction | **yes** | `get_num_source_shim_mux_connections`; see §6 for the trap |
| L1 bytes per core | not checked | |
| shim BD wrap/stride caps (the `MAX_WRAP` FIXME) | **not checked** | this is the one the FIXME needs; verify before promising `dev.max_wrap` |

### The resolution pipeline, and the shape/tuning invariant

```
operand shapes -> unify -> compile-time fields -> tuning() -> Tuning knobs -> construct
```

**A shape may reference compile-time fields only, never a `Tuning` knob**, or the
pipeline is a cycle. This holds naturally for all 12 operators, and it *forces
the right taxonomy*: `RMSNorm`'s `tile_size` is shape-bearing
(`rows = (size // tile_size, tile_size)`), so it must become a compile-time
field — which is also priority 9's un-flattening. The same invariant extends to
runtime values in §9.

---

## 5. What a compiled operator actually is

Everything from here rests on this section. The claims are read out of the
toolchain, not assumed.

`aiecc`'s own dependency graph (`aiecc --emit-dot`) splits at the tail. Up to
`physical_with_elfs.mlir` both modes are identical; after it:

| half | artifacts | a function of | **not** a function of |
|---|---|---|---|
| **overlay** — the configured array | `elfs_{0}.elf` (one per core), `cdo_{0}` → `{0}.pdi`; in xclbin packaging also `memTopology/kernels/partition_{0}.json` → `aie.xclbin` | the design, its compile-time fields, the device | the call order, the buffer bindings, any runtime value |
| **sequence** — the instruction stream | `npu_seq_{0}.mlir` → `npu_program_{0}.bin` → `insts_{0}.bin` (or `npu_insts_full_elf_{0}.bin` + `full_elf_{0}.ctrlpkt.bin` on the ELF path) | the overlay it targets, the steps in it, the overlay's ABI (§6) | the *contents* of any buffer |

The XRT dispatch ABI makes the split visible, and makes clear why the ELF path
gives it up:

```python
# xclbin: the sequence is argument 1. Swappable per call.
kernel(3, insts_bo, insts_bytes, *buffers)              # hostruntime.py:331

# full ELF: buffers only. There is no instruction-buffer slot at all.
for i, buf in enumerate(buffers):
    run.set_arg(i, buf)                                 # hostruntime.py:344-371
```

Upstream's runtime already caches the two halves independently — `hw_context`
keyed on `(xclbin_path, mtime)` (`hostruntime.py:817`), the instruction BO keyed
separately on `(insts_path, mtime)` (`:586-602`). **That is the structural basis
for one overlay and many sequences, and it exists today.** IRON already exploits
it in `SeparateDispatch`, which builds one `NPUKernel` per operator all pointing
at one chained xclbin, differing only by kernel name and insts path
(`iron/common/sequence.py:877-894`).

The full-ELF path collapses the split by construction: `hw_context` comes from
`pyxrt.elf` and is keyed on `(elf_path, mtime)` (`hostruntime.py:713`), the
kernel name is `"<device>:<sequence>"`, and no instruction cache is kept at all.

### Three degrees of sequence reuse

| level | what is reused | cost of a new sequence | available |
|---|---|---|---|
| **L1 — separate files** | the overlay's `hw_context`, across sequences in one process | a full `aiecc` run (both halves) | **now**; `SeparateDispatch` does it |
| **L2 — separate compiles** | the overlay's *compilation* | one `aiecc` run of the sequence half only | **no** — `--sequence-name`/`--device-name` exist as aiecc flags but nothing in Python drives them, and `--xclbin-input` needs a fresh run per kernel. Upstream ask; O8 |
| **L3 — host-generated** | everything; the sequence is built in-process | microseconds, no aiecc, via a prebuilt `dispatch-<digest>.so` | **now**, as the dispatch bridge — xclbin packaging only. §11 |

**L3 already delivers what L2 is wanted for**, in the case where only scalars
change between sequences — which is llama's case. That is why §11 makes it a
sequence *type* rather than a footnote.

### How the overlay reaches the array

`aiex.configure` lowers to load-PDI firmware instructions, and
`ExpandMode = {none, write32, ctrlpkt}` (`AIEXAttrs.td:41-42`) decides what those
become. This is a property of the **sequence**, because it determines what ends
up in the instruction stream:

| mode | mechanism | consequence |
|---|---|---|
| `Pdi` (`none`) | `load_pdi` against a PDI packaged in the image | the image must carry the PDI; the sequence alone cannot configure the array |
| `Inline` (`write32`) | `--expand-load-pdis` rewrites it to `write32`/`blockwrite` **inside the instruction stream** | the sequence is self-configuring. Bigger: 99,768 bytes against 70,936 on a two-step graph (`jit_compile.py:231-237`) — and the smaller one is a different, broken program, not a tuning win |
| `CtrlPkt` | `--load-pdi-to-ctrl-pkt`; config streamed as control packets over a control route | implies `--generate-ctrl-pkt-overlay`; mutually exclusive with `--expand-load-pdis` |

`Inline` is the load-bearing one. It is what lets a runtime sequence carry its
own array configuration; IRON already forces it for every fused ELF and the
device hangs without it. It is also, per §11, exactly what the dispatch bridge
needs — a convergence neither side currently knows about.

---

## 6. The overlay has an interface too

`interface()` is the operator's **host** ABI. An overlay has a symmetric
**device** ABI, and a sequence is valid against an overlay only if it agrees on
it. Comparing content hashes — an earlier draft's check — is a crude proxy: two
builds can hash differently for irrelevant reasons while agreeing perfectly, or
hash-match on the recipe while the core that reads a resident value has moved.

```python
@dataclass(frozen=True)
class ShimBinding:
    arg: int              # runtime_sequence argument index
    tile: Tile            # shim column, row 0
    direction: Direction  # MM2S (enters the array) | S2MM (leaves it)
    channel: int          # 0..1

@dataclass(frozen=True)
class ResidentSymbol:
    name: str
    address: int
    readers: tuple[Tile, ...]

class Overlay:
    hash:      str
    bindings:  tuple[ShimBinding, ...]      # which shim/channel each buffer uses
    residents: tuple[ResidentSymbol, ...]   # RTP scratchpad layout + who reads it
    sizes:     tuple[int, ...]              # expected memref element counts
```

**None of this needs new tooling — it is already on disk**, and two of the three
files are ones IRON already opens:

| field | source | who reads it today |
|---|---|---|
| `bindings` | `input_with_addresses.mlir` | IRON reads this file already, for trace layout (`sequence.py:779`, `tracing_utils.py:68`) — but never for bindings |
| `residents` | `params.txt`, from `--get-scratchpad-parameters` | `ParameterScratchpad`, `sequence.py:731-757` |
| `sizes` | `parse_dma_sizes` on `input_with_addresses.mlir` | `CompilableDesign.validate_tensor_args` |

Bindings are a two-hop join inside one file. Real generated output from
`build/FLM_GEMM_M1024_K10240_N2560_tn64_ma32_emf_conv_even_npu2.mlir.d/input_with_addresses.mlir`:

```mlir
// :5453   arg index -> memref
aie.runtime_sequence(%arg0: memref<10485760xbf16>,
                     %arg1: memref<3276800x!aiex.bfp<"v8bfp16ebs8">>,
                     %arg2: memref<2621440xbf16>)

// :5650+  arg -> symbol, via the dma_bd operand
%0 = aiex.dma_configure_task_for @B_L3L2_0_shim_alloc { aie.dma_bd(%arg1 : ...) }

// :6731+  symbol -> (tile, direction, channel)
aie.shim_dma_allocation @A_L3L2_0_shim_alloc(%shim_noc_tile_0_0, MM2S, 0)
aie.shim_dma_allocation @B_L3L2_0_shim_alloc(%shim_noc_tile_0_0, MM2S, 1)
aie.shim_dma_allocation @C_L2L3_0_shim_alloc(%shim_noc_tile_3_0, S2MM, 0)
aie.shim_dma_allocation @C_L2L3_3_shim_alloc(%shim_noc_tile_1_0, S2MM, 0)
```

Note the scramble on `C`: logical fifo `_0` lands in column 3, `_3` in column 1.
Pure placer output, no author intent — and the placer sorts fifos **by name**
(`program.py:162`), so renaming a fifo silently permutes the bindings. That is
the reuse hazard in one line, and it is invisible today.

Neither `params.txt` nor `kernels_main.json` carries bindings, so
`input_with_addresses.mlir` is the only source.

### Existence proof: IRON already does this agreement by hand

`iron/operators/flm/mm_prebuilt` is a sequence written against an overlay someone
else compiled — a **downloaded xclbin**. It works only because the author
hand-matched the shim bindings, in the only place in the tree that pins a channel
(`design.py:109-116`):

```python
shim = [aie.tile(c, 0) for c in range(COLS)]
for r in range(ROWS):
    aie.shim_dma_allocation(f"A_{r}", shim[A_SOURCE_COL[r]], DMAChannelDir.MM2S, 0)
for c in range(COLS):
    aie.shim_dma_allocation(f"B_{c}", shim[c], DMAChannelDir.MM2S, 1)
    aie.shim_dma_allocation(f"C_{c}", shim[c], DMAChannelDir.S2MM, 0)
```

with the reason at `:49-51` — *"Unlike flm.gemm — which lets the placer choose —
this must match the placement baked into the downloaded xclbin."*

And the failure of the contract is recorded too, at `:24-27`:

> `iron.operators.flm.gemm` is a port of this overlay… Its own instruction stream
> still cannot drive this xclbin: it writes no runtime parameters, and **its
> lowering puts B on MM2S channel 0 in the odd columns.**

That is a sequence that cannot drive an overlay, diagnosed by hand and written
into a comment. `Overlay.bindings` plus E23 turns it into a message.

### Constraining a binding

Verified controllable, end to end. The pin goes on the ObjectFifo handle that the
`Runtime` receives (`objectfifo.py:260-351`; it takes effect at
`runtime/runtime.py:301-305`):

```python
of_c.cons(tile=Tile(1, 0), channel=0)     # col 1, row 0 = shim
```

**Direction is not spelled, and must not be.** It follows from which end sits at
the shim: `.prod()` ⇒ `MM2S` (enters), `.cons()` ⇒ `S2MM` (leaves)
(`iron/dataflow/flow.py:48-57`). Which means `In`/`Out` in `interface()` already
carries it, and the operator-level spelling needs only column and channel:

```python
    def interface(self):
        self.A = In(self.M, self.K)                          # placer assigns
        self.C = Out(self.M, via=Shim(col=1, channel=0))     # this one is pinned
```

The design passes the constraint through to `.cons(tile=, channel=)`; if it
forgets, the post-compile read-back of `input_with_addresses.mlir` catches it
(E29). So the design does not have to be trusted — it has to be *checked*.

### What the hardware allows, and what nobody has exercised

- **2 MM2S + 2 S2MM per shim tile**, on npu1 and npu2 alike. Device-wide that is
  16 MM2S on npu2, 8 on npu1. IRON already wraps the query as
  `get_shim_dma_limit` (`iron/common/utils.py:7-19`) and guards on it
  (`operator_bases.py:70-75`). The accessor is
  `get_num_source_shim_mux_connections`, **not**
  `get_num_*_switchbox_connections` — the latter returns 0 for `DMA` on row 0,
  because the shim DMA hangs off the shim mux. Easy trap; worth a comment
  wherever it is used.
- **Existing pins.** `gemm/op.py:1021-1026` and `mha/op.py:927-932` pin shim
  *tiles*; `mem_copy/op.py:352-355` explicitly opts out with
  `RuntimeEndpoint(AnyShimTile)`. Only `mm_prebuilt` pins a channel.
- **`channel=` is unexercised.** Zero call sites in IRON, and no Python-side
  validation that `channel < 2` — an out-of-range value fails deep in lowering or
  not at all. E30 validates it at `interface()` time against the target model.
- **Re-pinning raises rather than merges** (`objectfifo.py:293-302`), comparing
  by `(col, row)` because `Tile.__eq__` is identity-based
  (`device/tile.py:107-110`).
- **Pinning constrains everything else's routing.** `flm/gemm` has zero placement
  slack — *"the memtiles pack to exactly 512 KB"* (`design.py:516-517`) — so
  adding shim pins there will surface "number of input DMA channel exceeded"
  rather than just working. Constraint is a tool, not a default.

**Correction to a standing belief:** `flm/gemm` does *not* demonstrate shim
control. Its one placement pin is a **memtile** (`design.py:523-533`,
`tile=Tile(c, 1)`), with a comment saying everything else is left to the placer.
Its README claims A broadcasts from columns 0/2/4/6 (`README.md:58`); that is
what the placer currently produces, but nothing pins it, and the name-sorted
placer can move it. That line should be corrected or the pin should be added —
tracked as O13, independent of this plan.

---

## 7. Lifecycle

```python
op  = GEMV(M=2048, K=2048)     # __init__ -> interface(). Cheap. No validation, no MLIR.
op  = op.specialize(dev)       # run tuning(), bind device, validate
ov  = Overlay(op, dev)         # core ELFs + PDI; publishes bindings/residents/sizes (§6)
seq = StaticSequence(ov, op)   # TXN / insts, written against ov's ABI
net = Xclbin(ov, seq).load(dev)
net(A, B, C)
```

The `specialize` split is load-bearing, not cosmetic. Today validation is spread
between `__post_init__` and five asserts inside `my_matvec`. Moving it to
`specialize()` is what lets `__init__` tolerate **symbols**, which is how
inference works:

```python
probe = GEMV(M=Sym("M"), K=Sym("K"), num_batches=Sym("b"))   # interface only, nothing validated
unify(probe.interface, operand_shapes)                        # -> {M: 2048, K: 2048, b: 1}
op = GEMV(M=2048, K=2048, num_batches=1)                      # construct for real
```

A symbol only has to survive *construction*, never a branch or an arithmetic
operation. That is why `num_batches` — which is both branched on *and* the thing
we want to infer, and which the annotation draft needed rank-directed branch
resolution for — is simply not a problem here.

`specialize()` is also upstream's word for binding a dynamic parameter to a
constant, so one method covers both jobs (§9, §11).

**Honest caveat on `Overlay` / `Sequence`.** Today `aiecc` emits both halves from
one invocation, so constructing both is *one* build underneath. What the plan
buys immediately is that the halves are **named, published and checked
separately** (§6) — which is L1, and which is what packaging needs in order to
reuse a `hw_context` across sequences. Splitting the *compile* is L2 and needs
upstream (O8). The API is shaped for L2 now so that landing it later is not a
signature change.

---

## 8. The design consumes the interface

```python
def my_matvec(dev, interface, M, K, num_batches, num_aie_columns, tile_size_input, ...):
    A, B, C = interface
    L1_A_ty = np.ndarray[(tile_size_input, K), bf16]
    ...
    rt = Runtime(sequence, [A, B, C, *fifo_endpoints])
```

`L3_A_ty` / `L3_B_ty` / `L3_C_ty` disappear — they *were* the duplicate. One
declaration in `interface()`, consumed by the design, enforced by identity (E7).
This is what deletes `arg_spec` and `bind()` outright: order, direction, shapes
and dtypes all fall out of one declaration.

**Known divergence from upstream.** mlir-aie's `@iron.jit` convention is
`def design(a: In, b: Out, *, N: CompileTime[int])`, classified by
`split_params()`. Here the design takes the interface positionally instead. That
is defensible — an IRON design is an internal function called by an operator, not
a user-facing jit entry point — but it is a real divergence, and §11 shows it has
a concrete consequence for `SequenceResident` values. See O4.

---

## 9. Runtime values: named by what rebuilds

A value that changes at runtime has to live somewhere, and where it lives decides
what a change costs. The declaration says *where*, so the cost is legible at the
declaration site:

```python
    def interface(self):
        self.src = In(self.n_kv_groups, self.head_dim)
        self.dst = Out(self.n_kv_groups, self.seq_len, self.head_dim)

        self.output_offset = HostResident(np.int32)      # in a buffer the device reads
        self.n_tokens      = SequenceResident(np.int32)  # in the instruction stream
    # a plain dataclass field is OverlayResident         # in the array configuration
```

| tier | lives in | changing it rebuilds | cost |
|---|---|---|---|
| `HostResident` | a resident BO the device reads (`aiex.scratchpad_parameter`) | **nothing** | a few words + a sync |
| `SequenceResident` | the instruction stream | the **Sequence** | stream regen + BO alloc per call |
| `OverlayResident` (a plain field) | the array configuration | the **Overlay** | a full compile — 8–12 ms/token if done per value (`project_patch_elf_measured`) |

Each tier is named for the artifact §5 defines, so "why is this slow" answers
itself and the error message needs no translation:

```
n_tokens is SequenceResident, so changing it rebuilds the Sequence
(stream regen + BO alloc per call). Declare it HostResident to make it free,
or as a plain field to bake it into the Overlay.
```

Deliberately **not** reusing upstream's `DispatchTime` for the middle tier:
upstream's `DispatchTime` *is* `SequenceResident`, and naming the free tier
anything with "dispatch" in it next to that would be a trap.

Verified that `HostResident` is genuinely free and genuinely powerful:
`strided_copy/op.py:174-189` passes a `ScratchpadParameter` as
`offset_parameter=` to `.fill()`/`.drain()` with `sync_parameters()` in the
sequence — so it drives DMA offsets, under full ELF. That is why llama's
`cache_offset` works today (`llama_npu.py:1101-1104`), and llama needs nothing
above the bottom tier.

### Choosing a tier

The author declares the tier. There is **no lazy compile and no silent deopt** —
`compile()` compiles, using the declared tiers as written.

Inference belongs only where the call *is* the entry point and compiling on the
first call is the whole contract:

```python
# compile-on-demand: eager, declared tiers used as written. No inference.
net = decode.compile(dev)

# JIT: values are in hand at the call, so specializing a SequenceResident that
# only ever takes one value to an OverlayResident constant is expected, not sneaky.
@iron.jit
def decode_step(x, offset): ...
```

A JIT that specializes must still be driven by **cardinality**, not by "it has
not changed yet". `cache_offset` takes one distinct value per token, unbounded;
specializing it is exactly the `patch_elf` disaster at 8–12 ms/token.

### Sharing is forced by the hardware, so make it explicit

A `HostResident` is **one named device symbol per design**. A fused sequence that
reuses one `StridedCopy` across 32 layers has one symbol, written once per token.
llama relies on this today and it happens to be correct only because all 32
layers want the same value.

Per-call-site values are not implementable on this mechanism — distinct symbols
would mean distinct designs, i.e. 32 compiled variants. So the contract is: **a
runtime value belongs to the operator instance, and reuse means sharing.**
Stated, documented, and checked (E10), not inherited.

```python
offset = g.param(np.int32)
for i, blk in enumerate(model.layers):
    g(StridedCopy.tuned(output_offset=offset), k, kc[i])
...
net[offset] = n * cfg.head_dim
```

Binding the same handle at many call sites is explicit sharing and legal. Binding
*different* handles to one operator instance is the accident, and it is an error
(E10).

### The shape invariant, extended

**A shape may reference compile-time fields only** — never a `Tuning` knob, a
`HostResident`, or a `SequenceResident`. One logical reason (§4's pipeline would
cycle) and one physical (a shape must be an `int` at build time). Upstream
already enforces it loudly for the middle tier: `_DispatchParameter` poisons
`__index__`, `__bool__`, arithmetic and comparisons (`markers.py:150-159`). IRON
enforces the same for `Tuning` and `HostResident` (E4, E5).

---

## 10. Primitives, not strategies

Today `dispatch="fused"|"separate"` is one string carrying four decisions. An
earlier draft replaced it with a four-axis `Deployment` record and a set of named
presets. That is the same mistake at higher resolution: it still enumerates
blessed combinations, and it still cannot express *partial* fusion, which is the
case that motivated the exercise.

**So there is no `Deployment` and there are no mode names.** There are four
constructors.

```python
class Sequence:
    """One entry point's instruction stream, written against one overlay's ABI."""
    overlay: Overlay
    steps: tuple[Step, ...]
    configure: Configure  # Pdi() | Inline() | CtrlPkt(); derived, overridable

class StaticSequence(Sequence):
    """insts.bin from aiecc --get-npu-insts. Read once, cached on (path, mtime)."""

class GeneratedSequence(Sequence):
    """dispatch-<digest>.so from --npu-cpp-emit-dispatch-shim. Called per dispatch."""
    params: tuple[SequenceResident, ...]

class Elf(Image):
    def __init__(self, overlay: Overlay, sequence: StaticSequence): ...
class Xclbin(Image):
    def __init__(self, overlay: Overlay, *sequences: Sequence): ...
```

Read the two `Image` signatures: they carry the legality story an earlier draft
needed a table for.

- **`Elf` takes exactly one sequence, and it must be static.** A full ELF has no
  instruction-buffer argument to swap a per-call stream into
  (`hostruntime.py:344-371`), so `Elf(ov, generated)` is a **pyright error**, not
  a runtime one. "`SequenceResident` ⇒ xclbin" stops being a rule and becomes a
  type.
- **`Xclbin` takes any number of sequences.** That is the chained-xclbin reality:
  one image, N kernels, one shared `hw_context` (`sequence.py:877-894`). The
  asymmetry between the two constructors is real and is now in the signature
  instead of buried in a policy class.

### Dispatch boundaries are structure, not a mode

The `schedule="fused"|"stepped"` axis is gone, because it was never a mode — it
was a question about **where the host regains control**, and that is a property
of how you carve the graph into sequences.

```python
decode = g.build()          # -> Graph, with .steps
ov     = Overlay(decode, dev)

# one sequence: one dispatch, host sees nothing in between
Xclbin(ov, StaticSequence(ov, decode.steps))

# one sequence per operator: today's "separate"
Xclbin(ov, *[StaticSequence(ov, [s]) for s in decode.steps])

# partial: four dispatches, eight layers each. Not expressible today at all.
Xclbin(ov, *[StaticSequence(ov, c) for c in decode.chunks(8)])
```

The third form is what justifies the rework. It is also how a graph too large for
one instruction stream gets split, and how a host-side operation is interleaved
without giving up fusion everywhere else.

### What is derived, and what the user says

| decision | default | why |
|---|---|---|
| `Sequence.configure` | `Inline()` if the sequence spans more than one device configuration, else `Pdi()` | a multi-config sequence *cannot* work with `Pdi()`. Overridable to `CtrlPkt()`, which has no automatic answer |
| which `Image` | `Elf` on NPU2 with one static sequence, `Xclbin` otherwise | today's `AutoDispatch`, kept as a **function returning a composed object**, not a mode anything branches on |
| `Sequence` subclass | `StaticSequence` unless the steps declare `SequenceResident` values | declaring one *is* the request for a generated sequence |
| shim bindings | the placer assigns | §6; constrain per-buffer with `via=`, verified post-compile (E29) |

Every default is a one-line function over the primitives, so a user who wants
something else calls the constructor directly. Nothing downstream asks "which
mode am I in".

### What survives as runtime checks

| check | when | reason |
|---|---|---|
| `Elf(ov, ...)` where `ov.device` is NPU1 | `Elf.__init__` | NPU1 has no full-ELF dispatch (`sequence.py:128-133`) |
| sequence's ABI disagrees with the overlay's | `Image.__init__` | §6 — names the binding, not just a hash |
| `GeneratedSequence` whose lowering leaves >1 runtime sequence | build | inherited from `_check_runtime_sequence_abi` |
| `CtrlPkt()` and `Inline()` together | build | mutually exclusive aiecc flags |

---

## 11. `StaticSequence` vs `GeneratedSequence`

### The gate today is a side effect, not a decision

```python
has_dispatch = bool(self.dispatch_params)
...
inst_path = None if has_dispatch else kernel_dir / "insts.bin"
compiler_options.append("--get=npu_lowered.mlir")          if has_dispatch
npu_cpp_path = kernel_dir / "dispatch_gen.cpp"             if has_dispatch
npu_cpp_emit_dispatch_shim = has_dispatch
dispatch_so_path = compile_dispatch_bridge(...)            if has_dispatch
```

Five build decisions keyed off "does any value happen to be dynamic". Which kind
of sequence you get is not expressible; it is inferred.

### Both kinds land in the same slot

```python
# StaticSequence    -- insts.bin read from disk, cached on (path, mtime)
insts_bo = runtime._read_insts_cached(seq.insts_path)

# GeneratedSequence -- dispatch-<digest>.so called host-side
insts    = seq.bridge.generate([cache_offset, softmax_vector_size])
insts_bo = allocate_cacheable_bo(insts)                               # hostruntime.py:299-312

# identical from here
kernel(3, insts_bo, insts_bytes, *buffers)                            # hostruntime.py:331
```

`GeneratedSequence` is not a different dispatch path; it is a different
**producer** for argument 1, and `SequenceResident` values are that producer's
**arguments**. A `GeneratedSequence` with zero of them is coherent; it needs
`has_dispatch` widened to `has_dispatch or generated`, and the existing ABI check
already tolerates it (`len(c_types) != len(dispatch_params)`, and `0 == 0`
passes). Whether to allow it in production is O11.

### The convergence nobody has noticed

```python
if len(sequences) != 1:
    raise DispatchCompileError(
        f"dispatch bridge requires exactly one runtime_sequence; found {len(sequences)}.")
if requires_pdi_resources:          # any aiex.npu.load_pdi survived lowering
    raise DispatchCompileError(
        "The Python dispatch runtime cannot supply load_pdi resources. "
        "Use aiecc --get-npu-cpp with a native host that packages the "
        "referenced PDIs, or specialize all dispatch parameters and use full_elf=True.")
```

That second message assumes the only escape is full ELF. **IRON's fused path
already takes the other escape without knowing it**: `Inline()`
(`--expand-load-pdis`) rewrites every `load_pdi` into `write32`/`blockwrite`
inside the stream, so `requires_pdi_resources` should be false by construction.
The same flag a multi-step sequence cannot run without is the flag the dispatch
bridge needs. Confirming that is step 0b (§12).

### The declaration tension this creates

`CompilableDesign` derives `dispatch_params` by **introspecting the design's
signature**, keyword-only. This plan's design takes the interface positionally:

```python
def my_matvec(dev, interface, M, K, ...):
    A, B, C, n_tokens = interface
    rt = Runtime(seq, fn_args=[A, B, C, n_tokens])   # nothing here says DispatchTime
```

```python
# (a) the design declares them too; interface() is checked against it.
#     Costs a second declaration -- exactly what this plan exists to delete.
def my_matvec(dev, interface, M, K, *, n_tokens: DispatchTime[np.int32]): ...

# (b) @operator synthesizes an annotated wrapper from interface(). More magic.

# (c) IRON supplies the classification directly; interface() stays the single
#     source of truth. Plain attributes -- just derived in __init__ today.
CompilableDesign(gen, dispatch_params=["n_tokens"], dispatch_param_types=[np.int32])
```

**Recommended: (c)**, as a small upstream ask, with an IRON subclass in the
meantime. It is also the only option that keeps the strings out — the list is
generated from the recorded interface members rather than typed. (a) is the
fallback, degrading to a drift check rather than a correctness hole.

Inherited free either way: `_DispatchParameter._bind` (`markers.py:140-146`)
already enforces "forwarded exactly once into `Runtime(seq, fn_args=[...])`".

### The cost to measure

`GeneratedSequence` copies a fresh `uint32` array out of the `.so` per call
(`_dispatch_bridge.py:144-192`) and allocates a new cacheable BO per call
(`hostruntime.py:299-312`). Against a `HostResident` write — a few words into a
resident BO — the prior is that generated **loses** on latency. The point of
making it a type is that the answer becomes a number, and that it buys what a
scratchpad cannot: changing DMA *sizes and strides*, not just offsets.

---

## 12. llama four ways — the acceptance criterion

**Test fixtures, not API.** The model code above `decode = g.build()` is
identical in all four.

```python
decode = g.build()
ov     = Overlay(decode, dev)          # shared by all four

net = Elf(ov, StaticSequence(ov, decode.steps)).load(dev)                        # A
net = Xclbin(ov, *[StaticSequence(ov, [s]) for s in decode.steps]).load(dev)     # B
net = Xclbin(ov, StaticSequence(ov, decode.steps)).load(dev)                     # Ca
net = Xclbin(ov, GeneratedSequence(ov, decode.steps)).load(dev)                  # Cb
```

| | image | sequences | kind | dispatches/token | |
|---|---|---|---|---|---|
| **A** | `Elf` | 1 | static | 1 | today's path; the baseline. NPU2 only |
| **B** | `Xclbin` | ~15 | static | ~15 | today; runs on NPU1. Overlay shared across every step |
| **Ca** | `Xclbin` | 1 | static | 1 | **one overlay, one reusable insts.bin** |
| **Cb** | `Xclbin` | 1 | generated | 1 | per-token scalars with no scratchpad |

A fifth — `decode.chunks(8)`, four sequences of eight layers — costs nothing
extra to express and is unreachable today.

### Ca carries the shared risk

The fused MLIR emits `aiex.configure`/`aiex.run` per step
(`compilation/sequence.py:219-297`), which under `Inline()` expands into
`write32`/`blockwrite` inside the instruction stream — at which point the
xclbin's packaged PDI is needed only to establish the partition. That *should*
make Ca work. Nothing in the tree does it, and `_fuse_as_children` forces
`_iron_full_elf=False` on children for a related-but-different reason
(`jit_compile.py:142-160`), the failure mode being a link that succeeds and a
device that hangs with `ERT_CMD_STATE_TIMEOUT`.

### Cb adds two constraints on top

- **exactly one `aie.runtime_sequence` survives into `npu_lowered.mlir`.** The
  fused module starts with one per child device plus `main:sequence`.
  `aie-materialize-runtime-sequences` inlines `aiex.run` callees but the pass
  description does not say whether the callees are **erased**.
- **no `aiex.npu.load_pdi` survives.** Should hold under `Inline()`.

### Step 0: settle both before writing any model code

```bash
# 0a -- the shared risk. Two-operator fused graph, full_elf=False.
aiecc ... --expand-load-pdis --get-xclbin --get-npu-insts ...
# dispatch via opcode 3; it either runs or it hangs.

# 0b -- Cb's two extra constraints, same build plus:
aiecc ... --get=npu_lowered.mlir --get-npu-cpp --npu-cpp-emit-dispatch-shim ...
grep -c 'aie.runtime_sequence' <prj>/npu_lowered.mlir     # must be 1
grep -c 'aiex.npu.load_pdi'    <prj>/npu_lowered.mlir     # must be 0
```

An afternoon each. If 0a hangs, the primitives survive unchanged — `Xclbin` with
one multi-step sequence has no legal construction, llama-without-ELF means config
B only, and Ca/Cb defer behind an upstream fix.

### What to measure once they run

Per-token latency A vs B vs Ca vs Cb, plus `chunks(8)`; build time and artifact
size; and for Cb, host-side regeneration cost per token against the
`HostResident` write it replaces. Per `project_npu_bimodal_timing`: interleave
the configurations, ≥8 rounds — a non-interleaved min-of-medians has fabricated a
5% "win" here before.

---

## 13. Harnesses compose too

What `compare` actually requires is **a boundary after every step** — a list of
single-step sequences, not a mode:

```python
probs = Reference(decode).run(inputs)      # never receives an overlay

net = Compare(ov, [StaticSequence(ov, [s]) for s in decode.steps],
              rel_tol=0.05, abs_tol=1e-2).load(dev)
```

`Compare` cannot be handed one multi-step sequence, because there would be
nowhere to interrupt — structural rather than documented. `Reference` never
receives an overlay, so "reference compiles nothing" is likewise in the
signature.

---

## 14. Verification for a new operator with no tests

**Duplication and verification pull in opposite directions.** A second
declaration catches *drift*, never *wrongness* — a matching typo passes. IRON
proves this today: `GEMV.arg_spec` says `(M,K),(K,),(M,)`, the design forty lines
later says `(num_batches*M*K,),(num_batches*K,),(num_batches*M,)`, and
`arg_spec_snapshot.json` (a third restatement, 22 classes) has blessed the
disagreement. Green.

So verification must come from *structure and behaviour*, not restatement. That
is why §8 has the design consume the interface rather than restate it, and why
the checks in §15 are mostly structural rather than comparisons between two
hand-written specs.

The build-time coverage checks (E15–E20) are only *possible* because of the
single declaration: today the shape in `arg_spec` and the `tensor_dims` in the
TAPs come from different places, so comparing them proves nothing.

**Separately, and worth fixing independently of this plan:** `run_test` uses the
arg spec for direction and order only and never checks `spec.shape` /
`spec.dtype`, while tests feed it pre-flattened data. That is why the GEMV rank
disagreement above is invisible. Tightening it will surface some currently-green
failures.

---

## 15. Enforcement matrix

**T1** static, **T2** import/registration, **T3** specialize, **T4** build,
**T5** compose/load, **T6** hardware.

| id | mistake | when | mechanism |
|---|---|---|---|
| E1 | a name assigned twice, or conditionally | T2 | `__setattr__` records; `interface()` replayed, each name assigned exactly once |
| E2 | an interface member assigned outside `interface()` | T2 | `__setattr__` rejects these types outside the `interface()` call frame |
| E3 | count/order disagrees with the design | T4 | identity check against `Runtime` fn_args (E7) |
| E4 | a shape reads a `Tuning` knob | T2 | symbolic probe run twice under **different tuning**; the interface must be identical |
| E5 | a shape reads a `HostResident`/`SequenceResident` | T2 | poisoned `__index__` raises, naming the value |
| E6 | `interface()` doesn't survive symbols | T2 | symbolic smoke construction at registration — catches validation that leaked into `__init__` |
| E7 | the design re-declares types instead of consuming the interface | T4 | the first N `Runtime` fn_args must be the *same objects* as the declared members |
| E8 | `reference()` arity disagrees with the `In` members | T2 | signature check |
| E9 | `tuning()` sets a field that doesn't exist, or a non-`Tuning` one | **T1** | `dataclasses.replace` return type; pyright |
| E10 | one operator instance bound to two different value handles | T2 (graph build) | recorded per instance; error explains one-symbol-per-design |
| E11 | a `HostResident` never written before dispatch | T6 | sync-time check on the handle |
| E12 | no legal tuning for this shape/device | T3 | `Untunable`, raised by `tuning()` |
| E13 | a `GeneratedSequence` packaged into an `Elf` | **T1** | `Elf.__init__(self, overlay, sequence: StaticSequence)`; pyright |
| E14 | `Overlay`/`Sequence` built before `specialize()` | T3/T4 | state machine on the base class |
| E15 | a declared tensor never forwarded to `Runtime` | T4 | fn_args inspection |
| E16 | an `Out` never drained, an `In` never filled | T4 | sequence inspection |
| E17 | DMA addresses past the end of a declared buffer | T4 | `access_order()` max vs `prod(shape)` |
| E18 | part of an `Out` never written | T4 | `access_count() == 0` — silent garbage |
| E19 | part of an `In` never read | T4 | `access_count() == 0` |
| E20 | an `Out` written twice | T4 | `access_count() > 1` |
| E21 | wrong type / missing arg / bogus kwarg at construction | T1 | pyright on real dataclass fields |
| E22 | the kernel computes the wrong thing | T6 | `reference()` — the only oracle |
| E23 | a sequence composed against an overlay it does not match | T5 | §6 ABI comparison; names the disagreeing **binding or symbol**, not a hash |
| E24 | `Elf` on NPU1 | T5 | `Elf.__init__`, from `overlay.device` |
| E25 | `Inline()` and `CtrlPkt()` requested together | T4 | mutually exclusive aiecc flags |
| E26 | a `SequenceResident` declared but never forwarded to `Runtime` | T4 | inherited: `_DispatchParameter._bind` |
| E27 | a `GeneratedSequence` whose lowering leaves >1 runtime sequence | T4 | inherited: `_check_runtime_sequence_abi`, re-raised naming the sequence |
| E28 | `Compare` handed a multi-step sequence | T1 | its constructor takes a list of sequences |
| E29 | a `via=Shim(...)` constraint the design didn't honour | T4 | read `input_with_addresses.mlir` back; compare to the declared constraint |
| E30 | `via=Shim(channel=2)` — past the hardware limit | T2 | 2 per direction per shim tile, from the target model. **Unvalidated today at any layer** |
| E31 | more shim endpoints than the device has | T3 | `get_shim_dma_limit` — already exists, already used; extend to the graph |

T4 uses `TensorAccessPattern`'s `tensor_dims`, `offset`, `sizes`, `strides`,
`access_order()`, `access_count()` (per-element touch count) and
`compare_access_orders()` (`aie/helpers/taplib/tap.py`).

T4 runs on every build unless disabled: `compile(check=False)`, with a size
threshold that degrades to bounds-checking-only for very large buffers
(`access_count()` materialises a buffer-sized array — llama's 2048-padded
attention buffers × 32 heads is real build time). See O3.

**E4 is worth calling out.** "Shapes must not depend on tuning" is usually a
convention people violate quietly. Running the symbolic probe twice under
different tuning and comparing turns it into a mechanical check that costs
microseconds.

**E9, E13 and E28 are T1** as a direct result of §3's `replace()` and §10's
constructor signatures — each was a runtime check in an earlier draft. That is
the payoff of priority 15.

**E29–E31 are the §6 rows**, and E30 catches a real gap: nothing in IRON or
mlir-aie validates a pinned channel against the 2-per-direction limit today, and
there are zero call sites to have noticed.

**Not enforceable without a test:** the math (E22), and access *order* — coverage
can be complete while the permutation is wrong. `compare_access_orders()` helps
where a fill and a drain should correspond, but it is not general.

---

## 16. Measurements taken

Probe at `/scratch/ehunhoff/spelling_probe/` (separate venv; `ironenv`
untouched, per requirements.txt drift risk).

**Spelling vs type checkers.** mlir-aie uses pyright,
`typeCheckingMode: "standard"`; IRON configures no checker today.

| spelling | pyright std | pyright strict | mypy --strict |
|---|---|---|---|
| `In[M, K]`, free names | 7 errors | — | — |
| `Annotated[Tensor, Shape[M,K]]`, free names | 7 errors | — | — |
| `In[M, K]`, module-level Dims | clean | clean | 33 errors |
| `Annotated[In, Shape[M,K]]`, module Dims | clean | clean | clean |
| `In[M, K]` + config suppression | clean | clean | n/a |

Suppression does **not** leak: a normal module still reports undefined names.
Strict is *better* than standard here — same result, more call-site checking.
All of this is why the annotation approach was *viable*; §3 is why it lost
anyway.

**Synthesised dataclass fields — the decisive one.** Measured: pyright reports
`No parameter named "M"` on **valid** calls. `@dataclass_transform` does not help
(PEP 681 infers from class-body annotations). Worse than unchecked. This is what
forces real, hand-written dataclass fields in §3.

**Resolver for the annotation approach.** ~90 lines; classification, evaluation,
inference, error messages. Two findings from building it, both of which are
*dissolved* rather than solved by putting the declaration in a method body:

- Annotations must be evaluated one at a time — evaluating them together forces
  `(N,K) if b_col_maj else (K,N)` while `b_col_maj` is still symbolic.
- A parameter a shape *branches* on cannot be symbolic; a forced symbol names
  itself, drops to its default and retries.

---

## 17. Authoring

The operator model is invisible from here, and so are the artifacts until you ask
for a specific composition.

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

decode = g.build()
net = decode.compile(dev)            # composes the §10 defaults
net[x] = embed(token); net[offset] = n * cfg.head_dim; net()
probs = net[logits]
```

No strings. `capture(model)` learns `id(tensor) -> name` from
`named_parameters()`, so a parameter *is* its handle. Every intermediate is
undeclared — `infer_buffer_offsets` already pools by live range, which deletes
`AIEPrefillBuffers` (~70 lines of `XRTTensor`/`subview`).

Prefill differs by passing the matmul class in (`def ffn(g, blk, x, mm=GEMV)`),
which also turns the `.T` layout disagreement into `GEMM.tuned(b_col_maj=True)`
and deletes `_upload(k_major=...)`.

Not llama-shaped: a CNN is `g(Conv2D, net.conv1.weight, x)` in the same graph,
same allocator, same handles.

`decode.compile(dev)` is three lines of library code over the primitives, and a
user who wants something else writes those three lines:

```python
ov          = Overlay(decode, dev)
decode_net  = Xclbin(ov, StaticSequence(ov, decode.steps)).load(dev)
prefill_net = Xclbin(ov, StaticSequence(ov, prefill.steps)).load(dev)   # same overlay
```

The second form is what makes E23 meaningful, and it is the shape L2 would slot
into without an API change.

---

## 18. What this deletes

**From today's tree:** `arg_spec`, `bind()`, `arg_spec_snapshot.json`, the
`L3_*_ty` re-declarations, `*_parameter="string"` kwargs, and the whole
`SequenceDispatch` hierarchy — `AutoDispatch`, `FusedDispatch`,
`SeparateDispatch`, `CompareDispatch`, `ReferenceDispatch`, `_DISPATCH_ALIASES`,
and `full_elf_path(seq)`'s "however it got built" escape hatch.

**From the annotation draft:** deferred annotations · `localns` evaluation · free
names in annotations · module-level `Dim`s · the `In[...]` vs
`Annotated[In, Shape[...]]` question · pyright suppression in pyrightconfig · the
`dims()` import · evaluating annotations one at a time · branch-parameter retry ·
rank-directed branch resolution · synthesise-vs-verify the field list ·
`@operator` reading a design signature.

**From the `Deployment` draft:** the `Deployment` record, its four string-valued
axes, its five presets, its eight-row legality table; the `Scalar`/`Extent`/
`Shape` role taxonomy; and the lazy-compile/`Frozen()` deopt machinery.

**Kept throughout:** `Tuning[T]` as an IRON-local marker (now a *field*
annotation), the tuning policy and `Untunable`, per-device numbers from the
target model, the un-flattening, the capture/handle authoring surface, and the T4
coverage checks.

**Cost.** The `__setattr__` hook is magic where an annotation is declarative; the
design diverges from upstream's `In`/`Out` convention (§8) with a real
consequence for `SequenceResident` (§11); `interface()` is structurally a method
returning the spec — which was objected to early on, though the objection was to
a *parallel* declaration and here the design consumes it (E7 makes that
mechanical). And the primitives are more to learn than `dispatch="fused"` for a
user who only ever wants the default — mitigated only by `decode.compile(dev)`
being genuinely the common path.

---

## 19. Sequencing

| step | what | blocks |
|---|---|---|
| **0a** | spike Ca: two-op fused graph, `full_elf=False` + `--expand-load-pdis`, opcode-3 dispatch | §10–§12 |
| **0b** | spike Cb: the two greps, then the shim | `GeneratedSequence` being real |
| 1 | `interface()` + `__setattr__` + `replace()`-based `tuning()` + E1–E9, on GEMV alone | — |
| 2 | the design consumes the interface (E7), deleting `arg_spec` for GEMV | — |
| 3 | `Overlay.bindings/residents/sizes` published and checked (§6, E23/E29–E31) — **standalone value even if everything else slips**; it would have caught the `mm_prebuilt` mismatch | — |
| 4 | `Sequence`/`Image`/harnesses, reproducing A and B exactly, 745/3165 baselines held | 5 |
| 5 | Ca and `chunks(n)`, if 0a said yes | 7 |
| 6 | remaining operators (O6), then llama rewritten against the capture surface | — |
| 7 | Cb, measured; `project-dispatch-bridge-not-applicable` revised or confirmed | — |

Steps 0a/0b, 1–2, and 3 touch disjoint files and can proceed in parallel. Per
`project_parallel_work_constraints`, the NPU device and the build dirs are the
only contention points — 0a/0b need the device, 1–3 do not.

Step 3 is worth calling out: it needs no new toolchain feature, reads files IRON
already opens, and pays for itself the first time two sequences share an overlay.

---

## 20. Open questions

- **O1. Does `interface()` assign to `self`, or return a list?** Assignment is
  the only stringless route to *names*, and names are what make the E-messages
  good. Returning a list needs no hook but numbers the members.
- **O2. Does `__init__` validate at all?** It must tolerate symbols, so probably
  not — everything moves to `specialize()`. A behaviour change for anyone relying
  on `GEMV(M=7)` raising immediately.
- **O3. T4 opt-out and size threshold.** `compile(check=False)` is the obvious
  home. What is the threshold, and is it per-operator or global?
- **O4. Accept the divergence from upstream's design signature (§8)?** §11 makes
  it concrete: it forces the (a)/(b)/(c) choice. Recommendation (c) is an
  upstream ask.
- **O5. Prefill scope.** ~300 lines of CPU/NPU ping-pong need real operators
  (masked softmax, attention context matmul, cache concat). Larger than the
  authoring rewrite. Sequence it after decode?
- **O6. Pilot operator and conversion order.** GEMV first; then what?
- **O7. Branch or worktree**, to keep the 745 / 3165 baselines undisturbed.
- **O8. Is L2 worth filing upstream?** `--sequence-name` and `--device-name`
  exist but are unused from Python. L3 covers llama's case; L2 matters for graphs
  where the *structure* changes but the overlay does not. Needs a second consumer
  before filing.
- **O9. Does `Tuning[T]` still want upstreaming** now that it is a field
  annotation rather than a design-signature one? It is a genuine gap next to
  `CompileTime`.
- **O10. How much default is too much?** `decode.compile(dev)` hides four
  constructor calls. Should it report what it composed under `verbose`?
- **O11. Should a `GeneratedSequence` with zero `SequenceResident` values be
  allowed?** Coherent, and the cheapest form of step 0b, but strictly slower than
  static in production. Allow-and-warn, or reject outside tests?
- **O12. Where does `chunks(n)` live** — on `Graph`, or a free function over
  `.steps`? A method invites "what's the right n", which has no general answer.
- **O13. `flm/gemm` README line 58** claims A broadcasts from shim columns
  0/2/4/6. True today, pinned by nothing, and the placer sorts by fifo name.
  Correct the doc or add the pin — independent of this plan, but someone will
  rely on it.
- **O14. Does `via=` belong on the interface at all,** given that pinning
  constrains routing for everything else and `flm/gemm` has zero placement slack?
  The weaker version — publish and check, never constrain — is most of the value
  at none of the risk. Decide after step 3.
- **O15. Verify the shim BD wrap/stride caps** in the target model before
  promising them to `tuning()` (§4). The `MAX_WRAP = 1023` FIXME depends on it.

---

## 21. Looked at and dismissed

| option | why not |
|---|---|
| Shape annotations on the design signature | the scope problem and everything in §18's second list; retained as the fallback if `__setattr__` collection proves worse than expected. §16 has the measurements |
| `Layer` + backend + `using()` + `infer` (exists on `ehunhoff/graph-capture-frontend`, incl. a 67-line `llama_model.py` and `iron/nn/`) | too much machinery; indirection the declaration model removes |
| `forward()` on the model tree | llama-shaped; `iron/models/llama.py` is deliberately parameters-only |
| Central `iron.shapes` registry of dim names | a global namespace of every dim any operator might use, edited per new operator |
| Module-level `M, K = dims(...)` per design module | works (measured clean) but names each dim three times |
| `Annotated[In, Shape[M,K]]` | only buys mypy, which nobody here runs |
| Per-arg lambda `In[lambda p: (p.M, p.K)]` / `@shapes` decorator | noisy; a deferred annotation *is* a lambda over a namespace, so this was the same mechanism spelled explicitly |
| `declare()` in the body + sentinel exception | control flow by exception |
| String dim names `In["M", "K"]` | conditionals inexpressible; strings |
| Reading `A.shape` inside the design | upstream `_TensorPlaceholder` poisons attribute access on purpose |
| A general inverse shape solver | no precedent in torch/JAX/ONNX/MLIR — all go params→shapes. Reframed as lazy specialization (`LazyLinear`, `flax.linen.Dense`) |
| Symbolic unification of the existing `arg_spec` | superseded: the declaration *is* the symbolic form |
| Einops-style shape DSL | GEMM's own docstring: "any shape-expression language able to express it would have become Python again" |
| Killing GEMV's `num_batches` conditional | unnecessary — conditionals work in a method body (§3) |
| interface-then-`yield` in the design body | same scope fix, but adds a generator protocol, a purity rule for the pre-yield prefix, and drops tensor params from the signature |
| Synthesised dataclass fields | measured in §16 — pyright rejects *valid* calls; `dataclass_transform` does not help |
| Per-call-site runtime values | not implementable: one scratchpad symbol per design; distinct symbols mean distinct designs |
| Two markers for scratchpad values (offset vs core-read) | same object, same mechanism; the distinction is in the design's use |
| Naming the tiers by role (`Scalar`/`Extent`/`Shape`) | abstractions over what the design does with a value; `shape` collides with flm.GEMM, and none of the three says what a change costs. §9 names the rebuilt artifact instead |
| Lazy compile + observe-and-deopt | `compile()` silently recompiling mid-run is the opposite of priority 13. Inference belongs only in the JIT path, where the call *is* the entry point |
| Keeping one `dispatch=` string | the combinations are a product, not a list, and partial fusion is not in the product at all. `"fused"` already means two different things depending on the device |
| A `Deployment` record with typed axes and presets | still enumerates blessed combinations; still cannot express `chunks(8)`; needed an eight-row legality table for facts two constructor signatures now carry |
| `Deployment` as a policy class hierarchy (today's `SequenceDispatch`) | scatters one matrix across five classes, and makes every error message a local decision |
| Comparing overlay/sequence **hashes** for compatibility | too crude in both directions — irrelevant differences fail, and a moved RTP reader passes. §6 compares the ABI |
| `DispatchTime[T]` as the mechanism for llama's `cache_offset` | it regenerates the whole stream; a scratchpad write is a few words. It is now `SequenceResident` and is an *option*, measured as config Cb (§12), not the default |
| Treating `SequenceResident` as a special parameter kind | it is an argument to a `GeneratedSequence` |
| Leaving `has_dispatch` as the gate | makes "which kind of sequence is this" an inference rather than a decision |
| `tuning()` returning a `dict` | string keys, no pyright, and a runtime check for what `replace()` catches in the editor |
| Exposing raw aiecc flags on the primitives | `--expand-load-pdis` is not tuning — without it the program links and hangs. `Inline()` carries the meaning, not the flag |
| `compare`/`reference` as dispatch modes | `compare` needs a boundary after every step, `reference` needs no device; both are structural facts their constructors now state |

---

## 22. Carried risk, unrelated to this work

**NPU decode output degrades after a few tokens** versus `llama_cpu.py` on the
same prompt and seed. Prefill reproduces exactly and the first tokens agree, then
the NPU drifts.

Not the weight-naming refactor — uploaded bytes are `torch.equal` for all 146
parameters. Predates observation; `llama_npu.py` could not run on this host until
XRT 2.26. `iron/applications/llama_3.2_1b/test.py` asserts only
`returncode == 0`, so it does not catch this, and **a rewritten llama will
inherit it and look guilty.**

Decision taken: snapshot the current token stream as a before/after artifact and
proceed. Cheapest real probe if revisited: compare NPU vs CPU *logits* for one
decode step rather than sampled tokens.
