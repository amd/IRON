# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
import aie.utils as aie_utils
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
    # Optional norm applied to the shared vector once before the matvec, fusing a
    # RMSNorm/LayerNorm decode prologue into the same dispatch. Affine-free (gamma/beta
    # fold into the weight matrix host-side, same convention the norm kernels already use).
    prologue: str = field(default="none", repr=False)
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
        if not (
            self.K >= self.kernel_vector_size and self.K % self.kernel_vector_size == 0
        ):
            raise ValueError("K must be multiple of kernel_vector_size")
        if self.epilogue not in ("none", "gelu"):
            raise ValueError(
                f"unknown epilogue {self.epilogue!r} (expected 'none' or 'gelu')"
            )
        if self.epilogue == "gelu" and self.tile_size_output % 16 != 0:
            raise ValueError(
                f"gelu epilogue needs tile_size_output % 16 == 0 (got {self.tile_size_output})"
            )
        if self.prologue not in ("none", "rms", "ln"):
            raise ValueError(
                f"unknown prologue {self.prologue!r} (expected 'none', 'rms' or 'ln')"
            )

        MLIROperator.__init__(self, context=self.context)

    @property
    def name(self) -> str:
        # epilogue is repr=False so the default path keeps a stable name, but the fused
        # variant must not share an artifact name with the plain GEMV of the same shape:
        # both would emit the same .mlir/.xclbin, and in a shared build dir a cached unfused
        # build can then satisfy the fused op (running the raw matvec with no activation).
        base = super().name
        suffix = ""
        if self.prologue != "none":
            suffix += f"_pro{self.prologue}"
        if self.epilogue != "none":
            suffix += f"_epi{self.epilogue}"
        return base + suffix

    @property
    def _kernel_link_file(self):
        # With a prologue and/or the gelu epilogue the core links extra kernels, so the
        # object becomes an archive; with neither, the plain matvec stays a single object.
        if self.prologue == "none" and self.epilogue == "none":
            return f"gemv_{self.K}k_{self.kernel_vector_size}vs.o"
        suffix = ""
        if self.prologue != "none":
            suffix += f"_pro{self.prologue}"
        if self.epilogue != "none":
            suffix += f"_epi{self.epilogue}"
        return f"gemv_{self.K}k_{self.kernel_vector_size}vs{suffix}_kernels.a"

    def get_mlir_artifact(self):
        mlir_verbose = getattr(self.context, "mlir_verbose", False)

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
                    "kernel_object": self._kernel_link_file,
                    "epilogue": self.epilogue,
                    "prologue": self.prologue,
                },
            ),
        )

    def get_kernel_artifacts(self):
        matvec_obj = KernelObjectArtifact(
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
        )
        extra_objs = []
        if self.prologue != "none":
            # rms_norm.cc / layer_norm.cc exist under both aie2 and aie2p with the same
            # extern-C signature, so the prologue works on NPU1 and NPU2 alike.
            norm_src = "rms_norm.cc" if self.prologue == "rms" else "layer_norm.cc"
            extra_objs.append(
                KernelObjectArtifact(
                    norm_src.replace(".cc", ".o"),
                    dependencies=[
                        SourceArtifact(
                            self.context.base_dir
                            / "aie_kernels"
                            / get_kernel_dir()
                            / norm_src
                        )
                    ],
                )
            )
        if self.epilogue == "gelu":
            # The gelu kernel lives in aie2p/gelu.cc, so the fused epilogue is NPU2-only.
            if get_kernel_dir() != "aie2p":
                raise NotImplementedError(
                    "gemv gelu epilogue is only available on NPU2 (aie2p); "
                    f"current kernel dir is {get_kernel_dir()!r}"
                )
            extra_objs.append(
                KernelObjectArtifact(
                    "gelu.o",
                    dependencies=[
                        SourceArtifact(
                            self.context.base_dir / "aie_kernels" / "aie2p" / "gelu.cc"
                        )
                    ],
                )
            )
        if not extra_objs:
            return [matvec_obj]
        return [
            KernelArchiveArtifact(
                self._kernel_link_file, dependencies=[matvec_obj] + extra_objs
            )
        ]

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
