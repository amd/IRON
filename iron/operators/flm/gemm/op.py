# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""bf16 GEMM over a 4-row compute-tile grid, in the declared form.

The array is one configuration of the grid: the n tile, the A-tile height,
the row-block chunk, the activations compiled into the epilogue and the
rounding mode. Everything the xclbin depends on, and nothing else; its
``config_name`` is the xclbin's stem. M, K, N, the activation and the
clamp bounds are values written to the cores and reach only the
instruction stream, so every shape sharing a configuration shares one
xclbin. That split is the point of this operator; ``GEMM.configuration``
names the half an ``OperatorImage`` compiles once.

``design.py`` keeps the fixed geometry and the L1 budget; README.md has the
per-choice breakdown against the shipped FastFlowLM overlay
(``shipped``).
"""

import dataclasses
from typing import Any, ClassVar, NamedTuple

import numpy as np
from aie.dialects._aie_enum_gen import AIEArch, AIETileType, DMAChannelDir
from aie.dialects.aie import (
    get_target_model,
)
from aie.helpers.taplib import TensorAccessPattern
from aie.helpers.util import v8bfp16ebs8
from aie.iron import (
    Acquire,
    Bd,
    Buffer,
    DmaChannel,
    Flow,
    Lock,
    ObjectFifo,
    Release,
    TileDma,
    Worker,
    WorkerRuntimeBarrier,
)
from aie.iron.controlflow import range_
from aie.iron.device import Tile
from aie.iron.kernels import fused_mm
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import (
    Extent,
    In,
    Operator,
    Out,
    Unresolvable,
    Value,
    auto,
    param,
    Select,
)
from iron.common.design import BdLimits
from iron.operators.flm.gemm.design import (
    _VERIFIED_CT_K,
    A_DEPTH,
    B_MAX_SLOTS,
    BFP16_GROUP,
    BFP16_GROUP_BYTES,
    C_DEPTH,
    CT_MAX_K_FOR_N,
    CT_OUT_LEN,
    K_TILE,
    M_CHUNK_FOR_N,
    M_TILE,
    N_TILE_DEFAULT,
    RTP_CLAMP_MAX,
    RTP_CLAMP_MIN,
    RTP_EPILOGUE,
    RTP_K_ITERS,
    RTP_M_ROW_BLOCKS,
    RTP_N_VAL,
    STACK_SIZE,
    Epilogue,
    Gelu,
    R,
    Rounding,
    S,
    T,
    _b_bytes,
    _b_depth_for,
    _default_l1,
    _Slab,
    compute_rows,
    l1_budget,
    rtp_layout,
)
from iron.operators.flm.packing import pack_b, packed_b_size


class _BPool(NamedTuple):
    """B's memtile path as ``array()`` builds it, for ``sequence()`` to program.

    Per column: the pool buffer, one prod/cons lock pair per slot, the flow
    from the shim into it and the broadcast out of it. The limits are the
    target model's, read where the device is known.
    """

    mt_tiles: list
    bufs: list
    prod: list  # [column][slot]
    cons: list  # [column][slot]
    shim_flows: list
    bcast_flows: list
    slots: int
    slot_elems: int
    queue: int  # entries in a DMA channel's task queue, shim or memtile
    lock_max: int  # the largest value a lock holds
    passes: int  # passes one queue push makes over a memtile chain


def _clamp_bits(clamp) -> tuple[int, int]:
    """The clamp bounds as the int32 bit patterns the parameter words carry.

    No clamp means the identity bounds rather than a different build: min(x,
    +inf) and max(x, -inf) leave every finite value bit-identical.
    """
    lo, hi = clamp if clamp is not None else (-np.inf, np.inf)
    return (
        int(np.float32(lo).view(np.int32)),
        int(np.float32(hi).view(np.int32)),
    )


class GEMM(Operator):
    """AIE-accelerated bf16 GEMM on a 4-row grid, with a fused epilogue.

    64-row tiles over a k tile of ``k_tile`` (512 unless the caller asks), and
    an activation plus optional clamp folded into the output stage. M, K, N, the activation and the clamp bounds are
    values written to the cores: they change the instruction stream only, so
    every shape on one configuration shares an xclbin.

    The grid is as wide as the device. ``tile_n`` defaults to 64 from the
    device alone (the general winner; 128 beats it by ~9% only on NPU2 at
    K = 512, where the caller asks for it). ``tile_ma`` and ``m_chunk`` are
    filled from the device's L1 and the tuning tables.
    """

    M: int = param()
    K: int = param()
    N: int = param()
    # Activation fused into the C drain, selected at run time from the
    # compiled-in modes.
    epilogue: Epilogue | str = param(default=Epilogue.NONE)
    # Optional (min, max) applied after the activation.
    clamp: tuple | None = param(default=None)
    # B's packed block count on AIE2P: blocks, not bytes, since B's
    # declaration counts bfp16ebs8 blocks and bfp.itemsize turns that back
    # into the byte count pack_B returns.
    packed_blocks: int = param(
        default=lambda op: op.K * op.N // BFP16_GROUP, repr=False
    )
    # n tile width. 64 halves the mmul's accumulator traffic per mac; 128
    # halves A fetches instead. See README.md.
    tile_n: int = auto(array=True)
    # k tile. K must be a multiple of it, and it of the compute tile's k slice.
    # 256 is what Gemma 4's per-layer-input projection needs, its K being 256.
    k_tile: int = param(default=K_TILE, array=True)
    # A-tile rows, decoupled from the accumulator's M_TILE (asymmetric tile
    # buffering). None resolves to whatever L1 affords.
    tile_ma: int = auto(array=True)
    # Row-blocks folded into one B fetch. None resolves from tile_n.
    m_chunk: int = auto(array=True)
    # The activations the epilogue can select between at run time. Each one
    # compiled in costs program memory, so a deployment that dispatches two
    # should compile two.
    epilogue_modes: tuple = param(default=tuple(Epilogue), array=True)
    # Rounding for every f32->bf16 conversion; see Rounding in design.py.
    rounding: Rounding | str = param(default=Rounding.CONV_EVEN, array=True)
    # Arithmetic of the gelu epilogue; see Gelu in design.py. Only the gelu
    # mode reads it.
    gelu: Gelu | str = param(default=Gelu.FP32, array=True)
    # B as stored (N, K), a checkpoint's layout, read as is: the memtile lays
    # out the k panels the kernel reads as B^T blocks, so no packed copy.
    b_col_maj: bool = param(default=False, array=True)
    # Multiply on AIE2P's bfp16 macs, A and B rounded to bfp16ebs8 (the
    # port's arithmetic, and AIE2P's default), or on its bf16 macs.
    emulate_bf16_mmul_with_bfp16: bool = auto(array=True)
    # Filled by resolve, from the device: the grid, B's storage, the L2 tiles.
    rows: int = auto(repr=False)
    cols: int = auto(repr=False)
    bfp16_b: bool = auto(repr=False, array=True)
    # B's element type, on the array and in DDR alike; the host holds a
    # block-float B as bytes (BoundBuffer.host_dtype).
    b_dtype: Any = auto(repr=False)
    l1_b_depth: int = auto(repr=False, array=True)
    a_l2: int = auto(repr=False)
    b_l2: int = auto(repr=False)
    c_l2: int = auto(repr=False)

    # The k order pack_B writes within a block: the port's kernel's, or the
    # shipped binary's own (see shipped.py).
    b_overlay_order: ClassVar[bool] = False
    # The sequence writes the cores' parameters itself, behind the first
    # block's fills and once per slab; see sequence().
    own_preamble: ClassVar[bool] = True
    # A split leg's pieces outnumber the shim's BD ids, so the compiler
    # recycles finished tasks' ids. Safe here: no task waits on a push
    # issued after it (see sequence()'s emit_slab).
    aiecc_flags: ClassVar[tuple[str, ...]] = ("--reclaim-runtime-bds",)

    A = In(M, K, tile=(a_l2,), per=(rows,), depth=A_DEPTH)
    # Packed for bfp16 macs, B is quantized to bfp16ebs8, so it is declared
    # as a count of those blocks, the unit the array, the core and every
    # descriptor into B count in. Declared in bytes, the sequence's offsets
    # and lengths would address a ui8 buffer with block-unit numbers and a
    # transfer would move a ninth of what it named. Otherwise it is bf16, a
    # (K, N) count pre-packed, or (N, K) as stored under b_col_maj. Its lanes
    # are flows into each column's memtile pool, whose slots are one tile each.
    B = In(
        Select(bfp16_b, (packed_blocks,), (Select(b_col_maj, (N, K), (K, N)),)),
        dtype=b_dtype,
        tile=(b_l2,),
        per=(cols,),
    )
    C = Out(M, N, tile=(c_l2,), per=(cols,), depth=C_DEPTH)
    # M, or fewer rows per call (``A[:n]`` in a graph). Every row is streamed
    # and computed either way; the rows past the bound are not read.
    valid = Extent(M)
    # The parameter words every core reads once its barrier opens. The last
    # two exist only at m_chunk > 1 (rtp_layout); a word is not free.
    n_val = Value(np.int32, derive=lambda op: op.N)
    m_row_blocks = Value(np.int32, derive=lambda op: op._m_row_blocks)
    k_iters = Value(np.int32, derive=lambda op: op._k_iters)
    mode = Value(np.int32, derive=lambda op: Epilogue(op.epilogue).mode)
    clamp_min = Value(np.int32, derive=lambda op: _clamp_bits(op.clamp)[0])
    clamp_max = Value(np.int32, derive=lambda op: _clamp_bits(op.clamp)[1])
    n_chunks = Value(np.int32, derive=lambda op: op._n_units, optional=True)
    n_units = Value(np.int32, derive=lambda op: op._n_units, optional=True)

    def extent_unit(self, buffer: str) -> int:
        return 0  # nothing is shortened

    # -- checks ----------------------------------------------------------------

    def validate(self) -> None:
        if self.tile_n is not None:
            if self.tile_n not in CT_MAX_K_FOR_N:
                raise ValueError(
                    f"tile_n must be one of {sorted(CT_MAX_K_FOR_N)}, got {self.tile_n}"
                )
            ct_k = CT_MAX_K_FOR_N[self.tile_n]
            if (self.tile_n, ct_k) not in _VERIFIED_CT_K:
                raise ValueError(
                    f"tile_n={self.tile_n} with ct_max_k={ct_k} is not a verified "
                    f"combination (verified: {sorted(_VERIFIED_CT_K)}). It would "
                    f"build, run, and compute the WRONG ANSWER -- see "
                    f"_VERIFIED_CT_K. If you are retuning CT_MAX_K_FOR_N, fix that "
                    f"coupling first and add the pair here once a hardware test "
                    f"passes."
                )
        if self.tile_ma is not None and (
            M_TILE % self.tile_ma or self.tile_ma % (2 * R)
        ):
            raise ValueError(
                f"tile_ma ({self.tile_ma}) must divide {M_TILE} and be a multiple "
                f"of {2 * R}"
            )
        # Coerce so callers may pass bare strings; deduplicate, since the mask
        # ORs one bit per mode.
        self.rounding = Rounding(self.rounding)
        self.gelu = Gelu(self.gelu)
        self.epilogue_modes = tuple(
            dict.fromkeys(Epilogue(m) for m in self.epilogue_modes)
        )
        self.epilogue = Epilogue(self.epilogue)
        if self.K % self.k_tile:
            raise ValueError(
                f"K ({self.K}) must be a multiple of k_tile ({self.k_tile})"
            )
        self.check_derived("packed_blocks")
        # A mode the mask leaves out reaches the kernel's default arm, which
        # is NONE: an unactivated result rather than an error. Refuse.
        if (
            self.epilogue is not Epilogue.NONE
            and self.epilogue not in self.epilogue_modes
        ):
            raise ValueError(
                f"epilogue {self.epilogue} is not in epilogue_modes "
                f"{tuple(str(m) for m in self.epilogue_modes)}, so it would "
                "not be compiled in and the kernel would silently apply none"
            )
        if self.clamp is not None:
            lo, hi = self.clamp
            if lo > hi:
                raise ValueError(f"clamp min ({lo}) must be <= max ({hi})")

    def resolve(self, dev):
        if dev is None:
            raise Unresolvable("flm.GEMM is sized from the device's L1 and grid")
        rows, cols = compute_rows(dev), dev.cols
        # B is packed to bfp16ebs8 where the macs are bfp16 and B is not read
        # as stored; otherwise it is bf16. AIE2 has no BFP types, so its mmul
        # lowers onto four native bf16 macs.
        aie2p = dev.arch == AIEArch.AIE2p
        emulate = self.emulate_bf16_mmul_with_bfp16
        if emulate is None:
            emulate = aie2p
        if emulate and not aie2p:
            raise ValueError("flm.GEMM: bfp16 macs are AIE2P's")
        bfp16_b = emulate and not self.b_col_maj
        b_elem_bytes = BFP16_GROUP_BYTES / BFP16_GROUP if bfp16_b else 2
        b_group = BFP16_GROUP if bfp16_b else 1
        tile_n = N_TILE_DEFAULT if self.tile_n is None else self.tile_n
        ct_k = CT_MAX_K_FOR_N[tile_n]
        m_chunk = M_CHUNK_FOR_N[tile_n] if self.m_chunk is None else self.m_chunk
        l1 = l1_budget(dev, self.epilogue_modes)
        if self.tile_ma is None:
            tile_ma, l1_b_depth = _default_l1(tile_n, ct_k, b_elem_bytes, l1, m_chunk)
        else:
            tile_ma = self.tile_ma
            l1_b_depth = _b_depth_for(tile_ma, tile_n, ct_k, b_elem_bytes, l1, m_chunk)
        b_dtype = v8bfp16ebs8 if bfp16_b else bfloat16
        return dataclasses.replace(
            self,
            tile_n=tile_n,
            tile_ma=tile_ma,
            m_chunk=m_chunk,
            rows=rows,
            cols=cols,
            emulate_bf16_mmul_with_bfp16=emulate,
            bfp16_b=bfp16_b,
            b_dtype=b_dtype,
            l1_b_depth=l1_b_depth,
            a_l2=m_chunk * M_TILE * self.k_tile,
            b_l2=self.k_tile * tile_n // b_group,
            c_l2=M_TILE * tile_n * rows,
        )

    def _check_shape(self) -> None:
        # B_ITERS = k_tile // ct_max_k counts the B chunks one k step
        # consumes, so a k tile the compute tile's slice does not divide is
        # inexpressible.
        if self.k_tile % self.ct_max_k:
            raise ValueError(
                f"k_tile ({self.k_tile}) must be a multiple of ct_max_k "
                f"({self.ct_max_k}) for tile_n={self.tile_n}"
            )
        # N only needs to tile to tile_n: a trailing group of fewer than
        # cols column-blocks is handled by per-column trip counts.
        for name, value, unit in (
            ("M", self.M, M_TILE * self.rows),
            ("K", self.K, self.k_tile),
            ("N", self.N, self.tile_n),
        ):
            if value % unit != 0:
                raise ValueError(f"{name} ({value}) must be a multiple of {unit}")
        m_row_blocks = self.M // (M_TILE * self.rows)
        if m_row_blocks % self.m_chunk:
            # A partial group is inexpressible: the object is m_chunk tiles
            # wide and the forward always drains that much.
            raise ValueError(
                f"m_row_blocks ({m_row_blocks}) must be a multiple of m_chunk "
                f"({self.m_chunk}); pass m_chunk=1 for this shape"
            )

    def compatible(self) -> None:
        self._check_shape()

    # -- derived -----------------------------------------------------------------

    @property
    def _tuned(self) -> "GEMM":
        """This operator resolved for the current device, when construction
        left it unresolved: the names and the packing read fields resolution
        fills (tile_n, tile_ma, the B block depth), and both are wanted
        before the build resolves.
        """
        if self._resolved:
            return self
        return self.resolved()

    @property
    def ct_max_k(self) -> int:
        return CT_MAX_K_FOR_N[self.tile_n]

    @property
    def b_group(self) -> int:
        """B values per element of the array type: 8 per v8bfp16ebs8, 1 per bf16."""
        return BFP16_GROUP if self.bfp16_b else 1

    @property
    def epilogue_mask(self) -> int:
        """Bitmask of the modes compiled into the epilogue. Mode 0 is always
        present; the kernel falls back to it.
        """
        mask = 1
        for m in self.epilogue_modes:
            mask |= 1 << Epilogue(m).mode
        return mask

    @property
    def config_name(self) -> str:
        """Stem of the artifacts that do not depend on the shape: the xclbin's.

        ``kt`` names the k tile, which the kernel is compiled for. ``ck`` is
        named separately because retuning CT_MAX_K_FOR_N moves it
        while tn stays, and tile_ma is caller-overridable. Without it, an
        xclbin built at one ck could serve a request for another.
        """
        t = self._tuned
        dev = self.dev
        if dev is None:
            raise Unresolvable(
                "FLM GEMM: the xclbin is named for a device; none is bound"
            )
        return (
            f"FLM_GEMM_tn{t.tile_n}_kt{t.k_tile}_ck{t.ct_max_k}"
            f"_ma{t.tile_ma}_mc{t.m_chunk}"
            f"_em{t.epilogue_mask:x}_{t.rounding}"
            + ("" if t.gelu is Gelu.FP32 else f"_gelu_{t.gelu}")
            + ("_bt" if t.b_col_maj else "")
            + (
                "_bf16mac"
                if dev.arch == AIEArch.AIE2p and not t.emulate_bf16_mmul_with_bfp16
                else ""
            )
            + f"_{dev.name}"
        )

    @property
    def name(self) -> str:
        """Artifact stem for the instruction stream, which does depend on it.

        The configuration it runs on, then the runtime parameters on top.
        Every runtime parameter has to appear, because the sequence writes
        them as immediates and the build cache keys on filename: a stem that
        omits one serves the first caller's instruction stream to the
        second. The clamp bounds go in as raw bit patterns.
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

    # -- the array -------------------------------------------------------------

    def array(self, target) -> list:
        COLS, ROWS = self.cols, self.rows
        N_TILE, CT_MAX_K, M_CHUNK, T_MA = (
            self.tile_n,
            self.ct_max_k,
            self.m_chunk,
            self.tile_ma,
        )
        B_GROUP, L1_B_DEPTH, K_TILE = self.b_group, self.l1_b_depth, self.k_tile
        RHO = M_TILE // T_MA
        K_DIV_CT_K_MAX = K_TILE // CT_MAX_K
        CT_A_LEN = 2 * R * CT_MAX_K  # one z slice
        CT_A_OBJ = CT_A_LEN * (T_MA // R // 2)  # every z slice of one mmul
        C_SLICE_LEN = M_TILE * N_TILE  # one compute tile's C contribution
        O_CHUNKS = C_SLICE_LEN // CT_OUT_LEN  # C objects an accumulator drains as
        B_ITERS = K_TILE // CT_MAX_K  # B chunks consumed per k step
        rtp_slots, rtp_words = rtp_layout(M_CHUNK)
        tm = get_target_model(target.dev.resolve())

        bf16_ty = np.dtype[bfloat16]
        f32 = np.dtype[np.float32]
        b_elem_ty = np.dtype[self.b_dtype]
        # L1 (per compute tile)
        ct_a_obj_ty = np.ndarray[(CT_A_OBJ,), bf16_ty]
        ct_b_ty = np.ndarray[(CT_MAX_K * N_TILE // B_GROUP,), b_elem_ty]
        ct_out_ty = np.ndarray[(CT_OUT_LEN,), bf16_ty]
        ct_acc_ty = np.ndarray[(M_TILE * N_TILE,), f32]
        # L2 (per memtile): the declared stream tiles.
        mt_a_ty = self.A.tile
        mt_out_ty = self.C.tile

        # Every field that changes the object reaches the factory, so its
        # object name keys the build. The activation is absent: the cores
        # select it at run time from the compiled-in modes, and mode 0 is
        # always compiled in, since the kernel falls back to it. Under
        # asymmetric tile buffering the k step takes the A band index, as the
        # core folds RHO A bands into one accumulator.
        modes = dict.fromkeys([Epilogue.NONE, *self.epilogue_modes])
        kernel = fused_mm(
            dim_m=M_TILE,
            dim_k=K_TILE,
            dim_n=N_TILE,
            band_m=T_MA,
            chunk_k=CT_MAX_K,
            out_chunk=CT_OUT_LEN,
            c_depth=C_DEPTH,
            # 8x8x8 on both architectures: AIE2P lowers it onto one bfp16 mac
            # or two bf16 ones, AIE2 onto four native bf16 macs.
            mmul_shape=(R, S, T),
            bfp16_b=self.bfp16_b,
            b_col_maj=self.b_col_maj,
            emulate_bf16_mmul_with_bfp16=self.emulate_bf16_mmul_with_bfp16,
            epilogue_modes=tuple(str(m) for m in modes),
            rounding=str(self.rounding),
            gelu=str(self.gelu),
        )
        acc_init = kernel.mm_fused_acc_init
        k_step = kernel.mm_fused_k_step
        epilogue_chunk = kernel.mm_fused_epilogue_chunk

        # --- Data movement ------------------------------------------------
        # These turn a row-major DDR tile into the blocked layout the mmul
        # indexes. A mismatch is silently wrong, not a build error.
        gather_dims = TensorAccessPattern.full((M_TILE, N_TILE)).tile((R, T))
        a_bands = M_CHUNK * M_TILE // R
        a_recv_dims = TensorAccessPattern.full((a_bands, K_TILE // S, R, S)).permute(
            (0, 2, 1, 3)
        )
        # Emits (b_iter, mc, band): the order the core acquires A in while
        # holding a B chunk across the group.
        # A mem tile's run is bounded in elements; one past the wrap splits.
        a_split = BdLimits.of(target.dev, 0, 1).factor(R * CT_MAX_K)
        assert a_split is not None
        a_hi, a_lo = a_split
        a_send_dims = TensorAccessPattern.full(
            (a_bands, K_DIV_CT_K_MAX, R * CT_MAX_K)
        ).permute((1, 0, 2))
        if a_hi > 1:
            a_send_dims = a_send_dims.split(2, a_lo)

        # No tile is pinned: column c and row r name logical tiles, and the
        # placer decides where each lands. One object per logical tile, since
        # tiles are told apart by identity. Typed up front: Flow reads
        # tile_type to find its shim end, and nothing else stamps these.
        shim_tiles = [Tile(tile_type=AIETileType.ShimNOCTile) for _ in range(COLS)]
        mt_tiles = [Tile(tile_type=AIETileType.MemTile) for _ in range(COLS)]
        ct_tiles = [
            [Tile(tile_type=AIETileType.CoreTile) for _ in range(COLS)]
            for _ in range(ROWS)
        ]

        # C: one join per column; each of the ROWS cores drops its slice at
        # its own offset in a single memtile buffer.
        c_l2l3_fifos, c_prod = [], {}
        for c in range(COLS):
            of_c = ObjectFifo(mt_out_ty, name=f"C_L2L3_{c}", depth=C_DEPTH)
            c_l2l3_fifos.append(of_c)
            sub = of_c.prod().join(
                [C_SLICE_LEN * r for r in range(ROWS)],
                tile=mt_tiles[c],
                obj_types=[ct_out_ty] * ROWS,
                names=[f"C_L1L2_{c}_{r}" for r in range(ROWS)],
                from_stream=[gather_dims] * ROWS,
            )
            for r in range(ROWS):
                c_prod[(r, c)] = sub[r]

        # A: shim -> memtile -> broadcast along the compute row, reblocking on
        # the forward(). One fifo per row even at M_CHUNK > 1: a second would
        # want a third core input DMA channel, and a tile has two.
        a_l3l2_fifos, a_cons = [], {}
        for r in range(ROWS):
            of_a_in = ObjectFifo(mt_a_ty, name=f"A_L3L2_{r}", depth=A_DEPTH)
            a_l3l2_fifos.append(of_a_in)
            of_a = of_a_in.cons(from_stream=a_recv_dims).forward(
                tile=mt_tiles[r * COLS // ROWS],
                obj_type=ct_a_obj_ty,
                depth=A_DEPTH,
                name=f"A_L2L1_{r}",
                to_stream=a_send_dims,
            )
            for c in range(COLS):
                a_cons[(r, c)] = of_a.cons()

        # B: shim -> memtile slot pool -> broadcast down the compute column,
        # over explicit flows, buffers and locks. The flows name no channel:
        # the compiler assigns them around A and C, and the DMA programs below
        # run on each flow's endpoint rather than an index. Everything
        # declared here is shape-independent, so it lives in the shared
        # xclbin. What varies per shape -- how the slots are filled and
        # replayed -- is the sequence's BD programming.
        #
        # The pool takes what the memtile has left once A and C are placed,
        # capped at B_MAX_SLOTS. Budgeted as if every memtile held an A
        # forward, though only every (COLS // ROWS)-th does, so a slot count
        # is the same on every column.
        b_slot_elems = K_TILE * N_TILE // B_GROUP
        b_slot_bytes = _b_bytes(K_TILE * N_TILE, self.bfp16_b)
        mt_free = (
            tm.get_mem_tile_size()
            - A_DEPTH * M_CHUNK * M_TILE * K_TILE * 2
            - C_DEPTH * C_SLICE_LEN * ROWS * 2
        )
        B_SLOTS = min(B_MAX_SLOTS, mt_free // b_slot_bytes)
        if B_SLOTS < 1:
            raise ValueError(
                f"no room for a {b_slot_bytes}-byte B slot in the memtile at "
                f"tile_n={N_TILE}; {mt_free} bytes remain after A and C"
            )
        b_mt_ty = np.ndarray[(B_SLOTS * b_slot_elems,), b_elem_ty]
        b_mt_bufs = [
            Buffer(b_mt_ty, name=f"b_mt_{c}", tile=mt_tiles[c]) for c in range(COLS)
        ]
        # One lock pair per slot, not per pool: a resident slot is consumed
        # once per unit and refilled only when all of them have, independently
        # of the other slots, so the next column-block's refill trails the
        # replay by one slot instead of waiting for the whole block.
        # Flows, locks and DMAs only the sequence and descriptors reach.
        unrouted: list = []
        b_mt_prod, b_mt_cons = [], []
        for c in range(COLS):
            for locks, side in ((b_mt_prod, "prod"), (b_mt_cons, "cons")):
                slots = [
                    Lock(mt_tiles[c], init=0, name=f"b_mt_{side}_{c}_{i}")
                    for i in range(B_SLOTS)
                ]
                locks.append(slots)
                unrouted += slots
        b_shim_flows = [
            Flow(shim_tiles[c], mt_tiles[c], shim_symbol=f"B_L3L2_{c}")
            for c in range(COLS)
        ]
        unrouted += b_shim_flows
        # One source, ROWS destinations: a circuit-switched broadcast.
        b_bcast_flows = [
            Flow(mt_tiles[c], [ct_tiles[r][c] for r in range(ROWS)])
            for c in range(COLS)
        ]
        unrouted += b_bcast_flows

        # The cores' end is static: a ring of L1_B_DEPTH buffers any shape
        # uses the same way, filled by a looping BD chain and consumed under
        # the same prod/cons lock pair an ObjectFifo would have generated.
        b_l1 = {}
        for r in range(ROWS):
            for c in range(COLS):
                tile = ct_tiles[r][c]
                bufs = [
                    Buffer(ct_b_ty, name=f"b_l1_{r}_{c}_{d}", tile=tile)
                    for d in range(L1_B_DEPTH)
                ]
                prod = Lock(tile, init=L1_B_DEPTH, name=f"b_l1_prod_{r}_{c}")
                cons = Lock(tile, init=0, name=f"b_l1_cons_{r}_{c}")
                b_l1[(r, c)] = (bufs, prod, cons)
                unrouted += [prod, cons]
                unrouted.append(
                    TileDma(
                        tile,
                        [
                            DmaChannel(
                                DMAChannelDir.S2MM,
                                b_bcast_flows[c].endpoint(tile),
                                [
                                    Bd(
                                        buf,
                                        acquires=[Acquire(prod)],
                                        releases=[Release(cons)],
                                        next=(d + 1) % L1_B_DEPTH,
                                    )
                                    for d, buf in enumerate(bufs)
                                ],
                            )
                        ],
                    )
                )

        # What sequence() programs per shape, and the limits it plans against.
        self._b_pool = _BPool(
            mt_tiles=mt_tiles,
            bufs=b_mt_bufs,
            prod=b_mt_prod,
            cons=b_mt_cons,
            shim_flows=b_shim_flows,
            bcast_flows=b_bcast_flows,
            slots=B_SLOTS,
            slot_elems=b_slot_elems,
            queue=tm.get_dma_task_queue_depth(),
            lock_max=tm.get_max_lock_value(),
            passes=tm.get_max_repeat_count() + 1,
        )

        # Data, not an immediate folded into the program: the core programs
        # differ only in symbol names.
        my_cols = [
            [
                Buffer(
                    np.ndarray[(1,), np.dtype[np.int32]],
                    name=f"my_col_{r}_{c}",
                    initial_value=np.array([c], dtype=np.int32),
                )
                for c in range(COLS)
            ]
            for r in range(ROWS)
        ]
        rtps = [
            [
                Buffer(
                    np.ndarray[(rtp_words,), np.dtype[np.int32]],
                    name=f"rtp_{r}_{c}",
                    initial_value=np.zeros(rtp_words, dtype=np.int32),
                    use_write_rtp=True,
                )
                for c in range(COLS)
            ]
            for r in range(ROWS)
        ]
        barriers = [[WorkerRuntimeBarrier() for _ in range(COLS)] for _ in range(ROWS)]

        # --- Compute ------------------------------------------------------
        def core_fn(
            accs,
            o_h,
            b_bufs,
            b_prod,
            b_cons,
            a_h,
            init_k,
            kstep_k,
            epi_k,
            my_rtp,
            my_col,
            barrier,
        ):
            """Core body. Every trip count and the activation come from the
            runtime parameter buffer, so one core program serves every shape.
            """
            barrier.wait_for_value(1)
            # Derived rather than sent, saving an RTP word: column c has work
            # in block j iff (j*COLS + c)*N_TILE < N. Both divisors are powers
            # of two, so this must leave no __divsi3; check the .o.
            n_tiles = my_rtp[RTP_N_VAL] // N_TILE
            n_work = (n_tiles - my_col[0] + COLS - 1) // COLS
            n_drain = ((n_tiles + COLS - 1) // COLS) - n_work
            n_row_blocks = my_rtp[RTP_M_ROW_BLOCKS]
            n_k_iters = my_rtp[RTP_K_ITERS]
            epi_mode = my_rtp[RTP_EPILOGUE]
            clamp_min_bits = my_rtp[RTP_CLAMP_MIN]
            clamp_max_bits = my_rtp[RTP_CLAMP_MAX]
            if "n_chunks" in rtp_slots:
                n_chunks = my_rtp[rtp_slots["n_chunks"]]
                n_units_rt = my_rtp[rtp_slots["n_units"]]
            else:
                n_chunks = n_row_blocks
                n_units_rt = n_row_blocks
            # Acquire does not consume the barrier, so take it back to zero or
            # the next dispatch re-reads these instead of waiting. Safe before
            # the work: the sequence cannot re-set it until this dispatch's C
            # drains.
            barrier.release_with_value(1)

            def sweep(group):
                """One k reduction feeding ``group`` accumulators off a shared B."""
                for a_acc in group:
                    init_k(a_acc)
                for _ in range_(n_k_iters):
                    # Unrolled by the ring depth, so each buffer is a fixed
                    # symbol. The DMA's ring and this walk stay in step
                    # because a k step consumes B_ITERS chunks, which the
                    # depth divides.
                    for _ in range_(B_ITERS // L1_B_DEPTH):
                        for b in b_bufs:
                            b_cons.acquire(1)
                            for a_acc in group:
                                for band in range(RHO):
                                    a = a_h.acquire(1)
                                    kstep_k(a, b, a_acc, band)
                                    a_h.release(1)
                            b_prod.release(1)
                # Unrolled by C_DEPTH; a full O_CHUNKS unroll overflows
                # program memory.
                for a_acc in group:
                    for chunk in range_(O_CHUNKS // C_DEPTH):
                        for half in range(C_DEPTH):
                            o = o_h.acquire(1)
                            epi_k(
                                o,
                                a_acc,
                                chunk,
                                half,
                                epi_mode,
                                clamp_min_bits,
                                clamp_max_bits,
                            )
                            o_h.release(1)

            for _ in range_(n_work):
                for _ in range_(n_chunks):
                    sweep(accs)

            # Column-blocks this column sits out. A is broadcast along the
            # row, so it must still consume its share or the columns that do
            # have work stall on the fifo. No B and no C; the sequence issues
            # neither.
            for _ in range_(n_drain):
                for _ in range_(n_units_rt):
                    for _ in range_(n_k_iters):
                        for _ in range_(B_ITERS // L1_B_DEPTH):
                            for _ in range(L1_B_DEPTH):
                                for _ in range(M_CHUNK * RHO):
                                    a_h.acquire(1)
                                    a_h.release(1)

        workers = []
        for r in range(ROWS):
            for c in range(COLS):
                accs = [
                    Buffer(type=ct_acc_ty, name=f"c_acc_{r}_{c}_{mc}")
                    for mc in range(M_CHUNK)
                ]
                b_bufs, b_prod, b_cons = b_l1[(r, c)]
                workers.append(
                    Worker(
                        core_fn,
                        [
                            accs,
                            c_prod[(r, c)].prod(),
                            b_bufs,
                            b_prod,
                            b_cons,
                            a_cons[(r, c)],
                            acc_init,
                            k_step,
                            epilogue_chunk,
                            rtps[r][c],
                            my_cols[r][c],
                            barriers[r][c],
                        ],
                        tile=ct_tiles[r][c],
                        stack_size=STACK_SIZE,
                    )
                )

        for r in range(ROWS):
            self.A.lane(r).bind(a_l3l2_fifos[r].prod())
        for c in range(COLS):
            self.B.lane(c).bind(b_shim_flows[c])
            self.C.lane(c).bind(c_l2l3_fifos[c].cons())
        flat = [b for row in rtps for b in row]
        self.n_val.bind(flat, RTP_N_VAL)
        self.m_row_blocks.bind(flat, RTP_M_ROW_BLOCKS)
        self.k_iters.bind(flat, RTP_K_ITERS)
        self.mode.bind(flat, RTP_EPILOGUE)
        self.clamp_min.bind(flat, RTP_CLAMP_MIN)
        self.clamp_max.bind(flat, RTP_CLAMP_MAX)
        if "n_chunks" in rtp_slots:
            self.n_chunks.bind(flat, rtp_slots["n_chunks"])
            self.n_units.bind(flat, rtp_slots["n_units"])
        return workers + unrouted + [b for row in barriers for b in row]

    # -- geometry of one dispatch ------------------------------------------------

    @property
    def _m_row_blocks(self) -> int:
        return self.M // (M_TILE * self.rows)

    @property
    def _k_iters(self) -> int:
        return self.K // self.k_tile

    @property
    def _n_units(self) -> int:
        """Groups of m_chunk row-blocks; every leg is issued per unit."""
        return self._m_row_blocks // self.m_chunk

    # -- the runtime sequence --------------------------------------------------

    def sequence(self, rt):
        M, K, N = self.M, self.K, self.N
        COLS, ROWS = self.cols, self.rows
        N_TILE, M_CHUNK, K_TILE = self.tile_n, self.m_chunk, self.k_tile
        k_iters, n_units = self._k_iters, self._n_units
        pool = self._b_pool
        B_SLOTS, b_slot_elems = pool.slots, pool.slot_elems
        # Sweeps where all COLS columns have work, plus a trailing group of
        # rem_blocks columns (0 <= rem_blocks < COLS) that do one block more.
        n_full = N // (N_TILE * COLS)
        rem_blocks = (N % (N_TILE * COLS)) // N_TILE

        # One transfer per (column-block, leg), not one per object: a
        # descriptor walks many fifo objects in consume order. Dimension
        # order must match the core's nest.
        A = TensorAccessPattern.full((n_units, M_CHUNK, ROWS, M_TILE, k_iters, K_TILE))

        def a_tap(r, slab):
            # Every (row-block, k) block this row consumes for one
            # column-block: per unit, k outermost, then the unit's
            # row-blocks. A does not depend on the column-block; it is
            # re-fetched because the cores re-consume it.
            rows = A[slab.first : slab.first + slab.units, :, r]
            return rows.permute((0, 3, 1, 2, 4))

        # B's slot pool, per shape. Resident where the column-block fits: DDR
        # reads it once and the memtile replays it n_units times. Otherwise
        # the pool is a plain ring and DDR re-reads B per unit, as a fifo
        # would.
        #
        # Each slot is filled when its producer lock reaches b_uses and
        # released by b_uses per fill, then drained once per use. So a
        # resident slot is not refilled until every unit has read it, while a
        # streamed one turns over like a fifo object. Both return the
        # producer lock to b_uses by the end of the slab, which the sequence
        # re-arms per slab since the previous one may have been a different
        # shape.
        def make_slab(first, units):
            """The plan for ``units`` units from unit ``first``, armed at once."""
            if k_iters <= B_SLOTS and units <= pool.lock_max:
                resident, b_slots, b_uses = True, k_iters, units
            else:
                # Streamed, a chain pass must cover whole units, so the ring
                # must divide what one takes.
                b_slots = max(
                    s for s in range(1, B_SLOTS + 1) if (units * k_iters) % s == 0
                )
                resident, b_uses = False, 1
            return _Slab(first, units, resident, b_slots, b_uses)

        def n_work(c):
            """Count the column-blocks, from the first, that column ``c`` works on."""
            return n_full + (1 if c < rem_blocks else 0)

        def b_mt_block_passes(slab):
            """(fill, drain) passes over the used slots per column-block."""
            if slab.b_resident:
                return 1, slab.units
            passes = slab.units * k_iters // slab.b_slots
            return passes, passes

        # M is cut into slabs of units, each armed once the last one's C has
        # drained -- the state between two dispatches, which the cores cannot
        # tell from one. Cut where a column-block's memtile pushes would not
        # fit one task queue: they go out ahead of the block's C (see
        # emit_slab), and one past the queue waits on the block's own first,
        # so on that C. Also cut where it keeps B resident past lock_max
        # units: B is then read once per slab instead of once per unit.
        def slab_fits(slab):
            return all(
                passes <= pool.queue * pool.passes for passes in b_mt_block_passes(slab)
            )

        def cut(n_slabs):
            size, extra = divmod(n_units, n_slabs)
            slabs, first = [], 0
            for i in range(n_slabs):
                units = size + (1 if i < extra else 0)
                slabs.append(make_slab(first, units))
                first += units
            return slabs

        for n_slabs in range(1, n_units + 1):
            slabs = cut(n_slabs)
            if all(map(slab_fits, slabs)) and (
                k_iters > B_SLOTS or all(s.b_resident for s in slabs)
            ):
                break
        else:
            raise ValueError(
                f"M={M} K={K} N={N}: even one unit per slab needs more passes "
                f"over a B pool per column-block than the {pool.queue} x "
                f"{pool.passes} one memtile channel can queue"
            )

        if self.b_col_maj:
            # A slot is the (N_TILE, K_TILE) block as stored, k_tile-long runs.
            B = TensorAccessPattern.full(
                (N // N_TILE, N_TILE, k_iters, K_TILE)
            ).permute((0, 2, 1, 3))
        else:
            B = TensorAccessPattern.full((N // N_TILE, k_iters, b_slot_elems))[
                :, :, None
            ]

        def b_tap(mega_col, c, slab):
            # Every (mega_row, k) chunk this column consumes. B arrives
            # pre-packed, or under b_col_maj as stored, so each slot is
            # k_tile-long runs or longer; reordering into the kernel's blocks
            # here instead gives an innermost run of T=8 bf16 and measured
            # 5.4x slower, so b_col_maj's reorder is the memtile's.
            #
            # Resident, one k sweep for the whole column-block. Otherwise one
            # per unit, not per row-block: the cores hold each B chunk across
            # a group. The unit dimension has stride 0 because B does not
            # depend on the row.
            sweeps = 1 if slab.b_resident else slab.units
            return B[mega_col * COLS + c].repeat(sweeps)

        slots = TensorAccessPattern.full((B_SLOTS * b_slot_elems,)).partition(B_SLOTS)
        if self.b_col_maj:
            # Each s-deep k panel, every n row of it: the kernel's B^T blocks.
            drains = TensorAccessPattern.full(
                (B_SLOTS, N_TILE, K_TILE // S, S)
            ).permute((0, 2, 1, 3))
        else:
            drains = slots

        def start_b_mt(c, direction, passes, slab):
            """Program and start one of column ``c``'s memtile B channels.

            The chain is one BD per used slot, walked ``passes`` times; past
            what one queue push carries, the compiler pushes it again. The
            task is returned for restarting, and never awaited: C completing
            implies it.
            """
            fill = direction == DMAChannelDir.S2MM
            flow = (pool.shim_flows if fill else pool.bcast_flows)[c]
            value = slab.b_uses if fill else 1
            chain = []
            for i in range(slab.b_slots):
                prod, cons = pool.prod[c][i], pool.cons[c][i]
                wait, post = (prod, cons) if fill else (cons, prod)
                chain.append(
                    Bd(
                        pool.bufs[c],
                        tap=(slots if fill else drains)[i],
                        acquires=[Acquire(wait, value=value)],
                        releases=[Release(post, value=value)],
                    )
                )
            return flow.endpoint(pool.mt_tiles[c]).task(*chain, runs=passes).start()

        C = TensorAccessPattern.full(
            (M // (ROWS * M_TILE), ROWS * M_TILE, N // N_TILE, N_TILE)
        )

        def c_tap(mega_col, c, slab):
            # Every joined block this column produces: one ROWS*M_TILE x
            # N_TILE per row-block, in plain row-block order even under
            # M_CHUNK.
            row_blocks = slice(
                slab.first * M_CHUNK, (slab.first + slab.units) * M_CHUNK
            )
            return C[row_blocks, :, mega_col * COLS + c]

        # A trailing block uses only the first rem_blocks columns. A is still
        # issued for every row, since the sitting-out columns drain it.
        blocks = [(mc, COLS) for mc in range(n_full)]
        if rem_blocks:
            blocks.append((n_full, rem_blocks))

        def emit_slab(slab):
            # Per-slab setup: arming B's memtile channels and the cores'
            # parameters. Neither is free -- together tens of microseconds of
            # command-processor time -- so it goes out *behind* the first
            # block's A and B fills, overlapping their DDR latency. A fill
            # running ahead of it is harmless: A only lands in fifo buffers,
            # and B backs up in the stream until its memtile channel has a
            # task. Measured on the benchmark shapes, arming first cost up to
            # +30 us (+9%) at M=256.
            #
            # Nothing ahead of it may wait on the cores, which are not
            # released yet. The only waits are the compiler's, for a queue
            # slot or a buffer descriptor, and here everything they can wait
            # on is an earlier slab's.
            b_mt_tasks = {}

            def push_b_mt(bi):
                """Push B's memtile chains for the chunks starting at block ``bi``.

                A push covers as many whole blocks as one push's passes carry
                and goes out at the first of them. Every push the compiler
                then waits on for a queue slot is an earlier block's, whose
                fills and C are already issued; pushing a whole slab up front
                would wait on fills not issued yet.
                """
                for c in range(COLS):
                    if bi >= n_work(c):
                        continue
                    for direction, passes in zip(
                        (DMAChannelDir.S2MM, DMAChannelDir.MM2S),
                        b_mt_block_passes(slab),
                    ):
                        per_push = max(1, pool.passes // passes)
                        if bi % per_push:
                            continue
                        count = min(per_push, n_work(c) - bi) * passes
                        task = b_mt_tasks.get((c, direction))
                        if task is None:
                            b_mt_tasks[c, direction] = start_b_mt(
                                c, direction, count, slab
                            )
                        else:
                            task.start(repeat_count=count - 1)

            def set_up():
                # Arm B's pools: only the slots this slab uses. A consumer
                # lock is always back at 0 by the end of a slab, so only the
                # producer side needs setting, and before its channel starts.
                for c in range(COLS):
                    if n_work(c):
                        for i in range(slab.b_slots):
                            pool.prod[c][i].set(slab.b_uses)
                push_b_mt(0)
                # Every core's parameters for this slab, then every barrier.
                rt.preamble(
                    m_row_blocks=slab.units * M_CHUNK,
                    n_chunks=slab.units,
                    n_units=slab.units,
                )

            # Every transfer is unmanaged: the compiler meters each channel's
            # queue and takes a descriptor back once a poll proves its
            # transfer done. A column's C drains in order on one channel, and
            # its last one finishing means the column's slab is done -- fills,
            # memtile chains and cores -- so only that one carries a token.
            last_c = []

            # C goes out after its block's fills, since the first C only
            # arrives after a whole k sweep. A leg whose pattern the shim
            # cannot take in one descriptor, or that needs more of them than a
            # task queue holds, the compiler cuts into pieces and interleaves
            # with the other legs'.
            for bi, (mega_col, active_cols) in enumerate(blocks):
                for r in range(ROWS):
                    rt.fill(self.A.lane(r), (self.A, a_tap(r, slab)), managed=False)
                for c in range(active_cols):
                    rt.fill(
                        self.B.lane(c),
                        (self.B, b_tap(mega_col, c, slab)),
                        managed=False,
                    )
                if bi == 0:
                    set_up()
                else:
                    push_b_mt(bi)
                for c in range(active_cols):
                    last = bi == n_work(c) - 1
                    task = rt.drain(
                        self.C.lane(c),
                        (self.C, c_tap(mega_col, c, slab)),
                        wait=last,
                        managed=False,
                    )
                    if last:
                        last_c.append(task)
            for task in last_c:
                task.await_()

        # Back to back: a slab returns only once its C has all drained.
        for slab in slabs:
            emit_slab(slab)

    # -- packaging: one xclbin per configuration ----------------------------------

    @property
    def _reference_shape(self) -> tuple[int, int, int]:
        """The shape the configuration-only module is emitted at: the smallest
        valid one, so the shape-independence is explicit.
        """
        return (M_TILE * self.rows * self.m_chunk, self.k_tile, self.tile_n * self.cols)

    def configuration(self):
        """This configuration at its reference shape and activation.

        Its xclbin is built once and serves every shape sharing the
        configuration: the cache keys on content, and the reference shape is
        what that content is. Only the instruction stream is per shape, an
        instructions-only compile with no kernel built twice.
        """
        M, K, N = self._reference_shape
        return dataclasses.replace(
            self, M=M, K=K, N=N, epilogue=Epilogue.NONE, clamp=None, packed_blocks=None
        )

    # -- host-side helpers -------------------------------------------------------

    def pack_B(self, B):
        """Reorder a row-major ``(K, N)`` weight matrix into consumption order.

        Flat uint8 bfp16ebs8 blocks on NPU2, flat bf16 on NPU1. Packing to
        consumption order is what makes both B hops linear descriptors. See
        ``iron.operators.flm.packing``.

        Raises:
            ValueError: Under ``b_col_maj``, which reads B as stored.
        """
        t = self._tuned
        if t.b_col_maj:
            raise ValueError("flm.GEMM(b_col_maj=True) reads B as stored (N, K)")
        return pack_b(
            B,
            k_tile=t.k_tile,
            n_tile=t.tile_n,
            s=S,
            t=T,
            ct_k=t.ct_max_k,
            bfp16=bool(t.bfp16_b),
            round_conv_even=t.rounding is Rounding.CONV_EVEN,
            overlay_order=t.b_overlay_order,
        )

    def packed_B_size(self, K, N):
        """Elements (bf16) or bytes (bfp16ebs8) that ``pack_B`` returns."""
        return packed_b_size(K, N, bool(self._tuned.bfp16_b))

    def ops(self) -> int:
        return 2 * self.M * self.K * self.N

    def reference(self, A, B):
        """``C = clamp(epilogue(A @ B))``, in the kernel's order of operations.

        The product accumulates in float32, as the kernel's f32 accumulator
        does, and is rounded to the output dtype before the epilogue and the
        clamp, because ``mm_fused_epilogue_chunk`` converts the accumulator
        to bf16 and applies the activation to that. End to end the order is
        second order (at M=256 K=512 N=1024 it moves mean |err| by under
        2e-4), but against the device's own accumulator on the shipped
        overlay it moves silu's worst-case disagreement from 0.043 to 0.031.

        Not bit-exact, and cannot be: the hardware's activation is a LUT on
        aie2 and a native instruction on aie2p, worth up to ~0.02 absolute,
        which the tolerance absorbs. ``B`` is ``(N, K)`` under ``b_col_maj``.
        """
        b = B.T if self.b_col_maj else B
        C = np.matmul(A.astype(np.float32), b.astype(np.float32)).astype(A.dtype)
        return Epilogue(self.epilogue).apply(C, self.clamp)

    def tolerance(self) -> Tolerance | None:
        """Each element of C within the roundings the kernel makes, in units
        of 2^-8 of ``|A| @ |B|``: under 2 for C's conversion to bf16, even
        truncating, and K * 2^-16 for the f32 accumulator. bfp16 macs round
        A and B to bfp16ebs8 as well, 2 units more to nearest and 8
        truncating.

        A clamp moves no element further from its reference; an activation's
        approximation is not bounded here, so an activated GEMM has none. On
        npu2 over K = 512 to 8192, normal and all-positive inputs, no
        configuration's worst element came above 0.89 of it.
        """
        if self.epilogue is not Epilogue.NONE:
            return None
        units = 2.0 + self.K * 2.0**-16
        if self.emulate_bf16_mmul_with_bfp16:
            units += 2.0 if self.rounding is Rounding.CONV_EVEN else 8.0

        def bound(A, B):
            b = B.T if self.b_col_maj else B
            return (
                units
                * 2.0**-8
                * (np.abs(A.astype(np.float32)) @ np.abs(b.astype(np.float32)))
            )

        return Tolerance.bounded(bound, note=f"{units:g} units of |A| @ |B|")
