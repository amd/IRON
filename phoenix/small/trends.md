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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.06 (+16.02%)</td><td>0.04 (+4.01%)</td><td>0.04 (-2.39%)</td><td>0.02 (-18.72%)</td><td>0.02 <b>(+52.43%)</b></td><td>628.30 <b>(+23.03%)</b></td><td>360.44 (+5.42%)</td><td>291.40 (+2.46%)</td><td>210.80 (-13.78%)</td><td>174.87 <b>(+58.16%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.70 (n/a)</td><td>341.92 (n/a)</td><td>284.40 (n/a)</td><td>244.50 (n/a)</td><td>110.56 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.05 (+2.29%)</td><td>0.04 (+10.08%)</td><td>0.03 (-14.58%)</td><td>0.02 <b>(+104.85%)</b></td><td>0.01 (-8.55%)</td><td>514.30 <b>(-51.19%)</b></td><td>377.40 <b>(-21.91%)</b></td><td>436.70 (+17.05%)</td><td>233.80 (-2.26%)</td><td>129.74 <b>(-60.67%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1053.60 (n/a)</td><td>483.30 (n/a)</td><td>373.10 (n/a)</td><td>239.20 (n/a)</td><td>329.91 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.05 <b>(-24.32%)</b></td><td>0.03 (-17.52%)</td><td>0.03 <b>(-33.21%)</b></td><td>0.02 <b>(+23.85%)</b></td><td>0.01 <b>(-45.16%)</b></td><td>526.30 (-19.25%)</td><td>413.26 (+3.38%)</td><td>473.60 <b>(+49.73%)</b></td><td>249.10 <b>(+32.15%)</b></td><td>118.36 <b>(-44.97%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>651.80 (n/a)</td><td>399.74 (n/a)</td><td>316.30 (n/a)</td><td>188.50 (n/a)</td><td>215.08 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (+1.94%)</td><td>0.02 (+11.16%)</td><td>0.02 (+17.73%)</td><td>0.01 (+3.86%)</td><td>0.00 (+6.86%)</td><td>400.70 (-3.72%)</td><td>280.58 (-9.70%)</td><td>245.40 (-15.06%)</td><td>226.00 (-1.91%)</td><td>70.95 (+1.95%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>416.20 (n/a)</td><td>310.72 (n/a)</td><td>288.90 (n/a)</td><td>230.40 (n/a)</td><td>69.60 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (+17.17%)</td><td>0.01 (+0.22%)</td><td>0.01 (-11.21%)</td><td>0.01 (-13.26%)</td><td>0.01 <b>(+25.85%)</b></td><td>659.40 (+15.28%)</td><td>420.52 (+4.29%)</td><td>439.80 (+12.62%)</td><td>214.40 (-14.65%)</td><td>170.60 <b>(+20.65%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.00 (n/a)</td><td>403.24 (n/a)</td><td>390.50 (n/a)</td><td>251.20 (n/a)</td><td>141.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (-15.73%)</td><td>0.01 (-4.69%)</td><td>0.01 (+1.40%)</td><td>0.01 (+16.74%)</td><td>0.00 <b>(-27.02%)</b></td><td>514.50 (-14.35%)</td><td>394.04 (+0.12%)</td><td>417.20 (-1.37%)</td><td>280.90 (+18.67%)</td><td>104.64 <b>(-26.74%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.70 (n/a)</td><td>393.58 (n/a)</td><td>423.00 (n/a)</td><td>236.70 (n/a)</td><td>142.84 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 <b>(-27.10%)</b></td><td>0.01 <b>(-34.64%)</b></td><td>0.01 <b>(-32.64%)</b></td><td>0.00 <b>(-73.02%)</b></td><td>0.00 (+2.48%)</td><td>1967.20 <b>(+270.61%)</b></td><td>757.28 <b>(+106.79%)</b></td><td>439.60 <b>(+48.46%)</b></td><td>347.90 <b>(+37.18%)</b></td><td>684.11 <b>(+454.64%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.80 (n/a)</td><td>366.20 (n/a)</td><td>296.10 (n/a)</td><td>253.60 (n/a)</td><td>123.34 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.01 <b>(-46.97%)</b></td><td>0.01 <b>(-39.91%)</b></td><td>0.01 <b>(-20.13%)</b></td><td>0.00 <b>(-68.02%)</b></td><td>0.00 <b>(-44.93%)</b></td><td>2022.60 <b>(+212.71%)</b></td><td>805.38 <b>(+94.50%)</b></td><td>539.50 <b>(+25.20%)</b></td><td>428.40 <b>(+88.64%)</b></td><td>682.09 <b>(+281.66%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>646.80 (n/a)</td><td>414.08 (n/a)</td><td>430.90 (n/a)</td><td>227.10 (n/a)</td><td>178.71 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (-1.93%)</td><td>0.01 <b>(-25.18%)</b></td><td>0.01 (-14.76%)</td><td>0.00 <b>(-73.65%)</b></td><td>0.01 <b>(+44.16%)</b></td><td>1878.70 <b>(+279.46%)</b></td><td>733.94 <b>(+86.75%)</b></td><td>482.70 (+17.33%)</td><td>279.70 (+1.97%)</td><td>648.35 <b>(+529.08%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.10 (n/a)</td><td>393.00 (n/a)</td><td>411.40 (n/a)</td><td>274.30 (n/a)</td><td>103.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>424.70 (n/a)</td><td>328.22 (n/a)</td><td>360.30 (n/a)</td><td>235.40 (n/a)</td><td>86.69 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>646.70 (n/a)</td><td>445.20 (n/a)</td><td>422.30 (n/a)</td><td>199.80 (n/a)</td><td>172.53 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.30 (n/a)</td><td>392.00 (n/a)</td><td>385.60 (n/a)</td><td>279.30 (n/a)</td><td>96.95 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.40 (n/a)</td><td>359.20 (n/a)</td><td>357.30 (n/a)</td><td>230.40 (n/a)</td><td>126.47 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>634.00 (n/a)</td><td>327.38 (n/a)</td><td>267.60 (n/a)</td><td>204.10 (n/a)</td><td>173.55 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>343.00 (n/a)</td><td>305.20 (n/a)</td><td>307.20 (n/a)</td><td>255.30 (n/a)</td><td>32.28 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.03 <b>(-21.24%)</b></td><td>0.86 (-0.01%)</td><td>0.90 (+17.24%)</td><td>0.62 (-9.05%)</td><td>0.18 <b>(-31.21%)</b></td><td>744.00 (+9.95%)</td><td>555.42 (-1.65%)</td><td>511.00 (-14.71%)</td><td>444.70 <b>(+26.98%)</b></td><td>126.07 (-0.13%)</td><td>75.46 <b>(-21.24%)</b></td><td>62.74 (-0.01%)</td><td>65.66 (+17.24%)</td><td>45.10 (-9.05%)</td><td>12.93 <b>(-31.21%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.31 (n/a)</td><td>0.86 (n/a)</td><td>0.77 (n/a)</td><td>0.68 (n/a)</td><td>0.26 (n/a)</td><td>676.70 (n/a)</td><td>564.72 (n/a)</td><td>599.10 (n/a)</td><td>350.20 (n/a)</td><td>126.23 (n/a)</td><td>95.81 (n/a)</td><td>62.75 (n/a)</td><td>56.01 (n/a)</td><td>49.59 (n/a)</td><td>18.80 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.27 (-18.26%)</td><td>0.89 <b>(-21.65%)</b></td><td>0.91 <b>(-21.95%)</b></td><td>0.28 <b>(-57.96%)</b></td><td>0.40 <b>(+20.88%)</b></td><td>2321.90 <b>(+137.90%)</b></td><td>987.60 <b>(+58.52%)</b></td><td>719.50 <b>(+28.12%)</b></td><td>515.30 <b>(+22.34%)</b></td><td>758.63 <b>(+252.40%)</b></td><td>130.24 (-18.26%)</td><td>91.52 <b>(-21.65%)</b></td><td>93.28 <b>(-21.95%)</b></td><td>28.90 <b>(-57.96%)</b></td><td>41.17 <b>(+20.88%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.56 (n/a)</td><td>1.14 (n/a)</td><td>1.17 (n/a)</td><td>0.67 (n/a)</td><td>0.33 (n/a)</td><td>976.00 (n/a)</td><td>623.02 (n/a)</td><td>561.60 (n/a)</td><td>421.20 (n/a)</td><td>215.27 (n/a)</td><td>159.33 (n/a)</td><td>116.81 (n/a)</td><td>119.50 (n/a)</td><td>68.76 (n/a)</td><td>34.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.01 <b>(-43.83%)</b></td><td>0.88 (-17.53%)</td><td>0.96 (-11.37%)</td><td>0.69 <b>(+40.84%)</b></td><td>0.15 <b>(-68.47%)</b></td><td>1088.60 <b>(-29.00%)</b></td><td>878.20 (+4.11%)</td><td>783.80 (+12.83%)</td><td>745.10 <b>(+78.04%)</b></td><td>162.12 <b>(-61.58%)</b></td><td>112.58 <b>(-43.83%)</b></td><td>98.01 (-17.53%)</td><td>107.02 (-11.37%)</td><td>77.06 <b>(+40.84%)</b></td><td>16.89 <b>(-68.47%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.80 (n/a)</td><td>1.07 (n/a)</td><td>1.08 (n/a)</td><td>0.49 (n/a)</td><td>0.48 (n/a)</td><td>1533.30 (n/a)</td><td>843.50 (n/a)</td><td>694.70 (n/a)</td><td>418.50 (n/a)</td><td>421.98 (n/a)</td><td>200.42 (n/a)</td><td>118.85 (n/a)</td><td>120.75 (n/a)</td><td>54.71 (n/a)</td><td>53.57 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.65 (-10.67%)</td><td>1.39 (+1.79%)</td><td>1.51 <b>(+28.58%)</b></td><td>0.93 (-18.98%)</td><td>0.31 (+0.31%)</td><td>1128.80 <b>(+23.43%)</b></td><td>789.68 (-0.58%)</td><td>692.60 <b>(-22.22%)</b></td><td>633.80 (+11.94%)</td><td>208.61 <b>(+34.57%)</b></td><td>211.76 (-10.67%)</td><td>178.22 (+1.79%)</td><td>193.79 <b>(+28.58%)</b></td><td>118.91 (-18.98%)</td><td>39.50 (+0.31%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.85 (n/a)</td><td>1.37 (n/a)</td><td>1.18 (n/a)</td><td>1.15 (n/a)</td><td>0.31 (n/a)</td><td>914.50 (n/a)</td><td>794.28 (n/a)</td><td>890.50 (n/a)</td><td>566.20 (n/a)</td><td>155.02 (n/a)</td><td>237.07 (n/a)</td><td>175.09 (n/a)</td><td>150.71 (n/a)</td><td>146.77 (n/a)</td><td>39.38 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.67 <b>(+22.41%)</b></td><td>1.22 (+15.47%)</td><td>1.32 (+0.23%)</td><td>0.46 <b>(+48.88%)</b></td><td>0.45 (+1.00%)</td><td>2284.50 <b>(-32.83%)</b></td><td>1055.82 <b>(-22.65%)</b></td><td>796.90 (-0.23%)</td><td>629.50 (-18.31%)</td><td>690.39 <b>(-39.69%)</b></td><td>213.20 <b>(+22.41%)</b></td><td>156.57 (+15.47%)</td><td>168.43 (+0.23%)</td><td>58.75 <b>(+48.88%)</b></td><td>57.81 (+1.00%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.36 (n/a)</td><td>1.06 (n/a)</td><td>1.31 (n/a)</td><td>0.31 (n/a)</td><td>0.45 (n/a)</td><td>3401.00 (n/a)</td><td>1364.96 (n/a)</td><td>798.70 (n/a)</td><td>770.60 (n/a)</td><td>1144.76 (n/a)</td><td>174.17 (n/a)</td><td>135.59 (n/a)</td><td>168.05 (n/a)</td><td>39.46 (n/a)</td><td>57.23 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.38 <b>(-34.39%)</b></td><td>1.04 <b>(-36.48%)</b></td><td>1.19 <b>(-20.97%)</b></td><td>0.30 <b>(-78.24%)</b></td><td>0.44 <b>(+49.69%)</b></td><td>3470.20 <b>(+359.51%)</b></td><td>1392.48 <b>(+112.36%)</b></td><td>880.50 <b>(+26.53%)</b></td><td>759.80 <b>(+52.42%)</b></td><td>1168.35 <b>(+999.73%)</b></td><td>176.64 <b>(-34.39%)</b></td><td>133.12 <b>(-36.48%)</b></td><td>152.43 <b>(-20.97%)</b></td><td>38.68 <b>(-78.24%)</b></td><td>56.71 <b>(+49.69%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>2.10 (n/a)</td><td>1.64 (n/a)</td><td>1.51 (n/a)</td><td>1.39 (n/a)</td><td>0.30 (n/a)</td><td>755.20 (n/a)</td><td>655.72 (n/a)</td><td>695.90 (n/a)</td><td>498.50 (n/a)</td><td>106.24 (n/a)</td><td>269.23 (n/a)</td><td>209.57 (n/a)</td><td>192.87 (n/a)</td><td>177.72 (n/a)</td><td>37.88 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>2.07 <b>(+36.77%)</b></td><td>1.30 <b>(+31.63%)</b></td><td>1.20 <b>(+36.28%)</b></td><td>0.43 <b>(+41.23%)</b></td><td>0.63 <b>(+23.30%)</b></td><td>2412.10 <b>(-29.19%)</b></td><td>1075.26 <b>(-27.11%)</b></td><td>870.80 <b>(-26.63%)</b></td><td>507.50 <b>(-26.88%)</b></td><td>772.42 <b>(-31.12%)</b></td><td>264.46 <b>(+36.77%)</b></td><td>166.90 <b>(+31.63%)</b></td><td>154.13 <b>(+36.28%)</b></td><td>55.64 <b>(+41.23%)</b></td><td>81.12 <b>(+23.30%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.51 (n/a)</td><td>0.99 (n/a)</td><td>0.88 (n/a)</td><td>0.31 (n/a)</td><td>0.51 (n/a)</td><td>3406.60 (n/a)</td><td>1475.10 (n/a)</td><td>1186.80 (n/a)</td><td>694.10 (n/a)</td><td>1121.36 (n/a)</td><td>193.36 (n/a)</td><td>126.79 (n/a)</td><td>113.10 (n/a)</td><td>39.40 (n/a)</td><td>65.79 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.63 (-10.25%)</td><td>0.54 (-8.69%)</td><td>0.54 (-6.31%)</td><td>0.48 (+8.09%)</td><td>0.06 <b>(-45.69%)</b></td><td>744.10 (-7.48%)</td><td>668.46 (+7.53%)</td><td>668.90 (+6.73%)</td><td>571.20 (+11.41%)</td><td>66.39 <b>(-43.48%)</b></td><td>29.37 (-10.25%)</td><td>25.31 (-8.69%)</td><td>25.08 (-6.31%)</td><td>22.55 (+8.09%)</td><td>2.63 <b>(-45.69%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.70 (n/a)</td><td>0.60 (n/a)</td><td>0.58 (n/a)</td><td>0.45 (n/a)</td><td>0.10 (n/a)</td><td>804.30 (n/a)</td><td>621.64 (n/a)</td><td>626.70 (n/a)</td><td>512.70 (n/a)</td><td>117.47 (n/a)</td><td>32.72 (n/a)</td><td>27.71 (n/a)</td><td>26.77 (n/a)</td><td>20.86 (n/a)</td><td>4.85 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>3.30 <b>(-23.17%)</b></td><td>2.16 (+15.17%)</td><td>2.34 <b>(+187.96%)</b></td><td>1.11 <b>(+50.51%)</b></td><td>0.88 <b>(-45.04%)</b></td><td>2368.20 <b>(-33.56%)</b></td><td>1417.12 <b>(-39.63%)</b></td><td>1118.70 <b>(-65.27%)</b></td><td>794.20 <b>(+30.15%)</b></td><td>648.40 <b>(-54.99%)</b></td><td>675.99 <b>(-23.17%)</b></td><td>442.29 (+15.17%)</td><td>479.90 <b>(+187.96%)</b></td><td>226.70 <b>(+50.51%)</b></td><td>180.44 <b>(-45.04%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>4.30 (n/a)</td><td>1.88 (n/a)</td><td>0.81 (n/a)</td><td>0.74 (n/a)</td><td>1.60 (n/a)</td><td>3564.30 (n/a)</td><td>2347.42 (n/a)</td><td>3221.40 (n/a)</td><td>610.20 (n/a)</td><td>1440.65 (n/a)</td><td>879.83 (n/a)</td><td>384.04 (n/a)</td><td>166.66 (n/a)</td><td>150.62 (n/a)</td><td>328.31 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>473.80 (n/a)</td><td>407.14 (n/a)</td><td>413.50 (n/a)</td><td>319.80 (n/a)</td><td>55.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.30 (n/a)</td><td>462.00 (n/a)</td><td>511.40 (n/a)</td><td>241.20 (n/a)</td><td>136.37 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>482.60 (n/a)</td><td>399.12 (n/a)</td><td>454.50 (n/a)</td><td>292.30 (n/a)</td><td>95.05 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.30 (n/a)</td><td>446.24 (n/a)</td><td>443.60 (n/a)</td><td>300.30 (n/a)</td><td>95.57 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>552.00 (n/a)</td><td>407.48 (n/a)</td><td>510.50 (n/a)</td><td>149.30 (n/a)</td><td>175.89 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>489.00 (n/a)</td><td>399.62 (n/a)</td><td>370.80 (n/a)</td><td>319.70 (n/a)</td><td>75.00 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.61 (-0.24%)</td><td>0.48 (+0.73%)</td><td>0.45 (-6.19%)</td><td>0.42 (+18.41%)</td><td>0.08 (-15.94%)</td><td>530.70 (-15.55%)</td><td>473.02 (-1.95%)</td><td>489.20 (+6.60%)</td><td>364.10 (+0.25%)</td><td>68.47 <b>(-29.44%)</b></td><td>25.92 (-0.24%)</td><td>20.34 (+0.73%)</td><td>19.29 (-6.19%)</td><td>17.78 (+18.41%)</td><td>3.35 (-15.94%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.61 (n/a)</td><td>0.47 (n/a)</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>628.40 (n/a)</td><td>482.44 (n/a)</td><td>458.90 (n/a)</td><td>363.20 (n/a)</td><td>97.04 (n/a)</td><td>25.98 (n/a)</td><td>20.19 (n/a)</td><td>20.56 (n/a)</td><td>15.02 (n/a)</td><td>3.99 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.66 (+14.81%)</td><td>0.36 (-18.07%)</td><td>0.34 (-19.42%)</td><td>0.13 <b>(-60.61%)</b></td><td>0.20 <b>(+125.83%)</b></td><td>1685.00 <b>(+153.84%)</b></td><td>830.92 <b>(+58.46%)</b></td><td>655.00 <b>(+24.10%)</b></td><td>336.80 (-12.90%)</td><td>529.23 <b>(+417.32%)</b></td><td>28.02 (+14.81%)</td><td>15.22 (-18.07%)</td><td>14.41 (-19.42%)</td><td>5.60 <b>(-60.61%)</b></td><td>8.60 <b>(+125.83%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.57 (n/a)</td><td>0.44 (n/a)</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.09 (n/a)</td><td>663.80 (n/a)</td><td>524.38 (n/a)</td><td>527.80 (n/a)</td><td>386.70 (n/a)</td><td>102.30 (n/a)</td><td>24.41 (n/a)</td><td>18.58 (n/a)</td><td>17.88 (n/a)</td><td>14.22 (n/a)</td><td>3.81 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.31 (+1.08%)</td><td>0.30 (-0.48%)</td><td>0.30 (-1.21%)</td><td>0.30 (-1.18%)</td><td>0.01 <b>(+78.10%)</b></td><td>84906.40 (+1.19%)</td><td>83088.28 (+0.49%)</td><td>83216.20 (+1.22%)</td><td>81170.00 (-1.07%)</td><td>1409.58 <b>(+78.27%)</b></td><td>211.65 (+1.08%)</td><td>206.81 (-0.48%)</td><td>206.45 (-1.21%)</td><td>202.34 (-1.18%)</td><td>3.52 <b>(+78.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83905.20 (n/a)</td><td>82679.40 (n/a)</td><td>82211.50 (n/a)</td><td>82048.90 (n/a)</td><td>790.69 (n/a)</td><td>209.39 (n/a)</td><td>207.80 (n/a)</td><td>208.97 (n/a)</td><td>204.75 (n/a)</td><td>1.97 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.15 (+0.16%)</td><td>1.13 (+1.75%)</td><td>1.15 (-0.04%)</td><td>1.10 (+4.41%)</td><td>0.02 <b>(-50.18%)</b></td><td>22932.80 (-4.22%)</td><td>22287.06 (-1.84%)</td><td>21976.90 (+0.04%)</td><td>21906.70 (-0.16%)</td><td>491.53 <b>(-52.31%)</b></td><td>784.23 (+0.16%)</td><td>771.14 (+1.75%)</td><td>781.72 (-0.04%)</td><td>749.14 (+4.41%)</td><td>16.85 <b>(-50.18%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.15 (n/a)</td><td>1.11 (n/a)</td><td>1.15 (n/a)</td><td>1.05 (n/a)</td><td>0.05 (n/a)</td><td>23943.30 (n/a)</td><td>22705.40 (n/a)</td><td>21967.60 (n/a)</td><td>21941.60 (n/a)</td><td>1030.59 (n/a)</td><td>782.98 (n/a)</td><td>757.87 (n/a)</td><td>782.05 (n/a)</td><td>717.52 (n/a)</td><td>33.82 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>2.22 <b>(-44.34%)</b></td><td>1.82 (-18.21%)</td><td>1.73 (-19.41%)</td><td>1.61 <b>(+38.75%)</b></td><td>0.25 <b>(-77.22%)</b></td><td>4998.10 <b>(-27.93%)</b></td><td>4481.16 (+5.11%)</td><td>4657.60 <b>(+24.09%)</b></td><td>3623.30 <b>(+79.66%)</b></td><td>545.43 <b>(-70.11%)</b></td><td>583.42 <b>(-44.34%)</b></td><td>477.97 (-18.21%)</td><td>453.86 (-19.41%)</td><td>422.95 <b>(+38.75%)</b></td><td>64.32 <b>(-77.22%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>4.00 (n/a)</td><td>2.23 (n/a)</td><td>2.15 (n/a)</td><td>1.16 (n/a)</td><td>1.08 (n/a)</td><td>6934.70 (n/a)</td><td>4263.16 (n/a)</td><td>3753.50 (n/a)</td><td>2016.80 (n/a)</td><td>1824.69 (n/a)</td><td>1048.17 (n/a)</td><td>584.36 (n/a)</td><td>563.19 (n/a)</td><td>304.83 (n/a)</td><td>282.35 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.28 (-4.11%)</td><td>0.21 (-5.07%)</td><td>0.20 (-4.66%)</td><td>0.16 (-13.13%)</td><td>0.05 (+13.95%)</td><td>7976.60 (+15.11%)</td><td>6219.06 (+7.12%)</td><td>6088.00 (+4.89%)</td><td>4397.20 (+4.29%)</td><td>1431.63 <b>(+42.18%)</b></td><td>15.26 (-4.11%)</td><td>11.28 (-5.07%)</td><td>11.02 (-4.66%)</td><td>8.41 (-13.13%)</td><td>2.72 (+13.95%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>6929.40 (n/a)</td><td>5805.76 (n/a)</td><td>5804.40 (n/a)</td><td>4216.50 (n/a)</td><td>1006.93 (n/a)</td><td>15.92 (n/a)</td><td>11.89 (n/a)</td><td>11.56 (n/a)</td><td>9.68 (n/a)</td><td>2.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>3.92 (n/a)</td><td>3.75 (n/a)</td><td>3.82 (n/a)</td><td>3.45 (n/a)</td><td>0.18 (n/a)</td><td>3.92 (n/a)</td><td>3.75 (n/a)</td><td>3.82 (n/a)</td><td>3.45 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>7.44 (+12.28%)</td><td>6.40 (+8.95%)</td><td>6.29 (+6.04%)</td><td>5.55 (+9.34%)</td><td>0.69 <b>(+21.33%)</b></td><td>7.43 (+12.28%)</td><td>6.39 (+8.95%)</td><td>6.29 (+6.04%)</td><td>5.54 (+9.34%)</td><td>0.69 <b>(+21.33%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>6.62 (n/a)</td><td>5.87 (n/a)</td><td>5.93 (n/a)</td><td>5.07 (n/a)</td><td>0.57 (n/a)</td><td>6.62 (n/a)</td><td>5.87 (n/a)</td><td>5.93 (n/a)</td><td>5.07 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>13.99 (-2.92%)</td><td>11.37 (+11.05%)</td><td>10.13 (+5.59%)</td><td>9.78 <b>(+33.19%)</b></td><td>2.02 <b>(-34.04%)</b></td><td>13.98 (-2.92%)</td><td>11.36 (+11.05%)</td><td>10.12 (+5.59%)</td><td>9.77 <b>(+33.19%)</b></td><td>2.02 <b>(-34.04%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>14.41 (n/a)</td><td>10.24 (n/a)</td><td>9.59 (n/a)</td><td>7.34 (n/a)</td><td>3.06 (n/a)</td><td>14.40 (n/a)</td><td>10.23 (n/a)</td><td>9.59 (n/a)</td><td>7.34 (n/a)</td><td>3.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>3.81 (n/a)</td><td>3.65 (n/a)</td><td>3.73 (n/a)</td><td>3.40 (n/a)</td><td>0.18 (n/a)</td><td>3.81 (n/a)</td><td>3.64 (n/a)</td><td>3.73 (n/a)</td><td>3.40 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>7.41 (-0.16%)</td><td>6.72 (+1.50%)</td><td>6.78 (-1.50%)</td><td>5.99 (+3.79%)</td><td>0.53 <b>(-33.11%)</b></td><td>7.40 (-0.16%)</td><td>6.71 (+1.50%)</td><td>6.78 (-1.50%)</td><td>5.98 (+3.79%)</td><td>0.53 <b>(-33.11%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>7.42 (n/a)</td><td>6.62 (n/a)</td><td>6.89 (n/a)</td><td>5.77 (n/a)</td><td>0.79 (n/a)</td><td>7.42 (n/a)</td><td>6.61 (n/a)</td><td>6.88 (n/a)</td><td>5.77 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>14.14 (+0.03%)</td><td>9.40 (-10.12%)</td><td>8.96 (+4.93%)</td><td>6.33 (-18.20%)</td><td>2.91 (-6.82%)</td><td>14.13 (+0.03%)</td><td>9.39 (-10.12%)</td><td>8.95 (+4.93%)</td><td>6.32 (-18.20%)</td><td>2.91 (-6.82%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>14.14 (n/a)</td><td>10.46 (n/a)</td><td>8.53 (n/a)</td><td>7.73 (n/a)</td><td>3.13 (n/a)</td><td>14.13 (n/a)</td><td>10.45 (n/a)</td><td>8.53 (n/a)</td><td>7.73 (n/a)</td><td>3.13 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>2.88 (-7.52%)</td><td>2.61 (+13.91%)</td><td>2.77 (-8.66%)</td><td>1.94 <b>(+85.95%)</b></td><td>0.38 <b>(-64.19%)</b></td><td>2.87 (-7.52%)</td><td>2.60 (+13.91%)</td><td>2.76 (-8.66%)</td><td>1.93 <b>(+85.95%)</b></td><td>0.38 <b>(-64.19%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>3.11 (n/a)</td><td>2.29 (n/a)</td><td>3.03 (n/a)</td><td>1.04 (n/a)</td><td>1.07 (n/a)</td><td>3.10 (n/a)</td><td>2.28 (n/a)</td><td>3.02 (n/a)</td><td>1.04 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.52 (-8.94%)</td><td>0.31 <b>(-30.93%)</b></td><td>0.39 (-4.99%)</td><td>0.07 <b>(-80.21%)</b></td><td>0.22 <b>(+148.23%)</b></td><td>0.51 (-8.94%)</td><td>0.31 <b>(-30.93%)</b></td><td>0.39 (-4.99%)</td><td>0.07 <b>(-80.21%)</b></td><td>0.22 <b>(+148.23%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.57 (n/a)</td><td>0.46 (n/a)</td><td>0.42 (n/a)</td><td>0.37 (n/a)</td><td>0.09 (n/a)</td><td>0.56 (n/a)</td><td>0.45 (n/a)</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.73 (+9.01%)</td><td>0.31 (-5.85%)</td><td>0.31 (-18.76%)</td><td>0.08 (-9.28%)</td><td>0.27 (+13.09%)</td><td>0.73 (+9.01%)</td><td>0.31 (-5.85%)</td><td>0.31 (-18.76%)</td><td>0.08 (-9.28%)</td><td>0.27 (+13.09%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.67 (n/a)</td><td>0.33 (n/a)</td><td>0.39 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td><td>0.67 (n/a)</td><td>0.33 (n/a)</td><td>0.38 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>2.13 (-16.48%)</td><td>1.62 (-13.60%)</td><td>1.86 (-15.04%)</td><td>0.45 (+1.70%)</td><td>0.68 <b>(-22.62%)</b></td><td>2.10 (-16.48%)</td><td>1.59 (-13.60%)</td><td>1.83 (-15.04%)</td><td>0.44 (+1.70%)</td><td>0.67 <b>(-22.62%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>2.55 (n/a)</td><td>1.87 (n/a)</td><td>2.18 (n/a)</td><td>0.44 (n/a)</td><td>0.87 (n/a)</td><td>2.51 (n/a)</td><td>1.84 (n/a)</td><td>2.15 (n/a)</td><td>0.43 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.00 (n/a)</td><td>408.82 (n/a)</td><td>409.80 (n/a)</td><td>282.20 (n/a)</td><td>120.89 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.30 (n/a)</td><td>364.98 (n/a)</td><td>272.90 (n/a)</td><td>229.70 (n/a)</td><td>154.47 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.40 (n/a)</td><td>463.38 (n/a)</td><td>513.60 (n/a)</td><td>281.20 (n/a)</td><td>158.85 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.70 (n/a)</td><td>383.00 (n/a)</td><td>410.10 (n/a)</td><td>230.10 (n/a)</td><td>127.32 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>475.90 (n/a)</td><td>411.56 (n/a)</td><td>466.60 (n/a)</td><td>209.80 (n/a)</td><td>114.33 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>490.20 (n/a)</td><td>406.86 (n/a)</td><td>429.10 (n/a)</td><td>252.40 (n/a)</td><td>90.28 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 <b>(+26.82%)</b></td><td>0.03 (+6.94%)</td><td>0.02 <b>(-29.25%)</b></td><td>0.02 (+12.21%)</td><td>0.01 <b>(+31.82%)</b></td><td>510.70 (-10.89%)</td><td>367.64 (-4.97%)</td><td>420.90 <b>(+41.34%)</b></td><td>203.10 <b>(-21.13%)</b></td><td>129.41 (-10.59%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>573.10 (n/a)</td><td>386.88 (n/a)</td><td>297.80 (n/a)</td><td>257.50 (n/a)</td><td>144.75 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 <b>(+52.37%)</b></td><td>0.02 <b>(+39.28%)</b></td><td>0.02 (+6.56%)</td><td>0.00 <b>(+26.62%)</b></td><td>0.01 <b>(+69.24%)</b></td><td>1960.20 <b>(-21.03%)</b></td><td>667.86 <b>(-21.59%)</b></td><td>433.20 (-6.15%)</td><td>215.00 <b>(-34.37%)</b></td><td>731.14 <b>(-20.04%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2482.10 (n/a)</td><td>851.78 (n/a)</td><td>461.60 (n/a)</td><td>327.60 (n/a)</td><td>914.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (+4.56%)</td><td>0.02 (-11.16%)</td><td>0.02 <b>(-23.01%)</b></td><td>0.01 <b>(-26.19%)</b></td><td>0.01 <b>(+69.63%)</b></td><td>575.70 <b>(+35.46%)</b></td><td>404.74 <b>(+22.93%)</b></td><td>376.20 <b>(+29.90%)</b></td><td>250.50 (-4.39%)</td><td>155.84 <b>(+119.81%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>425.00 (n/a)</td><td>329.24 (n/a)</td><td>289.60 (n/a)</td><td>262.00 (n/a)</td><td>70.90 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (-12.64%)</td><td>0.02 (-17.75%)</td><td>0.02 <b>(-31.45%)</b></td><td>0.01 <b>(+261.37%)</b></td><td>0.01 <b>(-44.72%)</b></td><td>595.40 <b>(-72.33%)</b></td><td>399.94 <b>(-36.69%)</b></td><td>401.80 <b>(+45.84%)</b></td><td>241.00 (+14.49%)</td><td>132.62 <b>(-84.40%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2151.70 (n/a)</td><td>631.74 (n/a)</td><td>275.50 (n/a)</td><td>210.50 (n/a)</td><td>850.33 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 <b>(+32.61%)</b></td><td>0.03 <b>(+31.58%)</b></td><td>0.03 <b>(+54.68%)</b></td><td>0.02 (+3.02%)</td><td>0.01 <b>(+110.52%)</b></td><td>520.90 (-2.93%)</td><td>343.52 (-16.82%)</td><td>269.80 <b>(-35.35%)</b></td><td>219.00 <b>(-24.61%)</b></td><td>142.74 <b>(+59.87%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>536.60 (n/a)</td><td>413.00 (n/a)</td><td>417.30 (n/a)</td><td>290.50 (n/a)</td><td>89.28 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (-3.67%)</td><td>0.02 (-11.10%)</td><td>0.02 (+0.46%)</td><td>0.00 <b>(-70.44%)</b></td><td>0.01 <b>(+64.86%)</b></td><td>2028.30 <b>(+238.28%)</b></td><td>762.40 <b>(+59.45%)</b></td><td>505.40 (-0.45%)</td><td>337.90 (+3.81%)</td><td>711.17 <b>(+577.79%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>599.60 (n/a)</td><td>478.14 (n/a)</td><td>507.70 (n/a)</td><td>325.50 (n/a)</td><td>104.93 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (-3.81%)</td><td>0.02 (-12.35%)</td><td>0.02 <b>(-36.42%)</b></td><td>0.02 <b>(+149.36%)</b></td><td>0.01 <b>(-45.74%)</b></td><td>537.20 <b>(-59.90%)</b></td><td>459.80 (-15.23%)</td><td>496.40 <b>(+57.29%)</b></td><td>289.70 (+3.95%)</td><td>99.49 <b>(-78.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1339.50 (n/a)</td><td>542.40 (n/a)</td><td>315.60 (n/a)</td><td>278.70 (n/a)</td><td>454.36 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 <b>(+48.29%)</b></td><td>0.02 (+6.63%)</td><td>0.02 (+4.90%)</td><td>0.01 (-18.78%)</td><td>0.01 <b>(+270.37%)</b></td><td>687.30 <b>(+23.11%)</b></td><td>496.76 (+3.83%)</td><td>433.40 (-4.66%)</td><td>283.90 <b>(-32.58%)</b></td><td>179.00 <b>(+227.71%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.30 (n/a)</td><td>478.42 (n/a)</td><td>454.60 (n/a)</td><td>421.10 (n/a)</td><td>54.62 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (-18.75%)</td><td>0.02 (-2.73%)</td><td>0.02 (-12.38%)</td><td>0.01 <b>(+178.79%)</b></td><td>0.01 <b>(-39.49%)</b></td><td>683.40 <b>(-64.13%)</b></td><td>473.62 <b>(-31.64%)</b></td><td>496.00 (+14.13%)</td><td>255.50 <b>(+23.07%)</b></td><td>154.67 <b>(-77.47%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1905.30 (n/a)</td><td>692.88 (n/a)</td><td>434.60 (n/a)</td><td>207.60 (n/a)</td><td>686.61 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (-12.18%)</td><td>0.02 (+4.48%)</td><td>0.02 (+15.77%)</td><td>0.02 <b>(+24.51%)</b></td><td>0.01 <b>(-32.72%)</b></td><td>517.30 (-19.69%)</td><td>440.38 (-10.10%)</td><td>458.00 (-13.62%)</td><td>275.40 (+13.90%)</td><td>96.83 <b>(-35.35%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>644.10 (n/a)</td><td>489.86 (n/a)</td><td>530.20 (n/a)</td><td>241.80 (n/a)</td><td>149.77 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 <b>(+48.92%)</b></td><td>0.02 <b>(+50.50%)</b></td><td>0.02 <b>(+53.79%)</b></td><td>0.02 <b>(+105.61%)</b></td><td>0.01 <b>(+35.76%)</b></td><td>515.20 <b>(-51.36%)</b></td><td>383.50 <b>(-36.39%)</b></td><td>347.80 <b>(-34.98%)</b></td><td>286.10 <b>(-32.86%)</b></td><td>108.18 <b>(-58.40%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1059.30 (n/a)</td><td>602.90 (n/a)</td><td>534.90 (n/a)</td><td>426.10 (n/a)</td><td>260.01 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 <b>(+65.65%)</b></td><td>0.02 <b>(+58.21%)</b></td><td>0.03 <b>(+68.60%)</b></td><td>0.01 <b>(+86.63%)</b></td><td>0.01 <b>(+82.19%)</b></td><td>1018.60 <b>(-46.42%)</b></td><td>461.64 <b>(-38.45%)</b></td><td>275.20 <b>(-40.69%)</b></td><td>245.70 <b>(-39.63%)</b></td><td>332.10 <b>(-48.51%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1901.10 (n/a)</td><td>750.06 (n/a)</td><td>464.00 (n/a)</td><td>407.00 (n/a)</td><td>645.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (-2.58%)</td><td>0.02 <b>(+26.50%)</b></td><td>0.02 <b>(+55.68%)</b></td><td>0.02 <b>(+25.04%)</b></td><td>0.01 <b>(-23.26%)</b></td><td>471.50 <b>(-20.02%)</b></td><td>353.62 <b>(-24.87%)</b></td><td>333.40 <b>(-35.77%)</b></td><td>245.90 (+2.67%)</td><td>93.26 <b>(-33.34%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.50 (n/a)</td><td>470.66 (n/a)</td><td>519.10 (n/a)</td><td>239.50 (n/a)</td><td>139.90 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 <b>(+33.87%)</b></td><td>0.02 (+9.65%)</td><td>0.02 (-14.15%)</td><td>0.01 (-4.15%)</td><td>0.01 <b>(+80.78%)</b></td><td>610.90 (+4.32%)</td><td>452.52 (-4.89%)</td><td>498.10 (+16.46%)</td><td>285.50 <b>(-25.30%)</b></td><td>129.17 <b>(+34.05%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>585.60 (n/a)</td><td>475.80 (n/a)</td><td>427.70 (n/a)</td><td>382.20 (n/a)</td><td>96.35 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.11 (+13.95%)</td><td>0.09 (+18.85%)</td><td>0.08 (+7.50%)</td><td>0.08 <b>(+38.80%)</b></td><td>0.01 (-14.62%)</td><td>300.80 <b>(-27.95%)</b></td><td>272.68 (-16.95%)</td><td>289.60 (-6.97%)</td><td>233.50 (-12.22%)</td><td>31.65 <b>(-46.50%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>417.50 (n/a)</td><td>328.32 (n/a)</td><td>311.30 (n/a)</td><td>266.00 (n/a)</td><td>59.16 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.16 (+0.79%)</td><td>0.14 (+2.09%)</td><td>0.14 (-0.05%)</td><td>0.11 <b>(+22.87%)</b></td><td>0.02 <b>(-28.55%)</b></td><td>373.10 (-18.61%)</td><td>307.74 (-5.11%)</td><td>284.60 (+0.04%)</td><td>248.40 (-0.80%)</td><td>55.36 <b>(-39.20%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>458.40 (n/a)</td><td>324.32 (n/a)</td><td>284.50 (n/a)</td><td>250.40 (n/a)</td><td>91.05 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 <b>(+33.64%)</b></td><td>0.02 <b>(+45.71%)</b></td><td>0.02 <b>(+50.78%)</b></td><td>0.02 <b>(+85.20%)</b></td><td>0.00 <b>(-46.73%)</b></td><td>289.40 <b>(-46.01%)</b></td><td>271.38 <b>(-34.22%)</b></td><td>274.20 <b>(-33.67%)</b></td><td>234.10 <b>(-25.16%)</b></td><td>22.24 <b>(-77.83%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>536.00 (n/a)</td><td>412.54 (n/a)</td><td>413.40 (n/a)</td><td>312.80 (n/a)</td><td>100.33 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (+4.19%)</td><td>0.02 (-17.75%)</td><td>0.02 <b>(-36.97%)</b></td><td>0.02 (-19.27%)</td><td>0.01 <b>(+70.17%)</b></td><td>492.20 <b>(+23.89%)</b></td><td>391.12 <b>(+29.84%)</b></td><td>468.10 <b>(+58.62%)</b></td><td>228.50 (-3.99%)</td><td>119.79 <b>(+103.07%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>397.30 (n/a)</td><td>301.24 (n/a)</td><td>295.10 (n/a)</td><td>238.00 (n/a)</td><td>58.99 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.05 (+4.33%)</td><td>0.03 (-5.09%)</td><td>0.02 <b>(-37.99%)</b></td><td>0.02 (+6.37%)</td><td>0.02 (+16.74%)</td><td>546.00 (-5.99%)</td><td>405.84 (+7.81%)</td><td>497.50 <b>(+61.26%)</b></td><td>233.00 (-4.15%)</td><td>152.16 (+2.63%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>580.80 (n/a)</td><td>376.44 (n/a)</td><td>308.50 (n/a)</td><td>243.10 (n/a)</td><td>148.26 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (-3.54%)</td><td>0.03 (+1.74%)</td><td>0.02 (-6.65%)</td><td>0.02 <b>(+25.93%)</b></td><td>0.01 (-3.59%)</td><td>524.20 <b>(-20.59%)</b></td><td>358.84 (-5.00%)</td><td>338.50 (+7.12%)</td><td>222.00 (+3.64%)</td><td>136.85 <b>(-23.16%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>660.10 (n/a)</td><td>377.72 (n/a)</td><td>316.00 (n/a)</td><td>214.20 (n/a)</td><td>178.09 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (+1.57%)</td><td>0.03 <b>(+37.28%)</b></td><td>0.04 <b>(+88.79%)</b></td><td>0.02 (-13.32%)</td><td>0.01 (+10.77%)</td><td>638.00 (+15.37%)</td><td>343.36 <b>(-23.88%)</b></td><td>257.50 <b>(-47.03%)</b></td><td>229.10 (-1.55%)</td><td>171.26 <b>(+36.56%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>553.00 (n/a)</td><td>451.06 (n/a)</td><td>486.10 (n/a)</td><td>232.70 (n/a)</td><td>125.41 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (-14.74%)</td><td>0.02 (-5.06%)</td><td>0.03 <b>(+34.72%)</b></td><td>0.01 (-17.76%)</td><td>0.01 <b>(-25.41%)</b></td><td>644.60 <b>(+21.60%)</b></td><td>392.80 (+3.32%)</td><td>314.50 <b>(-25.77%)</b></td><td>271.50 (+17.33%)</td><td>154.49 (+12.86%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.10 (n/a)</td><td>380.18 (n/a)</td><td>423.70 (n/a)</td><td>231.40 (n/a)</td><td>136.89 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.06 <b>(+39.11%)</b></td><td>0.03 <b>(+24.82%)</b></td><td>0.02 (-2.51%)</td><td>0.02 (+13.21%)</td><td>0.02 <b>(+76.64%)</b></td><td>547.10 (-11.66%)</td><td>395.80 (-12.39%)</td><td>464.30 (+2.59%)</td><td>186.00 <b>(-28.10%)</b></td><td>159.85 (+19.93%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>619.30 (n/a)</td><td>451.76 (n/a)</td><td>452.60 (n/a)</td><td>258.70 (n/a)</td><td>133.28 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (+0.17%)</td><td>0.02 (+9.74%)</td><td>0.02 (+9.75%)</td><td>0.02 (+18.08%)</td><td>0.01 (-8.75%)</td><td>542.00 (-15.31%)</td><td>432.70 (-10.55%)</td><td>479.30 (-8.90%)</td><td>294.90 (-0.17%)</td><td>104.23 <b>(-20.97%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>640.00 (n/a)</td><td>483.72 (n/a)</td><td>526.10 (n/a)</td><td>295.40 (n/a)</td><td>131.87 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (+18.38%)</td><td>0.02 (+13.75%)</td><td>0.02 (-0.28%)</td><td>0.01 <b>(+33.91%)</b></td><td>0.01 <b>(+22.00%)</b></td><td>818.90 <b>(-25.32%)</b></td><td>491.60 (-13.23%)</td><td>496.90 (+0.28%)</td><td>209.60 (-15.52%)</td><td>230.98 <b>(-27.27%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1096.60 (n/a)</td><td>566.58 (n/a)</td><td>495.50 (n/a)</td><td>248.10 (n/a)</td><td>317.59 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 <b>(-30.59%)</b></td><td>0.02 <b>(-33.89%)</b></td><td>0.02 (-5.42%)</td><td>0.00 <b>(-72.11%)</b></td><td>0.01 <b>(-24.40%)</b></td><td>2071.40 <b>(+258.56%)</b></td><td>779.50 <b>(+98.38%)</b></td><td>487.20 (+5.73%)</td><td>275.20 <b>(+44.08%)</b></td><td>732.07 <b>(+348.79%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.70 (n/a)</td><td>392.94 (n/a)</td><td>460.80 (n/a)</td><td>191.00 (n/a)</td><td>163.12 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (-17.43%)</td><td>0.02 (-14.81%)</td><td>0.02 (-6.96%)</td><td>0.00 <b>(-71.17%)</b></td><td>0.01 <b>(+37.71%)</b></td><td>1917.20 <b>(+246.88%)</b></td><td>726.58 <b>(+64.86%)</b></td><td>495.10 (+7.49%)</td><td>334.90 <b>(+21.08%)</b></td><td>670.70 <b>(+559.91%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>552.70 (n/a)</td><td>440.72 (n/a)</td><td>460.60 (n/a)</td><td>276.60 (n/a)</td><td>101.64 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (+2.49%)</td><td>0.03 (+13.23%)</td><td>0.02 <b>(+26.84%)</b></td><td>0.01 (-13.94%)</td><td>0.01 (+16.25%)</td><td>569.50 (+16.18%)</td><td>360.22 (-8.80%)</td><td>336.10 <b>(-21.16%)</b></td><td>236.00 (-2.44%)</td><td>133.16 <b>(+32.84%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>490.20 (n/a)</td><td>394.96 (n/a)</td><td>426.30 (n/a)</td><td>241.90 (n/a)</td><td>100.24 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.35 (+2.89%)</td><td>0.28 <b>(+22.32%)</b></td><td>0.33 <b>(+37.32%)</b></td><td>0.16 <b>(+182.09%)</b></td><td>0.08 <b>(-29.62%)</b></td><td>615.80 <b>(-64.55%)</b></td><td>385.58 <b>(-41.71%)</b></td><td>301.90 <b>(-27.18%)</b></td><td>277.60 (-2.80%)</td><td>144.77 <b>(-76.38%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.34 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>0.12 (n/a)</td><td>1737.10 (n/a)</td><td>661.44 (n/a)</td><td>414.60 (n/a)</td><td>285.60 (n/a)</td><td>612.90 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.43 (+13.01%)</td><td>0.27 (+11.03%)</td><td>0.19 (-3.93%)</td><td>0.15 (-14.55%)</td><td>0.12 <b>(+51.10%)</b></td><td>646.00 (+17.03%)</td><td>436.54 (-1.51%)</td><td>508.70 (+4.09%)</td><td>231.10 (-11.52%)</td><td>181.45 <b>(+49.25%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.38 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>552.00 (n/a)</td><td>443.22 (n/a)</td><td>488.70 (n/a)</td><td>261.20 (n/a)</td><td>121.58 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.41 (+13.23%)</td><td>0.29 (+14.87%)</td><td>0.25 (+14.10%)</td><td>0.17 (-12.43%)</td><td>0.10 <b>(+52.78%)</b></td><td>563.80 (+14.20%)</td><td>377.06 (-8.06%)</td><td>388.30 (-12.37%)</td><td>240.30 (-11.69%)</td><td>132.07 <b>(+51.75%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.36 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>493.70 (n/a)</td><td>410.10 (n/a)</td><td>443.10 (n/a)</td><td>272.10 (n/a)</td><td>87.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.29 (+6.08%)</td><td>0.25 <b>(+27.48%)</b></td><td>0.26 <b>(+58.68%)</b></td><td>0.15 (+4.08%)</td><td>0.06 (-1.09%)</td><td>492.30 (-3.92%)</td><td>313.18 <b>(-21.92%)</b></td><td>281.60 <b>(-36.99%)</b></td><td>250.60 (-5.75%)</td><td>101.13 (-6.34%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>512.40 (n/a)</td><td>401.10 (n/a)</td><td>446.90 (n/a)</td><td>265.90 (n/a)</td><td>107.97 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.30 (+5.56%)</td><td>0.19 (-5.39%)</td><td>0.14 (-18.95%)</td><td>0.12 (-16.99%)</td><td>0.08 <b>(+35.75%)</b></td><td>620.60 <b>(+20.46%)</b></td><td>446.00 (+13.17%)</td><td>528.50 <b>(+23.37%)</b></td><td>246.30 (-5.27%)</td><td>166.11 <b>(+54.42%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>515.20 (n/a)</td><td>394.08 (n/a)</td><td>428.40 (n/a)</td><td>260.00 (n/a)</td><td>107.57 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.33 <b>(+89.76%)</b></td><td>0.27 <b>(+101.15%)</b></td><td>0.29 <b>(+86.28%)</b></td><td>0.16 <b>(+409.98%)</b></td><td>0.07 (+11.21%)</td><td>470.70 <b>(-80.39%)</b></td><td>295.58 <b>(-65.49%)</b></td><td>255.30 <b>(-46.32%)</b></td><td>224.70 <b>(-47.32%)</b></td><td>99.63 <b>(-88.47%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.06 (n/a)</td><td>2400.30 (n/a)</td><td>856.42 (n/a)</td><td>475.60 (n/a)</td><td>426.50 (n/a)</td><td>864.29 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.44 (+0.28%)</td><td>0.32 (-0.06%)</td><td>0.25 (-2.52%)</td><td>0.23 (-4.32%)</td><td>0.11 (+14.76%)</td><td>575.70 (+4.52%)</td><td>454.14 (+2.33%)</td><td>516.80 (+2.58%)</td><td>295.70 (-0.30%)</td><td>139.75 (+18.13%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.09 (n/a)</td><td>550.80 (n/a)</td><td>443.82 (n/a)</td><td>503.80 (n/a)</td><td>296.60 (n/a)</td><td>118.30 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.40 (-9.91%)</td><td>0.29 (-9.43%)</td><td>0.26 <b>(-30.46%)</b></td><td>0.19 (+3.49%)</td><td>0.08 <b>(-28.43%)</b></td><td>685.30 (-3.38%)</td><td>479.10 (+4.46%)</td><td>495.50 <b>(+43.79%)</b></td><td>331.60 (+11.01%)</td><td>139.08 <b>(-25.35%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.38 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>709.30 (n/a)</td><td>458.64 (n/a)</td><td>344.60 (n/a)</td><td>298.70 (n/a)</td><td>186.31 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.40 <b>(+25.47%)</b></td><td>0.27 <b>(+20.72%)</b></td><td>0.25 (-8.13%)</td><td>0.19 <b>(+403.15%)</b></td><td>0.08 <b>(-27.13%)</b></td><td>681.20 <b>(-80.13%)</b></td><td>515.18 <b>(-52.35%)</b></td><td>530.90 (+8.84%)</td><td>325.30 <b>(-20.31%)</b></td><td>130.61 <b>(-90.06%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.27 (n/a)</td><td>0.04 (n/a)</td><td>0.11 (n/a)</td><td>3427.70 (n/a)</td><td>1081.14 (n/a)</td><td>487.80 (n/a)</td><td>408.20 (n/a)</td><td>1313.64 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 <b>(+37.54%)</b></td><td>0.02 <b>(+23.85%)</b></td><td>0.02 <b>(+20.60%)</b></td><td>0.01 (+11.75%)</td><td>0.00 <b>(+52.24%)</b></td><td>475.00 (-10.51%)</td><td>292.64 (-17.11%)</td><td>254.80 (-17.08%)</td><td>217.60 <b>(-27.27%)</b></td><td>103.91 (+3.82%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.80 (n/a)</td><td>353.06 (n/a)</td><td>307.30 (n/a)</td><td>299.20 (n/a)</td><td>100.09 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 <b>(+24.37%)</b></td><td>0.01 (+8.29%)</td><td>0.01 (+9.51%)</td><td>0.01 (-5.60%)</td><td>0.00 <b>(+71.30%)</b></td><td>527.60 (+5.94%)</td><td>346.38 (-2.91%)</td><td>309.70 (-8.70%)</td><td>234.40 (-19.59%)</td><td>119.73 <b>(+43.57%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>498.00 (n/a)</td><td>356.78 (n/a)</td><td>339.20 (n/a)</td><td>291.50 (n/a)</td><td>83.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.01 (-10.83%)</td><td>0.01 <b>(-25.17%)</b></td><td>0.01 <b>(-31.12%)</b></td><td>0.01 <b>(-23.87%)</b></td><td>0.00 (+7.28%)</td><td>619.10 <b>(+31.36%)</b></td><td>471.18 <b>(+36.82%)</b></td><td>454.80 <b>(+45.16%)</b></td><td>289.90 (+12.15%)</td><td>122.52 <b>(+49.57%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>471.30 (n/a)</td><td>344.38 (n/a)</td><td>313.30 (n/a)</td><td>258.50 (n/a)</td><td>81.91 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.51 (-13.49%)</td><td>0.33 <b>(-25.80%)</b></td><td>0.27 <b>(-40.76%)</b></td><td>0.26 <b>(-25.54%)</b></td><td>0.11 (+11.67%)</td><td>507.20 <b>(+34.32%)</b></td><td>427.36 <b>(+39.27%)</b></td><td>488.60 <b>(+68.77%)</b></td><td>256.80 (+15.62%)</td><td>109.57 <b>(+73.74%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.59 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.35 (n/a)</td><td>0.10 (n/a)</td><td>377.60 (n/a)</td><td>306.86 (n/a)</td><td>289.50 (n/a)</td><td>222.10 (n/a)</td><td>63.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.51 (+6.92%)</td><td>0.45 <b>(+22.22%)</b></td><td>0.49 <b>(+47.49%)</b></td><td>0.27 (+0.45%)</td><td>0.10 (-2.22%)</td><td>486.20 (-0.45%)</td><td>310.40 (-18.40%)</td><td>268.60 <b>(-32.19%)</b></td><td>257.30 (-6.47%)</td><td>98.43 (-2.99%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.48 (n/a)</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>488.40 (n/a)</td><td>380.40 (n/a)</td><td>396.10 (n/a)</td><td>275.10 (n/a)</td><td>101.46 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.63 <b>(+34.56%)</b></td><td>0.40 <b>(+30.36%)</b></td><td>0.28 (+1.22%)</td><td>0.24 <b>(+223.44%)</b></td><td>0.18 (+8.89%)</td><td>542.60 <b>(-69.08%)</b></td><td>386.26 <b>(-42.24%)</b></td><td>467.80 (-1.20%)</td><td>210.70 <b>(-25.71%)</b></td><td>151.02 <b>(-75.57%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.47 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.08 (n/a)</td><td>0.16 (n/a)</td><td>1755.10 (n/a)</td><td>668.76 (n/a)</td><td>473.50 (n/a)</td><td>283.60 (n/a)</td><td>618.16 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.49 (+6.28%)</td><td>0.37 (-0.11%)</td><td>0.32 (-9.60%)</td><td>0.29 (+0.29%)</td><td>0.09 <b>(+33.16%)</b></td><td>453.30 (-0.29%)</td><td>369.28 (+1.94%)</td><td>406.50 (+10.64%)</td><td>267.90 (-5.90%)</td><td>83.82 <b>(+24.95%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.46 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.07 (n/a)</td><td>454.60 (n/a)</td><td>362.26 (n/a)</td><td>367.40 (n/a)</td><td>284.70 (n/a)</td><td>67.08 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.55 (+3.42%)</td><td>0.47 <b>(+41.66%)</b></td><td>0.51 <b>(+66.72%)</b></td><td>0.27 <b>(+20.54%)</b></td><td>0.11 (-2.17%)</td><td>498.00 (-17.04%)</td><td>303.34 <b>(-30.13%)</b></td><td>260.30 <b>(-40.02%)</b></td><td>242.20 (-3.31%)</td><td>109.08 (-14.24%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.53 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>600.30 (n/a)</td><td>434.16 (n/a)</td><td>434.00 (n/a)</td><td>250.50 (n/a)</td><td>127.19 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (-1.11%)</td><td>0.01 (-14.96%)</td><td>0.01 (-12.59%)</td><td>0.01 (+7.48%)</td><td>0.00 (-18.90%)</td><td>532.00 (-6.96%)</td><td>457.12 (+13.18%)</td><td>494.40 (+14.42%)</td><td>258.60 (+1.13%)</td><td>112.76 <b>(-21.21%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>571.80 (n/a)</td><td>403.88 (n/a)</td><td>432.10 (n/a)</td><td>255.70 (n/a)</td><td>143.11 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (+8.14%)</td><td>0.01 (-3.73%)</td><td>0.01 (+1.83%)</td><td>0.01 <b>(-25.80%)</b></td><td>0.00 <b>(+82.84%)</b></td><td>621.70 <b>(+34.77%)</b></td><td>398.48 (+12.89%)</td><td>314.00 (-1.81%)</td><td>271.60 (-7.52%)</td><td>157.29 <b>(+123.32%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>461.30 (n/a)</td><td>352.98 (n/a)</td><td>319.80 (n/a)</td><td>293.70 (n/a)</td><td>70.43 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.00 (+0.00%)</td><td>0.00 (-17.39%)</td><td>0.00 <b>(-40.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-13.63%)</td><td>17162.77 (-6.86%)</td><td>12820.93 (+14.31%)</td><td>15978.49 <b>(+83.80%)</b></td><td>6276.50 (+11.80%)</td><td>5308.43 (-13.19%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18427.01 (n/a)</td><td>11215.44 (n/a)</td><td>8693.58 (n/a)</td><td>5613.99 (n/a)</td><td>6114.91 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.00 (+0.00%)</td><td>0.00 (-19.51%)</td><td>0.00 (-16.67%)</td><td>0.00 (+0.00%)</td><td>0.00 (-6.13%)</td><td>19036.65 (+2.27%)</td><td>15101.64 (+18.77%)</td><td>17490.54 <b>(+22.91%)</b></td><td>5923.10 (+0.58%)</td><td>5477.81 (-10.31%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18613.79 (n/a)</td><td>12715.00 (n/a)</td><td>14230.03 (n/a)</td><td>5888.93 (n/a)</td><td>6107.68 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.13 (-10.17%)</td><td>0.09 (-16.57%)</td><td>0.08 <b>(-22.68%)</b></td><td>0.08 (-2.02%)</td><td>0.02 <b>(-26.50%)</b></td><td>26982.14 (+2.05%)</td><td>23253.69 (+17.23%)</td><td>25420.22 <b>(+29.32%)</b></td><td>15932.03 (+11.27%)</td><td>4436.51 (-16.50%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>26440.05 (n/a)</td><td>19835.79 (n/a)</td><td>19657.22 (n/a)</td><td>14318.72 (n/a)</td><td>5313.50 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.61 (+8.10%)</td><td>0.95 (-8.50%)</td><td>1.42 <b>(+38.81%)</b></td><td>0.15 <b>(-77.78%)</b></td><td>0.73 <b>(+154.50%)</b></td><td>3459.60 <b>(+349.94%)</b></td><td>1561.14 <b>(+191.74%)</b></td><td>368.90 <b>(-27.96%)</b></td><td>326.60 (-7.50%)</td><td>1653.67 <b>(+1007.31%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.48 (n/a)</td><td>1.04 (n/a)</td><td>1.02 (n/a)</td><td>0.68 (n/a)</td><td>0.29 (n/a)</td><td>768.90 (n/a)</td><td>535.12 (n/a)</td><td>512.10 (n/a)</td><td>353.10 (n/a)</td><td>149.34 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>2.71 (+13.35%)</td><td>1.41 (-10.46%)</td><td>1.17 <b>(-25.89%)</b></td><td>0.30 (-8.50%)</td><td>1.17 <b>(+49.26%)</b></td><td>3457.50 (+9.29%)</td><td>1681.72 <b>(+53.98%)</b></td><td>896.70 <b>(+34.94%)</b></td><td>386.60 (-11.78%)</td><td>1545.66 <b>(+32.92%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>2.39 (n/a)</td><td>1.58 (n/a)</td><td>1.58 (n/a)</td><td>0.33 (n/a)</td><td>0.79 (n/a)</td><td>3163.70 (n/a)</td><td>1092.18 (n/a)</td><td>664.50 (n/a)</td><td>438.20 (n/a)</td><td>1162.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.77 (-19.98%)</td><td>1.32 (+9.73%)</td><td>1.50 <b>(+45.42%)</b></td><td>0.74 <b>(+186.80%)</b></td><td>0.50 <b>(-32.31%)</b></td><td>704.20 <b>(-65.13%)</b></td><td>455.16 <b>(-37.74%)</b></td><td>350.50 <b>(-31.23%)</b></td><td>295.50 <b>(+24.95%)</b></td><td>194.59 <b>(-73.41%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>2.22 (n/a)</td><td>1.20 (n/a)</td><td>1.03 (n/a)</td><td>0.26 (n/a)</td><td>0.73 (n/a)</td><td>2019.60 (n/a)</td><td>731.06 (n/a)</td><td>509.70 (n/a)</td><td>236.50 (n/a)</td><td>731.72 (n/a)</td>
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
