# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Copy's device-free edges: a reference write into a strided view of an
intermediate, and a pattern a shim descriptor does not fit.

The descriptors Copy issues run on a device, against numpy: slot writes as
the catalog's Copy cases, channel splits in
``iron/tests/operators/test_copy_channels.py``, and per-call offsets,
gathers and bounded views in ``iron/tests/operators``' test_copy_offset.py,
test_copy_gather.py and test_copy_bounded_view.py.
"""

import numpy as np
import pytest
from aie.helpers.taplib import TensorAccessPattern
from ml_dtypes import bfloat16

import iron
from iron.operators.copy import Copy

pytestmark = pytest.mark.usefixtures("npu2")


# A (V, W) table a gather reads rows of.
V, W = 64, 32


@pytest.mark.parametrize(
    "index, match",
    [
        (np.array([[0, 1]]), "1-D integer array"),
        (np.array([0.0, 1.0]), "1-D integer array"),
        (np.array([], dtype=np.int64), "gathering"),
        (np.array([0, V]), "gathering"),
        (np.array([-V - 1]), "gathering"),
        ((np.array([0, 1]), slice(0, 4)), "whole of every axis"),
    ],
)
def test_a_gather_refuses_what_it_cannot_lower(index, match):
    class Bad(iron.Graph):
        def body(self, x):
            return Copy.step(Copy.step(x)[index])

    with pytest.raises(IndexError, match=match):
        Bad().record(x=(V, W))


class _IntoColumns(iron.Graph):
    """A weight copied into the leading columns of an intermediate, a
    strided view of it, the rest of its rows kept.
    """

    def __init__(self, columns):
        self.columns = iron.param(columns)

    def body(self, x):
        h = Copy.step(x)
        Copy.step(self.columns, h[:, : self.columns.shape[1]])
        return Copy.step(h)


def test_the_reference_writes_a_copy_into_a_strided_view_through_it():
    N, D = 16, 64
    columns = np.arange(N * D, dtype=np.float32).reshape(N, D).astype(bfloat16)
    x = -np.arange(N * 2 * D, dtype=np.float32).reshape(N, 2 * D).astype(bfloat16)
    got = np.asarray(_IntoColumns(columns).reference(x)).reshape(N, 2 * D)
    assert (got[:, :D] == columns).all()
    assert (got[:, D:] == x[:, D:]).all()


def test_a_padded_pattern_does_not_fit_a_shim_descriptor():
    E = 2048
    op = Copy(
        src=TensorAccessPattern.full((4, E))[0],
        input_buffer_size=4 * E,
        output_buffer_size=E,
    )
    tap = TensorAccessPattern.full((E,))
    assert op.x.fits(tap)
    assert not op.x.fits(tap.pad([(0, 8)]))
