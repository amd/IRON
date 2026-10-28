# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An operator, or every operator a graph records, lowered to instructions."""

from aie.iron import ExternalFunction
from aie.utils import get_current_device
from aie.utils.compile import (
    compile_external_kernels,
    compile_mlir_module,
    resolve_target_arch,
)

from iron.common.design import OperatorDesign


def lower(op, tmp_path, name=None):
    """Generate the operator's MLIR and lower it to instructions; return both paths."""
    # op.name spells out every parameter, past a file name's 255 bytes for some.
    name = name or type(op).__name__
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


def lower_all(recording, tmp_path, device=None):
    for i, op in enumerate(recording.operators):
        (tmp_path / str(i)).mkdir()
        if device is not None:
            op = op.resolved(device)
        lower(op, tmp_path / str(i), name=f"{i}_{type(op).__name__}")
