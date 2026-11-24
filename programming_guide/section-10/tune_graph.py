# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Section-10 example: tuning a toy graph's profile with ``iron.tune.cli.tune``.

``MiniMLP`` is SwiGLU's shape (Section 9) at a size small enough to tune in a
couple of minutes: two GEMVs, SiLU and a multiply. ``record`` is the same
kind of callable a model's own tune (``iron.lm.tune``) passes for a
decoder's calls; ``main`` passes it to ``iron.tune.cli.tune`` directly, so
it searches ``MiniMLP``'s tunables, prices the packings and fusions its
steps admit, and writes a profile and a report the same way.
"""

import tempfile
from pathlib import Path

import numpy as np
from aie.utils.verify import compare
from ml_dtypes import bfloat16

import iron
from iron.common.declare import Profile
from iron.operators import GEMV, SiLU
from iron.tune import cli as tune_cli
from iron.tune.autotune import Timed

HIDDEN, INTERMEDIATE = 64, 256


class MiniMLP(iron.Graph):
    """``silu(w_gate @ x) * (w_up @ x)``, SwiGLU's shape (Section 9) sized to tune quickly."""

    def __init__(self, w_gate, w_up):
        self.w_gate, self.w_up = iron.param(w_gate), iron.param(w_up)

    def body(self, x):
        gate = GEMV.step(self.w_gate, x)
        up = GEMV.step(self.w_up, x)
        return SiLU.step(gate) * up


def weights(seed: int = 0) -> tuple[np.ndarray, np.ndarray]:
    """Return ``MiniMLP``'s two weights, drawn at ``seed``."""
    rng = np.random.default_rng(seed)
    scale = 1 / np.sqrt(HIDDEN)
    shape = (INTERMEDIATE, HIDDEN)
    w_gate = (rng.standard_normal(shape) * scale).astype(bfloat16)
    w_up = (rng.standard_normal(shape) * scale).astype(bfloat16)
    return w_gate, w_up


def record(profile: Profile) -> list[Timed]:
    """Return ``MiniMLP``'s one call, recorded under ``profile``.

    The same shape of callable a model's ``tune_calls`` returns: what
    ``iron.tune.cli.tune`` times, prices and checks.
    """
    w_gate, w_up = weights()
    graph = MiniMLP(w_gate, w_up)
    graph.profile = profile
    return [Timed(graph.record(x=(HIDDEN,)))]


def main(argv=None):
    parser = tune_cli.parser("Section 10: tuning a toy graph")
    parser.add_argument(
        "--profiles",
        type=Path,
        default=None,
        help="the directory whose <device>.json this writes and its report "
        "beside it (default: a temporary one, removed once checked)",
    )
    args = parser.parse_args(argv)

    cleanup = None
    profiles = args.profiles
    if profiles is None:
        cleanup = tempfile.TemporaryDirectory()
        profiles = Path(cleanup.name)
    path = tune_cli.tune(args, record, profiles)
    tuned = Profile.load(path)
    print((path.with_suffix(".report.txt")).read_text())
    if cleanup is not None:
        cleanup.cleanup()

    w_gate, w_up = weights()
    graph = MiniMLP(w_gate, w_up)
    graph.profile = tuned
    x = np.random.default_rng(1).standard_normal(HIDDEN).astype(bfloat16)
    reference = graph.reference(x)
    graph.compile(x=(HIDDEN,))
    result = np.asarray(graph(x))
    op = graph.record(x=(HIDDEN,)).steps[0].op
    verdict = compare(result, reference, op.resolved().tolerance())
    print(f"tuned profile vs. graph.reference(): {verdict.detail}")
    assert verdict, verdict.detail
    print("PASS!")


if __name__ == "__main__":
    main()
