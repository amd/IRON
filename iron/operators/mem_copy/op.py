# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
import aie.utils as aie_utils
import numpy as np
from aie.iron.kernels import eltwise

from iron.operators.mem_copy.design import mem_copy_line_size


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
                {"passthrough_kernel": self._kernel()},
            ),
        )

    def _kernel(self):
        if self.bypass:
            return None
        return eltwise.passthrough(mem_copy_line_size(self.tile_size), np.int16)

    def reference(self, x):
        from iron.operators.mem_copy.reference import reference

        return reference(x)

    def get_kernel_artifacts(self):
        if self.bypass:
            return []
        return [KernelObjectArtifact.from_extern(self._kernel())]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.size,)),
            AIERuntimeArgSpec("out", (self.size,)),
        ]
