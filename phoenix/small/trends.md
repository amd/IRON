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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (-9.46%)</td><td>0.03 <b>(-24.66%)</b></td><td>0.03 <b>(-38.33%)</b></td><td>0.02 (-11.07%)</td><td>0.01 (+7.85%)</td><td>559.50 (+12.44%)</td><td>406.08 <b>(+36.19%)</b></td><td>422.00 <b>(+62.18%)</b></td><td>253.90 (+10.44%)</td><td>140.18 <b>(+24.91%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.60 (n/a)</td><td>298.18 (n/a)</td><td>260.20 (n/a)</td><td>229.90 (n/a)</td><td>112.23 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.06 <b>(+41.24%)</b></td><td>0.04 (+16.83%)</td><td>0.02 (-10.03%)</td><td>0.01 <b>(-50.28%)</b></td><td>0.02 <b>(+178.41%)</b></td><td>1049.40 <b>(+101.11%)</b></td><td>516.68 (+19.70%)</td><td>541.60 (+11.14%)</td><td>201.00 <b>(-29.20%)</b></td><td>347.21 <b>(+247.85%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.80 (n/a)</td><td>431.64 (n/a)</td><td>487.30 (n/a)</td><td>283.90 (n/a)</td><td>99.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (-1.56%)</td><td>0.03 <b>(-25.10%)</b></td><td>0.03 <b>(-32.46%)</b></td><td>0.02 <b>(-36.48%)</b></td><td>0.01 <b>(+80.50%)</b></td><td>587.00 <b>(+57.46%)</b></td><td>414.30 <b>(+45.51%)</b></td><td>384.70 <b>(+48.08%)</b></td><td>254.60 (+1.60%)</td><td>149.17 <b>(+193.00%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>372.80 (n/a)</td><td>284.72 (n/a)</td><td>259.80 (n/a)</td><td>250.60 (n/a)</td><td>50.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 <b>(+91.17%)</b></td><td>0.02 <b>(+64.04%)</b></td><td>0.02 <b>(+29.17%)</b></td><td>0.02 <b>(+78.33%)</b></td><td>0.01 <b>(+59.95%)</b></td><td>319.20 <b>(-43.92%)</b></td><td>239.36 <b>(-40.49%)</b></td><td>242.80 <b>(-22.58%)</b></td><td>152.60 <b>(-47.69%)</b></td><td>62.22 <b>(-54.45%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.20 (n/a)</td><td>402.22 (n/a)</td><td>313.60 (n/a)</td><td>291.70 (n/a)</td><td>136.60 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 <b>(+27.77%)</b></td><td>0.02 <b>(+26.23%)</b></td><td>0.02 <b>(+43.92%)</b></td><td>0.01 (+8.51%)</td><td>0.01 <b>(+58.79%)</b></td><td>490.60 (-7.83%)</td><td>333.72 (-16.23%)</td><td>269.80 <b>(-30.50%)</b></td><td>207.30 <b>(-21.71%)</b></td><td>132.45 (+19.11%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.30 (n/a)</td><td>398.36 (n/a)</td><td>388.20 (n/a)</td><td>264.80 (n/a)</td><td>111.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (-4.27%)</td><td>0.02 <b>(+44.02%)</b></td><td>0.02 <b>(+80.19%)</b></td><td>0.02 <b>(+76.32%)</b></td><td>0.00 <b>(-57.58%)</b></td><td>330.90 <b>(-43.28%)</b></td><td>274.80 <b>(-36.79%)</b></td><td>261.00 <b>(-44.50%)</b></td><td>239.80 (+4.44%)</td><td>36.10 <b>(-73.66%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.40 (n/a)</td><td>434.76 (n/a)</td><td>470.30 (n/a)</td><td>229.60 (n/a)</td><td>137.07 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 <b>(+67.46%)</b></td><td>0.01 (+19.50%)</td><td>0.01 (+6.06%)</td><td>0.00 <b>(-60.95%)</b></td><td>0.01 <b>(+272.67%)</b></td><td>1889.60 <b>(+156.04%)</b></td><td>800.34 <b>(+40.89%)</b></td><td>564.80 (-5.71%)</td><td>243.50 <b>(-40.27%)</b></td><td>684.35 <b>(+443.31%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>738.00 (n/a)</td><td>568.08 (n/a)</td><td>599.00 (n/a)</td><td>407.70 (n/a)</td><td>125.96 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 <b>(+88.04%)</b></td><td>0.01 <b>(+78.08%)</b></td><td>0.01 <b>(+23.58%)</b></td><td>0.01 <b>(+266.03%)</b></td><td>0.01 <b>(+63.51%)</b></td><td>516.20 <b>(-72.68%)</b></td><td>406.14 <b>(-51.46%)</b></td><td>483.60 (-19.08%)</td><td>254.90 <b>(-46.83%)</b></td><td>126.36 <b>(-78.62%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1889.50 (n/a)</td><td>836.68 (n/a)</td><td>597.60 (n/a)</td><td>479.40 (n/a)</td><td>591.12 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 <b>(+25.64%)</b></td><td>0.02 <b>(+42.97%)</b></td><td>0.02 <b>(+50.30%)</b></td><td>0.01 <b>(+52.00%)</b></td><td>0.01 <b>(+29.57%)</b></td><td>706.30 <b>(-34.21%)</b></td><td>402.16 <b>(-31.33%)</b></td><td>330.60 <b>(-33.47%)</b></td><td>245.60 <b>(-20.39%)</b></td><td>188.89 <b>(-35.26%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1073.60 (n/a)</td><td>585.62 (n/a)</td><td>496.90 (n/a)</td><td>308.50 (n/a)</td><td>291.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>491.20 (n/a)</td><td>308.22 (n/a)</td><td>244.80 (n/a)</td><td>200.40 (n/a)</td><td>119.34 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>346.60 (n/a)</td><td>257.74 (n/a)</td><td>239.80 (n/a)</td><td>163.00 (n/a)</td><td>69.48 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>558.00 (n/a)</td><td>411.06 (n/a)</td><td>490.80 (n/a)</td><td>247.50 (n/a)</td><td>150.37 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>487.90 (n/a)</td><td>382.56 (n/a)</td><td>447.60 (n/a)</td><td>232.20 (n/a)</td><td>112.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>557.00 (n/a)</td><td>386.36 (n/a)</td><td>294.10 (n/a)</td><td>271.60 (n/a)</td><td>138.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>657.30 (n/a)</td><td>400.34 (n/a)</td><td>353.50 (n/a)</td><td>273.50 (n/a)</td><td>153.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.20 (n/a)</td><td>366.68 (n/a)</td><td>272.70 (n/a)</td><td>216.50 (n/a)</td><td>171.73 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>741.10 (n/a)</td><td>429.90 (n/a)</td><td>375.60 (n/a)</td><td>230.30 (n/a)</td><td>208.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2143.60 (n/a)</td><td>740.64 (n/a)</td><td>479.10 (n/a)</td><td>271.10 (n/a)</td><td>792.40 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1072.50 (n/a)</td><td>474.54 (n/a)</td><td>320.40 (n/a)</td><td>237.20 (n/a)</td><td>343.18 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.10 (n/a)</td><td>376.02 (n/a)</td><td>324.80 (n/a)</td><td>285.10 (n/a)</td><td>106.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1976.90 (n/a)</td><td>677.86 (n/a)</td><td>368.30 (n/a)</td><td>255.90 (n/a)</td><td>730.52 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.66 (+9.32%)</td><td>0.46 <b>(+27.48%)</b></td><td>0.43 <b>(+25.10%)</b></td><td>0.37 <b>(+55.52%)</b></td><td>0.11 <b>(-21.40%)</b></td><td>599.30 <b>(-35.70%)</b></td><td>496.08 <b>(-26.54%)</b></td><td>517.20 <b>(-20.06%)</b></td><td>334.80 (-8.52%)</td><td>98.56 <b>(-55.23%)</b></td><td>28.19 (+9.32%)</td><td>19.79 <b>(+27.48%)</b></td><td>18.25 <b>(+25.10%)</b></td><td>15.75 <b>(+55.52%)</b></td><td>4.86 <b>(-21.40%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.60 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>932.00 (n/a)</td><td>675.30 (n/a)</td><td>647.00 (n/a)</td><td>366.00 (n/a)</td><td>220.14 (n/a)</td><td>25.78 (n/a)</td><td>15.52 (n/a)</td><td>14.59 (n/a)</td><td>10.13 (n/a)</td><td>6.19 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.56 (+5.78%)</td><td>0.42 (-1.99%)</td><td>0.42 (-0.93%)</td><td>0.34 (+2.59%)</td><td>0.09 <b>(+20.07%)</b></td><td>655.50 (-2.53%)</td><td>545.14 (+2.94%)</td><td>524.30 (+0.92%)</td><td>397.40 (-5.47%)</td><td>108.69 (+13.14%)</td><td>23.74 (+5.78%)</td><td>17.91 (-1.99%)</td><td>18.00 (-0.93%)</td><td>14.40 (+2.59%)</td><td>3.83 <b>(+20.07%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.53 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>672.50 (n/a)</td><td>529.58 (n/a)</td><td>519.50 (n/a)</td><td>420.40 (n/a)</td><td>96.07 (n/a)</td><td>22.45 (n/a)</td><td>18.28 (n/a)</td><td>18.17 (n/a)</td><td>14.03 (n/a)</td><td>3.19 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.31 (-1.33%)</td><td>0.30 (+0.07%)</td><td>0.30 (+0.32%)</td><td>0.30 (+1.27%)</td><td>0.00 <b>(-40.90%)</b></td><td>84441.40 (-1.26%)</td><td>82982.52 (-0.10%)</td><td>82742.70 (-0.32%)</td><td>81682.30 (+1.34%)</td><td>1268.00 <b>(-40.87%)</b></td><td>210.33 (-1.33%)</td><td>207.07 (+0.07%)</td><td>207.63 (+0.32%)</td><td>203.45 (+1.27%)</td><td>3.16 <b>(-40.90%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>85515.10 (n/a)</td><td>83065.28 (n/a)</td><td>83007.50 (n/a)</td><td>80599.30 (n/a)</td><td>2144.28 (n/a)</td><td>213.15 (n/a)</td><td>206.93 (n/a)</td><td>206.97 (n/a)</td><td>200.90 (n/a)</td><td>5.34 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>1.03 (-2.92%)</td><td>1.01 (+0.82%)</td><td>1.01 (-0.15%)</td><td>1.00 (+9.47%)</td><td>0.01 <b>(-81.51%)</b></td><td>25251.20 (-8.65%)</td><td>24846.02 (-1.06%)</td><td>24799.50 (+0.15%)</td><td>24544.40 (+3.01%)</td><td>255.00 <b>(-82.77%)</b></td><td>699.95 (-2.92%)</td><td>691.51 (+0.82%)</td><td>692.75 (-0.15%)</td><td>680.36 (+9.47%)</td><td>7.06 <b>(-81.51%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>1.06 (n/a)</td><td>1.00 (n/a)</td><td>1.02 (n/a)</td><td>0.91 (n/a)</td><td>0.06 (n/a)</td><td>27642.40 (n/a)</td><td>25113.04 (n/a)</td><td>24761.30 (n/a)</td><td>23828.30 (n/a)</td><td>1480.09 (n/a)</td><td>720.99 (n/a)</td><td>685.90 (n/a)</td><td>693.82 (n/a)</td><td>621.50 (n/a)</td><td>38.15 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>3.66 (+3.51%)</td><td>2.83 (+1.33%)</td><td>2.92 (-8.56%)</td><td>1.95 (+14.98%)</td><td>0.84 (+5.18%)</td><td>4124.00 (-13.03%)</td><td>3077.52 (-1.62%)</td><td>2756.20 (+9.36%)</td><td>2203.30 (-3.39%)</td><td>962.01 (-9.21%)</td><td>959.42 (+3.51%)</td><td>741.61 (+1.33%)</td><td>766.98 (-8.56%)</td><td>512.59 (+14.98%)</td><td>220.50 (+5.18%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>3.53 (n/a)</td><td>2.79 (n/a)</td><td>3.20 (n/a)</td><td>1.70 (n/a)</td><td>0.80 (n/a)</td><td>4741.70 (n/a)</td><td>3128.04 (n/a)</td><td>2520.30 (n/a)</td><td>2280.70 (n/a)</td><td>1059.56 (n/a)</td><td>926.87 (n/a)</td><td>731.90 (n/a)</td><td>838.78 (n/a)</td><td>445.81 (n/a)</td><td>209.63 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.24 (-12.37%)</td><td>0.21 (+7.03%)</td><td>0.21 (+15.12%)</td><td>0.18 <b>(+27.88%)</b></td><td>0.03 <b>(-48.54%)</b></td><td>6999.10 <b>(-21.80%)</b></td><td>6106.98 (-9.96%)</td><td>5925.70 (-13.13%)</td><td>5135.70 (+14.12%)</td><td>770.08 <b>(-51.93%)</b></td><td>13.07 (-12.37%)</td><td>11.13 (+7.03%)</td><td>11.33 (+15.12%)</td><td>9.59 <b>(+27.88%)</b></td><td>1.42 <b>(-48.54%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>8950.10 (n/a)</td><td>6782.70 (n/a)</td><td>6821.50 (n/a)</td><td>4500.30 (n/a)</td><td>1601.93 (n/a)</td><td>14.91 (n/a)</td><td>10.40 (n/a)</td><td>9.84 (n/a)</td><td>7.50 (n/a)</td><td>2.76 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>3.93 (n/a)</td><td>3.67 (n/a)</td><td>3.65 (n/a)</td><td>3.46 (n/a)</td><td>0.20 (n/a)</td><td>3.93 (n/a)</td><td>3.67 (n/a)</td><td>3.65 (n/a)</td><td>3.46 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>7.41 (+7.10%)</td><td>6.45 (+6.92%)</td><td>6.69 (+13.51%)</td><td>5.66 (+0.31%)</td><td>0.76 <b>(+48.24%)</b></td><td>7.40 (+7.10%)</td><td>6.44 (+6.92%)</td><td>6.69 (+13.51%)</td><td>5.66 (+0.31%)</td><td>0.76 <b>(+48.24%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>6.92 (n/a)</td><td>6.03 (n/a)</td><td>5.90 (n/a)</td><td>5.64 (n/a)</td><td>0.51 (n/a)</td><td>6.91 (n/a)</td><td>6.03 (n/a)</td><td>5.89 (n/a)</td><td>5.64 (n/a)</td><td>0.51 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>10.15 <b>(-22.26%)</b></td><td>8.76 (-9.94%)</td><td>8.50 (-15.75%)</td><td>8.20 <b>(+21.16%)</b></td><td>0.78 <b>(-66.44%)</b></td><td>10.14 <b>(-22.26%)</b></td><td>8.75 (-9.94%)</td><td>8.49 (-15.75%)</td><td>8.20 <b>(+21.16%)</b></td><td>0.78 <b>(-66.44%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>13.05 (n/a)</td><td>9.73 (n/a)</td><td>10.08 (n/a)</td><td>6.77 (n/a)</td><td>2.34 (n/a)</td><td>13.04 (n/a)</td><td>9.72 (n/a)</td><td>10.08 (n/a)</td><td>6.77 (n/a)</td><td>2.34 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>3.90 (n/a)</td><td>3.65 (n/a)</td><td>3.53 (n/a)</td><td>3.48 (n/a)</td><td>0.20 (n/a)</td><td>3.90 (n/a)</td><td>3.65 (n/a)</td><td>3.53 (n/a)</td><td>3.48 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>7.49 (+9.18%)</td><td>6.62 (+8.37%)</td><td>6.52 (+6.84%)</td><td>5.77 (+9.84%)</td><td>0.66 (+2.13%)</td><td>7.49 (+9.18%)</td><td>6.62 (+8.37%)</td><td>6.52 (+6.84%)</td><td>5.77 (+9.84%)</td><td>0.66 (+2.13%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>6.86 (n/a)</td><td>6.11 (n/a)</td><td>6.11 (n/a)</td><td>5.25 (n/a)</td><td>0.64 (n/a)</td><td>6.86 (n/a)</td><td>6.11 (n/a)</td><td>6.10 (n/a)</td><td>5.25 (n/a)</td><td>0.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>14.05 (+6.16%)</td><td>12.54 <b>(+23.86%)</b></td><td>13.73 <b>(+57.70%)</b></td><td>7.51 (+0.71%)</td><td>2.82 (+5.38%)</td><td>14.05 (+6.16%)</td><td>12.54 <b>(+23.86%)</b></td><td>13.72 <b>(+57.70%)</b></td><td>7.50 (+0.71%)</td><td>2.82 (+5.38%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>13.24 (n/a)</td><td>10.13 (n/a)</td><td>8.71 (n/a)</td><td>7.45 (n/a)</td><td>2.68 (n/a)</td><td>13.23 (n/a)</td><td>10.12 (n/a)</td><td>8.70 (n/a)</td><td>7.45 (n/a)</td><td>2.67 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>3.15 (-0.75%)</td><td>2.52 (+11.27%)</td><td>3.04 (+4.25%)</td><td>1.09 (+0.03%)</td><td>0.89 (-15.49%)</td><td>3.14 (-0.75%)</td><td>2.51 (+11.27%)</td><td>3.03 (+4.25%)</td><td>1.09 (+0.03%)</td><td>0.89 (-15.49%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>3.17 (n/a)</td><td>2.26 (n/a)</td><td>2.91 (n/a)</td><td>1.09 (n/a)</td><td>1.05 (n/a)</td><td>3.17 (n/a)</td><td>2.26 (n/a)</td><td>2.91 (n/a)</td><td>1.09 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.57 (+1.36%)</td><td>0.37 <b>(+24.48%)</b></td><td>0.35 <b>(+40.93%)</b></td><td>0.08 (+0.68%)</td><td>0.20 (-11.31%)</td><td>0.56 (+1.36%)</td><td>0.37 <b>(+24.48%)</b></td><td>0.34 <b>(+40.93%)</b></td><td>0.08 (+0.68%)</td><td>0.20 (-11.31%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.56 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.08 (n/a)</td><td>0.22 (n/a)</td><td>0.55 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.73 (+0.15%)</td><td>0.41 <b>(-36.75%)</b></td><td>0.46 <b>(-35.34%)</b></td><td>0.08 <b>(-81.32%)</b></td><td>0.24 <b>(+79.03%)</b></td><td>0.72 (+0.15%)</td><td>0.41 <b>(-36.75%)</b></td><td>0.46 <b>(-35.34%)</b></td><td>0.08 <b>(-81.32%)</b></td><td>0.24 <b>(+79.03%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.73 (n/a)</td><td>0.65 (n/a)</td><td>0.72 (n/a)</td><td>0.41 (n/a)</td><td>0.13 (n/a)</td><td>0.72 (n/a)</td><td>0.64 (n/a)</td><td>0.71 (n/a)</td><td>0.41 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>2.47 (-1.03%)</td><td>1.58 <b>(+49.31%)</b></td><td>1.78 <b>(+114.11%)</b></td><td>0.44 (+0.74%)</td><td>0.76 (-9.70%)</td><td>2.43 (-1.03%)</td><td>1.55 <b>(+49.31%)</b></td><td>1.75 <b>(+114.11%)</b></td><td>0.43 (+0.74%)</td><td>0.75 (-9.70%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>2.49 (n/a)</td><td>1.06 (n/a)</td><td>0.83 (n/a)</td><td>0.44 (n/a)</td><td>0.85 (n/a)</td><td>2.45 (n/a)</td><td>1.04 (n/a)</td><td>0.82 (n/a)</td><td>0.43 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>517.90 (n/a)</td><td>341.80 (n/a)</td><td>311.10 (n/a)</td><td>203.00 (n/a)</td><td>122.27 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>390.80 (n/a)</td><td>305.56 (n/a)</td><td>281.80 (n/a)</td><td>198.30 (n/a)</td><td>79.06 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.90 (n/a)</td><td>412.24 (n/a)</td><td>455.10 (n/a)</td><td>253.70 (n/a)</td><td>146.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>623.80 (n/a)</td><td>464.66 (n/a)</td><td>404.30 (n/a)</td><td>368.40 (n/a)</td><td>107.92 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2465.80 (n/a)</td><td>812.48 (n/a)</td><td>438.60 (n/a)</td><td>272.10 (n/a)</td><td>927.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2315.80 (n/a)</td><td>931.82 (n/a)</td><td>625.50 (n/a)</td><td>429.40 (n/a)</td><td>786.63 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (+7.68%)</td><td>0.02 (-10.67%)</td><td>0.02 <b>(-36.57%)</b></td><td>0.01 (-12.38%)</td><td>0.01 <b>(+43.96%)</b></td><td>592.70 (+14.13%)</td><td>451.90 (+19.79%)</td><td>519.30 <b>(+57.65%)</b></td><td>253.10 (-7.15%)</td><td>162.42 <b>(+54.91%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.30 (n/a)</td><td>377.24 (n/a)</td><td>329.40 (n/a)</td><td>272.60 (n/a)</td><td>104.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (-1.65%)</td><td>0.02 (-14.66%)</td><td>0.02 <b>(-45.72%)</b></td><td>0.01 (-5.08%)</td><td>0.01 (+1.98%)</td><td>582.60 (+5.35%)</td><td>425.66 (+18.40%)</td><td>494.80 <b>(+84.21%)</b></td><td>259.40 (+1.69%)</td><td>150.31 (+8.13%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.00 (n/a)</td><td>359.50 (n/a)</td><td>268.60 (n/a)</td><td>255.10 (n/a)</td><td>139.01 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (+19.60%)</td><td>0.03 (+7.17%)</td><td>0.03 <b>(+28.91%)</b></td><td>0.02 (-4.10%)</td><td>0.01 <b>(+38.88%)</b></td><td>486.20 (+4.29%)</td><td>347.18 (-2.57%)</td><td>304.00 <b>(-22.41%)</b></td><td>218.00 (-16.38%)</td><td>120.23 <b>(+34.38%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>466.20 (n/a)</td><td>356.32 (n/a)</td><td>391.80 (n/a)</td><td>260.70 (n/a)</td><td>89.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (-1.58%)</td><td>0.02 (-16.93%)</td><td>0.02 <b>(-30.66%)</b></td><td>0.02 (-7.25%)</td><td>0.01 (+7.32%)</td><td>491.00 (+7.82%)</td><td>412.84 <b>(+21.40%)</b></td><td>441.10 <b>(+44.24%)</b></td><td>264.20 (+1.58%)</td><td>90.01 (+12.73%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>455.40 (n/a)</td><td>340.06 (n/a)</td><td>305.80 (n/a)</td><td>260.10 (n/a)</td><td>79.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 <b>(+105.91%)</b></td><td>0.02 <b>(+32.26%)</b></td><td>0.02 (+0.02%)</td><td>0.01 (+6.39%)</td><td>0.02 <b>(+255.28%)</b></td><td>550.40 (-5.99%)</td><td>416.02 (-10.19%)</td><td>459.40 (+0.00%)</td><td>153.50 <b>(-51.45%)</b></td><td>155.14 <b>(+53.07%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>585.50 (n/a)</td><td>463.24 (n/a)</td><td>459.40 (n/a)</td><td>316.20 (n/a)</td><td>101.35 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 <b>(-37.46%)</b></td><td>0.02 (-18.17%)</td><td>0.02 (-11.15%)</td><td>0.01 (-18.60%)</td><td>0.00 <b>(-65.15%)</b></td><td>587.10 <b>(+22.85%)</b></td><td>490.24 (+18.92%)</td><td>473.10 (+12.54%)</td><td>450.10 <b>(+59.89%)</b></td><td>55.77 <b>(-28.73%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>477.90 (n/a)</td><td>412.24 (n/a)</td><td>420.40 (n/a)</td><td>281.50 (n/a)</td><td>78.25 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (+5.84%)</td><td>0.02 (-11.09%)</td><td>0.02 (-4.21%)</td><td>0.00 <b>(-72.30%)</b></td><td>0.01 <b>(+52.80%)</b></td><td>2018.90 <b>(+261.03%)</b></td><td>760.24 <b>(+65.31%)</b></td><td>507.10 (+4.41%)</td><td>250.10 (-5.52%)</td><td>713.23 <b>(+512.82%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.20 (n/a)</td><td>459.90 (n/a)</td><td>485.70 (n/a)</td><td>264.70 (n/a)</td><td>116.39 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (-5.46%)</td><td>0.02 (-13.32%)</td><td>0.02 (-0.30%)</td><td>0.01 (-13.88%)</td><td>0.01 (-10.37%)</td><td>625.20 (+16.12%)</td><td>513.10 (+14.83%)</td><td>536.50 (+0.30%)</td><td>309.30 (+5.78%)</td><td>131.08 (+5.76%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.40 (n/a)</td><td>446.82 (n/a)</td><td>534.90 (n/a)</td><td>292.40 (n/a)</td><td>123.94 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (+8.70%)</td><td>0.03 <b>(+29.98%)</b></td><td>0.03 <b>(+50.98%)</b></td><td>0.02 (-3.61%)</td><td>0.01 (+0.42%)</td><td>544.50 (+3.73%)</td><td>340.56 <b>(-22.98%)</b></td><td>311.00 <b>(-33.76%)</b></td><td>222.20 (-7.99%)</td><td>121.11 (+5.06%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.90 (n/a)</td><td>442.18 (n/a)</td><td>469.50 (n/a)</td><td>241.50 (n/a)</td><td>115.28 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (-9.96%)</td><td>0.03 (+5.16%)</td><td>0.02 <b>(+29.26%)</b></td><td>0.02 <b>(+21.90%)</b></td><td>0.01 <b>(-23.29%)</b></td><td>538.90 (-17.96%)</td><td>368.22 (-13.16%)</td><td>336.90 <b>(-22.64%)</b></td><td>233.50 (+11.03%)</td><td>142.52 <b>(-29.34%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>656.90 (n/a)</td><td>424.04 (n/a)</td><td>435.50 (n/a)</td><td>210.30 (n/a)</td><td>201.68 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (+14.85%)</td><td>0.02 (+10.18%)</td><td>0.02 (-8.63%)</td><td>0.01 (+12.06%)</td><td>0.01 <b>(+23.82%)</b></td><td>586.90 (-10.75%)</td><td>413.14 (-6.66%)</td><td>501.10 (+9.43%)</td><td>214.80 (-12.93%)</td><td>171.55 (-3.66%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>657.60 (n/a)</td><td>442.60 (n/a)</td><td>457.90 (n/a)</td><td>246.70 (n/a)</td><td>178.07 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (+4.88%)</td><td>0.03 <b>(+61.61%)</b></td><td>0.04 <b>(+108.12%)</b></td><td>0.02 <b>(+44.53%)</b></td><td>0.01 (-14.20%)</td><td>438.70 <b>(-30.80%)</b></td><td>273.06 <b>(-41.41%)</b></td><td>234.00 <b>(-51.95%)</b></td><td>224.10 (-4.64%)</td><td>92.93 <b>(-39.97%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.00 (n/a)</td><td>466.02 (n/a)</td><td>487.00 (n/a)</td><td>235.00 (n/a)</td><td>154.80 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (+11.25%)</td><td>0.02 <b>(+56.83%)</b></td><td>0.03 <b>(+104.91%)</b></td><td>0.01 <b>(+77.96%)</b></td><td>0.01 (-9.22%)</td><td>609.10 <b>(-43.82%)</b></td><td>377.36 <b>(-42.01%)</b></td><td>312.00 <b>(-51.20%)</b></td><td>241.90 (-10.11%)</td><td>146.51 <b>(-49.37%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1084.10 (n/a)</td><td>650.78 (n/a)</td><td>639.30 (n/a)</td><td>269.10 (n/a)</td><td>289.39 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 <b>(+44.82%)</b></td><td>0.02 (+4.42%)</td><td>0.02 (-7.06%)</td><td>0.00 <b>(-68.61%)</b></td><td>0.01 <b>(+232.04%)</b></td><td>1826.80 <b>(+218.65%)</b></td><td>703.40 <b>(+43.42%)</b></td><td>514.10 (+7.60%)</td><td>259.20 <b>(-30.94%)</b></td><td>638.71 <b>(+701.59%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.30 (n/a)</td><td>490.44 (n/a)</td><td>477.80 (n/a)</td><td>375.30 (n/a)</td><td>79.68 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.11 <b>(+33.05%)</b></td><td>0.08 <b>(+75.75%)</b></td><td>0.08 <b>(+84.30%)</b></td><td>0.05 <b>(+249.46%)</b></td><td>0.02 (-7.57%)</td><td>531.50 <b>(-71.38%)</b></td><td>326.84 <b>(-56.71%)</b></td><td>294.50 <b>(-45.73%)</b></td><td>226.20 <b>(-24.83%)</b></td><td>117.97 <b>(-81.12%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1857.40 (n/a)</td><td>755.04 (n/a)</td><td>542.70 (n/a)</td><td>300.90 (n/a)</td><td>624.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.18 (+15.56%)</td><td>0.14 <b>(+24.68%)</b></td><td>0.14 (+14.79%)</td><td>0.09 <b>(+25.16%)</b></td><td>0.03 (-8.91%)</td><td>439.80 <b>(-20.11%)</b></td><td>305.04 <b>(-22.58%)</b></td><td>291.30 (-12.89%)</td><td>233.30 (-13.50%)</td><td>80.73 <b>(-37.51%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>550.50 (n/a)</td><td>394.00 (n/a)</td><td>334.40 (n/a)</td><td>269.70 (n/a)</td><td>129.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 <b>(+21.83%)</b></td><td>0.01 (-19.35%)</td><td>0.01 <b>(-36.19%)</b></td><td>0.01 (-19.58%)</td><td>0.01 <b>(+82.32%)</b></td><td>579.80 <b>(+24.34%)</b></td><td>439.12 <b>(+33.85%)</b></td><td>455.40 <b>(+56.71%)</b></td><td>230.10 (-17.91%)</td><td>143.64 <b>(+82.76%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>466.30 (n/a)</td><td>328.06 (n/a)</td><td>290.60 (n/a)</td><td>280.30 (n/a)</td><td>78.60 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (-7.64%)</td><td>0.03 (-13.99%)</td><td>0.03 (-6.07%)</td><td>0.02 <b>(-31.55%)</b></td><td>0.01 <b>(+44.95%)</b></td><td>479.10 <b>(+46.11%)</b></td><td>325.92 <b>(+23.85%)</b></td><td>271.00 (+6.44%)</td><td>223.20 (+8.30%)</td><td>114.23 <b>(+129.44%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>327.90 (n/a)</td><td>263.16 (n/a)</td><td>254.60 (n/a)</td><td>206.10 (n/a)</td><td>49.79 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (+13.27%)</td><td>0.04 (+16.20%)</td><td>0.04 <b>(+40.03%)</b></td><td>0.02 (-3.72%)</td><td>0.01 <b>(+56.78%)</b></td><td>551.90 (+3.86%)</td><td>371.30 (-10.41%)</td><td>297.60 <b>(-28.60%)</b></td><td>275.60 (-11.72%)</td><td>120.46 <b>(+42.33%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.40 (n/a)</td><td>414.46 (n/a)</td><td>416.80 (n/a)</td><td>312.20 (n/a)</td><td>84.64 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 <b>(-26.98%)</b></td><td>0.02 (-18.76%)</td><td>0.02 (-5.23%)</td><td>0.01 (-4.89%)</td><td>0.01 <b>(-46.43%)</b></td><td>581.20 (+5.14%)</td><td>439.26 (+13.50%)</td><td>428.40 (+5.54%)</td><td>280.90 <b>(+36.96%)</b></td><td>108.78 <b>(-26.22%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.80 (n/a)</td><td>387.02 (n/a)</td><td>405.90 (n/a)</td><td>205.10 (n/a)</td><td>147.44 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 <b>(+56.55%)</b></td><td>0.03 (+14.10%)</td><td>0.02 (-8.44%)</td><td>0.01 <b>(-30.82%)</b></td><td>0.02 <b>(+188.09%)</b></td><td>752.20 <b>(+44.54%)</b></td><td>464.64 (+9.86%)</td><td>492.20 (+9.21%)</td><td>187.80 <b>(-36.12%)</b></td><td>237.23 <b>(+168.42%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.40 (n/a)</td><td>422.94 (n/a)</td><td>450.70 (n/a)</td><td>294.00 (n/a)</td><td>88.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 <b>(-27.18%)</b></td><td>0.02 <b>(-35.56%)</b></td><td>0.02 <b>(-50.01%)</b></td><td>0.01 <b>(-20.64%)</b></td><td>0.00 <b>(-48.68%)</b></td><td>564.60 <b>(+26.00%)</b></td><td>476.72 <b>(+48.33%)</b></td><td>492.60 <b>(+100.00%)</b></td><td>327.70 <b>(+37.29%)</b></td><td>92.86 (-13.13%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>448.10 (n/a)</td><td>321.40 (n/a)</td><td>246.30 (n/a)</td><td>238.70 (n/a)</td><td>106.89 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (+1.80%)</td><td>0.03 (+19.57%)</td><td>0.04 <b>(+83.19%)</b></td><td>0.02 (-4.09%)</td><td>0.01 (+10.27%)</td><td>609.50 (+4.28%)</td><td>390.82 (-13.10%)</td><td>279.70 <b>(-45.40%)</b></td><td>222.90 (-1.76%)</td><td>181.70 (+18.96%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>584.50 (n/a)</td><td>449.74 (n/a)</td><td>512.30 (n/a)</td><td>226.90 (n/a)</td><td>152.74 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 (+6.47%)</td><td>0.03 (+3.00%)</td><td>0.03 (+5.68%)</td><td>0.02 (-7.66%)</td><td>0.01 <b>(+31.87%)</b></td><td>500.30 (+8.29%)</td><td>318.36 (+5.31%)</td><td>278.00 (-5.38%)</td><td>163.20 (-6.10%)</td><td>147.20 <b>(+40.65%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>462.00 (n/a)</td><td>302.32 (n/a)</td><td>293.80 (n/a)</td><td>173.80 (n/a)</td><td>104.66 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (+18.04%)</td><td>0.02 (-4.67%)</td><td>0.02 (-1.85%)</td><td>0.01 <b>(-52.50%)</b></td><td>0.01 <b>(+88.87%)</b></td><td>1036.60 <b>(+110.52%)</b></td><td>534.22 <b>(+24.56%)</b></td><td>466.60 (+1.90%)</td><td>243.20 (-15.29%)</td><td>296.73 <b>(+263.76%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.40 (n/a)</td><td>428.88 (n/a)</td><td>457.90 (n/a)</td><td>287.10 (n/a)</td><td>81.57 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.05 <b>(+31.95%)</b></td><td>0.03 (+14.76%)</td><td>0.03 <b>(+27.99%)</b></td><td>0.01 (-13.16%)</td><td>0.01 <b>(+37.77%)</b></td><td>563.30 (+15.15%)</td><td>323.58 (-7.69%)</td><td>259.80 <b>(-21.89%)</b></td><td>165.70 <b>(-24.23%)</b></td><td>154.03 <b>(+20.79%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>489.20 (n/a)</td><td>350.52 (n/a)</td><td>332.60 (n/a)</td><td>218.70 (n/a)</td><td>127.53 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.04 (+11.15%)</td><td>0.02 <b>(-23.07%)</b></td><td>0.02 (-19.62%)</td><td>0.01 <b>(-69.91%)</b></td><td>0.01 <b>(+59.60%)</b></td><td>1649.90 <b>(+232.31%)</b></td><td>695.12 <b>(+79.91%)</b></td><td>532.60 <b>(+24.44%)</b></td><td>223.70 (-10.02%)</td><td>551.46 <b>(+401.55%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.50 (n/a)</td><td>386.38 (n/a)</td><td>428.00 (n/a)</td><td>248.60 (n/a)</td><td>109.95 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.03 (+3.84%)</td><td>0.02 (+4.71%)</td><td>0.02 (-14.76%)</td><td>0.01 <b>(+196.83%)</b></td><td>0.00 <b>(-43.28%)</b></td><td>633.30 <b>(-66.31%)</b></td><td>474.00 <b>(-32.75%)</b></td><td>475.90 (+17.33%)</td><td>323.20 (-3.69%)</td><td>110.04 <b>(-83.35%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1879.70 (n/a)</td><td>704.86 (n/a)</td><td>405.60 (n/a)</td><td>335.60 (n/a)</td><td>660.87 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.35 (-3.05%)</td><td>0.29 (-6.01%)</td><td>0.34 (+5.07%)</td><td>0.19 (-7.51%)</td><td>0.08 <b>(+22.53%)</b></td><td>524.90 (+8.12%)</td><td>361.20 (+8.80%)</td><td>291.50 (-4.83%)</td><td>281.80 (+3.15%)</td><td>109.88 <b>(+26.16%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>485.50 (n/a)</td><td>331.98 (n/a)</td><td>306.30 (n/a)</td><td>273.20 (n/a)</td><td>87.09 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.30 (-9.03%)</td><td>0.22 (+9.22%)</td><td>0.20 (+6.80%)</td><td>0.18 <b>(+91.88%)</b></td><td>0.05 <b>(-42.97%)</b></td><td>537.00 <b>(-47.88%)</b></td><td>465.30 (-18.97%)</td><td>483.90 (-6.37%)</td><td>330.50 (+9.91%)</td><td>85.71 <b>(-68.53%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.33 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>1030.30 (n/a)</td><td>574.20 (n/a)</td><td>516.80 (n/a)</td><td>300.70 (n/a)</td><td>272.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.36 (-10.07%)</td><td>0.21 <b>(-29.42%)</b></td><td>0.20 <b>(-34.84%)</b></td><td>0.04 <b>(-74.42%)</b></td><td>0.12 <b>(+26.53%)</b></td><td>2422.70 <b>(+290.95%)</b></td><td>815.30 <b>(+123.32%)</b></td><td>499.50 <b>(+53.46%)</b></td><td>274.50 (+11.22%)</td><td>903.57 <b>(+507.59%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>619.70 (n/a)</td><td>365.08 (n/a)</td><td>325.50 (n/a)</td><td>246.80 (n/a)</td><td>148.71 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.29 <b>(+24.72%)</b></td><td>0.22 <b>(+27.47%)</b></td><td>0.24 <b>(+37.95%)</b></td><td>0.15 <b>(+29.83%)</b></td><td>0.06 <b>(+29.64%)</b></td><td>504.10 <b>(-22.98%)</b></td><td>353.58 <b>(-21.27%)</b></td><td>304.80 <b>(-27.51%)</b></td><td>250.40 (-19.82%)</td><td>108.32 (-19.54%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>654.50 (n/a)</td><td>449.12 (n/a)</td><td>420.50 (n/a)</td><td>312.30 (n/a)</td><td>134.63 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.35 (+14.03%)</td><td>0.22 <b>(+24.57%)</b></td><td>0.15 (+1.81%)</td><td>0.12 (+0.63%)</td><td>0.11 <b>(+48.19%)</b></td><td>598.10 (-0.63%)</td><td>413.10 (-11.89%)</td><td>488.10 (-1.77%)</td><td>211.30 (-12.29%)</td><td>181.71 <b>(+33.67%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>601.90 (n/a)</td><td>468.86 (n/a)</td><td>496.90 (n/a)</td><td>240.90 (n/a)</td><td>135.94 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.28 <b>(+32.24%)</b></td><td>0.14 (+1.46%)</td><td>0.13 (-15.19%)</td><td>0.07 <b>(+139.78%)</b></td><td>0.08 (+19.64%)</td><td>1044.50 <b>(-58.30%)</b></td><td>641.28 <b>(-25.83%)</b></td><td>576.10 (+17.91%)</td><td>259.30 <b>(-24.38%)</b></td><td>290.93 <b>(-68.40%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>2504.50 (n/a)</td><td>864.62 (n/a)</td><td>488.60 (n/a)</td><td>342.90 (n/a)</td><td>920.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.49 (+14.59%)</td><td>0.34 (+10.95%)</td><td>0.29 (-1.85%)</td><td>0.21 <b>(+27.92%)</b></td><td>0.13 <b>(+22.74%)</b></td><td>619.60 <b>(-21.83%)</b></td><td>433.62 (-9.62%)</td><td>454.30 (+1.88%)</td><td>267.60 (-12.72%)</td><td>160.77 (-18.64%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.43 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>792.60 (n/a)</td><td>479.76 (n/a)</td><td>445.90 (n/a)</td><td>306.60 (n/a)</td><td>197.62 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.47 (-12.57%)</td><td>0.34 (+7.29%)</td><td>0.35 <b>(+32.30%)</b></td><td>0.21 (+7.63%)</td><td>0.10 <b>(-27.17%)</b></td><td>618.40 (-7.09%)</td><td>416.80 (-11.80%)</td><td>379.10 <b>(-24.42%)</b></td><td>276.50 (+14.40%)</td><td>135.99 <b>(-21.70%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.54 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>665.60 (n/a)</td><td>472.56 (n/a)</td><td>501.60 (n/a)</td><td>241.70 (n/a)</td><td>173.68 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.55 <b>(+49.66%)</b></td><td>0.39 <b>(+50.45%)</b></td><td>0.38 <b>(+47.36%)</b></td><td>0.26 <b>(+60.26%)</b></td><td>0.11 <b>(+46.29%)</b></td><td>505.10 <b>(-37.60%)</b></td><td>357.32 <b>(-34.05%)</b></td><td>348.50 <b>(-32.15%)</b></td><td>237.40 <b>(-33.16%)</b></td><td>98.24 <b>(-40.45%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>809.50 (n/a)</td><td>541.82 (n/a)</td><td>513.60 (n/a)</td><td>355.20 (n/a)</td><td>164.97 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (-0.33%)</td><td>0.01 (-1.31%)</td><td>0.01 (-7.90%)</td><td>0.01 <b>(+56.75%)</b></td><td>0.00 (-19.93%)</td><td>489.90 <b>(-36.20%)</b></td><td>377.72 (-6.90%)</td><td>376.90 (+8.59%)</td><td>255.30 (+0.31%)</td><td>98.01 <b>(-52.49%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>767.90 (n/a)</td><td>405.72 (n/a)</td><td>347.10 (n/a)</td><td>254.50 (n/a)</td><td>206.31 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.01 (+7.24%)</td><td>0.01 <b>(-23.66%)</b></td><td>0.01 <b>(-35.38%)</b></td><td>0.01 (-10.30%)</td><td>0.00 <b>(+28.11%)</b></td><td>560.60 (+11.47%)</td><td>467.36 <b>(+33.92%)</b></td><td>484.90 <b>(+54.77%)</b></td><td>285.20 (-6.74%)</td><td>109.64 <b>(+27.29%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>502.90 (n/a)</td><td>348.98 (n/a)</td><td>313.30 (n/a)</td><td>305.80 (n/a)</td><td>86.14 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.02 (+8.53%)</td><td>0.01 (+8.23%)</td><td>0.01 <b>(+34.69%)</b></td><td>0.01 (+1.83%)</td><td>0.00 (+2.72%)</td><td>553.70 (-1.79%)</td><td>400.84 (-7.79%)</td><td>365.70 <b>(-25.76%)</b></td><td>251.10 (-7.85%)</td><td>130.81 (-3.32%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>563.80 (n/a)</td><td>434.70 (n/a)</td><td>492.60 (n/a)</td><td>272.50 (n/a)</td><td>135.30 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.62 (+2.49%)</td><td>0.50 (+13.77%)</td><td>0.50 (-0.02%)</td><td>0.32 (+19.63%)</td><td>0.11 <b>(-29.18%)</b></td><td>417.80 (-16.41%)</td><td>280.78 (-18.31%)</td><td>266.20 (+0.00%)</td><td>214.20 (-2.46%)</td><td>79.78 <b>(-42.86%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.60 (n/a)</td><td>0.44 (n/a)</td><td>0.50 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>499.80 (n/a)</td><td>343.70 (n/a)</td><td>266.20 (n/a)</td><td>219.60 (n/a)</td><td>139.63 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.52 (-5.17%)</td><td>0.37 (-9.04%)</td><td>0.29 <b>(-36.08%)</b></td><td>0.26 <b>(+26.18%)</b></td><td>0.12 (-14.16%)</td><td>505.80 <b>(-20.75%)</b></td><td>384.38 (+4.63%)</td><td>448.40 <b>(+56.45%)</b></td><td>255.00 (+5.46%)</td><td>116.45 <b>(-30.27%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.55 (n/a)</td><td>0.41 (n/a)</td><td>0.46 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>638.20 (n/a)</td><td>367.36 (n/a)</td><td>286.60 (n/a)</td><td>241.80 (n/a)</td><td>167.01 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.57 (+16.39%)</td><td>0.46 (+16.73%)</td><td>0.48 (+5.39%)</td><td>0.28 (+9.68%)</td><td>0.11 (+1.11%)</td><td>478.70 (-8.84%)</td><td>306.54 (-15.15%)</td><td>274.40 (-5.12%)</td><td>232.10 (-14.07%)</td><td>98.18 (-14.08%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.49 (n/a)</td><td>0.39 (n/a)</td><td>0.46 (n/a)</td><td>0.25 (n/a)</td><td>0.11 (n/a)</td><td>525.10 (n/a)</td><td>361.26 (n/a)</td><td>289.20 (n/a)</td><td>270.10 (n/a)</td><td>114.26 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.45 (-11.63%)</td><td>0.40 (+4.76%)</td><td>0.43 (+6.39%)</td><td>0.31 <b>(+42.03%)</b></td><td>0.06 <b>(-48.52%)</b></td><td>428.10 <b>(-29.59%)</b></td><td>340.06 (-11.67%)</td><td>308.40 (-6.00%)</td><td>290.80 (+13.15%)</td><td>59.07 <b>(-59.24%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.51 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>608.00 (n/a)</td><td>384.98 (n/a)</td><td>328.10 (n/a)</td><td>257.00 (n/a)</td><td>144.94 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.56 (+6.35%)</td><td>0.46 (+4.00%)</td><td>0.49 (+8.12%)</td><td>0.26 (-9.17%)</td><td>0.12 <b>(+22.87%)</b></td><td>517.00 (+10.09%)</td><td>312.68 (-1.06%)</td><td>269.60 (-7.51%)</td><td>236.60 (-6.00%)</td><td>115.27 <b>(+30.64%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.52 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>0.28 (n/a)</td><td>0.09 (n/a)</td><td>469.60 (n/a)</td><td>316.04 (n/a)</td><td>291.50 (n/a)</td><td>251.70 (n/a)</td><td>88.24 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.01 (-12.52%)</td><td>0.01 (-13.14%)</td><td>0.01 <b>(-23.80%)</b></td><td>0.01 (+17.20%)</td><td>0.00 <b>(-31.46%)</b></td><td>573.50 (-14.68%)</td><td>431.22 (+7.32%)</td><td>394.70 <b>(+31.22%)</b></td><td>281.60 (+14.29%)</td><td>119.59 <b>(-32.55%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>672.20 (n/a)</td><td>401.80 (n/a)</td><td>300.80 (n/a)</td><td>246.40 (n/a)</td><td>177.29 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.01 (-9.96%)</td><td>0.01 <b>(-30.11%)</b></td><td>0.01 <b>(-35.46%)</b></td><td>0.01 <b>(-34.80%)</b></td><td>0.00 <b>(+224.70%)</b></td><td>463.00 <b>(+53.36%)</b></td><td>416.70 <b>(+46.57%)</b></td><td>434.00 <b>(+54.94%)</b></td><td>301.40 (+11.05%)</td><td>66.54 <b>(+441.08%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>301.90 (n/a)</td><td>284.30 (n/a)</td><td>280.10 (n/a)</td><td>271.40 (n/a)</td><td>12.30 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.00 <b>(+40.00%)</b></td><td>0.00 <b>(+64.29%)</b></td><td>0.00 <b>(+150.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+92.51%)</b></td><td>21415.50 (+11.71%)</td><td>11789.16 <b>(-23.72%)</b></td><td>7780.39 <b>(-54.67%)</b></td><td>5714.62 <b>(-27.07%)</b></td><td>7500.24 <b>(+63.17%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19170.96 (n/a)</td><td>15456.11 (n/a)</td><td>17163.05 (n/a)</td><td>7836.15 (n/a)</td><td>4596.49 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.00 (+18.18%)</td><td>0.00 <b>(+25.00%)</b></td><td>0.00 (+20.00%)</td><td>0.00 <b>(+25.00%)</b></td><td>0.00 <b>(+22.69%)</b></td><td>17782.76 <b>(-22.62%)</b></td><td>12587.83 <b>(-21.84%)</b></td><td>14885.21 (-10.51%)</td><td>6077.00 (-18.94%)</td><td>5418.64 <b>(-22.71%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22982.51 (n/a)</td><td>16106.05 (n/a)</td><td>16633.39 (n/a)</td><td>7497.29 (n/a)</td><td>7010.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>0.14 (-2.05%)</td><td>0.09 (-3.42%)</td><td>0.08 (-4.71%)</td><td>0.07 (-7.16%)</td><td>0.03 (+0.70%)</td><td>29397.45 (+7.61%)</td><td>24686.08 (+4.06%)</td><td>26578.49 (+4.96%)</td><td>14617.47 (+2.09%)</td><td>5771.46 (+8.44%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>27319.71 (n/a)</td><td>23722.69 (n/a)</td><td>25321.65 (n/a)</td><td>14318.24 (n/a)</td><td>5322.31 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>1.85 <b>(+25.89%)</b></td><td>1.36 <b>(+26.41%)</b></td><td>1.66 <b>(+54.79%)</b></td><td>0.71 <b>(+22.41%)</b></td><td>0.52 <b>(+36.73%)</b></td><td>740.50 (-18.31%)</td><td>447.88 (-18.59%)</td><td>315.80 <b>(-35.41%)</b></td><td>283.90 <b>(-20.57%)</b></td><td>204.70 (-9.81%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>1.47 (n/a)</td><td>1.07 (n/a)</td><td>1.07 (n/a)</td><td>0.58 (n/a)</td><td>0.38 (n/a)</td><td>906.50 (n/a)</td><td>550.14 (n/a)</td><td>488.90 (n/a)</td><td>357.40 (n/a)</td><td>226.98 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>3.06 (-1.38%)</td><td>1.96 (-10.46%)</td><td>1.39 <b>(-39.71%)</b></td><td>1.37 (+3.72%)</td><td>0.81 (+18.74%)</td><td>768.00 (-3.59%)</td><td>605.68 (+15.89%)</td><td>752.70 <b>(+65.87%)</b></td><td>342.20 (+1.39%)</td><td>213.00 (+19.15%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>3.11 (n/a)</td><td>2.19 (n/a)</td><td>2.31 (n/a)</td><td>1.32 (n/a)</td><td>0.68 (n/a)</td><td>796.60 (n/a)</td><td>522.64 (n/a)</td><td>453.80 (n/a)</td><td>337.50 (n/a)</td><td>178.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:38:33</td><td>1.96 (+12.60%)</td><td>1.32 (+8.72%)</td><td>1.36 <b>(+33.67%)</b></td><td>0.81 (-9.27%)</td><td>0.42 (+14.70%)</td><td>648.50 (+10.21%)</td><td>430.84 (-6.49%)</td><td>386.80 <b>(-25.18%)</b></td><td>267.80 (-11.18%)</td><td>141.82 (+13.72%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:47:07</td><td>1.74 (n/a)</td><td>1.22 (n/a)</td><td>1.01 (n/a)</td><td>0.89 (n/a)</td><td>0.37 (n/a)</td><td>588.40 (n/a)</td><td>460.76 (n/a)</td><td>517.00 (n/a)</td><td>301.50 (n/a)</td><td>124.72 (n/a)</td>
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
