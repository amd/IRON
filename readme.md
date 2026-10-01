# IRON - CI Summary

## Examples

<details>
<summary>iron/applications/llama_3.2_1b</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_1] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_40] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_1] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_40] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter0] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter1] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter2] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter3] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter4] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter0] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter1] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter2] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter3] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter4] | ✅ | - | - | - |

</details>

## Small

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | ✅ | 178.74 | ✅ | 438.08 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 203.74 | ✅ | 426.22 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_1.003] | ✅ | 159.24 | ✅ | 332.16 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 180.88 | ✅ | 451.84 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_1.003] | ✅ | 218.98 | ✅ | 362.72 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 198.80 | ✅ | 389.74 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_1.003] | ✅ | 201.42 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 212.76 | - | - |
| test_axpy[input_length_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 2961.32 |
| test_axpy[input_length_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0] | ✅ | 901.28 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 148.28 | ✅ | 338.92 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 132.60 | ✅ | 341.34 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 137.44 | ✅ | 389.02 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 146.72 | ✅ | 589.12 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 144.90 | ✅ | 348.26 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 169.50 | ✅ | 492.96 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 192.70 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 204.80 | - | - |
| test_dequant[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-group_size_32] | - | - | ✅ | 1233.24 |
| test_dequant[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-group_size_32] | ✅ | 460.20 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 179.14 | ✅ | 667.32 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 161.66 | ✅ | 440.80 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 177.52 | ✅ | 391.22 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 178.30 | - | - |
| test_elementwise_add[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 4193.20 |
| test_elementwise_add[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 979.54 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 156.28 | ✅ | 388.92 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 170.46 | ✅ | 477.10 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 191.76 | ✅ | 455.40 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 224.18 | - | - |
| test_elementwise_mul[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 3872.52 |
| test_elementwise_mul[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 879.72 | - | - |

</details>

<details>
<summary>iron/operators/flm/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gate_up_interleaved_blob[iter0] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter1] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter2] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter3] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter4] | ✅ | - | - | - |
| test_large_k_shapes[K_4096-N_1536] | ✅ | - | - | - |
| test_large_k_shapes[K_6144-N_1536] | ✅ | - | - | - |
| test_matches_reference[K_1024-N_128] | ✅ | - | - | - |
| test_matches_reference[K_1024-N_512] | ✅ | - | - | - |
| test_matches_reference[K_1536-N_640] | ✅ | - | - | - |
| test_matches_reference[K_2048-N_256] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter0] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter1] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter2] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter3] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter4] | ✅ | - | - | - |
| test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of] | ✅ | - | ✅ | - |
| test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of] | ✅ | - | ✅ | - |
| test_rejects_unservable_shapes[K_512-N_128-exc_<class 'NotImplementedError'>-match_tile_n] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | ✅ | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | ✅ | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 372.00 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 301.12 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 358.06 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 313.18 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 362.92 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 326.58 | ✅ | 724.94 |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 353.74 | - | - |
| test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 706.38 |
| test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 673.16 |
| test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even] | - | - | ✅ | 1403.66 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | - | - | ✅ | 738.32 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor] | - | - | ✅ | 719.48 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even] | - | - | ✅ | 1011.60 |
| test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 651.76 |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 434.58 | - | - |
| test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 1499.08 |
| test_gemm_split_leg_bounds[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter4] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter4] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma32-default] | - | - | ✅ | - |
| test_gemm_tile_options[tn128-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn16-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma32-default] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter4] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 156.72 | ✅ | 317.98 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 171.60 | ✅ | 437.22 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 177.90 | ✅ | 675.02 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 218.92 | ✅ | 487.24 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 183.00 | ✅ | 455.68 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 188.46 | ✅ | 757.72 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 190.30 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 229.08 | - | - |
| test_gelu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3497.06 |
| test_gelu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 648.82 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-partition_N_1] | ✅ | 2115.68 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-partition_N_1] | ✅ | 247.30 | ✅ | 608.42 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-partition_N_1] | ✅ | 228.54 | ✅ | 576.68 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 47080.22 | ✅ | 82579.64 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 27644.14 | ✅ | 19018.86 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 7721.98 | - | - |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-partition_N_1] | ✅ | 2164.66 | ✅ | 3764.04 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-partition_N_4] | ✅ | 3433.22 | ✅ | 6801.34 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-partition_N_1] | ✅ | 1530.76 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 152.76 | ✅ | 371.10 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2562.60 | ✅ | 9399.94 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 1368.44 | ✅ | 5204.86 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 833.80 | ✅ | 3545.36 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 782.80 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2587.16 | ✅ | 9020.18 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 1367.48 | ✅ | 5147.58 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 845.46 | ✅ | 3578.66 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 766.76 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 464.42 | ✅ | 2501.84 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 344.50 | ✅ | 1365.96 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 236.52 | ✅ | 840.88 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 447.30 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 984.02 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 238.96 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 279.66 | ✅ | 1786.64 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 177.10 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2579.02 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2556.90 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 158.94 | ✅ | 432.74 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 164.62 | ✅ | 419.94 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 179.02 | ✅ | 364.54 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 211.00 | ✅ | 438.28 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 204.10 | ✅ | 426.56 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 188.88 | ✅ | 592.04 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 179.74 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 199.14 | - | - |
| test_layer_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3038.62 |
| test_layer_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 657.66 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 171.14 | ✅ | 383.66 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 159.12 | ✅ | 344.72 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 194.80 | ✅ | 327.44 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 184.50 | ✅ | 446.04 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 164.04 | ✅ | 408.64 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 195.80 | ✅ | 406.52 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 176.02 | ✅ | 657.84 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 195.36 | ✅ | 442.30 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 225.16 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 223.58 | - | - |
| test_leaky_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-alpha_0.01] | - | - | ✅ | 2836.16 |
| test_leaky_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 708.28 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 137.78 | ✅ | 309.26 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 244.44 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 164.98 | ✅ | 259.10 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 187.90 | ✅ | 503.98 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 170.04 | ✅ | 293.36 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 157.62 | ✅ | 410.30 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 194.60 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 207.36 | ✅ | 759.06 |
| test_mem_copy[input_length_8388608-num_cores_16-num_channels_2-bypass_False-tile_size_4096] | ✅ | 843.76 | - | - |
| test_mem_copy[input_length_8388608-num_cores_8-num_channels_2-bypass_False-tile_size_4096] | - | - | ✅ | 1622.16 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | - | ✅ | - |
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | - | ✅ | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 16793.60 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 168.38 | ✅ | 407.96 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 147.28 | ✅ | 414.00 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 162.74 | ✅ | 421.74 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 194.48 | ✅ | 505.62 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 164.72 | ✅ | 455.98 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 177.18 | ✅ | 382.66 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 188.50 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 216.10 | - | - |
| test_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 2903.14 |
| test_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 718.80 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 167.42 | ✅ | 367.98 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 172.20 | ✅ | 293.70 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 220.84 | ✅ | 376.00 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 169.06 | ✅ | 427.22 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 178.38 | ✅ | 444.80 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 187.08 | ✅ | 415.88 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 173.58 | ✅ | 396.42 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 160.62 | ✅ | 370.26 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 180.86 | ✅ | 389.26 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 168.48 | ✅ | 420.54 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 200.48 | ✅ | 537.86 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 161.62 | ✅ | 400.30 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 199.56 | ✅ | 390.56 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 211.14 | ✅ | 505.26 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 211.62 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 204.32 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 199.60 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 217.16 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 2280.30 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_False] | - | - | ✅ | 2982.68 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 657.58 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-weighted_False] | ✅ | 658.08 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 163.18 | ✅ | 412.94 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 176.74 | ✅ | 389.78 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 190.14 | ✅ | 483.70 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 181.48 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 170.94 | ✅ | 403.84 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 194.76 | ✅ | 418.06 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 177.00 | ✅ | 298.22 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 178.96 | - | - |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 1347.10 |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 305.72 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 163.46 | ✅ | 337.62 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 167.96 | ✅ | 371.02 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 164.32 | ✅ | 322.42 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 162.00 | ✅ | 366.34 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 168.68 | ✅ | 431.14 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 213.18 | ✅ | 386.62 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 156.54 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 209.20 | - | - |
| test_sigmoid[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3638.88 |
| test_sigmoid[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 654.64 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 190.88 | ✅ | 627.72 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 168.50 | ✅ | 507.44 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 196.08 | ✅ | 271.38 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 202.14 | - | - |
| test_silu[input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096] | - | - | ✅ | 4817.94 |
| test_silu[input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096] | ✅ | 667.60 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 545.82 | ✅ | 1929.96 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 184.00 | ✅ | 396.58 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 178.06 | ✅ | 497.10 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 193.72 | ✅ | 588.48 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[bench_flat_4mi] | ✅ | 492.82 | ✅ | 1706.18 |
| test_strided_copy[chunked_transfer] | ✅ | 237.10 | ✅ | 278.72 |
| test_strided_copy[contiguous] | ✅ | 188.50 | ✅ | 326.68 |
| test_strided_copy[four_channels] | ✅ | 185.54 | ✅ | 397.02 |
| test_strided_copy[kv_slot0] | ✅ | 173.04 | ✅ | 317.62 |
| test_strided_copy[kv_slot5] | ✅ | 173.94 | ✅ | 375.36 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 202.22 | ✅ | 455.52 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 213.96 | ✅ | 361.92 |
| test_strided_copy[kv_slot_last] | ✅ | 198.48 | ✅ | 299.10 |
| test_strided_copy[two_channels] | ✅ | 187.62 | ✅ | 479.02 |
| test_strided_copy[two_channels_chunked] | ✅ | 184.08 | ✅ | 408.28 |
| test_strided_copy_cache_offset_parameter[iter0] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter1] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter2] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter3] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter4] | ✅ | - | - | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 990.18 | ✅ | 9625.84 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1025.36 | ✅ | 13361.85 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False] | ✅ | 2158.14 | ✅ | 24258.80 |
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True] | ✅ | 2343.00 | ✅ | 21808.33 |
| test_weight_layout_reaches_both_gemms[b_col_maj_False] | ✅ | - | ✅ | - |
| test_weight_layout_reaches_both_gemms[b_col_maj_True] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 194.86 | ✅ | 300.78 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 138.20 | ✅ | 883.98 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 159.92 | ✅ | 456.90 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 168.48 | ✅ | 365.80 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 165.88 | ✅ | 404.28 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 187.74 | ✅ | 529.74 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 169.12 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 201.18 | - | - |
| test_tanh[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3247.72 |
| test_tanh[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 665.62 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_dimension_that_floors_to_zero_is_refused_by_name[M_2048-N_128-aie_columns_8-channels_1-m_256-n_32-bad_num_aie_columns] | ✅ | - | ✅ | - |
| test_a_dimension_that_floors_to_zero_is_refused_by_name[M_256-N_2048-aie_columns_1-channels_2-m_256-n_32-bad_num_channels] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_1] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_2] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_4] | ✅ | - | ✅ | - |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 201.64 | ✅ | 473.36 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 252.88 | ✅ | 2289.94 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 200.80 | ✅ | 453.68 |
| test_transpose[M_8192-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | - | - | ✅ | 3583.84 |
| test_transpose[M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 947.46 | - | - |

</details>

## Extensive

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_1.003] | ✅ | 141.28 | ✅ | 420.02 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0] | ✅ | 163.72 | ✅ | 378.08 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0] | ✅ | 183.56 | ✅ | 353.04 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_1.003] | ✅ | 199.02 | ✅ | 381.04 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0] | ✅ | 157.70 | ✅ | 328.94 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0] | ✅ | 149.74 | ✅ | 383.36 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_1.003] | ✅ | 158.60 | ✅ | 441.16 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0] | ✅ | 149.38 | ✅ | 462.38 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0] | ✅ | 170.82 | ✅ | 489.40 |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_1.003] | ✅ | 167.62 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0] | ✅ | 176.94 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0] | ✅ | 189.48 | - | - |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | ✅ | 196.32 | ✅ | 404.78 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0] | ✅ | 178.02 | ✅ | 323.98 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 163.36 | ✅ | 386.60 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_1.003] | ✅ | 159.84 | ✅ | 412.80 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0] | ✅ | 185.40 | ✅ | 425.20 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 160.88 | ✅ | 341.60 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_1.003] | ✅ | 174.72 | ✅ | 323.82 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0] | ✅ | 155.96 | ✅ | 423.12 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 162.48 | ✅ | 812.06 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_1.003] | ✅ | 205.18 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0] | ✅ | 179.46 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 210.20 | - | - |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_1.003] | ✅ | 185.82 | ✅ | 467.34 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0] | ✅ | 159.42 | ✅ | 373.66 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0] | ✅ | 158.12 | ✅ | 413.22 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_1.003] | ✅ | 184.38 | ✅ | 537.30 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0] | ✅ | 158.88 | ✅ | 361.54 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0] | ✅ | 175.88 | ✅ | 506.80 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_1.003] | ✅ | 181.70 | ✅ | 463.28 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0] | ✅ | 162.36 | ✅ | 684.20 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0] | ✅ | 156.32 | ✅ | 488.62 |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_1.003] | ✅ | 178.78 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0] | ✅ | 194.74 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0] | ✅ | 203.62 | - | - |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_1.003] | ✅ | 174.14 | ✅ | 357.22 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0] | ✅ | 169.58 | ✅ | 348.96 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0] | ✅ | 150.08 | ✅ | 400.36 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_1.003] | ✅ | 173.94 | ✅ | 339.94 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0] | ✅ | 172.68 | ✅ | 529.00 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0] | ✅ | 177.22 | ✅ | 650.24 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_1.003] | ✅ | 166.22 | ✅ | 418.98 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0] | ✅ | 189.80 | ✅ | 489.74 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0] | ✅ | 183.96 | ✅ | 436.26 |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_1.003] | ✅ | 227.00 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0] | ✅ | 196.78 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0] | ✅ | 200.32 | - | - |
| test_axpy[input_length_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 4225.48 |
| test_axpy[input_length_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0] | ✅ | 978.38 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32] | ✅ | 195.82 | ✅ | 338.72 |
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32] | ✅ | 161.28 | ✅ | 379.38 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32] | ✅ | 172.32 | ✅ | 373.54 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32] | ✅ | 154.76 | ✅ | 524.22 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32] | ✅ | 167.24 | ✅ | 527.86 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32] | ✅ | 182.80 | ✅ | 440.04 |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32] | ✅ | 204.36 | - | - |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32] | ✅ | 199.80 | - | - |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 154.60 | ✅ | 338.12 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 148.00 | ✅ | 491.78 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 158.02 | ✅ | 402.68 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 202.32 | ✅ | 727.68 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 175.86 | ✅ | 443.14 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 181.80 | ✅ | 699.60 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 177.70 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 212.52 | - | - |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32] | ✅ | 162.34 | ✅ | 358.74 |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32] | ✅ | 176.40 | ✅ | 467.06 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32] | ✅ | 174.86 | ✅ | 472.38 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32] | ✅ | 181.42 | ✅ | 490.54 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32] | ✅ | 181.24 | ✅ | 630.06 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32] | ✅ | 186.26 | ✅ | 608.66 |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32] | ✅ | 223.06 | - | - |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32] | ✅ | 220.26 | - | - |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32] | ✅ | 188.86 | ✅ | 401.28 |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32] | ✅ | 151.10 | ✅ | 410.54 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32] | ✅ | 180.38 | ✅ | 346.24 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32] | ✅ | 172.02 | ✅ | 477.30 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32] | ✅ | 181.82 | ✅ | 395.86 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32] | ✅ | 172.40 | ✅ | 525.76 |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32] | ✅ | 183.26 | - | - |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32] | ✅ | 222.98 | - | - |
| test_dequant[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-group_size_32] | - | - | ✅ | 1352.98 |
| test_dequant[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-group_size_32] | ✅ | 510.16 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 187.78 | ✅ | 414.92 |
| test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 190.08 | ✅ | 453.82 |
| test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 186.10 | ✅ | 298.98 |
| test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 185.22 | - | - |
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 166.88 | ✅ | 384.76 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 140.76 | ✅ | 430.10 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 182.68 | ✅ | 506.62 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 184.20 | - | - |
| test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 165.02 | ✅ | 652.76 |
| test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 179.96 | ✅ | 370.82 |
| test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 202.30 | ✅ | 482.70 |
| test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 226.78 | - | - |
| test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192] | ✅ | 191.30 | ✅ | 439.22 |
| test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 190.64 | ✅ | 470.52 |
| test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 186.06 | ✅ | 420.10 |
| test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 213.70 | - | - |
| test_elementwise_add[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 3800.26 |
| test_elementwise_add[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 891.10 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 150.50 | ✅ | 368.04 |
| test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 167.66 | ✅ | 400.92 |
| test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 162.82 | ✅ | 461.30 |
| test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 185.84 | - | - |
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 175.28 | ✅ | 435.40 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 169.40 | ✅ | 451.08 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 172.50 | ✅ | 735.82 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 202.30 | - | - |
| test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 167.30 | ✅ | 365.58 |
| test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 176.82 | ✅ | 373.56 |
| test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 156.38 | ✅ | 456.62 |
| test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 161.62 | - | - |
| test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 158.20 | ✅ | 389.76 |
| test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 146.88 | ✅ | 523.22 |
| test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 172.66 | - | - |
| test_elementwise_mul[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 2499.12 |
| test_elementwise_mul[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 858.50 | - | - |

</details>

<details>
<summary>iron/operators/flm/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_e4b_gate_up_interleaved[iter0] | ✅ | - | - | - |
| test_e4b_gate_up_interleaved[iter1] | ✅ | - | - | - |
| test_e4b_gate_up_interleaved[iter2] | ✅ | - | - | - |
| test_e4b_gate_up_interleaved[iter3] | ✅ | - | - | - |
| test_e4b_gate_up_interleaved[iter4] | ✅ | - | - | - |
| test_e4b_shapes[K_10240-N_2560] | ✅ | - | - | - |
| test_e4b_shapes[K_2560-N_10240] | ✅ | - | - | - |
| test_e4b_shapes[K_2560-N_2560] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter0] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter1] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter2] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter3] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter4] | ✅ | - | - | - |
| test_large_k_shapes[K_12288-N_1536] | ✅ | - | - | - |
| test_large_k_shapes[K_4096-N_1536] | ✅ | - | - | - |
| test_large_k_shapes[K_6144-N_1536] | ✅ | - | - | - |
| test_matches_reference[K_1024-N_128] | ✅ | - | - | - |
| test_matches_reference[K_1024-N_512] | ✅ | - | - | - |
| test_matches_reference[K_1536-N_640] | ✅ | - | - | - |
| test_matches_reference[K_2048-N_256] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter0] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter1] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter2] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter3] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter4] | ✅ | - | - | - |
| test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of] | ✅ | - | ✅ | - |
| test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of] | ✅ | - | ✅ | - |
| test_rejects_unservable_shapes[K_512-N_128-exc_<class 'NotImplementedError'>-match_tile_n] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | ✅ | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | ✅ | - |
| test_gemm[M_1024-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 3939.72 | - | - |
| test_gemm[M_1024-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 4593.88 |
| test_gemm[M_1024-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1049.08 | - | - |
| test_gemm[M_1024-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 3970.00 | - | - |
| test_gemm[M_1024-K_2560-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1202.08 | ✅ | 9439.06 |
| test_gemm[M_2048-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 7344.48 | - | - |
| test_gemm[M_2048-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 6388.94 |
| test_gemm[M_2048-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1680.36 | - | - |
| test_gemm[M_2048-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 7739.00 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 349.34 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 357.36 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 318.24 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 340.40 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_sigmoid-clamp_None-rounding_conv_even] | ✅ | 334.00 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 369.98 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_floor] | ✅ | 372.80 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 311.94 | ✅ | 609.20 |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 338.26 | - | - |
| test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 713.90 |
| test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 864.38 |
| test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even] | - | - | ✅ | 866.98 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | - | - | ✅ | 866.08 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor] | - | - | ✅ | 1038.46 |
| test_gemm[M_256-K_512-N_512-epilogue_sigmoid-clamp_None-rounding_conv_even] | - | - | ✅ | 1523.58 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even] | - | - | ✅ | 674.04 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_floor] | - | - | ✅ | 960.98 |
| test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 634.94 |
| test_gemm[M_512-K_1024-N_1024-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even] | - | - | ✅ | 1836.90 |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 470.84 | - | - |
| test_gemm[M_512-K_1024-N_2048-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even] | ✅ | 444.46 | - | - |
| test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 891.18 |
| test_gemm[M_512-K_1536-N_1536-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 494.82 | ✅ | 3197.60 |
| test_gemm_split_leg_bounds[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter4] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter4] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma32-default] | - | - | ✅ | - |
| test_gemm_tile_options[tn128-ma32] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma64] | - | - | ✅ | - |
| test_gemm_tile_options[tn16-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn16-ma32] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn16-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma32] | ✅ | - | ❌ | - |
| test_gemm_tile_options[tn32-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma32-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma64] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter4] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/flm/mm_prebuilt</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mm_prebuilt[M_256-K_512-N_1024-epilogue_gelu-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_1024-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_1024-epilogue_silu-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_1280-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_640-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_512-K_1024-N_2048-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_gelu-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_none-clamp_(-2.0, 2.0)] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_sigmoid-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_silu-clamp_None] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 168.46 | ✅ | 390.44 |
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 194.30 | ✅ | 377.84 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 146.76 | ✅ | 583.08 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 168.96 | ✅ | 559.46 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 179.10 | ✅ | 490.12 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 163.80 | ✅ | 420.72 |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 190.16 | - | - |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 193.88 | - | - |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 172.56 | ✅ | 360.44 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 153.64 | ✅ | 413.54 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 154.52 | ✅ | 447.82 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 182.64 | ✅ | 405.52 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 139.78 | ✅ | 372.18 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 170.24 | ✅ | 518.50 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 157.08 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 225.46 | - | - |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 155.16 | ✅ | 281.24 |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 146.86 | ✅ | 285.14 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 172.60 | ✅ | 325.78 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 166.98 | ✅ | 339.52 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 165.20 | ✅ | 481.58 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 169.28 | ✅ | 583.00 |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 155.46 | - | - |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 234.54 | - | - |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 161.48 | ✅ | 479.92 |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 168.58 | ✅ | 675.22 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 165.12 | ✅ | 525.52 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 209.20 | ✅ | 289.56 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 158.38 | ✅ | 357.04 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 190.48 | ✅ | 460.06 |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 193.42 | - | - |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 207.88 | - | - |
| test_gelu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 2978.34 |
| test_gelu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 660.20 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1024-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 18876.52 | - | - |
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-partition_N_1] | ✅ | 2243.52 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-partition_N_1] | ✅ | 233.78 | ✅ | 789.52 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-partition_N_1] | ✅ | 245.00 | ✅ | 528.24 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 47078.48 | ✅ | 82167.32 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-partition_N_1] | ✅ | 118686.70 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 27563.18 | ✅ | 20390.28 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-partition_N_1] | ✅ | 6989.68 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-partition_N_1] | ✅ | 8556.66 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 7677.20 | - | - |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 93376.88 | ✅ | 92268.60 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 100882.66 | ✅ | 92921.62 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 107010.28 | ✅ | 74698.56 |
| test_gemm[M_2048-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 37054.18 | - | - |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 1020.72 | ✅ | 2609.50 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 1127.18 | ✅ | 2659.12 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 1148.70 | ✅ | 3145.86 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 3629.42 | ✅ | 7383.48 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 3731.42 | ✅ | 6796.88 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 4080.26 | ✅ | 5537.68 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 93284.36 | ✅ | 98263.90 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 100798.66 | ✅ | 97919.40 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 105446.76 | ✅ | 76592.44 |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-partition_N_1] | ✅ | 2130.32 | ✅ | 2671.88 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-partition_N_4] | ✅ | 3593.94 | ✅ | 5224.30 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-partition_N_1] | ✅ | 1289.48 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 165.68 | ✅ | 480.22 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2725.56 | ✅ | 9402.32 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 1433.82 | ✅ | 5357.62 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 811.84 | ✅ | 3861.30 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 790.38 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2741.70 | ✅ | 9128.96 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 1411.78 | ✅ | 5307.42 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 854.22 | ✅ | 3167.60 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 798.24 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 491.92 | ✅ | 2562.74 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 341.14 | ✅ | 1216.16 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 243.00 | ✅ | 1277.86 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 466.88 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 976.08 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 228.86 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 315.86 | ✅ | 1360.88 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 138.34 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2666.42 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2679.84 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 158.02 | ✅ | 286.56 |
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 156.84 | ✅ | 824.82 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 199.40 | ✅ | 441.48 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 178.38 | ✅ | 484.60 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 174.80 | ✅ | 514.02 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 205.54 | ✅ | 422.68 |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 180.00 | - | - |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 207.74 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 169.04 | ✅ | 363.10 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 166.88 | ✅ | 397.04 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 155.70 | ✅ | 378.04 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 167.68 | ✅ | 474.16 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 196.62 | ✅ | 734.08 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 190.56 | ✅ | 480.06 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 208.04 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 224.52 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 168.00 | ✅ | 404.18 |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 195.84 | ✅ | 580.68 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 179.92 | ✅ | 409.66 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 174.24 | ✅ | 444.24 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 182.68 | ✅ | 692.00 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 201.20 | ✅ | 522.88 |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 211.50 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 223.76 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 161.20 | ✅ | 434.82 |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 177.54 | ✅ | 854.54 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 185.72 | ✅ | 427.72 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 173.12 | ✅ | 352.26 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 190.56 | ✅ | 492.92 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 203.90 | ✅ | 697.88 |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 187.68 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 239.90 | - | - |
| test_layer_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 2582.60 |
| test_layer_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 664.82 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 168.58 | ✅ | 267.66 |
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 180.48 | ✅ | 393.38 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 150.00 | ✅ | 337.52 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 182.70 | ✅ | 405.64 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 171.82 | ✅ | 638.92 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 174.66 | ✅ | 465.10 |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01] | ✅ | 169.80 | - | - |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01] | ✅ | 238.64 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 163.72 | ✅ | 511.36 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 215.12 | ✅ | 362.78 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 159.80 | ✅ | 357.70 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 160.26 | ✅ | 319.22 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 168.08 | ✅ | 443.86 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 211.16 | ✅ | 476.56 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 174.48 | ✅ | 409.52 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 196.56 | ✅ | 350.14 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 215.12 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 254.52 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 166.70 | ✅ | 352.74 |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 167.40 | ✅ | 409.52 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 171.38 | ✅ | 484.30 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 185.30 | ✅ | 421.02 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 176.58 | ✅ | 300.72 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 177.20 | ✅ | 474.94 |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 213.68 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 232.32 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 164.62 | ✅ | 397.84 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 161.52 | ✅ | 446.52 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 183.36 | ✅ | 357.24 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 163.42 | ✅ | 437.58 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 180.88 | ✅ | 528.42 |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 191.08 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 235.34 | - | - |
| test_leaky_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-alpha_0.01] | - | - | ✅ | 2928.22 |
| test_leaky_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 665.38 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024] | ✅ | 174.92 | ✅ | 622.00 |
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024] | ✅ | 149.24 | ✅ | 537.90 |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64] | ✅ | 232.32 | - | - |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64] | ✅ | 187.16 | - | - |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512] | ✅ | 171.12 | ✅ | 367.18 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512] | ✅ | 176.04 | ✅ | 368.40 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512] | ✅ | 156.82 | ✅ | 375.70 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512] | ✅ | 149.16 | ✅ | 459.10 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256] | ✅ | 157.94 | ✅ | 397.66 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256] | ✅ | 167.10 | ✅ | 409.62 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256] | ✅ | 169.68 | ✅ | 454.04 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256] | ✅ | 176.06 | ✅ | 710.12 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128] | ✅ | 228.70 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128] | ✅ | 174.72 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128] | ✅ | 193.66 | ✅ | 429.42 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128] | ✅ | 184.78 | ✅ | 603.84 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 182.10 | ✅ | 324.24 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048] | ✅ | 181.48 | ✅ | 298.00 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 196.16 | - | - |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128] | ✅ | 185.70 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 182.84 | ✅ | 630.02 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024] | ✅ | 189.70 | ✅ | 353.78 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 159.26 | ✅ | 323.84 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024] | ✅ | 158.86 | ✅ | 366.28 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 168.48 | ✅ | 281.62 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512] | ✅ | 171.36 | ✅ | 423.00 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 214.98 | ✅ | 285.02 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512] | ✅ | 163.28 | ✅ | 530.68 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 197.84 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256] | ✅ | 168.64 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 162.62 | ✅ | 388.64 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256] | ✅ | 148.18 | ✅ | 394.04 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096] | ✅ | 156.26 | ✅ | 338.12 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096] | ✅ | 150.10 | ✅ | 421.58 |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256] | ✅ | 210.90 | - | - |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256] | ✅ | 199.10 | - | - |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048] | ✅ | 174.70 | ✅ | 413.46 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048] | ✅ | 181.18 | ✅ | 385.10 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048] | ✅ | 155.46 | ✅ | 416.02 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048] | ✅ | 193.50 | ✅ | 372.36 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024] | ✅ | 194.98 | ✅ | 705.98 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024] | ✅ | 180.50 | ✅ | 512.98 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024] | ✅ | 175.60 | ✅ | 686.98 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024] | ✅ | 192.76 | ✅ | 347.86 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512] | ✅ | 187.58 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512] | ✅ | 176.72 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512] | ✅ | 190.44 | ✅ | 409.52 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512] | ✅ | 165.58 | ✅ | 412.88 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192] | ✅ | 180.76 | ✅ | 316.26 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192] | ✅ | 172.46 | ✅ | 333.64 |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512] | ✅ | 202.38 | - | - |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512] | ✅ | 185.18 | - | - |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096] | ✅ | 196.98 | ✅ | 436.04 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096] | ✅ | 182.30 | ✅ | 318.62 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096] | ✅ | 146.44 | ✅ | 461.58 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096] | ✅ | 164.52 | ✅ | 445.24 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048] | ✅ | 171.20 | ✅ | 456.66 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048] | ✅ | 149.52 | ✅ | 460.50 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048] | ✅ | 167.92 | ✅ | 504.06 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048] | ✅ | 216.32 | ✅ | 470.94 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024] | ✅ | 183.56 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024] | ✅ | 171.14 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024] | ✅ | 191.58 | ✅ | 503.82 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024] | ✅ | 173.36 | ✅ | 449.24 |
| test_mem_copy[input_length_8388608-num_cores_16-num_channels_2-bypass_False-tile_size_4096] | ✅ | 660.58 | - | - |
| test_mem_copy[input_length_8388608-num_cores_8-num_channels_2-bypass_False-tile_size_4096] | - | - | ✅ | 2687.56 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | - | ✅ | - |
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | - | ✅ | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0] | ✅ | 18371.00 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 17770.56 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | 154299.14 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 176.18 | ✅ | 300.32 |
| test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 199.92 | ✅ | 371.16 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 200.12 | ✅ | 311.40 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 179.94 | ✅ | 380.82 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 165.18 | ✅ | 438.02 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 180.70 | ✅ | 590.10 |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 166.88 | - | - |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 223.76 | - | - |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 169.66 | ✅ | 301.70 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 155.40 | ✅ | 341.98 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 161.94 | ✅ | 392.38 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 163.24 | ✅ | 807.82 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 176.96 | ✅ | 516.02 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 184.08 | ✅ | 439.82 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 192.04 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 275.86 | - | - |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 165.16 | ✅ | 424.82 |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 180.26 | ✅ | 406.14 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 181.82 | ✅ | 1235.12 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 173.00 | ✅ | 375.16 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 173.96 | ✅ | 686.34 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 189.68 | ✅ | 472.74 |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 195.56 | - | - |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 198.72 | - | - |
| test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 158.48 | ✅ | 365.02 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 159.52 | ✅ | 319.38 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 173.02 | ✅ | 669.80 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 167.34 | ✅ | 352.56 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 178.12 | ✅ | 399.04 |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 181.30 | - | - |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 220.90 | - | - |
| test_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3109.80 |
| test_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 666.16 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 147.14 | ✅ | 316.58 |
| test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None] | ✅ | 158.50 | ✅ | 352.12 |
| test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64] | ✅ | 807.86 | ✅ | 3131.68 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 154.72 | ✅ | 357.16 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 160.20 | ✅ | 346.02 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False] | ✅ | 163.34 | ✅ | 388.22 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True] | ✅ | 157.78 | ✅ | 369.66 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False] | ✅ | 149.10 | ✅ | 397.02 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True] | ✅ | 156.52 | ✅ | 475.86 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False] | ✅ | 149.04 | ✅ | 404.70 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True] | ✅ | 152.98 | ✅ | 412.36 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False] | ✅ | 139.10 | ✅ | 617.54 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True] | ✅ | 156.36 | ✅ | 430.76 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False] | ✅ | 149.54 | ✅ | 408.40 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True] | ✅ | 172.98 | ✅ | 598.60 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False] | ✅ | 169.12 | ✅ | 497.14 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True] | ✅ | 235.94 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False] | ✅ | 167.50 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True] | ✅ | 171.00 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False] | ✅ | 214.94 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 167.94 | ✅ | 382.48 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 156.70 | ✅ | 382.00 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 167.34 | ✅ | 262.60 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 163.94 | ✅ | 443.68 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 158.42 | ✅ | 451.42 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 154.02 | ✅ | 706.90 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 155.68 | ✅ | 335.80 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 171.50 | ✅ | 591.34 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 149.64 | ✅ | 356.72 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 168.10 | ✅ | 401.32 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 173.90 | ✅ | 396.00 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 176.70 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 180.82 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 190.70 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 257.88 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False] | ✅ | 175.46 | ✅ | 285.72 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | ✅ | 158.02 | ✅ | 396.22 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False] | ✅ | 167.74 | ✅ | 711.24 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True] | ✅ | 149.92 | ✅ | 492.62 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False] | ✅ | 151.98 | ✅ | 433.26 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True] | ✅ | 153.30 | ✅ | 608.84 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False] | ✅ | 146.02 | ✅ | 383.44 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True] | ✅ | 155.80 | ✅ | 415.86 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False] | ✅ | 161.92 | ✅ | 430.64 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True] | ✅ | 189.66 | ✅ | 405.68 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False] | ✅ | 158.94 | ✅ | 354.60 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True] | ✅ | 198.32 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False] | ✅ | 166.04 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True] | ✅ | 193.32 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False] | ✅ | 193.24 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False] | ✅ | 150.90 | ✅ | 327.14 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False] | ✅ | 153.94 | ✅ | 372.98 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True] | ✅ | 188.36 | ✅ | 655.60 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False] | ✅ | 188.34 | ✅ | 594.20 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True] | ✅ | 173.74 | ✅ | 668.08 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False] | ✅ | 158.36 | ✅ | 453.68 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True] | ✅ | 171.30 | ✅ | 341.24 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False] | ✅ | 153.30 | ✅ | 428.96 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True] | ✅ | 167.74 | ✅ | 668.56 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False] | ✅ | 169.78 | ✅ | 449.96 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True] | ✅ | 182.60 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False] | ✅ | 164.18 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True] | ✅ | 195.92 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False] | ✅ | 194.72 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 3012.90 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_False] | - | - | ✅ | 3051.76 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 646.36 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-weighted_False] | ✅ | 792.76 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 164.40 | ✅ | 410.28 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 168.26 | ✅ | 493.20 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 159.02 | ✅ | 675.30 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 164.44 | ✅ | 496.54 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 192.34 | ✅ | 703.60 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 183.60 | ✅ | 388.36 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 185.58 | - | - |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 185.42 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 150.64 | ✅ | 364.16 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 156.96 | ✅ | 402.84 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 152.10 | ✅ | 356.24 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 168.80 | ✅ | 371.70 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 150.70 | ✅ | 482.06 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 148.44 | ✅ | 477.16 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 176.56 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 190.68 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 164.62 | ✅ | 395.14 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 152.66 | ✅ | 298.20 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 186.82 | ✅ | 391.44 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 159.80 | ✅ | 461.56 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 166.24 | ✅ | 389.90 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 179.76 | ✅ | 458.58 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 185.66 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 165.48 | - | - |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 167.52 | ✅ | 431.06 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 160.08 | ✅ | 395.18 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 164.74 | ✅ | 335.40 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 201.04 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 215.48 | ✅ | 656.46 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 184.50 | ✅ | 447.60 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 184.76 | ✅ | 800.70 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 170.82 | - | - |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 1017.74 |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 324.40 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 170.80 | ✅ | 380.56 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 177.38 | ✅ | 316.16 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 156.96 | ✅ | 430.40 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 159.26 | ✅ | 424.08 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 173.62 | ✅ | 689.72 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 164.86 | ✅ | 420.66 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 148.78 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 178.04 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 160.14 | ✅ | 442.98 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 167.60 | ✅ | 423.80 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 153.64 | ✅ | 632.24 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 157.58 | ✅ | 506.60 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 177.20 | ✅ | 682.08 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 175.20 | ✅ | 429.00 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 185.40 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 179.92 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 159.28 | ✅ | 496.10 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 187.92 | ✅ | 372.10 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 176.24 | ✅ | 697.36 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 170.14 | ✅ | 692.76 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 155.90 | ✅ | 739.20 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 221.38 | ✅ | 754.24 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 189.98 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 163.54 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 158.38 | ✅ | 330.02 |
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 168.16 | ✅ | 356.10 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 233.22 | ✅ | 369.62 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 165.96 | ✅ | 804.06 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 162.76 | ✅ | 408.22 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 162.66 | ✅ | 484.14 |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 174.74 | - | - |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 211.90 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 154.46 | ✅ | 435.10 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 178.40 | ✅ | 352.32 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 196.36 | ✅ | 341.22 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 174.54 | ✅ | 491.70 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 154.00 | ✅ | 411.18 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 186.64 | ✅ | 1032.02 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 176.96 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 240.88 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 154.18 | ✅ | 624.96 |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 171.12 | ✅ | 377.42 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 152.38 | ✅ | 346.66 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 157.06 | ✅ | 403.10 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 169.02 | ✅ | 413.68 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 187.00 | ✅ | 440.92 |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 166.64 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 218.74 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 147.64 | ✅ | 339.28 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 194.94 | ✅ | 324.60 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 161.06 | ✅ | 466.92 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 175.28 | ✅ | 408.20 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 172.72 | ✅ | 806.98 |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 188.70 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 221.26 | - | - |
| test_sigmoid[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3182.96 |
| test_sigmoid[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 666.90 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 141.70 | ✅ | 331.18 |
| test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 157.86 | ✅ | 369.62 |
| test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 170.44 | ✅ | 471.68 |
| test_silu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 181.48 | - | - |
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 147.60 | ✅ | 804.60 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 149.56 | ✅ | 381.16 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 163.70 | ✅ | 359.76 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 158.80 | - | - |
| test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 165.02 | ✅ | 378.32 |
| test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 165.36 | ✅ | 400.22 |
| test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 187.44 | ✅ | 573.54 |
| test_silu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 190.82 | - | - |
| test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 175.12 | ✅ | 566.82 |
| test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 188.76 | ✅ | 442.32 |
| test_silu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 179.58 | - | - |
| test_silu[input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096] | - | - | ✅ | 4469.58 |
| test_silu[input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096] | ✅ | 689.52 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 525.30 | ✅ | 2178.48 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 162.26 | ✅ | 344.38 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 173.92 | ✅ | 430.52 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 210.14 | ✅ | 344.44 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[bench_flat_4mi] | ✅ | 517.78 | ✅ | 2404.92 |
| test_strided_copy[chunked_transfer] | ✅ | 177.54 | ✅ | 367.94 |
| test_strided_copy[contiguous] | ✅ | 169.44 | ✅ | 328.20 |
| test_strided_copy[four_channels] | ✅ | 173.82 | ✅ | 319.52 |
| test_strided_copy[kv_llama_full] | ✅ | 175.94 | ✅ | 305.90 |
| test_strided_copy[kv_slot0] | ✅ | 189.58 | ✅ | 329.26 |
| test_strided_copy[kv_slot5] | ✅ | 175.08 | ✅ | 315.50 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 181.84 | ✅ | 367.48 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 177.20 | ✅ | 374.70 |
| test_strided_copy[kv_slot_last] | ✅ | 187.60 | ✅ | 322.54 |
| test_strided_copy[two_channels] | ✅ | 183.16 | ✅ | 325.54 |
| test_strided_copy[two_channels_chunked] | ✅ | 177.78 | ✅ | 327.28 |
| test_strided_copy_cache_offset_parameter[iter0] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter1] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter2] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter3] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter4] | ✅ | - | - | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 993.58 | ✅ | 11513.43 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1067.00 | ✅ | 13962.08 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False] | ✅ | 2158.19 | ✅ | 24849.51 |
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True] | ✅ | 2386.66 | ✅ | 24024.24 |
| test_weight_layout_reaches_both_gemms[b_col_maj_False] | ✅ | - | ✅ | - |
| test_weight_layout_reaches_both_gemms[b_col_maj_True] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 192.22 | ✅ | 357.70 |
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 159.34 | ✅ | 349.84 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 192.82 | ✅ | 432.62 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 185.90 | ✅ | 1274.74 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 202.60 | ✅ | 434.84 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 182.60 | ✅ | 423.22 |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 173.38 | - | - |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 197.72 | - | - |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 160.90 | ✅ | 334.48 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 164.98 | ✅ | 336.60 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 161.36 | ✅ | 663.14 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 160.02 | ✅ | 667.68 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 156.96 | ✅ | 351.46 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 186.70 | ✅ | 562.28 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 154.38 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 234.24 | - | - |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 192.64 | ✅ | 391.36 |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 156.28 | ✅ | 261.82 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 145.24 | ✅ | 314.08 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 183.74 | ✅ | 390.16 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 172.40 | ✅ | 363.22 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 182.96 | ✅ | 387.94 |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 166.94 | - | - |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 190.86 | - | - |
| test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 138.82 | ✅ | 312.82 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 169.16 | ✅ | 331.20 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 172.10 | ✅ | 326.92 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 171.98 | ✅ | 405.20 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 203.64 | ✅ | 731.18 |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 204.96 | - | - |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 231.56 | - | - |
| test_tanh[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 2483.76 |
| test_tanh[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 748.62 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_dimension_that_floors_to_zero_is_refused_by_name[M_2048-N_128-aie_columns_8-channels_1-m_256-n_32-bad_num_aie_columns] | ✅ | - | ✅ | - |
| test_a_dimension_that_floors_to_zero_is_refused_by_name[M_256-N_2048-aie_columns_1-channels_2-m_256-n_32-bad_num_channels] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_1] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_2] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_4] | ✅ | - | ✅ | - |
| test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 249.52 | ✅ | 1008.68 |
| test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 236.96 | ✅ | 599.70 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 215.90 | ✅ | 892.66 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 217.12 | ✅ | 633.96 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 298.60 | ✅ | 742.90 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 290.60 | ✅ | 612.30 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 296.96 | ✅ | 1886.68 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 248.58 | ✅ | 616.78 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 270.66 | ✅ | 1287.42 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 290.70 | ✅ | 662.34 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 435.84 | ✅ | 993.10 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 382.16 | ✅ | 1480.08 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 366.64 | ✅ | 1082.90 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 351.76 | ✅ | 749.22 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 349.18 | ✅ | 1550.62 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 343.56 | ✅ | 863.64 |
| test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 331.32 | - | - |
| test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 380.18 | - | - |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 195.36 | ✅ | 445.68 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 243.22 | ✅ | 713.04 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4] | ✅ | 299.24 | ✅ | 1882.66 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 191.40 | ✅ | 530.58 |
| test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 192.48 | ✅ | 414.18 |
| test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 177.44 | ✅ | 565.80 |
| test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 159.76 | ✅ | 364.70 |
| test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 202.68 | ✅ | 456.98 |
| test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 172.12 | ✅ | 414.24 |
| test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 185.74 | ✅ | 442.74 |
| test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 189.90 | ✅ | 479.64 |
| test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 173.92 | ✅ | 447.08 |
| test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 175.36 | - | - |
| test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 176.22 | ✅ | 490.68 |
| test_transpose[M_8192-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | - | - | ✅ | 3172.16 |
| test_transpose[M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 999.30 | - | - |

</details>

