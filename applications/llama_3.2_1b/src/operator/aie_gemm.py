# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
import logging

from .aie_base import AIEOperatorBase, AIEOperatorConstraintError
from ..compilation import (
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from ..utils import torch_to_numpy, numpy_to_torch


class AIEGEMM(AIEOperatorBase):
    """AIE-accelerated General Matrix Multiplication (GEMM) layer"""

    def __init__(
        self,
        M,
        K,
        N,
        use_static_weight=False,
        tile_m=64,
        tile_k=64,
        tile_n=64,
        num_columns=8,
        do_set_up=True,
        **gemm_kwargs,
    ):

        min_tile_m, min_tile_k, min_tile_n = 4, 8, 8
        assert tile_m >= min_tile_m, f"tile_m ({tile_m}) must be >= {min_tile_m}"
        assert tile_k >= min_tile_k, f"tile_k ({tile_k}) must be >= {min_tile_k}"
        assert tile_n >= min_tile_n, f"tile_n ({tile_n}) must be >= {min_tile_n}"
        assert tile_k & (tile_k - 1) == 0, f"tile_k ({tile_k}) must be power of 2"
        assert tile_n & (tile_n - 1) == 0, f"tile_n ({tile_n}) must be power of 2"

        self.tile_m = tile_m
        self.tile_k = tile_k
        self.tile_n = tile_n
        self.num_columns = num_columns
        self.n_aie_rows = 4
        self.gemm_args = gemm_kwargs
        self.weight = (
            None
            if not use_static_weight
            else torch.zeros((K, N), dtype=torch.bfloat16).T
        )
        self.weight = (
            None
            if not use_static_weight
            else torch.zeros((K, N), dtype=torch.bfloat16).T
        )

        # The operator's M, K, N represent what the NPU operator supports.
        # Calls to forward() may supply matrices of different sizes, and the
        # Python code will perform necessary padding/repeated application of
        # the NPU operator.
        M_padded, K_padded, N_padded = self._get_padded_dims(M, K, N)
        self.M = M_padded
        self.K = K_padded
        self.N = N_padded

        self.do_set_up = do_set_up

        AIEOperatorBase.__init__(self)

    def get_artifacts(self, prefix="gemm_"):
        # Get parameters from self
        tile_m = self.tile_m
        tile_k = self.tile_k
        tile_n = self.tile_n
        M = self.M
        K = self.K
        N = self.N
        num_columns = self.num_columns
        base_dir = self.base_dir
        device_str = self.device_manager.device_str()

        b_col_maj = self.gemm_args.get("b_col_maj", False)
        c_col_maj = self.gemm_args.get("c_col_maj", False)
        dtype_in = self.gemm_args.get("dtype_in", "bf16")
        dtype_out = self.gemm_args.get("dtype_out", "bf16")
        emulate_bf16_mmul_with_bfp16 = self.gemm_args.get(
            "emulate_bf16_mmul_with_bfp16", False
        )
        prio_accuracy = self.gemm_args.get("prio_accuracy", True)
        use_scalar = self.gemm_args.get("use_scalar", False)
        bf16_f32_only = self.gemm_args.get("bf16_f32_only", True)
        round_conv_even = self.gemm_args.get("round_conv_even", True)

        file_name_tile_base = f"{prefix}{tile_m}x{tile_k}x{tile_n}"
        file_name_total_base = f"{prefix}{M}x{K}x{N}_{tile_m}x{tile_k}x{tile_n}"
        xclbin_kernel_name = f"gemm_{file_name_tile_base}"
        kernel_flags = [
            f"-DDIM_M={tile_m}",
            f"-DDIM_K={tile_k}",
            f"-DDIM_N={tile_n}",
        ]
        if bf16_f32_only:
            kernel_flags.append("-Dbf16_f32_ONLY")
        if round_conv_even:
            kernel_flags.append("-DROUND_CONV_EVEN")
        # FIXME: I believe the emulate_bf16_mmul_with_bfp16 flag should be added to the kernel flags here as well

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_total_base}.mlir",
            import_path=base_dir / "example" / "gemm" / "gemm.py",
            callback_fn="my_matmul",
            callback_kwargs={
                "dev": device_str,
                "M": M,
                "K": K,
                "N": N,
                "m": tile_m,
                "k": tile_k,
                "n": tile_n,
                "n_aie_cols": num_columns,
                "dtype_in_str": dtype_in,
                "dtype_out_str": dtype_out,
                "b_col_maj": b_col_maj,
                "c_col_maj": c_col_maj,
                "use_scalar": use_scalar,
                "emulate_bf16_mmul_with_bfp16": emulate_bf16_mmul_with_bfp16,
                "prio_accuracy": prio_accuracy,
                "trace_size": 0,
                "generate_taps": False,
            },
            requires_context=True,
        )

        # FIXME: We should be able to reuse the same xclbin for same tile
        # sizes, only swapping out the instruction sequence for different
        # problem sizes. However, there seem to be cases where this does
        # not work and the GEMM appears to be misconfigured for the wrong
        # size (resulting in a timeout when trying to run it). Perhaps
        # XRT is caching something, or something is wrong with the run-
        # time parameter (synchronization)? For now, create separate
        # xclbins for each problem size.
        xclbin_artifact = XclbinArtifact.new(
            f"{file_name_total_base}.xclbin",
            depends=[
                mlir_artifact,
                KernelArchiveArtifact.new(
                    f"gemm_{tile_m}x{tile_k}x{tile_n}_archive.a",
                    depends=[
                        KernelObjectArtifact.new(
                            f"gemm_{tile_m}x{tile_k}x{tile_n}.o",
                            extra_flags=kernel_flags,
                            depends=[SourceArtifact.new("aie_kernels/aie2p/mm.cc")],
                        ),
                        KernelObjectArtifact.new(
                            "convert_copy.o",
                            [SourceArtifact.new("aie_kernels/generic/convert_copy.cc")],
                        ),
                    ],
                ),
            ],
            extra_flags=["--dynamic-objFifos"],
        )

        insts_artifact = InstsBinArtifact.new(
            f"{file_name_total_base}.bin",
            depends=[mlir_artifact],
            extra_flags=["--dynamic-objFifos"],
        )

        return (xclbin_artifact, insts_artifact)

    def set_up(self):
        # If this operator is only used as a sub-operator in another operator that sets it up, we should skip the setup here as those artifacts and buffers may not be needed.
        if not self.do_set_up:
            return
        # Describe required artifacts (xclbin, insts.bin)
        device_str = self.device_manager.device_str()
        xclbin_artifact, insts_artifact = self.get_artifacts()
        self.add_artifacts([xclbin_artifact, insts_artifact])

        # Describe runtime components
        # The static weights might not yet be loaded upon initialization; therefore, the provided self.static_weights field is a callback that provides the weights at set-up time.
        static_weights = None
        if self.weight is not None:
            static_weights = self.weight.T
            if isinstance(static_weights, torch.Tensor):
                static_weights = torch_to_numpy(static_weights)
        self.add_kernel(
            "gemm", xclbin_artifact, xclbin_artifact.kernel_name, insts_artifact
        )
        self.add_buffer("A", self.M * self.K)
        self.add_buffer("B", self.K * self.N, static_data=static_weights)
        self.add_buffer("C", self.M * self.N)
        self.add_to_runlist("gemm", "A", "B", "C")

    def forward(self, A, B=None):
        """Forward pass through GEMM operation: C = A @ B"""
        B_shape = B.shape if B is not None else self.weight.T.shape
        expected_output_shape = A.shape[:-1] + (B_shape[-1],)

        # Remove batch dimension, if any
        if len(A.shape) > 2:
            A = A.view(-1, A.shape[-1])
        if B is not None and len(B.shape) > 2:
            B = B.view(-1, B_shape[-1])

        M, K = A.shape
        K2, N = B_shape

        applicable = (
            K == K2
            and (M <= self.M or not self.c_col_maj)
            and K <= self.K
            and N <= self.N
        )
        if not applicable:
            raise AIEOperatorConstraintError("AIEGEMM: incompatible tensor shape(s)")

        A_padded = self._pad_A(torch_to_numpy(A))
        if B is not None:
            B_padded = self._pad_B(torch_to_numpy(B))
        else:
            B_padded = None

        logging.debug(
            f"Executing GEMM for dimensions M={M}, K={K}, N={N} using NPU operator with M={self.M}, K={self.N}, N={self.N}"
        )

        result_padded = np.zeros((M, self.N), dtype=A_padded.dtype)
        for M_lo in range(0, M, self.M):
            A_part = A_padded[M_lo : M_lo + self.M, :]
            result_part = self._execute_aie_operation(A_part, B_padded)
            max_M = min(M_lo + self.M, M)
            result_padded[M_lo:max_M, :] = result_part[:max_M, :]

        # GEMM produces 2D result, reshape to expected output shape
        result = numpy_to_torch(result_padded[:M, :N])
        result = result.view(expected_output_shape)

        return result

    def _get_padded_dims(self, M, K, N):
        tile_m, tile_k, tile_n = self.tile_m, self.tile_n, self.tile_k
        num_columns = self.num_columns

        min_M = tile_m * self.n_aie_rows
        min_K = tile_k
        min_N = tile_n * num_columns

        # Calculate padded dimensions
        M_padded = ((M + min_M - 1) // min_M) * min_M
        K_padded = ((K + min_K - 1) // min_K) * min_K
        N_padded = ((N + min_N - 1) // min_N) * min_N

        return M_padded, K_padded, N_padded

    def _pad_A(self, A_np):
        M, K = A_np.shape
        A_padded = A_np
        if M % self.M != 0 or K != self.K:
            M_multiple = (M + self.M - 1) // self.M * self.M
            A_padded = np.zeros((M_multiple, self.K), dtype=A_np.dtype)
            A_padded[:M, :K] = A_np
        return A_padded

    def _pad_B(self, B_np):
        K, N = B_np.shape
        B_padded = B_np
        if K != self.K or N != self.N:
            B_padded = np.zeros((self.K, self.N), dtype=B_np.dtype)
            B_padded[:K, :N] = B_np
        return B_padded

    def _execute_aie_operation(self, A_np, B_np=None):
        """Execute GEMM operation on AIE hardware"""
        M, K = A_np.shape
        K2, N = B_np.shape if B_np is not None else self.weight.T.shape

        # If M is larger than kernel supports, split large GEMMs with many rows
        # into multiple invocations of the kernel. This is only supported for
        # row-wise concatenation of output in row-major order.
        assert M == self.M
        assert K == K2 and K == self.K
        assert N == self.N

        self.write_buffer("A", A_np)
        if B_np is not None:
            self.write_buffer("B", B_np)
        self.run_runlist()
        result_np = self.read_buffer("C", shape=(M, N), dtype=bfloat16)

        # Check for NaN and fail hard
        if np.isnan(result_np).any():
            nan_count = np.isnan(result_np).sum()
            total_count = result_np.size
            raise RuntimeError(
                f"AIE execution returned {nan_count}/{total_count} NaN values. "
            )

        # Convert back to torch tensor
        return result_np
