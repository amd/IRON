# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 1191.68 µs | 236.98 µs | ⚪ -80.11% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 335.16 µs | 251.26 µs | ⚪ -25.03% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 43.91 µs | 47.69 µs | ⚪ +8.61% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.28 GB/s | 14.99 GB/s | 🔴 -53.55% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1559.38 µs | 3357.33 µs | 🔴 +115.30% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 8.59 µs | 743.84 µs | ⚪ +8563.46% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.38 GOP/s | 2.50 GOP/s | 🔴 -53.55% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 316.61 µs | 298.49 µs | ⚪ -5.73% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 7.29 µs | 1.99 µs | ⚪ -72.70% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 417.50 µs | 288.77 µs | ⚪ -30.83% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 668.44 µs | 822.18 µs | ⚪ +23.00% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 159.74 µs | 277.10 µs | ⚪ +73.47% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 500.66 µs | 365.32 µs | ⚪ -27.03% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 241.02 µs | 770.81 µs | ⚪ +219.81% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 27.25 GB/s | 10.53 GB/s | 🔴 -61.36% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 1232.16 µs | 3189.00 µs | 🔴 +158.81% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 43.59 µs | 410.08 µs | ⚪ +840.84% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 27.23 GOP/s | 10.52 GOP/s | 🔴 -61.36% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 825.71 µs | 543.07 µs | ⚪ -34.23% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 400.86 µs | 303.53 µs | ⚪ -24.28% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 6.64 GB/s | 20.98 GB/s | 🟢 +216.00% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 3158.70 µs | 999.59 µs | 🟢 -68.35% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 149.86 µs | 2.37 µs | ⚪ -98.42% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 0.41 GOP/s | 1.31 GOP/s | 🟢 +216.00% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 107.60 µs | 74.74 µs | ⚪ -30.54% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 94.09 µs | 61.55 µs | ⚪ -34.58% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 115.30 µs | 432.26 µs | ⚪ +274.91% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 3.74 µs | 11.64 µs | ⚪ +211.34% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 7.20 µs | 8.93 µs | ⚪ +24.07% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 10.65 GB/s | 27.83 GB/s | 🟢 +161.26% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3150.72 µs | 1205.97 µs | 🟢 -61.72% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 854.21 µs | 32.73 µs | ⚪ -96.17% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 10.65 GOP/s | 27.82 GOP/s | 🟢 +161.26% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 28.41 GB/s | 10.49 GB/s | 🔴 -63.07% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1180.91 µs | 3197.99 µs | 🔴 +170.81% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 146.62 µs | 396.86 µs | ⚪ +170.68% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 28.41 GOP/s | 10.49 GOP/s | 🔴 -63.07% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 303.61 µs | 277.79 µs | ⚪ -8.51% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 183.95 µs | 218.64 µs | ⚪ +18.86% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 88.22 µs | 78.65 µs | ⚪ -10.85% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 56.63 µs | 13.03 µs | ⚪ -77.00% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 535.23 µs | 1113.14 µs | ⚪ +107.97% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 13.38 GB/s | 27.03 GB/s | 🟢 +102.02% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 913.70 µs | 80.01 µs | ⚪ -91.24% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 3.34 GOP/s | 6.76 GOP/s | 🟢 +102.02% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 10.43 µs | 19.32 µs | ⚪ +85.21% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 491.60 µs | 168.63 µs | ⚪ -65.70% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 350.95 µs | 307.36 µs | ⚪ -12.42% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 67.02 µs | 6.51 µs | ⚪ -90.28% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 44.76 µs | 118.84 µs | ⚪ +165.50% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.62 GB/s | 29.66 GB/s | 🟢 +155.33% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2888.60 µs | 1131.31 µs | 🟢 -60.84% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 863.08 µs | 9.57 µs | ⚪ -98.89% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.90 GOP/s | 7.41 GOP/s | 🟢 +155.33% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 147.04 µs | 214.62 µs | ⚪ +45.96% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 585.14 µs | 497.20 µs | ⚪ -15.03% |

