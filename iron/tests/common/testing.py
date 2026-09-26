# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Testing`` and the shared case sweeps, resolved against a bound device."""

import pytest

from iron.common.testing import (
    Case,
    Testing,
    binary_elementwise_cases,
    channeled_unary_cases,
)
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gelu import GELU
from iron.operators.silu import SiLU

pytestmark = pytest.mark.usefixtures("npu2")


def test_the_unary_sweep_reads_the_class_it_is_resolved_for():
    cases = channeled_unary_cases()(GELU)
    assert max(c.kwargs["tile_size"] for c in cases) == GELU.tile_cap == 8192
    for c in cases:
        k = c.kwargs
        assert (
            k["size"] % (k["num_aie_columns"] * k["num_channels"] * k["tile_size"]) == 0
        )
    assert {c.kwargs["size"] for c in cases if not c.extensive} == {2048}
    assert "num_channels" not in channeled_unary_cases(channels=None)(SiLU)[0].kwargs
    floored = channeled_unary_cases(tile_floor=1024)(GELU)
    assert floored and all(c.kwargs["tile_size"] >= 1024 for c in floored)


def test_the_binary_sweep_and_an_all_extensive_sweep():
    cases = binary_elementwise_cases()(ElementwiseAdd)
    assert {c.kwargs["num_aie_columns"] for c in cases} == {1, 2, 4, 8}  # divide 2^n
    extra = binary_elementwise_cases(regular=None, scalar_factor=10.0)(ElementwiseAdd)
    assert extra and all(
        c.extensive and c.kwargs["scalar_factor"] == 10.0 for c in extra
    )


def test_testing_resolves_lists_dicts_and_callables_of_the_class():
    t = Testing([dict(size=8), Case(dict(size=16), extensive=True)])
    assert [c.kwargs for c in t.resolve(GELU)] == [{"size": 8}, {"size": 16}]
    assert [c.extensive for c in t.resolve(GELU)] == [False, True]
    by_class = Testing(lambda cls: [dict(size=cls.tile_cap)])
    assert by_class.resolve(GELU)[0].kwargs == {"size": 8192}
