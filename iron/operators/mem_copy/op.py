# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from iron.operators.common import (
    AIEOperatorBase,
    AIEOperatorConstraintError,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEMemCopy(AIEOperatorBase):

    def __init__(self, size, num_cores, num_channels, bypass, tile_size, context=None):
        self.size = size
        self.num_cores = num_cores
        self.num_channels = num_channels
        self.bypass = bypass
        self.tile_size = tile_size

        # For naming consistency with other operators
        self.bypass_str = "bypass" if bypass else "no_bypass"

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent

        size = self.tile_size * self.num_cores

        # Xclbin base name (shared)
        xclbin_base_name = f"mem_copy_{self.num_cores}_cores_{self.num_channels}_chans_tile_{self.tile_size}_{self.bypass_str}"

        # Generate MLIR for xclbin (using dummy size)
        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{xclbin_base_name}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_mem_copy",
            callback_args=[
                self.context.device_manager.device_type,
                size,
                self.num_cores,
                self.num_channels,
                self.bypass,
                self.tile_size,
                0,
            ],
        )

        # Build kernel only if not bypass mode
        if not self.bypass:
            kernel_artifact = KernelObjectArtifact.new(
                "mem_copy.o",
                depends=[
                    SourceArtifact.new(
                        self.context.base_dir
                        / "aie_kernels"
                        / "generic"
                        / "passThrough.cc"
                    )
                ],
            )
            xclbin_depends = [mlir_artifact, kernel_artifact]
        else:
            xclbin_depends = [mlir_artifact]

        xclbin_artifact = XclbinArtifact.new(
            f"{xclbin_base_name}.xclbin",
            depends=xclbin_depends,
            extra_flags=["--dynamic-objFifos"],
        )

        insts_file_name = f"mem_copy_{self.num_cores}_cores_{self.num_channels}_chans_{self.size}_tile_{self.tile_size}_{self.bypass_str}"
        insts_artifact = InstsBinArtifact.new(
            f"{insts_file_name}.bin",
            depends=[mlir_artifact],
            extra_flags=["--dynamic-objFifos"],
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact

        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

    def set_up_runtime(self):
        self.add_buffer("input", self.size)
        self.add_buffer("output", self.size)
        self.add_kernel(
            "mem_copy",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("mem_copy", "input", "output")

    def forward(self, x):
        """Forward pass for memory copy"""
        if x.numel() != self.size:
            raise AIEOperatorConstraintError(
                f"AIEMemCopy: input size {x.numel()} does not match expected size {self.size}"
            )

        original_shape = x.shape
        x_flat = x.reshape(-1)

        # Execute on AIE
        self.write_buffer("input", x_flat)
        self.write_buffer("output", np.zeros(self.size, dtype=bfloat16))
        self.run_runlist()
        result = self.read_buffer_as_torch("output", shape=(self.size,), dtype=bfloat16)

        return result.reshape(*original_shape)
