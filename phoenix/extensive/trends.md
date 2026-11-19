# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 31.12 GB/s | 16.59 GB/s | 🔴 -46.68% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 1617.31 µs | 3033.36 µs | 🔴 +87.56% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 113.85 µs | 451.53 µs | ⚪ +296.58% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 10.37 GOP/s | 5.53 GOP/s | 🔴 -46.68% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 790.30 µs | 332.05 µs | ⚪ -57.98% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 205.56 µs | 236.26 µs | ⚪ +14.94% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 13.18 µs | 7.52 µs | ⚪ -42.95% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 328.73 µs | 686.86 µs | ⚪ +108.94% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 150.34 µs | 57.75 µs | ⚪ -61.59% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 7.40 µs | 5.01 µs | ⚪ -32.34% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 714.70 µs | 267.34 µs | ⚪ -62.59% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 116.60 µs | 722.56 µs | ⚪ +519.70% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 21.02 µs | 401.19 µs | ⚪ +1808.63% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 10.20 GB/s | 15.80 GB/s | 🟢 +54.94% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 3291.68 µs | 2124.42 µs | 🟢 -35.46% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 499.87 µs | 27.62 µs | ⚪ -94.47% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 10.19 GOP/s | 15.79 GOP/s | 🟢 +54.94% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 284.53 µs | 439.35 µs | ⚪ +54.41% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 10.64 GB/s | 27.25 GB/s | 🟢 +156.24% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 3157.02 µs | 1232.05 µs | 🟢 -60.97% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 581.72 µs | 15.42 µs | ⚪ -97.35% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 10.63 GOP/s | 27.23 GOP/s | 🟢 +156.24% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 287.12 µs | 618.12 µs | ⚪ +115.28% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 28.60 GB/s | 13.96 GB/s | 🔴 -51.19% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 108.49 µs | 862.71 µs | ⚪ +695.17% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 42.90 GOP/s | 20.94 GOP/s | 🔴 -51.19% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 14.80 µs | 28.41 µs | ⚪ +91.90% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 256.83 µs | 203.21 µs | ⚪ -20.88% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 60.68 µs | 109.58 µs | ⚪ +80.60% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 68.35 µs | 96.53 µs | ⚪ +41.23% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 90.66 µs | 283.90 µs | ⚪ +213.15% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 14.96 µs | 9.48 µs | ⚪ -36.60% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 215.67 µs | 957.88 µs | ⚪ +344.13% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 346.27 µs | 651.51 µs | ⚪ +88.15% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 374.50 µs | 297.64 µs | ⚪ -20.52% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 156.15 µs | 55.71 µs | ⚪ -64.32% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 15.03 µs | 29.76 µs | ⚪ +97.93% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.28 GB/s | 11.13 GB/s | 🔴 -60.66% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1186.81 µs | 3016.86 µs | 🔴 +154.20% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 34.45 µs | 512.91 µs | ⚪ +1388.63% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.07 GOP/s | 2.78 GOP/s | 🔴 -60.66% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 8.49 µs | 355.99 µs | ⚪ +4095.08% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 7.52 µs | 21.20 µs | ⚪ +181.93% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 104.35 µs | 298.34 µs | ⚪ +185.90% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 328.80 µs | 197.28 µs | ⚪ -40.00% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 1370.95 µs | 311.95 µs | ⚪ -77.25% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 5.96 GB/s | 2.81 GB/s | 🔴 -52.83% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 1406.75 µs | 2982.33 µs | 🔴 +112.00% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 278.18 µs | 457.06 µs | ⚪ +64.30% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 1.49 GOP/s | 0.70 GOP/s | 🔴 -52.83% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.49 GB/s | 1.48 GB/s | 🟢 +198.44% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 4239.06 µs | 1420.40 µs | 🟢 -66.49% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 208.48 µs | 247.73 µs | ⚪ +18.82% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 304.65 µs | 564.49 µs | ⚪ +85.29% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 716.10 µs | 600.84 µs | ⚪ -16.10% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 893.19 µs | 353.37 µs | ⚪ -60.44% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 1043.62 µs | 372.99 µs | ⚪ -64.26% |

