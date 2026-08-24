# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Repeat interleave
"""

import numpy as np

from aie.dialects.aiex import TensorAccessPattern
from aie.iron import ObjectFifo, Program, Runtime, TaskGroup


def repeat(dev, dtype, rows, cols, repeat, transfer_size=None):
    dtype = np.dtype[dtype]

    # Try to work around hardware size limitations by breaking transfers into smaller chunks
    cols_split = 1
    if cols > 1023:
        for divisor in range(2, cols + 1):
            if cols % divisor == 0 and cols // divisor <= 1023:
                cols_split = divisor
                break
        else:
            raise ValueError(
                f"Cannot split cols={cols} into chunks <= 1023; hardware limits cols to not exceed 1023"
            )
    assert cols_split <= 1023, "cols is too large, can't split into smaller transfers"

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
        sizes=[repeat, rows, cols // cols_split, cols_split],
        strides=[0, cols, cols_split, 1],
    )

    output_tap = TensorAccessPattern(
        tensor_dims=(rows * repeat, cols),
        offset=0,
        sizes=[repeat, rows, cols // cols_split, cols_split],
        strides=[cols, cols * repeat, cols_split, 1],
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
