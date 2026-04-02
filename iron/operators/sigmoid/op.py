# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from iron.common.device_utils import DEVICE_CONFIGS
from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIESigmoid(MLIROperator):
    """AIE-accelerated Sigmoid activation function"""

    def __init__(self, size, num_aie_columns, num_channels, tile_size, context=None):
        max_multiple = num_aie_columns * tile_size
        assert (
            size % max_multiple == 0
        ), "size must be multiple of num_aie_columns * tile_size"
        assert size % tile_size == 0, "size must be multiple of tile_size"

        self.size = size
        self.tile_size = tile_size

        self.num_columns = num_aie_columns
        self.num_channels = num_channels

        total_shimdma_channels = self.num_columns * self.num_channels
        assert total_shimdma_channels <= 16, "Conservative ShimDMA limit"

        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        return f"sigmoid_{self.num_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t"

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_sigmoid",
            callback_args=[
                self.context.device_manager.device_type,
                self.size,
                self.num_columns,
                self.num_channels,
                self.tile_size,
                0,
            ],
        )

    def get_kernel_artifacts(self):
        kernel_dir = DEVICE_CONFIGS[self.context.device_manager.device_str()][
            "kernel_dir"
        ]
        artifacts = [
            KernelObjectArtifact(
                "sigmoid.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir
                        / "aie_kernels"
                        / kernel_dir
                        / "sigmoid.cc"
                    )
                ],
            ),
        ]
        if kernel_dir == "aie2":
            artifacts.append(
                KernelObjectArtifact(
                    "lut_based_ops.o",
                    dependencies=[
                        SourceArtifact(
                            self.context.mlir_aie_dir
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
            AIERuntimeArgSpec("in", (self.size,)),  # input
            AIERuntimeArgSpec("out", (self.size,)),  # output
        ]
