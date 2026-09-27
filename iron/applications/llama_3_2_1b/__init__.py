# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 1B end to end, in numpy and on the NPU; no torch.

* :mod:`~iron.applications.llama_3_2_1b.weights` -- the checkpoint mapped
  as numpy (:class:`~.weights.LlamaWeights`).
* :mod:`~iron.applications.llama_3_2_1b.cpu` -- the float32 forward pass
  the NPU is judged against (:class:`~.cpu.Reference`).
* :mod:`~iron.applications.llama_3_2_1b.npu` -- prefill and decode as one
  graph function over those weights (:class:`~.npu.LlamaGraph`), and the
  forward pass that calls its images (:class:`~.npu.AIELlama`).
* :mod:`~iron.applications.llama_3_2_1b.runner` -- the config, the
  tokenizer, sampling, the generation loop, the accuracy and determinism
  checks, and the command line.

Run it with ``python -m iron.applications.llama_3_2_1b.runner``; the
accuracy check with ``--check-accuracy``.
"""
