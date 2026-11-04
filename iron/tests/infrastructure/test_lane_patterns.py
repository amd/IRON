# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``Operator.lane_transfers()``'s faithfulness.

For every catalog case of an operator with a hand-written ``sequence(rt)``, the per-lane
host access order it describes must equal, element for element, what the generated
module's shim tasks actually move. Device-free: ``generated_sequence`` only emits MLIR.
"""

from collections.abc import Iterator
from math import prod

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.helpers.taplib import PerCall, TensorAccessPattern

from iron.common import Precision, Unresolvable
from iron.common.image.packaging import Kind
from iron.common.testing import Case
from iron.operators.copy import Copy, Gather
from iron.operators.flm.gemm.op import ProjectionGEMM
from iron.operators.gemm import GEMM
from iron.operators.mha import MHA
from iron.operators.softmax import Softmax
from iron.tests.support.build import generated_sequence
from iron.tests.support.tools import DEVICES

pytestmark = pytest.mark.usefixtures("npu2")

NPU2 = DEVICES["npu2"]()
NPU1 = DEVICES["npu1"]()


def _lane_order(op, name: str) -> dict[int, list[TensorAccessPattern]]:
    """Per logical lane (in the order ``build()`` bound them).

    The patterns the generated module's shim tasks move buffer ``name`` by, in
    emission order.
    """
    _, tasks = generated_sequence(op, full_elf=False)
    idx = [b.name for b in op.buffers].index(name)
    operand = getattr(op, name)
    by_lane: dict[str, list[TensorAccessPattern]] = {}
    for t in tasks:
        if t.arg != idx:
            continue
        sizes = [int(s) for s in t.sizes.split(",")]
        strides = [int(s) for s in t.strides.split(",")]
        offset = t.offset if isinstance(t.offset, int) else 0
        by_lane.setdefault(t.lane, []).append(
            TensorAccessPattern(operand.shape, offset, sizes, strides)
        )
    return dict(enumerate(by_lane.values()))


def _slices(tap: TensorAccessPattern) -> Iterator[TensorAccessPattern]:
    """``tap`` in turn as patterns of 16M elements at most, outermost dimensions first."""
    if prod(tap.sizes) <= 1 << 24 or len(tap.sizes) == 1:
        yield tap
        return
    for i in range(tap.sizes[0]):
        yield from _slices(
            TensorAccessPattern(
                tap.tensor_dims,
                tap.offset + i * tap.strides[0],
                tap.sizes[1:],
                tap.strides[1:],
            )
        )


def _same_elements(
    a: list[TensorAccessPattern], b: list[TensorAccessPattern], index: np.ndarray
) -> bool:
    """Whether ``a``'s patterns in turn move the same elements as ``b``'s.

    Compared a slice at a time (``_slices``): a lane re-streaming its keys every
    round moves many times its operand, which whole would take gigabytes.
    """
    pieces = [
        (t.gather(index) for tap in taps for t in _slices(tap)) for taps in (a, b)
    ]
    left = [np.empty(0, index.dtype), np.empty(0, index.dtype)]
    while True:
        for k in (0, 1):
            while not len(left[k]):
                piece = next(pieces[k], None)
                if piece is None:
                    break
                left[k] = piece
        n = min(len(left[0]), len(left[1]))
        if not n:
            return not len(left[0]) and not len(left[1])
        if not np.array_equal(left[0][:n], left[1][:n]):
            return False
        left = [left[0][n:], left[1][n:]]


def _assert_described_and_faithful(op, name: str) -> None:
    operand = getattr(op, name)
    described = op.lane_transfers(operand)
    assert described is not None, f"{type(op).__name__}.{name} was not described"
    # A lane described in several patterns moves them in turn.
    predicted: dict[int, list] = {}
    for lane, tap, *_ in described:
        predicted.setdefault(lane, []).append(tap)
    truth = _lane_order(op, name)
    assert sorted(predicted) == sorted(
        truth
    ), f"{type(op).__name__}.{name}: lane sets differ"
    index = np.arange(prod(operand.shape), dtype=np.int32)
    for lane in sorted(truth):
        assert _same_elements(
            predicted[lane], truth[lane], index
        ), f"{type(op).__name__}.{name} lane {lane}"


def test_lanes_compare_by_their_elements_in_order_whatever_their_pieces():
    """The same elements cut at other piece boundaries match; reordered, missing or extra pieces do not."""
    shape = (4, 8)
    index = np.arange(prod(shape), dtype=np.int32)
    rows = [TensorAccessPattern(shape, 8 * r, [8], [1]) for r in range(4)]
    halves = [TensorAccessPattern(shape, 16 * h, [2, 8], [8, 1]) for h in range(2)]
    assert _same_elements(rows, halves, index)
    assert not _same_elements(rows[::-1], halves, index)
    assert not _same_elements(rows[:3], halves, index)
    assert not _same_elements(rows + rows[:1], halves, index)


@pytest.mark.parametrize("case", GEMM.test.resolve(GEMM, NPU2), ids=lambda c: c.label)
def test_gemm_lanes_are_faithful(case):
    """GEMM bounds its compute, not its DMA (AGENTS.md), so A, B and C's order holds at every catalog case regardless of a per-call bound."""
    op = GEMM(**case.kwargs).resolved(NPU2)
    for name in ("A", "B", "C"):
        _assert_described_and_faithful(op, name)


