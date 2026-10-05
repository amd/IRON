# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Building blocks for stream-dse-backed operators.

An operator supplies its reference layers and a placement; these modules turn
that into everything stream-dse needs:

* ``ops`` -- the registry binding an ONNX operator to its stream-dse kernel
  and its ``aie_kernels`` source.
* ``workload`` -- the layers as the ONNX workload stream-dse optimizes.
* ``mapping`` -- the mapping YAML, named from that same graph.

The submodules are not re-exported here: they need ``onnx``/``pyyaml`` (installed
with stream-dse, see ``requirements_stream.txt``), so importing an operator must not
pull them in. Import them directly from the module that builds the design.
"""
