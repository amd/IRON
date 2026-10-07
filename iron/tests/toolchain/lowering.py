# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every declared operator lowers to an NPU instruction stream.

Needs the mlir-aie package (its bindings generate the MLIR, its ``aiecc``
lowers it) and Peano, but no device: ``--get-npu-insts`` places, routes,
assigns buffer addresses, lowers the DMAs and emits the runtime sequence's
instructions. Peano is there for aiecc's probe of each core, which measures
its stack and so lowers the core's IR with every kernel it merges (an
``inline`` kernel, like the rounding-mode setup a kernel contract asks for);
object-linked kernels are not compiled. What that checks is everything the
operator model owns: the array an ``array()`` builds is placeable and
routable, every descriptor a sequence issues is legal, the resident writes
and barrier sets lower. What it cannot check is the kernels' objects and
the numbers, which need hardware.

The case table is ``iron/tests/common/cases.py``, one construction per
shape and dtype decision each operator makes.
"""

import importlib
import subprocess

import pytest

from iron.common import Unresolvable
from iron.common.design import OperatorDesign
from iron.tests.common.cases import CASES
from iron.tests.toolchain.tools import AIECC, PEANO, requires

pytestmark = requires("aiecc", "peano")


def lower(op, tmp_path, name=None):
    """Generate the operator's MLIR and lower it to instructions; return both paths."""
    from aie.iron import ExternalFunction
    from aie.utils import get_current_device
    from aie.utils.compile import compile_external_kernels, resolve_target_arch

    name = name or op.name
    src = tmp_path / f"{name}.mlir"
    # CompilableDesign clears the kernel registry before generating; a bare
    # generator() call in one process must do the same, or two designs
    # declaring one kernel with different flags collide. And after, as
    # compile() does: what stays registered is the next test's collision.
    ExternalFunction._instances.clear()
    try:
        src.write_text(str(OperatorDesign(op).build()))
        # aiecc merges these into the core IR it probes, reading them beside
        # the MLIR; the object-linked kernels it never reads here.
        merged = [f for f in ExternalFunction._instances if f.link_with_mode == "merge"]
    finally:
        ExternalFunction._instances.clear()
    arch = resolve_target_arch(get_current_device(probe_runtime=False))
    compile_external_kernels(merged, str(src.parent), arch)
    out = tmp_path / "out"
    result = subprocess.run(
        [
            str(AIECC),
            "--get-npu-insts",
            f"--peano={PEANO}",
            f"--npu-insts-name={name}.bin",
            f"--output-dir={out}",
            f"--tmpdir={tmp_path / 'prj'}",
            *op.aiecc_flags,
            str(src),
        ],
        capture_output=True,
        text=True,
        timeout=900,
    )
    assert result.returncode == 0, f"aiecc failed on {src}:\n{result.stderr[-4000:]}"
    insts = out / f"{name}.bin"
    assert insts.exists() and insts.stat().st_size > 0
    return src, insts


def _cases():
    for module, cls_name, kwargs_list in CASES:
        for i, kwargs in enumerate(kwargs_list):
            yield pytest.param(module, cls_name, kwargs, id=f"{cls_name}-{i}")


@pytest.mark.parametrize("module,cls_name,kwargs", list(_cases()))
def test_operator_lowers_to_instructions(device, module, cls_name, kwargs, tmp_path):
    cls = getattr(importlib.import_module(f"iron.operators.{module}"), cls_name)
    try:
        op = cls(**kwargs)
        op.resolved(device)
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
    op.use_value(bound, "n")  # what x[:n] in a graph does
    lower(op, tmp_path)
