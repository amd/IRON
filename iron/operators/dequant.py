# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from dataclasses import field
from typing import ClassVar

import numpy as np

from iron.common import ChanneledUnaryOverlay
from iron.common.declare import (
    Incompatible,
    In,
    Operator,
    Out,
    StreamIn,
    dim,
    operator,
    tunable,
)
from iron.common.testing import Case, Testing, device_columns


@operator
class DequantOverlay(ChanneledUnaryOverlay):
    """The array for int4 -> bf16 dequantization: the shared elementwise design.

    A core takes ``line_size`` values as ``in_tile`` packed bytes (two 4-bit
    values per byte plus a bf16 scale and zero point per ``group_size``) and
    produces ``line_size`` bf16 values, so its two streams carry different
    tile types.
    """

    group_size: int = field(default=32, repr=False)
    # The packed size of one tile; filled by tuning beside ``line_size``.
    in_tile: int | None = tunable(None, repr=False)

    default_tile: ClassVar[int] = 4096
    tile_cap: ClassVar[int] = 16384

    x = StreamIn(
        in_tile,
        dtype=np.uint8,
        per=(
            ChanneledUnaryOverlay.num_aie_columns,
            ChanneledUnaryOverlay.num_channels,
        ),
    )

    def tuning(self, dev) -> "DequantOverlay":
        tuned = super().tuning(dev)
        packed = (tuned.line_size // 2) + (tuned.line_size // self.group_size) * 2
        return dataclasses.replace(tuned, in_tile=packed)

    def kernel(self, target):
        return target.kernel(
            "expand_uint4_to_bfloat16",
            [self.x.tile, self.y.tile],
            source=target.kernels_dir / "generic" / "expand.cc",
            compile_flags=[
                f"-DTILE_SIZE={self.tile_size}",
                f"-DGROUP_SIZE={self.group_size}",
            ],
        )

    def kernel_call(self, kernel, elem_in, elem_out) -> None:
        # The tile size is a compile flag, not an argument.
        kernel(elem_in, elem_out)


def _cases():
    out = []
    for size in [1024, 2048, 4096, 8192]:
        for cols in range(1, device_columns() + 1):
            for channels in (1, 2):
                tile_size = min(size // (cols * channels), 16384)
                if tile_size * cols * channels != size:
                    continue
                out.append(
                    Case(
                        dict(
                            size=size,
                            num_aie_columns=cols,
                            num_channels=channels,
                            tile_size=tile_size,
                            group_size=32,
                        ),
                        extensive=size != 2048,
                    )
                )
    return out


def _packed(op):
    """Values in [0, 3.75) with scales in [1/3.75, 1) keep every quantized
    value inside int4's [0, 15]; the input is their packed form."""
    import torch

    torch.manual_seed(42)
    values = torch.rand(op.size, dtype=torch.bfloat16) * 3.75
    scales = 1 / 3.75 + (1 - 1 / 3.75) * torch.rand(
        op.size // op.ov.group_size, dtype=torch.bfloat16
    )
    return dict(x=op.pack(values, scales))


@operator
class Dequant(Operator[DequantOverlay]):
    """AIE-accelerated dequantization operator"""

    test = Testing(_cases, rel_tol=0.01, draw=_packed)

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
        if (self.size // total_cores) % ov.line_size:
            raise Incompatible(
                f"size ({self.size}) leaves each core {self.size // total_cores} "
                f"elements, not a multiple of the {ov.line_size}-element tile"
            )

    def residents(self) -> dict[str, int]:
        ov = self.ov
        return {
            "count": self.size // (ov.num_aie_columns * ov.num_channels) // ov.line_size
        }

    def pack(self, values, scales):
        """Quantize ``values`` (bf16, ``size``) by ``scales`` (bf16, one per
        ``group_size``, zero point 0) into the kernel's packed uint8 layout;
        the inverse of :meth:`reference`. Values are rounded half to even
        and clipped to the int4 range, as ``torch.quantize_per_channel`` does.
        """
        import torch

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
        import torch

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
