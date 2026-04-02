# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

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
class RMSNorm(MLIROperator):
    """AIE-accelerated RMS Normalization layer"""

    size: int
    num_aie_columns: int
    num_channels: int
    tile_size: int
    weighted: bool = False
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "weighted": "w",
    }

    def __post_init__(self):
        # Note: epsilon is hardcoded to 1e-5 in the AIE kernel and cannot be changed at runtime.
        max_multiple = self.num_aie_columns * self.num_channels * self.tile_size
        if self.size % max_multiple != 0:
            raise ValueError(
                f"size ({self.size}) must be a multiple of "
                f"num_aie_columns * num_channels * tile_size ({max_multiple})"
            )
        total_shimdma_channels = self.num_aie_columns * self.num_channels
        if total_shimdma_channels > 16:
            raise ValueError(
                f"num_aie_columns * num_channels ({total_shimdma_channels}) exceeds ShimDMA limit of 16"
            )
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        if self.weighted:
            source_path = self.operator_dir / "design_weighted.py"
            callback_fn = "my_weighted_rms_norm"
        else:
            source_path = self.operator_dir / "design.py"
            callback_fn = "my_rms_norm"

        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                source_path,
                callback_fn,
                (
                    aie_utils.DefaultNPURuntime.device(),
                    self.size,
                    self.num_aie_columns,
                    self.num_channels,
                    self.tile_size,
                    0,  # trace_size
                ),
            ),
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
