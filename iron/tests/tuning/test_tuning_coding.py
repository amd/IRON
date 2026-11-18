# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Transformation tests for coded weights, decoded on chip by a ``Decode`` actor."""

import numpy as np
import pytest
from aie.iron.device import NPU2
from ml_dtypes import bfloat16

import iron
from iron.common.declare import Profile
from iron.common.declare.composition import (
    Configuration,
    Entry,
    Member,
    Refinement,
    Region,
)
from iron.common.graph.record import Recording
from iron.common.image.step import Edge
from iron.operators.decode import Decode
from iron.operators.gemv import GEMV
from iron.tests.support import sequences
from iron.tests.support.toys_settings import (
    coded_consumer,
    coded_consumer_recording,
    coded_consumer_recording_with_weight,
    small_integer_weight,
)
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import candidates, check, fit, measure, search

NPU2_DEVICE = NPU2()

pytestmark = pytest.mark.usefixtures("npu2")


def _wide_weight(M: int, K: int) -> np.ndarray:
    """Return a real bf16 weight whose every row spans enough exponents to overflow a small coded capacity."""
    vals = [((-1) ** i) * 2.0 ** (i % 64 - 32) for i in range(K)]
    row = np.array(vals, dtype=np.float32).astype(bfloat16)
    return np.tile(row, (M, 1))


def _coded_region(M: int, K: int, rows: int, num_aie_columns: int) -> Region:
    return Region(
        parts=(
            Member(
                cls=Decode,
                dims=dict(M=M, K=K, rows=rows, num_aie_columns=num_aie_columns),
            ),
            Member(
                cls=GEMV,
                dims=dict(
                    M=M,
                    K=K,
                    num_aie_columns=num_aie_columns,
                    tile_size_input=1,
                    tile_size_output=M // num_aie_columns,
                ),
            ),
        ),
        edges=(Edge(0, "out", 1, "A"),),
        workers=((0, 1),),
    )


def test_coding_legality_depends_on_the_weights_own_values():
    """``Decode`` has no plain fallback: a weight a ``GEMV``'s own ``coded_a`` flag would read plain refuses it instead.

    ``Recording.code_weights`` is real, device-free host work (what a compile runs
    before any build): a weight whose coded form overflows its capacity is read plain
    with a warning where its reader can fall back (``GEMV``'s ``coded_a``), and refused
    where it cannot (``Decode``, which only ever reads coded rows).
    """
    wide = _wide_weight(M=128, K=64)

    class PlainCoded(iron.Graph):
        def __init__(self, weight):
            self.w = iron.param(weight)

        def body(self, x):
            return GEMV.step(
                self.w,
                x,
                coded_a=True,
                num_aie_columns=1,
                tile_size_input=1,
                tile_size_output=128,
            )

    plain_coded = PlainCoded(wide).record(x=(64,))
    plain_coded.code_weights()
    assert "w" in plain_coded.read_plain

    decode_consumer = coded_consumer_recording_with_weight(
        rows=1, num_aie_columns=1, weight=wide
    )
    with pytest.raises(ValueError, match="no flag to read it plain"):
        decode_consumer.code_weights()


@unbuilt
def test_coding_is_proposed_wherever_capacity_holds_at_that_width(tmp_path):
    """Coding round-trips as a ``Region`` whose ``Decode`` and its consumer share a worker, and is proposed wherever capacity holds."""
    decode, gemv = coded_consumer(M=128, K=128, rows=1, num_aie_columns=1)
    recording = coded_consumer_recording(
        "coded_candidates", decode.resolved(NPU2_DEVICE), gemv.resolved(NPU2_DEVICE)
    )
    entry = Entry(root=_coded_region(M=128, K=128, rows=1, num_aie_columns=1))
    profile = Profile()
    profile.add_entry(entry)
    path = tmp_path / "profile.json"
    profile.save(path)
    loaded = Profile.load(path)
    assert loaded.entries() == [entry]
    found = list(candidates([Timed(recording)], loaded, NPU2_DEVICE))
    assert any(
        isinstance(e.apply(loaded).entries()[-1].root, Region)
        and e.apply(loaded).entries()[-1].root.workers == ((0, 1),)
        for e in found
    )


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_coded_weights_are_bit_identical_to_plain():
    """A coded weight, decoded on chip by a ``Decode`` sharing a worker with its consumer, is bit-identical to the plain weight the untuned build reads.

    The recording carries a real weight (``coded_consumer_recording_with_weight``): both
    lossless coding and its legality depend on the weight's own values, not only the
    shapes ``Decode`` and ``GEMV`` are built at.
    """
    weight = small_integer_weight((128, 128), 0)
    recording = coded_consumer_recording_with_weight(
        rows=1, num_aie_columns=1, weight=weight
    )
    base = Profile()
    coded_profile = Profile()
    coded_profile.add_entry(
        Entry(root=_coded_region(M=128, K=128, rows=1, num_aie_columns=1))
    )
    result = check(
        coded_profile,
        base,
        [Timed(recording)],
        NPU2_DEVICE,
        refinement=Refinement.EXACT,
    )
    assert result.ok, result.why


