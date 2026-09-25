# IRON Trends


<details>
<summary>iron/operators/axpy</summary>


### test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.05 (+12.40%)</td><td>0.04 (+16.55%)</td><td>0.03 (+7.80%)</td><td>0.02 (+16.33%)</td><td>0.01 (+16.36%)</td><td>536.60 (-14.05%)</td><td>392.12 (-14.33%)</td><td>461.50 (-7.24%)</td><td>239.70 (-11.06%)</td><td>139.64 (-15.60%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>624.30 (n/a)</td><td>457.70 (n/a)</td><td>497.50 (n/a)</td><td>269.50 (n/a)</td><td>165.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.05 (+6.00%)</td><td>0.04 (+17.66%)</td><td>0.05 <b>(+60.57%)</b></td><td>0.02 (+2.99%)</td><td>0.01 (+2.48%)</td><td>519.70 (-2.90%)</td><td>338.64 (-15.24%)</td><td>270.80 <b>(-37.72%)</b></td><td>241.60 (-5.66%)</td><td>120.01 (-5.06%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.20 (n/a)</td><td>399.52 (n/a)</td><td>434.80 (n/a)</td><td>256.10 (n/a)</td><td>126.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.05 <b>(+27.39%)</b></td><td>0.03 <b>(+20.70%)</b></td><td>0.03 (+15.48%)</td><td>0.02 (-12.05%)</td><td>0.01 <b>(+94.29%)</b></td><td>651.90 (+13.69%)</td><td>416.60 (-8.33%)</td><td>390.60 (-13.39%)</td><td>246.30 <b>(-21.49%)</b></td><td>180.13 <b>(+58.81%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>573.40 (n/a)</td><td>454.48 (n/a)</td><td>451.00 (n/a)</td><td>313.70 (n/a)</td><td>113.43 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/dequant</summary>


### test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (+6.54%)</td><td>0.02 (-9.01%)</td><td>0.02 <b>(-22.63%)</b></td><td>0.01 (-5.46%)</td><td>0.01 <b>(+39.47%)</b></td><td>534.90 (+5.77%)</td><td>367.40 (+16.10%)</td><td>340.60 <b>(+29.21%)</b></td><td>231.10 (-6.13%)</td><td>143.22 <b>(+31.91%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>505.70 (n/a)</td><td>316.44 (n/a)</td><td>263.60 (n/a)</td><td>246.20 (n/a)</td><td>108.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (+6.77%)</td><td>0.02 (-4.49%)</td><td>0.02 (-4.63%)</td><td>0.01 (+5.45%)</td><td>0.01 (+15.47%)</td><td>423.80 (-5.17%)</td><td>291.96 (+5.61%)</td><td>252.70 (+4.85%)</td><td>194.30 (-6.32%)</td><td>95.02 (-1.86%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>446.90 (n/a)</td><td>276.44 (n/a)</td><td>241.00 (n/a)</td><td>207.40 (n/a)</td><td>96.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (+7.78%)</td><td>0.02 <b>(+20.43%)</b></td><td>0.02 <b>(+51.15%)</b></td><td>0.01 <b>(+27.47%)</b></td><td>0.01 <b>(-21.58%)</b></td><td>528.30 <b>(-21.55%)</b></td><td>321.36 <b>(-23.59%)</b></td><td>279.70 <b>(-33.85%)</b></td><td>215.30 (-7.20%)</td><td>122.34 <b>(-35.50%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>673.40 (n/a)</td><td>420.60 (n/a)</td><td>422.80 (n/a)</td><td>232.00 (n/a)</td><td>189.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (+11.58%)</td><td>0.01 (+14.77%)</td><td>0.01 (+10.42%)</td><td>0.01 <b>(+163.42%)</b></td><td>0.01 (-5.46%)</td><td>711.60 <b>(-62.04%)</b></td><td>439.04 <b>(-35.49%)</b></td><td>382.00 (-9.44%)</td><td>241.70 (-10.38%)</td><td>198.99 <b>(-70.49%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1874.40 (n/a)</td><td>680.58 (n/a)</td><td>421.80 (n/a)</td><td>269.70 (n/a)</td><td>674.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 <b>(+143.50%)</b></td><td>0.02 <b>(+52.10%)</b></td><td>0.01 (+12.72%)</td><td>0.01 <b>(+80.36%)</b></td><td>0.01 <b>(+197.22%)</b></td><td>581.30 <b>(-44.56%)</b></td><td>398.80 <b>(-27.37%)</b></td><td>385.10 (-11.29%)</td><td>155.50 <b>(-58.94%)</b></td><td>183.54 <b>(-34.61%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1048.50 (n/a)</td><td>549.10 (n/a)</td><td>434.10 (n/a)</td><td>378.70 (n/a)</td><td>280.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (-4.59%)</td><td>0.01 (+2.65%)</td><td>0.01 (-4.66%)</td><td>0.01 (+6.70%)</td><td>0.00 (-10.17%)</td><td>476.10 (-6.26%)</td><td>391.48 (-3.41%)</td><td>430.50 (+4.90%)</td><td>292.90 (+4.79%)</td><td>78.42 (-11.84%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.90 (n/a)</td><td>405.30 (n/a)</td><td>410.40 (n/a)</td><td>279.50 (n/a)</td><td>88.96 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_add</summary>


### test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>606.90 (n/a)</td><td>395.32 (n/a)</td><td>354.40 (n/a)</td><td>249.40 (n/a)</td><td>152.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.90 (n/a)</td><td>382.24 (n/a)</td><td>438.10 (n/a)</td><td>215.90 (n/a)</td><td>130.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>409.80 (n/a)</td><td>324.96 (n/a)</td><td>305.60 (n/a)</td><td>224.90 (n/a)</td><td>79.27 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_mul</summary>


### test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>575.70 (n/a)</td><td>450.20 (n/a)</td><td>399.30 (n/a)</td><td>363.10 (n/a)</td><td>94.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>427.80 (n/a)</td><td>296.46 (n/a)</td><td>258.70 (n/a)</td><td>209.80 (n/a)</td><td>88.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2003.70 (n/a)</td><td>735.82 (n/a)</td><td>505.50 (n/a)</td><td>278.00 (n/a)</td><td>721.66 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/flm/dequant</summary>


### test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of]

_No metrics available._


### test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of]

_No metrics available._


</details>


<details>
<summary>iron/operators/flm/gemm</summary>


### test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024]

_No metrics available._


### test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048]

_No metrics available._


