# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Experts' array, built device-free: every operand bound, and no core
reading more streams than its two input DMA channels.
"""

import inspect

import pytest
from aie.helpers.util import flatten_fn_args
from aie.iron import Worker, kernels
from aie.iron.dataflow.objectfifo import ObjectFifoHandle

from iron.operators.experts import Experts

# The kernel and the parameters its build() passes it, which an older
# mlir-aie's lacks (blocks=, from 7807032). Kept in step with that call by
# hand: a parameter added there belongs here too.
KERNELS = {
    Experts: (
        "moe",
        "experts",
        {"hidden", "width", "num_experts", "top_k", "rows", "cols"},
    ),
}

CASES = [(cls, case) for cls in (Experts,) for case in cls.test.cases]


@pytest.mark.parametrize(
    "cls,case", CASES, ids=[f"{c.__name__}-{i}" for i, (c, _) in enumerate(CASES)]
)
def test_each_core_reads_at_most_two_streams(cls, case, npu2):
    module, name, params = KERNELS[cls]
    kernel = getattr(getattr(kernels, module, None), name, None)
    if kernel is None or params - inspect.signature(kernel).parameters.keys():
        pytest.skip(f"mlir-aie has no kernels.{module}.{name} taking {sorted(params)}")
    view = cls(**case.kwargs).resolved(npu2).layout()
    built = view.build()
    for operand in (*view.inputs, *view.outputs):
        assert operand.handles
    for worker in (o for o in built.objects if isinstance(o, Worker)):
        reads = [
            a
            for a in flatten_fn_args(worker.fn_args)
            if isinstance(a, ObjectFifoHandle) and not a._is_prod
        ]
        assert len(reads) <= 2
