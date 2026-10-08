# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure Llama 3's cost table on this NPU (``iron.lm.tune``), beside
this file as ``costs_<device>.json``: ``costs_npu2.json`` is one, measured
on a Strix Halo NPU (8 columns); on NPU1 it is an xclbin chain's,
``costs_npu1.json``:

```bash
python -m iron.lm.llama3.tune
```
"""

from pathlib import Path

from iron.lm import tune

from .model import Runner

if __name__ == "__main__":
    tune.main(
        Runner,
        "Measure Llama 3.2 1B's cost table, its decode step and prompt chunk",
        Path(__file__).parent,
    )
