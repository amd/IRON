# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A fold (``iron.common.graph.fold``): a consumer's kernel runs inside its
producer's own cores, on the output tile before it leaves L1, so the
consumer takes no cores and no DMA hop of its own. No toolchain and no NPU
above the "On the device" line.
"""

import statistics

import numpy as np
import pytest
from aie.utils.verify import compare
from ml_dtypes import bfloat16

import iron
from iron import Scratchpad
from iron.common.declare.profile import Profile
from iron.common.design import OperatorDesign, BuiltArray
from iron.common.graph.fold import apply_folds, chosen_folds, fold_candidates
from iron.common.graph.record import Recording
from iron.common.image.link import FullELF
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef, Edge, Fusion, FusionKind
from iron.common.testing import vectors
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gelu import GELU
from iron.operators.gemv import GEMV
from iron.operators.silu import SiLU
from iron.tests.support import sequences
from iron.tests.support.llama_model import llama_1b, small
from iron.tune.measure import Timing, time_interleaved

pytestmark = pytest.mark.usefixtures("npu2")


def _stream(producer: int, output: str, input: str) -> Fusion:
    """A two-step stream fusion, the alternative a fold measures against."""
    return Fusion(
        FusionKind.STREAM,
        (producer, producer + 1),
        (Edge(producer, output, producer + 1, input),),
    )


def _silu_mul(size, tile, **extra):
    silu = SiLU(size=size, tile_size=tile, **extra)
    mul = ElementwiseMul(size=size, tile_size=tile, **extra)
    return silu, mul


def _silu_mul_recording(name, silu, mul):
    steps = sequences.steps((silu, "x", "mid"), (mul, "mid", "up", "out"))
    return Recording.of_steps(name, steps, ["x", "up"], ["out"])


def _gemv_add(M, K, tile_size_input, tile_size_output):
    gemv = GEMV(
        M=M, K=K, tile_size_input=tile_size_input, tile_size_output=tile_size_output
    )
    add = ElementwiseAdd(size=M, tile_size=tile_size_output)
    return gemv, add


def _gemv_add_recording(name, gemv, add):
    steps = sequences.steps((gemv, "A", "B", "mid"), (add, "r", "mid", "out"))
    return Recording.of_steps(name, steps, ["A", "B", "r"], ["out"])


# ---------------------------------------------------------------------------
# Device-free: fold_candidates() and apply_folds().
# ---------------------------------------------------------------------------


def test_silu_folds_elementwise_mul_candidate():
    silu, mul = _silu_mul(2048, 256)
    rec = _silu_mul_recording("silu_mul", silu, mul)
    (fusion,) = fold_candidates(rec)
    assert fusion == Fusion(FusionKind.FOLD, (0, 1), (Edge(0, "y", 1, "a"),))
    folded = apply_folds(rec, (fusion,))
    (step,) = folded.steps
    assert type(step.op).__name__ == "SiLU"
    assert [h.name for h in step.inputs] == ["x", "up"]
    assert [h.name for h in step.outputs] == ["out"]
    (link,) = step.op.finish
    assert (link.consumer, link.at, link.binary) == (ElementwiseMul, 0, True)


def test_gemv_folds_elementwise_add_candidate():
    gemv, add = _gemv_add(2048, 2048, 4, 256)
    rec = _gemv_add_recording("gemv_add", gemv, add)
    (fusion,) = fold_candidates(rec)
    assert fusion == Fusion(FusionKind.FOLD, (0, 1), (Edge(0, "C", 1, "b"),))
    folded = apply_folds(rec, (fusion,))
    (step,) = folded.steps
    assert type(step.op).__name__ == "GEMV"
    assert [h.name for h in step.inputs] == ["A", "B", "r"]
    (link,) = step.op.finish
    assert (link.consumer, link.at, link.binary) == (ElementwiseAdd, 1, True)


def test_a_chain_of_three_steps_admits_overlapping_candidates():
    """SiLU -> ElementwiseMul -> GELU: each pair, and the whole chain, is a
    separate candidate (overlapping ones included, as a stream run's are);
    applying the deepest collapses all three into one step, its finish the
    two consumers in order, only the first (binary) riding finish0.
    """
    silu = SiLU(size=2048, tile_size=256)
    mul = ElementwiseMul(size=2048, tile_size=256)
    gelu = GELU(size=2048, tile_size=256)
    steps = sequences.steps(
        (silu, "x", "mid1"), (mul, "mid1", "up", "mid2"), (gelu, "mid2", "out")
    )
    rec = Recording.of_steps("chain3", steps, ["x", "up"], ["out"])
    candidates = fold_candidates(rec)
    assert sorted(f.steps for f in candidates) == [(0, 1), (0, 1, 2), (1, 2)]
    (deepest,) = (f for f in candidates if len(f.steps) == 3)
    folded = apply_folds(rec, (deepest,))
    (step,) = folded.steps
    assert type(step.op).__name__ == "SiLU"
    assert [h.name for h in step.inputs] == ["x", "up"]
    assert [h.name for h in step.outputs] == ["out"]
    links = step.op.finish
    assert [(link.consumer, link.binary) for link in links] == [
        (ElementwiseMul, True),
        (GELU, False),
    ]
    op = step.op.resolved(step.op.dev)
    BuiltArray(OperatorDesign(op))


def test_a_second_binary_link_is_refused():
    """Only one step of a chain may take another input: its one free
    channel is the first's. SiLU folding Mul takes it; chaining Add in too
    would need a second (refused, chained or not: ``ElementwiseAdd`` into
    bare ``ElementwiseMul`` has no free channel of its own either, both of
    its own already a core's two).
    """
    silu = SiLU(size=2048, tile_size=256)
    mul = ElementwiseMul(size=2048, tile_size=256)
    add = ElementwiseAdd(size=2048, tile_size=256)
    steps = sequences.steps(
        (silu, "x", "mid1"), (mul, "mid1", "up", "mid2"), (add, "mid2", "r", "out")
    )
    rec = Recording.of_steps("two_binary", steps, ["x", "up", "r"], ["out"])
    candidates = fold_candidates(rec)
    assert sorted(f.steps for f in candidates) == [(0, 1)]


def test_a_graph_output_is_not_folded_away():
    """``mid``, both an intermediate and a graph output, keeps its own step:
    folding it would drop the step the host reads it from.
    """
    silu, mul = _silu_mul(2048, 256)
    steps = sequences.steps((silu, "x", "mid"), (mul, "mid", "up", "out"))
    rec = Recording.of_steps("kept_output", steps, ["x", "up"], ["mid", "out"])
    assert fold_candidates(rec) == ()


def test_a_tile_read_again_is_not_folded_away():
    """``mid`` read by a third step too: folding it would lose that read."""
    silu, mul = _silu_mul(2048, 256)
    mul2 = ElementwiseMul(size=2048, tile_size=256)
    steps = sequences.steps(
        (silu, "x", "mid"), (mul, "mid", "up", "out"), (mul2, "mid", "up2", "out2")
    )
    rec = Recording.of_steps("read_twice", steps, ["x", "up", "up2"], ["out", "out2"])
    assert fold_candidates(rec) == ()


def test_a_binary_producer_has_no_free_channel():
    """``ElementwiseAdd``'s own two inputs already hold both of a core's
    input channels, leaving none for a further binary finish's other input.
    """
    add = ElementwiseAdd(size=2048, tile_size=256)
    mul = ElementwiseMul(size=2048, tile_size=256)
    steps = sequences.steps((add, "a", "b", "mid"), (mul, "mid", "up", "out"))
    rec = Recording.of_steps("no_channel", steps, ["a", "b", "up"], ["out"])
    assert fold_candidates(rec) == ()
    # A unary finish needs no extra channel, and is admitted.
    silu = SiLU(size=2048, tile_size=256)
    steps = sequences.steps((add, "a", "b", "mid"), (silu, "mid", "out"))
    rec = Recording.of_steps("unary_ok", steps, ["a", "b"], ["out"])
    (fusion,) = fold_candidates(rec)
    assert fusion.steps == (0, 1)


def test_feed_b_leaves_no_channel_for_a_finish():
    gemv = GEMV(M=2048, K=2048, tile_size_input=4, tile_size_output=256, feed_b=True)
    add = ElementwiseAdd(size=2048, tile_size=256)
    rec = _gemv_add_recording("feed_b", gemv, add)
    assert fold_candidates(rec) == ()


def test_chosen_folds_matches_the_profile_and_is_applied_once():
    """``chosen_folds`` names the fusion a profile adds (the exact JSON form
    a ``Profile`` already carries any fusion kind in), a step in at most one.
    """
    silu, mul = _silu_mul(2048, 256)
    rec = _silu_mul_recording("profile_pick", silu, mul)
    profile = Profile()
    profile.add_fusion(
        FusionKind.FOLD, [(SiLU, {}), (ElementwiseMul, {})], [(0, "y", 1, "a")]
    )
    picked = chosen_folds(rec, profile)
    assert len(picked) == 1
    folded = apply_folds(rec, picked)
    assert len(folded.steps) == 1

    empty = Profile()
    assert chosen_folds(rec, empty) == ()


def test_the_folded_design_builds():
    """The finish chain's MLIR is real: it builds on the current device."""
    silu, mul = _silu_mul(2048, 256)
    rec = _silu_mul_recording("builds", silu, mul)
    folded = apply_folds(rec, fold_candidates(rec))
    op = folded.steps[0].op.resolved(folded.steps[0].op.dev)
    BuiltArray(OperatorDesign(op))

    gemv, add = _gemv_add(2048, 2048, 4, 256)
    rec2 = _gemv_add_recording("builds2", gemv, add)
    folded2 = apply_folds(rec2, fold_candidates(rec2))
    op2 = folded2.steps[0].op.resolved(folded2.steps[0].op.dev)
    BuiltArray(OperatorDesign(op2))


def _kinds(recording, fusion) -> tuple[str, ...]:
    return tuple(type(recording.steps[i].op.resolved()).__name__ for i in fusion.steps)


def test_fold_candidates_on_small_llama():
    """Decode's residual adds after o_proj and down_proj, and SwiGLU's
    gate activation, fold. The prompt chunk's own projections are
    ``ProjectionGEMM``, which declares no ``fold()``, so its residual adds
    stay; its SwiGLU gate, ``Elementwise`` like decode's, folds too, bound
    to the prompt chunk's own row count on both sides alike.
    """
    model = small()
    decode_shapes, prompt_shapes = model.shapes()
    decode, prompt = model.record(**decode_shapes), model.record(**prompt_shapes)
    folds = fold_candidates(decode)
    kinds = sorted(_kinds(decode, f) for f in folds)
    assert kinds == sorted(
        [("GEMV", "ElementwiseAdd")] * 4 + [("SiLU", "ElementwiseMul")] * 2
    )
    prompt_folds = fold_candidates(prompt)
    assert (
        sorted(_kinds(prompt, f) for f in prompt_folds)
        == [("SiLU", "ElementwiseMul")] * 2
    )


def test_fold_candidates_on_llama_1b_header():
    model = llama_1b(num_hidden_layers=1)
    decode_shapes, prompt_shapes = model.shapes()
    decode, prompt = model.record(**decode_shapes), model.record(**prompt_shapes)
    folds = fold_candidates(decode)
    kinds = sorted(_kinds(decode, f) for f in folds)
    assert kinds == sorted(
        [("GEMV", "ElementwiseAdd")] * 2 + [("SiLU", "ElementwiseMul")]
    )
    prompt_folds = fold_candidates(prompt)
    assert sorted(_kinds(prompt, f) for f in prompt_folds) == [
        ("SiLU", "ElementwiseMul")
    ]


# ---------------------------------------------------------------------------
# On the device: numpy, bit-equality to unfused, and timing vs unfused and
# vs the same pair stream-fused.
# ---------------------------------------------------------------------------


def _time(fused_run, unfused_run, stream_run):
    fused_stats, unfused_stats, stream_stats = time_interleaved(
        [fused_run, unfused_run, stream_run], Timing(rounds=10), log=lambda _: None
    )
    return {
        "folded": (
            min(fused_stats.samples_us),
            statistics.median(fused_stats.samples_us),
        ),
        "unfused": (
            min(unfused_stats.samples_us),
            statistics.median(unfused_stats.samples_us),
        ),
        "stream": (
            min(stream_stats.samples_us),
            statistics.median(stream_stats.samples_us),
        ),
    }


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize(
    "size,tile", [(8192, 1024), (2097152, 4096)], ids=["decode", "prompt"]
)
def test_silu_folds_elementwise_mul_on_device(size, tile, record_property):
    """``silu(gate) * up`` folded into SiLU's own cores holds to the two
    operators' references composed and is bit-equal to the pair run
    unfused; timed against both the unfused pair and the same pair
    stream-fused.
    """
    silu, mul = _silu_mul(size, tile)
    folded_op = silu.fold(mul, 0)
    assert folded_op is not None

    folded_rec = Recording.of_step(folded_op)
    unfused_rec = _silu_mul_recording("silu_mul_unfused", *_silu_mul(size, tile))
    stream_rec = _silu_mul_recording("silu_mul_stream", *_silu_mul(size, tile))

    folded_img = Image(folded_rec, FullELF())
    folded_img.compile()
    folded_run = folded_img.get_callable()

    unfused_img = Image(unfused_rec, FullELF())
    unfused_img.compile()
    unfused_run = unfused_img.get_callable()

    stream_img = Image(stream_rec, FullELF(), fusions=(_stream(0, "y", "a"),))
    stream_img.compile()
    stream_run = stream_img.get_callable()

    gate = vectors(silu).inputs["x"]
    up = vectors(mul, seed=7).inputs["b"]
    y_ref = np.asarray(folded_op.reference(gate, up))

    def dispatch(run, names):
        run.get_buffer(BufferRef(names[0])).numpy_view()[: gate.size] = gate.reshape(-1)
        run.get_buffer(BufferRef(names[1])).numpy_view()[: up.size] = up.reshape(-1)
        run()
        return run.get_buffer(BufferRef(names[2])).numpy()[:size].copy()

    out = dispatch(folded_run, ("x", "finish0", "y"))
    baseline = dispatch(unfused_run, ("x", "up", "out"))

    # SiLU's own contract through the multiply, plus both the device's and
    # the reference's roundings: WeightedRowwise.tolerance composes the
    # same way for a weight multiply.
    tol = folded_op.tolerance()
    verdict = compare(
        out, y_ref, tol, bound=tol.bound(gate, up) if tol.kind == "bound" else None
    )
    assert verdict, verdict.detail
    assert np.array_equal(
        out.view(np.uint16), baseline.view(np.uint16)
    ), "the folded and unfused devices differ"

    times = _time(folded_run, unfused_run, stream_run)
    for name, (lo, med) in times.items():
        record_property(f"{name} min us", lo)
        record_property(f"{name} median us", med)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize(
    "M,K", [(2048, 2048), (2048, 8192)], ids=["o_proj", "down_proj"]
)
def test_gemv_folds_elementwise_add_on_device(M, K, record_property):
    """Llama decode's GEMV -> ElementwiseAdd residual add, folded into GEMV's
    own cores, holds to the two operators' references composed and is
    bit-equal to the pair run unfused; timed against both the unfused pair
    and the same pair stream-fused.
    """
    tile_size_input, tile_size_output = (4, 256) if K == 2048 else (1, 256)
    gemv, add = _gemv_add(M, K, tile_size_input, tile_size_output)
    folded_op = gemv.fold(add, 1)
    assert folded_op is not None

    folded_rec = Recording.of_step(folded_op)
    unfused_rec = _gemv_add_recording(
        "gemv_add_unfused", *_gemv_add(M, K, tile_size_input, tile_size_output)
    )
    stream_rec = _gemv_add_recording(
        "gemv_add_stream", *_gemv_add(M, K, tile_size_input, tile_size_output)
    )

    folded_img = Image(folded_rec, FullELF())
    folded_img.compile()
    folded_run = folded_img.get_callable()

    unfused_img = Image(unfused_rec, FullELF())
    unfused_img.compile()
    unfused_run = unfused_img.get_callable()

    stream_img = Image(stream_rec, FullELF(), fusions=(_stream(0, "C", "b"),))
    stream_img.compile()
    stream_run = stream_img.get_callable()

    A = vectors(gemv).inputs["A"]
    B = vectors(gemv).inputs["B"]
    r = vectors(add, seed=7).inputs["a"]
    y_ref = np.asarray(folded_op.reference(A, B, r))

    def dispatch(run, names):
        run.get_buffer(BufferRef(names[0])).numpy_view()[:] = A.reshape(-1)
        run.get_buffer(BufferRef(names[1])).numpy_view()[:] = B.reshape(-1)
        run.get_buffer(BufferRef(names[2])).numpy_view()[:] = r.reshape(-1)
        run()
        return run.get_buffer(BufferRef(names[3])).numpy()[:M].copy()

    out = dispatch(folded_run, ("A", "B", "finish0", "C"))
    baseline = dispatch(unfused_run, ("A", "B", "r", "out"))

    tol = folded_op.tolerance()
    verdict = compare(
        out, y_ref, tol, bound=tol.bound(A, B, r) if tol.kind == "bound" else None
    )
    assert verdict, verdict.detail
    assert np.array_equal(
        out.view(np.uint16), baseline.view(np.uint16)
    ), "the folded and unfused devices differ"

    times = _time(folded_run, unfused_run, stream_run)
    for name, (lo, med) in times.items():
        record_property(f"{name} min us", lo)
        record_property(f"{name} median us", med)


@pytest.mark.supported_devices("npu2")
def test_a_three_step_chain_matches_reference_and_unfused_on_device():
    """GEMV -> ElementwiseAdd -> SiLU, all three folded into GEMV's own
    cores (a residual add then an activation), holds to the three
    operators' references composed and is bit-equal to the same three
    steps run unfused.
    """
    M, K = 2048, 2048
    gemv, add = _gemv_add(M, K, 4, 256)
    silu = SiLU(size=M, tile_size=256)
    chain_op = gemv.fold(add, 1).fold(silu, 0)
    assert chain_op is not None

    chain_rec = Recording.of_step(chain_op)
    plain_steps = sequences.steps(
        (gemv, "A", "B", "mid1"), (add, "r", "mid1", "mid2"), (silu, "mid2", "out")
    )
    unfused_rec = Recording.of_steps(
        "chain3_unfused", plain_steps, ["A", "B", "r"], ["out"]
    )

    chain_img = Image(chain_rec, FullELF())
    chain_img.compile()
    chain_run = chain_img.get_callable()

    unfused_img = Image(unfused_rec, FullELF())
    unfused_img.compile()
    unfused_run = unfused_img.get_callable()

    A = vectors(gemv).inputs["A"]
    B = vectors(gemv).inputs["B"]
    r = vectors(add, seed=7).inputs["a"]
    y_ref = np.asarray(chain_op.reference(A, B, r))

    def dispatch(run, names):
        run.get_buffer(BufferRef(names[0])).numpy_view()[:] = A.reshape(-1)
        run.get_buffer(BufferRef(names[1])).numpy_view()[:] = B.reshape(-1)
        run.get_buffer(BufferRef(names[2])).numpy_view()[:] = r.reshape(-1)
        run()
        return run.get_buffer(BufferRef(names[3])).numpy()[:M].copy()

    out = dispatch(chain_run, ("A", "B", "finish0", "C"))
    baseline = dispatch(unfused_run, ("A", "B", "r", "out"))

    tol = chain_op.tolerance()
    verdict = compare(
        out, y_ref, tol, bound=tol.bound(A, B, r) if tol.kind == "bound" else None
    )
    assert verdict, verdict.detail
    assert np.array_equal(
        out.view(np.uint16), baseline.view(np.uint16)
    ), "the chained and unfused devices differ"


@pytest.mark.supported_devices("npu2")
def test_a_bounded_fold_matches_across_different_per_call_counts():
    """SiLU -> ElementwiseMul, folded, bound to a graph's own per-call row
    count (as the prompt chunk's SwiGLU gate is): compiled once, called
    with several row counts, each bit-equal to the same call unfused and
    matching the graph's own reference over just the valid rows -- the
    prompt chunk's own regime, without needing the real model.
    """
    size, tile = 2048, 256

    class Gated(iron.Graph):
        def body(self, x, up, *, n: Scratchpad[np.int32]):
            y = SiLU.step(x[:n], tile_size=tile)
            return ElementwiseMul.step(y, up, tile_size=tile)

    profile = Profile()
    profile.add_fusion(
        FusionKind.FOLD, [(SiLU, {}), (ElementwiseMul, {})], [(0, "y", 1, "a")]
    )
    folded_graph = Gated()
    folded_graph.profile = profile
    folded = folded_graph.compile(x=(size,), up=(size,))
    assert len(folded.recording.steps) == 1
    folded.load()

    plain_graph = Gated()
    plain = plain_graph.compile(x=(size,), up=(size,))
    assert len(plain.recording.steps) == 2
    plain.load()

    rng = np.random.default_rng(3)
    x = rng.standard_normal(size).astype(np.float32).astype(bfloat16)
    up = rng.standard_normal(size).astype(np.float32).astype(bfloat16)

    for valid in (1024, 2048, 512):
        out = np.asarray(folded(x, up, n=valid))
        baseline = np.asarray(plain(x, up, n=valid))
        want = np.asarray(folded_graph.reference(x, up, n=valid))
        assert np.array_equal(
            out[:valid].view(np.uint16), baseline[:valid].view(np.uint16)
        ), f"n={valid}: the folded and unfused devices differ"
        assert np.array_equal(
            out[:valid].view(np.uint16), want[:valid].view(np.uint16)
        ), f"n={valid}: the folded device differs from the graph's own reference"
