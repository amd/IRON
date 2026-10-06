# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Co-residence: designs packed into one device configuration.

``y = silu(a + b)`` as a fused sequence, each op on half the columns, so the
pair can share the array. Checked at the MLIR level -- one pack device, one
configure point for both steps, each step running its own named sequence --
and through aiecc to a full ELF. The placer-driven policy must find the
pack a caller would name by hand, and must decline a pair whose union needs
more shim channels than the array has, or two members pinning one shim DMA
channel. A traced graph reaches the same packing through
``compile(coresident=)``.

The fit checks run mlir-aie's passes in process; only the ELF builds need
Peano and ``aiebu-asm``. Nothing dispatches: hardware checks the numbers
(``iron/tests/infrastructure/coresidence.py``).
"""

import json
import re

import numpy as np
import pytest
from aie.dialects import aie as aie_dialect
from aie.iron import ObjectFifo, Program, Runtime
from aie.iron.device import NPU2, AnyShimTile, Tile
from aie.utils.compile.jit._hash import _python_identity

import iron
from iron.common.image import (
    AdjacentPacking,
    Fusion,
    OperatorSequence,
    Packing,
    coresidence,
    fusion,
)
from iron.common.image.coresidence import fits
from iron.operators import ElementwiseAdd, ElementwiseMul, SiLU
from iron.tests.toolchain.tools import requires

SIZE = 8192
TILE = 256

pytestmark = pytest.mark.usefixtures("npu2")


def _builds_elf(test):
    """Skip ``test`` without Peano and ``aiebu-asm``."""
    for mark in requires("aiebu", "peano"):
        test = mark(test)
    return test


# Two cores pinned to one tile: a conflict no placer can resolve, which the
# merge itself must refuse before placement is asked.
_PINNED = """
aie.device(npu2) {
  %t = aie.tile(0, 2)
  %c = aie.core(%t) {
    aie.end
  }
  aie.runtime_sequence @sequence() {
  }
}
"""


def _shim_pinned(col: int, channel: int) -> str:
    """A pass-through design whose input enters on shim ``(col, 0)``, MM2S
    ``channel``: the device text, as a generator would hand it to the merge.
    """
    vec = np.ndarray[(1024,), np.dtype[np.int32]]
    line = np.ndarray[(256,), np.dtype[np.int32]]
    of_in = ObjectFifo(line, name="in")
    of_out = of_in.cons().forward()

    def sequence(a, c, in_h, out_h):
        in_h.fill(a)
        out_h.drain(c, wait=True)

    rt = Runtime(
        sequence,
        [
            vec,
            vec,
            of_in.prod(tile=Tile(col, 0), channel=channel),
            of_out.cons(tile=AnyShimTile),
        ],
    )
    module = Program(NPU2(), rt).resolve_program()
    [device] = [
        str(op) for op in module.body.operations if isinstance(op, aie_dialect.DeviceOp)
    ]
    return device


def _sequence(cols: int, coresident) -> OperatorSequence:
    add = ElementwiseAdd(size=SIZE, tile_size=TILE, num_aie_columns=cols)
    silu = SiLU(size=SIZE, tile_size=TILE, num_aie_columns=cols)
    seq = OperatorSequence(
        name="coresidence",
        runlist=[(add, "a", "b", "t"), (silu, "t", "y")],
        input_args=["a", "b"],
        output_args=["y"],
        dispatch="fused",
        coresident=coresident(add, silu),
    )
    seq.subbuffer_layout, seq.buffer_sizes, seq.slice_info = (
        seq.calculate_buffer_layout()
    )
    return seq


class Chain(iron.Graph):
    """add, silu, mul, add, silu on two columns: three designs, two recurring."""

    def __init__(self):
        super().__init__()
        narrow = dict(size=SIZE, tile_size=TILE, num_aie_columns=2)
        self.add = ElementwiseAdd(**narrow)
        self.silu = SiLU(**narrow)
        self.mul = ElementwiseMul(**narrow)

    def body(self, a, b):
        x = self.mul(self.silu(self.add(a, b)), b)
        return self.silu(self.add(x, b))


def _devices(text: str) -> list[str]:
    return re.findall(r"^  aie\.device\(\w+\) @(\w+) \{$", text, re.M)


def test_manual_pack_shares_one_configure():
    seq = _sequence(4, lambda add, silu: [[add, silu]])
    fused = Fusion(seq)
    text = fused.text()

    pack = Packing.device_name(list(fused.designs))
    assert fused.packing == Packing((tuple(fused.designs),))
    # The pack, and the reset the parity rule adds for one configure point
    # (main is left unnamed).
    assert _devices(text) == [pack, Fusion.RESET_DEVICE]
    assert re.findall(r"aiex\.configure @(\w+)", text) == [pack, Fusion.RESET_DEVICE]
    assert re.findall(r"aiex\.run @(\w+)", text) == list(fused.designs)


def test_policy_finds_the_manual_pack():
    manual = Fusion(_sequence(4, lambda add, silu: [[add, silu]])).text()
    auto = Fusion(_sequence(4, lambda add, silu: AdjacentPacking())).text()
    assert auto == manual


def test_policy_declines_what_does_not_fit():
    fused = Fusion(_sequence(8, lambda add, silu: []))
    text = fused.text()
    bodies = {}
    for name in fused.designs:
        body = re.search(
            rf"^  aie\.device\(\w+\) @{name} \{{$.*?^  \}}$", text, re.M | re.S
        )
        assert body is not None, f"no device @{name}"
        bodies[name] = body.group(0)
    for body in bodies.values():
        assert fits({"alone": body}) is None
    packing, stopped = AdjacentPacking().pack([n for n, *_ in fused.runlist], bodies)
    assert packing == Packing()
    [reason] = stopped.values()
    assert "ShimNOCTile" in reason


def test_merge_refuses_two_cores_on_one_tile():
    reason = fits({"x": _PINNED, "y": _PINNED})
    assert reason is not None and "aie.core" in reason and "(0, 2)" in reason


def test_packing_rejects_a_design_in_two_groups():
    with pytest.raises(ValueError, match="two groups"):
        Packing((("a", "b"), ("b", "c")))


def test_sequence_rejects_a_stray_operator():
    stray = SiLU(size=SIZE, tile_size=TILE, num_aie_columns=4)
    with pytest.raises(ValueError, match="not in the runlist"):
        _sequence(4, lambda add, silu: [[add, stray]])


def test_sequence_refuses_a_packing_without_a_full_elf():
    add = ElementwiseAdd(size=SIZE, tile_size=TILE, num_aie_columns=4)
    with pytest.raises(ValueError, match="one full-ELF device"):
        OperatorSequence(
            name="coresidence_xclbin",
            runlist=[(add, "a", "b", "y")],
            input_args=["a", "b"],
            output_args=["y"],
            dispatch="separate",
            coresident=AdjacentPacking(),
        )


def test_two_pins_on_one_shim_channel_do_not_fit():
    # Both members' logical shim tiles pinned to (0, 0), MM2S channel 1: the
    # fifo lowering must refuse the second, not the merge (neither pins a
    # physical aie.tile, so the merge sees nothing to share).
    reason = fits({"x": _shim_pinned(0, 1), "y": _shim_pinned(0, 1)})
    assert reason is not None and "already in use" in reason


@pytest.mark.parametrize("col, channel", [(0, 0), (1, 1)], ids=["channel", "column"])
def test_pins_on_distinct_shim_channels_fit(col, channel):
    assert fits({"x": _shim_pinned(0, 1), "y": _shim_pinned(col, channel)}) is None


def test_packing_is_in_the_fused_identity():
    # The fused generator closes over its Fusion, so the key follows the
    # modules a pack is merged and chosen in; and the packing itself is part
    # of the identity.
    temporal = Fusion(_sequence(4, lambda add, silu: []))
    packed = Fusion(_sequence(4, lambda add, silu: [[add, silu]]))
    reached = _python_identity([temporal])
    for module in (fusion, coresidence):
        assert f"{module.__name__}@".encode() in reached
    assert temporal.identity != packed.identity


def test_traced_graph_packs():
    # Three designs, add and silu recurring: the policy packs all three, so
    # the whole graph is one configure.
    traced = Chain().trace(a=(SIZE,), b=(SIZE,))
    temporal = traced.sequence("graph_temporal", dispatch="fused")
    packed = traced.sequence(
        "graph_packed", dispatch="fused", coresident=AdjacentPacking()
    )
    temporal.prepare()
    packed.prepare()
    fused = Fusion(packed)
    assert len(fused.designs) == 3 and len(fused.runlist) == 5

    # Temporal: a configure per step that changes design, and the reset.
    assert len(re.findall(r"aiex\.configure", Fusion(temporal).text())) == 6
    # Packed: one pack named for all three designs, each step its own run.
    text = fused.text()
    assert re.findall(r"aiex\.configure @(\w+)", text) == [
        Packing.device_name(list(fused.designs)),
        Fusion.RESET_DEVICE,
    ]
    assert re.findall(r"aiex\.run @(\w+)", text) == [n for n, *_ in fused.runlist]


@_builds_elf
def test_pack_compiles_to_a_full_elf():
    seq = _sequence(4, lambda add, silu: [[add, silu]])
    seq.compile()
    designs = list(Fusion(seq).designs)
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
    version = Chain().compile(
        image=iron.ELF, coresident=AdjacentPacking(), a=(SIZE,), b=(SIZE,)
    )
    assert version.sequence.coresident == AdjacentPacking()
    fused = Fusion(version.sequence)
    assert re.findall(r"aiex\.configure @(\w+)", fused.text()) == [
        Packing.device_name(list(fused.designs)),
        Fusion.RESET_DEVICE,
    ]
