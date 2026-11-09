# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 3.24 µs | 12.69 µs | ⚪ +291.61% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 7.14 µs | 5.14 µs | ⚪ -27.98% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 15.16 µs | 1.99 µs | ⚪ -86.88% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.82 µs | 6.80 µs | ⚪ +273.05% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.09 µs | 9.63 µs | ⚪ +211.71% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.39 µs | 9.09 µs | ⚪ +279.55% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 12.13 µs | 2.64 µs | ⚪ -78.23% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 66.09 µs | 11.64 µs | ⚪ -82.39% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 1.91 µs | 14.79 µs | ⚪ +675.14% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 9.83 µs | 3.86 µs | ⚪ -60.71% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 2.00 µs | 1.90 µs | ⚪ -5.24% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.13 µs | 2.22 µs | ⚪ -56.64% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.16 µs | 16.09 µs | ⚪ +409.58% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 7.93 µs | 5.99 µs | ⚪ -24.50% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.60 µs | 35.06 µs | ⚪ +874.62% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 61.24 µs | 37.63 µs | ⚪ -38.56% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 5.46 µs | 7.19 µs | ⚪ +31.63% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.77 µs | 1.67 µs | ⚪ -5.40% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 0.97 µs | 2.17 µs | ⚪ +124.19% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 6.88 µs | 7.74 µs | ⚪ +12.46% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.28 µs | 2.45 µs | ⚪ +7.72% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.44 µs | 6.96 µs | ⚪ +102.60% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 19.78 µs | 33.75 µs | ⚪ +70.64% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 2.74 µs | 1.20 µs | ⚪ -56.27% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 3.80 µs | 1.52 µs | ⚪ -59.96% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.36 µs | 1.93 µs | ⚪ -73.79% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 13.33 µs | 7.84 µs | ⚪ -41.23% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.92 µs | 11.36 µs | ⚪ +490.43% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 12.42 µs | 9.40 µs | ⚪ -24.33% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.28 µs | 6.94 µs | ⚪ -16.10% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.96 µs | 5.03 µs | ⚪ +26.94% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.78 µs | 0.73 µs | ⚪ -58.90% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.41 µs | 4.79 µs | ⚪ +8.51% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 6.11 µs | 10.23 µs | ⚪ +67.37% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 5.50 µs | 8.42 µs | ⚪ +52.88% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 6.07 µs | 9.19 µs | ⚪ +51.39% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 13.85 µs | 1.71 µs | ⚪ -87.66% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 9.06 µs | 3.72 µs | ⚪ -58.93% |

