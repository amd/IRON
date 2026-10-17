#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
from aie.utils.benchmark import run_iters
from ml_dtypes import bfloat16
from aie.utils.trace import TraceConfig
from aie.utils.verify import Tolerance, compare

from iron.common.tracing import dump_traces

# Optional dependency (requirements_stream.txt), absent from the default CI image.
pytest.importorskip(
    "stream", reason="stream-dse not installed (see requirements_stream.txt)"
)

# stream-dse emits `!aie.objectfifosubview`, removed in Xilinx/mlir-aie#3553.
pytest.skip(
    "stream-dse codegen does not parse against the pinned mlir-aie",
    allow_module_level=True,
)

from iron.operators.swiglu_prefill_stream.op import SwiGLUPrefillStream  # noqa: E402
from iron.operators.swiglu_prefill_stream.reference import (  # noqa: E402
    INPUT,
    OUTPUT,
    WEIGHTS,
    generate_golden_reference,
)

# The MILP-feasible shape on the whole-array Strix (npu2) target.
SEQ_LEN, EMBEDDING_DIM, HIDDEN_DIM = 256, 512, 2048

FUSION_GROUPS = [1, 2, 5]

TIMED_RUNS = 3
TRACE_SIZE = 8192


@pytest.mark.supported_devices("npu2")
@pytest.mark.bench
@pytest.mark.parametrize("k", FUSION_GROUPS)
def test_swiglu_prefill_stream(k, tmp_path, record_property):
    trace = TraceConfig(TRACE_SIZE, trace_file=str(tmp_path / f"k{k}.txt"))
    golden_ref = generate_golden_reference(M=SEQ_LEN, K=EMBEDDING_DIM, N=HIDDEN_DIM)
    graph = SwiGLUPrefillStream(
        seq_len=SEQ_LEN,
        embedding_dim=EMBEDDING_DIM,
        hidden_dim=HIDDEN_DIM,
        k=k,
        trace=trace,
    )
    inputs = [golden_ref[name].astype(bfloat16) for name in (INPUT, *WEIGHTS)]
    net = graph.compile(
        **{
            name: (t.shape, bfloat16)
            for name, t in zip((INPUT, *WEIGHTS), inputs, strict=True)
        }
    )

    # All in bf16: ~20% of elements drift past 8% through the chain and down sum.
    out = net(*inputs)
    dump_traces(net.callable, trace.trace_file)
    output = out.numpy()[: SEQ_LEN * EMBEDDING_DIM].reshape((SEQ_LEN, EMBEDDING_DIM))
    verdict = compare(
        output,
        golden_ref[OUTPUT],
        Tolerance.relative(0.08, 0.7, max_mismatch_frac=0.25),
    )
    assert verdict, verdict.detail

    # The first dispatch pays for the hardware context; time the ones after it.
    latency = run_iters(net.callable, iters=TIMED_RUNS).e2e
    elapsed_us = latency.min_us
    total_bytes = 4 * SEQ_LEN * EMBEDDING_DIM  # bf16 in + out
    print(
        f"Latency min/mean/max (us): {elapsed_us:.2f} / "
        f"{latency.avg_us:.2f} / {latency.max_us:.2f}"
    )
    record_property("Latency", elapsed_us)
    record_property("Bandwidth", total_bytes / (elapsed_us * 1e-6) / 1e9)
    ops = sum(step.op.resolved().ops() for step in net.traced.steps)
    record_property("Throughput", ops / (elapsed_us * 1e-6) / 1e9)
