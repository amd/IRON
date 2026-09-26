# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 1B end to end.

The NPU application imports no torch:

* :mod:`~iron.applications.llama_3_2_1b.weights` -- the checkpoint mapped
  as numpy (:class:`~.weights.LlamaWeights`), the embedding gather, and the
  RoPE table both the NPU and the reference read.
* :mod:`~iron.applications.llama_3_2_1b.graphs` -- prefill and decode as
  graph functions over those weights; they trace on handles, so they
  compile against a device or against nothing.
* :mod:`~iron.applications.llama_3_2_1b.npu` -- both graphs as fused
  images, and the forward pass the host loop calls.
* :mod:`~iron.applications.llama_3_2_1b.sampling` -- temperature and top-k
  sampling in numpy.
* :mod:`~iron.applications.llama_3_2_1b.harness` -- the config, the
  tokenizer, the generation loop and the accuracy and determinism checks.

torch is the CPU reference only:

* :mod:`~iron.applications.llama_3_2_1b.model` -- the parameters as a
  module tree and the plain causal forward the graphs are checked against.
* :mod:`~iron.applications.llama_3_2_1b.reference` -- that forward behind
  the harness's forward-pass protocol, numpy in and out.
* :mod:`~iron.applications.llama_3_2_1b.accuracy` -- the NPU against it.

Run it with ``python -m iron.applications.llama_3_2_1b.npu``; the accuracy
check with ``python -m iron.applications.llama_3_2_1b.accuracy``.
"""
