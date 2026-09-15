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
import aie.utils as aie_utils

from iron.operators.flm.packing import pack_b, packed_b_size
from iron.operators.flm.gemm.design import (
    BFP16_GROUP,
    BFP16_GROUP_BYTES,
    CT_MAX_K_FOR_N,
    M_CHUNK_FOR_N,
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
    _hw_stride_ok,
)


@dataclass
class GEMM(MLIROperator):
    """AIE-accelerated bf16 GEMM on a 4-row grid, with a fused epilogue.

    Fixed 64/512/128 tiling, no tiling knobs, and an activation plus optional
    clamp folded into the output stage. The grid is as wide as the device: 8
    columns on NPU2, 4 on NPU1. See ``design.py``.
    """

    # Every field below is repr=True, so MLIROperator.name derives the artifact
    # stem from all of them. The build cache keys on filename, not on source or
    # flags, so any field that changes the emitted MLIR or the kernel object
    # must reach the stem or a stale build silently satisfies the request.
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
    # Optional (min, max) applied after the activation. The bounds are runtime
    # parameters and the kernel always clamps, so this changes the instruction
    # stream only -- clamped and unclamped callers share one xclbin.
    clamp: tuple[float, float] | None = None
    # n tile width. 64 halves the mmul's accumulator traffic per mac; 128
    # halves A fetches instead. __post_init__ resolves None per device and
    # shape; see the comment there and README.md.
    tile_n: int | None = None
    # A-tile rows, decoupled from the accumulator's M_TILE (asymmetric tile
    # buffering). __post_init__ resolves None to whatever L1 affords.
    tile_ma: int | None = None
    # Row-blocks folded into one B fetch. __post_init__ resolves None from
    # tile_n, falling back to 1 when it would not divide m_row_blocks.
    m_chunk: int | None = None
    # Rounding for every f32->bf16 conversion; see Rounding in design.py.
    rounding: Rounding = Rounding.CONV_EVEN
    context: object = field(default=None, repr=False)

    _name_aliases: ClassVar[Dict[str, str]] = {
        **MLIROperator._name_aliases,
        "epilogue": "epi",
        "tile_n": "tn",
        "tile_ma": "ma",
        "m_chunk": "mc",
        "rounding": "rnd",
    }

    def __post_init__(self):
        # Resolve both tile knobs here, so the fields hold what the build
        # actually uses. tile_ma especially must reach the artifact name: the
        # design sizes the A object from it and the kernel derives the mmul's
        # rowA from it.
        dev = aie_utils.get_current_device()
        if self.tile_n is None:
            # The trade flips with K on NPU2: one k iteration has too little
            # compute to hide n=64's extra A traffic, so n=128 wins there by
            # ~9% and n=64 by ~20% at K >= 1024. NPU1 has half the columns and
            # a quarter of the per-tile bf16 throughput, so it stays
            # compute-bound and n=64 wins at every K by 1.21-1.38x.
            single_k_iter = self.K // K_TILE <= 1
            self.tile_n = 128 if (dev.arch == AIEArch.AIE2p and single_k_iter) else 64
        elif self.tile_n not in CT_MAX_K_FOR_N:
            raise ValueError(
                f"tile_n must be one of {sorted(CT_MAX_K_FOR_N)}, got {self.tile_n}"
            )
        # m_chunk falls back to 1 unless both hold: it divides m_row_blocks (a
        # partial group is inexpressible, see design.py), and the group's
        # row-blocks sit ROWS*M_TILE*K apart inside the A descriptor, a stride
        # that must fit the shim BD's 20-bit step. K=10240 overflows it where
        # m_chunk=1 would not.
        if self.m_chunk is None:
            want = M_CHUNK_FOR_N[self.tile_n]
            rows = M_TILE * compute_rows(dev)
            m_row_blocks = self.M // rows if self.M % rows == 0 else 0
            fits = m_row_blocks and m_row_blocks % want == 0
            if fits and not _hw_stride_ok(compute_rows(dev) * M_TILE * self.K):
                fits = False
            self.m_chunk = want if fits else 1
        if self.tile_ma is None:
            self.tile_ma = _default_l1(
                self.tile_n,
                CT_MAX_K_FOR_N[self.tile_n],
                self._b_elem_bytes,
                get_target_model(dev.resolve()).get_local_memory_size(),
                self.m_chunk,
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
        # Deduplicated, since the mask ORs one bit per mode and a repeat would
        # otherwise have to be tolerated by every consumer of the tuple.
        self.epilogue_modes = tuple(
            dict.fromkeys(Epilogue(m) for m in self.epilogue_modes)
        )
        # A mode the mask leaves out reaches the kernel's default arm, which is
        # NONE -- an unactivated result rather than a build or dispatch error.
        # Refuse instead: this is the caller contradicting itself.
        if (
            self.epilogue is not Epilogue.NONE
            and self.epilogue not in self.epilogue_modes
        ):
            raise ValueError(
                f"epilogue {self.epilogue} is not in epilogue_modes "
                f"{tuple(str(m) for m in self.epilogue_modes)}, so it would not "
                "be compiled in and the kernel would silently apply none"
            )
        if self.clamp is not None:
            lo, hi = self.clamp
            if lo > hi:
                raise ValueError(f"clamp min ({lo}) must be <= max ({hi})")

        MLIROperator.__init__(self, context=self.context)

    @property
    def _epilogue_mask(self) -> int:
        """Bitmask of the modes compiled into the epilogue. Mode 0 is always
        present -- the kernel falls back to it.

        OR rather than sum: ``__post_init__`` deduplicates, but a sum would
        make that a correctness requirement rather than tidiness, since two
        copies of a mode carry into the neighbouring mode's bit.
        """
        mask = 1
        for m in self.epilogue_modes:
            mask |= 1 << Epilogue(m).mode
        return mask

    @property
    def config_name(self) -> str:
        """Stem of the artifacts that do not depend on the shape.

        Everything here shapes the device configuration, and so the xclbin. M,
        K, N, the activation and the clamp bounds are absent: they are runtime
        parameters, so they reach the instruction stream instead -- see
        ``name``.

        ``ck`` needs naming separately because retuning CT_MAX_K_FOR_N moves it
        while tn is unmoved, and tile_ma is caller-overridable. Omitting it
        once served an xclbin built at one ck to a request for another.
        """
        dev = aie_utils.get_current_device().resolve().name
        return (
            f"FLM_GEMM_tn{self.tile_n}_ck{CT_MAX_K_FOR_N[self.tile_n]}"
            f"_ma{self.tile_ma}_mc{self.m_chunk}"
            f"_em{self._epilogue_mask:x}_{self.rounding}_{dev}"
        )

    @property
    def name(self) -> str:
        """Artifact stem for the instruction stream, which does depend on it.

        The configuration it runs on, then the runtime parameters on top. That
        also inherits ``config_name``'s prefix, which disambiguates from
        ``iron.operators.GEMM`` -- that class would otherwise share a stem and
        satisfy this operator's cache lookups.

        Every runtime parameter has to appear, because the sequence writes them
        as immediates and the build cache keys on filename and mtime: a stem
        that omits one serves the first caller's instruction stream to the
        second and silently applies the first caller's values. The clamp bounds
        go in as raw bit patterns, so bounds that differ only below the printed
        precision still get their own stem.
        """
        base = f"{self.config_name}_M{self.M}_K{self.K}_N{self.N}"
        if self.epilogue != Epilogue.NONE:
            base = f"{base}_epi{self.epilogue}"
        if self.clamp is not None:
            lo, hi = (
                int(np.float32(v).view(np.int32)) & 0xFFFFFFFF for v in self.clamp
            )
            base = f"{base}_cl{lo:08x}{hi:08x}"
        return base

    @property
    def _bfp16_b(self) -> bool:
        """Whether B is stored as bfp16ebs8 rather than bf16.

        AIE2P only, which is why both mmul templates in the kernel header are
        live: on AIE2 the scalar BFP types do not exist, so B stays bf16 and
        the mmul lowers onto four native 4x8x4 macs.
        """
        return aie_utils.get_current_device().arch == AIEArch.AIE2p

    @property
    def _b_elem_bytes(self) -> float:
        """Bytes per B element in L1/L2: bfp16ebs8 packs 8 values into 9 bytes."""
        return BFP16_GROUP_BYTES / BFP16_GROUP if self._bfp16_b else 2

    @property
    def _kernel_object(self) -> str:
        """Object name over every flag that changes the emitted code.

        Every -D flag from ``get_kernel_artifacts`` has to appear, for the
        cache reason above. ``ck`` looks derivable from tile_n, but that is a
        tuning table: naming it means retuning an entry does not also require
        wiping the build dir.
        """
        return (
            f"mm_fused_{M_TILE}x{K_TILE}x{self.tile_n}"
            f"_ck{CT_MAX_K_FOR_N[self.tile_n]}"
            f"_r{R}t{T}_ma{self.tile_ma}_{self.rounding}"
            f"_em{self._epilogue_mask:x}.o"
        )

    @property
    def _link_file(self) -> str:
        """What the design names as its kernel: the bare object, or the archive
        bundling it with the tanh LUT tables.

        Only AIE2 evaluates activations through a LUT, and only an activation
        references tanh. Getting this wrong is a link error, so it surfaces
        late.
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

        Its runtime sequence is discarded; only the device body reaches the
        xclbin. The smallest valid shape keeps it cheap and makes the
        shape-independence explicit.
        """
        dev = aie_utils.get_current_device()
        # M must be at least m_chunk row-blocks: a partial group is
        # inexpressible (see design.py), and this module must build.
        return (
            M_TILE * compute_rows(dev) * self.m_chunk,
            MIN_K,
            self.tile_n * dev.cols,
        )

    def _mlir_artifact(self, filename, M, K, N, epilogue, clamp):
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
                    "m_chunk": self.m_chunk,
                    "epilogue": epilogue,
                    "clamp": clamp,
                    "kernel_object": self._link_file,
                    "trace_size": 0,
                },
            ),
        )

    def get_mlir_artifact(self):
        return self._mlir_artifact(
            f"{self.name}.mlir", self.M, self.K, self.N, self.epilogue, self.clamp
        )

    def set_up_artifacts(self) -> None:
        kernels = self.get_kernel_artifacts()

        # Emitted at a reference shape and activation, so every shape sharing
        # this configuration reuses it. No clamp, not this instance's bounds:
        # they reach only the discarded runtime sequence.
        config_mlir = self._mlir_artifact(
            f"{self.config_name}.mlir",
            *self._reference_shape,
            Epilogue.NONE,
            None,
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
        kernels_dir = self.context.kernels_dir
        generic = kernels_dir / "generic"

        # The last kernel IRON keeps in-tree, pending upstreaming to mlir-aie:
        # its runtime epilogue (#200) is newer than the package copy. Its
        # #included companions are unchanged, so they come from kernels_dir; the
        # include path needs generic/ (activations.h, mm_fused_mmul.h,
        # ../aie_kernel_utils.h) and the arch dir (zero.cc), since neither sits
        # beside the in-tree source.
        in_tree_generic = self.context.base_dir / "aie_kernels" / "generic"
        arch_include = [
            f"-I{generic}",
            f"-I{kernels_dir / kernel_dir}",
        ]

        # AIE2P lowers the 8x8x8 mmul onto two bfp16-emulated macs, which this
        # selects; AIE2 lowers it onto four native bf16 macs and ignores it.
        # MM_FUSED_BFP16_B rides along, since bfp16ebs8 storage needs the
        # scalar BFP types.
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
        if self.rounding is Rounding.CONV_EVEN:
            # mm.cc's flag and polarity, reused: absent means the core's
            # power-up floor mode, though this operator defaults the other way.
            # Covers both conversions in the kernel, which must agree.
            flags.append("-DROUND_CONV_EVEN")

        kernel_obj = KernelObjectArtifact(
            self._kernel_object,
            dependencies=[
                SourceArtifact(in_tree_generic / "mm_fused.cc"),
                SourceArtifact(generic / "mm_fused_mmul.h"),
                SourceArtifact(generic / "activations.h"),
                SourceArtifact(kernels_dir / "aie_kernel_utils.h"),
                SourceArtifact(kernels_dir / kernel_dir / "zero.cc"),
            ],
            extra_flags=flags,
        )
        if self._link_file == self._kernel_object:
            return [kernel_obj]
        # The tanh LUT tables live in their own translation unit, so on AIE2
        # the kernel object alone leaves them undefined at link time.
        return [
            KernelArchiveArtifact(
                self._link_file,
                dependencies=[kernel_obj] + lut_based_ops_artifacts(kernel_dir),
            )
        ]

    def pack_B(self, B):
        """Reorder a row-major ``(K, N)`` weight matrix into consumption order.

        Flat uint8 bfp16ebs8 blocks on NPU2, flat bf16 on NPU1. Bound to the
        operator because the layout depends on the resolved ``tile_n`` and the
        device. Packing to consumption order is what makes both B hops linear
        descriptors, freeing the dimensions a deep k slice needs. See
        :mod:`iron.operators.flm.packing`.
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
            # On AIE2P B is quantized to bfp16ebs8, so it is declared in
            # bytes and sized from what pack_B returns; a (K, N) bf16 spec
            # would over-allocate by 1.78x. On AIE2 it is an element count.
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
