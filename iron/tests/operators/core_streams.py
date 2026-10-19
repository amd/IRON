# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Experts', SelectiveScan's and GatedDeltaRule's arrays, built device-free: every operand
bound, and no core reading more streams than its two input DMA channels.
"""

import pytest
from aie.helpers.util import flatten_fn_args
from aie.iron import Worker, kernels
from aie.iron.dataflow.objectfifo import ObjectFifoHandle

from iron.common import Unresolvable
from iron.operators.experts import Experts
from iron.operators.gated_delta_rule import GatedDeltaRule
from iron.operators.selective_scan import SelectiveScan

CASES = [
    (cls, case)
    for cls in (Experts, SelectiveScan, GatedDeltaRule)
    for case in cls.test.cases
]


@pytest.mark.parametrize(
    "cls,case", CASES, ids=[f"{c.__name__}-{i}" for i, (c, _) in enumerate(CASES)]
)
def test_each_core_reads_at_most_two_streams(cls, case, npu2):
    if not hasattr(kernels, "ssm") or not hasattr(kernels.ssm, "gated_delta_rule"):
        pytest.skip("mlir-aie has no expert or scan kernels before 454c28d")
    op = cls(**case.kwargs).resolved(npu2)
    built = op.array_config().build()
    for operand in (*op.inputs, *op.outputs):
        assert operand.handles
    for worker in (o for o in built.objects if isinstance(o, Worker)):
        reads = [
            a
            for a in flatten_fn_args(worker.fn_args)
            if isinstance(a, ObjectFifoHandle) and not a._is_prod
        ]
        assert len(reads) <= 2


@pytest.mark.parametrize(
    "cls,case", CASES, ids=[f"{c.__name__}-{i}" for i, (c, _) in enumerate(CASES)]
)
@pytest.mark.parametrize("device", ["npu1", "npu2"])
def test_the_columns_resolved_fit_the_shims_input_channels(cls, case, device, request):
    """Every lane of every input is a shim stream: two to a shim, so
    SelectiveScan's four and GatedDeltaRule's five a core cap the cores.
    """
    dev = request.getfixturevalue(device)
    op = cls(**case.kwargs).resolved(dev)
    assert sum(o.lanes for o in op.inputs) <= dev.shim_dma_channels_in


@pytest.mark.parametrize(
    "op,match",
    [
        (SelectiveScan(rows=1024, heads=2, head_dim=16, state_size=16), "1024 rows"),
        (
            SelectiveScan(rows=8, heads=2, head_dim=528, state_size=16, columns=1),
            "66 slices a core",
        ),
        (
            GatedDeltaRule(rows=1024, k_heads=1, v_heads=2, key_dim=16, value_dim=16),
            "1024 rows",
        ),
        (
            GatedDeltaRule(
                rows=8, k_heads=1, v_heads=2, key_dim=16, value_dim=528, columns=1
            ),
            "66 slices a core",
        ),
    ],
)
def test_a_shape_no_shim_bd_holds_is_refused(op, match, npu2):
    """A core's slices repeat its rows' fill, at most 64 times a BD, and a
    BD dimension counts the rows, at most 1023.
    """
    with pytest.raises(Unresolvable, match=match):
        op.resolved(npu2)
