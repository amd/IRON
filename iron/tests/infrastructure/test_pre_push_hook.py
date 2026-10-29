# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""scripts/hooks/pre-push, run as git runs it, over a project of one Python file."""

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[3]


@pytest.mark.parametrize(
    "source,verdict",
    [
        ('x = {  "a":1 }\n', "❌ Python formatting check failed"),
        ('x = {"a": 1}\n', "✅ Python formatting check passed"),
    ],
)
def test_the_hook_holds_python_to_black(tmp_path, source, verdict):
    (tmp_path / "scripts" / "hooks").mkdir(parents=True)
    for script in ("scripts/clang-format-wrapper.py", "scripts/hooks/pre-push"):
        shutil.copy(_ROOT / script, tmp_path / script)
    # Its own root for black, wherever the test's temporary directory is.
    (tmp_path / "pyproject.toml").write_text("[tool.black]\n")
    (tmp_path / "module.py").write_text(source)
    env = dict(os.environ, PATH=f"{Path(sys.executable).parent}:{os.environ['PATH']}")
    result = subprocess.run(
        ["bash", "scripts/hooks/pre-push"],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
    )
    assert verdict in result.stdout, result.stdout + result.stderr
