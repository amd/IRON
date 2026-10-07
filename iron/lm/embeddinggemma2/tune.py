# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure EmbeddingGemma 2's cost table on this NPU (``probe.measure_graph``):
every design of each version of the text encoder and both towers, at each
width, and the configure cost between a few pairs of them. One run measures
them all, since the table drops the designs its run's graphs do not have.
Run with XRT sourced and the NPU otherwise idle:

```bash
python -m iron.lm.embeddinggemma2.tune /path/to/embeddinggemma-2
```
"""

import argparse
from pathlib import Path

from iron.common.graph.narrowing import CostTable
from iron.common.graph.probe import Call, Timing, measure_graph, pmode

from iron.lm import Checkpoint, load_weights

from .audio import model as audio_model
from .model import COSTS, EMBEDDINGGEMMA_2, EmbeddingGemma, layout, text_tensors
from .vision import model as vision_model

CALIBRATION_PAIRS = [
    ("ElementwiseAdd", "ElementwiseMul"),
    ("ElementwiseAdd", "GELU"),
    ("GELU", "ElementwiseMul"),
]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("directory", type=Path, help="the checkpoint directory")
    ap.add_argument(
        "--table",
        type=Path,
        default=COSTS,
        help=f"the table to fill (default: {COSTS})",
    )
    ap.add_argument("--rounds", type=int, default=8)
    ap.add_argument("--calls", type=int, default=50)
    ap.add_argument(
        "--repeats",
        type=int,
        default=9,
        help="steps per long run; a step's time is the long run's excess over "
        "a run of one, per extra step (default: 9)",
    )
    ap.add_argument(
        "--remeasure",
        action="store_true",
        help="measure designs and calibrations already in the table again",
    )
    args = ap.parse_args()

    print(f"power mode: {pmode()}")
    c, A, V = EMBEDDINGGEMMA_2, audio_model.AUDIO, vision_model.VISION
    tensors = Checkpoint(args.directory / "model.safetensors").tensors
    text = EmbeddingGemma(
        c, load_weights(text_tensors(tensors), layout(c), c.n_layers), c.sliding_window
    )
    vision = vision_model.Vision(
        V,
        load_weights(
            vision_model.vision_tensors(tensors), vision_model.layout(V), V.n_layers
        ),
    )
    audio = audio_model.Audio(
        A,
        load_weights(
            audio_model.audio_tensors(tensors), audio_model.layout(A), A.n_layers
        ),
    )
    # Each version at its every row real: the masked Softmax's longest span.
    calls = [
        *(Call(text.trace(**s), dict(n=s["ids"][0][0])) for s in text.shapes()),
        *(Call(vision.trace(**s), dict(n=s["pixels"][0])) for s in vision.shapes()),
    ]
    for s in audio.shapes():
        frames = s["x"][0][0] // A.hop - 1
        calls.append(Call(audio.trace(**s), dict(n=frames // 2, frames=frames)))
    measure_graph(
        CostTable(args.table),
        calls,
        CALIBRATION_PAIRS,
        Timing(args.rounds, args.calls),
        args.repeats,
        args.remeasure,
    )


if __name__ == "__main__":
    main()
