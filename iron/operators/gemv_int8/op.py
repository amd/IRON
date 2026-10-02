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
import aie.utils as aie_utils


@dataclass
class GEMVInt8(MLIROperator):
    """int8-weight GEMV with in-kernel dequantization (W8A16).

    Weights are GPTQ int8, repacked host-side to row-major (M, K) int8 plus a
    (M, K/128) bf16 per-(channel, group) scale table (fp16 checkpoint scales
    are transposed + converted on load).  The kernel dequantizes in registers
    and feeds the bf16 mac pipeline, so quantization genuinely halves the
    weight DRAM traffic instead of writing dequantized weights back out.
    """

    M: int
    K: int
    num_aie_columns: int = 1
    tile_size_input: int = 2
    tile_size_output: int | None = None
    num_batches: int = 1
    kernel_vector_size: int = field(default=128, repr=False)
    # Weight-fifo depth in L1. 2 is plain double buffering; deeper hides more of the shim->L1
    # latency at extra L1 cost. The other weight-streaming designs in this tree gained from exactly
    # this (swiglu_mlp_dp: 29.2 -> 38 GB/s going 1 -> 2), and this op carries the chain's largest
    # single stream (lm_head, 158 MB/token at 36.5 GB/s against a 49.7 GB/s pure-read bound).
    # There is NO L1 assert for it in design.py (a model that did exist rejected the known-good
    # depth=2), so a deeper value must be validated by the chain's cosine gate.
    weight_depth: int = field(default=2, repr=False)
    # Per-INSTANCE kernel FILE override (e.g. "mv_int8_signed.cc" for a signed-payload arm),
    # falling back to the context attribute `gemv_int8_kernel_source` (the GEMV_KERNEL_SOURCE
    # env path) and then to the production biased kernel.  Per-instance selection is what lets
    # ONE chain run two payload domains at once: the host can pack W_o/lm_head in the signed
    # domain while every other int8 design stays biased.  Kernel source and packing domain must
    # always switch TOGETHER -- this field only fixes the kernel side; the packer is the
    # caller's responsibility.
    # Deliberately NOT part of `name` (repr=False, like weight_depth below): the tree's
    # convention is that kernel variants are isolated by BUILD DIR, not by op name (the
    # GEMV_KERNEL_SOURCE path this mirrors has always worked that way), and an artifact name
    # carrying a filename would leak a "." into every file it generates.  Two arms that differ
    # ONLY in this field must therefore not share a build directory.
    kernel_source: str | None = field(default=None, repr=False)
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "num_aie_columns": "col",
        "tile_size_input": "tsi",
        "tile_size_output": "tso",
        "num_batches": "batch",
        "weight_depth": "wd",   # MUST be in the name: the op-level artifact cache is keyed by name
                                # alone, so two depths would silently share one ELF (the qkv
                                # runtime_tile_loop bug, 9/16).
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
        if self.K % 128 != 0:
            raise ValueError("K must be a multiple of GROUP_SIZE=128")

        MLIROperator.__init__(self, context=self.context)

    @property
    def name(self) -> str:
        return super().name  # aliases already encode M/K/cols/tiling

    def _kernel_source(self) -> str:
        """Kernel FILE this instance compiles from: instance override > context > production.

        The context attribute is the GEMV_KERNEL_SOURCE env path (chain-wide, for ablation
        benches); the per-instance `kernel_source` field is what a chain uses to switch ONE
        op's payload domain without dragging every other GEMVInt8 in the sequence with it.
        """
        if self.kernel_source is not None:
            return self.kernel_source
        return getattr(self.context, "gemv_int8_kernel_source", None) or "mv_int8.cc"

    def get_mlir_artifact(self):
        mlir_verbose = getattr(self.context, "mlir_verbose", False)
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "my_matvec_int8",
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
                    "kernel_object": self._kernel_source().replace(".cc", ".o"),
                    "n_aie_rows": getattr(self.context, "gemv_int8_aie_rows", 1),
                    "weight_depth": self.weight_depth,
                },
            ),
        )

    def get_kernel_artifacts(self):
        # context may inject extra kernel flags (e.g. -DDEQUANT_MODE for
        # ablation benches); empty by default so other sequences are unaffected.
        # gemv_int8_kernel_source / the instance's `kernel_source` field: the
        # kernel FILE (e.g. "mv_int8_2stage.cc" for the two-stage variant,
        # "mv_int8_signed.cc" for the signed-payload variant); the .o and the
        # extern-C entry derive from it, so variants live as separate files
        # (no #if gymnastics).
        src = self._kernel_source()
        kobj = src.replace(".cc", ".o")
        extra = list(getattr(self.context, "gemv_int8_kernel_flags", []))
        return [
            KernelObjectArtifact(
                kobj,
                dependencies=[
                    SourceArtifact(
                        self.context.base_dir / "aie_kernels" / "aie2p" / src
                    )
                ],
                extra_flags=[
                    f"-DDIM_K={self.K}",
                    f"-DVEC_SIZE={self.kernel_vector_size}",
                    "-DGROUP_SIZE=128",
                    *extra,
                ],
            )
        ]

    def get_arg_spec(self):
        batch_dim = (self.num_batches,) if self.num_batches > 1 else ()
        # Single packed weight payload per batch: per (M//cols) row-tile,
        # [tile_m*K int8 weights | tile_m*(K/128) bf16 scales], viewed as bf16
        # elements (bytes/2). Scaled to the full M across cols by the design.
        # Per row-block payload: [tile_m*K int8 | tile_m*G bf16 scales] where
        # tile_m = tile_size_input (one L1 W-tile). The L3 stream is flat over
        # all M rows: (M / tile_m) blocks. Viewed as bf16 elements (bytes / 2).
        tile_m = self.tile_size_input
        tile_bytes = tile_m * self.K + tile_m * (self.K // 128) * 2
        w_elems = self.num_batches * (self.M // tile_m) * tile_bytes // 2
        return [
            AIERuntimeArgSpec("in", (w_elems,)),           # packed int8+scales (bf16 view)
            AIERuntimeArgSpec("in", batch_dim + (self.K,)),  # bf16 vector
            AIERuntimeArgSpec("out", batch_dim + (self.M,)),  # output
        ]

    def reference(self, A_q, scales, B):
        """CPU reference: dequantize int8 weights then matvec."""
        import torch

        a = A_q.to(torch.float32) * scales.to(torch.float32)
        return (a @ B.float()).to(torch.bfloat16)
