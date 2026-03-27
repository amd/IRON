# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIELayerNorm(MLIROperator):
    """AIE-accelerated LAYER NORM operator"""

    def __init__(
        self, size, num_aie_columns, num_channels, tile_size, trace_size=0, context=None
    ):
        max_multiple = num_aie_columns * tile_size
        assert (
            size % max_multiple == 0
        ), "size must be multiple of num_aie_columns * tile_size"
        assert size % tile_size == 0, "size must be multiple of tile_size"

        self.size = size
        self.tile_size = tile_size
        self.trace_size = trace_size
        self.num_aie_columns = num_aie_columns
        self.num_channels = num_channels

        total_shimdma_channels = self.num_aie_columns * self.num_channels
        assert total_shimdma_channels <= 16, "Conservative ShimDMA limit"

        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        return f"layer_norm_{self.num_aie_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t"

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_layer_norm",
            callback_args=[
                self.context.device_manager.device_type,
                self.size,
                self.num_aie_columns,
                self.num_channels,
                self.trace_size,
                self.tile_size,
            ],
        )

    def get_kernel_artifacts(self):
        # Use device-aware kernel selection
        arch_dir = (
            "aie2p" if self.context.device_manager.device_str() == "npu2" else "aie2"
        )
        return [
            KernelObjectArtifact(
                f"layer_norm.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir
                        / "aie_kernels"
                        / arch_dir
                        / "layer_norm.cc"
                    )
                ],
            ),
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.size,)),  # input
            AIERuntimeArgSpec("out", (self.size,)),  # output
        ]
