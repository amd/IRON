# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whole models built on IRON's operators, one package each, over what
every language model shares (:mod:`.common`).

:mod:`.common` is the decoder as one graph (``CausalLM``: prefill and
decode, the caches, attention and ``logits(tokens)``), the checkpoint and
the weight tree, sampling, the accuracy and determinism checks, the
command line and the device tests' checks. An application is what is its
model's alone: its ``layer`` and ``head``, its config, where its checkpoint
keeps each weight, its tokenizer, its CPU reference and its profiles.
Nothing in the library imports an application, so one can be replaced or
deleted on its own.
"""
