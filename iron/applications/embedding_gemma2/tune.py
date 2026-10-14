# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure EmbeddingGemma 2's cost table on this NPU, in ``profiles/`` as
``costs_<device>.json`` (``iron.common.graph.tune``): every design of every
version of ``Multimodal`` (the text encoder, each tower, the merge) at its
longest call, at each width, as traced and with each fold it admits, and
the configure cost between three of them. A design's time follows its
shapes, not the weights, so no checkpoint is read. Run with XRT sourced
and the NPU otherwise idle:

```bash
python -m iron.applications.embedding_gemma2.tune
```
"""

import aie.utils as aie_utils

from iron.common.graph import tune
from iron.common.graph.probe import Call
from iron.lm.tune import CALIBRATION_TRIANGLE

from .config import PROFILES, Config
from .model import Multimodal
from .weights import Weights


def main():
    args = tune.parser(
        "Measure EmbeddingGemma 2's cost table: the text encoder and both towers",
        PROFILES,
    ).parse_args()
    dev = aie_utils.ensure_current_device()
    graph = Multimodal(Config(), Weights.unread())
    calls = [
        call
        for shapes in graph.shapes()
        for call in Call.admitted(graph.trace(**shapes), dev, graph.longest())
    ]
    tune.measure(args, calls, CALIBRATION_TRIANGLE, PROFILES)


if __name__ == "__main__":
    main()
