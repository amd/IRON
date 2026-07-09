# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field

import aie.utils as aie_utils

from iron.common.device_utils import get_kernel_dir
from iron.common.operator_bases import lut_based_ops_artifacts
from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelArchiveArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)


@dataclass
class Softmax(MLIROperator):
    """AIE-accelerated Softmax operation

    When *chunk_size* is set (and < cols), uses an online / tiled softmax
    that processes each row in two passes with sub-tile chunks, avoiding the
    local-memory exhaustion that occurs with very long rows (e.g. S >= 8192).
    """

    rows: int
    cols: int
    num_aie_columns: int = 1
    num_channels: int = 1
    rtp_vector_size: int | None = None
    vector_size_parameter: str | None = None
    chunk_size: int | None = None
    context: object = field(default=None, repr=False)

    @property
    def size(self):
        return self.rows * self.cols

    def __post_init__(self):
        if self.rows % 16 != 0:
            raise ValueError(f"rows ({self.rows}) must be a multiple of 16")
        if self.cols % 16 != 0:
            raise ValueError(f"cols ({self.cols}) must be a multiple of 16")
        if self.rows % self.num_aie_columns != 0:
            raise ValueError(
                f"rows ({self.rows}) must be a multiple of num_aie_columns ({self.num_aie_columns})"
            )
        if self.chunk_size is not None:
            if self.cols % self.chunk_size != 0:
                raise ValueError(
                    f"cols ({self.cols}) must be a multiple of chunk_size ({self.chunk_size})"
                )
            if self.chunk_size % 64 != 0:
                raise ValueError(
                    f"chunk_size ({self.chunk_size}) must be a multiple of 64"
                )
        MLIROperator.__init__(self, context=self.context)

    @property
    def _kernel_link_file(self):
        kernel_dir = get_kernel_dir()
        if kernel_dir == "aie2":
            return f"{self.name}_kernels.a"
        return "softmax.o"

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "softmax",
                (),
                {
                    "dev": aie_utils.get_current_device(),
                    "num_elements": self.size,
                    "num_aie_columns": self.num_aie_columns,
                    "num_channels": self.num_channels,
                    "trace_size": 0,
                    "tile_size": self.cols,
                    "rtp_vector_size": self.rtp_vector_size,
                    "vector_size_parameter": self.vector_size_parameter,
                    "kernel_obj_file": self._kernel_link_file,
                    "chunk_size": self.chunk_size,
                },
            ),
        )

    def get_kernel_artifacts(self):
        kernel_dir = get_kernel_dir()
        softmax_obj = KernelObjectArtifact(
            "softmax.o",
            dependencies=[
                SourceArtifact(
                    self.context.base_dir / "aie_kernels" / kernel_dir / "softmax.cc"
                )
            ],
        )
        lut_objs = lut_based_ops_artifacts(kernel_dir)
        if lut_objs:
            return [
                KernelArchiveArtifact(
                    f"{self.name}_kernels.a",
                    dependencies=[softmax_obj] + lut_objs,
                )
            ]
        return [softmax_obj]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.size,)),
            AIERuntimeArgSpec("out", (self.size,)),
        ]

    def reference(self, x):
        """CPU reference: row-wise softmax over ``cols``.

        Note: ignores the runtime ``vector_size_parameter`` (if any); the
        reference always softmaxes over the full ``cols``. For decode-style
        usage with a masked tail, the trailing positions will not match the
        NPU output."""
        from iron.operators.softmax.reference import reference

        return reference(x.reshape(self.rows, self.cols))
