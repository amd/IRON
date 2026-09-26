#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Infrastructure tests for :mod:`iron.common.image.allocator`, the memory planner.

Pure logic over synthetic runlists -- no operators, no toolchain, no hardware.
The properties that matter are: a plan never lets two simultaneously-live
buffers share bytes (correctness), it reaches the peak-liveness lower bound on
the shapes real models produce (quality), and it leaves host-addressed buffers
alone (pinning).
"""

import random
from types import SimpleNamespace

import pytest

from iron.common.image.allocator import (
    Allocation,
    ArenaPlan,
    LiveRange,
    live_ranges,
    peak_live_bytes,
    place,
    touch_ranges,
)


def _buf(direction):
    return SimpleNamespace(direction=direction, shape=(1,), nbytes=2)


class Op:
    """Stand-in operator: N inputs then M outputs, declared like a real one's buffers."""

    def __init__(self, n_in, n_out=1):
        self.buffers = [_buf("in")] * n_in + [_buf("out")] * n_out


def steps_of(runlist):
    """The (reads, writes) of each entry, which is all liveness needs."""
    steps = []
    for op, *bufs in runlist:
        steps.append(
            (
                [b for b, s in zip(bufs, op.buffers) if s.direction in ("in", "inout")],
                [
                    b
                    for b, s in zip(bufs, op.buffers)
                    if s.direction in ("out", "inout")
                ],
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
    """A -> b -> c needs exactly two slots, and alternates between them.

    A step that reads ``a`` and writes ``b`` has both live at that step, so
    they may not share an address -- writing ``b`` would clobber ``a`` mid-read.
    (Only an operator that declares itself in-place could, and none here do.)
    Two slots therefore suffice and are necessary: the chain ping-pongs.
    """
    op = Op(1)
    runlist = [(op, "x", "a"), (op, "a", "b"), (op, "b", "c"), (op, "c", "out")]
    ranges = live_ranges(steps_of(runlist))
    sizes = dict.fromkeys(ranges, 1024)
    allocations, pool = place(ranges, sizes)
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
    allocations, pool = place(ranges, sizes)
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
    allocations, pool = place(ranges, sizes)

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
    allocations, pool = place(ranges, sizes)
    assert pool == peak_live_bytes(ranges, sizes)
    assert_no_overlap(allocations, ranges)


def test_offsets_are_aligned():
    unary, binary = Op(1), Op(2)
    runlist = [(unary, "x", "a"), (unary, "x", "b"), (binary, "a", "b", "out")]
    ranges = live_ranges(steps_of(runlist))
    sizes = {n: 100 for n in ranges}  # deliberately not a multiple of 64
    allocations, _ = place(ranges, sizes, alignment=64)
    for a in allocations.values():
        assert a.offset % 64 == 0, f"{a.name} at unaligned offset {a.offset}"


def test_empty_graph():
    allocations, pool = place({}, {})
    assert allocations == {} and pool == 0


# --- integration with OperatorSequence's arena layout -----------------------


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _two_step_sequence(buffer_offsets):
    """A tiny real sequence: one weight-like buffer plus one intermediate."""
    from iron.common.image import OperatorSequence
    from iron.operators import ElementwiseAdd

    add = ElementwiseAdd(size=1024, tile_size=128)
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
    from iron.common.image import OperatorSequence
    from iron.operators import ElementwiseAdd

    add = ElementwiseAdd(size=1024, tile_size=128)
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
    from iron.common.image.allocator import LiveRange

    layout, _ = _chain(4, plan_scratch=True)
    scratch = {k: v for k, v in layout.items() if v[0] == "scratch"}
    # t_i is live from step i to step i+1, so consecutive ones overlap.
    for i in range(3):
        a, b = scratch.get(f"t{i}"), scratch.get(f"t{i + 1}")
        if a is None or b is None:
            continue
        assert LiveRange(i, i + 1).overlaps(LiveRange(i + 1, i + 2))
        a_lo, a_hi = a[1], a[1] + a[2]
        b_lo, b_hi = b[1], b[1] + b[2]
        assert a_hi <= b_lo or b_hi <= a_lo, (
            f"t{i}@[{a_lo},{a_hi}) and t{i + 1}@[{b_lo},{b_hi}) overlap in bytes "
            "while both are live"
        )


def test_slices_are_never_pooled():
    """A slice has to sit at its parent's offset plus its start.

    Pooling one hands it an address unrelated to its parent, and nothing
    raises -- the slice simply reads the wrong memory. Found by probing the
    written-slice case, which the whole-buffer tests above cannot reach.
    """
    from iron.common.image import OperatorSequence
    from iron.operators import ElementwiseAdd

    add = ElementwiseAdd(size=1024, tile_size=128)
    seq = OperatorSequence(
        "slice_pooling_probe",
        [(add, "x", "w", "big[0:1024]"), (add, "big[0:1024]", "w", "out")],
        input_args=["x", "w"],
        output_args=["out"],
        buffer_sizes={"big": 4096},
        dispatch="reference",
        plan_scratch=True,
    )
    assert not any("[" in name for name in seq.infer_buffer_offsets()), (
        "a sliced buffer was given a pooled offset; its address must stay "
        "derived from its parent"
    )


# --- touch ranges: the rule for arenas whose host-visible buffers live elsewhere


def test_touch_ranges_span_first_to_last_use_whatever_the_direction():
    steps = [
        ([], ["a"]),  # 0: a written
        (["a"], ["dead"]),  # 1: dead written, never read
        (["early"], ["b"]),  # 2: early read before any write
        (["b", "a"], ["early"]),  # 3
    ]
    ranges = touch_ranges(steps, ["a", "b", "dead", "early", "unused"])
    assert ranges["a"] == LiveRange(0, 3)
    assert ranges["b"] == LiveRange(2, 3)
    assert ranges["dead"] == LiveRange(1, 1), "a dead write still needs its step"
    assert ranges["early"] == LiveRange(2, 3), "read-first still occupies its span"
    assert ranges["unused"] == LiveRange(0, 3), "an untouched buffer is always live"


def test_touch_ranges_ignore_names_not_asked_for():
    ranges = touch_ranges([(["x"], ["y"])], ["y"])
    assert set(ranges) == {"y"}


# --- place with fixed allocations and alignment ------------------------------


def test_fixed_allocations_are_obstacles_at_every_step():
    fixed = [Allocation("w", 0, 1000)]
    ranges = {"t": LiveRange(0, 0), "u": LiveRange(5, 5)}
    allocations, _ = place(ranges, {"t": 64, "u": 64}, 64, fixed=fixed)
    for a in allocations.values():
        assert not a.overlaps(fixed[0]), f"{a} placed over a fixed allocation"
        assert a.offset == 1024, "the first aligned byte past the fixed one"


def test_a_gap_between_fixed_allocations_is_used_when_it_fits():
    fixed = [Allocation("lo", 0, 64), Allocation("hi", 1024, 64)]
    allocations, top = place({"t": LiveRange(0, 0)}, {"t": 900}, 64, fixed=fixed)
    assert allocations["t"].offset == 64
    assert top == 964


def test_odd_sizes_never_leave_an_offset_unaligned():
    """bfp16 blocks are 9 bytes: nothing about a size promises alignment."""
    ranges = {f"b{i}": LiveRange(0, 0) for i in range(6)}
    sizes = {n: 9 * (i + 1) for i, n in enumerate(ranges)}
    fixed = [Allocation("w", 0, 27)]
    allocations, _ = place(ranges, sizes, 128, fixed=fixed)
    for a in allocations.values():
        assert a.offset % 128 == 0, f"{a.name} at {a.offset}"


# --- ArenaPlan: several images over one arena --------------------------------


def _chain_steps(names):
    """X -> names[0] -> ... -> names[-1] -> out, one step per arrow."""
    steps = [(["x"], [names[0]])]
    steps += [([a], [b]) for a, b in zip(names, names[1:])]
    steps.append(([names[-1]], ["out"]))
    return steps


def test_a_resident_has_one_offset_in_every_image():
    arena = ArenaPlan(alignment=64)
    first = arena.place_image(
        [(["w0"], ["t"]), (["t", "cache"], ["cache"])],
        {"w0": 4096, "t": 128, "cache": 1024},
        {"w0": "W0", "cache": "KV"},
    )
    # The second image names the same storage differently and in another order.
    second = arena.place_image(
        [(["kv", "weight"], ["big"]), (["big"], ["kv"])],
        {"weight": 4096, "kv": 1024, "big": 1 << 16},
        {"kv": "KV", "weight": "W0"},
    )
    assert second["weight"].offset == first["w0"].offset
    assert second["kv"].offset == first["cache"].offset
    assert set(arena.residents) == {"W0", "KV"}


def test_transients_of_different_images_share_bytes():
    arena = ArenaPlan(alignment=64)
    sizes = {"w": 4096, "a": 1024, "b": 1024}
    first = arena.place_image(_chain_steps(["a", "b"]), sizes, {"w": "W"})
    size_after_first = arena.size
    second = arena.place_image(_chain_steps(["a", "b"]), sizes, {"w": "W"})
    assert arena.size == size_after_first, "an identical image costs nothing more"
    assert second["a"].offset == first["a"].offset


def test_an_image_added_later_moves_nothing_and_its_residents_go_on_top():
    """Offsets are baked into instruction streams; an earlier image must keep
    running unchanged. A new resident placed below an earlier image's
    transients would be overwritten the next time that image ran.
    """
    arena = ArenaPlan(alignment=64)
    first = arena.place_image(
        _chain_steps(["a", "b"]), {"w": 256, "a": 4096, "b": 4096}, {"w": "W"}
    )
    before = arena.residents
    top_of_first = max(a.end for a in first.values())
    second = arena.place_image(
        _chain_steps(["c"]), {"w": 256, "v": 512, "c": 64}, {"w": "W", "v": "V"}
    )
    assert arena.residents["W"] == before["W"]
    assert second["v"].offset >= top_of_first
    for a in first.values():
        assert not a.overlaps(second["v"]), f"new resident over {a.name} of image 1"


def test_one_storage_is_one_size():
    arena = ArenaPlan()
    arena.place_image([], {"w": 128}, {"w": "W"})
    with pytest.raises(ValueError, match="one storage is one size"):
        arena.place_image([], {"w2": 256}, {"w2": "W"})


def test_a_resident_needs_a_size():
    with pytest.raises(ValueError, match="have no size"):
        ArenaPlan().place_image([], {}, {"w": "W"})


def test_one_image_reaches_the_lower_bound_above_its_residents():
    """The sizes of test_mixed_sizes_reach_the_lower_bound, over a resident:
    the resident must not cost the transients anything but its own bytes.
    """
    arena = ArenaPlan(alignment=64)
    names = [f"b{i}" for i in range(12)]
    sizes = {n: (1 + (i * 7) % 5) * 4096 for i, n in enumerate(sorted(names))}
    sizes["w"] = 8192 + 9
    steps = _chain_steps(names)
    layout = arena.place_image(steps, sizes, {"w": "W"})
    transient = touch_ranges(steps, names)
    bound = peak_live_bytes(transient, sizes)
    top = max(a.end for n, a in layout.items() if n != "w")
    assert top - (layout["w"].end + 64 - 9) == bound


def _random_image(rng, residents, prefix):
    """A random DAG-shaped run over some residents and fresh transients."""
    n_steps = rng.randint(1, 30)
    live = []
    steps, sizes, used = [], {}, {}
    for i in range(n_steps):
        reads = rng.sample(live, k=min(len(live), rng.randint(0, 3)))
        keys = rng.sample(sorted(residents), k=rng.randint(0, 2))
        for key in keys:
            name = f"{prefix}_{key}"
            used[name] = key
            sizes[name] = residents[key]
            reads.append(name)
        out = f"{prefix}_t{i}"
        sizes[out] = rng.choice([9, 64, 100, 4096, 9000, 1 << 16])
        steps.append((reads, [out]))
        live.append(out)
    return steps, sizes, used


@pytest.mark.parametrize("seed", range(20))
def test_random_images_keep_every_invariant(seed):
    """Across several images: residents are disjoint from each other and from
    every transient; co-live transients of one image are disjoint; nothing
    placed ever moves; every offset is aligned; the arena covers it all.
    """
    rng = random.Random(seed)
    alignment = rng.choice([64, 128, 4096])
    resident_sizes = {f"R{i}": rng.choice([18, 2048, 1 << 20]) for i in range(6)}
    arena = ArenaPlan(alignment=alignment)
    images = []
    for image in range(rng.randint(1, 4)):
        steps, sizes, used = _random_image(rng, resident_sizes, f"i{image}")
        layout = arena.place_image(steps, sizes, used)
        images.append((steps, used, layout))
        # Nothing an earlier image placed has moved.
        for _, used_before, layout_before in images:
            for name, key in used_before.items():
                assert arena.residents[key].offset == layout_before[name].offset

    residents = list(arena.residents.values())
    for i, a in enumerate(residents):
        assert a.offset % alignment == 0
        assert a.end <= arena.size
        for b in residents[i + 1 :]:
            assert not a.overlaps(b), f"residents {a} and {b} overlap"

    for steps, used, layout in images:
        transients = {n: a for n, a in layout.items() if n not in used}
        ranges = touch_ranges(steps, transients)
        for a in transients.values():
            assert a.offset % alignment == 0, f"{a} unaligned"
            assert a.end <= arena.size
            for r in residents:
                assert not a.overlaps(r), f"transient {a} over resident {r}"
        assert_no_overlap(transients, ranges)


# --- OperatorSequence in a shared arena ----------------------------------------


def _add():
    from iron.operators import ElementwiseAdd

    return ElementwiseAdd(size=1024, tile_size=128)


def _arena_sequence(name, runlist, arena, residents, buffer_sizes=None, **kwargs):
    from iron.common.image import OperatorSequence

    return OperatorSequence(
        name,
        runlist,
        input_args=["x"],
        output_args=["out"],
        buffer_sizes=buffer_sizes or {n: 2048 for n in residents},
        dispatch="reference",
        arena=arena,
        residents=residents,
        **kwargs,
    )


def test_two_sequences_in_one_arena_agree_on_residents_and_share_transients():
    add = _add()
    arena = ArenaPlan(alignment=64)
    one = _arena_sequence(
        "arena_one",
        [(add, "x", "w", "t0"), (add, "t0", "w", "t1"), (add, "t1", "w", "out")],
        arena,
        {"w": "W"},
    )
    two = _arena_sequence(
        "arena_two",
        [(add, "x", "weight", "u"), (add, "u", "weight", "out")],
        arena,
        {"weight": "W"},
    )
    one_layout, one_sizes, _ = one.calculate_buffer_layout()
    two_layout, two_sizes, _ = two.calculate_buffer_layout()
    assert one_layout["w"][1] == two_layout["weight"][1]
    assert two_layout["u"][1] == one_layout["t0"][1], "transients reuse bytes"
    assert max(one_sizes[2], two_sizes[2]) == arena.size


def test_placing_is_done_once_per_sequence():
    add = _add()
    arena = ArenaPlan(alignment=64)
    seq = _arena_sequence(
        "arena_once", [(add, "x", "w", "t"), (add, "t", "w", "out")], arena, {"w": "W"}
    )
    first, _, _ = seq.calculate_buffer_layout()
    size = arena.size
    again, _, _ = seq.calculate_buffer_layout()
    assert again == first and arena.size == size


def test_a_parent_reached_only_through_slices_lives_from_first_to_last_slice():
    """Its slices sit at fixed offsets inside it, so the parent is the thing
    placed, and a slice written early and read late keeps all of it live.
    """
    add = _add()
    arena = ArenaPlan(alignment=64)
    seq = _arena_sequence(
        "arena_slices",
        [
            (add, "x", "w", "big[0:2048]"),  # 0: first half of big written
            (add, "x", "w", "side"),  # 1: side live alongside big
            (add, "big[0:2048]", "side", "big[2048:4096]"),  # 2
            (add, "big[2048:4096]", "w", "out"),  # 3: big's last use
        ],
        arena,
        {"w": "W"},
        buffer_sizes={"w": 2048, "big": 4096},
    )
    seq.prepare()
    layout = seq.subbuffer_layout
    _, big_at, big_len = layout["big"]
    _, side_at, side_len = layout["side"]
    assert big_len == 4096
    assert big_at + big_len <= side_at or side_at + side_len <= big_at
    assert seq.get_layout_for_buffer("big[2048:4096]") == (
        "scratch",
        big_at + 2048,
        2048,  # a length, as a full-ELF view takes it
    )


def test_residents_must_be_scratch_buffers():
    add = _add()
    seq = _arena_sequence(
        "arena_bad_resident", [(add, "x", "w", "out")], ArenaPlan(), {"x": "X"}
    )
    with pytest.raises(ValueError, match="not scratch buffers"):
        seq.calculate_buffer_layout()


def test_an_arena_needs_an_image_that_addresses_scratch_by_offset():
    from iron.common.image import OperatorSequence

    with pytest.raises(ValueError, match="full ELF"):
        OperatorSequence(
            "arena_xclbin",
            [(_add(), "x", "w", "out")],
            ["x", "w"],
            ["out"],
            dispatch="separate",
            arena=ArenaPlan(),
        )
    with pytest.raises(ValueError, match="pass arena"):
        OperatorSequence(
            "arena_missing",
            [(_add(), "x", "w", "out")],
            ["x", "w"],
            ["out"],
            residents={"w": "W"},
        )


def test_back_to_back_buffers_start_aligned_whatever_their_sizes():
    """Without a plan, pinned buffers pack in order -- each still on a
    boundary a host view and a DMA burst can start at.
    """
    from iron.common.image import OperatorSequence
    from iron.common.image.sequence import ALIGNMENT

    add = _add()
    seq = OperatorSequence(
        "odd_pinned",
        [(add, "x", "w", "big[0:2048]"), (add, "big[0:2048]", "w", "out")],
        input_args=["x", "w"],
        output_args=["out"],
        buffer_sizes={"big": 2048 + 18, "odd": 9},
        dispatch="reference",
    )
    layout, _, _ = seq.calculate_buffer_layout()
    for name, (_, offset, _) in layout.items():
        assert offset % ALIGNMENT == 0, f"{name} at {offset}"
