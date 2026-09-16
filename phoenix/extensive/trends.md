# IRON Trends


<details>
<summary>iron/operators/axpy</summary>


### test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (-14.14%)</td><td>0.02 (+2.65%)</td><td>0.02 (-12.78%)</td><td>0.01 <b>(+31.78%)</b></td><td>0.00 <b>(-40.83%)</b></td><td>495.60 <b>(-24.12%)</b></td><td>360.42 (-14.77%)</td><td>353.10 (+14.64%)</td><td>271.20 (+16.49%)</td><td>95.67 <b>(-54.26%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>653.10 (n/a)</td><td>422.90 (n/a)</td><td>308.00 (n/a)</td><td>232.80 (n/a)</td><td>209.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+1.98%)</td><td>0.02 (-3.07%)</td><td>0.01 <b>(-24.94%)</b></td><td>0.01 (-6.69%)</td><td>0.00 <b>(+36.91%)</b></td><td>550.50 (+7.16%)</td><td>437.08 (+6.85%)</td><td>509.60 <b>(+33.23%)</b></td><td>293.30 (-1.94%)</td><td>124.95 <b>(+37.92%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>513.70 (n/a)</td><td>409.06 (n/a)</td><td>382.50 (n/a)</td><td>299.10 (n/a)</td><td>90.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 <b>(-37.07%)</b></td><td>0.01 <b>(-32.72%)</b></td><td>0.01 <b>(-46.94%)</b></td><td>0.01 (-10.50%)</td><td>0.00 <b>(-50.61%)</b></td><td>658.70 (+11.74%)</td><td>486.34 <b>(+39.23%)</b></td><td>516.00 <b>(+88.46%)</b></td><td>362.80 <b>(+58.91%)</b></td><td>120.97 (-17.56%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>589.50 (n/a)</td><td>349.30 (n/a)</td><td>273.80 (n/a)</td><td>228.30 (n/a)</td><td>146.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (+10.90%)</td><td>0.02 <b>(+26.99%)</b></td><td>0.01 (+5.47%)</td><td>0.01 <b>(+362.14%)</b></td><td>0.01 <b>(-21.71%)</b></td><td>524.30 <b>(-78.36%)</b></td><td>399.80 <b>(-51.32%)</b></td><td>441.80 (-5.17%)</td><td>228.30 (-9.83%)</td><td>113.97 <b>(-87.36%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2423.10 (n/a)</td><td>821.24 (n/a)</td><td>465.90 (n/a)</td><td>253.20 (n/a)</td><td>901.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 <b>(-22.56%)</b></td><td>0.02 (-11.18%)</td><td>0.02 (-4.25%)</td><td>0.01 (+5.47%)</td><td>0.01 <b>(-33.46%)</b></td><td>626.30 (-5.18%)</td><td>390.90 (+1.37%)</td><td>303.80 (+4.43%)</td><td>237.00 <b>(+29.08%)</b></td><td>168.88 <b>(-20.65%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>660.50 (n/a)</td><td>385.60 (n/a)</td><td>290.90 (n/a)</td><td>183.60 (n/a)</td><td>212.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 <b>(-49.76%)</b></td><td>0.01 (-19.40%)</td><td>0.01 (+0.54%)</td><td>0.01 <b>(+87.13%)</b></td><td>0.00 <b>(-69.98%)</b></td><td>587.20 <b>(-46.56%)</b></td><td>483.50 (-11.98%)</td><td>487.40 (-0.53%)</td><td>296.50 <b>(+98.99%)</b></td><td>117.48 <b>(-65.78%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1098.90 (n/a)</td><td>549.30 (n/a)</td><td>490.00 (n/a)</td><td>149.00 (n/a)</td><td>343.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (-10.44%)</td><td>0.03 <b>(-23.54%)</b></td><td>0.03 <b>(-41.51%)</b></td><td>0.03 (-13.17%)</td><td>0.01 (+9.06%)</td><td>463.20 (+15.17%)</td><td>383.86 <b>(+33.39%)</b></td><td>435.40 <b>(+70.95%)</b></td><td>267.50 (+11.64%)</td><td>95.84 <b>(+41.55%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>402.20 (n/a)</td><td>287.78 (n/a)</td><td>254.70 (n/a)</td><td>239.60 (n/a)</td><td>67.71 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 <b>(-20.06%)</b></td><td>0.03 <b>(-38.37%)</b></td><td>0.03 <b>(-50.73%)</b></td><td>0.02 (+9.02%)</td><td>0.01 <b>(-34.70%)</b></td><td>570.90 (-8.27%)</td><td>461.34 <b>(+48.97%)</b></td><td>466.30 <b>(+103.00%)</b></td><td>262.80 <b>(+25.14%)</b></td><td>125.25 <b>(-28.98%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>622.40 (n/a)</td><td>309.68 (n/a)</td><td>229.70 (n/a)</td><td>210.00 (n/a)</td><td>176.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (+0.17%)</td><td>0.04 (-12.77%)</td><td>0.03 <b>(-44.57%)</b></td><td>0.02 (-7.64%)</td><td>0.02 (+18.04%)</td><td>559.50 (+8.26%)</td><td>405.58 <b>(+20.09%)</b></td><td>481.60 <b>(+80.37%)</b></td><td>224.10 (-0.18%)</td><td>159.71 <b>(+23.78%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.80 (n/a)</td><td>337.72 (n/a)</td><td>267.00 (n/a)</td><td>224.50 (n/a)</td><td>129.03 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (-0.47%)</td><td>0.04 (+6.46%)</td><td>0.04 (-8.37%)</td><td>0.02 (+11.92%)</td><td>0.01 <b>(-21.12%)</b></td><td>538.80 (-10.65%)</td><td>320.30 (-11.48%)</td><td>283.80 (+9.15%)</td><td>235.10 (+0.47%)</td><td>125.72 <b>(-24.82%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>603.00 (n/a)</td><td>361.84 (n/a)</td><td>260.00 (n/a)</td><td>234.00 (n/a)</td><td>167.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (+12.93%)</td><td>0.04 <b>(+24.08%)</b></td><td>0.03 (+14.08%)</td><td>0.02 (+14.25%)</td><td>0.02 <b>(+28.22%)</b></td><td>543.30 (-12.47%)</td><td>374.72 (-16.18%)</td><td>429.60 (-12.33%)</td><td>199.50 (-11.45%)</td><td>150.83 (+3.46%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>620.70 (n/a)</td><td>447.04 (n/a)</td><td>490.00 (n/a)</td><td>225.30 (n/a)</td><td>145.79 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (+4.01%)</td><td>0.04 (+6.70%)</td><td>0.04 (-13.29%)</td><td>0.02 <b>(+288.90%)</b></td><td>0.02 (-17.37%)</td><td>636.60 <b>(-74.29%)</b></td><td>403.12 <b>(-46.47%)</b></td><td>321.10 (+15.30%)</td><td>233.80 (-3.87%)</td><td>193.27 <b>(-80.05%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2475.80 (n/a)</td><td>753.02 (n/a)</td><td>278.50 (n/a)</td><td>243.20 (n/a)</td><td>968.99 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 <b>(+46.77%)</b></td><td>0.10 <b>(+38.50%)</b></td><td>0.10 <b>(+23.36%)</b></td><td>0.06 <b>(+59.45%)</b></td><td>0.03 (+9.61%)</td><td>392.10 <b>(-37.29%)</b></td><td>269.56 <b>(-31.55%)</b></td><td>242.40 (-18.93%)</td><td>184.30 <b>(-31.87%)</b></td><td>79.39 <b>(-50.55%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>625.30 (n/a)</td><td>393.80 (n/a)</td><td>299.00 (n/a)</td><td>270.50 (n/a)</td><td>160.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (-1.36%)</td><td>0.07 (-13.62%)</td><td>0.05 <b>(-43.26%)</b></td><td>0.04 (-4.19%)</td><td>0.03 (+11.85%)</td><td>633.80 (+4.38%)</td><td>422.24 (+18.83%)</td><td>478.80 <b>(+76.22%)</b></td><td>245.40 (+1.40%)</td><td>169.15 (+9.71%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>607.20 (n/a)</td><td>355.34 (n/a)</td><td>271.70 (n/a)</td><td>242.00 (n/a)</td><td>154.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.11 <b>(+46.67%)</b></td><td>0.07 (+17.13%)</td><td>0.05 (-13.26%)</td><td>0.04 (-13.93%)</td><td>0.03 <b>(+189.76%)</b></td><td>592.80 (+16.19%)</td><td>397.44 (-2.91%)</td><td>465.70 (+15.27%)</td><td>224.00 <b>(-31.81%)</b></td><td>162.01 <b>(+114.30%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>510.20 (n/a)</td><td>409.36 (n/a)</td><td>404.00 (n/a)</td><td>328.50 (n/a)</td><td>75.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (-19.68%)</td><td>0.06 (+0.75%)</td><td>0.05 (-1.13%)</td><td>0.04 (+2.59%)</td><td>0.02 <b>(-22.38%)</b></td><td>558.00 (-2.53%)</td><td>435.96 (-2.82%)</td><td>487.20 (+1.14%)</td><td>294.60 <b>(+24.46%)</b></td><td>125.87 (-1.79%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>572.50 (n/a)</td><td>448.60 (n/a)</td><td>481.70 (n/a)</td><td>236.70 (n/a)</td><td>128.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.11 (+10.17%)</td><td>0.08 (-4.70%)</td><td>0.09 (-1.38%)</td><td>0.04 (-11.00%)</td><td>0.03 <b>(+45.59%)</b></td><td>571.60 (+12.36%)</td><td>362.46 (+12.72%)</td><td>285.60 (+1.42%)</td><td>215.40 (-9.23%)</td><td>156.52 <b>(+44.80%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>508.70 (n/a)</td><td>321.56 (n/a)</td><td>281.60 (n/a)</td><td>237.30 (n/a)</td><td>108.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.11 (-14.44%)</td><td>0.06 (-13.44%)</td><td>0.06 (+0.42%)</td><td>0.02 <b>(-40.67%)</b></td><td>0.03 (-8.15%)</td><td>1319.40 <b>(+68.55%)</b></td><td>593.54 <b>(+31.24%)</b></td><td>437.80 (-0.41%)</td><td>224.70 (+16.91%)</td><td>427.01 <b>(+98.46%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>782.80 (n/a)</td><td>452.24 (n/a)</td><td>439.60 (n/a)</td><td>192.20 (n/a)</td><td>215.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.26 <b>(+36.23%)</b></td><td>0.18 (+7.06%)</td><td>0.20 (+18.32%)</td><td>0.10 (-19.65%)</td><td>0.07 <b>(+197.09%)</b></td><td>476.90 <b>(+24.48%)</b></td><td>321.84 (+6.04%)</td><td>244.20 (-15.50%)</td><td>192.50 <b>(-26.58%)</b></td><td>139.87 <b>(+190.13%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>383.10 (n/a)</td><td>303.52 (n/a)</td><td>289.00 (n/a)</td><td>262.20 (n/a)</td><td>48.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.23 <b>(+31.38%)</b></td><td>0.15 <b>(+22.31%)</b></td><td>0.20 <b>(+69.44%)</b></td><td>0.03 <b>(-67.06%)</b></td><td>0.08 <b>(+102.75%)</b></td><td>1856.20 <b>(+203.60%)</b></td><td>595.94 <b>(+40.83%)</b></td><td>249.50 <b>(-40.99%)</b></td><td>213.80 <b>(-23.89%)</b></td><td>709.15 <b>(+412.41%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>611.40 (n/a)</td><td>423.16 (n/a)</td><td>422.80 (n/a)</td><td>280.90 (n/a)</td><td>138.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.20 (-11.02%)</td><td>0.13 (+3.56%)</td><td>0.10 (+4.22%)</td><td>0.06 <b>(-32.78%)</b></td><td>0.06 (+6.32%)</td><td>824.20 <b>(+48.77%)</b></td><td>472.96 (+4.57%)</td><td>513.10 (-4.04%)</td><td>241.80 (+12.41%)</td><td>237.96 <b>(+63.02%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>554.00 (n/a)</td><td>452.28 (n/a)</td><td>534.70 (n/a)</td><td>215.10 (n/a)</td><td>145.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.20 (+7.08%)</td><td>0.17 <b>(+34.50%)</b></td><td>0.19 <b>(+78.68%)</b></td><td>0.11 <b>(+46.63%)</b></td><td>0.03 <b>(-30.18%)</b></td><td>433.60 <b>(-31.81%)</b></td><td>296.58 <b>(-30.97%)</b></td><td>265.30 <b>(-44.03%)</b></td><td>250.30 (-6.60%)</td><td>77.56 <b>(-50.74%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>635.90 (n/a)</td><td>429.64 (n/a)</td><td>474.00 (n/a)</td><td>268.00 (n/a)</td><td>157.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.17 (+18.65%)</td><td>0.12 <b>(+22.34%)</b></td><td>0.11 <b>(+41.72%)</b></td><td>0.10 <b>(+38.60%)</b></td><td>0.03 (-8.51%)</td><td>502.80 <b>(-27.85%)</b></td><td>440.54 <b>(-21.26%)</b></td><td>459.40 <b>(-29.44%)</b></td><td>297.80 (-15.71%)</td><td>81.87 <b>(-47.37%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>696.90 (n/a)</td><td>559.48 (n/a)</td><td>651.10 (n/a)</td><td>353.30 (n/a)</td><td>155.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.20 <b>(+33.51%)</b></td><td>0.14 <b>(+31.16%)</b></td><td>0.16 <b>(+49.03%)</b></td><td>0.08 (+4.82%)</td><td>0.05 <b>(+94.65%)</b></td><td>611.80 (-4.60%)</td><td>393.86 (-16.87%)</td><td>313.30 <b>(-32.90%)</b></td><td>241.00 <b>(-25.11%)</b></td><td>167.57 <b>(+43.72%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>641.30 (n/a)</td><td>473.80 (n/a)</td><td>466.90 (n/a)</td><td>321.80 (n/a)</td><td>116.60 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/dequant</summary>


### test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 <b>(-23.54%)</b></td><td>0.01 (+0.85%)</td><td>0.01 (+13.18%)</td><td>0.01 (+10.11%)</td><td>0.00 <b>(-35.51%)</b></td><td>464.60 (-9.19%)</td><td>331.18 (-6.35%)</td><td>278.60 (-11.64%)</td><td>254.70 <b>(+30.82%)</b></td><td>94.40 <b>(-26.27%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.60 (n/a)</td><td>353.64 (n/a)</td><td>315.30 (n/a)</td><td>194.70 (n/a)</td><td>128.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (-11.26%)</td><td>0.01 <b>(+25.39%)</b></td><td>0.01 <b>(+25.24%)</b></td><td>0.01 <b>(+51.93%)</b></td><td>0.00 <b>(-27.68%)</b></td><td>486.30 <b>(-34.19%)</b></td><td>370.82 <b>(-26.49%)</b></td><td>410.80 <b>(-20.16%)</b></td><td>260.10 (+12.65%)</td><td>101.53 <b>(-43.78%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>738.90 (n/a)</td><td>504.42 (n/a)</td><td>514.50 (n/a)</td><td>230.90 (n/a)</td><td>180.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (+1.73%)</td><td>0.01 (-7.62%)</td><td>0.01 (+11.63%)</td><td>0.00 <b>(-80.50%)</b></td><td>0.00 <b>(+95.08%)</b></td><td>2526.20 <b>(+412.83%)</b></td><td>765.76 <b>(+118.84%)</b></td><td>282.60 (-10.43%)</td><td>239.20 (-1.69%)</td><td>991.92 <b>(+866.18%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>492.60 (n/a)</td><td>349.92 (n/a)</td><td>315.50 (n/a)</td><td>243.30 (n/a)</td><td>102.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (+14.21%)</td><td>0.01 (+14.99%)</td><td>0.01 <b>(+26.26%)</b></td><td>0.01 (-10.65%)</td><td>0.00 <b>(+35.32%)</b></td><td>491.00 (+11.92%)</td><td>312.30 (-10.02%)</td><td>259.60 <b>(-20.78%)</b></td><td>221.20 (-12.43%)</td><td>110.01 <b>(+29.64%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>438.70 (n/a)</td><td>347.08 (n/a)</td><td>327.70 (n/a)</td><td>252.60 (n/a)</td><td>84.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 <b>(+47.54%)</b></td><td>0.01 <b>(+43.50%)</b></td><td>0.01 <b>(+27.84%)</b></td><td>0.00 <b>(+94.12%)</b></td><td>0.00 <b>(+50.08%)</b></td><td>541.60 <b>(-48.48%)</b></td><td>382.22 <b>(-32.39%)</b></td><td>361.10 <b>(-21.79%)</b></td><td>227.60 <b>(-32.22%)</b></td><td>142.16 <b>(-49.65%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1051.30 (n/a)</td><td>565.36 (n/a)</td><td>461.70 (n/a)</td><td>335.80 (n/a)</td><td>282.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 <b>(-33.38%)</b></td><td>0.01 <b>(-28.20%)</b></td><td>0.01 <b>(-34.40%)</b></td><td>0.00 <b>(-45.77%)</b></td><td>0.00 <b>(-30.28%)</b></td><td>1032.00 <b>(+84.38%)</b></td><td>551.66 <b>(+44.35%)</b></td><td>480.00 <b>(+52.43%)</b></td><td>348.20 <b>(+50.09%)</b></td><td>275.14 <b>(+99.00%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>559.70 (n/a)</td><td>382.16 (n/a)</td><td>314.90 (n/a)</td><td>232.00 (n/a)</td><td>138.26 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (-14.89%)</td><td>0.01 <b>(-33.48%)</b></td><td>0.01 <b>(-36.88%)</b></td><td>0.00 <b>(-72.15%)</b></td><td>0.01 <b>(+36.16%)</b></td><td>1862.90 <b>(+259.08%)</b></td><td>692.34 <b>(+123.90%)</b></td><td>412.80 <b>(+58.40%)</b></td><td>258.20 (+17.52%)</td><td>669.63 <b>(+459.29%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>518.80 (n/a)</td><td>309.22 (n/a)</td><td>260.60 (n/a)</td><td>219.70 (n/a)</td><td>119.73 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+7.13%)</td><td>0.01 (-9.07%)</td><td>0.01 (-6.97%)</td><td>0.01 (+8.17%)</td><td>0.01 (+5.99%)</td><td>524.70 (-7.56%)</td><td>444.86 (+9.66%)</td><td>488.60 (+7.48%)</td><td>223.40 (-6.64%)</td><td>126.15 (-9.24%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.60 (n/a)</td><td>405.66 (n/a)</td><td>454.60 (n/a)</td><td>239.30 (n/a)</td><td>139.00 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 <b>(-22.74%)</b></td><td>0.01 (-12.21%)</td><td>0.01 <b>(-37.57%)</b></td><td>0.01 <b>(+98.80%)</b></td><td>0.00 <b>(-53.57%)</b></td><td>539.40 <b>(-49.69%)</b></td><td>384.78 (-17.24%)</td><td>400.10 <b>(+60.17%)</b></td><td>259.80 <b>(+29.45%)</b></td><td>109.62 <b>(-70.23%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1072.20 (n/a)</td><td>464.94 (n/a)</td><td>249.80 (n/a)</td><td>200.70 (n/a)</td><td>368.29 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 <b>(-45.69%)</b></td><td>0.01 <b>(-28.54%)</b></td><td>0.01 (-11.66%)</td><td>0.01 <b>(+29.05%)</b></td><td>0.00 <b>(-72.36%)</b></td><td>616.60 <b>(-22.51%)</b></td><td>498.96 (+18.61%)</td><td>460.50 (+13.20%)</td><td>415.30 <b>(+84.09%)</b></td><td>88.69 <b>(-60.67%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>795.70 (n/a)</td><td>420.68 (n/a)</td><td>406.80 (n/a)</td><td>225.60 (n/a)</td><td>225.54 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 <b>(+31.13%)</b></td><td>0.01 (+6.19%)</td><td>0.01 (-17.66%)</td><td>0.01 (+18.36%)</td><td>0.01 <b>(+30.11%)</b></td><td>517.30 (-15.52%)</td><td>405.72 (-5.51%)</td><td>449.90 <b>(+21.43%)</b></td><td>202.50 <b>(-23.76%)</b></td><td>134.02 (-19.71%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>612.30 (n/a)</td><td>429.38 (n/a)</td><td>370.50 (n/a)</td><td>265.60 (n/a)</td><td>166.92 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+4.54%)</td><td>0.01 (-7.02%)</td><td>0.01 <b>(-27.04%)</b></td><td>0.01 (-17.94%)</td><td>0.00 <b>(+56.61%)</b></td><td>598.70 <b>(+21.86%)</b></td><td>453.54 (+12.61%)</td><td>495.90 <b>(+37.06%)</b></td><td>309.30 (-4.33%)</td><td>132.00 <b>(+68.96%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.30 (n/a)</td><td>402.74 (n/a)</td><td>361.80 (n/a)</td><td>323.30 (n/a)</td><td>78.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 <b>(-20.03%)</b></td><td>0.03 (-11.72%)</td><td>0.04 (-7.54%)</td><td>0.02 (+19.71%)</td><td>0.01 <b>(-27.33%)</b></td><td>455.10 (-16.46%)</td><td>337.52 (+7.85%)</td><td>294.00 (+8.13%)</td><td>259.10 <b>(+25.05%)</b></td><td>91.54 <b>(-30.93%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.80 (n/a)</td><td>312.96 (n/a)</td><td>271.90 (n/a)</td><td>207.20 (n/a)</td><td>132.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (-17.55%)</td><td>0.03 (-16.95%)</td><td>0.03 <b>(-23.57%)</b></td><td>0.02 <b>(+358.86%)</b></td><td>0.01 <b>(-56.86%)</b></td><td>538.40 <b>(-78.21%)</b></td><td>422.94 <b>(-40.98%)</b></td><td>407.80 <b>(+30.83%)</b></td><td>291.00 <b>(+21.25%)</b></td><td>106.30 <b>(-89.17%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2470.60 (n/a)</td><td>716.60 (n/a)</td><td>311.70 (n/a)</td><td>240.00 (n/a)</td><td>981.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (-7.25%)</td><td>0.04 (+19.65%)</td><td>0.04 (-2.79%)</td><td>0.04 <b>(+258.43%)</b></td><td>0.01 <b>(-62.49%)</b></td><td>294.50 <b>(-72.10%)</b></td><td>267.46 <b>(-40.37%)</b></td><td>280.20 (+2.86%)</td><td>203.50 (+7.79%)</td><td>36.92 <b>(-89.59%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1055.50 (n/a)</td><td>448.52 (n/a)</td><td>272.40 (n/a)</td><td>188.80 (n/a)</td><td>354.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 <b>(-27.05%)</b></td><td>0.02 (-11.86%)</td><td>0.02 (-10.13%)</td><td>0.02 (+1.09%)</td><td>0.00 <b>(-52.82%)</b></td><td>582.40 (-1.07%)</td><td>491.82 (+7.50%)</td><td>507.10 (+11.28%)</td><td>363.50 <b>(+37.07%)</b></td><td>79.45 <b>(-36.94%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>588.70 (n/a)</td><td>457.52 (n/a)</td><td>455.70 (n/a)</td><td>265.20 (n/a)</td><td>126.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 <b>(+44.88%)</b></td><td>0.04 <b>(+21.56%)</b></td><td>0.04 <b>(+23.06%)</b></td><td>0.02 (-5.78%)</td><td>0.02 <b>(+89.37%)</b></td><td>578.80 (+6.12%)</td><td>360.28 (-6.05%)</td><td>273.90 (-18.72%)</td><td>186.90 <b>(-30.98%)</b></td><td>187.99 <b>(+49.27%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.40 (n/a)</td><td>383.50 (n/a)</td><td>337.00 (n/a)</td><td>270.80 (n/a)</td><td>125.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (-13.98%)</td><td>0.03 (-5.36%)</td><td>0.02 (+3.10%)</td><td>0.02 <b>(+22.24%)</b></td><td>0.01 <b>(-39.66%)</b></td><td>517.20 (-18.19%)</td><td>423.14 (-1.39%)</td><td>460.50 (-3.01%)</td><td>302.50 (+16.26%)</td><td>92.72 <b>(-39.81%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>632.20 (n/a)</td><td>429.12 (n/a)</td><td>474.80 (n/a)</td><td>260.20 (n/a)</td><td>154.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.09 (-17.18%)</td><td>0.07 (+16.06%)</td><td>0.08 <b>(+40.26%)</b></td><td>0.05 <b>(+40.67%)</b></td><td>0.02 <b>(-44.72%)</b></td><td>458.50 <b>(-28.91%)</b></td><td>314.12 <b>(-22.44%)</b></td><td>276.20 <b>(-28.70%)</b></td><td>246.30 <b>(+20.74%)</b></td><td>84.33 <b>(-50.02%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>645.00 (n/a)</td><td>404.98 (n/a)</td><td>387.40 (n/a)</td><td>204.00 (n/a)</td><td>168.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 <b>(-29.79%)</b></td><td>0.04 <b>(-20.42%)</b></td><td>0.04 (-7.03%)</td><td>0.01 <b>(-67.52%)</b></td><td>0.02 (-13.28%)</td><td>1873.40 <b>(+207.92%)</b></td><td>715.62 <b>(+67.32%)</b></td><td>499.90 (+7.57%)</td><td>285.50 <b>(+42.47%)</b></td><td>658.11 <b>(+338.60%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>608.40 (n/a)</td><td>427.70 (n/a)</td><td>464.70 (n/a)</td><td>200.40 (n/a)</td><td>150.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 <b>(+26.95%)</b></td><td>0.05 (-13.91%)</td><td>0.05 (-3.73%)</td><td>0.01 <b>(-68.51%)</b></td><td>0.03 <b>(+76.72%)</b></td><td>1892.20 <b>(+217.48%)</b></td><td>693.06 <b>(+77.29%)</b></td><td>411.80 (+3.86%)</td><td>213.00 <b>(-21.23%)</b></td><td>680.87 <b>(+415.31%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>596.00 (n/a)</td><td>390.92 (n/a)</td><td>396.50 (n/a)</td><td>270.40 (n/a)</td><td>132.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 <b>(-30.18%)</b></td><td>0.06 (+1.19%)</td><td>0.05 <b>(+29.24%)</b></td><td>0.04 (-2.92%)</td><td>0.01 <b>(-53.85%)</b></td><td>552.80 (+3.00%)</td><td>398.40 (-11.25%)</td><td>402.70 <b>(-22.63%)</b></td><td>271.10 <b>(+43.21%)</b></td><td>102.89 <b>(-29.91%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>536.70 (n/a)</td><td>448.88 (n/a)</td><td>520.50 (n/a)</td><td>189.30 (n/a)</td><td>146.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.11 <b>(+63.54%)</b></td><td>0.08 <b>(+67.44%)</b></td><td>0.08 <b>(+65.52%)</b></td><td>0.07 <b>(+75.35%)</b></td><td>0.02 <b>(+35.12%)</b></td><td>317.80 <b>(-42.96%)</b></td><td>260.00 <b>(-41.63%)</b></td><td>273.30 <b>(-39.59%)</b></td><td>184.00 <b>(-38.85%)</b></td><td>51.26 <b>(-55.47%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>557.20 (n/a)</td><td>445.42 (n/a)</td><td>452.40 (n/a)</td><td>300.90 (n/a)</td><td>115.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (-11.04%)</td><td>0.05 (-16.78%)</td><td>0.05 (+0.70%)</td><td>0.02 <b>(-56.87%)</b></td><td>0.02 (+1.67%)</td><td>1377.30 <b>(+131.87%)</b></td><td>610.26 <b>(+42.41%)</b></td><td>430.20 (-0.69%)</td><td>290.00 (+12.40%)</td><td>442.49 <b>(+182.18%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>594.00 (n/a)</td><td>428.52 (n/a)</td><td>433.20 (n/a)</td><td>258.00 (n/a)</td><td>156.81 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_add</summary>


