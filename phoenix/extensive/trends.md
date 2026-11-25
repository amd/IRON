# Performance trends

**Operators added:** `lm_server`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 39.39 µs | 95.10 µs | ⚪ +141.43% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 303.40 µs | 1233.67 µs | ⚪ +306.62% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1518.07 µs | 3177.14 µs | 🔴 +109.29% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 619.74 µs | 221.64 µs | ⚪ -64.24% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 18.44 µs | 12.12 µs | ⚪ -34.29% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.18 GB/s | 16.27 GB/s | 🔴 -49.44% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1564.06 µs | 3093.44 µs | 🔴 +97.78% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 7.53 µs | 579.53 µs | ⚪ +7592.26% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.36 GOP/s | 2.71 GOP/s | 🔴 -49.44% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 469.24 µs | 634.58 µs | ⚪ +35.24% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 11.27 µs | 5.98 µs | ⚪ -46.95% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.94 GB/s | 18.08 GB/s | 🟢 +65.25% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3067.58 µs | 1856.30 µs | 🟢 -39.49% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 376.55 µs | 18.04 µs | ⚪ -95.21% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.73 GOP/s | 4.52 GOP/s | 🟢 +65.25% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 641.86 µs | 235.79 µs | ⚪ -63.26% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 53.74 µs | 257.33 µs | ⚪ +378.88% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 11.48 GB/s | 15.69 GB/s | 🟢 +36.61% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 2923.69 µs | 2140.20 µs | 🟢 -26.80% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 315.36 µs | 57.14 µs | ⚪ -81.88% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 11.48 GOP/s | 15.68 GOP/s | 🟢 +36.61% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 311.60 µs | 520.78 µs | ⚪ +67.13% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 3431.91 µs | 1863.53 µs | 🟢 -45.70% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 218.67 µs | 723.43 µs | ⚪ +230.83% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 273.42 µs | 388.28 µs | ⚪ +42.01% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 512.54 µs | 893.95 µs | ⚪ +74.41% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 404.61 µs | 200.88 µs | ⚪ -50.35% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 138.11 µs | 203.78 µs | ⚪ +47.56% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 114.47 µs | 49.87 µs | ⚪ -56.44% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 78.72 µs | 86.87 µs | ⚪ +10.35% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 161.05 µs | 173.00 µs | ⚪ +7.42% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 0.82 µs | 10.53 µs | ⚪ +1180.47% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 14.76 µs | 2.39 µs | ⚪ -83.81% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 430.25 µs | 1168.81 µs | ⚪ +171.66% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.98 GB/s | 10.41 GB/s | 🔴 -65.29% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1119.14 µs | 3224.48 µs | 🔴 +188.12% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 49.39 µs | 309.10 µs | ⚪ +525.80% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 29.98 GOP/s | 10.41 GOP/s | 🔴 -65.29% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.71 GB/s | 11.37 GB/s | 🔴 -61.73% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1129.50 µs | 2951.45 µs | 🔴 +161.31% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 17.39 µs | 300.55 µs | ⚪ +1627.97% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.43 GOP/s | 2.84 GOP/s | 🔴 -61.73% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 275.24 µs | 243.83 µs | ⚪ -11.41% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 225.36 µs | 72.29 µs | ⚪ -67.92% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 20.59 µs | 12.86 µs | ⚪ -37.56% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 359.44 µs | 403.92 µs | ⚪ +12.37% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 13.60 GB/s | 28.31 GB/s | 🟢 +108.11% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 948.22 µs | 32.44 µs | ⚪ -96.58% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 3.40 GOP/s | 7.08 GOP/s | 🟢 +108.11% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 16.36 µs | 33.79 µs | ⚪ +106.59% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Bandwidth` | 0.10 GB/s | 0.09 GB/s | 🔴 -6.77% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 117.52 µs | 317.57 µs | ⚪ +170.22% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Throughput` | 2.49 GOP/s | 2.32 GOP/s | 🔴 -6.77% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 10.00 GB/s | 18.03 GB/s | 🟢 +80.40% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3356.92 µs | 1860.81 µs | 🟢 -44.57% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 259.95 µs | 61.27 µs | ⚪ -76.43% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.50 GOP/s | 4.51 GOP/s | 🟢 +80.40% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.86 GB/s | 10.55 GB/s | 🔴 -64.66% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1123.60 µs | 3179.04 µs | 🔴 +182.93% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 25.46 µs | 318.29 µs | ⚪ +1150.23% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.47 GOP/s | 2.64 GOP/s | 🔴 -64.66% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 6.47 GB/s | 2.66 GB/s | 🔴 -58.95% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 1296.68 µs | 3158.87 µs | 🔴 +143.61% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 38.58 µs | 171.72 µs | ⚪ +345.09% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 1.62 GOP/s | 0.66 GOP/s | 🔴 -58.95% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 9.70 GB/s | 29.63 GB/s | 🟢 +205.40% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3459.04 µs | 1132.63 µs | 🟢 -67.26% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 351.90 µs | 14.48 µs | ⚪ -95.88% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.43 GOP/s | 7.41 GOP/s | 🟢 +205.40% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 121.99 µs | 214.35 µs | ⚪ +75.70% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 965.74 µs | 1017.93 µs | ⚪ +5.40% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 542.33 µs | 254.56 µs | ⚪ -53.06% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 486.74 µs | 613.85 µs | ⚪ +26.12% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 573.73 µs | 1778.38 µs | ⚪ +209.97% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 428.01 µs | 462.08 µs | ⚪ +7.96% |

