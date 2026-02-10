# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import torch.nn as nn
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIERMSNorm(MLIROperator):
    """AIE-accelerated RMS Normalization layer"""

    def __init__(
        self,
        size,
        eps=1e-6,
        num_aie_columns=None,
        num_channels=None,
        tile_size=None,
        weighted=False,
        context=None,
    ):
        max_multiple = num_aie_columns * tile_size
        assert (
            size % max_multiple == 0
        ), "size must be multiple of num_aie_columns * tile_size"
        assert size % tile_size == 0, "size must be multiple of tile_size"

        self.size = size
        self.tile_size = tile_size

        self.num_columns = num_aie_columns
        self.num_channels = num_channels
        self.eps = eps
        self.weighted = weighted

        # Enforce ShimDMA limits for weighted RMS Norm (uses 2 inputs per core)
        # Maximum safe configuration: 8 columns × 2 channels = 16 ShimDMA channels
        total_shimdma_channels = self.num_columns * self.num_channels
        assert total_shimdma_channels <= 16, "Conservative ShimDMA limit"

        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        return f"weighted_rms_{self.num_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t"

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent
        if self.weighted:
            import_path = operator_dir / "design_weighted.py"
            callback_fn = "my_weighted_rms_norm"
            callback_args = [
                self.context.device_manager.device_type,
                self.size,
                self.num_columns,
                self.num_channels,
                self.tile_size,
                0,
            ]
        else:
            import_path = operator_dir / "design.py"
            callback_fn = "my_rms_norm"
            callback_args = [
                self.context.device_manager.device_type,
                self.size,
                self.num_columns,
                self.num_channels,
                0,  # trace_size
                self.tile_size,
            ]

        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=import_path,
            callback_fn=callback_fn,
            callback_args=callback_args,
            callback_kwargs={
                "kernel_archive": self.kernel_archive,
            },
        )

    def get_kernel_artifacts(self):
        artifacts = [
            KernelObjectArtifact(
                f"rms_norm.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir / "aie_kernels" / "aie2p" / "rms_norm.cc"
                    )
                ],
            ),
        ]
        if self.weighted:
            artifacts.append(
                KernelObjectArtifact(
                    "mul.o",
                    dependencies=[
                        SourceArtifact(
                            self.context.base_dir / "aie_kernels" / "generic" / "mul.cc"
                        )
                    ],
                )
            )
        return artifacts

    def get_arg_spec(self):
        specs = [AIERuntimeArgSpec("in", (self.size // self.tile_size, self.tile_size))]
        if self.weighted:
            specs.append(AIERuntimeArgSpec("in", (self.tile_size,)))
        specs.append(
            AIERuntimeArgSpec("out", (self.size // self.tile_size, self.tile_size))
        )
        return specs
