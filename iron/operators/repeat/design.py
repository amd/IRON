# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Repeat interleave
"""

import numpy as np

from aie.dialects.aiex import TensorAccessPattern
from aie.iron import ObjectFifo, Program, Runtime, TaskGroup

from iron.common.shim_bd import SHIM_MAX_WRAP, shim_gran_elems, split_run


def repeat(dev, dtype, rows, cols, repeat, transfer_size=None):
    elem_bytes = np.dtype(dtype).itemsize
    dtype = np.dtype[dtype]

    # One BD-split invariant, shared with gemv: the chunk length is the innermost dim and
    # must be <= 1023 (10-bit wrap) and a whole number of 32-bit words; the chunk count is
    # the next dim out, same wrap field. split_run maximises the inner length, which is what
    # keeps the innermost DMA run long. An odd cols has only odd divisors, so no split of it
    # is ever word-aligned at bf16; that is reported here rather than left to the BD verifier.
    granule = shim_gran_elems(dtype)
    split = split_run(cols, gran=granule)
    if split is None:
        raise ValueError(
            f"Cannot split cols={cols} at {elem_bytes} bytes/element: need a divisor d "
            f"with cols//d <= {SHIM_MAX_WRAP}, d <= {SHIM_MAX_WRAP}, and cols//d a multiple "
            f"of {granule} ({granule} elements = one 32-bit word). "
            f"No divisor of {cols} satisfies all three."
        )
    cols_split, _chunk = split  # (count, length); sizes below put the length innermost

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
