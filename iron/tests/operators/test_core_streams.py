# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Experts', SelectiveScan's and GatedDeltaRule's arrays, built device-free: every operand
bound, and no core reading more streams than its two input DMA channels.
"""

import inspect

import pytest
from aie.helpers.util import flatten_fn_args
from aie.iron import Worker, kernels
from aie.iron.dataflow.objectfifo import ObjectFifoHandle

from iron.operators.experts import Experts
from iron.operators.gated_delta_rule import GatedDeltaRule
from iron.operators.selective_scan import SelectiveScan

# Each operator's kernel and the parameters its build() passes it,
# which an older mlir-aie's lacks (blocks=, from 7807032). Kept in step with
# those calls by hand: a parameter added there belongs here too.
KERNELS = {
    Experts: (
        "moe",
        "experts",
        {"hidden", "width", "num_experts", "top_k", "rows", "cols"},
    ),
    SelectiveScan: ("ssm", "selective_scan", {"rows", "head_dim", "state", "blocks"}),
    GatedDeltaRule: (
        "ssm",
        "gated_delta_rule",
        {"rows", "key_dim", "value_dim", "blocks"},
    ),
}

CASES = [
    (cls, case)
    for cls in (Experts, SelectiveScan, GatedDeltaRule)
    for case in cls.test.cases
]


@pytest.mark.parametrize(
    "cls,case", CASES, ids=[f"{c.__name__}-{i}" for i, (c, _) in enumerate(CASES)]
)
def test_each_core_reads_at_most_two_streams(cls, case, npu2):
    module, name, params = KERNELS[cls]
    kernel = getattr(getattr(kernels, module, None), name, None)
    if kernel is None or params - inspect.signature(kernel).parameters.keys():
        pytest.skip(f"mlir-aie has no kernels.{module}.{name} taking {sorted(params)}")
    op = cls(**case.kwargs).resolved(npu2)
    built = op.layout().build()
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
