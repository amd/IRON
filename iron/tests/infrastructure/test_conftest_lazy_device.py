# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The root conftest.py's device gating, run as a real pytest session.

Its pytest_collection_modifyitems must not resolve a device unless some collected
test restricts itself via @pytest.mark.supported_devices: resolving one opens the
single-tenant NPU on every plain `pytest` in this tree, whatever was selected.
When a test does restrict itself, it skips the tests this device is not listed
for, and skips them all, each with the reason, when there is no NPU runtime
at all: the rest of the tree still runs on a host without an NPU.

Each case runs pytest in a subprocess, over a directory holding a copy of the
root conftest and one test module. The no-runtime cases hide pyxrt from it,
which is what an unsourced XRT amounts to and the setup the laziness exists for.
"""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from iron.tests.support.xrt import without_xrt

_ROOT_CONFTEST = Path(__file__).resolve().parents[3] / "conftest.py"

_INI = """\
[pytest]
markers =
    supported_devices(*devices): only supported on the given devices
"""


def _pytest(tmp_path, test_source, hide_xrt=False):
    """Run pytest over one test module under the root conftest."""
    shutil.copy(_ROOT_CONFTEST, tmp_path / "conftest.py")
    (tmp_path / "pytest.ini").write_text(_INI)
    (tmp_path / "test_gated.py").write_text(test_source)
    env = without_xrt() if hide_xrt else None
    return subprocess.run(
        [sys.executable, "-m", "pytest", "-p", "no:cacheprovider"]
        + ["-v", "-rs", "test_gated.py"],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
    )


def test_unrestricted_tests_need_no_npu_runtime(tmp_path):
    result = _pytest(
        tmp_path,
        "def test_plain():\n    pass\n",
        hide_xrt=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "1 passed" in result.stdout


@pytest.mark.parametrize("phase", ["setup", "call"])
def test_device_heap_exhaustion_is_a_failure(tmp_path, monkeypatch, phase):
    monkeypatch.setenv("IRON_XFAIL_DEVICE_HEAP", "1")
    source = (
        "import pytest\n"
        "def heap():\n"
        "    raise RuntimeError('DRM_IOCTL_AMDXDNA_CREATE_BO failed: err=-28')\n"
    )
    source += (
        "@pytest.fixture\n"
        "def allocate():\n    heap()\n"
        "def test_heap(allocate):\n    pass\n"
        if phase == "setup"
        else "def test_heap():\n    heap()\n"
    )
    result = _pytest(tmp_path, source, hide_xrt=True)
    assert result.returncode == 1, result.stdout + result.stderr
    assert ("1 error" if phase == "setup" else "1 failed") in result.stdout
    assert "xfailed" not in result.stdout


def test_restricted_test_without_npu_runtime_skips_with_the_reason(tmp_path):
    result = _pytest(
        tmp_path,
        "import pytest\n"
        "def test_plain():\n    pass\n"
        "@pytest.mark.supported_devices('npu1', 'npu2')\n"
        "def test_gated():\n    pass\n",
        hide_xrt=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "1 passed, 1 skipped" in result.stdout, result.stdout
    (reason,) = [ln for ln in result.stdout.splitlines() if ln.startswith("SKIPPED")]
    assert "No NPU runtime: " in reason, reason


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
