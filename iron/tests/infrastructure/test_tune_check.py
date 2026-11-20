# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``check``'s pairing of a call's points with its base call's, refused before any build: device-free."""

import pytest

from iron.common.declare import Profile
from iron.common.declare.composition import Refinement
from iron.tests.support.toys_check import MulUpToM, MulUpToN
from iron.tune.autotune import Point, Timed
from iron.tune.search import check

pytestmark = pytest.mark.usefixtures("npu2")


def test_a_bound_given_only_in_a_call_s_points_is_whole_at_its_bare_values(npu2):
    """Each side's bound given only in its points: its bare values cut ``out`` whole on both sides, and the points' second pair, 128 against 64, is refused.

    The bare values are where ``_in_order`` runs a call; the bound read there
    is the one ``_bound_points`` also leaves unhalved.
    """
    shapes = dict(x=(256,), y=(256,))
    call = Timed(
        MulUpToN().record(**shapes),
        points=(Point(0.5, {"n": 256}), Point(0.5, {"n": 128})),
    )
    base = Timed(
        MulUpToM().record(**shapes),
        points=(Point(0.5, {"m": 256}), Point(0.5, {"m": 64})),
    )
    with pytest.raises(ValueError, match=r"select other extents of out \(\(64,\)"):
        check(Profile(), Profile(), [call], npu2, Refinement.EXACT, base_calls=[base])
