# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

import numpy as np

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
from iron.common.device_utils import get_kernel_dir
import aie.utils as aie_utils


@dataclass
class GEMM(MLIROperator):
    """AIE-accelerated General Matrix Multiplication (GEMM) layer.

    Supported integer data types: ``dtype_in="i8"`` / ``"i16"`` with
    ``dtype_out="i32"`` (the only bit-exact integer output — integer
    microkernels accumulate in 32 bits, and narrower outputs truncate and
    are rejected). ``dtype_in="bf16"`` with ``"bf16"`` or ``"f32"`` output
    is the default floating-point path.

    Known flake (XRT/amdxdna, not this operator): on NPU2 (Strix Halo) a
    dispatch can rarely (~5% per process) return a wrong result after
    several *distinct* xclbins have been compiled in one process — the
    zero/accumulate write races the first submit on a freshly-registered
    context. It self-heals on the next dispatch. The repo test harness
    already warms up and verifies; production callers should do the same
    (warm-up once, verify the first result, retry once on mismatch).
    """

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
    dtype_in: str = field(default="bf16")
    dtype_out: str = field(default="bf16")
    dtype_b: str = field(default="")
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

        # r/s/t MAC shapes per dtype (see microkernel_mac_dim_map in design.py).
        # The vectorized kernels static_assert m % (2*r) == 0, k % s == 0,
        # n % (2*t) == 0, so the tile must be a multiple of (2r, s, 2t).
        # Asymmetric INT4 weights (dtype_b="i4") use the AIE2P 4x16x16 shape:
        # K and N per MAC are 16 (2x int8xint8's density), so tile_k and
        # tile_n must be multiples of 16 and 32 respectively.
        if self.dtype_in == "i8" and self.dtype_b == "i4":
            r, s, t = 4, 16, 16
        elif self.dtype_in == "i8":
            r, s, t = 8, 8, 8
        elif self.dtype_in == "i16":
            r, s, t = 4, 4, 8
        elif self.emulate_bf16_mmul_with_bfp16:
            r, s, t = 8, 8, 8
        else:
            r, s, t = 4, 8, 8
        min_tile_m, min_tile_k, min_tile_n = 2 * r, s, 2 * t
        if (self.tile_m % min_tile_m) != 0 or (self.tile_k % min_tile_k) != 0 or (self.tile_n % min_tile_n) != 0:
            raise ValueError(
                f"tile sizes ({self.tile_m},{self.tile_k},{self.tile_n}) must be multiples of "
                f"({min_tile_m},{min_tile_k},{min_tile_n}) for dtype {self.dtype_in}"
            )

        # Integer microkernels accumulate in 32 bits (accauto resolves int8xint8
        # and int16xint16 to a 32-bit accumulator). Narrowing that accumulator
        # into a smaller output (i8->i8, i8->i16, i16->i16) silently truncates,
        # so only the exact 32-bit integer output is supported.
        if self.dtype_in in ("i8", "i16") and self.dtype_out != "i32":
            raise ValueError(
                f"dtype_out ({self.dtype_out}) for dtype_in={self.dtype_in} must be 'i32': "
                f"integer microkernels accumulate in 32 bits; narrower outputs truncate"
            )

        MLIROperator.__init__(self, context=self.context)

    @property
    def _kernel_flags_suffix(self):
        """Suffix encoding compile-time flags that affect the kernel binary."""
        return f"_{self.dtype_in}_{self.dtype_b or ''}_{self.dtype_out}_{int(self.prio_accuracy)}_{int(self.emulate_bf16_mmul_with_bfp16)}_{int(self.round_conv_even)}"

    @property
    def _kernel_dtype_flag(self) -> str:
        """Compile-time -D flag selecting the dtype combo in aie_kernels/**/mm.cc.

        The microkernel library instantiates extern-C entry points from a
        ``combos(X)`` list; exactly one ``*_ONLY`` define narrows it to a
        single (input, output) dtype pair so the object file exports only the
        symbols this operator references.

        With ``prio_accuracy`` the design accumulates in an internal f32 buffer
        and resolves the kernels as ``matmul_{dtype_in}_f32`` / ``zero_f32``
        (see design.py), so the kernel object must be built with the f32-output
        combo even though the user-visible output dtype stays bf16.
        """
        if self.prio_accuracy:
            if self.dtype_in != "bf16":
                raise ValueError(
                    f"prio_accuracy is only supported for dtype_in='bf16', got {self.dtype_in!r}"
                )
            return "bf16_f32_ONLY"
        if self.dtype_in == "i8" and self.dtype_b == "i4":
            return "i8_i4_ONLY"
        return {
            ("bf16", "bf16"): "bf16_bf16_ONLY",
            ("bf16", "f32"): "bf16_f32_ONLY",
            ("i8", "i32"): "i8_i32_ONLY",
            ("i16", "i32"): "i16_i32_ONLY",
        }[(self.dtype_in, self.dtype_out)]

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
                    "dtype_b_str": self.dtype_b,
                    "b_col_maj": int(self.b_col_maj),
                    "c_col_maj": int(self.c_col_maj),
                    "use_scalar": self.use_scalar,
                    "emulate_bf16_mmul_with_bfp16": self.emulate_bf16_mmul_with_bfp16,
                    "prio_accuracy": self.prio_accuracy,
                    "separate_c_tiles": int(self.separate_c_tiles),
                    "trace_size": 0,
                    "generate_taps": False,
                    "kernel_object": f"gemm_{self.tile_m}x{self.tile_k}x{self.tile_n}_{int(self.b_col_maj)}_{int(self.c_col_maj)}{self._kernel_flags_suffix}.o",
                },
            ),
        )

    def get_kernel_artifacts(self):
        base_dir = self.context.base_dir
        kernel_flags = [
            f"-DDIM_M={self.tile_m}",
            f"-DDIM_K={self.tile_k}",
            f"-DDIM_N={self.tile_n}",
        ]
        kernel_flags.append(f"-D{self._kernel_dtype_flag}")
        if self.dtype_in == "bf16" and self.emulate_bf16_mmul_with_bfp16:
            kernel_flags.append("-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16")
        if self.round_conv_even:
            kernel_flags.append("-DROUND_CONV_EVEN")
        if self.b_col_maj:
            kernel_flags.append("-DB_COL_MAJ")
        if self.c_col_maj:
            kernel_flags.append("-DC_COL_MAJ")

        kernel_dir = get_kernel_dir()
        return [
            KernelObjectArtifact(
                f"gemm_{self.tile_m}x{self.tile_k}x{self.tile_n}_{int(self.b_col_maj)}_{int(self.c_col_maj)}{self._kernel_flags_suffix}.o",
                extra_flags=kernel_flags,
                dependencies=[
                    SourceArtifact(base_dir / "aie_kernels" / kernel_dir / "mm.cc")
                ],
            ),
            KernelObjectArtifact(
                "convert_copy.o",
                [
                    SourceArtifact(
                        base_dir / "aie_kernels" / "generic" / "convert_copy.cc"
                    )
                ],
            ),
        ]

    def get_arg_spec(self):
        # B (weights) is passed packed for asymmetric INT4: (K, N//2) int8
        # storage, two nibbles per byte.
        b_n = self.N // 2 if self.dtype_b == "i4" else self.N
        return [
            AIERuntimeArgSpec("in", (self.M, self.K)),  # input A
            AIERuntimeArgSpec(
                "in", (self.K, b_n) if not self.b_col_maj else (b_n, self.K)
            ),  # input B (weights)
            AIERuntimeArgSpec(
                "out", (self.M, self.N) if not self.c_col_maj else (self.N, self.M)
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

    @staticmethod
    def pack_i4(B_np):
        """Pack an int8-valued (K, N) matrix into (K, N//2) int8 nibbles.

        For ``dtype_b="i4"`` the caller stores 4-bit weights in an int8
        array with values in [-8, 7]; this packs two nibbles per byte
        (low nibble first: byte = (b_lo & 0xf) | (b_hi << 4)) matching the
        kernel's int4 reinterpret. N must be even.

        NOTE: the asymmetric INT4 GEMM (A=i8, B=i4, 4x16x16 mmul on AIE2P)
        is bit-exact against a 32-bit reference for random and identity
        inputs. The one subtlety lives in the microkernel, not here: the AIE
        API's ``int4_t`` is an empty struct (``sizeof(int4) == 1``) although
        each element is really 4 bits, so manual pointer arithmetic on
        ``int4*`` (the j-block offset and the k-loop B advance) must halve
        the element counts to land on the true packed byte offsets. ``mm.cc``
        encodes this as ``B_ADV = size_B / 2`` for int4. With the corrected
        strides the L2->L1 B stream is plain k-block-major (16 blocks of
        16x16 int4) and the A stream is plain row-major, so no host-side
        permutation is needed; pack plain, low-nibble-first.
        """
        B_np = np.asarray(B_np, dtype=np.int8)
        K, N = B_np.shape
        if N % 2 != 0:
            raise ValueError(f"B N ({N}) must be even for INT4 packing")
        packed = np.zeros((K, N // 2), dtype=np.int8)
        packed[:, :] = (B_np[:, 0::2].astype(np.uint8) & 0x0F) | (
            (B_np[:, 1::2].astype(np.uint8) & 0x0F) << 4
        )
        return packed

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
            if self.dtype_b == "i4":
                B_parts[i] = self.pack_i4(B_parts[i])
        return B_parts