@pytest.mark.parametrize(
    "dev,case",
    [(NPU2, c) for c in MHA.test.resolve(MHA, NPU2)]
    + [
        (NPU1, c)
        for c in MHA.test.resolve(MHA, NPU1)
        if c.kwargs.get("cores_per_block") == 1
    ],
    ids=lambda x: x.label if isinstance(x, Case) else x.name,
)
def test_mha_lanes_are_faithful(dev, case):
    """Every catalog case on npu2, and one core a block's on npu1 too, at the unbounded shapes.

    Q and O stream every row unconditionally; K and V's (or KV's) order has
    no ``length_parameter`` there. One core a block streams KV a pattern a
    fill: a prompt's groups of rounds up to their last query, a decode
    step's lanes every n-th block.
    """
    with aie_utils.set_current_device(dev):
        try:
            op = MHA(**case.kwargs).resolved(dev)
        except Unresolvable as e:
            pytest.skip(str(e))
        # Split decode's Q rides KV's lanes: no stream of its own.
        for b in op.buffers:
            if b.streamed:
                _assert_described_and_faithful(op, b.name)


@pytest.mark.parametrize("paired", [False, True])
def test_mha_k_and_v_match_the_generated_module_under_a_kv_bound(paired):
    """``kv_blocks``, the ``length_parameter`` K and V (or KV) describe.

    Is the same real per-call parameter the generated module's shim tasks patch their
    length from, under a growing KV cache's attention (AGENTS.md's "length-free
    extents").
    """
    op = MHA(
        num_heads=8,
        num_KV_heads=2,
        seq_len=2048,
        kv_len=8192,
        num_pipelines=8,
        kv_paired=paired,
    )
    op.use_value("kv_valid", PerCall("n", Kind.SCRATCHPAD, np.int32).affine())
    op = op.resolved(NPU2)
    word = op.kv_blocks
    text, tasks = generated_sequence(op, full_elf=True)
    for name in ("KV",) if paired else ("K", "V"):
        operand = getattr(op, name)
        idx = [b.name for b in op.buffers].index(name)
        real = {t.length_parameter: int(t.length_unit) for t in tasks if t.arg == idx}
        assert len(real) == 1
        (real_param, real_unit), *_ = real.items()
        assert real_param.endswith(f"_{word.name}")
        described = op.lane_transfers(operand)
        for lane, tap, length_parameter, length_unit in described:
            assert length_parameter is word
            assert length_unit == real_unit
        for rows in (1, 63, 64, 8192):
            assert op.derived_at(word.name, kv_valid=rows) == -(-rows // op.B_kv)


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


def test_gather_y_lanes_are_faithful_unbounded():
    op = Gather(rows=64, table_rows=1024, row=256).resolved(NPU2)
    _assert_described_and_faithful(op, "y")


@pytest.mark.parametrize("rows", [15, 31, 32, 64])
def test_gather_y_lanes_match_the_generated_module_under_a_bound(rows):
    """Each feed's drain length (``drainedN``, 16-byte units: valid rows at full length, the rest padding) is the real word the generated module patches.

    At several row counts either side of a feed boundary (``rows`` is 64 over 4 feeds of
    ``chain``-batches, 8 rows a batch).
    """
    op = Gather(rows=64, table_rows=1024, row=256)
    op.use_value("valid_rows", PerCall("n", Kind.SCRATCHPAD, np.int32).affine())
    op = op.resolved(NPU2)
    described = op.lane_transfers(op.y)
    text, tasks = generated_sequence(op, full_elf=True)
    idx = [b.name for b in op.buffers].index("y")
    real_by_lane = {
        t.lane: (t.length_parameter, int(t.length_unit)) for t in tasks if t.arg == idx
    }
    lane_names = sorted(real_by_lane, key=lambda name: int(name.split("_")[-1]))
    for (lane, tap, length_parameter, length_unit), lane_name in zip(
        described, lane_names
    ):
        real_param, real_unit = real_by_lane[lane_name]
        # The hook's word is the same real per-call parameter the generated
        # module's task patches its length from, in the same units.
        assert real_param.endswith(f"_{length_parameter.name}")
        assert length_unit == real_unit
        predicted = op.derived_at(length_parameter.name, valid_rows=rows)
        # The static tap always covers the lane's whole (unbounded) share;
        # the bound only ever shortens it.
        assert predicted * length_unit <= prod(tap.sizes)


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
    # More than one row-block unit per lane: C's N-tile axis is resent whole
    # (outermost), not interleaved a row at a time (regression cover for a
    # permute bug lane_transfers() had here).
    pytest.param(dict(M=512, K=512, N=1024), True, id="two_units"),
    pytest.param(dict(M=1024, K=512, N=1024), True, id="four_units"),
]


