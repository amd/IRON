# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Co-residence: designs packed into one device configuration.

``y = silu(a + b)`` as a full-ELF sequence, each op on half the columns, so the
pair can share the array. Checked at the MLIR level -- one pack device, one
configure point for both steps, each step running its own named sequence --
and through aiecc to a full ELF. The placer-driven policy must find the
pack a caller would name by hand, and must decline a pair whose union needs
more shim channels than the array has, or two members pinning one shim DMA
channel. A recorded graph reaches the same packing through
``compile(coresident=)``.

The fit checks run mlir-aie's passes in process; only the ELF builds need
Peano and ``aiebu-asm``. Nothing dispatches: hardware checks the numbers
(``iron/tests/infrastructure/coresidence.py``).
"""

import json
import re

import numpy as np
import pytest
from aie import ir
from aie.dialects import aie as aie_dialect
from aie.dialects.aie import DMAChannelDir, shim_dma_allocation
from aie.iron import DeviceConfiguration, Flow, ObjectFifo, Program, Runtime, Worker
from aie.iron.device import NPU2, AnyShimTile, Tile
from aie.utils.compile.jit._hash import _python_identity

from iron.common.image import AdjacentPacking, compose, coresidence
from iron.common.image.coresidence import Packing
from iron.common.image.compose import Composition
from iron.common.image.link import FullELF
from iron.common.image.sequence import Image
from iron.common.graph.record import Recording
from iron.common.image.coresidence import CoResidenceError, conflicts, fits, places
from iron.common.design import OperatorDesign
from iron.operators import GEMM, GEMV, ElementwiseAdd, ElementwiseMul, SiLU
from iron.operators.gemm import GEMMPlacement
from iron.tests.common.graphs import Chain
from iron.tests.common import sequences
from iron.tests.toolchain.tools import requires

SIZE = 8192
TILE = 256

pytestmark = pytest.mark.usefixtures("npu2")


def _builds_elf(test):
    """Skip ``test`` without Peano and ``aiebu-asm``."""
    for mark in requires("aiebu", "peano"):
        test = mark(test)
    return test


def _shim_pinned(col: int, channel: int, name: str) -> Runtime:
    """A pass-through whose input enters on shim ``(col, 0)``, MM2S
    ``channel``, through a fifo named ``name``: its runtime sequence, which
    reaches the rest.
    """
    vec = np.ndarray[(1024,), np.dtype[np.int32]]
    line = np.ndarray[(256,), np.dtype[np.int32]]
    of_in = ObjectFifo(line, depth=2, name=name)
    of_out = of_in.cons().forward()

    def sequence(a, c, in_h, out_h):
        in_h.fill(a)
        out_h.drain(c, wait=True)

    return Runtime(
        sequence,
        [
            vec,
            vec,
            of_in.prod(tile=Tile(col, 0), channel=channel),
            of_out.cons(tile=AnyShimTile),
        ],
    )


class _Allocated(Runtime):
    """Rows routed by hand from shim (0, 0) MM2S 1 into shim (1, 0) S2MM 0,
    and (1, 0) MM2S 0 held for packets, each channel allocated as
    ``OperatorRuntime`` allocates a pinned lane (``Operand.pin``).
    """

    CHANNELS = (
        ("ctrl", 1, DMAChannelDir.MM2S, 0),
        ("rows_src", 0, DMAChannelDir.MM2S, 1),
        ("rows", 1, DMAChannelDir.S2MM, 0),
    )

    def __init__(self):
        self.tiles = (Tile(0, 0), Tile(1, 0))
        super().__init__(lambda: None, [])
        self.add_flow(Flow(*self.tiles, src_channel=1, dst_channel=0))

    def resolve(self, loc=None, ip=None, *, device=None, **options):
        for symbol, col, direction, channel in self.CHANNELS:
            device.resolve_tile(self.tiles[col])
            shim_dma_allocation(symbol, self.tiles[col].op, direction, channel)
        super().resolve(loc, ip, device=device, **options)


def _places(*members: Runtime | Worker) -> str | None:
    """``places``'s verdict on ``members`` composed into one device
    configuration, which must itself resolve.
    """
    runtimes = [m for m in members if isinstance(m, Runtime)]
    workers = [m for m in members if isinstance(m, Worker)]
    configured = DeviceConfiguration("pack", NPU2(), workers=workers, runtimes=runtimes)
    module = Program.compose([configured], entry=runtimes[0]).resolve_program()
    return places(module)


def _conflict(**texts: str) -> str | None:
    """The conflict ``conflicts`` finds among the devices ``texts``, by
    member, or None.
    """
    with ir.Context():
        modules = {member: ir.Module.parse(text) for member, text in texts.items()}
        devices = {
            member: next(
                op
                for op in module.body.operations
                if isinstance(op, aie_dialect.DeviceOp)
            )
            for member, module in modules.items()
        }
        try:
            conflicts(devices)
        except CoResidenceError as e:
            return str(e)
    return None


def _routed(allocated: bool, logical: bool = False) -> str:
    """Rows routed by hand from shim (0, 0) MM2S 1 into shim (1, 0) S2MM 0,
    (0, 0)'s BDs written through its TileControl by packets from (1, 0)
    MM2S 0: a per-call gather's routes, with or without the allocations
    that tell the fifo lowering its channels are taken, on physical tiles
    or on logical ones pinned to them (as a ``Gather`` builds them). The
    device text, for ``conflicts``.
    """
    allocations = (
        """
  aie.shim_dma_allocation @ctrl(%t1, MM2S, 0)
  aie.shim_dma_allocation @rows_src(%t0, MM2S, 1)
  aie.shim_dma_allocation @rows(%t1, S2MM, 0)"""
        if allocated
        else ""
    )
    t0, t1 = (
        ("aie.logical_tile<ShimNOCTile>(0, 0)", "aie.logical_tile<ShimNOCTile>(1, 0)")
        if logical
        else ("aie.tile(0, 0)", "aie.tile(1, 0)")
    )
    return f"""
