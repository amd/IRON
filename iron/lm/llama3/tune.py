# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure Llama 3's cost table on this NPU (``iron.lm.tune``).

``costs_npu2.json`` beside this file is such a table, measured on a
Strix Halo NPU (8 columns):

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
        Path(__file__).with_name("costs_npu2.json"),
    )
