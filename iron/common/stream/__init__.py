# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Building blocks for stream-dse-backed operators.

An operator supplies a reference ``nn.Module`` and a placement; these modules turn
that into everything stream-dse needs:

* :mod:`~iron.common.stream.ops` -- the registry binding a torch ATen op to its ONNX
  form, its stream-dse kernel and IRON's ``aie_kernels`` source.
* :mod:`~iron.common.stream.workload` -- ``torch.export`` of the module into the ONNX
  workload stream-dse optimizes.
* :mod:`~iron.common.stream.mapping` -- the mapping YAML, named from that same graph.

The submodules are not re-exported here: they need ``onnx``/``pyyaml`` (installed
with stream-dse, see ``requirements_stream.txt``), so importing an operator must not
pull them in. Import them directly from the module that builds the design.
"""
