# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 3.47 µs | 2.00 µs | ⚪ -42.20% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 3.89 µs | 7.04 µs | ⚪ +80.99% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 7.17 µs | 2.30 µs | ⚪ -67.94% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 3.69 µs | 2.76 µs | ⚪ -25.14% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 10.65 µs | 3.07 µs | ⚪ -71.15% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 11.90 µs | 4.51 µs | ⚪ -62.11% |
| `Emit` | `npu2-Emit-eight_carried` | `Bandwidth` | 0.12 GB/s | 0.09 GB/s | 🔴 -21.17% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency` | 17.17 µs | 21.78 µs | 🔴 +26.85% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 4.71 µs | 1.79 µs | ⚪ -61.90% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.54 µs | 2.51 µs | ⚪ -54.62% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 12.75 GB/s | 8.88 GB/s | 🔴 -30.35% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 1974.50 µs | 2834.95 µs | 🔴 +43.58% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 4.10 µs | 16.04 µs | ⚪ +291.45% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 8700.86 GOP/s | 6060.03 GOP/s | 🔴 -30.35% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 8.20 µs | 6.28 µs | ⚪ -23.41% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 14.71 µs | 5.82 µs | ⚪ -60.45% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 15.51 µs | 4.28 µs | ⚪ -72.41% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 8.50 µs | 3.88 µs | ⚪ -54.36% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 4.29 µs | 10.84 µs | ⚪ +152.40% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.98 µs | 16.82 µs | ⚪ +464.40% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 106.34 µs | 11.34 µs | ⚪ -89.34% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 4.98 µs | 1.99 µs | ⚪ -59.95% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.38 µs | 7.12 µs | ⚪ +415.26% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.55 µs | 5.39 µs | ⚪ +246.89% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 8.28 µs | 5.31 µs | ⚪ -35.89% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.50 µs | 3.03 µs | ⚪ +21.24% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 9.08 µs | 7.47 µs | ⚪ -17.70% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 16.69 µs | 28.93 µs | ⚪ +73.26% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.34 µs | 2.06 µs | ⚪ +53.43% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 2.96 µs | 2.37 µs | ⚪ -19.98% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.72 µs | 7.48 µs | ⚪ +11.34% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.76 µs | 8.59 µs | ⚪ +49.14% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.43 µs | 1.76 µs | ⚪ +23.11% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 1.90 µs | 14.52 µs | ⚪ +664.97% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 9.00 µs | 6.09 µs | ⚪ -32.35% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 2.06 µs | 2.33 µs | ⚪ +12.89% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.44 µs | 8.15 µs | ⚪ +136.99% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Bandwidth` | -61.19 GB/s | 5.49 GB/s | 🔴 -108.97% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency` | -154.22 µs | 1718.52 µs | 🟢 -1214.30% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Throughput` | -13951.64 GOP/s | 1252.05 GOP/s | 🔴 -108.97% |

