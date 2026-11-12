# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 11.34 µs | 10.56 µs | ⚪ -6.89% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 5.02 µs | 3.03 µs | ⚪ -39.60% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 5.18 µs | 1.22 µs | ⚪ -76.41% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.36 µs | 10.05 µs | ⚪ +324.93% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.47 µs | 2.25 µs | ⚪ -8.89% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 13.15 µs | 1.94 µs | ⚪ -85.22% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 3.55 µs | 2.10 µs | ⚪ -40.68% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.42 µs | 7.25 µs | ⚪ +111.98% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 10.49 µs | 159.35 µs | ⚪ +1419.11% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 12.80 GB/s | 8.56 GB/s | 🔴 -33.18% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 1965.45 µs | 2941.28 µs | 🔴 +49.65% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 4.56 µs | 25.53 µs | ⚪ +459.42% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 8740.92 GOP/s | 5840.96 GOP/s | 🔴 -33.18% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 2.75 µs | 9.70 µs | ⚪ +252.67% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 14.45 µs | 3.56 µs | ⚪ -75.39% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 3.40 µs | 4.27 µs | ⚪ +25.66% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 3.99 µs | 1.36 µs | ⚪ -66.00% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.51 µs | 7.11 µs | ⚪ +102.88% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.00 µs | 2.44 µs | ⚪ -51.23% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 9.39 µs | 5.99 µs | ⚪ -36.21% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 20.61 µs | 27.91 µs | ⚪ +35.41% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 77.12 µs | 19.76 µs | ⚪ -74.38% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 132.75 µs | 78.34 µs | ⚪ -40.98% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 2.50 µs | 3.75 µs | ⚪ +50.13% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 2.81 µs | 7.95 µs | ⚪ +182.69% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.62 µs | 2.72 µs | ⚪ -51.53% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.55 µs | 3.61 µs | ⚪ +41.42% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.75 µs | 7.63 µs | ⚪ +335.39% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 10.46 µs | 17.01 µs | ⚪ +62.54% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 2.26 µs | 2.76 µs | ⚪ +21.68% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 9.16 µs | 2.70 µs | ⚪ -70.52% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.26 µs | 4.45 µs | ⚪ -15.25% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.16 µs | 1.26 µs | ⚪ +8.69% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 1.50 µs | 20.11 µs | ⚪ +1238.34% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 4.84 µs | 1.67 µs | ⚪ -65.45% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.96 µs | 2.81 µs | ⚪ +43.27% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.92 µs | 2.64 µs | ⚪ +37.60% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.32 µs | 3.15 µs | ⚪ -40.93% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 4.78 GB/s | 5.04 GB/s | 🟢 +5.38% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 438.88 µs | 416.48 µs | 🟢 -5.10% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 3.63 µs | 14.95 µs | ⚪ +311.69% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 35.93 µs | 21.84 µs | ⚪ -39.23% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.29 µs | 2.36 µs | ⚪ +82.41% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 4.91 µs | 11.62 µs | ⚪ +136.49% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 4.48 µs | 3.56 µs | ⚪ -20.66% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 5.53 µs | 9.49 µs | ⚪ +71.80% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 10.31 µs | 11.26 µs | ⚪ +9.19% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 2.91 µs | 9.97 µs | ⚪ +243.05% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 4.27 µs | 8.25 µs | ⚪ +92.98% |

