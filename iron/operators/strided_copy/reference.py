# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import torch

from iron.common.test_utils import torch_dtype_map


def _pad_to_4d(sizes, strides):
    """design.py pads access patterns to 4D before building the taps; the reference
    has to pad identically or the per-channel split lands on a different dimension."""
    return (
        [1] * (4 - len(sizes)) + list(sizes),
        [0] * (4 - len(strides)) + list(strides),
    )


def _tap_offsets(sizes, strides, offset):
    """Flat element offsets a TensorAccessPattern visits, in issue order."""
    grids = np.meshgrid(*[np.arange(s) for s in sizes], indexing="ij")
    flat = np.full(grids[0].shape, offset, dtype=np.int64)
    for grid, stride in zip(grids, strides):
        flat = flat + grid * stride
    return flat.reshape(-1)


def _channel_offsets(sizes, strides, offset, num_aie_channels):
    sizes, strides = _pad_to_4d(sizes, strides)
    highest = max(idx for idx, sz in enumerate(sizes) if sz >= 1)
    per_channel = sizes[highest] // num_aie_channels
    split = sizes[:highest] + [per_channel] + sizes[highest + 1 :]
    return [
        _tap_offsets(split, strides, offset + c * per_channel * strides[highest])
        for c in range(num_aie_channels)
    ]


def reference(
    input_flat,
    input_sizes,
    input_strides,
    input_offset,
    output_buffer_size,
    output_sizes,
    output_strides,
    output_offset,
    num_aie_channels=1,
    input_offset_addend=0,
    output_offset_addend=0,
):
    """Gather by the input tap, scatter by the output tap, one channel at a time.

    The addends are the *_offset_parameter values. They are element counts, not byte
    offsets: the firmware multiplies the scratchpad word by the element size before
    adding it into the BD address register.
    """
    src = _channel_offsets(
        input_sizes, input_strides, input_offset + input_offset_addend, num_aie_channels
    )
    dst = _channel_offsets(
        output_sizes,
        output_strides,
        output_offset + output_offset_addend,
        num_aie_channels,
    )

    out = torch.zeros(int(output_buffer_size), dtype=input_flat.dtype)
    for src_c, dst_c in zip(src, dst):
        if len(src_c) != len(dst_c):
            raise ValueError(
                f"tap element counts differ ({len(src_c)} vs {len(dst_c)}); "
                "the input and output access patterns must move the same number "
                "of elements"
            )
        out[dst_c] = input_flat[src_c]
    return out


def generate_golden_reference(
    input_buffer_size,
    input_sizes,
    input_strides,
    input_offset,
    output_buffer_size,
    output_sizes,
    output_strides,
    output_offset,
    num_aie_channels=1,
    input_offset_addend=0,
    output_offset_addend=0,
    dtype="bf16",
    seed=42,
):
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = (
        torch.rand(int(input_buffer_size), dtype=torch_dtype_map[dtype]) * val_range
    )
    output_tensor = reference(
        input_tensor,
        input_sizes,
        input_strides,
        input_offset,
        output_buffer_size,
        output_sizes,
        output_strides,
        output_offset,
        num_aie_channels=num_aie_channels,
        input_offset_addend=input_offset_addend,
        output_offset_addend=output_offset_addend,
    )
    return {"input": input_tensor, "output": output_tensor}
