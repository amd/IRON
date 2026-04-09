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
class ScaleI32(MLIROperator):
    """AIE-accelerated int32 to bfloat16 conversion with per-tensor scale.

    Designed to compose directly with INT8 GEMM output — no packed buffer formats.
    Each element: out[i] = bf16(float(in_i32[i]) * scale)
    """

    size: int
    num_aie_columns: int
    num_channels: int
    tile_size: int
    context: object = field(default=None, repr=False)

    def __post_init__(self):
        total_cores = self.num_aie_columns * self.num_channels
        if self.size % self.tile_size != 0:
            raise ValueError(
                f"size ({self.size}) must be divisible by tile_size ({self.tile_size})"
            )
        if self.size % total_cores != 0:
            raise ValueError(
                f"size ({self.size}) must be divisible by total cores ({total_cores})"
            )
        if total_cores > 8:
            raise ValueError(f"total cores ({total_cores}) must be <= 8")
        if self.tile_size % 16 != 0:
            raise ValueError(f"tile_size ({self.tile_size}) must be a multiple of 16")
        self.total_cores = total_cores
        # Scale buffer: 16 bf16 values per core (for DMA alignment)
        self.scale_size = total_cores * 16
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "my_scale_i32_bf16_kernel",
                (
                    aie_utils.get_current_device(),
                    self.size,
                    self.num_aie_columns,
                    self.num_channels,
                    0,  # trace_size
                    self.tile_size,
                ),
            ),
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                f"scale_i32_bf16_{self.tile_size}.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir
                        / "aie_kernels"
                        / "generic"
                        / "scale_i32_bf16.cc"
                    )
                ],
                extra_flags=[],
            )
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.size,), dtype=np.int32),
            AIERuntimeArgSpec("in", (self.scale_size,), dtype=bfloat16),
            AIERuntimeArgSpec("out", (self.size,), dtype=bfloat16),
        ]
