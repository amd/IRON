# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure EmbeddingGemma 2's vision cost table on this NPU, beside this
file as ``costs_<device>.json`` (``iron.common.graph.tune``): every design
of the graph, at each width, as traced and with each fold it admits,
and the configure cost between three of them. A design's time follows
its shapes, not the weights, so no checkpoint is read. Run with XRT
sourced and the NPU otherwise idle:

```bash
python -m iron.lm.embeddinggemma2.vision.tune
```
"""

import aie.utils as aie_utils
import numpy as np

from iron.common.graph import tune
from iron.common.graph.probe import Call
from iron.lm import unread_weights
from iron.operators import GELU, ElementwiseAdd, ElementwiseMul

from .model import COSTS, LARGEST, VISION, Vision, layout

CALIBRATION_TRIANGLE = (ElementwiseAdd, GELU, ElementwiseMul)


def main():
    args = tune.parser(__doc__.split("\n\n")[0], COSTS).parse_args()
    dev = aie_utils.ensure_current_device()
    graph = Vision(VISION, unread_weights(layout(VISION), VISION.n_layers))
    # At the largest image, its patches filled.
    processor = graph.vision.processor
    (s,) = graph.shapes()
    _, values = processor.inputs(
        np.zeros((*LARGEST, 3), np.uint8), processor.patches // VISION.pool**2
    )
    calls = Call.admitted(graph.trace(**s), dev, values)
    tune.measure(args, calls, CALIBRATION_TRIANGLE, COSTS)


if __name__ == "__main__":
    main()
