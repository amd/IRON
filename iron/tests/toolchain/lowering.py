# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every declared operator lowers to an NPU instruction stream.

Needs the mlir-aie package (its bindings generate the MLIR, its ``aiecc``
lowers it) but neither Peano nor a device: ``--get-npu-insts`` places,
routes, assigns buffer addresses, lowers the DMAs and emits the runtime
sequence's instructions without compiling a core. What that checks is
everything the operator model owns: the array an ``array()`` builds is
placeable and routable, every descriptor a sequence issues is legal, the
resident writes and barrier sets lower. What it cannot check is the
kernels, which need Peano, and the numbers, which need hardware.

The case table is ``iron/tests/common/cases.py``, one construction per
shape and dtype decision each operator makes.
"""

import importlib
import subprocess

import pytest

from iron.common import Incompatible, Unresolvable
from iron.tests.common.cases import CASES
from iron.tests.toolchain.tools import AIECC, requires

pytestmark = requires("aiecc")


def lower(op, tmp_path, name=None):
    """Generate the operator's MLIR and lower it to instructions; return both paths."""
    from aie.iron import ExternalFunction

    name = name or op.name
    src = tmp_path / f"{name}.mlir"
    # CompilableDesign clears the kernel registry before generating; a bare
    # generator() call in one process must do the same, or two designs
    # declaring one kernel with different flags collide. And after, as
    # compile() does: what stays registered is the next test's collision.
    ExternalFunction._instances.clear()
    try:
        src.write_text(str(op.generator()()))
    finally:
        ExternalFunction._instances.clear()
    out = tmp_path / "out"
    result = subprocess.run(
        [
            str(AIECC),
            "--get-npu-insts",
            f"--npu-insts-name={name}.bin",
            f"--output-dir={out}",
            f"--tmpdir={tmp_path / 'prj'}",
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
    except (ValueError, Unresolvable, Incompatible) as e:
        pytest.skip(f"not for {device.resolve().name}: {e}")
    lower(op, tmp_path)


@pytest.mark.parametrize(
    "module,cls_name,kwargs,bound",
    [
        ("relu", "ReLU", dict(size=4096, tile_size=256, num_aie_columns=2), "valid"),
        ("rms_norm", "RMSNorm", dict(rows=64, tile_size=256), "valid"),
        ("softmax", "Softmax", dict(rows=64, cols=64, num_aie_columns=2), "valid"),
        ("rope.op", "RoPE", dict(rows=64, cols=64, num_aie_columns=2), "valid"),
        # These stream every row and bound their compute: no size patch, so
        # they lower all the way through aiecc today.
        ("gemm.op", "GEMM", dict(M=256, K=64, N=512, num_aie_columns=4), "valid"),
        (
            "mha.op",
            "MHA",
            dict(num_heads=4, num_KV_heads=2, seq_len=256, num_pipelines=2),
            "valid",
        ),
    ],
    ids=lambda v: v if isinstance(v, str) and "." not in v else "",
)
def test_a_bounded_operator_lowers_or_waits_for_the_size_kind(
    device, module, cls_name, kwargs, bound, tmp_path
):
    """An operator with a bounded extent builds its array against the
    per-call words (each core reads its count from the scratchpad) and
    asks the toolchain to patch its descriptors' sizes. Until mlir-aie has
    the size-kind parameter that is a skip naming it, not a failure.
    """
    cls = getattr(importlib.import_module(f"iron.operators.{module}"), cls_name)
    try:
        op = cls(**kwargs).resolved(device)
    except (ValueError, Unresolvable, Incompatible) as e:
        pytest.skip(f"not for {device.resolve().name}: {e}")
    op.use_value(bound, "n")  # what x[:n] in a graph does
    lower(op, tmp_path)  # or the conftest's skip, naming the missing kind
