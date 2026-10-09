# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure EmbeddingGemma 2's cost table on this NPU (``probe.measure_graph``):
every design of each version of the text encoder, both towers and the
multimodal graph, at each width, and the configure cost between a few pairs
of them. One run measures them all, since the table drops the designs its
run's graphs do not have.
Run with XRT sourced and the NPU otherwise idle:

```bash
python -m iron.lm.embeddinggemma2.tune /path/to/embeddinggemma-2
```
"""

import argparse
import itertools
from pathlib import Path

import numpy as np

from iron.common.graph.narrowing import CostTable
from iron.common.graph.probe import Call, Timing, measure_graph, pmode

from iron.lm import Checkpoint, load_weights

from .audio import model as audio_model
from .model import COSTS, EMBEDDINGGEMMA_2, EmbeddingGemma, layout, text_tensors
from .multimodal import Multimodal
from .vision import model as vision_model

CALIBRATION_PAIRS = [
    ("ElementwiseAdd", "ElementwiseMul"),
    ("ElementwiseAdd", "GELU"),
    ("GELU", "ElementwiseMul"),
]


def calls(directory: Path) -> list[Call]:
    """A call of each version of the text encoder, both towers and the
    multimodal graph a prompt can reach, every row real (the longest bound a
    call gives).

    Args:
        directory: The checkpoint directory.
    """
    c, A, V = EMBEDDINGGEMMA_2, audio_model.AUDIO, vision_model.VISION
    tensors = Checkpoint(directory / "model.safetensors").tensors
    weights = load_weights(text_tensors(tensors), layout(c), c.n_layers)
    text = EmbeddingGemma(c, weights)
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
    # Each vision version at the largest image it takes, its patches filled.
    sized = {
        T: vision.vision.processor.inputs(
            np.zeros((*image, 3), np.uint8), T // V.pool**2
        )[1]
        for T, image in zip(vision.vision.rows, vision_model.LARGEST, strict=True)
    }
    out = [
        *(Call(text.trace(**s), dict(n=s["ids"][0][0])) for s in text.shapes()),
        *(
            Call(vision.trace(**s), sized[T])
            for T, s in zip(vision.vision.rows, vision.shapes())
        ),
    ]
    for s in audio.shapes():
        frames = s["x"][0][0] // A.hop - 1
        out.append(Call(audio.trace(**s), dict(n=frames // 2, frames=frames)))

    graph = Multimodal(c, weights, text.max_tokens, audio.audio, vision.vision)
    # A tower version's fewest soft tokens: one past the version before it.
    fewest_audio = dict(zip(audio.audio.rows, (1, *(T + 1 for T in audio.audio.rows))))
    fewest_image = dict(
        zip(vision.vision.rows, (1, *(T // V.pool**2 + 1 for T in vision.vision.rows)))
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
            shapes.update(vision.vision.processor.shapes(T_v))
            sizes = dict(sized[T_v])
            values.update(n_patches=sizes.pop("n"), **sizes)
        out.append(Call(graph.trace(**shapes), values))
    return out


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
    measure_graph(
        CostTable(args.table),
        calls(args.directory),
        CALIBRATION_PAIRS,
        Timing(args.rounds, args.calls),
        args.repeats,
        args.remeasure,
    )


if __name__ == "__main__":
    main()
