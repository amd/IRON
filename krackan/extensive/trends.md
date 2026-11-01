# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 2.40 µs | 2.61 µs | ⚪ +8.61% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 4.85 µs | 4.48 µs | ⚪ -7.54% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 6.39 µs | 8.29 µs | ⚪ +29.72% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 3.51 µs | 1.97 µs | ⚪ -43.91% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.14 µs | 9.03 µs | ⚪ +10.88% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.57 µs | 2.48 µs | ⚪ -30.46% |
| `Emit` | `npu2-Emit-eight_carried` | `Bandwidth` | 0.13 GB/s | 0.11 GB/s | 🔴 -16.67% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency` | 15.32 µs | 18.38 µs | 🔴 +20.01% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 0.74 µs | 1.50 µs | ⚪ +103.39% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.49 µs | 6.90 µs | ⚪ +97.98% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 7.37 µs | 454.91 µs | ⚪ +6069.59% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 39.52 µs | 19.22 µs | ⚪ -51.37% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 15.08 µs | 1.76 µs | ⚪ -88.34% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 2.11 µs | 1.55 µs | ⚪ -26.38% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 16.53 µs | 9.52 µs | ⚪ -42.40% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 4.11 µs | 3.12 µs | ⚪ -24.13% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 17.27 µs | 4.37 µs | ⚪ -74.67% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.29 µs | 2.05 µs | ⚪ -61.21% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 6.03 µs | 3.17 µs | ⚪ -47.51% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 18.73 µs | 16.08 µs | ⚪ -14.17% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 46.39 µs | 70.85 µs | ⚪ +52.73% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 161.11 µs | 102.28 µs | ⚪ -36.51% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 1.71 µs | 1.28 µs | ⚪ -25.42% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.17 GB/s | 0.18 GB/s | 🟢 +9.61% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 98.75 µs | 90.09 µs | 🟢 -8.77% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.82 µs | 3.34 µs | ⚪ +83.25% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.95 µs | 1.01 µs | ⚪ -48.36% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 4.28 µs | 7.10 µs | ⚪ +65.94% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.41 µs | 2.27 µs | ⚪ -33.32% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.67 µs | 3.27 µs | ⚪ -42.36% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 20.98 µs | 60.33 µs | ⚪ +187.50% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.08 µs | 7.01 µs | ⚪ +550.74% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.91 µs | 1.70 µs | ⚪ -11.00% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 2.78 µs | 11.12 µs | ⚪ +299.80% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.34 µs | 7.92 µs | ⚪ +48.39% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.56 µs | 0.72 µs | ⚪ -54.19% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 6.97 µs | 6.27 µs | ⚪ -10.06% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 6.44 µs | 4.63 µs | ⚪ -28.09% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.78 µs | 5.00 µs | ⚪ +180.40% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 2.52 µs | 3.90 µs | ⚪ +54.57% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.40 µs | 2.97 µs | ⚪ +23.73% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 17.02 µs | 14.14 µs | ⚪ -16.92% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 28.81 µs | 42.43 µs | ⚪ +47.26% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 2.31 µs | 2.47 µs | ⚪ +6.94% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.60 µs | 3.14 µs | ⚪ -12.81% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 20.84 µs | 4.81 µs | ⚪ -76.93% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 14.48 µs | 10.24 µs | ⚪ -29.30% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Bandwidth` | 20.58 GB/s | 10.33 GB/s | 🔴 -49.80% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency` | 458.60 µs | 913.47 µs | 🔴 +99.19% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Throughput` | 4691.81 GOP/s | 2355.49 GOP/s | 🔴 -49.80% |