### test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>478.00 (n/a)</td><td>358.20 (n/a)</td><td>302.90 (n/a)</td><td>241.80 (n/a)</td><td>109.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>640.10 (n/a)</td><td>393.38 (n/a)</td><td>394.40 (n/a)</td><td>197.10 (n/a)</td><td>169.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>521.30 (n/a)</td><td>414.30 (n/a)</td><td>483.60 (n/a)</td><td>258.40 (n/a)</td><td>130.61 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.90 (n/a)</td><td>368.44 (n/a)</td><td>284.10 (n/a)</td><td>244.80 (n/a)</td><td>138.42 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>541.90 (n/a)</td><td>399.70 (n/a)</td><td>403.40 (n/a)</td><td>294.70 (n/a)</td><td>105.36 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1087.10 (n/a)</td><td>656.34 (n/a)</td><td>545.10 (n/a)</td><td>487.60 (n/a)</td><td>245.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2106.50 (n/a)</td><td>847.88 (n/a)</td><td>643.20 (n/a)</td><td>267.70 (n/a)</td><td>724.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>547.20 (n/a)</td><td>359.82 (n/a)</td><td>296.40 (n/a)</td><td>237.80 (n/a)</td><td>142.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>541.10 (n/a)</td><td>388.64 (n/a)</td><td>321.60 (n/a)</td><td>237.10 (n/a)</td><td>140.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.21 <b>(+21.33%)</b></td><td>0.16 <b>(+21.44%)</b></td><td>0.20 <b>(+21.66%)</b></td><td>0.09 <b>(+29.37%)</b></td><td>0.05 (+13.32%)</td><td>545.40 <b>(-22.69%)</b></td><td>334.38 (-19.35%)</td><td>251.10 (-17.81%)</td><td>229.30 (-17.58%)</td><td>135.99 <b>(-26.63%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>705.50 (n/a)</td><td>414.60 (n/a)</td><td>305.50 (n/a)</td><td>278.20 (n/a)</td><td>185.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>618.10 (n/a)</td><td>398.58 (n/a)</td><td>302.90 (n/a)</td><td>180.70 (n/a)</td><td>203.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>546.20 (n/a)</td><td>405.72 (n/a)</td><td>442.50 (n/a)</td><td>211.30 (n/a)</td><td>126.27 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/elementwise_mul</summary>


### test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>478.60 (n/a)</td><td>291.86 (n/a)</td><td>281.20 (n/a)</td><td>159.50 (n/a)</td><td>117.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.10 (n/a)</td><td>444.16 (n/a)</td><td>564.30 (n/a)</td><td>225.00 (n/a)</td><td>195.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.80 (n/a)</td><td>383.42 (n/a)</td><td>365.10 (n/a)</td><td>255.30 (n/a)</td><td>131.73 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1967.60 (n/a)</td><td>673.66 (n/a)</td><td>300.80 (n/a)</td><td>269.90 (n/a)</td><td>730.90 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>582.90 (n/a)</td><td>366.86 (n/a)</td><td>298.20 (n/a)</td><td>201.20 (n/a)</td><td>177.48 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>633.20 (n/a)</td><td>466.80 (n/a)</td><td>504.90 (n/a)</td><td>268.10 (n/a)</td><td>147.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>671.50 (n/a)</td><td>411.32 (n/a)</td><td>428.40 (n/a)</td><td>210.30 (n/a)</td><td>196.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>531.20 (n/a)</td><td>436.00 (n/a)</td><td>468.10 (n/a)</td><td>270.20 (n/a)</td><td>104.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>763.20 (n/a)</td><td>453.18 (n/a)</td><td>469.20 (n/a)</td><td>236.90 (n/a)</td><td>221.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>554.90 (n/a)</td><td>449.54 (n/a)</td><td>478.90 (n/a)</td><td>266.70 (n/a)</td><td>108.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>541.60 (n/a)</td><td>318.32 (n/a)</td><td>283.10 (n/a)</td><td>210.70 (n/a)</td><td>130.98 (n/a)</td>
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


### test_gemm[M_1024-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.12 (+18.77%)</td><td>3.81 <b>(+21.20%)</b></td><td>4.07 <b>(+22.59%)</b></td><td>2.74 (+2.01%)</td><td>0.60 <b>(+66.03%)</b></td><td>3823.00 (-1.97%)</td><td>2819.64 (-16.31%)</td><td>2573.80 (-18.43%)</td><td>2546.90 (-15.80%)</td><td>561.05 <b>(+38.79%)</b></td><td>1686.36 (+18.77%)</td><td>1562.30 <b>(+21.20%)</b></td><td>1668.74 <b>(+22.59%)</b></td><td>1123.45 (+2.01%)</td><td>245.47 <b>(+66.03%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.47 (n/a)</td><td>3.15 (n/a)</td><td>3.32 (n/a)</td><td>2.69 (n/a)</td><td>0.36 (n/a)</td><td>3900.00 (n/a)</td><td>3368.96 (n/a)</td><td>3155.30 (n/a)</td><td>3024.90 (n/a)</td><td>404.24 (n/a)</td><td>1419.87 (n/a)</td><td>1289.04 (n/a)</td><td>1361.19 (n/a)</td><td>1101.28 (n/a)</td><td>147.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_1024-K_2560-N_2560-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.82 (+14.28%)</td><td>3.68 <b>(+22.17%)</b></td><td>3.70 <b>(+24.66%)</b></td><td>3.58 <b>(+26.63%)</b></td><td>0.09 <b>(-52.25%)</b></td><td>6581.80 <b>(-21.03%)</b></td><td>6405.68 (-18.36%)</td><td>6378.00 (-19.78%)</td><td>6169.40 (-12.50%)</td><td>159.97 <b>(-66.51%)</b></td><td>2175.53 (+14.28%)</td><td>2096.35 <b>(+22.17%)</b></td><td>2104.40 <b>(+24.66%)</b></td><td>2039.22 <b>(+26.63%)</b></td><td>52.88 <b>(-52.25%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.35 (n/a)</td><td>3.02 (n/a)</td><td>2.97 (n/a)</td><td>2.83 (n/a)</td><td>0.19 (n/a)</td><td>8334.60 (n/a)</td><td>7846.62 (n/a)</td><td>7951.00 (n/a)</td><td>7050.60 (n/a)</td><td>477.73 (n/a)</td><td>1903.64 (n/a)</td><td>1715.90 (n/a)</td><td>1688.06 (n/a)</td><td>1610.36 (n/a)</td><td>110.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.09 (+5.86%)</td><td>3.42 (+6.15%)</td><td>3.82 (+12.26%)</td><td>2.38 (-10.37%)</td><td>0.72 <b>(+40.72%)</b></td><td>7061.50 (+11.58%)</td><td>5111.52 (-3.83%)</td><td>4393.20 (-10.92%)</td><td>4099.20 (-5.54%)</td><td>1236.75 <b>(+45.07%)</b></td><td>2095.53 (+5.86%)</td><td>1750.86 (+6.15%)</td><td>1955.29 (+12.26%)</td><td>1216.45 (-10.37%)</td><td>366.58 <b>(+40.72%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.87 (n/a)</td><td>3.22 (n/a)</td><td>3.40 (n/a)</td><td>2.65 (n/a)</td><td>0.51 (n/a)</td><td>6328.90 (n/a)</td><td>5314.88 (n/a)</td><td>4931.80 (n/a)</td><td>4339.40 (n/a)</td><td>852.53 (n/a)</td><td>1979.53 (n/a)</td><td>1649.49 (n/a)</td><td>1741.76 (n/a)</td><td>1357.26 (n/a)</td><td>260.50 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.96 (-11.25%)</td><td>0.72 (-17.92%)</td><td>0.67 <b>(-24.76%)</b></td><td>0.56 <b>(-25.05%)</b></td><td>0.18 <b>(+32.60%)</b></td><td>819.70 <b>(+33.41%)</b></td><td>667.50 <b>(+25.40%)</b></td><td>685.00 <b>(+32.91%)</b></td><td>478.90 (+12.68%)</td><td>155.20 <b>(+101.53%)</b></td><td>70.07 (-11.25%)</td><td>52.66 (-17.92%)</td><td>48.98 <b>(-24.76%)</b></td><td>40.94 <b>(-25.05%)</b></td><td>12.97 <b>(+32.60%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.08 (n/a)</td><td>0.88 (n/a)</td><td>0.89 (n/a)</td><td>0.75 (n/a)</td><td>0.13 (n/a)</td><td>614.40 (n/a)</td><td>532.30 (n/a)</td><td>515.40 (n/a)</td><td>425.00 (n/a)</td><td>77.01 (n/a)</td><td>78.96 (n/a)</td><td>64.16 (n/a)</td><td>65.10 (n/a)</td><td>54.61 (n/a)</td><td>9.78 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.33 (-12.31%)</td><td>1.06 (-10.33%)</td><td>1.07 (-1.13%)</td><td>0.79 (+7.49%)</td><td>0.22 <b>(-34.29%)</b></td><td>824.60 (-6.97%)</td><td>638.50 (+7.59%)</td><td>610.90 (+1.14%)</td><td>492.00 (+14.05%)</td><td>135.78 <b>(-27.06%)</b></td><td>136.40 (-12.31%)</td><td>108.88 (-10.33%)</td><td>109.85 (-1.13%)</td><td>81.38 (+7.49%)</td><td>22.41 <b>(-34.29%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.52 (n/a)</td><td>1.19 (n/a)</td><td>1.08 (n/a)</td><td>0.74 (n/a)</td><td>0.33 (n/a)</td><td>886.40 (n/a)</td><td>593.46 (n/a)</td><td>604.00 (n/a)</td><td>431.40 (n/a)</td><td>186.16 (n/a)</td><td>155.55 (n/a)</td><td>121.41 (n/a)</td><td>111.10 (n/a)</td><td>75.71 (n/a)</td><td>34.11 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.61 (-15.03%)</td><td>0.85 (-12.34%)</td><td>0.74 (-14.35%)</td><td>0.23 (+5.61%)</td><td>0.58 (-4.02%)</td><td>3340.00 (-5.31%)</td><td>1451.64 (+12.99%)</td><td>1018.60 (+16.74%)</td><td>469.50 (+17.67%)</td><td>1182.34 (-6.84%)</td><td>178.67 (-15.03%)</td><td>94.44 (-12.34%)</td><td>82.35 (-14.35%)</td><td>25.12 (+5.61%)</td><td>64.26 (-4.02%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.89 (n/a)</td><td>0.97 (n/a)</td><td>0.86 (n/a)</td><td>0.21 (n/a)</td><td>0.60 (n/a)</td><td>3527.30 (n/a)</td><td>1284.80 (n/a)</td><td>872.50 (n/a)</td><td>399.00 (n/a)</td><td>1269.09 (n/a)</td><td>210.26 (n/a)</td><td>107.74 (n/a)</td><td>96.15 (n/a)</td><td>23.78 (n/a)</td><td>66.95 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.50 <b>(-21.79%)</b></td><td>1.12 (-14.38%)</td><td>1.20 (+2.50%)</td><td>0.49 <b>(-54.92%)</b></td><td>0.38 (+9.82%)</td><td>2124.70 <b>(+121.81%)</b></td><td>1089.72 <b>(+30.37%)</b></td><td>872.00 (-2.44%)</td><td>697.10 <b>(+27.86%)</b></td><td>585.42 <b>(+254.75%)</b></td><td>192.53 <b>(-21.79%)</b></td><td>143.43 (-14.38%)</td><td>153.91 (+2.50%)</td><td>63.17 <b>(-54.92%)</b></td><td>48.53 (+9.82%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.92 (n/a)</td><td>1.31 (n/a)</td><td>1.17 (n/a)</td><td>1.09 (n/a)</td><td>0.35 (n/a)</td><td>957.90 (n/a)</td><td>835.88 (n/a)</td><td>893.80 (n/a)</td><td>545.20 (n/a)</td><td>165.02 (n/a)</td><td>246.16 (n/a)</td><td>167.53 (n/a)</td><td>150.16 (n/a)</td><td>140.12 (n/a)</td><td>44.19 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.78 (-19.57%)</td><td>1.25 (-12.16%)</td><td>1.30 (-3.52%)</td><td>0.57 <b>(-46.01%)</b></td><td>0.46 (-1.66%)</td><td>1829.20 <b>(+85.22%)</b></td><td>977.10 <b>(+23.77%)</b></td><td>803.70 (+3.65%)</td><td>588.40 <b>(+24.34%)</b></td><td>497.94 <b>(+138.03%)</b></td><td>228.10 (-19.57%)</td><td>160.26 (-12.16%)</td><td>167.01 (-3.52%)</td><td>73.38 <b>(-46.01%)</b></td><td>59.10 (-1.66%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.22 (n/a)</td><td>1.43 (n/a)</td><td>1.35 (n/a)</td><td>1.06 (n/a)</td><td>0.47 (n/a)</td><td>987.60 (n/a)</td><td>789.48 (n/a)</td><td>775.40 (n/a)</td><td>473.20 (n/a)</td><td>209.19 (n/a)</td><td>283.61 (n/a)</td><td>182.44 (n/a)</td><td>173.10 (n/a)</td><td>135.91 (n/a)</td><td>60.10 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.94 (-12.82%)</td><td>1.38 (-10.81%)</td><td>1.39 (+5.83%)</td><td>0.64 <b>(-41.99%)</b></td><td>0.48 (+4.14%)</td><td>1650.20 <b>(+72.38%)</b></td><td>877.28 <b>(+21.28%)</b></td><td>755.80 (-5.51%)</td><td>541.80 (+14.72%)</td><td>441.99 <b>(+128.24%)</b></td><td>247.73 (-12.82%)</td><td>176.47 (-10.81%)</td><td>177.59 (+5.83%)</td><td>81.33 <b>(-41.99%)</b></td><td>60.93 (+4.14%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.22 (n/a)</td><td>1.55 (n/a)</td><td>1.31 (n/a)</td><td>1.10 (n/a)</td><td>0.46 (n/a)</td><td>957.30 (n/a)</td><td>723.36 (n/a)</td><td>799.90 (n/a)</td><td>472.30 (n/a)</td><td>193.65 (n/a)</td><td>284.16 (n/a)</td><td>197.86 (n/a)</td><td>167.80 (n/a)</td><td>140.21 (n/a)</td><td>58.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_512-epilogue_sigmoid-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.65 (-19.71%)</td><td>1.45 (+19.48%)</td><td>1.55 <b>(+57.53%)</b></td><td>1.19 <b>(+52.05%)</b></td><td>0.20 <b>(-60.05%)</b></td><td>881.80 <b>(-34.23%)</b></td><td>733.08 <b>(-23.73%)</b></td><td>678.10 <b>(-36.52%)</b></td><td>634.40 <b>(+24.56%)</b></td><td>107.35 <b>(-65.69%)</b></td><td>211.58 (-19.71%)</td><td>186.09 (+19.48%)</td><td>197.92 <b>(+57.53%)</b></td><td>152.21 <b>(+52.04%)</b></td><td>25.73 <b>(-60.05%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.06 (n/a)</td><td>1.22 (n/a)</td><td>0.98 (n/a)</td><td>0.78 (n/a)</td><td>0.50 (n/a)</td><td>1340.80 (n/a)</td><td>961.16 (n/a)</td><td>1068.20 (n/a)</td><td>509.30 (n/a)</td><td>312.91 (n/a)</td><td>263.52 (n/a)</td><td>155.76 (n/a)</td><td>125.65 (n/a)</td><td>100.11 (n/a)</td><td>64.41 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.63 (-16.44%)</td><td>1.26 (-2.61%)</td><td>1.46 <b>(+21.06%)</b></td><td>0.48 (-0.23%)</td><td>0.47 (-15.05%)</td><td>2193.40 (+0.23%)</td><td>1025.88 (+0.20%)</td><td>718.40 (-17.39%)</td><td>643.70 (+19.69%)</td><td>660.11 (-1.08%)</td><td>208.53 (-16.44%)</td><td>160.95 (-2.61%)</td><td>186.84 <b>(+21.06%)</b></td><td>61.19 (-0.23%)</td><td>60.13 (-15.05%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.95 (n/a)</td><td>1.29 (n/a)</td><td>1.21 (n/a)</td><td>0.48 (n/a)</td><td>0.55 (n/a)</td><td>2188.40 (n/a)</td><td>1023.80 (n/a)</td><td>869.60 (n/a)</td><td>537.80 (n/a)</td><td>667.32 (n/a)</td><td>249.55 (n/a)</td><td>165.25 (n/a)</td><td>154.34 (n/a)</td><td>61.33 (n/a)</td><td>70.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_floor]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.47 <b>(-20.92%)</b></td><td>1.25 (+18.76%)</td><td>1.21 <b>(+59.62%)</b></td><td>1.16 <b>(+102.90%)</b></td><td>0.13 <b>(-76.39%)</b></td><td>903.80 <b>(-50.71%)</b></td><td>843.86 <b>(-30.00%)</b></td><td>865.30 <b>(-37.35%)</b></td><td>711.90 <b>(+26.45%)</b></td><td>78.70 <b>(-85.07%)</b></td><td>188.54 <b>(-20.92%)</b></td><td>160.28 (+18.75%)</td><td>155.11 <b>(+59.62%)</b></td><td>148.50 <b>(+102.90%)</b></td><td>16.52 <b>(-76.39%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.86 (n/a)</td><td>1.05 (n/a)</td><td>0.76 (n/a)</td><td>0.57 (n/a)</td><td>0.55 (n/a)</td><td>1833.80 (n/a)</td><td>1205.50 (n/a)</td><td>1381.20 (n/a)</td><td>563.00 (n/a)</td><td>527.27 (n/a)</td><td>238.41 (n/a)</td><td>134.97 (n/a)</td><td>97.17 (n/a)</td><td>73.19 (n/a)</td><td>70.00 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.85 <b>(-36.98%)</b></td><td>0.59 <b>(-22.03%)</b></td><td>0.54 (-14.79%)</td><td>0.39 <b>(-27.42%)</b></td><td>0.19 <b>(-43.78%)</b></td><td>914.20 <b>(+37.76%)</b></td><td>666.12 <b>(+24.81%)</b></td><td>663.40 (+17.37%)</td><td>426.00 <b>(+58.66%)</b></td><td>202.58 <b>(+31.74%)</b></td><td>39.38 <b>(-36.98%)</b></td><td>27.26 <b>(-22.03%)</b></td><td>25.29 (-14.79%)</td><td>18.35 <b>(-27.42%)</b></td><td>8.71 <b>(-43.78%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.34 (n/a)</td><td>0.75 (n/a)</td><td>0.64 (n/a)</td><td>0.54 (n/a)</td><td>0.33 (n/a)</td><td>663.60 (n/a)</td><td>533.72 (n/a)</td><td>565.20 (n/a)</td><td>268.50 (n/a)</td><td>153.78 (n/a)</td><td>62.48 (n/a)</td><td>34.97 (n/a)</td><td>29.68 (n/a)</td><td>25.28 (n/a)</td><td>15.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_512-K_1024-N_1024-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>2.97 (-6.55%)</td><td>2.23 (-14.26%)</td><td>2.54 (-10.25%)</td><td>1.37 <b>(-28.99%)</b></td><td>0.70 <b>(+21.34%)</b></td><td>3061.60 <b>(+40.83%)</b></td><td>2062.16 <b>(+22.47%)</b></td><td>1648.80 (+11.42%)</td><td>1411.30 (+7.01%)</td><td>728.27 <b>(+82.28%)</b></td><td>760.81 (-6.55%)</td><td>570.68 (-14.26%)</td><td>651.21 (-10.25%)</td><td>350.72 <b>(-28.99%)</b></td><td>178.86 <b>(+21.34%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.18 (n/a)</td><td>2.60 (n/a)</td><td>2.83 (n/a)</td><td>1.93 (n/a)</td><td>0.58 (n/a)</td><td>2173.90 (n/a)</td><td>1683.80 (n/a)</td><td>1479.80 (n/a)</td><td>1318.90 (n/a)</td><td>399.54 (n/a)</td><td>814.14 (n/a)</td><td>665.58 (n/a)</td><td>725.60 (n/a)</td><td>493.91 (n/a)</td><td>147.40 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.94 (-19.31%)</td><td>3.15 (+7.02%)</td><td>3.51 (+7.35%)</td><td>1.09 <b>(+47.91%)</b></td><td>1.19 <b>(-21.87%)</b></td><td>2412.20 <b>(-32.39%)</b></td><td>1058.22 <b>(-21.73%)</b></td><td>746.30 (-6.85%)</td><td>664.50 <b>(+23.93%)</b></td><td>759.12 <b>(-39.46%)</b></td><td>807.92 (-19.31%)</td><td>645.08 (+7.02%)</td><td>719.36 (+7.35%)</td><td>222.56 <b>(+47.91%)</b></td><td>243.50 <b>(-21.87%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>4.89 (n/a)</td><td>2.94 (n/a)</td><td>3.27 (n/a)</td><td>0.73 (n/a)</td><td>1.52 (n/a)</td><td>3567.80 (n/a)</td><td>1352.08 (n/a)</td><td>801.20 (n/a)</td><td>536.20 (n/a)</td><td>1253.86 (n/a)</td><td>1001.23 (n/a)</td><td>602.75 (n/a)</td><td>670.09 (n/a)</td><td>150.48 (n/a)</td><td>311.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_512-K_1536-N_1536-epilogue_silu-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.15 (-8.06%)</td><td>2.44 (-11.43%)</td><td>2.05 <b>(-30.58%)</b></td><td>2.03 <b>(+27.92%)</b></td><td>0.56 <b>(-22.18%)</b></td><td>3883.40 <b>(-21.83%)</b></td><td>3350.28 (+8.90%)</td><td>3843.80 <b>(+44.05%)</b></td><td>2496.30 (+8.77%)</td><td>706.22 <b>(-35.18%)</b></td><td>967.78 (-8.06%)</td><td>750.16 (-11.43%)</td><td>628.52 <b>(-30.58%)</b></td><td>622.12 <b>(+27.92%)</b></td><td>172.41 <b>(-22.18%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.43 (n/a)</td><td>2.76 (n/a)</td><td>2.95 (n/a)</td><td>1.58 (n/a)</td><td>0.72 (n/a)</td><td>4967.80 (n/a)</td><td>3076.40 (n/a)</td><td>2668.30 (n/a)</td><td>2295.10 (n/a)</td><td>1089.49 (n/a)</td><td>1052.65 (n/a)</td><td>847.00 (n/a)</td><td>905.40 (n/a)</td><td>486.32 (n/a)</td><td>221.56 (n/a)</td>
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


### test_gemm_tile_options[tn128-ma16]

_No metrics available._


### test_gemm_tile_options[tn128-ma32]

_No metrics available._


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn16-ma16]

_No metrics available._


### test_gemm_tile_options[tn16-ma32]

_No metrics available._


### test_gemm_tile_options[tn16-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn32-ma16]

_No metrics available._


### test_gemm_tile_options[tn32-ma32]

_No metrics available._


### test_gemm_tile_options[tn32-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma16-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma32]

_No metrics available._


</details>


<details>
<summary>iron/operators/gelu</summary>


