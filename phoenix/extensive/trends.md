# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 943.03 µs | 594.22 µs | ⚪ -36.99% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 7.56 µs | 9.09 µs | ⚪ +20.27% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 223.37 µs | 93.17 µs | ⚪ -58.29% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 9.27 µs | 6.21 µs | ⚪ -32.97% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 600.01 µs | 478.90 µs | ⚪ -20.18% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 411.86 µs | 564.40 µs | ⚪ +37.04% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 6.99 µs | 8.15 µs | ⚪ +16.61% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 16.90 GB/s | 10.54 GB/s | 🔴 -37.67% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1985.02 µs | 3184.90 µs | 🔴 +60.45% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 193.08 µs | 280.91 µs | ⚪ +45.49% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 4.23 GOP/s | 2.63 GOP/s | 🔴 -37.67% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 619.31 µs | 711.76 µs | ⚪ +14.93% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 133.71 µs | 385.73 µs | ⚪ +188.49% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 114.98 µs | 156.62 µs | ⚪ +36.22% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Bandwidth` | 10.75 GB/s | 15.77 GB/s | 🟢 +46.69% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 505.72 µs | 13.92 µs | ⚪ -97.25% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Throughput` | 10.74 GOP/s | 15.76 GOP/s | 🟢 +46.69% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 27.65 GB/s | 9.81 GB/s | 🔴 -64.51% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 1214.38 µs | 3421.93 µs | 🔴 +181.78% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 60.16 µs | 227.91 µs | ⚪ +278.82% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 27.63 GOP/s | 9.81 GOP/s | 🔴 -64.51% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 8.04 µs | 22.16 µs | ⚪ +175.81% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1477.15 µs | 3301.26 µs | 🔴 +123.49% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 503.64 µs | 280.71 µs | ⚪ -44.26% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 21.00 GB/s | 6.81 GB/s | 🔴 -67.57% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 998.87 µs | 3079.64 µs | 🔴 +208.31% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 13.58 µs | 253.65 µs | ⚪ +1767.80% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 1.31 GOP/s | 0.43 GOP/s | 🔴 -67.57% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 185.04 µs | 385.59 µs | ⚪ +108.38% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 218.76 µs | 124.19 µs | ⚪ -43.23% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 62.17 µs | 165.39 µs | ⚪ +166.03% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 81.07 µs | 122.60 µs | ⚪ +51.23% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 25.80 µs | 6.47 µs | ⚪ -74.92% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 14.40 µs | 10.76 µs | ⚪ -25.26% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 10.22 GB/s | 28.07 GB/s | 🟢 +174.74% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3285.37 µs | 1195.83 µs | 🟢 -63.60% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 272.14 µs | 18.31 µs | ⚪ -93.27% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 10.21 GOP/s | 28.06 GOP/s | 🟢 +174.74% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.71 GB/s | 11.00 GB/s | 🔴 -62.97% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1129.32 µs | 3049.94 µs | 🔴 +170.07% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 14.05 µs | 535.72 µs | ⚪ +3713.90% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 29.71 GOP/s | 11.00 GOP/s | 🔴 -62.97% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 29.48 µs | 931.89 µs | ⚪ +3061.04% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 269.97 µs | 192.00 µs | ⚪ -28.88% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 50.11 µs | 47.28 µs | ⚪ -5.64% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 6.78 µs | 13.03 µs | ⚪ +92.08% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 824.00 µs | 540.15 µs | ⚪ -34.45% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 64.57 µs | 927.35 µs | ⚪ +1336.26% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 8.48 µs | 9.21 µs | ⚪ +8.63% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 555.94 µs | 256.55 µs | ⚪ -53.85% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 303.53 µs | 687.75 µs | ⚪ +126.59% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 316.92 µs | 850.33 µs | ⚪ +168.31% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 5.70 GB/s | 2.83 GB/s | 🔴 -50.45% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 1471.05 µs | 2969.01 µs | 🔴 +101.83% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 320.15 µs | 453.49 µs | ⚪ +41.65% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 1.43 GOP/s | 0.71 GOP/s | 🔴 -50.45% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.12 GB/s | 29.40 GB/s | 🟢 +164.43% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3017.76 µs | 1141.21 µs | 🟢 -62.18% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 731.00 µs | 11.50 µs | ⚪ -98.43% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.78 GOP/s | 7.35 GOP/s | 🟢 +164.43% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.27 GB/s | 0.49 GB/s | 🔴 -61.07% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1656.05 µs | 4254.09 µs | 🔴 +156.88% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 194.74 µs | 301.75 µs | ⚪ +54.95% |

