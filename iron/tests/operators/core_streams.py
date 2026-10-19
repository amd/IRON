# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Experts' and SelectiveScan's arrays, built device-free: every operand
bound, and no core reading more streams than its two input DMA channels.
"""

import pytest
from aie.helpers.util import flatten_fn_args
from aie.iron import Worker, kernels
from aie.iron.dataflow.objectfifo import ObjectFifoHandle

from iron.operators.experts import Experts
from iron.operators.selective_scan import SelectiveScan

CASES = [(Experts, case) for case in Experts.test.cases] + [
    (SelectiveScan, case) for case in SelectiveScan.test.cases
]


@pytest.mark.parametrize(
    "cls,case", CASES, ids=[f"{c.__name__}-{i}" for i, (c, _) in enumerate(CASES)]
)
def test_each_core_reads_at_most_two_streams(cls, case, npu2):
    if not hasattr(kernels, "ssm") or not hasattr(kernels.moe, "experts"):
        pytest.skip("mlir-aie has no expert or scan kernels before 780703205")
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
