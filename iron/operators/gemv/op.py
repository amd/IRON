# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)


class AIEGEMV(MLIROperator):
    """AIE-accelerated General Matrix-Vector/Vector-Matrix Multiplication layer"""

    def __init__(
        self,
        M,
        K,
        num_aie_columns=1,
        tile_size_input=2,
        tile_size_output=None,
        num_batches=1,
        kernel_vector_size=64,
        context=None,
    ):
        if tile_size_output is None:
            tile_size_output = tile_size_input

        if not (
            tile_size_output % tile_size_input == 0
            and tile_size_output >= tile_size_input
        ):
            raise ValueError("tile_size_output must be a multiple of tile_size_input")
        self.M = M  # matrix rows
        self.K = K  # matrix columns, vector rows
        self.num_aie_columns = num_aie_columns
        self.tile_size_input = tile_size_input
        self.tile_size_output = tile_size_output
        self.num_batches = num_batches
        self.kernel_vector_size = kernel_vector_size
        if not (K >= kernel_vector_size and K % kernel_vector_size == 0):
            raise ValueError("K must be multiple of kernel_vector_size")

        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        return f"gemv_{self.M}x{self.K}_{self.tile_size_input}tsi_{self.tile_size_output}tso_{self.num_batches}batch_{self.num_aie_columns}col"

    def get_mlir_artifact(self):
        mlir_verbose = getattr(self.context, "mlir_verbose", False)

        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
            import_path=self.operator_dir / "design.py",
            callback_fn="my_matvec",
            callback_args=[
                self.context.device_manager.device_type,
                self.num_aie_columns,
                self.M,
                self.K,
                self.tile_size_input,
                self.tile_size_output,
                self.num_batches,
            ],
            callback_kwargs={
                "verbose": mlir_verbose,
                "kernel_object": f"gemv_{self.K}k_{self.kernel_vector_size}vs.o",
            },
        )

    def get_kernel_artifacts(self):
        return [
            KernelObjectArtifact(
                f"gemv_{self.K}k_{self.kernel_vector_size}vs.o",
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir / "aie_kernels" / "generic" / "mv.cc"
                    )
                ],
                extra_flags=[
                    f"-DDIM_K={self.K}",
                    f"-DVEC_SIZE={self.kernel_vector_size}",
                ],
            ),
        ]

    def get_arg_spec(self):
        batch_dim = (self.num_batches,) if self.num_batches > 1 else ()
        return [
            AIERuntimeArgSpec("in", batch_dim + (self.M, self.K)),  # matrix
            AIERuntimeArgSpec("in", batch_dim + (self.K,)),  # vector
            AIERuntimeArgSpec("out", batch_dim + (self.M,)),  # output
        ]
