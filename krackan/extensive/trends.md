# Performance trends

**Operators added:** `flm/layer`

**Operators dropped:** `swiglu_prefill_stream`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `swiglu_decode` | `embedding_dim_1024-hidden_dim_3584` | `Bandwidth` | 0.00 | 0.00 | 🟢 +6.06% |

