# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``FusionKind.STAGED`` (an edge whose lanes do not meet, restaged through memtiles, ``Staging``) and fan-out (one output feeding several inputs).

No toolchain and no NPU above the "On the device" line.
"""

import re
import statistics
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import pytest
from aie import ir
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

import iron
from iron import Profile, Scratchpad
from iron.common.declare.operand import Staging
from iron.common.design import BuiltArray, OperatorDesign
from iron.common.graph.fusion import candidates
from iron.common.graph.record import Recording
from iron.common.image.compose import Composition, phases, places
from iron.common.image.link import FullELF, FusedDesign, PerStep
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef, Edge, Fusion, FusionKind
from iron.common.testing import vectors
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.rms_norm import RMSNorm
from iron.operators.silu import SiLU
from iron.tests.support import hang, sequences
from iron.tests.support.llama_model import llama_1b
from iron.tune.measure import Timing, time_interleaved

pytestmark = pytest.mark.usefixtures("npu2")

LLAMA_NPU2_PROFILE = Profile.load(
    Path(__file__).resolve().parents[2] / "applications/llama/profiles/npu2.json"
)


def _staged(*edges: Edge) -> Fusion:
    steps = sorted({s for e in edges for s in (e.producer, e.consumer)})
    return Fusion(FusionKind.STAGED, tuple(range(steps[0], steps[-1] + 1)), edges)


def _add_norm(add_cols=8, norm_cols=4):
    """Eight rows of 2048: ElementwiseAdd's lanes a row each, RMSNorm's two (four lanes) or more, so each RMSNorm lane joins whole add lanes."""
    add = ElementwiseAdd(size=8 * 2048, num_aie_columns=add_cols, tile_size=2048)
    norm = RMSNorm(rows=8, tile_size=2048, num_aie_columns=norm_cols)
    return add, norm


def _add_norm_recording(name, add, norm):
    steps = sequences.steps((add, "a", "b", "mid"), (norm, "mid", "out"))
    return Recording.of_steps(name, steps, ["a", "b"], ["out"])


def _norm_mul(cols=4):
    """One normed row of 2048 into an ElementwiseMul of ``cols`` lanes, each a slot of every object RMSNorm's one lane streams."""
    norm = RMSNorm(rows=1, tile_size=2048)
    mul = ElementwiseMul(size=2048, num_aie_columns=cols, tile_size=2048 // cols)
    return norm, mul


def _norm_mul_recording(name, norm, mul):
    steps = sequences.steps((norm, "x", "mid"), (mul, "mid", "up", "out"))
    return Recording.of_steps(name, steps, ["x", "up"], ["out"])


def _mul_down(mul_cols=4):
    """Llama decode's down_proj (M=2048, K=8192) streaming B, fed the gated product, ``mul_cols`` lanes: every GEMV core reads the whole vector."""
    mul = ElementwiseMul(size=8192, num_aie_columns=mul_cols, tile_size=1024)
    down = GEMV(M=2048, K=8192, feed_b=True)
    return mul, down


def _mul_down_recording(name, mul, down):
    steps = sequences.steps((mul, "g", "u", "mid"), (down, "W", "mid", "out"))
    return Recording.of_steps(name, steps, ["g", "u", "W"], ["out"])


def _silu_down():
    """down_proj fed from eight lanes of one input: a join of joins (four and four, then two)."""
    silu = SiLU(size=8192, num_aie_columns=8, tile_size=1024)
    down = GEMV(M=2048, K=8192, feed_b=True)
    return silu, down


def _silu_down_recording(name, silu, down):
    steps = sequences.steps((silu, "x", "mid"), (down, "W", "mid", "out"))
    return Recording.of_steps(name, steps, ["x", "W"], ["out"])


def _norm_qkv(columns=(8, 4, 2)):
    """Llama decode's q/k/v projections (M=2048/512/512, K=2048) streaming B, each fed the one normed row, ``columns`` wide."""
    qc, kc, vc = columns
    norm = RMSNorm(rows=1, tile_size=2048)
    q = GEMV(M=2048, K=2048, feed_b=True, num_aie_columns=qc)
    k = GEMV(M=512, K=2048, feed_b=True, num_aie_columns=kc)
    v = GEMV(M=512, K=2048, feed_b=True, num_aie_columns=vc)
    return norm, q, k, v


def _norm_qkv_recording(name, norm, q, k, v):
    steps = sequences.steps(
        (norm, "x", "n"),
        (q, "Aq", "n", "oq"),
        (k, "Ak", "n", "ok"),
        (v, "Av", "n", "ov"),
    )
    return Recording.of_steps(name, steps, ["x", "Aq", "Ak", "Av"], ["oq", "ok", "ov"])


def _norm_qkv_fusion() -> Fusion:
    return Fusion(
        FusionKind.STREAM,
        (0, 1, 2, 3),
        (Edge(0, "y", 1, "B"), Edge(0, "y", 2, "B"), Edge(0, "y", 3, "B")),
    )


def _silu_muls():
    silu = SiLU(size=2048, num_aie_columns=1, tile_size=1024)
    mul1 = ElementwiseMul(size=2048, num_aie_columns=1, tile_size=1024)
    mul2 = ElementwiseMul(size=2048, num_aie_columns=1, tile_size=1024)
    return silu, mul1, mul2


def _silu_muls_recording(name, silu, mul1, mul2):
    steps = sequences.steps(
        (silu, "x", "mid"), (mul1, "mid", "up1", "out1"), (mul2, "mid", "up2", "out2")
    )
    return Recording.of_steps(name, steps, ["x", "up1", "up2"], ["out1", "out2"])


def _silu_muls_fusion() -> Fusion:
    return Fusion(
        FusionKind.STREAM, (0, 1, 2), (Edge(0, "y", 1, "a"), Edge(0, "y", 2, "a"))
    )


def _mlp():
    """Llama 3.2 1B decode's gate and up projections (M=8192, K=2048) into SiLU and the multiply, at the profile's own tunables, all 32 cores."""
    gate = LLAMA_NPU2_PROFILE.make(GEMV, M=8192, K=2048)
    up = LLAMA_NPU2_PROFILE.make(GEMV, M=8192, K=2048)
    silu = LLAMA_NPU2_PROFILE.make(SiLU, size=8192)
    mul = LLAMA_NPU2_PROFILE.make(ElementwiseMul, size=8192)
    return gate, up, silu, mul


def _mlp_recording(name, gate, up, silu, mul):
    steps = sequences.steps(
        (gate, "Wg", "x", "g"),
        (up, "Wu", "x", "u"),
        (silu, "g", "s"),
        (mul, "s", "u", "out"),
    )
    return Recording.of_steps(name, steps, ["Wg", "Wu", "x"], ["out"])


def _mlp_fusion() -> Fusion:
    return Fusion(
        FusionKind.STREAM,
        (0, 1, 2, 3),
        (Edge(0, "C", 2, "x"), Edge(1, "C", 3, "b"), Edge(2, "y", 3, "a")),
    )


def _plan(producer, output, consumer, input_) -> Staging:
    producer, consumer = producer.resolved(), consumer.resolved()
    return Staging(getattr(producer, output), getattr(consumer, input_))


def _skip():
    """Return a residual add read by RMSNorm and, past a GEMV reducing its row, again.

    Each add moves two lanes of four 256-element objects; the second add reads the
    first's output and the GEMV's.
    """
    add = ElementwiseAdd(size=2048, num_aie_columns=2, tile_size=256)
    norm = RMSNorm(rows=1, tile_size=2048)
    proj = GEMV(M=2048, K=2048, feed_b=True, num_aie_columns=2)
    add2 = ElementwiseAdd(size=2048, num_aie_columns=2, tile_size=256)
    return add, norm, proj, add2


def _skip_recording(name, add, norm, proj, add2):
    steps = sequences.steps(
        (add, "a", "b", "h"),
        (norm, "h", "n"),
        (proj, "W", "n", "g"),
        (add2, "g", "h", "out"),
    )
    return Recording.of_steps(name, steps, ["a", "b", "W"], ["out"])


def _skip_fusion():
    return _staged(
        Edge(0, "y", 1, "x"),
        Edge(1, "y", 2, "B"),
        Edge(2, "C", 3, "a"),
        Edge(0, "y", 3, "b"),
    )


def _residual(mul_first: bool):
    """Return a residual add read once, past a GEMV fed whole, and the steps' order.

    The first add moves two lanes of sixteen 256-element objects into the second add,
    its only reader; the GEMV takes the multiply's vector whole. ``mul_first`` puts
    the multiply before the first add.
    """
    add = ElementwiseAdd(size=8192, num_aie_columns=2, tile_size=256)
    mul = ElementwiseMul(size=2048, num_aie_columns=2, tile_size=1024)
    proj = GEMV(M=8192, K=2048, feed_b=True, num_aie_columns=2)
    add2 = ElementwiseAdd(size=8192, num_aie_columns=2, tile_size=256)
    steps = {
        "add": (add, "a", "b", "h"),
        "mul": (mul, "c", "d", "m"),
        "proj": (proj, "W", "m", "g"),
        "add2": (add2, "g", "h", "out"),
    }
    order = (
        ["mul", "add", "proj", "add2"] if mul_first else ["add", "mul", "proj", "add2"]
    )
    return [steps[k][0] for k in order], [steps[k] for k in order], order


def _residual_fusion(order, phased=True) -> Fusion:
    at = {k: i for i, k in enumerate(order)}
    edges = (
        Edge(at["mul"], "y", at["proj"], "B"),
        Edge(at["proj"], "C", at["add2"], "a"),
        Edge(at["add"], "y", at["add2"], "b"),
    )
    return Fusion(FusionKind.STAGED, (0, 1, 2, 3), edges, phased=phased)


def _residual_recording(name, order, steps):
    return Recording.of_steps(
        name, sequences.steps(*steps), ["a", "b", "c", "d", "W"], ["out"]
    )


def _composed(recording, fusions) -> str:
    image = Image(recording, FullELF(), fusions=fusions)
    image._prepare()
    return Composition(image).text()


# ---------------------------------------------------------------------------
# Staging: the plan each edge derives from its two operands' transfers().
# ---------------------------------------------------------------------------


def test_eight_lanes_join_in_pairs_into_four():
    """Each of RMSNorm's four lanes (two rows) joins two of ElementwiseAdd's eight (a row each), whole, in one round of both rows."""
    add, norm = _add_norm()
    plan = _plan(add, "y", norm, "x")
    assert plan.joins == [([2 * k, 2 * k + 1], [2048, 2048]) for k in range(4)]
    assert plan.splits == []


def test_one_lane_splits_into_four_slots_of_each_object():
    norm, mul = _norm_mul(4)
    plan = _plan(norm, "y", mul, "a")
    assert plan.joins == []
    assert plan.splits == [([0, 1, 2, 3], [512] * 4)]


def test_a_gather_for_every_core_joins_all_lanes():
    """GEMV's B is one lane of the whole vector: the product's four lanes join into it, every core reading that one fifo."""
    mul, down = _mul_down()
    plan = _plan(mul, "y", down, "B")
    assert plan.joins == [(list(range(4)), [2048] * 4)]


def test_a_tile_mismatch_forwards_in_rounds():
    """One lane each, SiLU's 1024-element objects into ElementwiseMul's 512: a forward of one producer object a round, two consumer objects each."""
    silu = SiLU(size=2048, num_aie_columns=1, tile_size=1024)
    mul = ElementwiseMul(size=2048, num_aie_columns=1, tile_size=512)
    plan = _plan(silu, "y", mul, "a")
    assert plan.joins == [([0], [1024])]


def test_eight_lanes_join_in_two_levels():
    """Eight lanes into one: a memtile takes six, so two join four each and a third joins their two outputs."""
    add = ElementwiseAdd(size=2048, num_aie_columns=8, tile_size=256)
    norm = RMSNorm(rows=1, tile_size=2048)
    plan = _plan(add, "y", norm, "x")
    assert plan.joins == [(list(range(8)), [256] * 8)]
    recording = Recording.of_steps(
        "join_of_joins",
        sequences.steps((add, "a", "b", "mid"), (norm, "mid", "out")),
        ["a", "b"],
        ["out"],
    )
    text = _composed(recording, (_staged(Edge(0, "y", 1, "x")),))
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(text))
    assert diagnostic is None, diagnostic
    assert text.count("aie.objectfifo.link") == 3


