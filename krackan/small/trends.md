# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 2.00 µs | 10.78 µs | ⚪ +438.31% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 7.04 µs | 2.20 µs | ⚪ -68.78% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 2.30 µs | 1.97 µs | ⚪ -14.37% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.76 µs | 2.51 µs | ⚪ -9.07% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.07 µs | 10.49 µs | ⚪ +241.58% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 4.51 µs | 3.09 µs | ⚪ -31.54% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 1.79 µs | 2.09 µs | ⚪ +16.44% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.51 µs | 7.26 µs | ⚪ +188.67% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 8.88 GB/s | 8.37 GB/s | 🔴 -5.66% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 2834.95 µs | 3004.88 µs | 🔴 +5.99% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 6060.03 GOP/s | 5717.32 GOP/s | 🔴 -5.66% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 6.28 µs | 3.58 µs | ⚪ -42.98% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 5.82 µs | 1.57 µs | ⚪ -72.96% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 4.28 µs | 8.12 µs | ⚪ +89.69% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 2.70 µs | 4.11 µs | ⚪ +51.85% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 8.14 µs | 9.03 µs | ⚪ +10.96% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.88 µs | 7.67 µs | ⚪ +97.81% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 10.84 µs | 6.38 µs | ⚪ -41.15% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 16.82 µs | 30.19 µs | ⚪ +79.48% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 11.34 µs | 41.73 µs | ⚪ +268.09% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 1.99 µs | 1.87 µs | ⚪ -6.02% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 7.12 µs | 2.08 µs | ⚪ -70.74% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 5.39 µs | 2.11 µs | ⚪ -60.75% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.47 µs | 3.96 µs | ⚪ -47.05% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 28.93 µs | 13.81 µs | ⚪ -52.26% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 2.06 µs | 2.94 µs | ⚪ +42.81% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Bandwidth` | 55.97 GB/s | 60.16 GB/s | 🟢 +7.49% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency` | 150.02 µs | 139.57 µs | 🟢 -6.97% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 2.37 µs | 3.31 µs | ⚪ +39.59% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Throughput` | 41.94 GOP/s | 45.08 GOP/s | 🟢 +7.49% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.48 µs | 2.35 µs | ⚪ -68.58% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.59 µs | 3.50 µs | ⚪ -59.25% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.76 µs | 0.85 µs | ⚪ -51.56% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 14.52 µs | 2.85 µs | ⚪ -80.38% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 6.09 µs | 3.15 µs | ⚪ -48.32% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.25 µs | 7.78 µs | ⚪ +48.18% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 2.33 µs | 1.25 µs | ⚪ -46.34% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 8.15 µs | 3.97 µs | ⚪ -51.23% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 5.02 GB/s | 4.76 GB/s | 🔴 -5.11% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 417.99 µs | 440.48 µs | 🔴 +5.38% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 12.83 µs | 8.04 µs | ⚪ -37.29% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 14.78 µs | 12.80 µs | ⚪ -13.42% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 16.60 µs | 6.39 µs | ⚪ -61.48% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 7.39 µs | 1.98 µs | ⚪ -73.24% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 5.02 µs | 3.13 µs | ⚪ -37.68% |

