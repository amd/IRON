# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3.2 1B end to end.

* :mod:`~iron.applications.llama_3_2_1b.model` -- the parameters as a module
  tree, so a checkpoint's ``state_dict`` loads into it and every weight has
  one name, plus the plain causal forward the graphs are checked against.
* :mod:`~iron.applications.llama_3_2_1b.graphs` -- prefill and decode as
  graph functions over that tree; they trace on handles, so they compile
  against a device or against nothing.
* :mod:`~iron.applications.llama_3_2_1b.npu` -- both graphs as one image,
  and the forward pass the host loop calls.
* :mod:`~iron.applications.llama_3_2_1b.harness` -- the checkpoint, the
  tokenizer and the generation loop.

Run it with ``python -m iron.applications.llama_3_2_1b.npu``.
"""
