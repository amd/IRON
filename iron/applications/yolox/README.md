<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# YOLOX-Nano on the NPU

Megvii's YOLOX-Nano object detector as one IRON graph, `YOLOXNano`, from a
416x416 image to its three scales' predictions, and the float32 numpy
forward pass it is checked against, `YOLOXNanoOracle`; `model.py`'s
docstrings describe both. Both read the release's own PyTorch checkpoint by
its own names (`iron.lm.Checkpoint` reads it without torch).

The graph is built from `iron.lm`'s `Conv2d`, `MaxPool2d` and
`ConcatChannels`, and `F.linear` for each 1x1 conv (`Pointwise`). Its tunables are `profiles/<device>.json`: the narrow
projections' `flm.ProjectionGEMM` `tile_n`, and the stem's GEMM `tile_k`.

## Weights

[`yolox_nano.pth`](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_nano.pth)
from the 0.1.1rc0 release (Apache-2.0). The tests also fetch two COCO
val2017 photos into IRON's cache.

## Testing

```bash
pytest tests/applications/yolox/
```

The oracle finds the photos' cats and stop sign; the graph's own
reference, device-free, and the graph on the NPU, detect as the oracle
does at every anchor it scores at least 0.25.
