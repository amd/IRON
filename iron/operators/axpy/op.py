# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field

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
class AXPY(MLIROperator):
    """AIE-accelerated aX + Y operator"""

    size: int
    num_aie_columns: int
    tile_size: int
    scalar_factor: float = 3.0
    context: object = field(default=None, repr=False)

    def __post_init__(self):
        max_multiple = self.num_aie_columns * self.tile_size
        if self.size % max_multiple != 0:
            raise ValueError(
                f"size ({self.size}) must be a multiple of num_aie_columns * tile_size ({max_multiple})"
            )
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "my_axpy",
                (
                    aie_utils.DefaultNPURuntime.device(),
                    self.size,
                    self.num_aie_columns,
                    self.tile_size,
                    0,
                    self.scalar_factor,
                ),
            ),
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                "axpy.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir / "aie_kernels" / "generic" / "axpy.cc"
                    )
                ],
            ),
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.size,)),  # x
            AIERuntimeArgSpec("in", (self.size,)),  # y
            AIERuntimeArgSpec("out", (self.size,)),  # output
        ]
