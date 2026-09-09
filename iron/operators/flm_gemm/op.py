# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field

import numpy as np
import torch
from typing import ClassVar, Dict

from iron.common import (
    MLIROperator,
    AIERuntimeArgSpec,
    KernelObjectArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
    DesignGenerator,
)
from iron.common.device_utils import get_kernel_dir
import aie.utils as aie_utils

from iron.operators.flm_gemm.design import (
    COLS,
    C_DEPTH,
    CT_OUT_LEN,
    EPILOGUE_MODES,
    K_TILE,
    MIN_K,
    MIN_M,
    M_TILE,
    N_TILE_DEFAULT,
    S,
    T,
)


def _f32_to_bfp16ebs8(a, round_conv_even=True):
    """float32 -> bfp16ebs8, matching the hardware's to_v64bfp16ebs8.

    Blocks of 8 share the max f32 exponent in the block; each mantissa is the
    24-bit magnitude with the implicit bit made explicit, shifted right by
    17 + (maxExp - exp) to land on the shared exponent.

    That shift OBEYS THE CORE'S ROUNDING MODE. mlir-aie's reference
    ``floatToBfp16`` (``programming_examples/ml/block_datatypes/helper.h``)
    hardcodes truncation and says AIE2P always truncates -- true only of the
    power-up ``floor`` mode. flm_gemm calls ``set_rounding(conv_even)``, so the
    kernel's own conversion rounds to nearest with ties to even, and matching
    it here is what makes packing B on the host numerically free. Measured on
    hardware: 14.9375 -> 15 (rounds up) while 106.5 -> 106 and 94.5 -> 94
    (ties to even), which truncation cannot produce.

    Layout per block: one shared-exponent byte then the 8 mantissa bytes.
    """
    flat = np.ascontiguousarray(a, dtype=np.float32).reshape(-1, 8)
    u = flat.view(np.uint32)
    sign = (u & 0x80000000) != 0
    exp = ((u >> 23) & 0xFF).astype(np.int32)
    man = (u & 0x007FFFFF).astype(np.uint32)
    man = np.where(exp != 0, man | 0x00800000, man).astype(np.uint32)
    max_exp = exp.max(axis=1, keepdims=True)
    # signed magnitude; rounding below must see the sign to tie correctly
    mag = np.where(sign, -man.astype(np.int64), man.astype(np.int64))
    # The two shifts compose: 17 to keep 7 mantissa bits plus the sign, then
    # (maxExp - exp) to bring the value onto the block's shared exponent.
    # TRUNCATION, not rounding -- that is what AIE2P does, and round-to-nearest
    # here measures 6.18e-03 against truncation's 2.69e-04.
    shift = (max_exp - exp).astype(np.int64)
    total = np.clip(17 + shift, 0, 62)
    if round_conv_even:
        # np.rint is round-half-to-even. man < 2**24 and the divisor is a power
        # of two, so the quotient is exact in float64 and the only rounding is
        # the intended one.
        v8 = np.rint(mag.astype(np.float64) / np.exp2(total.astype(np.float64)))
    else:
        v8 = mag >> total
    v8 = np.where(shift >= 32, np.where(sign, -1, 0), v8)
    # Rounding can carry the block's largest magnitude from 127 to 128, which
    # does not fit the signed 8-bit mantissa; saturate rather than wrap.
    v8 = np.clip(v8, -128, 127)
    out = np.empty((flat.shape[0], 9), dtype=np.uint8)
    out[:, 0] = max_exp[:, 0].astype(np.uint8)
    out[:, 1:] = v8.astype(np.int8).view(np.uint8)
    return torch.from_numpy(out.reshape(-1))


