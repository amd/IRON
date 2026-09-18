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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (+16.68%)</td><td>0.04 (+0.11%)</td><td>0.03 (-7.39%)</td><td>0.02 (-11.82%)</td><td>0.01 <b>(+45.41%)</b></td><td>542.70 (+13.39%)</td><td>371.84 (+3.40%)</td><td>351.20 (+7.96%)</td><td>251.80 (-14.30%)</td><td>112.53 <b>(+43.73%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>478.60 (n/a)</td><td>359.60 (n/a)</td><td>325.30 (n/a)</td><td>293.80 (n/a)</td><td>78.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (+5.53%)</td><td>0.04 (+10.79%)</td><td>0.04 <b>(+40.82%)</b></td><td>0.02 (+5.92%)</td><td>0.01 (-13.23%)</td><td>508.00 (-5.58%)</td><td>343.16 (-12.14%)</td><td>305.80 <b>(-28.98%)</b></td><td>233.40 (-5.24%)</td><td>103.45 (-17.65%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.00 (n/a)</td><td>390.56 (n/a)</td><td>430.60 (n/a)</td><td>246.30 (n/a)</td><td>125.62 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (+18.31%)</td><td>0.03 (-6.59%)</td><td>0.03 (-10.06%)</td><td>0.02 (-0.91%)</td><td>0.01 <b>(+35.56%)</b></td><td>617.10 (+0.92%)</td><td>425.34 (+10.40%)</td><td>407.60 (+11.18%)</td><td>229.30 (-15.48%)</td><td>143.22 (+7.32%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>611.50 (n/a)</td><td>385.28 (n/a)</td><td>366.60 (n/a)</td><td>271.30 (n/a)</td><td>133.45 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 <b>(-22.30%)</b></td><td>0.01 <b>(-30.89%)</b></td><td>0.01 <b>(-32.08%)</b></td><td>0.01 <b>(-28.37%)</b></td><td>0.01 <b>(-23.39%)</b></td><td>593.10 <b>(+39.59%)</b></td><td>387.84 <b>(+45.56%)</b></td><td>385.40 <b>(+47.21%)</b></td><td>241.50 <b>(+28.66%)</b></td><td>135.86 <b>(+40.60%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>424.90 (n/a)</td><td>266.44 (n/a)</td><td>261.80 (n/a)</td><td>187.70 (n/a)</td><td>96.63 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 <b>(-36.88%)</b></td><td>0.01 <b>(-26.52%)</b></td><td>0.01 (-6.30%)</td><td>0.01 (+6.11%)</td><td>0.00 <b>(-59.93%)</b></td><td>516.70 (-5.76%)</td><td>412.36 (+18.27%)</td><td>425.80 (+6.72%)</td><td>267.60 <b>(+58.44%)</b></td><td>92.31 <b>(-40.66%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.30 (n/a)</td><td>348.66 (n/a)</td><td>399.00 (n/a)</td><td>168.90 (n/a)</td><td>155.56 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.01 <b>(-45.03%)</b></td><td>0.01 <b>(-40.63%)</b></td><td>0.01 (-14.09%)</td><td>0.00 <b>(-68.99%)</b></td><td>0.00 <b>(-47.97%)</b></td><td>1895.70 <b>(+222.51%)</b></td><td>725.84 <b>(+97.88%)</b></td><td>442.40 (+16.42%)</td><td>354.60 <b>(+81.94%)</b></td><td>656.06 <b>(+279.20%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.80 (n/a)</td><td>366.80 (n/a)</td><td>380.00 (n/a)</td><td>194.90 (n/a)</td><td>173.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (+3.05%)</td><td>0.01 (-13.47%)</td><td>0.01 <b>(-34.89%)</b></td><td>0.01 (+9.93%)</td><td>0.01 (-9.27%)</td><td>525.50 (-9.04%)</td><td>402.04 (+11.98%)</td><td>443.20 <b>(+53.62%)</b></td><td>222.90 (-2.96%)</td><td>129.53 (-16.38%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.70 (n/a)</td><td>359.02 (n/a)</td><td>288.50 (n/a)</td><td>229.70 (n/a)</td><td>154.89 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.01 <b>(-37.18%)</b></td><td>0.01 <b>(-30.68%)</b></td><td>0.01 (-17.83%)</td><td>0.00 <b>(-59.27%)</b></td><td>0.00 <b>(-20.47%)</b></td><td>1111.10 <b>(+145.49%)</b></td><td>601.56 <b>(+56.75%)</b></td><td>496.40 <b>(+21.70%)</b></td><td>380.70 <b>(+59.16%)</b></td><td>292.96 <b>(+250.82%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>452.60 (n/a)</td><td>383.78 (n/a)</td><td>407.90 (n/a)</td><td>239.20 (n/a)</td><td>83.51 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.01 <b>(-32.55%)</b></td><td>0.01 <b>(-27.61%)</b></td><td>0.01 <b>(-27.07%)</b></td><td>0.00 <b>(-71.55%)</b></td><td>0.00 (+4.77%)</td><td>1897.50 <b>(+251.52%)</b></td><td>779.14 <b>(+82.73%)</b></td><td>596.30 <b>(+37.11%)</b></td><td>365.70 <b>(+48.24%)</b></td><td>639.27 <b>(+477.54%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.80 (n/a)</td><td>426.40 (n/a)</td><td>434.90 (n/a)</td><td>246.70 (n/a)</td><td>110.69 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>348.30 (n/a)</td><td>271.92 (n/a)</td><td>250.60 (n/a)</td><td>242.70 (n/a)</td><td>44.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>576.10 (n/a)</td><td>356.06 (n/a)</td><td>259.50 (n/a)</td><td>233.40 (n/a)</td><td>157.02 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>420.80 (n/a)</td><td>333.86 (n/a)</td><td>342.80 (n/a)</td><td>249.20 (n/a)</td><td>81.53 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.00 (n/a)</td><td>440.54 (n/a)</td><td>487.00 (n/a)</td><td>295.10 (n/a)</td><td>100.95 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>632.90 (n/a)</td><td>478.94 (n/a)</td><td>515.20 (n/a)</td><td>269.10 (n/a)</td><td>133.19 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.90 (n/a)</td><td>397.30 (n/a)</td><td>446.30 (n/a)</td><td>238.20 (n/a)</td><td>120.84 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.74 <b>(-25.77%)</b></td><td>0.65 (-12.62%)</td><td>0.65 (-5.77%)</td><td>0.54 (-10.99%)</td><td>0.07 <b>(-53.40%)</b></td><td>845.80 (+12.34%)</td><td>716.38 (+12.33%)</td><td>705.10 (+6.13%)</td><td>619.10 <b>(+34.70%)</b></td><td>81.84 <b>(-26.04%)</b></td><td>54.20 <b>(-25.77%)</b></td><td>47.31 (-12.62%)</td><td>47.59 (-5.77%)</td><td>39.67 (-10.99%)</td><td>5.17 <b>(-53.40%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.00 (n/a)</td><td>0.74 (n/a)</td><td>0.69 (n/a)</td><td>0.61 (n/a)</td><td>0.15 (n/a)</td><td>752.90 (n/a)</td><td>637.74 (n/a)</td><td>664.40 (n/a)</td><td>459.60 (n/a)</td><td>110.66 (n/a)</td><td>73.01 (n/a)</td><td>54.14 (n/a)</td><td>50.51 (n/a)</td><td>44.57 (n/a)</td><td>11.10 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.52 (+15.49%)</td><td>1.12 <b>(+40.30%)</b></td><td>1.09 <b>(+24.12%)</b></td><td>0.80 <b>(+324.21%)</b></td><td>0.30 <b>(-27.51%)</b></td><td>817.70 <b>(-76.43%)</b></td><td>621.36 <b>(-51.43%)</b></td><td>602.70 (-19.44%)</td><td>432.40 (-13.42%)</td><td>162.38 <b>(-86.86%)</b></td><td>155.20 (+15.49%)</td><td>114.28 <b>(+40.30%)</b></td><td>111.35 <b>(+24.12%)</b></td><td>82.07 <b>(+324.21%)</b></td><td>30.45 <b>(-27.51%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.31 (n/a)</td><td>0.80 (n/a)</td><td>0.88 (n/a)</td><td>0.19 (n/a)</td><td>0.41 (n/a)</td><td>3468.60 (n/a)</td><td>1279.22 (n/a)</td><td>748.10 (n/a)</td><td>499.40 (n/a)</td><td>1235.34 (n/a)</td><td>134.39 (n/a)</td><td>81.45 (n/a)</td><td>89.71 (n/a)</td><td>19.35 (n/a)</td><td>42.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.34 (-1.00%)</td><td>0.99 (+2.43%)</td><td>1.00 (-11.00%)</td><td>0.56 <b>(+166.87%)</b></td><td>0.35 <b>(-22.01%)</b></td><td>1337.40 <b>(-62.53%)</b></td><td>848.48 <b>(-31.60%)</b></td><td>751.70 (+12.36%)</td><td>562.90 (+1.00%)</td><td>331.34 <b>(-74.59%)</b></td><td>149.02 (-1.00%)</td><td>110.62 (+2.43%)</td><td>111.60 (-11.00%)</td><td>62.72 <b>(+166.87%)</b></td><td>38.62 <b>(-22.01%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.35 (n/a)</td><td>0.97 (n/a)</td><td>1.13 (n/a)</td><td>0.21 (n/a)</td><td>0.44 (n/a)</td><td>3569.20 (n/a)</td><td>1240.50 (n/a)</td><td>669.00 (n/a)</td><td>557.30 (n/a)</td><td>1304.00 (n/a)</td><td>150.52 (n/a)</td><td>108.00 (n/a)</td><td>125.40 (n/a)</td><td>23.50 (n/a)</td><td>49.52 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.62 (-6.61%)</td><td>0.96 <b>(-26.13%)</b></td><td>0.98 <b>(-20.43%)</b></td><td>0.49 <b>(-52.88%)</b></td><td>0.47 <b>(+78.91%)</b></td><td>2141.50 <b>(+112.24%)</b></td><td>1341.10 <b>(+60.98%)</b></td><td>1064.60 <b>(+25.69%)</b></td><td>648.00 (+7.07%)</td><td>658.76 <b>(+352.45%)</b></td><td>207.11 (-6.61%)</td><td>122.40 <b>(-26.13%)</b></td><td>126.08 <b>(-20.43%)</b></td><td>62.68 <b>(-52.88%)</b></td><td>59.54 <b>(+78.91%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.73 (n/a)</td><td>1.29 (n/a)</td><td>1.24 (n/a)</td><td>1.04 (n/a)</td><td>0.26 (n/a)</td><td>1009.00 (n/a)</td><td>833.08 (n/a)</td><td>847.00 (n/a)</td><td>605.20 (n/a)</td><td>145.60 (n/a)</td><td>221.77 (n/a)</td><td>165.70 (n/a)</td><td>158.46 (n/a)</td><td>133.02 (n/a)</td><td>33.28 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>2.16 (-8.76%)</td><td>1.64 (+6.83%)</td><td>1.60 (+16.58%)</td><td>1.30 <b>(+37.09%)</b></td><td>0.35 <b>(-32.71%)</b></td><td>804.10 <b>(-27.06%)</b></td><td>663.72 (-11.16%)</td><td>654.40 (-14.22%)</td><td>486.20 (+9.60%)</td><td>135.07 <b>(-43.86%)</b></td><td>276.04 (-8.76%)</td><td>209.50 (+6.83%)</td><td>205.09 (+16.58%)</td><td>166.92 <b>(+37.09%)</b></td><td>45.25 <b>(-32.71%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>2.36 (n/a)</td><td>1.53 (n/a)</td><td>1.37 (n/a)</td><td>0.95 (n/a)</td><td>0.53 (n/a)</td><td>1102.40 (n/a)</td><td>747.10 (n/a)</td><td>762.90 (n/a)</td><td>443.60 (n/a)</td><td>240.58 (n/a)</td><td>302.55 (n/a)</td><td>196.10 (n/a)</td><td>175.93 (n/a)</td><td>121.76 (n/a)</td><td>67.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>2.37 (+5.29%)</td><td>1.33 (-9.37%)</td><td>1.29 (-0.48%)</td><td>0.32 (+9.10%)</td><td>0.75 (-5.68%)</td><td>3228.20 (-8.34%)</td><td>1229.44 (+1.04%)</td><td>810.30 (+0.48%)</td><td>443.20 (-5.04%)</td><td>1137.38 (-12.46%)</td><td>302.81 (+5.29%)</td><td>169.95 (-9.37%)</td><td>165.64 (-0.48%)</td><td>41.58 (+9.10%)</td><td>96.31 (-5.68%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>2.25 (n/a)</td><td>1.47 (n/a)</td><td>1.30 (n/a)</td><td>0.30 (n/a)</td><td>0.80 (n/a)</td><td>3521.80 (n/a)</td><td>1216.78 (n/a)</td><td>806.40 (n/a)</td><td>466.70 (n/a)</td><td>1299.33 (n/a)</td><td>287.61 (n/a)</td><td>187.52 (n/a)</td><td>166.44 (n/a)</td><td>38.11 (n/a)</td><td>102.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.92 <b>(+30.98%)</b></td><td>1.18 (+3.11%)</td><td>1.23 (+0.67%)</td><td>0.47 (-2.61%)</td><td>0.59 <b>(+48.35%)</b></td><td>2217.00 (+2.69%)</td><td>1143.06 (+5.80%)</td><td>854.50 (-0.66%)</td><td>545.20 <b>(-23.65%)</b></td><td>685.83 (+12.48%)</td><td>246.17 <b>(+30.98%)</b></td><td>151.07 (+3.11%)</td><td>157.07 (+0.67%)</td><td>60.54 (-2.61%)</td><td>75.06 <b>(+48.35%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.47 (n/a)</td><td>1.14 (n/a)</td><td>1.22 (n/a)</td><td>0.49 (n/a)</td><td>0.40 (n/a)</td><td>2159.00 (n/a)</td><td>1080.38 (n/a)</td><td>860.20 (n/a)</td><td>714.10 (n/a)</td><td>609.73 (n/a)</td><td>187.95 (n/a)</td><td>146.51 (n/a)</td><td>156.02 (n/a)</td><td>62.17 (n/a)</td><td>50.60 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.98 <b>(+53.09%)</b></td><td>0.62 (+10.86%)</td><td>0.55 (-3.56%)</td><td>0.34 <b>(-27.30%)</b></td><td>0.25 <b>(+282.07%)</b></td><td>1051.90 <b>(+37.56%)</b></td><td>663.40 (+1.70%)</td><td>654.30 (+3.69%)</td><td>366.00 <b>(-34.68%)</b></td><td>265.40 <b>(+237.38%)</b></td><td>45.84 <b>(+53.09%)</b></td><td>28.84 (+10.86%)</td><td>25.64 (-3.56%)</td><td>15.95 <b>(-27.30%)</b></td><td>11.69 <b>(+282.07%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.64 (n/a)</td><td>0.56 (n/a)</td><td>0.57 (n/a)</td><td>0.47 (n/a)</td><td>0.07 (n/a)</td><td>764.70 (n/a)</td><td>652.32 (n/a)</td><td>631.00 (n/a)</td><td>560.30 (n/a)</td><td>78.66 (n/a)</td><td>29.94 (n/a)</td><td>26.01 (n/a)</td><td>26.59 (n/a)</td><td>21.94 (n/a)</td><td>3.06 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>4.08 (+13.65%)</td><td>3.02 (+4.71%)</td><td>3.72 (+11.67%)</td><td>1.70 (+4.90%)</td><td>1.16 <b>(+33.91%)</b></td><td>1541.20 (-4.67%)</td><td>1004.30 (+0.66%)</td><td>703.90 (-10.46%)</td><td>641.90 (-12.01%)</td><td>447.88 (+17.54%)</td><td>836.40 (+13.65%)</td><td>619.43 (+4.71%)</td><td>762.67 (+11.67%)</td><td>348.35 (+4.90%)</td><td>238.56 <b>(+33.91%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>3.59 (n/a)</td><td>2.89 (n/a)</td><td>3.33 (n/a)</td><td>1.62 (n/a)</td><td>0.87 (n/a)</td><td>1616.70 (n/a)</td><td>997.68 (n/a)</td><td>786.10 (n/a)</td><td>729.50 (n/a)</td><td>381.06 (n/a)</td><td>735.94 (n/a)</td><td>591.57 (n/a)</td><td>682.98 (n/a)</td><td>332.08 (n/a)</td><td>178.14 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>612.90 (n/a)</td><td>374.28 (n/a)</td><td>256.40 (n/a)</td><td>218.00 (n/a)</td><td>186.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>586.80 (n/a)</td><td>512.72 (n/a)</td><td>567.50 (n/a)</td><td>404.80 (n/a)</td><td>92.89 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1097.10 (n/a)</td><td>488.54 (n/a)</td><td>271.40 (n/a)</td><td>214.50 (n/a)</td><td>372.61 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>571.40 (n/a)</td><td>390.96 (n/a)</td><td>423.60 (n/a)</td><td>228.30 (n/a)</td><td>153.38 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.10 (n/a)</td><td>378.48 (n/a)</td><td>307.10 (n/a)</td><td>254.70 (n/a)</td><td>148.54 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.40 (n/a)</td><td>444.22 (n/a)</td><td>384.90 (n/a)</td><td>234.90 (n/a)</td><td>186.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.65 <b>(+23.06%)</b></td><td>0.45 (+3.04%)</td><td>0.44 (-7.83%)</td><td>0.28 (-14.07%)</td><td>0.14 <b>(+38.41%)</b></td><td>797.00 (+16.38%)</td><td>537.46 (+0.31%)</td><td>507.80 (+8.48%)</td><td>342.10 (-18.76%)</td><td>172.81 <b>(+29.23%)</b></td><td>27.58 <b>(+23.06%)</b></td><td>19.03 (+3.04%)</td><td>18.58 (-7.83%)</td><td>11.84 (-14.07%)</td><td>5.94 <b>(+38.41%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.10 (n/a)</td><td>684.80 (n/a)</td><td>535.82 (n/a)</td><td>468.10 (n/a)</td><td>421.10 (n/a)</td><td>133.72 (n/a)</td><td>22.41 (n/a)</td><td>18.47 (n/a)</td><td>20.16 (n/a)</td><td>13.78 (n/a)</td><td>4.29 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.57 (+0.02%)</td><td>0.43 <b>(+30.88%)</b></td><td>0.42 <b>(+22.72%)</b></td><td>0.35 <b>(+199.86%)</b></td><td>0.09 <b>(-42.99%)</b></td><td>640.30 <b>(-66.65%)</b></td><td>527.40 <b>(-39.72%)</b></td><td>526.60 (-18.51%)</td><td>391.30 (+0.00%)</td><td>107.17 <b>(-82.22%)</b></td><td>24.12 (+0.02%)</td><td>18.53 <b>(+30.88%)</b></td><td>17.92 <b>(+22.72%)</b></td><td>14.74 <b>(+199.86%)</b></td><td>3.96 <b>(-42.99%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.57 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.12 (n/a)</td><td>0.16 (n/a)</td><td>1919.90 (n/a)</td><td>874.92 (n/a)</td><td>646.20 (n/a)</td><td>391.30 (n/a)</td><td>602.72 (n/a)</td><td>24.12 (n/a)</td><td>14.16 (n/a)</td><td>14.60 (n/a)</td><td>4.92 (n/a)</td><td>6.94 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.31 (+0.45%)</td><td>0.30 (+0.34%)</td><td>0.30 (+0.08%)</td><td>0.30 (+2.67%)</td><td>0.00 <b>(-41.69%)</b></td><td>83858.60 (-2.60%)</td><td>82780.98 (-0.37%)</td><td>82941.30 (-0.08%)</td><td>81113.10 (-0.44%)</td><td>1065.68 <b>(-43.47%)</b></td><td>211.80 (+0.45%)</td><td>207.56 (+0.34%)</td><td>207.13 (+0.08%)</td><td>204.87 (+2.67%)</td><td>2.69 <b>(-41.69%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>86093.60 (n/a)</td><td>83085.62 (n/a)</td><td>83004.80 (n/a)</td><td>81475.40 (n/a)</td><td>1885.13 (n/a)</td><td>210.86 (n/a)</td><td>206.86 (n/a)</td><td>206.97 (n/a)</td><td>199.55 (n/a)</td><td>4.62 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.15 (-0.20%)</td><td>1.12 (+1.59%)</td><td>1.15 (+0.21%)</td><td>1.08 (+11.92%)</td><td>0.03 <b>(-60.15%)</b></td><td>23364.70 (-10.65%)</td><td>22403.24 (-1.96%)</td><td>21961.10 (-0.21%)</td><td>21942.30 (+0.20%)</td><td>653.04 <b>(-64.66%)</b></td><td>782.96 (-0.20%)</td><td>767.36 (+1.59%)</td><td>782.29 (+0.21%)</td><td>735.29 (+11.92%)</td><td>21.99 <b>(-60.15%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.15 (n/a)</td><td>1.11 (n/a)</td><td>1.14 (n/a)</td><td>0.96 (n/a)</td><td>0.08 (n/a)</td><td>26149.80 (n/a)</td><td>22851.20 (n/a)</td><td>22007.00 (n/a)</td><td>21899.20 (n/a)</td><td>1848.09 (n/a)</td><td>784.50 (n/a)</td><td>755.38 (n/a)</td><td>780.65 (n/a)</td><td>656.98 (n/a)</td><td>55.18 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>3.97 (-0.35%)</td><td>3.05 (+10.64%)</td><td>3.38 <b>(+55.38%)</b></td><td>1.86 (-8.09%)</td><td>1.02 (+11.54%)</td><td>4335.00 (+8.79%)</td><td>2936.48 (-7.42%)</td><td>2381.80 <b>(-35.64%)</b></td><td>2031.30 (+0.35%)</td><td>1095.01 (+18.33%)</td><td>1040.67 (-0.35%)</td><td>798.83 (+10.64%)</td><td>887.54 <b>(+55.38%)</b></td><td>487.64 (-8.09%)</td><td>266.67 (+11.54%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>3.98 (n/a)</td><td>2.75 (n/a)</td><td>2.18 (n/a)</td><td>2.02 (n/a)</td><td>0.91 (n/a)</td><td>3984.60 (n/a)</td><td>3171.70 (n/a)</td><td>3700.90 (n/a)</td><td>2024.20 (n/a)</td><td>925.39 (n/a)</td><td>1044.34 (n/a)</td><td>722.04 (n/a)</td><td>571.20 (n/a)</td><td>530.53 (n/a)</td><td>239.09 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.27 (+11.91%)</td><td>0.21 (-9.81%)</td><td>0.20 (-14.36%)</td><td>0.18 (-19.36%)</td><td>0.04 <b>(+265.67%)</b></td><td>7046.30 <b>(+24.01%)</b></td><td>6125.32 (+13.45%)</td><td>6242.80 (+16.77%)</td><td>4546.10 (-10.64%)</td><td>1000.02 <b>(+299.23%)</b></td><td>14.76 (+11.91%)</td><td>11.23 (-9.81%)</td><td>10.75 (-14.36%)</td><td>9.52 (-19.36%)</td><td>2.11 <b>(+265.67%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.01 (n/a)</td><td>5682.00 (n/a)</td><td>5399.10 (n/a)</td><td>5346.30 (n/a)</td><td>5087.30 (n/a)</td><td>250.49 (n/a)</td><td>13.19 (n/a)</td><td>12.45 (n/a)</td><td>12.55 (n/a)</td><td>11.81 (n/a)</td><td>0.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>3.90 (n/a)</td><td>3.58 (n/a)</td><td>3.77 (n/a)</td><td>3.01 (n/a)</td><td>0.37 (n/a)</td><td>3.90 (n/a)</td><td>3.58 (n/a)</td><td>3.76 (n/a)</td><td>3.00 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>7.60 (+0.95%)</td><td>6.71 (-6.79%)</td><td>6.92 (-7.22%)</td><td>5.54 (-15.69%)</td><td>0.79 <b>(+81.92%)</b></td><td>7.59 (+0.95%)</td><td>6.71 (-6.79%)</td><td>6.91 (-7.22%)</td><td>5.53 (-15.69%)</td><td>0.79 <b>(+81.92%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>7.52 (n/a)</td><td>7.20 (n/a)</td><td>7.45 (n/a)</td><td>6.57 (n/a)</td><td>0.43 (n/a)</td><td>7.52 (n/a)</td><td>7.20 (n/a)</td><td>7.45 (n/a)</td><td>6.56 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>14.09 (+5.64%)</td><td>9.89 (-6.51%)</td><td>9.50 (-17.07%)</td><td>7.63 (-7.12%)</td><td>2.49 (+9.23%)</td><td>14.08 (+5.64%)</td><td>9.88 (-6.51%)</td><td>9.50 (-17.07%)</td><td>7.62 (-7.12%)</td><td>2.49 (+9.23%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>13.33 (n/a)</td><td>10.58 (n/a)</td><td>11.46 (n/a)</td><td>8.21 (n/a)</td><td>2.28 (n/a)</td><td>13.33 (n/a)</td><td>10.57 (n/a)</td><td>11.45 (n/a)</td><td>8.21 (n/a)</td><td>2.28 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>3.92 (n/a)</td><td>3.60 (n/a)</td><td>3.73 (n/a)</td><td>3.20 (n/a)</td><td>0.34 (n/a)</td><td>3.91 (n/a)</td><td>3.60 (n/a)</td><td>3.72 (n/a)</td><td>3.20 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>7.30 (+9.85%)</td><td>6.11 (-2.70%)</td><td>5.71 (-11.25%)</td><td>5.59 (-2.27%)</td><td>0.72 <b>(+97.49%)</b></td><td>7.29 (+9.85%)</td><td>6.11 (-2.70%)</td><td>5.70 (-11.25%)</td><td>5.59 (-2.27%)</td><td>0.72 <b>(+97.49%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>6.64 (n/a)</td><td>6.28 (n/a)</td><td>6.43 (n/a)</td><td>5.72 (n/a)</td><td>0.36 (n/a)</td><td>6.64 (n/a)</td><td>6.28 (n/a)</td><td>6.43 (n/a)</td><td>5.72 (n/a)</td><td>0.36 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>12.47 (-5.11%)</td><td>9.37 (-8.15%)</td><td>8.24 (-3.72%)</td><td>8.05 (+0.53%)</td><td>1.91 <b>(-27.58%)</b></td><td>12.46 (-5.11%)</td><td>9.36 (-8.15%)</td><td>8.23 (-3.72%)</td><td>8.05 (+0.53%)</td><td>1.91 <b>(-27.58%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>13.14 (n/a)</td><td>10.20 (n/a)</td><td>8.56 (n/a)</td><td>8.01 (n/a)</td><td>2.63 (n/a)</td><td>13.13 (n/a)</td><td>10.19 (n/a)</td><td>8.55 (n/a)</td><td>8.00 (n/a)</td><td>2.63 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>3.13 (-1.98%)</td><td>2.31 (+12.23%)</td><td>2.76 <b>(+59.82%)</b></td><td>1.20 (+9.09%)</td><td>0.91 (-2.30%)</td><td>3.13 (-1.98%)</td><td>2.31 (+12.23%)</td><td>2.75 <b>(+59.82%)</b></td><td>1.20 (+9.09%)</td><td>0.90 (-2.30%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>3.19 (n/a)</td><td>2.06 (n/a)</td><td>1.73 (n/a)</td><td>1.10 (n/a)</td><td>0.93 (n/a)</td><td>3.19 (n/a)</td><td>2.06 (n/a)</td><td>1.72 (n/a)</td><td>1.10 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.58 (+6.30%)</td><td>0.25 <b>(-34.76%)</b></td><td>0.14 <b>(-69.64%)</b></td><td>0.08 (+0.72%)</td><td>0.21 (+9.12%)</td><td>0.57 (+6.30%)</td><td>0.25 <b>(-34.76%)</b></td><td>0.14 <b>(-69.64%)</b></td><td>0.08 (+0.72%)</td><td>0.21 (+9.12%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.54 (n/a)</td><td>0.39 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.53 (n/a)</td><td>0.38 (n/a)</td><td>0.46 (n/a)</td><td>0.07 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.63 (-7.43%)</td><td>0.47 (+5.41%)</td><td>0.63 (-4.17%)</td><td>0.08 (+6.31%)</td><td>0.24 <b>(-21.21%)</b></td><td>0.62 (-7.43%)</td><td>0.46 (+5.41%)</td><td>0.62 (-4.17%)</td><td>0.08 (+6.31%)</td><td>0.24 <b>(-21.21%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.68 (n/a)</td><td>0.45 (n/a)</td><td>0.65 (n/a)</td><td>0.08 (n/a)</td><td>0.31 (n/a)</td><td>0.67 (n/a)</td><td>0.44 (n/a)</td><td>0.65 (n/a)</td><td>0.08 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>2.34 (-16.85%)</td><td>1.72 <b>(+45.37%)</b></td><td>1.74 <b>(+266.67%)</b></td><td>0.46 (+1.70%)</td><td>0.77 <b>(-27.74%)</b></td><td>2.30 (-16.85%)</td><td>1.69 <b>(+45.37%)</b></td><td>1.72 <b>(+266.67%)</b></td><td>0.45 (+1.70%)</td><td>0.75 <b>(-27.74%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>2.81 (n/a)</td><td>1.18 (n/a)</td><td>0.48 (n/a)</td><td>0.45 (n/a)</td><td>1.06 (n/a)</td><td>2.77 (n/a)</td><td>1.16 (n/a)</td><td>0.47 (n/a)</td><td>0.44 (n/a)</td><td>1.04 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.90 (n/a)</td><td>388.22 (n/a)</td><td>327.00 (n/a)</td><td>296.70 (n/a)</td><td>110.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.60 (n/a)</td><td>370.14 (n/a)</td><td>306.60 (n/a)</td><td>251.90 (n/a)</td><td>136.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2438.80 (n/a)</td><td>1436.22 (n/a)</td><td>1873.50 (n/a)</td><td>376.00 (n/a)</td><td>918.33 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>340.90 (n/a)</td><td>286.12 (n/a)</td><td>288.90 (n/a)</td><td>226.70 (n/a)</td><td>41.82 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1078.30 (n/a)</td><td>589.04 (n/a)</td><td>494.70 (n/a)</td><td>433.20 (n/a)</td><td>275.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1020.00 (n/a)</td><td>655.84 (n/a)</td><td>629.50 (n/a)</td><td>272.60 (n/a)</td><td>352.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (-8.18%)</td><td>0.03 (+3.68%)</td><td>0.03 (+12.79%)</td><td>0.02 <b>(+30.32%)</b></td><td>0.01 <b>(-37.23%)</b></td><td>377.50 <b>(-23.26%)</b></td><td>284.18 (-8.42%)</td><td>257.60 (-11.33%)</td><td>243.00 (+8.87%)</td><td>56.17 <b>(-48.05%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.90 (n/a)</td><td>310.30 (n/a)</td><td>290.50 (n/a)</td><td>223.20 (n/a)</td><td>108.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 <b>(+28.43%)</b></td><td>0.04 <b>(+62.37%)</b></td><td>0.03 <b>(+39.36%)</b></td><td>0.03 <b>(+613.17%)</b></td><td>0.00 <b>(-54.01%)</b></td><td>268.60 <b>(-85.98%)</b></td><td>235.70 <b>(-63.25%)</b></td><td>247.80 <b>(-28.26%)</b></td><td>199.10 <b>(-22.14%)</b></td><td>31.66 <b>(-95.57%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1915.30 (n/a)</td><td>641.36 (n/a)</td><td>345.40 (n/a)</td><td>255.70 (n/a)</td><td>714.20 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (+8.71%)</td><td>0.03 (+9.75%)</td><td>0.03 <b>(+29.17%)</b></td><td>0.01 (-4.45%)</td><td>0.01 (+7.72%)</td><td>618.30 (+4.67%)</td><td>358.66 (-7.22%)</td><td>285.70 <b>(-22.57%)</b></td><td>188.90 (-7.99%)</td><td>179.51 (+5.18%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.70 (n/a)</td><td>386.56 (n/a)</td><td>369.00 (n/a)</td><td>205.30 (n/a)</td><td>170.66 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (-15.01%)</td><td>0.03 <b>(+33.80%)</b></td><td>0.03 <b>(+56.58%)</b></td><td>0.02 <b>(+286.43%)</b></td><td>0.01 <b>(-46.89%)</b></td><td>500.10 <b>(-74.12%)</b></td><td>301.46 <b>(-55.36%)</b></td><td>264.40 <b>(-36.12%)</b></td><td>237.10 (+17.67%)</td><td>111.90 <b>(-84.38%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1932.60 (n/a)</td><td>675.26 (n/a)</td><td>413.90 (n/a)</td><td>201.50 (n/a)</td><td>716.29 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (-11.09%)</td><td>0.02 <b>(-21.33%)</b></td><td>0.02 <b>(-36.16%)</b></td><td>0.01 (-6.37%)</td><td>0.01 (-3.39%)</td><td>585.10 (+6.81%)</td><td>417.60 <b>(+27.20%)</b></td><td>458.10 <b>(+56.67%)</b></td><td>276.80 (+12.47%)</td><td>130.16 (+4.60%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.80 (n/a)</td><td>328.30 (n/a)</td><td>292.40 (n/a)</td><td>246.10 (n/a)</td><td>124.44 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 <b>(+45.31%)</b></td><td>0.02 (+15.37%)</td><td>0.02 <b>(-23.83%)</b></td><td>0.02 <b>(+323.16%)</b></td><td>0.01 (-7.94%)</td><td>456.70 <b>(-76.37%)</b></td><td>360.08 <b>(-43.99%)</b></td><td>400.40 <b>(+31.32%)</b></td><td>204.10 <b>(-31.19%)</b></td><td>103.11 <b>(-85.71%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1932.50 (n/a)</td><td>642.92 (n/a)</td><td>304.90 (n/a)</td><td>296.60 (n/a)</td><td>721.71 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (-6.48%)</td><td>0.02 (-12.43%)</td><td>0.02 (-16.44%)</td><td>0.02 (-10.78%)</td><td>0.01 (-6.33%)</td><td>537.30 (+12.10%)</td><td>372.64 (+14.76%)</td><td>333.70 (+19.65%)</td><td>250.20 (+6.92%)</td><td>120.14 (+14.65%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>479.30 (n/a)</td><td>324.70 (n/a)</td><td>278.90 (n/a)</td><td>234.00 (n/a)</td><td>104.79 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 <b>(+37.51%)</b></td><td>0.02 <b>(+27.25%)</b></td><td>0.02 <b>(+39.65%)</b></td><td>0.01 <b>(+70.07%)</b></td><td>0.01 (+15.83%)</td><td>623.60 <b>(-41.20%)</b></td><td>420.02 <b>(-26.48%)</b></td><td>377.20 <b>(-28.40%)</b></td><td>224.50 <b>(-27.28%)</b></td><td>170.80 <b>(-44.63%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1060.50 (n/a)</td><td>571.30 (n/a)</td><td>526.80 (n/a)</td><td>308.70 (n/a)</td><td>308.46 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (+0.89%)</td><td>0.03 (+6.78%)</td><td>0.03 (+6.64%)</td><td>0.03 <b>(+32.28%)</b></td><td>0.00 <b>(-38.66%)</b></td><td>319.70 <b>(-24.40%)</b></td><td>267.20 (-9.18%)</td><td>261.40 (-6.24%)</td><td>234.20 (-0.89%)</td><td>33.90 <b>(-54.95%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>422.90 (n/a)</td><td>294.22 (n/a)</td><td>278.80 (n/a)</td><td>236.30 (n/a)</td><td>75.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (+8.93%)</td><td>0.02 (+0.62%)</td><td>0.02 <b>(+22.46%)</b></td><td>0.02 (+5.88%)</td><td>0.01 (-15.98%)</td><td>491.80 (-5.57%)</td><td>388.70 (-4.35%)</td><td>393.50 (-18.34%)</td><td>242.10 (-8.19%)</td><td>93.92 <b>(-27.97%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.80 (n/a)</td><td>406.38 (n/a)</td><td>481.90 (n/a)</td><td>263.70 (n/a)</td><td>130.38 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (+14.35%)</td><td>0.02 (-12.32%)</td><td>0.01 <b>(-32.61%)</b></td><td>0.00 <b>(-78.81%)</b></td><td>0.01 <b>(+137.81%)</b></td><td>2474.30 <b>(+372.01%)</b></td><td>827.78 <b>(+111.85%)</b></td><td>563.20 <b>(+48.41%)</b></td><td>236.60 (-12.56%)</td><td>934.53 <b>(+912.12%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.20 (n/a)</td><td>390.74 (n/a)</td><td>379.50 (n/a)</td><td>270.60 (n/a)</td><td>92.33 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (-4.18%)</td><td>0.02 (-4.54%)</td><td>0.02 (+0.18%)</td><td>0.01 (-3.83%)</td><td>0.01 (-2.92%)</td><td>597.90 (+3.98%)</td><td>446.44 (+5.12%)</td><td>412.10 (-0.19%)</td><td>260.40 (+4.37%)</td><td>133.46 (+7.56%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.00 (n/a)</td><td>424.68 (n/a)</td><td>412.90 (n/a)</td><td>249.50 (n/a)</td><td>124.08 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (-9.06%)</td><td>0.02 (-12.19%)</td><td>0.02 <b>(-36.88%)</b></td><td>0.01 (+9.05%)</td><td>0.01 (-12.44%)</td><td>562.70 (-8.31%)</td><td>421.22 (+10.41%)</td><td>463.80 <b>(+58.40%)</b></td><td>248.10 (+9.97%)</td><td>144.47 (-13.22%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.70 (n/a)</td><td>381.50 (n/a)</td><td>292.80 (n/a)</td><td>225.60 (n/a)</td><td>166.47 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (-5.99%)</td><td>0.02 (-0.87%)</td><td>0.02 (-0.10%)</td><td>0.01 <b>(-24.60%)</b></td><td>0.01 <b>(+21.25%)</b></td><td>711.90 <b>(+32.62%)</b></td><td>474.26 (+5.64%)</td><td>476.90 (+0.10%)</td><td>310.90 (+6.40%)</td><td>162.40 <b>(+72.77%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.80 (n/a)</td><td>448.96 (n/a)</td><td>476.40 (n/a)</td><td>292.20 (n/a)</td><td>93.99 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.11 (+11.24%)</td><td>0.08 (+3.45%)</td><td>0.09 (+16.58%)</td><td>0.04 <b>(-25.47%)</b></td><td>0.03 <b>(+48.93%)</b></td><td>675.40 <b>(+34.19%)</b></td><td>377.38 (+6.63%)</td><td>275.30 (-14.24%)</td><td>229.70 (-10.10%)</td><td>187.89 <b>(+80.23%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>503.30 (n/a)</td><td>353.92 (n/a)</td><td>321.00 (n/a)</td><td>255.50 (n/a)</td><td>104.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.16 (+5.66%)</td><td>0.15 <b>(+55.07%)</b></td><td>0.15 <b>(+72.78%)</b></td><td>0.14 <b>(+110.01%)</b></td><td>0.01 <b>(-72.33%)</b></td><td>298.00 <b>(-52.38%)</b></td><td>274.86 <b>(-40.88%)</b></td><td>279.10 <b>(-42.12%)</b></td><td>250.10 (-5.37%)</td><td>17.85 <b>(-87.27%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>625.80 (n/a)</td><td>464.90 (n/a)</td><td>482.20 (n/a)</td><td>264.30 (n/a)</td><td>140.23 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (+17.39%)</td><td>0.02 <b>(+30.34%)</b></td><td>0.02 (+14.20%)</td><td>0.01 <b>(+20.54%)</b></td><td>0.00 (-3.59%)</td><td>579.70 (-17.04%)</td><td>332.06 <b>(-26.94%)</b></td><td>293.70 (-12.43%)</td><td>233.30 (-14.82%)</td><td>140.93 <b>(-30.70%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>698.80 (n/a)</td><td>454.48 (n/a)</td><td>335.40 (n/a)</td><td>273.90 (n/a)</td><td>203.37 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (-6.27%)</td><td>0.03 (+10.43%)</td><td>0.03 (+4.71%)</td><td>0.02 <b>(+24.34%)</b></td><td>0.01 <b>(-34.38%)</b></td><td>444.90 (-19.58%)</td><td>303.32 (-15.82%)</td><td>269.70 (-4.50%)</td><td>242.60 (+6.68%)</td><td>81.93 <b>(-43.17%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.20 (n/a)</td><td>360.34 (n/a)</td><td>282.40 (n/a)</td><td>227.40 (n/a)</td><td>144.16 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 (-19.54%)</td><td>0.03 <b>(-28.33%)</b></td><td>0.03 <b>(-33.87%)</b></td><td>0.02 (-8.42%)</td><td>0.01 <b>(-31.08%)</b></td><td>667.40 (+9.20%)</td><td>461.90 <b>(+33.75%)</b></td><td>455.70 <b>(+51.19%)</b></td><td>301.00 <b>(+24.28%)</b></td><td>133.27 (-11.85%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>611.20 (n/a)</td><td>345.34 (n/a)</td><td>301.40 (n/a)</td><td>242.20 (n/a)</td><td>151.19 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 <b>(+33.85%)</b></td><td>0.03 <b>(+54.94%)</b></td><td>0.03 <b>(+87.06%)</b></td><td>0.02 <b>(+26.64%)</b></td><td>0.01 <b>(+39.52%)</b></td><td>398.20 <b>(-21.04%)</b></td><td>275.46 <b>(-34.99%)</b></td><td>246.40 <b>(-46.55%)</b></td><td>223.40 <b>(-25.28%)</b></td><td>70.70 (-13.12%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>504.30 (n/a)</td><td>423.74 (n/a)</td><td>461.00 (n/a)</td><td>299.00 (n/a)</td><td>81.38 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (+8.92%)</td><td>0.03 (-11.07%)</td><td>0.02 (-2.51%)</td><td>0.02 (-15.99%)</td><td>0.01 (+5.17%)</td><td>627.80 (+19.04%)</td><td>432.04 (+16.18%)</td><td>434.70 (+2.57%)</td><td>205.80 (-8.21%)</td><td>174.77 <b>(+25.51%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.40 (n/a)</td><td>371.86 (n/a)</td><td>423.80 (n/a)</td><td>224.20 (n/a)</td><td>139.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 <b>(+33.94%)</b></td><td>0.02 (+16.19%)</td><td>0.02 (+10.90%)</td><td>0.02 (+5.03%)</td><td>0.01 <b>(+46.10%)</b></td><td>511.00 (-4.79%)</td><td>376.18 (-11.77%)</td><td>405.00 (-9.82%)</td><td>221.90 <b>(-25.36%)</b></td><td>111.44 (+0.61%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.70 (n/a)</td><td>426.38 (n/a)</td><td>449.10 (n/a)</td><td>297.30 (n/a)</td><td>110.77 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.05 (+4.38%)</td><td>0.03 (-6.95%)</td><td>0.02 (-19.91%)</td><td>0.02 <b>(+150.96%)</b></td><td>0.02 (-7.06%)</td><td>666.80 <b>(-60.16%)</b></td><td>462.00 <b>(-22.25%)</b></td><td>437.90 <b>(+24.83%)</b></td><td>193.10 (-4.17%)</td><td>185.83 <b>(-69.55%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1673.50 (n/a)</td><td>594.20 (n/a)</td><td>350.80 (n/a)</td><td>201.50 (n/a)</td><td>610.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (+1.85%)</td><td>0.02 (-9.56%)</td><td>0.02 (-19.07%)</td><td>0.02 (+4.71%)</td><td>0.01 (+14.49%)</td><td>543.00 (-4.50%)</td><td>412.48 (+12.23%)</td><td>412.30 <b>(+23.59%)</b></td><td>268.60 (-1.83%)</td><td>126.52 (+6.99%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.60 (n/a)</td><td>367.52 (n/a)</td><td>333.60 (n/a)</td><td>273.60 (n/a)</td><td>118.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.04 <b>(+32.54%)</b></td><td>0.02 (+9.20%)</td><td>0.02 (+18.80%)</td><td>0.00 <b>(-67.51%)</b></td><td>0.01 <b>(+124.88%)</b></td><td>1867.40 <b>(+207.75%)</b></td><td>688.44 <b>(+41.91%)</b></td><td>424.30 (-15.83%)</td><td>233.90 <b>(-24.55%)</b></td><td>671.34 <b>(+496.06%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>606.80 (n/a)</td><td>485.12 (n/a)</td><td>504.10 (n/a)</td><td>310.00 (n/a)</td><td>112.63 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 <b>(+55.28%)</b></td><td>0.03 <b>(+56.82%)</b></td><td>0.03 <b>(+76.26%)</b></td><td>0.02 (+13.45%)</td><td>0.01 <b>(+121.26%)</b></td><td>534.70 (-11.87%)</td><td>323.56 <b>(-32.90%)</b></td><td>275.70 <b>(-43.27%)</b></td><td>245.40 <b>(-35.59%)</b></td><td>119.20 <b>(+34.42%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>606.70 (n/a)</td><td>482.24 (n/a)</td><td>486.00 (n/a)</td><td>381.00 (n/a)</td><td>88.68 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 <b>(-22.73%)</b></td><td>0.02 (-3.69%)</td><td>0.02 (+7.28%)</td><td>0.02 <b>(+311.32%)</b></td><td>0.00 <b>(-67.48%)</b></td><td>592.40 <b>(-75.69%)</b></td><td>499.96 <b>(-39.57%)</b></td><td>509.40 (-6.79%)</td><td>377.00 <b>(+29.42%)</b></td><td>89.01 <b>(-90.20%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2436.80 (n/a)</td><td>827.34 (n/a)</td><td>546.50 (n/a)</td><td>291.30 (n/a)</td><td>907.95 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.03 (+7.78%)</td><td>0.02 (+10.36%)</td><td>0.02 (+18.32%)</td><td>0.01 (+3.77%)</td><td>0.01 (+18.79%)</td><td>603.90 (-3.64%)</td><td>443.38 (-8.15%)</td><td>422.30 (-15.49%)</td><td>305.80 (-7.22%)</td><td>119.94 (+9.53%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>626.70 (n/a)</td><td>482.74 (n/a)</td><td>499.70 (n/a)</td><td>329.60 (n/a)</td><td>109.50 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.39 (+1.25%)</td><td>0.29 (-2.76%)</td><td>0.31 (-13.61%)</td><td>0.18 (+9.51%)</td><td>0.09 (-18.65%)</td><td>535.80 (-8.69%)</td><td>372.80 (-2.22%)</td><td>321.10 (+15.75%)</td><td>250.50 (-1.22%)</td><td>124.05 <b>(-24.13%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.35 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>586.80 (n/a)</td><td>381.28 (n/a)</td><td>277.40 (n/a)</td><td>253.60 (n/a)</td><td>163.50 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.40 (+12.17%)</td><td>0.20 <b>(-25.13%)</b></td><td>0.20 <b>(-30.03%)</b></td><td>0.05 <b>(-68.38%)</b></td><td>0.12 <b>(+70.65%)</b></td><td>1862.30 <b>(+216.29%)</b></td><td>739.08 <b>(+89.65%)</b></td><td>500.10 <b>(+42.89%)</b></td><td>247.40 (-10.85%)</td><td>640.69 <b>(+419.60%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>588.80 (n/a)</td><td>389.70 (n/a)</td><td>350.00 (n/a)</td><td>277.50 (n/a)</td><td>123.31 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.37 (-9.95%)</td><td>0.23 <b>(-21.21%)</b></td><td>0.18 <b>(-43.52%)</b></td><td>0.18 (+7.61%)</td><td>0.08 <b>(-27.85%)</b></td><td>546.60 (-7.06%)</td><td>463.68 (+19.06%)</td><td>533.70 <b>(+77.01%)</b></td><td>268.90 (+11.02%)</td><td>118.70 <b>(-28.29%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.33 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>588.10 (n/a)</td><td>389.44 (n/a)</td><td>301.50 (n/a)</td><td>242.20 (n/a)</td><td>165.52 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.29 (+1.46%)</td><td>0.19 (-13.86%)</td><td>0.17 <b>(-35.55%)</b></td><td>0.12 <b>(-23.01%)</b></td><td>0.07 (+7.35%)</td><td>608.10 <b>(+29.88%)</b></td><td>415.34 (+18.78%)</td><td>445.00 <b>(+55.16%)</b></td><td>250.90 (-1.41%)</td><td>137.71 <b>(+28.75%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>468.20 (n/a)</td><td>349.68 (n/a)</td><td>286.80 (n/a)</td><td>254.50 (n/a)</td><td>106.96 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.24 (-16.72%)</td><td>0.15 <b>(-36.37%)</b></td><td>0.12 <b>(-55.22%)</b></td><td>0.07 <b>(-44.65%)</b></td><td>0.06 (-14.32%)</td><td>1017.30 <b>(+80.66%)</b></td><td>587.22 <b>(+66.13%)</b></td><td>594.30 <b>(+123.34%)</b></td><td>303.90 <b>(+20.07%)</b></td><td>271.72 <b>(+95.09%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>563.10 (n/a)</td><td>353.46 (n/a)</td><td>266.10 (n/a)</td><td>253.10 (n/a)</td><td>139.28 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.26 (+6.72%)</td><td>0.19 (+3.49%)</td><td>0.21 <b>(+34.14%)</b></td><td>0.11 (-9.71%)</td><td>0.07 <b>(+27.50%)</b></td><td>692.20 (+10.75%)</td><td>447.20 (+2.19%)</td><td>345.90 <b>(-25.45%)</b></td><td>287.10 (-6.27%)</td><td>186.60 <b>(+41.06%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>625.00 (n/a)</td><td>437.60 (n/a)</td><td>464.00 (n/a)</td><td>306.30 (n/a)</td><td>132.28 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.44 <b>(+40.93%)</b></td><td>0.35 <b>(+98.16%)</b></td><td>0.40 <b>(+102.06%)</b></td><td>0.22 <b>(+234.79%)</b></td><td>0.09 (-12.46%)</td><td>601.10 <b>(-70.13%)</b></td><td>398.80 <b>(-63.34%)</b></td><td>327.50 <b>(-50.51%)</b></td><td>297.80 <b>(-29.03%)</b></td><td>127.92 <b>(-83.09%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>0.11 (n/a)</td><td>2012.40 (n/a)</td><td>1087.76 (n/a)</td><td>661.80 (n/a)</td><td>419.60 (n/a)</td><td>756.34 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.50 (+13.16%)</td><td>0.34 (+8.01%)</td><td>0.29 (+7.19%)</td><td>0.25 (+0.49%)</td><td>0.10 <b>(+22.04%)</b></td><td>520.00 (-0.48%)</td><td>409.14 (-6.21%)</td><td>448.00 (-6.71%)</td><td>261.00 (-11.65%)</td><td>106.66 (+4.05%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.08 (n/a)</td><td>522.50 (n/a)</td><td>436.22 (n/a)</td><td>480.20 (n/a)</td><td>295.40 (n/a)</td><td>102.51 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.48 (+3.68%)</td><td>0.32 (+5.19%)</td><td>0.28 (+3.73%)</td><td>0.18 (-1.20%)</td><td>0.12 (+6.20%)</td><td>731.00 (+1.22%)</td><td>461.52 (-4.11%)</td><td>472.10 (-3.59%)</td><td>273.20 (-3.57%)</td><td>182.67 (+2.67%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.46 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>722.20 (n/a)</td><td>481.28 (n/a)</td><td>489.70 (n/a)</td><td>283.30 (n/a)</td><td>177.92 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (-2.49%)</td><td>0.02 (+18.70%)</td><td>0.01 (+19.21%)</td><td>0.01 <b>(+67.75%)</b></td><td>0.00 <b>(-74.76%)</b></td><td>296.10 <b>(-40.39%)</b></td><td>272.68 <b>(-22.32%)</b></td><td>276.80 (-16.12%)</td><td>248.10 (+2.56%)</td><td>18.11 <b>(-84.17%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.70 (n/a)</td><td>351.04 (n/a)</td><td>330.00 (n/a)</td><td>241.90 (n/a)</td><td>114.40 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 <b>(+22.26%)</b></td><td>0.01 (+2.64%)</td><td>0.02 (+13.05%)</td><td>0.01 <b>(-38.39%)</b></td><td>0.00 <b>(+469.04%)</b></td><td>484.90 <b>(+62.34%)</b></td><td>297.18 (+5.61%)</td><td>248.40 (-11.57%)</td><td>214.00 (-18.20%)</td><td>109.27 <b>(+692.20%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>298.70 (n/a)</td><td>281.40 (n/a)</td><td>280.90 (n/a)</td><td>261.60 (n/a)</td><td>13.79 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 (+3.44%)</td><td>0.01 (+10.95%)</td><td>0.02 (+13.19%)</td><td>0.01 (+3.09%)</td><td>0.00 (-9.49%)</td><td>464.60 (-2.99%)</td><td>314.68 (-11.06%)</td><td>272.00 (-11.66%)</td><td>253.50 (-3.32%)</td><td>86.73 (-13.63%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>478.90 (n/a)</td><td>353.80 (n/a)</td><td>307.90 (n/a)</td><td>262.20 (n/a)</td><td>100.42 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.51 <b>(-23.43%)</b></td><td>0.39 (-7.92%)</td><td>0.37 (+13.43%)</td><td>0.28 <b>(+35.25%)</b></td><td>0.10 <b>(-52.16%)</b></td><td>474.60 <b>(-26.07%)</b></td><td>355.60 (-6.51%)</td><td>356.60 (-11.84%)</td><td>257.20 <b>(+30.62%)</b></td><td>91.31 <b>(-50.59%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.67 (n/a)</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>642.00 (n/a)</td><td>380.36 (n/a)</td><td>404.50 (n/a)</td><td>196.90 (n/a)</td><td>184.82 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.61 <b>(+30.07%)</b></td><td>0.42 (+12.72%)</td><td>0.39 (+19.49%)</td><td>0.29 (-3.03%)</td><td>0.13 <b>(+57.38%)</b></td><td>448.80 (+3.13%)</td><td>334.32 (-8.17%)</td><td>338.90 (-16.32%)</td><td>216.50 <b>(-23.12%)</b></td><td>95.42 <b>(+28.11%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.47 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>435.20 (n/a)</td><td>364.08 (n/a)</td><td>405.00 (n/a)</td><td>281.60 (n/a)</td><td>74.48 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.45 (-5.75%)</td><td>0.30 (+1.32%)</td><td>0.30 (-3.74%)</td><td>0.21 <b>(+33.28%)</b></td><td>0.09 <b>(-25.87%)</b></td><td>639.40 <b>(-24.98%)</b></td><td>464.14 (-8.85%)</td><td>446.10 (+3.89%)</td><td>295.00 (+6.08%)</td><td>127.01 <b>(-43.21%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.48 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>852.30 (n/a)</td><td>509.22 (n/a)</td><td>429.40 (n/a)</td><td>278.10 (n/a)</td><td>223.65 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.60 (+5.19%)</td><td>0.43 (+11.85%)</td><td>0.40 <b>(+26.01%)</b></td><td>0.34 <b>(+41.67%)</b></td><td>0.10 <b>(-38.09%)</b></td><td>390.90 <b>(-29.41%)</b></td><td>316.34 (-19.04%)</td><td>326.40 <b>(-20.66%)</b></td><td>221.30 (-4.94%)</td><td>64.17 <b>(-57.64%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.57 (n/a)</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>553.80 (n/a)</td><td>390.76 (n/a)</td><td>411.40 (n/a)</td><td>232.80 (n/a)</td><td>151.47 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.59 (-6.02%)</td><td>0.45 (-5.99%)</td><td>0.46 (-6.77%)</td><td>0.31 <b>(+21.10%)</b></td><td>0.11 <b>(-24.05%)</b></td><td>424.00 (-17.43%)</td><td>309.12 (+1.49%)</td><td>284.40 (+7.28%)</td><td>225.60 (+6.36%)</td><td>77.70 <b>(-35.75%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.62 (n/a)</td><td>0.48 (n/a)</td><td>0.50 (n/a)</td><td>0.26 (n/a)</td><td>0.14 (n/a)</td><td>513.50 (n/a)</td><td>304.58 (n/a)</td><td>265.10 (n/a)</td><td>212.10 (n/a)</td><td>120.94 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 <b>(+20.41%)</b></td><td>0.02 <b>(+34.25%)</b></td><td>0.02 <b>(+20.11%)</b></td><td>0.01 <b>(+64.24%)</b></td><td>0.00 <b>(-31.69%)</b></td><td>314.50 <b>(-39.11%)</b></td><td>259.68 <b>(-29.21%)</b></td><td>249.80 (-16.76%)</td><td>222.80 (-16.96%)</td><td>37.72 <b>(-65.85%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>516.50 (n/a)</td><td>366.84 (n/a)</td><td>300.10 (n/a)</td><td>268.30 (n/a)</td><td>110.46 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.02 <b>(+27.19%)</b></td><td>0.02 (+14.11%)</td><td>0.02 (+12.00%)</td><td>0.01 (+1.34%)</td><td>0.00 <b>(+201.16%)</b></td><td>327.10 (-1.33%)</td><td>268.78 (-10.97%)</td><td>266.50 (-10.72%)</td><td>223.50 <b>(-21.39%)</b></td><td>41.34 <b>(+130.32%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>331.50 (n/a)</td><td>301.90 (n/a)</td><td>298.50 (n/a)</td><td>284.30 (n/a)</td><td>17.95 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+26.32%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+19.40%)</td><td>22405.15 (+12.18%)</td><td>11972.99 (-7.79%)</td><td>6531.78 <b>(-53.34%)</b></td><td>6023.47 (+4.34%)</td><td>7946.79 <b>(+31.69%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19972.52 (n/a)</td><td>12984.47 (n/a)</td><td>13998.81 (n/a)</td><td>5773.07 (n/a)</td><td>6034.63 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.00 (+8.33%)</td><td>0.00 (+5.56%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+15.01%)</td><td>22076.53 (+7.01%)</td><td>13799.19 (-2.76%)</td><td>16215.12 (-8.22%)</td><td>6496.14 (-2.48%)</td><td>6737.55 (+4.73%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20630.54 (n/a)</td><td>14191.21 (n/a)</td><td>17666.55 (n/a)</td><td>6661.56 (n/a)</td><td>6433.26 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.09 <b>(-41.54%)</b></td><td>0.08 <b>(-26.45%)</b></td><td>0.08 (-5.72%)</td><td>0.07 (+0.28%)</td><td>0.01 <b>(-78.49%)</b></td><td>29471.13 (-0.19%)</td><td>26636.50 <b>(+22.62%)</b></td><td>26497.60 (+5.97%)</td><td>22637.65 <b>(+70.99%)</b></td><td>2927.42 <b>(-61.16%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>29528.24 (n/a)</td><td>21722.14 (n/a)</td><td>25004.94 (n/a)</td><td>13239.53 (n/a)</td><td>7537.48 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.76 (+15.55%)</td><td>1.47 <b>(+51.86%)</b></td><td>1.55 (+12.51%)</td><td>0.93 <b>(+506.62%)</b></td><td>0.32 <b>(-53.14%)</b></td><td>566.60 <b>(-83.52%)</b></td><td>376.24 <b>(-70.48%)</b></td><td>338.30 (-11.11%)</td><td>298.60 (-13.45%)</td><td>108.73 <b>(-92.08%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>1.52 (n/a)</td><td>0.97 (n/a)</td><td>1.38 (n/a)</td><td>0.15 (n/a)</td><td>0.69 (n/a)</td><td>3437.30 (n/a)</td><td>1274.56 (n/a)</td><td>380.60 (n/a)</td><td>345.00 (n/a)</td><td>1372.84 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.74 <b>(-41.16%)</b></td><td>1.38 <b>(-23.65%)</b></td><td>1.55 (-16.37%)</td><td>0.42 <b>(+30.20%)</b></td><td>0.55 <b>(-50.60%)</b></td><td>2519.70 <b>(-23.19%)</b></td><td>1024.60 (-7.15%)</td><td>677.50 (+19.59%)</td><td>604.00 <b>(+69.95%)</b></td><td>837.14 <b>(-32.46%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>2.95 (n/a)</td><td>1.81 (n/a)</td><td>1.85 (n/a)</td><td>0.32 (n/a)</td><td>1.11 (n/a)</td><td>3280.50 (n/a)</td><td>1103.48 (n/a)</td><td>566.50 (n/a)</td><td>355.40 (n/a)</td><td>1239.40 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>1.95 (-5.43%)</td><td>1.74 <b>(+49.02%)</b></td><td>1.66 <b>(+82.69%)</b></td><td>1.59 <b>(+158.39%)</b></td><td>0.15 <b>(-75.33%)</b></td><td>330.40 <b>(-61.30%)</b></td><td>302.76 <b>(-45.39%)</b></td><td>315.30 <b>(-45.27%)</b></td><td>268.20 (+5.72%)</td><td>25.88 <b>(-89.98%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>2.07 (n/a)</td><td>1.17 (n/a)</td><td>0.91 (n/a)</td><td>0.61 (n/a)</td><td>0.62 (n/a)</td><td>853.70 (n/a)</td><td>554.38 (n/a)</td><td>576.10 (n/a)</td><td>253.70 (n/a)</td><td>258.22 (n/a)</td>
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
