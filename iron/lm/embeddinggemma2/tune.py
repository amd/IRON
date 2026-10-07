# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure EmbeddingGemma 2's cost table on this NPU (``probe.measure_graph``):
every design of each version, at each width, and the configure cost
between a few pairs of them. Run with XRT sourced and the NPU otherwise idle:

```bash
python -m iron.lm.embeddinggemma2.tune /path/to/embeddinggemma-2
```
"""

import argparse
from pathlib import Path

from iron.common.graph.narrowing import CostTable
from iron.common.graph.probe import Call, Timing, measure_graph, pmode

from iron.lm import Checkpoint, load_weights

from .encoder import COSTS
from .model import EMBEDDINGGEMMA_2, EmbeddingGemma, layout, text_tensors

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
        help="measure designs and calibrations already in the table or the "
        "cost cache again",
    )
    args = ap.parse_args()

    print(f"power mode: {pmode()}")
    c = EMBEDDINGGEMMA_2
    tensors = text_tensors(Checkpoint(args.directory / "model.safetensors").tensors)
    weights = load_weights(tensors, layout(c), c.n_layers)
    graph = EmbeddingGemma(c, weights, c.sliding_window)
    # Each version at its every row real: the masked Softmax's longest span.
    calls = [Call(graph.trace(**s), dict(n=s["x"][0])) for s in graph.shapes()]
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
