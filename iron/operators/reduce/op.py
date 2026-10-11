# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron.kernels import reduce

from iron.common import In, Out, Rowwise, param

# A reduction writes one value into a DMA-aligned output tile; bf16's is two
# elements (``_min_dma_aligned_elems``, mlir-aie's), the only dtype this
# operator's callers use. Elementwise's resolve()/compatible() key every
# column-fitting and divisibility check off ``tile_size`` meaning the
# *output* row's width (as Magnitude's narrowing Rowwise already does, its
# own ``width`` the wider input row); this operator's input row is ``window``.
OUT_WIDTH = 2


class Reduce(Rowwise):
    """``rows`` rows of ``window`` elements in, each row's ``op`` (sum, min
    or max) out: element 0 of a 2-element row, the other undefined (the
    kernel writes fewer elements than it reads, like ``Magnitude``'s).
    """

    op: str = param(default="max", array=True)
    window: int = param()
    tile_size: int = param(default=OUT_WIDTH)

    x = In(
        Rowwise.rows,
        window,
        tile=(window,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )
    y = Out(
        Rowwise.rows,
        tile_size,
        tile=(tile_size,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )

    def validate(self) -> None:
        if self.tile_size != OUT_WIDTH:
            raise ValueError(f"Reduce: tile_size is fixed at {OUT_WIDTH}")
        if self.window % 2:
            raise ValueError(
                f"Reduce: window ({self.window}) is odd; a bf16 DMA transfer "
                f"must be a whole number of 4-byte (2-element) units. Pad the "
                f"window with an element that cannot win op's reduction "
                f"(-inf-equivalent for max, +inf-equivalent for min, 0 for add)"
            )

    def kernel(self):
        factory = {"add": reduce.reduce_add, "min": reduce.reduce_min, "max": reduce.reduce_max}[
            self.op
        ]
        return factory(self.window, self.x.dtype, vectorized=self.window % 32 == 0)

    def reference(self, x):
        """Element 0 of each output row, the kernel's one defined lane,
        repeated into element 1 (undefined on the device; a caller never
        reads it).
        """
        ref = {
            "add": reduce.reduce_add_ref,
            "min": reduce.reduce_min_ref,
            "max": reduce.reduce_max_ref,
        }[self.op]
        value = ref(x.reshape(-1, self.window))  # (rows, 1)
        return np.broadcast_to(value, (value.shape[0], OUT_WIDTH))
