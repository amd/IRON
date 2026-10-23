# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Dataflow pieces the FastFlowLM-derived designs share."""

from aie.iron import Acquire, Bd, Release


def ping_pong(b0, b1, acq, rel, acq_val=1, rel_val=1, **bd_args):
    """Two BDs that alternate between b0 and b1 behind one lock pair."""
    return [
        Bd(
            b,
            acquires=[Acquire(acq, value=acq_val)],
            releases=[Release(rel, value=rel_val)],
            next=nxt,
            **bd_args,
        )
        for b, nxt in ((b0, 1), (b1, 0))
    ]
