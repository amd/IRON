# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field

import numpy as np
from typing import ClassVar, Dict

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelArchiveArtifact,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
from iron.common.device_utils import get_kernel_dir
from iron.common.operator_bases import lut_based_ops_artifacts
import aie.utils as aie_utils

from iron.operators.flm.packing import pack_b, packed_b_size
from iron.operators.flm.gemm.design import (
    CT_MAX_K_FOR_N,
    C_DEPTH,
    CT_OUT_LEN,
    EPILOGUE_MODES,
    K_TILE,
    MIN_K,
    MIN_M,
    M_TILE,
    _default_l1,
    register_tiling,
)


@dataclass
class GEMM(MLIROperator):
    """AIE-accelerated bf16 GEMM on a 4-row grid, with a fused epilogue.

    A row-broadcast / C memtile-join design with fixed 64/512/128 tiling. See
    ``design.py`` for how it differs from the more general ``GEMM`` operator.
    Unlike ``GEMM`` this exposes no tiling knobs, but folds an activation and an
    optional clamp into the output stage.

    The grid is as wide as the device: 8 columns on NPU2, 4 on NPU1 (Phoenix).
    Only the width varies -- the tiling and the blocked L1 layout are shared.
    """

    # Every field below is repr=True, so MLIROperator.name derives the artifact
    # stem from all of them. That is not cosmetic: each one changes the emitted
    # MLIR or the kernel object, and this repo's build cache keys on filename,
    # so a variant that shared a stem would be silently satisfied by another
    # variant's cached build.
    M: int
    K: int
    N: int
    # "none" | "gelu" | "silu" | "sigmoid", fused into the C drain.
    epilogue: str = "none"
    # Optional (min, max) applied after the activation.
    clamp: tuple[float, float] | None = None
    # n tile width. 64 halves the mmul's accumulator traffic per mac; 128
    # halves A fetches instead. __post_init__ resolves None per device and
    # shape; see _default_tile_n and README.md.
    tile_n: int | None = None
    # A-tile rows, decoupled from the accumulator's M_TILE (asymmetric tile
    # buffering). __post_init__ resolves None to whatever L1 affords.
    tile_ma: int | None = None
    # "conv_even" (round to nearest even) or "floor" (truncate). The core powers
    # up in floor and the overlay this was ported from never sets the mode, so
    # "floor" reproduces its arithmetic exactly -- at ~40x the error, because
    # truncation biases every conversion the same way and the bias accumulates
    # over the K reduction instead of cancelling.
    rounding: str = "conv_even"
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "epilogue": "epi",
        "tile_n": "tn",
        "tile_ma": "ma",
        "rounding": "rnd",
    }

    def __post_init__(self):
        # Resolve both tile knobs to concrete values here, so the dataclass
        # fields hold what the build actually uses. The resolved tile_ma in
        # particular must reach the artifact name: the design sizes the A object
        # from it while the kernel derives the mmul's rowA from it, so an
        # artifact built for one value must never satisfy a request for another.
        if self.tile_n is None:
            self.tile_n = self._default_tile_n(self.K)
        elif self.tile_n not in CT_MAX_K_FOR_N:
            raise ValueError(
                f"tile_n must be one of {sorted(CT_MAX_K_FOR_N)}, got {self.tile_n}"
            )
        if self.tile_ma is None:
            self.tile_ma = _default_l1(
                self.tile_n, CT_MAX_K_FOR_N[self.tile_n], self._b_elem_bytes
            )[0]
        # N only needs to tile to N_TILE: a trailing group of fewer than
        # COLS column-blocks is handled by giving the columns different trip
        # counts. See design.py.
        for name, value, unit in (
            ("M", self.M, MIN_M),
            ("K", self.K, MIN_K),
            ("N", self.N, self.tile_n),
        ):
            if value % unit != 0:
                raise ValueError(f"{name} ({value}) must be a multiple of {unit}")
        if self.epilogue not in EPILOGUE_MODES:
            raise ValueError(
                f"epilogue must be one of {sorted(EPILOGUE_MODES)}, "
                f"got {self.epilogue!r}"
            )
        if self.clamp is not None:
            lo, hi = self.clamp
            if lo > hi:
                raise ValueError(f"clamp min ({lo}) must be <= max ({hi})")
        if self.rounding not in ("conv_even", "floor"):
            raise ValueError(
                f"rounding must be 'conv_even' or 'floor', got {self.rounding!r}"
            )

        MLIROperator.__init__(self, context=self.context)

    @staticmethod
    def _default_tile_n(K: int, kernel_dir: str | None = None) -> int:
        """Pick the n tile from the shape and the device.

        n=64 gives the mmul colA=8 instead of 4, halving accumulator traffic
        per mac; n=128 halves A fetches instead. Which wins depends on whether
        compute or data movement is the critical path.

        On NPU2 that flips with K: with a single k iteration there is too
        little compute to hide the extra A traffic, so n=128 wins there.
        Measured ~20% for n=64 at K >= 1024 and ~9% the other way at K = 512.

        NPU1 never reaches that crossover. It has half the columns AND a
        quarter of the per-tile bf16 mac throughput (four native 4x8x4 macs per
        8x8x8 shape, against NPU2's two bfp16-emulated ones), so it stays
        compute-bound at every K, and n=128's 32 KB f32 accumulator also
        overflows bank-aware L1 allocation. Measured on Phoenix, n=64 wins
        everywhere by 1.21x (M=256 K=512 N=512) to 1.38x (M=1024 K=2048
        N=1024) -- including at K=512, where NPU2's rule would pick 128.
        """
        if kernel_dir is None:
            kernel_dir = get_kernel_dir()
        if kernel_dir == "aie2":
            return 64
        return 128 if K // K_TILE <= 1 else 64

    @property
    def name(self) -> str:
        """Artifact stem, prefixed to disambiguate from ``iron.operators.GEMM``.

        ``MLIROperator.name`` derives the stem from ``type(self).__name__``,
        which is ``GEMM`` for both operators. This repo's build cache keys on
        filename and mtime rather than on source or flags, so two operators
        sharing a stem in one build dir would silently satisfy each other.
        """
        return f"FLM_{super().name}"

    @property
    def _epilogue_artifact(self) -> str:
        """Object name for the epilogue, over the flags that shape it."""
        clamp = ""
        if self.clamp is not None:
            clamp = "_clamp" + "_".join(
                repr(float(v)).replace(".", "p").replace("-", "n").replace("+", "")
                for v in self.clamp
            )
        return f"mm_fused_epilogue_{self.epilogue}{clamp}_{self.rounding}.o"

    @property
    def _needs_tanh_lut(self) -> bool:
        """Whether the epilogue has to be linked against the tanh LUT tables.

        Only AIE2 evaluates the activations through a LUT (AIE2P has a native
        vector tanh), and only an activation references tanh at all -- the
        plain epilogue converts and stores. Note the failure mode when this is
        wrong is a LINK error for tanh_lut_ab/tanh_lut_cd, not a compile error,
        so it surfaces late.
        """
        return self.epilogue != "none" and get_kernel_dir() == "aie2"

    @property
    def _epilogue_link_file(self) -> str:
        """What the design should name as the epilogue kernel: the bare object,
        or the archive bundling it with the LUT tables."""
        if self._needs_tanh_lut:
            return f"{self.name}_epilogue.a"
        return self._epilogue_artifact

    @property
    def _rounding_flags(self) -> list[str]:
        """Applies to both kernels: the mmul and the epilogue's f32->bf16
        store are both conversions and must agree.

        ROUND_CONV_EVEN is mm.cc's flag, reused here rather than inventing a
        second spelling. Its polarity is mm.cc's too -- absent means the core's
        power-up floor mode -- even though this operator defaults the other way.
        """
        return ["-DROUND_CONV_EVEN"] if self.rounding == "conv_even" else []

    @property
    def _epilogue_source(self):
        return (
            self.context.base_dir / "aie_kernels" / "generic" / "mm_fused_epilogue.cc"
        )

    @property
    def _epilogue_flags(self) -> list[str]:
        """Compile flags for the epilogue."""
        flags = [
            f"-DMM_FUSED_OUT_CHUNK={CT_OUT_LEN}",
            f"-DMM_FUSED_C_DEPTH={C_DEPTH}",
            f"-DMM_FUSED_EPILOGUE_MODE={EPILOGUE_MODES[self.epilogue]}",
        ]
        if self.clamp is not None:
            lo, hi = self.clamp
            # repr() rather than :g -- the latter renders -4.0 as "-4", and
            # "-4f" is not a valid C float literal.
            flags += [
                "-DMM_FUSED_CLAMP=1",
                f"-DMM_FUSED_CLAMP_MIN={float(lo)!r}f",
                f"-DMM_FUSED_CLAMP_MAX={float(hi)!r}f",
            ]
        return flags + self._rounding_flags

    @property
    def _bfp16_b(self) -> bool:
        """Whether B is stored as bfp16ebs8 rather than bf16.

        AIE2P only. ``__AIE_API_SCALAR_BFP_TYPES__`` is defined solely in
        ``aie_api/detail/aie2p/config.hpp`` and ``mmul_bfp16_bfp16.hpp`` exists
        only under ``aie2p/``; on AIE2, ``aie_api/types.hpp`` gives
        ``bfp16ebs8`` an empty placeholder struct. So AIE2 keeps B in bf16 and
        uses the native 4x8x4-composed mmul, which is why both mmul templates
        in the kernel header are live rather than one being dead code.
        """
        return get_kernel_dir() == "aie2p"

    @property
    def _b_elem_bytes(self) -> float:
        """Bytes per B element in L1/L2: bfp16ebs8 packs 8 values into 9 bytes."""
        return 9 / 8 if self._bfp16_b else 2

    @property
    def _rst(self) -> tuple[int, int, int]:
        """The mmul's r/s/t for this device. ``pack_B`` and the design's stream
        dimensions must agree on these or the result is silently wrong."""
        return register_tiling(aie_utils.get_current_device().resolve().name)

    @property
    def _kernel_object(self) -> str:
        """Object name over every flag that changes the emitted code.

        r/t are included even though build dirs are already architecture-scoped,
        because they set the blocked layout: an object built for one shape must
        never satisfy a request for another.
        """
        r, _s, t = self._rst
        return (
            f"mm_fused_{M_TILE}x{K_TILE}x{self.tile_n}"
            f"_r{r}t{t}_ma{self.tile_ma}_{self.rounding}.o"
        )

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "gemm",
                (),
                {
                    "dev": aie_utils.get_current_device(),
                    "M": self.M,
                    "K": self.K,
                    "N": self.N,
                    "tile_n": self.tile_n,
                    "tile_ma": self.tile_ma,
                    "epilogue": self.epilogue,
                    "kernel_object": self._kernel_object,
                    "epilogue_object": self._epilogue_link_file,
                    "trace_size": 0,
                },
            ),
        )

    def get_kernel_artifacts(self):
        kernel_dir = get_kernel_dir()
        base_dir = self.context.base_dir
        generic = base_dir / "aie_kernels" / "generic"

        # mm_fused.cc includes zero.cc, which is genuinely per-architecture
        # (AIE2 stores 256 bits at a time, AIE2P 512). A quoted include searches
        # the including file's own directory first -- now generic/ -- so the
        # arch directory has to be on the include path for it to resolve there.
        arch_include = [f"-I{base_dir / 'aie_kernels' / kernel_dir}"]

        # The 8x8x8 mmul shape this design uses exists on both architectures,
        # but by different routes: AIE2P lowers it onto two bfp16-emulated macs,
        # which is what this flag selects, while AIE2 lowers it onto four native
        # 4x8x4 bf16 macs and ignores the flag entirely (it has no bfp16
        # hardware). Passing it on AIE2 would be harmless but misleading, so it
        # is scoped to the architecture where it actually changes codegen.
        #
        # MM_FUSED_BFP16_B rides along with it: storing B as bfp16ebs8 needs the
        # scalar BFP types, which only AIE2P has. See _bfp16_b.
        emulate_flags = (
            ["-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16", "-DMM_FUSED_BFP16_B"]
            if self._bfp16_b
            else []
        )

        artifacts = [
            KernelObjectArtifact(
                self._kernel_object,
                dependencies=[
                    SourceArtifact(generic / "mm_fused.cc"),
                    SourceArtifact(generic / "mm_fused_mmul.h"),
                    SourceArtifact(base_dir / "aie_kernels" / "aie_kernel_utils.h"),
                    SourceArtifact(base_dir / "aie_kernels" / kernel_dir / "zero.cc"),
                ],
                extra_flags=[
                    f"-DMM_FUSED_TILE_M={M_TILE}",
                    f"-DMM_FUSED_TILE_K={K_TILE}",
                    f"-DMM_FUSED_TILE_N={self.tile_n}",
                    f"-DMM_FUSED_TILE_MA={self.tile_ma}",
                    f"-DMM_FUSED_R={self._rst[0]}",
                    f"-DMM_FUSED_S={self._rst[1]}",
                    f"-DMM_FUSED_T={self._rst[2]}",
                    # The k slice. Passed rather than looked up in the kernel so
                    # that CT_MAX_K_FOR_N below is the only place it is chosen.
                    f"-DMM_FUSED_CT_K={CT_MAX_K_FOR_N[self.tile_n]}",
                ]
                + arch_include
                + emulate_flags
                + self._rounding_flags,
            ),
        ]
        epilogue_obj = KernelObjectArtifact(
            self._epilogue_artifact,
            dependencies=[
                SourceArtifact(self._epilogue_source),
                SourceArtifact(generic / "activations.h"),
                SourceArtifact(base_dir / "aie_kernels" / "aie_kernel_utils.h"),
            ],
            extra_flags=self._epilogue_flags,
        )
        if self._needs_tanh_lut:
            # The LUT's coefficient tables live in their own translation unit in
            # mlir-aie's runtime lib, so the epilogue object alone leaves
            # tanh_lut_ab/tanh_lut_cd undefined at link time.
            artifacts.append(
                KernelArchiveArtifact(
                    self._epilogue_link_file,
                    dependencies=[epilogue_obj] + lut_based_ops_artifacts(kernel_dir),
                )
            )
        else:
            artifacts.append(epilogue_obj)
        return artifacts

    def pack_B(self, B):
        """Reorder a row-major ``(K, N)`` weight matrix into consumption order.

        Returns a flat uint8 tensor of bfp16ebs8 blocks on NPU2, where B is also
        quantized, and a flat bf16 tensor on NPU1. Bound to the operator rather
        than a static method because the layout depends on the resolved
        ``tile_n`` and on the device; call ``op.pack_B(B)``.

        Packing all the way to consumption order is what makes both B hops
        linear descriptors (design.py's b_recv_dims and b_send_dims are both
        None), which in turn leaves the descriptor dimensions for a k slice deep
        enough to halve the accumulator traffic while B is also memtile-resident.
        See :mod:`iron.operators.flm.packing` for the layout itself.
        """
        _r, s, t = self._rst
        return pack_b(
            B,
            k_tile=K_TILE,
            n_tile=self.tile_n,
            s=s,
            t=t,
            ct_k=CT_MAX_K_FOR_N[self.tile_n],
            bfp16=self._bfp16_b,
            round_conv_even=self.rounding == "conv_even",
        )

    def packed_B_size(self, K, N):
        """Elements (bf16) or bytes (bfp16ebs8) that ``pack_B`` returns."""
        return packed_b_size(K, N, self._bfp16_b)

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.M, self.K)),  # A
            # B arrives pre-packed by pack_B. On AIE2P it is also quantized to
            # bfp16ebs8 -- 9 bytes per 8 values rather than bf16's 16 -- so it
            # is declared in BYTES there, sizing the buffer from what pack_B
            # actually returns; a (K, N) bf16 spec would over-allocate the
            # largest buffer by 1.78x. On AIE2 B stays bf16 and the spec is the
            # plain element count.
            (
                AIERuntimeArgSpec(
                    "in", (self.packed_B_size(self.K, self.N),), dtype=np.uint8
                )
                if self._bfp16_b
                else AIERuntimeArgSpec("in", (self.K, self.N))
            ),  # B (weights)
            AIERuntimeArgSpec("out", (self.M, self.N)),  # C
        ]

    def reference(self, A, B):
        """CPU reference: ``C = epilogue(A @ B)``."""
        from iron.operators.flm.gemm.reference import reference

        return reference(A, B, self.epilogue, self.clamp)
