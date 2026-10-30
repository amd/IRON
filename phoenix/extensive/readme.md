
# IRON

Tested on `2026_10_30_01_25_12` at commit `ce440fa`.

<details>
<summary>iron/operators/flm/gemm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gemm[npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even]</td><td>✅ 1/1</td><td>6419.21</td><td>3.68</td><td>2090.87</td></tr>
        <tr><td>test_gemm[npu1-M_16384-K_512-N_256-epilogue_none-rounding_conv_even]</td><td>✅ 1/1</td><td>3113.06</td><td>8.17</td><td>1379.66</td></tr>
        <tr><td>test_gemm[npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even]</td><td>✅ 1/1</td><td>4551.99</td><td>3.69</td><td>1887.07</td></tr>
        <tr><td>test_gemm[npu1-M_256-K_512-N_128-epilogue_none-rounding_conv_even]</td><td>✅ 1/1</td><td>87.23</td><td>5.26</td><td>384.65</td></tr>
        <tr><td>test_gemm[npu1-M_256-K_512-N_256-epilogue_none-rounding_conv_even]</td><td>✅ 1/1</td><td>97.58</td><td>6.72</td><td>687.71</td></tr>
        <tr><td>test_gemm[npu1-M_256-K_512-N_320-epilogue_none-rounding_conv_even]</td><td>✅ 1/1</td><td>129.06</td><td>5.84</td><td>649.99</td></tr>
        <tr><td>test_gemm[npu1-M_256-K_512-N_512-epilogue_gelu-rounding_conv_even]</td><td>✅ 1/1</td><td>144.92</td><td>7.24</td><td>926.13</td></tr>
        <tr><td>test_gemm[npu1-M_256-K_512-N_512-epilogue_none-rounding_floor]</td><td>✅ 1/1</td><td>135.58</td><td>7.73</td><td>989.99</td></tr>
        <tr><td>test_gemm[npu1-M_256-K_512-N_512-epilogue_sigmoid-rounding_conv_even]</td><td>✅ 1/1</td><td>133.61</td><td>7.85</td><td>1004.53</td></tr>
        <tr><td>test_gemm[npu1-M_256-K_512-N_512-epilogue_silu-rounding_conv_even]</td><td>✅ 1/1</td><td>152.52</td><td>6.87</td><td>879.99</td></tr>
        <tr><td>test_gemm[npu1-M_256-K_512-N_64-epilogue_none-rounding_conv_even]</td><td>✅ 1/1</td><td>79.26</td><td>4.55</td><td>211.67</td></tr>
        <tr><td>test_gemm_b_col_maj[npu1-resident-high]</td><td>✅ 1/1</td><td>91.58</td><td>7.16</td><td>732.77</td></tr>
        <tr><td>test_gemm_b_col_maj[npu1-slabs-high]</td><td>✅ 1/1</td><td>3138.65</td><td>8.10</td><td>1368.41</td></tr>
        <tr><td>test_gemm_b_col_maj[npu1-streamed-high]</td><td>✅ 1/1</td><td>827.15</td><td>11.73</td><td>1947.19</td></tr>
        <tr><td>test_gemm_b_col_maj[npu1-tables-linked-high]</td><td>✅ 1/1</td><td>88.57</td><td>7.40</td><td>757.68</td></tr>
        <tr><td>test_gemm_b_col_maj[npu1-tn128-high]</td><td>✅ 1/1</td><td>152.88</td><td>6.86</td><td>877.94</td></tr>
        <tr><td>test_gemm_b_col_maj[npu1-tn16-high]</td><td>✅ 1/1</td><td>77.04</td><td>4.68</td><td>217.76</td></tr>
        <tr><td>test_gemm_b_col_maj[npu1-tn32-high]</td><td>✅ 1/1</td><td>67.41</td><td>6.81</td><td>497.79</td></tr>
        <tr><td>test_gemm_b_col_maj[npu1-trailing-col-high]</td><td>✅ 1/1</td><td>115.56</td><td>6.52</td><td>725.93</td></tr>
        <tr><td>test_gemm_k_slices[npu1-ck128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_slices[npu1-ck16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_slices[npu1-ck32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_slices[npu1-ck8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_slices[npu1-default]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_tile[K_256]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_tile[K_768]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_tile_of_few_chunks[K_16-tile_n_16-k_tile_16-ct_k_16-high]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_tile_of_few_chunks[K_16-tile_n_16-k_tile_16-ct_k_16-medium]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_tile_of_few_chunks[K_512-tile_n_64-k_tile_128-ct_k_128-high]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_tile_of_few_chunks[K_512-tile_n_64-k_tile_128-ct_k_128-medium]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_tile_of_few_chunks[K_64-tile_n_32-k_tile_64-ct_k_32-high]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_tile_of_few_chunks[K_64-tile_n_32-k_tile_64-ct_k_32-medium]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_tile_of_few_chunks[K_96-tile_n_32-k_tile_96-ct_k_32-high]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_k_tile_of_few_chunks[K_96-tile_n_32-k_tile_96-ct_k_32-medium]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[test_gemm_split_leg_bounds_runs]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[npu1-tn128-default]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[npu1-tn128-ma16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[npu1-tn128-ma64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[npu1-tn16-default]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[npu1-tn16-ma16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[npu1-tn16-ma64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[npu1-tn32-default]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[npu1-tn32-ma16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[npu1-tn32-ma64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[npu1-tn64-default]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[npu1-tn64-ma16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[npu1-tn64-ma32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_without_activations[M_256-K_512-N_256]</td><td>✅ 1/1</td><td>85.91</td><td>7.63</td><td>781.18</td></tr>
        <tr><td>test_gemm_without_activations[M_512-K_1024-N_512]</td><td>✅ 1/1</td><td>297.36</td><td>8.82</td><td>1805.49</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[test_one_xclbin_serves_every_shape]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/flm/layer</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_weight_reads_fit_proj[gemma4_e2b-layer_type_global]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e2b-layer_type_global_skip]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa_skip]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e4b-layer_type_global]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e4b-layer_type_global_skip]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa_skip]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/tests/common</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>TestLlama::test_a_prompt_longer_than_a_chunk_runs_in_chunks[test_a_prompt_longer_than_a_chunk_runs_in_chunks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestLlama::test_decode_from_an_empty_cache_matches_the_forward_token_by_token[test_decode_from_an_empty_cache_matches_the_forward_token_by_token]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestLlama::test_every_step_of_every_version_resolves[test_every_step_of_every_version_resolves]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestLlama::test_the_accuracy_check_scores_the_model_against_the_reference[test_the_accuracy_check_scores_the_model_against_the_reference]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestLlama::test_the_determinism_check_finds_the_reference_deterministic[test_the_determinism_check_finds_the_reference_deterministic]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>TestLlama::test_the_prompt_matches_the_forward_and_leaves_decode_its_caches[test_the_prompt_matches_the_forward_and_leaves_decode_its_caches]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_block_float_tile_is_sized_by_its_blocks[test_a_block_float_tile_is_sized_by_its_blocks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_body_of_args_with_no_signature_is_refused_as_its_class_is_made[test_a_body_of_args_with_no_signature_is_refused_as_its_class_is_made]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bound_is_refused_where_no_extent_takes_it[test_a_bound_is_refused_where_no_extent_takes_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bound_on_one_side_of_a_copy_holds_the_other[test_a_bound_on_one_side_of_a_copy_holds_the_other]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bound_travels_through_reshape_and_transpose[test_a_bound_travels_through_reshape_and_transpose]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bound_value_is_its_member_on_the_instance[test_a_bound_value_is_its_member_on_the_instance]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bound_value_survives_tuning[test_a_bound_value_survives_tuning]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_elf-llama_q]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_elf-qwen2_down]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_elf-qwen2_up]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_xclbin-llama_q]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_xclbin-qwen2_down]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu1-image_xclbin-qwen2_up]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_elf-llama_q]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_elf-qwen2_down]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_elf-qwen2_up]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_xclbin-llama_q]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_xclbin-qwen2_down]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_flm_gemm_moves_a_and_c_for_the_units_its_bound_reaches[device_npu2-image_xclbin-qwen2_up]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_flm_gemm_refuses_a_call_with_no_rows[test_a_bounded_flm_gemm_refuses_a_call_with_no_rows]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_gemv_moves_a_and_c_in_output_tiles_round_robin[test_a_bounded_gemv_moves_a_and_c_in_output_tiles_round_robin]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operand_binds_the_extent_and_what_derives_from_it[test_a_bounded_operand_binds_the_extent_and_what_derives_from_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operand_goes_round_robin_over_the_lanes[test_a_bounded_operand_goes_round_robin_over_the_lanes]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operand_makes_the_trip_count_per_call[test_a_bounded_operand_makes_the_trip_count_per_call]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_rope_lane_takes_whole_positions_and_their_angles[test_a_bounded_rope_lane_takes_whole_positions_and_their_angles]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_step_ends_no_command[test_a_bounded_step_ends_no_command]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_view_of_a_state_is_its_rows_this_call[test_a_bounded_view_of_a_state_is_its_rows_this_call]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_call_skips_the_commands_its_values_leave_without_work[test_a_call_skips_the_commands_its_values_leave_without_work]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_called_graph_records_into_its_caller[test_a_called_graph_records_into_its_caller]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_called_graph_takes_every_value_and_carries_none[test_a_called_graph_takes_every_value_and_carries_none]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_called_graph_writes_a_given_output_bounded_by_its_callers_value[test_a_called_graph_writes_a_given_output_bounded_by_its_callers_value]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_caller_bounds_its_rows[test_a_caller_bounds_its_rows]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_caller_records_and_bounds_it[test_a_caller_records_and_bounds_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_carried_handle_may_also_be_returned[test_a_carried_handle_may_also_be_returned]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Copy-contiguous]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Emit-one_carried]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Limbs-rows_64-line_160-num_aie_columns_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Magnitude-rows_64-width_640-num_aie_columns_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Merge-rows_192-block_32-placeholders_((258881, 2048), (258880, 2560))]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[PatchPositions-rows_2304-out_height_768-out_width_768]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Resample-height_480-width_640-out_height_480-out_width_1008-num_aie_columns_4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[ResampleTaps-in_size_17-out_size_1008]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Sample-small]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[SelectiveScan-rows_5-heads_2-head_dim_16-state_size_16-columns_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[SiLU-size_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[flm.DequantBFP-K_512-N_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance[flm.LMHead-dim_1536-vocab_4096-softcap_30.0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_causal_model_s_versions_and_signature[test_a_causal_model_s_versions_and_signature]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_chain_applies_its_profile[columns_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_chain_applies_its_profile[columns_None]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_channel_count_no_column_fits_adds_no_grid[test_a_channel_count_no_column_fits_adds_no_grid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_chat_s_added_tokens_are_their_ids_and_its_bos_is_the_template_s[bos_<|bos|>]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_chat_s_added_tokens_are_their_ids_and_its_bos_is_the_template_s[bos_]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_chat_s_added_tokens_are_their_ids_and_its_bos_is_the_template_s[bos_{{ bos_token }}]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_chat_template_jinja_file_is_read_and_may_call_strftime_now[test_a_chat_template_jinja_file_is_read_and_may_call_strftime_now]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_chat_template_jinja_file_is_read_over_tokenizer_config_s[test_a_chat_template_jinja_file_is_read_over_tokenizer_config_s]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_chat_template_s_raise_exception_raises_its_message[test_a_chat_template_s_raise_exception_raises_its_message]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_chat_template_writes_tokenizer_config_s_bos_token[given_<s>-written_<s>]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_chat_template_writes_tokenizer_config_s_bos_token[given_None-written_]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_chat_template_writes_tokenizer_config_s_bos_token[given_{'content': '<s>'}-written_<s>]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_checkpoint_s_golden_is_refused_once_it_changes[change_config]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_checkpoint_s_golden_is_refused_once_it_changes[change_first weight]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_checkpoint_s_golden_is_refused_once_it_changes[change_last weight]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_column_major_product_is_read_as_stored_by_the_next_reference[test_a_column_major_product_is_read_as_stored_by_the_next_reference]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_command_reads_at_most_a_scratchpads_words[test_a_command_reads_at_most_a_scratchpads_words]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_config_whose_application_states_no_precision_is_refused[test_a_config_whose_application_states_no_precision_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_context_no_chunk_divides_is_allocated_exactly[test_a_context_no_chunk_divides_is_allocated_exactly]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_context_no_chunk_divides_runs_to_its_last_position[test_a_context_no_chunk_divides_runs_to_its_last_position]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_decoder_without_rope_places_its_positions_through_the_hook[test_a_decoder_without_rope_places_its_positions_through_the_hook]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_derive_that_fails_for_another_reason_than_resolution_raises[test_a_derive_that_fails_for_another_reason_than_resolution_raises]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_derived_value_is_written_once_per_build[test_a_derived_value_is_written_once_per_build]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_design_is_keyed_by_what_it_builds[test_a_design_is_keyed_by_what_it_builds]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_difference_is_one_axpy_and_a_number_less_a_handle_two_steps[test_a_difference_is_one_axpy_and_a_number_less_a_handle_two_steps]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_fetch_refuses_plain_http_and_a_download_of_another_digest[test_a_fetch_refuses_plain_http_and_a_download_of_another_digest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_fetch_reuses_a_file_of_the_pinned_digest[test_a_fetch_reuses_a_file_of_the_pinned_digest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_field_added_at_its_default_keeps_the_fingerprint[test_a_field_added_at_its_default_keeps_the_fingerprint]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_field_resolve_computes_is_kept_by_copies_and_checked_once_known[test_a_field_resolve_computes_is_kept_by_copies_and_checked_once_known]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_file_of_other_inputs_is_refused_and_rerecorded[test_a_file_of_other_inputs_is_refused_and_rerecorded]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_float32_product_is_not_rounded_to_its_inputs_dtype[test_a_float32_product_is_not_rounded_to_its_inputs_dtype]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_forced_xclbin_is_derived_and_says_why[test_a_forced_xclbin_is_derived_and_says_why]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_full_elf_ends_a_command_at_a_host_step[test_a_full_elf_ends_a_command_at_a_host_step]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_gather_refuses_what_it_cannot_lower[index_(array([0, 1]), slice(0, 4, None))-match_whole of every axis]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_gather_refuses_what_it_cannot_lower[index_[ 0 64]-match_gathering]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_gather_refuses_what_it_cannot_lower[index_[-65]-match_gathering]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_gather_refuses_what_it_cannot_lower[index_[0. 1.]-match_1-D integer array]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_gather_refuses_what_it_cannot_lower[index_[[0 1]]-match_1-D integer array]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_gather_refuses_what_it_cannot_lower[index_[]-match_gathering]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_generation_block_renders_its_body[test_a_generation_block_renders_its_body]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_generation_s_timings_are_the_model_s_stats[test_a_generation_s_timings_are_the_model_s_stats]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_given_output_of_another_rank_is_refused_unless_declared_flat[test_a_given_output_of_another_rank_is_refused_unless_declared_flat]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_graph_carries_its_next_values[test_a_graph_carries_its_next_values]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_graph_carries_its_profile[test_a_graph_carries_its_profile]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_graph_names_its_inputs_and_values_in_signature[count_2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_graph_names_its_inputs_and_values_in_signature[count_3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_graph_reads_as_its_name_and_recorded_shapes[test_a_graph_reads_as_its_name_and_recorded_shapes]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_handle_adds_and_multiplies_by_elementwise_and_rowwise_steps[test_a_handle_adds_and_multiplies_by_elementwise_and_rowwise_steps]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_held_array_is_viewed_in_the_body_under_its_own_path[test_a_held_array_is_viewed_in_the_body_under_its_own_path]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_held_array_that_is_no_param_is_refused[test_a_held_array_that_is_no_param_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_host_step_is_recorded_before_the_next_step[test_a_host_step_is_recorded_before_the_next_step]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_host_step_runs_between_the_device_s_steps[each_step]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_host_write_to_a_state_a_step_writes_is_refused[test_a_host_write_to_a_state_a_step_writes_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_host_write_to_other_than_a_state_is_refused[test_a_host_write_to_other_than_a_state_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_lane_pins_to_a_channel_moving_its_way[test_a_lane_pins_to_a_channel_moving_its_way]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_layer_norm_s_eps_is_its_kernel_s[test_a_layer_norm_s_eps_is_its_kernel_s]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_matvec_whose_columns_are_given_resolves_with_no_device[test_a_matvec_whose_columns_are_given_resolves_with_no_device]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_mixed_call_places_the_soft_tokens_and_attends_over_them[soft_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_mixed_call_places_the_soft_tokens_and_attends_over_them[soft_5]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_model_fits_its_context_with_no_device_bound[test_a_model_fits_its_context_with_no_device_bound]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_model_runs_only_the_versions_it_loaded[test_a_model_runs_only_the_versions_it_loaded]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_name_the_tracer_makes_up_never_aliases_one_it_was_given[test_a_name_the_tracer_makes_up_never_aliases_one_it_was_given]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_norm_is_its_kernel_weighted_if_given_then_any_bias[layer_weighted_biased]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_norm_is_its_kernel_weighted_if_given_then_any_bias[rms_unweighted]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_norm_over_another_axis_than_the_last_is_refused[layer]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_norm_over_another_axis_than_the_last_is_refused[rms]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_number_on_either_side_is_a_row_of_it[test_a_number_on_either_side_is_a_row_of_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_numpy_function_on_a_handle_says_what_to_call[test_a_numpy_function_on_a_handle_says_what_to_call]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_padded_pattern_does_not_fit_a_shim_descriptor[test_a_padded_pattern_does_not_fit_a_shim_descriptor]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_per_call_length_counts_a_dimension_by_a_word[no_dimension_of_the_unit]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_per_call_length_counts_a_dimension_by_a_word[not_a_word]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_per_call_value_cannot_steer_the_record[test_a_per_call_value_cannot_steer_the_record]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_per_call_value_s_default_is_given_when_left_out[test_a_per_call_value_s_default_is_given_when_left_out]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_positional_operand_past_the_inputs_is_an_output_not_an_optional_one[test_a_positional_operand_past_the_inputs_is_an_output_not_an_optional_one]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_profile_fills_the_tunables_a_call_leaves_open[test_a_profile_fills_the_tunables_a_call_leaves_open]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_profile_is_checked_as_it_is_written_and_as_it_is_read[test_a_profile_is_checked_as_it_is_written_and_as_it_is_read]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_prompt_begins_as_the_tokenizer_begins_a_text[gemma-4-e2b-it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_prompt_begins_as_the_tokenizer_begins_a_text[llama3.2-1b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_prompt_chunk_past_the_last_position_is_refused[chunk_0-rows_256-inside_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_prompt_chunk_past_the_last_position_is_refused[chunk_1-rows_44-inside_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_prompt_chunk_past_the_last_position_is_refused[chunk_1-rows_45-inside_False]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_prompt_chunk_past_the_last_position_is_refused[chunk_2-rows_1-inside_False]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_reference_only_operator_runs_its_reference_and_does_not_compile[test_a_reference_only_operator_runs_its_reference_and_does_not_compile]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_reference_only_operator_takes_no_image[test_a_reference_only_operator_takes_no_image]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_reference_takes_valid_rows_short_of_a_whole_line[n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_reference_takes_valid_rows_short_of_a_whole_line[n_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_reference_takes_valid_rows_short_of_a_whole_line[n_9]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_refused_compile_restores_the_device_it_was_given_over[test_a_refused_compile_restores_the_device_it_was_given_over]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_refused_step_names_the_graph_the_operator_and_the_held_path[test_a_refused_step_names_the_graph_the_operator_and_the_held_path]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_refused_step_shows_an_unheld_param_as_an_array_of_its_shape[test_a_refused_step_shows_an_unheld_param_as_an_array_of_its_shape]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_row_bound_needs_one_row_block_per_unit[test_a_row_bound_needs_one_row_block_per_unit]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_row_sweep_splits_each_length_into_rows_of_the_tile[test_a_row_sweep_splits_each_length_into_rows_of_the_tile]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_run_as_wide_as_its_axis_keeps_its_start_under_a_bound[test_a_run_as_wide_as_its_axis_keeps_its_start_under_a_bound]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_run_from_a_per_call_start_has_a_fixed_width_and_one_start[another_value]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_run_from_a_per_call_start_has_a_fixed_width_and_one_start[no_stop]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_run_from_a_per_call_start_has_a_fixed_width_and_one_start[two_per_call]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_run_from_a_per_call_start_has_a_fixed_width_and_one_start[wider_than_the_axis]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_run_from_a_per_call_start_is_its_whole_chunk_s_view[test_a_run_from_a_per_call_start_is_its_whole_chunk_s_view]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_run_from_a_per_call_start_is_written_and_read_as_numpy_does[test_a_run_from_a_per_call_start_is_written_and_read_as_numpy_does]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_run_from_a_per_call_start_takes_any_start_on_any_axis[test_a_run_from_a_per_call_start_takes_any_start_on_any_axis]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_run_is_bounded_from_its_start_on_its_own_axis[test_a_run_is_bounded_from_its_start_on_its_own_axis]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_run_of_soft_tokens_crossing_a_chunk_is_placed_on_both_sides[test_a_run_of_soft_tokens_crossing_a_chunk_is_placed_on_both_sides]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_run_past_the_buffer_s_end_is_kept_inside_by_each_call[test_a_run_past_the_buffer_s_end_is_kept_inside_by_each_call]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_run_that_draws_no_eos_draws_max_tokens[test_a_run_that_draws_no_eos_draws_max_tokens]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_scratchpad_parameter_holds_one_word[test_a_scratchpad_parameter_holds_one_word]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_shipped_image_declares_its_pins_and_parameter_block[test_a_shipped_image_declares_its_pins_and_parameter_block]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_shipped_image_in_a_graph_is_refused[test_a_shipped_image_in_a_graph_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_shipped_image_runs_only_with_instructions[test_a_shipped_image_runs_only_with_instructions]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_size_the_default_line_does_not_split_takes_a_narrower_one[test_a_size_the_default_line_does_not_split_takes_a_narrower_one]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_sliding_window_some_layers_take_is_refused[test_a_sliding_window_some_layers_take_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_state_is_subtracted_as_it_is_added[test_a_state_is_subtracted_as_it_is_added]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_state_written_by_one_step_is_pinned_and_readable[test_a_state_written_by_one_step_is_pinned_and_readable]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_stream_binds_a_handle_per_lane[test_a_stream_binds_a_handle_per_lane]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_stream_with_no_lanes_is_paid_once_in_the_shim_budget[test_a_stream_with_no_lanes_is_paid_once_in_the_shim_budget]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_t_or_none_dim_is_omitted_when_none_and_may_sit_anywhere[test_a_t_or_none_dim_is_omitted_when_none_and_may_sit_anywhere]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_text_only_call_runs_the_text_model_s_version[test_a_text_only_call_runs_the_text_model_s_version]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_token_outside_the_vocabulary_is_refused_before_any_dispatch[outside_-1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_token_outside_the_vocabulary_is_refused_before_any_dispatch[outside_1024]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tower_runs_its_front_end_s_rows[test_a_tower_runs_its_front_end_s_rows]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tunable_free_operator_takes_the_widest_split_that_leaves_whole_lines[test_a_tunable_free_operator_takes_the_widest_split_that_leaves_whole_lines]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tunable_given_as_none_is_left_to_the_profile[test_a_tunable_given_as_none_is_left_to_the_profile]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_turn_runs_from_its_first_new_token[test_a_turn_runs_from_its_first_new_token]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_value_a_graph_binds_is_per_call_and_no_longer_a_resident[test_a_value_a_graph_binds_is_per_call_and_no_longer_a_resident]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_value_only_a_core_reads_is_declared_on_a_full_elf[test_a_value_only_a_core_reads_is_declared_on_a_full_elf]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_version_reads_none_of_the_words_its_image_writes[test_a_version_reads_none_of_the_words_its_image_writes]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_version_reads_only_the_values_its_steps_read[test_a_version_reads_only_the_values_its_steps_read]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_version_with_no_tensor_splits_at_a_host_step_too[test_a_version_with_no_tensor_splits_at_a_host_step_too]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_walk_one_descriptor_cannot_hold_is_refused[sizes_[2, 2, 8, 2048]-strides_[0, 65536, 4096, 1]-bounded_True-match_one shim]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_walk_one_descriptor_cannot_hold_is_refused[sizes_[4, 4, 4, 1024]-strides_[0, 4096, 1024, 1]-bounded_False-match_give bounds]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_walk_one_descriptor_cannot_hold_is_refused[sizes_[64, 4096]-strides_[4096, 1]-bounded_True-match_one shim]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_weight_given_where_an_optional_input_was_meant_is_refused[view_False]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_weight_given_where_an_optional_input_was_meant_is_refused[view_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_weight_times_a_row_is_linear_and_a_plain_matrix_is_refused[test_a_weight_times_a_row_is_linear_and_a_plain_matrix_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_whole_reshape_of_a_held_array_is_gathered_under_its_own_path[test_a_whole_reshape_of_a_held_array_is_gathered_under_its_own_path]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_alike_instances_bound_to_different_values_are_different_designs[test_alike_instances_bound_to_different_values_are_different_designs]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_activation_is_judged_by_its_devices_row[GELU-device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_activation_is_judged_by_its_devices_row[GELU-device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_activation_is_judged_by_its_devices_row[SiLU-device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_activation_is_judged_by_its_devices_row[SiLU-device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_activation_is_judged_by_its_devices_row[Sigmoid-device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_activation_is_judged_by_its_devices_row[Sigmoid-device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_activation_is_judged_by_its_devices_row[Tanh-device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_activation_is_judged_by_its_devices_row[Tanh-device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_assignment_into_a_view_is_the_copy_into_it[test_an_assignment_into_a_view_is_the_copy_into_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_axis_is_found_through_the_branch_a_select_takes[test_an_axis_is_found_through_the_branch_a_select_takes]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_encoder_attends_its_valid_rows_both_ways[n_1-window_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_encoder_attends_its_valid_rows_both_ways[n_1-window_None]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_encoder_attends_its_valid_rows_both_ways[n_128-window_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_encoder_attends_its_valid_rows_both_ways[n_128-window_None]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_encoder_places_its_positions_through_the_hook[n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_encoder_places_its_positions_through_the_hook[n_9]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_explicit_instance_is_applied_like_the_class[test_an_explicit_instance_is_applied_like_the_class]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_exported_design_replaces_the_derived_one[test_an_exported_design_replaces_the_derived_one]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_extent_reads_as_its_field_until_a_graph_bounds_it[test_an_extent_reads_as_its_field_until_a_graph_bounds_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_image_a_call_does_not_hold_is_refused[test_an_image_a_call_does_not_hold_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_index_before_a_bound_keeps_the_bound_on_its_axis[test_an_index_before_a_bound_keeps_the_bound_on_its_axis]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_index_may_floor_and_a_bound_may_only_clamp[test_an_index_may_floor_and_a_bound_may_only_clamp]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_input_given_as_an_output_is_refused[test_an_input_given_as_an_output_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_input_named_as_a_compile_keyword_is_refused[test_an_input_named_as_a_compile_keyword_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_interval_is_what_compare_admits[bound]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_interval_is_what_compare_admits[exact]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_interval_is_what_compare_admits[relative]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_interval_is_what_compare_admits[relative_atol]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_interval_is_what_compare_admits[relative_range]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_interval_is_what_compare_admits[ulps]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_interval_is_what_compare_admits[ulps_atol]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_operand_declared_when_a_flag_exists_only_where_it_is_true[test_an_operand_declared_when_a_flag_exists_only_where_it_is_true]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_operand_fills_only_inside_its_operators_sequence[test_an_operand_fills_only_inside_its_operators_sequence]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_operand_with_a_tile_is_its_own_stream[test_an_operand_with_a_tile_is_its_own_stream]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_operator_written_by_inheritance_inherits_the_sweep[test_an_operator_written_by_inheritance_inherits_the_sweep]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_optional_input_gives_a_version_without_it[test_an_optional_input_gives_a_version_without_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_unaligned_gather_computes_whole_blocks[test_an_unaligned_gather_computes_whole_blocks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_unaligned_gather_writes_no_callers_output[test_an_unaligned_gather_writes_no_callers_output]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_xclbin_is_asked_for_where_a_full_elf_would_do[test_an_xclbin_is_asked_for_where_a_full_elf_would_do]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_angles_are_the_unscaled_table_at_rope_width[test_angles_are_the_unscaled_table_at_rope_width]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_array_sees_the_array_tier_alone[test_array_sees_the_array_tier_alone]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_arrays_are_shared_by_array_key_and_extents_are_not[test_arrays_are_shared_by_array_key_and_extents_are_not]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_attention_scaling_multiplies_the_whole_table_once[test_attention_scaling_multiplies_the_whole_table_once]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_binding_two_handles_to_one_instance_is_an_error[test_binding_two_handles_to_one_instance_is_an_error]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_buffers_resolve_shape_dtype_and_direction[test_buffers_resolve_shape_dtype_and_direction]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_by_default_the_table_is_rope_angles_at_head_dim[test_by_default_the_table_is_rope_angles_at_head_dim]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_call_reference_gives_an_output_only_to_a_reference_that_names_it[test_call_reference_gives_an_output_only_to_a_reference_that_names_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_call_reference_pairs_buffers_by_name_not_by_order[test_call_reference_pairs_buffers_by_name_not_by_order]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_call_reference_refuses_a_reference_that_returns_nothing[test_call_reference_refuses_a_reference_that_returns_nothing]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_chat_messages_are_rendered_by_the_checkpoint_s_template[test_chat_messages_are_rendered_by_the_checkpoint_s_template]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_check_determinism_needs_two_rounds_before_any_load[rounds_0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_check_determinism_needs_two_rounds_before_any_load[rounds_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_check_takes_an_xclbin_per_step[test_check_takes_an_xclbin_per_step]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_compatible_runs_at_construction_once_every_tunable_is_known[test_compatible_runs_at_construction_once_every_tunable_is_known]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_concurrent_fetches_of_a_shipped_image_each_get_the_whole_file[test_concurrent_fetches_of_a_shipped_image_each_get_the_whole_file]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_decode_step_reads_the_rope_table_at_its_own_width[test_decode_step_reads_the_rope_table_at_its_own_width]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_default_is_a_full_elf_on_npu2[test_default_is_a_full_elf_on_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_devices_are_named_for_their_design_not_their_step[test_devices_are_named_for_their_design_not_their_step]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_gelu_is_its_operator_s_form[act_gelu-approximate_none]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_gelu_is_its_operator_s_form[act_gelu_pytorch_tanh-approximate_tanh]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embedding_gemma2_from_checkpoint_is_the_default_instance[cls_<class 'iron.applications.embedding_gemma2.model.Config'>-instance_Config(eps=1e-06, precision=<Precision.HIGHEST: 'highest'>, vocab_size=262144, hidden_size=512, num_hidden_layers=24, num_attention_heads=4, intermediate_size=2048, num_key_value_heads=2, head_dim=256, rope_theta=10000.0, layer_types=('sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'full_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'full_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'full_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'sliding_attention', 'full_attention'), global_kv_groups=1, global_head_dim=512, global_rope_theta=1000000.0, sliding_window=512, ple_dim=512, embedding_dim=768, hidden_act='gelu_pytorch_tanh', mrl_dims=(768, 512, 256, 128), image_token=258880, audio_token=258881, boi=255999, eoi=258882, boa=256000, eoa=258883, max_tokens=2048, block=64)]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embedding_gemma2_from_checkpoint_is_the_default_instance[cls_<class 'iron.applications.gemma4.audio.AudioConfig'>-instance_AudioConfig(eps=1e-06, precision=<Precision.HIGHEST: 'highest'>, hidden_size=1024, num_hidden_layers=12, num_attention_heads=8, intermediate_size=4096, mels=128, subsampling_conv_channels=(128, 32), window=12, band=32, attention_logit_cap=50.0, use_clipped_linears=True, conv_kernel_size=5, residual_weight=0.5, text_dim=512, output_proj_dims=1536, sample_rate=16000, frame=320, hop=160, max_samples=480000, max_tokens=768)]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embedding_gemma2_from_checkpoint_is_the_default_instance[cls_<class 'iron.applications.gemma4.vision.VisionConfig'>-instance_VisionConfig(eps=1e-06, precision=<Precision.HIGHEST: 'highest'>, hidden_size=768, num_hidden_layers=16, num_attention_heads=12, head_dim=64, intermediate_size=3072, patch_size=16, pooling_kernel_size=3, position_embedding_size=10240, rope_theta=100.0, hidden_act='gelu_pytorch_tanh', use_clipped_linears=False, text_dim=512, image_tokens=280, patches=2560, largest=(3072, 4096), rows=256, chunk=4096, patch_columns=8)]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embeddinggemma_2_loads_a_layer_s_per_layer_input_flat_or_nested[test_embeddinggemma_2_loads_a_layer_s_per_layer_input_flat_or_nested]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_equal_kernel_recipes_share_one_object_across_designs[test_equal_kernel_recipes_share_one_object_across_designs]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_every_carried_value_is_carried_and_nothing_else[test_every_carried_value_is_carried_and_nothing_else]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_every_declared_case_resolves_on_npu2[test_every_declared_case_resolves_on_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_every_tolerance_says_where_its_numbers_come_from[npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_every_tolerance_says_where_its_numbers_come_from[npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_AXPY]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_Clamp]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_Copy]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_DepthwiseConv1d]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_ElementwiseAdd]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_ElementwiseMul]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_Emit]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_GELU]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_GEMM]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_GEMV]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_GatherWords]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_Gather]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_LayerNorm]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_Limbs]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_Log]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_MHA]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_Magnitude]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_Merge]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_PatchPositions]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_RMSNorm]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_ReLU]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_ResampleTaps]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_Resample]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_RoPE]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_RowwiseAdd]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_RowwiseMul]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_Sample]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_SelectiveScan]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_SiLU]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_Sigmoid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_Softmax]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_Tanh]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_flm.DecodeLayer]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_flm.DequantBFP]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_flm.LMHead]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_flm.PrefillAttention]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_flm.PrefillSlidingAttention]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_exported_operator_is_declared[name_flm.ProjectionGEMM]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_fit_keeps_the_native_context_where_it_fits_else_whole_chunks[test_fit_keeps_the_native_context_where_it_fits_else_whole_chunks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_gemm_declares_every_b_pool_whichever_columns_a_shape_fills[test_flm_gemm_declares_every_b_pool_whichever_columns_a_shape_fills]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_gemm_image_keeps_the_tiles_a_narrow_shape_resolves_to[test_flm_gemm_image_keeps_the_tiles_a_narrow_shape_resolves_to]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_gemm_keyword_construction_tunes_from_the_device[test_flm_gemm_keyword_construction_tunes_from_the_device]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_gemm_selects_its_activation_by_a_word[test_flm_gemm_selects_its_activation_by_a_word]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_float_scratchpad_annotation_is_rejected[test_float_scratchpad_annotation_is_rejected]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_from_checkpoint_draws_its_weights_at_a_seed[test_from_checkpoint_draws_its_weights_at_a_seed]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_from_checkpoint_lowers_the_context_and_refuses_to_raise_it[test_from_checkpoint_lowers_the_context_and_refuses_to_raise_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_from_checkpoint_names_the_keys_a_config_json_lacks[test_from_checkpoint_names_the_keys_a_config_json_lacks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_from_checkpoint_opens_the_tokenizer_beside_it[test_from_checkpoint_opens_the_tokenizer_beside_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_from_checkpoint_reads_each_key_and_no_not_json_field[iron.applications.embedding_gemma2.model.Config]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_from_checkpoint_reads_each_key_and_no_not_json_field[iron.applications.gemma4.audio.AudioConfig]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_from_checkpoint_reads_each_key_and_no_not_json_field[iron.applications.gemma4.vision.VisionConfig]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_from_checkpoint_reads_each_key_and_no_not_json_field[iron.applications.granite.model.GraniteConfig]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_from_checkpoint_reads_each_key_and_no_not_json_field[iron.applications.llama.model.LlamaConfig]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_from_checkpoint_refuses_a_rope_scaling_it_builds_no_table_for[test_from_checkpoint_refuses_a_rope_scaling_it_builds_no_table_for]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_from_checkpoint_takes_either_the_file_or_its_directory[test_from_checkpoint_takes_either_the_file_or_its_directory]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gathered_patches_hold_no_padding[test_gathered_patches_hold_no_padding]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gelu_refuses_a_form_it_has_no_kernel_for[test_gelu_refuses_a_form_it_has_no_kernel_for]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_bounds_its_compute_and_mha_its_compute_and_kv_traffic[test_gemm_bounds_its_compute_and_mha_its_compute_and_kv_traffic]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemma_s_text_layer_projects_at_highest_precision[test_gemma_s_text_layer_projects_at_highest_precision]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemma_s_text_layer_through_its_operators_references_is_hugging_face_s[test_gemma_s_text_layer_through_its_operators_references_is_hugging_face_s]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_generate_gives_text_for_text_and_ids_for_ids[test_generate_gives_text_for_text_and_ids_for_ids]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_generation_stops_at_an_eos_and_includes_it[test_generation_stops_at_an_eos_and_includes_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_head_dim_falls_back_and_max_seq_len_is_the_native_context[test_head_dim_falls_back_and_max_seq_len_is_the_native_context]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_highest_runs_the_gemm_that_rounds_once[test_highest_runs_the_gemm_that_rounds_once]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_identity_holds_across_processes[test_identity_holds_across_processes]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_identity_is_what_the_text_is_a_function_of[test_identity_is_what_the_text_is_a_function_of]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_inline_records_only_into_a_body[test_inline_records_only_into_a_body]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_inputs_pad_with_zero_and_give_rows[test_inputs_pad_with_zero_and_give_rows]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_inputs_refuse_what_no_call_takes[tokens_[-1]-error_<class 'IndexError'>]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_inputs_refuse_what_no_call_takes[tokens_[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]-error_<class 'ValueError'>]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_inputs_refuse_what_no_call_takes[tokens_[32]-error_<class 'IndexError'>]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_inputs_refuse_what_no_call_takes[tokens_[]-error_<class 'ValueError'>]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_integer_arithmetic_on_an_expression_is_an_expression[test_integer_arithmetic_on_an_expression_is_an_expression]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_it_records_only_while_asked_and_reads_back_without_the_reference[test_it_records_only_while_asked_and_reads_back_without_the_reference]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_its_signature_is_its_text_model_s_and_towers[test_its_signature_is_its_text_model_s_and_towers]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_judge_names_each_output_and_refuses_a_missing_one[test_judge_names_each_output_and_refuses_a_missing_one]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_keyword_only_parameters_must_be_annotated_as_values[test_keyword_only_parameters_must_be_annotated_as_values]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_linear_takes_a_precision_for_any_rows_and_gemv_tunables_for_one[gemm]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_linear_takes_a_precision_for_any_rows_and_gemv_tunables_for_one[gemv]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_linear_takes_one_row_or_several[test_linear_takes_one_row_or_several]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_1b_from_checkpoint_is_its_published_shape[test_llama_1b_from_checkpoint_is_its_published_shape]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_decode_records_and_tunes[test_llama_decode_records_and_tunes]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_projects_at_high_from_3b_s_width_unless_given[test_llama_projects_at_high_from_3b_s_width_unless_given]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_prompt_projects_with_flm_gemm[device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_prompt_projects_with_flm_gemm[device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_prompt_records_over_the_same_caches[test_llama_prompt_records_over_the_same_caches]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_log_mel_holds_to_the_extractor[test_log_mel_holds_to_the_extractor]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_matmul_of_a_row_by_a_weight_s_transpose_is_linear[param]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_matmul_of_a_row_by_a_weight_s_transpose_is_linear[state]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_matmul_of_a_row_by_a_weight_s_transpose_is_linear[weight]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_binds_p_times_v_at_its_own_shape[test_mha_binds_p_times_v_at_its_own_shape]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_refuses_a_sequence_pad_of_no_whole_blocks[test_mha_refuses_a_sequence_pad_of_no_whole_blocks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_no_column_count_resolves_when_one_column_overruns_the_shim[test_no_column_count_resolves_when_one_column_overruns_the_shim]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_no_npu_says_how_to_compile_without_one[test_no_npu_says_how_to_compile_without_one]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_no_sampler_is_greedy[test_no_sampler_is_greedy]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_npu1_forces_xclbin_and_reports_the_scratchpad_lowering[test_npu1_forces_xclbin_and_reports_the_scratchpad_lowering]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_npu1_runs_every_case_of_an_operator_it_runs[test_npu1_runs_every_case_of_an_operator_it_runs]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_on_an_xclbin_a_bounded_flm_gemm_repeats_a_by_the_dispatch_scalar[test_on_an_xclbin_a_bounded_flm_gemm_repeats_a_by_the_dispatch_scalar]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_on_an_xclbin_a_copy_bounded_on_its_innermost_axis_sizes_it[test_on_an_xclbin_a_copy_bounded_on_its_innermost_axis_sizes_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_on_an_xclbin_a_per_call_length_sizes_the_coalesced_descriptor[five_dimensions]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_on_an_xclbin_a_per_call_length_sizes_the_coalesced_descriptor[repeat_led]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_on_an_xclbin_the_size_is_the_dispatch_scalar[test_on_an_xclbin_the_size_is_the_dispatch_scalar]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_on_host_outside_a_body_is_refused[test_on_host_outside_a_body_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_configuration_records_at_one_size[test_one_configuration_records_at_one_size]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_row_a_core_holds_is_still_rowwise[test_one_row_a_core_holds_is_still_rowwise]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_row_times_a_number_is_elementwise[test_one_row_times_a_number_is_elementwise]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_only_a_copy_takes_the_rows_an_input_names[test_only_a_copy_takes_the_rows_an_input_names]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_only_none_may_default_an_input[test_only_none_may_default_an_input]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_patches_short_of_a_tile_compute_a_whole_one[test_patches_short_of_a_tile_compute_a_whole_one]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_per_call_values_bind_on_the_operator[test_per_call_values_bind_on_the_operator]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_per_call_values_bind_to_the_operator_and_enable_it[test_per_call_values_bind_to_the_operator_and_enable_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_placeholders_that_are_not_the_soft_tokens_are_refused[test_placeholders_that_are_not_the_soft_tokens_are_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prompt_chunk_reads_the_rope_table_at_its_own_width[test_prompt_chunk_reads_the_rope_table_at_its_own_width]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_reference_without_a_device_names_how_to_bind_one[test_reference_without_a_device_names_how_to_bind_one]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_report_reads_as_one_block[test_report_reads_as_one_block]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_resolve_columns_is_the_count_given_or_the_most_that_fit[test_resolve_columns_is_the_count_given_or_the_most_that_fit]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_returning_an_input_or_a_slice_is_refused[test_returning_an_input_or_a_slice_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rope_width_is_the_rotary_dim_when_given[test_rope_width_is_the_rotary_dim_when_given]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_runtime_parameters_lay_out_the_buffer_words_and_skip_scratchpad_ones[test_runtime_parameters_lay_out_the_buffer_words_and_skip_scratchpad_ones]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_saving_an_operator_outside_the_catalog_names_it[test_saving_an_operator_outside_the_catalog_names_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_shape_mismatch_and_rank_rules[test_shape_mismatch_and_rank_rules]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_slices_are_views_into_the_parent_in_bytes[test_slices_are_views_into_the_parent_in_bytes]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_split_takes_every_batch_and_broadcasts[test_split_takes_every_batch_and_broadcasts]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_stream_s_pieces_joined_are_what_generate_gives[test_stream_s_pieces_joined_are_what_generate_gives]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_testing_resolves_cases_and_callables_of_the_class[test_testing_resolves_cases_and_callables_of_the_class]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_architecture_decides_not_the_name[test_the_architecture_decides_not_the_name]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_binary_sweep_and_an_all_extensive_sweep[test_the_binary_sweep_and_an_all_extensive_sweep]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_callers_reference_runs_the_called_graph[test_the_callers_reference_runs_the_called_graph]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_carried_draws_are_the_host_loop_s_tokens[temperature_0.0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_carried_draws_are_the_host_loop_s_tokens[temperature_0.7]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_cases_judge_by_every_kind_of_tolerance[test_the_cases_judge_by_every_kind_of_tolerance]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_default_layer_is_an_encoder_layer_attending_both_ways[test_the_default_layer_is_an_encoder_layer_attending_both_ways]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_gather_reads_only_the_rows_a_call_bounds[test_the_gather_reads_only_the_rows_a_call_bounds]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_oracles_steps_pass_and_a_wrong_weight_is_caught_at_its_step[test_the_oracles_steps_pass_and_a_wrong_weight_is_caught_at_its_step]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_quick_start_script_runs_on_a_toy_repository[test_the_quick_start_script_runs_on_a_toy_repository]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_computes_the_expressions[test_the_reference_computes_the_expressions]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_copies_a_bounded_call_into_the_rows_it_covers[test_the_reference_copies_a_bounded_call_into_the_rows_it_covers]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_holds_one_layer_s_intermediates_at_a_time[test_the_reference_holds_one_layer_s_intermediates_at_a_time]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_is_its_parts_on_their_own[test_the_reference_is_its_parts_on_their_own]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_is_the_convolution[case_band]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_is_the_convolution[case_depthwise]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_is_the_convolution[case_depthwise_13_rows]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_is_the_convolution[case_patches]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_refuses_what_a_call_refuses[test_the_reference_refuses_what_a_call_refuses]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_runs_the_host_step_on_the_rows_the_call_bounds[rows_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_runs_the_host_step_on_the_rows_the_call_bounds[rows_5]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_runs_the_trace_so_held_state_takes_arithmetic[test_the_reference_runs_the_trace_so_held_state_takes_arithmetic]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_writes_a_copy_into_a_strided_view_through_it[test_the_reference_writes_a_copy_into_a_strided_view_through_it]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_writes_a_given_output_of_an_operator_that_returns_one[test_the_reference_writes_a_given_output_of_an_operator_that_returns_one]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_refusals_name_what_to_change[test_the_refusals_name_what_to_change]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_slots_after_a_multi_word_value_follow_its_words[test_the_slots_after_a_multi_word_value_follow_its_words]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_trace_records_the_range_each_per_call_index_and_bound_holds[test_the_trace_records_the_range_each_per_call_index_and_bound_holds]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_trip_count_is_a_resident_the_build_writes[test_the_trip_count_is_a_resident_the_build_writes]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_unary_sweep_reads_the_class_it_is_resolved_for[test_the_unary_sweep_reads_the_class_it_is_resolved_for]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_to_json_is_from_checkpoint_s_inverse[embedding_gemma2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_to_json_is_from_checkpoint_s_inverse[llama]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_tracing_records_the_runlist_with_names_from_roles[test_tracing_records_the_runlist_with_names_from_roles]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_two_designs_whose_device_names_collide_are_refused[test_two_designs_whose_device_names_collide_are_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_two_sessions_share_one_model[test_two_sessions_share_one_model]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_two_towers_on_one_input_name_are_refused[test_two_towers_on_one_input_name_are_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_v_shows_iron_s_info_lines[test_v_shows_iron_s_info_lines]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_vectors_draws_each_input_and_runs_the_reference_on_the_draw[test_vectors_draws_each_input_and_runs_the_reference_on_the_draw]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_vectors_takes_a_given_shape_or_refuses_an_unknown_input[test_vectors_takes_a_given_shape_or_refuses_an_unknown_input]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_walks_take_a_repeat_each[taps_1-repeats_2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_walks_take_a_repeat_each[taps_2-repeats_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_what_a_bound_makes_per_call_is_worked_out_once_per_binding[test_what_a_bound_makes_per_call_is_worked_out_once_per_binding]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/tests/docs</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_section1_axpy_matches_numpy[test_section1_axpy_matches_numpy]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_section2_first_graph_matches_numpy[test_section2_first_graph_matches_numpy]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_section3_bounded_graph_matches_numpy[test_section3_bounded_graph_matches_numpy]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_section3_bounded_graph_rejects_an_out_of_range_call[test_section3_bounded_graph_rejects_an_out_of_range_call]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_section4_subtraction_exercise_selects_arithmetic[test_section4_subtraction_exercise_selects_arithmetic]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_section4_weights_and_state_matches_numpy[test_section4_weights_and_state_matches_numpy]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_section5_walk_matches_numpy_host_driven[test_section5_walk_matches_numpy_host_driven]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_section6_reference_matches_its_operators_chained_by_hand[test_section6_reference_matches_its_operators_chained_by_hand]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_section7_a_calls_own_value_wins_over_the_profile[test_section7_a_calls_own_value_wins_over_the_profile]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_section7_profile_sets_tunables_by_shape[test_section7_profile_sets_tunables_by_shape]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_section8_toy_decoder_matches_numpy[test_section8_toy_decoder_matches_numpy]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/tests/infrastructure</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_a_batchnorm_s_int64_counter_loads_beside_its_float_weights[test_a_batchnorm_s_int64_counter_loads_beside_its_float_weights]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_buffer_named_in_part_is_never_pooled[test_a_buffer_named_in_part_is_never_pooled]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_call_takes_exactly_the_declared_scalars[scalars_{'m': 1}-error_<class 'TypeError'>-match_unexpected keyword argument\(s\): \['m'\]]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_call_takes_exactly_the_declared_scalars[scalars_{'n': 1, 'm': 1}-error_<class 'TypeError'>-match_unexpected keyword argument\(s\): \['m'\]]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_call_takes_exactly_the_declared_scalars[scalars_{}-error_<class 'aie.utils.hostruntime.hostruntime.HostRuntimeError'>-match_dispatch scalar mismatch]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_design_links_the_same_objects_alone_or_composed[test_a_design_links_the_same_objects_alone_or_composed]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_field_the_repr_leaves_out_still_keys_the_build[test_a_field_the_repr_leaves_out_still_keys_the_build]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_filled_tree_has_the_checkpoints_names_shapes_and_dtypes[fill_random]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_filled_tree_has_the_checkpoints_names_shapes_and_dtypes[fill_unread]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_full_elf_refuses_a_dispatch_value[test_a_full_elf_refuses_a_dispatch_value]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_full_elf_takes_the_repeat_count_from_the_scratchpad[test_a_full_elf_takes_the_repeat_count_from_the_scratchpad]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_gap_between_fixed_allocations_is_used_when_it_fits[test_a_gap_between_fixed_allocations_is_used_when_it_fits]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_graph_records_the_same_steps_as_a_hand_written_runlist[test_a_graph_records_the_same_steps_as_a_hand_written_runlist]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_layer_index_far_past_its_layers_is_refused[test_a_layer_index_far_past_its_layers_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_parent_reached_only_through_slices_lives_from_first_to_last_slice[test_a_parent_reached_only_through_slices_lives_from_first_to_last_slice]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_pytorch_checkpoint_naming_another_global_is_refused[module_os-name_system]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_pytorch_checkpoint_naming_another_global_is_refused[module_torch-name_DoubleStorage]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_pytorch_checkpoint_naming_another_global_is_refused[module_torch._utils-name__rebuild_parameter]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_pytorch_tensor_outside_its_storage_is_refused[foreign_id]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_pytorch_tensor_outside_its_storage_is_refused[past_the_end]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_pytorch_tensor_outside_its_storage_is_refused[short_storage]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_resident_has_one_offset_in_every_image[test_a_resident_has_one_offset_in_every_image]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_resident_needs_a_size[test_a_resident_needs_a_size]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_session_not_asked_for_a_csv_writes_none[test_a_session_not_asked_for_a_csv_writes_none]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_session_split_over_workers_writes_every_result[test_a_session_split_over_workers_writes_every_result]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_session_that_dies_keeps_its_results_and_names_the_test[test_a_session_that_dies_keeps_its_results_and_names_the_test]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_test_failing_in_setup_is_a_failed_check[test_a_test_failing_in_setup_is_a_failed_check]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_traced_build_carries_the_lowered_module[test_a_traced_build_carries_the_lowered_module]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_version_compiled_after_the_first_call_grows_the_arena_and_keeps_state[test_a_version_compiled_after_the_first_call_grows_the_arena_and_keeps_state]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_version_reads_as_its_inputs_plan_and_build_directory[test_a_version_reads_as_its_inputs_plan_and_build_directory]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_worse_time_fails_the_run[faster]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_worse_time_fails_the_run[fewer_tokens_a_second]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_worse_time_fails_the_run[kl]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_worse_time_fails_the_run[slower_first_token]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_worse_time_fails_the_run[within]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_written_pytorch_tensor_reads_as_its_storage[test_a_written_pytorch_tensor_reads_as_its_storage]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aligned_row_count_records_with_the_given_extents[test_aligned_row_count_records_with_the_given_extents]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_argument_ends_past_the_arena_buffer_placed_last[test_an_argument_ends_past_the_arena_buffer_placed_last]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_opaque_design_parameter_is_rejected[test_an_opaque_design_parameter_is_rejected]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_operator_builds_its_own_image_once[test_an_operator_builds_its_own_image_once]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_auto_dispatch_selects_platform_default[size_4096]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_captured_graph_compiles_to_an_elf[test_captured_graph_compiles_to_an_elf]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_cgroup_limit_reads_the_lowest_ceiling[unbounded]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_cgroup_limit_reads_the_lowest_ceiling[v1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_cgroup_limit_reads_the_lowest_ceiling[v2-nested]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_check_mode_judges_each_step_by_its_tolerance[test_check_mode_judges_each_step_by_its_tolerance]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_check_mode_judges_every_output_at_the_calls_values[test_check_mode_judges_every_output_at_the_calls_values]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_checkpoint_matches_safetensors_for_every_dtype[test_checkpoint_matches_safetensors_for_every_dtype]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_checkpoint_reads_a_sharded_index[test_checkpoint_reads_a_sharded_index]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_checkpoint_refuses_a_shard_outside_the_index_s_directory[shard_../a.safetensors]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_checkpoint_refuses_a_shard_outside_the_index_s_directory[shard_/tmp/a.safetensors]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_checkpoint_rejects_a_malformed_file[range-before-the-data]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_checkpoint_rejects_a_malformed_file[range-not-the-shape]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_checkpoint_rejects_a_malformed_file[range-past-the-end]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_checkpoint_rejects_a_shard_that_disagrees_with_the_index[test_checkpoint_rejects_a_shard_that_disagrees_with_the_index]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_checkpoint_rejects_a_tensor_with_no_byte_range[test_checkpoint_rejects_a_tensor_with_no_byte_range]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_checkpoint_rejects_an_empty_archive[test_checkpoint_rejects_an_empty_archive]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_checkpoint_rejects_an_unsupported_dtype[test_checkpoint_rejects_an_unsupported_dtype]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_checkpoint_release_drops_the_right_shard[test_checkpoint_release_drops_the_right_shard]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_checkpoint_views_the_mapping_without_copying[test_checkpoint_views_the_mapping_without_copying]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_commands_are_runtime_sequences_over_the_same_designs[test_commands_are_runtime_sequences_over_the_same_designs]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_composed_mlir_contains_reconfiguration[sequence_add_relu]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_device_heap_exhaustion_is_a_failure[phase_call]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_device_heap_exhaustion_is_a_failure[phase_setup]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_device_rows_are_the_host_draws[test_device_rows_are_the_host_draws]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_device_rows_refuse_an_unbounded_top_k[test_device_rows_refuse_an_unbounded_top_k]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_dispatch_modes_bit_identical[dispatch_compare]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_dispatch_modes_bit_identical[dispatch_separate]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_download_fetches_into_the_cache_not_the_read_only_weights_dir[test_download_fetches_into_the_cache_not_the_read_only_weights_dir]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_download_shares_no_partial_file_with_a_concurrent_fetch[test_download_shares_no_partial_file_with_a_concurrent_fetch]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_draws_follow_the_distribution[test_draws_follow_the_distribution]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_checkpoint_tensor_lands_on_its_name_bitwise[test_each_checkpoint_tensor_lands_on_its_name_bitwise]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_runner_s_nightly_results_get_charts_of_their_own[test_each_runner_s_nightly_results_get_charts_of_their_own]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_step_versions_share_weights_and_state_through_one_arena[test_each_step_versions_share_weights_and_state_through_one_arena]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_empty_graph[test_empty_graph]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_every_dispatch_returns_its_own_output[calls_2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_every_dispatch_returns_its_own_output[calls_3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_feedback_argument_only_when_declared[test_feedback_argument_only_when_declared]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_fixed_allocations_are_obstacles_at_every_step[test_fixed_allocations_are_obstacles_at_every_step]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_graph_inputs_and_outputs_are_left_alone[test_graph_inputs_and_outputs_are_left_alone]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_greedy_is_argmax[test_greedy_is_argmax]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_identical_operators_reuse_the_compiled_xclbin[test_identical_operators_reuse_the_compiled_xclbin]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_identical_sequences_reuse_the_compiled_elf[test_identical_sequences_reuse_the_compiled_elf]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_importing_iron_and_its_applications_imports_no_torch_or_transformers[test_importing_iron_and_its_applications_imports_no_torch_or_transformers]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_kernel_objects_land_in_the_entry_under_bare_names[test_kernel_objects_land_in_the_entry_under_bare_names]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_live_range_overlap[test_live_range_overlap]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama3_scaling_matches_the_formula_in_every_band[test_llama3_scaling_matches_the_formula_in_every_band]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_load_hands_each_piece_of_each_weight_to_release_once_it_is_uploaded[test_load_hands_each_piece_of_each_weight_to_release_once_it_is_uploaded]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_load_loads_a_version_whose_weights_are_already_uploaded[test_load_loads_a_version_whose_weights_are_already_uploaded]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_misaligned_buffer_is_rejected[test_misaligned_buffer_is_rejected]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mixed_sizes_reach_the_lower_bound[test_mixed_sizes_reach_the_lower_bound]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_non_aligned_row_count_raises_instead_of_being_padded[test_non_aligned_row_count_raises_instead_of_being_padded]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_non_input_buffers_sync_without_explicit_flush[dispatch_separate]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_npu1_xclbin_pushes_the_call_s_repeat_count[test_npu1_xclbin_pushes_the_call_s_repeat_count]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_odd_sizes_never_leave_an_offset_unaligned[test_odd_sizes_never_leave_an_offset_unaligned]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offsets_are_aligned[test_offsets_are_aligned]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_design_expands_only_to_reconfigure[reconfigure_False]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_design_expands_only_to_reconfigure[reconfigure_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_image_serves_every_parameter[test_one_image_serves_every_parameter]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_storage_is_one_size[test_one_storage_is_one_size]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_pinned_buffers_are_not_pooled[test_pinned_buffers_are_not_pooled]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_fill_draws_a_bias_about_zero[test_random_fill_draws_a_bias_about_zero]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_fill_draws_at_its_seed[test_random_fill_draws_at_its_seed]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_10]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_11]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_12]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_13]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_14]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_15]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_17]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_18]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_19]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_5]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_6]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_7]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_random_images_keep_every_invariant[seed_9]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_real_checkpoint_every_tensor_bitwise[test_real_checkpoint_every_tensor_bitwise]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_real_checkpoint_is_llama_3_2_1b[test_real_checkpoint_is_llama_3_2_1b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_real_sharded_checkpoint_every_tensor_bitwise[test_real_sharded_checkpoint_every_tensor_bitwise]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_real_tokenizer_s_added_tokens_are_their_ids[test_real_tokenizer_s_added_tokens_are_their_ids]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_refuses_an_n_past_the_buffers[test_refuses_an_n_past_the_buffers]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_release_drops_the_pages_and_keeps_the_bytes[test_release_drops_the_pages_and_keeps_the_bytes]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_release_frees_the_buffers_and_the_next_call_loads_them_again[test_release_frees_the_buffers_and_the_next_call_loads_them_again]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_release_leaves_anything_else_alone[test_release_leaves_anything_else_alone]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_renamed_is_a_copy_a_caller_may_change[test_renamed_is_a_copy_a_caller_may_change]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_repeated_block_packs_to_one_block_worth[test_repeated_block_packs_to_one_block_worth]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_restricted_test_without_npu_runtime_skips_with_the_reason[test_restricted_test_without_npu_runtime_skips_with_the_reason]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_restricted_tests_skip_where_the_device_is_not_listed[test_restricted_tests_skip_where_the_device_is_not_listed]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rope_is_correctly_rounded_at_position_zero_and_one[test_rope_is_correctly_rounded_at_position_zero_and_one]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rope_is_the_formula_rounded_once[test_rope_is_the_formula_rounded_once]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_scaled_rope_table_rotates_by_the_scaled_frequencies[test_scaled_rope_table_rotates_by_the_scaled_frequencies]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_seeded_sampling_is_reproducible[test_seeded_sampling_is_reproducible]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_sequential_chain_double_buffers[test_sequential_chain_double_buffers]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_simultaneously_live_buffers_do_not_share[test_simultaneously_live_buffers_do_not_share]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_compile_key_covers_the_library_a_design_calls[test_the_compile_key_covers_the_library_a_design_calls]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_compile_key_is_stable_across_identical_operators[test_the_compile_key_is_stable_across_identical_operators]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_device_keys_the_build_by_identity_not_address[test_the_device_keys_the_build_by_identity_not_address]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_hook_holds_python_to_black[source_x = {  "a":1 }
-verdict_❌ Python formatting check failed][test_the_hook_holds_python_to_black[source_x = {  "a":1 }
-verdict_❌ Python formatting check failed]]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_hook_holds_python_to_black[source_x = {"a": 1}
-verdict_✅ Python formatting check passed][test_the_hook_holds_python_to_black[source_x = {"a": 1}
-verdict_✅ Python formatting check passed]]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_lm_testing_helpers_import_without_pytest[test_the_lm_testing_helpers_import_without_pytest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_prompt_text_repeats_past_its_end[test_the_prompt_text_repeats_past_its_end]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_stream_is_generated_per_call[test_the_stream_is_generated_per_call]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_top_k_keeps_ties_with_the_kth[test_top_k_keeps_ties_with_the_kth]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_top_k_never_leaves_the_top_k[test_top_k_never_leaves_the_top_k]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_touching_ranges_ignore_names_not_asked_for[test_touching_ranges_ignore_names_not_asked_for]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_touching_ranges_span_first_to_last_use_whatever_the_direction[test_touching_ranges_span_first_to_last_use_whatever_the_direction]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_tree_names_a_layer_past_the_last[test_tree_names_a_layer_past_the_last]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_tree_names_a_missing_tensor_by_its_path_and_file[test_tree_names_a_missing_tensor_by_its_path_and_file]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_tree_names_a_tensor_of_a_skipped_layer[test_tree_names_a_tensor_of_a_skipped_layer]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_two_graphs_get_distinct_cache_keys[test_two_graphs_get_distinct_cache_keys]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_unread_fill_zeroes_a_scalar[test_unread_fill_zeroes_a_scalar]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_unrestricted_tests_need_no_npu_runtime[test_unrestricted_tests_need_no_npu_runtime]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/tests/lm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_a_cache_attends_within_its_window[test_a_cache_attends_within_its_window]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_graph_held_at_two_paths_skips_the_second_paths_tensors[test_a_graph_held_at_two_paths_skips_the_second_paths_tensors]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_layer_reading_another_s_cache_projects_and_writes_no_keys[test_a_layer_reading_another_s_cache_projects_and_writes_no_keys]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_param_never_bound_is_named_at_record[test_a_param_never_bound_is_named_at_record]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_q_table_scaled_by_two_doubles_the_logits_scale[test_a_q_table_scaled_by_two_doubles_the_logits_scale]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_random_tree_draws_a_scalar_as_an_array[test_a_random_tree_draws_a_scalar_as_an_array]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_ring_restarts_at_the_chunk_while_it_holds_the_window_before[test_a_ring_restarts_at_the_chunk_while_it_holds_the_window_before]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_ring_s_chunk_attends_from_its_valid_rows_alone[test_a_ring_s_chunk_attends_from_its_valid_rows_alone]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_second_bind_is_refused[test_a_second_bind_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tied_param_ignores_a_tensor_at_its_other_path[test_a_tied_param_ignores_a_tensor_at_its_other_path]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_turn_over_a_ring_is_the_run_from_scratch_bit_for_bit[test_a_turn_over_a_ring_is_the_run_from_scratch_bit_for_bit]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_window_keeps_every_position_where_a_ring_takes_as_many_rows[test_a_window_keeps_every_position_where_a_ring_takes_as_many_rows]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_index_a_checkpoint_skips_is_empty_and_no_leaf[test_an_index_a_checkpoint_skips_is_empty_and_no_leaf]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_odd_vocabulary_pads_the_head_with_a_row_no_draw_takes[test_an_odd_vocabulary_pads_the_head_with_a_row_no_draw_takes]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_attention_refuses_a_norm_of_other_than_q_k_and_v[test_attention_refuses_a_norm_of_other_than_q_k_and_v]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_attention_turns_only_the_rotary_columns[test_attention_turns_only_the_rotary_columns]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_causal_conv_accepts_a_chunk_that_holds_its_history[chunk_1-kernel_2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_causal_conv_accepts_a_chunk_that_holds_its_history[chunk_2-kernel_3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_causal_conv_accepts_a_chunk_that_holds_its_history[chunk_4-kernel_4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_causal_conv_accepts_a_chunk_that_holds_its_history[chunk_4-kernel_5]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_causal_conv_accepts_a_chunk_that_holds_its_history[chunk_8-kernel_4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_causal_conv_refuses_a_chunk_shorter_than_its_history[chunk_1-kernel_3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_causal_conv_refuses_a_chunk_shorter_than_its_history[chunk_2-kernel_4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_causal_conv_refuses_a_chunk_shorter_than_its_history[chunk_2-kernel_5]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_conv2d[case_depthwise_13_rows-share_0.25]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_conv2d[case_depthwise_13_rows-share_1.0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_generation_check_prefills_its_whole_prompt[test_each_generation_check_prefills_its_whole_prompt]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_layer_reads_the_rows_of_its_own_rope[test_each_layer_reads_the_rows_of_its_own_rope]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_embedding_gemma2_is_on_npu[test_embedding_gemma2_is_on_npu]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemma4_towers_are_on_npu[test_gemma4_towers_are_on_npu]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_leaf_modules_match_numpy[test_leaf_modules_match_numpy]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_load_state_dict_casts_to_the_params_dtype[test_load_state_dict_casts_to_the_params_dtype]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_load_state_dict_names_each_kind_in_one_error[test_load_state_dict_names_each_kind_in_one_error]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_load_state_dict_refuses_a_change_of_kind[test_load_state_dict_refuses_a_change_of_kind]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_load_state_dict_refuses_a_param_in_a_frozen_dataclass[test_load_state_dict_refuses_a_param_in_a_frozen_dataclass]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_load_state_dict_refuses_a_param_in_a_tuple[test_load_state_dict_refuses_a_param_in_a_tuple]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_log_mel[frames_200]</td><td>✅ 1/1</td><td>27808.39</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_log_mel[frames_3072]</td><td>✅ 1/1</td><td>33217.41</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_tensors_at_indices_are_a_list_of_tensors[test_tensors_at_indices_are_a_list_of_tensors]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/tests/operators</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_a_bounded_gather_moves_its_rows_and_a_unit_for_each_other[test_a_bounded_gather_moves_its_rows_and_a_unit_for_each_other]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_gather_of_rows_not_whole_16_byte_units_is_refused[test_a_bounded_gather_of_rows_not_whole_16_byte_units_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_prompt_chunk_moves_13_rows_not_2048[test_a_bounded_prompt_chunk_moves_13_rows_not_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_float32_softmax_under_a_per_call_bound_is_refused[test_a_float32_softmax_under_a_per_call_bound_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_gather_feeding_from_more_shim_pairs_than_the_device_has_is_refused[name_npu1-feeds_3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_gather_feeding_from_more_shim_pairs_than_the_device_has_is_refused[name_npu2-feeds_0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_gather_feeding_from_more_shim_pairs_than_the_device_has_is_refused[name_npu2-feeds_5]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_gather_whose_feeds_outnumber_its_batch_pairs_is_refused[test_a_gather_whose_feeds_outnumber_its_batch_pairs_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_given_raster_keeps_the_rows_past_the_image[test_a_given_raster_keeps_the_rows_past_the_image]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_line_of_part_of_a_vector_is_refused[limbs]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_line_of_part_of_a_vector_is_refused[magnitude]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_prompt_chunk_s_rows_are_gathered_each_call[test_a_prompt_chunk_s_rows_are_gathered_each_call]</td><td>✅ 1/1</td><td>4262.59</td><td>0.49</td><td>n/a</td></tr>
        <tr><td>test_a_short_m_takes_fewer_rows_of_cores[device_npu1-precision_high-M_16-rows_1-tile_m_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_short_m_takes_fewer_rows_of_cores[device_npu1-precision_high-M_32-rows_2-tile_m_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_short_m_takes_fewer_rows_of_cores[device_npu2-precision_high-M_16-rows_2-tile_m_8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_short_m_takes_fewer_rows_of_cores[device_npu2-precision_medium-M_32-rows_2-tile_m_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_streamed_softmax_core_with_more_rows_than_it_unrolls_is_refused[test_a_streamed_softmax_core_with_more_rows_than_it_unrolls_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tile_past_what_one_core_holds_is_refused_not_split[test_a_tile_past_what_one_core_holds_is_refused_not_split]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_validate_or_compatible_branch_refuses[clamp_bounds]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_validate_or_compatible_branch_refuses[conv_channels]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_validate_or_compatible_branch_refuses[conv_runs]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_validate_or_compatible_branch_refuses[emit_rows]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_validate_or_compatible_branch_refuses[rope_angle_rows]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_validate_or_compatible_branch_refuses[rope_angle_rows_split]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_validate_or_compatible_branch_refuses[rope_cols]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_validate_or_compatible_branch_refuses[rope_rows_split]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_validate_or_compatible_branch_refuses[softmax_f32_option]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_validate_or_compatible_branch_refuses[softmax_window_alone]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_validate_or_compatible_branch_refuses[softmax_window_no_addend]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_walk_by_a_per_call_repeat_and_length_is_its_reference[band_stride_0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_walk_by_a_per_call_repeat_and_length_is_its_reference[band_stride_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_activations_bring_their_lut_tables_into_the_frame[test_aie2_activations_bring_their_lut_tables_into_the_frame]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_16-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_16-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_16-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_16-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_32-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_32-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_32-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_32-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_64-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_64-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_64-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_128-tile_ma_64-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_16-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_16-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_16-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_16-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_32-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_32-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_32-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_32-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_64-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_64-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_64-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_1-ct_k_32-tile_ma_64-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_16-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_16-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_16-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_16-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_32-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_32-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_32-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_32-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_64-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_64-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_64-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_128-tile_ma_64-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_16-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_16-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_16-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_16-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_32-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_32-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_32-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_32-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_64-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_64-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_64-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_aie2_tile_validation_includes_the_frame[m_chunk_2-ct_k_32-tile_ma_64-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_input_gathers_from_a_table_once[test_an_input_gathers_from_a_table_once]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_m_no_tile_splits_is_rejected[device_npu1-precision_high]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_m_no_tile_splits_is_rejected[device_npu2-precision_medium]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_open_tile_m_is_the_widest_that_splits_m[device_npu1-precision_high-M_64-tile_m_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_open_tile_m_is_the_widest_that_splits_m[device_npu2-precision_high-M_32-tile_m_8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_open_tile_m_is_the_widest_that_splits_m[device_npu2-precision_medium-M_128-tile_m_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_open_tile_m_is_the_widest_that_splits_m[device_npu2-precision_medium-M_2048-tile_m_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_open_tile_m_is_the_widest_that_splits_m[device_npu2-precision_medium-M_64-tile_m_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_b_ring_divides_the_chunks_a_k_step_consumes[ct_k_32-chunks_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_b_ring_divides_the_chunks_a_k_step_consumes[ct_k_32-chunks_3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_b_ring_divides_the_chunks_a_k_step_consumes[ct_k_64-chunks_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_b_ring_divides_the_chunks_a_k_step_consumes[ct_k_64-chunks_3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_bounded_rows_past_a_wrap_halve_the_run[test_bounded_rows_past_a_wrap_halve_the_run]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_buffers_do_not_follow_the_pipeline_count[test_buffers_do_not_follow_the_pipeline_count]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_bytes_match_pack_b[K_1024-N_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_bytes_match_pack_b[K_1536-N_640]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_bytes_match_pack_b[K_2048-N_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_bytes_match_pack_b[K_2048-N_256]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_bytes_match_pack_b[K_512-N_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_channels_not_dividing_the_shared_run_are_rejected[test_channels_not_dividing_the_shared_run_are_rejected]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu1-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu1-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu1-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu1-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu2-tile_n_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu2-tile_n_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu2-tile_n_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_default_k_slice_is_the_deepest_that_fits_double_buffered[device_npu2-tile_n_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_default_tiles_account_for_the_frame[device_npu1-b_bytes_2-tile_n_128-expected_(32, 32, 2)]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_default_tiles_account_for_the_frame[device_npu1-b_bytes_2-tile_n_64-expected_(64, 64, 2)]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_default_tiles_account_for_the_frame[device_npu2-b_bytes_1.125-tile_n_128-expected_(64, 32, 2)]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_default_tiles_account_for_the_frame[device_npu2-b_bytes_1.125-tile_n_64-expected_(128, 32, 2)]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_descriptors_are_dma_expressible[test_descriptors_are_dma_expressible]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_step_gathers_by_ids_the_device_made[n_ids_15]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_step_gathers_by_ids_the_device_made[n_ids_512]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_step_gathers_the_rows_a_call_bounds[n_ids_15]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_step_gathers_the_rows_a_call_bounds[n_ids_256]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_step_gathers_the_rows_a_call_bounds_by_ids_the_device_made[n_ids_15]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_step_gathers_the_rows_a_call_bounds_by_ids_the_device_made[n_ids_256]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_each_step_gathers_the_rows_an_input_names[test_each_step_gathers_the_rows_an_input_names]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_every_operator_is_in_the_catalog[test_every_operator_is_in_the_catalog]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_explicit_aie2_tile_falls_back_to_single_buffered_b[test_explicit_aie2_tile_falls_back_to_single_buffered_b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_decode_layer_rejects_unknown_configurations[geometry]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_decode_layer_rejects_unknown_configurations[layer_type]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_dequant_rejects_unservable_shapes[K_1000-N_128-match_K \(1000\)]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_dequant_rejects_unservable_shapes[K_1024-N_100-match_N \(100\)]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_gemm_reads_b_as_stored_in_bf16[test_flm_gemm_reads_b_as_stored_in_bf16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_lm_head_rejects_unservable_shapes[dim_1000-vocab_4096-softcap_30.0-match_dim \(1000\) must be a multiple]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_lm_head_rejects_unservable_shapes[dim_1536-vocab_1000-softcap_30.0-match_vocab \(1000\) must be a multiple]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_lm_head_rejects_unservable_shapes[dim_1536-vocab_4096-softcap_0.0-match_finite and positive]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_prefill_attention_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 0}-match_must be positive]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_prefill_attention_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 3}-match_multiple of]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_prefill_attention_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 8}-match_query heads]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_prefill_attention_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 1, 'window': 500}-match_multiple of 128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_on_columns_that_do_not_divide_its_rows_is_refused[device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_on_columns_that_do_not_divide_its_rows_is_refused[device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_the_kernel_cannot_build_is_rejected[k4_emulated]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_the_kernel_cannot_build_is_rejected[m8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_the_kernel_cannot_build_is_rejected[m8_emulated]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_the_kernel_cannot_build_is_rejected[n8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_merge_of_no_or_repeated_placeholders_is_refused[placeholders_((7, 0), (7, 64))]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_merge_of_no_or_repeated_placeholders_is_refused[placeholders_()]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_merge_of_part_of_a_block_is_refused[test_merge_of_part_of_a_block_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_band_and_head_that_do_not_tile_are_refused[block_past_the_padding]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_band_and_head_that_do_not_tile_are_refused[empty_window]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_band_and_head_that_do_not_tile_are_refused[head_not_whole_64]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_band_and_head_that_do_not_tile_are_refused[negative_scale]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_of_one_query_that_does_not_pack_is_refused[group_past_a_block]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_of_one_query_that_does_not_pack_is_refused[more_than_four_pipelines]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_of_one_query_that_does_not_pack_is_refused[uneven_groups]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_one_query_packed_takes_the_narrowest_block_and_64_keys[test_mha_one_query_packed_takes_the_narrowest_block_and_64_keys]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_whose_blocks_do_not_line_up_is_refused[kv_len_not_whole_blocks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_whose_blocks_do_not_line_up_is_refused[kv_len_short_of_queries]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_whose_head_fits_no_block_is_refused[test_mha_whose_head_fits_no_block_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_whose_pipelines_do_not_fill_the_rows_is_refused[test_mha_whose_pipelines_do_not_fill_the_rows_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_whose_pv_split_does_not_route_is_refused[one_query_packed]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_whose_pv_split_does_not_route_is_refused[six_pipelines_to_a_join]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha_whose_pv_split_does_not_route_is_refused[three_ways]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-AXPY-size_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0]</td><td>✅ 1/1</td><td>33.68</td><td>0.18</td><td>0.06</td></tr>
        <tr><td>test_operator[npu1-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003]</td><td>✅ 1/1</td><td>23.18</td><td>0.53</td><td>0.18</td></tr>
        <tr><td>test_operator[npu1-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]</td><td>✅ 1/1</td><td>22.05</td><td>0.56</td><td>0.19</td></tr>
        <tr><td>test_operator[npu1-AXPY-size_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0]</td><td>✅ 1/1</td><td>29.52</td><td>0.42</td><td>0.14</td></tr>
        <tr><td>test_operator[npu1-AXPY-size_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0]</td><td>✅ 1/1</td><td>23.80</td><td>1.03</td><td>0.34</td></tr>
        <tr><td>test_operator[npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0]</td><td>✅ 1/1</td><td>3305.17</td><td>15.23</td><td>5.08</td></tr>
        <tr><td>test_operator[npu1-Clamp-size_1024-num_aie_columns_4-num_channels_2-tile_size_128-low_-0.75-high_1.25]</td><td>✅ 1/1</td><td>50.30</td><td>0.08</td><td>0.02</td></tr>
        <tr><td>test_operator[npu1-Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25]</td><td>✅ 1/1</td><td>24.90</td><td>0.33</td><td>0.08</td></tr>
        <tr><td>test_operator[npu1-Clamp-size_2048-num_aie_columns_1-tile_size_2048-low_0.5-high_1.5]</td><td>✅ 1/1</td><td>24.98</td><td>0.33</td><td>0.08</td></tr>
        <tr><td>test_operator[npu1-Clamp-size_2048-num_aie_columns_2-tile_size_1024-low_-30000.0-high_30000.0]</td><td>✅ 1/1</td><td>23.10</td><td>0.35</td><td>0.09</td></tr>
        <tr><td>test_operator[npu1-Clamp-size_2048-num_aie_columns_4-num_channels_2-tile_size_256-low_-0.75-high_1.25]</td><td>✅ 1/1</td><td>58.81</td><td>0.14</td><td>0.03</td></tr>
        <tr><td>test_operator[npu1-Clamp-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096-low_-0.75-high_1.25]</td><td>✅ 1/1</td><td>27.01</td><td>0.61</td><td>0.15</td></tr>
        <tr><td>test_operator[npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25]</td><td>✅ 1/1</td><td>1119.15</td><td>29.98</td><td>7.50</td></tr>
        <tr><td>test_operator[npu1-Copy-bench_flat_4mi]</td><td>✅ 1/1</td><td>3168.56</td><td>5.29</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Copy-by_head_two_channels]</td><td>✅ 1/1</td><td>18.65</td><td>0.88</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Copy-chunked_transfer]</td><td>✅ 1/1</td><td>20.61</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Copy-contiguous]</td><td>✅ 1/1</td><td>18.82</td><td>0.22</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Copy-float32]</td><td>✅ 1/1</td><td>23.27</td><td>0.35</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Copy-past_one_memtile]</td><td>✅ 1/1</td><td>547.96</td><td>3.83</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Copy-slot5]</td><td>✅ 1/1</td><td>17.67</td><td>7.47</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Copy-slot5_two_channels]</td><td>✅ 1/1</td><td>20.29</td><td>6.51</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Copy-slot_last]</td><td>✅ 1/1</td><td>15.90</td><td>8.31</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Copy-two_channels]</td><td>✅ 1/1</td><td>21.18</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-DepthwiseConv1d-rows_32-channels_96-num_aie_columns_4]</td><td>✅ 1/1</td><td>28.61</td><td>0.46</td><td>1.07</td></tr>
        <tr><td>test_operator[npu1-DepthwiseConv1d-rows_64-channels_256-num_aie_columns_2]</td><td>✅ 1/1</td><td>25.30</td><td>2.69</td><td>6.48</td></tr>
        <tr><td>test_operator[npu1-DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1]</td><td>✅ 1/1</td><td>26.85</td><td>0.63</td><td>1.53</td></tr>
        <tr><td>test_operator[npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4]</td><td>✅ 1/1</td><td>329.06</td><td>9.59</td><td>23.90</td></tr>
        <tr><td>test_operator[npu1-ElementwiseAdd-size_1024-num_aie_columns_4-tile_size_256]</td><td>✅ 1/1</td><td>34.16</td><td>0.18</td><td>0.03</td></tr>
        <tr><td>test_operator[npu1-ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 1/1</td><td>23.98</td><td>0.51</td><td>0.09</td></tr>
        <tr><td>test_operator[npu1-ElementwiseAdd-size_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 1/1</td><td>31.06</td><td>0.40</td><td>0.07</td></tr>
        <tr><td>test_operator[npu1-ElementwiseAdd-size_4096-num_aie_columns_1-tile_size_4096]</td><td>✅ 1/1</td><td>39.79</td><td>0.62</td><td>0.10</td></tr>
        <tr><td>test_operator[npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096]</td><td>✅ 1/1</td><td>2457.79</td><td>20.48</td><td>3.41</td></tr>
        <tr><td>test_operator[npu1-ElementwiseMul-size_1024-num_aie_columns_4-tile_size_256]</td><td>✅ 1/1</td><td>30.41</td><td>0.20</td><td>0.03</td></tr>
        <tr><td>test_operator[npu1-ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 1/1</td><td>23.85</td><td>0.52</td><td>0.09</td></tr>
        <tr><td>test_operator[npu1-ElementwiseMul-size_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 1/1</td><td>31.37</td><td>0.39</td><td>0.07</td></tr>
        <tr><td>test_operator[npu1-ElementwiseMul-size_4096-num_aie_columns_1-tile_size_4096]</td><td>✅ 1/1</td><td>25.07</td><td>0.98</td><td>0.16</td></tr>
        <tr><td>test_operator[npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096]</td><td>✅ 1/1</td><td>3153.62</td><td>15.96</td><td>2.66</td></tr>
        <tr><td>test_operator[npu1-Emit-eight_carried]</td><td>✅ 1/1</td><td>27.37</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Emit-one_carried]</td><td>✅ 1/1</td><td>18.46</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-GELU-size_1024-num_aie_columns_4-num_channels_2-tile_size_128-approximate_none]</td><td>✅ 1/1</td><td>49.30</td><td>0.08</td><td>0.02</td></tr>
        <tr><td>test_operator[npu1-GELU-size_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 1/1</td><td>47.20</td><td>0.09</td><td>0.02</td></tr>
        <tr><td>test_operator[npu1-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-approximate_none]</td><td>✅ 1/1</td><td>52.14</td><td>0.16</td><td>0.04</td></tr>
        <tr><td>test_operator[npu1-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>29.81</td><td>0.27</td><td>0.07</td></tr>
        <tr><td>test_operator[npu1-GELU-size_2048-num_aie_columns_4-num_channels_2-tile_size_256-approximate_none]</td><td>✅ 1/1</td><td>43.30</td><td>0.19</td><td>0.05</td></tr>
        <tr><td>test_operator[npu1-GELU-size_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 1/1</td><td>45.14</td><td>0.18</td><td>0.05</td></tr>
        <tr><td>test_operator[npu1-GELU-size_8192-num_aie_columns_1-num_channels_1-tile_size_8192-approximate_none]</td><td>✅ 1/1</td><td>126.72</td><td>0.26</td><td>0.06</td></tr>
        <tr><td>test_operator[npu1-GELU-size_8192-num_aie_columns_1-num_channels_1-tile_size_8192]</td><td>✅ 1/1</td><td>43.72</td><td>0.75</td><td>0.19</td></tr>
        <tr><td>test_operator[npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 1/1</td><td>3091.22</td><td>10.85</td><td>2.71</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_1024-K_2560-N_10240-num_aie_columns_4-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest]</td><td>✅ 1/1</td><td>25877.41</td><td>3.04</td><td>2074.67</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_1792-K_896-N_1152-num_aie_columns_4-tile_m_64-tile_k_32-tile_n_48-b_col_maj_False-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>2454.13</td><td>3.83</td><td>1507.41</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_192-K_384-N_64-num_aie_columns_4-tile_m_48-tile_k_96-tile_n_16-b_col_maj_True-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>58.43</td><td>3.79</td><td>161.51</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True]</td><td>✅ 1/1</td><td>7817.10</td><td>3.22</td><td>2197.73</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest]</td><td>✅ 1/1</td><td>79280.23</td><td>0.32</td><td>216.70</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-precision_medium-placement_tiles]</td><td>✅ 1/1</td><td>18061.39</td><td>1.39</td><td>951.19</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest]</td><td>✅ 1/1</td><td>17966.51</td><td>1.40</td><td>956.22</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_4-tile_m_128-tile_k_32-tile_n_32-b_col_maj_True-c_col_maj_False-precision_highest]</td><td>✅ 1/1</td><td>12261.54</td><td>2.05</td><td>1401.12</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_4-tile_m_32-tile_k_32-tile_n_128-b_col_maj_False-c_col_maj_False-precision_highest]</td><td>✅ 1/1</td><td>12310.22</td><td>2.04</td><td>1395.58</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_4-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>8428.04</td><td>2.99</td><td>2038.42</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_2048-K_2048-N_8192-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest]</td><td>✅ 1/1</td><td>71490.37</td><td>1.06</td><td>961.24</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_2048-K_64-N_2048-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest]</td><td>✅ 1/1</td><td>1760.21</td><td>5.06</td><td>305.00</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_2048-K_64-N_8192-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest]</td><td>✅ 1/1</td><td>5321.57</td><td>6.55</td><td>403.54</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_2048-K_8192-N_2048-num_aie_columns_2-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest]</td><td>✅ 1/1</td><td>75257.45</td><td>1.00</td><td>913.13</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_32-K_1152-N_2048-num_aie_columns_4-tile_m_16-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>348.25</td><td>14.14</td><td>433.59</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_384-K_1536-N_1792-num_aie_columns_4-tile_m_32-tile_k_48-tile_n_64-b_col_maj_True-c_col_maj_False-precision_highest]</td><td>✅ 1/1</td><td>3491.08</td><td>2.31</td><td>605.52</td></tr>
        <tr><td>test_operator[npu1-GEMM-M_896-K_1792-N_640-num_aie_columns_4-tile_m_32-tile_k_64-tile_n_80-b_col_maj_False-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>2390.51</td><td>2.78</td><td>859.74</td></tr>
        <tr><td>test_operator[npu1-GEMM-f32_out]</td><td>✅ 1/1</td><td>299.87</td><td>5.25</td><td>447.59</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2]</td><td>✅ 1/1</td><td>1074.59</td><td>3.91</td><td>3.90</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_4-repeat_2]</td><td>✅ 1/1</td><td>2092.96</td><td>2.01</td><td>4.01</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2]</td><td>✅ 1/1</td><td>329.27</td><td>0.81</td><td>0.80</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 1/1</td><td>39.64</td><td>0.84</td><td>0.83</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64]</td><td>✅ 1/1</td><td>3246.93</td><td>11.63</td><td>11.63</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_2048-K_64-num_aie_columns_4-tile_size_input_4-tile_size_output_256-num_batches_32-repeat_4]</td><td>✅ 1/1</td><td>645.74</td><td>3.46</td><td>12.99</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_2048-K_64-num_aie_columns_4-tile_size_input_4-tile_size_output_256-num_channels_2-num_batches_32-repeat_4]</td><td>✅ 1/1</td><td>580.59</td><td>3.84</td><td>14.45</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256]</td><td>✅ 1/1</td><td>2686.03</td><td>12.50</td><td>12.49</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4]</td><td>✅ 1/1</td><td>150.62</td><td>1.76</td><td>1.74</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_32-num_channels_2-num_batches_8]</td><td>✅ 1/1</td><td>93.83</td><td>5.65</td><td>5.59</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_64-num_batches_4-repeat_4]</td><td>✅ 1/1</td><td>93.37</td><td>0.73</td><td>2.81</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_256-K_128-num_aie_columns_2-tile_size_input_1-tile_size_output_64-num_batches_8-repeat_4]</td><td>✅ 1/1</td><td>156.18</td><td>0.88</td><td>3.36</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_256-K_128-num_aie_columns_4-tile_size_input_1-tile_size_output_32-num_batches_100]</td><td>✅ 1/1</td><td>834.62</td><td>7.94</td><td>7.85</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_448-K_64-num_aie_columns_4-tile_size_input_1-tile_size_output_56-num_batches_192]</td><td>✅ 1/1</td><td>3016.80</td><td>3.71</td><td>3.65</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_512-K_64-num_aie_columns_4-tile_size_input_4-tile_size_output_64-num_batches_32]</td><td>✅ 1/1</td><td>275.16</td><td>7.76</td><td>7.62</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8]</td><td>✅ 1/1</td><td>418.05</td><td>3.82</td><td>3.76</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024]</td><td>✅ 1/1</td><td>3005.03</td><td>11.17</td><td>11.17</td></tr>
        <tr><td>test_operator[npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2]</td><td>✅ 1/1</td><td>3228.16</td><td>10.40</td><td>10.39</td></tr>
        <tr><td>test_operator[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 1/1</td><td>18.96</td><td>0.65</td><td>0.65</td></tr>
        <tr><td>test_operator[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>24.55</td><td>0.33</td><td>0.50</td></tr>
        <tr><td>test_operator[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True]</td><td>✅ 1/1</td><td>21.27</td><td>1.16</td><td>1.16</td></tr>
        <tr><td>test_operator[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_8192]</td><td>✅ 1/1</td><td>29.88</td><td>1.10</td><td>1.64</td></tr>
        <tr><td>test_operator[npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True]</td><td>✅ 1/1</td><td>3227.82</td><td>10.40</td><td>15.59</td></tr>
        <tr><td>test_operator[npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 1/1</td><td>1136.98</td><td>29.51</td><td>44.27</td></tr>
        <tr><td>test_operator[npu1-LayerNorm-rows_4-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 1/1</td><td>30.26</td><td>0.30</td><td>0.41</td></tr>
        <tr><td>test_operator[npu1-LayerNorm-rows_4-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True]</td><td>✅ 1/1</td><td>33.22</td><td>0.14</td><td>0.18</td></tr>
        <tr><td>test_operator[npu1-LayerNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 1/1</td><td>48.01</td><td>0.09</td><td>0.13</td></tr>
        <tr><td>test_operator[npu1-LayerNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 1/1</td><td>32.35</td><td>0.25</td><td>0.38</td></tr>
        <tr><td>test_operator[npu1-Limbs-rows_4096-line_320-num_aie_columns_4]</td><td>✅ 1/1</td><td>3110.18</td><td>6.74</td><td>0.42</td></tr>
        <tr><td>test_operator[npu1-Limbs-rows_512-line_320-num_aie_columns_4]</td><td>✅ 1/1</td><td>161.54</td><td>16.23</td><td>1.01</td></tr>
        <tr><td>test_operator[npu1-Limbs-rows_64-line_160-num_aie_columns_1]</td><td>✅ 1/1</td><td>59.89</td><td>2.74</td><td>0.17</td></tr>
        <tr><td>test_operator[npu1-Log-size_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 1/1</td><td>48.71</td><td>0.13</td><td>0.02</td></tr>
        <tr><td>test_operator[npu1-Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>63.98</td><td>0.19</td><td>0.03</td></tr>
        <tr><td>test_operator[npu1-Log-size_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 1/1</td><td>50.45</td><td>0.24</td><td>0.04</td></tr>
        <tr><td>test_operator[npu1-Log-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 1/1</td><td>96.01</td><td>0.26</td><td>0.04</td></tr>
        <tr><td>test_operator[npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 1/1</td><td>22751.84</td><td>2.21</td><td>0.37</td></tr>
        <tr><td>test_operator[npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4]</td><td>✅ 1/1</td><td>81348.76</td><td>0.10</td><td>422.40</td></tr>
        <tr><td>test_operator[npu1-MHA-num_heads_24-num_KV_heads_8-d_128-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True]</td><td>✅ 1/1</td><td>755.52</td><td>11.12</td><td>33.31</td></tr>
        <tr><td>test_operator[npu1-MHA-num_heads_32-num_KV_heads_8-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True]</td><td>✅ 1/1</td><td>355.38</td><td>11.83</td><td>47.21</td></tr>
        <tr><td>test_operator[npu1-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_1-kv_len_2048-window_511-num_pipelines_1-heads_interleaved_True]</td><td>✅ 1/1</td><td>312.49</td><td>6.72</td><td>6.71</td></tr>
        <tr><td>test_operator[npu1-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_512-kv_len_2048-window_511-num_pipelines_4-heads_interleaved_True]</td><td>✅ 1/1</td><td>11478.72</td><td>0.37</td><td>93.54</td></tr>
        <tr><td>test_operator[npu1-MHA-num_heads_4-num_KV_heads_1-seq_len_2000-d_512-causal_False-num_pipelines_4]</td><td>✅ 1/1</td><td>65420.59</td><td>0.32</td><td>500.88</td></tr>
        <tr><td>test_operator[npu1-MHA-num_heads_4-num_KV_heads_2-seq_len_2000-d_256-causal_False-window_512-num_pipelines_4]</td><td>✅ 1/1</td><td>49104.12</td><td>0.26</td><td>149.09</td></tr>
        <tr><td>test_operator[npu1-MHA-num_heads_40-num_KV_heads_8-d_64-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True]</td><td>✅ 1/1</td><td>360.39</td><td>11.67</td><td>58.19</td></tr>
        <tr><td>test_operator[npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_1-kv_len_512-num_pipelines_1]</td><td>✅ 1/1</td><td>83.51</td><td>3.16</td><td>12.56</td></tr>
        <tr><td>test_operator[npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4]</td><td>✅ 1/1</td><td>640716.64</td><td>0.07</td><td>429.04</td></tr>
        <tr><td>test_operator[npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-d_128-num_pipelines_4]</td><td>✅ 1/1</td><td>40589.80</td><td>0.26</td><td>211.73</td></tr>
        <tr><td>test_operator[npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_4]</td><td>✅ 1/1</td><td>57990.46</td><td>0.14</td><td>518.48</td></tr>
        <tr><td>test_operator[npu1-Magnitude-rows_4096-width_640-num_aie_columns_4]</td><td>✅ 1/1</td><td>3417.31</td><td>4.60</td><td>0.38</td></tr>
        <tr><td>test_operator[npu1-Magnitude-rows_512-width_640-num_aie_columns_4]</td><td>✅ 1/1</td><td>434.01</td><td>4.53</td><td>0.38</td></tr>
        <tr><td>test_operator[npu1-Magnitude-rows_64-width_640-num_aie_columns_1]</td><td>✅ 1/1</td><td>231.84</td><td>1.06</td><td>0.09</td></tr>
        <tr><td>test_operator[npu1-Merge-rows_128-placeholders_((0, 0), (1, 40), (2, 20))-offset_True]</td><td>✅ 1/1</td><td>24.39</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Merge-rows_128-placeholders_((0, 0), (1, 40), (2, 20))]</td><td>✅ 1/1</td><td>19.94</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Merge-rows_192-block_32-placeholders_((258881, 2048), (258880, 2560))]</td><td>✅ 1/1</td><td>29.29</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Merge-rows_192-placeholders_((49190, 64),)]</td><td>✅ 1/1</td><td>22.04</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))-offset_True]</td><td>✅ 1/1</td><td>96.43</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))]</td><td>✅ 1/1</td><td>79.52</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-PatchPositions-rows_2048-out_height_480-out_width_1056-cores_8]</td><td>✅ 1/1</td><td>104.77</td><td>0.39</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-PatchPositions-rows_2304-out_height_768-out_width_768]</td><td>✅ 1/1</td><td>123.41</td><td>0.37</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-PatchPositions-rows_256-out_height_48-out_width_48]</td><td>✅ 1/1</td><td>25.14</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-PatchPositions-rows_2560-out_height_672-out_width_912]</td><td>✅ 1/1</td><td>124.99</td><td>0.41</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 1/1</td><td>23.29</td><td>0.53</td><td>0.35</td></tr>
        <tr><td>test_operator[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>18.51</td><td>0.44</td><td>0.44</td></tr>
        <tr><td>test_operator[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True]</td><td>✅ 1/1</td><td>30.45</td><td>0.81</td><td>0.54</td></tr>
        <tr><td>test_operator[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_8192]</td><td>✅ 1/1</td><td>29.78</td><td>1.10</td><td>1.10</td></tr>
        <tr><td>test_operator[npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True]</td><td>✅ 1/1</td><td>2596.17</td><td>12.93</td><td>12.92</td></tr>
        <tr><td>test_operator[npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 1/1</td><td>2987.44</td><td>11.23</td><td>11.23</td></tr>
        <tr><td>test_operator[npu1-RMSNorm-rows_4-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 1/1</td><td>38.62</td><td>0.24</td><td>0.21</td></tr>
        <tr><td>test_operator[npu1-RMSNorm-rows_4-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True]</td><td>✅ 1/1</td><td>31.21</td><td>0.15</td><td>0.13</td></tr>
        <tr><td>test_operator[npu1-RMSNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 1/1</td><td>48.45</td><td>0.08</td><td>0.08</td></tr>
        <tr><td>test_operator[npu1-RMSNorm-rows_8-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 1/1</td><td>50.03</td><td>0.16</td><td>0.16</td></tr>
        <tr><td>test_operator[npu1-ReLU-size_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 1/1</td><td>48.24</td><td>0.08</td><td>0.02</td></tr>
        <tr><td>test_operator[npu1-ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>23.32</td><td>0.35</td><td>0.09</td></tr>
        <tr><td>test_operator[npu1-ReLU-size_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 1/1</td><td>47.68</td><td>0.17</td><td>0.04</td></tr>
        <tr><td>test_operator[npu1-ReLU-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 1/1</td><td>25.93</td><td>0.63</td><td>0.16</td></tr>
        <tr><td>test_operator[npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 1/1</td><td>3139.77</td><td>10.69</td><td>2.67</td></tr>
        <tr><td>test_operator[npu1-Resample-height_3024-width_4032-out_height_672-out_width_912]</td><td>✅ 1/1</td><td>50621.80</td><td>0.82</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Resample-height_37-width_53-out_height_96-out_width_144]</td><td>✅ 1/1</td><td>318.34</td><td>1.08</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Resample-height_37-width_53-out_height_96-out_width_256]</td><td>✅ 1/1</td><td>920.22</td><td>0.45</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Resample-height_480-width_640-out_height_480-out_width_1008-num_aie_columns_4]</td><td>✅ 1/1</td><td>8181.33</td><td>0.62</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Resample-height_6000-width_500-out_height_672-out_width_432]</td><td>✅ 1/1</td><td>32627.23</td><td>0.82</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-ResampleTaps-in_size_1-out_size_48-num_aie_columns_2]</td><td>✅ 1/1</td><td>1956.93</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-ResampleTaps-in_size_17-out_size_1008]</td><td>✅ 1/1</td><td>4965.28</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-ResampleTaps-in_size_3024-out_size_672-words_356-slots_16]</td><td>✅ 1/1</td><td>12288.95</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-ResampleTaps-in_size_4032-out_size_912]</td><td>✅ 1/1</td><td>15728.14</td><td>0.00</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-ResampleTaps-in_size_8000-out_size_672-num_aie_columns_1-num_channels_1]</td><td>✅ 1/1</td><td>214179.44</td><td>0.00</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-ResampleTaps-in_size_961-out_size_960]</td><td>✅ 1/1</td><td>4026.17</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-RoPE-rows_32-cols_128-num_aie_columns_1-angle_rows_8-two_halves_False]</td><td>✅ 1/1</td><td>23.76</td><td>0.78</td><td>0.52</td></tr>
        <tr><td>test_operator[npu1-RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8]</td><td>✅ 1/1</td><td>30.02</td><td>2.46</td><td>1.64</td></tr>
        <tr><td>test_operator[npu1-RoPE-rows_32-cols_512-num_aie_columns_4-angle_rows_32]</td><td>✅ 1/1</td><td>30.32</td><td>3.24</td><td>1.62</td></tr>
        <tr><td>test_operator[npu1-RoPE-rows_4096-cols_512-angle_rows_8]</td><td>✅ 1/1</td><td>322.42</td><td>26.04</td><td>19.51</td></tr>
        <tr><td>test_operator[npu1-RoPE-rows_64-cols_128-num_aie_columns_4-angle_rows_16]</td><td>✅ 1/1</td><td>32.23</td><td>1.14</td><td>0.76</td></tr>
        <tr><td>test_operator[npu1-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>22.17</td><td>0.55</td><td>0.09</td></tr>
        <tr><td>test_operator[npu1-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 1/1</td><td>28.42</td><td>0.86</td><td>0.14</td></tr>
        <tr><td>test_operator[npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096]</td><td>✅ 1/1</td><td>1179.04</td><td>28.47</td><td>7.11</td></tr>
        <tr><td>test_operator[npu1-RowwiseAdd-rows_4-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 1/1</td><td>52.42</td><td>0.18</td><td>0.04</td></tr>
        <tr><td>test_operator[npu1-RowwiseAdd-rows_4-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 1/1</td><td>33.95</td><td>0.14</td><td>0.03</td></tr>
        <tr><td>test_operator[npu1-RowwiseAdd-wide_row]</td><td>✅ 1/1</td><td>74.22</td><td>17.80</td><td>4.41</td></tr>
        <tr><td>test_operator[npu1-RowwiseAdd-wider_row]</td><td>✅ 1/1</td><td>52.09</td><td>8.02</td><td>1.89</td></tr>
        <tr><td>test_operator[npu1-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>26.25</td><td>0.47</td><td>0.08</td></tr>
        <tr><td>test_operator[npu1-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 1/1</td><td>20.70</td><td>1.19</td><td>0.20</td></tr>
        <tr><td>test_operator[npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096]</td><td>✅ 1/1</td><td>1175.70</td><td>28.55</td><td>7.13</td></tr>
        <tr><td>test_operator[npu1-RowwiseMul-rows_4-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 1/1</td><td>52.22</td><td>0.18</td><td>0.04</td></tr>
        <tr><td>test_operator[npu1-RowwiseMul-rows_4-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 1/1</td><td>29.46</td><td>0.16</td><td>0.03</td></tr>
        <tr><td>test_operator[npu1-RowwiseMul-wide_row]</td><td>✅ 1/1</td><td>77.37</td><td>17.07</td><td>4.24</td></tr>
        <tr><td>test_operator[npu1-RowwiseMul-wider_row]</td><td>✅ 1/1</td><td>44.42</td><td>9.40</td><td>2.21</td></tr>
        <tr><td>test_operator[npu1-Sample-llama]</td><td>✅ 1/1</td><td>335.60</td><td>0.76</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Sample-padded]</td><td>✅ 1/1</td><td>359.15</td><td>0.84</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Sample-small]</td><td>✅ 1/1</td><td>161.55</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Sample-two_cores]</td><td>✅ 1/1</td><td>131.78</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-Sample-uneven]</td><td>✅ 1/1</td><td>189.35</td><td>0.55</td><td>n/a</td></tr>
        <tr><td>test_operator[npu1-SelectiveScan-decode]</td><td>✅ 1/1</td><td>41.97</td><td>0.80</td><td>0.49</td></tr>
        <tr><td>test_operator[npu1-SelectiveScan-odd_rows]</td><td>✅ 1/1</td><td>44.11</td><td>0.40</td><td>0.70</td></tr>
        <tr><td>test_operator[npu1-SelectiveScan-reclaim]</td><td>✅ 1/1</td><td>91110.32</td><td>0.05</td><td>0.92</td></tr>
        <tr><td>test_operator[npu1-SelectiveScan-rows_5-heads_2-head_dim_16-state_size_16-columns_1]</td><td>✅ 1/1</td><td>54.45</td><td>0.09</td><td>0.24</td></tr>
        <tr><td>test_operator[npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2]</td><td>✅ 1/1</td><td>8930.61</td><td>0.09</td><td>2.35</td></tr>
        <tr><td>test_operator[npu1-SelectiveScan-rows_8-heads_4-head_dim_32-state_size_32-groups_2]</td><td>✅ 1/1</td><td>105.81</td><td>0.37</td><td>1.55</td></tr>
        <tr><td>test_operator[npu1-SiLU-size_1024-num_aie_columns_4-tile_size_256]</td><td>✅ 1/1</td><td>26.84</td><td>0.15</td><td>0.04</td></tr>
        <tr><td>test_operator[npu1-SiLU-size_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 1/1</td><td>23.39</td><td>0.35</td><td>0.09</td></tr>
        <tr><td>test_operator[npu1-SiLU-size_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 1/1</td><td>42.45</td><td>0.19</td><td>0.05</td></tr>
        <tr><td>test_operator[npu1-SiLU-size_4096-num_aie_columns_1-tile_size_4096]</td><td>✅ 1/1</td><td>29.02</td><td>0.56</td><td>0.14</td></tr>
        <tr><td>test_operator[npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096]</td><td>✅ 1/1</td><td>2641.57</td><td>12.70</td><td>3.18</td></tr>
        <tr><td>test_operator[npu1-Sigmoid-size_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 1/1</td><td>48.60</td><td>0.08</td><td>0.02</td></tr>
        <tr><td>test_operator[npu1-Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>23.84</td><td>0.34</td><td>0.09</td></tr>
        <tr><td>test_operator[npu1-Sigmoid-size_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 1/1</td><td>51.49</td><td>0.16</td><td>0.04</td></tr>
        <tr><td>test_operator[npu1-Sigmoid-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 1/1</td><td>23.25</td><td>0.70</td><td>0.18</td></tr>
        <tr><td>test_operator[npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 1/1</td><td>2982.43</td><td>11.25</td><td>2.81</td></tr>
        <tr><td>test_operator[npu1-Softmax-f32_soft_cap_banded_addend]</td><td>✅ 1/1</td><td>62.72</td><td>0.33</td><td>0.03</td></tr>
        <tr><td>test_operator[npu1-Softmax-rows_16-cols_4096-block_1024-num_aie_columns_2-num_channels_2]</td><td>✅ 1/1</td><td>125.56</td><td>2.09</td><td>0.52</td></tr>
        <tr><td>test_operator[npu1-Softmax-rows_16-cols_4608-num_aie_columns_2-num_channels_2]</td><td>✅ 1/1</td><td>143.01</td><td>2.06</td><td>0.52</td></tr>
        <tr><td>test_operator[npu1-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2-input_dtype_<class 'numpy.float32'>]</td><td>✅ 1/1</td><td>116.99</td><td>1.68</td><td>0.28</td></tr>
        <tr><td>test_operator[npu1-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2]</td><td>✅ 1/1</td><td>38.15</td><td>3.44</td><td>0.86</td></tr>
        <tr><td>test_operator[npu1-Softmax-rows_32-cols_32768-num_aie_columns_2-num_channels_2]</td><td>✅ 1/1</td><td>3067.09</td><td>1.37</td><td>0.34</td></tr>
        <tr><td>test_operator[npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2]</td><td>✅ 1/1</td><td>1299.48</td><td>6.46</td><td>1.61</td></tr>
        <tr><td>test_operator[npu1-Tanh-size_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 1/1</td><td>45.53</td><td>0.09</td><td>0.02</td></tr>
        <tr><td>test_operator[npu1-Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>31.52</td><td>0.26</td><td>0.06</td></tr>
        <tr><td>test_operator[npu1-Tanh-size_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 1/1</td><td>56.30</td><td>0.15</td><td>0.04</td></tr>
        <tr><td>test_operator[npu1-Tanh-size_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 1/1</td><td>32.59</td><td>0.50</td><td>0.13</td></tr>
        <tr><td>test_operator[npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 1/1</td><td>3204.83</td><td>10.47</td><td>2.62</td></tr>
        <tr><td>test_patch_positions_that_do_not_tile_are_refused[more_patches_than_rows]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_patch_positions_that_do_not_tile_are_refused[not_whole_windows]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_patch_positions_that_do_not_tile_are_refused[rows_not_whole_blocks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_reference_matches_device_convention_across_shapes[test_reference_matches_device_convention_across_shapes]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rows_are_masked_to_the_per_call_length[xclbin-llama]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rows_are_masked_to_the_per_call_length[xclbin-unaligned]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rows_are_masked_to_the_per_call_length[xclbin-vision]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_sample_over_an_odd_vocab_is_refused[test_sample_over_an_odd_vocab_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_sample_with_more_cores_than_a_memtile_joins_is_refused[test_sample_with_more_cores_than_a_memtile_joins_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_accepts_blocks_dividing_rows[rows_5-block_16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_accepts_blocks_dividing_rows[rows_5-block_80]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_accepts_blocks_dividing_rows[rows_8-block_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_accepts_blocks_dividing_rows[rows_8-block_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_a_state_not_whole_slices[state_size_136]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_a_state_not_whole_slices[state_size_24]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_a_state_not_whole_slices[state_size_8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_an_explicit_block_past_core_memory[test_selective_scan_rejects_an_explicit_block_past_core_memory]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_invalid_blocks[columns_1-block_-16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_invalid_blocks[columns_1-block_0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_invalid_blocks[columns_1-block_17]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_invalid_blocks[columns_1-block_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_invalid_blocks[columns_1-block_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_invalid_blocks[columns_1-block_96]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_invalid_blocks[columns_None-block_-16]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_invalid_blocks[columns_None-block_0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_invalid_blocks[columns_None-block_17]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_invalid_blocks[columns_None-block_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_invalid_blocks[columns_None-block_32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_selective_scan_rejects_invalid_blocks[columns_None-block_96]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_softmax_with_no_column_count_that_tiles_is_refused[test_softmax_with_no_column_count_that_tiles_is_refused]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_bound_rows_are_what_moves[n_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_bound_rows_are_what_moves[n_256]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_bound_rows_are_what_moves[n_40]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_default_patch_rows_are_the_rows_the_cores_write[out_width_144-device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_default_patch_rows_are_the_rows_the_cores_write[out_width_144-device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_default_patch_rows_are_the_rows_the_cores_write[out_width_256-device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_default_patch_rows_are_the_rows_the_cores_write[out_width_256-device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_reference_scores_a_long_cache_a_few_rows_at_a_time[test_the_reference_scores_a_long_cache_a_few_rows_at_a_time]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_rows_of_a_bound_are_computed[xclbin]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_units_a_bound_reaches_are_computed[xclbin-qwen2_down]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_units_a_bound_reaches_are_computed[xclbin-qwen2_up]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_units_a_bound_reaches_are_computed[xclbin-resident_b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_units_a_bound_reaches_are_computed[xclbin-streamed_b]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_a_bounded_row_is_rejected[test_transfer_size_not_dividing_a_bounded_row_is_rejected]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_the_per_channel_share_is_rejected[test_transfer_size_not_dividing_the_per_channel_share_is_rejected]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_walks_in_turn_are_their_reference[band_stride_0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_walks_in_turn_are_their_reference[band_stride_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/tests/toolchain</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_a_bounded_operator_lowers[device_npu1-gemm-GEMM--valid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operator_lowers[device_npu1-mha-MHA--kv_valid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operator_lowers[device_npu1-mha-MHA--valid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operator_lowers[device_npu1-relu-ReLU--valid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operator_lowers[device_npu1-rms_norm-RMSNorm--valid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operator_lowers[device_npu1-rope-RoPE--valid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operator_lowers[device_npu1-softmax-Softmax--length]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operator_lowers[device_npu2-gemm-GEMM--valid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operator_lowers[device_npu2-mha-MHA--kv_valid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operator_lowers[device_npu2-mha-MHA--valid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operator_lowers[device_npu2-relu-ReLU--valid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operator_lowers[device_npu2-rms_norm-RMSNorm--valid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operator_lowers[device_npu2-rope-RoPE--valid]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_bounded_operator_lowers[device_npu2-softmax-Softmax--length]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_cached_build_leaves_no_kernel_for_the_next_graph_to_collide_with[test_a_cached_build_leaves_no_kernel_for_the_next_graph_to_collide_with]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_declared_operator_compiles_to_an_xclbin_on_npu1[test_a_declared_operator_compiles_to_an_xclbin_on_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_graph_called_in_a_graph_lowers[device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_graph_called_in_a_graph_lowers[device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_graph_compiles_to_one_xclbin_per_operator_chained[device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_graph_compiles_to_one_xclbin_per_operator_chained[device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_per_call_size_over_one_block_builds_at_each_step[test_a_per_call_size_over_one_block_builds_at_each_step]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_scratch_arena_past_a_bank_links_as_its_banks[test_a_scratch_arena_past_a_bank_links_as_its_banks]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_inline_kernel_lowers[device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_an_inline_kernel_lowers[device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_attention_over_a_128k_cache_lowers[rows_decode]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_attention_over_a_128k_cache_lowers[rows_prompt]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_convolutions_called_in_a_graph_lower[device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_convolutions_called_in_a_graph_lower[device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_decode_graph_builds_a_full_elf_with_its_values_in_the_table[test_decode_graph_builds_a_full_elf_with_its_values_in_the_table]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_decode_graph_operators_lower_with_their_values[test_decode_graph_operators_lower_with_their_values]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_gemm_links_its_configuration_xclbin_and_its_own_instructions[test_flm_gemm_links_its_configuration_xclbin_and_its_own_instructions]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_gemm_lowers_and_so_does_its_configuration_module[base]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_gemm_lowers_and_so_does_its_configuration_module[n10240]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_flm_gemm_lowers_and_so_does_its_configuration_module[tn128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_image_patches_called_in_a_graph_lower[device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_image_patches_called_in_a_graph_lower[device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_instructions_compile_alone_against_an_external_image[test_instructions_compile_alone_against_an_external_image]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_its_reference_is_the_contracts[device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_its_reference_is_the_contracts[device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_builds_xclbins_at_its_size_on_npu1[chunk_False-pipelines_2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_builds_xclbins_at_its_size_on_npu1[chunk_True-pipelines_4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_no_scratch_buffer_crosses_a_bank[test_no_scratch_buffer_crosses_a_bank]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_npu1_compiles_each_step_unasked[test_npu1_compiles_each_step_unasked]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Copy-by_head_two_channels]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Copy-contiguous]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Copy-float32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Copy-slot5]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Emit-one_carried]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-GEMM-M_1792-K_896-N_1152-num_aie_columns_4-tile_m_64-tile_k_32-tile_n_48-b_col_maj_False-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-GEMM-M_192-K_384-N_64-num_aie_columns_4-tile_m_48-tile_k_96-tile_n_16-b_col_maj_True-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-GEMM-M_2048-K_2048-N_2048-num_aie_columns_4-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-GEMM-M_32-K_1152-N_2048-num_aie_columns_4-tile_m_16-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-GEMM-M_896-K_1792-N_640-num_aie_columns_4-tile_m_32-tile_k_64-tile_n_80-b_col_maj_False-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-GEMM-f32_out]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-GEMV-M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Limbs-rows_64-line_160-num_aie_columns_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-MHA-num_heads_24-num_KV_heads_8-d_128-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-MHA-num_heads_32-num_KV_heads_8-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_1-kv_len_2048-window_511-num_pipelines_1-heads_interleaved_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_512-kv_len_2048-window_511-num_pipelines_4-heads_interleaved_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-MHA-num_heads_4-num_KV_heads_1-seq_len_2000-d_512-causal_False-num_pipelines_4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-MHA-num_heads_40-num_KV_heads_8-d_64-seq_len_1-kv_len_2048-num_pipelines_2-heads_interleaved_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Magnitude-rows_64-width_640-num_aie_columns_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-PatchPositions-rows_2560-out_height_672-out_width_912]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Resample-height_3024-width_4032-out_height_672-out_width_912]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-ResampleTaps-in_size_4032-out_size_912]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-RowwiseAdd-wide_row]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-RowwiseMul-wide_row]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Sample-padded]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Sample-small]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Sample-uneven]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-SelectiveScan-rows_5-heads_2-head_dim_16-state_size_16-columns_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-SiLU-size_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Softmax-rows_16-cols_4096-block_1024-num_aie_columns_2-num_channels_2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2-input_dtype_<class 'numpy.float32'>]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu1-Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-AXPY-size_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Clamp-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048-low_-0.75-high_1.25]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Copy-by_head_two_channels]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Copy-contiguous]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Copy-float32]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Copy-slot5]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-DepthwiseConv1d-rows_64-channels_64-num_aie_columns_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-ElementwiseAdd-size_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-ElementwiseMul-size_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Emit-one_carried]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-GELU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-GEMM-M_1792-K_896-N_1152-num_aie_columns_8-tile_m_64-tile_k_32-tile_n_48-b_col_maj_False-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-GEMM-M_192-K_384-N_64-num_aie_columns_4-tile_m_48-tile_k_96-tile_n_16-b_col_maj_True-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_1-tile_m_64-tile_k_64-tile_n_64-b_col_maj_False-c_col_maj_False-precision_highest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-GEMM-M_2048-K_2048-N_2048-num_aie_columns_8-tile_m_64-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-GEMM-M_32-K_1152-N_2048-num_aie_columns_4-tile_m_16-tile_k_64-tile_n_64-b_col_maj_True-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-GEMM-M_896-K_1792-N_640-num_aie_columns_8-tile_m_32-tile_k_64-tile_n_80-b_col_maj_False-c_col_maj_True-precision_highest]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-GEMM-f32_out]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-GEMV-M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-GEMV-M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-LayerNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Limbs-rows_64-line_160-num_aie_columns_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Log-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-MHA-num_heads_24-num_KV_heads_8-d_128-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-MHA-num_heads_32-num_KV_heads_8-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_1-kv_len_2048-window_511-num_pipelines_1-heads_interleaved_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-MHA-num_heads_4-num_KV_heads_1-d_256-seq_len_512-kv_len_2048-window_511-num_pipelines_8-heads_interleaved_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-MHA-num_heads_4-num_KV_heads_1-seq_len_2000-d_512-causal_False-num_pipelines_8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-MHA-num_heads_40-num_KV_heads_8-d_64-seq_len_1-kv_len_2048-num_pipelines_4-heads_interleaved_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_2048-kv_len_8192-num_pipelines_8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Magnitude-rows_64-width_640-num_aie_columns_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-PatchPositions-rows_2560-out_height_672-out_width_912]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-RMSNorm-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-ReLU-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Resample-height_3024-width_4032-out_height_672-out_width_912]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-ResampleTaps-in_size_4032-out_size_912]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-RoPE-rows_32-cols_512-num_aie_columns_1-angle_rows_8]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-RowwiseAdd-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-RowwiseAdd-wide_row]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-RowwiseMul-rows_1-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-RowwiseMul-wide_row]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Sample-padded]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Sample-small]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Sample-uneven]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-SelectiveScan-rows_5-heads_2-head_dim_16-state_size_16-columns_1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-SiLU-size_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Sigmoid-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Softmax-rows_16-cols_4096-block_1024-num_aie_columns_2-num_channels_2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2-input_dtype_<class 'numpy.float32'>]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Softmax-rows_32-cols_1024-num_aie_columns_2-num_channels_2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-Tanh-size_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-flm.DequantBFP-K_512-N_128]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_operator_lowers_to_instructions[npu2-flm.LMHead-dim_1536-vocab_4096-softcap_30.0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prefill_graph_builds_a_full_elf_at_llama_size_for_one_layer[test_prefill_graph_builds_a_full_elf_at_llama_size_for_one_layer]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prefill_graph_builds_a_full_elf_with_its_value_in_the_table[test_prefill_graph_builds_a_full_elf_with_its_value_in_the_table]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prefill_graph_operators_lower_with_their_value[test_prefill_graph_operators_lower_with_their_value]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prefill_steps_lower_at_llama_size[down_projection_checkpoint_layout]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prefill_steps_lower_at_llama_size[kv_into_cache]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prefill_steps_lower_at_llama_size[mha_in_the_projections_layout]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_shipped_builds_its_instructions_for_the_external_image[test_shipped_builds_its_instructions_for_the_external_image]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_shipped_external_sequence_lowers[test_shipped_external_sequence_lowers]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_shipped_fetches_its_image[test_shipped_fetches_its_image]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_swiglu_graph_compiles_to_a_full_elf[test_swiglu_graph_compiles_to_a_full_elf]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_swiglu_graphs_operators_lower[test_swiglu_graphs_operators_lower]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_array_is_the_same_at_two_extents[device_npu1-elementwise_add-ElementwiseAdd--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_array_is_the_same_at_two_extents[device_npu1-gemm-GEMM--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_array_is_the_same_at_two_extents[device_npu1-gemv-GEMV--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_array_is_the_same_at_two_extents[device_npu1-rope-RoPE--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_array_is_the_same_at_two_extents[device_npu1-softmax-Softmax--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_array_is_the_same_at_two_extents[device_npu2-elementwise_add-ElementwiseAdd--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_array_is_the_same_at_two_extents[device_npu2-gemm-GEMM--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_array_is_the_same_at_two_extents[device_npu2-gemv-GEMV--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_array_is_the_same_at_two_extents[device_npu2-rope-RoPE--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_array_is_the_same_at_two_extents[device_npu2-softmax-Softmax--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_extents_share_one_device[elementwise_add-ElementwiseAdd--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_extents_share_one_device[gemm-GEMM--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_extents_share_one_device[gemv-GEMV--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_extents_share_one_device[rope-RoPE--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_the_extents_share_one_device[softmax-Softmax--]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_values_become_dispatch_time_kernels_at_each_step[device_npu1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_values_become_dispatch_time_kernels_at_each_step[device_npu2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

