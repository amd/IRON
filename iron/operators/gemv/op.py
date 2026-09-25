# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

import numpy as np
from ml_dtypes import bfloat16

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
import aie.utils as aie_utils
from aie.iron.kernels import activation, linalg
from iron.common.device_utils import get_kernel_dir


@dataclass
class GEMV(MLIROperator):
    """AIE-accelerated General Matrix-Vector/Vector-Matrix Multiplication layer"""

    M: int
    K: int
    num_aie_columns: int = 1
    tile_size_input: int = 2
    tile_size_output: int | None = None
    num_batches: int = 1
    kernel_vector_size: int = field(default=64, repr=False)
    # Optional fused activation applied to each output tile in the producing core.
    # "none" (default) leaves the output unchanged; "gelu" applies GELU(tanh approx).
    # repr=False keeps operator/artifact names stable for the default path.
    epilogue: str = field(default="none", repr=False)
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "num_aie_columns": "col",
        "tile_size_input": "tsi",
        "tile_size_output": "tso",
        "num_batches": "batch",
    }

    def __post_init__(self):
        if self.tile_size_output is None:
            self.tile_size_output = self.tile_size_input

        if not (
            self.tile_size_output % self.tile_size_input == 0
            and self.tile_size_output >= self.tile_size_input
        ):
            raise ValueError("tile_size_output must be a multiple of tile_size_input")
        # mv.cc pipelines the k loop on the assumption that it runs at least
        # twice, so VEC_SIZE has to divide K at least twice over. Narrow the
        # vector instead of refusing the shape: llama's attention-scores GEMV
        # has K = head_dim = 64, which the 64-wide default cannot serve.
        while self.kernel_vector_size > 16 and self.K < 2 * self.kernel_vector_size:
            self.kernel_vector_size //= 2
        if self.K % self.kernel_vector_size or self.K < 2 * self.kernel_vector_size:
            raise ValueError(
                f"K ({self.K}) must be a multiple of kernel_vector_size "
                f"({self.kernel_vector_size}) and at least twice as large"
            )
        if self.epilogue not in ("none", "gelu"):
            raise ValueError(
                f"unknown epilogue {self.epilogue!r} (expected 'none' or 'gelu')"
            )
        if self.epilogue == "gelu" and self.tile_size_output % 16 != 0:
            raise ValueError(
                f"gelu epilogue needs tile_size_output % 16 == 0 (got {self.tile_size_output})"
            )

        MLIROperator.__init__(self, context=self.context)

    @property
    def name(self) -> str:
        # epilogue is repr=False so the default path keeps a stable name, but the fused
        # variant must not share an artifact name with the plain GEMV of the same shape:
        # both would emit the same .mlir/.xclbin, and in a shared build dir a cached unfused
        # build can then satisfy the fused op (running the raw matvec with no activation).
        base = super().name
        if self.epilogue == "none":
            return base
        return f"{base}_epi{self.epilogue}"

    def _matvec(self):
        return linalg.mv(
            self.tile_size_input,
            self.K,
            bfloat16,
            bfloat16,
            vec_size=self.kernel_vector_size,
            output_rows=self.tile_size_output,
            use_chess=self.context.compiler == "chess",
        )

    def _gelu(self):
        # The epilogue is gelu.cc's in-place gelu_tile_bf16, which only
        # gelu_aie2p.h provides; it rides in the object the gelu factory builds.
        if get_kernel_dir() != "aie2p":
            raise NotImplementedError(
                "gemv gelu epilogue is only available on NPU2 (aie2p); "
                f"current kernel dir is {get_kernel_dir()!r}"
            )
        return activation.gelu()

    def get_mlir_artifact(self):
        mlir_verbose = getattr(self.context, "mlir_verbose", False)
        epilogue_fn = None
        if self.epilogue == "gelu":
            epilogue_fn = self._gelu().object_file.bind(
                "gelu_tile_bf16",
                [np.int32, np.ndarray[(self.tile_size_output,), np.dtype[bfloat16]]],
            )

        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "my_matvec",
                (
                    aie_utils.get_current_device(),
                    self.num_aie_columns,
                    self.M,
                    self.K,
                    self.tile_size_input,
                    self.tile_size_output,
                    self.num_batches,
                ),
                {
                    "verbose": mlir_verbose,
                    "matvec_fn": self._matvec(),
                    "epilogue_fn": epilogue_fn,
                },
            ),
        )

    def get_kernel_artifacts(self):
        fns = [self._matvec()]
        if self.epilogue == "gelu":
            fns.append(self._gelu())
        return [KernelObjectArtifact.from_extern(fn) for fn in fns]

    def get_arg_spec(self):
        batch_dim = (self.num_batches,) if self.num_batches > 1 else ()
        return [
            AIERuntimeArgSpec("in", batch_dim + (self.M, self.K)),  # matrix
            AIERuntimeArgSpec("in", batch_dim + (self.K,)),  # vector
            AIERuntimeArgSpec("out", batch_dim + (self.M,)),  # output
        ]

    def reference(self, A, B):
        """CPU reference: (optionally batched) matrix-vector product."""
        from iron.operators.gemv.reference import reference

        return reference(A, B)
