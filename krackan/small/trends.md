# Performance trends

**Operators dropped:** `swiglu_prefill_stream`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `mha` | `seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0` | `Bandwidth` | 0.16 | 0.50 | 🟢 +210.46% |
| `mha` | `seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0` | `Latency` | 52553.44 | 17301.10 | 🟢 -67.08% |
| `silu` | `input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096` | `Bandwidth` | 35.94 | 49.07 | 🟢 +36.52% |
| `silu` | `input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096` | `Latency` | 935.20 | 688.80 | 🟢 -26.35% |
| `softmax` | `input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512` | `Bandwidth` | 12.57 | 16.00 | 🟢 +27.21% |
| `softmax` | `input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512` | `Latency` | 670.68 | 526.14 | 🟢 -21.55% |
| `transpose` | `M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1` | `Bandwidth` | 8.80 | 17.17 | 🟢 +95.13% |
| `transpose` | `M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1` | `Latency` | 1942.44 | 1031.18 | 🟢 -46.91% |

