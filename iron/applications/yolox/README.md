<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# YOLOX-Nano on the NPU

Megvii's YOLOX-Nano object detector as one IRON graph, `YOLOXNano`, from a
416x416 image to its three scales' predictions, and the float32 numpy
forward pass it is checked against, `YOLOXNanoOracle`. Both read the
release's own PyTorch checkpoint by its own names (`Checkpoint` reads it
without torch); nothing here needs torch.

What is YOLOX's own is in `iron/applications/yolox/model.py`: the oracle;
the image preprocessing (upstream's letterbox to 416, padded with 114, BGR)
and the box decode, both on the host; and the graph, built from
`iron.lm`'s `Conv2d`, `MaxPool2d`, `ConcatChannels` and `project`:

- every `BaseConv`'s BatchNorm folds into its weight and bias once, as
  `iron.lm.Derived` (its epsilon is 1e-3, which upstream's
  `exp.get_model()` sets, not `nn.BatchNorm2d`'s default);
- a 1x1 conv is a projection of its pixels (`Pointwise`), copied first into
  a held map of whole 256-row blocks where its pixel count is not one; a
  3x3 conv is `Conv2d` (`Spatial`): depthwise between two held zero rows,
  or, the stem, dense inside a held zero border;
- the image's rows carry a fourth, zero channel, and the stem's weight a
  zero input channel to match, so each corner the stem gathers is whole
  4-byte units; the box, objectness and class predictions are zero-padded
  to 16, 32 and 96 channels, which the caller drops
  (`YOLOXNano.predictions`).

Its tunables are `profiles/<device>.json`: the narrow projections' flm.ProjectionGEMM
`tile_n`, and the stem's GEMM `tile_k`.

## Weights

[`yolox_nano.pth`](https://github.com/Megvii-BaseDetection/YOLOX/releases/download/0.1.1rc0/yolox_nano.pth)
from the 0.1.1rc0 release (Apache-2.0). The tests look for it in
`$IRON_EXAMPLE_WEIGHTS_DIR/yolox-nano/` (`/srv` by default); they fetch
two COCO val2017 photos into IRON's cache.

## Testing

```bash
pytest tests/applications/yolox/
```

The oracle finds the photos' cats and stop sign; the graph's own
reference, device-free, and the graph on the NPU, detect as the oracle
does at every anchor it scores at least 0.25.
