# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from dataclasses import dataclass, field
from typing import ClassVar, Dict

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
import aie.utils as aie_utils
import numpy as np
from aie.iron import Kernel, ObjectFifo, Program, Runtime, TaskGroup, Worker
from iron.operators._kernels import declare_kernel
from aie.iron.device import NPU1, NPU2
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.helpers.dialects.scf import _for as range_
from ml_dtypes import bfloat16
from iron.operators._trace import maybe_enable_trace
import torch


@dataclass
class RoPE(MLIROperator):
    """AIE-accelerated RoPE (Rotary Position Embedding) operator"""

    rows: int
    cols: int
    angle_rows: int | None = None
    num_aie_columns: int = 1
    method_type: int = 0
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "num_aie_columns": "col",
        "angle_rows": "arows",
        "method_type": "m",
    }

    def __post_init__(self):
        if self.angle_rows is None:
            self.angle_rows = self.rows

        if not (self.cols % (16 * 2) == 0 and self.cols >= (16 * 2)):
            raise ValueError("cols must be multiple of 32 and >= 32")
        if self.rows % self.num_aie_columns != 0:
            raise ValueError("rows must be divisible by num_aie_columns")
        if not (self.angle_rows <= self.rows and self.rows % self.angle_rows == 0):
            raise ValueError("angle_rows must divide rows")
        if not (
            self.angle_rows >= self.num_aie_columns
            and self.angle_rows % self.num_aie_columns == 0
        ):
            raise ValueError("angle_rows must be divisible by num_aie_columns")
        if self.method_type not in {0, 1}:
            raise ValueError(f"method_type must be 0 or 1, got {self.method_type}")

        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(fn=rope, bind_from=self),
        )

    @staticmethod
    def arg_spec(rows, cols, angle_rows=None):
        # The angles broadcast: angle_rows divides rows, and defaults to it.
        angle_rows = rows if angle_rows is None else angle_rows
        return [
            AIERuntimeArgSpec("in", (rows, cols)),  # input tensor
            AIERuntimeArgSpec("in", (angle_rows, cols)),  # angles
            AIERuntimeArgSpec("out", (rows, cols)),  # output
        ]

    def reference(self, x, angles):
        """CPU reference for RoPE.

        Assumes ``angles`` holds interleaved [cos, sin, cos, sin, ...] pairs
        along the last dim (length ``cols``).  Only ``method_type == 0``
        (TWO_HALVES) is currently supported.

        ``angles`` may have fewer rows than ``x``; in that case the angles
        are tiled along the row dimension to match ``x``."""
        return reference(x, angles, self.method_type, self.rows, self.cols)


# --------------------------------------------------------------------------
# The MLIR this operator generates.
# --------------------------------------------------------------------------

"""
Rotary Positional Encoding (RoPE) design

Applies RoPE to each row of the input tensor.
Expects input tensor of shape (rows, cols) and a tensor of precomputed angles (look-up table) of shape (angle_rows, cols).
Another interpretation of the input tensor is (rows / num_heads, num_heads, cols), where num_heads = rows / angle_rows.

- rows: number of rows in the input tensor (e.g., number of tokens)
- cols: number of columns in the input tensor (e.g., head dimension)
- angle_rows: number of input rows in the angle look-up table.
  If this is less than `rows`, each row of angles will be reused for `rows / angle_rows` consecutive rows of the input tensor.
  This is useful for models where multiple heads share the same positional encodings and the heads are 'interspersed' in the input tensor (i.e. input tensor shape is (rows, n_heads, cols)).
"""


