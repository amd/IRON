# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path

from operators.common import (
    AIEOperatorBase,
    AIEOperatorConstraintError,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    torch_to_numpy,
    numpy_to_torch,
)


class AIEAXPY(AIEOperatorBase):
    """AIE-accelerated aX + Y operator"""

    def __init__(
        self, size, num_aie_columns, num_channels, tile_size, scalar_factor=0.01
    ):
        max_multiple = num_aie_columns * tile_size
        padded_size = ((size + max_multiple - 1) // max_multiple) * max_multiple
        self.orig_size = size
        self.size = padded_size
        self.tile_size = tile_size
        self.num_aie_columns = num_aie_columns
        self.num_channels = num_channels
        self.scalar_factor = scalar_factor

        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self)

    def set_up_artifacts(self):
        operator_dir = Path(__file__).parent
        file_name_base = f"axpy_{self.num_aie_columns}c_{self.num_channels}ch_{self.size}_{self.tile_size}t_{self.scalar_factor}s"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="my_axpy",
            callback_args=[
                self.device_manager.device_type,
                self.size,
                self.num_aie_columns,
                self.num_channels,
                self.tile_size,
                0,
                self.scalar_factor,
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    f"axpy.o",
                    depends=[
                        SourceArtifact.new(
                            self.base_dir / "aie_kernels" / "generic" / "axpy.cc"
                        )
                    ],
                ),
            ],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact
        self.add_artifacts([xclbin_artifact, insts_artifact])

    def set_up_runtime(self):
        self.add_buffer("x", self.size)
        self.add_buffer("y", self.size)
        self.add_buffer("output", self.size)
        self.add_kernel(
            "axpy",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("axpy", "x", "y", "output")

    def forward(self, x, y):
        if x.numel() > self.size or y.numel() > self.size:
            raise AIEOperatorConstraintError(
                "AIEAXPY: input too large for configured size"
            )
        if x.numel() != y.numel():
            raise AIEOperatorConstraintError("AIEAXPY: sizes of X and Y do not match")

        original_shape = x.shape
        x_flat = x.reshape(-1)
        y_flat = y.reshape(-1)

        pad_len = self.size - x_flat.numel()
        if pad_len > 0:
            x_flat = torch.nn.functional.pad(x_flat, (0, pad_len))
            y_flat = torch.nn.functional.pad(y_flat, (0, pad_len))

        x_np = torch_to_numpy(x_flat)
        y_np = torch_to_numpy(y_flat)
        self.write_buffer("x", x_np)
        self.write_buffer("y", y_np)
        self.write_buffer("output", np.zeros(self.size, dtype=bfloat16))
        self.run_runlist()
        result = self.read_buffer_as_torch("output", shape=(self.size,), dtype=bfloat16)

        if pad_len > 0:
            result = result[: x_flat.numel() - pad_len]

        return result.reshape(*original_shape)
