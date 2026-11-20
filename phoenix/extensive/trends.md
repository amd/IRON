# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 451.53 µs | 275.41 µs | ⚪ -39.00% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 10.77 GB/s | 29.59 GB/s | 🟢 +174.62% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 3114.55 µs | 1134.13 µs | 🟢 -63.59% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 332.05 µs | 6.93 µs | ⚪ -97.91% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 2.69 GOP/s | 7.40 GOP/s | 🟢 +174.62% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 236.26 µs | 187.40 µs | ⚪ -20.68% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 7.52 µs | 12.54 µs | ⚪ +66.74% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 20.01 GB/s | 31.44 GB/s | 🟢 +57.11% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 686.86 µs | 118.42 µs | ⚪ -82.76% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 3.33 GOP/s | 5.24 GOP/s | 🟢 +57.11% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.72 GB/s | 16.32 GB/s | 🔴 -50.14% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1538.19 µs | 3084.84 µs | 🔴 +100.55% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 57.75 µs | 378.61 µs | ⚪ +555.57% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.45 GOP/s | 2.72 GOP/s | 🔴 -50.14% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 5.01 µs | 6.20 µs | ⚪ +23.69% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 267.34 µs | 344.30 µs | ⚪ +28.79% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 722.56 µs | 583.62 µs | ⚪ -19.23% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 401.19 µs | 194.55 µs | ⚪ -51.51% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 15.80 GB/s | 10.28 GB/s | 🔴 -34.94% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 2124.42 µs | 3265.32 µs | 🔴 +53.70% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 27.62 µs | 281.11 µs | ⚪ +917.70% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 15.79 GOP/s | 10.28 GOP/s | 🔴 -34.94% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 439.35 µs | 648.43 µs | ⚪ +47.59% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 15.42 µs | 598.24 µs | ⚪ +3779.74% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 618.12 µs | 301.31 µs | ⚪ -51.25% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 862.71 µs | 311.78 µs | ⚪ -63.86% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 28.41 µs | 40.27 µs | ⚪ +41.76% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 109.58 µs | 66.73 µs | ⚪ -39.10% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 96.53 µs | 38.01 µs | ⚪ -60.63% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 283.90 µs | 184.78 µs | ⚪ -34.92% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 9.48 µs | 15.46 µs | ⚪ +63.02% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 7.15 µs | 16.01 µs | ⚪ +123.87% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 957.88 µs | 1088.41 µs | ⚪ +13.63% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.13 GB/s | 24.79 GB/s | 🟢 +122.86% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3016.09 µs | 1353.38 µs | 🟢 -55.13% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 651.51 µs | 367.74 µs | ⚪ -43.56% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 11.13 GOP/s | 24.79 GOP/s | 🟢 +122.86% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.09 GB/s | 29.57 GB/s | 🟢 +166.67% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3026.03 µs | 1134.74 µs | 🟢 -62.50% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 794.76 µs | 7.26 µs | ⚪ -99.09% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.77 GOP/s | 7.39 GOP/s | 🟢 +166.67% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 297.64 µs | 238.67 µs | ⚪ -19.81% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 55.71 µs | 43.68 µs | ⚪ -21.60% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 29.76 µs | 86.46 µs | ⚪ +190.55% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 512.91 µs | 366.74 µs | ⚪ -28.50% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 355.99 µs | 6.57 µs | ⚪ -98.16% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 21.20 µs | 27.82 µs | ⚪ +31.22% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 298.34 µs | 456.23 µs | ⚪ +52.92% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 197.28 µs | 745.19 µs | ⚪ +277.73% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 2.81 GB/s | 6.47 GB/s | 🟢 +130.00% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 2982.33 µs | 1296.65 µs | 🟢 -56.52% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 457.06 µs | 12.95 µs | ⚪ -97.17% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 0.70 GOP/s | 1.62 GOP/s | 🟢 +130.00% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.97 GB/s | 29.65 GB/s | 🟢 +170.39% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3059.83 µs | 1131.63 µs | 🟢 -63.02% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 524.32 µs | 9.24 µs | ⚪ -98.24% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.74 GOP/s | 7.41 GOP/s | 🟢 +170.39% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 45.93 µs | 88.49 µs | ⚪ +92.65% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 247.73 µs | 609.72 µs | ⚪ +146.13% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 564.49 µs | 336.68 µs | ⚪ -40.36% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 600.84 µs | 456.42 µs | ⚪ -24.04% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 353.37 µs | 628.09 µs | ⚪ +77.75% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 372.99 µs | 511.75 µs | ⚪ +37.20% |

