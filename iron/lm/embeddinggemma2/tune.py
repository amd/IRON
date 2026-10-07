# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure EmbeddingGemma 2's cost table on this NPU (``iron.common.graph.tune``):
every design of each version, at each width, as traced and with each fold
it admits, and the configure cost between a few pairs of them. A design's
time follows its shapes, not the weights, so no checkpoint is read. Run
with XRT sourced and the NPU otherwise idle:

```bash
python -m iron.lm.embeddinggemma2.tune
```
"""

import aie.utils as aie_utils

from iron.common.graph import tune
from iron.common.graph.probe import Call
from iron.lm import unread_weights

from .encoder import COSTS
from .model import EMBEDDINGGEMMA_2, EmbeddingGemma, layout

CALIBRATION_PAIRS = [
    ("ElementwiseAdd", "ElementwiseMul"),
    ("ElementwiseAdd", "GELU"),
    ("GELU", "ElementwiseMul"),
]


def main():
    args = tune.parser(__doc__.split("\n\n")[0], COSTS).parse_args()
    dev = aie_utils.ensure_current_device()
    c = EMBEDDINGGEMMA_2
    graph = EmbeddingGemma(c, unread_weights(layout(c), c.n_layers), c.sliding_window)
    # Each version at its every row real: the masked Softmax's longest span.
    calls = [
        call
        for s in graph.shapes()
        for call in Call.admitted(graph.trace(**s), dev, dict(n=s["x"][0]))
    ]
    tune.measure(args, calls, CALIBRATION_PAIRS)


if __name__ == "__main__":
    main()
