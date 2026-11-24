# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A device run in a child process a hang cannot outlive."""

import multiprocessing

import aie.utils as aie_utils
import pytest


def _child(results, target, args) -> None:
    try:
        aie_utils.ensure_current_device()
        results.put((True, target(*args)))
    except Exception as e:  # the parent reports it
        results.put((False, repr(e)))


def bounded(seconds: int, target, *args):
    """Return ``target(*args)`` run in a spawned child, failing the test where it runs past ``seconds``.

    ``target`` is a module's own function, and its arguments and result pickle; an
    exception it raises fails the test with its ``repr``.
    """
    context = multiprocessing.get_context("spawn")
    results = context.Queue()
    child = context.Process(target=_child, args=(results, target, args))
    child.start()
    child.join(seconds)
    if child.is_alive():
        child.kill()
        pytest.fail(f"{target.__name__} did not finish in {seconds} s: a hang")
    ok, got = results.get(timeout=10)
    assert ok, got
    return got
