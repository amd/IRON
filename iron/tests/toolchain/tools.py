# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What the toolchain gates share: which tools are installed, the devices
they build for, and the graph they all build.
"""

import shutil
from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16

aie = pytest.importorskip("aie")
import aie.utils.config as aie_config  # noqa: E402
from aie.iron.device import NPU2, from_name  # noqa: E402

AIECC = Path(aie.__file__).resolve().parents[2] / "bin" / "aiecc"
AIEBU = shutil.which("aiebu-asm")
XCLBINUTIL = shutil.which("xclbinutil")
try:
    PEANO = Path(aie_config.peano_install_dir())
except Exception:  # noqa: BLE001 - any failure means no Peano
    PEANO = None

_MISSING = {
    "aiecc": (not AIECC.exists(), f"no aiecc at {AIECC}"),
    "aiebu": (AIEBU is None, "no aiebu-asm on the PATH"),
    "xclbinutil": (XCLBINUTIL is None, "no xclbinutil on the PATH"),
    "peano": (PEANO is None or not PEANO.exists(), "no Peano (llvm-aie) installed"),
}


def requires(*tools):
    """Skip marks for a module that needs these tools."""
    return [pytest.mark.skipif(_MISSING[t][0], reason=_MISSING[t][1]) for t in tools]


DEVICES = {
    "npu2": lambda: NPU2(),  # pyright: ignore[reportCallIssue]
    "npu1": lambda: from_name("npu1", n_cols=4),
}


def swiglu_decode():
    """The swiglu decode graph function at Llama 3.2 1B's width, and that width."""
    from iron.operators.swiglu_decode.op import swiglu_decode

    z = lambda *s: np.zeros(s, dtype=bfloat16)  # noqa: E731
    E, H = 2048, 8192
    return swiglu_decode(z(H, E), z(H, E), z(E, H)), E
