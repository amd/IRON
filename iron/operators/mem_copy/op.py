# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEMemCopy(MLIROperator):
    """AIE-accelerated memory copy operator. Note: the `prefix` parameter is intentionally not supported."""

    def __init__(self, size, num_cores, num_channels, bypass, tile_size, context=None):
        self.size = size
        self.num_cores = num_cores
        self.num_channels = num_channels
        self.bypass = bypass
        self.tile_size = tile_size

        # For naming consistency with other operators
        self.bypass_str = "bypass" if bypass else "no_bypass"

        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        return f"mem_copy_{self.num_cores}_cores_{self.num_channels}_chans_tile_{self.tile_size}_{self.bypass_str}"

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=self.operator_dir / "design.py",
            callback_fn="my_mem_copy",
            callback_args=[
                self.context.device_manager.device_type,
                self.size,
                self.num_cores,
                self.num_channels,
                self.bypass,
                self.tile_size,
                0,
            ],
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
            AIERuntimeArgSpec("in", (self.size,)),  # input
            AIERuntimeArgSpec("out", (self.size,)),  # output
        ]
