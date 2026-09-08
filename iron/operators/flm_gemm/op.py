# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass, field
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
    N_TILE,
    S,
    T,
)


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
    # "conv_even" (round to nearest even) or "floor" (truncate). The core
    # powers up in floor, and the design this was ported from never sets the
    # mode, so "floor" reproduces its arithmetic exactly -- at ~40x the error,
    # because truncation biases every conversion the same way and the bias
    # accumulates over the K reduction instead of cancelling.
    rounding: str = field(default="conv_even", repr=False)
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {**MLIROperator._name_aliases}

    def __post_init__(self):
        # N only needs to tile to N_TILE: a trailing group of fewer than
        # COLS column-blocks is handled by giving the columns different trip
        # counts. See design.py.
        for name, value, unit in (
            ("M", self.M, MIN_M),
            ("K", self.K, MIN_K),
            ("N", self.N, N_TILE),
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
    def _kernel_object(self) -> str:
        rnd = "" if self.rounding == "conv_even" else f"_{self.rounding}"
        return f"flm_gemm_{M_TILE}x{K_TILE}x{N_TILE}{rnd}.o"

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
                    f"-DFLM_GEMM_TILE_N={N_TILE}",
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

    @staticmethod
    def pack_B(B):
        """Reorder a row-major ``(K, N)`` weight matrix into the layout the B
        fill expects. Returns a flat tensor.

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
        if K % K_TILE or N % N_TILE:
            raise ValueError(
                f"B ({K}, {N}) must tile to ({K_TILE}, {N_TILE}) to be packed"
            )
        t = B.reshape(K // K_TILE, K_TILE // S, S, N // N_TILE, N_TILE // T, T)
        # (kb, kb8, s_in, cb, tb, t_in) -> (cb, kb, tb, s_in, kb8, t_in)
        return t.permute(3, 0, 4, 2, 1, 5).reshape(-1).contiguous()

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (self.M, self.K)),  # A
            # B, pre-packed by pack_B -- same element count, different order.
            AIERuntimeArgSpec("in", (self.K, self.N)),  # B (weights)
            AIERuntimeArgSpec("out", (self.M, self.N)),  # C
        ]

    def reference(self, A, B):
        """CPU reference: ``C = epilogue(A @ B)``."""
        from iron.operators.flm_gemm.reference import reference

        return reference(A, B, self.epilogue, self.clamp)
