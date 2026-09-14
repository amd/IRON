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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.05 (-16.84%)</td><td>0.04 (-10.82%)</td><td>0.04 (-13.80%)</td><td>0.02 <b>(+278.97%)</b></td><td>0.01 <b>(-49.07%)</b></td><td>510.70 <b>(-73.61%)</b></td><td>341.92 <b>(-40.54%)</b></td><td>284.40 (+15.99%)</td><td>244.50 <b>(+20.27%)</b></td><td>110.56 <b>(-85.46%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1935.40 (n/a)</td><td>575.08 (n/a)</td><td>245.20 (n/a)</td><td>203.30 (n/a)</td><td>760.66 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.05 (-4.64%)</td><td>0.03 <b>(-35.42%)</b></td><td>0.03 <b>(-37.67%)</b></td><td>0.01 <b>(-73.06%)</b></td><td>0.02 <b>(+243.93%)</b></td><td>1053.60 <b>(+271.12%)</b></td><td>483.30 <b>(+99.83%)</b></td><td>373.10 <b>(+60.47%)</b></td><td>239.20 (+4.87%)</td><td>329.91 <b>(+1298.30%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>283.90 (n/a)</td><td>241.86 (n/a)</td><td>232.50 (n/a)</td><td>228.10 (n/a)</td><td>23.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.07 (-6.01%)</td><td>0.04 (-14.09%)</td><td>0.04 <b>(-21.01%)</b></td><td>0.02 (+2.37%)</td><td>0.02 (+9.49%)</td><td>651.80 (-2.32%)</td><td>399.74 <b>(+21.72%)</b></td><td>316.30 <b>(+26.62%)</b></td><td>188.50 (+6.38%)</td><td>215.08 (+10.67%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>667.30 (n/a)</td><td>328.42 (n/a)</td><td>249.80 (n/a)</td><td>177.20 (n/a)</td><td>194.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (-15.92%)</td><td>0.02 (-3.80%)</td><td>0.02 (+3.91%)</td><td>0.01 <b>(+25.97%)</b></td><td>0.00 <b>(-39.11%)</b></td><td>416.20 <b>(-20.60%)</b></td><td>310.72 (-2.67%)</td><td>288.90 (-3.73%)</td><td>230.40 (+18.89%)</td><td>69.60 <b>(-43.82%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>524.20 (n/a)</td><td>319.24 (n/a)</td><td>300.10 (n/a)</td><td>193.80 (n/a)</td><td>123.88 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (-7.07%)</td><td>0.01 (-4.06%)</td><td>0.01 (+3.31%)</td><td>0.01 (-10.20%)</td><td>0.01 (+1.77%)</td><td>572.00 (+11.37%)</td><td>403.24 (+6.38%)</td><td>390.50 (-3.20%)</td><td>251.20 (+7.58%)</td><td>141.39 <b>(+23.33%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>513.60 (n/a)</td><td>379.06 (n/a)</td><td>403.40 (n/a)</td><td>233.50 (n/a)</td><td>114.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 <b>(-39.55%)</b></td><td>0.01 (-15.05%)</td><td>0.01 (-1.78%)</td><td>0.01 <b>(-26.66%)</b></td><td>0.01 <b>(-49.75%)</b></td><td>600.70 <b>(+36.37%)</b></td><td>393.58 (+9.04%)</td><td>423.00 (+1.81%)</td><td>236.70 <b>(+65.41%)</b></td><td>142.84 (+15.14%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>440.50 (n/a)</td><td>360.94 (n/a)</td><td>415.50 (n/a)</td><td>143.10 (n/a)</td><td>124.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (-4.00%)</td><td>0.02 <b>(+30.36%)</b></td><td>0.02 <b>(+56.80%)</b></td><td>0.01 <b>(+28.48%)</b></td><td>0.00 (-16.53%)</td><td>530.80 <b>(-22.17%)</b></td><td>366.20 <b>(-27.34%)</b></td><td>296.10 <b>(-36.23%)</b></td><td>253.60 (+4.19%)</td><td>123.34 <b>(-31.83%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>682.00 (n/a)</td><td>503.96 (n/a)</td><td>464.30 (n/a)</td><td>243.40 (n/a)</td><td>180.94 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (+8.59%)</td><td>0.01 (+2.72%)</td><td>0.01 (+5.63%)</td><td>0.01 <b>(-26.63%)</b></td><td>0.01 <b>(+46.58%)</b></td><td>646.80 <b>(+36.28%)</b></td><td>414.08 (+6.86%)</td><td>430.90 (-5.32%)</td><td>227.10 (-7.94%)</td><td>178.71 <b>(+68.63%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>474.60 (n/a)</td><td>387.50 (n/a)</td><td>455.10 (n/a)</td><td>246.70 (n/a)</td><td>105.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (+16.60%)</td><td>0.01 <b>(+33.83%)</b></td><td>0.01 <b>(+31.15%)</b></td><td>0.01 <b>(+61.80%)</b></td><td>0.00 (+4.84%)</td><td>495.10 <b>(-38.20%)</b></td><td>393.00 <b>(-27.87%)</b></td><td>411.40 <b>(-23.76%)</b></td><td>274.30 (-14.23%)</td><td>103.06 <b>(-43.24%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>801.10 (n/a)</td><td>544.84 (n/a)</td><td>539.60 (n/a)</td><td>319.80 (n/a)</td><td>181.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.40 (n/a)</td><td>351.82 (n/a)</td><td>280.70 (n/a)</td><td>237.90 (n/a)</td><td>122.49 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>549.20 (n/a)</td><td>335.70 (n/a)</td><td>294.50 (n/a)</td><td>152.10 (n/a)</td><td>160.76 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>661.20 (n/a)</td><td>534.18 (n/a)</td><td>507.60 (n/a)</td><td>428.10 (n/a)</td><td>91.48 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>359.40 (n/a)</td><td>298.68 (n/a)</td><td>298.10 (n/a)</td><td>250.40 (n/a)</td><td>43.30 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.90 (n/a)</td><td>360.94 (n/a)</td><td>360.80 (n/a)</td><td>223.00 (n/a)</td><td>126.03 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.40 (n/a)</td><td>368.00 (n/a)</td><td>356.10 (n/a)</td><td>294.80 (n/a)</td><td>78.42 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.31 (+15.05%)</td><td>0.86 (+2.89%)</td><td>0.77 (-0.91%)</td><td>0.68 (+3.04%)</td><td>0.26 <b>(+40.87%)</b></td><td>676.70 (-2.94%)</td><td>564.72 (-0.71%)</td><td>599.10 (+0.93%)</td><td>350.20 (-13.08%)</td><td>126.23 (+17.22%)</td><td>95.81 (+15.05%)</td><td>62.75 (+2.89%)</td><td>56.01 (-0.91%)</td><td>49.59 (+3.04%)</td><td>18.80 <b>(+40.87%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.14 (n/a)</td><td>0.83 (n/a)</td><td>0.77 (n/a)</td><td>0.66 (n/a)</td><td>0.18 (n/a)</td><td>697.20 (n/a)</td><td>568.74 (n/a)</td><td>593.60 (n/a)</td><td>402.90 (n/a)</td><td>107.68 (n/a)</td><td>83.28 (n/a)</td><td>60.99 (n/a)</td><td>56.53 (n/a)</td><td>48.12 (n/a)</td><td>13.34 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.56 <b>(+30.29%)</b></td><td>1.14 (+16.42%)</td><td>1.17 (+16.77%)</td><td>0.67 (+5.31%)</td><td>0.33 <b>(+53.43%)</b></td><td>976.00 (-5.05%)</td><td>623.02 (-11.28%)</td><td>561.60 (-14.36%)</td><td>421.20 <b>(-23.25%)</b></td><td>215.27 (+12.38%)</td><td>159.33 <b>(+30.29%)</b></td><td>116.81 (+16.42%)</td><td>119.50 (+16.77%)</td><td>68.76 (+5.31%)</td><td>34.06 <b>(+53.43%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.19 (n/a)</td><td>0.98 (n/a)</td><td>1.00 (n/a)</td><td>0.64 (n/a)</td><td>0.22 (n/a)</td><td>1027.90 (n/a)</td><td>702.24 (n/a)</td><td>655.80 (n/a)</td><td>548.80 (n/a)</td><td>191.56 (n/a)</td><td>122.29 (n/a)</td><td>100.34 (n/a)</td><td>102.34 (n/a)</td><td>65.29 (n/a)</td><td>22.20 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.80 (+10.94%)</td><td>1.07 <b>(-25.72%)</b></td><td>1.08 <b>(-26.37%)</b></td><td>0.49 <b>(-60.08%)</b></td><td>0.48 <b>(+224.43%)</b></td><td>1533.30 <b>(+150.50%)</b></td><td>843.50 <b>(+59.47%)</b></td><td>694.70 <b>(+35.82%)</b></td><td>418.50 (-9.86%)</td><td>421.98 <b>(+648.32%)</b></td><td>200.42 (+10.94%)</td><td>118.85 <b>(-25.72%)</b></td><td>120.75 <b>(-26.37%)</b></td><td>54.71 <b>(-60.08%)</b></td><td>53.57 <b>(+224.43%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.62 (n/a)</td><td>1.44 (n/a)</td><td>1.47 (n/a)</td><td>1.23 (n/a)</td><td>0.15 (n/a)</td><td>612.10 (n/a)</td><td>528.94 (n/a)</td><td>511.50 (n/a)</td><td>464.30 (n/a)</td><td>56.39 (n/a)</td><td>180.66 (n/a)</td><td>160.00 (n/a)</td><td>164.00 (n/a)</td><td>137.06 (n/a)</td><td>16.51 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.85 (+13.39%)</td><td>1.37 <b>(+21.79%)</b></td><td>1.18 (-0.82%)</td><td>1.15 <b>(+128.29%)</b></td><td>0.31 <b>(-24.78%)</b></td><td>914.50 <b>(-56.20%)</b></td><td>794.28 <b>(-27.19%)</b></td><td>890.50 (+0.82%)</td><td>566.20 (-11.79%)</td><td>155.02 <b>(-72.89%)</b></td><td>237.07 (+13.39%)</td><td>175.09 <b>(+21.79%)</b></td><td>150.71 (-0.82%)</td><td>146.77 <b>(+128.29%)</b></td><td>39.38 <b>(-24.78%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.63 (n/a)</td><td>1.12 (n/a)</td><td>1.19 (n/a)</td><td>0.50 (n/a)</td><td>0.41 (n/a)</td><td>2087.80 (n/a)</td><td>1090.96 (n/a)</td><td>883.30 (n/a)</td><td>641.90 (n/a)</td><td>571.82 (n/a)</td><td>209.08 (n/a)</td><td>143.77 (n/a)</td><td>151.96 (n/a)</td><td>64.29 (n/a)</td><td>52.35 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.36 <b>(-42.65%)</b></td><td>1.06 <b>(-32.24%)</b></td><td>1.31 (-16.42%)</td><td>0.31 <b>(-62.26%)</b></td><td>0.45 (-19.68%)</td><td>3401.00 <b>(+164.94%)</b></td><td>1364.96 <b>(+80.89%)</b></td><td>798.70 (+19.66%)</td><td>770.60 <b>(+74.34%)</b></td><td>1144.76 <b>(+262.59%)</b></td><td>174.17 <b>(-42.65%)</b></td><td>135.59 <b>(-32.24%)</b></td><td>168.05 (-16.42%)</td><td>39.46 <b>(-62.26%)</b></td><td>57.23 (-19.68%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>2.37 (n/a)</td><td>1.56 (n/a)</td><td>1.57 (n/a)</td><td>0.82 (n/a)</td><td>0.56 (n/a)</td><td>1283.70 (n/a)</td><td>754.60 (n/a)</td><td>667.50 (n/a)</td><td>442.00 (n/a)</td><td>315.72 (n/a)</td><td>303.69 (n/a)</td><td>200.10 (n/a)</td><td>201.07 (n/a)</td><td>104.56 (n/a)</td><td>71.25 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>2.10 (-16.22%)</td><td>1.64 (+19.92%)</td><td>1.51 (+10.58%)</td><td>1.39 <b>(+371.31%)</b></td><td>0.30 <b>(-72.36%)</b></td><td>755.20 <b>(-78.78%)</b></td><td>655.72 <b>(-62.33%)</b></td><td>695.90 (-9.56%)</td><td>498.50 (+19.37%)</td><td>106.24 <b>(-93.54%)</b></td><td>269.23 (-16.22%)</td><td>209.57 (+19.92%)</td><td>192.87 (+10.58%)</td><td>177.72 <b>(+371.31%)</b></td><td>37.88 <b>(-72.36%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>2.51 (n/a)</td><td>1.37 (n/a)</td><td>1.36 (n/a)</td><td>0.29 (n/a)</td><td>1.07 (n/a)</td><td>3559.40 (n/a)</td><td>1740.54 (n/a)</td><td>769.50 (n/a)</td><td>417.60 (n/a)</td><td>1644.59 (n/a)</td><td>321.37 (n/a)</td><td>174.75 (n/a)</td><td>174.42 (n/a)</td><td>37.71 (n/a)</td><td>137.04 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.51 <b>(-22.30%)</b></td><td>0.99 <b>(-36.44%)</b></td><td>0.88 <b>(-40.39%)</b></td><td>0.31 <b>(-74.84%)</b></td><td>0.51 <b>(+77.80%)</b></td><td>3406.60 <b>(+297.50%)</b></td><td>1475.10 <b>(+113.37%)</b></td><td>1186.80 <b>(+67.77%)</b></td><td>694.10 <b>(+28.70%)</b></td><td>1121.36 <b>(+788.54%)</b></td><td>193.36 <b>(-22.30%)</b></td><td>126.79 <b>(-36.44%)</b></td><td>113.10 <b>(-40.39%)</b></td><td>39.40 <b>(-74.84%)</b></td><td>65.79 <b>(+77.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.94 (n/a)</td><td>1.56 (n/a)</td><td>1.48 (n/a)</td><td>1.22 (n/a)</td><td>0.29 (n/a)</td><td>857.00 (n/a)</td><td>691.34 (n/a)</td><td>707.40 (n/a)</td><td>539.30 (n/a)</td><td>126.20 (n/a)</td><td>248.85 (n/a)</td><td>199.50 (n/a)</td><td>189.73 (n/a)</td><td>156.62 (n/a)</td><td>37.00 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.70 <b>(-36.60%)</b></td><td>0.60 (-16.30%)</td><td>0.58 (-6.75%)</td><td>0.45 (-13.61%)</td><td>0.10 <b>(-56.48%)</b></td><td>804.30 (+15.74%)</td><td>621.64 (+13.95%)</td><td>626.70 (+7.24%)</td><td>512.70 <b>(+57.71%)</b></td><td>117.47 <b>(-20.21%)</b></td><td>32.72 <b>(-36.59%)</b></td><td>27.71 (-16.30%)</td><td>26.77 (-6.75%)</td><td>20.86 (-13.61%)</td><td>4.85 <b>(-56.48%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.11 (n/a)</td><td>0.71 (n/a)</td><td>0.62 (n/a)</td><td>0.52 (n/a)</td><td>0.24 (n/a)</td><td>694.90 (n/a)</td><td>545.52 (n/a)</td><td>584.40 (n/a)</td><td>325.10 (n/a)</td><td>147.23 (n/a)</td><td>51.61 (n/a)</td><td>33.11 (n/a)</td><td>28.71 (n/a)</td><td>24.14 (n/a)</td><td>11.14 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>4.30 (+1.29%)</td><td>1.88 <b>(-37.31%)</b></td><td>0.81 <b>(-74.72%)</b></td><td>0.74 <b>(-31.17%)</b></td><td>1.60 <b>(+33.15%)</b></td><td>3564.30 <b>(+45.29%)</b></td><td>2347.42 <b>(+111.53%)</b></td><td>3221.40 <b>(+295.56%)</b></td><td>610.20 (-1.28%)</td><td>1440.65 <b>(+89.38%)</b></td><td>879.83 (+1.29%)</td><td>384.04 <b>(-37.31%)</b></td><td>166.66 <b>(-74.72%)</b></td><td>150.62 <b>(-31.17%)</b></td><td>328.31 <b>(+33.15%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>4.24 (n/a)</td><td>2.99 (n/a)</td><td>3.22 (n/a)</td><td>1.07 (n/a)</td><td>1.20 (n/a)</td><td>2453.20 (n/a)</td><td>1109.72 (n/a)</td><td>814.40 (n/a)</td><td>618.10 (n/a)</td><td>760.71 (n/a)</td><td>868.64 (n/a)</td><td>612.57 (n/a)</td><td>659.21 (n/a)</td><td>218.84 (n/a)</td><td>246.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm_split_leg_windowing[iter0]

_No metrics available._


### test_gemm_split_leg_windowing[iter1]

_No metrics available._


### test_gemm_split_leg_windowing[iter2]

_No metrics available._


### test_gemm_split_leg_windowing[iter3]

_No metrics available._


### test_gemm_split_leg_windowing[iter4]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter0]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter1]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter2]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter3]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter4]

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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>431.90 (n/a)</td><td>356.36 (n/a)</td><td>366.40 (n/a)</td><td>305.00 (n/a)</td><td>52.61 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2095.10 (n/a)</td><td>801.50 (n/a)</td><td>552.90 (n/a)</td><td>293.20 (n/a)</td><td>732.23 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1951.40 (n/a)</td><td>686.44 (n/a)</td><td>323.50 (n/a)</td><td>236.70 (n/a)</td><td>721.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.30 (n/a)</td><td>447.40 (n/a)</td><td>483.10 (n/a)</td><td>261.60 (n/a)</td><td>110.11 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.10 (n/a)</td><td>373.84 (n/a)</td><td>347.40 (n/a)</td><td>244.30 (n/a)</td><td>135.30 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1906.90 (n/a)</td><td>784.28 (n/a)</td><td>542.50 (n/a)</td><td>402.00 (n/a)</td><td>634.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.61 (+8.23%)</td><td>0.47 (-1.50%)</td><td>0.48 (-4.50%)</td><td>0.35 (-5.34%)</td><td>0.09 <b>(+30.05%)</b></td><td>628.40 (+5.63%)</td><td>482.44 (+2.73%)</td><td>458.90 (+4.70%)</td><td>363.20 (-7.61%)</td><td>97.04 <b>(+25.11%)</b></td><td>25.98 (+8.23%)</td><td>20.19 (-1.50%)</td><td>20.56 (-4.50%)</td><td>15.02 (-5.34%)</td><td>3.99 <b>(+30.05%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.56 (n/a)</td><td>0.48 (n/a)</td><td>0.50 (n/a)</td><td>0.37 (n/a)</td><td>0.07 (n/a)</td><td>594.90 (n/a)</td><td>469.60 (n/a)</td><td>438.30 (n/a)</td><td>393.10 (n/a)</td><td>77.56 (n/a)</td><td>24.00 (n/a)</td><td>20.50 (n/a)</td><td>21.53 (n/a)</td><td>15.86 (n/a)</td><td>3.07 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.57 (+0.78%)</td><td>0.44 (-3.54%)</td><td>0.42 (+4.54%)</td><td>0.33 (-11.80%)</td><td>0.09 (-1.77%)</td><td>663.80 (+13.37%)</td><td>524.38 (+3.81%)</td><td>527.80 (-4.35%)</td><td>386.70 (-0.77%)</td><td>102.30 (+8.10%)</td><td>24.41 (+0.78%)</td><td>18.58 (-3.54%)</td><td>17.88 (+4.54%)</td><td>14.22 (-11.80%)</td><td>3.81 (-1.77%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.57 (n/a)</td><td>0.45 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.09 (n/a)</td><td>585.50 (n/a)</td><td>505.14 (n/a)</td><td>551.80 (n/a)</td><td>389.70 (n/a)</td><td>94.63 (n/a)</td><td>24.22 (n/a)</td><td>19.26 (n/a)</td><td>17.10 (n/a)</td><td>16.12 (n/a)</td><td>3.87 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.31 (-1.82%)</td><td>0.30 (-0.66%)</td><td>0.31 (-0.09%)</td><td>0.30 (-1.00%)</td><td>0.00 <b>(-23.53%)</b></td><td>83905.20 (+1.01%)</td><td>82679.40 (+0.66%)</td><td>82211.50 (+0.09%)</td><td>82048.90 (+1.86%)</td><td>790.69 <b>(-21.34%)</b></td><td>209.39 (-1.82%)</td><td>207.80 (-0.66%)</td><td>208.97 (-0.09%)</td><td>204.75 (-1.00%)</td><td>1.97 <b>(-23.53%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83063.20 (n/a)</td><td>82138.60 (n/a)</td><td>82139.80 (n/a)</td><td>80551.80 (n/a)</td><td>1005.26 (n/a)</td><td>213.28 (n/a)</td><td>209.18 (n/a)</td><td>209.15 (n/a)</td><td>206.83 (n/a)</td><td>2.58 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.15 (-1.29%)</td><td>1.11 (-3.43%)</td><td>1.15 (-0.28%)</td><td>1.05 (-8.03%)</td><td>0.05 <b>(+574.89%)</b></td><td>23943.30 (+8.72%)</td><td>22705.40 (+3.72%)</td><td>21967.60 (+0.28%)</td><td>21941.60 (+1.30%)</td><td>1030.59 <b>(+641.51%)</b></td><td>782.98 (-1.29%)</td><td>757.87 (-3.43%)</td><td>782.05 (-0.28%)</td><td>717.52 (-8.03%)</td><td>33.82 <b>(+574.86%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.16 (n/a)</td><td>1.15 (n/a)</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>0.01 (n/a)</td><td>22021.90 (n/a)</td><td>21891.10 (n/a)</td><td>21906.80 (n/a)</td><td>21659.60 (n/a)</td><td>138.99 (n/a)</td><td>793.17 (n/a)</td><td>784.81 (n/a)</td><td>784.22 (n/a)</td><td>780.13 (n/a)</td><td>5.01 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>4.00 <b>(+63.69%)</b></td><td>2.23 (+13.15%)</td><td>2.15 (+3.14%)</td><td>1.16 (-15.51%)</td><td>1.08 <b>(+150.30%)</b></td><td>6934.70 (+18.36%)</td><td>4263.16 (-0.22%)</td><td>3753.50 (-3.05%)</td><td>2016.80 <b>(-38.91%)</b></td><td>1824.69 <b>(+75.57%)</b></td><td>1048.17 <b>(+63.69%)</b></td><td>584.36 (+13.15%)</td><td>563.19 (+3.14%)</td><td>304.83 (-15.51%)</td><td>282.35 <b>(+150.30%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>2.44 (n/a)</td><td>1.97 (n/a)</td><td>2.08 (n/a)</td><td>1.38 (n/a)</td><td>0.43 (n/a)</td><td>5858.90 (n/a)</td><td>4272.48 (n/a)</td><td>3871.50 (n/a)</td><td>3301.20 (n/a)</td><td>1039.27 (n/a)</td><td>640.35 (n/a)</td><td>516.47 (n/a)</td><td>546.03 (n/a)</td><td>360.81 (n/a)</td><td>112.80 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.30 (+8.98%)</td><td>0.22 (-2.92%)</td><td>0.21 (-14.47%)</td><td>0.18 (+4.56%)</td><td>0.04 (-6.00%)</td><td>6929.40 (-4.36%)</td><td>5805.76 (+2.01%)</td><td>5804.40 (+16.91%)</td><td>4216.50 (-8.24%)</td><td>1006.93 <b>(-20.81%)</b></td><td>15.92 (+8.98%)</td><td>11.89 (-2.92%)</td><td>11.56 (-14.47%)</td><td>9.68 (+4.56%)</td><td>2.39 (-6.00%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>7245.10 (n/a)</td><td>5691.38 (n/a)</td><td>4964.80 (n/a)</td><td>4594.90 (n/a)</td><td>1271.57 (n/a)</td><td>14.61 (n/a)</td><td>12.25 (n/a)</td><td>13.52 (n/a)</td><td>9.26 (n/a)</td><td>2.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>3.86 (n/a)</td><td>3.76 (n/a)</td><td>3.76 (n/a)</td><td>3.66 (n/a)</td><td>0.09 (n/a)</td><td>3.86 (n/a)</td><td>3.76 (n/a)</td><td>3.76 (n/a)</td><td>3.66 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>6.62 (+11.50%)</td><td>5.87 (+2.06%)</td><td>5.93 (+4.55%)</td><td>5.07 (-9.17%)</td><td>0.57 <b>(+242.51%)</b></td><td>6.62 (+11.50%)</td><td>5.87 (+2.06%)</td><td>5.93 (+4.55%)</td><td>5.07 (-9.17%)</td><td>0.57 <b>(+242.51%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>5.94 (n/a)</td><td>5.75 (n/a)</td><td>5.67 (n/a)</td><td>5.59 (n/a)</td><td>0.17 (n/a)</td><td>5.94 (n/a)</td><td>5.75 (n/a)</td><td>5.67 (n/a)</td><td>5.58 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>14.41 (+4.34%)</td><td>10.24 (-2.54%)</td><td>9.59 (-1.43%)</td><td>7.34 (-10.55%)</td><td>3.06 <b>(+45.37%)</b></td><td>14.40 (+4.34%)</td><td>10.23 (-2.54%)</td><td>9.59 (-1.43%)</td><td>7.34 (-10.55%)</td><td>3.06 <b>(+45.37%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>13.81 (n/a)</td><td>10.50 (n/a)</td><td>9.73 (n/a)</td><td>8.21 (n/a)</td><td>2.10 (n/a)</td><td>13.80 (n/a)</td><td>10.50 (n/a)</td><td>9.72 (n/a)</td><td>8.20 (n/a)</td><td>2.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>3.69 (n/a)</td><td>3.57 (n/a)</td><td>3.54 (n/a)</td><td>3.43 (n/a)</td><td>0.11 (n/a)</td><td>3.69 (n/a)</td><td>3.57 (n/a)</td><td>3.54 (n/a)</td><td>3.42 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>7.42 (-0.13%)</td><td>6.62 (-5.13%)</td><td>6.89 (+1.23%)</td><td>5.77 (-13.65%)</td><td>0.79 <b>(+136.97%)</b></td><td>7.42 (-0.13%)</td><td>6.61 (-5.13%)</td><td>6.88 (+1.23%)</td><td>5.77 (-13.65%)</td><td>0.79 <b>(+136.97%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>7.43 (n/a)</td><td>6.98 (n/a)</td><td>6.80 (n/a)</td><td>6.68 (n/a)</td><td>0.33 (n/a)</td><td>7.43 (n/a)</td><td>6.97 (n/a)</td><td>6.80 (n/a)</td><td>6.68 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>14.14 (+1.57%)</td><td>10.46 (+0.52%)</td><td>8.53 (-0.80%)</td><td>7.73 (-2.15%)</td><td>3.13 (+5.19%)</td><td>14.13 (+1.57%)</td><td>10.45 (+0.52%)</td><td>8.53 (-0.80%)</td><td>7.73 (-2.15%)</td><td>3.13 (+5.19%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>13.92 (n/a)</td><td>10.40 (n/a)</td><td>8.60 (n/a)</td><td>7.90 (n/a)</td><td>2.97 (n/a)</td><td>13.91 (n/a)</td><td>10.40 (n/a)</td><td>8.60 (n/a)</td><td>7.90 (n/a)</td><td>2.97 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>3.11 (+14.98%)</td><td>2.29 (+6.10%)</td><td>3.03 <b>(+28.55%)</b></td><td>1.04 <b>(-26.25%)</b></td><td>1.07 <b>(+86.41%)</b></td><td>3.10 (+14.98%)</td><td>2.28 (+6.10%)</td><td>3.02 <b>(+28.55%)</b></td><td>1.04 <b>(-26.25%)</b></td><td>1.07 <b>(+86.41%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>2.70 (n/a)</td><td>2.16 (n/a)</td><td>2.36 (n/a)</td><td>1.41 (n/a)</td><td>0.57 (n/a)</td><td>2.70 (n/a)</td><td>2.15 (n/a)</td><td>2.35 (n/a)</td><td>1.41 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.57 (+12.69%)</td><td>0.46 (+13.34%)</td><td>0.42 (+4.66%)</td><td>0.37 (+14.61%)</td><td>0.09 <b>(+36.99%)</b></td><td>0.56 (+12.69%)</td><td>0.45 (+13.34%)</td><td>0.41 (+4.66%)</td><td>0.36 (+14.61%)</td><td>0.09 <b>(+36.99%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.51 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.67 (-16.84%)</td><td>0.33 <b>(-32.09%)</b></td><td>0.39 <b>(-45.76%)</b></td><td>0.08 (+9.63%)</td><td>0.24 <b>(-37.27%)</b></td><td>0.67 (-16.84%)</td><td>0.33 <b>(-32.09%)</b></td><td>0.38 <b>(-45.76%)</b></td><td>0.08 (+9.63%)</td><td>0.24 <b>(-37.27%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.81 (n/a)</td><td>0.49 (n/a)</td><td>0.71 (n/a)</td><td>0.08 (n/a)</td><td>0.38 (n/a)</td><td>0.80 (n/a)</td><td>0.49 (n/a)</td><td>0.71 (n/a)</td><td>0.08 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>2.55 (+2.10%)</td><td>1.87 (+18.13%)</td><td>2.18 <b>(+36.78%)</b></td><td>0.44 <b>(-39.64%)</b></td><td>0.87 <b>(+29.95%)</b></td><td>2.51 (+2.10%)</td><td>1.84 (+18.13%)</td><td>2.15 <b>(+36.78%)</b></td><td>0.43 <b>(-39.64%)</b></td><td>0.86 <b>(+29.95%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>2.50 (n/a)</td><td>1.58 (n/a)</td><td>1.60 (n/a)</td><td>0.73 (n/a)</td><td>0.67 (n/a)</td><td>2.46 (n/a)</td><td>1.56 (n/a)</td><td>1.57 (n/a)</td><td>0.72 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.90 (n/a)</td><td>399.80 (n/a)</td><td>325.10 (n/a)</td><td>290.30 (n/a)</td><td>133.94 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1872.60 (n/a)</td><td>728.30 (n/a)</td><td>476.30 (n/a)</td><td>241.30 (n/a)</td><td>651.44 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.20 (n/a)</td><td>360.10 (n/a)</td><td>275.80 (n/a)</td><td>229.30 (n/a)</td><td>145.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.70 (n/a)</td><td>361.52 (n/a)</td><td>297.70 (n/a)</td><td>231.30 (n/a)</td><td>139.30 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1987.10 (n/a)</td><td>651.54 (n/a)</td><td>354.10 (n/a)</td><td>256.40 (n/a)</td><td>747.72 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>491.00 (n/a)</td><td>366.96 (n/a)</td><td>366.20 (n/a)</td><td>291.10 (n/a)</td><td>78.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (-5.98%)</td><td>0.02 (-16.70%)</td><td>0.03 (-14.23%)</td><td>0.01 (-3.32%)</td><td>0.01 (-0.35%)</td><td>573.10 (+3.43%)</td><td>386.88 <b>(+21.03%)</b></td><td>297.80 (+16.60%)</td><td>257.50 (+6.36%)</td><td>144.75 (+9.07%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.10 (n/a)</td><td>319.66 (n/a)</td><td>255.40 (n/a)</td><td>242.10 (n/a)</td><td>132.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (-10.59%)</td><td>0.02 <b>(-20.54%)</b></td><td>0.02 (-14.77%)</td><td>0.00 <b>(-57.59%)</b></td><td>0.01 (+2.07%)</td><td>2482.10 <b>(+135.78%)</b></td><td>851.78 <b>(+69.62%)</b></td><td>461.60 (+17.31%)</td><td>327.60 (+11.85%)</td><td>914.39 <b>(+191.99%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1052.70 (n/a)</td><td>502.16 (n/a)</td><td>393.50 (n/a)</td><td>292.90 (n/a)</td><td>313.16 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (-6.72%)</td><td>0.03 (+9.45%)</td><td>0.03 (+19.37%)</td><td>0.02 <b>(+37.83%)</b></td><td>0.01 <b>(-38.58%)</b></td><td>425.00 <b>(-27.44%)</b></td><td>329.24 (-15.38%)</td><td>289.60 (-16.25%)</td><td>262.00 (+7.25%)</td><td>70.90 <b>(-51.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.70 (n/a)</td><td>389.08 (n/a)</td><td>345.80 (n/a)</td><td>244.30 (n/a)</td><td>147.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (+14.35%)</td><td>0.03 <b>(+29.46%)</b></td><td>0.03 <b>(+58.55%)</b></td><td>0.00 <b>(-73.86%)</b></td><td>0.01 <b>(+76.37%)</b></td><td>2151.70 <b>(+282.59%)</b></td><td>631.74 <b>(+48.24%)</b></td><td>275.50 <b>(-36.93%)</b></td><td>210.50 (-12.58%)</td><td>850.33 <b>(+563.22%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.40 (n/a)</td><td>426.16 (n/a)</td><td>436.80 (n/a)</td><td>240.80 (n/a)</td><td>128.21 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 <b>(-26.70%)</b></td><td>0.02 <b>(-22.71%)</b></td><td>0.02 <b>(-27.00%)</b></td><td>0.02 (-4.59%)</td><td>0.00 <b>(-50.77%)</b></td><td>536.60 (+4.83%)</td><td>413.00 <b>(+20.05%)</b></td><td>417.30 <b>(+37.00%)</b></td><td>290.50 <b>(+36.45%)</b></td><td>89.28 <b>(-31.82%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.90 (n/a)</td><td>344.02 (n/a)</td><td>304.60 (n/a)</td><td>212.90 (n/a)</td><td>130.95 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 <b>(-30.00%)</b></td><td>0.02 (-11.13%)</td><td>0.02 (-2.71%)</td><td>0.01 (+0.61%)</td><td>0.00 <b>(-49.86%)</b></td><td>599.60 (-0.61%)</td><td>478.14 (+5.16%)</td><td>507.70 (+2.79%)</td><td>325.50 <b>(+42.83%)</b></td><td>104.93 <b>(-24.45%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.30 (n/a)</td><td>454.68 (n/a)</td><td>493.90 (n/a)</td><td>227.90 (n/a)</td><td>138.89 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (+4.41%)</td><td>0.02 (+17.77%)</td><td>0.03 <b>(+48.26%)</b></td><td>0.01 <b>(+75.50%)</b></td><td>0.01 (+3.24%)</td><td>1339.50 <b>(-43.02%)</b></td><td>542.40 <b>(-31.14%)</b></td><td>315.60 <b>(-32.55%)</b></td><td>278.70 (-4.23%)</td><td>454.36 <b>(-48.29%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2350.80 (n/a)</td><td>787.64 (n/a)</td><td>467.90 (n/a)</td><td>291.00 (n/a)</td><td>878.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (-5.58%)</td><td>0.02 (+9.08%)</td><td>0.02 <b>(+21.30%)</b></td><td>0.01 (+9.20%)</td><td>0.00 <b>(-33.00%)</b></td><td>558.30 (-8.43%)</td><td>478.42 (-9.42%)</td><td>454.60 (-17.57%)</td><td>421.10 (+5.91%)</td><td>54.62 <b>(-32.89%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>609.70 (n/a)</td><td>528.18 (n/a)</td><td>551.50 (n/a)</td><td>397.60 (n/a)</td><td>81.39 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 <b>(+23.57%)</b></td><td>0.02 <b>(-20.94%)</b></td><td>0.02 <b>(-32.89%)</b></td><td>0.00 <b>(-69.50%)</b></td><td>0.01 <b>(+73.17%)</b></td><td>1905.30 <b>(+227.88%)</b></td><td>692.88 <b>(+92.99%)</b></td><td>434.60 <b>(+48.99%)</b></td><td>207.60 (-19.06%)</td><td>686.61 <b>(+411.62%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.10 (n/a)</td><td>359.02 (n/a)</td><td>291.70 (n/a)</td><td>256.50 (n/a)</td><td>134.20 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (-14.92%)</td><td>0.02 <b>(-30.55%)</b></td><td>0.02 <b>(-42.79%)</b></td><td>0.01 (-15.21%)</td><td>0.01 (-7.46%)</td><td>644.10 (+17.95%)</td><td>489.86 <b>(+45.32%)</b></td><td>530.20 <b>(+74.81%)</b></td><td>241.80 (+17.49%)</td><td>149.77 (+15.01%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>546.10 (n/a)</td><td>337.08 (n/a)</td><td>303.30 (n/a)</td><td>205.80 (n/a)</td><td>130.22 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 <b>(-46.89%)</b></td><td>0.02 <b>(-39.11%)</b></td><td>0.02 <b>(-37.48%)</b></td><td>0.01 <b>(-53.89%)</b></td><td>0.00 <b>(-39.90%)</b></td><td>1059.30 <b>(+116.89%)</b></td><td>602.90 <b>(+70.45%)</b></td><td>534.90 <b>(+59.96%)</b></td><td>426.10 <b>(+88.29%)</b></td><td>260.01 <b>(+159.10%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>488.40 (n/a)</td><td>353.72 (n/a)</td><td>334.40 (n/a)</td><td>226.30 (n/a)</td><td>100.35 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 <b>(-48.15%)</b></td><td>0.02 <b>(-42.81%)</b></td><td>0.02 <b>(-39.77%)</b></td><td>0.00 <b>(-71.37%)</b></td><td>0.01 <b>(-41.61%)</b></td><td>1901.10 <b>(+249.34%)</b></td><td>750.06 <b>(+107.91%)</b></td><td>464.00 <b>(+66.01%)</b></td><td>407.00 <b>(+92.89%)</b></td><td>645.03 <b>(+298.72%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.20 (n/a)</td><td>360.76 (n/a)</td><td>279.50 (n/a)</td><td>211.00 (n/a)</td><td>161.77 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 <b>(-28.79%)</b></td><td>0.02 <b>(-31.76%)</b></td><td>0.02 <b>(-44.11%)</b></td><td>0.01 (-15.04%)</td><td>0.01 <b>(-30.79%)</b></td><td>589.50 (+17.69%)</td><td>470.66 <b>(+42.85%)</b></td><td>519.10 <b>(+78.94%)</b></td><td>239.50 <b>(+40.39%)</b></td><td>139.90 (+10.53%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.90 (n/a)</td><td>329.48 (n/a)</td><td>290.10 (n/a)</td><td>170.60 (n/a)</td><td>126.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 <b>(-30.75%)</b></td><td>0.02 <b>(-26.54%)</b></td><td>0.02 <b>(-20.84%)</b></td><td>0.01 (-17.90%)</td><td>0.00 <b>(-38.67%)</b></td><td>585.60 <b>(+21.82%)</b></td><td>475.80 <b>(+34.26%)</b></td><td>427.70 <b>(+26.35%)</b></td><td>382.20 <b>(+44.39%)</b></td><td>96.35 (+11.34%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.70 (n/a)</td><td>354.38 (n/a)</td><td>338.50 (n/a)</td><td>264.70 (n/a)</td><td>86.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.09 (-6.12%)</td><td>0.08 (-4.00%)</td><td>0.08 (-0.29%)</td><td>0.06 (-8.52%)</td><td>0.01 (+3.53%)</td><td>417.50 (+9.32%)</td><td>328.32 (+4.69%)</td><td>311.30 (+0.29%)</td><td>266.00 (+6.53%)</td><td>59.16 <b>(+22.17%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>381.90 (n/a)</td><td>313.60 (n/a)</td><td>310.40 (n/a)</td><td>249.70 (n/a)</td><td>48.42 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.16 (+0.16%)</td><td>0.13 <b>(+39.21%)</b></td><td>0.14 <b>(+95.42%)</b></td><td>0.09 <b>(+319.95%)</b></td><td>0.03 <b>(-46.64%)</b></td><td>458.40 <b>(-76.19%)</b></td><td>324.32 <b>(-55.43%)</b></td><td>284.50 <b>(-48.82%)</b></td><td>250.40 (-0.16%)</td><td>91.05 <b>(-86.85%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1925.20 (n/a)</td><td>727.74 (n/a)</td><td>555.90 (n/a)</td><td>250.80 (n/a)</td><td>692.45 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (-19.34%)</td><td>0.01 <b>(-21.83%)</b></td><td>0.01 <b>(-28.74%)</b></td><td>0.01 <b>(-26.47%)</b></td><td>0.00 (-0.89%)</td><td>536.00 <b>(+36.01%)</b></td><td>412.54 <b>(+30.15%)</b></td><td>413.40 <b>(+40.33%)</b></td><td>312.80 <b>(+23.98%)</b></td><td>100.33 <b>(+58.25%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>394.10 (n/a)</td><td>316.98 (n/a)</td><td>294.60 (n/a)</td><td>252.30 (n/a)</td><td>63.40 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (-3.01%)</td><td>0.03 (-3.62%)</td><td>0.03 (-15.13%)</td><td>0.02 <b>(+49.22%)</b></td><td>0.00 <b>(-43.58%)</b></td><td>397.30 <b>(-32.99%)</b></td><td>301.24 (-5.70%)</td><td>295.10 (+17.85%)</td><td>238.00 (+3.07%)</td><td>58.99 <b>(-61.71%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.90 (n/a)</td><td>319.44 (n/a)</td><td>250.40 (n/a)</td><td>230.90 (n/a)</td><td>154.07 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.05 (-15.84%)</td><td>0.04 (-11.49%)</td><td>0.04 (-1.88%)</td><td>0.02 <b>(-26.89%)</b></td><td>0.01 (+11.40%)</td><td>580.80 <b>(+36.79%)</b></td><td>376.44 (+19.84%)</td><td>308.50 (+1.92%)</td><td>243.10 (+18.82%)</td><td>148.26 <b>(+86.24%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>424.60 (n/a)</td><td>314.12 (n/a)</td><td>302.70 (n/a)</td><td>204.60 (n/a)</td><td>79.61 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (+13.15%)</td><td>0.03 (-3.57%)</td><td>0.03 (-4.26%)</td><td>0.01 <b>(-33.97%)</b></td><td>0.01 <b>(+56.56%)</b></td><td>660.10 <b>(+51.43%)</b></td><td>377.72 (+14.97%)</td><td>316.00 (+4.43%)</td><td>214.20 (-11.60%)</td><td>178.09 <b>(+110.86%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>435.90 (n/a)</td><td>328.54 (n/a)</td><td>302.60 (n/a)</td><td>242.30 (n/a)</td><td>84.46 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (-15.42%)</td><td>0.03 (-19.88%)</td><td>0.02 (-10.49%)</td><td>0.02 (-3.34%)</td><td>0.01 <b>(-26.62%)</b></td><td>553.00 (+3.44%)</td><td>451.06 (+17.99%)</td><td>486.10 (+11.72%)</td><td>232.70 (+18.24%)</td><td>125.41 (-16.64%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.60 (n/a)</td><td>382.28 (n/a)</td><td>435.10 (n/a)</td><td>196.80 (n/a)</td><td>150.44 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (-9.01%)</td><td>0.02 <b>(-23.67%)</b></td><td>0.02 <b>(-43.10%)</b></td><td>0.02 (-15.29%)</td><td>0.01 (+16.79%)</td><td>530.10 (+18.04%)</td><td>380.18 <b>(+37.00%)</b></td><td>423.70 <b>(+75.74%)</b></td><td>231.40 (+9.88%)</td><td>136.89 <b>(+39.07%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>449.10 (n/a)</td><td>277.50 (n/a)</td><td>241.10 (n/a)</td><td>210.60 (n/a)</td><td>98.43 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (+16.32%)</td><td>0.02 (-4.62%)</td><td>0.02 (+1.39%)</td><td>0.02 (-13.15%)</td><td>0.01 <b>(+23.14%)</b></td><td>619.30 (+15.13%)</td><td>451.76 (+7.57%)</td><td>452.60 (-1.37%)</td><td>258.70 (-14.02%)</td><td>133.28 <b>(+21.74%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.90 (n/a)</td><td>419.98 (n/a)</td><td>458.90 (n/a)</td><td>300.90 (n/a)</td><td>109.48 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 <b>(-35.42%)</b></td><td>0.02 <b>(-43.96%)</b></td><td>0.02 <b>(-52.52%)</b></td><td>0.01 <b>(-38.18%)</b></td><td>0.01 <b>(-27.36%)</b></td><td>640.00 <b>(+61.78%)</b></td><td>483.72 <b>(+80.87%)</b></td><td>526.10 <b>(+110.61%)</b></td><td>295.40 <b>(+54.82%)</b></td><td>131.87 <b>(+70.28%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>395.60 (n/a)</td><td>267.44 (n/a)</td><td>249.80 (n/a)</td><td>190.80 (n/a)</td><td>77.45 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (-15.10%)</td><td>0.02 <b>(-24.12%)</b></td><td>0.02 (-11.02%)</td><td>0.01 <b>(-53.46%)</b></td><td>0.01 (-3.28%)</td><td>1096.60 <b>(+114.85%)</b></td><td>566.58 <b>(+47.54%)</b></td><td>495.50 (+12.38%)</td><td>248.10 (+17.75%)</td><td>317.59 <b>(+149.66%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.40 (n/a)</td><td>384.02 (n/a)</td><td>440.90 (n/a)</td><td>210.70 (n/a)</td><td>127.21 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.04 (+11.10%)</td><td>0.02 (+19.33%)</td><td>0.02 (-0.09%)</td><td>0.01 <b>(+317.83%)</b></td><td>0.01 (-10.59%)</td><td>577.70 <b>(-76.07%)</b></td><td>392.94 <b>(-50.07%)</b></td><td>460.80 (+0.09%)</td><td>191.00 (-9.99%)</td><td>163.12 <b>(-82.29%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2413.90 (n/a)</td><td>787.06 (n/a)</td><td>460.40 (n/a)</td><td>212.20 (n/a)</td><td>920.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (-11.45%)</td><td>0.02 (-18.26%)</td><td>0.02 <b>(-24.16%)</b></td><td>0.02 (-7.18%)</td><td>0.01 (-19.06%)</td><td>552.70 (+7.74%)</td><td>440.72 <b>(+20.22%)</b></td><td>460.60 <b>(+31.86%)</b></td><td>276.60 (+12.94%)</td><td>101.64 (-7.35%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.00 (n/a)</td><td>366.58 (n/a)</td><td>349.30 (n/a)</td><td>244.90 (n/a)</td><td>109.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.03 (-14.90%)</td><td>0.02 (+10.60%)</td><td>0.02 <b>(+22.50%)</b></td><td>0.02 <b>(+35.26%)</b></td><td>0.01 <b>(-37.31%)</b></td><td>490.20 <b>(-26.06%)</b></td><td>394.96 (-18.13%)</td><td>426.30 (-18.36%)</td><td>241.90 (+17.54%)</td><td>100.24 <b>(-40.86%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>663.00 (n/a)</td><td>482.40 (n/a)</td><td>522.20 (n/a)</td><td>205.80 (n/a)</td><td>169.50 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.34 <b>(-39.94%)</b></td><td>0.23 <b>(-34.65%)</b></td><td>0.24 <b>(-25.45%)</b></td><td>0.06 <b>(-66.59%)</b></td><td>0.12 (-17.85%)</td><td>1737.10 <b>(+199.35%)</b></td><td>661.44 <b>(+102.11%)</b></td><td>414.60 <b>(+34.13%)</b></td><td>285.60 <b>(+66.53%)</b></td><td>612.90 <b>(+300.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.57 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>580.30 (n/a)</td><td>327.26 (n/a)</td><td>309.10 (n/a)</td><td>171.50 (n/a)</td><td>152.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.38 (-2.37%)</td><td>0.24 <b>(-26.20%)</b></td><td>0.20 <b>(-43.35%)</b></td><td>0.18 (+0.11%)</td><td>0.08 (-0.97%)</td><td>552.00 (-0.11%)</td><td>443.22 <b>(+34.91%)</b></td><td>488.70 <b>(+76.55%)</b></td><td>261.20 (+2.43%)</td><td>121.58 (-3.35%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.36 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>552.60 (n/a)</td><td>328.54 (n/a)</td><td>276.80 (n/a)</td><td>255.00 (n/a)</td><td>125.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.36 (-14.53%)</td><td>0.25 (-18.83%)</td><td>0.22 <b>(-38.88%)</b></td><td>0.20 <b>(+21.16%)</b></td><td>0.07 <b>(-46.69%)</b></td><td>493.70 (-17.46%)</td><td>410.10 (+10.06%)</td><td>443.10 <b>(+63.63%)</b></td><td>272.10 (+16.98%)</td><td>87.03 <b>(-49.53%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.36 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>598.10 (n/a)</td><td>372.60 (n/a)</td><td>270.80 (n/a)</td><td>232.60 (n/a)</td><td>172.45 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.28 (-1.63%)</td><td>0.20 (-15.53%)</td><td>0.16 <b>(-35.61%)</b></td><td>0.14 (+17.52%)</td><td>0.06 (-6.96%)</td><td>512.40 (-14.91%)</td><td>401.10 (+15.25%)</td><td>446.90 <b>(+55.28%)</b></td><td>265.90 (+1.68%)</td><td>107.97 <b>(-24.45%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>602.20 (n/a)</td><td>348.02 (n/a)</td><td>287.80 (n/a)</td><td>261.50 (n/a)</td><td>142.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.28 (-14.98%)</td><td>0.20 (-10.04%)</td><td>0.17 <b>(-25.08%)</b></td><td>0.14 (+8.57%)</td><td>0.06 <b>(-23.30%)</b></td><td>515.20 (-7.88%)</td><td>394.08 (+7.22%)</td><td>428.40 <b>(+33.50%)</b></td><td>260.00 (+17.59%)</td><td>107.57 (-19.23%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>559.30 (n/a)</td><td>367.56 (n/a)</td><td>320.90 (n/a)</td><td>221.10 (n/a)</td><td>133.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.17 <b>(-43.33%)</b></td><td>0.13 <b>(-48.00%)</b></td><td>0.16 <b>(-45.86%)</b></td><td>0.03 <b>(-79.17%)</b></td><td>0.06 (-10.83%)</td><td>2400.30 <b>(+380.16%)</b></td><td>856.42 <b>(+175.15%)</b></td><td>475.60 <b>(+84.70%)</b></td><td>426.50 <b>(+76.46%)</b></td><td>864.29 <b>(+692.19%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.29 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>499.90 (n/a)</td><td>311.26 (n/a)</td><td>257.50 (n/a)</td><td>241.70 (n/a)</td><td>109.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.44 (+0.48%)</td><td>0.32 (+6.08%)</td><td>0.26 (+1.75%)</td><td>0.24 (-5.13%)</td><td>0.09 (+15.63%)</td><td>550.80 (+5.42%)</td><td>443.82 (-3.91%)</td><td>503.80 (-1.72%)</td><td>296.60 (-0.47%)</td><td>118.30 <b>(+23.40%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.08 (n/a)</td><td>522.50 (n/a)</td><td>461.86 (n/a)</td><td>512.60 (n/a)</td><td>298.00 (n/a)</td><td>95.87 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.44 <b>(-30.91%)</b></td><td>0.32 (+12.20%)</td><td>0.38 <b>(+68.17%)</b></td><td>0.18 <b>(+134.67%)</b></td><td>0.11 <b>(-45.52%)</b></td><td>709.30 <b>(-57.38%)</b></td><td>458.64 <b>(-35.24%)</b></td><td>344.60 <b>(-40.53%)</b></td><td>298.70 <b>(+44.72%)</b></td><td>186.31 <b>(-66.74%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.64 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.08 (n/a)</td><td>0.21 (n/a)</td><td>1664.40 (n/a)</td><td>708.26 (n/a)</td><td>579.50 (n/a)</td><td>206.40 (n/a)</td><td>560.22 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.32 <b>(-22.90%)</b></td><td>0.22 <b>(-30.84%)</b></td><td>0.27 <b>(-26.95%)</b></td><td>0.04 <b>(-82.15%)</b></td><td>0.11 <b>(+22.40%)</b></td><td>3427.70 <b>(+460.26%)</b></td><td>1081.14 <b>(+148.80%)</b></td><td>487.80 <b>(+36.91%)</b></td><td>408.20 <b>(+29.71%)</b></td><td>1313.64 <b>(+881.97%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.37 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>611.80 (n/a)</td><td>434.54 (n/a)</td><td>356.30 (n/a)</td><td>314.70 (n/a)</td><td>133.78 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.01 <b>(-33.80%)</b></td><td>0.01 (-0.42%)</td><td>0.01 <b>(+34.52%)</b></td><td>0.01 (+10.25%)</td><td>0.00 <b>(-56.93%)</b></td><td>530.80 (-9.30%)</td><td>353.06 (-11.40%)</td><td>307.30 <b>(-25.67%)</b></td><td>299.20 <b>(+51.03%)</b></td><td>100.09 <b>(-40.99%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.20 (n/a)</td><td>398.48 (n/a)</td><td>413.40 (n/a)</td><td>198.10 (n/a)</td><td>169.62 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.01 (-14.73%)</td><td>0.01 (-2.37%)</td><td>0.01 (-16.08%)</td><td>0.01 (+11.61%)</td><td>0.00 <b>(-46.94%)</b></td><td>498.00 (-10.40%)</td><td>356.78 (-6.03%)</td><td>339.20 (+19.18%)</td><td>291.50 (+17.30%)</td><td>83.39 <b>(-45.81%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>555.80 (n/a)</td><td>379.68 (n/a)</td><td>284.60 (n/a)</td><td>248.50 (n/a)</td><td>153.89 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (+2.80%)</td><td>0.01 <b>(+26.30%)</b></td><td>0.01 <b>(+43.61%)</b></td><td>0.01 <b>(+30.08%)</b></td><td>0.00 (-18.55%)</td><td>471.30 <b>(-23.13%)</b></td><td>344.38 <b>(-23.45%)</b></td><td>313.30 <b>(-30.36%)</b></td><td>258.50 (-2.75%)</td><td>81.91 <b>(-34.68%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>613.10 (n/a)</td><td>449.88 (n/a)</td><td>449.90 (n/a)</td><td>265.80 (n/a)</td><td>125.41 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.59 (+9.01%)</td><td>0.45 (+1.85%)</td><td>0.46 (-7.62%)</td><td>0.35 <b>(+126.51%)</b></td><td>0.10 <b>(-39.48%)</b></td><td>377.60 <b>(-55.86%)</b></td><td>306.86 (-19.11%)</td><td>289.50 (+8.26%)</td><td>222.10 (-8.30%)</td><td>63.06 <b>(-76.34%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.49 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>855.40 (n/a)</td><td>379.36 (n/a)</td><td>267.40 (n/a)</td><td>242.20 (n/a)</td><td>266.56 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.48 (-3.40%)</td><td>0.37 (-6.24%)</td><td>0.33 <b>(-29.88%)</b></td><td>0.27 <b>(+319.77%)</b></td><td>0.10 <b>(-44.25%)</b></td><td>488.40 <b>(-76.18%)</b></td><td>380.40 <b>(-39.85%)</b></td><td>396.10 <b>(+42.64%)</b></td><td>275.10 (+3.54%)</td><td>101.46 <b>(-87.20%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.48 (n/a)</td><td>0.06 (n/a)</td><td>0.19 (n/a)</td><td>2050.20 (n/a)</td><td>632.38 (n/a)</td><td>277.70 (n/a)</td><td>265.70 (n/a)</td><td>792.67 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.47 <b>(-21.52%)</b></td><td>0.30 (-19.51%)</td><td>0.28 (-2.87%)</td><td>0.08 <b>(-71.21%)</b></td><td>0.16 (+11.79%)</td><td>1755.10 <b>(+247.34%)</b></td><td>668.76 <b>(+72.45%)</b></td><td>473.50 (+2.96%)</td><td>283.60 <b>(+27.46%)</b></td><td>618.16 <b>(+385.65%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.59 (n/a)</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>505.30 (n/a)</td><td>387.80 (n/a)</td><td>459.90 (n/a)</td><td>222.50 (n/a)</td><td>127.29 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.46 (-17.32%)</td><td>0.37 (-4.39%)</td><td>0.36 (-17.72%)</td><td>0.29 <b>(+21.13%)</b></td><td>0.07 <b>(-50.42%)</b></td><td>454.60 (-17.44%)</td><td>362.26 (-4.04%)</td><td>367.40 <b>(+21.53%)</b></td><td>284.70 <b>(+20.94%)</b></td><td>67.08 <b>(-53.63%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.56 (n/a)</td><td>0.39 (n/a)</td><td>0.44 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>550.60 (n/a)</td><td>377.50 (n/a)</td><td>302.30 (n/a)</td><td>235.40 (n/a)</td><td>144.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.53 (+7.73%)</td><td>0.33 (-2.37%)</td><td>0.30 (-14.29%)</td><td>0.22 <b>(+214.72%)</b></td><td>0.12 <b>(-28.59%)</b></td><td>600.30 <b>(-68.23%)</b></td><td>434.16 <b>(-32.72%)</b></td><td>434.00 (+16.67%)</td><td>250.50 (-7.15%)</td><td>127.19 <b>(-81.77%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.36 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>1889.30 (n/a)</td><td>645.26 (n/a)</td><td>372.00 (n/a)</td><td>269.80 (n/a)</td><td>697.55 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.02 (+3.62%)</td><td>0.01 (-3.98%)</td><td>0.01 <b>(-24.21%)</b></td><td>0.01 (-15.66%)</td><td>0.00 <b>(+40.27%)</b></td><td>571.80 (+18.58%)</td><td>403.88 (+10.01%)</td><td>432.10 <b>(+31.94%)</b></td><td>255.70 (-3.51%)</td><td>143.11 <b>(+44.35%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>482.20 (n/a)</td><td>367.14 (n/a)</td><td>327.50 (n/a)</td><td>265.00 (n/a)</td><td>99.14 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.01 <b>(-21.55%)</b></td><td>0.01 (-11.05%)</td><td>0.01 (-5.58%)</td><td>0.01 (-1.68%)</td><td>0.00 <b>(-31.35%)</b></td><td>461.30 (+1.70%)</td><td>352.98 (+10.38%)</td><td>319.80 (+5.93%)</td><td>293.70 <b>(+27.47%)</b></td><td>70.43 (-14.00%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>453.60 (n/a)</td><td>319.80 (n/a)</td><td>301.90 (n/a)</td><td>230.40 (n/a)</td><td>81.90 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.00 (-12.50%)</td><td>0.00 <b>(+27.78%)</b></td><td>0.00 <b>(+66.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-0.00%)</td><td>18427.01 (-7.71%)</td><td>11215.44 <b>(-23.12%)</b></td><td>8693.58 <b>(-43.48%)</b></td><td>5613.99 (+3.12%)</td><td>6114.91 (+11.98%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19965.95 (n/a)</td><td>14588.16 (n/a)</td><td>15380.78 (n/a)</td><td>5444.28 (n/a)</td><td>5460.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.00 <b>(+27.27%)</b></td><td>0.00 <b>(+20.59%)</b></td><td>0.00 (+20.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+31.40%)</b></td><td>18613.79 (-16.46%)</td><td>12715.00 (-16.84%)</td><td>14230.03 (-19.35%)</td><td>5888.93 (-18.48%)</td><td>6107.68 (-12.91%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22280.55 (n/a)</td><td>15290.52 (n/a)</td><td>17644.14 (n/a)</td><td>7223.64 (n/a)</td><td>7013.44 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>0.15 (-4.44%)</td><td>0.11 (+1.91%)</td><td>0.11 <b>(+20.84%)</b></td><td>0.08 (-6.26%)</td><td>0.03 (-9.78%)</td><td>26440.05 (+6.64%)</td><td>19835.79 (-2.77%)</td><td>19657.22 (-17.23%)</td><td>14318.72 (+4.69%)</td><td>5313.50 (-3.88%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>24794.05 (n/a)</td><td>20400.77 (n/a)</td><td>23748.63 (n/a)</td><td>13677.08 (n/a)</td><td>5528.03 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>1.48 (-18.55%)</td><td>1.04 <b>(-20.28%)</b></td><td>1.02 <b>(-28.28%)</b></td><td>0.68 (-10.43%)</td><td>0.29 <b>(-31.87%)</b></td><td>768.90 (+11.65%)</td><td>535.12 <b>(+20.99%)</b></td><td>512.10 <b>(+39.42%)</b></td><td>353.10 <b>(+22.77%)</b></td><td>149.34 (-8.12%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.82 (n/a)</td><td>1.31 (n/a)</td><td>1.43 (n/a)</td><td>0.76 (n/a)</td><td>0.42 (n/a)</td><td>688.70 (n/a)</td><td>442.30 (n/a)</td><td>367.30 (n/a)</td><td>287.60 (n/a)</td><td>162.53 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>2.39 (-17.11%)</td><td>1.58 (-19.24%)</td><td>1.58 <b>(-30.96%)</b></td><td>0.33 (+5.02%)</td><td>0.79 <b>(-23.15%)</b></td><td>3163.70 (-4.78%)</td><td>1092.18 (+5.61%)</td><td>664.50 <b>(+44.83%)</b></td><td>438.20 <b>(+20.65%)</b></td><td>1162.83 (-9.37%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>2.89 (n/a)</td><td>1.96 (n/a)</td><td>2.29 (n/a)</td><td>0.32 (n/a)</td><td>1.02 (n/a)</td><td>3322.40 (n/a)</td><td>1034.16 (n/a)</td><td>458.80 (n/a)</td><td>363.20 (n/a)</td><td>1283.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:39:46</td><td>2.22 <b>(+39.15%)</b></td><td>1.20 (-16.15%)</td><td>1.03 <b>(-26.59%)</b></td><td>0.26 <b>(-79.11%)</b></td><td>0.73 <b>(+409.89%)</b></td><td>2019.60 <b>(+378.69%)</b></td><td>731.06 <b>(+98.40%)</b></td><td>509.70 <b>(+36.21%)</b></td><td>236.50 <b>(-28.12%)</b></td><td>731.72 <b>(+1846.01%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:36</td><td>1.59 (n/a)</td><td>1.43 (n/a)</td><td>1.40 (n/a)</td><td>1.24 (n/a)</td><td>0.14 (n/a)</td><td>421.90 (n/a)</td><td>368.48 (n/a)</td><td>374.20 (n/a)</td><td>329.00 (n/a)</td><td>37.60 (n/a)</td>
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
