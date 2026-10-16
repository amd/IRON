# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `layer_norm` | `input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 8.83 | 21.56 | 🟢 +144.26% |
| `layer_norm` | `input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3830.00 | 1677.82 | 🟢 -56.19% |

