# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar, Dict

import aie.utils as aie_utils

from iron.common.device_utils import get_kernel_dir
from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)


@dataclass
class SiLU(MLIROperator):
    """AIE-accelerated SiLU activation function"""

    size: int
    tile_size: int
    num_aie_columns: int = 8
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "num_aie_columns": "col",
    }

    def __post_init__(self):
        if self.size % (self.num_aie_columns * self.tile_size) != 0:
            raise ValueError(
                f"size ({self.size}) must be a multiple of num_aie_columns * tile_size "
                f"({self.num_aie_columns * self.tile_size})"
            )
        if self.num_aie_columns > 8:
            raise ValueError(
                f"num_aie_columns ({self.num_aie_columns}) exceeds ShimDMA limit: "
                f"a unary operator uses 2 DMA channels per column, max 8 columns (16 channels total)"
            )
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "my_silu",
                (
                    aie_utils.get_current_device(),
                    self.size,
                    self.num_aie_columns,
                    self.tile_size,
                    0,
                ),
            ),
        )

    def get_kernel_artifacts(self):
        kernel_dir = get_kernel_dir()
        artifacts = [
            KernelObjectArtifact(
                "silu.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir / "aie_kernels" / kernel_dir / "silu.cc"
                    )
                ],
            ),
        ]
        if kernel_dir == "aie2":
            mlir_aie_dir = Path(aie_utils.config.root_path())
            artifacts.append(
                KernelObjectArtifact(
                    "lut_based_ops.o",
                    dependencies=[
                        SourceArtifact(
                            mlir_aie_dir
                            / "aie_runtime_lib"
                            / "AIE2"
                            / "lut_based_ops.cpp"
                        )
                    ],
                )
            )
        return artifacts

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.size,)),
            AIERuntimeArgSpec("out", (self.size,)),
        ]