### test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.98 (+1.54%)</td><td>0.73 (+10.64%)</td><td>0.69 (+3.43%)</td><td>0.62 <b>(+188.21%)</b></td><td>0.14 <b>(-49.22%)</b></td><td>735.80 <b>(-65.30%)</b></td><td>645.88 <b>(-29.54%)</b></td><td>660.40 (-3.31%)</td><td>468.00 (-1.52%)</td><td>104.63 <b>(-84.65%)</b></td><td>71.70 (+1.54%)</td><td>53.31 (+10.64%)</td><td>50.81 (+3.43%)</td><td>45.60 <b>(+188.21%)</b></td><td>10.53 <b>(-49.22%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.97 (n/a)</td><td>0.66 (n/a)</td><td>0.67 (n/a)</td><td>0.22 (n/a)</td><td>0.28 (n/a)</td><td>2120.70 (n/a)</td><td>916.62 (n/a)</td><td>683.00 (n/a)</td><td>475.20 (n/a)</td><td>681.68 (n/a)</td><td>70.62 (n/a)</td><td>48.18 (n/a)</td><td>49.13 (n/a)</td><td>15.82 (n/a)</td><td>20.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.40 (-5.59%)</td><td>0.98 (-14.73%)</td><td>1.15 (+3.01%)</td><td>0.27 <b>(-53.78%)</b></td><td>0.45 <b>(+24.02%)</b></td><td>2420.70 <b>(+116.37%)</b></td><td>957.30 <b>(+49.47%)</b></td><td>569.50 (-2.93%)</td><td>469.70 (+5.93%)</td><td>827.34 <b>(+198.61%)</b></td><td>142.88 (-5.59%)</td><td>99.85 (-14.73%)</td><td>117.83 (+3.01%)</td><td>27.72 <b>(-53.78%)</b></td><td>45.65 <b>(+24.02%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.48 (n/a)</td><td>1.14 (n/a)</td><td>1.12 (n/a)</td><td>0.59 (n/a)</td><td>0.36 (n/a)</td><td>1118.80 (n/a)</td><td>640.48 (n/a)</td><td>586.70 (n/a)</td><td>443.40 (n/a)</td><td>277.07 (n/a)</td><td>151.34 (n/a)</td><td>117.10 (n/a)</td><td>114.39 (n/a)</td><td>59.98 (n/a)</td><td>36.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.49 (+9.46%)</td><td>1.25 (+16.11%)</td><td>1.29 <b>(+31.22%)</b></td><td>0.96 (-1.03%)</td><td>0.20 (+18.41%)</td><td>789.00 (+1.04%)</td><td>618.50 (-13.42%)</td><td>582.70 <b>(-23.79%)</b></td><td>505.70 (-8.65%)</td><td>106.65 (+12.67%)</td><td>165.87 (+9.46%)</td><td>138.62 (+16.11%)</td><td>143.96 <b>(+31.22%)</b></td><td>106.32 (-1.03%)</td><td>21.95 (+18.41%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.36 (n/a)</td><td>1.07 (n/a)</td><td>0.99 (n/a)</td><td>0.97 (n/a)</td><td>0.17 (n/a)</td><td>780.90 (n/a)</td><td>714.38 (n/a)</td><td>764.60 (n/a)</td><td>553.60 (n/a)</td><td>94.66 (n/a)</td><td>151.53 (n/a)</td><td>119.39 (n/a)</td><td>109.71 (n/a)</td><td>107.42 (n/a)</td><td>18.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.41 (-12.66%)</td><td>0.90 <b>(-21.47%)</b></td><td>1.17 (-15.44%)</td><td>0.28 (-1.89%)</td><td>0.50 (-6.55%)</td><td>3791.30 (+1.92%)</td><td>1724.80 <b>(+24.75%)</b></td><td>898.70 (+18.25%)</td><td>743.20 (+14.48%)</td><td>1318.26 (+0.17%)</td><td>180.59 (-12.66%)</td><td>114.96 <b>(-21.47%)</b></td><td>149.35 (-15.44%)</td><td>35.40 (-1.89%)</td><td>63.92 (-6.55%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.62 (n/a)</td><td>1.14 (n/a)</td><td>1.38 (n/a)</td><td>0.28 (n/a)</td><td>0.53 (n/a)</td><td>3719.70 (n/a)</td><td>1382.58 (n/a)</td><td>760.00 (n/a)</td><td>649.20 (n/a)</td><td>1316.01 (n/a)</td><td>206.76 (n/a)</td><td>146.38 (n/a)</td><td>176.61 (n/a)</td><td>36.08 (n/a)</td><td>68.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.90 (+6.78%)</td><td>1.58 <b>(+20.81%)</b></td><td>1.55 <b>(+24.79%)</b></td><td>1.29 <b>(+43.92%)</b></td><td>0.22 <b>(-30.94%)</b></td><td>811.90 <b>(-30.51%)</b></td><td>675.16 (-19.89%)</td><td>677.80 (-19.86%)</td><td>553.00 (-6.37%)</td><td>93.73 <b>(-55.38%)</b></td><td>242.69 (+6.78%)</td><td>201.87 <b>(+20.81%)</b></td><td>198.02 <b>(+24.79%)</b></td><td>165.32 <b>(+43.92%)</b></td><td>28.03 <b>(-30.94%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.78 (n/a)</td><td>1.31 (n/a)</td><td>1.24 (n/a)</td><td>0.90 (n/a)</td><td>0.32 (n/a)</td><td>1168.40 (n/a)</td><td>842.78 (n/a)</td><td>845.80 (n/a)</td><td>590.60 (n/a)</td><td>210.05 (n/a)</td><td>227.27 (n/a)</td><td>167.10 (n/a)</td><td>158.68 (n/a)</td><td>114.87 (n/a)</td><td>40.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>2.18 (+0.36%)</td><td>1.92 <b>(+32.37%)</b></td><td>1.78 (+1.40%)</td><td>1.77 <b>(+234.99%)</b></td><td>0.20 <b>(-70.01%)</b></td><td>592.60 <b>(-70.15%)</b></td><td>551.70 <b>(-41.31%)</b></td><td>590.60 (-1.39%)</td><td>482.10 (-0.35%)</td><td>55.07 <b>(-91.17%)</b></td><td>278.41 (+0.36%)</td><td>245.31 <b>(+32.37%)</b></td><td>227.24 (+1.40%)</td><td>226.47 <b>(+234.99%)</b></td><td>25.56 <b>(-70.01%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>2.17 (n/a)</td><td>1.45 (n/a)</td><td>1.75 (n/a)</td><td>0.53 (n/a)</td><td>0.67 (n/a)</td><td>1985.30 (n/a)</td><td>940.04 (n/a)</td><td>598.90 (n/a)</td><td>483.80 (n/a)</td><td>623.39 (n/a)</td><td>277.40 (n/a)</td><td>185.33 (n/a)</td><td>224.09 (n/a)</td><td>67.61 (n/a)</td><td>85.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.48 (-14.23%)</td><td>1.14 (-4.21%)</td><td>1.20 (+3.27%)</td><td>0.50 <b>(-33.03%)</b></td><td>0.39 (+12.22%)</td><td>2079.30 <b>(+49.31%)</b></td><td>1070.26 (+13.54%)</td><td>876.70 (-3.16%)</td><td>710.20 (+16.60%)</td><td>572.98 <b>(+101.94%)</b></td><td>188.98 (-14.23%)</td><td>146.15 (-4.21%)</td><td>153.10 (+3.27%)</td><td>64.55 <b>(-33.03%)</b></td><td>49.87 (+12.22%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.72 (n/a)</td><td>1.19 (n/a)</td><td>1.16 (n/a)</td><td>0.75 (n/a)</td><td>0.35 (n/a)</td><td>1392.60 (n/a)</td><td>942.66 (n/a)</td><td>905.30 (n/a)</td><td>609.10 (n/a)</td><td>283.74 (n/a)</td><td>220.34 (n/a)</td><td>152.58 (n/a)</td><td>148.25 (n/a)</td><td>96.38 (n/a)</td><td>44.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.73 (+7.05%)</td><td>0.59 (+10.38%)</td><td>0.60 (+19.42%)</td><td>0.37 (-14.30%)</td><td>0.14 <b>(+55.22%)</b></td><td>963.60 (+16.67%)</td><td>651.86 (-6.12%)</td><td>600.30 (-16.26%)</td><td>493.20 (-6.57%)</td><td>189.42 <b>(+75.96%)</b></td><td>34.02 (+7.05%)</td><td>27.25 (+10.38%)</td><td>27.95 (+19.42%)</td><td>17.41 (-14.30%)</td><td>6.63 <b>(+55.22%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.68 (n/a)</td><td>0.53 (n/a)</td><td>0.50 (n/a)</td><td>0.44 (n/a)</td><td>0.09 (n/a)</td><td>825.90 (n/a)</td><td>694.32 (n/a)</td><td>716.90 (n/a)</td><td>527.90 (n/a)</td><td>107.65 (n/a)</td><td>31.78 (n/a)</td><td>24.69 (n/a)</td><td>23.40 (n/a)</td><td>20.31 (n/a)</td><td>4.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>2.91 (-15.19%)</td><td>2.20 (-19.31%)</td><td>2.49 <b>(-21.43%)</b></td><td>1.16 (+4.38%)</td><td>0.69 <b>(-28.30%)</b></td><td>2259.10 (-4.19%)</td><td>1323.92 (+15.31%)</td><td>1051.70 <b>(+27.28%)</b></td><td>901.70 (+17.92%)</td><td>551.90 (-19.15%)</td><td>595.43 (-15.19%)</td><td>451.08 (-19.31%)</td><td>510.50 <b>(-21.43%)</b></td><td>237.65 (+4.38%)</td><td>140.48 <b>(-28.30%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>3.43 (n/a)</td><td>2.73 (n/a)</td><td>3.17 (n/a)</td><td>1.11 (n/a)</td><td>0.96 (n/a)</td><td>2358.00 (n/a)</td><td>1148.12 (n/a)</td><td>826.30 (n/a)</td><td>764.70 (n/a)</td><td>682.66 (n/a)</td><td>702.10 (n/a)</td><td>559.02 (n/a)</td><td>649.74 (n/a)</td><td>227.68 (n/a)</td><td>195.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm_split_leg_bounds[iter0]

_No metrics available._


### test_gemm_split_leg_bounds[iter1]

_No metrics available._


### test_gemm_split_leg_bounds[iter2]

_No metrics available._


### test_gemm_split_leg_bounds[iter3]

_No metrics available._


### test_gemm_split_leg_bounds[iter4]

_No metrics available._


### test_gemm_split_leg_bounds_runs[iter0]

_No metrics available._


### test_gemm_split_leg_bounds_runs[iter1]

_No metrics available._


### test_gemm_split_leg_bounds_runs[iter2]

