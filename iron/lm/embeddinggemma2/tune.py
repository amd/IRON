# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure EmbeddingGemma 2's text cost table on this NPU, beside this file
as ``costs_<device>.json`` (``iron.common.graph.tune``; each tower's is its
own, ``vision.tune``'s and ``audio.tune``'s): every design of the text
encoder and of each mixed version of the multimodal graph, at each width,
as traced and with each fold it admits, and the configure cost between
three of them. A design's time follows its shapes, not the weights, so
no checkpoint is read. Run with XRT sourced and the NPU otherwise idle:

```bash
python -m iron.lm.embeddinggemma2.tune
```
"""

import aie.utils as aie_utils
import numpy as np

from iron.common.graph import tune
from iron.common.graph.probe import Call
from iron.lm import unread_weights
from iron.operators import GELU, ElementwiseAdd, ElementwiseMul

from .audio.model import AUDIO, AudioTower, unread_audio_weights
from .model import COSTS, EMBEDDINGGEMMA_2, EmbeddingGemma, layout
from .multimodal import Multimodal
from .vision import model as vision_model

CALIBRATION_TRIANGLE = (ElementwiseAdd, GELU, ElementwiseMul)


def main():
    args = tune.parser(__doc__.split("\n\n")[0], COSTS).parse_args()
    dev = aie_utils.ensure_current_device()
    c, A, V = EMBEDDINGGEMMA_2, AUDIO, vision_model.VISION
    weights = unread_weights(layout(c), c.n_layers)
    text = EmbeddingGemma(c, weights)
    audio = AudioTower(A, unread_audio_weights(A))
    vision = vision_model.VisionTower(
        V, unread_weights(vision_model.layout(V), V.n_layers)
    )
    # Every call at its longest bound: each row real, the clip its longest,
    # the image the largest, its patches filled.
    calls = [
        call
        for s in text.shapes()
        for call in Call.admitted(text.trace(**s), dev, dict(n=s["ids"][0][0]))
    ]
    processor = vision.processor
    _, sized = processor.inputs(
        np.zeros((*vision_model.LARGEST, 3), np.uint8),
        processor.patches // V.pool**2,
    )
    T_a = audio.max_tokens
    graph = Multimodal(c, weights, text.max_tokens, audio, vision)
    (s,) = graph.shapes()
    sizes = dict(sized)
    values = dict(
        n=s["ids"][0][0],
        n_audio=2 * T_a,
        frames=4 * T_a,
        audio_tokens=T_a,
        n_patches=sizes.pop("n"),
        **sizes,
    )
    for shapes in (
        dict(wave=(((4 * T_a + 1) * A.hop,), np.float32)),
        processor.shapes(),
        dict(placed=s["ids"]),
    ):
        calls += Call.admitted(graph.trace(**shapes), dev, values)
    tune.measure(args, calls, CALIBRATION_TRIANGLE, COSTS)


if __name__ == "__main__":
    main()
