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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (-2.54%)</td><td>0.02 (+8.24%)</td><td>0.02 <b>(+28.89%)</b></td><td>0.01 <b>(+300.23%)</b></td><td>0.01 <b>(-39.24%)</b></td><td>518.90 <b>(-75.02%)</b></td><td>368.68 <b>(-45.93%)</b></td><td>315.90 <b>(-22.42%)</b></td><td>235.30 (+2.62%)</td><td>127.66 <b>(-83.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2076.90 (n/a)</td><td>681.86 (n/a)</td><td>407.20 (n/a)</td><td>229.30 (n/a)</td><td>786.88 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (+1.36%)</td><td>0.02 <b>(+25.88%)</b></td><td>0.02 <b>(+66.23%)</b></td><td>0.01 <b>(+74.68%)</b></td><td>0.00 <b>(-41.38%)</b></td><td>413.50 <b>(-42.74%)</b></td><td>315.28 <b>(-29.72%)</b></td><td>299.50 <b>(-39.84%)</b></td><td>246.00 (-1.36%)</td><td>68.45 <b>(-64.68%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>722.20 (n/a)</td><td>448.60 (n/a)</td><td>497.80 (n/a)</td><td>249.40 (n/a)</td><td>193.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 <b>(-53.42%)</b></td><td>0.01 <b>(-51.33%)</b></td><td>0.01 <b>(-47.55%)</b></td><td>0.00 <b>(-58.43%)</b></td><td>0.01 <b>(-52.84%)</b></td><td>1253.50 <b>(+140.60%)</b></td><td>635.58 <b>(+112.90%)</b></td><td>554.60 <b>(+90.65%)</b></td><td>286.40 <b>(+114.69%)</b></td><td>366.51 <b>(+160.05%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>521.00 (n/a)</td><td>298.54 (n/a)</td><td>290.90 (n/a)</td><td>133.40 (n/a)</td><td>140.94 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 <b>(-22.35%)</b></td><td>0.02 <b>(-23.98%)</b></td><td>0.01 <b>(-44.45%)</b></td><td>0.01 (-14.38%)</td><td>0.01 <b>(-25.40%)</b></td><td>623.40 (+16.81%)</td><td>443.84 <b>(+26.87%)</b></td><td>442.30 <b>(+80.02%)</b></td><td>251.30 <b>(+28.81%)</b></td><td>175.32 (+4.91%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>533.70 (n/a)</td><td>349.84 (n/a)</td><td>245.70 (n/a)</td><td>195.10 (n/a)</td><td>167.11 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 <b>(-20.69%)</b></td><td>0.01 <b>(-20.41%)</b></td><td>0.01 <b>(-22.16%)</b></td><td>0.01 (+8.98%)</td><td>0.00 <b>(-42.18%)</b></td><td>673.90 (-8.24%)</td><td>474.74 (+12.49%)</td><td>470.60 <b>(+28.47%)</b></td><td>288.50 <b>(+26.09%)</b></td><td>142.27 <b>(-32.53%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>734.40 (n/a)</td><td>422.04 (n/a)</td><td>366.30 (n/a)</td><td>228.80 (n/a)</td><td>210.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 <b>(+31.32%)</b></td><td>0.01 (+10.88%)</td><td>0.01 (+9.16%)</td><td>0.00 <b>(-44.93%)</b></td><td>0.01 <b>(+62.53%)</b></td><td>1881.90 <b>(+81.58%)</b></td><td>675.28 <b>(+24.50%)</b></td><td>441.10 (-8.39%)</td><td>239.00 <b>(-23.86%)</b></td><td>680.41 <b>(+138.63%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1036.40 (n/a)</td><td>542.40 (n/a)</td><td>481.50 (n/a)</td><td>313.90 (n/a)</td><td>285.13 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (-15.15%)</td><td>0.04 (-17.52%)</td><td>0.04 <b>(-20.23%)</b></td><td>0.02 (-16.42%)</td><td>0.01 (-14.66%)</td><td>569.50 (+19.64%)</td><td>363.22 <b>(+21.29%)</b></td><td>335.60 <b>(+25.36%)</b></td><td>281.20 (+17.85%)</td><td>118.56 (+19.00%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>476.00 (n/a)</td><td>299.46 (n/a)</td><td>267.70 (n/a)</td><td>238.60 (n/a)</td><td>99.63 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 <b>(-34.51%)</b></td><td>0.03 <b>(-29.00%)</b></td><td>0.03 (-18.34%)</td><td>0.01 <b>(-32.17%)</b></td><td>0.01 <b>(-33.30%)</b></td><td>835.50 <b>(+47.43%)</b></td><td>502.04 <b>(+41.81%)</b></td><td>426.00 <b>(+22.48%)</b></td><td>264.30 <b>(+52.69%)</b></td><td>238.30 <b>(+53.96%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>566.70 (n/a)</td><td>354.02 (n/a)</td><td>347.80 (n/a)</td><td>173.10 (n/a)</td><td>154.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 (+14.77%)</td><td>0.03 (+17.39%)</td><td>0.03 (-4.46%)</td><td>0.02 <b>(+290.87%)</b></td><td>0.01 <b>(-27.18%)</b></td><td>494.70 <b>(-74.41%)</b></td><td>402.56 <b>(-42.53%)</b></td><td>409.70 (+4.65%)</td><td>246.80 (-12.85%)</td><td>102.07 <b>(-85.33%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1933.50 (n/a)</td><td>700.50 (n/a)</td><td>391.50 (n/a)</td><td>283.20 (n/a)</td><td>695.77 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 <b>(-36.84%)</b></td><td>0.02 <b>(-20.34%)</b></td><td>0.02 (-18.07%)</td><td>0.02 (-7.50%)</td><td>0.00 <b>(-57.26%)</b></td><td>598.20 (+8.11%)</td><td>510.10 (+19.94%)</td><td>540.30 <b>(+22.05%)</b></td><td>412.90 <b>(+58.32%)</b></td><td>83.40 <b>(-26.05%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>553.30 (n/a)</td><td>425.30 (n/a)</td><td>442.70 (n/a)</td><td>260.80 (n/a)</td><td>112.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 <b>(+36.55%)</b></td><td>0.04 <b>(+21.52%)</b></td><td>0.03 (+14.19%)</td><td>0.02 (+6.20%)</td><td>0.01 <b>(+105.23%)</b></td><td>537.40 (-5.83%)</td><td>367.28 (-12.47%)</td><td>354.70 (-12.42%)</td><td>232.90 <b>(-26.78%)</b></td><td>127.46 <b>(+36.10%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>570.70 (n/a)</td><td>419.60 (n/a)</td><td>405.00 (n/a)</td><td>318.10 (n/a)</td><td>93.65 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (+0.83%)</td><td>0.02 (-1.14%)</td><td>0.02 (-7.64%)</td><td>0.01 <b>(+91.08%)</b></td><td>0.01 <b>(-30.27%)</b></td><td>1037.60 <b>(-47.66%)</b></td><td>640.26 <b>(-29.39%)</b></td><td>616.20 (+8.28%)</td><td>304.90 (-0.81%)</td><td>262.73 <b>(-64.05%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1982.60 (n/a)</td><td>906.80 (n/a)</td><td>569.10 (n/a)</td><td>307.40 (n/a)</td><td>730.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 <b>(-32.66%)</b></td><td>0.07 (-19.86%)</td><td>0.06 <b>(-21.13%)</b></td><td>0.05 (-13.36%)</td><td>0.02 <b>(-42.44%)</b></td><td>471.20 (+15.43%)</td><td>383.08 <b>(+20.84%)</b></td><td>380.90 <b>(+26.80%)</b></td><td>292.10 <b>(+48.50%)</b></td><td>86.80 (-4.84%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>408.20 (n/a)</td><td>317.02 (n/a)</td><td>300.40 (n/a)</td><td>196.70 (n/a)</td><td>91.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 (+15.86%)</td><td>0.07 (+1.35%)</td><td>0.05 <b>(-31.46%)</b></td><td>0.05 (+7.57%)</td><td>0.03 <b>(+36.94%)</b></td><td>524.90 (-7.03%)</td><td>390.12 (+2.83%)</td><td>454.50 <b>(+45.91%)</b></td><td>218.90 (-13.68%)</td><td>142.33 (+8.34%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>564.60 (n/a)</td><td>379.40 (n/a)</td><td>311.50 (n/a)</td><td>253.60 (n/a)</td><td>131.37 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 <b>(-44.52%)</b></td><td>0.06 <b>(-31.76%)</b></td><td>0.05 <b>(-45.00%)</b></td><td>0.05 (+4.93%)</td><td>0.01 <b>(-64.13%)</b></td><td>495.60 (-4.69%)</td><td>429.10 <b>(+32.40%)</b></td><td>485.20 <b>(+81.86%)</b></td><td>329.70 <b>(+80.26%)</b></td><td>82.03 <b>(-39.26%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>520.00 (n/a)</td><td>324.10 (n/a)</td><td>266.80 (n/a)</td><td>182.90 (n/a)</td><td>135.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (-19.04%)</td><td>0.04 <b>(-27.90%)</b></td><td>0.05 (-15.92%)</td><td>0.01 <b>(-74.04%)</b></td><td>0.02 <b>(+97.07%)</b></td><td>1931.80 <b>(+285.20%)</b></td><td>788.72 <b>(+83.36%)</b></td><td>532.10 (+18.93%)</td><td>439.50 <b>(+23.49%)</b></td><td>640.25 <b>(+943.92%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>501.50 (n/a)</td><td>430.14 (n/a)</td><td>447.40 (n/a)</td><td>355.90 (n/a)</td><td>61.33 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (-2.37%)</td><td>0.05 (-16.92%)</td><td>0.05 (-13.42%)</td><td>0.02 <b>(-50.25%)</b></td><td>0.02 <b>(+56.92%)</b></td><td>1105.90 <b>(+101.00%)</b></td><td>600.52 <b>(+35.42%)</b></td><td>539.60 (+15.50%)</td><td>355.30 (+2.42%)</td><td>296.03 <b>(+247.91%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>550.20 (n/a)</td><td>443.46 (n/a)</td><td>467.20 (n/a)</td><td>346.90 (n/a)</td><td>85.09 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (-18.85%)</td><td>0.06 <b>(-28.72%)</b></td><td>0.05 <b>(-37.94%)</b></td><td>0.04 <b>(-26.40%)</b></td><td>0.02 <b>(-23.78%)</b></td><td>652.60 <b>(+35.87%)</b></td><td>461.56 <b>(+39.82%)</b></td><td>451.20 <b>(+61.14%)</b></td><td>289.20 <b>(+23.22%)</b></td><td>141.04 <b>(+28.42%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>480.30 (n/a)</td><td>330.10 (n/a)</td><td>280.00 (n/a)</td><td>234.70 (n/a)</td><td>109.82 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.20 (+6.27%)</td><td>0.11 (+13.43%)</td><td>0.13 <b>(+25.62%)</b></td><td>0.03 (+6.92%)</td><td>0.06 (+9.25%)</td><td>1955.20 (-6.48%)</td><td>699.30 (-9.18%)</td><td>392.50 <b>(-20.40%)</b></td><td>249.70 (-5.92%)</td><td>709.07 (-4.85%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2090.60 (n/a)</td><td>770.02 (n/a)</td><td>493.10 (n/a)</td><td>265.40 (n/a)</td><td>745.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.22 (+18.27%)</td><td>0.11 (-18.05%)</td><td>0.11 <b>(-39.11%)</b></td><td>0.02 <b>(-64.94%)</b></td><td>0.07 <b>(+21.44%)</b></td><td>2092.40 <b>(+185.26%)</b></td><td>738.54 <b>(+73.39%)</b></td><td>453.70 <b>(+64.21%)</b></td><td>224.50 (-15.44%)</td><td>765.24 <b>(+250.97%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>733.50 (n/a)</td><td>425.94 (n/a)</td><td>276.30 (n/a)</td><td>265.50 (n/a)</td><td>218.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.17 (-16.80%)</td><td>0.12 (-11.97%)</td><td>0.10 <b>(-28.65%)</b></td><td>0.09 (+2.34%)</td><td>0.03 <b>(-32.02%)</b></td><td>543.70 (-2.30%)</td><td>425.66 (+7.53%)</td><td>472.30 <b>(+40.15%)</b></td><td>281.20 <b>(+20.17%)</b></td><td>107.72 <b>(-26.88%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>556.50 (n/a)</td><td>395.84 (n/a)</td><td>337.00 (n/a)</td><td>234.00 (n/a)</td><td>147.32 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.20 (-6.78%)</td><td>0.14 (-5.89%)</td><td>0.15 (-4.64%)</td><td>0.08 (-6.55%)</td><td>0.06 (-4.58%)</td><td>636.90 (+7.01%)</td><td>409.50 (+6.97%)</td><td>318.50 (+4.84%)</td><td>245.50 (+7.30%)</td><td>192.51 (+9.33%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>595.20 (n/a)</td><td>382.80 (n/a)</td><td>303.80 (n/a)</td><td>228.80 (n/a)</td><td>176.08 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 <b>(-36.61%)</b></td><td>0.07 <b>(-44.07%)</b></td><td>0.08 <b>(-36.68%)</b></td><td>0.02 <b>(-78.92%)</b></td><td>0.03 (-11.53%)</td><td>2437.10 <b>(+374.33%)</b></td><td>952.10 <b>(+139.34%)</b></td><td>618.60 <b>(+57.93%)</b></td><td>440.10 <b>(+57.74%)</b></td><td>836.72 <b>(+631.67%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>513.80 (n/a)</td><td>397.80 (n/a)</td><td>391.70 (n/a)</td><td>279.00 (n/a)</td><td>114.36 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.12 <b>(-43.47%)</b></td><td>0.10 <b>(-23.24%)</b></td><td>0.10 (+15.33%)</td><td>0.08 (+17.07%)</td><td>0.02 <b>(-74.67%)</b></td><td>624.60 (-14.58%)</td><td>523.08 (+8.70%)</td><td>487.80 (-13.28%)</td><td>424.90 <b>(+76.89%)</b></td><td>91.95 <b>(-57.98%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>731.20 (n/a)</td><td>481.20 (n/a)</td><td>562.50 (n/a)</td><td>240.20 (n/a)</td><td>218.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (-0.53%)</td><td>0.01 (-8.98%)</td><td>0.01 (-5.09%)</td><td>0.01 (-9.54%)</td><td>0.00 <b>(+29.90%)</b></td><td>484.90 (+10.53%)</td><td>355.48 (+12.54%)</td><td>305.90 (+5.37%)</td><td>270.40 (+0.52%)</td><td>96.44 <b>(+38.90%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>438.70 (n/a)</td><td>315.88 (n/a)</td><td>290.30 (n/a)</td><td>269.00 (n/a)</td><td>69.43 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 <b>(-21.75%)</b></td><td>0.01 (+19.45%)</td><td>0.01 <b>(+54.68%)</b></td><td>0.01 <b>(+21.18%)</b></td><td>0.00 <b>(-42.77%)</b></td><td>493.10 (-17.47%)</td><td>356.42 <b>(-23.21%)</b></td><td>310.90 <b>(-35.35%)</b></td><td>273.40 <b>(+27.82%)</b></td><td>95.78 <b>(-37.68%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>597.50 (n/a)</td><td>464.14 (n/a)</td><td>480.90 (n/a)</td><td>213.90 (n/a)</td><td>153.70 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 <b>(+87.37%)</b></td><td>0.01 <b>(+61.90%)</b></td><td>0.01 (+11.05%)</td><td>0.00 <b>(+330.30%)</b></td><td>0.00 <b>(+20.02%)</b></td><td>557.20 <b>(-76.76%)</b></td><td>431.20 <b>(-53.36%)</b></td><td>476.40 (-9.94%)</td><td>273.70 <b>(-46.64%)</b></td><td>118.83 <b>(-85.61%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2397.50 (n/a)</td><td>924.58 (n/a)</td><td>529.00 (n/a)</td><td>512.90 (n/a)</td><td>825.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 <b>(-34.75%)</b></td><td>0.01 (-2.63%)</td><td>0.01 <b>(+22.91%)</b></td><td>0.00 (+18.66%)</td><td>0.00 <b>(-65.84%)</b></td><td>533.90 (-15.72%)</td><td>447.26 (-9.98%)</td><td>447.80 (-18.64%)</td><td>333.10 <b>(+53.29%)</b></td><td>76.49 <b>(-55.50%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>633.50 (n/a)</td><td>496.82 (n/a)</td><td>550.40 (n/a)</td><td>217.30 (n/a)</td><td>171.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (+1.67%)</td><td>0.01 (+5.29%)</td><td>0.01 (+9.11%)</td><td>0.00 (-10.77%)</td><td>0.00 (+16.65%)</td><td>531.20 (+12.07%)</td><td>381.62 (-1.99%)</td><td>394.50 (-8.34%)</td><td>232.80 (-1.61%)</td><td>123.51 <b>(+32.61%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>474.00 (n/a)</td><td>389.38 (n/a)</td><td>430.40 (n/a)</td><td>236.60 (n/a)</td><td>93.14 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (-8.83%)</td><td>0.01 (-11.37%)</td><td>0.01 (-8.71%)</td><td>0.00 <b>(-21.39%)</b></td><td>0.00 (+0.85%)</td><td>695.80 <b>(+27.20%)</b></td><td>516.10 (+15.25%)</td><td>511.30 (+9.53%)</td><td>309.40 (+9.68%)</td><td>145.48 <b>(+42.20%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>547.00 (n/a)</td><td>447.82 (n/a)</td><td>466.80 (n/a)</td><td>282.10 (n/a)</td><td>102.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 <b>(-23.10%)</b></td><td>0.01 (-13.19%)</td><td>0.01 (+0.53%)</td><td>0.01 (-5.69%)</td><td>0.00 <b>(-40.74%)</b></td><td>461.10 (+6.02%)</td><td>374.24 (+10.87%)</td><td>353.90 (-0.51%)</td><td>265.40 <b>(+30.03%)</b></td><td>78.04 (-17.92%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>434.90 (n/a)</td><td>337.56 (n/a)</td><td>355.70 (n/a)</td><td>204.10 (n/a)</td><td>95.08 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 <b>(+65.48%)</b></td><td>0.02 <b>(+37.42%)</b></td><td>0.02 <b>(+50.65%)</b></td><td>0.01 (+9.72%)</td><td>0.01 <b>(+88.24%)</b></td><td>427.70 (-8.86%)</td><td>292.70 <b>(-23.78%)</b></td><td>302.90 <b>(-33.62%)</b></td><td>146.50 <b>(-39.59%)</b></td><td>100.09 (-7.32%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>469.30 (n/a)</td><td>384.00 (n/a)</td><td>456.30 (n/a)</td><td>242.50 (n/a)</td><td>107.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (-15.35%)</td><td>0.01 (+11.56%)</td><td>0.02 <b>(+53.76%)</b></td><td>0.01 (-8.46%)</td><td>0.00 <b>(-22.73%)</b></td><td>579.70 (+9.23%)</td><td>378.58 (-12.04%)</td><td>310.10 <b>(-34.96%)</b></td><td>272.30 (+18.13%)</td><td>126.69 (+2.58%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>530.70 (n/a)</td><td>430.40 (n/a)</td><td>476.80 (n/a)</td><td>230.50 (n/a)</td><td>123.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 <b>(-26.65%)</b></td><td>0.01 <b>(-32.13%)</b></td><td>0.01 <b>(-51.51%)</b></td><td>0.01 (-0.77%)</td><td>0.00 <b>(-46.29%)</b></td><td>719.50 (+0.77%)</td><td>545.60 <b>(+31.76%)</b></td><td>581.80 <b>(+106.24%)</b></td><td>334.80 <b>(+36.32%)</b></td><td>167.36 <b>(-22.99%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>714.00 (n/a)</td><td>414.10 (n/a)</td><td>282.10 (n/a)</td><td>245.60 (n/a)</td><td>217.31 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (+17.33%)</td><td>0.01 (+7.32%)</td><td>0.01 <b>(+20.51%)</b></td><td>0.01 <b>(-47.26%)</b></td><td>0.01 <b>(+55.47%)</b></td><td>999.80 <b>(+89.64%)</b></td><td>479.90 (+11.57%)</td><td>425.90 (-17.01%)</td><td>224.50 (-14.77%)</td><td>309.10 <b>(+142.10%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>527.20 (n/a)</td><td>430.14 (n/a)</td><td>513.20 (n/a)</td><td>263.40 (n/a)</td><td>127.67 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 <b>(+57.49%)</b></td><td>0.01 <b>(+31.38%)</b></td><td>0.01 <b>(+21.36%)</b></td><td>0.01 (+0.40%)</td><td>0.00 <b>(+229.36%)</b></td><td>690.80 (-0.40%)</td><td>454.76 (-18.57%)</td><td>441.60 (-17.60%)</td><td>318.20 <b>(-36.51%)</b></td><td>151.72 <b>(+96.49%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>693.60 (n/a)</td><td>558.44 (n/a)</td><td>535.90 (n/a)</td><td>501.20 (n/a)</td><td>77.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (+2.04%)</td><td>0.03 (+7.91%)</td><td>0.04 (-0.38%)</td><td>0.03 <b>(+42.59%)</b></td><td>0.01 <b>(-30.46%)</b></td><td>376.20 <b>(-29.87%)</b></td><td>313.44 (-12.14%)</td><td>295.10 (+0.37%)</td><td>241.60 (-2.03%)</td><td>59.43 <b>(-50.84%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.40 (n/a)</td><td>356.74 (n/a)</td><td>294.00 (n/a)</td><td>246.60 (n/a)</td><td>120.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 <b>(+36.24%)</b></td><td>0.04 <b>(+28.09%)</b></td><td>0.04 <b>(+41.39%)</b></td><td>0.02 (-0.49%)</td><td>0.01 <b>(+88.76%)</b></td><td>464.20 (+0.48%)</td><td>327.98 (-17.32%)</td><td>292.90 <b>(-29.29%)</b></td><td>200.20 <b>(-26.61%)</b></td><td>108.68 <b>(+49.86%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>462.00 (n/a)</td><td>396.70 (n/a)</td><td>414.20 (n/a)</td><td>272.80 (n/a)</td><td>72.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 <b>(-28.65%)</b></td><td>0.03 (-0.80%)</td><td>0.04 <b>(+55.82%)</b></td><td>0.02 (+8.73%)</td><td>0.01 <b>(-43.63%)</b></td><td>508.20 (-8.03%)</td><td>354.86 (-7.81%)</td><td>289.10 <b>(-35.83%)</b></td><td>273.10 <b>(+40.12%)</b></td><td>107.93 <b>(-28.89%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>552.60 (n/a)</td><td>384.94 (n/a)</td><td>450.50 (n/a)</td><td>194.90 (n/a)</td><td>151.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (-17.72%)</td><td>0.03 (-12.66%)</td><td>0.03 (-14.88%)</td><td>0.02 (+9.30%)</td><td>0.01 <b>(-34.44%)</b></td><td>479.90 (-8.52%)</td><td>368.86 (+6.47%)</td><td>354.60 (+17.50%)</td><td>235.80 <b>(+21.55%)</b></td><td>107.85 <b>(-26.43%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>524.60 (n/a)</td><td>346.44 (n/a)</td><td>301.80 (n/a)</td><td>194.00 (n/a)</td><td>146.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (-19.09%)</td><td>0.03 (+14.07%)</td><td>0.04 <b>(+55.09%)</b></td><td>0.03 <b>(+70.43%)</b></td><td>0.01 <b>(-64.92%)</b></td><td>364.80 <b>(-41.32%)</b></td><td>306.52 <b>(-26.55%)</b></td><td>291.10 <b>(-35.51%)</b></td><td>257.30 <b>(+23.58%)</b></td><td>49.17 <b>(-73.84%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>621.70 (n/a)</td><td>417.32 (n/a)</td><td>451.40 (n/a)</td><td>208.20 (n/a)</td><td>187.96 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 <b>(+21.89%)</b></td><td>0.02 (+3.64%)</td><td>0.02 (-6.58%)</td><td>0.02 <b>(+23.07%)</b></td><td>0.01 (+16.65%)</td><td>605.20 (-18.74%)</td><td>486.70 (-4.46%)</td><td>513.10 (+7.05%)</td><td>283.50 (-17.97%)</td><td>122.40 <b>(-25.60%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>744.80 (n/a)</td><td>509.44 (n/a)</td><td>479.30 (n/a)</td><td>345.60 (n/a)</td><td>164.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (+19.99%)</td><td>0.07 (+18.25%)</td><td>0.07 <b>(+24.71%)</b></td><td>0.03 <b>(-29.03%)</b></td><td>0.02 <b>(+79.69%)</b></td><td>737.60 <b>(+40.90%)</b></td><td>373.88 (-5.41%)</td><td>282.50 (-19.81%)</td><td>253.30 (-16.68%)</td><td>204.46 <b>(+123.48%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>523.50 (n/a)</td><td>395.28 (n/a)</td><td>352.30 (n/a)</td><td>304.00 (n/a)</td><td>91.49 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (+1.04%)</td><td>0.06 (+18.77%)</td><td>0.06 (+15.75%)</td><td>0.05 <b>(+318.70%)</b></td><td>0.01 <b>(-52.49%)</b></td><td>453.00 <b>(-76.12%)</b></td><td>368.18 <b>(-44.84%)</b></td><td>337.70 (-13.61%)</td><td>301.30 (-1.02%)</td><td>69.92 <b>(-89.84%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1896.80 (n/a)</td><td>667.50 (n/a)</td><td>390.90 (n/a)</td><td>304.40 (n/a)</td><td>688.18 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (-0.55%)</td><td>0.05 (-12.35%)</td><td>0.05 <b>(-25.81%)</b></td><td>0.03 <b>(-24.79%)</b></td><td>0.02 (+2.04%)</td><td>644.30 <b>(+32.96%)</b></td><td>430.62 (+16.14%)</td><td>439.40 <b>(+34.79%)</b></td><td>276.40 (+0.58%)</td><td>138.45 <b>(+32.12%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>484.60 (n/a)</td><td>370.78 (n/a)</td><td>326.00 (n/a)</td><td>274.80 (n/a)</td><td>104.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 <b>(-29.16%)</b></td><td>0.04 <b>(-25.45%)</b></td><td>0.04 (-18.06%)</td><td>0.01 <b>(-66.63%)</b></td><td>0.02 (-5.55%)</td><td>1930.10 <b>(+199.66%)</b></td><td>734.44 <b>(+79.00%)</b></td><td>495.40 <b>(+22.05%)</b></td><td>317.90 <b>(+41.16%)</b></td><td>677.06 <b>(+327.62%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>644.10 (n/a)</td><td>410.30 (n/a)</td><td>405.90 (n/a)</td><td>225.20 (n/a)</td><td>158.33 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 <b>(-31.03%)</b></td><td>0.05 (-5.83%)</td><td>0.05 <b>(+28.91%)</b></td><td>0.03 <b>(+191.16%)</b></td><td>0.02 <b>(-61.06%)</b></td><td>640.10 <b>(-65.66%)</b></td><td>427.02 <b>(-37.75%)</b></td><td>390.90 <b>(-22.43%)</b></td><td>280.70 <b>(+44.99%)</b></td><td>135.69 <b>(-80.11%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1863.80 (n/a)</td><td>685.94 (n/a)</td><td>503.90 (n/a)</td><td>193.60 (n/a)</td><td>682.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 <b>(+44.49%)</b></td><td>0.04 (-9.63%)</td><td>0.04 (+2.06%)</td><td>0.01 <b>(-63.48%)</b></td><td>0.03 <b>(+170.41%)</b></td><td>2508.60 <b>(+173.77%)</b></td><td>1162.24 <b>(+101.96%)</b></td><td>493.20 (-2.03%)</td><td>296.20 <b>(-30.78%)</b></td><td>1031.45 <b>(+431.08%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>916.30 (n/a)</td><td>575.48 (n/a)</td><td>503.40 (n/a)</td><td>427.90 (n/a)</td><td>194.22 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1110.00 (n/a)</td><td>514.62 (n/a)</td><td>441.30 (n/a)</td><td>287.70 (n/a)</td><td>341.47 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>485.40 (n/a)</td><td>293.46 (n/a)</td><td>238.80 (n/a)</td><td>224.80 (n/a)</td><td>110.11 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1349.00 (n/a)</td><td>529.40 (n/a)</td><td>315.70 (n/a)</td><td>268.60 (n/a)</td><td>461.94 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>457.50 (n/a)</td><td>309.26 (n/a)</td><td>267.20 (n/a)</td><td>243.50 (n/a)</td><td>90.36 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>522.80 (n/a)</td><td>344.50 (n/a)</td><td>285.80 (n/a)</td><td>201.50 (n/a)</td><td>142.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2433.70 (n/a)</td><td>893.58 (n/a)</td><td>496.80 (n/a)</td><td>481.30 (n/a)</td><td>861.74 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>559.50 (n/a)</td><td>376.52 (n/a)</td><td>353.10 (n/a)</td><td>249.30 (n/a)</td><td>126.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>596.40 (n/a)</td><td>404.14 (n/a)</td><td>344.80 (n/a)</td><td>281.20 (n/a)</td><td>141.54 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>812.60 (n/a)</td><td>441.40 (n/a)</td><td>378.80 (n/a)</td><td>261.90 (n/a)</td><td>225.97 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.21 (-2.58%)</td><td>0.14 (+19.61%)</td><td>0.16 <b>(+59.83%)</b></td><td>0.02 <b>(-66.50%)</b></td><td>0.08 <b>(+36.35%)</b></td><td>1967.10 <b>(+198.54%)</b></td><td>637.08 <b>(+35.11%)</b></td><td>302.40 <b>(-37.44%)</b></td><td>236.20 (+2.65%)</td><td>747.60 <b>(+370.61%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>658.90 (n/a)</td><td>471.52 (n/a)</td><td>483.40 (n/a)</td><td>230.10 (n/a)</td><td>158.86 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1892.80 (n/a)</td><td>662.46 (n/a)</td><td>273.90 (n/a)</td><td>267.10 (n/a)</td><td>703.54 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>609.60 (n/a)</td><td>422.70 (n/a)</td><td>437.60 (n/a)</td><td>295.90 (n/a)</td><td>130.12 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>486.30 (n/a)</td><td>322.70 (n/a)</td><td>292.00 (n/a)</td><td>263.40 (n/a)</td><td>92.22 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.50 (n/a)</td><td>471.42 (n/a)</td><td>554.10 (n/a)</td><td>236.30 (n/a)</td><td>140.74 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.50 (n/a)</td><td>456.80 (n/a)</td><td>554.90 (n/a)</td><td>274.40 (n/a)</td><td>166.14 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>630.80 (n/a)</td><td>487.58 (n/a)</td><td>544.40 (n/a)</td><td>212.20 (n/a)</td><td>160.75 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1982.60 (n/a)</td><td>796.38 (n/a)</td><td>524.00 (n/a)</td><td>384.60 (n/a)</td><td>666.82 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>630.50 (n/a)</td><td>427.22 (n/a)</td><td>436.80 (n/a)</td><td>255.20 (n/a)</td><td>167.84 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>534.90 (n/a)</td><td>433.10 (n/a)</td><td>458.00 (n/a)</td><td>300.40 (n/a)</td><td>90.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>519.40 (n/a)</td><td>365.40 (n/a)</td><td>342.60 (n/a)</td><td>239.70 (n/a)</td><td>129.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>545.50 (n/a)</td><td>418.00 (n/a)</td><td>444.50 (n/a)</td><td>273.20 (n/a)</td><td>121.77 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>2041.20 (n/a)</td><td>799.70 (n/a)</td><td>487.50 (n/a)</td><td>480.50 (n/a)</td><td>694.08 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1886.90 (n/a)</td><td>776.86 (n/a)</td><td>535.00 (n/a)</td><td>421.10 (n/a)</td><td>623.57 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.98 <b>(-25.32%)</b></td><td>2.30 (-6.30%)</td><td>2.30 (+1.62%)</td><td>1.60 (+2.07%)</td><td>0.49 <b>(-48.59%)</b></td><td>6560.90 (-2.03%)</td><td>4738.86 (-0.00%)</td><td>4560.90 (-1.59%)</td><td>3518.50 <b>(+33.91%)</b></td><td>1112.80 <b>(-29.70%)</b></td><td>1220.66 <b>(-25.32%)</b></td><td>943.11 (-6.30%)</td><td>941.70 (+1.62%)</td><td>654.63 (+2.07%)</td><td>200.83 <b>(-48.59%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.99 (n/a)</td><td>2.46 (n/a)</td><td>2.26 (n/a)</td><td>1.57 (n/a)</td><td>0.95 (n/a)</td><td>6696.70 (n/a)</td><td>4738.96 (n/a)</td><td>4634.80 (n/a)</td><td>2627.60 (n/a)</td><td>1582.83 (n/a)</td><td>1634.57 (n/a)</td><td>1006.47 (n/a)</td><td>926.68 (n/a)</td><td>641.36 (n/a)</td><td>390.69 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.58 <b>(-29.92%)</b></td><td>2.45 (-16.83%)</td><td>2.56 (-10.44%)</td><td>2.11 (-6.99%)</td><td>0.20 <b>(-60.97%)</b></td><td>11179.20 (+7.52%)</td><td>9669.32 (+18.04%)</td><td>9208.40 (+11.65%)</td><td>9143.00 <b>(+42.69%)</b></td><td>864.85 <b>(-40.20%)</b></td><td>1467.98 <b>(-29.92%)</b></td><td>1396.16 (-16.83%)</td><td>1457.56 (-10.44%)</td><td>1200.60 (-6.99%)</td><td>113.02 <b>(-60.97%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.68 (n/a)</td><td>2.95 (n/a)</td><td>2.86 (n/a)</td><td>2.27 (n/a)</td><td>0.51 (n/a)</td><td>10397.70 (n/a)</td><td>8191.72 (n/a)</td><td>8247.30 (n/a)</td><td>6407.70 (n/a)</td><td>1446.32 (n/a)</td><td>2094.62 (n/a)</td><td>1678.71 (n/a)</td><td>1627.42 (n/a)</td><td>1290.84 (n/a)</td><td>289.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.75 <b>(-22.21%)</b></td><td>2.43 <b>(-20.68%)</b></td><td>2.31 <b>(-23.91%)</b></td><td>2.18 <b>(-22.50%)</b></td><td>0.25 (-13.67%)</td><td>7711.20 <b>(+29.03%)</b></td><td>6954.56 <b>(+26.27%)</b></td><td>7276.20 <b>(+31.42%)</b></td><td>6094.70 <b>(+28.56%)</b></td><td>696.22 <b>(+42.64%)</b></td><td>1409.41 <b>(-22.21%)</b></td><td>1245.41 <b>(-20.68%)</b></td><td>1180.55 <b>(-23.91%)</b></td><td>1113.96 <b>(-22.50%)</b></td><td>128.33 (-13.67%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.54 (n/a)</td><td>3.07 (n/a)</td><td>3.03 (n/a)</td><td>2.81 (n/a)</td><td>0.29 (n/a)</td><td>5976.20 (n/a)</td><td>5507.56 (n/a)</td><td>5536.40 (n/a)</td><td>4740.90 (n/a)</td><td>488.10 (n/a)</td><td>1811.86 (n/a)</td><td>1570.18 (n/a)</td><td>1551.55 (n/a)</td><td>1437.36 (n/a)</td><td>148.66 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.98 (+17.44%)</td><td>0.71 (+18.02%)</td><td>0.63 (-4.10%)</td><td>0.51 <b>(+284.92%)</b></td><td>0.19 <b>(-32.87%)</b></td><td>901.40 <b>(-74.02%)</b></td><td>682.76 <b>(-43.77%)</b></td><td>730.70 (+4.28%)</td><td>468.30 (-14.84%)</td><td>167.67 <b>(-86.73%)</b></td><td>71.66 (+17.44%)</td><td>51.76 (+18.02%)</td><td>45.92 (-4.10%)</td><td>37.23 <b>(+284.92%)</b></td><td>13.56 <b>(-32.87%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.83 (n/a)</td><td>0.60 (n/a)</td><td>0.65 (n/a)</td><td>0.13 (n/a)</td><td>0.28 (n/a)</td><td>3469.50 (n/a)</td><td>1214.16 (n/a)</td><td>700.70 (n/a)</td><td>549.90 (n/a)</td><td>1263.36 (n/a)</td><td>61.02 (n/a)</td><td>43.86 (n/a)</td><td>47.88 (n/a)</td><td>9.67 (n/a)</td><td>20.20 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.26 (-1.33%)</td><td>0.97 (-0.89%)</td><td>0.91 (-0.25%)</td><td>0.56 (-14.39%)</td><td>0.28 (+12.72%)</td><td>1171.30 (+16.81%)</td><td>735.72 (+3.71%)</td><td>719.70 (+0.25%)</td><td>520.10 (+1.36%)</td><td>261.97 <b>(+35.19%)</b></td><td>129.04 (-1.33%)</td><td>99.20 (-0.89%)</td><td>93.25 (-0.25%)</td><td>57.29 (-14.39%)</td><td>28.93 (+12.71%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.28 (n/a)</td><td>0.98 (n/a)</td><td>0.91 (n/a)</td><td>0.65 (n/a)</td><td>0.25 (n/a)</td><td>1002.70 (n/a)</td><td>709.38 (n/a)</td><td>717.90 (n/a)</td><td>513.10 (n/a)</td><td>193.78 (n/a)</td><td>130.78 (n/a)</td><td>100.09 (n/a)</td><td>93.48 (n/a)</td><td>66.93 (n/a)</td><td>25.66 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.35 (-5.95%)</td><td>1.18 (+1.33%)</td><td>1.32 <b>(+26.31%)</b></td><td>0.90 (-8.38%)</td><td>0.22 (+5.69%)</td><td>840.20 (+9.13%)</td><td>660.80 (-0.69%)</td><td>572.80 <b>(-20.83%)</b></td><td>560.10 (+6.32%)</td><td>133.10 <b>(+20.18%)</b></td><td>149.76 (-5.95%)</td><td>130.84 (+1.33%)</td><td>146.45 <b>(+26.31%)</b></td><td>99.84 (-8.38%)</td><td>24.24 (+5.69%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.43 (n/a)</td><td>1.16 (n/a)</td><td>1.04 (n/a)</td><td>0.98 (n/a)</td><td>0.21 (n/a)</td><td>769.90 (n/a)</td><td>665.38 (n/a)</td><td>723.50 (n/a)</td><td>526.80 (n/a)</td><td>110.74 (n/a)</td><td>159.23 (n/a)</td><td>129.12 (n/a)</td><td>115.94 (n/a)</td><td>108.96 (n/a)</td><td>22.93 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.34 (-15.05%)</td><td>0.87 <b>(-28.14%)</b></td><td>1.13 <b>(-23.60%)</b></td><td>0.30 <b>(-37.33%)</b></td><td>0.48 (+2.69%)</td><td>3539.40 <b>(+59.57%)</b></td><td>1727.06 <b>(+62.76%)</b></td><td>931.20 <b>(+30.88%)</b></td><td>781.20 (+17.70%)</td><td>1232.14 <b>(+86.28%)</b></td><td>171.80 (-15.05%)</td><td>111.44 <b>(-28.14%)</b></td><td>144.14 <b>(-23.60%)</b></td><td>37.92 <b>(-37.33%)</b></td><td>60.93 (+2.69%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.58 (n/a)</td><td>1.21 (n/a)</td><td>1.47 (n/a)</td><td>0.47 (n/a)</td><td>0.46 (n/a)</td><td>2218.10 (n/a)</td><td>1061.14 (n/a)</td><td>711.50 (n/a)</td><td>663.70 (n/a)</td><td>661.45 (n/a)</td><td>202.23 (n/a)</td><td>155.07 (n/a)</td><td>188.65 (n/a)</td><td>60.51 (n/a)</td><td>59.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.05 (-11.91%)</td><td>1.51 (-2.21%)</td><td>1.71 <b>(+28.64%)</b></td><td>0.93 <b>(-27.19%)</b></td><td>0.48 (+7.41%)</td><td>1126.60 <b>(+37.34%)</b></td><td>764.46 (+6.67%)</td><td>613.40 <b>(-22.26%)</b></td><td>511.10 (+13.53%)</td><td>269.42 <b>(+76.05%)</b></td><td>262.60 (-11.91%)</td><td>192.64 (-2.21%)</td><td>218.83 <b>(+28.64%)</b></td><td>119.13 <b>(-27.19%)</b></td><td>61.32 (+7.41%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>2.33 (n/a)</td><td>1.54 (n/a)</td><td>1.33 (n/a)</td><td>1.28 (n/a)</td><td>0.45 (n/a)</td><td>820.30 (n/a)</td><td>716.68 (n/a)</td><td>789.00 (n/a)</td><td>450.20 (n/a)</td><td>153.03 (n/a)</td><td>298.10 (n/a)</td><td>196.99 (n/a)</td><td>170.11 (n/a)</td><td>163.63 (n/a)</td><td>57.09 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.86 (+0.96%)</td><td>1.20 (+1.81%)</td><td>1.30 (-1.11%)</td><td>0.29 <b>(-29.41%)</b></td><td>0.57 (+7.51%)</td><td>3588.70 <b>(+41.67%)</b></td><td>1319.32 (+14.92%)</td><td>809.20 (+1.12%)</td><td>563.60 (-0.95%)</td><td>1273.38 <b>(+60.34%)</b></td><td>238.16 (+0.96%)</td><td>154.00 (+1.81%)</td><td>165.86 (-1.11%)</td><td>37.40 <b>(-29.41%)</b></td><td>72.58 (+7.51%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.84 (n/a)</td><td>1.18 (n/a)</td><td>1.31 (n/a)</td><td>0.41 (n/a)</td><td>0.53 (n/a)</td><td>2533.20 (n/a)</td><td>1148.02 (n/a)</td><td>800.20 (n/a)</td><td>569.00 (n/a)</td><td>794.15 (n/a)</td><td>235.89 (n/a)</td><td>151.26 (n/a)</td><td>167.72 (n/a)</td><td>52.98 (n/a)</td><td>67.51 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.68 (+2.16%)</td><td>1.17 <b>(-20.99%)</b></td><td>1.20 <b>(-21.36%)</b></td><td>0.29 <b>(-75.65%)</b></td><td>0.55 <b>(+217.57%)</b></td><td>3614.90 <b>(+310.60%)</b></td><td>1346.98 <b>(+88.03%)</b></td><td>872.70 <b>(+27.16%)</b></td><td>622.70 (-2.12%)</td><td>1276.05 <b>(+1234.80%)</b></td><td>215.53 (+2.16%)</td><td>149.90 <b>(-20.99%)</b></td><td>153.80 <b>(-21.36%)</b></td><td>37.13 <b>(-75.65%)</b></td><td>70.95 <b>(+217.57%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.65 (n/a)</td><td>1.48 (n/a)</td><td>1.53 (n/a)</td><td>1.19 (n/a)</td><td>0.17 (n/a)</td><td>880.40 (n/a)</td><td>716.36 (n/a)</td><td>686.30 (n/a)</td><td>636.20 (n/a)</td><td>95.60 (n/a)</td><td>210.97 (n/a)</td><td>189.74 (n/a)</td><td>195.57 (n/a)</td><td>152.45 (n/a)</td><td>22.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.64 (-7.98%)</td><td>1.04 <b>(-21.03%)</b></td><td>1.00 <b>(-23.17%)</b></td><td>0.33 <b>(-35.24%)</b></td><td>0.53 (+4.84%)</td><td>3198.10 <b>(+54.41%)</b></td><td>1393.54 <b>(+42.38%)</b></td><td>1047.10 <b>(+30.16%)</b></td><td>640.40 (+8.67%)</td><td>1048.84 <b>(+69.39%)</b></td><td>209.59 (-7.98%)</td><td>132.99 <b>(-21.03%)</b></td><td>128.18 <b>(-23.17%)</b></td><td>41.97 <b>(-35.24%)</b></td><td>67.57 (+4.84%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.78 (n/a)</td><td>1.32 (n/a)</td><td>1.30 (n/a)</td><td>0.51 (n/a)</td><td>0.50 (n/a)</td><td>2071.20 (n/a)</td><td>978.78 (n/a)</td><td>804.50 (n/a)</td><td>589.30 (n/a)</td><td>619.17 (n/a)</td><td>227.77 (n/a)</td><td>168.40 (n/a)</td><td>166.84 (n/a)</td><td>64.80 (n/a)</td><td>64.46 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.36 (+6.30%)</td><td>0.86 (-4.12%)</td><td>0.83 (-11.21%)</td><td>0.43 (-10.03%)</td><td>0.43 <b>(+24.31%)</b></td><td>2446.00 (+11.15%)</td><td>1514.62 (+13.31%)</td><td>1258.20 (+12.62%)</td><td>768.30 (-5.93%)</td><td>782.97 <b>(+34.43%)</b></td><td>174.69 (+6.30%)</td><td>110.51 (-4.12%)</td><td>106.67 (-11.21%)</td><td>54.87 (-10.03%)</td><td>54.57 <b>(+24.31%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.28 (n/a)</td><td>0.90 (n/a)</td><td>0.94 (n/a)</td><td>0.48 (n/a)</td><td>0.34 (n/a)</td><td>2200.70 (n/a)</td><td>1336.70 (n/a)</td><td>1117.20 (n/a)</td><td>816.70 (n/a)</td><td>582.42 (n/a)</td><td>164.34 (n/a)</td><td>115.26 (n/a)</td><td>120.14 (n/a)</td><td>60.99 (n/a)</td><td>43.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.81 (-3.97%)</td><td>0.60 (-3.68%)</td><td>0.59 (+0.25%)</td><td>0.44 (+5.29%)</td><td>0.15 (-12.82%)</td><td>826.40 (-5.03%)</td><td>627.10 (+2.36%)</td><td>612.20 (-0.24%)</td><td>445.30 (+4.14%)</td><td>153.78 (-12.27%)</td><td>37.68 (-3.97%)</td><td>28.10 (-3.68%)</td><td>27.41 (+0.25%)</td><td>20.30 (+5.29%)</td><td>6.99 (-12.82%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.84 (n/a)</td><td>0.63 (n/a)</td><td>0.59 (n/a)</td><td>0.41 (n/a)</td><td>0.17 (n/a)</td><td>870.20 (n/a)</td><td>612.64 (n/a)</td><td>613.70 (n/a)</td><td>427.60 (n/a)</td><td>175.29 (n/a)</td><td>39.23 (n/a)</td><td>29.18 (n/a)</td><td>27.34 (n/a)</td><td>19.28 (n/a)</td><td>8.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.63 (-12.88%)</td><td>1.81 <b>(+22.79%)</b></td><td>1.69 <b>(+52.42%)</b></td><td>1.00 (-1.08%)</td><td>0.80 (-8.27%)</td><td>4195.80 (+1.09%)</td><td>2751.28 (-18.72%)</td><td>2480.70 <b>(-34.39%)</b></td><td>1592.50 (+14.77%)</td><td>1237.00 (+9.64%)</td><td>674.24 (-12.88%)</td><td>462.08 <b>(+22.79%)</b></td><td>432.83 <b>(+52.42%)</b></td><td>255.91 (-1.08%)</td><td>204.14 (-8.27%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.02 (n/a)</td><td>1.47 (n/a)</td><td>1.11 (n/a)</td><td>1.01 (n/a)</td><td>0.87 (n/a)</td><td>4150.70 (n/a)</td><td>3384.76 (n/a)</td><td>3781.10 (n/a)</td><td>1387.50 (n/a)</td><td>1128.20 (n/a)</td><td>773.89 (n/a)</td><td>376.31 (n/a)</td><td>283.98 (n/a)</td><td>258.69 (n/a)</td><td>222.54 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.37 (-15.05%)</td><td>1.71 <b>(-48.53%)</b></td><td>1.29 <b>(-63.39%)</b></td><td>1.07 <b>(-49.70%)</b></td><td>0.96 <b>(+37.12%)</b></td><td>2457.30 <b>(+98.81%)</b></td><td>1831.56 <b>(+121.30%)</b></td><td>2026.00 <b>(+173.16%)</b></td><td>777.80 (+17.72%)</td><td>692.20 <b>(+199.00%)</b></td><td>690.21 (-15.05%)</td><td>350.28 <b>(-48.53%)</b></td><td>264.99 <b>(-63.39%)</b></td><td>218.48 <b>(-49.70%)</b></td><td>197.12 <b>(+37.12%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.97 (n/a)</td><td>3.32 (n/a)</td><td>3.53 (n/a)</td><td>2.12 (n/a)</td><td>0.70 (n/a)</td><td>1236.00 (n/a)</td><td>827.62 (n/a)</td><td>741.70 (n/a)</td><td>660.70 (n/a)</td><td>231.51 (n/a)</td><td>812.54 (n/a)</td><td>680.60 (n/a)</td><td>723.79 (n/a)</td><td>434.37 (n/a)</td><td>143.76 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.69 (-16.99%)</td><td>2.57 (-4.28%)</td><td>2.58 (-11.06%)</td><td>2.46 <b>(+41.77%)</b></td><td>0.10 <b>(-84.42%)</b></td><td>3191.80 <b>(-29.46%)</b></td><td>3059.18 (-0.84%)</td><td>3048.50 (+12.43%)</td><td>2925.80 <b>(+20.47%)</b></td><td>115.89 <b>(-86.71%)</b></td><td>825.74 (-16.99%)</td><td>790.64 (-4.28%)</td><td>792.50 (-11.06%)</td><td>756.91 <b>(+41.77%)</b></td><td>29.93 <b>(-84.41%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.24 (n/a)</td><td>2.69 (n/a)</td><td>2.90 (n/a)</td><td>1.74 (n/a)</td><td>0.63 (n/a)</td><td>4525.00 (n/a)</td><td>3085.10 (n/a)</td><td>2711.40 (n/a)</td><td>2428.60 (n/a)</td><td>872.28 (n/a)</td><td>994.78 (n/a)</td><td>825.96 (n/a)</td><td>891.02 (n/a)</td><td>533.91 (n/a)</td><td>192.05 (n/a)</td>
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


### test_gemm_tile_options[tn128-ma32-default]

_No metrics available._


### test_gemm_tile_options[tn128-ma32]

_No metrics available._


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn128-ma64]

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


### test_gemm_tile_options[tn64-ma16]

_No metrics available._


### test_gemm_tile_options[tn64-ma32-default]

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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>465.80 (n/a)</td><td>357.74 (n/a)</td><td>299.00 (n/a)</td><td>268.60 (n/a)</td><td>95.22 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1059.30 (n/a)</td><td>496.80 (n/a)</td><td>472.60 (n/a)</td><td>216.30 (n/a)</td><td>338.22 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>595.60 (n/a)</td><td>490.12 (n/a)</td><td>544.00 (n/a)</td><td>222.70 (n/a)</td><td>154.41 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>587.30 (n/a)</td><td>447.04 (n/a)</td><td>491.30 (n/a)</td><td>206.60 (n/a)</td><td>142.88 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.30 (n/a)</td><td>466.34 (n/a)</td><td>489.10 (n/a)</td><td>308.40 (n/a)</td><td>104.33 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>680.10 (n/a)</td><td>491.86 (n/a)</td><td>489.00 (n/a)</td><td>351.40 (n/a)</td><td>131.29 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>516.80 (n/a)</td><td>370.48 (n/a)</td><td>336.70 (n/a)</td><td>304.30 (n/a)</td><td>88.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1050.90 (n/a)</td><td>632.90 (n/a)</td><td>570.20 (n/a)</td><td>391.80 (n/a)</td><td>254.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.40 (n/a)</td><td>374.32 (n/a)</td><td>299.90 (n/a)</td><td>230.30 (n/a)</td><td>164.24 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>698.00 (n/a)</td><td>392.60 (n/a)</td><td>318.00 (n/a)</td><td>272.20 (n/a)</td><td>174.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.10 (n/a)</td><td>436.64 (n/a)</td><td>433.50 (n/a)</td><td>262.70 (n/a)</td><td>120.56 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>602.10 (n/a)</td><td>426.28 (n/a)</td><td>370.90 (n/a)</td><td>341.40 (n/a)</td><td>111.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>567.70 (n/a)</td><td>388.12 (n/a)</td><td>355.00 (n/a)</td><td>274.50 (n/a)</td><td>110.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>455.00 (n/a)</td><td>286.88 (n/a)</td><td>253.40 (n/a)</td><td>214.50 (n/a)</td><td>97.26 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>560.10 (n/a)</td><td>390.88 (n/a)</td><td>441.60 (n/a)</td><td>184.30 (n/a)</td><td>164.38 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>592.50 (n/a)</td><td>395.46 (n/a)</td><td>375.70 (n/a)</td><td>200.40 (n/a)</td><td>164.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>561.10 (n/a)</td><td>366.52 (n/a)</td><td>320.10 (n/a)</td><td>204.90 (n/a)</td><td>146.60 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1010.60 (n/a)</td><td>571.34 (n/a)</td><td>461.50 (n/a)</td><td>265.70 (n/a)</td><td>288.06 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>702.50 (n/a)</td><td>474.62 (n/a)</td><td>463.20 (n/a)</td><td>317.10 (n/a)</td><td>158.16 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>624.70 (n/a)</td><td>529.70 (n/a)</td><td>491.30 (n/a)</td><td>476.30 (n/a)</td><td>63.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>519.00 (n/a)</td><td>381.04 (n/a)</td><td>322.20 (n/a)</td><td>273.60 (n/a)</td><td>115.22 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>936.10 (n/a)</td><td>604.96 (n/a)</td><td>558.10 (n/a)</td><td>259.20 (n/a)</td><td>267.96 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>456.80 (n/a)</td><td>345.06 (n/a)</td><td>289.60 (n/a)</td><td>254.70 (n/a)</td><td>93.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>594.00 (n/a)</td><td>406.68 (n/a)</td><td>339.30 (n/a)</td><td>266.90 (n/a)</td><td>144.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.47 (-19.23%)</td><td>0.32 (-14.53%)</td><td>0.32 (-3.69%)</td><td>0.13 <b>(-29.36%)</b></td><td>0.12 (-18.04%)</td><td>1729.30 <b>(+41.57%)</b></td><td>837.76 <b>(+21.94%)</b></td><td>682.50 (+3.83%)</td><td>466.10 <b>(+23.80%)</b></td><td>506.74 <b>(+56.06%)</b></td><td>20.25 (-19.23%)</td><td>13.69 (-14.53%)</td><td>13.83 (-3.69%)</td><td>5.46 <b>(-29.36%)</b></td><td>5.33 (-18.04%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.59 (n/a)</td><td>0.38 (n/a)</td><td>0.34 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>1221.50 (n/a)</td><td>687.02 (n/a)</td><td>657.30 (n/a)</td><td>376.50 (n/a)</td><td>324.72 (n/a)</td><td>25.07 (n/a)</td><td>16.02 (n/a)</td><td>14.36 (n/a)</td><td>7.73 (n/a)</td><td>6.51 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.64 (-2.21%)</td><td>0.47 (-6.74%)</td><td>0.44 (-14.18%)</td><td>0.32 (+2.89%)</td><td>0.12 (-5.95%)</td><td>685.70 (-2.81%)</td><td>497.04 (+6.26%)</td><td>503.40 (+16.53%)</td><td>347.00 (+2.27%)</td><td>131.82 (-9.04%)</td><td>27.20 (-2.21%)</td><td>20.08 (-6.74%)</td><td>18.75 (-14.18%)</td><td>13.76 (+2.89%)</td><td>5.28 (-5.95%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.65 (n/a)</td><td>0.50 (n/a)</td><td>0.51 (n/a)</td><td>0.31 (n/a)</td><td>0.13 (n/a)</td><td>705.50 (n/a)</td><td>467.74 (n/a)</td><td>432.00 (n/a)</td><td>339.30 (n/a)</td><td>144.92 (n/a)</td><td>27.82 (n/a)</td><td>21.54 (n/a)</td><td>21.84 (n/a)</td><td>13.38 (n/a)</td><td>5.62 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.31 (+0.20%)</td><td>0.31 (+1.37%)</td><td>0.31 (+2.29%)</td><td>0.30 (+0.60%)</td><td>0.00 (-1.40%)</td><td>83798.80 (-0.59%)</td><td>82118.34 (-1.35%)</td><td>81858.00 (-2.24%)</td><td>81019.00 (-0.20%)</td><td>1195.69 (-2.08%)</td><td>212.05 (+0.20%)</td><td>209.24 (+1.37%)</td><td>209.87 (+2.29%)</td><td>205.01 (+0.60%)</td><td>3.03 (-1.40%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84297.90 (n/a)</td><td>83241.68 (n/a)</td><td>83730.80 (n/a)</td><td>81180.80 (n/a)</td><td>1221.07 (n/a)</td><td>211.62 (n/a)</td><td>206.42 (n/a)</td><td>205.18 (n/a)</td><td>203.80 (n/a)</td><td>3.07 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.17 (+1.99%)</td><td>1.14 (+4.25%)</td><td>1.15 (+1.81%)</td><td>1.12 (+13.82%)</td><td>0.02 <b>(-71.74%)</b></td><td>22470.80 (-12.14%)</td><td>22006.68 (-4.36%)</td><td>21951.20 (-1.78%)</td><td>21486.20 (-1.95%)</td><td>361.07 <b>(-75.85%)</b></td><td>799.58 (+1.99%)</td><td>780.83 (+4.25%)</td><td>782.64 (+1.81%)</td><td>764.54 (+13.82%)</td><td>12.86 <b>(-71.74%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.15 (n/a)</td><td>1.10 (n/a)</td><td>1.13 (n/a)</td><td>0.98 (n/a)</td><td>0.07 (n/a)</td><td>25575.80 (n/a)</td><td>23008.78 (n/a)</td><td>22348.50 (n/a)</td><td>21914.50 (n/a)</td><td>1495.17 (n/a)</td><td>783.95 (n/a)</td><td>749.03 (n/a)</td><td>768.73 (n/a)</td><td>671.72 (n/a)</td><td>45.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.80 (-0.31%)</td><td>0.79 (+0.51%)</td><td>0.80 (+0.12%)</td><td>0.78 (+4.05%)</td><td>0.01 <b>(-58.68%)</b></td><td>97159.80 (-3.89%)</td><td>95288.48 (-0.57%)</td><td>94823.10 (-0.12%)</td><td>94178.50 (+0.32%)</td><td>1182.81 <b>(-60.31%)</b></td><td>729.67 (-0.31%)</td><td>721.26 (+0.51%)</td><td>724.71 (+0.12%)</td><td>707.28 (+4.05%)</td><td>8.87 <b>(-58.68%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.80 (n/a)</td><td>0.75 (n/a)</td><td>0.02 (n/a)</td><td>101097.20 (n/a)</td><td>95833.52 (n/a)</td><td>94936.00 (n/a)</td><td>93882.60 (n/a)</td><td>2979.86 (n/a)</td><td>731.97 (n/a)</td><td>717.61 (n/a)</td><td>723.85 (n/a)</td><td>679.74 (n/a)</td><td>21.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.78 (+1.46%)</td><td>0.77 (+1.85%)</td><td>0.78 (+1.12%)</td><td>0.76 (+2.24%)</td><td>0.01 <b>(-38.29%)</b></td><td>98936.10 (-2.19%)</td><td>97454.66 (-1.83%)</td><td>97285.00 (-1.11%)</td><td>96420.80 (-1.44%)</td><td>962.58 <b>(-40.52%)</b></td><td>712.70 (+1.46%)</td><td>705.20 (+1.85%)</td><td>706.37 (+1.12%)</td><td>694.58 (+2.24%)</td><td>6.93 <b>(-38.29%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101148.70 (n/a)</td><td>99267.98 (n/a)</td><td>98379.10 (n/a)</td><td>97827.50 (n/a)</td><td>1618.22 (n/a)</td><td>702.46 (n/a)</td><td>692.41 (n/a)</td><td>698.52 (n/a)</td><td>679.39 (n/a)</td><td>11.23 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.90 (+1.43%)</td><td>0.89 (+1.57%)</td><td>0.89 (+1.91%)</td><td>0.87 (+0.49%)</td><td>0.01 <b>(+58.42%)</b></td><td>86350.70 (-0.49%)</td><td>84895.06 (-1.54%)</td><td>84710.70 (-1.88%)</td><td>84126.80 (-1.41%)</td><td>886.08 <b>(+55.61%)</b></td><td>816.86 (+1.43%)</td><td>809.53 (+1.57%)</td><td>811.23 (+1.91%)</td><td>795.82 (+0.49%)</td><td>8.37 <b>(+58.42%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>86772.20 (n/a)</td><td>86221.02 (n/a)</td><td>86332.90 (n/a)</td><td>85330.70 (n/a)</td><td>569.42 (n/a)</td><td>805.33 (n/a)</td><td>797.04 (n/a)</td><td>795.98 (n/a)</td><td>791.95 (n/a)</td><td>5.29 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>4.05 <b>(-28.06%)</b></td><td>3.14 (-17.63%)</td><td>3.24 (-9.13%)</td><td>2.17 (-1.15%)</td><td>0.93 <b>(-40.85%)</b></td><td>4113.10 (+1.17%)</td><td>3063.26 (+13.36%)</td><td>2754.70 (+10.04%)</td><td>2199.90 <b>(+39.01%)</b></td><td>953.52 (-15.28%)</td><td>244.05 <b>(-28.06%)</b></td><td>189.13 (-17.63%)</td><td>194.89 (-9.13%)</td><td>130.53 (-1.15%)</td><td>56.12 <b>(-40.85%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.63 (n/a)</td><td>3.81 (n/a)</td><td>3.56 (n/a)</td><td>2.19 (n/a)</td><td>1.58 (n/a)</td><td>4065.60 (n/a)</td><td>2702.18 (n/a)</td><td>2503.30 (n/a)</td><td>1582.50 (n/a)</td><td>1125.51 (n/a)</td><td>339.26 (n/a)</td><td>229.61 (n/a)</td><td>214.47 (n/a)</td><td>132.05 (n/a)</td><td>94.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>4.69 (-3.28%)</td><td>2.89 (-11.49%)</td><td>2.07 <b>(-33.05%)</b></td><td>2.03 (-6.68%)</td><td>1.21 <b>(+23.86%)</b></td><td>4400.00 (+7.16%)</td><td>3482.80 (+19.44%)</td><td>4298.10 <b>(+49.35%)</b></td><td>1902.00 (+3.39%)</td><td>1202.05 <b>(+48.50%)</b></td><td>282.27 (-3.28%)</td><td>174.05 (-11.49%)</td><td>124.91 <b>(-33.05%)</b></td><td>122.02 (-6.68%)</td><td>72.93 <b>(+23.86%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>4.85 (n/a)</td><td>3.26 (n/a)</td><td>3.10 (n/a)</td><td>2.17 (n/a)</td><td>0.98 (n/a)</td><td>4106.00 (n/a)</td><td>2915.90 (n/a)</td><td>2877.80 (n/a)</td><td>1839.60 (n/a)</td><td>809.45 (n/a)</td><td>291.85 (n/a)</td><td>196.64 (n/a)</td><td>186.56 (n/a)</td><td>130.75 (n/a)</td><td>58.88 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>4.16 <b>(-25.14%)</b></td><td>3.01 <b>(-35.08%)</b></td><td>2.85 <b>(-47.79%)</b></td><td>2.17 (-0.50%)</td><td>0.89 <b>(-38.96%)</b></td><td>4109.00 (+0.50%)</td><td>3175.50 <b>(+44.98%)</b></td><td>3125.60 <b>(+91.52%)</b></td><td>2141.70 <b>(+33.59%)</b></td><td>905.15 (-15.85%)</td><td>250.68 <b>(-25.14%)</b></td><td>181.10 <b>(-35.08%)</b></td><td>171.76 <b>(-47.79%)</b></td><td>130.66 (-0.50%)</td><td>53.40 <b>(-38.96%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.56 (n/a)</td><td>4.63 (n/a)</td><td>5.46 (n/a)</td><td>2.18 (n/a)</td><td>1.45 (n/a)</td><td>4088.40 (n/a)</td><td>2190.28 (n/a)</td><td>1632.00 (n/a)</td><td>1603.20 (n/a)</td><td>1075.59 (n/a)</td><td>334.86 (n/a)</td><td>278.97 (n/a)</td><td>328.96 (n/a)</td><td>131.32 (n/a)</td><td>87.49 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>6.50 (-1.62%)</td><td>5.49 (+4.91%)</td><td>5.44 (-0.50%)</td><td>4.82 <b>(+29.97%)</b></td><td>0.65 <b>(-47.82%)</b></td><td>7231.90 <b>(-23.06%)</b></td><td>6418.56 (-8.24%)</td><td>6411.80 (+0.50%)</td><td>5361.70 (+1.65%)</td><td>714.63 <b>(-59.57%)</b></td><td>400.53 (-1.62%)</td><td>338.11 (+4.91%)</td><td>334.93 (-0.50%)</td><td>296.95 <b>(+29.97%)</b></td><td>39.85 <b>(-47.82%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>6.61 (n/a)</td><td>5.23 (n/a)</td><td>5.46 (n/a)</td><td>3.71 (n/a)</td><td>1.24 (n/a)</td><td>9399.60 (n/a)</td><td>6995.16 (n/a)</td><td>6380.00 (n/a)</td><td>5274.80 (n/a)</td><td>1767.41 (n/a)</td><td>407.12 (n/a)</td><td>322.29 (n/a)</td><td>336.60 (n/a)</td><td>228.46 (n/a)</td><td>76.37 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>5.70 (+11.06%)</td><td>4.63 (+5.78%)</td><td>4.33 (-1.71%)</td><td>3.61 (-0.00%)</td><td>0.92 <b>(+64.30%)</b></td><td>9660.40 (+0.00%)</td><td>7762.28 (-3.76%)</td><td>8050.50 (+1.74%)</td><td>6113.90 (-9.95%)</td><td>1516.13 <b>(+42.79%)</b></td><td>351.24 (+11.06%)</td><td>285.46 (+5.78%)</td><td>266.75 (-1.71%)</td><td>222.30 (-0.00%)</td><td>56.70 <b>(+64.30%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.13 (n/a)</td><td>4.38 (n/a)</td><td>4.41 (n/a)</td><td>3.61 (n/a)</td><td>0.56 (n/a)</td><td>9660.40 (n/a)</td><td>8065.34 (n/a)</td><td>7913.00 (n/a)</td><td>6789.80 (n/a)</td><td>1061.79 (n/a)</td><td>316.28 (n/a)</td><td>269.87 (n/a)</td><td>271.39 (n/a)</td><td>222.30 (n/a)</td><td>34.51 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>6.82 (+7.38%)</td><td>5.46 (+5.95%)</td><td>5.69 (+16.45%)</td><td>3.86 (-5.90%)</td><td>1.15 <b>(+29.61%)</b></td><td>9038.00 (+6.27%)</td><td>6641.94 (-4.09%)</td><td>6125.20 (-14.12%)</td><td>5112.10 (-6.87%)</td><td>1549.67 <b>(+31.26%)</b></td><td>420.08 (+7.38%)</td><td>336.41 (+5.95%)</td><td>350.60 (+16.45%)</td><td>237.61 (-5.90%)</td><td>71.08 <b>(+29.61%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>6.35 (n/a)</td><td>5.15 (n/a)</td><td>4.89 (n/a)</td><td>4.10 (n/a)</td><td>0.89 (n/a)</td><td>8505.00 (n/a)</td><td>6925.14 (n/a)</td><td>7132.50 (n/a)</td><td>5489.20 (n/a)</td><td>1180.62 (n/a)</td><td>391.22 (n/a)</td><td>317.52 (n/a)</td><td>301.09 (n/a)</td><td>252.50 (n/a)</td><td>54.84 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.78 (-0.23%)</td><td>0.76 (-1.25%)</td><td>0.76 (-1.64%)</td><td>0.74 (-1.50%)</td><td>0.02 <b>(+49.27%)</b></td><td>101520.00 (+1.52%)</td><td>99364.84 (+1.29%)</td><td>99133.80 (+1.66%)</td><td>96915.40 (+0.23%)</td><td>2049.61 <b>(+52.24%)</b></td><td>709.07 (-0.23%)</td><td>691.82 (-1.25%)</td><td>693.20 (-1.64%)</td><td>676.91 (-1.50%)</td><td>14.27 <b>(+49.27%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99995.90 (n/a)</td><td>98102.74 (n/a)</td><td>97510.60 (n/a)</td><td>96690.10 (n/a)</td><td>1346.27 (n/a)</td><td>710.72 (n/a)</td><td>700.59 (n/a)</td><td>704.74 (n/a)</td><td>687.22 (n/a)</td><td>9.56 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.77 (-0.14%)</td><td>0.76 (+0.99%)</td><td>0.77 (+1.41%)</td><td>0.74 (+1.35%)</td><td>0.01 <b>(-26.87%)</b></td><td>101620.20 (-1.34%)</td><td>98946.72 (-1.01%)</td><td>97858.10 (-1.39%)</td><td>97480.60 (+0.14%)</td><td>1878.07 <b>(-27.97%)</b></td><td>704.96 (-0.14%)</td><td>694.71 (+0.99%)</td><td>702.24 (+1.41%)</td><td>676.24 (+1.35%)</td><td>13.06 <b>(-26.87%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>102996.00 (n/a)</td><td>99952.38 (n/a)</td><td>99238.20 (n/a)</td><td>97342.30 (n/a)</td><td>2607.51 (n/a)</td><td>705.96 (n/a)</td><td>687.89 (n/a)</td><td>692.47 (n/a)</td><td>667.21 (n/a)</td><td>17.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.90 (+0.03%)</td><td>0.89 (-0.56%)</td><td>0.89 (+0.28%)</td><td>0.85 (-2.74%)</td><td>0.02 <b>(+125.00%)</b></td><td>88451.20 (+2.82%)</td><td>85283.52 (+0.59%)</td><td>84431.90 (-0.28%)</td><td>84006.50 (-0.03%)</td><td>1814.82 <b>(+131.86%)</b></td><td>818.03 (+0.03%)</td><td>806.06 (-0.56%)</td><td>813.90 (+0.28%)</td><td>776.92 (-2.74%)</td><td>16.73 <b>(+125.01%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>86024.30 (n/a)</td><td>84785.46 (n/a)</td><td>84668.40 (n/a)</td><td>84035.50 (n/a)</td><td>782.72 (n/a)</td><td>817.74 (n/a)</td><td>810.56 (n/a)</td><td>811.63 (n/a)</td><td>798.84 (n/a)</td><td>7.44 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>4.29 <b>(+75.74%)</b></td><td>2.58 <b>(+52.83%)</b></td><td>2.44 <b>(+47.27%)</b></td><td>1.46 (+14.57%)</td><td>1.04 <b>(+128.97%)</b></td><td>5528.80 (-12.72%)</td><td>3513.34 <b>(-29.98%)</b></td><td>3305.00 <b>(-32.10%)</b></td><td>1879.00 <b>(-43.10%)</b></td><td>1306.53 (+13.66%)</td><td>1125.01 <b>(+75.74%)</b></td><td>676.52 <b>(+52.83%)</b></td><td>639.62 <b>(+47.27%)</b></td><td>382.35 (+14.57%)</td><td>272.55 <b>(+128.97%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>2.44 (n/a)</td><td>1.69 (n/a)</td><td>1.66 (n/a)</td><td>1.27 (n/a)</td><td>0.45 (n/a)</td><td>6334.50 (n/a)</td><td>5017.60 (n/a)</td><td>4867.30 (n/a)</td><td>3302.30 (n/a)</td><td>1149.55 (n/a)</td><td>640.15 (n/a)</td><td>442.67 (n/a)</td><td>434.31 (n/a)</td><td>333.72 (n/a)</td><td>119.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.27 <b>(+26.91%)</b></td><td>0.24 <b>(+21.63%)</b></td><td>0.25 <b>(+32.33%)</b></td><td>0.18 (-2.88%)</td><td>0.04 <b>(+194.83%)</b></td><td>7011.90 (+2.97%)</td><td>5344.42 (-15.91%)</td><td>4924.20 <b>(-24.43%)</b></td><td>4560.50 <b>(-21.20%)</b></td><td>1031.90 <b>(+137.61%)</b></td><td>14.72 <b>(+26.91%)</b></td><td>12.89 <b>(+21.63%)</b></td><td>13.63 <b>(+32.33%)</b></td><td>9.57 (-2.88%)</td><td>2.19 <b>(+194.83%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>6809.60 (n/a)</td><td>6355.46 (n/a)</td><td>6516.50 (n/a)</td><td>5787.80 (n/a)</td><td>434.27 (n/a)</td><td>11.59 (n/a)</td><td>10.60 (n/a)</td><td>10.30 (n/a)</td><td>9.85 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.94 (n/a)</td><td>3.75 (n/a)</td><td>3.85 (n/a)</td><td>3.40 (n/a)</td><td>0.22 (n/a)</td><td>3.94 (n/a)</td><td>3.75 (n/a)</td><td>3.85 (n/a)</td><td>3.40 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>6.88 (+4.82%)</td><td>6.33 (+10.64%)</td><td>6.55 (+13.56%)</td><td>5.70 <b>(+21.35%)</b></td><td>0.57 (-15.89%)</td><td>6.87 (+4.82%)</td><td>6.32 (+10.64%)</td><td>6.55 (+13.56%)</td><td>5.69 <b>(+21.35%)</b></td><td>0.57 (-15.89%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>6.56 (n/a)</td><td>5.72 (n/a)</td><td>5.77 (n/a)</td><td>4.69 (n/a)</td><td>0.68 (n/a)</td><td>6.56 (n/a)</td><td>5.71 (n/a)</td><td>5.76 (n/a)</td><td>4.69 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>13.49 (-2.35%)</td><td>9.35 (+3.83%)</td><td>8.51 (+5.87%)</td><td>7.38 (+4.52%)</td><td>2.40 (-12.62%)</td><td>13.48 (-2.35%)</td><td>9.34 (+3.83%)</td><td>8.51 (+5.87%)</td><td>7.37 (+4.52%)</td><td>2.40 (-12.62%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>13.81 (n/a)</td><td>9.01 (n/a)</td><td>8.04 (n/a)</td><td>7.06 (n/a)</td><td>2.75 (n/a)</td><td>13.80 (n/a)</td><td>9.00 (n/a)</td><td>8.03 (n/a)</td><td>7.06 (n/a)</td><td>2.75 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.81 (n/a)</td><td>3.66 (n/a)</td><td>3.69 (n/a)</td><td>3.36 (n/a)</td><td>0.18 (n/a)</td><td>3.80 (n/a)</td><td>3.65 (n/a)</td><td>3.69 (n/a)</td><td>3.36 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>7.40 (-2.36%)</td><td>6.64 (+1.69%)</td><td>6.48 (-1.83%)</td><td>6.06 (+4.34%)</td><td>0.51 <b>(-31.06%)</b></td><td>7.40 (-2.36%)</td><td>6.63 (+1.69%)</td><td>6.48 (-1.83%)</td><td>6.05 (+4.34%)</td><td>0.51 <b>(-31.06%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>7.58 (n/a)</td><td>6.52 (n/a)</td><td>6.61 (n/a)</td><td>5.80 (n/a)</td><td>0.73 (n/a)</td><td>7.57 (n/a)</td><td>6.52 (n/a)</td><td>6.60 (n/a)</td><td>5.80 (n/a)</td><td>0.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>13.88 (-1.18%)</td><td>10.03 (-1.80%)</td><td>9.80 (-5.86%)</td><td>8.21 <b>(+28.62%)</b></td><td>2.32 <b>(-30.89%)</b></td><td>13.87 (-1.18%)</td><td>10.02 (-1.80%)</td><td>9.79 (-5.86%)</td><td>8.20 <b>(+28.62%)</b></td><td>2.32 <b>(-30.89%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>14.05 (n/a)</td><td>10.21 (n/a)</td><td>10.41 (n/a)</td><td>6.38 (n/a)</td><td>3.36 (n/a)</td><td>14.04 (n/a)</td><td>10.20 (n/a)</td><td>10.40 (n/a)</td><td>6.38 (n/a)</td><td>3.35 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.54 (-16.38%)</td><td>1.36 <b>(-42.89%)</b></td><td>1.03 <b>(-62.36%)</b></td><td>1.02 <b>(-29.61%)</b></td><td>0.67 (-13.53%)</td><td>2.54 (-16.38%)</td><td>1.36 <b>(-42.89%)</b></td><td>1.03 <b>(-62.36%)</b></td><td>1.02 <b>(-29.61%)</b></td><td>0.66 (-13.53%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.04 (n/a)</td><td>2.38 (n/a)</td><td>2.74 (n/a)</td><td>1.45 (n/a)</td><td>0.77 (n/a)</td><td>3.04 (n/a)</td><td>2.37 (n/a)</td><td>2.73 (n/a)</td><td>1.44 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.58 (+15.65%)</td><td>0.25 <b>(-20.50%)</b></td><td>0.11 <b>(-65.89%)</b></td><td>0.07 (-1.38%)</td><td>0.23 <b>(+52.12%)</b></td><td>0.57 (+15.65%)</td><td>0.25 <b>(-20.50%)</b></td><td>0.11 <b>(-65.89%)</b></td><td>0.07 (-1.38%)</td><td>0.23 <b>(+52.12%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.50 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.15 (n/a)</td><td>0.49 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.74 (+1.59%)</td><td>0.56 <b>(+26.58%)</b></td><td>0.64 <b>(+37.04%)</b></td><td>0.34 <b>(+337.32%)</b></td><td>0.16 <b>(-33.26%)</b></td><td>0.73 (+1.59%)</td><td>0.56 <b>(+26.58%)</b></td><td>0.63 <b>(+37.04%)</b></td><td>0.34 <b>(+337.32%)</b></td><td>0.16 <b>(-33.26%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.73 (n/a)</td><td>0.44 (n/a)</td><td>0.46 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td><td>0.72 (n/a)</td><td>0.44 (n/a)</td><td>0.46 (n/a)</td><td>0.08 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.50 (+0.25%)</td><td>1.78 (+8.38%)</td><td>1.88 (-7.07%)</td><td>0.43 <b>(-34.90%)</b></td><td>0.84 (-6.53%)</td><td>2.46 (+0.25%)</td><td>1.75 (+8.38%)</td><td>1.85 (-7.07%)</td><td>0.42 <b>(-34.90%)</b></td><td>0.82 (-6.53%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>2.49 (n/a)</td><td>1.64 (n/a)</td><td>2.03 (n/a)</td><td>0.66 (n/a)</td><td>0.90 (n/a)</td><td>2.45 (n/a)</td><td>1.62 (n/a)</td><td>1.99 (n/a)</td><td>0.65 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>299.60 (n/a)</td><td>260.66 (n/a)</td><td>267.70 (n/a)</td><td>219.70 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>679.70 (n/a)</td><td>407.70 (n/a)</td><td>357.60 (n/a)</td><td>220.60 (n/a)</td><td>200.41 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>567.90 (n/a)</td><td>337.30 (n/a)</td><td>272.90 (n/a)</td><td>248.90 (n/a)</td><td>134.12 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>538.20 (n/a)</td><td>362.52 (n/a)</td><td>333.70 (n/a)</td><td>247.30 (n/a)</td><td>111.49 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1044.00 (n/a)</td><td>528.36 (n/a)</td><td>483.10 (n/a)</td><td>273.40 (n/a)</td><td>307.31 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>695.20 (n/a)</td><td>514.20 (n/a)</td><td>459.40 (n/a)</td><td>441.90 (n/a)</td><td>106.65 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>656.30 (n/a)</td><td>442.24 (n/a)</td><td>503.70 (n/a)</td><td>266.70 (n/a)</td><td>168.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>483.10 (n/a)</td><td>348.82 (n/a)</td><td>309.60 (n/a)</td><td>242.40 (n/a)</td><td>97.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.60 (n/a)</td><td>325.26 (n/a)</td><td>283.60 (n/a)</td><td>233.90 (n/a)</td><td>109.56 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>668.20 (n/a)</td><td>455.12 (n/a)</td><td>421.40 (n/a)</td><td>310.50 (n/a)</td><td>155.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.10 (n/a)</td><td>381.90 (n/a)</td><td>316.10 (n/a)</td><td>274.60 (n/a)</td><td>122.32 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.00 (n/a)</td><td>408.48 (n/a)</td><td>326.70 (n/a)</td><td>263.90 (n/a)</td><td>160.61 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>519.80 (n/a)</td><td>436.36 (n/a)</td><td>503.70 (n/a)</td><td>309.50 (n/a)</td><td>106.93 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>533.40 (n/a)</td><td>387.58 (n/a)</td><td>398.00 (n/a)</td><td>233.40 (n/a)</td><td>131.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>582.50 (n/a)</td><td>485.82 (n/a)</td><td>494.20 (n/a)</td><td>308.00 (n/a)</td><td>111.14 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>529.20 (n/a)</td><td>395.42 (n/a)</td><td>445.00 (n/a)</td><td>200.60 (n/a)</td><td>130.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1025.20 (n/a)</td><td>558.58 (n/a)</td><td>546.50 (n/a)</td><td>271.90 (n/a)</td><td>312.60 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>618.00 (n/a)</td><td>464.32 (n/a)</td><td>476.80 (n/a)</td><td>229.80 (n/a)</td><td>150.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>693.60 (n/a)</td><td>474.62 (n/a)</td><td>523.50 (n/a)</td><td>202.50 (n/a)</td><td>182.63 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>517.20 (n/a)</td><td>375.24 (n/a)</td><td>360.90 (n/a)</td><td>311.20 (n/a)</td><td>82.53 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2580.50 (n/a)</td><td>908.86 (n/a)</td><td>527.70 (n/a)</td><td>313.60 (n/a)</td><td>941.61 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>716.60 (n/a)</td><td>471.84 (n/a)</td><td>448.30 (n/a)</td><td>290.50 (n/a)</td><td>156.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1867.80 (n/a)</td><td>744.74 (n/a)</td><td>461.20 (n/a)</td><td>431.50 (n/a)</td><td>628.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>635.10 (n/a)</td><td>435.70 (n/a)</td><td>385.80 (n/a)</td><td>257.70 (n/a)</td><td>147.40 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (-15.20%)</td><td>0.01 <b>(-32.39%)</b></td><td>0.01 <b>(-47.97%)</b></td><td>0.01 (-10.21%)</td><td>0.00 (-19.98%)</td><td>591.20 (+11.36%)</td><td>452.94 <b>(+45.36%)</b></td><td>506.40 <b>(+92.18%)</b></td><td>286.40 (+17.91%)</td><td>123.69 (+0.33%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>530.90 (n/a)</td><td>311.60 (n/a)</td><td>263.50 (n/a)</td><td>242.90 (n/a)</td><td>123.28 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (-3.83%)</td><td>0.01 (+12.18%)</td><td>0.01 <b>(+51.85%)</b></td><td>0.01 (+17.60%)</td><td>0.00 <b>(-31.79%)</b></td><td>462.40 (-14.97%)</td><td>315.50 (-19.12%)</td><td>307.70 <b>(-34.15%)</b></td><td>201.60 (+3.97%)</td><td>93.55 <b>(-40.19%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>543.80 (n/a)</td><td>390.06 (n/a)</td><td>467.30 (n/a)</td><td>193.90 (n/a)</td><td>156.40 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (-11.40%)</td><td>0.01 (-0.24%)</td><td>0.01 (+0.82%)</td><td>0.01 (-8.80%)</td><td>0.00 (-3.75%)</td><td>625.00 (+9.65%)</td><td>454.22 (+1.73%)</td><td>458.60 (-0.82%)</td><td>293.30 (+12.85%)</td><td>145.06 <b>(+25.19%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>570.00 (n/a)</td><td>446.48 (n/a)</td><td>462.40 (n/a)</td><td>259.90 (n/a)</td><td>115.88 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (+14.53%)</td><td>0.01 <b>(+21.27%)</b></td><td>0.01 <b>(+42.68%)</b></td><td>0.01 (+11.91%)</td><td>0.00 (+11.79%)</td><td>500.10 (-10.65%)</td><td>368.22 (-17.71%)</td><td>353.10 <b>(-29.91%)</b></td><td>210.10 (-12.68%)</td><td>119.95 (-11.38%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>559.70 (n/a)</td><td>447.44 (n/a)</td><td>503.80 (n/a)</td><td>240.60 (n/a)</td><td>135.36 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (-7.48%)</td><td>0.01 <b>(+28.35%)</b></td><td>0.01 <b>(+39.72%)</b></td><td>0.01 <b>(+32.50%)</b></td><td>0.00 <b>(-20.38%)</b></td><td>491.50 <b>(-24.52%)</b></td><td>380.06 <b>(-26.78%)</b></td><td>423.80 <b>(-28.44%)</b></td><td>252.80 (+8.08%)</td><td>112.12 <b>(-32.41%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>651.20 (n/a)</td><td>519.04 (n/a)</td><td>592.20 (n/a)</td><td>233.90 (n/a)</td><td>165.88 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (+6.44%)</td><td>0.01 <b>(+24.91%)</b></td><td>0.01 <b>(+43.76%)</b></td><td>0.01 <b>(+55.93%)</b></td><td>0.00 <b>(-30.27%)</b></td><td>517.60 <b>(-35.86%)</b></td><td>409.26 <b>(-26.24%)</b></td><td>408.00 <b>(-30.45%)</b></td><td>316.30 (-6.06%)</td><td>89.07 <b>(-56.56%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>807.00 (n/a)</td><td>554.86 (n/a)</td><td>586.60 (n/a)</td><td>336.70 (n/a)</td><td>205.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (+15.35%)</td><td>0.03 (+10.10%)</td><td>0.03 (+14.09%)</td><td>0.02 (+8.59%)</td><td>0.01 <b>(+35.44%)</b></td><td>530.10 (-7.90%)</td><td>353.00 (-5.18%)</td><td>287.10 (-12.34%)</td><td>214.70 (-13.29%)</td><td>145.02 (+11.01%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>575.60 (n/a)</td><td>372.28 (n/a)</td><td>327.50 (n/a)</td><td>247.60 (n/a)</td><td>130.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (-4.25%)</td><td>0.02 (-15.00%)</td><td>0.02 <b>(-26.47%)</b></td><td>0.02 <b>(-20.17%)</b></td><td>0.01 (+7.47%)</td><td>507.00 <b>(+25.28%)</b></td><td>387.96 (+19.44%)</td><td>401.00 <b>(+36.02%)</b></td><td>256.90 (+4.43%)</td><td>95.15 <b>(+32.00%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>404.70 (n/a)</td><td>324.82 (n/a)</td><td>294.80 (n/a)</td><td>246.00 (n/a)</td><td>72.08 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 <b>(-42.16%)</b></td><td>0.02 <b>(-51.93%)</b></td><td>0.02 <b>(-46.19%)</b></td><td>0.00 <b>(-85.21%)</b></td><td>0.01 <b>(+61.13%)</b></td><td>2092.90 <b>(+576.22%)</b></td><td>763.56 <b>(+207.39%)</b></td><td>450.30 <b>(+85.84%)</b></td><td>370.20 <b>(+72.91%)</b></td><td>743.98 <b>(+1950.40%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>309.50 (n/a)</td><td>248.40 (n/a)</td><td>242.30 (n/a)</td><td>214.10 (n/a)</td><td>36.28 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (-4.07%)</td><td>0.02 (+1.87%)</td><td>0.03 <b>(+58.85%)</b></td><td>0.00 <b>(-70.19%)</b></td><td>0.01 <b>(+27.76%)</b></td><td>2419.10 <b>(+235.52%)</b></td><td>751.74 <b>(+65.01%)</b></td><td>308.10 <b>(-37.06%)</b></td><td>277.00 (+4.25%)</td><td>935.17 <b>(+398.95%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>721.00 (n/a)</td><td>455.56 (n/a)</td><td>489.50 (n/a)</td><td>265.70 (n/a)</td><td>187.43 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (+2.26%)</td><td>0.02 (+7.31%)</td><td>0.02 (+1.98%)</td><td>0.01 <b>(+271.77%)</b></td><td>0.01 <b>(-29.10%)</b></td><td>663.20 <b>(-73.10%)</b></td><td>395.38 <b>(-47.54%)</b></td><td>334.20 (-1.94%)</td><td>238.90 (-2.21%)</td><td>166.39 <b>(-82.67%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2465.50 (n/a)</td><td>753.74 (n/a)</td><td>340.80 (n/a)</td><td>244.30 (n/a)</td><td>959.83 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (+0.85%)</td><td>0.02 (-0.94%)</td><td>0.03 (-4.36%)</td><td>0.01 (+3.46%)</td><td>0.01 <b>(-20.42%)</b></td><td>603.40 (-3.33%)</td><td>379.26 (-4.83%)</td><td>319.70 (+4.55%)</td><td>244.60 (-0.85%)</td><td>143.28 <b>(-21.59%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>624.20 (n/a)</td><td>398.52 (n/a)</td><td>305.80 (n/a)</td><td>246.70 (n/a)</td><td>182.72 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 <b>(-34.71%)</b></td><td>0.01 <b>(-38.51%)</b></td><td>0.01 <b>(-49.50%)</b></td><td>0.00 (+1.18%)</td><td>0.01 <b>(-48.74%)</b></td><td>1878.20 (-1.17%)</td><td>784.26 (+19.39%)</td><td>579.00 <b>(+98.02%)</b></td><td>319.90 <b>(+53.21%)</b></td><td>621.41 (-13.27%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1900.40 (n/a)</td><td>656.90 (n/a)</td><td>292.40 (n/a)</td><td>208.80 (n/a)</td><td>716.47 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (+17.62%)</td><td>0.02 (+3.86%)</td><td>0.02 (-4.76%)</td><td>0.01 (-7.56%)</td><td>0.01 <b>(+43.35%)</b></td><td>636.30 (+8.16%)</td><td>441.38 (+1.66%)</td><td>473.50 (+4.99%)</td><td>257.50 (-14.96%)</td><td>160.62 <b>(+32.67%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>588.30 (n/a)</td><td>434.16 (n/a)</td><td>451.00 (n/a)</td><td>302.80 (n/a)</td><td>121.06 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (-7.04%)</td><td>0.04 <b>(-24.42%)</b></td><td>0.03 <b>(-52.47%)</b></td><td>0.03 (-6.65%)</td><td>0.02 (+3.61%)</td><td>536.60 (+7.13%)</td><td>420.22 <b>(+35.73%)</b></td><td>508.80 <b>(+110.42%)</b></td><td>245.90 (+7.57%)</td><td>143.49 <b>(+24.25%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>500.90 (n/a)</td><td>309.60 (n/a)</td><td>241.80 (n/a)</td><td>228.60 (n/a)</td><td>115.49 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (-18.75%)</td><td>0.04 <b>(-29.51%)</b></td><td>0.03 <b>(-32.62%)</b></td><td>0.02 <b>(-29.22%)</b></td><td>0.01 <b>(-25.02%)</b></td><td>667.70 <b>(+41.28%)</b></td><td>492.40 <b>(+40.68%)</b></td><td>499.40 <b>(+48.41%)</b></td><td>292.50 <b>(+23.11%)</b></td><td>133.21 <b>(+22.10%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>472.60 (n/a)</td><td>350.02 (n/a)</td><td>336.50 (n/a)</td><td>237.60 (n/a)</td><td>109.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (+5.97%)</td><td>0.05 (-4.87%)</td><td>0.06 (-11.57%)</td><td>0.03 <b>(+21.67%)</b></td><td>0.02 (-3.11%)</td><td>474.80 (-17.81%)</td><td>334.64 (+2.19%)</td><td>295.80 (+13.07%)</td><td>234.90 (-5.62%)</td><td>104.25 <b>(-26.21%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>577.70 (n/a)</td><td>327.48 (n/a)</td><td>261.60 (n/a)</td><td>248.90 (n/a)</td><td>141.29 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (-19.98%)</td><td>0.04 (+12.39%)</td><td>0.04 <b>(+37.88%)</b></td><td>0.03 (+13.49%)</td><td>0.01 <b>(-29.75%)</b></td><td>538.90 (-11.89%)</td><td>395.22 (-15.55%)</td><td>368.10 <b>(-27.47%)</b></td><td>272.40 <b>(+24.95%)</b></td><td>125.78 (-16.58%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>611.60 (n/a)</td><td>468.00 (n/a)</td><td>507.50 (n/a)</td><td>218.00 (n/a)</td><td>150.77 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (+13.51%)</td><td>0.05 (+11.09%)</td><td>0.07 (-1.48%)</td><td>0.03 <b>(+38.25%)</b></td><td>0.02 (-11.65%)</td><td>544.90 <b>(-27.66%)</b></td><td>345.04 (-19.86%)</td><td>250.70 (+1.50%)</td><td>212.20 (-11.91%)</td><td>153.11 <b>(-40.26%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>753.30 (n/a)</td><td>430.54 (n/a)</td><td>247.00 (n/a)</td><td>240.90 (n/a)</td><td>256.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (-8.46%)</td><td>0.04 (+18.05%)</td><td>0.04 <b>(+39.89%)</b></td><td>0.03 <b>(+252.78%)</b></td><td>0.01 <b>(-55.36%)</b></td><td>504.60 <b>(-71.65%)</b></td><td>399.44 <b>(-44.00%)</b></td><td>401.60 <b>(-28.52%)</b></td><td>289.20 (+9.26%)</td><td>88.80 <b>(-85.70%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1780.00 (n/a)</td><td>713.24 (n/a)</td><td>561.80 (n/a)</td><td>264.70 (n/a)</td><td>621.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (+0.09%)</td><td>0.11 (+6.97%)</td><td>0.10 (-17.11%)</td><td>0.07 <b>(+117.30%)</b></td><td>0.03 <b>(-39.25%)</b></td><td>477.50 <b>(-53.98%)</b></td><td>329.30 <b>(-26.99%)</b></td><td>336.10 <b>(+20.64%)</b></td><td>237.80 (-0.08%)</td><td>95.80 <b>(-71.89%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1037.60 (n/a)</td><td>451.06 (n/a)</td><td>278.60 (n/a)</td><td>238.00 (n/a)</td><td>340.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (+0.06%)</td><td>0.08 (-13.09%)</td><td>0.07 (-13.66%)</td><td>0.06 (-1.90%)</td><td>0.03 (-2.33%)</td><td>526.80 (+1.93%)</td><td>414.22 (+14.68%)</td><td>438.10 (+15.81%)</td><td>252.10 (-0.08%)</td><td>102.22 (-3.10%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>516.80 (n/a)</td><td>361.20 (n/a)</td><td>378.30 (n/a)</td><td>252.30 (n/a)</td><td>105.49 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.09 <b>(-31.03%)</b></td><td>0.05 <b>(-52.81%)</b></td><td>0.05 <b>(-50.49%)</b></td><td>0.02 <b>(-77.11%)</b></td><td>0.03 <b>(+43.60%)</b></td><td>1956.20 <b>(+336.85%)</b></td><td>1058.90 <b>(+231.65%)</b></td><td>645.30 <b>(+101.97%)</b></td><td>346.60 <b>(+44.96%)</b></td><td>802.47 <b>(+907.31%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>447.80 (n/a)</td><td>319.28 (n/a)</td><td>319.50 (n/a)</td><td>239.10 (n/a)</td><td>79.66 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (+2.29%)</td><td>0.10 (+3.51%)</td><td>0.11 <b>(+27.46%)</b></td><td>0.06 (-5.54%)</td><td>0.03 (+7.71%)</td><td>552.60 (+5.86%)</td><td>371.64 (-1.33%)</td><td>302.50 <b>(-21.53%)</b></td><td>239.70 (-2.24%)</td><td>138.76 (+17.10%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>522.00 (n/a)</td><td>376.64 (n/a)</td><td>385.50 (n/a)</td><td>245.20 (n/a)</td><td>118.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 (-9.75%)</td><td>0.08 (+18.70%)</td><td>0.07 (+11.30%)</td><td>0.06 <b>(+361.39%)</b></td><td>0.02 <b>(-48.59%)</b></td><td>536.30 <b>(-78.33%)</b></td><td>430.74 <b>(-49.29%)</b></td><td>454.70 (-10.17%)</td><td>285.00 (+10.81%)</td><td>92.76 <b>(-89.86%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2474.50 (n/a)</td><td>849.48 (n/a)</td><td>506.20 (n/a)</td><td>257.20 (n/a)</td><td>914.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (+8.68%)</td><td>0.02 <b>(+27.62%)</b></td><td>0.02 <b>(+56.00%)</b></td><td>0.01 (-1.63%)</td><td>0.00 (+8.25%)</td><td>509.50 (+1.66%)</td><td>291.86 <b>(-21.07%)</b></td><td>229.60 <b>(-35.90%)</b></td><td>216.50 (-7.99%)</td><td>124.49 (-0.03%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>501.20 (n/a)</td><td>369.76 (n/a)</td><td>358.20 (n/a)</td><td>235.30 (n/a)</td><td>124.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (+6.12%)</td><td>0.01 (+17.46%)</td><td>0.02 (+15.23%)</td><td>0.01 (+4.78%)</td><td>0.00 (+7.12%)</td><td>500.10 (-4.56%)</td><td>304.84 (-14.52%)</td><td>254.90 (-13.24%)</td><td>237.10 (-5.76%)</td><td>110.79 (-1.89%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.00 (n/a)</td><td>356.64 (n/a)</td><td>293.80 (n/a)</td><td>251.60 (n/a)</td><td>112.92 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (-1.31%)</td><td>0.01 (-15.38%)</td><td>0.01 <b>(-28.63%)</b></td><td>0.01 (+12.29%)</td><td>0.00 (-12.70%)</td><td>492.50 (-10.94%)</td><td>373.82 (+14.45%)</td><td>391.10 <b>(+40.13%)</b></td><td>246.20 (+1.36%)</td><td>91.27 <b>(-28.47%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>553.00 (n/a)</td><td>326.62 (n/a)</td><td>279.10 (n/a)</td><td>242.90 (n/a)</td><td>127.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (+14.64%)</td><td>0.01 (+19.32%)</td><td>0.01 <b>(+53.05%)</b></td><td>0.01 (-12.61%)</td><td>0.00 <b>(+32.33%)</b></td><td>562.90 (+14.43%)</td><td>341.84 (-12.44%)</td><td>275.60 <b>(-34.66%)</b></td><td>234.20 (-12.74%)</td><td>139.71 <b>(+29.31%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.90 (n/a)</td><td>390.40 (n/a)</td><td>421.80 (n/a)</td><td>268.40 (n/a)</td><td>108.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 <b>(+26.36%)</b></td><td>0.01 <b>(+32.74%)</b></td><td>0.01 (+18.13%)</td><td>0.01 <b>(+138.53%)</b></td><td>0.00 (-2.58%)</td><td>548.30 <b>(-58.08%)</b></td><td>404.76 <b>(-35.47%)</b></td><td>427.20 (-15.34%)</td><td>243.50 <b>(-20.86%)</b></td><td>113.79 <b>(-71.13%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1308.00 (n/a)</td><td>627.22 (n/a)</td><td>504.60 (n/a)</td><td>307.70 (n/a)</td><td>394.13 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 <b>(-23.68%)</b></td><td>0.01 <b>(-27.55%)</b></td><td>0.01 <b>(-30.53%)</b></td><td>0.01 <b>(-29.58%)</b></td><td>0.00 (-12.14%)</td><td>604.40 <b>(+42.01%)</b></td><td>413.58 <b>(+42.07%)</b></td><td>419.30 <b>(+43.94%)</b></td><td>244.00 <b>(+30.97%)</b></td><td>140.55 <b>(+61.35%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>425.60 (n/a)</td><td>291.12 (n/a)</td><td>291.30 (n/a)</td><td>186.30 (n/a)</td><td>87.11 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (-3.80%)</td><td>0.01 <b>(-21.36%)</b></td><td>0.01 <b>(-39.15%)</b></td><td>0.01 <b>(-28.05%)</b></td><td>0.00 <b>(+61.45%)</b></td><td>529.90 <b>(+38.97%)</b></td><td>405.88 <b>(+39.19%)</b></td><td>464.80 <b>(+64.36%)</b></td><td>225.10 (+3.97%)</td><td>143.30 <b>(+141.83%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>381.30 (n/a)</td><td>291.60 (n/a)</td><td>282.80 (n/a)</td><td>216.50 (n/a)</td><td>59.26 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 <b>(+28.04%)</b></td><td>0.01 <b>(+26.19%)</b></td><td>0.01 <b>(+40.16%)</b></td><td>0.01 (-6.77%)</td><td>0.00 <b>(+60.02%)</b></td><td>591.30 (+7.28%)</td><td>376.74 (-17.11%)</td><td>327.00 <b>(-28.65%)</b></td><td>249.90 <b>(-21.91%)</b></td><td>134.26 <b>(+33.44%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.20 (n/a)</td><td>454.48 (n/a)</td><td>458.30 (n/a)</td><td>320.00 (n/a)</td><td>100.62 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (-18.35%)</td><td>0.01 (-12.92%)</td><td>0.01 (+1.34%)</td><td>0.01 (-15.70%)</td><td>0.00 <b>(-31.51%)</b></td><td>578.00 (+18.64%)</td><td>430.66 (+12.23%)</td><td>433.10 (-1.32%)</td><td>303.90 <b>(+22.49%)</b></td><td>104.34 (-1.30%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>487.20 (n/a)</td><td>383.72 (n/a)</td><td>438.90 (n/a)</td><td>248.10 (n/a)</td><td>105.72 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (-10.29%)</td><td>0.01 (-14.50%)</td><td>0.01 (-3.57%)</td><td>0.00 <b>(-68.97%)</b></td><td>0.00 <b>(+45.23%)</b></td><td>1920.30 <b>(+222.31%)</b></td><td>725.14 <b>(+63.32%)</b></td><td>448.10 (+3.70%)</td><td>327.80 (+11.46%)</td><td>671.79 <b>(+499.45%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>595.80 (n/a)</td><td>444.00 (n/a)</td><td>432.10 (n/a)</td><td>294.10 (n/a)</td><td>112.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>656.30 (n/a)</td><td>452.94 (n/a)</td><td>511.60 (n/a)</td><td>209.30 (n/a)</td><td>170.53 (n/a)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td><td>n/a (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (+13.59%)</td><td>0.01 (-7.46%)</td><td>0.01 <b>(-23.68%)</b></td><td>0.00 (-9.47%)</td><td>0.00 <b>(+29.21%)</b></td><td>825.90 (+10.47%)</td><td>558.36 (+12.73%)</td><td>608.00 <b>(+31.01%)</b></td><td>284.50 (-11.95%)</td><td>202.27 <b>(+20.35%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>747.60 (n/a)</td><td>495.32 (n/a)</td><td>464.10 (n/a)</td><td>323.10 (n/a)</td><td>168.07 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (-10.60%)</td><td>0.03 <b>(+20.88%)</b></td><td>0.03 <b>(+40.26%)</b></td><td>0.01 (-6.37%)</td><td>0.01 (-6.54%)</td><td>626.00 (+6.81%)</td><td>335.16 (-16.12%)</td><td>267.80 <b>(-28.70%)</b></td><td>248.10 (+11.86%)</td><td>163.20 (+16.45%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.10 (n/a)</td><td>399.56 (n/a)</td><td>375.60 (n/a)</td><td>221.80 (n/a)</td><td>140.14 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (+10.77%)</td><td>0.03 <b>(+28.14%)</b></td><td>0.03 <b>(+80.87%)</b></td><td>0.02 <b>(+74.90%)</b></td><td>0.01 (-16.55%)</td><td>516.10 <b>(-42.83%)</b></td><td>333.20 <b>(-31.91%)</b></td><td>260.20 <b>(-44.71%)</b></td><td>218.40 (-9.71%)</td><td>130.67 <b>(-52.20%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>902.80 (n/a)</td><td>489.36 (n/a)</td><td>470.60 (n/a)</td><td>241.90 (n/a)</td><td>273.36 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 <b>(+35.77%)</b></td><td>0.03 (+17.58%)</td><td>0.02 (-1.78%)</td><td>0.02 <b>(+25.54%)</b></td><td>0.01 <b>(+28.39%)</b></td><td>456.70 <b>(-20.34%)</b></td><td>349.02 (-15.88%)</td><td>347.80 (+1.81%)</td><td>204.80 <b>(-26.36%)</b></td><td>97.45 <b>(-30.82%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>573.30 (n/a)</td><td>414.92 (n/a)</td><td>341.60 (n/a)</td><td>278.10 (n/a)</td><td>140.86 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (+8.37%)</td><td>0.03 <b>(+49.20%)</b></td><td>0.03 <b>(+71.83%)</b></td><td>0.02 <b>(+76.48%)</b></td><td>0.01 <b>(-33.24%)</b></td><td>364.70 <b>(-43.33%)</b></td><td>269.96 <b>(-38.13%)</b></td><td>244.10 <b>(-41.80%)</b></td><td>226.30 (-7.75%)</td><td>55.43 <b>(-63.79%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.60 (n/a)</td><td>436.30 (n/a)</td><td>419.40 (n/a)</td><td>245.30 (n/a)</td><td>153.09 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (+13.10%)</td><td>0.02 (+16.48%)</td><td>0.02 (+8.30%)</td><td>0.01 (+3.23%)</td><td>0.01 <b>(+33.27%)</b></td><td>566.70 (-3.13%)</td><td>400.74 (-10.51%)</td><td>464.80 (-7.67%)</td><td>227.60 (-11.58%)</td><td>154.68 (+7.33%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.00 (n/a)</td><td>447.80 (n/a)</td><td>503.40 (n/a)</td><td>257.40 (n/a)</td><td>144.12 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (+6.73%)</td><td>0.03 <b>(+41.81%)</b></td><td>0.03 <b>(+83.00%)</b></td><td>0.02 <b>(+32.10%)</b></td><td>0.01 <b>(-20.31%)</b></td><td>444.30 <b>(-24.30%)</b></td><td>296.38 <b>(-33.36%)</b></td><td>270.80 <b>(-45.36%)</b></td><td>229.10 (-6.30%)</td><td>85.57 <b>(-41.53%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>586.90 (n/a)</td><td>444.74 (n/a)</td><td>495.60 (n/a)</td><td>244.50 (n/a)</td><td>146.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 <b>(+25.41%)</b></td><td>0.02 (+11.74%)</td><td>0.03 <b>(+61.49%)</b></td><td>0.00 <b>(-70.83%)</b></td><td>0.01 <b>(+139.37%)</b></td><td>1934.20 <b>(+242.82%)</b></td><td>662.44 <b>(+54.41%)</b></td><td>273.10 <b>(-38.09%)</b></td><td>244.40 <b>(-20.26%)</b></td><td>726.22 <b>(+551.02%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.20 (n/a)</td><td>429.02 (n/a)</td><td>441.10 (n/a)</td><td>306.50 (n/a)</td><td>111.55 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 <b>(+36.16%)</b></td><td>0.03 <b>(+25.37%)</b></td><td>0.03 (+8.56%)</td><td>0.02 <b>(+46.01%)</b></td><td>0.01 (+19.73%)</td><td>426.00 <b>(-31.51%)</b></td><td>334.14 <b>(-21.88%)</b></td><td>325.40 (-7.90%)</td><td>221.70 <b>(-26.57%)</b></td><td>86.10 <b>(-38.59%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>622.00 (n/a)</td><td>427.72 (n/a)</td><td>353.30 (n/a)</td><td>301.90 (n/a)</td><td>140.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 <b>(-35.77%)</b></td><td>0.02 <b>(-22.87%)</b></td><td>0.02 <b>(-26.57%)</b></td><td>0.02 (-0.35%)</td><td>0.00 <b>(-67.90%)</b></td><td>503.80 (+0.36%)</td><td>437.44 <b>(+22.98%)</b></td><td>450.30 <b>(+36.21%)</b></td><td>374.30 <b>(+55.70%)</b></td><td>49.96 <b>(-50.63%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.00 (n/a)</td><td>355.70 (n/a)</td><td>330.60 (n/a)</td><td>240.40 (n/a)</td><td>101.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (+17.25%)</td><td>0.02 (-15.19%)</td><td>0.02 <b>(-23.39%)</b></td><td>0.00 <b>(-57.31%)</b></td><td>0.01 <b>(+46.27%)</b></td><td>1850.00 <b>(+134.24%)</b></td><td>726.46 <b>(+57.23%)</b></td><td>473.90 <b>(+30.52%)</b></td><td>267.50 (-14.73%)</td><td>638.01 <b>(+224.40%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>789.80 (n/a)</td><td>462.04 (n/a)</td><td>363.10 (n/a)</td><td>313.70 (n/a)</td><td>196.67 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (-12.57%)</td><td>0.02 <b>(+25.60%)</b></td><td>0.03 <b>(+52.45%)</b></td><td>0.01 <b>(+75.42%)</b></td><td>0.01 <b>(-30.22%)</b></td><td>591.70 <b>(-42.99%)</b></td><td>395.78 <b>(-30.44%)</b></td><td>313.10 <b>(-34.42%)</b></td><td>285.50 (+14.38%)</td><td>133.70 <b>(-55.01%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1037.90 (n/a)</td><td>569.00 (n/a)</td><td>477.40 (n/a)</td><td>249.60 (n/a)</td><td>297.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (+18.26%)</td><td>0.02 (-2.00%)</td><td>0.02 (-13.67%)</td><td>0.01 (-17.20%)</td><td>0.01 <b>(+86.29%)</b></td><td>609.70 <b>(+20.78%)</b></td><td>452.92 (+9.35%)</td><td>511.70 (+15.85%)</td><td>269.20 (-15.45%)</td><td>145.68 <b>(+91.36%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>504.80 (n/a)</td><td>414.20 (n/a)</td><td>441.70 (n/a)</td><td>318.40 (n/a)</td><td>76.13 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (-3.84%)</td><td>0.06 (+9.94%)</td><td>0.06 (+8.62%)</td><td>0.04 <b>(+34.13%)</b></td><td>0.01 <b>(-41.73%)</b></td><td>381.60 <b>(-25.45%)</b></td><td>298.72 (-14.17%)</td><td>285.70 (-7.96%)</td><td>241.50 (+4.01%)</td><td>51.72 <b>(-54.39%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>511.90 (n/a)</td><td>348.04 (n/a)</td><td>310.40 (n/a)</td><td>232.20 (n/a)</td><td>113.40 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (-2.63%)</td><td>0.05 (-5.02%)</td><td>0.06 (-7.79%)</td><td>0.03 <b>(-20.66%)</b></td><td>0.02 (+16.10%)</td><td>630.40 <b>(+26.05%)</b></td><td>346.46 (+10.44%)</td><td>291.70 (+8.48%)</td><td>248.80 (+2.73%)</td><td>160.02 <b>(+51.25%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>500.10 (n/a)</td><td>313.72 (n/a)</td><td>268.90 (n/a)</td><td>242.20 (n/a)</td><td>105.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 <b>(+59.29%)</b></td><td>0.04 (+11.75%)</td><td>0.05 (+12.58%)</td><td>0.01 <b>(-69.33%)</b></td><td>0.02 <b>(+250.57%)</b></td><td>1863.20 <b>(+226.02%)</b></td><td>628.36 <b>(+48.82%)</b></td><td>352.80 (-11.18%)</td><td>229.80 <b>(-37.21%)</b></td><td>693.17 <b>(+711.71%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>571.50 (n/a)</td><td>422.22 (n/a)</td><td>397.20 (n/a)</td><td>366.00 (n/a)</td><td>85.40 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (+14.19%)</td><td>0.06 <b>(+29.67%)</b></td><td>0.06 (+5.55%)</td><td>0.06 <b>(+115.32%)</b></td><td>0.01 <b>(-49.05%)</b></td><td>294.50 <b>(-53.56%)</b></td><td>266.64 <b>(-31.54%)</b></td><td>281.30 (-5.25%)</td><td>210.40 (-12.44%)</td><td>33.96 <b>(-79.82%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>634.10 (n/a)</td><td>389.50 (n/a)</td><td>296.90 (n/a)</td><td>240.30 (n/a)</td><td>168.28 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (-11.73%)</td><td>0.04 <b>(-25.48%)</b></td><td>0.04 <b>(-36.12%)</b></td><td>0.03 (+10.91%)</td><td>0.01 (-19.62%)</td><td>497.80 (-9.84%)</td><td>413.32 <b>(+29.15%)</b></td><td>452.10 <b>(+56.54%)</b></td><td>249.20 (+13.32%)</td><td>99.05 <b>(-25.58%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>552.10 (n/a)</td><td>320.04 (n/a)</td><td>288.80 (n/a)</td><td>219.90 (n/a)</td><td>133.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (+0.92%)</td><td>0.06 <b>(+22.20%)</b></td><td>0.06 (+3.91%)</td><td>0.05 <b>(+84.67%)</b></td><td>0.01 <b>(-62.88%)</b></td><td>308.60 <b>(-45.85%)</b></td><td>265.92 <b>(-28.09%)</b></td><td>274.90 (-3.75%)</td><td>232.80 (-0.94%)</td><td>31.15 <b>(-80.50%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>569.90 (n/a)</td><td>369.80 (n/a)</td><td>285.60 (n/a)</td><td>235.00 (n/a)</td><td>159.74 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.09 <b>(+54.31%)</b></td><td>0.05 <b>(+34.31%)</b></td><td>0.06 <b>(+81.90%)</b></td><td>0.03 (+0.25%)</td><td>0.02 <b>(+63.21%)</b></td><td>594.70 (-0.25%)</td><td>365.58 <b>(-20.61%)</b></td><td>290.90 <b>(-45.02%)</b></td><td>189.00 <b>(-35.21%)</b></td><td>164.40 (+10.25%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>596.20 (n/a)</td><td>460.46 (n/a)</td><td>529.10 (n/a)</td><td>291.70 (n/a)</td><td>149.12 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 <b>(-22.59%)</b></td><td>0.06 (+11.91%)</td><td>0.06 <b>(+42.85%)</b></td><td>0.03 (-3.45%)</td><td>0.01 <b>(-36.13%)</b></td><td>509.30 (+3.58%)</td><td>316.36 (-15.02%)</td><td>281.30 <b>(-30.01%)</b></td><td>246.10 <b>(+29.19%)</b></td><td>109.88 (-12.19%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>491.70 (n/a)</td><td>372.26 (n/a)</td><td>401.90 (n/a)</td><td>190.50 (n/a)</td><td>125.13 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (-8.73%)</td><td>0.06 (+12.14%)</td><td>0.06 (+6.80%)</td><td>0.04 <b>(+32.96%)</b></td><td>0.01 <b>(-38.58%)</b></td><td>438.60 <b>(-24.79%)</b></td><td>304.84 (-17.46%)</td><td>273.10 (-6.38%)</td><td>255.20 (+9.57%)</td><td>75.89 <b>(-48.62%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>583.20 (n/a)</td><td>369.34 (n/a)</td><td>291.70 (n/a)</td><td>232.90 (n/a)</td><td>147.69 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (-1.54%)</td><td>0.05 (+3.58%)</td><td>0.04 (+2.59%)</td><td>0.03 (+3.46%)</td><td>0.02 (+1.71%)</td><td>574.80 (-3.35%)</td><td>397.26 (-3.23%)</td><td>410.90 (-2.51%)</td><td>250.20 (+1.54%)</td><td>129.87 (-0.52%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>594.70 (n/a)</td><td>410.54 (n/a)</td><td>421.50 (n/a)</td><td>246.40 (n/a)</td><td>130.55 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (+0.56%)</td><td>0.06 <b>(+27.19%)</b></td><td>0.06 <b>(+66.85%)</b></td><td>0.03 <b>(+22.74%)</b></td><td>0.01 <b>(-24.61%)</b></td><td>469.90 (-18.53%)</td><td>313.04 <b>(-25.35%)</b></td><td>280.80 <b>(-40.06%)</b></td><td>242.30 (-0.57%)</td><td>90.59 <b>(-35.15%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>576.80 (n/a)</td><td>419.36 (n/a)</td><td>468.50 (n/a)</td><td>243.70 (n/a)</td><td>139.70 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 <b>(-23.35%)</b></td><td>0.05 (+1.24%)</td><td>0.05 (-4.15%)</td><td>0.04 <b>(+27.60%)</b></td><td>0.01 <b>(-57.62%)</b></td><td>441.30 <b>(-21.63%)</b></td><td>327.10 (-13.61%)</td><td>306.70 (+4.32%)</td><td>260.30 <b>(+30.41%)</b></td><td>68.70 <b>(-59.56%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>563.10 (n/a)</td><td>378.62 (n/a)</td><td>294.00 (n/a)</td><td>199.60 (n/a)</td><td>169.86 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 <b>(-36.04%)</b></td><td>0.10 (-18.47%)</td><td>0.13 <b>(+20.14%)</b></td><td>0.02 <b>(-77.56%)</b></td><td>0.05 (-7.87%)</td><td>2005.60 <b>(+345.59%)</b></td><td>637.24 <b>(+98.86%)</b></td><td>255.60 (-16.77%)</td><td>249.00 <b>(+56.41%)</b></td><td>768.64 <b>(+510.34%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>450.10 (n/a)</td><td>320.44 (n/a)</td><td>307.10 (n/a)</td><td>159.20 (n/a)</td><td>125.94 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (-12.29%)</td><td>0.12 (+3.62%)</td><td>0.13 (+8.24%)</td><td>0.09 <b>(+68.76%)</b></td><td>0.02 <b>(-49.59%)</b></td><td>370.20 <b>(-40.74%)</b></td><td>284.06 (-14.10%)</td><td>260.00 (-7.60%)</td><td>244.50 (+14.04%)</td><td>52.99 <b>(-68.37%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>624.70 (n/a)</td><td>330.68 (n/a)</td><td>281.40 (n/a)</td><td>214.40 (n/a)</td><td>167.51 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (-6.30%)</td><td>0.11 <b>(+38.52%)</b></td><td>0.11 <b>(+68.59%)</b></td><td>0.07 <b>(+280.85%)</b></td><td>0.03 <b>(-45.09%)</b></td><td>493.50 <b>(-73.74%)</b></td><td>315.88 <b>(-53.93%)</b></td><td>288.90 <b>(-40.68%)</b></td><td>245.20 (+6.70%)</td><td>101.52 <b>(-85.06%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1879.60 (n/a)</td><td>685.72 (n/a)</td><td>487.00 (n/a)</td><td>229.80 (n/a)</td><td>679.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (-6.40%)</td><td>0.09 (-3.55%)</td><td>0.11 <b>(+60.02%)</b></td><td>0.02 <b>(-43.85%)</b></td><td>0.05 (+6.27%)</td><td>1853.90 <b>(+78.11%)</b></td><td>675.92 <b>(+35.96%)</b></td><td>291.00 <b>(-37.51%)</b></td><td>241.60 (+6.81%)</td><td>685.02 <b>(+108.83%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1040.90 (n/a)</td><td>497.16 (n/a)</td><td>465.70 (n/a)</td><td>226.20 (n/a)</td><td>328.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (+7.77%)</td><td>0.09 (+3.06%)</td><td>0.08 (+6.90%)</td><td>0.06 (+8.67%)</td><td>0.03 (+16.03%)</td><td>553.60 (-7.98%)</td><td>399.32 (-1.37%)</td><td>390.70 (-6.44%)</td><td>244.50 (-7.21%)</td><td>135.65 (+2.64%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>601.60 (n/a)</td><td>404.88 (n/a)</td><td>417.60 (n/a)</td><td>263.50 (n/a)</td><td>132.16 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 <b>(-38.67%)</b></td><td>0.09 <b>(-21.03%)</b></td><td>0.09 (-14.39%)</td><td>0.06 (-7.03%)</td><td>0.03 <b>(-47.66%)</b></td><td>535.00 (+7.56%)</td><td>388.48 (+16.48%)</td><td>375.60 (+16.83%)</td><td>252.50 <b>(+63.11%)</b></td><td>128.06 (-8.74%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>497.40 (n/a)</td><td>333.52 (n/a)</td><td>321.50 (n/a)</td><td>154.80 (n/a)</td><td>140.33 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (+3.74%)</td><td>0.10 (+4.19%)</td><td>0.09 (+3.63%)</td><td>0.07 (+19.99%)</td><td>0.03 (-12.19%)</td><td>479.10 (-16.66%)</td><td>369.58 (-7.28%)</td><td>377.80 (-3.50%)</td><td>249.40 (-3.59%)</td><td>106.00 <b>(-25.20%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>574.90 (n/a)</td><td>398.58 (n/a)</td><td>391.50 (n/a)</td><td>258.70 (n/a)</td><td>141.71 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.16 (+15.10%)</td><td>0.11 (+7.41%)</td><td>0.11 (+2.43%)</td><td>0.05 (-7.18%)</td><td>0.04 (+11.54%)</td><td>607.00 (+7.74%)</td><td>340.94 (-4.72%)</td><td>302.80 (-2.39%)</td><td>210.40 (-13.13%)</td><td>155.87 (+13.91%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>563.40 (n/a)</td><td>357.82 (n/a)</td><td>310.20 (n/a)</td><td>242.20 (n/a)</td><td>136.84 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (+7.18%)</td><td>0.12 (-3.14%)</td><td>0.12 (-2.80%)</td><td>0.09 (-19.12%)</td><td>0.02 <b>(+87.01%)</b></td><td>374.80 <b>(+23.61%)</b></td><td>286.70 (+5.64%)</td><td>277.60 (+2.89%)</td><td>228.10 (-6.71%)</td><td>57.98 <b>(+117.85%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>303.20 (n/a)</td><td>271.40 (n/a)</td><td>269.80 (n/a)</td><td>244.50 (n/a)</td><td>26.61 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (-1.66%)</td><td>0.10 (-12.73%)</td><td>0.09 <b>(-26.93%)</b></td><td>0.06 <b>(-23.77%)</b></td><td>0.03 <b>(+32.54%)</b></td><td>516.30 <b>(+31.17%)</b></td><td>373.82 <b>(+20.39%)</b></td><td>382.60 <b>(+36.89%)</b></td><td>248.90 (+1.72%)</td><td>122.86 <b>(+66.11%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>393.60 (n/a)</td><td>310.50 (n/a)</td><td>279.50 (n/a)</td><td>244.70 (n/a)</td><td>73.96 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 <b>(-23.25%)</b></td><td>0.09 (-5.68%)</td><td>0.10 (-2.85%)</td><td>0.06 (+6.77%)</td><td>0.02 <b>(-38.46%)</b></td><td>550.80 (-6.34%)</td><td>382.48 (-1.16%)</td><td>321.60 (+2.94%)</td><td>291.30 <b>(+30.28%)</b></td><td>111.46 <b>(-29.02%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>588.10 (n/a)</td><td>386.96 (n/a)</td><td>312.40 (n/a)</td><td>223.60 (n/a)</td><td>157.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (-5.07%)</td><td>0.10 <b>(+27.07%)</b></td><td>0.12 <b>(+92.99%)</b></td><td>0.05 <b>(+25.93%)</b></td><td>0.04 (-0.47%)</td><td>603.10 <b>(-20.59%)</b></td><td>381.94 <b>(-23.14%)</b></td><td>267.50 <b>(-48.18%)</b></td><td>260.90 (+5.33%)</td><td>164.71 (-19.13%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>759.50 (n/a)</td><td>496.92 (n/a)</td><td>516.20 (n/a)</td><td>247.70 (n/a)</td><td>203.67 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.10 (-3.65%)</td><td>0.06 <b>(-26.43%)</b></td><td>0.05 <b>(-33.85%)</b></td><td>0.04 (-8.29%)</td><td>0.02 (+1.57%)</td><td>547.20 (+9.05%)</td><td>437.86 <b>(+37.50%)</b></td><td>449.40 <b>(+51.16%)</b></td><td>247.30 (+3.78%)</td><td>123.98 (+14.80%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>501.80 (n/a)</td><td>318.44 (n/a)</td><td>297.30 (n/a)</td><td>238.30 (n/a)</td><td>108.00 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.20 (+15.53%)</td><td>0.16 (+14.38%)</td><td>0.17 (+18.30%)</td><td>0.10 (+15.31%)</td><td>0.04 <b>(+33.93%)</b></td><td>488.60 (-13.28%)</td><td>338.14 (-11.10%)</td><td>286.10 (-15.46%)</td><td>248.20 (-13.46%)</td><td>106.85 (-3.31%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>563.40 (n/a)</td><td>380.38 (n/a)</td><td>338.40 (n/a)</td><td>286.80 (n/a)</td><td>110.51 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>4.26 (+0.84%)</td><td>3.36 (-8.78%)</td><td>3.63 (-9.30%)</td><td>2.34 (-9.76%)</td><td>0.83 <b>(+27.71%)</b></td><td>4490.50 (+10.82%)</td><td>3300.26 (+12.20%)</td><td>2888.90 (+10.25%)</td><td>2463.50 (-0.83%)</td><td>888.30 <b>(+38.28%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>4.22 (n/a)</td><td>3.68 (n/a)</td><td>4.00 (n/a)</td><td>2.59 (n/a)</td><td>0.65 (n/a)</td><td>4052.20 (n/a)</td><td>2941.36 (n/a)</td><td>2620.20 (n/a)</td><td>2484.10 (n/a)</td><td>642.39 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.19 <b>(+29.89%)</b></td><td>0.12 (-1.66%)</td><td>0.09 <b>(-35.34%)</b></td><td>0.07 (+1.90%)</td><td>0.06 <b>(+76.68%)</b></td><td>588.70 (-1.85%)</td><td>404.98 (+11.73%)</td><td>448.10 <b>(+54.62%)</b></td><td>214.80 <b>(-23.01%)</b></td><td>173.10 <b>(+27.22%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>599.80 (n/a)</td><td>362.46 (n/a)</td><td>289.80 (n/a)</td><td>279.00 (n/a)</td><td>136.07 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (-3.85%)</td><td>0.02 (-4.66%)</td><td>0.02 (+3.29%)</td><td>0.01 <b>(+42.84%)</b></td><td>0.01 (-13.70%)</td><td>539.60 <b>(-29.99%)</b></td><td>356.66 (-3.76%)</td><td>278.60 (-3.20%)</td><td>247.30 (+4.04%)</td><td>131.53 <b>(-41.62%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>770.80 (n/a)</td><td>370.60 (n/a)</td><td>287.80 (n/a)</td><td>237.70 (n/a)</td><td>225.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (+12.69%)</td><td>0.01 (-16.50%)</td><td>0.01 <b>(-27.91%)</b></td><td>0.01 <b>(-36.97%)</b></td><td>0.01 <b>(+153.93%)</b></td><td>468.50 <b>(+58.65%)</b></td><td>352.64 <b>(+31.03%)</b></td><td>386.00 <b>(+38.70%)</b></td><td>192.10 (-11.27%)</td><td>110.42 <b>(+259.27%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>295.30 (n/a)</td><td>269.12 (n/a)</td><td>278.30 (n/a)</td><td>216.50 (n/a)</td><td>30.74 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (-7.37%)</td><td>0.01 (-3.33%)</td><td>0.01 (-11.56%)</td><td>0.01 <b>(+70.30%)</b></td><td>0.00 <b>(-42.92%)</b></td><td>601.00 <b>(-41.28%)</b></td><td>473.78 (-9.12%)</td><td>457.10 (+13.06%)</td><td>360.40 (+7.94%)</td><td>101.31 <b>(-64.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1023.50 (n/a)</td><td>521.34 (n/a)</td><td>404.30 (n/a)</td><td>333.90 (n/a)</td><td>287.70 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (-13.11%)</td><td>0.01 (-16.29%)</td><td>0.01 <b>(-27.41%)</b></td><td>0.01 (+1.54%)</td><td>0.00 <b>(-34.69%)</b></td><td>535.10 (-1.53%)</td><td>393.64 (+10.42%)</td><td>333.70 <b>(+37.72%)</b></td><td>258.80 (+15.07%)</td><td>128.18 <b>(-23.10%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>543.40 (n/a)</td><td>356.48 (n/a)</td><td>242.30 (n/a)</td><td>224.90 (n/a)</td><td>166.68 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (+4.01%)</td><td>0.01 (-13.22%)</td><td>0.01 <b>(-23.21%)</b></td><td>0.01 (+0.76%)</td><td>0.01 (+3.30%)</td><td>660.80 (-0.75%)</td><td>456.90 (+15.61%)</td><td>414.50 <b>(+30.22%)</b></td><td>229.10 (-3.86%)</td><td>179.26 (+1.04%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>665.80 (n/a)</td><td>395.20 (n/a)</td><td>318.30 (n/a)</td><td>238.30 (n/a)</td><td>177.41 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (-3.17%)</td><td>0.01 (+17.34%)</td><td>0.02 <b>(+77.89%)</b></td><td>0.01 (-16.35%)</td><td>0.01 (-6.86%)</td><td>660.40 (+19.55%)</td><td>332.34 (-12.84%)</td><td>249.70 <b>(-43.79%)</b></td><td>213.50 (+3.29%)</td><td>185.93 <b>(+26.70%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.40 (n/a)</td><td>381.32 (n/a)</td><td>444.20 (n/a)</td><td>206.70 (n/a)</td><td>146.75 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (-16.23%)</td><td>0.01 (-15.98%)</td><td>0.01 (+9.53%)</td><td>0.00 <b>(-66.27%)</b></td><td>0.01 (-6.62%)</td><td>1829.30 <b>(+196.48%)</b></td><td>668.70 <b>(+58.61%)</b></td><td>441.00 (-8.70%)</td><td>283.40 (+19.38%)</td><td>654.07 <b>(+282.91%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>617.00 (n/a)</td><td>421.60 (n/a)</td><td>483.00 (n/a)</td><td>237.40 (n/a)</td><td>170.82 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (+13.07%)</td><td>0.01 <b>(+28.55%)</b></td><td>0.02 <b>(+67.67%)</b></td><td>0.00 <b>(-43.75%)</b></td><td>0.01 <b>(+49.09%)</b></td><td>1776.80 <b>(+77.79%)</b></td><td>582.44 (+12.65%)</td><td>264.90 <b>(-40.35%)</b></td><td>247.30 (-11.55%)</td><td>669.17 <b>(+135.71%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>999.40 (n/a)</td><td>517.02 (n/a)</td><td>444.10 (n/a)</td><td>279.60 (n/a)</td><td>283.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (-14.47%)</td><td>0.01 <b>(-29.92%)</b></td><td>0.01 <b>(-38.94%)</b></td><td>0.00 <b>(-36.80%)</b></td><td>0.00 (+4.68%)</td><td>1011.80 <b>(+58.22%)</b></td><td>649.38 <b>(+60.17%)</b></td><td>568.20 <b>(+63.79%)</b></td><td>312.00 (+16.90%)</td><td>331.73 <b>(+109.02%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>639.50 (n/a)</td><td>405.44 (n/a)</td><td>346.90 (n/a)</td><td>266.90 (n/a)</td><td>158.71 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (-0.99%)</td><td>0.01 (+15.79%)</td><td>0.01 (+15.52%)</td><td>0.01 (+11.43%)</td><td>0.00 (+2.93%)</td><td>574.00 (-10.27%)</td><td>415.44 (-12.74%)</td><td>428.20 (-13.42%)</td><td>232.70 (+1.00%)</td><td>158.50 (+4.62%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>639.70 (n/a)</td><td>476.08 (n/a)</td><td>494.60 (n/a)</td><td>230.40 (n/a)</td><td>151.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (-4.35%)</td><td>0.01 (-8.20%)</td><td>0.01 (-5.85%)</td><td>0.01 (-15.51%)</td><td>0.00 (-10.58%)</td><td>668.80 (+18.35%)</td><td>452.28 (+8.43%)</td><td>472.40 (+6.23%)</td><td>268.00 (+4.56%)</td><td>158.02 (+9.33%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>565.10 (n/a)</td><td>417.12 (n/a)</td><td>444.70 (n/a)</td><td>256.30 (n/a)</td><td>144.53 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (-0.25%)</td><td>0.01 (+4.46%)</td><td>0.01 (+14.96%)</td><td>0.01 (-14.41%)</td><td>0.00 (+18.82%)</td><td>573.80 (+16.84%)</td><td>418.52 (-1.06%)</td><td>391.50 (-13.00%)</td><td>272.60 (+0.26%)</td><td>129.10 <b>(+49.66%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.10 (n/a)</td><td>423.00 (n/a)</td><td>450.00 (n/a)</td><td>271.90 (n/a)</td><td>86.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (-8.81%)</td><td>0.03 (-15.81%)</td><td>0.03 (-7.97%)</td><td>0.02 <b>(-37.31%)</b></td><td>0.01 <b>(+86.87%)</b></td><td>457.10 <b>(+59.55%)</b></td><td>321.32 <b>(+22.80%)</b></td><td>288.10 (+8.68%)</td><td>259.80 (+9.67%)</td><td>79.13 <b>(+240.89%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>286.50 (n/a)</td><td>261.66 (n/a)</td><td>265.10 (n/a)</td><td>236.90 (n/a)</td><td>23.21 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 <b>(+22.94%)</b></td><td>0.04 (+6.58%)</td><td>0.03 <b>(-20.37%)</b></td><td>0.02 (-6.86%)</td><td>0.02 <b>(+55.28%)</b></td><td>599.70 (+7.36%)</td><td>418.56 (+4.96%)</td><td>476.90 <b>(+25.60%)</b></td><td>193.90 (-18.67%)</td><td>196.56 <b>(+33.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>558.60 (n/a)</td><td>398.78 (n/a)</td><td>379.70 (n/a)</td><td>238.40 (n/a)</td><td>146.93 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 <b>(+25.84%)</b></td><td>0.03 <b>(+24.01%)</b></td><td>0.03 <b>(+22.32%)</b></td><td>0.02 <b>(+23.74%)</b></td><td>0.01 (+0.51%)</td><td>503.60 (-19.19%)</td><td>288.18 <b>(-23.60%)</b></td><td>246.60 (-18.24%)</td><td>172.80 <b>(-20.52%)</b></td><td>126.64 <b>(-30.31%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.20 (n/a)</td><td>377.20 (n/a)</td><td>301.60 (n/a)</td><td>217.40 (n/a)</td><td>181.72 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (+6.07%)</td><td>0.02 (+13.25%)</td><td>0.02 (+1.21%)</td><td>0.01 <b>(+87.70%)</b></td><td>0.01 (+5.33%)</td><td>1004.50 <b>(-46.72%)</b></td><td>520.92 <b>(-26.81%)</b></td><td>470.70 (-1.18%)</td><td>272.10 (-5.72%)</td><td>294.94 <b>(-55.37%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1885.40 (n/a)</td><td>711.76 (n/a)</td><td>476.30 (n/a)</td><td>288.60 (n/a)</td><td>660.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 <b>(+41.90%)</b></td><td>0.03 <b>(+59.34%)</b></td><td>0.03 <b>(+41.70%)</b></td><td>0.03 <b>(+116.04%)</b></td><td>0.00 <b>(-34.69%)</b></td><td>274.30 <b>(-53.71%)</b></td><td>240.64 <b>(-41.85%)</b></td><td>247.50 <b>(-29.45%)</b></td><td>199.10 <b>(-29.52%)</b></td><td>29.39 <b>(-79.21%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.60 (n/a)</td><td>413.84 (n/a)</td><td>350.80 (n/a)</td><td>282.50 (n/a)</td><td>141.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (-1.84%)</td><td>0.03 (+11.18%)</td><td>0.03 <b>(+39.46%)</b></td><td>0.02 <b>(+34.32%)</b></td><td>0.01 <b>(-27.95%)</b></td><td>450.10 <b>(-25.54%)</b></td><td>333.10 (-15.27%)</td><td>302.70 <b>(-28.30%)</b></td><td>256.00 (+1.87%)</td><td>82.82 <b>(-42.45%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>604.50 (n/a)</td><td>393.12 (n/a)</td><td>422.20 (n/a)</td><td>251.30 (n/a)</td><td>143.90 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (-0.71%)</td><td>0.02 (+16.44%)</td><td>0.03 <b>(+44.72%)</b></td><td>0.01 (-8.57%)</td><td>0.01 (+2.87%)</td><td>599.30 (+9.36%)</td><td>366.14 (-12.12%)</td><td>302.20 <b>(-30.89%)</b></td><td>231.50 (+0.74%)</td><td>145.86 <b>(+26.05%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>548.00 (n/a)</td><td>416.62 (n/a)</td><td>437.30 (n/a)</td><td>229.80 (n/a)</td><td>115.71 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 <b>(+48.21%)</b></td><td>0.03 <b>(+21.16%)</b></td><td>0.03 <b>(+21.55%)</b></td><td>0.02 (-18.38%)</td><td>0.01 <b>(+303.42%)</b></td><td>563.10 <b>(+22.52%)</b></td><td>385.18 (-9.72%)</td><td>352.90 (-17.72%)</td><td>244.10 <b>(-32.51%)</b></td><td>134.47 <b>(+236.98%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>459.60 (n/a)</td><td>426.64 (n/a)</td><td>428.90 (n/a)</td><td>361.70 (n/a)</td><td>39.91 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 <b>(-28.76%)</b></td><td>0.02 (-17.84%)</td><td>0.02 (+1.29%)</td><td>0.01 <b>(-27.26%)</b></td><td>0.01 <b>(-35.42%)</b></td><td>775.40 <b>(+37.48%)</b></td><td>513.82 (+19.68%)</td><td>455.30 (-1.28%)</td><td>335.50 <b>(+40.38%)</b></td><td>169.41 <b>(+28.06%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.00 (n/a)</td><td>429.32 (n/a)</td><td>461.20 (n/a)</td><td>239.00 (n/a)</td><td>132.29 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (-6.02%)</td><td>0.02 (+11.33%)</td><td>0.03 <b>(+50.97%)</b></td><td>0.01 <b>(+177.20%)</b></td><td>0.01 <b>(-33.90%)</b></td><td>673.20 <b>(-63.93%)</b></td><td>415.76 <b>(-38.89%)</b></td><td>321.50 <b>(-33.77%)</b></td><td>271.10 (+6.44%)</td><td>170.42 <b>(-74.72%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1866.20 (n/a)</td><td>680.34 (n/a)</td><td>485.40 (n/a)</td><td>254.70 (n/a)</td><td>674.28 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (+9.08%)</td><td>0.02 (+17.87%)</td><td>0.02 (+11.37%)</td><td>0.01 <b>(+34.39%)</b></td><td>0.01 (+19.81%)</td><td>977.00 <b>(-25.59%)</b></td><td>513.90 (-16.62%)</td><td>441.30 (-10.21%)</td><td>261.40 (-8.35%)</td><td>290.98 <b>(-27.31%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1313.00 (n/a)</td><td>616.36 (n/a)</td><td>491.50 (n/a)</td><td>285.20 (n/a)</td><td>400.33 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (+15.50%)</td><td>0.06 <b>(+30.14%)</b></td><td>0.07 <b>(+70.75%)</b></td><td>0.03 (-11.20%)</td><td>0.02 (+16.08%)</td><td>579.70 (+12.63%)</td><td>314.10 <b>(-20.67%)</b></td><td>249.60 <b>(-41.45%)</b></td><td>208.50 (-13.41%)</td><td>151.30 (+18.26%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>514.70 (n/a)</td><td>395.96 (n/a)</td><td>426.30 (n/a)</td><td>240.80 (n/a)</td><td>127.94 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.10 <b>(+73.27%)</b></td><td>0.08 <b>(+127.49%)</b></td><td>0.08 <b>(+121.17%)</b></td><td>0.07 <b>(+409.70%)</b></td><td>0.01 <b>(-37.01%)</b></td><td>375.10 <b>(-80.38%)</b></td><td>311.26 <b>(-65.89%)</b></td><td>308.50 <b>(-54.79%)</b></td><td>257.70 <b>(-42.28%)</b></td><td>42.57 <b>(-92.90%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1911.80 (n/a)</td><td>912.58 (n/a)</td><td>682.40 (n/a)</td><td>446.50 (n/a)</td><td>599.33 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.09 <b>(+49.18%)</b></td><td>0.06 (+15.63%)</td><td>0.06 (+12.47%)</td><td>0.03 <b>(-21.50%)</b></td><td>0.03 <b>(+115.16%)</b></td><td>619.90 <b>(+27.39%)</b></td><td>369.24 (+2.49%)</td><td>263.50 (-11.07%)</td><td>178.70 <b>(-32.97%)</b></td><td>201.02 <b>(+91.96%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>486.60 (n/a)</td><td>360.26 (n/a)</td><td>296.30 (n/a)</td><td>266.60 (n/a)</td><td>104.72 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (-14.80%)</td><td>0.05 <b>(-27.66%)</b></td><td>0.04 <b>(-40.45%)</b></td><td>0.03 (-12.55%)</td><td>0.02 <b>(-33.49%)</b></td><td>593.60 (+14.35%)</td><td>468.42 <b>(+31.45%)</b></td><td>467.80 <b>(+67.97%)</b></td><td>282.20 (+17.39%)</td><td>119.77 (-14.99%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>519.10 (n/a)</td><td>356.36 (n/a)</td><td>278.50 (n/a)</td><td>240.40 (n/a)</td><td>140.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (+0.76%)</td><td>0.05 (+14.12%)</td><td>0.07 <b>(+77.43%)</b></td><td>0.02 <b>(-40.55%)</b></td><td>0.03 <b>(+57.65%)</b></td><td>1032.70 <b>(+68.19%)</b></td><td>475.16 (+12.62%)</td><td>246.80 <b>(-43.64%)</b></td><td>235.00 (-0.76%)</td><td>350.85 <b>(+150.72%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>614.00 (n/a)</td><td>421.92 (n/a)</td><td>437.90 (n/a)</td><td>236.80 (n/a)</td><td>139.94 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (+7.58%)</td><td>0.05 (-1.59%)</td><td>0.05 (-0.37%)</td><td>0.03 (-11.49%)</td><td>0.02 <b>(+29.50%)</b></td><td>592.70 (+12.98%)</td><td>455.08 (+5.96%)</td><td>453.10 (+0.35%)</td><td>253.50 (-7.04%)</td><td>141.91 <b>(+41.16%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>524.60 (n/a)</td><td>429.50 (n/a)</td><td>451.50 (n/a)</td><td>272.70 (n/a)</td><td>100.53 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (+13.04%)</td><td>0.05 <b>(+25.89%)</b></td><td>0.05 (+17.26%)</td><td>0.03 <b>(+36.31%)</b></td><td>0.01 (-2.70%)</td><td>566.80 <b>(-26.64%)</b></td><td>352.88 <b>(-23.94%)</b></td><td>314.20 (-14.71%)</td><td>250.80 (-11.53%)</td><td>125.42 <b>(-35.89%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>772.60 (n/a)</td><td>463.92 (n/a)</td><td>368.40 (n/a)</td><td>283.50 (n/a)</td><td>195.62 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (-6.58%)</td><td>0.04 (-16.36%)</td><td>0.04 <b>(-33.30%)</b></td><td>0.03 (-19.40%)</td><td>0.02 (+14.55%)</td><td>707.00 <b>(+24.08%)</b></td><td>473.80 <b>(+25.26%)</b></td><td>475.30 <b>(+49.94%)</b></td><td>294.00 (+7.06%)</td><td>181.17 <b>(+44.25%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>569.80 (n/a)</td><td>378.24 (n/a)</td><td>317.00 (n/a)</td><td>274.60 (n/a)</td><td>125.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 <b>(-45.60%)</b></td><td>0.03 <b>(-27.83%)</b></td><td>0.03 (-5.75%)</td><td>0.03 (-8.38%)</td><td>0.00 <b>(-77.83%)</b></td><td>630.70 (+9.16%)</td><td>538.60 <b>(+22.63%)</b></td><td>544.20 (+6.10%)</td><td>443.20 <b>(+83.82%)</b></td><td>69.39 <b>(-57.34%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>577.80 (n/a)</td><td>439.20 (n/a)</td><td>512.90 (n/a)</td><td>241.10 (n/a)</td><td>162.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 <b>(-38.80%)</b></td><td>0.03 <b>(-40.16%)</b></td><td>0.04 (-13.84%)</td><td>0.01 <b>(-75.13%)</b></td><td>0.01 <b>(-21.81%)</b></td><td>1973.70 <b>(+302.06%)</b></td><td>802.60 <b>(+110.97%)</b></td><td>509.80 (+16.05%)</td><td>413.10 <b>(+63.41%)</b></td><td>659.14 <b>(+484.23%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>490.90 (n/a)</td><td>380.44 (n/a)</td><td>439.30 (n/a)</td><td>252.80 (n/a)</td><td>112.82 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 <b>(+23.32%)</b></td><td>0.04 <b>(+42.21%)</b></td><td>0.04 <b>(+58.07%)</b></td><td>0.03 <b>(+44.15%)</b></td><td>0.01 (-2.28%)</td><td>505.50 <b>(-30.62%)</b></td><td>386.76 <b>(-31.29%)</b></td><td>366.30 <b>(-36.75%)</b></td><td>292.10 (-18.93%)</td><td>77.95 <b>(-42.04%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>728.60 (n/a)</td><td>562.92 (n/a)</td><td>579.10 (n/a)</td><td>360.30 (n/a)</td><td>134.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (+2.18%)</td><td>0.10 (+5.12%)</td><td>0.10 (-6.89%)</td><td>0.06 (+11.68%)</td><td>0.04 (-3.39%)</td><td>548.30 (-10.47%)</td><td>383.52 (-7.78%)</td><td>339.20 (+7.41%)</td><td>233.40 (-2.10%)</td><td>145.85 (-19.57%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>612.40 (n/a)</td><td>415.88 (n/a)</td><td>315.80 (n/a)</td><td>238.40 (n/a)</td><td>181.34 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.12 <b>(-27.54%)</b></td><td>0.04 <b>(-56.39%)</b></td><td>0.02 <b>(-84.99%)</b></td><td>0.02 <b>(-70.31%)</b></td><td>0.04 (-2.86%)</td><td>2027.10 <b>(+236.78%)</b></td><td>1350.30 <b>(+252.01%)</b></td><td>1888.00 <b>(+566.43%)</b></td><td>276.10 <b>(+38.05%)</b></td><td>838.50 <b>(+361.39%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>601.90 (n/a)</td><td>383.60 (n/a)</td><td>283.30 (n/a)</td><td>200.00 (n/a)</td><td>181.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.15 (+17.05%)</td><td>0.10 (+0.49%)</td><td>0.09 (+2.14%)</td><td>0.07 (+18.00%)</td><td>0.03 (+7.80%)</td><td>565.00 (-15.25%)</td><td>441.88 (-1.58%)</td><td>449.70 (-2.11%)</td><td>267.90 (-14.57%)</td><td>113.66 <b>(-21.03%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>666.70 (n/a)</td><td>448.98 (n/a)</td><td>459.40 (n/a)</td><td>313.60 (n/a)</td><td>143.94 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 <b>(-52.59%)</b></td><td>0.05 <b>(-42.69%)</b></td><td>0.06 <b>(-32.08%)</b></td><td>0.02 <b>(-69.61%)</b></td><td>0.02 <b>(-41.83%)</b></td><td>2029.80 <b>(+228.98%)</b></td><td>825.34 <b>(+106.91%)</b></td><td>539.30 <b>(+47.23%)</b></td><td>483.20 <b>(+110.91%)</b></td><td>673.74 <b>(+329.75%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>617.00 (n/a)</td><td>398.88 (n/a)</td><td>366.30 (n/a)</td><td>229.10 (n/a)</td><td>156.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.17 (+0.59%)</td><td>0.12 (-8.65%)</td><td>0.14 (+7.30%)</td><td>0.05 <b>(-40.57%)</b></td><td>0.05 <b>(+40.71%)</b></td><td>800.90 <b>(+68.29%)</b></td><td>451.22 <b>(+28.20%)</b></td><td>300.50 (-6.79%)</td><td>237.90 (-0.59%)</td><td>256.77 <b>(+130.45%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>475.90 (n/a)</td><td>351.96 (n/a)</td><td>322.40 (n/a)</td><td>239.30 (n/a)</td><td>111.42 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 <b>(-23.90%)</b></td><td>0.10 (+9.66%)</td><td>0.09 <b>(+37.97%)</b></td><td>0.09 <b>(+68.69%)</b></td><td>0.01 <b>(-72.81%)</b></td><td>382.80 <b>(-40.72%)</b></td><td>348.02 <b>(-20.97%)</b></td><td>366.20 <b>(-27.51%)</b></td><td>304.80 <b>(+31.44%)</b></td><td>37.91 <b>(-78.41%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>645.70 (n/a)</td><td>440.36 (n/a)</td><td>505.20 (n/a)</td><td>231.90 (n/a)</td><td>175.56 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.16 <b>(-25.93%)</b></td><td>0.09 <b>(-22.60%)</b></td><td>0.07 (-11.17%)</td><td>0.06 (-18.41%)</td><td>0.04 <b>(-32.40%)</b></td><td>604.90 <b>(+22.55%)</b></td><td>458.52 <b>(+23.40%)</b></td><td>516.80 (+12.59%)</td><td>231.10 <b>(+34.99%)</b></td><td>167.51 (+9.43%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>493.60 (n/a)</td><td>371.56 (n/a)</td><td>459.00 (n/a)</td><td>171.20 (n/a)</td><td>153.07 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 (-16.86%)</td><td>0.06 <b>(-41.59%)</b></td><td>0.07 <b>(-40.67%)</b></td><td>0.01 <b>(-66.33%)</b></td><td>0.04 (+1.84%)</td><td>2487.20 <b>(+197.01%)</b></td><td>1131.54 <b>(+164.71%)</b></td><td>487.10 <b>(+68.55%)</b></td><td>302.00 <b>(+20.27%)</b></td><td>996.30 <b>(+301.46%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>837.40 (n/a)</td><td>427.46 (n/a)</td><td>289.00 (n/a)</td><td>251.10 (n/a)</td><td>248.17 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.18 (+0.62%)</td><td>0.12 <b>(+22.56%)</b></td><td>0.12 <b>(+64.61%)</b></td><td>0.07 (+13.08%)</td><td>0.04 (-13.71%)</td><td>516.90 (-11.57%)</td><td>330.02 <b>(-22.09%)</b></td><td>301.20 <b>(-39.25%)</b></td><td>206.90 (-0.58%)</td><td>120.38 <b>(-22.49%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>584.50 (n/a)</td><td>423.60 (n/a)</td><td>495.80 (n/a)</td><td>208.10 (n/a)</td><td>155.30 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.12 (+15.06%)</td><td>0.07 (-12.14%)</td><td>0.06 (-15.00%)</td><td>0.02 <b>(-59.81%)</b></td><td>0.05 <b>(+101.47%)</b></td><td>1871.40 <b>(+148.79%)</b></td><td>959.48 <b>(+101.39%)</b></td><td>556.70 (+17.65%)</td><td>263.60 (-13.09%)</td><td>818.01 <b>(+365.13%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>752.20 (n/a)</td><td>476.42 (n/a)</td><td>473.20 (n/a)</td><td>303.30 (n/a)</td><td>175.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (+9.90%)</td><td>0.06 (+6.18%)</td><td>0.06 (-2.62%)</td><td>0.04 (+10.50%)</td><td>0.02 (-9.45%)</td><td>501.60 (-9.51%)</td><td>366.82 (-8.33%)</td><td>343.50 (+2.69%)</td><td>262.00 (-9.00%)</td><td>98.15 <b>(-25.80%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>554.30 (n/a)</td><td>400.14 (n/a)</td><td>334.50 (n/a)</td><td>287.90 (n/a)</td><td>132.28 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (-9.89%)</td><td>0.05 (-14.42%)</td><td>0.04 <b>(-23.77%)</b></td><td>0.02 <b>(-41.30%)</b></td><td>0.02 (+13.25%)</td><td>968.90 <b>(+70.37%)</b></td><td>519.98 <b>(+29.48%)</b></td><td>504.50 <b>(+31.18%)</b></td><td>283.60 (+11.00%)</td><td>277.28 <b>(+102.60%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>568.70 (n/a)</td><td>401.60 (n/a)</td><td>384.60 (n/a)</td><td>255.50 (n/a)</td><td>136.86 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 <b>(+22.14%)</b></td><td>0.06 (+13.33%)</td><td>0.05 (+9.78%)</td><td>0.04 (-10.65%)</td><td>0.02 <b>(+59.32%)</b></td><td>567.80 (+11.93%)</td><td>405.96 (-7.51%)</td><td>452.20 (-8.92%)</td><td>246.90 (-18.11%)</td><td>127.46 <b>(+39.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>507.30 (n/a)</td><td>438.94 (n/a)</td><td>496.50 (n/a)</td><td>301.50 (n/a)</td><td>91.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 <b>(-48.18%)</b></td><td>0.04 <b>(-31.35%)</b></td><td>0.04 <b>(-28.91%)</b></td><td>0.03 (+7.81%)</td><td>0.00 <b>(-91.71%)</b></td><td>585.50 (-7.24%)</td><td>544.14 <b>(+27.89%)</b></td><td>542.00 <b>(+40.67%)</b></td><td>514.60 <b>(+92.95%)</b></td><td>26.30 <b>(-84.65%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>631.20 (n/a)</td><td>425.46 (n/a)</td><td>385.30 (n/a)</td><td>266.70 (n/a)</td><td>171.25 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (+12.66%)</td><td>0.07 (+18.31%)</td><td>0.08 <b>(+56.86%)</b></td><td>0.04 (-5.82%)</td><td>0.02 <b>(+26.06%)</b></td><td>534.70 (+6.18%)</td><td>346.36 (-12.83%)</td><td>270.40 <b>(-36.24%)</b></td><td>243.00 (-11.25%)</td><td>130.49 (+16.59%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>503.60 (n/a)</td><td>397.32 (n/a)</td><td>424.10 (n/a)</td><td>273.80 (n/a)</td><td>111.92 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 <b>(-44.11%)</b></td><td>0.04 <b>(-34.00%)</b></td><td>0.04 (-19.78%)</td><td>0.02 <b>(-41.08%)</b></td><td>0.01 <b>(-50.80%)</b></td><td>1036.10 <b>(+69.71%)</b></td><td>623.74 <b>(+47.99%)</b></td><td>573.00 <b>(+24.65%)</b></td><td>436.10 <b>(+78.95%)</b></td><td>239.78 <b>(+60.00%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>610.50 (n/a)</td><td>421.48 (n/a)</td><td>459.70 (n/a)</td><td>243.70 (n/a)</td><td>149.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.10 (-17.74%)</td><td>0.06 <b>(-21.37%)</b></td><td>0.05 <b>(-36.49%)</b></td><td>0.04 <b>(-20.86%)</b></td><td>0.03 (-15.93%)</td><td>589.00 <b>(+26.34%)</b></td><td>423.48 <b>(+27.49%)</b></td><td>480.90 <b>(+57.47%)</b></td><td>237.80 <b>(+21.57%)</b></td><td>145.09 <b>(+21.22%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>466.20 (n/a)</td><td>332.18 (n/a)</td><td>305.40 (n/a)</td><td>195.60 (n/a)</td><td>119.69 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (-12.59%)</td><td>0.06 <b>(-27.09%)</b></td><td>0.05 <b>(-38.17%)</b></td><td>0.04 <b>(-23.15%)</b></td><td>0.02 <b>(+23.46%)</b></td><td>591.10 <b>(+30.11%)</b></td><td>469.28 <b>(+41.82%)</b></td><td>496.40 <b>(+61.75%)</b></td><td>320.30 (+14.43%)</td><td>124.69 <b>(+78.15%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>454.30 (n/a)</td><td>330.90 (n/a)</td><td>306.90 (n/a)</td><td>279.90 (n/a)</td><td>69.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.09 (-7.59%)</td><td>0.06 (-4.25%)</td><td>0.07 (-15.65%)</td><td>0.02 <b>(+84.28%)</b></td><td>0.03 <b>(-30.82%)</b></td><td>1067.90 <b>(-45.74%)</b></td><td>477.94 <b>(-26.76%)</b></td><td>342.00 (+18.54%)</td><td>277.40 (+8.19%)</td><td>331.96 <b>(-55.25%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1968.00 (n/a)</td><td>652.54 (n/a)</td><td>288.50 (n/a)</td><td>256.40 (n/a)</td><td>741.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.10 (+14.58%)</td><td>0.07 (+1.66%)</td><td>0.05 (-14.38%)</td><td>0.04 (-1.48%)</td><td>0.03 <b>(+59.58%)</b></td><td>568.00 (+1.48%)</td><td>417.52 (+4.33%)</td><td>471.50 (+16.79%)</td><td>246.90 (-12.69%)</td><td>141.79 <b>(+38.27%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>559.70 (n/a)</td><td>400.18 (n/a)</td><td>403.70 (n/a)</td><td>282.80 (n/a)</td><td>102.54 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 <b>(-37.93%)</b></td><td>0.05 (-18.43%)</td><td>0.06 <b>(+32.30%)</b></td><td>0.04 (-6.70%)</td><td>0.01 <b>(-66.32%)</b></td><td>665.70 (+7.18%)</td><td>495.72 (+6.82%)</td><td>433.10 <b>(-24.42%)</b></td><td>401.10 <b>(+61.08%)</b></td><td>111.64 <b>(-41.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>621.10 (n/a)</td><td>464.08 (n/a)</td><td>573.00 (n/a)</td><td>249.00 (n/a)</td><td>191.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (-10.52%)</td><td>0.05 <b>(-28.96%)</b></td><td>0.06 <b>(-25.96%)</b></td><td>0.01 <b>(-77.17%)</b></td><td>0.03 <b>(+106.16%)</b></td><td>1836.20 <b>(+338.13%)</b></td><td>677.94 <b>(+108.33%)</b></td><td>407.90 <b>(+35.07%)</b></td><td>299.70 (+11.79%)</td><td>651.13 <b>(+1010.32%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>419.10 (n/a)</td><td>325.42 (n/a)</td><td>302.00 (n/a)</td><td>268.10 (n/a)</td><td>58.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 <b>(-22.11%)</b></td><td>0.04 <b>(-39.49%)</b></td><td>0.04 <b>(-48.25%)</b></td><td>0.02 <b>(-54.48%)</b></td><td>0.02 (+5.11%)</td><td>1033.70 <b>(+119.70%)</b></td><td>559.08 <b>(+88.98%)</b></td><td>525.90 <b>(+93.20%)</b></td><td>247.50 <b>(+28.44%)</b></td><td>296.40 <b>(+183.45%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>470.50 (n/a)</td><td>295.84 (n/a)</td><td>272.20 (n/a)</td><td>192.70 (n/a)</td><td>104.57 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (-1.97%)</td><td>0.06 (-16.66%)</td><td>0.06 (-4.26%)</td><td>0.04 <b>(-39.48%)</b></td><td>0.02 <b>(+90.85%)</b></td><td>495.80 <b>(+65.21%)</b></td><td>358.30 <b>(+30.78%)</b></td><td>308.10 (+4.44%)</td><td>218.60 (+2.01%)</td><td>127.06 <b>(+245.76%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>300.10 (n/a)</td><td>273.98 (n/a)</td><td>295.00 (n/a)</td><td>214.30 (n/a)</td><td>36.75 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (-0.94%)</td><td>0.06 (+0.92%)</td><td>0.07 (+18.15%)</td><td>0.04 <b>(-21.68%)</b></td><td>0.02 <b>(+63.12%)</b></td><td>500.30 <b>(+27.66%)</b></td><td>344.00 (+6.56%)</td><td>258.80 (-15.34%)</td><td>241.00 (+0.92%)</td><td>129.19 <b>(+107.72%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>391.90 (n/a)</td><td>322.82 (n/a)</td><td>305.70 (n/a)</td><td>238.80 (n/a)</td><td>62.20 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (+17.55%)</td><td>0.05 (-13.06%)</td><td>0.03 <b>(-43.20%)</b></td><td>0.03 <b>(-23.50%)</b></td><td>0.02 <b>(+77.47%)</b></td><td>570.20 <b>(+30.69%)</b></td><td>440.82 <b>(+25.74%)</b></td><td>537.00 <b>(+76.07%)</b></td><td>243.80 (-14.93%)</td><td>156.53 <b>(+101.24%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>436.30 (n/a)</td><td>350.58 (n/a)</td><td>305.00 (n/a)</td><td>286.60 (n/a)</td><td>77.78 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 <b>(-49.17%)</b></td><td>0.04 <b>(-33.23%)</b></td><td>0.04 <b>(-38.78%)</b></td><td>0.04 (+4.78%)</td><td>0.01 <b>(-76.03%)</b></td><td>514.10 (-4.57%)</td><td>468.60 <b>(+30.33%)</b></td><td>499.00 <b>(+63.34%)</b></td><td>359.70 <b>(+96.66%)</b></td><td>64.31 <b>(-57.74%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>538.70 (n/a)</td><td>359.54 (n/a)</td><td>305.50 (n/a)</td><td>182.90 (n/a)</td><td>152.18 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (-4.75%)</td><td>0.04 (-15.23%)</td><td>0.04 (-17.22%)</td><td>0.01 <b>(-49.89%)</b></td><td>0.02 (+13.88%)</td><td>2154.40 <b>(+99.57%)</b></td><td>773.60 <b>(+55.55%)</b></td><td>449.90 <b>(+20.78%)</b></td><td>263.80 (+4.97%)</td><td>783.91 <b>(+136.42%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1079.50 (n/a)</td><td>497.32 (n/a)</td><td>372.50 (n/a)</td><td>251.30 (n/a)</td><td>331.58 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.43 <b>(+21.78%)</b></td><td>0.25 (+1.93%)</td><td>0.21 (-0.41%)</td><td>0.04 <b>(-75.42%)</b></td><td>0.16 <b>(+97.45%)</b></td><td>2392.30 <b>(+306.85%)</b></td><td>777.38 <b>(+78.14%)</b></td><td>472.30 (+0.40%)</td><td>229.40 (-17.87%)</td><td>912.56 <b>(+594.07%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>588.00 (n/a)</td><td>436.38 (n/a)</td><td>470.40 (n/a)</td><td>279.30 (n/a)</td><td>131.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.31 <b>(+33.97%)</b></td><td>0.24 <b>(+57.07%)</b></td><td>0.19 (+13.15%)</td><td>0.19 <b>(+268.58%)</b></td><td>0.07 (-12.20%)</td><td>527.70 <b>(-72.87%)</b></td><td>439.22 <b>(-50.74%)</b></td><td>515.60 (-11.62%)</td><td>313.00 <b>(-25.35%)</b></td><td>113.67 <b>(-82.18%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>0.08 (n/a)</td><td>1944.90 (n/a)</td><td>891.58 (n/a)</td><td>583.40 (n/a)</td><td>419.30 (n/a)</td><td>637.93 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.32 <b>(-23.32%)</b></td><td>0.18 <b>(-36.70%)</b></td><td>0.19 <b>(-21.62%)</b></td><td>0.08 <b>(-58.84%)</b></td><td>0.09 (+1.86%)</td><td>1164.90 <b>(+142.99%)</b></td><td>691.10 <b>(+84.83%)</b></td><td>513.90 <b>(+27.58%)</b></td><td>312.10 <b>(+30.42%)</b></td><td>368.07 <b>(+237.72%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.41 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>479.40 (n/a)</td><td>373.92 (n/a)</td><td>402.80 (n/a)</td><td>239.30 (n/a)</td><td>108.99 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.29 (+6.25%)</td><td>0.18 (-14.74%)</td><td>0.15 <b>(-38.01%)</b></td><td>0.13 (-3.93%)</td><td>0.06 (+5.51%)</td><td>553.00 (+4.08%)</td><td>442.20 (+17.62%)</td><td>486.90 <b>(+61.33%)</b></td><td>258.40 (-5.90%)</td><td>116.86 (-0.20%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>531.30 (n/a)</td><td>375.96 (n/a)</td><td>301.80 (n/a)</td><td>274.60 (n/a)</td><td>117.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.36 <b>(+135.15%)</b></td><td>0.25 <b>(+106.79%)</b></td><td>0.28 <b>(+101.89%)</b></td><td>0.13 <b>(+230.66%)</b></td><td>0.10 <b>(+124.51%)</b></td><td>577.10 <b>(-69.76%)</b></td><td>352.84 <b>(-56.13%)</b></td><td>267.20 <b>(-50.46%)</b></td><td>203.00 <b>(-57.47%)</b></td><td>167.95 <b>(-72.82%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>1908.20 (n/a)</td><td>804.28 (n/a)</td><td>539.40 (n/a)</td><td>477.30 (n/a)</td><td>617.87 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.23 <b>(-37.47%)</b></td><td>0.18 (-18.79%)</td><td>0.16 (-6.83%)</td><td>0.16 <b>(+76.11%)</b></td><td>0.03 <b>(-71.27%)</b></td><td>471.60 <b>(-43.21%)</b></td><td>413.94 (-2.99%)</td><td>459.00 (+7.32%)</td><td>314.20 <b>(+59.90%)</b></td><td>70.75 <b>(-72.09%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.38 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.12 (n/a)</td><td>830.50 (n/a)</td><td>426.68 (n/a)</td><td>427.70 (n/a)</td><td>196.50 (n/a)</td><td>253.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.15 (+9.70%)</td><td>0.10 <b>(+22.43%)</b></td><td>0.08 (+5.66%)</td><td>0.06 <b>(+34.05%)</b></td><td>0.04 <b>(+24.02%)</b></td><td>582.90 <b>(-25.40%)</b></td><td>428.68 (-17.04%)</td><td>486.70 (-5.35%)</td><td>250.80 (-8.87%)</td><td>156.10 (-13.04%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>781.40 (n/a)</td><td>516.76 (n/a)</td><td>514.20 (n/a)</td><td>275.20 (n/a)</td><td>179.51 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (+18.34%)</td><td>0.10 (+0.14%)</td><td>0.12 (+1.21%)</td><td>0.07 (-16.19%)</td><td>0.03 <b>(+84.19%)</b></td><td>529.00 (+19.31%)</td><td>385.74 (+6.44%)</td><td>316.00 (-1.19%)</td><td>263.10 (-15.51%)</td><td>131.80 <b>(+99.47%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>443.40 (n/a)</td><td>362.40 (n/a)</td><td>319.80 (n/a)</td><td>311.40 (n/a)</td><td>66.07 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.16 (-7.38%)</td><td>0.11 (-14.68%)</td><td>0.13 (-12.46%)</td><td>0.06 (-17.55%)</td><td>0.04 (+10.89%)</td><td>644.90 <b>(+21.29%)</b></td><td>372.74 <b>(+22.77%)</b></td><td>281.60 (+14.19%)</td><td>233.10 (+7.97%)</td><td>175.32 <b>(+35.07%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>531.70 (n/a)</td><td>303.60 (n/a)</td><td>246.60 (n/a)</td><td>215.90 (n/a)</td><td>129.80 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.15 (+4.75%)</td><td>0.09 (-1.60%)</td><td>0.07 (-8.61%)</td><td>0.06 <b>(+194.66%)</b></td><td>0.04 <b>(-26.13%)</b></td><td>621.60 <b>(-66.06%)</b></td><td>466.78 <b>(-30.06%)</b></td><td>521.20 (+9.43%)</td><td>247.60 (-4.55%)</td><td>144.05 <b>(-78.15%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1831.50 (n/a)</td><td>667.42 (n/a)</td><td>476.30 (n/a)</td><td>259.40 (n/a)</td><td>659.15 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.18 (+13.88%)</td><td>0.09 (-17.79%)</td><td>0.07 (-13.26%)</td><td>0.05 <b>(-25.08%)</b></td><td>0.05 (+17.42%)</td><td>776.80 <b>(+33.49%)</b></td><td>526.34 <b>(+29.82%)</b></td><td>496.80 (+15.29%)</td><td>204.50 (-12.16%)</td><td>217.30 <b>(+34.16%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>581.90 (n/a)</td><td>405.44 (n/a)</td><td>430.90 (n/a)</td><td>232.80 (n/a)</td><td>161.98 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 <b>(-24.44%)</b></td><td>0.08 <b>(-28.94%)</b></td><td>0.07 <b>(-41.39%)</b></td><td>0.05 (-0.10%)</td><td>0.03 <b>(-34.53%)</b></td><td>721.70 (+0.10%)</td><td>535.06 <b>(+30.34%)</b></td><td>550.60 <b>(+70.62%)</b></td><td>290.80 <b>(+32.36%)</b></td><td>155.26 <b>(-22.09%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>721.00 (n/a)</td><td>410.50 (n/a)</td><td>322.70 (n/a)</td><td>219.70 (n/a)</td><td>199.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.18 <b>(+33.40%)</b></td><td>0.13 <b>(+62.47%)</b></td><td>0.15 <b>(+87.57%)</b></td><td>0.07 <b>(+275.06%)</b></td><td>0.05 <b>(+24.82%)</b></td><td>552.90 <b>(-73.34%)</b></td><td>368.68 <b>(-52.66%)</b></td><td>265.40 <b>(-46.70%)</b></td><td>230.00 <b>(-25.06%)</b></td><td>164.84 <b>(-77.39%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2073.80 (n/a)</td><td>778.76 (n/a)</td><td>497.90 (n/a)</td><td>306.90 (n/a)</td><td>729.09 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.16 <b>(-24.40%)</b></td><td>0.12 (-6.28%)</td><td>0.14 (+16.08%)</td><td>0.07 (-6.83%)</td><td>0.04 <b>(-36.43%)</b></td><td>605.90 (+7.31%)</td><td>379.54 (-0.45%)</td><td>302.00 (-13.86%)</td><td>259.20 <b>(+32.31%)</b></td><td>142.79 (-13.28%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>564.60 (n/a)</td><td>381.24 (n/a)</td><td>350.60 (n/a)</td><td>195.90 (n/a)</td><td>164.66 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.19 (+12.29%)</td><td>0.14 (+15.04%)</td><td>0.13 (-0.01%)</td><td>0.09 <b>(+35.42%)</b></td><td>0.04 (-14.57%)</td><td>434.30 <b>(-26.16%)</b></td><td>302.24 (-17.66%)</td><td>305.10 (+0.00%)</td><td>218.60 (-10.96%)</td><td>83.15 <b>(-42.59%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>588.20 (n/a)</td><td>367.06 (n/a)</td><td>305.10 (n/a)</td><td>245.50 (n/a)</td><td>144.83 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.17 <b>(+40.51%)</b></td><td>0.12 <b>(+26.99%)</b></td><td>0.14 <b>(+74.37%)</b></td><td>0.04 <b>(-43.39%)</b></td><td>0.06 <b>(+126.41%)</b></td><td>1063.40 <b>(+76.64%)</b></td><td>471.80 (+0.96%)</td><td>288.00 <b>(-42.65%)</b></td><td>235.30 <b>(-28.83%)</b></td><td>346.75 <b>(+195.93%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>602.00 (n/a)</td><td>467.30 (n/a)</td><td>502.20 (n/a)</td><td>330.60 (n/a)</td><td>117.17 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.16 <b>(+25.42%)</b></td><td>0.10 (+5.94%)</td><td>0.08 (-12.00%)</td><td>0.06 <b>(-20.12%)</b></td><td>0.04 <b>(+87.59%)</b></td><td>741.10 <b>(+25.19%)</b></td><td>454.84 (+4.21%)</td><td>483.20 (+13.64%)</td><td>250.40 <b>(-20.28%)</b></td><td>192.58 <b>(+81.63%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>592.00 (n/a)</td><td>436.48 (n/a)</td><td>425.20 (n/a)</td><td>314.10 (n/a)</td><td>106.03 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.18 (+10.72%)</td><td>0.10 (-1.53%)</td><td>0.09 (+16.01%)</td><td>0.02 <b>(-67.04%)</b></td><td>0.06 <b>(+39.53%)</b></td><td>1954.20 <b>(+203.45%)</b></td><td>700.22 <b>(+49.91%)</b></td><td>467.30 (-13.80%)</td><td>225.60 (-9.69%)</td><td>709.02 <b>(+338.28%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>644.00 (n/a)</td><td>467.08 (n/a)</td><td>542.10 (n/a)</td><td>249.80 (n/a)</td><td>161.77 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (-2.35%)</td><td>0.10 (-15.12%)</td><td>0.11 (-15.89%)</td><td>0.06 <b>(-25.87%)</b></td><td>0.03 <b>(+38.49%)</b></td><td>573.80 <b>(+34.88%)</b></td><td>392.16 <b>(+25.62%)</b></td><td>330.90 (+18.90%)</td><td>257.30 (+2.43%)</td><td>144.15 <b>(+96.15%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>425.40 (n/a)</td><td>312.18 (n/a)</td><td>278.30 (n/a)</td><td>251.20 (n/a)</td><td>73.49 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (+17.71%)</td><td>0.10 <b>(+31.57%)</b></td><td>0.11 <b>(+49.81%)</b></td><td>0.06 <b>(+341.19%)</b></td><td>0.03 <b>(-21.53%)</b></td><td>558.00 <b>(-77.33%)</b></td><td>379.60 <b>(-53.14%)</b></td><td>318.50 <b>(-33.24%)</b></td><td>264.00 (-15.03%)</td><td>131.36 <b>(-85.83%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2461.60 (n/a)</td><td>810.14 (n/a)</td><td>477.10 (n/a)</td><td>310.70 (n/a)</td><td>927.00 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (-13.34%)</td><td>0.10 (-8.44%)</td><td>0.12 (+5.13%)</td><td>0.06 (-8.25%)</td><td>0.03 <b>(-20.03%)</b></td><td>547.40 (+8.98%)</td><td>367.86 (+7.48%)</td><td>302.70 (-4.90%)</td><td>253.80 (+15.42%)</td><td>120.93 (+2.48%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>502.30 (n/a)</td><td>342.26 (n/a)</td><td>318.30 (n/a)</td><td>219.90 (n/a)</td><td>118.01 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (+0.73%)</td><td>0.11 (+6.17%)</td><td>0.13 <b>(+28.75%)</b></td><td>0.08 <b>(+26.61%)</b></td><td>0.03 (-6.26%)</td><td>452.60 <b>(-21.01%)</b></td><td>338.38 (-7.80%)</td><td>276.40 <b>(-22.34%)</b></td><td>253.30 (-0.71%)</td><td>96.95 <b>(-23.77%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>573.00 (n/a)</td><td>367.00 (n/a)</td><td>355.90 (n/a)</td><td>255.10 (n/a)</td><td>127.17 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 <b>(-43.64%)</b></td><td>0.07 <b>(-26.83%)</b></td><td>0.08 (-11.46%)</td><td>0.03 <b>(-40.16%)</b></td><td>0.02 <b>(-41.58%)</b></td><td>999.10 <b>(+67.10%)</b></td><td>558.00 <b>(+38.32%)</b></td><td>458.90 (+12.95%)</td><td>414.50 <b>(+77.44%)</b></td><td>248.09 <b>(+85.55%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>597.90 (n/a)</td><td>403.42 (n/a)</td><td>406.30 (n/a)</td><td>233.60 (n/a)</td><td>133.71 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.15 (+14.72%)</td><td>0.09 (-3.79%)</td><td>0.07 <b>(-38.89%)</b></td><td>0.06 <b>(+193.22%)</b></td><td>0.04 <b>(-21.70%)</b></td><td>613.50 <b>(-65.90%)</b></td><td>448.32 <b>(-29.87%)</b></td><td>490.10 <b>(+63.64%)</b></td><td>232.40 (-12.83%)</td><td>141.05 <b>(-78.55%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1798.90 (n/a)</td><td>639.24 (n/a)</td><td>299.50 (n/a)</td><td>266.60 (n/a)</td><td>657.56 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.52 <b>(+21.22%)</b></td><td>0.36 (+12.56%)</td><td>0.38 (-10.90%)</td><td>0.21 <b>(+205.99%)</b></td><td>0.11 <b>(-28.13%)</b></td><td>620.20 <b>(-67.32%)</b></td><td>402.40 <b>(-40.23%)</b></td><td>348.40 (+12.24%)</td><td>254.20 (-17.52%)</td><td>140.79 <b>(-79.65%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.43 (n/a)</td><td>0.32 (n/a)</td><td>0.42 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>1897.70 (n/a)</td><td>673.22 (n/a)</td><td>310.40 (n/a)</td><td>308.20 (n/a)</td><td>691.84 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.56 <b>(+37.93%)</b></td><td>0.36 <b>(+22.67%)</b></td><td>0.37 <b>(+35.32%)</b></td><td>0.22 (-3.33%)</td><td>0.13 <b>(+97.50%)</b></td><td>593.60 (+3.43%)</td><td>411.02 (-12.40%)</td><td>357.10 <b>(-26.10%)</b></td><td>233.60 <b>(-27.50%)</b></td><td>145.50 <b>(+59.75%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.41 (n/a)</td><td>0.29 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>573.90 (n/a)</td><td>469.22 (n/a)</td><td>483.20 (n/a)</td><td>322.20 (n/a)</td><td>91.08 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.25 <b>(-40.11%)</b></td><td>0.20 <b>(-36.46%)</b></td><td>0.23 (-15.71%)</td><td>0.05 <b>(-77.93%)</b></td><td>0.08 (+0.23%)</td><td>2435.90 <b>(+353.02%)</b></td><td>933.72 <b>(+112.04%)</b></td><td>579.90 (+18.64%)</td><td>522.90 <b>(+66.95%)</b></td><td>840.09 <b>(+699.80%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.08 (n/a)</td><td>537.70 (n/a)</td><td>440.36 (n/a)</td><td>488.80 (n/a)</td><td>313.20 (n/a)</td><td>105.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (-2.41%)</td><td>0.01 (+9.15%)</td><td>0.01 <b>(+26.57%)</b></td><td>0.01 (-1.77%)</td><td>0.00 (+4.97%)</td><td>511.40 (+1.81%)</td><td>364.80 (-7.79%)</td><td>309.10 <b>(-20.99%)</b></td><td>275.90 (+2.49%)</td><td>105.49 (+5.66%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>502.30 (n/a)</td><td>395.62 (n/a)</td><td>391.20 (n/a)</td><td>269.20 (n/a)</td><td>99.84 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (+16.50%)</td><td>0.01 (-3.91%)</td><td>0.01 (+11.04%)</td><td>0.01 <b>(-27.81%)</b></td><td>0.00 (+14.07%)</td><td>745.40 <b>(+38.52%)</b></td><td>446.38 (+8.42%)</td><td>426.10 (-9.95%)</td><td>224.60 (-14.14%)</td><td>187.94 <b>(+37.80%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>538.10 (n/a)</td><td>411.70 (n/a)</td><td>473.20 (n/a)</td><td>261.60 (n/a)</td><td>136.39 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (+17.07%)</td><td>0.01 (+3.35%)</td><td>0.01 (+7.62%)</td><td>0.01 <b>(+22.15%)</b></td><td>0.00 <b>(+25.52%)</b></td><td>496.80 (-18.14%)</td><td>349.44 (-2.48%)</td><td>282.10 (-7.08%)</td><td>240.80 (-14.58%)</td><td>122.34 (-12.39%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>606.90 (n/a)</td><td>358.32 (n/a)</td><td>303.60 (n/a)</td><td>281.90 (n/a)</td><td>139.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>7.85 <b>(-20.75%)</b></td><td>6.26 <b>(-21.65%)</b></td><td>7.06 (-5.77%)</td><td>3.13 <b>(-50.79%)</b></td><td>1.89 (+19.70%)</td><td>670.50 <b>(+103.18%)</b></td><td>375.06 <b>(+38.52%)</b></td><td>297.40 (+6.14%)</td><td>267.10 <b>(+26.17%)</b></td><td>168.30 <b>(+225.35%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>9.91 (n/a)</td><td>7.99 (n/a)</td><td>7.49 (n/a)</td><td>6.36 (n/a)</td><td>1.58 (n/a)</td><td>330.00 (n/a)</td><td>270.76 (n/a)</td><td>280.20 (n/a)</td><td>211.70 (n/a)</td><td>51.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.46 (-16.81%)</td><td>0.29 <b>(-20.98%)</b></td><td>0.32 (+8.18%)</td><td>0.07 <b>(-71.88%)</b></td><td>0.14 (+7.15%)</td><td>1803.50 <b>(+255.58%)</b></td><td>682.88 <b>(+71.59%)</b></td><td>418.30 (-7.56%)</td><td>287.90 <b>(+20.21%)</b></td><td>630.74 <b>(+414.78%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.55 (n/a)</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>507.20 (n/a)</td><td>397.98 (n/a)</td><td>452.50 (n/a)</td><td>239.50 (n/a)</td><td>122.53 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.49 (-12.50%)</td><td>0.32 (-19.87%)</td><td>0.32 <b>(-21.89%)</b></td><td>0.07 <b>(-68.55%)</b></td><td>0.16 (+8.10%)</td><td>1840.50 <b>(+217.93%)</b></td><td>654.64 <b>(+75.53%)</b></td><td>412.20 <b>(+28.01%)</b></td><td>267.70 (+14.30%)</td><td>666.17 <b>(+347.90%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.56 (n/a)</td><td>0.40 (n/a)</td><td>0.41 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>578.90 (n/a)</td><td>372.96 (n/a)</td><td>322.00 (n/a)</td><td>234.20 (n/a)</td><td>148.73 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.59 <b>(+23.98%)</b></td><td>0.44 <b>(+34.46%)</b></td><td>0.50 <b>(+41.03%)</b></td><td>0.24 (+17.19%)</td><td>0.15 <b>(+34.52%)</b></td><td>557.10 (-14.66%)</td><td>340.74 <b>(-24.33%)</b></td><td>266.80 <b>(-29.10%)</b></td><td>225.10 (-19.35%)</td><td>142.11 (-12.54%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.47 (n/a)</td><td>0.33 (n/a)</td><td>0.35 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>652.80 (n/a)</td><td>450.32 (n/a)</td><td>376.30 (n/a)</td><td>279.10 (n/a)</td><td>162.48 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.59 <b>(+22.37%)</b></td><td>0.41 (+14.69%)</td><td>0.32 (+8.27%)</td><td>0.25 (-3.70%)</td><td>0.16 <b>(+47.66%)</b></td><td>526.60 (+3.82%)</td><td>364.46 (-8.56%)</td><td>408.00 (-7.65%)</td><td>222.70 (-18.28%)</td><td>130.74 (+19.85%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>507.20 (n/a)</td><td>398.58 (n/a)</td><td>441.80 (n/a)</td><td>272.50 (n/a)</td><td>109.09 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.56 (-3.43%)</td><td>0.44 (-12.15%)</td><td>0.49 (-0.23%)</td><td>0.21 <b>(-54.17%)</b></td><td>0.14 <b>(+169.66%)</b></td><td>635.80 <b>(+118.19%)</b></td><td>342.70 <b>(+28.52%)</b></td><td>271.60 (+0.22%)</td><td>235.30 (+3.57%)</td><td>166.76 <b>(+540.33%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.58 (n/a)</td><td>0.50 (n/a)</td><td>0.49 (n/a)</td><td>0.45 (n/a)</td><td>0.05 (n/a)</td><td>291.40 (n/a)</td><td>266.66 (n/a)</td><td>271.00 (n/a)</td><td>227.20 (n/a)</td><td>26.04 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (+10.41%)</td><td>0.01 (-14.78%)</td><td>0.01 <b>(-36.96%)</b></td><td>0.00 <b>(-29.78%)</b></td><td>0.01 <b>(+32.35%)</b></td><td>824.60 <b>(+42.42%)</b></td><td>453.30 <b>(+30.09%)</b></td><td>424.20 <b>(+58.64%)</b></td><td>232.50 (-9.43%)</td><td>236.86 <b>(+70.77%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.00 (n/a)</td><td>348.44 (n/a)</td><td>267.40 (n/a)</td><td>256.70 (n/a)</td><td>138.70 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 <b>(-33.17%)</b></td><td>0.01 <b>(-22.24%)</b></td><td>0.01 (-19.11%)</td><td>0.01 (-2.40%)</td><td>0.00 <b>(-51.94%)</b></td><td>502.30 (+2.47%)</td><td>408.64 <b>(+22.52%)</b></td><td>381.60 <b>(+23.62%)</b></td><td>325.10 <b>(+49.61%)</b></td><td>79.14 <b>(-25.38%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>490.20 (n/a)</td><td>333.54 (n/a)</td><td>308.70 (n/a)</td><td>217.30 (n/a)</td><td>106.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.00 <b>(-57.14%)</b></td><td>0.00 <b>(-26.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-80.00%)</b></td><td>22241.06 (+0.12%)</td><td>19313.73 (+8.58%)</td><td>20695.25 (-2.39%)</td><td>15998.37 <b>(+160.49%)</b></td><td>2756.56 <b>(-59.08%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22214.58 (n/a)</td><td>17787.09 (n/a)</td><td>21201.47 (n/a)</td><td>6141.64 (n/a)</td><td>6736.69 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.00 (+11.11%)</td><td>0.00 (-13.33%)</td><td>0.00 <b>(-20.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+14.42%)</td><td>22456.26 (+13.97%)</td><td>18434.50 <b>(+23.19%)</b></td><td>19898.22 (+10.78%)</td><td>8305.52 (-6.34%)</td><td>5793.30 (+10.98%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19703.68 (n/a)</td><td>14963.95 (n/a)</td><td>17961.50 (n/a)</td><td>8867.63 (n/a)</td><td>5219.93 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 <b>(+56.40%)</b></td><td>0.09 (+15.79%)</td><td>0.08 (+10.13%)</td><td>0.07 (-5.41%)</td><td>0.02 <b>(+531.78%)</b></td><td>31566.21 (+5.59%)</td><td>25259.88 (-9.55%)</td><td>25390.65 (-9.14%)</td><td>16662.95 <b>(-36.03%)</b></td><td>5678.38 <b>(+312.82%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>29894.75 (n/a)</td><td>27927.24 (n/a)</td><td>27945.62 (n/a)</td><td>26048.41 (n/a)</td><td>1375.52 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.16 (+17.87%)</td><td>0.12 <b>(+26.91%)</b></td><td>0.12 <b>(+46.55%)</b></td><td>0.07 (-7.69%)</td><td>0.04 <b>(+50.83%)</b></td><td>30644.45 (+8.23%)</td><td>19707.87 (-17.43%)</td><td>17031.77 <b>(-31.80%)</b></td><td>13354.90 (-15.17%)</td><td>7019.95 <b>(+47.25%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>28313.49 (n/a)</td><td>23868.00 (n/a)</td><td>24973.54 (n/a)</td><td>15743.83 (n/a)</td><td>4767.50 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.33 (-9.91%)</td><td>1.59 (-19.63%)</td><td>1.48 <b>(-33.27%)</b></td><td>0.53 <b>(-51.17%)</b></td><td>0.72 (+18.56%)</td><td>1966.90 <b>(+104.78%)</b></td><td>869.58 <b>(+48.59%)</b></td><td>708.50 <b>(+49.88%)</b></td><td>450.10 (+11.00%)</td><td>627.39 <b>(+174.86%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>2.59 (n/a)</td><td>1.98 (n/a)</td><td>2.22 (n/a)</td><td>1.09 (n/a)</td><td>0.61 (n/a)</td><td>960.50 (n/a)</td><td>585.22 (n/a)</td><td>472.70 (n/a)</td><td>405.50 (n/a)</td><td>228.26 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.13 (-5.21%)</td><td>1.91 (-16.72%)</td><td>1.63 <b>(-32.63%)</b></td><td>0.55 <b>(-62.79%)</b></td><td>1.03 <b>(+45.44%)</b></td><td>1913.20 <b>(+168.78%)</b></td><td>791.58 <b>(+60.52%)</b></td><td>644.20 <b>(+48.43%)</b></td><td>335.30 (+5.47%)</td><td>645.38 <b>(+316.33%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.30 (n/a)</td><td>2.30 (n/a)</td><td>2.42 (n/a)</td><td>1.47 (n/a)</td><td>0.71 (n/a)</td><td>711.80 (n/a)</td><td>493.14 (n/a)</td><td>434.00 (n/a)</td><td>317.90 (n/a)</td><td>155.02 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.14 (-14.37%)</td><td>1.60 (-15.07%)</td><td>1.57 (-10.79%)</td><td>0.98 <b>(-30.01%)</b></td><td>0.42 (+0.36%)</td><td>1069.60 <b>(+42.88%)</b></td><td>701.72 <b>(+21.04%)</b></td><td>668.50 (+12.11%)</td><td>490.60 (+16.78%)</td><td>219.50 <b>(+76.94%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>2.50 (n/a)</td><td>1.88 (n/a)</td><td>1.76 (n/a)</td><td>1.40 (n/a)</td><td>0.42 (n/a)</td><td>748.60 (n/a)</td><td>579.74 (n/a)</td><td>596.30 (n/a)</td><td>420.10 (n/a)</td><td>124.05 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.63 (+8.65%)</td><td>1.99 (-13.32%)</td><td>1.82 <b>(-29.20%)</b></td><td>1.02 (-16.16%)</td><td>1.00 (+14.01%)</td><td>1024.20 (+19.27%)</td><td>628.92 (+19.76%)</td><td>576.90 <b>(+41.26%)</b></td><td>288.90 (-7.96%)</td><td>276.89 <b>(+20.15%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.34 (n/a)</td><td>2.30 (n/a)</td><td>2.57 (n/a)</td><td>1.22 (n/a)</td><td>0.88 (n/a)</td><td>858.70 (n/a)</td><td>525.14 (n/a)</td><td>408.40 (n/a)</td><td>313.90 (n/a)</td><td>230.45 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.14 <b>(-24.58%)</b></td><td>1.56 <b>(-53.33%)</b></td><td>0.98 <b>(-70.74%)</b></td><td>0.62 <b>(-74.85%)</b></td><td>1.09 <b>(+74.01%)</b></td><td>3377.10 <b>(+297.59%)</b></td><td>1928.74 <b>(+199.28%)</b></td><td>2150.20 <b>(+241.79%)</b></td><td>667.80 <b>(+32.58%)</b></td><td>1127.18 <b>(+769.46%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>4.16 (n/a)</td><td>3.35 (n/a)</td><td>3.33 (n/a)</td><td>2.47 (n/a)</td><td>0.63 (n/a)</td><td>849.40 (n/a)</td><td>644.46 (n/a)</td><td>629.10 (n/a)</td><td>503.70 (n/a)</td><td>129.64 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.06 (-18.76%)</td><td>2.43 (-12.83%)</td><td>2.66 (-5.81%)</td><td>1.12 <b>(-43.82%)</b></td><td>0.77 (+12.99%)</td><td>1879.70 <b>(+77.99%)</b></td><td>988.50 <b>(+25.26%)</b></td><td>787.90 (+6.16%)</td><td>685.80 <b>(+23.10%)</b></td><td>502.52 <b>(+160.66%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.76 (n/a)</td><td>2.79 (n/a)</td><td>2.83 (n/a)</td><td>1.99 (n/a)</td><td>0.68 (n/a)</td><td>1056.10 (n/a)</td><td>789.18 (n/a)</td><td>742.20 (n/a)</td><td>557.10 (n/a)</td><td>192.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>4.78 (-10.71%)</td><td>2.88 <b>(-22.23%)</b></td><td>4.21 (+14.05%)</td><td>0.60 <b>(-65.63%)</b></td><td>2.09 <b>(+36.32%)</b></td><td>3518.40 <b>(+190.92%)</b></td><td>1675.12 <b>(+149.18%)</b></td><td>498.30 (-12.32%)</td><td>439.00 (+11.99%)</td><td>1639.39 <b>(+386.11%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.35 (n/a)</td><td>3.71 (n/a)</td><td>3.69 (n/a)</td><td>1.73 (n/a)</td><td>1.53 (n/a)</td><td>1209.40 (n/a)</td><td>672.26 (n/a)</td><td>568.30 (n/a)</td><td>392.00 (n/a)</td><td>337.25 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>6.22 (+10.56%)</td><td>3.63 (+17.56%)</td><td>3.51 (+10.41%)</td><td>0.65 (+11.37%)</td><td>2.29 <b>(+24.39%)</b></td><td>3248.80 (-10.21%)</td><td>1097.00 (-10.05%)</td><td>596.60 (-9.43%)</td><td>337.00 (-9.55%)</td><td>1224.99 (-9.46%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.63 (n/a)</td><td>3.09 (n/a)</td><td>3.18 (n/a)</td><td>0.58 (n/a)</td><td>1.84 (n/a)</td><td>3618.10 (n/a)</td><td>1219.56 (n/a)</td><td>658.70 (n/a)</td><td>372.60 (n/a)</td><td>1353.06 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.98 (-6.72%)</td><td>2.53 (-1.67%)</td><td>2.74 (-15.50%)</td><td>0.65 (+11.70%)</td><td>1.48 (-19.78%)</td><td>3211.20 (-10.47%)</td><td>1311.24 <b>(-24.75%)</b></td><td>766.00 (+18.34%)</td><td>527.00 (+7.22%)</td><td>1135.33 <b>(-30.67%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>4.27 (n/a)</td><td>2.57 (n/a)</td><td>3.24 (n/a)</td><td>0.58 (n/a)</td><td>1.85 (n/a)</td><td>3586.70 (n/a)</td><td>1742.52 (n/a)</td><td>647.30 (n/a)</td><td>491.50 (n/a)</td><td>1637.63 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.92 <b>(-39.28%)</b></td><td>2.31 <b>(-23.79%)</b></td><td>2.72 (-13.42%)</td><td>1.00 (+17.89%)</td><td>0.80 <b>(-45.79%)</b></td><td>2101.40 (-15.18%)</td><td>1066.60 (+7.77%)</td><td>770.90 (+15.51%)</td><td>718.10 <b>(+64.70%)</b></td><td>589.27 <b>(-30.14%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>4.81 (n/a)</td><td>3.03 (n/a)</td><td>3.14 (n/a)</td><td>0.85 (n/a)</td><td>1.48 (n/a)</td><td>2477.40 (n/a)</td><td>989.66 (n/a)</td><td>667.40 (n/a)</td><td>436.00 (n/a)</td><td>843.44 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.76 <b>(-31.91%)</b></td><td>2.33 <b>(-40.78%)</b></td><td>2.08 <b>(-52.32%)</b></td><td>1.22 (+11.75%)</td><td>1.01 <b>(-39.41%)</b></td><td>3449.70 (-10.51%)</td><td>2104.80 <b>(+40.13%)</b></td><td>2015.60 <b>(+109.74%)</b></td><td>1114.80 <b>(+46.86%)</b></td><td>920.77 <b>(-30.17%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.53 (n/a)</td><td>3.93 (n/a)</td><td>4.36 (n/a)</td><td>1.09 (n/a)</td><td>1.67 (n/a)</td><td>3855.00 (n/a)</td><td>1502.00 (n/a)</td><td>961.00 (n/a)</td><td>759.10 (n/a)</td><td>1318.65 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>7.11 (-10.16%)</td><td>3.91 <b>(-41.08%)</b></td><td>3.96 <b>(-36.02%)</b></td><td>1.19 <b>(-79.92%)</b></td><td>2.69 <b>(+222.47%)</b></td><td>3538.80 <b>(+398.00%)</b></td><td>1830.94 <b>(+186.33%)</b></td><td>1058.70 <b>(+56.31%)</b></td><td>589.60 (+11.31%)</td><td>1449.77 <b>(+1838.33%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>7.92 (n/a)</td><td>6.64 (n/a)</td><td>6.19 (n/a)</td><td>5.90 (n/a)</td><td>0.83 (n/a)</td><td>710.60 (n/a)</td><td>639.44 (n/a)</td><td>677.30 (n/a)</td><td>529.70 (n/a)</td><td>74.79 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>6.20 (+10.74%)</td><td>4.07 <b>(+42.93%)</b></td><td>4.53 <b>(+120.53%)</b></td><td>1.10 (-8.53%)</td><td>1.93 (-1.55%)</td><td>3825.90 (+9.33%)</td><td>1492.92 <b>(-30.64%)</b></td><td>926.00 <b>(-54.65%)</b></td><td>676.70 (-9.69%)</td><td>1318.37 (+0.74%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>5.60 (n/a)</td><td>2.85 (n/a)</td><td>2.05 (n/a)</td><td>1.20 (n/a)</td><td>1.96 (n/a)</td><td>3499.40 (n/a)</td><td>2152.50 (n/a)</td><td>2042.10 (n/a)</td><td>749.30 (n/a)</td><td>1308.67 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>8.59 (-14.39%)</td><td>6.84 (-1.80%)</td><td>6.90 (-2.12%)</td><td>4.23 (+2.09%)</td><td>1.83 <b>(-32.73%)</b></td><td>991.70 (-2.04%)</td><td>656.78 (-4.75%)</td><td>607.80 (+2.17%)</td><td>488.40 (+16.81%)</td><td>207.32 <b>(-26.90%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>10.03 (n/a)</td><td>6.96 (n/a)</td><td>7.05 (n/a)</td><td>4.14 (n/a)</td><td>2.72 (n/a)</td><td>1012.40 (n/a)</td><td>689.50 (n/a)</td><td>594.90 (n/a)</td><td>418.10 (n/a)</td><td>283.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>8.70 <b>(+26.77%)</b></td><td>7.08 <b>(+22.07%)</b></td><td>7.79 (+15.93%)</td><td>3.99 (+10.26%)</td><td>1.84 <b>(+27.14%)</b></td><td>1050.50 (-9.31%)</td><td>640.60 (-16.84%)</td><td>538.30 (-13.73%)</td><td>482.10 <b>(-21.11%)</b></td><td>233.39 (-1.63%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>6.86 (n/a)</td><td>5.80 (n/a)</td><td>6.72 (n/a)</td><td>3.62 (n/a)</td><td>1.44 (n/a)</td><td>1158.30 (n/a)</td><td>770.30 (n/a)</td><td>624.00 (n/a)</td><td>611.10 (n/a)</td><td>237.27 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>10.32 (+16.68%)</td><td>5.78 (-12.68%)</td><td>6.42 (-8.37%)</td><td>1.15 <b>(-73.92%)</b></td><td>3.48 <b>(+97.46%)</b></td><td>3659.00 <b>(+283.38%)</b></td><td>1279.72 <b>(+90.00%)</b></td><td>653.00 (+9.12%)</td><td>406.50 (-14.29%)</td><td>1354.33 <b>(+601.35%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>8.84 (n/a)</td><td>6.62 (n/a)</td><td>7.01 (n/a)</td><td>4.39 (n/a)</td><td>1.76 (n/a)</td><td>954.40 (n/a)</td><td>673.54 (n/a)</td><td>598.40 (n/a)</td><td>474.30 (n/a)</td><td>193.10 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.47 (-8.45%)</td><td>0.99 (+0.77%)</td><td>1.26 <b>(+33.30%)</b></td><td>0.15 (-4.39%)</td><td>0.56 (-2.21%)</td><td>3420.30 (+4.59%)</td><td>1065.12 (+2.70%)</td><td>414.90 <b>(-24.97%)</b></td><td>356.20 (+9.23%)</td><td>1326.45 (+5.60%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.61 (n/a)</td><td>0.98 (n/a)</td><td>0.95 (n/a)</td><td>0.16 (n/a)</td><td>0.57 (n/a)</td><td>3270.30 (n/a)</td><td>1037.08 (n/a)</td><td>553.00 (n/a)</td><td>326.10 (n/a)</td><td>1256.06 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.57 <b>(+34.02%)</b></td><td>1.48 <b>(+36.55%)</b></td><td>1.52 (+8.44%)</td><td>0.30 (-0.45%)</td><td>0.81 (+9.31%)</td><td>3533.70 (+0.45%)</td><td>1204.80 <b>(-32.08%)</b></td><td>690.10 (-7.79%)</td><td>408.40 <b>(-25.38%)</b></td><td>1308.00 (-13.97%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.92 (n/a)</td><td>1.08 (n/a)</td><td>1.40 (n/a)</td><td>0.30 (n/a)</td><td>0.74 (n/a)</td><td>3517.90 (n/a)</td><td>1773.86 (n/a)</td><td>748.40 (n/a)</td><td>547.30 (n/a)</td><td>1520.42 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.32 <b>(-40.90%)</b></td><td>1.34 <b>(-53.40%)</b></td><td>1.14 <b>(-56.13%)</b></td><td>0.58 <b>(-66.63%)</b></td><td>0.77 <b>(-21.50%)</b></td><td>3597.00 <b>(+199.68%)</b></td><td>2083.88 <b>(+158.81%)</b></td><td>1843.00 <b>(+127.92%)</b></td><td>904.80 <b>(+69.22%)</b></td><td>1182.52 <b>(+321.18%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>3.92 (n/a)</td><td>2.87 (n/a)</td><td>2.59 (n/a)</td><td>1.75 (n/a)</td><td>0.98 (n/a)</td><td>1200.30 (n/a)</td><td>805.18 (n/a)</td><td>808.60 (n/a)</td><td>534.70 (n/a)</td><td>280.76 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.53 (-12.26%)</td><td>1.09 (-18.35%)</td><td>1.02 (-19.38%)</td><td>0.95 (-3.58%)</td><td>0.25 (-13.87%)</td><td>551.30 (+3.73%)</td><td>494.58 <b>(+21.94%)</b></td><td>516.30 <b>(+24.05%)</b></td><td>341.90 (+14.00%)</td><td>87.01 (+0.14%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>1.75 (n/a)</td><td>1.34 (n/a)</td><td>1.26 (n/a)</td><td>0.99 (n/a)</td><td>0.29 (n/a)</td><td>531.50 (n/a)</td><td>405.58 (n/a)</td><td>416.20 (n/a)</td><td>299.90 (n/a)</td><td>86.89 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 <b>(-37.44%)</b></td><td>0.09 (-13.72%)</td><td>0.08 <b>(+31.66%)</b></td><td>0.07 <b>(+37.06%)</b></td><td>0.03 <b>(-63.40%)</b></td><td>481.40 <b>(-27.04%)</b></td><td>396.04 (-10.23%)</td><td>420.20 <b>(-24.04%)</b></td><td>254.80 <b>(+59.85%)</b></td><td>93.92 <b>(-58.41%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>659.80 (n/a)</td><td>441.16 (n/a)</td><td>553.20 (n/a)</td><td>159.40 (n/a)</td><td>225.85 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.12 <b>(-27.97%)</b></td><td>0.09 (-2.24%)</td><td>0.09 (+13.54%)</td><td>0.06 (+4.92%)</td><td>0.03 <b>(-34.24%)</b></td><td>583.90 (-4.68%)</td><td>400.80 (-3.91%)</td><td>382.40 (-11.93%)</td><td>265.20 <b>(+38.85%)</b></td><td>140.54 (-13.11%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>612.60 (n/a)</td><td>417.12 (n/a)</td><td>434.20 (n/a)</td><td>191.00 (n/a)</td><td>161.75 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.25 (-16.97%)</td><td>0.20 (+7.80%)</td><td>0.21 <b>(+39.30%)</b></td><td>0.12 (-9.80%)</td><td>0.05 <b>(-30.66%)</b></td><td>564.40 (+10.86%)</td><td>349.74 (-10.17%)</td><td>308.40 <b>(-28.21%)</b></td><td>260.50 <b>(+20.43%)</b></td><td>122.14 (-2.53%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.30 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>509.10 (n/a)</td><td>389.32 (n/a)</td><td>429.60 (n/a)</td><td>216.30 (n/a)</td><td>125.31 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.24 <b>(-41.19%)</b></td><td>0.19 (-18.07%)</td><td>0.19 (-17.95%)</td><td>0.14 (+0.34%)</td><td>0.04 <b>(-60.48%)</b></td><td>467.50 (-0.34%)</td><td>353.92 (+9.47%)</td><td>338.40 <b>(+21.86%)</b></td><td>268.60 <b>(+70.00%)</b></td><td>83.06 <b>(-35.41%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.41 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>469.10 (n/a)</td><td>323.30 (n/a)</td><td>277.70 (n/a)</td><td>158.00 (n/a)</td><td>128.59 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.25 (-9.85%)</td><td>0.16 (-8.52%)</td><td>0.15 (+11.82%)</td><td>0.12 (+6.00%)</td><td>0.05 <b>(-31.13%)</b></td><td>544.00 (-5.67%)</td><td>434.90 (+1.67%)</td><td>435.90 (-10.57%)</td><td>259.50 (+10.90%)</td><td>108.87 <b>(-32.41%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>576.70 (n/a)</td><td>427.74 (n/a)</td><td>487.40 (n/a)</td><td>234.00 (n/a)</td><td>161.07 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.54 (+14.56%)</td><td>0.34 (+16.93%)</td><td>0.32 <b>(+23.48%)</b></td><td>0.20 (+2.78%)</td><td>0.13 <b>(+26.74%)</b></td><td>642.10 (-2.70%)</td><td>439.18 (-11.32%)</td><td>411.20 (-19.02%)</td><td>244.10 (-12.70%)</td><td>161.42 (+16.75%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.47 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>659.90 (n/a)</td><td>495.22 (n/a)</td><td>507.80 (n/a)</td><td>279.60 (n/a)</td><td>138.26 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.49 (-4.43%)</td><td>0.34 (-12.63%)</td><td>0.38 (-12.70%)</td><td>0.20 (-15.06%)</td><td>0.13 <b>(+20.37%)</b></td><td>658.90 (+17.72%)</td><td>441.62 <b>(+21.36%)</b></td><td>349.20 (+14.57%)</td><td>268.50 (+4.64%)</td><td>182.89 <b>(+52.09%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.43 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>559.70 (n/a)</td><td>363.90 (n/a)</td><td>304.80 (n/a)</td><td>256.60 (n/a)</td><td>120.25 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.44 <b>(+26.92%)</b></td><td>0.30 (+8.92%)</td><td>0.28 (-3.30%)</td><td>0.24 (+12.84%)</td><td>0.08 <b>(+49.93%)</b></td><td>536.40 (-11.38%)</td><td>450.26 (-6.97%)</td><td>464.40 (+3.41%)</td><td>298.00 <b>(-21.23%)</b></td><td>90.56 (-1.77%)</td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.05 (n/a)</td><td>605.30 (n/a)</td><td>484.02 (n/a)</td><td>449.10 (n/a)</td><td>378.30 (n/a)</td><td>92.19 (n/a)</td>
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
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (+10.19%)</td><td>0.03 (-4.91%)</td><td>0.03 (-7.98%)</td><td>0.01 <b>(-47.89%)</b></td><td>0.01 <b>(+63.49%)</b></td><td>1100.30 <b>(+91.92%)</b></td><td>609.30 <b>(+20.59%)</b></td><td>598.00 (+8.69%)</td><td>296.30 (-9.25%)</td><td>301.67 <b>(+197.23%)</b></td>
</tr>
<tr>
<td><code>7b8fba7</code> — 2026-09-19 00:08:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>573.30 (n/a)</td><td>505.26 (n/a)</td><td>550.20 (n/a)</td><td>326.50 (n/a)</td><td>101.49 (n/a)</td>
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