@pytest.mark.parametrize("kwargs,described", _PROJECTION_GEMM_CASES)
def test_projection_gemm_lanes_are_faithful(kwargs, described):
    """A and C are described at one slab, ``m_chunk=1``.

    With every column doing work; past that (a second slab, too few active columns, a
    split leg) ``lane_transfers`` refuses, same as the catalog cases above would if
    their own derived order did not hold.
    """
    op = ProjectionGEMM(
        **kwargs, precision=Precision.MEDIUM, bfp16_b=not kwargs.get("b_col_maj")
    ).resolved(NPU2)
    for name in ("A", "C"):
        operand = getattr(op, name)
        result = op.lane_transfers(operand)
        if not described:
            assert result is None, f"{name}: expected a refusal at {kwargs}"
            continue
        _assert_described_and_faithful(op, name)


def test_projection_gemm_refuses_a_per_call_bound():
    """A row bound moves A and C through a dynamic start ``Operand.transfers()`` does not carry.

    The start is the second half of the core rows, and the tuple carries only
    ``length_parameter``/``length_unit``, so a bound call is refused rather than
    described wrong.
    """
    op = ProjectionGEMM(M=2048, K=512, N=1024, precision=Precision.MEDIUM, bfp16_b=True)
    op.use_value("valid", PerCall("n", Kind.SCRATCHPAD, np.int32).affine())
    op = op.resolved(NPU2)
    assert op.lane_transfers(op.A) is None
    assert op.lane_transfers(op.C) is None


def test_projection_gemm_refuses_a_second_slab_under_a_bound():
    """A row bound still needs one slab (``_single_slab``), whether or not it is reached.

    A shape refused unbounded (two slabs) is refused bounded too.
    """
    op = ProjectionGEMM(
        M=16384, K=512, N=1024, precision=Precision.MEDIUM, bfp16_b=True
    )
    op.use_value("valid", PerCall("n", Kind.SCRATCHPAD, np.int32).affine())
    op = op.resolved(NPU2)
    assert op.lane_transfers(op.A) is None
    assert op.lane_transfers(op.C) is None


def test_projection_gemm_m_chunk_refuses_a_bound_before_building():
    """``m_chunk > 1`` under a row bound is already refused at ``resolve()`` (``compatible()``).

    ``lane_transfers`` never has to.
    """
    op = ProjectionGEMM(
        M=512, K=512, N=20480, m_chunk=2, precision=Precision.MEDIUM, bfp16_b=True
    )
    op.use_value("valid", PerCall("n", Kind.SCRATCHPAD, np.int32).affine())
    with pytest.raises(ValueError, match=r"m_chunk \(2\)"):
        op.resolved(NPU2)
