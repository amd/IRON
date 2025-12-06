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


def torch_to_numpy(tensor: torch.Tensor) -> np.ndarray:
    # Detach (to drop grad) and ensure on CPU
    t = tensor.detach()
    if t.device.type != 'cpu':
        t = t.cpu()
    # Ensure contiguous for safe view operations
    if not t.is_contiguous():
        t = t.contiguous()

    if t.dtype == torch.bfloat16:
        # Zero-copy reinterpret: view the same memory as uint16, then as NumPy bfloat16
        # This avoids numeric conversion and extra passes over memory.
        u16_np = t.view(torch.uint16).numpy()        # shares memory, zero-copy
        return u16_np.view(np.dtype('bfloat16'))     # reinterpret, zero-copy

    # For supported dtypes, this is already zero-copy
    return t.numpy()


def numpy_to_torch(array: np.ndarray) -> torch.Tensor:
    # Ensure contiguous to let from_numpy create a view
    if not array.flags['C_CONTIGUOUS']:
        array = np.ascontiguousarray(array)

    if array.dtype == np.dtype('bfloat16'):
        # reinterpret the same memory as uint16, then view as torch.bfloat16
        t_u16 = torch.from_numpy(array.view(np.uint16))  # zero-copy
        return t_u16.view(torch.bfloat16)                # view, zero-copy

    # For supported dtypes, from_numpy is already zero-copy
    return torch.from_numpy(array)