### test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>354.20 (n/a)</td><td>251.92 (n/a)</td><td>235.00 (n/a)</td><td>192.50 (n/a)</td><td>60.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>876.80 (n/a)</td><td>442.98 (n/a)</td><td>358.80 (n/a)</td><td>242.30 (n/a)</td><td>249.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.50 (n/a)</td><td>336.40 (n/a)</td><td>298.30 (n/a)</td><td>226.70 (n/a)</td><td>126.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>620.70 (n/a)</td><td>419.80 (n/a)</td><td>371.60 (n/a)</td><td>243.80 (n/a)</td><td>180.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>412.20 (n/a)</td><td>326.38 (n/a)</td><td>312.50 (n/a)</td><td>238.90 (n/a)</td><td>73.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.90 (n/a)</td><td>492.22 (n/a)</td><td>496.50 (n/a)</td><td>411.90 (n/a)</td><td>73.05 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.20 (n/a)</td><td>387.86 (n/a)</td><td>346.10 (n/a)</td><td>255.10 (n/a)</td><td>122.72 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.50 (n/a)</td><td>348.42 (n/a)</td><td>296.40 (n/a)</td><td>224.20 (n/a)</td><td>114.66 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>489.90 (n/a)</td><td>349.74 (n/a)</td><td>309.30 (n/a)</td><td>283.80 (n/a)</td><td>87.56 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.50 (n/a)</td><td>346.86 (n/a)</td><td>314.10 (n/a)</td><td>249.60 (n/a)</td><td>116.17 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1299.00 (n/a)</td><td>599.02 (n/a)</td><td>493.20 (n/a)</td><td>226.50 (n/a)</td><td>408.47 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1374.80 (n/a)</td><td>611.32 (n/a)</td><td>429.70 (n/a)</td><td>360.60 (n/a)</td><td>428.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>567.40 (n/a)</td><td>430.06 (n/a)</td><td>399.90 (n/a)</td><td>306.50 (n/a)</td><td>127.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>431.90 (n/a)</td><td>325.76 (n/a)</td><td>284.80 (n/a)</td><td>278.10 (n/a)</td><td>66.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>527.00 (n/a)</td><td>439.26 (n/a)</td><td>488.50 (n/a)</td><td>238.40 (n/a)</td><td>119.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>461.40 (n/a)</td><td>285.52 (n/a)</td><td>243.30 (n/a)</td><td>210.50 (n/a)</td><td>101.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>486.00 (n/a)</td><td>327.90 (n/a)</td><td>244.30 (n/a)</td><td>236.90 (n/a)</td><td>121.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>602.20 (n/a)</td><td>405.44 (n/a)</td><td>367.10 (n/a)</td><td>252.60 (n/a)</td><td>143.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>570.90 (n/a)</td><td>463.94 (n/a)</td><td>560.90 (n/a)</td><td>267.20 (n/a)</td><td>143.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>642.10 (n/a)</td><td>426.30 (n/a)</td><td>454.20 (n/a)</td><td>254.40 (n/a)</td><td>148.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>556.00 (n/a)</td><td>441.92 (n/a)</td><td>471.40 (n/a)</td><td>316.20 (n/a)</td><td>98.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2411.00 (n/a)</td><td>815.60 (n/a)</td><td>463.60 (n/a)</td><td>231.40 (n/a)</td><td>907.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>564.00 (n/a)</td><td>482.70 (n/a)</td><td>524.10 (n/a)</td><td>289.60 (n/a)</td><td>112.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>670.90 (n/a)</td><td>473.90 (n/a)</td><td>451.30 (n/a)</td><td>350.80 (n/a)</td><td>125.81 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.53 <b>(-31.76%)</b></td><td>0.49 (+13.38%)</td><td>0.51 <b>(+46.80%)</b></td><td>0.44 <b>(+35.90%)</b></td><td>0.04 <b>(-77.70%)</b></td><td>502.50 <b>(-26.42%)</b></td><td>456.70 <b>(-20.22%)</b></td><td>430.60 <b>(-31.88%)</b></td><td>420.30 <b>(+46.55%)</b></td><td>41.27 <b>(-74.73%)</b></td><td>22.46 <b>(-31.76%)</b></td><td>20.80 (+13.38%)</td><td>21.92 <b>(+46.80%)</b></td><td>18.78 <b>(+35.90%)</b></td><td>1.82 <b>(-77.70%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.77 (n/a)</td><td>0.43 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.19 (n/a)</td><td>682.90 (n/a)</td><td>572.46 (n/a)</td><td>632.10 (n/a)</td><td>286.80 (n/a)</td><td>163.31 (n/a)</td><td>32.91 (n/a)</td><td>18.34 (n/a)</td><td>14.93 (n/a)</td><td>13.82 (n/a)</td><td>8.18 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.63 (+4.14%)</td><td>0.48 (+11.57%)</td><td>0.45 (-16.68%)</td><td>0.39 <b>(+226.22%)</b></td><td>0.11 <b>(-48.20%)</b></td><td>571.00 <b>(-69.35%)</b></td><td>476.26 <b>(-35.53%)</b></td><td>494.00 <b>(+20.02%)</b></td><td>353.60 (-3.99%)</td><td>97.87 <b>(-84.69%)</b></td><td>26.69 (+4.14%)</td><td>20.55 (+11.57%)</td><td>19.10 (-16.68%)</td><td>16.53 <b>(+226.22%)</b></td><td>4.49 <b>(-48.20%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.60 (n/a)</td><td>0.43 (n/a)</td><td>0.54 (n/a)</td><td>0.12 (n/a)</td><td>0.20 (n/a)</td><td>1862.80 (n/a)</td><td>738.72 (n/a)</td><td>411.60 (n/a)</td><td>368.30 (n/a)</td><td>639.39 (n/a)</td><td>25.62 (n/a)</td><td>18.42 (n/a)</td><td>22.93 (n/a)</td><td>5.07 (n/a)</td><td>8.67 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.31 (+0.07%)</td><td>0.30 (-0.89%)</td><td>0.30 (-1.42%)</td><td>0.30 (-1.11%)</td><td>0.00 <b>(+51.11%)</b></td><td>84090.70 (+1.13%)</td><td>82995.22 (+0.91%)</td><td>83276.80 (+1.44%)</td><td>81400.40 (-0.07%)</td><td>1136.93 <b>(+52.78%)</b></td><td>211.05 (+0.07%)</td><td>207.03 (-0.89%)</td><td>206.30 (-1.42%)</td><td>204.30 (-1.11%)</td><td>2.85 <b>(+51.11%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83155.10 (n/a)</td><td>82246.44 (n/a)</td><td>82090.90 (n/a)</td><td>81459.60 (n/a)</td><td>744.18 (n/a)</td><td>210.90 (n/a)</td><td>208.90 (n/a)</td><td>209.28 (n/a)</td><td>206.60 (n/a)</td><td>1.89 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.13 (-1.48%)</td><td>1.09 (-0.20%)</td><td>1.10 (-3.48%)</td><td>1.02 (+5.87%)</td><td>0.05 <b>(-41.52%)</b></td><td>24708.40 (-5.54%)</td><td>23168.98 (-0.12%)</td><td>22919.30 (+3.60%)</td><td>22245.10 (+1.51%)</td><td>1038.39 <b>(-43.75%)</b></td><td>772.30 (-1.48%)</td><td>742.67 (-0.20%)</td><td>749.58 (-3.48%)</td><td>695.31 (+5.87%)</td><td>32.58 <b>(-41.52%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.15 (n/a)</td><td>1.09 (n/a)</td><td>1.14 (n/a)</td><td>0.96 (n/a)</td><td>0.08 (n/a)</td><td>26158.20 (n/a)</td><td>23197.62 (n/a)</td><td>22122.50 (n/a)</td><td>21914.80 (n/a)</td><td>1845.91 (n/a)</td><td>783.94 (n/a)</td><td>744.13 (n/a)</td><td>776.58 (n/a)</td><td>656.77 (n/a)</td><td>55.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.81 (+0.75%)</td><td>0.80 (+1.38%)</td><td>0.80 (+1.92%)</td><td>0.78 (+0.96%)</td><td>0.01 (+0.42%)</td><td>96780.20 (-0.95%)</td><td>94969.30 (-1.37%)</td><td>94727.40 (-1.88%)</td><td>93635.00 (-0.74%)</td><td>1300.23 (-1.24%)</td><td>733.91 (+0.75%)</td><td>723.70 (+1.38%)</td><td>725.44 (+1.92%)</td><td>710.06 (+0.96%)</td><td>9.86 (+0.42%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>97712.50 (n/a)</td><td>96284.34 (n/a)</td><td>96542.10 (n/a)</td><td>94333.50 (n/a)</td><td>1316.49 (n/a)</td><td>728.47 (n/a)</td><td>713.82 (n/a)</td><td>711.81 (n/a)</td><td>703.28 (n/a)</td><td>9.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.78 (+1.09%)</td><td>0.76 (-0.60%)</td><td>0.77 (+0.54%)</td><td>0.74 (-3.49%)</td><td>0.02 <b>(+372.13%)</b></td><td>102705.60 (+3.62%)</td><td>99098.36 (+0.66%)</td><td>97850.40 (-0.54%)</td><td>96699.00 (-1.08%)</td><td>2522.96 <b>(+384.04%)</b></td><td>710.65 (+1.09%)</td><td>693.80 (-0.60%)</td><td>702.29 (+0.54%)</td><td>669.09 (-3.49%)</td><td>17.45 <b>(+372.13%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.00 (n/a)</td><td>99119.30 (n/a)</td><td>98451.18 (n/a)</td><td>98381.00 (n/a)</td><td>97754.10 (n/a)</td><td>521.23 (n/a)</td><td>702.98 (n/a)</td><td>698.02 (n/a)</td><td>698.50 (n/a)</td><td>693.30 (n/a)</td><td>3.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.90 (+0.17%)</td><td>0.89 (+0.18%)</td><td>0.89 (-0.14%)</td><td>0.88 (+0.72%)</td><td>0.01 <b>(-20.42%)</b></td><td>86043.90 (-0.71%)</td><td>85001.58 (-0.19%)</td><td>85001.20 (+0.15%)</td><td>84047.50 (-0.17%)</td><td>770.79 <b>(-21.17%)</b></td><td>817.63 (+0.17%)</td><td>808.50 (+0.18%)</td><td>808.45 (-0.14%)</td><td>798.66 (+0.72%)</td><td>7.32 <b>(-20.42%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>86660.70 (n/a)</td><td>85159.36 (n/a)</td><td>84878.10 (n/a)</td><td>84187.00 (n/a)</td><td>977.78 (n/a)</td><td>816.27 (n/a)</td><td>807.04 (n/a)</td><td>809.63 (n/a)</td><td>792.97 (n/a)</td><td>9.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.93 (+8.75%)</td><td>3.24 (+11.32%)</td><td>2.80 (+19.23%)</td><td>2.19 (+19.30%)</td><td>1.21 (+6.28%)</td><td>4072.30 (-16.18%)</td><td>3054.02 (-10.92%)</td><td>3177.50 (-16.13%)</td><td>1806.60 (-8.05%)</td><td>1033.04 (-13.69%)</td><td>297.17 (+8.75%)</td><td>195.19 (+11.32%)</td><td>168.96 (+19.23%)</td><td>131.83 (+19.30%)</td><td>72.98 (+6.28%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>4.54 (n/a)</td><td>2.91 (n/a)</td><td>2.35 (n/a)</td><td>1.83 (n/a)</td><td>1.14 (n/a)</td><td>4858.30 (n/a)</td><td>3428.56 (n/a)</td><td>3788.50 (n/a)</td><td>1964.70 (n/a)</td><td>1196.95 (n/a)</td><td>273.25 (n/a)</td><td>175.34 (n/a)</td><td>141.71 (n/a)</td><td>110.51 (n/a)</td><td>68.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.16 (-11.73%)</td><td>2.90 (-14.96%)</td><td>2.86 (-18.08%)</td><td>2.06 (-6.71%)</td><td>0.78 <b>(-31.84%)</b></td><td>4324.20 (+7.20%)</td><td>3244.38 (+12.34%)</td><td>3121.10 <b>(+22.08%)</b></td><td>2144.20 (+13.29%)</td><td>796.52 <b>(-21.78%)</b></td><td>250.38 (-11.73%)</td><td>174.47 (-14.96%)</td><td>172.01 (-18.08%)</td><td>124.15 (-6.71%)</td><td>47.16 <b>(-31.84%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>4.71 (n/a)</td><td>3.41 (n/a)</td><td>3.49 (n/a)</td><td>2.21 (n/a)</td><td>1.15 (n/a)</td><td>4033.90 (n/a)</td><td>2888.12 (n/a)</td><td>2556.70 (n/a)</td><td>1892.70 (n/a)</td><td>1018.24 (n/a)</td><td>283.65 (n/a)</td><td>205.17 (n/a)</td><td>209.99 (n/a)</td><td>133.09 (n/a)</td><td>69.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>5.67 (+4.09%)</td><td>3.91 <b>(+21.16%)</b></td><td>3.74 <b>(+67.91%)</b></td><td>2.10 (+2.90%)</td><td>1.59 (+4.80%)</td><td>4243.30 (-2.82%)</td><td>2644.70 (-18.07%)</td><td>2384.20 <b>(-40.45%)</b></td><td>1571.20 (-3.93%)</td><td>1148.65 (-8.04%)</td><td>341.69 (+4.09%)</td><td>235.39 <b>(+21.16%)</b></td><td>225.18 <b>(+67.91%)</b></td><td>126.52 (+2.90%)</td><td>96.07 (+4.80%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>5.45 (n/a)</td><td>3.23 (n/a)</td><td>2.23 (n/a)</td><td>2.04 (n/a)</td><td>1.52 (n/a)</td><td>4366.50 (n/a)</td><td>3227.96 (n/a)</td><td>4003.40 (n/a)</td><td>1635.40 (n/a)</td><td>1249.05 (n/a)</td><td>328.27 (n/a)</td><td>194.28 (n/a)</td><td>134.10 (n/a)</td><td>122.95 (n/a)</td><td>91.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>6.72 (+5.91%)</td><td>5.63 (+8.10%)</td><td>5.67 (+16.47%)</td><td>4.58 (+0.72%)</td><td>0.86 (+10.97%)</td><td>7612.70 (-0.72%)</td><td>6311.52 (-7.27%)</td><td>6153.50 (-14.14%)</td><td>5191.50 (-5.58%)</td><td>977.64 (+3.50%)</td><td>413.65 (+5.91%)</td><td>346.77 (+8.10%)</td><td>348.99 (+16.47%)</td><td>282.09 (+0.72%)</td><td>52.95 (+10.97%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>6.34 (n/a)</td><td>5.21 (n/a)</td><td>4.86 (n/a)</td><td>4.55 (n/a)</td><td>0.77 (n/a)</td><td>7667.90 (n/a)</td><td>6806.66 (n/a)</td><td>7166.90 (n/a)</td><td>5498.10 (n/a)</td><td>944.56 (n/a)</td><td>390.58 (n/a)</td><td>320.78 (n/a)</td><td>299.64 (n/a)</td><td>280.06 (n/a)</td><td>47.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>5.64 (+3.42%)</td><td>4.75 (-11.27%)</td><td>4.58 (-14.47%)</td><td>4.01 <b>(-23.90%)</b></td><td>0.62 <b>(+811.50%)</b></td><td>8696.30 <b>(+31.41%)</b></td><td>7435.70 (+14.18%)</td><td>7605.60 (+16.92%)</td><td>6182.70 (-3.31%)</td><td>945.98 <b>(+1050.85%)</b></td><td>347.34 (+3.42%)</td><td>292.65 (-11.27%)</td><td>282.35 (-14.47%)</td><td>246.94 <b>(-23.90%)</b></td><td>38.03 <b>(+811.49%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>5.45 (n/a)</td><td>5.35 (n/a)</td><td>5.36 (n/a)</td><td>5.27 (n/a)</td><td>0.07 (n/a)</td><td>6617.90 (n/a)</td><td>6512.14 (n/a)</td><td>6505.00 (n/a)</td><td>6394.20 (n/a)</td><td>82.20 (n/a)</td><td>335.85 (n/a)</td><td>329.81 (n/a)</td><td>330.13 (n/a)</td><td>324.50 (n/a)</td><td>4.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>6.03 (-12.70%)</td><td>5.20 (-9.46%)</td><td>4.93 (-5.78%)</td><td>4.40 (-3.89%)</td><td>0.66 <b>(-35.81%)</b></td><td>7926.10 (+4.04%)</td><td>6793.98 (+9.05%)</td><td>7065.40 (+6.13%)</td><td>5781.30 (+14.55%)</td><td>862.02 <b>(-21.77%)</b></td><td>371.45 (-12.70%)</td><td>320.22 (-9.46%)</td><td>303.94 (-5.78%)</td><td>270.94 (-3.89%)</td><td>40.89 <b>(-35.81%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>6.91 (n/a)</td><td>5.74 (n/a)</td><td>5.24 (n/a)</td><td>4.58 (n/a)</td><td>1.03 (n/a)</td><td>7618.10 (n/a)</td><td>6229.96 (n/a)</td><td>6657.10 (n/a)</td><td>5047.10 (n/a)</td><td>1101.85 (n/a)</td><td>425.48 (n/a)</td><td>353.67 (n/a)</td><td>322.58 (n/a)</td><td>281.89 (n/a)</td><td>63.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.78 (-0.07%)</td><td>0.75 (-1.93%)</td><td>0.75 (-2.53%)</td><td>0.74 (-3.01%)</td><td>0.01 <b>(+201.21%)</b></td><td>101718.30 (+3.10%)</td><td>100051.90 (+2.00%)</td><td>100828.30 (+2.59%)</td><td>97359.70 (+0.07%)</td><td>1901.08 <b>(+211.03%)</b></td><td>705.83 (-0.07%)</td><td>687.04 (-1.93%)</td><td>681.55 (-2.53%)</td><td>675.59 (-3.01%)</td><td>13.17 <b>(+201.21%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.00 (n/a)</td><td>98656.40 (n/a)</td><td>98093.26 (n/a)</td><td>98280.60 (n/a)</td><td>97294.90 (n/a)</td><td>611.22 (n/a)</td><td>706.30 (n/a)</td><td>700.57 (n/a)</td><td>699.22 (n/a)</td><td>696.55 (n/a)</td><td>4.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.76 (-1.43%)</td><td>0.74 (-1.93%)</td><td>0.76 (-0.07%)</td><td>0.72 (-4.80%)</td><td>0.02 <b>(+183.72%)</b></td><td>105182.50 (+5.04%)</td><td>101480.32 (+2.02%)</td><td>99857.70 (+0.07%)</td><td>99397.90 (+1.45%)</td><td>2636.13 <b>(+201.89%)</b></td><td>691.36 (-1.43%)</td><td>677.53 (-1.93%)</td><td>688.17 (-0.07%)</td><td>653.34 (-4.80%)</td><td>17.37 <b>(+183.72%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100133.00 (n/a)</td><td>99469.94 (n/a)</td><td>99786.10 (n/a)</td><td>97977.70 (n/a)</td><td>873.20 (n/a)</td><td>701.38 (n/a)</td><td>690.90 (n/a)</td><td>688.67 (n/a)</td><td>686.28 (n/a)</td><td>6.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.89 (-0.05%)</td><td>0.89 (+0.50%)</td><td>0.89 (+1.16%)</td><td>0.87 (-0.83%)</td><td>0.01 <b>(+34.33%)</b></td><td>86824.70 (+0.83%)</td><td>85211.06 (-0.49%)</td><td>85028.10 (-1.15%)</td><td>84425.80 (+0.05%)</td><td>978.59 <b>(+35.64%)</b></td><td>813.96 (-0.05%)</td><td>806.55 (+0.50%)</td><td>808.20 (+1.16%)</td><td>791.47 (-0.83%)</td><td>9.17 <b>(+34.33%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>86107.20 (n/a)</td><td>85634.62 (n/a)</td><td>86018.60 (n/a)</td><td>84386.30 (n/a)</td><td>721.46 (n/a)</td><td>814.34 (n/a)</td><td>802.52 (n/a)</td><td>798.89 (n/a)</td><td>798.07 (n/a)</td><td>6.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.56 (-4.17%)</td><td>2.54 (-9.35%)</td><td>2.31 <b>(-23.52%)</b></td><td>1.58 (-7.13%)</td><td>0.96 (+17.49%)</td><td>5109.60 (+7.68%)</td><td>3569.08 (+14.46%)</td><td>3495.40 <b>(+30.74%)</b></td><td>2261.80 (+4.36%)</td><td>1324.98 <b>(+25.73%)</b></td><td>934.63 (-4.17%)</td><td>666.00 (-9.35%)</td><td>604.77 <b>(-23.52%)</b></td><td>413.72 (-7.13%)</td><td>252.14 (+17.49%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.72 (n/a)</td><td>2.80 (n/a)</td><td>3.02 (n/a)</td><td>1.70 (n/a)</td><td>0.82 (n/a)</td><td>4745.30 (n/a)</td><td>3118.26 (n/a)</td><td>2673.50 (n/a)</td><td>2167.40 (n/a)</td><td>1053.85 (n/a)</td><td>975.32 (n/a)</td><td>734.73 (n/a)</td><td>790.70 (n/a)</td><td>445.48 (n/a)</td><td>214.61 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.21 (-10.88%)</td><td>0.19 (-0.27%)</td><td>0.19 (+3.55%)</td><td>0.16 (-1.66%)</td><td>0.02 <b>(-35.85%)</b></td><td>7601.10 (+1.69%)</td><td>6483.00 (-0.58%)</td><td>6405.90 (-3.43%)</td><td>5884.60 (+12.20%)</td><td>667.33 <b>(-25.75%)</b></td><td>11.40 (-10.88%)</td><td>10.43 (-0.27%)</td><td>10.48 (+3.55%)</td><td>8.83 (-1.66%)</td><td>0.99 <b>(-35.85%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>7474.70 (n/a)</td><td>6520.52 (n/a)</td><td>6633.40 (n/a)</td><td>5244.60 (n/a)</td><td>898.74 (n/a)</td><td>12.80 (n/a)</td><td>10.46 (n/a)</td><td>10.12 (n/a)</td><td>8.98 (n/a)</td><td>1.54 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.92 (n/a)</td><td>3.59 (n/a)</td><td>3.60 (n/a)</td><td>3.32 (n/a)</td><td>0.26 (n/a)</td><td>3.92 (n/a)</td><td>3.59 (n/a)</td><td>3.60 (n/a)</td><td>3.31 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>7.59 (+3.82%)</td><td>6.65 (-2.43%)</td><td>6.91 (+0.81%)</td><td>5.69 (-10.94%)</td><td>0.75 <b>(+119.10%)</b></td><td>7.58 (+3.82%)</td><td>6.65 (-2.43%)</td><td>6.90 (+0.81%)</td><td>5.68 (-10.94%)</td><td>0.75 <b>(+119.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>7.31 (n/a)</td><td>6.81 (n/a)</td><td>6.85 (n/a)</td><td>6.38 (n/a)</td><td>0.34 (n/a)</td><td>7.30 (n/a)</td><td>6.81 (n/a)</td><td>6.85 (n/a)</td><td>6.38 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>14.06 (+4.43%)</td><td>11.46 (+4.11%)</td><td>13.55 <b>(+20.79%)</b></td><td>7.36 (-10.44%)</td><td>3.27 <b>(+45.91%)</b></td><td>14.05 (+4.43%)</td><td>11.46 (+4.11%)</td><td>13.54 <b>(+20.79%)</b></td><td>7.35 (-10.44%)</td><td>3.27 <b>(+45.91%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>13.46 (n/a)</td><td>11.01 (n/a)</td><td>11.22 (n/a)</td><td>8.22 (n/a)</td><td>2.24 (n/a)</td><td>13.45 (n/a)</td><td>11.00 (n/a)</td><td>11.21 (n/a)</td><td>8.21 (n/a)</td><td>2.24 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.97 (n/a)</td><td>3.69 (n/a)</td><td>3.65 (n/a)</td><td>3.45 (n/a)</td><td>0.25 (n/a)</td><td>3.97 (n/a)</td><td>3.69 (n/a)</td><td>3.64 (n/a)</td><td>3.45 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>7.67 (+9.95%)</td><td>6.84 (+8.41%)</td><td>7.22 (+13.05%)</td><td>5.09 (-9.37%)</td><td>1.02 <b>(+81.61%)</b></td><td>7.66 (+9.95%)</td><td>6.83 (+8.41%)</td><td>7.21 (+13.05%)</td><td>5.09 (-9.37%)</td><td>1.02 <b>(+81.61%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>6.97 (n/a)</td><td>6.31 (n/a)</td><td>6.38 (n/a)</td><td>5.62 (n/a)</td><td>0.56 (n/a)</td><td>6.97 (n/a)</td><td>6.30 (n/a)</td><td>6.38 (n/a)</td><td>5.62 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>9.96 <b>(-29.14%)</b></td><td>8.77 (-9.37%)</td><td>8.75 (+6.88%)</td><td>7.68 (+0.71%)</td><td>0.93 <b>(-65.78%)</b></td><td>9.96 <b>(-29.14%)</b></td><td>8.76 (-9.37%)</td><td>8.75 (+6.88%)</td><td>7.68 (+0.71%)</td><td>0.93 <b>(-65.78%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>14.06 (n/a)</td><td>9.68 (n/a)</td><td>8.19 (n/a)</td><td>7.63 (n/a)</td><td>2.71 (n/a)</td><td>14.05 (n/a)</td><td>9.67 (n/a)</td><td>8.19 (n/a)</td><td>7.62 (n/a)</td><td>2.71 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.16 (+14.73%)</td><td>2.22 <b>(+33.99%)</b></td><td>2.86 <b>(+143.54%)</b></td><td>1.03 (+1.26%)</td><td>1.08 <b>(+33.20%)</b></td><td>3.15 (+14.73%)</td><td>2.21 <b>(+33.99%)</b></td><td>2.86 <b>(+143.54%)</b></td><td>1.03 (+1.26%)</td><td>1.08 <b>(+33.20%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.75 (n/a)</td><td>1.66 (n/a)</td><td>1.17 (n/a)</td><td>1.02 (n/a)</td><td>0.81 (n/a)</td><td>2.75 (n/a)</td><td>1.65 (n/a)</td><td>1.17 (n/a)</td><td>1.02 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.57 (+11.36%)</td><td>0.42 <b>(+26.99%)</b></td><td>0.52 <b>(+48.64%)</b></td><td>0.14 <b>(+80.58%)</b></td><td>0.19 (+17.45%)</td><td>0.56 (+11.36%)</td><td>0.41 <b>(+26.99%)</b></td><td>0.51 <b>(+48.64%)</b></td><td>0.13 <b>(+80.58%)</b></td><td>0.18 (+17.45%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.51 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>0.16 (n/a)</td><td>0.50 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.78 (+19.74%)</td><td>0.46 (+11.81%)</td><td>0.49 (+11.23%)</td><td>0.08 (-0.64%)</td><td>0.25 (+15.98%)</td><td>0.77 (+19.74%)</td><td>0.46 (+11.81%)</td><td>0.48 (+11.23%)</td><td>0.08 (-0.64%)</td><td>0.25 (+15.98%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.65 (n/a)</td><td>0.41 (n/a)</td><td>0.44 (n/a)</td><td>0.08 (n/a)</td><td>0.22 (n/a)</td><td>0.64 (n/a)</td><td>0.41 (n/a)</td><td>0.43 (n/a)</td><td>0.08 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>2.64 <b>(+36.08%)</b></td><td>1.37 (-0.85%)</td><td>0.85 <b>(-46.63%)</b></td><td>0.78 <b>(+72.30%)</b></td><td>0.82 <b>(+40.03%)</b></td><td>2.59 <b>(+36.08%)</b></td><td>1.35 (-0.85%)</td><td>0.84 <b>(-46.63%)</b></td><td>0.77 <b>(+72.30%)</b></td><td>0.81 <b>(+40.03%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.94 (n/a)</td><td>1.38 (n/a)</td><td>1.59 (n/a)</td><td>0.45 (n/a)</td><td>0.59 (n/a)</td><td>1.91 (n/a)</td><td>1.36 (n/a)</td><td>1.57 (n/a)</td><td>0.45 (n/a)</td><td>0.58 (n/a)</td>
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


### test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>500.10 (n/a)</td><td>363.10 (n/a)</td><td>314.60 (n/a)</td><td>258.10 (n/a)</td><td>107.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>504.90 (n/a)</td><td>367.30 (n/a)</td><td>397.10 (n/a)</td><td>231.90 (n/a)</td><td>122.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>389.10 (n/a)</td><td>287.42 (n/a)</td><td>265.70 (n/a)</td><td>240.60 (n/a)</td><td>59.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.50 (n/a)</td><td>392.26 (n/a)</td><td>354.80 (n/a)</td><td>245.20 (n/a)</td><td>131.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>527.80 (n/a)</td><td>395.84 (n/a)</td><td>359.20 (n/a)</td><td>271.70 (n/a)</td><td>104.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>505.60 (n/a)</td><td>406.52 (n/a)</td><td>408.30 (n/a)</td><td>279.60 (n/a)</td><td>92.90 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>546.10 (n/a)</td><td>391.86 (n/a)</td><td>307.00 (n/a)</td><td>288.20 (n/a)</td><td>130.56 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.00 (n/a)</td><td>436.06 (n/a)</td><td>444.00 (n/a)</td><td>203.20 (n/a)</td><td>185.40 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1899.00 (n/a)</td><td>780.26 (n/a)</td><td>489.00 (n/a)</td><td>285.30 (n/a)</td><td>646.63 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>999.60 (n/a)</td><td>512.64 (n/a)</td><td>453.60 (n/a)</td><td>268.70 (n/a)</td><td>291.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1746.20 (n/a)</td><td>673.40 (n/a)</td><td>430.10 (n/a)</td><td>274.90 (n/a)</td><td>615.97 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.60 (n/a)</td><td>479.50 (n/a)</td><td>548.60 (n/a)</td><td>256.50 (n/a)</td><td>138.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>584.50 (n/a)</td><td>363.50 (n/a)</td><td>310.50 (n/a)</td><td>249.10 (n/a)</td><td>136.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>645.60 (n/a)</td><td>447.08 (n/a)</td><td>382.10 (n/a)</td><td>289.90 (n/a)</td><td>144.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>471.30 (n/a)</td><td>365.32 (n/a)</td><td>313.10 (n/a)</td><td>292.90 (n/a)</td><td>89.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>558.30 (n/a)</td><td>365.54 (n/a)</td><td>303.80 (n/a)</td><td>268.10 (n/a)</td><td>120.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1059.10 (n/a)</td><td>582.70 (n/a)</td><td>494.50 (n/a)</td><td>276.60 (n/a)</td><td>301.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1157.00 (n/a)</td><td>644.18 (n/a)</td><td>466.30 (n/a)</td><td>364.90 (n/a)</td><td>343.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>600.60 (n/a)</td><td>359.68 (n/a)</td><td>284.70 (n/a)</td><td>276.10 (n/a)</td><td>138.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>558.60 (n/a)</td><td>408.76 (n/a)</td><td>387.90 (n/a)</td><td>248.40 (n/a)</td><td>136.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>617.50 (n/a)</td><td>574.10 (n/a)</td><td>609.00 (n/a)</td><td>437.20 (n/a)</td><td>77.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>791.60 (n/a)</td><td>477.10 (n/a)</td><td>426.90 (n/a)</td><td>316.00 (n/a)</td><td>185.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>601.60 (n/a)</td><td>432.18 (n/a)</td><td>459.60 (n/a)</td><td>270.50 (n/a)</td><td>140.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>593.20 (n/a)</td><td>554.72 (n/a)</td><td>546.60 (n/a)</td><td>537.80 (n/a)</td><td>22.54 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/leaky_relu</summary>


