# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from dataclasses import field

import numpy as np
import torch
from ml_dtypes import bfloat16

from iron.common.declare import (
    Incompatible,
    In,
    Operator,
    Out,
    Overlay,
    Resident,
    StreamIn,
    StreamOut,
    Untunable,
    dim,
    operator,
    tunable,
)


@operator
class DequantOverlay(Overlay):
    """The array for int4 -> bf16 dequantization: one core per (column, channel).

    A core takes ``per_tile`` values as ``in_tile`` packed bytes (two 4-bit
    values per byte plus a bf16 scale and zero point per ``group_size``) and
    produces ``per_tile`` bf16 values.
    """

    # None: every column of the device, one channel each, 4096-value tiles.
    num_aie_columns: int | None = tunable(None)
    num_channels: int = tunable(1)
    tile_size: int | None = tunable(None)
    group_size: int = field(default=32, repr=False)
    # Filled by tuning: the largest tile 64 KB of L1 holds, and its packed size.
    per_tile: int | None = tunable(None, repr=False)
    in_tile: int | None = tunable(None, repr=False)

    x = StreamIn(in_tile, dtype=np.uint8, per=(num_aie_columns, num_channels))
    y = StreamOut(per_tile, per=(num_aie_columns, num_channels))
    count = Resident(np.int32)

    def tuning(self, dev) -> "DequantOverlay":
        from iron.common.utils import device_columns

        cols = self.num_aie_columns
        if cols is None:
            if dev is None:
                raise Untunable("num_aie_columns defaults from the device; none given")
            cols = min(device_columns(dev), 16 // self.num_channels)
        tile_size = 4096 if self.tile_size is None else self.tile_size
        total_cores = cols * self.num_channels
        if total_cores > 16:
            raise Untunable(f"total cores ({total_cores}) must be <= 16")
        per_tile = min(tile_size, 16384)
        return dataclasses.replace(
            self,
            num_aie_columns=cols,
            tile_size=tile_size,
            per_tile=per_tile,
            in_tile=(per_tile // 2) + (per_tile // self.group_size) * 2,
        )

    def design(self, target) -> list:
        from aie.iron import ObjectFifo, Worker
        from aie.iron.controlflow import range_

        in_tile_ty, out_tile_ty = self.x.tile, self.y.tile
        cols, chans = self.num_aie_columns, self.num_channels
        depth = 1 if self.tile_size > 8192 else 2

        kernel = target.kernel(
            "expand_uint4_to_bfloat16",
            [in_tile_ty, out_tile_ty],
            source=target.kernels_dir / "generic" / "expand.cc",
            compile_flags=[
                f"-DTILE_SIZE={self.tile_size}",
                f"-DGROUP_SIZE={self.group_size}",
            ],
        )
        of_ins = [
            ObjectFifo(in_tile_ty, name=f"in1_{i}_{j}", depth=depth)
            for i in range(cols)
            for j in range(chans)
        ]
        of_outs = [
            ObjectFifo(out_tile_ty, name=f"out_{i}_{j}", depth=depth)
            for i in range(cols)
            for j in range(chans)
        ]
        i32 = np.ndarray[(1,), np.dtype[np.int32]]
        counts = [target.rtp(i32, name=f"count_{k}") for k in range(cols * chans)]
        barriers = [target.barrier() for _ in range(cols * chans)]

        def core_body(of_in, of_out, dequant, count, barrier):
            barrier.wait_for_value(1)
            n = count[0]
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                dequant(elem_in, elem_out)
                of_in.release(1)
                of_out.release(1)

        workers = [
            Worker(
                core_body,
                [of_ins[k].cons(), of_outs[k].prod(), kernel, counts[k], barriers[k]],
            )
            for k in range(cols * chans)
        ]
        for k in range(cols * chans):
            self.x[k].bind(of_ins[k].prod())
            self.y[k].bind(of_outs[k].cons())
        self.count.bind(counts)
        return workers


@operator
class Dequant(Operator[DequantOverlay]):
    """AIE-accelerated dequantization operator"""

    size: int = dim()
    # The packed input's length: two 4-bit values per byte plus a bf16 scale
    # and zero point per group. Derived from size unless given.
    packed: int | None = dim(None, repr=False)

    x = In(packed, dtype=np.uint8, to=DequantOverlay.x)
    y = Out(size, from_=DequantOverlay.y)

    def validate(self) -> None:
        expected = (self.size // 2) + (self.size // self.ov.group_size) * 2
        if self.packed is None:
            self.packed = expected
        elif self.packed != expected:
            raise ValueError(
                f"packed={self.packed} does not match size={self.size} with "
                f"group_size={self.ov.group_size} (expected {expected})"
            )

    @property
    def input_size(self) -> int:
        return self.packed

    @property
    def output_size(self) -> int:
        return self.size

    def compatible(self) -> None:
        ov = self.ov
        total_cores = ov.num_aie_columns * ov.num_channels
        if self.size % total_cores:
            raise Incompatible(
                f"size ({self.size}) must be divisible by total cores ({total_cores})"
            )
        if (self.size // total_cores) % ov.per_tile:
            raise Incompatible(
                f"size ({self.size}) leaves each core {self.size // total_cores} "
                f"elements, not a multiple of the {ov.per_tile}-element tile"
            )

    def residents(self) -> dict[str, int]:
        ov = self.ov
        return {
            "count": self.size // (ov.num_aie_columns * ov.num_channels) // ov.per_tile
        }


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def generate_golden_reference(input_length, tile_size, group_size):
    torch.manual_seed(42)

    if input_length % tile_size != 0:
        raise ValueError("Input length must be a multiple of tile size.")
    if tile_size % group_size != 0:
        raise ValueError("Tile size must be a multiple of group size.")

    num_tiles = input_length // tile_size
    num_scale_factors = tile_size // group_size
    scale_size = num_scale_factors * 2  # Total bytes (uint8 elements) for scale factors
    per_tile_size = tile_size // 2
    per_tile_bytes = (
        scale_size + per_tile_size
    )  # Total bytes (uint8 elements) after processing each tile
    val_range = 3.75  # Values in [0, 3.75)

    # Generate golden output with uniform distribution between 0 and val_range
    # This output will be quantized to be used as the input
    A = (
        torch.rand(num_tiles * num_scale_factors, group_size, dtype=torch.bfloat16)
        * val_range
    )

    # Generate scale factors in [0.25, 1) for each tile
    # The quantized values will thus be within [0,15], which is the range of int4
    # Zero points for each tile are fixed to 0 since the kernel only uses the scale factors
    r1, r2 = 1 / val_range, 1
    scales = r1 + (r2 - r1) * torch.rand(
        num_tiles * num_scale_factors, dtype=torch.bfloat16
    )
    zero_points = torch.zeros(num_tiles * num_scale_factors, dtype=torch.bfloat16)

    A = torch.quantize_per_channel(
        A.to(torch.float32),
        scales=scales.to(torch.float32),
        zero_points=zero_points.to(torch.float32),
        axis=0,
        dtype=torch.quint8,
    )
    B = torch.dequantize(A)

    # Convert A from a quantized tensor type to regular tensor type for data packing
    # We do the data packing here instead of the host to show how the data would need to be
    # manipulated from a PyTorch standpoint in order to use the dequant kernel.
    A = A.int_repr()

    # Concatenate the bottom four bits of every two elements across the tiles in A to generate
    # an 8-bit value (little endian order). This is because there's no native 4-bit datatype in C++.
    # At the end of each tile, concatenate the bf16 scale factor, which comes out to two int8 values.
    A_concat = torch.zeros(num_tiles, per_tile_bytes, dtype=torch.uint8)
    for i in range(num_tiles):
        for j in range(num_scale_factors):
            for k in range(group_size // 2):
                A_concat[i, j * (group_size // 2) + k] = torch.bitwise_or(
                    torch.bitwise_and(A[i * num_scale_factors + j, 2 * k], 0x0F),
                    torch.bitwise_and(A[i * num_scale_factors + j, 2 * k + 1], 0x0F)
                    * 2**4,
                )
        for j in range(num_scale_factors):
            A_concat[i, per_tile_size + 2 * j] = torch.bitwise_and(
                scales[i * num_scale_factors + j].view(torch.uint16), 0xFF
            )
            # Extract high byte (bits 15-8) of the bfloat16 bit pattern.
            # View as int16 (same width), promote to int32 for bitwise_right_shift
            # support, shift right 8, then mask to 8 bits. The & 0xFF also
            # handles sign-extension from int32 arithmetic right shift.
            A_concat[i, per_tile_size + 2 * j + 1] = torch.bitwise_and(
                scales[i * num_scale_factors + j].view(torch.int16).to(torch.int32)
                >> 8,
                0xFF,
            )

    return {
        "input": A_concat,
        "output": B,
    }
