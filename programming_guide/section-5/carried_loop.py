# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Section-5 example: carried values, called from the host and looped on
the device.

``Walk`` walks a linked list one node per call: the next node is gathered
from a successor table the graph holds, and recorded in ``trail`` at the
step count. Both ``node`` and ``steps`` are carried: the host seeds the
first call, and every later call starts from what the previous one carried.
"""

import argparse

import numpy as np

import iron
from iron import Carried
from iron.operators.copy import Copy

N = 64


class Walk(iron.Graph):
    """One step of a linked list walk: the next node gathered from
    ``successor`` and recorded in ``trail`` at the step count, the step
    count one more than the last."""

    def __init__(self, successor, steps: int):
        self.successor = iron.weight(successor)
        self.trail = iron.state((steps,), np.int32, name="trail")

    def body(self, *, node: Carried[np.int32], steps: Carried[np.int32]):
        nxt = Copy.step(self.successor[node], dtype=np.int32)
        Copy.step(nxt, self.trail[steps], dtype=np.int32)
        return iron.carry(node=nxt, steps=steps + 1)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Section 5: carried loops")
    parser.add_argument("--steps", type=int, default=3 * N)
    args = parser.parse_args(argv)

    rng = np.random.default_rng(0)
    successor = rng.permutation(N).astype(np.int32)
    start = int(rng.integers(N))

    # The device loop's `first` call is itself a step, so it makes steps + 1.
    trail = [start]
    for _ in range(args.steps + 1):
        trail.append(int(successor[trail[-1]]))

    walk = Walk(successor, args.steps + 1)
    node, steps = start, 0
    for expected in trail[1 : args.steps + 1]:
        nxt = walk.reference(node=node, steps=steps)
        node, steps = int(nxt["node"]), int(nxt["steps"])
        assert node == expected, (node, expected)
    print(f"host-driven walk: {args.steps} steps match the numpy reference")

    body = walk.compile()
    loop = iron.CarriedLoop(body, body, depth=2)
    got = list(loop.run(args.steps, node=start, steps=0))
    assert got == list(range(args.steps))

    recorded = body.read(walk.trail)
    expected = np.array(trail[1:], dtype=np.int32)
    assert np.array_equal(recorded, expected), (recorded, expected)
    print(f"device loop: ran {args.steps} steps, {loop.depth} in flight")
    print("PASS!")


if __name__ == "__main__":
    main()
