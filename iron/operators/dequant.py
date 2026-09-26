# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from typing import ClassVar

import numpy as np
from aie.iron.kernels import datamovement
from aie.iron.kernels.datamovement import expand_ref
from ml_dtypes import bfloat16

from iron.common import In, UnaryElementwise, Unresolvable, auto, param
from iron.common.testing import Testing, channeled_unary_cases


def _packed(op):
    """Values in [0, 3.75) with scales in [1/3.75, 1) keep every quantized
    value inside int4's [0, 15]; the input is their packed form.
    """
    rng = np.random.default_rng(42)
    values = (rng.random(op.size) * 3.75).astype(bfloat16)
    scales = (1 / 3.75 + (1 - 1 / 3.75) * rng.random(op.size // op.group_size)).astype(
        bfloat16
    )
    return dict(x=op.pack(values, scales))


class Dequant(UnaryElementwise):
    """AIE-accelerated int4 -> bf16 dequantization: the elementwise design
    over a packed input.

    A core takes ``tile_size`` values as ``in_tile`` packed bytes (two 4-bit
    values per byte plus a bf16 scale and zero point per ``group_size``) and
    produces ``tile_size`` bf16 values, so its two streams carry different
    tiles.
    """

    test = Testing(channeled_unary_cases(group_size=32), draw=_packed)

    group_size: int = param(default=32, repr=False, array=True)
    # The packed input's length: two 4-bit values per byte plus a bf16 scale
    # and zero point per group.
    packed: int = param(
        default=lambda op: op.size // 2 + (op.size // op.group_size) * 2, repr=False
    )
    # The packed size of one line; filled by resolve from ``tile_size``.
    in_tile: int = auto(repr=False)

    default_tile: ClassVar[int] = 4096
    tile_cap: ClassVar[int] = 16384

    x = In(
        packed,
        dtype=np.uint8,
        tile=(in_tile,),
        per=(UnaryElementwise.num_aie_columns, UnaryElementwise.num_channels),
    )

    def validate(self) -> None:
        self.check_derived("packed")
        if self.size % self.group_size:
            raise ValueError(
                f"size={self.size} is not whole groups of {self.group_size}"
            )

    def resolve(self, dev):
        op = super().resolve(dev)
        if op.tile_size % self.group_size:
            raise Unresolvable(
                f"tile_size={op.tile_size} is not whole groups of {self.group_size}"
            )
        packed = (op.tile_size // 2) + (op.tile_size // self.group_size) * 2
        return dataclasses.replace(op, in_tile=packed)

    def kernel(self, target):
        return datamovement.expand(self.tile_size, self.group_size)

    def kernel_call(self, kernel, elem_in, elem_out) -> None:
        # The line length is a compile flag, not an argument.
        kernel(elem_in, elem_out)

    def pack(self, values, scales):
        """Quantize ``values`` (bf16, ``size``) by ``scales`` (bf16, one per
        ``group_size``, zero point 0) into the kernel's packed uint8 layout;
        the inverse of :meth:`reference`. Values are rounded half to even
        and clipped to the int4 range.
        """
        tile, group = self.tile_size, self.group_size
        if tile is None:
            raise ValueError("Dequant.pack needs tile_size (resolve first)")
        n_tiles, groups = self.size // tile, tile // group
        v = values.reshape(n_tiles, groups, group).astype(np.float32)
        s = scales.reshape(n_tiles, groups, 1).astype(np.float32)
        # np.round is round-half-to-even, as torch.round is.
        q = np.clip(np.round(v / s), 0, 15).astype(np.uint8)
        nibbles = (q[..., 0::2] | (q[..., 1::2] << 4)).reshape(n_tiles, tile // 2)
        scale_bytes = np.ascontiguousarray(scales.reshape(n_tiles, groups)).view(
            np.uint8
        )
        return np.concatenate(
            [nibbles, scale_bytes.reshape(n_tiles, -1)], axis=1
        ).reshape(-1)

    def reference(self, x):
        """CPU reference: int4 values times their group's bf16 scale, in f32.

        The packed tile is ``tile_size // 2`` bytes of nibbles (element ``2k``
        in the low nibble of byte ``k``, ``2k + 1`` in the high) followed by
        one little-endian bf16 scale per ``group_size`` values; the zero point
        is 0. Results are exact in f32.
        """
        tile, group = self.tile_size, self.group_size
        if tile is None:
            raise ValueError("Dequant.reference needs tile_size (resolve first)")
        tiles = x.reshape(self.size // tile, -1)
        return expand_ref(tiles, tile_size=tile, group_size=group).reshape(self.size)
