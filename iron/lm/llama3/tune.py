# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure Llama 3's cost table on this NPU (``iron.lm.tune``), beside
this file as ``costs_<device>.json``; ``--dispatch separate`` on an NPU2
prices an xclbin chain (``--each-step`` in ``iron.lm.runner``) as
``costs_npu2_separate.json``:

```bash
python -m iron.lm.llama3.tune
python -m iron.lm.llama3.tune --dispatch separate
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
