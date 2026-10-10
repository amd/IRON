# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Testing`` and the shared case sweeps, resolved for an eight-column NPU2."""

from aie.iron.device import from_name

from iron.common.testing import BENCH_ELEMENTS, Case, Sweep, Testing
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gelu import GELU
from iron.operators.rms_norm import RMSNorm
from iron.operators.silu import SiLU

NPU2 = from_name("npu2", n_cols=8)


def test_the_unary_sweep_reads_the_class_it_is_resolved_for():
    cases = Sweep()(GELU, NPU2)
    assert max(c.kwargs["tile_size"] for c in cases) == GELU.tile_cap == 8192
    for c in cases:
        k = c.kwargs
        assert (
            k["size"] % (k["num_aie_columns"] * k["num_channels"] * k["tile_size"]) == 0
        )
    default = {c.kwargs["size"] for c in cases if not c.extensive and not c.bench}
    assert default == {2048}
    # One benched case, in the default suite: the widest grid, most channels.
    (bench,) = [c for c in cases if c.bench]
    assert not bench.extensive
    assert bench.kwargs == dict(
        size=BENCH_ELEMENTS, num_aie_columns=8, num_channels=2, tile_size=4096
    )
    assert "num_channels" not in Sweep(channels=None)(SiLU, NPU2)[0].kwargs


def test_the_binary_sweep_and_an_all_extensive_sweep():
    cases = Sweep(channels=None)(ElementwiseAdd, NPU2)
    assert {c.kwargs["num_aie_columns"] for c in cases} == {1, 2, 4, 8}  # divide 2^n
    (bench,) = [c for c in cases if c.bench]
    assert bench.kwargs == dict(size=BENCH_ELEMENTS, num_aie_columns=8, tile_size=4096)
    extra = Sweep(channels=None, regular=None, bench=None, scalar_factor=10.0)(
        ElementwiseAdd, NPU2
    )
    assert extra and all(
        c.extensive and c.kwargs["scalar_factor"] == 10.0 for c in extra
    )


def test_testing_resolves_lists_dicts_and_callables_of_the_class():
    t = Testing([dict(size=8), Case(dict(size=16), extensive=True)])
    assert [c.kwargs for c in t.resolve(GELU, NPU2)] == [{"size": 8}, {"size": 16}]
    assert [c.extensive for c in t.resolve(GELU, NPU2)] == [False, True]
    by_class = Testing(lambda cls, dev: [dict(size=cls.tile_cap)])
    assert by_class.resolve(GELU, NPU2)[0].kwargs == {"size": 8192}
    mixed = Testing([Sweep(regular=None), dict(size=8)]).resolve(GELU, NPU2)
    assert mixed[:-1] == Sweep(regular=None)(GELU, NPU2) and mixed[-1] == Case(
        {"size": 8}
    )


def test_a_row_sweep_splits_each_length_into_rows_of_the_tile():
    flat = {
        (c.kwargs["num_aie_columns"], c.kwargs["num_channels"], c.kwargs["size"])
        for c in Sweep()(RMSNorm, NPU2)
    }
    rows = Sweep(rows=True)(RMSNorm, NPU2)
    assert rows and all("size" not in c.kwargs for c in rows)
    assert {
        (
            c.kwargs["num_aie_columns"],
            c.kwargs["num_channels"],
            c.kwargs["rows"] * c.kwargs["tile_size"],
        )
        for c in rows
    } == flat
