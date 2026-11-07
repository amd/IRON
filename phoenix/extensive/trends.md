# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 395.84 µs | 1191.68 µs | ⚪ +201.05% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 272.69 µs | 335.16 µs | ⚪ +22.91% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 699.81 µs | 43.91 µs | ⚪ -93.73% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 10.33 µs | 22.51 µs | ⚪ +117.93% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 16.03 µs | 8.59 µs | ⚪ -46.44% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 441.71 µs | 316.61 µs | ⚪ -28.32% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 4.41 µs | 7.29 µs | ⚪ +65.35% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 239.49 µs | 417.50 µs | ⚪ +74.33% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 517.82 µs | 668.44 µs | ⚪ +29.09% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 8.31 µs | 159.74 µs | ⚪ +1822.14% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 432.03 µs | 500.66 µs | ⚪ +15.89% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 97.54 µs | 241.02 µs | ⚪ +147.11% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 7.19 µs | 43.59 µs | ⚪ +506.30% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 332.64 µs | 825.71 µs | ⚪ +148.23% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 30.08 GB/s | 10.19 GB/s | 🔴 -66.12% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1115.46 µs | 3292.23 µs | 🔴 +195.15% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 15.80 µs | 400.86 µs | ⚪ +2437.91% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 45.12 GOP/s | 15.29 GOP/s | 🔴 -66.12% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 21.02 GB/s | 6.64 GB/s | 🔴 -68.42% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 997.49 µs | 3158.70 µs | 🔴 +216.66% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 17.93 µs | 149.86 µs | ⚪ +735.88% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 1.31 GOP/s | 0.41 GOP/s | 🔴 -68.42% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 337.97 µs | 238.82 µs | ⚪ -29.34% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 96.77 µs | 107.60 µs | ⚪ +11.19% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 81.54 µs | 94.09 µs | ⚪ +15.38% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 44.15 µs | 115.30 µs | ⚪ +161.16% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 8.39 µs | 3.74 µs | ⚪ -55.46% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 20.69 µs | 7.20 µs | ⚪ -65.20% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 27.81 GB/s | 10.65 GB/s | 🔴 -61.69% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1206.89 µs | 3150.72 µs | 🔴 +161.06% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 41.03 µs | 854.21 µs | ⚪ +1981.79% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 27.80 GOP/s | 10.65 GOP/s | 🔴 -61.69% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.47 GB/s | 28.41 GB/s | 🟢 +171.31% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3203.99 µs | 1180.91 µs | 🟢 -63.14% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 327.64 µs | 146.62 µs | ⚪ -55.25% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 10.47 GOP/s | 28.41 GOP/s | 🟢 +171.31% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.97 GB/s | 10.57 GB/s | 🔴 -64.74% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1119.68 µs | 3175.34 µs | 🔴 +183.59% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 25.97 µs | 303.61 µs | ⚪ +1069.16% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.49 GOP/s | 2.64 GOP/s | 🔴 -64.74% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 341.45 µs | 183.95 µs | ⚪ -46.13% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 84.00 µs | 88.22 µs | ⚪ +5.02% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 32.04 µs | 56.63 µs | ⚪ +76.74% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 284.03 µs | 535.23 µs | ⚪ +88.44% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.32 GB/s | 13.38 GB/s | 🔴 -52.76% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 75.42 µs | 913.70 µs | ⚪ +1111.52% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.08 GOP/s | 3.34 GOP/s | 🔴 -52.76% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 38.70 µs | 10.43 µs | ⚪ -73.05% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 184.43 µs | 491.60 µs | ⚪ +166.55% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 419.38 µs | 350.95 µs | ⚪ -16.32% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 9.91 GB/s | 28.44 GB/s | 🟢 +187.04% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3386.04 µs | 1179.64 µs | 🟢 -65.16% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 325.35 µs | 67.02 µs | ⚪ -79.40% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.48 GOP/s | 7.11 GOP/s | 🟢 +187.04% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 29.22 µs | 44.76 µs | ⚪ +53.20% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.70 GB/s | 11.62 GB/s | 🔴 -60.89% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1129.84 µs | 2888.60 µs | 🔴 +155.66% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 14.31 µs | 863.08 µs | ⚪ +5932.38% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.42 GOP/s | 2.90 GOP/s | 🔴 -60.89% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.44 GB/s | 0.49 GB/s | 🔴 -65.88% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1457.49 µs | 4271.43 µs | 🔴 +193.07% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 296.84 µs | 147.04 µs | ⚪ -50.47% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 511.30 µs | 585.14 µs | ⚪ +14.44% |

