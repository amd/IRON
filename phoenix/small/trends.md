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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.05 (-6.52%)</td><td>0.04 (-11.80%)</td><td>0.04 (-15.70%)</td><td>0.02 (-0.75%)</td><td>0.01 (-9.92%)</td><td>618.80 (+0.75%)</td><td>366.02 (+11.27%)</td><td>291.70 (+18.63%)</td><td>251.90 (+6.96%)</td><td>154.55 (-4.96%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>614.20 (n/a)</td><td>328.94 (n/a)</td><td>245.90 (n/a)</td><td>235.50 (n/a)</td><td>162.61 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 <b>(-48.28%)</b></td><td>0.02 <b>(-54.07%)</b></td><td>0.02 <b>(-53.80%)</b></td><td>0.01 <b>(-77.89%)</b></td><td>0.01 <b>(-24.13%)</b></td><td>1931.30 <b>(+352.30%)</b></td><td>789.30 <b>(+177.65%)</b></td><td>517.10 <b>(+116.45%)</b></td><td>405.20 <b>(+93.32%)</b></td><td>642.37 <b>(+628.01%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>427.00 (n/a)</td><td>284.28 (n/a)</td><td>238.90 (n/a)</td><td>209.60 (n/a)</td><td>88.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.05 (-18.12%)</td><td>0.03 <b>(-21.45%)</b></td><td>0.03 <b>(-37.86%)</b></td><td>0.02 <b>(+34.87%)</b></td><td>0.01 <b>(-22.36%)</b></td><td>539.30 <b>(-25.85%)</b></td><td>418.28 (+17.18%)</td><td>468.40 <b>(+60.91%)</b></td><td>267.90 <b>(+22.11%)</b></td><td>133.92 <b>(-36.04%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>727.30 (n/a)</td><td>356.94 (n/a)</td><td>291.10 (n/a)</td><td>219.40 (n/a)</td><td>209.37 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (-13.10%)</td><td>0.02 (-13.07%)</td><td>0.02 (-12.07%)</td><td>0.01 (-17.71%)</td><td>0.00 (-1.07%)</td><td>515.80 <b>(+21.51%)</b></td><td>339.24 (+17.15%)</td><td>305.10 (+13.72%)</td><td>238.60 (+15.10%)</td><td>110.36 <b>(+35.09%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>424.50 (n/a)</td><td>289.58 (n/a)</td><td>268.30 (n/a)</td><td>207.30 (n/a)</td><td>81.69 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (+11.63%)</td><td>0.02 (+0.27%)</td><td>0.02 (+8.10%)</td><td>0.01 (-13.77%)</td><td>0.01 <b>(+86.29%)</b></td><td>529.80 (+15.96%)</td><td>347.60 (+8.93%)</td><td>267.50 (-7.50%)</td><td>230.10 (-10.43%)</td><td>143.85 <b>(+82.33%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>456.90 (n/a)</td><td>319.10 (n/a)</td><td>289.20 (n/a)</td><td>256.90 (n/a)</td><td>78.90 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (-16.37%)</td><td>0.02 (-8.79%)</td><td>0.02 (-12.80%)</td><td>0.01 (-9.11%)</td><td>0.00 <b>(-25.86%)</b></td><td>652.90 (+10.01%)</td><td>372.94 (+5.96%)</td><td>300.40 (+14.66%)</td><td>268.40 (+19.55%)</td><td>161.35 (+0.89%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.50 (n/a)</td><td>351.96 (n/a)</td><td>262.00 (n/a)</td><td>224.50 (n/a)</td><td>159.92 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (+12.43%)</td><td>0.01 (+9.53%)</td><td>0.01 (+14.20%)</td><td>0.01 (-5.18%)</td><td>0.01 <b>(+29.89%)</b></td><td>523.60 (+5.46%)</td><td>393.92 (-5.26%)</td><td>384.10 (-12.45%)</td><td>224.70 (-11.05%)</td><td>124.72 <b>(+31.50%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.50 (n/a)</td><td>415.80 (n/a)</td><td>438.70 (n/a)</td><td>252.60 (n/a)</td><td>94.84 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (+2.96%)</td><td>0.02 (-4.18%)</td><td>0.01 <b>(-23.94%)</b></td><td>0.01 <b>(+65.37%)</b></td><td>0.00 <b>(-25.54%)</b></td><td>474.40 <b>(-39.53%)</b></td><td>357.40 (-7.68%)</td><td>368.00 <b>(+31.48%)</b></td><td>232.20 (-2.89%)</td><td>90.15 <b>(-60.14%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>784.50 (n/a)</td><td>387.12 (n/a)</td><td>279.90 (n/a)</td><td>239.10 (n/a)</td><td>226.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (+15.78%)</td><td>0.01 <b>(+35.92%)</b></td><td>0.01 (+19.60%)</td><td>0.01 <b>(+197.74%)</b></td><td>0.01 (-2.50%)</td><td>627.20 <b>(-66.41%)</b></td><td>423.56 <b>(-44.14%)</b></td><td>482.50 (-16.39%)</td><td>212.20 (-13.60%)</td><td>163.53 <b>(-74.35%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1867.30 (n/a)</td><td>758.30 (n/a)</td><td>577.10 (n/a)</td><td>245.60 (n/a)</td><td>637.63 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>586.40 (n/a)</td><td>371.18 (n/a)</td><td>316.20 (n/a)</td><td>237.50 (n/a)</td><td>143.97 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>655.40 (n/a)</td><td>392.96 (n/a)</td><td>276.00 (n/a)</td><td>203.90 (n/a)</td><td>200.61 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1851.40 (n/a)</td><td>739.42 (n/a)</td><td>542.30 (n/a)</td><td>247.00 (n/a)</td><td>636.15 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.70 (n/a)</td><td>382.14 (n/a)</td><td>367.40 (n/a)</td><td>275.60 (n/a)</td><td>99.40 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>586.20 (n/a)</td><td>380.00 (n/a)</td><td>296.40 (n/a)</td><td>234.20 (n/a)</td><td>153.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>575.60 (n/a)</td><td>470.48 (n/a)</td><td>509.50 (n/a)</td><td>253.10 (n/a)</td><td>125.11 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.49 <b>(+92.27%)</b></td><td>1.03 <b>(+110.68%)</b></td><td>0.94 <b>(+111.63%)</b></td><td>0.81 <b>(+344.66%)</b></td><td>0.26 (+18.43%)</td><td>563.30 <b>(-77.51%)</b></td><td>462.94 <b>(-60.98%)</b></td><td>490.00 <b>(-52.75%)</b></td><td>308.40 <b>(-47.99%)</b></td><td>94.25 <b>(-87.64%)</b></td><td>108.79 <b>(+92.27%)</b></td><td>75.57 <b>(+110.68%)</b></td><td>68.48 <b>(+111.63%)</b></td><td>59.56 <b>(+344.66%)</b></td><td>19.18 (+18.43%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.77 (n/a)</td><td>0.49 (n/a)</td><td>0.44 (n/a)</td><td>0.18 (n/a)</td><td>0.22 (n/a)</td><td>2504.90 (n/a)</td><td>1186.42 (n/a)</td><td>1037.00 (n/a)</td><td>593.00 (n/a)</td><td>762.75 (n/a)</td><td>56.58 (n/a)</td><td>35.87 (n/a)</td><td>32.36 (n/a)</td><td>13.40 (n/a)</td><td>16.20 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.53 <b>(+28.13%)</b></td><td>1.00 (-6.85%)</td><td>1.06 (-7.93%)</td><td>0.32 <b>(-64.70%)</b></td><td>0.45 <b>(+229.96%)</b></td><td>2049.70 <b>(+183.26%)</b></td><td>877.20 <b>(+41.37%)</b></td><td>620.80 (+8.61%)</td><td>428.90 <b>(-21.95%)</b></td><td>664.91 <b>(+710.35%)</b></td><td>156.48 <b>(+28.13%)</b></td><td>102.10 (-6.85%)</td><td>108.10 (-7.93%)</td><td>32.74 <b>(-64.70%)</b></td><td>45.62 <b>(+229.96%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.19 (n/a)</td><td>1.07 (n/a)</td><td>1.15 (n/a)</td><td>0.91 (n/a)</td><td>0.14 (n/a)</td><td>723.60 (n/a)</td><td>620.52 (n/a)</td><td>571.60 (n/a)</td><td>549.50 (n/a)</td><td>82.05 (n/a)</td><td>122.12 (n/a)</td><td>109.61 (n/a)</td><td>117.41 (n/a)</td><td>92.74 (n/a)</td><td>13.83 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.60 (+14.57%)</td><td>1.34 (+17.57%)</td><td>1.42 (+13.76%)</td><td>0.96 <b>(+26.82%)</b></td><td>0.28 (+13.27%)</td><td>785.70 <b>(-21.15%)</b></td><td>585.90 (-15.52%)</td><td>531.70 (-12.09%)</td><td>470.20 (-12.72%)</td><td>136.33 <b>(-25.36%)</b></td><td>178.40 (+14.57%)</td><td>149.00 (+17.57%)</td><td>157.78 (+13.76%)</td><td>106.77 <b>(+26.82%)</b></td><td>31.50 (+13.27%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.40 (n/a)</td><td>1.14 (n/a)</td><td>1.25 (n/a)</td><td>0.76 (n/a)</td><td>0.25 (n/a)</td><td>996.40 (n/a)</td><td>693.54 (n/a)</td><td>604.80 (n/a)</td><td>538.70 (n/a)</td><td>182.65 (n/a)</td><td>155.71 (n/a)</td><td>126.73 (n/a)</td><td>138.69 (n/a)</td><td>84.19 (n/a)</td><td>27.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.75 (+7.39%)</td><td>1.09 (-14.37%)</td><td>1.22 (-9.80%)</td><td>0.32 <b>(-53.77%)</b></td><td>0.53 <b>(+44.11%)</b></td><td>3312.70 <b>(+116.32%)</b></td><td>1356.38 <b>(+49.45%)</b></td><td>857.50 (+10.87%)</td><td>599.10 (-6.89%)</td><td>1112.60 <b>(+208.64%)</b></td><td>224.04 (+7.39%)</td><td>139.11 (-14.37%)</td><td>156.53 (-9.80%)</td><td>40.52 <b>(-53.77%)</b></td><td>67.64 <b>(+44.11%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.63 (n/a)</td><td>1.27 (n/a)</td><td>1.36 (n/a)</td><td>0.68 (n/a)</td><td>0.37 (n/a)</td><td>1531.40 (n/a)</td><td>907.56 (n/a)</td><td>773.40 (n/a)</td><td>643.40 (n/a)</td><td>360.48 (n/a)</td><td>208.62 (n/a)</td><td>162.45 (n/a)</td><td>173.54 (n/a)</td><td>87.64 (n/a)</td><td>46.94 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.90 <b>(-35.78%)</b></td><td>1.46 (-6.65%)</td><td>1.42 (-9.58%)</td><td>0.97 <b>(+200.05%)</b></td><td>0.43 <b>(-57.10%)</b></td><td>1076.00 <b>(-66.67%)</b></td><td>775.50 <b>(-34.19%)</b></td><td>739.70 (+10.60%)</td><td>552.80 <b>(+55.72%)</b></td><td>236.00 <b>(-80.01%)</b></td><td>242.80 <b>(-35.78%)</b></td><td>186.39 (-6.65%)</td><td>181.45 (-9.58%)</td><td>124.74 <b>(+200.05%)</b></td><td>55.36 <b>(-57.10%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>2.95 (n/a)</td><td>1.56 (n/a)</td><td>1.57 (n/a)</td><td>0.32 (n/a)</td><td>1.01 (n/a)</td><td>3228.40 (n/a)</td><td>1178.42 (n/a)</td><td>668.80 (n/a)</td><td>355.00 (n/a)</td><td>1180.82 (n/a)</td><td>378.05 (n/a)</td><td>199.67 (n/a)</td><td>200.68 (n/a)</td><td>41.57 (n/a)</td><td>129.05 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>2.90 (+15.07%)</td><td>1.62 (-3.17%)</td><td>1.45 (-9.26%)</td><td>0.30 <b>(-53.71%)</b></td><td>1.01 <b>(+37.41%)</b></td><td>3481.90 <b>(+116.03%)</b></td><td>1187.30 <b>(+51.34%)</b></td><td>724.00 (+10.21%)</td><td>361.40 (-13.10%)</td><td>1301.00 <b>(+169.18%)</b></td><td>371.33 (+15.07%)</td><td>207.17 (-3.17%)</td><td>185.40 (-9.26%)</td><td>38.55 <b>(-53.71%)</b></td><td>129.30 <b>(+37.41%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>2.52 (n/a)</td><td>1.67 (n/a)</td><td>1.60 (n/a)</td><td>0.65 (n/a)</td><td>0.74 (n/a)</td><td>1611.80 (n/a)</td><td>784.52 (n/a)</td><td>656.90 (n/a)</td><td>415.90 (n/a)</td><td>483.32 (n/a)</td><td>322.69 (n/a)</td><td>213.94 (n/a)</td><td>204.31 (n/a)</td><td>83.27 (n/a)</td><td>94.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.84 (-8.18%)</td><td>1.28 (+16.62%)</td><td>1.23 <b>(+49.05%)</b></td><td>0.51 (+7.22%)</td><td>0.56 (-8.57%)</td><td>2037.40 (-6.73%)</td><td>1020.10 (-16.91%)</td><td>852.30 <b>(-32.91%)</b></td><td>570.40 (+8.90%)</td><td>604.44 (-7.18%)</td><td>235.30 (-8.18%)</td><td>163.37 (+16.62%)</td><td>157.47 <b>(+49.05%)</b></td><td>65.88 (+7.22%)</td><td>72.02 (-8.57%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>2.00 (n/a)</td><td>1.09 (n/a)</td><td>0.83 (n/a)</td><td>0.48 (n/a)</td><td>0.62 (n/a)</td><td>2184.40 (n/a)</td><td>1227.64 (n/a)</td><td>1270.40 (n/a)</td><td>523.80 (n/a)</td><td>651.21 (n/a)</td><td>256.25 (n/a)</td><td>140.10 (n/a)</td><td>105.65 (n/a)</td><td>61.44 (n/a)</td><td>78.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.96 (-13.68%)</td><td>0.71 (+19.72%)</td><td>0.65 <b>(+56.52%)</b></td><td>0.52 <b>(+54.34%)</b></td><td>0.17 <b>(-48.41%)</b></td><td>697.70 <b>(-35.21%)</b></td><td>533.28 <b>(-29.53%)</b></td><td>553.50 <b>(-36.11%)</b></td><td>374.00 (+15.83%)</td><td>123.80 <b>(-63.02%)</b></td><td>44.86 (-13.68%)</td><td>32.93 (+19.72%)</td><td>30.31 <b>(+56.52%)</b></td><td>24.05 <b>(+54.34%)</b></td><td>8.07 <b>(-48.41%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.12 (n/a)</td><td>0.59 (n/a)</td><td>0.42 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>1076.80 (n/a)</td><td>756.78 (n/a)</td><td>866.40 (n/a)</td><td>322.90 (n/a)</td><td>334.81 (n/a)</td><td>51.96 (n/a)</td><td>27.51 (n/a)</td><td>19.37 (n/a)</td><td>15.58 (n/a)</td><td>15.64 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>3.91 (-5.55%)</td><td>3.18 <b>(+27.23%)</b></td><td>3.24 <b>(+47.24%)</b></td><td>2.49 <b>(+111.05%)</b></td><td>0.64 <b>(-42.20%)</b></td><td>1051.80 <b>(-52.62%)</b></td><td>851.64 <b>(-31.41%)</b></td><td>809.00 <b>(-32.09%)</b></td><td>669.80 (+5.86%)</td><td>174.21 <b>(-71.01%)</b></td><td>801.49 (-5.55%)</td><td>651.64 <b>(+27.23%)</b></td><td>663.60 <b>(+47.24%)</b></td><td>510.43 <b>(+111.05%)</b></td><td>130.56 <b>(-42.20%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>4.14 (n/a)</td><td>2.50 (n/a)</td><td>2.20 (n/a)</td><td>1.18 (n/a)</td><td>1.10 (n/a)</td><td>2219.90 (n/a)</td><td>1241.60 (n/a)</td><td>1191.20 (n/a)</td><td>632.70 (n/a)</td><td>600.96 (n/a)</td><td>848.57 (n/a)</td><td>512.19 (n/a)</td><td>450.69 (n/a)</td><td>241.85 (n/a)</td><td>225.88 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.00 (n/a)</td><td>334.58 (n/a)</td><td>290.10 (n/a)</td><td>216.30 (n/a)</td><td>129.07 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.70 (n/a)</td><td>401.56 (n/a)</td><td>468.40 (n/a)</td><td>245.00 (n/a)</td><td>134.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1878.70 (n/a)</td><td>666.86 (n/a)</td><td>307.00 (n/a)</td><td>256.70 (n/a)</td><td>690.88 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>693.00 (n/a)</td><td>518.40 (n/a)</td><td>588.60 (n/a)</td><td>232.10 (n/a)</td><td>179.34 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>794.50 (n/a)</td><td>547.88 (n/a)</td><td>538.30 (n/a)</td><td>270.80 (n/a)</td><td>243.67 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>675.80 (n/a)</td><td>489.78 (n/a)</td><td>484.60 (n/a)</td><td>323.50 (n/a)</td><td>125.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.60 <b>(+25.25%)</b></td><td>0.49 <b>(+79.24%)</b></td><td>0.48 <b>(+89.50%)</b></td><td>0.35 <b>(+187.20%)</b></td><td>0.09 <b>(-34.09%)</b></td><td>634.10 <b>(-65.18%)</b></td><td>466.42 <b>(-54.00%)</b></td><td>458.00 <b>(-47.22%)</b></td><td>366.80 <b>(-20.16%)</b></td><td>101.07 <b>(-81.26%)</b></td><td>25.73 <b>(+25.25%)</b></td><td>20.91 <b>(+79.24%)</b></td><td>20.61 <b>(+89.50%)</b></td><td>14.88 <b>(+187.20%)</b></td><td>3.97 <b>(-34.09%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.48 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>1821.10 (n/a)</td><td>1013.90 (n/a)</td><td>867.80 (n/a)</td><td>459.40 (n/a)</td><td>539.31 (n/a)</td><td>20.54 (n/a)</td><td>11.67 (n/a)</td><td>10.87 (n/a)</td><td>5.18 (n/a)</td><td>6.03 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.48 (+5.02%)</td><td>0.39 <b>(+29.39%)</b></td><td>0.36 (+1.59%)</td><td>0.34 <b>(+162.23%)</b></td><td>0.06 <b>(-57.75%)</b></td><td>657.00 <b>(-61.87%)</b></td><td>572.90 <b>(-38.98%)</b></td><td>609.50 (-1.57%)</td><td>465.00 (-4.79%)</td><td>86.19 <b>(-84.53%)</b></td><td>20.29 (+5.02%)</td><td>16.79 <b>(+29.39%)</b></td><td>15.48 (+1.59%)</td><td>14.36 <b>(+162.23%)</b></td><td>2.67 <b>(-57.75%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.45 (n/a)</td><td>0.30 (n/a)</td><td>0.36 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>1722.90 (n/a)</td><td>938.84 (n/a)</td><td>619.20 (n/a)</td><td>488.40 (n/a)</td><td>557.03 (n/a)</td><td>19.32 (n/a)</td><td>12.98 (n/a)</td><td>15.24 (n/a)</td><td>5.48 (n/a)</td><td>6.31 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.31 (-1.53%)</td><td>0.30 (-2.01%)</td><td>0.30 (-1.05%)</td><td>0.29 (-3.73%)</td><td>0.00 <b>(+129.41%)</b></td><td>85872.90 (+3.87%)</td><td>83521.26 (+2.06%)</td><td>82764.80 (+1.06%)</td><td>82463.60 (+1.56%)</td><td>1402.53 <b>(+142.35%)</b></td><td>208.33 (-1.53%)</td><td>205.74 (-2.01%)</td><td>207.57 (-1.05%)</td><td>200.06 (-3.73%)</td><td>3.40 <b>(+129.41%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>82669.60 (n/a)</td><td>81831.66 (n/a)</td><td>81895.60 (n/a)</td><td>81198.40 (n/a)</td><td>578.73 (n/a)</td><td>211.58 (n/a)</td><td>209.95 (n/a)</td><td>209.78 (n/a)</td><td>207.81 (n/a)</td><td>1.48 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>1.15 (-1.66%)</td><td>1.14 (-0.50%)</td><td>1.15 (-0.14%)</td><td>1.10 (-0.81%)</td><td>0.02 (-7.79%)</td><td>22794.10 (+0.81%)</td><td>22127.48 (+0.50%)</td><td>21966.10 (+0.14%)</td><td>21878.20 (+1.69%)</td><td>378.41 (-5.38%)</td><td>785.25 (-1.66%)</td><td>776.58 (-0.50%)</td><td>782.11 (-0.14%)</td><td>753.70 (-0.81%)</td><td>13.00 (-7.79%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.17 (n/a)</td><td>1.14 (n/a)</td><td>1.15 (n/a)</td><td>1.11 (n/a)</td><td>0.02 (n/a)</td><td>22610.00 (n/a)</td><td>22017.58 (n/a)</td><td>21934.50 (n/a)</td><td>21515.60 (n/a)</td><td>399.93 (n/a)</td><td>798.48 (n/a)</td><td>780.48 (n/a)</td><td>783.23 (n/a)</td><td>759.83 (n/a)</td><td>14.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>3.70 <b>(+53.60%)</b></td><td>2.92 <b>(+47.19%)</b></td><td>3.58 <b>(+82.75%)</b></td><td>1.58 (-0.47%)</td><td>1.02 <b>(+202.07%)</b></td><td>5101.20 (+0.48%)</td><td>3133.92 <b>(-24.74%)</b></td><td>2249.50 <b>(-45.28%)</b></td><td>2180.40 <b>(-34.90%)</b></td><td>1334.66 <b>(+86.70%)</b></td><td>969.50 <b>(+53.60%)</b></td><td>765.02 <b>(+47.19%)</b></td><td>939.74 <b>(+82.75%)</b></td><td>414.40 (-0.47%)</td><td>268.67 <b>(+202.07%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>2.41 (n/a)</td><td>1.98 (n/a)</td><td>1.96 (n/a)</td><td>1.59 (n/a)</td><td>0.34 (n/a)</td><td>5077.00 (n/a)</td><td>4164.40 (n/a)</td><td>4110.90 (n/a)</td><td>3349.30 (n/a)</td><td>714.87 (n/a)</td><td>631.16 (n/a)</td><td>519.76 (n/a)</td><td>514.22 (n/a)</td><td>416.37 (n/a)</td><td>88.94 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.22 (+4.63%)</td><td>0.20 (+7.80%)</td><td>0.19 (-0.41%)</td><td>0.19 (+19.91%)</td><td>0.01 <b>(-45.43%)</b></td><td>6639.80 (-16.60%)</td><td>6343.88 (-8.28%)</td><td>6603.50 (+0.41%)</td><td>5725.40 (-4.43%)</td><td>410.04 <b>(-56.85%)</b></td><td>11.72 (+4.63%)</td><td>10.62 (+7.80%)</td><td>10.16 (-0.41%)</td><td>10.11 (+19.91%)</td><td>0.72 <b>(-45.43%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>7961.70 (n/a)</td><td>6916.48 (n/a)</td><td>6576.30 (n/a)</td><td>5990.50 (n/a)</td><td>950.31 (n/a)</td><td>11.20 (n/a)</td><td>9.85 (n/a)</td><td>10.20 (n/a)</td><td>8.43 (n/a)</td><td>1.32 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>3.77 (n/a)</td><td>3.63 (n/a)</td><td>3.74 (n/a)</td><td>3.41 (n/a)</td><td>0.17 (n/a)</td><td>3.76 (n/a)</td><td>3.62 (n/a)</td><td>3.74 (n/a)</td><td>3.41 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>7.01 (-6.71%)</td><td>6.10 (+0.44%)</td><td>6.40 (+11.87%)</td><td>4.63 (-8.34%)</td><td>0.98 (+0.76%)</td><td>7.00 (-6.71%)</td><td>6.10 (+0.44%)</td><td>6.39 (+11.87%)</td><td>4.62 (-8.34%)</td><td>0.98 (+0.76%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>7.51 (n/a)</td><td>6.08 (n/a)</td><td>5.72 (n/a)</td><td>5.05 (n/a)</td><td>0.97 (n/a)</td><td>7.51 (n/a)</td><td>6.07 (n/a)</td><td>5.71 (n/a)</td><td>5.04 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>14.22 (+3.76%)</td><td>9.89 (+3.13%)</td><td>8.50 (+0.46%)</td><td>8.26 (+12.12%)</td><td>2.52 (-0.66%)</td><td>14.22 (+3.76%)</td><td>9.88 (+3.13%)</td><td>8.50 (+0.46%)</td><td>8.25 (+12.12%)</td><td>2.52 (-0.66%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>13.71 (n/a)</td><td>9.59 (n/a)</td><td>8.46 (n/a)</td><td>7.36 (n/a)</td><td>2.53 (n/a)</td><td>13.70 (n/a)</td><td>9.58 (n/a)</td><td>8.46 (n/a)</td><td>7.36 (n/a)</td><td>2.53 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>3.96 (n/a)</td><td>3.71 (n/a)</td><td>3.73 (n/a)</td><td>3.42 (n/a)</td><td>0.24 (n/a)</td><td>3.96 (n/a)</td><td>3.71 (n/a)</td><td>3.73 (n/a)</td><td>3.42 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>6.90 (-5.67%)</td><td>6.51 (+2.07%)</td><td>6.81 (+5.22%)</td><td>5.46 (+7.78%)</td><td>0.60 <b>(-35.47%)</b></td><td>6.89 (-5.67%)</td><td>6.51 (+2.07%)</td><td>6.80 (+5.22%)</td><td>5.46 (+7.78%)</td><td>0.60 <b>(-35.47%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>7.31 (n/a)</td><td>6.38 (n/a)</td><td>6.47 (n/a)</td><td>5.07 (n/a)</td><td>0.93 (n/a)</td><td>7.31 (n/a)</td><td>6.38 (n/a)</td><td>6.46 (n/a)</td><td>5.06 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>11.44 (-14.60%)</td><td>9.62 (-1.97%)</td><td>10.31 <b>(+27.69%)</b></td><td>7.40 (+7.33%)</td><td>1.74 <b>(-44.03%)</b></td><td>11.43 (-14.60%)</td><td>9.61 (-1.97%)</td><td>10.30 <b>(+27.69%)</b></td><td>7.39 (+7.33%)</td><td>1.74 <b>(-44.03%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>13.40 (n/a)</td><td>9.81 (n/a)</td><td>8.07 (n/a)</td><td>6.89 (n/a)</td><td>3.11 (n/a)</td><td>13.39 (n/a)</td><td>9.81 (n/a)</td><td>8.07 (n/a)</td><td>6.89 (n/a)</td><td>3.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>3.12 (-2.10%)</td><td>2.70 (+3.06%)</td><td>2.94 (+1.57%)</td><td>1.75 <b>(+46.02%)</b></td><td>0.55 <b>(-32.09%)</b></td><td>3.11 (-2.10%)</td><td>2.69 (+3.06%)</td><td>2.94 (+1.57%)</td><td>1.75 <b>(+46.02%)</b></td><td>0.55 <b>(-32.09%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>3.19 (n/a)</td><td>2.62 (n/a)</td><td>2.90 (n/a)</td><td>1.20 (n/a)</td><td>0.81 (n/a)</td><td>3.18 (n/a)</td><td>2.61 (n/a)</td><td>2.89 (n/a)</td><td>1.20 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.61 (+7.12%)</td><td>0.42 (-14.01%)</td><td>0.50 (-5.45%)</td><td>0.08 <b>(-78.00%)</b></td><td>0.21 <b>(+102.90%)</b></td><td>0.60 (+7.12%)</td><td>0.41 (-14.01%)</td><td>0.49 (-5.45%)</td><td>0.07 <b>(-78.00%)</b></td><td>0.20 <b>(+102.90%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.57 (n/a)</td><td>0.49 (n/a)</td><td>0.53 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>0.56 (n/a)</td><td>0.48 (n/a)</td><td>0.52 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.50 <b>(-29.06%)</b></td><td>0.33 (-13.80%)</td><td>0.37 (-2.04%)</td><td>0.08 (-0.50%)</td><td>0.15 <b>(-49.34%)</b></td><td>0.49 <b>(-29.06%)</b></td><td>0.33 (-13.80%)</td><td>0.37 (-2.04%)</td><td>0.07 (-0.50%)</td><td>0.15 <b>(-49.34%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.70 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.08 (n/a)</td><td>0.31 (n/a)</td><td>0.69 (n/a)</td><td>0.38 (n/a)</td><td>0.37 (n/a)</td><td>0.08 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>2.60 (-7.25%)</td><td>1.80 (-8.02%)</td><td>1.93 (-4.39%)</td><td>0.49 <b>(-36.96%)</b></td><td>0.83 (+8.82%)</td><td>2.56 (-7.25%)</td><td>1.77 (-8.02%)</td><td>1.90 (-4.39%)</td><td>0.48 <b>(-36.96%)</b></td><td>0.82 (+8.82%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>2.80 (n/a)</td><td>1.96 (n/a)</td><td>2.02 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>2.76 (n/a)</td><td>1.93 (n/a)</td><td>1.99 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>733.30 (n/a)</td><td>362.54 (n/a)</td><td>279.80 (n/a)</td><td>240.00 (n/a)</td><td>208.22 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.00 (n/a)</td><td>368.52 (n/a)</td><td>373.00 (n/a)</td><td>245.00 (n/a)</td><td>123.69 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.90 (n/a)</td><td>420.44 (n/a)</td><td>451.40 (n/a)</td><td>236.00 (n/a)</td><td>138.67 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>490.00 (n/a)</td><td>400.42 (n/a)</td><td>453.00 (n/a)</td><td>246.20 (n/a)</td><td>108.53 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.70 (n/a)</td><td>363.86 (n/a)</td><td>317.20 (n/a)</td><td>254.20 (n/a)</td><td>112.13 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>538.90 (n/a)</td><td>448.56 (n/a)</td><td>434.90 (n/a)</td><td>367.10 (n/a)</td><td>65.66 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (-10.62%)</td><td>0.03 (+13.99%)</td><td>0.03 <b>(+35.26%)</b></td><td>0.02 (+10.24%)</td><td>0.01 (-17.64%)</td><td>509.60 (-9.29%)</td><td>347.96 (-14.55%)</td><td>295.60 <b>(-26.08%)</b></td><td>225.70 (+11.84%)</td><td>122.52 (-8.28%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.80 (n/a)</td><td>407.20 (n/a)</td><td>399.90 (n/a)</td><td>201.80 (n/a)</td><td>133.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 <b>(-21.72%)</b></td><td>0.03 (+7.04%)</td><td>0.03 <b>(+54.90%)</b></td><td>0.02 (+3.08%)</td><td>0.01 <b>(-42.67%)</b></td><td>471.90 (-2.98%)</td><td>331.14 (-13.27%)</td><td>290.80 <b>(-35.45%)</b></td><td>247.30 <b>(+27.74%)</b></td><td>90.72 <b>(-30.38%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>486.40 (n/a)</td><td>381.80 (n/a)</td><td>450.50 (n/a)</td><td>193.60 (n/a)</td><td>130.30 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 <b>(-24.98%)</b></td><td>0.02 (-8.92%)</td><td>0.02 (+14.35%)</td><td>0.01 <b>(-53.63%)</b></td><td>0.01 (-12.98%)</td><td>1094.90 <b>(+115.66%)</b></td><td>473.40 <b>(+27.16%)</b></td><td>334.90 (-12.54%)</td><td>235.80 <b>(+33.30%)</b></td><td>356.84 <b>(+150.53%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.70 (n/a)</td><td>372.28 (n/a)</td><td>382.90 (n/a)</td><td>176.90 (n/a)</td><td>142.43 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (-3.39%)</td><td>0.02 (-19.12%)</td><td>0.02 <b>(-44.73%)</b></td><td>0.01 <b>(+236.84%)</b></td><td>0.01 <b>(-36.36%)</b></td><td>571.70 <b>(-70.31%)</b></td><td>466.98 <b>(-25.76%)</b></td><td>526.10 <b>(+80.91%)</b></td><td>239.70 (+3.50%)</td><td>137.14 <b>(-81.24%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1925.80 (n/a)</td><td>629.04 (n/a)</td><td>290.80 (n/a)</td><td>231.60 (n/a)</td><td>730.98 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (-1.28%)</td><td>0.02 (-12.39%)</td><td>0.02 <b>(-23.51%)</b></td><td>0.01 (+7.32%)</td><td>0.01 (+1.68%)</td><td>605.60 (-6.82%)</td><td>479.16 (+13.56%)</td><td>490.90 <b>(+30.73%)</b></td><td>269.70 (+1.31%)</td><td>130.37 (-9.94%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>649.90 (n/a)</td><td>421.96 (n/a)</td><td>375.50 (n/a)</td><td>266.20 (n/a)</td><td>144.77 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 <b>(-47.39%)</b></td><td>0.01 <b>(-38.29%)</b></td><td>0.02 (-15.37%)</td><td>0.00 <b>(-75.45%)</b></td><td>0.01 <b>(-29.32%)</b></td><td>1933.30 <b>(+307.27%)</b></td><td>782.30 <b>(+104.37%)</b></td><td>503.10 (+18.15%)</td><td>410.80 <b>(+90.10%)</b></td><td>645.94 <b>(+542.79%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>474.70 (n/a)</td><td>382.78 (n/a)</td><td>425.80 (n/a)</td><td>216.10 (n/a)</td><td>100.49 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (-3.28%)</td><td>0.02 <b>(-24.29%)</b></td><td>0.02 <b>(-22.37%)</b></td><td>0.01 (-19.15%)</td><td>0.01 (+5.85%)</td><td>751.90 <b>(+23.69%)</b></td><td>548.28 <b>(+37.95%)</b></td><td>538.20 <b>(+28.85%)</b></td><td>250.00 (+3.39%)</td><td>199.90 <b>(+36.77%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.90 (n/a)</td><td>397.44 (n/a)</td><td>417.70 (n/a)</td><td>241.80 (n/a)</td><td>146.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 <b>(+37.52%)</b></td><td>0.02 (+6.97%)</td><td>0.02 (-7.09%)</td><td>0.02 (+10.74%)</td><td>0.01 <b>(+107.49%)</b></td><td>540.60 (-9.70%)</td><td>465.16 (-1.37%)</td><td>505.50 (+7.64%)</td><td>252.70 <b>(-27.28%)</b></td><td>120.93 <b>(+34.76%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.70 (n/a)</td><td>471.62 (n/a)</td><td>469.60 (n/a)</td><td>347.50 (n/a)</td><td>89.74 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (-3.18%)</td><td>0.03 (+6.51%)</td><td>0.03 <b>(+21.96%)</b></td><td>0.02 (+6.37%)</td><td>0.01 (-8.85%)</td><td>507.50 (-5.98%)</td><td>291.54 (-7.52%)</td><td>244.80 (-17.99%)</td><td>206.30 (+3.25%)</td><td>122.63 (-8.08%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.80 (n/a)</td><td>315.26 (n/a)</td><td>298.50 (n/a)</td><td>199.80 (n/a)</td><td>133.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (-8.20%)</td><td>0.02 (+1.58%)</td><td>0.03 <b>(+39.11%)</b></td><td>0.01 (+2.76%)</td><td>0.01 (-16.83%)</td><td>562.40 (-2.68%)</td><td>371.88 (-3.97%)</td><td>300.40 <b>(-28.12%)</b></td><td>244.20 (+8.92%)</td><td>132.50 (-7.05%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.90 (n/a)</td><td>387.26 (n/a)</td><td>417.90 (n/a)</td><td>224.20 (n/a)</td><td>142.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (-16.23%)</td><td>0.02 <b>(-22.60%)</b></td><td>0.03 (-5.01%)</td><td>0.01 <b>(-47.39%)</b></td><td>0.01 <b>(+129.35%)</b></td><td>578.20 <b>(+90.07%)</b></td><td>393.40 <b>(+44.98%)</b></td><td>285.10 (+5.28%)</td><td>267.60 (+19.36%)</td><td>162.29 <b>(+433.07%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>304.20 (n/a)</td><td>271.34 (n/a)</td><td>270.80 (n/a)</td><td>224.20 (n/a)</td><td>30.44 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (-9.04%)</td><td>0.03 (+11.24%)</td><td>0.03 <b>(+63.20%)</b></td><td>0.02 (+3.69%)</td><td>0.01 <b>(-31.81%)</b></td><td>517.70 (-3.56%)</td><td>346.58 (-16.03%)</td><td>302.70 <b>(-38.72%)</b></td><td>252.00 (+9.90%)</td><td>107.48 <b>(-29.26%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.80 (n/a)</td><td>412.74 (n/a)</td><td>494.00 (n/a)</td><td>229.30 (n/a)</td><td>151.93 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (-8.74%)</td><td>0.02 (-0.30%)</td><td>0.03 <b>(+24.23%)</b></td><td>0.01 (-16.32%)</td><td>0.01 (+10.41%)</td><td>608.70 (+19.52%)</td><td>389.36 (+4.25%)</td><td>302.30 (-19.49%)</td><td>266.40 (+9.58%)</td><td>150.02 <b>(+44.22%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>509.30 (n/a)</td><td>373.48 (n/a)</td><td>375.50 (n/a)</td><td>243.10 (n/a)</td><td>104.02 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (-14.68%)</td><td>0.02 (+8.70%)</td><td>0.02 <b>(+36.67%)</b></td><td>0.01 (+14.88%)</td><td>0.01 <b>(-36.57%)</b></td><td>603.20 (-12.96%)</td><td>384.00 (-15.31%)</td><td>343.60 <b>(-26.82%)</b></td><td>265.90 (+17.19%)</td><td>128.77 <b>(-30.28%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>693.00 (n/a)</td><td>453.40 (n/a)</td><td>469.50 (n/a)</td><td>226.90 (n/a)</td><td>184.69 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.08 (-17.96%)</td><td>0.06 <b>(-20.12%)</b></td><td>0.07 <b>(-26.93%)</b></td><td>0.05 (-7.27%)</td><td>0.02 <b>(-25.85%)</b></td><td>543.70 (+7.83%)</td><td>408.10 <b>(+22.89%)</b></td><td>345.50 <b>(+36.83%)</b></td><td>300.80 <b>(+21.88%)</b></td><td>123.98 (+5.25%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>504.20 (n/a)</td><td>332.08 (n/a)</td><td>252.50 (n/a)</td><td>246.80 (n/a)</td><td>117.80 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.17 (+7.57%)</td><td>0.12 (+1.46%)</td><td>0.10 (+1.06%)</td><td>0.09 (-7.12%)</td><td>0.04 <b>(+30.88%)</b></td><td>473.00 (+7.67%)</td><td>366.22 (+1.55%)</td><td>390.50 (-1.06%)</td><td>239.00 (-7.04%)</td><td>104.49 <b>(+31.79%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>439.30 (n/a)</td><td>360.62 (n/a)</td><td>394.70 (n/a)</td><td>257.10 (n/a)</td><td>79.28 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 <b>(-33.99%)</b></td><td>0.02 <b>(-24.57%)</b></td><td>0.02 (-4.12%)</td><td>0.01 <b>(-37.86%)</b></td><td>0.00 (-16.03%)</td><td>475.70 <b>(+60.93%)</b></td><td>360.18 <b>(+35.77%)</b></td><td>294.50 (+4.32%)</td><td>279.40 <b>(+51.52%)</b></td><td>97.67 <b>(+111.54%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>295.60 (n/a)</td><td>265.28 (n/a)</td><td>282.30 (n/a)</td><td>184.40 (n/a)</td><td>46.17 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (-0.31%)</td><td>0.03 (+1.10%)</td><td>0.03 (+2.08%)</td><td>0.01 (-11.26%)</td><td>0.01 (-1.17%)</td><td>579.00 (+12.69%)</td><td>348.64 (-0.77%)</td><td>258.60 (-2.05%)</td><td>239.90 (+0.33%)</td><td>149.82 (+5.58%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.80 (n/a)</td><td>351.34 (n/a)</td><td>264.00 (n/a)</td><td>239.10 (n/a)</td><td>141.90 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.06 <b>(+29.43%)</b></td><td>0.05 <b>(+38.88%)</b></td><td>0.05 <b>(+55.12%)</b></td><td>0.04 <b>(+60.89%)</b></td><td>0.01 (-4.78%)</td><td>299.20 <b>(-37.85%)</b></td><td>254.08 <b>(-30.06%)</b></td><td>251.10 <b>(-35.55%)</b></td><td>192.80 <b>(-22.76%)</b></td><td>42.00 <b>(-53.52%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>481.40 (n/a)</td><td>363.26 (n/a)</td><td>389.60 (n/a)</td><td>249.60 (n/a)</td><td>90.36 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (+0.26%)</td><td>0.03 (-3.95%)</td><td>0.03 (-6.68%)</td><td>0.02 <b>(+24.97%)</b></td><td>0.01 (-19.10%)</td><td>504.90 (-19.98%)</td><td>325.84 (-2.90%)</td><td>296.70 (+7.19%)</td><td>210.60 (-0.28%)</td><td>109.72 <b>(-35.91%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>631.00 (n/a)</td><td>335.58 (n/a)</td><td>276.80 (n/a)</td><td>211.20 (n/a)</td><td>171.21 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (-4.98%)</td><td>0.02 (-14.89%)</td><td>0.02 (-12.13%)</td><td>0.01 <b>(+22.65%)</b></td><td>0.01 (-10.75%)</td><td>819.30 (-18.47%)</td><td>552.80 (+10.64%)</td><td>513.20 (+13.82%)</td><td>267.00 (+5.24%)</td><td>228.32 <b>(-23.49%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1004.90 (n/a)</td><td>499.62 (n/a)</td><td>450.90 (n/a)</td><td>253.70 (n/a)</td><td>298.41 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (+19.69%)</td><td>0.03 (-1.78%)</td><td>0.03 (-10.48%)</td><td>0.01 <b>(-40.39%)</b></td><td>0.01 <b>(+162.65%)</b></td><td>587.60 <b>(+67.74%)</b></td><td>326.22 (+15.54%)</td><td>300.50 (+11.71%)</td><td>199.70 (-16.44%)</td><td>155.28 <b>(+265.98%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>350.30 (n/a)</td><td>282.34 (n/a)</td><td>269.00 (n/a)</td><td>239.00 (n/a)</td><td>42.43 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (+10.71%)</td><td>0.03 <b>(+26.81%)</b></td><td>0.02 (+6.55%)</td><td>0.02 <b>(+68.59%)</b></td><td>0.01 (+0.63%)</td><td>616.50 <b>(-40.69%)</b></td><td>467.82 <b>(-26.76%)</b></td><td>541.40 (-6.15%)</td><td>227.60 (-9.68%)</td><td>171.09 <b>(-40.98%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1039.40 (n/a)</td><td>638.72 (n/a)</td><td>576.90 (n/a)</td><td>252.00 (n/a)</td><td>289.89 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (-19.92%)</td><td>0.02 (-16.85%)</td><td>0.02 (-16.05%)</td><td>0.01 (-1.64%)</td><td>0.01 <b>(-39.53%)</b></td><td>557.50 (+1.66%)</td><td>418.68 (+12.41%)</td><td>352.20 (+19.15%)</td><td>297.60 <b>(+24.88%)</b></td><td>122.06 <b>(-21.52%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.40 (n/a)</td><td>372.46 (n/a)</td><td>295.60 (n/a)</td><td>238.30 (n/a)</td><td>155.54 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (-9.91%)</td><td>0.02 (-1.79%)</td><td>0.02 (+4.61%)</td><td>0.01 (+3.63%)</td><td>0.01 <b>(-20.81%)</b></td><td>720.80 (-3.51%)</td><td>440.86 (-1.22%)</td><td>405.00 (-4.39%)</td><td>328.30 (+10.99%)</td><td>161.17 (-11.56%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>747.00 (n/a)</td><td>446.30 (n/a)</td><td>423.60 (n/a)</td><td>295.80 (n/a)</td><td>182.23 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.04 (-11.35%)</td><td>0.02 (-13.66%)</td><td>0.02 <b>(-27.35%)</b></td><td>0.01 <b>(-42.72%)</b></td><td>0.01 (+10.31%)</td><td>1125.40 <b>(+74.56%)</b></td><td>542.42 <b>(+36.61%)</b></td><td>472.50 <b>(+37.63%)</b></td><td>225.00 (+12.78%)</td><td>370.87 <b>(+93.93%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>644.70 (n/a)</td><td>397.06 (n/a)</td><td>343.30 (n/a)</td><td>199.50 (n/a)</td><td>191.24 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 (+0.73%)</td><td>0.03 (+10.73%)</td><td>0.03 <b>(+52.47%)</b></td><td>0.02 (+6.34%)</td><td>0.01 (-8.23%)</td><td>521.40 (-5.95%)</td><td>373.44 (-10.87%)</td><td>312.30 <b>(-34.42%)</b></td><td>283.90 (-0.73%)</td><td>108.78 (-10.77%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>554.40 (n/a)</td><td>418.98 (n/a)</td><td>476.20 (n/a)</td><td>286.00 (n/a)</td><td>121.91 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.03 <b>(+22.96%)</b></td><td>0.02 (-2.31%)</td><td>0.01 (-17.73%)</td><td>0.01 (-15.04%)</td><td>0.01 <b>(+72.52%)</b></td><td>749.00 (+17.69%)</td><td>554.72 (+9.88%)</td><td>603.00 <b>(+21.55%)</b></td><td>276.10 (-18.67%)</td><td>174.18 <b>(+56.20%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>636.40 (n/a)</td><td>504.86 (n/a)</td><td>496.10 (n/a)</td><td>339.50 (n/a)</td><td>111.52 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.41 (+15.19%)</td><td>0.27 (-4.08%)</td><td>0.25 (-17.72%)</td><td>0.16 (-4.93%)</td><td>0.10 <b>(+49.04%)</b></td><td>615.40 (+5.20%)</td><td>403.92 (+9.93%)</td><td>395.30 <b>(+21.56%)</b></td><td>241.30 (-13.17%)</td><td>154.66 <b>(+24.95%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>585.00 (n/a)</td><td>367.44 (n/a)</td><td>325.20 (n/a)</td><td>277.90 (n/a)</td><td>123.78 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.28 <b>(-29.50%)</b></td><td>0.19 <b>(-30.43%)</b></td><td>0.17 <b>(-22.79%)</b></td><td>0.16 (-6.08%)</td><td>0.05 <b>(-55.48%)</b></td><td>612.10 (+6.47%)</td><td>528.68 <b>(+32.15%)</b></td><td>563.00 <b>(+29.51%)</b></td><td>349.30 <b>(+41.82%)</b></td><td>103.23 <b>(-30.50%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.40 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>574.90 (n/a)</td><td>400.06 (n/a)</td><td>434.70 (n/a)</td><td>246.30 (n/a)</td><td>148.55 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.38 (+13.95%)</td><td>0.32 <b>(+61.78%)</b></td><td>0.31 <b>(+92.16%)</b></td><td>0.22 <b>(+72.20%)</b></td><td>0.06 <b>(-23.18%)</b></td><td>446.00 <b>(-41.93%)</b></td><td>322.38 <b>(-42.60%)</b></td><td>318.40 <b>(-47.96%)</b></td><td>255.90 (-12.24%)</td><td>75.11 <b>(-58.51%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.34 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>768.00 (n/a)</td><td>561.64 (n/a)</td><td>611.80 (n/a)</td><td>291.60 (n/a)</td><td>181.02 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.24 (-19.22%)</td><td>0.17 <b>(-25.38%)</b></td><td>0.16 <b>(-31.90%)</b></td><td>0.14 (+16.86%)</td><td>0.04 <b>(-37.33%)</b></td><td>545.40 (-14.42%)</td><td>455.22 <b>(+25.75%)</b></td><td>454.20 <b>(+46.85%)</b></td><td>308.20 <b>(+23.78%)</b></td><td>93.11 <b>(-40.32%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>637.30 (n/a)</td><td>362.00 (n/a)</td><td>309.30 (n/a)</td><td>249.00 (n/a)</td><td>156.01 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.26 (-15.94%)</td><td>0.21 <b>(-30.39%)</b></td><td>0.24 <b>(-20.08%)</b></td><td>0.12 <b>(-52.10%)</b></td><td>0.07 <b>(+199.06%)</b></td><td>597.40 <b>(+108.74%)</b></td><td>394.52 <b>(+57.93%)</b></td><td>301.90 <b>(+25.11%)</b></td><td>282.40 (+18.96%)</td><td>146.75 <b>(+612.90%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.02 (n/a)</td><td>286.20 (n/a)</td><td>249.80 (n/a)</td><td>241.30 (n/a)</td><td>237.40 (n/a)</td><td>20.58 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.18 <b>(-35.61%)</b></td><td>0.15 (-4.20%)</td><td>0.15 (+3.32%)</td><td>0.12 (+14.40%)</td><td>0.03 <b>(-62.71%)</b></td><td>631.50 (-12.58%)</td><td>494.90 (-5.07%)</td><td>501.50 (-3.22%)</td><td>399.40 <b>(+55.29%)</b></td><td>92.05 <b>(-45.89%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.29 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>722.40 (n/a)</td><td>521.32 (n/a)</td><td>518.20 (n/a)</td><td>257.20 (n/a)</td><td>170.12 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.47 <b>(+72.77%)</b></td><td>0.40 <b>(+62.95%)</b></td><td>0.42 <b>(+71.30%)</b></td><td>0.27 <b>(+29.89%)</b></td><td>0.07 <b>(+229.30%)</b></td><td>476.80 <b>(-23.01%)</b></td><td>338.10 <b>(-36.89%)</b></td><td>311.60 <b>(-41.63%)</b></td><td>277.10 <b>(-42.11%)</b></td><td>79.04 <b>(+52.30%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>619.30 (n/a)</td><td>535.76 (n/a)</td><td>533.80 (n/a)</td><td>478.70 (n/a)</td><td>51.90 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.51 <b>(+20.49%)</b></td><td>0.36 (+16.79%)</td><td>0.39 <b>(+41.22%)</b></td><td>0.19 (-9.45%)</td><td>0.14 <b>(+46.69%)</b></td><td>675.40 (+10.43%)</td><td>418.70 (-8.41%)</td><td>337.80 <b>(-29.20%)</b></td><td>257.80 (-17.00%)</td><td>182.49 <b>(+37.20%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>611.60 (n/a)</td><td>457.14 (n/a)</td><td>477.10 (n/a)</td><td>310.60 (n/a)</td><td>133.00 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.51 <b>(+26.80%)</b></td><td>0.37 <b>(+38.82%)</b></td><td>0.42 <b>(+76.58%)</b></td><td>0.13 <b>(-33.17%)</b></td><td>0.14 <b>(+84.60%)</b></td><td>976.60 <b>(+49.65%)</b></td><td>438.72 (-14.36%)</td><td>310.30 <b>(-43.37%)</b></td><td>259.50 <b>(-21.15%)</b></td><td>302.01 <b>(+151.47%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.40 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>652.60 (n/a)</td><td>512.28 (n/a)</td><td>547.90 (n/a)</td><td>329.10 (n/a)</td><td>120.10 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (-13.58%)</td><td>0.02 <b>(+29.05%)</b></td><td>0.02 <b>(+32.77%)</b></td><td>0.01 <b>(+94.60%)</b></td><td>0.00 <b>(-66.66%)</b></td><td>300.90 <b>(-48.61%)</b></td><td>251.08 <b>(-30.88%)</b></td><td>236.40 <b>(-24.67%)</b></td><td>232.50 (+15.67%)</td><td>28.64 <b>(-80.18%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>585.50 (n/a)</td><td>363.24 (n/a)</td><td>313.80 (n/a)</td><td>201.00 (n/a)</td><td>144.46 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (+11.99%)</td><td>0.01 (+17.57%)</td><td>0.01 (-5.37%)</td><td>0.00 (+3.09%)</td><td>0.01 (-11.87%)</td><td>1932.40 (-3.00%)</td><td>669.42 <b>(-30.64%)</b></td><td>354.10 (+5.67%)</td><td>259.50 (-10.70%)</td><td>712.07 <b>(-20.40%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1992.10 (n/a)</td><td>965.14 (n/a)</td><td>335.10 (n/a)</td><td>290.60 (n/a)</td><td>894.58 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.01 (-10.04%)</td><td>0.01 (-12.78%)</td><td>0.01 <b>(-24.85%)</b></td><td>0.01 (+13.34%)</td><td>0.00 <b>(-39.72%)</b></td><td>451.10 (-11.76%)</td><td>400.92 (+9.87%)</td><td>423.80 <b>(+33.06%)</b></td><td>295.90 (+11.16%)</td><td>63.95 <b>(-41.22%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.20 (n/a)</td><td>364.90 (n/a)</td><td>318.50 (n/a)</td><td>266.20 (n/a)</td><td>108.79 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.60 <b>(-21.43%)</b></td><td>0.37 (-15.28%)</td><td>0.35 (+0.99%)</td><td>0.22 <b>(-31.95%)</b></td><td>0.14 <b>(-23.81%)</b></td><td>602.90 <b>(+46.94%)</b></td><td>399.06 (+18.53%)</td><td>377.50 (-1.00%)</td><td>220.70 <b>(+27.28%)</b></td><td>138.94 <b>(+43.95%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.76 (n/a)</td><td>0.43 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.19 (n/a)</td><td>410.30 (n/a)</td><td>336.68 (n/a)</td><td>381.30 (n/a)</td><td>173.40 (n/a)</td><td>96.52 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.56 <b>(+84.29%)</b></td><td>0.41 <b>(+55.73%)</b></td><td>0.45 <b>(+60.56%)</b></td><td>0.23 (+10.36%)</td><td>0.16 <b>(+321.42%)</b></td><td>576.10 (-9.39%)</td><td>376.66 <b>(-26.82%)</b></td><td>296.20 <b>(-37.73%)</b></td><td>236.70 <b>(-45.72%)</b></td><td>166.47 <b>(+105.53%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>635.80 (n/a)</td><td>514.72 (n/a)</td><td>475.70 (n/a)</td><td>436.10 (n/a)</td><td>81.00 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.59 (+8.48%)</td><td>0.35 (-15.14%)</td><td>0.31 <b>(-30.54%)</b></td><td>0.20 <b>(-23.26%)</b></td><td>0.15 (+16.56%)</td><td>645.10 <b>(+30.32%)</b></td><td>434.92 <b>(+22.90%)</b></td><td>431.70 <b>(+44.00%)</b></td><td>225.40 (-7.81%)</td><td>162.57 <b>(+34.50%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.54 (n/a)</td><td>0.41 (n/a)</td><td>0.44 (n/a)</td><td>0.27 (n/a)</td><td>0.13 (n/a)</td><td>495.00 (n/a)</td><td>353.88 (n/a)</td><td>299.80 (n/a)</td><td>244.50 (n/a)</td><td>120.88 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.44 (-1.65%)</td><td>0.37 (+7.43%)</td><td>0.36 (+15.07%)</td><td>0.29 (+14.73%)</td><td>0.06 <b>(-32.40%)</b></td><td>455.90 (-12.83%)</td><td>362.46 (-9.56%)</td><td>364.20 (-13.10%)</td><td>299.10 (+1.67%)</td><td>60.89 <b>(-37.95%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.45 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>523.00 (n/a)</td><td>400.76 (n/a)</td><td>419.10 (n/a)</td><td>294.20 (n/a)</td><td>98.12 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.54 (+0.50%)</td><td>0.46 <b>(+28.35%)</b></td><td>0.47 <b>(+32.37%)</b></td><td>0.39 <b>(+505.56%)</b></td><td>0.06 <b>(-65.36%)</b></td><td>340.00 <b>(-83.48%)</b></td><td>293.38 <b>(-56.15%)</b></td><td>279.10 <b>(-24.45%)</b></td><td>243.60 (-0.49%)</td><td>41.47 <b>(-94.68%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.54 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.06 (n/a)</td><td>0.19 (n/a)</td><td>2058.70 (n/a)</td><td>669.04 (n/a)</td><td>369.40 (n/a)</td><td>244.80 (n/a)</td><td>779.78 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (+15.76%)</td><td>0.01 <b>(+48.00%)</b></td><td>0.01 <b>(+89.79%)</b></td><td>0.01 <b>(+29.26%)</b></td><td>0.00 <b>(+27.47%)</b></td><td>608.30 <b>(-22.64%)</b></td><td>364.28 <b>(-31.63%)</b></td><td>276.70 <b>(-47.31%)</b></td><td>246.30 (-13.64%)</td><td>158.34 (-15.94%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>786.30 (n/a)</td><td>532.84 (n/a)</td><td>525.10 (n/a)</td><td>285.20 (n/a)</td><td>188.37 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.02 (-0.93%)</td><td>0.01 <b>(+23.61%)</b></td><td>0.01 <b>(+51.06%)</b></td><td>0.01 <b>(+35.45%)</b></td><td>0.00 <b>(-56.45%)</b></td><td>336.80 <b>(-26.16%)</b></td><td>289.72 <b>(-22.44%)</b></td><td>282.00 <b>(-33.80%)</b></td><td>267.10 (+0.94%)</td><td>28.50 <b>(-67.47%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>456.10 (n/a)</td><td>373.56 (n/a)</td><td>426.00 (n/a)</td><td>264.60 (n/a)</td><td>87.59 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.00 <b>(-25.00%)</b></td><td>0.00 <b>(-46.15%)</b></td><td>0.00 <b>(-66.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-41.02%)</b></td><td>22437.57 (-0.74%)</td><td>17159.11 <b>(+41.52%)</b></td><td>17251.15 <b>(+160.84%)</b></td><td>7100.69 <b>(+35.21%)</b></td><td>6198.69 <b>(-29.56%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22605.29 (n/a)</td><td>12124.46 (n/a)</td><td>6613.74 (n/a)</td><td>5251.52 (n/a)</td><td>8799.81 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.00 (+9.09%)</td><td>0.00 (-2.86%)</td><td>0.00 (-16.67%)</td><td>0.00 (+0.00%)</td><td>0.00 (-1.37%)</td><td>22173.59 (+7.14%)</td><td>14317.42 (+1.70%)</td><td>16229.00 (+14.28%)</td><td>6831.76 (-9.05%)</td><td>5999.15 (-4.37%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20695.92 (n/a)</td><td>14077.66 (n/a)</td><td>14201.12 (n/a)</td><td>7511.46 (n/a)</td><td>6273.39 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>0.14 (+0.59%)</td><td>0.09 (+6.40%)</td><td>0.08 (+0.88%)</td><td>0.07 (+1.64%)</td><td>0.03 (-1.95%)</td><td>28258.41 (-1.57%)</td><td>23356.93 (-6.20%)</td><td>26230.02 (-0.84%)</td><td>15412.93 (-0.59%)</td><td>5313.91 (-1.01%)</td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28709.91 (n/a)</td><td>24899.92 (n/a)</td><td>26451.07 (n/a)</td><td>15504.10 (n/a)</td><td>5368.16 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>2.16 <b>(+31.23%)</b></td><td>1.23 (-12.77%)</td><td>0.92 <b>(-41.11%)</b></td><td>0.74 <b>(-28.96%)</b></td><td>0.58 <b>(+111.30%)</b></td><td>709.20 <b>(+40.77%)</b></td><td>492.42 <b>(+28.24%)</b></td><td>569.70 <b>(+69.81%)</b></td><td>242.70 <b>(-23.82%)</b></td><td>185.22 <b>(+124.68%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.65 (n/a)</td><td>1.41 (n/a)</td><td>1.56 (n/a)</td><td>1.04 (n/a)</td><td>0.27 (n/a)</td><td>503.80 (n/a)</td><td>383.98 (n/a)</td><td>335.50 (n/a)</td><td>318.60 (n/a)</td><td>82.44 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>2.94 (-6.39%)</td><td>1.39 <b>(-34.58%)</b></td><td>1.23 <b>(-43.92%)</b></td><td>0.32 <b>(-72.35%)</b></td><td>0.96 <b>(+28.26%)</b></td><td>3309.60 <b>(+261.59%)</b></td><td>1254.98 <b>(+126.35%)</b></td><td>850.10 <b>(+78.29%)</b></td><td>356.80 (+6.83%)</td><td>1174.78 <b>(+420.98%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>3.14 (n/a)</td><td>2.12 (n/a)</td><td>2.20 (n/a)</td><td>1.15 (n/a)</td><td>0.75 (n/a)</td><td>915.30 (n/a)</td><td>554.44 (n/a)</td><td>476.80 (n/a)</td><td>334.00 (n/a)</td><td>225.50 (n/a)</td>
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
<td><code>8354a4c</code> — 2026-09-12 01:02:31</td><td>2.21 <b>(+26.91%)</b></td><td>1.08 (+0.79%)</td><td>0.95 (+2.48%)</td><td>0.28 <b>(-41.09%)</b></td><td>0.70 <b>(+37.03%)</b></td><td>1876.20 <b>(+69.76%)</b></td><td>747.66 <b>(+24.20%)</b></td><td>552.00 (-2.42%)</td><td>237.20 <b>(-21.20%)</b></td><td>644.86 <b>(+102.36%)</b></td>
</tr>
<tr>
<td><code>7fa2bc1</code> — 2026-09-12 00:10:25</td><td>1.74 (n/a)</td><td>1.07 (n/a)</td><td>0.93 (n/a)</td><td>0.47 (n/a)</td><td>0.51 (n/a)</td><td>1105.20 (n/a)</td><td>601.98 (n/a)</td><td>565.70 (n/a)</td><td>301.00 (n/a)</td><td>318.68 (n/a)</td>
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
