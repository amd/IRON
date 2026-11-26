# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 95.10 µs | 8.65 µs | ⚪ -90.91% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 1233.67 µs | 425.03 µs | ⚪ -65.55% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 221.64 µs | 110.99 µs | ⚪ -49.92% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 12.12 µs | 4.86 µs | ⚪ -59.86% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 579.53 µs | 1130.45 µs | ⚪ +95.06% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 16.23 GB/s | 32.14 GB/s | 🟢 +98.00% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3100.45 µs | 1565.91 µs | 🟢 -49.49% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 634.58 µs | 5.34 µs | ⚪ -99.16% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.71 GOP/s | 5.36 GOP/s | 🟢 +98.00% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 5.98 µs | 7.17 µs | ⚪ +19.94% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 18.04 µs | 1152.73 µs | ⚪ +6290.23% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 235.79 µs | 680.20 µs | ⚪ +188.47% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 257.33 µs | 217.53 µs | ⚪ -15.47% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 57.14 µs | 615.53 µs | ⚪ +977.18% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 520.78 µs | 569.56 µs | ⚪ +9.37% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 723.43 µs | 37.42 µs | ⚪ -94.83% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 388.28 µs | 1102.39 µs | ⚪ +183.92% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 893.95 µs | 527.65 µs | ⚪ -40.98% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 200.88 µs | 287.61 µs | ⚪ +43.17% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 203.78 µs | 88.15 µs | ⚪ -56.74% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 49.87 µs | 89.18 µs | ⚪ +78.83% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 86.87 µs | 63.77 µs | ⚪ -26.59% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 173.00 µs | 44.93 µs | ⚪ -74.03% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 10.53 µs | 20.61 µs | ⚪ +95.80% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 2.39 µs | 19.80 µs | ⚪ +728.73% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 1168.81 µs | 226.67 µs | ⚪ -80.61% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 309.10 µs | 611.62 µs | ⚪ +97.87% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 300.55 µs | 790.17 µs | ⚪ +162.91% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 72.29 µs | 127.57 µs | ⚪ +76.47% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 12.86 µs | 25.85 µs | ⚪ +101.05% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 403.92 µs | 342.27 µs | ⚪ -15.26% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 32.44 µs | 4.33 µs | ⚪ -86.66% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 33.79 µs | 7.18 µs | ⚪ -78.75% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 317.57 µs | 294.88 µs | ⚪ -7.14% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 61.27 µs | 69.96 µs | ⚪ +14.18% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.55 GB/s | 29.77 GB/s | 🟢 +182.08% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3179.04 µs | 1126.99 µs | 🟢 -64.55% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 318.29 µs | 17.34 µs | ⚪ -94.55% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.64 GOP/s | 7.44 GOP/s | 🟢 +182.08% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 2.66 GB/s | 6.44 GB/s | 🟢 +142.50% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 3158.87 µs | 1302.62 µs | 🟢 -58.76% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 171.72 µs | 37.42 µs | ⚪ -78.21% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 0.66 GOP/s | 1.61 GOP/s | 🟢 +142.50% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 14.48 µs | 12.87 µs | ⚪ -11.14% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 214.35 µs | 169.61 µs | ⚪ -20.87% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 1017.93 µs | 213.65 µs | ⚪ -79.01% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 254.56 µs | 334.35 µs | ⚪ +31.34% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 613.85 µs | 398.00 µs | ⚪ -35.16% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 1778.38 µs | 1009.09 µs | ⚪ -43.26% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 462.08 µs | 1097.46 µs | ⚪ +137.50% |