_No metrics available._


### test_gemm_split_leg_bounds_runs[iter3]

_No metrics available._


### test_gemm_split_leg_bounds_runs[iter4]

_No metrics available._


### test_gemm_tile_options[tn128-ma32-default]

_No metrics available._


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn16-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn32-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma16-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma32-default]

_No metrics available._


</details>


<details>
<summary>iron/operators/gelu</summary>


### test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.50 (n/a)</td><td>357.24 (n/a)</td><td>312.20 (n/a)</td><td>253.00 (n/a)</td><td>96.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.40 (n/a)</td><td>390.30 (n/a)</td><td>331.20 (n/a)</td><td>259.00 (n/a)</td><td>141.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1930.70 (n/a)</td><td>757.52 (n/a)</td><td>553.30 (n/a)</td><td>248.30 (n/a)</td><td>691.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1038.80 (n/a)</td><td>526.10 (n/a)</td><td>434.00 (n/a)</td><td>244.00 (n/a)</td><td>301.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.00 (n/a)</td><td>433.72 (n/a)</td><td>470.70 (n/a)</td><td>223.00 (n/a)</td><td>120.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.50 (n/a)</td><td>447.30 (n/a)</td><td>481.10 (n/a)</td><td>256.30 (n/a)</td><td>132.39 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gemm</summary>


### test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.54 (+6.94%)</td><td>0.47 <b>(+25.42%)</b></td><td>0.51 <b>(+34.97%)</b></td><td>0.35 <b>(+108.50%)</b></td><td>0.09 <b>(-30.51%)</b></td><td>623.90 <b>(-52.04%)</b></td><td>489.58 <b>(-28.71%)</b></td><td>433.10 <b>(-25.90%)</b></td><td>408.90 (-6.49%)</td><td>99.54 <b>(-71.55%)</b></td><td>23.08 (+6.94%)</td><td>19.88 <b>(+25.42%)</b></td><td>21.79 <b>(+34.97%)</b></td><td>15.13 <b>(+108.50%)</b></td><td>3.73 <b>(-30.51%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.51 (n/a)</td><td>0.37 (n/a)</td><td>0.38 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>1300.90 (n/a)</td><td>686.72 (n/a)</td><td>584.50 (n/a)</td><td>437.30 (n/a)</td><td>349.93 (n/a)</td><td>21.58 (n/a)</td><td>15.85 (n/a)</td><td>16.15 (n/a)</td><td>7.25 (n/a)</td><td>5.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.47 (-0.31%)</td><td>0.42 (+18.00%)</td><td>0.42 (+14.36%)</td><td>0.36 <b>(+92.06%)</b></td><td>0.04 <b>(-57.77%)</b></td><td>614.80 <b>(-47.93%)</b></td><td>529.24 <b>(-22.63%)</b></td><td>526.70 (-12.57%)</td><td>467.30 (+0.32%)</td><td>57.92 <b>(-79.61%)</b></td><td>20.20 (-0.31%)</td><td>18.00 (+18.00%)</td><td>17.92 (+14.36%)</td><td>15.35 <b>(+92.06%)</b></td><td>1.91 <b>(-57.77%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.47 (n/a)</td><td>0.36 (n/a)</td><td>0.37 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>1180.80 (n/a)</td><td>684.00 (n/a)</td><td>602.40 (n/a)</td><td>465.80 (n/a)</td><td>284.11 (n/a)</td><td>20.26 (n/a)</td><td>15.25 (n/a)</td><td>15.67 (n/a)</td><td>7.99 (n/a)</td><td>4.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.31 (+2.14%)</td><td>0.31 (+2.95%)</td><td>0.31 (+3.87%)</td><td>0.30 (+2.02%)</td><td>0.00 (-8.81%)</td><td>84163.80 (-1.98%)</td><td>82144.92 (-2.87%)</td><td>81868.40 (-3.73%)</td><td>80843.80 (-2.10%)</td><td>1222.20 (-12.25%)</td><td>212.51 (+2.14%)</td><td>209.18 (+2.95%)</td><td>209.85 (+3.87%)</td><td>204.12 (+2.02%)</td><td>3.08 (-8.80%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.00 (n/a)</td><td>85863.60 (n/a)</td><td>84569.42 (n/a)</td><td>85036.20 (n/a)</td><td>82577.40 (n/a)</td><td>1392.87 (n/a)</td><td>208.05 (n/a)</td><td>203.19 (n/a)</td><td>202.03 (n/a)</td><td>200.08 (n/a)</td><td>3.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.17 (+0.71%)</td><td>1.14 (-0.58%)</td><td>1.15 (+0.26%)</td><td>1.11 (-2.36%)</td><td>0.02 <b>(+188.06%)</b></td><td>22664.60 (+2.41%)</td><td>22075.86 (+0.62%)</td><td>21917.00 (-0.26%)</td><td>21539.20 (-0.70%)</td><td>466.48 <b>(+193.88%)</b></td><td>797.61 (+0.71%)</td><td>778.50 (-0.58%)</td><td>783.86 (+0.26%)</td><td>758.00 (-2.36%)</td><td>16.39 <b>(+188.06%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.16 (n/a)</td><td>1.15 (n/a)</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>0.01 (n/a)</td><td>22130.60 (n/a)</td><td>21940.88 (n/a)</td><td>21973.90 (n/a)</td><td>21691.20 (n/a)</td><td>158.73 (n/a)</td><td>792.02 (n/a)</td><td>783.04 (n/a)</td><td>781.83 (n/a)</td><td>776.29 (n/a)</td><td>5.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>4.05 (-1.56%)</td><td>2.67 (-9.55%)</td><td>2.08 <b>(-33.50%)</b></td><td>1.81 (-1.67%)</td><td>1.02 (+0.85%)</td><td>4464.70 (+1.69%)</td><td>3351.30 (+10.81%)</td><td>3877.50 <b>(+50.38%)</b></td><td>1989.00 (+1.59%)</td><td>1115.24 (+1.02%)</td><td>1062.81 (-1.56%)</td><td>701.08 (-9.55%)</td><td>545.18 <b>(-33.50%)</b></td><td>473.48 (-1.67%)</td><td>266.46 (+0.85%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>4.12 (n/a)</td><td>2.96 (n/a)</td><td>3.13 (n/a)</td><td>1.84 (n/a)</td><td>1.01 (n/a)</td><td>4390.30 (n/a)</td><td>3024.24 (n/a)</td><td>2578.40 (n/a)</td><td>1957.90 (n/a)</td><td>1103.93 (n/a)</td><td>1079.67 (n/a)</td><td>775.10 (n/a)</td><td>819.85 (n/a)</td><td>481.50 (n/a)</td><td>264.23 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-trace_size_0-partition_N_4]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.32 (+2.36%)</td><td>0.21 (-13.22%)</td><td>0.19 (-8.51%)</td><td>0.15 (-13.92%)</td><td>0.06 (+2.00%)</td><td>8291.20 (+16.17%)</td><td>6432.66 (+16.14%)</td><td>6492.90 (+9.30%)</td><td>3924.20 (-2.31%)</td><td>1608.81 (+14.45%)</td><td>17.10 (+2.36%)</td><td>11.12 (-13.22%)</td><td>10.34 (-8.51%)</td><td>8.09 (-13.92%)</td><td>3.50 (+2.00%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>7136.90 (n/a)</td><td>5538.68 (n/a)</td><td>5940.60 (n/a)</td><td>4016.90 (n/a)</td><td>1405.71 (n/a)</td><td>16.71 (n/a)</td><td>12.81 (n/a)</td><td>11.30 (n/a)</td><td>9.40 (n/a)</td><td>3.43 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gemv</summary>


