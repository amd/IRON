# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Any toy under several legal firing orders and depths gives bit-identical output every time."""

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Entry, Refinement
from iron.tests.support import toys_dataflow as toys
from iron.tests.support.tuning import unbuilt
from iron.tune.autotune import Timed
from iron.tune.search import check

pytestmark = pytest.mark.usefixtures("npu2")

_REPEATS = 3


@pytest.mark.parametrize("depth", [1, 2, 4])
@pytest.mark.supported_devices("npu2")
def test_chain_is_bit_identical_at_every_legal_depth(depth):
    """``add -> SiLU -> mul`` at every depth from the minimum to well past the knee: every repeated ``check`` passes, not only at one depth."""
    add, silu, mul = toys.add_silu_mul()
    region = toys.add_silu_mul_region(add, silu, mul, depth=depth)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.add_silu_mul_recording(f"depth-{depth}", add, silu, mul)
    for _ in range(_REPEATS):
        result = check(
            profile, Profile(), [Timed(recording)], toys.NPU2, Refinement.EXACT
        )
        assert result.ok, result.why


@pytest.mark.supported_devices("npu2")
def test_skip_diamond_is_bit_identical_under_its_one_legal_firing_order():
    """The residual-add skip/broadcast window, checked repeatedly at its one legal order.

    ``first`` must fire before both its readers; every repeated ``check``
    passes, no arrival-order nondeterminism in a non-reducing broadcast.
    """
    region, first, norm, second = toys.broadcast_skip(depth=4)
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.broadcast_skip_recording("legal-order", first, norm, second)
    for _ in range(_REPEATS):
        result = check(
            profile, Profile(), [Timed(recording)], toys.NPU2, Refinement.EXACT
        )
        assert result.ok, result.why


@unbuilt
@pytest.mark.supported_devices("npu2")
def test_running_sum_is_bit_identical_at_its_one_legal_initial_token_count():
    """The running-sum loop with ``acc`` carried across calls (the one count a self-loop edge's carry supports): every repeated ``check`` passes.

    A self-loop edge's initial tokens come from whether its buffer is
    carried (``Recording.feedback``), which is a yes/no fact, not a count;
    there is no field for a loop pre-loaded two or three calls ahead, which
    would need that many distinct carried buffers rather than one, a
    different recording, not a parameter of this one.
    """
    region, add = toys.running_sum()
    profile = Profile()
    profile.add_entry(Entry(root=region))
    recording = toys.running_sum_recording("legal-initial-tokens", add, carried=True)
    for _ in range(_REPEATS):
        result = check(
            profile, Profile(), [Timed(recording)], toys.NPU2, Refinement.EXACT
        )
        assert result.ok, result.why
