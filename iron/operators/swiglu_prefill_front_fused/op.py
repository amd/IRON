# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

import numpy as np

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
from iron.common.device_utils import get_kernel_dir
from iron.common.operator_bases import lut_based_ops_artifacts
import aie.utils as aie_utils


@dataclass
class SwigluFrontFused(MLIROperator):
    """AIE-accelerated General Matrix Multiplication (GEMM) layer"""

    M: int
    K: int
    N: int
    tile_m: int = 64
    tile_k: int = 64
    tile_n: int = 64
    num_aie_columns: int = field(default=8)
    emulate_bf16_mmul_with_bfp16: bool = field(default=True, repr=False)
    prio_accuracy: bool = field(default=False, repr=False)
    round_conv_even: bool = field(default=True, repr=False)
    dtype_in: str = field(default="bf16", repr=False)
    dtype_out: str = field(default="bf16", repr=False)
    use_scalar: bool = field(default=False, repr=False)
    separate_c_tiles: bool = field(default=False, repr=False)
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "tile_m": "tm",
        "tile_k": "tk",
        "tile_n": "tn",
        "b_col_maj": "bc",
        "c_col_maj": "cc",
    }

    def __post_init__(self):
        num_aie_rows = 4
        min_M = self.tile_m * num_aie_rows
        min_K = self.tile_k
        min_N = self.tile_n * self.num_aie_columns
        if self.M % min_M != 0:
            raise ValueError(f"M ({self.M}) must be a multiple of {min_M}")
        if self.K % min_K != 0:
            raise ValueError(f"K ({self.K}) must be a multiple of {min_K}")
        if self.N % min_N != 0:
            raise ValueError(f"N ({self.N}) must be a multiple of {min_N}")

        if self.emulate_bf16_mmul_with_bfp16:
            min_tile_m, min_tile_k, min_tile_n = 8, 8, 8
        else:
            min_tile_m, min_tile_k, min_tile_n = 4, 8, 8
        if self.tile_m < min_tile_m:
            raise ValueError(f"tile_m ({self.tile_m}) must be >= {min_tile_m}")
        if self.tile_k < min_tile_k:
            raise ValueError(f"tile_k ({self.tile_k}) must be >= {min_tile_k}")
        if self.tile_n < min_tile_n:
            raise ValueError(f"tile_n ({self.tile_n}) must be >= {min_tile_n}")

        MLIROperator.__init__(self, context=self.context)

    @property
    def _kernel_flags_suffix(self):
        """Suffix encoding compile-time flags that affect the kernel binary."""
        return f"_{int(self.prio_accuracy)}_{int(self.emulate_bf16_mmul_with_bfp16)}_{int(self.round_conv_even)}"

    def get_mlir_artifact(self):
        kernel_tile_n = 2 * self.tile_n
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "my_swiglu_fused",
                (),
                {
                    "dev": aie_utils.get_current_device(),
                    "M": self.M,
                    "K": self.K,
                    "N": self.N,
                    "m": self.tile_m,
                    "k": self.tile_k,
                    "n": self.tile_n,
                    "n_aie_cols": self.num_aie_columns,
                    "dtype_in_str": self.dtype_in,
                    "dtype_out_str": self.dtype_out,
                    "use_scalar": self.use_scalar,
                    "emulate_bf16_mmul_with_bfp16": self.emulate_bf16_mmul_with_bfp16,
                    "prio_accuracy": self.prio_accuracy,
                    "separate_c_tiles": int(self.separate_c_tiles),
                    "trace_size": 0,
                    "generate_taps": False,
                    "kernel_object": f"gemm_{self.tile_m}x{self.tile_k}x{kernel_tile_n}{self._kernel_flags_suffix}.o",
                },
            ),
        )

    def get_kernel_artifacts(self):
        base_dir = self.context.base_dir
        kernel_dir = get_kernel_dir()
        kernel_tile_n = 2 * self.tile_n
        kernel_flags = [
            f"-DDIM_M={self.tile_m}",
            f"-DDIM_K={self.tile_k}",
            f"-DDIM_N={kernel_tile_n}",
        ]
        if self.prio_accuracy:
            kernel_flags.append("-Dbf16_f32_ONLY")
        else:
            kernel_flags.append("-Dbf16_bf16_ONLY")
        if self.round_conv_even:
            kernel_flags.append("-DROUND_CONV_EVEN")
        if self.emulate_bf16_mmul_with_bfp16:
            kernel_flags.append("-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16")

        artifacts = [
            KernelObjectArtifact(
                f"gemm_{self.tile_m}x{self.tile_k}x{kernel_tile_n}{self._kernel_flags_suffix}.o",
                extra_flags=kernel_flags,
                dependencies=[
                    SourceArtifact(base_dir / "aie_kernels" / kernel_dir / "mm.cc")
                ],
            ),
        ]
        swiglu_obj = KernelObjectArtifact(
            "swiglu.o",
            dependencies=[
                SourceArtifact(base_dir / "aie_kernels" / kernel_dir / "silu.cc")
            ],
        )
        lut_objs = lut_based_ops_artifacts(kernel_dir)
        if lut_objs:
            artifacts.append(
                KernelArchiveArtifact(
                    "swiglu_kernels.a",
                    dependencies=[swiglu_obj] + lut_objs,
                )
            )
        else:
            artifacts.append(swiglu_obj)
        return artifacts

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.M, self.K)),  # input A
            AIERuntimeArgSpec("in", (2 * self.K * self.N,)),  # packed weights
            AIERuntimeArgSpec("out", (self.M, self.N)),  # output C
        ]

    def reference(self, A, B):
        """CPU reference: ``SiLU(A @ B_gate) * (A @ B_up)``."""
        from iron.operators.swiglu_prefill_front_fused.reference import reference

        return reference(
            A,
            B,
            self.K,
            self.N,
            self.tile_k,
            self.tile_n,
            self.num_aie_columns,
        )

