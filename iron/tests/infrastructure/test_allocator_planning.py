# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Infrastructure tests for ``iron.common.image.allocator``, the memory planner.

Pure logic over synthetic runlists -- no operators, no toolchain, no hardware.
The properties that matter are: a plan never lets two simultaneously-live
buffers share bytes (correctness), it reaches the peak-liveness lower bound on
the shapes real models produce (quality), and it leaves host-addressed buffers
alone (pinning).
"""

import random

import pytest

from iron.common.graph.record import Recording
from iron.common.image.allocator import Allocation, ArenaPlan, LiveRange, Pool, lay_out
from iron.common.image.link import FullELF, PerStep
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef
from iron.operators import ElementwiseAdd, ReLU
from iron.tests.support import sequences


def steps_of(runlist):
    """Return the (reads, writes) of each entry, which is all liveness needs."""
    steps = []
    for op, *bufs in runlist:
        steps.append(
            (
                [b for b, s in zip(bufs, op.buffers) if s.fills],
                [b for b, s in zip(bufs, op.buffers) if s.drains],
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
    op = ReLU(size=1024, tile_size=128)
    runlist = [(op, "x", "a"), (op, "a", "b"), (op, "b", "c"), (op, "c", "out")]
    ranges = LiveRange.scan(steps_of(runlist))
    sizes = dict.fromkeys(ranges, 1024)
    allocations, pool = Pool().place(ranges, sizes)
    assert pool == 2048, f"a chain should ping-pong between two slots, got {pool}"
    assert allocations["a"].offset == allocations["c"].offset, "a and c should alias"
    assert pool == LiveRange.peak(ranges, sizes)
    assert_no_overlap(allocations, ranges)


def test_simultaneously_live_buffers_do_not_share():
    """Fan-out then fan-in: both branches are live together, so both are resident."""
    unary, binary = ReLU(size=1024, tile_size=128), ElementwiseAdd(
        size=1024, tile_size=128
    )
    runlist = [
        (unary, "x", "left"),
        (unary, "x", "right"),
        (binary, "left", "right", "out"),
    ]
    ranges = LiveRange.scan(steps_of(runlist))
    sizes = dict.fromkeys(ranges, 4096)
    allocations, pool = Pool().place(ranges, sizes)
    assert pool == 8192, f"two co-live buffers need both slots, got {pool}"
    assert_no_overlap(allocations, ranges)


def test_pinned_buffers_are_not_pooled():
    op = ReLU(size=1024, tile_size=128)
    runlist = [(op, "x", "scratch"), (op, "scratch", "keep"), (op, "keep", "out")]
    ranges = LiveRange.scan(steps_of(runlist), pinned={"keep"})
    assert "keep" not in ranges
    assert "scratch" in ranges


def test_graph_inputs_and_outputs_are_left_alone():
    """Values the host supplies or reads back outlive the sequence."""
    op = ReLU(size=1024, tile_size=128)
    runlist = [(op, "x", "mid"), (op, "mid", "logits")]
    ranges = LiveRange.scan(steps_of(runlist))
    assert "x" not in ranges, "an input is never written; not ours to pool"
    assert "logits" not in ranges, "an output is never read again; host reads it"
    assert "mid" in ranges


def test_repeated_block_packs_to_one_block_worth():
    """The Phase 1 claim: N identical layers cost one layer's scratch.

    This is the shape a recorded transformer produces once capture names every
    intermediate itself -- 16 copies of each scratch buffer, none of which are
    live at the same time.
    """
    unary = ReLU(size=1024, tile_size=128)
    runlist, prev = [], "x"
    for layer in range(16):
        runlist.append((unary, prev, f"h_{layer}"))
        runlist.append((unary, f"h_{layer}", f"t_{layer}"))
        prev = f"t_{layer}"
    runlist.append((unary, prev, "logits"))

    ranges = LiveRange.scan(steps_of(runlist))
    sizes = {n: 1 << 20 for n in ranges}
    allocations, pool = Pool().place(ranges, sizes)

    naive = sum(sizes.values())
    assert pool == LiveRange.peak(ranges, sizes), "should hit the lower bound"
    assert pool <= 2 << 20, f"16 layers should fold to two slots, got {pool}"
    assert pool < naive // 10, f"expected a big win over {naive}, got {pool}"
    assert_no_overlap(allocations, ranges)


def test_mixed_sizes_reach_the_lower_bound():
    """Greedy-by-size + best-fit should match peak liveness on ragged sizes."""
    unary = ReLU(size=1024, tile_size=128)
    runlist, prev = [], "x"
    for i in range(12):
        runlist.append((unary, prev, f"b{i}"))
        prev = f"b{i}"
    runlist.append((unary, prev, "out"))
    ranges = LiveRange.scan(steps_of(runlist))
    sizes = {n: (1 + (i * 7) % 5) * 4096 for i, n in enumerate(sorted(ranges))}
    allocations, pool = Pool().place(ranges, sizes)
    assert pool == LiveRange.peak(ranges, sizes)
    assert_no_overlap(allocations, ranges)


def test_offsets_are_aligned():
    unary, binary = ReLU(size=1024, tile_size=128), ElementwiseAdd(
        size=1024, tile_size=128
    )
    runlist = [(unary, "x", "a"), (unary, "x", "b"), (binary, "a", "b", "out")]
    ranges = LiveRange.scan(steps_of(runlist))
    sizes = {n: 100 for n in ranges}  # deliberately not a multiple of 64
    allocations, _ = Pool(64).place(ranges, sizes)
    for a in allocations.values():
        assert a.offset % 64 == 0, f"{a.name} at unaligned offset {a.offset}"


def test_empty_graph():
    allocations, pool = Pool().place({}, {})
    assert allocations == {} and pool == 0


# --- integration with Image's arena layout -----------------------


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _laid_out(seq):
    seq._prepare()
    return seq.layout, seq.buffer_sizes


def test_a_buffer_named_in_part_is_never_pooled():
    """A part has to sit at its buffer's offset plus its start.

    Pooling the buffer could hand its bytes to an intermediate whose life
    does not overlap the parts', and nothing raises -- a part simply reads
    the wrong memory. Found by probing the written-slice case, which the
    whole-buffer tests above cannot reach.
    """
    add = ElementwiseAdd(size=1024, tile_size=128)
    half = BufferRef("big", 0, 2048)
    recording = Recording.of_steps(
        "slice_pooling_probe",
        sequences.steps(
            (add, "x", "w", half),
            (add, half, "w", "t"),
            (add, "t", "w", "u"),
            (add, "u", "w", "v"),
            (add, "v", "w", "out"),
        ),
        ["x", "w"],
        ["out"],
        pinned={"big": 4096},
    )
    layout, sizes = _laid_out(Image(recording, FullELF()))
    _, big_at, big_len = layout["big"]
    assert big_len == 4096 and half.place(layout) == ("scratch", big_at, 2048)
    # u and v outlive every use of big, so a pooled big would lend them its bytes.
    for name in ("t", "u", "v"):
        _, at, length = layout[name]
        assert at >= big_at + big_len or at + length <= big_at, f"{name} in big"
    assert sizes.scratch == 4096 + 2 * 2048


# --- touch ranges: the rule for arenas whose host-visible buffers live elsewhere


def test_touching_ranges_span_first_to_last_use_whatever_the_direction():
    steps = [
        ([], ["a"]),  # 0: a written
        (["a"], ["dead"]),  # 1: dead written, never read
        (["early"], ["b"]),  # 2: early read before any write
        (["b", "a"], ["early"]),  # 3
    ]
    ranges = LiveRange.touching(steps, ["a", "b", "dead", "early", "unused"])
    assert ranges["a"] == LiveRange(0, 3)
    assert ranges["b"] == LiveRange(2, 3)
    assert ranges["dead"] == LiveRange(1, 1), "a dead write still needs its step"
    assert ranges["early"] == LiveRange(2, 3), "read-first still occupies its span"
    assert ranges["unused"] == LiveRange(0, 3), "an untouched buffer is always live"


def test_touching_ranges_ignore_names_not_asked_for():
    ranges = LiveRange.touching([(["x"], ["y"])], ["y"])
    assert set(ranges) == {"y"}


# --- place with fixed allocations and alignment ------------------------------


def test_fixed_allocations_are_obstacles_at_every_step():
    fixed = [Allocation("w", 0, 1000)]
    ranges = {"t": LiveRange(0, 0), "u": LiveRange(5, 5)}
    allocations, _ = Pool(64).place(ranges, {"t": 64, "u": 64}, fixed=fixed)
    for a in allocations.values():
        assert not a.overlaps(fixed[0]), f"{a} placed over a fixed allocation"
        assert a.offset == 1024, "the first aligned byte past the fixed one"


def test_a_gap_between_fixed_allocations_is_used_when_it_fits():
    fixed = [Allocation("lo", 0, 64), Allocation("hi", 1024, 64)]
    allocations, top = Pool(64).place({"t": LiveRange(0, 0)}, {"t": 900}, fixed=fixed)
    assert allocations["t"].offset == 64
    assert top == 964


def test_odd_sizes_never_leave_an_offset_unaligned():
    """bfp16 blocks are 9 bytes: nothing about a size promises alignment."""
    ranges = {f"b{i}": LiveRange(0, 0) for i in range(6)}
    sizes = {n: 9 * (i + 1) for i, n in enumerate(ranges)}
    fixed = [Allocation("w", 0, 27)]
    allocations, _ = Pool(128).place(ranges, sizes, fixed=fixed)
    for a in allocations.values():
        assert a.offset % 128 == 0, f"{a.name} at {a.offset}"


# --- ArenaPlan: several images over one arena --------------------------------


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


def test_one_storage_is_one_size():
    arena = ArenaPlan()
    arena.place_image([], {"w": 128}, {"w": "W"})
    with pytest.raises(ValueError, match="one storage is one size"):
        arena.place_image([], {"w2": 256}, {"w2": "W"})


def test_a_resident_needs_a_size():
    with pytest.raises(ValueError, match="have no size"):
        ArenaPlan().place_image([], {}, {"w": "W"})


def _random_image(rng, residents, prefix):
    """Draw a random DAG-shaped run over some residents and fresh transients."""
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
    """Check every invariant across several images.

    Residents are disjoint from each other and from every transient;
    co-live transients of one image are disjoint; nothing placed ever
    moves; every offset is aligned; the arena covers it all.
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
        ranges = LiveRange.touching(steps, transients)
        for a in transients.values():
            assert a.offset % alignment == 0, f"{a} unaligned"
            assert a.end <= arena.size
            for r in residents:
                assert not a.overlaps(r), f"transient {a} over resident {r}"
        assert_no_overlap(transients, ranges)


