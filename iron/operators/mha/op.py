# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
from pathlib import Path
from typing import Dict, List

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from iron.common.utils import torch_to_numpy, numpy_to_torch


class AIEMHA(MLIROperator):
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

        MLIROperator.__init__(self, context=context)

    def get_operator_name(self):
        kv_heads = self.num_KV_heads if self.num_KV_heads > 0 else self.num_heads
        return f"mha_{self.num_heads}h_{kv_heads}kv_{self.seq_len}s_{self.d}d"

    def get_mlir_artifact(self):
        operator_dir = Path(__file__).parent
        return PythonGeneratedMLIRArtifact(
            f"{self.get_operator_name()}.mlir",
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

    def get_kernel_artifacts(self):
        # Select kernel directory based on device type
        device_str = self.context.device_manager.device_str()
        kernel_dir = "aie2p" if device_str == "npu2" else "aie2"

        # Define source files
        mm_source = str(self.context.base_dir / "aie_kernels" / kernel_dir / "mm.cc")
        softmax_source = str(
            self.context.base_dir / "aie_kernels" / kernel_dir / "softmax.cc"
        )
        mha_source = str(
            self.context.base_dir / "aie_kernels" / "aie2p" / "mha.cc"
        )  # TODO: MHA kernel only exists in aie2p
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

        return [
            KernelObjectArtifact(
                f"mha_mm.o",
                extra_flags=mm_defines_colmaj,
                dependencies=[SourceArtifact(mm_source)],
            ),
            KernelObjectArtifact(
                f"mha_mm_rowmaj.o",
                extra_flags=mm_defines_rowmaj,
                dependencies=[SourceArtifact(mm_source)],
                rename_symbols=mm_rename_symbols,
            ),
            KernelObjectArtifact(
                "mha_softmax.o",
                dependencies=[SourceArtifact(softmax_source)],
            ),
            KernelObjectArtifact(
                "mha_mha.o", dependencies=[SourceArtifact(mha_source)]
            ),
            KernelObjectArtifact(
                "mha_passThrough.o",
                extra_flags=["-DBIT_WIDTH=16"],
                dependencies=[SourceArtifact(passthrough_source)],
            ),
        ]

    def get_artifacts(self):
        # Override to add --dynamic-objFifos flag
        operator_name = self.get_operator_name()
        mlir_artifact = self.get_mlir_artifact()
        kernel_deps_inputs = self.get_kernel_artifacts()
        if len(kernel_deps_inputs) > 0:
            mlir_artifact.callback_kwargs["kernel_archive"] = self.kernel_archive
        kernel_deps = (
            [
                KernelArchiveArtifact(
                    self.kernel_archive,
                    dependencies=kernel_deps_inputs,
                )
            ]
            if kernel_deps_inputs
            else []
        )
        xclbin_artifact = XclbinArtifact(
            f"{operator_name}.xclbin",
            mlir_input=mlir_artifact,
            dependencies=[mlir_artifact] + kernel_deps,
            extra_flags=["--dynamic-objFifos"],
        )
        insts_artifact = InstsBinArtifact(
            f"{operator_name}.bin",
            mlir_input=mlir_artifact,
            dependencies=[mlir_artifact],
            extra_flags=["--dynamic-objFifos"],
        )
        return xclbin_artifact, insts_artifact

    def get_arg_spec(self):
        seq_padding = self._calculate_seq_padding(self.seq_len, self.num_of_pipelines)
        buffer_size = self.num_heads * self.d * seq_padding
        return [
            AIERuntimeArgSpec("in", (buffer_size,)),  # Q
            AIERuntimeArgSpec("in", (buffer_size,)),  # K
            AIERuntimeArgSpec("in", (buffer_size,)),  # V
            AIERuntimeArgSpec("out", (buffer_size,)),  # O
        ]

    def _calculate_seq_padding(self, seq_len, num_pipeline=1):
        return ((seq_len + 63 * num_pipeline) // (64 * num_pipeline)) * (
            64 * num_pipeline
        )

    def _pad_to_multiple_of_64(self, tensor, seq_dim, num_pipeline=1):
        seq_len = tensor.shape[seq_dim]
        padded_seq_len = self._calculate_seq_padding(seq_len, num_pipeline)
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
