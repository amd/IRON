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
``compile(coresident=)``. On NPU1's xclbin, a pack's back-to-back steps
are one sequence over the pack's arrays.

The fit checks run mlir-aie's passes in process; only the ELF builds need
Peano and ``aiebu-asm``. Nothing dispatches.
"""

import json
import re
from types import SimpleNamespace

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
from iron.common.image.link import FullELF, PerStep, _run
from iron.common.image.sequence import Image
from iron.common.graph.record import Recording
from iron.common.image.coresidence import CoResidenceError, conflicts, fits, places
from iron.common.design import OperatorDesign
import iron
from iron import Scratchpad
from iron.operators import GEMM, GEMV, ElementwiseAdd, ElementwiseMul, SiLU
from iron.operators.copy import Gather
from iron.operators.gemm import GEMMPlacement
from iron.tests.support.graphs import Chain
from iron.tests.support import sequences
from iron.tests.support.tools import requires

SIZE = 8192
TILE = 256

pytestmark = pytest.mark.usefixtures("npu2")


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
    seq._prepare()
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
    seq._prepare()
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
    seq._prepare()
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
    seq._prepare()
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
    temporal._prepare()
    packed._prepare()
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


@requires("aiebu", "peano")
def test_pack_compiles_to_a_full_elf():
    seq = _sequence(4, lambda add, silu: [[add, silu]])
    seq.compile()
    designs = list(Composition(seq).designs)
    config = json.loads((seq.image.parent / "full_elf_config.json").read_text())
    instances = [
        instance["id"]
        for kernel in config["xrt-kernels"]
        if kernel["name"] == Packing.device_name(designs)
        for instance in kernel["instance"]
    ]
    assert instances == designs


@requires("aiebu", "peano")
def test_graph_compile_forwards_the_packing():
    version = Chain(SIZE, TILE, columns=2).compile(
        full_elf=True, coresident=AdjacentPacking(), a=(SIZE,), b=(SIZE,)
    )
    assert version.sequence.packaging.coresident == AdjacentPacking()
    composed = Composition(version.sequence)
    assert re.findall(r"aiex\.configure @(\w+)", composed.text()) == [
        Packing.device_name(list(composed.designs))
    ]


def _image(recording, coresident) -> Image:
    seq = Image(recording, PerStep(coresident=coresident))
    seq._prepare()
    return seq


def _runs(seq: Image) -> tuple[list[str], dict]:
    """``seq``'s designs by step, and its runs."""
    designs, design_of = seq.unique_designs()
    names = [OperatorDesign(op, full_elf=False).name for op in designs]
    order = [names[design_of[id(s.op)]] for s in seq.steps]
    assert isinstance(seq.packaging, PerStep)
    return order, seq.packaging._runs(order, dict(zip(names, designs)))


def _chain(coresident) -> tuple[list[str], dict]:
    """The NPU1 ``Chain``'s designs by step, and its runs on ``coresident``."""
    graph = Chain(SIZE, TILE, columns=1)
    packs = coresident(graph) if callable(coresident) else coresident
    return _runs(_image(graph.record(a=(SIZE,), b=(SIZE,)), packs))


def _steps(*kinds: str) -> Recording:
    """Adds and SiLUs on one column, in ``kinds`` order, each on the last's output."""
    add = ElementwiseAdd(size=SIZE, tile_size=TILE, num_aie_columns=1)
    silu = SiLU(size=SIZE, tile_size=TILE, num_aie_columns=1)
    steps, last = [], "a"
    for i, kind in enumerate(kinds):
        out = f"t{i}"
        steps.append((add, last, "b", out) if kind == "add" else (silu, last, out))
        last = out
    return Recording.of_steps("steps", sequences.steps(*steps), ["a", "b"], [last])


def test_an_npu1_pack_runs_its_steps_as_one_sequence(npu1):
    order, runs = _chain(AdjacentPacking())
    assert list(runs) == [(0, 5)]
    text = str(_run(runs[0, 5], tuple(order)).generate_mlir())
    assert len(re.findall(r"aie\.device\(npu1\)", text)) == 1
    (sequence,) = re.findall(r"aie\.runtime_sequence\((.*)\) \{", text)
    # add, silu, mul, add, silu: 3 + 2 + 3 + 3 + 2 buffers, in turn.
    assert sequence.count("memref<") == 13
    # Each step writes its core's parameter, then moves its own fifos.
    moves = re.findall(r"rtp_write\(@(rtp\d)|task_for @(of\d)", text)
    assert ["".join(m) for m in moves] == (
        "rtp0 of0 of1 of2 rtp1 of3 of4 rtp2 of5 of6 of7 "
        "rtp0 of0 of1 of2 rtp1 of3 of4"
    ).split()


