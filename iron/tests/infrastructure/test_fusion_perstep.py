# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A stream fusion in ``PerStep`` packaging.

Its steps link as one ``FusedDesign`` (``iron.common.image.link``), one xclbin
dispatched once with every member's buffers and per-call values. No toolchain and no NPU
below the "On the device" and "npu1: device-free" section markers.

To run this module's real npu1 dispatch tests on a Phoenix host
(xcoradaie203 or xcoradaie205), once mlir-aie and IRON are built there and
XRT is sourced::

pytest iron/tests/infrastructure/test_fusion_perstep.py -v

They carry no device fixture, so the current device is whatever the attached
runtime reports (``aie_utils.get_current_device()``'s probe, as
``iron/tests/operators/test_catalog.py``'s tests do), and ``supported_devices``
gates them to run only where the attached NPU matches. The device-free npu1
tests (bound in software, no chip needed) run anywhere::

pytest iron/tests/infrastructure/test_fusion_perstep.py -k npu1 -v

The rest of this module (npu2-forced dispatch, device-free compiles, Llama
candidates) runs on any host with aiecc and Peano installed; only the tests
under "On the device" dispatch, and need an attached NPU.
"""

from pathlib import Path

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

from iron import Profile
from iron.applications.llama import Llama
from iron.common.graph.fusion import candidates
from iron.common.graph.record import Recording
from iron.common.image.callable import PerStepCallable
from iron.common.image.link import FusedDesign, PerStep
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef, Edge, Fusion, FusionKind
from iron.common.testing import vectors
from iron.lm.testing import require
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.silu import SiLU
from iron.tests.support import sequences
from iron.tests.support.graphs import Chain
from iron.tests.support.llama_model import llama_1b

LLAMA_1B_WEIGHTS = Path("/scratch/ehunhoff/iron-next/weights-220/llama3.2-1b")


def _fuse(producer: int, output: str, input: str) -> Fusion:
    return Fusion(
        FusionKind.STREAM,
        (producer, producer + 1),
        (Edge(producer, output, producer + 1, input),),
    )


def _silu_mul(size, cols, tile, **extra):
    silu = SiLU(size=size, num_aie_columns=cols, tile_size=tile, **extra)
    mul = ElementwiseMul(size=size, num_aie_columns=cols, tile_size=tile, **extra)
    return silu, mul


def _silu_mul_recording(name, silu, mul):
    steps = sequences.steps((silu, "x", "mid"), (mul, "mid", "up", "out"))
    return Recording.of_steps(name, steps, ["x", "up"], ["out"])


def _gemv_add():
    # Llama decode's own profile tunables for M=2048, K=2048.
    gemv = GEMV(M=2048, K=2048, tile_size_input=4, tile_size_output=256)
    add = ElementwiseAdd(size=2048, tile_size=256)
    return gemv, add


def _gemv_add_recording(name, gemv, add):
    steps = sequences.steps((gemv, "A", "B", "mid"), (add, "r", "mid", "out"))
    return Recording.of_steps(name, steps, ["A", "B", "r"], ["out"])


def _gemv_silu_mul():
    gemv = GEMV(M=2048, K=2048, tile_size_input=4, tile_size_output=2048)
    silu, mul = _silu_mul(2048, 1, 2048)
    return gemv, silu, mul


def _gemv_silu_mul_recording(name, gemv, silu, mul):
    steps = sequences.steps(
        (gemv, "A", "B", "mid1"), (silu, "mid1", "mid2"), (mul, "mid2", "up", "out")
    )
    return Recording.of_steps(name, steps, ["A", "B", "up"], ["out"])


def _three_step_fusion() -> Fusion:
    return Fusion(
        FusionKind.STREAM, (0, 1, 2), (Edge(0, "C", 1, "x"), Edge(1, "y", 2, "a"))
    )


# ---------------------------------------------------------------------------
# On the device, whichever is attached (npu1 or npu2): numpy and bit-equal
# to the same steps run unfused. No device fixture: the current device is
# whatever the runtime finds attached (aie_utils.get_current_device()'s
# probe_runtime=True), as iron/tests/operators/test_catalog.py's do; shapes
# are chosen to fit npu1's 4 columns as well as npu2's 8.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu1", "npu2")
@pytest.mark.parametrize("size,cols", [(2048, 1), (4096, 4)])
def test_silu_mul_fused_matches_reference_and_unfused(size, cols):
    tile = 1024

    def build(name, fusions):
        silu, mul = _silu_mul(size, cols, tile)
        img = Image(_silu_mul_recording(name, silu, mul), PerStep(), fusions=fusions)
        img.compile()
        return img.get_callable(), silu, mul

    fused_run, silu, mul = build(f"perstep_fused_{size}_{cols}", (_fuse(0, "y", "a"),))
    plain_run, _, _ = build(f"perstep_plain_{size}_{cols}", ())

    gate = vectors(silu).inputs["x"]
    up = vectors(mul, seed=7).inputs["b"]
    y_ref = np.asarray(mul.reference(silu.reference(gate), up))

    def dispatch(run):
        run.get_buffer(BufferRef("x")).numpy_view()[: gate.size] = gate.reshape(-1)
        run.get_buffer(BufferRef("up")).numpy_view()[: up.size] = up.reshape(-1)
        run()
        return run.get_buffer(BufferRef("out")).numpy()[:size].copy()

    out = dispatch(fused_run)
    baseline = dispatch(plain_run)

    tol = Tolerance.bf16_ulps(
        3,
        atol=mul.tolerance().atol,
        note="SiLU's 1 ulp through the multiply (2), plus both roundings",
    )
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail
    assert np.array_equal(
        out.view(np.uint16), baseline.view(np.uint16)
    ), "the fused and unfused per-step images differ"


@pytest.mark.supported_devices("npu1", "npu2")
def test_silu_mul_fused_per_call_bound_value():
    """Both operators' ``valid`` is a dispatch-time scalar (no scratchpad on an xclbin).

    The host writes each design's own symbol, the fused kernel declaring both members'
    as its own ``dispatch_params``.
    """
    size, cols, tile = 2048, 1, 1024
    silu, mul = _silu_mul(size, cols, tile, bound_values={"valid": None})
    img = Image(
        _silu_mul_recording("perstep_bound_valid", silu, mul),
        PerStep(),
        fusions=(_fuse(0, "y", "a"),),
    )
    img.compile()
    run = img.get_callable()
    assert isinstance(run, PerStepCallable)
    (kernel,) = [k for _, k, _, _ in run._steps]
    assert any(s.startswith("SiLU") for s in kernel.dispatch_params)
    assert any(s.startswith("ElementwiseMul") for s in kernel.dispatch_params)

    gate = vectors(silu).inputs["x"]
    up = vectors(mul, seed=7).inputs["b"]
    run.get_buffer(BufferRef("x")).numpy_view()[: gate.size] = gate.reshape(-1)
    run.get_buffer(BufferRef("up")).numpy_view()[: up.size] = up.reshape(-1)
    values = {}
    for op in (silu.resolved(), mul.resolved()):
        for v in op.values:
            values[v.symbol] = np.int32(
                size if v.derive is None else op.derived_at(v.name, valid=size)
            )
    run.write_values(values)
    run()
    out = run.get_buffer(BufferRef("out")).numpy()[:size].copy()

    y_ref = np.asarray(mul.reference(silu.reference(gate), up))
    tol = Tolerance.bf16_ulps(
        3, atol=mul.tolerance().atol, note="shared valid, every element live"
    )
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail


# ---------------------------------------------------------------------------
# On the device, npu2: GEMV fusions.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu2")
def test_gemv_to_elementwiseadd_fused_matches_reference_and_unfused(npu2):
    """Llama decode's GEMV(M=2048, K=2048) -> ElementwiseAdd residual add, fused on one xclbin.

    Holds to the operators' references fused and is bit-equal to the same two steps run
    unfused.
    """

    def build(name, fusions):
        gemv, add = _gemv_add()
        img = Image(_gemv_add_recording(name, gemv, add), PerStep(), fusions=fusions)
        img.compile()
        return img.get_callable(), gemv, add

    fused_run, gemv, add = build("gemv_add_fused", (_fuse(0, "C", "b"),))
    plain_run, _, _ = build("gemv_add_plain", ())

    A = vectors(gemv).inputs["A"]
    B = vectors(gemv).inputs["B"]
    r = vectors(add, seed=7).inputs["a"]
    y_ref = np.asarray(add.reference(gemv.reference(A, B), r))

    def dispatch(run):
        run.get_buffer(BufferRef("A")).numpy_view()[:] = A.reshape(-1)
        run.get_buffer(BufferRef("B")).numpy_view()[:] = B.reshape(-1)
        run.get_buffer(BufferRef("r")).numpy_view()[:] = r.reshape(-1)
        run()
        return run.get_buffer(BufferRef("out")).numpy()[:2048].copy()

    out = dispatch(fused_run)
    baseline = dispatch(plain_run)
    verdict = compare(out, y_ref, gemv.tolerance())
    assert verdict, verdict.detail
    assert np.array_equal(out.view(np.uint16), baseline.view(np.uint16))


@pytest.mark.supported_devices("npu2")
def test_three_step_fusion_matches_reference_and_unfused(npu2):
    """GEMV -> SiLU -> ElementwiseMul, all three fused into one xclbin.

    Holds to the operators' references fused and is bit-equal to the same three steps
    run unfused.
    """

    def build(name, fusions):
        gemv, silu, mul = _gemv_silu_mul()
        img = Image(
            _gemv_silu_mul_recording(name, gemv, silu, mul), PerStep(), fusions=fusions
        )
        img.compile()
        return img.get_callable(), gemv, silu, mul

    fused_run, gemv, silu, mul = build("three_step_fused", (_three_step_fusion(),))
    plain_run, _, _, _ = build("three_step_plain", ())

    A = vectors(gemv).inputs["A"]
    B = vectors(gemv).inputs["B"]
    up = vectors(mul, seed=7).inputs["b"]
    y_ref = np.asarray(mul.reference(silu.reference(gemv.reference(A, B)), up))

    def dispatch(run):
        run.get_buffer(BufferRef("A")).numpy_view()[:] = A.reshape(-1)
        run.get_buffer(BufferRef("B")).numpy_view()[:] = B.reshape(-1)
        run.get_buffer(BufferRef("up")).numpy_view()[: up.size] = up.reshape(-1)
        run()
        return run.get_buffer(BufferRef("out")).numpy()[:2048].copy()

    out = dispatch(fused_run)
    baseline = dispatch(plain_run)
    tol = Tolerance.bf16_ulps(
        3,
        atol=mul.tolerance().atol,
        note="GEMV's accumulation and SiLU's 1 ulp through the multiply, "
        "plus both roundings",
    )
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail
    assert np.array_equal(out.view(np.uint16), baseline.view(np.uint16))


# A pack of two Copies of one design, each writing its own row into its own
# buffer at one per-call offset: Llama decode's K- and V-cache writes.
ROW, SLOTS = 64, 4


def _cache_write():
    write = Copy(
        input_buffer_size=ROW,
        src=TensorAccessPattern((ROW,), 0, [1, 1, 1, ROW], [0, 0, 0, 1]),
        output_buffer_size=SLOTS * ROW,
        dst=TensorAccessPattern((SLOTS * ROW,), 0, [1, 1, 1, ROW], [0, 0, 0, 1]),
        dtype=np.int32,
    )
    write.use_value("out_offset")
    return write


def _cache_writes_recording(name, k, v):
    steps = sequences.steps((k, "xk", "ck"), (v, "xv", "cv"))
    return Recording.of_steps(name, steps, ["xk", "xv"], ["ck", "cv"])


def test_packed_members_of_one_design_take_their_own_dispatch_parameters(npu2):
    """Two Copies of one design share their per-call symbol.

    As one graph value drives both; a fused xclbin binds a dispatch parameter in one
    runtime, so each member takes its own, written from that symbol.
    """
    k, v = _cache_write().resolved(), _cache_write().resolved()
    (symbol,) = {val.symbol for op in (k, v) for val in op.values}
    design = FusedDesign(Fusion(FusionKind.PACK, (0, 1)), [k, v])
    assert design.symbols == {f"{symbol}_0": symbol, f"{symbol}_1": symbol}
    design.module(**{name: 0 for name in design.symbols})


def test_a_pack_of_projections_on_a_shared_xclbin_builds_per_step(npu2):
    """Llama 1B's prompt q/k/v projections (flm.ProjectionGEMM) each run their configuration's xclbin alone; packed.

    The fused design builds each one's own array, as a full ELF does.
    """
    model = llama_1b(num_hidden_layers=1)
    prompt = model.record(**model.shapes()[1])
    pack = next(
        f
        for f in candidates(prompt, (FusionKind.PACK,))
        if len(f.steps) == 3
        and all(type(prompt.steps[i].op).__name__ == "ProjectionGEMM" for i in f.steps)
    )
    ops = [prompt.steps[i].op.resolved() for i in pack.steps]
    assert all(op.xclbin_operator() is not op for op in ops)
    design = FusedDesign(Fusion(FusionKind.PACK, (0, 1, 2)), ops)
    design.module(**{name: 0 for name in design.symbols})


@pytest.mark.supported_devices("npu2")
def test_packed_cache_writes_match_reference_and_unfused(npu2):
    """The pack of two cache writes, one per-step dispatch, lands each row in its own buffer's slot at every offset, bit-equal to the writes apart."""

    def build(fusions):
        k, v = _cache_write(), _cache_write()
        image = Image(
            _cache_writes_recording("perstep_cache_writes", k, v),
            PerStep(),
            fusions=fusions,
        )
        image.compile()
        return image.get_callable(), k.resolved()

    packed_run, k = build((Fusion(FusionKind.PACK, (0, 1)),))
    plain_run, _ = build(())
    (symbol,) = {val.symbol for val in k.values}
    rng = np.random.default_rng(5)
    expected = {
        name: np.full((SLOTS, ROW), -1, dtype=np.int32) for name in ("ck", "cv")
    }
    for run in (packed_run, plain_run):
        for name in ("ck", "cv"):
            run.get_buffer(BufferRef(name)).numpy_view()[:] = -1
            run.get_buffer(BufferRef(name)).to("npu")
    for slot in (2, 0, 3):
        rows = {
            "xk": rng.integers(-(2**31), 2**31 - 1, ROW, dtype=np.int32),
            "xv": rng.integers(-(2**31), 2**31 - 1, ROW, dtype=np.int32),
        }
        expected["ck"][slot], expected["cv"][slot] = rows["xk"], rows["xv"]
        got = []
        for run in (packed_run, plain_run):
            for name, row in rows.items():
                run.get_buffer(BufferRef(name)).numpy_view()[:ROW] = row
            run.write_values({symbol: np.int32(slot * ROW)})
            run()
            got.append(
                {
                    name: run.get_buffer(BufferRef(name)).numpy()[: SLOTS * ROW]
                    for name in ("ck", "cv")
                }
            )
        packed, plain = got
        for name in ("ck", "cv"):
            assert np.array_equal(
                packed[name].reshape(SLOTS, ROW), expected[name]
            ), f"slot {slot}: {name} holds the wrong rows"
            assert np.array_equal(packed[name], plain[name]), f"{name} differs apart"


# ---------------------------------------------------------------------------
# On the device, whichever is attached: a graph, not just a hand-built Image.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu1", "npu2")
def test_small_graph_compiled_per_step_with_a_named_fusion_is_bit_equal():
    """``Chain`` (add, silu, mul, add, silu) compiled ``full_elf=False``.

    A profile naming its silu -> mul fusion (steps 1, 2), is bit-equal to the same graph
    compiled without one: a profile reaches a per-step image too. ``columns=1`` fits
    npu1's 4 columns as well as npu2's 8.
    """
    size, tile, cols = 2048, 2048, 1
    rng = np.random.default_rng(0)
    a = rng.standard_normal(size).astype(np.float32).astype(bfloat16)
    b = rng.standard_normal(size).astype(np.float32).astype(bfloat16)

    unfused = Chain(size=size, tile=tile, columns=cols).compile(
        full_elf=False, check=False, a=(size,), b=(size,)
    )
    assert unfused.sequence.fusions == ()
    out_unfused = np.asarray(unfused(a, b))

    profile = Profile()
    profile.add_fusion(
        FusionKind.STREAM,
        [(SiLU, dict(size=size)), (ElementwiseMul, dict(size=size))],
        [(0, "y", 1, "a")],
    )
    graph = Chain(size=size, tile=tile, columns=cols)
    graph.profile = profile
    fused = graph.compile(full_elf=False, check=False, a=(size,), b=(size,))
    assert len(fused.sequence.fusions) == 1
    out_fused = np.asarray(fused(a, b))

    assert np.array_equal(
        out_fused.view(np.uint16), out_unfused.view(np.uint16)
    ), "a named fusion changed the per-step image's output"


# ---------------------------------------------------------------------------
# npu1: device-free (bound, not attached): the same fusions compile.
# ---------------------------------------------------------------------------


def test_silu_mul_fusion_builds_an_xclbin_per_fused_step_on_npu1(npu1):
    silu, mul = _silu_mul(2048, 1, 1024)
    img = Image(
        _silu_mul_recording("npu1_silu_mul", silu, mul),
        PerStep(),
        fusions=(_fuse(0, "y", "a"),),
    )
    img.compile()
    # One Design record per member (as a full ELF's fusion reports), both
    # naming the one xclbin the fused dispatch runs.
    assert len(img.artifacts.designs) == 2
    assert len({d.image for d in img.artifacts.designs}) == 1


def test_gemv_fusions_build_an_xclbin_per_fused_step_on_npu1(npu1):
    def build(fused_steps, recording_fn, ops_fn):
        img = Image(
            recording_fn("npu1_gemv", *ops_fn()), PerStep(), fusions=fused_steps
        )
        img.compile()
        return img

    build((_fuse(0, "C", "b"),), _gemv_add_recording, _gemv_add)
    build((_three_step_fusion(),), _gemv_silu_mul_recording, _gemv_silu_mul)


# ---------------------------------------------------------------------------
# npu1: Llama 3.2 1B's own fusion candidates, device-free.
# ---------------------------------------------------------------------------


def test_llama_1b_finds_its_fusion_candidates_on_npu1(npu1, record_property):
    """Llama 3.2 1B, random weights drawn in the real checkpoint's shapes (only its header is read).

    Records on npu1 with its own npu1 profile and finds the on-chip fusions
    ``candidates()`` admits: one SiLU -> Mul per layer in both the decode step and the
    prompt chunk (16 each, Llama 3.2 1B's layer count), the prompt chunk's also a Copy
    -> RMSNorm; GEMV -> ElementwiseAdd residual adds are recorded but not asserted, as
    GEMV is being edited concurrently.
    """
    require(
        LLAMA_1B_WEIGHTS / "config.json",
        LLAMA_1B_WEIGHTS / "model.safetensors",
        staged=False,
    )

    def load():
        model = Llama.from_checkpoint(str(LLAMA_1B_WEIGHTS), random_weights=0)
        decode_shapes, prompt_shapes = model.shapes()
        return model.record(**decode_shapes), model.record(**prompt_shapes)

    decode, prompt = load()

    def pairs(recording):
        return [
            (
                type(recording.steps[f.steps[0]].op.resolved()).__name__,
                f.edges[0].output,
                type(recording.steps[f.steps[1]].op.resolved()).__name__,
                f.edges[0].input,
            )
            for f in candidates(recording)
            if len(f.steps) == 2
        ]

    decode_pairs, prompt_pairs = pairs(decode), pairs(prompt)
    decode_silu_mul = [p for p in decode_pairs if p[0] == "SiLU"]
    prompt_silu_mul = [p for p in prompt_pairs if p[0] == "SiLU"]
    record_property("decode SiLU->Mul candidates", len(decode_silu_mul))
    record_property("prompt SiLU->Mul candidates", len(prompt_silu_mul))
    record_property(
        "decode GEMV->Add candidates", len([p for p in decode_pairs if p[0] == "GEMV"])
    )
    assert all(p == ("SiLU", "y", "ElementwiseMul", "a") for p in decode_silu_mul)
    assert len(decode_silu_mul) == 16  # Llama 3.2 1B's num_hidden_layers
    assert len(prompt_silu_mul) == 16
    assert ("Copy", "RMSNorm") in {
        (
            type(prompt.steps[f.steps[0]].op.resolved()).__name__,
            type(prompt.steps[f.steps[1]].op.resolved()).__name__,
        )
        for f in candidates(prompt)
        if len(f.steps) == 2
    }

    # One decode candidate builds to a per-step xclbin on npu1: compile, no
    # dispatch (no NPU attached here).
    pair = next(f for f in candidates(decode) if len(f.steps) == 2)
    Image(decode, PerStep(), fusions=(pair,)).compile()