def test_a_round_past_a_memtile_is_refused():
    """One lane of a 2 MiB buffer joins two contiguous halves whole: one round is the whole buffer, past a memtile's 512 KiB."""
    add = ElementwiseAdd(size=1 << 20, num_aie_columns=2, tile_size=2048)
    mul = ElementwiseMul(size=1 << 20, num_aie_columns=1, tile_size=2048)
    with pytest.raises(ValueError, match="past a memtile"):
        _plan(add, "y", mul, "a")


def test_an_order_neither_a_join_nor_a_split_gives_is_refused():
    """RMSNorm's two lanes of two rows each into four lanes of one row: each round (a row) feeds one lane of the four, not a slot of each."""
    norm = RMSNorm(rows=4, tile_size=2048, num_aie_columns=2)
    add = ElementwiseAdd(size=4 * 2048, num_aie_columns=4, tile_size=2048)
    with pytest.raises(ValueError, match="neither a join .* nor a split"):
        _plan(norm, "y", add, "b")


def _bounded(tile=4096):
    """SiLU's eight lanes of 2048 into ElementwiseMul's four of ``tile``, both bounded by the graph's own per-call element count ``n``."""

    class Staged(iron.Graph):
        def body(self, x, up, *, n: Scratchpad[np.int32]):
            y = SiLU.step(x[:n], tile_size=2048, num_aie_columns=8)
            return ElementwiseMul.step(y, up, tile_size=tile, num_aie_columns=4)

    return Staged()