def test_an_npu1_pack_member_between_others_runs_alone(npu1):
    order, runs = _chain(lambda graph: [[graph.add, graph.silu]])
    assert order[2].startswith("ElementwiseMul") and list(runs) == [(0, 2), (3, 5)]


def test_an_npu1_pack_runs_only_where_its_members_meet(npu1):
    _, runs = _chain(lambda graph: [[graph.add, graph.mul]])
    assert list(runs) == [(2, 4)]


def test_an_npu1_run_is_cut_at_the_kernel_s_buffers(npu1):
    # 3 + 2 + 3 + 2 + 3 + 2 = 15 buffers, then 3 more: the last add runs alone.
    seq = _image(_steps(*["add", "silu"] * 3, "add"), AdjacentPacking())
    assert list(_runs(seq)[1]) == [(0, 6)]


class _Bounded(iron.Graph):
    def body(self, a, b, *, n: Scratchpad[np.int32]):
        shape = dict(tile_size=TILE, num_aie_columns=1)
        return SiLU.step(ElementwiseAdd.step(a[:n], b[:n], **shape), **shape)


def test_an_npu1_design_with_per_call_values_packs_with_none(npu1, caplog):
    recording = _Bounded().record(a=(SIZE,), b=(SIZE,))
    members = [s.op for s in recording.steps]
    with caplog.at_level("INFO", logger=coresidence.__name__):
        assert _runs(_image(recording, AdjacentPacking()))[1] == {}
    assert "takes per-call value 'valid'" in caplog.text
    with pytest.raises(CoResidenceError, match="per-call value 'valid'"):
        _runs(_image(recording, [members]))


def test_an_npu1_run_declares_a_pinned_design_s_pins_once(npu1):
    gather = Gather(rows=16, table_rows=64, row=512, feeds=1)
    add = ElementwiseAdd(size=16 * 512, tile_size=512, num_aie_columns=1)
    recording = Recording.of_steps(
        "gathers",
        sequences.steps(
            (gather, "table", "control", "y"),
            (add, "y", "b", "z"),
            (gather, "table", "control", "w"),
        ),
        ["table", "control", "b"],
        ["z", "w"],
    )
    order, runs = _runs(_image(recording, [[gather, add]]))
    text = str(_run(runs[0, 3], tuple(order)).generate_mlir())
    assert len(re.findall(r"aie\.shim_dma_allocation @y_0\(", text)) == 1


class _Built:
    """A design ``CompilableDesign.chain`` compiled, without aiecc."""

    dispatch_params = ()

    def get_cache_entry(self):
        return SimpleNamespace(insts=None)

    def get_dispatch_lib_path(self):
        return None


class _Tensor:
    """An XRTTensor's shape alone, for a callable built without a runtime."""

    def __init__(self, shape, dtype=None):
        self.shape = shape

    def subview(self, start, shape, dtype):
        return _Tensor(shape)

    def to(self, device):
        pass


def test_an_npu1_pack_links_and_dispatches_each_run_once(npu1, monkeypatch):
    """Without aiecc: each run is one kernel over its steps' buffers, and a
    member that also runs alone still builds its own.
    """
    from iron.common.image import callable as image_callable
    from iron.common.image import link

    built = []

    def chain(designs, name):
        built.extend(designs)
        return [(_Built(), f"x{i}", f"k{i}") for i in range(len(designs))]

    calls = []

    class Kernel:
        dispatch_params = ()

        def __init__(self, xclbin, insts, kernel_name, **_):
            self.xclbin_path, self.name = xclbin, kernel_name

        def __call__(self, *args):
            calls.append((self.name, len(args)))

    monkeypatch.setattr(link.CompilableDesign, "chain", staticmethod(chain))
    monkeypatch.setattr(link, "NPUKernel", Kernel)
    monkeypatch.setattr(image_callable, "_require_xrt", lambda: None)
    monkeypatch.setattr(image_callable, "XRTTensor", _Tensor)
    graph = Chain(SIZE, TILE, columns=1)
    recording = graph.record(a=(SIZE,), b=(SIZE,))
    image = Image(recording, PerStep(coresident=[[graph.add, graph.mul]])).compile()
    # add, silu, then mul and add as one run, then silu: add also runs alone,
    # so it builds its own; mul runs only in the run.
    assert len(built) == 3 and list(image.packaging.runs) == [2]
    assert [s.design for s in image.artifacts.steps] == ["k0", "k1", "k2", "k2", "k1"]
    image.get_callable()()
    assert calls == [("k0", 3), ("k1", 2), ("k2", 3 + 3), ("k1", 2)]


def test_check_packs_nothing():
    with pytest.raises(ValueError, match="pass check=False or drop coresident"):
        PerStep(check=True, coresident=AdjacentPacking())
