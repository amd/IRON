# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``check`` and ``measure`` on the NPU: a composition held bit-identical to its steps run apart, and timed against them."""

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Refinement
from iron.common.graph.record import Recording
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.rms_norm import RMSNorm
from iron.tests.support import sequences
from iron.tests.support.tools import DEVICES
from iron.tests.support.toys_edges import chain
from iron.tune.autotune import Timed
from iron.tune.search import check, measure

DEVICE = DEVICES["npu2"]()

pytestmark = [pytest.mark.usefixtures("npu2"), pytest.mark.supported_devices("npu2")]


def test_a_stream_window_is_bit_identical_to_its_steps_apart():
    """Add, RMSNorm and multiply fused as one stream window, held to the three run apart."""
    recording, region = chain()
    profile = Profile()
    profile.add_entry(Entry(region))
    result = check(profile, Profile(), [Timed(recording)], DEVICE, Refinement.EXACT)
    assert result.ok, result.why


def test_a_build_computing_something_else_is_caught():
    """The same chain held to one ending in an add, not a multiply: its ``out`` differs, and the check names it."""
    recording, region = chain()
    add = ElementwiseAdd(size=256, num_aie_columns=1, tile_size=256)
    norm = RMSNorm(rows=1, tile_size=256, num_aie_columns=1)
    last = ElementwiseAdd(size=256, num_aie_columns=1, tile_size=256)
    other = Recording.of_steps(
        "toy_chain",
        sequences.steps(
            (add, "a", "b", "h"), (norm, "h", "n"), (last, "n", "up", "out")
        ),
        ["a", "b", "up"],
        ["out"],
    )
    assert isinstance(recording.steps[2].op, ElementwiseMul)
    profile = Profile()
    profile.add_entry(Entry(region))
    result = check(
        profile,
        Profile(),
        [Timed(recording)],
        DEVICE,
        Refinement.EXACT,
        base_calls=[Timed(other)],
    )
    assert not result.ok
    assert "out" in (result.why or "")


def test_a_build_measured_against_itself_takes_about_as_long():
    """The same build timed in pairs against itself: the median paired ratio is near one."""
    recording, _ = chain()
    measured = measure(Profile(), Profile(), [Timed(recording)], DEVICE)
    assert 0.8 < measured.ratio < 1.25
    assert measured.seconds > 0 and measured.base_seconds > 0


def test_a_stream_window_measures_faster_than_its_steps_apart():
    """Add, RMSNorm and multiply as one stream window take about a third of their time apart (one dispatch, no host round trips)."""
    recording, region = chain()
    profile = Profile()
    profile.add_entry(Entry(region))
    measured = measure(profile, Profile(), [Timed(recording)], DEVICE)
    assert measured.ratio < 0.8
    assert measured.seconds < measured.base_seconds
