# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Gemma 4 E2B's random weights load under a peak-memory ceiling (CPU only).

Its per-layer embeddings (4.38 GiB bf16) are the largest of any shipped model: a whole-array float32 copy in the load path adds 8.76 GiB, past the ceiling.
"""

import os
import subprocess
import sys

from iron.lm.checkpoint import weights_file
from iron.lm.testing import require, weights_dir

DIRECTORY = weights_dir("gemma-4-e2b-it")
# Measured 14.73 GiB on xcoradaie220 (11-04).
CEILING_GIB = 18


def test_random_weights_load_under_the_ceiling():
    """A child process loads the model, so its peak is the load's alone, not this test session's."""
    require(DIRECTORY / "config.json", weights_file(DIRECTORY))
    child = subprocess.Popen(
        [
            sys.executable,
            "-c",
            "from iron.applications.gemma4 import Gemma4\n"
            f"Gemma4.from_checkpoint({str(DIRECTORY)!r}, random_weights=0, "
            "max_seq_len=8192)\n",
        ]
    )
    _, status, usage = os.wait4(child.pid, 0)
    assert os.waitstatus_to_exitcode(status) == 0
    peak = usage.ru_maxrss / 2**20
    assert peak <= CEILING_GIB, f"loading peaked at {peak:.2f} GiB"
