#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every fused group of a stream-backed operator's mapping names a kernel for each of
its layers and tiles only its own layers; an operator joins by adding to :data:`DESIGNS`.
"""

import pytest
import yaml

pytest.importorskip(
    "stream", reason="stream-dse not installed (see requirements_stream.txt)"
)

import aie.utils as aie_utils  # noqa: E402
from aie.iron.device import NPU2  # noqa: E402

aie_utils.set_current_device(NPU2())

from iron.operators.mha_prefill_stream import stream_design as mha  # noqa: E402
from iron.operators.swiglu_prefill_stream import stream_design as swiglu  # noqa: E402

# Stream-backed operators as (design module, dimensions, group counts built).
DESIGNS = {
    "swiglu": (swiglu, (256, 512, 2048), (1, 2, 5)),
    "mha": (mha, (256, 64), (mha.LAYER_BY_LAYER,)),
}


def group_findings(mapping: dict, index: int) -> list[str]:
    """Why the fused group at ``index`` cannot be lowered."""
    layers = {layer["name"]: layer for layer in mapping["layers"]}
    group = mapping["fused_groups"][index]
    findings = []
    for name in group["layers"]:
        layer = layers.get(name)
        if layer is None:
            findings.append(f"{group['name']} names unmapped layer {name}")
        elif not layer["kernel"]["name"]:
            findings.append(f"{name} names no kernel")
    for entry in group["intra_core_tiling"]:
        if str(entry["dim"]).split(".")[0] not in group["layers"]:
            findings.append(f"{group['name']} tiles {entry['dim']} from another group")
    return findings


def _cases():
    for operator, (design, dims, counts) in DESIGNS.items():
        for k in counts:
            for index in range(k):
                yield pytest.param(
                    design, dims, k, index, id=f"{operator}-k{k}-group{index}"
                )


CASES = list(_cases())


@pytest.mark.parametrize("design, dims, k, index", CASES)
def test_group_names_the_kernels_of_its_layers(design, dims, k, index, tmp_path):
    _, mapping_path = design.build_inputs(*dims, output_dir=str(tmp_path), k=k)
    with open(mapping_path) as handle:
        mapping = yaml.safe_load(handle)
    assert group_findings(mapping, index) == []


def test_a_flash_mapping_seeds_at_the_finest_block_the_kernels_compile_for():
    """The query block is stream-dse's to choose, so IRON only says where the search
    starts, and it starts fine because placement is generated from the seed."""
    from iron.common.stream.kernel_library import flash_blocks

    seed = mha.flash_query_seed()
    assert seed == min(flash_blocks())
    assert mha.query_tile(256, 1, flash=True) == seed
    assert mha.kernel_tiles(256, 64, 1, flash=True)[mha.SCORES_NODE][0] == seed
