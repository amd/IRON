# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""bf16 GEMM over a 4-row compute-tile grid, in the declared form.

``design.py`` keeps the fixed geometry and the L1 budget; README.md has the
per-choice breakdown against the shipped FastFlowLM overlay (``shipped``).
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
    In,
    Lock,
    ObjectFifo,
    Out,
    Release,
    TileDma,
    Worker,
    ceildiv,
)
from aie.iron.controlflow import range_
from aie.iron.device import Tile
from aie.iron.kernels import fused_mm
from aie.utils import bfp, set_current_device
from aie.utils.compile.jit.context import compile_context
from aie.utils.compile.jit.params import Select, divisors, param, per_call, tunable
from aie.utils.compile.utils import resolve_target_arch
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Precision, Rtp, Unresolvable
from iron.operators.flm.gemm.design import (
    A_DEPTH,
    B_MAX_SLOTS,
    C_DEPTH,
    C_JOINS,
    CT_OUT_LEN,
    K_TILE,
    M_TILE,
    N_TILE_DEFAULT,
    TILE_NS,
    Epilogue,
    Gelu,
    R,
    Rounding,
    S,
    T,
    _b_bytes,
    _Slab,
    compute_rows,
    l1_tiles,
)
from iron.operators.flm.packing import pack_b


