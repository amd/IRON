#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Carried values, on a device, through the host.

A graph with ``Carried`` values returns their next values from each call:
an expression of the current ones is evaluated on the host, and an element
the graph computed is read back from its output buffer. The next call takes
them as its values. The graph here has no tensor input at all and walks a
linked list: each call gathers the current node's successor on the device.
A walk that went wrong anywhere (the offset, the int32 gather, the readback)
leaves the permutation's cycle and is caught at the step it happens.
"""

import numpy as np
import pytest

import iron
from iron.common import Carried
from iron.operators.copy import Copy

N = 64


class Walk(iron.Graph):
    def __init__(self, successor):
        self.successor = iron.weight(successor)

    def body(self, *, node: Carried[np.int32], steps: Carried[np.int32]):
        nxt = Copy(self.successor[node], dtype=np.int32)
        return iron.carry(node=nxt, steps=steps + 1)


@pytest.mark.supported_devices("npu2")
def test_a_graph_walks_a_linked_list_through_its_carried_values(npu_runtime):
    successor = np.random.default_rng(0).permutation(N).astype(np.int32)
    walk = Walk(successor)
    net = walk.compile()
    assert net.plan.image == "elf", "only the full ELF carries a scratchpad"

    node, steps = 0, 0
    for step in range(2 * N):
        nxt = walk(node=node, steps=steps)
        assert dict(nxt) == {"node": successor[node], "steps": steps + 1}, step
        node, steps = nxt["node"], nxt["steps"]
