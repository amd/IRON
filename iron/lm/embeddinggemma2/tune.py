# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure EmbeddingGemma 2's cost table on this NPU (``probe.measure_graph``):
every design of each version, at each width, and the configure cost
between a few pairs of them. A design's time follows its shapes, not the
weights, so no checkpoint is read. Run with XRT sourced and the NPU
otherwise idle:

```bash
python -m iron.lm.embeddinggemma2.tune
```
"""

import argparse
from pathlib import Path

from iron.common.graph.narrowing import CostTable
from iron.common.graph.probe import Call, Timing, measure_graph, pmode

from iron.lm import unread_weights

from .encoder import COSTS
from .model import EMBEDDINGGEMMA_2, EmbeddingGemma, layout

CALIBRATION_PAIRS = [
    ("ElementwiseAdd", "ElementwiseMul"),
    ("ElementwiseAdd", "GELU"),
    ("GELU", "ElementwiseMul"),
]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
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
    graph = EmbeddingGemma(c, unread_weights(layout(c), c.n_layers), c.sliding_window)
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
