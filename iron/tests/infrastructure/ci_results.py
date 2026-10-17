#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The root conftest.py's results CSV, run as a real pytest session: a test
whose fixture fails in setup is a failed check, not missing from the CSV.
"""

import csv
import shutil
import subprocess
import sys
from pathlib import Path

_ROOT_CONFTEST = Path(__file__).resolve().parents[3] / "conftest.py"

_TESTS = """\
import pytest

@pytest.fixture(scope="module")
def runner():
    pytest.fail("this CI runner lacks config.json", pytrace=False)

def test_accuracy(runner):
    pass

def test_latency(runner):
    pass

def test_plain():
    pass

def test_skipped():
    pytest.skip("not here")
"""


def test_a_test_failing_in_setup_is_a_failed_check(tmp_path):
    shutil.copy(_ROOT_CONFTEST, tmp_path / "conftest.py")
    (tmp_path / "pytest.ini").write_text("[pytest]\n")
    (tmp_path / "test_model.py").write_text(_TESTS)
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-p", "no:cacheprovider", "test_model.py"]
        + [f"--csv-output={tmp_path / 'out.csv'}"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1, result.stdout + result.stderr
    with open(tmp_path / "out.csv") as f:
        checks = {row["Test"]: row["Checks"] for row in csv.DictReader(f)}
    assert checks == {
        "test_accuracy": "0/1",
        "test_latency": "0/1",
        "test_plain": "1/1",
    }
