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
from aie.dialects.aie import get_target_model
from aie.dialects._aie_enum_gen import AIEArch
from iron.common.device_utils import get_kernel_dir
from iron.common.compilation import InstsBinArtifact, XclbinArtifact
from iron.common.operator_bases import lut_based_ops_artifacts
from iron.common.utils import float_to_name
import aie.utils as aie_utils

from iron.operators.flm.packing import pack_b, packed_b_size
from iron.operators.flm.gemm.design import (
    BFP16_GROUP,
    BFP16_GROUP_BYTES,
    CT_MAX_K_FOR_N,
    C_DEPTH,
    compute_rows,
    CT_OUT_LEN,
    Epilogue,
    K_TILE,
    MIN_K,
    M_TILE,
    R,
    Rounding,
    S,
    T,
    _default_l1,
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
    # Activation fused into the C drain.
    epilogue: Epilogue = Epilogue.NONE
    # The activations the epilogue can select between at run time. Each one
    # compiled in costs program memory, so a deployment that dispatches two
    # should compile two. Unlike `epilogue`, this is part of the
    # configuration.
    epilogue_modes: tuple[Epilogue, ...] = tuple(Epilogue)
    # Optional (min, max) applied after the activation.
    clamp: tuple[float, float] | None = None
    # n tile width. 64 halves the mmul's accumulator traffic per mac; 128
    # halves A fetches instead. __post_init__ resolves None per device and
    # shape; see the comment there and README.md.
    tile_n: int | None = None
    # A-tile rows, decoupled from the accumulator's M_TILE (asymmetric tile
    # buffering). __post_init__ resolves None to whatever L1 affords.
    tile_ma: int | None = None
    # Rounding for every f32->bf16 conversion; see Rounding in design.py.
    rounding: Rounding = Rounding.CONV_EVEN
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
        dev = aie_utils.get_current_device()
        if self.tile_n is None:
            # n=64 gives the mmul colA=8 instead of 4, halving accumulator
            # traffic per mac; n=128 halves A fetches instead. Which wins
            # depends on whether compute or data movement is the critical path.
            #
            # On NPU2 that flips with K: with a single k iteration there is too
            # little compute to hide the extra A traffic, so n=128 wins there
            # (~9%), while n=64 wins by ~20% at K >= 1024.
            #
            # NPU1 never reaches that crossover. It has half the columns AND a
            # quarter of the per-tile bf16 mac throughput (four native 4x8x4
            # macs per 8x8x8 shape, against NPU2's two bfp16-emulated ones), so
            # it stays compute-bound at every K, and n=128's 32 KB f32
            # accumulator also overflows bank-aware L1 allocation. n=64 wins
            # everywhere there by 1.21-1.38x, including at K=512 where NPU2's
            # rule would pick 128.
            single_k_iter = self.K // K_TILE <= 1
            self.tile_n = 128 if (dev.arch == AIEArch.AIE2p and single_k_iter) else 64
        elif self.tile_n not in CT_MAX_K_FOR_N:
            raise ValueError(
                f"tile_n must be one of {sorted(CT_MAX_K_FOR_N)}, got {self.tile_n}"
            )
        if self.tile_ma is None:
            self.tile_ma = _default_l1(
                self.tile_n,
                CT_MAX_K_FOR_N[self.tile_n],
                self._b_elem_bytes,
                get_target_model(dev.resolve()).get_local_memory_size(),
            )[0]
        # N only needs to tile to N_TILE: a trailing group of fewer than
        # COLS column-blocks is handled by giving the columns different trip
        # counts. See design.py.
        for name, value, unit in (
            ("M", self.M, M_TILE * compute_rows(dev)),
            ("K", self.K, MIN_K),
            ("N", self.N, self.tile_n),
        ):
            if value % unit != 0:
                raise ValueError(f"{name} ({value}) must be a multiple of {unit}")
        # Coerce so callers may pass the bare string; the enums are StrEnum, so
        # the resolved fields still serialize into artifact names unchanged.
        self.epilogue = Epilogue(self.epilogue)
        self.rounding = Rounding(self.rounding)
        if self.clamp is not None:
            lo, hi = self.clamp
            if lo > hi:
                raise ValueError(f"clamp min ({lo}) must be <= max ({hi})")

        MLIROperator.__init__(self, context=self.context)

    @property
    def _epilogue_mask(self) -> int:
        """Bitmask of the modes compiled into the epilogue. Mode 0 is always
        present -- the kernel falls back to it."""
        return 1 | sum(1 << Epilogue(m).mode for m in self.epilogue_modes)

    @property
    def _config_tag(self) -> str:
        """Everything that shapes the device configuration, and so the xclbin.

        M, K, N and the activation are absent: they are runtime parameters, so
        they change only the instruction stream.
        """
        clamp = ""
        if self.clamp is not None:
            clamp = "_clamp" + "_".join(float_to_name(float(v)) for v in self.clamp)
        dev = aie_utils.get_current_device().resolve().name
        return (
            f"tn{self.tile_n}_ma{self.tile_ma}_em{self._epilogue_mask:x}"
            f"_{self.rounding}{clamp}_{dev}"
        )

    @property
    def config_name(self) -> str:
        """Stem of the artifacts that do not depend on the shape."""
        return f"FLM_GEMM_{self._config_tag}"

    @property
    def name(self) -> str:
        """Artifact stem for the instruction stream, which does depend on it.

        Prefixed to disambiguate from ``iron.operators.GEMM``: this repo's
        build cache keys on filename and mtime rather than on source or flags,
        so two operators sharing a stem would silently satisfy each other.
        """
        base = f"FLM_GEMM_M{self.M}_K{self.K}_N{self.N}_{self._config_tag}"
        if self.epilogue != Epilogue.NONE:
            base = f"{base}_epi{self.epilogue}"
        return base

    @property
    def _bfp16_b(self) -> bool:
        """Whether B is stored as bfp16ebs8 rather than bf16.

        AIE2P only, and the reason both mmul templates in the kernel header are
        live rather than one being dead code: on AIE2 the scalar BFP types do
        not exist, so B stays bf16 and the mmul lowers onto four native 4x8x4
        macs.
        """
        return aie_utils.get_current_device().arch == AIEArch.AIE2p

    @property
    def _b_elem_bytes(self) -> float:
        """Bytes per B element in L1/L2: bfp16ebs8 packs 8 values into 9 bytes."""
        return BFP16_GROUP_BYTES / BFP16_GROUP if self._bfp16_b else 2

    @property
    def _kernel_object(self) -> str:
        """Object name over every flag that changes the emitted code.

        Everything the -D flags in ``get_kernel_artifacts`` carry has to appear
        here: this repo's build cache keys on filename and mtime rather than on
        source or flags, so an object built for one configuration would
        otherwise silently satisfy a request for another. That includes r/t,
        which set the blocked layout, and the epilogue flags, which since the
        epilogue was folded into this translation unit shape the same object.
        """
        clamp = ""
        if self.clamp is not None:
            clamp = "_clamp" + "_".join(float_to_name(float(v)) for v in self.clamp)
        return (
            f"mm_fused_{M_TILE}x{K_TILE}x{self.tile_n}"
            f"_r{R}t{T}_ma{self.tile_ma}_{self.rounding}"
            f"_em{self._epilogue_mask:x}{clamp}.o"
        )

    @property
    def _link_file(self) -> str:
        """What the design names as its kernel: the bare object, or the archive
        bundling it with the tanh LUT tables.

        Only AIE2 evaluates the activations through a LUT (AIE2P has a native
        vector tanh), and only an activation references tanh at all -- the plain
        epilogue just converts and stores. When this is wrong the failure is a
        LINK error for tanh_lut_ab/tanh_lut_cd rather than a compile error, so
        it surfaces late.
        """
        if (
            any(Epilogue(m) is not Epilogue.NONE for m in self.epilogue_modes)
            and get_kernel_dir() == "aie2"
        ):
            # config_name, not name: this string reaches the design's
            # link_with, so a shape in it would put the shape in the device
            # configuration.
            return f"{self.config_name}_kernels.a"
        return self._kernel_object

    @property
    def _reference_shape(self) -> tuple[int, int, int]:
        """The shape the configuration-only module is emitted at.

        Its runtime sequence is discarded; only its device body reaches the
        xclbin. Taking the smallest valid shape keeps that module cheap to
        build and makes the shape-independence explicit -- if a real shape's
        instruction stream did not run against this xclbin, some dimension
        would still be reaching the configuration.
        """
        dev = aie_utils.get_current_device()
        return M_TILE * compute_rows(dev), MIN_K, self.tile_n * dev.cols

    def _mlir_artifact(self, filename, M, K, N, epilogue):
        return PythonGeneratedMLIRArtifact(
            filename,
            DesignGenerator(
                self.operator_dir / "design.py",
                "gemm",
                (),
                {
                    "dev": aie_utils.get_current_device(),
                    "M": M,
                    "K": K,
                    "N": N,
                    "tile_n": self.tile_n,
                    "tile_ma": self.tile_ma,
                    "epilogue": epilogue,
                    "kernel_object": self._link_file,
                    "trace_size": 0,
                },
            ),
        )

    def get_mlir_artifact(self):
        return self._mlir_artifact(
            f"{self.name}.mlir", self.M, self.K, self.N, self.epilogue
        )

    def set_up_artifacts(self) -> None:
        kernels = self.get_kernel_artifacts()

        # The xclbin comes from a module emitted at a reference shape and a
        # reference activation, so every shape sharing this configuration
        # reuses it rather than rebuilding an identical one.
        config_mlir = self._mlir_artifact(
            f"{self.config_name}.mlir", *self._reference_shape, Epilogue.NONE
        )
        self.xclbin_artifact = XclbinArtifact(
            f"{self.config_name}.xclbin",
            mlir_input=config_mlir,
            dependencies=[config_mlir] + kernels,
        )
        shape_mlir = self.get_mlir_artifact()
        self.insts_artifact = InstsBinArtifact(
            f"{self.name}.bin",
            mlir_input=shape_mlir,
            # aiecc compiles the cores on the way to an instruction stream, so
            # this needs the kernel objects too.
            dependencies=[shape_mlir] + kernels,
        )
        self.add_artifacts([self.xclbin_artifact, self.insts_artifact])

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
        flags = [
            # Tile geometry and register tiling, for the mmul.
            f"-DMM_FUSED_TILE_M={M_TILE}",
            f"-DMM_FUSED_TILE_K={K_TILE}",
            f"-DMM_FUSED_TILE_N={self.tile_n}",
            f"-DMM_FUSED_TILE_MA={self.tile_ma}",
            f"-DMM_FUSED_R={R}",
            f"-DMM_FUSED_S={S}",
            f"-DMM_FUSED_T={T}",
            # The k slice. Passed rather than looked up in the kernel so that
            # CT_MAX_K_FOR_N is the only place it is chosen.
            f"-DMM_FUSED_CT_K={CT_MAX_K_FOR_N[self.tile_n]}",
            # Output stage.
            f"-DMM_FUSED_OUT_CHUNK={CT_OUT_LEN}",
            f"-DMM_FUSED_C_DEPTH={C_DEPTH}",
            f"-DMM_FUSED_EPILOGUE_MODE_MASK={self._epilogue_mask}",
        ] + arch_include
        if self._bfp16_b:
            flags += [
                "-DAIE_API_EMULATE_BFLOAT16_MMUL_WITH_BFP16",
                "-DMM_FUSED_BFP16_B",
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
        if self.rounding is Rounding.CONV_EVEN:
            # ROUND_CONV_EVEN is mm.cc's flag, reused rather than inventing a
            # second spelling, and its polarity is mm.cc's too: absent means the
            # core's power-up floor mode, even though this operator defaults the
            # other way. It covers both conversions in the kernel -- the mmul
            # and the epilogue's f32->bf16 store -- which must agree.
            flags.append("-DROUND_CONV_EVEN")

        kernel_obj = KernelObjectArtifact(
            self._kernel_object,
            dependencies=[
                SourceArtifact(generic / "mm_fused.cc"),
                SourceArtifact(generic / "mm_fused_mmul.h"),
                SourceArtifact(generic / "activations.h"),
                SourceArtifact(base_dir / "aie_kernels" / "aie_kernel_utils.h"),
                SourceArtifact(base_dir / "aie_kernels" / kernel_dir / "zero.cc"),
            ],
            extra_flags=flags,
        )
        if self._link_file == self._kernel_object:
            return [kernel_obj]
        # The tanh LUT's coefficient tables live in their own translation unit
        # in mlir-aie's runtime lib, so on AIE2 the kernel object alone leaves
        # tanh_lut_ab/tanh_lut_cd undefined at link time. See _link_file.
        return [
            KernelArchiveArtifact(
                self._link_file,
                dependencies=[kernel_obj] + lut_based_ops_artifacts(kernel_dir),
            )
        ]

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
        return pack_b(
            B,
            k_tile=K_TILE,
            n_tile=self.tile_n,
            s=S,
            t=T,
            ct_k=CT_MAX_K_FOR_N[self.tile_n],
            bfp16=self._bfp16_b,
            round_conv_even=self.rounding is Rounding.CONV_EVEN,
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
