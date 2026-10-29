# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Image(fusions=...)``: a run of steps streamed on-chip into the next, all
running as one device configuration with no host transfer between them. No
toolchain and no NPU below ``test_fusion_device.py``'s line.
"""

import statistics

import numpy as np
import pytest
from aie import ir
from aie.utils.verify import Tolerance, compare

from iron.common.design import BuiltArray, OperatorDesign
from iron.common.graph.record import Recording
from iron.common.image.compose import CoResidenceError, Composition, places
from iron.common.image.link import FullELF, PerStep
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef, Edge, Fusion, FusionKind
from iron.common.testing import vectors
from iron.operators.clamp import Clamp
from iron.operators.copy import Gather
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.silu import SiLU
from iron.tests.support import sequences
from iron.tune.measure import Timing, time_interleaved

pytestmark = pytest.mark.usefixtures("npu2")


def _fuse(producer: int, output: str, input: str) -> Fusion:
    """A two-step stream fusion, as a ``Chain`` used to be spelled."""
    return Fusion(
        FusionKind.STREAM,
        (producer, producer + 1),
        (Edge(producer, output, producer + 1, input),),
    )


def _steps(silu, mul, mid):
    """SiLU's ``y`` and ElementwiseMul's ``a`` name ``mid``, the one fused."""
    return sequences.steps((silu, "x", mid), (mul, mid, "up", "out"))


def _silu_mul(size, cols, tile, **extra):
    silu = SiLU(size=size, num_aie_columns=cols, tile_size=tile, **extra)
    mul = ElementwiseMul(size=size, num_aie_columns=cols, tile_size=tile, **extra)
    return silu, mul


def _recording(name, silu, mul):
    return Recording.of_steps(name, _steps(silu, mul, "mid"), ["x", "up"], ["out"])


def _gemv_add(M, K, **extra):
    # Llama decode's own profile tunables for M=2048, K=2048.
    gemv = GEMV(M=M, K=K, tile_size_input=4, tile_size_output=256, **extra)
    add = ElementwiseAdd(size=M, tile_size=256, **extra)
    return gemv, add


def _gemv_add_steps(gemv, add, mid):
    """GEMV's ``C`` and ElementwiseAdd's ``b`` name ``mid``, the one fused."""
    return sequences.steps((gemv, "A", "B", mid), (add, "r", mid, "out"))


def _gemv_add_recording(name, gemv, add):
    return Recording.of_steps(
        name, _gemv_add_steps(gemv, add, "mid"), ["A", "B", "r"], ["out"]
    )


def _gemv_silu_mul(M, cols, tile, **extra):
    gemv = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=tile, **extra)
    silu, mul = _silu_mul(M, cols, tile, **extra)
    return gemv, silu, mul


def _gemv_silu_mul_steps(gemv, silu, mul, mid1, mid2):
    """GEMV's ``C`` feeds SiLU's ``x``, SiLU's ``y`` feeds ElementwiseMul's ``a``."""
    return sequences.steps(
        (gemv, "A", "B", mid1), (silu, mid1, mid2), (mul, mid2, "up", "out")
    )


def _gemv_silu_mul_recording(name, gemv, silu, mul):
    return Recording.of_steps(
        name,
        _gemv_silu_mul_steps(gemv, silu, mul, "mid1", "mid2"),
        ["A", "B", "up"],
        ["out"],
    )


def _three_step_fusion() -> Fusion:
    return Fusion(
        FusionKind.STREAM,
        (0, 1, 2),
        (Edge(0, "C", 1, "x"), Edge(1, "y", 2, "a")),
    )


# ---------------------------------------------------------------------------
# Device-free: the composed module.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("size,cols", [(2048, 1), (8192, 8)])
def test_fused_pair_is_one_device_configuration(size, cols):
    """A fused pair places as one device, which is one fewer ``aie.device``
    than the same two steps unfused; its identity differs too.
    """
    tile = 1024
    silu, mul = _silu_mul(size, cols, tile)
    fused = Image(
        _recording(f"fuse_struct_{size}_{cols}", silu, mul),
        FullELF(),
        fusions=(_fuse(0, "y", "a"),),
    )
    fused._prepare()
    fused_composition = Composition(fused)
    fused_text = fused_composition.text()
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(fused_text))
    assert diagnostic is None, diagnostic

    silu2, mul2 = _silu_mul(size, cols, tile)
    unfused = Image(_recording(f"unfuse_struct_{size}_{cols}", silu2, mul2), FullELF())
    unfused._prepare()
    unfused_text = Composition(unfused).text()

    assert (
        unfused_text.count("aie.device(") - fused_text.count("aie.device(") == 1
    ), "a fused pair should drop exactly one aie.device"


def test_fused_identity_differs_from_unfused():
    silu, mul = _silu_mul(2048, 1, 1024)
    fused = Image(
        _recording("fuse_identity_fused", silu, mul),
        FullELF(),
        fusions=(_fuse(0, "y", "a"),),
    )
    fused._prepare()
    silu2, mul2 = _silu_mul(2048, 1, 1024)
    unfused = Image(_recording("fuse_identity_unfused", silu2, mul2), FullELF())
    unfused._prepare()
    assert Composition(fused).identity != Composition(unfused).identity


def test_gemv_to_elementwiseadd_fused_pair_is_one_device_configuration():
    """GEMV.C -> ElementwiseAdd.b (Llama decode's residual adds) places as one
    device, as the Elementwise-only pair does: the generalization is not
    restricted to ``Elementwise``.
    """
    gemv, add = _gemv_add(2048, 2048)
    fused = Image(
        _gemv_add_recording("gemv_add_struct_fused", gemv, add),
        FullELF(),
        fusions=(_fuse(0, "C", "b"),),
    )
    fused._prepare()
    fused_composition = Composition(fused)
    fused_text = fused_composition.text()
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(fused_text))
    assert diagnostic is None, diagnostic

    gemv2, add2 = _gemv_add(2048, 2048)
    unfused = Image(
        _gemv_add_recording("gemv_add_struct_unfused", gemv2, add2), FullELF()
    )
    unfused._prepare()
    unfused_text = Composition(unfused).text()

    assert (
        unfused_text.count("aie.device(") - fused_text.count("aie.device(") == 1
    ), "a fused pair should drop exactly one aie.device"


def test_three_step_fusion_is_one_device_configuration():
    """GEMV -> SiLU -> ElementwiseMul, all three fused, drops two
    ``aie.device``s against the same steps unfused.
    """
    gemv, silu, mul = _gemv_silu_mul(2048, 1, 1024)
    fused = Image(
        _gemv_silu_mul_recording("three_step_struct_fused", gemv, silu, mul),
        FullELF(),
        fusions=(_three_step_fusion(),),
    )
    fused._prepare()
    fused_text = Composition(fused).text()
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(fused_text))
    assert diagnostic is None, diagnostic

    gemv2, silu2, mul2 = _gemv_silu_mul(2048, 1, 1024)
    unfused = Image(
        _gemv_silu_mul_recording("three_step_struct_unfused", gemv2, silu2, mul2),
        FullELF(),
    )
    unfused._prepare()
    unfused_text = Composition(unfused).text()

    assert (
        unfused_text.count("aie.device(") - fused_text.count("aie.device(") == 2
    ), "a three-step fusion should drop two aie.devices"


# ---------------------------------------------------------------------------
# Refusals.
# ---------------------------------------------------------------------------


def test_bad_step_index_refused():
    silu, mul = _silu_mul(2048, 1, 1024)
    recording = _recording("fuse_bad_index", silu, mul)
    with pytest.raises(ValueError, match="names no step"):
        Image(recording, FullELF(), fusions=(_fuse(1, "y", "a"),))


def test_wrong_buffer_names_refused():
    silu, mul = _silu_mul(2048, 1, 1024)
    with pytest.raises(ValueError, match="no drained buffer"):
        Image(
            _recording("fuse_bad_output", silu, mul),
            FullELF(),
            fusions=(_fuse(0, "nope", "a"),),
        )
    silu, mul = _silu_mul(2048, 1, 1024)
    with pytest.raises(ValueError, match="no filled buffer"):
        Image(
            _recording("fuse_bad_input", silu, mul),
            FullELF(),
            fusions=(_fuse(0, "y", "nope"),),
        )
    silu, mul = _silu_mul(2048, 1, 1024)
    split = Recording.of_steps(
        "fuse_split_roots",
        sequences.steps((silu, "x", "mid_a"), (mul, "mid_b", "up", "out")),
        ["x", "up"],
        ["out"],
    )
    with pytest.raises(ValueError, match="do not name one whole buffer"):
        Image(split, FullELF(), fusions=(_fuse(0, "y", "a"),))


def test_step_in_two_fusions_refused():
    silu, mul = _silu_mul(2048, 1, 1024)
    recording = _recording("fuse_double_claim", silu, mul)
    with pytest.raises(ValueError, match="is in two fusions"):
        Image(recording, FullELF(), fusions=(_fuse(0, "y", "a"), _fuse(0, "y", "a")))


def test_perstep_builds_fusions_but_check_refuses_them():
    """A per-step image links a fusion's steps as one xclbin
    (``iron.common.image.link.FusedDesign``); ``check=True`` still refuses,
    since it holds each step to its reference on its own dispatch."""
    silu, mul = _silu_mul(2048, 1, 1024)
    Image(
        _recording("fuse_perstep", silu, mul), PerStep(), fusions=(_fuse(0, "y", "a"),)
    )

    silu2, mul2 = _silu_mul(2048, 1, 1024)
    recording = _recording("fuse_perstep_check", silu2, mul2)
    with pytest.raises(ValueError, match="check=True"):
        Image(recording, PerStep(check=True), fusions=(_fuse(0, "y", "a"),))


def test_fusion_needs_at_least_two_steps():
    with pytest.raises(ValueError, match="at least two steps"):
        Fusion(FusionKind.STREAM, (0,), ())


def test_fusion_steps_must_be_increasing_and_distinct():
    with pytest.raises(ValueError, match="increasing and distinct"):
        Fusion(FusionKind.STREAM, (1, 0), ())
    with pytest.raises(ValueError, match="increasing and distinct"):
        Fusion(FusionKind.STREAM, (0, 0, 1), ())


def test_edge_skipping_a_non_member_step_refused():
    """An edge between two members may not skip a step between them that is
    not itself a member: that step would have to run on another device
    configuration, interleaved between the fusion's two halves.
    """
    with pytest.raises(ValueError, match="skips a step"):
        Fusion(FusionKind.STREAM, (0, 2), (Edge(0, "y", 2, "a"),))


def test_stream_fusion_edges_must_run_forward():
    with pytest.raises(ValueError, match="run forward"):
        Fusion(FusionKind.STREAM, (0, 1), (Edge(1, "y", 0, "a"),))


def test_fusion_input_fed_twice_refused():
    with pytest.raises(ValueError, match="fed twice"):
        Fusion(
            FusionKind.STREAM,
            (0, 1, 2),
            (Edge(0, "y", 2, "a"), Edge(1, "y", 2, "a")),
        )


def test_fan_out_representable_but_not_yet_buildable():
    """One producer output feeding two consumers' inputs is a valid
    ``Fusion``: the representation and its validation admit it. Building it
    (``Composition``) is not yet done, pending ``Operand.fifos()`` feeding
    more than one reader from one lane, so it raises a clear error instead
    of silently building something wrong.
    """
    fanout = Fusion(
        FusionKind.STREAM,
        (0, 1, 2),
        (Edge(0, "y", 1, "a"), Edge(0, "y", 2, "a")),
    )
    assert fanout.edges[0].producer == fanout.edges[1].producer == 0

    silu = SiLU(size=2048, num_aie_columns=1, tile_size=1024)
    mul1 = ElementwiseMul(size=2048, num_aie_columns=1, tile_size=1024)
    mul2 = ElementwiseMul(size=2048, num_aie_columns=1, tile_size=1024)
    recording = Recording.of_steps(
        "fan_out",
        sequences.steps(
            (silu, "x", "mid"),
            (mul1, "mid", "up1", "out1"),
            (mul2, "mid", "up2", "out2"),
        ),
        ["x", "up1", "up2"],
        ["out1", "out2"],
    )
    image = Image(recording, FullELF(), fusions=(fanout,))
    image._prepare()
    with pytest.raises(CoResidenceError, match="fan-out"):
        Composition(image).text()


def test_bind_refuses_a_fed_input():
    """A build that bound a fed input's own lanes, rather than reading them
    from ``fifos()``, would silently ignore the feed and hang; ``bind()``
    refuses it instead.
    """
    kwargs = dict(size=2048, num_aie_columns=1, tile_size=2048, low=0.0, high=1.0)
    producer = Clamp(**kwargs).resolved()
    consumer = Clamp(**kwargs).resolved()
    produced = BuiltArray(OperatorDesign(producer))
    (source,) = [b for b in produced.op.buffers if b.name == "y"]
    consumer.x.feed(source)
    view = consumer.layout()
    view.x.fed_from = consumer.x.fed_from
    with pytest.raises(ValueError, match="fifos"):
        view.x.bind(source.handles)


def test_feed_refuses_a_pinned_source():
    """``Gather`` pins its output to shim channels rather than streaming it
    through a fifo, so it cannot feed another operator on-chip.
    """
    gather = Gather(rows=8, table_rows=8, row=32, feeds=1).resolved()
    produced = BuiltArray(OperatorDesign(gather))
    (source,) = [b for b in produced.op.buffers if b.name == "y"]
    clamp = Clamp(
        size=32, num_aie_columns=1, tile_size=32, low=0.0, high=1.0
    ).resolved()
    with pytest.raises(ValueError, match="pinned"):
        clamp.x.feed(source)


def test_feed_refuses_a_lane_order_mismatch():
    """GEMV with ``num_batches`` streams ``C`` as one run per batch; a plain
    ElementwiseAdd of the same per-lane tile reads a single run, so lane 0's
    host access order differs, and ``feed`` names it.
    """
    gemv = GEMV(
        M=2048, K=64, num_batches=4, tile_size_input=4, tile_size_output=256
    ).resolved()
    add = ElementwiseAdd(size=2048, tile_size=256).resolved()
    produced = BuiltArray(OperatorDesign(gemv))
    (source,) = [b for b in produced.op.buffers if b.name == "C"]
    with pytest.raises(ValueError, match="lane 0"):
        add.b.feed(source)


# ---------------------------------------------------------------------------
# On the device.
# ---------------------------------------------------------------------------


@pytest.mark.supported_devices("npu2")
def test_fused_matches_reference_and_unfused():
    """silu(gate) * up fused on-chip holds to the operators' references
    fused, and is bit-equal to the same two steps run unfused.
    """
    size, cols, tile = 2048, 1, 1024

    def build(fusions):
        silu, mul = _silu_mul(size, cols, tile)
        img = Image(_recording("fuse_device", silu, mul), FullELF(), fusions=fusions)
        img.compile()
        return img.get_callable(), silu, mul

    fused_run, silu, mul = build((_fuse(0, "y", "a"),))
    plain_run, _, _ = build(())

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

    # A 1-ulp intermediate becomes at most 2 ulps of the product, plus half an
    # ulp for each of the device's and the reference's rounding.
    tol = Tolerance.bf16_ulps(
        3,
        atol=mul.tolerance().atol,
        note="SiLU's 1 ulp through the multiply (2), plus both roundings",
    )
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail
    assert np.array_equal(
        out.view(np.uint16), baseline.view(np.uint16)
    ), "the fused and unfused devices differ"


@pytest.mark.supported_devices("npu2")
def test_fused_per_call_shared_value():
    """Both operators' ``valid`` bound to one graph value share one scratchpad
    word (``FullELF.shared_words``), which the device still reads correctly.
    """
    size, cols, tile = 2048, 1, 1024
    silu, mul = _silu_mul(size, cols, tile, bound_values={"valid": None})
    # "valid" bounds each core's trip count only through "count", derived from
    # it; that is the word a core reads, and the one the two operators share.
    shared = {
        silu.value("count").symbol: "fuse_count",
        mul.value("count").symbol: "fuse_count",
    }
    img = Image(
        _recording("fuse_device_per_call", silu, mul),
        FullELF(shared_words=shared),
        fusions=(_fuse(0, "y", "a"),),
    )
    img.compile()
    assert (
        sum(p.name == "fuse_count" for p in img.artifacts.parameter_table) == 1
    ), "both operators' count should share one scratchpad word"

    # Every per-call word both operators declare, not just the shared one: a
    # bounded call still writes each buffer's own tile count.
    declared = img.artifacts.parameters
    words = {
        shared.get(v.symbol, v.symbol): np.int32(
            size if v.derive is None else op.derived_at(v.name, valid=size)
        )
        for op in (silu, mul)
        for v in op.values
    }

    run = img.get_callable()
    gate = vectors(silu).inputs["x"]
    up = vectors(mul, seed=7).inputs["b"]
    run.get_buffer(BufferRef("x")).numpy_view()[: gate.size] = gate.reshape(-1)
    run.get_buffer(BufferRef("up")).numpy_view()[: up.size] = up.reshape(-1)
    run.write_values({k: w for k, w in words.items() if k in declared})
    run()
    out = run.get_buffer(BufferRef("out")).numpy()[:size].copy()

    y_ref = np.asarray(mul.reference(silu.reference(gate), up))
    tol = Tolerance.bf16_ulps(
        3, atol=mul.tolerance().atol, note="shared valid, every element live"
    )
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail


@pytest.mark.supported_devices("npu2")
def test_gemv_to_elementwiseadd_matches_reference_and_unfused(record_property):
    """Llama decode's GEMV(M=2048, K=2048) -> ElementwiseAdd residual add,
    fused on-chip, holds to the operators' references fused and is
    bit-equal to the same two steps run unfused; also times both the
    tuner's way (``time_interleaved``: each image's calls run in turn within
    a round, so a round pays one hardware-context load per image rather
    than one per call), min and median over interleaved rounds.
    """
    M, K = 2048, 2048

    def build(fusions):
        gemv, add = _gemv_add(M, K)
        img = Image(
            _gemv_add_recording("gemv_add_device", gemv, add),
            FullELF(),
            fusions=fusions,
        )
        img.compile()
        return img.get_callable(), gemv, add

    fused_run, gemv, add = build((_fuse(0, "C", "b"),))
    plain_run, _, _ = build(())

    A = vectors(gemv).inputs["A"]
    B = vectors(gemv).inputs["B"]
    r = vectors(add, seed=7).inputs["a"]
    y_ref = np.asarray(add.reference(gemv.reference(A, B), r))

    def dispatch(run):
        run.get_buffer(BufferRef("A")).numpy_view()[:] = A.reshape(-1)
        run.get_buffer(BufferRef("B")).numpy_view()[:] = B.reshape(-1)
        run.get_buffer(BufferRef("r")).numpy_view()[:] = r.reshape(-1)
        run()
        return run.get_buffer(BufferRef("out")).numpy()[:M].copy()

    out = dispatch(fused_run)
    baseline = dispatch(plain_run)

    # GEMV's own tolerance (f32 accumulation) composed with ElementwiseAdd's
    # exact kernel: the sum's error is the product's.
    tol = gemv.tolerance()
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail
    assert np.array_equal(
        out.view(np.uint16), baseline.view(np.uint16)
    ), "the fused and unfused devices differ"

    fused_stats, unfused_stats = time_interleaved(
        [fused_run, plain_run], Timing(rounds=20), log=lambda _: None
    )
    record_property("Fused min us", min(fused_stats.samples_us))
    record_property("Fused median us", statistics.median(fused_stats.samples_us))
    record_property("Unfused min us", min(unfused_stats.samples_us))
    record_property("Unfused median us", statistics.median(unfused_stats.samples_us))


@pytest.mark.supported_devices("npu2")
def test_three_step_fusion_matches_reference_and_unfused():
    """GEMV -> SiLU -> ElementwiseMul, all three fused on-chip, holds to the
    operators' references fused and is bit-equal to the same three steps
    run unfused.
    """
    M, cols, tile = 2048, 1, 1024

    def build(fusions):
        gemv, silu, mul = _gemv_silu_mul(M, cols, tile)
        img = Image(
            _gemv_silu_mul_recording("three_step_device", gemv, silu, mul),
            FullELF(),
            fusions=fusions,
        )
        img.compile()
        return img.get_callable(), gemv, silu, mul

    fused_run, gemv, silu, mul = build((_three_step_fusion(),))
    plain_run, _, _, _ = build(())

    A = vectors(gemv).inputs["A"]
    B = vectors(gemv).inputs["B"]
    up = vectors(mul, seed=7).inputs["b"]
    y_ref = np.asarray(mul.reference(silu.reference(gemv.reference(A, B)), up))

    def dispatch(run):
        run.get_buffer(BufferRef("A")).numpy_view()[:] = A.reshape(-1)
        run.get_buffer(BufferRef("B")).numpy_view()[:] = B.reshape(-1)
        run.get_buffer(BufferRef("up")).numpy_view()[: up.size] = up.reshape(-1)
        run()
        return run.get_buffer(BufferRef("out")).numpy()[:M].copy()

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
    assert np.array_equal(
        out.view(np.uint16), baseline.view(np.uint16)
    ), "the fused and unfused devices differ"
