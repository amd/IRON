
# IRON

Tested on `2026_10_04_18_37_11` at commit `79c04e6`.

<details>
<summary>iron/operators/axpy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003]</td><td>✅ 5/5</td><td>155.12</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>155.90</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_1.003]</td><td>✅ 5/5</td><td>172.82</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>166.34</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_1.003]</td><td>✅ 5/5</td><td>195.06</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>217.60</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_1.003]</td><td>✅ 5/5</td><td>192.96</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0]</td><td>✅ 5/5</td><td>220.08</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0]</td><td>✅ 5/5</td><td>850.28</td><td>59.20</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/dequant</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>177.36</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>149.18</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>142.52</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>137.96</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>139.80</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>196.50</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>181.74</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32]</td><td>✅ 5/5</td><td>201.06</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>484.22</td><td>44.83</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>145.14</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>172.90</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>172.78</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256]</td><td>✅ 5/5</td><td>168.00</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8388608-num_aie_columns_8-tile_size_4096]</td><td>✅ 5/5</td><td>981.48</td><td>53.79</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>167.48</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>183.54</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>175.94</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256]</td><td>✅ 5/5</td><td>206.32</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8388608-num_aie_columns_8-tile_size_4096]</td><td>✅ 5/5</td><td>877.66</td><td>57.39</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/flm/dequant</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gate_up_interleaved_blob[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gate_up_interleaved_blob[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gate_up_interleaved_blob[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gate_up_interleaved_blob[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gate_up_interleaved_blob[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_large_k_shapes[K_4096-N_1536]</td><td>✅ 5/5</td><td>663.68</td><td>16.60</td><td>n/a</td></tr>
        <tr><td>test_large_k_shapes[K_6144-N_1536]</td><td>✅ 5/5</td><td>963.78</td><td>17.89</td><td>n/a</td></tr>
        <tr><td>test_matches_reference[K_1024-N_128]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_matches_reference[K_1024-N_512]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_matches_reference[K_1536-N_640]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_matches_reference[K_2048-N_256]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_output_feeds_gemm_unchanged[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_output_feeds_gemm_unchanged[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_output_feeds_gemm_unchanged[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_output_feeds_gemm_unchanged[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_output_feeds_gemm_unchanged[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[K_512-N_128-exc_<class 'NotImplementedError'>-match_tile_n]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>353.60</td><td>3.98</td><td>775.82</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even]</td><td>✅ 5/5</td><td>307.12</td><td>4.72</td><td>921.41</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>296.76</td><td>4.97</td><td>970.10</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor]</td><td>✅ 5/5</td><td>289.10</td><td>5.21</td><td>1015.85</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>336.50</td><td>4.13</td><td>805.28</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>313.00</td><td>1.30</td><td>108.56</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>294.62</td><td>6.94</td><td>1444.49</td></tr>
        <tr><td>test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>372.28</td><td>15.39</td><td>6002.26</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn128-ma64-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn16-ma64-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn32-ma64-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn64-ma32-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_clamp_bound[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_clamp_bound[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_clamp_bound[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_clamp_bound[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_clamp_bound[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_xclbin_serves_every_shape[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
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
        <tr><td>test_matches_reference[gemma4_e2b-global-5]</td><td>✅ 5/5</td><td>823.16</td><td>35.17</td><td>106.29</td></tr>
        <tr><td>test_matches_reference[gemma4_e2b-global-700]</td><td>✅ 5/5</td><td>876.62</td><td>34.78</td><td>113.24</td></tr>
        <tr><td>test_matches_reference[gemma4_e2b-global_skip-37]</td><td>✅ 5/5</td><td>1234.32</td><td>38.47</td><td>119.05</td></tr>
        <tr><td>test_matches_reference[gemma4_e2b-global_skip-700]</td><td>✅ 5/5</td><td>1283.14</td><td>37.56</td><td>121.54</td></tr>
        <tr><td>test_matches_reference[gemma4_e2b-swa-1023]</td><td>✅ 5/5</td><td>784.50</td><td>32.22</td><td>99.67</td></tr>
        <tr><td>test_matches_reference[gemma4_e2b-swa-37]</td><td>✅ 5/5</td><td>729.88</td><td>33.73</td><td>101.05</td></tr>
        <tr><td>test_matches_reference[gemma4_e2b-swa-511]</td><td>✅ 5/5</td><td>737.44</td><td>34.00</td><td>105.15</td></tr>
        <tr><td>test_matches_reference[gemma4_e2b-swa-512]</td><td>✅ 5/5</td><td>744.26</td><td>33.61</td><td>103.96</td></tr>
        <tr><td>test_matches_reference[gemma4_e2b-swa-700]</td><td>✅ 5/5</td><td>745.54</td><td>33.54</td><td>103.75</td></tr>
        <tr><td>test_matches_reference[gemma4_e2b-swa_skip-1023]</td><td>✅ 5/5</td><td>1041.52</td><td>40.61</td><td>127.39</td></tr>
        <tr><td>test_matches_reference[gemma4_e2b-swa_skip-37]</td><td>✅ 5/5</td><td>1188.86</td><td>36.68</td><td>112.98</td></tr>
        <tr><td>test_matches_reference[gemma4_e2b-swa_skip-511]</td><td>✅ 5/5</td><td>1011.56</td><td>41.73</td><td>130.88</td></tr>
        <tr><td>test_matches_reference[gemma4_e2b-swa_skip-512]</td><td>✅ 5/5</td><td>1132.44</td><td>38.42</td><td>120.52</td></tr>
        <tr><td>test_matches_reference[gemma4_e2b-swa_skip-700]</td><td>✅ 5/5</td><td>1088.12</td><td>39.36</td><td>123.47</td></tr>
        <tr><td>test_rejects_unknown_configurations[geometry]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unknown_configurations[layer_type]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e2b-layer_type_global]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e2b-layer_type_global_skip]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa_skip]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e4b-layer_type_global]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e4b-layer_type_global_skip]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa_skip]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/flm/lm_head</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gemma4_softcap[dim_1536]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemma4_softcap[dim_2560]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_projection_matches_reference[dim_1536]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_projection_matches_reference[dim_2560]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[dim_1000-vocab_4096-softcap_30.0-match_multiple of]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[dim_1536-vocab_1000-softcap_30.0-match_multiple of]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[dim_1536-vocab_4096-softcap_0.0-match_finite and positive]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[dim_1536-vocab_4096-softcap_inf-match_finite and positive]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_softcap_bounds_the_logits[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_softcap_bounds_the_logits[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_softcap_bounds_the_logits[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_softcap_bounds_the_logits[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_softcap_bounds_the_logits[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/flm/prefill_attn</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_1]</td><td>✅ 5/5</td><td>369.68</td><td>6.38</td><td>365.90</td></tr>
        <tr><td>test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_2]</td><td>✅ 5/5</td><td>374.98</td><td>6.99</td><td>360.79</td></tr>
        <tr><td>test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_1]</td><td>✅ 5/5</td><td>766.94</td><td>6.15</td><td>702.80</td></tr>
        <tr><td>test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_2]</td><td>✅ 5/5</td><td>770.08</td><td>6.81</td><td>699.90</td></tr>
        <tr><td>test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1]</td><td>✅ 5/5</td><td>1873.94</td><td>5.05</td><td>1150.39</td></tr>
        <tr><td>test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2]</td><td>✅ 5/5</td><td>2066.84</td><td>5.29</td><td>1086.28</td></tr>
        <tr><td>test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_1]</td><td>✅ 5/5</td><td>1013.28</td><td>4.92</td><td>1061.83</td></tr>
        <tr><td>test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_2]</td><td>✅ 5/5</td><td>1003.34</td><td>5.75</td><td>1072.27</td></tr>
        <tr><td>test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_1]</td><td>✅ 5/5</td><td>4510.56</td><td>3.25</td><td>1786.78</td></tr>
        <tr><td>test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_2]</td><td>✅ 5/5</td><td>4501.54</td><td>3.73</td><td>1790.37</td></tr>
        <tr><td>test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_1]</td><td>✅ 5/5</td><td>1912.70</td><td>4.93</td><td>1685.25</td></tr>
        <tr><td>test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_2]</td><td>✅ 5/5</td><td>1901.24</td><td>5.52</td><td>1696.03</td></tr>
        <tr><td>test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_1]</td><td>✅ 5/5</td><td>216.74</td><td>5.44</td><td>312.04</td></tr>
        <tr><td>test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_2]</td><td>✅ 5/5</td><td>216.32</td><td>6.06</td><td>312.67</td></tr>
        <tr><td>test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1]</td><td>✅ 5/5</td><td>801.34</td><td>5.89</td><td>1342.59</td></tr>
        <tr><td>test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2]</td><td>✅ 5/5</td><td>807.38</td><td>6.49</td><td>1332.54</td></tr>
        <tr><td>test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_1]</td><td>✅ 5/5</td><td>2671.96</td><td>3.89</td><td>1675.56</td></tr>
        <tr><td>test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_2]</td><td>✅ 5/5</td><td>2361.52</td><td>4.88</td><td>1818.74</td></tr>
        <tr><td>test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1]</td><td>✅ 5/5</td><td>1255.12</td><td>4.18</td><td>1710.98</td></tr>
        <tr><td>test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_2]</td><td>✅ 5/5</td><td>1252.86</td><td>5.02</td><td>1714.13</td></tr>
        <tr><td>test_one_callable_serves_every_range[kind_attn]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_one_callable_serves_every_range[kind_swa]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'max_context': 1000, 'num_kv_heads': 1}-match_multiple of 128]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 0}-match_must be positive]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 3}-match_multiple of]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 8}-match_query heads]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'max_context': 1000, 'num_kv_heads': 1}-match_multiple of 128]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 1, 'window': 500}-match_multiple of 128]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 3}-match_multiple of]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 4}-match_query heads]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/gelu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>174.46</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>181.98</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>208.48</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>209.38</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>161.64</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>173.86</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>199.66</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>227.50</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>687.78</td><td>48.83</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/gemm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-partition_N_1]</td><td>✅ 5/5</td><td>2268.62</td><td>4.23</td><td>1664.58</td></tr>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-partition_N_1]</td><td>✅ 5/5</td><td>238.90</td><td>0.94</td><td>40.30</td></tr>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-partition_N_1]</td><td>✅ 5/5</td><td>259.04</td><td>0.90</td><td>38.43</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>46982.78</td><td>0.54</td><td>365.67</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>27692.88</td><td>0.91</td><td>620.40</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>7674.80</td><td>3.28</td><td>2239.57</td></tr>
        <tr><td>test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-partition_N_1]</td><td>✅ 5/5</td><td>2210.16</td><td>3.71</td><td>973.97</td></tr>
        <tr><td>test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-partition_N_4]</td><td>✅ 5/5</td><td>3278.60</td><td>0.41</td><td>22.03</td></tr>
        <tr><td>test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-partition_N_1]</td><td>✅ 5/5</td><td>1438.56</td><td>4.80</td><td>1482.37</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/gemv</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 5/5</td><td>178.12</td><td>0.19</td><td>0.19</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>✅ 5/5</td><td>2634.42</td><td>12.76</td><td>12.75</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024]</td><td>✅ 5/5</td><td>1394.28</td><td>24.12</td><td>24.11</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512]</td><td>✅ 5/5</td><td>830.98</td><td>40.46</td><td>40.43</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256]</td><td>✅ 5/5</td><td>792.80</td><td>42.36</td><td>42.34</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>2810.00</td><td>12.09</td><td>12.08</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>1473.78</td><td>23.00</td><td>22.99</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>836.68</td><td>40.16</td><td>40.14</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>843.12</td><td>40.30</td><td>40.27</td></tr>
        <tr><td>test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2]</td><td>✅ 5/5</td><td>462.38</td><td>9.11</td><td>9.10</td></tr>
        <tr><td>test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2]</td><td>✅ 5/5</td><td>309.58</td><td>0.86</td><td>0.85</td></tr>
        <tr><td>test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4]</td><td>✅ 5/5</td><td>237.16</td><td>1.13</td><td>1.11</td></tr>
        <tr><td>test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100]</td><td>✅ 5/5</td><td>446.58</td><td>14.89</td><td>14.72</td></tr>
        <tr><td>test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192]</td><td>✅ 5/5</td><td>1100.98</td><td>10.66</td><td>10.47</td></tr>
        <tr><td>test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32]</td><td>✅ 5/5</td><td>205.14</td><td>10.69</td><td>10.51</td></tr>
        <tr><td>test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8]</td><td>✅ 5/5</td><td>290.38</td><td>5.51</td><td>5.42</td></tr>
        <tr><td>test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 5/5</td><td>191.92</td><td>0.18</td><td>0.18</td></tr>
        <tr><td>test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>✅ 5/5</td><td>2641.52</td><td>12.73</td><td>12.72</td></tr>
        <tr><td>test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>2599.58</td><td>12.92</td><td>12.92</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/layer_norm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>154.16</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>161.06</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>168.66</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>173.02</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>166.74</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>172.50</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>218.32</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>213.54</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>706.96</td><td>47.76</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>161.10</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1]</td><td>✅ 5/5</td><td>174.74</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25]</td><td>✅ 5/5</td><td>178.34</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>175.96</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>177.80</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>163.80</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>144.14</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>176.56</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>181.76</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01]</td><td>✅ 5/5</td><td>206.62</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>676.88</td><td>49.87</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/mem_copy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>186.82</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128]</td><td>✅ 5/5</td><td>233.44</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>166.18</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>148.30</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>153.44</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>157.12</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>187.66</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>175.06</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8388608-num_cores_16-num_channels_2-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>670.02</td><td>50.28</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/mha</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0]</td><td>✅ 5/5</td><td>17077.68</td><td>0.51</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/relu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>158.72</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>156.84</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>191.06</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>173.98</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>153.32</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>173.20</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>187.84</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>196.18</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>677.94</td><td>49.78</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/repeat</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None]</td><td>✅ 5/5</td><td>162.98</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_512-repeat_4-transfer_size_64]</td><td>✅ 5/5</td><td>196.54</td><td>0.21</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_64-repeat_4-transfer_size_None]</td><td>✅ 5/5</td><td>199.80</td><td>0.03</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/rms_norm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>170.02</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>164.54</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>171.50</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>162.16</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>198.92</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>165.52</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>156.28</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>199.62</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>171.58</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>190.00</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>179.84</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>203.46</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>180.88</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>221.96</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False]</td><td>✅ 5/5</td><td>208.08</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>736.40</td><td>45.72</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>683.30</td><td>49.35</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/rope</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>189.26</td><td>0.54</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>177.94</td><td>0.56</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>184.30</td><td>0.55</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>202.42</td><td>0.50</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>175.48</td><td>0.43</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>160.58</td><td>0.46</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>164.26</td><td>0.45</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>186.58</td><td>0.40</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_8-method_type_0]</td><td>✅ 5/5</td><td>323.96</td><td>26.27</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/sigmoid</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>189.86</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>171.38</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>167.08</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>161.76</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>168.18</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>180.18</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>192.26</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>191.38</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>674.80</td><td>50.00</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/silu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>162.78</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>201.74</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>177.78</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>206.22</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>682.54</td><td>49.48</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/softmax</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_softmax[input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>518.82</td><td>16.20</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>175.14</td><td>0.77</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>168.84</td><td>0.78</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>171.02</td><td>0.78</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/strided_copy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_strided_copy[bench_flat_4mi]</td><td>✅ 5/5</td><td>476.30</td><td>35.30</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[chunked_transfer]</td><td>✅ 5/5</td><td>169.56</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[contiguous]</td><td>✅ 5/5</td><td>176.70</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[four_channels]</td><td>✅ 5/5</td><td>173.12</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot0]</td><td>✅ 5/5</td><td>163.40</td><td>0.84</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5]</td><td>✅ 5/5</td><td>172.74</td><td>0.79</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5_four_channels]</td><td>✅ 5/5</td><td>161.64</td><td>0.83</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5_two_channels]</td><td>✅ 5/5</td><td>165.92</td><td>0.82</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot_last]</td><td>✅ 5/5</td><td>156.98</td><td>0.85</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[two_channels]</td><td>✅ 5/5</td><td>199.64</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[two_channels_chunked]</td><td>✅ 5/5</td><td>155.58</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_strided_copy_cache_offset_parameter[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_strided_copy_cache_offset_parameter[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_strided_copy_cache_offset_parameter[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_strided_copy_cache_offset_parameter[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_strided_copy_cache_offset_parameter[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_swiglu_decode[embedding_dim_1024-hidden_dim_3584]</td><td>✅ 5/5</td><td>1012.42</td><td>0.00</td><td>n/a</td></tr>
        <tr><td>test_swiglu_decode[embedding_dim_2048-hidden_dim_2048]</td><td>✅ 5/5</td><td>1043.82</td><td>0.01</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False]</td><td>✅ 5/5</td><td>2147.32</td><td>0.98</td><td>n/a</td></tr>
        <tr><td>test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True]</td><td>✅ 5/5</td><td>2330.91</td><td>0.90</td><td>n/a</td></tr>
        <tr><td>test_weight_layout_reaches_both_gemms[b_col_maj_False]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_weight_layout_reaches_both_gemms[b_col_maj_True]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/tanh</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>158.80</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>165.66</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>166.20</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>208.20</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>209.70</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>193.56</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>221.72</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>234.28</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>777.98</td><td>45.00</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/operators/transpose</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_a_dimension_that_floors_to_zero_is_refused_by_name[M_2048-N_128-aie_columns_8-channels_1-m_256-n_32-bad_num_aie_columns]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_dimension_that_floors_to_zero_is_refused_by_name[M_256-N_2048-aie_columns_1-channels_2-m_256-n_32-bad_num_channels]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tiling_that_fits_is_still_accepted[aie_columns_1]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tiling_that_fits_is_still_accepted[aie_columns_2]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_a_tiling_that_fits_is_still_accepted[aie_columns_4]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>180.44</td><td>2.92</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2]</td><td>✅ 5/5</td><td>213.22</td><td>4.94</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>205.48</td><td>2.78</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>994.68</td><td>16.96</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

