# Performance trends

**Operators added:** `SelectiveScan`, `pre_push_hook`

**Operators dropped:** `visualize`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 361.25 | 668.62 | 🔴 +85.09% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 12.94 | 29.98 | 🟢 +131.66% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 2592.59 | 1119.15 | 🟢 -56.83% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 1220.90 | 16.63 | 🟢 -98.64% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 3.24 | 7.50 | 🟢 +131.66% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 15.65 | 5.29 | 🔴 -66.17% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1071.78 | 3168.56 | 🔴 +195.64% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 122.80 | 313.60 | 🔴 +155.37% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 15.84 | 20.48 | 🟢 +29.32% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3178.35 | 2457.79 | 🟢 -22.67% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 656.27 | 862.94 | 🔴 +31.49% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.64 | 3.41 | 🟢 +29.32% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 17.38 | 15.96 | 🔴 -8.14% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 2896.78 | 3153.62 | 🔴 +8.87% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 1128.30 | 703.17 | 🟢 -37.68% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.90 | 2.66 | 🔴 -8.14% |
| `Emit` | `npu1-Emit-eight_carried` | `Bandwidth` | 0.13 | 0.07 | 🔴 -42.83% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency` | 15.64 | 27.37 | 🔴 +74.92% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 3.45 | 12.84 | 🔴 +272.51% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.29 | 10.85 | 🟢 +5.49% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3260.85 | 3091.22 | 🟢 -5.20% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 358.71 | 218.93 | 🟢 -38.97% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.57 | 2.71 | 🟢 +5.49% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 444.04 | 311.05 | 🟢 -29.95% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 138.88 | 405.96 | 🔴 +192.31% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 15.27 | 10.96 | 🟢 -28.25% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 250.10 | 161.72 | 🟢 -35.34% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 130.06 | 111.78 | 🟢 -14.06% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 105.39 | 124.33 | 🔴 +17.96% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.19 | 0.21 | 🟢 +5.95% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 84.25 | 79.52 | 🟢 -5.61% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 10.03 | 1.94 | 🟢 -80.62% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 9.53 | 10.78 | 🔴 +13.03% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.17 | 12.93 | 🔴 -54.10% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1191.59 | 2596.17 | 🔴 +117.88% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 6.57 | 1145.56 | 🔴 +17342.85% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 28.16 | 12.92 | 🔴 -54.10% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 486.90 | 441.74 | 🟢 -9.27% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 273.01 | 555.85 | 🔴 +103.60% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 341.21 | 319.87 | 🟢 -6.25% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 54.67 | 35.39 | 🟢 -35.27% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 6.43 | 11.11 | 🔴 +72.81% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 8.43 | 16.23 | 🔴 +92.58% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 25.55 | 7.42 | 🟢 -70.96% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 9.31 | 31.51 | 🔴 +238.59% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 9.58 | 12.70 | 🟢 +32.61% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3503.00 | 2641.57 | 🟢 -24.59% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 376.38 | 787.30 | 🔴 +109.17% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.39 | 3.18 | 🟢 +32.61% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 17.00 | 11.25 | 🔴 -33.80% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1974.28 | 2982.43 | 🔴 +51.06% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 906.96 | 618.17 | 🟢 -31.84% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 4.25 | 2.81 | 🔴 -33.80% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 2.74 | 6.46 | 🟢 +135.19% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 3056.20 | 1299.48 | 🟢 -57.48% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 554.28 | 9.94 | 🟢 -98.21% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 0.69 | 1.61 | 🟢 +135.19% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.45 | 10.47 | 🔴 -64.45% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1139.44 | 3204.83 | 🔴 +181.26% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 18.60 | 593.25 | 🔴 +3089.53% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.36 | 2.62 | 🔴 -64.45% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 390.00 | 194.91 | 🟢 -50.02% |

