# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIETranspose(MLIROperator):
    """AIE-accelerated transpose operator"""

    def __init__(self, M, N, num_aie_columns, num_channels, m, n, s, context=None):
        assert M % m == 0, f"Matrix rows ({M}) must be a multiple of {m}"
        assert N % n == 0, f"Matrix columns ({N}) must be a multiple of {n}"
        assert m % s == 0, f"AIE tile rows ({m}) must be a multiple of {s}"
        assert n % s == 0, f"AIE tile columns ({n}) must be a multiple of {s}"
        assert (
            M * N % (m * n * num_aie_columns * num_channels) == 0
        ), "Transfer size must be divisible by m*n*num_columns*num_channels"

        self.M = M
        self.N = N
        self.m = m
        self.n = n
        self.s = s
        self.num_columns = num_aie_columns
        self.num_channels = num_channels

        super().__init__(context=context)

    def get_operator_name(self):
        return f"transpose_{self.num_columns}c_{self.num_channels}ch_{self.M}x{self.N}_{self.m}x{self.n}_{self.s}s"

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=operator_dir / "design.py",
            callback_fn="shuffle_transpose",
            callback_args=[
                self.context.device_manager.device_type,
                self.M,
                self.N,
                self.num_columns,
                self.num_channels,
                self.m,
                self.n,
                self.s,
            ],
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                f"transpose_{self.m}x{self.n}.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir
                        / "aie_kernels"
                        / "generic"
                        / "transpose.cc"
                    )
                ],
                extra_flags=[
                    f"-DDIM_m={self.m}",
                    f"-DDIM_n={self.n}",
                ],
            ),
        ]

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.M * self.N,)),  # input
            AIERuntimeArgSpec("out", (self.M * self.N,)),  # output (transposed)
        ]
