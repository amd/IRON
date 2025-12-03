<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# RoPE Example for Ryzen NPU

This repository contains an example implementation of the **RoPE (Rotary Position Embedding)** algorithm for the **Ryzen Neural Processing Unit (NPU)**. The implementation utilizes the [RoPE](./aie_kernels/aie2p/rope.cc) kernel to demonstrate the capabilities of the NPU in handling advanced embedding techniques.

## Notes
The RoPE kernel offers two methods for applying embedding: a two-halves method (default) and an interleaved method. The two-halves method is what's used in Hugging Face's `transformer` library, while the interleaved method is used in Meta's official repo. Using the two-halves method is necessary when using Llama weights from Hugging Face, as the parameters of some layers are re-permuted while converting the Llama weights to Hugging Face. See [Issue #25199](https://github.com/huggingface/transformers/issues/25199) for reference.