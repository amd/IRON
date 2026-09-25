# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field

import numpy as np
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.iron.kernels import activation

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)


@dataclass
class Softmax(MLIROperator):
    """AIE-accelerated Softmax operation"""

    rows: int
    cols: int
    num_aie_columns: int = 1
    num_channels: int = 1
    rtp_vector_size: int | None = None
    vector_size_parameter: str | None = None
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
        MLIROperator.__init__(self, context=self.context)

    def _softmax(self):
        return activation.softmax(self.cols)

    def get_mlir_artifact(self):
        softmax_fn = self._softmax()
        # mask_bf16 is exported by the same softmax.cc translation unit.
        mask_fn = softmax_fn.object_file.bind(
            "mask_bf16",
            [np.ndarray[(self.cols,), np.dtype[bfloat16]], np.int32, np.int32],
        )
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
                    "softmax_kernel": softmax_fn,
                    "mask_kernel": mask_fn,
                },
            ),
        )

    def get_kernel_artifacts(self):
        return [KernelObjectArtifact.from_extern(self._softmax())]

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
