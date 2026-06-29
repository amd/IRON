# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

import aie.utils as aie_utils
from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)


@dataclass
class Transpose(MLIROperator):
    """AIE-accelerated transpose operator.

    ``num_batches`` > 1 performs that many independent (M,N)->(N,M) transposes on
    contiguous matrices laid back-to-back in memory (results concatenated), mirroring
    GEMV's batching — the per-batch tile work rides the same ObjectFifos, so B batched
    transposes cost ONE dispatch instead of B unrolled ones.
    """

    M: int
    N: int
    num_aie_columns: int
    num_channels: int
    m: int
    n: int
    s: int
    num_batches: int = 1
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "num_batches": "batch",
    }

    def __post_init__(self):
        if self.M % self.m != 0:
            raise ValueError(f"Matrix rows ({self.M}) must be a multiple of {self.m}")
        if self.N % self.n != 0:
            raise ValueError(
                f"Matrix columns ({self.N}) must be a multiple of {self.n}"
            )
        if self.m % self.s != 0:
            raise ValueError(f"AIE tile rows ({self.m}) must be a multiple of {self.s}")
        if self.n % self.s != 0:
            raise ValueError(
                f"AIE tile columns ({self.n}) must be a multiple of {self.s}"
            )
        if (
            self.M
            * self.N
            % (self.m * self.n * self.num_aie_columns * self.num_channels)
            != 0
        ):
            raise ValueError(
                "Transfer size must be divisible by m*n*num_columns*num_channels"
            )
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "shuffle_transpose",
                (
                    aie_utils.get_current_device(),
                    self.M,
                    self.N,
                    self.num_aie_columns,
                    self.num_channels,
                    self.m,
                    self.n,
                    self.s,
                    self.num_batches,
                ),
            ),
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
        batch_dim = (self.num_batches,) if self.num_batches > 1 else ()
        return [
            AIERuntimeArgSpec("in", batch_dim + (self.M * self.N,)),
            AIERuntimeArgSpec("out", batch_dim + (self.N * self.M,)),
        ]
