# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
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
        num_aie_columns=None,
        num_channels=None,
        tile_size=None,
        weighted=False,
        context=None,
    ):
        # Note: epsilon is hardcoded to 1e-5 in the AIE kernel (rms_norm.cc) and cannot be changed at runtime.
        if weighted and num_channels != 1:
            raise ValueError(
                f"Weighted RMS Norm only supports num_channels=1 (got {num_channels})"
            )
        max_multiple = num_aie_columns * tile_size
        if size % max_multiple != 0:
            raise ValueError(
                f"size ({size}) must be a multiple of num_aie_columns * tile_size ({max_multiple})"
            )

        self.size = size
        self.tile_size = tile_size

        self.num_columns = num_aie_columns
        self.num_channels = num_channels
        self.weighted = weighted

        # Enforce ShimDMA limits for weighted RMS Norm (uses 2 inputs per core)
        # Maximum safe configuration: 8 columns × 2 channels = 16 ShimDMA channels
        total_shimdma_channels = self.num_columns * self.num_channels
        if total_shimdma_channels > 16:
            raise ValueError(
                f"num_aie_columns * num_channels ({total_shimdma_channels}) exceeds ShimDMA limit of 16"
            )

        super().__init__(context=context)

    def get_operator_name(self):
        prefix = "weighted_rms" if self.weighted else "rms_norm"
        return f"{prefix}_{self.num_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t"

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
                "rms_norm.o",
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
