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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.05 (+15.48%)</td><td>0.05 <b>(+41.76%)</b></td><td>0.05 (+19.70%)</td><td>0.05 <b>(+108.99%)</b></td><td>0.00 <b>(-85.58%)</b></td><td>261.10 <b>(-52.15%)</b></td><td>248.42 <b>(-35.48%)</b></td><td>247.80 (-16.48%)</td><td>239.30 (-13.39%)</td><td>7.95 <b>(-94.06%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.70 (n/a)</td><td>385.00 (n/a)</td><td>296.70 (n/a)</td><td>276.30 (n/a)</td><td>133.93 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.05 (-0.74%)</td><td>0.04 (-1.85%)</td><td>0.05 (+10.36%)</td><td>0.03 <b>(+20.95%)</b></td><td>0.01 (+4.09%)</td><td>458.10 (-17.33%)</td><td>320.54 (+0.57%)</td><td>247.10 (-9.39%)</td><td>231.20 (+0.74%)</td><td>109.01 (-18.32%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>554.10 (n/a)</td><td>318.72 (n/a)</td><td>272.70 (n/a)</td><td>229.50 (n/a)</td><td>133.45 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.05 (+6.08%)</td><td>0.04 (+19.20%)</td><td>0.04 <b>(+32.85%)</b></td><td>0.03 <b>(+25.45%)</b></td><td>0.01 (-17.06%)</td><td>466.50 <b>(-20.28%)</b></td><td>325.76 (-19.95%)</td><td>333.20 <b>(-24.72%)</b></td><td>237.10 (-5.73%)</td><td>90.21 <b>(-35.50%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>585.20 (n/a)</td><td>406.94 (n/a)</td><td>442.60 (n/a)</td><td>251.50 (n/a)</td><td>139.86 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 <b>(-28.07%)</b></td><td>0.02 (-7.65%)</td><td>0.02 (+5.57%)</td><td>0.01 (+14.20%)</td><td>0.01 <b>(-40.84%)</b></td><td>512.20 (-12.43%)</td><td>308.66 (-0.94%)</td><td>268.90 (-5.25%)</td><td>222.80 <b>(+38.99%)</b></td><td>116.57 <b>(-27.59%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.90 (n/a)</td><td>311.60 (n/a)</td><td>283.80 (n/a)</td><td>160.30 (n/a)</td><td>161.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (+0.79%)</td><td>0.01 <b>(-21.21%)</b></td><td>0.01 <b>(-43.80%)</b></td><td>0.00 <b>(-71.37%)</b></td><td>0.01 <b>(+43.92%)</b></td><td>2456.50 <b>(+249.23%)</b></td><td>796.28 <b>(+120.53%)</b></td><td>475.80 <b>(+77.94%)</b></td><td>229.10 (-0.78%)</td><td>941.34 <b>(+374.24%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>703.40 (n/a)</td><td>361.08 (n/a)</td><td>267.40 (n/a)</td><td>230.90 (n/a)</td><td>198.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (-14.27%)</td><td>0.02 (-12.89%)</td><td>0.02 (-8.36%)</td><td>0.01 (-7.26%)</td><td>0.01 (-0.55%)</td><td>499.10 (+7.82%)</td><td>331.70 (+16.14%)</td><td>263.90 (+9.14%)</td><td>241.00 (+16.65%)</td><td>117.64 (+14.64%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>462.90 (n/a)</td><td>285.60 (n/a)</td><td>241.80 (n/a)</td><td>206.60 (n/a)</td><td>102.61 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 <b>(+68.31%)</b></td><td>0.02 <b>(+55.33%)</b></td><td>0.01 <b>(+42.03%)</b></td><td>0.01 <b>(+279.90%)</b></td><td>0.01 <b>(+52.18%)</b></td><td>500.50 <b>(-73.68%)</b></td><td>371.68 <b>(-49.77%)</b></td><td>375.30 <b>(-29.60%)</b></td><td>162.80 <b>(-40.58%)</b></td><td>129.20 <b>(-80.38%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1901.50 (n/a)</td><td>740.00 (n/a)</td><td>533.10 (n/a)</td><td>274.00 (n/a)</td><td>658.38 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (+0.42%)</td><td>0.01 <b>(-24.42%)</b></td><td>0.01 <b>(-27.71%)</b></td><td>0.00 <b>(-69.72%)</b></td><td>0.01 (+18.75%)</td><td>2000.40 <b>(+230.21%)</b></td><td>759.94 <b>(+85.20%)</b></td><td>459.20 <b>(+38.31%)</b></td><td>242.70 (-0.41%)</td><td>710.33 <b>(+301.74%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.80 (n/a)</td><td>410.34 (n/a)</td><td>332.00 (n/a)</td><td>243.70 (n/a)</td><td>176.81 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (+7.91%)</td><td>0.02 <b>(+24.21%)</b></td><td>0.01 <b>(+32.47%)</b></td><td>0.01 <b>(+75.90%)</b></td><td>0.00 <b>(-34.01%)</b></td><td>428.40 <b>(-43.15%)</b></td><td>351.66 <b>(-25.80%)</b></td><td>368.30 <b>(-24.53%)</b></td><td>283.40 (-7.36%)</td><td>63.88 <b>(-64.73%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>753.50 (n/a)</td><td>473.96 (n/a)</td><td>488.00 (n/a)</td><td>305.90 (n/a)</td><td>181.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.50 (n/a)</td><td>371.14 (n/a)</td><td>425.10 (n/a)</td><td>247.10 (n/a)</td><td>112.63 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>596.30 (n/a)</td><td>425.44 (n/a)</td><td>465.00 (n/a)</td><td>257.80 (n/a)</td><td>155.43 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.30 (n/a)</td><td>445.12 (n/a)</td><td>491.30 (n/a)</td><td>272.80 (n/a)</td><td>104.54 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>474.60 (n/a)</td><td>388.66 (n/a)</td><td>422.10 (n/a)</td><td>274.60 (n/a)</td><td>94.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>525.90 (n/a)</td><td>389.96 (n/a)</td><td>452.80 (n/a)</td><td>203.10 (n/a)</td><td>140.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1897.80 (n/a)</td><td>755.80 (n/a)</td><td>479.80 (n/a)</td><td>261.90 (n/a)</td><td>656.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1850.20 (n/a)</td><td>678.12 (n/a)</td><td>429.90 (n/a)</td><td>293.00 (n/a)</td><td>659.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.80 (n/a)</td><td>476.82 (n/a)</td><td>533.50 (n/a)</td><td>303.70 (n/a)</td><td>135.50 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.00 (n/a)</td><td>338.84 (n/a)</td><td>291.90 (n/a)</td><td>198.60 (n/a)</td><td>134.86 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.80 (n/a)</td><td>403.36 (n/a)</td><td>406.20 (n/a)</td><td>252.10 (n/a)</td><td>126.18 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.50 (n/a)</td><td>434.24 (n/a)</td><td>496.60 (n/a)</td><td>263.20 (n/a)</td><td>144.06 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>534.60 (n/a)</td><td>481.88 (n/a)</td><td>505.30 (n/a)</td><td>381.10 (n/a)</td><td>65.26 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.69 <b>(+21.00%)</b></td><td>0.45 (+7.21%)</td><td>0.39 (-15.08%)</td><td>0.20 <b>(+77.51%)</b></td><td>0.20 (+8.09%)</td><td>1125.60 <b>(-43.66%)</b></td><td>595.02 <b>(-21.73%)</b></td><td>561.20 (+17.78%)</td><td>320.20 (-17.35%)</td><td>319.93 <b>(-53.89%)</b></td><td>29.48 <b>(+21.00%)</b></td><td>19.20 (+7.21%)</td><td>16.82 (-15.08%)</td><td>8.38 <b>(+77.51%)</b></td><td>8.38 (+8.09%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.57 (n/a)</td><td>0.42 (n/a)</td><td>0.46 (n/a)</td><td>0.11 (n/a)</td><td>0.18 (n/a)</td><td>1998.00 (n/a)</td><td>760.20 (n/a)</td><td>476.50 (n/a)</td><td>387.40 (n/a)</td><td>693.86 (n/a)</td><td>24.36 (n/a)</td><td>17.91 (n/a)</td><td>19.80 (n/a)</td><td>4.72 (n/a)</td><td>7.76 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.56 (+2.65%)</td><td>0.40 (-4.48%)</td><td>0.35 (-9.86%)</td><td>0.30 (-14.26%)</td><td>0.11 <b>(+37.23%)</b></td><td>747.80 (+16.64%)</td><td>587.94 (+8.08%)</td><td>640.80 (+10.94%)</td><td>394.70 (-2.57%)</td><td>152.77 <b>(+55.39%)</b></td><td>23.91 (+2.65%)</td><td>17.06 (-4.48%)</td><td>14.73 (-9.86%)</td><td>12.62 (-14.26%)</td><td>4.90 <b>(+37.23%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.55 (n/a)</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>641.10 (n/a)</td><td>543.98 (n/a)</td><td>577.60 (n/a)</td><td>405.10 (n/a)</td><td>98.31 (n/a)</td><td>23.30 (n/a)</td><td>17.86 (n/a)</td><td>16.34 (n/a)</td><td>14.72 (n/a)</td><td>3.57 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.31 (-0.34%)</td><td>0.30 (-0.82%)</td><td>0.30 (+0.49%)</td><td>0.29 (-3.85%)</td><td>0.01 <b>(+102.28%)</b></td><td>87179.40 (+4.00%)</td><td>83910.20 (+0.87%)</td><td>83210.90 (-0.49%)</td><td>81696.00 (+0.34%)</td><td>2121.70 <b>(+111.96%)</b></td><td>210.29 (-0.34%)</td><td>204.84 (-0.82%)</td><td>206.46 (+0.49%)</td><td>197.06 (-3.85%)</td><td>5.11 <b>(+102.28%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83824.40 (n/a)</td><td>83187.78 (n/a)</td><td>83620.70 (n/a)</td><td>81415.80 (n/a)</td><td>1001.00 (n/a)</td><td>211.01 (n/a)</td><td>206.54 (n/a)</td><td>205.45 (n/a)</td><td>204.95 (n/a)</td><td>2.52 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>1.04 (+0.63%)</td><td>0.96 (-3.83%)</td><td>1.01 (+1.44%)</td><td>0.78 (-19.84%)</td><td>0.10 <b>(+320.64%)</b></td><td>32143.60 <b>(+24.75%)</b></td><td>26415.86 (+5.05%)</td><td>24872.70 (-1.42%)</td><td>24279.30 (-0.63%)</td><td>3256.15 <b>(+429.57%)</b></td><td>707.59 (+0.63%)</td><td>657.31 (-3.83%)</td><td>690.71 (+1.44%)</td><td>534.47 (-19.84%)</td><td>70.53 <b>(+320.64%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>1.00 (n/a)</td><td>0.98 (n/a)</td><td>0.02 (n/a)</td><td>25766.20 (n/a)</td><td>25147.12 (n/a)</td><td>25232.00 (n/a)</td><td>24433.20 (n/a)</td><td>614.87 (n/a)</td><td>703.14 (n/a)</td><td>683.50 (n/a)</td><td>680.88 (n/a)</td><td>666.76 (n/a)</td><td>16.77 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>3.51 (-6.27%)</td><td>2.97 (+5.11%)</td><td>3.27 (+18.15%)</td><td>1.49 (-18.65%)</td><td>0.84 (+6.84%)</td><td>5427.40 <b>(+22.92%)</b></td><td>3021.88 (-1.14%)</td><td>2464.10 (-15.36%)</td><td>2299.40 (+6.68%)</td><td>1349.56 <b>(+46.94%)</b></td><td>919.32 (-6.27%)</td><td>778.11 (+5.11%)</td><td>857.89 (+18.15%)</td><td>389.50 (-18.65%)</td><td>221.00 (+6.84%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>3.74 (n/a)</td><td>2.82 (n/a)</td><td>2.77 (n/a)</td><td>1.83 (n/a)</td><td>0.79 (n/a)</td><td>4415.40 (n/a)</td><td>3056.70 (n/a)</td><td>2911.30 (n/a)</td><td>2155.40 (n/a)</td><td>918.47 (n/a)</td><td>980.78 (n/a)</td><td>740.27 (n/a)</td><td>726.11 (n/a)</td><td>478.76 (n/a)</td><td>206.85 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.20 <b>(-35.48%)</b></td><td>0.18 <b>(-20.74%)</b></td><td>0.18 (-7.66%)</td><td>0.17 (-11.68%)</td><td>0.01 <b>(-76.90%)</b></td><td>7503.70 (+13.22%)</td><td>6868.82 <b>(+22.19%)</b></td><td>6770.30 (+8.30%)</td><td>6335.30 <b>(+54.99%)</b></td><td>448.40 <b>(-59.69%)</b></td><td>10.59 <b>(-35.48%)</b></td><td>9.80 <b>(-20.74%)</b></td><td>9.91 (-7.66%)</td><td>8.94 (-11.68%)</td><td>0.63 <b>(-76.90%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>6627.40 (n/a)</td><td>5621.64 (n/a)</td><td>6251.50 (n/a)</td><td>4087.60 (n/a)</td><td>1112.25 (n/a)</td><td>16.42 (n/a)</td><td>12.37 (n/a)</td><td>10.73 (n/a)</td><td>10.13 (n/a)</td><td>2.73 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>3.88 (n/a)</td><td>3.72 (n/a)</td><td>3.74 (n/a)</td><td>3.48 (n/a)</td><td>0.15 (n/a)</td><td>3.88 (n/a)</td><td>3.72 (n/a)</td><td>3.74 (n/a)</td><td>3.48 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>7.15 (+2.34%)</td><td>6.48 (+0.54%)</td><td>6.37 (-6.60%)</td><td>6.00 (+3.84%)</td><td>0.52 (-12.20%)</td><td>7.14 (+2.34%)</td><td>6.48 (+0.54%)</td><td>6.37 (-6.60%)</td><td>6.00 (+3.84%)</td><td>0.52 (-12.20%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>6.98 (n/a)</td><td>6.45 (n/a)</td><td>6.82 (n/a)</td><td>5.78 (n/a)</td><td>0.59 (n/a)</td><td>6.98 (n/a)</td><td>6.44 (n/a)</td><td>6.82 (n/a)</td><td>5.78 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>12.73 (-7.12%)</td><td>9.37 (-9.55%)</td><td>9.59 (+12.74%)</td><td>7.26 (-7.46%)</td><td>2.23 <b>(-25.37%)</b></td><td>12.72 (-7.12%)</td><td>9.36 (-9.55%)</td><td>9.59 (+12.74%)</td><td>7.26 (-7.46%)</td><td>2.22 <b>(-25.37%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>13.70 (n/a)</td><td>10.36 (n/a)</td><td>8.51 (n/a)</td><td>7.85 (n/a)</td><td>2.98 (n/a)</td><td>13.70 (n/a)</td><td>10.35 (n/a)</td><td>8.50 (n/a)</td><td>7.85 (n/a)</td><td>2.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>3.85 (n/a)</td><td>3.65 (n/a)</td><td>3.74 (n/a)</td><td>3.14 (n/a)</td><td>0.29 (n/a)</td><td>3.85 (n/a)</td><td>3.65 (n/a)</td><td>3.74 (n/a)</td><td>3.13 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>6.98 (+0.12%)</td><td>6.49 (+0.45%)</td><td>6.73 (+1.39%)</td><td>5.91 (+2.69%)</td><td>0.52 (-9.52%)</td><td>6.98 (+0.12%)</td><td>6.49 (+0.45%)</td><td>6.72 (+1.39%)</td><td>5.90 (+2.69%)</td><td>0.51 (-9.52%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>6.97 (n/a)</td><td>6.46 (n/a)</td><td>6.64 (n/a)</td><td>5.75 (n/a)</td><td>0.57 (n/a)</td><td>6.97 (n/a)</td><td>6.46 (n/a)</td><td>6.63 (n/a)</td><td>5.75 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>13.83 <b>(+36.87%)</b></td><td>9.46 <b>(+22.51%)</b></td><td>8.60 <b>(+22.50%)</b></td><td>7.41 (+5.93%)</td><td>2.67 <b>(+97.95%)</b></td><td>13.83 <b>(+36.87%)</b></td><td>9.46 <b>(+22.51%)</b></td><td>8.60 <b>(+22.50%)</b></td><td>7.41 (+5.93%)</td><td>2.67 <b>(+97.95%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>10.11 (n/a)</td><td>7.73 (n/a)</td><td>7.02 (n/a)</td><td>7.00 (n/a)</td><td>1.35 (n/a)</td><td>10.10 (n/a)</td><td>7.72 (n/a)</td><td>7.02 (n/a)</td><td>6.99 (n/a)</td><td>1.35 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>3.02 (+7.82%)</td><td>2.32 (+19.41%)</td><td>2.75 <b>(+31.00%)</b></td><td>1.22 <b>(+20.42%)</b></td><td>0.83 (-6.16%)</td><td>3.01 (+7.82%)</td><td>2.32 (+19.41%)</td><td>2.75 <b>(+31.00%)</b></td><td>1.21 <b>(+20.42%)</b></td><td>0.83 (-6.16%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>2.80 (n/a)</td><td>1.95 (n/a)</td><td>2.10 (n/a)</td><td>1.01 (n/a)</td><td>0.89 (n/a)</td><td>2.79 (n/a)</td><td>1.94 (n/a)</td><td>2.10 (n/a)</td><td>1.01 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.54 (-5.86%)</td><td>0.29 <b>(-30.89%)</b></td><td>0.36 <b>(-29.49%)</b></td><td>0.08 (+0.08%)</td><td>0.20 (+0.43%)</td><td>0.53 (-5.86%)</td><td>0.28 <b>(-30.89%)</b></td><td>0.36 <b>(-29.49%)</b></td><td>0.07 (+0.08%)</td><td>0.20 (+0.43%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.57 (n/a)</td><td>0.42 (n/a)</td><td>0.52 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td><td>0.56 (n/a)</td><td>0.41 (n/a)</td><td>0.51 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.74 (+7.25%)</td><td>0.42 <b>(-30.44%)</b></td><td>0.36 <b>(-46.25%)</b></td><td>0.08 <b>(-80.77%)</b></td><td>0.27 <b>(+120.83%)</b></td><td>0.73 (+7.25%)</td><td>0.42 <b>(-30.44%)</b></td><td>0.36 <b>(-46.25%)</b></td><td>0.08 <b>(-80.77%)</b></td><td>0.26 <b>(+120.83%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.69 (n/a)</td><td>0.61 (n/a)</td><td>0.67 (n/a)</td><td>0.40 (n/a)</td><td>0.12 (n/a)</td><td>0.68 (n/a)</td><td>0.60 (n/a)</td><td>0.66 (n/a)</td><td>0.40 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>2.52 (+0.43%)</td><td>1.55 <b>(+32.20%)</b></td><td>1.36 <b>(+111.48%)</b></td><td>0.70 <b>(+59.31%)</b></td><td>0.75 <b>(-20.47%)</b></td><td>2.48 (+0.43%)</td><td>1.52 <b>(+32.20%)</b></td><td>1.33 <b>(+111.48%)</b></td><td>0.69 <b>(+59.31%)</b></td><td>0.74 <b>(-20.47%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>2.51 (n/a)</td><td>1.17 (n/a)</td><td>0.64 (n/a)</td><td>0.44 (n/a)</td><td>0.94 (n/a)</td><td>2.47 (n/a)</td><td>1.15 (n/a)</td><td>0.63 (n/a)</td><td>0.43 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>490.40 (n/a)</td><td>295.56 (n/a)</td><td>265.40 (n/a)</td><td>195.80 (n/a)</td><td>113.32 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>481.70 (n/a)</td><td>342.66 (n/a)</td><td>289.40 (n/a)</td><td>221.90 (n/a)</td><td>109.82 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>532.30 (n/a)</td><td>435.86 (n/a)</td><td>418.90 (n/a)</td><td>315.30 (n/a)</td><td>86.58 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2436.30 (n/a)</td><td>776.62 (n/a)</td><td>426.50 (n/a)</td><td>233.90 (n/a)</td><td>934.40 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.60 (n/a)</td><td>414.32 (n/a)</td><td>512.40 (n/a)</td><td>181.70 (n/a)</td><td>188.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>384.20 (n/a)</td><td>324.88 (n/a)</td><td>341.70 (n/a)</td><td>220.20 (n/a)</td><td>63.90 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (+3.24%)</td><td>0.03 (-3.99%)</td><td>0.03 (-2.30%)</td><td>0.02 (-17.97%)</td><td>0.01 <b>(+25.14%)</b></td><td>497.60 <b>(+21.90%)</b></td><td>320.76 (+7.78%)</td><td>271.50 (+2.38%)</td><td>235.40 (-3.13%)</td><td>107.77 <b>(+52.06%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>408.20 (n/a)</td><td>297.62 (n/a)</td><td>265.20 (n/a)</td><td>243.00 (n/a)</td><td>70.87 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (-6.49%)</td><td>0.03 (-2.52%)</td><td>0.03 (+1.21%)</td><td>0.02 (+8.25%)</td><td>0.01 (-3.57%)</td><td>493.80 (-7.61%)</td><td>350.16 (+1.98%)</td><td>277.20 (-1.21%)</td><td>255.40 (+6.95%)</td><td>114.96 (-5.44%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.50 (n/a)</td><td>343.36 (n/a)</td><td>280.60 (n/a)</td><td>238.80 (n/a)</td><td>121.57 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (+17.95%)</td><td>0.02 (-4.75%)</td><td>0.02 <b>(-25.74%)</b></td><td>0.02 (+14.40%)</td><td>0.01 <b>(+34.96%)</b></td><td>454.70 (-12.57%)</td><td>356.84 (+6.69%)</td><td>395.50 <b>(+34.66%)</b></td><td>229.90 (-15.20%)</td><td>100.30 (-3.79%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.10 (n/a)</td><td>334.46 (n/a)</td><td>293.70 (n/a)</td><td>271.10 (n/a)</td><td>104.25 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (+3.26%)</td><td>0.03 (+6.38%)</td><td>0.03 (-8.50%)</td><td>0.02 <b>(+45.00%)</b></td><td>0.01 <b>(-22.90%)</b></td><td>408.40 <b>(-31.04%)</b></td><td>307.72 (-12.55%)</td><td>289.90 (+9.31%)</td><td>230.20 (-3.16%)</td><td>79.88 <b>(-47.73%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.20 (n/a)</td><td>351.88 (n/a)</td><td>265.20 (n/a)</td><td>237.70 (n/a)</td><td>152.82 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (-9.17%)</td><td>0.03 (+3.17%)</td><td>0.03 (+3.04%)</td><td>0.02 (-0.69%)</td><td>0.01 <b>(-20.64%)</b></td><td>422.30 (+0.69%)</td><td>300.00 (-4.44%)</td><td>270.80 (-2.97%)</td><td>255.40 (+10.09%)</td><td>69.70 (-11.74%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>419.40 (n/a)</td><td>313.94 (n/a)</td><td>279.10 (n/a)</td><td>232.00 (n/a)</td><td>78.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 <b>(+20.74%)</b></td><td>0.03 (+9.52%)</td><td>0.02 (+18.31%)</td><td>0.02 <b>(+51.42%)</b></td><td>0.01 (-3.01%)</td><td>426.80 <b>(-33.96%)</b></td><td>338.00 (-14.02%)</td><td>346.10 (-15.46%)</td><td>194.20 (-17.19%)</td><td>94.97 <b>(-43.44%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>646.30 (n/a)</td><td>393.12 (n/a)</td><td>409.40 (n/a)</td><td>234.50 (n/a)</td><td>167.91 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (-3.83%)</td><td>0.02 <b>(-23.80%)</b></td><td>0.02 <b>(-44.45%)</b></td><td>0.01 <b>(-22.69%)</b></td><td>0.01 <b>(+48.50%)</b></td><td>563.20 <b>(+29.35%)</b></td><td>429.22 <b>(+41.65%)</b></td><td>519.10 <b>(+79.99%)</b></td><td>245.10 (+3.99%)</td><td>149.42 <b>(+93.44%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>435.40 (n/a)</td><td>303.02 (n/a)</td><td>288.40 (n/a)</td><td>235.70 (n/a)</td><td>77.24 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 <b>(+42.67%)</b></td><td>0.02 <b>(+24.36%)</b></td><td>0.02 (-0.93%)</td><td>0.01 (+5.71%)</td><td>0.01 <b>(+173.11%)</b></td><td>616.70 (-5.40%)</td><td>456.74 (-12.94%)</td><td>532.00 (+0.93%)</td><td>293.20 <b>(-29.91%)</b></td><td>151.51 <b>(+70.47%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>651.90 (n/a)</td><td>524.64 (n/a)</td><td>527.10 (n/a)</td><td>418.30 (n/a)</td><td>88.87 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (+1.56%)</td><td>0.02 (-15.23%)</td><td>0.03 (-5.75%)</td><td>0.00 <b>(-72.99%)</b></td><td>0.01 <b>(+60.33%)</b></td><td>2088.70 <b>(+270.27%)</b></td><td>662.56 <b>(+99.99%)</b></td><td>302.70 (+6.10%)</td><td>248.00 (-1.51%)</td><td>799.27 <b>(+509.30%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.10 (n/a)</td><td>331.30 (n/a)</td><td>285.30 (n/a)</td><td>251.80 (n/a)</td><td>131.18 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (-16.44%)</td><td>0.02 (-6.48%)</td><td>0.02 <b>(+27.35%)</b></td><td>0.01 (-3.74%)</td><td>0.01 <b>(-21.76%)</b></td><td>578.80 (+3.90%)</td><td>402.24 (+4.73%)</td><td>330.50 <b>(-21.48%)</b></td><td>263.20 (+19.69%)</td><td>148.93 (+4.51%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.10 (n/a)</td><td>384.08 (n/a)</td><td>420.90 (n/a)</td><td>219.90 (n/a)</td><td>142.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (+0.08%)</td><td>0.02 (-9.31%)</td><td>0.02 (+3.14%)</td><td>0.00 <b>(-74.62%)</b></td><td>0.01 <b>(+46.43%)</b></td><td>2430.40 <b>(+294.03%)</b></td><td>800.12 <b>(+83.99%)</b></td><td>438.20 (-3.03%)</td><td>283.50 (-0.07%)</td><td>918.85 <b>(+524.50%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.80 (n/a)</td><td>434.86 (n/a)</td><td>451.90 (n/a)</td><td>283.70 (n/a)</td><td>147.13 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (-5.01%)</td><td>0.02 (-16.77%)</td><td>0.02 <b>(-39.18%)</b></td><td>0.01 <b>(-22.45%)</b></td><td>0.01 (+18.36%)</td><td>601.70 <b>(+28.95%)</b></td><td>439.22 <b>(+28.75%)</b></td><td>515.50 <b>(+64.43%)</b></td><td>238.70 (+5.29%)</td><td>175.01 <b>(+55.09%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>466.60 (n/a)</td><td>341.14 (n/a)</td><td>313.50 (n/a)</td><td>226.70 (n/a)</td><td>112.85 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 <b>(-23.48%)</b></td><td>0.02 (-15.51%)</td><td>0.02 (-0.55%)</td><td>0.02 (-3.09%)</td><td>0.01 <b>(-38.25%)</b></td><td>517.30 (+3.19%)</td><td>422.64 (+10.47%)</td><td>453.60 (+0.55%)</td><td>245.80 <b>(+30.68%)</b></td><td>105.03 <b>(-22.44%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>501.30 (n/a)</td><td>382.58 (n/a)</td><td>451.10 (n/a)</td><td>188.10 (n/a)</td><td>135.41 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 <b>(-22.16%)</b></td><td>0.02 (+15.90%)</td><td>0.02 (+15.10%)</td><td>0.01 <b>(+230.46%)</b></td><td>0.00 <b>(-59.16%)</b></td><td>549.80 <b>(-69.74%)</b></td><td>437.98 <b>(-40.22%)</b></td><td>467.10 (-13.13%)</td><td>322.40 <b>(+28.50%)</b></td><td>88.18 <b>(-85.75%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1816.80 (n/a)</td><td>732.64 (n/a)</td><td>537.70 (n/a)</td><td>250.90 (n/a)</td><td>618.72 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.11 (+5.67%)</td><td>0.08 (+10.37%)</td><td>0.09 (-0.53%)</td><td>0.04 <b>(+221.75%)</b></td><td>0.03 <b>(-29.41%)</b></td><td>591.50 <b>(-68.92%)</b></td><td>327.88 <b>(-44.96%)</b></td><td>276.10 (+0.51%)</td><td>233.90 (-5.38%)</td><td>149.63 <b>(-79.53%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1903.00 (n/a)</td><td>595.74 (n/a)</td><td>274.70 (n/a)</td><td>247.20 (n/a)</td><td>731.12 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.16 (-7.36%)</td><td>0.14 (-9.89%)</td><td>0.14 (-13.49%)</td><td>0.08 (-16.84%)</td><td>0.03 (+4.28%)</td><td>496.40 <b>(+20.25%)</b></td><td>316.42 (+12.99%)</td><td>289.00 (+15.60%)</td><td>249.00 (+7.93%)</td><td>102.77 <b>(+35.58%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>412.80 (n/a)</td><td>280.04 (n/a)</td><td>250.00 (n/a)</td><td>230.70 (n/a)</td><td>75.80 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (-0.53%)</td><td>0.02 (-16.36%)</td><td>0.01 <b>(-31.00%)</b></td><td>0.01 (+14.65%)</td><td>0.01 (+1.02%)</td><td>547.10 (-12.77%)</td><td>375.38 (+16.81%)</td><td>358.60 <b>(+44.95%)</b></td><td>228.50 (+0.53%)</td><td>142.36 (-16.94%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.20 (n/a)</td><td>321.36 (n/a)</td><td>247.40 (n/a)</td><td>227.30 (n/a)</td><td>171.41 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 (-9.15%)</td><td>0.02 (-14.07%)</td><td>0.03 (+4.81%)</td><td>0.01 (-19.73%)</td><td>0.01 (+13.86%)</td><td>674.30 <b>(+24.57%)</b></td><td>421.84 <b>(+30.97%)</b></td><td>289.30 (-4.58%)</td><td>195.40 (+10.08%)</td><td>231.30 <b>(+73.27%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.30 (n/a)</td><td>322.08 (n/a)</td><td>303.20 (n/a)</td><td>177.50 (n/a)</td><td>133.49 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.06 (-3.59%)</td><td>0.04 (+14.89%)</td><td>0.04 <b>(+31.69%)</b></td><td>0.03 (+12.80%)</td><td>0.01 <b>(-26.35%)</b></td><td>412.50 (-11.35%)</td><td>300.14 (-17.28%)</td><td>311.30 <b>(-24.05%)</b></td><td>220.00 (+3.68%)</td><td>75.23 <b>(-35.11%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>465.30 (n/a)</td><td>362.84 (n/a)</td><td>409.90 (n/a)</td><td>212.20 (n/a)</td><td>115.93 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (-5.71%)</td><td>0.02 (+1.85%)</td><td>0.02 (-5.92%)</td><td>0.01 (-6.94%)</td><td>0.01 (+12.77%)</td><td>608.30 (+7.45%)</td><td>454.58 (+2.32%)</td><td>527.40 (+6.29%)</td><td>261.30 (+6.05%)</td><td>170.60 <b>(+27.51%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.10 (n/a)</td><td>444.26 (n/a)</td><td>496.20 (n/a)</td><td>246.40 (n/a)</td><td>133.79 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.04 <b>(-37.47%)</b></td><td>0.03 <b>(-23.37%)</b></td><td>0.02 (+1.11%)</td><td>0.01 <b>(-31.44%)</b></td><td>0.01 <b>(-45.63%)</b></td><td>908.10 <b>(+45.86%)</b></td><td>485.54 <b>(+21.46%)</b></td><td>459.50 (-1.10%)</td><td>245.00 <b>(+59.92%)</b></td><td>254.51 <b>(+32.89%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>622.60 (n/a)</td><td>399.74 (n/a)</td><td>464.60 (n/a)</td><td>153.20 (n/a)</td><td>191.53 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 <b>(-25.17%)</b></td><td>0.02 (-14.29%)</td><td>0.02 (-6.50%)</td><td>0.01 <b>(-22.42%)</b></td><td>0.01 <b>(-35.01%)</b></td><td>649.40 <b>(+28.90%)</b></td><td>465.54 (+13.19%)</td><td>479.40 (+6.94%)</td><td>277.40 <b>(+33.69%)</b></td><td>134.25 (+11.79%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.80 (n/a)</td><td>411.28 (n/a)</td><td>448.30 (n/a)</td><td>207.50 (n/a)</td><td>120.09 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (-10.52%)</td><td>0.02 (-13.19%)</td><td>0.02 <b>(-31.89%)</b></td><td>0.02 (-15.13%)</td><td>0.01 <b>(+20.64%)</b></td><td>585.10 (+17.82%)</td><td>466.88 <b>(+20.19%)</b></td><td>553.50 <b>(+46.82%)</b></td><td>298.50 (+11.80%)</td><td>141.93 <b>(+62.28%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.60 (n/a)</td><td>388.44 (n/a)</td><td>377.00 (n/a)</td><td>267.00 (n/a)</td><td>87.46 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 <b>(-24.61%)</b></td><td>0.02 (+14.82%)</td><td>0.03 <b>(+57.81%)</b></td><td>0.02 <b>(+249.74%)</b></td><td>0.01 <b>(-52.22%)</b></td><td>522.00 <b>(-71.41%)</b></td><td>358.70 <b>(-46.44%)</b></td><td>299.50 <b>(-36.63%)</b></td><td>256.00 <b>(+32.64%)</b></td><td>113.85 <b>(-82.82%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1825.70 (n/a)</td><td>669.68 (n/a)</td><td>472.60 (n/a)</td><td>193.00 (n/a)</td><td>662.89 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.05 <b>(+28.79%)</b></td><td>0.02 (+15.20%)</td><td>0.02 (-10.15%)</td><td>0.02 <b>(+308.96%)</b></td><td>0.01 (+10.51%)</td><td>589.00 <b>(-75.55%)</b></td><td>461.04 <b>(-43.26%)</b></td><td>490.80 (+11.32%)</td><td>191.00 <b>(-22.36%)</b></td><td>162.88 <b>(-81.95%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2408.80 (n/a)</td><td>812.58 (n/a)</td><td>440.90 (n/a)</td><td>246.00 (n/a)</td><td>902.40 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (-18.43%)</td><td>0.02 (+11.35%)</td><td>0.02 <b>(+39.50%)</b></td><td>0.01 (-7.88%)</td><td>0.01 <b>(-23.98%)</b></td><td>581.30 (+8.55%)</td><td>386.70 (-12.21%)</td><td>337.50 <b>(-28.31%)</b></td><td>264.60 <b>(+22.61%)</b></td><td>135.52 (+4.96%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.50 (n/a)</td><td>440.48 (n/a)</td><td>470.80 (n/a)</td><td>215.80 (n/a)</td><td>129.11 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.06 <b>(+29.28%)</b></td><td>0.03 (+11.71%)</td><td>0.02 (+0.64%)</td><td>0.02 (+8.13%)</td><td>0.02 <b>(+27.10%)</b></td><td>591.50 (-7.51%)</td><td>369.66 (-8.79%)</td><td>411.00 (-0.63%)</td><td>162.70 <b>(-22.67%)</b></td><td>165.07 (-9.09%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>639.50 (n/a)</td><td>405.28 (n/a)</td><td>413.60 (n/a)</td><td>210.40 (n/a)</td><td>181.58 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.03 (-11.19%)</td><td>0.02 <b>(-21.78%)</b></td><td>0.02 <b>(-26.15%)</b></td><td>0.01 <b>(-38.05%)</b></td><td>0.01 (+17.43%)</td><td>784.70 <b>(+61.43%)</b></td><td>519.36 <b>(+38.26%)</b></td><td>498.30 <b>(+35.41%)</b></td><td>279.70 (+12.60%)</td><td>205.30 <b>(+111.74%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>486.10 (n/a)</td><td>375.64 (n/a)</td><td>368.00 (n/a)</td><td>248.40 (n/a)</td><td>96.96 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.37 (-2.23%)</td><td>0.27 (-0.14%)</td><td>0.22 (-3.91%)</td><td>0.20 (+7.93%)</td><td>0.08 (+1.30%)</td><td>501.70 (-7.33%)</td><td>396.42 (+0.17%)</td><td>438.00 (+4.06%)</td><td>266.40 (+2.26%)</td><td>112.50 (-2.05%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.38 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>541.40 (n/a)</td><td>395.74 (n/a)</td><td>420.90 (n/a)</td><td>260.50 (n/a)</td><td>114.86 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.33 <b>(-25.55%)</b></td><td>0.22 <b>(-32.57%)</b></td><td>0.20 <b>(-48.57%)</b></td><td>0.17 (+6.11%)</td><td>0.07 <b>(-49.87%)</b></td><td>589.90 (-5.75%)</td><td>478.28 <b>(+31.50%)</b></td><td>480.30 <b>(+94.45%)</b></td><td>295.00 <b>(+34.34%)</b></td><td>119.82 <b>(-35.15%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.40 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>625.90 (n/a)</td><td>363.70 (n/a)</td><td>247.00 (n/a)</td><td>219.60 (n/a)</td><td>184.78 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.32 <b>(-33.66%)</b></td><td>0.24 (-15.80%)</td><td>0.25 (+17.80%)</td><td>0.17 (+5.53%)</td><td>0.06 <b>(-56.29%)</b></td><td>580.00 (-5.24%)</td><td>441.82 (+4.14%)</td><td>398.00 (-15.10%)</td><td>305.30 <b>(+50.77%)</b></td><td>116.25 <b>(-36.42%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.49 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>612.10 (n/a)</td><td>424.26 (n/a)</td><td>468.80 (n/a)</td><td>202.50 (n/a)</td><td>182.84 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.28 (-10.46%)</td><td>0.18 (-13.90%)</td><td>0.16 (-4.08%)</td><td>0.11 <b>(-25.74%)</b></td><td>0.06 (-10.97%)</td><td>659.20 <b>(+34.67%)</b></td><td>448.52 (+17.08%)</td><td>450.90 (+4.25%)</td><td>261.70 (+11.65%)</td><td>144.16 <b>(+29.08%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>489.50 (n/a)</td><td>383.10 (n/a)</td><td>432.50 (n/a)</td><td>234.40 (n/a)</td><td>111.68 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.31 (+19.77%)</td><td>0.17 (-18.80%)</td><td>0.15 <b>(-39.61%)</b></td><td>0.03 <b>(-73.27%)</b></td><td>0.11 <b>(+54.48%)</b></td><td>2502.10 <b>(+274.17%)</b></td><td>839.18 <b>(+106.47%)</b></td><td>493.80 <b>(+65.59%)</b></td><td>235.30 (-16.53%)</td><td>941.80 <b>(+451.90%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.25 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>668.70 (n/a)</td><td>406.44 (n/a)</td><td>298.20 (n/a)</td><td>281.90 (n/a)</td><td>170.65 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.28 (-16.15%)</td><td>0.16 (-6.81%)</td><td>0.15 (+18.73%)</td><td>0.04 <b>(-32.37%)</b></td><td>0.10 (-12.40%)</td><td>2027.90 <b>(+47.87%)</b></td><td>758.52 <b>(+20.73%)</b></td><td>499.70 (-15.78%)</td><td>263.90 (+19.25%)</td><td>730.74 <b>(+60.27%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.33 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.11 (n/a)</td><td>1371.40 (n/a)</td><td>628.28 (n/a)</td><td>593.30 (n/a)</td><td>221.30 (n/a)</td><td>455.95 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.44 <b>(-22.47%)</b></td><td>0.29 (-13.38%)</td><td>0.24 (-6.08%)</td><td>0.18 (-15.93%)</td><td>0.12 (-18.33%)</td><td>716.50 (+18.94%)</td><td>513.68 (+15.57%)</td><td>555.40 (+6.46%)</td><td>294.70 <b>(+28.97%)</b></td><td>197.41 <b>(+22.31%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.57 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>602.40 (n/a)</td><td>444.46 (n/a)</td><td>521.70 (n/a)</td><td>228.50 (n/a)</td><td>161.41 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.55 (+10.82%)</td><td>0.28 (-12.92%)</td><td>0.29 (+11.18%)</td><td>0.05 <b>(-74.52%)</b></td><td>0.18 <b>(+51.63%)</b></td><td>2425.00 <b>(+292.39%)</b></td><td>828.96 <b>(+86.55%)</b></td><td>449.30 (-10.05%)</td><td>240.50 (-9.76%)</td><td>901.16 <b>(+527.21%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.49 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>618.00 (n/a)</td><td>444.36 (n/a)</td><td>499.50 (n/a)</td><td>266.50 (n/a)</td><td>143.68 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.47 (+2.18%)</td><td>0.35 (+8.20%)</td><td>0.32 (+6.32%)</td><td>0.21 (-7.81%)</td><td>0.11 (+11.29%)</td><td>611.40 (+8.48%)</td><td>406.12 (-6.18%)</td><td>414.60 (-5.94%)</td><td>276.20 (-2.16%)</td><td>135.72 (+11.59%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.10 (n/a)</td><td>563.60 (n/a)</td><td>432.88 (n/a)</td><td>440.80 (n/a)</td><td>282.30 (n/a)</td><td>121.62 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 <b>(+28.02%)</b></td><td>0.02 <b>(+38.23%)</b></td><td>0.02 <b>(+56.69%)</b></td><td>0.01 <b>(+68.78%)</b></td><td>0.00 <b>(-24.44%)</b></td><td>312.30 <b>(-40.75%)</b></td><td>267.06 <b>(-30.38%)</b></td><td>256.80 <b>(-36.17%)</b></td><td>220.90 <b>(-21.89%)</b></td><td>36.99 <b>(-63.13%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>527.10 (n/a)</td><td>383.58 (n/a)</td><td>402.30 (n/a)</td><td>282.80 (n/a)</td><td>100.32 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (+0.89%)</td><td>0.01 (-16.65%)</td><td>0.01 (-16.06%)</td><td>0.01 <b>(-34.61%)</b></td><td>0.00 <b>(+210.65%)</b></td><td>489.90 <b>(+52.90%)</b></td><td>377.60 <b>(+25.57%)</b></td><td>366.00 (+19.10%)</td><td>267.30 (-0.85%)</td><td>91.86 <b>(+382.00%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>320.40 (n/a)</td><td>300.70 (n/a)</td><td>307.30 (n/a)</td><td>269.60 (n/a)</td><td>19.06 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (+18.71%)</td><td>0.01 <b>(+32.02%)</b></td><td>0.02 <b>(+73.16%)</b></td><td>0.01 (+10.74%)</td><td>0.00 <b>(+69.08%)</b></td><td>535.10 (-9.70%)</td><td>356.96 (-18.07%)</td><td>254.10 <b>(-42.25%)</b></td><td>233.10 (-15.76%)</td><td>154.58 <b>(+36.36%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.60 (n/a)</td><td>435.68 (n/a)</td><td>440.00 (n/a)</td><td>276.70 (n/a)</td><td>113.36 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.65 <b>(+47.66%)</b></td><td>0.45 <b>(+31.36%)</b></td><td>0.51 <b>(+62.74%)</b></td><td>0.21 (-9.77%)</td><td>0.17 <b>(+91.07%)</b></td><td>617.10 (+10.83%)</td><td>346.14 (-16.11%)</td><td>257.40 <b>(-38.55%)</b></td><td>204.10 <b>(-32.28%)</b></td><td>167.72 <b>(+53.67%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.44 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.09 (n/a)</td><td>556.80 (n/a)</td><td>412.62 (n/a)</td><td>418.90 (n/a)</td><td>301.40 (n/a)</td><td>109.14 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.55 (+16.89%)</td><td>0.49 <b>(+44.41%)</b></td><td>0.50 <b>(+83.70%)</b></td><td>0.42 <b>(+70.71%)</b></td><td>0.05 <b>(-53.36%)</b></td><td>314.50 <b>(-41.42%)</b></td><td>270.74 <b>(-35.57%)</b></td><td>264.50 <b>(-45.55%)</b></td><td>241.30 (-14.46%)</td><td>30.06 <b>(-75.95%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.11 (n/a)</td><td>536.90 (n/a)</td><td>420.24 (n/a)</td><td>485.80 (n/a)</td><td>282.10 (n/a)</td><td>124.97 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.50 (+1.42%)</td><td>0.36 (-15.38%)</td><td>0.36 (-15.89%)</td><td>0.23 <b>(-28.32%)</b></td><td>0.11 <b>(+57.31%)</b></td><td>585.80 <b>(+39.51%)</b></td><td>401.64 <b>(+25.51%)</b></td><td>368.00 (+18.90%)</td><td>262.00 (-1.43%)</td><td>133.83 <b>(+116.99%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.50 (n/a)</td><td>0.42 (n/a)</td><td>0.43 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>419.90 (n/a)</td><td>320.00 (n/a)</td><td>309.50 (n/a)</td><td>265.80 (n/a)</td><td>61.68 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.72 <b>(+27.63%)</b></td><td>0.50 <b>(+22.01%)</b></td><td>0.51 (+16.20%)</td><td>0.27 (-8.94%)</td><td>0.17 <b>(+52.00%)</b></td><td>494.50 (+9.82%)</td><td>296.86 (-13.67%)</td><td>259.20 (-13.94%)</td><td>184.70 <b>(-21.64%)</b></td><td>122.63 <b>(+25.29%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.56 (n/a)</td><td>0.41 (n/a)</td><td>0.44 (n/a)</td><td>0.29 (n/a)</td><td>0.11 (n/a)</td><td>450.30 (n/a)</td><td>343.88 (n/a)</td><td>301.20 (n/a)</td><td>235.70 (n/a)</td><td>97.88 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.76 (+11.37%)</td><td>0.42 (-5.98%)</td><td>0.33 <b>(-23.34%)</b></td><td>0.20 (-15.69%)</td><td>0.24 <b>(+46.41%)</b></td><td>669.90 (+18.61%)</td><td>403.32 <b>(+20.58%)</b></td><td>402.10 <b>(+30.47%)</b></td><td>174.10 (-10.21%)</td><td>204.96 <b>(+48.05%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.68 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>564.80 (n/a)</td><td>334.48 (n/a)</td><td>308.20 (n/a)</td><td>193.90 (n/a)</td><td>138.44 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (+9.88%)</td><td>0.01 <b>(+38.99%)</b></td><td>0.01 <b>(+44.83%)</b></td><td>0.01 <b>(+43.41%)</b></td><td>0.00 (-9.57%)</td><td>414.90 <b>(-30.27%)</b></td><td>305.04 <b>(-31.04%)</b></td><td>309.70 <b>(-30.95%)</b></td><td>211.90 (-8.98%)</td><td>80.82 <b>(-38.66%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>595.00 (n/a)</td><td>442.32 (n/a)</td><td>448.50 (n/a)</td><td>232.80 (n/a)</td><td>131.75 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.02 (-1.98%)</td><td>0.01 (-3.28%)</td><td>0.02 (+12.24%)</td><td>0.01 <b>(-37.87%)</b></td><td>0.00 <b>(+126.78%)</b></td><td>496.10 <b>(+60.97%)</b></td><td>306.62 (+10.33%)</td><td>251.50 (-10.91%)</td><td>239.40 (+2.00%)</td><td>108.37 <b>(+284.33%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>308.20 (n/a)</td><td>277.90 (n/a)</td><td>282.30 (n/a)</td><td>234.70 (n/a)</td><td>28.20 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.00 <b>(-33.33%)</b></td><td>0.00 (-20.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-48.36%)</b></td><td>22057.54 (-2.07%)</td><td>17768.95 (+7.46%)</td><td>18534.29 (-4.63%)</td><td>10316.17 <b>(+43.32%)</b></td><td>4629.89 <b>(-30.07%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22524.77 (n/a)</td><td>16535.20 (n/a)</td><td>19434.19 (n/a)</td><td>7197.81 (n/a)</td><td>6620.94 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.00 (+16.67%)</td><td>0.00 <b>(+51.72%)</b></td><td>0.00 <b>(+75.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+39.38%)</b></td><td>19102.96 (-2.17%)</td><td>11517.88 <b>(-27.76%)</b></td><td>10955.05 <b>(-40.28%)</b></td><td>5883.28 (-16.46%)</td><td>5881.21 (+13.45%)</td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19525.87 (n/a)</td><td>15943.22 (n/a)</td><td>18343.84 (n/a)</td><td>7042.60 (n/a)</td><td>5184.00 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>0.15 <b>(+21.75%)</b></td><td>0.12 (+15.85%)</td><td>0.12 <b>(+22.47%)</b></td><td>0.08 (+1.80%)</td><td>0.03 <b>(+58.20%)</b></td><td>26471.86 (-1.81%)</td><td>18895.09 (-11.09%)</td><td>17326.94 (-18.33%)</td><td>13983.85 (-17.88%)</td><td>5319.99 <b>(+28.38%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>26960.92 (n/a)</td><td>21251.20 (n/a)</td><td>21216.20 (n/a)</td><td>17028.98 (n/a)</td><td>4143.98 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>1.95 (+12.68%)</td><td>1.29 <b>(+22.63%)</b></td><td>1.46 <b>(+34.22%)</b></td><td>0.70 <b>(+335.07%)</b></td><td>0.56 (-5.59%)</td><td>749.00 <b>(-77.02%)</b></td><td>485.00 <b>(-51.57%)</b></td><td>358.70 <b>(-25.49%)</b></td><td>269.50 (-11.26%)</td><td>232.64 <b>(-81.63%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>1.73 (n/a)</td><td>1.05 (n/a)</td><td>1.09 (n/a)</td><td>0.16 (n/a)</td><td>0.59 (n/a)</td><td>3258.80 (n/a)</td><td>1001.38 (n/a)</td><td>481.40 (n/a)</td><td>303.70 (n/a)</td><td>1266.51 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>2.83 <b>(+23.05%)</b></td><td>2.16 <b>(+86.62%)</b></td><td>2.33 <b>(+126.36%)</b></td><td>1.33 <b>(+342.54%)</b></td><td>0.61 <b>(-29.03%)</b></td><td>786.40 <b>(-77.40%)</b></td><td>522.48 <b>(-67.38%)</b></td><td>450.20 <b>(-55.82%)</b></td><td>371.00 (-18.73%)</td><td>169.94 <b>(-87.05%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>2.30 (n/a)</td><td>1.16 (n/a)</td><td>1.03 (n/a)</td><td>0.30 (n/a)</td><td>0.85 (n/a)</td><td>3480.00 (n/a)</td><td>1601.82 (n/a)</td><td>1019.00 (n/a)</td><td>456.50 (n/a)</td><td>1312.76 (n/a)</td>
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
<td><code>72002fb</code> — 2026-09-09 02:19:11</td><td>2.09 <b>(+45.46%)</b></td><td>1.54 <b>(+52.92%)</b></td><td>1.66 <b>(+76.69%)</b></td><td>0.86 (+12.53%)</td><td>0.46 <b>(+82.56%)</b></td><td>609.90 (-11.13%)</td><td>373.74 <b>(-31.33%)</b></td><td>316.40 <b>(-43.41%)</b></td><td>251.50 <b>(-31.25%)</b></td><td>140.78 <b>(+22.62%)</b></td>
</tr>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:30:09</td><td>1.43 (n/a)</td><td>1.01 (n/a)</td><td>0.94 (n/a)</td><td>0.76 (n/a)</td><td>0.25 (n/a)</td><td>686.30 (n/a)</td><td>544.26 (n/a)</td><td>559.10 (n/a)</td><td>365.80 (n/a)</td><td>114.81 (n/a)</td>
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
