# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Building blocks for stream-dse-backed operators.

An operator supplies a reference ``nn.Module`` and a placement; these modules turn
that into everything stream-dse needs:

* :mod:`~iron.common.stream.kernels` -- the AIE kernels and operand layouts a design
  runs. Free of ``onnx``, so an operator may name its kernels at import time.
* :mod:`~iron.common.stream.ops` -- the registry binding a torch ATen op to its ONNX
  form and to one of those kernels.
* :mod:`~iron.common.stream.workload` -- ``torch.export`` of the module into the ONNX
  workload stream-dse optimizes.
* :mod:`~iron.common.stream.mapping` -- the mapping YAML, named from that same graph.

The submodules are not re-exported here: they need ``onnx``/``pyyaml`` (installed
with stream-dse, see ``requirements_stream.txt``), so importing an operator must not
pull them in. Import them directly from the module that builds the design.
"""
