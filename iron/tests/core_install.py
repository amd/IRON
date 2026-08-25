# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a core install must be able to import.

``requirements.txt`` is the core install; ``requirements_stream.txt`` adds
``onnx``/``onnxscript`` for the one stream-dse-backed operator, whose test skips
itself when they are absent. That promise only holds if nothing reachable from
``import iron.operators`` pulls them in -- a hard import there fails pytest
collection for every operator, not just that one.

The dependencies are usually installed in the environment running this, so the
check has to happen in a child interpreter that cannot see them.
"""

import subprocess
import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[2]

_BLOCK_AND_IMPORT = """
import sys


class Blocked:
    def find_spec(self, name, path=None, target=None):
        if name.split(".")[0] in ("onnx", "onnxscript"):
            raise ImportError("No module named %r" % name)
        return None


sys.meta_path.insert(0, Blocked())
import {module}
"""


@pytest.mark.parametrize("module", ["iron.operators", "iron.common.stream.kernels"])
def test_imports_without_stream_dependencies(module):
    result = subprocess.run(
        [sys.executable, "-c", _BLOCK_AND_IMPORT.format(module=module)],
        cwd=_REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
