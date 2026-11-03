# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``iron.tune.measure``'s device lock, device-free."""

import subprocess
import sys

from iron.tune.measure import NpuLock


def test_npu_lock_keeps_another_process_out_until_its_outermost_exit(tmp_path):
    path = tmp_path / "npu.lock"
    probe = [
        sys.executable,
        "-c",
        "import fcntl\n"
        f"f = open({str(path)!r}, 'a+')\n"
        "fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)",
    ]
    lock = NpuLock(path)
    with lock:
        with lock:
            assert lock.depth == 2
        held = subprocess.run(probe, capture_output=True).returncode
    released = subprocess.run(probe, capture_output=True).returncode
    assert held != 0 and released == 0
    assert lock.depth == 0 and lock.file is None
