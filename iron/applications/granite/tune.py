# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure Granite 4.2 3B's cost table on this NPU (``iron.lm.tune``),
beside this file as ``costs_<device>.json``.

Granite's decode step does not fit a full ELF at its scale (see
``model.py``'s docstring), so it always runs each step as its own xclbin
dispatch: give ``--dispatch separate``, not the default, which measures
the fused (full-ELF) packaging this device cannot build:

```bash
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
