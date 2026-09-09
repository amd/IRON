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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.06 <b>(+33.35%)</b></td><td>0.04 <b>(+22.83%)</b></td><td>0.05 <b>(+70.03%)</b></td><td>0.02 (-4.52%)</td><td>0.02 <b>(+56.86%)</b></td><td>586.00 (+4.74%)</td><td>369.36 (-9.04%)</td><td>248.20 <b>(-41.18%)</b></td><td>190.40 <b>(-25.01%)</b></td><td>195.34 <b>(+39.35%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>559.50 (n/a)</td><td>406.08 (n/a)</td><td>422.00 (n/a)</td><td>253.90 (n/a)</td><td>140.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.05 (-12.53%)</td><td>0.04 (+8.87%)</td><td>0.04 <b>(+82.01%)</b></td><td>0.01 (+2.51%)</td><td>0.02 <b>(-32.22%)</b></td><td>1023.70 (-2.45%)</td><td>427.92 (-17.18%)</td><td>297.60 <b>(-45.05%)</b></td><td>229.80 (+14.33%)</td><td>334.57 (-3.64%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1049.40 (n/a)</td><td>516.68 (n/a)</td><td>541.60 (n/a)</td><td>201.00 (n/a)</td><td>347.21 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.05 (+13.21%)</td><td>0.04 <b>(+34.21%)</b></td><td>0.05 <b>(+43.21%)</b></td><td>0.03 (+19.59%)</td><td>0.01 (+2.09%)</td><td>490.80 (-16.39%)</td><td>300.90 <b>(-27.37%)</b></td><td>268.60 <b>(-30.18%)</b></td><td>224.90 (-11.67%)</td><td>110.30 <b>(-26.06%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>587.00 (n/a)</td><td>414.30 (n/a)</td><td>384.70 (n/a)</td><td>254.60 (n/a)</td><td>149.17 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 <b>(-38.18%)</b></td><td>0.02 <b>(-25.96%)</b></td><td>0.02 (-18.97%)</td><td>0.01 (-16.03%)</td><td>0.00 <b>(-58.81%)</b></td><td>380.10 (+19.08%)</td><td>310.62 <b>(+29.77%)</b></td><td>299.70 <b>(+23.43%)</b></td><td>246.80 <b>(+61.73%)</b></td><td>50.82 (-18.34%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>319.20 (n/a)</td><td>239.36 (n/a)</td><td>242.80 (n/a)</td><td>152.60 (n/a)</td><td>62.22 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (-8.61%)</td><td>0.02 (+3.15%)</td><td>0.02 (-4.40%)</td><td>0.01 (+14.71%)</td><td>0.00 <b>(-31.41%)</b></td><td>427.70 (-12.82%)</td><td>302.12 (-9.47%)</td><td>282.20 (+4.60%)</td><td>226.80 (+9.41%)</td><td>81.74 <b>(-38.28%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>490.60 (n/a)</td><td>333.72 (n/a)</td><td>269.80 (n/a)</td><td>207.30 (n/a)</td><td>132.45 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (+1.87%)</td><td>0.01 <b>(-26.21%)</b></td><td>0.01 <b>(-47.34%)</b></td><td>0.01 <b>(-44.27%)</b></td><td>0.01 <b>(+175.54%)</b></td><td>593.80 <b>(+79.45%)</b></td><td>429.74 <b>(+56.38%)</b></td><td>495.70 <b>(+89.92%)</b></td><td>235.40 (-1.83%)</td><td>171.33 <b>(+374.61%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>330.90 (n/a)</td><td>274.80 (n/a)</td><td>261.00 (n/a)</td><td>239.80 (n/a)</td><td>36.10 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (-0.68%)</td><td>0.01 (+2.78%)</td><td>0.01 <b>(+39.00%)</b></td><td>0.00 (-5.57%)</td><td>0.01 (-16.04%)</td><td>2001.10 (+5.90%)</td><td>732.56 (-8.47%)</td><td>406.30 <b>(-28.06%)</b></td><td>245.10 (+0.66%)</td><td>722.63 (+5.59%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1889.60 (n/a)</td><td>800.34 (n/a)</td><td>564.80 (n/a)</td><td>243.50 (n/a)</td><td>684.35 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 <b>(-20.25%)</b></td><td>0.01 (-7.80%)</td><td>0.01 <b>(+35.43%)</b></td><td>0.01 (-10.43%)</td><td>0.00 <b>(-35.09%)</b></td><td>576.30 (+11.64%)</td><td>424.76 (+4.58%)</td><td>357.10 <b>(-26.16%)</b></td><td>319.70 <b>(+25.42%)</b></td><td>115.40 (-8.67%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>516.20 (n/a)</td><td>406.14 (n/a)</td><td>483.60 (n/a)</td><td>254.90 (n/a)</td><td>126.36 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (-15.94%)</td><td>0.01 <b>(-25.01%)</b></td><td>0.01 <b>(-30.53%)</b></td><td>0.01 (+6.43%)</td><td>0.00 <b>(-30.61%)</b></td><td>663.60 (-6.05%)</td><td>502.08 <b>(+24.85%)</b></td><td>475.90 <b>(+43.95%)</b></td><td>292.10 (+18.93%)</td><td>143.61 <b>(-23.97%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>706.30 (n/a)</td><td>402.16 (n/a)</td><td>330.60 (n/a)</td><td>245.60 (n/a)</td><td>188.89 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>592.90 (n/a)</td><td>381.80 (n/a)</td><td>296.40 (n/a)</td><td>235.20 (n/a)</td><td>159.40 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>593.80 (n/a)</td><td>425.00 (n/a)</td><td>414.20 (n/a)</td><td>243.90 (n/a)</td><td>153.47 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>576.20 (n/a)</td><td>471.62 (n/a)</td><td>569.50 (n/a)</td><td>299.90 (n/a)</td><td>139.24 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>443.40 (n/a)</td><td>288.22 (n/a)</td><td>268.30 (n/a)</td><td>215.80 (n/a)</td><td>91.76 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>699.70 (n/a)</td><td>494.34 (n/a)</td><td>437.90 (n/a)</td><td>236.90 (n/a)</td><td>194.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>589.50 (n/a)</td><td>381.44 (n/a)</td><td>338.20 (n/a)</td><td>247.20 (n/a)</td><td>129.53 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.00 (n/a)</td><td>322.28 (n/a)</td><td>322.20 (n/a)</td><td>165.90 (n/a)</td><td>128.24 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.40 (n/a)</td><td>363.36 (n/a)</td><td>308.00 (n/a)</td><td>234.50 (n/a)</td><td>117.20 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>483.30 (n/a)</td><td>335.14 (n/a)</td><td>297.30 (n/a)</td><td>232.80 (n/a)</td><td>113.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>771.30 (n/a)</td><td>458.20 (n/a)</td><td>361.60 (n/a)</td><td>240.00 (n/a)</td><td>223.54 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>864.00 (n/a)</td><td>518.66 (n/a)</td><td>533.70 (n/a)</td><td>248.00 (n/a)</td><td>230.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>673.70 (n/a)</td><td>491.48 (n/a)</td><td>463.00 (n/a)</td><td>371.10 (n/a)</td><td>111.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.62 (-5.70%)</td><td>0.49 (+5.17%)</td><td>0.55 <b>(+28.10%)</b></td><td>0.30 (-17.74%)</td><td>0.13 (+11.68%)</td><td>728.50 <b>(+21.56%)</b></td><td>484.52 (-2.33%)</td><td>403.80 <b>(-21.93%)</b></td><td>355.00 (+6.03%)</td><td>151.49 <b>(+53.70%)</b></td><td>26.58 (-5.70%)</td><td>20.81 (+5.17%)</td><td>23.37 <b>(+28.10%)</b></td><td>12.95 (-17.74%)</td><td>5.43 (+11.68%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.66 (n/a)</td><td>0.46 (n/a)</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.11 (n/a)</td><td>599.30 (n/a)</td><td>496.08 (n/a)</td><td>517.20 (n/a)</td><td>334.80 (n/a)</td><td>98.56 (n/a)</td><td>28.19 (n/a)</td><td>19.79 (n/a)</td><td>18.25 (n/a)</td><td>15.75 (n/a)</td><td>4.86 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.60 (+7.55%)</td><td>0.50 (+19.72%)</td><td>0.53 <b>(+24.58%)</b></td><td>0.34 (-0.55%)</td><td>0.11 (+17.75%)</td><td>659.20 (+0.56%)</td><td>459.64 (-15.68%)</td><td>420.90 (-19.72%)</td><td>369.60 (-7.00%)</td><td>118.05 (+8.62%)</td><td>25.54 (+7.55%)</td><td>21.45 (+19.72%)</td><td>22.42 <b>(+24.58%)</b></td><td>14.32 (-0.55%)</td><td>4.51 (+17.75%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.56 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>0.34 (n/a)</td><td>0.09 (n/a)</td><td>655.50 (n/a)</td><td>545.14 (n/a)</td><td>524.30 (n/a)</td><td>397.40 (n/a)</td><td>108.69 (n/a)</td><td>23.74 (n/a)</td><td>17.91 (n/a)</td><td>18.00 (n/a)</td><td>14.40 (n/a)</td><td>3.83 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.31 (+0.82%)</td><td>0.30 (-0.49%)</td><td>0.31 (+1.20%)</td><td>0.29 (-3.61%)</td><td>0.01 <b>(+129.21%)</b></td><td>87605.70 (+3.75%)</td><td>83459.02 (+0.57%)</td><td>81764.40 (-1.18%)</td><td>81020.00 (-0.81%)</td><td>2981.19 <b>(+135.11%)</b></td><td>212.04 (+0.82%)</td><td>206.05 (-0.49%)</td><td>210.11 (+1.20%)</td><td>196.10 (-3.61%)</td><td>7.24 <b>(+129.21%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84441.40 (n/a)</td><td>82982.52 (n/a)</td><td>82742.70 (n/a)</td><td>81682.30 (n/a)</td><td>1268.00 (n/a)</td><td>210.33 (n/a)</td><td>207.07 (n/a)</td><td>207.63 (n/a)</td><td>203.45 (n/a)</td><td>3.16 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>1.03 (+0.11%)</td><td>1.00 (-1.06%)</td><td>0.99 (-2.35%)</td><td>0.98 (-1.26%)</td><td>0.02 <b>(+84.12%)</b></td><td>25572.30 (+1.27%)</td><td>25116.78 (+1.09%)</td><td>25396.60 (+2.41%)</td><td>24518.40 (-0.11%)</td><td>473.69 <b>(+85.76%)</b></td><td>700.69 (+0.11%)</td><td>684.20 (-1.06%)</td><td>676.46 (-2.35%)</td><td>671.82 (-1.26%)</td><td>12.99 <b>(+84.12%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>1.03 (n/a)</td><td>1.01 (n/a)</td><td>1.01 (n/a)</td><td>1.00 (n/a)</td><td>0.01 (n/a)</td><td>25251.20 (n/a)</td><td>24846.02 (n/a)</td><td>24799.50 (n/a)</td><td>24544.40 (n/a)</td><td>255.00 (n/a)</td><td>699.95 (n/a)</td><td>691.51 (n/a)</td><td>692.75 (n/a)</td><td>680.36 (n/a)</td><td>7.06 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>3.43 (-6.36%)</td><td>2.33 (-17.43%)</td><td>2.18 <b>(-25.33%)</b></td><td>1.55 <b>(-20.79%)</b></td><td>0.76 (-10.18%)</td><td>5206.40 <b>(+26.25%)</b></td><td>3741.82 <b>(+21.59%)</b></td><td>3690.90 <b>(+33.91%)</b></td><td>2352.90 (+6.79%)</td><td>1147.93 (+19.33%)</td><td>898.45 (-6.36%)</td><td>612.34 (-17.43%)</td><td>572.74 <b>(-25.33%)</b></td><td>406.02 <b>(-20.79%)</b></td><td>198.06 (-10.18%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>3.66 (n/a)</td><td>2.83 (n/a)</td><td>2.92 (n/a)</td><td>1.95 (n/a)</td><td>0.84 (n/a)</td><td>4124.00 (n/a)</td><td>3077.52 (n/a)</td><td>2756.20 (n/a)</td><td>2203.30 (n/a)</td><td>962.01 (n/a)</td><td>959.42 (n/a)</td><td>741.61 (n/a)</td><td>766.98 (n/a)</td><td>512.59 (n/a)</td><td>220.50 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.21 (-11.58%)</td><td>0.20 (-4.74%)</td><td>0.20 (-5.64%)</td><td>0.17 (-6.19%)</td><td>0.02 <b>(-26.25%)</b></td><td>7460.70 (+6.60%)</td><td>6382.00 (+4.50%)</td><td>6280.00 (+5.98%)</td><td>5808.30 (+13.10%)</td><td>673.48 (-12.54%)</td><td>11.55 (-11.58%)</td><td>10.60 (-4.74%)</td><td>10.69 (-5.64%)</td><td>9.00 (-6.19%)</td><td>1.05 <b>(-26.25%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>6999.10 (n/a)</td><td>6106.98 (n/a)</td><td>5925.70 (n/a)</td><td>5135.70 (n/a)</td><td>770.08 (n/a)</td><td>13.07 (n/a)</td><td>11.13 (n/a)</td><td>11.33 (n/a)</td><td>9.59 (n/a)</td><td>1.42 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>3.83 (n/a)</td><td>3.49 (n/a)</td><td>3.62 (n/a)</td><td>2.87 (n/a)</td><td>0.37 (n/a)</td><td>3.83 (n/a)</td><td>3.49 (n/a)</td><td>3.62 (n/a)</td><td>2.87 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>7.45 (+0.61%)</td><td>7.05 (+9.37%)</td><td>7.09 (+5.87%)</td><td>6.47 (+14.27%)</td><td>0.36 <b>(-52.19%)</b></td><td>7.45 (+0.61%)</td><td>7.05 (+9.37%)</td><td>7.08 (+5.87%)</td><td>6.46 (+14.27%)</td><td>0.36 <b>(-52.19%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>7.41 (n/a)</td><td>6.45 (n/a)</td><td>6.69 (n/a)</td><td>5.66 (n/a)</td><td>0.76 (n/a)</td><td>7.40 (n/a)</td><td>6.44 (n/a)</td><td>6.69 (n/a)</td><td>5.66 (n/a)</td><td>0.76 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>12.93 <b>(+27.40%)</b></td><td>9.32 (+6.38%)</td><td>8.51 (+0.20%)</td><td>7.41 (-9.73%)</td><td>2.19 <b>(+179.25%)</b></td><td>12.92 <b>(+27.40%)</b></td><td>9.31 (+6.38%)</td><td>8.51 (+0.20%)</td><td>7.40 (-9.73%)</td><td>2.19 <b>(+179.25%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>10.15 (n/a)</td><td>8.76 (n/a)</td><td>8.50 (n/a)</td><td>8.20 (n/a)</td><td>0.78 (n/a)</td><td>10.14 (n/a)</td><td>8.75 (n/a)</td><td>8.49 (n/a)</td><td>8.20 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>3.57 (n/a)</td><td>3.50 (n/a)</td><td>3.49 (n/a)</td><td>3.43 (n/a)</td><td>0.05 (n/a)</td><td>3.57 (n/a)</td><td>3.50 (n/a)</td><td>3.49 (n/a)</td><td>3.43 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>7.62 (+1.69%)</td><td>6.84 (+3.31%)</td><td>6.89 (+5.62%)</td><td>6.10 (+5.71%)</td><td>0.56 (-14.82%)</td><td>7.61 (+1.69%)</td><td>6.84 (+3.31%)</td><td>6.89 (+5.62%)</td><td>6.09 (+5.71%)</td><td>0.56 (-14.82%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>7.49 (n/a)</td><td>6.62 (n/a)</td><td>6.52 (n/a)</td><td>5.77 (n/a)</td><td>0.66 (n/a)</td><td>7.49 (n/a)</td><td>6.62 (n/a)</td><td>6.52 (n/a)</td><td>5.77 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>13.84 (-1.55%)</td><td>11.61 (-7.43%)</td><td>13.19 (-3.93%)</td><td>8.03 (+6.93%)</td><td>2.61 (-7.42%)</td><td>13.83 (-1.55%)</td><td>11.60 (-7.43%)</td><td>13.18 (-3.93%)</td><td>8.02 (+6.93%)</td><td>2.61 (-7.42%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>14.05 (n/a)</td><td>12.54 (n/a)</td><td>13.73 (n/a)</td><td>7.51 (n/a)</td><td>2.82 (n/a)</td><td>14.05 (n/a)</td><td>12.54 (n/a)</td><td>13.72 (n/a)</td><td>7.50 (n/a)</td><td>2.82 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>3.09 (-1.99%)</td><td>2.30 (-8.77%)</td><td>2.92 (-3.97%)</td><td>1.09 (-0.15%)</td><td>0.94 (+6.14%)</td><td>3.08 (-1.99%)</td><td>2.29 (-8.77%)</td><td>2.91 (-3.97%)</td><td>1.08 (-0.15%)</td><td>0.94 (+6.14%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>3.15 (n/a)</td><td>2.52 (n/a)</td><td>3.04 (n/a)</td><td>1.09 (n/a)</td><td>0.89 (n/a)</td><td>3.14 (n/a)</td><td>2.51 (n/a)</td><td>3.03 (n/a)</td><td>1.09 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.51 (-9.64%)</td><td>0.22 <b>(-40.28%)</b></td><td>0.08 <b>(-78.11%)</b></td><td>0.07 (-2.83%)</td><td>0.21 (+4.39%)</td><td>0.51 (-9.64%)</td><td>0.22 <b>(-40.28%)</b></td><td>0.08 <b>(-78.11%)</b></td><td>0.07 (-2.83%)</td><td>0.20 (+4.39%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.57 (n/a)</td><td>0.37 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.56 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.71 (-2.14%)</td><td>0.44 (+6.24%)</td><td>0.47 (+1.72%)</td><td>0.08 (-0.84%)</td><td>0.26 (+7.74%)</td><td>0.70 (-2.14%)</td><td>0.43 (+6.24%)</td><td>0.47 (+1.72%)</td><td>0.08 (-0.84%)</td><td>0.25 (+7.74%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.73 (n/a)</td><td>0.41 (n/a)</td><td>0.46 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td><td>0.72 (n/a)</td><td>0.41 (n/a)</td><td>0.46 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>2.38 (-3.37%)</td><td>1.34 (-14.99%)</td><td>1.52 (-14.26%)</td><td>0.46 (+3.38%)</td><td>0.86 (+11.96%)</td><td>2.34 (-3.37%)</td><td>1.32 (-14.99%)</td><td>1.50 (-14.26%)</td><td>0.45 (+3.38%)</td><td>0.84 (+11.96%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>2.47 (n/a)</td><td>1.58 (n/a)</td><td>1.78 (n/a)</td><td>0.44 (n/a)</td><td>0.76 (n/a)</td><td>2.43 (n/a)</td><td>1.55 (n/a)</td><td>1.75 (n/a)</td><td>0.43 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.40 (n/a)</td><td>430.76 (n/a)</td><td>469.30 (n/a)</td><td>231.70 (n/a)</td><td>113.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.10 (n/a)</td><td>358.22 (n/a)</td><td>296.50 (n/a)</td><td>240.00 (n/a)</td><td>118.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.90 (n/a)</td><td>327.90 (n/a)</td><td>258.20 (n/a)</td><td>225.70 (n/a)</td><td>126.49 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>488.70 (n/a)</td><td>360.90 (n/a)</td><td>329.20 (n/a)</td><td>240.70 (n/a)</td><td>116.98 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>501.30 (n/a)</td><td>466.60 (n/a)</td><td>470.60 (n/a)</td><td>417.40 (n/a)</td><td>31.44 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>625.30 (n/a)</td><td>472.72 (n/a)</td><td>478.70 (n/a)</td><td>364.00 (n/a)</td><td>110.92 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (+14.11%)</td><td>0.02 (+10.51%)</td><td>0.02 (+9.63%)</td><td>0.02 (+11.26%)</td><td>0.01 (+9.57%)</td><td>532.80 (-10.11%)</td><td>405.50 (-10.27%)</td><td>473.70 (-8.78%)</td><td>221.80 (-12.37%)</td><td>138.61 (-14.66%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.70 (n/a)</td><td>451.90 (n/a)</td><td>519.30 (n/a)</td><td>253.10 (n/a)</td><td>162.42 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (-3.69%)</td><td>0.02 (+5.70%)</td><td>0.02 (+16.44%)</td><td>0.02 (+12.43%)</td><td>0.01 (-19.02%)</td><td>518.20 (-11.05%)</td><td>384.52 (-9.66%)</td><td>425.00 (-14.11%)</td><td>269.40 (+3.86%)</td><td>110.32 <b>(-26.60%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.60 (n/a)</td><td>425.66 (n/a)</td><td>494.80 (n/a)</td><td>259.40 (n/a)</td><td>150.31 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (-6.15%)</td><td>0.02 (-13.92%)</td><td>0.02 <b>(-37.04%)</b></td><td>0.02 (-1.61%)</td><td>0.01 (-6.16%)</td><td>494.10 (+1.62%)</td><td>401.46 (+15.63%)</td><td>482.80 <b>(+58.82%)</b></td><td>232.30 (+6.56%)</td><td>121.14 (+0.76%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>486.20 (n/a)</td><td>347.18 (n/a)</td><td>304.00 (n/a)</td><td>218.00 (n/a)</td><td>120.23 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (+16.34%)</td><td>0.03 <b>(+24.42%)</b></td><td>0.03 <b>(+43.22%)</b></td><td>0.02 (+5.59%)</td><td>0.01 <b>(+39.05%)</b></td><td>465.00 (-5.30%)</td><td>343.10 (-16.89%)</td><td>307.90 <b>(-30.20%)</b></td><td>227.10 (-14.04%)</td><td>110.52 <b>(+22.79%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.00 (n/a)</td><td>412.84 (n/a)</td><td>441.10 (n/a)</td><td>264.20 (n/a)</td><td>90.01 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 <b>(-21.00%)</b></td><td>0.02 (-4.57%)</td><td>0.02 (-3.70%)</td><td>0.01 (-13.53%)</td><td>0.01 <b>(-26.62%)</b></td><td>636.50 (+15.64%)</td><td>419.92 (+0.94%)</td><td>477.00 (+3.83%)</td><td>194.40 <b>(+26.64%)</b></td><td>175.54 (+13.15%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>550.40 (n/a)</td><td>416.02 (n/a)</td><td>459.40 (n/a)</td><td>153.50 (n/a)</td><td>155.14 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 <b>(+90.59%)</b></td><td>0.02 <b>(+28.40%)</b></td><td>0.02 (-5.50%)</td><td>0.01 (-12.66%)</td><td>0.01 <b>(+486.55%)</b></td><td>672.20 (+14.49%)</td><td>445.12 (-9.20%)</td><td>500.70 (+5.83%)</td><td>236.20 <b>(-47.52%)</b></td><td>185.26 <b>(+232.16%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.10 (n/a)</td><td>490.24 (n/a)</td><td>473.10 (n/a)</td><td>450.10 (n/a)</td><td>55.77 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (-5.31%)</td><td>0.02 <b>(+31.87%)</b></td><td>0.02 <b>(+39.99%)</b></td><td>0.01 <b>(+267.54%)</b></td><td>0.01 <b>(-34.36%)</b></td><td>549.30 <b>(-72.79%)</b></td><td>393.32 <b>(-48.26%)</b></td><td>362.20 <b>(-28.57%)</b></td><td>264.10 (+5.60%)</td><td>121.04 <b>(-83.03%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2018.90 (n/a)</td><td>760.24 (n/a)</td><td>507.10 (n/a)</td><td>250.10 (n/a)</td><td>713.23 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 <b>(+24.49%)</b></td><td>0.02 (+1.24%)</td><td>0.01 (-11.00%)</td><td>0.01 <b>(-20.58%)</b></td><td>0.01 <b>(+64.44%)</b></td><td>787.30 <b>(+25.93%)</b></td><td>556.98 (+8.55%)</td><td>602.80 (+12.36%)</td><td>248.40 (-19.69%)</td><td>206.79 <b>(+57.76%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>625.20 (n/a)</td><td>513.10 (n/a)</td><td>536.50 (n/a)</td><td>309.30 (n/a)</td><td>131.08 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (-4.40%)</td><td>0.03 (+3.74%)</td><td>0.03 <b>(+29.04%)</b></td><td>0.01 (-9.55%)</td><td>0.01 <b>(+34.61%)</b></td><td>602.00 (+10.56%)</td><td>353.10 (+3.68%)</td><td>241.00 <b>(-22.51%)</b></td><td>232.40 (+4.59%)</td><td>168.50 <b>(+39.13%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.50 (n/a)</td><td>340.56 (n/a)</td><td>311.00 (n/a)</td><td>222.20 (n/a)</td><td>121.11 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (+0.09%)</td><td>0.03 (+1.08%)</td><td>0.03 (+15.94%)</td><td>0.01 (-19.85%)</td><td>0.01 (+9.47%)</td><td>672.40 <b>(+24.77%)</b></td><td>383.04 (+4.02%)</td><td>290.60 (-13.74%)</td><td>233.30 (-0.09%)</td><td>190.79 <b>(+33.87%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.90 (n/a)</td><td>368.22 (n/a)</td><td>336.90 (n/a)</td><td>233.50 (n/a)</td><td>142.52 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (-8.95%)</td><td>0.03 (+19.83%)</td><td>0.03 <b>(+98.33%)</b></td><td>0.01 (+3.96%)</td><td>0.01 <b>(-24.94%)</b></td><td>564.50 (-3.82%)</td><td>323.02 <b>(-21.81%)</b></td><td>252.70 <b>(-49.57%)</b></td><td>235.90 (+9.82%)</td><td>139.62 (-18.62%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.90 (n/a)</td><td>413.14 (n/a)</td><td>501.10 (n/a)</td><td>214.80 (n/a)</td><td>171.55 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.05 <b>(+37.09%)</b></td><td>0.03 (+1.27%)</td><td>0.03 (-5.80%)</td><td>0.02 (-12.03%)</td><td>0.01 <b>(+59.36%)</b></td><td>498.60 (+13.65%)</td><td>287.02 (+5.11%)</td><td>248.40 (+6.15%)</td><td>163.40 <b>(-27.09%)</b></td><td>126.06 <b>(+35.65%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>438.70 (n/a)</td><td>273.06 (n/a)</td><td>234.00 (n/a)</td><td>224.10 (n/a)</td><td>92.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (-0.04%)</td><td>0.03 (+9.99%)</td><td>0.03 <b>(+20.81%)</b></td><td>0.02 <b>(+24.06%)</b></td><td>0.01 (+7.20%)</td><td>491.00 (-19.39%)</td><td>340.96 (-9.65%)</td><td>258.20 (-17.24%)</td><td>242.00 (+0.04%)</td><td>124.03 (-15.34%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.10 (n/a)</td><td>377.36 (n/a)</td><td>312.00 (n/a)</td><td>241.90 (n/a)</td><td>146.51 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (+0.10%)</td><td>0.02 (-9.13%)</td><td>0.01 (-16.27%)</td><td>0.00 (-13.11%)</td><td>0.01 (+2.36%)</td><td>2102.40 (+15.09%)</td><td>807.24 (+14.76%)</td><td>614.00 (+19.43%)</td><td>258.90 (-0.12%)</td><td>740.24 (+15.90%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1826.80 (n/a)</td><td>703.40 (n/a)</td><td>514.10 (n/a)</td><td>259.20 (n/a)</td><td>638.71 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.09 (-18.79%)</td><td>0.07 (-11.82%)</td><td>0.08 (-4.43%)</td><td>0.04 (-7.75%)</td><td>0.02 (-17.17%)</td><td>576.20 (+8.41%)</td><td>367.16 (+12.34%)</td><td>308.10 (+4.62%)</td><td>278.50 <b>(+23.12%)</b></td><td>123.13 (+4.37%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>531.50 (n/a)</td><td>326.84 (n/a)</td><td>294.50 (n/a)</td><td>226.20 (n/a)</td><td>117.97 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.15 (-16.97%)</td><td>0.12 (-16.37%)</td><td>0.12 (-13.50%)</td><td>0.08 (-15.66%)</td><td>0.03 (-11.93%)</td><td>521.50 (+18.58%)</td><td>366.06 <b>(+20.00%)</b></td><td>336.70 (+15.59%)</td><td>281.00 <b>(+20.45%)</b></td><td>98.40 <b>(+21.88%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>439.80 (n/a)</td><td>305.04 (n/a)</td><td>291.30 (n/a)</td><td>233.30 (n/a)</td><td>80.73 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (-11.34%)</td><td>0.02 <b>(+28.62%)</b></td><td>0.02 <b>(+50.89%)</b></td><td>0.01 <b>(+29.30%)</b></td><td>0.00 <b>(-40.04%)</b></td><td>448.40 <b>(-22.66%)</b></td><td>316.92 <b>(-27.83%)</b></td><td>301.80 <b>(-33.73%)</b></td><td>259.50 (+12.78%)</td><td>76.60 <b>(-46.67%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.80 (n/a)</td><td>439.12 (n/a)</td><td>455.40 (n/a)</td><td>230.10 (n/a)</td><td>143.64 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (-0.76%)</td><td>0.02 (-9.51%)</td><td>0.02 <b>(-34.41%)</b></td><td>0.02 (-5.00%)</td><td>0.01 (+17.07%)</td><td>504.30 (+5.26%)</td><td>373.18 (+14.50%)</td><td>413.20 <b>(+52.47%)</b></td><td>224.90 (+0.76%)</td><td>137.33 <b>(+20.22%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>479.10 (n/a)</td><td>325.92 (n/a)</td><td>271.00 (n/a)</td><td>223.20 (n/a)</td><td>114.23 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.06 <b>(+38.14%)</b></td><td>0.03 (-8.78%)</td><td>0.03 <b>(-34.54%)</b></td><td>0.02 (-19.52%)</td><td>0.02 <b>(+72.99%)</b></td><td>685.90 <b>(+24.28%)</b></td><td>448.06 <b>(+20.67%)</b></td><td>454.60 <b>(+52.76%)</b></td><td>199.50 <b>(-27.61%)</b></td><td>179.17 <b>(+48.74%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>551.90 (n/a)</td><td>371.30 (n/a)</td><td>297.60 (n/a)</td><td>275.60 (n/a)</td><td>120.46 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (+18.63%)</td><td>0.02 <b>(+26.56%)</b></td><td>0.02 (+8.39%)</td><td>0.02 <b>(+20.93%)</b></td><td>0.01 <b>(+39.43%)</b></td><td>480.60 (-17.31%)</td><td>354.22 (-19.36%)</td><td>395.20 (-7.75%)</td><td>236.80 (-15.70%)</td><td>105.11 (-3.37%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.20 (n/a)</td><td>439.26 (n/a)</td><td>428.40 (n/a)</td><td>280.90 (n/a)</td><td>108.78 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (-19.89%)</td><td>0.03 (+19.45%)</td><td>0.04 <b>(+73.13%)</b></td><td>0.02 <b>(+62.07%)</b></td><td>0.01 <b>(-48.31%)</b></td><td>464.10 <b>(-38.30%)</b></td><td>317.54 <b>(-31.66%)</b></td><td>284.30 <b>(-42.24%)</b></td><td>234.40 <b>(+24.81%)</b></td><td>94.77 <b>(-60.05%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>752.20 (n/a)</td><td>464.64 (n/a)</td><td>492.20 (n/a)</td><td>187.80 (n/a)</td><td>237.23 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 <b>(+47.36%)</b></td><td>0.02 <b>(+37.93%)</b></td><td>0.02 (+19.97%)</td><td>0.01 (-10.03%)</td><td>0.01 <b>(+168.06%)</b></td><td>627.60 (+11.16%)</td><td>395.42 (-17.05%)</td><td>410.60 (-16.65%)</td><td>222.40 <b>(-32.13%)</b></td><td>175.08 <b>(+88.54%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>564.60 (n/a)</td><td>476.72 (n/a)</td><td>492.60 (n/a)</td><td>327.70 (n/a)</td><td>92.86 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 <b>(-34.87%)</b></td><td>0.02 <b>(-33.74%)</b></td><td>0.02 <b>(-48.54%)</b></td><td>0.02 (-7.31%)</td><td>0.01 <b>(-57.10%)</b></td><td>657.60 (+7.89%)</td><td>524.32 <b>(+34.16%)</b></td><td>543.50 <b>(+94.32%)</b></td><td>342.20 <b>(+53.52%)</b></td><td>114.83 <b>(-36.80%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>609.50 (n/a)</td><td>390.82 (n/a)</td><td>279.70 (n/a)</td><td>222.90 (n/a)</td><td>181.70 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 <b>(-22.88%)</b></td><td>0.02 (-19.90%)</td><td>0.02 <b>(-35.67%)</b></td><td>0.02 (+3.96%)</td><td>0.01 <b>(-31.51%)</b></td><td>481.20 (-3.82%)</td><td>371.10 (+16.57%)</td><td>432.20 <b>(+55.47%)</b></td><td>211.70 <b>(+29.72%)</b></td><td>124.80 (-15.22%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.30 (n/a)</td><td>318.36 (n/a)</td><td>278.00 (n/a)</td><td>163.20 (n/a)</td><td>147.20 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (+1.94%)</td><td>0.03 <b>(+29.75%)</b></td><td>0.02 (+8.31%)</td><td>0.02 <b>(+132.25%)</b></td><td>0.01 (-12.58%)</td><td>446.30 <b>(-56.95%)</b></td><td>361.86 <b>(-32.26%)</b></td><td>430.80 (-7.67%)</td><td>238.60 (-1.89%)</td><td>106.48 <b>(-64.12%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1036.60 (n/a)</td><td>534.22 (n/a)</td><td>466.60 (n/a)</td><td>243.20 (n/a)</td><td>296.73 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 <b>(-27.35%)</b></td><td>0.02 <b>(-26.68%)</b></td><td>0.02 <b>(-41.28%)</b></td><td>0.02 <b>(+21.98%)</b></td><td>0.01 <b>(-40.78%)</b></td><td>461.80 (-18.02%)</td><td>400.44 <b>(+23.75%)</b></td><td>442.50 <b>(+70.32%)</b></td><td>228.10 <b>(+37.66%)</b></td><td>97.49 <b>(-36.71%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.30 (n/a)</td><td>323.58 (n/a)</td><td>259.80 (n/a)</td><td>165.70 (n/a)</td><td>154.03 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.05 (+14.68%)</td><td>0.03 <b>(+54.31%)</b></td><td>0.04 <b>(+104.79%)</b></td><td>0.02 <b>(+175.00%)</b></td><td>0.01 (+4.27%)</td><td>600.00 <b>(-63.63%)</b></td><td>365.88 <b>(-47.36%)</b></td><td>260.10 <b>(-51.16%)</b></td><td>195.10 (-12.78%)</td><td>182.91 <b>(-66.83%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1649.90 (n/a)</td><td>695.12 (n/a)</td><td>532.60 (n/a)</td><td>223.70 (n/a)</td><td>551.46 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (+6.10%)</td><td>0.02 (+14.03%)</td><td>0.02 <b>(+28.59%)</b></td><td>0.02 (+16.62%)</td><td>0.00 (+8.50%)</td><td>543.00 (-14.26%)</td><td>416.08 (-12.22%)</td><td>370.10 <b>(-22.23%)</b></td><td>304.60 (-5.75%)</td><td>101.58 (-7.70%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>633.30 (n/a)</td><td>474.00 (n/a)</td><td>475.90 (n/a)</td><td>323.20 (n/a)</td><td>110.04 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.33 (-5.98%)</td><td>0.26 (-11.13%)</td><td>0.24 <b>(-28.13%)</b></td><td>0.19 (+3.14%)</td><td>0.06 <b>(-26.20%)</b></td><td>508.90 (-3.05%)</td><td>395.44 (+9.48%)</td><td>405.60 <b>(+39.14%)</b></td><td>299.70 (+6.35%)</td><td>85.36 <b>(-22.31%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.34 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>524.90 (n/a)</td><td>361.20 (n/a)</td><td>291.50 (n/a)</td><td>281.80 (n/a)</td><td>109.88 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.42 <b>(+40.02%)</b></td><td>0.29 <b>(+32.06%)</b></td><td>0.31 <b>(+52.43%)</b></td><td>0.17 (-9.26%)</td><td>0.11 <b>(+123.39%)</b></td><td>591.80 (+10.20%)</td><td>385.56 (-17.14%)</td><td>317.50 <b>(-34.39%)</b></td><td>236.00 <b>(-28.59%)</b></td><td>154.39 <b>(+80.14%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>537.00 (n/a)</td><td>465.30 (n/a)</td><td>483.90 (n/a)</td><td>330.50 (n/a)</td><td>85.71 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.49 <b>(+36.22%)</b></td><td>0.25 <b>(+21.06%)</b></td><td>0.21 (+7.11%)</td><td>0.17 <b>(+307.78%)</b></td><td>0.13 (+14.06%)</td><td>594.10 <b>(-75.48%)</b></td><td>445.74 <b>(-45.33%)</b></td><td>466.40 (-6.63%)</td><td>201.50 <b>(-26.59%)</b></td><td>148.18 <b>(-83.60%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.36 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>0.12 (n/a)</td><td>2422.70 (n/a)</td><td>815.30 (n/a)</td><td>499.50 (n/a)</td><td>274.50 (n/a)</td><td>903.57 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.26 (-10.44%)</td><td>0.19 (-13.26%)</td><td>0.18 <b>(-27.16%)</b></td><td>0.12 (-15.23%)</td><td>0.06 (+0.46%)</td><td>594.60 (+17.95%)</td><td>414.24 (+17.16%)</td><td>418.40 <b>(+37.27%)</b></td><td>279.60 (+11.66%)</td><td>134.50 <b>(+24.17%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>504.10 (n/a)</td><td>353.58 (n/a)</td><td>304.80 (n/a)</td><td>250.40 (n/a)</td><td>108.32 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.28 (-19.94%)</td><td>0.23 (+7.25%)</td><td>0.25 <b>(+64.39%)</b></td><td>0.15 (+17.64%)</td><td>0.05 <b>(-52.85%)</b></td><td>508.40 (-15.00%)</td><td>334.36 (-19.06%)</td><td>296.90 <b>(-39.17%)</b></td><td>263.90 <b>(+24.89%)</b></td><td>99.38 <b>(-45.31%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.35 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>598.10 (n/a)</td><td>413.10 (n/a)</td><td>488.10 (n/a)</td><td>211.30 (n/a)</td><td>181.71 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.23 (-17.71%)</td><td>0.16 (+11.87%)</td><td>0.16 <b>(+24.11%)</b></td><td>0.03 <b>(-57.12%)</b></td><td>0.08 (+0.39%)</td><td>2436.10 <b>(+133.23%)</b></td><td>811.64 <b>(+26.57%)</b></td><td>464.20 (-19.42%)</td><td>315.10 <b>(+21.52%)</b></td><td>912.80 <b>(+213.76%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.28 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>1044.50 (n/a)</td><td>641.28 (n/a)</td><td>576.10 (n/a)</td><td>259.30 (n/a)</td><td>290.93 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.41 (-16.63%)</td><td>0.30 (-12.31%)</td><td>0.25 (-11.67%)</td><td>0.21 (-2.30%)</td><td>0.10 <b>(-26.17%)</b></td><td>634.20 (+2.36%)</td><td>476.24 (+9.83%)</td><td>514.30 (+13.21%)</td><td>320.90 (+19.92%)</td><td>146.98 (-8.58%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>619.60 (n/a)</td><td>433.62 (n/a)</td><td>454.30 (n/a)</td><td>267.60 (n/a)</td><td>160.77 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.58 <b>(+21.37%)</b></td><td>0.38 (+10.41%)</td><td>0.36 (+5.20%)</td><td>0.23 (+9.06%)</td><td>0.15 <b>(+45.55%)</b></td><td>567.00 (-8.31%)</td><td>397.46 (-4.64%)</td><td>360.40 (-4.93%)</td><td>227.80 (-17.61%)</td><td>157.18 (+15.58%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.35 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>618.40 (n/a)</td><td>416.80 (n/a)</td><td>379.10 (n/a)</td><td>276.50 (n/a)</td><td>135.99 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.52 (-6.41%)</td><td>0.23 <b>(-41.89%)</b></td><td>0.16 <b>(-56.75%)</b></td><td>0.05 <b>(-79.69%)</b></td><td>0.18 <b>(+68.40%)</b></td><td>2487.10 <b>(+392.40%)</b></td><td>1014.44 <b>(+183.90%)</b></td><td>806.00 <b>(+131.28%)</b></td><td>253.60 (+6.82%)</td><td>877.66 <b>(+793.39%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.55 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>505.10 (n/a)</td><td>357.32 (n/a)</td><td>348.50 (n/a)</td><td>237.40 (n/a)</td><td>98.24 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (-6.44%)</td><td>0.01 (+3.91%)</td><td>0.01 (+16.39%)</td><td>0.01 (-17.11%)</td><td>0.00 (-4.71%)</td><td>591.00 <b>(+20.64%)</b></td><td>368.32 (-2.49%)</td><td>323.80 (-14.09%)</td><td>272.90 (+6.89%)</td><td>127.10 <b>(+29.68%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>489.90 (n/a)</td><td>377.72 (n/a)</td><td>376.90 (n/a)</td><td>255.30 (n/a)</td><td>98.01 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (+8.59%)</td><td>0.01 <b>(+22.27%)</b></td><td>0.01 (+15.81%)</td><td>0.01 (+7.70%)</td><td>0.00 <b>(+28.42%)</b></td><td>520.50 (-7.15%)</td><td>391.24 (-16.29%)</td><td>418.70 (-13.65%)</td><td>262.60 (-7.92%)</td><td>119.73 (+9.21%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>560.60 (n/a)</td><td>467.36 (n/a)</td><td>484.90 (n/a)</td><td>285.20 (n/a)</td><td>109.64 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (+0.70%)</td><td>0.01 <b>(+23.20%)</b></td><td>0.01 <b>(+25.42%)</b></td><td>0.01 <b>(+40.18%)</b></td><td>0.00 <b>(-41.23%)</b></td><td>395.00 <b>(-28.66%)</b></td><td>304.60 <b>(-24.01%)</b></td><td>291.60 <b>(-20.26%)</b></td><td>249.40 (-0.68%)</td><td>54.12 <b>(-58.63%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.70 (n/a)</td><td>400.84 (n/a)</td><td>365.70 (n/a)</td><td>251.10 (n/a)</td><td>130.81 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.56 (-8.60%)</td><td>0.41 (-16.36%)</td><td>0.46 (-8.12%)</td><td>0.23 <b>(-27.67%)</b></td><td>0.16 <b>(+39.37%)</b></td><td>577.60 <b>(+38.25%)</b></td><td>365.54 <b>(+30.19%)</b></td><td>289.80 (+8.87%)</td><td>234.40 (+9.43%)</td><td>157.08 <b>(+96.90%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.62 (n/a)</td><td>0.50 (n/a)</td><td>0.50 (n/a)</td><td>0.32 (n/a)</td><td>0.11 (n/a)</td><td>417.80 (n/a)</td><td>280.78 (n/a)</td><td>266.20 (n/a)</td><td>214.20 (n/a)</td><td>79.78 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.51 (-0.81%)</td><td>0.39 (+3.31%)</td><td>0.46 <b>(+55.85%)</b></td><td>0.23 (-12.21%)</td><td>0.13 (+6.13%)</td><td>576.10 (+13.90%)</td><td>382.94 (-0.37%)</td><td>287.70 <b>(-35.84%)</b></td><td>257.10 (+0.82%)</td><td>149.71 <b>(+28.56%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.52 (n/a)</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>505.80 (n/a)</td><td>384.38 (n/a)</td><td>448.40 (n/a)</td><td>255.00 (n/a)</td><td>116.45 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.45 <b>(-21.59%)</b></td><td>0.33 <b>(-29.09%)</b></td><td>0.29 <b>(-40.45%)</b></td><td>0.21 <b>(-25.00%)</b></td><td>0.11 (+2.72%)</td><td>638.40 <b>(+33.36%)</b></td><td>447.26 <b>(+45.91%)</b></td><td>460.80 <b>(+67.93%)</b></td><td>296.00 <b>(+27.53%)</b></td><td>150.64 <b>(+53.44%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.57 (n/a)</td><td>0.46 (n/a)</td><td>0.48 (n/a)</td><td>0.28 (n/a)</td><td>0.11 (n/a)</td><td>478.70 (n/a)</td><td>306.54 (n/a)</td><td>274.40 (n/a)</td><td>232.10 (n/a)</td><td>98.18 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.51 (+12.17%)</td><td>0.37 (-6.06%)</td><td>0.34 <b>(-21.21%)</b></td><td>0.31 (-0.35%)</td><td>0.08 <b>(+33.44%)</b></td><td>429.60 (+0.35%)</td><td>366.78 (+7.86%)</td><td>391.40 <b>(+26.91%)</b></td><td>259.20 (-10.87%)</td><td>71.24 <b>(+20.59%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.45 (n/a)</td><td>0.40 (n/a)</td><td>0.43 (n/a)</td><td>0.31 (n/a)</td><td>0.06 (n/a)</td><td>428.10 (n/a)</td><td>340.06 (n/a)</td><td>308.40 (n/a)</td><td>290.80 (n/a)</td><td>59.07 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.86 <b>(+54.17%)</b></td><td>0.45 (-0.63%)</td><td>0.40 (-18.61%)</td><td>0.23 (-10.87%)</td><td>0.24 <b>(+105.78%)</b></td><td>580.10 (+12.21%)</td><td>349.64 (+11.82%)</td><td>331.30 <b>(+22.89%)</b></td><td>153.50 <b>(-35.12%)</b></td><td>153.65 <b>(+33.29%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.49 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>517.00 (n/a)</td><td>312.68 (n/a)</td><td>269.60 (n/a)</td><td>236.60 (n/a)</td><td>115.27 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (+8.06%)</td><td>0.01 <b>(+29.64%)</b></td><td>0.01 <b>(+35.04%)</b></td><td>0.01 <b>(+21.19%)</b></td><td>0.00 (-9.63%)</td><td>473.20 (-17.49%)</td><td>325.24 <b>(-24.58%)</b></td><td>292.30 <b>(-25.94%)</b></td><td>260.60 (-7.46%)</td><td>84.65 <b>(-29.21%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.50 (n/a)</td><td>431.22 (n/a)</td><td>394.70 (n/a)</td><td>281.60 (n/a)</td><td>119.59 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 <b>(+26.79%)</b></td><td>0.01 <b>(+24.86%)</b></td><td>0.01 <b>(+23.72%)</b></td><td>0.01 (-3.60%)</td><td>0.00 <b>(+77.58%)</b></td><td>480.30 (+3.74%)</td><td>346.68 (-16.80%)</td><td>350.80 (-19.17%)</td><td>237.70 <b>(-21.13%)</b></td><td>97.02 <b>(+45.81%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>463.00 (n/a)</td><td>416.70 (n/a)</td><td>434.00 (n/a)</td><td>301.40 (n/a)</td><td>66.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3]

_No metrics available._


### test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4]

_No metrics available._


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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.00 (+0.00%)</td><td>0.00 (+13.04%)</td><td>0.00 (+20.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-23.36%)</b></td><td>16696.79 <b>(-22.03%)</b></td><td>9031.84 <b>(-23.39%)</b></td><td>7219.43 (-7.21%)</td><td>6195.75 (+8.42%)</td><td>4332.25 <b>(-42.24%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21415.50 (n/a)</td><td>11789.16 (n/a)</td><td>7780.39 (n/a)</td><td>5714.62 (n/a)</td><td>7500.24 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.00 (+7.69%)</td><td>0.00 <b>(+22.50%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(-20.00%)</b></td><td>0.00 <b>(+20.12%)</b></td><td>18894.39 (+6.25%)</td><td>10186.35 (-19.08%)</td><td>6687.49 <b>(-55.07%)</b></td><td>5943.19 (-2.20%)</td><td>5674.87 (+4.73%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>17782.76 (n/a)</td><td>12587.83 (n/a)</td><td>14885.21 (n/a)</td><td>6077.00 (n/a)</td><td>5418.64 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.16 (+12.54%)</td><td>0.10 (+11.82%)</td><td>0.08 (-4.31%)</td><td>0.07 (-2.52%)</td><td>0.04 <b>(+41.35%)</b></td><td>30158.41 (+2.59%)</td><td>23438.22 (-5.05%)</td><td>27792.19 (+4.57%)</td><td>12986.63 (-11.16%)</td><td>8227.36 <b>(+42.55%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29397.45 (n/a)</td><td>24686.08 (n/a)</td><td>26578.49 (n/a)</td><td>14617.47 (n/a)</td><td>5771.46 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>1.43 <b>(-22.66%)</b></td><td>1.05 <b>(-22.74%)</b></td><td>1.02 <b>(-38.74%)</b></td><td>0.58 (-17.54%)</td><td>0.33 <b>(-36.45%)</b></td><td>898.10 <b>(+21.28%)</b></td><td>550.74 <b>(+22.97%)</b></td><td>515.60 <b>(+63.27%)</b></td><td>367.10 <b>(+29.31%)</b></td><td>209.97 (+2.57%)</td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>1.85 (n/a)</td><td>1.36 (n/a)</td><td>1.66 (n/a)</td><td>0.71 (n/a)</td><td>0.52 (n/a)</td><td>740.50 (n/a)</td><td>447.88 (n/a)</td><td>315.80 (n/a)</td><td>283.90 (n/a)</td><td>204.70 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>2.63 (-14.21%)</td><td>1.12 <b>(-42.86%)</b></td><td>1.07 <b>(-22.90%)</b></td><td>0.30 <b>(-78.04%)</b></td><td>0.95 (+17.24%)</td><td>3497.40 <b>(+355.39%)</b></td><td>1790.02 <b>(+195.54%)</b></td><td>976.30 <b>(+29.71%)</b></td><td>398.80 (+16.54%)</td><td>1464.23 <b>(+587.42%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>3.06 (n/a)</td><td>1.96 (n/a)</td><td>1.39 (n/a)</td><td>1.37 (n/a)</td><td>0.81 (n/a)</td><td>768.00 (n/a)</td><td>605.68 (n/a)</td><td>752.70 (n/a)</td><td>342.20 (n/a)</td><td>213.00 (n/a)</td>
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
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>1.86 (-4.89%)</td><td>1.08 (-18.19%)</td><td>0.90 <b>(-33.59%)</b></td><td>0.22 <b>(-73.21%)</b></td><td>0.65 <b>(+52.73%)</b></td><td>2420.40 <b>(+273.23%)</b></td><td>845.06 <b>(+96.14%)</b></td><td>582.40 <b>(+50.57%)</b></td><td>281.60 (+5.15%)</td><td>892.49 <b>(+529.30%)</b></td>
</tr>
<tr>
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>1.96 (n/a)</td><td>1.32 (n/a)</td><td>1.36 (n/a)</td><td>0.81 (n/a)</td><td>0.42 (n/a)</td><td>648.50 (n/a)</td><td>430.84 (n/a)</td><td>386.80 (n/a)</td><td>267.80 (n/a)</td><td>141.82 (n/a)</td>
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
