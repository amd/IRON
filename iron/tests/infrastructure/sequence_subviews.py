# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Host-only coverage of the shared upstream tensor subview path."""

from types import SimpleNamespace

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.common.sequence import SequenceReferenceCallable


@pytest.fixture
def run():
    op = SimpleNamespace(
        subbuffer_layout={"packed": ("output", 0, 1024)},
        slice_info={
            "first": ("packed", 0, 512),
            "second": ("packed", 512, 1024),
        },
    )
    return SequenceReferenceCallable(op)


@pytest.mark.parametrize("name, start", [("first", 0), ("second", 256)])
def test_slices_alias_the_parent_and_are_cached(run, name, start):
    parent = run.get_buffer("packed")
    parent.fill_(0)
    view = run.get_buffer(name)

    assert view is run.get_buffer(name)
    assert view is run._resolve_buffer(name)
    assert view.dtype == np.dtype(bfloat16)
    assert view.shape == (256,)
    assert np.shares_memory(view.data, parent.data)

    view.fill_(3)
    expected = np.zeros(512, dtype=bfloat16)
    expected[start : start + 256] = 3
    np.testing.assert_array_equal(parent.numpy(), expected)

    parent.fill_(7)
    np.testing.assert_array_equal(view.numpy(), np.full(256, 7, dtype=bfloat16))


def test_unknown_buffer_is_rejected(run):
    with pytest.raises(ValueError, match="Unknown buffer"):
        run.get_buffer("missing")


def test_out_of_bounds_slice_is_rejected_by_upstream(run):
    run.op.slice_info["invalid"] = ("packed", 512, 1536)
    with pytest.raises(ValueError):
        run.get_buffer("invalid")


def test_input_slices_resolve_during_reference_dispatch(run, monkeypatch):
    run.op.input_args = ["packed"]
    parent = run.get_buffer("packed")

    def evaluate():
        assert parent.device == "cpu"
        for name in ("first", "second"):
            view = run._resolve_buffer(name)
            assert view.device == "cpu"
            np.testing.assert_array_equal(view.numpy(), parent.numpy()[:256])

    monkeypatch.setattr(run, "_run", evaluate)
    for value in (3, 7):
        parent.fill_(value)
        run()