BOUNDED_SIZE = 8 * 16384


def test_a_bound_moving_whole_rounds_alike_is_staged():
    """Both sides move ceil(n / 16384) rounds of 16384 elements a call, so the static link stays in step."""
    recording = _bounded().record(x=(BOUNDED_SIZE,), up=(BOUNDED_SIZE,))
    silu, mul = (s.op.resolved() for s in recording.steps)
    plan = Staging(silu.y, mul.a)
    assert plan.joins == [([2 * k, 2 * k + 1], [2048, 2048]) for k in range(4)]
    assert candidates(recording) == (_staged(Edge(0, "y", 1, "a")),)


def test_a_bound_moving_other_rounds_is_refused():
    """Mul at 2048-element tiles moves rounds of 8192 a call against SiLU's 16384, which would leave SiLU's link half a round short."""
    recording = _bounded(2048).record(x=(BOUNDED_SIZE,), up=(BOUNDED_SIZE,))
    silu, mul = (s.op.resolved() for s in recording.steps)
    with pytest.raises(ValueError, match="not one graph value moving whole rounds"):
        Staging(silu.y, mul.a)


def test_a_bound_without_a_graph_value_is_refused():
    """Bound to no graph value, the two counts cannot be known to agree."""
    add = ElementwiseAdd(
        size=8 * 2048, num_aie_columns=8, tile_size=2048, bound_values={"valid": None}
    )
    norm = RMSNorm(
        rows=8, tile_size=2048, num_aie_columns=4, bound_values={"valid": None}
    )
    with pytest.raises(ValueError, match="not one graph value"):
        _plan(add, "y", norm, "x")


def test_one_side_bounded_is_refused():
    add = ElementwiseAdd(
        size=8 * 2048, num_aie_columns=8, tile_size=2048, bound_values={"valid": None}
    )
    norm = RMSNorm(rows=8, tile_size=2048, num_aie_columns=4)
    with pytest.raises(ValueError, match="one side is bounded"):
        _plan(add, "y", norm, "x")


def test_a_length_no_bound_names_is_refused():
    """Copy of SiLU's whole output cut to ``n`` rows moves ``n`` a call against SiLU's every element, with no bound on either side to compare."""

    class Tail(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            y = SiLU.step(x, tile_size=2048, num_aie_columns=8)
            return Copy.step(y[:n])

    recording = Tail().record(x=(BOUNDED_SIZE,))
    silu, copy = (s.op.resolved() for s in recording.steps)
    with pytest.raises(ValueError, match="no bound of its operator names it"):
        Staging(silu.y, copy.x)
    assert candidates(recording) == ()


def test_feed_refuses_a_mismatch_unless_staged():
    """A stream edge's ``feed`` still refuses lanes that do not meet; staged, the consumer's lanes read the fifos the plan built."""
    add, norm = _add_norm()
    produced = BuiltArray(OperatorDesign(add.resolved()))
    (source,) = [b for b in produced.op.buffers if b.name == "y"]
    with pytest.raises(ValueError, match="streams 8 lanes"):
        norm.resolved().x.feed(source)
    consumer = norm.resolved()
    consumer.x.feed(source, staged=True)
    assert consumer.x.staged is not None and len(consumer.x.staged) == 4
    assert source.feeds == [consumer.x]


# ---------------------------------------------------------------------------
# Composition: staged and fan-out fusions as one device configuration.
# ---------------------------------------------------------------------------


def test_staged_pair_is_one_device_configuration_with_memtile_links():
    add, norm = _add_norm()
    text = _composed(
        _add_norm_recording("staged_struct", add, norm),
        (_staged(Edge(0, "y", 1, "x")),),
    )
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(text))
    assert diagnostic is None, diagnostic
    assert text.count("aie.objectfifo.link") == 4
    add2, norm2 = _add_norm()
    unfused = _composed(_add_norm_recording("staged_struct_apart", add2, norm2), ())
    assert unfused.count("aie.device(") - text.count("aie.device(") == 1


def test_split_pair_places():
    norm, mul = _norm_mul(4)
    text = _composed(
        _norm_mul_recording("split_struct", norm, mul),
        (_staged(Edge(0, "y", 1, "a")),),
    )
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(text))
    assert diagnostic is None, diagnostic
    assert text.count("aie.objectfifo.link") == 1


def test_a_stream_fusion_refuses_lanes_a_staged_one_takes():
    add, norm = _add_norm()
    stream = Fusion(FusionKind.STREAM, (0, 1), (Edge(0, "y", 1, "x"),))
    with pytest.raises(ValueError, match="streams 8 lanes"):
        _composed(_add_norm_recording("stream_refuses", add, norm), (stream,))


