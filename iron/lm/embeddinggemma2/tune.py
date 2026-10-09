# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure EmbeddingGemma 2's text cost table on this NPU, beside this file
as ``costs_<device>.json`` (``iron.common.graph.tune``; each tower's is its
own, ``vision.tune``'s and ``audio.tune``'s): every design of the text
encoder and of each mixed version of the multimodal graph, at each width,
as traced and with each fold it admits, and the configure cost between a
few pairs of them. A design's time follows its shapes, not the weights, so
no checkpoint is read. Run with XRT sourced and the NPU otherwise idle:

```bash
python -m iron.lm.embeddinggemma2.tune
```
"""

import itertools

import aie.utils as aie_utils
import numpy as np

from iron.common.graph import tune
from iron.common.graph.probe import Call
from iron.lm import unread_weights

from .audio.model import AUDIO, AudioTower, unread_audio_weights
from .model import COSTS, EMBEDDINGGEMMA_2, EmbeddingGemma, layout
from .multimodal import Multimodal
from .vision import model as vision_model

CALIBRATION_PAIRS = [
    ("ElementwiseAdd", "ElementwiseMul"),
    ("ElementwiseAdd", "GELU"),
    ("GELU", "ElementwiseMul"),
]


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
    # Every call at its longest bound: each row real, each vision version at
    # the largest image it takes, its patches filled.
    calls = [
        call
        for s in text.shapes()
        for call in Call.admitted(text.trace(**s), dev, dict(n=s["ids"][0][0]))
    ]
    sized = {
        T: vision.processor.inputs(np.zeros((*image, 3), np.uint8), T // V.pool**2)[1]
        for T, image in zip(vision.rows, vision_model.LARGEST, strict=True)
    }
    graph = Multimodal(c, weights, text.max_tokens, audio, vision)
    # A tower version's fewest soft tokens: one past the version before it.
    fewest_audio = dict(zip(audio.rows, (1, *(T + 1 for T in audio.rows))))
    fewest_image = dict(
        zip(vision.rows, (1, *(T // V.pool**2 + 1 for T in vision.rows)))
    )
    fewest_audio[0] = fewest_image[0] = 0
    for s, T_a, T_v in itertools.product(graph.shapes(), fewest_audio, fewest_image):
        rows = s["ids"][0][0]
        if not T_a and not T_v or fewest_audio[T_a] + fewest_image[T_v] > rows:
            continue
        shapes = dict(ids=s["ids"])
        if T_a:
            shapes["wave"] = (((4 * T_a + 1) * A.hop,), np.float32)
        values = dict(
            n=rows,
            n_audio=2 * T_a,
            frames=4 * T_a,
            n_patches=0,
            height=0,
            width=0,
            out_height=0,
            out_width=0,
        )
        if T_v:
            shapes.update(vision.processor.shapes(T_v))
            sizes = dict(sized[T_v])
            values.update(n_patches=sizes.pop("n"), **sizes)
        calls += Call.admitted(graph.trace(**shapes), dev, values)
    tune.measure(args, calls, CALIBRATION_PAIRS, COSTS)


if __name__ == "__main__":
    main()
