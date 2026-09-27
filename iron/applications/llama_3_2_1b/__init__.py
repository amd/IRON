# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 1B end to end, in numpy and on the NPU; no torch.

* :mod:`~iron.applications.llama_3_2_1b.npu` -- prefill and decode as one
  graph (:class:`~.npu.Llama3_2_1b`), called through its ``logits``.
* :mod:`~iron.applications.llama_3_2_1b.cpu` -- the float32 forward pass
  the NPU is judged against (:class:`~.cpu.Reference`).
* :mod:`~iron.applications.llama_3_2_1b.runner` -- the config, the
  checkpoint and the weights, the tokenizer, sampling, the generation loop,
  the accuracy and determinism checks, :class:`~.runner.Runner`, which
  builds either model, and the command line.

Run it with ``python -m iron.applications.llama_3_2_1b.runner``; the
accuracy check with ``--check-accuracy``.
"""