### test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>3.81 (n/a)</td><td>3.74 (n/a)</td><td>3.74 (n/a)</td><td>3.65 (n/a)</td><td>0.06 (n/a)</td><td>3.80 (n/a)</td><td>3.74 (n/a)</td><td>3.73 (n/a)</td><td>3.64 (n/a)</td><td>0.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>7.31 (-2.97%)</td><td>6.23 (-5.36%)</td><td>5.95 (-7.21%)</td><td>5.34 (-1.72%)</td><td>0.84 (-1.74%)</td><td>7.31 (-2.97%)</td><td>6.23 (-5.36%)</td><td>5.94 (-7.21%)</td><td>5.34 (-1.72%)</td><td>0.84 (-1.74%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>7.54 (n/a)</td><td>6.58 (n/a)</td><td>6.41 (n/a)</td><td>5.43 (n/a)</td><td>0.86 (n/a)</td><td>7.53 (n/a)</td><td>6.58 (n/a)</td><td>6.41 (n/a)</td><td>5.43 (n/a)</td><td>0.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>13.97 (+1.35%)</td><td>9.56 (-19.65%)</td><td>8.47 <b>(-37.45%)</b></td><td>7.41 (-13.78%)</td><td>2.58 (+2.63%)</td><td>13.96 (+1.35%)</td><td>9.55 (-19.65%)</td><td>8.47 <b>(-37.45%)</b></td><td>7.40 (-13.78%)</td><td>2.58 (+2.63%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>13.79 (n/a)</td><td>11.89 (n/a)</td><td>13.55 (n/a)</td><td>8.59 (n/a)</td><td>2.52 (n/a)</td><td>13.78 (n/a)</td><td>11.89 (n/a)</td><td>13.54 (n/a)</td><td>8.59 (n/a)</td><td>2.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>3.89 (n/a)</td><td>3.64 (n/a)</td><td>3.64 (n/a)</td><td>3.35 (n/a)</td><td>0.20 (n/a)</td><td>3.88 (n/a)</td><td>3.64 (n/a)</td><td>3.64 (n/a)</td><td>3.35 (n/a)</td><td>0.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>7.13 (-4.31%)</td><td>6.51 (+1.04%)</td><td>6.60 (+5.34%)</td><td>5.65 (-4.90%)</td><td>0.60 (-4.20%)</td><td>7.12 (-4.31%)</td><td>6.51 (+1.04%)</td><td>6.59 (+5.34%)</td><td>5.65 (-4.90%)</td><td>0.60 (-4.20%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>7.45 (n/a)</td><td>6.44 (n/a)</td><td>6.26 (n/a)</td><td>5.94 (n/a)</td><td>0.63 (n/a)</td><td>7.44 (n/a)</td><td>6.44 (n/a)</td><td>6.26 (n/a)</td><td>5.94 (n/a)</td><td>0.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>13.54 <b>(+21.38%)</b></td><td>9.79 (+14.69%)</td><td>8.52 (+2.94%)</td><td>7.97 <b>(+22.05%)</b></td><td>2.36 <b>(+33.47%)</b></td><td>13.53 <b>(+21.38%)</b></td><td>9.78 (+14.69%)</td><td>8.52 (+2.94%)</td><td>7.96 <b>(+22.05%)</b></td><td>2.36 <b>(+33.47%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>11.16 (n/a)</td><td>8.54 (n/a)</td><td>8.28 (n/a)</td><td>6.53 (n/a)</td><td>1.77 (n/a)</td><td>11.15 (n/a)</td><td>8.53 (n/a)</td><td>8.28 (n/a)</td><td>6.53 (n/a)</td><td>1.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>2.38 <b>(-20.83%)</b></td><td>1.57 <b>(-28.91%)</b></td><td>1.46 <b>(-47.20%)</b></td><td>1.02 (-16.84%)</td><td>0.60 <b>(-33.38%)</b></td><td>2.37 <b>(-20.83%)</b></td><td>1.57 <b>(-28.91%)</b></td><td>1.46 <b>(-47.20%)</b></td><td>1.02 (-16.84%)</td><td>0.59 <b>(-33.38%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>3.00 (n/a)</td><td>2.21 (n/a)</td><td>2.77 (n/a)</td><td>1.23 (n/a)</td><td>0.89 (n/a)</td><td>3.00 (n/a)</td><td>2.21 (n/a)</td><td>2.76 (n/a)</td><td>1.23 (n/a)</td><td>0.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.52 <b>(+27.69%)</b></td><td>0.31 <b>(+56.44%)</b></td><td>0.27 <b>(+147.72%)</b></td><td>0.11 <b>(+40.63%)</b></td><td>0.15 (-1.13%)</td><td>0.51 <b>(+27.69%)</b></td><td>0.30 <b>(+56.44%)</b></td><td>0.27 <b>(+147.72%)</b></td><td>0.10 <b>(+40.63%)</b></td><td>0.15 (-1.13%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.41 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.15 (n/a)</td><td>0.40 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.40 <b>(-52.36%)</b></td><td>0.25 <b>(-53.46%)</b></td><td>0.33 <b>(-29.92%)</b></td><td>0.08 <b>(-72.88%)</b></td><td>0.16 <b>(-28.29%)</b></td><td>0.40 <b>(-52.36%)</b></td><td>0.25 <b>(-53.46%)</b></td><td>0.33 <b>(-29.92%)</b></td><td>0.08 <b>(-72.88%)</b></td><td>0.16 <b>(-28.29%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.85 (n/a)</td><td>0.54 (n/a)</td><td>0.47 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.84 (n/a)</td><td>0.54 (n/a)</td><td>0.47 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>2.49 <b>(+31.69%)</b></td><td>1.31 (+5.20%)</td><td>0.83 <b>(-30.11%)</b></td><td>0.43 <b>(-41.62%)</b></td><td>1.03 <b>(+99.29%)</b></td><td>2.45 <b>(+31.69%)</b></td><td>1.29 (+5.20%)</td><td>0.82 <b>(-30.11%)</b></td><td>0.42 <b>(-41.62%)</b></td><td>1.01 <b>(+99.29%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.89 (n/a)</td><td>1.25 (n/a)</td><td>1.19 (n/a)</td><td>0.74 (n/a)</td><td>0.52 (n/a)</td><td>1.86 (n/a)</td><td>1.23 (n/a)</td><td>1.17 (n/a)</td><td>0.73 (n/a)</td><td>0.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]

_No metrics available._


### test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]

_No metrics available._


### test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]

_No metrics available._


</details>


<details>
<summary>iron/operators/layer_norm</summary>


### test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2052.70 (n/a)</td><td>729.52 (n/a)</td><td>449.20 (n/a)</td><td>251.90 (n/a)</td><td>745.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.10 (n/a)</td><td>395.34 (n/a)</td><td>284.30 (n/a)</td><td>234.20 (n/a)</td><td>194.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1028.00 (n/a)</td><td>466.26 (n/a)</td><td>390.90 (n/a)</td><td>238.00 (n/a)</td><td>323.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>663.40 (n/a)</td><td>431.94 (n/a)</td><td>418.20 (n/a)</td><td>274.30 (n/a)</td><td>160.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1322.90 (n/a)</td><td>542.22 (n/a)</td><td>341.10 (n/a)</td><td>298.70 (n/a)</td><td>440.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>639.30 (n/a)</td><td>465.80 (n/a)</td><td>472.90 (n/a)</td><td>240.50 (n/a)</td><td>162.29 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/leaky_relu</summary>


