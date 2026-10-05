# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Test helpers the FastFlowLM-derived operators share."""

import aie.utils as aie_utils
import pytest
from aie.dialects._aie_enum_gen import AIEArch


def _on_aie2p():
    dev = aie_utils.get_current_device()
    return dev is not None and dev.arch == AIEArch.AIE2p


# The FastFlowLM kernels use AIE2P's bfp16 and its native tanh.
requires_aie2p = pytest.mark.skipif(not _on_aie2p(), reason="AIE2P only")

_dev = aie_utils.get_current_device()
# Every flm.GEMM shape times out on NPU1 hardware, and a run of timeouts leaves
# the device returning EIO until it is reset, failing every later job.
skip_flm_gemm_on_npu1 = pytest.mark.skipif(
    _dev is not None and _dev.resolve().name == "npu1",
    reason="flm.GEMM hangs on NPU1 hardware",
)
