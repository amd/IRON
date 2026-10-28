# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Section-7 example: a profile setting an operator's tunables by shape.

``Scaled`` never names ``AXPY``'s ``tile_size`` or ``num_aie_columns``
itself; a ``Profile`` assigned to the graph fills them in for every step
whose shape matches an entry, without a model's ``body`` repeating tunables
at every call site.
"""

import argparse

import numpy as np
from aie.utils.verify import compare
from ml_dtypes import bfloat16

import iron
from iron.operators import AXPY


class Scaled(iron.Graph):
    """``1.5 * x + y``: one ``AXPY`` step, its tunables left to the profile."""

    def body(self, x, y):
        return AXPY.step(x, y, scalar_factor=1.5)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Section 7: profiles and tunables")
    parser.add_argument("--size", type=int, default=2048)
    args = parser.parse_args(argv)

    profile = iron.Profile()
    # Matches any AXPY built at this size: tile_size and num_aie_columns,
    # not scalar_factor or size itself, which a call always gives.
    profile.add(AXPY, size=args.size, tile_size=1024, num_aie_columns=2)

    graph = Scaled()
    graph.profile = profile

    recording = graph.record(x=(args.size,), y=(args.size,))
    op = recording.steps[0].op
    print(
        f"from the profile: tile_size={op.tile_size}, num_aie_columns={op.num_aie_columns}"
    )
    assert (op.tile_size, op.num_aie_columns) == (1024, 2)

    rng = np.random.default_rng(0)
    x = rng.standard_normal(args.size).astype(bfloat16)
    y = rng.standard_normal(args.size).astype(bfloat16)
    reference = graph.reference(x, y)
    graph.compile(x=(args.size,), y=(args.size,))
    result = graph(x, y)
    verdict = compare(result, reference, op.resolved().tolerance())
    print(f"device call vs. graph.reference(): {verdict.detail}")
    assert verdict, verdict.detail
    print("PASS!")


if __name__ == "__main__":
    main()
