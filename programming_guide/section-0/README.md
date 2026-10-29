<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 0 - Getting Set Up

This guide assumes IRON is installed as the top-level
[README](../../README.md#installation-linux) describes: the XDNA driver,
XRT, and `pip install -r requirements.txt`, which also installs this
checkout in editable mode.

## Check your installation

```bash
source /opt/xilinx/xrt/setup.sh
xrt-smi examine            # confirms XRT sees the NPU
pytest iron/tests/operators/test_catalog.py -k AXPY
```

If the test passes, the toolchain can compile for and run on your NPU.

## The device

Every operator and graph compiles for *the current device*. When an NPU is
attached, IRON finds it through XRT. On a host without one, for example to
compile without running or to check a design against its numpy reference,
bind a device before anything else runs:

```python
import aie.utils as aie_utils
from aie.iron.device import from_name

aie_utils.set_current_device(from_name("npu2", n_cols=8))
```

`npu1` is Phoenix and Hawk Point, with 4 usable columns. `npu2` is Strix,
Strix Halo and Krackan, with 8. The examples in this guide build operators
and graphs the same way either way. Only calling a compiled graph or
operator needs a real NPU.

## The cache

Compiled artifacts are cached by content hash under
`${NPU_CACHE_HOME:-~/.npu/cache}`. Nothing is written next to your source.
To give a session its own cache:

```bash
export NPU_CACHE_HOME=/scratch/$USER/iron_cache
```

The first compile of a design is the slow one. Compiling the same design
again with the same cache reuses what is already there.

## Where to go next

* [Section 1 — An operator on its own](../section-1/) calls one operator
  without a graph.
* [Section 2 — Your first graph](../section-2/) composes several operators
  into one compiled image.

-----
[Top](..) &middot; [Next](../section-1/)
