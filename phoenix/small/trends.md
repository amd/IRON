# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `gelu` | `input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 4.34 | 11.95 | 🟢 +175.71% |
| `gelu` | `input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 7789.86 | 2961.56 | 🟢 -61.98% |
| `silu` | `input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096` | `Bandwidth` | 3.17 | 7.79 | 🟢 +145.70% |
| `silu` | `input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096` | `Latency` | 10601.94 | 4413.88 | 🟢 -58.37% |

