# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path
from typing import Dict, List

from iron.common import (
    AIEOperatorBase,
    AIEOperatorConstraintError,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from iron.common.utils import torch_to_numpy, numpy_to_torch


class AIEMHA(AIEOperatorBase):

    def __init__(
        self,
        num_heads: int,
        seq_len: int,
        d: int,
        num_KV_heads: int,
        num_of_pipelines: int = 1,
        context=None,
    ):
        self.num_heads = num_heads
        self.seq_len = seq_len
        self.d = d
        self.B_q = 64
        self.B_kv = 64
        self.num_KV_heads = num_KV_heads
        self.num_of_pipelines = num_of_pipelines
        assert d == 64, "Only d=64 is supported in this version"

        # Artifacts created by set_up_artifacts()
        self.xclbin_artifact = None
        self.insts_artifact = None

        AIEOperatorBase.__init__(self, context=context)

    def set_up_artifacts(self):
        # Set up compilation artifacts
        # ---
        operator_dir = Path(__file__).parent

        kv_heads = self.num_KV_heads if self.num_KV_heads > 0 else self.num_heads
        file_name_base = f"mha_{self.num_heads}h_{kv_heads}kv_{self.seq_len}s_{self.d}d"

        # Define source files
        mm_source = str(self.context.base_dir / "aie_kernels" / "aie2p" / "mm.cc")
        softmax_source = str(
            self.context.base_dir / "aie_kernels" / "aie2p" / "softmax.cc"
        )
        mha_source = str(self.context.base_dir / "aie_kernels" / "aie2p" / "mha.cc")
        passthrough_source = str(
            self.context.base_dir / "aie_kernels" / "generic" / "passThrough.cc"
        )

        # Compile mm.cc (col-major)
        mm_defines_rowmaj = [
            "-Dbf16_bf16_ONLY",
            f"-DDIM_M={self.B_q}",
            f"-DDIM_K={self.d}",
            f"-DDIM_N={self.B_kv}",
            "-DROUND_CONV_EVEN",
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
            import_path=operator_dir / "design.py",
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
            f"{file_name_base}.xclbin",
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
            f"{file_name_base}.bin", depends=[mlir_artifact], extra_flags=["--dynamic-objFifos"]
        )

        self.xclbin_artifact = xclbin_artifact
        self.insts_artifact = insts_artifact

        artifacts = [xclbin_artifact, insts_artifact]
        self.add_artifacts(artifacts)

    def set_up_runtime(self):
        # Set up runtime
        # ---
        self.add_kernel(
            "mha",
            self.xclbin_artifact,
            self.xclbin_artifact.kernel_name,
            self.insts_artifact,
        )
        self.add_buffer(
            "Q",
            self.num_heads
            * self.d
            * self._calculate_seq_padding(self.seq_len, self.num_of_pipelines),
        )
        self.add_buffer(
            "K",
            self.num_heads
            * self.d
            * self._calculate_seq_padding(self.seq_len, self.num_of_pipelines),
        )
        self.add_buffer(
            "V",
            self.num_heads
            * self.d
            * self._calculate_seq_padding(self.seq_len, self.num_of_pipelines),
        )
        self.add_buffer(
            "O",
            self.num_heads
            * self.d
            * self._calculate_seq_padding(self.seq_len, self.num_of_pipelines),
        )
        self.add_to_runlist("mha", "Q", "K", "V", "O")

    def _calculate_seq_padding(self, seq_len, num_pipeline=1):
        return ((seq_len + 63 * num_pipeline) // (64 * num_pipeline)) * (
            64 * num_pipeline
        )

    def _pad_to_multiple_of_64(self, tensor, seq_dim, num_pipeline=1):
        seq_len = tensor.shape[seq_dim]
        padded_seq_len = _calculate_seq_padding(seq_len, num_pipeline)
        if padded_seq_len == seq_len:
            return tensor

        pad_size = padded_seq_len - seq_len
        pad_dims = [0] * (2 * tensor.ndim)
        pad_dims[2 * (tensor.ndim - 1 - seq_dim) + 1] = pad_size

        return torch.nn.functional.pad(tensor, pad_dims)

    def _pack_compact_to_padded(
        self, src: np.ndarray, H: int, S: int, S_pad: int, D: int
    ) -> np.ndarray:
        """Pack compact tensor into padded format."""
        dst = src
        if S != S_pad:
            dst = np.zeros((H, S_pad, D), dtype=src.dtype)
            dst[:H, :S, :D] = src
        return dst

    def _unpack_padded_to_compact(
        self, src: np.ndarray, H: int, S: int, S_pad: int, D: int
    ) -> np.ndarray:
        """Unpack padded tensor back to compact format."""
        dst = src
        if S < S_pad:
            dst = np.zeros((H, S, D), dtype=src.dtype)
            dst = src[:H, :S, :D]
        return dst

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
        # Convert to numpy
        q_np = torch_to_numpy(q)
        k_np = torch_to_numpy(k)
        v_np = torch_to_numpy(v)

        # Calculate padded sequence length
        S_pad = self._calculate_seq_padding(self.seq_len, self.num_of_pipelines)

        # Pack compact inputs to padded format
        q_padded = self._pack_compact_to_padded(
            q_np, self.num_heads, self.seq_len, S_pad, self.d
        )
        k_padded = self._pack_compact_to_padded(
            k_np, self.num_heads, self.seq_len, S_pad, self.d
        )
        v_padded = self._pack_compact_to_padded(
            v_np, self.num_heads, self.seq_len, S_pad, self.d
        )

        # Write padded buffers
        self.write_buffer("Q", q_padded)
        self.write_buffer("K", k_padded)
        self.write_buffer("V", v_padded)

        # Execute
        self.run_runlist()

        # Read padded output
        o_padded = self.read_buffer(
            "O", shape=(self.num_heads, S_pad, self.d), dtype=bfloat16
        )

        # Unpack padded output to compact format
        o_compact = self._unpack_padded_to_compact(
            o_padded, self.num_heads, self.seq_len, S_pad, self.d
        )

        # Convert back to torch with correct shape
        result = numpy_to_torch(o_compact)
        return result
