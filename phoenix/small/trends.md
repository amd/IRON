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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.05 (-19.19%)</td><td>0.03 (-14.26%)</td><td>0.03 <b>(-30.87%)</b></td><td>0.02 <b>(+20.10%)</b></td><td>0.01 <b>(-32.64%)</b></td><td>523.20 (-16.73%)</td><td>385.78 (+7.03%)</td><td>421.50 <b>(+44.65%)</b></td><td>260.80 <b>(+23.72%)</b></td><td>116.45 <b>(-33.41%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>628.30 (n/a)</td><td>360.44 (n/a)</td><td>291.40 (n/a)</td><td>210.80 (n/a)</td><td>174.87 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.05 (-3.87%)</td><td>0.03 (-12.22%)</td><td>0.02 (-16.02%)</td><td>0.02 (-10.45%)</td><td>0.01 (-6.81%)</td><td>574.30 (+11.67%)</td><td>432.86 (+14.70%)</td><td>520.00 (+19.07%)</td><td>243.30 (+4.06%)</td><td>149.02 (+14.86%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.30 (n/a)</td><td>377.40 (n/a)</td><td>436.70 (n/a)</td><td>233.80 (n/a)</td><td>129.74 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.05 (+2.53%)</td><td>0.03 (+0.60%)</td><td>0.03 <b>(+34.04%)</b></td><td>0.02 <b>(-24.31%)</b></td><td>0.01 <b>(+24.71%)</b></td><td>695.30 <b>(+32.11%)</b></td><td>444.74 (+7.62%)</td><td>353.30 <b>(-25.40%)</b></td><td>242.90 (-2.49%)</td><td>199.68 <b>(+68.71%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.30 (n/a)</td><td>413.26 (n/a)</td><td>473.60 (n/a)</td><td>249.10 (n/a)</td><td>118.36 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (+2.40%)</td><td>0.02 (+6.53%)</td><td>0.02 (-3.15%)</td><td>0.02 <b>(+41.61%)</b></td><td>0.00 <b>(-51.68%)</b></td><td>283.00 <b>(-29.37%)</b></td><td>254.24 (-9.39%)</td><td>253.40 (+3.26%)</td><td>220.70 (-2.35%)</td><td>22.96 <b>(-67.65%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>400.70 (n/a)</td><td>280.58 (n/a)</td><td>245.40 (n/a)</td><td>226.00 (n/a)</td><td>70.95 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (-13.34%)</td><td>0.02 <b>(+31.34%)</b></td><td>0.02 <b>(+66.25%)</b></td><td>0.01 <b>(+70.86%)</b></td><td>0.00 <b>(-52.37%)</b></td><td>385.90 <b>(-41.48%)</b></td><td>283.70 <b>(-32.54%)</b></td><td>264.50 <b>(-39.86%)</b></td><td>247.40 (+15.39%)</td><td>57.74 <b>(-66.15%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>659.40 (n/a)</td><td>420.52 (n/a)</td><td>439.80 (n/a)</td><td>214.40 (n/a)</td><td>170.60 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 <b>(+33.69%)</b></td><td>0.02 (+11.55%)</td><td>0.02 <b>(+43.17%)</b></td><td>0.01 <b>(-50.58%)</b></td><td>0.01 <b>(+88.45%)</b></td><td>1041.20 <b>(+102.37%)</b></td><td>449.18 (+13.99%)</td><td>291.40 <b>(-30.15%)</b></td><td>210.10 <b>(-25.20%)</b></td><td>339.08 <b>(+224.04%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.50 (n/a)</td><td>394.04 (n/a)</td><td>417.20 (n/a)</td><td>280.90 (n/a)</td><td>104.64 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 <b>(+97.91%)</b></td><td>0.02 <b>(+96.25%)</b></td><td>0.02 <b>(+71.48%)</b></td><td>0.01 <b>(+330.35%)</b></td><td>0.01 <b>(+41.06%)</b></td><td>457.10 <b>(-76.76%)</b></td><td>290.10 <b>(-61.69%)</b></td><td>256.40 <b>(-41.67%)</b></td><td>175.80 <b>(-49.47%)</b></td><td>106.66 <b>(-84.41%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1967.20 (n/a)</td><td>757.28 (n/a)</td><td>439.60 (n/a)</td><td>347.90 (n/a)</td><td>684.11 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 <b>(+76.96%)</b></td><td>0.02 <b>(+84.95%)</b></td><td>0.02 <b>(+99.43%)</b></td><td>0.01 <b>(+282.07%)</b></td><td>0.01 <b>(+38.41%)</b></td><td>529.40 <b>(-73.83%)</b></td><td>346.82 <b>(-56.94%)</b></td><td>270.50 <b>(-49.86%)</b></td><td>242.10 <b>(-43.49%)</b></td><td>125.28 <b>(-81.63%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2022.60 (n/a)</td><td>805.38 (n/a)</td><td>539.50 (n/a)</td><td>428.40 (n/a)</td><td>682.09 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (+18.42%)</td><td>0.02 <b>(+49.66%)</b></td><td>0.02 <b>(+47.12%)</b></td><td>0.01 <b>(+192.87%)</b></td><td>0.01 (-11.68%)</td><td>641.50 <b>(-65.85%)</b></td><td>368.76 <b>(-49.76%)</b></td><td>328.10 <b>(-32.03%)</b></td><td>236.20 (-15.55%)</td><td>157.30 <b>(-75.74%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1878.70 (n/a)</td><td>733.94 (n/a)</td><td>482.70 (n/a)</td><td>279.70 (n/a)</td><td>648.35 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>599.10 (n/a)</td><td>408.88 (n/a)</td><td>443.60 (n/a)</td><td>269.00 (n/a)</td><td>139.31 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>561.40 (n/a)</td><td>449.80 (n/a)</td><td>460.80 (n/a)</td><td>228.10 (n/a)</td><td>132.68 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1872.20 (n/a)</td><td>876.74 (n/a)</td><td>608.50 (n/a)</td><td>234.90 (n/a)</td><td>632.66 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>466.50 (n/a)</td><td>352.90 (n/a)</td><td>420.70 (n/a)</td><td>208.40 (n/a)</td><td>116.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>504.00 (n/a)</td><td>321.66 (n/a)</td><td>239.20 (n/a)</td><td>209.00 (n/a)</td><td>131.14 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>697.80 (n/a)</td><td>399.84 (n/a)</td><td>329.00 (n/a)</td><td>198.80 (n/a)</td><td>205.06 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.85 (-18.09%)</td><td>0.69 (-19.77%)</td><td>0.68 <b>(-24.63%)</b></td><td>0.45 <b>(-26.55%)</b></td><td>0.16 (-9.31%)</td><td>1012.90 <b>(+36.14%)</b></td><td>701.46 <b>(+26.29%)</b></td><td>678.00 <b>(+32.68%)</b></td><td>542.90 <b>(+22.08%)</b></td><td>190.48 <b>(+51.09%)</b></td><td>61.81 (-18.09%)</td><td>50.34 (-19.77%)</td><td>49.49 <b>(-24.63%)</b></td><td>33.13 <b>(-26.55%)</b></td><td>11.73 (-9.31%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.03 (n/a)</td><td>0.86 (n/a)</td><td>0.90 (n/a)</td><td>0.62 (n/a)</td><td>0.18 (n/a)</td><td>744.00 (n/a)</td><td>555.42 (n/a)</td><td>511.00 (n/a)</td><td>444.70 (n/a)</td><td>126.07 (n/a)</td><td>75.46 (n/a)</td><td>62.74 (n/a)</td><td>65.66 (n/a)</td><td>45.10 (n/a)</td><td>12.93 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.37 (+7.38%)</td><td>1.10 <b>(+22.62%)</b></td><td>0.99 (+8.15%)</td><td>0.86 <b>(+204.82%)</b></td><td>0.25 <b>(-38.28%)</b></td><td>761.80 <b>(-67.19%)</b></td><td>622.14 <b>(-37.00%)</b></td><td>665.20 (-7.55%)</td><td>479.90 (-6.87%)</td><td>133.61 <b>(-82.39%)</b></td><td>139.85 (+7.38%)</td><td>112.22 <b>(+22.62%)</b></td><td>100.88 (+8.15%)</td><td>88.10 <b>(+204.82%)</b></td><td>25.41 <b>(-38.28%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.27 (n/a)</td><td>0.89 (n/a)</td><td>0.91 (n/a)</td><td>0.28 (n/a)</td><td>0.40 (n/a)</td><td>2321.90 (n/a)</td><td>987.60 (n/a)</td><td>719.50 (n/a)</td><td>515.30 (n/a)</td><td>758.63 (n/a)</td><td>130.24 (n/a)</td><td>91.52 (n/a)</td><td>93.28 (n/a)</td><td>28.90 (n/a)</td><td>41.17 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.19 (+17.67%)</td><td>1.00 (+13.63%)</td><td>1.01 (+5.08%)</td><td>0.71 (+2.45%)</td><td>0.20 <b>(+28.75%)</b></td><td>1062.60 (-2.39%)</td><td>780.08 (-11.17%)</td><td>745.90 (-4.84%)</td><td>633.30 (-15.00%)</td><td>173.98 (+7.31%)</td><td>132.47 (+17.67%)</td><td>111.37 (+13.63%)</td><td>112.46 (+5.08%)</td><td>78.94 (+2.45%)</td><td>21.75 <b>(+28.75%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.01 (n/a)</td><td>0.88 (n/a)</td><td>0.96 (n/a)</td><td>0.69 (n/a)</td><td>0.15 (n/a)</td><td>1088.60 (n/a)</td><td>878.20 (n/a)</td><td>783.80 (n/a)</td><td>745.10 (n/a)</td><td>162.12 (n/a)</td><td>112.58 (n/a)</td><td>98.01 (n/a)</td><td>107.02 (n/a)</td><td>77.06 (n/a)</td><td>16.89 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.33 (-19.78%)</td><td>1.04 <b>(-25.42%)</b></td><td>1.16 <b>(-23.63%)</b></td><td>0.50 <b>(-45.80%)</b></td><td>0.32 (+4.40%)</td><td>2082.60 <b>(+84.50%)</b></td><td>1140.10 <b>(+44.37%)</b></td><td>906.90 <b>(+30.94%)</b></td><td>790.10 <b>(+24.66%)</b></td><td>535.65 <b>(+156.77%)</b></td><td>169.87 (-19.78%)</td><td>132.91 <b>(-25.42%)</b></td><td>148.00 <b>(-23.63%)</b></td><td>64.45 <b>(-45.80%)</b></td><td>41.24 (+4.40%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.65 (n/a)</td><td>1.39 (n/a)</td><td>1.51 (n/a)</td><td>0.93 (n/a)</td><td>0.31 (n/a)</td><td>1128.80 (n/a)</td><td>789.68 (n/a)</td><td>692.60 (n/a)</td><td>633.80 (n/a)</td><td>208.61 (n/a)</td><td>211.76 (n/a)</td><td>178.22 (n/a)</td><td>193.79 (n/a)</td><td>118.91 (n/a)</td><td>39.50 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>2.45 <b>(+47.04%)</b></td><td>1.67 <b>(+36.68%)</b></td><td>1.77 <b>(+34.58%)</b></td><td>0.83 <b>(+80.16%)</b></td><td>0.59 <b>(+31.33%)</b></td><td>1268.00 <b>(-44.50%)</b></td><td>714.58 <b>(-32.32%)</b></td><td>592.10 <b>(-25.70%)</b></td><td>428.10 <b>(-31.99%)</b></td><td>326.20 <b>(-52.75%)</b></td><td>313.50 <b>(+47.04%)</b></td><td>214.00 <b>(+36.68%)</b></td><td>226.68 <b>(+34.58%)</b></td><td>105.85 <b>(+80.16%)</b></td><td>75.92 <b>(+31.33%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.67 (n/a)</td><td>1.22 (n/a)</td><td>1.32 (n/a)</td><td>0.46 (n/a)</td><td>0.45 (n/a)</td><td>2284.50 (n/a)</td><td>1055.82 (n/a)</td><td>796.90 (n/a)</td><td>629.50 (n/a)</td><td>690.39 (n/a)</td><td>213.20 (n/a)</td><td>156.57 (n/a)</td><td>168.43 (n/a)</td><td>58.75 (n/a)</td><td>57.81 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.87 <b>(+35.55%)</b></td><td>1.21 (+16.50%)</td><td>1.43 <b>(+20.41%)</b></td><td>0.30 (+0.21%)</td><td>0.69 <b>(+55.35%)</b></td><td>3463.00 (-0.21%)</td><td>1376.14 (-1.17%)</td><td>731.30 (-16.94%)</td><td>560.50 <b>(-26.23%)</b></td><td>1232.12 (+5.46%)</td><td>239.45 <b>(+35.55%)</b></td><td>155.08 (+16.50%)</td><td>183.54 <b>(+20.41%)</b></td><td>38.76 (+0.21%)</td><td>88.10 <b>(+55.35%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.38 (n/a)</td><td>1.04 (n/a)</td><td>1.19 (n/a)</td><td>0.30 (n/a)</td><td>0.44 (n/a)</td><td>3470.20 (n/a)</td><td>1392.48 (n/a)</td><td>880.50 (n/a)</td><td>759.80 (n/a)</td><td>1168.35 (n/a)</td><td>176.64 (n/a)</td><td>133.12 (n/a)</td><td>152.43 (n/a)</td><td>38.68 (n/a)</td><td>56.71 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.88 (-8.98%)</td><td>1.62 <b>(+24.01%)</b></td><td>1.71 <b>(+41.70%)</b></td><td>1.25 <b>(+188.49%)</b></td><td>0.25 <b>(-60.33%)</b></td><td>836.10 <b>(-65.34%)</b></td><td>662.44 <b>(-38.39%)</b></td><td>614.50 <b>(-29.43%)</b></td><td>557.60 (+9.87%)</td><td>112.61 <b>(-85.42%)</b></td><td>240.71 (-8.98%)</td><td>206.96 <b>(+24.01%)</b></td><td>218.41 <b>(+41.70%)</b></td><td>160.53 <b>(+188.49%)</b></td><td>32.18 <b>(-60.33%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>2.07 (n/a)</td><td>1.30 (n/a)</td><td>1.20 (n/a)</td><td>0.43 (n/a)</td><td>0.63 (n/a)</td><td>2412.10 (n/a)</td><td>1075.26 (n/a)</td><td>870.80 (n/a)</td><td>507.50 (n/a)</td><td>772.42 (n/a)</td><td>264.46 (n/a)</td><td>166.90 (n/a)</td><td>154.13 (n/a)</td><td>55.64 (n/a)</td><td>81.12 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.80 <b>(+26.22%)</b></td><td>0.68 <b>(+24.73%)</b></td><td>0.71 <b>(+31.80%)</b></td><td>0.50 (+2.90%)</td><td>0.13 <b>(+132.31%)</b></td><td>723.10 (-2.82%)</td><td>549.48 (-17.80%)</td><td>507.50 <b>(-24.13%)</b></td><td>452.60 <b>(-20.76%)</b></td><td>116.70 <b>(+75.78%)</b></td><td>37.07 <b>(+26.22%)</b></td><td>31.56 <b>(+24.73%)</b></td><td>33.06 <b>(+31.80%)</b></td><td>23.20 (+2.90%)</td><td>6.12 <b>(+132.30%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.63 (n/a)</td><td>0.54 (n/a)</td><td>0.54 (n/a)</td><td>0.48 (n/a)</td><td>0.06 (n/a)</td><td>744.10 (n/a)</td><td>668.46 (n/a)</td><td>668.90 (n/a)</td><td>571.20 (n/a)</td><td>66.39 (n/a)</td><td>29.37 (n/a)</td><td>25.31 (n/a)</td><td>25.08 (n/a)</td><td>22.55 (n/a)</td><td>2.63 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>4.05 <b>(+22.68%)</b></td><td>2.42 (+12.21%)</td><td>1.88 (-19.60%)</td><td>1.10 (-0.65%)</td><td>1.39 <b>(+58.01%)</b></td><td>2383.70 (+0.65%)</td><td>1423.80 (+0.47%)</td><td>1391.40 <b>(+24.38%)</b></td><td>647.40 (-18.48%)</td><td>773.17 (+19.24%)</td><td>829.33 <b>(+22.68%)</b></td><td>496.30 (+12.21%)</td><td>385.84 (-19.60%)</td><td>225.23 (-0.65%)</td><td>285.11 <b>(+58.01%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>3.30 (n/a)</td><td>2.16 (n/a)</td><td>2.34 (n/a)</td><td>1.11 (n/a)</td><td>0.88 (n/a)</td><td>2368.20 (n/a)</td><td>1417.12 (n/a)</td><td>1118.70 (n/a)</td><td>794.20 (n/a)</td><td>648.40 (n/a)</td><td>675.99 (n/a)</td><td>442.29 (n/a)</td><td>479.90 (n/a)</td><td>226.70 (n/a)</td><td>180.44 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.50 (n/a)</td><td>387.32 (n/a)</td><td>391.70 (n/a)</td><td>225.50 (n/a)</td><td>119.87 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>546.40 (n/a)</td><td>411.86 (n/a)</td><td>417.40 (n/a)</td><td>282.00 (n/a)</td><td>99.32 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>473.60 (n/a)</td><td>350.08 (n/a)</td><td>326.00 (n/a)</td><td>244.30 (n/a)</td><td>93.81 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.70 (n/a)</td><td>356.16 (n/a)</td><td>322.10 (n/a)</td><td>227.20 (n/a)</td><td>130.91 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.90 (n/a)</td><td>444.82 (n/a)</td><td>535.60 (n/a)</td><td>255.10 (n/a)</td><td>167.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>467.20 (n/a)</td><td>372.46 (n/a)</td><td>353.10 (n/a)</td><td>261.80 (n/a)</td><td>80.12 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.64 (+4.79%)</td><td>0.47 (-0.36%)</td><td>0.50 (+11.48%)</td><td>0.21 <b>(-48.89%)</b></td><td>0.16 <b>(+105.01%)</b></td><td>1038.40 <b>(+95.67%)</b></td><td>540.12 (+14.19%)</td><td>438.80 (-10.30%)</td><td>347.50 (-4.56%)</td><td>283.13 <b>(+313.49%)</b></td><td>27.16 (+4.79%)</td><td>20.26 (-0.36%)</td><td>21.51 (+11.48%)</td><td>9.09 <b>(-48.89%)</b></td><td>6.87 <b>(+105.01%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.61 (n/a)</td><td>0.48 (n/a)</td><td>0.45 (n/a)</td><td>0.42 (n/a)</td><td>0.08 (n/a)</td><td>530.70 (n/a)</td><td>473.02 (n/a)</td><td>489.20 (n/a)</td><td>364.10 (n/a)</td><td>68.47 (n/a)</td><td>25.92 (n/a)</td><td>20.34 (n/a)</td><td>19.29 (n/a)</td><td>17.78 (n/a)</td><td>3.35 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.48 <b>(-27.26%)</b></td><td>0.35 (-0.83%)</td><td>0.41 <b>(+22.32%)</b></td><td>0.12 (-4.85%)</td><td>0.14 <b>(-30.73%)</b></td><td>1770.80 (+5.09%)</td><td>793.44 (-4.51%)</td><td>535.50 (-18.24%)</td><td>463.00 <b>(+37.47%)</b></td><td>552.43 (+4.38%)</td><td>20.38 <b>(-27.26%)</b></td><td>15.10 (-0.83%)</td><td>17.62 <b>(+22.32%)</b></td><td>5.33 (-4.85%)</td><td>5.95 <b>(-30.73%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.66 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.13 (n/a)</td><td>0.20 (n/a)</td><td>1685.00 (n/a)</td><td>830.92 (n/a)</td><td>655.00 (n/a)</td><td>336.80 (n/a)</td><td>529.23 (n/a)</td><td>28.02 (n/a)</td><td>15.22 (n/a)</td><td>14.41 (n/a)</td><td>5.60 (n/a)</td><td>8.60 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.31 (-0.52%)</td><td>0.31 (+0.96%)</td><td>0.31 (+1.25%)</td><td>0.30 (+1.96%)</td><td>0.00 <b>(-49.57%)</b></td><td>83270.60 (-1.93%)</td><td>82280.60 (-0.97%)</td><td>82188.40 (-1.24%)</td><td>81592.80 (+0.52%)</td><td>700.73 <b>(-50.29%)</b></td><td>210.56 (-0.52%)</td><td>208.81 (+0.96%)</td><td>209.03 (+1.25%)</td><td>206.31 (+1.96%)</td><td>1.77 <b>(-49.57%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84906.40 (n/a)</td><td>83088.28 (n/a)</td><td>83216.20 (n/a)</td><td>81170.00 (n/a)</td><td>1409.58 (n/a)</td><td>211.65 (n/a)</td><td>206.81 (n/a)</td><td>206.45 (n/a)</td><td>202.34 (n/a)</td><td>3.52 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.15 (+0.13%)</td><td>1.13 (-0.24%)</td><td>1.14 (-0.69%)</td><td>1.07 (-2.28%)</td><td>0.03 <b>(+28.88%)</b></td><td>23468.90 (+2.34%)</td><td>22346.14 (+0.27%)</td><td>22129.30 (+0.69%)</td><td>21877.80 (-0.13%)</td><td>651.02 <b>(+32.45%)</b></td><td>785.26 (+0.13%)</td><td>769.31 (-0.24%)</td><td>776.34 (-0.69%)</td><td>732.03 (-2.28%)</td><td>21.71 <b>(+28.88%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.15 (n/a)</td><td>1.13 (n/a)</td><td>1.15 (n/a)</td><td>1.10 (n/a)</td><td>0.02 (n/a)</td><td>22932.80 (n/a)</td><td>22287.06 (n/a)</td><td>21976.90 (n/a)</td><td>21906.70 (n/a)</td><td>491.53 (n/a)</td><td>784.23 (n/a)</td><td>771.14 (n/a)</td><td>781.72 (n/a)</td><td>749.14 (n/a)</td><td>16.85 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>4.21 <b>(+89.16%)</b></td><td>3.19 <b>(+74.91%)</b></td><td>4.14 <b>(+138.94%)</b></td><td>1.43 (-11.49%)</td><td>1.37 <b>(+457.99%)</b></td><td>5647.00 (+12.98%)</td><td>3101.02 <b>(-30.80%)</b></td><td>1949.30 <b>(-58.15%)</b></td><td>1915.50 <b>(-47.13%)</b></td><td>1697.98 <b>(+211.31%)</b></td><td>1103.59 <b>(+89.16%)</b></td><td>836.03 <b>(+74.91%)</b></td><td>1084.44 <b>(+138.94%)</b></td><td>374.35 (-11.49%)</td><td>358.91 <b>(+457.99%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>2.22 (n/a)</td><td>1.82 (n/a)</td><td>1.73 (n/a)</td><td>1.61 (n/a)</td><td>0.25 (n/a)</td><td>4998.10 (n/a)</td><td>4481.16 (n/a)</td><td>4657.60 (n/a)</td><td>3623.30 (n/a)</td><td>545.43 (n/a)</td><td>583.42 (n/a)</td><td>477.97 (n/a)</td><td>453.86 (n/a)</td><td>422.95 (n/a)</td><td>64.32 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.28 (-1.29%)</td><td>0.20 (-2.44%)</td><td>0.21 (+0.35%)</td><td>0.13 (-16.31%)</td><td>0.07 <b>(+34.06%)</b></td><td>9531.20 (+19.49%)</td><td>6701.74 (+7.76%)</td><td>6066.80 (-0.35%)</td><td>4454.50 (+1.30%)</td><td>2315.62 <b>(+61.75%)</b></td><td>15.07 (-1.29%)</td><td>11.01 (-2.44%)</td><td>11.06 (+0.35%)</td><td>7.04 (-16.31%)</td><td>3.65 <b>(+34.06%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>7976.60 (n/a)</td><td>6219.06 (n/a)</td><td>6088.00 (n/a)</td><td>4397.20 (n/a)</td><td>1431.63 (n/a)</td><td>15.26 (n/a)</td><td>11.28 (n/a)</td><td>11.02 (n/a)</td><td>8.41 (n/a)</td><td>2.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>3.93 (n/a)</td><td>3.70 (n/a)</td><td>3.70 (n/a)</td><td>3.48 (n/a)</td><td>0.19 (n/a)</td><td>3.93 (n/a)</td><td>3.70 (n/a)</td><td>3.70 (n/a)</td><td>3.48 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>7.13 (-4.12%)</td><td>6.24 (-2.43%)</td><td>6.65 (+5.76%)</td><td>4.77 (-13.93%)</td><td>0.97 <b>(+40.89%)</b></td><td>7.13 (-4.12%)</td><td>6.24 (-2.43%)</td><td>6.65 (+5.76%)</td><td>4.77 (-13.93%)</td><td>0.97 <b>(+40.89%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>7.44 (n/a)</td><td>6.40 (n/a)</td><td>6.29 (n/a)</td><td>5.55 (n/a)</td><td>0.69 (n/a)</td><td>7.43 (n/a)</td><td>6.39 (n/a)</td><td>6.29 (n/a)</td><td>5.54 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>14.40 (+2.96%)</td><td>11.33 (-0.29%)</td><td>12.57 <b>(+24.15%)</b></td><td>7.46 <b>(-23.71%)</b></td><td>3.32 <b>(+64.75%)</b></td><td>14.40 (+2.96%)</td><td>11.33 (-0.29%)</td><td>12.57 <b>(+24.15%)</b></td><td>7.45 <b>(-23.71%)</b></td><td>3.32 <b>(+64.74%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>13.99 (n/a)</td><td>11.37 (n/a)</td><td>10.13 (n/a)</td><td>9.78 (n/a)</td><td>2.02 (n/a)</td><td>13.98 (n/a)</td><td>11.36 (n/a)</td><td>10.12 (n/a)</td><td>9.77 (n/a)</td><td>2.02 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>3.84 (n/a)</td><td>3.56 (n/a)</td><td>3.56 (n/a)</td><td>3.31 (n/a)</td><td>0.19 (n/a)</td><td>3.84 (n/a)</td><td>3.56 (n/a)</td><td>3.56 (n/a)</td><td>3.30 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>7.52 (+1.57%)</td><td>6.56 (-2.39%)</td><td>6.75 (-0.50%)</td><td>5.67 (-5.25%)</td><td>0.80 <b>(+52.09%)</b></td><td>7.52 (+1.57%)</td><td>6.55 (-2.39%)</td><td>6.75 (-0.50%)</td><td>5.67 (-5.25%)</td><td>0.80 <b>(+52.09%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>7.41 (n/a)</td><td>6.72 (n/a)</td><td>6.78 (n/a)</td><td>5.99 (n/a)</td><td>0.53 (n/a)</td><td>7.40 (n/a)</td><td>6.71 (n/a)</td><td>6.78 (n/a)</td><td>5.98 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>14.01 (-0.91%)</td><td>11.48 <b>(+22.17%)</b></td><td>13.42 <b>(+49.85%)</b></td><td>7.77 <b>(+22.80%)</b></td><td>3.15 (+7.97%)</td><td>14.00 (-0.91%)</td><td>11.48 <b>(+22.17%)</b></td><td>13.41 <b>(+49.85%)</b></td><td>7.76 <b>(+22.80%)</b></td><td>3.14 (+7.97%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>14.14 (n/a)</td><td>9.40 (n/a)</td><td>8.96 (n/a)</td><td>6.33 (n/a)</td><td>2.91 (n/a)</td><td>14.13 (n/a)</td><td>9.39 (n/a)</td><td>8.95 (n/a)</td><td>6.32 (n/a)</td><td>2.91 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>2.80 (-2.62%)</td><td>2.31 (-11.44%)</td><td>2.77 (+0.07%)</td><td>1.52 <b>(-21.47%)</b></td><td>0.66 <b>(+71.25%)</b></td><td>2.79 (-2.62%)</td><td>2.30 (-11.44%)</td><td>2.76 (+0.07%)</td><td>1.52 <b>(-21.47%)</b></td><td>0.66 <b>(+71.25%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>2.88 (n/a)</td><td>2.61 (n/a)</td><td>2.77 (n/a)</td><td>1.94 (n/a)</td><td>0.38 (n/a)</td><td>2.87 (n/a)</td><td>2.60 (n/a)</td><td>2.76 (n/a)</td><td>1.93 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.56 (+8.23%)</td><td>0.32 (+2.91%)</td><td>0.33 (-16.93%)</td><td>0.14 <b>(+94.55%)</b></td><td>0.16 <b>(-28.95%)</b></td><td>0.55 (+8.23%)</td><td>0.32 (+2.91%)</td><td>0.32 (-16.93%)</td><td>0.14 <b>(+94.55%)</b></td><td>0.16 <b>(-28.95%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.52 (n/a)</td><td>0.31 (n/a)</td><td>0.39 (n/a)</td><td>0.07 (n/a)</td><td>0.22 (n/a)</td><td>0.51 (n/a)</td><td>0.31 (n/a)</td><td>0.39 (n/a)</td><td>0.07 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.72 (-2.04%)</td><td>0.31 (+0.08%)</td><td>0.29 (-8.36%)</td><td>0.08 (+4.23%)</td><td>0.25 (-6.26%)</td><td>0.71 (-2.04%)</td><td>0.31 (+0.08%)</td><td>0.28 (-8.36%)</td><td>0.08 (+4.23%)</td><td>0.25 (-6.26%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.73 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>0.27 (n/a)</td><td>0.73 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>2.51 (+17.77%)</td><td>1.44 (-10.86%)</td><td>1.35 <b>(-27.01%)</b></td><td>0.46 (+2.65%)</td><td>0.99 <b>(+45.51%)</b></td><td>2.47 (+17.77%)</td><td>1.42 (-10.86%)</td><td>1.33 <b>(-27.01%)</b></td><td>0.45 (+2.65%)</td><td>0.97 <b>(+45.51%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>2.13 (n/a)</td><td>1.62 (n/a)</td><td>1.86 (n/a)</td><td>0.45 (n/a)</td><td>0.68 (n/a)</td><td>2.10 (n/a)</td><td>1.59 (n/a)</td><td>1.83 (n/a)</td><td>0.44 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>488.70 (n/a)</td><td>300.64 (n/a)</td><td>279.00 (n/a)</td><td>173.10 (n/a)</td><td>114.99 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.80 (n/a)</td><td>302.04 (n/a)</td><td>246.80 (n/a)</td><td>224.90 (n/a)</td><td>127.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>621.70 (n/a)</td><td>541.70 (n/a)</td><td>554.40 (n/a)</td><td>470.70 (n/a)</td><td>57.74 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.30 (n/a)</td><td>443.08 (n/a)</td><td>453.80 (n/a)</td><td>285.90 (n/a)</td><td>135.25 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>545.60 (n/a)</td><td>446.36 (n/a)</td><td>475.80 (n/a)</td><td>321.40 (n/a)</td><td>92.57 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.50 (n/a)</td><td>459.28 (n/a)</td><td>500.40 (n/a)</td><td>266.80 (n/a)</td><td>109.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 <b>(-30.41%)</b></td><td>0.02 (-16.32%)</td><td>0.02 (-11.22%)</td><td>0.02 (-3.09%)</td><td>0.01 <b>(-41.62%)</b></td><td>527.00 (+3.19%)</td><td>414.48 (+12.74%)</td><td>474.10 (+12.64%)</td><td>291.80 <b>(+43.67%)</b></td><td>109.30 (-15.54%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.70 (n/a)</td><td>367.64 (n/a)</td><td>420.90 (n/a)</td><td>203.10 (n/a)</td><td>129.41 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (-15.80%)</td><td>0.02 (-1.54%)</td><td>0.02 (-13.49%)</td><td>0.01 <b>(+232.90%)</b></td><td>0.01 <b>(-32.04%)</b></td><td>588.80 <b>(-69.96%)</b></td><td>428.52 <b>(-35.84%)</b></td><td>500.80 (+15.60%)</td><td>255.30 (+18.74%)</td><td>158.44 <b>(-78.33%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1960.20 (n/a)</td><td>667.86 (n/a)</td><td>433.20 (n/a)</td><td>215.00 (n/a)</td><td>731.14 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (+9.64%)</td><td>0.02 (-1.42%)</td><td>0.02 (-13.59%)</td><td>0.02 <b>(+31.79%)</b></td><td>0.01 (-14.72%)</td><td>436.90 <b>(-24.11%)</b></td><td>386.76 (-4.44%)</td><td>435.40 (+15.74%)</td><td>228.50 (-8.78%)</td><td>90.06 <b>(-42.21%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.70 (n/a)</td><td>404.74 (n/a)</td><td>376.20 (n/a)</td><td>250.50 (n/a)</td><td>155.84 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (+6.80%)</td><td>0.03 (+17.74%)</td><td>0.03 <b>(+29.47%)</b></td><td>0.02 <b>(+41.85%)</b></td><td>0.01 (-15.83%)</td><td>419.80 <b>(-29.49%)</b></td><td>324.54 (-18.85%)</td><td>310.40 <b>(-22.75%)</b></td><td>225.70 (-6.35%)</td><td>74.18 <b>(-44.06%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.40 (n/a)</td><td>399.94 (n/a)</td><td>401.80 (n/a)</td><td>241.00 (n/a)</td><td>132.62 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (-10.75%)</td><td>0.02 <b>(-21.19%)</b></td><td>0.02 <b>(-38.32%)</b></td><td>0.01 (-6.38%)</td><td>0.01 <b>(-29.33%)</b></td><td>556.40 (+6.82%)</td><td>411.64 (+19.83%)</td><td>437.40 <b>(+62.12%)</b></td><td>245.40 (+12.05%)</td><td>112.83 <b>(-20.95%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.90 (n/a)</td><td>343.52 (n/a)</td><td>269.80 (n/a)</td><td>219.00 (n/a)</td><td>142.74 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (-7.82%)</td><td>0.01 (-17.33%)</td><td>0.02 (-0.18%)</td><td>0.00 (+8.95%)</td><td>0.01 (+2.03%)</td><td>1861.60 (-8.22%)</td><td>907.18 (+18.99%)</td><td>506.30 (+0.18%)</td><td>366.60 (+8.49%)</td><td>651.35 (-8.41%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2028.30 (n/a)</td><td>762.40 (n/a)</td><td>505.40 (n/a)</td><td>337.90 (n/a)</td><td>711.17 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (-17.89%)</td><td>0.02 (-10.72%)</td><td>0.02 (+15.72%)</td><td>0.01 <b>(-55.33%)</b></td><td>0.01 (+18.59%)</td><td>1202.60 <b>(+123.86%)</b></td><td>592.50 <b>(+28.86%)</b></td><td>428.90 (-13.60%)</td><td>352.80 <b>(+21.78%)</b></td><td>350.90 <b>(+252.68%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.20 (n/a)</td><td>459.80 (n/a)</td><td>496.40 (n/a)</td><td>289.70 (n/a)</td><td>99.49 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 <b>(-35.32%)</b></td><td>0.02 (-14.62%)</td><td>0.02 (-16.67%)</td><td>0.01 (+6.41%)</td><td>0.00 <b>(-69.70%)</b></td><td>646.00 (-6.01%)</td><td>528.26 (+6.34%)</td><td>520.10 <b>(+20.00%)</b></td><td>439.00 <b>(+54.63%)</b></td><td>74.48 <b>(-58.39%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>687.30 (n/a)</td><td>496.76 (n/a)</td><td>433.40 (n/a)</td><td>283.90 (n/a)</td><td>179.00 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (+11.31%)</td><td>0.03 <b>(+70.63%)</b></td><td>0.03 <b>(+107.62%)</b></td><td>0.03 <b>(+132.14%)</b></td><td>0.00 <b>(-55.22%)</b></td><td>294.40 <b>(-56.92%)</b></td><td>252.48 <b>(-46.69%)</b></td><td>238.90 <b>(-51.83%)</b></td><td>229.50 (-10.18%)</td><td>28.08 <b>(-81.85%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>683.40 (n/a)</td><td>473.62 (n/a)</td><td>496.00 (n/a)</td><td>255.50 (n/a)</td><td>154.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (+16.83%)</td><td>0.03 <b>(+37.67%)</b></td><td>0.03 <b>(+64.72%)</b></td><td>0.02 (-4.60%)</td><td>0.01 <b>(+50.04%)</b></td><td>542.20 (+4.81%)</td><td>336.24 <b>(-23.65%)</b></td><td>278.00 <b>(-39.30%)</b></td><td>235.70 (-14.42%)</td><td>130.78 <b>(+35.06%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.30 (n/a)</td><td>440.38 (n/a)</td><td>458.00 (n/a)</td><td>275.40 (n/a)</td><td>96.83 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 <b>(+42.41%)</b></td><td>0.03 <b>(+25.74%)</b></td><td>0.03 (+12.94%)</td><td>0.02 (+3.27%)</td><td>0.01 <b>(+51.98%)</b></td><td>498.90 (-3.16%)</td><td>315.04 (-17.85%)</td><td>308.00 (-11.44%)</td><td>200.90 <b>(-29.78%)</b></td><td>114.52 (+5.86%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.20 (n/a)</td><td>383.50 (n/a)</td><td>347.80 (n/a)</td><td>286.10 (n/a)</td><td>108.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 <b>(+25.14%)</b></td><td>0.02 (-11.99%)</td><td>0.02 <b>(-34.78%)</b></td><td>0.01 (+0.93%)</td><td>0.01 (+12.26%)</td><td>1009.20 (-0.92%)</td><td>520.78 (+12.81%)</td><td>422.00 <b>(+53.34%)</b></td><td>196.30 <b>(-20.11%)</b></td><td>313.20 (-5.69%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1018.60 (n/a)</td><td>461.64 (n/a)</td><td>275.20 (n/a)</td><td>245.70 (n/a)</td><td>332.10 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (-11.58%)</td><td>0.02 <b>(-26.60%)</b></td><td>0.02 <b>(-36.70%)</b></td><td>0.01 <b>(-22.57%)</b></td><td>0.01 (+2.38%)</td><td>609.00 <b>(+29.16%)</b></td><td>494.38 <b>(+39.81%)</b></td><td>526.70 <b>(+57.98%)</b></td><td>278.10 (+13.09%)</td><td>135.00 <b>(+44.76%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>471.50 (n/a)</td><td>353.62 (n/a)</td><td>333.40 (n/a)</td><td>245.90 (n/a)</td><td>93.26 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 <b>(-33.21%)</b></td><td>0.01 <b>(-30.45%)</b></td><td>0.01 (-10.97%)</td><td>0.00 <b>(-71.52%)</b></td><td>0.01 (-3.73%)</td><td>2144.80 <b>(+251.09%)</b></td><td>848.60 <b>(+87.53%)</b></td><td>559.50 (+12.33%)</td><td>427.50 <b>(+49.74%)</b></td><td>729.06 <b>(+464.43%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.90 (n/a)</td><td>452.52 (n/a)</td><td>498.10 (n/a)</td><td>285.50 (n/a)</td><td>129.17 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.09 (-14.53%)</td><td>0.07 <b>(-24.97%)</b></td><td>0.06 <b>(-28.92%)</b></td><td>0.05 <b>(-41.07%)</b></td><td>0.02 <b>(+79.73%)</b></td><td>510.40 <b>(+69.68%)</b></td><td>383.88 <b>(+40.78%)</b></td><td>407.40 <b>(+40.68%)</b></td><td>273.20 (+17.00%)</td><td>106.65 <b>(+236.95%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>300.80 (n/a)</td><td>272.68 (n/a)</td><td>289.60 (n/a)</td><td>233.50 (n/a)</td><td>31.65 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.17 (+1.02%)</td><td>0.11 (-16.50%)</td><td>0.10 <b>(-30.00%)</b></td><td>0.08 <b>(-29.18%)</b></td><td>0.04 <b>(+64.93%)</b></td><td>526.90 <b>(+41.22%)</b></td><td>393.64 <b>(+27.91%)</b></td><td>406.60 <b>(+42.87%)</b></td><td>245.90 (-1.01%)</td><td>125.97 <b>(+127.54%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>373.10 (n/a)</td><td>307.74 (n/a)</td><td>284.60 (n/a)</td><td>248.40 (n/a)</td><td>55.36 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (-17.54%)</td><td>0.02 (-13.33%)</td><td>0.02 (-6.71%)</td><td>0.01 <b>(-30.44%)</b></td><td>0.00 <b>(+38.62%)</b></td><td>416.10 <b>(+43.78%)</b></td><td>317.60 (+17.03%)</td><td>293.90 (+7.18%)</td><td>283.80 <b>(+21.23%)</b></td><td>55.47 <b>(+149.38%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>289.40 (n/a)</td><td>271.38 (n/a)</td><td>274.20 (n/a)</td><td>234.10 (n/a)</td><td>22.24 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (+5.52%)</td><td>0.03 <b>(+20.42%)</b></td><td>0.03 <b>(+77.61%)</b></td><td>0.02 (+3.59%)</td><td>0.01 (+0.48%)</td><td>475.10 (-3.47%)</td><td>322.24 (-17.61%)</td><td>263.60 <b>(-43.69%)</b></td><td>216.50 (-5.25%)</td><td>109.22 (-8.83%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.20 (n/a)</td><td>391.12 (n/a)</td><td>468.10 (n/a)</td><td>228.50 (n/a)</td><td>119.79 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (-15.66%)</td><td>0.03 (-12.01%)</td><td>0.04 <b>(+55.21%)</b></td><td>0.01 <b>(-73.10%)</b></td><td>0.02 (+5.30%)</td><td>2029.90 <b>(+271.78%)</b></td><td>690.00 <b>(+70.02%)</b></td><td>320.50 <b>(-35.58%)</b></td><td>276.30 (+18.58%)</td><td>755.17 <b>(+396.31%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>546.00 (n/a)</td><td>405.84 (n/a)</td><td>497.50 (n/a)</td><td>233.00 (n/a)</td><td>152.16 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (-12.19%)</td><td>0.02 (-13.14%)</td><td>0.02 (-19.26%)</td><td>0.02 (+9.55%)</td><td>0.01 <b>(-36.91%)</b></td><td>478.50 (-8.72%)</td><td>385.64 (+7.47%)</td><td>419.30 <b>(+23.87%)</b></td><td>252.80 (+13.87%)</td><td>89.51 <b>(-34.59%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.20 (n/a)</td><td>358.84 (n/a)</td><td>338.50 (n/a)</td><td>222.00 (n/a)</td><td>136.85 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 (-16.62%)</td><td>0.03 <b>(-22.06%)</b></td><td>0.02 <b>(-41.86%)</b></td><td>0.02 <b>(+33.16%)</b></td><td>0.01 <b>(-40.31%)</b></td><td>479.10 <b>(-24.91%)</b></td><td>401.42 (+16.91%)</td><td>442.90 <b>(+72.00%)</b></td><td>274.80 (+19.95%)</td><td>93.05 <b>(-45.67%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>638.00 (n/a)</td><td>343.36 (n/a)</td><td>257.50 (n/a)</td><td>229.10 (n/a)</td><td>171.26 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (+12.34%)</td><td>0.02 (-9.27%)</td><td>0.02 <b>(-29.80%)</b></td><td>0.01 (+0.26%)</td><td>0.01 (+16.64%)</td><td>642.90 (-0.26%)</td><td>439.48 (+11.88%)</td><td>448.00 <b>(+42.45%)</b></td><td>241.60 (-11.01%)</td><td>156.31 (+1.18%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>644.60 (n/a)</td><td>392.80 (n/a)</td><td>314.50 (n/a)</td><td>271.50 (n/a)</td><td>154.49 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.04 <b>(-32.78%)</b></td><td>0.02 <b>(-22.75%)</b></td><td>0.02 (-5.43%)</td><td>0.02 (+2.65%)</td><td>0.01 <b>(-52.72%)</b></td><td>532.90 (-2.60%)</td><td>455.48 (+15.08%)</td><td>491.00 (+5.75%)</td><td>276.60 <b>(+48.71%)</b></td><td>101.91 <b>(-36.25%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>547.10 (n/a)</td><td>395.80 (n/a)</td><td>464.30 (n/a)</td><td>186.00 (n/a)</td><td>159.85 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (+6.89%)</td><td>0.02 (+16.19%)</td><td>0.03 <b>(+58.91%)</b></td><td>0.01 (-3.42%)</td><td>0.01 <b>(+26.88%)</b></td><td>561.20 (+3.54%)</td><td>383.18 (-11.44%)</td><td>301.60 <b>(-37.07%)</b></td><td>275.90 (-6.44%)</td><td>128.25 <b>(+23.05%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.00 (n/a)</td><td>432.70 (n/a)</td><td>479.30 (n/a)</td><td>294.90 (n/a)</td><td>104.23 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 <b>(-31.82%)</b></td><td>0.02 (-4.78%)</td><td>0.02 (+0.61%)</td><td>0.01 <b>(+28.51%)</b></td><td>0.01 <b>(-46.64%)</b></td><td>637.20 <b>(-22.19%)</b></td><td>451.62 (-8.13%)</td><td>493.90 (-0.60%)</td><td>307.40 <b>(+46.66%)</b></td><td>137.69 <b>(-40.39%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>818.90 (n/a)</td><td>491.60 (n/a)</td><td>496.90 (n/a)</td><td>209.60 (n/a)</td><td>230.98 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.03 (-3.84%)</td><td>0.02 <b>(+24.65%)</b></td><td>0.02 (+6.26%)</td><td>0.02 <b>(+308.43%)</b></td><td>0.01 <b>(-44.30%)</b></td><td>507.20 <b>(-75.51%)</b></td><td>418.94 <b>(-46.26%)</b></td><td>458.50 (-5.89%)</td><td>286.20 (+4.00%)</td><td>91.49 <b>(-87.50%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2071.40 (n/a)</td><td>779.50 (n/a)</td><td>487.20 (n/a)</td><td>275.20 (n/a)</td><td>732.07 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.06 <b>(+116.28%)</b></td><td>0.03 <b>(+50.56%)</b></td><td>0.02 (+11.28%)</td><td>0.00 (+3.37%)</td><td>0.02 <b>(+131.41%)</b></td><td>1854.70 (-3.26%)</td><td>633.80 (-12.77%)</td><td>444.90 (-10.14%)</td><td>154.90 <b>(-53.75%)</b></td><td>694.72 (+3.58%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1917.20 (n/a)</td><td>726.58 (n/a)</td><td>495.10 (n/a)</td><td>334.90 (n/a)</td><td>670.70 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 <b>(-29.40%)</b></td><td>0.02 <b>(-20.67%)</b></td><td>0.02 <b>(-21.32%)</b></td><td>0.02 (+15.03%)</td><td>0.00 <b>(-60.42%)</b></td><td>495.10 (-13.06%)</td><td>420.28 (+16.67%)</td><td>427.10 <b>(+27.08%)</b></td><td>334.30 <b>(+41.65%)</b></td><td>65.26 <b>(-50.99%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.50 (n/a)</td><td>360.22 (n/a)</td><td>336.10 (n/a)</td><td>236.00 (n/a)</td><td>133.16 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.37 (+5.00%)</td><td>0.29 (+2.40%)</td><td>0.32 (-2.35%)</td><td>0.20 <b>(+28.18%)</b></td><td>0.07 (-14.63%)</td><td>480.40 <b>(-21.99%)</b></td><td>362.32 (-6.03%)</td><td>309.20 (+2.42%)</td><td>264.40 (-4.76%)</td><td>96.93 <b>(-33.05%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.33 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>615.80 (n/a)</td><td>385.58 (n/a)</td><td>301.90 (n/a)</td><td>277.60 (n/a)</td><td>144.77 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.31 <b>(-26.14%)</b></td><td>0.23 (-14.45%)</td><td>0.19 (-2.11%)</td><td>0.18 (+17.13%)</td><td>0.06 <b>(-51.87%)</b></td><td>551.50 (-14.63%)</td><td>454.34 (+4.08%)</td><td>519.60 (+2.14%)</td><td>313.00 <b>(+35.44%)</b></td><td>106.70 <b>(-41.20%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.43 (n/a)</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>646.00 (n/a)</td><td>436.54 (n/a)</td><td>508.70 (n/a)</td><td>231.10 (n/a)</td><td>181.45 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.41 (+1.06%)</td><td>0.32 (+10.60%)</td><td>0.33 <b>(+31.99%)</b></td><td>0.19 (+10.08%)</td><td>0.08 (-18.59%)</td><td>512.10 (-9.17%)</td><td>329.86 (-12.52%)</td><td>294.20 <b>(-24.23%)</b></td><td>237.80 (-1.04%)</td><td>106.48 (-19.38%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>563.80 (n/a)</td><td>377.06 (n/a)</td><td>388.30 (n/a)</td><td>240.30 (n/a)</td><td>132.07 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.27 (-9.26%)</td><td>0.19 <b>(-25.68%)</b></td><td>0.15 <b>(-41.35%)</b></td><td>0.12 <b>(-22.35%)</b></td><td>0.06 (+11.78%)</td><td>634.00 <b>(+28.78%)</b></td><td>436.52 <b>(+39.38%)</b></td><td>480.20 <b>(+70.53%)</b></td><td>276.20 (+10.22%)</td><td>147.28 <b>(+45.64%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>492.30 (n/a)</td><td>313.18 (n/a)</td><td>281.60 (n/a)</td><td>250.60 (n/a)</td><td>101.13 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.26 (-11.73%)</td><td>0.17 (-11.45%)</td><td>0.17 (+19.89%)</td><td>0.04 <b>(-65.13%)</b></td><td>0.09 (+14.56%)</td><td>1780.00 <b>(+186.82%)</b></td><td>686.84 <b>(+54.00%)</b></td><td>440.80 (-16.59%)</td><td>279.10 (+13.32%)</td><td>627.95 <b>(+278.04%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.30 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>620.60 (n/a)</td><td>446.00 (n/a)</td><td>528.50 (n/a)</td><td>246.30 (n/a)</td><td>166.11 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.38 (+16.63%)</td><td>0.22 (-16.65%)</td><td>0.23 (-19.87%)</td><td>0.04 <b>(-75.35%)</b></td><td>0.13 <b>(+100.49%)</b></td><td>1909.20 <b>(+305.61%)</b></td><td>624.70 <b>(+111.35%)</b></td><td>318.60 <b>(+24.79%)</b></td><td>192.70 (-14.24%)</td><td>724.76 <b>(+627.47%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.29 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>470.70 (n/a)</td><td>295.58 (n/a)</td><td>255.30 (n/a)</td><td>224.70 (n/a)</td><td>99.63 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.40 (-8.92%)</td><td>0.27 (-15.56%)</td><td>0.26 (+2.59%)</td><td>0.06 <b>(-72.43%)</b></td><td>0.14 <b>(+25.56%)</b></td><td>2087.90 <b>(+262.67%)</b></td><td>767.64 <b>(+69.03%)</b></td><td>503.80 (-2.52%)</td><td>324.70 (+9.81%)</td><td>745.24 <b>(+433.27%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>575.70 (n/a)</td><td>454.14 (n/a)</td><td>516.80 (n/a)</td><td>295.70 (n/a)</td><td>139.75 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.40 (+1.83%)</td><td>0.31 (+6.47%)</td><td>0.28 (+4.23%)</td><td>0.25 <b>(+28.55%)</b></td><td>0.07 (-12.51%)</td><td>533.10 <b>(-22.21%)</b></td><td>438.68 (-8.44%)</td><td>475.40 (-4.06%)</td><td>325.60 (-1.81%)</td><td>93.91 <b>(-32.48%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>685.30 (n/a)</td><td>479.10 (n/a)</td><td>495.50 (n/a)</td><td>331.60 (n/a)</td><td>139.08 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.38 (-6.14%)</td><td>0.26 (-2.82%)</td><td>0.24 (-0.91%)</td><td>0.21 (+10.65%)</td><td>0.07 (-17.70%)</td><td>615.70 (-9.62%)</td><td>519.56 (+0.85%)</td><td>535.80 (+0.92%)</td><td>346.60 (+6.55%)</td><td>102.44 <b>(-21.57%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.40 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>681.20 (n/a)</td><td>515.18 (n/a)</td><td>530.90 (n/a)</td><td>325.30 (n/a)</td><td>130.61 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (+2.25%)</td><td>0.01 <b>(-22.15%)</b></td><td>0.01 <b>(-37.34%)</b></td><td>0.01 (-18.02%)</td><td>0.01 <b>(+34.35%)</b></td><td>579.40 <b>(+21.98%)</b></td><td>404.18 <b>(+38.12%)</b></td><td>406.60 <b>(+59.58%)</b></td><td>212.80 (-2.21%)</td><td>160.80 <b>(+54.75%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>475.00 (n/a)</td><td>292.64 (n/a)</td><td>254.80 (n/a)</td><td>217.60 (n/a)</td><td>103.91 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 (+6.45%)</td><td>0.01 (-10.49%)</td><td>0.01 <b>(-40.99%)</b></td><td>0.01 (-11.98%)</td><td>0.01 <b>(+43.41%)</b></td><td>599.40 (+13.61%)</td><td>425.12 <b>(+22.73%)</b></td><td>524.90 <b>(+69.49%)</b></td><td>220.20 (-6.06%)</td><td>179.10 <b>(+49.59%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>527.60 (n/a)</td><td>346.38 (n/a)</td><td>309.70 (n/a)</td><td>234.40 (n/a)</td><td>119.73 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 <b>(+50.18%)</b></td><td>0.01 <b>(+35.98%)</b></td><td>0.01 (-9.43%)</td><td>0.01 (-0.45%)</td><td>0.01 <b>(+147.03%)</b></td><td>621.90 (+0.45%)</td><td>414.10 (-12.11%)</td><td>502.10 (+10.40%)</td><td>193.10 <b>(-33.39%)</b></td><td>199.25 <b>(+62.63%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>619.10 (n/a)</td><td>471.18 (n/a)</td><td>454.80 (n/a)</td><td>289.90 (n/a)</td><td>122.52 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.56 (+8.54%)</td><td>0.45 <b>(+36.47%)</b></td><td>0.46 <b>(+71.37%)</b></td><td>0.28 (+6.65%)</td><td>0.11 (-0.36%)</td><td>475.60 (-6.23%)</td><td>310.44 <b>(-27.36%)</b></td><td>285.10 <b>(-41.65%)</b></td><td>236.60 (-7.87%)</td><td>95.97 (-12.41%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.51 (n/a)</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>507.20 (n/a)</td><td>427.36 (n/a)</td><td>488.60 (n/a)</td><td>256.80 (n/a)</td><td>109.57 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.65 <b>(+26.01%)</b></td><td>0.49 (+8.44%)</td><td>0.51 (+2.78%)</td><td>0.30 (+8.65%)</td><td>0.13 <b>(+31.98%)</b></td><td>447.50 (-7.96%)</td><td>290.16 (-6.52%)</td><td>261.30 (-2.72%)</td><td>204.20 <b>(-20.64%)</b></td><td>95.09 (-3.39%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.51 (n/a)</td><td>0.45 (n/a)</td><td>0.49 (n/a)</td><td>0.27 (n/a)</td><td>0.10 (n/a)</td><td>486.20 (n/a)</td><td>310.40 (n/a)</td><td>268.60 (n/a)</td><td>257.30 (n/a)</td><td>98.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.29 <b>(-53.98%)</b></td><td>0.23 <b>(-42.38%)</b></td><td>0.25 (-11.49%)</td><td>0.12 <b>(-48.86%)</b></td><td>0.07 <b>(-61.44%)</b></td><td>1061.10 <b>(+95.56%)</b></td><td>636.26 <b>(+64.72%)</b></td><td>528.50 (+12.98%)</td><td>457.90 <b>(+117.32%)</b></td><td>252.45 <b>(+67.16%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.63 (n/a)</td><td>0.40 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>542.60 (n/a)</td><td>386.26 (n/a)</td><td>467.80 (n/a)</td><td>210.70 (n/a)</td><td>151.02 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.58 (+18.20%)</td><td>0.43 (+15.41%)</td><td>0.44 <b>(+36.18%)</b></td><td>0.21 <b>(-27.68%)</b></td><td>0.14 <b>(+50.72%)</b></td><td>626.80 <b>(+38.27%)</b></td><td>345.60 (-6.41%)</td><td>298.50 <b>(-26.57%)</b></td><td>226.60 (-15.42%)</td><td>160.73 <b>(+91.77%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.49 (n/a)</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.09 (n/a)</td><td>453.30 (n/a)</td><td>369.28 (n/a)</td><td>406.50 (n/a)</td><td>267.90 (n/a)</td><td>83.82 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.53 (-3.69%)</td><td>0.42 (-11.26%)</td><td>0.45 (-10.99%)</td><td>0.26 (-2.02%)</td><td>0.12 (+4.31%)</td><td>508.30 (+2.07%)</td><td>343.42 (+13.21%)</td><td>292.50 (+12.37%)</td><td>251.50 (+3.84%)</td><td>112.55 (+3.18%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.55 (n/a)</td><td>0.47 (n/a)</td><td>0.51 (n/a)</td><td>0.27 (n/a)</td><td>0.11 (n/a)</td><td>498.00 (n/a)</td><td>303.34 (n/a)</td><td>260.30 (n/a)</td><td>242.20 (n/a)</td><td>109.08 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 <b>(+21.38%)</b></td><td>0.01 <b>(+24.90%)</b></td><td>0.01 (-4.75%)</td><td>0.01 (-0.29%)</td><td>0.01 <b>(+68.53%)</b></td><td>533.60 (+0.30%)</td><td>404.72 (-11.46%)</td><td>519.00 (+4.98%)</td><td>213.00 (-17.63%)</td><td>166.51 <b>(+47.67%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.00 (n/a)</td><td>457.12 (n/a)</td><td>494.40 (n/a)</td><td>258.60 (n/a)</td><td>112.76 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.02 <b>(+45.96%)</b></td><td>0.01 (+15.30%)</td><td>0.01 (-18.91%)</td><td>0.01 <b>(+42.96%)</b></td><td>0.01 <b>(+32.51%)</b></td><td>434.90 <b>(-30.05%)</b></td><td>339.50 (-14.80%)</td><td>387.20 <b>(+23.31%)</b></td><td>186.10 <b>(-31.48%)</b></td><td>100.01 <b>(-36.42%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>621.70 (n/a)</td><td>398.48 (n/a)</td><td>314.00 (n/a)</td><td>271.60 (n/a)</td><td>157.29 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.00 (+0.00%)</td><td>0.00 (+5.26%)</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+26.32%)</b></td><td>19677.02 (+14.65%)</td><td>13987.29 (+9.10%)</td><td>18697.33 (+17.02%)</td><td>5733.88 (-8.65%)</td><td>7347.63 <b>(+38.41%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17162.77 (n/a)</td><td>12820.93 (n/a)</td><td>15978.49 (n/a)</td><td>6276.50 (n/a)</td><td>5308.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.00 (-7.14%)</td><td>0.00 <b>(+27.27%)</b></td><td>0.00 <b>(+80.00%)</b></td><td>0.00 <b>(+25.00%)</b></td><td>0.00 (-18.58%)</td><td>17954.73 (-5.68%)</td><td>11727.11 <b>(-22.35%)</b></td><td>9216.11 <b>(-47.31%)</b></td><td>6459.78 (+9.06%)</td><td>5378.28 (-1.82%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19036.65 (n/a)</td><td>15101.64 (n/a)</td><td>17490.54 (n/a)</td><td>5923.10 (n/a)</td><td>5477.81 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>0.16 (+18.31%)</td><td>0.13 <b>(+43.26%)</b></td><td>0.14 <b>(+72.00%)</b></td><td>0.09 (+11.84%)</td><td>0.03 <b>(+24.38%)</b></td><td>24135.86 (-10.55%)</td><td>16372.17 <b>(-29.59%)</b></td><td>14779.36 <b>(-41.86%)</b></td><td>13467.34 (-15.47%)</td><td>4414.26 (-0.50%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>26982.14 (n/a)</td><td>23253.69 (n/a)</td><td>25420.22 (n/a)</td><td>15932.03 (n/a)</td><td>4436.51 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.40 (-12.48%)</td><td>1.00 (+4.50%)</td><td>0.96 <b>(-32.68%)</b></td><td>0.78 <b>(+417.62%)</b></td><td>0.24 <b>(-67.09%)</b></td><td>668.40 <b>(-80.68%)</b></td><td>547.62 <b>(-64.92%)</b></td><td>548.00 <b>(+48.55%)</b></td><td>373.20 (+14.27%)</td><td>110.17 <b>(-93.34%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.61 (n/a)</td><td>0.95 (n/a)</td><td>1.42 (n/a)</td><td>0.15 (n/a)</td><td>0.73 (n/a)</td><td>3459.60 (n/a)</td><td>1561.14 (n/a)</td><td>368.90 (n/a)</td><td>326.60 (n/a)</td><td>1653.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>2.57 (-5.17%)</td><td>2.02 <b>(+42.89%)</b></td><td>2.30 <b>(+96.83%)</b></td><td>1.11 <b>(+264.87%)</b></td><td>0.63 <b>(-46.04%)</b></td><td>947.60 <b>(-72.59%)</b></td><td>574.92 <b>(-65.81%)</b></td><td>455.60 <b>(-49.19%)</b></td><td>407.60 (+5.43%)</td><td>229.15 <b>(-85.17%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>2.71 (n/a)</td><td>1.41 (n/a)</td><td>1.17 (n/a)</td><td>0.30 (n/a)</td><td>1.17 (n/a)</td><td>3457.50 (n/a)</td><td>1681.72 (n/a)</td><td>896.70 (n/a)</td><td>386.60 (n/a)</td><td>1545.66 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:22:28</td><td>1.98 (+11.32%)</td><td>1.05 <b>(-20.25%)</b></td><td>0.88 <b>(-41.20%)</b></td><td>0.62 (-16.40%)</td><td>0.53 (+7.03%)</td><td>842.40 (+19.63%)</td><td>576.90 <b>(+26.75%)</b></td><td>596.10 <b>(+70.07%)</b></td><td>265.50 (-10.15%)</td><td>207.26 (+6.51%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 22:06:36</td><td>1.77 (n/a)</td><td>1.32 (n/a)</td><td>1.50 (n/a)</td><td>0.74 (n/a)</td><td>0.50 (n/a)</td><td>704.20 (n/a)</td><td>455.16 (n/a)</td><td>350.50 (n/a)</td><td>295.50 (n/a)</td><td>194.59 (n/a)</td>
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