def test_fan_out_to_two_of_one_design_places_each_its_own_array():
    """SiLU's output feeds two ElementwiseMuls of one design; each keeps an array of its own, where an unfused image would share one."""
    text = _composed(
        _silu_muls_recording("fan_out_struct", *_silu_muls()), (_silu_muls_fusion(),)
    )
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(text))
    assert diagnostic is None, diagnostic
    assert text.count("aie.core(") == 3


def test_a_later_reader_holds_its_lanes_whole_call():
    """Hold a lane's whole call at a reader that takes it a phase later.

    The second add reads the first's lanes only once the GEMV past the norm has its
    row: its ends hold a lane's four objects, so the first add never waits on it while
    the norm still needs the rest.
    """
    text = _composed(_skip_recording("skip_struct", *_skip()), (_skip_fusion(),))
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(text))
    assert diagnostic is None, diagnostic
    later = re.findall(
        r"aie\.objectfifo @\S+\(%\w+, \{%\w+, %\w+\}, "
        r"\[2 : i32, 2 : i32, 4 : i32\]\)",
        text,
    )
    assert len(later) == 2, text


def _mul_down_fusion(phased: bool) -> Fusion:
    return Fusion(FusionKind.STAGED, (0, 1), (Edge(0, "y", 1, "B"),), phased=phased)


def test_a_reader_of_a_whole_object_starts_a_phase():
    """Run the down projection, fed its vector as one object, a phase after the multiply."""
    mul, down = _mul_down()
    rec = _mul_down_recording("phases_of", mul, down)
    image = Image(rec, FullELF(), fusions=(_mul_down_fusion(True),))
    image._prepare()
    arrays = {j: BuiltArray(OperatorDesign(rec.steps[j].op.resolved())) for j in (0, 1)}
    assert phases(_mul_down_fusion(True), arrays) == {0: 0, 1: 1}


def test_a_first_reader_of_several_objects_runs_in_its_producers_phase():
    """Keep a residual add with its only reader, the add past the GEMV, in one phase.

    Its lanes move sixteen objects into an end two deep: run a phase earlier, it would
    stall once that end fills, and its phase's awaited fills would never complete, as
    the reader waits on the GEMV's weights the next phase sends. The multiply first,
    the residual add runs with the GEMV and the second add; the add first, its phase
    would precede the multiply's, out of step order, so the fusion runs in no phases.
    """
    for mul_first, want in ((True, {0: 0, 1: 1, 2: 1, 3: 1}), (False, None)):
        ops, steps, order = _residual(mul_first)
        rec = _residual_recording("residual_phases", order, steps)
        arrays = {
            j: BuiltArray(OperatorDesign(rec.steps[j].op.resolved())) for j in range(4)
        }
        if want is None:
            with pytest.raises(ValueError, match="do not follow step order"):
                phases(_residual_fusion(order), arrays)
        else:
            assert phases(_residual_fusion(order), arrays) == want


def test_a_later_reader_may_run_phases_after_its_producer():
    """Run the skip window's second add, a later reader of the first, two phases on."""
    rec = _skip_recording("skip_phases", *_skip())
    arrays = {
        j: BuiltArray(OperatorDesign(rec.steps[j].op.resolved())) for j in range(4)
    }
    fusion = Fusion(FusionKind.STAGED, (0, 1, 2, 3), _skip_fusion().edges, phased=True)
    # The norm takes the add's row whole, the GEMV the norm's: three phases.
    assert phases(fusion, arrays) == {0: 0, 1: 1, 2: 2, 3: 2}


def test_a_phased_fusion_takes_the_shims_channels_a_phase_at_a_time():
    """Place a fusion past the shim's sending channels once it runs a sequence a phase.

    Eight multiply lanes reading two inputs and eight down-projection lanes need 24
    sending channels at once, past npu2's 16: as one sequence they do not place; a
    sequence a phase, 16 then 8, they do.
    """
    whole = _composed(
        _mul_down_recording("one_sequence", *_mul_down(mul_cols=8)),
        (_mul_down_fusion(False),),
    )
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(whole))
    assert diagnostic is not None and "16/16 output channels used" in diagnostic
    text = _composed(
        _mul_down_recording("a_sequence_a_phase", *_mul_down(mul_cols=8)),
        (_mul_down_fusion(True),),
    )
    with ir.Context(), ir.Location.unknown():
        diagnostic = places(ir.Module.parse(text))
    assert diagnostic is None, diagnostic
    assert "aiex.run @sequence_1(" in text and "aiex.run @sequence_1(" not in whole


def test_a_phase_awaits_its_fills_before_the_next_phase_takes_its_channels():
    """End a phase only once its fills complete, as a dispatch ends.

    mlir-aie lets the next phase's sequence reuse the shim channels and descriptors the
    phase used; freed without an await (the multiply's phase drains nothing), they were
    reused in flight and Llama decode's 9-step window hung at 8 GEMV lanes.
    """
    text = _composed(
        _mul_down_recording("awaited_phases", *_mul_down(mul_cols=8)),
        (_mul_down_fusion(True),),
    )
    first = text[text.index("aie.runtime_sequence(") :]
    first = first[: first.index("aie.runtime_sequence @sequence_1")]
    starts = first.count("aiex.dma_start_task")
    assert starts == 16 and first.count("aiex.dma_await_task") == starts, first
    assert first.rindex("aiex.dma_await_task") < first.index(
        "aiex.dma_free_task"
    ), first


def test_a_phased_fusion_is_refused_on_an_xclbin():
    """Refuse a phased fusion an xclbin per step would build, before any cache lookup.

    A pack has no phases at all.
    """
    with pytest.raises(ValueError, match="no phases to run apart"):
        Fusion(FusionKind.PACK, (0, 1), phased=True)
    mul, down = _mul_down()
    with pytest.raises(ValueError, match="an xclbin's one kernel cannot"):
        FusedDesign(_mul_down_fusion(True), [mul.resolved(), down.resolved()])
    FusedDesign(_mul_down_fusion(False), [mul.resolved(), down.resolved()])


