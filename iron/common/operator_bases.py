# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, ClassVar

import aie.utils as aie_utils

from .base import MLIROperator, AIERuntimeArgSpec
from .context import AIEContext
from .compilation import (
    KernelArchiveArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
from .device_utils import get_kernel_dir
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
    def _kernel_link_file(self) -> str:
        """The file name that the MLIR Kernel declaration should link_with.

        When auxiliary objects are required (e.g. lut_based_ops.o on aie2),
        all objects are bundled into an archive and the archive name is
        returned so that aiecc links the entire archive.
        """
        if self.needs_lut_ops and get_kernel_dir() == "aie2":
            return f"{self.name}_kernels.a"
        return f"{self.kernel_name}.o"

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        callback_args = self._mlir_callback_args() + [
            self.kernel_fn_name,
            self._kernel_link_file,
            self.tile_cap,
        ]
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir.parent / "channeled_unary_design.py",
                "channeled_unary_design",
                tuple(callback_args),
            ),
        )

    def get_kernel_artifacts(self) -> list:
        dev = aie_utils.get_current_device()
        kernel_dir = get_kernel_dir(dev)
        kernel_obj = KernelObjectArtifact(
            f"{self.kernel_name}.o",
            dependencies=[
                SourceArtifact(
                    self.context.base_dir
                    / "aie_kernels"
                    / kernel_dir
                    / f"{self.kernel_name}.cc"
                )
            ],
        )
        if self.needs_lut_ops and kernel_dir == "aie2":
            lut_objs = lut_based_ops_artifacts(kernel_dir)
            return [
                KernelArchiveArtifact(
                    f"{self.name}_kernels.a",
                    dependencies=[kernel_obj] + lut_objs,
                )
            ]
        return [kernel_obj]


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

    def get_mlir_artifact(self) -> PythonGeneratedMLIRArtifact:
        callback_args = self._mlir_callback_args() + [
            self.kernel_fn_name,
            f"{self.kernel_name}.o",
        ]
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir.parent / "binary_elementwise_design.py",
                "binary_elementwise_design",
                tuple(callback_args),
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
