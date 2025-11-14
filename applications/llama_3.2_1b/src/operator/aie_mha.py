# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path
from typing import Dict, List

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


class AIEMHA(AIEOperatorBase):

    def __init__(
        self,
        num_heads: int,
        seq_len: int,
        d: int,
        num_KV_heads: int,
        num_of_pipelines: int = 1,
    ):
        self.num_heads = num_heads
        self.seq_len = seq_len
        self.d = d
        self.B_q = 64
        self.B_kv = 64
        self.num_KV_heads = num_KV_heads
        self.num_of_pipelines = num_of_pipelines
        assert d == 64, "Only d=64 is supported in this version"
        AIEOperatorBase.__init__(self)

    def set_up(self):
        # Set up compilation artifacts
        # ---

        kv_heads = self.num_KV_heads if self.num_KV_heads > 0 else self.num_heads
        file_name_base = f"mha_{self.num_heads}h_{kv_heads}kv_{self.seq_len}s_{self.d}d"

        # Determine kernel source directories
        kernels_dir = Path(self.base_dir) / "aie_kernels" / "aie2p"
        kernels_generic_dir = Path(self.base_dir) / "aie_kernels" / "generic"

        # Define source files
        mm_source = str(kernels_dir / "mm.cc")
        softmax_source = str(kernels_dir / "softmax.cc")
        mha_source = str(kernels_dir / "mha.cc")
        passthrough_source = str(kernels_generic_dir / "passThrough.cc")

        # Compile mm.cc (col-major)
        mm_defines_rowmaj = [
            "-Dbf16_bf16_ONLY",
            f"-DDIM_M={self.B_q}",
            f"-DDIM_K={self.d}",
            f"-DDIM_N={self.B_kv}",
            "-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16",
        ]
        mm_defines_colmaj = mm_defines_rowmaj + [
            "-DB_COL_MAJ",
        ]
        mm_rename_symbols = {
            "matmul_bf16_bf16": "matmul_bf16_bf16_rowmaj",
            "matmul_scalar_bf16_bf16": "matmul_scalar_bf16_bf16_rowmaj",
            "zero_bf16": "zero_bf16_rowmaj",
            "zero_scalar_bf16": "zero_scalar_bf16_rowmaj",
        }

        mlir_artifact = PythonGeneratedMLIRArtifact.new(
            f"{file_name_base}.mlir",
            import_path=self.base_dir / "example" / "mha" / "mha.py",
            callback_fn="fused_mha",
            callback_kwargs={
                "heads": self.num_heads,
                "S_q": self.seq_len,
                "S_kv": self.seq_len,
                "d": self.d,
                "B_q": self.B_q,
                "B_kv": self.B_kv,
                "num_KV_heads": self.num_KV_heads,
                "number_of_pipelines": self.num_of_pipelines,
                "emulate_bf16_mmul_with_bfp16": True,
                "trace_size": 0,
                "verbose": False,
            },
        )

        xclbin_artifact = XclbinArtifact.new(
            f"mha.xclbin",
            depends=[
                mlir_artifact,
                KernelArchiveArtifact.new(
                    f"mha_kernels.a",
                    depends=[
                        KernelObjectArtifact.new(
                            f"mha_mm.o",
                            extra_flags=mm_defines_colmaj,
                            depends=[SourceArtifact.new(mm_source)],
                        ),
                        KernelObjectArtifact.new(
                            f"mha_mm_rowmaj.o",
                            extra_flags=mm_defines_rowmaj,
                            depends=[SourceArtifact.new(mm_source)],
                            rename_symbols=mm_rename_symbols,
                        ),
                        KernelObjectArtifact.new(
                            "mha_softmax.o",
                            depends=[SourceArtifact.new(softmax_source)],
                        ),
                        KernelObjectArtifact.new(
                            "mha_mha.o", depends=[SourceArtifact.new(mha_source)]
                        ),
                        KernelObjectArtifact.new(
                            "mha_passThrough.o",
                            extra_flags=["-DBIT_WIDTH=16"],
                            depends=[SourceArtifact.new(passthrough_source)],
                        ),
                    ],
                ),
            ],
            extra_flags=["--dynamic-objFifos"],
        )

        insts_artifact = InstsBinArtifact.new(
            f"mha.bin", depends=[mlir_artifact], extra_flags=["--dynamic-objFifos"]
        )

        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

        # Set up runtime
        # ---
        self.add_kernel(
            "mha", xclbin_artifact, xclbin_artifact.kernel_name, insts_artifact
        )
        self.add_buffer("Q", self.num_heads * self.d * self.seq_len)
        self.add_buffer("K", self.num_heads * self.d * self.seq_len)
        self.add_buffer("V", self.num_heads * self.d * self.seq_len)
        self.add_buffer("O", self.num_heads * self.d * self.seq_len)
        self.add_to_runlist("mha", "Q", "K", "V", "O")

    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor):
        applicable = (
            q.shape[-1] == self.d
            and k.shape[-1] == self.d
            and v.shape[-1] == self.d
            and q.shape[-2] == self.seq_len
            and k.shape[-2] == self.seq_len
            and v.shape[-2] == self.seq_len
            and self.seq_len % 64 == 0,  # Sequence length must be multiple of 64
        )
        if not applicable:
            raise AIEOperatorConstraintError(
                "AIEElementwiseAdd: incompatible tensor shape(s)"
            )

        ret = self._execute_aie_operation(q, k, v)
        return ret

    def _execute_aie_operation(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor):
        q_np = torch_to_numpy(q)
        k_np = torch_to_numpy(k)
        v_np = torch_to_numpy(v)
        self.write_buffer("Q", q_np)
        self.write_buffer("K", k_np)
        self.write_buffer("V", v_np)
        self.write_buffer("O", np.zeros(q_np.size, dtype=bfloat16))
        self.run_runlist()
        result = self.read_buffer_as_torch("O", shape=q_np.shape, dtype=q_np.dtype)
        return result