# --- Image in a shared arena ----------------------------------------


def _add():

    return ElementwiseAdd(size=1024, tile_size=128)


def _arena_sequence(name, runlist, arena, residents, pinned=None, full_elf=True):

    recording = Recording.of_steps(
        name,
        sequences.steps(*runlist),
        ["x"],
        ["out"],
        pinned=pinned or {n: 2048 for n in residents},
    )
    packaging = FullELF() if full_elf else PerStep()
    return Image(recording, packaging, arena=arena, residents=residents)


def test_a_parent_reached_only_through_slices_lives_from_first_to_last_slice():
    """Check that the parent is the thing placed, since its slices sit at fixed offsets.

    A slice written early and read late keeps all of it live.
    """
    add = _add()
    arena = ArenaPlan(alignment=64)
    first, second = BufferRef("big", 0, 2048), BufferRef("big", 2048, 2048)
    seq = _arena_sequence(
        "arena_slices",
        [
            (add, "x", "w", first),  # 0: first half of big written
            (add, "x", "w", "side"),  # 1: side live alongside big
            (add, first, "side", second),  # 2
            (add, second, "w", "out"),  # 3: big's last use
        ],
        arena,
        {"w": "W"},
        pinned={"w": 2048, "big": 4096},
    )
    layout, _ = _laid_out(seq)
    _, big_at, big_len = layout["big"]
    _, side_at, side_len = layout["side"]
    assert big_len == 4096
    assert big_at + big_len <= side_at or side_at + side_len <= big_at
    assert second.place(layout) == ("scratch", big_at + 2048, 2048)


def test_an_argument_ends_past_the_arena_buffer_placed_last():
    # "kept" sits in the arena past "x", the one buffer laid out after it.
    arena = {"kept": Allocation("kept", 8192, 64)}
    steps = [((), ("kept", "x")), (("kept", "x"), ())]
    _, args = lay_out({"kept": 64, "x": 64}, steps, ((), (), ()), {"x"}, arena)
    assert args.scratch == 8256
