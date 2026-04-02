# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar, Dict

import aie.utils as aie_utils
from .base import MLIROperator, AIERuntimeArgSpec
from .compilation import (
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)


@dataclass
class ChanneledUnaryOperator(MLIROperator):
    """Base class for channeled unary AIE operators (single input, single output).

    Assumes a single kernel source file and a standard design.py callback
    with args [device, size, num_aie_columns, num_channels, tile_size, trace_size].

    Subclasses must define three ClassVar attributes:
        kernel_name:   name of the kernel object file (e.g. "gelu" → gelu.o / gelu.cc)
        kernel_subdir: subdirectory under aie_kernels/ (e.g. "aie2p", "generic")
        callback_fn:   design.py callback function name (e.g. "my_gelu")

    Customization points:
        - For operators with extra parameters (e.g. alpha, trace_size), add
          dataclass fields and override _mlir_callback_args().
        - For operators requiring multiple kernels, extra compile flags, or
          external source files, override get_kernel_artifacts() directly.
        - For non-standard arg specs, override get_arg_spec() directly.
        - If none of these fit, subclass MLIROperator instead.
    """

    size: int
    num_aie_columns: int
    num_channels: int
    tile_size: int
    context: object = field(default=None, repr=False)

    kernel_name: ClassVar[str]
    kernel_subdir: ClassVar[str]
    callback_fn: ClassVar[str]

    def __post_init__(self) -> None:
        max_multiple = self.num_aie_columns * self.tile_size
        if self.size % max_multiple != 0:
            raise ValueError(
                f"size ({self.size}) must be a multiple of "
                f"num_aie_columns * tile_size ({max_multiple})"
            )
        total_shimdma_channels = self.num_aie_columns * self.num_channels
        if total_shimdma_channels > 16:
            raise ValueError(
                f"num_aie_columns * num_channels ({total_shimdma_channels}) "
                f"exceeds conservative ShimDMA limit of 16"
            )
        MLIROperator.__init__(self, context=self.context)

    def get_arg_spec(self) -> list[AIERuntimeArgSpec]:
        return [
            AIERuntimeArgSpec("in", (self.size,)),
            AIERuntimeArgSpec("out", (self.size,)),
        ]

    def _mlir_callback_args(self) -> list[Any]:
        """Return the callback_args list for PythonGeneratedMLIRArtifact.

        Subclasses with extra parameters (e.g. alpha, trace_size) should
        override this method.
        """
        return [
            aie_utils.DefaultNPURuntime.device(),
            self.size,
            self.num_aie_columns,
            self.num_channels,
            self.tile_size,
            0,
        ]

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                self.callback_fn,
                tuple(self._mlir_callback_args()),
            ),
        )

    def get_kernel_artifacts(self) -> list[KernelObjectArtifact]:
        return [
            KernelObjectArtifact(
                f"{self.kernel_name}.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir
                        / "aie_kernels"
                        / self.kernel_subdir
                        / f"{self.kernel_name}.cc"
                    )
                ],
            ),
        ]


@dataclass
class BinaryElementwiseOperator(MLIROperator):
    """Base class for binary element-wise AIE operators (two inputs, one output).

    Assumes a single kernel source file and a standard design.py callback
    with args [device, size, num_aie_columns, tile_size, trace_size].

    Unlike ChanneledUnaryOperator, binary operators have no explicit num_channels
    parameter — each core uses 2 DMA channels (one per input), so the ShimDMA
    limit is enforced as num_aie_columns * 2 <= 16.

    Subclasses must define three ClassVar attributes:
        kernel_name:   name of the kernel object file (e.g. "add" → add.o / add.cc)
        kernel_subdir: subdirectory under aie_kernels/ (e.g. "generic")
        callback_fn:   design.py callback function name (e.g. "my_eltwise_add")
    """

    size: int
    tile_size: int
    num_aie_columns: int = 8
    context: object = field(default=None, repr=False)

    kernel_name: ClassVar[str]
    kernel_subdir: ClassVar[str]
    callback_fn: ClassVar[str]
    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "num_aie_columns": "col",
    }

    def __post_init__(self) -> None:
        if self.size % (self.num_aie_columns * self.tile_size) != 0:
            raise ValueError(
                f"size ({self.size}) must be a multiple of "
                f"num_aie_columns * tile_size ({self.num_aie_columns * self.tile_size})"
            )
        total_shimdma_channels = self.num_aie_columns * 2
        if total_shimdma_channels > 16:
            raise ValueError(
                f"num_aie_columns ({self.num_aie_columns}) exceeds conservative ShimDMA limit"
            )
        MLIROperator.__init__(self, context=self.context)

    def get_arg_spec(self) -> list[AIERuntimeArgSpec]:
        return [
            AIERuntimeArgSpec("in", (self.size,)),
            AIERuntimeArgSpec("in", (self.size,)),
            AIERuntimeArgSpec("out", (self.size,)),
        ]

    def _mlir_callback_args(self) -> list[Any]:
        return [
            aie_utils.DefaultNPURuntime.device(),
            self.size,
            self.num_aie_columns,
            self.tile_size,
            0,
        ]

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                self.callback_fn,
                tuple(self._mlir_callback_args()),
            ),
        )

    def get_kernel_artifacts(self) -> list[KernelObjectArtifact]:
        return [
            KernelObjectArtifact(
                f"{self.kernel_name}.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir
                        / "aie_kernels"
                        / self.kernel_subdir
                        / f"{self.kernel_name}.cc"
                    )
                ],
            ),
        ]
