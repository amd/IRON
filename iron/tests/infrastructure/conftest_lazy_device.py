#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The root conftest.py's device gating, run as a real pytest session.

Its pytest_collection_modifyitems must not resolve a device unless some collected
test restricts itself via @pytest.mark.supported_devices: resolving one opens the
single-tenant NPU on every plain `pytest` in this tree, whatever was selected.
When a test does restrict itself, it skips the tests this device is not listed
for, and stops with the reason when there is no NPU runtime at all.

Each case runs pytest in a subprocess, over a directory holding a copy of the
root conftest and one test module. The no-runtime cases hide pyxrt from it,
which is what an unsourced XRT amounts to and the setup the laziness exists for.
"""

import importlib.util
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

_ROOT_CONFTEST = Path(__file__).resolve().parents[3] / "conftest.py"

_INI = """\
[pytest]
markers =
    supported_devices(*devices): only supported on the given devices
"""


def _pytest(tmp_path, test_source, without_xrt=False):
    """Run pytest over one test module under the root conftest."""
    shutil.copy(_ROOT_CONFTEST, tmp_path / "conftest.py")
    (tmp_path / "pytest.ini").write_text(_INI)
    (tmp_path / "test_gated.py").write_text(test_source)
    env = dict(os.environ)
    pyxrt = importlib.util.find_spec("pyxrt")
    if without_xrt and pyxrt is not None and pyxrt.origin is not None:
        hidden = os.path.dirname(pyxrt.origin)
        entries = env.get("PYTHONPATH", "").split(os.pathsep)
        if hidden not in entries:
            pytest.skip(f"pyxrt is installed, not on PYTHONPATH: {pyxrt.origin}")
        env["PYTHONPATH"] = os.pathsep.join(p for p in entries if p != hidden)
    return subprocess.run(
        [sys.executable, "-m", "pytest", "-p", "no:cacheprovider"]
        + ["--iterations", "1", "-v", "test_gated.py"],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
    )


def test_unrestricted_tests_need_no_npu_runtime(tmp_path):
    result = _pytest(
        tmp_path,
        "def test_plain():\n    pass\n",
        without_xrt=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "1 passed" in result.stdout


def test_restricted_test_without_npu_runtime_stops_with_the_reason(tmp_path):
    result = _pytest(
        tmp_path,
        "import pytest\n"
        "@pytest.mark.supported_devices('npu1', 'npu2')\n"
        "def test_gated():\n    pass\n",
        without_xrt=True,
    )
    assert result.returncode == pytest.ExitCode.USAGE_ERROR, result.stdout
    assert "No NPU runtime: " in result.stderr
    assert "xrt" in result.stderr.lower(), result.stderr


@pytest.mark.supported_devices("npu1", "npu2")
def test_restricted_tests_skip_where_the_device_is_not_listed(tmp_path):
    result = _pytest(
        tmp_path,
        "import pytest\n"
        "def test_plain():\n    pass\n"
        "@pytest.mark.supported_devices('npu1', 'npu2')\n"
        "def test_any_npu():\n    pass\n"
        "@pytest.mark.supported_devices('no_such_npu')\n"
        "def test_elsewhere():\n    pass\n",
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "2 passed, 1 skipped" in result.stdout, result.stdout
    assert "test_elsewhere SKIPPED (Not supported on" in result.stdout, result.stdout
