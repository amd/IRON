# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Testing`` and the shared case sweeps, resolved against a bound device."""

import pytest

from iron.common.testing import Case, Sweep, Testing
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gelu import GELU
from iron.operators.rms_norm import RMSNorm
from iron.operators.silu import SiLU

pytestmark = pytest.mark.usefixtures("npu2")


def test_the_unary_sweep_reads_the_class_it_is_resolved_for():
    cases = Sweep()(GELU)
    assert max(c.kwargs["tile_size"] for c in cases) == GELU.tile_cap == 8192
    for c in cases:
        k = c.kwargs
        assert (
            k["size"] % (k["num_aie_columns"] * k["num_channels"] * k["tile_size"]) == 0
        )
    assert {c.kwargs["size"] for c in cases if not c.extensive} == {2048}
    assert "num_channels" not in Sweep(channels=None)(SiLU)[0].kwargs


def test_the_binary_sweep_and_an_all_extensive_sweep():
    cases = Sweep(channels=None)(ElementwiseAdd)
    assert {c.kwargs["num_aie_columns"] for c in cases} == {1, 2, 4, 8}  # divide 2^n
    extra = Sweep(channels=None, regular=None, scalar_factor=10.0)(ElementwiseAdd)
    assert extra and all(
        c.extensive and c.kwargs["scalar_factor"] == 10.0 for c in extra
    )


def test_testing_resolves_lists_dicts_and_callables_of_the_class():
    t = Testing([dict(size=8), Case(dict(size=16), extensive=True)])
    assert [c.kwargs for c in t.resolve(GELU)] == [{"size": 8}, {"size": 16}]
    assert [c.extensive for c in t.resolve(GELU)] == [False, True]
    by_class = Testing(lambda cls: [dict(size=cls.tile_cap)])
    assert by_class.resolve(GELU)[0].kwargs == {"size": 8192}
    mixed = Testing([Sweep(regular=None), dict(size=8)]).resolve(GELU)
    assert mixed[:-1] == Sweep(regular=None)(GELU) and mixed[-1] == Case({"size": 8})


def test_a_row_sweep_splits_each_length_into_rows_of_the_tile():
    flat = {
        (c.kwargs["num_aie_columns"], c.kwargs["num_channels"], c.kwargs["size"])
        for c in Sweep()(RMSNorm)
    }
    rows = Sweep(rows=True)(RMSNorm)
    assert rows and all("size" not in c.kwargs for c in rows)
    assert {
        (
            c.kwargs["num_aie_columns"],
            c.kwargs["num_channels"],
            c.kwargs["rows"] * c.kwargs["tile_size"],
        )
        for c in rows
    } == flat
