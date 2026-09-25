# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, ClassVar

import aie.utils as aie_utils
from aie.iron.kernel import ExternalFunction

from .base import MLIROperator, AIERuntimeArgSpec
from .context import AIEContext
from .compilation import (
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
from .utils import get_shim_dma_limit


def lut_based_ops_artifacts(kernel_dir: str) -> list[KernelObjectArtifact]:
    """Return the lut_based_ops kernel artifact for aie2 devices, empty list otherwise."""
    if kernel_dir != "aie2":
        return []
    mlir_aie_dir = Path(aie_utils.config.root_path())
    return [
        KernelObjectArtifact(
            "lut_based_ops.o",
            dependencies=[
                SourceArtifact(
                    mlir_aie_dir / "aie_runtime_lib" / "AIE2" / "lut_based_ops.cpp"
                )
            ],
        )
    ]


@dataclass
class ChanneledUnaryOperator(MLIROperator):
    """Base class for channeled unary AIE operators (single input, single output).

    Assumes a single kernel and a standard design.py callback with args
    [device, size, num_aie_columns, num_channels, tile_size, trace_size].

    Subclasses must implement _kernel(), returning the mlir-aie kernel factory's
    ExternalFunction for one line of _line_size elements.

    Customization points:
        - For operators with extra parameters (e.g. alpha, trace_size), add
          dataclass fields and override _mlir_callback_args().
        - For non-standard arg specs, override get_arg_spec() directly.
        - If none of these fit, subclass MLIROperator instead.
    """

    size: int
    num_aie_columns: int
    num_channels: int
    tile_size: int
    context: AIEContext | None = field(default=None, repr=False)

    callback_fn: ClassVar[str]
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
            aie_utils.get_current_device(),
            self.size,
            self.num_aie_columns,
            self.num_channels,
            self.tile_size,
            0,
        ]

    @property
    def _line_size(self) -> int:
        """Elements each core processes per kernel call."""
        return min(self.tile_size, self.tile_cap)

    def _kernel(self) -> ExternalFunction:
        """The kernel each core runs over one line of _line_size elements."""
        raise NotImplementedError

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        callback_args = self._mlir_callback_args() + [self._kernel(), self.tile_cap]
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir.parent / "channeled_unary_design.py",
                "channeled_unary_design",
                tuple(callback_args),
            ),
        )

    def get_kernel_artifacts(self) -> list[KernelObjectArtifact]:
        return [KernelObjectArtifact.from_extern(self._kernel())]


@dataclass
class BinaryElementwiseOperator(MLIROperator):
    """Base class for binary element-wise AIE operators (two inputs, one output).

    Assumes a single kernel and a standard design.py callback with args
    [device, size, num_aie_columns, tile_size, trace_size].

    Unlike ChanneledUnaryOperator, binary operators have no explicit num_channels
    parameter — each core uses 2 DMA channels (one per input), so the ShimDMA
    limit is enforced as num_aie_columns * 2 <= 16.

    Subclasses must implement _kernel(), returning the mlir-aie kernel factory's
    ExternalFunction for one tile of _tile_elements elements.
    """

    size: int
    tile_size: int
    num_aie_columns: int = 8
    context: AIEContext | None = field(default=None, repr=False)

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

    def get_arg_spec(self) -> list[AIERuntimeArgSpec]:
        return [
            AIERuntimeArgSpec("in", (self.size,)),
            AIERuntimeArgSpec("in", (self.size,)),
            AIERuntimeArgSpec("out", (self.size,)),
        ]

    def _mlir_callback_args(self) -> list[Any]:
        """Return the callback_args list for PythonGeneratedMLIRArtifact.

        Subclasses with extra parameters (e.g. scalar_factor) should
        override this method.
        """
        return [
            aie_utils.get_current_device(),
            self.size,
            self.num_aie_columns,
            self.tile_size,
            0,
        ]

    @property
    def _tile_elements(self) -> int:
        """Elements each core processes per kernel call."""
        return min(self.tile_size, 4096)

    def _kernel(self) -> ExternalFunction:
        """The kernel each core runs over one tile of _tile_elements elements."""
        raise NotImplementedError

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        callback_args = self._mlir_callback_args() + [self._kernel()]
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir.parent / "binary_elementwise_design.py",
                "binary_elementwise_design",
                tuple(callback_args),
            ),
        )

    def get_kernel_artifacts(self) -> list[KernelObjectArtifact]:
        return [KernelObjectArtifact.from_extern(self._kernel())]
