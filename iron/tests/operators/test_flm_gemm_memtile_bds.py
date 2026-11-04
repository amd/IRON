# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""flm.ProjectionGEMM's B memtile chains hold to the BD ids their channels reach, device-free."""

import re
import subprocess
from pathlib import Path

import aie.utils.config as aie_config
import numpy as np
import pytest
from aie.helpers.taplib import PerCall

from iron import Precision
from iron.common.design.design import OperatorDesign
from iron.common.image.packaging import Kind
from iron.operators.flm.gemm.op import ProjectionGEMM

# Through runtime BD assignment as aiecc runs it, reclaiming as ProjectionGEMM asks.
PIPELINE = (
    "builtin.module(aie.device(aie-place-tiles{placer=sequential_placer}),"
    "aie-lower-scratchpad-parameters,"
    "aie.device(aie-objectFifo-stateful-transform,aie-assign-lock-ids,"
    "aie-reserve-runtime-bd-ids,aie-assign-bd-ids,aie-prepare-buffers,"
    "aie-assign-buffer-addresses,aie-create-pathfinder-flows,"
    "aie-materialize-bd-chains,aie-substitute-shim-dma-allocations,"
    "aie-assign-runtime-sequence-bd-ids{reclaim-bds=true}))"
)


@pytest.mark.parametrize("device", ["npu1", "npu2"])
@pytest.mark.parametrize("k_tile,resident", [(256, False), (512, True)])
def test_a_bounded_b_never_reclaims_a_memtile_bd(device, k_tile, resident, request):
    """Gemma 4's prompt projection at a k tile that puts six slots in the pool.

    Resident under a bound, its fill, peek and final chains took 18 BD ids where
    16 are free, so aiecc reclaimed the live fill's behind a poll that never
    returns: the device hung. It streams instead; three slots stay resident.
    """
    request.getfixturevalue(device)
    op = ProjectionGEMM(
        M=2048,
        K=1536,
        N=12288,
        b_col_maj=True,
        precision=Precision.MEDIUM,
        k_tile=k_tile,
    )
    op.use_value("valid", PerCall("rows", Kind.SCRATCHPAD, np.int32).affine())
    op = op.resolved()
    assert op._b_resident == resident
    lowered = subprocess.run(
        [
            str(Path(aie_config.aiecc_path()).with_name("aie-opt")),
            f"--pass-pipeline={PIPELINE}",
            "-o",
            "/dev/null",
        ],
        input=str(OperatorDesign(op).module()),
        capture_output=True,
        text=True,
    )
    assert lowered.returncode == 0, lowered.stderr[-2000:]
    memtiles = re.findall(r"tile \(\d+,1\) has no free buffer", lowered.stderr)
    assert not memtiles, memtiles
