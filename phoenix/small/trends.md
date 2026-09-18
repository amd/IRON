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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (-7.96%)</td><td>0.04 (-0.70%)</td><td>0.04 (+5.24%)</td><td>0.03 <b>(+21.20%)</b></td><td>0.01 <b>(-27.36%)</b></td><td>447.80 (-17.49%)</td><td>361.84 (-2.69%)</td><td>333.70 (-4.98%)</td><td>273.50 (+8.62%)</td><td>75.22 <b>(-33.16%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.70 (n/a)</td><td>371.84 (n/a)</td><td>351.20 (n/a)</td><td>251.80 (n/a)</td><td>112.53 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.05 (-12.52%)</td><td>0.04 (-7.79%)</td><td>0.03 (-16.78%)</td><td>0.02 (-10.55%)</td><td>0.01 (+1.84%)</td><td>567.90 (+11.79%)</td><td>377.80 (+10.09%)</td><td>367.50 <b>(+20.18%)</b></td><td>266.80 (+14.31%)</td><td>124.80 <b>(+20.64%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.00 (n/a)</td><td>343.16 (n/a)</td><td>305.80 (n/a)</td><td>233.40 (n/a)</td><td>103.45 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.05 (-3.45%)</td><td>0.04 (+16.82%)</td><td>0.04 <b>(+42.08%)</b></td><td>0.02 <b>(+24.05%)</b></td><td>0.01 (-6.44%)</td><td>497.50 (-19.38%)</td><td>358.38 (-15.74%)</td><td>286.90 <b>(-29.61%)</b></td><td>237.50 (+3.58%)</td><td>124.00 (-13.42%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>617.10 (n/a)</td><td>425.34 (n/a)</td><td>407.60 (n/a)</td><td>229.30 (n/a)</td><td>143.22 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (+7.13%)</td><td>0.01 (-15.09%)</td><td>0.01 <b>(-25.27%)</b></td><td>0.01 (-9.87%)</td><td>0.01 <b>(+24.46%)</b></td><td>658.00 (+10.94%)</td><td>479.82 <b>(+23.72%)</b></td><td>515.70 <b>(+33.81%)</b></td><td>225.50 (-6.63%)</td><td>170.07 <b>(+25.18%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.10 (n/a)</td><td>387.84 (n/a)</td><td>385.40 (n/a)</td><td>241.50 (n/a)</td><td>135.86 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (+5.69%)</td><td>0.02 <b>(+26.36%)</b></td><td>0.02 <b>(+59.66%)</b></td><td>0.01 (+4.29%)</td><td>0.00 <b>(+31.49%)</b></td><td>495.50 (-4.10%)</td><td>335.74 (-18.58%)</td><td>266.70 <b>(-37.36%)</b></td><td>253.20 (-5.38%)</td><td>110.90 <b>(+20.14%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>516.70 (n/a)</td><td>412.36 (n/a)</td><td>425.80 (n/a)</td><td>267.60 (n/a)</td><td>92.31 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 <b>(+55.91%)</b></td><td>0.02 <b>(+51.83%)</b></td><td>0.01 (+3.36%)</td><td>0.01 <b>(+229.26%)</b></td><td>0.01 <b>(+41.57%)</b></td><td>575.80 <b>(-69.63%)</b></td><td>379.64 <b>(-47.70%)</b></td><td>428.00 (-3.25%)</td><td>227.40 <b>(-35.87%)</b></td><td>147.87 <b>(-77.46%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1895.70 (n/a)</td><td>725.84 (n/a)</td><td>442.40 (n/a)</td><td>354.60 (n/a)</td><td>656.06 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (-8.62%)</td><td>0.01 (+2.80%)</td><td>0.01 (+2.98%)</td><td>0.01 (+3.60%)</td><td>0.01 (-10.14%)</td><td>507.30 (-3.46%)</td><td>385.00 (-4.24%)</td><td>430.30 (-2.91%)</td><td>244.00 (+9.47%)</td><td>119.63 (-7.64%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>525.50 (n/a)</td><td>402.04 (n/a)</td><td>443.20 (n/a)</td><td>222.90 (n/a)</td><td>129.53 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 <b>(+65.41%)</b></td><td>0.02 <b>(+81.16%)</b></td><td>0.02 <b>(+71.89%)</b></td><td>0.01 <b>(+199.72%)</b></td><td>0.00 (-5.54%)</td><td>370.70 <b>(-66.64%)</b></td><td>297.24 <b>(-50.59%)</b></td><td>288.80 <b>(-41.82%)</b></td><td>230.20 <b>(-39.53%)</b></td><td>51.90 <b>(-82.28%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1111.10 (n/a)</td><td>601.56 (n/a)</td><td>496.40 (n/a)</td><td>380.70 (n/a)</td><td>292.96 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 <b>(+50.98%)</b></td><td>0.01 <b>(+35.30%)</b></td><td>0.01 <b>(+32.80%)</b></td><td>0.01 <b>(+105.24%)</b></td><td>0.01 <b>(+33.37%)</b></td><td>924.50 <b>(-51.28%)</b></td><td>505.10 <b>(-35.17%)</b></td><td>449.00 <b>(-24.70%)</b></td><td>242.20 <b>(-33.77%)</b></td><td>272.76 <b>(-57.33%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1897.50 (n/a)</td><td>779.14 (n/a)</td><td>596.30 (n/a)</td><td>365.70 (n/a)</td><td>639.27 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>580.50 (n/a)</td><td>363.60 (n/a)</td><td>282.30 (n/a)</td><td>223.60 (n/a)</td><td>149.73 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.60 (n/a)</td><td>397.58 (n/a)</td><td>436.90 (n/a)</td><td>226.00 (n/a)</td><td>112.42 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>568.10 (n/a)</td><td>463.54 (n/a)</td><td>463.50 (n/a)</td><td>320.30 (n/a)</td><td>101.59 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.90 (n/a)</td><td>312.06 (n/a)</td><td>258.60 (n/a)</td><td>248.80 (n/a)</td><td>111.13 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>470.70 (n/a)</td><td>297.24 (n/a)</td><td>257.60 (n/a)</td><td>239.80 (n/a)</td><td>97.49 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>574.90 (n/a)</td><td>362.20 (n/a)</td><td>296.20 (n/a)</td><td>290.50 (n/a)</td><td>121.87 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.69 (-7.35%)</td><td>0.62 (-3.88%)</td><td>0.64 (-2.16%)</td><td>0.51 (-6.49%)</td><td>0.07 (-4.70%)</td><td>904.50 (+6.94%)</td><td>745.84 (+4.11%)</td><td>720.60 (+2.20%)</td><td>668.20 (+7.93%)</td><td>91.44 (+11.72%)</td><td>50.22 (-7.35%)</td><td>45.47 (-3.88%)</td><td>46.56 (-2.16%)</td><td>37.10 (-6.49%)</td><td>4.93 (-4.70%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.74 (n/a)</td><td>0.65 (n/a)</td><td>0.65 (n/a)</td><td>0.54 (n/a)</td><td>0.07 (n/a)</td><td>845.80 (n/a)</td><td>716.38 (n/a)</td><td>705.10 (n/a)</td><td>619.10 (n/a)</td><td>81.84 (n/a)</td><td>54.20 (n/a)</td><td>47.31 (n/a)</td><td>47.59 (n/a)</td><td>39.67 (n/a)</td><td>5.17 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.16 <b>(-23.64%)</b></td><td>0.84 <b>(-25.10%)</b></td><td>0.90 (-17.47%)</td><td>0.18 <b>(-76.94%)</b></td><td>0.38 <b>(+28.58%)</b></td><td>3545.40 <b>(+333.58%)</b></td><td>1241.26 <b>(+99.77%)</b></td><td>730.30 <b>(+21.17%)</b></td><td>566.30 <b>(+30.97%)</b></td><td>1290.33 <b>(+694.64%)</b></td><td>118.51 <b>(-23.64%)</b></td><td>85.59 <b>(-25.10%)</b></td><td>91.90 (-17.47%)</td><td>18.93 <b>(-76.94%)</b></td><td>39.15 <b>(+28.58%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.52 (n/a)</td><td>1.12 (n/a)</td><td>1.09 (n/a)</td><td>0.80 (n/a)</td><td>0.30 (n/a)</td><td>817.70 (n/a)</td><td>621.36 (n/a)</td><td>602.70 (n/a)</td><td>432.40 (n/a)</td><td>162.38 (n/a)</td><td>155.20 (n/a)</td><td>114.28 (n/a)</td><td>111.35 (n/a)</td><td>82.07 (n/a)</td><td>30.45 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.60 (+19.85%)</td><td>1.15 (+15.62%)</td><td>1.06 (+5.98%)</td><td>0.98 <b>(+73.17%)</b></td><td>0.26 <b>(-25.23%)</b></td><td>772.30 <b>(-42.25%)</b></td><td>677.66 <b>(-20.13%)</b></td><td>709.20 (-5.65%)</td><td>469.70 (-16.56%)</td><td>121.39 <b>(-63.36%)</b></td><td>178.60 (+19.85%)</td><td>127.91 (+15.62%)</td><td>118.28 (+5.98%)</td><td>108.62 <b>(+73.17%)</b></td><td>28.88 <b>(-25.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.34 (n/a)</td><td>0.99 (n/a)</td><td>1.00 (n/a)</td><td>0.56 (n/a)</td><td>0.35 (n/a)</td><td>1337.40 (n/a)</td><td>848.48 (n/a)</td><td>751.70 (n/a)</td><td>562.90 (n/a)</td><td>331.34 (n/a)</td><td>149.02 (n/a)</td><td>110.62 (n/a)</td><td>111.60 (n/a)</td><td>62.72 (n/a)</td><td>38.62 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.77 (+9.31%)</td><td>1.05 (+9.35%)</td><td>0.82 (-17.07%)</td><td>0.53 (+8.42%)</td><td>0.54 (+15.63%)</td><td>1975.20 (-7.77%)</td><td>1233.28 (-8.04%)</td><td>1283.70 <b>(+20.58%)</b></td><td>592.90 (-8.50%)</td><td>582.02 (-11.65%)</td><td>226.38 (+9.31%)</td><td>133.85 (+9.35%)</td><td>104.56 (-17.07%)</td><td>67.95 (+8.42%)</td><td>68.84 (+15.63%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.62 (n/a)</td><td>0.96 (n/a)</td><td>0.98 (n/a)</td><td>0.49 (n/a)</td><td>0.47 (n/a)</td><td>2141.50 (n/a)</td><td>1341.10 (n/a)</td><td>1064.60 (n/a)</td><td>648.00 (n/a)</td><td>658.76 (n/a)</td><td>207.11 (n/a)</td><td>122.40 (n/a)</td><td>126.08 (n/a)</td><td>62.68 (n/a)</td><td>59.54 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.82 (-15.41%)</td><td>1.41 (-14.01%)</td><td>1.29 (-19.21%)</td><td>1.16 (-11.36%)</td><td>0.27 <b>(-22.24%)</b></td><td>907.10 (+12.81%)</td><td>766.16 (+15.43%)</td><td>810.00 <b>(+23.78%)</b></td><td>574.80 (+18.22%)</td><td>136.31 (+0.92%)</td><td>233.49 (-15.41%)</td><td>180.15 (-14.01%)</td><td>165.70 (-19.21%)</td><td>147.96 (-11.36%)</td><td>35.19 <b>(-22.24%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>2.16 (n/a)</td><td>1.64 (n/a)</td><td>1.60 (n/a)</td><td>1.30 (n/a)</td><td>0.35 (n/a)</td><td>804.10 (n/a)</td><td>663.72 (n/a)</td><td>654.40 (n/a)</td><td>486.20 (n/a)</td><td>135.07 (n/a)</td><td>276.04 (n/a)</td><td>209.50 (n/a)</td><td>205.09 (n/a)</td><td>166.92 (n/a)</td><td>45.25 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>2.10 (-11.40%)</td><td>1.47 (+10.36%)</td><td>1.31 (+1.32%)</td><td>1.05 <b>(+221.83%)</b></td><td>0.47 <b>(-37.54%)</b></td><td>1003.10 <b>(-68.93%)</b></td><td>774.08 <b>(-37.04%)</b></td><td>799.80 (-1.30%)</td><td>500.30 (+12.88%)</td><td>230.56 <b>(-79.73%)</b></td><td>268.28 (-11.40%)</td><td>187.55 (+10.36%)</td><td>167.82 (+1.32%)</td><td>133.80 <b>(+221.83%)</b></td><td>60.15 <b>(-37.54%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>2.37 (n/a)</td><td>1.33 (n/a)</td><td>1.29 (n/a)</td><td>0.32 (n/a)</td><td>0.75 (n/a)</td><td>3228.20 (n/a)</td><td>1229.44 (n/a)</td><td>810.30 (n/a)</td><td>443.20 (n/a)</td><td>1137.38 (n/a)</td><td>302.81 (n/a)</td><td>169.95 (n/a)</td><td>165.64 (n/a)</td><td>41.58 (n/a)</td><td>96.31 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.58 (-17.80%)</td><td>1.37 (+16.27%)</td><td>1.45 (+18.41%)</td><td>0.93 <b>(+95.96%)</b></td><td>0.26 <b>(-55.62%)</b></td><td>1131.30 <b>(-48.97%)</b></td><td>793.16 <b>(-30.61%)</b></td><td>721.60 (-15.55%)</td><td>663.30 <b>(+21.66%)</b></td><td>192.51 <b>(-71.93%)</b></td><td>202.35 (-17.80%)</td><td>175.65 (+16.27%)</td><td>186.00 (+18.41%)</td><td>118.64 <b>(+95.96%)</b></td><td>33.31 <b>(-55.62%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.92 (n/a)</td><td>1.18 (n/a)</td><td>1.23 (n/a)</td><td>0.47 (n/a)</td><td>0.59 (n/a)</td><td>2217.00 (n/a)</td><td>1143.06 (n/a)</td><td>854.50 (n/a)</td><td>545.20 (n/a)</td><td>685.83 (n/a)</td><td>246.17 (n/a)</td><td>151.07 (n/a)</td><td>157.07 (n/a)</td><td>60.54 (n/a)</td><td>75.06 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.80 (-18.50%)</td><td>0.63 (+2.11%)</td><td>0.72 <b>(+30.79%)</b></td><td>0.37 (+8.79%)</td><td>0.19 <b>(-25.40%)</b></td><td>966.90 (-8.08%)</td><td>621.56 (-6.31%)</td><td>500.30 <b>(-23.54%)</b></td><td>449.10 <b>(+22.70%)</b></td><td>221.99 (-16.36%)</td><td>37.35 (-18.50%)</td><td>29.45 (+2.11%)</td><td>33.54 <b>(+30.79%)</b></td><td>17.35 (+8.79%)</td><td>8.72 <b>(-25.40%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.98 (n/a)</td><td>0.62 (n/a)</td><td>0.55 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>1051.90 (n/a)</td><td>663.40 (n/a)</td><td>654.30 (n/a)</td><td>366.00 (n/a)</td><td>265.40 (n/a)</td><td>45.84 (n/a)</td><td>28.84 (n/a)</td><td>25.64 (n/a)</td><td>15.95 (n/a)</td><td>11.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>3.46 (-15.37%)</td><td>2.17 <b>(-28.12%)</b></td><td>2.40 <b>(-35.62%)</b></td><td>0.69 <b>(-59.72%)</b></td><td>1.22 (+4.82%)</td><td>3825.90 <b>(+148.24%)</b></td><td>1755.22 <b>(+74.77%)</b></td><td>1093.30 <b>(+55.32%)</b></td><td>758.40 (+18.15%)</td><td>1309.04 <b>(+192.27%)</b></td><td>707.88 (-15.37%)</td><td>445.28 <b>(-28.12%)</b></td><td>491.04 <b>(-35.62%)</b></td><td>140.33 <b>(-59.72%)</b></td><td>250.06 (+4.82%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>4.08 (n/a)</td><td>3.02 (n/a)</td><td>3.72 (n/a)</td><td>1.70 (n/a)</td><td>1.16 (n/a)</td><td>1541.20 (n/a)</td><td>1004.30 (n/a)</td><td>703.90 (n/a)</td><td>641.90 (n/a)</td><td>447.88 (n/a)</td><td>836.40 (n/a)</td><td>619.43 (n/a)</td><td>762.67 (n/a)</td><td>348.35 (n/a)</td><td>238.56 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.20 (n/a)</td><td>379.18 (n/a)</td><td>436.70 (n/a)</td><td>242.80 (n/a)</td><td>125.75 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>707.60 (n/a)</td><td>435.16 (n/a)</td><td>306.50 (n/a)</td><td>255.90 (n/a)</td><td>208.29 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.60 (n/a)</td><td>443.64 (n/a)</td><td>408.40 (n/a)</td><td>304.80 (n/a)</td><td>149.08 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>631.40 (n/a)</td><td>482.54 (n/a)</td><td>538.10 (n/a)</td><td>259.70 (n/a)</td><td>147.41 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>682.50 (n/a)</td><td>437.58 (n/a)</td><td>443.30 (n/a)</td><td>192.30 (n/a)</td><td>220.75 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1997.80 (n/a)</td><td>759.14 (n/a)</td><td>490.60 (n/a)</td><td>309.70 (n/a)</td><td>698.14 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.64 (-1.16%)</td><td>0.46 (+2.11%)</td><td>0.48 (+9.57%)</td><td>0.32 (+15.57%)</td><td>0.13 (-6.51%)</td><td>689.60 (-13.48%)</td><td>518.58 (-3.51%)</td><td>463.50 (-8.72%)</td><td>346.20 (+1.20%)</td><td>146.36 (-15.31%)</td><td>27.26 (-1.16%)</td><td>19.43 (+2.11%)</td><td>20.36 (+9.57%)</td><td>13.69 (+15.57%)</td><td>5.56 (-6.51%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.65 (n/a)</td><td>0.45 (n/a)</td><td>0.44 (n/a)</td><td>0.28 (n/a)</td><td>0.14 (n/a)</td><td>797.00 (n/a)</td><td>537.46 (n/a)</td><td>507.80 (n/a)</td><td>342.10 (n/a)</td><td>172.81 (n/a)</td><td>27.58 (n/a)</td><td>19.03 (n/a)</td><td>18.58 (n/a)</td><td>11.84 (n/a)</td><td>5.94 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.58 (+3.42%)</td><td>0.45 (+3.52%)</td><td>0.42 (-0.14%)</td><td>0.36 (+2.95%)</td><td>0.09 (-1.25%)</td><td>621.90 (-2.87%)</td><td>507.50 (-3.77%)</td><td>527.40 (+0.15%)</td><td>378.30 (-3.32%)</td><td>96.54 (-9.92%)</td><td>24.95 (+3.42%)</td><td>19.18 (+3.52%)</td><td>17.89 (-0.14%)</td><td>15.17 (+2.95%)</td><td>3.91 (-1.25%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.57 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>640.30 (n/a)</td><td>527.40 (n/a)</td><td>526.60 (n/a)</td><td>391.30 (n/a)</td><td>107.17 (n/a)</td><td>24.12 (n/a)</td><td>18.53 (n/a)</td><td>17.92 (n/a)</td><td>14.74 (n/a)</td><td>3.96 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.31 (+0.68%)</td><td>0.31 (+1.40%)</td><td>0.31 (+1.80%)</td><td>0.30 (+1.24%)</td><td>0.00 <b>(-20.08%)</b></td><td>82829.70 (-1.23%)</td><td>81633.18 (-1.39%)</td><td>81474.10 (-1.77%)</td><td>80569.10 (-0.67%)</td><td>836.86 <b>(-21.47%)</b></td><td>213.23 (+0.68%)</td><td>210.47 (+1.40%)</td><td>210.86 (+1.80%)</td><td>207.41 (+1.24%)</td><td>2.15 <b>(-20.08%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83858.60 (n/a)</td><td>82780.98 (n/a)</td><td>82941.30 (n/a)</td><td>81113.10 (n/a)</td><td>1065.68 (n/a)</td><td>211.80 (n/a)</td><td>207.56 (n/a)</td><td>207.13 (n/a)</td><td>204.87 (n/a)</td><td>2.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.17 (+1.65%)</td><td>1.13 (+0.47%)</td><td>1.15 (+0.15%)</td><td>1.07 (-0.49%)</td><td>0.04 (+17.37%)</td><td>23478.80 (+0.49%)</td><td>22304.34 (-0.44%)</td><td>21928.50 (-0.15%)</td><td>21586.50 (-1.62%)</td><td>762.82 (+16.81%)</td><td>795.86 (+1.65%)</td><td>770.95 (+0.47%)</td><td>783.45 (+0.15%)</td><td>731.72 (-0.49%)</td><td>25.81 (+17.37%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.15 (n/a)</td><td>1.12 (n/a)</td><td>1.15 (n/a)</td><td>1.08 (n/a)</td><td>0.03 (n/a)</td><td>23364.70 (n/a)</td><td>22403.24 (n/a)</td><td>21961.10 (n/a)</td><td>21942.30 (n/a)</td><td>653.04 (n/a)</td><td>782.96 (n/a)</td><td>767.36 (n/a)</td><td>782.29 (n/a)</td><td>735.29 (n/a)</td><td>21.99 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>3.77 (-5.02%)</td><td>2.31 <b>(-24.33%)</b></td><td>1.84 <b>(-45.67%)</b></td><td>1.43 <b>(-23.30%)</b></td><td>0.94 (-7.46%)</td><td>5652.30 <b>(+30.39%)</b></td><td>3930.34 <b>(+33.85%)</b></td><td>4384.00 <b>(+84.06%)</b></td><td>2138.60 (+5.28%)</td><td>1375.39 <b>(+25.61%)</b></td><td>988.47 (-5.02%)</td><td>604.49 <b>(-24.33%)</b></td><td>482.19 <b>(-45.67%)</b></td><td>374.00 <b>(-23.30%)</b></td><td>246.78 (-7.46%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>3.97 (n/a)</td><td>3.05 (n/a)</td><td>3.38 (n/a)</td><td>1.86 (n/a)</td><td>1.02 (n/a)</td><td>4335.00 (n/a)</td><td>2936.48 (n/a)</td><td>2381.80 (n/a)</td><td>2031.30 (n/a)</td><td>1095.01 (n/a)</td><td>1040.67 (n/a)</td><td>798.83 (n/a)</td><td>887.54 (n/a)</td><td>487.64 (n/a)</td><td>266.67 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.21 <b>(-22.21%)</b></td><td>0.19 (-6.91%)</td><td>0.19 (-2.67%)</td><td>0.18 (+3.39%)</td><td>0.01 <b>(-69.17%)</b></td><td>6815.30 (-3.28%)</td><td>6438.68 (+5.12%)</td><td>6413.90 (+2.74%)</td><td>5844.00 <b>(+28.55%)</b></td><td>386.88 <b>(-61.31%)</b></td><td>11.48 <b>(-22.21%)</b></td><td>10.45 (-6.91%)</td><td>10.46 (-2.67%)</td><td>9.85 (+3.39%)</td><td>0.65 <b>(-69.17%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>7046.30 (n/a)</td><td>6125.32 (n/a)</td><td>6242.80 (n/a)</td><td>4546.10 (n/a)</td><td>1000.02 (n/a)</td><td>14.76 (n/a)</td><td>11.23 (n/a)</td><td>10.75 (n/a)</td><td>9.52 (n/a)</td><td>2.11 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>3.82 (n/a)</td><td>3.61 (n/a)</td><td>3.52 (n/a)</td><td>3.43 (n/a)</td><td>0.19 (n/a)</td><td>3.82 (n/a)</td><td>3.60 (n/a)</td><td>3.52 (n/a)</td><td>3.43 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>6.70 (-11.75%)</td><td>5.96 (-11.20%)</td><td>5.78 (-16.49%)</td><td>5.24 (-5.42%)</td><td>0.63 <b>(-20.27%)</b></td><td>6.70 (-11.75%)</td><td>5.96 (-11.20%)</td><td>5.77 (-16.49%)</td><td>5.23 (-5.42%)</td><td>0.63 <b>(-20.27%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>7.60 (n/a)</td><td>6.71 (n/a)</td><td>6.92 (n/a)</td><td>5.54 (n/a)</td><td>0.79 (n/a)</td><td>7.59 (n/a)</td><td>6.71 (n/a)</td><td>6.91 (n/a)</td><td>5.53 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>9.87 <b>(-29.91%)</b></td><td>8.65 (-12.55%)</td><td>8.96 (-5.73%)</td><td>7.09 (-6.99%)</td><td>1.09 <b>(-56.04%)</b></td><td>9.87 <b>(-29.91%)</b></td><td>8.64 (-12.55%)</td><td>8.95 (-5.73%)</td><td>7.09 (-6.99%)</td><td>1.09 <b>(-56.04%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>14.09 (n/a)</td><td>9.89 (n/a)</td><td>9.50 (n/a)</td><td>7.63 (n/a)</td><td>2.49 (n/a)</td><td>14.08 (n/a)</td><td>9.88 (n/a)</td><td>9.50 (n/a)</td><td>7.62 (n/a)</td><td>2.49 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>3.76 (n/a)</td><td>3.53 (n/a)</td><td>3.60 (n/a)</td><td>3.29 (n/a)</td><td>0.19 (n/a)</td><td>3.76 (n/a)</td><td>3.52 (n/a)</td><td>3.60 (n/a)</td><td>3.29 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>7.06 (-3.24%)</td><td>6.18 (+1.16%)</td><td>6.44 (+12.89%)</td><td>4.83 (-13.55%)</td><td>0.96 <b>(+34.66%)</b></td><td>7.06 (-3.24%)</td><td>6.18 (+1.16%)</td><td>6.44 (+12.89%)</td><td>4.83 (-13.55%)</td><td>0.96 <b>(+34.66%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>7.30 (n/a)</td><td>6.11 (n/a)</td><td>5.71 (n/a)</td><td>5.59 (n/a)</td><td>0.72 (n/a)</td><td>7.29 (n/a)</td><td>6.11 (n/a)</td><td>5.70 (n/a)</td><td>5.59 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>13.74 (+10.20%)</td><td>9.89 (+5.59%)</td><td>9.19 (+11.52%)</td><td>8.18 (+1.58%)</td><td>2.22 (+16.61%)</td><td>13.73 (+10.20%)</td><td>9.89 (+5.59%)</td><td>9.18 (+11.52%)</td><td>8.17 (+1.58%)</td><td>2.22 (+16.61%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>12.47 (n/a)</td><td>9.37 (n/a)</td><td>8.24 (n/a)</td><td>8.05 (n/a)</td><td>1.91 (n/a)</td><td>12.46 (n/a)</td><td>9.36 (n/a)</td><td>8.23 (n/a)</td><td>8.05 (n/a)</td><td>1.91 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>3.18 (+1.42%)</td><td>2.32 (+0.45%)</td><td>2.80 (+1.65%)</td><td>1.24 (+3.34%)</td><td>0.88 (-2.64%)</td><td>3.17 (+1.42%)</td><td>2.32 (+0.45%)</td><td>2.80 (+1.65%)</td><td>1.24 (+3.34%)</td><td>0.88 (-2.64%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>3.13 (n/a)</td><td>2.31 (n/a)</td><td>2.76 (n/a)</td><td>1.20 (n/a)</td><td>0.91 (n/a)</td><td>3.13 (n/a)</td><td>2.31 (n/a)</td><td>2.75 (n/a)</td><td>1.20 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.57 (-1.71%)</td><td>0.45 <b>(+77.20%)</b></td><td>0.45 <b>(+219.22%)</b></td><td>0.34 <b>(+342.38%)</b></td><td>0.10 <b>(-50.92%)</b></td><td>0.56 (-1.71%)</td><td>0.44 <b>(+77.20%)</b></td><td>0.45 <b>(+219.22%)</b></td><td>0.33 <b>(+342.38%)</b></td><td>0.10 <b>(-50.92%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.58 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.21 (n/a)</td><td>0.57 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.75 (+18.59%)</td><td>0.46 (-1.76%)</td><td>0.34 <b>(-45.96%)</b></td><td>0.25 <b>(+202.15%)</b></td><td>0.24 (-0.22%)</td><td>0.74 (+18.59%)</td><td>0.46 (-1.76%)</td><td>0.33 <b>(-45.96%)</b></td><td>0.24 <b>(+202.15%)</b></td><td>0.24 (-0.22%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.63 (n/a)</td><td>0.47 (n/a)</td><td>0.63 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td><td>0.62 (n/a)</td><td>0.46 (n/a)</td><td>0.62 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>2.58 (+10.41%)</td><td>1.79 (+4.12%)</td><td>2.40 <b>(+37.36%)</b></td><td>0.44 (-5.04%)</td><td>0.96 <b>(+25.66%)</b></td><td>2.54 (+10.41%)</td><td>1.76 (+4.12%)</td><td>2.36 <b>(+37.36%)</b></td><td>0.43 (-5.04%)</td><td>0.95 <b>(+25.66%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>2.34 (n/a)</td><td>1.72 (n/a)</td><td>1.74 (n/a)</td><td>0.46 (n/a)</td><td>0.77 (n/a)</td><td>2.30 (n/a)</td><td>1.69 (n/a)</td><td>1.72 (n/a)</td><td>0.45 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>470.70 (n/a)</td><td>362.08 (n/a)</td><td>413.10 (n/a)</td><td>240.20 (n/a)</td><td>105.06 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.50 (n/a)</td><td>381.38 (n/a)</td><td>431.20 (n/a)</td><td>206.80 (n/a)</td><td>153.09 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>463.20 (n/a)</td><td>351.42 (n/a)</td><td>376.70 (n/a)</td><td>215.40 (n/a)</td><td>116.40 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>634.70 (n/a)</td><td>442.08 (n/a)</td><td>412.10 (n/a)</td><td>310.80 (n/a)</td><td>120.30 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2449.90 (n/a)</td><td>866.50 (n/a)</td><td>491.00 (n/a)</td><td>273.60 (n/a)</td><td>895.78 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1082.40 (n/a)</td><td>575.18 (n/a)</td><td>504.40 (n/a)</td><td>302.20 (n/a)</td><td>296.04 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (-9.71%)</td><td>0.02 <b>(-30.69%)</b></td><td>0.02 <b>(-40.45%)</b></td><td>0.01 <b>(-41.01%)</b></td><td>0.01 <b>(+48.58%)</b></td><td>639.90 <b>(+69.51%)</b></td><td>443.42 <b>(+56.03%)</b></td><td>432.50 <b>(+67.90%)</b></td><td>269.20 (+10.78%)</td><td>156.30 <b>(+178.29%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>377.50 (n/a)</td><td>284.18 (n/a)</td><td>257.60 (n/a)</td><td>243.00 (n/a)</td><td>56.17 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (+0.40%)</td><td>0.03 (-10.11%)</td><td>0.03 (-0.37%)</td><td>0.02 <b>(-39.31%)</b></td><td>0.01 <b>(+71.96%)</b></td><td>442.50 <b>(+64.74%)</b></td><td>278.16 (+18.01%)</td><td>248.70 (+0.36%)</td><td>198.30 (-0.40%)</td><td>95.68 <b>(+202.26%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>268.60 (n/a)</td><td>235.70 (n/a)</td><td>247.80 (n/a)</td><td>199.10 (n/a)</td><td>31.66 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (-15.08%)</td><td>0.03 (+11.09%)</td><td>0.03 (+19.00%)</td><td>0.02 <b>(+20.41%)</b></td><td>0.01 <b>(-30.03%)</b></td><td>513.50 (-16.95%)</td><td>295.00 (-17.75%)</td><td>240.10 (-15.96%)</td><td>222.40 (+17.73%)</td><td>123.86 <b>(-31.00%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.30 (n/a)</td><td>358.66 (n/a)</td><td>285.70 (n/a)</td><td>188.90 (n/a)</td><td>179.51 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (-8.30%)</td><td>0.03 (-7.91%)</td><td>0.03 (-1.24%)</td><td>0.01 (-9.44%)</td><td>0.01 (-4.79%)</td><td>552.20 (+10.42%)</td><td>329.16 (+9.19%)</td><td>267.70 (+1.25%)</td><td>258.60 (+9.07%)</td><td>126.24 (+12.82%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.10 (n/a)</td><td>301.46 (n/a)</td><td>264.40 (n/a)</td><td>237.10 (n/a)</td><td>111.90 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 <b>(+35.02%)</b></td><td>0.03 <b>(+40.39%)</b></td><td>0.03 <b>(+63.52%)</b></td><td>0.02 <b>(+40.28%)</b></td><td>0.01 (+7.10%)</td><td>417.10 <b>(-28.71%)</b></td><td>289.00 <b>(-30.80%)</b></td><td>280.20 <b>(-38.83%)</b></td><td>205.00 <b>(-25.94%)</b></td><td>79.37 <b>(-39.02%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.10 (n/a)</td><td>417.60 (n/a)</td><td>458.10 (n/a)</td><td>276.80 (n/a)</td><td>130.16 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 <b>(-29.29%)</b></td><td>0.02 (-18.83%)</td><td>0.02 (-15.67%)</td><td>0.01 <b>(-21.19%)</b></td><td>0.01 <b>(-25.71%)</b></td><td>579.50 <b>(+26.89%)</b></td><td>444.10 <b>(+23.33%)</b></td><td>474.80 (+18.58%)</td><td>288.70 <b>(+41.45%)</b></td><td>138.83 <b>(+34.64%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>456.70 (n/a)</td><td>360.08 (n/a)</td><td>400.40 (n/a)</td><td>204.10 (n/a)</td><td>103.11 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (-1.49%)</td><td>0.02 (-7.13%)</td><td>0.02 <b>(-30.71%)</b></td><td>0.02 (+5.70%)</td><td>0.01 (+6.93%)</td><td>508.30 (-5.40%)</td><td>405.14 (+8.72%)</td><td>481.70 <b>(+44.35%)</b></td><td>254.00 (+1.52%)</td><td>124.54 (+3.66%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.30 (n/a)</td><td>372.64 (n/a)</td><td>333.70 (n/a)</td><td>250.20 (n/a)</td><td>120.14 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (-19.04%)</td><td>0.02 (-17.14%)</td><td>0.02 <b>(-26.37%)</b></td><td>0.01 (+10.24%)</td><td>0.01 <b>(-35.52%)</b></td><td>565.60 (-9.30%)</td><td>468.88 (+11.63%)</td><td>512.30 <b>(+35.82%)</b></td><td>277.30 <b>(+23.52%)</b></td><td>112.49 <b>(-34.14%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.60 (n/a)</td><td>420.02 (n/a)</td><td>377.20 (n/a)</td><td>224.50 (n/a)</td><td>170.80 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (+0.40%)</td><td>0.03 (+4.86%)</td><td>0.03 (+7.03%)</td><td>0.03 (+10.76%)</td><td>0.00 <b>(-25.12%)</b></td><td>288.60 (-9.73%)</td><td>253.30 (-5.20%)</td><td>244.30 (-6.54%)</td><td>233.30 (-0.38%)</td><td>22.76 <b>(-32.85%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>319.70 (n/a)</td><td>267.20 (n/a)</td><td>261.40 (n/a)</td><td>234.20 (n/a)</td><td>33.90 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (-13.09%)</td><td>0.02 (-0.68%)</td><td>0.02 (+5.66%)</td><td>0.01 (-15.63%)</td><td>0.01 (-2.67%)</td><td>582.90 (+18.52%)</td><td>398.46 (+2.51%)</td><td>372.40 (-5.36%)</td><td>278.60 (+15.08%)</td><td>127.01 <b>(+35.24%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.80 (n/a)</td><td>388.70 (n/a)</td><td>393.50 (n/a)</td><td>242.10 (n/a)</td><td>93.92 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (-18.08%)</td><td>0.02 (+6.21%)</td><td>0.02 <b>(+47.16%)</b></td><td>0.01 <b>(+264.00%)</b></td><td>0.01 <b>(-42.92%)</b></td><td>679.80 <b>(-72.53%)</b></td><td>449.90 <b>(-45.65%)</b></td><td>382.70 <b>(-32.05%)</b></td><td>288.80 <b>(+22.06%)</b></td><td>174.98 <b>(-81.28%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2474.30 (n/a)</td><td>827.78 (n/a)</td><td>563.20 (n/a)</td><td>236.60 (n/a)</td><td>934.53 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 <b>(-35.40%)</b></td><td>0.02 (-14.31%)</td><td>0.02 (-13.13%)</td><td>0.02 (+10.27%)</td><td>0.00 <b>(-70.00%)</b></td><td>542.20 (-9.32%)</td><td>484.20 (+8.46%)</td><td>474.40 (+15.12%)</td><td>403.10 <b>(+54.80%)</b></td><td>56.84 <b>(-57.41%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.90 (n/a)</td><td>446.44 (n/a)</td><td>412.10 (n/a)</td><td>260.40 (n/a)</td><td>133.46 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (+11.19%)</td><td>0.03 (+17.33%)</td><td>0.03 <b>(+52.00%)</b></td><td>0.02 (+10.83%)</td><td>0.01 (+1.87%)</td><td>507.70 (-9.77%)</td><td>353.64 (-16.04%)</td><td>305.10 <b>(-34.22%)</b></td><td>223.10 (-10.08%)</td><td>122.72 (-15.05%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.70 (n/a)</td><td>421.22 (n/a)</td><td>463.80 (n/a)</td><td>248.10 (n/a)</td><td>144.47 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 <b>(-32.36%)</b></td><td>0.01 <b>(-33.97%)</b></td><td>0.01 (-19.16%)</td><td>0.00 <b>(-63.15%)</b></td><td>0.01 (-10.99%)</td><td>1932.00 <b>(+171.39%)</b></td><td>860.34 <b>(+81.41%)</b></td><td>589.90 <b>(+23.69%)</b></td><td>459.60 <b>(+47.83%)</b></td><td>616.26 <b>(+279.48%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>711.90 (n/a)</td><td>474.26 (n/a)</td><td>476.90 (n/a)</td><td>310.90 (n/a)</td><td>162.40 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.10 (-10.65%)</td><td>0.08 (-0.05%)</td><td>0.09 (+0.89%)</td><td>0.05 <b>(+38.65%)</b></td><td>0.02 <b>(-25.01%)</b></td><td>487.10 <b>(-27.88%)</b></td><td>347.36 (-7.95%)</td><td>272.90 (-0.87%)</td><td>257.10 (+11.93%)</td><td>113.79 <b>(-39.44%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>675.40 (n/a)</td><td>377.38 (n/a)</td><td>275.30 (n/a)</td><td>229.70 (n/a)</td><td>187.89 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.15 (-7.59%)</td><td>0.13 (-11.69%)</td><td>0.14 (-4.77%)</td><td>0.10 <b>(-28.73%)</b></td><td>0.02 <b>(+109.54%)</b></td><td>418.10 <b>(+40.30%)</b></td><td>317.48 (+15.51%)</td><td>293.00 (+4.98%)</td><td>270.60 (+8.20%)</td><td>58.68 <b>(+228.66%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>298.00 (n/a)</td><td>274.86 (n/a)</td><td>279.10 (n/a)</td><td>250.10 (n/a)</td><td>17.85 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (-7.52%)</td><td>0.01 (-13.39%)</td><td>0.02 (+6.43%)</td><td>0.01 (-9.17%)</td><td>0.01 <b>(+21.40%)</b></td><td>638.30 (+10.11%)</td><td>410.56 <b>(+23.64%)</b></td><td>276.00 (-6.03%)</td><td>252.30 (+8.14%)</td><td>196.72 <b>(+39.59%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.70 (n/a)</td><td>332.06 (n/a)</td><td>293.70 (n/a)</td><td>233.30 (n/a)</td><td>140.93 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (+18.79%)</td><td>0.03 (+2.66%)</td><td>0.03 (-0.52%)</td><td>0.01 <b>(-22.04%)</b></td><td>0.01 <b>(+57.17%)</b></td><td>570.80 <b>(+28.30%)</b></td><td>318.28 (+4.93%)</td><td>271.10 (+0.52%)</td><td>204.20 (-15.83%)</td><td>145.16 <b>(+77.17%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>444.90 (n/a)</td><td>303.32 (n/a)</td><td>269.70 (n/a)</td><td>242.60 (n/a)</td><td>81.93 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.06 <b>(+36.20%)</b></td><td>0.04 <b>(+46.41%)</b></td><td>0.05 <b>(+71.95%)</b></td><td>0.02 <b>(+30.45%)</b></td><td>0.01 <b>(+58.21%)</b></td><td>511.60 <b>(-23.34%)</b></td><td>324.52 <b>(-29.74%)</b></td><td>265.00 <b>(-41.85%)</b></td><td>221.00 <b>(-26.58%)</b></td><td>119.80 (-10.11%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>667.40 (n/a)</td><td>461.90 (n/a)</td><td>455.70 (n/a)</td><td>301.00 (n/a)</td><td>133.27 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (-9.87%)</td><td>0.02 <b>(-21.00%)</b></td><td>0.03 <b>(-20.53%)</b></td><td>0.02 (-18.24%)</td><td>0.01 (+16.03%)</td><td>487.00 <b>(+22.30%)</b></td><td>361.10 <b>(+31.09%)</b></td><td>310.10 <b>(+25.85%)</b></td><td>247.90 (+10.97%)</td><td>113.51 <b>(+60.55%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>398.20 (n/a)</td><td>275.46 (n/a)</td><td>246.40 (n/a)</td><td>223.40 (n/a)</td><td>70.70 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 <b>(-23.43%)</b></td><td>0.02 (-19.16%)</td><td>0.02 <b>(-20.20%)</b></td><td>0.02 (+9.18%)</td><td>0.01 <b>(-36.35%)</b></td><td>575.00 (-8.41%)</td><td>492.74 (+14.05%)</td><td>544.80 <b>(+25.33%)</b></td><td>268.80 <b>(+30.61%)</b></td><td>126.95 <b>(-27.37%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>627.80 (n/a)</td><td>432.04 (n/a)</td><td>434.70 (n/a)</td><td>205.80 (n/a)</td><td>174.77 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (-7.43%)</td><td>0.02 (+4.32%)</td><td>0.02 (+7.95%)</td><td>0.02 (+4.91%)</td><td>0.01 (+1.02%)</td><td>487.10 (-4.68%)</td><td>362.76 (-3.57%)</td><td>375.20 (-7.36%)</td><td>239.80 (+8.07%)</td><td>116.24 (+4.31%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.00 (n/a)</td><td>376.18 (n/a)</td><td>405.00 (n/a)</td><td>221.90 (n/a)</td><td>111.44 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.06 (+11.90%)</td><td>0.03 (+1.78%)</td><td>0.02 (-17.86%)</td><td>0.02 (+13.69%)</td><td>0.02 (+18.37%)</td><td>586.50 (-12.04%)</td><td>465.18 (+0.69%)</td><td>533.20 <b>(+21.76%)</b></td><td>172.50 (-10.67%)</td><td>171.84 (-7.52%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>666.80 (n/a)</td><td>462.00 (n/a)</td><td>437.90 (n/a)</td><td>193.10 (n/a)</td><td>185.83 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 <b>(+23.14%)</b></td><td>0.03 <b>(+20.36%)</b></td><td>0.03 <b>(+35.59%)</b></td><td>0.02 (-0.20%)</td><td>0.01 <b>(+50.85%)</b></td><td>544.10 (+0.20%)</td><td>366.16 (-11.23%)</td><td>304.10 <b>(-26.24%)</b></td><td>218.20 (-18.76%)</td><td>158.00 <b>(+24.88%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.00 (n/a)</td><td>412.48 (n/a)</td><td>412.30 (n/a)</td><td>268.60 (n/a)</td><td>126.52 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (-4.68%)</td><td>0.02 (-5.54%)</td><td>0.02 (-2.64%)</td><td>0.00 (-6.00%)</td><td>0.01 (-4.13%)</td><td>1986.70 (+6.39%)</td><td>734.26 (+6.66%)</td><td>435.90 (+2.73%)</td><td>245.40 (+4.92%)</td><td>715.21 (+6.53%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1867.40 (n/a)</td><td>688.44 (n/a)</td><td>424.30 (n/a)</td><td>233.90 (n/a)</td><td>671.34 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 (+5.67%)</td><td>0.02 (-19.45%)</td><td>0.03 (+3.91%)</td><td>0.00 <b>(-71.73%)</b></td><td>0.01 <b>(+106.79%)</b></td><td>1891.70 <b>(+253.79%)</b></td><td>724.90 <b>(+124.04%)</b></td><td>265.40 (-3.74%)</td><td>232.20 (-5.38%)</td><td>723.13 <b>(+506.65%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.70 (n/a)</td><td>323.56 (n/a)</td><td>275.70 (n/a)</td><td>245.40 (n/a)</td><td>119.20 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.04 <b>(+51.49%)</b></td><td>0.02 <b>(+29.92%)</b></td><td>0.02 (+6.29%)</td><td>0.02 (+5.58%)</td><td>0.01 <b>(+174.60%)</b></td><td>561.10 (-5.28%)</td><td>423.70 (-15.25%)</td><td>479.30 (-5.91%)</td><td>248.90 <b>(-33.98%)</b></td><td>152.73 <b>(+71.59%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>592.40 (n/a)</td><td>499.96 (n/a)</td><td>509.40 (n/a)</td><td>377.00 (n/a)</td><td>89.01 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.03 (+4.83%)</td><td>0.02 (-9.44%)</td><td>0.02 <b>(-21.40%)</b></td><td>0.00 <b>(-64.83%)</b></td><td>0.01 <b>(+89.66%)</b></td><td>1717.30 <b>(+184.37%)</b></td><td>694.54 <b>(+56.65%)</b></td><td>537.30 <b>(+27.23%)</b></td><td>291.70 (-4.61%)</td><td>590.72 <b>(+392.50%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.90 (n/a)</td><td>443.38 (n/a)</td><td>422.30 (n/a)</td><td>305.80 (n/a)</td><td>119.94 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.41 (+3.61%)</td><td>0.33 (+15.71%)</td><td>0.34 (+12.34%)</td><td>0.17 (-5.70%)</td><td>0.09 (+6.53%)</td><td>568.20 (+6.05%)</td><td>326.72 (-12.36%)</td><td>285.80 (-10.99%)</td><td>241.80 (-3.47%)</td><td>137.02 (+10.45%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>535.80 (n/a)</td><td>372.80 (n/a)</td><td>321.10 (n/a)</td><td>250.50 (n/a)</td><td>124.05 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.42 (+6.34%)</td><td>0.29 <b>(+44.21%)</b></td><td>0.24 <b>(+24.34%)</b></td><td>0.18 <b>(+239.46%)</b></td><td>0.11 (-8.78%)</td><td>548.60 <b>(-70.54%)</b></td><td>379.40 <b>(-48.67%)</b></td><td>402.20 (-19.58%)</td><td>232.60 (-5.98%)</td><td>139.10 <b>(-78.29%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.40 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>0.12 (n/a)</td><td>1862.30 (n/a)</td><td>739.08 (n/a)</td><td>500.10 (n/a)</td><td>247.40 (n/a)</td><td>640.69 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.41 (+11.50%)</td><td>0.27 (+16.23%)</td><td>0.21 (+15.03%)</td><td>0.15 (-15.47%)</td><td>0.12 <b>(+48.63%)</b></td><td>646.60 (+18.29%)</td><td>433.02 (-6.61%)</td><td>464.00 (-13.06%)</td><td>241.20 (-10.30%)</td><td>178.03 <b>(+49.98%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.37 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>546.60 (n/a)</td><td>463.68 (n/a)</td><td>533.70 (n/a)</td><td>268.90 (n/a)</td><td>118.70 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.29 (-2.40%)</td><td>0.19 (-4.07%)</td><td>0.20 (+19.77%)</td><td>0.11 (-8.12%)</td><td>0.07 (+2.00%)</td><td>661.90 (+8.85%)</td><td>441.28 (+6.25%)</td><td>371.50 (-16.52%)</td><td>257.00 (+2.43%)</td><td>164.42 (+19.40%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>608.10 (n/a)</td><td>415.34 (n/a)</td><td>445.00 (n/a)</td><td>250.90 (n/a)</td><td>137.71 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.29 <b>(+20.48%)</b></td><td>0.27 <b>(+83.67%)</b></td><td>0.27 <b>(+113.74%)</b></td><td>0.25 <b>(+246.36%)</b></td><td>0.02 <b>(-71.45%)</b></td><td>293.70 <b>(-71.13%)</b></td><td>272.74 <b>(-53.55%)</b></td><td>278.00 <b>(-53.22%)</b></td><td>252.20 (-17.01%)</td><td>18.41 <b>(-93.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>1017.30 (n/a)</td><td>587.22 (n/a)</td><td>594.30 (n/a)</td><td>303.90 (n/a)</td><td>271.72 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.29 (+14.45%)</td><td>0.26 <b>(+39.37%)</b></td><td>0.27 <b>(+27.70%)</b></td><td>0.20 <b>(+87.23%)</b></td><td>0.04 <b>(-47.50%)</b></td><td>369.70 <b>(-46.59%)</b></td><td>287.18 <b>(-35.78%)</b></td><td>270.90 <b>(-21.68%)</b></td><td>250.80 (-12.64%)</td><td>47.07 <b>(-74.77%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>692.20 (n/a)</td><td>447.20 (n/a)</td><td>345.90 (n/a)</td><td>287.10 (n/a)</td><td>186.60 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.55 <b>(+25.67%)</b></td><td>0.32 (-8.99%)</td><td>0.24 <b>(-39.10%)</b></td><td>0.20 (-6.62%)</td><td>0.15 <b>(+57.83%)</b></td><td>643.70 (+7.09%)</td><td>471.76 (+18.29%)</td><td>537.80 <b>(+64.21%)</b></td><td>236.90 <b>(-20.45%)</b></td><td>175.24 <b>(+37.00%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.40 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>601.10 (n/a)</td><td>398.80 (n/a)</td><td>327.50 (n/a)</td><td>297.80 (n/a)</td><td>127.92 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.54 (+8.14%)</td><td>0.29 (-14.93%)</td><td>0.19 <b>(-34.18%)</b></td><td>0.14 <b>(-46.08%)</b></td><td>0.17 <b>(+65.31%)</b></td><td>964.20 <b>(+85.42%)</b></td><td>581.52 <b>(+42.13%)</b></td><td>680.70 <b>(+51.94%)</b></td><td>241.40 (-7.51%)</td><td>292.87 <b>(+174.58%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.50 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.10 (n/a)</td><td>520.00 (n/a)</td><td>409.14 (n/a)</td><td>448.00 (n/a)</td><td>261.00 (n/a)</td><td>106.66 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.40 (-16.30%)</td><td>0.31 (-4.54%)</td><td>0.28 (+0.29%)</td><td>0.24 <b>(+31.06%)</b></td><td>0.08 <b>(-36.21%)</b></td><td>557.70 <b>(-23.71%)</b></td><td>449.26 (-2.66%)</td><td>470.70 (-0.30%)</td><td>326.40 (+19.47%)</td><td>109.55 <b>(-40.03%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.48 (n/a)</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>731.00 (n/a)</td><td>461.52 (n/a)</td><td>472.10 (n/a)</td><td>273.20 (n/a)</td><td>182.67 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (-7.27%)</td><td>0.01 (-9.83%)</td><td>0.01 (-6.92%)</td><td>0.01 (-18.33%)</td><td>0.00 <b>(+43.49%)</b></td><td>362.50 <b>(+22.42%)</b></td><td>304.30 (+11.60%)</td><td>297.40 (+7.44%)</td><td>267.50 (+7.82%)</td><td>35.21 <b>(+94.46%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>296.10 (n/a)</td><td>272.68 (n/a)</td><td>276.80 (n/a)</td><td>248.10 (n/a)</td><td>18.11 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (-6.36%)</td><td>0.01 (-6.73%)</td><td>0.02 (-8.14%)</td><td>0.01 (-7.84%)</td><td>0.00 (-8.69%)</td><td>526.10 (+8.50%)</td><td>318.44 (+7.15%)</td><td>270.50 (+8.90%)</td><td>228.50 (+6.78%)</td><td>118.65 (+8.58%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>484.90 (n/a)</td><td>297.18 (n/a)</td><td>248.40 (n/a)</td><td>214.00 (n/a)</td><td>109.27 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.01 <b>(-29.33%)</b></td><td>0.01 <b>(-52.43%)</b></td><td>0.00 <b>(-67.76%)</b></td><td>0.00 <b>(-76.68%)</b></td><td>0.00 <b>(+47.44%)</b></td><td>1992.30 <b>(+328.82%)</b></td><td>957.98 <b>(+204.43%)</b></td><td>843.60 <b>(+210.15%)</b></td><td>358.70 <b>(+41.50%)</b></td><td>678.72 <b>(+682.53%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>464.60 (n/a)</td><td>314.68 (n/a)</td><td>272.00 (n/a)</td><td>253.50 (n/a)</td><td>86.73 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.53 (+3.16%)</td><td>0.41 (+4.81%)</td><td>0.46 <b>(+23.28%)</b></td><td>0.27 (-1.84%)</td><td>0.10 (+3.64%)</td><td>483.50 (+1.88%)</td><td>341.00 (-4.11%)</td><td>289.30 (-18.87%)</td><td>249.30 (-3.07%)</td><td>96.65 (+5.84%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>474.60 (n/a)</td><td>355.60 (n/a)</td><td>356.60 (n/a)</td><td>257.20 (n/a)</td><td>91.31 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.56 (-8.69%)</td><td>0.44 (+3.35%)</td><td>0.42 (+6.91%)</td><td>0.31 (+5.11%)</td><td>0.11 (-11.90%)</td><td>427.00 (-4.86%)</td><td>318.58 (-4.71%)</td><td>317.00 (-6.46%)</td><td>237.10 (+9.52%)</td><td>83.70 (-12.29%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.61 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.29 (n/a)</td><td>0.13 (n/a)</td><td>448.80 (n/a)</td><td>334.32 (n/a)</td><td>338.90 (n/a)</td><td>216.50 (n/a)</td><td>95.42 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.50 (+11.89%)</td><td>0.36 (+19.44%)</td><td>0.33 (+10.12%)</td><td>0.26 <b>(+24.47%)</b></td><td>0.11 (+16.66%)</td><td>513.70 (-19.66%)</td><td>388.76 (-16.24%)</td><td>405.10 (-9.19%)</td><td>263.70 (-10.61%)</td><td>106.98 (-15.77%)</td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.45 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>639.40 (n/a)</td><td>464.14 (n/a)</td><td>446.10 (n/a)</td><td>295.00 (n/a)</td><td>127.01 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.55 (-7.37%)</td><td>0.44 (+1.89%)</td><td>0.47 (+16.71%)</td><td>0.26 <b>(-24.36%)</b></td><td>0.11 (+11.23%)</td><td>516.80 <b>(+32.21%)</b></td><td>321.16 (+1.52%)</td><td>279.70 (-14.31%)</td><td>238.90 (+7.95%)</td><td>111.45 <b>(+73.69%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.60 (n/a)</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>390.90 (n/a)</td><td>316.34 (n/a)</td><td>326.40 (n/a)</td><td>221.30 (n/a)</td><td>64.17 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.67 (+14.13%)</td><td>0.42 (-5.88%)</td><td>0.33 <b>(-28.32%)</b></td><td>0.26 (-18.00%)</td><td>0.17 <b>(+59.93%)</b></td><td>517.10 <b>(+21.96%)</b></td><td>352.84 (+14.14%)</td><td>396.70 <b>(+39.49%)</b></td><td>197.70 (-12.37%)</td><td>127.61 <b>(+64.23%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.59 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.31 (n/a)</td><td>0.11 (n/a)</td><td>424.00 (n/a)</td><td>309.12 (n/a)</td><td>284.40 (n/a)</td><td>225.60 (n/a)</td><td>77.70 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.01 <b>(-25.18%)</b></td><td>0.01 <b>(-42.14%)</b></td><td>0.01 <b>(-46.89%)</b></td><td>0.01 <b>(-46.48%)</b></td><td>0.00 <b>(+20.10%)</b></td><td>587.50 <b>(+86.80%)</b></td><td>466.18 <b>(+79.52%)</b></td><td>470.40 <b>(+88.31%)</b></td><td>297.80 <b>(+33.66%)</b></td><td>109.51 <b>(+190.32%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>314.50 (n/a)</td><td>259.68 (n/a)</td><td>249.80 (n/a)</td><td>222.80 (n/a)</td><td>37.72 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.02 (+3.10%)</td><td>0.01 (-7.40%)</td><td>0.01 (-3.59%)</td><td>0.01 <b>(-36.45%)</b></td><td>0.00 <b>(+79.93%)</b></td><td>514.70 <b>(+57.35%)</b></td><td>311.78 (+16.00%)</td><td>276.40 (+3.71%)</td><td>216.80 (-3.00%)</td><td>118.81 <b>(+187.40%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>327.10 (n/a)</td><td>268.78 (n/a)</td><td>266.50 (n/a)</td><td>223.50 (n/a)</td><td>41.34 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-29.17%)</b></td><td>0.00 <b>(-50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-19.89%)</td><td>20137.04 (-10.12%)</td><td>14147.93 (+18.17%)</td><td>13987.56 <b>(+114.15%)</b></td><td>5610.25 (-6.86%)</td><td>5410.42 <b>(-31.92%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22405.15 (n/a)</td><td>11972.99 (n/a)</td><td>6531.78 (n/a)</td><td>6023.47 (n/a)</td><td>7946.79 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+28.95%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(+25.00%)</b></td><td>0.00 <b>(-28.04%)</b></td><td>15876.32 <b>(-28.09%)</b></td><td>9131.71 <b>(-33.82%)</b></td><td>7840.45 <b>(-51.65%)</b></td><td>6263.10 (-3.59%)</td><td>3836.85 <b>(-43.05%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22076.53 (n/a)</td><td>13799.19 (n/a)</td><td>16215.12 (n/a)</td><td>6496.14 (n/a)</td><td>6737.55 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29467.27 (n/a)</td><td>23285.89 (n/a)</td><td>25225.82 (n/a)</td><td>16577.63 (n/a)</td><td>5834.92 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28670.00 (n/a)</td><td>24407.66 (n/a)</td><td>26158.32 (n/a)</td><td>15164.87 (n/a)</td><td>5399.22 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.52 (-13.65%)</td><td>1.08 <b>(-26.55%)</b></td><td>0.99 <b>(-36.38%)</b></td><td>0.66 <b>(-28.39%)</b></td><td>0.37 (+15.82%)</td><td>791.30 <b>(+39.66%)</b></td><td>537.30 <b>(+42.81%)</b></td><td>531.70 <b>(+57.17%)</b></td><td>345.80 (+15.81%)</td><td>187.61 <b>(+72.55%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.76 (n/a)</td><td>1.47 (n/a)</td><td>1.55 (n/a)</td><td>0.93 (n/a)</td><td>0.32 (n/a)</td><td>566.60 (n/a)</td><td>376.24 (n/a)</td><td>338.30 (n/a)</td><td>298.60 (n/a)</td><td>108.73 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>2.59 <b>(+49.40%)</b></td><td>2.09 <b>(+51.40%)</b></td><td>2.24 <b>(+44.86%)</b></td><td>1.09 <b>(+162.57%)</b></td><td>0.59 (+6.89%)</td><td>959.60 <b>(-61.92%)</b></td><td>553.40 <b>(-45.99%)</b></td><td>467.70 <b>(-30.97%)</b></td><td>404.30 <b>(-33.06%)</b></td><td>230.14 <b>(-72.51%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.74 (n/a)</td><td>1.38 (n/a)</td><td>1.55 (n/a)</td><td>0.42 (n/a)</td><td>0.55 (n/a)</td><td>2519.70 (n/a)</td><td>1024.60 (n/a)</td><td>677.50 (n/a)</td><td>604.00 (n/a)</td><td>837.14 (n/a)</td>
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
<td><code>9938c0a</code> — 2026-09-18 23:01:17</td><td>1.98 (+1.52%)</td><td>1.35 <b>(-22.32%)</b></td><td>1.13 <b>(-32.00%)</b></td><td>0.83 <b>(-48.00%)</b></td><td>0.52 <b>(+236.55%)</b></td><td>635.30 <b>(+92.28%)</b></td><td>434.70 <b>(+43.58%)</b></td><td>463.70 <b>(+47.07%)</b></td><td>264.20 (-1.49%)</td><td>157.78 <b>(+509.66%)</b></td>
</tr>
<tr>
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.95 (n/a)</td><td>1.74 (n/a)</td><td>1.66 (n/a)</td><td>1.59 (n/a)</td><td>0.15 (n/a)</td><td>330.40 (n/a)</td><td>302.76 (n/a)</td><td>315.30 (n/a)</td><td>268.20 (n/a)</td><td>25.88 (n/a)</td>
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
