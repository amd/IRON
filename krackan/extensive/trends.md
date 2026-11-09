# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 14.29 µs | 8.41 µs | ⚪ -41.15% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 2.06 µs | 7.23 µs | ⚪ +251.42% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 4.97 µs | 3.63 µs | ⚪ -26.91% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 7.24 µs | 8.50 µs | ⚪ +17.44% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 12.91 µs | 12.12 µs | ⚪ -6.09% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.43 µs | 2.68 µs | ⚪ +10.29% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.10 µs | 7.71 µs | ⚪ +149.07% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Bandwidth` | 11.68 GB/s | 10.66 GB/s | 🔴 -8.68% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency` | 2963.00 µs | 3244.60 µs | 🔴 +9.50% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 2.33 µs | 5.08 µs | ⚪ +118.22% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Throughput` | 6522.91 GOP/s | 5956.77 GOP/s | 🔴 -8.68% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 6.73 GB/s | 12.77 GB/s | 🟢 +89.65% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 3738.07 µs | 1971.03 µs | 🟢 -47.27% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 64.13 µs | 3.16 µs | ⚪ -95.07% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 4595.92 GOP/s | 8716.17 GOP/s | 🟢 +89.65% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 15.53 µs | 1.62 µs | ⚪ -89.58% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 9.11 µs | 2.95 µs | ⚪ -67.67% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 16.65 µs | 7.05 µs | ⚪ -57.64% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 3.36 µs | 4.19 µs | ⚪ +24.94% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.07 µs | 11.38 µs | ⚪ +124.20% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 8.48 µs | 7.01 µs | ⚪ -17.37% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.10 µs | 29.15 µs | ⚪ +610.38% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 35.24 µs | 64.96 µs | ⚪ +84.33% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 88.85 µs | 62.39 µs | ⚪ -29.78% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 2.60 µs | 2.07 µs | ⚪ -20.27% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.14 µs | 2.26 µs | ⚪ +98.21% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.85 µs | 1.07 µs | ⚪ -41.98% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 7.25 µs | 7.67 µs | ⚪ +5.80% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.13 µs | 1.10 µs | ⚪ -64.96% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.67 µs | 3.64 µs | ⚪ -22.09% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 6.67 µs | 28.18 µs | ⚪ +322.65% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.07 µs | 3.31 µs | ⚪ +208.30% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.99 µs | 1.19 µs | ⚪ -40.22% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.21 µs | 7.37 µs | ⚪ +18.70% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 12.13 µs | 3.30 µs | ⚪ -72.84% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 2.21 µs | 1.69 µs | ⚪ -23.53% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Bandwidth` | 0.57 GB/s | 0.54 GB/s | 🔴 -5.30% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency` | 1429.40 µs | 1509.37 µs | 🔴 +5.59% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 5.48 µs | 8.93 µs | ⚪ +62.99% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Throughput` | 14.67 GOP/s | 13.89 GOP/s | 🔴 -5.30% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.88 µs | 7.00 µs | ⚪ +142.98% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 30.88 µs | 12.40 µs | ⚪ -59.85% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.51 µs | 1.39 µs | ⚪ -7.90% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.29 µs | 3.65 µs | ⚪ +183.50% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 4.67 GB/s | 4.21 GB/s | 🔴 -9.81% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 449.27 µs | 498.12 µs | 🔴 +10.87% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 2.27 µs | 15.12 µs | ⚪ +566.16% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 0.86 µs | 1.69 µs | ⚪ +96.40% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 1.64 µs | 2.55 µs | ⚪ +55.69% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 2.43 µs | 6.19 µs | ⚪ +154.84% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 9.83 µs | 12.37 µs | ⚪ +25.84% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 12.41 µs | 13.85 µs | ⚪ +11.55% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 4.47 µs | 6.87 µs | ⚪ +53.53% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 18.06 µs | 10.32 µs | ⚪ -42.85% |

