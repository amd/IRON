# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure EmbeddingGemma 2's audio cost table on this NPU, beside this
file as ``costs_<device>.json`` (``iron.common.graph.tune``): every design
of the graph, at each width, as traced and with each fold it admits,
and the configure cost between three of them. A design's time follows
its shapes, not the weights, so no checkpoint is read. Run with XRT
sourced and the NPU otherwise idle:

```bash
python -m iron.lm.embeddinggemma2.audio.tune
```
"""

import aie.utils as aie_utils

from iron.common.graph import tune
from iron.common.graph.probe import Call
from iron.operators import ElementwiseAdd, ElementwiseMul, SiLU

from .model import AUDIO, COSTS, Audio, unread_audio_weights

CALIBRATION_TRIANGLE = (ElementwiseAdd, SiLU, ElementwiseMul)


def main():
    args = tune.parser(__doc__.split("\n\n")[0], COSTS).parse_args()
    dev = aie_utils.ensure_current_device()
    graph = Audio(AUDIO, unread_audio_weights(AUDIO))
    # Every frame real.
    (s,) = graph.shapes()
    T = graph.audio.max_tokens
    calls = Call.admitted(graph.trace(**s), dev, dict(n=2 * T, frames=4 * T, tokens=T))
    tune.measure(args, calls, CALIBRATION_TRIANGLE, COSTS)


if __name__ == "__main__":
    main()
