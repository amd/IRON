# Performance trends

**Operators dropped:** `flm/gemm`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `strided_copy` | `bench_flat_4mi` | `Bandwidth` | 5.96 | 12.32 | 🟢 +106.61% |
| `strided_copy` | `bench_flat_4mi` | `Latency` | 2955.90 | 1394.60 | 🟢 -52.82% |

