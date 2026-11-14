# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 327.98 µs | 822.46 µs | ⚪ +150.76% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 5.27 GB/s | 15.80 GB/s | 🟢 +199.60% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 3180.81 µs | 1061.69 µs | 🟢 -66.62% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 85.46 µs | 16.36 µs | ⚪ -80.86% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 6.35 µs | 10.73 µs | ⚪ +69.06% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 15.20 GB/s | 32.24 GB/s | 🟢 +112.14% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3311.61 µs | 1561.03 µs | 🟢 -52.86% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 433.79 µs | 26.63 µs | ⚪ -93.86% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.53 GOP/s | 5.37 GOP/s | 🟢 +112.14% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.27 GB/s | 15.20 GB/s | 🔴 -52.88% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1559.93 µs | 3310.45 µs | 🔴 +112.22% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 6.52 µs | 297.57 µs | ⚪ +4462.55% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.38 GOP/s | 2.53 GOP/s | 🔴 -52.88% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 12.91 µs | 4.40 µs | ⚪ -65.91% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.74 GB/s | 17.90 GB/s | 🟢 +66.71% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3124.83 µs | 1874.45 µs | 🟢 -40.01% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 381.07 µs | 31.85 µs | ⚪ -91.64% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.68 GOP/s | 4.48 GOP/s | 🟢 +66.71% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 321.56 µs | 139.21 µs | ⚪ -56.71% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 90.23 µs | 107.99 µs | ⚪ +19.68% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 15.85 GB/s | 10.47 GB/s | 🔴 -33.96% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 2117.95 µs | 3207.04 µs | 🔴 +51.42% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 55.90 µs | 350.33 µs | ⚪ +526.71% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 15.84 GOP/s | 10.46 GOP/s | 🔴 -33.96% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 278.84 µs | 660.81 µs | ⚪ +136.98% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 27.03 GB/s | 10.62 GB/s | 🔴 -60.69% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 1242.26 µs | 3160.38 µs | 🔴 +154.41% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 80.74 µs | 367.88 µs | ⚪ +355.63% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 27.01 GOP/s | 10.62 GOP/s | 🔴 -60.69% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 10.91 GB/s | 28.21 GB/s | 🟢 +158.62% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3077.18 µs | 1189.82 µs | 🟢 -61.33% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 543.92 µs | 6.80 µs | ⚪ -98.75% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 16.36 GOP/s | 42.30 GOP/s | 🟢 +158.62% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.63 GB/s | 9.76 GB/s | 🔴 -67.08% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1132.44 µs | 3439.71 µs | 🔴 +203.74% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 10.48 µs | 181.31 µs | ⚪ +1630.11% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 44.45 GOP/s | 14.63 GOP/s | 🔴 -67.08% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 20.74 GB/s | 6.99 GB/s | 🔴 -66.30% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 1011.31 µs | 3000.61 µs | 🔴 +196.70% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 25.69 µs | 179.33 µs | ⚪ +597.98% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 1.30 GOP/s | 0.44 GOP/s | 🔴 -66.30% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 314.61 µs | 255.39 µs | ⚪ -18.82% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 29.26 µs | 55.58 µs | ⚪ +89.99% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 79.02 µs | 57.67 µs | ⚪ -27.01% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 341.73 µs | 472.72 µs | ⚪ +38.33% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 13.89 µs | 27.69 µs | ⚪ +99.38% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.30 GB/s | 29.77 GB/s | 🟢 +189.20% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3259.14 µs | 1126.94 µs | 🟢 -65.42% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 390.30 µs | 9.45 µs | ⚪ -97.58% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 10.30 GOP/s | 29.77 GOP/s | 🟢 +189.20% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 10.55 µs | 5.45 µs | ⚪ -48.38% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 321.83 µs | 203.10 µs | ⚪ -36.89% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 43.00 µs | 106.24 µs | ⚪ +147.06% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 87.03 µs | 23.28 µs | ⚪ -73.25% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 798.62 µs | 496.57 µs | ⚪ -37.82% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.88 GB/s | 28.60 GB/s | 🟢 +162.78% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3084.30 µs | 1173.71 µs | 🟢 -61.95% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 420.96 µs | 27.42 µs | ⚪ -93.49% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.72 GOP/s | 7.15 GOP/s | 🟢 +162.78% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 37.19 µs | 11.79 µs | ⚪ -68.31% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 229.70 µs | 315.85 µs | ⚪ +37.51% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 185.95 µs | 368.21 µs | ⚪ +98.02% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 10.69 µs | 19.24 µs | ⚪ +79.95% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 28.92 µs | 39.30 µs | ⚪ +35.91% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 950.47 µs | 536.12 µs | ⚪ -43.59% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 443.02 µs | 220.16 µs | ⚪ -50.30% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 1004.64 µs | 528.90 µs | ⚪ -47.35% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 515.01 µs | 409.00 µs | ⚪ -20.58% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 551.66 µs | 1481.51 µs | ⚪ +168.56% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 884.70 µs | 597.51 µs | ⚪ -32.46% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 810.36 µs | 630.04 µs | ⚪ -22.25% |

