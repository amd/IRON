# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The placer's verdicts the tuner keeps (``autotune.refusal``): each is
read back only for the recipe it was placed for, built with the same tools
for the same device.
"""

import hashlib

from iron.common.design import OperatorDesign
from iron.operators import ElementwiseAdd
from iron.tune.autotune import FIT_CACHE, refusal


def test_a_verdict_kept_for_other_tools_is_not_read(npu2):
    """A refusal kept under the recipe alone, as one placed with an older
    placer or for another device would be, is not this build's verdict:
    the placer runs again and keeps its own beside it.
    """
    add = ElementwiseAdd(size=8192, tile_size=256, num_aie_columns=1)
    compilable = OperatorDesign(add.resolved()).compilable()
    recipe, tools = compilable.recipe_hash, compilable.artifact_hash
    stale = FIT_CACHE / hashlib.sha256(recipe.encode()).hexdigest()[:24]
    own = FIT_CACHE / hashlib.sha256((recipe + tools).encode()).hexdigest()[:24]
    own.unlink(missing_ok=True)
    stale.parent.mkdir(parents=True, exist_ok=True)
    stale.write_text("refused: placed by another toolchain")
    try:
        assert refusal(add) is None
        assert own.read_text() == "fits"
        assert refusal(add) is None
    finally:
        stale.unlink()
