<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 0 - Getting Set Up

This guide assumes IRON is already installed, as the top-level
[README](../../README.md#installation-linux) describes: the XDNA driver and
XRT, `pip install -r requirements.txt`, and `pip install -e .` from this
checkout.

## Check your installation

```bash
source /opt/xilinx/xrt/setup.sh
xrt-smi examine            # confirms XRT sees the NPU
pytest iron/tests/operators/test_catalog.py -k AXPY
```

If that test passes, the toolchain compiles and runs on your attached NPU.

## The device

Every operator and graph compiles for *the current device*, which `iron`
detects automatically from XRT when one is attached. On a host with no NPU
(to compile without running, or to record and check a design against its
numpy reference), bind one explicitly before anything else runs:

```python
import aie.utils as aie_utils
from aie.iron.device import from_name

aie_utils.set_current_device(from_name("npu2", n_cols=8))
```

`npu1` is Phoenix and Hawk Point (4 columns usable); `npu2` is Strix, Strix
Halo and Krackan (8 columns). The rest of this guide's examples call
`iron.operators` and `iron.Graph` the same way whether a real NPU answers or
not; only the device run itself (calling a compiled graph) needs one
attached.

## The cache

Compiled artifacts are cached by content hash under `${NPU_CACHE_HOME:-~/.npu/cache}`,
nothing is written next to your source. Point a session at its own cache
with:

```bash
export NPU_CACHE_HOME=/scratch/$USER/iron_cache
```

The first compile of a design is the slow one; a later compile of the same
shape, on the same machine, with the same cache, is near-instant.

## Where to go next

* [Section 1 — An operator on its own](../section-1/) to call one operator
  without recording a graph.
* [Section 2 — Your first graph](../section-2/) to compose several operators
  into one compiled image.

-----
[Top](..) &middot; [Next](../section-1/)