### test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (-17.66%)</td><td>0.01 (-0.83%)</td><td>0.01 (+15.20%)</td><td>0.01 (+15.12%)</td><td>0.00 <b>(-52.82%)</b></td><td>459.40 (-13.12%)</td><td>381.02 (-5.23%)</td><td>382.30 (-13.19%)</td><td>298.20 <b>(+21.47%)</b></td><td>58.24 <b>(-50.83%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.80 (n/a)</td><td>402.04 (n/a)</td><td>440.40 (n/a)</td><td>245.50 (n/a)</td><td>118.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (-7.49%)</td><td>0.01 (+11.54%)</td><td>0.01 (+15.59%)</td><td>0.01 (+12.09%)</td><td>0.00 (-12.63%)</td><td>575.40 (-10.79%)</td><td>357.30 (-14.37%)</td><td>276.10 (-13.48%)</td><td>248.30 (+8.10%)</td><td>141.97 <b>(-22.71%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>645.00 (n/a)</td><td>417.28 (n/a)</td><td>319.10 (n/a)</td><td>229.70 (n/a)</td><td>183.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+12.03%)</td><td>0.01 (-14.29%)</td><td>0.01 <b>(-36.38%)</b></td><td>0.01 <b>(+236.83%)</b></td><td>0.00 <b>(-25.12%)</b></td><td>579.80 <b>(-70.31%)</b></td><td>459.60 <b>(-27.18%)</b></td><td>476.70 <b>(+57.17%)</b></td><td>240.90 (-10.74%)</td><td>129.75 <b>(-82.46%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1952.90 (n/a)</td><td>631.14 (n/a)</td><td>303.30 (n/a)</td><td>269.90 (n/a)</td><td>739.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+2.12%)</td><td>0.01 <b>(-25.58%)</b></td><td>0.01 <b>(-44.47%)</b></td><td>0.00 (-7.96%)</td><td>0.01 (-12.64%)</td><td>2427.20 (+8.65%)</td><td>833.92 (+19.87%)</td><td>499.90 <b>(+80.08%)</b></td><td>228.70 (-2.06%)</td><td>899.68 (+3.85%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2234.00 (n/a)</td><td>695.70 (n/a)</td><td>277.60 (n/a)</td><td>233.50 (n/a)</td><td>866.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 <b>(+53.12%)</b></td><td>0.01 (-17.27%)</td><td>0.01 <b>(-42.67%)</b></td><td>0.01 (-5.65%)</td><td>0.01 <b>(+113.94%)</b></td><td>584.80 (+5.98%)</td><td>443.48 <b>(+39.62%)</b></td><td>472.30 <b>(+74.41%)</b></td><td>153.90 <b>(-34.68%)</b></td><td>169.00 <b>(+28.18%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.80 (n/a)</td><td>317.64 (n/a)</td><td>270.80 (n/a)</td><td>235.60 (n/a)</td><td>131.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+17.63%)</td><td>0.01 (-10.12%)</td><td>0.01 <b>(-26.93%)</b></td><td>0.01 (-8.09%)</td><td>0.01 <b>(+31.46%)</b></td><td>677.30 (+8.80%)</td><td>471.84 (+15.65%)</td><td>482.20 <b>(+36.87%)</b></td><td>218.30 (-14.96%)</td><td>165.03 (+9.25%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>622.50 (n/a)</td><td>407.98 (n/a)</td><td>352.30 (n/a)</td><td>256.70 (n/a)</td><td>151.06 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (+8.23%)</td><td>0.02 (-6.69%)</td><td>0.02 (-4.73%)</td><td>0.01 (-7.70%)</td><td>0.01 (+10.94%)</td><td>558.30 (+8.37%)</td><td>393.08 (+10.07%)</td><td>373.20 (+4.95%)</td><td>226.10 (-7.60%)</td><td>141.08 <b>(+21.18%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>515.20 (n/a)</td><td>357.12 (n/a)</td><td>355.60 (n/a)</td><td>244.70 (n/a)</td><td>116.42 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 <b>(+31.60%)</b></td><td>0.03 <b>(+22.77%)</b></td><td>0.03 (+4.61%)</td><td>0.02 <b>(+258.13%)</b></td><td>0.01 (-17.52%)</td><td>537.30 <b>(-72.08%)</b></td><td>310.54 <b>(-49.32%)</b></td><td>274.00 (-4.40%)</td><td>203.40 <b>(-24.02%)</b></td><td>130.82 <b>(-82.16%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1924.20 (n/a)</td><td>612.78 (n/a)</td><td>286.60 (n/a)</td><td>267.70 (n/a)</td><td>733.20 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (-4.39%)</td><td>0.02 (+3.35%)</td><td>0.02 (-3.31%)</td><td>0.01 (+16.52%)</td><td>0.01 (-12.80%)</td><td>645.70 (-14.18%)</td><td>395.34 (-9.41%)</td><td>330.40 (+3.41%)</td><td>244.80 (+4.57%)</td><td>172.04 <b>(-24.82%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>752.40 (n/a)</td><td>436.42 (n/a)</td><td>319.50 (n/a)</td><td>234.10 (n/a)</td><td>228.84 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (+5.16%)</td><td>0.02 (+7.72%)</td><td>0.02 (+7.82%)</td><td>0.02 (+19.77%)</td><td>0.01 (-8.18%)</td><td>493.20 (-16.51%)</td><td>386.86 (-11.00%)</td><td>444.90 (-7.25%)</td><td>228.50 (-4.91%)</td><td>119.20 <b>(-26.84%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.70 (n/a)</td><td>434.66 (n/a)</td><td>479.70 (n/a)</td><td>240.30 (n/a)</td><td>162.92 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (-19.20%)</td><td>0.02 <b>(-22.14%)</b></td><td>0.02 <b>(-26.45%)</b></td><td>0.01 <b>(-25.04%)</b></td><td>0.01 (-15.55%)</td><td>611.50 <b>(+33.40%)</b></td><td>373.50 <b>(+30.24%)</b></td><td>361.90 <b>(+35.95%)</b></td><td>222.80 <b>(+23.71%)</b></td><td>145.16 <b>(+38.81%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>458.40 (n/a)</td><td>286.78 (n/a)</td><td>266.20 (n/a)</td><td>180.10 (n/a)</td><td>104.57 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 <b>(+75.19%)</b></td><td>0.02 <b>(+41.54%)</b></td><td>0.02 (+15.72%)</td><td>0.02 <b>(+21.40%)</b></td><td>0.01 <b>(+344.38%)</b></td><td>491.30 (-17.62%)</td><td>392.36 <b>(-25.19%)</b></td><td>441.40 (-13.57%)</td><td>265.40 <b>(-42.91%)</b></td><td>104.30 <b>(+107.88%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.40 (n/a)</td><td>524.46 (n/a)</td><td>510.70 (n/a)</td><td>464.90 (n/a)</td><td>50.17 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (+5.03%)</td><td>0.02 (-15.55%)</td><td>0.02 (+6.39%)</td><td>0.00 <b>(-74.76%)</b></td><td>0.01 <b>(+42.35%)</b></td><td>2407.90 <b>(+296.23%)</b></td><td>824.24 <b>(+85.82%)</b></td><td>468.60 (-6.00%)</td><td>276.60 (-4.78%)</td><td>890.32 <b>(+555.46%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.70 (n/a)</td><td>443.58 (n/a)</td><td>498.50 (n/a)</td><td>290.50 (n/a)</td><td>135.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (-1.21%)</td><td>0.02 (-4.06%)</td><td>0.02 (-13.21%)</td><td>0.01 (+3.35%)</td><td>0.01 (+3.98%)</td><td>614.20 (-3.25%)</td><td>456.34 (+4.83%)</td><td>523.20 (+15.22%)</td><td>285.80 (+1.24%)</td><td>139.52 (+1.56%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.80 (n/a)</td><td>435.30 (n/a)</td><td>454.10 (n/a)</td><td>282.30 (n/a)</td><td>137.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 <b>(+31.46%)</b></td><td>0.06 (-6.76%)</td><td>0.05 (-13.56%)</td><td>0.03 <b>(-34.49%)</b></td><td>0.02 <b>(+145.84%)</b></td><td>489.60 <b>(+52.67%)</b></td><td>319.22 (+18.30%)</td><td>303.90 (+15.68%)</td><td>168.80 <b>(-23.96%)</b></td><td>115.79 <b>(+173.31%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>320.70 (n/a)</td><td>269.84 (n/a)</td><td>262.70 (n/a)</td><td>222.00 (n/a)</td><td>42.37 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 <b>(-21.90%)</b></td><td>0.04 <b>(-24.82%)</b></td><td>0.04 <b>(-24.01%)</b></td><td>0.03 <b>(-30.60%)</b></td><td>0.01 (-8.64%)</td><td>646.20 <b>(+44.08%)</b></td><td>411.54 <b>(+36.58%)</b></td><td>375.60 <b>(+31.60%)</b></td><td>293.20 <b>(+28.03%)</b></td><td>144.14 <b>(+64.13%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>448.50 (n/a)</td><td>301.32 (n/a)</td><td>285.40 (n/a)</td><td>229.00 (n/a)</td><td>87.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (+4.23%)</td><td>0.04 <b>(-23.69%)</b></td><td>0.03 <b>(-36.23%)</b></td><td>0.03 <b>(-32.89%)</b></td><td>0.02 <b>(+64.15%)</b></td><td>603.90 <b>(+49.00%)</b></td><td>458.66 <b>(+41.84%)</b></td><td>475.80 <b>(+56.82%)</b></td><td>231.10 (-4.07%)</td><td>141.69 <b>(+118.05%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>405.30 (n/a)</td><td>323.36 (n/a)</td><td>303.40 (n/a)</td><td>240.90 (n/a)</td><td>64.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (-1.65%)</td><td>0.05 (-11.60%)</td><td>0.04 <b>(-27.61%)</b></td><td>0.03 (-2.07%)</td><td>0.02 (+15.93%)</td><td>499.80 (+2.13%)</td><td>372.24 (+16.12%)</td><td>400.90 <b>(+38.15%)</b></td><td>241.90 (+1.68%)</td><td>122.61 (+17.82%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>489.40 (n/a)</td><td>320.56 (n/a)</td><td>290.20 (n/a)</td><td>237.90 (n/a)</td><td>104.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 <b>(-27.23%)</b></td><td>0.04 (-18.22%)</td><td>0.04 (+4.63%)</td><td>0.01 <b>(-64.88%)</b></td><td>0.02 (-15.36%)</td><td>1877.90 <b>(+184.70%)</b></td><td>679.08 <b>(+60.67%)</b></td><td>430.60 (-4.44%)</td><td>301.60 <b>(+37.40%)</b></td><td>673.80 <b>(+270.49%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>659.60 (n/a)</td><td>422.66 (n/a)</td><td>450.60 (n/a)</td><td>219.50 (n/a)</td><td>181.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (+5.78%)</td><td>0.03 (-16.69%)</td><td>0.03 (-14.12%)</td><td>0.01 <b>(-71.05%)</b></td><td>0.02 <b>(+96.61%)</b></td><td>1864.20 <b>(+245.48%)</b></td><td>743.04 <b>(+69.67%)</b></td><td>521.70 (+16.45%)</td><td>288.10 (-5.48%)</td><td>637.14 <b>(+654.55%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>539.60 (n/a)</td><td>437.92 (n/a)</td><td>448.00 (n/a)</td><td>304.80 (n/a)</td><td>84.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (-12.37%)</td><td>0.08 (-11.52%)</td><td>0.07 (+1.14%)</td><td>0.06 (+16.98%)</td><td>0.03 <b>(-33.44%)</b></td><td>564.30 (-14.51%)</td><td>431.86 (+4.24%)</td><td>439.20 (-1.13%)</td><td>261.10 (+14.12%)</td><td>112.31 <b>(-35.27%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>660.10 (n/a)</td><td>414.28 (n/a)</td><td>444.20 (n/a)</td><td>228.80 (n/a)</td><td>173.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 (-16.06%)</td><td>0.09 (+17.13%)</td><td>0.07 (+18.91%)</td><td>0.06 <b>(+48.37%)</b></td><td>0.03 <b>(-33.43%)</b></td><td>518.50 <b>(-32.60%)</b></td><td>411.58 <b>(-22.58%)</b></td><td>475.40 (-15.90%)</td><td>272.60 (+19.14%)</td><td>115.51 <b>(-42.17%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>769.30 (n/a)</td><td>531.60 (n/a)</td><td>565.30 (n/a)</td><td>228.80 (n/a)</td><td>199.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (-9.85%)</td><td>0.09 <b>(+31.55%)</b></td><td>0.07 (+14.03%)</td><td>0.07 <b>(+323.41%)</b></td><td>0.03 <b>(-29.95%)</b></td><td>490.60 <b>(-76.38%)</b></td><td>381.12 <b>(-49.96%)</b></td><td>448.50 (-12.30%)</td><td>251.60 (+10.93%)</td><td>117.88 <b>(-84.19%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2077.40 (n/a)</td><td>761.62 (n/a)</td><td>511.40 (n/a)</td><td>226.80 (n/a)</td><td>745.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (+12.64%)</td><td>0.08 <b>(+21.29%)</b></td><td>0.07 <b>(+29.55%)</b></td><td>0.05 (+17.71%)</td><td>0.03 (+2.54%)</td><td>682.70 (-15.06%)</td><td>466.06 <b>(-20.76%)</b></td><td>455.00 <b>(-22.80%)</b></td><td>236.20 (-11.20%)</td><td>159.15 <b>(-27.46%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>803.70 (n/a)</td><td>588.14 (n/a)</td><td>589.40 (n/a)</td><td>266.00 (n/a)</td><td>219.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 <b>(+82.88%)</b></td><td>0.09 <b>(+29.00%)</b></td><td>0.07 (-0.38%)</td><td>0.05 (-11.42%)</td><td>0.04 <b>(+322.25%)</b></td><td>600.20 (+12.90%)</td><td>425.20 (-10.31%)</td><td>503.10 (+0.38%)</td><td>203.40 <b>(-45.32%)</b></td><td>166.01 <b>(+164.09%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>531.60 (n/a)</td><td>474.08 (n/a)</td><td>501.20 (n/a)</td><td>372.00 (n/a)</td><td>62.86 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mem_copy</summary>


### test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+4.58%)</td><td>0.02 <b>(+21.28%)</b></td><td>0.02 (-1.49%)</td><td>0.01 <b>(+83.23%)</b></td><td>0.00 <b>(-74.56%)</b></td><td>293.20 <b>(-45.43%)</b></td><td>269.26 <b>(-26.15%)</b></td><td>272.10 (+1.49%)</td><td>244.70 (-4.38%)</td><td>19.22 <b>(-86.60%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.30 (n/a)</td><td>364.60 (n/a)</td><td>268.10 (n/a)</td><td>255.90 (n/a)</td><td>143.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+3.80%)</td><td>0.01 (-12.47%)</td><td>0.02 (-7.45%)</td><td>0.01 <b>(-31.87%)</b></td><td>0.00 <b>(+169.50%)</b></td><td>441.00 <b>(+46.76%)</b></td><td>311.16 <b>(+21.19%)</b></td><td>268.40 (+8.05%)</td><td>230.50 (-3.64%)</td><td>92.91 <b>(+271.55%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>300.50 (n/a)</td><td>256.76 (n/a)</td><td>248.40 (n/a)</td><td>239.20 (n/a)</td><td>25.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 <b>(+26.18%)</b></td><td>0.01 <b>(+27.05%)</b></td><td>0.01 (+18.68%)</td><td>0.01 <b>(+24.84%)</b></td><td>0.00 <b>(+26.47%)</b></td><td>365.10 (-19.90%)</td><td>289.22 <b>(-21.37%)</b></td><td>273.80 (-15.75%)</td><td>230.70 <b>(-20.75%)</b></td><td>60.49 <b>(-23.17%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>455.80 (n/a)</td><td>367.84 (n/a)</td><td>325.00 (n/a)</td><td>291.10 (n/a)</td><td>78.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 <b>(+39.94%)</b></td><td>0.02 <b>(+37.14%)</b></td><td>0.02 <b>(+78.20%)</b></td><td>0.01 (+2.33%)</td><td>0.01 <b>(+34.76%)</b></td><td>542.00 (-2.27%)</td><td>298.76 <b>(-25.19%)</b></td><td>270.00 <b>(-43.88%)</b></td><td>149.60 <b>(-28.56%)</b></td><td>146.23 (-2.89%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.60 (n/a)</td><td>399.34 (n/a)</td><td>481.10 (n/a)</td><td>209.40 (n/a)</td><td>150.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 <b>(+32.91%)</b></td><td>0.01 (+16.56%)</td><td>0.01 <b>(+41.60%)</b></td><td>0.00 <b>(-69.58%)</b></td><td>0.01 <b>(+180.97%)</b></td><td>1989.20 <b>(+228.74%)</b></td><td>672.50 <b>(+41.48%)</b></td><td>334.80 <b>(-29.38%)</b></td><td>259.00 <b>(-24.75%)</b></td><td>739.84 <b>(+690.87%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>605.10 (n/a)</td><td>475.34 (n/a)</td><td>474.10 (n/a)</td><td>344.20 (n/a)</td><td>93.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (-3.19%)</td><td>0.01 (+2.22%)</td><td>0.01 (-4.97%)</td><td>0.01 (-9.77%)</td><td>0.00 (-0.75%)</td><td>433.30 (+10.85%)</td><td>300.80 (-1.83%)</td><td>282.30 (+5.22%)</td><td>243.20 (+3.31%)</td><td>78.10 (+10.61%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>390.90 (n/a)</td><td>306.40 (n/a)</td><td>268.30 (n/a)</td><td>235.40 (n/a)</td><td>70.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 <b>(+61.17%)</b></td><td>0.01 <b>(+77.32%)</b></td><td>0.01 <b>(+88.77%)</b></td><td>0.01 <b>(+65.15%)</b></td><td>0.00 <b>(+66.82%)</b></td><td>463.10 <b>(-39.45%)</b></td><td>309.06 <b>(-43.38%)</b></td><td>277.40 <b>(-47.03%)</b></td><td>246.30 <b>(-37.94%)</b></td><td>87.89 <b>(-35.80%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>764.80 (n/a)</td><td>545.84 (n/a)</td><td>523.70 (n/a)</td><td>396.90 (n/a)</td><td>136.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+11.63%)</td><td>0.01 (+7.83%)</td><td>0.01 (-17.15%)</td><td>0.01 (+19.82%)</td><td>0.00 <b>(+20.01%)</b></td><td>543.00 (-16.55%)</td><td>390.20 (-7.03%)</td><td>433.90 <b>(+20.70%)</b></td><td>249.00 (-10.43%)</td><td>133.30 (-15.51%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>650.70 (n/a)</td><td>419.70 (n/a)</td><td>359.50 (n/a)</td><td>278.00 (n/a)</td><td>157.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (-6.26%)</td><td>0.01 (+3.65%)</td><td>0.01 (+1.17%)</td><td>0.01 (-4.14%)</td><td>0.00 <b>(-21.65%)</b></td><td>559.80 (+4.32%)</td><td>355.62 (-6.84%)</td><td>334.50 (-1.15%)</td><td>263.90 (+6.67%)</td><td>120.18 (-14.35%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>536.60 (n/a)</td><td>381.72 (n/a)</td><td>338.40 (n/a)</td><td>247.40 (n/a)</td><td>140.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+4.43%)</td><td>0.01 (+4.36%)</td><td>0.01 (+3.73%)</td><td>0.01 <b>(+28.60%)</b></td><td>0.00 (-10.30%)</td><td>385.30 <b>(-22.24%)</b></td><td>304.04 (-6.43%)</td><td>291.40 (-3.61%)</td><td>242.20 (-4.23%)</td><td>62.41 <b>(-36.39%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.50 (n/a)</td><td>324.92 (n/a)</td><td>302.30 (n/a)</td><td>252.90 (n/a)</td><td>98.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128]

