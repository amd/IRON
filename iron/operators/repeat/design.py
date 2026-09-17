# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Repeat interleave
"""

import numpy as np

from aie.dialects.aiex import TensorAccessPattern
from aie.iron import ObjectFifo, Program, Runtime, TaskGroup


def repeat(dev, dtype, rows, cols, repeat, transfer_size=None):
    elem_bytes = np.dtype(dtype).itemsize
    dtype = np.dtype[dtype]

    # Split cols into cols_split chunks of cols // cols_split. This is required to
    # satisfy hardware constraints on BD dimensions. We must choose a split that
    # does not exceed the hardware register sizes:
    #   - the chunk length is the innermost dim: <= 1023 (10-bit wrap) AND a whole number
    #     of 32-bit words, since the BD's innermost size is denominated in words
    #   - the chunk count is the next dim out: <= 1023, the same wrap field
    # An odd cols has only odd divisors, so no split of it is ever word-aligned at bf16;
    # that is reported here rather than left to the BD verifier.
    granule = max(1, 4 // elem_bytes)  # elements per 32-bit word
    cols_split = None
    for divisor in range(1, cols + 1):
        if cols % divisor:
            continue
        chunk = cols // divisor
        if chunk <= 1023 and divisor <= 1023 and chunk % granule == 0:
            cols_split = divisor
            break
    if cols_split is None:
        raise ValueError(
            f"Cannot split cols={cols} at {elem_bytes} bytes/element: need a divisor d "
            f"with cols//d <= 1023, d <= 1023, and cols//d a multiple of {granule} "
            f"({granule} elements = one 32-bit word). No divisor of {cols} satisfies all three."
        )

    if transfer_size is None:
        transfer_size = cols

    inp_ty = np.ndarray[
        (rows, cols),
        dtype,
    ]
    out_ty = np.ndarray[
        (rows * repeat, cols),
        dtype,
    ]
    transfer_ty = np.ndarray[
        (transfer_size,),
        dtype,
    ]

    input_tap = TensorAccessPattern(
        tensor_dims=(rows, cols),
        offset=0,
        # The chunk LENGTH is innermost so the contiguous run is the innermost dim; the
        # chunk COUNT sits outside it. Swapping these two produces the same address
        # sequence, but putting the count innermost makes the unsplit case (cols_split
        # == 1) a 1-element innermost dim, which is not a whole 32-bit word for any
        # sub-word dtype and is rejected by the BD verifier.
        sizes=[repeat, rows, cols_split, cols // cols_split],
        strides=[0, cols, cols // cols_split, 1],
    )

    output_tap = TensorAccessPattern(
        tensor_dims=(rows * repeat, cols),
        offset=0,
        sizes=[repeat, rows, cols_split, cols // cols_split],
        strides=[cols, cols * repeat, cols // cols_split, 1],
    )

    # Use smaller FIFOs for the transfer amount
    fifo_in = ObjectFifo(transfer_ty, name="fifo_in", depth=2)
    fifo_out = fifo_in.cons().forward(name="fifo_out", depth=2)

    def sequence(inp, out, fifo_in_prod, fifo_out_cons):
        tg = TaskGroup()
        fifo_in_prod.fill(inp, input_tap, group=tg)
        fifo_out_cons.drain(out, output_tap, group=tg, wait=True)
        tg.finish()

    rt = Runtime(
        sequence,
        [
            inp_ty,
            out_ty,
            fifo_in.prod(),
            fifo_out.cons(),
        ],
    )
    return Program(dev, rt).resolve_program()
