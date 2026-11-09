# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 1.84 µs | 3.24 µs | ⚪ +76.26% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 4.78 µs | 15.16 µs | ⚪ +217.33% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.32 µs | 1.82 µs | ⚪ +38.35% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 4.53 µs | 3.09 µs | ⚪ -31.75% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.74 µs | 7.68 µs | ⚪ +180.70% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.14 µs | 2.39 µs | ⚪ +11.66% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 8.38 µs | 12.13 µs | ⚪ +44.80% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 12.75 GB/s | 9.01 GB/s | 🔴 -29.36% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 1973.39 µs | 2793.49 µs | 🔴 +41.56% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 4.39 µs | 66.09 µs | ⚪ +1406.00% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 8705.76 GOP/s | 6149.96 GOP/s | 🔴 -29.36% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 16.66 µs | 1.91 µs | ⚪ -88.55% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 14.05 µs | 9.83 µs | ⚪ -30.00% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 15.43 µs | 2.00 µs | ⚪ -87.01% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 6.28 µs | 5.13 µs | ⚪ -18.29% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.56 µs | 3.16 µs | ⚪ +23.06% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 3.99 µs | 7.93 µs | ⚪ +98.61% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 44.85 µs | 3.60 µs | ⚪ -91.98% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 46.47 µs | 61.24 µs | ⚪ +31.79% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 3.67 µs | 5.46 µs | ⚪ +49.03% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.25 µs | 1.77 µs | ⚪ +41.20% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 0.70 µs | 0.97 µs | ⚪ +37.92% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.50 µs | 6.88 µs | ⚪ +25.03% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 6.50 µs | 2.28 µs | ⚪ -64.96% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 10.18 µs | 3.44 µs | ⚪ -66.25% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 12.15 µs | 2.74 µs | ⚪ -77.45% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 2.65 µs | 3.80 µs | ⚪ +43.71% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.13 µs | 7.36 µs | ⚪ -9.43% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.34 µs | 13.33 µs | ⚪ +81.53% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 3.47 µs | 1.92 µs | ⚪ -44.60% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 2.59 µs | 12.42 µs | ⚪ +378.55% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 5.08 µs | 8.28 µs | ⚪ +62.76% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.45 µs | 3.96 µs | ⚪ +61.75% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 3.04 µs | 1.78 µs | ⚪ -41.52% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.97 µs | 4.41 µs | ⚪ -44.62% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 4.19 µs | 6.11 µs | ⚪ +45.93% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 14.84 µs | 5.50 µs | ⚪ -62.91% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 5.07 µs | 6.07 µs | ⚪ +19.65% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 3.81 µs | 13.85 µs | ⚪ +263.66% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 11.69 µs | 9.06 µs | ⚪ -22.49% |

