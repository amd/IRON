# Performance trends

**Operators added:** `mha_prefill_lxl`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 12.69 µs | 10.53 µs | ⚪ -17.05% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 5.14 µs | 11.09 µs | ⚪ +115.49% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 1.99 µs | 3.35 µs | ⚪ +68.48% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 6.80 µs | 4.05 µs | ⚪ -40.42% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 9.63 µs | 11.52 µs | ⚪ +19.60% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 7.55 µs | 2.31 µs | ⚪ -69.34% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 9.09 µs | 2.22 µs | ⚪ -75.52% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.64 µs | 2.12 µs | ⚪ -19.53% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 8.77 GB/s | 6.90 GB/s | 🔴 -21.40% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 2868.36 µs | 3649.38 µs | 🔴 +27.23% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 11.64 µs | 35.91 µs | ⚪ +208.57% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 5989.44 GOP/s | 4707.61 GOP/s | 🔴 -21.40% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 3.86 µs | 17.00 µs | ⚪ +340.01% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 1.90 µs | 8.73 µs | ⚪ +359.58% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 4.92 µs | 8.36 µs | ⚪ +69.90% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 2.22 µs | 3.40 µs | ⚪ +52.95% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 16.09 µs | 4.46 µs | ⚪ -72.28% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 5.99 µs | 10.80 µs | ⚪ +80.33% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 35.06 µs | 25.69 µs | ⚪ -26.71% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 37.63 µs | 44.89 µs | ⚪ +19.31% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 7.19 µs | 1.11 µs | ⚪ -84.60% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.67 µs | 1.86 µs | ⚪ +11.09% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 2.17 µs | 2.62 µs | ⚪ +21.02% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 7.74 µs | 5.52 µs | ⚪ -28.63% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.45 µs | 4.61 µs | ⚪ +87.98% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 6.96 µs | 6.44 µs | ⚪ -7.55% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 33.75 µs | 30.30 µs | ⚪ -10.21% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.20 µs | 11.80 µs | ⚪ +885.14% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.52 µs | 1.74 µs | ⚪ +14.45% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 1.93 µs | 4.77 µs | ⚪ +147.26% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.84 µs | 13.57 µs | ⚪ +73.21% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 11.36 µs | 1.50 µs | ⚪ -86.81% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 9.40 µs | 7.12 µs | ⚪ -24.19% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 6.94 µs | 5.41 µs | ⚪ -22.01% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.03 µs | 3.37 µs | ⚪ -32.98% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 0.73 µs | 0.99 µs | ⚪ +35.77% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.79 µs | 8.34 µs | ⚪ +74.17% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 10.23 µs | 14.53 µs | ⚪ +42.03% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 8.42 µs | 2.24 µs | ⚪ -73.34% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 9.19 µs | 8.41 µs | ⚪ -8.56% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 1.71 µs | 17.58 µs | ⚪ +929.51% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 3.72 µs | 5.23 µs | ⚪ +40.65% |