### test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (-17.24%)</td><td>0.02 <b>(-31.30%)</b></td><td>0.02 <b>(-42.65%)</b></td><td>0.01 <b>(-48.08%)</b></td><td>0.01 (+19.40%)</td><td>667.90 <b>(+92.59%)</b></td><td>421.90 <b>(+57.25%)</b></td><td>430.40 <b>(+74.32%)</b></td><td>247.90 <b>(+20.81%)</b></td><td>162.56 <b>(+170.40%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>346.80 (n/a)</td><td>268.30 (n/a)</td><td>246.90 (n/a)</td><td>205.20 (n/a)</td><td>60.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (-15.84%)</td><td>0.02 (-12.63%)</td><td>0.03 (-9.24%)</td><td>0.01 <b>(-28.45%)</b></td><td>0.01 (+0.21%)</td><td>666.10 <b>(+39.76%)</b></td><td>383.04 (+19.17%)</td><td>309.30 (+10.19%)</td><td>279.60 (+18.83%)</td><td>162.45 <b>(+67.32%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.60 (n/a)</td><td>321.42 (n/a)</td><td>280.70 (n/a)</td><td>235.30 (n/a)</td><td>97.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 <b>(-21.00%)</b></td><td>0.02 <b>(-27.88%)</b></td><td>0.02 <b>(-48.03%)</b></td><td>0.01 <b>(-20.79%)</b></td><td>0.01 <b>(-26.38%)</b></td><td>647.30 <b>(+26.25%)</b></td><td>463.16 <b>(+36.54%)</b></td><td>488.50 <b>(+92.40%)</b></td><td>309.60 <b>(+26.57%)</b></td><td>147.82 (+15.64%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.70 (n/a)</td><td>339.20 (n/a)</td><td>253.90 (n/a)</td><td>244.60 (n/a)</td><td>127.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (+6.74%)</td><td>0.03 (+3.68%)</td><td>0.03 (-1.78%)</td><td>0.02 (+4.59%)</td><td>0.01 <b>(+21.45%)</b></td><td>533.50 (-4.39%)</td><td>367.38 (-0.49%)</td><td>306.80 (+1.79%)</td><td>233.20 (-6.31%)</td><td>146.88 (+11.24%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.00 (n/a)</td><td>369.20 (n/a)</td><td>301.40 (n/a)</td><td>248.90 (n/a)</td><td>132.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 <b>(+69.22%)</b></td><td>0.03 <b>(+44.70%)</b></td><td>0.03 <b>(+43.03%)</b></td><td>0.02 <b>(+31.15%)</b></td><td>0.01 <b>(+134.97%)</b></td><td>492.20 <b>(-23.75%)</b></td><td>346.38 <b>(-27.73%)</b></td><td>324.90 <b>(-30.07%)</b></td><td>228.30 <b>(-40.90%)</b></td><td>107.42 (+5.34%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>645.50 (n/a)</td><td>479.26 (n/a)</td><td>464.60 (n/a)</td><td>386.30 (n/a)</td><td>101.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (-16.87%)</td><td>0.02 (-17.39%)</td><td>0.02 (-10.85%)</td><td>0.01 (-11.56%)</td><td>0.01 <b>(-21.74%)</b></td><td>602.20 (+13.07%)</td><td>478.44 (+18.67%)</td><td>511.30 (+12.18%)</td><td>264.70 <b>(+20.26%)</b></td><td>128.19 (+1.30%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.60 (n/a)</td><td>403.16 (n/a)</td><td>455.80 (n/a)</td><td>220.10 (n/a)</td><td>126.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (-16.71%)</td><td>0.02 (-9.28%)</td><td>0.02 (+2.37%)</td><td>0.01 (-12.33%)</td><td>0.01 <b>(-25.69%)</b></td><td>601.80 (+14.06%)</td><td>440.96 (+8.17%)</td><td>417.80 (-2.31%)</td><td>284.00 <b>(+20.03%)</b></td><td>116.56 (+2.66%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.60 (n/a)</td><td>407.66 (n/a)</td><td>427.70 (n/a)</td><td>236.60 (n/a)</td><td>113.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (+0.33%)</td><td>0.02 (-0.56%)</td><td>0.02 (-5.54%)</td><td>0.01 (+3.68%)</td><td>0.01 (+3.70%)</td><td>604.70 (-3.56%)</td><td>484.78 (+1.14%)</td><td>543.20 (+5.87%)</td><td>285.90 (-0.35%)</td><td>130.52 (+3.81%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.00 (n/a)</td><td>479.32 (n/a)</td><td>513.10 (n/a)</td><td>286.90 (n/a)</td><td>125.73 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mem_copy</summary>


### test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (-3.54%)</td><td>0.03 (+16.65%)</td><td>0.03 <b>(+55.21%)</b></td><td>0.02 <b>(+48.95%)</b></td><td>0.01 <b>(-22.87%)</b></td><td>465.40 <b>(-32.86%)</b></td><td>339.04 <b>(-22.52%)</b></td><td>307.70 <b>(-35.57%)</b></td><td>201.70 (+3.70%)</td><td>112.83 <b>(-42.04%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>693.20 (n/a)</td><td>437.56 (n/a)</td><td>477.60 (n/a)</td><td>194.50 (n/a)</td><td>194.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.05 <b>(+57.96%)</b></td><td>0.02 (+1.54%)</td><td>0.02 (-7.68%)</td><td>0.00 <b>(-72.72%)</b></td><td>0.02 <b>(+172.67%)</b></td><td>2092.00 <b>(+266.50%)</b></td><td>723.62 <b>(+72.45%)</b></td><td>435.00 (+8.32%)</td><td>178.40 <b>(-36.69%)</b></td><td>774.69 <b>(+601.63%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.80 (n/a)</td><td>419.62 (n/a)</td><td>401.60 (n/a)</td><td>281.80 (n/a)</td><td>110.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 <b>(-23.44%)</b></td><td>0.02 (-4.91%)</td><td>0.02 (+4.19%)</td><td>0.02 (-3.20%)</td><td>0.00 <b>(-47.56%)</b></td><td>475.60 (+3.30%)</td><td>409.28 (+1.79%)</td><td>420.30 (-4.02%)</td><td>326.30 <b>(+30.62%)</b></td><td>64.00 <b>(-27.38%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>460.40 (n/a)</td><td>402.10 (n/a)</td><td>437.90 (n/a)</td><td>249.80 (n/a)</td><td>88.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (+15.57%)</td><td>0.03 (+19.73%)</td><td>0.02 (+14.10%)</td><td>0.02 <b>(+97.52%)</b></td><td>0.01 (-2.75%)</td><td>523.60 <b>(-49.37%)</b></td><td>352.82 <b>(-27.29%)</b></td><td>363.60 (-12.34%)</td><td>203.10 (-13.46%)</td><td>122.04 <b>(-61.42%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1034.20 (n/a)</td><td>485.22 (n/a)</td><td>414.80 (n/a)</td><td>234.70 (n/a)</td><td>316.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (-4.32%)</td><td>0.02 (-5.72%)</td><td>0.02 (-8.37%)</td><td>0.01 (-4.97%)</td><td>0.01 (-8.21%)</td><td>565.80 (+5.25%)</td><td>426.80 (+4.37%)</td><td>446.80 (+9.14%)</td><td>231.90 (+4.51%)</td><td>122.26 (-8.79%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.60 (n/a)</td><td>408.94 (n/a)</td><td>409.40 (n/a)</td><td>221.90 (n/a)</td><td>134.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 <b>(-32.72%)</b></td><td>0.02 (-8.42%)</td><td>0.02 (+9.05%)</td><td>0.02 <b>(+42.56%)</b></td><td>0.00 <b>(-75.95%)</b></td><td>513.20 <b>(-29.85%)</b></td><td>436.74 (-4.17%)</td><td>436.60 (-8.32%)</td><td>383.60 <b>(+48.62%)</b></td><td>49.50 <b>(-73.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>731.60 (n/a)</td><td>455.74 (n/a)</td><td>476.20 (n/a)</td><td>258.10 (n/a)</td><td>189.14 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mha</summary>


### test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0]

_No metrics available._


### test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2]

_No metrics available._


</details>


<details>
<summary>iron/operators/repeat</summary>


### test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count]

_No metrics available._


### test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word]

_No metrics available._


### test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.11 (+8.19%)</td><td>0.08 (-10.19%)</td><td>0.09 (-1.55%)</td><td>0.05 <b>(-33.54%)</b></td><td>0.02 <b>(+240.15%)</b></td><td>452.70 <b>(+50.50%)</b></td><td>319.68 <b>(+20.16%)</b></td><td>266.80 (+1.60%)</td><td>227.20 (-7.57%)</td><td>105.13 <b>(+377.10%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>300.80 (n/a)</td><td>266.04 (n/a)</td><td>262.60 (n/a)</td><td>245.80 (n/a)</td><td>22.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_512-repeat_4-transfer_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.15 (-3.13%)</td><td>0.12 (-11.97%)</td><td>0.14 (-2.54%)</td><td>0.07 <b>(-37.21%)</b></td><td>0.03 <b>(+109.94%)</b></td><td>559.90 <b>(+59.24%)</b></td><td>357.16 <b>(+21.12%)</b></td><td>299.20 (+2.61%)</td><td>265.50 (+3.23%)</td><td>121.92 <b>(+243.11%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>351.60 (n/a)</td><td>294.88 (n/a)</td><td>291.60 (n/a)</td><td>257.20 (n/a)</td><td>35.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_64-repeat_4-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (+0.40%)</td><td>0.01 (-15.43%)</td><td>0.02 (-8.07%)</td><td>0.00 <b>(-70.68%)</b></td><td>0.01 <b>(+109.78%)</b></td><td>1464.90 <b>(+240.99%)</b></td><td>531.74 <b>(+73.78%)</b></td><td>304.80 (+8.82%)</td><td>260.20 (-0.42%)</td><td>523.04 <b>(+644.25%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>429.60 (n/a)</td><td>305.98 (n/a)</td><td>280.10 (n/a)</td><td>261.30 (n/a)</td><td>70.28 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rms_norm</summary>


