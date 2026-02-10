# Copyright (c) Sebastian Raschka under Apache License 2.0.
# Source for "Build a Large Language Model From Scratch"
#   - https://www.manning.com/books/build-a-large-language-model-from-scratch
# Code: https://github.com/rasbt/LLMs-from-scratch/blob/main/ch05/07_gpt_to_llama/standalone-llama32.ipynb
#
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import time
import torch
import numpy as np
from ml_dtypes import bfloat16

torch_dtype_map = {
    "bf16": torch.bfloat16,
    "f32": torch.float32,
    "i8": torch.int8,
    "ui8": torch.uint8,
    "i16": torch.int16,
    "i32": torch.int32,
}


def xrt_to_torch(xrttensor) -> torch.Tensor:
    """
    Convert an XRTTensor (or compatible object with buffer_object()) to a Torch tensor
    without intermediate numpy array creation, supporting bfloat16.
    """
    dtype_map = {
        np.dtype("float32"): torch.float32,
        np.dtype("int32"): torch.int32,
        np.dtype("int16"): torch.int16,
        np.dtype("int8"): torch.int8,
        np.dtype("uint8"): torch.uint8,
        np.dtype("float16"): torch.float16,
        np.dtype(bfloat16): torch.bfloat16,
        bfloat16: torch.bfloat16,
    }

    torch_dtype = dtype_map.get(xrttensor.dtype)
    if torch_dtype is None:
        raise ValueError(f"Unsupported dtype: {xrttensor.dtype}")

    xrttensor.to("cpu")
    bo = xrttensor.buffer_object()
    mem = bo.map()
    t = torch.frombuffer(mem, dtype=torch_dtype)
    return t.reshape(xrttensor.shape)
