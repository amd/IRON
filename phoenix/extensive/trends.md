# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 14.94 GB/s | 31.12 GB/s | 🟢 +108.29% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 3368.67 µs | 1617.31 µs | 🟢 -51.99% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 529.75 µs | 113.85 µs | ⚪ -78.51% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 4.98 GOP/s | 10.37 GOP/s | 🟢 +108.29% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 553.38 µs | 790.30 µs | ⚪ +42.81% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 15.93 GB/s | 5.59 GB/s | 🔴 -64.93% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1053.08 µs | 3003.14 µs | 🔴 +185.18% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 34.29 µs | 205.56 µs | ⚪ +499.39% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 36.20 µs | 13.18 µs | ⚪ -63.60% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 33.15 GB/s | 15.64 GB/s | 🔴 -52.81% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1518.37 µs | 3217.50 µs | 🔴 +111.90% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 43.95 µs | 328.73 µs | ⚪ +648.00% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.52 GOP/s | 2.61 GOP/s | 🔴 -52.81% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 15.34 GB/s | 31.54 GB/s | 🟢 +105.67% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3282.09 µs | 1595.77 µs | 🟢 -51.38% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 372.02 µs | 150.34 µs | ⚪ -59.59% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.56 GOP/s | 5.26 GOP/s | 🟢 +105.67% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 8.80 µs | 7.40 µs | ⚪ -15.88% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 45.27 µs | 714.70 µs | ⚪ +1478.73% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 485.06 µs | 116.60 µs | ⚪ -75.96% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 33.99 µs | 21.02 µs | ⚪ -38.17% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 15.30 GB/s | 10.20 GB/s | 🔴 -33.35% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 2194.03 µs | 3291.68 µs | 🔴 +50.03% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 151.40 µs | 499.87 µs | ⚪ +230.16% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 15.29 GOP/s | 10.19 GOP/s | 🔴 -33.35% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Bandwidth` | 16.01 GB/s | 10.81 GB/s | 🔴 -32.48% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency` | 2096.94 µs | 3105.80 µs | 🔴 +48.11% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 52.70 µs | 284.53 µs | ⚪ +439.87% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Throughput` | 16.00 GOP/s | 10.80 GOP/s | 🔴 -32.48% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 323.67 µs | 581.72 µs | ⚪ +79.72% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1536.02 µs | 3346.55 µs | 🔴 +117.87% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 419.43 µs | 287.12 µs | ⚪ -31.54% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.73 GB/s | 28.60 GB/s | 🟢 +166.44% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3125.84 µs | 1173.18 µs | 🟢 -62.47% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 407.25 µs | 108.49 µs | ⚪ -73.36% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 16.10 GOP/s | 42.90 GOP/s | 🟢 +166.44% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 6.63 GB/s | 20.95 GB/s | 🟢 +216.12% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 3164.05 µs | 1000.90 µs | 🟢 -68.37% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 208.39 µs | 14.80 µs | ⚪ -92.90% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 0.41 GOP/s | 1.31 GOP/s | 🟢 +216.12% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 115.84 µs | 256.83 µs | ⚪ +121.71% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 69.81 µs | 60.68 µs | ⚪ -13.08% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 85.76 µs | 68.35 µs | ⚪ -20.30% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 104.03 µs | 90.66 µs | ⚪ -12.86% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.07 µs | 14.96 µs | ⚪ +1295.38% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 22.76 µs | 7.53 µs | ⚪ -66.92% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 1537.52 µs | 215.67 µs | ⚪ -85.97% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 398.99 µs | 346.27 µs | ⚪ -13.21% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 465.28 µs | 777.17 µs | ⚪ +67.03% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 215.74 µs | 374.50 µs | ⚪ +73.59% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 33.82 µs | 156.15 µs | ⚪ +361.70% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 44.53 µs | 15.03 µs | ⚪ -66.24% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 67.53 µs | 34.45 µs | ⚪ -48.98% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 19.45 µs | 8.49 µs | ⚪ -56.37% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 44.72 µs | 7.52 µs | ⚪ -83.19% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 408.21 µs | 104.35 µs | ⚪ -74.44% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 360.41 µs | 328.80 µs | ⚪ -8.77% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 56.20 µs | 1370.95 µs | ⚪ +2339.62% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 2.76 GB/s | 5.96 GB/s | 🟢 +116.39% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 3044.05 µs | 1406.75 µs | 🟢 -53.79% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 577.70 µs | 278.18 µs | ⚪ -51.85% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 0.69 GOP/s | 1.49 GOP/s | 🟢 +116.39% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 28.49 GB/s | 11.38 GB/s | 🔴 -60.07% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1177.64 µs | 2949.53 µs | 🔴 +150.46% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 152.29 µs | 549.79 µs | ⚪ +261.02% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.12 GOP/s | 2.84 GOP/s | 🔴 -60.07% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 11.81 µs | 45.50 µs | ⚪ +285.34% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 626.30 µs | 208.48 µs | ⚪ -66.71% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 547.55 µs | 304.65 µs | ⚪ -44.36% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 505.46 µs | 716.10 µs | ⚪ +41.67% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 707.71 µs | 893.19 µs | ⚪ +26.21% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 464.25 µs | 1043.62 µs | ⚪ +124.80% |

