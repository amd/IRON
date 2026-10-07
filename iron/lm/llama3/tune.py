# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure Llama 3's decode cost table on this NPU (``iron.lm.tune``).

``decode_costs_<device>.json`` beside this file are such tables, the
current device's the default: ``npu2`` measured on a Strix Halo NPU (8
columns), ``npu1`` on a Phoenix NPU (4 columns):

```bash
python -m iron.lm.llama3.tune model.safetensors tokenizer.model
```
"""

from pathlib import Path

import aie.utils as aie_utils

from iron.lm import tune

from .model import Runner

if __name__ == "__main__":
    tune.main(
        Runner,
        "Measure Llama 3.2 1B's decode cost table",
        Path(__file__).with_name(
            f"decode_costs_{aie_utils.ensure_current_device().name}.json"
        ),
    )
