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
from iron.common.device_utils import get_kernel_dir
from iron.common.utils import get_shim_dma_limit


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
        dev = aie_utils.get_current_device()
        shim_dma_limit = get_shim_dma_limit(dev)

        # The weighted design uses one weight ObjectFifo per channel shared across all
        # columns, so its ShimDMA budget is:
        #   (num_aie_columns * num_channels) in-fills
        #   + num_channels weight-fills
        #   + (num_aie_columns * num_channels) out-drains
        # The binding constraint is on the output (host→AIE) shim DMA channels:
        #   num_channels * (num_aie_columns + 1) <= shim_dma_limit
        if self.weighted:
            weighted_shim_usage = self.num_channels * (self.num_aie_columns + 1)
            if weighted_shim_usage > shim_dma_limit:
                raise ValueError(
                    f"weighted RMSNorm with num_aie_columns={self.num_aie_columns}, "
                    f"num_channels={self.num_channels} requires {weighted_shim_usage} ShimDMA "
                    f"output channels but device only has {shim_dma_limit}"
                )
        max_multiple = self.num_aie_columns * self.num_channels * self.tile_size
        if self.size % max_multiple != 0:
            raise ValueError(
                f"size ({self.size}) must be a multiple of "
                f"num_aie_columns * num_channels * tile_size ({max_multiple})"
            )
        total_shimdma_channels = self.num_aie_columns * self.num_channels
        if total_shimdma_channels > shim_dma_limit:
            raise ValueError(
                f"num_aie_columns * num_channels ({total_shimdma_channels}) "
                f"exceeds ShimDMA limit of {shim_dma_limit} for this device"
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
                    aie_utils.get_current_device(),
                    self.size,
                    self.num_aie_columns,
                    self.num_channels,
                    self.tile_size,
                    0,  # trace_size
                ),
            ),
        )

    def get_kernel_artifacts(self):
        arch_dir = get_kernel_dir()
        artifacts = [
            KernelObjectArtifact(
                "rms_norm.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir / "aie_kernels" / arch_dir / "rms_norm.cc"
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
