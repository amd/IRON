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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.06 (+19.44%)</td><td>0.05 <b>(+27.26%)</b></td><td>0.05 (+18.34%)</td><td>0.04 <b>(+70.71%)</b></td><td>0.01 <b>(-29.88%)</b></td><td>287.80 <b>(-41.42%)</b></td><td>248.84 <b>(-25.11%)</b></td><td>241.50 (-15.50%)</td><td>201.30 (-16.26%)</td><td>34.10 <b>(-66.12%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>491.30 (n/a)</td><td>332.26 (n/a)</td><td>285.80 (n/a)</td><td>240.40 (n/a)</td><td>100.63 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.05 (-4.22%)</td><td>0.04 (+1.22%)</td><td>0.05 (-0.66%)</td><td>0.03 (+6.46%)</td><td>0.01 (-11.16%)</td><td>416.60 (-6.07%)</td><td>299.70 (-2.85%)</td><td>258.40 (+0.66%)</td><td>229.00 (+4.42%)</td><td>82.52 (-14.64%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>443.50 (n/a)</td><td>308.50 (n/a)</td><td>256.70 (n/a)</td><td>219.30 (n/a)</td><td>96.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.05 (+4.79%)</td><td>0.04 (+4.89%)</td><td>0.04 (+19.16%)</td><td>0.02 (-8.56%)</td><td>0.01 (+5.18%)</td><td>578.50 (+9.38%)</td><td>365.26 (-3.36%)</td><td>340.10 (-16.07%)</td><td>236.30 (-4.56%)</td><td>128.07 (+16.79%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.90 (n/a)</td><td>377.94 (n/a)</td><td>405.20 (n/a)</td><td>247.60 (n/a)</td><td>109.65 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (+11.48%)</td><td>0.02 (+18.85%)</td><td>0.02 <b>(+56.78%)</b></td><td>0.01 (+11.46%)</td><td>0.01 (+10.87%)</td><td>492.50 (-10.28%)</td><td>342.32 (-15.48%)</td><td>290.60 <b>(-36.22%)</b></td><td>212.90 (-10.28%)</td><td>126.42 (-5.53%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.90 (n/a)</td><td>405.04 (n/a)</td><td>455.60 (n/a)</td><td>237.30 (n/a)</td><td>133.81 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (-0.88%)</td><td>0.01 (-11.60%)</td><td>0.01 (-2.78%)</td><td>0.01 (-16.26%)</td><td>0.00 (-5.37%)</td><td>657.40 (+19.42%)</td><td>460.36 (+13.38%)</td><td>457.90 (+2.85%)</td><td>266.60 (+0.91%)</td><td>140.01 (+12.92%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>550.50 (n/a)</td><td>406.04 (n/a)</td><td>445.20 (n/a)</td><td>264.20 (n/a)</td><td>124.00 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 <b>(+50.70%)</b></td><td>0.02 <b>(+34.62%)</b></td><td>0.01 <b>(+23.10%)</b></td><td>0.01 <b>(+33.01%)</b></td><td>0.01 <b>(+90.50%)</b></td><td>590.80 <b>(-24.82%)</b></td><td>407.18 (-19.87%)</td><td>420.70 (-18.77%)</td><td>207.00 <b>(-33.63%)</b></td><td>172.03 (-3.34%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>785.80 (n/a)</td><td>508.12 (n/a)</td><td>517.90 (n/a)</td><td>311.90 (n/a)</td><td>177.97 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (-5.19%)</td><td>0.02 (-8.49%)</td><td>0.02 (-4.49%)</td><td>0.01 (-5.23%)</td><td>0.01 (-2.50%)</td><td>562.70 (+5.51%)</td><td>375.70 (+10.34%)</td><td>306.40 (+4.72%)</td><td>231.80 (+5.46%)</td><td>143.86 (+11.90%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>533.30 (n/a)</td><td>340.48 (n/a)</td><td>292.60 (n/a)</td><td>219.80 (n/a)</td><td>128.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (+3.13%)</td><td>0.01 (+9.29%)</td><td>0.01 (+0.43%)</td><td>0.01 <b>(+55.88%)</b></td><td>0.01 (-3.64%)</td><td>678.30 <b>(-35.85%)</b></td><td>435.34 (-17.30%)</td><td>462.00 (-0.45%)</td><td>240.70 (-3.06%)</td><td>188.60 <b>(-42.33%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1057.30 (n/a)</td><td>526.42 (n/a)</td><td>464.10 (n/a)</td><td>248.30 (n/a)</td><td>327.02 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (+17.91%)</td><td>0.01 (-12.03%)</td><td>0.01 (-18.99%)</td><td>0.01 (-15.40%)</td><td>0.00 <b>(+79.61%)</b></td><td>578.80 (+18.19%)</td><td>439.32 (+18.54%)</td><td>425.30 <b>(+23.45%)</b></td><td>274.30 (-15.18%)</td><td>114.36 <b>(+69.47%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>489.70 (n/a)</td><td>370.62 (n/a)</td><td>344.50 (n/a)</td><td>323.40 (n/a)</td><td>67.48 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>290.80 (n/a)</td><td>268.72 (n/a)</td><td>271.70 (n/a)</td><td>244.40 (n/a)</td><td>21.38 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>273.80 (n/a)</td><td>249.74 (n/a)</td><td>256.80 (n/a)</td><td>211.60 (n/a)</td><td>25.86 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1935.00 (n/a)</td><td>715.94 (n/a)</td><td>541.40 (n/a)</td><td>222.10 (n/a)</td><td>700.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>453.50 (n/a)</td><td>339.36 (n/a)</td><td>296.00 (n/a)</td><td>245.30 (n/a)</td><td>97.95 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>486.10 (n/a)</td><td>306.88 (n/a)</td><td>282.90 (n/a)</td><td>224.70 (n/a)</td><td>104.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>458.30 (n/a)</td><td>275.82 (n/a)</td><td>243.50 (n/a)</td><td>188.00 (n/a)</td><td>104.91 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.93 (-1.65%)</td><td>0.57 <b>(-28.74%)</b></td><td>0.65 (-16.47%)</td><td>0.13 <b>(-79.51%)</b></td><td>0.36 <b>(+181.70%)</b></td><td>3489.50 <b>(+388.11%)</b></td><td>1419.00 <b>(+140.26%)</b></td><td>704.20 (+19.72%)</td><td>492.80 (+1.67%)</td><td>1290.71 <b>(+1239.51%)</b></td><td>68.09 (-1.65%)</td><td>41.36 <b>(-28.74%)</b></td><td>47.65 (-16.47%)</td><td>9.62 <b>(-79.51%)</b></td><td>26.50 <b>(+181.70%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.95 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.64 (n/a)</td><td>0.13 (n/a)</td><td>714.90 (n/a)</td><td>590.60 (n/a)</td><td>588.20 (n/a)</td><td>484.70 (n/a)</td><td>96.36 (n/a)</td><td>69.23 (n/a)</td><td>58.04 (n/a)</td><td>57.05 (n/a)</td><td>46.94 (n/a)</td><td>9.41 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.13 (+0.04%)</td><td>0.72 <b>(-26.74%)</b></td><td>0.64 <b>(-32.58%)</b></td><td>0.35 <b>(-59.57%)</b></td><td>0.29 <b>(+178.80%)</b></td><td>1855.50 <b>(+147.33%)</b></td><td>1063.34 <b>(+57.22%)</b></td><td>1023.30 <b>(+48.33%)</b></td><td>577.50 (-0.05%)</td><td>487.87 <b>(+601.84%)</b></td><td>116.20 (+0.04%)</td><td>73.33 <b>(-26.74%)</b></td><td>65.58 <b>(-32.58%)</b></td><td>36.17 <b>(-59.57%)</b></td><td>30.04 <b>(+178.80%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.13 (n/a)</td><td>0.98 (n/a)</td><td>0.95 (n/a)</td><td>0.87 (n/a)</td><td>0.11 (n/a)</td><td>750.20 (n/a)</td><td>676.36 (n/a)</td><td>689.90 (n/a)</td><td>577.80 (n/a)</td><td>69.51 (n/a)</td><td>116.15 (n/a)</td><td>100.10 (n/a)</td><td>97.27 (n/a)</td><td>89.46 (n/a)</td><td>10.78 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.78 <b>(+27.01%)</b></td><td>1.09 (-11.33%)</td><td>0.99 <b>(-20.14%)</b></td><td>0.74 <b>(-30.53%)</b></td><td>0.40 <b>(+224.94%)</b></td><td>1022.70 <b>(+43.96%)</b></td><td>750.60 <b>(+21.63%)</b></td><td>761.80 <b>(+25.21%)</b></td><td>424.30 <b>(-21.27%)</b></td><td>214.10 <b>(+242.25%)</b></td><td>197.70 <b>(+27.01%)</b></td><td>121.49 (-11.33%)</td><td>110.12 <b>(-20.14%)</b></td><td>82.03 <b>(-30.53%)</b></td><td>44.30 <b>(+224.94%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.40 (n/a)</td><td>1.23 (n/a)</td><td>1.24 (n/a)</td><td>1.06 (n/a)</td><td>0.12 (n/a)</td><td>710.40 (n/a)</td><td>617.14 (n/a)</td><td>608.40 (n/a)</td><td>538.90 (n/a)</td><td>62.55 (n/a)</td><td>155.65 (n/a)</td><td>137.02 (n/a)</td><td>137.89 (n/a)</td><td>118.08 (n/a)</td><td>13.63 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.58 (+0.71%)</td><td>0.74 <b>(-43.40%)</b></td><td>0.32 <b>(-74.33%)</b></td><td>0.29 <b>(-73.68%)</b></td><td>0.61 <b>(+225.14%)</b></td><td>3578.40 <b>(+279.95%)</b></td><td>2386.58 <b>(+191.27%)</b></td><td>3301.20 <b>(+289.61%)</b></td><td>663.00 (-0.72%)</td><td>1478.68 <b>(+1220.88%)</b></td><td>202.43 (+0.71%)</td><td>94.18 <b>(-43.40%)</b></td><td>40.66 <b>(-74.33%)</b></td><td>37.51 <b>(-73.68%)</b></td><td>77.89 <b>(+225.14%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.57 (n/a)</td><td>1.30 (n/a)</td><td>1.24 (n/a)</td><td>1.11 (n/a)</td><td>0.19 (n/a)</td><td>941.80 (n/a)</td><td>819.36 (n/a)</td><td>847.30 (n/a)</td><td>667.80 (n/a)</td><td>111.95 (n/a)</td><td>200.99 (n/a)</td><td>166.41 (n/a)</td><td>158.40 (n/a)</td><td>142.51 (n/a)</td><td>23.96 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.67 (-4.17%)</td><td>1.33 (+4.57%)</td><td>1.26 (-5.13%)</td><td>0.90 <b>(+36.86%)</b></td><td>0.34 (-14.72%)</td><td>1165.30 <b>(-26.93%)</b></td><td>833.36 (-9.21%)</td><td>833.70 (+5.41%)</td><td>626.90 (+4.36%)</td><td>223.89 <b>(-42.54%)</b></td><td>214.11 (-4.17%)</td><td>170.16 (+4.57%)</td><td>161.00 (-5.13%)</td><td>115.18 <b>(+36.86%)</b></td><td>43.07 (-14.72%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.75 (n/a)</td><td>1.27 (n/a)</td><td>1.33 (n/a)</td><td>0.66 (n/a)</td><td>0.39 (n/a)</td><td>1594.80 (n/a)</td><td>917.88 (n/a)</td><td>790.90 (n/a)</td><td>600.70 (n/a)</td><td>389.68 (n/a)</td><td>223.43 (n/a)</td><td>162.73 (n/a)</td><td>169.71 (n/a)</td><td>84.16 (n/a)</td><td>50.50 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.54 (-17.89%)</td><td>1.10 (-0.68%)</td><td>1.27 (+16.60%)</td><td>0.30 <b>(-46.04%)</b></td><td>0.49 (-9.85%)</td><td>3439.70 <b>(+85.32%)</b></td><td>1350.84 (+16.97%)</td><td>826.20 (-14.24%)</td><td>678.70 <b>(+21.78%)</b></td><td>1176.02 <b>(+110.09%)</b></td><td>197.75 (-17.89%)</td><td>140.81 (-0.68%)</td><td>162.44 (+16.60%)</td><td>39.02 <b>(-46.04%)</b></td><td>62.42 (-9.85%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.88 (n/a)</td><td>1.11 (n/a)</td><td>1.09 (n/a)</td><td>0.56 (n/a)</td><td>0.54 (n/a)</td><td>1856.10 (n/a)</td><td>1154.90 (n/a)</td><td>963.40 (n/a)</td><td>557.30 (n/a)</td><td>559.78 (n/a)</td><td>240.84 (n/a)</td><td>141.77 (n/a)</td><td>139.31 (n/a)</td><td>72.31 (n/a)</td><td>69.24 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.78 (+14.01%)</td><td>1.46 <b>(+23.21%)</b></td><td>1.54 <b>(+28.05%)</b></td><td>0.90 (-5.22%)</td><td>0.33 <b>(+35.37%)</b></td><td>1162.90 (+5.51%)</td><td>760.84 (-16.89%)</td><td>681.60 <b>(-21.92%)</b></td><td>589.40 (-12.29%)</td><td>230.27 <b>(+28.91%)</b></td><td>227.72 (+14.01%)</td><td>186.64 <b>(+23.21%)</b></td><td>196.91 <b>(+28.05%)</b></td><td>115.41 (-5.22%)</td><td>42.83 <b>(+35.37%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.56 (n/a)</td><td>1.18 (n/a)</td><td>1.20 (n/a)</td><td>0.95 (n/a)</td><td>0.25 (n/a)</td><td>1102.20 (n/a)</td><td>915.50 (n/a)</td><td>872.90 (n/a)</td><td>672.00 (n/a)</td><td>178.63 (n/a)</td><td>199.74 (n/a)</td><td>151.49 (n/a)</td><td>153.77 (n/a)</td><td>121.77 (n/a)</td><td>31.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.78 (-3.74%)</td><td>0.50 (-9.44%)</td><td>0.47 (-6.31%)</td><td>0.29 <b>(-21.33%)</b></td><td>0.18 (+7.94%)</td><td>1223.40 <b>(+27.12%)</b></td><td>790.04 (+13.99%)</td><td>766.80 (+6.74%)</td><td>460.20 (+3.88%)</td><td>274.89 <b>(+45.19%)</b></td><td>36.46 (-3.74%)</td><td>23.37 (-9.44%)</td><td>21.88 (-6.31%)</td><td>13.71 <b>(-21.33%)</b></td><td>8.22 (+7.94%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.81 (n/a)</td><td>0.55 (n/a)</td><td>0.50 (n/a)</td><td>0.37 (n/a)</td><td>0.16 (n/a)</td><td>962.40 (n/a)</td><td>693.06 (n/a)</td><td>718.40 (n/a)</td><td>443.00 (n/a)</td><td>189.33 (n/a)</td><td>37.88 (n/a)</td><td>25.81 (n/a)</td><td>23.35 (n/a)</td><td>17.43 (n/a)</td><td>7.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>3.84 (+4.92%)</td><td>2.60 (+11.45%)</td><td>3.11 <b>(+32.22%)</b></td><td>1.16 (+5.35%)</td><td>1.32 (+7.39%)</td><td>2266.00 (-5.08%)</td><td>1330.76 (-9.35%)</td><td>842.00 <b>(-24.38%)</b></td><td>682.60 (-4.68%)</td><td>804.71 (-4.53%)</td><td>786.53 (+4.92%)</td><td>532.96 (+11.45%)</td><td>637.59 <b>(+32.22%)</b></td><td>236.92 (+5.35%)</td><td>270.26 (+7.39%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>3.66 (n/a)</td><td>2.33 (n/a)</td><td>2.35 (n/a)</td><td>1.10 (n/a)</td><td>1.23 (n/a)</td><td>2387.30 (n/a)</td><td>1468.02 (n/a)</td><td>1113.40 (n/a)</td><td>716.10 (n/a)</td><td>842.85 (n/a)</td><td>749.67 (n/a)</td><td>478.20 (n/a)</td><td>482.21 (n/a)</td><td>224.89 (n/a)</td><td>251.67 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.90 (n/a)</td><td>333.86 (n/a)</td><td>297.80 (n/a)</td><td>259.70 (n/a)</td><td>103.15 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.40 (n/a)</td><td>467.54 (n/a)</td><td>496.20 (n/a)</td><td>190.00 (n/a)</td><td>164.03 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>546.00 (n/a)</td><td>434.06 (n/a)</td><td>511.40 (n/a)</td><td>284.40 (n/a)</td><td>130.15 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1919.80 (n/a)</td><td>752.40 (n/a)</td><td>526.20 (n/a)</td><td>307.00 (n/a)</td><td>659.44 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>595.80 (n/a)</td><td>498.32 (n/a)</td><td>532.60 (n/a)</td><td>341.20 (n/a)</td><td>97.50 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>589.90 (n/a)</td><td>434.74 (n/a)</td><td>373.00 (n/a)</td><td>357.90 (n/a)</td><td>100.57 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.60 (+14.67%)</td><td>0.30 <b>(-36.02%)</b></td><td>0.21 <b>(-57.87%)</b></td><td>0.11 <b>(-72.17%)</b></td><td>0.20 <b>(+257.98%)</b></td><td>1963.30 <b>(+259.32%)</b></td><td>1047.00 <b>(+120.09%)</b></td><td>1056.20 <b>(+137.35%)</b></td><td>367.20 (-12.78%)</td><td>638.89 <b>(+973.67%)</b></td><td>25.70 (+14.67%)</td><td>12.85 <b>(-36.02%)</b></td><td>8.94 <b>(-57.87%)</b></td><td>4.81 <b>(-72.17%)</b></td><td>8.66 <b>(+257.98%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.53 (n/a)</td><td>0.47 (n/a)</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.06 (n/a)</td><td>546.40 (n/a)</td><td>475.72 (n/a)</td><td>445.00 (n/a)</td><td>421.00 (n/a)</td><td>59.50 (n/a)</td><td>22.41 (n/a)</td><td>20.08 (n/a)</td><td>21.21 (n/a)</td><td>17.27 (n/a)</td><td>2.42 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.54 (-5.94%)</td><td>0.45 (+9.08%)</td><td>0.47 (+9.85%)</td><td>0.34 <b>(+54.68%)</b></td><td>0.08 <b>(-41.81%)</b></td><td>647.90 <b>(-35.35%)</b></td><td>506.20 (-15.40%)</td><td>472.30 (-8.96%)</td><td>409.60 (+6.33%)</td><td>94.16 <b>(-61.13%)</b></td><td>23.04 (-5.94%)</td><td>19.13 (+9.08%)</td><td>19.98 (+9.85%)</td><td>14.56 <b>(+54.68%)</b></td><td>3.31 <b>(-41.81%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.57 (n/a)</td><td>0.41 (n/a)</td><td>0.43 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>1002.20 (n/a)</td><td>598.36 (n/a)</td><td>518.80 (n/a)</td><td>385.20 (n/a)</td><td>242.23 (n/a)</td><td>24.50 (n/a)</td><td>17.54 (n/a)</td><td>18.19 (n/a)</td><td>9.42 (n/a)</td><td>5.69 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.31 (+0.09%)</td><td>0.30 (-0.08%)</td><td>0.31 (+0.06%)</td><td>0.30 (-0.98%)</td><td>0.01 <b>(+59.81%)</b></td><td>84744.30 (+0.99%)</td><td>82618.42 (+0.10%)</td><td>82415.00 (-0.06%)</td><td>80823.50 (-0.09%)</td><td>1795.39 <b>(+61.15%)</b></td><td>212.56 (+0.09%)</td><td>208.02 (-0.08%)</td><td>208.46 (+0.06%)</td><td>202.73 (-0.98%)</td><td>4.51 <b>(+59.81%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83916.70 (n/a)</td><td>82532.32 (n/a)</td><td>82461.20 (n/a)</td><td>80896.30 (n/a)</td><td>1114.09 (n/a)</td><td>212.37 (n/a)</td><td>208.19 (n/a)</td><td>208.34 (n/a)</td><td>204.73 (n/a)</td><td>2.82 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.15 (-0.10%)</td><td>1.15 (+0.56%)</td><td>1.15 (+0.48%)</td><td>1.15 (+1.54%)</td><td>0.00 <b>(-83.87%)</b></td><td>21975.80 (-1.52%)</td><td>21934.02 (-0.56%)</td><td>21931.00 (-0.47%)</td><td>21910.60 (+0.10%)</td><td>25.33 <b>(-84.13%)</b></td><td>784.09 (-0.10%)</td><td>783.25 (+0.56%)</td><td>783.36 (+0.48%)</td><td>781.76 (+1.54%)</td><td>0.90 <b>(-83.87%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>1.14 (n/a)</td><td>1.13 (n/a)</td><td>0.01 (n/a)</td><td>22314.80 (n/a)</td><td>22057.70 (n/a)</td><td>22035.40 (n/a)</td><td>21888.10 (n/a)</td><td>159.61 (n/a)</td><td>784.89 (n/a)</td><td>778.89 (n/a)</td><td>779.65 (n/a)</td><td>769.89 (n/a)</td><td>5.61 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>4.04 (-2.98%)</td><td>2.86 (+4.14%)</td><td>2.80 <b>(+32.50%)</b></td><td>1.75 <b>(+34.15%)</b></td><td>0.99 <b>(-23.56%)</b></td><td>4600.60 <b>(-25.46%)</b></td><td>3121.74 (-12.23%)</td><td>2882.30 <b>(-24.53%)</b></td><td>1993.70 (+3.08%)</td><td>1116.27 <b>(-35.84%)</b></td><td>1060.28 (-2.98%)</td><td>749.66 (+4.14%)</td><td>733.43 <b>(+32.50%)</b></td><td>459.49 <b>(+34.15%)</b></td><td>258.76 <b>(-23.56%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>4.17 (n/a)</td><td>2.75 (n/a)</td><td>2.11 (n/a)</td><td>1.31 (n/a)</td><td>1.29 (n/a)</td><td>6171.70 (n/a)</td><td>3556.80 (n/a)</td><td>3819.00 (n/a)</td><td>1934.20 (n/a)</td><td>1739.87 (n/a)</td><td>1092.89 (n/a)</td><td>719.87 (n/a)</td><td>553.54 (n/a)</td><td>342.52 (n/a)</td><td>338.53 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.32 (+5.61%)</td><td>0.21 (+3.40%)</td><td>0.19 (+1.75%)</td><td>0.17 (+6.23%)</td><td>0.06 (+8.48%)</td><td>7135.60 (-5.86%)</td><td>6120.86 (-3.06%)</td><td>6416.00 (-1.72%)</td><td>3935.20 (-5.31%)</td><td>1262.78 (-3.18%)</td><td>17.05 (+5.61%)</td><td>11.48 (+3.40%)</td><td>10.46 (+1.75%)</td><td>9.40 (+6.23%)</td><td>3.15 (+8.48%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>7579.90 (n/a)</td><td>6313.86 (n/a)</td><td>6528.20 (n/a)</td><td>4155.90 (n/a)</td><td>1304.23 (n/a)</td><td>16.15 (n/a)</td><td>11.10 (n/a)</td><td>10.28 (n/a)</td><td>8.85 (n/a)</td><td>2.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>3.61 (n/a)</td><td>3.50 (n/a)</td><td>3.49 (n/a)</td><td>3.32 (n/a)</td><td>0.12 (n/a)</td><td>3.61 (n/a)</td><td>3.49 (n/a)</td><td>3.49 (n/a)</td><td>3.32 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>7.47 (-1.82%)</td><td>7.01 (+11.75%)</td><td>7.29 <b>(+24.56%)</b></td><td>6.00 <b>(+29.24%)</b></td><td>0.59 <b>(-52.69%)</b></td><td>7.46 (-1.82%)</td><td>7.01 (+11.75%)</td><td>7.28 <b>(+24.56%)</b></td><td>6.00 <b>(+29.24%)</b></td><td>0.59 <b>(-52.69%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>7.61 (n/a)</td><td>6.27 (n/a)</td><td>5.85 (n/a)</td><td>4.64 (n/a)</td><td>1.24 (n/a)</td><td>7.60 (n/a)</td><td>6.27 (n/a)</td><td>5.85 (n/a)</td><td>4.64 (n/a)</td><td>1.24 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>14.10 (+4.67%)</td><td>10.20 (-9.32%)</td><td>9.52 <b>(-23.09%)</b></td><td>8.32 (+14.79%)</td><td>2.39 (-10.72%)</td><td>14.10 (+4.67%)</td><td>10.20 (-9.32%)</td><td>9.51 <b>(-23.09%)</b></td><td>8.31 (+14.79%)</td><td>2.39 (-10.72%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>13.48 (n/a)</td><td>11.25 (n/a)</td><td>12.38 (n/a)</td><td>7.25 (n/a)</td><td>2.68 (n/a)</td><td>13.47 (n/a)</td><td>11.24 (n/a)</td><td>12.37 (n/a)</td><td>7.24 (n/a)</td><td>2.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>3.88 (n/a)</td><td>3.69 (n/a)</td><td>3.73 (n/a)</td><td>3.47 (n/a)</td><td>0.16 (n/a)</td><td>3.88 (n/a)</td><td>3.69 (n/a)</td><td>3.72 (n/a)</td><td>3.47 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>6.85 (-6.21%)</td><td>5.72 (-19.57%)</td><td>5.73 (-19.69%)</td><td>4.75 <b>(-29.86%)</b></td><td>0.85 <b>(+303.98%)</b></td><td>6.84 (-6.21%)</td><td>5.72 (-19.57%)</td><td>5.72 (-19.69%)</td><td>4.75 <b>(-29.86%)</b></td><td>0.84 <b>(+303.98%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>7.30 (n/a)</td><td>7.12 (n/a)</td><td>7.13 (n/a)</td><td>6.78 (n/a)</td><td>0.21 (n/a)</td><td>7.30 (n/a)</td><td>7.11 (n/a)</td><td>7.13 (n/a)</td><td>6.77 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>13.90 (+4.75%)</td><td>9.63 (-1.77%)</td><td>8.06 (-13.09%)</td><td>7.09 (-14.16%)</td><td>2.93 <b>(+43.48%)</b></td><td>13.89 (+4.75%)</td><td>9.63 (-1.77%)</td><td>8.05 (-13.09%)</td><td>7.08 (-14.16%)</td><td>2.93 <b>(+43.48%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>13.27 (n/a)</td><td>9.81 (n/a)</td><td>9.27 (n/a)</td><td>8.26 (n/a)</td><td>2.04 (n/a)</td><td>13.26 (n/a)</td><td>9.80 (n/a)</td><td>9.26 (n/a)</td><td>8.25 (n/a)</td><td>2.04 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>2.90 (-0.08%)</td><td>1.65 (+8.60%)</td><td>1.03 (-0.79%)</td><td>1.02 (+5.24%)</td><td>0.88 (+7.17%)</td><td>2.89 (-0.08%)</td><td>1.65 (+8.60%)</td><td>1.03 (-0.79%)</td><td>1.02 (+5.24%)</td><td>0.88 (+7.17%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>2.90 (n/a)</td><td>1.52 (n/a)</td><td>1.04 (n/a)</td><td>0.97 (n/a)</td><td>0.82 (n/a)</td><td>2.89 (n/a)</td><td>1.52 (n/a)</td><td>1.04 (n/a)</td><td>0.97 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.58 (-19.08%)</td><td>0.30 <b>(-35.33%)</b></td><td>0.33 <b>(-35.64%)</b></td><td>0.08 <b>(-71.26%)</b></td><td>0.20 (+10.32%)</td><td>0.57 (-19.08%)</td><td>0.30 <b>(-35.33%)</b></td><td>0.33 <b>(-35.64%)</b></td><td>0.08 <b>(-71.26%)</b></td><td>0.19 (+10.32%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.71 (n/a)</td><td>0.47 (n/a)</td><td>0.51 (n/a)</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.70 (n/a)</td><td>0.46 (n/a)</td><td>0.51 (n/a)</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.49 <b>(-21.38%)</b></td><td>0.32 <b>(-44.43%)</b></td><td>0.43 <b>(-29.20%)</b></td><td>0.08 <b>(-81.70%)</b></td><td>0.19 <b>(+160.29%)</b></td><td>0.48 <b>(-21.38%)</b></td><td>0.32 <b>(-44.43%)</b></td><td>0.43 <b>(-29.20%)</b></td><td>0.08 <b>(-81.70%)</b></td><td>0.19 <b>(+160.29%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.62 (n/a)</td><td>0.58 (n/a)</td><td>0.61 (n/a)</td><td>0.45 (n/a)</td><td>0.07 (n/a)</td><td>0.62 (n/a)</td><td>0.57 (n/a)</td><td>0.61 (n/a)</td><td>0.44 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>2.55 (-7.53%)</td><td>2.04 (+14.85%)</td><td>2.42 <b>(+52.44%)</b></td><td>0.45 (-1.78%)</td><td>0.89 (-1.83%)</td><td>2.51 (-7.53%)</td><td>2.01 (+14.85%)</td><td>2.38 <b>(+52.44%)</b></td><td>0.44 (-1.78%)</td><td>0.88 (-1.83%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>2.75 (n/a)</td><td>1.78 (n/a)</td><td>1.59 (n/a)</td><td>0.45 (n/a)</td><td>0.91 (n/a)</td><td>2.71 (n/a)</td><td>1.75 (n/a)</td><td>1.56 (n/a)</td><td>0.45 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>671.90 (n/a)</td><td>400.64 (n/a)</td><td>304.40 (n/a)</td><td>272.40 (n/a)</td><td>171.54 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.50 (n/a)</td><td>347.46 (n/a)</td><td>298.00 (n/a)</td><td>264.30 (n/a)</td><td>98.84 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>629.30 (n/a)</td><td>499.58 (n/a)</td><td>501.00 (n/a)</td><td>337.20 (n/a)</td><td>115.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.10 (n/a)</td><td>421.00 (n/a)</td><td>476.50 (n/a)</td><td>232.90 (n/a)</td><td>115.10 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.60 (n/a)</td><td>383.34 (n/a)</td><td>301.00 (n/a)</td><td>262.10 (n/a)</td><td>131.97 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>496.10 (n/a)</td><td>408.18 (n/a)</td><td>388.60 (n/a)</td><td>327.00 (n/a)</td><td>70.22 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 <b>(-32.92%)</b></td><td>0.02 <b>(-22.27%)</b></td><td>0.03 <b>(-20.87%)</b></td><td>0.01 <b>(-28.15%)</b></td><td>0.01 <b>(-34.69%)</b></td><td>800.40 <b>(+39.18%)</b></td><td>420.20 <b>(+23.35%)</b></td><td>307.20 <b>(+26.37%)</b></td><td>247.50 <b>(+49.10%)</b></td><td>233.11 <b>(+24.49%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>575.10 (n/a)</td><td>340.66 (n/a)</td><td>243.10 (n/a)</td><td>166.00 (n/a)</td><td>187.25 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (+5.50%)</td><td>0.03 <b>(+23.83%)</b></td><td>0.03 <b>(+45.39%)</b></td><td>0.02 <b>(+45.07%)</b></td><td>0.01 (-12.61%)</td><td>432.20 <b>(-31.07%)</b></td><td>334.30 <b>(-22.00%)</b></td><td>298.70 <b>(-31.22%)</b></td><td>250.90 (-5.21%)</td><td>77.89 <b>(-40.69%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.00 (n/a)</td><td>428.60 (n/a)</td><td>434.30 (n/a)</td><td>264.70 (n/a)</td><td>131.33 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 <b>(-41.69%)</b></td><td>0.02 <b>(-27.77%)</b></td><td>0.03 (-19.23%)</td><td>0.01 <b>(-34.38%)</b></td><td>0.01 <b>(-40.34%)</b></td><td>759.50 <b>(+52.39%)</b></td><td>407.70 <b>(+32.22%)</b></td><td>263.60 <b>(+23.81%)</b></td><td>255.60 <b>(+71.54%)</b></td><td>221.74 <b>(+31.42%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>498.40 (n/a)</td><td>308.36 (n/a)</td><td>212.90 (n/a)</td><td>149.00 (n/a)</td><td>168.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 <b>(-26.73%)</b></td><td>0.03 (-1.09%)</td><td>0.03 <b>(+30.46%)</b></td><td>0.02 <b>(+27.72%)</b></td><td>0.01 <b>(-47.25%)</b></td><td>410.00 <b>(-21.71%)</b></td><td>317.88 (-8.37%)</td><td>286.10 <b>(-23.34%)</b></td><td>226.30 <b>(+36.49%)</b></td><td>83.75 <b>(-38.19%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.70 (n/a)</td><td>346.90 (n/a)</td><td>373.20 (n/a)</td><td>165.80 (n/a)</td><td>135.50 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 <b>(-37.23%)</b></td><td>0.02 (-18.44%)</td><td>0.03 <b>(+21.25%)</b></td><td>0.02 (-16.13%)</td><td>0.01 <b>(-50.83%)</b></td><td>526.50 (+19.23%)</td><td>361.86 (+13.24%)</td><td>297.30 (-17.53%)</td><td>261.00 <b>(+59.34%)</b></td><td>114.25 (-7.97%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>441.60 (n/a)</td><td>319.56 (n/a)</td><td>360.50 (n/a)</td><td>163.80 (n/a)</td><td>124.14 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (+2.70%)</td><td>0.02 <b>(+36.20%)</b></td><td>0.02 (+10.19%)</td><td>0.02 <b>(+355.21%)</b></td><td>0.01 <b>(-39.75%)</b></td><td>535.40 <b>(-78.03%)</b></td><td>440.68 <b>(-53.80%)</b></td><td>476.90 (-9.27%)</td><td>273.20 (-2.64%)</td><td>99.89 <b>(-88.53%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2437.30 (n/a)</td><td>953.92 (n/a)</td><td>525.60 (n/a)</td><td>280.60 (n/a)</td><td>870.64 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (-12.95%)</td><td>0.02 (-1.34%)</td><td>0.02 (-10.18%)</td><td>0.01 <b>(+140.11%)</b></td><td>0.01 <b>(-30.80%)</b></td><td>984.00 <b>(-58.35%)</b></td><td>558.24 <b>(-32.03%)</b></td><td>495.20 (+11.33%)</td><td>284.70 (+14.89%)</td><td>258.32 <b>(-70.34%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2362.60 (n/a)</td><td>821.28 (n/a)</td><td>444.80 (n/a)</td><td>247.80 (n/a)</td><td>870.98 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 <b>(-37.25%)</b></td><td>0.02 <b>(-23.05%)</b></td><td>0.02 (-8.74%)</td><td>0.01 <b>(-50.31%)</b></td><td>0.01 <b>(-31.93%)</b></td><td>1061.40 <b>(+101.25%)</b></td><td>550.30 <b>(+36.23%)</b></td><td>474.80 (+9.58%)</td><td>355.20 <b>(+59.35%)</b></td><td>292.26 <b>(+119.34%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.40 (n/a)</td><td>403.94 (n/a)</td><td>433.30 (n/a)</td><td>222.90 (n/a)</td><td>133.24 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (-8.31%)</td><td>0.02 <b>(-27.50%)</b></td><td>0.02 <b>(-42.62%)</b></td><td>0.01 <b>(-34.96%)</b></td><td>0.01 <b>(+24.20%)</b></td><td>789.20 <b>(+53.75%)</b></td><td>477.56 <b>(+53.80%)</b></td><td>488.40 <b>(+74.30%)</b></td><td>229.60 (+9.07%)</td><td>226.10 <b>(+91.03%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.30 (n/a)</td><td>310.50 (n/a)</td><td>280.20 (n/a)</td><td>210.50 (n/a)</td><td>118.35 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (+5.95%)</td><td>0.02 (-14.88%)</td><td>0.02 <b>(-30.95%)</b></td><td>0.01 <b>(+48.05%)</b></td><td>0.01 (-14.42%)</td><td>691.60 <b>(-32.45%)</b></td><td>488.92 (+2.11%)</td><td>542.40 <b>(+44.83%)</b></td><td>223.90 (-5.61%)</td><td>176.21 <b>(-45.98%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1023.90 (n/a)</td><td>478.80 (n/a)</td><td>374.50 (n/a)</td><td>237.20 (n/a)</td><td>326.19 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (+3.89%)</td><td>0.02 (+14.37%)</td><td>0.02 (+16.63%)</td><td>0.02 (+0.80%)</td><td>0.01 (+4.63%)</td><td>503.30 (-0.79%)</td><td>383.10 (-12.00%)</td><td>418.60 (-14.26%)</td><td>219.90 (-3.72%)</td><td>122.73 (+4.08%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.30 (n/a)</td><td>435.32 (n/a)</td><td>488.20 (n/a)</td><td>228.40 (n/a)</td><td>117.92 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (+6.63%)</td><td>0.02 (+11.90%)</td><td>0.02 (+5.38%)</td><td>0.01 (+15.31%)</td><td>0.01 (+14.65%)</td><td>690.00 (-13.28%)</td><td>443.60 (-10.48%)</td><td>386.60 (-5.11%)</td><td>298.40 (-6.22%)</td><td>169.00 (-12.11%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>795.70 (n/a)</td><td>495.52 (n/a)</td><td>407.40 (n/a)</td><td>318.20 (n/a)</td><td>192.30 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (-8.55%)</td><td>0.02 (-1.59%)</td><td>0.02 (-3.87%)</td><td>0.02 (+14.66%)</td><td>0.01 (-17.36%)</td><td>509.80 (-12.80%)</td><td>404.32 (-2.54%)</td><td>486.30 (+4.02%)</td><td>239.80 (+9.35%)</td><td>127.98 (-18.14%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.60 (n/a)</td><td>414.86 (n/a)</td><td>467.50 (n/a)</td><td>219.30 (n/a)</td><td>156.34 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 <b>(+22.69%)</b></td><td>0.02 <b>(+30.46%)</b></td><td>0.02 <b>(+40.58%)</b></td><td>0.01 <b>(+40.14%)</b></td><td>0.00 <b>(+20.57%)</b></td><td>562.90 <b>(-28.64%)</b></td><td>453.98 <b>(-23.70%)</b></td><td>402.20 <b>(-28.86%)</b></td><td>370.80 (-18.51%)</td><td>88.26 <b>(-29.70%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>788.80 (n/a)</td><td>595.02 (n/a)</td><td>565.40 (n/a)</td><td>455.00 (n/a)</td><td>125.56 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.11 (-9.67%)</td><td>0.10 (-6.68%)</td><td>0.10 (-0.45%)</td><td>0.08 (-12.24%)</td><td>0.01 (+16.93%)</td><td>298.40 (+13.94%)</td><td>256.38 (+7.67%)</td><td>245.00 (+0.45%)</td><td>229.00 (+10.74%)</td><td>30.97 <b>(+47.39%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>261.90 (n/a)</td><td>238.12 (n/a)</td><td>243.90 (n/a)</td><td>206.80 (n/a)</td><td>21.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.18 (-2.91%)</td><td>0.14 (-7.13%)</td><td>0.16 (+4.48%)</td><td>0.07 (-19.53%)</td><td>0.05 <b>(+32.91%)</b></td><td>555.50 <b>(+24.27%)</b></td><td>338.08 (+14.20%)</td><td>250.40 (-4.28%)</td><td>233.40 (+2.96%)</td><td>139.93 <b>(+59.01%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>447.00 (n/a)</td><td>296.04 (n/a)</td><td>261.60 (n/a)</td><td>226.70 (n/a)</td><td>88.00 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (-3.13%)</td><td>0.02 (+0.85%)</td><td>0.02 (-10.12%)</td><td>0.02 <b>(+44.34%)</b></td><td>0.00 <b>(-62.12%)</b></td><td>283.80 <b>(-30.71%)</b></td><td>265.68 (-4.64%)</td><td>272.70 (+11.26%)</td><td>243.40 (+3.22%)</td><td>19.65 <b>(-73.49%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>409.60 (n/a)</td><td>278.62 (n/a)</td><td>245.10 (n/a)</td><td>235.80 (n/a)</td><td>74.11 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (+19.56%)</td><td>0.03 <b>(+20.38%)</b></td><td>0.03 (+15.91%)</td><td>0.02 (+5.18%)</td><td>0.01 <b>(+24.68%)</b></td><td>465.20 (-4.91%)</td><td>305.84 (-15.93%)</td><td>270.50 (-13.72%)</td><td>229.40 (-16.37%)</td><td>93.15 (+2.23%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>489.20 (n/a)</td><td>363.80 (n/a)</td><td>313.50 (n/a)</td><td>274.30 (n/a)</td><td>91.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.05 <b>(+29.58%)</b></td><td>0.04 <b>(+53.26%)</b></td><td>0.04 <b>(+74.90%)</b></td><td>0.02 <b>(+278.07%)</b></td><td>0.01 (+9.50%)</td><td>648.10 <b>(-73.55%)</b></td><td>394.30 <b>(-54.20%)</b></td><td>293.50 <b>(-42.83%)</b></td><td>232.20 <b>(-22.81%)</b></td><td>175.69 <b>(-80.35%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2450.30 (n/a)</td><td>860.86 (n/a)</td><td>513.40 (n/a)</td><td>300.80 (n/a)</td><td>894.16 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (-7.66%)</td><td>0.02 (+12.95%)</td><td>0.03 <b>(+54.58%)</b></td><td>0.01 <b>(+26.21%)</b></td><td>0.01 (-11.29%)</td><td>634.70 <b>(-20.77%)</b></td><td>375.12 (-15.65%)</td><td>280.40 <b>(-35.32%)</b></td><td>249.60 (+8.29%)</td><td>163.28 <b>(-25.51%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>801.10 (n/a)</td><td>444.72 (n/a)</td><td>433.50 (n/a)</td><td>230.50 (n/a)</td><td>219.19 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (-8.91%)</td><td>0.03 (-2.24%)</td><td>0.02 (-8.88%)</td><td>0.02 (+14.54%)</td><td>0.01 (-14.42%)</td><td>517.00 (-12.68%)</td><td>405.88 (-0.80%)</td><td>459.30 (+9.75%)</td><td>242.50 (+9.78%)</td><td>128.59 (-14.91%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>592.10 (n/a)</td><td>409.14 (n/a)</td><td>418.50 (n/a)</td><td>220.90 (n/a)</td><td>151.12 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (+15.25%)</td><td>0.03 <b>(+26.83%)</b></td><td>0.03 <b>(+29.55%)</b></td><td>0.02 <b>(+28.55%)</b></td><td>0.01 (-0.49%)</td><td>450.70 <b>(-22.21%)</b></td><td>315.74 <b>(-23.84%)</b></td><td>313.20 <b>(-22.80%)</b></td><td>230.50 (-13.22%)</td><td>91.78 <b>(-35.47%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.40 (n/a)</td><td>414.58 (n/a)</td><td>405.70 (n/a)</td><td>265.60 (n/a)</td><td>142.23 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.05 <b>(+46.35%)</b></td><td>0.03 <b>(+39.01%)</b></td><td>0.04 <b>(+62.05%)</b></td><td>0.02 (-1.31%)</td><td>0.01 <b>(+101.45%)</b></td><td>511.20 (+1.33%)</td><td>337.24 <b>(-21.66%)</b></td><td>291.40 <b>(-38.29%)</b></td><td>190.60 <b>(-31.66%)</b></td><td>136.86 <b>(+45.30%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.50 (n/a)</td><td>430.46 (n/a)</td><td>472.20 (n/a)</td><td>278.90 (n/a)</td><td>94.20 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 (-9.53%)</td><td>0.03 (+17.45%)</td><td>0.03 (+18.68%)</td><td>0.02 <b>(+43.19%)</b></td><td>0.00 <b>(-55.09%)</b></td><td>363.60 <b>(-30.16%)</b></td><td>293.46 <b>(-21.86%)</b></td><td>284.10 (-15.75%)</td><td>244.60 (+10.53%)</td><td>43.55 <b>(-66.42%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.60 (n/a)</td><td>375.56 (n/a)</td><td>337.20 (n/a)</td><td>221.30 (n/a)</td><td>129.71 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (-10.18%)</td><td>0.03 (+9.91%)</td><td>0.03 <b>(+40.04%)</b></td><td>0.02 (+6.80%)</td><td>0.01 <b>(-33.85%)</b></td><td>460.20 (-6.35%)</td><td>320.68 (-13.50%)</td><td>296.30 <b>(-28.59%)</b></td><td>234.40 (+11.35%)</td><td>83.99 <b>(-28.07%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.40 (n/a)</td><td>370.74 (n/a)</td><td>414.90 (n/a)</td><td>210.50 (n/a)</td><td>116.77 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 <b>(-23.00%)</b></td><td>0.02 <b>(-22.71%)</b></td><td>0.02 <b>(+41.26%)</b></td><td>0.00 <b>(-69.73%)</b></td><td>0.01 <b>(-29.06%)</b></td><td>2020.00 <b>(+230.39%)</b></td><td>686.70 <b>(+70.13%)</b></td><td>366.40 <b>(-29.21%)</b></td><td>228.60 <b>(+29.89%)</b></td><td>751.52 <b>(+266.00%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>611.40 (n/a)</td><td>403.64 (n/a)</td><td>517.60 (n/a)</td><td>176.00 (n/a)</td><td>205.33 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.03 <b>(-29.13%)</b></td><td>0.02 <b>(-31.62%)</b></td><td>0.02 (-17.78%)</td><td>0.02 (+0.78%)</td><td>0.01 <b>(-53.11%)</b></td><td>604.10 (-0.77%)</td><td>521.86 <b>(+27.40%)</b></td><td>569.40 <b>(+21.61%)</b></td><td>295.50 <b>(+41.12%)</b></td><td>128.06 <b>(-31.85%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>608.80 (n/a)</td><td>409.62 (n/a)</td><td>468.20 (n/a)</td><td>209.40 (n/a)</td><td>187.92 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.04 (+8.45%)</td><td>0.02 (+17.98%)</td><td>0.02 <b>(+34.00%)</b></td><td>0.02 (+16.96%)</td><td>0.01 (-0.31%)</td><td>517.40 (-14.51%)</td><td>401.66 (-17.72%)</td><td>417.10 <b>(-25.37%)</b></td><td>205.60 (-7.80%)</td><td>123.33 <b>(-21.45%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.20 (n/a)</td><td>488.14 (n/a)</td><td>558.90 (n/a)</td><td>223.00 (n/a)</td><td>156.99 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.42 (+19.14%)</td><td>0.30 (+10.58%)</td><td>0.32 (+0.22%)</td><td>0.15 (+1.07%)</td><td>0.11 <b>(+26.21%)</b></td><td>638.70 (-1.05%)</td><td>377.90 (-6.64%)</td><td>311.10 (-0.22%)</td><td>236.90 (-16.05%)</td><td>170.59 (+5.45%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.32 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>645.50 (n/a)</td><td>404.76 (n/a)</td><td>311.80 (n/a)</td><td>282.20 (n/a)</td><td>161.78 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.49 <b>(+32.59%)</b></td><td>0.27 (+17.82%)</td><td>0.23 (+16.68%)</td><td>0.14 (-19.71%)</td><td>0.14 <b>(+73.98%)</b></td><td>678.30 <b>(+24.55%)</b></td><td>430.60 (-5.15%)</td><td>436.30 (-14.28%)</td><td>199.80 <b>(-24.60%)</b></td><td>187.99 <b>(+64.17%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.37 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>544.60 (n/a)</td><td>454.00 (n/a)</td><td>509.00 (n/a)</td><td>265.00 (n/a)</td><td>114.51 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.35 (-7.71%)</td><td>0.23 (+2.55%)</td><td>0.22 (+10.65%)</td><td>0.17 (+3.03%)</td><td>0.07 <b>(-20.21%)</b></td><td>568.70 (-2.94%)</td><td>450.14 (-5.08%)</td><td>449.70 (-9.63%)</td><td>284.10 (+8.39%)</td><td>109.20 (-15.48%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.38 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>585.90 (n/a)</td><td>474.24 (n/a)</td><td>497.60 (n/a)</td><td>262.10 (n/a)</td><td>129.19 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.28 (-2.45%)</td><td>0.19 (-13.64%)</td><td>0.15 <b>(-41.53%)</b></td><td>0.11 (-16.08%)</td><td>0.08 (+8.20%)</td><td>642.20 (+19.15%)</td><td>439.56 (+19.22%)</td><td>496.80 <b>(+71.02%)</b></td><td>260.50 (+2.52%)</td><td>165.20 <b>(+22.70%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>539.00 (n/a)</td><td>368.70 (n/a)</td><td>290.50 (n/a)</td><td>254.10 (n/a)</td><td>134.63 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.27 (-4.91%)</td><td>0.15 (-14.08%)</td><td>0.16 (+10.97%)</td><td>0.04 <b>(-70.25%)</b></td><td>0.11 <b>(+74.56%)</b></td><td>1944.30 <b>(+236.09%)</b></td><td>960.08 <b>(+111.92%)</b></td><td>448.90 (-9.88%)</td><td>275.30 (+5.16%)</td><td>852.18 <b>(+570.51%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>578.50 (n/a)</td><td>453.04 (n/a)</td><td>498.10 (n/a)</td><td>261.80 (n/a)</td><td>127.09 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.30 <b>(+26.19%)</b></td><td>0.21 (+9.48%)</td><td>0.24 <b>(+30.92%)</b></td><td>0.12 <b>(-22.39%)</b></td><td>0.08 <b>(+89.92%)</b></td><td>621.60 <b>(+28.86%)</b></td><td>394.50 (-0.43%)</td><td>304.10 <b>(-23.63%)</b></td><td>244.10 <b>(-20.77%)</b></td><td>159.44 <b>(+98.38%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>482.40 (n/a)</td><td>396.20 (n/a)</td><td>398.20 (n/a)</td><td>308.10 (n/a)</td><td>80.37 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.54 (+9.13%)</td><td>0.38 (+13.91%)</td><td>0.42 <b>(+57.05%)</b></td><td>0.26 <b>(+23.59%)</b></td><td>0.12 (-12.98%)</td><td>510.90 (-19.08%)</td><td>376.98 (-16.27%)</td><td>311.90 <b>(-36.32%)</b></td><td>244.60 (-8.36%)</td><td>124.15 <b>(-27.28%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.49 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>631.40 (n/a)</td><td>450.24 (n/a)</td><td>489.80 (n/a)</td><td>266.90 (n/a)</td><td>170.73 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.63 (-10.82%)</td><td>0.37 (+4.16%)</td><td>0.27 (+18.74%)</td><td>0.22 <b>(+22.49%)</b></td><td>0.18 (-18.52%)</td><td>596.70 (-18.36%)</td><td>425.04 (-11.45%)</td><td>481.00 (-15.79%)</td><td>207.20 (+12.18%)</td><td>172.72 <b>(-22.72%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.71 (n/a)</td><td>0.35 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.22 (n/a)</td><td>730.90 (n/a)</td><td>479.98 (n/a)</td><td>571.20 (n/a)</td><td>184.70 (n/a)</td><td>223.50 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.47 (-13.94%)</td><td>0.28 (-7.67%)</td><td>0.27 (+6.30%)</td><td>0.12 <b>(-41.67%)</b></td><td>0.12 (-10.11%)</td><td>1054.20 <b>(+71.41%)</b></td><td>557.32 (+15.81%)</td><td>486.40 (-5.94%)</td><td>278.60 (+16.18%)</td><td>291.79 <b>(+102.40%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.55 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>615.00 (n/a)</td><td>481.24 (n/a)</td><td>517.10 (n/a)</td><td>239.80 (n/a)</td><td>144.16 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (-12.99%)</td><td>0.01 (-14.90%)</td><td>0.01 <b>(-37.23%)</b></td><td>0.01 <b>(+29.07%)</b></td><td>0.00 <b>(-23.07%)</b></td><td>504.90 <b>(-22.51%)</b></td><td>386.90 (+9.80%)</td><td>411.80 <b>(+59.30%)</b></td><td>264.30 (+14.91%)</td><td>114.83 <b>(-34.64%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>651.60 (n/a)</td><td>352.38 (n/a)</td><td>258.50 (n/a)</td><td>230.00 (n/a)</td><td>175.69 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 <b>(-30.02%)</b></td><td>0.01 <b>(-33.30%)</b></td><td>0.01 <b>(-29.96%)</b></td><td>0.00 <b>(-78.60%)</b></td><td>0.01 (+5.58%)</td><td>2057.40 <b>(+367.17%)</b></td><td>710.66 <b>(+137.11%)</b></td><td>451.10 <b>(+42.80%)</b></td><td>245.90 <b>(+42.88%)</b></td><td>761.20 <b>(+673.61%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>440.40 (n/a)</td><td>299.72 (n/a)</td><td>315.90 (n/a)</td><td>172.10 (n/a)</td><td>98.40 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.01 (-8.77%)</td><td>0.01 (-15.97%)</td><td>0.01 (-19.60%)</td><td>0.01 (-10.78%)</td><td>0.00 <b>(-25.94%)</b></td><td>618.80 (+12.10%)</td><td>424.30 (+15.64%)</td><td>416.30 <b>(+24.38%)</b></td><td>274.90 (+9.61%)</td><td>123.91 (-4.62%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>552.00 (n/a)</td><td>366.90 (n/a)</td><td>334.70 (n/a)</td><td>250.80 (n/a)</td><td>129.91 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.51 (+0.60%)</td><td>0.36 (-0.67%)</td><td>0.34 (+6.10%)</td><td>0.24 (-6.12%)</td><td>0.10 (-9.17%)</td><td>539.60 (+6.51%)</td><td>385.42 (-0.19%)</td><td>383.80 (-5.75%)</td><td>259.60 (-0.57%)</td><td>101.37 (-3.02%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.51 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>506.60 (n/a)</td><td>386.16 (n/a)</td><td>407.20 (n/a)</td><td>261.10 (n/a)</td><td>104.52 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.74 <b>(+28.95%)</b></td><td>0.54 <b>(+39.51%)</b></td><td>0.50 <b>(+27.29%)</b></td><td>0.42 <b>(+94.23%)</b></td><td>0.12 <b>(-24.83%)</b></td><td>313.10 <b>(-48.51%)</b></td><td>251.50 <b>(-36.37%)</b></td><td>262.20 <b>(-21.43%)</b></td><td>178.20 <b>(-22.45%)</b></td><td>50.03 <b>(-71.32%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.57 (n/a)</td><td>0.39 (n/a)</td><td>0.40 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>608.10 (n/a)</td><td>395.28 (n/a)</td><td>333.70 (n/a)</td><td>229.80 (n/a)</td><td>174.46 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.53 (+4.00%)</td><td>0.36 (-16.00%)</td><td>0.31 <b>(-34.19%)</b></td><td>0.29 (+14.15%)</td><td>0.10 (-1.90%)</td><td>462.70 (-12.38%)</td><td>389.20 (+17.26%)</td><td>431.40 <b>(+51.95%)</b></td><td>251.20 (-3.83%)</td><td>86.64 <b>(-21.95%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.51 (n/a)</td><td>0.42 (n/a)</td><td>0.47 (n/a)</td><td>0.25 (n/a)</td><td>0.10 (n/a)</td><td>528.10 (n/a)</td><td>331.90 (n/a)</td><td>283.90 (n/a)</td><td>261.20 (n/a)</td><td>111.01 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.54 (+16.81%)</td><td>0.38 (+3.59%)</td><td>0.33 (+2.65%)</td><td>0.28 (+2.54%)</td><td>0.10 <b>(+22.39%)</b></td><td>470.60 (-2.47%)</td><td>369.60 (-2.35%)</td><td>403.80 (-2.58%)</td><td>244.10 (-14.38%)</td><td>89.89 (+4.91%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.09 (n/a)</td><td>482.50 (n/a)</td><td>378.50 (n/a)</td><td>414.50 (n/a)</td><td>285.10 (n/a)</td><td>85.68 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.56 (+1.83%)</td><td>0.51 <b>(+24.22%)</b></td><td>0.52 <b>(+27.88%)</b></td><td>0.40 <b>(+40.50%)</b></td><td>0.06 <b>(-37.92%)</b></td><td>331.50 <b>(-28.82%)</b></td><td>264.70 <b>(-22.40%)</b></td><td>255.00 <b>(-21.80%)</b></td><td>237.40 (-1.78%)</td><td>38.37 <b>(-55.98%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.55 (n/a)</td><td>0.41 (n/a)</td><td>0.41 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>465.70 (n/a)</td><td>341.12 (n/a)</td><td>326.10 (n/a)</td><td>241.70 (n/a)</td><td>87.17 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (+11.68%)</td><td>0.01 <b>(+39.37%)</b></td><td>0.01 <b>(+60.32%)</b></td><td>0.01 <b>(+41.84%)</b></td><td>0.00 (-14.22%)</td><td>445.20 <b>(-29.50%)</b></td><td>298.06 <b>(-31.98%)</b></td><td>277.30 <b>(-37.63%)</b></td><td>219.20 (-10.46%)</td><td>86.98 <b>(-42.64%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>631.50 (n/a)</td><td>438.20 (n/a)</td><td>444.60 (n/a)</td><td>244.80 (n/a)</td><td>151.62 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.02 (+9.66%)</td><td>0.02 <b>(+27.16%)</b></td><td>0.02 <b>(+57.84%)</b></td><td>0.01 (+6.72%)</td><td>0.00 (-4.60%)</td><td>438.70 (-6.28%)</td><td>287.74 <b>(-22.41%)</b></td><td>269.70 <b>(-36.63%)</b></td><td>219.50 (-8.81%)</td><td>87.16 (-14.96%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>468.10 (n/a)</td><td>370.84 (n/a)</td><td>425.60 (n/a)</td><td>240.70 (n/a)</td><td>102.50 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+24.72%)</b></td><td>19326.93 (-9.49%)</td><td>13178.37 (-1.92%)</td><td>14730.90 (-0.66%)</td><td>7025.94 (-2.92%)</td><td>5808.95 (+2.97%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21353.13 (n/a)</td><td>13436.13 (n/a)</td><td>14829.01 (n/a)</td><td>7237.07 (n/a)</td><td>5641.35 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.00 (-8.33%)</td><td>0.00 <b>(-28.57%)</b></td><td>0.00 <b>(-54.55%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-29.94%)</b></td><td>18580.78 (-18.12%)</td><td>14807.40 (+16.85%)</td><td>15464.91 <b>(+103.34%)</b></td><td>7621.59 (+12.69%)</td><td>4229.27 <b>(-44.10%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22691.68 (n/a)</td><td>12672.56 (n/a)</td><td>7605.39 (n/a)</td><td>6763.08 (n/a)</td><td>7566.05 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>0.13 (-15.41%)</td><td>0.09 <b>(-20.54%)</b></td><td>0.09 <b>(-33.86%)</b></td><td>0.08 (+1.27%)</td><td>0.02 <b>(-45.34%)</b></td><td>26281.37 (-1.22%)</td><td>22914.76 (+18.64%)</td><td>23906.45 <b>(+51.13%)</b></td><td>16251.10 (+18.18%)</td><td>4112.61 <b>(-38.26%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>26607.02 (n/a)</td><td>19314.01 (n/a)</td><td>15818.70 (n/a)</td><td>13751.14 (n/a)</td><td>6661.03 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.84 (+8.98%)</td><td>1.04 (-8.42%)</td><td>0.93 <b>(-21.27%)</b></td><td>0.59 (-9.29%)</td><td>0.48 <b>(+26.67%)</b></td><td>883.60 (+10.26%)</td><td>578.90 (+14.09%)</td><td>565.20 <b>(+27.01%)</b></td><td>284.80 (-8.25%)</td><td>219.58 (+19.63%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.69 (n/a)</td><td>1.14 (n/a)</td><td>1.18 (n/a)</td><td>0.65 (n/a)</td><td>0.38 (n/a)</td><td>801.40 (n/a)</td><td>507.42 (n/a)</td><td>445.00 (n/a)</td><td>310.40 (n/a)</td><td>183.55 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>2.42 <b>(-23.65%)</b></td><td>1.08 <b>(-41.63%)</b></td><td>1.04 <b>(-57.18%)</b></td><td>0.29 (-1.90%)</td><td>0.88 <b>(-26.18%)</b></td><td>3591.90 (+1.94%)</td><td>1861.10 <b>(+59.10%)</b></td><td>1007.90 <b>(+133.53%)</b></td><td>433.30 <b>(+30.99%)</b></td><td>1551.54 (+14.54%)</td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>3.17 (n/a)</td><td>1.85 (n/a)</td><td>2.43 (n/a)</td><td>0.30 (n/a)</td><td>1.19 (n/a)</td><td>3523.70 (n/a)</td><td>1169.80 (n/a)</td><td>431.60 (n/a)</td><td>330.80 (n/a)</td><td>1354.58 (n/a)</td>
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
<td><code>0c0eaee</code> — 2026-09-18 00:02:08</td><td>1.69 (-5.64%)</td><td>1.04 <b>(-23.56%)</b></td><td>0.96 <b>(-26.99%)</b></td><td>0.16 <b>(-82.28%)</b></td><td>0.61 <b>(+65.74%)</b></td><td>3217.80 <b>(+464.33%)</b></td><td>1007.94 <b>(+145.04%)</b></td><td>544.00 <b>(+36.96%)</b></td><td>310.20 (+5.98%)</td><td>1242.32 <b>(+982.49%)</b></td>
</tr>
<tr>
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.79 (n/a)</td><td>1.35 (n/a)</td><td>1.32 (n/a)</td><td>0.92 (n/a)</td><td>0.37 (n/a)</td><td>570.20 (n/a)</td><td>411.34 (n/a)</td><td>397.20 (n/a)</td><td>292.70 (n/a)</td><td>114.76 (n/a)</td>
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
