# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Test helpers the FastFlowLM-derived operators share."""

import pytest

import aie.utils as aie_utils
from aie.dialects._aie_enum_gen import AIEArch


def _on_aie2p():
    dev = aie_utils.get_current_device()
    return dev is not None and dev.arch == AIEArch.AIE2p


# The FastFlowLM kernels use AIE2P's bfp16 and its native tanh.
requires_aie2p = pytest.mark.skipif(not _on_aie2p(), reason="AIE2P only")
