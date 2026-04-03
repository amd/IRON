# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from pathlib import Path

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
class Softmax(MLIROperator):
    """AIE-accelerated Softmax operation"""

    rows: int
    cols: int
    num_aie_columns: int = 1
    num_channels: int = 1
    rtp_vector_size: int | None = None
    mask_patch_value: int = 0
    context: object = field(default=None, repr=False)

    @property
    def size(self):
        return self.rows * self.cols

    def __post_init__(self):
        if self.rows % 16 != 0:
            raise ValueError(f"rows ({self.rows}) must be a multiple of 16")
        if self.cols % 16 != 0:
            raise ValueError(f"cols ({self.cols}) must be a multiple of 16")
        if self.rows % self.num_aie_columns != 0:
            raise ValueError(
                f"rows ({self.rows}) must be a multiple of num_aie_columns ({self.num_aie_columns})"
            )
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "softmax",
                (
                    aie_utils.get_current_device(),
                    self.size,
                    self.num_aie_columns,
                    self.num_channels,
                    0,  # trace_size
                    self.cols,
                    self.rtp_vector_size,
                    self.mask_patch_value,
                ),
            ),
        )

    def get_kernel_artifacts(self):
        kernel_dir = get_kernel_dir()
        artifacts = [
            KernelObjectArtifact(
                "softmax.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir
                        / "aie_kernels"
                        / kernel_dir
                        / "softmax.cc"
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
