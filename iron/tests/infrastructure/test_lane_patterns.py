# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Operator.lane_transfers()``'s faithfulness: for every catalog case of an
operator with a hand-written ``sequence(rt)``, the per-lane host access order
it describes must equal, element for element, what the generated module's
shim tasks actually move. Device-free: ``generated_sequence`` only emits MLIR.
"""

from math import prod

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern

from aie.helpers.taplib import PerCall

from iron.common import Precision
from iron.common.image.packaging import Kind
from iron.operators.copy import Copy
from iron.operators.flm.gemm.op import ProjectionGEMM
from iron.operators.gemm import GEMM
from iron.operators.mha import MHA
from iron.operators.softmax import Softmax
from iron.tests.support.build import generated_sequence
from iron.tests.support.tools import DEVICES

pytestmark = pytest.mark.usefixtures("npu2")

NPU2 = DEVICES["npu2"]()


def _lane_order(op, name: str) -> dict[int, np.ndarray]:
    """Per logical lane (in the order ``build()`` bound them), the flat
    elements the generated module's shim tasks move for buffer ``name``, in
    emission order.
    """
    _, tasks = generated_sequence(op, full_elf=False)
    idx = [b.name for b in op.buffers].index(name)
    operand = getattr(op, name)
    elements = prod(operand.shape)
    lane_names: list[str] = []
    by_lane: dict[str, list] = {}
    for t in tasks:
        if t.arg != idx:
            continue
        if t.lane not in by_lane:
            by_lane[t.lane] = []
            lane_names.append(t.lane)
        by_lane[t.lane].append(t)
    out = {}
    for lane, lane_name in enumerate(lane_names):
        pieces = []
        for t in by_lane[lane_name]:
            sizes = [int(s) for s in t.sizes.split(",")]
            strides = [int(s) for s in t.strides.split(",")]
            offset = t.offset if isinstance(t.offset, int) else 0
            tap = TensorAccessPattern(operand.shape, offset, sizes, strides)
            pieces.append(tap.gather(np.arange(elements)))
        out[lane] = np.concatenate(pieces)
    return out


def _assert_described_and_faithful(op, name: str) -> None:
    operand = getattr(op, name)
    described = op.lane_transfers(operand)
    assert described is not None, f"{type(op).__name__}.{name} was not described"
    predicted = {lane: tap for lane, tap, _, _ in described}
    truth = _lane_order(op, name)
    assert sorted(predicted) == sorted(
        truth
    ), f"{type(op).__name__}.{name}: lane sets differ"
    elements = prod(operand.shape)
    for lane in sorted(truth):
        got = predicted[lane].gather(np.arange(elements))
        assert np.array_equal(
            got, truth[lane]
        ), f"{type(op).__name__}.{name} lane {lane}"


@pytest.mark.parametrize("case", GEMM.test.resolve(GEMM, NPU2), ids=lambda c: c.label)
def test_gemm_lanes_are_faithful(case):
    """GEMM bounds its compute, not its DMA (AGENTS.md), so A, B and C's order
    holds at every catalog case regardless of a per-call bound.
    """
    op = GEMM(**case.kwargs).resolved(NPU2)
    for name in ("A", "B", "C"):
        _assert_described_and_faithful(op, name)


@pytest.mark.parametrize("case", MHA.test.resolve(MHA, NPU2), ids=lambda c: c.label)
def test_mha_lanes_are_faithful(case):
    """Q and O stream every row unconditionally; K and V's order is checked
    at the unbounded catalog shapes, where ``length_parameter`` is None."""
    op = MHA(**case.kwargs).resolved(NPU2)
    for name in ("Q", "O", "K", "V"):
        _assert_described_and_faithful(op, name)


@pytest.mark.parametrize(
    "case", Softmax.test.resolve(Softmax, NPU2), ids=lambda c: c.label
)
def test_softmax_lanes_are_faithful(case):
    op = Softmax(**case.kwargs).resolved(NPU2)
    for name in ("x", "y"):
        _assert_described_and_faithful(op, name)
    if op.has_addend:
        _assert_described_and_faithful(op, "addend")


@pytest.mark.parametrize("case", Copy.test.resolve(Copy, NPU2), ids=lambda c: c.label)
def test_copy_lanes_are_faithful(case):
    op = Copy(**case.kwargs).resolved(NPU2)
    for name in ("x", "y"):
        _assert_described_and_faithful(op, name)


# flm.ProjectionGEMM has no `Testing` catalog (it is checked on hardware in
# iron/operators/flm/gemm/test.py); these mirror that module's own shapes.
_PROJECTION_GEMM_CASES = [
    pytest.param(dict(M=256, K=512, N=1024), True, id="smallest_full_sweep"),
    pytest.param(dict(M=256, K=512, N=1536), True, id="trailing_column_block"),
    pytest.param(dict(M=256, K=512, N=128), False, id="remainder_only_too_few_cols"),
    pytest.param(dict(M=2048, K=1024, N=16), False, id="narrow_n_too_few_cols"),
    pytest.param(
        dict(M=256, K=512, N=1024, tile_n=None, b_col_maj=True),
        True,
        id="b_col_maj_resident",
    ),
    pytest.param(
        dict(M=512, K=6144, N=512, b_col_maj=True), True, id="b_col_maj_streamed"
    ),
    pytest.param(dict(M=512, K=512, N=20480, m_chunk=2), False, id="m_chunk_split_leg"),
    pytest.param(
        dict(M=256, K=512, N=64 * 8 + 64, b_col_maj=True),
        True,
        id="b_col_maj_trailing_column",
    ),
    pytest.param(
        dict(M=256, K=256, N=64 * 8, tile_n=64, k_tile=256), True, id="three_k_steps"
    ),
    pytest.param(dict(M=16384, K=512, N=1024), False, id="two_slabs"),
]


@pytest.mark.parametrize("kwargs,described", _PROJECTION_GEMM_CASES)
def test_projection_gemm_lanes_are_faithful(kwargs, described):
    """A and C are described at one slab, ``m_chunk=1``, with every column
    doing work; past that (a second slab, too few active columns, a split
    leg) ``lane_transfers`` refuses, same as the catalog cases above would if
    their own derived order did not hold.
    """
    op = ProjectionGEMM(**kwargs, precision=Precision.MEDIUM).resolved(NPU2)
    for name in ("A", "C"):
        operand = getattr(op, name)
        result = op.lane_transfers(operand)
        if not described:
            assert result is None, f"{name}: expected a refusal at {kwargs}"
            continue
        _assert_described_and_faithful(op, name)


def test_projection_gemm_refuses_a_per_call_bound():
    """A row bound moves ``A`` and ``C`` through an ``offset_parameter`` and a
    ``repeat_parameter``, neither of which ``Operand.transfers()``'s tuple
    carries, so a bound call is refused rather than described wrong.
    """
    op = ProjectionGEMM(M=256, K=512, N=1024, precision=Precision.MEDIUM)
    op.use_value("valid", PerCall("n", Kind.SCRATCHPAD, np.int32).affine())
    op = op.resolved(NPU2)
    assert op.lane_transfers(op.A) is None
    assert op.lane_transfers(op.C) is None
