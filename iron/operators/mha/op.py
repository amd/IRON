# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
from typing import ClassVar, Dict

import torch
import numpy as np
from ml_dtypes import bfloat16

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
import aie.utils as aie_utils


@dataclass
class MHA(MLIROperator):
    """AIE-accelerated Multi-Head Attention operator"""

    num_heads: int
    seq_len: int
    d: int
    num_KV_heads: int
    num_of_pipelines: int = field(default=1, repr=False)
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "num_heads": "h",
        "num_KV_heads": "kv",
        "seq_len": "s",
    }

    def __post_init__(self):
        self.B_q = 64
        self.B_kv = 64
        if self.d != 64:
            raise ValueError(f"Only d=64 is supported in this version, got d={self.d}")
        MLIROperator.__init__(self, context=self.context)

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "fused_mha",
                (),
                {
                    "dev": aie_utils.DefaultNPURuntime.device(),
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
            ),
        )

    def get_kernel_artifacts(self):
        mm_source = str(self.context.base_dir / "aie_kernels" / "aie2p" / "mm.cc")
        softmax_source = str(
            self.context.base_dir / "aie_kernels" / "aie2p" / "softmax.cc"
        )
        mha_source = str(self.context.base_dir / "aie_kernels" / "aie2p" / "mha.cc")
        passthrough_source = str(
            self.context.base_dir / "aie_kernels" / "generic" / "passThrough.cc"
        )

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
        # mha.cc #includes softmax.cc and mm.cc (both col-major and row-major)
        # directly, so everything is compiled into a single mha.o translation unit.
        return [
            KernelObjectArtifact(
                "mha.o",
                extra_flags=mm_defines_colmaj,
                dependencies=[
                    SourceArtifact(mha_source),
                    SourceArtifact(mm_source),
                    SourceArtifact(softmax_source),
                ],
            ),
            KernelObjectArtifact(
                "mha_passThrough.o",
                extra_flags=["-DBIT_WIDTH=16"],
                dependencies=[SourceArtifact(passthrough_source)],
            ),
        ]

    def get_artifacts(self):
        return super().get_artifacts(dynamic_obj_fifos=True)

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
        if S < S_pad:
            return src[:H, :S, :D]
        return src
