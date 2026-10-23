<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# ResNet-50 on the NPU

ResNet-50, `ResNet` in `model.py`, an image classifier as one graph, whose
docstring says what it computes and how the stem and the pools map onto
the feature-map operators. The image is ImageNet-normalized before the
graph and laid out by `ResNet.inputs`.

Its device-free test is `tests/applications/resnet/reference/`, against
transformers' ResNet on drawn weights at ResNet-50's widths; its device
test, `tests/applications/resnet/test.py`, holds the NPU to the graph's
own reference on the released checkpoint.

## Weights

From Hugging Face
([`microsoft/resnet-50`](https://huggingface.co/microsoft/resnet-50),
Apache-2.0), in one directory: `config.json` and `model.safetensors`.