### test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (-15.23%)</td><td>0.02 <b>(-42.67%)</b></td><td>0.02 <b>(-52.56%)</b></td><td>0.00 <b>(-85.37%)</b></td><td>0.01 <b>(+255.58%)</b></td><td>1866.40 <b>(+583.41%)</b></td><td>691.24 <b>(+182.81%)</b></td><td>522.10 <b>(+110.86%)</b></td><td>249.20 (+17.99%)</td><td>669.45 <b>(+2913.41%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>273.10 (n/a)</td><td>244.42 (n/a)</td><td>247.60 (n/a)</td><td>211.20 (n/a)</td><td>22.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (-17.85%)</td><td>0.03 <b>(-34.71%)</b></td><td>0.02 <b>(-51.70%)</b></td><td>0.02 <b>(-43.88%)</b></td><td>0.01 <b>(+90.06%)</b></td><td>559.00 <b>(+78.20%)</b></td><td>447.62 <b>(+64.28%)</b></td><td>522.70 <b>(+107.09%)</b></td><td>298.90 <b>(+21.75%)</b></td><td>132.05 <b>(+309.56%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>313.70 (n/a)</td><td>272.48 (n/a)</td><td>252.40 (n/a)</td><td>245.50 (n/a)</td><td>32.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (-7.16%)</td><td>0.03 (-0.76%)</td><td>0.03 (+2.17%)</td><td>0.01 (-14.61%)</td><td>0.01 (+1.36%)</td><td>579.20 (+17.10%)</td><td>352.48 (+2.58%)</td><td>283.30 (-2.14%)</td><td>267.10 (+7.70%)</td><td>132.43 <b>(+26.58%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.60 (n/a)</td><td>343.60 (n/a)</td><td>289.50 (n/a)</td><td>248.00 (n/a)</td><td>104.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 <b>(-34.16%)</b></td><td>0.02 <b>(-42.15%)</b></td><td>0.02 <b>(-45.21%)</b></td><td>0.01 <b>(-75.46%)</b></td><td>0.01 (-11.74%)</td><td>1940.40 <b>(+307.48%)</b></td><td>760.20 <b>(+134.08%)</b></td><td>517.60 <b>(+82.51%)</b></td><td>291.90 <b>(+51.87%)</b></td><td>671.51 <b>(+496.20%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.20 (n/a)</td><td>324.76 (n/a)</td><td>283.60 (n/a)</td><td>192.20 (n/a)</td><td>112.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 (+7.96%)</td><td>0.03 (-8.07%)</td><td>0.03 (-9.30%)</td><td>0.01 (-9.99%)</td><td>0.01 <b>(+42.09%)</b></td><td>593.70 (+11.10%)</td><td>375.80 (+17.90%)</td><td>300.70 (+10.27%)</td><td>224.10 (-7.36%)</td><td>174.55 <b>(+41.87%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.40 (n/a)</td><td>318.74 (n/a)</td><td>272.70 (n/a)</td><td>241.90 (n/a)</td><td>123.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.04 <b>(-31.63%)</b></td><td>0.03 <b>(-31.57%)</b></td><td>0.03 <b>(-36.58%)</b></td><td>0.02 (-0.50%)</td><td>0.01 <b>(-43.22%)</b></td><td>529.70 (+0.49%)</td><td>414.38 <b>(+37.55%)</b></td><td>392.80 <b>(+57.69%)</b></td><td>275.90 <b>(+46.29%)</b></td><td>104.89 <b>(-20.28%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.10 (n/a)</td><td>301.26 (n/a)</td><td>249.10 (n/a)</td><td>188.60 (n/a)</td><td>131.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (-18.94%)</td><td>0.02 <b>(-43.31%)</b></td><td>0.02 <b>(-43.23%)</b></td><td>0.00 <b>(-76.30%)</b></td><td>0.01 <b>(+48.21%)</b></td><td>1740.40 <b>(+321.92%)</b></td><td>697.38 <b>(+142.23%)</b></td><td>463.30 <b>(+76.16%)</b></td><td>303.90 <b>(+23.34%)</b></td><td>590.79 <b>(+742.53%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>412.50 (n/a)</td><td>287.90 (n/a)</td><td>263.00 (n/a)</td><td>246.40 (n/a)</td><td>70.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 <b>(-41.95%)</b></td><td>0.02 <b>(-43.83%)</b></td><td>0.02 <b>(-48.71%)</b></td><td>0.02 <b>(-29.07%)</b></td><td>0.00 <b>(-59.33%)</b></td><td>595.40 <b>(+40.99%)</b></td><td>531.12 <b>(+74.44%)</b></td><td>543.40 <b>(+94.98%)</b></td><td>427.60 <b>(+72.28%)</b></td><td>62.18 (-8.55%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>422.30 (n/a)</td><td>304.48 (n/a)</td><td>278.70 (n/a)</td><td>248.20 (n/a)</td><td>68.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 <b>(-20.10%)</b></td><td>0.02 <b>(-43.43%)</b></td><td>0.02 <b>(-49.73%)</b></td><td>0.00 <b>(-80.35%)</b></td><td>0.01 <b>(+73.49%)</b></td><td>2038.50 <b>(+408.99%)</b></td><td>767.24 <b>(+179.12%)</b></td><td>489.40 <b>(+98.94%)</b></td><td>290.60 <b>(+25.15%)</b></td><td>731.87 <b>(+936.99%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>400.50 (n/a)</td><td>274.88 (n/a)</td><td>246.00 (n/a)</td><td>232.20 (n/a)</td><td>70.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (-15.97%)</td><td>0.02 <b>(-38.30%)</b></td><td>0.02 <b>(-44.52%)</b></td><td>0.00 <b>(-68.82%)</b></td><td>0.01 (+2.29%)</td><td>1902.60 <b>(+220.68%)</b></td><td>708.30 <b>(+118.67%)</b></td><td>456.70 <b>(+80.30%)</b></td><td>278.60 (+19.01%)</td><td>672.12 <b>(+340.28%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>593.30 (n/a)</td><td>323.92 (n/a)</td><td>253.30 (n/a)</td><td>234.10 (n/a)</td><td>152.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.03 (-7.45%)</td><td>0.02 <b>(-22.41%)</b></td><td>0.02 <b>(-28.95%)</b></td><td>0.01 (-19.64%)</td><td>0.01 (+11.18%)</td><td>566.90 <b>(+24.43%)</b></td><td>432.46 <b>(+31.84%)</b></td><td>413.10 <b>(+40.70%)</b></td><td>284.10 (+8.02%)</td><td>113.79 <b>(+47.95%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>455.60 (n/a)</td><td>328.02 (n/a)</td><td>293.60 (n/a)</td><td>263.00 (n/a)</td><td>76.91 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rope</summary>


### test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.32 (-10.12%)</td><td>0.26 <b>(-20.79%)</b></td><td>0.29 (-8.85%)</td><td>0.18 <b>(-40.17%)</b></td><td>0.07 <b>(+206.72%)</b></td><td>542.60 <b>(+67.11%)</b></td><td>407.06 <b>(+33.51%)</b></td><td>336.10 (+9.69%)</td><td>306.00 (+11.27%)</td><td>114.30 <b>(+486.10%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.02 (n/a)</td><td>324.70 (n/a)</td><td>304.90 (n/a)</td><td>306.40 (n/a)</td><td>275.00 (n/a)</td><td>19.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.34 (-9.87%)</td><td>0.23 (+10.59%)</td><td>0.21 <b>(+22.90%)</b></td><td>0.18 <b>(+43.96%)</b></td><td>0.06 <b>(-38.25%)</b></td><td>531.90 <b>(-30.53%)</b></td><td>443.12 (-17.72%)</td><td>457.80 (-18.63%)</td><td>290.60 (+10.92%)</td><td>90.54 <b>(-53.16%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.38 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>765.70 (n/a)</td><td>538.52 (n/a)</td><td>562.60 (n/a)</td><td>262.00 (n/a)</td><td>193.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.25 <b>(-37.87%)</b></td><td>0.20 <b>(-30.71%)</b></td><td>0.18 <b>(-21.16%)</b></td><td>0.16 <b>(-20.57%)</b></td><td>0.04 <b>(-59.38%)</b></td><td>617.20 <b>(+25.91%)</b></td><td>512.38 <b>(+36.40%)</b></td><td>534.70 <b>(+26.86%)</b></td><td>397.50 <b>(+60.93%)</b></td><td>97.59 (-15.77%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>490.20 (n/a)</td><td>375.64 (n/a)</td><td>421.50 (n/a)</td><td>247.00 (n/a)</td><td>115.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.32 <b>(+30.60%)</b></td><td>0.22 <b>(+29.05%)</b></td><td>0.24 <b>(+56.00%)</b></td><td>0.14 (+8.46%)</td><td>0.07 <b>(+61.21%)</b></td><td>529.10 (-7.81%)</td><td>372.34 (-18.84%)</td><td>313.70 <b>(-35.89%)</b></td><td>233.60 <b>(-23.43%)</b></td><td>130.68 <b>(+21.06%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>573.90 (n/a)</td><td>458.76 (n/a)</td><td>489.30 (n/a)</td><td>305.10 (n/a)</td><td>107.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.15 <b>(-51.21%)</b></td><td>0.11 <b>(-42.20%)</b></td><td>0.14 <b>(-37.50%)</b></td><td>0.04 (-2.54%)</td><td>0.05 <b>(-53.77%)</b></td><td>1921.40 (+2.61%)</td><td>847.26 <b>(+32.24%)</b></td><td>526.10 <b>(+60.01%)</b></td><td>496.90 <b>(+104.99%)</b></td><td>612.63 (-11.73%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>0.10 (n/a)</td><td>1872.60 (n/a)</td><td>640.72 (n/a)</td><td>328.80 (n/a)</td><td>242.40 (n/a)</td><td>694.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.25 <b>(-24.10%)</b></td><td>0.16 <b>(-37.15%)</b></td><td>0.14 <b>(-42.56%)</b></td><td>0.12 (-19.79%)</td><td>0.05 (-19.69%)</td><td>634.40 <b>(+24.69%)</b></td><td>511.28 <b>(+59.02%)</b></td><td>528.40 <b>(+74.10%)</b></td><td>296.90 <b>(+31.72%)</b></td><td>134.13 <b>(+22.07%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>508.80 (n/a)</td><td>321.52 (n/a)</td><td>303.50 (n/a)</td><td>225.40 (n/a)</td><td>109.88 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/softmax</summary>


