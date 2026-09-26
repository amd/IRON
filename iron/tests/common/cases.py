# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Construction cases for every declared operator, as keyword arguments.

One matrix, reused: the shapes each operator reads, varied over the shape
and dtype decisions it makes, with the tuning knobs at one valid value.
Every case constructs on a device-free host; ``iron/tests/toolchain/lowering.py``
runs the same table through the real lowering, to an instruction stream.
"""

import numpy as np
from ml_dtypes import bfloat16

from iron.common.tiling import Walk

# (module, class name, [kwargs, ...])
CASES = [
    # num_aie_columns is pinned everywhere it has a default, rather than left
    # to the operator: the defaults (AXPY's is 8) exceed the ShimDMA limit of
    # the narrow devices, so a snapshot that relied on them would record a
    # different shape per device width instead of a stable one.
    ("axpy", "AXPY", [dict(size=2048, tile_size=256, num_aie_columns=1)]),
    (
        "dequant",
        "Dequant",
        [dict(size=1024, num_aie_columns=1, num_channels=1, tile_size=256)],
    ),
    (
        "elementwise_add",
        "ElementwiseAdd",
        [dict(size=2048, tile_size=256, num_aie_columns=1)],
    ),
    (
        "elementwise_mul",
        "ElementwiseMul",
        [dict(size=2048, tile_size=256, num_aie_columns=1)],
    ),
    (
        "gelu",
        "GELU",
        [dict(size=1024, num_aie_columns=1, num_channels=1, tile_size=256)],
    ),
    (
        "gemm.op",
        "GEMM",
        [
            # M must be a multiple of 256 and N of 512.
            dict(M=256, K=64, N=512),
            # b_col_maj / c_col_maj transpose the declared shapes (GEMM's
            # select()).
            dict(M=256, K=64, N=512, b_col_maj=True),
            dict(M=256, K=64, N=512, c_col_maj=True),
            # f32 output at the default 64-tile overflows a core's memory; smaller tiles.
            dict(
                M=512,
                K=256,
                N=512,
                dtype_in=bfloat16,
                dtype_out=np.float32,
                tile_m=32,
                tile_k=32,
                tile_n=32,
            ),
        ],
    ),
    (
        "gemv.op",
        "GEMV",
        [
            dict(M=256, K=64),
            # num_batches > 1 prepends a batch dimension; == 1 must not.
            dict(M=256, K=64, num_batches=4),
        ],
    ),
    (
        "layer_norm",
        "LayerNorm",
        [dict(size=1024, num_aie_columns=1, num_channels=1, tile_size=256)],
    ),
    (
        "leaky_relu",
        "LeakyReLU",
        [dict(size=1024, num_aie_columns=1, num_channels=1, tile_size=256)],
    ),
    (
        "mem_copy",
        "MemCopy",
        [dict(size=1024, num_cores=1, num_channels=1, bypass=False, tile_size=256)],
    ),
    (
        "mha.op",
        "MHA",
        [
            # Left out, plain MHA; fewer KV heads is grouped-query, and
            # the two size the K/V buffers differently.
            dict(num_heads=8, seq_len=128, d=64),  # plain MHA: as many KV heads
            dict(num_heads=8, seq_len=128, d=64, num_KV_heads=2),
            # The projections' layout, (seq, heads, d): a head is a strided slice.
            dict(
                num_heads=8, seq_len=128, d=64, num_KV_heads=2, heads_interleaved=True
            ),
        ],
    ),
    (
        "relu",
        "ReLU",
        [dict(size=1024, num_aie_columns=1, num_channels=1, tile_size=256)],
    ),
    (
        "repeat",
        "Repeat",
        [
            dict(rows=8, cols=64, repeat=4),
            dict(rows=8, cols=64, repeat=4, dtype=np.int32),
        ],
    ),
    (
        "rms_norm",
        "RMSNorm",
        [dict(rows=4, num_aie_columns=1, num_channels=1, tile_size=256)],
    ),
    (
        "rms_norm",
        "WeightedRMSNorm",
        # The weight row sits between the input and the output.
        [dict(rows=4, num_aie_columns=1, num_channels=1, tile_size=256)],
    ),
    (
        "rope.op",
        "RoPE",
        [
            dict(rows=16, cols=64),
            # angle_rows is an independent parameter that merely defaults to
            # rows, so the angles buffer broadcasts. Without an explicit value
            # RoPE reads as "three buffers of one shape" and would be grouped
            # with the elementwise binaries, which it is not.
            dict(rows=32, cols=64, angle_rows=8),
        ],
    ),
    # mlir-aie's LUT activations need a tile of at least 1024.
    (
        "sigmoid",
        "Sigmoid",
        [dict(size=1024, num_aie_columns=1, num_channels=1, tile_size=1024)],
    ),
    ("silu", "SiLU", [dict(size=1024, num_aie_columns=1, tile_size=256)]),
    ("softmax", "Softmax", [dict(rows=16, cols=64)]),
    # SwiGLUDecode / SwiGLUPrefill are graph functions and SwiGLUPrefillStream
    # an OperatorSequence: none declares buffers of its own. Only the leaf
    # operator of that family does, the per-group stream operator, covered here.
    (
        "copy",
        "Copy",
        [
            dict(input_buffer_size=1024, output_buffer_size=1024),
            dict(input_buffer_size=1024, output_buffer_size=1024, dtype=np.float32),
            # Input and output buffer sizes are independent here, unlike every
            # other (in, out) operator: a gather of every other pair of a
            # 1024-element buffer into a 256-element one (a pair, because a
            # bf16 element is half the shim's 4-byte granule). Equal-size
            # cases alone would let a refactor that tied the output shape to
            # the input pass unnoticed. (The copy itself moves the same
            # element count both ways; the operator checks that at
            # construction.)
            dict(
                src=Walk(0, (128, 2), (8, 1)),
                input_buffer_size=1024,
                output_buffer_size=256,
            ),
            # A reorder of (seq, groups, d) into (groups, seq, d), the KV-cache
            # write of a prefill: a 3-D walk the copy legalizes for the shim.
            dict(
                src=Walk.permuted((128, 4, 64), (1, 0, 2)),
                dst=Walk.slice((4, 128, 64), (slice(None), slice(0, 128))),
                input_buffer_size=4 * 128 * 64,
                output_buffer_size=4 * 128 * 64,
                tile_size=1024,
            ),
        ],
    ),
    (
        "tanh",
        "Tanh",
        [dict(size=1024, num_aie_columns=1, num_channels=1, tile_size=1024)],
    ),
    (
        "transpose",
        "Transpose",
        [
            dict(M=64, N=64, num_aie_columns=1, num_channels=1, m=32, n=32, s=8),
            # Non-square, to pin that the output carries the transposed shape
            # (N, M) while the input keeps (M, N). A square-only case cannot
            # tell the two apart.
            dict(M=64, N=128, num_aie_columns=1, num_channels=1, m=32, n=32, s=8),
        ],
    ),
]
assert len({(m, c) for m, c, _ in CASES}) == len(CASES), "a class is listed twice"

_DTYPE_ALIASES = {bfloat16: "bfloat16"}


def dtype_name(dtype):
    """Canonical, stable name for a spec dtype.

    ``np.dtype(bfloat16).name`` round-trips, but going through ``np.dtype``
    first normalises the several forms an operator may hand back (a numpy
    scalar type, a ``np.dtype``, or ml_dtypes' ``bfloat16``) to one string, so
    a snapshot does not churn on an equivalent dtype written differently.
    """
    if dtype in _DTYPE_ALIASES:
        return _DTYPE_ALIASES[dtype]
    return np.dtype(dtype).name
