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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 <b>(+27.86%)</b></td><td>0.02 (+7.12%)</td><td>0.02 (+15.01%)</td><td>0.00 <b>(-74.11%)</b></td><td>0.01 <b>(+121.54%)</b></td><td>2076.90 <b>(+286.26%)</b></td><td>681.86 <b>(+64.72%)</b></td><td>407.20 (-13.05%)</td><td>229.30 <b>(-21.79%)</b></td><td>786.88 <b>(+611.14%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>537.70 (n/a)</td><td>413.96 (n/a)</td><td>468.30 (n/a)</td><td>293.20 (n/a)</td><td>110.65 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-2.40%)</td><td>0.02 (-7.80%)</td><td>0.01 <b>(-39.17%)</b></td><td>0.01 (-1.70%)</td><td>0.01 (-1.90%)</td><td>722.20 (+1.72%)</td><td>448.60 (+6.97%)</td><td>497.80 <b>(+64.40%)</b></td><td>249.40 (+2.47%)</td><td>193.79 (-5.38%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>710.00 (n/a)</td><td>419.38 (n/a)</td><td>302.80 (n/a)</td><td>243.40 (n/a)</td><td>204.82 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 <b>(+52.07%)</b></td><td>0.02 (+6.05%)</td><td>0.02 (-6.99%)</td><td>0.01 <b>(-27.56%)</b></td><td>0.01 <b>(+138.19%)</b></td><td>521.00 <b>(+38.01%)</b></td><td>298.54 (+8.87%)</td><td>290.90 (+7.50%)</td><td>133.40 <b>(-34.25%)</b></td><td>140.94 <b>(+109.83%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>377.50 (n/a)</td><td>274.22 (n/a)</td><td>270.60 (n/a)</td><td>202.90 (n/a)</td><td>67.17 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 <b>(+36.01%)</b></td><td>0.02 (+13.81%)</td><td>0.03 (+16.21%)</td><td>0.01 (-6.94%)</td><td>0.01 <b>(+65.10%)</b></td><td>533.70 (+7.45%)</td><td>349.84 (-3.38%)</td><td>245.70 (-13.94%)</td><td>195.10 <b>(-26.46%)</b></td><td>167.11 <b>(+40.44%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>496.70 (n/a)</td><td>362.08 (n/a)</td><td>285.50 (n/a)</td><td>265.30 (n/a)</td><td>119.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (+12.96%)</td><td>0.02 (-3.17%)</td><td>0.02 (-17.35%)</td><td>0.01 <b>(-21.95%)</b></td><td>0.01 <b>(+52.06%)</b></td><td>734.40 <b>(+28.12%)</b></td><td>422.04 (+14.96%)</td><td>366.30 <b>(+20.97%)</b></td><td>228.80 (-11.49%)</td><td>210.87 <b>(+64.66%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>573.20 (n/a)</td><td>367.12 (n/a)</td><td>302.80 (n/a)</td><td>258.50 (n/a)</td><td>128.06 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 <b>(-20.40%)</b></td><td>0.01 (-13.69%)</td><td>0.01 (+4.02%)</td><td>0.01 <b>(-47.38%)</b></td><td>0.00 (-13.18%)</td><td>1036.40 <b>(+90.03%)</b></td><td>542.40 <b>(+24.02%)</b></td><td>481.50 (-3.87%)</td><td>313.90 <b>(+25.66%)</b></td><td>285.13 <b>(+116.72%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>545.40 (n/a)</td><td>437.36 (n/a)</td><td>500.90 (n/a)</td><td>249.80 (n/a)</td><td>131.57 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (-8.15%)</td><td>0.04 (+14.07%)</td><td>0.05 (+15.42%)</td><td>0.03 (+12.54%)</td><td>0.01 (-18.26%)</td><td>476.00 (-11.14%)</td><td>299.46 (-14.83%)</td><td>267.70 (-13.37%)</td><td>238.60 (+8.85%)</td><td>99.63 (-19.22%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.70 (n/a)</td><td>351.62 (n/a)</td><td>309.00 (n/a)</td><td>219.20 (n/a)</td><td>123.33 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 <b>(+35.63%)</b></td><td>0.04 (+9.17%)</td><td>0.04 (-1.53%)</td><td>0.02 (-19.38%)</td><td>0.02 <b>(+72.27%)</b></td><td>566.70 <b>(+24.03%)</b></td><td>354.02 (+1.04%)</td><td>347.80 (+1.55%)</td><td>173.10 <b>(-26.28%)</b></td><td>154.78 <b>(+50.38%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>456.90 (n/a)</td><td>350.38 (n/a)</td><td>342.50 (n/a)</td><td>234.80 (n/a)</td><td>102.93 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (-17.75%)</td><td>0.03 <b>(-25.22%)</b></td><td>0.03 (-3.31%)</td><td>0.01 <b>(-75.45%)</b></td><td>0.01 (+18.77%)</td><td>1933.50 <b>(+307.31%)</b></td><td>700.50 <b>(+95.65%)</b></td><td>391.50 (+3.43%)</td><td>283.20 <b>(+21.55%)</b></td><td>695.77 <b>(+556.39%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>474.70 (n/a)</td><td>358.04 (n/a)</td><td>378.50 (n/a)</td><td>233.00 (n/a)</td><td>106.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (-8.75%)</td><td>0.03 (-13.83%)</td><td>0.03 (+0.64%)</td><td>0.02 (-17.69%)</td><td>0.01 (-17.80%)</td><td>553.30 <b>(+21.47%)</b></td><td>425.30 (+14.51%)</td><td>442.70 (-0.63%)</td><td>260.80 (+9.58%)</td><td>112.78 (+3.39%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>455.50 (n/a)</td><td>371.40 (n/a)</td><td>445.50 (n/a)</td><td>238.00 (n/a)</td><td>109.08 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (-7.26%)</td><td>0.03 (+5.58%)</td><td>0.03 (+18.20%)</td><td>0.02 (+0.61%)</td><td>0.01 <b>(-22.83%)</b></td><td>570.70 (-0.61%)</td><td>419.60 (-6.94%)</td><td>405.00 (-15.41%)</td><td>318.10 (+7.83%)</td><td>93.65 (-13.43%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>574.20 (n/a)</td><td>450.90 (n/a)</td><td>478.80 (n/a)</td><td>295.00 (n/a)</td><td>108.17 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 <b>(-42.58%)</b></td><td>0.02 <b>(-43.21%)</b></td><td>0.02 <b>(-37.07%)</b></td><td>0.01 <b>(-71.78%)</b></td><td>0.02 (-17.26%)</td><td>1982.60 <b>(+254.35%)</b></td><td>906.80 <b>(+152.89%)</b></td><td>569.10 <b>(+58.92%)</b></td><td>307.40 <b>(+74.16%)</b></td><td>730.79 <b>(+404.97%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>559.50 (n/a)</td><td>358.58 (n/a)</td><td>358.10 (n/a)</td><td>176.50 (n/a)</td><td>144.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.12 <b>(+26.91%)</b></td><td>0.08 <b>(+28.32%)</b></td><td>0.08 <b>(+53.88%)</b></td><td>0.06 (+19.99%)</td><td>0.03 <b>(+30.56%)</b></td><td>408.20 (-16.66%)</td><td>317.02 <b>(-21.35%)</b></td><td>300.40 <b>(-35.02%)</b></td><td>196.70 <b>(-21.19%)</b></td><td>91.21 (-11.01%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>489.80 (n/a)</td><td>403.06 (n/a)</td><td>462.30 (n/a)</td><td>249.60 (n/a)</td><td>102.50 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (-4.28%)</td><td>0.07 (+8.68%)</td><td>0.08 <b>(+42.78%)</b></td><td>0.04 (+9.18%)</td><td>0.02 (-17.62%)</td><td>564.60 (-8.40%)</td><td>379.40 (-11.71%)</td><td>311.50 <b>(-29.95%)</b></td><td>253.60 (+4.49%)</td><td>131.37 (-19.28%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>616.40 (n/a)</td><td>429.72 (n/a)</td><td>444.70 (n/a)</td><td>242.70 (n/a)</td><td>162.76 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 <b>(+37.10%)</b></td><td>0.09 <b>(+27.57%)</b></td><td>0.09 <b>(+75.42%)</b></td><td>0.05 (+4.45%)</td><td>0.03 <b>(+33.40%)</b></td><td>520.00 (-4.25%)</td><td>324.10 (-19.42%)</td><td>266.80 <b>(-43.00%)</b></td><td>182.90 <b>(-27.07%)</b></td><td>135.04 (-0.31%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>543.10 (n/a)</td><td>402.22 (n/a)</td><td>468.10 (n/a)</td><td>250.80 (n/a)</td><td>135.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 <b>(-30.33%)</b></td><td>0.06 (-8.48%)</td><td>0.05 (+1.18%)</td><td>0.05 (-3.95%)</td><td>0.01 <b>(-57.94%)</b></td><td>501.50 (+4.13%)</td><td>430.14 (+4.52%)</td><td>447.40 (-1.17%)</td><td>355.90 <b>(+43.57%)</b></td><td>61.33 <b>(-36.42%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>481.60 (n/a)</td><td>411.54 (n/a)</td><td>452.70 (n/a)</td><td>247.90 (n/a)</td><td>96.47 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 <b>(-30.64%)</b></td><td>0.06 (-11.35%)</td><td>0.05 <b>(-24.34%)</b></td><td>0.04 <b>(+346.26%)</b></td><td>0.01 <b>(-71.87%)</b></td><td>550.20 <b>(-77.59%)</b></td><td>443.46 <b>(-43.35%)</b></td><td>467.20 <b>(+32.16%)</b></td><td>346.90 <b>(+44.12%)</b></td><td>85.09 <b>(-91.02%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2455.20 (n/a)</td><td>782.84 (n/a)</td><td>353.50 (n/a)</td><td>240.70 (n/a)</td><td>947.66 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 <b>(+23.59%)</b></td><td>0.08 <b>(+32.57%)</b></td><td>0.09 <b>(+77.88%)</b></td><td>0.05 (+14.51%)</td><td>0.02 <b>(+29.13%)</b></td><td>480.30 (-12.67%)</td><td>330.10 <b>(-23.68%)</b></td><td>280.00 <b>(-43.78%)</b></td><td>234.70 (-19.10%)</td><td>109.82 (-8.51%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>550.00 (n/a)</td><td>432.50 (n/a)</td><td>498.00 (n/a)</td><td>290.10 (n/a)</td><td>120.03 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.19 <b>(+26.04%)</b></td><td>0.10 (-9.41%)</td><td>0.10 (-10.11%)</td><td>0.02 <b>(-70.11%)</b></td><td>0.06 <b>(+137.09%)</b></td><td>2090.60 <b>(+234.50%)</b></td><td>770.02 <b>(+68.02%)</b></td><td>493.10 (+11.26%)</td><td>265.40 <b>(-20.63%)</b></td><td>745.23 <b>(+612.49%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>625.00 (n/a)</td><td>458.28 (n/a)</td><td>443.20 (n/a)</td><td>334.40 (n/a)</td><td>104.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.19 (-5.37%)</td><td>0.14 (-2.02%)</td><td>0.18 <b>(+32.29%)</b></td><td>0.07 <b>(-29.56%)</b></td><td>0.06 <b>(+20.01%)</b></td><td>733.50 <b>(+41.96%)</b></td><td>425.94 (+11.64%)</td><td>276.30 <b>(-24.40%)</b></td><td>265.50 (+5.69%)</td><td>218.04 <b>(+68.47%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>516.70 (n/a)</td><td>381.54 (n/a)</td><td>365.50 (n/a)</td><td>251.20 (n/a)</td><td>129.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 (-10.86%)</td><td>0.14 (-1.24%)</td><td>0.15 <b>(+38.60%)</b></td><td>0.09 (+1.95%)</td><td>0.05 (-19.42%)</td><td>556.50 (-1.90%)</td><td>395.84 (-1.84%)</td><td>337.00 <b>(-27.85%)</b></td><td>234.00 (+12.18%)</td><td>147.32 (-3.73%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>567.30 (n/a)</td><td>403.24 (n/a)</td><td>467.10 (n/a)</td><td>208.60 (n/a)</td><td>153.03 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 <b>(+27.77%)</b></td><td>0.15 <b>(+35.37%)</b></td><td>0.16 <b>(+57.83%)</b></td><td>0.08 (-2.34%)</td><td>0.06 <b>(+93.49%)</b></td><td>595.20 (+2.39%)</td><td>382.80 (-17.54%)</td><td>303.80 <b>(-36.63%)</b></td><td>228.80 <b>(-21.75%)</b></td><td>176.08 <b>(+66.30%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>581.30 (n/a)</td><td>464.22 (n/a)</td><td>479.40 (n/a)</td><td>292.40 (n/a)</td><td>105.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.18 (-2.82%)</td><td>0.13 (+6.06%)</td><td>0.13 <b>(+21.56%)</b></td><td>0.10 (-1.43%)</td><td>0.04 (+5.84%)</td><td>513.80 (+1.46%)</td><td>397.80 (-4.82%)</td><td>391.70 (-17.74%)</td><td>279.00 (+2.91%)</td><td>114.36 (+9.90%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>506.40 (n/a)</td><td>417.96 (n/a)</td><td>476.20 (n/a)</td><td>271.10 (n/a)</td><td>104.05 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.20 (-5.65%)</td><td>0.13 (-7.48%)</td><td>0.09 (-19.89%)</td><td>0.07 <b>(-32.15%)</b></td><td>0.07 <b>(+32.75%)</b></td><td>731.20 <b>(+47.39%)</b></td><td>481.20 <b>(+22.07%)</b></td><td>562.50 <b>(+24.83%)</b></td><td>240.20 (+6.00%)</td><td>218.85 <b>(+96.39%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>496.10 (n/a)</td><td>394.20 (n/a)</td><td>450.60 (n/a)</td><td>226.60 (n/a)</td><td>111.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (-8.91%)</td><td>0.01 (-7.49%)</td><td>0.01 (-5.86%)</td><td>0.01 (-11.50%)</td><td>0.00 (-1.41%)</td><td>438.70 (+13.01%)</td><td>315.88 (+8.68%)</td><td>290.30 (+6.22%)</td><td>269.00 (+9.80%)</td><td>69.43 <b>(+22.81%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>388.20 (n/a)</td><td>290.64 (n/a)</td><td>273.30 (n/a)</td><td>245.00 (n/a)</td><td>56.54 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (+4.80%)</td><td>0.01 (-17.61%)</td><td>0.01 (-16.96%)</td><td>0.00 (-0.59%)</td><td>0.00 (-6.81%)</td><td>597.50 (+0.59%)</td><td>464.14 (+18.78%)</td><td>480.90 <b>(+20.41%)</b></td><td>213.90 (-4.59%)</td><td>153.70 (-7.50%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>594.00 (n/a)</td><td>390.76 (n/a)</td><td>399.40 (n/a)</td><td>224.20 (n/a)</td><td>166.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 <b>(-55.48%)</b></td><td>0.00 <b>(-54.69%)</b></td><td>0.00 <b>(-44.91%)</b></td><td>0.00 <b>(-77.21%)</b></td><td>0.00 <b>(-32.45%)</b></td><td>2397.50 <b>(+338.86%)</b></td><td>924.58 <b>(+186.19%)</b></td><td>529.00 <b>(+81.54%)</b></td><td>512.90 <b>(+124.66%)</b></td><td>825.73 <b>(+545.69%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>546.30 (n/a)</td><td>323.06 (n/a)</td><td>291.40 (n/a)</td><td>228.30 (n/a)</td><td>127.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 <b>(+37.79%)</b></td><td>0.01 (-7.80%)</td><td>0.00 <b>(-31.32%)</b></td><td>0.00 (+0.73%)</td><td>0.00 <b>(+100.36%)</b></td><td>633.50 (-0.72%)</td><td>496.82 (+19.33%)</td><td>550.40 <b>(+45.61%)</b></td><td>217.30 <b>(-27.45%)</b></td><td>171.90 <b>(+32.81%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>638.10 (n/a)</td><td>416.34 (n/a)</td><td>378.00 (n/a)</td><td>299.50 (n/a)</td><td>129.43 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 <b>(+23.39%)</b></td><td>0.01 <b>(+24.91%)</b></td><td>0.01 <b>(+20.62%)</b></td><td>0.01 <b>(+31.41%)</b></td><td>0.00 <b>(+21.01%)</b></td><td>474.00 <b>(-23.90%)</b></td><td>389.38 <b>(-20.28%)</b></td><td>430.40 (-17.10%)</td><td>236.60 (-18.97%)</td><td>93.14 <b>(-23.39%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>622.90 (n/a)</td><td>488.46 (n/a)</td><td>519.20 (n/a)</td><td>292.00 (n/a)</td><td>121.57 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 <b>(+51.79%)</b></td><td>0.01 (+13.69%)</td><td>0.01 (-0.10%)</td><td>0.00 (+11.15%)</td><td>0.00 <b>(+134.04%)</b></td><td>547.00 (-10.02%)</td><td>447.82 (-8.77%)</td><td>466.80 (+0.11%)</td><td>282.10 <b>(-34.12%)</b></td><td>102.30 <b>(+35.10%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>607.90 (n/a)</td><td>490.88 (n/a)</td><td>466.30 (n/a)</td><td>428.20 (n/a)</td><td>75.73 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 <b>(+26.52%)</b></td><td>0.02 <b>(+25.79%)</b></td><td>0.01 (+19.25%)</td><td>0.01 <b>(+21.02%)</b></td><td>0.01 <b>(+36.43%)</b></td><td>434.90 (-17.35%)</td><td>337.56 (-19.27%)</td><td>355.70 (-16.15%)</td><td>204.10 <b>(-20.95%)</b></td><td>95.08 (-7.63%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>526.20 (n/a)</td><td>418.14 (n/a)</td><td>424.20 (n/a)</td><td>258.20 (n/a)</td><td>102.94 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (+6.23%)</td><td>0.01 (+2.03%)</td><td>0.01 (+3.31%)</td><td>0.01 (+9.99%)</td><td>0.00 (-7.89%)</td><td>469.30 (-9.09%)</td><td>384.00 (-4.06%)</td><td>456.30 (-3.20%)</td><td>242.50 (-5.86%)</td><td>107.99 (-15.95%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>516.20 (n/a)</td><td>400.26 (n/a)</td><td>471.40 (n/a)</td><td>257.60 (n/a)</td><td>128.49 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-2.57%)</td><td>0.01 <b>(-29.60%)</b></td><td>0.01 <b>(-42.75%)</b></td><td>0.01 (-13.88%)</td><td>0.01 (+12.60%)</td><td>530.70 (+16.13%)</td><td>430.40 <b>(+46.24%)</b></td><td>476.80 <b>(+74.65%)</b></td><td>230.50 (+2.63%)</td><td>123.50 <b>(+29.96%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>457.00 (n/a)</td><td>294.32 (n/a)</td><td>273.00 (n/a)</td><td>224.60 (n/a)</td><td>95.03 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (+10.21%)</td><td>0.02 (-2.42%)</td><td>0.02 (+0.04%)</td><td>0.01 <b>(-31.92%)</b></td><td>0.01 <b>(+51.23%)</b></td><td>714.00 <b>(+46.88%)</b></td><td>414.10 (+16.25%)</td><td>282.10 (-0.04%)</td><td>245.60 (-9.24%)</td><td>217.31 <b>(+95.42%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>486.10 (n/a)</td><td>356.20 (n/a)</td><td>282.20 (n/a)</td><td>270.60 (n/a)</td><td>111.20 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-2.75%)</td><td>0.01 (-16.26%)</td><td>0.01 <b>(-47.20%)</b></td><td>0.01 (+9.87%)</td><td>0.00 (-14.46%)</td><td>527.20 (-8.99%)</td><td>430.14 (+16.03%)</td><td>513.20 <b>(+89.37%)</b></td><td>263.40 (+2.81%)</td><td>127.67 (-13.81%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.30 (n/a)</td><td>370.72 (n/a)</td><td>271.00 (n/a)</td><td>256.20 (n/a)</td><td>148.14 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 <b>(-40.72%)</b></td><td>0.01 <b>(-27.08%)</b></td><td>0.01 (-9.20%)</td><td>0.01 <b>(-23.64%)</b></td><td>0.00 <b>(-68.74%)</b></td><td>693.60 <b>(+30.97%)</b></td><td>558.44 <b>(+31.15%)</b></td><td>535.90 (+10.13%)</td><td>501.20 <b>(+68.70%)</b></td><td>77.21 <b>(-28.40%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>529.60 (n/a)</td><td>425.80 (n/a)</td><td>486.60 (n/a)</td><td>297.10 (n/a)</td><td>107.85 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (-6.19%)</td><td>0.03 (-1.21%)</td><td>0.04 (+13.47%)</td><td>0.02 (+3.72%)</td><td>0.01 (-12.44%)</td><td>536.40 (-3.59%)</td><td>356.74 (-0.52%)</td><td>294.00 (-11.87%)</td><td>246.60 (+6.61%)</td><td>120.90 (-7.95%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>556.40 (n/a)</td><td>358.62 (n/a)</td><td>333.60 (n/a)</td><td>231.30 (n/a)</td><td>131.34 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (-10.18%)</td><td>0.03 <b>(-22.95%)</b></td><td>0.03 <b>(-33.68%)</b></td><td>0.02 (+16.14%)</td><td>0.01 <b>(-32.87%)</b></td><td>462.00 (-13.89%)</td><td>396.70 <b>(+23.59%)</b></td><td>414.20 <b>(+50.78%)</b></td><td>272.80 (+11.35%)</td><td>72.52 <b>(-40.67%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.50 (n/a)</td><td>320.98 (n/a)</td><td>274.70 (n/a)</td><td>245.00 (n/a)</td><td>122.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (+19.38%)</td><td>0.03 (+11.50%)</td><td>0.02 <b>(+24.90%)</b></td><td>0.02 (+5.85%)</td><td>0.01 (+6.77%)</td><td>552.60 (-5.52%)</td><td>384.94 (-12.21%)</td><td>450.50 (-19.93%)</td><td>194.90 (-16.21%)</td><td>151.79 (-16.66%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>584.90 (n/a)</td><td>438.48 (n/a)</td><td>562.60 (n/a)</td><td>232.60 (n/a)</td><td>182.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 <b>(+20.84%)</b></td><td>0.04 (-0.93%)</td><td>0.03 (-3.98%)</td><td>0.02 (-7.96%)</td><td>0.01 <b>(+56.64%)</b></td><td>524.60 (+8.66%)</td><td>346.44 (+9.27%)</td><td>301.80 (+4.14%)</td><td>194.00 (-17.27%)</td><td>146.59 <b>(+45.75%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>482.80 (n/a)</td><td>317.04 (n/a)</td><td>289.80 (n/a)</td><td>234.50 (n/a)</td><td>100.58 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (+10.19%)</td><td>0.03 (+5.00%)</td><td>0.02 (-11.60%)</td><td>0.02 (-19.90%)</td><td>0.02 <b>(+60.60%)</b></td><td>621.70 <b>(+24.84%)</b></td><td>417.32 (+8.23%)</td><td>451.40 (+13.10%)</td><td>208.20 (-9.24%)</td><td>187.96 <b>(+88.45%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.00 (n/a)</td><td>385.60 (n/a)</td><td>399.10 (n/a)</td><td>229.40 (n/a)</td><td>99.74 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (+2.56%)</td><td>0.02 (-1.73%)</td><td>0.02 (+0.65%)</td><td>0.01 (-9.90%)</td><td>0.01 <b>(+30.58%)</b></td><td>744.80 (+10.98%)</td><td>509.44 (+5.38%)</td><td>479.30 (-0.64%)</td><td>345.60 (-2.48%)</td><td>164.52 <b>(+37.76%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>671.10 (n/a)</td><td>483.44 (n/a)</td><td>482.40 (n/a)</td><td>354.40 (n/a)</td><td>119.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (-7.22%)</td><td>0.06 (+2.65%)</td><td>0.06 (+15.92%)</td><td>0.04 <b>(+20.63%)</b></td><td>0.01 <b>(-31.15%)</b></td><td>523.50 (-17.10%)</td><td>395.28 (-7.15%)</td><td>352.30 (-13.74%)</td><td>304.00 (+7.76%)</td><td>91.49 <b>(-36.29%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>631.50 (n/a)</td><td>425.74 (n/a)</td><td>408.40 (n/a)</td><td>282.10 (n/a)</td><td>143.61 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 <b>(-23.21%)</b></td><td>0.05 <b>(-28.68%)</b></td><td>0.05 <b>(-28.10%)</b></td><td>0.01 <b>(-75.91%)</b></td><td>0.02 <b>(+33.56%)</b></td><td>1896.80 <b>(+315.05%)</b></td><td>667.50 <b>(+108.72%)</b></td><td>390.90 <b>(+39.11%)</b></td><td>304.40 <b>(+30.25%)</b></td><td>688.18 <b>(+689.92%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>457.00 (n/a)</td><td>319.80 (n/a)</td><td>281.00 (n/a)</td><td>233.70 (n/a)</td><td>87.12 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (+0.31%)</td><td>0.06 (+13.70%)</td><td>0.06 <b>(+50.55%)</b></td><td>0.04 <b>(+33.59%)</b></td><td>0.02 <b>(-20.53%)</b></td><td>484.60 <b>(-25.15%)</b></td><td>370.78 (-16.49%)</td><td>326.00 <b>(-33.58%)</b></td><td>274.80 (-0.33%)</td><td>104.79 <b>(-34.27%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>647.40 (n/a)</td><td>443.98 (n/a)</td><td>490.80 (n/a)</td><td>275.70 (n/a)</td><td>159.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (+1.69%)</td><td>0.06 (-15.85%)</td><td>0.05 <b>(-28.24%)</b></td><td>0.03 (-11.86%)</td><td>0.02 (+11.40%)</td><td>644.10 (+13.46%)</td><td>410.30 <b>(+21.86%)</b></td><td>405.90 <b>(+39.34%)</b></td><td>225.20 (-1.66%)</td><td>158.33 (+17.23%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>567.70 (n/a)</td><td>336.70 (n/a)</td><td>291.30 (n/a)</td><td>229.00 (n/a)</td><td>135.06 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.11 (+18.92%)</td><td>0.06 (-5.46%)</td><td>0.04 <b>(-27.63%)</b></td><td>0.01 <b>(-67.20%)</b></td><td>0.04 <b>(+72.60%)</b></td><td>1863.80 <b>(+204.94%)</b></td><td>685.94 <b>(+71.49%)</b></td><td>503.90 <b>(+38.17%)</b></td><td>193.60 (-15.90%)</td><td>682.34 <b>(+335.48%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.20 (n/a)</td><td>399.98 (n/a)</td><td>364.70 (n/a)</td><td>230.20 (n/a)</td><td>156.69 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 <b>(-34.33%)</b></td><td>0.04 <b>(-21.34%)</b></td><td>0.04 (+0.05%)</td><td>0.02 <b>(-30.01%)</b></td><td>0.01 <b>(-50.30%)</b></td><td>916.30 <b>(+42.88%)</b></td><td>575.48 <b>(+20.96%)</b></td><td>503.40 (-0.04%)</td><td>427.90 <b>(+52.28%)</b></td><td>194.22 (+13.75%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>641.30 (n/a)</td><td>475.78 (n/a)</td><td>503.60 (n/a)</td><td>281.00 (n/a)</td><td>170.74 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>542.40 (n/a)</td><td>366.50 (n/a)</td><td>316.90 (n/a)</td><td>263.30 (n/a)</td><td>119.45 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>464.40 (n/a)</td><td>361.48 (n/a)</td><td>452.70 (n/a)</td><td>152.00 (n/a)</td><td>141.40 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.70 (n/a)</td><td>429.34 (n/a)</td><td>450.60 (n/a)</td><td>302.50 (n/a)</td><td>87.66 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>597.30 (n/a)</td><td>452.00 (n/a)</td><td>512.10 (n/a)</td><td>268.20 (n/a)</td><td>161.74 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>602.90 (n/a)</td><td>450.64 (n/a)</td><td>509.40 (n/a)</td><td>278.80 (n/a)</td><td>154.87 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>592.90 (n/a)</td><td>456.64 (n/a)</td><td>478.90 (n/a)</td><td>268.10 (n/a)</td><td>139.20 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>655.60 (n/a)</td><td>411.34 (n/a)</td><td>340.20 (n/a)</td><td>278.90 (n/a)</td><td>156.99 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>598.10 (n/a)</td><td>419.56 (n/a)</td><td>423.80 (n/a)</td><td>248.60 (n/a)</td><td>166.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>601.10 (n/a)</td><td>463.88 (n/a)</td><td>506.70 (n/a)</td><td>249.80 (n/a)</td><td>146.37 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 (+4.43%)</td><td>0.12 <b>(-28.57%)</b></td><td>0.10 <b>(-42.73%)</b></td><td>0.07 <b>(-28.78%)</b></td><td>0.06 <b>(+38.55%)</b></td><td>658.90 <b>(+40.43%)</b></td><td>471.52 <b>(+50.16%)</b></td><td>483.40 <b>(+74.58%)</b></td><td>230.10 (-4.24%)</td><td>158.86 <b>(+71.08%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>469.20 (n/a)</td><td>314.02 (n/a)</td><td>276.90 (n/a)</td><td>240.30 (n/a)</td><td>92.86 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1889.70 (n/a)</td><td>716.94 (n/a)</td><td>459.50 (n/a)</td><td>323.70 (n/a)</td><td>660.96 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>610.10 (n/a)</td><td>469.62 (n/a)</td><td>476.30 (n/a)</td><td>261.70 (n/a)</td><td>131.18 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>594.10 (n/a)</td><td>390.20 (n/a)</td><td>330.40 (n/a)</td><td>303.70 (n/a)</td><td>122.78 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.80 (n/a)</td><td>401.50 (n/a)</td><td>414.10 (n/a)</td><td>232.10 (n/a)</td><td>132.52 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>697.10 (n/a)</td><td>451.26 (n/a)</td><td>391.00 (n/a)</td><td>283.40 (n/a)</td><td>158.70 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.90 (n/a)</td><td>393.82 (n/a)</td><td>450.70 (n/a)</td><td>255.30 (n/a)</td><td>111.78 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>620.60 (n/a)</td><td>363.56 (n/a)</td><td>272.90 (n/a)</td><td>237.70 (n/a)</td><td>162.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>455.80 (n/a)</td><td>320.04 (n/a)</td><td>295.30 (n/a)</td><td>253.50 (n/a)</td><td>78.28 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>574.80 (n/a)</td><td>367.62 (n/a)</td><td>307.00 (n/a)</td><td>210.00 (n/a)</td><td>157.32 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>627.90 (n/a)</td><td>453.48 (n/a)</td><td>461.50 (n/a)</td><td>239.40 (n/a)</td><td>169.73 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1077.10 (n/a)</td><td>589.20 (n/a)</td><td>570.00 (n/a)</td><td>273.50 (n/a)</td><td>299.97 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>608.00 (n/a)</td><td>462.78 (n/a)</td><td>483.50 (n/a)</td><td>264.10 (n/a)</td><td>124.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>675.20 (n/a)</td><td>574.46 (n/a)</td><td>595.20 (n/a)</td><td>438.70 (n/a)</td><td>89.19 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.99 (+0.34%)</td><td>2.46 (-12.25%)</td><td>2.26 (-12.57%)</td><td>1.57 (-9.70%)</td><td>0.95 (-15.00%)</td><td>6696.70 (+10.74%)</td><td>4738.96 (+10.69%)</td><td>4634.80 (+14.37%)</td><td>2627.60 (-0.34%)</td><td>1582.83 (-6.98%)</td><td>1634.57 (+0.34%)</td><td>1006.47 (-12.25%)</td><td>926.68 (-12.57%)</td><td>641.36 (-9.70%)</td><td>390.69 (-15.00%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.98 (n/a)</td><td>2.80 (n/a)</td><td>2.59 (n/a)</td><td>1.73 (n/a)</td><td>1.12 (n/a)</td><td>6047.30 (n/a)</td><td>4281.42 (n/a)</td><td>4052.40 (n/a)</td><td>2636.60 (n/a)</td><td>1701.67 (n/a)</td><td>1628.99 (n/a)</td><td>1146.92 (n/a)</td><td>1059.86 (n/a)</td><td>710.23 (n/a)</td><td>459.65 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.68 (-1.16%)</td><td>2.95 (-10.93%)</td><td>2.86 <b>(-21.37%)</b></td><td>2.27 (-15.46%)</td><td>0.51 (-1.70%)</td><td>10397.70 (+18.29%)</td><td>8191.72 (+12.64%)</td><td>8247.30 <b>(+27.18%)</b></td><td>6407.70 (+1.17%)</td><td>1446.32 (+19.56%)</td><td>2094.62 (-1.16%)</td><td>1678.71 (-10.93%)</td><td>1627.42 <b>(-21.37%)</b></td><td>1290.84 (-15.46%)</td><td>289.58 (-1.70%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.73 (n/a)</td><td>3.31 (n/a)</td><td>3.64 (n/a)</td><td>2.68 (n/a)</td><td>0.52 (n/a)</td><td>8789.80 (n/a)</td><td>7272.46 (n/a)</td><td>6484.90 (n/a)</td><td>6333.50 (n/a)</td><td>1209.67 (n/a)</td><td>2119.17 (n/a)</td><td>1884.74 (n/a)</td><td>2069.69 (n/a)</td><td>1526.98 (n/a)</td><td>294.57 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.54 (-12.35%)</td><td>3.07 (-5.11%)</td><td>3.03 (-1.95%)</td><td>2.81 (+19.77%)</td><td>0.29 <b>(-56.25%)</b></td><td>5976.20 (-16.51%)</td><td>5507.56 (+2.36%)</td><td>5536.40 (+1.99%)</td><td>4740.90 (+14.09%)</td><td>488.10 <b>(-58.32%)</b></td><td>1811.86 (-12.35%)</td><td>1570.18 (-5.11%)</td><td>1551.55 (-1.95%)</td><td>1437.36 (+19.77%)</td><td>148.66 <b>(-56.25%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.04 (n/a)</td><td>3.23 (n/a)</td><td>3.09 (n/a)</td><td>2.34 (n/a)</td><td>0.66 (n/a)</td><td>7158.00 (n/a)</td><td>5380.72 (n/a)</td><td>5428.20 (n/a)</td><td>4155.40 (n/a)</td><td>1171.18 (n/a)</td><td>2067.17 (n/a)</td><td>1654.72 (n/a)</td><td>1582.47 (n/a)</td><td>1200.05 (n/a)</td><td>339.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.83 (-4.66%)</td><td>0.60 (-19.57%)</td><td>0.65 (-10.83%)</td><td>0.13 <b>(-79.33%)</b></td><td>0.28 <b>(+177.74%)</b></td><td>3469.50 <b>(+383.89%)</b></td><td>1214.16 <b>(+94.58%)</b></td><td>700.70 (+12.15%)</td><td>549.90 (+4.88%)</td><td>1263.36 <b>(+1443.10%)</b></td><td>61.02 (-4.66%)</td><td>43.86 (-19.57%)</td><td>47.88 (-10.83%)</td><td>9.67 <b>(-79.33%)</b></td><td>20.20 <b>(+177.74%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.87 (n/a)</td><td>0.75 (n/a)</td><td>0.73 (n/a)</td><td>0.64 (n/a)</td><td>0.10 (n/a)</td><td>717.00 (n/a)</td><td>624.00 (n/a)</td><td>624.80 (n/a)</td><td>524.30 (n/a)</td><td>81.87 (n/a)</td><td>64.00 (n/a)</td><td>54.53 (n/a)</td><td>53.70 (n/a)</td><td>46.80 (n/a)</td><td>7.27 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.28 (-16.59%)</td><td>0.98 (-14.43%)</td><td>0.91 <b>(-20.79%)</b></td><td>0.65 (-8.27%)</td><td>0.25 (-19.57%)</td><td>1002.70 (+9.01%)</td><td>709.38 (+15.50%)</td><td>717.90 <b>(+26.26%)</b></td><td>513.10 (+19.88%)</td><td>193.78 (+1.51%)</td><td>130.78 (-16.59%)</td><td>100.09 (-14.43%)</td><td>93.48 <b>(-20.79%)</b></td><td>66.93 (-8.27%)</td><td>25.66 (-19.57%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.53 (n/a)</td><td>1.14 (n/a)</td><td>1.15 (n/a)</td><td>0.71 (n/a)</td><td>0.31 (n/a)</td><td>919.80 (n/a)</td><td>614.20 (n/a)</td><td>568.60 (n/a)</td><td>428.00 (n/a)</td><td>190.89 (n/a)</td><td>156.79 (n/a)</td><td>116.97 (n/a)</td><td>118.03 (n/a)</td><td>72.96 (n/a)</td><td>31.91 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.43 (-14.81%)</td><td>1.16 (-10.22%)</td><td>1.04 (-13.41%)</td><td>0.98 (-6.59%)</td><td>0.21 (-16.96%)</td><td>769.90 (+7.05%)</td><td>665.38 (+11.04%)</td><td>723.50 (+15.48%)</td><td>526.80 (+17.38%)</td><td>110.74 (+5.66%)</td><td>159.23 (-14.81%)</td><td>129.12 (-10.22%)</td><td>115.94 (-13.41%)</td><td>108.96 (-6.59%)</td><td>22.93 (-16.96%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.68 (n/a)</td><td>1.29 (n/a)</td><td>1.20 (n/a)</td><td>1.05 (n/a)</td><td>0.25 (n/a)</td><td>719.20 (n/a)</td><td>599.20 (n/a)</td><td>626.50 (n/a)</td><td>448.80 (n/a)</td><td>104.81 (n/a)</td><td>186.91 (n/a)</td><td>143.83 (n/a)</td><td>133.91 (n/a)</td><td>116.65 (n/a)</td><td>27.61 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.58 (-3.19%)</td><td>1.21 <b>(+37.30%)</b></td><td>1.47 <b>(+216.92%)</b></td><td>0.47 <b>(+58.93%)</b></td><td>0.46 <b>(-29.68%)</b></td><td>2218.10 <b>(-37.08%)</b></td><td>1061.14 <b>(-43.73%)</b></td><td>711.50 <b>(-68.45%)</b></td><td>663.70 (+3.30%)</td><td>661.45 <b>(-46.25%)</b></td><td>202.23 (-3.19%)</td><td>155.07 <b>(+37.30%)</b></td><td>188.65 <b>(+216.92%)</b></td><td>60.51 <b>(+58.93%)</b></td><td>59.34 <b>(-29.68%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.63 (n/a)</td><td>0.88 (n/a)</td><td>0.47 (n/a)</td><td>0.30 (n/a)</td><td>0.66 (n/a)</td><td>3525.30 (n/a)</td><td>1885.92 (n/a)</td><td>2254.80 (n/a)</td><td>642.50 (n/a)</td><td>1230.58 (n/a)</td><td>208.91 (n/a)</td><td>112.94 (n/a)</td><td>59.53 (n/a)</td><td>38.07 (n/a)</td><td>84.38 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>2.33 <b>(+66.89%)</b></td><td>1.54 <b>(+41.18%)</b></td><td>1.33 (+3.33%)</td><td>1.28 <b>(+103.91%)</b></td><td>0.45 <b>(+27.51%)</b></td><td>820.30 <b>(-50.96%)</b></td><td>716.68 <b>(-32.73%)</b></td><td>789.00 (-3.23%)</td><td>450.20 <b>(-40.09%)</b></td><td>153.03 <b>(-62.50%)</b></td><td>298.10 <b>(+66.89%)</b></td><td>196.99 <b>(+41.18%)</b></td><td>170.11 (+3.33%)</td><td>163.63 <b>(+103.91%)</b></td><td>57.09 <b>(+27.51%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.40 (n/a)</td><td>1.09 (n/a)</td><td>1.29 (n/a)</td><td>0.63 (n/a)</td><td>0.35 (n/a)</td><td>1672.70 (n/a)</td><td>1065.44 (n/a)</td><td>815.30 (n/a)</td><td>751.40 (n/a)</td><td>408.07 (n/a)</td><td>178.63 (n/a)</td><td>139.53 (n/a)</td><td>164.63 (n/a)</td><td>80.24 (n/a)</td><td>44.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.84 <b>(-20.98%)</b></td><td>1.18 <b>(-32.35%)</b></td><td>1.31 <b>(-27.85%)</b></td><td>0.41 <b>(-68.07%)</b></td><td>0.53 (+18.77%)</td><td>2533.20 <b>(+213.20%)</b></td><td>1148.02 <b>(+81.39%)</b></td><td>800.20 <b>(+38.61%)</b></td><td>569.00 <b>(+26.56%)</b></td><td>794.15 <b>(+389.81%)</b></td><td>235.89 <b>(-20.98%)</b></td><td>151.26 <b>(-32.35%)</b></td><td>167.72 <b>(-27.85%)</b></td><td>52.98 <b>(-68.07%)</b></td><td>67.51 (+18.77%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>2.33 (n/a)</td><td>1.75 (n/a)</td><td>1.82 (n/a)</td><td>1.30 (n/a)</td><td>0.44 (n/a)</td><td>808.80 (n/a)</td><td>632.90 (n/a)</td><td>577.30 (n/a)</td><td>449.60 (n/a)</td><td>162.14 (n/a)</td><td>298.50 (n/a)</td><td>223.58 (n/a)</td><td>232.48 (n/a)</td><td>165.95 (n/a)</td><td>56.84 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.65 (-10.10%)</td><td>1.48 (+9.16%)</td><td>1.53 <b>(+31.67%)</b></td><td>1.19 <b>(+22.81%)</b></td><td>0.17 <b>(-54.09%)</b></td><td>880.40 (-18.57%)</td><td>716.36 (-12.67%)</td><td>686.30 <b>(-24.05%)</b></td><td>636.20 (+11.24%)</td><td>95.60 <b>(-55.91%)</b></td><td>210.97 (-10.10%)</td><td>189.74 (+9.16%)</td><td>195.57 <b>(+31.67%)</b></td><td>152.45 <b>(+22.81%)</b></td><td>22.34 <b>(-54.09%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.83 (n/a)</td><td>1.36 (n/a)</td><td>1.16 (n/a)</td><td>0.97 (n/a)</td><td>0.38 (n/a)</td><td>1081.20 (n/a)</td><td>820.28 (n/a)</td><td>903.60 (n/a)</td><td>571.90 (n/a)</td><td>216.81 (n/a)</td><td>234.68 (n/a)</td><td>173.82 (n/a)</td><td>148.53 (n/a)</td><td>124.14 (n/a)</td><td>48.67 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.78 (-9.54%)</td><td>1.32 (+14.67%)</td><td>1.30 (+11.84%)</td><td>0.51 (+2.14%)</td><td>0.50 (-11.88%)</td><td>2071.20 (-2.10%)</td><td>978.78 (-14.53%)</td><td>804.50 (-10.58%)</td><td>589.30 (+10.54%)</td><td>619.17 (-1.72%)</td><td>227.77 (-9.54%)</td><td>168.40 (+14.67%)</td><td>166.84 (+11.84%)</td><td>64.80 (+2.14%)</td><td>64.46 (-11.88%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.97 (n/a)</td><td>1.15 (n/a)</td><td>1.17 (n/a)</td><td>0.50 (n/a)</td><td>0.57 (n/a)</td><td>2115.60 (n/a)</td><td>1145.20 (n/a)</td><td>899.70 (n/a)</td><td>533.10 (n/a)</td><td>630.03 (n/a)</td><td>251.79 (n/a)</td><td>146.85 (n/a)</td><td>149.18 (n/a)</td><td>63.44 (n/a)</td><td>73.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.28 <b>(-27.04%)</b></td><td>0.90 <b>(-37.39%)</b></td><td>0.94 <b>(-40.44%)</b></td><td>0.48 <b>(-54.08%)</b></td><td>0.34 (+7.19%)</td><td>2200.70 <b>(+117.76%)</b></td><td>1336.70 <b>(+75.48%)</b></td><td>1117.20 <b>(+67.90%)</b></td><td>816.70 <b>(+37.05%)</b></td><td>582.42 <b>(+215.94%)</b></td><td>164.34 <b>(-27.04%)</b></td><td>115.26 <b>(-37.39%)</b></td><td>120.14 <b>(-40.44%)</b></td><td>60.99 <b>(-54.08%)</b></td><td>43.90 (+7.19%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.76 (n/a)</td><td>1.44 (n/a)</td><td>1.58 (n/a)</td><td>1.04 (n/a)</td><td>0.32 (n/a)</td><td>1010.60 (n/a)</td><td>761.72 (n/a)</td><td>665.40 (n/a)</td><td>595.90 (n/a)</td><td>184.34 (n/a)</td><td>225.25 (n/a)</td><td>184.09 (n/a)</td><td>201.72 (n/a)</td><td>132.81 (n/a)</td><td>40.95 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.84 (-5.41%)</td><td>0.63 (+8.59%)</td><td>0.59 (+16.25%)</td><td>0.41 (-4.23%)</td><td>0.17 (-7.07%)</td><td>870.20 (+4.42%)</td><td>612.64 (-8.14%)</td><td>613.70 (-13.98%)</td><td>427.60 (+5.71%)</td><td>175.29 (+3.89%)</td><td>39.23 (-5.41%)</td><td>29.18 (+8.59%)</td><td>27.34 (+16.25%)</td><td>19.28 (-4.23%)</td><td>8.02 (-7.07%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.89 (n/a)</td><td>0.58 (n/a)</td><td>0.51 (n/a)</td><td>0.43 (n/a)</td><td>0.19 (n/a)</td><td>833.40 (n/a)</td><td>666.94 (n/a)</td><td>713.40 (n/a)</td><td>404.50 (n/a)</td><td>168.73 (n/a)</td><td>41.48 (n/a)</td><td>26.87 (n/a)</td><td>23.52 (n/a)</td><td>20.13 (n/a)</td><td>8.63 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.02 (-2.81%)</td><td>1.47 <b>(-31.42%)</b></td><td>1.11 <b>(-41.45%)</b></td><td>1.01 (+2.15%)</td><td>0.87 (-0.15%)</td><td>4150.70 (-2.11%)</td><td>3384.76 <b>(+46.41%)</b></td><td>3781.10 <b>(+70.80%)</b></td><td>1387.50 (+2.89%)</td><td>1128.20 (-3.04%)</td><td>773.89 (-2.81%)</td><td>376.31 <b>(-31.42%)</b></td><td>283.98 <b>(-41.45%)</b></td><td>258.69 (+2.15%)</td><td>222.54 (-0.15%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.11 (n/a)</td><td>2.14 (n/a)</td><td>1.89 (n/a)</td><td>0.99 (n/a)</td><td>0.87 (n/a)</td><td>4240.00 (n/a)</td><td>2311.88 (n/a)</td><td>2213.80 (n/a)</td><td>1348.50 (n/a)</td><td>1163.57 (n/a)</td><td>796.25 (n/a)</td><td>548.71 (n/a)</td><td>485.03 (n/a)</td><td>253.24 (n/a)</td><td>222.87 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.97 (+2.20%)</td><td>3.32 <b>(+22.77%)</b></td><td>3.53 (-1.22%)</td><td>2.12 <b>(+83.56%)</b></td><td>0.70 <b>(-49.51%)</b></td><td>1236.00 <b>(-45.52%)</b></td><td>827.62 <b>(-36.64%)</b></td><td>741.70 (+1.23%)</td><td>660.70 (-2.16%)</td><td>231.51 <b>(-71.89%)</b></td><td>812.54 (+2.20%)</td><td>680.60 <b>(+22.77%)</b></td><td>723.79 (-1.22%)</td><td>434.37 <b>(+83.56%)</b></td><td>143.76 <b>(-49.51%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.88 (n/a)</td><td>2.71 (n/a)</td><td>3.58 (n/a)</td><td>1.16 (n/a)</td><td>1.39 (n/a)</td><td>2268.70 (n/a)</td><td>1306.14 (n/a)</td><td>732.70 (n/a)</td><td>675.30 (n/a)</td><td>823.65 (n/a)</td><td>795.05 (n/a)</td><td>554.39 (n/a)</td><td>732.71 (n/a)</td><td>236.64 (n/a)</td><td>284.74 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.24 (+10.79%)</td><td>2.69 <b>(+23.21%)</b></td><td>2.90 <b>(+42.33%)</b></td><td>1.74 (+14.86%)</td><td>0.63 (-0.15%)</td><td>4525.00 (-12.94%)</td><td>3085.10 (-19.89%)</td><td>2711.40 <b>(-29.74%)</b></td><td>2428.60 (-9.74%)</td><td>872.28 (-19.94%)</td><td>994.78 (+10.79%)</td><td>825.96 <b>(+23.21%)</b></td><td>891.02 <b>(+42.33%)</b></td><td>533.91 (+14.86%)</td><td>192.05 (-0.15%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>2.92 (n/a)</td><td>2.18 (n/a)</td><td>2.04 (n/a)</td><td>1.51 (n/a)</td><td>0.63 (n/a)</td><td>5197.30 (n/a)</td><td>3851.12 (n/a)</td><td>3859.10 (n/a)</td><td>2690.60 (n/a)</td><td>1089.55 (n/a)</td><td>897.92 (n/a)</td><td>670.35 (n/a)</td><td>626.04 (n/a)</td><td>464.84 (n/a)</td><td>192.35 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.30 (n/a)</td><td>356.02 (n/a)</td><td>298.50 (n/a)</td><td>241.50 (n/a)</td><td>123.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>492.40 (n/a)</td><td>343.04 (n/a)</td><td>301.90 (n/a)</td><td>220.90 (n/a)</td><td>123.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>602.50 (n/a)</td><td>405.34 (n/a)</td><td>434.20 (n/a)</td><td>182.20 (n/a)</td><td>158.49 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>778.10 (n/a)</td><td>442.42 (n/a)</td><td>346.10 (n/a)</td><td>165.50 (n/a)</td><td>253.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>564.20 (n/a)</td><td>378.76 (n/a)</td><td>326.00 (n/a)</td><td>241.30 (n/a)</td><td>130.78 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>615.30 (n/a)</td><td>504.62 (n/a)</td><td>495.30 (n/a)</td><td>392.90 (n/a)</td><td>93.33 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>468.90 (n/a)</td><td>309.08 (n/a)</td><td>302.90 (n/a)</td><td>235.00 (n/a)</td><td>95.58 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.40 (n/a)</td><td>310.12 (n/a)</td><td>259.30 (n/a)</td><td>205.70 (n/a)</td><td>147.07 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.00 (n/a)</td><td>471.04 (n/a)</td><td>549.80 (n/a)</td><td>186.30 (n/a)</td><td>170.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.60 (n/a)</td><td>351.78 (n/a)</td><td>249.20 (n/a)</td><td>197.90 (n/a)</td><td>167.74 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>868.00 (n/a)</td><td>493.48 (n/a)</td><td>375.30 (n/a)</td><td>218.50 (n/a)</td><td>277.61 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>769.40 (n/a)</td><td>481.32 (n/a)</td><td>499.70 (n/a)</td><td>251.10 (n/a)</td><td>196.10 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>491.90 (n/a)</td><td>361.14 (n/a)</td><td>324.90 (n/a)</td><td>263.40 (n/a)</td><td>92.97 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>798.20 (n/a)</td><td>533.80 (n/a)</td><td>516.50 (n/a)</td><td>277.80 (n/a)</td><td>189.07 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>476.00 (n/a)</td><td>361.78 (n/a)</td><td>319.80 (n/a)</td><td>270.60 (n/a)</td><td>103.02 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1056.40 (n/a)</td><td>636.84 (n/a)</td><td>530.60 (n/a)</td><td>450.20 (n/a)</td><td>244.94 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>653.20 (n/a)</td><td>440.80 (n/a)</td><td>485.30 (n/a)</td><td>252.80 (n/a)</td><td>173.25 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>617.40 (n/a)</td><td>465.74 (n/a)</td><td>423.50 (n/a)</td><td>374.60 (n/a)</td><td>100.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>590.90 (n/a)</td><td>468.16 (n/a)</td><td>549.70 (n/a)</td><td>292.40 (n/a)</td><td>134.11 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>502.00 (n/a)</td><td>362.74 (n/a)</td><td>329.20 (n/a)</td><td>261.40 (n/a)</td><td>91.06 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2046.40 (n/a)</td><td>694.40 (n/a)</td><td>324.10 (n/a)</td><td>264.50 (n/a)</td><td>763.27 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2411.30 (n/a)</td><td>884.08 (n/a)</td><td>593.00 (n/a)</td><td>285.80 (n/a)</td><td>863.27 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>585.50 (n/a)</td><td>443.74 (n/a)</td><td>462.00 (n/a)</td><td>215.30 (n/a)</td><td>144.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>563.10 (n/a)</td><td>441.22 (n/a)</td><td>436.10 (n/a)</td><td>338.10 (n/a)</td><td>82.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.59 <b>(+20.55%)</b></td><td>0.38 (+10.44%)</td><td>0.34 (-18.03%)</td><td>0.18 <b>(+37.65%)</b></td><td>0.15 (-7.36%)</td><td>1221.50 <b>(-27.35%)</b></td><td>687.02 (-19.46%)</td><td>657.30 <b>(+21.99%)</b></td><td>376.50 (-17.03%)</td><td>324.72 <b>(-39.86%)</b></td><td>25.07 <b>(+20.55%)</b></td><td>16.02 (+10.44%)</td><td>14.36 (-18.03%)</td><td>7.73 <b>(+37.65%)</b></td><td>6.51 (-7.36%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.41 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>1681.40 (n/a)</td><td>853.02 (n/a)</td><td>538.80 (n/a)</td><td>453.80 (n/a)</td><td>539.98 (n/a)</td><td>20.79 (n/a)</td><td>14.50 (n/a)</td><td>17.52 (n/a)</td><td>5.61 (n/a)</td><td>7.02 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.65 <b>(+38.02%)</b></td><td>0.50 <b>(+57.31%)</b></td><td>0.51 <b>(+54.07%)</b></td><td>0.31 <b>(+136.72%)</b></td><td>0.13 (+8.37%)</td><td>705.50 <b>(-57.75%)</b></td><td>467.74 <b>(-43.38%)</b></td><td>432.00 <b>(-35.11%)</b></td><td>339.30 <b>(-27.55%)</b></td><td>144.92 <b>(-69.77%)</b></td><td>27.82 <b>(+38.02%)</b></td><td>21.54 <b>(+57.31%)</b></td><td>21.84 <b>(+54.07%)</b></td><td>13.38 <b>(+136.72%)</b></td><td>5.62 (+8.37%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>1669.90 (n/a)</td><td>826.12 (n/a)</td><td>665.70 (n/a)</td><td>468.30 (n/a)</td><td>479.34 (n/a)</td><td>20.15 (n/a)</td><td>13.69 (n/a)</td><td>14.18 (n/a)</td><td>5.65 (n/a)</td><td>5.18 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.31 (+1.11%)</td><td>0.30 (-0.22%)</td><td>0.30 (-1.09%)</td><td>0.30 (+0.26%)</td><td>0.00 <b>(+24.15%)</b></td><td>84297.90 (-0.26%)</td><td>83241.68 (+0.23%)</td><td>83730.80 (+1.11%)</td><td>81180.80 (-1.10%)</td><td>1221.07 <b>(+22.18%)</b></td><td>211.62 (+1.11%)</td><td>206.42 (-0.22%)</td><td>205.18 (-1.09%)</td><td>203.80 (+0.26%)</td><td>3.07 <b>(+24.15%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84518.30 (n/a)</td><td>83051.94 (n/a)</td><td>82814.90 (n/a)</td><td>82081.00 (n/a)</td><td>999.37 (n/a)</td><td>209.30 (n/a)</td><td>206.88 (n/a)</td><td>207.45 (n/a)</td><td>203.27 (n/a)</td><td>2.48 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.15 (+0.20%)</td><td>1.10 (-3.57%)</td><td>1.13 (-1.61%)</td><td>0.98 (-12.11%)</td><td>0.07 <b>(+477.95%)</b></td><td>25575.80 (+13.78%)</td><td>23008.78 (+4.03%)</td><td>22348.50 (+1.64%)</td><td>21914.50 (-0.20%)</td><td>1495.17 <b>(+561.65%)</b></td><td>783.95 (+0.20%)</td><td>749.03 (-3.57%)</td><td>768.73 (-1.61%)</td><td>671.72 (-12.11%)</td><td>45.50 <b>(+477.94%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>1.14 (n/a)</td><td>1.12 (n/a)</td><td>0.01 (n/a)</td><td>22478.20 (n/a)</td><td>22118.24 (n/a)</td><td>21988.30 (n/a)</td><td>21958.40 (n/a)</td><td>225.98 (n/a)</td><td>782.38 (n/a)</td><td>776.79 (n/a)</td><td>781.32 (n/a)</td><td>764.29 (n/a)</td><td>7.87 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.80 (-0.11%)</td><td>0.79 (-1.19%)</td><td>0.80 (-0.07%)</td><td>0.75 (-5.88%)</td><td>0.02 <b>(+398.54%)</b></td><td>101097.20 (+6.24%)</td><td>95833.52 (+1.28%)</td><td>94936.00 (+0.07%)</td><td>93882.60 (+0.11%)</td><td>2979.86 <b>(+432.81%)</b></td><td>731.97 (-0.11%)</td><td>717.61 (-1.19%)</td><td>723.85 (-0.07%)</td><td>679.74 (-5.88%)</td><td>21.48 <b>(+398.54%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95156.40 (n/a)</td><td>94620.74 (n/a)</td><td>94867.50 (n/a)</td><td>93777.50 (n/a)</td><td>559.27 (n/a)</td><td>732.79 (n/a)</td><td>726.28 (n/a)</td><td>724.37 (n/a)</td><td>722.17 (n/a)</td><td>4.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.77 (-1.34%)</td><td>0.76 (-0.69%)</td><td>0.77 (-0.03%)</td><td>0.75 (-0.06%)</td><td>0.01 (-17.71%)</td><td>101148.70 (+0.06%)</td><td>99267.98 (+0.69%)</td><td>98379.10 (+0.03%)</td><td>97827.50 (+1.36%)</td><td>1618.22 (-16.41%)</td><td>702.46 (-1.34%)</td><td>692.41 (-0.69%)</td><td>698.52 (-0.03%)</td><td>679.39 (-0.06%)</td><td>11.23 (-17.71%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101090.10 (n/a)</td><td>98588.42 (n/a)</td><td>98348.30 (n/a)</td><td>96517.30 (n/a)</td><td>1935.91 (n/a)</td><td>711.99 (n/a)</td><td>697.25 (n/a)</td><td>698.74 (n/a)</td><td>679.78 (n/a)</td><td>13.64 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.88 (-0.54%)</td><td>0.88 (+0.23%)</td><td>0.87 (-1.62%)</td><td>0.87 (+2.33%)</td><td>0.01 <b>(-72.75%)</b></td><td>86772.20 (-2.28%)</td><td>86221.02 (-0.27%)</td><td>86332.90 (+1.65%)</td><td>85330.70 (+0.54%)</td><td>569.42 <b>(-73.24%)</b></td><td>805.33 (-0.54%)</td><td>797.04 (+0.23%)</td><td>795.98 (-1.62%)</td><td>791.95 (+2.33%)</td><td>5.29 <b>(-72.75%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.89 (n/a)</td><td>0.85 (n/a)</td><td>0.02 (n/a)</td><td>88794.30 (n/a)</td><td>86455.48 (n/a)</td><td>84930.70 (n/a)</td><td>84872.40 (n/a)</td><td>2128.16 (n/a)</td><td>809.68 (n/a)</td><td>795.24 (n/a)</td><td>809.12 (n/a)</td><td>773.92 (n/a)</td><td>19.40 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.63 (+6.85%)</td><td>3.81 (-7.20%)</td><td>3.56 (-11.87%)</td><td>2.19 (-0.55%)</td><td>1.58 <b>(+31.29%)</b></td><td>4065.60 (+0.55%)</td><td>2702.18 (+13.19%)</td><td>2503.30 (+13.47%)</td><td>1582.50 (-6.41%)</td><td>1125.51 (+17.79%)</td><td>339.26 (+6.85%)</td><td>229.61 (-7.20%)</td><td>214.47 (-11.87%)</td><td>132.05 (-0.55%)</td><td>94.89 <b>(+31.29%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>5.27 (n/a)</td><td>4.11 (n/a)</td><td>4.04 (n/a)</td><td>2.20 (n/a)</td><td>1.20 (n/a)</td><td>4043.40 (n/a)</td><td>2387.20 (n/a)</td><td>2206.10 (n/a)</td><td>1690.90 (n/a)</td><td>955.56 (n/a)</td><td>317.51 (n/a)</td><td>247.43 (n/a)</td><td>243.36 (n/a)</td><td>132.78 (n/a)</td><td>72.27 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>4.85 (-1.31%)</td><td>3.26 (-3.46%)</td><td>3.10 (+8.52%)</td><td>2.17 (-11.92%)</td><td>0.98 (-8.66%)</td><td>4106.00 (+13.53%)</td><td>2915.90 (+2.84%)</td><td>2877.80 (-7.85%)</td><td>1839.60 (+1.33%)</td><td>809.45 (+1.76%)</td><td>291.85 (-1.31%)</td><td>196.64 (-3.46%)</td><td>186.56 (+8.52%)</td><td>130.75 (-11.92%)</td><td>58.88 (-8.66%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.91 (n/a)</td><td>3.38 (n/a)</td><td>2.85 (n/a)</td><td>2.46 (n/a)</td><td>1.07 (n/a)</td><td>3616.60 (n/a)</td><td>2835.30 (n/a)</td><td>3123.00 (n/a)</td><td>1815.40 (n/a)</td><td>795.46 (n/a)</td><td>295.72 (n/a)</td><td>203.67 (n/a)</td><td>171.91 (n/a)</td><td>148.44 (n/a)</td><td>64.47 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.56 (+7.57%)</td><td>4.63 <b>(+28.12%)</b></td><td>5.46 <b>(+30.48%)</b></td><td>2.18 (+2.41%)</td><td>1.45 (+9.22%)</td><td>4088.40 (-2.35%)</td><td>2190.28 <b>(-21.64%)</b></td><td>1632.00 <b>(-23.36%)</b></td><td>1603.20 (-7.04%)</td><td>1075.59 (-5.16%)</td><td>334.86 (+7.57%)</td><td>278.97 <b>(+28.12%)</b></td><td>328.96 <b>(+30.48%)</b></td><td>131.32 (+2.41%)</td><td>87.49 (+9.22%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>5.17 (n/a)</td><td>3.61 (n/a)</td><td>4.19 (n/a)</td><td>2.13 (n/a)</td><td>1.33 (n/a)</td><td>4187.00 (n/a)</td><td>2794.98 (n/a)</td><td>2129.50 (n/a)</td><td>1724.70 (n/a)</td><td>1134.14 (n/a)</td><td>311.29 (n/a)</td><td>217.74 (n/a)</td><td>252.11 (n/a)</td><td>128.22 (n/a)</td><td>80.11 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>6.61 (+12.74%)</td><td>5.23 (+1.28%)</td><td>5.46 (+7.93%)</td><td>3.71 <b>(-22.36%)</b></td><td>1.24 <b>(+185.93%)</b></td><td>9399.60 <b>(+28.80%)</b></td><td>6995.16 (+3.10%)</td><td>6380.00 (-7.34%)</td><td>5274.80 (-11.30%)</td><td>1767.41 <b>(+228.60%)</b></td><td>407.12 (+12.74%)</td><td>322.29 (+1.28%)</td><td>336.60 (+7.93%)</td><td>228.46 <b>(-22.36%)</b></td><td>76.37 <b>(+185.93%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>5.86 (n/a)</td><td>5.17 (n/a)</td><td>5.06 (n/a)</td><td>4.78 (n/a)</td><td>0.43 (n/a)</td><td>7297.60 (n/a)</td><td>6784.64 (n/a)</td><td>6885.70 (n/a)</td><td>5947.00 (n/a)</td><td>537.86 (n/a)</td><td>361.10 (n/a)</td><td>318.21 (n/a)</td><td>311.88 (n/a)</td><td>294.27 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.13 (+0.48%)</td><td>4.38 (-3.64%)</td><td>4.41 (-5.89%)</td><td>3.61 (-6.92%)</td><td>0.56 (+4.19%)</td><td>9660.40 (+7.43%)</td><td>8065.34 (+3.97%)</td><td>7913.00 (+6.26%)</td><td>6789.80 (-0.48%)</td><td>1061.79 (+12.14%)</td><td>316.28 (+0.48%)</td><td>269.87 (-3.64%)</td><td>271.39 (-5.89%)</td><td>222.30 (-6.92%)</td><td>34.51 (+4.19%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>5.11 (n/a)</td><td>4.55 (n/a)</td><td>4.68 (n/a)</td><td>3.88 (n/a)</td><td>0.54 (n/a)</td><td>8991.90 (n/a)</td><td>7757.40 (n/a)</td><td>7446.60 (n/a)</td><td>6822.50 (n/a)</td><td>946.88 (n/a)</td><td>314.77 (n/a)</td><td>280.06 (n/a)</td><td>288.38 (n/a)</td><td>238.82 (n/a)</td><td>33.12 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>6.35 (-7.35%)</td><td>5.15 (-5.66%)</td><td>4.89 (-17.35%)</td><td>4.10 (+9.07%)</td><td>0.89 <b>(-34.72%)</b></td><td>8505.00 (-8.31%)</td><td>6925.14 (+2.66%)</td><td>7132.50 <b>(+20.99%)</b></td><td>5489.20 (+7.93%)</td><td>1180.62 <b>(-35.97%)</b></td><td>391.22 (-7.35%)</td><td>317.52 (-5.66%)</td><td>301.09 (-17.35%)</td><td>252.50 (+9.07%)</td><td>54.84 <b>(-34.72%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>6.86 (n/a)</td><td>5.46 (n/a)</td><td>5.91 (n/a)</td><td>3.76 (n/a)</td><td>1.36 (n/a)</td><td>9276.30 (n/a)</td><td>6746.00 (n/a)</td><td>5895.10 (n/a)</td><td>5085.80 (n/a)</td><td>1843.77 (n/a)</td><td>422.25 (n/a)</td><td>336.57 (n/a)</td><td>364.28 (n/a)</td><td>231.50 (n/a)</td><td>84.01 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.78 (-1.16%)</td><td>0.77 (+0.69%)</td><td>0.77 (-0.64%)</td><td>0.76 (+2.95%)</td><td>0.01 <b>(-61.10%)</b></td><td>99995.90 (-2.87%)</td><td>98102.74 (-0.77%)</td><td>97510.60 (+0.64%)</td><td>96690.10 (+1.17%)</td><td>1346.27 <b>(-61.89%)</b></td><td>710.72 (-1.16%)</td><td>700.59 (+0.69%)</td><td>704.74 (-0.64%)</td><td>687.22 (+2.95%)</td><td>9.56 <b>(-61.10%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.79 (n/a)</td><td>0.76 (n/a)</td><td>0.78 (n/a)</td><td>0.73 (n/a)</td><td>0.03 (n/a)</td><td>102946.30 (n/a)</td><td>98864.20 (n/a)</td><td>96888.20 (n/a)</td><td>95567.20 (n/a)</td><td>3532.18 (n/a)</td><td>719.07 (n/a)</td><td>695.79 (n/a)</td><td>709.27 (n/a)</td><td>667.53 (n/a)</td><td>24.58 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.78 (+0.56%)</td><td>0.76 (-1.44%)</td><td>0.76 (-0.94%)</td><td>0.73 (-3.42%)</td><td>0.02 <b>(+302.69%)</b></td><td>102996.00 (+3.54%)</td><td>99952.38 (+1.52%)</td><td>99238.20 (+0.95%)</td><td>97342.30 (-0.56%)</td><td>2607.51 <b>(+314.85%)</b></td><td>705.96 (+0.56%)</td><td>687.89 (-1.44%)</td><td>692.47 (-0.94%)</td><td>667.21 (-3.42%)</td><td>17.85 <b>(+302.69%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.00 (n/a)</td><td>99474.20 (n/a)</td><td>98458.48 (n/a)</td><td>98301.20 (n/a)</td><td>97888.00 (n/a)</td><td>628.54 (n/a)</td><td>702.02 (n/a)</td><td>697.98 (n/a)</td><td>699.07 (n/a)</td><td>690.83 (n/a)</td><td>4.43 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.90 (-0.11%)</td><td>0.89 (-0.34%)</td><td>0.89 (-0.74%)</td><td>0.88 (-0.59%)</td><td>0.01 (+9.90%)</td><td>86024.30 (+0.60%)</td><td>84785.46 (+0.34%)</td><td>84668.40 (+0.74%)</td><td>84035.50 (+0.11%)</td><td>782.72 (+10.84%)</td><td>817.74 (-0.11%)</td><td>810.56 (-0.34%)</td><td>811.63 (-0.74%)</td><td>798.84 (-0.59%)</td><td>7.44 (+9.90%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.90 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>85513.80 (n/a)</td><td>84497.50 (n/a)</td><td>84042.50 (n/a)</td><td>83942.20 (n/a)</td><td>706.18 (n/a)</td><td>818.65 (n/a)</td><td>813.32 (n/a)</td><td>817.68 (n/a)</td><td>803.61 (n/a)</td><td>6.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>2.44 <b>(-38.17%)</b></td><td>1.69 <b>(-32.79%)</b></td><td>1.66 <b>(-25.51%)</b></td><td>1.27 (-12.14%)</td><td>0.45 <b>(-60.58%)</b></td><td>6334.50 (+13.82%)</td><td>5017.60 <b>(+31.62%)</b></td><td>4867.30 <b>(+34.25%)</b></td><td>3302.30 <b>(+61.73%)</b></td><td>1149.55 <b>(-31.75%)</b></td><td>640.15 <b>(-38.17%)</b></td><td>442.67 <b>(-32.79%)</b></td><td>434.31 <b>(-25.51%)</b></td><td>333.72 (-12.14%)</td><td>119.03 <b>(-60.58%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.95 (n/a)</td><td>2.51 (n/a)</td><td>2.22 (n/a)</td><td>1.45 (n/a)</td><td>1.15 (n/a)</td><td>5565.40 (n/a)</td><td>3812.08 (n/a)</td><td>3625.50 (n/a)</td><td>2041.90 (n/a)</td><td>1684.39 (n/a)</td><td>1035.26 (n/a)</td><td>658.68 (n/a)</td><td>583.08 (n/a)</td><td>379.83 (n/a)</td><td>301.98 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.22 (-9.33%)</td><td>0.20 (+1.50%)</td><td>0.19 (-5.74%)</td><td>0.18 <b>(+21.98%)</b></td><td>0.01 <b>(-58.35%)</b></td><td>6809.60 (-18.02%)</td><td>6355.46 (-3.47%)</td><td>6516.50 (+6.09%)</td><td>5787.80 (+10.29%)</td><td>434.27 <b>(-62.86%)</b></td><td>11.59 (-9.33%)</td><td>10.60 (+1.50%)</td><td>10.30 (-5.74%)</td><td>9.85 <b>(+21.98%)</b></td><td>0.74 <b>(-58.35%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>8306.70 (n/a)</td><td>6584.00 (n/a)</td><td>6142.70 (n/a)</td><td>5247.70 (n/a)</td><td>1169.31 (n/a)</td><td>12.79 (n/a)</td><td>10.44 (n/a)</td><td>10.92 (n/a)</td><td>8.08 (n/a)</td><td>1.78 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.72 (n/a)</td><td>3.53 (n/a)</td><td>3.49 (n/a)</td><td>3.44 (n/a)</td><td>0.11 (n/a)</td><td>3.72 (n/a)</td><td>3.53 (n/a)</td><td>3.49 (n/a)</td><td>3.44 (n/a)</td><td>0.11 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>6.56 (-12.92%)</td><td>5.72 (-16.24%)</td><td>5.77 (-14.97%)</td><td>4.69 (-19.34%)</td><td>0.68 (-1.44%)</td><td>6.56 (-12.92%)</td><td>5.71 (-16.24%)</td><td>5.76 (-14.97%)</td><td>4.69 (-19.34%)</td><td>0.68 (-1.44%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>7.54 (n/a)</td><td>6.83 (n/a)</td><td>6.78 (n/a)</td><td>5.82 (n/a)</td><td>0.69 (n/a)</td><td>7.53 (n/a)</td><td>6.82 (n/a)</td><td>6.78 (n/a)</td><td>5.82 (n/a)</td><td>0.69 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>13.81 (-1.32%)</td><td>9.01 (+3.17%)</td><td>8.04 (+10.28%)</td><td>7.06 (+0.35%)</td><td>2.75 (-7.58%)</td><td>13.80 (-1.32%)</td><td>9.00 (+3.17%)</td><td>8.03 (+10.28%)</td><td>7.06 (+0.35%)</td><td>2.75 (-7.58%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>14.00 (n/a)</td><td>8.73 (n/a)</td><td>7.29 (n/a)</td><td>7.04 (n/a)</td><td>2.98 (n/a)</td><td>13.99 (n/a)</td><td>8.72 (n/a)</td><td>7.29 (n/a)</td><td>7.03 (n/a)</td><td>2.97 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.79 (n/a)</td><td>3.48 (n/a)</td><td>3.54 (n/a)</td><td>3.01 (n/a)</td><td>0.29 (n/a)</td><td>3.79 (n/a)</td><td>3.47 (n/a)</td><td>3.53 (n/a)</td><td>3.01 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>7.58 (+2.68%)</td><td>6.52 (+3.22%)</td><td>6.61 (+5.58%)</td><td>5.80 (+2.54%)</td><td>0.73 (+2.96%)</td><td>7.57 (+2.68%)</td><td>6.52 (+3.22%)</td><td>6.60 (+5.58%)</td><td>5.80 (+2.54%)</td><td>0.73 (+2.96%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>7.38 (n/a)</td><td>6.32 (n/a)</td><td>6.26 (n/a)</td><td>5.66 (n/a)</td><td>0.71 (n/a)</td><td>7.38 (n/a)</td><td>6.32 (n/a)</td><td>6.25 (n/a)</td><td>5.66 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>14.05 (+0.79%)</td><td>10.21 (+0.33%)</td><td>10.41 (+5.21%)</td><td>6.38 (-15.16%)</td><td>3.36 <b>(+29.22%)</b></td><td>14.04 (+0.79%)</td><td>10.20 (+0.33%)</td><td>10.40 (+5.21%)</td><td>6.38 (-15.16%)</td><td>3.35 <b>(+29.22%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>13.94 (n/a)</td><td>10.18 (n/a)</td><td>9.89 (n/a)</td><td>7.52 (n/a)</td><td>2.60 (n/a)</td><td>13.93 (n/a)</td><td>10.17 (n/a)</td><td>9.88 (n/a)</td><td>7.52 (n/a)</td><td>2.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.04 (-13.30%)</td><td>2.38 (-12.80%)</td><td>2.74 (-4.29%)</td><td>1.45 (-7.75%)</td><td>0.77 (+8.84%)</td><td>3.04 (-13.30%)</td><td>2.37 (-12.80%)</td><td>2.73 (-4.29%)</td><td>1.44 (-7.75%)</td><td>0.77 (+8.84%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.51 (n/a)</td><td>2.73 (n/a)</td><td>2.86 (n/a)</td><td>1.57 (n/a)</td><td>0.71 (n/a)</td><td>3.50 (n/a)</td><td>2.72 (n/a)</td><td>2.85 (n/a)</td><td>1.57 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.50 <b>(+31.43%)</b></td><td>0.32 <b>(+78.30%)</b></td><td>0.33 <b>(+178.28%)</b></td><td>0.08 (-1.52%)</td><td>0.15 (+18.14%)</td><td>0.49 <b>(+31.43%)</b></td><td>0.31 <b>(+78.30%)</b></td><td>0.32 <b>(+178.28%)</b></td><td>0.07 (-1.52%)</td><td>0.15 (+18.14%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.38 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.13 (n/a)</td><td>0.37 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.73 (+7.09%)</td><td>0.44 (-14.33%)</td><td>0.46 (-10.08%)</td><td>0.08 <b>(-78.96%)</b></td><td>0.24 <b>(+72.56%)</b></td><td>0.72 (+7.09%)</td><td>0.44 (-14.33%)</td><td>0.46 (-10.08%)</td><td>0.08 <b>(-78.96%)</b></td><td>0.24 <b>(+72.56%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.68 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.37 (n/a)</td><td>0.14 (n/a)</td><td>0.67 (n/a)</td><td>0.51 (n/a)</td><td>0.51 (n/a)</td><td>0.37 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>2.49 (+0.73%)</td><td>1.64 (-13.25%)</td><td>2.03 (-11.56%)</td><td>0.66 <b>(+44.24%)</b></td><td>0.90 (+5.31%)</td><td>2.45 (+0.73%)</td><td>1.62 (-13.25%)</td><td>1.99 (-11.56%)</td><td>0.65 <b>(+44.24%)</b></td><td>0.88 (+5.31%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>2.47 (n/a)</td><td>1.90 (n/a)</td><td>2.29 (n/a)</td><td>0.46 (n/a)</td><td>0.85 (n/a)</td><td>2.43 (n/a)</td><td>1.87 (n/a)</td><td>2.25 (n/a)</td><td>0.45 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>567.00 (n/a)</td><td>354.36 (n/a)</td><td>298.40 (n/a)</td><td>231.20 (n/a)</td><td>142.76 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>572.20 (n/a)</td><td>431.06 (n/a)</td><td>463.80 (n/a)</td><td>263.60 (n/a)</td><td>141.76 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>523.70 (n/a)</td><td>385.98 (n/a)</td><td>459.70 (n/a)</td><td>228.70 (n/a)</td><td>138.34 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1968.90 (n/a)</td><td>717.98 (n/a)</td><td>421.60 (n/a)</td><td>327.70 (n/a)</td><td>701.11 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>615.70 (n/a)</td><td>488.86 (n/a)</td><td>548.80 (n/a)</td><td>236.10 (n/a)</td><td>148.63 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>751.30 (n/a)</td><td>513.78 (n/a)</td><td>453.40 (n/a)</td><td>296.70 (n/a)</td><td>185.43 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>475.00 (n/a)</td><td>340.42 (n/a)</td><td>285.40 (n/a)</td><td>228.80 (n/a)</td><td>123.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.80 (n/a)</td><td>366.36 (n/a)</td><td>335.90 (n/a)</td><td>275.90 (n/a)</td><td>95.19 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.40 (n/a)</td><td>358.80 (n/a)</td><td>307.20 (n/a)</td><td>224.30 (n/a)</td><td>135.87 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.00 (n/a)</td><td>512.80 (n/a)</td><td>515.20 (n/a)</td><td>456.20 (n/a)</td><td>56.62 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>554.30 (n/a)</td><td>361.80 (n/a)</td><td>289.30 (n/a)</td><td>213.10 (n/a)</td><td>164.29 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1041.20 (n/a)</td><td>594.30 (n/a)</td><td>578.80 (n/a)</td><td>195.40 (n/a)</td><td>300.47 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1782.30 (n/a)</td><td>745.32 (n/a)</td><td>562.70 (n/a)</td><td>251.20 (n/a)</td><td>601.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>560.60 (n/a)</td><td>365.52 (n/a)</td><td>284.10 (n/a)</td><td>226.90 (n/a)</td><td>147.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1854.30 (n/a)</td><td>609.24 (n/a)</td><td>278.00 (n/a)</td><td>168.40 (n/a)</td><td>704.45 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>550.70 (n/a)</td><td>342.40 (n/a)</td><td>301.50 (n/a)</td><td>214.50 (n/a)</td><td>135.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1100.40 (n/a)</td><td>511.70 (n/a)</td><td>475.20 (n/a)</td><td>175.60 (n/a)</td><td>359.32 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>518.70 (n/a)</td><td>415.66 (n/a)</td><td>451.40 (n/a)</td><td>267.20 (n/a)</td><td>99.79 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>538.30 (n/a)</td><td>447.44 (n/a)</td><td>475.30 (n/a)</td><td>280.40 (n/a)</td><td>102.35 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>610.70 (n/a)</td><td>350.42 (n/a)</td><td>287.40 (n/a)</td><td>260.90 (n/a)</td><td>146.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>549.40 (n/a)</td><td>380.28 (n/a)</td><td>302.20 (n/a)</td><td>261.10 (n/a)</td><td>135.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>558.40 (n/a)</td><td>391.12 (n/a)</td><td>354.80 (n/a)</td><td>254.50 (n/a)</td><td>142.92 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>496.10 (n/a)</td><td>386.50 (n/a)</td><td>423.70 (n/a)</td><td>248.70 (n/a)</td><td>120.19 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>526.40 (n/a)</td><td>404.00 (n/a)</td><td>466.00 (n/a)</td><td>261.80 (n/a)</td><td>125.08 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-8.74%)</td><td>0.01 (+5.09%)</td><td>0.02 (+8.46%)</td><td>0.01 <b>(+26.42%)</b></td><td>0.00 (-17.62%)</td><td>530.90 <b>(-20.89%)</b></td><td>311.60 (-10.46%)</td><td>263.50 (-7.80%)</td><td>242.90 (+9.56%)</td><td>123.28 <b>(-32.63%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>671.10 (n/a)</td><td>348.00 (n/a)</td><td>285.80 (n/a)</td><td>221.70 (n/a)</td><td>183.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 <b>(+45.67%)</b></td><td>0.01 (+16.81%)</td><td>0.01 (-9.81%)</td><td>0.01 (+1.71%)</td><td>0.01 <b>(+86.44%)</b></td><td>543.80 (-1.68%)</td><td>390.06 (-6.06%)</td><td>467.30 (+10.87%)</td><td>193.90 <b>(-31.36%)</b></td><td>156.40 <b>(+28.54%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.10 (n/a)</td><td>415.24 (n/a)</td><td>421.50 (n/a)</td><td>282.50 (n/a)</td><td>121.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-5.49%)</td><td>0.01 (-16.06%)</td><td>0.01 <b>(-24.17%)</b></td><td>0.01 (+9.48%)</td><td>0.00 <b>(-21.32%)</b></td><td>570.00 (-8.65%)</td><td>446.48 (+13.37%)</td><td>462.40 <b>(+31.89%)</b></td><td>259.90 (+5.82%)</td><td>115.88 <b>(-26.95%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>624.00 (n/a)</td><td>393.82 (n/a)</td><td>350.60 (n/a)</td><td>245.60 (n/a)</td><td>158.64 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (+2.04%)</td><td>0.01 (-2.74%)</td><td>0.01 (-2.62%)</td><td>0.01 <b>(+78.95%)</b></td><td>0.00 <b>(-25.12%)</b></td><td>559.70 <b>(-44.12%)</b></td><td>447.44 (-12.53%)</td><td>503.80 (+2.69%)</td><td>240.60 (-2.00%)</td><td>135.36 <b>(-55.80%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1001.60 (n/a)</td><td>511.54 (n/a)</td><td>490.60 (n/a)</td><td>245.50 (n/a)</td><td>306.23 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (+8.09%)</td><td>0.01 (+9.34%)</td><td>0.01 (-9.50%)</td><td>0.01 <b>(+281.18%)</b></td><td>0.00 <b>(-28.84%)</b></td><td>651.20 <b>(-73.77%)</b></td><td>519.04 <b>(-52.95%)</b></td><td>592.20 (+10.51%)</td><td>233.90 (-7.48%)</td><td>165.88 <b>(-84.04%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2482.30 (n/a)</td><td>1103.14 (n/a)</td><td>535.90 (n/a)</td><td>252.80 (n/a)</td><td>1039.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (-7.38%)</td><td>0.01 (-18.00%)</td><td>0.01 <b>(-23.44%)</b></td><td>0.01 <b>(-32.14%)</b></td><td>0.00 <b>(+23.92%)</b></td><td>807.00 <b>(+47.37%)</b></td><td>554.86 <b>(+30.57%)</b></td><td>586.60 <b>(+30.62%)</b></td><td>336.70 (+7.99%)</td><td>205.02 <b>(+94.68%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.60 (n/a)</td><td>424.96 (n/a)</td><td>449.10 (n/a)</td><td>311.80 (n/a)</td><td>105.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (-6.64%)</td><td>0.02 <b>(-20.22%)</b></td><td>0.03 <b>(-26.95%)</b></td><td>0.01 <b>(-23.81%)</b></td><td>0.01 (+3.59%)</td><td>575.60 <b>(+31.24%)</b></td><td>372.28 <b>(+28.99%)</b></td><td>327.50 <b>(+36.86%)</b></td><td>247.60 (+7.09%)</td><td>130.64 <b>(+48.23%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>438.60 (n/a)</td><td>288.62 (n/a)</td><td>239.30 (n/a)</td><td>231.20 (n/a)</td><td>88.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (+11.59%)</td><td>0.03 <b>(+39.37%)</b></td><td>0.03 <b>(+31.04%)</b></td><td>0.02 <b>(+375.89%)</b></td><td>0.01 <b>(-44.33%)</b></td><td>404.70 <b>(-78.99%)</b></td><td>324.82 <b>(-53.96%)</b></td><td>294.80 <b>(-23.71%)</b></td><td>246.00 (-10.38%)</td><td>72.08 <b>(-89.63%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1926.10 (n/a)</td><td>705.52 (n/a)</td><td>386.40 (n/a)</td><td>274.50 (n/a)</td><td>695.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 <b>(+49.57%)</b></td><td>0.03 <b>(+85.57%)</b></td><td>0.03 <b>(+92.67%)</b></td><td>0.03 <b>(+99.65%)</b></td><td>0.00 (-5.84%)</td><td>309.50 <b>(-49.90%)</b></td><td>248.40 <b>(-47.80%)</b></td><td>242.30 <b>(-48.10%)</b></td><td>214.10 <b>(-33.16%)</b></td><td>36.28 <b>(-66.71%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>617.80 (n/a)</td><td>475.82 (n/a)</td><td>466.90 (n/a)</td><td>320.30 (n/a)</td><td>108.99 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (-8.41%)</td><td>0.02 (+6.08%)</td><td>0.02 (+12.83%)</td><td>0.01 <b>(+165.60%)</b></td><td>0.01 <b>(-32.55%)</b></td><td>721.00 <b>(-62.35%)</b></td><td>455.56 <b>(-36.65%)</b></td><td>489.50 (-11.37%)</td><td>265.70 (+9.21%)</td><td>187.43 <b>(-72.85%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1915.10 (n/a)</td><td>719.10 (n/a)</td><td>552.30 (n/a)</td><td>243.30 (n/a)</td><td>690.27 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (-12.94%)</td><td>0.02 (-16.45%)</td><td>0.02 (-14.65%)</td><td>0.00 <b>(-78.30%)</b></td><td>0.01 <b>(+26.69%)</b></td><td>2465.50 <b>(+360.84%)</b></td><td>753.74 <b>(+114.99%)</b></td><td>340.80 (+17.15%)</td><td>244.30 (+14.86%)</td><td>959.83 <b>(+622.74%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>535.00 (n/a)</td><td>350.60 (n/a)</td><td>290.90 (n/a)</td><td>212.70 (n/a)</td><td>132.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 <b>(+50.23%)</b></td><td>0.02 <b>(+50.23%)</b></td><td>0.03 <b>(+59.74%)</b></td><td>0.01 <b>(+66.98%)</b></td><td>0.01 <b>(+80.92%)</b></td><td>624.20 <b>(-40.11%)</b></td><td>398.52 <b>(-31.30%)</b></td><td>305.80 <b>(-37.39%)</b></td><td>246.70 <b>(-33.43%)</b></td><td>182.72 <b>(-32.05%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1042.30 (n/a)</td><td>580.12 (n/a)</td><td>488.40 (n/a)</td><td>370.60 (n/a)</td><td>268.89 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 <b>(+23.16%)</b></td><td>0.02 (-14.63%)</td><td>0.03 (-4.33%)</td><td>0.00 <b>(-77.21%)</b></td><td>0.01 <b>(+180.74%)</b></td><td>1900.40 <b>(+338.79%)</b></td><td>656.90 <b>(+114.39%)</b></td><td>292.40 (+4.54%)</td><td>208.80 (-18.82%)</td><td>716.47 <b>(+885.05%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>433.10 (n/a)</td><td>306.40 (n/a)</td><td>279.70 (n/a)</td><td>257.20 (n/a)</td><td>72.73 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (-9.98%)</td><td>0.02 (-8.81%)</td><td>0.02 <b>(-21.20%)</b></td><td>0.01 (+14.77%)</td><td>0.01 (-14.68%)</td><td>588.30 (-12.86%)</td><td>434.16 (+6.33%)</td><td>451.00 <b>(+26.93%)</b></td><td>302.80 (+11.08%)</td><td>121.06 <b>(-23.56%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>675.10 (n/a)</td><td>408.30 (n/a)</td><td>355.30 (n/a)</td><td>272.60 (n/a)</td><td>158.39 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (+7.45%)</td><td>0.06 (+9.40%)</td><td>0.07 (+2.89%)</td><td>0.03 (+8.26%)</td><td>0.02 (-9.41%)</td><td>500.90 (-7.63%)</td><td>309.60 (-11.47%)</td><td>241.80 (-2.81%)</td><td>228.60 (-6.92%)</td><td>115.49 (-19.16%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>542.30 (n/a)</td><td>349.70 (n/a)</td><td>248.80 (n/a)</td><td>245.60 (n/a)</td><td>142.87 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (+19.62%)</td><td>0.05 <b>(+33.92%)</b></td><td>0.05 <b>(+37.55%)</b></td><td>0.03 <b>(+62.32%)</b></td><td>0.02 <b>(+20.64%)</b></td><td>472.60 <b>(-38.38%)</b></td><td>350.02 <b>(-26.91%)</b></td><td>336.50 <b>(-27.31%)</b></td><td>237.60 (-16.40%)</td><td>109.10 <b>(-38.74%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>767.00 (n/a)</td><td>478.92 (n/a)</td><td>462.90 (n/a)</td><td>284.20 (n/a)</td><td>178.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (-10.84%)</td><td>0.06 (+9.53%)</td><td>0.06 (+6.85%)</td><td>0.03 (+10.65%)</td><td>0.02 <b>(-20.47%)</b></td><td>577.70 (-9.62%)</td><td>327.48 (-13.09%)</td><td>261.60 (-6.40%)</td><td>248.90 (+12.17%)</td><td>141.29 (-19.08%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>639.20 (n/a)</td><td>376.82 (n/a)</td><td>279.50 (n/a)</td><td>221.90 (n/a)</td><td>174.61 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (+6.93%)</td><td>0.04 (-1.87%)</td><td>0.03 (-6.57%)</td><td>0.03 (-8.00%)</td><td>0.02 (+18.03%)</td><td>611.60 (+8.71%)</td><td>468.00 (+5.55%)</td><td>507.50 (+7.04%)</td><td>218.00 (-6.48%)</td><td>150.77 (+17.30%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>562.60 (n/a)</td><td>443.40 (n/a)</td><td>474.10 (n/a)</td><td>233.10 (n/a)</td><td>128.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (-12.96%)</td><td>0.05 (-1.06%)</td><td>0.07 (+16.62%)</td><td>0.02 <b>(+217.25%)</b></td><td>0.02 (-12.16%)</td><td>753.30 <b>(-68.48%)</b></td><td>430.54 <b>(-38.88%)</b></td><td>247.00 (-14.27%)</td><td>240.90 (+14.93%)</td><td>256.30 <b>(-72.86%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2389.90 (n/a)</td><td>704.40 (n/a)</td><td>288.10 (n/a)</td><td>209.60 (n/a)</td><td>944.40 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (-3.32%)</td><td>0.04 (-18.06%)</td><td>0.03 <b>(-36.05%)</b></td><td>0.01 <b>(-66.32%)</b></td><td>0.02 <b>(+45.30%)</b></td><td>1780.00 <b>(+196.91%)</b></td><td>713.24 <b>(+73.70%)</b></td><td>561.80 <b>(+56.36%)</b></td><td>264.70 (+3.44%)</td><td>621.04 <b>(+320.26%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.50 (n/a)</td><td>410.62 (n/a)</td><td>359.30 (n/a)</td><td>255.90 (n/a)</td><td>147.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (+3.31%)</td><td>0.10 (-0.45%)</td><td>0.12 (+8.82%)</td><td>0.03 <b>(-42.37%)</b></td><td>0.05 <b>(+31.32%)</b></td><td>1037.60 <b>(+73.51%)</b></td><td>451.06 <b>(+21.10%)</b></td><td>278.60 (-8.11%)</td><td>238.00 (-3.21%)</td><td>340.78 <b>(+121.18%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>598.00 (n/a)</td><td>372.48 (n/a)</td><td>303.20 (n/a)</td><td>245.90 (n/a)</td><td>154.07 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 <b>(-22.58%)</b></td><td>0.10 (-16.84%)</td><td>0.09 <b>(-24.28%)</b></td><td>0.06 (-16.98%)</td><td>0.03 <b>(-24.91%)</b></td><td>516.80 <b>(+20.47%)</b></td><td>361.20 (+18.92%)</td><td>378.30 <b>(+32.04%)</b></td><td>252.30 <b>(+29.19%)</b></td><td>105.49 (+12.84%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>429.00 (n/a)</td><td>303.74 (n/a)</td><td>286.50 (n/a)</td><td>195.30 (n/a)</td><td>93.49 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (-12.47%)</td><td>0.11 (-5.11%)</td><td>0.10 (-9.71%)</td><td>0.07 (+3.13%)</td><td>0.02 <b>(-29.28%)</b></td><td>447.80 (-3.03%)</td><td>319.28 (+1.94%)</td><td>319.50 (+10.75%)</td><td>239.10 (+14.24%)</td><td>79.66 <b>(-20.75%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>461.80 (n/a)</td><td>313.20 (n/a)</td><td>288.50 (n/a)</td><td>209.30 (n/a)</td><td>100.52 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (+3.72%)</td><td>0.09 (+14.68%)</td><td>0.08 <b>(+33.31%)</b></td><td>0.06 (+8.52%)</td><td>0.03 (-4.31%)</td><td>522.00 (-7.86%)</td><td>376.64 (-14.95%)</td><td>385.50 <b>(-25.00%)</b></td><td>245.20 (-3.58%)</td><td>118.50 (-19.92%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>566.50 (n/a)</td><td>442.86 (n/a)</td><td>514.00 (n/a)</td><td>254.30 (n/a)</td><td>147.99 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (+11.50%)</td><td>0.07 <b>(-20.42%)</b></td><td>0.06 (-14.02%)</td><td>0.01 <b>(-78.11%)</b></td><td>0.04 <b>(+85.51%)</b></td><td>2474.50 <b>(+356.89%)</b></td><td>849.48 <b>(+107.38%)</b></td><td>506.20 (+16.31%)</td><td>257.20 (-10.32%)</td><td>914.78 <b>(+800.92%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>541.60 (n/a)</td><td>409.62 (n/a)</td><td>435.20 (n/a)</td><td>286.80 (n/a)</td><td>101.54 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-17.79%)</td><td>0.01 (+1.60%)</td><td>0.01 (-1.91%)</td><td>0.01 <b>(+96.78%)</b></td><td>0.00 <b>(-33.66%)</b></td><td>501.20 <b>(-49.18%)</b></td><td>369.76 (-19.03%)</td><td>358.20 (+1.94%)</td><td>235.30 <b>(+21.66%)</b></td><td>124.52 <b>(-60.08%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>986.30 (n/a)</td><td>456.64 (n/a)</td><td>351.40 (n/a)</td><td>193.40 (n/a)</td><td>311.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-15.93%)</td><td>0.01 (-16.73%)</td><td>0.01 (-4.42%)</td><td>0.01 <b>(-27.38%)</b></td><td>0.00 (+13.13%)</td><td>524.00 <b>(+37.68%)</b></td><td>356.64 <b>(+24.71%)</b></td><td>293.80 (+4.63%)</td><td>251.60 (+18.96%)</td><td>112.92 <b>(+86.14%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>380.60 (n/a)</td><td>285.98 (n/a)</td><td>280.80 (n/a)</td><td>211.50 (n/a)</td><td>60.66 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 <b>(-28.59%)</b></td><td>0.01 (-5.99%)</td><td>0.01 (+11.02%)</td><td>0.01 <b>(-23.91%)</b></td><td>0.00 <b>(-33.05%)</b></td><td>553.00 <b>(+31.42%)</b></td><td>326.62 (+5.82%)</td><td>279.10 (-9.94%)</td><td>242.90 <b>(+40.00%)</b></td><td>127.59 <b>(+36.99%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>420.80 (n/a)</td><td>308.66 (n/a)</td><td>309.90 (n/a)</td><td>173.50 (n/a)</td><td>93.14 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-6.67%)</td><td>0.01 (+3.75%)</td><td>0.01 (+14.33%)</td><td>0.01 (+3.14%)</td><td>0.00 (-7.72%)</td><td>491.90 (-3.05%)</td><td>390.40 (-4.60%)</td><td>421.80 (-12.54%)</td><td>268.40 (+7.15%)</td><td>108.04 (-6.78%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>507.40 (n/a)</td><td>409.24 (n/a)</td><td>482.30 (n/a)</td><td>250.50 (n/a)</td><td>115.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (+2.06%)</td><td>0.01 (-19.11%)</td><td>0.01 (-12.36%)</td><td>0.00 <b>(-56.06%)</b></td><td>0.00 <b>(+46.91%)</b></td><td>1308.00 <b>(+127.60%)</b></td><td>627.22 <b>(+47.85%)</b></td><td>504.60 (+14.09%)</td><td>307.70 (-2.01%)</td><td>394.13 <b>(+267.82%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>574.70 (n/a)</td><td>424.24 (n/a)</td><td>442.30 (n/a)</td><td>314.00 (n/a)</td><td>107.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (+5.14%)</td><td>0.02 (+0.83%)</td><td>0.01 (-0.40%)</td><td>0.01 (+7.97%)</td><td>0.00 (-1.34%)</td><td>425.60 (-7.40%)</td><td>291.12 (-2.08%)</td><td>291.30 (+0.41%)</td><td>186.30 (-4.85%)</td><td>87.11 (-14.18%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>459.60 (n/a)</td><td>297.30 (n/a)</td><td>290.10 (n/a)</td><td>195.80 (n/a)</td><td>101.50 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-14.39%)</td><td>0.01 <b>(+32.85%)</b></td><td>0.01 <b>(+76.80%)</b></td><td>0.01 <b>(+39.12%)</b></td><td>0.00 <b>(-53.13%)</b></td><td>381.30 <b>(-28.11%)</b></td><td>291.60 <b>(-33.91%)</b></td><td>282.80 <b>(-43.44%)</b></td><td>216.50 (+16.77%)</td><td>59.26 <b>(-59.23%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>530.40 (n/a)</td><td>441.20 (n/a)</td><td>500.00 (n/a)</td><td>185.40 (n/a)</td><td>145.33 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (-16.23%)</td><td>0.01 <b>(-21.37%)</b></td><td>0.01 <b>(-30.97%)</b></td><td>0.01 (-9.68%)</td><td>0.00 <b>(-30.14%)</b></td><td>551.20 (+10.70%)</td><td>454.48 <b>(+24.37%)</b></td><td>458.30 <b>(+44.85%)</b></td><td>320.00 (+19.36%)</td><td>100.62 (-5.98%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>497.90 (n/a)</td><td>365.42 (n/a)</td><td>316.40 (n/a)</td><td>268.10 (n/a)</td><td>107.02 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (+14.98%)</td><td>0.01 <b>(+34.23%)</b></td><td>0.01 <b>(+34.97%)</b></td><td>0.01 <b>(+36.13%)</b></td><td>0.00 (+5.90%)</td><td>487.20 <b>(-26.55%)</b></td><td>383.72 <b>(-27.15%)</b></td><td>438.90 <b>(-25.91%)</b></td><td>248.10 (-13.04%)</td><td>105.72 <b>(-30.01%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>663.30 (n/a)</td><td>526.76 (n/a)</td><td>592.40 (n/a)</td><td>285.30 (n/a)</td><td>151.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (+13.58%)</td><td>0.01 (+3.96%)</td><td>0.01 (+1.35%)</td><td>0.01 (-8.31%)</td><td>0.00 <b>(+48.35%)</b></td><td>595.80 (+9.06%)</td><td>444.00 (-1.05%)</td><td>432.10 (-1.32%)</td><td>294.10 (-11.95%)</td><td>112.07 <b>(+43.15%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>546.30 (n/a)</td><td>448.70 (n/a)</td><td>437.90 (n/a)</td><td>334.00 (n/a)</td><td>78.28 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (-8.79%)</td><td>0.01 (-12.84%)</td><td>0.01 (-14.98%)</td><td>0.01 <b>(-26.05%)</b></td><td>0.00 (+18.54%)</td><td>747.60 <b>(+35.21%)</b></td><td>495.32 (+19.87%)</td><td>464.10 (+17.61%)</td><td>323.10 (+9.64%)</td><td>168.07 <b>(+75.58%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>552.90 (n/a)</td><td>413.22 (n/a)</td><td>394.60 (n/a)</td><td>294.70 (n/a)</td><td>95.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 <b>(+43.93%)</b></td><td>0.02 (+2.34%)</td><td>0.02 (-9.13%)</td><td>0.01 (-4.58%)</td><td>0.01 <b>(+101.56%)</b></td><td>586.10 (+4.81%)</td><td>399.56 (+4.58%)</td><td>375.60 (+10.05%)</td><td>221.80 <b>(-30.51%)</b></td><td>140.14 <b>(+40.32%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.20 (n/a)</td><td>382.06 (n/a)</td><td>341.30 (n/a)</td><td>319.20 (n/a)</td><td>99.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (+4.16%)</td><td>0.02 (-18.17%)</td><td>0.02 <b>(-38.22%)</b></td><td>0.01 <b>(-27.35%)</b></td><td>0.01 <b>(+41.68%)</b></td><td>902.80 <b>(+37.64%)</b></td><td>489.36 <b>(+38.52%)</b></td><td>470.60 <b>(+61.83%)</b></td><td>241.90 (-4.01%)</td><td>273.36 <b>(+60.52%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>655.90 (n/a)</td><td>353.28 (n/a)</td><td>290.80 (n/a)</td><td>252.00 (n/a)</td><td>170.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (-10.15%)</td><td>0.02 (-9.53%)</td><td>0.02 (-17.20%)</td><td>0.01 (+9.99%)</td><td>0.01 <b>(-25.96%)</b></td><td>573.30 (-9.09%)</td><td>414.92 (+4.21%)</td><td>341.60 <b>(+20.79%)</b></td><td>278.10 (+11.33%)</td><td>140.86 <b>(-21.11%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.60 (n/a)</td><td>398.16 (n/a)</td><td>282.80 (n/a)</td><td>249.80 (n/a)</td><td>178.56 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (-2.68%)</td><td>0.02 (-2.83%)</td><td>0.02 (-9.79%)</td><td>0.01 <b>(+63.76%)</b></td><td>0.01 <b>(-29.08%)</b></td><td>643.60 <b>(-38.94%)</b></td><td>436.30 (-14.87%)</td><td>419.40 (+10.84%)</td><td>245.30 (+2.76%)</td><td>153.09 <b>(-54.85%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1054.00 (n/a)</td><td>512.54 (n/a)</td><td>378.40 (n/a)</td><td>238.70 (n/a)</td><td>339.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (+0.90%)</td><td>0.02 (-9.93%)</td><td>0.02 <b>(-22.46%)</b></td><td>0.01 <b>(-20.47%)</b></td><td>0.01 <b>(+45.26%)</b></td><td>585.00 <b>(+25.73%)</b></td><td>447.80 (+18.37%)</td><td>503.40 <b>(+28.98%)</b></td><td>257.40 (-0.89%)</td><td>144.12 <b>(+93.17%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>465.30 (n/a)</td><td>378.30 (n/a)</td><td>390.30 (n/a)</td><td>259.70 (n/a)</td><td>74.61 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (-8.53%)</td><td>0.02 <b>(-23.75%)</b></td><td>0.02 <b>(-40.70%)</b></td><td>0.01 (-9.07%)</td><td>0.01 (+6.70%)</td><td>586.90 (+9.97%)</td><td>444.74 <b>(+34.57%)</b></td><td>495.60 <b>(+68.63%)</b></td><td>244.50 (+9.30%)</td><td>146.34 <b>(+22.58%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.70 (n/a)</td><td>330.48 (n/a)</td><td>293.90 (n/a)</td><td>223.70 (n/a)</td><td>119.39 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 <b>(-21.30%)</b></td><td>0.02 (-18.64%)</td><td>0.02 <b>(-28.87%)</b></td><td>0.01 (-3.64%)</td><td>0.01 <b>(-34.81%)</b></td><td>564.20 (+3.77%)</td><td>429.02 (+17.60%)</td><td>441.10 <b>(+40.61%)</b></td><td>306.50 <b>(+27.07%)</b></td><td>111.55 (-16.10%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.70 (n/a)</td><td>364.80 (n/a)</td><td>313.70 (n/a)</td><td>241.20 (n/a)</td><td>132.96 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 <b>(-25.40%)</b></td><td>0.02 (-19.93%)</td><td>0.02 <b>(-29.53%)</b></td><td>0.01 (-1.05%)</td><td>0.01 <b>(-46.79%)</b></td><td>622.00 (+1.06%)</td><td>427.72 (+10.43%)</td><td>353.30 <b>(+41.89%)</b></td><td>301.90 <b>(+34.06%)</b></td><td>140.19 <b>(-30.45%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.50 (n/a)</td><td>387.32 (n/a)</td><td>249.00 (n/a)</td><td>225.20 (n/a)</td><td>201.56 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (-7.87%)</td><td>0.02 <b>(-20.64%)</b></td><td>0.02 <b>(-28.70%)</b></td><td>0.02 (+2.96%)</td><td>0.01 <b>(-21.35%)</b></td><td>502.00 (-2.88%)</td><td>355.70 <b>(+21.43%)</b></td><td>330.60 <b>(+40.26%)</b></td><td>240.40 (+8.58%)</td><td>101.21 (-19.67%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.90 (n/a)</td><td>292.92 (n/a)</td><td>235.70 (n/a)</td><td>221.40 (n/a)</td><td>126.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 <b>(-23.27%)</b></td><td>0.02 (-6.30%)</td><td>0.02 <b>(+25.77%)</b></td><td>0.01 <b>(+35.23%)</b></td><td>0.01 <b>(-41.20%)</b></td><td>789.80 <b>(-26.06%)</b></td><td>462.04 (-9.53%)</td><td>363.10 <b>(-20.48%)</b></td><td>313.70 <b>(+30.33%)</b></td><td>196.67 <b>(-41.07%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1068.10 (n/a)</td><td>510.70 (n/a)</td><td>456.60 (n/a)</td><td>240.70 (n/a)</td><td>333.73 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 <b>(+22.19%)</b></td><td>0.02 (-9.33%)</td><td>0.02 (-9.53%)</td><td>0.01 <b>(-41.13%)</b></td><td>0.01 <b>(+79.04%)</b></td><td>1037.90 <b>(+69.87%)</b></td><td>569.00 <b>(+29.25%)</b></td><td>477.40 (+10.53%)</td><td>249.60 (-18.16%)</td><td>297.15 <b>(+150.32%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.00 (n/a)</td><td>440.22 (n/a)</td><td>431.90 (n/a)</td><td>305.00 (n/a)</td><td>118.71 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 <b>(-21.19%)</b></td><td>0.02 (+4.71%)</td><td>0.02 (+13.12%)</td><td>0.02 <b>(+25.64%)</b></td><td>0.00 <b>(-48.91%)</b></td><td>504.80 <b>(-20.42%)</b></td><td>414.20 (-10.78%)</td><td>441.70 (-11.61%)</td><td>318.40 <b>(+26.90%)</b></td><td>76.13 <b>(-45.67%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>634.30 (n/a)</td><td>464.26 (n/a)</td><td>499.70 (n/a)</td><td>250.90 (n/a)</td><td>140.12 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (-10.17%)</td><td>0.05 (+6.55%)</td><td>0.05 <b>(+61.69%)</b></td><td>0.03 (+8.55%)</td><td>0.02 <b>(-34.27%)</b></td><td>511.90 (-7.87%)</td><td>348.04 (-14.71%)</td><td>310.40 <b>(-38.14%)</b></td><td>232.20 (+11.31%)</td><td>113.40 <b>(-32.80%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>555.60 (n/a)</td><td>408.08 (n/a)</td><td>501.80 (n/a)</td><td>208.60 (n/a)</td><td>168.75 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (-3.02%)</td><td>0.06 (+5.43%)</td><td>0.06 (+14.14%)</td><td>0.03 (+8.62%)</td><td>0.01 (-15.27%)</td><td>500.10 (-7.93%)</td><td>313.72 (-7.34%)</td><td>268.90 (-12.38%)</td><td>242.20 (+3.11%)</td><td>105.79 (-15.20%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>543.20 (n/a)</td><td>338.56 (n/a)</td><td>306.90 (n/a)</td><td>234.90 (n/a)</td><td>124.75 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 <b>(-40.14%)</b></td><td>0.04 <b>(-21.70%)</b></td><td>0.04 <b>(-28.61%)</b></td><td>0.03 (+7.56%)</td><td>0.01 <b>(-70.34%)</b></td><td>571.50 (-7.03%)</td><td>422.22 (+8.97%)</td><td>397.20 <b>(+40.06%)</b></td><td>366.00 <b>(+67.05%)</b></td><td>85.40 <b>(-55.31%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>614.70 (n/a)</td><td>387.46 (n/a)</td><td>283.60 (n/a)</td><td>219.10 (n/a)</td><td>191.09 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (-4.31%)</td><td>0.05 (-15.73%)</td><td>0.06 (-1.43%)</td><td>0.03 <b>(-34.15%)</b></td><td>0.02 <b>(+47.40%)</b></td><td>634.10 <b>(+51.84%)</b></td><td>389.50 <b>(+30.23%)</b></td><td>296.90 (+1.47%)</td><td>240.30 (+4.52%)</td><td>168.28 <b>(+132.36%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>417.60 (n/a)</td><td>299.08 (n/a)</td><td>292.60 (n/a)</td><td>229.90 (n/a)</td><td>72.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (+8.76%)</td><td>0.06 (+8.87%)</td><td>0.06 (-4.39%)</td><td>0.03 (-10.29%)</td><td>0.02 (+2.58%)</td><td>552.10 (+11.47%)</td><td>320.04 (-7.34%)</td><td>288.80 (+4.60%)</td><td>219.90 (-8.07%)</td><td>133.10 (+9.74%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>495.30 (n/a)</td><td>345.40 (n/a)</td><td>276.10 (n/a)</td><td>239.20 (n/a)</td><td>121.28 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (+17.05%)</td><td>0.05 <b>(+24.41%)</b></td><td>0.06 <b>(+45.85%)</b></td><td>0.03 (-10.27%)</td><td>0.02 <b>(+76.23%)</b></td><td>569.90 (+11.44%)</td><td>369.80 (-11.89%)</td><td>285.60 <b>(-31.43%)</b></td><td>235.00 (-14.58%)</td><td>159.74 <b>(+71.05%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>511.40 (n/a)</td><td>419.72 (n/a)</td><td>416.50 (n/a)</td><td>275.10 (n/a)</td><td>93.39 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (+7.90%)</td><td>0.04 (+2.85%)</td><td>0.03 (-3.10%)</td><td>0.03 (-13.02%)</td><td>0.01 <b>(+53.09%)</b></td><td>596.20 (+14.96%)</td><td>460.46 (+2.81%)</td><td>529.10 (+3.20%)</td><td>291.70 (-7.31%)</td><td>149.12 <b>(+55.26%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>518.60 (n/a)</td><td>447.86 (n/a)</td><td>512.70 (n/a)</td><td>314.70 (n/a)</td><td>96.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 <b>(+31.93%)</b></td><td>0.05 (+15.47%)</td><td>0.04 (+2.24%)</td><td>0.03 <b>(+101.59%)</b></td><td>0.02 (+4.91%)</td><td>491.70 <b>(-50.39%)</b></td><td>372.26 <b>(-23.84%)</b></td><td>401.90 (-2.19%)</td><td>190.50 <b>(-24.22%)</b></td><td>125.13 <b>(-58.75%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>991.20 (n/a)</td><td>488.78 (n/a)</td><td>410.90 (n/a)</td><td>251.40 (n/a)</td><td>303.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 <b>(+36.04%)</b></td><td>0.05 <b>(+25.99%)</b></td><td>0.06 <b>(+45.54%)</b></td><td>0.03 (+0.62%)</td><td>0.02 <b>(+56.96%)</b></td><td>583.20 (-0.61%)</td><td>369.34 (-16.50%)</td><td>291.70 <b>(-31.28%)</b></td><td>232.90 <b>(-26.48%)</b></td><td>147.69 (+17.55%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>586.80 (n/a)</td><td>442.32 (n/a)</td><td>424.50 (n/a)</td><td>316.80 (n/a)</td><td>125.64 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 <b>(+22.93%)</b></td><td>0.04 (+4.83%)</td><td>0.04 (-19.54%)</td><td>0.03 (+3.00%)</td><td>0.01 (+10.21%)</td><td>594.70 (-2.91%)</td><td>410.54 (-5.74%)</td><td>421.50 <b>(+24.30%)</b></td><td>246.40 (-18.65%)</td><td>130.55 (-17.61%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>612.50 (n/a)</td><td>435.56 (n/a)</td><td>339.10 (n/a)</td><td>302.90 (n/a)</td><td>158.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (+4.28%)</td><td>0.04 (-0.34%)</td><td>0.03 <b>(-26.87%)</b></td><td>0.03 (+2.49%)</td><td>0.02 (+7.42%)</td><td>576.80 (-2.42%)</td><td>419.36 (+0.38%)</td><td>468.50 <b>(+36.75%)</b></td><td>243.70 (-4.09%)</td><td>139.70 (-7.02%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>591.10 (n/a)</td><td>417.78 (n/a)</td><td>342.60 (n/a)</td><td>254.10 (n/a)</td><td>150.23 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 <b>(+22.43%)</b></td><td>0.05 (+13.44%)</td><td>0.06 <b>(+54.53%)</b></td><td>0.03 <b>(+37.54%)</b></td><td>0.02 (+10.40%)</td><td>563.10 <b>(-27.29%)</b></td><td>378.62 (-13.46%)</td><td>294.00 <b>(-35.29%)</b></td><td>199.60 (-18.30%)</td><td>169.86 <b>(-21.35%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>774.40 (n/a)</td><td>437.52 (n/a)</td><td>454.30 (n/a)</td><td>244.30 (n/a)</td><td>215.97 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 <b>(+25.21%)</b></td><td>0.12 (-4.62%)</td><td>0.11 <b>(-20.25%)</b></td><td>0.07 (-11.50%)</td><td>0.05 <b>(+37.04%)</b></td><td>450.10 (+12.98%)</td><td>320.44 (+10.91%)</td><td>307.10 <b>(+25.40%)</b></td><td>159.20 <b>(-20.16%)</b></td><td>125.94 <b>(+25.36%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>398.40 (n/a)</td><td>288.92 (n/a)</td><td>244.90 (n/a)</td><td>199.40 (n/a)</td><td>100.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.15 (+11.99%)</td><td>0.11 (+7.15%)</td><td>0.12 (+0.23%)</td><td>0.05 <b>(-26.92%)</b></td><td>0.04 <b>(+26.19%)</b></td><td>624.70 <b>(+36.85%)</b></td><td>330.68 (-0.08%)</td><td>281.40 (-0.25%)</td><td>214.40 (-10.70%)</td><td>167.51 <b>(+63.32%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>456.50 (n/a)</td><td>330.96 (n/a)</td><td>282.10 (n/a)</td><td>240.10 (n/a)</td><td>102.57 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (+11.66%)</td><td>0.08 (-15.70%)</td><td>0.07 <b>(-38.34%)</b></td><td>0.02 <b>(-68.54%)</b></td><td>0.05 <b>(+46.92%)</b></td><td>1879.60 <b>(+217.88%)</b></td><td>685.72 <b>(+76.54%)</b></td><td>487.00 <b>(+62.17%)</b></td><td>229.80 (-10.44%)</td><td>679.34 <b>(+344.28%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>591.30 (n/a)</td><td>388.42 (n/a)</td><td>300.30 (n/a)</td><td>256.60 (n/a)</td><td>152.91 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (+14.06%)</td><td>0.09 (+6.49%)</td><td>0.07 (-4.26%)</td><td>0.03 <b>(-53.58%)</b></td><td>0.05 <b>(+91.94%)</b></td><td>1040.90 <b>(+115.42%)</b></td><td>497.16 (+19.52%)</td><td>465.70 (+4.44%)</td><td>226.20 (-12.33%)</td><td>328.04 <b>(+262.23%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>483.20 (n/a)</td><td>415.96 (n/a)</td><td>445.90 (n/a)</td><td>258.00 (n/a)</td><td>90.56 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.12 (-12.31%)</td><td>0.09 (-7.16%)</td><td>0.08 (+0.77%)</td><td>0.05 <b>(-21.97%)</b></td><td>0.03 (-8.65%)</td><td>601.60 <b>(+28.16%)</b></td><td>404.88 (+9.00%)</td><td>417.60 (-0.76%)</td><td>263.50 (+14.02%)</td><td>132.16 <b>(+31.01%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>469.40 (n/a)</td><td>371.46 (n/a)</td><td>420.80 (n/a)</td><td>231.10 (n/a)</td><td>100.87 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 <b>(+55.56%)</b></td><td>0.12 (+18.89%)</td><td>0.10 (+17.08%)</td><td>0.07 (+8.63%)</td><td>0.06 <b>(+66.72%)</b></td><td>497.40 (-7.94%)</td><td>333.52 (-9.86%)</td><td>321.50 (-14.61%)</td><td>154.80 <b>(-35.74%)</b></td><td>140.33 (+7.17%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>540.30 (n/a)</td><td>370.00 (n/a)</td><td>376.50 (n/a)</td><td>240.90 (n/a)</td><td>130.94 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 <b>(-32.65%)</b></td><td>0.09 <b>(-23.81%)</b></td><td>0.08 <b>(-28.71%)</b></td><td>0.06 (-5.85%)</td><td>0.03 <b>(-29.44%)</b></td><td>574.90 (+6.23%)</td><td>398.58 <b>(+27.40%)</b></td><td>391.50 <b>(+40.27%)</b></td><td>258.70 <b>(+48.51%)</b></td><td>141.71 (+2.45%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>541.20 (n/a)</td><td>312.86 (n/a)</td><td>279.10 (n/a)</td><td>174.20 (n/a)</td><td>138.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (-2.98%)</td><td>0.10 (+17.34%)</td><td>0.11 <b>(+58.98%)</b></td><td>0.06 (+3.06%)</td><td>0.03 (-4.84%)</td><td>563.40 (-2.96%)</td><td>357.82 (-16.00%)</td><td>310.20 <b>(-37.09%)</b></td><td>242.20 (+3.11%)</td><td>136.84 (-7.83%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>580.60 (n/a)</td><td>425.96 (n/a)</td><td>493.10 (n/a)</td><td>234.90 (n/a)</td><td>148.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (-8.48%)</td><td>0.12 <b>(+25.94%)</b></td><td>0.12 <b>(+47.60%)</b></td><td>0.11 <b>(+80.44%)</b></td><td>0.01 <b>(-68.37%)</b></td><td>303.20 <b>(-44.57%)</b></td><td>271.40 <b>(-28.77%)</b></td><td>269.80 <b>(-32.25%)</b></td><td>244.50 (+9.30%)</td><td>26.61 <b>(-80.67%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>547.00 (n/a)</td><td>381.04 (n/a)</td><td>398.20 (n/a)</td><td>223.70 (n/a)</td><td>137.66 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (-0.02%)</td><td>0.11 <b>(+27.54%)</b></td><td>0.12 (+6.11%)</td><td>0.08 <b>(+376.21%)</b></td><td>0.02 <b>(-47.46%)</b></td><td>393.60 <b>(-79.00%)</b></td><td>310.50 <b>(-52.42%)</b></td><td>279.50 (-5.77%)</td><td>244.70 (+0.00%)</td><td>73.96 <b>(-89.33%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1874.20 (n/a)</td><td>652.52 (n/a)</td><td>296.60 (n/a)</td><td>244.70 (n/a)</td><td>693.39 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.15 <b>(+20.98%)</b></td><td>0.10 <b>(+28.64%)</b></td><td>0.10 <b>(+51.85%)</b></td><td>0.06 <b>(+218.72%)</b></td><td>0.04 (-9.46%)</td><td>588.10 <b>(-68.63%)</b></td><td>386.96 <b>(-44.33%)</b></td><td>312.40 <b>(-34.15%)</b></td><td>223.60 (-17.34%)</td><td>157.02 <b>(-76.55%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1874.50 (n/a)</td><td>695.08 (n/a)</td><td>474.40 (n/a)</td><td>270.50 (n/a)</td><td>669.63 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (+10.17%)</td><td>0.08 (-7.84%)</td><td>0.06 <b>(-32.43%)</b></td><td>0.04 (-11.65%)</td><td>0.04 (+14.24%)</td><td>759.50 (+13.19%)</td><td>496.92 (+11.37%)</td><td>516.20 <b>(+47.99%)</b></td><td>247.70 (-9.23%)</td><td>203.67 (+9.90%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>671.00 (n/a)</td><td>446.18 (n/a)</td><td>348.80 (n/a)</td><td>272.90 (n/a)</td><td>185.32 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (+0.15%)</td><td>0.08 (+1.55%)</td><td>0.08 (+2.60%)</td><td>0.05 (-5.05%)</td><td>0.02 (+13.86%)</td><td>501.80 (+5.31%)</td><td>318.44 (+0.16%)</td><td>297.30 (-2.56%)</td><td>238.30 (-0.13%)</td><td>108.00 (+15.66%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>476.50 (n/a)</td><td>317.94 (n/a)</td><td>305.10 (n/a)</td><td>238.60 (n/a)</td><td>93.38 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.17 <b>(-21.77%)</b></td><td>0.14 (-10.23%)</td><td>0.15 (-16.77%)</td><td>0.09 <b>(+240.70%)</b></td><td>0.03 <b>(-55.47%)</b></td><td>563.40 <b>(-70.65%)</b></td><td>380.38 <b>(-36.61%)</b></td><td>338.40 <b>(+20.17%)</b></td><td>286.80 <b>(+27.81%)</b></td><td>110.51 <b>(-85.03%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1919.40 (n/a)</td><td>600.04 (n/a)</td><td>281.60 (n/a)</td><td>224.40 (n/a)</td><td>738.04 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>4.22 (+7.81%)</td><td>3.68 <b>(+21.36%)</b></td><td>4.00 <b>(+47.87%)</b></td><td>2.59 (+10.38%)</td><td>0.65 (-3.28%)</td><td>4052.20 (-9.41%)</td><td>2941.36 (-18.15%)</td><td>2620.20 <b>(-32.37%)</b></td><td>2484.10 (-7.24%)</td><td>642.39 (-15.18%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.92 (n/a)</td><td>3.03 (n/a)</td><td>2.71 (n/a)</td><td>2.34 (n/a)</td><td>0.68 (n/a)</td><td>4473.00 (n/a)</td><td>3593.54 (n/a)</td><td>3874.40 (n/a)</td><td>2678.10 (n/a)</td><td>757.38 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.15 <b>(-21.49%)</b></td><td>0.12 (+6.24%)</td><td>0.14 <b>(+41.98%)</b></td><td>0.07 <b>(+20.54%)</b></td><td>0.03 <b>(-34.43%)</b></td><td>599.80 (-17.04%)</td><td>362.46 (-13.04%)</td><td>289.80 <b>(-29.56%)</b></td><td>279.00 <b>(+27.34%)</b></td><td>136.07 <b>(-29.67%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>723.00 (n/a)</td><td>416.82 (n/a)</td><td>411.40 (n/a)</td><td>219.10 (n/a)</td><td>193.47 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-6.09%)</td><td>0.02 (-11.61%)</td><td>0.02 (+1.76%)</td><td>0.01 <b>(-60.53%)</b></td><td>0.01 <b>(+129.39%)</b></td><td>770.80 <b>(+153.39%)</b></td><td>370.60 <b>(+34.24%)</b></td><td>287.80 (-1.74%)</td><td>237.70 (+6.45%)</td><td>225.30 <b>(+560.76%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>304.20 (n/a)</td><td>276.08 (n/a)</td><td>292.90 (n/a)</td><td>223.30 (n/a)</td><td>34.10 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (+9.77%)</td><td>0.02 (+10.04%)</td><td>0.01 (-1.20%)</td><td>0.01 <b>(+70.04%)</b></td><td>0.00 <b>(-41.51%)</b></td><td>295.30 <b>(-41.20%)</b></td><td>269.12 (-14.15%)</td><td>278.30 (+1.24%)</td><td>216.50 (-8.92%)</td><td>30.74 <b>(-71.30%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>502.20 (n/a)</td><td>313.46 (n/a)</td><td>274.90 (n/a)</td><td>237.70 (n/a)</td><td>107.08 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 <b>(-32.02%)</b></td><td>0.01 <b>(-23.25%)</b></td><td>0.02 (-17.15%)</td><td>0.01 <b>(-37.22%)</b></td><td>0.00 <b>(-29.05%)</b></td><td>1023.50 <b>(+59.30%)</b></td><td>521.34 <b>(+33.96%)</b></td><td>404.30 <b>(+20.69%)</b></td><td>333.90 <b>(+47.09%)</b></td><td>287.70 <b>(+70.76%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>642.50 (n/a)</td><td>389.18 (n/a)</td><td>335.00 (n/a)</td><td>227.00 (n/a)</td><td>168.48 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-0.97%)</td><td>0.01 <b>(+27.69%)</b></td><td>0.02 <b>(+137.46%)</b></td><td>0.01 <b>(+24.07%)</b></td><td>0.01 (-2.48%)</td><td>543.40 (-19.39%)</td><td>356.48 <b>(-24.40%)</b></td><td>242.30 <b>(-57.88%)</b></td><td>224.90 (+0.99%)</td><td>166.68 (-18.56%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>674.10 (n/a)</td><td>471.54 (n/a)</td><td>575.30 (n/a)</td><td>222.70 (n/a)</td><td>204.65 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (+12.85%)</td><td>0.01 (-5.52%)</td><td>0.02 (-9.90%)</td><td>0.01 (-16.04%)</td><td>0.01 <b>(+37.15%)</b></td><td>665.80 (+19.11%)</td><td>395.20 (+13.15%)</td><td>318.30 (+10.98%)</td><td>238.30 (-11.38%)</td><td>177.41 <b>(+44.95%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.00 (n/a)</td><td>349.28 (n/a)</td><td>286.80 (n/a)</td><td>268.90 (n/a)</td><td>122.39 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 <b>(+23.82%)</b></td><td>0.01 (+13.85%)</td><td>0.01 (+17.35%)</td><td>0.01 (-4.90%)</td><td>0.01 <b>(+29.42%)</b></td><td>552.40 (+5.16%)</td><td>381.32 (-9.26%)</td><td>444.20 (-14.79%)</td><td>206.70 (-19.23%)</td><td>146.75 (+4.00%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.30 (n/a)</td><td>420.22 (n/a)</td><td>521.30 (n/a)</td><td>255.90 (n/a)</td><td>141.10 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 <b>(+43.20%)</b></td><td>0.01 (+15.10%)</td><td>0.01 (-13.67%)</td><td>0.01 (-17.27%)</td><td>0.01 <b>(+230.53%)</b></td><td>617.00 <b>(+20.89%)</b></td><td>421.60 (-0.43%)</td><td>483.00 (+15.83%)</td><td>237.40 <b>(-30.18%)</b></td><td>170.82 <b>(+159.91%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.40 (n/a)</td><td>423.40 (n/a)</td><td>417.00 (n/a)</td><td>340.00 (n/a)</td><td>65.72 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (-14.27%)</td><td>0.01 <b>(-28.81%)</b></td><td>0.01 <b>(-27.89%)</b></td><td>0.00 <b>(-57.91%)</b></td><td>0.00 <b>(+46.87%)</b></td><td>999.40 <b>(+137.56%)</b></td><td>517.02 <b>(+63.40%)</b></td><td>444.10 <b>(+38.65%)</b></td><td>279.60 (+16.65%)</td><td>283.90 <b>(+322.58%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>420.70 (n/a)</td><td>316.42 (n/a)</td><td>320.30 (n/a)</td><td>239.70 (n/a)</td><td>67.18 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-11.80%)</td><td>0.01 (-1.98%)</td><td>0.01 <b>(+30.69%)</b></td><td>0.01 (-11.31%)</td><td>0.00 (-15.17%)</td><td>639.50 (+12.75%)</td><td>405.44 (+1.17%)</td><td>346.90 <b>(-23.49%)</b></td><td>266.90 (+13.38%)</td><td>158.71 (+10.13%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.20 (n/a)</td><td>400.76 (n/a)</td><td>453.40 (n/a)</td><td>235.40 (n/a)</td><td>144.11 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 <b>(+25.54%)</b></td><td>0.01 (-6.04%)</td><td>0.01 (-18.80%)</td><td>0.01 (-14.97%)</td><td>0.00 <b>(+89.87%)</b></td><td>639.70 (+17.61%)</td><td>476.08 (+15.56%)</td><td>494.60 <b>(+23.16%)</b></td><td>230.40 <b>(-20.36%)</b></td><td>151.50 <b>(+65.99%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>543.90 (n/a)</td><td>411.96 (n/a)</td><td>401.60 (n/a)</td><td>289.30 (n/a)</td><td>91.27 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-0.20%)</td><td>0.01 (-11.70%)</td><td>0.01 <b>(-22.85%)</b></td><td>0.01 (-10.76%)</td><td>0.00 <b>(+24.35%)</b></td><td>565.10 (+12.06%)</td><td>417.12 (+18.66%)</td><td>444.70 <b>(+29.61%)</b></td><td>256.30 (+0.20%)</td><td>144.53 <b>(+42.31%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>504.30 (n/a)</td><td>351.54 (n/a)</td><td>343.10 (n/a)</td><td>255.80 (n/a)</td><td>101.56 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (+6.06%)</td><td>0.01 (+6.07%)</td><td>0.01 (-0.40%)</td><td>0.01 <b>(+23.24%)</b></td><td>0.00 (-1.14%)</td><td>491.10 (-18.85%)</td><td>423.00 (-7.04%)</td><td>450.00 (+0.40%)</td><td>271.90 (-5.72%)</td><td>86.27 <b>(-25.19%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>605.20 (n/a)</td><td>455.02 (n/a)</td><td>448.20 (n/a)</td><td>288.40 (n/a)</td><td>115.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (+1.91%)</td><td>0.03 <b>(+28.96%)</b></td><td>0.03 <b>(+44.91%)</b></td><td>0.03 <b>(+81.97%)</b></td><td>0.00 <b>(-67.56%)</b></td><td>286.50 <b>(-45.05%)</b></td><td>261.66 <b>(-29.45%)</b></td><td>265.10 <b>(-31.00%)</b></td><td>236.90 (-1.86%)</td><td>23.21 <b>(-81.64%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>521.40 (n/a)</td><td>370.86 (n/a)</td><td>384.20 (n/a)</td><td>241.40 (n/a)</td><td>126.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (+6.01%)</td><td>0.03 (+9.89%)</td><td>0.03 <b>(+38.62%)</b></td><td>0.02 (+5.33%)</td><td>0.01 (+3.42%)</td><td>558.60 (-5.06%)</td><td>398.78 (-9.17%)</td><td>379.70 <b>(-27.87%)</b></td><td>238.40 (-5.66%)</td><td>146.93 (-3.89%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>588.40 (n/a)</td><td>439.06 (n/a)</td><td>526.40 (n/a)</td><td>252.70 (n/a)</td><td>152.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (+0.38%)</td><td>0.03 <b>(+33.97%)</b></td><td>0.03 <b>(+68.93%)</b></td><td>0.01 (+11.87%)</td><td>0.01 (+7.73%)</td><td>623.20 (-10.60%)</td><td>377.20 <b>(-23.77%)</b></td><td>301.60 <b>(-40.80%)</b></td><td>217.40 (-0.41%)</td><td>181.72 (+4.44%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>697.10 (n/a)</td><td>494.80 (n/a)</td><td>509.50 (n/a)</td><td>218.30 (n/a)</td><td>174.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 <b>(-20.19%)</b></td><td>0.02 (-15.76%)</td><td>0.02 (-3.84%)</td><td>0.01 <b>(-70.25%)</b></td><td>0.01 (+0.24%)</td><td>1885.40 <b>(+236.14%)</b></td><td>711.76 <b>(+61.00%)</b></td><td>476.30 (+4.00%)</td><td>288.60 <b>(+25.31%)</b></td><td>660.85 <b>(+420.07%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>560.90 (n/a)</td><td>442.10 (n/a)</td><td>458.00 (n/a)</td><td>230.30 (n/a)</td><td>127.07 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 <b>(-34.40%)</b></td><td>0.02 (-12.33%)</td><td>0.02 (-11.18%)</td><td>0.01 <b>(+80.37%)</b></td><td>0.01 <b>(-53.18%)</b></td><td>592.60 <b>(-44.56%)</b></td><td>413.84 (-14.75%)</td><td>350.80 (+12.62%)</td><td>282.50 <b>(+52.46%)</b></td><td>141.34 <b>(-61.01%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1068.90 (n/a)</td><td>485.42 (n/a)</td><td>311.50 (n/a)</td><td>185.30 (n/a)</td><td>362.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (+1.08%)</td><td>0.03 (-3.55%)</td><td>0.02 (-14.71%)</td><td>0.02 <b>(-21.27%)</b></td><td>0.01 <b>(+45.34%)</b></td><td>604.50 <b>(+27.00%)</b></td><td>393.12 (+10.34%)</td><td>422.20 (+17.25%)</td><td>251.30 (-1.06%)</td><td>143.90 <b>(+73.62%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.00 (n/a)</td><td>356.28 (n/a)</td><td>360.10 (n/a)</td><td>254.00 (n/a)</td><td>82.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (-2.98%)</td><td>0.02 (-3.76%)</td><td>0.02 <b>(+26.93%)</b></td><td>0.01 <b>(+46.79%)</b></td><td>0.01 <b>(-35.00%)</b></td><td>548.00 <b>(-31.87%)</b></td><td>416.62 (-12.20%)</td><td>437.30 <b>(-21.22%)</b></td><td>229.80 (+3.05%)</td><td>115.71 <b>(-53.00%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>804.40 (n/a)</td><td>474.52 (n/a)</td><td>555.10 (n/a)</td><td>223.00 (n/a)</td><td>246.19 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 <b>(-41.51%)</b></td><td>0.02 (-14.75%)</td><td>0.02 (+8.17%)</td><td>0.02 <b>(+38.72%)</b></td><td>0.00 <b>(-81.29%)</b></td><td>459.60 <b>(-27.92%)</b></td><td>426.64 (+1.33%)</td><td>428.90 (-7.54%)</td><td>361.70 <b>(+70.94%)</b></td><td>39.91 <b>(-76.40%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.60 (n/a)</td><td>421.06 (n/a)</td><td>463.90 (n/a)</td><td>211.60 (n/a)</td><td>169.06 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (+8.46%)</td><td>0.02 (+15.89%)</td><td>0.02 (+16.30%)</td><td>0.01 (+10.86%)</td><td>0.01 (+6.53%)</td><td>564.00 (-9.79%)</td><td>429.32 (-13.74%)</td><td>461.20 (-14.02%)</td><td>239.00 (-7.79%)</td><td>132.29 (-5.30%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>625.20 (n/a)</td><td>497.72 (n/a)</td><td>536.40 (n/a)</td><td>259.20 (n/a)</td><td>139.69 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (-16.79%)</td><td>0.02 <b>(-22.21%)</b></td><td>0.02 <b>(-20.87%)</b></td><td>0.00 <b>(-70.88%)</b></td><td>0.01 (+15.98%)</td><td>1866.20 <b>(+243.43%)</b></td><td>680.34 <b>(+88.49%)</b></td><td>485.40 <b>(+26.37%)</b></td><td>254.70 <b>(+20.14%)</b></td><td>674.28 <b>(+400.44%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.40 (n/a)</td><td>360.94 (n/a)</td><td>384.10 (n/a)</td><td>212.00 (n/a)</td><td>134.74 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (-6.53%)</td><td>0.02 <b>(-23.44%)</b></td><td>0.02 <b>(-25.06%)</b></td><td>0.01 <b>(-38.91%)</b></td><td>0.01 (-1.17%)</td><td>1313.00 <b>(+63.67%)</b></td><td>616.36 <b>(+43.21%)</b></td><td>491.50 <b>(+33.45%)</b></td><td>285.20 (+6.98%)</td><td>400.33 <b>(+84.33%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>802.20 (n/a)</td><td>430.38 (n/a)</td><td>368.30 (n/a)</td><td>266.60 (n/a)</td><td>217.18 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (-13.65%)</td><td>0.05 <b>(-22.55%)</b></td><td>0.04 <b>(-35.23%)</b></td><td>0.03 (+2.07%)</td><td>0.02 (-9.21%)</td><td>514.70 (-2.04%)</td><td>395.96 <b>(+28.35%)</b></td><td>426.30 <b>(+54.40%)</b></td><td>240.80 (+15.82%)</td><td>127.94 (+1.23%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>525.40 (n/a)</td><td>308.50 (n/a)</td><td>276.10 (n/a)</td><td>207.90 (n/a)</td><td>126.39 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 <b>(-43.91%)</b></td><td>0.04 <b>(-52.32%)</b></td><td>0.04 <b>(-51.36%)</b></td><td>0.01 <b>(-72.50%)</b></td><td>0.02 <b>(-23.65%)</b></td><td>1911.80 <b>(+263.60%)</b></td><td>912.58 <b>(+153.02%)</b></td><td>682.40 <b>(+105.60%)</b></td><td>446.50 <b>(+78.31%)</b></td><td>599.33 <b>(+410.51%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>525.80 (n/a)</td><td>360.68 (n/a)</td><td>331.90 (n/a)</td><td>250.40 (n/a)</td><td>117.40 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 <b>(-21.91%)</b></td><td>0.05 (+6.22%)</td><td>0.06 <b>(+52.77%)</b></td><td>0.03 (+17.56%)</td><td>0.01 <b>(-38.25%)</b></td><td>486.60 (-14.93%)</td><td>360.26 (-12.79%)</td><td>296.30 <b>(-34.55%)</b></td><td>266.60 <b>(+28.05%)</b></td><td>104.72 <b>(-31.31%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>572.00 (n/a)</td><td>413.10 (n/a)</td><td>452.70 (n/a)</td><td>208.20 (n/a)</td><td>152.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (+3.13%)</td><td>0.06 (+5.19%)</td><td>0.07 (+1.77%)</td><td>0.04 (+13.59%)</td><td>0.02 (+10.21%)</td><td>519.10 (-11.96%)</td><td>356.36 (-4.30%)</td><td>278.50 (-1.76%)</td><td>240.40 (-3.03%)</td><td>140.89 (-4.52%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>589.60 (n/a)</td><td>372.38 (n/a)</td><td>283.50 (n/a)</td><td>247.90 (n/a)</td><td>147.56 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 <b>(+21.94%)</b></td><td>0.04 <b>(+20.51%)</b></td><td>0.04 (+12.93%)</td><td>0.03 (+11.52%)</td><td>0.02 <b>(+29.27%)</b></td><td>614.00 (-10.33%)</td><td>421.92 (-15.49%)</td><td>437.90 (-11.45%)</td><td>236.80 (-17.98%)</td><td>139.94 (-3.78%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>684.70 (n/a)</td><td>499.24 (n/a)</td><td>494.50 (n/a)</td><td>288.70 (n/a)</td><td>145.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (-9.11%)</td><td>0.05 <b>(-23.40%)</b></td><td>0.05 <b>(-33.48%)</b></td><td>0.04 (-14.80%)</td><td>0.01 (-13.90%)</td><td>524.60 (+17.36%)</td><td>429.50 <b>(+30.16%)</b></td><td>451.50 <b>(+50.35%)</b></td><td>272.70 (+10.00%)</td><td>100.53 (+10.96%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>447.00 (n/a)</td><td>329.98 (n/a)</td><td>300.30 (n/a)</td><td>247.90 (n/a)</td><td>90.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (-6.77%)</td><td>0.04 (-12.65%)</td><td>0.04 (-11.15%)</td><td>0.02 <b>(-32.04%)</b></td><td>0.01 (+13.07%)</td><td>772.60 <b>(+47.16%)</b></td><td>463.92 <b>(+21.38%)</b></td><td>368.40 (+12.52%)</td><td>283.50 (+7.26%)</td><td>195.62 <b>(+78.21%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>525.00 (n/a)</td><td>382.22 (n/a)</td><td>327.40 (n/a)</td><td>264.30 (n/a)</td><td>109.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (-3.91%)</td><td>0.05 (-3.95%)</td><td>0.06 (-12.11%)</td><td>0.03 (+13.91%)</td><td>0.01 <b>(-22.02%)</b></td><td>569.80 (-12.22%)</td><td>378.24 (-1.20%)</td><td>317.00 (+13.78%)</td><td>274.60 (+4.05%)</td><td>125.59 <b>(-25.91%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>649.10 (n/a)</td><td>382.82 (n/a)</td><td>278.60 (n/a)</td><td>263.90 (n/a)</td><td>169.52 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (+0.11%)</td><td>0.04 (+1.39%)</td><td>0.03 (-4.84%)</td><td>0.03 (+5.80%)</td><td>0.02 (+5.58%)</td><td>577.80 (-5.50%)</td><td>439.20 (-0.16%)</td><td>512.90 (+5.08%)</td><td>241.10 (-0.08%)</td><td>162.64 (+3.43%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.40 (n/a)</td><td>439.90 (n/a)</td><td>488.10 (n/a)</td><td>241.30 (n/a)</td><td>157.24 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (+9.47%)</td><td>0.05 (-10.46%)</td><td>0.04 <b>(-32.44%)</b></td><td>0.04 <b>(-20.61%)</b></td><td>0.02 <b>(+107.68%)</b></td><td>490.90 <b>(+25.97%)</b></td><td>380.44 (+19.02%)</td><td>439.30 <b>(+48.01%)</b></td><td>252.80 (-8.67%)</td><td>112.82 <b>(+132.97%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>389.70 (n/a)</td><td>319.64 (n/a)</td><td>296.80 (n/a)</td><td>276.80 (n/a)</td><td>48.43 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (-19.21%)</td><td>0.03 <b>(-28.66%)</b></td><td>0.03 <b>(-38.40%)</b></td><td>0.02 (-13.28%)</td><td>0.01 <b>(-33.67%)</b></td><td>728.60 (+15.30%)</td><td>562.92 <b>(+35.52%)</b></td><td>579.10 <b>(+62.35%)</b></td><td>360.30 <b>(+23.77%)</b></td><td>134.48 (-7.68%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>631.90 (n/a)</td><td>415.38 (n/a)</td><td>356.70 (n/a)</td><td>291.10 (n/a)</td><td>145.67 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (+5.37%)</td><td>0.09 (-7.75%)</td><td>0.10 (-5.49%)</td><td>0.05 (-17.86%)</td><td>0.04 <b>(+28.96%)</b></td><td>612.40 <b>(+21.75%)</b></td><td>415.88 (+16.67%)</td><td>315.80 (+5.80%)</td><td>238.40 (-5.13%)</td><td>181.34 <b>(+61.23%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>503.00 (n/a)</td><td>356.46 (n/a)</td><td>298.50 (n/a)</td><td>251.30 (n/a)</td><td>112.47 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.16 <b>(+43.65%)</b></td><td>0.10 (-1.01%)</td><td>0.12 (+3.98%)</td><td>0.05 <b>(-23.88%)</b></td><td>0.05 <b>(+155.16%)</b></td><td>601.90 <b>(+31.36%)</b></td><td>383.60 (+17.09%)</td><td>283.30 (-3.84%)</td><td>200.00 <b>(-30.41%)</b></td><td>181.73 <b>(+147.72%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>458.20 (n/a)</td><td>327.60 (n/a)</td><td>294.60 (n/a)</td><td>287.40 (n/a)</td><td>73.36 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (-12.72%)</td><td>0.10 (+5.53%)</td><td>0.09 (-5.55%)</td><td>0.06 <b>(+192.51%)</b></td><td>0.03 <b>(-43.76%)</b></td><td>666.70 <b>(-65.81%)</b></td><td>448.98 <b>(-37.31%)</b></td><td>459.40 (+5.88%)</td><td>313.60 (+14.58%)</td><td>143.94 <b>(-79.54%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1950.10 (n/a)</td><td>716.18 (n/a)</td><td>433.90 (n/a)</td><td>273.70 (n/a)</td><td>703.50 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 <b>(+21.93%)</b></td><td>0.09 (+5.40%)</td><td>0.09 (-15.49%)</td><td>0.05 (-4.42%)</td><td>0.04 (+19.62%)</td><td>617.00 (+4.63%)</td><td>398.88 (-3.82%)</td><td>366.30 (+18.31%)</td><td>229.10 (-18.00%)</td><td>156.78 (-2.03%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>589.70 (n/a)</td><td>414.72 (n/a)</td><td>309.60 (n/a)</td><td>279.40 (n/a)</td><td>160.02 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.17 (-9.91%)</td><td>0.13 (-6.69%)</td><td>0.13 (-19.12%)</td><td>0.09 (+13.98%)</td><td>0.04 <b>(-20.37%)</b></td><td>475.90 (-12.28%)</td><td>351.96 (+2.49%)</td><td>322.40 <b>(+23.62%)</b></td><td>239.30 (+10.99%)</td><td>111.42 <b>(-21.52%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>542.50 (n/a)</td><td>343.40 (n/a)</td><td>260.80 (n/a)</td><td>215.60 (n/a)</td><td>141.97 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (-16.01%)</td><td>0.09 (-12.63%)</td><td>0.06 <b>(-26.64%)</b></td><td>0.05 (-3.59%)</td><td>0.04 (-10.20%)</td><td>645.70 (+3.73%)</td><td>440.36 (+15.03%)</td><td>505.20 <b>(+36.32%)</b></td><td>231.90 (+19.05%)</td><td>175.56 (+9.49%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>622.50 (n/a)</td><td>382.82 (n/a)</td><td>370.60 (n/a)</td><td>194.80 (n/a)</td><td>160.34 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.22 <b>(+41.82%)</b></td><td>0.12 (+18.97%)</td><td>0.08 (+1.71%)</td><td>0.07 (+16.18%)</td><td>0.06 <b>(+61.10%)</b></td><td>493.60 (-13.92%)</td><td>371.56 (-9.57%)</td><td>459.00 (-1.69%)</td><td>171.20 <b>(-29.46%)</b></td><td>153.07 (+6.94%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>573.40 (n/a)</td><td>410.88 (n/a)</td><td>466.90 (n/a)</td><td>242.70 (n/a)</td><td>143.14 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (+9.65%)</td><td>0.09 (+11.07%)</td><td>0.11 <b>(+47.93%)</b></td><td>0.04 <b>(-26.91%)</b></td><td>0.04 <b>(+28.32%)</b></td><td>837.40 <b>(+36.81%)</b></td><td>427.46 (-0.48%)</td><td>289.00 <b>(-32.40%)</b></td><td>251.10 (-8.79%)</td><td>248.17 <b>(+63.85%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>612.10 (n/a)</td><td>429.52 (n/a)</td><td>427.50 (n/a)</td><td>275.30 (n/a)</td><td>151.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.18 (+18.72%)</td><td>0.10 (-2.43%)</td><td>0.07 <b>(-27.58%)</b></td><td>0.06 (-1.42%)</td><td>0.05 <b>(+31.64%)</b></td><td>584.50 (+1.44%)</td><td>423.60 (+6.76%)</td><td>495.80 <b>(+38.07%)</b></td><td>208.10 (-15.78%)</td><td>155.30 (+9.41%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>576.20 (n/a)</td><td>396.76 (n/a)</td><td>359.10 (n/a)</td><td>247.10 (n/a)</td><td>141.95 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.11 (-15.11%)</td><td>0.08 (-8.34%)</td><td>0.07 (-0.82%)</td><td>0.04 (-18.16%)</td><td>0.03 (-18.90%)</td><td>752.20 <b>(+22.19%)</b></td><td>476.42 (+8.35%)</td><td>473.20 (+0.83%)</td><td>303.30 (+17.83%)</td><td>175.87 (+17.02%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>615.60 (n/a)</td><td>439.72 (n/a)</td><td>469.30 (n/a)</td><td>257.40 (n/a)</td><td>150.28 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (-14.07%)</td><td>0.06 (-4.66%)</td><td>0.06 <b>(+31.21%)</b></td><td>0.04 (-4.53%)</td><td>0.02 <b>(-22.61%)</b></td><td>554.30 (+4.74%)</td><td>400.14 (+2.56%)</td><td>334.50 <b>(-23.79%)</b></td><td>287.90 (+16.37%)</td><td>132.28 (+0.38%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>529.20 (n/a)</td><td>390.14 (n/a)</td><td>438.90 (n/a)</td><td>247.40 (n/a)</td><td>131.78 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (-5.04%)</td><td>0.06 <b>(+25.00%)</b></td><td>0.05 <b>(+27.10%)</b></td><td>0.04 <b>(+101.89%)</b></td><td>0.02 <b>(-21.85%)</b></td><td>568.70 <b>(-50.47%)</b></td><td>401.60 <b>(-31.33%)</b></td><td>384.60 <b>(-21.32%)</b></td><td>255.50 (+5.32%)</td><td>136.86 <b>(-59.87%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1148.20 (n/a)</td><td>584.84 (n/a)</td><td>488.80 (n/a)</td><td>242.60 (n/a)</td><td>341.07 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (-17.98%)</td><td>0.05 <b>(-23.57%)</b></td><td>0.04 <b>(-39.11%)</b></td><td>0.04 (+15.18%)</td><td>0.01 <b>(-40.62%)</b></td><td>507.30 (-13.18%)</td><td>438.94 <b>(+23.16%)</b></td><td>496.50 <b>(+64.24%)</b></td><td>301.50 <b>(+21.92%)</b></td><td>91.19 <b>(-34.94%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>584.30 (n/a)</td><td>356.40 (n/a)</td><td>302.30 (n/a)</td><td>247.30 (n/a)</td><td>140.15 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (-13.28%)</td><td>0.05 (-3.68%)</td><td>0.05 (+6.43%)</td><td>0.03 (-8.51%)</td><td>0.02 (-7.99%)</td><td>631.20 (+9.30%)</td><td>425.46 (+4.07%)</td><td>385.30 (-6.05%)</td><td>266.70 (+15.35%)</td><td>171.25 (+10.27%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.50 (n/a)</td><td>408.84 (n/a)</td><td>410.10 (n/a)</td><td>231.20 (n/a)</td><td>155.31 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 <b>(-25.60%)</b></td><td>0.06 (-15.04%)</td><td>0.05 <b>(-37.23%)</b></td><td>0.04 <b>(+26.71%)</b></td><td>0.02 <b>(-45.45%)</b></td><td>503.60 <b>(-21.08%)</b></td><td>397.32 (+1.20%)</td><td>424.10 <b>(+59.32%)</b></td><td>273.80 <b>(+34.41%)</b></td><td>111.92 <b>(-46.87%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>638.10 (n/a)</td><td>392.62 (n/a)</td><td>266.20 (n/a)</td><td>203.70 (n/a)</td><td>210.65 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 <b>(-38.03%)</b></td><td>0.05 <b>(-21.43%)</b></td><td>0.04 <b>(-20.96%)</b></td><td>0.03 (-7.07%)</td><td>0.02 <b>(-47.04%)</b></td><td>610.50 (+7.62%)</td><td>421.48 (+15.23%)</td><td>459.70 <b>(+26.53%)</b></td><td>243.70 <b>(+61.39%)</b></td><td>149.87 (-8.71%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>567.30 (n/a)</td><td>365.76 (n/a)</td><td>363.30 (n/a)</td><td>151.00 (n/a)</td><td>164.16 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (+6.68%)</td><td>0.08 (-10.24%)</td><td>0.08 (-9.75%)</td><td>0.05 (-7.60%)</td><td>0.03 <b>(+22.51%)</b></td><td>466.20 (+8.24%)</td><td>332.18 (+16.07%)</td><td>305.40 (+10.81%)</td><td>195.60 (-6.28%)</td><td>119.69 <b>(+33.02%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>430.70 (n/a)</td><td>286.18 (n/a)</td><td>275.60 (n/a)</td><td>208.70 (n/a)</td><td>89.98 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (-4.25%)</td><td>0.08 (-5.46%)</td><td>0.08 (-7.05%)</td><td>0.05 (+1.18%)</td><td>0.01 (-16.86%)</td><td>454.30 (-1.15%)</td><td>330.90 (+4.62%)</td><td>306.90 (+7.57%)</td><td>279.90 (+4.44%)</td><td>69.99 (-13.17%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>459.60 (n/a)</td><td>316.28 (n/a)</td><td>285.30 (n/a)</td><td>268.00 (n/a)</td><td>80.61 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (-3.74%)</td><td>0.07 (+3.73%)</td><td>0.09 <b>(+75.00%)</b></td><td>0.01 <b>(-73.11%)</b></td><td>0.04 <b>(+45.17%)</b></td><td>1968.00 <b>(+271.95%)</b></td><td>652.54 <b>(+56.25%)</b></td><td>288.50 <b>(-42.85%)</b></td><td>256.40 (+3.89%)</td><td>741.89 <b>(+442.30%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>529.10 (n/a)</td><td>417.62 (n/a)</td><td>504.80 (n/a)</td><td>246.80 (n/a)</td><td>136.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (-6.66%)</td><td>0.06 (-13.81%)</td><td>0.06 <b>(-33.05%)</b></td><td>0.04 (-8.35%)</td><td>0.02 <b>(-31.90%)</b></td><td>559.70 (+9.12%)</td><td>400.18 (+11.41%)</td><td>403.70 <b>(+49.35%)</b></td><td>282.80 (+7.12%)</td><td>102.54 (-18.40%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>512.90 (n/a)</td><td>359.18 (n/a)</td><td>270.30 (n/a)</td><td>264.00 (n/a)</td><td>125.66 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 <b>(+20.82%)</b></td><td>0.06 <b>(+20.20%)</b></td><td>0.04 (-7.02%)</td><td>0.04 (-2.25%)</td><td>0.03 <b>(+79.07%)</b></td><td>621.10 (+2.29%)</td><td>464.08 (-7.30%)</td><td>573.00 (+7.55%)</td><td>249.00 (-17.22%)</td><td>191.73 <b>(+53.59%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>607.20 (n/a)</td><td>500.64 (n/a)</td><td>532.80 (n/a)</td><td>300.80 (n/a)</td><td>124.83 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (+4.46%)</td><td>0.08 (+14.99%)</td><td>0.08 (-1.03%)</td><td>0.06 <b>(+63.36%)</b></td><td>0.01 <b>(-49.64%)</b></td><td>419.10 <b>(-38.78%)</b></td><td>325.42 <b>(-22.64%)</b></td><td>302.00 (+1.04%)</td><td>268.10 (-4.28%)</td><td>58.64 <b>(-68.66%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>684.60 (n/a)</td><td>420.64 (n/a)</td><td>298.90 (n/a)</td><td>280.10 (n/a)</td><td>187.12 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (-12.08%)</td><td>0.07 (+10.24%)</td><td>0.07 (+9.64%)</td><td>0.04 <b>(+299.27%)</b></td><td>0.02 <b>(-48.88%)</b></td><td>470.50 <b>(-74.95%)</b></td><td>295.84 <b>(-51.47%)</b></td><td>272.20 (-8.78%)</td><td>192.70 (+13.75%)</td><td>104.57 <b>(-85.49%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1878.60 (n/a)</td><td>609.66 (n/a)</td><td>298.40 (n/a)</td><td>169.40 (n/a)</td><td>720.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 <b>(+41.34%)</b></td><td>0.07 <b>(+39.42%)</b></td><td>0.06 <b>(+30.02%)</b></td><td>0.06 <b>(+62.17%)</b></td><td>0.01 (+1.47%)</td><td>300.10 <b>(-38.34%)</b></td><td>273.98 <b>(-29.66%)</b></td><td>295.00 <b>(-23.10%)</b></td><td>214.30 <b>(-29.25%)</b></td><td>36.75 <b>(-55.31%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>486.70 (n/a)</td><td>389.52 (n/a)</td><td>383.60 (n/a)</td><td>302.90 (n/a)</td><td>82.23 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (-1.69%)</td><td>0.06 (-2.91%)</td><td>0.06 (-2.04%)</td><td>0.05 (+18.82%)</td><td>0.01 <b>(-29.03%)</b></td><td>391.90 (-15.83%)</td><td>322.82 (-0.77%)</td><td>305.70 (+2.07%)</td><td>238.80 (+1.75%)</td><td>62.20 <b>(-36.82%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>465.60 (n/a)</td><td>325.34 (n/a)</td><td>299.50 (n/a)</td><td>234.70 (n/a)</td><td>98.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (+7.36%)</td><td>0.05 <b>(+27.59%)</b></td><td>0.06 <b>(+42.93%)</b></td><td>0.04 <b>(+78.21%)</b></td><td>0.01 (-17.69%)</td><td>436.30 <b>(-43.88%)</b></td><td>350.58 <b>(-26.31%)</b></td><td>305.00 <b>(-30.03%)</b></td><td>286.60 (-6.86%)</td><td>77.78 <b>(-57.46%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>777.40 (n/a)</td><td>475.78 (n/a)</td><td>435.90 (n/a)</td><td>307.70 (n/a)</td><td>182.85 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 <b>(+56.56%)</b></td><td>0.06 <b>(+26.54%)</b></td><td>0.06 <b>(+28.72%)</b></td><td>0.03 (+8.44%)</td><td>0.03 <b>(+76.99%)</b></td><td>538.70 (-7.77%)</td><td>359.54 (-15.29%)</td><td>305.50 <b>(-22.30%)</b></td><td>182.90 <b>(-36.12%)</b></td><td>152.18 (+9.01%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>584.10 (n/a)</td><td>424.44 (n/a)</td><td>393.20 (n/a)</td><td>286.30 (n/a)</td><td>139.60 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (-15.92%)</td><td>0.05 (+0.22%)</td><td>0.05 <b>(+26.14%)</b></td><td>0.02 <b>(-45.06%)</b></td><td>0.02 (-12.07%)</td><td>1079.50 <b>(+82.01%)</b></td><td>497.32 (+10.78%)</td><td>372.50 <b>(-20.71%)</b></td><td>251.30 (+18.93%)</td><td>331.58 <b>(+127.61%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>593.10 (n/a)</td><td>448.94 (n/a)</td><td>469.80 (n/a)</td><td>211.30 (n/a)</td><td>145.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.35 (-9.72%)</td><td>0.24 (+0.69%)</td><td>0.21 (-5.13%)</td><td>0.17 (+2.37%)</td><td>0.08 (-6.98%)</td><td>588.00 (-2.31%)</td><td>436.38 (-0.62%)</td><td>470.40 (+5.42%)</td><td>279.30 (+10.75%)</td><td>131.48 (+5.64%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.39 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>601.90 (n/a)</td><td>439.10 (n/a)</td><td>446.20 (n/a)</td><td>252.20 (n/a)</td><td>124.46 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.23 <b>(-40.36%)</b></td><td>0.15 <b>(-45.26%)</b></td><td>0.17 <b>(-36.22%)</b></td><td>0.05 <b>(-73.78%)</b></td><td>0.08 (-5.04%)</td><td>1944.90 <b>(+281.43%)</b></td><td>891.58 <b>(+134.69%)</b></td><td>583.40 <b>(+56.83%)</b></td><td>419.30 <b>(+67.65%)</b></td><td>637.93 <b>(+498.14%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.39 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>509.90 (n/a)</td><td>379.90 (n/a)</td><td>372.00 (n/a)</td><td>250.10 (n/a)</td><td>106.65 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.41 (+16.77%)</td><td>0.28 <b>(+21.71%)</b></td><td>0.24 <b>(+40.36%)</b></td><td>0.21 <b>(+40.39%)</b></td><td>0.09 (-11.49%)</td><td>479.40 <b>(-28.77%)</b></td><td>373.92 <b>(-23.48%)</b></td><td>402.80 <b>(-28.76%)</b></td><td>239.30 (-14.35%)</td><td>108.99 <b>(-42.93%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.35 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>673.00 (n/a)</td><td>488.66 (n/a)</td><td>565.40 (n/a)</td><td>279.40 (n/a)</td><td>190.96 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.27 (+10.74%)</td><td>0.21 (+19.52%)</td><td>0.24 <b>(+38.58%)</b></td><td>0.14 (-0.74%)</td><td>0.06 <b>(+40.27%)</b></td><td>531.30 (+0.74%)</td><td>375.96 (-13.74%)</td><td>301.80 <b>(-27.85%)</b></td><td>274.60 (-9.70%)</td><td>117.10 <b>(+25.33%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>527.40 (n/a)</td><td>435.82 (n/a)</td><td>418.30 (n/a)</td><td>304.10 (n/a)</td><td>93.43 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.15 <b>(-29.64%)</b></td><td>0.12 (-14.84%)</td><td>0.14 (-9.50%)</td><td>0.04 (+5.73%)</td><td>0.05 <b>(-33.92%)</b></td><td>1908.20 (-5.41%)</td><td>804.28 (+3.35%)</td><td>539.40 (+10.51%)</td><td>477.30 <b>(+42.10%)</b></td><td>617.87 (-12.00%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.22 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.07 (n/a)</td><td>2017.40 (n/a)</td><td>778.20 (n/a)</td><td>488.10 (n/a)</td><td>335.90 (n/a)</td><td>702.14 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.38 <b>(+27.94%)</b></td><td>0.23 (-0.37%)</td><td>0.17 <b>(-27.90%)</b></td><td>0.09 <b>(-31.80%)</b></td><td>0.12 <b>(+95.12%)</b></td><td>830.50 <b>(+46.63%)</b></td><td>426.68 <b>(+20.90%)</b></td><td>427.70 <b>(+38.68%)</b></td><td>196.50 <b>(-21.84%)</b></td><td>253.52 <b>(+102.86%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>566.40 (n/a)</td><td>352.92 (n/a)</td><td>308.40 (n/a)</td><td>251.40 (n/a)</td><td>124.98 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (-18.37%)</td><td>0.08 <b>(-39.64%)</b></td><td>0.07 <b>(-45.43%)</b></td><td>0.05 <b>(-50.85%)</b></td><td>0.03 <b>(+29.42%)</b></td><td>781.40 <b>(+103.44%)</b></td><td>516.76 <b>(+79.39%)</b></td><td>514.20 <b>(+83.25%)</b></td><td>275.20 <b>(+22.53%)</b></td><td>179.51 <b>(+200.84%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>384.10 (n/a)</td><td>288.06 (n/a)</td><td>280.60 (n/a)</td><td>224.60 (n/a)</td><td>59.67 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.12 <b>(-33.21%)</b></td><td>0.10 (-10.49%)</td><td>0.12 (-7.74%)</td><td>0.08 <b>(+20.11%)</b></td><td>0.02 <b>(-60.99%)</b></td><td>443.40 (-16.73%)</td><td>362.40 (+0.35%)</td><td>319.80 (+8.37%)</td><td>311.40 <b>(+49.71%)</b></td><td>66.07 <b>(-54.99%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>532.50 (n/a)</td><td>361.14 (n/a)</td><td>295.10 (n/a)</td><td>208.00 (n/a)</td><td>146.79 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.17 (+13.71%)</td><td>0.13 <b>(+35.83%)</b></td><td>0.15 <b>(+64.81%)</b></td><td>0.07 (+12.75%)</td><td>0.04 (+7.26%)</td><td>531.70 (-11.31%)</td><td>303.60 <b>(-26.67%)</b></td><td>246.60 <b>(-39.32%)</b></td><td>215.90 (-12.06%)</td><td>129.80 (-11.20%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>599.50 (n/a)</td><td>414.00 (n/a)</td><td>406.40 (n/a)</td><td>245.50 (n/a)</td><td>146.17 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (-2.37%)</td><td>0.09 (+3.53%)</td><td>0.08 (+8.89%)</td><td>0.02 <b>(-26.94%)</b></td><td>0.05 (+3.75%)</td><td>1831.50 <b>(+36.87%)</b></td><td>667.42 (+11.89%)</td><td>476.30 (-8.16%)</td><td>259.40 (+2.41%)</td><td>659.15 <b>(+51.25%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1338.10 (n/a)</td><td>596.48 (n/a)</td><td>518.60 (n/a)</td><td>253.30 (n/a)</td><td>435.79 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.16 (-6.93%)</td><td>0.11 (-10.56%)</td><td>0.09 <b>(-29.08%)</b></td><td>0.06 <b>(-22.66%)</b></td><td>0.05 <b>(+28.14%)</b></td><td>581.90 <b>(+29.28%)</b></td><td>405.44 <b>(+20.58%)</b></td><td>430.90 <b>(+41.00%)</b></td><td>232.80 (+7.43%)</td><td>161.98 <b>(+65.31%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>450.10 (n/a)</td><td>336.24 (n/a)</td><td>305.60 (n/a)</td><td>216.70 (n/a)</td><td>97.98 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.17 <b>(+21.10%)</b></td><td>0.11 (+5.74%)</td><td>0.11 <b>(+34.50%)</b></td><td>0.05 (-17.77%)</td><td>0.05 <b>(+30.74%)</b></td><td>721.00 <b>(+21.61%)</b></td><td>410.50 (+1.70%)</td><td>322.70 <b>(-25.65%)</b></td><td>219.70 (-17.41%)</td><td>199.27 <b>(+45.14%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>592.90 (n/a)</td><td>403.62 (n/a)</td><td>434.00 (n/a)</td><td>266.00 (n/a)</td><td>137.29 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (-6.82%)</td><td>0.08 <b>(-24.48%)</b></td><td>0.08 (-5.83%)</td><td>0.02 <b>(-73.48%)</b></td><td>0.04 <b>(+21.75%)</b></td><td>2073.80 <b>(+277.05%)</b></td><td>778.76 <b>(+85.39%)</b></td><td>497.90 (+6.21%)</td><td>306.90 (+7.31%)</td><td>729.09 <b>(+498.38%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>550.00 (n/a)</td><td>420.06 (n/a)</td><td>468.80 (n/a)</td><td>286.00 (n/a)</td><td>121.84 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 <b>(+25.77%)</b></td><td>0.13 (-13.62%)</td><td>0.12 (-16.88%)</td><td>0.07 <b>(-46.15%)</b></td><td>0.06 <b>(+333.65%)</b></td><td>564.60 <b>(+85.72%)</b></td><td>381.24 <b>(+35.68%)</b></td><td>350.60 <b>(+20.32%)</b></td><td>195.90 <b>(-20.50%)</b></td><td>164.66 <b>(+573.70%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>304.00 (n/a)</td><td>280.98 (n/a)</td><td>291.40 (n/a)</td><td>246.40 (n/a)</td><td>24.44 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.17 (-0.50%)</td><td>0.12 (-7.12%)</td><td>0.13 (-5.59%)</td><td>0.07 <b>(-27.49%)</b></td><td>0.04 (+17.68%)</td><td>588.20 <b>(+37.91%)</b></td><td>367.06 (+12.97%)</td><td>305.10 (+5.94%)</td><td>245.50 (+0.49%)</td><td>144.83 <b>(+58.64%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>426.50 (n/a)</td><td>324.92 (n/a)</td><td>288.00 (n/a)</td><td>244.30 (n/a)</td><td>91.30 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.12 (-19.41%)</td><td>0.09 <b>(-20.14%)</b></td><td>0.08 <b>(-39.08%)</b></td><td>0.07 (-2.22%)</td><td>0.02 <b>(-38.15%)</b></td><td>602.00 (+2.28%)</td><td>467.30 (+18.14%)</td><td>502.20 <b>(+64.17%)</b></td><td>330.60 <b>(+24.05%)</b></td><td>117.17 <b>(-23.92%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>588.60 (n/a)</td><td>395.54 (n/a)</td><td>305.90 (n/a)</td><td>266.50 (n/a)</td><td>154.01 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 <b>(-43.44%)</b></td><td>0.10 (-18.36%)</td><td>0.10 (+9.01%)</td><td>0.07 (-3.26%)</td><td>0.02 <b>(-64.70%)</b></td><td>592.00 (+3.37%)</td><td>436.48 (+6.90%)</td><td>425.20 (-8.26%)</td><td>314.10 <b>(+76.86%)</b></td><td>106.03 <b>(-34.63%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>572.70 (n/a)</td><td>408.32 (n/a)</td><td>463.50 (n/a)</td><td>177.60 (n/a)</td><td>162.21 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.16 <b>(-23.43%)</b></td><td>0.10 (-13.81%)</td><td>0.08 <b>(-22.45%)</b></td><td>0.06 (-12.35%)</td><td>0.04 <b>(-28.26%)</b></td><td>644.00 (+14.08%)</td><td>467.08 (+12.44%)</td><td>542.10 <b>(+28.95%)</b></td><td>249.80 <b>(+30.58%)</b></td><td>161.77 (+6.63%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>564.50 (n/a)</td><td>415.42 (n/a)</td><td>420.40 (n/a)</td><td>191.30 (n/a)</td><td>151.71 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (+0.97%)</td><td>0.12 (+10.70%)</td><td>0.13 (+7.20%)</td><td>0.08 <b>(+22.67%)</b></td><td>0.02 <b>(-26.98%)</b></td><td>425.40 (-18.47%)</td><td>312.18 (-14.23%)</td><td>278.30 (-6.74%)</td><td>251.20 (-0.99%)</td><td>73.49 <b>(-42.05%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>521.80 (n/a)</td><td>363.96 (n/a)</td><td>298.40 (n/a)</td><td>253.70 (n/a)</td><td>126.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.11 (-13.14%)</td><td>0.08 <b>(-25.30%)</b></td><td>0.07 <b>(-39.99%)</b></td><td>0.01 <b>(-76.27%)</b></td><td>0.04 <b>(+25.45%)</b></td><td>2461.60 <b>(+321.36%)</b></td><td>810.14 <b>(+115.77%)</b></td><td>477.10 <b>(+66.64%)</b></td><td>310.70 (+15.12%)</td><td>927.00 <b>(+565.37%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>584.20 (n/a)</td><td>375.46 (n/a)</td><td>286.30 (n/a)</td><td>269.90 (n/a)</td><td>139.32 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.16 (+14.01%)</td><td>0.11 (+5.80%)</td><td>0.11 (-5.67%)</td><td>0.07 (-0.25%)</td><td>0.04 (+11.85%)</td><td>502.30 (+0.26%)</td><td>342.26 (-5.11%)</td><td>318.30 (+6.03%)</td><td>219.90 (-12.32%)</td><td>118.01 (-4.94%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>501.00 (n/a)</td><td>360.68 (n/a)</td><td>300.20 (n/a)</td><td>250.80 (n/a)</td><td>124.13 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (+4.38%)</td><td>0.10 <b>(+29.50%)</b></td><td>0.10 <b>(+40.77%)</b></td><td>0.06 (+0.55%)</td><td>0.03 (+6.03%)</td><td>573.00 (-0.56%)</td><td>367.00 <b>(-22.17%)</b></td><td>355.90 <b>(-28.95%)</b></td><td>255.10 (-4.21%)</td><td>127.17 (+6.90%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>576.20 (n/a)</td><td>471.54 (n/a)</td><td>500.90 (n/a)</td><td>266.30 (n/a)</td><td>118.96 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.15 (+12.42%)</td><td>0.09 (-0.44%)</td><td>0.09 (+4.30%)</td><td>0.06 (-0.08%)</td><td>0.03 (+7.17%)</td><td>597.90 (+0.08%)</td><td>403.42 (+0.65%)</td><td>406.30 (-4.13%)</td><td>233.60 (-11.04%)</td><td>133.71 (-1.96%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>597.40 (n/a)</td><td>400.82 (n/a)</td><td>423.80 (n/a)</td><td>262.60 (n/a)</td><td>136.38 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 <b>(+36.15%)</b></td><td>0.09 <b>(+37.16%)</b></td><td>0.12 <b>(+118.13%)</b></td><td>0.02 <b>(-42.36%)</b></td><td>0.05 <b>(+68.41%)</b></td><td>1798.90 <b>(+73.49%)</b></td><td>639.24 (+3.00%)</td><td>299.50 <b>(-54.16%)</b></td><td>266.60 <b>(-26.54%)</b></td><td>657.56 <b>(+137.41%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1036.90 (n/a)</td><td>620.62 (n/a)</td><td>653.40 (n/a)</td><td>362.90 (n/a)</td><td>276.97 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.43 (-14.82%)</td><td>0.32 (+6.02%)</td><td>0.42 <b>(+53.13%)</b></td><td>0.07 <b>(-44.58%)</b></td><td>0.16 (+13.95%)</td><td>1897.70 <b>(+80.46%)</b></td><td>673.22 <b>(+24.26%)</b></td><td>310.40 <b>(-34.69%)</b></td><td>308.20 (+17.41%)</td><td>691.84 <b>(+126.66%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.50 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>1051.60 (n/a)</td><td>541.80 (n/a)</td><td>475.30 (n/a)</td><td>262.50 (n/a)</td><td>305.23 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.41 (-0.12%)</td><td>0.29 (+10.04%)</td><td>0.27 (+10.62%)</td><td>0.23 <b>(+53.99%)</b></td><td>0.07 <b>(-28.11%)</b></td><td>573.90 <b>(-35.06%)</b></td><td>469.22 (-15.24%)</td><td>483.20 (-9.61%)</td><td>322.20 (+0.12%)</td><td>91.08 <b>(-56.08%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.41 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>883.70 (n/a)</td><td>553.60 (n/a)</td><td>534.60 (n/a)</td><td>321.80 (n/a)</td><td>207.39 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.42 <b>(+76.43%)</b></td><td>0.31 <b>(+59.79%)</b></td><td>0.27 <b>(+21.83%)</b></td><td>0.24 <b>(+252.11%)</b></td><td>0.08 (+14.35%)</td><td>537.70 <b>(-71.60%)</b></td><td>440.36 <b>(-47.57%)</b></td><td>488.80 (-17.92%)</td><td>313.20 <b>(-43.32%)</b></td><td>105.04 <b>(-82.17%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>1893.20 (n/a)</td><td>839.88 (n/a)</td><td>595.50 (n/a)</td><td>552.60 (n/a)</td><td>589.23 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (+0.18%)</td><td>0.01 (-19.40%)</td><td>0.01 <b>(-27.10%)</b></td><td>0.01 (-9.53%)</td><td>0.00 (+13.63%)</td><td>502.30 (+10.54%)</td><td>395.62 <b>(+26.07%)</b></td><td>391.20 <b>(+37.17%)</b></td><td>269.20 (-0.19%)</td><td>99.84 <b>(+26.20%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>454.40 (n/a)</td><td>313.82 (n/a)</td><td>285.20 (n/a)</td><td>269.70 (n/a)</td><td>79.12 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-6.54%)</td><td>0.01 <b>(-20.73%)</b></td><td>0.01 <b>(-38.40%)</b></td><td>0.01 (-19.62%)</td><td>0.00 <b>(+48.02%)</b></td><td>538.10 <b>(+24.42%)</b></td><td>411.70 <b>(+34.55%)</b></td><td>473.20 <b>(+62.33%)</b></td><td>261.60 (+6.99%)</td><td>136.39 <b>(+84.46%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>432.50 (n/a)</td><td>305.98 (n/a)</td><td>291.50 (n/a)</td><td>244.50 (n/a)</td><td>73.94 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (-12.46%)</td><td>0.01 <b>(+35.93%)</b></td><td>0.01 <b>(+53.05%)</b></td><td>0.01 <b>(+96.57%)</b></td><td>0.00 <b>(-31.84%)</b></td><td>606.90 <b>(-49.13%)</b></td><td>358.32 <b>(-37.85%)</b></td><td>303.60 <b>(-34.65%)</b></td><td>281.90 (+14.22%)</td><td>139.64 <b>(-61.31%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1193.00 (n/a)</td><td>576.58 (n/a)</td><td>464.60 (n/a)</td><td>246.80 (n/a)</td><td>360.90 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>9.91 <b>(+28.59%)</b></td><td>7.99 <b>(+31.50%)</b></td><td>7.49 (+2.51%)</td><td>6.36 <b>(+69.49%)</b></td><td>1.58 (-16.96%)</td><td>330.00 <b>(-41.00%)</b></td><td>270.76 <b>(-28.57%)</b></td><td>280.20 (-2.44%)</td><td>211.70 <b>(-22.23%)</b></td><td>51.73 <b>(-61.83%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>7.71 (n/a)</td><td>6.07 (n/a)</td><td>7.30 (n/a)</td><td>3.75 (n/a)</td><td>1.90 (n/a)</td><td>559.30 (n/a)</td><td>379.08 (n/a)</td><td>287.20 (n/a)</td><td>272.20 (n/a)</td><td>135.52 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.55 (-5.62%)</td><td>0.36 (-3.95%)</td><td>0.29 (-14.50%)</td><td>0.26 (-8.57%)</td><td>0.13 (+10.13%)</td><td>507.20 (+9.38%)</td><td>397.98 (+7.42%)</td><td>452.50 (+16.96%)</td><td>239.50 (+5.97%)</td><td>122.53 <b>(+39.53%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.58 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.12 (n/a)</td><td>463.70 (n/a)</td><td>370.48 (n/a)</td><td>386.90 (n/a)</td><td>226.00 (n/a)</td><td>87.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.56 (+10.31%)</td><td>0.40 (+13.45%)</td><td>0.41 <b>(+28.65%)</b></td><td>0.23 (-0.97%)</td><td>0.15 <b>(+20.54%)</b></td><td>578.90 (+0.98%)</td><td>372.96 (-9.33%)</td><td>322.00 <b>(-22.26%)</b></td><td>234.20 (-9.33%)</td><td>148.73 (+10.09%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.51 (n/a)</td><td>0.35 (n/a)</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>573.30 (n/a)</td><td>411.36 (n/a)</td><td>414.20 (n/a)</td><td>258.30 (n/a)</td><td>135.11 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.47 (-1.54%)</td><td>0.33 (-14.00%)</td><td>0.35 <b>(-20.03%)</b></td><td>0.20 (-15.37%)</td><td>0.11 (+3.33%)</td><td>652.80 (+18.15%)</td><td>450.32 (+19.19%)</td><td>376.30 <b>(+25.06%)</b></td><td>279.10 (+1.56%)</td><td>162.48 <b>(+30.76%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.48 (n/a)</td><td>0.38 (n/a)</td><td>0.44 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>552.50 (n/a)</td><td>377.82 (n/a)</td><td>300.90 (n/a)</td><td>274.80 (n/a)</td><td>124.26 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.48 <b>(+44.17%)</b></td><td>0.35 <b>(+38.13%)</b></td><td>0.30 (+16.14%)</td><td>0.26 <b>(+126.20%)</b></td><td>0.11 <b>(+22.16%)</b></td><td>507.20 <b>(-55.79%)</b></td><td>398.58 <b>(-33.20%)</b></td><td>441.80 (-13.90%)</td><td>272.50 <b>(-30.64%)</b></td><td>109.09 <b>(-65.11%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>1147.20 (n/a)</td><td>596.68 (n/a)</td><td>513.10 (n/a)</td><td>392.90 (n/a)</td><td>312.66 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.58 <b>(+32.02%)</b></td><td>0.50 <b>(+52.38%)</b></td><td>0.49 <b>(+73.54%)</b></td><td>0.45 <b>(+72.49%)</b></td><td>0.05 <b>(-36.88%)</b></td><td>291.40 <b>(-42.02%)</b></td><td>266.66 <b>(-36.84%)</b></td><td>271.00 <b>(-42.36%)</b></td><td>227.20 <b>(-24.27%)</b></td><td>26.04 <b>(-72.84%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.44 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.08 (n/a)</td><td>502.60 (n/a)</td><td>422.20 (n/a)</td><td>470.20 (n/a)</td><td>300.00 (n/a)</td><td>95.89 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (-1.15%)</td><td>0.01 (+14.73%)</td><td>0.02 <b>(+70.15%)</b></td><td>0.01 (-8.77%)</td><td>0.00 (-0.06%)</td><td>579.00 (+9.62%)</td><td>348.44 (-12.08%)</td><td>267.40 <b>(-41.23%)</b></td><td>256.70 (+1.18%)</td><td>138.70 (+11.38%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.20 (n/a)</td><td>396.32 (n/a)</td><td>455.00 (n/a)</td><td>253.70 (n/a)</td><td>124.53 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (+5.45%)</td><td>0.01 (+3.55%)</td><td>0.01 (-1.71%)</td><td>0.01 (+4.91%)</td><td>0.00 (-9.13%)</td><td>490.20 (-4.69%)</td><td>333.54 (-6.20%)</td><td>308.70 (+1.75%)</td><td>217.30 (-5.15%)</td><td>106.05 (-19.54%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>514.30 (n/a)</td><td>355.58 (n/a)</td><td>303.40 (n/a)</td><td>229.10 (n/a)</td><td>131.81 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-37.50%)</b></td><td>0.00 <b>(-60.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+16.25%)</td><td>22214.58 <b>(+32.99%)</b></td><td>17787.09 <b>(+89.65%)</b></td><td>21201.47 <b>(+155.49%)</b></td><td>6141.64 (+10.37%)</td><td>6736.69 <b>(+53.64%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>16703.39 (n/a)</td><td>9378.67 (n/a)</td><td>8298.28 (n/a)</td><td>5564.44 (n/a)</td><td>4384.85 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.00 (-18.18%)</td><td>0.00 (+7.14%)</td><td>0.00 <b>(+25.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-23.10%)</b></td><td>19703.68 (-9.19%)</td><td>14963.95 (-14.23%)</td><td>17961.50 (-14.70%)</td><td>8867.63 (+17.75%)</td><td>5219.93 (-13.31%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21697.01 (n/a)</td><td>17445.67 (n/a)</td><td>21057.78 (n/a)</td><td>7530.58 (n/a)</td><td>6021.64 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 <b>(-50.03%)</b></td><td>0.08 <b>(-26.72%)</b></td><td>0.07 (-16.48%)</td><td>0.07 (-15.42%)</td><td>0.00 <b>(-88.78%)</b></td><td>29894.75 (+18.26%)</td><td>27927.24 <b>(+28.82%)</b></td><td>27945.62 (+19.71%)</td><td>26048.41 <b>(+100.15%)</b></td><td>1375.52 <b>(-72.09%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>25278.45 (n/a)</td><td>21678.79 (n/a)</td><td>23343.96 (n/a)</td><td>13014.67 (n/a)</td><td>4928.89 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 <b>(+34.82%)</b></td><td>0.09 (+3.29%)</td><td>0.08 (-2.33%)</td><td>0.07 (-12.10%)</td><td>0.02 <b>(+297.69%)</b></td><td>28313.49 (+13.86%)</td><td>23868.00 (+0.64%)</td><td>24973.54 (+2.43%)</td><td>15743.83 <b>(-25.81%)</b></td><td>4767.50 <b>(+220.65%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>24866.02 (n/a)</td><td>23715.52 (n/a)</td><td>24381.56 (n/a)</td><td>21221.93 (n/a)</td><td>1486.84 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:05:01</td><td>0.14 (-3.03%)</td><td>0.10 (+3.28%)</td><td>0.09 (+8.02%)</td><td>0.08 (+3.38%)</td><td>0.03 (-8.84%)</td><td>27406.71 (-3.28%)</td><td>21153.91 (-4.07%)</td><td>22243.66 (-7.45%)</td><td>15227.60 (+3.12%)</td><td>4937.71 (-9.41%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 20:45:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28335.16 (n/a)</td><td>22050.70 (n/a)</td><td>24034.92 (n/a)</td><td>14767.00 (n/a)</td><td>5450.80 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>2.59 (-18.15%)</td><td>1.98 (-4.53%)</td><td>2.22 <b>(+22.21%)</b></td><td>1.09 <b>(-24.99%)</b></td><td>0.61 (-12.62%)</td><td>960.50 <b>(+33.31%)</b></td><td>585.22 (+6.83%)</td><td>472.70 (-18.18%)</td><td>405.50 <b>(+22.18%)</b></td><td>228.26 <b>(+44.93%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.16 (n/a)</td><td>2.07 (n/a)</td><td>1.82 (n/a)</td><td>1.46 (n/a)</td><td>0.69 (n/a)</td><td>720.50 (n/a)</td><td>547.82 (n/a)</td><td>577.70 (n/a)</td><td>331.90 (n/a)</td><td>157.50 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.30 (+3.84%)</td><td>2.30 (+3.83%)</td><td>2.42 (-4.66%)</td><td>1.47 <b>(+33.66%)</b></td><td>0.71 <b>(-21.58%)</b></td><td>711.80 <b>(-25.18%)</b></td><td>493.14 (-11.88%)</td><td>434.00 (+4.88%)</td><td>317.90 (-3.70%)</td><td>155.02 <b>(-42.67%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.18 (n/a)</td><td>2.21 (n/a)</td><td>2.53 (n/a)</td><td>1.10 (n/a)</td><td>0.90 (n/a)</td><td>951.40 (n/a)</td><td>559.64 (n/a)</td><td>413.80 (n/a)</td><td>330.10 (n/a)</td><td>270.37 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>2.50 <b>(-26.02%)</b></td><td>1.88 <b>(-29.01%)</b></td><td>1.76 <b>(-32.23%)</b></td><td>1.40 (-12.15%)</td><td>0.42 <b>(-38.95%)</b></td><td>748.60 (+13.84%)</td><td>579.74 <b>(+36.74%)</b></td><td>596.30 <b>(+47.53%)</b></td><td>420.10 <b>(+35.17%)</b></td><td>124.05 (-9.86%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.37 (n/a)</td><td>2.65 (n/a)</td><td>2.59 (n/a)</td><td>1.59 (n/a)</td><td>0.69 (n/a)</td><td>657.60 (n/a)</td><td>423.98 (n/a)</td><td>404.20 (n/a)</td><td>310.80 (n/a)</td><td>137.62 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.34 (-2.70%)</td><td>2.30 (+13.53%)</td><td>2.57 <b>(+29.12%)</b></td><td>1.22 <b>(+25.10%)</b></td><td>0.88 (-2.04%)</td><td>858.70 <b>(-20.06%)</b></td><td>525.14 (-13.87%)</td><td>408.40 <b>(-22.56%)</b></td><td>313.90 (+2.78%)</td><td>230.45 (-19.30%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>3.43 (n/a)</td><td>2.02 (n/a)</td><td>1.99 (n/a)</td><td>0.98 (n/a)</td><td>0.90 (n/a)</td><td>1074.20 (n/a)</td><td>609.68 (n/a)</td><td>527.40 (n/a)</td><td>305.40 (n/a)</td><td>285.55 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>4.16 (-2.03%)</td><td>3.35 <b>(+65.56%)</b></td><td>3.33 <b>(+117.24%)</b></td><td>2.47 <b>(+326.19%)</b></td><td>0.63 <b>(-61.69%)</b></td><td>849.40 <b>(-76.54%)</b></td><td>644.46 <b>(-66.74%)</b></td><td>629.10 <b>(-53.96%)</b></td><td>503.70 (+2.07%)</td><td>129.64 <b>(-91.57%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.25 (n/a)</td><td>2.03 (n/a)</td><td>1.53 (n/a)</td><td>0.58 (n/a)</td><td>1.63 (n/a)</td><td>3619.90 (n/a)</td><td>1937.66 (n/a)</td><td>1366.50 (n/a)</td><td>493.50 (n/a)</td><td>1538.00 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.76 (-15.56%)</td><td>2.79 <b>(-21.75%)</b></td><td>2.83 <b>(-20.24%)</b></td><td>1.99 <b>(-22.68%)</b></td><td>0.68 (-3.56%)</td><td>1056.10 <b>(+29.34%)</b></td><td>789.18 <b>(+29.56%)</b></td><td>742.20 <b>(+25.39%)</b></td><td>557.10 (+18.43%)</td><td>192.79 <b>(+46.60%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.46 (n/a)</td><td>3.56 (n/a)</td><td>3.54 (n/a)</td><td>2.57 (n/a)</td><td>0.71 (n/a)</td><td>816.50 (n/a)</td><td>609.14 (n/a)</td><td>591.90 (n/a)</td><td>470.40 (n/a)</td><td>131.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.35 <b>(+31.14%)</b></td><td>3.71 <b>(+100.67%)</b></td><td>3.69 <b>(+222.64%)</b></td><td>1.73 <b>(+195.20%)</b></td><td>1.53 (+0.24%)</td><td>1209.40 <b>(-66.13%)</b></td><td>672.26 <b>(-66.12%)</b></td><td>568.30 <b>(-69.01%)</b></td><td>392.00 <b>(-23.75%)</b></td><td>337.25 <b>(-75.86%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.08 (n/a)</td><td>1.85 (n/a)</td><td>1.14 (n/a)</td><td>0.59 (n/a)</td><td>1.53 (n/a)</td><td>3570.20 (n/a)</td><td>1984.44 (n/a)</td><td>1833.60 (n/a)</td><td>514.10 (n/a)</td><td>1397.34 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.63 (+17.09%)</td><td>3.09 (+16.46%)</td><td>3.18 (+17.36%)</td><td>0.58 <b>(-42.21%)</b></td><td>1.84 <b>(+28.93%)</b></td><td>3618.10 <b>(+73.05%)</b></td><td>1219.56 (+17.83%)</td><td>658.70 (-14.80%)</td><td>372.60 (-14.58%)</td><td>1353.06 <b>(+109.84%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.81 (n/a)</td><td>2.65 (n/a)</td><td>2.71 (n/a)</td><td>1.00 (n/a)</td><td>1.43 (n/a)</td><td>2090.80 (n/a)</td><td>1035.06 (n/a)</td><td>773.10 (n/a)</td><td>436.20 (n/a)</td><td>644.80 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>4.27 <b>(-28.59%)</b></td><td>2.57 <b>(-39.82%)</b></td><td>3.24 (-16.12%)</td><td>0.58 <b>(-82.50%)</b></td><td>1.85 <b>(+69.70%)</b></td><td>3586.70 <b>(+471.40%)</b></td><td>1742.52 <b>(+238.89%)</b></td><td>647.30 (+19.21%)</td><td>491.50 <b>(+40.03%)</b></td><td>1637.63 <b>(+1325.47%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>5.97 (n/a)</td><td>4.27 (n/a)</td><td>3.86 (n/a)</td><td>3.34 (n/a)</td><td>1.09 (n/a)</td><td>627.70 (n/a)</td><td>514.18 (n/a)</td><td>543.00 (n/a)</td><td>351.00 (n/a)</td><td>114.88 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>4.81 (-11.19%)</td><td>3.03 <b>(+85.37%)</b></td><td>3.14 <b>(+420.01%)</b></td><td>0.85 <b>(+45.16%)</b></td><td>1.48 <b>(-30.23%)</b></td><td>2477.40 <b>(-31.11%)</b></td><td>989.66 <b>(-62.27%)</b></td><td>667.40 <b>(-80.77%)</b></td><td>436.00 (+12.60%)</td><td>843.44 <b>(-39.39%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>5.42 (n/a)</td><td>1.64 (n/a)</td><td>0.60 (n/a)</td><td>0.58 (n/a)</td><td>2.12 (n/a)</td><td>3596.30 (n/a)</td><td>2623.30 (n/a)</td><td>3470.60 (n/a)</td><td>387.20 (n/a)</td><td>1391.62 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.53 <b>(+23.23%)</b></td><td>3.93 <b>(+29.68%)</b></td><td>4.36 <b>(+23.11%)</b></td><td>1.09 (-8.43%)</td><td>1.67 (+10.93%)</td><td>3855.00 (+9.21%)</td><td>1502.00 (-17.71%)</td><td>961.00 (-18.77%)</td><td>759.10 (-18.85%)</td><td>1318.65 (+14.94%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>4.48 (n/a)</td><td>3.03 (n/a)</td><td>3.55 (n/a)</td><td>1.19 (n/a)</td><td>1.51 (n/a)</td><td>3530.00 (n/a)</td><td>1825.20 (n/a)</td><td>1183.10 (n/a)</td><td>935.40 (n/a)</td><td>1147.21 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>7.92 (-1.20%)</td><td>6.64 (+16.14%)</td><td>6.19 (+6.89%)</td><td>5.90 <b>(+65.00%)</b></td><td>0.83 <b>(-59.06%)</b></td><td>710.60 <b>(-39.39%)</b></td><td>639.44 <b>(-22.02%)</b></td><td>677.30 (-6.44%)</td><td>529.70 (+1.22%)</td><td>74.79 <b>(-75.55%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>8.01 (n/a)</td><td>5.71 (n/a)</td><td>5.79 (n/a)</td><td>3.58 (n/a)</td><td>2.04 (n/a)</td><td>1172.50 (n/a)</td><td>820.04 (n/a)</td><td>723.90 (n/a)</td><td>523.30 (n/a)</td><td>305.95 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.60 <b>(-28.86%)</b></td><td>2.85 <b>(-50.18%)</b></td><td>2.05 <b>(-64.66%)</b></td><td>1.20 <b>(-65.98%)</b></td><td>1.96 (-9.66%)</td><td>3499.40 <b>(+193.94%)</b></td><td>2152.50 <b>(+158.20%)</b></td><td>2042.10 <b>(+182.96%)</b></td><td>749.30 <b>(+40.56%)</b></td><td>1308.67 <b>(+291.57%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>7.87 (n/a)</td><td>5.72 (n/a)</td><td>5.81 (n/a)</td><td>3.52 (n/a)</td><td>2.17 (n/a)</td><td>1190.50 (n/a)</td><td>833.66 (n/a)</td><td>721.70 (n/a)</td><td>533.10 (n/a)</td><td>334.21 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>10.03 (+6.55%)</td><td>6.96 (+16.00%)</td><td>7.05 (+5.92%)</td><td>4.14 (+18.29%)</td><td>2.72 (+11.56%)</td><td>1012.40 (-15.46%)</td><td>689.50 (-14.18%)</td><td>594.90 (-5.59%)</td><td>418.10 (-6.15%)</td><td>283.59 (-14.75%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>9.41 (n/a)</td><td>6.00 (n/a)</td><td>6.66 (n/a)</td><td>3.50 (n/a)</td><td>2.44 (n/a)</td><td>1197.60 (n/a)</td><td>803.38 (n/a)</td><td>630.10 (n/a)</td><td>445.50 (n/a)</td><td>332.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>6.86 <b>(-25.50%)</b></td><td>5.80 <b>(+28.04%)</b></td><td>6.72 <b>(+67.59%)</b></td><td>3.62 <b>(+209.61%)</b></td><td>1.44 <b>(-59.51%)</b></td><td>1158.30 <b>(-67.70%)</b></td><td>770.30 <b>(-58.03%)</b></td><td>624.00 <b>(-40.33%)</b></td><td>611.10 <b>(+34.22%)</b></td><td>237.27 <b>(-84.90%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>9.21 (n/a)</td><td>4.53 (n/a)</td><td>4.01 (n/a)</td><td>1.17 (n/a)</td><td>3.57 (n/a)</td><td>3586.30 (n/a)</td><td>1835.20 (n/a)</td><td>1045.80 (n/a)</td><td>455.30 (n/a)</td><td>1571.51 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>8.84 <b>(+27.80%)</b></td><td>6.62 (+11.64%)</td><td>7.01 (+11.65%)</td><td>4.39 (+5.16%)</td><td>1.76 <b>(+67.42%)</b></td><td>954.40 (-4.91%)</td><td>673.54 (-7.64%)</td><td>598.40 (-10.43%)</td><td>474.30 <b>(-21.75%)</b></td><td>193.10 <b>(+21.90%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>6.92 (n/a)</td><td>5.93 (n/a)</td><td>6.28 (n/a)</td><td>4.18 (n/a)</td><td>1.05 (n/a)</td><td>1003.70 (n/a)</td><td>729.24 (n/a)</td><td>668.10 (n/a)</td><td>606.10 (n/a)</td><td>158.41 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.61 (-5.82%)</td><td>0.98 (-8.46%)</td><td>0.95 (-18.62%)</td><td>0.16 (+4.59%)</td><td>0.57 (-1.18%)</td><td>3270.30 (-4.39%)</td><td>1037.08 (+1.95%)</td><td>553.00 <b>(+22.86%)</b></td><td>326.10 (+6.15%)</td><td>1256.06 (-6.66%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.71 (n/a)</td><td>1.08 (n/a)</td><td>1.16 (n/a)</td><td>0.15 (n/a)</td><td>0.58 (n/a)</td><td>3420.40 (n/a)</td><td>1017.26 (n/a)</td><td>450.10 (n/a)</td><td>307.20 (n/a)</td><td>1345.63 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.92 (-13.03%)</td><td>1.08 (+1.46%)</td><td>1.40 <b>(+47.59%)</b></td><td>0.30 (-3.97%)</td><td>0.74 (-9.94%)</td><td>3517.90 (+4.14%)</td><td>1773.86 (-0.47%)</td><td>748.40 <b>(-32.24%)</b></td><td>547.30 (+14.98%)</td><td>1520.42 (+6.22%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>2.20 (n/a)</td><td>1.07 (n/a)</td><td>0.95 (n/a)</td><td>0.31 (n/a)</td><td>0.82 (n/a)</td><td>3378.10 (n/a)</td><td>1782.28 (n/a)</td><td>1104.50 (n/a)</td><td>476.00 (n/a)</td><td>1431.42 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.92 <b>(+41.02%)</b></td><td>2.87 <b>(+82.48%)</b></td><td>2.59 <b>(+120.85%)</b></td><td>1.75 <b>(+189.17%)</b></td><td>0.98 (+9.71%)</td><td>1200.30 <b>(-65.42%)</b></td><td>805.18 <b>(-54.58%)</b></td><td>808.60 <b>(-54.72%)</b></td><td>534.70 <b>(-29.08%)</b></td><td>280.76 <b>(-73.85%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>2.78 (n/a)</td><td>1.57 (n/a)</td><td>1.17 (n/a)</td><td>0.60 (n/a)</td><td>0.89 (n/a)</td><td>3471.00 (n/a)</td><td>1772.58 (n/a)</td><td>1785.70 (n/a)</td><td>754.00 (n/a)</td><td>1073.68 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.75 <b>(+47.41%)</b></td><td>1.34 <b>(+38.34%)</b></td><td>1.26 <b>(+29.40%)</b></td><td>0.99 <b>(+30.75%)</b></td><td>0.29 <b>(+86.22%)</b></td><td>531.50 <b>(-23.53%)</b></td><td>405.58 <b>(-26.58%)</b></td><td>416.20 <b>(-22.73%)</b></td><td>299.90 <b>(-32.18%)</b></td><td>86.89 (-5.01%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>1.19 (n/a)</td><td>0.97 (n/a)</td><td>0.97 (n/a)</td><td>0.75 (n/a)</td><td>0.15 (n/a)</td><td>695.00 (n/a)</td><td>552.38 (n/a)</td><td>538.60 (n/a)</td><td>442.20 (n/a)</td><td>91.47 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 <b>(+45.09%)</b></td><td>0.10 (+8.54%)</td><td>0.06 (-18.60%)</td><td>0.05 <b>(-26.85%)</b></td><td>0.07 <b>(+102.53%)</b></td><td>659.80 <b>(+36.69%)</b></td><td>441.16 (+14.49%)</td><td>553.20 <b>(+22.85%)</b></td><td>159.40 <b>(-31.09%)</b></td><td>225.85 <b>(+88.92%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>482.70 (n/a)</td><td>385.32 (n/a)</td><td>450.30 (n/a)</td><td>231.30 (n/a)</td><td>119.54 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.17 (+19.03%)</td><td>0.09 (+16.66%)</td><td>0.08 (+11.94%)</td><td>0.05 (+8.86%)</td><td>0.05 <b>(+26.60%)</b></td><td>612.60 (-8.14%)</td><td>417.12 (-11.30%)</td><td>434.20 (-10.66%)</td><td>191.00 (-16.01%)</td><td>161.75 (+2.72%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>666.90 (n/a)</td><td>470.28 (n/a)</td><td>486.00 (n/a)</td><td>227.40 (n/a)</td><td>157.47 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.30 <b>(+43.78%)</b></td><td>0.19 <b>(+25.22%)</b></td><td>0.15 (+13.93%)</td><td>0.13 <b>(+20.14%)</b></td><td>0.07 <b>(+82.13%)</b></td><td>509.10 (-16.76%)</td><td>389.32 (-16.02%)</td><td>429.60 (-12.24%)</td><td>216.30 <b>(-30.45%)</b></td><td>125.31 (+8.97%)</td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>611.60 (n/a)</td><td>463.58 (n/a)</td><td>489.50 (n/a)</td><td>311.00 (n/a)</td><td>114.99 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.41 <b>(+85.32%)</b></td><td>0.24 <b>(+42.79%)</b></td><td>0.24 <b>(+46.76%)</b></td><td>0.14 (+9.43%)</td><td>0.11 <b>(+192.01%)</b></td><td>469.10 (-8.61%)</td><td>323.30 <b>(-21.58%)</b></td><td>277.70 <b>(-31.85%)</b></td><td>158.00 <b>(-46.04%)</b></td><td>128.59 <b>(+48.70%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>513.30 (n/a)</td><td>412.28 (n/a)</td><td>407.50 (n/a)</td><td>292.80 (n/a)</td><td>86.48 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.28 <b>(+20.21%)</b></td><td>0.18 (+14.08%)</td><td>0.13 (+2.06%)</td><td>0.11 <b>(+36.85%)</b></td><td>0.08 (+6.47%)</td><td>576.70 <b>(-26.93%)</b></td><td>427.74 (-15.86%)</td><td>487.40 (-2.03%)</td><td>234.00 (-16.81%)</td><td>161.07 <b>(-29.96%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>789.20 (n/a)</td><td>508.38 (n/a)</td><td>497.50 (n/a)</td><td>281.30 (n/a)</td><td>229.99 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.47 (+13.65%)</td><td>0.29 (-9.33%)</td><td>0.26 (-14.99%)</td><td>0.20 (-11.41%)</td><td>0.10 <b>(+40.03%)</b></td><td>659.90 (+12.88%)</td><td>495.22 (+14.34%)</td><td>507.80 (+17.66%)</td><td>279.60 (-12.02%)</td><td>138.26 <b>(+31.21%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.07 (n/a)</td><td>584.60 (n/a)</td><td>433.12 (n/a)</td><td>431.60 (n/a)</td><td>317.80 (n/a)</td><td>105.37 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.51 (-8.32%)</td><td>0.39 <b>(+25.25%)</b></td><td>0.43 <b>(+56.76%)</b></td><td>0.23 (+10.64%)</td><td>0.11 <b>(-24.78%)</b></td><td>559.70 (-9.61%)</td><td>363.90 <b>(-23.70%)</b></td><td>304.80 <b>(-36.22%)</b></td><td>256.60 (+9.10%)</td><td>120.25 <b>(-20.02%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.56 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>619.20 (n/a)</td><td>476.94 (n/a)</td><td>477.90 (n/a)</td><td>235.20 (n/a)</td><td>150.35 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.35 <b>(-42.90%)</b></td><td>0.28 (-3.57%)</td><td>0.29 (+10.66%)</td><td>0.22 <b>(+105.58%)</b></td><td>0.05 <b>(-72.61%)</b></td><td>605.30 <b>(-51.35%)</b></td><td>484.02 <b>(-22.05%)</b></td><td>449.10 (-9.64%)</td><td>378.30 <b>(+75.14%)</b></td><td>92.19 <b>(-75.98%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.61 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>0.19 (n/a)</td><td>1244.30 (n/a)</td><td>620.92 (n/a)</td><td>497.00 (n/a)</td><td>216.00 (n/a)</td><td>383.77 (n/a)</td>
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
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (-8.45%)</td><td>0.03 (+10.48%)</td><td>0.03 (+3.24%)</td><td>0.03 <b>(+107.86%)</b></td><td>0.01 <b>(-38.58%)</b></td><td>573.30 <b>(-51.89%)</b></td><td>505.26 <b>(-21.81%)</b></td><td>550.20 (-3.15%)</td><td>326.50 (+9.23%)</td><td>101.49 <b>(-69.13%)</b></td>
</tr>
<tr>
<td><code>9938c0a</code> — 2026-09-18 23:10:40</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1191.70 (n/a)</td><td>646.18 (n/a)</td><td>568.10 (n/a)</td><td>298.90 (n/a)</td><td>328.81 (n/a)</td>
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
