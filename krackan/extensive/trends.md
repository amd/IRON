# Performance trends

**Operators dropped:** `swiglu_prefill_stream`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `mha` | `seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0` | `Bandwidth` | 0.16 | 0.47 | 🟢 +191.69% |
| `mha` | `seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0` | `Latency` | 52612.66 | 18100.46 | 🟢 -65.60% |
| `mha` | `seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2` | `Bandwidth` | 0.10 | 0.27 | 🟢 +163.92% |
| `mha` | `seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2` | `Latency` | 415504.66 | 157433.92 | 🟢 -62.11% |
| `rms_norm` | `input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 36.43 | 46.73 | 🟢 +28.25% |
| `rms_norm` | `input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 924.88 | 720.58 | 🟢 -22.09% |
| `silu` | `input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096` | `Bandwidth` | 37.52 | 50.73 | 🟢 +35.22% |
| `silu` | `input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096` | `Latency` | 895.06 | 665.40 | 🟢 -25.66% |
| `softmax` | `input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512` | `Bandwidth` | 12.51 | 15.98 | 🟢 +27.74% |
| `softmax` | `input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512` | `Latency` | 671.62 | 527.28 | 🟢 -21.49% |
| `transpose` | `M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1` | `Bandwidth` | 9.45 | 18.33 | 🟢 +94.02% |
| `transpose` | `M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1` | `Latency` | 1810.94 | 918.60 | 🟢 -49.27% |

