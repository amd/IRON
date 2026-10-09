# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure EmbeddingGemma 2's audio cost table on this NPU, beside this
file as ``costs_<device>.json`` (``iron.common.graph.tune``): every design
of each version, at each width, as traced and with each fold it admits,
and the configure cost between a pair of them. A design's time follows
its shapes, not the weights, so no checkpoint is read. Run with XRT
sourced and the NPU otherwise idle:

```bash
python -m iron.lm.embeddinggemma2.audio.tune
```
"""

import aie.utils as aie_utils

from iron.common.graph import tune
from iron.common.graph.probe import Call

from .model import AUDIO, COSTS, Audio, unread_audio_weights

CALIBRATION_PAIRS = [("ElementwiseAdd", "ElementwiseMul"), ("SiLU", "ElementwiseMul")]


def main():
    args = tune.parser(__doc__.split("\n\n")[0], COSTS).parse_args()
    dev = aie_utils.ensure_current_device()
    graph = Audio(AUDIO, unread_audio_weights(AUDIO))
    # Each version at its every frame real.
    calls = []
    for s in graph.shapes():
        frames = s["x"][0][0] // AUDIO.hop - 1
        calls += Call.admitted(
            graph.trace(**s), dev, dict(n=frames // 2, frames=frames)
        )
    tune.measure(args, calls, CALIBRATION_PAIRS, COSTS)


if __name__ == "__main__":
    main()
