# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure EmbeddingGemma 2's vision cost table on this NPU
(``probe.measure_graph``): every design of each version, at each width, and
the configure cost between a pair of them. Run with XRT sourced and the NPU
otherwise idle:

```bash
python -m iron.lm.embeddinggemma2.vision.tune /path/to/embeddinggemma-2
```
"""

import argparse
from pathlib import Path

from iron.common.graph.narrowing import CostTable
from iron.common.graph.probe import Call, Timing, measure_graph, pmode
from iron.lm import Checkpoint, load_weights

from ..model import COSTS
from .model import VISION, Vision, layout, vision_tensors

CALIBRATION_PAIRS = [("ElementwiseAdd", "GELU"), ("GELU", "ElementwiseMul")]


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
    tensors = vision_tensors(Checkpoint(args.directory / "model.safetensors").tensors)
    graph = Vision(VISION, load_weights(tensors, layout(VISION), VISION.n_layers))
    # Each version at its every row real: the masked Softmax's longest span.
    calls = [Call(graph.trace(**s), dict(n=s["pixels"][0])) for s in graph.shapes()]
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
