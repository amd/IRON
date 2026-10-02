# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `sigmoid` | `input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 15.94 | 8.59 | 🔴 -46.12% |
| `sigmoid` | `input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2169.24 | 3912.88 | 🔴 +80.38% |

