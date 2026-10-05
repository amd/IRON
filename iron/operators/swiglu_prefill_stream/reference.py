# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Reference SwiGLU-prefill block: ``(SiLU(x @ gate) * (x @ up)) @ down``.

``LAYERS`` is the block. Evaluating it produces the golden output; building
the ONNX graph from it produces the workload stream-dse generates the design
from.

The names below are the block's vocabulary, and they are the keys
``generate_golden_reference`` gives the same tensors. Everything
downstream is named from here: the ONNX tensors, the mapping's layers and runtime arguments, the runtime
buffers, and the tensor handed between fusion groups.
"""

import numpy as np
from ml_dtypes import bfloat16

INPUT = "input"
OUTPUT = "output"
GATE_PROJECTION = "left"
UP_PROJECTION = "right"
ACTIVATION = "left_swished"
HIDDEN = "intermediate"

WEIGHTS = ("w_gate", "w_up", "w_down")

# Every name this module exports, for the correspondence check in iron/tests/stream.
TENSOR_NAMES = (
    INPUT,
    OUTPUT,
    GATE_PROJECTION,
    UP_PROJECTION,
    ACTIVATION,
    HIDDEN,
    *WEIGHTS,
)

# (result, ONNX operator, operands), in topological order.
LAYERS = (
    (GATE_PROJECTION, "Gemm", (INPUT, "w_gate")),
    (UP_PROJECTION, "Gemm", (INPUT, "w_up")),
    (ACTIVATION, "Silu", (GATE_PROJECTION,)),
    (HIDDEN, "Mul", (ACTIVATION, UP_PROJECTION)),
    (OUTPUT, "Gemm", (HIDDEN, "w_down")),
)

# Each operator in float32; its result is rounded to bfloat16 once.
COMPUTE = {
    "Gemm": np.matmul,
    "Silu": lambda x: x * np.exp(-np.logaddexp(0, -x)),
    "Mul": np.multiply,
}


def operand_shapes(M, K, N) -> dict[str, tuple[int, int]]:
    """The input's and the weights' shapes at sequence `M`, embedding `K`, hidden `N`."""
    return {INPUT: (M, K), "w_gate": (K, N), "w_up": (K, N), "w_down": (N, K)}


def swiglu(tensors: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
    """Evaluate ``LAYERS`` in bfloat16.

    Args:
        `tensors`: the input and the weights, by name.

    Returns:
        `tensors` and every tensor the layers produce, by name.
    """
    tensors = dict(tensors)
    for result, operator, operands in LAYERS:
        args = (tensors[name].astype(np.float32) for name in operands)
        tensors[result] = COMPUTE[operator](*args).astype(bfloat16)
    return tensors


def generate_golden_reference(M=1, K=2048, N=8192, seed=42):
    """Golden data for the block: random inputs and every tensor between them.

    Args:
        `M`: sequence length.
        `K`: embedding dimension.
        `N`: hidden dimension (the FFN's intermediate dimension).
        `seed`: random seed.

    Returns:
        Every name in `TENSOR_NAMES`, mapped to its bfloat16 tensor.
    """
    rng = np.random.default_rng(seed)
    val_range = 4
    return swiglu(
        {
            name: (rng.standard_normal(shape) * val_range).astype(bfloat16)
            for name, shape in operand_shapes(M, K, N).items()
        }
    )
