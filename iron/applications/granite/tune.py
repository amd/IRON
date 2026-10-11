# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure Granite 4.2 3B's cost table on this NPU (``iron.lm.tune``),
beside this file as ``costs_<device>.json``; ``--dispatch separate``
prices the per-step xclbin chain (``--each-step`` in
``iron.lm.base``) as ``costs_npu2_separate.json``:

```bash
python -m iron.applications.granite.tune
python -m iron.applications.granite.tune --dispatch separate
```
"""

from pathlib import Path

from iron.lm import tune

from .model import Runner

if __name__ == "__main__":
    tune.main(
        Runner,
        "Measure Granite 4.2 3B's cost table, its decode step and prompt chunk",
        Path(__file__).parent,
    )
