# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import ClassVar

from iron.common import (
    BinaryElementwiseOperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)


@dataclass
class AXPY(BinaryElementwiseOperator):
    """AIE-accelerated aX + Y operator.

    Optional flags select degenerate variants that skip part of the formula:

    * ``add_y=False``  → ``Z = a * X``   (drop the +Y term and the Y buffer)
    * ``mul_x=False``  → ``Z = a + Y``   (drop the *X term and the X buffer)
    * ``causal_mask=True`` (requires ``mul_x=False``) →
        ``Z[i,j] = a if (j > i within head)  else  Y[i,j]``
      Treats the data as a sequence of (mask_block_dim, mask_block_dim) blocks
      and applies a causal (lower-triangular-keep) mask in-place per block.
      Tile-position info is supplied to the kernel via an idx_buffer; tiles
      that lie entirely below the diagonal degenerate to a kernel-side copy
      (no per-tile DMA skipping).  Used by MHA to avoid materialising an
      H * S * S causal-mask input buffer.

    ``add_y=False`` and ``mul_x=False`` cannot be combined.
    """

    scalar_factor: float = 3.0
    add_y: bool = True
    mul_x: bool = True
    causal_mask: bool = False
    mask_block_dim: int | None = None
    # Sub-block parameters (causal_mask only).  Default: process full
    # mask_block_dim rows per (S,S) block starting at row 0.  Set
    # rows_per_block < mask_block_dim and/or row_offset > 0 to process a
    # contiguous row-range slice of one block per invocation — useful when
    # a single full block's element count exceeds the per-invocation BD
    # cap (e.g. S>=32K).
    rows_per_block: int | None = None
    row_offset: int = 0

    kernel_name: ClassVar[str] = "axpy"
    kernel_fn_name: ClassVar[str] = "saxpy"
    callback_fn: ClassVar[str] = "my_axpy"

    def __post_init__(self) -> None:
        if not self.add_y and not self.mul_x:
            raise ValueError("AXPY requires at least one of add_y or mul_x to be True")
        if self.causal_mask:
            if self.mul_x:
                raise ValueError(
                    "AXPY causal_mask=True requires mul_x=False (Z = a + Y form)"
                )
            if not self.add_y:
                raise ValueError(
                    "AXPY causal_mask=True requires add_y=True (needs the Y buffer)"
                )
            if self.mask_block_dim is None:
                raise ValueError(
                    "AXPY causal_mask=True requires mask_block_dim (the (S,S) block dim)"
                )
            # Default rows_per_block = mask_block_dim (process full blocks)
            if self.rows_per_block is None:
                self.rows_per_block = self.mask_block_dim
            if self.rows_per_block <= 0 or self.rows_per_block > self.mask_block_dim:
                raise ValueError(
                    f"rows_per_block ({self.rows_per_block}) must be in (0, "
                    f"mask_block_dim={self.mask_block_dim}]"
                )
            if self.row_offset + self.rows_per_block > self.mask_block_dim:
                raise ValueError(
                    f"row_offset ({self.row_offset}) + rows_per_block "
                    f"({self.rows_per_block}) must be <= mask_block_dim "
                    f"({self.mask_block_dim})"
                )
            block_elements = self.rows_per_block * self.mask_block_dim
            if self.size % block_elements != 0:
                raise ValueError(
                    f"size ({self.size}) must be a multiple of "
                    f"rows_per_block * mask_block_dim ({block_elements})"
                )
            # Multi-core split: either block-aligned (each core handles
            # whole blocks; num_aie_columns must divide num_blocks) or
            # within-block (num_blocks == 1; num_aie_columns must divide
            # rows_per_block).
            num_blocks = self.size // block_elements
            if num_blocks >= self.num_aie_columns:
                if num_blocks % self.num_aie_columns != 0:
                    raise ValueError(
                        f"AXPY causal_mask block-aligned split: "
                        f"num_aie_columns ({self.num_aie_columns}) must "
                        f"divide num_blocks ({num_blocks})"
                    )
            else:
                if num_blocks != 1:
                    raise ValueError(
                        f"AXPY causal_mask within-block split requires "
                        f"num_blocks == 1, got {num_blocks}"
                    )
                if self.rows_per_block % self.num_aie_columns != 0:
                    raise ValueError(
                        f"AXPY causal_mask within-block split: "
                        f"rows_per_block ({self.rows_per_block}) must be a "
                        f"multiple of num_aie_columns ({self.num_aie_columns})"
                    )
        super().__post_init__()

    def get_arg_spec(self) -> list[AIERuntimeArgSpec]:
        # When either input is dropped, the design has one input + one output.
        if not self.add_y or not self.mul_x:
            return [
                AIERuntimeArgSpec("in", (self.size,)),
                AIERuntimeArgSpec("out", (self.size,)),
            ]
        return super().get_arg_spec()

    def get_kernel_artifacts(self) -> list[KernelObjectArtifact]:
        # axpy.cc lives under aie_kernels/generic/ (not device-specific)
        return [
            KernelObjectArtifact(
                "axpy.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir / "aie_kernels" / "generic" / "axpy.cc"
                    )
                ],
            )
        ]

    def _mlir_callback_args(self):
        return super()._mlir_callback_args() + [
            self.scalar_factor,
            self.add_y,
            self.mul_x,
            self.causal_mask,
            self.mask_block_dim if self.mask_block_dim is not None else 0,
            self.rows_per_block if self.rows_per_block is not None else 0,
            self.row_offset,
        ]

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                self.callback_fn,
                tuple(self._mlir_callback_args()),
            ),
        )
