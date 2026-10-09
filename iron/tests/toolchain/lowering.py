# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every declared operator lowers to an NPU instruction stream.

Needs the mlir-aie package (its bindings generate the MLIR, its ``aiecc``
lowers it) and Peano, but no device: ``--get-npu-insts`` places, routes,
assigns buffer addresses, lowers the DMAs and emits the runtime sequence's
instructions. Peano is there for the kernels and aiecc's probe of each
core, which links the core with them to measure its stack and reserve each
bank's kernel data before placement. What that checks is everything the
operator model owns: the array an ``array()`` builds is placeable and
routable, every descriptor a sequence issues is legal, the resident writes
and barrier sets lower. What it cannot check is the kernels' objects and
the numbers, which need hardware.

The cases are the catalog's own ``Testing`` declarations: each operator's
first default case, and every case it flags ``lower`` for a shape or dtype
decision that one does not reach.
"""

import importlib

import numpy as np
import pytest
from aie.iron import ExternalFunction
from aie.utils import get_current_device
from aie.utils.compile import (
    compile_external_kernels,
    compile_mlir_module,
    resolve_target_arch,
)

import iron.operators as catalog
from iron.common import graph
from iron.common.design import OperatorDesign
from iron.tests.toolchain.tools import DEVICES, requires

pytestmark = requires("aiecc", "peano")


def lower(op, tmp_path, name=None):
    """Generate the operator's MLIR and lower it to instructions; return both paths."""
    name = name or op.name
    src = tmp_path / f"{name}.mlir"
    # CompilableDesign clears the kernel registry before generating; a bare
    # generator() call in one process must do the same, or two designs
    # declaring one kernel with different flags collide. And after, as
    # compile() does: what stays registered is the next test's collision.
    ExternalFunction._instances.clear()
    try:
        src.write_text(str(OperatorDesign(op).build()))
        kernels = list(ExternalFunction._instances)
    finally:
        ExternalFunction._instances.clear()
    arch = resolve_target_arch(get_current_device(probe_runtime=False))
    compile_external_kernels(kernels, str(tmp_path), arch)
    insts = tmp_path / f"{name}.bin"
    compile_mlir_module(
        src.read_text(), insts_path=insts, work_dir=tmp_path, options=op.aiecc_flags
    )
    assert insts.stat().st_size > 0
    return src, insts


def _cases():
    params = []
    for device in sorted(DEVICES):
        dev = DEVICES[device]()
        for name in sorted(catalog._OPERATOR_MODULES):
            cls = getattr(catalog, name)
            if cls.test is None:
                continue
            cases = cls.test.resolve(cls, dev)
            first = next(c for c in cases if not c.extensive)
            for case in [first, *(c for c in cases if c.lower and c is not first)]:
                params.append(
                    pytest.param(device, cls, case, id=f"{device}-{name}-{case.label}")
                )
    return params


@pytest.mark.parametrize("device,cls,case", _cases(), indirect=["device"])
def test_operator_lowers_to_instructions(device, cls, case, tmp_path):
    try:
        op = cls(**case.kwargs).resolved(device)
    except ValueError as e:
        pytest.skip(f"not for {device.name}: {e}")
    lower(op, tmp_path)


@pytest.mark.parametrize(
    "module,cls_name,kwargs,bound",
    [
        ("relu", "ReLU", dict(size=4096, tile_size=256, num_aie_columns=2), "valid"),
        ("rms_norm", "RMSNorm", dict(rows=64, tile_size=256), "valid"),
        (
            "softmax",
            "Softmax",
            dict(rows=64, cols=256, block=64, num_aie_columns=2),
            "length",
        ),
        ("rope", "RoPE", dict(rows=64, cols=64, num_aie_columns=2), "valid"),
        ("gqa", "GQAScores", dict(heads=8, groups=4, seq_len=256), "valid"),
        ("gqa", "GQAContext", dict(heads=8, groups=4, seq_len=256), "valid"),
        # These stream every row and bound their compute: no size patch, so
        # they lower all the way through aiecc today.
        ("gemm", "GEMM", dict(M=256, K=64, N=512, num_aie_columns=4), "valid"),
        (
            "mha",
            "MHA",
            dict(num_heads=4, num_KV_heads=2, seq_len=256, num_pipelines=2),
            "valid",
        ),
    ],
    ids=lambda v: v if isinstance(v, str) and "." not in v else "",
)
def test_a_bounded_operator_lowers(device, module, cls_name, kwargs, bound, tmp_path):
    """An operator with a bounded extent builds its array against the
    per-call words (each core reads its count from the scratchpad) and
    asks the toolchain to patch its descriptors' lengths.
    """
    cls = getattr(importlib.import_module(f"iron.operators.{module}"), cls_name)
    try:
        op = cls(**kwargs).resolved(device)
    except ValueError as e:
        pytest.skip(f"not for {device.name}: {e}")
    n = graph.Value("n", "scratchpad", np.int32)
    op.use_value(bound, n.affine())  # what x[:n] in a graph does
    lower(op, tmp_path)
