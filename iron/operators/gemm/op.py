# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

import numpy as np

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
from aie.iron import str_to_dtype
from aie.iron.kernels import datamovement, linalg, zero
import aie.utils as aie_utils


@dataclass
class GEMM(MLIROperator):
    """AIE-accelerated General Matrix Multiplication (GEMM) layer"""

    M: int
    K: int
    N: int
    tile_m: int = 64
    tile_k: int = 64
    tile_n: int = 64
    b_col_maj: bool = False
    c_col_maj: bool = False
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

        # r, s, t are the aie::mmul tile dims the bf16 kernel is built from
        # (aie_kernels/aie2p/mm.cc, matmul_vectorized_2x2_mmul)
        if self.emulate_bf16_mmul_with_bfp16:
            r, s, t = 8, 8, 8
        else:
            r, s, t = 4, 8, 8
        min_tile_m, min_tile_k, min_tile_n = 2 * r, s, 2 * t
        if self.tile_m % min_tile_m != 0:
            raise ValueError(
                f"tile_m ({self.tile_m}) must be a multiple of {min_tile_m} "
                f"(aie_kernels/aie2p/mm.cc requires m % (2*r) == 0, r={r})"
            )
        if self.tile_k % min_tile_k != 0:
            raise ValueError(
                f"tile_k ({self.tile_k}) must be a multiple of {min_tile_k} "
                f"(aie_kernels/aie2p/mm.cc requires k % s == 0, s={s})"
            )
        if self.tile_n % min_tile_n != 0:
            raise ValueError(
                f"tile_n ({self.tile_n}) must be a multiple of {min_tile_n} "
                f"(aie_kernels/aie2p/mm.cc requires n % (2*t) == 0, t={t})"
            )

        MLIROperator.__init__(self, context=self.context)

    def _kernels(self):
        """The matmul, the zero that clears its accumulator and, under
        prio_accuracy, the f32 -> bf16 copy out of that accumulator.

        prio_accuracy accumulates in f32 in L1 and converts on the way out, so
        the matmul's C, and the buffer that gets zeroed, are f32 even when C
        is bf16.
        """
        use_chess = self.context.compiler == "chess"
        dtype_acc = np.float32 if self.prio_accuracy else str_to_dtype(self.dtype_out)
        kernels = {
            "matmul_kernel": linalg.mm(
                self.tile_m,
                self.tile_k,
                self.tile_n,
                input_dtype=str_to_dtype(self.dtype_in),
                output_dtype=dtype_acc,
                vectorized=not self.use_scalar,
                b_col_maj=self.b_col_maj,
                c_col_maj=self.c_col_maj,
                use_chess=use_chess,
                emulate_bf16_mmul_with_bfp16=self.emulate_bf16_mmul_with_bfp16,
                round_conv_even=self.round_conv_even,
            ),
            "zero_kernel": zero(
                self.tile_m * self.tile_n,
                dtype_acc,
                vectorized=not self.use_scalar,
                use_chess=use_chess,
            ),
        }
        if self.prio_accuracy:
            kernels["convert_copy_kernel"] = datamovement.convert_copy(
                self.tile_m * self.tile_n
            )
        return kernels

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "my_matmul",
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
                    "b_col_maj": int(self.b_col_maj),
                    "c_col_maj": int(self.c_col_maj),
                    "use_scalar": self.use_scalar,
                    "emulate_bf16_mmul_with_bfp16": self.emulate_bf16_mmul_with_bfp16,
                    "prio_accuracy": self.prio_accuracy,
                    "separate_c_tiles": int(self.separate_c_tiles),
                    "trace_size": 0,
                    **self._kernels(),
                },
            ),
        )

    def get_kernel_artifacts(self):
        return [KernelObjectArtifact.from_extern(k) for k in self._kernels().values()]

    def get_arg_spec(self):
        dtype_in = str_to_dtype(self.dtype_in)
        dtype_out = str_to_dtype(self.dtype_out)
        return [
            AIERuntimeArgSpec("in", (self.M, self.K), dtype=dtype_in),  # input A
            AIERuntimeArgSpec(
                "in",
                (self.K, self.N) if not self.b_col_maj else (self.N, self.K),
                dtype=dtype_in,
            ),  # input B (weights)
            AIERuntimeArgSpec(
                "out",
                (self.M, self.N) if not self.c_col_maj else (self.N, self.M),
                dtype=dtype_out,
            ),  # output C
        ]

    def reference(self, A, B):
        """CPU reference: ``C = A @ B`` honoring ``b_col_maj`` / ``c_col_maj``."""
        from iron.operators.gemm.reference import reference

        return reference(A, B, self.b_col_maj, self.c_col_maj)

    def pad_A(self, A_np):
        """Pad A matrix to match operator dimensions (M, K)"""
        M, K = A_np.shape
        if M > self.M:
            raise ValueError(f"A rows ({M}) exceeds operator M ({self.M})")
        if M == self.M and K == self.K:
            return A_np

        M_padded = ((M + self.M - 1) // self.M) * self.M
        A_padded = np.zeros((M_padded, self.K), dtype=A_np.dtype)
        A_padded[:M, :K] = A_np
        return A_padded

    def pad_B(self, B_np):
        """Pad B matrix to match operator dimensions based on layout"""
        if self.b_col_maj:
            N, K = B_np.shape
            if N > self.N or K > self.K:
                raise ValueError(
                    f"B (col-major) shape ({N}, {K}) exceeds operator N ({self.N}), K ({self.K})"
                )
            if N == self.N and K == self.K:
                return B_np
            B_padded = np.zeros((self.N, self.K), dtype=B_np.dtype)
            B_padded[:N, :K] = B_np
        else:
            K, N = B_np.shape
            if N > self.N or K > self.K:
                raise ValueError(
                    f"B (row-major) shape ({K}, {N}) exceeds operator K ({self.K}), N ({self.N})"
                )
            if K == self.K and N == self.N:
                return B_np
            B_padded = np.zeros((self.K, self.N), dtype=B_np.dtype)
            B_padded[:K, :N] = B_np
        return B_padded

    def partition_B(self, B, partition_N):
        B_parts = [None] * partition_N
        if B is None:
            return B_parts
        for i in range(partition_N):
            col_start = i * self.N
            col_end = (i + 1) * self.N

            if self.b_col_maj:
                B_parts[i] = self.pad_B(B[col_start:col_end, :])
            else:
                B_parts[i] = self.pad_B(B[:, col_start:col_end])
        return B_parts