def test_a_phased_fusion_is_its_own_build():
    """Name a phased fusion apart from its members unphased: their modules differ.

    So neither hits the other's cached ELF, and both may sit in one recording.
    """
    names = ["m", "d"]
    assert _mul_down_fusion(True).name(names) != _mul_down_fusion(False).name(names)
    identities = []
    for phased in (False, True):
        image = Image(
            _mul_down_recording("phased_identity", *_mul_down()),
            FullELF(),
            fusions=(_mul_down_fusion(phased),),
        )
        image._prepare()
        identities.append(Composition(image).identity)
    assert identities[0] != identities[1]


def test_staged_edges_run_forward():
    with pytest.raises(ValueError, match="run forward"):
        Fusion(FusionKind.STAGED, (0, 1), (Edge(1, "y", 0, "x"),))


def test_staged_fusion_builds_one_per_step_module():
    """A per-step image builds a staged fusion as one ``FusedDesign``, the same members and links as the full ELF's, which places."""
    add, norm = _add_norm()
    image = Image(
        _add_norm_recording("staged_perstep", add, norm),
        PerStep(),
        fusions=(_staged(Edge(0, "y", 1, "x")),),
    )
    image._prepare()
    design = FusedDesign(image.fusions[0], [s.op for s in image.steps])
    dispatch = {v.symbol: 1 for d in design.designs for v in d.op.values}
    text = str(design.module(**dispatch))
    assert text.count("aie.objectfifo.link") == 4


# ---------------------------------------------------------------------------
# candidates(): staged edges and fan-out windows.
# ---------------------------------------------------------------------------


def test_candidates_stage_an_edge_a_stream_refuses():
    add, norm = _add_norm()
    recording = _add_norm_recording("staged_candidates", add, norm)
    assert candidates(recording, (FusionKind.STREAM,)) == ()
    assert candidates(recording) == (_staged(Edge(0, "y", 1, "x")),)


def test_candidates_fan_out_to_every_reader():
    """SiLU's output, read by both ElementwiseMuls, fans out to both; no window feeds one of them alone."""
    recording = _silu_muls_recording("fan_out_candidates", *_silu_muls())
    assert candidates(recording) == (_silu_muls_fusion(),)


def test_candidates_fan_out_into_b_a_flipped_flag_streams():
    """q/k/v as recorded (``feed_b`` False) take B riding A; the fan-out is still proposed, for a tuner to run at the setting that builds."""
    norm = RMSNorm(rows=1, tile_size=2048)
    q, k, v = (
        GEMV(M=m, K=2048, num_aie_columns=c) for m, c in ((2048, 8), (512, 4), (512, 2))
    )
    recording = _norm_qkv_recording("fan_out_flag", norm, q, k, v)
    assert _norm_qkv_fusion() in candidates(recording)
    assert not any(s.op.resolved().feed_b for s in recording.steps[1:])


def test_profile_round_trips_staged_and_fan_out_entries(tmp_path):
    add, norm = _add_norm()
    silu, mul1, mul2 = _silu_muls()
    profile = Profile()
    profile.add_fusion(
        FusionKind.STAGED,
        [(ElementwiseAdd, {"size": 8 * 2048}), (RMSNorm, {"rows": 8})],
        [(0, "y", 1, "x")],
    )
    profile.add_fusion(
        FusionKind.STREAM,
        [(SiLU, None), (ElementwiseMul, None), (ElementwiseMul, None)],
        [(0, "y", 1, "a"), (0, "y", 2, "a")],
    )
    path = tmp_path / "npu2.json"
    profile.save(path)
    loaded = Profile.load(path)
    assert loaded.fusions() == profile.fusions()
    assert loaded.fused(
        FusionKind.STAGED, [add.resolved(), norm.resolved()], [(0, "y", 1, "x")]
    )
    assert loaded.fused(
        FusionKind.STREAM,
        [silu.resolved(), mul1.resolved(), mul2.resolved()],
        [(0, "y", 1, "a"), (0, "y", 2, "a")],
    )


def test_llama_1b_decode_fuses_its_mlp_up_to_the_down_projection():
    """Llama 1B's decode step (its shape, one layer): the gate and up projections each feed SiLU and the multiply, a window whose edges skip a step."""
    model = llama_1b(num_hidden_layers=1)
    decode = model.record(**model.shapes()[0])
    found = set()
    for fusion in candidates(decode):
        lo = fusion.steps[0]
        names = tuple(
            type(decode.steps[s].op.resolved()).__name__ for s in fusion.steps
        )
        wiring = tuple(
            (e.producer - lo, e.output, e.consumer - lo, e.input) for e in fusion.edges
        )
        found.add((fusion.kind, names, wiring))
    assert (
        FusionKind.STREAM,
        ("GEMV", "GEMV", "SiLU", "ElementwiseMul"),
        ((0, "C", 2, "x"), (1, "C", 3, "b"), (2, "y", 3, "a")),
    ) in found


def test_a_fused_sequence_pushes_every_task_before_it_waits():
    """The MLP window's one sequence issues every transfer before its first wait, and no channel more than its task queue holds."""
    text = _composed(_mlp_recording("mlp_order", *_mlp()), (_mlp_fusion(),))
    (fused,) = re.findall(r"aie\.device\(npu2\) @(fusion\S+) \{", text)
    body = text[text.index(f"@{fused} {{") :]
    body = body[body.index("aie.runtime_sequence") : body.index("aie.device(", 1)]
    tasks, ops = {}, []
    for m in re.finditer(
        r"(%\S+) = aiex\.dma_configure_task_for @(\S+) \{|"
        r"aiex\.dma_start_task\((%[^)]+)\)|aiex\.dma_await_task",
        body,
    ):
        if m.group(1):
            tasks[m.group(1)] = m.group(2)
        else:
            ops.append(tasks[m.group(3)] if m.group(3) else None)
    first_wait = ops.index(None)
    assert all(op is None for op in ops[first_wait:])
    depth = aie_utils.get_current_device().dma_task_queue_depth
    pushes = {op: ops[:first_wait].count(op) for op in ops[:first_wait]}
    assert max(pushes.values()) <= depth, pushes


# ---------------------------------------------------------------------------
# On the device: each held to numpy and bit-equal to the steps unfused, full
# ELF and per-step, and timed fused against unfused the tuner's way
# (time_interleaved: each image's calls in turn within a round).
# ---------------------------------------------------------------------------


