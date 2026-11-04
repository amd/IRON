# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Which of each shipped decoder's attention shapes take npu2's fused attention (device-free).

The shapes that cannot are listed, so a new model or shape that misses the gain fails here.
"""

import aie.utils as aie_utils
import pytest

from iron import Profile
from iron.applications.gemma4 import Gemma4
from iron.applications.granite import Granite
from iron.applications.granite_hybrid import GraniteHybrid
from iron.applications.llama import Llama
from iron.common.graph.compiled import apply_profile
from iron.lm.checkpoint import weights_file
from iron.lm.testing import require, weights_dir
from iron.operators.mha import MHA

# Each decoder's checkpoint, and its (decode step, d) shapes the fused path
# does not take yet: Gemma 4's global layers at d=512 (no fused d=512 core).
DECODERS = [
    pytest.param(Llama, "llama3.2-1b", set(), id="llama-1b"),
    pytest.param(Llama, "llama3.2-3b", set(), id="llama-3b"),
    pytest.param(Granite, "granite-4.2-3b", set(), id="granite-3b"),
    pytest.param(GraniteHybrid, "granite-4.0-h-1b", set(), id="granite-h-1b"),
    pytest.param(
        Gemma4, "gemma-4-e2b-it", {(False, 512), (True, 512)}, id="gemma4-e2b"
    ),
]

# No device is used, but the npu2 runner is the one staging these checkpoints.
pytestmark = pytest.mark.supported_devices("npu2")


@pytest.mark.parametrize("cls,checkpoint,composed", DECODERS)
def test_each_attention_shape_is_fused_unless_listed(cls, checkpoint, composed, npu2):
    """Prompt chunks take float32 scores one core a query block; decode steps split over keys."""
    directory = weights_dir(checkpoint)
    require(directory / "config.json", weights_file(directory))
    with aie_utils.set_current_device(npu2):
        model = cls.from_checkpoint(directory, random_weights=0, max_seq_len=8192)
        profile = Profile.load(model.profile / "npu2.json")
        missed = set()
        for shape in model.shapes():
            recording, _, _ = apply_profile(model.record(**shape), profile, npu2)
            for step in recording.steps:
                if not isinstance(step.op, MHA):
                    continue
                op = step.op.resolved(npu2)
                decode = op.seq_len == 1
                if not op.fused:
                    missed.add((decode, op.d))
                    continue
                assert op.split if decode else op.f32_scores, op
    assert missed == composed