@unbuilt
def test_coding_is_kept_only_where_ddr_bytes_saved_beat_the_decode_cost():
    """The tuner keeps coding on a weight-bound decode ``GEMV`` and drops it on a compute-bound one.

    Both calls run the same ``Decode`` into ``GEMV`` toy and the same real weight
    (``coded_consumer_recording_with_weight``), so the same ``_coded_region`` Region is
    held to each: only ``num_batches`` differs, amortizing the one decoded weight over
    more of the ``GEMV``'s compute (a prompt chunk) rather than a single row.
    """
    weight = small_integer_weight((2048, 8192), 0)
    weight_bound = coded_consumer_recording_with_weight(
        rows=1, num_aie_columns=4, weight=weight
    )
    compute_bound = coded_consumer_recording_with_weight(
        rows=1, num_aie_columns=4, weight=weight, num_batches=256
    )
    start = Profile()
    with_entry = Profile()
    with_entry.add_entry(
        Entry(root=_coded_region(M=2048, K=8192, rows=1, num_aie_columns=4))
    )

    weight_bound_calls = [Timed(weight_bound)]
    weight_bound_ratio = measure(
        with_entry, start, weight_bound_calls, NPU2_DEVICE
    ).ratio
    assert weight_bound_ratio < 0.95
    weight_bound_tuned = search(weight_bound_calls, start, NPU2_DEVICE, budget_s=5.0)
    assert any(isinstance(e.root, Region) for e in weight_bound_tuned.entries())

    compute_bound_calls = [Timed(compute_bound)]
    compute_bound_ratio = measure(
        with_entry, start, compute_bound_calls, NPU2_DEVICE
    ).ratio
    assert compute_bound_ratio > 1.05
    compute_bound_tuned = search(compute_bound_calls, start, NPU2_DEVICE, budget_s=5.0)
    assert not any(isinstance(e.root, Region) for e in compute_bound_tuned.entries())


@unbuilt
def test_a_width_where_a_row_overflows_its_capacity_is_refused_before_any_build():
    """A width whose coded row overflows its exception capacity is refused before any build, naming the row."""
    weight = _wide_weight(M=128, K=64)
    recording = coded_consumer_recording_with_weight(
        rows=1, num_aie_columns=1, weight=weight
    )
    profile = Profile()
    profile.add_entry(Entry(root=_coded_region(M=128, K=64, rows=1, num_aie_columns=1)))
    result = fit(profile, [Timed(recording)], NPU2_DEVICE)
    assert not result.ok
    assert result.stage == "counts"
    assert "row" in result.why


@unbuilt
def test_coding_part_of_a_shared_array_is_refused_unless_the_split_is_proposed():
    """Coding part of a shared array (not every shape sharing it) is refused unless the candidate also proposes the split."""
    decode, gemv = coded_consumer(M=2048, K=8192, rows=1, num_aie_columns=8)
    other = GEMV(
        M=2048, K=8192, num_aie_columns=8, tile_size_input=1, tile_size_output=256
    ).resolved(NPU2_DEVICE)
    steps = sequences.steps(
        (decode.resolved(NPU2_DEVICE), "coded", "w"),
        (gemv.resolved(NPU2_DEVICE), "w", "x", "out1"),
        (other, "w2", "x2", "out2"),
    )
    recording = Recording.of_steps(
        "coded_shared_array", steps, ["coded", "x", "w2", "x2"], ["out1", "out2"]
    )
    configuration = Configuration(
        parts=(
            _coded_region(M=2048, K=8192, rows=1, num_aie_columns=8),
            Member(
                cls=GEMV,
                dims=dict(
                    M=2048,
                    K=8192,
                    num_aie_columns=8,
                    tile_size_input=1,
                    tile_size_output=256,
                ),
            ),
        )
    )
    profile = Profile()
    profile.add_entry(Entry(root=configuration))
    result = fit(profile, [Timed(recording)], NPU2_DEVICE)
    assert not result.ok
    assert result.stage == "counts"


@unbuilt
def test_lossy_coding_is_never_proposed():
    """Coding is lossless by declaration (``Decode.tolerance`` is exact); a lossy encoding is never among the candidates."""
    decode, gemv = coded_consumer(M=128, K=128, rows=1, num_aie_columns=1)
    resolved = decode.resolved(NPU2_DEVICE)
    assert resolved.tolerance().rtol is None and resolved.tolerance().atol is None
    recording = coded_consumer_recording(
        "lossless_only", resolved, gemv.resolved(NPU2_DEVICE)
    )
    profile = Profile()
    found = list(candidates([Timed(recording)], profile, NPU2_DEVICE))
    decode_members = [
        part
        for e in found
        for part in e.apply(profile).entries()[-1].root.parts
        if part.cls is Decode
    ]
    assert all(
        part.cls(**part.dims).tolerance().rtol is None for part in decode_members
    )
