
# IRON

Tested on `2026_10_03_08_53_51` at commit `416c53d`.

<details>
<summary>iron/operators/axpy</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_1.003]</td><td>✅ 5/5</td><td>854.28</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>543.82</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>682.84</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_1.003]</td><td>✅ 5/5</td><td>395.76</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0]</td><td>✅ 5/5</td><td>430.06</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>455.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_1.003]</td><td>✅ 5/5</td><td>548.52</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0]</td><td>✅ 5/5</td><td>515.08</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0]</td><td>✅ 5/5</td><td>386.20</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003]</td><td>✅ 5/5</td><td>327.18</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>637.84</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>288.44</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_1.003]</td><td>✅ 5/5</td><td>426.42</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>371.24</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>312.84</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_1.003]</td><td>✅ 5/5</td><td>425.14</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0]</td><td>✅ 5/5</td><td>473.68</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0]</td><td>✅ 5/5</td><td>393.24</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_1.003]</td><td>✅ 5/5</td><td>353.90</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0]</td><td>✅ 5/5</td><td>395.38</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0]</td><td>✅ 5/5</td><td>351.60</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_1.003]</td><td>✅ 5/5</td><td>367.86</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>725.88</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>342.62</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_1.003]</td><td>✅ 5/5</td><td>406.74</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0]</td><td>✅ 5/5</td><td>468.80</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0]</td><td>✅ 5/5</td><td>491.84</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_1.003]</td><td>✅ 5/5</td><td>278.32</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0]</td><td>✅ 5/5</td><td>291.66</td><td>0.17</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0]</td><td>✅ 5/5</td><td>285.14</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_1.003]</td><td>✅ 5/5</td><td>463.78</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0]</td><td>✅ 5/5</td><td>280.28</td><td>0.18</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0]</td><td>✅ 5/5</td><td>391.58</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_1.003]</td><td>✅ 5/5</td><td>407.26</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0]</td><td>✅ 5/5</td><td>488.34</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0]</td><td>✅ 5/5</td><td>1092.84</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_axpy[input_length_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0]</td><td>✅ 5/5</td><td>3949.40</td><td>16.39</td><td>n/a</td></tr>
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
        <tr><td>test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>401.08</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>381.48</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>454.72</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>349.30</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>596.68</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32]</td><td>✅ 5/5</td><td>677.94</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>361.12</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>450.14</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>419.48</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>711.64</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>486.24</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32]</td><td>✅ 5/5</td><td>593.44</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>716.90</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>442.80</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>409.20</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>437.12</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>463.20</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32]</td><td>✅ 5/5</td><td>444.26</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32]</td><td>✅ 5/5</td><td>346.44</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>668.70</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>380.96</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>404.34</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32]</td><td>✅ 5/5</td><td>514.66</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32]</td><td>✅ 5/5</td><td>923.38</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_dequant[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-group_size_32]</td><td>✅ 5/5</td><td>1410.18</td><td>16.45</td><td>n/a</td></tr>
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
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024]</td><td>✅ 5/5</td><td>330.34</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512]</td><td>✅ 5/5</td><td>329.34</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256]</td><td>✅ 5/5</td><td>446.80</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>495.30</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>455.16</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>457.30</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096]</td><td>✅ 5/5</td><td>391.40</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048]</td><td>✅ 5/5</td><td>440.26</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024]</td><td>✅ 5/5</td><td>473.56</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192]</td><td>✅ 5/5</td><td>398.90</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096]</td><td>✅ 5/5</td><td>428.58</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048]</td><td>✅ 5/5</td><td>510.20</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_elementwise_add[input_length_8388608-num_aie_columns_4-tile_size_4096]</td><td>✅ 5/5</td><td>5310.26</td><td>10.03</td><td>n/a</td></tr>
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
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024]</td><td>✅ 5/5</td><td>364.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512]</td><td>✅ 5/5</td><td>698.34</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256]</td><td>✅ 5/5</td><td>535.94</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048]</td><td>✅ 5/5</td><td>337.00</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024]</td><td>✅ 5/5</td><td>468.26</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512]</td><td>✅ 5/5</td><td>550.78</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096]</td><td>✅ 5/5</td><td>481.46</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048]</td><td>✅ 5/5</td><td>402.64</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024]</td><td>✅ 5/5</td><td>729.44</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096]</td><td>✅ 5/5</td><td>553.94</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048]</td><td>✅ 5/5</td><td>469.76</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_elementwise_mul[input_length_8388608-num_aie_columns_4-tile_size_4096]</td><td>✅ 5/5</td><td>5390.44</td><td>9.97</td><td>n/a</td></tr>
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
        <tr><td>test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
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
        <tr><td>test_gemm[M_1024-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>4493.20</td><td>2.39</td><td>979.32</td></tr>
        <tr><td>test_gemm[M_1024-K_2560-N_2560-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>9234.14</td><td>2.56</td><td>1454.01</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>6388.62</td><td>2.64</td><td>1350.57</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>642.02</td><td>0.72</td><td>52.71</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>671.16</td><td>1.00</td><td>102.03</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>766.54</td><td>1.03</td><td>114.54</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>823.82</td><td>1.32</td><td>168.72</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even]</td><td>✅ 5/5</td><td>797.36</td><td>1.46</td><td>187.20</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor]</td><td>✅ 5/5</td><td>871.68</td><td>1.27</td><td>162.24</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_512-epilogue_sigmoid-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>798.24</td><td>1.32</td><td>169.46</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>952.56</td><td>1.26</td><td>160.77</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_floor]</td><td>✅ 5/5</td><td>875.82</td><td>1.30</td><td>165.81</td></tr>
        <tr><td>test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>748.06</td><td>0.49</td><td>22.98</td></tr>
        <tr><td>test_gemm[M_512-K_1024-N_1024-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even]</td><td>✅ 5/5</td><td>1970.70</td><td>2.21</td><td>565.94</td></tr>
        <tr><td>test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>1087.98</td><td>2.47</td><td>506.59</td></tr>
        <tr><td>test_gemm[M_512-K_1536-N_1536-epilogue_silu-clamp_None-rounding_conv_even]</td><td>✅ 5/5</td><td>2810.08</td><td>2.89</td><td>888.82</td></tr>
        <tr><td>test_gemm_gelu_bf16_steps_matches_overlay[M_256-K_512-N_1024]</td><td>❌ 0/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_gelu_bf16_steps_matches_overlay[M_512-K_1536-N_256]</td><td>❌ 0/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_gelu_bf16_steps_matches_overlay[M_512-K_1536-N_6144]</td><td>❌ 0/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_split_leg_bounds_runs[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn128-ma16]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn128-ma32-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn128-ma64]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn16-ma16]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn16-ma32]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn16-ma64-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn32-ma16]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn32-ma32]</td><td>❌ 0/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn32-ma64-default]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemm_tile_options[tn64-ma16]</td><td>✅ 5/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
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
<summary>iron/operators/gelu</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>Latency (mean)</td><td>Bandwidth (mean)</td><td>Throughput (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>429.78</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>599.96</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>370.30</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>498.16</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>384.84</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>481.52</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>454.36</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>415.28</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>405.30</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>454.86</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>363.58</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>549.78</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>364.20</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>358.18</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>299.22</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>381.84</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>417.24</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>495.92</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]</td><td>✅ 5/5</td><td>610.00</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>345.74</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>520.18</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>560.78</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>449.32</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>475.50</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_gelu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>3953.50</td><td>8.64</td><td>n/a</td></tr>
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
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-partition_N_1]</td><td>✅ 5/5</td><td>618.86</td><td>0.36</td><td>15.53</td></tr>
        <tr><td>test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-partition_N_1]</td><td>✅ 5/5</td><td>513.60</td><td>0.46</td><td>19.50</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>82430.38</td><td>0.31</td><td>208.54</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>18691.00</td><td>1.35</td><td>919.19</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>91400.42</td><td>0.83</td><td>751.94</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>91475.30</td><td>0.83</td><td>751.50</td></tr>
        <tr><td>test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>74229.96</td><td>1.02</td><td>927.04</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>2440.08</td><td>4.02</td><td>242.12</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>3161.92</td><td>3.10</td><td>186.54</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>3355.08</td><td>2.78</td><td>167.59</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>6818.90</td><td>5.29</td><td>325.98</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>7228.42</td><td>4.85</td><td>299.03</td></tr>
        <tr><td>test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>5253.48</td><td>6.84</td><td>421.56</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>97211.98</td><td>0.78</td><td>707.02</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>98173.80</td><td>0.77</td><td>700.72</td></tr>
        <tr><td>test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1]</td><td>✅ 5/5</td><td>74660.08</td><td>1.01</td><td>920.44</td></tr>
        <tr><td>test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-partition_N_1]</td><td>✅ 5/5</td><td>4218.84</td><td>2.06</td><td>540.07</td></tr>
        <tr><td>test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-partition_N_4]</td><td>✅ 5/5</td><td>6262.10</td><td>0.20</td><td>10.82</td></tr>
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
        <tr><td>test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>✅ 5/5</td><td>461.48</td><td>0.09</td><td>0.09</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>✅ 5/5</td><td>9176.44</td><td>3.66</td><td>3.66</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024]</td><td>✅ 5/5</td><td>5339.20</td><td>6.32</td><td>6.32</td></tr>
        <tr><td>test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512]</td><td>✅ 5/5</td><td>4446.40</td><td>7.72</td><td>7.72</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>9181.16</td><td>3.66</td><td>3.66</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>5187.00</td><td>6.51</td><td>6.51</td></tr>
        <tr><td>test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024]</td><td>✅ 5/5</td><td>4265.22</td><td>8.17</td><td>8.16</td></tr>
        <tr><td>test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2]</td><td>✅ 5/5</td><td>2543.66</td><td>1.91</td><td>1.90</td></tr>
        <tr><td>test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2]</td><td>✅ 5/5</td><td>1468.50</td><td>0.31</td><td>0.30</td></tr>
        <tr><td>test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4]</td><td>✅ 5/5</td><td>888.58</td><td>0.41</td><td>0.41</td></tr>
        <tr><td>test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8]</td><td>✅ 5/5</td><td>1526.62</td><td>1.54</td><td>1.51</td></tr>
        <tr><td>test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]</td><td>❌ 0/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]</td><td>❌ 0/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]</td><td>❌ 0/5</td><td>n/a</td><td>n/a</td><td>n/a</td></tr>
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
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>397.90</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>375.08</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>334.46</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>299.32</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>361.96</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>526.18</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>373.56</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>371.04</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>353.46</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>427.84</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>743.08</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>404.42</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>237.82</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>691.00</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>306.90</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>577.12</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>716.56</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>485.26</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]</td><td>✅ 5/5</td><td>442.34</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>450.72</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>379.82</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>354.10</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>391.98</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>464.10</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_layer_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>3403.10</td><td>10.47</td><td>n/a</td></tr>
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
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>376.02</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>362.50</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>395.58</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>477.96</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>325.12</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01]</td><td>✅ 5/5</td><td>388.54</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>325.04</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1]</td><td>✅ 5/5</td><td>319.16</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25]</td><td>✅ 5/5</td><td>393.72</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>290.98</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>408.88</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>557.90</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>298.54</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01]</td><td>✅ 5/5</td><td>554.42</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>378.90</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>435.94</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>351.96</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>619.68</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>512.88</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01]</td><td>✅ 5/5</td><td>603.38</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>469.90</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>409.80</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>465.66</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01]</td><td>✅ 5/5</td><td>388.04</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01]</td><td>✅ 5/5</td><td>455.38</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_leaky_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-alpha_0.01]</td><td>✅ 5/5</td><td>3445.24</td><td>10.62</td><td>n/a</td></tr>
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
        <tr><td>test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>360.00</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>318.20</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>328.76</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>337.34</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>333.52</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>265.10</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>482.00</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>471.90</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>399.72</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>290.42</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128]</td><td>✅ 5/5</td><td>594.10</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128]</td><td>✅ 5/5</td><td>326.92</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>372.30</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>283.92</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>449.78</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>394.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>397.40</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>410.34</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>360.08</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>487.42</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>547.34</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>302.34</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256]</td><td>✅ 5/5</td><td>418.90</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256]</td><td>✅ 5/5</td><td>439.44</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>280.32</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>265.62</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>351.66</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>392.64</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>380.60</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>431.58</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>369.38</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>325.68</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>338.56</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>352.00</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512]</td><td>✅ 5/5</td><td>513.06</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512]</td><td>✅ 5/5</td><td>428.78</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192]</td><td>✅ 5/5</td><td>311.90</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192]</td><td>✅ 5/5</td><td>253.48</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>401.10</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>431.14</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>387.54</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096]</td><td>✅ 5/5</td><td>458.10</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>561.44</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>449.52</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048]</td><td>✅ 5/5</td><td>416.40</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048]</td><td>✅ 5/5</td><td>475.62</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024]</td><td>✅ 5/5</td><td>793.40</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024]</td><td>✅ 5/5</td><td>361.46</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_mem_copy[input_length_8388608-num_cores_8-num_channels_2-bypass_False-tile_size_4096]</td><td>✅ 5/5</td><td>2755.72</td><td>14.99</td><td>n/a</td></tr>
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
        <tr><td>test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>335.26</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>339.50</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>464.04</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>799.92</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>810.40</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>484.26</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>372.34</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>314.58</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>276.58</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>414.74</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>391.62</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>437.86</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>395.94</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>371.38</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>851.26</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>462.82</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>503.58</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>597.20</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>350.66</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>471.20</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>456.44</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>417.40</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>483.42</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>3768.56</td><td>9.17</td><td>n/a</td></tr>
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
        <tr><td>test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None]</td><td>✅ 5/5</td><td>364.86</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None]</td><td>✅ 5/5</td><td>458.72</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64]</td><td>✅ 5/5</td><td>3735.26</td><td>2.85</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_512-repeat_4-transfer_size_64]</td><td>✅ 5/5</td><td>434.98</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_repeat[rows_8-cols_64-repeat_4-transfer_size_None]</td><td>✅ 5/5</td><td>338.12</td><td>0.02</td><td>n/a</td></tr>
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
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>312.00</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>379.08</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>407.76</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>457.60</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>471.36</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>716.38</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>358.14</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>546.68</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>461.46</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True]</td><td>✅ 5/5</td><td>405.30</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False]</td><td>✅ 5/5</td><td>472.30</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>414.16</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>273.22</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>431.24</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>421.42</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>338.76</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>442.90</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>427.24</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>480.48</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>400.62</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True]</td><td>✅ 5/5</td><td>360.90</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False]</td><td>✅ 5/5</td><td>694.40</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>383.64</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>328.44</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>642.68</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>404.92</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>420.02</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>276.80</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>464.56</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>413.42</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>438.60</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True]</td><td>✅ 5/5</td><td>310.18</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False]</td><td>✅ 5/5</td><td>439.68</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False]</td><td>✅ 5/5</td><td>320.34</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>431.18</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>342.84</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>477.78</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>325.28</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>691.30</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>415.56</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False]</td><td>✅ 5/5</td><td>515.38</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True]</td><td>✅ 5/5</td><td>550.96</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False]</td><td>✅ 5/5</td><td>611.54</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8388608-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True]</td><td>✅ 5/5</td><td>2679.78</td><td>15.02</td><td>n/a</td></tr>
        <tr><td>test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_False]</td><td>✅ 5/5</td><td>2354.88</td><td>16.62</td><td>n/a</td></tr>
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
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>362.04</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>403.34</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>436.16</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>437.78</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>404.44</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>864.10</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>436.76</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>393.58</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>323.18</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>410.56</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>460.74</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>568.74</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>403.20</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>329.16</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>309.24</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>472.04</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>407.96</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>512.10</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>362.12</td><td>0.31</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>455.40</td><td>0.24</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>410.34</td><td>0.25</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>529.86</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>773.04</td><td>0.19</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>421.22</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>1129.32</td><td>10.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>463.76</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>510.58</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>323.98</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>348.80</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>385.20</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>383.34</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>413.72</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>332.70</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>414.28</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>340.18</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>367.20</td><td>0.13</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>328.50</td><td>0.14</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0]</td><td>✅ 5/5</td><td>399.92</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1]</td><td>✅ 5/5</td><td>495.96</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0]</td><td>✅ 5/5</td><td>396.16</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1]</td><td>✅ 5/5</td><td>351.48</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0]</td><td>✅ 5/5</td><td>394.80</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1]</td><td>✅ 5/5</td><td>487.96</td><td>0.09</td><td>n/a</td></tr>
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
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>370.26</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>470.74</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>675.28</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>494.72</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>389.46</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>445.84</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>287.48</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>423.38</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>347.28</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>389.68</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>429.38</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>444.48</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>416.68</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>479.36</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>432.76</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>387.78</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>493.10</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>554.80</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>455.08</td><td>0.07</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>405.46</td><td>0.11</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>388.56</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>327.88</td><td>0.12</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>379.86</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_sigmoid[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>3171.94</td><td>11.78</td><td>n/a</td></tr>
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
        <tr><td>test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>387.56</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>662.66</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>386.82</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>308.12</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>400.58</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>517.66</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>298.32</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>788.90</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>402.62</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>792.86</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>772.14</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_silu[input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>4403.98</td><td>7.66</td><td>n/a</td></tr>
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
        <tr><td>test_softmax[input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>2954.82</td><td>3.18</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>722.42</td><td>0.26</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>458.90</td><td>0.30</td><td>n/a</td></tr>
        <tr><td>test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>504.90</td><td>0.26</td><td>n/a</td></tr>
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
        <tr><td>test_strided_copy[bench_flat_4mi]</td><td>✅ 5/5</td><td>2977.48</td><td>6.85</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[chunked_transfer]</td><td>✅ 5/5</td><td>454.70</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[contiguous]</td><td>✅ 5/5</td><td>314.66</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[four_channels]</td><td>✅ 5/5</td><td>399.52</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_llama_full]</td><td>✅ 5/5</td><td>258.38</td><td>8.74</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot0]</td><td>✅ 5/5</td><td>374.48</td><td>0.39</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5]</td><td>✅ 5/5</td><td>335.94</td><td>0.47</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5_four_channels]</td><td>✅ 5/5</td><td>330.70</td><td>0.44</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot5_two_channels]</td><td>✅ 5/5</td><td>450.54</td><td>0.36</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[kv_slot_last]</td><td>✅ 5/5</td><td>319.44</td><td>0.44</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[two_channels]</td><td>✅ 5/5</td><td>426.74</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_strided_copy[two_channels_chunked]</td><td>✅ 5/5</td><td>316.68</td><td>0.01</td><td>n/a</td></tr>
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
        <tr><td>test_swiglu_decode[embedding_dim_1024-hidden_dim_3584]</td><td>✅ 5/5</td><td>17843.93</td><td>0.00</td><td>n/a</td></tr>
        <tr><td>test_swiglu_decode[embedding_dim_2048-hidden_dim_2048]</td><td>✅ 5/5</td><td>12686.38</td><td>0.00</td><td>n/a</td></tr>
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
        <tr><td>test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False]</td><td>✅ 5/5</td><td>21693.86</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True]</td><td>✅ 5/5</td><td>20953.59</td><td>0.10</td><td>n/a</td></tr>
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
        <tr><td>test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>487.28</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>491.54</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>458.42</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>558.16</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]</td><td>✅ 5/5</td><td>574.98</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]</td><td>✅ 5/5</td><td>426.00</td><td>0.01</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>340.54</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>467.08</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>333.10</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>453.92</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]</td><td>✅ 5/5</td><td>410.90</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]</td><td>✅ 5/5</td><td>818.94</td><td>0.02</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>284.32</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>362.72</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>405.70</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>633.18</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]</td><td>✅ 5/5</td><td>420.20</td><td>0.05</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]</td><td>✅ 5/5</td><td>721.48</td><td>0.03</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>646.38</td><td>0.08</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]</td><td>✅ 5/5</td><td>427.34</td><td>0.09</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]</td><td>✅ 5/5</td><td>509.66</td><td>0.06</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]</td><td>✅ 5/5</td><td>368.98</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]</td><td>✅ 5/5</td><td>398.56</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_tanh[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096]</td><td>✅ 5/5</td><td>3194.68</td><td>12.11</td><td>n/a</td></tr>
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
        <tr><td>test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>802.66</td><td>1.72</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>730.04</td><td>1.46</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1123.30</td><td>1.80</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>615.72</td><td>1.94</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>2144.34</td><td>1.57</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>674.08</td><td>3.44</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1569.34</td><td>2.23</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>790.48</td><td>2.67</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1228.08</td><td>2.79</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>2345.68</td><td>1.83</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1400.30</td><td>3.41</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1190.02</td><td>3.54</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1291.98</td><td>5.25</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>662.60</td><td>7.03</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1433.84</td><td>4.06</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>1148.18</td><td>6.45</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>799.84</td><td>1.08</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2]</td><td>✅ 5/5</td><td>1064.74</td><td>1.96</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4]</td><td>✅ 5/5</td><td>1908.20</td><td>1.77</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>468.16</td><td>1.25</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>381.50</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>354.12</td><td>0.10</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>365.76</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>374.88</td><td>0.20</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>464.94</td><td>0.15</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>463.68</td><td>0.33</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>489.72</td><td>0.32</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>442.54</td><td>0.31</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>416.12</td><td>0.04</td><td>n/a</td></tr>
        <tr><td>test_transpose[M_8192-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]</td><td>✅ 5/5</td><td>3821.12</td><td>4.74</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

