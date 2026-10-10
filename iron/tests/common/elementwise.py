# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The elementwise template: what an operator that names one kernel gets."""

import ml_dtypes
import numpy as np
import pytest
from aie.iron.device import from_name
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad, UnaryElementwise, Unresolvable
from iron.common.design.build import build_design
from iron.common.elementwise import _interval
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.relu import ReLU

pytestmark = pytest.mark.usefixtures("npu2")
NPU2 = from_name("npu2", n_cols=8)


def test_a_tunable_free_operator_takes_the_widest_split_that_leaves_whole_lines():
    for size, cols in ((256, 1), (1024, 4), (2048, 8), (3072, 6), (8192, 8)):
        op = ReLU(size=size).resolved(NPU2)
        assert (op.num_aie_columns, op.num_channels, op.tile_size) == (cols, 1, 256)
        assert op.lines % op.cores == 0
    assert ElementwiseAdd(size=2048).resolved(NPU2).num_aie_columns == 8


def test_the_refusals_name_what_to_change():
    with pytest.raises(ValueError, match="give a tile_size= or num_aie_columns="):
        ReLU(size=1000).resolved(NPU2)
    with pytest.raises(Unresolvable, match="none is bound and none was given"):
        ReLU(size=1024).resolve(None)  # what resolved() asks on a host with no device


def test_the_trip_count_is_a_resident_the_build_writes():
    op = ReLU(size=2048, tile_size=512).resolved(NPU2)
    assert op.cores == 4 and op.lines == 4
    assert op.residents == {"count": 1}
    # The preamble writes it into each core's runtime-parameter buffer.
    one_core = ReLU(size=2560, num_aie_columns=1, tile_size=256)
    assert "aiex.npu.rtp_write(@count_0, 0, %c10_i32)" in str(build_design(one_core))


def test_an_operator_written_by_inheritance_inherits_the_sweep():
    class Neg(UnaryElementwise):
        def kernel(self):
            raise NotImplementedError

        def reference(self, x):
            return -x

    assert Neg.test is not None
    cases = Neg.test.resolve(Neg, NPU2)
    assert all(c.kwargs["tile_size"] <= Neg.tile_cap for c in cases)


def test_a_bounded_operand_makes_the_trip_count_per_call():
    """``x[:n]`` bounds the template's extent: the count each core reads
    and the tiles each lane moves become words the host writes per call.
    """

    class G(iron.Graph):
        def body(self, x, *, n: Scratchpad[np.int32]):
            return ReLU(x[:n], tile_size=256, num_aie_columns=2)

    g = G()

    t = g.trace(x=(4096,))
    (op,) = t.operators
    assert {k: e.name for k, e in op.bound_extents.items()} == {"valid": "n"}
    assert [v.name for v in op.values] == ["valid", "count", "valid_x", "valid_y"]
    assert op.derived_at("count", valid=1024) == 1024 // (2 * 256)
    assert op.derived_at("valid_x", valid=1024) == 1024 // (2 * 256)
    assert op.residents == {}  # nothing is written once per build
    # Unbounded, the same class is what it was: one resident, no words.
    plain = ReLU(size=4096, tile_size=256, num_aie_columns=2).resolved(NPU2)
    assert plain.valid == 4096 and plain.residents == {"count": 8}
    assert [v.name for v in plain.values] == []


def _bound(x):
    return 0.01 * np.abs(x) + 1e-3


@pytest.mark.parametrize(
    "tol",
    [
        Tolerance.relative(0.04),
        Tolerance.relative(0.04, 1e-3),
        Tolerance.relative(0.04, range_frac=1e-3),
        Tolerance.bf16_ulps(2),
        Tolerance.bf16_ulps(1, atol=float(ml_dtypes.finfo(bfloat16).smallest_normal)),
        Tolerance.bounded(_bound),
        Tolerance.exact(),
    ],
    ids=[
        "relative",
        "relative_atol",
        "relative_range",
        "ulps",
        "ulps_atol",
        "bound",
        "exact",
    ],
)
def test_a_chains_interval_is_what_compare_admits(tol):
    """A chain's gate carries each step's admitted outputs as an interval:
    its edges pass ``compare``, and the next value past either fails.
    """
    rng = np.random.default_rng(0)
    x = rng.standard_normal(4096) * np.exp(rng.uniform(-8, 8, 4096))
    x = np.concatenate([x, [0.0, 0.0, 1e-40, -1e-39]])
    v = np.concatenate([x[:2048], x[2048:].astype(bfloat16).astype(np.float64)])
    lo, hi = _interval(tol, [v], [(x,)], bfloat16)
    bound = dict(bound=_bound(x)) if tol.kind == "bound" else {}
    for edge, away in ((lo, -np.inf), (hi, np.inf)):
        at = edge.astype(bfloat16)
        past = np.nextafter(at, np.asarray(away, bfloat16))
        assert compare(at, v, tol, **bound).n_mismatch == 0
        assert compare(past, v, tol, **bound).n_mismatch == v.size
