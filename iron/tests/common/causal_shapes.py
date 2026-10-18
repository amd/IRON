# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``CausalLM.shapes()``'s one-list convention (``Model``'s own):
the decode step's (none) then the prompt chunk's token ids. Device-free.
"""

import numpy as np

from iron.applications.llama.model import Llama
from iron.tests.common.llama_model import SMALL, checkpoint


def test_shapes_is_the_decode_step_then_the_prompt_chunk():
    weights = checkpoint(SMALL).tree("unread")
    model = Llama(SMALL, weights)
    decode, prompt = model.shapes()
    assert decode == {}
    assert prompt == {"ids": ((SMALL.prefill_chunk,), np.int32)}
