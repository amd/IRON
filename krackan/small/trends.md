# Performance trends

**Operators dropped:** `swiglu_prefill_stream`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `layer_norm` | `input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Bandwidth` | 46.22 | 51.17 | 🟢 +10.72% |
| `layer_norm` | `input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency` | 726.70 | 655.98 | 🟢 -9.73% |