class _BPool(NamedTuple):
    """B's memtile path as ``build()`` builds it, for ``sequence()`` to program.

    Per column, the pool buffer, one prod/cons lock pair per slot, and the
    shim-in/broadcast-out flows. Limits are the target model's.
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


# The kernel's clamp bounds as the int32 bit patterns the parameter words
# carry: the identity, min(x, +inf) and max(x, -inf), which leave every
# finite value bit-identical.
CLAMP_BITS = (
    int(np.float32(-np.inf).view(np.int32)),
    int(np.float32(np.inf).view(np.int32)),
)


# ProjectionGEMM.frame's, by device, tiles and the fields its kernel reads.
_FRAMES: dict[tuple, int] = {}


def _compiled_modes(epilogue_modes) -> tuple[Epilogue, ...]:
    """Mode 0, then ``epilogue_modes``."""
    return tuple(dict.fromkeys([Epilogue.NONE, *map(Epilogue, epilogue_modes)]))


@dataclasses.dataclass(frozen=True, kw_only=True)
class _Built(Built):
    """ProjectionGEMM's build, with B's memtile pool for ``sequence()`` to program."""

    b_pool: _BPool


def _units_valid(op) -> Any:
    """Return the 256-row units a call's row bound reaches, at least one.

    Raises:
        ValueError: A call with no rows, which would end before the cores
            drain the B its units past the bound still receive.
    """
    rows = op.valid
    if isinstance(rows, (int, np.integer)) and rows < 1:
        raise ValueError(f"flm.ProjectionGEMM: valid ({rows}) must be at least 1 row")
    return ceildiv(rows, M_TILE * op.rows * op.m_chunk)


class ProjectionGEMM(Operator):
    """AIE-accelerated bf16 GEMM on a 4-row grid, as wide as the device.

    With a fused epilogue. M, K, N and the activation are values written to
    the cores, so every shape on one ``config_name`` shares an xclbin. Used
    wherever ``iron.operators.GEMM`` doesn't apply (a weight operand,
    MEDIUM/HIGH, two or more rows).
    """

    M: int = param()
    K: int = param()
    N: int = param()
    # The activation, selected at run time from the compiled-in modes; its
    # gelu is x * sigmoid(1.702x), the port's own arithmetic.
    epilogue: Epilogue | str = param(default=Epilogue.NONE)
    # B's packed block count on AIE2P: blocks, not bytes, since B's
    # declaration counts bfp16ebs8 blocks and bfp.itemsize turns that back
    # into the byte count pack_b returns.
    packed_blocks: int = param(derive=lambda op: op.K * op.N // bfp.BLOCK, repr=False)
    # 64 halves the mmul's accumulator traffic per mac; 128 halves A fetches.
    tile_n: int = tunable()
    # k tile. K must be a multiple of it, and it of the compute tile's k slice.
    k_tile: int = tunable(
        domain=lambda op, dev, t: divisors(t, of=op.K, step=op.ct_k, cap=K_TILE),
    )
    # How much of the k tile a compute tile holds at a time, the kernel's
    # chunk_k. None resolves to the deepest that fits L1 (see l1_tiles); the
    # search tries the slice either side of it.
    ct_k: int = tunable(
        domain=lambda op, dev, t: divisors(t, of=op.k_tile, step=S, span=1)
    )
    # A-tile rows, decoupled from the accumulator's M_TILE (asymmetric tile
    # buffering). None resolves to whatever L1 affords.
    tile_ma: int = tunable(domain=lambda op, dev, t: divisors(t, of=M_TILE, step=2 * R))
    # Row-blocks a core folds into one B fetch, cutting B's DDR reads by
    # m_chunk at the cost of that many L1 accumulators. 1 by default: it must
    # divide m_row_blocks (M % 512 == 0), and a shape that cannot use it would
    # fork config_name. See README.md.
    m_chunk: int = tunable(
        default=1,
        domain=lambda op, dev, t: divisors(t, of=op.M // (M_TILE * op.rows)),
    )
    # The activations the epilogue can select between at run time. Each one
    # compiled in costs
    # program memory, so a deployment that dispatches two should compile two.
    epilogue_modes: tuple = param(default=tuple(Epilogue), array=True)
    rounding: Rounding | str = param(default=Rounding.CONV_EVEN, array=True)
    gelu: Gelu | str = param(default=Gelu.FP32, array=True)
    # B as stored (N, K), a checkpoint's layout, read as is: the memtile lays
    # out the k panels the kernel reads as B^T blocks, so no packed copy.
    b_col_maj: bool = param(default=False, array=True)
    # MEDIUM multiplies on AIE2P's bfp16 macs, A and B rounded to bfp16ebs8
    # (the port's arithmetic); above it, or on AIE2, on bf16 macs.
    precision: Precision = param(array=True)
    # B in DDR as pack_b's bfp16ebs8 blocks, which AIE2P's bfp16 macs
    # multiply unconverted: a packed B at precision='medium' there must say
    # so, since B's host shape depends on it and no device is known yet.
    bfp16_b: bool = param(default=False, repr=False, array=True)
    # B's element type, on the array and in DDR alike; the host holds a
    # block-float B as bytes (Operand.host_dtype).
    b_dtype: Any = param(
        derive=lambda op: v8bfp16ebs8 if op.bfp16_b else bfloat16,
        repr=False,
        init=False,
    )
    # Filled by resolve, from the device: the macs, the grid, B's storage,
    # the L2 tiles.
    emulate_bf16_mmul_with_bfp16: bool = tunable(repr=False, init=False)
    rows: int = tunable(repr=False, init=False)
    cols: int = tunable(repr=False, init=False)
    joins: int = tunable(repr=False, init=False)
    # B is packed to bfp16ebs8 where the macs are bfp16 and B is not read as
    # stored; B's host shape follows it, so a graph's step, which infers B's
    # shape from the weight it is given, passes it.
    bfp16_b: bool = param(
        derive=lambda op: (
            op.dev.arch == AIEArch.AIE2p
            and op.precision == Precision.MEDIUM
            and not op.b_col_maj
        ),
        array=True,
        repr=False,
    )
    # B's element type, on the array and in DDR alike; the host holds a
    # block-float B as bytes (Operand.host_dtype).
    b_dtype: Any = param(
        derive=lambda op: v8bfp16ebs8 if op.bfp16_b else bfloat16, repr=False
    )
    l1_b_depth: int = tunable(repr=False, init=False)
    a_l2: int = tunable(repr=False, init=False)
    b_l2: int = tunable(repr=False, init=False)
    c_l2: int = tunable(repr=False, init=False)

    # The sequence writes the cores' parameters itself, behind the first
    # block's fills and once per slab; see sequence().
    own_preamble: ClassVar[bool] = True
    # A split leg's pieces outnumber the shim's BD ids, so the compiler
    # recycles finished tasks' ids. Safe here: no task waits on a push
    # issued after it (see sequence()'s emit_slab).
    aiecc_flags: ClassVar[tuple[str, ...]] = ("--reclaim-runtime-bds",)

    A = In(M, K, obj_shape=(a_l2,), per=(rows,), depth=A_DEPTH)
    # For bfp16 macs B is counted in bfp16ebs8 blocks, the unit every
    # descriptor into it counts in: in bytes, a transfer would move a ninth
    # of what it named.
    B = In(
        Select(
            bfp16_b,
            (packed_blocks,),
            (Select(b_col_maj, (N, K), (K, N)),),
        ),
        dtype=b_dtype,
        obj_shape=(b_l2,),
        per=(cols,),
    )
    C = Out(M, N, obj_shape=(c_l2,), per=(cols, joins), depth=C_DEPTH)
    # M, or fewer rows per call (``A[:n]`` in a graph). A and C move, and the
    # cores compute, only the units (rows * M_TILE rows each) the bound
    # reaches; past them the cores drain each column-block's B replay
    # uncomputed, since its count is in the memtile's lock values, which no
    # per-call word reaches. B moves as it does unbounded.
    valid = per_call(bounds=M)
    # The parameter words every core reads once a call. The unit counts are
    # read only at m_chunk > 1: each word costs every dispatch (README.md, "A
    # word is not free"). The clamp bounds are read
    # always, the identity: the kernel's clamp is not compiled out.
    n_val = per_call(derive=lambda op: op.N)
    m_row_blocks = per_call(derive=lambda op: op._m_row_blocks)
    k_iters = per_call(derive=lambda op: op._k_iters)
    mode = per_call(derive=lambda op: op.epilogue.mode)
    clamp_min = per_call(derive=lambda op: CLAMP_BITS[0])
    clamp_max = per_call(derive=lambda op: CLAMP_BITS[1])
    n_units = per_call(derive=lambda op: op._n_units)
    # Under a bound, the units it reaches: the cores' trip count and C's
    # length, in row blocks.
    units_valid = per_call(derive=_units_valid)
    # A's repeat count on a full ELF: the units less one.
    units_repeat = per_call(derive=lambda op: _units_valid(op) - 1)
    # Under a bound, the passes B's memtile ring takes on a column-block, less
    # one: a streamed ring's per call, as DDR reads B once per unit reached.
    b_passes_repeat = per_call(
        derive=lambda op: _units_valid(op) * op._k_iters // op._b_ring - 1
    )
    # Whether the memtile replays B to every unit, as it does where B is
    # resident, so that the cores drain the replays past a bound.
    b_resident = per_call(derive=lambda op: int(op._b_resident))
    # Under a bound, where the second half of the core rows starts in A and in
    # C: past the first half's share of the units it reaches.
    a_half = per_call(
        derive=lambda op: _units_valid(op) * M_TILE * op.rows // op.joins * op.K
    )
    c_half = per_call(
        derive=lambda op: _units_valid(op) * M_TILE * op.rows // op.joins * op.N
    )

    def extent_unit(self, buffer: str) -> int:
        return 0  # nothing is shortened

    def validate(self) -> None:
        if self.precision == Precision.HIGHEST:
            raise ValueError(
                "flm.ProjectionGEMM: rounds per K tile at best (precision='high'); "
                "iron.operators.GEMM rounds once"
            )
        if self.bfp16_b and (self.b_col_maj or self.precision != Precision.MEDIUM):
            raise ValueError(
                "flm.ProjectionGEMM: bfp16_b (True) is a packed B (b_col_maj=False) "
                "at precision='medium'"
            )
        if self.tile_n is not None and self.tile_n not in TILE_NS:
            raise ValueError(
                f"flm.ProjectionGEMM: tile_n ({self.tile_n}) must be one of "
                f"{TILE_NS}"
            )
        if self.ct_k is not None and self.ct_k % S:
            raise ValueError(
                f"flm.ProjectionGEMM: ct_k ({self.ct_k}) must be a multiple of {S}"
            )
        if self.tile_ma is not None and (
            M_TILE % self.tile_ma or self.tile_ma % (2 * R)
        ):
            raise ValueError(
                f"flm.ProjectionGEMM: tile_ma ({self.tile_ma}) must divide {M_TILE} and be a multiple "
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
        if self.k_tile is not None and self.K % self.k_tile:
            raise ValueError(
                f"flm.ProjectionGEMM: K ({self.K}) must be a multiple of k_tile ({self.k_tile})"
            )
        # A mode the mask leaves out reaches the kernel's default arm, which
        # is NONE: an unactivated result rather than an error. Refuse.
        if (
            self.epilogue is not Epilogue.NONE
            and self.epilogue not in self.epilogue_modes
        ):
            raise ValueError(
                f"flm.ProjectionGEMM: epilogue ({self.epilogue}) is not in epilogue_modes "
                f"{tuple(str(m) for m in self.epilogue_modes)}, so it would "
                "not be compiled in and the kernel would silently apply none"
            )

    def resolve(self, dev):
        if dev is None:
            raise Unresolvable(
                "flm.ProjectionGEMM is sized from the device's L1 and grid"
            )
        rows, cols = compute_rows(dev), dev.cols
        # AIE2 has no BFP types, so its mmul lowers onto four native bf16 macs.
        emulate = dev.arch == AIEArch.AIE2p and self.precision == Precision.MEDIUM
        bfp16_b = self.bfp16_b
        b_elem_bytes = bfp.BLOCK_BYTES / bfp.BLOCK if bfp16_b else 2
        b_group = bfp.BLOCK if bfp16_b else 1
        tile_n = self.tile_n or next(
            (n for n in (N_TILE_DEFAULT, 32, 16) if self.N % n == 0),
            N_TILE_DEFAULT,
        )
        m_chunk = self.m_chunk
        k_tile = self.k_tile
        if k_tile is None:
            k_tile = K_TILE
            while self.K % k_tile and (k_tile // 2) % S == 0:
                k_tile //= 2
        ct_k, tile_ma, l1_b_depth = l1_tiles(
            tile_n,
            b_elem_bytes,
            dev.core_memory_bytes,
            lambda height, ct_k: self.frame(
                dev, tile_n, k_tile, ct_k, height, bfp16_b, emulate
            ),
            m_chunk,
            k_tile,
            self.tile_ma,
            self.ct_k,
        )
        return self.replace(
            tile_n=tile_n,
            k_tile=k_tile,
            ct_k=ct_k,
            tile_ma=tile_ma,
            rows=rows,
            cols=cols,
            joins=C_JOINS,
            emulate_bf16_mmul_with_bfp16=emulate,
            l1_b_depth=l1_b_depth,
            a_l2=m_chunk * M_TILE * k_tile,
            b_l2=k_tile * tile_n // b_group,
            c_l2=M_TILE * tile_n * rows // C_JOINS,
        )

    def compatible(self) -> None:
        # B_ITERS = k_tile // ct_k counts the B chunks one k step consumes,
        # so a k tile the compute tile's slice does not divide is
        # inexpressible.
        if self.k_tile % self.ct_k:
            raise ValueError(
                f"flm.ProjectionGEMM: k_tile ({self.k_tile}) must be a multiple of ct_k "
                f"({self.ct_k})"
            )
        # N only needs to tile to tile_n: a trailing group of fewer than
        # cols column-blocks is handled by per-column trip counts.
        for name, value, unit in (
            ("M", self.M, M_TILE * self.rows),
            ("K", self.K, self.k_tile),
            ("N", self.N, self.tile_n),
        ):
            if value % unit != 0:
                raise ValueError(
                    f"flm.ProjectionGEMM: {name} ({value}) must be a multiple of {unit}"
                )
        m_row_blocks = self._m_row_blocks
        if m_row_blocks % self.m_chunk:
            # A partial group is inexpressible: the object is m_chunk tiles
            # wide and the forward always drains that much.
            raise ValueError(
                f"flm.ProjectionGEMM: m_row_blocks ({m_row_blocks}) must be a multiple of m_chunk "
                f"({self.m_chunk}); pass m_chunk=1 for this shape"
            )
        # A bound's A transfer is one unit's row block a descriptor
        # dimension long; a unit of m_chunk blocks has no dimension left.
        if "valid" in self.bound_extents and self.m_chunk != 1:
            raise ValueError(
                f"flm.ProjectionGEMM: m_chunk ({self.m_chunk}) must be 1 under a per-call "
                f"row bound"
            )

    @property
    def compiled_modes(self) -> tuple[Epilogue, ...]:
        """Return the activations compiled into the epilogue.

        None and ``epilogue_modes``.
        """
        return _compiled_modes(self.epilogue_modes)

    @property
    def epilogue_mask(self) -> int:
        """Return the bitmask of the modes compiled into the epilogue.

        Mode 0 is always present; the kernel falls back to it.
        """
        mask = 1
        for m in self.compiled_modes:
            mask |= 1 << m.mode
        return mask

    @property
    def config_name(self) -> str:
        """Stem of the artifacts that do not depend on the shape: the xclbin's."""
        t = self.resolved()
        dev = self.dev
        if dev is None:
            raise Unresolvable(
                "flm.ProjectionGEMM: the xclbin is named for a device; none is bound"
            )
        return (
            f"FLM_GEMM_tn{t.tile_n}_kt{t.k_tile}_ck{t.ct_k}"
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
        """Return the configuration's stem, then every runtime parameter.

        Two instruction streams never share a name.
        """
        base = f"{self.config_name}_M{self.M}_K{self.K}_N{self.N}"
        if self.epilogue is not Epilogue.NONE:
            base = f"{base}_epi{self.epilogue}"
        return base

    def frame(self, dev, tile_n, k_tile, ct_k, band_m, bfp16_b, emulate) -> int:
        """Return what a core of ``dev`` holds beside its buffers at these tiles.

        Its kernel's data and deepest call's stack, over the default stack.
        Kept per kernel, as every resolve asks it of up to six.
        """
        tiles = (tile_n, k_tile, ct_k, band_m, bfp16_b, emulate)
        key = (
            dev,
            tiles,
            self.b_col_maj,
            self.epilogue_modes,
            self.rounding,
            self.gelu,
        )
        if key in _FRAMES:
            return _FRAMES[key]
        arch = resolve_target_arch(dev)
        # Measured, never built: kept out of the build's registry.
        with set_current_device(dev), compile_context(_iron_kernel_registry=set()):
            k = self.kernel(*tiles)
            calls = (k.mm_fused_acc_init, k.mm_fused_k_step, k.mm_fused_epilogue_chunk)
            deepest = max(k.frame_bytes(arch, entry=c.name) for c in calls)
        _FRAMES[key] = dev.default_core_stack_bytes + deepest
        return _FRAMES[key]

    def kernel(self, tile_n, k_tile, ct_k, band_m, bfp16_b, emulate):
        """Return the fused tile kernel each core runs at these tiles."""
        modes = _compiled_modes(self.epilogue_modes)
        return fused_mm(
            dim_m=M_TILE,
            dim_k=k_tile,
            dim_n=tile_n,
            band_m=band_m,
            chunk_k=ct_k,
            out_chunk=CT_OUT_LEN,
            c_depth=C_DEPTH,
            # 8x8x8 on both architectures: AIE2P lowers it onto one bfp16 mac
            # or two bf16 ones, AIE2 onto four native bf16 macs.
            mmul_shape=(R, S, T),
            bfp16_b=bfp16_b,
            b_col_maj=self.b_col_maj,
            emulate_bf16_mmul_with_bfp16=emulate,
            epilogue_modes=tuple(str(m) for m in modes),
            rounding=str(self.rounding),
            gelu=str(self.gelu),
        )

    def build(self) -> Built:
        dev = self.dev
        if dev is None:
            raise Unresolvable(
                "flm.ProjectionGEMM: build() runs on a bound device; none is bound"
            )
        COLS, ROWS, JOINS = self.cols, self.rows, self.joins
        N_TILE, CT_K, M_CHUNK, T_MA = (
            self.tile_n,
            self.ct_k,
            self.m_chunk,
            self.tile_ma,
        )
        B_GROUP = bfp.BLOCK if self.bfp16_b else 1  # B values per element
        L1_B_DEPTH, K_TILE = self.l1_b_depth, self.k_tile
        RHO = M_TILE // T_MA
        CT_A_LEN = 2 * R * CT_K  # one z slice
        CT_A_OBJ = CT_A_LEN * (T_MA // R // 2)  # every z slice of one mmul
        C_SLICE_LEN = M_TILE * N_TILE  # one compute tile's C contribution
        O_CHUNKS = C_SLICE_LEN // CT_OUT_LEN  # C objects an accumulator drains as
        B_ITERS = K_TILE // CT_K  # B chunks consumed per k step
        # Where the cores read a row bound: the scratchpad on a full ELF, else
        # their parameter buffer.
        bounded = self.value("valid").per_call
        tm = get_target_model(dev.resolve())

        bf16_ty = np.dtype[bfloat16]
        f32 = np.dtype[np.float32]
        b_elem_ty = np.dtype[self.b_dtype]
        # L1 (per compute tile)
        ct_a_obj_ty = np.ndarray[(CT_A_OBJ,), bf16_ty]
        ct_b_ty = np.ndarray[(CT_K * N_TILE // B_GROUP,), b_elem_ty]
        ct_out_ty = np.ndarray[(CT_OUT_LEN,), bf16_ty]
        ct_acc_ty = np.ndarray[(M_TILE * N_TILE,), f32]
        # L2 (per memtile): the declared stream tile.
        mt_a_ty = self.A.obj_type

        # Every field that changes the object reaches the factory, so its
        # object name keys the build. The activation is absent: the cores
        # select it at run time from the compiled-in modes, and mode 0 is
        # always compiled in, since the kernel falls back to it. Under
        # asymmetric tile buffering the k step takes the A band index, as the
        # core folds RHO A bands into one accumulator.
        kernel = self.kernel(
            N_TILE,
            K_TILE,
            CT_K,
            T_MA,
            self.bfp16_b,
            self.emulate_bf16_mmul_with_bfp16,
        )
        acc_init = kernel.mm_fused_acc_init
        k_step = kernel.mm_fused_k_step
        epilogue_chunk = kernel.mm_fused_epilogue_chunk

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
        run, wrap = R * CT_K, (1 << dev.get_dma_bd_wrap_bits(0, 1)) - 1
        a_lo = max(d for d in range(1, min(run, wrap) + 1) if run % d == 0)
        a_hi = run // a_lo
        a_send_dims = TensorAccessPattern.full((a_bands, B_ITERS, R * CT_K)).permute(
            (1, 0, 2)
        )
        if a_hi > 1:
            a_send_dims = a_send_dims.split(2, a_lo)

        # Column c and row r name logical tiles, and the placer decides
        # where each lands; only C's shim ends are pinned (below). One object
        # per logical tile, since tiles are told apart by identity. Typed up
        # front: Flow reads tile_type to find its shim end, and nothing else
        # stamps these.
        shim_tiles = [Tile(tile_type=AIETileType.ShimNOCTile) for _ in range(COLS)]
        mt_tiles = [Tile(tile_type=AIETileType.MemTile) for _ in range(COLS)]
        ct_tiles = [
            [Tile(tile_type=AIETileType.CoreTile) for _ in range(COLS)]
            for _ in range(ROWS)
        ]

        # C: a join per column and half of the core rows; each core drops its
        # slice at its own offset in its half's memtile buffer. Placed at
        # column c's shim, as the shared image has them: where the placer
        # chose, a shape whose transfers differ would move them.
        HALF = ROWS // JOINS
        c_fifos = self.C.fifos(
            C_DEPTH, tiles=[Tile(c, 0) for c in range(COLS) for _ in range(JOINS)]
        )
        c_prod = {}
        for c in range(COLS):
            for h in range(JOINS):
                sub = (
                    c_fifos[c * JOINS + h]
                    .prod()
                    .join(
                        [C_SLICE_LEN * p for p in range(HALF)],
                        tile=mt_tiles[c],
                        obj_types=[ct_out_ty] * HALF,
                        from_stream=[gather_dims] * HALF,
                    )
                )
                for p in range(HALF):
                    c_prod[(h * HALF + p, c)] = sub[p]

        # A: shim -> memtile -> broadcast along the compute row, reblocking on
        # the forward(). One fifo per row even at M_CHUNK > 1: a second would
        # want a third core input DMA channel, and a tile has two.
        a_l3l2_fifos, a_cons = [], {}
        for r in range(ROWS):
            of_a_in = ObjectFifo(mt_a_ty, depth=A_DEPTH)
            a_l3l2_fifos.append(of_a_in)
            of_a = of_a_in.cons(from_stream=a_recv_dims).forward(
                tile=mt_tiles[r * COLS // ROWS],
                obj_type=ct_a_obj_ty,
                depth=A_DEPTH,
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
        # The pool takes what the memtile has left once A and C are placed
        # (_b_slots).
        b_slot_elems = K_TILE * N_TILE // B_GROUP
        B_SLOTS = self._b_slots
        if B_SLOTS < 1:
            raise ValueError(
                f"flm.ProjectionGEMM: tile_n ({N_TILE}) leaves no room for a "
                f"{_b_bytes(K_TILE * N_TILE, self.bfp16_b)}-byte B slot in the "
                f"memtile after A and C"
            )
        b_mt_ty = np.ndarray[(B_SLOTS * b_slot_elems,), b_elem_ty]
        b_mt_bufs = [Buffer(b_mt_ty, tile=mt_tiles[c]) for c in range(COLS)]
        # One lock pair per slot, not per pool: a resident slot is consumed
        # once per unit and refilled only when all of them have, independently
        # of the other slots, so the next column-block's refill trails the
        # replay by one slot instead of waiting for the whole block.
        # Buffers, flows, locks and DMAs only the sequence and descriptors
        # reach, declared whichever columns a shape's sequence uses.
        unrouted: list = [*b_mt_bufs]
        b_mt_prod, b_mt_cons = [], []
        for c in range(COLS):
            for locks in (b_mt_prod, b_mt_cons):
                slots = [Lock(mt_tiles[c], init=0) for _ in range(B_SLOTS)]
                locks.append(slots)
                unrouted += slots
        b_shim_flows = [Flow(shim_tiles[c], mt_tiles[c]) for c in range(COLS)]
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
                bufs = [Buffer(ct_b_ty, tile=tile) for _ in range(L1_B_DEPTH)]
                prod = Lock(tile, init=L1_B_DEPTH)
                cons = Lock(tile, init=0)
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
        b_pool = _BPool(
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
                    initial_value=np.array([c], dtype=np.int32),
                )
                for c in range(COLS)
            ]
            for r in range(ROWS)
        ]
        read = [
            self.n_val,
            self.m_row_blocks,
            self.k_iters,
            self.mode,
            self.clamp_min,
            self.clamp_max,
        ]
        if M_CHUNK > 1:
            read.append(self.n_units)
        if bounded:
            read += [self.units_valid, self.b_resident]
        rtps = [Rtp(read) for _ in range(ROWS * COLS)]

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
            rtp,
            my_col,
        ):
            """Core body.

            Every trip count and the activation come from the runtime
            parameters, so one core program serves every shape.
            """
            # Safe to re-arm before the work: the sequence cannot open the
            # barrier again until this dispatch's C drains.
            words = rtp.read()
            # Derived rather than sent, saving an RTP word: column c has work
            # in block j iff (j*COLS + c)*N_TILE < N. Both divisors are powers
            # of two, so this must leave no __divsi3; check the .o.
            n_tiles = words[self.n_val] // N_TILE
            n_work = (n_tiles - my_col[0] + COLS - 1) // COLS
            n_drain = ((n_tiles + COLS - 1) // COLS) - n_work
            n_row_blocks = words[self.m_row_blocks]
            n_k_iters = words[self.k_iters]
            epi_mode = words[self.mode]
            clamp_min_bits = words[self.clamp_min]
            clamp_max_bits = words[self.clamp_max]
            n_units_rt = words[self.n_units] if M_CHUNK > 1 else n_row_blocks
            # Bounded, m_chunk is 1: a unit is a chunk.
            n_live = words[self.units_valid] if bounded else n_units_rt

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
                # A unit past the bound has its B replay all the same where B
                # is resident, its count in the memtile's locks; every replay
                # is the same B, so those go first and the call's last C still
                # comes after the cores' last acquire. A streamed ring stops at
                # the bound.
                if bounded:
                    for _ in range_((n_units_rt - n_live) * words[self.b_resident]):
                        for _ in range_(n_k_iters):
                            for _ in range_(B_ITERS // L1_B_DEPTH):
                                for _ in b_bufs:
                                    b_cons.acquire(1)
                                    b_prod.release(1)
                for _ in range_(n_live):
                    sweep(accs)

            # Column-blocks this column sits out. A is broadcast along the
            # row, so it must still consume its share or the columns that do
            # have work stall on the fifo. No B and no C; the sequence issues
            # neither.
            for _ in range_(n_drain):
                for _ in range_(n_live):
                    for _ in range_(n_k_iters):
                        for _ in range_(B_ITERS // L1_B_DEPTH):
                            for _ in range(L1_B_DEPTH):
                                for _ in range(M_CHUNK * RHO):
                                    a_h.acquire(1)
                                    a_h.release(1)

        workers = []
        for r in range(ROWS):
            for c in range(COLS):
                accs = [Buffer(type=ct_acc_ty) for _ in range(M_CHUNK)]
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
                            rtps[r * COLS + c],
                            my_cols[r][c],
                        ],
                        tile=ct_tiles[r][c],
                    )
                )

        self.A.bind([f.prod() for f in a_l3l2_fifos])
        self.B.bind(b_shim_flows)
        return _Built(workers + unrouted, rtps, b_pool=b_pool)

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

    @property
    def _b_slots(self) -> int:
        """Return B's memtile pool in k-tile slots: what A and C leave.

        At most ``B_MAX_SLOTS``, budgeted as if every memtile held an A
        forward (uniform across columns, though only every (cols //
        rows)-th does).
        """
        dev = self.dev
        if dev is None:
            raise Unresolvable(
                "flm.ProjectionGEMM: B's memtile budget is per device; none is bound"
            )
        free = (
            get_target_model(dev.resolve()).get_mem_tile_size()
            - A_DEPTH * self.m_chunk * M_TILE * self.k_tile * 2
            - C_DEPTH * M_TILE * self.tile_n * self.rows * 2
        )
        return min(
            B_MAX_SLOTS, free // _b_bytes(self.k_tile * self.tile_n, self.bfp16_b)
        )

    @property
    def _b_resident(self) -> bool:
        """Whether a column-block of B stays in the memtile for all of M's units."""
        dev = self.dev
        if dev is None:
            raise Unresolvable(
                "flm.ProjectionGEMM: B's residency depends on the device; none is bound"
            )
        lock_max = get_target_model(dev.resolve()).get_max_lock_value()
        return self._k_iters <= self._b_slots and self._n_units <= lock_max

    @property
    def _b_ring(self) -> int:
        """Return the slots B's memtile ring uses under a bound.

        Every k tile where B is resident, else the most that one unit's k
        tiles fill whole, so that a call's ring passes follow the units it
        reaches.
        """
        if self._b_resident:
            return self._k_iters
        return max(s for s in range(1, self._b_slots + 1) if self._k_iters % s == 0)

    def sequence(self, rt):
        M, K, N = self.M, self.K, self.N
        COLS, ROWS, JOINS = self.cols, self.rows, self.joins
        N_TILE, M_CHUNK, K_TILE = self.tile_n, self.m_chunk, self.k_tile
        k_iters, n_units = self._k_iters, self._n_units
        pool = rt.built.b_pool
        B_SLOTS, b_slot_elems = pool.slots, pool.slot_elems
        bounded = "valid" in self.bound_extents
        # Sweeps where all COLS columns have work, plus a trailing group of
        # rem_blocks columns (0 <= rem_blocks < COLS) that do one block more.
        n_full = N // (N_TILE * COLS)
        rem_blocks = (N % (N_TILE * COLS)) // N_TILE

        # One transfer per (column-block, leg), not one per object: a
        # descriptor walks many fifo objects in consume order. Dimension
        # order must match the core's nest.
        #
        # Each half of the core rows takes its own range of M, its rows'
        # row-blocks interleaved in it, so a leg steps HALF row-blocks a unit
        # rather than ROWS: K and N up to twice as wide fit a descriptor.
        HALF = ROWS // JOINS
        A = TensorAccessPattern.full(
            (JOINS, n_units, M_CHUNK, HALF, M_TILE, k_iters, K_TILE)
        )

        def a_tap(r, slab):
            # Every (row-block, k) block this row consumes for one
            # column-block: per unit, k outermost, then the unit's
            # row-blocks. A does not depend on the column-block; it is
            # re-fetched because the cores re-consume it.
            half, p = divmod(r, HALF)
            rows = A[half, slab.first : slab.first + slab.units, :, p]
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
            """Return the plan for ``units`` units from unit ``first``.

            Armed at once.
            """
            if k_iters <= B_SLOTS and units <= pool.lock_max:
                resident, b_slots, b_uses = True, k_iters, units
            elif bounded:
                # Streamed under a bound, the ring passes follow the units
                # reached, so a pass covers part of one unit (_b_ring).
                resident, b_slots, b_uses = False, self._b_ring, 1
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
                f"flm.ProjectionGEMM: M, K, N ({M}, {K}, {N}): even one unit per slab needs more passes "
                f"over a B pool per column-block than the {pool.queue} x "
                f"{pool.passes} one memtile channel can queue"
            )
        # A bound reaches units from the first, and a slab past it would arm
        # B and the cores for nothing.
        if bounded and len(slabs) > 1:
            raise ValueError(
                f"flm.ProjectionGEMM: M, K, N ({M}, {K}, {N}): a per-call row bound needs M in one slab, "
                f"and this shape takes {len(slabs)}"
            )
        if (
            bounded
            and not slabs[0].b_resident
            and n_units * k_iters // self._b_ring > pool.passes
        ):
            raise ValueError(
                f"flm.ProjectionGEMM: M, K, N ({M}, {K}, {N}): a per-call row bound needs a "
                f"column-block's B ring passes in one queue push of {pool.passes}"
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
            # here instead gives an innermost run of T=8 bf16, several times
            # slower (README.md), so b_col_maj's reorder is the memtile's.
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

        def b_mt_task(c, direction, passes, slab):
            """Program one of column ``c``'s memtile B channels.

            One BD per used slot, walked ``passes`` times (re-pushed past
            one queue's carry); returned for starting but never awaited --
            C completing implies it.
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
            return flow.endpoint(pool.mt_tiles[c]).task(*chain, runs=passes)

        C = TensorAccessPattern.full(
            (JOINS, n_units * M_CHUNK, HALF * M_TILE, N // N_TILE, N_TILE)
        )

        def c_tap(mega_col, c, half, slab):
            # Every joined block this column's half produces: one HALF*M_TILE
            # x N_TILE per row-block, in plain row-block order even under
            # M_CHUNK.
            row_blocks = slice(
                slab.first * M_CHUNK, (slab.first + slab.units) * M_CHUNK
            )
            return C[half, row_blocks, :, mega_col * COLS + c]

        # A trailing block uses only the first rem_blocks columns. A is still
        # issued for every row, since the sitting-out columns drain it.
        blocks = [(mc, COLS) for mc in range(n_full)]
        if rem_blocks:
            blocks.append((n_full, rem_blocks))

        def emit_slab(slab):
            # Arming B's memtile channels and the cores' parameters costs tens
            # of microseconds, so it goes out behind the first block's A and B
            # fills, overlapping their DDR latency: A only lands in fifo
            # buffers, and B backs up until its memtile channel has a task.
            # Nothing ahead of it may wait on the cores, which are not released
            # yet; the compiler's waits ahead of it are all an earlier slab's.
            b_mt_tasks = {}

            def push_b_mt(bi):
                """Push B's memtile chains for the chunks starting at block ``bi``.

                A push covers as many whole blocks as its passes carry,
                issued at the first of them, so the compiler only waits on
                an earlier, already-issued block's queue slot. Under a bound
                a streamed ring pushes one block a call.
                """
                per_call = bounded and not slab.b_resident
                for c in range(COLS):
                    if bi >= n_work(c):
                        continue
                    for direction, passes in zip(
                        (DMAChannelDir.S2MM, DMAChannelDir.MM2S),
                        b_mt_block_passes(slab),
                    ):
                        per_push = 1 if per_call else max(1, pool.passes // passes)
                        if bi % per_push:
                            continue
                        count = min(per_push, n_work(c) - bi) * passes
                        task = b_mt_tasks.get((c, direction))
                        if per_call:
                            if task is None:
                                task = b_mt_tasks[c, direction] = b_mt_task(
                                    c, direction, count, slab
                                )
                            word = self.b_passes_repeat
                            if word.ssa is None:
                                task.start(repeat_parameter=word.param)
                            else:
                                task.start(repeat_count=word.ssa)
                        elif task is None:
                            b_mt_tasks[c, direction] = b_mt_task(
                                c, direction, count, slab
                            ).start()
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
                    n_units=slab.units,
                )

            # Every transfer is unmanaged: the compiler meters each channel's
            # queue and takes a descriptor back once a poll proves its
            # transfer done. A column half's C drains in order on one channel,
            # and its last one finishing means its cores' slab is done -- fills,
            # memtile chains and cores -- so only that one carries a token.
            last_c = []

            # A's transfers, one per lane. Bounded, each repeats over the
            # units the bound reaches, a per-call repeat count, and the second
            # half's start past them is a per-call offset.
            if bounded:
                a_legs = [
                    (
                        A[0, :, 0, r % HALF].permute((0, 2, 1, 3)),
                        self.a_half if r >= HALF else None,
                    )
                    for r in range(ROWS)
                ]
            else:
                a_legs = [(a_tap(r, slab), None) for r in range(ROWS)]

            # C goes out after its block's fills, since the first C only
            # arrives after a whole k sweep. A leg whose pattern the shim
            # cannot take in one descriptor, or that needs more of them than a
            # task queue holds, the compiler cuts into pieces and interleaves
            # with the other legs'.
            for bi, (mega_col, active_cols) in enumerate(blocks):
                for r, (tap, offset) in enumerate(a_legs):
                    self.A.fill(
                        tap,
                        lane=r,
                        offset_parameter=offset,
                        repeat_parameter=self.units_repeat if bounded else None,
                        managed=False,
                    )
                for c in range(active_cols):
                    self.B.fill(
                        b_tap(mega_col, c, slab),
                        lane=c,
                        repeat_parameter=(
                            self.units_repeat
                            if bounded and not slab.b_resident
                            else None
                        ),
                        managed=False,
                    )
                if bi == 0:
                    set_up()
                else:
                    push_b_mt(bi)
                for c in range(active_cols):
                    last = bi == n_work(c) - 1
                    for half in range(JOINS):
                        task = self.C.drain(
                            c_tap(mega_col, c, 0 if bounded else half, slab),
                            lane=c * JOINS + half,
                            wait=last,
                            offset_parameter=self.c_half if bounded and half else None,
                            length_parameter=self.units_valid if bounded else None,
                            length_unit=HALF * M_TILE * N_TILE,
                            managed=False,
                        )
                        if last:
                            last_c.append(task)
            for task in last_c:
                task.await_()

        # Back to back: a slab returns only once its C has all drained.
        for slab in slabs:
            emit_slab(slab)

    def _single_slab(self) -> bool:
        """Whether ``sequence`` arms M in one slab.

        The same accept test ``cut()`` runs for ``n_slabs=1``, without a build to read
        ``rt.built`` from (the hardware limits ``_BPool`` carries are the device's own).
        """
        tm = get_target_model(self.dev.resolve())
        queue, passes_cap = tm.get_dma_task_queue_depth(), tm.get_max_repeat_count() + 1
        k_iters, n_units, b_slots = self._k_iters, self._n_units, self._b_slots
        if self._b_resident:
            passes = (1, n_units)
        elif k_iters > b_slots:
            divisor = max(
                s for s in range(1, b_slots + 1) if (n_units * k_iters) % s == 0
            )
            passes = (n_units * k_iters // divisor,) * 2
        else:
            return False
        return all(p <= queue * passes_cap for p in passes)

    def lane_transfers(self, operand):
        """Return a and C's order, one slab, ``m_chunk=1`` and unbounded.

        Past that a second slab, or a row bound's dynamic start (the second half of the
        core rows, ``a_half``/``c_half``) and its ``n_units`` axis truncation, are not
        one of ``Operand.transfers()``'s tuples.
        """
        if operand is not self.A and operand is not self.C:
            return None
        if self.m_chunk > 1 or "valid" in self.bound_extents:
            return None
        COLS, ROWS, JOINS = self.cols, self.rows, self.joins
        N_TILE, K_TILE = self.tile_n, self.k_tile
        k_iters, n_units = self._k_iters, self._n_units
        HALF = ROWS // JOINS
        N = self.N
        if N // N_TILE < COLS or not self._single_slab():
            return None
        n_full = N // (N_TILE * COLS)
        rem_blocks = (N % (N_TILE * COLS)) // N_TILE
        n_blocks = n_full + (1 if rem_blocks else 0)
        if operand is self.A:
            A = TensorAccessPattern.full(
                (JOINS, n_units, 1, HALF, M_TILE, k_iters, K_TILE)
            )
            out = []
            for r in range(ROWS):
                half, p = divmod(r, HALF)
                # B's column-block sweep resends A's K-sweep, unchanged, once
                # a column-block (``n_blocks`` of them).
                rows = A[half, :, :, p].permute((0, 3, 1, 2, 4))
                out.append((r, rows.repeat(n_blocks), None, None))
            return out
        C = TensorAccessPattern.full(
            (JOINS, n_units, HALF * M_TILE, N // N_TILE, N_TILE)
        )
        # The N-tile axis is outermost: C is resent column-block by
        # column-block, each one's whole row range before the next.
        return [
            (c * JOINS + half, C[half, :, :, c::COLS].permute((2, 0, 1, 3)), None, None)
            for c in range(COLS)
            for half in range(JOINS)
        ]

    @property
    def _reference_shape(self) -> tuple[int, int, int]:
        """Return the shape the configuration-only module is emitted at.

        The smallest valid one, so the shape-independence is explicit.
        """
        return (M_TILE * self.rows * self.m_chunk, self.k_tile, self.tile_n * self.cols)

    def xclbin_operator(self):
        """Return this configuration at its reference shape and activation.

        The xclbin every shape sharing it runs, each with its own
        instruction stream.
        """
        M, K, N = self._reference_shape
        # The tiles are named: the copy resolves again, at the reference shape.
        return self.replace(
            M=M,
            K=K,
            N=N,
            tile_n=self.tile_n,
            k_tile=self.k_tile,
            ct_k=self.ct_k,
            tile_ma=self.tile_ma,
            m_chunk=self.m_chunk,
            epilogue=Epilogue.NONE,
            epilogue_modes=self.compiled_modes,
            packed_blocks=None,
        )

    def pack_b(self, B):
        """Reorder a row-major ``(K, N)`` weight matrix into consumption order.

        (``iron.operators.flm.packing``): flat uint8 bfp16ebs8 blocks on
        NPU2, flat bf16 on NPU1, making both B hops linear descriptors.

        Raises:
            ValueError: Under ``b_col_maj``, which reads B as stored.
        """
        t = self.resolved()
        if t.b_col_maj:
            raise ValueError(
                "flm.ProjectionGEMM: b_col_maj (True) reads B as stored (N, K)"
            )
        return pack_b(
            B,
            k_tile=t.k_tile,
            n_tile=t.tile_n,
            s=S,
            t=T,
            ct_k=t.ct_k,
            bfp16=bool(t.bfp16_b),
            round_conv_even=t.rounding is Rounding.CONV_EVEN,
        )

    def ops(self) -> int:
        return 2 * self.M * self.K * self.N

    def reference(self, A, B):
        """``C = epilogue(A @ B)``, in the kernel's order.

        The product accumulates in float32 and rounds to the output dtype
        before the epilogue, since ``mm_fused_epilogue_chunk`` converts the
        accumulator to bf16 first. Not bit-exact -- the activation is a LUT
        on aie2, native on aie2p, worth up to ~0.02 absolute, absorbed by
        the tolerance. ``B`` is ``(N, K)`` under ``b_col_maj``.
        """
        b = B.T if self.b_col_maj else B
        C = np.matmul(A.astype(np.float32), b.astype(np.float32)).astype(A.dtype)
        return Epilogue(self.epilogue).apply(C)

    def tolerance(self) -> Tolerance | None:
        """Return C's roundings, in units of 2^-8 of ``|A| @ |B|``.

        Under 2 for C's conversion to bf16, plus K * 2^-16 for the f32
        accumulator; bfp16 macs add 2 more units (nearest) or 8
        (truncating). An activated GEMM has no tolerance, since the
        approximation isn't bounded here.
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
