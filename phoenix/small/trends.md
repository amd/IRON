# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 461.86 µs | 578.91 µs | ⚪ +25.34% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 28.18 GB/s | 10.39 GB/s | 🔴 -63.13% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 1190.63 µs | 3228.87 µs | 🔴 +171.19% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 120.62 µs | 326.60 µs | ⚪ +170.76% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 7.05 GOP/s | 2.60 GOP/s | 🔴 -63.13% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 15.77 GB/s | 5.19 GB/s | 🔴 -67.07% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1064.16 µs | 3232.08 µs | 🔴 +203.72% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 25.73 µs | 94.09 µs | ⚪ +265.69% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 14.57 µs | 28.31 µs | ⚪ +94.36% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.37 GB/s | 14.16 GB/s | 🔴 -56.24% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1554.98 µs | 3553.71 µs | 🔴 +128.54% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 49.95 µs | 472.71 µs | ⚪ +846.29% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.39 GOP/s | 2.36 GOP/s | 🔴 -56.24% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 322.45 µs | 590.80 µs | ⚪ +83.22% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 4.81 µs | 3.38 µs | ⚪ -29.78% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 285.32 µs | 397.96 µs | ⚪ +39.48% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 132.76 µs | 228.07 µs | ⚪ +71.79% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 338.40 µs | 426.84 µs | ⚪ +26.13% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 667.52 µs | 615.82 µs | ⚪ -7.74% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 386.91 µs | 556.25 µs | ⚪ +43.77% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 10.17 GB/s | 28.00 GB/s | 🟢 +175.27% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3299.10 µs | 1198.49 µs | 🟢 -63.67% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 266.67 µs | 13.98 µs | ⚪ -94.76% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 15.26 GOP/s | 42.00 GOP/s | 🟢 +175.27% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.81 GB/s | 29.47 GB/s | 🟢 +172.66% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3104.53 µs | 1138.59 µs | 🟢 -63.32% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 409.60 µs | 23.50 µs | ⚪ -94.26% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 16.21 GOP/s | 44.21 GOP/s | 🟢 +172.66% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 530.77 µs | 127.24 µs | ⚪ -76.03% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 274.11 µs | 243.79 µs | ⚪ -11.06% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 162.27 µs | 90.05 µs | ⚪ -44.51% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 170.91 µs | 515.28 µs | ⚪ +201.49% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 7.28 µs | 51.43 µs | ⚪ +606.02% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 9.49 µs | 14.90 µs | ⚪ +56.99% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 10.86 GB/s | 28.14 GB/s | 🟢 +159.02% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3089.73 µs | 1192.84 µs | 🟢 -61.39% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 463.35 µs | 47.20 µs | ⚪ -89.81% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 10.86 GOP/s | 28.13 GOP/s | 🟢 +159.02% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.98 µs | 8.19 µs | ⚪ +17.44% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 29.91 µs | 24.25 µs | ⚪ -18.93% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 26.46 µs | 146.36 µs | ⚪ +453.03% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 11.11 µs | 7.65 µs | ⚪ -31.16% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.36 GB/s | 10.15 GB/s | 🔴 -64.22% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1183.46 µs | 3307.39 µs | 🔴 +179.47% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 18.43 µs | 334.71 µs | ⚪ +1716.19% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.09 GOP/s | 2.54 GOP/s | 🔴 -64.22% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 245.06 µs | 307.61 µs | ⚪ +25.52% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 33.15 µs | 9.57 µs | ⚪ -71.12% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 115.21 µs | 228.04 µs | ⚪ +97.94% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 343.07 µs | 636.37 µs | ⚪ +85.49% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 545.56 µs | 617.86 µs | ⚪ +13.25% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 3194.30 µs | 1782.69 µs | 🟢 -44.19% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 131.44 µs | 569.87 µs | ⚪ +333.55% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 27.91 GB/s | 11.13 GB/s | 🔴 -60.14% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1202.11 µs | 3015.68 µs | 🔴 +150.87% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 177.68 µs | 310.58 µs | ⚪ +74.79% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 6.98 GOP/s | 2.78 GOP/s | 🔴 -60.14% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.55 GB/s | 0.57 GB/s | 🔴 -63.21% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1352.59 µs | 3676.55 µs | 🔴 +171.82% |

