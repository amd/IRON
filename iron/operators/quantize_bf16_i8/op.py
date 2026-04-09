# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field

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
class Quantize(MLIROperator):
    """AIE-accelerated quantization operator (bfloat16 -> int8)"""

    size: int
    num_aie_columns: int
    num_channels: int
    tile_size: int
    group_size: int = field(default=32, repr=False)
    context: object = field(default=None, repr=False)

    def __post_init__(self):
        # Output: int8 data (1 byte each) + bf16 scale factors (2 bytes each, one per group)
        self.input_size = self.size
        self.output_size = self.size + (self.size // self.group_size) * 2

        total_cores = self.num_aie_columns * self.num_channels
        if self.size % self.tile_size != 0:
            raise ValueError(
                f"size ({self.size}) must be divisible by tile_size ({self.tile_size})"
            )
        if self.size % total_cores != 0:
            raise ValueError(
                f"size ({self.size}) must be divisible by total cores ({total_cores})"
            )
        if total_cores > 16:
            raise ValueError(f"total cores ({total_cores}) must be <= 16")
        if self.tile_size % self.group_size != 0:
            raise ValueError(
                f"tile_size ({self.tile_size}) must be divisible by group_size ({self.group_size})"
            )
        if self.group_size % 16 != 0:
            raise ValueError(f"group_size ({self.group_size}) must be a multiple of 16")
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "my_quantize_kernel",
                (
                    aie_utils.get_current_device(),
                    self.size,
                    self.num_aie_columns,
                    self.num_channels,
                    0,  # trace_size
                    self.tile_size,
                    self.group_size,
                ),
            ),
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                f"quantize_bf16_i8_{self.tile_size}.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir
                        / "aie_kernels"
                        / "generic"
                        / "quantize_bf16_i8.cc"
                    )
                ],
                extra_flags=[
                    f"-DTILE_SIZE={self.tile_size}",
                    f"-DGROUP_SIZE={self.group_size}",
                ],
            )
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.input_size,), dtype=bfloat16),
            AIERuntimeArgSpec("out", (self.output_size,), dtype=np.uint8),
        ]
