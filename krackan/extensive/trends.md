# Performance trends

**Operators added:** `merge_results`

**Operators dropped:** `pre_push_hook`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 3.16 µs | 2.40 µs | ⚪ -23.99% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 3.99 µs | 4.85 µs | ⚪ +21.45% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 2.25 µs | 6.39 µs | ⚪ +183.36% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.51 µs | 3.51 µs | ⚪ +40.15% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 10.93 µs | 8.14 µs | ⚪ -25.52% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.47 µs | 3.57 µs | ⚪ +44.10% |
| `Emit` | `npu2-Emit-eight_carried` | `Bandwidth` | 0.12 GB/s | 0.13 GB/s | 🟢 +10.30% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency` | 16.90 µs | 15.32 µs | 🟢 -9.34% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.16 µs | 0.74 µs | ⚪ -65.97% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.83 µs | 3.49 µs | ⚪ -27.79% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 8.75 GB/s | 6.80 GB/s | 🔴 -22.26% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 2875.61 µs | 3698.89 µs | 🔴 +28.63% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 10.51 µs | 39.52 µs | ⚪ +276.00% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 5974.33 GOP/s | 4644.60 GOP/s | 🔴 -22.26% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 5.83 µs | 15.08 µs | ⚪ +158.82% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 11.21 µs | 2.11 µs | ⚪ -81.18% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 15.50 µs | 16.53 µs | ⚪ +6.66% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 3.60 µs | 4.11 µs | ⚪ +14.36% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 2.44 µs | 17.27 µs | ⚪ +607.87% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.15 µs | 5.29 µs | ⚪ +27.51% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.46 µs | 18.73 µs | ⚪ +320.11% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 73.19 µs | 46.39 µs | ⚪ -36.62% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 122.15 µs | 161.11 µs | ⚪ +31.90% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 8.59 µs | 1.71 µs | ⚪ -80.06% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.43 µs | 1.82 µs | ⚪ +27.25% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Bandwidth` | 0.70 GB/s | 0.66 GB/s | 🔴 -5.92% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 73.40 µs | 78.02 µs | 🔴 +6.29% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.68 µs | 1.95 µs | ⚪ +16.15% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 4.96 µs | 4.28 µs | ⚪ -13.74% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.11 µs | 5.67 µs | ⚪ +82.39% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 15.76 µs | 20.98 µs | ⚪ +33.16% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 3.94 µs | 1.08 µs | ⚪ -72.68% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.74 µs | 1.91 µs | ⚪ +10.10% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.06 µs | 2.78 µs | ⚪ -60.60% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.98 µs | 5.34 µs | ⚪ -23.52% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 2.38 µs | 1.56 µs | ⚪ -34.31% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 4.78 µs | 6.97 µs | ⚪ +45.66% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 5.86 µs | 6.44 µs | ⚪ +9.92% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.93 µs | 1.78 µs | ⚪ -39.16% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.75 µs | 2.52 µs | ⚪ +44.42% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 23.50 µs | 2.40 µs | ⚪ -89.77% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 13.43 µs | 17.02 µs | ⚪ +26.80% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 31.86 µs | 28.81 µs | ⚪ -9.57% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 4.59 µs | 20.84 µs | ⚪ +353.74% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 12.23 µs | 14.48 µs | ⚪ +18.43% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Bandwidth` | 5.53 GB/s | 20.58 GB/s | 🟢 +272.38% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency` | 1707.75 µs | 458.60 µs | 🟢 -73.15% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Throughput` | 1259.95 GOP/s | 4691.81 GOP/s | 🟢 +272.38% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Bandwidth` | 5.69 GB/s | 4.76 GB/s | 🔴 -16.35% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency` | 921.73 µs | 1101.87 µs | 🔴 +19.54% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Throughput` | 2329.83 GOP/s | 1948.95 GOP/s | 🔴 -16.35% |

