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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 (+15.78%)</td><td>0.04 (+12.64%)</td><td>0.04 (+11.88%)</td><td>0.03 (+13.16%)</td><td>0.01 (+11.48%)</td><td>491.30 (-11.64%)</td><td>332.26 (-11.44%)</td><td>285.80 (-10.60%)</td><td>240.40 (-13.62%)</td><td>100.63 (-13.20%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>556.00 (n/a)</td><td>375.16 (n/a)</td><td>319.70 (n/a)</td><td>278.30 (n/a)</td><td>115.93 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.06 (+16.78%)</td><td>0.04 <b>(+22.49%)</b></td><td>0.05 <b>(+61.45%)</b></td><td>0.03 (+5.69%)</td><td>0.01 <b>(+24.29%)</b></td><td>443.50 (-5.40%)</td><td>308.50 (-17.13%)</td><td>256.70 <b>(-38.06%)</b></td><td>219.30 (-14.37%)</td><td>96.68 (+2.70%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>468.80 (n/a)</td><td>372.26 (n/a)</td><td>414.40 (n/a)</td><td>256.10 (n/a)</td><td>94.13 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 (+18.39%)</td><td>0.03 <b>(+47.07%)</b></td><td>0.03 <b>(+29.36%)</b></td><td>0.02 <b>(+294.30%)</b></td><td>0.01 (-18.09%)</td><td>528.90 <b>(-74.64%)</b></td><td>377.94 <b>(-52.13%)</b></td><td>405.20 <b>(-22.70%)</b></td><td>247.60 (-15.55%)</td><td>109.65 <b>(-85.02%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2085.60 (n/a)</td><td>789.48 (n/a)</td><td>524.20 (n/a)</td><td>293.20 (n/a)</td><td>731.92 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (-17.00%)</td><td>0.01 <b>(-29.78%)</b></td><td>0.01 <b>(-41.35%)</b></td><td>0.01 <b>(-23.88%)</b></td><td>0.01 (+1.63%)</td><td>548.90 <b>(+31.35%)</b></td><td>405.04 <b>(+47.85%)</b></td><td>455.60 <b>(+70.51%)</b></td><td>237.30 <b>(+20.52%)</b></td><td>133.81 <b>(+55.29%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>417.90 (n/a)</td><td>273.96 (n/a)</td><td>267.20 (n/a)</td><td>196.90 (n/a)</td><td>86.17 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (-13.13%)</td><td>0.01 (-7.56%)</td><td>0.01 (-5.38%)</td><td>0.01 (+2.74%)</td><td>0.00 (-18.82%)</td><td>550.50 (-2.67%)</td><td>406.04 (+5.39%)</td><td>445.20 (+5.70%)</td><td>264.20 (+15.12%)</td><td>124.00 (-8.97%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.60 (n/a)</td><td>385.26 (n/a)</td><td>421.20 (n/a)</td><td>229.50 (n/a)</td><td>136.22 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (-8.60%)</td><td>0.01 (-13.83%)</td><td>0.01 (-1.18%)</td><td>0.01 <b>(-31.71%)</b></td><td>0.00 (-12.94%)</td><td>785.80 <b>(+46.44%)</b></td><td>508.12 (+17.46%)</td><td>517.90 (+1.21%)</td><td>311.90 (+9.40%)</td><td>177.97 <b>(+39.34%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>536.60 (n/a)</td><td>432.58 (n/a)</td><td>511.70 (n/a)</td><td>285.10 (n/a)</td><td>127.72 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (+7.33%)</td><td>0.02 <b>(+25.58%)</b></td><td>0.02 <b>(+55.66%)</b></td><td>0.01 <b>(+52.31%)</b></td><td>0.01 (-9.30%)</td><td>533.30 <b>(-34.35%)</b></td><td>340.48 <b>(-26.56%)</b></td><td>292.60 <b>(-35.76%)</b></td><td>219.80 (-6.82%)</td><td>128.56 <b>(-43.12%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>812.30 (n/a)</td><td>463.64 (n/a)</td><td>455.50 (n/a)</td><td>235.90 (n/a)</td><td>226.02 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (+0.52%)</td><td>0.01 (+1.03%)</td><td>0.01 (+2.79%)</td><td>0.00 <b>(-50.01%)</b></td><td>0.01 <b>(+45.87%)</b></td><td>1057.30 <b>(+100.02%)</b></td><td>526.42 (+19.97%)</td><td>464.10 (-2.70%)</td><td>248.30 (-0.52%)</td><td>327.02 <b>(+186.82%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.60 (n/a)</td><td>438.78 (n/a)</td><td>477.00 (n/a)</td><td>249.60 (n/a)</td><td>114.02 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 <b>(-22.78%)</b></td><td>0.01 (+12.16%)</td><td>0.02 <b>(+39.24%)</b></td><td>0.01 <b>(+23.24%)</b></td><td>0.00 <b>(-55.26%)</b></td><td>489.70 (-18.86%)</td><td>370.62 (-16.73%)</td><td>344.50 <b>(-28.18%)</b></td><td>323.40 <b>(+29.52%)</b></td><td>67.48 <b>(-49.08%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>603.50 (n/a)</td><td>445.06 (n/a)</td><td>479.70 (n/a)</td><td>249.70 (n/a)</td><td>132.51 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>692.40 (n/a)</td><td>402.02 (n/a)</td><td>385.50 (n/a)</td><td>245.30 (n/a)</td><td>175.90 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.60 (n/a)</td><td>399.52 (n/a)</td><td>391.30 (n/a)</td><td>277.50 (n/a)</td><td>120.74 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.80 (n/a)</td><td>392.68 (n/a)</td><td>390.60 (n/a)</td><td>250.60 (n/a)</td><td>113.93 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>615.40 (n/a)</td><td>411.18 (n/a)</td><td>405.80 (n/a)</td><td>251.20 (n/a)</td><td>156.11 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1918.20 (n/a)</td><td>947.82 (n/a)</td><td>491.40 (n/a)</td><td>197.30 (n/a)</td><td>875.74 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>438.80 (n/a)</td><td>384.22 (n/a)</td><td>390.90 (n/a)</td><td>305.70 (n/a)</td><td>57.60 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.95 (-12.50%)</td><td>0.79 (+3.52%)</td><td>0.78 (+8.03%)</td><td>0.64 <b>(+31.14%)</b></td><td>0.13 <b>(-40.93%)</b></td><td>714.90 <b>(-23.74%)</b></td><td>590.60 (-7.74%)</td><td>588.20 (-7.43%)</td><td>484.70 (+14.29%)</td><td>96.36 <b>(-49.40%)</b></td><td>69.23 (-12.50%)</td><td>58.04 (+3.52%)</td><td>57.05 (+8.03%)</td><td>46.94 <b>(+31.14%)</b></td><td>9.41 <b>(-40.93%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.08 (n/a)</td><td>0.77 (n/a)</td><td>0.72 (n/a)</td><td>0.49 (n/a)</td><td>0.22 (n/a)</td><td>937.50 (n/a)</td><td>640.16 (n/a)</td><td>635.40 (n/a)</td><td>424.10 (n/a)</td><td>190.43 (n/a)</td><td>79.12 (n/a)</td><td>56.06 (n/a)</td><td>52.80 (n/a)</td><td>35.79 (n/a)</td><td>15.93 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.13 <b>(+23.87%)</b></td><td>0.98 <b>(+31.29%)</b></td><td>0.95 (+11.96%)</td><td>0.87 <b>(+140.76%)</b></td><td>0.11 <b>(-53.40%)</b></td><td>750.20 <b>(-58.46%)</b></td><td>676.36 <b>(-31.72%)</b></td><td>689.90 (-10.69%)</td><td>577.80 (-19.27%)</td><td>69.51 <b>(-84.95%)</b></td><td>116.15 <b>(+23.87%)</b></td><td>100.10 <b>(+31.29%)</b></td><td>97.27 (+11.96%)</td><td>89.46 <b>(+140.76%)</b></td><td>10.78 <b>(-53.40%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.92 (n/a)</td><td>0.74 (n/a)</td><td>0.85 (n/a)</td><td>0.36 (n/a)</td><td>0.23 (n/a)</td><td>1806.10 (n/a)</td><td>990.60 (n/a)</td><td>772.50 (n/a)</td><td>715.70 (n/a)</td><td>461.96 (n/a)</td><td>93.77 (n/a)</td><td>76.25 (n/a)</td><td>86.88 (n/a)</td><td>37.16 (n/a)</td><td>23.12 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.40 (-11.55%)</td><td>1.23 (-2.44%)</td><td>1.24 (-9.52%)</td><td>1.06 (+12.13%)</td><td>0.12 <b>(-54.69%)</b></td><td>710.40 (-10.83%)</td><td>617.14 (-0.63%)</td><td>608.40 (+10.52%)</td><td>538.90 (+13.05%)</td><td>62.55 <b>(-55.22%)</b></td><td>155.65 (-11.55%)</td><td>137.02 (-2.44%)</td><td>137.89 (-9.52%)</td><td>118.08 (+12.13%)</td><td>13.63 <b>(-54.69%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.58 (n/a)</td><td>1.26 (n/a)</td><td>1.37 (n/a)</td><td>0.95 (n/a)</td><td>0.27 (n/a)</td><td>796.70 (n/a)</td><td>621.08 (n/a)</td><td>550.50 (n/a)</td><td>476.70 (n/a)</td><td>139.70 (n/a)</td><td>175.99 (n/a)</td><td>140.45 (n/a)</td><td>152.39 (n/a)</td><td>105.30 (n/a)</td><td>30.10 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.57 <b>(+34.06%)</b></td><td>1.30 <b>(+35.32%)</b></td><td>1.24 <b>(+26.44%)</b></td><td>1.11 <b>(+83.93%)</b></td><td>0.19 (-19.89%)</td><td>941.80 <b>(-45.63%)</b></td><td>819.36 <b>(-29.19%)</b></td><td>847.30 <b>(-20.91%)</b></td><td>667.80 <b>(-25.41%)</b></td><td>111.95 <b>(-67.46%)</b></td><td>200.99 <b>(+34.06%)</b></td><td>166.41 <b>(+35.32%)</b></td><td>158.40 <b>(+26.44%)</b></td><td>142.51 <b>(+83.93%)</b></td><td>23.96 (-19.89%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.17 (n/a)</td><td>0.96 (n/a)</td><td>0.98 (n/a)</td><td>0.61 (n/a)</td><td>0.23 (n/a)</td><td>1732.20 (n/a)</td><td>1157.06 (n/a)</td><td>1071.30 (n/a)</td><td>895.30 (n/a)</td><td>343.99 (n/a)</td><td>149.92 (n/a)</td><td>122.98 (n/a)</td><td>125.28 (n/a)</td><td>77.48 (n/a)</td><td>29.90 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.75 <b>(+21.77%)</b></td><td>1.27 <b>(+34.13%)</b></td><td>1.33 (+6.23%)</td><td>0.66 <b>(+113.30%)</b></td><td>0.39 <b>(-25.40%)</b></td><td>1594.80 <b>(-53.12%)</b></td><td>917.88 <b>(-43.65%)</b></td><td>790.90 (-5.87%)</td><td>600.70 (-17.88%)</td><td>389.68 <b>(-67.64%)</b></td><td>223.43 <b>(+21.77%)</b></td><td>162.73 <b>(+34.13%)</b></td><td>169.71 (+6.23%)</td><td>84.16 <b>(+113.30%)</b></td><td>50.50 <b>(-25.40%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.43 (n/a)</td><td>0.95 (n/a)</td><td>1.25 (n/a)</td><td>0.31 (n/a)</td><td>0.53 (n/a)</td><td>3401.70 (n/a)</td><td>1628.94 (n/a)</td><td>840.20 (n/a)</td><td>731.50 (n/a)</td><td>1204.19 (n/a)</td><td>183.48 (n/a)</td><td>121.32 (n/a)</td><td>159.75 (n/a)</td><td>39.46 (n/a)</td><td>67.70 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.88 (-4.35%)</td><td>1.11 <b>(-31.08%)</b></td><td>1.09 <b>(-35.76%)</b></td><td>0.56 <b>(-55.40%)</b></td><td>0.54 <b>(+84.82%)</b></td><td>1856.10 <b>(+124.19%)</b></td><td>1154.90 <b>(+72.18%)</b></td><td>963.40 <b>(+55.64%)</b></td><td>557.30 (+4.56%)</td><td>559.78 <b>(+345.21%)</b></td><td>240.84 (-4.35%)</td><td>141.77 <b>(-31.08%)</b></td><td>139.31 <b>(-35.76%)</b></td><td>72.31 <b>(-55.40%)</b></td><td>69.24 <b>(+84.82%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.97 (n/a)</td><td>1.61 (n/a)</td><td>1.69 (n/a)</td><td>1.27 (n/a)</td><td>0.29 (n/a)</td><td>827.90 (n/a)</td><td>670.76 (n/a)</td><td>619.00 (n/a)</td><td>533.00 (n/a)</td><td>125.73 (n/a)</td><td>251.80 (n/a)</td><td>205.69 (n/a)</td><td>216.85 (n/a)</td><td>162.12 (n/a)</td><td>37.46 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.56 (-12.74%)</td><td>1.18 (-4.19%)</td><td>1.20 (-2.73%)</td><td>0.95 <b>(+119.58%)</b></td><td>0.25 <b>(-50.95%)</b></td><td>1102.20 <b>(-54.46%)</b></td><td>915.50 (-15.43%)</td><td>872.90 (+2.82%)</td><td>672.00 (+14.62%)</td><td>178.63 <b>(-76.37%)</b></td><td>199.74 (-12.74%)</td><td>151.49 (-4.19%)</td><td>153.77 (-2.73%)</td><td>121.77 <b>(+119.58%)</b></td><td>31.64 <b>(-50.95%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.79 (n/a)</td><td>1.24 (n/a)</td><td>1.24 (n/a)</td><td>0.43 (n/a)</td><td>0.50 (n/a)</td><td>2420.20 (n/a)</td><td>1082.56 (n/a)</td><td>849.00 (n/a)</td><td>586.30 (n/a)</td><td>756.06 (n/a)</td><td>228.92 (n/a)</td><td>158.11 (n/a)</td><td>158.09 (n/a)</td><td>55.46 (n/a)</td><td>64.50 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.81 (-11.56%)</td><td>0.55 (-1.38%)</td><td>0.50 (-1.61%)</td><td>0.37 (+1.35%)</td><td>0.16 <b>(-24.94%)</b></td><td>962.40 (-1.33%)</td><td>693.06 (-2.22%)</td><td>718.40 (+1.64%)</td><td>443.00 (+13.10%)</td><td>189.33 (-16.63%)</td><td>37.88 (-11.56%)</td><td>25.81 (-1.38%)</td><td>23.35 (-1.61%)</td><td>17.43 (+1.35%)</td><td>7.62 <b>(-24.94%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.92 (n/a)</td><td>0.56 (n/a)</td><td>0.51 (n/a)</td><td>0.37 (n/a)</td><td>0.22 (n/a)</td><td>975.40 (n/a)</td><td>708.78 (n/a)</td><td>706.80 (n/a)</td><td>391.70 (n/a)</td><td>227.09 (n/a)</td><td>42.83 (n/a)</td><td>26.17 (n/a)</td><td>23.74 (n/a)</td><td>17.20 (n/a)</td><td>10.15 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>3.66 (-7.05%)</td><td>2.33 (-6.08%)</td><td>2.35 (-10.22%)</td><td>1.10 (+5.23%)</td><td>1.23 (-5.72%)</td><td>2387.30 (-4.97%)</td><td>1468.02 (+5.36%)</td><td>1113.40 (+11.38%)</td><td>716.10 (+7.59%)</td><td>842.85 (+0.80%)</td><td>749.67 (-7.05%)</td><td>478.20 (-6.08%)</td><td>482.21 (-10.22%)</td><td>224.89 (+5.23%)</td><td>251.67 (-5.72%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>3.94 (n/a)</td><td>2.49 (n/a)</td><td>2.62 (n/a)</td><td>1.04 (n/a)</td><td>1.30 (n/a)</td><td>2512.20 (n/a)</td><td>1393.34 (n/a)</td><td>999.60 (n/a)</td><td>665.60 (n/a)</td><td>836.18 (n/a)</td><td>806.54 (n/a)</td><td>509.16 (n/a)</td><td>537.07 (n/a)</td><td>213.71 (n/a)</td><td>266.92 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>471.30 (n/a)</td><td>343.98 (n/a)</td><td>380.00 (n/a)</td><td>192.30 (n/a)</td><td>115.33 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.40 (n/a)</td><td>390.84 (n/a)</td><td>377.80 (n/a)</td><td>245.70 (n/a)</td><td>104.37 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.00 (n/a)</td><td>359.84 (n/a)</td><td>311.00 (n/a)</td><td>244.80 (n/a)</td><td>139.85 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>435.60 (n/a)</td><td>329.58 (n/a)</td><td>306.40 (n/a)</td><td>287.90 (n/a)</td><td>60.06 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.70 (n/a)</td><td>466.14 (n/a)</td><td>501.90 (n/a)</td><td>285.60 (n/a)</td><td>104.92 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>472.80 (n/a)</td><td>387.92 (n/a)</td><td>445.20 (n/a)</td><td>266.60 (n/a)</td><td>94.63 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.53 (-19.74%)</td><td>0.47 <b>(+28.15%)</b></td><td>0.50 <b>(+42.75%)</b></td><td>0.40 <b>(+212.42%)</b></td><td>0.06 <b>(-69.74%)</b></td><td>546.40 <b>(-67.99%)</b></td><td>475.72 <b>(-39.62%)</b></td><td>445.00 <b>(-29.94%)</b></td><td>421.00 <b>(+24.59%)</b></td><td>59.50 <b>(-88.77%)</b></td><td>22.41 (-19.74%)</td><td>20.08 <b>(+28.15%)</b></td><td>21.21 <b>(+42.75%)</b></td><td>17.27 <b>(+212.42%)</b></td><td>2.42 <b>(-69.74%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.65 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.13 (n/a)</td><td>0.19 (n/a)</td><td>1707.00 (n/a)</td><td>787.86 (n/a)</td><td>635.20 (n/a)</td><td>337.90 (n/a)</td><td>529.65 (n/a)</td><td>27.93 (n/a)</td><td>15.67 (n/a)</td><td>14.86 (n/a)</td><td>5.53 (n/a)</td><td>7.99 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.57 (-17.22%)</td><td>0.41 (+11.32%)</td><td>0.43 <b>(+23.34%)</b></td><td>0.22 <b>(+75.45%)</b></td><td>0.13 <b>(-46.96%)</b></td><td>1002.20 <b>(-43.01%)</b></td><td>598.36 <b>(-37.49%)</b></td><td>518.80 (-18.92%)</td><td>385.20 <b>(+20.79%)</b></td><td>242.23 <b>(-65.39%)</b></td><td>24.50 (-17.22%)</td><td>17.54 (+11.32%)</td><td>18.19 <b>(+23.34%)</b></td><td>9.42 <b>(+75.45%)</b></td><td>5.69 <b>(-46.96%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.69 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.13 (n/a)</td><td>0.25 (n/a)</td><td>1758.40 (n/a)</td><td>957.18 (n/a)</td><td>639.90 (n/a)</td><td>318.90 (n/a)</td><td>699.80 (n/a)</td><td>29.59 (n/a)</td><td>15.76 (n/a)</td><td>14.75 (n/a)</td><td>5.37 (n/a)</td><td>10.73 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.31 (-0.05%)</td><td>0.30 (-0.62%)</td><td>0.31 (-0.36%)</td><td>0.30 (-0.27%)</td><td>0.00 (-1.07%)</td><td>83916.70 (+0.27%)</td><td>82532.32 (+0.62%)</td><td>82461.20 (+0.36%)</td><td>80896.30 (+0.05%)</td><td>1114.09 (-0.79%)</td><td>212.37 (-0.05%)</td><td>208.19 (-0.62%)</td><td>208.34 (-0.36%)</td><td>204.73 (-0.27%)</td><td>2.82 (-1.07%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83694.10 (n/a)</td><td>82022.86 (n/a)</td><td>82161.50 (n/a)</td><td>80857.80 (n/a)</td><td>1123.02 (n/a)</td><td>212.47 (n/a)</td><td>209.48 (n/a)</td><td>209.10 (n/a)</td><td>205.27 (n/a)</td><td>2.85 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.15 (+0.04%)</td><td>1.14 (+2.29%)</td><td>1.14 (-0.52%)</td><td>1.13 (+6.83%)</td><td>0.01 <b>(-82.15%)</b></td><td>22314.80 (-6.39%)</td><td>22057.70 (-2.37%)</td><td>22035.40 (+0.53%)</td><td>21888.10 (-0.04%)</td><td>159.61 <b>(-83.18%)</b></td><td>784.89 (+0.04%)</td><td>778.89 (+2.29%)</td><td>779.65 (-0.52%)</td><td>769.89 (+6.83%)</td><td>5.61 <b>(-82.15%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.15 (n/a)</td><td>1.12 (n/a)</td><td>1.15 (n/a)</td><td>1.06 (n/a)</td><td>0.05 (n/a)</td><td>23839.20 (n/a)</td><td>22593.44 (n/a)</td><td>21920.00 (n/a)</td><td>21896.60 (n/a)</td><td>948.79 (n/a)</td><td>784.59 (n/a)</td><td>761.45 (n/a)</td><td>783.75 (n/a)</td><td>720.66 (n/a)</td><td>31.41 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>4.17 (-5.56%)</td><td>2.75 (-18.34%)</td><td>2.11 <b>(-41.35%)</b></td><td>1.31 <b>(-33.27%)</b></td><td>1.29 (+18.00%)</td><td>6171.70 <b>(+49.86%)</b></td><td>3556.80 <b>(+34.15%)</b></td><td>3819.00 <b>(+70.51%)</b></td><td>1934.20 (+5.88%)</td><td>1739.87 <b>(+75.45%)</b></td><td>1092.89 (-5.56%)</td><td>719.87 (-18.34%)</td><td>553.54 <b>(-41.35%)</b></td><td>342.52 <b>(-33.27%)</b></td><td>338.53 (+18.00%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>4.41 (n/a)</td><td>3.36 (n/a)</td><td>3.60 (n/a)</td><td>1.96 (n/a)</td><td>1.09 (n/a)</td><td>4118.20 (n/a)</td><td>2651.30 (n/a)</td><td>2239.70 (n/a)</td><td>1826.70 (n/a)</td><td>991.65 (n/a)</td><td>1157.25 (n/a)</td><td>881.58 (n/a)</td><td>943.85 (n/a)</td><td>513.31 (n/a)</td><td>286.89 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.30 (-3.21%)</td><td>0.21 (-11.74%)</td><td>0.19 (-10.45%)</td><td>0.16 (-9.85%)</td><td>0.05 (-5.30%)</td><td>7579.90 (+10.92%)</td><td>6313.86 (+13.13%)</td><td>6528.20 (+11.67%)</td><td>4155.90 (+3.31%)</td><td>1304.23 (+2.44%)</td><td>16.15 (-3.21%)</td><td>11.10 (-11.74%)</td><td>10.28 (-10.45%)</td><td>8.85 (-9.85%)</td><td>2.90 (-5.30%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>6833.70 (n/a)</td><td>5581.26 (n/a)</td><td>5846.00 (n/a)</td><td>4022.70 (n/a)</td><td>1273.19 (n/a)</td><td>16.68 (n/a)</td><td>12.58 (n/a)</td><td>11.48 (n/a)</td><td>9.82 (n/a)</td><td>3.07 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>3.85 (n/a)</td><td>3.61 (n/a)</td><td>3.73 (n/a)</td><td>3.28 (n/a)</td><td>0.25 (n/a)</td><td>3.85 (n/a)</td><td>3.61 (n/a)</td><td>3.73 (n/a)</td><td>3.27 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>7.61 (+10.97%)</td><td>6.27 (+3.06%)</td><td>5.85 (-0.98%)</td><td>4.64 (-18.81%)</td><td>1.24 <b>(+166.78%)</b></td><td>7.60 (+10.97%)</td><td>6.27 (+3.06%)</td><td>5.85 (-0.98%)</td><td>4.64 (-18.81%)</td><td>1.24 <b>(+166.78%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>6.85 (n/a)</td><td>6.09 (n/a)</td><td>5.91 (n/a)</td><td>5.72 (n/a)</td><td>0.47 (n/a)</td><td>6.85 (n/a)</td><td>6.08 (n/a)</td><td>5.90 (n/a)</td><td>5.72 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>13.48 (-1.97%)</td><td>11.25 (+7.33%)</td><td>12.38 <b>(+26.97%)</b></td><td>7.25 <b>(-20.31%)</b></td><td>2.68 <b>(+39.09%)</b></td><td>13.47 (-1.97%)</td><td>11.24 (+7.33%)</td><td>12.37 <b>(+26.97%)</b></td><td>7.24 <b>(-20.31%)</b></td><td>2.68 <b>(+39.09%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>13.75 (n/a)</td><td>10.48 (n/a)</td><td>9.75 (n/a)</td><td>9.09 (n/a)</td><td>1.93 (n/a)</td><td>13.74 (n/a)</td><td>10.48 (n/a)</td><td>9.74 (n/a)</td><td>9.09 (n/a)</td><td>1.93 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>3.83 (n/a)</td><td>3.69 (n/a)</td><td>3.70 (n/a)</td><td>3.51 (n/a)</td><td>0.11 (n/a)</td><td>3.82 (n/a)</td><td>3.69 (n/a)</td><td>3.70 (n/a)</td><td>3.51 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>7.30 (-2.58%)</td><td>7.12 (+9.15%)</td><td>7.13 (+2.48%)</td><td>6.78 <b>(+28.73%)</b></td><td>0.21 <b>(-78.01%)</b></td><td>7.30 (-2.58%)</td><td>7.11 (+9.15%)</td><td>7.13 (+2.48%)</td><td>6.77 <b>(+28.73%)</b></td><td>0.21 <b>(-78.01%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>7.49 (n/a)</td><td>6.52 (n/a)</td><td>6.96 (n/a)</td><td>5.26 (n/a)</td><td>0.95 (n/a)</td><td>7.49 (n/a)</td><td>6.52 (n/a)</td><td>6.95 (n/a)</td><td>5.26 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>13.27 (+3.87%)</td><td>9.81 (+15.12%)</td><td>9.27 (+15.51%)</td><td>8.26 <b>(+41.92%)</b></td><td>2.04 <b>(-20.42%)</b></td><td>13.26 (+3.87%)</td><td>9.80 (+15.12%)</td><td>9.26 (+15.51%)</td><td>8.25 <b>(+41.92%)</b></td><td>2.04 <b>(-20.42%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>12.78 (n/a)</td><td>8.52 (n/a)</td><td>8.02 (n/a)</td><td>5.82 (n/a)</td><td>2.57 (n/a)</td><td>12.77 (n/a)</td><td>8.51 (n/a)</td><td>8.02 (n/a)</td><td>5.81 (n/a)</td><td>2.57 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>2.90 (+4.86%)</td><td>1.52 <b>(-29.95%)</b></td><td>1.04 <b>(-45.41%)</b></td><td>0.97 <b>(-43.09%)</b></td><td>0.82 <b>(+50.42%)</b></td><td>2.89 (+4.86%)</td><td>1.52 <b>(-29.95%)</b></td><td>1.04 <b>(-45.41%)</b></td><td>0.97 <b>(-43.09%)</b></td><td>0.82 <b>(+50.42%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>2.76 (n/a)</td><td>2.17 (n/a)</td><td>1.91 (n/a)</td><td>1.71 (n/a)</td><td>0.55 (n/a)</td><td>2.76 (n/a)</td><td>2.17 (n/a)</td><td>1.90 (n/a)</td><td>1.70 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.71 <b>(+23.74%)</b></td><td>0.47 (+19.40%)</td><td>0.51 (+13.81%)</td><td>0.28 <b>(+277.55%)</b></td><td>0.18 (-12.40%)</td><td>0.70 <b>(+23.74%)</b></td><td>0.46 (+19.40%)</td><td>0.51 (+13.81%)</td><td>0.28 <b>(+277.55%)</b></td><td>0.18 (-12.40%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.58 (n/a)</td><td>0.39 (n/a)</td><td>0.45 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td><td>0.57 (n/a)</td><td>0.38 (n/a)</td><td>0.45 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.62 (-14.55%)</td><td>0.58 <b>(+119.59%)</b></td><td>0.61 <b>(+668.87%)</b></td><td>0.45 <b>(+487.90%)</b></td><td>0.07 <b>(-73.91%)</b></td><td>0.62 (-14.55%)</td><td>0.57 <b>(+119.59%)</b></td><td>0.61 <b>(+668.87%)</b></td><td>0.44 <b>(+487.90%)</b></td><td>0.07 <b>(-73.91%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.73 (n/a)</td><td>0.26 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.29 (n/a)</td><td>0.72 (n/a)</td><td>0.26 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.28 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>2.75 (-7.43%)</td><td>1.78 <b>(+71.59%)</b></td><td>1.59 <b>(+251.28%)</b></td><td>0.45 (+2.43%)</td><td>0.91 (-17.09%)</td><td>2.71 (-7.43%)</td><td>1.75 <b>(+71.59%)</b></td><td>1.56 <b>(+251.27%)</b></td><td>0.45 (+2.43%)</td><td>0.90 (-17.09%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>2.98 (n/a)</td><td>1.04 (n/a)</td><td>0.45 (n/a)</td><td>0.44 (n/a)</td><td>1.10 (n/a)</td><td>2.93 (n/a)</td><td>1.02 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.50 (n/a)</td><td>440.82 (n/a)</td><td>488.60 (n/a)</td><td>274.50 (n/a)</td><td>111.07 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.70 (n/a)</td><td>382.66 (n/a)</td><td>360.50 (n/a)</td><td>205.80 (n/a)</td><td>149.36 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>522.40 (n/a)</td><td>431.16 (n/a)</td><td>458.40 (n/a)</td><td>336.80 (n/a)</td><td>82.20 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>527.80 (n/a)</td><td>435.66 (n/a)</td><td>452.30 (n/a)</td><td>302.10 (n/a)</td><td>86.87 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.30 (n/a)</td><td>390.98 (n/a)</td><td>267.60 (n/a)</td><td>248.90 (n/a)</td><td>180.92 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>657.20 (n/a)</td><td>501.60 (n/a)</td><td>582.40 (n/a)</td><td>249.80 (n/a)</td><td>172.16 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 <b>(+57.03%)</b></td><td>0.03 <b>(+28.59%)</b></td><td>0.03 <b>(+37.47%)</b></td><td>0.01 (+3.78%)</td><td>0.02 <b>(+105.56%)</b></td><td>575.10 (-3.65%)</td><td>340.66 (-10.12%)</td><td>243.10 <b>(-27.26%)</b></td><td>166.00 <b>(-36.33%)</b></td><td>187.25 <b>(+35.66%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>596.90 (n/a)</td><td>379.02 (n/a)</td><td>334.20 (n/a)</td><td>260.70 (n/a)</td><td>138.03 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (-7.94%)</td><td>0.02 <b>(-22.28%)</b></td><td>0.02 <b>(-32.19%)</b></td><td>0.01 (-9.66%)</td><td>0.01 (-9.41%)</td><td>627.00 (+10.70%)</td><td>428.60 <b>(+27.41%)</b></td><td>434.30 <b>(+47.47%)</b></td><td>264.70 (+8.62%)</td><td>131.33 (+0.52%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.40 (n/a)</td><td>336.40 (n/a)</td><td>294.50 (n/a)</td><td>243.70 (n/a)</td><td>130.65 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 <b>(+53.81%)</b></td><td>0.03 (+18.20%)</td><td>0.04 <b>(+26.90%)</b></td><td>0.02 (+7.71%)</td><td>0.02 <b>(+115.41%)</b></td><td>498.40 (-7.15%)</td><td>308.36 (-1.98%)</td><td>212.90 <b>(-21.21%)</b></td><td>149.00 <b>(-34.99%)</b></td><td>168.73 <b>(+34.45%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.80 (n/a)</td><td>314.60 (n/a)</td><td>270.20 (n/a)</td><td>229.20 (n/a)</td><td>125.50 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 <b>(+54.08%)</b></td><td>0.03 <b>(+28.51%)</b></td><td>0.02 <b>(+27.99%)</b></td><td>0.02 <b>(+24.99%)</b></td><td>0.01 <b>(+36.68%)</b></td><td>523.70 (-20.00%)</td><td>346.90 <b>(-22.82%)</b></td><td>373.20 <b>(-21.88%)</b></td><td>165.80 <b>(-35.11%)</b></td><td>135.50 <b>(-27.70%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>654.60 (n/a)</td><td>449.48 (n/a)</td><td>477.70 (n/a)</td><td>255.50 (n/a)</td><td>187.42 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 <b>(+61.79%)</b></td><td>0.03 (+12.56%)</td><td>0.02 <b>(-22.83%)</b></td><td>0.02 <b>(+29.71%)</b></td><td>0.01 <b>(+100.09%)</b></td><td>441.60 <b>(-22.91%)</b></td><td>319.56 (-5.04%)</td><td>360.50 <b>(+29.58%)</b></td><td>163.80 <b>(-38.19%)</b></td><td>124.14 (-6.25%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>572.80 (n/a)</td><td>336.52 (n/a)</td><td>278.20 (n/a)</td><td>265.00 (n/a)</td><td>132.41 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (+3.14%)</td><td>0.01 <b>(-38.53%)</b></td><td>0.02 <b>(-33.42%)</b></td><td>0.00 <b>(-81.71%)</b></td><td>0.01 <b>(+116.98%)</b></td><td>2437.30 <b>(+446.72%)</b></td><td>953.92 <b>(+165.08%)</b></td><td>525.60 <b>(+50.21%)</b></td><td>280.60 (-3.04%)</td><td>870.64 <b>(+1137.18%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>445.80 (n/a)</td><td>359.86 (n/a)</td><td>349.90 (n/a)</td><td>289.40 (n/a)</td><td>70.37 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (-13.26%)</td><td>0.02 <b>(-29.92%)</b></td><td>0.02 <b>(-32.96%)</b></td><td>0.00 <b>(-74.58%)</b></td><td>0.01 (+7.76%)</td><td>2362.60 <b>(+293.37%)</b></td><td>821.28 <b>(+115.73%)</b></td><td>444.80 <b>(+49.16%)</b></td><td>247.80 (+15.26%)</td><td>870.98 <b>(+435.95%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>600.60 (n/a)</td><td>380.70 (n/a)</td><td>298.20 (n/a)</td><td>215.00 (n/a)</td><td>162.51 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 <b>(+37.89%)</b></td><td>0.02 (+11.32%)</td><td>0.02 (-18.14%)</td><td>0.02 <b>(+22.44%)</b></td><td>0.01 <b>(+56.04%)</b></td><td>527.40 (-18.33%)</td><td>403.94 (-7.19%)</td><td>433.30 <b>(+22.16%)</b></td><td>222.90 <b>(-27.49%)</b></td><td>133.24 (-5.71%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>645.80 (n/a)</td><td>435.22 (n/a)</td><td>354.70 (n/a)</td><td>307.40 (n/a)</td><td>141.31 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (+7.41%)</td><td>0.03 <b>(+27.46%)</b></td><td>0.03 <b>(+48.27%)</b></td><td>0.02 (+14.57%)</td><td>0.01 (-8.74%)</td><td>513.30 (-12.72%)</td><td>310.50 <b>(-24.24%)</b></td><td>280.20 <b>(-32.56%)</b></td><td>210.50 (-6.90%)</td><td>118.35 <b>(-21.96%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.10 (n/a)</td><td>409.84 (n/a)</td><td>415.50 (n/a)</td><td>226.10 (n/a)</td><td>151.65 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (+3.19%)</td><td>0.02 (-19.11%)</td><td>0.02 <b>(-23.36%)</b></td><td>0.01 <b>(-67.74%)</b></td><td>0.01 <b>(+246.75%)</b></td><td>1023.90 <b>(+209.99%)</b></td><td>478.80 <b>(+63.67%)</b></td><td>374.50 <b>(+30.49%)</b></td><td>237.20 (-3.10%)</td><td>326.19 <b>(+889.95%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>330.30 (n/a)</td><td>292.54 (n/a)</td><td>287.00 (n/a)</td><td>244.80 (n/a)</td><td>32.95 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 <b>(+22.35%)</b></td><td>0.02 (+1.29%)</td><td>0.02 (+8.81%)</td><td>0.02 (+15.53%)</td><td>0.01 (+13.24%)</td><td>507.30 (-13.44%)</td><td>435.32 (-2.11%)</td><td>488.20 (-8.09%)</td><td>228.40 (-18.28%)</td><td>117.92 (-19.35%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.10 (n/a)</td><td>444.72 (n/a)</td><td>531.20 (n/a)</td><td>279.50 (n/a)</td><td>146.22 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 <b>(-28.90%)</b></td><td>0.02 <b>(-21.68%)</b></td><td>0.02 (+18.78%)</td><td>0.01 <b>(-33.97%)</b></td><td>0.01 <b>(-39.51%)</b></td><td>795.70 <b>(+51.45%)</b></td><td>495.52 <b>(+23.89%)</b></td><td>407.40 (-15.81%)</td><td>318.20 <b>(+40.67%)</b></td><td>192.30 <b>(+29.97%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.40 (n/a)</td><td>399.98 (n/a)</td><td>483.90 (n/a)</td><td>226.20 (n/a)</td><td>147.95 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (+13.15%)</td><td>0.02 (+10.24%)</td><td>0.02 (+8.00%)</td><td>0.01 (+7.06%)</td><td>0.01 <b>(+21.95%)</b></td><td>584.60 (-6.58%)</td><td>414.86 (-6.86%)</td><td>467.50 (-7.41%)</td><td>219.30 (-11.61%)</td><td>156.34 (+2.13%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>625.80 (n/a)</td><td>445.40 (n/a)</td><td>504.90 (n/a)</td><td>248.10 (n/a)</td><td>153.09 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 <b>(-33.59%)</b></td><td>0.01 (-12.35%)</td><td>0.01 (-8.60%)</td><td>0.01 <b>(+43.34%)</b></td><td>0.00 <b>(-62.71%)</b></td><td>788.80 <b>(-30.24%)</b></td><td>595.02 (-3.25%)</td><td>565.40 (+9.40%)</td><td>455.00 <b>(+50.56%)</b></td><td>125.56 <b>(-61.13%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1130.70 (n/a)</td><td>614.98 (n/a)</td><td>516.80 (n/a)</td><td>302.20 (n/a)</td><td>322.99 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.12 (-2.39%)</td><td>0.10 (+13.84%)</td><td>0.10 (+2.22%)</td><td>0.09 <b>(+111.23%)</b></td><td>0.01 <b>(-66.26%)</b></td><td>261.90 <b>(-52.66%)</b></td><td>238.12 <b>(-21.59%)</b></td><td>243.90 (-2.17%)</td><td>206.80 (+2.43%)</td><td>21.01 <b>(-85.16%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>553.20 (n/a)</td><td>303.70 (n/a)</td><td>249.30 (n/a)</td><td>201.90 (n/a)</td><td>141.55 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.18 (-1.81%)</td><td>0.15 (-8.89%)</td><td>0.16 (-3.67%)</td><td>0.09 <b>(-37.06%)</b></td><td>0.03 <b>(+116.04%)</b></td><td>447.00 <b>(+58.91%)</b></td><td>296.04 (+15.24%)</td><td>261.60 (+3.81%)</td><td>226.70 (+1.84%)</td><td>88.00 <b>(+259.86%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>281.30 (n/a)</td><td>256.90 (n/a)</td><td>252.00 (n/a)</td><td>222.60 (n/a)</td><td>24.45 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (-8.70%)</td><td>0.02 (-0.89%)</td><td>0.02 (+0.39%)</td><td>0.01 (+5.41%)</td><td>0.00 (-14.53%)</td><td>409.60 (-5.12%)</td><td>278.62 (-0.59%)</td><td>245.10 (-0.41%)</td><td>235.80 (+9.57%)</td><td>74.11 (-14.47%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>431.70 (n/a)</td><td>280.28 (n/a)</td><td>246.10 (n/a)</td><td>215.20 (n/a)</td><td>86.65 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 (-12.28%)</td><td>0.02 (-17.55%)</td><td>0.03 (-18.21%)</td><td>0.02 (+5.49%)</td><td>0.01 <b>(-27.12%)</b></td><td>489.20 (-5.21%)</td><td>363.80 (+17.21%)</td><td>313.50 <b>(+22.27%)</b></td><td>274.30 (+14.01%)</td><td>91.12 <b>(-22.00%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.10 (n/a)</td><td>310.38 (n/a)</td><td>256.40 (n/a)</td><td>240.60 (n/a)</td><td>116.83 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (-14.77%)</td><td>0.02 <b>(-37.41%)</b></td><td>0.02 <b>(-41.68%)</b></td><td>0.01 <b>(-80.14%)</b></td><td>0.01 <b>(+31.19%)</b></td><td>2450.30 <b>(+403.66%)</b></td><td>860.86 <b>(+147.53%)</b></td><td>513.40 <b>(+71.48%)</b></td><td>300.80 (+17.32%)</td><td>894.16 <b>(+799.04%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>486.50 (n/a)</td><td>347.78 (n/a)</td><td>299.40 (n/a)</td><td>256.40 (n/a)</td><td>99.46 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (-5.25%)</td><td>0.02 (+14.84%)</td><td>0.02 <b>(+23.74%)</b></td><td>0.01 (-18.62%)</td><td>0.01 (-7.41%)</td><td>801.10 <b>(+22.89%)</b></td><td>444.72 (-11.05%)</td><td>433.50 (-19.18%)</td><td>230.50 (+5.54%)</td><td>219.19 <b>(+32.88%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.90 (n/a)</td><td>499.98 (n/a)</td><td>536.40 (n/a)</td><td>218.40 (n/a)</td><td>164.95 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 <b>(+70.73%)</b></td><td>0.03 <b>(+23.62%)</b></td><td>0.02 (+7.14%)</td><td>0.02 (-9.24%)</td><td>0.01 <b>(+313.83%)</b></td><td>592.10 (+10.18%)</td><td>409.14 (-9.31%)</td><td>418.50 (-6.65%)</td><td>220.90 <b>(-41.42%)</b></td><td>151.12 <b>(+165.14%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>537.40 (n/a)</td><td>451.16 (n/a)</td><td>448.30 (n/a)</td><td>377.10 (n/a)</td><td>57.00 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.03 <b>(-26.77%)</b></td><td>0.02 <b>(-30.32%)</b></td><td>0.02 <b>(-36.94%)</b></td><td>0.01 (-9.53%)</td><td>0.01 <b>(-24.57%)</b></td><td>579.40 (+10.55%)</td><td>414.58 <b>(+40.73%)</b></td><td>405.70 <b>(+58.60%)</b></td><td>265.60 <b>(+36.56%)</b></td><td>142.23 (+7.23%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.10 (n/a)</td><td>294.60 (n/a)</td><td>255.80 (n/a)</td><td>194.50 (n/a)</td><td>132.64 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (-6.31%)</td><td>0.02 (-8.04%)</td><td>0.02 <b>(-22.94%)</b></td><td>0.02 <b>(+42.82%)</b></td><td>0.01 <b>(-24.80%)</b></td><td>504.50 <b>(-29.98%)</b></td><td>430.46 (+1.91%)</td><td>472.20 <b>(+29.76%)</b></td><td>278.90 (+6.74%)</td><td>94.20 <b>(-46.89%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>720.50 (n/a)</td><td>422.38 (n/a)</td><td>363.90 (n/a)</td><td>261.30 (n/a)</td><td>177.36 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (+4.68%)</td><td>0.02 (-5.92%)</td><td>0.02 (-11.19%)</td><td>0.02 (+2.20%)</td><td>0.01 (+2.00%)</td><td>520.60 (-2.16%)</td><td>375.56 (+6.35%)</td><td>337.20 (+12.63%)</td><td>221.30 (-4.45%)</td><td>129.71 (-0.22%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.10 (n/a)</td><td>353.14 (n/a)</td><td>299.40 (n/a)</td><td>231.60 (n/a)</td><td>129.99 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (-15.54%)</td><td>0.03 (-6.53%)</td><td>0.02 <b>(-23.32%)</b></td><td>0.02 <b>(+166.08%)</b></td><td>0.01 <b>(-37.99%)</b></td><td>491.40 <b>(-62.42%)</b></td><td>370.74 <b>(-25.24%)</b></td><td>414.90 <b>(+30.39%)</b></td><td>210.50 (+18.39%)</td><td>116.77 <b>(-74.79%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1307.60 (n/a)</td><td>495.94 (n/a)</td><td>318.20 (n/a)</td><td>177.80 (n/a)</td><td>463.25 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.05 <b>(+30.82%)</b></td><td>0.03 <b>(+32.06%)</b></td><td>0.02 (-16.04%)</td><td>0.01 <b>(+34.78%)</b></td><td>0.02 <b>(+75.48%)</b></td><td>611.40 <b>(-25.81%)</b></td><td>403.64 (-14.74%)</td><td>517.60 (+19.13%)</td><td>176.00 <b>(-23.58%)</b></td><td>205.33 (-5.71%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>824.10 (n/a)</td><td>473.40 (n/a)</td><td>434.50 (n/a)</td><td>230.30 (n/a)</td><td>217.77 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 <b>(+60.89%)</b></td><td>0.03 <b>(+33.27%)</b></td><td>0.02 (-4.85%)</td><td>0.02 (+10.66%)</td><td>0.01 <b>(+191.16%)</b></td><td>608.80 (-9.65%)</td><td>409.62 (-12.08%)</td><td>468.20 (+5.10%)</td><td>209.40 <b>(-37.86%)</b></td><td>187.92 <b>(+47.89%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>673.80 (n/a)</td><td>465.88 (n/a)</td><td>445.50 (n/a)</td><td>337.00 (n/a)</td><td>127.07 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.04 (-4.17%)</td><td>0.02 (-9.98%)</td><td>0.01 (-18.26%)</td><td>0.01 (-10.59%)</td><td>0.01 (+3.47%)</td><td>605.20 (+11.85%)</td><td>488.14 (+14.52%)</td><td>558.90 <b>(+22.35%)</b></td><td>223.00 (+4.35%)</td><td>156.99 <b>(+25.89%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.10 (n/a)</td><td>426.24 (n/a)</td><td>456.80 (n/a)</td><td>213.70 (n/a)</td><td>124.71 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.35 (-10.03%)</td><td>0.27 (-8.75%)</td><td>0.32 (-12.74%)</td><td>0.15 (-13.54%)</td><td>0.09 (-16.38%)</td><td>645.50 (+15.66%)</td><td>404.76 (+7.55%)</td><td>311.80 (+14.63%)</td><td>282.20 (+11.15%)</td><td>161.78 (+2.63%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.39 (n/a)</td><td>0.30 (n/a)</td><td>0.36 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>558.10 (n/a)</td><td>376.34 (n/a)</td><td>272.00 (n/a)</td><td>253.90 (n/a)</td><td>157.62 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.37 <b>(-30.35%)</b></td><td>0.23 <b>(-27.87%)</b></td><td>0.19 <b>(-40.26%)</b></td><td>0.18 (-1.17%)</td><td>0.08 <b>(-43.02%)</b></td><td>544.60 (+1.19%)</td><td>454.00 <b>(+28.40%)</b></td><td>509.00 <b>(+67.38%)</b></td><td>265.00 <b>(+43.63%)</b></td><td>114.51 <b>(-21.83%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.53 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>538.20 (n/a)</td><td>353.58 (n/a)</td><td>304.10 (n/a)</td><td>184.50 (n/a)</td><td>146.49 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.38 <b>(-29.34%)</b></td><td>0.23 (-7.00%)</td><td>0.20 (+6.85%)</td><td>0.17 <b>(+20.86%)</b></td><td>0.09 <b>(-47.33%)</b></td><td>585.90 (-17.26%)</td><td>474.24 (-6.28%)</td><td>497.60 (-6.41%)</td><td>262.10 <b>(+41.52%)</b></td><td>129.19 <b>(-33.98%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.53 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>708.10 (n/a)</td><td>506.04 (n/a)</td><td>531.70 (n/a)</td><td>185.20 (n/a)</td><td>195.69 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.29 (+12.47%)</td><td>0.22 <b>(+21.31%)</b></td><td>0.25 <b>(+65.45%)</b></td><td>0.14 <b>(+23.11%)</b></td><td>0.07 (+5.63%)</td><td>539.00 (-18.78%)</td><td>368.70 (-18.56%)</td><td>290.50 <b>(-39.57%)</b></td><td>254.10 (-11.09%)</td><td>134.63 (-17.27%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>663.60 (n/a)</td><td>452.72 (n/a)</td><td>480.70 (n/a)</td><td>285.80 (n/a)</td><td>162.74 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.28 (-3.03%)</td><td>0.18 (-15.05%)</td><td>0.15 <b>(-38.44%)</b></td><td>0.13 <b>(+28.65%)</b></td><td>0.06 <b>(-28.63%)</b></td><td>578.50 <b>(-22.27%)</b></td><td>453.04 (+5.90%)</td><td>498.10 <b>(+62.41%)</b></td><td>261.80 (+3.15%)</td><td>127.09 <b>(-42.11%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>744.20 (n/a)</td><td>427.78 (n/a)</td><td>306.70 (n/a)</td><td>253.80 (n/a)</td><td>219.53 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.24 (-13.66%)</td><td>0.19 (+5.19%)</td><td>0.19 (+10.57%)</td><td>0.15 <b>(+304.00%)</b></td><td>0.04 <b>(-59.91%)</b></td><td>482.40 <b>(-75.25%)</b></td><td>396.20 <b>(-41.60%)</b></td><td>398.20 (-9.56%)</td><td>308.10 (+15.83%)</td><td>80.37 <b>(-88.78%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.10 (n/a)</td><td>1949.10 (n/a)</td><td>678.48 (n/a)</td><td>440.30 (n/a)</td><td>266.00 (n/a)</td><td>716.57 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.49 (-17.92%)</td><td>0.33 (-9.80%)</td><td>0.27 <b>(-30.54%)</b></td><td>0.21 <b>(+20.57%)</b></td><td>0.14 (-16.38%)</td><td>631.40 (-17.06%)</td><td>450.24 (+5.15%)</td><td>489.80 <b>(+43.97%)</b></td><td>266.90 <b>(+21.82%)</b></td><td>170.73 <b>(-21.06%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.60 (n/a)</td><td>0.37 (n/a)</td><td>0.39 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>761.30 (n/a)</td><td>428.20 (n/a)</td><td>340.20 (n/a)</td><td>219.10 (n/a)</td><td>216.27 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.71 <b>(+64.50%)</b></td><td>0.35 (+5.44%)</td><td>0.23 <b>(-34.80%)</b></td><td>0.18 (-11.72%)</td><td>0.22 <b>(+117.35%)</b></td><td>730.90 (+13.28%)</td><td>479.98 (+11.77%)</td><td>571.20 <b>(+53.38%)</b></td><td>184.70 <b>(-39.22%)</b></td><td>223.50 <b>(+51.31%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>645.20 (n/a)</td><td>429.44 (n/a)</td><td>372.40 (n/a)</td><td>303.90 (n/a)</td><td>147.71 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.55 (+16.16%)</td><td>0.30 (-14.32%)</td><td>0.25 <b>(-32.71%)</b></td><td>0.21 (+16.59%)</td><td>0.14 <b>(+29.91%)</b></td><td>615.00 (-14.23%)</td><td>481.24 (+17.62%)</td><td>517.10 <b>(+48.63%)</b></td><td>239.80 (-13.90%)</td><td>144.16 (-17.68%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.47 (n/a)</td><td>0.36 (n/a)</td><td>0.38 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>717.00 (n/a)</td><td>409.16 (n/a)</td><td>347.90 (n/a)</td><td>278.50 (n/a)</td><td>175.12 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (+14.94%)</td><td>0.01 (+13.40%)</td><td>0.02 <b>(+20.17%)</b></td><td>0.01 (-10.78%)</td><td>0.00 <b>(+38.11%)</b></td><td>651.60 (+12.09%)</td><td>352.38 (-5.97%)</td><td>258.50 (-16.77%)</td><td>230.00 (-13.01%)</td><td>175.69 <b>(+35.36%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>581.30 (n/a)</td><td>374.74 (n/a)</td><td>310.60 (n/a)</td><td>264.40 (n/a)</td><td>129.79 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 <b>(+32.44%)</b></td><td>0.02 <b>(+39.54%)</b></td><td>0.01 <b>(+66.89%)</b></td><td>0.01 <b>(+36.76%)</b></td><td>0.01 (+10.28%)</td><td>440.40 <b>(-26.88%)</b></td><td>299.72 <b>(-32.11%)</b></td><td>315.90 <b>(-40.09%)</b></td><td>172.10 <b>(-24.48%)</b></td><td>98.40 <b>(-41.68%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>602.30 (n/a)</td><td>441.46 (n/a)</td><td>527.30 (n/a)</td><td>227.90 (n/a)</td><td>168.73 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 <b>(-24.98%)</b></td><td>0.01 <b>(-20.99%)</b></td><td>0.01 <b>(-23.21%)</b></td><td>0.01 <b>(-26.91%)</b></td><td>0.00 (-5.62%)</td><td>552.00 <b>(+36.80%)</b></td><td>366.90 <b>(+30.83%)</b></td><td>334.70 <b>(+30.23%)</b></td><td>250.80 <b>(+33.26%)</b></td><td>129.91 <b>(+62.95%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>403.50 (n/a)</td><td>280.44 (n/a)</td><td>257.00 (n/a)</td><td>188.20 (n/a)</td><td>79.72 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.51 (-1.13%)</td><td>0.36 (-7.10%)</td><td>0.32 (-15.98%)</td><td>0.26 (+17.77%)</td><td>0.11 (-5.37%)</td><td>506.60 (-15.09%)</td><td>386.16 (+5.43%)</td><td>407.20 (+19.03%)</td><td>261.10 (+1.16%)</td><td>104.52 <b>(-22.47%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>596.60 (n/a)</td><td>366.28 (n/a)</td><td>342.10 (n/a)</td><td>258.10 (n/a)</td><td>134.81 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.57 <b>(+23.07%)</b></td><td>0.39 (-3.35%)</td><td>0.40 (-7.00%)</td><td>0.22 <b>(-34.59%)</b></td><td>0.16 <b>(+177.52%)</b></td><td>608.10 <b>(+52.90%)</b></td><td>395.28 (+18.70%)</td><td>333.70 (+7.51%)</td><td>229.80 (-18.74%)</td><td>174.46 <b>(+247.98%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.47 (n/a)</td><td>0.40 (n/a)</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.06 (n/a)</td><td>397.70 (n/a)</td><td>333.00 (n/a)</td><td>310.40 (n/a)</td><td>282.80 (n/a)</td><td>50.14 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.51 (+3.27%)</td><td>0.42 <b>(+25.20%)</b></td><td>0.47 <b>(+51.94%)</b></td><td>0.25 (+18.44%)</td><td>0.10 <b>(-24.17%)</b></td><td>528.10 (-15.57%)</td><td>331.90 <b>(-24.90%)</b></td><td>283.90 <b>(-34.19%)</b></td><td>261.20 (-3.19%)</td><td>111.01 <b>(-34.62%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>625.50 (n/a)</td><td>441.96 (n/a)</td><td>431.40 (n/a)</td><td>269.80 (n/a)</td><td>169.79 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.46 <b>(-28.60%)</b></td><td>0.36 (-14.26%)</td><td>0.32 <b>(-26.05%)</b></td><td>0.27 <b>(+30.40%)</b></td><td>0.09 <b>(-48.77%)</b></td><td>482.50 <b>(-23.32%)</b></td><td>378.50 (+5.05%)</td><td>414.50 <b>(+35.24%)</b></td><td>285.10 <b>(+40.03%)</b></td><td>85.68 <b>(-48.63%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.65 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>629.20 (n/a)</td><td>360.30 (n/a)</td><td>306.50 (n/a)</td><td>203.60 (n/a)</td><td>166.80 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.55 <b>(-22.13%)</b></td><td>0.41 <b>(-24.48%)</b></td><td>0.41 (-16.72%)</td><td>0.28 <b>(-33.32%)</b></td><td>0.10 (-19.85%)</td><td>465.70 <b>(+49.98%)</b></td><td>341.12 <b>(+33.63%)</b></td><td>326.10 <b>(+20.07%)</b></td><td>241.70 <b>(+28.43%)</b></td><td>87.17 <b>(+54.85%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.70 (n/a)</td><td>0.54 (n/a)</td><td>0.49 (n/a)</td><td>0.43 (n/a)</td><td>0.13 (n/a)</td><td>310.50 (n/a)</td><td>255.28 (n/a)</td><td>271.60 (n/a)</td><td>188.20 (n/a)</td><td>56.29 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (+10.42%)</td><td>0.01 (-13.81%)</td><td>0.01 <b>(-34.38%)</b></td><td>0.01 (-7.82%)</td><td>0.00 (+15.87%)</td><td>631.50 (+8.49%)</td><td>438.20 (+18.81%)</td><td>444.60 <b>(+52.36%)</b></td><td>244.80 (-9.43%)</td><td>151.62 (+14.09%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>582.10 (n/a)</td><td>368.82 (n/a)</td><td>291.80 (n/a)</td><td>270.30 (n/a)</td><td>132.89 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.02 (+4.89%)</td><td>0.01 (-5.09%)</td><td>0.01 <b>(-20.39%)</b></td><td>0.01 <b>(+28.77%)</b></td><td>0.00 (-3.31%)</td><td>468.10 <b>(-22.35%)</b></td><td>370.84 (+2.55%)</td><td>425.60 <b>(+25.58%)</b></td><td>240.70 (-4.67%)</td><td>102.50 <b>(-28.10%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>602.80 (n/a)</td><td>361.62 (n/a)</td><td>338.90 (n/a)</td><td>252.50 (n/a)</td><td>142.55 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.00 (-14.29%)</td><td>0.00 (-5.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-29.94%)</b></td><td>21353.13 (+16.86%)</td><td>13436.13 (+4.64%)</td><td>14829.01 (-8.98%)</td><td>7237.07 <b>(+32.09%)</b></td><td>5641.35 (-7.76%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18273.08 (n/a)</td><td>12839.75 (n/a)</td><td>16292.53 (n/a)</td><td>5478.93 (n/a)</td><td>6116.21 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+31.25%)</b></td><td>0.00 <b>(+175.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+12.85%)</td><td>22691.68 (+12.99%)</td><td>12672.56 (-17.43%)</td><td>7605.39 <b>(-59.72%)</b></td><td>6763.08 (-4.24%)</td><td>7566.05 <b>(+26.11%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20083.18 (n/a)</td><td>15348.50 (n/a)</td><td>18879.22 (n/a)</td><td>7062.33 (n/a)</td><td>5999.45 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>0.15 <b>(+75.89%)</b></td><td>0.12 <b>(+46.70%)</b></td><td>0.13 <b>(+69.35%)</b></td><td>0.08 (+4.37%)</td><td>0.04 <b>(+615.53%)</b></td><td>26607.02 (-4.17%)</td><td>19314.01 <b>(-25.68%)</b></td><td>15818.70 <b>(-40.95%)</b></td><td>13751.14 <b>(-43.18%)</b></td><td>6661.03 <b>(+306.29%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>27764.51 (n/a)</td><td>25986.49 (n/a)</td><td>26787.86 (n/a)</td><td>24199.30 (n/a)</td><td>1639.46 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.69 (+6.17%)</td><td>1.14 (+2.96%)</td><td>1.18 <b>(+20.08%)</b></td><td>0.65 <b>(-20.39%)</b></td><td>0.38 <b>(+23.70%)</b></td><td>801.40 <b>(+25.61%)</b></td><td>507.42 (+1.29%)</td><td>445.00 (-16.71%)</td><td>310.40 (-5.80%)</td><td>183.55 <b>(+52.91%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.59 (n/a)</td><td>1.10 (n/a)</td><td>0.98 (n/a)</td><td>0.82 (n/a)</td><td>0.31 (n/a)</td><td>638.00 (n/a)</td><td>500.96 (n/a)</td><td>534.30 (n/a)</td><td>329.50 (n/a)</td><td>120.04 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>3.17 (+16.79%)</td><td>1.85 <b>(+31.49%)</b></td><td>2.43 <b>(+65.89%)</b></td><td>0.30 <b>(-42.12%)</b></td><td>1.19 <b>(+29.47%)</b></td><td>3523.70 <b>(+72.76%)</b></td><td>1169.80 (+3.97%)</td><td>431.60 <b>(-39.72%)</b></td><td>330.80 (-14.37%)</td><td>1354.58 <b>(+73.16%)</b></td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>2.71 (n/a)</td><td>1.41 (n/a)</td><td>1.46 (n/a)</td><td>0.51 (n/a)</td><td>0.92 (n/a)</td><td>2039.60 (n/a)</td><td>1125.12 (n/a)</td><td>716.00 (n/a)</td><td>386.30 (n/a)</td><td>782.28 (n/a)</td>
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
<td><code>f13a48a</code> — 2026-09-17 23:25:21</td><td>1.79 (+1.78%)</td><td>1.35 (-0.59%)</td><td>1.32 (-9.53%)</td><td>0.92 (+3.38%)</td><td>0.37 (+11.28%)</td><td>570.20 (-3.27%)</td><td>411.34 (+1.30%)</td><td>397.20 (+10.55%)</td><td>292.70 (-1.75%)</td><td>114.76 (+1.37%)</td>
</tr>
<tr>
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.76 (n/a)</td><td>1.36 (n/a)</td><td>1.46 (n/a)</td><td>0.89 (n/a)</td><td>0.33 (n/a)</td><td>589.50 (n/a)</td><td>406.06 (n/a)</td><td>359.30 (n/a)</td><td>297.90 (n/a)</td><td>113.22 (n/a)</td>
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
