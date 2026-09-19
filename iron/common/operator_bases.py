# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, ClassVar

import aie.utils as aie_utils

from .base import (
    MLIROperator,
    AIERuntimeArgSpec,
    same_shape_unary,
    same_shape_binary,
)
from .context import AIEContext
from .compilation import (
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
from .device_utils import get_kernel_dir, lut_sources
from .utils import get_shim_dma_limit


@dataclass
class ChanneledUnaryOperator(MLIROperator):
    """Base class for channeled unary AIE operators (single input, single output).

    Assumes a single kernel source file and a standard design.py callback
    with args [device, size, num_aie_columns, num_channels, tile_size, trace_size].

    Subclasses must define ClassVar attributes:
        kernel_name:   name of the kernel object file (e.g. "gelu" → gelu.o / gelu.cc)
        callback_fn:   design.py callback function name (e.g. "my_gelu")
        needs_lut_ops: set True for operators that require lut_based_ops.o on aie2

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
    context: AIEContext | None = field(default=None, repr=False)

    kernel_name: ClassVar[str]
    kernel_fn_name: ClassVar[str]
    callback_fn: ClassVar[str]
    needs_lut_ops: ClassVar[bool] = False
    tile_cap: ClassVar[int] = 4096

    def __post_init__(self) -> None:
        max_multiple = self.num_aie_columns * self.tile_size
        if self.size % max_multiple != 0:
            raise ValueError(
                f"size ({self.size}) must be a multiple of "
                f"num_aie_columns * tile_size ({max_multiple})"
            )
        dev = aie_utils.get_current_device()
        shim_dma_limit = get_shim_dma_limit(dev)
        total_shimdma_channels = self.num_aie_columns * self.num_channels
        if total_shimdma_channels > shim_dma_limit:
            raise ValueError(
                f"num_aie_columns * num_channels ({total_shimdma_channels}) "
                f"exceeds ShimDMA limit of {shim_dma_limit} for this device"
            )
        super().__init__(context=self.context)

    @staticmethod
    def arg_spec(size) -> list[AIERuntimeArgSpec]:
        return same_shape_unary(size)

    def _mlir_callback_args(self) -> list[Any]:
        """Return the callback_args list for PythonGeneratedMLIRArtifact.

        Retained for the operators that append an extra parameter and build
        their own artifact (axpy's scalar_factor, leaky_relu's alpha). The
        base itself binds by name instead.
        """
        return [
            aie_utils.get_current_device(),
            self.size,
            self.num_aie_columns,
            self.num_channels,
            self.tile_size,
            self.trace_size,
        ]

    @property
    def bundled_sources(self) -> tuple:
        """Translation units the kernel links but never calls through MLIR."""
        return lut_sources() if self.needs_lut_ops else ()

    @property
    def kernel_source(self):
        """The C++ source this operator's kernel is compiled from."""
        return self.context.kernels_dir / get_kernel_dir() / f"{self.kernel_name}.cc"

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        # Bound by name rather than passed by position. The old list matched
        # the design's signature by order alone, so inserting a parameter into
        # that signature shifted every argument after it silently.
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir.parent / "channeled_unary_design.py",
                "channeled_unary_design",
                bind_from=self,
            ),
        )

    def get_kernel_artifacts(self) -> list:
        # None: the design declares its kernel as an ExternalFunction, with any
        # lut tables compiled into the same translation unit.
        return []


@dataclass
class BinaryElementwiseOperator(MLIROperator):
    """Base class for binary element-wise AIE operators (two inputs, one output).

    Assumes a single kernel source file and a standard design.py callback
    with args [device, size, num_aie_columns, tile_size, trace_size].

    Unlike ChanneledUnaryOperator, binary operators have no explicit num_channels
    parameter — each core uses 2 DMA channels (one per input), so the ShimDMA
    limit is enforced as num_aie_columns * 2 <= 16.

    Subclasses must define ClassVar attributes:
        kernel_name:   name of the kernel object file (e.g. "add" → add.o / add.cc)
        kernel_subdir: subdirectory under aie_kernels/ (e.g. "generic")
        callback_fn:   design.py callback function name (e.g. "my_eltwise_add")
    """

    size: int
    tile_size: int
    num_aie_columns: int = 8
    context: AIEContext | None = field(default=None, repr=False)

    kernel_name: ClassVar[str]
    kernel_fn_name: ClassVar[str]
    kernel_subdir: ClassVar[str]
    callback_fn: ClassVar[str]
    # Override parent's "c" alias with "col" so binary-elementwise operator names
    # are unambiguous when num_aie_columns and num_channels both appear in the
    # name (the parent ChanneledUnaryOperator uses "c" for num_aie_columns).
    _name_aliases: ClassVar[dict[str, str]] = {
        **MLIROperator._name_aliases,
        "num_aie_columns": "col",  # intentionally overrides parent's "c" alias
    }

    def __post_init__(self) -> None:
        if self.size % (self.num_aie_columns * self.tile_size) != 0:
            raise ValueError(
                f"size ({self.size}) must be a multiple of "
                f"num_aie_columns * tile_size ({self.num_aie_columns * self.tile_size})"
            )
        dev = aie_utils.get_current_device()
        shim_dma_limit = get_shim_dma_limit(dev)
        # Binary operators use 2 ShimDMA channels per column (one per input).
        total_shimdma_channels = self.num_aie_columns * 2
        if total_shimdma_channels > shim_dma_limit:
            raise ValueError(
                f"num_aie_columns ({self.num_aie_columns}) exceeds ShimDMA limit "
                f"of {shim_dma_limit // 2} columns for this device"
            )
        super().__init__(context=self.context)

    @staticmethod
    def arg_spec(size) -> list[AIERuntimeArgSpec]:
        return same_shape_binary(size)

    def _mlir_callback_args(self) -> list[Any]:
        """Return the callback_args list for PythonGeneratedMLIRArtifact.

        Retained for axpy, which appends scalar_factor and builds its own
        artifact. The base itself binds by name instead.
        """
        return [
            aie_utils.get_current_device(),
            self.size,
            self.num_aie_columns,
            self.tile_size,
            self.trace_size,
        ]

    @property
    def kernel_source(self):
        """The C++ source this operator's kernel is compiled from."""
        return self.context.kernels_dir / get_kernel_dir() / f"{self.kernel_name}.cc"

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        # Bound by name; see the note on the unary base about position.
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir.parent / "binary_elementwise_design.py",
                "binary_elementwise_design",
                bind_from=self,
            ),
        )

    def get_kernel_artifacts(self) -> list:
        # The design declares its kernel as an ExternalFunction; nothing here
        # names the object a second time. No binary operator needs the aie2
        # lut archive, so unlike the unary base there is no prebuilt branch.
        return []
