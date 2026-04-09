# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

import numpy as np
from ml_dtypes import bfloat16

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
import aie.utils as aie_utils


@dataclass
class GEMVInt4(MLIROperator):
    """AIE-accelerated fused INT4 dequantization and GEMV operator"""

    M: int
    K: int
    num_aie_columns: int = 4
    tile_size_input: int = 1
    tile_size_output: int | None = None
    group_size: int = field(default=32, repr=False)
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "num_aie_columns": "col",
        "tile_size_input": "tsi",
        "tile_size_output": "tso",
        "group_size": "g",
    }

    def __post_init__(self):
        if self.tile_size_output is None:
            self.tile_size_output = self.M // self.num_aie_columns

        if not (
            self.tile_size_output % self.tile_size_input == 0
            and self.tile_size_output >= self.tile_size_input
        ):
            raise ValueError("tile_size_output must be a multiple of tile_size_input")
        if not (self.K % self.group_size == 0):
            raise ValueError("K must be a multiple of group_size")
        if not (self.group_size % 32 == 0):
            raise ValueError("group_size must be a multiple of 32")
        if not (self.M % self.num_aie_columns == 0):
            raise ValueError("M must be a multiple of num_aie_columns")

        MLIROperator.__init__(self, context=self.context)

    @property
    def _packed_buffer_size(self):
        num_groups_per_row = self.K // self.group_size
        packed_tile_bytes = (
            self.tile_size_input * self.K // 2
            + self.tile_size_input * num_groups_per_row * 2
        )
        rows_per_col = self.M // self.num_aie_columns
        tiles_per_col = rows_per_col // self.tile_size_input
        return self.num_aie_columns * tiles_per_col * packed_tile_bytes

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "my_fused_dequant_matvec",
                (
                    aie_utils.get_current_device(),
                    self.num_aie_columns,
                    self.M,
                    self.K,
                    self.tile_size_input,
                    self.tile_size_output,
                    self.group_size,
                ),
            ),
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                f"fused_dequant_gemv_g{self.group_size}.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir
                        / "aie_kernels"
                        / "generic"
                        / "fused_dequant_gemv.cc"
                    )
                ],
                extra_flags=[
                    f"-DGROUP_SIZE={self.group_size}",
                ],
            ),
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec(
                "in", (self._packed_buffer_size,), dtype=np.uint8
            ),  # packed INT4 weights
            AIERuntimeArgSpec("in", (self.K,)),  # bf16 activation vector
            AIERuntimeArgSpec("out", (self.M,)),  # bf16 output vector
        ]