aie.device(npu2) {{
  %t0 = {t0}
  %t1 = {t1}
  aie.packet_flow(29) {{
    aie.packet_source<%t1, DMA : 0>
    aie.packet_dest<%t0, TileControl : 0>
  }}
  aie.flow(%t0, DMA : 1, %t1, DMA : 0){allocations}
  aie.runtime_sequence @sequence() {{
  }}
}}
"""


def _sequence(cols: int, coresident) -> Image:
    add = ElementwiseAdd(size=SIZE, tile_size=TILE, num_aie_columns=cols)
    silu = SiLU(size=SIZE, tile_size=TILE, num_aie_columns=cols)
    recording = Recording.of_steps(
        "coresidence",
        sequences.steps((add, "a", "b", "t"), (silu, "t", "y")),
        ["a", "b"],
        ["y"],
    )
    seq = Image(recording, FullELF(coresident(add, silu)))
    seq.prepare()
    return seq


def _devices(text: str) -> list[str]:
    return re.findall(r"^  aie\.device\(\w+\) @(\w+) \{$", text, re.M)


def test_manual_pack_shares_one_configure():
    seq = _sequence(4, lambda add, silu: [[add, silu]])
    composed = Composition(seq)
    text = composed.text()

    pack = Packing.device_name(list(composed.designs))
    assert composed.packing == Packing((tuple(composed.designs),))
    # The pack (main is left unnamed).
    assert _devices(text) == [pack]
    assert re.findall(r"aiex\.configure @(\w+)", text) == [pack]
    assert re.findall(r"aiex\.run @(\w+)", text) == list(composed.designs)


def test_policy_finds_the_manual_pack():
    manual = Composition(_sequence(4, lambda add, silu: [[add, silu]])).text()
    auto = Composition(_sequence(4, lambda add, silu: AdjacentPacking())).text()
    assert auto == manual


def test_policy_declines_what_does_not_fit():
    composed = Composition(_sequence(8, lambda add, silu: []))
    for name, design in composed.designs.items():
        assert fits({name: design}) is None
    packing, stopped = AdjacentPacking().pack(
        [n for n, _ in composed.steps], composed.designs
    )
    assert packing == Packing()
    [reason] = stopped.values()
    assert "ShimNOCTile" in reason


def test_one_array_joins_two_packs_only_where_their_union_fits():
    # SiLU at two sizes is one array, packed with an add and with a mul:
    # each pack of two four-column arrays fits, the three together do not,
    # so the array is built in each pack rather than joining them.
    add = ElementwiseAdd(size=SIZE, tile_size=TILE, num_aie_columns=4)
    silu = SiLU(size=SIZE, tile_size=TILE, num_aie_columns=4)
    wider = SiLU(size=2 * SIZE, tile_size=TILE, num_aie_columns=4)
    mul = ElementwiseMul(size=2 * SIZE, tile_size=TILE, num_aie_columns=4)
    recording = Recording.of_steps(
        "joined_packs",
        sequences.steps(
            (add, "a", "b", "t"),
            (silu, "t", "y"),
            (wider, "c", "u"),
            (mul, "u", "d", "z"),
        ),
        ["a", "b", "c", "d"],
        ["y", "z"],
    )
    seq = Image(recording, FullELF([[add, silu], [wider, mul]]))
    seq.prepare()
    composed = Composition(seq)
    a, s, w, m = (name for name, _ in composed.steps)
    assert fits({n: composed.designs[n] for n in (a, s)}) is None
    assert fits({n: composed.designs[n] for n in (w, m)}) is None
    assert fits(composed.designs) is not None
    devices = _devices(composed.text())
    assert devices[:2] == [Packing.device_name([a, s]), Packing.device_name([w, m])]


def test_designs_of_one_array_share_its_device():
    # Two extents of one add are one array: the full width packs with
    # itself, and the steps run on one configure.
    small = ElementwiseAdd(size=SIZE, tile_size=TILE, num_aie_columns=8)
    large = ElementwiseAdd(size=2 * SIZE, tile_size=TILE, num_aie_columns=8)
    recording = Recording.of_steps(
        "shared_array",
        sequences.steps(
            (small, "a", "b", "t"),
            (large, "c", "d", "u"),
            (small, "t", "b", "y"),
        ),
        ["a", "b", "c", "d"],
        ["y", "u"],
    )
    seq = Image(recording, FullELF())
    seq.prepare()
    composed = Composition(seq)
    text = composed.text()
    pack = Packing.device_name(list(composed.designs))
    assert _devices(text) == [pack]
    assert re.findall(r"aiex\.configure @(\w+)", text) == [pack]
    assert re.findall(r"aiex\.run @(\w+)", text) == [n for n, _ in composed.steps]
    assert text.count("aie.core(") == 8
    assert fits(composed.designs) is None


def test_two_arrays_of_one_class_pack():
    # aie.iron names the two GEMV arrays' fifos in one symbol table.
    gemvs = [
        GEMV(M=512, K=512, num_aie_columns=2, tile_size_output=tile)
        for tile in (32, 16)
    ]
    assert gemvs[0].resolved().array_key() != gemvs[1].resolved().array_key()
    recording = Recording.of_steps(
        "gemv_pack",
        sequences.steps((gemvs[0], "wa", "x", "ya"), (gemvs[1], "wb", "x", "yb")),
        ["wa", "wb", "x"],
        ["ya", "yb"],
    )
    seq = Image(recording, FullELF([gemvs]))
    seq.prepare()
    composed = Composition(seq)
    assert fits(composed.designs) is None
    fifos = re.findall(r"aie\.objectfifo @(\w+)\(", composed.text())
    assert fifos and len(fifos) == len(set(fifos))


def test_packing_rejects_a_design_in_two_groups():
    with pytest.raises(ValueError, match="two groups"):
        Packing((("a", "b"), ("b", "c")))


def test_sequence_rejects_a_stray_operator():
    stray = SiLU(size=SIZE, tile_size=TILE, num_aie_columns=2)
    seq = _sequence(4, lambda add, silu: [[add, stray]])
    with pytest.raises(ValueError, match="no step runs"):
        Composition(seq)


def test_a_pack_refuses_two_cores_on_one_tile():
    # Two GEMM arrays, each with its cores pinned from tile (0, 2); they
    # differ in b_col_maj only so that they are two distinct designs.
    def gemm(b_col_maj):
        op = GEMM(
            M=256,
            K=256,
            N=256,
            num_aie_columns=1,
            b_col_maj=b_col_maj,
            placement=GEMMPlacement.TILES,
        )
        return OperatorDesign(op.resolved())

    assert fits({"a": gemm(False)}) is None
    reason = fits({"a": gemm(False), "b": gemm(True)})
    assert reason is not None and "already has a core" in reason


def test_two_pins_on_one_shim_channel_do_not_fit():
    # Both members' logical shim tiles pinned to (0, 0), MM2S channel 1: the
    # fifo lowering must refuse the second (neither pins a physical
    # aie.tile, so no claim is seen before placement).
    assert _places(_shim_pinned(0, 1, "x")) is None
    reason = _places(_shim_pinned(0, 1, "x"), _shim_pinned(0, 1, "y"))
    assert reason is not None and "already in use" in reason


@pytest.mark.parametrize("col, channel", [(0, 0), (1, 1)], ids=["channel", "column"])
def test_pins_on_distinct_shim_channels_fit(col, channel):
    assert _places(_shim_pinned(0, 1, "x"), _shim_pinned(col, channel, "y")) is None


@pytest.mark.parametrize("logical", [False, True], ids=["physical", "logical"])
def test_a_hand_routed_shim_channel_needs_its_allocation(logical):
    # Unallocated, (0, 0) MM2S 1 is free to the fifo lowering, which would
    # give it to another member's pinned fifo too: one port feeding both.
    reason = _conflict(x=_routed(allocated=False, logical=logical))
    assert reason is not None and "shim_dma_allocation" in reason
    assert "(0, 0) MM2S channel 1" in reason


@pytest.mark.parametrize(
    "col, channel, taken",
    [(0, 1, True), (1, 0, True), (0, 0, False), (2, 0, False)],
    ids=["routed", "packets", "same_tile", "elsewhere"],
)
def test_an_allocated_route_holds_its_channels(col, channel, taken):
    assert _places(_Allocated()) is None
    reason = _places(_Allocated(), _shim_pinned(col, channel, "y"))
    if taken:
        assert reason is not None and "already in use" in reason
    else:
        assert reason is None


def test_packing_is_in_the_composed_identity():
    # The composed generator closes over its Composition, so the key follows the
    # modules a pack is built and chosen in; and the packing itself is part
    # of the identity.
    temporal = Composition(_sequence(4, lambda add, silu: []))
    packed = Composition(_sequence(4, lambda add, silu: [[add, silu]]))
    reached = _python_identity([temporal])
    for module in (compose, coresidence):
        assert f"{module.__name__}@".encode() in reached
    assert temporal.identity != packed.identity


def test_recorded_graph_packs():
    # Three designs, add and silu recurring: the policy packs all three, so
    # the whole graph is one configure.
    recording = Chain(SIZE, TILE, columns=2).record(a=(SIZE,), b=(SIZE,))
    temporal = Image(recording, FullELF())
    packed = Image(recording, FullELF(AdjacentPacking()))
    temporal.prepare()
    packed.prepare()
    composed = Composition(packed)
    assert len(composed.designs) == 3 and len(composed.steps) == 5

    # Temporal: a configure per step that changes design.
    assert len(re.findall(r"aiex\.configure", Composition(temporal).text())) == 5
    # Packed: one pack named for all three designs, each step its own run.
    text = composed.text()
    assert re.findall(r"aiex\.configure @(\w+)", text) == [
        Packing.device_name(list(composed.designs))
    ]
    assert re.findall(r"aiex\.run @(\w+)", text) == [n for n, _ in composed.steps]


@_builds_elf
def test_pack_compiles_to_a_full_elf():
    seq = _sequence(4, lambda add, silu: [[add, silu]])
    seq.compile()
    designs = list(Composition(seq).designs)
    assert seq.elf_path is not None
    config = json.loads((seq.elf_path.parent / "full_elf_config.json").read_text())
    instances = [
        instance["id"]
        for kernel in config["xrt-kernels"]
        if kernel["name"] == Packing.device_name(designs)
        for instance in kernel["instance"]
    ]
    assert instances == designs


@_builds_elf
def test_graph_compile_forwards_the_packing():
    version = Chain(SIZE, TILE, columns=2).compile(
        full_elf=True, coresident=AdjacentPacking(), a=(SIZE,), b=(SIZE,)
    )
    assert version.sequence.coresident == AdjacentPacking()
    composed = Composition(version.sequence)
    assert re.findall(r"aiex\.configure @(\w+)", composed.text()) == [
        Packing.device_name(list(composed.designs))
    ]
