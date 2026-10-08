# Performance trends

**Operators dropped:** `swiglu_prefill_stream`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `rope` | `rows_4096-cols_512-angle_rows_8-aie_columns_8-method_type_0` | `Latency` | 297.36 | 334.50 | 🔴 +12.49% |

