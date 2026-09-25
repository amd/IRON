#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A factory kernel must compile when AIEContext's build_dir is relative.

mlir-aie's compile_external_kernel() runs the compiler with cwd set to its
output directory, so a relative output directory is resolved twice and the
compiler looks for the kernel source under build_dir/<arch>/build_dir/<arch>.
Llama's AIEContext(build_dir="build_elf") hit exactly this. The operator
tests never did because their build_dir is absolute.
"""

import os
from pathlib import Path

import aie.utils as aie_utils
from aie.iron.device import NPU2

from iron.common import AIEContext
from iron.common.compilation import KernelObjectArtifact
from iron.operators.elementwise_mul.op import ElementwiseMul


def test_factory_kernel_compiles_with_a_relative_build_dir(tmp_path):
    aie_utils.set_current_device(NPU2())
    ctx = AIEContext(build_dir=os.path.relpath(tmp_path / "build_rel"))
    op = ElementwiseMul(size=4096, tile_size=4096, num_aie_columns=1, context=ctx)
    op.compile()

    objects = [a for a in op.artifacts.bfs() if isinstance(a, KernelObjectArtifact)]
    assert objects, "ElementwiseMul produced no KernelObjectArtifact"
    for obj in objects:
        path = Path(obj.filename).resolve()
        assert path.is_relative_to(tmp_path / "build_rel"), path
        assert path.is_file(), f"{path} was not built"
