# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Qwen3-MoE's graph against Hugging Face's Qwen3MoE in float32 over the
same random weights at a toy shape, its logits recorded in ``goldens/``,
device-free: the shared decoder's tests (``Decoder``).
"""

import dataclasses

import pytest

from iron.applications.qwen3_moe.model import Qwen3Moe, Qwen3MoeConfig
from iron.tests.support.llama_reference import Decoder
from iron.tests.support.qwen3_moe import TOY, names


class TestQwen3Moe(Decoder):
    model, config, model_type, name = Qwen3Moe, TOY, "qwen3_moe", "toy"
    recorded = dict(num_experts=64)
    # One whose bf16 router picks the experts float32 does at every step.
    seed = 0

    @classmethod
    def names(cls):
        assert isinstance(cls.config, Qwen3MoeConfig), "Qwen3-MoE's shape"
        return names(cls.config)


@pytest.mark.parametrize(
    "change",
    [
        dict(norm_topk_prob=False),
        dict(decoder_sparse_step=2),
        dict(mlp_only_layers=(1,)),
    ],
)
def test_unnormalized_weights_or_a_dense_layer_is_refused(change):
    with pytest.raises(ValueError, match="Qwen3MoeConfig"):
        dataclasses.replace(TOY, **change)
