# Performance trends

**Operators dropped:** `swiglu_prefill_stream`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `gemv` | `M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Bandwidth` | 43.82 | 40.75 | 🔴 -7.00% |
| `gemv` | `M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency` | 766.76 | 824.56 | 🔴 +7.54% |
| `gemv` | `M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Throughput` | 43.79 | 40.73 | 🔴 -7.00% |