### test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.54 (+18.30%)</td><td>0.43 <b>(+25.66%)</b></td><td>0.44 <b>(+42.34%)</b></td><td>0.27 <b>(+22.68%)</b></td><td>0.10 (-1.06%)</td><td>485.60 (-18.48%)</td><td>323.06 <b>(-21.99%)</b></td><td>297.70 <b>(-29.74%)</b></td><td>240.80 (-15.48%)</td><td>95.92 <b>(-25.61%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.46 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>595.70 (n/a)</td><td>414.10 (n/a)</td><td>423.70 (n/a)</td><td>284.90 (n/a)</td><td>128.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.47 (+3.84%)</td><td>0.36 (+12.74%)</td><td>0.43 <b>(+67.59%)</b></td><td>0.07 <b>(-70.67%)</b></td><td>0.16 <b>(+64.58%)</b></td><td>1819.20 <b>(+240.93%)</b></td><td>605.00 <b>(+38.55%)</b></td><td>304.50 <b>(-40.33%)</b></td><td>278.30 (-3.70%)</td><td>678.92 <b>(+464.90%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.10 (n/a)</td><td>533.60 (n/a)</td><td>436.66 (n/a)</td><td>510.30 (n/a)</td><td>289.00 (n/a)</td><td>120.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.47 (+4.83%)</td><td>0.35 <b>(+23.24%)</b></td><td>0.40 <b>(+60.54%)</b></td><td>0.19 (-8.44%)</td><td>0.12 <b>(+30.55%)</b></td><td>703.50 (+9.22%)</td><td>423.90 (-14.15%)</td><td>324.60 <b>(-37.71%)</b></td><td>279.50 (-4.61%)</td><td>183.16 <b>(+40.02%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.45 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>644.10 (n/a)</td><td>493.76 (n/a)</td><td>521.10 (n/a)</td><td>293.00 (n/a)</td><td>130.82 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/strided_copy</summary>


### test_strided_copy[chunked_transfer]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 <b>(-22.70%)</b></td><td>0.01 (-12.29%)</td><td>0.01 (-0.56%)</td><td>0.00 <b>(-38.55%)</b></td><td>0.00 (-9.34%)</td><td>827.70 <b>(+62.74%)</b></td><td>422.34 <b>(+23.59%)</b></td><td>311.90 (+0.55%)</td><td>240.60 <b>(+29.35%)</b></td><td>242.43 <b>(+92.85%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>508.60 (n/a)</td><td>341.72 (n/a)</td><td>310.20 (n/a)</td><td>186.00 (n/a)</td><td>125.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[contiguous]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (-2.92%)</td><td>0.01 (+8.36%)</td><td>0.01 <b>(+20.81%)</b></td><td>0.01 (-5.57%)</td><td>0.00 (+3.16%)</td><td>423.70 (+5.90%)</td><td>299.30 (-7.20%)</td><td>275.00 (-17.22%)</td><td>225.30 (+3.02%)</td><td>83.98 (+7.69%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>400.10 (n/a)</td><td>322.52 (n/a)</td><td>332.20 (n/a)</td><td>218.70 (n/a)</td><td>77.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (-7.18%)</td><td>0.01 (-5.48%)</td><td>0.01 (+0.18%)</td><td>0.01 (-4.07%)</td><td>0.00 <b>(-21.89%)</b></td><td>564.60 (+4.25%)</td><td>407.26 (+2.01%)</td><td>399.00 (-0.18%)</td><td>256.50 (+7.73%)</td><td>114.62 (-16.62%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>541.60 (n/a)</td><td>399.24 (n/a)</td><td>399.70 (n/a)</td><td>238.10 (n/a)</td><td>137.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.53 (-2.38%)</td><td>0.41 (-2.36%)</td><td>0.37 <b>(-28.28%)</b></td><td>0.32 <b>(+66.95%)</b></td><td>0.10 <b>(-39.17%)</b></td><td>413.60 <b>(-40.10%)</b></td><td>333.10 (-9.37%)</td><td>352.40 <b>(+39.45%)</b></td><td>247.10 (+2.40%)</td><td>72.94 <b>(-62.10%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.55 (n/a)</td><td>0.42 (n/a)</td><td>0.52 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>690.50 (n/a)</td><td>367.52 (n/a)</td><td>252.70 (n/a)</td><td>241.30 (n/a)</td><td>192.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.59 (+8.04%)</td><td>0.44 (+10.34%)</td><td>0.55 <b>(+62.43%)</b></td><td>0.18 <b>(-32.48%)</b></td><td>0.18 <b>(+37.28%)</b></td><td>742.10 <b>(+48.12%)</b></td><td>368.46 (+2.76%)</td><td>240.30 <b>(-38.42%)</b></td><td>223.70 (-7.45%)</td><td>221.98 <b>(+95.77%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.55 (n/a)</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>501.00 (n/a)</td><td>358.56 (n/a)</td><td>390.20 (n/a)</td><td>241.70 (n/a)</td><td>113.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_four_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.51 (+7.74%)</td><td>0.38 (-4.67%)</td><td>0.40 (-4.21%)</td><td>0.20 <b>(-32.34%)</b></td><td>0.13 <b>(+71.70%)</b></td><td>651.20 <b>(+47.80%)</b></td><td>391.38 (+14.34%)</td><td>331.00 (+4.42%)</td><td>256.60 (-7.16%)</td><td>162.98 <b>(+133.77%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.48 (n/a)</td><td>0.40 (n/a)</td><td>0.42 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>440.60 (n/a)</td><td>342.30 (n/a)</td><td>317.00 (n/a)</td><td>276.40 (n/a)</td><td>69.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot5_two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.51 (-10.44%)</td><td>0.36 (-18.59%)</td><td>0.29 <b>(-43.75%)</b></td><td>0.22 (-17.11%)</td><td>0.13 (-9.58%)</td><td>590.20 <b>(+20.65%)</b></td><td>409.48 <b>(+23.00%)</b></td><td>452.00 <b>(+77.81%)</b></td><td>259.70 (+11.65%)</td><td>143.74 (+13.53%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.57 (n/a)</td><td>0.44 (n/a)</td><td>0.52 (n/a)</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>489.20 (n/a)</td><td>332.90 (n/a)</td><td>254.20 (n/a)</td><td>232.60 (n/a)</td><td>126.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_slot_last]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.57 (-14.40%)</td><td>0.44 (-6.74%)</td><td>0.44 (-4.65%)</td><td>0.26 (-4.13%)</td><td>0.11 <b>(-20.18%)</b></td><td>511.40 (+4.30%)</td><td>324.46 (+5.58%)</td><td>296.90 (+4.87%)</td><td>232.00 (+16.82%)</td><td>107.91 (-0.86%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.67 (n/a)</td><td>0.47 (n/a)</td><td>0.47 (n/a)</td><td>0.27 (n/a)</td><td>0.14 (n/a)</td><td>490.30 (n/a)</td><td>307.32 (n/a)</td><td>283.10 (n/a)</td><td>198.60 (n/a)</td><td>108.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 (-1.80%)</td><td>0.01 (-7.21%)</td><td>0.01 (-18.65%)</td><td>0.01 (+4.91%)</td><td>0.00 <b>(-26.18%)</b></td><td>428.90 (-4.67%)</td><td>347.12 (+5.33%)</td><td>341.80 <b>(+22.91%)</b></td><td>267.40 (+1.83%)</td><td>63.90 <b>(-26.26%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>449.90 (n/a)</td><td>329.56 (n/a)</td><td>278.10 (n/a)</td><td>262.60 (n/a)</td><td>86.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[two_channels_chunked]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.02 <b>(+34.51%)</b></td><td>0.01 (+19.19%)</td><td>0.01 (-6.28%)</td><td>0.01 (+19.83%)</td><td>0.00 <b>(+64.95%)</b></td><td>435.60 (-16.55%)</td><td>331.34 (-13.20%)</td><td>381.20 (+6.72%)</td><td>218.00 <b>(-25.65%)</b></td><td>101.15 (+1.76%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>522.00 (n/a)</td><td>381.72 (n/a)</td><td>357.20 (n/a)</td><td>293.20 (n/a)</td><td>99.41 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/swiglu_decode</summary>


