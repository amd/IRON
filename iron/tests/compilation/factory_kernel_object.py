# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An operator can build its kernel object from an ``aie.iron.kernels`` factory."""

import os
import subprocess
from pathlib import Path

import aie.utils as aie_utils
import aie.utils.config
import numpy as np
from aie.iron import kernels
from aie.iron.device import NPU2

from iron.common import compilation as comp
from iron.common.context import AIEContext


def _build(tmp_path):
    aie_utils.set_current_device(NPU2())
    fn = kernels.passthrough(tile_size=1024, dtype=np.int32)
    artifact = comp.KernelObjectArtifact.from_extern(fn)
    graph = comp.CompilationArtifactGraph([artifact])
    comp.compile(AIEContext(build_dir=tmp_path).compilation_rules, graph, str(tmp_path))
    return fn, artifact


def _defined(path):
    out = subprocess.run(
        [str(aie.utils.config.nm_path()), "--defined-only", path],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    return {line.split()[-1] for line in out.splitlines()}


def test_the_object_exports_the_factory_symbol(tmp_path):
    """The design calls fn.name, which carries the factory's symbol prefix."""
    fn, artifact = _build(tmp_path)
    assert Path(artifact.filename).name == fn.object_file_name
    assert fn.name in _defined(artifact.filename)


def test_an_out_of_date_object_is_rebuilt(tmp_path):
    """An object older than its source is rebuilt, though its bytes are intact."""
    _, artifact = _build(tmp_path)
    past = os.path.getmtime(artifact.dependencies[0].filename) - 60
    os.utime(artifact.filename, (past, past))

    _, rebuilt = _build(tmp_path)

    assert os.path.getmtime(rebuilt.filename) > past
