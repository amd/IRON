# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 14.59 GB/s | 32.34 GB/s | 🟢 +121.67% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 3450.46 µs | 1556.54 µs | 🟢 -54.89% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 781.54 µs | 21.52 µs | ⚪ -97.25% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 4.86 GOP/s | 10.78 GOP/s | 🟢 +121.67% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 10.46 GB/s | 29.60 GB/s | 🟢 +183.11% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 3209.12 µs | 1133.51 µs | 🟢 -64.68% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 456.57 µs | 102.79 µs | ⚪ -77.49% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 2.61 GOP/s | 7.40 GOP/s | 🟢 +183.11% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 109.21 µs | 1136.83 µs | ⚪ +940.96% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 22.85 µs | 7.16 µs | ⚪ -68.67% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 672.18 µs | 29.14 µs | ⚪ -95.66% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 463.39 µs | 343.87 µs | ⚪ -25.79% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 11.80 µs | 3.87 µs | ⚪ -67.24% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 421.10 µs | 661.15 µs | ⚪ +57.00% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 208.46 µs | 417.24 µs | ⚪ +100.15% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 285.12 µs | 97.85 µs | ⚪ -65.68% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 226.55 µs | 608.30 µs | ⚪ +168.51% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 229.09 µs | 393.89 µs | ⚪ +71.94% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 166.50 µs | 187.60 µs | ⚪ +12.67% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 375.64 µs | 1168.82 µs | ⚪ +211.15% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 303.78 µs | 676.48 µs | ⚪ +122.69% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 7.01 GB/s | 21.07 GB/s | 🟢 +200.71% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 2992.94 µs | 995.30 µs | 🟢 -66.75% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 103.04 µs | 13.22 µs | ⚪ -87.17% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 0.44 GOP/s | 1.32 GOP/s | 🟢 +200.71% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 253.25 µs | 325.76 µs | ⚪ +28.63% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 111.22 µs | 89.36 µs | ⚪ -19.65% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 106.41 µs | 85.71 µs | ⚪ -19.45% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 103.30 µs | 76.23 µs | ⚪ -26.21% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 7.69 µs | 9.68 µs | ⚪ +25.77% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 10.81 µs | 16.94 µs | ⚪ +56.67% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.22 GB/s | 10.25 GB/s | 🔴 -63.67% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1189.18 µs | 3272.86 µs | 🔴 +175.22% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 19.59 µs | 397.51 µs | ⚪ +1929.47% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 28.22 GOP/s | 10.25 GOP/s | 🔴 -63.67% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 332.19 µs | 352.38 µs | ⚪ +6.08% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.61 GB/s | 10.11 GB/s | 🔴 -65.85% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1133.36 µs | 3318.67 µs | 🔴 +192.82% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.03 µs | 418.69 µs | ⚪ +6848.12% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.40 GOP/s | 2.53 GOP/s | 🔴 -65.85% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 180.48 µs | 224.63 µs | ⚪ +24.46% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 99.77 µs | 72.17 µs | ⚪ -27.66% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Bandwidth` | 25.68 GB/s | 2.63 GB/s | 🔴 -89.74% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency` | 327.02 µs | 3188.02 µs | 🔴 +874.88% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 14.82 µs | 105.13 µs | ⚪ +609.52% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Throughput` | 19.24 GOP/s | 1.97 GOP/s | 🔴 -89.74% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.18 GB/s | 10.30 GB/s | 🔴 -63.46% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1191.19 µs | 3259.59 µs | 🔴 +173.64% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 11.48 µs | 341.66 µs | ⚪ +2875.73% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.04 GOP/s | 2.57 GOP/s | 🔴 -63.46% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 20.04 µs | 11.56 µs | ⚪ -42.30% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 28.84 µs | 14.68 µs | ⚪ -49.10% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 380.48 µs | 24.64 µs | ⚪ -93.52% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 250.57 µs | 231.17 µs | ⚪ -7.74% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.26 GB/s | 29.39 GB/s | 🟢 +186.46% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3270.79 µs | 1141.81 µs | 🟢 -65.09% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 390.04 µs | 10.87 µs | ⚪ -97.21% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.56 GOP/s | 7.35 GOP/s | 🟢 +186.46% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 2.96 GB/s | 6.50 GB/s | 🟢 +119.47% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 2830.72 µs | 1289.81 µs | 🟢 -54.44% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 660.59 µs | 5.79 µs | ⚪ -99.12% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 0.74 GOP/s | 1.63 GOP/s | 🟢 +119.47% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.63 GB/s | 10.70 GB/s | 🔴 -63.88% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1132.63 µs | 3135.83 µs | 🔴 +176.86% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.75 µs | 723.86 µs | ⚪ +12498.69% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.41 GOP/s | 2.68 GOP/s | 🔴 -63.88% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 328.06 µs | 226.49 µs | ⚪ -30.96% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 295.05 µs | 58.00 µs | ⚪ -80.34% |

