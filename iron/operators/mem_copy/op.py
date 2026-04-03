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
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir
                        / "aie_kernels"
                        / "generic"
                        / "passThrough.cc"
                    )
                ],
            )
        ]

    def get_artifacts(self):
        return super().get_artifacts(dynamic_obj_fifos=True)

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.size,)),
            AIERuntimeArgSpec("out", (self.size,)),
        ]
