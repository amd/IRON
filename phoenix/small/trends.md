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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 <b>(-31.08%)</b></td><td>0.03 (-15.46%)</td><td>0.04 (-16.35%)</td><td>0.02 (+7.38%)</td><td>0.01 <b>(-44.24%)</b></td><td>545.70 (-6.88%)</td><td>385.00 (+4.23%)</td><td>296.70 (+19.54%)</td><td>276.30 <b>(+45.12%)</b></td><td>133.93 <b>(-31.44%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>586.00 (n/a)</td><td>369.36 (n/a)</td><td>248.20 (n/a)</td><td>190.40 (n/a)</td><td>195.34 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.05 (+0.15%)</td><td>0.04 (+11.56%)</td><td>0.05 (+9.14%)</td><td>0.02 <b>(+84.74%)</b></td><td>0.01 <b>(-22.34%)</b></td><td>554.10 <b>(-45.87%)</b></td><td>318.72 <b>(-25.52%)</b></td><td>272.70 (-8.37%)</td><td>229.50 (-0.13%)</td><td>133.45 <b>(-60.11%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1023.70 (n/a)</td><td>427.92 (n/a)</td><td>297.60 (n/a)</td><td>229.80 (n/a)</td><td>334.57 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.05 (-10.58%)</td><td>0.03 <b>(-24.47%)</b></td><td>0.03 <b>(-39.31%)</b></td><td>0.02 (-16.12%)</td><td>0.01 (+0.08%)</td><td>585.20 (+19.23%)</td><td>406.94 <b>(+35.24%)</b></td><td>442.60 <b>(+64.78%)</b></td><td>251.50 (+11.83%)</td><td>139.86 <b>(+26.81%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>490.80 (n/a)</td><td>300.90 (n/a)</td><td>268.60 (n/a)</td><td>224.90 (n/a)</td><td>110.30 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 <b>(+54.02%)</b></td><td>0.02 (+16.04%)</td><td>0.02 (+5.58%)</td><td>0.01 <b>(-35.01%)</b></td><td>0.01 <b>(+201.41%)</b></td><td>584.90 <b>(+53.88%)</b></td><td>311.60 (+0.32%)</td><td>283.80 (-5.31%)</td><td>160.30 <b>(-35.05%)</b></td><td>161.00 <b>(+216.83%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>380.10 (n/a)</td><td>310.62 (n/a)</td><td>299.70 (n/a)</td><td>246.80 (n/a)</td><td>50.82 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (-1.77%)</td><td>0.02 (-5.99%)</td><td>0.02 (+5.53%)</td><td>0.01 <b>(-39.20%)</b></td><td>0.01 <b>(+42.38%)</b></td><td>703.40 <b>(+64.46%)</b></td><td>361.08 (+19.52%)</td><td>267.40 (-5.24%)</td><td>230.90 (+1.81%)</td><td>198.49 <b>(+142.82%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>427.70 (n/a)</td><td>302.12 (n/a)</td><td>282.20 (n/a)</td><td>226.80 (n/a)</td><td>81.74 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (+13.95%)</td><td>0.02 <b>(+39.25%)</b></td><td>0.02 <b>(+104.99%)</b></td><td>0.01 <b>(+28.28%)</b></td><td>0.01 (-18.09%)</td><td>462.90 <b>(-22.04%)</b></td><td>285.60 <b>(-33.54%)</b></td><td>241.80 <b>(-51.22%)</b></td><td>206.60 (-12.23%)</td><td>102.61 <b>(-40.11%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.80 (n/a)</td><td>429.74 (n/a)</td><td>495.70 (n/a)</td><td>235.40 (n/a)</td><td>171.33 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (-10.53%)</td><td>0.01 (-10.06%)</td><td>0.01 <b>(-23.77%)</b></td><td>0.00 (+5.24%)</td><td>0.01 (-15.79%)</td><td>1901.50 (-4.98%)</td><td>740.00 (+1.02%)</td><td>533.10 <b>(+31.21%)</b></td><td>274.00 (+11.79%)</td><td>658.38 (-8.89%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2001.10 (n/a)</td><td>732.56 (n/a)</td><td>406.30 (n/a)</td><td>245.10 (n/a)</td><td>722.63 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 <b>(+31.17%)</b></td><td>0.01 (+13.27%)</td><td>0.02 (+7.56%)</td><td>0.01 (-4.86%)</td><td>0.01 <b>(+81.47%)</b></td><td>605.80 (+5.12%)</td><td>410.34 (-3.39%)</td><td>332.00 (-7.03%)</td><td>243.70 <b>(-23.77%)</b></td><td>176.81 <b>(+53.21%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.30 (n/a)</td><td>424.76 (n/a)</td><td>357.10 (n/a)</td><td>319.70 (n/a)</td><td>115.40 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (-4.49%)</td><td>0.01 (+8.96%)</td><td>0.01 (-2.47%)</td><td>0.01 (-11.93%)</td><td>0.00 (+9.05%)</td><td>753.50 (+13.55%)</td><td>473.96 (-5.60%)</td><td>488.00 (+2.54%)</td><td>305.90 (+4.72%)</td><td>181.14 <b>(+26.13%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>663.60 (n/a)</td><td>502.08 (n/a)</td><td>475.90 (n/a)</td><td>292.10 (n/a)</td><td>143.61 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.80 (n/a)</td><td>293.48 (n/a)</td><td>241.20 (n/a)</td><td>211.20 (n/a)</td><td>128.64 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>475.30 (n/a)</td><td>271.18 (n/a)</td><td>250.40 (n/a)</td><td>164.30 (n/a)</td><td>119.97 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>591.10 (n/a)</td><td>368.22 (n/a)</td><td>286.80 (n/a)</td><td>230.00 (n/a)</td><td>155.03 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>567.60 (n/a)</td><td>459.08 (n/a)</td><td>441.60 (n/a)</td><td>329.10 (n/a)</td><td>90.77 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>664.70 (n/a)</td><td>352.06 (n/a)</td><td>294.20 (n/a)</td><td>213.50 (n/a)</td><td>181.51 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>594.20 (n/a)</td><td>388.86 (n/a)</td><td>317.10 (n/a)</td><td>248.50 (n/a)</td><td>155.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.80 (n/a)</td><td>394.30 (n/a)</td><td>408.40 (n/a)</td><td>260.10 (n/a)</td><td>115.30 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.70 (n/a)</td><td>381.56 (n/a)</td><td>378.40 (n/a)</td><td>197.60 (n/a)</td><td>119.48 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.80 (n/a)</td><td>420.54 (n/a)</td><td>415.50 (n/a)</td><td>220.60 (n/a)</td><td>182.30 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.60 (n/a)</td><td>413.34 (n/a)</td><td>425.40 (n/a)</td><td>283.10 (n/a)</td><td>115.82 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.40 (n/a)</td><td>477.44 (n/a)</td><td>420.10 (n/a)</td><td>368.20 (n/a)</td><td>111.48 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>530.10 (n/a)</td><td>462.66 (n/a)</td><td>456.40 (n/a)</td><td>428.70 (n/a)</td><td>40.90 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.57 (-8.36%)</td><td>0.42 (-13.93%)</td><td>0.46 (-15.27%)</td><td>0.11 <b>(-63.54%)</b></td><td>0.18 <b>(+42.79%)</b></td><td>1998.00 <b>(+174.26%)</b></td><td>760.20 <b>(+56.90%)</b></td><td>476.50 (+18.00%)</td><td>387.40 (+9.13%)</td><td>693.86 <b>(+358.02%)</b></td><td>24.36 (-8.36%)</td><td>17.91 (-13.93%)</td><td>19.80 (-15.27%)</td><td>4.72 <b>(-63.54%)</b></td><td>7.76 <b>(+42.79%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.62 (n/a)</td><td>0.49 (n/a)</td><td>0.55 (n/a)</td><td>0.30 (n/a)</td><td>0.13 (n/a)</td><td>728.50 (n/a)</td><td>484.52 (n/a)</td><td>403.80 (n/a)</td><td>355.00 (n/a)</td><td>151.49 (n/a)</td><td>26.58 (n/a)</td><td>20.81 (n/a)</td><td>23.37 (n/a)</td><td>12.95 (n/a)</td><td>5.43 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.55 (-8.78%)</td><td>0.42 (-16.73%)</td><td>0.38 <b>(-27.13%)</b></td><td>0.34 (+2.81%)</td><td>0.08 <b>(-20.87%)</b></td><td>641.10 (-2.75%)</td><td>543.98 (+18.35%)</td><td>577.60 <b>(+37.23%)</b></td><td>405.10 (+9.60%)</td><td>98.31 (-16.72%)</td><td>23.30 (-8.78%)</td><td>17.86 (-16.73%)</td><td>16.34 <b>(-27.13%)</b></td><td>14.72 (+2.81%)</td><td>3.57 <b>(-20.87%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.60 (n/a)</td><td>0.50 (n/a)</td><td>0.53 (n/a)</td><td>0.34 (n/a)</td><td>0.11 (n/a)</td><td>659.20 (n/a)</td><td>459.64 (n/a)</td><td>420.90 (n/a)</td><td>369.60 (n/a)</td><td>118.05 (n/a)</td><td>25.54 (n/a)</td><td>21.45 (n/a)</td><td>22.42 (n/a)</td><td>14.32 (n/a)</td><td>4.51 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.31 (-0.49%)</td><td>0.30 (+0.24%)</td><td>0.30 (-2.22%)</td><td>0.30 (+4.51%)</td><td>0.00 <b>(-65.12%)</b></td><td>83824.40 (-4.32%)</td><td>83187.78 (-0.32%)</td><td>83620.70 (+2.27%)</td><td>81415.80 (+0.49%)</td><td>1001.00 <b>(-66.42%)</b></td><td>211.01 (-0.49%)</td><td>206.54 (+0.24%)</td><td>205.45 (-2.22%)</td><td>204.95 (+4.51%)</td><td>2.52 <b>(-65.12%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>87605.70 (n/a)</td><td>83459.02 (n/a)</td><td>81764.40 (n/a)</td><td>81020.00 (n/a)</td><td>2981.19 (n/a)</td><td>212.04 (n/a)</td><td>206.05 (n/a)</td><td>210.11 (n/a)</td><td>196.10 (n/a)</td><td>7.24 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>1.03 (+0.35%)</td><td>1.00 (-0.10%)</td><td>1.00 (+0.65%)</td><td>0.98 (-0.75%)</td><td>0.02 <b>(+29.07%)</b></td><td>25766.20 (+0.76%)</td><td>25147.12 (+0.12%)</td><td>25232.00 (-0.65%)</td><td>24433.20 (-0.35%)</td><td>614.87 <b>(+29.80%)</b></td><td>703.14 (+0.35%)</td><td>683.50 (-0.10%)</td><td>680.88 (+0.65%)</td><td>666.76 (-0.75%)</td><td>16.77 <b>(+29.07%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>0.99 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25572.30 (n/a)</td><td>25116.78 (n/a)</td><td>25396.60 (n/a)</td><td>24518.40 (n/a)</td><td>473.69 (n/a)</td><td>700.69 (n/a)</td><td>684.20 (n/a)</td><td>676.46 (n/a)</td><td>671.82 (n/a)</td><td>12.99 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>3.74 (+9.16%)</td><td>2.82 <b>(+20.89%)</b></td><td>2.77 <b>(+26.78%)</b></td><td>1.83 (+17.91%)</td><td>0.79 (+4.44%)</td><td>4415.40 (-15.19%)</td><td>3056.70 (-18.31%)</td><td>2911.30 <b>(-21.12%)</b></td><td>2155.40 (-8.39%)</td><td>918.47 (-19.99%)</td><td>980.78 (+9.16%)</td><td>740.27 <b>(+20.89%)</b></td><td>726.11 <b>(+26.78%)</b></td><td>478.76 (+17.91%)</td><td>206.85 (+4.44%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>3.43 (n/a)</td><td>2.33 (n/a)</td><td>2.18 (n/a)</td><td>1.55 (n/a)</td><td>0.76 (n/a)</td><td>5206.40 (n/a)</td><td>3741.82 (n/a)</td><td>3690.90 (n/a)</td><td>2352.90 (n/a)</td><td>1147.93 (n/a)</td><td>898.45 (n/a)</td><td>612.34 (n/a)</td><td>572.74 (n/a)</td><td>406.02 (n/a)</td><td>198.06 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.30 <b>(+42.10%)</b></td><td>0.23 (+16.64%)</td><td>0.20 (+0.46%)</td><td>0.19 (+12.57%)</td><td>0.05 <b>(+161.15%)</b></td><td>6627.40 (-11.17%)</td><td>5621.64 (-11.91%)</td><td>6251.50 (-0.45%)</td><td>4087.60 <b>(-29.62%)</b></td><td>1112.25 <b>(+65.15%)</b></td><td>16.42 <b>(+42.10%)</b></td><td>12.37 (+16.64%)</td><td>10.73 (+0.46%)</td><td>10.13 (+12.57%)</td><td>2.73 <b>(+161.16%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>7460.70 (n/a)</td><td>6382.00 (n/a)</td><td>6280.00 (n/a)</td><td>5808.30 (n/a)</td><td>673.48 (n/a)</td><td>11.55 (n/a)</td><td>10.60 (n/a)</td><td>10.69 (n/a)</td><td>9.00 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>3.94 (n/a)</td><td>3.81 (n/a)</td><td>3.77 (n/a)</td><td>3.75 (n/a)</td><td>0.08 (n/a)</td><td>3.93 (n/a)</td><td>3.81 (n/a)</td><td>3.77 (n/a)</td><td>3.75 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>6.98 (-6.32%)</td><td>6.45 (-8.55%)</td><td>6.82 (-3.79%)</td><td>5.78 (-10.63%)</td><td>0.59 <b>(+61.63%)</b></td><td>6.98 (-6.32%)</td><td>6.44 (-8.55%)</td><td>6.82 (-3.79%)</td><td>5.78 (-10.63%)</td><td>0.59 <b>(+61.63%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>7.45 (n/a)</td><td>7.05 (n/a)</td><td>7.09 (n/a)</td><td>6.47 (n/a)</td><td>0.36 (n/a)</td><td>7.45 (n/a)</td><td>7.05 (n/a)</td><td>7.08 (n/a)</td><td>6.46 (n/a)</td><td>0.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>13.70 (+6.02%)</td><td>10.36 (+11.15%)</td><td>8.51 (-0.06%)</td><td>7.85 (+6.00%)</td><td>2.98 <b>(+36.13%)</b></td><td>13.70 (+6.02%)</td><td>10.35 (+11.15%)</td><td>8.50 (-0.06%)</td><td>7.85 (+6.00%)</td><td>2.98 <b>(+36.13%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>12.93 (n/a)</td><td>9.32 (n/a)</td><td>8.51 (n/a)</td><td>7.41 (n/a)</td><td>2.19 (n/a)</td><td>12.92 (n/a)</td><td>9.31 (n/a)</td><td>8.51 (n/a)</td><td>7.40 (n/a)</td><td>2.19 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>3.80 (n/a)</td><td>3.65 (n/a)</td><td>3.65 (n/a)</td><td>3.38 (n/a)</td><td>0.17 (n/a)</td><td>3.80 (n/a)</td><td>3.65 (n/a)</td><td>3.65 (n/a)</td><td>3.38 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>6.97 (-8.45%)</td><td>6.46 (-5.55%)</td><td>6.64 (-3.69%)</td><td>5.75 (-5.70%)</td><td>0.57 (+1.47%)</td><td>6.97 (-8.45%)</td><td>6.46 (-5.55%)</td><td>6.63 (-3.69%)</td><td>5.75 (-5.70%)</td><td>0.57 (+1.47%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>7.62 (n/a)</td><td>6.84 (n/a)</td><td>6.89 (n/a)</td><td>6.10 (n/a)</td><td>0.56 (n/a)</td><td>7.61 (n/a)</td><td>6.84 (n/a)</td><td>6.89 (n/a)</td><td>6.09 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>10.11 <b>(-26.94%)</b></td><td>7.73 <b>(-33.47%)</b></td><td>7.02 <b>(-46.78%)</b></td><td>7.00 (-12.81%)</td><td>1.35 <b>(-48.38%)</b></td><td>10.10 <b>(-26.94%)</b></td><td>7.72 <b>(-33.47%)</b></td><td>7.02 <b>(-46.78%)</b></td><td>6.99 (-12.81%)</td><td>1.35 <b>(-48.38%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>13.84 (n/a)</td><td>11.61 (n/a)</td><td>13.19 (n/a)</td><td>8.03 (n/a)</td><td>2.61 (n/a)</td><td>13.83 (n/a)</td><td>11.60 (n/a)</td><td>13.18 (n/a)</td><td>8.02 (n/a)</td><td>2.61 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>2.80 (-9.30%)</td><td>1.95 (-15.25%)</td><td>2.10 <b>(-27.91%)</b></td><td>1.01 (-7.10%)</td><td>0.89 (-5.55%)</td><td>2.79 (-9.30%)</td><td>1.94 (-15.25%)</td><td>2.10 <b>(-27.91%)</b></td><td>1.01 (-7.10%)</td><td>0.89 (-5.55%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>3.09 (n/a)</td><td>2.30 (n/a)</td><td>2.92 (n/a)</td><td>1.09 (n/a)</td><td>0.94 (n/a)</td><td>3.08 (n/a)</td><td>2.29 (n/a)</td><td>2.91 (n/a)</td><td>1.08 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.57 (+10.91%)</td><td>0.42 <b>(+86.85%)</b></td><td>0.52 <b>(+576.98%)</b></td><td>0.07 (+0.60%)</td><td>0.20 (-1.59%)</td><td>0.56 (+10.91%)</td><td>0.41 <b>(+86.85%)</b></td><td>0.51 <b>(+576.98%)</b></td><td>0.07 (+0.60%)</td><td>0.20 (-1.59%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.51 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.21 (n/a)</td><td>0.51 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.69 (-3.02%)</td><td>0.61 <b>(+39.40%)</b></td><td>0.67 <b>(+41.91%)</b></td><td>0.40 <b>(+421.71%)</b></td><td>0.12 <b>(-53.08%)</b></td><td>0.68 (-3.02%)</td><td>0.60 <b>(+39.40%)</b></td><td>0.66 <b>(+41.91%)</b></td><td>0.40 <b>(+421.71%)</b></td><td>0.12 <b>(-53.08%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.71 (n/a)</td><td>0.44 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>0.26 (n/a)</td><td>0.70 (n/a)</td><td>0.43 (n/a)</td><td>0.47 (n/a)</td><td>0.08 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>2.51 (+5.35%)</td><td>1.17 (-12.80%)</td><td>0.64 <b>(-57.89%)</b></td><td>0.44 (-3.29%)</td><td>0.94 (+10.13%)</td><td>2.47 (+5.35%)</td><td>1.15 (-12.80%)</td><td>0.63 <b>(-57.89%)</b></td><td>0.43 (-3.29%)</td><td>0.93 (+10.13%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>2.38 (n/a)</td><td>1.34 (n/a)</td><td>1.52 (n/a)</td><td>0.46 (n/a)</td><td>0.86 (n/a)</td><td>2.34 (n/a)</td><td>1.32 (n/a)</td><td>1.50 (n/a)</td><td>0.45 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.90 (n/a)</td><td>402.64 (n/a)</td><td>483.90 (n/a)</td><td>225.40 (n/a)</td><td>143.40 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.00 (n/a)</td><td>351.72 (n/a)</td><td>301.80 (n/a)</td><td>250.00 (n/a)</td><td>108.61 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>646.70 (n/a)</td><td>440.56 (n/a)</td><td>474.40 (n/a)</td><td>266.70 (n/a)</td><td>149.58 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.80 (n/a)</td><td>403.70 (n/a)</td><td>464.30 (n/a)</td><td>237.30 (n/a)</td><td>127.74 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.60 (n/a)</td><td>433.16 (n/a)</td><td>440.30 (n/a)</td><td>269.40 (n/a)</td><td>104.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2444.20 (n/a)</td><td>864.00 (n/a)</td><td>466.30 (n/a)</td><td>317.30 (n/a)</td><td>891.23 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (-8.71%)</td><td>0.03 <b>(+26.05%)</b></td><td>0.03 <b>(+78.60%)</b></td><td>0.02 <b>(+30.52%)</b></td><td>0.01 <b>(-36.54%)</b></td><td>408.20 <b>(-23.39%)</b></td><td>297.62 <b>(-26.60%)</b></td><td>265.20 <b>(-44.02%)</b></td><td>243.00 (+9.56%)</td><td>70.87 <b>(-48.87%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>532.80 (n/a)</td><td>405.50 (n/a)</td><td>473.70 (n/a)</td><td>221.80 (n/a)</td><td>138.61 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (+12.79%)</td><td>0.03 (+13.62%)</td><td>0.03 <b>(+51.45%)</b></td><td>0.02 (-3.05%)</td><td>0.01 (+11.30%)</td><td>534.50 (+3.15%)</td><td>343.36 (-10.70%)</td><td>280.60 <b>(-33.98%)</b></td><td>238.80 (-11.36%)</td><td>121.57 (+10.20%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.20 (n/a)</td><td>384.52 (n/a)</td><td>425.00 (n/a)</td><td>269.40 (n/a)</td><td>110.32 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (-14.33%)</td><td>0.03 (+15.88%)</td><td>0.03 <b>(+64.41%)</b></td><td>0.02 (-5.00%)</td><td>0.01 <b>(-30.12%)</b></td><td>520.10 (+5.26%)</td><td>334.46 (-16.69%)</td><td>293.70 <b>(-39.17%)</b></td><td>271.10 (+16.70%)</td><td>104.25 (-13.94%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.10 (n/a)</td><td>401.46 (n/a)</td><td>482.80 (n/a)</td><td>232.30 (n/a)</td><td>121.14 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (-4.47%)</td><td>0.03 (+1.70%)</td><td>0.03 (+16.12%)</td><td>0.01 <b>(-21.48%)</b></td><td>0.01 (+12.08%)</td><td>592.20 <b>(+27.35%)</b></td><td>351.88 (+2.56%)</td><td>265.20 (-13.87%)</td><td>237.70 (+4.67%)</td><td>152.82 <b>(+38.27%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>465.00 (n/a)</td><td>343.10 (n/a)</td><td>307.90 (n/a)</td><td>227.10 (n/a)</td><td>110.52 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (-16.22%)</td><td>0.03 (+17.51%)</td><td>0.03 <b>(+70.90%)</b></td><td>0.02 <b>(+51.77%)</b></td><td>0.01 <b>(-45.39%)</b></td><td>419.40 <b>(-34.11%)</b></td><td>313.94 <b>(-25.24%)</b></td><td>279.10 <b>(-41.49%)</b></td><td>232.00 (+19.34%)</td><td>78.97 <b>(-55.01%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.50 (n/a)</td><td>419.92 (n/a)</td><td>477.00 (n/a)</td><td>194.40 (n/a)</td><td>175.54 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (+0.71%)</td><td>0.02 (+10.91%)</td><td>0.02 <b>(+22.28%)</b></td><td>0.01 (+4.01%)</td><td>0.01 (-2.83%)</td><td>646.30 (-3.85%)</td><td>393.12 (-11.68%)</td><td>409.40 (-18.23%)</td><td>234.50 (-0.72%)</td><td>167.91 (-9.36%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>672.20 (n/a)</td><td>445.12 (n/a)</td><td>500.70 (n/a)</td><td>236.20 (n/a)</td><td>185.26 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (+12.06%)</td><td>0.03 <b>(+25.65%)</b></td><td>0.03 <b>(+25.61%)</b></td><td>0.02 <b>(+26.16%)</b></td><td>0.01 (-12.70%)</td><td>435.40 <b>(-20.74%)</b></td><td>303.02 <b>(-22.96%)</b></td><td>288.40 <b>(-20.38%)</b></td><td>235.70 (-10.75%)</td><td>77.24 <b>(-36.19%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.30 (n/a)</td><td>393.32 (n/a)</td><td>362.20 (n/a)</td><td>264.10 (n/a)</td><td>121.04 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 <b>(-40.61%)</b></td><td>0.02 (-7.62%)</td><td>0.02 (+14.38%)</td><td>0.01 <b>(+20.78%)</b></td><td>0.00 <b>(-70.71%)</b></td><td>651.90 (-17.20%)</td><td>524.64 (-5.81%)</td><td>527.10 (-12.56%)</td><td>418.30 <b>(+68.40%)</b></td><td>88.87 <b>(-57.02%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>787.30 (n/a)</td><td>556.98 (n/a)</td><td>602.80 (n/a)</td><td>248.40 (n/a)</td><td>206.79 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (-7.70%)</td><td>0.03 (-0.58%)</td><td>0.03 (-15.52%)</td><td>0.01 (+6.72%)</td><td>0.01 <b>(-31.28%)</b></td><td>564.10 (-6.30%)</td><td>331.30 (-6.17%)</td><td>285.30 (+18.38%)</td><td>251.80 (+8.35%)</td><td>131.18 <b>(-22.15%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.00 (n/a)</td><td>353.10 (n/a)</td><td>241.00 (n/a)</td><td>232.40 (n/a)</td><td>168.50 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (+6.09%)</td><td>0.02 (-4.78%)</td><td>0.02 <b>(-30.95%)</b></td><td>0.01 <b>(+20.69%)</b></td><td>0.01 (-5.20%)</td><td>557.10 (-17.15%)</td><td>384.08 (+0.27%)</td><td>420.90 <b>(+44.84%)</b></td><td>219.90 (-5.74%)</td><td>142.51 <b>(-25.31%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>672.40 (n/a)</td><td>383.04 (n/a)</td><td>290.60 (n/a)</td><td>233.30 (n/a)</td><td>190.79 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (-16.83%)</td><td>0.02 <b>(-26.45%)</b></td><td>0.02 <b>(-44.09%)</b></td><td>0.01 (-8.47%)</td><td>0.01 (-14.75%)</td><td>616.80 (+9.26%)</td><td>434.86 <b>(+34.62%)</b></td><td>451.90 <b>(+78.83%)</b></td><td>283.70 <b>(+20.26%)</b></td><td>147.13 (+5.38%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.50 (n/a)</td><td>323.02 (n/a)</td><td>252.70 (n/a)</td><td>235.90 (n/a)</td><td>139.62 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 <b>(-27.91%)</b></td><td>0.03 (-19.20%)</td><td>0.03 <b>(-20.75%)</b></td><td>0.02 (+6.87%)</td><td>0.01 <b>(-29.68%)</b></td><td>466.60 (-6.42%)</td><td>341.14 (+18.86%)</td><td>313.50 <b>(+26.21%)</b></td><td>226.70 <b>(+38.74%)</b></td><td>112.85 (-10.49%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.60 (n/a)</td><td>287.02 (n/a)</td><td>248.40 (n/a)</td><td>163.40 (n/a)</td><td>126.06 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 <b>(+28.65%)</b></td><td>0.02 (-7.17%)</td><td>0.02 <b>(-42.75%)</b></td><td>0.02 (-2.06%)</td><td>0.01 <b>(+35.76%)</b></td><td>501.30 (+2.10%)</td><td>382.58 (+12.21%)</td><td>451.10 <b>(+74.71%)</b></td><td>188.10 <b>(-22.27%)</b></td><td>135.41 (+9.17%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>491.00 (n/a)</td><td>340.96 (n/a)</td><td>258.20 (n/a)</td><td>242.00 (n/a)</td><td>124.03 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (+3.19%)</td><td>0.02 (+3.00%)</td><td>0.02 (+14.19%)</td><td>0.00 (+15.72%)</td><td>0.01 (-1.10%)</td><td>1816.80 (-13.58%)</td><td>732.64 (-9.24%)</td><td>537.70 (-12.43%)</td><td>250.90 (-3.09%)</td><td>618.72 (-16.42%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2102.40 (n/a)</td><td>807.24 (n/a)</td><td>614.00 (n/a)</td><td>258.90 (n/a)</td><td>740.24 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.10 (+12.69%)</td><td>0.08 (+6.07%)</td><td>0.09 (+12.18%)</td><td>0.01 <b>(-69.72%)</b></td><td>0.04 <b>(+94.81%)</b></td><td>1903.00 <b>(+230.27%)</b></td><td>595.74 <b>(+62.26%)</b></td><td>274.70 (-10.84%)</td><td>247.20 (-11.24%)</td><td>731.12 <b>(+493.79%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>576.20 (n/a)</td><td>367.16 (n/a)</td><td>308.10 (n/a)</td><td>278.50 (n/a)</td><td>123.13 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.18 <b>(+21.83%)</b></td><td>0.15 <b>(+30.02%)</b></td><td>0.16 <b>(+34.68%)</b></td><td>0.10 <b>(+26.34%)</b></td><td>0.03 (+14.88%)</td><td>412.80 <b>(-20.84%)</b></td><td>280.04 <b>(-23.50%)</b></td><td>250.00 <b>(-25.75%)</b></td><td>230.70 (-17.90%)</td><td>75.80 <b>(-22.97%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>521.50 (n/a)</td><td>366.06 (n/a)</td><td>336.70 (n/a)</td><td>281.00 (n/a)</td><td>98.40 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (+14.17%)</td><td>0.02 (+9.60%)</td><td>0.02 <b>(+21.99%)</b></td><td>0.01 <b>(-28.50%)</b></td><td>0.01 <b>(+76.17%)</b></td><td>627.20 <b>(+39.88%)</b></td><td>321.36 (+1.40%)</td><td>247.40 (-18.03%)</td><td>227.30 (-12.41%)</td><td>171.41 <b>(+123.77%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>448.40 (n/a)</td><td>316.92 (n/a)</td><td>301.80 (n/a)</td><td>259.50 (n/a)</td><td>76.60 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.05 <b>(+26.65%)</b></td><td>0.03 (+15.62%)</td><td>0.03 <b>(+36.27%)</b></td><td>0.02 (-6.84%)</td><td>0.01 (+9.32%)</td><td>541.30 (+7.34%)</td><td>322.08 (-13.69%)</td><td>303.20 <b>(-26.62%)</b></td><td>177.50 <b>(-21.08%)</b></td><td>133.49 (-2.80%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.30 (n/a)</td><td>373.18 (n/a)</td><td>413.20 (n/a)</td><td>224.90 (n/a)</td><td>137.33 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.06 (-5.96%)</td><td>0.04 (+15.06%)</td><td>0.03 (+10.91%)</td><td>0.03 <b>(+47.40%)</b></td><td>0.01 (-18.15%)</td><td>465.30 <b>(-32.16%)</b></td><td>362.84 (-19.02%)</td><td>409.90 (-9.83%)</td><td>212.20 (+6.37%)</td><td>115.93 <b>(-35.30%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>685.90 (n/a)</td><td>448.06 (n/a)</td><td>454.60 (n/a)</td><td>199.50 (n/a)</td><td>179.17 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (-3.89%)</td><td>0.02 (-18.79%)</td><td>0.02 <b>(-20.35%)</b></td><td>0.01 (-15.10%)</td><td>0.01 (-0.80%)</td><td>566.10 (+17.79%)</td><td>444.26 <b>(+25.42%)</b></td><td>496.20 <b>(+25.56%)</b></td><td>246.40 (+4.05%)</td><td>133.79 <b>(+27.29%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>480.60 (n/a)</td><td>354.22 (n/a)</td><td>395.20 (n/a)</td><td>236.80 (n/a)</td><td>105.11 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.07 <b>(+52.99%)</b></td><td>0.03 (-3.41%)</td><td>0.02 <b>(-38.81%)</b></td><td>0.02 <b>(-25.45%)</b></td><td>0.02 <b>(+133.41%)</b></td><td>622.60 <b>(+34.15%)</b></td><td>399.74 <b>(+25.89%)</b></td><td>464.60 <b>(+63.42%)</b></td><td>153.20 <b>(-34.64%)</b></td><td>191.53 <b>(+102.09%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>464.10 (n/a)</td><td>317.54 (n/a)</td><td>284.30 (n/a)</td><td>234.40 (n/a)</td><td>94.77 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (+7.16%)</td><td>0.02 (-9.85%)</td><td>0.02 (-8.41%)</td><td>0.02 <b>(+24.58%)</b></td><td>0.01 (-13.24%)</td><td>503.80 (-19.73%)</td><td>411.28 (+4.01%)</td><td>448.30 (+9.18%)</td><td>207.50 (-6.70%)</td><td>120.09 <b>(-31.41%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.60 (n/a)</td><td>395.42 (n/a)</td><td>410.60 (n/a)</td><td>222.40 (n/a)</td><td>175.08 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 <b>(+28.16%)</b></td><td>0.03 <b>(+34.61%)</b></td><td>0.03 <b>(+44.16%)</b></td><td>0.02 <b>(+32.41%)</b></td><td>0.01 <b>(+23.79%)</b></td><td>496.60 <b>(-24.48%)</b></td><td>388.44 <b>(-25.92%)</b></td><td>377.00 <b>(-30.63%)</b></td><td>267.00 <b>(-21.98%)</b></td><td>87.46 <b>(-23.84%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>657.60 (n/a)</td><td>524.32 (n/a)</td><td>543.50 (n/a)</td><td>342.20 (n/a)</td><td>114.83 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (+9.68%)</td><td>0.02 (-13.24%)</td><td>0.02 (-8.55%)</td><td>0.00 <b>(-73.64%)</b></td><td>0.01 <b>(+48.64%)</b></td><td>1825.70 <b>(+279.41%)</b></td><td>669.68 <b>(+80.46%)</b></td><td>472.60 (+9.35%)</td><td>193.00 (-8.83%)</td><td>662.89 <b>(+431.14%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.20 (n/a)</td><td>371.10 (n/a)</td><td>432.20 (n/a)</td><td>211.70 (n/a)</td><td>124.80 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (-3.02%)</td><td>0.02 <b>(-25.21%)</b></td><td>0.02 (-2.31%)</td><td>0.00 <b>(-81.47%)</b></td><td>0.01 <b>(+37.17%)</b></td><td>2408.80 <b>(+439.73%)</b></td><td>812.58 <b>(+124.56%)</b></td><td>440.90 (+2.34%)</td><td>246.00 (+3.10%)</td><td>902.40 <b>(+747.48%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>446.30 (n/a)</td><td>361.86 (n/a)</td><td>430.80 (n/a)</td><td>238.60 (n/a)</td><td>106.48 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (+5.69%)</td><td>0.02 (-5.19%)</td><td>0.02 (-6.02%)</td><td>0.02 (-13.76%)</td><td>0.01 <b>(+23.11%)</b></td><td>535.50 (+15.96%)</td><td>440.48 (+10.00%)</td><td>470.80 (+6.40%)</td><td>215.80 (-5.39%)</td><td>129.11 <b>(+32.43%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>461.80 (n/a)</td><td>400.44 (n/a)</td><td>442.50 (n/a)</td><td>228.10 (n/a)</td><td>97.49 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (-7.28%)</td><td>0.03 (-10.81%)</td><td>0.02 <b>(-37.12%)</b></td><td>0.01 (-6.19%)</td><td>0.01 (-5.38%)</td><td>639.50 (+6.58%)</td><td>405.28 (+10.77%)</td><td>413.60 <b>(+59.02%)</b></td><td>210.40 (+7.84%)</td><td>181.58 (-0.73%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.00 (n/a)</td><td>365.88 (n/a)</td><td>260.10 (n/a)</td><td>195.10 (n/a)</td><td>182.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 <b>(+22.63%)</b></td><td>0.02 (+12.07%)</td><td>0.02 (+0.55%)</td><td>0.02 (+11.71%)</td><td>0.01 <b>(+32.97%)</b></td><td>486.10 (-10.48%)</td><td>375.64 (-9.72%)</td><td>368.00 (-0.57%)</td><td>248.40 (-18.45%)</td><td>96.96 (-4.54%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>543.00 (n/a)</td><td>416.08 (n/a)</td><td>370.10 (n/a)</td><td>304.60 (n/a)</td><td>101.58 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.38 (+15.07%)</td><td>0.27 (+3.46%)</td><td>0.23 (-3.62%)</td><td>0.18 (-6.01%)</td><td>0.08 <b>(+46.08%)</b></td><td>541.40 (+6.39%)</td><td>395.74 (+0.08%)</td><td>420.90 (+3.77%)</td><td>260.50 (-13.08%)</td><td>114.86 <b>(+34.56%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>508.90 (n/a)</td><td>395.44 (n/a)</td><td>405.60 (n/a)</td><td>299.70 (n/a)</td><td>85.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.45 (+7.47%)</td><td>0.32 (+12.64%)</td><td>0.40 <b>(+28.53%)</b></td><td>0.16 (-5.44%)</td><td>0.14 <b>(+27.92%)</b></td><td>625.90 (+5.76%)</td><td>363.70 (-5.67%)</td><td>247.00 <b>(-22.20%)</b></td><td>219.60 (-6.95%)</td><td>184.78 (+19.68%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.42 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>591.80 (n/a)</td><td>385.56 (n/a)</td><td>317.50 (n/a)</td><td>236.00 (n/a)</td><td>154.39 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.49 (-0.50%)</td><td>0.28 (+9.78%)</td><td>0.21 (-0.51%)</td><td>0.16 (-2.94%)</td><td>0.14 (+7.95%)</td><td>612.10 (+3.03%)</td><td>424.26 (-4.82%)</td><td>468.80 (+0.51%)</td><td>202.50 (+0.50%)</td><td>182.84 <b>(+23.39%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.49 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>594.10 (n/a)</td><td>445.74 (n/a)</td><td>466.40 (n/a)</td><td>201.50 (n/a)</td><td>148.18 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.31 (+19.31%)</td><td>0.21 (+7.62%)</td><td>0.17 (-3.26%)</td><td>0.15 <b>(+21.47%)</b></td><td>0.07 (+12.90%)</td><td>489.50 (-17.68%)</td><td>383.10 (-7.52%)</td><td>432.50 (+3.37%)</td><td>234.40 (-16.17%)</td><td>111.68 (-16.96%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>594.60 (n/a)</td><td>414.24 (n/a)</td><td>418.40 (n/a)</td><td>279.60 (n/a)</td><td>134.50 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.26 (-6.38%)</td><td>0.20 (-12.21%)</td><td>0.25 (-0.43%)</td><td>0.11 <b>(-23.97%)</b></td><td>0.07 <b>(+33.11%)</b></td><td>668.70 <b>(+31.53%)</b></td><td>406.44 <b>(+21.56%)</b></td><td>298.20 (+0.44%)</td><td>281.90 (+6.82%)</td><td>170.65 <b>(+71.71%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>508.40 (n/a)</td><td>334.36 (n/a)</td><td>296.90 (n/a)</td><td>263.90 (n/a)</td><td>99.38 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.33 <b>(+42.40%)</b></td><td>0.17 (+9.66%)</td><td>0.12 <b>(-21.77%)</b></td><td>0.05 <b>(+77.63%)</b></td><td>0.11 <b>(+36.18%)</b></td><td>1371.40 <b>(-43.71%)</b></td><td>628.28 <b>(-22.59%)</b></td><td>593.30 <b>(+27.81%)</b></td><td>221.30 <b>(-29.77%)</b></td><td>455.95 <b>(-50.05%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>0.08 (n/a)</td><td>2436.10 (n/a)</td><td>811.64 (n/a)</td><td>464.20 (n/a)</td><td>315.10 (n/a)</td><td>912.80 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.57 <b>(+40.45%)</b></td><td>0.34 (+12.87%)</td><td>0.25 (-1.41%)</td><td>0.22 (+5.28%)</td><td>0.15 <b>(+53.11%)</b></td><td>602.40 (-5.01%)</td><td>444.46 (-6.67%)</td><td>521.70 (+1.44%)</td><td>228.50 <b>(-28.79%)</b></td><td>161.41 (+9.81%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.41 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>634.20 (n/a)</td><td>476.24 (n/a)</td><td>514.30 (n/a)</td><td>320.90 (n/a)</td><td>146.98 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.49 (-14.52%)</td><td>0.32 (-13.72%)</td><td>0.26 <b>(-27.85%)</b></td><td>0.21 (-8.26%)</td><td>0.12 <b>(-22.24%)</b></td><td>618.00 (+8.99%)</td><td>444.36 (+11.80%)</td><td>499.50 <b>(+38.60%)</b></td><td>266.50 (+16.99%)</td><td>143.68 (-8.59%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.58 (n/a)</td><td>0.38 (n/a)</td><td>0.36 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>567.00 (n/a)</td><td>397.46 (n/a)</td><td>360.40 (n/a)</td><td>227.80 (n/a)</td><td>157.18 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.46 (-10.15%)</td><td>0.32 <b>(+43.38%)</b></td><td>0.30 <b>(+82.84%)</b></td><td>0.23 <b>(+341.28%)</b></td><td>0.10 <b>(-45.59%)</b></td><td>563.60 <b>(-77.34%)</b></td><td>432.88 <b>(-57.33%)</b></td><td>440.80 <b>(-45.31%)</b></td><td>282.30 (+11.32%)</td><td>121.62 <b>(-86.14%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.52 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>0.18 (n/a)</td><td>2487.10 (n/a)</td><td>1014.44 (n/a)</td><td>806.00 (n/a)</td><td>253.60 (n/a)</td><td>877.66 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.01 (-3.49%)</td><td>0.01 (-5.62%)</td><td>0.01 (-19.51%)</td><td>0.01 (+12.13%)</td><td>0.00 (-4.91%)</td><td>527.10 (-10.81%)</td><td>383.58 (+4.14%)</td><td>402.30 <b>(+24.24%)</b></td><td>282.80 (+3.63%)</td><td>100.32 <b>(-21.07%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.00 (n/a)</td><td>368.32 (n/a)</td><td>323.80 (n/a)</td><td>272.90 (n/a)</td><td>127.10 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (-2.59%)</td><td>0.01 <b>(+20.18%)</b></td><td>0.01 <b>(+36.27%)</b></td><td>0.01 <b>(+62.47%)</b></td><td>0.00 <b>(-75.45%)</b></td><td>320.40 <b>(-38.44%)</b></td><td>300.70 <b>(-23.14%)</b></td><td>307.30 <b>(-26.61%)</b></td><td>269.60 (+2.67%)</td><td>19.06 <b>(-84.08%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.50 (n/a)</td><td>391.24 (n/a)</td><td>418.70 (n/a)</td><td>262.60 (n/a)</td><td>119.73 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.01 (-9.87%)</td><td>0.01 <b>(-27.36%)</b></td><td>0.01 <b>(-33.73%)</b></td><td>0.01 <b>(-33.35%)</b></td><td>0.00 <b>(+34.72%)</b></td><td>592.60 <b>(+50.03%)</b></td><td>435.68 <b>(+43.03%)</b></td><td>440.00 <b>(+50.89%)</b></td><td>276.70 (+10.95%)</td><td>113.36 <b>(+109.48%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>395.00 (n/a)</td><td>304.60 (n/a)</td><td>291.60 (n/a)</td><td>249.40 (n/a)</td><td>54.12 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.44 <b>(-22.23%)</b></td><td>0.34 (-18.24%)</td><td>0.32 <b>(-30.83%)</b></td><td>0.24 (+3.73%)</td><td>0.09 <b>(-42.84%)</b></td><td>556.80 (-3.60%)</td><td>412.62 (+12.88%)</td><td>418.90 <b>(+44.55%)</b></td><td>301.40 <b>(+28.58%)</b></td><td>109.14 <b>(-30.52%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.56 (n/a)</td><td>0.41 (n/a)</td><td>0.46 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>577.60 (n/a)</td><td>365.54 (n/a)</td><td>289.80 (n/a)</td><td>234.40 (n/a)</td><td>157.08 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.47 (-8.86%)</td><td>0.34 (-11.66%)</td><td>0.27 <b>(-40.78%)</b></td><td>0.25 (+7.29%)</td><td>0.11 (-14.89%)</td><td>536.90 (-6.80%)</td><td>420.24 (+9.74%)</td><td>485.80 <b>(+68.86%)</b></td><td>282.10 (+9.72%)</td><td>124.97 (-16.53%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.46 (n/a)</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>576.10 (n/a)</td><td>382.94 (n/a)</td><td>287.70 (n/a)</td><td>257.10 (n/a)</td><td>149.71 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.50 (+11.37%)</td><td>0.42 <b>(+30.38%)</b></td><td>0.43 <b>(+48.87%)</b></td><td>0.31 <b>(+52.03%)</b></td><td>0.07 <b>(-35.25%)</b></td><td>419.90 <b>(-34.23%)</b></td><td>320.00 <b>(-28.45%)</b></td><td>309.50 <b>(-32.83%)</b></td><td>265.80 (-10.20%)</td><td>61.68 <b>(-59.06%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.45 (n/a)</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>638.40 (n/a)</td><td>447.26 (n/a)</td><td>460.80 (n/a)</td><td>296.00 (n/a)</td><td>150.64 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.56 (+9.99%)</td><td>0.41 (+9.85%)</td><td>0.44 <b>(+29.94%)</b></td><td>0.29 (-4.60%)</td><td>0.11 <b>(+35.94%)</b></td><td>450.30 (+4.82%)</td><td>343.88 (-6.24%)</td><td>301.20 <b>(-23.05%)</b></td><td>235.70 (-9.07%)</td><td>97.88 <b>(+37.40%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.51 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.08 (n/a)</td><td>429.60 (n/a)</td><td>366.78 (n/a)</td><td>391.40 (n/a)</td><td>259.20 (n/a)</td><td>71.24 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.68 <b>(-20.85%)</b></td><td>0.44 (-2.06%)</td><td>0.43 (+7.47%)</td><td>0.23 (+2.69%)</td><td>0.16 <b>(-33.15%)</b></td><td>564.80 (-2.64%)</td><td>334.48 (-4.34%)</td><td>308.20 (-6.97%)</td><td>193.90 <b>(+26.32%)</b></td><td>138.44 (-9.90%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.86 (n/a)</td><td>0.45 (n/a)</td><td>0.40 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>580.10 (n/a)</td><td>349.64 (n/a)</td><td>331.30 (n/a)</td><td>153.50 (n/a)</td><td>153.65 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (+11.95%)</td><td>0.01 <b>(-22.16%)</b></td><td>0.01 <b>(-34.82%)</b></td><td>0.01 <b>(-20.47%)</b></td><td>0.00 <b>(+57.85%)</b></td><td>595.00 <b>(+25.74%)</b></td><td>442.32 <b>(+36.00%)</b></td><td>448.50 <b>(+53.44%)</b></td><td>232.80 (-10.67%)</td><td>131.75 <b>(+55.64%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>473.20 (n/a)</td><td>325.24 (n/a)</td><td>292.30 (n/a)</td><td>260.60 (n/a)</td><td>84.65 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (+1.30%)</td><td>0.01 (+18.11%)</td><td>0.01 <b>(+24.27%)</b></td><td>0.01 <b>(+55.83%)</b></td><td>0.00 <b>(-54.33%)</b></td><td>308.20 <b>(-35.83%)</b></td><td>277.90 (-19.84%)</td><td>282.30 (-19.53%)</td><td>234.70 (-1.26%)</td><td>28.20 <b>(-70.94%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>480.30 (n/a)</td><td>346.68 (n/a)</td><td>350.80 (n/a)</td><td>237.70 (n/a)</td><td>97.02 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-42.31%)</b></td><td>0.00 <b>(-66.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-9.95%)</td><td>22524.77 <b>(+34.90%)</b></td><td>16535.20 <b>(+83.08%)</b></td><td>19434.19 <b>(+169.19%)</b></td><td>7197.81 (+16.17%)</td><td>6620.94 <b>(+52.83%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>16696.79 (n/a)</td><td>9031.84 (n/a)</td><td>7219.43 (n/a)</td><td>6195.75 (n/a)</td><td>4332.25 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-40.82%)</b></td><td>0.00 <b>(-66.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-22.29%)</b></td><td>19525.87 (+3.34%)</td><td>15943.22 <b>(+56.52%)</b></td><td>18343.84 <b>(+174.30%)</b></td><td>7042.60 (+18.50%)</td><td>5184.00 (-8.65%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18894.39 (n/a)</td><td>10186.35 (n/a)</td><td>6687.49 (n/a)</td><td>5943.19 (n/a)</td><td>5674.87 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.12 <b>(-23.72%)</b></td><td>0.10 (+0.47%)</td><td>0.10 <b>(+30.86%)</b></td><td>0.08 (+11.94%)</td><td>0.02 <b>(-54.08%)</b></td><td>26960.92 (-10.60%)</td><td>21251.20 (-9.33%)</td><td>21216.20 <b>(-23.66%)</b></td><td>17028.98 <b>(+31.13%)</b></td><td>4143.98 <b>(-49.63%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>30158.41 (n/a)</td><td>23438.22 (n/a)</td><td>27792.19 (n/a)</td><td>12986.63 (n/a)</td><td>8227.36 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>1.73 <b>(+20.90%)</b></td><td>1.05 (+0.43%)</td><td>1.09 (+7.09%)</td><td>0.16 <b>(-72.44%)</b></td><td>0.59 <b>(+79.59%)</b></td><td>3258.80 <b>(+262.85%)</b></td><td>1001.38 <b>(+81.82%)</b></td><td>481.40 (-6.63%)</td><td>303.70 (-17.27%)</td><td>1266.51 <b>(+503.18%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>1.43 (n/a)</td><td>1.05 (n/a)</td><td>1.02 (n/a)</td><td>0.58 (n/a)</td><td>0.33 (n/a)</td><td>898.10 (n/a)</td><td>550.74 (n/a)</td><td>515.60 (n/a)</td><td>367.10 (n/a)</td><td>209.97 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>2.30 (-12.62%)</td><td>1.16 (+3.53%)</td><td>1.03 (-4.19%)</td><td>0.30 (+0.50%)</td><td>0.85 (-10.14%)</td><td>3480.00 (-0.50%)</td><td>1601.82 (-10.51%)</td><td>1019.00 (+4.37%)</td><td>456.50 (+14.47%)</td><td>1312.76 (-10.34%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>2.63 (n/a)</td><td>1.12 (n/a)</td><td>1.07 (n/a)</td><td>0.30 (n/a)</td><td>0.95 (n/a)</td><td>3497.40 (n/a)</td><td>1790.02 (n/a)</td><td>976.30 (n/a)</td><td>398.80 (n/a)</td><td>1464.23 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>1.43 <b>(-23.02%)</b></td><td>1.01 (-7.16%)</td><td>0.94 (+4.18%)</td><td>0.76 <b>(+252.65%)</b></td><td>0.25 <b>(-61.07%)</b></td><td>686.30 <b>(-71.65%)</b></td><td>544.26 <b>(-35.60%)</b></td><td>559.10 (-4.00%)</td><td>365.80 <b>(+29.90%)</b></td><td>114.81 <b>(-87.14%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:15:58</td><td>1.86 (n/a)</td><td>1.08 (n/a)</td><td>0.90 (n/a)</td><td>0.22 (n/a)</td><td>0.65 (n/a)</td><td>2420.40 (n/a)</td><td>845.06 (n/a)</td><td>582.40 (n/a)</td><td>281.60 (n/a)</td><td>892.49 (n/a)</td>
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
