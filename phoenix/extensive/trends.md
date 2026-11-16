# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 309.05 µs | 396.43 µs | ⚪ +28.27% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 326.02 µs | 282.40 µs | ⚪ -13.38% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 254.53 µs | 918.69 µs | ⚪ +260.94% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 14.32 µs | 8.57 µs | ⚪ -40.17% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 439.21 µs | 675.31 µs | ⚪ +53.76% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 259.81 µs | 1370.58 µs | ⚪ +427.53% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 12.76 µs | 5.41 µs | ⚪ -57.58% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 724.46 µs | 398.29 µs | ⚪ -45.02% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 319.22 µs | 6.58 µs | ⚪ -97.94% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 300.49 µs | 221.64 µs | ⚪ -26.24% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 419.93 µs | 545.42 µs | ⚪ +29.88% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 9.79 GB/s | 27.23 GB/s | 🟢 +178.16% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 3429.19 µs | 1232.81 µs | 🟢 -64.05% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 560.41 µs | 26.27 µs | ⚪ -95.31% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 9.78 GOP/s | 27.22 GOP/s | 🟢 +178.16% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 326.08 µs | 1057.14 µs | ⚪ +224.20% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.59 GB/s | 10.18 GB/s | 🔴 -65.59% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1133.98 µs | 3295.28 µs | 🔴 +190.59% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 13.71 µs | 333.61 µs | ⚪ +2334.15% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 44.39 GOP/s | 15.27 GOP/s | 🔴 -65.59% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 425.01 µs | 162.85 µs | ⚪ -61.68% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 178.88 µs | 338.67 µs | ⚪ +89.33% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 73.74 µs | 42.81 µs | ⚪ -41.95% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 58.86 µs | 188.34 µs | ⚪ +219.96% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 5.92 µs | 162.62 µs | ⚪ +2648.85% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 10.37 µs | 12.11 µs | ⚪ +16.76% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 9.49 µs | 21.75 µs | ⚪ +129.18% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 27.97 GB/s | 11.11 GB/s | 🔴 -60.27% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1200.05 µs | 3020.22 µs | 🔴 +151.67% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 73.49 µs | 358.88 µs | ⚪ +388.32% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 27.96 GOP/s | 11.11 GOP/s | 🔴 -60.27% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2911.77 µs | 1523.83 µs | 🟢 -47.67% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 595.36 µs | 416.72 µs | ⚪ -30.01% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.57 GB/s | 11.32 GB/s | 🔴 -61.72% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1134.64 µs | 2963.98 µs | 🔴 +161.23% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 4.41 µs | 696.56 µs | ⚪ +15698.62% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.39 GOP/s | 2.83 GOP/s | 🔴 -61.72% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 202.82 µs | 348.94 µs | ⚪ +72.04% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 176.55 µs | 207.22 µs | ⚪ +17.37% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 16.13 µs | 11.03 µs | ⚪ -31.64% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 609.85 µs | 509.59 µs | ⚪ -16.44% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.60 GB/s | 24.44 GB/s | 🟢 +130.48% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3165.19 µs | 1373.29 µs | 🟢 -56.61% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 331.18 µs | 355.51 µs | ⚪ +7.35% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.65 GOP/s | 6.11 GOP/s | 🟢 +130.48% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 15.67 µs | 8.16 µs | ⚪ -47.94% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 78.11 µs | 407.67 µs | ⚪ +421.93% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 312.75 µs | 287.24 µs | ⚪ -8.16% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.73 GB/s | 29.72 GB/s | 🟢 +153.33% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2860.54 µs | 1129.19 µs | 🟢 -60.53% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 732.16 µs | 6.43 µs | ⚪ -99.12% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.93 GOP/s | 7.43 GOP/s | 🟢 +153.33% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 3.39 GB/s | 6.53 GB/s | 🟢 +92.83% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 794.54 µs | 9.23 µs | ⚪ -98.84% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 0.85 GOP/s | 1.63 GOP/s | 🟢 +92.83% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.21 µs | 30.11 µs | ⚪ +477.86% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.49 GB/s | 1.54 GB/s | 🟢 +213.42% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 4271.76 µs | 1362.93 µs | 🟢 -68.09% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 135.74 µs | 206.94 µs | ⚪ +52.45% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 965.74 µs | 282.76 µs | ⚪ -70.72% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 430.06 µs | 335.20 µs | ⚪ -22.06% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 526.60 µs | 405.57 µs | ⚪ -22.98% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 782.09 µs | 547.00 µs | ⚪ -30.06% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 549.30 µs | 277.79 µs | ⚪ -49.43% |

