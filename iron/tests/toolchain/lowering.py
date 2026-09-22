# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every declared operator lowers to an NPU instruction stream.

Needs the mlir-aie package (its bindings generate the MLIR, its ``aiecc``
lowers it) but neither Peano nor a device: ``--get-npu-insts`` places,
routes, assigns buffer addresses, lowers the DMAs and emits the runtime
sequence's instructions without compiling a core. What that checks is
everything the operator model owns: the array a ``design()`` builds is
placeable and routable, every descriptor a sequence issues is legal, the
resident writes and barrier sets lower. What it cannot check is the
kernels, which need Peano, and the numbers, which need hardware.

The case table is ``iron/tests/common/cases.py``, one construction per
shape and dtype decision each operator makes.
"""

import importlib
import subprocess

import pytest

from iron.common.declare import Incompatible, Untunable
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
    # declaring one kernel with different flags collide.
    ExternalFunction._instances.clear()
    src.write_text(str(op.generator()()))
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
        op.tuned(device)
    except (ValueError, Untunable, Incompatible) as e:
        pytest.skip(f"not for {device.resolve().name}: {e}")
    lower(op, tmp_path)
