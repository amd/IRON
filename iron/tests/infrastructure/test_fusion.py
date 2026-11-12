# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Image(fusions=...)``.

A run of steps streamed into the next, one device configuration with no host transfer. No toolchain and no NPU below the "On the device" line.
"""

import statistics

import numpy as np
import pytest
from aie import ir
from aie.utils.verify import Tolerance, compare

from iron.common.design import BuiltArray, OperatorDesign
from iron.common.graph.record import Recording
from iron.common.image.compose import Composition, places
from iron.common.image.link import FullELF, PerStep
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef, Edge, Fusion, FusionKind
from iron.common.testing import vectors
from iron.operators.clamp import Clamp
from iron.operators.copy import Gather
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemv import GEMV
from iron.tests.support import fusable, sequences
from iron.tune.measure import Timing, time_interleaved

pytestmark = pytest.mark.usefixtures("npu2")


# ---------------------------------------------------------------------------
# Device-free: the composed module.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("size,cols", [(2048, 1), (8192, 8)])
def test_fused_pair_is_one_device_configuration(size, cols):
    """A fused pair places as one device, which is one fewer ``aie.device`` than the same two steps unfused; its identity differs too."""
    tile = 1024
    silu, mul = fusable.silu_mul(size, tile, num_aie_columns=cols)
    fused = Image(
        fusable.silu_mul_recording(f"fuse_struct_{size}_{cols}", silu, mul),
        FullELF(),
        fusions=(fusable.stream(0, "y", "a"),),
    )
    fused._prepare()
    fused_composition = Composition(fused)
    fused_text = fused_composition.text()
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(fused_text))
    assert diagnostic is None, diagnostic

    silu2, mul2 = fusable.silu_mul(size, tile, num_aie_columns=cols)
    unfused = Image(
        fusable.silu_mul_recording(f"unfuse_struct_{size}_{cols}", silu2, mul2),
        FullELF(),
    )
    unfused._prepare()
    unfused_text = Composition(unfused).text()

    assert unfused_text.count("aie.device(") - fused_text.count("aie.device(") == 1, "a fused pair should drop exactly one aie.device"


def test_fused_identity_differs_from_unfused():
    silu, mul = fusable.silu_mul(2048, 1024, num_aie_columns=1)
    fused = Image(
        fusable.silu_mul_recording("fuse_identity_fused", silu, mul),
        FullELF(),
        fusions=(fusable.stream(0, "y", "a"),),
    )
    fused._prepare()
    silu2, mul2 = fusable.silu_mul(2048, 1024, num_aie_columns=1)
    unfused = Image(fusable.silu_mul_recording("fuse_identity_unfused", silu2, mul2), FullELF())
    unfused._prepare()
    assert Composition(fused).identity != Composition(unfused).identity


def test_gemv_to_elementwiseadd_fused_pair_is_one_device_configuration():
    """GEMV.C -> ElementwiseAdd.b (Llama decode's residual adds) places as one device, as the Elementwise-only pair does.

    The generalization is not restricted to ``Elementwise``.
    """
    gemv, add = fusable.gemv_add(2048, 2048)
    fused = Image(
        fusable.gemv_add_recording("gemv_add_struct_fused", gemv, add),
        FullELF(),
        fusions=(fusable.stream(0, "C", "b"),),
    )
    fused._prepare()
    fused_composition = Composition(fused)
    fused_text = fused_composition.text()
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(fused_text))
    assert diagnostic is None, diagnostic

    gemv2, add2 = fusable.gemv_add(2048, 2048)
    unfused = Image(fusable.gemv_add_recording("gemv_add_struct_unfused", gemv2, add2), FullELF())
    unfused._prepare()
    unfused_text = Composition(unfused).text()

    assert unfused_text.count("aie.device(") - fused_text.count("aie.device(") == 1, "a fused pair should drop exactly one aie.device"


def test_three_step_fusion_is_one_device_configuration():
    """GEMV -> SiLU -> ElementwiseMul, all three fused, drops two ``aie.device``s against the same steps unfused."""
    gemv, silu, mul = fusable.gemv_silu_mul(2048, 1, 2048)
    fused = Image(
        fusable.gemv_silu_mul_recording("three_step_struct_fused", gemv, silu, mul),
        FullELF(),
        fusions=(fusable.three_step(),),
    )
    fused._prepare()
    fused_text = Composition(fused).text()
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(fused_text))
    assert diagnostic is None, diagnostic

    gemv2, silu2, mul2 = fusable.gemv_silu_mul(2048, 1, 1024)
    unfused = Image(
        fusable.gemv_silu_mul_recording("three_step_struct_unfused", gemv2, silu2, mul2),
        FullELF(),
    )
    unfused._prepare()
    unfused_text = Composition(unfused).text()

    assert unfused_text.count("aie.device(") - fused_text.count("aie.device(") == 2, "a three-step fusion should drop two aie.devices"


# ---------------------------------------------------------------------------
# Refusals.
# ---------------------------------------------------------------------------


def test_bad_step_index_refused():
    silu, mul = fusable.silu_mul(2048, 1024, num_aie_columns=1)
    recording = fusable.silu_mul_recording("fuse_bad_index", silu, mul)
    with pytest.raises(ValueError, match="names no step"):
        Image(recording, FullELF(), fusions=(fusable.stream(1, "y", "a"),))


@pytest.mark.parametrize("packaging", [FullELF(), PerStep()], ids=["full_elf", "per_step"])
def test_an_image_refuses_a_fusion_with_a_gap(packaging):
    silu, mul = fusable.silu_mul(2048, 1024, num_aie_columns=1)
    steps = sequences.steps((silu, "x", "a"), (mul, "a", "up", "b"), (silu, "up", "c"))
    recording = Recording.of_steps("gap", steps, ["x", "up"], ["b", "c"])
    with pytest.raises(ValueError, match="must be consecutive"):
        Image(recording, packaging, fusions=(Fusion(FusionKind.PACK, (0, 2)),))


def test_wrong_buffer_names_refused():
    silu, mul = fusable.silu_mul(2048, 1024, num_aie_columns=1)
    with pytest.raises(ValueError, match="no drained buffer"):
        Image(
            fusable.silu_mul_recording("fuse_bad_output", silu, mul),
            FullELF(),
            fusions=(fusable.stream(0, "nope", "a"),),
        )
    silu, mul = fusable.silu_mul(2048, 1024, num_aie_columns=1)
    with pytest.raises(ValueError, match="no filled buffer"):
        Image(
            fusable.silu_mul_recording("fuse_bad_input", silu, mul),
            FullELF(),
            fusions=(fusable.stream(0, "y", "nope"),),
        )
    silu, mul = fusable.silu_mul(2048, 1024, num_aie_columns=1)
    split = Recording.of_steps(
        "fuse_split_roots",
        sequences.steps((silu, "x", "mid_a"), (mul, "mid_b", "up", "out")),
        ["x", "up"],
        ["out"],
    )
    with pytest.raises(ValueError, match="do not name one whole buffer"):
        Image(split, FullELF(), fusions=(fusable.stream(0, "y", "a"),))


def test_step_in_two_fusions_refused():
    silu, mul = fusable.silu_mul(2048, 1024, num_aie_columns=1)
    recording = fusable.silu_mul_recording("fuse_double_claim", silu, mul)
    with pytest.raises(ValueError, match="is in two fusions"):
        Image(
            recording,
            FullELF(),
            fusions=(fusable.stream(0, "y", "a"), fusable.stream(0, "y", "a")),
        )


def test_perstep_builds_fusions_but_check_refuses_them():
    """A per-step image links a fusion's steps as one xclbin (``iron.common.image.link.FusedDesign``); ``check=True`` still refuses.

    Since it holds each step to its reference on its own dispatch.
    """
    silu, mul = fusable.silu_mul(2048, 1024, num_aie_columns=1)
    Image(
        fusable.silu_mul_recording("fuse_perstep", silu, mul),
        PerStep(),
        fusions=(fusable.stream(0, "y", "a"),),
    )

    silu2, mul2 = fusable.silu_mul(2048, 1024, num_aie_columns=1)
    recording = fusable.silu_mul_recording("fuse_perstep_check", silu2, mul2)
    with pytest.raises(ValueError, match="check=True"):
        Image(recording, PerStep(check=True), fusions=(fusable.stream(0, "y", "a"),))


def test_fusion_needs_at_least_two_steps():
    with pytest.raises(ValueError, match="at least two steps"):
        Fusion(FusionKind.STREAM, (0,), ())


# ---------------------------------------------------------------------------
# A member no edge touches (REGIONS-IMPLEMENT 4.3).
# ---------------------------------------------------------------------------


def _chain_and_rider(independent: bool):
    """Return a SiLU -> Mul stream, plus a third step.

    Independent of the chain (``independent``), or reading the chain's own on-chip
    intermediate (``mid``) without being one of its edge's recorded readers, a hazard
    no edge records.
    """
    silu, mul = fusable.silu_mul(2048, 1024, num_aie_columns=1)
    rider = GEMV(M=2048, K=2048, tile_size_input=4, tile_size_output=256)
    third = "side" if independent else "mid"
    steps = sequences.steps((silu, "x", "mid"), (mul, "mid", "up", "out"), (rider, "A", third, "y"))
    inputs = ["x", "up", "A"] + (["side"] if independent else [])
    return Recording.of_steps("fuse_rider", steps, inputs, ["out", "y"])


def test_a_member_no_edge_touches_may_ride_beside_a_stream():
    recording = _chain_and_rider(independent=True)
    fusion = Fusion(FusionKind.STREAM, (0, 1, 2), (Edge(0, "y", 1, "a"),))
    Image(recording, FullELF(), fusions=(fusion,))


def test_a_rider_sharing_the_chains_own_input_is_refused_as_a_hazard():
    recording = _chain_and_rider(independent=False)
    fusion = Fusion(FusionKind.STREAM, (0, 1, 2), (Edge(0, "y", 1, "a"),))
    with pytest.raises(ValueError, match="share a root with no edge between them"):
        Image(recording, FullELF(), fusions=(fusion,))


def test_fusion_steps_must_be_increasing_and_distinct():
    with pytest.raises(ValueError, match="increasing and distinct"):
        Fusion(FusionKind.STREAM, (1, 0), ())
    with pytest.raises(ValueError, match="increasing and distinct"):
        Fusion(FusionKind.STREAM, (0, 0, 1), ())


def test_edge_skipping_a_non_member_step_refused():
    """An edge may not skip a non-member step, which would have to run interleaved between the fusion's two halves."""
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


def test_bind_refuses_a_fed_input():
    """A build that bound a fed input's own lanes, rather than reading them from ``fifos()``.

    Would silently ignore the feed and hang; ``bind()`` refuses it instead.
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
    """``Gather`` pins its output to shim channels rather than streaming it through a fifo, so it cannot feed another operator on-chip."""
    gather = Gather(rows=8, table_rows=8, row=32, feeds=1).resolved()
    produced = BuiltArray(OperatorDesign(gather))
    (source,) = [b for b in produced.op.buffers if b.name == "y"]
    clamp = Clamp(size=32, num_aie_columns=1, tile_size=32, low=0.0, high=1.0).resolved()
    with pytest.raises(ValueError, match="pinned"):
        clamp.x.feed(source)


def test_feed_refuses_a_lane_order_mismatch():
    """GEMV with ``num_batches`` streams ``C`` as one run per batch; a plain ElementwiseAdd of the same per-lane tile reads a single run.

    So lane 0's host access order differs, and ``feed`` names it.
    """
    gemv = GEMV(M=2048, K=64, num_batches=4, tile_size_input=4, tile_size_output=256).resolved()
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
    """silu(gate) * up fused on-chip holds to the operators' references fused, and is bit-equal to the same two steps run unfused."""
    size, cols, tile = 2048, 1, 1024

    def build(fusions):
        silu, mul = fusable.silu_mul(size, tile, num_aie_columns=cols)
        img = Image(
            fusable.silu_mul_recording("fuse_device", silu, mul),
            FullELF(),
            fusions=fusions,
        )
        img.compile()
        return img.get_callable(), silu, mul

    fused_run, silu, mul = build((fusable.stream(0, "y", "a"),))
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
    assert np.array_equal(out.view(np.uint16), baseline.view(np.uint16)), "the fused and unfused devices differ"


@pytest.mark.supported_devices("npu2")
def test_fused_per_call_shared_value():
    """Both operators' ``valid`` bound to one graph value share one scratchpad word (``FullELF.shared_words``).

    Which the device still reads correctly.
    """
    size, cols, tile = 2048, 1, 1024
    silu, mul = fusable.silu_mul(size, tile, num_aie_columns=cols, bound_values={"valid": None})
    # "valid" bounds each core's trip count only through "count", derived from
    # it; that is the word a core reads, and the one the two operators share.
    shared = {
        silu.value("count").symbol: "fuse_count",
        mul.value("count").symbol: "fuse_count",
    }
    img = Image(
        fusable.silu_mul_recording("fuse_device_per_call", silu, mul),
        FullELF(shared_words=shared),
        fusions=(fusable.stream(0, "y", "a"),),
    )
    img.compile()
    assert sum(p.name == "fuse_count" for p in img.artifacts.parameter_table) == 1, "both operators' count should share one scratchpad word"

    # Every per-call word both operators declare, not just the shared one: a
    # bounded call still writes each buffer's own tile count.
    declared = img.artifacts.parameters
    words = {shared.get(v.symbol, v.symbol): np.int32(size if v.derive is None else op.derived_at(v.name, valid=size)) for op in (silu, mul) for v in op.values}

    run = img.get_callable()
    gate = vectors(silu).inputs["x"]
    up = vectors(mul, seed=7).inputs["b"]
    run.get_buffer(BufferRef("x")).numpy_view()[: gate.size] = gate.reshape(-1)
    run.get_buffer(BufferRef("up")).numpy_view()[: up.size] = up.reshape(-1)
    run.write_values({k: w for k, w in words.items() if k in declared})
    run()
    out = run.get_buffer(BufferRef("out")).numpy()[:size].copy()

    y_ref = np.asarray(mul.reference(silu.reference(gate), up))
    tol = Tolerance.bf16_ulps(3, atol=mul.tolerance().atol, note="shared valid, every element live")
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail


@pytest.mark.supported_devices("npu2")
def test_gemv_to_elementwiseadd_matches_reference_and_unfused(record_property):
    """Llama decode's GEMV(M=2048, K=2048) -> ElementwiseAdd residual add, fused on-chip.

    Holds to the references fused and is bit-equal to the same steps unfused; also times both the tuner's way, min and median over interleaved rounds.
    """
    M, K = 2048, 2048

    def build(fusions):
        gemv, add = fusable.gemv_add(M, K)
        img = Image(
            fusable.gemv_add_recording("gemv_add_device", gemv, add),
            FullELF(),
            fusions=fusions,
        )
        img.compile()
        return img.get_callable(), gemv, add

    fused_run, gemv, add = build((fusable.stream(0, "C", "b"),))
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
    assert np.array_equal(out.view(np.uint16), baseline.view(np.uint16)), "the fused and unfused devices differ"

    fused_stats, unfused_stats = time_interleaved([fused_run, plain_run], Timing(rounds=20), log=lambda _: None)
    record_property("Fused min us", min(fused_stats.samples_us))
    record_property("Fused median us", statistics.median(fused_stats.samples_us))
    record_property("Unfused min us", min(unfused_stats.samples_us))
    record_property("Unfused median us", statistics.median(unfused_stats.samples_us))


@pytest.mark.supported_devices("npu2")
def test_three_step_fusion_matches_reference_and_unfused():
    """GEMV -> SiLU -> ElementwiseMul, all three fused on-chip, holds to the references fused and is bit-equal to the same steps unfused."""
    M, cols, tile = 2048, 1, 2048

    def build(fusions):
        gemv, silu, mul = fusable.gemv_silu_mul(M, cols, tile)
        img = Image(
            fusable.gemv_silu_mul_recording("three_step_device", gemv, silu, mul),
            FullELF(),
            fusions=fusions,
        )
        img.compile()
        return img.get_callable(), gemv, silu, mul

    fused_run, gemv, silu, mul = build((fusable.three_step(),))
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
        note="GEMV's accumulation and SiLU's 1 ulp through the multiply, plus both roundings",
    )
    verdict = compare(out, y_ref, tol)
    assert verdict, verdict.detail
    assert np.array_equal(out.view(np.uint16), baseline.view(np.uint16)), "the fused and unfused devices differ"
