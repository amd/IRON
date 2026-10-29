# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolLM3 3B's per-step form (``tests/applications/decoders`` and
``long_context`` hold its full-ELF one): every step its own xclbin
dispatch, the form NPU1 runs. The model is built and dropped with the
class, first: after any other test it would be held beside the module's
full-ELF one.
"""

import aie.utils as aie_utils
import pytest

from iron.applications.smollm3 import SmolLM3
from iron.lm.testing import (
    check_accuracy,
    check_determinism,
    check_generation,
    load_from_flags,
    weights_dir,
)

WEIGHTS = weights_dir("smollm3-3b") / "model.safetensors.index.json"

# KL(fp32 CPU || NPU), each step's form, measured mean 0.0045, p90 0.012,
# max 0.019 over 20 steps (Strix Halo), 2 top-1 swaps.
MAX_KL = {"Mean": 0.02, "P90": 0.04, "Max": 0.08}


@pytest.fixture(scope="module")
def load(request):
    return load_from_flags(request, SmolLM3, WEIGHTS)


@pytest.mark.extensive
@pytest.mark.supported_devices("npu1", "npu2")
class TestEachStep:
    @pytest.fixture(scope="class")
    def model(self, load):
        model = load(full_elf=False)
        assert not model.device_loop
        yield model
        if aie_utils.DefaultNPURuntime is not None:
            aie_utils.DefaultNPURuntime.cleanup()

    def test_smollm3_3b_each_step(self, model, record_property):
        check_generation(model, 13, 1, record=record_property)

    def test_smollm3_3b_each_step_accuracy(self, model, record_property):
        check_accuracy(model, MAX_KL, 20, 256, record=record_property)

    def test_smollm3_3b_each_step_determinism(self, model, record_property):
        check_determinism(model, 4, 3, 128, record=record_property)
