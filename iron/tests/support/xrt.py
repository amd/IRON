# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A process as an unsourced XRT leaves it: no pyxrt, so no NPU runtime."""

import importlib.util
import os

import pytest


def without_xrt() -> dict[str, str]:
    """``os.environ`` with pyxrt's directory off ``PYTHONPATH``; skips the
    calling test where pyxrt is installed rather than on ``PYTHONPATH``.
    """
    env = dict(os.environ)
    pyxrt = importlib.util.find_spec("pyxrt")
    if pyxrt is None or pyxrt.origin is None:
        return env
    hidden = os.path.dirname(pyxrt.origin)
    entries = env.get("PYTHONPATH", "").split(os.pathsep)
    if hidden not in entries:
        pytest.skip(f"pyxrt is installed, not on PYTHONPATH: {pyxrt.origin}")
    env["PYTHONPATH"] = os.pathsep.join(p for p in entries if p != hidden)
    return env
