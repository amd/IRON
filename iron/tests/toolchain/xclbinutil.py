# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The installed ``xclbinutil`` round-trips an AIE partition.

aiecc links a chained xclbin (``--xclbin-input``, the separate dispatch's
image) by dumping the previous xclbin's ``AIE_PARTITION`` as JSON,
appending a PDI and re-adding it, so the tool's own dump must be something
its own add accepts. The Boost-free ``xclbinutil`` mlir-aie vendors under
``tools/hrx-xclbinutil`` dumped every scalar array element nested one level
too deep (``"start_columns": [["0"]]``) and then refused its own output
("bad value: "), so no chain could be linked with it. The fix is carried in
``patches/hrx-xclbinutil-empty-path.patch``; this names the failure when
an unpatched build is on the PATH, instead of a chained build failing
three tools down.
"""

import json
import subprocess
from pathlib import Path

from iron.tests.toolchain.tools import XCLBINUTIL, requires

PATCH = Path(__file__).with_name("patches") / "hrx-xclbinutil-empty-path.patch"

pytestmark = requires("xclbinutil")


def _run(*args, cwd):
    assert XCLBINUTIL is not None
    result = subprocess.run(
        [XCLBINUTIL, *args], cwd=cwd, capture_output=True, text=True, timeout=120
    )
    assert (
        result.returncode == 0
    ), f"xclbinutil {' '.join(args)} failed:\n{result.stdout[-2000:]}{result.stderr[-2000:]}"
    return result


def _flat(obj):
    """Whether every array holds scalars or objects, never a bare array."""
    if isinstance(obj, dict):
        return all(_flat(v) for v in obj.values())
    if isinstance(obj, list):
        return all(not isinstance(v, list) and _flat(v) for v in obj)
    return True


def test_a_dumped_partition_is_flat_and_re_adds(tmp_path):
    pdi = tmp_path / "sample.pdi"
    pdi.write_bytes(bytes(range(256)) * 4)
    partition = {
        "aie_partition": {
            "name": "QoS",
            "operations_per_cycle": "2048",
            "inference_fingerprint": "23423",
            "pre_post_fingerprint": "12345",
            "partition": {"column_width": 4, "start_columns": [0, 4]},
            "PDIs": [
                {
                    "uuid": "acd92aa2-2672-46b4-85df-cfd997367d63",
                    "file_name": str(pdi),
                    "cdo_groups": [
                        {
                            "name": "DPU",
                            "type": "PRIMARY",
                            "pdi_id": "0x01",
                            "dpu_kernel_ids": ["0x901"],
                            "pre_cdo_groups": ["0xC1"],
                        }
                    ],
                }
            ],
        }
    }
    (tmp_path / "partition.json").write_text(json.dumps(partition))
    _run(
        "--add-replace-section",
        f"AIE_PARTITION:JSON:{tmp_path / 'partition.json'}",
        "--force",
        "--output",
        str(tmp_path / "part.xclbin"),
        cwd=tmp_path,
    )
    _run(
        "--dump-section",
        f"AIE_PARTITION:JSON:{tmp_path / 'dump.json'}",
        "--force",
        "--quiet",
        "--input",
        str(tmp_path / "part.xclbin"),
        cwd=tmp_path,
    )
    dumped = json.loads((tmp_path / "dump.json").read_text())
    assert _flat(dumped), (
        f"xclbinutil nests scalar array elements on dump: {dumped}\n"
        f"an unpatched hrx-xclbinutil; apply {PATCH} to mlir-aie and rebuild"
    )
    part = dumped["aie_partition"]
    assert part["partition"]["start_columns"] == ["0", "4"]
    assert part["PDIs"][0]["cdo_groups"][0]["dpu_kernel_ids"] == ["0x901"]
    # What aiecc does next: re-add the dump. The dump names the PDI by uuid
    # next to itself, which is why this runs from tmp_path.
    _run(
        "--input",
        str(tmp_path / "part.xclbin"),
        "--add-replace-section",
        f"AIE_PARTITION:JSON:{tmp_path / 'dump.json'}",
        "--force",
        "--output",
        str(tmp_path / "part2.xclbin"),
        cwd=tmp_path,
    )
    assert (tmp_path / "part2.xclbin").stat().st_size > 0
