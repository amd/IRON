# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure EmbeddingGemma 2's vision cost table on this NPU, beside this
file as ``costs_<device>.json`` (``iron.common.graph.tune``): every design
of each version, at each width, as traced and with each fold it admits,
and the configure cost between a pair of them. A design's time follows
its shapes, not the weights, so no checkpoint is read. Run with XRT
sourced and the NPU otherwise idle:

```bash
python -m iron.lm.embeddinggemma2.vision.tune
```
"""

import aie.utils as aie_utils

from iron.common.graph import tune
from iron.common.graph.probe import Call
from iron.lm import unread_weights

from .model import COSTS, VISION, Vision, layout

CALIBRATION_PAIRS = [("ElementwiseAdd", "GELU"), ("GELU", "ElementwiseMul")]


def main():
    args = tune.parser(__doc__.split("\n\n")[0], COSTS).parse_args()
    dev = aie_utils.ensure_current_device()
    graph = Vision(VISION, unread_weights(layout(VISION), VISION.n_layers))
    # Each version at its every row real: the masked Softmax's longest span.
    calls = [
        call
        for s in graph.shapes()
        for call in Call.admitted(graph.trace(**s), dev, dict(n=s["pixels"][0]))
    ]
    tune.measure(args, calls, CALIBRATION_PAIRS, COSTS)


if __name__ == "__main__":
    main()
