#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Co-residence: two designs packed into one device configuration.

``y = silu(a + b)`` as a fused sequence, each op on half the columns, so the
pair can share the array. Checked end to end at the MLIR level -- one pack
device, one configure point for both steps, each step running its own named
sequence -- and through aiecc to a full ELF. The placer-driven policy must
find the same pack a caller would name by hand, and must decline a pair
whose union needs more shim channels than the array has, or two members
pinning one shim DMA channel. A traced ``@iron.graph`` reaches the same
packing through ``TracedGraph.sequence``.

Compile-only: nothing here dispatches, so no NPU is needed, only the
toolchain.
"""

import json
import re
from pathlib import Path

import numpy as np
import pytest

import aie.utils as aie_utils
from aie.dialects import aie as aie_dialect
from aie.iron import ObjectFifo, Program, Runtime
from aie.iron.device import NPU2, AnyShimTile, Tile, from_name

import iron
from iron.common.image import OperatorSequence, build_fused_mlir, coresidence, fusion
from iron.common.image.coresidence import AdjacentPacking, Packing, fits
from iron.common.image.fused import fused_plan
from iron.common.image.jit_compile import _GENERATOR_TREES
from iron.operators import ElementwiseAdd, ElementwiseMul, SiLU

SIZE = 8192
TILE = 256

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
    ``channel``: the device text, as a generator would hand it to the merge."""
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


def _chain_fn(a, b):
    narrow = dict(num_aie_columns=2, tile_size=TILE)
    x = SiLU(ElementwiseAdd(a, b, **narrow), **narrow)
    x = ElementwiseMul(x, b, **narrow)
    return SiLU(ElementwiseAdd(x, b, **narrow), **narrow)


_chain = iron.graph(_chain_fn)


@pytest.fixture(autouse=True)
def device():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)


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


def _devices(text: str) -> list[str]:
    return re.findall(r"^  aie\.device\(\w+\) @(\w+) \{$", text, re.M)


def test_manual_pack_shares_one_configure():
    seq = _sequence(4, lambda add, silu: [[add, silu]])
    generators, _, packing = fused_plan(seq)
    text = build_fused_mlir(seq)

    pack = Packing.device_name(list(generators))
    assert packing.groups == (tuple(generators),)
    # The pack, the reset the parity rule adds for one configure point, and
    # main (which the fused module leaves unnamed).
    assert _devices(text) == [pack, "reset_device"]
    assert re.findall(r"aiex\.configure @(\w+)", text) == [pack, "reset_device"]
    assert re.findall(r"aiex\.run @(\w+)", text) == list(generators)


def test_policy_finds_the_manual_pack():
    manual = build_fused_mlir(_sequence(4, lambda add, silu: [[add, silu]]))
    auto = build_fused_mlir(_sequence(4, lambda add, silu: AdjacentPacking()))
    assert auto == manual


def test_policy_declines_what_does_not_fit():
    seq = _sequence(8, lambda add, silu: [])
    generators, runlist, _ = fused_plan(seq)
    text = build_fused_mlir(seq)
    bodies = {
        name: re.search(
            rf"^  aie\.device\(\w+\) @{name} \{{$.*?^  \}}$", text, re.M | re.S
        ).group(0)
        for name in generators
    }
    for body in bodies.values():
        assert fits({"alone": body}) is None
    packing, stopped = AdjacentPacking().pack([n for n, *_ in runlist], bodies)
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


def test_pack_compiles_to_a_full_elf():
    seq = _sequence(4, lambda add, silu: [[add, silu]])
    generators, _, _ = fused_plan(seq)
    seq.compile()
    config = json.loads((seq.elf_path.parent / "full_elf_config.json").read_text())
    instances = [
        instance["id"]
        for kernel in config["xrt-kernels"]
        if kernel["name"] == Packing.device_name(list(generators))
        for instance in kernel["instance"]
    ]
    assert instances == list(generators)


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
    # The fused identity digests every source under the generator trees, so
    # an edit to how a pack is merged or chosen rebuilds what was packed.
    for module in (fusion, coresidence):
        path = Path(module.__file__).resolve()
        assert any(path.is_relative_to(root) for root in _GENERATOR_TREES)


def test_traced_graph_packs_and_compiles():
    # add, silu, mul, add, silu: three designs, add and silu recurring. The
    # policy packs all three, so the whole graph is one configure.
    traced = _chain.trace(a=(SIZE,), b=(SIZE,))
    temporal = traced.sequence(name="graph_temporal", dispatch="fused")
    packed = traced.sequence(
        name="graph_packed", dispatch="fused", coresident=AdjacentPacking()
    )
    temporal.prepare()
    packed.prepare()
    generators, runlist, _ = fused_plan(packed)
    assert len(generators) == 3 and len(runlist) == 5

    # Temporal: a configure per step that changes design, and the reset.
    temporal_text = build_fused_mlir(temporal)
    packed_text = build_fused_mlir(packed)
    assert len(re.findall(r"aiex\.configure", temporal_text)) == 6
    # Packed: one pack named for all three designs, each step its own run.
    pack = Packing.device_name(list(generators))
    assert re.findall(r"aiex\.configure @(\w+)", packed_text) == [
        pack,
        "reset_device",
    ]
    assert re.findall(r"aiex\.run @(\w+)", packed_text) == [
        name for name, *_ in runlist
    ]
    packed.compile()
    assert packed.elf_path.is_file()


def test_graph_compile_forwards_the_packing():
    # A fresh graph function: versions are cached per function and signature.
    version = iron.graph(_chain_fn).compile(
        coresident=AdjacentPacking(), a=(SIZE,), b=(SIZE,)
    )
    assert version.sequence.coresident == AdjacentPacking()
    generators, _, _ = fused_plan(version.sequence)
    text = build_fused_mlir(version.sequence)
    assert re.findall(r"aiex\.configure @(\w+)", text) == [
        Packing.device_name(list(generators)),
        "reset_device",
    ]
