# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

from ml_dtypes import bfloat16

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
import aie.utils as aie_utils


@dataclass
class StridedCopy(MLIROperator):
    """AIE-accelerated strided copy operator"""

    input_sizes: list
    input_strides: list
    input_offset: int
    output_sizes: list
    output_strides: list
    output_offset: int
    input_buffer_size: int = field(repr=False)
    output_buffer_size: int = field(repr=False)
    dtype: object = field(default=bfloat16, repr=False)
    transfer_size: int | None = None
    num_aie_channels: int = 1
    input_offset_parameter: str | None = None
    output_offset_parameter: str | None = None
    kwargs: dict = field(default_factory=dict, repr=False)
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "input_sizes": "isz",
        "input_strides": "ist",
        "input_offset": "ioff",
        "output_sizes": "osz",
        "output_strides": "ost",
        "output_offset": "ooff",
        "transfer_size": "tr",
        "num_aie_channels": "ch",
        "input_offset_parameter": "ipar",
        "output_offset_parameter": "opar",
    }

    def __post_init__(self):
        if len(self.input_sizes) != len(self.input_strides):
            raise ValueError(
                f"input_sizes and input_strides must have the same length "
                f"({len(self.input_sizes)} vs {len(self.input_strides)})"
            )
        if len(self.output_sizes) != len(self.output_strides):
            raise ValueError(
                f"output_sizes and output_strides must have the same length "
                f"({len(self.output_sizes)} vs {len(self.output_strides)})"
            )
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "strided_copy",
                kwargs=self.kwargs,
                bind_from=self,
            ),
        )

    def get_kernel_artifacts(self):
        return []

    @staticmethod
    def arg_spec(input_buffer_size, output_buffer_size, dtype=bfloat16):
        # The two sizes are independent: a strided copy may gather from a large
        # buffer into a small one.
        return [
            AIERuntimeArgSpec("in", (int(input_buffer_size),), dtype=dtype),
            AIERuntimeArgSpec("out", (int(output_buffer_size),), dtype=dtype),
        ]