def _record_times(record_property, fused_run, plain_run, label):
    fused, plain = time_interleaved(
        [fused_run, plain_run], Timing(rounds=20), log=lambda _: None
    )
    record_property(f"{label} fused min us", min(fused.samples_us))
    record_property(f"{label} fused median us", statistics.median(fused.samples_us))
    record_property(f"{label} unfused min us", min(plain.samples_us))
    record_property(f"{label} unfused median us", statistics.median(plain.samples_us))


def _dispatch(run, inputs, outputs):
    for name, data in inputs.items():
        run.get_buffer(BufferRef(name)).numpy_view()[: data.size] = data.reshape(-1)
    run()
    return {
        name: run.get_buffer(BufferRef(name)).numpy()[:size].copy()
        for name, size in outputs.items()
    }


def _bit_equal(fused, plain):
    for name in fused:
        assert np.array_equal(
            fused[name].view(np.uint16), plain[name].view(np.uint16)
        ), f"{name}: the fused and unfused devices differ"


PACKAGINGS = [
    pytest.param(FullELF, id="full_elf"),
    pytest.param(PerStep, id="per_step"),
]


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("packaging", PACKAGINGS)
def test_join_add_into_norm_matches_reference_and_unfused(packaging, record_property):
    """(a) ElementwiseAdd's eight lanes joined in pairs into RMSNorm's four."""

    def build(fusions):
        add, norm = _add_norm()
        image = Image(
            _add_norm_recording("staged_add_norm", add, norm),
            packaging(),
            fusions=fusions,
        )
        image.compile()
        return image.get_callable(), add, norm

    fused_run, add, norm = build((_staged(Edge(0, "y", 1, "x")),))
    plain_run, _, _ = build(())
    a = vectors(add).inputs["a"]
    b = vectors(add, seed=7).inputs["b"]
    ref = np.asarray(norm.reference(add.reference(a, b))).reshape(-1)
    inputs, outputs = {"a": a, "b": b}, {"out": ref.size}
    fused = _dispatch(fused_run, inputs, outputs)
    plain = _dispatch(plain_run, inputs, outputs)
    tol = Tolerance.bf16_ulps(
        3,
        atol=norm.tolerance().atol,
        note="the add's 1 ulp through the normalization, RMSNorm's own, and "
        "both roundings",
    )
    verdict = compare(fused["out"], ref, tol)
    assert verdict, verdict.detail
    _bit_equal(fused, plain)
    _record_times(record_property, fused_run, plain_run, packaging.__name__)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("packaging", PACKAGINGS)
def test_split_norm_into_mul_matches_reference_and_unfused(packaging, record_property):
    """RMSNorm's one lane split into ElementwiseMul's four, a slot of each object."""

    def build(fusions):
        norm, mul = _norm_mul(4)
        image = Image(
            _norm_mul_recording("staged_norm_mul", norm, mul),
            packaging(),
            fusions=fusions,
        )
        image.compile()
        return image.get_callable(), norm, mul

    fused_run, norm, mul = build((_staged(Edge(0, "y", 1, "a")),))
    plain_run, _, _ = build(())
    x = vectors(norm).inputs["x"]
    up = vectors(mul, seed=7).inputs["b"]
    ref = np.asarray(mul.reference(norm.reference(x), up)).reshape(-1)
    inputs, outputs = {"x": x, "up": up}, {"out": ref.size}
    fused = _dispatch(fused_run, inputs, outputs)
    plain = _dispatch(plain_run, inputs, outputs)
    tol = Tolerance.bf16_ulps(
        3,
        atol=mul.tolerance().atol,
        note="RMSNorm's 1 ulp through the multiply (2), plus both roundings",
    )
    verdict = compare(fused["out"], ref, tol)
    assert verdict, verdict.detail
    _bit_equal(fused, plain)
    _record_times(record_property, fused_run, plain_run, packaging.__name__)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("packaging", PACKAGINGS)
def test_gather_broadcast_into_down_proj_matches_reference_and_unfused(
    packaging, record_property
):
    """(b) The gated product's lanes gathered into the whole vector every core of Llama decode's down_proj (M=2048, K=8192) reads."""

    def build(fusions):
        mul, down = _mul_down()
        image = Image(
            _mul_down_recording("staged_mul_down", mul, down),
            packaging(),
            fusions=fusions,
        )
        image.compile()
        return image.get_callable(), mul, down

    fused_run, mul, down = build((_staged(Edge(0, "y", 1, "B")),))
    plain_run, _, _ = build(())
    g = vectors(mul).inputs["a"]
    u = vectors(mul, seed=7).inputs["b"]
    W = vectors(down, seed=11).inputs["A"]
    ref = np.asarray(down.reference(W, mul.reference(g, u))).reshape(-1)
    inputs, outputs = {"g": g, "u": u, "W": W}, {"out": ref.size}
    fused = _dispatch(fused_run, inputs, outputs)
    plain = _dispatch(plain_run, inputs, outputs)
    verdict = compare(fused["out"], ref, down.tolerance())
    assert verdict, verdict.detail
    _bit_equal(fused, plain)
    _record_times(record_property, fused_run, plain_run, packaging.__name__)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("packaging", PACKAGINGS)
def test_join_of_joins_into_down_proj_matches_reference_and_unfused(
    packaging, record_property
):
    """(b) at eight producer lanes: SiLU's lanes gathered, four and four then two, into the whole vector every down_proj core reads."""

    def build(fusions):
        silu, down = _silu_down()
        image = Image(
            _silu_down_recording("staged_silu_down", silu, down),
            packaging(),
            fusions=fusions,
        )
        image.compile()
        return image.get_callable(), silu, down

    fused_run, silu, down = build((_staged(Edge(0, "y", 1, "B")),))
    plain_run, _, _ = build(())
    x = vectors(silu).inputs["x"]
    W = vectors(down, seed=11).inputs["A"]
    ref = np.asarray(down.reference(W, silu.reference(x))).reshape(-1)
    inputs, outputs = {"x": x, "W": W}, {"out": ref.size}
    fused = _dispatch(fused_run, inputs, outputs)
    plain = _dispatch(plain_run, inputs, outputs)
    verdict = compare(fused["out"], ref, down.tolerance())
    assert verdict, verdict.detail
    _bit_equal(fused, plain)
    _record_times(record_property, fused_run, plain_run, packaging.__name__)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("packaging", PACKAGINGS)
