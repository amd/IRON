# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Construction cases for every operator that declares an arg spec.

Kept apart from the test that consumes them so the same matrix can be reused:
the point of this data is to pin ``get_arg_spec()`` across the refactor that
moves specs out of ``op.py`` and into a shape function on the operator itself.
A case is only useful here if it exercises a *shape or dtype* decision, so the
matrix varies the dimensions and dtypes each operator reads and ignores the
knobs it does not (tiling, channel counts, scheduling) beyond one valid value.

Every case must construct on a device-free host -- no ``XRTTensor``, no
``pyxrt`` -- which is what lets this run as the equivalence gate anywhere.
"""

import numpy as np
from ml_dtypes import bfloat16

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
        "gemm",
        "GEMM",
        [
            # M must be a multiple of 256 and N of 512.
            dict(M=256, K=64, N=512),
            # b_col_maj / c_col_maj transpose the declared shapes; they are the
            # reason a shape function has to stay ordinary Python.
            dict(M=256, K=64, N=512, b_col_maj=True),
            dict(M=256, K=64, N=512, c_col_maj=True),
            dict(M=512, K=256, N=512, dtype_in="bf16", dtype_out="f32"),
        ],
    ),
    (
        "gemv",
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
        "mha",
        "MHA",
        [
            # num_KV_heads == 0 means plain MHA; non-zero is grouped-query, and
            # the two size the K/V buffers differently.
            dict(num_heads=8, seq_len=128, d=64, num_KV_heads=0),
            dict(num_heads=8, seq_len=128, d=64, num_KV_heads=2),
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
        [dict(size=1024, num_aie_columns=1, num_channels=1, tile_size=256)],
    ),
    (
        "rms_norm",
        "WeightedRMSNorm",
        # The weight row sits between the input and the output.
        [dict(size=1024, num_aie_columns=1, num_channels=1, tile_size=256)],
    ),
    (
        "rope",
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
    (
        "sigmoid",
        "Sigmoid",
        [dict(size=1024, num_aie_columns=1, num_channels=1, tile_size=256)],
    ),
    ("silu", "SiLU", [dict(size=1024, num_aie_columns=1, tile_size=256)]),
    ("softmax", "Softmax", [dict(rows=16, cols=64)]),
    # SwiGLUDecode / SwiGLUPrefill / SwiGLUPrefillStream are deliberately absent:
    # all three are OperatorSequence subclasses, and OperatorSequence raises
    # from get_arg_spec() ("does not expose a unified arg spec; use
    # get_layout_for_buffer()"). Only the leaf operator of that family declares
    # one -- the per-group stream operator, covered here.
    (
        "swiglu_prefill_stream",
        "_SwiGLUStreamGroup",
        [
            dict(
                seq_len=128,
                embedding_dim=2048,
                hidden_dim=8192,
                k=1,
                group_index=0,
            )
        ],
    ),
    (
        "strided_copy",
        "StridedCopy",
        [
            dict(
                input_sizes=[1024],
                input_strides=[1],
                input_offset=0,
                output_sizes=[1024],
                output_strides=[1],
                output_offset=0,
                input_buffer_size=1024,
                output_buffer_size=1024,
            ),
            dict(
                input_sizes=[1024],
                input_strides=[1],
                input_offset=0,
                output_sizes=[1024],
                output_strides=[1],
                output_offset=0,
                input_buffer_size=1024,
                output_buffer_size=1024,
                dtype=np.float32,
            ),
            # Input and output buffer sizes are independent here, unlike every
            # other (in, out) operator: a gather of every fourth element of a
            # 1024-element buffer into a 256-element one. Equal-size cases
            # alone would let a refactor that tied the output shape to the
            # input pass unnoticed. (The copy itself moves the same element
            # count both ways; the operator checks that at construction.)
            dict(
                input_sizes=[256],
                input_strides=[4],
                input_offset=0,
                output_sizes=[256],
                output_strides=[1],
                output_offset=0,
                input_buffer_size=1024,
                output_buffer_size=256,
            ),
        ],
    ),
    (
        "tanh",
        "Tanh",
        [dict(size=1024, num_aie_columns=1, num_channels=1, tile_size=256)],
    ),
    (
        "transpose",
        "Transpose",
        [
            dict(M=64, N=64, num_aie_columns=1, num_channels=1, m=32, n=32, s=1),
            # Non-square, to pin that the output carries the transposed shape
            # (N, M) while the input keeps (M, N). A square-only case cannot
            # tell the two apart.
            dict(M=64, N=128, num_aie_columns=1, num_channels=1, m=32, n=32, s=1),
        ],
    ),
]

_DTYPE_ALIASES = {bfloat16: "bfloat16"}


def dtype_name(dtype):
    """Canonical, stable name for a spec dtype.

    ``np.dtype(bfloat16).name`` round-trips, but going through ``np.dtype``
    first normalises the several spellings an operator may hand back (a numpy
    scalar type, a ``np.dtype``, or ml_dtypes' ``bfloat16``) to one string, so
    a snapshot does not churn on an equivalent-but-differently-spelled dtype.
    """
    if dtype in _DTYPE_ALIASES:
        return _DTYPE_ALIASES[dtype]
    return np.dtype(dtype).name
