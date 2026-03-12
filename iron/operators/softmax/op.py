# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIESoftmax(MLIROperator):
    """AIE-accelerated Softmax operation"""

    def __init__(
        self,
        rows: int,
        cols: int,
        num_aie_columns=1,
        num_channels=1,
        rtp_vector_size=None,
        mask_patch_value=0,
        context=None,
    ):
        assert rows % 16 == 0, "rows must be multiple of 16"
        assert cols % 16 == 0, "cols must be multiple of 16"
        assert (rows * cols) % (
            num_aie_columns * cols
        ) == 0, "size must be multiple of num_aie_columns * tile_size"

        self.rows = rows
        self.cols = cols
        self.size = rows * cols
        self.num_aie_columns = num_aie_columns
        self.num_channels = num_channels
        self.rtp_vector_size = rtp_vector_size
        self.mask_patch_value = mask_patch_value

        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        name = f"softmax_{self.num_aie_columns}col_{self.num_channels}ch_{self.size}_{self.cols}t"
        if self.rtp_vector_size is not None:
            name += f"_{self.rtp_vector_size}rtp"
        return name

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="softmax",
            callback_args=[
                self.context.device_manager.device_type,
                self.size,
                self.num_aie_columns,
                self.num_channels,
                0,  # trace_size
                self.cols,
                self.rtp_vector_size,
                self.mask_patch_value,
            ],
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                f"softmax.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir / "aie_kernels" / "aie2p" / "softmax.cc"
                    )
                ],
            ),
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.size,)),
            AIERuntimeArgSpec("out", (self.size,)),
        ]