_No metrics available._


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.01 (-2.39%)</td><td>0.01 (-1.50%)</td><td>0.01 <b>(-24.96%)</b></td><td>0.01 <b>(+53.11%)</b></td><td>0.00 (-14.08%)</td><td>587.30 <b>(-34.69%)</b></td><td>461.54 (-5.53%)</td><td>534.40 <b>(+33.27%)</b></td><td>296.50 (+2.45%)</td><td>129.60 <b>(-46.01%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>899.30 (n/a)</td><td>488.54 (n/a)</td><td>401.00 (n/a)</td><td>289.40 (n/a)</td><td>240.04 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (-14.29%)</td><td>0.02 (-16.07%)</td><td>0.02 <b>(-27.38%)</b></td><td>0.02 <b>(-22.96%)</b></td><td>0.01 (+16.67%)</td><td>518.40 <b>(+29.79%)</b></td><td>415.24 <b>(+24.04%)</b></td><td>498.10 <b>(+37.71%)</b></td><td>279.30 (+16.72%)</td><td>123.45 <b>(+69.57%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>399.40 (n/a)</td><td>334.76 (n/a)</td><td>361.70 (n/a)</td><td>239.30 (n/a)</td><td>72.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (-4.32%)</td><td>0.03 (+19.07%)</td><td>0.03 <b>(+35.38%)</b></td><td>0.02 <b>(+39.23%)</b></td><td>0.01 <b>(-35.52%)</b></td><td>420.00 <b>(-28.18%)</b></td><td>295.52 <b>(-21.90%)</b></td><td>278.40 <b>(-26.13%)</b></td><td>229.30 (+4.51%)</td><td>72.57 <b>(-48.48%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.80 (n/a)</td><td>378.40 (n/a)</td><td>376.90 (n/a)</td><td>219.40 (n/a)</td><td>140.84 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (+4.43%)</td><td>0.02 <b>(-21.13%)</b></td><td>0.01 <b>(-45.97%)</b></td><td>0.01 (-0.18%)</td><td>0.01 <b>(+25.24%)</b></td><td>566.70 (+0.19%)</td><td>445.36 <b>(+32.68%)</b></td><td>548.20 <b>(+85.08%)</b></td><td>215.40 (-4.22%)</td><td>158.66 (+18.37%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>565.60 (n/a)</td><td>335.66 (n/a)</td><td>296.20 (n/a)</td><td>224.90 (n/a)</td><td>134.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (+17.16%)</td><td>0.02 (+6.10%)</td><td>0.02 (+8.64%)</td><td>0.01 (-0.31%)</td><td>0.01 <b>(+34.43%)</b></td><td>572.00 (+0.30%)</td><td>428.50 (-3.11%)</td><td>433.20 (-7.95%)</td><td>238.80 (-14.65%)</td><td>122.14 (+11.99%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>570.30 (n/a)</td><td>442.24 (n/a)</td><td>470.60 (n/a)</td><td>279.80 (n/a)</td><td>109.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (+1.45%)</td><td>0.02 (-2.91%)</td><td>0.02 (-0.81%)</td><td>0.01 (-14.29%)</td><td>0.01 (+5.06%)</td><td>1052.60 (+16.68%)</td><td>501.50 (+7.82%)</td><td>398.60 (+0.83%)</td><td>264.80 (-1.41%)</td><td>317.09 <b>(+24.56%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>902.10 (n/a)</td><td>465.12 (n/a)</td><td>395.30 (n/a)</td><td>268.60 (n/a)</td><td>254.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 <b>(-25.51%)</b></td><td>0.02 (-8.45%)</td><td>0.02 <b>(-20.13%)</b></td><td>0.02 (+16.79%)</td><td>0.01 <b>(-45.49%)</b></td><td>424.30 (-14.37%)</td><td>341.38 (+1.51%)</td><td>358.00 <b>(+25.22%)</b></td><td>264.90 <b>(+34.26%)</b></td><td>72.27 <b>(-41.72%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.50 (n/a)</td><td>336.30 (n/a)</td><td>285.90 (n/a)</td><td>197.30 (n/a)</td><td>124.00 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 <b>(+24.67%)</b></td><td>0.02 (+17.57%)</td><td>0.02 <b>(-29.86%)</b></td><td>0.01 <b>(+190.13%)</b></td><td>0.01 (-6.59%)</td><td>622.60 <b>(-65.53%)</b></td><td>420.48 <b>(-39.93%)</b></td><td>455.10 <b>(+42.58%)</b></td><td>217.00 (-19.81%)</td><td>170.43 <b>(-73.93%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1806.40 (n/a)</td><td>699.94 (n/a)</td><td>319.20 (n/a)</td><td>270.60 (n/a)</td><td>653.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 <b>(+20.74%)</b></td><td>0.02 (+1.16%)</td><td>0.02 <b>(-21.61%)</b></td><td>0.01 (-6.08%)</td><td>0.01 <b>(+41.57%)</b></td><td>1092.10 (+6.47%)</td><td>540.02 (+7.94%)</td><td>482.70 <b>(+27.56%)</b></td><td>249.90 (-17.17%)</td><td>340.52 (+13.39%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1025.70 (n/a)</td><td>500.30 (n/a)</td><td>378.40 (n/a)</td><td>301.70 (n/a)</td><td>300.31 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (-5.82%)</td><td>0.03 <b>(+41.28%)</b></td><td>0.03 <b>(+103.94%)</b></td><td>0.02 <b>(+52.76%)</b></td><td>0.01 (-14.90%)</td><td>511.70 <b>(-34.54%)</b></td><td>362.98 <b>(-33.66%)</b></td><td>289.90 <b>(-50.97%)</b></td><td>248.10 (+6.21%)</td><td>135.40 <b>(-32.83%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>781.70 (n/a)</td><td>547.18 (n/a)</td><td>591.30 (n/a)</td><td>233.60 (n/a)</td><td>201.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (+14.18%)</td><td>0.03 <b>(+45.37%)</b></td><td>0.03 <b>(+41.20%)</b></td><td>0.03 <b>(+94.54%)</b></td><td>0.00 <b>(-70.58%)</b></td><td>304.00 <b>(-48.59%)</b></td><td>281.80 <b>(-35.44%)</b></td><td>273.90 <b>(-29.19%)</b></td><td>264.30 (-12.43%)</td><td>16.27 <b>(-87.14%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.30 (n/a)</td><td>436.50 (n/a)</td><td>386.80 (n/a)</td><td>301.80 (n/a)</td><td>126.48 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (+4.80%)</td><td>0.02 (+2.64%)</td><td>0.02 (-15.61%)</td><td>0.01 (+13.48%)</td><td>0.01 (-2.34%)</td><td>593.00 (-11.87%)</td><td>428.70 (-4.26%)</td><td>458.10 (+18.49%)</td><td>297.40 (-4.59%)</td><td>119.30 <b>(-20.50%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>672.90 (n/a)</td><td>447.76 (n/a)</td><td>386.60 (n/a)</td><td>311.70 (n/a)</td><td>150.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (+6.27%)</td><td>0.02 (-9.95%)</td><td>0.02 (-9.86%)</td><td>0.01 <b>(-44.42%)</b></td><td>0.01 <b>(+47.01%)</b></td><td>1055.40 <b>(+79.92%)</b></td><td>577.60 <b>(+33.66%)</b></td><td>471.30 (+10.95%)</td><td>266.10 (-5.87%)</td><td>337.83 <b>(+142.48%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.60 (n/a)</td><td>432.14 (n/a)</td><td>424.80 (n/a)</td><td>282.70 (n/a)</td><td>139.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (+1.79%)</td><td>0.05 (-10.94%)</td><td>0.05 (-12.10%)</td><td>0.03 <b>(-25.14%)</b></td><td>0.01 <b>(+31.04%)</b></td><td>581.20 <b>(+33.58%)</b></td><td>356.94 (+17.75%)</td><td>318.90 (+13.77%)</td><td>245.50 (-1.76%)</td><td>132.56 <b>(+74.53%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>435.10 (n/a)</td><td>303.14 (n/a)</td><td>280.30 (n/a)</td><td>249.90 (n/a)</td><td>75.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (+4.32%)</td><td>0.06 (+3.21%)</td><td>0.06 (+4.52%)</td><td>0.05 (-7.38%)</td><td>0.01 <b>(+58.46%)</b></td><td>333.50 (+7.96%)</td><td>280.90 (-2.32%)</td><td>277.80 (-4.34%)</td><td>243.50 (-4.13%)</td><td>36.76 <b>(+61.71%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>308.90 (n/a)</td><td>287.58 (n/a)</td><td>290.40 (n/a)</td><td>254.00 (n/a)</td><td>22.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (+11.40%)</td><td>0.05 (+14.44%)</td><td>0.07 <b>(+41.21%)</b></td><td>0.03 (-16.13%)</td><td>0.02 <b>(+57.54%)</b></td><td>619.00 (+19.24%)</td><td>351.62 (-3.66%)</td><td>246.40 <b>(-29.18%)</b></td><td>219.90 (-10.24%)</td><td>173.94 <b>(+63.38%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>519.10 (n/a)</td><td>364.96 (n/a)</td><td>347.90 (n/a)</td><td>245.00 (n/a)</td><td>106.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (+2.16%)</td><td>0.05 (+9.68%)</td><td>0.04 (+10.42%)</td><td>0.03 (+14.53%)</td><td>0.02 (-1.67%)</td><td>474.40 (-12.68%)</td><td>360.82 (-10.68%)</td><td>410.70 (-9.44%)</td><td>238.20 (-2.10%)</td><td>111.98 (-18.71%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>543.30 (n/a)</td><td>403.96 (n/a)</td><td>453.50 (n/a)</td><td>243.30 (n/a)</td><td>137.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.09 <b>(+28.92%)</b></td><td>0.06 <b>(+36.77%)</b></td><td>0.06 <b>(+58.09%)</b></td><td>0.04 <b>(+54.25%)</b></td><td>0.02 (+3.26%)</td><td>444.50 <b>(-35.18%)</b></td><td>288.04 <b>(-30.71%)</b></td><td>263.30 <b>(-36.74%)</b></td><td>191.50 <b>(-22.44%)</b></td><td>95.62 <b>(-44.98%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>685.70 (n/a)</td><td>415.68 (n/a)</td><td>416.20 (n/a)</td><td>246.90 (n/a)</td><td>173.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (+1.25%)</td><td>0.06 <b>(+50.44%)</b></td><td>0.07 <b>(+74.09%)</b></td><td>0.05 <b>(+85.30%)</b></td><td>0.01 <b>(-57.07%)</b></td><td>315.50 <b>(-46.03%)</b></td><td>259.44 <b>(-39.16%)</b></td><td>244.10 <b>(-42.56%)</b></td><td>241.00 (-1.23%)</td><td>31.78 <b>(-77.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>584.60 (n/a)</td><td>426.40 (n/a)</td><td>425.00 (n/a)</td><td>244.00 (n/a)</td><td>138.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 <b>(+63.57%)</b></td><td>0.06 <b>(+98.35%)</b></td><td>0.07 <b>(+128.77%)</b></td><td>0.05 <b>(+103.67%)</b></td><td>0.01 (-13.37%)</td><td>298.20 <b>(-50.91%)</b></td><td>262.02 <b>(-50.55%)</b></td><td>250.30 <b>(-56.29%)</b></td><td>244.40 <b>(-38.85%)</b></td><td>22.71 <b>(-74.19%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>607.40 (n/a)</td><td>529.86 (n/a)</td><td>572.70 (n/a)</td><td>399.70 (n/a)</td><td>87.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 <b>(+28.50%)</b></td><td>0.05 (+14.93%)</td><td>0.05 <b>(+32.29%)</b></td><td>0.03 <b>(-23.96%)</b></td><td>0.02 <b>(+101.70%)</b></td><td>606.00 <b>(+31.51%)</b></td><td>358.80 (-3.26%)</td><td>303.20 <b>(-24.41%)</b></td><td>209.70 <b>(-22.19%)</b></td><td>160.23 <b>(+111.44%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>460.80 (n/a)</td><td>370.90 (n/a)</td><td>401.10 (n/a)</td><td>269.50 (n/a)</td><td>75.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 <b>(-26.77%)</b></td><td>0.03 <b>(-23.67%)</b></td><td>0.03 <b>(-20.21%)</b></td><td>0.02 <b>(-20.13%)</b></td><td>0.01 <b>(-44.82%)</b></td><td>665.80 <b>(+25.20%)</b></td><td>509.86 <b>(+25.48%)</b></td><td>534.00 <b>(+25.32%)</b></td><td>363.20 <b>(+36.54%)</b></td><td>120.32 (-7.01%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>531.80 (n/a)</td><td>406.32 (n/a)</td><td>426.10 (n/a)</td><td>266.00 (n/a)</td><td>129.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 <b>(-28.55%)</b></td><td>0.06 (-5.86%)</td><td>0.06 (+6.66%)</td><td>0.03 (+7.74%)</td><td>0.01 <b>(-41.98%)</b></td><td>487.90 (-7.19%)</td><td>310.94 (-0.24%)</td><td>274.60 (-6.22%)</td><td>244.00 <b>(+39.91%)</b></td><td>100.29 <b>(-22.92%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>525.70 (n/a)</td><td>311.68 (n/a)</td><td>292.80 (n/a)</td><td>174.40 (n/a)</td><td>130.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (-14.10%)</td><td>0.04 <b>(-20.94%)</b></td><td>0.03 <b>(-31.17%)</b></td><td>0.02 (-19.95%)</td><td>0.02 (-14.45%)</td><td>758.40 <b>(+24.92%)</b></td><td>528.06 <b>(+25.40%)</b></td><td>541.30 <b>(+45.28%)</b></td><td>261.40 (+16.44%)</td><td>179.48 (+9.99%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>607.10 (n/a)</td><td>421.10 (n/a)</td><td>372.60 (n/a)</td><td>224.50 (n/a)</td><td>163.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 <b>(+78.27%)</b></td><td>0.05 <b>(+46.58%)</b></td><td>0.05 <b>(+49.05%)</b></td><td>0.04 (+13.04%)</td><td>0.01 <b>(+944.66%)</b></td><td>450.60 (-11.54%)</td><td>346.60 <b>(-29.18%)</b></td><td>323.60 <b>(-32.90%)</b></td><td>265.90 <b>(-43.90%)</b></td><td>76.80 <b>(+420.81%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>509.40 (n/a)</td><td>489.44 (n/a)</td><td>482.30 (n/a)</td><td>474.00 (n/a)</td><td>14.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (+0.79%)</td><td>0.11 (+19.76%)</td><td>0.12 <b>(+87.96%)</b></td><td>0.06 (+7.09%)</td><td>0.03 (-16.51%)</td><td>509.30 (-6.64%)</td><td>335.54 <b>(-20.59%)</b></td><td>276.10 <b>(-46.80%)</b></td><td>241.00 (-0.78%)</td><td>116.91 <b>(-25.39%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>545.50 (n/a)</td><td>422.52 (n/a)</td><td>519.00 (n/a)</td><td>242.90 (n/a)</td><td>156.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (-9.79%)</td><td>0.12 (-6.31%)</td><td>0.12 (-3.54%)</td><td>0.10 (-10.67%)</td><td>0.02 (-7.20%)</td><td>338.30 (+11.95%)</td><td>274.38 (+6.88%)</td><td>265.50 (+3.67%)</td><td>232.70 (+10.86%)</td><td>40.94 (+16.68%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>302.20 (n/a)</td><td>256.72 (n/a)</td><td>256.10 (n/a)</td><td>209.90 (n/a)</td><td>35.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (+13.60%)</td><td>0.12 <b>(+41.96%)</b></td><td>0.13 <b>(+23.33%)</b></td><td>0.07 <b>(+395.70%)</b></td><td>0.03 <b>(-32.64%)</b></td><td>489.50 <b>(-79.83%)</b></td><td>296.62 <b>(-60.74%)</b></td><td>248.50 (-18.92%)</td><td>239.40 (-11.99%)</td><td>108.20 <b>(-88.46%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2426.30 (n/a)</td><td>755.56 (n/a)</td><td>306.50 (n/a)</td><td>272.00 (n/a)</td><td>937.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (+3.72%)</td><td>0.13 <b>(+48.08%)</b></td><td>0.13 <b>(+99.44%)</b></td><td>0.11 <b>(+116.72%)</b></td><td>0.01 <b>(-64.23%)</b></td><td>311.40 <b>(-53.86%)</b></td><td>259.86 <b>(-41.87%)</b></td><td>258.50 <b>(-49.85%)</b></td><td>230.10 (-3.60%)</td><td>31.33 <b>(-83.05%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>674.90 (n/a)</td><td>447.02 (n/a)</td><td>515.50 (n/a)</td><td>238.70 (n/a)</td><td>184.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 <b>(-24.30%)</b></td><td>0.08 (-10.73%)</td><td>0.08 <b>(+21.60%)</b></td><td>0.06 (-8.58%)</td><td>0.03 <b>(-40.79%)</b></td><td>580.70 (+9.40%)</td><td>420.22 (+3.01%)</td><td>401.60 (-17.77%)</td><td>249.10 <b>(+32.08%)</b></td><td>122.66 <b>(-20.59%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>530.80 (n/a)</td><td>407.96 (n/a)</td><td>488.40 (n/a)</td><td>188.60 (n/a)</td><td>154.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (-12.61%)</td><td>0.12 <b>(+33.67%)</b></td><td>0.12 <b>(+55.53%)</b></td><td>0.07 <b>(+293.58%)</b></td><td>0.03 <b>(-47.46%)</b></td><td>478.80 <b>(-74.59%)</b></td><td>299.22 <b>(-54.77%)</b></td><td>272.50 <b>(-35.70%)</b></td><td>218.40 (+14.47%)</td><td>102.79 <b>(-85.19%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1884.40 (n/a)</td><td>661.50 (n/a)</td><td>423.80 (n/a)</td><td>190.80 (n/a)</td><td>694.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.09 <b>(-53.12%)</b></td><td>0.07 <b>(-30.83%)</b></td><td>0.08 (+16.16%)</td><td>0.06 (-7.99%)</td><td>0.01 <b>(-76.09%)</b></td><td>566.60 (+8.69%)</td><td>465.04 <b>(+20.57%)</b></td><td>421.70 (-13.90%)</td><td>385.20 <b>(+113.29%)</b></td><td>91.76 <b>(-46.40%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>521.30 (n/a)</td><td>385.70 (n/a)</td><td>489.80 (n/a)</td><td>180.60 (n/a)</td><td>171.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 <b>(-26.29%)</b></td><td>0.11 (+18.10%)</td><td>0.11 <b>(+64.60%)</b></td><td>0.08 <b>(+61.55%)</b></td><td>0.02 <b>(-58.18%)</b></td><td>386.00 <b>(-38.10%)</b></td><td>314.40 <b>(-27.85%)</b></td><td>295.90 <b>(-39.25%)</b></td><td>233.60 <b>(+35.66%)</b></td><td>67.34 <b>(-59.81%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>623.60 (n/a)</td><td>435.74 (n/a)</td><td>487.10 (n/a)</td><td>172.20 (n/a)</td><td>167.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 (+16.19%)</td><td>0.09 (-10.96%)</td><td>0.08 <b>(-38.65%)</b></td><td>0.06 (+15.64%)</td><td>0.04 (-12.32%)</td><td>545.30 (-13.53%)</td><td>395.18 (+2.76%)</td><td>396.00 <b>(+62.96%)</b></td><td>203.90 (-13.93%)</td><td>123.52 <b>(-37.90%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>630.60 (n/a)</td><td>384.58 (n/a)</td><td>243.00 (n/a)</td><td>236.90 (n/a)</td><td>198.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (-4.61%)</td><td>0.11 (+14.87%)</td><td>0.11 <b>(+44.31%)</b></td><td>0.06 (+10.80%)</td><td>0.03 <b>(-20.56%)</b></td><td>529.30 (-9.75%)</td><td>334.38 (-16.13%)</td><td>306.90 <b>(-30.71%)</b></td><td>250.80 (+4.85%)</td><td>113.01 (-19.71%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>586.50 (n/a)</td><td>398.68 (n/a)</td><td>442.90 (n/a)</td><td>239.20 (n/a)</td><td>140.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 (+15.58%)</td><td>0.08 (+4.91%)</td><td>0.09 (-2.30%)</td><td>0.05 (+2.62%)</td><td>0.03 <b>(+36.23%)</b></td><td>663.40 (-2.56%)</td><td>440.28 (-0.42%)</td><td>383.20 (+2.35%)</td><td>265.30 (-13.47%)</td><td>174.83 (+15.35%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>680.80 (n/a)</td><td>442.12 (n/a)</td><td>374.40 (n/a)</td><td>306.60 (n/a)</td><td>151.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (+7.58%)</td><td>0.10 (+17.31%)</td><td>0.12 <b>(+32.27%)</b></td><td>0.04 <b>(-39.79%)</b></td><td>0.04 <b>(+42.71%)</b></td><td>932.30 <b>(+66.10%)</b></td><td>404.60 (+0.37%)</td><td>279.10 <b>(-24.40%)</b></td><td>261.80 (-7.06%)</td><td>295.15 <b>(+130.15%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>561.30 (n/a)</td><td>403.12 (n/a)</td><td>369.20 (n/a)</td><td>281.70 (n/a)</td><td>128.24 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.11 <b>(+20.94%)</b></td><td>0.09 <b>(+32.80%)</b></td><td>0.09 <b>(+23.43%)</b></td><td>0.07 <b>(+57.41%)</b></td><td>0.02 <b>(-25.92%)</b></td><td>365.60 <b>(-36.47%)</b></td><td>283.56 <b>(-29.59%)</b></td><td>281.40 (-18.97%)</td><td>223.20 (-17.33%)</td><td>54.29 <b>(-61.58%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>575.50 (n/a)</td><td>402.74 (n/a)</td><td>347.30 (n/a)</td><td>270.00 (n/a)</td><td>141.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.21 (+17.23%)</td><td>0.15 <b>(+25.70%)</b></td><td>0.14 <b>(+67.63%)</b></td><td>0.11 <b>(+43.59%)</b></td><td>0.04 <b>(-29.33%)</b></td><td>461.10 <b>(-30.36%)</b></td><td>344.50 <b>(-27.86%)</b></td><td>341.70 <b>(-40.35%)</b></td><td>237.00 (-14.69%)</td><td>80.35 <b>(-56.17%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>662.10 (n/a)</td><td>477.54 (n/a)</td><td>572.80 (n/a)</td><td>277.80 (n/a)</td><td>183.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.15 (+0.04%)</td><td>3.11 (+6.66%)</td><td>3.00 (+13.85%)</td><td>2.66 (+6.99%)</td><td>0.61 (-12.93%)</td><td>3937.40 (-6.54%)</td><td>3461.26 (-7.18%)</td><td>3497.90 (-12.17%)</td><td>2524.40 (-0.04%)</td><td>566.69 (-17.55%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>4.15 (n/a)</td><td>2.91 (n/a)</td><td>2.63 (n/a)</td><td>2.49 (n/a)</td><td>0.70 (n/a)</td><td>4212.80 (n/a)</td><td>3729.06 (n/a)</td><td>3982.50 (n/a)</td><td>2525.40 (n/a)</td><td>687.33 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.19 (+3.23%)</td><td>0.13 (-3.44%)</td><td>0.16 (+3.35%)</td><td>0.07 (-17.18%)</td><td>0.06 <b>(+29.69%)</b></td><td>618.70 <b>(+20.75%)</b></td><td>390.94 (+14.90%)</td><td>263.70 (-3.23%)</td><td>220.10 (-3.12%)</td><td>206.45 <b>(+60.20%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>512.40 (n/a)</td><td>340.24 (n/a)</td><td>272.50 (n/a)</td><td>227.20 (n/a)</td><td>128.87 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+5.24%)</td><td>0.02 (-2.08%)</td><td>0.02 (-6.95%)</td><td>0.02 (+11.47%)</td><td>0.00 (-9.62%)</td><td>319.40 (-10.31%)</td><td>278.60 (+1.40%)</td><td>290.80 (+7.46%)</td><td>223.20 (-4.98%)</td><td>36.56 <b>(-24.88%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>356.10 (n/a)</td><td>274.74 (n/a)</td><td>270.60 (n/a)</td><td>234.90 (n/a)</td><td>48.67 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rms_norm</summary>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (-1.05%)</td><td>0.01 (+5.09%)</td><td>0.02 (+8.66%)</td><td>0.01 (+10.32%)</td><td>0.00 (-6.82%)</td><td>498.20 (-9.37%)</td><td>301.34 (-6.53%)</td><td>251.20 (-7.99%)</td><td>242.00 (+1.04%)</td><td>110.72 (-14.86%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>549.70 (n/a)</td><td>322.38 (n/a)</td><td>273.00 (n/a)</td><td>239.50 (n/a)</td><td>130.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (+1.34%)</td><td>0.02 (-11.54%)</td><td>0.02 (-6.99%)</td><td>0.00 <b>(-72.00%)</b></td><td>0.01 <b>(+39.44%)</b></td><td>1989.80 <b>(+257.11%)</b></td><td>651.10 <b>(+83.64%)</b></td><td>299.70 (+7.50%)</td><td>241.60 (-1.35%)</td><td>753.18 <b>(+439.20%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.20 (n/a)</td><td>354.56 (n/a)</td><td>278.80 (n/a)</td><td>244.90 (n/a)</td><td>139.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (-19.23%)</td><td>0.01 <b>(-24.18%)</b></td><td>0.01 <b>(-35.86%)</b></td><td>0.01 <b>(+20.43%)</b></td><td>0.00 <b>(-29.90%)</b></td><td>479.00 (-16.96%)</td><td>349.16 <b>(+21.23%)</b></td><td>357.20 <b>(+55.91%)</b></td><td>243.00 <b>(+23.79%)</b></td><td>105.90 <b>(-34.84%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>576.80 (n/a)</td><td>288.02 (n/a)</td><td>229.10 (n/a)</td><td>196.30 (n/a)</td><td>162.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (-10.39%)</td><td>0.01 (-18.54%)</td><td>0.01 <b>(-30.46%)</b></td><td>0.01 (-14.43%)</td><td>0.00 (-11.95%)</td><td>513.90 (+16.88%)</td><td>405.32 <b>(+22.03%)</b></td><td>449.40 <b>(+43.81%)</b></td><td>238.40 (+11.61%)</td><td>105.86 (+4.61%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>439.70 (n/a)</td><td>332.16 (n/a)</td><td>312.50 (n/a)</td><td>213.60 (n/a)</td><td>101.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 <b>(-24.13%)</b></td><td>0.01 (-17.35%)</td><td>0.02 (-9.17%)</td><td>0.01 <b>(-20.00%)</b></td><td>0.00 (-12.34%)</td><td>461.30 <b>(+25.01%)</b></td><td>332.72 <b>(+23.69%)</b></td><td>268.10 (+10.10%)</td><td>230.30 <b>(+31.75%)</b></td><td>116.83 <b>(+48.05%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>369.00 (n/a)</td><td>269.00 (n/a)</td><td>243.50 (n/a)</td><td>174.80 (n/a)</td><td>78.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (-18.98%)</td><td>0.02 <b>(+49.50%)</b></td><td>0.02 <b>(+109.12%)</b></td><td>0.01 <b>(+146.50%)</b></td><td>0.00 <b>(-42.91%)</b></td><td>512.70 <b>(-59.44%)</b></td><td>302.86 <b>(-48.74%)</b></td><td>247.60 <b>(-52.17%)</b></td><td>238.10 <b>(+23.43%)</b></td><td>118.04 <b>(-70.50%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1263.90 (n/a)</td><td>590.78 (n/a)</td><td>517.70 (n/a)</td><td>192.90 (n/a)</td><td>400.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 <b>(-34.02%)</b></td><td>0.01 (-11.30%)</td><td>0.01 (-13.06%)</td><td>0.01 <b>(+42.53%)</b></td><td>0.00 <b>(-59.89%)</b></td><td>460.50 <b>(-29.84%)</b></td><td>334.58 (-8.21%)</td><td>302.00 (+15.00%)</td><td>243.80 <b>(+51.52%)</b></td><td>85.86 <b>(-58.56%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>656.40 (n/a)</td><td>364.52 (n/a)</td><td>262.60 (n/a)</td><td>160.90 (n/a)</td><td>207.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+7.81%)</td><td>0.01 <b>(+50.84%)</b></td><td>0.01 <b>(+84.74%)</b></td><td>0.01 <b>(+189.72%)</b></td><td>0.00 <b>(-24.98%)</b></td><td>604.80 <b>(-65.48%)</b></td><td>363.62 <b>(-50.23%)</b></td><td>314.10 <b>(-45.87%)</b></td><td>244.70 (-7.24%)</td><td>140.04 <b>(-76.18%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1752.20 (n/a)</td><td>730.54 (n/a)</td><td>580.30 (n/a)</td><td>263.80 (n/a)</td><td>587.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+2.83%)</td><td>0.01 (+13.33%)</td><td>0.01 (+5.16%)</td><td>0.01 (+9.18%)</td><td>0.00 (-11.04%)</td><td>537.20 (-8.41%)</td><td>317.40 (-14.19%)</td><td>277.50 (-4.90%)</td><td>239.00 (-2.73%)</td><td>124.45 (-16.34%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>586.50 (n/a)</td><td>369.88 (n/a)</td><td>291.80 (n/a)</td><td>245.70 (n/a)</td><td>148.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 <b>(+54.88%)</b></td><td>0.01 (-12.71%)</td><td>0.01 <b>(-20.46%)</b></td><td>0.00 <b>(-58.07%)</b></td><td>0.01 <b>(+320.87%)</b></td><td>1091.80 <b>(+138.49%)</b></td><td>594.54 <b>(+44.61%)</b></td><td>547.80 <b>(+25.70%)</b></td><td>229.20 <b>(-35.45%)</b></td><td>312.16 <b>(+528.68%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>457.80 (n/a)</td><td>411.14 (n/a)</td><td>435.80 (n/a)</td><td>355.10 (n/a)</td><td>49.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 <b>(+21.56%)</b></td><td>0.01 (+3.91%)</td><td>0.01 <b>(+22.17%)</b></td><td>0.01 (-19.69%)</td><td>0.00 <b>(+81.88%)</b></td><td>677.30 <b>(+24.53%)</b></td><td>456.62 (+8.53%)</td><td>354.40 (-18.13%)</td><td>231.80 (-17.71%)</td><td>202.65 <b>(+111.78%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>543.90 (n/a)</td><td>420.74 (n/a)</td><td>432.90 (n/a)</td><td>281.70 (n/a)</td><td>95.69 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (-5.82%)</td><td>0.03 (+5.27%)</td><td>0.03 (-5.32%)</td><td>0.02 (+11.99%)</td><td>0.01 <b>(-33.02%)</b></td><td>432.80 (-10.71%)</td><td>289.34 (-10.58%)</td><td>256.30 (+5.65%)</td><td>230.60 (+6.17%)</td><td>81.97 <b>(-34.43%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>484.70 (n/a)</td><td>323.56 (n/a)</td><td>242.60 (n/a)</td><td>217.20 (n/a)</td><td>125.01 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (+6.09%)</td><td>0.04 (+14.94%)</td><td>0.04 (+8.39%)</td><td>0.03 (+8.06%)</td><td>0.01 (-10.87%)</td><td>473.30 (-7.47%)</td><td>305.54 (-15.40%)</td><td>279.20 (-7.73%)</td><td>229.10 (-5.76%)</td><td>97.71 <b>(-22.02%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.50 (n/a)</td><td>361.14 (n/a)</td><td>302.60 (n/a)</td><td>243.10 (n/a)</td><td>125.31 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (+0.08%)</td><td>0.02 (-8.87%)</td><td>0.02 <b>(-39.59%)</b></td><td>0.01 (-16.40%)</td><td>0.01 (+19.64%)</td><td>653.30 (+19.63%)</td><td>432.10 (+16.30%)</td><td>463.70 <b>(+65.55%)</b></td><td>228.50 (-0.09%)</td><td>192.90 <b>(+25.60%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>546.10 (n/a)</td><td>371.54 (n/a)</td><td>280.10 (n/a)</td><td>228.70 (n/a)</td><td>153.58 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (-5.84%)</td><td>0.03 <b>(+22.35%)</b></td><td>0.03 <b>(+74.58%)</b></td><td>0.02 <b>(+60.11%)</b></td><td>0.01 (-18.53%)</td><td>662.00 <b>(-37.54%)</b></td><td>395.32 <b>(-28.49%)</b></td><td>315.30 <b>(-42.72%)</b></td><td>242.60 (+6.22%)</td><td>178.05 <b>(-45.12%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1059.80 (n/a)</td><td>552.80 (n/a)</td><td>550.50 (n/a)</td><td>228.40 (n/a)</td><td>324.43 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 (+14.90%)</td><td>0.03 <b>(+26.43%)</b></td><td>0.03 (+5.35%)</td><td>0.02 <b>(+81.98%)</b></td><td>0.01 <b>(-26.48%)</b></td><td>356.80 <b>(-45.04%)</b></td><td>256.24 <b>(-31.41%)</b></td><td>236.10 (-5.10%)</td><td>194.40 (-12.98%)</td><td>69.90 <b>(-64.50%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>649.20 (n/a)</td><td>373.60 (n/a)</td><td>248.80 (n/a)</td><td>223.40 (n/a)</td><td>196.88 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 (+16.34%)</td><td>0.04 <b>(+37.82%)</b></td><td>0.04 <b>(+86.93%)</b></td><td>0.02 <b>(+47.59%)</b></td><td>0.01 (-18.15%)</td><td>423.40 <b>(-32.25%)</b></td><td>278.22 <b>(-35.53%)</b></td><td>276.30 <b>(-46.51%)</b></td><td>189.70 (-14.05%)</td><td>93.98 <b>(-51.11%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>624.90 (n/a)</td><td>431.58 (n/a)</td><td>516.50 (n/a)</td><td>220.70 (n/a)</td><td>192.21 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 <b>(+23.30%)</b></td><td>0.02 <b>(+27.15%)</b></td><td>0.02 (+19.71%)</td><td>0.01 <b>(+44.59%)</b></td><td>0.01 <b>(+25.91%)</b></td><td>559.00 <b>(-30.83%)</b></td><td>388.02 <b>(-22.15%)</b></td><td>393.30 (-16.46%)</td><td>234.90 (-18.89%)</td><td>130.01 <b>(-31.62%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>808.20 (n/a)</td><td>498.42 (n/a)</td><td>470.80 (n/a)</td><td>289.60 (n/a)</td><td>190.13 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.04 <b>(+23.23%)</b></td><td>0.02 (+13.33%)</td><td>0.02 (+2.53%)</td><td>0.01 (-0.70%)</td><td>0.01 <b>(+80.01%)</b></td><td>624.90 (+0.71%)</td><td>431.70 (-3.79%)</td><td>429.80 (-2.45%)</td><td>247.50 (-18.85%)</td><td>173.06 <b>(+46.77%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.50 (n/a)</td><td>448.70 (n/a)</td><td>440.60 (n/a)</td><td>305.00 (n/a)</td><td>117.91 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (-11.08%)</td><td>0.02 (-4.35%)</td><td>0.03 <b>(+40.59%)</b></td><td>0.01 <b>(-29.49%)</b></td><td>0.01 (-0.09%)</td><td>703.30 <b>(+41.82%)</b></td><td>415.56 (+10.18%)</td><td>300.60 <b>(-28.89%)</b></td><td>265.20 (+12.47%)</td><td>197.93 <b>(+54.87%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.90 (n/a)</td><td>377.18 (n/a)</td><td>422.70 (n/a)</td><td>235.80 (n/a)</td><td>127.80 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (-4.78%)</td><td>0.02 <b>(-26.14%)</b></td><td>0.02 <b>(-28.98%)</b></td><td>0.02 <b>(-37.93%)</b></td><td>0.01 <b>(+95.76%)</b></td><td>572.10 <b>(+61.11%)</b></td><td>453.12 <b>(+41.16%)</b></td><td>456.40 <b>(+40.82%)</b></td><td>294.20 (+5.03%)</td><td>102.87 <b>(+215.56%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>355.10 (n/a)</td><td>321.00 (n/a)</td><td>324.10 (n/a)</td><td>280.10 (n/a)</td><td>32.60 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.03 (-10.24%)</td><td>0.02 (-16.94%)</td><td>0.02 <b>(-33.83%)</b></td><td>0.01 <b>(-34.22%)</b></td><td>0.01 (-0.97%)</td><td>1038.20 <b>(+52.03%)</b></td><td>567.08 <b>(+27.40%)</b></td><td>541.00 <b>(+51.16%)</b></td><td>324.00 (+11.42%)</td><td>284.42 <b>(+65.51%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>682.90 (n/a)</td><td>445.12 (n/a)</td><td>357.90 (n/a)</td><td>290.80 (n/a)</td><td>171.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (-8.59%)</td><td>0.05 (-17.32%)</td><td>0.05 (-11.81%)</td><td>0.04 <b>(-26.10%)</b></td><td>0.01 <b>(+25.66%)</b></td><td>405.80 <b>(+35.31%)</b></td><td>325.76 <b>(+22.82%)</b></td><td>301.00 (+13.41%)</td><td>255.20 (+9.39%)</td><td>59.86 <b>(+90.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>299.90 (n/a)</td><td>265.24 (n/a)</td><td>265.40 (n/a)</td><td>233.30 (n/a)</td><td>31.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (-2.38%)</td><td>0.08 (-3.24%)</td><td>0.09 (+7.13%)</td><td>0.04 <b>(+36.70%)</b></td><td>0.03 (-1.17%)</td><td>568.80 <b>(-26.84%)</b></td><td>362.78 (-2.23%)</td><td>263.30 (-6.66%)</td><td>235.80 (+2.43%)</td><td>157.11 <b>(-31.51%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>777.50 (n/a)</td><td>371.06 (n/a)</td><td>282.10 (n/a)</td><td>230.20 (n/a)</td><td>229.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (+5.88%)</td><td>0.05 (+3.54%)</td><td>0.05 (+1.39%)</td><td>0.03 (-3.98%)</td><td>0.02 (+14.76%)</td><td>505.00 (+4.15%)</td><td>356.12 (-1.60%)</td><td>311.90 (-1.36%)</td><td>231.20 (-5.56%)</td><td>123.45 (+9.80%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>484.90 (n/a)</td><td>361.92 (n/a)</td><td>316.20 (n/a)</td><td>244.80 (n/a)</td><td>112.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.09 (+7.03%)</td><td>0.06 (-2.39%)</td><td>0.05 (-12.01%)</td><td>0.04 (-1.61%)</td><td>0.02 <b>(+20.81%)</b></td><td>544.20 (+1.64%)</td><td>401.92 (+5.41%)</td><td>435.10 (+13.66%)</td><td>230.00 (-6.58%)</td><td>131.53 (+15.87%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>535.40 (n/a)</td><td>381.28 (n/a)</td><td>382.80 (n/a)</td><td>246.20 (n/a)</td><td>113.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (+15.64%)</td><td>0.04 (-8.55%)</td><td>0.03 <b>(-30.87%)</b></td><td>0.03 (-17.63%)</td><td>0.02 <b>(+62.08%)</b></td><td>581.10 <b>(+21.42%)</b></td><td>433.54 (+19.84%)</td><td>507.10 <b>(+44.64%)</b></td><td>224.20 (-13.50%)</td><td>163.53 <b>(+75.18%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>478.60 (n/a)</td><td>361.78 (n/a)</td><td>350.60 (n/a)</td><td>259.20 (n/a)</td><td>93.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (+17.41%)</td><td>0.06 <b>(+32.13%)</b></td><td>0.05 <b>(+26.84%)</b></td><td>0.04 <b>(+24.70%)</b></td><td>0.02 <b>(+23.50%)</b></td><td>503.10 (-19.81%)</td><td>386.28 <b>(-23.98%)</b></td><td>418.40 <b>(-21.16%)</b></td><td>265.90 (-14.83%)</td><td>103.67 (-13.31%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>627.40 (n/a)</td><td>508.12 (n/a)</td><td>530.70 (n/a)</td><td>312.20 (n/a)</td><td>119.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (+18.90%)</td><td>0.06 <b>(+25.26%)</b></td><td>0.07 (+19.17%)</td><td>0.03 <b>(+278.58%)</b></td><td>0.02 (-13.57%)</td><td>501.40 <b>(-73.59%)</b></td><td>330.30 <b>(-48.07%)</b></td><td>243.40 (-16.10%)</td><td>220.40 (-15.91%)</td><td>132.08 <b>(-81.39%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1898.20 (n/a)</td><td>636.08 (n/a)</td><td>290.10 (n/a)</td><td>262.10 (n/a)</td><td>709.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (-4.55%)</td><td>0.04 (-2.05%)</td><td>0.04 (+4.69%)</td><td>0.01 <b>(-55.38%)</b></td><td>0.02 <b>(+27.17%)</b></td><td>1365.00 <b>(+124.10%)</b></td><td>587.34 <b>(+26.46%)</b></td><td>488.50 (-4.48%)</td><td>280.40 (+4.78%)</td><td>447.22 <b>(+193.70%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>609.10 (n/a)</td><td>464.46 (n/a)</td><td>511.40 (n/a)</td><td>267.60 (n/a)</td><td>152.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (+1.61%)</td><td>0.05 (-4.70%)</td><td>0.06 (-6.21%)</td><td>0.03 (+0.96%)</td><td>0.02 (-12.08%)</td><td>485.70 (-0.96%)</td><td>349.48 (+2.65%)</td><td>292.30 (+6.60%)</td><td>232.50 (-1.57%)</td><td>109.77 (-11.36%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>490.40 (n/a)</td><td>340.46 (n/a)</td><td>274.20 (n/a)</td><td>236.20 (n/a)</td><td>123.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (+10.86%)</td><td>0.04 (-6.98%)</td><td>0.04 (-12.21%)</td><td>0.03 (-8.64%)</td><td>0.02 <b>(+41.13%)</b></td><td>605.60 (+9.47%)</td><td>458.98 (+13.47%)</td><td>452.00 (+13.91%)</td><td>236.00 (-9.82%)</td><td>147.10 <b>(+39.99%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>553.20 (n/a)</td><td>404.50 (n/a)</td><td>396.80 (n/a)</td><td>261.70 (n/a)</td><td>105.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (-9.42%)</td><td>0.04 (+8.74%)</td><td>0.04 <b>(+20.01%)</b></td><td>0.03 (+17.15%)</td><td>0.01 (-16.23%)</td><td>556.00 (-14.65%)</td><td>422.02 (-11.07%)</td><td>414.90 (-16.69%)</td><td>281.60 (+10.39%)</td><td>130.54 (-18.87%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>651.40 (n/a)</td><td>474.56 (n/a)</td><td>498.00 (n/a)</td><td>255.10 (n/a)</td><td>160.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (-10.52%)</td><td>0.09 (-18.78%)</td><td>0.07 <b>(-36.86%)</b></td><td>0.06 (-11.55%)</td><td>0.03 (+15.81%)</td><td>540.90 (+13.04%)</td><td>418.30 <b>(+27.82%)</b></td><td>474.60 <b>(+58.41%)</b></td><td>259.70 (+11.75%)</td><td>132.54 <b>(+42.65%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>478.50 (n/a)</td><td>327.26 (n/a)</td><td>299.60 (n/a)</td><td>232.40 (n/a)</td><td>92.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (-14.24%)</td><td>0.10 (+4.74%)</td><td>0.11 <b>(+34.59%)</b></td><td>0.07 <b>(+26.43%)</b></td><td>0.03 <b>(-24.68%)</b></td><td>466.60 <b>(-20.92%)</b></td><td>342.34 (-8.99%)</td><td>290.60 <b>(-25.72%)</b></td><td>240.60 (+16.63%)</td><td>104.49 <b>(-26.58%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>590.00 (n/a)</td><td>376.14 (n/a)</td><td>391.20 (n/a)</td><td>206.30 (n/a)</td><td>142.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.18 <b>(+93.96%)</b></td><td>0.13 <b>(+66.65%)</b></td><td>0.14 <b>(+56.46%)</b></td><td>0.09 <b>(+55.06%)</b></td><td>0.03 <b>(+166.03%)</b></td><td>439.10 <b>(-35.50%)</b></td><td>324.22 <b>(-38.12%)</b></td><td>302.90 <b>(-36.08%)</b></td><td>232.00 <b>(-48.44%)</b></td><td>85.20 (-11.05%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>680.80 (n/a)</td><td>523.96 (n/a)</td><td>473.90 (n/a)</td><td>450.00 (n/a)</td><td>95.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 <b>(+31.25%)</b></td><td>0.10 (+10.46%)</td><td>0.13 <b>(+38.05%)</b></td><td>0.02 <b>(-64.31%)</b></td><td>0.06 <b>(+139.78%)</b></td><td>1348.30 <b>(+180.14%)</b></td><td>504.78 <b>(+37.24%)</b></td><td>249.60 <b>(-27.55%)</b></td><td>210.00 <b>(-23.83%)</b></td><td>483.51 <b>(+418.34%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>481.30 (n/a)</td><td>367.82 (n/a)</td><td>344.50 (n/a)</td><td>275.70 (n/a)</td><td>93.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 <b>(-26.04%)</b></td><td>0.09 <b>(-25.98%)</b></td><td>0.08 (-13.50%)</td><td>0.03 <b>(-60.87%)</b></td><td>0.05 (-19.87%)</td><td>1304.00 <b>(+155.54%)</b></td><td>587.64 <b>(+55.39%)</b></td><td>507.90 (+15.62%)</td><td>253.70 <b>(+35.23%)</b></td><td>416.09 <b>(+182.66%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>510.30 (n/a)</td><td>378.18 (n/a)</td><td>439.30 (n/a)</td><td>187.60 (n/a)</td><td>147.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 (+0.26%)</td><td>0.09 (-8.38%)</td><td>0.08 (-16.63%)</td><td>0.06 <b>(-22.38%)</b></td><td>0.03 <b>(+86.45%)</b></td><td>516.70 <b>(+28.82%)</b></td><td>379.50 (+15.61%)</td><td>396.90 (+19.95%)</td><td>263.00 (-0.27%)</td><td>113.29 <b>(+126.77%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>401.10 (n/a)</td><td>328.26 (n/a)</td><td>330.90 (n/a)</td><td>263.70 (n/a)</td><td>49.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (+3.06%)</td><td>0.11 (-9.46%)</td><td>0.09 <b>(-30.72%)</b></td><td>0.07 (-10.11%)</td><td>0.03 (+7.64%)</td><td>501.50 (+11.25%)</td><td>378.70 (+11.72%)</td><td>399.30 <b>(+44.36%)</b></td><td>241.20 (-2.94%)</td><td>110.25 (+11.04%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>450.80 (n/a)</td><td>338.98 (n/a)</td><td>276.60 (n/a)</td><td>248.50 (n/a)</td><td>99.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (+5.10%)</td><td>0.08 (-5.57%)</td><td>0.06 (-15.85%)</td><td>0.06 <b>(+249.21%)</b></td><td>0.03 <b>(-23.55%)</b></td><td>590.20 <b>(-71.36%)</b></td><td>483.12 <b>(-31.49%)</b></td><td>543.40 (+18.85%)</td><td>242.70 (-4.86%)</td><td>140.59 <b>(-81.60%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2061.10 (n/a)</td><td>705.18 (n/a)</td><td>457.20 (n/a)</td><td>255.10 (n/a)</td><td>763.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 <b>(+23.43%)</b></td><td>0.11 (+5.47%)</td><td>0.10 (-4.20%)</td><td>0.07 (+3.27%)</td><td>0.03 <b>(+39.09%)</b></td><td>496.40 (-3.16%)</td><td>371.76 (-2.60%)</td><td>384.90 (+4.39%)</td><td>236.80 (-18.96%)</td><td>108.70 (+13.36%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>512.60 (n/a)</td><td>381.68 (n/a)</td><td>368.70 (n/a)</td><td>292.20 (n/a)</td><td>95.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.11 <b>(-22.65%)</b></td><td>0.08 (-13.36%)</td><td>0.07 (-4.60%)</td><td>0.06 (-12.88%)</td><td>0.03 <b>(-21.42%)</b></td><td>593.60 (+14.79%)</td><td>445.08 (+14.89%)</td><td>447.60 (+4.82%)</td><td>285.20 <b>(+29.28%)</b></td><td>145.29 (+19.71%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>517.10 (n/a)</td><td>387.38 (n/a)</td><td>427.00 (n/a)</td><td>220.60 (n/a)</td><td>121.37 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/rope</summary>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (-6.10%)</td><td>0.06 (-11.85%)</td><td>0.08 (-1.54%)</td><td>0.04 (-14.51%)</td><td>0.02 <b>(+23.04%)</b></td><td>510.30 (+16.96%)</td><td>351.42 (+18.39%)</td><td>272.30 (+1.57%)</td><td>241.50 (+6.48%)</td><td>124.74 <b>(+51.03%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>436.30 (n/a)</td><td>296.82 (n/a)</td><td>268.10 (n/a)</td><td>226.80 (n/a)</td><td>82.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (-18.24%)</td><td>0.06 (-8.58%)</td><td>0.06 (+9.41%)</td><td>0.04 (+12.12%)</td><td>0.01 <b>(-38.74%)</b></td><td>476.20 (-10.81%)</td><td>366.82 (+3.71%)</td><td>339.70 (-8.61%)</td><td>275.60 <b>(+22.33%)</b></td><td>87.09 <b>(-29.62%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>533.90 (n/a)</td><td>353.70 (n/a)</td><td>371.70 (n/a)</td><td>225.30 (n/a)</td><td>123.73 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (-0.47%)</td><td>0.05 <b>(-21.37%)</b></td><td>0.04 <b>(-42.16%)</b></td><td>0.04 (-2.95%)</td><td>0.02 (+6.39%)</td><td>556.00 (+3.04%)</td><td>433.38 <b>(+28.95%)</b></td><td>480.40 <b>(+72.87%)</b></td><td>243.30 (+0.50%)</td><td>134.47 (+10.18%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>539.60 (n/a)</td><td>336.08 (n/a)</td><td>277.90 (n/a)</td><td>242.10 (n/a)</td><td>122.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.05 <b>(-36.05%)</b></td><td>0.04 <b>(-23.28%)</b></td><td>0.04 (-7.80%)</td><td>0.03 (-12.87%)</td><td>0.01 <b>(-58.80%)</b></td><td>630.70 (+14.78%)</td><td>501.56 <b>(+22.47%)</b></td><td>488.00 (+8.44%)</td><td>377.80 <b>(+56.37%)</b></td><td>94.10 <b>(-25.76%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>549.50 (n/a)</td><td>409.54 (n/a)</td><td>450.00 (n/a)</td><td>241.60 (n/a)</td><td>126.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 (+12.80%)</td><td>0.05 (-13.32%)</td><td>0.05 <b>(-20.06%)</b></td><td>0.01 <b>(-72.29%)</b></td><td>0.03 <b>(+75.85%)</b></td><td>1863.30 <b>(+260.82%)</b></td><td>677.68 <b>(+75.13%)</b></td><td>446.70 <b>(+25.09%)</b></td><td>247.10 (-11.37%)</td><td>671.22 <b>(+512.08%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>516.40 (n/a)</td><td>386.96 (n/a)</td><td>357.10 (n/a)</td><td>278.80 (n/a)</td><td>109.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.08 <b>(+65.43%)</b></td><td>0.06 <b>(+38.69%)</b></td><td>0.04 (+5.25%)</td><td>0.04 (+8.71%)</td><td>0.02 <b>(+273.71%)</b></td><td>535.90 (-8.00%)</td><td>402.78 <b>(-20.66%)</b></td><td>481.50 (-4.99%)</td><td>247.30 <b>(-39.57%)</b></td><td>137.67 <b>(+101.74%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>582.50 (n/a)</td><td>507.64 (n/a)</td><td>506.80 (n/a)</td><td>409.20 (n/a)</td><td>68.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (+0.43%)</td><td>0.07 <b>(-24.31%)</b></td><td>0.06 <b>(-29.21%)</b></td><td>0.05 <b>(-32.53%)</b></td><td>0.02 <b>(+101.37%)</b></td><td>478.20 <b>(+48.23%)</b></td><td>386.72 <b>(+38.56%)</b></td><td>394.80 <b>(+41.25%)</b></td><td>247.90 (-0.44%)</td><td>94.74 <b>(+204.58%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>322.60 (n/a)</td><td>279.10 (n/a)</td><td>279.50 (n/a)</td><td>249.00 (n/a)</td><td>31.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (-3.64%)</td><td>0.07 <b>(+26.90%)</b></td><td>0.06 (+18.68%)</td><td>0.04 <b>(+229.25%)</b></td><td>0.02 <b>(-29.51%)</b></td><td>592.00 <b>(-69.63%)</b></td><td>399.82 <b>(-45.93%)</b></td><td>425.80 (-15.75%)</td><td>256.90 (+3.80%)</td><td>134.89 <b>(-80.46%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1949.20 (n/a)</td><td>739.42 (n/a)</td><td>505.40 (n/a)</td><td>247.50 (n/a)</td><td>690.48 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 <b>(+31.36%)</b></td><td>0.08 <b>(+22.47%)</b></td><td>0.08 <b>(+42.81%)</b></td><td>0.05 (+4.68%)</td><td>0.03 <b>(+50.62%)</b></td><td>521.50 (-4.47%)</td><td>364.18 (-14.15%)</td><td>321.10 <b>(-29.97%)</b></td><td>213.00 <b>(-23.87%)</b></td><td>141.19 (+16.22%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>545.90 (n/a)</td><td>424.20 (n/a)</td><td>458.50 (n/a)</td><td>279.80 (n/a)</td><td>121.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.09 (+11.55%)</td><td>0.07 (+15.85%)</td><td>0.08 <b>(+49.04%)</b></td><td>0.01 <b>(-75.98%)</b></td><td>0.03 <b>(+101.58%)</b></td><td>2465.40 <b>(+316.24%)</b></td><td>741.92 <b>(+62.84%)</b></td><td>304.10 <b>(-32.90%)</b></td><td>267.30 (-10.33%)</td><td>964.52 <b>(+706.92%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>592.30 (n/a)</td><td>455.60 (n/a)</td><td>453.20 (n/a)</td><td>298.10 (n/a)</td><td>119.53 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 (-0.14%)</td><td>0.06 <b>(-20.48%)</b></td><td>0.08 (-19.05%)</td><td>0.01 <b>(-74.89%)</b></td><td>0.03 <b>(+45.07%)</b></td><td>1852.20 <b>(+298.24%)</b></td><td>649.46 <b>(+93.94%)</b></td><td>327.00 <b>(+23.54%)</b></td><td>247.80 (+0.12%)</td><td>679.58 <b>(+528.26%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>465.10 (n/a)</td><td>334.88 (n/a)</td><td>264.70 (n/a)</td><td>247.50 (n/a)</td><td>108.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 <b>(+26.56%)</b></td><td>0.08 <b>(+48.58%)</b></td><td>0.09 <b>(+63.15%)</b></td><td>0.05 <b>(+32.39%)</b></td><td>0.02 <b>(+26.36%)</b></td><td>450.60 <b>(-24.46%)</b></td><td>316.70 <b>(-32.63%)</b></td><td>288.00 <b>(-38.71%)</b></td><td>249.50 <b>(-20.99%)</b></td><td>80.88 (-19.71%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>596.50 (n/a)</td><td>470.10 (n/a)</td><td>469.90 (n/a)</td><td>315.80 (n/a)</td><td>100.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (-10.73%)</td><td>0.05 (-12.97%)</td><td>0.05 <b>(-25.88%)</b></td><td>0.03 <b>(+29.76%)</b></td><td>0.02 <b>(-20.50%)</b></td><td>537.00 <b>(-22.94%)</b></td><td>398.44 (+7.51%)</td><td>408.80 <b>(+34.92%)</b></td><td>274.20 (+12.01%)</td><td>121.93 <b>(-35.27%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>696.90 (n/a)</td><td>370.60 (n/a)</td><td>303.00 (n/a)</td><td>244.80 (n/a)</td><td>188.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (-11.38%)</td><td>0.05 <b>(-20.11%)</b></td><td>0.06 (-10.68%)</td><td>0.03 <b>(-33.69%)</b></td><td>0.02 <b>(+36.06%)</b></td><td>638.40 <b>(+50.78%)</b></td><td>397.64 <b>(+35.36%)</b></td><td>303.90 (+11.97%)</td><td>272.50 (+12.88%)</td><td>164.50 <b>(+118.86%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>423.40 (n/a)</td><td>293.76 (n/a)</td><td>271.40 (n/a)</td><td>241.40 (n/a)</td><td>75.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (+3.25%)</td><td>0.05 <b>(+21.40%)</b></td><td>0.05 <b>(+37.83%)</b></td><td>0.03 (-2.69%)</td><td>0.02 (+16.43%)</td><td>581.80 (+2.76%)</td><td>401.92 (-15.68%)</td><td>371.70 <b>(-27.44%)</b></td><td>270.80 (-3.15%)</td><td>135.80 (+18.55%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>566.20 (n/a)</td><td>476.64 (n/a)</td><td>512.30 (n/a)</td><td>279.60 (n/a)</td><td>114.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.07 (-1.94%)</td><td>0.05 (+2.28%)</td><td>0.04 (-2.28%)</td><td>0.03 <b>(+348.72%)</b></td><td>0.01 <b>(-44.54%)</b></td><td>563.00 <b>(-77.71%)</b></td><td>435.46 <b>(-46.25%)</b></td><td>429.20 (+2.34%)</td><td>264.30 (+2.01%)</td><td>111.22 <b>(-88.50%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2526.20 (n/a)</td><td>810.14 (n/a)</td><td>419.40 (n/a)</td><td>259.10 (n/a)</td><td>967.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.10 <b>(+56.19%)</b></td><td>0.07 <b>(+46.18%)</b></td><td>0.07 <b>(+33.82%)</b></td><td>0.04 <b>(+47.59%)</b></td><td>0.02 <b>(+60.14%)</b></td><td>456.10 <b>(-32.24%)</b></td><td>291.58 <b>(-31.22%)</b></td><td>273.90 <b>(-25.29%)</b></td><td>188.60 <b>(-35.98%)</b></td><td>99.99 <b>(-31.85%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>673.10 (n/a)</td><td>423.94 (n/a)</td><td>366.60 (n/a)</td><td>294.60 (n/a)</td><td>146.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 (-14.51%)</td><td>0.04 (-19.81%)</td><td>0.04 <b>(-25.23%)</b></td><td>0.02 <b>(-38.38%)</b></td><td>0.02 (+1.03%)</td><td>805.20 <b>(+62.27%)</b></td><td>476.20 <b>(+32.01%)</b></td><td>416.30 <b>(+33.73%)</b></td><td>293.70 (+16.97%)</td><td>208.44 <b>(+83.55%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>496.20 (n/a)</td><td>360.74 (n/a)</td><td>311.30 (n/a)</td><td>251.10 (n/a)</td><td>113.56 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.35 (-4.62%)</td><td>0.26 (-6.36%)</td><td>0.32 <b>(+24.93%)</b></td><td>0.12 <b>(-39.37%)</b></td><td>0.11 <b>(+59.13%)</b></td><td>836.00 <b>(+64.92%)</b></td><td>461.16 <b>(+23.16%)</b></td><td>310.80 (-19.96%)</td><td>282.70 (+4.86%)</td><td>245.91 <b>(+164.37%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>506.90 (n/a)</td><td>374.44 (n/a)</td><td>388.30 (n/a)</td><td>269.60 (n/a)</td><td>93.02 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.39 (-13.06%)</td><td>0.26 (+9.80%)</td><td>0.22 (+19.39%)</td><td>0.13 <b>(-22.44%)</b></td><td>0.11 (-5.64%)</td><td>755.80 <b>(+28.93%)</b></td><td>437.98 (-6.05%)</td><td>437.90 (-16.24%)</td><td>250.70 (+15.00%)</td><td>204.69 <b>(+37.61%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.45 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>586.20 (n/a)</td><td>466.16 (n/a)</td><td>522.80 (n/a)</td><td>218.00 (n/a)</td><td>148.75 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.40 (+12.34%)</td><td>0.26 (+1.39%)</td><td>0.24 (+5.63%)</td><td>0.18 <b>(+20.61%)</b></td><td>0.09 (-4.52%)</td><td>539.50 (-17.09%)</td><td>416.22 (-4.42%)</td><td>409.40 (-5.32%)</td><td>246.00 (-11.00%)</td><td>117.67 <b>(-26.09%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.36 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>650.70 (n/a)</td><td>435.48 (n/a)</td><td>432.40 (n/a)</td><td>276.40 (n/a)</td><td>159.21 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.32 (+1.84%)</td><td>0.22 (+7.61%)</td><td>0.19 (-6.37%)</td><td>0.15 <b>(+63.86%)</b></td><td>0.07 <b>(-29.50%)</b></td><td>498.10 <b>(-38.98%)</b></td><td>370.14 <b>(-20.82%)</b></td><td>397.10 (+6.80%)</td><td>233.50 (-1.81%)</td><td>110.71 <b>(-57.14%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>816.30 (n/a)</td><td>467.46 (n/a)</td><td>371.80 (n/a)</td><td>237.80 (n/a)</td><td>258.33 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.31 (+12.72%)</td><td>0.23 (-0.55%)</td><td>0.25 (+8.21%)</td><td>0.12 <b>(-27.37%)</b></td><td>0.09 <b>(+94.00%)</b></td><td>626.80 <b>(+37.70%)</b></td><td>374.92 (+12.41%)</td><td>289.60 (-7.59%)</td><td>237.10 (-11.30%)</td><td>170.90 <b>(+128.02%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>455.20 (n/a)</td><td>333.52 (n/a)</td><td>313.40 (n/a)</td><td>267.30 (n/a)</td><td>74.95 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.30 (+4.77%)</td><td>0.22 <b>(+41.55%)</b></td><td>0.25 <b>(+91.14%)</b></td><td>0.14 <b>(+95.67%)</b></td><td>0.07 (-10.27%)</td><td>545.00 <b>(-48.89%)</b></td><td>373.06 <b>(-36.35%)</b></td><td>291.80 <b>(-47.69%)</b></td><td>244.10 (-4.54%)</td><td>136.63 <b>(-53.99%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.29 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>1066.40 (n/a)</td><td>586.12 (n/a)</td><td>557.80 (n/a)</td><td>255.70 (n/a)</td><td>296.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 <b>(+28.17%)</b></td><td>0.12 (+12.45%)</td><td>0.12 (+8.98%)</td><td>0.07 (-19.91%)</td><td>0.03 <b>(+119.73%)</b></td><td>519.10 <b>(+24.84%)</b></td><td>337.36 (-5.72%)</td><td>320.00 (-8.26%)</td><td>239.50 <b>(-21.99%)</b></td><td>111.83 <b>(+113.75%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>415.80 (n/a)</td><td>357.84 (n/a)</td><td>348.80 (n/a)</td><td>307.00 (n/a)</td><td>52.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.18 <b>(+27.79%)</b></td><td>0.10 (+8.86%)</td><td>0.08 (-2.59%)</td><td>0.07 <b>(+34.33%)</b></td><td>0.05 <b>(+22.77%)</b></td><td>563.00 <b>(-25.56%)</b></td><td>414.00 (-8.54%)</td><td>465.70 (+2.67%)</td><td>209.10 <b>(-21.77%)</b></td><td>153.80 <b>(-22.69%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>756.30 (n/a)</td><td>452.68 (n/a)</td><td>453.60 (n/a)</td><td>267.30 (n/a)</td><td>198.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (-9.94%)</td><td>0.11 (-1.97%)</td><td>0.13 (+4.28%)</td><td>0.07 (-11.16%)</td><td>0.03 (-5.28%)</td><td>499.20 (+12.56%)</td><td>347.84 (+2.57%)</td><td>288.30 (-4.09%)</td><td>245.10 (+11.06%)</td><td>111.59 (+12.71%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>443.50 (n/a)</td><td>339.14 (n/a)</td><td>300.60 (n/a)</td><td>220.70 (n/a)</td><td>99.00 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (-0.70%)</td><td>0.12 (+10.34%)</td><td>0.13 (+4.14%)</td><td>0.07 <b>(+21.97%)</b></td><td>0.04 (-12.88%)</td><td>504.30 (-18.01%)</td><td>341.34 (-14.64%)</td><td>284.70 (-3.98%)</td><td>240.70 (+0.71%)</td><td>119.67 <b>(-32.96%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>615.10 (n/a)</td><td>399.90 (n/a)</td><td>296.50 (n/a)</td><td>239.00 (n/a)</td><td>178.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (+7.58%)</td><td>0.10 (+2.13%)</td><td>0.07 (-6.07%)</td><td>0.07 (+19.19%)</td><td>0.04 (+0.20%)</td><td>547.10 (-16.10%)</td><td>428.98 (-3.43%)</td><td>528.00 (+6.45%)</td><td>244.40 (-7.04%)</td><td>152.69 (-11.79%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>652.10 (n/a)</td><td>444.22 (n/a)</td><td>496.00 (n/a)</td><td>262.90 (n/a)</td><td>173.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (+7.72%)</td><td>0.12 <b>(+36.64%)</b></td><td>0.12 <b>(+44.87%)</b></td><td>0.07 <b>(+263.73%)</b></td><td>0.03 <b>(-31.04%)</b></td><td>564.80 <b>(-72.51%)</b></td><td>333.40 <b>(-53.15%)</b></td><td>301.60 <b>(-30.98%)</b></td><td>241.30 (-7.19%)</td><td>132.12 <b>(-82.57%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2054.20 (n/a)</td><td>711.56 (n/a)</td><td>437.00 (n/a)</td><td>260.00 (n/a)</td><td>758.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 (+1.17%)</td><td>0.13 (+16.39%)</td><td>0.13 <b>(+45.36%)</b></td><td>0.09 (+14.78%)</td><td>0.03 (-16.36%)</td><td>459.50 (-12.87%)</td><td>338.82 (-17.34%)</td><td>319.90 <b>(-31.20%)</b></td><td>250.70 (-1.14%)</td><td>91.07 <b>(-30.16%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>527.40 (n/a)</td><td>409.90 (n/a)</td><td>465.00 (n/a)</td><td>253.60 (n/a)</td><td>130.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 (+5.69%)</td><td>0.12 (+15.76%)</td><td>0.14 (+0.38%)</td><td>0.08 <b>(+405.46%)</b></td><td>0.03 <b>(-38.23%)</b></td><td>494.20 <b>(-80.22%)</b></td><td>354.74 <b>(-53.49%)</b></td><td>299.10 (-0.37%)</td><td>254.80 (-5.35%)</td><td>107.56 <b>(-88.94%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2498.10 (n/a)</td><td>762.78 (n/a)</td><td>300.20 (n/a)</td><td>269.20 (n/a)</td><td>972.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.21 (+19.62%)</td><td>0.14 (+13.27%)</td><td>0.14 <b>(+52.97%)</b></td><td>0.07 (-3.61%)</td><td>0.06 <b>(+20.21%)</b></td><td>563.00 (+3.74%)</td><td>351.44 (-8.30%)</td><td>291.80 <b>(-34.63%)</b></td><td>199.50 (-16.39%)</td><td>156.39 (+14.75%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>542.70 (n/a)</td><td>383.24 (n/a)</td><td>446.40 (n/a)</td><td>238.60 (n/a)</td><td>136.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.17 (+1.93%)</td><td>0.12 (+10.42%)</td><td>0.11 <b>(+42.17%)</b></td><td>0.07 (+5.37%)</td><td>0.04 (-4.50%)</td><td>553.20 (-5.10%)</td><td>389.48 (-11.15%)</td><td>371.70 <b>(-29.67%)</b></td><td>247.50 (-1.90%)</td><td>137.70 (-11.46%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>582.90 (n/a)</td><td>438.36 (n/a)</td><td>528.50 (n/a)</td><td>252.30 (n/a)</td><td>155.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.16 (-6.16%)</td><td>0.11 (+14.07%)</td><td>0.10 <b>(+21.16%)</b></td><td>0.07 (-2.06%)</td><td>0.04 (-9.76%)</td><td>561.00 (+2.09%)</td><td>400.04 (-13.37%)</td><td>429.50 (-17.45%)</td><td>248.90 (+6.60%)</td><td>129.76 (-1.29%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>549.50 (n/a)</td><td>461.76 (n/a)</td><td>520.30 (n/a)</td><td>233.50 (n/a)</td><td>131.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.12 <b>(-32.65%)</b></td><td>0.09 <b>(-21.29%)</b></td><td>0.11 (+12.10%)</td><td>0.04 <b>(-44.32%)</b></td><td>0.03 <b>(-33.43%)</b></td><td>1007.50 <b>(+79.59%)</b></td><td>518.68 <b>(+31.01%)</b></td><td>380.90 (-10.80%)</td><td>356.20 <b>(+48.48%)</b></td><td>276.62 <b>(+93.04%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>561.00 (n/a)</td><td>395.92 (n/a)</td><td>427.00 (n/a)</td><td>239.90 (n/a)</td><td>143.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 <b>(+21.14%)</b></td><td>0.11 (+6.60%)</td><td>0.10 (-14.69%)</td><td>0.08 (+7.95%)</td><td>0.03 <b>(+26.05%)</b></td><td>433.70 (-7.35%)</td><td>342.58 (-5.23%)</td><td>365.20 (+17.20%)</td><td>230.30 (-17.46%)</td><td>92.30 (-4.67%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>468.10 (n/a)</td><td>361.48 (n/a)</td><td>311.60 (n/a)</td><td>279.00 (n/a)</td><td>96.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (+1.21%)</td><td>0.10 <b>(+30.81%)</b></td><td>0.09 <b>(+43.79%)</b></td><td>0.06 (+8.27%)</td><td>0.03 (+0.07%)</td><td>620.20 (-7.63%)</td><td>389.80 <b>(-24.06%)</b></td><td>368.20 <b>(-30.45%)</b></td><td>263.30 (-1.16%)</td><td>145.25 (-6.36%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>671.40 (n/a)</td><td>513.30 (n/a)</td><td>529.40 (n/a)</td><td>266.40 (n/a)</td><td>155.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (-5.19%)</td><td>0.10 (-9.48%)</td><td>0.08 <b>(-26.63%)</b></td><td>0.07 (-0.33%)</td><td>0.03 (-9.14%)</td><td>517.30 (+0.33%)</td><td>389.26 (+9.16%)</td><td>441.20 <b>(+36.30%)</b></td><td>248.90 (+5.47%)</td><td>112.88 (-5.81%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>515.60 (n/a)</td><td>356.58 (n/a)</td><td>323.70 (n/a)</td><td>236.00 (n/a)</td><td>119.84 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 <b>(+94.71%)</b></td><td>0.10 <b>(+80.97%)</b></td><td>0.11 <b>(+64.99%)</b></td><td>0.05 <b>(+182.39%)</b></td><td>0.03 <b>(+57.56%)</b></td><td>635.10 <b>(-64.59%)</b></td><td>379.64 <b>(-51.59%)</b></td><td>307.10 <b>(-39.39%)</b></td><td>245.10 <b>(-48.64%)</b></td><td>158.50 <b>(-72.07%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1793.40 (n/a)</td><td>784.24 (n/a)</td><td>506.70 (n/a)</td><td>477.20 (n/a)</td><td>567.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (+1.37%)</td><td>0.08 (-5.78%)</td><td>0.07 (+2.78%)</td><td>0.06 (+12.22%)</td><td>0.03 (-11.70%)</td><td>564.20 (-10.90%)</td><td>464.68 (+2.53%)</td><td>491.70 (-2.71%)</td><td>263.50 (-1.35%)</td><td>120.25 <b>(-23.44%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>633.20 (n/a)</td><td>453.22 (n/a)</td><td>505.40 (n/a)</td><td>267.10 (n/a)</td><td>157.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.13 (-3.17%)</td><td>0.07 (-10.71%)</td><td>0.06 (-14.78%)</td><td>0.02 (+5.81%)</td><td>0.04 (+10.34%)</td><td>1887.20 (-5.49%)</td><td>841.04 (+14.50%)</td><td>552.10 (+17.34%)</td><td>277.40 (+3.28%)</td><td>667.36 (-6.15%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1996.80 (n/a)</td><td>734.54 (n/a)</td><td>470.50 (n/a)</td><td>268.60 (n/a)</td><td>711.07 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.59 <b>(+21.15%)</b></td><td>0.31 (-11.10%)</td><td>0.23 <b>(-20.06%)</b></td><td>0.21 (-18.88%)</td><td>0.16 <b>(+52.44%)</b></td><td>633.20 <b>(+23.26%)</b></td><td>494.96 <b>(+21.26%)</b></td><td>561.60 <b>(+25.11%)</b></td><td>220.40 (-17.45%)</td><td>160.78 <b>(+41.96%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>513.70 (n/a)</td><td>408.18 (n/a)</td><td>448.90 (n/a)</td><td>267.00 (n/a)</td><td>113.25 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.56 <b>(+23.06%)</b></td><td>0.36 (+13.51%)</td><td>0.37 <b>(+37.59%)</b></td><td>0.13 <b>(-48.06%)</b></td><td>0.16 <b>(+79.36%)</b></td><td>1030.60 <b>(+92.53%)</b></td><td>467.20 (+7.71%)</td><td>353.90 <b>(-27.33%)</b></td><td>233.80 (-18.73%)</td><td>323.01 <b>(+201.78%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.09 (n/a)</td><td>535.30 (n/a)</td><td>433.76 (n/a)</td><td>487.00 (n/a)</td><td>287.70 (n/a)</td><td>107.04 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.50 (-6.63%)</td><td>0.31 (-14.48%)</td><td>0.27 (-4.87%)</td><td>0.18 (-18.70%)</td><td>0.13 (-10.84%)</td><td>731.10 <b>(+23.00%)</b></td><td>479.56 (+18.07%)</td><td>487.50 (+5.11%)</td><td>262.80 (+7.09%)</td><td>187.62 <b>(+24.22%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.53 (n/a)</td><td>0.37 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>594.40 (n/a)</td><td>406.16 (n/a)</td><td>463.80 (n/a)</td><td>245.40 (n/a)</td><td>151.04 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (-18.07%)</td><td>0.01 <b>(-23.51%)</b></td><td>0.01 <b>(-28.72%)</b></td><td>0.01 <b>(-36.39%)</b></td><td>0.00 (-13.57%)</td><td>657.80 <b>(+57.18%)</b></td><td>421.50 <b>(+34.58%)</b></td><td>446.40 <b>(+40.29%)</b></td><td>259.40 <b>(+22.07%)</b></td><td>157.71 <b>(+64.29%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>418.50 (n/a)</td><td>313.20 (n/a)</td><td>318.20 (n/a)</td><td>212.50 (n/a)</td><td>95.99 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+1.46%)</td><td>0.02 (+14.02%)</td><td>0.02 (+3.60%)</td><td>0.01 <b>(+99.49%)</b></td><td>0.00 <b>(-61.98%)</b></td><td>309.10 <b>(-49.87%)</b></td><td>262.08 <b>(-21.53%)</b></td><td>257.30 (-3.49%)</td><td>236.60 (-1.42%)</td><td>28.46 <b>(-82.10%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>616.60 (n/a)</td><td>334.00 (n/a)</td><td>266.60 (n/a)</td><td>240.00 (n/a)</td><td>158.97 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+10.72%)</td><td>0.01 (-1.66%)</td><td>0.01 <b>(-27.98%)</b></td><td>0.01 (+19.79%)</td><td>0.00 (-9.05%)</td><td>469.20 (-16.53%)</td><td>366.58 (-3.38%)</td><td>388.80 <b>(+38.81%)</b></td><td>220.30 (-9.68%)</td><td>108.09 <b>(-32.72%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.10 (n/a)</td><td>379.42 (n/a)</td><td>280.10 (n/a)</td><td>243.90 (n/a)</td><td>160.65 (n/a)</td>
</tr>
</tbody>
</table>


### test_strided_copy[kv_llama_full]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>9.23 (+5.06%)</td><td>7.67 (+11.48%)</td><td>7.95 (+9.52%)</td><td>5.92 <b>(+70.49%)</b></td><td>1.26 <b>(-37.45%)</b></td><td>354.50 <b>(-41.35%)</b></td><td>280.04 (-17.52%)</td><td>264.00 (-8.68%)</td><td>227.20 (-4.82%)</td><td>48.99 <b>(-67.27%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>8.79 (n/a)</td><td>6.88 (n/a)</td><td>7.26 (n/a)</td><td>3.47 (n/a)</td><td>2.01 (n/a)</td><td>604.40 (n/a)</td><td>339.52 (n/a)</td><td>289.10 (n/a)</td><td>238.70 (n/a)</td><td>149.67 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.51 <b>(-23.60%)</b></td><td>0.43 (-9.55%)</td><td>0.43 <b>(-23.61%)</b></td><td>0.38 <b>(+64.45%)</b></td><td>0.05 <b>(-70.44%)</b></td><td>344.70 <b>(-39.20%)</b></td><td>307.68 (-3.46%)</td><td>305.80 <b>(+30.91%)</b></td><td>259.20 <b>(+30.91%)</b></td><td>35.88 <b>(-76.49%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.67 (n/a)</td><td>0.48 (n/a)</td><td>0.57 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>566.90 (n/a)</td><td>318.70 (n/a)</td><td>233.60 (n/a)</td><td>198.00 (n/a)</td><td>152.63 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.53 (-8.63%)</td><td>0.41 (-14.94%)</td><td>0.46 (-13.61%)</td><td>0.27 (+3.64%)</td><td>0.13 (+0.82%)</td><td>490.30 (-3.52%)</td><td>352.36 (+18.14%)</td><td>284.60 (+15.79%)</td><td>251.40 (+9.45%)</td><td>123.71 (+4.50%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.58 (n/a)</td><td>0.48 (n/a)</td><td>0.54 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>508.20 (n/a)</td><td>298.26 (n/a)</td><td>245.80 (n/a)</td><td>229.70 (n/a)</td><td>118.39 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.56 (+5.76%)</td><td>0.46 (+4.33%)</td><td>0.48 (-6.38%)</td><td>0.32 (-0.62%)</td><td>0.09 (-16.95%)</td><td>416.90 (+0.63%)</td><td>297.64 (-5.82%)</td><td>275.10 (+6.83%)</td><td>236.20 (-5.44%)</td><td>70.06 (-17.96%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.53 (n/a)</td><td>0.44 (n/a)</td><td>0.51 (n/a)</td><td>0.32 (n/a)</td><td>0.11 (n/a)</td><td>414.30 (n/a)</td><td>316.02 (n/a)</td><td>257.50 (n/a)</td><td>249.80 (n/a)</td><td>85.40 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.59 (+5.60%)</td><td>0.51 <b>(+21.57%)</b></td><td>0.50 (+7.34%)</td><td>0.46 <b>(+67.84%)</b></td><td>0.05 <b>(-57.72%)</b></td><td>286.60 <b>(-40.43%)</b></td><td>263.14 <b>(-23.63%)</b></td><td>266.70 (-6.81%)</td><td>222.60 (-5.32%)</td><td>25.85 <b>(-77.16%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.56 (n/a)</td><td>0.42 (n/a)</td><td>0.46 (n/a)</td><td>0.27 (n/a)</td><td>0.13 (n/a)</td><td>481.10 (n/a)</td><td>344.58 (n/a)</td><td>286.20 (n/a)</td><td>235.10 (n/a)</td><td>113.19 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.62 (-2.78%)</td><td>0.45 (-11.05%)</td><td>0.40 (-19.52%)</td><td>0.31 <b>(-21.51%)</b></td><td>0.13 <b>(+50.97%)</b></td><td>422.90 <b>(+27.42%)</b></td><td>313.44 (+17.50%)</td><td>328.00 <b>(+24.24%)</b></td><td>211.40 (+2.87%)</td><td>88.00 <b>(+95.59%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.64 (n/a)</td><td>0.51 (n/a)</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.09 (n/a)</td><td>331.90 (n/a)</td><td>266.76 (n/a)</td><td>264.00 (n/a)</td><td>205.50 (n/a)</td><td>44.99 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (-10.38%)</td><td>0.01 (+19.49%)</td><td>0.01 <b>(+35.13%)</b></td><td>0.01 <b>(+46.23%)</b></td><td>0.00 <b>(-39.13%)</b></td><td>494.90 <b>(-31.62%)</b></td><td>314.72 <b>(-25.97%)</b></td><td>276.90 <b>(-26.00%)</b></td><td>247.80 (+11.57%)</td><td>101.67 <b>(-50.66%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>723.70 (n/a)</td><td>425.14 (n/a)</td><td>374.20 (n/a)</td><td>222.10 (n/a)</td><td>206.06 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.02 (+11.33%)</td><td>0.01 (-15.00%)</td><td>0.01 <b>(-23.25%)</b></td><td>0.01 <b>(-40.60%)</b></td><td>0.00 <b>(+315.34%)</b></td><td>561.60 <b>(+68.35%)</b></td><td>394.48 <b>(+29.33%)</b></td><td>390.10 <b>(+30.29%)</b></td><td>249.90 (-10.17%)</td><td>135.01 <b>(+515.22%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>333.60 (n/a)</td><td>305.02 (n/a)</td><td>299.40 (n/a)</td><td>278.20 (n/a)</td><td>21.94 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.00 <b>(+133.33%)</b></td><td>0.00 <b>(+81.82%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+374.34%)</b></td><td>18987.08 (-13.84%)</td><td>12217.26 <b>(-34.43%)</b></td><td>9966.58 <b>(-47.64%)</b></td><td>5704.51 <b>(-61.46%)</b></td><td>5729.15 <b>(+109.26%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22035.99 (n/a)</td><td>18632.01 (n/a)</td><td>19035.50 (n/a)</td><td>14801.57 (n/a)</td><td>2737.83 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.00 <b>(+30.00%)</b></td><td>0.00 (-12.12%)</td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+28.57%)</b></td><td>21447.14 (-4.77%)</td><td>16986.69 (+11.99%)</td><td>18864.81 (+17.22%)</td><td>6226.98 <b>(-20.33%)</b></td><td>6119.68 (-9.90%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22520.44 (n/a)</td><td>15168.15 (n/a)</td><td>16093.07 (n/a)</td><td>7815.52 (n/a)</td><td>6792.07 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (+0.92%)</td><td>0.10 (+4.39%)</td><td>0.08 (-8.45%)</td><td>0.07 (-4.98%)</td><td>0.04 <b>(+40.59%)</b></td><td>29690.55 (+5.24%)</td><td>23341.72 (+1.14%)</td><td>27660.49 (+9.26%)</td><td>14781.02 (-0.91%)</td><td>7752.70 <b>(+49.13%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28213.40 (n/a)</td><td>23078.94 (n/a)</td><td>25316.44 (n/a)</td><td>14917.12 (n/a)</td><td>5198.55 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/transpose</summary>


### test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>2.83 (+5.67%)</td><td>1.76 (+16.00%)</td><td>1.66 (+5.77%)</td><td>0.30 (-6.30%)</td><td>0.99 (+16.78%)</td><td>3522.90 (+6.73%)</td><td>1126.68 (-2.29%)</td><td>632.40 (-5.46%)</td><td>370.80 (-5.36%)</td><td>1346.27 (+11.35%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.68 (n/a)</td><td>1.52 (n/a)</td><td>1.57 (n/a)</td><td>0.32 (n/a)</td><td>0.84 (n/a)</td><td>3300.90 (n/a)</td><td>1153.12 (n/a)</td><td>668.90 (n/a)</td><td>391.80 (n/a)</td><td>1209.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>2.72 (-5.32%)</td><td>1.79 (-2.96%)</td><td>1.83 (+9.94%)</td><td>1.17 (+0.84%)</td><td>0.64 (+0.92%)</td><td>893.10 (-0.83%)</td><td>648.00 (+4.66%)</td><td>572.10 (-9.05%)</td><td>385.80 (+5.61%)</td><td>222.03 (+15.50%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>2.87 (n/a)</td><td>1.84 (n/a)</td><td>1.67 (n/a)</td><td>1.16 (n/a)</td><td>0.63 (n/a)</td><td>900.60 (n/a)</td><td>619.16 (n/a)</td><td>629.00 (n/a)</td><td>365.30 (n/a)</td><td>192.24 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.63 <b>(+21.91%)</b></td><td>2.22 <b>(+73.35%)</b></td><td>1.72 <b>(+62.72%)</b></td><td>1.62 <b>(+438.68%)</b></td><td>0.87 <b>(-20.59%)</b></td><td>648.50 <b>(-81.44%)</b></td><td>520.18 <b>(-67.30%)</b></td><td>608.80 <b>(-38.54%)</b></td><td>288.60 (-17.96%)</td><td>159.20 <b>(-88.16%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.98 (n/a)</td><td>1.28 (n/a)</td><td>1.06 (n/a)</td><td>0.30 (n/a)</td><td>1.09 (n/a)</td><td>3493.40 (n/a)</td><td>1590.62 (n/a)</td><td>990.60 (n/a)</td><td>351.80 (n/a)</td><td>1344.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.20 (-4.35%)</td><td>2.02 (+1.57%)</td><td>2.01 (+13.57%)</td><td>1.35 (+14.36%)</td><td>0.74 (-9.77%)</td><td>777.00 (-12.55%)</td><td>569.10 (-3.57%)</td><td>522.10 (-11.96%)</td><td>327.30 (+4.54%)</td><td>180.13 (-12.93%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.35 (n/a)</td><td>1.99 (n/a)</td><td>1.77 (n/a)</td><td>1.18 (n/a)</td><td>0.81 (n/a)</td><td>888.50 (n/a)</td><td>590.16 (n/a)</td><td>593.00 (n/a)</td><td>313.10 (n/a)</td><td>206.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.16 <b>(+61.22%)</b></td><td>2.21 (+6.53%)</td><td>2.32 <b>(+26.19%)</b></td><td>0.30 <b>(-81.57%)</b></td><td>1.40 <b>(+209.90%)</b></td><td>3511.80 <b>(+442.53%)</b></td><td>1047.58 <b>(+100.01%)</b></td><td>451.10 <b>(-20.75%)</b></td><td>252.30 <b>(-37.96%)</b></td><td>1383.64 <b>(+1172.29%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.58 (n/a)</td><td>2.08 (n/a)</td><td>1.84 (n/a)</td><td>1.62 (n/a)</td><td>0.45 (n/a)</td><td>647.30 (n/a)</td><td>523.76 (n/a)</td><td>569.20 (n/a)</td><td>406.70 (n/a)</td><td>108.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.00 <b>(-20.24%)</b></td><td>2.12 (-0.61%)</td><td>1.78 (-1.19%)</td><td>1.26 (-19.13%)</td><td>0.76 (-17.59%)</td><td>835.20 <b>(+23.66%)</b></td><td>549.46 (+1.09%)</td><td>588.30 (+1.20%)</td><td>349.00 <b>(+25.36%)</b></td><td>198.89 <b>(+29.77%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.77 (n/a)</td><td>2.13 (n/a)</td><td>1.80 (n/a)</td><td>1.55 (n/a)</td><td>0.92 (n/a)</td><td>675.40 (n/a)</td><td>543.54 (n/a)</td><td>581.30 (n/a)</td><td>278.40 (n/a)</td><td>153.27 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.28 <b>(+34.65%)</b></td><td>2.63 <b>(+41.90%)</b></td><td>1.93 <b>(+25.80%)</b></td><td>1.70 <b>(+22.04%)</b></td><td>1.16 <b>(+55.11%)</b></td><td>616.50 (-18.05%)</td><td>457.84 <b>(-26.07%)</b></td><td>543.90 <b>(-20.52%)</b></td><td>244.90 <b>(-25.74%)</b></td><td>169.61 (+1.68%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.18 (n/a)</td><td>1.85 (n/a)</td><td>1.53 (n/a)</td><td>1.39 (n/a)</td><td>0.75 (n/a)</td><td>752.30 (n/a)</td><td>619.30 (n/a)</td><td>684.30 (n/a)</td><td>329.80 (n/a)</td><td>166.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>3.42 (+15.72%)</td><td>2.00 (-15.76%)</td><td>1.92 (-16.79%)</td><td>0.30 <b>(-83.18%)</b></td><td>1.19 <b>(+164.52%)</b></td><td>3483.00 <b>(+494.67%)</b></td><td>1075.72 <b>(+136.07%)</b></td><td>546.40 <b>(+20.19%)</b></td><td>307.00 (-13.57%)</td><td>1352.93 <b>(+1418.77%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>2.95 (n/a)</td><td>2.37 (n/a)</td><td>2.31 (n/a)</td><td>1.79 (n/a)</td><td>0.45 (n/a)</td><td>585.70 (n/a)</td><td>455.68 (n/a)</td><td>454.60 (n/a)</td><td>355.20 (n/a)</td><td>89.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.73 (+1.40%)</td><td>2.37 (-6.23%)</td><td>3.02 (+6.90%)</td><td>0.60 (+0.06%)</td><td>1.40 (+9.69%)</td><td>3510.00 (-0.06%)</td><td>1440.80 (+11.27%)</td><td>693.30 (-6.45%)</td><td>562.90 (-1.38%)</td><td>1265.87 (+0.87%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.67 (n/a)</td><td>2.53 (n/a)</td><td>2.83 (n/a)</td><td>0.60 (n/a)</td><td>1.28 (n/a)</td><td>3512.10 (n/a)</td><td>1294.86 (n/a)</td><td>741.10 (n/a)</td><td>570.80 (n/a)</td><td>1254.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>4.27 (+5.01%)</td><td>2.38 (-0.41%)</td><td>2.30 <b>(-23.02%)</b></td><td>0.85 <b>(+44.01%)</b></td><td>1.22 <b>(-27.53%)</b></td><td>2480.30 <b>(-30.56%)</b></td><td>1151.68 <b>(-35.14%)</b></td><td>912.40 <b>(+29.90%)</b></td><td>491.60 (-4.77%)</td><td>766.82 <b>(-52.63%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.06 (n/a)</td><td>2.39 (n/a)</td><td>2.99 (n/a)</td><td>0.59 (n/a)</td><td>1.69 (n/a)</td><td>3572.00 (n/a)</td><td>1775.74 (n/a)</td><td>702.40 (n/a)</td><td>516.20 (n/a)</td><td>1618.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>5.81 (+17.96%)</td><td>2.53 <b>(-22.95%)</b></td><td>2.45 (-19.25%)</td><td>0.59 <b>(-74.31%)</b></td><td>2.14 <b>(+103.92%)</b></td><td>3535.00 <b>(+289.27%)</b></td><td>1715.62 <b>(+150.05%)</b></td><td>856.20 <b>(+23.84%)</b></td><td>361.10 (-15.23%)</td><td>1506.72 <b>(+675.83%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>4.92 (n/a)</td><td>3.29 (n/a)</td><td>3.03 (n/a)</td><td>2.31 (n/a)</td><td>1.05 (n/a)</td><td>908.10 (n/a)</td><td>686.12 (n/a)</td><td>691.40 (n/a)</td><td>426.00 (n/a)</td><td>194.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.35 <b>(+62.04%)</b></td><td>3.73 <b>(+74.69%)</b></td><td>3.84 <b>(+33.01%)</b></td><td>1.65 <b>(+179.02%)</b></td><td>1.65 (+16.55%)</td><td>1269.90 <b>(-64.16%)</b></td><td>687.54 <b>(-61.85%)</b></td><td>545.90 <b>(-24.82%)</b></td><td>392.20 <b>(-38.29%)</b></td><td>371.48 <b>(-76.12%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>3.30 (n/a)</td><td>2.13 (n/a)</td><td>2.89 (n/a)</td><td>0.59 (n/a)</td><td>1.41 (n/a)</td><td>3543.40 (n/a)</td><td>1802.06 (n/a)</td><td>726.10 (n/a)</td><td>635.60 (n/a)</td><td>1555.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.85 <b>(-34.29%)</b></td><td>3.16 (-18.29%)</td><td>3.54 (+19.72%)</td><td>0.84 <b>(+44.87%)</b></td><td>1.48 <b>(-45.28%)</b></td><td>2507.30 <b>(-30.97%)</b></td><td>964.98 (-16.55%)</td><td>593.00 (-16.48%)</td><td>432.60 <b>(+52.16%)</b></td><td>868.40 <b>(-38.03%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>7.38 (n/a)</td><td>3.87 (n/a)</td><td>2.95 (n/a)</td><td>0.58 (n/a)</td><td>2.70 (n/a)</td><td>3632.40 (n/a)</td><td>1156.42 (n/a)</td><td>710.00 (n/a)</td><td>284.30 (n/a)</td><td>1401.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>4.95 (-15.99%)</td><td>4.07 <b>(+21.39%)</b></td><td>4.13 <b>(+23.08%)</b></td><td>3.21 <b>(+439.17%)</b></td><td>0.83 <b>(-56.43%)</b></td><td>652.90 <b>(-81.45%)</b></td><td>533.80 <b>(-53.45%)</b></td><td>507.60 (-18.76%)</td><td>423.60 (+19.02%)</td><td>110.95 <b>(-91.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.89 (n/a)</td><td>3.35 (n/a)</td><td>3.36 (n/a)</td><td>0.60 (n/a)</td><td>1.90 (n/a)</td><td>3520.50 (n/a)</td><td>1146.74 (n/a)</td><td>624.80 (n/a)</td><td>355.90 (n/a)</td><td>1332.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>5.14 <b>(+26.30%)</b></td><td>2.90 (+7.49%)</td><td>2.74 (+8.52%)</td><td>0.59 (-3.85%)</td><td>1.76 <b>(+28.52%)</b></td><td>3558.60 (+4.01%)</td><td>1258.40 (+2.13%)</td><td>764.80 (-7.84%)</td><td>408.10 <b>(-20.82%)</b></td><td>1308.44 (+6.10%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>4.07 (n/a)</td><td>2.70 (n/a)</td><td>2.53 (n/a)</td><td>0.61 (n/a)</td><td>1.37 (n/a)</td><td>3421.50 (n/a)</td><td>1232.20 (n/a)</td><td>829.90 (n/a)</td><td>515.40 (n/a)</td><td>1233.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.47 (-3.67%)</td><td>3.39 (-10.38%)</td><td>2.67 <b>(-49.85%)</b></td><td>1.75 <b>(+199.68%)</b></td><td>1.54 <b>(-37.16%)</b></td><td>1197.20 <b>(-66.63%)</b></td><td>729.76 <b>(-38.72%)</b></td><td>786.90 <b>(+99.42%)</b></td><td>383.50 (+3.82%)</td><td>323.98 <b>(-76.69%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.68 (n/a)</td><td>3.79 (n/a)</td><td>5.31 (n/a)</td><td>0.58 (n/a)</td><td>2.45 (n/a)</td><td>3587.70 (n/a)</td><td>1190.90 (n/a)</td><td>394.60 (n/a)</td><td>369.40 (n/a)</td><td>1389.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>6.34 (+2.01%)</td><td>3.25 <b>(-22.81%)</b></td><td>2.90 <b>(-22.21%)</b></td><td>0.59 <b>(-75.70%)</b></td><td>2.07 (+11.49%)</td><td>3553.00 <b>(+311.51%)</b></td><td>1186.94 <b>(+103.25%)</b></td><td>724.10 <b>(+28.57%)</b></td><td>330.60 (-1.96%)</td><td>1333.22 <b>(+432.41%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>6.22 (n/a)</td><td>4.22 (n/a)</td><td>3.72 (n/a)</td><td>2.43 (n/a)</td><td>1.86 (n/a)</td><td>863.40 (n/a)</td><td>583.98 (n/a)</td><td>563.20 (n/a)</td><td>337.20 (n/a)</td><td>250.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.96 <b>(+23.76%)</b></td><td>3.51 (+6.96%)</td><td>2.99 <b>(-26.20%)</b></td><td>1.55 <b>(+163.99%)</b></td><td>1.64 (-1.15%)</td><td>1350.70 <b>(-62.12%)</b></td><td>726.38 <b>(-37.04%)</b></td><td>702.50 <b>(+35.51%)</b></td><td>352.00 (-19.21%)</td><td>379.90 <b>(-71.92%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.81 (n/a)</td><td>3.28 (n/a)</td><td>4.05 (n/a)</td><td>0.59 (n/a)</td><td>1.66 (n/a)</td><td>3565.60 (n/a)</td><td>1153.72 (n/a)</td><td>518.40 (n/a)</td><td>435.70 (n/a)</td><td>1352.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>5.92 (+14.23%)</td><td>3.25 <b>(+28.77%)</b></td><td>3.99 <b>(+100.37%)</b></td><td>0.57 (-6.58%)</td><td>2.53 <b>(+47.88%)</b></td><td>3647.80 (+7.04%)</td><td>1691.08 <b>(+26.08%)</b></td><td>525.00 <b>(-50.10%)</b></td><td>354.00 (-12.46%)</td><td>1730.72 <b>(+45.22%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>5.19 (n/a)</td><td>2.52 (n/a)</td><td>1.99 (n/a)</td><td>0.62 (n/a)</td><td>1.71 (n/a)</td><td>3407.90 (n/a)</td><td>1341.30 (n/a)</td><td>1052.00 (n/a)</td><td>404.40 (n/a)</td><td>1191.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.28 <b>(+28.71%)</b></td><td>3.36 (+19.70%)</td><td>3.13 (-12.45%)</td><td>0.60 (+2.21%)</td><td>1.86 (+17.42%)</td><td>3522.30 (-2.17%)</td><td>1147.98 (-11.03%)</td><td>670.40 (+14.21%)</td><td>396.90 <b>(-22.31%)</b></td><td>1334.91 (+0.60%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>4.10 (n/a)</td><td>2.81 (n/a)</td><td>3.57 (n/a)</td><td>0.58 (n/a)</td><td>1.59 (n/a)</td><td>3600.30 (n/a)</td><td>1290.32 (n/a)</td><td>587.00 (n/a)</td><td>510.90 (n/a)</td><td>1326.95 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>4.04 <b>(-24.57%)</b></td><td>2.41 <b>(-38.98%)</b></td><td>1.70 <b>(-58.39%)</b></td><td>1.13 (-0.72%)</td><td>1.50 (-10.73%)</td><td>3698.70 (+0.73%)</td><td>2372.06 <b>(+61.70%)</b></td><td>2467.80 <b>(+140.32%)</b></td><td>1039.20 <b>(+32.58%)</b></td><td>1308.78 (+5.72%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>5.35 (n/a)</td><td>3.95 (n/a)</td><td>4.08 (n/a)</td><td>1.14 (n/a)</td><td>1.67 (n/a)</td><td>3672.00 (n/a)</td><td>1466.96 (n/a)</td><td>1026.90 (n/a)</td><td>783.80 (n/a)</td><td>1237.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>5.37 (+1.85%)</td><td>3.79 (-0.55%)</td><td>4.04 (-3.64%)</td><td>1.21 (-1.35%)</td><td>1.55 (+0.44%)</td><td>3452.90 (+1.37%)</td><td>1457.76 (+0.94%)</td><td>1037.80 (+3.78%)</td><td>781.10 (-1.81%)</td><td>1120.90 (+1.67%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>5.27 (n/a)</td><td>3.82 (n/a)</td><td>4.19 (n/a)</td><td>1.23 (n/a)</td><td>1.54 (n/a)</td><td>3406.10 (n/a)</td><td>1444.20 (n/a)</td><td>1000.00 (n/a)</td><td>795.50 (n/a)</td><td>1102.52 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>8.31 (+9.86%)</td><td>5.20 <b>(+45.76%)</b></td><td>6.35 <b>(+92.55%)</b></td><td>1.12 (+2.37%)</td><td>2.95 (+9.15%)</td><td>3737.00 (-2.31%)</td><td>1359.66 <b>(-32.63%)</b></td><td>660.60 <b>(-48.07%)</b></td><td>504.60 (-8.98%)</td><td>1365.08 (-11.78%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>7.57 (n/a)</td><td>3.57 (n/a)</td><td>3.30 (n/a)</td><td>1.10 (n/a)</td><td>2.70 (n/a)</td><td>3825.50 (n/a)</td><td>2018.18 (n/a)</td><td>1272.00 (n/a)</td><td>554.40 (n/a)</td><td>1547.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>8.72 (+12.22%)</td><td>5.54 (-13.52%)</td><td>4.21 <b>(-37.76%)</b></td><td>2.86 <b>(-24.46%)</b></td><td>2.53 <b>(+57.48%)</b></td><td>1466.70 <b>(+32.37%)</b></td><td>897.28 <b>(+28.02%)</b></td><td>995.70 <b>(+60.67%)</b></td><td>480.80 (-10.90%)</td><td>401.00 <b>(+70.78%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>7.77 (n/a)</td><td>6.41 (n/a)</td><td>6.77 (n/a)</td><td>3.79 (n/a)</td><td>1.61 (n/a)</td><td>1108.00 (n/a)</td><td>700.90 (n/a)</td><td>619.70 (n/a)</td><td>539.60 (n/a)</td><td>234.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>7.81 <b>(+33.77%)</b></td><td>5.76 <b>(+58.59%)</b></td><td>5.85 <b>(+71.20%)</b></td><td>1.68 (-14.81%)</td><td>2.46 <b>(+75.44%)</b></td><td>2491.30 (+17.39%)</td><td>1002.98 <b>(-22.95%)</b></td><td>716.70 <b>(-41.59%)</b></td><td>536.90 <b>(-25.25%)</b></td><td>836.55 <b>(+63.02%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>5.84 (n/a)</td><td>3.63 (n/a)</td><td>3.42 (n/a)</td><td>1.98 (n/a)</td><td>1.40 (n/a)</td><td>2122.20 (n/a)</td><td>1301.74 (n/a)</td><td>1227.10 (n/a)</td><td>718.30 (n/a)</td><td>513.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>7.21 <b>(-20.35%)</b></td><td>4.99 (-10.67%)</td><td>4.41 <b>(-29.75%)</b></td><td>3.49 <b>(+84.64%)</b></td><td>1.46 <b>(-56.57%)</b></td><td>1200.90 <b>(-45.84%)</b></td><td>895.24 <b>(-21.47%)</b></td><td>950.80 <b>(+42.36%)</b></td><td>581.60 <b>(+25.56%)</b></td><td>239.06 <b>(-71.25%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>9.05 (n/a)</td><td>5.59 (n/a)</td><td>6.28 (n/a)</td><td>1.89 (n/a)</td><td>3.37 (n/a)</td><td>2217.30 (n/a)</td><td>1139.96 (n/a)</td><td>667.90 (n/a)</td><td>463.20 (n/a)</td><td>831.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>10.41 (+11.97%)</td><td>6.81 <b>(+117.78%)</b></td><td>6.70 <b>(+241.98%)</b></td><td>4.35 <b>(+286.34%)</b></td><td>2.57 <b>(-26.18%)</b></td><td>963.10 <b>(-74.12%)</b></td><td>690.50 <b>(-71.18%)</b></td><td>626.10 <b>(-70.76%)</b></td><td>402.80 (-10.69%)</td><td>253.33 <b>(-81.37%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>9.30 (n/a)</td><td>3.13 (n/a)</td><td>1.96 (n/a)</td><td>1.13 (n/a)</td><td>3.48 (n/a)</td><td>3720.80 (n/a)</td><td>2395.82 (n/a)</td><td>2141.10 (n/a)</td><td>451.00 (n/a)</td><td>1359.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>11.34 <b>(+46.16%)</b></td><td>4.97 (-6.08%)</td><td>3.94 <b>(-42.29%)</b></td><td>1.67 <b>(+45.76%)</b></td><td>3.70 <b>(+33.91%)</b></td><td>2516.70 <b>(-31.40%)</b></td><td>1216.70 (-6.92%)</td><td>1063.80 <b>(+73.29%)</b></td><td>369.70 <b>(-31.59%)</b></td><td>787.40 <b>(-41.21%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>7.76 (n/a)</td><td>5.29 (n/a)</td><td>6.83 (n/a)</td><td>1.14 (n/a)</td><td>2.76 (n/a)</td><td>3668.40 (n/a)</td><td>1307.10 (n/a)</td><td>613.90 (n/a)</td><td>540.40 (n/a)</td><td>1339.29 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>9.29 (-15.19%)</td><td>7.53 (-1.03%)</td><td>7.16 (-8.18%)</td><td>6.45 <b>(+55.59%)</b></td><td>1.24 <b>(-62.42%)</b></td><td>650.70 <b>(-35.73%)</b></td><td>568.82 (-13.37%)</td><td>586.00 (+8.90%)</td><td>451.30 (+17.93%)</td><td>88.67 <b>(-71.20%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>10.96 (n/a)</td><td>7.61 (n/a)</td><td>7.79 (n/a)</td><td>4.14 (n/a)</td><td>3.31 (n/a)</td><td>1012.40 (n/a)</td><td>656.62 (n/a)</td><td>538.10 (n/a)</td><td>382.70 (n/a)</td><td>307.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>7.78 <b>(-24.93%)</b></td><td>5.95 (+16.74%)</td><td>6.18 (+9.78%)</td><td>3.89 <b>(+182.61%)</b></td><td>1.55 <b>(-56.33%)</b></td><td>1079.20 <b>(-64.61%)</b></td><td>749.56 <b>(-44.63%)</b></td><td>678.20 (-8.92%)</td><td>539.00 <b>(+33.22%)</b></td><td>217.01 <b>(-80.19%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>10.37 (n/a)</td><td>5.10 (n/a)</td><td>5.63 (n/a)</td><td>1.38 (n/a)</td><td>3.55 (n/a)</td><td>3049.80 (n/a)</td><td>1353.78 (n/a)</td><td>744.60 (n/a)</td><td>404.60 (n/a)</td><td>1095.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>9.35 (+1.03%)</td><td>6.34 (+12.99%)</td><td>6.70 (+0.61%)</td><td>4.27 <b>(+285.59%)</b></td><td>2.06 <b>(-33.90%)</b></td><td>983.30 <b>(-74.06%)</b></td><td>719.14 <b>(-44.77%)</b></td><td>625.90 (-0.62%)</td><td>448.50 (-1.02%)</td><td>226.86 <b>(-83.89%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>9.26 (n/a)</td><td>5.61 (n/a)</td><td>6.66 (n/a)</td><td>1.11 (n/a)</td><td>3.12 (n/a)</td><td>3791.30 (n/a)</td><td>1302.08 (n/a)</td><td>629.80 (n/a)</td><td>453.10 (n/a)</td><td>1408.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>8.34 (-15.31%)</td><td>5.95 (+5.52%)</td><td>7.42 <b>(+69.24%)</b></td><td>1.15 <b>(-66.33%)</b></td><td>3.09 (+16.03%)</td><td>3646.90 <b>(+196.98%)</b></td><td>1228.06 <b>(+42.12%)</b></td><td>564.90 <b>(-40.92%)</b></td><td>502.70 (+18.06%)</td><td>1363.09 <b>(+313.37%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>9.85 (n/a)</td><td>5.64 (n/a)</td><td>4.39 (n/a)</td><td>3.42 (n/a)</td><td>2.66 (n/a)</td><td>1228.00 (n/a)</td><td>864.10 (n/a)</td><td>956.10 (n/a)</td><td>425.80 (n/a)</td><td>329.75 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.66 (-3.07%)</td><td>1.22 (-14.87%)</td><td>1.07 <b>(-29.05%)</b></td><td>0.94 (+3.20%)</td><td>0.31 (-6.57%)</td><td>555.30 (-3.11%)</td><td>451.18 (+16.75%)</td><td>489.20 <b>(+40.94%)</b></td><td>316.10 (+3.17%)</td><td>104.13 (-6.11%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.71 (n/a)</td><td>1.43 (n/a)</td><td>1.51 (n/a)</td><td>0.91 (n/a)</td><td>0.33 (n/a)</td><td>573.10 (n/a)</td><td>386.46 (n/a)</td><td>347.10 (n/a)</td><td>306.40 (n/a)</td><td>110.91 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.28 <b>(+33.87%)</b></td><td>1.32 <b>(-24.42%)</b></td><td>1.35 (-17.28%)</td><td>0.30 <b>(-78.30%)</b></td><td>1.22 <b>(+181.33%)</b></td><td>3526.10 <b>(+360.81%)</b></td><td>1780.26 <b>(+183.10%)</b></td><td>778.70 <b>(+20.90%)</b></td><td>320.10 <b>(-25.30%)</b></td><td>1594.41 <b>(+1089.35%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>2.45 (n/a)</td><td>1.74 (n/a)</td><td>1.63 (n/a)</td><td>1.37 (n/a)</td><td>0.43 (n/a)</td><td>765.20 (n/a)</td><td>628.84 (n/a)</td><td>644.10 (n/a)</td><td>428.50 (n/a)</td><td>134.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>3.50 (+8.85%)</td><td>2.45 (+19.98%)</td><td>2.36 (+6.87%)</td><td>0.76 (-8.49%)</td><td>1.10 (-5.39%)</td><td>2746.30 (+9.28%)</td><td>1158.40 <b>(-20.42%)</b></td><td>887.30 (-6.43%)</td><td>598.30 (-8.14%)</td><td>900.45 (-6.20%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>3.22 (n/a)</td><td>2.04 (n/a)</td><td>2.21 (n/a)</td><td>0.83 (n/a)</td><td>1.16 (n/a)</td><td>2513.10 (n/a)</td><td>1455.72 (n/a)</td><td>948.30 (n/a)</td><td>651.30 (n/a)</td><td>959.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>1.97 (+19.29%)</td><td>1.41 <b>(+26.75%)</b></td><td>1.28 <b>(+31.21%)</b></td><td>0.79 <b>(+38.25%)</b></td><td>0.48 (-2.22%)</td><td>660.60 <b>(-27.67%)</b></td><td>412.38 <b>(-25.88%)</b></td><td>410.70 <b>(-23.79%)</b></td><td>265.60 (-16.16%)</td><td>157.56 <b>(-37.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>1.66 (n/a)</td><td>1.11 (n/a)</td><td>0.97 (n/a)</td><td>0.57 (n/a)</td><td>0.49 (n/a)</td><td>913.30 (n/a)</td><td>556.40 (n/a)</td><td>538.90 (n/a)</td><td>316.80 (n/a)</td><td>252.67 (n/a)</td>
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
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>1.90 (+9.85%)</td><td>1.04 <b>(-25.85%)</b></td><td>0.86 <b>(-49.31%)</b></td><td>0.69 <b>(-22.09%)</b></td><td>0.49 (+15.48%)</td><td>759.20 <b>(+28.35%)</b></td><td>570.40 <b>(+39.97%)</b></td><td>609.80 <b>(+97.28%)</b></td><td>276.60 (-8.95%)</td><td>181.70 <b>(+29.71%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>1.73 (n/a)</td><td>1.40 (n/a)</td><td>1.70 (n/a)</td><td>0.89 (n/a)</td><td>0.42 (n/a)</td><td>591.50 (n/a)</td><td>407.52 (n/a)</td><td>309.10 (n/a)</td><td>303.80 (n/a)</td><td>140.07 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>1.59 (-19.93%)</td><td>1.24 (-13.53%)</td><td>1.30 (-11.39%)</td><td>0.90 (-2.42%)</td><td>0.31 <b>(-21.60%)</b></td><td>579.40 (+2.48%)</td><td>447.26 (+14.39%)</td><td>401.80 (+12.83%)</td><td>329.80 <b>(+24.88%)</b></td><td>116.43 (+2.51%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>1.99 (n/a)</td><td>1.43 (n/a)</td><td>1.47 (n/a)</td><td>0.93 (n/a)</td><td>0.39 (n/a)</td><td>565.40 (n/a)</td><td>390.98 (n/a)</td><td>356.10 (n/a)</td><td>264.10 (n/a)</td><td>113.57 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.15 (+6.10%)</td><td>0.11 <b>(+34.73%)</b></td><td>0.11 <b>(+54.50%)</b></td><td>0.06 (+11.83%)</td><td>0.04 (+9.74%)</td><td>536.90 (-10.59%)</td><td>341.66 <b>(-25.53%)</b></td><td>290.40 <b>(-35.27%)</b></td><td>224.50 (-5.75%)</td><td>133.72 (-7.03%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>600.50 (n/a)</td><td>458.78 (n/a)</td><td>448.60 (n/a)</td><td>238.20 (n/a)</td><td>143.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.14 (+0.75%)</td><td>0.12 <b>(+25.51%)</b></td><td>0.12 <b>(+36.03%)</b></td><td>0.10 <b>(+67.75%)</b></td><td>0.01 <b>(-56.00%)</b></td><td>322.90 <b>(-40.38%)</b></td><td>280.66 <b>(-26.79%)</b></td><td>278.40 <b>(-26.49%)</b></td><td>240.50 (-0.78%)</td><td>34.05 <b>(-73.68%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>541.60 (n/a)</td><td>383.36 (n/a)</td><td>378.70 (n/a)</td><td>242.40 (n/a)</td><td>129.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.14 (+12.52%)</td><td>0.11 (+17.89%)</td><td>0.11 (+6.68%)</td><td>0.06 (+4.72%)</td><td>0.03 (+2.41%)</td><td>564.80 (-4.51%)</td><td>329.70 (-15.76%)</td><td>288.20 (-6.25%)</td><td>240.30 (-11.13%)</td><td>134.03 (-8.42%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>591.50 (n/a)</td><td>391.40 (n/a)</td><td>307.40 (n/a)</td><td>270.40 (n/a)</td><td>146.34 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.15 (+12.42%)</td><td>0.09 (+6.12%)</td><td>0.09 <b>(+32.18%)</b></td><td>0.05 (-19.76%)</td><td>0.04 <b>(+26.65%)</b></td><td>658.70 <b>(+24.61%)</b></td><td>423.32 (+0.01%)</td><td>375.60 <b>(-24.35%)</b></td><td>222.20 (-11.05%)</td><td>180.07 <b>(+38.08%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>528.60 (n/a)</td><td>423.26 (n/a)</td><td>496.50 (n/a)</td><td>249.80 (n/a)</td><td>130.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.22 (+6.61%)</td><td>0.16 (-1.90%)</td><td>0.14 (+0.37%)</td><td>0.11 <b>(-20.29%)</b></td><td>0.05 <b>(+42.51%)</b></td><td>602.10 <b>(+25.46%)</b></td><td>432.26 (+6.37%)</td><td>454.30 (-0.37%)</td><td>297.40 (-6.18%)</td><td>131.23 <b>(+61.84%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>479.90 (n/a)</td><td>406.36 (n/a)</td><td>456.00 (n/a)</td><td>317.00 (n/a)</td><td>81.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.29 (+10.69%)</td><td>0.18 (+9.40%)</td><td>0.12 (-5.48%)</td><td>0.12 (+8.59%)</td><td>0.09 <b>(+30.24%)</b></td><td>567.10 (-7.91%)</td><td>430.14 (-3.32%)</td><td>556.40 (+5.80%)</td><td>222.80 (-9.69%)</td><td>180.68 (+12.51%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>615.80 (n/a)</td><td>444.90 (n/a)</td><td>525.90 (n/a)</td><td>246.70 (n/a)</td><td>160.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.26 <b>(+43.82%)</b></td><td>0.20 <b>(+51.22%)</b></td><td>0.22 <b>(+69.80%)</b></td><td>0.13 <b>(+21.14%)</b></td><td>0.05 <b>(+93.81%)</b></td><td>486.60 (-17.46%)</td><td>345.28 <b>(-31.51%)</b></td><td>299.30 <b>(-41.12%)</b></td><td>250.50 <b>(-30.47%)</b></td><td>101.57 (+15.53%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>589.50 (n/a)</td><td>504.16 (n/a)</td><td>508.30 (n/a)</td><td>360.30 (n/a)</td><td>87.92 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.27 (+14.48%)</td><td>0.16 <b>(-20.48%)</b></td><td>0.13 <b>(-41.15%)</b></td><td>0.10 <b>(-23.64%)</b></td><td>0.07 <b>(+65.25%)</b></td><td>644.20 <b>(+30.96%)</b></td><td>476.14 <b>(+36.29%)</b></td><td>513.00 <b>(+69.92%)</b></td><td>242.90 (-12.66%)</td><td>162.21 <b>(+84.91%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>491.90 (n/a)</td><td>349.36 (n/a)</td><td>301.90 (n/a)</td><td>278.10 (n/a)</td><td>87.72 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.28 (-10.58%)</td><td>0.19 (+14.18%)</td><td>0.15 <b>(+23.74%)</b></td><td>0.10 (-15.65%)</td><td>0.09 (+2.00%)</td><td>643.60 (+18.55%)</td><td>417.76 (-9.11%)</td><td>430.10 (-19.18%)</td><td>230.30 (+11.80%)</td><td>185.20 <b>(+28.67%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.32 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>542.90 (n/a)</td><td>459.62 (n/a)</td><td>532.20 (n/a)</td><td>206.00 (n/a)</td><td>143.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.26 (-13.49%)</td><td>0.20 (+7.41%)</td><td>0.18 <b>(+23.46%)</b></td><td>0.13 (+6.95%)</td><td>0.06 <b>(-24.32%)</b></td><td>491.00 (-6.49%)</td><td>354.42 (-10.52%)</td><td>354.40 (-18.99%)</td><td>249.10 (+15.59%)</td><td>101.36 <b>(-20.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.30 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>525.10 (n/a)</td><td>396.10 (n/a)</td><td>437.50 (n/a)</td><td>215.50 (n/a)</td><td>126.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.54 (+15.83%)</td><td>0.41 (+6.02%)</td><td>0.45 (+6.88%)</td><td>0.26 (-6.61%)</td><td>0.13 <b>(+45.10%)</b></td><td>511.30 (+7.10%)</td><td>348.98 (-1.52%)</td><td>292.80 (-6.42%)</td><td>243.00 (-13.65%)</td><td>120.92 <b>(+36.48%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.47 (n/a)</td><td>0.39 (n/a)</td><td>0.42 (n/a)</td><td>0.27 (n/a)</td><td>0.09 (n/a)</td><td>477.40 (n/a)</td><td>354.36 (n/a)</td><td>312.90 (n/a)</td><td>281.40 (n/a)</td><td>88.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.44 (-3.31%)</td><td>0.34 (+7.72%)</td><td>0.31 (+19.91%)</td><td>0.23 (+4.85%)</td><td>0.09 (-14.01%)</td><td>569.00 (-4.63%)</td><td>406.64 (-9.41%)</td><td>422.50 (-16.60%)</td><td>295.50 (+3.43%)</td><td>112.84 (-17.49%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.46 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>596.60 (n/a)</td><td>448.86 (n/a)</td><td>506.60 (n/a)</td><td>285.70 (n/a)</td><td>136.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.56 <b>(+118.65%)</b></td><td>0.41 <b>(+93.01%)</b></td><td>0.47 <b>(+118.40%)</b></td><td>0.21 <b>(+60.45%)</b></td><td>0.15 <b>(+205.25%)</b></td><td>614.10 <b>(-37.68%)</b></td><td>363.26 <b>(-44.12%)</b></td><td>276.60 <b>(-54.21%)</b></td><td>234.70 <b>(-54.28%)</b></td><td>159.55 (-16.73%)</td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>985.40 (n/a)</td><td>650.12 (n/a)</td><td>604.10 (n/a)</td><td>513.30 (n/a)</td><td>191.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.37 (-17.09%)</td><td>0.27 (-11.22%)</td><td>0.25 <b>(-26.39%)</b></td><td>0.20 <b>(+189.58%)</b></td><td>0.07 <b>(-53.11%)</b></td><td>646.10 <b>(-65.47%)</b></td><td>506.90 <b>(-25.38%)</b></td><td>524.90 <b>(+35.84%)</b></td><td>350.80 <b>(+20.59%)</b></td><td>130.20 <b>(-80.70%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.45 (n/a)</td><td>0.31 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>1871.10 (n/a)</td><td>679.34 (n/a)</td><td>386.40 (n/a)</td><td>290.90 (n/a)</td><td>674.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.42 <b>(-22.72%)</b></td><td>0.31 (-14.68%)</td><td>0.28 <b>(-28.58%)</b></td><td>0.27 <b>(+285.64%)</b></td><td>0.06 <b>(-68.50%)</b></td><td>493.20 <b>(-74.07%)</b></td><td>438.48 <b>(-32.05%)</b></td><td>465.90 <b>(+40.04%)</b></td><td>313.00 <b>(+29.45%)</b></td><td>71.63 <b>(-89.92%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.54 (n/a)</td><td>0.36 (n/a)</td><td>0.39 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td><td>1902.10 (n/a)</td><td>645.34 (n/a)</td><td>332.70 (n/a)</td><td>241.80 (n/a)</td><td>710.66 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.54 (-13.61%)</td><td>0.37 (-2.01%)</td><td>0.30 (+4.69%)</td><td>0.25 (+11.13%)</td><td>0.12 <b>(-30.23%)</b></td><td>519.80 (-10.01%)</td><td>390.46 (-5.87%)</td><td>433.60 (-4.49%)</td><td>244.10 (+15.74%)</td><td>118.23 <b>(-30.38%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.62 (n/a)</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>577.60 (n/a)</td><td>414.82 (n/a)</td><td>454.00 (n/a)</td><td>210.90 (n/a)</td><td>169.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:48:32</td><td>0.06 <b>(+33.79%)</b></td><td>0.04 (+10.15%)</td><td>0.04 (+2.99%)</td><td>0.03 (-0.76%)</td><td>0.01 <b>(+103.34%)</b></td><td>624.90 (+0.77%)</td><td>469.40 (-5.39%)</td><td>458.50 (-2.90%)</td><td>297.00 <b>(-25.25%)</b></td><td>123.21 <b>(+48.56%)</b></td>
</tr>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:46:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>620.10 (n/a)</td><td>496.14 (n/a)</td><td>472.20 (n/a)</td><td>397.30 (n/a)</td><td>82.94 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:53:11</td><td>0.10 <b>(+53.54%)</b></td><td>0.06 <b>(+34.40%)</b></td><td>0.06 <b>(+46.03%)</b></td><td>0.03 (-6.25%)</td><td>0.03 <b>(+108.82%)</b></td><td>608.00 (+6.69%)</td><td>347.14 (-16.43%)</td><td>276.80 <b>(-31.50%)</b></td><td>171.70 <b>(-34.86%)</b></td><td>168.16 <b>(+52.39%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:55:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>569.90 (n/a)</td><td>415.38 (n/a)</td><td>404.10 (n/a)</td><td>263.60 (n/a)</td><td>110.35 (n/a)</td>
</tr>
</tbody>
</table>


</details>