@pytest.mark.parametrize("columns", [(2, 1, 1), (8, 4, 2)])
def test_fan_out_norm_into_qkv_matches_reference_and_unfused(
    packaging, columns, record_property
):
    """(c) The normed row fanned out to Llama decode's q/k/v projections, each core of each reading it, the three run concurrently."""

    def build(fusions):
        norm, q, k, v = _norm_qkv(columns)
        image = Image(
            _norm_qkv_recording("fan_out_qkv", norm, q, k, v),
            packaging(),
            fusions=fusions,
        )
        image.compile()
        return image.get_callable(), norm, q, k, v

    fused_run, norm, q, k, v = build((_norm_qkv_fusion(),))
    plain_run, _, _, _, _ = build(())
    x = vectors(norm).inputs["x"]
    n = np.asarray(norm.reference(x))
    weights = {
        name: vectors(op, seed=seed).inputs["A"]
        for name, op, seed in (("Aq", q, 7), ("Ak", k, 11), ("Av", v, 13))
    }
    refs = {
        "oq": np.asarray(q.reference(weights["Aq"], n)).reshape(-1),
        "ok": np.asarray(k.reference(weights["Ak"], n)).reshape(-1),
        "ov": np.asarray(v.reference(weights["Av"], n)).reshape(-1),
    }
    inputs = {"x": x, **weights}
    outputs = {name: ref.size for name, ref in refs.items()}
    fused = _dispatch(fused_run, inputs, outputs)
    plain = _dispatch(plain_run, inputs, outputs)
    for name, ref in refs.items():
        verdict = compare(fused[name], ref, q.tolerance())
        assert verdict, f"{name}: {verdict.detail}"
    _bit_equal(fused, plain)
    _record_times(record_property, fused_run, plain_run, packaging.__name__)


@pytest.mark.supported_devices("npu2")
def test_fan_out_silu_into_two_muls_matches_reference_and_unfused():
    """SiLU's output fanned out to two ElementwiseMuls of one design."""

    def build(fusions):
        silu, mul1, mul2 = _silu_muls()
        image = Image(
            _silu_muls_recording("fan_out_silu", silu, mul1, mul2),
            FullELF(),
            fusions=fusions,
        )
        image.compile()
        return image.get_callable(), silu, mul1

    fused_run, silu, mul = build((_silu_muls_fusion(),))
    plain_run, _, _ = build(())
    x = vectors(silu).inputs["x"]
    up1 = vectors(mul, seed=7).inputs["b"]
    up2 = vectors(mul, seed=11).inputs["b"]
    y = silu.reference(x)
    refs = {
        "out1": np.asarray(mul.reference(y, up1)).reshape(-1),
        "out2": np.asarray(mul.reference(y, up2)).reshape(-1),
    }
    inputs = {"x": x, "up1": up1, "up2": up2}
    outputs = {name: ref.size for name, ref in refs.items()}
    fused = _dispatch(fused_run, inputs, outputs)
    plain = _dispatch(plain_run, inputs, outputs)
    tol = Tolerance.bf16_ulps(
        3,
        atol=mul.tolerance().atol,
        note="SiLU's 1 ulp through the multiply (2), plus both roundings",
    )
    for name, ref in refs.items():
        verdict = compare(fused[name], ref, tol)
        assert verdict, f"{name}: {verdict.detail}"
    _bit_equal(fused, plain)


@pytest.mark.supported_devices("npu2")
def test_bounded_staged_pair_matches_across_per_call_counts():
    """The bounded join (SiLU's eight lanes into Mul's four), compiled once and called at several counts, whole rounds and not."""
    profile = Profile()
    profile.add_fusion(
        FusionKind.STAGED, [(SiLU, {}), (ElementwiseMul, {})], [(0, "y", 1, "a")]
    )
    staged_graph = _bounded()
    staged_graph.profile = profile
    staged = staged_graph.compile(x=(BOUNDED_SIZE,), up=(BOUNDED_SIZE,))
    assert staged.sequence.fusions, "the profile's staged fusion was not taken"
    staged.load()
    plain = _bounded().compile(x=(BOUNDED_SIZE,), up=(BOUNDED_SIZE,))
    plain.load()
    rng = np.random.default_rng(3)
    x = rng.standard_normal(BOUNDED_SIZE).astype(np.float32).astype(bfloat16)
    up = rng.standard_normal(BOUNDED_SIZE).astype(np.float32).astype(bfloat16)
    for n in (BOUNDED_SIZE, 16384, 2048, 3 * 16384 + 512):
        out = np.asarray(staged(x, up, n=n))[:n]
        baseline = np.asarray(plain(x, up, n=n))[:n]
        want = np.asarray(staged_graph.reference(x, up, n=n))[:n]
        assert np.array_equal(
            out.view(np.uint16), baseline.view(np.uint16)
        ), f"n={n}: the staged and unfused devices differ"
        verdict = compare(
            out,
            want,
            Tolerance.bf16_ulps(
                3,
                atol=1.2e-38,
                note="SiLU's 1 ulp through the multiply, both roundings",
            ),
        )
        assert verdict, f"n={n}: {verdict.detail}"


def _run_mlp(packaging_name: str) -> list:
    """Return the MLP window's output fused, then apart."""
    packaging = {"full_elf": FullELF, "per_step": PerStep}[packaging_name]
    outs = []
    for fusions in ((_mlp_fusion(),), ()):
        gate, up, silu, mul = _mlp()
        image = Image(
            _mlp_recording("mlp_device", gate, up, silu, mul),
            packaging(),
            fusions=fusions,
        )
        image.compile()
        run = image.get_callable()
        x = vectors(gate).inputs["B"]
        # The profile may code A: each buffer holds the form its GEMV reads.
        inputs = {
            "Wg": gate.resolved().A.device_form(vectors(gate, seed=3).inputs["A"]),
            "Wu": up.resolved().A.device_form(vectors(up, seed=5).inputs["A"]),
            "x": x,
        }
        outs.append(_dispatch(run, inputs, {"out": 8192})["out"])
    return outs


