#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""ResNet-50 from its released checkpoint on the NPU: the logits its graph's
own reference gives, for a drawn image.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.resnet.model import ResNet, ResNetConfig
from iron.lm import Checkpoint
from iron.lm.testing import assert_close, require, weights_dir

WEIGHTS = weights_dir("resnet-50") / "model.safetensors"


@pytest.mark.supported_devices("npu2")
def test_resnet_50_classifies_as_its_graph_reference():
    require(WEIGHTS, staged=False)
    model = ResNet(ResNetConfig.from_checkpoint(WEIGHTS), Checkpoint(WEIGHTS).tree())
    S = model.config.image_size
    image = np.random.default_rng(0).standard_normal((S, S, 3)).astype(bfloat16)
    x = model.inputs(image)
    want = model.reference(x)
    model.compile(image=(x.shape, bfloat16))
    got = np.array(model(aie_utils.DEFAULT_TENSOR_CLASS(x)).numpy())
    assert_close(got, want)
