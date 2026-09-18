# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

from iron.common import (
    MLIROperator,
    same_shape_unary,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
import aie.utils as aie_utils


@dataclass
class MemCopy(MLIROperator):
    """AIE-accelerated memory copy operator."""

    size: int
    num_cores: int
    num_channels: int
    bypass: bool
    tile_size: int
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "num_cores": "cores",
        "num_channels": "chans",
        "tile_size": "tile",
    }

    def __post_init__(self):
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "my_mem_copy",
                (
                    aie_utils.get_current_device(),
                    self.size,
                    self.num_cores,
                    self.num_channels,
                    self.bypass,
                    self.tile_size,
                    0,
                ),
            ),
        )

    def get_kernel_artifacts(self):
        if self.bypass:
            return []
        return [
            KernelObjectArtifact(
                "mem_copy.o",
                extra_flags=["-DBIT_WIDTH=16"],
                dependencies=[
                    SourceArtifact(
                        self.context.kernels_dir / "generic" / "passThrough.cc"
                    )
                ],
            )
        ]

    @staticmethod
    def arg_spec(size):
        return same_shape_unary(size)
