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
    if tensor.dtype == torch.bfloat16:
        float_arr = tensor.float().detach().cpu().numpy()
        return float_arr.astype(bfloat16)
    return tensor.detach().cpu().numpy()


def numpy_to_torch(array: np.ndarray) -> torch.Tensor:
    device = torch.device("cpu")
    if array.dtype == bfloat16:
        return torch.from_numpy(array.astype(np.float32)).to(torch.bfloat16).to(device)
    return torch.from_numpy(array).to(device)
