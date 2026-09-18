# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The operator test adapter keeps reporting NPU, not host, latency."""

from types import SimpleNamespace

import pytest

torch = pytest.importorskip("torch")

from aie.utils.hostruntime.tensor_class import CPUOnlyTensor
from iron.common.base import AIEOperatorBase, AIERuntimeArgSpec
from iron.common import test_utils


class _Operator(AIEOperatorBase):
    def __init__(self, results):
        self.results = iter(results)
        self.calls = 0

    def set_up_artifacts(self):
        pass

    def compile(self):
        return self

    def get_arg_spec(self):
        return [
            AIERuntimeArgSpec("in", (32,)),
            AIERuntimeArgSpec("out", (32,)),
        ]

    def get_callable(self):
        def run(source, target):
            self.calls += 1
            target[:] = source.numpy()
            return next(self.results)

        return run


@pytest.mark.parametrize("tuple_result", [False, True])
def test_run_test_uses_upstream_npu_timing(monkeypatch, tuple_result):
    monkeypatch.setattr(test_utils.aie_utils, "DEFAULT_TENSOR_CLASS", CPUOnlyTensor)
    results = [SimpleNamespace(npu_time=ns) for ns in (1000000, 2000, 4000)]
    if tuple_result:
        results = [(None, result) for result in results]
    op = _Operator(results)
    data = torch.ones(32, dtype=torch.bfloat16)

    errors, latency_us, bandwidth = test_utils.run_test(
        op, {"in": data}, {"out": data}, warmup_iters=1, timed_iters=2
    )

    assert op.calls == 3
    assert errors == {}
    assert latency_us == 3.0
    assert bandwidth == pytest.approx(128 / (3e-6) / 1e9)


def test_missing_npu_timing_is_rejected(monkeypatch):
    monkeypatch.setattr(test_utils.aie_utils, "DEFAULT_TENSOR_CLASS", CPUOnlyTensor)
    op = _Operator([None])
    data = torch.ones(32, dtype=torch.bfloat16)
    with pytest.raises(RuntimeError, match="NPU execution time"):
        test_utils.run_test(
            op, {"in": data}, {"out": data}, warmup_iters=0, timed_iters=1
        )
