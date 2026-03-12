# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

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

# Maps XRTTensor dtype objects/types to their torch equivalents.
# Both np.dtype(...) objects and bare ml_dtypes types are included because
# xrttensor.dtype may return either form depending on how the tensor was created.
_XRT_TO_TORCH_DTYPE: dict = {
    np.dtype("float32"): torch.float32,
    np.dtype("int32"): torch.int32,
    np.dtype("int16"): torch.int16,
    np.dtype("int8"): torch.int8,
    np.dtype("uint8"): torch.uint8,
    np.dtype("float16"): torch.float16,
    np.dtype(bfloat16): torch.bfloat16,
    bfloat16: torch.bfloat16,
}


def xrt_to_torch(xrttensor) -> torch.Tensor:
    """
    Convert an XRTTensor (or compatible object with buffer_object()) to a Torch tensor,
    supporting bfloat16.

    Note: calls xrttensor.to("cpu") as a side effect to ensure the buffer is
    synchronized to host memory before reading.
    """
    torch_dtype = _XRT_TO_TORCH_DTYPE.get(xrttensor.dtype)
    if torch_dtype is None:
        raise ValueError(f"Unsupported dtype: {xrttensor.dtype}")

    xrttensor.to("cpu")
    bo = xrttensor.buffer_object()
    mem = bo.map()
    t = torch.frombuffer(mem, dtype=torch_dtype)
    return t.reshape(xrttensor.shape)
