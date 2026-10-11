#!/usr/bin/env python3

# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure SmolLM2's cost table on this NPU (``iron.lm.tune``), beside
this file as ``costs_<device>.json``; ``--dispatch separate`` on an NPU2
prices an xclbin chain (``--each-step`` in ``iron.lm.base``) as
``costs_npu2_separate.json``:

```bash
python -m iron.applications.llama.smollm2.tune
python -m iron.applications.llama.smollm2.tune --dispatch separate
```
"""

from pathlib import Path

from iron.lm import tune

from iron.applications.llama.model import SmolLM2Runner

if __name__ == "__main__":
    tune.main(
        SmolLM2Runner,
        "Measure SmolLM2 1.7B Instruct's cost table, its decode step and prompt chunk",
        Path(__file__).parent,
    )
