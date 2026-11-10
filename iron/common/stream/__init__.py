# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Operators whose design stream-dse generates.

An operator gives a reference ``torch.nn.Module`` and its fused groups; these
modules turn that into what stream-dse solves, and its designs into IRON's:

- ``ops``: each torch operator's ONNX form and stream-dse kernel.
- ``workload``: the module exported to the ONNX workload stream-dse solves.
- ``mapping``: the mapping YAML, named from that same graph.
- ``kernel_library``: IRON's kernel library, one TOML per architecture.
- ``runner``: the solve, its options and its cache.
- ``operator``: ``StreamOperator``, one fused group as an operator.

They need stream-dse, torch and onnxscript (``requirements_stream.txt``),
so nothing here is imported by ``iron.common``; an operator imports them
when it builds.
"""
