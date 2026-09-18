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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.07 (+9.42%)</td><td>0.04 (-18.08%)</td><td>0.05 (-5.80%)</td><td>0.01 <b>(-72.90%)</b></td><td>0.02 <b>(+204.71%)</b></td><td>1061.90 <b>(+268.97%)</b></td><td>439.84 <b>(+76.76%)</b></td><td>256.40 (+6.17%)</td><td>183.90 (-8.64%)</td><td>363.80 <b>(+966.94%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>287.80 (n/a)</td><td>248.84 (n/a)</td><td>241.50 (n/a)</td><td>201.30 (n/a)</td><td>34.10 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.06 (+7.58%)</td><td>0.04 (-14.18%)</td><td>0.03 <b>(-32.97%)</b></td><td>0.02 <b>(-23.99%)</b></td><td>0.01 <b>(+30.16%)</b></td><td>548.10 <b>(+31.57%)</b></td><td>367.76 <b>(+22.71%)</b></td><td>385.50 <b>(+49.19%)</b></td><td>212.80 (-7.07%)</td><td>129.85 <b>(+57.35%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>416.60 (n/a)</td><td>299.70 (n/a)</td><td>258.40 (n/a)</td><td>229.00 (n/a)</td><td>82.52 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.05 (+0.12%)</td><td>0.04 (+9.81%)</td><td>0.04 (+14.51%)</td><td>0.02 (+8.17%)</td><td>0.01 (+13.47%)</td><td>534.80 (-7.55%)</td><td>336.10 (-7.98%)</td><td>297.00 (-12.67%)</td><td>236.00 (-0.13%)</td><td>124.75 (-2.59%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>578.50 (n/a)</td><td>365.26 (n/a)</td><td>340.10 (n/a)</td><td>236.30 (n/a)</td><td>128.07 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (-7.81%)</td><td>0.02 (+9.04%)</td><td>0.02 (+0.13%)</td><td>0.01 <b>(+29.10%)</b></td><td>0.00 <b>(-43.94%)</b></td><td>381.50 <b>(-22.54%)</b></td><td>290.02 (-15.28%)</td><td>290.20 (-0.14%)</td><td>230.90 (+8.45%)</td><td>57.39 <b>(-54.60%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>492.50 (n/a)</td><td>342.32 (n/a)</td><td>290.60 (n/a)</td><td>212.90 (n/a)</td><td>126.42 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 <b>(+22.62%)</b></td><td>0.02 <b>(+34.20%)</b></td><td>0.01 <b>(+30.44%)</b></td><td>0.01 <b>(+47.24%)</b></td><td>0.01 (+19.14%)</td><td>446.50 <b>(-32.08%)</b></td><td>338.94 <b>(-26.38%)</b></td><td>351.10 <b>(-23.32%)</b></td><td>217.40 (-18.45%)</td><td>96.92 <b>(-30.78%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>657.40 (n/a)</td><td>460.36 (n/a)</td><td>457.90 (n/a)</td><td>266.60 (n/a)</td><td>140.01 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (-7.91%)</td><td>0.01 (-2.94%)</td><td>0.02 <b>(+43.27%)</b></td><td>0.00 <b>(-68.49%)</b></td><td>0.01 (+7.79%)</td><td>1875.00 <b>(+217.37%)</b></td><td>623.52 <b>(+53.13%)</b></td><td>293.60 <b>(-30.21%)</b></td><td>224.70 (+8.55%)</td><td>703.59 <b>(+308.99%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.80 (n/a)</td><td>407.18 (n/a)</td><td>420.70 (n/a)</td><td>207.00 (n/a)</td><td>172.03 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (-2.15%)</td><td>0.01 (-6.01%)</td><td>0.01 <b>(-28.23%)</b></td><td>0.01 (-11.40%)</td><td>0.01 (+9.82%)</td><td>635.10 (+12.87%)</td><td>410.76 (+9.33%)</td><td>426.90 <b>(+39.33%)</b></td><td>236.90 (+2.20%)</td><td>166.37 (+15.64%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.70 (n/a)</td><td>375.70 (n/a)</td><td>306.40 (n/a)</td><td>231.80 (n/a)</td><td>143.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (+11.65%)</td><td>0.01 (+2.90%)</td><td>0.01 (+0.05%)</td><td>0.01 (+14.54%)</td><td>0.01 (+3.42%)</td><td>592.10 (-12.71%)</td><td>417.10 (-4.19%)</td><td>461.80 (-0.04%)</td><td>215.60 (-10.43%)</td><td>164.98 (-12.52%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>678.30 (n/a)</td><td>435.34 (n/a)</td><td>462.00 (n/a)</td><td>240.70 (n/a)</td><td>188.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (-7.65%)</td><td>0.01 (-3.98%)</td><td>0.01 (-10.25%)</td><td>0.01 (+3.69%)</td><td>0.00 (-16.86%)</td><td>558.30 (-3.54%)</td><td>449.72 (+2.37%)</td><td>473.90 (+11.43%)</td><td>297.00 (+8.28%)</td><td>98.13 (-14.19%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.80 (n/a)</td><td>439.32 (n/a)</td><td>425.30 (n/a)</td><td>274.30 (n/a)</td><td>114.36 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>466.50 (n/a)</td><td>328.74 (n/a)</td><td>294.30 (n/a)</td><td>210.60 (n/a)</td><td>115.10 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>878.40 (n/a)</td><td>516.62 (n/a)</td><td>604.40 (n/a)</td><td>213.00 (n/a)</td><td>271.99 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>625.60 (n/a)</td><td>439.08 (n/a)</td><td>356.10 (n/a)</td><td>352.60 (n/a)</td><td>123.05 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.70 (n/a)</td><td>308.86 (n/a)</td><td>271.50 (n/a)</td><td>222.00 (n/a)</td><td>121.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>455.70 (n/a)</td><td>333.06 (n/a)</td><td>294.30 (n/a)</td><td>239.50 (n/a)</td><td>92.06 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.90 (n/a)</td><td>449.90 (n/a)</td><td>466.70 (n/a)</td><td>260.90 (n/a)</td><td>121.67 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.89 (-4.28%)</td><td>0.69 <b>(+22.87%)</b></td><td>0.67 (+3.56%)</td><td>0.61 <b>(+365.16%)</b></td><td>0.11 <b>(-68.62%)</b></td><td>750.20 <b>(-78.50%)</b></td><td>672.56 <b>(-52.60%)</b></td><td>680.00 (-3.44%)</td><td>514.90 (+4.48%)</td><td>94.16 <b>(-92.70%)</b></td><td>65.17 (-4.28%)</td><td>50.82 <b>(+22.87%)</b></td><td>49.34 (+3.56%)</td><td>44.73 <b>(+365.16%)</b></td><td>8.32 <b>(-68.62%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.93 (n/a)</td><td>0.57 (n/a)</td><td>0.65 (n/a)</td><td>0.13 (n/a)</td><td>0.36 (n/a)</td><td>3489.50 (n/a)</td><td>1419.00 (n/a)</td><td>704.20 (n/a)</td><td>492.80 (n/a)</td><td>1290.71 (n/a)</td><td>68.09 (n/a)</td><td>41.36 (n/a)</td><td>47.65 (n/a)</td><td>9.62 (n/a)</td><td>26.50 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.60 <b>(+41.17%)</b></td><td>1.10 <b>(+54.09%)</b></td><td>0.93 <b>(+45.10%)</b></td><td>0.68 <b>(+91.65%)</b></td><td>0.42 <b>(+41.77%)</b></td><td>968.20 <b>(-47.82%)</b></td><td>664.54 <b>(-37.50%)</b></td><td>705.20 <b>(-31.09%)</b></td><td>409.10 <b>(-29.16%)</b></td><td>238.86 <b>(-51.04%)</b></td><td>164.04 <b>(+41.17%)</b></td><td>113.00 <b>(+54.09%)</b></td><td>95.16 <b>(+45.10%)</b></td><td>69.32 <b>(+91.65%)</b></td><td>42.59 <b>(+41.77%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.13 (n/a)</td><td>0.72 (n/a)</td><td>0.64 (n/a)</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>1855.50 (n/a)</td><td>1063.34 (n/a)</td><td>1023.30 (n/a)</td><td>577.50 (n/a)</td><td>487.87 (n/a)</td><td>116.20 (n/a)</td><td>73.33 (n/a)</td><td>65.58 (n/a)</td><td>36.17 (n/a)</td><td>30.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.49 (-15.99%)</td><td>1.02 (-6.36%)</td><td>0.98 (-1.30%)</td><td>0.71 (-3.73%)</td><td>0.29 <b>(-27.66%)</b></td><td>1062.30 (+3.87%)</td><td>780.60 (+4.00%)</td><td>771.80 (+1.31%)</td><td>505.10 (+19.04%)</td><td>198.99 (-7.05%)</td><td>166.08 (-15.99%)</td><td>113.77 (-6.36%)</td><td>108.69 (-1.30%)</td><td>78.97 (-3.73%)</td><td>32.05 <b>(-27.66%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.78 (n/a)</td><td>1.09 (n/a)</td><td>0.99 (n/a)</td><td>0.74 (n/a)</td><td>0.40 (n/a)</td><td>1022.70 (n/a)</td><td>750.60 (n/a)</td><td>761.80 (n/a)</td><td>424.30 (n/a)</td><td>214.10 (n/a)</td><td>197.70 (n/a)</td><td>121.49 (n/a)</td><td>110.12 (n/a)</td><td>82.03 (n/a)</td><td>44.30 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.50 (-5.38%)</td><td>1.01 <b>(+37.82%)</b></td><td>1.06 <b>(+232.45%)</b></td><td>0.53 <b>(+81.86%)</b></td><td>0.45 <b>(-26.77%)</b></td><td>1967.70 <b>(-45.01%)</b></td><td>1239.06 <b>(-48.08%)</b></td><td>993.00 <b>(-69.92%)</b></td><td>700.70 (+5.69%)</td><td>595.08 <b>(-59.76%)</b></td><td>191.54 (-5.38%)</td><td>129.81 <b>(+37.82%)</b></td><td>135.17 <b>(+232.45%)</b></td><td>68.21 <b>(+81.86%)</b></td><td>57.04 <b>(-26.77%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.58 (n/a)</td><td>0.74 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.61 (n/a)</td><td>3578.40 (n/a)</td><td>2386.58 (n/a)</td><td>3301.20 (n/a)</td><td>663.00 (n/a)</td><td>1478.68 (n/a)</td><td>202.43 (n/a)</td><td>94.18 (n/a)</td><td>40.66 (n/a)</td><td>37.51 (n/a)</td><td>77.89 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>2.18 <b>(+30.31%)</b></td><td>1.75 <b>(+32.00%)</b></td><td>1.75 <b>(+39.14%)</b></td><td>1.29 <b>(+43.43%)</b></td><td>0.33 (-2.47%)</td><td>812.40 <b>(-30.28%)</b></td><td>615.86 <b>(-26.10%)</b></td><td>599.10 <b>(-28.14%)</b></td><td>481.00 <b>(-23.27%)</b></td><td>124.37 <b>(-44.45%)</b></td><td>279.01 <b>(+30.31%)</b></td><td>224.60 <b>(+32.00%)</b></td><td>224.02 <b>(+39.14%)</b></td><td>165.21 <b>(+43.43%)</b></td><td>42.00 (-2.47%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.67 (n/a)</td><td>1.33 (n/a)</td><td>1.26 (n/a)</td><td>0.90 (n/a)</td><td>0.34 (n/a)</td><td>1165.30 (n/a)</td><td>833.36 (n/a)</td><td>833.70 (n/a)</td><td>626.90 (n/a)</td><td>223.89 (n/a)</td><td>214.11 (n/a)</td><td>170.16 (n/a)</td><td>161.00 (n/a)</td><td>115.18 (n/a)</td><td>43.07 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>2.14 <b>(+38.64%)</b></td><td>1.43 <b>(+30.01%)</b></td><td>1.65 <b>(+29.74%)</b></td><td>0.32 (+4.17%)</td><td>0.68 <b>(+40.01%)</b></td><td>3302.10 (-4.00%)</td><td>1164.58 (-13.79%)</td><td>636.90 <b>(-22.91%)</b></td><td>489.60 <b>(-27.86%)</b></td><td>1199.15 (+1.97%)</td><td>274.15 <b>(+38.64%)</b></td><td>183.06 <b>(+30.01%)</b></td><td>210.75 <b>(+29.74%)</b></td><td>40.65 (+4.17%)</td><td>87.40 <b>(+40.01%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.54 (n/a)</td><td>1.10 (n/a)</td><td>1.27 (n/a)</td><td>0.30 (n/a)</td><td>0.49 (n/a)</td><td>3439.70 (n/a)</td><td>1350.84 (n/a)</td><td>826.20 (n/a)</td><td>678.70 (n/a)</td><td>1176.02 (n/a)</td><td>197.75 (n/a)</td><td>140.81 (n/a)</td><td>162.44 (n/a)</td><td>39.02 (n/a)</td><td>62.42 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.54 (-13.49%)</td><td>1.05 <b>(-27.85%)</b></td><td>1.23 <b>(-20.30%)</b></td><td>0.47 <b>(-48.23%)</b></td><td>0.51 <b>(+53.25%)</b></td><td>2246.40 <b>(+93.17%)</b></td><td>1282.22 <b>(+68.53%)</b></td><td>855.30 <b>(+25.48%)</b></td><td>681.30 (+15.59%)</td><td>743.57 <b>(+222.91%)</b></td><td>197.00 (-13.49%)</td><td>134.67 <b>(-27.85%)</b></td><td>156.93 <b>(-20.30%)</b></td><td>59.75 <b>(-48.23%)</b></td><td>65.63 <b>(+53.25%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.78 (n/a)</td><td>1.46 (n/a)</td><td>1.54 (n/a)</td><td>0.90 (n/a)</td><td>0.33 (n/a)</td><td>1162.90 (n/a)</td><td>760.84 (n/a)</td><td>681.60 (n/a)</td><td>589.40 (n/a)</td><td>230.27 (n/a)</td><td>227.72 (n/a)</td><td>186.64 (n/a)</td><td>196.91 (n/a)</td><td>115.41 (n/a)</td><td>42.83 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.83 (+5.53%)</td><td>0.65 <b>(+28.51%)</b></td><td>0.62 <b>(+32.29%)</b></td><td>0.44 <b>(+50.28%)</b></td><td>0.14 (-19.77%)</td><td>814.10 <b>(-33.46%)</b></td><td>583.02 <b>(-26.20%)</b></td><td>579.60 <b>(-24.41%)</b></td><td>436.10 (-5.24%)</td><td>142.71 <b>(-48.09%)</b></td><td>38.47 (+5.53%)</td><td>30.04 <b>(+28.51%)</b></td><td>28.94 <b>(+32.29%)</b></td><td>20.61 <b>(+50.28%)</b></td><td>6.60 (-19.77%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.78 (n/a)</td><td>0.50 (n/a)</td><td>0.47 (n/a)</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>1223.40 (n/a)</td><td>790.04 (n/a)</td><td>766.80 (n/a)</td><td>460.20 (n/a)</td><td>274.89 (n/a)</td><td>36.46 (n/a)</td><td>23.37 (n/a)</td><td>21.88 (n/a)</td><td>13.71 (n/a)</td><td>8.22 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>3.45 (-10.12%)</td><td>2.84 (+9.24%)</td><td>3.37 (+8.11%)</td><td>0.69 <b>(-40.31%)</b></td><td>1.20 (-8.75%)</td><td>3796.40 <b>(+67.54%)</b></td><td>1379.74 (+3.68%)</td><td>778.90 (-7.49%)</td><td>759.40 (+11.25%)</td><td>1351.00 <b>(+67.89%)</b></td><td>706.92 (-10.12%)</td><td>582.18 (+9.24%)</td><td>689.28 (+8.11%)</td><td>141.41 <b>(-40.31%)</b></td><td>246.61 (-8.75%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>3.84 (n/a)</td><td>2.60 (n/a)</td><td>3.11 (n/a)</td><td>1.16 (n/a)</td><td>1.32 (n/a)</td><td>2266.00 (n/a)</td><td>1330.76 (n/a)</td><td>842.00 (n/a)</td><td>682.60 (n/a)</td><td>804.71 (n/a)</td><td>786.53 (n/a)</td><td>532.96 (n/a)</td><td>637.59 (n/a)</td><td>236.92 (n/a)</td><td>270.26 (n/a)</td>
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


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn16-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn32-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma16-default]

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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.00 (n/a)</td><td>371.56 (n/a)</td><td>437.10 (n/a)</td><td>230.10 (n/a)</td><td>130.29 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.50 (n/a)</td><td>371.30 (n/a)</td><td>290.30 (n/a)</td><td>208.30 (n/a)</td><td>169.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.70 (n/a)</td><td>423.08 (n/a)</td><td>470.10 (n/a)</td><td>215.70 (n/a)</td><td>119.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2396.10 (n/a)</td><td>840.22 (n/a)</td><td>492.20 (n/a)</td><td>296.30 (n/a)</td><td>879.97 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2129.60 (n/a)</td><td>873.38 (n/a)</td><td>472.80 (n/a)</td><td>272.20 (n/a)</td><td>755.97 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>665.10 (n/a)</td><td>503.32 (n/a)</td><td>515.20 (n/a)</td><td>363.30 (n/a)</td><td>111.69 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.56 (-6.41%)</td><td>0.44 <b>(+45.37%)</b></td><td>0.46 <b>(+117.92%)</b></td><td>0.31 <b>(+179.26%)</b></td><td>0.10 <b>(-50.58%)</b></td><td>703.00 <b>(-64.19%)</b></td><td>528.28 <b>(-49.54%)</b></td><td>484.70 <b>(-54.11%)</b></td><td>392.30 (+6.84%)</td><td>126.67 <b>(-80.17%)</b></td><td>24.06 (-6.41%)</td><td>18.67 <b>(+45.37%)</b></td><td>19.47 <b>(+117.92%)</b></td><td>13.42 <b>(+179.26%)</b></td><td>4.28 <b>(-50.58%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.60 (n/a)</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.20 (n/a)</td><td>1963.30 (n/a)</td><td>1047.00 (n/a)</td><td>1056.20 (n/a)</td><td>367.20 (n/a)</td><td>638.89 (n/a)</td><td>25.70 (n/a)</td><td>12.85 (n/a)</td><td>8.94 (n/a)</td><td>4.81 (n/a)</td><td>8.66 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.61 (+13.30%)</td><td>0.54 <b>(+20.90%)</b></td><td>0.56 (+18.68%)</td><td>0.44 <b>(+29.39%)</b></td><td>0.07 (-14.83%)</td><td>500.80 <b>(-22.70%)</b></td><td>413.30 (-18.35%)</td><td>397.90 (-15.75%)</td><td>361.50 (-11.74%)</td><td>54.70 <b>(-41.91%)</b></td><td>26.11 (+13.30%)</td><td>23.13 <b>(+20.90%)</b></td><td>23.72 (+18.68%)</td><td>18.84 <b>(+29.39%)</b></td><td>2.82 (-14.83%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.54 (n/a)</td><td>0.45 (n/a)</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>647.90 (n/a)</td><td>506.20 (n/a)</td><td>472.30 (n/a)</td><td>409.60 (n/a)</td><td>94.16 (n/a)</td><td>23.04 (n/a)</td><td>19.13 (n/a)</td><td>19.98 (n/a)</td><td>14.56 (n/a)</td><td>3.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.31 (-1.19%)</td><td>0.30 (+0.01%)</td><td>0.31 (-0.10%)</td><td>0.30 (+1.59%)</td><td>0.00 <b>(-61.75%)</b></td><td>83420.40 (-1.56%)</td><td>82579.82 (-0.05%)</td><td>82494.80 (+0.10%)</td><td>81799.20 (+1.21%)</td><td>685.16 <b>(-61.84%)</b></td><td>210.02 (-1.19%)</td><td>208.05 (+0.01%)</td><td>208.25 (-0.10%)</td><td>205.94 (+1.59%)</td><td>1.72 <b>(-61.75%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84744.30 (n/a)</td><td>82618.42 (n/a)</td><td>82415.00 (n/a)</td><td>80823.50 (n/a)</td><td>1795.39 (n/a)</td><td>212.56 (n/a)</td><td>208.02 (n/a)</td><td>208.46 (n/a)</td><td>202.73 (n/a)</td><td>4.51 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.15 (-0.24%)</td><td>1.12 (-2.11%)</td><td>1.14 (-0.79%)</td><td>1.07 (-6.59%)</td><td>0.03 <b>(+2320.20%)</b></td><td>23527.20 (+7.06%)</td><td>22422.14 (+2.23%)</td><td>22105.30 (+0.79%)</td><td>21963.20 (+0.24%)</td><td>658.54 <b>(+2499.52%)</b></td><td>782.21 (-0.24%)</td><td>766.72 (-2.11%)</td><td>777.18 (-0.79%)</td><td>730.21 (-6.59%)</td><td>21.89 <b>(+2320.22%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.15 (n/a)</td><td>1.15 (n/a)</td><td>1.15 (n/a)</td><td>1.15 (n/a)</td><td>0.00 (n/a)</td><td>21975.80 (n/a)</td><td>21934.02 (n/a)</td><td>21931.00 (n/a)</td><td>21910.60 (n/a)</td><td>25.33 (n/a)</td><td>784.09 (n/a)</td><td>783.25 (n/a)</td><td>783.36 (n/a)</td><td>781.76 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>4.10 (+1.51%)</td><td>2.37 (-17.22%)</td><td>1.95 <b>(-30.20%)</b></td><td>1.77 (+0.87%)</td><td>0.98 (-0.96%)</td><td>4561.10 (-0.86%)</td><td>3741.14 (+19.84%)</td><td>4129.40 <b>(+43.27%)</b></td><td>1964.10 (-1.48%)</td><td>1021.61 (-8.48%)</td><td>1076.29 (+1.51%)</td><td>620.60 (-17.22%)</td><td>511.92 <b>(-30.20%)</b></td><td>463.47 (+0.87%)</td><td>256.29 (-0.96%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>4.04 (n/a)</td><td>2.86 (n/a)</td><td>2.80 (n/a)</td><td>1.75 (n/a)</td><td>0.99 (n/a)</td><td>4600.60 (n/a)</td><td>3121.74 (n/a)</td><td>2882.30 (n/a)</td><td>1993.70 (n/a)</td><td>1116.27 (n/a)</td><td>1060.28 (n/a)</td><td>749.66 (n/a)</td><td>733.43 (n/a)</td><td>459.49 (n/a)</td><td>258.76 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.32 (-0.37%)</td><td>0.24 (+11.85%)</td><td>0.22 (+11.46%)</td><td>0.20 (+14.69%)</td><td>0.05 (-19.43%)</td><td>6221.40 (-12.81%)</td><td>5370.78 (-12.25%)</td><td>5756.20 (-10.28%)</td><td>3949.80 (+0.37%)</td><td>921.92 <b>(-26.99%)</b></td><td>16.99 (-0.37%)</td><td>12.84 (+11.85%)</td><td>11.66 (+11.46%)</td><td>10.79 (+14.69%)</td><td>2.54 (-19.43%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>7135.60 (n/a)</td><td>6120.86 (n/a)</td><td>6416.00 (n/a)</td><td>3935.20 (n/a)</td><td>1262.78 (n/a)</td><td>17.05 (n/a)</td><td>11.48 (n/a)</td><td>10.46 (n/a)</td><td>9.40 (n/a)</td><td>3.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>3.91 (n/a)</td><td>3.63 (n/a)</td><td>3.56 (n/a)</td><td>3.36 (n/a)</td><td>0.21 (n/a)</td><td>3.90 (n/a)</td><td>3.63 (n/a)</td><td>3.55 (n/a)</td><td>3.36 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>7.36 (-1.48%)</td><td>6.40 (-8.72%)</td><td>6.12 (-15.95%)</td><td>5.66 (-5.71%)</td><td>0.70 (+18.40%)</td><td>7.35 (-1.48%)</td><td>6.40 (-8.72%)</td><td>6.12 (-15.95%)</td><td>5.65 (-5.71%)</td><td>0.70 (+18.40%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>7.47 (n/a)</td><td>7.01 (n/a)</td><td>7.29 (n/a)</td><td>6.00 (n/a)</td><td>0.59 (n/a)</td><td>7.46 (n/a)</td><td>7.01 (n/a)</td><td>7.28 (n/a)</td><td>6.00 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>14.04 (-0.49%)</td><td>9.73 (-4.65%)</td><td>8.66 (-9.00%)</td><td>7.60 (-8.61%)</td><td>2.52 (+5.36%)</td><td>14.03 (-0.49%)</td><td>9.72 (-4.65%)</td><td>8.66 (-9.00%)</td><td>7.60 (-8.61%)</td><td>2.52 (+5.36%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>14.10 (n/a)</td><td>10.20 (n/a)</td><td>9.52 (n/a)</td><td>8.32 (n/a)</td><td>2.39 (n/a)</td><td>14.10 (n/a)</td><td>10.20 (n/a)</td><td>9.51 (n/a)</td><td>8.31 (n/a)</td><td>2.39 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>3.74 (n/a)</td><td>3.66 (n/a)</td><td>3.66 (n/a)</td><td>3.53 (n/a)</td><td>0.08 (n/a)</td><td>3.73 (n/a)</td><td>3.66 (n/a)</td><td>3.66 (n/a)</td><td>3.53 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>7.56 (+10.47%)</td><td>6.57 (+14.86%)</td><td>6.72 (+17.31%)</td><td>5.87 <b>(+23.45%)</b></td><td>0.72 (-15.37%)</td><td>7.56 (+10.47%)</td><td>6.57 (+14.86%)</td><td>6.71 (+17.31%)</td><td>5.87 <b>(+23.45%)</b></td><td>0.71 (-15.37%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>6.85 (n/a)</td><td>5.72 (n/a)</td><td>5.73 (n/a)</td><td>4.75 (n/a)</td><td>0.85 (n/a)</td><td>6.84 (n/a)</td><td>5.72 (n/a)</td><td>5.72 (n/a)</td><td>4.75 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>13.01 (-6.45%)</td><td>10.06 (+4.42%)</td><td>9.59 (+19.07%)</td><td>8.62 <b>(+21.70%)</b></td><td>1.73 <b>(-40.99%)</b></td><td>13.00 (-6.45%)</td><td>10.05 (+4.42%)</td><td>9.59 (+19.07%)</td><td>8.62 <b>(+21.70%)</b></td><td>1.73 <b>(-40.99%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>13.90 (n/a)</td><td>9.63 (n/a)</td><td>8.06 (n/a)</td><td>7.09 (n/a)</td><td>2.93 (n/a)</td><td>13.89 (n/a)</td><td>9.63 (n/a)</td><td>8.05 (n/a)</td><td>7.08 (n/a)</td><td>2.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>3.10 (+6.90%)</td><td>2.53 <b>(+53.23%)</b></td><td>2.87 <b>(+177.60%)</b></td><td>1.77 <b>(+72.54%)</b></td><td>0.64 <b>(-27.67%)</b></td><td>3.09 (+6.90%)</td><td>2.52 <b>(+53.23%)</b></td><td>2.86 <b>(+177.60%)</b></td><td>1.76 <b>(+72.54%)</b></td><td>0.63 <b>(-27.67%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>2.90 (n/a)</td><td>1.65 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>0.88 (n/a)</td><td>2.89 (n/a)</td><td>1.65 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.64 (+11.05%)</td><td>0.38 <b>(+24.83%)</b></td><td>0.45 <b>(+35.18%)</b></td><td>0.14 <b>(+73.69%)</b></td><td>0.23 (+14.65%)</td><td>0.63 (+11.05%)</td><td>0.37 <b>(+24.83%)</b></td><td>0.44 <b>(+35.18%)</b></td><td>0.14 <b>(+73.69%)</b></td><td>0.22 (+14.65%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.58 (n/a)</td><td>0.30 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.57 (n/a)</td><td>0.30 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.81 <b>(+66.05%)</b></td><td>0.48 <b>(+47.74%)</b></td><td>0.63 <b>(+45.61%)</b></td><td>0.08 (-8.33%)</td><td>0.37 <b>(+90.10%)</b></td><td>0.80 <b>(+66.05%)</b></td><td>0.47 <b>(+47.74%)</b></td><td>0.62 <b>(+45.61%)</b></td><td>0.07 (-8.33%)</td><td>0.37 <b>(+90.10%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.49 (n/a)</td><td>0.32 (n/a)</td><td>0.43 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td><td>0.48 (n/a)</td><td>0.32 (n/a)</td><td>0.43 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>2.67 (+4.76%)</td><td>1.77 (-13.47%)</td><td>2.40 (-0.70%)</td><td>0.45 (+0.15%)</td><td>1.04 (+16.44%)</td><td>2.63 (+4.76%)</td><td>1.74 (-13.47%)</td><td>2.36 (-0.70%)</td><td>0.44 (+0.15%)</td><td>1.03 (+16.44%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>2.55 (n/a)</td><td>2.04 (n/a)</td><td>2.42 (n/a)</td><td>0.45 (n/a)</td><td>0.89 (n/a)</td><td>2.51 (n/a)</td><td>2.01 (n/a)</td><td>2.38 (n/a)</td><td>0.44 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>534.90 (n/a)</td><td>441.82 (n/a)</td><td>425.20 (n/a)</td><td>326.30 (n/a)</td><td>85.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.30 (n/a)</td><td>358.94 (n/a)</td><td>317.40 (n/a)</td><td>253.20 (n/a)</td><td>118.58 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.60 (n/a)</td><td>334.68 (n/a)</td><td>275.70 (n/a)</td><td>247.70 (n/a)</td><td>146.76 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.00 (n/a)</td><td>374.88 (n/a)</td><td>430.80 (n/a)</td><td>217.70 (n/a)</td><td>137.10 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>442.40 (n/a)</td><td>301.10 (n/a)</td><td>261.20 (n/a)</td><td>234.40 (n/a)</td><td>84.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>438.30 (n/a)</td><td>326.14 (n/a)</td><td>291.00 (n/a)</td><td>257.80 (n/a)</td><td>71.69 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (-5.01%)</td><td>0.02 (+4.67%)</td><td>0.02 (-12.82%)</td><td>0.02 <b>(+61.67%)</b></td><td>0.01 <b>(-36.09%)</b></td><td>495.10 <b>(-38.14%)</b></td><td>349.52 (-16.82%)</td><td>352.40 (+14.71%)</td><td>260.50 (+5.25%)</td><td>95.65 <b>(-58.97%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>800.40 (n/a)</td><td>420.20 (n/a)</td><td>307.20 (n/a)</td><td>247.50 (n/a)</td><td>233.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (-7.92%)</td><td>0.02 (-7.85%)</td><td>0.03 (-1.88%)</td><td>0.01 <b>(-45.23%)</b></td><td>0.01 <b>(+40.34%)</b></td><td>789.20 <b>(+82.60%)</b></td><td>405.88 <b>(+21.41%)</b></td><td>304.40 (+1.91%)</td><td>272.50 (+8.61%)</td><td>218.25 <b>(+180.19%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>432.20 (n/a)</td><td>334.30 (n/a)</td><td>298.70 (n/a)</td><td>250.90 (n/a)</td><td>77.89 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (+8.03%)</td><td>0.03 (+17.51%)</td><td>0.03 (-0.30%)</td><td>0.02 <b>(+58.77%)</b></td><td>0.01 <b>(-31.48%)</b></td><td>478.40 <b>(-37.01%)</b></td><td>305.40 <b>(-25.09%)</b></td><td>264.40 (+0.30%)</td><td>236.60 (-7.43%)</td><td>98.80 <b>(-55.44%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>759.50 (n/a)</td><td>407.70 (n/a)</td><td>263.60 (n/a)</td><td>255.60 (n/a)</td><td>221.74 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (-13.70%)</td><td>0.02 (-16.40%)</td><td>0.02 <b>(-24.22%)</b></td><td>0.01 <b>(-42.10%)</b></td><td>0.01 (+15.19%)</td><td>708.20 <b>(+72.73%)</b></td><td>408.84 <b>(+28.61%)</b></td><td>377.50 <b>(+31.95%)</b></td><td>262.30 (+15.91%)</td><td>180.70 <b>(+115.75%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>410.00 (n/a)</td><td>317.88 (n/a)</td><td>286.10 (n/a)</td><td>226.30 (n/a)</td><td>83.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.05 <b>(+59.11%)</b></td><td>0.03 (+3.57%)</td><td>0.02 <b>(-38.35%)</b></td><td>0.01 (-17.41%)</td><td>0.02 <b>(+134.09%)</b></td><td>637.50 <b>(+21.08%)</b></td><td>424.78 (+17.39%)</td><td>482.30 <b>(+62.23%)</b></td><td>164.00 <b>(-37.16%)</b></td><td>207.18 <b>(+81.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.50 (n/a)</td><td>361.86 (n/a)</td><td>297.30 (n/a)</td><td>261.00 (n/a)</td><td>114.25 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (+12.01%)</td><td>0.02 (+14.85%)</td><td>0.02 (+0.73%)</td><td>0.02 (-1.46%)</td><td>0.01 <b>(+48.21%)</b></td><td>543.40 (+1.49%)</td><td>405.94 (-7.88%)</td><td>473.50 (-0.71%)</td><td>243.90 (-10.72%)</td><td>139.14 <b>(+39.29%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.40 (n/a)</td><td>440.68 (n/a)</td><td>476.90 (n/a)</td><td>273.20 (n/a)</td><td>99.89 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (+18.09%)</td><td>0.02 (+18.34%)</td><td>0.02 (+2.13%)</td><td>0.00 <b>(-47.17%)</b></td><td>0.01 <b>(+62.36%)</b></td><td>1862.40 <b>(+89.27%)</b></td><td>675.90 <b>(+21.08%)</b></td><td>484.90 (-2.08%)</td><td>241.10 (-15.31%)</td><td>675.03 <b>(+161.31%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>984.00 (n/a)</td><td>558.24 (n/a)</td><td>495.20 (n/a)</td><td>284.70 (n/a)</td><td>258.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 <b>(+43.66%)</b></td><td>0.02 <b>(+22.39%)</b></td><td>0.02 (+4.21%)</td><td>0.01 <b>(+76.53%)</b></td><td>0.01 <b>(+39.36%)</b></td><td>601.30 <b>(-43.35%)</b></td><td>434.34 <b>(-21.07%)</b></td><td>455.60 (-4.04%)</td><td>247.30 <b>(-30.38%)</b></td><td>156.93 <b>(-46.31%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1061.40 (n/a)</td><td>550.30 (n/a)</td><td>474.80 (n/a)</td><td>355.20 (n/a)</td><td>292.26 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (-8.23%)</td><td>0.02 (+16.13%)</td><td>0.02 <b>(+44.81%)</b></td><td>0.02 <b>(+45.94%)</b></td><td>0.01 <b>(-35.80%)</b></td><td>540.70 <b>(-31.49%)</b></td><td>361.38 <b>(-24.33%)</b></td><td>337.30 <b>(-30.94%)</b></td><td>250.20 (+8.97%)</td><td>113.16 <b>(-49.95%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>789.20 (n/a)</td><td>477.56 (n/a)</td><td>488.40 (n/a)</td><td>229.60 (n/a)</td><td>226.10 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 <b>(-29.83%)</b></td><td>0.02 (+2.13%)</td><td>0.02 <b>(+33.83%)</b></td><td>0.02 <b>(+30.09%)</b></td><td>0.00 <b>(-61.24%)</b></td><td>531.70 <b>(-23.12%)</b></td><td>423.72 (-13.34%)</td><td>405.30 <b>(-25.28%)</b></td><td>319.00 <b>(+42.47%)</b></td><td>79.59 <b>(-54.83%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>691.60 (n/a)</td><td>488.92 (n/a)</td><td>542.40 (n/a)</td><td>223.90 (n/a)</td><td>176.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (+12.90%)</td><td>0.03 <b>(+27.60%)</b></td><td>0.03 <b>(+63.44%)</b></td><td>0.02 <b>(+29.92%)</b></td><td>0.01 (-0.66%)</td><td>387.40 <b>(-23.03%)</b></td><td>291.86 <b>(-23.82%)</b></td><td>256.10 <b>(-38.82%)</b></td><td>194.80 (-11.41%)</td><td>86.91 <b>(-29.19%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.30 (n/a)</td><td>383.10 (n/a)</td><td>418.60 (n/a)</td><td>219.90 (n/a)</td><td>122.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 <b>(+42.75%)</b></td><td>0.02 (+17.64%)</td><td>0.03 <b>(+20.83%)</b></td><td>0.01 (+12.41%)</td><td>0.01 <b>(+49.21%)</b></td><td>613.80 (-11.04%)</td><td>395.32 (-10.88%)</td><td>320.00 (-17.23%)</td><td>209.00 <b>(-29.96%)</b></td><td>170.95 (+1.15%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>690.00 (n/a)</td><td>443.60 (n/a)</td><td>386.60 (n/a)</td><td>298.40 (n/a)</td><td>169.00 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 <b>(+29.04%)</b></td><td>0.02 (+2.27%)</td><td>0.02 <b>(+20.17%)</b></td><td>0.00 <b>(-72.57%)</b></td><td>0.02 <b>(+86.45%)</b></td><td>1858.40 <b>(+264.54%)</b></td><td>659.62 <b>(+63.14%)</b></td><td>404.60 (-16.80%)</td><td>185.80 <b>(-22.52%)</b></td><td>687.76 <b>(+437.38%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>509.80 (n/a)</td><td>404.32 (n/a)</td><td>486.30 (n/a)</td><td>239.80 (n/a)</td><td>127.98 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (+17.80%)</td><td>0.02 (+8.36%)</td><td>0.02 (-17.15%)</td><td>0.02 (+9.85%)</td><td>0.01 <b>(+54.32%)</b></td><td>512.40 (-8.97%)</td><td>428.48 (-5.62%)</td><td>485.50 <b>(+20.71%)</b></td><td>314.80 (-15.10%)</td><td>102.61 (+16.26%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.90 (n/a)</td><td>453.98 (n/a)</td><td>402.20 (n/a)</td><td>370.80 (n/a)</td><td>88.26 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.09 (-16.74%)</td><td>0.08 (-19.47%)</td><td>0.08 (-17.06%)</td><td>0.05 <b>(-36.70%)</b></td><td>0.01 <b>(+31.40%)</b></td><td>471.40 <b>(+57.98%)</b></td><td>327.08 <b>(+27.58%)</b></td><td>295.40 <b>(+20.57%)</b></td><td>275.00 <b>(+20.09%)</b></td><td>81.22 <b>(+162.28%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>298.40 (n/a)</td><td>256.38 (n/a)</td><td>245.00 (n/a)</td><td>229.00 (n/a)</td><td>30.97 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.20 (+13.58%)</td><td>0.13 (-6.40%)</td><td>0.14 (-13.72%)</td><td>0.05 <b>(-29.38%)</b></td><td>0.06 <b>(+34.39%)</b></td><td>786.60 <b>(+41.60%)</b></td><td>410.64 <b>(+21.46%)</b></td><td>290.20 (+15.89%)</td><td>205.50 (-11.95%)</td><td>243.46 <b>(+73.99%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>555.50 (n/a)</td><td>338.08 (n/a)</td><td>250.40 (n/a)</td><td>233.40 (n/a)</td><td>139.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (+13.87%)</td><td>0.02 (+4.95%)</td><td>0.02 (+11.99%)</td><td>0.02 (-8.98%)</td><td>0.00 <b>(+95.43%)</b></td><td>311.80 (+9.87%)</td><td>256.20 (-3.57%)</td><td>243.50 (-10.71%)</td><td>213.70 (-12.20%)</td><td>37.56 <b>(+91.17%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>283.80 (n/a)</td><td>265.68 (n/a)</td><td>272.70 (n/a)</td><td>243.40 (n/a)</td><td>19.65 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (-0.90%)</td><td>0.02 <b>(-28.92%)</b></td><td>0.02 <b>(-45.68%)</b></td><td>0.01 <b>(-25.14%)</b></td><td>0.01 <b>(+31.96%)</b></td><td>621.40 <b>(+33.58%)</b></td><td>458.48 <b>(+49.91%)</b></td><td>498.00 <b>(+84.10%)</b></td><td>231.50 (+0.92%)</td><td>153.53 <b>(+64.82%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>465.20 (n/a)</td><td>305.84 (n/a)</td><td>270.50 (n/a)</td><td>229.40 (n/a)</td><td>93.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.05 (-6.43%)</td><td>0.04 (+0.82%)</td><td>0.03 <b>(-21.60%)</b></td><td>0.02 <b>(+29.55%)</b></td><td>0.01 <b>(-27.82%)</b></td><td>500.30 <b>(-22.81%)</b></td><td>360.22 (-8.64%)</td><td>374.40 <b>(+27.56%)</b></td><td>248.10 (+6.85%)</td><td>100.00 <b>(-43.08%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>648.10 (n/a)</td><td>394.30 (n/a)</td><td>293.50 (n/a)</td><td>232.20 (n/a)</td><td>175.69 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (+0.95%)</td><td>0.02 (-3.13%)</td><td>0.02 <b>(-24.43%)</b></td><td>0.02 <b>(+25.72%)</b></td><td>0.01 (-14.48%)</td><td>504.90 <b>(-20.45%)</b></td><td>368.02 (-1.89%)</td><td>371.10 <b>(+32.35%)</b></td><td>247.30 (-0.92%)</td><td>109.22 <b>(-33.11%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.70 (n/a)</td><td>375.12 (n/a)</td><td>280.40 (n/a)</td><td>249.60 (n/a)</td><td>163.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (+1.42%)</td><td>0.03 (+2.41%)</td><td>0.02 (+0.72%)</td><td>0.02 (-10.03%)</td><td>0.01 (+13.87%)</td><td>574.60 (+11.14%)</td><td>408.12 (+0.55%)</td><td>456.00 (-0.72%)</td><td>239.10 (-1.40%)</td><td>149.74 (+16.45%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.00 (n/a)</td><td>405.88 (n/a)</td><td>459.30 (n/a)</td><td>242.50 (n/a)</td><td>128.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (-15.71%)</td><td>0.02 <b>(-21.93%)</b></td><td>0.02 <b>(-33.47%)</b></td><td>0.02 (-10.88%)</td><td>0.01 (-13.09%)</td><td>505.70 (+12.20%)</td><td>406.26 <b>(+28.67%)</b></td><td>470.70 <b>(+50.29%)</b></td><td>273.50 (+18.66%)</td><td>111.39 <b>(+21.38%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>450.70 (n/a)</td><td>315.74 (n/a)</td><td>313.20 (n/a)</td><td>230.50 (n/a)</td><td>91.78 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 <b>(-59.38%)</b></td><td>0.02 <b>(-46.66%)</b></td><td>0.02 <b>(-41.50%)</b></td><td>0.01 <b>(-51.84%)</b></td><td>0.01 <b>(-63.28%)</b></td><td>1061.50 <b>(+107.65%)</b></td><td>608.48 <b>(+80.43%)</b></td><td>498.10 <b>(+70.93%)</b></td><td>469.10 <b>(+146.12%)</b></td><td>254.89 <b>(+86.24%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.20 (n/a)</td><td>337.24 (n/a)</td><td>291.40 (n/a)</td><td>190.60 (n/a)</td><td>136.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (+2.15%)</td><td>0.02 (-19.32%)</td><td>0.02 <b>(-37.98%)</b></td><td>0.01 <b>(-41.21%)</b></td><td>0.01 <b>(+156.12%)</b></td><td>618.40 <b>(+70.08%)</b></td><td>416.02 <b>(+41.76%)</b></td><td>458.10 <b>(+61.25%)</b></td><td>239.40 (-2.13%)</td><td>168.36 <b>(+286.57%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>363.60 (n/a)</td><td>293.46 (n/a)</td><td>284.10 (n/a)</td><td>244.60 (n/a)</td><td>43.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (-13.09%)</td><td>0.02 (-19.23%)</td><td>0.03 (-12.36%)</td><td>0.00 <b>(-80.07%)</b></td><td>0.01 <b>(+71.17%)</b></td><td>2309.20 <b>(+401.78%)</b></td><td>715.04 <b>(+122.98%)</b></td><td>338.00 (+14.07%)</td><td>269.60 (+15.02%)</td><td>891.76 <b>(+961.77%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>460.20 (n/a)</td><td>320.68 (n/a)</td><td>296.30 (n/a)</td><td>234.40 (n/a)</td><td>83.99 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (+11.26%)</td><td>0.02 (+13.60%)</td><td>0.02 <b>(-21.86%)</b></td><td>0.01 <b>(+221.92%)</b></td><td>0.01 (+2.81%)</td><td>627.50 <b>(-68.94%)</b></td><td>420.18 <b>(-38.81%)</b></td><td>468.90 <b>(+27.97%)</b></td><td>205.50 (-10.10%)</td><td>186.00 <b>(-75.25%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2020.00 (n/a)</td><td>686.70 (n/a)</td><td>366.40 (n/a)</td><td>228.60 (n/a)</td><td>751.52 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (+12.04%)</td><td>0.02 (+4.45%)</td><td>0.02 (-7.01%)</td><td>0.01 (-4.14%)</td><td>0.01 <b>(+27.02%)</b></td><td>630.20 (+4.32%)</td><td>518.14 (-0.71%)</td><td>612.40 (+7.55%)</td><td>263.80 (-10.73%)</td><td>156.14 <b>(+21.93%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>604.10 (n/a)</td><td>521.86 (n/a)</td><td>569.40 (n/a)</td><td>295.50 (n/a)</td><td>128.06 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (-11.73%)</td><td>0.02 (+1.24%)</td><td>0.02 (+6.80%)</td><td>0.01 (-12.83%)</td><td>0.01 (-14.48%)</td><td>593.50 (+14.71%)</td><td>395.24 (-1.60%)</td><td>390.50 (-6.38%)</td><td>232.90 (+13.28%)</td><td>140.78 (+14.15%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.40 (n/a)</td><td>401.66 (n/a)</td><td>417.10 (n/a)</td><td>205.60 (n/a)</td><td>123.33 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.39 (-4.87%)</td><td>0.31 (+1.67%)</td><td>0.37 (+16.01%)</td><td>0.19 <b>(+21.50%)</b></td><td>0.10 (-8.59%)</td><td>525.70 (-17.69%)</td><td>360.60 (-4.58%)</td><td>268.10 (-13.82%)</td><td>249.00 (+5.11%)</td><td>140.75 (-17.50%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.42 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>638.70 (n/a)</td><td>377.90 (n/a)</td><td>311.10 (n/a)</td><td>236.90 (n/a)</td><td>170.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.40 (-18.11%)</td><td>0.28 (+1.12%)</td><td>0.23 (+3.24%)</td><td>0.18 <b>(+25.84%)</b></td><td>0.09 <b>(-33.54%)</b></td><td>539.00 <b>(-20.54%)</b></td><td>386.38 (-10.27%)</td><td>422.60 (-3.14%)</td><td>244.00 <b>(+22.12%)</b></td><td>120.17 <b>(-36.07%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.49 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>678.30 (n/a)</td><td>430.60 (n/a)</td><td>436.30 (n/a)</td><td>199.80 (n/a)</td><td>187.99 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.41 (+17.57%)</td><td>0.28 (+19.81%)</td><td>0.31 <b>(+42.16%)</b></td><td>0.16 (-6.58%)</td><td>0.10 <b>(+53.35%)</b></td><td>608.70 (+7.03%)</td><td>403.64 (-10.33%)</td><td>316.40 <b>(-29.64%)</b></td><td>241.60 (-14.96%)</td><td>165.13 <b>(+51.23%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.35 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>568.70 (n/a)</td><td>450.14 (n/a)</td><td>449.70 (n/a)</td><td>284.10 (n/a)</td><td>109.20 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.27 (-6.11%)</td><td>0.18 (-3.12%)</td><td>0.16 (+8.49%)</td><td>0.14 <b>(+21.23%)</b></td><td>0.05 <b>(-30.57%)</b></td><td>529.80 (-17.50%)</td><td>424.16 (-3.50%)</td><td>458.00 (-7.81%)</td><td>277.40 (+6.49%)</td><td>108.65 <b>(-34.23%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>642.20 (n/a)</td><td>439.56 (n/a)</td><td>496.80 (n/a)</td><td>260.50 (n/a)</td><td>165.20 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.43 <b>(+60.22%)</b></td><td>0.20 <b>(+32.66%)</b></td><td>0.14 (-13.28%)</td><td>0.14 <b>(+258.19%)</b></td><td>0.13 (+16.18%)</td><td>542.80 <b>(-72.08%)</b></td><td>445.04 <b>(-53.65%)</b></td><td>517.60 (+15.30%)</td><td>171.80 <b>(-37.60%)</b></td><td>156.66 <b>(-81.62%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>0.11 (n/a)</td><td>1944.30 (n/a)</td><td>960.08 (n/a)</td><td>448.90 (n/a)</td><td>275.30 (n/a)</td><td>852.18 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.25 (-16.24%)</td><td>0.16 <b>(-21.86%)</b></td><td>0.14 <b>(-43.07%)</b></td><td>0.13 (+10.11%)</td><td>0.05 <b>(-32.04%)</b></td><td>564.50 (-9.19%)</td><td>475.66 <b>(+20.57%)</b></td><td>534.20 <b>(+75.67%)</b></td><td>291.40 (+19.38%)</td><td>113.34 <b>(-28.92%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>621.60 (n/a)</td><td>394.50 (n/a)</td><td>304.10 (n/a)</td><td>244.10 (n/a)</td><td>159.44 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.52 (-3.56%)</td><td>0.37 (-1.42%)</td><td>0.41 (-3.62%)</td><td>0.26 (+1.34%)</td><td>0.11 (-10.80%)</td><td>504.20 (-1.31%)</td><td>375.86 (-0.30%)</td><td>323.60 (+3.75%)</td><td>253.60 (+3.68%)</td><td>110.28 (-11.17%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.54 (n/a)</td><td>0.38 (n/a)</td><td>0.42 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>510.90 (n/a)</td><td>376.98 (n/a)</td><td>311.90 (n/a)</td><td>244.60 (n/a)</td><td>124.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.41 <b>(-35.23%)</b></td><td>0.33 (-10.79%)</td><td>0.34 <b>(+26.60%)</b></td><td>0.21 (-6.51%)</td><td>0.09 <b>(-50.96%)</b></td><td>638.30 (+6.97%)</td><td>430.74 (+1.34%)</td><td>380.00 <b>(-21.00%)</b></td><td>319.80 <b>(+54.34%)</b></td><td>134.44 <b>(-22.16%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.63 (n/a)</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>596.70 (n/a)</td><td>425.04 (n/a)</td><td>481.00 (n/a)</td><td>207.20 (n/a)</td><td>172.72 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.60 <b>(+27.56%)</b></td><td>0.37 <b>(+31.85%)</b></td><td>0.38 <b>(+42.67%)</b></td><td>0.20 <b>(+58.79%)</b></td><td>0.15 <b>(+25.14%)</b></td><td>663.90 <b>(-37.02%)</b></td><td>407.86 <b>(-26.82%)</b></td><td>340.90 <b>(-29.91%)</b></td><td>218.40 <b>(-21.61%)</b></td><td>173.69 <b>(-40.47%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.47 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>1054.20 (n/a)</td><td>557.32 (n/a)</td><td>486.40 (n/a)</td><td>278.60 (n/a)</td><td>291.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (+16.25%)</td><td>0.01 <b>(+23.10%)</b></td><td>0.02 <b>(+52.64%)</b></td><td>0.01 (-13.45%)</td><td>0.00 (+17.56%)</td><td>583.30 (+15.53%)</td><td>325.56 (-15.85%)</td><td>269.80 <b>(-34.48%)</b></td><td>227.40 (-13.96%)</td><td>146.59 <b>(+27.66%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>504.90 (n/a)</td><td>386.90 (n/a)</td><td>411.80 (n/a)</td><td>264.30 (n/a)</td><td>114.83 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (+16.75%)</td><td>0.01 <b>(+21.89%)</b></td><td>0.01 (+9.24%)</td><td>0.01 <b>(+293.00%)</b></td><td>0.01 (-9.29%)</td><td>523.50 <b>(-74.56%)</b></td><td>384.20 <b>(-45.94%)</b></td><td>412.90 (-8.47%)</td><td>210.60 (-14.36%)</td><td>145.47 <b>(-80.89%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2057.40 (n/a)</td><td>710.66 (n/a)</td><td>451.10 (n/a)</td><td>245.90 (n/a)</td><td>761.20 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.01 (-2.29%)</td><td>0.01 (+9.04%)</td><td>0.01 (+8.08%)</td><td>0.01 <b>(+42.46%)</b></td><td>0.00 <b>(-30.97%)</b></td><td>434.30 <b>(-29.82%)</b></td><td>372.90 (-12.11%)</td><td>385.20 (-7.47%)</td><td>281.40 (+2.36%)</td><td>60.64 <b>(-51.06%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>618.80 (n/a)</td><td>424.30 (n/a)</td><td>416.30 (n/a)</td><td>274.90 (n/a)</td><td>123.91 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.59 (+16.28%)</td><td>0.46 <b>(+25.87%)</b></td><td>0.48 <b>(+38.42%)</b></td><td>0.30 <b>(+24.03%)</b></td><td>0.10 (+9.25%)</td><td>435.10 (-19.37%)</td><td>304.06 <b>(-21.11%)</b></td><td>277.30 <b>(-27.75%)</b></td><td>223.20 (-14.02%)</td><td>79.74 <b>(-21.33%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.51 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.10 (n/a)</td><td>539.60 (n/a)</td><td>385.42 (n/a)</td><td>383.80 (n/a)</td><td>259.60 (n/a)</td><td>101.37 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.57 <b>(-22.59%)</b></td><td>0.50 (-8.11%)</td><td>0.51 (+0.77%)</td><td>0.41 (-3.74%)</td><td>0.06 <b>(-49.42%)</b></td><td>325.20 (+3.86%)</td><td>267.52 (+6.37%)</td><td>260.10 (-0.80%)</td><td>230.20 <b>(+29.18%)</b></td><td>35.54 <b>(-28.96%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.74 (n/a)</td><td>0.54 (n/a)</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.12 (n/a)</td><td>313.10 (n/a)</td><td>251.50 (n/a)</td><td>262.20 (n/a)</td><td>178.20 (n/a)</td><td>50.03 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.52 (-1.80%)</td><td>0.43 <b>(+20.60%)</b></td><td>0.46 <b>(+49.79%)</b></td><td>0.25 (-13.09%)</td><td>0.11 (+7.13%)</td><td>532.40 (+15.06%)</td><td>329.44 (-15.35%)</td><td>288.00 <b>(-33.24%)</b></td><td>255.80 (+1.83%)</td><td>115.00 <b>(+32.73%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.53 (n/a)</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.10 (n/a)</td><td>462.70 (n/a)</td><td>389.20 (n/a)</td><td>431.40 (n/a)</td><td>251.20 (n/a)</td><td>86.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.53 (-1.37%)</td><td>0.48 <b>(+26.01%)</b></td><td>0.47 <b>(+43.90%)</b></td><td>0.42 <b>(+48.52%)</b></td><td>0.04 <b>(-59.39%)</b></td><td>316.80 <b>(-32.68%)</b></td><td>279.48 <b>(-24.38%)</b></td><td>280.60 <b>(-30.51%)</b></td><td>247.50 (+1.39%)</td><td>25.37 <b>(-71.78%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.54 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>470.60 (n/a)</td><td>369.60 (n/a)</td><td>403.80 (n/a)</td><td>244.10 (n/a)</td><td>89.89 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.52 (-7.44%)</td><td>0.42 (-16.72%)</td><td>0.45 (-13.77%)</td><td>0.25 <b>(-37.95%)</b></td><td>0.10 <b>(+64.56%)</b></td><td>534.10 <b>(+61.12%)</b></td><td>335.36 <b>(+26.69%)</b></td><td>295.70 (+15.96%)</td><td>256.50 (+8.05%)</td><td>113.30 <b>(+195.27%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.56 (n/a)</td><td>0.51 (n/a)</td><td>0.52 (n/a)</td><td>0.40 (n/a)</td><td>0.06 (n/a)</td><td>331.50 (n/a)</td><td>264.70 (n/a)</td><td>255.00 (n/a)</td><td>237.40 (n/a)</td><td>38.37 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (-1.26%)</td><td>0.02 (+5.20%)</td><td>0.01 (+0.77%)</td><td>0.01 <b>(+42.18%)</b></td><td>0.00 <b>(-38.40%)</b></td><td>313.10 <b>(-29.67%)</b></td><td>271.90 (-8.78%)</td><td>275.20 (-0.76%)</td><td>222.00 (+1.28%)</td><td>36.46 <b>(-58.08%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>445.20 (n/a)</td><td>298.06 (n/a)</td><td>277.30 (n/a)</td><td>219.20 (n/a)</td><td>86.98 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (-16.28%)</td><td>0.01 <b>(-37.83%)</b></td><td>0.01 <b>(-45.47%)</b></td><td>0.00 <b>(-78.82%)</b></td><td>0.01 <b>(+69.69%)</b></td><td>2071.10 <b>(+372.10%)</b></td><td>763.46 <b>(+165.33%)</b></td><td>494.50 <b>(+83.35%)</b></td><td>262.20 (+19.45%)</td><td>755.20 <b>(+766.45%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>438.70 (n/a)</td><td>287.74 (n/a)</td><td>269.70 (n/a)</td><td>219.50 (n/a)</td><td>87.16 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.00 (+0.00%)</td><td>0.00 (-15.79%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-19.82%)</td><td>18407.49 (-4.76%)</td><td>13984.87 (+6.12%)</td><td>14552.73 (-1.21%)</td><td>6425.42 (-8.55%)</td><td>4836.44 (-16.74%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19326.93 (n/a)</td><td>13178.37 (n/a)</td><td>14730.90 (n/a)</td><td>7025.94 (n/a)</td><td>5808.95 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.00 <b>(-54.55%)</b></td><td>0.00 <b>(-26.67%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-80.64%)</b></td><td>20704.30 (+11.43%)</td><td>18683.58 <b>(+26.18%)</b></td><td>18527.49 (+19.80%)</td><td>17241.90 <b>(+126.22%)</b></td><td>1269.36 <b>(-69.99%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18580.78 (n/a)</td><td>14807.40 (n/a)</td><td>15464.91 (n/a)</td><td>7621.59 (n/a)</td><td>4229.27 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/swiglu_prefill</summary>


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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.14 (+5.50%)</td><td>0.09 (-1.02%)</td><td>0.09 (-1.03%)</td><td>0.08 (-3.38%)</td><td>0.02 (+19.65%)</td><td>27217.70 (+3.56%)</td><td>23420.31 (+2.21%)</td><td>24158.90 (+1.06%)</td><td>15404.63 (-5.21%)</td><td>4724.11 (+14.87%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>26281.37 (n/a)</td><td>22914.76 (n/a)</td><td>23906.45 (n/a)</td><td>16251.10 (n/a)</td><td>4112.61 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.49 (-18.89%)</td><td>1.23 (+18.60%)</td><td>1.48 <b>(+59.58%)</b></td><td>0.77 <b>(+30.31%)</b></td><td>0.35 <b>(-27.01%)</b></td><td>678.00 <b>(-23.27%)</b></td><td>458.60 <b>(-20.78%)</b></td><td>354.20 <b>(-37.33%)</b></td><td>351.20 <b>(+23.31%)</b></td><td>151.00 <b>(-31.23%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.84 (n/a)</td><td>1.04 (n/a)</td><td>0.93 (n/a)</td><td>0.59 (n/a)</td><td>0.48 (n/a)</td><td>883.60 (n/a)</td><td>578.90 (n/a)</td><td>565.20 (n/a)</td><td>284.80 (n/a)</td><td>219.58 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>2.59 (+6.82%)</td><td>2.00 <b>(+84.60%)</b></td><td>2.43 <b>(+133.44%)</b></td><td>1.01 <b>(+245.66%)</b></td><td>0.71 (-18.84%)</td><td>1039.10 <b>(-71.07%)</b></td><td>602.64 <b>(-67.62%)</b></td><td>431.80 <b>(-57.16%)</b></td><td>405.60 (-6.39%)</td><td>276.13 <b>(-82.20%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>2.42 (n/a)</td><td>1.08 (n/a)</td><td>1.04 (n/a)</td><td>0.29 (n/a)</td><td>0.88 (n/a)</td><td>3591.90 (n/a)</td><td>1861.10 (n/a)</td><td>1007.90 (n/a)</td><td>433.30 (n/a)</td><td>1551.54 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.69 (-0.17%)</td><td>1.07 (+3.25%)</td><td>0.99 (+2.47%)</td><td>0.28 <b>(+74.25%)</b></td><td>0.57 (-5.37%)</td><td>1846.70 <b>(-42.61%)</b></td><td>732.18 <b>(-27.36%)</b></td><td>530.90 (-2.41%)</td><td>310.70 (+0.16%)</td><td>637.80 <b>(-48.66%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.69 (n/a)</td><td>1.04 (n/a)</td><td>0.96 (n/a)</td><td>0.16 (n/a)</td><td>0.61 (n/a)</td><td>3217.80 (n/a)</td><td>1007.94 (n/a)</td><td>544.00 (n/a)</td><td>310.20 (n/a)</td><td>1242.32 (n/a)</td>
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
