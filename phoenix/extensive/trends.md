# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `elementwise_mul` | `input_length_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 5634.66 | 2493.32 | 🟢 -55.75% |
| `gelu` | `input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 4.42 | 8.75 | 🟢 +98.17% |
| `gelu` | `input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 7641.04 | 3853.48 | 🟢 -49.57% |
| `silu` | `input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096` | `Bandwidth` | 3.28 | 7.73 | 🟢 +135.36% |
| `silu` | `input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096` | `Latency` | 10228.58 | 4536.86 | 🟢 -55.65% |