### test_swiglu_decode[embedding_dim_1024-hidden_dim_3584]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 <b>(-23.53%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-54.12%)</b></td><td>20422.69 (-0.17%)</td><td>16705.37 (+15.21%)</td><td>17326.83 (-8.34%)</td><td>10441.56 <b>(+61.89%)</b></td><td>3895.14 <b>(-42.74%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20457.51 (n/a)</td><td>14499.91 (n/a)</td><td>18904.04 (n/a)</td><td>6449.61 (n/a)</td><td>6802.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_decode[embedding_dim_2048-hidden_dim_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.00 <b>(+57.14%)</b></td><td>0.00 <b>(+68.00%)</b></td><td>0.00 <b>(+80.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+120.61%)</b></td><td>18660.83 (-8.56%)</td><td>10664.50 <b>(-37.43%)</b></td><td>9421.47 <b>(-47.99%)</b></td><td>7425.83 <b>(-39.23%)</b></td><td>4582.01 <b>(+46.57%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20407.99 (n/a)</td><td>17045.09 (n/a)</td><td>18113.54 (n/a)</td><td>12219.46 (n/a)</td><td>3126.14 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/swiglu_prefill</summary>


### test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.15 (-2.90%)</td><td>0.13 (+13.84%)</td><td>0.13 (+7.92%)</td><td>0.10 <b>(+40.22%)</b></td><td>0.02 <b>(-51.52%)</b></td><td>20459.71 <b>(-28.72%)</b></td><td>16753.40 (-17.98%)</td><td>16376.48 (-7.30%)</td><td>14231.58 (+3.01%)</td><td>2345.44 <b>(-65.00%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28704.72 (n/a)</td><td>20425.51 (n/a)</td><td>17665.47 (n/a)</td><td>13816.18 (n/a)</td><td>6701.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>0.14 (-5.55%)</td><td>0.10 (-1.49%)</td><td>0.08 (-8.77%)</td><td>0.07 (+0.97%)</td><td>0.04 (+5.35%)</td><td>28732.28 (-0.98%)</td><td>22647.72 (+2.81%)</td><td>26903.25 (+9.70%)</td><td>14678.08 (+5.87%)</td><td>7139.42 (+9.55%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29016.35 (n/a)</td><td>22027.87 (n/a)</td><td>24523.77 (n/a)</td><td>13863.78 (n/a)</td><td>6517.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.09 <b>(-41.54%)</b></td><td>0.08 <b>(-26.45%)</b></td><td>0.08 (-5.72%)</td><td>0.07 (+0.28%)</td><td>0.01 <b>(-78.49%)</b></td><td>29471.13 (-0.19%)</td><td>26636.50 <b>(+22.62%)</b></td><td>26497.60 (+5.97%)</td><td>22637.65 <b>(+70.99%)</b></td><td>2927.42 <b>(-61.16%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>29528.24 (n/a)</td><td>21722.14 (n/a)</td><td>25004.94 (n/a)</td><td>13239.53 (n/a)</td><td>7537.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_weight_layout_reaches_both_gemms[b_col_maj_False]

_No metrics available._


### test_weight_layout_reaches_both_gemms[b_col_maj_True]

_No metrics available._


</details>


<details>
<summary>iron/operators/transpose</summary>


### test_a_dimension_that_floors_to_zero_is_refused_by_name[M_2048-N_128-aie_columns_8-channels_1-m_256-n_32-bad_num_aie_columns]

_No metrics available._


### test_a_dimension_that_floors_to_zero_is_refused_by_name[M_256-N_2048-aie_columns_1-channels_2-m_256-n_32-bad_num_channels]

_No metrics available._


### test_a_tiling_that_fits_is_still_accepted[aie_columns_1]

_No metrics available._


### test_a_tiling_that_fits_is_still_accepted[aie_columns_2]

_No metrics available._


### test_a_tiling_that_fits_is_still_accepted[aie_columns_4]

_No metrics available._


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.79 (+18.03%)</td><td>1.17 (-12.65%)</td><td>1.38 (-2.55%)</td><td>0.28 <b>(-69.88%)</b></td><td>0.60 <b>(+152.81%)</b></td><td>1884.80 <b>(+232.01%)</b></td><td>699.46 <b>(+73.61%)</b></td><td>380.20 (+2.62%)</td><td>293.40 (-15.28%)</td><td>673.32 <b>(+626.49%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.51 (n/a)</td><td>1.35 (n/a)</td><td>1.41 (n/a)</td><td>0.92 (n/a)</td><td>0.24 (n/a)</td><td>567.70 (n/a)</td><td>402.88 (n/a)</td><td>370.50 (n/a)</td><td>346.30 (n/a)</td><td>92.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>2.79 (+19.69%)</td><td>1.57 (-4.04%)</td><td>1.52 <b>(-24.17%)</b></td><td>0.55 <b>(+88.07%)</b></td><td>0.88 (+7.48%)</td><td>1897.00 <b>(-46.83%)</b></td><td>914.14 <b>(-20.72%)</b></td><td>690.80 <b>(+31.86%)</b></td><td>375.80 (-16.47%)</td><td>611.53 <b>(-54.84%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>2.33 (n/a)</td><td>1.64 (n/a)</td><td>2.00 (n/a)</td><td>0.29 (n/a)</td><td>0.82 (n/a)</td><td>3567.70 (n/a)</td><td>1153.10 (n/a)</td><td>523.90 (n/a)</td><td>449.90 (n/a)</td><td>1354.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>1.58 (-2.67%)</td><td>1.21 (+5.65%)</td><td>1.29 <b>(+41.89%)</b></td><td>0.66 <b>(-20.05%)</b></td><td>0.38 (-2.53%)</td><td>792.90 <b>(+25.08%)</b></td><td>479.12 (-3.80%)</td><td>406.80 <b>(-29.52%)</b></td><td>331.10 (+2.76%)</td><td>189.18 <b>(+26.62%)</b></td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>1.63 (n/a)</td><td>1.14 (n/a)</td><td>0.91 (n/a)</td><td>0.83 (n/a)</td><td>0.38 (n/a)</td><td>633.90 (n/a)</td><td>498.02 (n/a)</td><td>577.20 (n/a)</td><td>322.20 (n/a)</td><td>149.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:27:17</td><td>1.65 (-15.53%)</td><td>1.18 (-0.48%)</td><td>1.05 (+11.84%)</td><td>0.77 (+14.99%)</td><td>0.37 <b>(-38.24%)</b></td><td>683.90 (-13.03%)</td><td>481.10 (-10.87%)</td><td>497.80 (-10.58%)</td><td>318.60 (+18.35%)</td><td>148.93 <b>(-39.66%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.95 (n/a)</td><td>1.18 (n/a)</td><td>0.94 (n/a)</td><td>0.67 (n/a)</td><td>0.60 (n/a)</td><td>786.40 (n/a)</td><td>539.80 (n/a)</td><td>556.70 (n/a)</td><td>269.20 (n/a)</td><td>246.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-25 20:01:37</td><td>1.75 (-15.44%)</td><td>1.32 (-0.50%)</td><td>1.36 <b>(+22.47%)</b></td><td>0.77 (-19.20%)</td><td>0.36 <b>(-21.75%)</b></td><td>678.10 <b>(+23.76%)</b></td><td>430.02 (-0.09%)</td><td>385.10 (-18.34%)</td><td>300.10 (+18.29%)</td><td>146.96 (+19.46%)</td>
</tr>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:49</td><td>2.07 (n/a)</td><td>1.32 (n/a)</td><td>1.11 (n/a)</td><td>0.96 (n/a)</td><td>0.46 (n/a)</td><td>547.90 (n/a)</td><td>430.40 (n/a)</td><td>471.60 (n/a)</td><td>253.70 (n/a)</td><td>123.02 (n/a)</td>
</tr>
</tbody>
</table>


</details>
