# Performance trends

**Operators added:** `mha_prefill_lxl`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 763.06 µs | 1154.37 µs | ⚪ +51.28% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 766.61 µs | 502.27 µs | ⚪ -34.48% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 11.64 µs | 6.15 µs | ⚪ -47.17% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 10.82 µs | 12.98 µs | ⚪ +19.97% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 1171.12 µs | 634.29 µs | ⚪ -45.84% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 276.61 µs | 658.23 µs | ⚪ +137.97% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 10.00 µs | 5.07 µs | ⚪ -49.28% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 197.97 µs | 443.88 µs | ⚪ +124.21% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 533.13 µs | 345.84 µs | ⚪ -35.13% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 254.24 µs | 129.24 µs | ⚪ -49.17% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 10.23 GB/s | 15.79 GB/s | 🟢 +54.37% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 3282.96 µs | 2126.64 µs | 🟢 -35.22% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 399.62 µs | 4.87 µs | ⚪ -98.78% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 10.22 GOP/s | 15.78 GOP/s | 🟢 +54.37% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 123.40 µs | 600.21 µs | ⚪ +386.38% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 1687.73 µs | 3397.97 µs | 🔴 +101.33% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 550.26 µs | 364.95 µs | ⚪ -33.68% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 609.45 µs | 36.04 µs | ⚪ -94.09% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.89 GB/s | 29.37 GB/s | 🟢 +169.75% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3082.25 µs | 1142.64 µs | 🟢 -62.93% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 607.91 µs | 18.98 µs | ⚪ -96.88% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 16.33 GOP/s | 44.05 GOP/s | 🟢 +169.75% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 7.03 GB/s | 21.24 GB/s | 🟢 +201.98% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 2981.77 µs | 987.40 µs | 🟢 -66.89% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 136.77 µs | 5.48 µs | ⚪ -95.99% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 0.44 GOP/s | 1.33 GOP/s | 🟢 +201.98% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 229.55 µs | 272.73 µs | ⚪ +18.81% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 69.35 µs | 83.48 µs | ⚪ +20.38% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 82.48 µs | 54.35 µs | ⚪ -34.10% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 36.48 µs | 135.23 µs | ⚪ +270.72% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 12.79 µs | 9.76 µs | ⚪ -23.66% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 34.52 µs | 9.12 µs | ⚪ -73.58% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 178.39 µs | 308.66 µs | ⚪ +73.03% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.82 GB/s | 29.21 GB/s | 🟢 +169.93% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3100.99 µs | 1148.83 µs | 🟢 -62.95% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 388.06 µs | 21.53 µs | ⚪ -94.45% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 10.82 GOP/s | 29.21 GOP/s | 🟢 +169.93% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.17 GB/s | 29.64 GB/s | 🟢 +191.50% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3299.54 µs | 1131.93 µs | 🟢 -65.69% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 307.73 µs | 18.14 µs | ⚪ -94.10% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.54 GOP/s | 7.41 GOP/s | 🟢 +191.50% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 211.96 µs | 315.22 µs | ⚪ +48.72% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 59.49 µs | 88.22 µs | ⚪ +48.30% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 71.72 µs | 106.62 µs | ⚪ +48.65% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 715.58 µs | 436.73 µs | ⚪ -38.97% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 9.96 GB/s | 28.55 GB/s | 🟢 +186.68% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3370.22 µs | 1175.60 µs | 🟢 -65.12% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 237.41 µs | 15.65 µs | ⚪ -93.41% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.49 GOP/s | 7.14 GOP/s | 🟢 +186.68% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 9.56 µs | 12.75 µs | ⚪ +33.33% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 522.72 µs | 414.24 µs | ⚪ -20.75% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 263.57 µs | 717.28 µs | ⚪ +172.14% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 843.59 µs | 284.43 µs | ⚪ -66.28% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 2.77 GB/s | 6.46 GB/s | 🟢 +133.21% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 3029.99 µs | 1299.24 µs | 🟢 -57.12% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 550.83 µs | 25.48 µs | ⚪ -95.37% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 0.69 GOP/s | 1.61 GOP/s | 🟢 +133.21% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 678.24 µs | 1163.78 µs | ⚪ +71.59% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.50 GB/s | 1.46 GB/s | 🟢 +188.64% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 4158.06 µs | 1440.57 µs | 🟢 -65.35% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 1008.38 µs | 4.69 µs | ⚪ -99.54% |

