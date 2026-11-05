# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Run the results publisher with the test session's Python and an explicit shell."""

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


def merge_results(run: Path, suite: Path) -> None:
    """Run the actual CI merge script, through Bash on Windows as well as POSIX."""
    bash = shutil.which("bash")
    if bash is None:
        pytest.skip("merge_results.sh requires Bash")
    script = Path(__file__).resolve().parents[3] / "ci" / "scripts" / "merge_results.sh"
    subprocess.run(
        [bash, script.as_posix(), run.as_posix(), suite.as_posix()],
        env=os.environ | {"PYTHON": Path(sys.executable).as_posix()},
        check=True,
        timeout=120,
    )
