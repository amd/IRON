#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Infrastructure tests for :mod:`iron.common.allocator`, the memory planner.

Pure logic over synthetic runlists -- no operators, no toolchain, no hardware.
The properties that matter are: a plan never lets two simultaneously-live
buffers share bytes (correctness), it reaches the peak-liveness lower bound on
the shapes real models produce (quality), and it leaves host-addressed buffers
alone (pinning).
"""

import pytest

from iron.common.base import AIERuntimeArgSpec
from iron.common.allocator import LiveRange, live_ranges, peak_live_bytes, plan


class Op:
    """Stand-in operator: N inputs then M outputs, with real arg specs."""

    def __init__(self, n_in, n_out=1):
        self.specs = [AIERuntimeArgSpec("in", (1,))] * n_in + [
            AIERuntimeArgSpec("out", (1,))
        ] * n_out

    def get_arg_spec(self):
        return self.specs


def steps_of(runlist):
    """The (reads, writes) of each entry, which is all liveness needs."""
    steps = []
    for op, *bufs in runlist:
        specs = op.get_arg_spec()
        steps.append(
            (
                [b for b, s in zip(bufs, specs) if s.reads],
                [b for b, s in zip(bufs, specs) if s.writes],
            )
        )
    return steps


def assert_no_overlap(allocations, ranges):
    """No two buffers alive at the same step may share a byte."""
    items = list(allocations.values())
    for i, a in enumerate(items):
        for b in items[i + 1 :]:
            if not ranges[a.name].overlaps(ranges[b.name]):
                continue
            assert a.offset >= b.offset + b.size or b.offset >= a.offset + a.size, (
                f"{a.name}@{a.offset}+{a.size} overlaps {b.name}@{b.offset}+{b.size} "
                f"while both live"
            )


def test_live_range_overlap():
    assert LiveRange(0, 5).overlaps(LiveRange(5, 9))  # touching counts
    assert not LiveRange(0, 4).overlaps(LiveRange(5, 9))
    assert LiveRange(2, 3).overlaps(LiveRange(0, 9))  # nested


def test_sequential_chain_double_buffers():
    """a -> b -> c needs exactly two slots, and alternates between them.

    A step that reads ``a`` and writes ``b`` has both live at that step, so
    they may not share an address -- writing ``b`` would clobber ``a`` mid-read.
    (Only an operator that declares itself in-place could, and none here do.)
    Two slots therefore suffice and are necessary: the chain ping-pongs.
    """
    op = Op(1)
    runlist = [(op, "x", "a"), (op, "a", "b"), (op, "b", "c"), (op, "c", "out")]
    ranges = live_ranges(steps_of(runlist))
    sizes = dict.fromkeys(ranges, 1024)
    allocations, pool = plan(ranges, sizes)
    assert pool == 2048, f"a chain should ping-pong between two slots, got {pool}"
    assert allocations["a"].offset == allocations["c"].offset, "a and c should alias"
    assert pool == peak_live_bytes(ranges, sizes)
    assert_no_overlap(allocations, ranges)


def test_simultaneously_live_buffers_do_not_share():
    """Fan-out then fan-in: both branches are live together, so both are resident."""
    unary, binary = Op(1), Op(2)
    runlist = [
        (unary, "x", "left"),
        (unary, "x", "right"),
        (binary, "left", "right", "out"),
    ]
    ranges = live_ranges(steps_of(runlist))
    sizes = dict.fromkeys(ranges, 4096)
    allocations, pool = plan(ranges, sizes)
    assert pool == 8192, f"two co-live buffers need both slots, got {pool}"
    assert_no_overlap(allocations, ranges)


def test_pinned_buffers_are_not_pooled():
    op = Op(1)
    runlist = [(op, "x", "scratch"), (op, "scratch", "keep"), (op, "keep", "out")]
    ranges = live_ranges(steps_of(runlist), pinned={"keep"})
    assert "keep" not in ranges
    assert "scratch" in ranges


def test_graph_inputs_and_outputs_are_left_alone():
    """Values the host supplies or reads back outlive the sequence."""
    op = Op(1)
    runlist = [(op, "x", "mid"), (op, "mid", "logits")]
    ranges = live_ranges(steps_of(runlist))
    assert "x" not in ranges, "an input is never written; not ours to pool"
    assert "logits" not in ranges, "an output is never read again; host reads it"
    assert "mid" in ranges


def test_repeated_block_packs_to_one_block_worth():
    """The Phase 1 claim: N identical layers cost one layer's scratch.

    This is the shape a recorded transformer produces once capture names every
    intermediate itself -- 16 copies of each scratch buffer, none of which are
    live at the same time.
    """
    unary = Op(1)
    runlist, prev = [], "x"
    for layer in range(16):
        runlist.append((unary, prev, f"h_{layer}"))
        runlist.append((unary, f"h_{layer}", f"t_{layer}"))
        prev = f"t_{layer}"
    runlist.append((unary, prev, "logits"))

    ranges = live_ranges(steps_of(runlist))
    sizes = {n: 1 << 20 for n in ranges}
    allocations, pool = plan(ranges, sizes)

    naive = sum(sizes.values())
    assert pool == peak_live_bytes(ranges, sizes), "should hit the lower bound"
    assert pool <= 2 << 20, f"16 layers should fold to two slots, got {pool}"
    assert pool < naive // 10, f"expected a big win over {naive}, got {pool}"
    assert_no_overlap(allocations, ranges)


def test_mixed_sizes_reach_the_lower_bound():
    """Greedy-by-size + best-fit should match peak liveness on ragged sizes."""
    unary = Op(1)
    runlist, prev = [], "x"
    for i in range(12):
        runlist.append((unary, prev, f"b{i}"))
        prev = f"b{i}"
    runlist.append((unary, prev, "out"))
    ranges = live_ranges(steps_of(runlist))
    sizes = {n: (1 + (i * 7) % 5) * 4096 for i, n in enumerate(sorted(ranges))}
    allocations, pool = plan(ranges, sizes)
    assert pool == peak_live_bytes(ranges, sizes)
    assert_no_overlap(allocations, ranges)


def test_offsets_are_aligned():
    unary, binary = Op(1), Op(2)
    runlist = [(unary, "x", "a"), (unary, "x", "b"), (binary, "a", "b", "out")]
    ranges = live_ranges(steps_of(runlist))
    sizes = {n: 100 for n in ranges}  # deliberately not a multiple of 64
    allocations, _ = plan(ranges, sizes, alignment=64)
    for a in allocations.values():
        assert a.offset % 64 == 0, f"{a.name} at unaligned offset {a.offset}"


def test_empty_graph():
    allocations, pool = plan({}, {})
    assert allocations == {} and pool == 0


# --- integration with OperatorSequence's arena layout -----------------------


@pytest.fixture(autouse=True)
def device():
    """Operators read the ShimDMA limit at construction, so one must be set.

    Without it get_current_device() returns None and construction dies with
    "'NoneType' object has no attribute 'resolve'" -- which reads like a bug in
    the code under test rather than a missing fixture.
    """
    import aie.utils as aie_utils
    from aie.iron.device import from_name

    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)


def _two_step_sequence(buffer_offsets):
    """A tiny real sequence: one weight-like buffer plus one intermediate."""
    from iron.common.context import AIEContext
    from iron.common.sequence import OperatorSequence
    from iron.operators import ElementwiseAdd

    add = ElementwiseAdd(size=1024, tile_size=128, context=AIEContext())
    runlist = [(add, "w", "x", "t0"), (add, "w", "t0", "out")]
    seq = OperatorSequence(
        "alloc_layout_probe",
        runlist,
        input_args=["x"],
        output_args=["out"],
        dispatch="reference",
        buffer_offsets=buffer_offsets,
    )
    layout, sizes, _ = seq.calculate_buffer_layout()
    return layout, sizes


def test_planned_offsets_do_not_collide_with_unplanned():
    """Planned scratch must be placed past every unplanned buffer.

    Regression: offsets were applied from 0, so a planned intermediate landed
    on top of the weights. It showed up as an arena that did not grow at all
    when planned buffers were added -- the aliasing was silent.
    """
    layout, _ = _two_step_sequence({"t0": 0})
    _, w_off, w_len = layout["w"]
    _, t_off, _ = layout["t0"]
    assert t_off >= w_off + w_len, (
        f"planned t0@{t_off} overlaps unplanned w@{w_off}+{w_len}; "
        "planned buffers must occupy their own region"
    )


def test_layout_is_unchanged_without_offsets():
    """The default path must lay out exactly as it did before.

    Buffers are split across three arenas (input, output, scratch), each
    starting at zero, so packing is checked per arena.
    """
    layout, _ = _two_step_sequence(None)
    arenas = {}
    for buf_type, off, ln in layout.values():
        arenas.setdefault(buf_type, []).append((off, ln))
    for buf_type, entries in arenas.items():
        cursor = 0
        for off, ln in sorted(entries):
            assert off == cursor, f"{buf_type} buffers should pack back to back"
            cursor += ln


def _chain(n_intermediates, plan_scratch):
    """A chain where each intermediate dies as the next is produced."""
    from iron.common.context import AIEContext
    from iron.common.sequence import OperatorSequence
    from iron.operators import ElementwiseAdd

    add = ElementwiseAdd(size=1024, tile_size=128, context=AIEContext())
    names = [f"t{i}" for i in range(n_intermediates)]
    runlist = [(add, "x", "w", names[0])]
    for prev, nxt in zip(names, names[1:]):
        runlist.append((add, prev, "w", nxt))
    runlist.append((add, names[-1], "w", "out"))
    seq = OperatorSequence(
        f"chain{n_intermediates}_{plan_scratch}",
        runlist,
        input_args=["x", "w"],
        output_args=["out"],
        dispatch="reference",
        plan_scratch=plan_scratch,
    )
    layout, sizes, _ = seq.calculate_buffer_layout()
    return layout, sizes[2]


def test_planning_reuses_addresses_of_dead_intermediates():
    """A chain of four holds at most two intermediates live at once."""
    _, unplanned = _chain(4, plan_scratch=False)
    _, planned = _chain(4, plan_scratch=True)
    assert planned < unplanned, "planning should shrink the scratch arena"


def test_planned_buffers_never_share_bytes_while_both_live():
    """The invariant a liveness bug would break, stated directly.

    This is the one failure mode in planning that does not announce itself:
    two buffers aliased while both are live produce wrong numbers, not a crash.
    """
    from iron.common.allocator import LiveRange

    layout, _ = _chain(4, plan_scratch=True)
    scratch = {k: v for k, v in layout.items() if v[0] == "scratch"}
    # t_i is live from step i to step i+1, so consecutive ones overlap.
    for i in range(3):
        a, b = scratch.get(f"t{i}"), scratch.get(f"t{i+1}")
        if a is None or b is None:
            continue
        assert LiveRange(i, i + 1).overlaps(LiveRange(i + 1, i + 2))
        a_lo, a_hi = a[1], a[1] + a[2]
        b_lo, b_hi = b[1], b[1] + b[2]
        assert a_hi <= b_lo or b_hi <= a_lo, (
            f"t{i}@[{a_lo},{a_hi}) and t{i+1}@[{b_lo},{b_hi}) overlap in bytes "
            "while both are live"
        )


def test_slices_are_never_pooled():
    """A slice has to sit at its parent's offset plus its start.

    Pooling one hands it an address unrelated to its parent, and nothing
    raises -- the slice simply reads the wrong memory. Found by probing the
    written-slice case, which the whole-buffer tests above cannot reach.
    """
    from iron.common.context import AIEContext
    from iron.common.sequence import OperatorSequence
    from iron.operators import ElementwiseAdd

    add = ElementwiseAdd(size=1024, tile_size=128, context=AIEContext())
    seq = OperatorSequence(
        "slice_pooling_probe",
        [(add, "x", "w", "big[0:1024]"), (add, "big[0:1024]", "w", "out")],
        input_args=["x", "w"],
        output_args=["out"],
        buffer_sizes={"big": 4096},
        dispatch="reference",
        plan_scratch=True,
    )
    assert not any("[" in name for name in seq.scratch_plan()), (
        "a sliced buffer was given a pooled offset; its address must stay "
        "derived from its parent"
    )
