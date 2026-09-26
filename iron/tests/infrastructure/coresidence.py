#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Co-residence: two designs packed into one device configuration.

``y = silu(a + b)`` as a fused sequence, each op on half the columns, so the
pair can share the array. Checked end to end at the MLIR level -- one pack
device, one configure point for both steps, each step running its own named
sequence -- and through aiecc to a full ELF. The placer-driven policy must
find the same pack a caller would name by hand, and must decline a pair
whose union needs more shim channels than the array has.

Compile-only: nothing here dispatches, so no NPU is needed, only the
toolchain.
"""

import json
import re

import pytest

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.common.image import OperatorSequence, build_fused_mlir
from iron.common.image.coresidence import AdjacentPacking, Packing, fits
from iron.common.image.fused import fused_plan
from iron.operators import ElementwiseAdd, SiLU

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
