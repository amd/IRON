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

    def pack(self, values, scales):
        """Quantize ``values`` (bf16, ``size``) by ``scales`` (bf16, one per
        ``group_size``, zero point 0) into the kernel's packed uint8 layout;
        the inverse of :meth:`reference`. Values are rounded half to even
        and clipped to the int4 range, as ``torch.quantize_per_channel`` does.
        """
        tile, group = self.ov.tile_size, self.ov.group_size
        if tile is None:
            raise ValueError("Dequant.pack needs tile_size (tune the overlay)")
        n_tiles, groups = self.size // tile, tile // group
        v = values.reshape(n_tiles, groups, group).to(torch.float32)
        s = scales.reshape(n_tiles, groups, 1).to(torch.float32)
        q = torch.round(v / s).clamp(0, 15).to(torch.uint8)
        nibbles = (q[..., 0::2] | (q[..., 1::2] << 4)).reshape(n_tiles, tile // 2)
        scale_bytes = scales.reshape(n_tiles, groups).contiguous().view(torch.uint8)
        return torch.cat([nibbles, scale_bytes.reshape(n_tiles, -1)], dim=1).reshape(-1)

    def reference(self, x):
        """CPU reference: int4 values times their group's bf16 scale, in f32.

        The packed tile is ``tile_size // 2`` bytes of nibbles (element ``2k``
        in the low nibble of byte ``k``, ``2k + 1`` in the high) followed by
        one little-endian bf16 scale per ``group_size`` values; the zero point
        is 0. Results are exact in f32, as ``torch.dequantize`` gives them.
        """
        tile, group = self.ov.tile_size, self.ov.group_size
        if tile is None:
            raise ValueError("Dequant.reference needs tile_size (tune the overlay)")
        n_tiles, groups = self.size // tile, tile // group
        packed = x.reshape(n_tiles, tile // 2 + groups * 2)
        nibbles = packed[:, : tile // 2].to(torch.int32)
        q = torch.stack([nibbles & 0xF, nibbles >> 4], dim=-1).reshape(
            n_tiles, groups, group
        )
        scales = packed[:, tile // 2 :].reshape(n_tiles, groups, 2).contiguous()
        scales = scales.view(torch.bfloat16).to(torch.float32)  # (n_tiles, groups, 1)
        return (q.to(torch.float32) * scales).reshape(self.size)