def _run_skip(packaging_name: str) -> list:
    """Return the skip window's output fused, then apart."""
    packaging = {"full_elf": FullELF, "per_step": PerStep}[packaging_name]
    outs = []
    for fusions in ((_skip_fusion(),), ()):
        add, norm, proj, add2 = _skip()
        image = Image(
            _skip_recording("skip_device", add, norm, proj, add2),
            packaging(),
            fusions=fusions,
        )
        image.compile()
        inputs = {
            "a": vectors(add).inputs["a"],
            "b": vectors(add, seed=7).inputs["b"],
            "W": proj.resolved().A.device_form(vectors(proj, seed=3).inputs["A"]),
        }
        outs.append(_dispatch(image.get_callable(), inputs, {"out": 2048})["out"])
    return outs


# Ample for two compiles and two dispatches.
_MLP_TIMEOUT_S = 900


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("packaging", ["full_elf", "per_step"])
def test_mlp_window_matches_reference_and_unfused(packaging):
    """Llama decode's gate/up projections, SiLU and the multiply fused as one window, run in a child process a hang cannot outlive."""
    fused, apart = hang.bounded(_MLP_TIMEOUT_S, _run_mlp, packaging)
    gate, up, silu, mul = (op.resolved() for op in _mlp())
    x = vectors(gate).inputs["B"]
    ref = np.asarray(
        mul.reference(
            silu.reference(gate.reference(vectors(gate, seed=3).inputs["A"], x)),
            up.reference(vectors(up, seed=5).inputs["A"], x),
        )
    ).reshape(-1)
    verdict = compare(fused, ref, gate.tolerance())
    assert verdict, verdict.detail
    _bit_equal({"out": fused}, {"out": apart})


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("packaging", ["full_elf", "per_step"])
def test_a_reader_a_phase_later_does_not_hang(packaging):
    """Run a residual add read by the norm and, past the GEMV, by a second add.

    In a child process a hang cannot outlive, it matches the reference and the steps
    apart; with two-deep ends it timed out on the device.
    """
    fused, apart = hang.bounded(_MLP_TIMEOUT_S, _run_skip, packaging)
    add, norm, proj, add2 = (op.resolved() for op in _skip())
    a, b = vectors(add).inputs["a"], vectors(add, seed=7).inputs["b"]
    h = add.reference(a, b)
    g = proj.reference(vectors(proj, seed=3).inputs["A"], norm.reference(h))
    ref = np.asarray(add2.reference(g, h)).reshape(-1)
    verdict = compare(fused, ref, proj.tolerance())
    assert verdict, verdict.detail
    _bit_equal({"out": fused}, {"out": apart})


def _phased_window(window: str):
    """Return a phased window's recording, fusion and inputs, by name, and its reference."""
    if window == "mul_down":
        # Sixteen multiply lanes then eight GEMV lanes: the phases take the shim's
        # sending channels in turn.
        mul, down = _mul_down(mul_cols=8)
        rec = _mul_down_recording("phased_mul_down", mul, down)
        fusion = _mul_down_fusion(True)
        g, u = vectors(mul).inputs["a"], vectors(mul, seed=7).inputs["b"]
        W = vectors(down, seed=11).inputs["A"]
        inputs = {"g": g, "u": u, "W": down.resolved().A.device_form(W)}
        ref = down.resolved().reference(W, mul.resolved().reference(g, u))
        return rec, fusion, inputs, np.asarray(ref).reshape(-1), down
    if window == "skip":
        add, norm, proj, add2 = _skip()
        rec = _skip_recording("phased_skip", add, norm, proj, add2)
        fusion = Fusion(
            FusionKind.STAGED, (0, 1, 2, 3), _skip_fusion().edges, phased=True
        )
        a, b = vectors(add).inputs["a"], vectors(add, seed=7).inputs["b"]
        W = vectors(proj, seed=3).inputs["A"]
        inputs = {"a": a, "b": b, "W": proj.resolved().A.device_form(W)}
        h = add.resolved().reference(a, b)
        g = proj.resolved().reference(W, norm.resolved().reference(h))
        return (
            rec,
            fusion,
            inputs,
            np.asarray(add2.resolved().reference(g, h)).reshape(-1),
            proj,
        )
    ops, steps, order = _residual(mul_first=True)
    mul, add, proj, add2 = ops
    rec = _residual_recording("phased_residual", order, steps)
    a, b = vectors(add).inputs["a"], vectors(add, seed=7).inputs["b"]
    c, d = vectors(mul).inputs["a"], vectors(mul, seed=5).inputs["b"]
    W = vectors(proj, seed=3).inputs["A"]
    inputs = {"a": a, "b": b, "c": c, "d": d, "W": proj.resolved().A.device_form(W)}
    g = proj.resolved().reference(W, mul.resolved().reference(c, d))
    ref = add2.resolved().reference(g, add.resolved().reference(a, b))
    return rec, _residual_fusion(order), inputs, np.asarray(ref).reshape(-1), proj


def _run_phased(window: str) -> list:
    """Return the window's output run phased, then apart, in a full ELF."""
    outs = []
    for fused in (True, False):
        rec, fusion, inputs, ref, _ = _phased_window(window)
        image = Image(rec, FullELF(), fusions=(fusion,) if fused else ())
        image.compile()
        outs.append(_dispatch(image.get_callable(), inputs, {"out": ref.size})["out"])
    return outs


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("window", ["mul_down", "skip", "residual"])
def test_a_phased_window_matches_reference_and_unfused(window):
    """Run a window a sequence a phase on the device, in a child a hang cannot outlive.

    The multiply into the down projection takes the shim's channels in turn; the skip
    window's second add reads the first two phases on; the residual add runs with its
    only reader, a phase after the multiply. Each matches numpy and the steps apart.
    """
    fused, apart = hang.bounded(_MLP_TIMEOUT_S, _run_phased, window)
    _, _, _, ref, gemv = _phased_window(window)
    verdict = compare(fused, ref, gemv.resolved().tolerance())
    assert verdict, verdict.detail
    _bit_equal({"out": fused}, {"out": apart})
