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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.05 <b>(-23.04%)</b></td><td>0.03 (-11.23%)</td><td>0.02 (-1.82%)</td><td>0.02 (+2.35%)</td><td>0.01 <b>(-27.45%)</b></td><td>624.30 (-2.29%)</td><td>457.70 (+7.33%)</td><td>497.50 (+1.86%)</td><td>269.50 <b>(+29.94%)</b></td><td>165.46 (-6.24%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>638.90 (n/a)</td><td>426.46 (n/a)</td><td>488.40 (n/a)</td><td>207.40 (n/a)</td><td>176.47 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.05 <b>(-33.13%)</b></td><td>0.03 (-19.42%)</td><td>0.03 <b>(-34.91%)</b></td><td>0.02 (+11.49%)</td><td>0.01 <b>(-46.40%)</b></td><td>535.20 (-10.31%)</td><td>399.52 (+7.10%)</td><td>434.80 <b>(+53.64%)</b></td><td>256.10 <b>(+49.50%)</b></td><td>126.40 <b>(-36.59%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>596.70 (n/a)</td><td>373.04 (n/a)</td><td>283.00 (n/a)</td><td>171.30 (n/a)</td><td>199.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 <b>(-22.53%)</b></td><td>0.03 <b>(-25.11%)</b></td><td>0.03 <b>(-31.26%)</b></td><td>0.02 (-2.00%)</td><td>0.01 <b>(-27.20%)</b></td><td>573.40 (+2.05%)</td><td>454.48 <b>(+30.37%)</b></td><td>451.00 <b>(+45.48%)</b></td><td>313.70 <b>(+29.09%)</b></td><td>113.43 (-8.01%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>561.90 (n/a)</td><td>348.62 (n/a)</td><td>310.00 (n/a)</td><td>243.00 (n/a)</td><td>123.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (-2.03%)</td><td>0.02 (+5.51%)</td><td>0.02 (+14.01%)</td><td>0.01 (-11.73%)</td><td>0.00 (+6.49%)</td><td>505.70 (+13.28%)</td><td>316.44 (-3.57%)</td><td>263.60 (-12.28%)</td><td>246.20 (+2.07%)</td><td>108.58 <b>(+25.60%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>446.40 (n/a)</td><td>328.16 (n/a)</td><td>300.50 (n/a)</td><td>241.20 (n/a)</td><td>86.45 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (-18.78%)</td><td>0.02 (+12.70%)</td><td>0.02 <b>(+68.93%)</b></td><td>0.01 (+2.31%)</td><td>0.01 <b>(-39.71%)</b></td><td>446.90 (-2.25%)</td><td>276.44 (-17.92%)</td><td>241.00 <b>(-40.80%)</b></td><td>207.40 <b>(+23.09%)</b></td><td>96.81 <b>(-23.93%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>457.20 (n/a)</td><td>336.80 (n/a)</td><td>407.10 (n/a)</td><td>168.50 (n/a)</td><td>127.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (+7.53%)</td><td>0.01 (-2.60%)</td><td>0.01 (-8.22%)</td><td>0.01 <b>(-33.65%)</b></td><td>0.01 <b>(+81.41%)</b></td><td>673.40 <b>(+50.72%)</b></td><td>420.60 (+17.07%)</td><td>422.80 (+8.94%)</td><td>232.00 (-7.01%)</td><td>189.68 <b>(+139.15%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>446.80 (n/a)</td><td>359.26 (n/a)</td><td>388.10 (n/a)</td><td>249.50 (n/a)</td><td>79.31 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (+11.11%)</td><td>0.01 <b>(+24.55%)</b></td><td>0.01 <b>(+42.82%)</b></td><td>0.00 <b>(+30.25%)</b></td><td>0.01 (+7.52%)</td><td>1874.40 <b>(-23.22%)</b></td><td>680.58 <b>(-23.73%)</b></td><td>421.80 <b>(-29.98%)</b></td><td>269.70 (-10.01%)</td><td>674.23 <b>(-23.64%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2441.30 (n/a)</td><td>892.38 (n/a)</td><td>602.40 (n/a)</td><td>299.70 (n/a)</td><td>882.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.01 <b>(-37.52%)</b></td><td>0.01 (-15.54%)</td><td>0.01 <b>(+31.85%)</b></td><td>0.01 <b>(-39.16%)</b></td><td>0.00 <b>(-44.78%)</b></td><td>1048.50 <b>(+64.37%)</b></td><td>549.10 (+15.60%)</td><td>434.10 <b>(-24.15%)</b></td><td>378.70 <b>(+60.06%)</b></td><td>280.68 <b>(+51.29%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.90 (n/a)</td><td>475.02 (n/a)</td><td>572.30 (n/a)</td><td>236.60 (n/a)</td><td>185.53 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 <b>(+56.74%)</b></td><td>0.01 <b>(+29.08%)</b></td><td>0.01 (+19.86%)</td><td>0.01 (+15.32%)</td><td>0.00 <b>(+203.45%)</b></td><td>507.90 (-13.28%)</td><td>405.30 (-19.81%)</td><td>410.40 (-16.57%)</td><td>279.50 <b>(-36.19%)</b></td><td>88.96 <b>(+65.25%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>585.70 (n/a)</td><td>505.42 (n/a)</td><td>491.90 (n/a)</td><td>438.00 (n/a)</td><td>53.83 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>383.80 (n/a)</td><td>316.70 (n/a)</td><td>303.40 (n/a)</td><td>242.80 (n/a)</td><td>63.61 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>507.50 (n/a)</td><td>325.44 (n/a)</td><td>271.10 (n/a)</td><td>156.30 (n/a)</td><td>146.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1887.90 (n/a)</td><td>687.20 (n/a)</td><td>330.70 (n/a)</td><td>291.40 (n/a)</td><td>686.29 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>471.70 (n/a)</td><td>316.92 (n/a)</td><td>300.60 (n/a)</td><td>246.00 (n/a)</td><td>89.70 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.50 (n/a)</td><td>304.20 (n/a)</td><td>246.20 (n/a)</td><td>232.50 (n/a)</td><td>121.60 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1701.40 (n/a)</td><td>626.84 (n/a)</td><td>346.80 (n/a)</td><td>276.60 (n/a)</td><td>607.19 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/flm/dequant</summary>


### test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of]

_No metrics available._


### test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of]

_No metrics available._


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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.97 <b>(-22.18%)</b></td><td>0.66 (-12.28%)</td><td>0.67 (+2.98%)</td><td>0.22 <b>(-57.23%)</b></td><td>0.28 (-0.24%)</td><td>2120.70 <b>(+133.84%)</b></td><td>916.62 <b>(+37.33%)</b></td><td>683.00 (-2.90%)</td><td>475.20 <b>(+28.50%)</b></td><td>681.68 <b>(+251.87%)</b></td><td>70.62 <b>(-22.18%)</b></td><td>48.18 (-12.28%)</td><td>49.13 (+2.98%)</td><td>15.82 <b>(-57.23%)</b></td><td>20.73 (-0.24%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.24 (n/a)</td><td>0.75 (n/a)</td><td>0.65 (n/a)</td><td>0.51 (n/a)</td><td>0.28 (n/a)</td><td>906.90 (n/a)</td><td>667.46 (n/a)</td><td>703.40 (n/a)</td><td>369.80 (n/a)</td><td>193.73 (n/a)</td><td>90.74 (n/a)</td><td>54.92 (n/a)</td><td>47.71 (n/a)</td><td>37.00 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.48 (-18.67%)</td><td>1.14 (-10.77%)</td><td>1.12 (-4.05%)</td><td>0.59 <b>(-33.18%)</b></td><td>0.36 (-1.07%)</td><td>1118.80 <b>(+49.65%)</b></td><td>640.48 (+17.76%)</td><td>586.70 (+4.23%)</td><td>443.40 <b>(+22.96%)</b></td><td>277.07 <b>(+87.96%)</b></td><td>151.34 (-18.67%)</td><td>117.10 (-10.77%)</td><td>114.39 (-4.05%)</td><td>59.98 <b>(-33.18%)</b></td><td>36.80 (-1.07%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.82 (n/a)</td><td>1.28 (n/a)</td><td>1.16 (n/a)</td><td>0.88 (n/a)</td><td>0.36 (n/a)</td><td>747.60 (n/a)</td><td>543.90 (n/a)</td><td>562.90 (n/a)</td><td>360.60 (n/a)</td><td>147.41 (n/a)</td><td>186.08 (n/a)</td><td>131.24 (n/a)</td><td>119.22 (n/a)</td><td>89.77 (n/a)</td><td>37.20 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.36 (-9.85%)</td><td>1.07 (+9.60%)</td><td>0.99 (+17.98%)</td><td>0.97 <b>(+45.70%)</b></td><td>0.17 <b>(-52.89%)</b></td><td>780.90 <b>(-31.36%)</b></td><td>714.38 (-15.51%)</td><td>764.60 (-15.24%)</td><td>553.60 (+10.92%)</td><td>94.66 <b>(-64.50%)</b></td><td>151.53 (-9.85%)</td><td>119.39 (+9.60%)</td><td>109.71 (+17.98%)</td><td>107.42 <b>(+45.70%)</b></td><td>18.54 <b>(-52.89%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.51 (n/a)</td><td>0.98 (n/a)</td><td>0.84 (n/a)</td><td>0.66 (n/a)</td><td>0.35 (n/a)</td><td>1137.70 (n/a)</td><td>845.52 (n/a)</td><td>902.10 (n/a)</td><td>499.10 (n/a)</td><td>266.66 (n/a)</td><td>168.09 (n/a)</td><td>108.93 (n/a)</td><td>92.99 (n/a)</td><td>73.73 (n/a)</td><td>39.36 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.62 (+1.42%)</td><td>1.14 <b>(+20.19%)</b></td><td>1.38 <b>(+21.24%)</b></td><td>0.28 (-6.12%)</td><td>0.53 (-1.11%)</td><td>3719.70 (+6.52%)</td><td>1382.58 (-14.33%)</td><td>760.00 (-17.52%)</td><td>649.20 (-1.40%)</td><td>1316.01 (+9.31%)</td><td>206.76 (+1.42%)</td><td>146.38 <b>(+20.19%)</b></td><td>176.61 <b>(+21.24%)</b></td><td>36.08 (-6.12%)</td><td>68.40 (-1.11%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.59 (n/a)</td><td>0.95 (n/a)</td><td>1.14 (n/a)</td><td>0.30 (n/a)</td><td>0.54 (n/a)</td><td>3491.90 (n/a)</td><td>1613.90 (n/a)</td><td>921.40 (n/a)</td><td>658.40 (n/a)</td><td>1203.94 (n/a)</td><td>203.86 (n/a)</td><td>121.79 (n/a)</td><td>145.67 (n/a)</td><td>38.44 (n/a)</td><td>69.17 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.78 <b>(+30.94%)</b></td><td>1.31 <b>(+35.81%)</b></td><td>1.24 (-4.52%)</td><td>0.90 <b>(+193.81%)</b></td><td>0.32 <b>(-38.50%)</b></td><td>1168.40 <b>(-65.96%)</b></td><td>842.78 <b>(-46.63%)</b></td><td>845.80 (+4.73%)</td><td>590.60 <b>(-23.63%)</b></td><td>210.05 <b>(-82.24%)</b></td><td>227.27 <b>(+30.94%)</b></td><td>167.10 <b>(+35.81%)</b></td><td>158.68 (-4.52%)</td><td>114.87 <b>(+193.81%)</b></td><td>40.59 <b>(-38.50%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.36 (n/a)</td><td>0.96 (n/a)</td><td>1.30 (n/a)</td><td>0.31 (n/a)</td><td>0.52 (n/a)</td><td>3432.90 (n/a)</td><td>1579.18 (n/a)</td><td>807.60 (n/a)</td><td>773.30 (n/a)</td><td>1183.06 (n/a)</td><td>173.57 (n/a)</td><td>123.03 (n/a)</td><td>166.20 (n/a)</td><td>39.10 (n/a)</td><td>65.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>2.17 (+0.47%)</td><td>1.45 (-10.46%)</td><td>1.75 (+6.36%)</td><td>0.53 <b>(-43.10%)</b></td><td>0.67 <b>(+31.09%)</b></td><td>1985.30 <b>(+75.74%)</b></td><td>940.04 <b>(+31.90%)</b></td><td>598.90 (-5.98%)</td><td>483.80 (-0.47%)</td><td>623.39 <b>(+136.96%)</b></td><td>277.40 (+0.47%)</td><td>185.33 (-10.46%)</td><td>224.09 (+6.36%)</td><td>67.61 <b>(-43.10%)</b></td><td>85.21 <b>(+31.09%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>2.16 (n/a)</td><td>1.62 (n/a)</td><td>1.65 (n/a)</td><td>0.93 (n/a)</td><td>0.51 (n/a)</td><td>1129.70 (n/a)</td><td>712.70 (n/a)</td><td>637.00 (n/a)</td><td>486.10 (n/a)</td><td>263.07 (n/a)</td><td>276.10 (n/a)</td><td>206.97 (n/a)</td><td>210.70 (n/a)</td><td>118.81 (n/a)</td><td>65.00 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.72 (-6.26%)</td><td>1.19 <b>(+26.58%)</b></td><td>1.16 <b>(+134.96%)</b></td><td>0.75 <b>(+152.85%)</b></td><td>0.35 <b>(-54.27%)</b></td><td>1392.60 <b>(-60.45%)</b></td><td>942.66 <b>(-50.82%)</b></td><td>905.30 <b>(-57.44%)</b></td><td>609.10 (+6.67%)</td><td>283.74 <b>(-78.25%)</b></td><td>220.34 (-6.26%)</td><td>152.58 <b>(+26.58%)</b></td><td>148.25 <b>(+134.96%)</b></td><td>96.38 <b>(+152.85%)</b></td><td>44.44 <b>(-54.27%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.84 (n/a)</td><td>0.94 (n/a)</td><td>0.49 (n/a)</td><td>0.30 (n/a)</td><td>0.76 (n/a)</td><td>3521.30 (n/a)</td><td>1916.76 (n/a)</td><td>2127.10 (n/a)</td><td>571.00 (n/a)</td><td>1304.80 (n/a)</td><td>235.05 (n/a)</td><td>120.54 (n/a)</td><td>63.10 (n/a)</td><td>38.12 (n/a)</td><td>97.17 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.68 <b>(-24.20%)</b></td><td>0.53 (-18.05%)</td><td>0.50 (-3.83%)</td><td>0.44 (-6.96%)</td><td>0.09 <b>(-53.70%)</b></td><td>825.90 (+7.48%)</td><td>694.32 (+16.24%)</td><td>716.90 (+3.99%)</td><td>527.90 <b>(+31.91%)</b></td><td>107.65 <b>(-35.13%)</b></td><td>31.78 <b>(-24.20%)</b></td><td>24.69 (-18.05%)</td><td>23.40 (-3.83%)</td><td>20.31 (-6.96%)</td><td>4.27 <b>(-53.70%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.90 (n/a)</td><td>0.65 (n/a)</td><td>0.52 (n/a)</td><td>0.47 (n/a)</td><td>0.20 (n/a)</td><td>768.40 (n/a)</td><td>597.34 (n/a)</td><td>689.40 (n/a)</td><td>400.20 (n/a)</td><td>165.95 (n/a)</td><td>41.92 (n/a)</td><td>30.13 (n/a)</td><td>24.34 (n/a)</td><td>21.83 (n/a)</td><td>9.22 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>3.43 (-15.87%)</td><td>2.73 (-5.79%)</td><td>3.17 (+18.86%)</td><td>1.11 (-13.07%)</td><td>0.96 (-16.74%)</td><td>2358.00 (+15.04%)</td><td>1148.12 (+6.73%)</td><td>826.30 (-15.86%)</td><td>764.70 (+18.87%)</td><td>682.66 (+19.09%)</td><td>702.10 (-15.87%)</td><td>559.02 (-5.79%)</td><td>649.74 (+18.86%)</td><td>227.68 (-13.07%)</td><td>195.93 (-16.74%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>4.07 (n/a)</td><td>2.90 (n/a)</td><td>2.67 (n/a)</td><td>1.28 (n/a)</td><td>1.15 (n/a)</td><td>2049.80 (n/a)</td><td>1075.74 (n/a)</td><td>982.10 (n/a)</td><td>643.30 (n/a)</td><td>573.21 (n/a)</td><td>834.50 (n/a)</td><td>593.40 (n/a)</td><td>546.64 (n/a)</td><td>261.92 (n/a)</td><td>235.32 (n/a)</td>
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


### test_gemm_tile_options[tn128-ma32-default]

_No metrics available._


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn16-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn32-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma16-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma32-default]

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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>463.70 (n/a)</td><td>312.34 (n/a)</td><td>276.30 (n/a)</td><td>238.50 (n/a)</td><td>88.42 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.20 (n/a)</td><td>343.82 (n/a)</td><td>295.40 (n/a)</td><td>279.90 (n/a)</td><td>90.55 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.10 (n/a)</td><td>403.44 (n/a)</td><td>486.70 (n/a)</td><td>193.40 (n/a)</td><td>163.83 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.10 (n/a)</td><td>395.76 (n/a)</td><td>459.90 (n/a)</td><td>235.60 (n/a)</td><td>135.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2121.90 (n/a)</td><td>727.36 (n/a)</td><td>403.70 (n/a)</td><td>231.40 (n/a)</td><td>791.35 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.50 (n/a)</td><td>407.04 (n/a)</td><td>417.80 (n/a)</td><td>237.30 (n/a)</td><td>164.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.51 (-8.77%)</td><td>0.37 (-0.03%)</td><td>0.38 (+3.02%)</td><td>0.17 (-0.45%)</td><td>0.13 (-9.28%)</td><td>1300.90 (+0.46%)</td><td>686.72 (-0.86%)</td><td>584.50 (-2.94%)</td><td>437.30 (+9.60%)</td><td>349.93 (+0.19%)</td><td>21.58 (-8.77%)</td><td>15.85 (-0.03%)</td><td>16.15 (+3.02%)</td><td>7.25 (-0.45%)</td><td>5.37 (-9.28%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.55 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>1295.00 (n/a)</td><td>692.66 (n/a)</td><td>602.20 (n/a)</td><td>399.00 (n/a)</td><td>349.27 (n/a)</td><td>23.66 (n/a)</td><td>15.86 (n/a)</td><td>15.67 (n/a)</td><td>7.29 (n/a)</td><td>5.92 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.47 <b>(-21.49%)</b></td><td>0.36 (-17.52%)</td><td>0.37 (-9.65%)</td><td>0.19 <b>(-44.25%)</b></td><td>0.11 (+3.75%)</td><td>1180.80 <b>(+79.37%)</b></td><td>684.00 <b>(+29.05%)</b></td><td>602.40 (+10.67%)</td><td>465.80 <b>(+27.37%)</b></td><td>284.11 <b>(+166.60%)</b></td><td>20.26 <b>(-21.49%)</b></td><td>15.25 (-17.52%)</td><td>15.67 (-9.65%)</td><td>7.99 <b>(-44.25%)</b></td><td>4.51 (+3.75%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.60 (n/a)</td><td>0.43 (n/a)</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.10 (n/a)</td><td>658.30 (n/a)</td><td>530.04 (n/a)</td><td>544.30 (n/a)</td><td>365.70 (n/a)</td><td>106.57 (n/a)</td><td>25.80 (n/a)</td><td>18.49 (n/a)</td><td>17.34 (n/a)</td><td>14.33 (n/a)</td><td>4.35 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.30 (-1.12%)</td><td>0.30 (-1.65%)</td><td>0.30 (-2.77%)</td><td>0.29 (-0.73%)</td><td>0.00 (-19.00%)</td><td>85863.60 (+0.74%)</td><td>84569.42 (+1.66%)</td><td>85036.20 (+2.84%)</td><td>82577.40 (+1.13%)</td><td>1392.87 (-17.33%)</td><td>208.05 (-1.12%)</td><td>203.19 (-1.65%)</td><td>202.03 (-2.77%)</td><td>200.08 (-0.73%)</td><td>3.37 (-19.00%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>85232.60 (n/a)</td><td>83185.76 (n/a)</td><td>82684.10 (n/a)</td><td>81656.20 (n/a)</td><td>1684.88 (n/a)</td><td>210.39 (n/a)</td><td>206.59 (n/a)</td><td>207.78 (n/a)</td><td>201.56 (n/a)</td><td>4.16 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.16 (+0.89%)</td><td>1.15 (+0.75%)</td><td>1.15 (-0.25%)</td><td>1.14 (+3.27%)</td><td>0.01 <b>(-60.35%)</b></td><td>22130.60 (-3.16%)</td><td>21940.88 (-0.77%)</td><td>21973.90 (+0.25%)</td><td>21691.20 (-0.89%)</td><td>158.73 <b>(-62.04%)</b></td><td>792.02 (+0.89%)</td><td>783.04 (+0.75%)</td><td>781.83 (-0.25%)</td><td>776.29 (+3.27%)</td><td>5.69 <b>(-60.35%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>1.15 (n/a)</td><td>1.10 (n/a)</td><td>0.02 (n/a)</td><td>22853.70 (n/a)</td><td>22110.34 (n/a)</td><td>21919.30 (n/a)</td><td>21885.00 (n/a)</td><td>418.12 (n/a)</td><td>785.01 (n/a)</td><td>777.22 (n/a)</td><td>783.78 (n/a)</td><td>751.73 (n/a)</td><td>14.35 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>4.12 (-1.77%)</td><td>2.96 (+1.85%)</td><td>3.13 (+19.46%)</td><td>1.84 (-4.78%)</td><td>1.01 (+3.05%)</td><td>4390.30 (+5.02%)</td><td>3024.24 (-0.36%)</td><td>2578.40 (-16.29%)</td><td>1957.90 (+1.80%)</td><td>1103.93 (+13.67%)</td><td>1079.67 (-1.77%)</td><td>775.10 (+1.85%)</td><td>819.85 (+19.46%)</td><td>481.50 (-4.78%)</td><td>264.23 (+3.05%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>4.19 (n/a)</td><td>2.90 (n/a)</td><td>2.62 (n/a)</td><td>1.93 (n/a)</td><td>0.98 (n/a)</td><td>4180.50 (n/a)</td><td>3035.26 (n/a)</td><td>3080.20 (n/a)</td><td>1923.30 (n/a)</td><td>971.19 (n/a)</td><td>1099.13 (n/a)</td><td>761.01 (n/a)</td><td>686.29 (n/a)</td><td>505.66 (n/a)</td><td>256.42 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.31 <b>(+44.41%)</b></td><td>0.24 (+19.13%)</td><td>0.21 (+7.91%)</td><td>0.17 (-8.86%)</td><td>0.06 <b>(+530.43%)</b></td><td>7136.90 (+9.73%)</td><td>5538.68 (-11.45%)</td><td>5940.60 (-7.33%)</td><td>4016.90 <b>(-30.75%)</b></td><td>1405.71 <b>(+358.05%)</b></td><td>16.71 <b>(+44.41%)</b></td><td>12.81 (+19.13%)</td><td>11.30 (+7.91%)</td><td>9.40 (-8.86%)</td><td>3.43 <b>(+530.42%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>6504.20 (n/a)</td><td>6254.52 (n/a)</td><td>6410.80 (n/a)</td><td>5800.70 (n/a)</td><td>306.89 (n/a)</td><td>11.57 (n/a)</td><td>10.75 (n/a)</td><td>10.47 (n/a)</td><td>10.32 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>3.76 (n/a)</td><td>3.58 (n/a)</td><td>3.54 (n/a)</td><td>3.36 (n/a)</td><td>0.16 (n/a)</td><td>3.76 (n/a)</td><td>3.58 (n/a)</td><td>3.53 (n/a)</td><td>3.36 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>7.54 (+5.21%)</td><td>6.58 (+3.67%)</td><td>6.41 (-1.98%)</td><td>5.43 (-4.33%)</td><td>0.86 <b>(+41.20%)</b></td><td>7.53 (+5.21%)</td><td>6.58 (+3.67%)</td><td>6.41 (-1.98%)</td><td>5.43 (-4.33%)</td><td>0.86 <b>(+41.20%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>7.16 (n/a)</td><td>6.35 (n/a)</td><td>6.54 (n/a)</td><td>5.68 (n/a)</td><td>0.61 (n/a)</td><td>7.16 (n/a)</td><td>6.35 (n/a)</td><td>6.54 (n/a)</td><td>5.68 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>13.79 <b>(+30.09%)</b></td><td>11.89 <b>(+33.77%)</b></td><td>13.55 <b>(+60.90%)</b></td><td>8.59 (+18.80%)</td><td>2.52 <b>(+83.01%)</b></td><td>13.78 <b>(+30.09%)</b></td><td>11.89 <b>(+33.77%)</b></td><td>13.54 <b>(+60.90%)</b></td><td>8.59 (+18.80%)</td><td>2.52 <b>(+83.01%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>10.60 (n/a)</td><td>8.89 (n/a)</td><td>8.42 (n/a)</td><td>7.23 (n/a)</td><td>1.38 (n/a)</td><td>10.59 (n/a)</td><td>8.89 (n/a)</td><td>8.41 (n/a)</td><td>7.23 (n/a)</td><td>1.37 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>3.78 (n/a)</td><td>3.60 (n/a)</td><td>3.73 (n/a)</td><td>3.31 (n/a)</td><td>0.22 (n/a)</td><td>3.78 (n/a)</td><td>3.60 (n/a)</td><td>3.72 (n/a)</td><td>3.31 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>7.45 (-2.16%)</td><td>6.44 (-6.91%)</td><td>6.26 (-12.48%)</td><td>5.94 (+3.57%)</td><td>0.63 (-16.73%)</td><td>7.44 (-2.16%)</td><td>6.44 (-6.91%)</td><td>6.26 (-12.48%)</td><td>5.94 (+3.57%)</td><td>0.63 (-16.73%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>7.61 (n/a)</td><td>6.92 (n/a)</td><td>7.16 (n/a)</td><td>5.74 (n/a)</td><td>0.75 (n/a)</td><td>7.61 (n/a)</td><td>6.92 (n/a)</td><td>7.15 (n/a)</td><td>5.73 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>11.16 (-13.87%)</td><td>8.54 (-9.91%)</td><td>8.28 (-0.78%)</td><td>6.53 (-12.32%)</td><td>1.77 <b>(-27.16%)</b></td><td>11.15 (-13.87%)</td><td>8.53 (-9.91%)</td><td>8.28 (-0.78%)</td><td>6.53 (-12.32%)</td><td>1.77 <b>(-27.16%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>12.95 (n/a)</td><td>9.47 (n/a)</td><td>8.35 (n/a)</td><td>7.45 (n/a)</td><td>2.43 (n/a)</td><td>12.94 (n/a)</td><td>9.47 (n/a)</td><td>8.34 (n/a)</td><td>7.44 (n/a)</td><td>2.43 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>3.00 (+0.19%)</td><td>2.21 (-3.22%)</td><td>2.77 (+0.76%)</td><td>1.23 <b>(+21.34%)</b></td><td>0.89 (+0.71%)</td><td>3.00 (+0.19%)</td><td>2.21 (-3.22%)</td><td>2.76 (+0.76%)</td><td>1.23 <b>(+21.34%)</b></td><td>0.89 (+0.71%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>3.00 (n/a)</td><td>2.29 (n/a)</td><td>2.75 (n/a)</td><td>1.01 (n/a)</td><td>0.89 (n/a)</td><td>2.99 (n/a)</td><td>2.28 (n/a)</td><td>2.74 (n/a)</td><td>1.01 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.41 <b>(-30.35%)</b></td><td>0.20 <b>(-59.06%)</b></td><td>0.11 <b>(-77.91%)</b></td><td>0.08 <b>(-77.71%)</b></td><td>0.15 <b>(+73.99%)</b></td><td>0.40 <b>(-30.35%)</b></td><td>0.19 <b>(-59.06%)</b></td><td>0.11 <b>(-77.91%)</b></td><td>0.07 <b>(-77.71%)</b></td><td>0.15 <b>(+73.99%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.58 (n/a)</td><td>0.48 (n/a)</td><td>0.50 (n/a)</td><td>0.34 (n/a)</td><td>0.09 (n/a)</td><td>0.58 (n/a)</td><td>0.47 (n/a)</td><td>0.49 (n/a)</td><td>0.33 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.85 (+2.84%)</td><td>0.54 <b>(+36.06%)</b></td><td>0.47 (+0.09%)</td><td>0.29 <b>(+268.63%)</b></td><td>0.22 <b>(-26.44%)</b></td><td>0.84 (+2.84%)</td><td>0.54 <b>(+36.06%)</b></td><td>0.47 (+0.09%)</td><td>0.29 <b>(+268.63%)</b></td><td>0.22 <b>(-26.44%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.82 (n/a)</td><td>0.40 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>0.30 (n/a)</td><td>0.81 (n/a)</td><td>0.39 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.89 (+6.49%)</td><td>1.25 (+16.20%)</td><td>1.19 (-0.57%)</td><td>0.74 <b>(+72.62%)</b></td><td>0.52 (-15.55%)</td><td>1.86 (+6.49%)</td><td>1.23 (+16.20%)</td><td>1.17 (-0.57%)</td><td>0.73 <b>(+72.62%)</b></td><td>0.51 (-15.55%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.78 (n/a)</td><td>1.07 (n/a)</td><td>1.19 (n/a)</td><td>0.43 (n/a)</td><td>0.61 (n/a)</td><td>1.75 (n/a)</td><td>1.06 (n/a)</td><td>1.18 (n/a)</td><td>0.42 (n/a)</td><td>0.60 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>429.80 (n/a)</td><td>326.82 (n/a)</td><td>288.20 (n/a)</td><td>246.40 (n/a)</td><td>89.57 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>654.80 (n/a)</td><td>381.02 (n/a)</td><td>265.80 (n/a)</td><td>246.60 (n/a)</td><td>184.45 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.00 (n/a)</td><td>405.84 (n/a)</td><td>418.90 (n/a)</td><td>245.00 (n/a)</td><td>152.61 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1022.20 (n/a)</td><td>603.50 (n/a)</td><td>530.40 (n/a)</td><td>346.30 (n/a)</td><td>255.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.70 (n/a)</td><td>382.04 (n/a)</td><td>356.50 (n/a)</td><td>218.20 (n/a)</td><td>128.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>789.80 (n/a)</td><td>487.24 (n/a)</td><td>482.00 (n/a)</td><td>308.30 (n/a)</td><td>186.56 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (+15.24%)</td><td>0.03 (+18.28%)</td><td>0.03 (+13.67%)</td><td>0.02 <b>(+22.73%)</b></td><td>0.01 (-4.64%)</td><td>346.80 (-18.52%)</td><td>268.30 (-17.40%)</td><td>246.90 (-12.01%)</td><td>205.20 (-13.20%)</td><td>60.12 <b>(-34.96%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>425.60 (n/a)</td><td>324.80 (n/a)</td><td>280.60 (n/a)</td><td>236.40 (n/a)</td><td>92.44 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (-17.91%)</td><td>0.03 (-12.95%)</td><td>0.03 (-6.79%)</td><td>0.02 (-15.31%)</td><td>0.01 (-14.33%)</td><td>476.60 (+18.09%)</td><td>321.42 (+15.32%)</td><td>280.70 (+7.30%)</td><td>235.30 <b>(+21.79%)</b></td><td>97.09 <b>(+22.80%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>403.60 (n/a)</td><td>278.72 (n/a)</td><td>261.60 (n/a)</td><td>193.20 (n/a)</td><td>79.07 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (-6.36%)</td><td>0.03 (-2.70%)</td><td>0.03 (+15.79%)</td><td>0.02 (-11.41%)</td><td>0.01 <b>(+38.24%)</b></td><td>512.70 (+12.88%)</td><td>339.20 (+8.45%)</td><td>253.90 (-13.64%)</td><td>244.60 (+6.81%)</td><td>127.83 <b>(+52.42%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>454.20 (n/a)</td><td>312.78 (n/a)</td><td>294.00 (n/a)</td><td>229.00 (n/a)</td><td>83.86 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (-4.82%)</td><td>0.02 (-0.69%)</td><td>0.03 (-0.75%)</td><td>0.01 (+0.75%)</td><td>0.01 (-10.31%)</td><td>558.00 (-0.75%)</td><td>369.20 (-1.21%)</td><td>301.40 (+0.77%)</td><td>248.90 (+5.07%)</td><td>132.03 (-8.37%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.20 (n/a)</td><td>373.72 (n/a)</td><td>299.10 (n/a)</td><td>236.90 (n/a)</td><td>144.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 <b>(-40.62%)</b></td><td>0.02 <b>(-20.91%)</b></td><td>0.02 (+10.76%)</td><td>0.01 (-7.88%)</td><td>0.00 <b>(-66.94%)</b></td><td>645.50 (+8.56%)</td><td>479.26 (+12.63%)</td><td>464.60 (-9.72%)</td><td>386.30 <b>(+68.40%)</b></td><td>101.98 <b>(-37.98%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.60 (n/a)</td><td>425.50 (n/a)</td><td>514.60 (n/a)</td><td>229.40 (n/a)</td><td>164.42 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (-5.09%)</td><td>0.02 (-3.12%)</td><td>0.02 <b>(+22.25%)</b></td><td>0.02 (+10.93%)</td><td>0.01 <b>(-27.81%)</b></td><td>532.60 (-9.85%)</td><td>403.16 (-7.24%)</td><td>455.80 (-18.20%)</td><td>220.10 (+5.36%)</td><td>126.55 <b>(-34.38%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.80 (n/a)</td><td>434.62 (n/a)</td><td>557.20 (n/a)</td><td>208.90 (n/a)</td><td>192.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (-1.44%)</td><td>0.02 (-0.45%)</td><td>0.02 <b>(+32.20%)</b></td><td>0.02 <b>(+22.04%)</b></td><td>0.01 <b>(-32.40%)</b></td><td>527.60 (-18.05%)</td><td>407.66 (-10.99%)</td><td>427.70 <b>(-24.35%)</b></td><td>236.60 (+1.50%)</td><td>113.54 <b>(-43.64%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.80 (n/a)</td><td>457.98 (n/a)</td><td>565.40 (n/a)</td><td>233.10 (n/a)</td><td>201.46 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (-1.15%)</td><td>0.02 (-5.31%)</td><td>0.02 (-15.27%)</td><td>0.01 (+9.36%)</td><td>0.01 (-10.44%)</td><td>627.00 (-8.56%)</td><td>479.32 (+2.70%)</td><td>513.10 (+18.01%)</td><td>286.90 (+1.16%)</td><td>125.73 <b>(-21.92%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>685.70 (n/a)</td><td>466.70 (n/a)</td><td>434.80 (n/a)</td><td>283.60 (n/a)</td><td>161.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 <b>(+36.37%)</b></td><td>0.02 (-13.28%)</td><td>0.02 <b>(-37.36%)</b></td><td>0.01 <b>(-32.96%)</b></td><td>0.01 <b>(+139.99%)</b></td><td>693.20 <b>(+49.17%)</b></td><td>437.56 <b>(+35.08%)</b></td><td>477.60 <b>(+59.63%)</b></td><td>194.50 <b>(-26.69%)</b></td><td>194.68 <b>(+142.91%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>464.70 (n/a)</td><td>323.92 (n/a)</td><td>299.20 (n/a)</td><td>265.30 (n/a)</td><td>80.14 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (-9.37%)</td><td>0.02 (-3.37%)</td><td>0.02 (+11.01%)</td><td>0.01 (-7.19%)</td><td>0.01 (-15.02%)</td><td>570.80 (+7.74%)</td><td>419.62 (+2.66%)</td><td>401.60 (-9.91%)</td><td>281.80 (+10.34%)</td><td>110.41 (+3.41%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>529.80 (n/a)</td><td>408.76 (n/a)</td><td>445.80 (n/a)</td><td>255.40 (n/a)</td><td>106.77 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (-18.37%)</td><td>0.02 <b>(-20.30%)</b></td><td>0.02 <b>(-41.07%)</b></td><td>0.02 <b>(+34.22%)</b></td><td>0.01 <b>(-46.34%)</b></td><td>460.40 <b>(-25.49%)</b></td><td>402.10 (+8.75%)</td><td>437.90 <b>(+69.66%)</b></td><td>249.80 <b>(+22.51%)</b></td><td>88.12 <b>(-53.52%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.90 (n/a)</td><td>369.76 (n/a)</td><td>258.10 (n/a)</td><td>203.90 (n/a)</td><td>189.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (+2.53%)</td><td>0.02 (+13.04%)</td><td>0.02 <b>(+32.14%)</b></td><td>0.01 <b>(-35.14%)</b></td><td>0.01 (+10.85%)</td><td>1034.20 <b>(+54.17%)</b></td><td>485.22 (-1.27%)</td><td>414.80 <b>(-24.32%)</b></td><td>234.70 (-2.45%)</td><td>316.34 <b>(+86.81%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>670.80 (n/a)</td><td>491.48 (n/a)</td><td>548.10 (n/a)</td><td>240.60 (n/a)</td><td>169.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (+19.45%)</td><td>0.02 <b>(-24.49%)</b></td><td>0.02 <b>(-32.91%)</b></td><td>0.02 <b>(-44.15%)</b></td><td>0.01 <b>(+555.34%)</b></td><td>537.60 <b>(+79.02%)</b></td><td>408.94 <b>(+47.15%)</b></td><td>409.40 <b>(+49.04%)</b></td><td>221.90 (-16.30%)</td><td>134.05 <b>(+899.54%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>300.30 (n/a)</td><td>277.90 (n/a)</td><td>274.70 (n/a)</td><td>265.10 (n/a)</td><td>13.41 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (-17.14%)</td><td>0.02 (-12.59%)</td><td>0.02 (-8.20%)</td><td>0.01 <b>(-35.99%)</b></td><td>0.01 (-4.58%)</td><td>731.60 <b>(+56.22%)</b></td><td>455.74 <b>(+20.13%)</b></td><td>476.20 (+8.95%)</td><td>258.10 <b>(+20.66%)</b></td><td>189.14 <b>(+68.88%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>468.30 (n/a)</td><td>379.38 (n/a)</td><td>437.10 (n/a)</td><td>213.90 (n/a)</td><td>111.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.10 (-14.77%)</td><td>0.09 (+1.77%)</td><td>0.09 (+6.69%)</td><td>0.08 (+2.32%)</td><td>0.01 <b>(-52.01%)</b></td><td>300.80 (-2.27%)</td><td>266.04 (-3.12%)</td><td>262.60 (-6.28%)</td><td>245.80 (+17.33%)</td><td>22.03 <b>(-44.33%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>307.80 (n/a)</td><td>274.60 (n/a)</td><td>280.20 (n/a)</td><td>209.50 (n/a)</td><td>39.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.16 (+16.99%)</td><td>0.14 <b>(+27.09%)</b></td><td>0.14 <b>(+22.01%)</b></td><td>0.12 <b>(+46.81%)</b></td><td>0.02 <b>(-26.86%)</b></td><td>351.60 <b>(-31.87%)</b></td><td>294.88 <b>(-23.14%)</b></td><td>291.60 (-18.04%)</td><td>257.20 (-14.52%)</td><td>35.53 <b>(-57.59%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>516.10 (n/a)</td><td>383.68 (n/a)</td><td>355.80 (n/a)</td><td>300.90 (n/a)</td><td>83.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (-11.09%)</td><td>0.02 (+10.80%)</td><td>0.02 <b>(+25.66%)</b></td><td>0.01 (+18.42%)</td><td>0.00 <b>(-42.58%)</b></td><td>429.60 (-15.55%)</td><td>305.98 (-15.49%)</td><td>280.10 <b>(-20.43%)</b></td><td>261.30 (+12.48%)</td><td>70.28 <b>(-43.65%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>508.70 (n/a)</td><td>362.08 (n/a)</td><td>352.00 (n/a)</td><td>232.30 (n/a)</td><td>124.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (+16.92%)</td><td>0.03 (+19.60%)</td><td>0.03 (+5.98%)</td><td>0.03 <b>(+102.39%)</b></td><td>0.00 <b>(-57.76%)</b></td><td>273.10 <b>(-50.59%)</b></td><td>244.42 <b>(-23.23%)</b></td><td>247.60 (-5.68%)</td><td>211.20 (-14.49%)</td><td>22.22 <b>(-83.07%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.70 (n/a)</td><td>318.38 (n/a)</td><td>262.50 (n/a)</td><td>247.00 (n/a)</td><td>131.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.05 (-10.82%)</td><td>0.05 (+2.10%)</td><td>0.05 (-3.76%)</td><td>0.04 <b>(+108.72%)</b></td><td>0.01 <b>(-65.33%)</b></td><td>313.70 <b>(-52.09%)</b></td><td>272.48 (-15.95%)</td><td>252.40 (+3.87%)</td><td>245.50 (+12.15%)</td><td>32.24 <b>(-82.62%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>654.80 (n/a)</td><td>324.18 (n/a)</td><td>243.00 (n/a)</td><td>218.90 (n/a)</td><td>185.54 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (-8.08%)</td><td>0.03 <b>(+22.46%)</b></td><td>0.03 <b>(+63.36%)</b></td><td>0.02 <b>(+302.51%)</b></td><td>0.01 <b>(-45.17%)</b></td><td>494.60 <b>(-75.16%)</b></td><td>343.60 <b>(-50.45%)</b></td><td>289.50 <b>(-38.78%)</b></td><td>248.00 (+8.82%)</td><td>104.62 <b>(-85.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1990.90 (n/a)</td><td>693.44 (n/a)</td><td>472.90 (n/a)</td><td>227.90 (n/a)</td><td>735.66 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.05 (+14.66%)</td><td>0.03 <b>(+61.22%)</b></td><td>0.04 <b>(+74.64%)</b></td><td>0.02 <b>(+408.21%)</b></td><td>0.01 <b>(-26.77%)</b></td><td>476.20 <b>(-80.32%)</b></td><td>324.76 <b>(-65.68%)</b></td><td>283.60 <b>(-42.74%)</b></td><td>192.20 (-12.76%)</td><td>112.63 <b>(-87.65%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2420.00 (n/a)</td><td>946.32 (n/a)</td><td>495.30 (n/a)</td><td>220.30 (n/a)</td><td>912.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (-4.01%)</td><td>0.03 (+5.30%)</td><td>0.03 (+8.64%)</td><td>0.02 (-13.76%)</td><td>0.01 (-2.72%)</td><td>534.40 (+15.97%)</td><td>318.74 (-3.99%)</td><td>272.70 (-7.96%)</td><td>241.90 (+4.18%)</td><td>123.03 (+19.02%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>460.80 (n/a)</td><td>331.98 (n/a)</td><td>296.30 (n/a)</td><td>232.20 (n/a)</td><td>103.37 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.05 (+2.83%)</td><td>0.04 (+10.43%)</td><td>0.04 (+12.87%)</td><td>0.02 (-0.61%)</td><td>0.01 (-9.21%)</td><td>527.10 (+0.63%)</td><td>301.26 (-11.73%)</td><td>249.10 (-11.42%)</td><td>188.60 (-2.78%)</td><td>131.57 (-8.89%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.80 (n/a)</td><td>341.30 (n/a)</td><td>281.20 (n/a)</td><td>194.00 (n/a)</td><td>144.41 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (-15.91%)</td><td>0.03 (+17.33%)</td><td>0.03 <b>(+27.95%)</b></td><td>0.02 <b>(+64.69%)</b></td><td>0.01 <b>(-51.86%)</b></td><td>412.50 <b>(-39.28%)</b></td><td>287.90 <b>(-26.75%)</b></td><td>263.00 <b>(-21.84%)</b></td><td>246.40 (+18.92%)</td><td>70.12 <b>(-64.06%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>679.40 (n/a)</td><td>393.04 (n/a)</td><td>336.50 (n/a)</td><td>207.20 (n/a)</td><td>195.08 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (+9.34%)</td><td>0.03 <b>(+49.13%)</b></td><td>0.03 <b>(+79.71%)</b></td><td>0.02 <b>(+35.10%)</b></td><td>0.01 <b>(-22.37%)</b></td><td>422.30 <b>(-25.99%)</b></td><td>304.48 <b>(-35.49%)</b></td><td>278.70 <b>(-44.35%)</b></td><td>248.20 (-8.55%)</td><td>68.00 <b>(-42.08%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>570.60 (n/a)</td><td>472.02 (n/a)</td><td>500.80 (n/a)</td><td>271.40 (n/a)</td><td>117.40 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (-9.03%)</td><td>0.03 <b>(+21.49%)</b></td><td>0.03 <b>(+70.49%)</b></td><td>0.02 <b>(+24.80%)</b></td><td>0.01 <b>(-44.19%)</b></td><td>400.50 (-19.87%)</td><td>274.88 <b>(-24.92%)</b></td><td>246.00 <b>(-41.34%)</b></td><td>232.20 (+9.89%)</td><td>70.58 <b>(-48.07%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>499.80 (n/a)</td><td>366.14 (n/a)</td><td>419.40 (n/a)</td><td>211.30 (n/a)</td><td>135.92 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.04 (+16.24%)</td><td>0.03 (+6.40%)</td><td>0.04 (+13.21%)</td><td>0.02 <b>(-23.71%)</b></td><td>0.01 <b>(+76.83%)</b></td><td>593.30 <b>(+31.09%)</b></td><td>323.92 (+2.28%)</td><td>253.30 (-11.68%)</td><td>234.10 (-13.97%)</td><td>152.66 <b>(+99.95%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>452.60 (n/a)</td><td>316.70 (n/a)</td><td>286.80 (n/a)</td><td>272.10 (n/a)</td><td>76.35 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.03 (+11.07%)</td><td>0.03 (+12.50%)</td><td>0.03 (+7.12%)</td><td>0.02 (+10.59%)</td><td>0.01 (-13.41%)</td><td>455.60 (-9.57%)</td><td>328.02 (-13.07%)</td><td>293.60 (-6.65%)</td><td>263.00 (-9.96%)</td><td>76.91 <b>(-27.84%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.80 (n/a)</td><td>377.34 (n/a)</td><td>314.50 (n/a)</td><td>292.10 (n/a)</td><td>106.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.36 (-14.77%)</td><td>0.32 <b>(+25.38%)</b></td><td>0.32 <b>(+69.56%)</b></td><td>0.30 <b>(+95.61%)</b></td><td>0.02 <b>(-81.67%)</b></td><td>324.70 <b>(-48.87%)</b></td><td>304.90 <b>(-31.21%)</b></td><td>306.40 <b>(-41.02%)</b></td><td>275.00 (+17.32%)</td><td>19.50 <b>(-88.80%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.42 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>635.10 (n/a)</td><td>443.22 (n/a)</td><td>519.50 (n/a)</td><td>234.40 (n/a)</td><td>174.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.38 <b>(-39.28%)</b></td><td>0.21 <b>(-22.99%)</b></td><td>0.17 (-6.46%)</td><td>0.13 <b>(-28.29%)</b></td><td>0.10 <b>(-49.09%)</b></td><td>765.70 <b>(+39.45%)</b></td><td>538.52 (+18.13%)</td><td>562.60 (+6.90%)</td><td>262.00 <b>(+64.68%)</b></td><td>193.28 (+16.23%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.62 (n/a)</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>549.10 (n/a)</td><td>455.86 (n/a)</td><td>526.30 (n/a)</td><td>159.10 (n/a)</td><td>166.29 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.40 (+9.37%)</td><td>0.29 (+10.71%)</td><td>0.23 <b>(-33.48%)</b></td><td>0.20 <b>(+393.23%)</b></td><td>0.10 <b>(-33.21%)</b></td><td>490.20 <b>(-79.73%)</b></td><td>375.64 <b>(-50.63%)</b></td><td>421.50 <b>(+50.32%)</b></td><td>247.00 (-8.55%)</td><td>115.85 <b>(-87.61%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.36 (n/a)</td><td>0.26 (n/a)</td><td>0.35 (n/a)</td><td>0.04 (n/a)</td><td>0.15 (n/a)</td><td>2417.90 (n/a)</td><td>760.90 (n/a)</td><td>280.40 (n/a)</td><td>270.10 (n/a)</td><td>934.66 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.24 (-17.50%)</td><td>0.17 (-12.70%)</td><td>0.15 <b>(-32.59%)</b></td><td>0.13 <b>(+320.27%)</b></td><td>0.05 <b>(-53.67%)</b></td><td>573.90 <b>(-76.20%)</b></td><td>458.76 <b>(-38.04%)</b></td><td>489.30 <b>(+48.32%)</b></td><td>305.10 <b>(+21.22%)</b></td><td>107.95 <b>(-88.46%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>0.10 (n/a)</td><td>2411.80 (n/a)</td><td>740.38 (n/a)</td><td>329.90 (n/a)</td><td>251.70 (n/a)</td><td>935.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.30 (+12.55%)</td><td>0.20 (+16.51%)</td><td>0.22 <b>(+50.44%)</b></td><td>0.04 <b>(-70.22%)</b></td><td>0.10 <b>(+78.95%)</b></td><td>1872.60 <b>(+235.77%)</b></td><td>640.72 <b>(+36.70%)</b></td><td>328.80 <b>(-33.54%)</b></td><td>242.40 (-11.14%)</td><td>694.06 <b>(+512.57%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>557.70 (n/a)</td><td>468.72 (n/a)</td><td>494.70 (n/a)</td><td>272.80 (n/a)</td><td>113.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.33 (-5.31%)</td><td>0.25 <b>(+30.83%)</b></td><td>0.24 <b>(+72.46%)</b></td><td>0.14 <b>(+99.10%)</b></td><td>0.07 <b>(-37.19%)</b></td><td>508.80 <b>(-49.78%)</b></td><td>321.52 <b>(-37.57%)</b></td><td>303.50 <b>(-42.01%)</b></td><td>225.40 (+5.62%)</td><td>109.88 <b>(-64.57%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.35 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.11 (n/a)</td><td>1013.10 (n/a)</td><td>515.04 (n/a)</td><td>523.40 (n/a)</td><td>213.40 (n/a)</td><td>310.14 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.46 (-2.90%)</td><td>0.34 (+7.14%)</td><td>0.31 (+15.59%)</td><td>0.22 (-1.11%)</td><td>0.10 (-3.32%)</td><td>595.70 (+1.12%)</td><td>414.10 (-7.24%)</td><td>423.70 (-13.50%)</td><td>284.90 (+3.00%)</td><td>128.95 (-3.84%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>589.10 (n/a)</td><td>446.42 (n/a)</td><td>489.80 (n/a)</td><td>276.60 (n/a)</td><td>134.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.45 (+10.16%)</td><td>0.32 <b>(+27.82%)</b></td><td>0.26 (+11.27%)</td><td>0.25 <b>(+42.36%)</b></td><td>0.10 (+7.61%)</td><td>533.60 <b>(-29.75%)</b></td><td>436.66 <b>(-22.82%)</b></td><td>510.30 (-10.14%)</td><td>289.00 (-9.23%)</td><td>120.18 <b>(-24.97%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.41 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>759.60 (n/a)</td><td>565.80 (n/a)</td><td>567.90 (n/a)</td><td>318.40 (n/a)</td><td>160.17 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.45 (-7.18%)</td><td>0.29 (+1.29%)</td><td>0.25 (+17.48%)</td><td>0.20 <b>(+23.87%)</b></td><td>0.10 <b>(-30.96%)</b></td><td>644.10 (-19.27%)</td><td>493.76 (-10.84%)</td><td>521.10 (-14.88%)</td><td>293.00 (+7.72%)</td><td>130.82 <b>(-43.29%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.48 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>797.80 (n/a)</td><td>553.82 (n/a)</td><td>612.20 (n/a)</td><td>272.00 (n/a)</td><td>230.67 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 <b>(+43.43%)</b></td><td>0.01 (+7.67%)</td><td>0.01 (-0.30%)</td><td>0.01 (-9.75%)</td><td>0.01 <b>(+83.42%)</b></td><td>508.60 (+10.81%)</td><td>341.72 (-0.32%)</td><td>310.20 (+0.32%)</td><td>186.00 <b>(-30.26%)</b></td><td>125.71 <b>(+44.44%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>459.00 (n/a)</td><td>342.82 (n/a)</td><td>309.20 (n/a)</td><td>266.70 (n/a)</td><td>87.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 <b>(+35.35%)</b></td><td>0.01 <b>(+21.15%)</b></td><td>0.01 (-6.60%)</td><td>0.01 <b>(+377.81%)</b></td><td>0.00 <b>(-28.40%)</b></td><td>400.10 <b>(-79.07%)</b></td><td>322.52 <b>(-48.77%)</b></td><td>332.20 (+7.06%)</td><td>218.70 <b>(-26.11%)</b></td><td>77.98 <b>(-89.12%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1911.90 (n/a)</td><td>629.56 (n/a)</td><td>310.30 (n/a)</td><td>296.00 (n/a)</td><td>716.92 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (+4.44%)</td><td>0.01 (-9.76%)</td><td>0.01 <b>(-29.85%)</b></td><td>0.01 (+5.25%)</td><td>0.00 (+7.51%)</td><td>541.60 (-4.98%)</td><td>399.24 (+11.74%)</td><td>399.70 <b>(+42.55%)</b></td><td>238.10 (-4.22%)</td><td>137.46 (+1.45%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>570.00 (n/a)</td><td>357.30 (n/a)</td><td>280.40 (n/a)</td><td>248.60 (n/a)</td><td>135.49 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.55 (-3.93%)</td><td>0.42 (-2.49%)</td><td>0.52 (+15.42%)</td><td>0.19 <b>(-28.90%)</b></td><td>0.16 <b>(+36.17%)</b></td><td>690.50 <b>(+40.66%)</b></td><td>367.52 (+12.92%)</td><td>252.70 (-13.37%)</td><td>241.30 (+4.10%)</td><td>192.45 <b>(+89.03%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.57 (n/a)</td><td>0.43 (n/a)</td><td>0.45 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>490.90 (n/a)</td><td>325.46 (n/a)</td><td>291.70 (n/a)</td><td>231.80 (n/a)</td><td>101.81 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.55 (+2.80%)</td><td>0.40 (-9.75%)</td><td>0.34 <b>(-27.33%)</b></td><td>0.26 (-14.41%)</td><td>0.13 <b>(+48.55%)</b></td><td>501.00 (+16.84%)</td><td>358.56 (+16.24%)</td><td>390.20 <b>(+37.59%)</b></td><td>241.70 (-2.74%)</td><td>113.39 <b>(+55.39%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.53 (n/a)</td><td>0.44 (n/a)</td><td>0.47 (n/a)</td><td>0.31 (n/a)</td><td>0.09 (n/a)</td><td>428.80 (n/a)</td><td>308.46 (n/a)</td><td>283.60 (n/a)</td><td>248.50 (n/a)</td><td>72.97 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.48 <b>(-30.13%)</b></td><td>0.40 (+13.85%)</td><td>0.42 <b>(+49.00%)</b></td><td>0.30 <b>(+299.96%)</b></td><td>0.08 <b>(-67.97%)</b></td><td>440.60 <b>(-75.00%)</b></td><td>342.30 <b>(-47.81%)</b></td><td>317.00 <b>(-32.90%)</b></td><td>276.40 <b>(+43.14%)</b></td><td>69.72 <b>(-89.06%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.68 (n/a)</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.07 (n/a)</td><td>0.24 (n/a)</td><td>1762.30 (n/a)</td><td>655.82 (n/a)</td><td>472.40 (n/a)</td><td>193.10 (n/a)</td><td>637.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.57 <b>(+27.88%)</b></td><td>0.44 <b>(+29.08%)</b></td><td>0.52 <b>(+77.83%)</b></td><td>0.27 (+0.44%)</td><td>0.15 <b>(+75.45%)</b></td><td>489.20 (-0.43%)</td><td>332.90 (-17.63%)</td><td>254.20 <b>(-43.77%)</b></td><td>232.60 <b>(-21.79%)</b></td><td>126.61 <b>(+37.80%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.44 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.08 (n/a)</td><td>491.30 (n/a)</td><td>404.16 (n/a)</td><td>452.10 (n/a)</td><td>297.40 (n/a)</td><td>91.88 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.67 (-6.88%)</td><td>0.47 (-7.24%)</td><td>0.47 (-8.68%)</td><td>0.27 (+6.47%)</td><td>0.14 (-15.04%)</td><td>490.30 (-6.07%)</td><td>307.32 (+4.27%)</td><td>283.10 (+9.47%)</td><td>198.60 (+7.35%)</td><td>108.84 (-16.93%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.71 (n/a)</td><td>0.50 (n/a)</td><td>0.51 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>522.00 (n/a)</td><td>294.74 (n/a)</td><td>258.60 (n/a)</td><td>185.00 (n/a)</td><td>131.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.02 (-6.73%)</td><td>0.01 (-6.56%)</td><td>0.01 (+5.62%)</td><td>0.01 (-9.30%)</td><td>0.00 <b>(+22.66%)</b></td><td>449.90 (+10.24%)</td><td>329.56 (+9.23%)</td><td>278.10 (-5.31%)</td><td>262.60 (+7.23%)</td><td>86.66 <b>(+37.13%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>408.10 (n/a)</td><td>301.72 (n/a)</td><td>293.70 (n/a)</td><td>244.90 (n/a)</td><td>63.20 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.01 (-18.26%)</td><td>0.01 (-8.90%)</td><td>0.01 (+9.00%)</td><td>0.01 (-10.48%)</td><td>0.00 <b>(-23.31%)</b></td><td>522.00 (+11.71%)</td><td>381.72 (+8.41%)</td><td>357.20 (-8.27%)</td><td>293.20 <b>(+22.32%)</b></td><td>99.41 (+4.26%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>467.30 (n/a)</td><td>352.12 (n/a)</td><td>389.40 (n/a)</td><td>239.70 (n/a)</td><td>95.35 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.00 <b>(+200.00%)</b></td><td>0.00 <b>(+70.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (n/a)</td><td>20457.51 (-9.80%)</td><td>14499.91 <b>(-22.00%)</b></td><td>18904.04 (+5.33%)</td><td>6449.61 <b>(-61.48%)</b></td><td>6802.52 <b>(+187.43%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22680.85 (n/a)</td><td>18589.20 (n/a)</td><td>17947.82 (n/a)</td><td>16744.67 (n/a)</td><td>2366.65 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.00 <b>(-36.36%)</b></td><td>0.00 <b>(-32.43%)</b></td><td>0.00 (-16.67%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-63.57%)</b></td><td>20407.99 (+5.33%)</td><td>17045.09 <b>(+31.40%)</b></td><td>18113.54 <b>(+40.43%)</b></td><td>12219.46 <b>(+64.60%)</b></td><td>3126.14 <b>(-43.60%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19375.92 (n/a)</td><td>12972.22 (n/a)</td><td>12898.60 (n/a)</td><td>7423.59 (n/a)</td><td>5542.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.15 (+12.61%)</td><td>0.11 <b>(+25.06%)</b></td><td>0.12 <b>(+47.45%)</b></td><td>0.07 (+3.98%)</td><td>0.03 <b>(+32.89%)</b></td><td>28704.72 (-3.82%)</td><td>20425.51 (-17.45%)</td><td>17665.47 <b>(-32.17%)</b></td><td>13816.18 (-11.18%)</td><td>6701.40 <b>(+23.89%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29845.02 (n/a)</td><td>24742.09 (n/a)</td><td>26042.96 (n/a)</td><td>15555.27 (n/a)</td><td>5408.98 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>0.15 (+8.61%)</td><td>0.10 (-6.26%)</td><td>0.09 <b>(-35.91%)</b></td><td>0.07 (+3.58%)</td><td>0.03 (-6.24%)</td><td>29016.35 (-3.37%)</td><td>22027.87 (+4.17%)</td><td>24523.77 <b>(+56.03%)</b></td><td>13863.78 (-7.89%)</td><td>6517.00 (-18.13%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>30028.66 (n/a)</td><td>21145.71 (n/a)</td><td>15717.66 (n/a)</td><td>15051.64 (n/a)</td><td>7960.37 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.51 (-16.97%)</td><td>1.35 (+7.76%)</td><td>1.41 (-3.00%)</td><td>0.92 <b>(+338.05%)</b></td><td>0.24 <b>(-64.77%)</b></td><td>567.70 <b>(-77.17%)</b></td><td>402.88 <b>(-49.35%)</b></td><td>370.50 (+3.09%)</td><td>346.30 <b>(+20.45%)</b></td><td>92.68 <b>(-90.26%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.82 (n/a)</td><td>1.25 (n/a)</td><td>1.46 (n/a)</td><td>0.21 (n/a)</td><td>0.68 (n/a)</td><td>2486.80 (n/a)</td><td>795.48 (n/a)</td><td>359.40 (n/a)</td><td>287.50 (n/a)</td><td>951.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>2.33 <b>(-23.00%)</b></td><td>1.64 <b>(-22.58%)</b></td><td>2.00 (-12.58%)</td><td>0.29 <b>(-78.75%)</b></td><td>0.82 (+18.04%)</td><td>3567.70 <b>(+370.55%)</b></td><td>1153.10 <b>(+112.10%)</b></td><td>523.90 (+14.39%)</td><td>449.90 <b>(+29.88%)</b></td><td>1354.07 <b>(+632.79%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>3.03 (n/a)</td><td>2.11 (n/a)</td><td>2.29 (n/a)</td><td>1.38 (n/a)</td><td>0.70 (n/a)</td><td>758.20 (n/a)</td><td>543.66 (n/a)</td><td>458.00 (n/a)</td><td>346.40 (n/a)</td><td>184.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 22:54:35</td><td>1.95 (+17.38%)</td><td>1.18 (-18.58%)</td><td>0.94 <b>(-38.87%)</b></td><td>0.67 <b>(-30.83%)</b></td><td>0.60 <b>(+114.09%)</b></td><td>786.40 <b>(+44.56%)</b></td><td>539.80 <b>(+44.02%)</b></td><td>556.70 <b>(+63.59%)</b></td><td>269.20 (-14.78%)</td><td>246.84 <b>(+159.47%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:01:04</td><td>1.66 (n/a)</td><td>1.46 (n/a)</td><td>1.54 (n/a)</td><td>0.96 (n/a)</td><td>0.28 (n/a)</td><td>544.00 (n/a)</td><td>374.80 (n/a)</td><td>340.30 (n/a)</td><td>315.90 (n/a)</td><td>95.13 (n/a)</td>
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
