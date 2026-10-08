# Performance trends

**Operators dropped:** `flm/gemm`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `gemv` | `M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Bandwidth` | 8.24 | 11.56 | 🟢 +40.30% |
| `gemv` | `M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency` | 4115.02 | 2945.32 | 🟢 -28.43% |
| `gemv` | `M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Throughput` | 8.24 | 11.56 | 🟢 +40.30% |

