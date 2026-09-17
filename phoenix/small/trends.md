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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (-6.29%)</td><td>0.03 (+1.44%)</td><td>0.04 <b>(+31.84%)</b></td><td>0.02 (-5.90%)</td><td>0.01 (-16.82%)</td><td>556.00 (+6.27%)</td><td>375.16 (-2.75%)</td><td>319.70 <b>(-24.15%)</b></td><td>278.30 (+6.71%)</td><td>115.93 (-0.44%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.20 (n/a)</td><td>385.78 (n/a)</td><td>421.50 (n/a)</td><td>260.80 (n/a)</td><td>116.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.05 (-5.01%)</td><td>0.03 (+9.53%)</td><td>0.03 <b>(+25.49%)</b></td><td>0.03 <b>(+22.52%)</b></td><td>0.01 <b>(-25.11%)</b></td><td>468.80 (-18.37%)</td><td>372.26 (-14.00%)</td><td>414.40 <b>(-20.31%)</b></td><td>256.10 (+5.26%)</td><td>94.13 <b>(-36.83%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>574.30 (n/a)</td><td>432.86 (n/a)</td><td>520.00 (n/a)</td><td>243.30 (n/a)</td><td>149.02 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (-17.13%)</td><td>0.02 <b>(-26.84%)</b></td><td>0.02 <b>(-32.60%)</b></td><td>0.01 <b>(-66.66%)</b></td><td>0.01 (-6.91%)</td><td>2085.60 <b>(+199.96%)</b></td><td>789.48 <b>(+77.51%)</b></td><td>524.20 <b>(+48.37%)</b></td><td>293.20 <b>(+20.71%)</b></td><td>731.92 <b>(+266.55%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>695.30 (n/a)</td><td>444.74 (n/a)</td><td>353.30 (n/a)</td><td>242.90 (n/a)</td><td>199.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (+12.09%)</td><td>0.02 (-1.53%)</td><td>0.02 (-5.18%)</td><td>0.01 <b>(-32.29%)</b></td><td>0.01 <b>(+175.19%)</b></td><td>417.90 <b>(+47.67%)</b></td><td>273.96 (+7.76%)</td><td>267.20 (+5.45%)</td><td>196.90 (-10.78%)</td><td>86.17 <b>(+275.36%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>283.00 (n/a)</td><td>254.24 (n/a)</td><td>253.40 (n/a)</td><td>220.70 (n/a)</td><td>22.96 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (+7.81%)</td><td>0.02 <b>(-20.06%)</b></td><td>0.01 <b>(-37.20%)</b></td><td>0.01 <b>(-31.77%)</b></td><td>0.01 <b>(+84.23%)</b></td><td>565.60 <b>(+46.57%)</b></td><td>385.26 <b>(+35.80%)</b></td><td>421.20 <b>(+59.24%)</b></td><td>229.50 (-7.24%)</td><td>136.22 <b>(+135.92%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>385.90 (n/a)</td><td>283.70 (n/a)</td><td>264.50 (n/a)</td><td>247.40 (n/a)</td><td>57.74 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 <b>(-26.30%)</b></td><td>0.01 (-16.63%)</td><td>0.01 <b>(-43.06%)</b></td><td>0.01 <b>(+94.01%)</b></td><td>0.00 <b>(-41.39%)</b></td><td>536.60 <b>(-48.46%)</b></td><td>432.58 (-3.70%)</td><td>511.70 <b>(+75.60%)</b></td><td>285.10 <b>(+35.70%)</b></td><td>127.72 <b>(-62.33%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1041.20 (n/a)</td><td>449.18 (n/a)</td><td>291.40 (n/a)</td><td>210.10 (n/a)</td><td>339.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 <b>(-25.48%)</b></td><td>0.01 <b>(-31.94%)</b></td><td>0.01 <b>(-43.72%)</b></td><td>0.01 <b>(-43.72%)</b></td><td>0.01 (-7.71%)</td><td>812.30 <b>(+77.71%)</b></td><td>463.64 <b>(+59.82%)</b></td><td>455.50 <b>(+77.65%)</b></td><td>235.90 <b>(+34.19%)</b></td><td>226.02 <b>(+111.92%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>457.10 (n/a)</td><td>290.10 (n/a)</td><td>256.40 (n/a)</td><td>175.80 (n/a)</td><td>106.66 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (-3.01%)</td><td>0.01 <b>(-22.23%)</b></td><td>0.01 <b>(-43.29%)</b></td><td>0.01 (+0.15%)</td><td>0.00 (-9.81%)</td><td>528.60 (-0.15%)</td><td>438.78 <b>(+26.52%)</b></td><td>477.00 <b>(+76.34%)</b></td><td>249.60 (+3.10%)</td><td>114.02 (-8.99%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>529.40 (n/a)</td><td>346.82 (n/a)</td><td>270.50 (n/a)</td><td>242.10 (n/a)</td><td>125.28 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (-5.42%)</td><td>0.01 (-18.71%)</td><td>0.01 <b>(-31.61%)</b></td><td>0.01 (+6.29%)</td><td>0.00 (-3.99%)</td><td>603.50 (-5.92%)</td><td>445.06 <b>(+20.69%)</b></td><td>479.70 <b>(+46.21%)</b></td><td>249.70 (+5.72%)</td><td>132.51 (-15.76%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>641.50 (n/a)</td><td>368.76 (n/a)</td><td>328.10 (n/a)</td><td>236.20 (n/a)</td><td>157.30 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.60 (n/a)</td><td>371.00 (n/a)</td><td>300.50 (n/a)</td><td>251.20 (n/a)</td><td>139.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>484.70 (n/a)</td><td>408.86 (n/a)</td><td>396.60 (n/a)</td><td>302.40 (n/a)</td><td>75.37 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.30 (n/a)</td><td>376.24 (n/a)</td><td>345.70 (n/a)</td><td>247.10 (n/a)</td><td>124.36 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>478.90 (n/a)</td><td>408.62 (n/a)</td><td>434.30 (n/a)</td><td>308.90 (n/a)</td><td>75.30 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1908.80 (n/a)</td><td>786.92 (n/a)</td><td>483.40 (n/a)</td><td>463.40 (n/a)</td><td>629.54 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.60 (n/a)</td><td>399.40 (n/a)</td><td>373.30 (n/a)</td><td>291.90 (n/a)</td><td>110.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.08 <b>(+28.00%)</b></td><td>0.77 (+11.37%)</td><td>0.72 (+6.70%)</td><td>0.49 (+8.05%)</td><td>0.22 <b>(+35.82%)</b></td><td>937.50 (-7.44%)</td><td>640.16 (-8.74%)</td><td>635.40 (-6.28%)</td><td>424.10 <b>(-21.88%)</b></td><td>190.43 (-0.02%)</td><td>79.12 <b>(+28.00%)</b></td><td>56.06 (+11.37%)</td><td>52.80 (+6.70%)</td><td>35.79 (+8.05%)</td><td>15.93 <b>(+35.82%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.85 (n/a)</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.45 (n/a)</td><td>0.16 (n/a)</td><td>1012.90 (n/a)</td><td>701.46 (n/a)</td><td>678.00 (n/a)</td><td>542.90 (n/a)</td><td>190.48 (n/a)</td><td>61.81 (n/a)</td><td>50.34 (n/a)</td><td>49.49 (n/a)</td><td>33.13 (n/a)</td><td>11.73 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.92 <b>(-32.95%)</b></td><td>0.74 <b>(-32.06%)</b></td><td>0.85 (-13.88%)</td><td>0.36 <b>(-57.82%)</b></td><td>0.23 (-9.01%)</td><td>1806.10 <b>(+137.08%)</b></td><td>990.60 <b>(+59.22%)</b></td><td>772.50 (+16.13%)</td><td>715.70 <b>(+49.14%)</b></td><td>461.96 <b>(+245.76%)</b></td><td>93.77 <b>(-32.95%)</b></td><td>76.25 <b>(-32.06%)</b></td><td>86.88 (-13.88%)</td><td>37.16 <b>(-57.82%)</b></td><td>23.12 (-9.01%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.37 (n/a)</td><td>1.10 (n/a)</td><td>0.99 (n/a)</td><td>0.86 (n/a)</td><td>0.25 (n/a)</td><td>761.80 (n/a)</td><td>622.14 (n/a)</td><td>665.20 (n/a)</td><td>479.90 (n/a)</td><td>133.61 (n/a)</td><td>139.85 (n/a)</td><td>112.22 (n/a)</td><td>100.88 (n/a)</td><td>88.10 (n/a)</td><td>25.41 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.58 <b>(+32.85%)</b></td><td>1.26 <b>(+26.11%)</b></td><td>1.37 <b>(+35.51%)</b></td><td>0.95 <b>(+33.38%)</b></td><td>0.27 <b>(+38.38%)</b></td><td>796.70 <b>(-25.02%)</b></td><td>621.08 <b>(-20.38%)</b></td><td>550.50 <b>(-26.20%)</b></td><td>476.70 <b>(-24.73%)</b></td><td>139.70 (-19.70%)</td><td>175.99 <b>(+32.85%)</b></td><td>140.45 <b>(+26.11%)</b></td><td>152.39 <b>(+35.51%)</b></td><td>105.30 <b>(+33.38%)</b></td><td>30.10 <b>(+38.38%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.19 (n/a)</td><td>1.00 (n/a)</td><td>1.01 (n/a)</td><td>0.71 (n/a)</td><td>0.20 (n/a)</td><td>1062.60 (n/a)</td><td>780.08 (n/a)</td><td>745.90 (n/a)</td><td>633.30 (n/a)</td><td>173.98 (n/a)</td><td>132.47 (n/a)</td><td>111.37 (n/a)</td><td>112.46 (n/a)</td><td>78.94 (n/a)</td><td>21.75 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.17 (-11.75%)</td><td>0.96 (-7.47%)</td><td>0.98 (-15.35%)</td><td>0.61 <b>(+20.23%)</b></td><td>0.23 <b>(-27.49%)</b></td><td>1732.20 (-16.83%)</td><td>1157.06 (+1.49%)</td><td>1071.30 (+18.13%)</td><td>895.30 (+13.31%)</td><td>343.99 <b>(-35.78%)</b></td><td>149.92 (-11.75%)</td><td>122.98 (-7.47%)</td><td>125.28 (-15.35%)</td><td>77.48 <b>(+20.23%)</b></td><td>29.90 <b>(-27.49%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.33 (n/a)</td><td>1.04 (n/a)</td><td>1.16 (n/a)</td><td>0.50 (n/a)</td><td>0.32 (n/a)</td><td>2082.60 (n/a)</td><td>1140.10 (n/a)</td><td>906.90 (n/a)</td><td>790.10 (n/a)</td><td>535.65 (n/a)</td><td>169.87 (n/a)</td><td>132.91 (n/a)</td><td>148.00 (n/a)</td><td>64.45 (n/a)</td><td>41.24 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.43 <b>(-41.47%)</b></td><td>0.95 <b>(-43.31%)</b></td><td>1.25 <b>(-29.52%)</b></td><td>0.31 <b>(-62.72%)</b></td><td>0.53 (-10.83%)</td><td>3401.70 <b>(+168.27%)</b></td><td>1628.94 <b>(+127.96%)</b></td><td>840.20 <b>(+41.90%)</b></td><td>731.50 <b>(+70.87%)</b></td><td>1204.19 <b>(+269.16%)</b></td><td>183.48 <b>(-41.47%)</b></td><td>121.32 <b>(-43.31%)</b></td><td>159.75 <b>(-29.52%)</b></td><td>39.46 <b>(-62.72%)</b></td><td>67.70 (-10.83%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>2.45 (n/a)</td><td>1.67 (n/a)</td><td>1.77 (n/a)</td><td>0.83 (n/a)</td><td>0.59 (n/a)</td><td>1268.00 (n/a)</td><td>714.58 (n/a)</td><td>592.10 (n/a)</td><td>428.10 (n/a)</td><td>326.20 (n/a)</td><td>313.50 (n/a)</td><td>214.00 (n/a)</td><td>226.68 (n/a)</td><td>105.85 (n/a)</td><td>75.92 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.97 (+5.16%)</td><td>1.61 <b>(+32.64%)</b></td><td>1.69 (+18.15%)</td><td>1.27 <b>(+318.29%)</b></td><td>0.29 <b>(-57.48%)</b></td><td>827.90 <b>(-76.09%)</b></td><td>670.76 <b>(-51.26%)</b></td><td>619.00 (-15.36%)</td><td>533.00 (-4.91%)</td><td>125.73 <b>(-89.80%)</b></td><td>251.80 (+5.16%)</td><td>205.69 <b>(+32.64%)</b></td><td>216.85 (+18.15%)</td><td>162.12 <b>(+318.29%)</b></td><td>37.46 <b>(-57.48%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.87 (n/a)</td><td>1.21 (n/a)</td><td>1.43 (n/a)</td><td>0.30 (n/a)</td><td>0.69 (n/a)</td><td>3463.00 (n/a)</td><td>1376.14 (n/a)</td><td>731.30 (n/a)</td><td>560.50 (n/a)</td><td>1232.12 (n/a)</td><td>239.45 (n/a)</td><td>155.08 (n/a)</td><td>183.54 (n/a)</td><td>38.76 (n/a)</td><td>88.10 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.79 (-4.90%)</td><td>1.24 <b>(-23.60%)</b></td><td>1.24 <b>(-27.62%)</b></td><td>0.43 <b>(-65.45%)</b></td><td>0.50 <b>(+100.43%)</b></td><td>2420.20 <b>(+189.46%)</b></td><td>1082.56 <b>(+63.42%)</b></td><td>849.00 <b>(+38.16%)</b></td><td>586.30 (+5.15%)</td><td>756.06 <b>(+571.41%)</b></td><td>228.92 (-4.90%)</td><td>158.11 <b>(-23.60%)</b></td><td>158.09 <b>(-27.62%)</b></td><td>55.46 <b>(-65.45%)</b></td><td>64.50 <b>(+100.43%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.88 (n/a)</td><td>1.62 (n/a)</td><td>1.71 (n/a)</td><td>1.25 (n/a)</td><td>0.25 (n/a)</td><td>836.10 (n/a)</td><td>662.44 (n/a)</td><td>614.50 (n/a)</td><td>557.60 (n/a)</td><td>112.61 (n/a)</td><td>240.71 (n/a)</td><td>206.96 (n/a)</td><td>218.41 (n/a)</td><td>160.53 (n/a)</td><td>32.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.92 (+15.53%)</td><td>0.56 (-17.08%)</td><td>0.51 <b>(-28.20%)</b></td><td>0.37 <b>(-25.86%)</b></td><td>0.22 <b>(+65.92%)</b></td><td>975.40 <b>(+34.89%)</b></td><td>708.78 <b>(+28.99%)</b></td><td>706.80 <b>(+39.27%)</b></td><td>391.70 (-13.46%)</td><td>227.09 <b>(+94.60%)</b></td><td>42.83 (+15.53%)</td><td>26.17 (-17.08%)</td><td>23.74 <b>(-28.20%)</b></td><td>17.20 <b>(-25.86%)</b></td><td>10.15 <b>(+65.92%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.80 (n/a)</td><td>0.68 (n/a)</td><td>0.71 (n/a)</td><td>0.50 (n/a)</td><td>0.13 (n/a)</td><td>723.10 (n/a)</td><td>549.48 (n/a)</td><td>507.50 (n/a)</td><td>452.60 (n/a)</td><td>116.70 (n/a)</td><td>37.07 (n/a)</td><td>31.56 (n/a)</td><td>33.06 (n/a)</td><td>23.20 (n/a)</td><td>6.12 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>3.94 (-2.75%)</td><td>2.49 (+2.59%)</td><td>2.62 <b>(+39.20%)</b></td><td>1.04 (-5.11%)</td><td>1.30 (-6.38%)</td><td>2512.20 (+5.39%)</td><td>1393.34 (-2.14%)</td><td>999.60 <b>(-28.16%)</b></td><td>665.60 (+2.81%)</td><td>836.18 (+8.15%)</td><td>806.54 (-2.75%)</td><td>509.16 (+2.59%)</td><td>537.07 <b>(+39.20%)</b></td><td>213.71 (-5.11%)</td><td>266.92 (-6.38%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>4.05 (n/a)</td><td>2.42 (n/a)</td><td>1.88 (n/a)</td><td>1.10 (n/a)</td><td>1.39 (n/a)</td><td>2383.70 (n/a)</td><td>1423.80 (n/a)</td><td>1391.40 (n/a)</td><td>647.40 (n/a)</td><td>773.17 (n/a)</td><td>829.33 (n/a)</td><td>496.30 (n/a)</td><td>385.84 (n/a)</td><td>225.23 (n/a)</td><td>285.11 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.30 (n/a)</td><td>354.78 (n/a)</td><td>286.00 (n/a)</td><td>219.20 (n/a)</td><td>144.65 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>311.30 (n/a)</td><td>278.60 (n/a)</td><td>283.40 (n/a)</td><td>231.50 (n/a)</td><td>29.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.70 (n/a)</td><td>359.56 (n/a)</td><td>309.90 (n/a)</td><td>218.00 (n/a)</td><td>122.57 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1058.30 (n/a)</td><td>664.90 (n/a)</td><td>661.00 (n/a)</td><td>275.20 (n/a)</td><td>385.73 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>660.20 (n/a)</td><td>488.72 (n/a)</td><td>435.80 (n/a)</td><td>398.50 (n/a)</td><td>109.14 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>675.90 (n/a)</td><td>435.12 (n/a)</td><td>369.60 (n/a)</td><td>299.00 (n/a)</td><td>157.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.65 (+2.82%)</td><td>0.37 <b>(-22.68%)</b></td><td>0.35 <b>(-30.92%)</b></td><td>0.13 <b>(-39.17%)</b></td><td>0.19 (+16.31%)</td><td>1707.00 <b>(+64.39%)</b></td><td>787.86 <b>(+45.87%)</b></td><td>635.20 <b>(+44.76%)</b></td><td>337.90 (-2.76%)</td><td>529.65 <b>(+87.07%)</b></td><td>27.93 (+2.82%)</td><td>15.67 <b>(-22.68%)</b></td><td>14.86 <b>(-30.92%)</b></td><td>5.53 <b>(-39.17%)</b></td><td>7.99 (+16.31%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.64 (n/a)</td><td>0.47 (n/a)</td><td>0.50 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>1038.40 (n/a)</td><td>540.12 (n/a)</td><td>438.80 (n/a)</td><td>347.50 (n/a)</td><td>283.13 (n/a)</td><td>27.16 (n/a)</td><td>20.26 (n/a)</td><td>21.51 (n/a)</td><td>9.09 (n/a)</td><td>6.87 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.69 <b>(+45.18%)</b></td><td>0.37 (+4.38%)</td><td>0.35 (-16.32%)</td><td>0.13 (+0.71%)</td><td>0.25 <b>(+80.27%)</b></td><td>1758.40 (-0.70%)</td><td>957.18 <b>(+20.64%)</b></td><td>639.90 (+19.50%)</td><td>318.90 <b>(-31.12%)</b></td><td>699.80 <b>(+26.68%)</b></td><td>29.59 <b>(+45.18%)</b></td><td>15.76 (+4.38%)</td><td>14.75 (-16.32%)</td><td>5.37 (+0.71%)</td><td>10.73 <b>(+80.27%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.41 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>1770.80 (n/a)</td><td>793.44 (n/a)</td><td>535.50 (n/a)</td><td>463.00 (n/a)</td><td>552.43 (n/a)</td><td>20.38 (n/a)</td><td>15.10 (n/a)</td><td>17.62 (n/a)</td><td>5.33 (n/a)</td><td>5.95 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.31 (+0.91%)</td><td>0.31 (+0.32%)</td><td>0.31 (+0.03%)</td><td>0.30 (-0.51%)</td><td>0.00 <b>(+60.88%)</b></td><td>83694.10 (+0.51%)</td><td>82022.86 (-0.31%)</td><td>82161.50 (-0.03%)</td><td>80857.80 (-0.90%)</td><td>1123.02 <b>(+60.26%)</b></td><td>212.47 (+0.91%)</td><td>209.48 (+0.32%)</td><td>209.10 (+0.03%)</td><td>205.27 (-0.51%)</td><td>2.85 <b>(+60.87%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83270.60 (n/a)</td><td>82280.60 (n/a)</td><td>82188.40 (n/a)</td><td>81592.80 (n/a)</td><td>700.73 (n/a)</td><td>210.56 (n/a)</td><td>208.81 (n/a)</td><td>209.03 (n/a)</td><td>206.31 (n/a)</td><td>1.77 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.15 (-0.09%)</td><td>1.12 (-1.02%)</td><td>1.15 (+0.95%)</td><td>1.06 (-1.55%)</td><td>0.05 <b>(+44.63%)</b></td><td>23839.20 (+1.58%)</td><td>22593.44 (+1.11%)</td><td>21920.00 (-0.95%)</td><td>21896.60 (+0.09%)</td><td>948.79 <b>(+45.74%)</b></td><td>784.59 (-0.09%)</td><td>761.45 (-1.02%)</td><td>783.75 (+0.95%)</td><td>720.66 (-1.55%)</td><td>31.41 <b>(+44.63%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.15 (n/a)</td><td>1.13 (n/a)</td><td>1.14 (n/a)</td><td>1.07 (n/a)</td><td>0.03 (n/a)</td><td>23468.90 (n/a)</td><td>22346.14 (n/a)</td><td>22129.30 (n/a)</td><td>21877.80 (n/a)</td><td>651.02 (n/a)</td><td>785.26 (n/a)</td><td>769.31 (n/a)</td><td>776.34 (n/a)</td><td>732.03 (n/a)</td><td>21.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>4.41 (+4.86%)</td><td>3.36 (+5.45%)</td><td>3.60 (-12.96%)</td><td>1.96 <b>(+37.12%)</b></td><td>1.09 <b>(-20.07%)</b></td><td>4118.20 <b>(-27.07%)</b></td><td>2651.30 (-14.50%)</td><td>2239.70 (+14.90%)</td><td>1826.70 (-4.64%)</td><td>991.65 <b>(-41.60%)</b></td><td>1157.25 (+4.86%)</td><td>881.58 (+5.45%)</td><td>943.85 (-12.96%)</td><td>513.31 <b>(+37.12%)</b></td><td>286.89 <b>(-20.07%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>4.21 (n/a)</td><td>3.19 (n/a)</td><td>4.14 (n/a)</td><td>1.43 (n/a)</td><td>1.37 (n/a)</td><td>5647.00 (n/a)</td><td>3101.02 (n/a)</td><td>1949.30 (n/a)</td><td>1915.50 (n/a)</td><td>1697.98 (n/a)</td><td>1103.59 (n/a)</td><td>836.03 (n/a)</td><td>1084.44 (n/a)</td><td>374.35 (n/a)</td><td>358.91 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.31 (+10.74%)</td><td>0.23 (+14.27%)</td><td>0.21 (+3.78%)</td><td>0.18 <b>(+39.47%)</b></td><td>0.06 (-15.99%)</td><td>6833.70 <b>(-28.30%)</b></td><td>5581.26 (-16.72%)</td><td>5846.00 (-3.64%)</td><td>4022.70 (-9.69%)</td><td>1273.19 <b>(-45.02%)</b></td><td>16.68 (+10.74%)</td><td>12.58 (+14.27%)</td><td>11.48 (+3.78%)</td><td>9.82 <b>(+39.47%)</b></td><td>3.07 (-15.99%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>9531.20 (n/a)</td><td>6701.74 (n/a)</td><td>6066.80 (n/a)</td><td>4454.50 (n/a)</td><td>2315.62 (n/a)</td><td>15.07 (n/a)</td><td>11.01 (n/a)</td><td>11.06 (n/a)</td><td>7.04 (n/a)</td><td>3.65 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>3.95 (n/a)</td><td>3.61 (n/a)</td><td>3.56 (n/a)</td><td>3.39 (n/a)</td><td>0.22 (n/a)</td><td>3.95 (n/a)</td><td>3.60 (n/a)</td><td>3.56 (n/a)</td><td>3.39 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>6.85 (-3.88%)</td><td>6.09 (-2.50%)</td><td>5.91 (-11.21%)</td><td>5.72 (+19.80%)</td><td>0.47 <b>(-51.87%)</b></td><td>6.85 (-3.88%)</td><td>6.08 (-2.50%)</td><td>5.90 (-11.21%)</td><td>5.72 (+19.80%)</td><td>0.47 <b>(-51.87%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>7.13 (n/a)</td><td>6.24 (n/a)</td><td>6.65 (n/a)</td><td>4.77 (n/a)</td><td>0.97 (n/a)</td><td>7.13 (n/a)</td><td>6.24 (n/a)</td><td>6.65 (n/a)</td><td>4.77 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>13.75 (-4.56%)</td><td>10.48 (-7.52%)</td><td>9.75 <b>(-22.48%)</b></td><td>9.09 <b>(+21.90%)</b></td><td>1.93 <b>(-42.06%)</b></td><td>13.74 (-4.56%)</td><td>10.48 (-7.52%)</td><td>9.74 <b>(-22.48%)</b></td><td>9.09 <b>(+21.90%)</b></td><td>1.93 <b>(-42.06%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>14.40 (n/a)</td><td>11.33 (n/a)</td><td>12.57 (n/a)</td><td>7.46 (n/a)</td><td>3.32 (n/a)</td><td>14.40 (n/a)</td><td>11.33 (n/a)</td><td>12.57 (n/a)</td><td>7.45 (n/a)</td><td>3.32 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>3.91 (n/a)</td><td>3.81 (n/a)</td><td>3.80 (n/a)</td><td>3.78 (n/a)</td><td>0.05 (n/a)</td><td>3.91 (n/a)</td><td>3.81 (n/a)</td><td>3.80 (n/a)</td><td>3.78 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>7.49 (-0.42%)</td><td>6.52 (-0.56%)</td><td>6.96 (+3.10%)</td><td>5.26 (-7.20%)</td><td>0.95 (+18.80%)</td><td>7.49 (-0.42%)</td><td>6.52 (-0.56%)</td><td>6.95 (+3.10%)</td><td>5.26 (-7.20%)</td><td>0.95 (+18.80%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>7.52 (n/a)</td><td>6.56 (n/a)</td><td>6.75 (n/a)</td><td>5.67 (n/a)</td><td>0.80 (n/a)</td><td>7.52 (n/a)</td><td>6.55 (n/a)</td><td>6.75 (n/a)</td><td>5.67 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>12.78 (-8.81%)</td><td>8.52 <b>(-25.82%)</b></td><td>8.02 <b>(-40.21%)</b></td><td>5.82 <b>(-25.12%)</b></td><td>2.57 (-18.39%)</td><td>12.77 (-8.81%)</td><td>8.51 <b>(-25.82%)</b></td><td>8.02 <b>(-40.21%)</b></td><td>5.81 <b>(-25.12%)</b></td><td>2.57 (-18.39%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>14.01 (n/a)</td><td>11.48 (n/a)</td><td>13.42 (n/a)</td><td>7.77 (n/a)</td><td>3.15 (n/a)</td><td>14.00 (n/a)</td><td>11.48 (n/a)</td><td>13.41 (n/a)</td><td>7.76 (n/a)</td><td>3.14 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>2.76 (-1.28%)</td><td>2.17 (-5.95%)</td><td>1.91 <b>(-31.11%)</b></td><td>1.71 (+12.30%)</td><td>0.55 (-17.02%)</td><td>2.76 (-1.28%)</td><td>2.17 (-5.95%)</td><td>1.90 <b>(-31.11%)</b></td><td>1.70 (+12.30%)</td><td>0.54 (-17.02%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>2.80 (n/a)</td><td>2.31 (n/a)</td><td>2.77 (n/a)</td><td>1.52 (n/a)</td><td>0.66 (n/a)</td><td>2.79 (n/a)</td><td>2.30 (n/a)</td><td>2.76 (n/a)</td><td>1.52 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.58 (+2.80%)</td><td>0.39 <b>(+20.35%)</b></td><td>0.45 <b>(+38.04%)</b></td><td>0.07 <b>(-47.53%)</b></td><td>0.20 <b>(+27.94%)</b></td><td>0.57 (+2.80%)</td><td>0.38 <b>(+20.35%)</b></td><td>0.45 <b>(+38.04%)</b></td><td>0.07 <b>(-47.53%)</b></td><td>0.20 <b>(+27.94%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.56 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.55 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.73 (+1.39%)</td><td>0.26 (-16.15%)</td><td>0.08 <b>(-72.38%)</b></td><td>0.08 (-4.05%)</td><td>0.29 (+13.59%)</td><td>0.72 (+1.39%)</td><td>0.26 (-16.15%)</td><td>0.08 <b>(-72.38%)</b></td><td>0.08 (-4.05%)</td><td>0.28 (+13.59%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.72 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td><td>0.71 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>2.98 (+18.41%)</td><td>1.04 <b>(-28.07%)</b></td><td>0.45 <b>(-66.65%)</b></td><td>0.44 (-3.58%)</td><td>1.10 (+11.58%)</td><td>2.93 (+18.41%)</td><td>1.02 <b>(-28.07%)</b></td><td>0.44 <b>(-66.65%)</b></td><td>0.44 (-3.58%)</td><td>1.08 (+11.58%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>2.51 (n/a)</td><td>1.44 (n/a)</td><td>1.35 (n/a)</td><td>0.46 (n/a)</td><td>0.99 (n/a)</td><td>2.47 (n/a)</td><td>1.42 (n/a)</td><td>1.33 (n/a)</td><td>0.45 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2112.80 (n/a)</td><td>729.50 (n/a)</td><td>501.00 (n/a)</td><td>227.30 (n/a)</td><td>783.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.90 (n/a)</td><td>426.26 (n/a)</td><td>442.10 (n/a)</td><td>206.90 (n/a)</td><td>147.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1026.90 (n/a)</td><td>545.04 (n/a)</td><td>445.80 (n/a)</td><td>389.00 (n/a)</td><td>270.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>519.50 (n/a)</td><td>425.00 (n/a)</td><td>457.30 (n/a)</td><td>295.30 (n/a)</td><td>91.35 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.10 (n/a)</td><td>368.64 (n/a)</td><td>301.40 (n/a)</td><td>272.00 (n/a)</td><td>115.74 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>476.00 (n/a)</td><td>390.46 (n/a)</td><td>432.30 (n/a)</td><td>287.20 (n/a)</td><td>80.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (+11.95%)</td><td>0.02 (+12.66%)</td><td>0.02 <b>(+41.86%)</b></td><td>0.01 (-11.70%)</td><td>0.01 <b>(+21.57%)</b></td><td>596.90 (+13.26%)</td><td>379.02 (-8.56%)</td><td>334.20 <b>(-29.51%)</b></td><td>260.70 (-10.66%)</td><td>138.03 <b>(+26.29%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.00 (n/a)</td><td>414.48 (n/a)</td><td>474.10 (n/a)</td><td>291.80 (n/a)</td><td>109.30 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (+4.78%)</td><td>0.03 <b>(+21.88%)</b></td><td>0.03 <b>(+70.02%)</b></td><td>0.01 (+3.95%)</td><td>0.01 <b>(-20.41%)</b></td><td>566.40 (-3.80%)</td><td>336.40 <b>(-21.50%)</b></td><td>294.50 <b>(-41.19%)</b></td><td>243.70 (-4.54%)</td><td>130.65 (-17.54%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.80 (n/a)</td><td>428.52 (n/a)</td><td>500.80 (n/a)</td><td>255.30 (n/a)</td><td>158.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (-0.31%)</td><td>0.03 <b>(+26.19%)</b></td><td>0.03 <b>(+61.14%)</b></td><td>0.02 (-18.62%)</td><td>0.01 (+3.85%)</td><td>536.80 <b>(+22.87%)</b></td><td>314.60 (-18.66%)</td><td>270.20 <b>(-37.94%)</b></td><td>229.20 (+0.31%)</td><td>125.50 <b>(+39.36%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>436.90 (n/a)</td><td>386.76 (n/a)</td><td>435.40 (n/a)</td><td>228.50 (n/a)</td><td>90.06 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (-11.69%)</td><td>0.02 (-18.84%)</td><td>0.02 <b>(-35.02%)</b></td><td>0.01 <b>(-35.87%)</b></td><td>0.01 <b>(+51.27%)</b></td><td>654.60 <b>(+55.93%)</b></td><td>449.48 <b>(+38.50%)</b></td><td>477.70 <b>(+53.90%)</b></td><td>255.50 (+13.20%)</td><td>187.42 <b>(+152.65%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>419.80 (n/a)</td><td>324.54 (n/a)</td><td>310.40 (n/a)</td><td>225.70 (n/a)</td><td>74.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (-7.41%)</td><td>0.03 <b>(+23.81%)</b></td><td>0.03 <b>(+57.20%)</b></td><td>0.01 (-2.87%)</td><td>0.01 (-3.15%)</td><td>572.80 (+2.95%)</td><td>336.52 (-18.25%)</td><td>278.20 <b>(-36.40%)</b></td><td>265.00 (+7.99%)</td><td>132.41 (+17.36%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.40 (n/a)</td><td>411.64 (n/a)</td><td>437.40 (n/a)</td><td>245.40 (n/a)</td><td>112.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 <b>(+26.66%)</b></td><td>0.02 <b>(+78.28%)</b></td><td>0.02 <b>(+44.68%)</b></td><td>0.02 <b>(+317.57%)</b></td><td>0.00 <b>(-40.45%)</b></td><td>445.80 <b>(-76.05%)</b></td><td>359.86 <b>(-60.33%)</b></td><td>349.90 <b>(-30.89%)</b></td><td>289.40 <b>(-21.06%)</b></td><td>70.37 <b>(-89.20%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1861.60 (n/a)</td><td>907.18 (n/a)</td><td>506.30 (n/a)</td><td>366.60 (n/a)</td><td>651.35 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 <b>(+64.12%)</b></td><td>0.02 <b>(+48.12%)</b></td><td>0.03 <b>(+43.84%)</b></td><td>0.01 <b>(+100.24%)</b></td><td>0.01 <b>(+54.35%)</b></td><td>600.60 <b>(-50.06%)</b></td><td>380.70 <b>(-35.75%)</b></td><td>298.20 <b>(-30.47%)</b></td><td>215.00 <b>(-39.06%)</b></td><td>162.51 <b>(-53.69%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1202.60 (n/a)</td><td>592.50 (n/a)</td><td>428.90 (n/a)</td><td>352.80 (n/a)</td><td>350.90 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 <b>(+42.81%)</b></td><td>0.02 <b>(+28.93%)</b></td><td>0.02 <b>(+46.64%)</b></td><td>0.01 (+0.03%)</td><td>0.01 <b>(+172.02%)</b></td><td>645.80 (-0.03%)</td><td>435.22 (-17.61%)</td><td>354.70 <b>(-31.80%)</b></td><td>307.40 <b>(-29.98%)</b></td><td>141.31 <b>(+89.73%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>646.00 (n/a)</td><td>528.26 (n/a)</td><td>520.10 (n/a)</td><td>439.00 (n/a)</td><td>74.48 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (+1.52%)</td><td>0.02 <b>(-30.82%)</b></td><td>0.02 <b>(-42.50%)</b></td><td>0.01 <b>(-49.94%)</b></td><td>0.01 <b>(+171.02%)</b></td><td>588.10 <b>(+99.76%)</b></td><td>409.84 <b>(+62.33%)</b></td><td>415.50 <b>(+73.92%)</b></td><td>226.10 (-1.48%)</td><td>151.65 <b>(+440.08%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>294.40 (n/a)</td><td>252.48 (n/a)</td><td>238.90 (n/a)</td><td>229.50 (n/a)</td><td>28.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (-3.70%)</td><td>0.03 (+4.85%)</td><td>0.03 (-3.14%)</td><td>0.02 <b>(+64.17%)</b></td><td>0.00 <b>(-61.28%)</b></td><td>330.30 <b>(-39.08%)</b></td><td>292.54 (-13.00%)</td><td>287.00 (+3.24%)</td><td>244.80 (+3.86%)</td><td>32.95 <b>(-74.81%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.20 (n/a)</td><td>336.24 (n/a)</td><td>278.00 (n/a)</td><td>235.70 (n/a)</td><td>130.78 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 <b>(-28.12%)</b></td><td>0.02 <b>(-28.62%)</b></td><td>0.02 <b>(-42.03%)</b></td><td>0.01 (-14.88%)</td><td>0.01 (-18.39%)</td><td>586.10 (+17.48%)</td><td>444.72 <b>(+41.16%)</b></td><td>531.20 <b>(+72.47%)</b></td><td>279.50 <b>(+39.12%)</b></td><td>146.22 <b>(+27.69%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.90 (n/a)</td><td>315.04 (n/a)</td><td>308.00 (n/a)</td><td>200.90 (n/a)</td><td>114.52 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (-13.21%)</td><td>0.02 (+11.01%)</td><td>0.02 (-12.79%)</td><td>0.02 <b>(+92.09%)</b></td><td>0.01 <b>(-21.93%)</b></td><td>525.40 <b>(-47.94%)</b></td><td>399.98 <b>(-23.20%)</b></td><td>483.90 (+14.67%)</td><td>226.20 (+15.23%)</td><td>147.95 <b>(-52.76%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1009.20 (n/a)</td><td>520.78 (n/a)</td><td>422.00 (n/a)</td><td>196.30 (n/a)</td><td>313.20 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (+12.06%)</td><td>0.02 (+14.46%)</td><td>0.02 (+4.33%)</td><td>0.01 (-2.69%)</td><td>0.01 <b>(+23.83%)</b></td><td>625.80 (+2.76%)</td><td>445.40 (-9.91%)</td><td>504.90 (-4.14%)</td><td>248.10 (-10.79%)</td><td>153.09 (+13.40%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.00 (n/a)</td><td>494.38 (n/a)</td><td>526.70 (n/a)</td><td>278.10 (n/a)</td><td>135.00 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 <b>(+41.46%)</b></td><td>0.02 (+19.84%)</td><td>0.02 (+8.27%)</td><td>0.01 <b>(+89.68%)</b></td><td>0.01 <b>(+27.19%)</b></td><td>1130.70 <b>(-47.28%)</b></td><td>614.98 <b>(-27.53%)</b></td><td>516.80 (-7.63%)</td><td>302.20 <b>(-29.31%)</b></td><td>322.99 <b>(-55.70%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2144.80 (n/a)</td><td>848.60 (n/a)</td><td>559.50 (n/a)</td><td>427.50 (n/a)</td><td>729.06 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.12 <b>(+35.31%)</b></td><td>0.09 <b>(+33.41%)</b></td><td>0.10 <b>(+63.39%)</b></td><td>0.04 (-7.73%)</td><td>0.03 <b>(+43.30%)</b></td><td>553.20 (+8.39%)</td><td>303.70 <b>(-20.89%)</b></td><td>249.30 <b>(-38.81%)</b></td><td>201.90 <b>(-26.10%)</b></td><td>141.55 <b>(+32.72%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>510.40 (n/a)</td><td>383.88 (n/a)</td><td>407.40 (n/a)</td><td>273.20 (n/a)</td><td>106.65 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.18 (+10.48%)</td><td>0.16 <b>(+40.93%)</b></td><td>0.16 <b>(+61.33%)</b></td><td>0.15 <b>(+87.30%)</b></td><td>0.02 <b>(-59.82%)</b></td><td>281.30 <b>(-46.61%)</b></td><td>256.90 <b>(-34.74%)</b></td><td>252.00 <b>(-38.02%)</b></td><td>222.60 (-9.48%)</td><td>24.45 <b>(-80.59%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>526.90 (n/a)</td><td>393.64 (n/a)</td><td>406.60 (n/a)</td><td>245.90 (n/a)</td><td>125.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 <b>(+31.88%)</b></td><td>0.02 (+17.74%)</td><td>0.02 (+19.44%)</td><td>0.01 (-3.63%)</td><td>0.00 <b>(+92.00%)</b></td><td>431.70 (+3.75%)</td><td>280.28 (-11.75%)</td><td>246.10 (-16.26%)</td><td>215.20 <b>(-24.17%)</b></td><td>86.65 <b>(+56.19%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>416.10 (n/a)</td><td>317.60 (n/a)</td><td>293.90 (n/a)</td><td>283.80 (n/a)</td><td>55.47 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 (-10.00%)</td><td>0.03 (+3.39%)</td><td>0.03 (+2.78%)</td><td>0.02 (-7.94%)</td><td>0.01 (-11.71%)</td><td>516.10 (+8.63%)</td><td>310.38 (-3.68%)</td><td>256.40 (-2.73%)</td><td>240.60 (+11.13%)</td><td>116.83 (+6.97%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>475.10 (n/a)</td><td>322.24 (n/a)</td><td>263.60 (n/a)</td><td>216.50 (n/a)</td><td>109.22 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.05 (+7.76%)</td><td>0.04 <b>(+22.73%)</b></td><td>0.04 (+7.06%)</td><td>0.03 <b>(+317.21%)</b></td><td>0.01 <b>(-38.37%)</b></td><td>486.50 <b>(-76.03%)</b></td><td>347.78 <b>(-49.60%)</b></td><td>299.40 (-6.58%)</td><td>256.40 (-7.20%)</td><td>99.46 <b>(-86.83%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2029.90 (n/a)</td><td>690.00 (n/a)</td><td>320.50 (n/a)</td><td>276.30 (n/a)</td><td>755.17 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (+15.76%)</td><td>0.02 (-14.75%)</td><td>0.02 <b>(-21.83%)</b></td><td>0.01 <b>(-26.60%)</b></td><td>0.01 <b>(+68.19%)</b></td><td>651.90 <b>(+36.24%)</b></td><td>499.98 <b>(+29.65%)</b></td><td>536.40 <b>(+27.93%)</b></td><td>218.40 (-13.61%)</td><td>164.95 <b>(+84.28%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.50 (n/a)</td><td>385.64 (n/a)</td><td>419.30 (n/a)</td><td>252.80 (n/a)</td><td>89.51 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 <b>(-27.13%)</b></td><td>0.02 (-14.26%)</td><td>0.02 (-1.22%)</td><td>0.02 (-10.85%)</td><td>0.00 <b>(-59.27%)</b></td><td>537.40 (+12.17%)</td><td>451.16 (+12.39%)</td><td>448.30 (+1.22%)</td><td>377.10 <b>(+37.23%)</b></td><td>57.00 <b>(-38.75%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>479.10 (n/a)</td><td>401.42 (n/a)</td><td>442.90 (n/a)</td><td>274.80 (n/a)</td><td>93.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 <b>(+24.22%)</b></td><td>0.03 <b>(+49.67%)</b></td><td>0.03 <b>(+75.11%)</b></td><td>0.02 <b>(+22.66%)</b></td><td>0.01 <b>(+20.77%)</b></td><td>524.10 (-18.48%)</td><td>294.60 <b>(-32.97%)</b></td><td>255.80 <b>(-42.90%)</b></td><td>194.50 (-19.50%)</td><td>132.64 (-15.14%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>642.90 (n/a)</td><td>439.48 (n/a)</td><td>448.00 (n/a)</td><td>241.60 (n/a)</td><td>156.31 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (+5.88%)</td><td>0.03 (+14.13%)</td><td>0.03 <b>(+34.93%)</b></td><td>0.01 <b>(-26.04%)</b></td><td>0.01 <b>(+23.42%)</b></td><td>720.50 <b>(+35.20%)</b></td><td>422.38 (-7.27%)</td><td>363.90 <b>(-25.89%)</b></td><td>261.30 (-5.53%)</td><td>177.36 <b>(+74.04%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.90 (n/a)</td><td>455.48 (n/a)</td><td>491.00 (n/a)</td><td>276.60 (n/a)</td><td>101.91 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 (+19.11%)</td><td>0.03 (+10.74%)</td><td>0.03 (+0.73%)</td><td>0.02 (+5.47%)</td><td>0.01 <b>(+25.96%)</b></td><td>532.10 (-5.19%)</td><td>353.14 (-7.84%)</td><td>299.40 (-0.73%)</td><td>231.60 (-16.06%)</td><td>129.99 (+1.36%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.20 (n/a)</td><td>383.18 (n/a)</td><td>301.60 (n/a)</td><td>275.90 (n/a)</td><td>128.25 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.05 <b>(+72.94%)</b></td><td>0.03 <b>(+33.13%)</b></td><td>0.03 <b>(+55.23%)</b></td><td>0.01 <b>(-51.27%)</b></td><td>0.02 <b>(+146.01%)</b></td><td>1307.60 <b>(+105.21%)</b></td><td>495.94 (+9.81%)</td><td>318.20 <b>(-35.57%)</b></td><td>177.80 <b>(-42.16%)</b></td><td>463.25 <b>(+236.44%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.20 (n/a)</td><td>451.62 (n/a)</td><td>493.90 (n/a)</td><td>307.40 (n/a)</td><td>137.69 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 <b>(+24.28%)</b></td><td>0.02 (-0.19%)</td><td>0.02 (+5.52%)</td><td>0.01 <b>(-38.46%)</b></td><td>0.01 <b>(+81.73%)</b></td><td>824.10 <b>(+62.48%)</b></td><td>473.40 (+13.00%)</td><td>434.50 (-5.23%)</td><td>230.30 (-19.53%)</td><td>217.77 <b>(+138.02%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.20 (n/a)</td><td>418.94 (n/a)</td><td>458.50 (n/a)</td><td>286.20 (n/a)</td><td>91.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.03 <b>(-54.04%)</b></td><td>0.02 <b>(-26.42%)</b></td><td>0.02 (-0.14%)</td><td>0.01 <b>(+175.27%)</b></td><td>0.01 <b>(-75.81%)</b></td><td>673.80 <b>(-63.67%)</b></td><td>465.88 <b>(-26.49%)</b></td><td>445.50 (+0.13%)</td><td>337.00 <b>(+117.56%)</b></td><td>127.07 <b>(-81.71%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1854.70 (n/a)</td><td>633.80 (n/a)</td><td>444.90 (n/a)</td><td>154.90 (n/a)</td><td>694.72 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.04 <b>(+56.48%)</b></td><td>0.02 (+7.70%)</td><td>0.02 (-6.50%)</td><td>0.02 (-8.50%)</td><td>0.01 <b>(+195.54%)</b></td><td>541.10 (+9.29%)</td><td>426.24 (+1.42%)</td><td>456.80 (+6.95%)</td><td>213.70 <b>(-36.08%)</b></td><td>124.71 <b>(+91.10%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>495.10 (n/a)</td><td>420.28 (n/a)</td><td>427.10 (n/a)</td><td>334.30 (n/a)</td><td>65.26 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.39 (+4.13%)</td><td>0.30 (+3.76%)</td><td>0.36 (+13.66%)</td><td>0.18 (-13.92%)</td><td>0.11 <b>(+49.77%)</b></td><td>558.10 (+16.17%)</td><td>376.34 (+3.87%)</td><td>272.00 (-12.03%)</td><td>253.90 (-3.97%)</td><td>157.62 <b>(+62.61%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.32 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>480.40 (n/a)</td><td>362.32 (n/a)</td><td>309.20 (n/a)</td><td>264.40 (n/a)</td><td>96.93 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.53 <b>(+69.58%)</b></td><td>0.32 <b>(+41.57%)</b></td><td>0.32 <b>(+70.88%)</b></td><td>0.18 (+2.47%)</td><td>0.14 <b>(+132.67%)</b></td><td>538.20 (-2.41%)</td><td>353.58 <b>(-22.18%)</b></td><td>304.10 <b>(-41.47%)</b></td><td>184.50 <b>(-41.05%)</b></td><td>146.49 <b>(+37.29%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>551.50 (n/a)</td><td>454.34 (n/a)</td><td>519.60 (n/a)</td><td>313.00 (n/a)</td><td>106.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.53 <b>(+28.38%)</b></td><td>0.24 <b>(-23.84%)</b></td><td>0.18 <b>(-44.66%)</b></td><td>0.14 <b>(-27.67%)</b></td><td>0.16 <b>(+99.83%)</b></td><td>708.10 <b>(+38.27%)</b></td><td>506.04 <b>(+53.41%)</b></td><td>531.70 <b>(+80.73%)</b></td><td>185.20 <b>(-22.12%)</b></td><td>195.69 <b>(+83.78%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>512.10 (n/a)</td><td>329.86 (n/a)</td><td>294.20 (n/a)</td><td>237.80 (n/a)</td><td>106.48 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.26 (-3.35%)</td><td>0.18 (-2.17%)</td><td>0.15 (-0.10%)</td><td>0.11 (-4.45%)</td><td>0.07 (+4.55%)</td><td>663.60 (+4.67%)</td><td>452.72 (+3.71%)</td><td>480.70 (+0.10%)</td><td>285.80 (+3.48%)</td><td>162.74 (+10.50%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>634.00 (n/a)</td><td>436.52 (n/a)</td><td>480.20 (n/a)</td><td>276.20 (n/a)</td><td>147.28 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.29 (+9.94%)</td><td>0.21 <b>(+24.05%)</b></td><td>0.24 <b>(+43.75%)</b></td><td>0.10 <b>(+139.16%)</b></td><td>0.09 (-5.20%)</td><td>744.20 <b>(-58.19%)</b></td><td>427.78 <b>(-37.72%)</b></td><td>306.70 <b>(-30.42%)</b></td><td>253.80 (-9.06%)</td><td>219.53 <b>(-65.04%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.09 (n/a)</td><td>1780.00 (n/a)</td><td>686.84 (n/a)</td><td>440.80 (n/a)</td><td>279.10 (n/a)</td><td>627.95 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.28 <b>(-27.55%)</b></td><td>0.18 (-17.72%)</td><td>0.17 <b>(-27.62%)</b></td><td>0.04 (-2.04%)</td><td>0.10 <b>(-24.33%)</b></td><td>1949.10 (+2.09%)</td><td>678.48 (+8.61%)</td><td>440.30 <b>(+38.20%)</b></td><td>266.00 <b>(+38.04%)</b></td><td>716.57 (-1.13%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.38 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>0.13 (n/a)</td><td>1909.20 (n/a)</td><td>624.70 (n/a)</td><td>318.60 (n/a)</td><td>192.70 (n/a)</td><td>724.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.60 <b>(+48.22%)</b></td><td>0.37 <b>(+38.63%)</b></td><td>0.39 <b>(+48.09%)</b></td><td>0.17 <b>(+174.26%)</b></td><td>0.17 <b>(+22.33%)</b></td><td>761.30 <b>(-63.54%)</b></td><td>428.20 <b>(-44.22%)</b></td><td>340.20 <b>(-32.47%)</b></td><td>219.10 <b>(-32.52%)</b></td><td>216.27 <b>(-70.98%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.40 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>0.14 (n/a)</td><td>2087.90 (n/a)</td><td>767.64 (n/a)</td><td>503.80 (n/a)</td><td>324.70 (n/a)</td><td>745.24 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.43 (+7.15%)</td><td>0.33 (+6.99%)</td><td>0.35 <b>(+27.66%)</b></td><td>0.20 (-17.37%)</td><td>0.10 <b>(+42.03%)</b></td><td>645.20 <b>(+21.03%)</b></td><td>429.44 (-2.11%)</td><td>372.40 <b>(-21.67%)</b></td><td>303.90 (-6.66%)</td><td>147.71 <b>(+57.30%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>533.10 (n/a)</td><td>438.68 (n/a)</td><td>475.40 (n/a)</td><td>325.60 (n/a)</td><td>93.91 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.47 <b>(+24.43%)</b></td><td>0.36 <b>(+35.38%)</b></td><td>0.38 <b>(+54.00%)</b></td><td>0.18 (-14.13%)</td><td>0.11 <b>(+59.91%)</b></td><td>717.00 (+16.45%)</td><td>409.16 <b>(-21.25%)</b></td><td>347.90 <b>(-35.07%)</b></td><td>278.50 (-19.65%)</td><td>175.12 <b>(+70.95%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.07 (n/a)</td><td>615.70 (n/a)</td><td>519.56 (n/a)</td><td>535.80 (n/a)</td><td>346.60 (n/a)</td><td>102.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (-19.52%)</td><td>0.01 (+1.01%)</td><td>0.01 <b>(+30.91%)</b></td><td>0.01 (-0.33%)</td><td>0.00 <b>(-34.31%)</b></td><td>581.30 (+0.33%)</td><td>374.74 (-7.28%)</td><td>310.60 <b>(-23.61%)</b></td><td>264.40 <b>(+24.25%)</b></td><td>129.79 (-19.28%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.40 (n/a)</td><td>404.18 (n/a)</td><td>406.60 (n/a)</td><td>212.80 (n/a)</td><td>160.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (-3.42%)</td><td>0.01 (-6.69%)</td><td>0.01 (-0.46%)</td><td>0.01 (-0.48%)</td><td>0.00 (-12.97%)</td><td>602.30 (+0.48%)</td><td>441.46 (+3.84%)</td><td>527.30 (+0.46%)</td><td>227.90 (+3.50%)</td><td>168.73 (-5.79%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.40 (n/a)</td><td>425.12 (n/a)</td><td>524.90 (n/a)</td><td>220.20 (n/a)</td><td>179.10 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 (+2.60%)</td><td>0.02 <b>(+23.16%)</b></td><td>0.02 <b>(+95.35%)</b></td><td>0.01 <b>(+54.13%)</b></td><td>0.00 <b>(-40.62%)</b></td><td>403.50 <b>(-35.12%)</b></td><td>280.44 <b>(-32.28%)</b></td><td>257.00 <b>(-48.81%)</b></td><td>188.20 (-2.54%)</td><td>79.72 <b>(-59.99%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.90 (n/a)</td><td>414.10 (n/a)</td><td>502.10 (n/a)</td><td>193.10 (n/a)</td><td>199.25 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.51 (-8.36%)</td><td>0.39 (-13.15%)</td><td>0.39 (-16.67%)</td><td>0.22 <b>(-20.29%)</b></td><td>0.11 (+2.57%)</td><td>596.60 <b>(+25.44%)</b></td><td>366.28 (+17.99%)</td><td>342.10 (+19.99%)</td><td>258.10 (+9.09%)</td><td>134.81 <b>(+40.47%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.56 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.28 (n/a)</td><td>0.11 (n/a)</td><td>475.60 (n/a)</td><td>310.44 (n/a)</td><td>285.10 (n/a)</td><td>236.60 (n/a)</td><td>95.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.47 <b>(-27.79%)</b></td><td>0.40 (-17.48%)</td><td>0.43 (-15.81%)</td><td>0.33 (+12.52%)</td><td>0.06 <b>(-56.18%)</b></td><td>397.70 (-11.13%)</td><td>333.00 (+14.76%)</td><td>310.40 (+18.79%)</td><td>282.80 <b>(+38.49%)</b></td><td>50.14 <b>(-47.27%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.65 (n/a)</td><td>0.49 (n/a)</td><td>0.51 (n/a)</td><td>0.30 (n/a)</td><td>0.13 (n/a)</td><td>447.50 (n/a)</td><td>290.16 (n/a)</td><td>261.30 (n/a)</td><td>204.20 (n/a)</td><td>95.09 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.49 <b>(+69.75%)</b></td><td>0.34 <b>(+48.23%)</b></td><td>0.31 <b>(+22.52%)</b></td><td>0.21 <b>(+69.63%)</b></td><td>0.13 <b>(+94.22%)</b></td><td>625.50 <b>(-41.05%)</b></td><td>441.96 <b>(-30.54%)</b></td><td>431.40 (-18.37%)</td><td>269.80 <b>(-41.08%)</b></td><td>169.79 <b>(-32.74%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>1061.10 (n/a)</td><td>636.26 (n/a)</td><td>528.50 (n/a)</td><td>457.90 (n/a)</td><td>252.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.65 (+11.31%)</td><td>0.43 (-1.63%)</td><td>0.43 (-2.63%)</td><td>0.21 (-0.38%)</td><td>0.17 <b>(+20.75%)</b></td><td>629.20 (+0.38%)</td><td>360.30 (+4.25%)</td><td>306.50 (+2.68%)</td><td>203.60 (-10.15%)</td><td>166.80 (+3.77%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.58 (n/a)</td><td>0.43 (n/a)</td><td>0.44 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>626.80 (n/a)</td><td>345.60 (n/a)</td><td>298.50 (n/a)</td><td>226.60 (n/a)</td><td>160.73 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.70 <b>(+33.60%)</b></td><td>0.54 <b>(+29.86%)</b></td><td>0.49 (+7.69%)</td><td>0.43 <b>(+63.67%)</b></td><td>0.13 (+6.24%)</td><td>310.50 <b>(-38.91%)</b></td><td>255.28 <b>(-25.67%)</b></td><td>271.60 (-7.15%)</td><td>188.20 <b>(-25.17%)</b></td><td>56.29 <b>(-49.98%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.53 (n/a)</td><td>0.42 (n/a)</td><td>0.45 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>508.30 (n/a)</td><td>343.42 (n/a)</td><td>292.50 (n/a)</td><td>251.50 (n/a)</td><td>112.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 <b>(-21.19%)</b></td><td>0.01 (+0.46%)</td><td>0.01 <b>(+77.89%)</b></td><td>0.01 (-8.34%)</td><td>0.00 <b>(-40.10%)</b></td><td>582.10 (+9.09%)</td><td>368.82 (-8.87%)</td><td>291.80 <b>(-43.78%)</b></td><td>270.30 <b>(+26.90%)</b></td><td>132.89 <b>(-20.19%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>533.60 (n/a)</td><td>404.72 (n/a)</td><td>519.00 (n/a)</td><td>213.00 (n/a)</td><td>166.51 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.02 <b>(-26.30%)</b></td><td>0.01 (-5.76%)</td><td>0.01 (+14.28%)</td><td>0.01 <b>(-27.86%)</b></td><td>0.00 <b>(-26.00%)</b></td><td>602.80 <b>(+38.61%)</b></td><td>361.62 (+6.52%)</td><td>338.90 (-12.47%)</td><td>252.50 <b>(+35.68%)</b></td><td>142.55 <b>(+42.53%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>434.90 (n/a)</td><td>339.50 (n/a)</td><td>387.20 (n/a)</td><td>186.10 (n/a)</td><td>100.01 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.00 (+0.00%)</td><td>0.00 (-0.00%)</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-14.37%)</td><td>18273.08 (-7.13%)</td><td>12839.75 (-8.20%)</td><td>16292.53 (-12.86%)</td><td>5478.93 (-4.45%)</td><td>6116.21 (-16.76%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19677.02 (n/a)</td><td>13987.29 (n/a)</td><td>18697.33 (n/a)</td><td>5733.88 (n/a)</td><td>7347.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.00 (-7.69%)</td><td>0.00 <b>(-23.81%)</b></td><td>0.00 <b>(-55.56%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (+4.15%)</td><td>20083.18 (+11.85%)</td><td>15348.50 <b>(+30.88%)</b></td><td>18879.22 <b>(+104.85%)</b></td><td>7062.33 (+9.33%)</td><td>5999.45 (+11.55%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17954.73 (n/a)</td><td>11727.11 (n/a)</td><td>9216.11 (n/a)</td><td>6459.78 (n/a)</td><td>5378.28 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>0.09 <b>(-44.32%)</b></td><td>0.08 <b>(-39.56%)</b></td><td>0.08 <b>(-44.82%)</b></td><td>0.08 (-13.12%)</td><td>0.01 <b>(-81.11%)</b></td><td>27764.51 (+15.03%)</td><td>25986.49 <b>(+58.72%)</b></td><td>26787.86 <b>(+81.25%)</b></td><td>24199.30 <b>(+79.69%)</b></td><td>1639.46 <b>(-62.86%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>24135.86 (n/a)</td><td>16372.17 (n/a)</td><td>14779.36 (n/a)</td><td>13467.34 (n/a)</td><td>4414.26 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.59 (+13.24%)</td><td>1.10 (+10.89%)</td><td>0.98 (+2.56%)</td><td>0.82 (+4.76%)</td><td>0.31 <b>(+26.81%)</b></td><td>638.00 (-4.55%)</td><td>500.96 (-8.52%)</td><td>534.30 (-2.50%)</td><td>329.50 (-11.71%)</td><td>120.04 (+8.96%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.40 (n/a)</td><td>1.00 (n/a)</td><td>0.96 (n/a)</td><td>0.78 (n/a)</td><td>0.24 (n/a)</td><td>668.40 (n/a)</td><td>547.62 (n/a)</td><td>548.00 (n/a)</td><td>373.20 (n/a)</td><td>110.17 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>2.71 (+5.51%)</td><td>1.41 <b>(-30.29%)</b></td><td>1.46 <b>(-36.38%)</b></td><td>0.51 <b>(-53.54%)</b></td><td>0.92 <b>(+45.62%)</b></td><td>2039.60 <b>(+115.24%)</b></td><td>1125.12 <b>(+95.70%)</b></td><td>716.00 <b>(+57.16%)</b></td><td>386.30 (-5.23%)</td><td>782.28 <b>(+241.37%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>2.57 (n/a)</td><td>2.02 (n/a)</td><td>2.30 (n/a)</td><td>1.11 (n/a)</td><td>0.63 (n/a)</td><td>947.60 (n/a)</td><td>574.92 (n/a)</td><td>455.60 (n/a)</td><td>407.60 (n/a)</td><td>229.15 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 21:52:10</td><td>1.76 (-10.88%)</td><td>1.36 <b>(+29.48%)</b></td><td>1.46 <b>(+65.90%)</b></td><td>0.89 <b>(+42.91%)</b></td><td>0.33 <b>(-38.09%)</b></td><td>589.50 <b>(-30.02%)</b></td><td>406.06 <b>(-29.61%)</b></td><td>359.30 <b>(-39.72%)</b></td><td>297.90 (+12.20%)</td><td>113.22 <b>(-45.37%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.98 (n/a)</td><td>1.05 (n/a)</td><td>0.88 (n/a)</td><td>0.62 (n/a)</td><td>0.53 (n/a)</td><td>842.40 (n/a)</td><td>576.90 (n/a)</td><td>596.10 (n/a)</td><td>265.50 (n/a)</td><td>207.26 (n/a)</td>
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
