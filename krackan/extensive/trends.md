# Performance trends

**Operators added:** `flm/lm_head`

**Operators dropped:** `swiglu_prefill_stream`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `strided_copy` | `bench_flat_4mi` | `Bandwidth` | 32.18 | 36.76 | 🟢 +14.23% |
| `strided_copy` | `bench_flat_4mi` | `Latency` | 522.38 | 456.44 | 🟢 -12.62% |

