# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 32.04 GB/s | 15.51 GB/s | 🔴 -51.59% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 1570.79 µs | 3244.70 µs | 🔴 +106.56% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 27.50 µs | 395.84 µs | ⚪ +1339.33% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 10.68 GOP/s | 5.17 GOP/s | 🔴 -51.59% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 1171.96 µs | 272.69 µs | ⚪ -76.73% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 538.14 µs | 699.81 µs | ⚪ +30.04% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 30.63 µs | 10.33 µs | ⚪ -66.27% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 15.47 GB/s | 32.37 GB/s | 🟢 +109.33% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3254.55 µs | 1554.71 µs | 🟢 -52.23% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 398.63 µs | 16.03 µs | ⚪ -95.98% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.58 GOP/s | 5.40 GOP/s | 🟢 +109.33% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 329.21 µs | 441.71 µs | ⚪ +34.17% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 6.95 µs | 4.41 µs | ⚪ -36.56% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 16.80 GB/s | 11.28 GB/s | 🔴 -32.86% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1997.29 µs | 2974.93 µs | 🔴 +48.95% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 4.20 GOP/s | 2.82 GOP/s | 🔴 -32.86% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 464.71 µs | 517.82 µs | ⚪ +11.43% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 125.98 µs | 8.31 µs | ⚪ -93.40% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 370.74 µs | 432.03 µs | ⚪ +16.53% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 26.76 µs | 97.54 µs | ⚪ +264.43% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 10.45 GB/s | 27.11 GB/s | 🟢 +159.47% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 3213.10 µs | 1238.34 µs | 🟢 -61.46% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 376.26 µs | 7.19 µs | ⚪ -98.09% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 10.44 GOP/s | 27.10 GOP/s | 🟢 +159.47% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 902.01 µs | 332.64 µs | ⚪ -63.12% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.49 GB/s | 30.08 GB/s | 🟢 +186.70% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3197.97 µs | 1115.46 µs | 🟢 -65.12% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 396.98 µs | 15.80 µs | ⚪ -96.02% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 15.74 GOP/s | 45.12 GOP/s | 🟢 +186.70% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 7.38 GB/s | 21.02 GB/s | 🟢 +184.73% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 2840.20 µs | 997.49 µs | 🟢 -64.88% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 378.64 µs | 17.93 µs | ⚪ -95.26% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 0.46 GOP/s | 1.31 GOP/s | 🟢 +184.73% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 421.28 µs | 337.97 µs | ⚪ -19.78% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 170.20 µs | 96.77 µs | ⚪ -43.14% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 139.13 µs | 81.54 µs | ⚪ -41.39% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 200.87 µs | 44.15 µs | ⚪ -78.02% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 3.74 µs | 8.39 µs | ⚪ +124.56% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 10.55 µs | 20.69 µs | ⚪ +96.12% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 13.70 GB/s | 27.81 GB/s | 🟢 +102.98% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 1019.34 µs | 41.03 µs | ⚪ -95.97% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 13.70 GOP/s | 27.80 GOP/s | 🟢 +102.98% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 402.84 µs | 327.64 µs | ⚪ -18.67% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 18.64 µs | 25.97 µs | ⚪ +39.28% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 244.16 µs | 341.45 µs | ⚪ +39.84% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 65.60 µs | 84.00 µs | ⚪ +28.06% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 55.92 µs | 32.04 µs | ⚪ -42.70% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 975.11 µs | 284.03 µs | ⚪ -70.87% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 23.27 µs | 75.42 µs | ⚪ +224.04% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 210.99 µs | 38.70 µs | ⚪ -81.66% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 103.38 µs | 184.43 µs | ⚪ +78.40% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.71 GB/s | 9.91 GB/s | 🔴 -66.65% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1129.34 µs | 3386.04 µs | 🔴 +199.82% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 24.68 µs | 325.35 µs | ⚪ +1218.26% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.43 GOP/s | 2.48 GOP/s | 🔴 -66.65% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 2.82 GB/s | 6.54 GB/s | 🟢 +131.64% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 2969.90 µs | 1282.11 µs | 🟢 -56.83% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 313.89 µs | 29.22 µs | ⚪ -90.69% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 0.71 GOP/s | 1.64 GOP/s | 🟢 +131.64% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 39.36 µs | 14.31 µs | ⚪ -63.65% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.34 GB/s | 1.44 GB/s | 🟢 +7.52% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1567.14 µs | 1457.49 µs | 🟢 -7.00% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 1149.03 µs | 511.30 µs | ⚪ -55.50% |

