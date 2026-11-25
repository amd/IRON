# Performance trends

**Operators added:** `lm_server`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 866.55 µs | 403.01 µs | ⚪ -53.49% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 3273.47 µs | 1546.83 µs | 🟢 -52.75% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 312.93 µs | 587.77 µs | ⚪ +87.83% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 15.79 GB/s | 5.46 GB/s | 🔴 -65.40% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1062.83 µs | 3071.55 µs | 🔴 +189.00% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 10.50 µs | 620.57 µs | ⚪ +5807.69% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 15.19 µs | 21.41 µs | ⚪ +40.92% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 1200.24 µs | 488.13 µs | ⚪ -59.33% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 640.28 µs | 359.84 µs | ⚪ -43.80% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 7.50 µs | 8.27 µs | ⚪ +10.22% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.13 GB/s | 18.18 GB/s | 🟢 +63.36% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 594.15 µs | 69.21 µs | ⚪ -88.35% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.78 GOP/s | 4.54 GOP/s | 🟢 +63.36% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 629.55 µs | 414.03 µs | ⚪ -34.23% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Bandwidth` | 12.00 GB/s | 13.26 GB/s | 🟢 +10.56% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency` | 3149.30 µs | 2848.48 µs | 🟢 -9.55% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 145.47 µs | 7.58 µs | ⚪ -94.79% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Throughput` | 11.99 GOP/s | 13.25 GOP/s | 🟢 +10.56% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 526.70 µs | 377.37 µs | ⚪ -28.35% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 284.86 µs | 485.00 µs | ⚪ +70.26% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 352.71 µs | 200.40 µs | ⚪ -43.18% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 11.01 GB/s | 28.03 GB/s | 🟢 +154.59% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3048.09 µs | 1197.25 µs | 🟢 -60.72% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 446.81 µs | 12.66 µs | ⚪ -97.17% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 16.51 GOP/s | 42.04 GOP/s | 🟢 +154.59% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 747.51 µs | 1281.52 µs | ⚪ +71.44% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 416.86 µs | 314.53 µs | ⚪ -24.55% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 136.52 µs | 255.85 µs | ⚪ +87.41% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 44.67 µs | 100.00 µs | ⚪ +123.87% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 279.41 µs | 183.10 µs | ⚪ -34.47% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 8.58 µs | 12.93 µs | ⚪ +50.67% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 8.96 µs | 11.63 µs | ⚪ +29.74% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 67.04 µs | 56.32 µs | ⚪ -15.99% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.81 GB/s | 29.63 GB/s | 🟢 +173.99% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3103.23 µs | 1132.63 µs | 🟢 -63.50% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 464.60 µs | 11.09 µs | ⚪ -97.61% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 10.81 GOP/s | 29.63 GOP/s | 🟢 +173.99% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.43 GB/s | 29.59 GB/s | 🟢 +183.77% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3217.65 µs | 1133.88 µs | 🟢 -64.76% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 564.34 µs | 11.88 µs | ⚪ -97.90% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.61 GOP/s | 7.40 GOP/s | 🟢 +183.77% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Bandwidth` | 0.81 GB/s | 0.62 GB/s | 🔴 -24.48% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency` | 50893.67 µs | 67387.92 µs | 🔴 +32.41% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 168.19 µs | 62.20 µs | ⚪ -63.02% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 12.02 µs | 35.69 µs | ⚪ +196.84% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.74 GB/s | 11.46 GB/s | 🔴 -60.11% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1167.85 µs | 2927.75 µs | 🔴 +150.70% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 51.09 µs | 658.94 µs | ⚪ +1189.73% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.18 GOP/s | 2.87 GOP/s | 🔴 -60.11% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.45 GB/s | 25.57 GB/s | 🟢 +144.75% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3212.30 µs | 1312.48 µs | 🟢 -59.14% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 324.97 µs | 234.42 µs | ⚪ -27.87% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.61 GOP/s | 6.39 GOP/s | 🟢 +144.75% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 27.79 µs | 8.93 µs | ⚪ -67.86% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 353.87 µs | 407.57 µs | ⚪ +15.18% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 18.34 GB/s | 12.41 GB/s | 🔴 -32.34% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 15.06 µs | 608.56 µs | ⚪ +3941.34% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 4.58 GOP/s | 3.10 GOP/s | 🔴 -32.34% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 324.53 µs | 433.10 µs | ⚪ +33.46% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 522.49 µs | 693.12 µs | ⚪ +32.66% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.72 µs | 7.23 µs | ⚪ +7.51% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.53 GB/s | 1.62 GB/s | 🟢 +5.60% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1368.21 µs | 1295.70 µs | 🟢 -5.30% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 880.29 µs | 412.43 µs | ⚪ -53.15% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 561.55 µs | 499.81 µs | ⚪ -10.99% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 4347.39 µs | 598.32 µs | ⚪ -86.24% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 908.56 µs | 853.95 µs | ⚪ -6.01% |