def rope(
    dev,
    rows,
    cols,
    angle_rows=None,
    num_aie_columns=1,
    trace_size=0,
    method_type=None,
    func_prefix="",
    kernels_dir=None,
):
    dtype = bfloat16

    if angle_rows is None:
        angle_rows = rows
    assert cols % (16 * 2) == 0 and cols >= (
        16 * 2
    ), "cols must be multiple of 32 and >= 32 (rope.cc kernel processes two 16-element vectors at a time)"
    assert rows % num_aie_columns == 0, "rows must be divisible by num_aie_columns"
    assert angle_rows <= rows and rows % angle_rows == 0, "angle_rows must divide rows"
    assert (
        angle_rows >= num_aie_columns and angle_rows % num_aie_columns == 0
    ), "angle_rows must be divisible by num_aie_columns"

    tensor_rows_per_aie_column = rows // num_aie_columns
    angle_rows_per_aie_column = angle_rows // num_aie_columns
    tensor_rows_per_angle_row = rows // angle_rows

    # Define tensor types
    tensor_ty = np.ndarray[(rows, cols), np.dtype[dtype]]
    angle_ty = np.ndarray[(angle_rows, cols), np.dtype[dtype]]
    tensor_tile_ty = np.ndarray[(1, cols), np.dtype[dtype]]
    angle_tile_ty = np.ndarray[(1, cols), np.dtype[dtype]]

    # AIE-array data movement with object fifos (one per column, not per channel)
    of_in = [ObjectFifo(tensor_tile_ty, name=f"in_{i}") for i in range(num_aie_columns)]
    of_lut = [
        ObjectFifo(angle_tile_ty, name=f"lut_{i}") for i in range(num_aie_columns)
    ]
    of_out = [
        ObjectFifo(tensor_tile_ty, name=f"out_{i}") for i in range(num_aie_columns)
    ]

    # AIE Core Function declaration. method_type 0 = two-halves (HF), 1 =
    # interleaved/Llama (the "rope" symbol).
    rope_symbol = "rope_two_halves" if method_type == 0 else "rope"
    rope_kernel = declare_kernel(
        rope_symbol,
        [tensor_tile_ty, angle_tile_ty, tensor_tile_ty, np.int32],
        source=Path(kernels_dir) / "generic" / "rope.cc",
        func_prefix=func_prefix,
    )

    # Define a task that will run on a compute tile
    def core_body(of_in, of_lut, of_out, rope_kernel):
        # Number of sub-vector "tile" iterations
        for _ in range_(angle_rows_per_aie_column):
            elem_lut = of_lut.acquire(1)
            for _ in range_(tensor_rows_per_angle_row):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                rope_kernel(elem_in, elem_lut, elem_out, cols)
                of_in.release(1)
                of_out.release(1)
            of_lut.release(1)

    # Create a worker to run the task on a compute tile (one per column)
    my_workers = [
        Worker(
            core_body,
            [
                of_in[i].cons(),
                of_lut[i].cons(),
                of_out[i].prod(),
                rope_kernel,
            ],
        )
        for i in range(num_aie_columns)
    ]

    # This pattern chops the data into equal chunks and moves them in parallel across the columns
    tensor_taps = [
        TensorAccessPattern(
            (rows, cols),
            i * tensor_rows_per_aie_column * cols,  # Start offset for column i
            [1, 1, 1, tensor_rows_per_aie_column * cols],
            [0, 0, 0, 1],
        )
        for i in range(num_aie_columns)
    ]
    angle_taps = [
        TensorAccessPattern(
            (angle_rows, cols),
            i * angle_rows_per_aie_column * cols,  # Start offset for column i
            [1, 1, 1, angle_rows_per_aie_column * cols],
            [0, 0, 0, 1],
        )
        for i in range(num_aie_columns)
    ]

    # Runtime operations to move data to/from the AIE-array
    def sequence(A, B, C, of_in_prods, of_lut_prods, of_out_conss):

        # Initialize a group for parallel drain tasks, with fill resources free'd when drains complete.
        tg = TaskGroup()

        # Fill the input objectFIFOs with data
        for i in range(num_aie_columns):
            of_in_prods[i].fill(
                A,
                tensor_taps[i],
                group=tg,
            )
            of_lut_prods[i].fill(
                B,
                angle_taps[i],
                group=tg,
            )
        # Drain the output objectFIFOs with data
        for i in range(num_aie_columns):
            of_out_conss[i].drain(
                C,
                tensor_taps[i],
                wait=True,  # wait for the transfer to complete and data to be available
                group=tg,
            )
        tg.finish()

    rt = Runtime(
        sequence,
        [
            tensor_ty,
            angle_ty,
            tensor_ty,
            [of.prod() for of in of_in],
            [of.prod() for of in of_lut],
            [of.cons() for of in of_out],
        ],
    )
    # Place program components (assign them resources on the device) and generate an MLIR module
    prog = Program(dev, rt, workers=my_workers)
    maybe_enable_trace(prog, trace_size, my_workers)
    return prog.resolve_program()


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def compute_rope_params(
    head_dim,
    theta_base=10_000,
    context_length=4096,
    method_type=0,
    freq_config=None,
    dtype=torch.float32,
):
    """Compute RoPE parameters (cos and sin tables)."""
    assert head_dim % 2 == 0, "Embedding dimension must be even"

    # Compute the inverse frequencies
    inv_freq = 1.0 / (
        theta_base
        ** (
            torch.arange(0, head_dim, 2, dtype=dtype)[: (head_dim // 2)].float()
            / head_dim
        )
    )

    # Frequency adjustments
    if freq_config is not None:
        low_freq_wavelen = (
            freq_config["original_context_length"] / freq_config["low_freq_factor"]
        )
        high_freq_wavelen = (
            freq_config["original_context_length"] / freq_config["high_freq_factor"]
        )

        wavelen = 2 * torch.pi / inv_freq

        inv_freq_llama = torch.where(
            wavelen > low_freq_wavelen, inv_freq / freq_config["factor"], inv_freq
        )

        smooth_factor = (
            freq_config["original_context_length"] / wavelen
            - freq_config["low_freq_factor"]
        ) / (freq_config["high_freq_factor"] - freq_config["low_freq_factor"])

        smoothed_inv_freq = (1 - smooth_factor) * (
            inv_freq / freq_config["factor"]
        ) + smooth_factor * inv_freq

        is_medium_freq = (wavelen <= low_freq_wavelen) & (wavelen >= high_freq_wavelen)
        inv_freq_llama = torch.where(is_medium_freq, smoothed_inv_freq, inv_freq_llama)
        inv_freq = inv_freq_llama

    # Generate position indices
    positions = torch.arange(context_length, dtype=dtype)

    # Compute the angles
    angles = positions.unsqueeze(1) * inv_freq.unsqueeze(
        0
    )  # Shape: (context_length, head_dim / 2)

    # Precompute sine and cosine
    cos = torch.cos(angles)
    sin = torch.sin(angles)

    return cos, sin


def apply_rope(x, cos, sin, method_type=0):
    """Apply rotary position embedding to input tensor."""
    if method_type == 0:  # For the two-halves method used in HF transformers
        # x: (n_heads, seq_len, head_dim)
        n_heads, seq_len, head_dim = x.shape
        assert head_dim % 2 == 0, "Head dimension must be even"

        # Split x into first half and second half
        x1 = x[..., : head_dim // 2]  # First half
        x2 = x[..., head_dim // 2 :]  # Second half

        # Adjust sin and cos shapes
        cos = cos[:seq_len, :]  # Shape: (seq_len, head_dim / 2)
        sin = sin[:seq_len, :]

        # Apply the rotary transformation
        x_rotated = torch.empty_like(x)
        x_rotated[..., : head_dim // 2] = (x1 * cos) + (-x2 * sin)
        x_rotated[..., head_dim // 2 :] = (x2 * cos) + (x1 * sin)

        # It's ok to use lower-precision after applying cos and sin rotation
        return x_rotated.to(dtype=x.dtype)
    elif method_type == 1:  # For the interleaved method used in the Llama paper
        # x: (n_heads, seq_len, head_dim)
        n_heads, seq_len, head_dim = x.shape
        assert head_dim % 2 == 0, "Head dimension must be even"

        # Split x into even and odd columns
        x_even = x[..., ::2]  # Even columns
        x_odd = x[..., 1::2]  # Odd columns

        # Adjust sin and cos shapes
        cos = cos[:seq_len, :]  # Shape: (seq_len, head_dim / 2)
        sin = sin[:seq_len, :]

        # Apply the rotary transformation and interleave the even and odd outputs
        x_rotated = torch.empty_like(x)
        x_rotated[..., ::2] = (x_even * cos) - (x_odd * sin)
        x_rotated[..., 1::2] = (x_even * sin) + (x_odd * cos)

        # It's ok to use lower-precision after applying cos and sin rotation
        return x_rotated.to(dtype=x.dtype)
    else:
        raise ValueError("Invalid method_type. Must be 0 or 1.")


def reference(x, angles, method_type=0, rows=None, cols=None):
    """CPU reference for RoPE from the operator's packed ``angles`` buffer.

    ``angles`` holds interleaved [cos, sin, cos, sin, ...] pairs along the last
    dim (length ``cols``).  Only ``method_type == 0`` (TWO_HALVES) is supported
    here; the golden-data generator uses :func:`apply_rope`, which additionally
    supports the interleaved method and works from the full-precision cos/sin
    tables.  ``angles`` may have fewer rows than ``x``; in that case each angle
    row is repeated for ``rows / angles.shape[0]`` *consecutive* rows of ``x``,
    matching the device kernel (design.py's ``core_body`` acquires one angle
    row and applies it to that many consecutive input rows before moving on).
    """
    if method_type != 0:
        raise NotImplementedError(
            f"RoPE reference only supports method_type=0 (TWO_HALVES), "
            f"got {method_type}"
        )
    if cols is None:
        cols = x.shape[-1]
    if rows is None:
        rows = x.shape[0]
    half = cols // 2
    cos = angles[..., 0::2].to(torch.float32)
    sin = angles[..., 1::2].to(torch.float32)
    if cos.shape[0] != rows:
        if rows % cos.shape[0] == 0:
            rep = rows // cos.shape[0]
            cos = cos.repeat_interleave(rep, dim=0)
            sin = sin.repeat_interleave(rep, dim=0)
        else:
            cos = cos[:rows]
            sin = sin[:rows]
    x32 = x.to(torch.float32)
    x1, x2 = x32[..., :half], x32[..., half:]
    y1 = x1 * cos - x2 * sin
    y2 = x2 * cos + x1 * sin
    return torch.cat([y1, y2], dim=-1).to(torch.bfloat16)


def generate_golden_reference(
    rows=4096,
    cols=64,
    context_len=131072,
    method_type=0,
    rope_theta_base=500000.0,
    rope_freq_factor=32.0,
    rope_freq_low_factor=1.0,
    rope_freq_high_factor=4.0,
    rope_freq_orig_ctx_len=8192,
    seed=42,
):
    torch.manual_seed(seed)

    # Generate golden inputs
    freq_config = {
        "factor": rope_freq_factor,
        "low_freq_factor": rope_freq_low_factor,
        "high_freq_factor": rope_freq_high_factor,
        "original_context_length": rope_freq_orig_ctx_len,
    }
    cos, sin = compute_rope_params(
        head_dim=cols,
        theta_base=rope_theta_base,
        context_length=context_len,
        method_type=method_type,
        freq_config=freq_config,
    )
    val_range = 4
    # Head count is inferred from rows and context_len. This logic assumes rows is either
    # smaller than context_len (1 head, seq_len == rows) or an exact multiple of context_len
    # (n_heads == rows // context_len).
    if context_len < rows and rows % context_len != 0:
        raise ValueError(
            f"rows ({rows}) must be a multiple of context_len ({context_len}) when rows > context_len"
        )
    n_heads = rows // context_len if context_len < rows else 1
    seq_len = rows // n_heads
    A = torch.rand(n_heads, seq_len, cols, dtype=torch.bfloat16) * val_range

    # Create the lut by interleaving cos and sin
    B = torch.zeros((seq_len, cols), dtype=torch.bfloat16)
    B[:, ::2] = cos[:seq_len, : cols // 2]
    B[:, 1::2] = sin[:seq_len, : cols // 2]

    # Generate golden outputs
    C = apply_rope(A, cos, sin, method_type)

    return {
        "A": A,
        "B": B,
        "C": C,
    }
