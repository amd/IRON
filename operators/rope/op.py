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
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIERope(AIEOperatorBase):

    def __init__(
        self,
        rows: int,
        cols: int,
        angle_rows=None,
        num_aie_columns=None,
        method_type=0,
        context=None,
    ):
        if angle_rows is None:
            angle_rows = rows
        if num_aie_columns is None:
            num_aie_columns = 1

        self.rows = rows
        self.cols = cols
        self.angle_rows = angle_rows
        self.num_aie_columns = num_aie_columns
        self.method_type = method_type
        assert method_type in {0, 1}

        # Artifacts created by set_up_artifacts()
        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def set_up_artifacts(self):
        # Compilation artifacts
        operator_dir = Path(__file__).parent
        file_name_base = f"rope_{self.num_aie_columns}c_{self.rows}rows_{self.cols}cols_{self.angle_rows}arows_{self.method_type}m"

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="rope",
            callback_args=[
                self.context.device_manager.device_type,
                self.rows,
                self.cols,
                self.angle_rows,
                self.num_aie_columns,
                0,
                self.method_type,
            ],
        )

        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelObjectArtifact.new(
                    f"rope_{self.method_type}.o",
                    depends=[
                        SourceArtifact.new(
                            self.context.base_dir
                            / "aie_kernels"
                            / "generic"
                            / "rope.cc"
                        )
                    ],
                    extra_flags=[
                        "-DTWO_HALVES" if 0 == self.method_type else "-DINTERLEAVED"
                    ],
                ),
            ],
        )
        insts_artifact = InstsBinArtifact.new(
            f"{file_name_base}.bin", depends=[mlir_artifact]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact

        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

    def set_up_runtime(self):
        # Runtime setup
        self.add_buffer("in", self.rows * self.cols)
        self.add_buffer("angles", self.angle_rows * self.cols)
        self.add_buffer("output", self.rows * self.cols)
        self.add_kernel(
            "rope",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_to_runlist("rope", "in", "angles", "output")

    def forward(self, tensor, angles):
        applicable = (
            tensor.shape[-2] == self.rows
            and tensor.shape[-1] == self.cols
            and tensor.shape[-1] % 16 == 0
            and angles.shape[-2] == self.angle_rows
            and angles.shape[-1] == self.cols
        )
        if not applicable:
            raise AIEOperatorConstraintError("AIERope: incompatible tensor shape(s)")

        # Write data to buffers
        self.write_buffer("in", tensor)
        self.write_buffer("angles", angles)

        # Execute kernel
        self.run_runlist()

        # Read output
        result = self.read_buffer_as_torch("output", shape=tensor.shape, dtype=bfloat16)

        return result