@dataclass
class FLMGEMM(MLIROperator):
    """AIE-accelerated bf16 GEMM on a fixed 4x8 grid, with a fused epilogue.

    A row-broadcast / C memtile-join design with fixed 64/512/128 tiling. See
    ``design.py`` for how it differs from the more general ``GEMM`` operator.
    Unlike ``GEMM`` this exposes no tiling knobs, but folds an activation and an
    optional clamp into the output stage.
    """

    M: int
    K: int
    N: int
    # "none" | "gelu" | "silu" | "sigmoid", fused into the C drain.
    epilogue: str = field(default="none", repr=False)
    # Optional (min, max) applied after the activation.
    clamp: tuple[float, float] | None = field(default=None, repr=False)
    # n tile width. 64 halves the mmul's accumulator traffic per mac; 128
    # halves A fetches instead and wins only when small K makes the operator
    # DMA-bound. See README.md.
    tile_n: int | None = field(default=None, repr=False)
    # A-tile rows, decoupled from the accumulator's M_TILE (asymmetric tile
    # buffering). None means symmetric (T_MA == M_TILE).
    tile_ma: int | None = field(default=None, repr=False)
    # "conv_even" (round to nearest even) or "floor" (truncate). The core
    # powers up in floor, and the design this was ported from never sets the
    # mode, so "floor" reproduces its arithmetic exactly -- at ~40x the error,
    # because truncation biases every conversion the same way and the bias
    # accumulates over the K reduction instead of cancelling.
    rounding: str = field(default="conv_even", repr=False)
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {**MLIROperator._name_aliases}

    def __post_init__(self):
        if self.tile_n is None:
            self.tile_n = self._default_tile_n(self.K)
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
    def _default_tile_n(K: int) -> int:
        """Pick the n tile from the shape.

        n=64 gives the mmul colA=8 instead of 4, halving accumulator traffic
        per mac; n=128 halves A fetches instead. Which wins depends on whether
        compute or data movement is the critical path, and that is set by how
        much K there is to reduce over: with a single k iteration there is too
        little compute to hide the extra A traffic. Measured ~20% for n=64 at
        K >= 1024 and ~9% the other way at K = 512.
        """
        return 128 if K // K_TILE <= 1 else 64

    @property
    def name(self) -> str:
        # epilogue/clamp are repr=False so the plain path keeps a stable name,
        # but they change the emitted kernel, so the variants must not share an
        # artifact name: in a shared build dir a cached plain build would
        # otherwise satisfy a fused op and silently skip the activation.
        base = super().name
        if self.epilogue != "none":
            base = f"{base}_epi{self.epilogue}"
        if self.clamp is not None:
            base = f"{base}_clamp{self._clamp_tag}"
        if self.rounding != "conv_even":
            base = f"{base}_{self.rounding}"
        if self.tile_n != self._default_tile_n(self.K):
            base = f"{base}_tn{self.tile_n}"
        # The RESOLVED height, not just an explicit override: it changes the
        # emitted MLIR and the kernel object, so a build dir holding another
        # value's artifacts must not satisfy this one.
        if self._tile_ma != M_TILE:
            base = f"{base}_ma{self._tile_ma}"
        return base

    @property
    def _clamp_tag(self) -> str:
        lo, hi = self.clamp
        return f"{lo:g}_{hi:g}".replace("-", "m").replace(".", "p")

    @property
    def _epilogue_artifact(self) -> str:
        obj = f"flm_gemm_epilogue_{self.epilogue}"
        if self.clamp is not None:
            obj = f"{obj}_clamp{self._clamp_tag}"
        if self.rounding != "conv_even":
            obj = f"{obj}_{self.rounding}"
        return f"{obj}.o"

    @property
    def _rounding_flags(self) -> list[str]:
        """Applies to both kernels: the mmul and the epilogue's f32->bf16
        store are both conversions and must agree."""
        return ["-DFLM_GEMM_ROUND_FLOOR"] if self.rounding == "floor" else []

    @property
    def _epilogue_source(self):
        return self.context.base_dir / "aie_kernels" / "aie2p" / "flm_gemm_epilogue.cc"

    @property
    def _epilogue_flags(self) -> list[str]:
        """Compile flags for the epilogue."""
        flags = [
            f"-DFLM_GEMM_OUT_CHUNK={CT_OUT_LEN}",
            f"-DFLM_GEMM_C_DEPTH={C_DEPTH}",
            f"-DFLM_GEMM_EPILOGUE_MODE={EPILOGUE_MODES[self.epilogue]}",
        ]
        if self.clamp is not None:
            lo, hi = self.clamp
            # repr() rather than :g -- the latter renders -4.0 as "-4", and
            # "-4f" is not a valid C float literal.
            flags += [
                "-DFLM_GEMM_CLAMP=1",
                f"-DFLM_GEMM_CLAMP_MIN={float(lo)!r}f",
                f"-DFLM_GEMM_CLAMP_MAX={float(hi)!r}f",
            ]
        return flags + self._rounding_flags

    @property
    def _ablate_mmul(self) -> bool:
        """ABLATION: FLM_NULL_MMUL=1 nulls the multiply, leaving all data
        movement. Threaded into the object AND operator names because the
        build cache is keyed on filename."""
        import os

        return os.environ.get("FLM_NULL_MMUL", "") == "1"

    @property
    def _tile_ma(self) -> int:
        """Resolved A-tile height. design.py picks the default, and it MUST be
        the same value the kernel is compiled with -- the design sizes the A
        object from it while the kernel derives the mmul's rowA from it, so a
        mismatch reads past the buffer and produces garbage rather than a build
        error."""
        from iron.operators.flm_gemm.design import CT_MAX_K_FOR_N, _default_l1

        if self.tile_ma is not None:
            return self.tile_ma
        return _default_l1(self.tile_n, CT_MAX_K_FOR_N[self.tile_n])[0]

    @property
    def _kernel_object(self) -> str:
        rnd = "" if self.rounding == "conv_even" else f"_{self.rounding}"
        ma = f"_ma{self._tile_ma}" + ("_nomm" if self._ablate_mmul else "")
        return f"flm_gemm_{M_TILE}x{K_TILE}x{self.tile_n}{rnd}{ma}.o"

    def get_mlir_artifact(self):
        return PythonGeneratedMLIRArtifact(
            f"{self.name}.mlir",
            DesignGenerator(
                self.operator_dir / "design.py",
                "flm_gemm",
                (),
                {
                    "dev": aie_utils.get_current_device(),
                    "M": self.M,
                    "K": self.K,
                    "N": self.N,
                    "tile_n": self.tile_n,
                    "tile_ma": self._tile_ma,
                    "epilogue": self.epilogue,
                    "kernel_object": self._kernel_object,
                    "epilogue_object": self._epilogue_artifact,
                    "trace_size": 0,
                },
            ),
        )

    def get_kernel_artifacts(self):
        # The mmul and the epilogue are both aie2p-only: the mmul relies on the
        # bf16 emulation path and the grid needs 8 columns.
        kernel_dir = get_kernel_dir()
        if kernel_dir != "aie2p":
            raise NotImplementedError(
                f"flm_gemm is only available on NPU2 (aie2p); got {kernel_dir!r}"
            )
        base_dir = self.context.base_dir
        aie2p = base_dir / "aie_kernels" / "aie2p"

        artifacts = [
            KernelObjectArtifact(
                self._kernel_object,
                dependencies=[SourceArtifact(aie2p / "flm_gemm.cc")],
                extra_flags=[
                    f"-DFLM_GEMM_TILE_M={M_TILE}",
                    f"-DFLM_GEMM_TILE_K={K_TILE}",
                    f"-DFLM_GEMM_TILE_N={self.tile_n}",
                    f"-DFLM_GEMM_TILE_MA={self._tile_ma}",
                    "-DFLM_GEMM_BFP16_B",
                    *(["-DFLM_GEMM_NULL_MMUL"] if self._ablate_mmul else []),
                    # The r=8 mmul shape this design uses only exists on the
                    # bfp16-emulated path; without this the kernel will not
                    # compile.
                    "-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16",
                ]
                + self._rounding_flags,
            ),
        ]
        artifacts.append(
            KernelObjectArtifact(
                self._epilogue_artifact,
                dependencies=[SourceArtifact(self._epilogue_source)],
                extra_flags=self._epilogue_flags,
            )
        )
        return artifacts

    def pack_B(self, B):
        """Reorder and quantize a row-major ``(K, N)`` weight matrix into the
        layout the B fill expects. Returns a flat uint8 tensor of bfp16ebs8
        blocks, NOT a bf16 tensor.

        The quantization is not a loss this adds. The mmul only multiplies
        bfp16, so the bf16 path converts B inside every mac call; doing it here
        hoists a rounding that already happened and leaves the arithmetic
        bit-identical. It also makes B 9 bytes per 8 values instead of 16,
        which is the point -- this operator is data-movement bound.

        Each ``K_TILE x N_TILE`` tile is emitted in t-block-major order -- the
        odometer ``(n//T, k%S, k//S, n%T)``, outermost first -- with tiles
        ordered by column stripe and then by k-block, so each fill is one
        contiguous read.

        This is deliberately the caller's job. The same reorder is expressible
        as a strided descriptor over an unpacked B, but its innermost run is
        then T=8 bf16 = 16 bytes, turning each 128 KB transfer into 8192
        scattered bursts -- measured 5.4x slower end to end, and the whole of
        this operator's gap against the design it was ported from, which packs
        its weights on the host for the same reason. Weights are packed once
        and reused across dispatches, so the cost belongs here.
        """
        K, N = B.shape
        N_TILE = self.tile_n
        if K % K_TILE or N % N_TILE:
            raise ValueError(
                f"B ({K}, {N}) must tile to ({K_TILE}, {N_TILE}) to be packed"
            )
        # Emit the FINAL consumption order, not an intermediate one. The old
        # layout left a 4-dimension scatter for the memtile's dims_from_stream
        # to finish, which put the n-block index outside the k-slice index and
        # so cost two descriptor dimensions on the way back out. Packing all
        # the way here makes both B hops linear, which is what leaves room for
        # a k-slice deep enough to halve the accumulator traffic (CT_MAX_K=128)
        # while B is also memtile-resident.
        from iron.operators.flm_gemm.design import CT_MAX_K_FOR_N

        CT_K = CT_MAX_K_FOR_N[N_TILE]
        col_a = CT_K // S
        t = B.reshape(
            K // K_TILE, K_TILE // CT_K, col_a, S, N // N_TILE, N_TILE // T, T
        )
        # (kb, kslice, i, s_in, cb, tb, t_in)
        #   -> (cb, kb, kslice, tb, i, t_in, s_in)
        # t-major within the block: the mixed mmul hands B straight to
        # mac_8x8_8x8T without the transpose the bf16 form applies, so the
        # transpose happens here instead. It also puts the 8 values that share
        # a bfp16 exponent (8 consecutive k for one n) adjacent, which is what
        # makes the block grouping below match the kernel's.
        # Grouping the shared exponent over 8 consecutive k (for one n) is
        # verified: grouping over n instead measures 1.95e-02 against this
        # layout's 2.69e-04.
        t = t.permute(4, 0, 1, 5, 2, 6, 3).reshape(-1, 8).contiguous()
        return _f32_to_bfp16ebs8(
            t.float().numpy(), round_conv_even=self.rounding == "conv_even"
        )

    @staticmethod
    def unpack_B_size(K, N):
        """Bytes ``pack_B`` returns for a ``(K, N)`` weight matrix."""
        return K * N // 8 * 9

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.M, self.K)),  # A
            # B arrives pre-packed AND quantized by pack_B: bfp16ebs8, which is
            # 9 bytes per 8 values rather than bf16's 16. Declared in bytes so
            # the buffer is sized from what pack_B actually returns -- a
            # (K, N) bf16 spec would over-allocate the largest buffer by 1.78x.
            AIERuntimeArgSpec(
                "in", (self.unpack_B_size(self.K, self.N),), dtype=np.uint8
            ),  # B (weights)
            AIERuntimeArgSpec("out", (self.M, self.N)),  # C
        ]

    def reference(self, A, B):
        """CPU reference: ``C = epilogue(A @ B)``."""
        from iron.operators.flm_gemm.reference import reference

        return reference(A, B, self.epilogue, self.clamp)
