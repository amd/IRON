# Performance trends

**Operators added:** `merge_results`

**Operators dropped:** `pre_push_hook`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 5.90 µs | 3.47 µs | ⚪ -41.27% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 2.30 µs | 3.89 µs | ⚪ +68.89% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 4.38 µs | 7.17 µs | ⚪ +63.85% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.04 µs | 3.69 µs | ⚪ +254.06% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.34 µs | 10.65 µs | ⚪ +27.71% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.44 µs | 11.90 µs | ⚪ +386.70% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 5.02 µs | 4.71 µs | ⚪ -6.18% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 6.89 µs | 5.54 µs | ⚪ -19.57% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 8.10 µs | 4.10 µs | ⚪ -49.41% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 2.80 µs | 8.20 µs | ⚪ +193.42% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 10.41 µs | 14.71 µs | ⚪ +41.23% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 4.21 µs | 15.51 µs | ⚪ +268.53% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 7.20 µs | 2.81 µs | ⚪ -61.04% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 9.65 µs | 8.20 µs | ⚪ -15.00% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.81 µs | 8.50 µs | ⚪ +46.32% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 7.37 µs | 4.29 µs | ⚪ -41.74% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 185.60 µs | 2.98 µs | ⚪ -98.39% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 37.38 µs | 106.34 µs | ⚪ +184.49% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 5.99 µs | 4.98 µs | ⚪ -16.83% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.59 µs | 1.38 µs | ⚪ -13.21% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.08 µs | 1.55 µs | ⚪ +43.48% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 6.85 µs | 8.28 µs | ⚪ +20.77% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.97 µs | 2.50 µs | ⚪ +26.68% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 8.44 µs | 9.08 µs | ⚪ +7.66% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 31.85 µs | 16.69 µs | ⚪ -47.58% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 0.39 µs | 1.34 µs | ⚪ +247.67% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 4.98 µs | 6.72 µs | ⚪ +34.78% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.31 µs | 5.76 µs | ⚪ -21.24% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 5.48 µs | 1.43 µs | ⚪ -73.92% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 1.38 µs | 1.90 µs | ⚪ +37.77% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 7.86 µs | 9.00 µs | ⚪ +14.54% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.24 µs | 5.37 µs | ⚪ +65.69% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.30 µs | 2.06 µs | ⚪ +58.06% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.45 µs | 3.44 µs | ⚪ -22.82% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 5.43 µs | 13.49 µs | ⚪ +148.36% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Bandwidth` | 5.53 GB/s | -61.19 GB/s | 🔴 -1207.07% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency` | 1707.37 µs | -154.22 µs | 🟢 -109.03% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Throughput` | 1260.23 GOP/s | -13951.64 GOP/s | 🔴 -1207.07% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Bandwidth` | 4.47 GB/s | 4.78 GB/s | 🟢 +7.06% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency` | 1173.64 µs | 1096.28 µs | 🟢 -6.59% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Throughput` | 1829.77 GOP/s | 1958.89 GOP/s | 🟢 +7.06% |

