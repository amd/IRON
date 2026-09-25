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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (-10.86%)</td><td>0.02 (+2.68%)</td><td>0.02 (+3.22%)</td><td>0.01 (+12.75%)</td><td>0.00 <b>(-26.31%)</b></td><td>460.30 (-11.29%)</td><td>343.34 (-6.87%)</td><td>306.00 (-3.13%)</td><td>264.00 (+12.20%)</td><td>88.43 <b>(-30.73%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>518.90 (n/a)</td><td>368.68 (n/a)</td><td>315.90 (n/a)</td><td>235.30 (n/a)</td><td>127.66 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (+4.27%)</td><td>0.02 (+13.67%)</td><td>0.02 (+19.03%)</td><td>0.02 (+7.76%)</td><td>0.00 (+0.18%)</td><td>383.70 (-7.21%)</td><td>276.48 (-12.31%)</td><td>251.60 (-15.99%)</td><td>236.00 (-4.07%)</td><td>61.87 (-9.62%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>413.50 (n/a)</td><td>315.28 (n/a)</td><td>299.50 (n/a)</td><td>246.00 (n/a)</td><td>68.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 <b>(+25.25%)</b></td><td>0.02 <b>(+42.27%)</b></td><td>0.01 (+17.59%)</td><td>0.01 <b>(+97.82%)</b></td><td>0.01 <b>(+42.08%)</b></td><td>633.70 <b>(-49.45%)</b></td><td>432.48 <b>(-31.96%)</b></td><td>471.70 (-14.95%)</td><td>228.70 <b>(-20.15%)</b></td><td>192.44 <b>(-47.49%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1253.50 (n/a)</td><td>635.58 (n/a)</td><td>554.60 (n/a)</td><td>286.40 (n/a)</td><td>366.51 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (-1.52%)</td><td>0.02 (-2.26%)</td><td>0.01 (-6.21%)</td><td>0.01 <b>(+26.14%)</b></td><td>0.00 <b>(-26.16%)</b></td><td>494.20 <b>(-20.73%)</b></td><td>420.24 (-5.32%)</td><td>471.60 (+6.62%)</td><td>255.10 (+1.51%)</td><td>100.47 <b>(-42.69%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.40 (n/a)</td><td>443.84 (n/a)</td><td>442.30 (n/a)</td><td>251.30 (n/a)</td><td>175.32 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (+17.70%)</td><td>0.02 <b>(+34.42%)</b></td><td>0.02 <b>(+63.08%)</b></td><td>0.01 <b>(+29.21%)</b></td><td>0.01 <b>(+21.31%)</b></td><td>521.60 <b>(-22.60%)</b></td><td>353.98 <b>(-25.44%)</b></td><td>288.60 <b>(-38.67%)</b></td><td>245.10 (-15.04%)</td><td>117.57 (-17.36%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>673.90 (n/a)</td><td>474.74 (n/a)</td><td>470.60 (n/a)</td><td>288.50 (n/a)</td><td>142.27 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-2.72%)</td><td>0.02 (+11.47%)</td><td>0.01 (+2.84%)</td><td>0.01 <b>(+180.18%)</b></td><td>0.01 (-16.32%)</td><td>671.70 <b>(-64.31%)</b></td><td>430.12 <b>(-36.30%)</b></td><td>428.90 (-2.77%)</td><td>245.70 (+2.80%)</td><td>176.22 <b>(-74.10%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1881.90 (n/a)</td><td>675.28 (n/a)</td><td>441.10 (n/a)</td><td>239.00 (n/a)</td><td>680.41 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (-5.56%)</td><td>0.03 (-10.47%)</td><td>0.04 (-2.88%)</td><td>0.02 (-10.36%)</td><td>0.01 (+2.61%)</td><td>635.40 (+11.57%)</td><td>411.02 (+13.16%)</td><td>345.60 (+2.98%)</td><td>297.80 (+5.90%)</td><td>139.99 (+18.08%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>569.50 (n/a)</td><td>363.22 (n/a)</td><td>335.60 (n/a)</td><td>281.20 (n/a)</td><td>118.56 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (+11.17%)</td><td>0.04 <b>(+53.76%)</b></td><td>0.05 <b>(+57.42%)</b></td><td>0.04 <b>(+172.84%)</b></td><td>0.00 <b>(-62.99%)</b></td><td>306.20 <b>(-63.35%)</b></td><td>275.86 <b>(-45.05%)</b></td><td>270.60 <b>(-36.48%)</b></td><td>237.70 (-10.06%)</td><td>29.22 <b>(-87.74%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>835.50 (n/a)</td><td>502.04 (n/a)</td><td>426.00 (n/a)</td><td>264.30 (n/a)</td><td>238.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 <b>(+24.51%)</b></td><td>0.03 (+2.10%)</td><td>0.03 (-11.24%)</td><td>0.02 (-10.76%)</td><td>0.02 <b>(+62.54%)</b></td><td>554.30 (+12.05%)</td><td>426.86 (+6.04%)</td><td>461.60 (+12.67%)</td><td>198.20 (-19.69%)</td><td>147.87 <b>(+44.88%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.70 (n/a)</td><td>402.56 (n/a)</td><td>409.70 (n/a)</td><td>246.80 (n/a)</td><td>102.07 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 <b>(+41.11%)</b></td><td>0.03 <b>(+32.19%)</b></td><td>0.03 <b>(+39.53%)</b></td><td>0.02 (+17.21%)</td><td>0.01 <b>(+102.83%)</b></td><td>510.30 (-14.69%)</td><td>399.02 <b>(-21.78%)</b></td><td>387.20 <b>(-28.34%)</b></td><td>292.60 <b>(-29.14%)</b></td><td>104.59 <b>(+25.40%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>598.20 (n/a)</td><td>510.10 (n/a)</td><td>540.30 (n/a)</td><td>412.90 (n/a)</td><td>83.40 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (+6.30%)</td><td>0.04 (-5.12%)</td><td>0.02 <b>(-31.58%)</b></td><td>0.02 (-7.65%)</td><td>0.02 <b>(+36.22%)</b></td><td>581.90 (+8.28%)</td><td>420.54 (+14.50%)</td><td>518.40 <b>(+46.15%)</b></td><td>219.10 (-5.93%)</td><td>176.83 <b>(+38.73%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.40 (n/a)</td><td>367.28 (n/a)</td><td>354.70 (n/a)</td><td>232.90 (n/a)</td><td>127.46 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (+17.75%)</td><td>0.03 <b>(+54.62%)</b></td><td>0.03 <b>(+53.25%)</b></td><td>0.02 <b>(+103.06%)</b></td><td>0.01 (-10.55%)</td><td>511.00 <b>(-50.75%)</b></td><td>376.96 <b>(-41.12%)</b></td><td>402.10 <b>(-34.75%)</b></td><td>258.90 (-15.09%)</td><td>100.55 <b>(-61.73%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1037.60 (n/a)</td><td>640.26 (n/a)</td><td>616.20 (n/a)</td><td>304.90 (n/a)</td><td>262.73 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 <b>(+30.69%)</b></td><td>0.08 (+13.65%)</td><td>0.08 <b>(+20.31%)</b></td><td>0.05 (-7.34%)</td><td>0.02 <b>(+62.12%)</b></td><td>508.50 (+7.92%)</td><td>353.20 (-7.80%)</td><td>316.60 (-16.88%)</td><td>223.50 <b>(-23.49%)</b></td><td>117.68 <b>(+35.58%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>471.20 (n/a)</td><td>383.08 (n/a)</td><td>380.90 (n/a)</td><td>292.10 (n/a)</td><td>86.80 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (-3.49%)</td><td>0.08 (+5.42%)</td><td>0.08 <b>(+48.91%)</b></td><td>0.05 (-0.89%)</td><td>0.02 <b>(-23.37%)</b></td><td>529.50 (+0.88%)</td><td>352.16 (-9.73%)</td><td>305.20 <b>(-32.85%)</b></td><td>226.80 (+3.61%)</td><td>115.57 (-18.80%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>524.90 (n/a)</td><td>390.12 (n/a)</td><td>454.50 (n/a)</td><td>218.90 (n/a)</td><td>142.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 <b>(+37.17%)</b></td><td>0.09 <b>(+46.39%)</b></td><td>0.09 <b>(+78.55%)</b></td><td>0.06 <b>(+23.60%)</b></td><td>0.02 <b>(+28.72%)</b></td><td>401.00 (-19.09%)</td><td>293.02 <b>(-31.71%)</b></td><td>271.70 <b>(-44.00%)</b></td><td>240.40 <b>(-27.09%)</b></td><td>63.54 <b>(-22.54%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>495.60 (n/a)</td><td>429.10 (n/a)</td><td>485.20 (n/a)</td><td>329.70 (n/a)</td><td>82.03 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 <b>(+47.98%)</b></td><td>0.06 <b>(+32.74%)</b></td><td>0.05 (+2.24%)</td><td>0.02 <b>(+75.96%)</b></td><td>0.03 <b>(+56.92%)</b></td><td>1097.90 <b>(-43.17%)</b></td><td>556.44 <b>(-29.45%)</b></td><td>520.50 (-2.18%)</td><td>297.00 <b>(-32.42%)</b></td><td>327.43 <b>(-48.86%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1931.80 (n/a)</td><td>788.72 (n/a)</td><td>532.10 (n/a)</td><td>439.50 (n/a)</td><td>640.25 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 <b>(+51.74%)</b></td><td>0.08 <b>(+65.93%)</b></td><td>0.08 <b>(+74.86%)</b></td><td>0.05 <b>(+139.42%)</b></td><td>0.02 (+9.44%)</td><td>461.90 <b>(-58.23%)</b></td><td>328.48 <b>(-45.30%)</b></td><td>308.60 <b>(-42.81%)</b></td><td>234.20 <b>(-34.08%)</b></td><td>86.19 <b>(-70.89%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1105.90 (n/a)</td><td>600.52 (n/a)</td><td>539.60 (n/a)</td><td>355.30 (n/a)</td><td>296.03 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (-3.17%)</td><td>0.05 (-4.82%)</td><td>0.04 <b>(-21.76%)</b></td><td>0.04 (+8.15%)</td><td>0.02 (+1.59%)</td><td>603.40 (-7.54%)</td><td>486.62 (+5.43%)</td><td>576.60 <b>(+27.79%)</b></td><td>298.70 (+3.28%)</td><td>141.91 (+0.62%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>652.60 (n/a)</td><td>461.56 (n/a)</td><td>451.20 (n/a)</td><td>289.20 (n/a)</td><td>141.04 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.21 (+6.10%)</td><td>0.14 (+19.62%)</td><td>0.14 (+15.24%)</td><td>0.06 <b>(+153.07%)</b></td><td>0.05 (-15.07%)</td><td>772.60 <b>(-60.48%)</b></td><td>418.96 <b>(-40.09%)</b></td><td>340.60 (-13.22%)</td><td>235.30 (-5.77%)</td><td>208.91 <b>(-70.54%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>0.06 (n/a)</td><td>1955.20 (n/a)</td><td>699.30 (n/a)</td><td>392.50 (n/a)</td><td>249.70 (n/a)</td><td>709.07 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.21 (-5.64%)</td><td>0.17 <b>(+51.18%)</b></td><td>0.18 <b>(+64.21%)</b></td><td>0.12 <b>(+405.04%)</b></td><td>0.03 <b>(-51.83%)</b></td><td>414.30 <b>(-80.20%)</b></td><td>296.50 <b>(-59.85%)</b></td><td>276.30 <b>(-39.10%)</b></td><td>237.90 (+5.97%)</td><td>69.87 <b>(-90.87%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.22 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>2092.40 (n/a)</td><td>738.54 (n/a)</td><td>453.70 (n/a)</td><td>224.50 (n/a)</td><td>765.24 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.22 <b>(+26.26%)</b></td><td>0.15 <b>(+22.89%)</b></td><td>0.17 <b>(+60.28%)</b></td><td>0.09 (+4.20%)</td><td>0.05 <b>(+48.71%)</b></td><td>521.80 (-4.03%)</td><td>361.46 (-15.08%)</td><td>294.70 <b>(-37.60%)</b></td><td>222.70 <b>(-20.80%)</b></td><td>129.06 (+19.81%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>543.70 (n/a)</td><td>425.66 (n/a)</td><td>472.30 (n/a)</td><td>281.20 (n/a)</td><td>107.72 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.21 (+4.51%)</td><td>0.14 (-0.93%)</td><td>0.11 <b>(-27.69%)</b></td><td>0.09 (+16.42%)</td><td>0.05 (-12.05%)</td><td>547.10 (-14.10%)</td><td>387.86 (-5.28%)</td><td>440.50 <b>(+38.30%)</b></td><td>234.90 (-4.32%)</td><td>132.92 <b>(-30.95%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>636.90 (n/a)</td><td>409.50 (n/a)</td><td>318.50 (n/a)</td><td>245.50 (n/a)</td><td>192.51 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.16 <b>(+47.23%)</b></td><td>0.11 <b>(+49.06%)</b></td><td>0.10 <b>(+26.47%)</b></td><td>0.08 <b>(+317.48%)</b></td><td>0.03 (-5.33%)</td><td>583.80 <b>(-76.05%)</b></td><td>471.48 <b>(-50.48%)</b></td><td>489.10 <b>(-20.93%)</b></td><td>298.90 <b>(-32.08%)</b></td><td>113.34 <b>(-86.45%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>2437.10 (n/a)</td><td>952.10 (n/a)</td><td>618.60 (n/a)</td><td>440.10 (n/a)</td><td>836.72 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.22 <b>(+94.14%)</b></td><td>0.12 (+19.60%)</td><td>0.09 (-11.72%)</td><td>0.06 (-19.83%)</td><td>0.06 <b>(+291.89%)</b></td><td>779.10 <b>(+24.74%)</b></td><td>516.30 (-1.30%)</td><td>552.50 (+13.26%)</td><td>218.80 <b>(-48.51%)</b></td><td>212.92 <b>(+131.55%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>624.60 (n/a)</td><td>523.08 (n/a)</td><td>487.80 (n/a)</td><td>424.90 (n/a)</td><td>91.95 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (+9.96%)</td><td>0.01 (+14.27%)</td><td>0.01 (+18.88%)</td><td>0.01 (+8.81%)</td><td>0.00 (+15.87%)</td><td>445.70 (-8.08%)</td><td>312.44 (-12.11%)</td><td>257.30 (-15.89%)</td><td>245.90 (-9.06%)</td><td>90.18 (-6.50%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>484.90 (n/a)</td><td>355.48 (n/a)</td><td>305.90 (n/a)</td><td>270.40 (n/a)</td><td>96.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (+14.96%)</td><td>0.01 (+2.69%)</td><td>0.01 <b>(+20.78%)</b></td><td>0.00 <b>(-75.32%)</b></td><td>0.00 <b>(+121.98%)</b></td><td>1998.20 <b>(+305.23%)</b></td><td>628.54 <b>(+76.35%)</b></td><td>257.40 (-17.21%)</td><td>237.80 (-13.02%)</td><td>768.95 <b>(+702.81%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>493.10 (n/a)</td><td>356.42 (n/a)</td><td>310.90 (n/a)</td><td>273.40 (n/a)</td><td>95.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (+7.90%)</td><td>0.01 (+11.46%)</td><td>0.01 <b>(+48.79%)</b></td><td>0.00 <b>(-68.36%)</b></td><td>0.00 <b>(+76.16%)</b></td><td>1760.80 <b>(+216.01%)</b></td><td>602.14 <b>(+39.64%)</b></td><td>320.20 <b>(-32.79%)</b></td><td>253.70 (-7.31%)</td><td>650.91 <b>(+447.77%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>557.20 (n/a)</td><td>431.20 (n/a)</td><td>476.40 (n/a)</td><td>273.70 (n/a)</td><td>118.83 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 <b>(+33.82%)</b></td><td>0.01 (+1.69%)</td><td>0.00 (-19.38%)</td><td>0.00 (-18.99%)</td><td>0.00 <b>(+146.24%)</b></td><td>659.00 <b>(+23.43%)</b></td><td>494.14 (+10.48%)</td><td>555.50 <b>(+24.05%)</b></td><td>248.90 <b>(-25.28%)</b></td><td>182.86 <b>(+139.07%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>533.90 (n/a)</td><td>447.26 (n/a)</td><td>447.80 (n/a)</td><td>333.10 (n/a)</td><td>76.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (-11.72%)</td><td>0.01 (-12.10%)</td><td>0.01 (-1.58%)</td><td>0.00 (-14.41%)</td><td>0.00 (-18.94%)</td><td>620.60 (+16.83%)</td><td>428.42 (+12.26%)</td><td>400.80 (+1.60%)</td><td>263.70 (+13.27%)</td><td>132.69 (+7.43%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>531.20 (n/a)</td><td>381.62 (n/a)</td><td>394.50 (n/a)</td><td>232.80 (n/a)</td><td>123.51 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 <b>(+22.95%)</b></td><td>0.01 <b>(+39.20%)</b></td><td>0.01 <b>(+74.33%)</b></td><td>0.00 (+11.70%)</td><td>0.00 <b>(+42.87%)</b></td><td>622.90 (-10.48%)</td><td>385.78 <b>(-25.25%)</b></td><td>293.30 <b>(-42.64%)</b></td><td>251.70 (-18.65%)</td><td>156.71 (+7.72%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>695.80 (n/a)</td><td>516.10 (n/a)</td><td>511.30 (n/a)</td><td>309.40 (n/a)</td><td>145.48 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 <b>(+28.34%)</b></td><td>0.02 (+10.99%)</td><td>0.02 (+17.48%)</td><td>0.01 (-17.07%)</td><td>0.01 <b>(+102.75%)</b></td><td>556.00 <b>(+20.58%)</b></td><td>376.70 (+0.66%)</td><td>301.20 (-14.89%)</td><td>206.80 <b>(-22.08%)</b></td><td>161.27 <b>(+106.65%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>461.10 (n/a)</td><td>374.24 (n/a)</td><td>353.90 (n/a)</td><td>265.40 (n/a)</td><td>78.04 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 <b>(-47.98%)</b></td><td>0.01 <b>(-31.58%)</b></td><td>0.01 <b>(-33.11%)</b></td><td>0.01 (-16.45%)</td><td>0.00 <b>(-52.37%)</b></td><td>511.90 (+19.69%)</td><td>407.28 <b>(+39.15%)</b></td><td>452.80 <b>(+49.49%)</b></td><td>281.60 <b>(+92.22%)</b></td><td>115.71 (+15.60%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>427.70 (n/a)</td><td>292.70 (n/a)</td><td>302.90 (n/a)</td><td>146.50 (n/a)</td><td>100.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 <b>(+46.33%)</b></td><td>0.02 (+7.82%)</td><td>0.02 (-2.10%)</td><td>0.01 (-8.11%)</td><td>0.01 <b>(+92.83%)</b></td><td>630.90 (+8.83%)</td><td>397.34 (+4.96%)</td><td>316.80 (+2.16%)</td><td>186.10 <b>(-31.66%)</b></td><td>191.17 <b>(+50.90%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.70 (n/a)</td><td>378.58 (n/a)</td><td>310.10 (n/a)</td><td>272.30 (n/a)</td><td>126.69 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (+17.38%)</td><td>0.01 <b>(+35.82%)</b></td><td>0.01 <b>(+50.71%)</b></td><td>0.01 <b>(+53.34%)</b></td><td>0.00 (-10.74%)</td><td>469.20 <b>(-34.79%)</b></td><td>383.34 <b>(-29.74%)</b></td><td>386.00 <b>(-33.65%)</b></td><td>285.20 (-14.81%)</td><td>83.70 <b>(-49.99%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>719.50 (n/a)</td><td>545.60 (n/a)</td><td>581.80 (n/a)</td><td>334.80 (n/a)</td><td>167.36 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (-8.35%)</td><td>0.02 <b>(+29.02%)</b></td><td>0.02 <b>(+63.96%)</b></td><td>0.01 <b>(+113.13%)</b></td><td>0.00 <b>(-41.45%)</b></td><td>469.10 <b>(-53.08%)</b></td><td>302.40 <b>(-36.99%)</b></td><td>259.70 <b>(-39.02%)</b></td><td>245.00 (+9.13%)</td><td>94.48 <b>(-69.43%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>999.80 (n/a)</td><td>479.90 (n/a)</td><td>425.90 (n/a)</td><td>224.50 (n/a)</td><td>309.10 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (-5.50%)</td><td>0.01 (+11.98%)</td><td>0.01 <b>(+21.06%)</b></td><td>0.01 <b>(+57.63%)</b></td><td>0.00 <b>(-62.35%)</b></td><td>438.20 <b>(-36.57%)</b></td><td>377.78 (-16.93%)</td><td>364.80 (-17.39%)</td><td>336.70 (+5.81%)</td><td>39.87 <b>(-73.72%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>690.80 (n/a)</td><td>454.76 (n/a)</td><td>441.60 (n/a)</td><td>318.20 (n/a)</td><td>151.72 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (-9.71%)</td><td>0.03 (+1.26%)</td><td>0.04 (+8.14%)</td><td>0.02 (-17.85%)</td><td>0.01 (+4.80%)</td><td>457.90 <b>(+21.72%)</b></td><td>313.50 (+0.02%)</td><td>272.90 (-7.52%)</td><td>267.60 (+10.76%)</td><td>81.74 <b>(+37.54%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>376.20 (n/a)</td><td>313.44 (n/a)</td><td>295.10 (n/a)</td><td>241.60 (n/a)</td><td>59.43 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (-11.46%)</td><td>0.03 (-3.97%)</td><td>0.04 (+6.99%)</td><td>0.02 <b>(-21.31%)</b></td><td>0.01 (+7.78%)</td><td>590.00 <b>(+27.10%)</b></td><td>360.18 (+9.82%)</td><td>273.80 (-6.52%)</td><td>226.10 (+12.94%)</td><td>161.54 <b>(+48.64%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>464.20 (n/a)</td><td>327.98 (n/a)</td><td>292.90 (n/a)</td><td>200.20 (n/a)</td><td>108.68 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 <b>(+25.63%)</b></td><td>0.04 <b>(+21.49%)</b></td><td>0.04 (+17.02%)</td><td>0.02 (+17.81%)</td><td>0.01 (+11.98%)</td><td>431.40 (-15.11%)</td><td>289.96 (-18.29%)</td><td>247.10 (-14.53%)</td><td>217.40 <b>(-20.40%)</b></td><td>86.22 <b>(-20.11%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.20 (n/a)</td><td>354.86 (n/a)</td><td>289.10 (n/a)</td><td>273.10 (n/a)</td><td>107.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (-0.06%)</td><td>0.03 (-2.73%)</td><td>0.02 <b>(-25.50%)</b></td><td>0.02 (-9.68%)</td><td>0.01 <b>(+28.40%)</b></td><td>531.30 (+10.71%)</td><td>399.20 (+8.23%)</td><td>476.00 <b>(+34.24%)</b></td><td>236.00 (+0.08%)</td><td>143.62 <b>(+33.16%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>479.90 (n/a)</td><td>368.86 (n/a)</td><td>354.60 (n/a)</td><td>235.80 (n/a)</td><td>107.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (-2.35%)</td><td>0.03 (-12.81%)</td><td>0.04 (-1.32%)</td><td>0.02 <b>(-40.07%)</b></td><td>0.01 <b>(+90.80%)</b></td><td>608.70 <b>(+66.86%)</b></td><td>386.38 <b>(+26.05%)</b></td><td>295.00 (+1.34%)</td><td>263.50 (+2.41%)</td><td>155.13 <b>(+215.46%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>364.80 (n/a)</td><td>306.52 (n/a)</td><td>291.10 (n/a)</td><td>257.30 (n/a)</td><td>49.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (-4.04%)</td><td>0.03 (+12.99%)</td><td>0.03 <b>(+22.72%)</b></td><td>0.02 (-3.93%)</td><td>0.01 (+9.22%)</td><td>630.00 (+4.10%)</td><td>440.38 (-9.52%)</td><td>418.10 (-18.51%)</td><td>295.40 (+4.20%)</td><td>149.01 <b>(+21.74%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>605.20 (n/a)</td><td>486.70 (n/a)</td><td>513.10 (n/a)</td><td>283.50 (n/a)</td><td>122.40 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (-0.62%)</td><td>0.05 (-18.50%)</td><td>0.05 <b>(-34.16%)</b></td><td>0.03 (-1.66%)</td><td>0.02 (+8.82%)</td><td>750.00 (+1.68%)</td><td>464.08 <b>(+24.13%)</b></td><td>429.10 <b>(+51.89%)</b></td><td>254.90 (+0.63%)</td><td>208.13 (+1.79%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>737.60 (n/a)</td><td>373.88 (n/a)</td><td>282.50 (n/a)</td><td>253.30 (n/a)</td><td>204.46 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 <b>(+38.16%)</b></td><td>0.06 (+7.92%)</td><td>0.06 (-3.82%)</td><td>0.03 <b>(-25.75%)</b></td><td>0.03 <b>(+152.91%)</b></td><td>610.10 <b>(+34.68%)</b></td><td>387.40 (+5.22%)</td><td>351.10 (+3.97%)</td><td>218.10 <b>(-27.61%)</b></td><td>168.83 <b>(+141.47%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>453.00 (n/a)</td><td>368.18 (n/a)</td><td>337.70 (n/a)</td><td>301.30 (n/a)</td><td>69.92 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.09 <b>(+25.06%)</b></td><td>0.07 <b>(+27.22%)</b></td><td>0.08 <b>(+76.49%)</b></td><td>0.03 (+5.69%)</td><td>0.03 <b>(+78.71%)</b></td><td>609.60 (-5.39%)</td><td>379.42 (-11.89%)</td><td>249.00 <b>(-43.33%)</b></td><td>221.00 <b>(-20.04%)</b></td><td>193.30 <b>(+39.62%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>644.30 (n/a)</td><td>430.62 (n/a)</td><td>439.40 (n/a)</td><td>276.40 (n/a)</td><td>138.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (+13.85%)</td><td>0.05 <b>(+26.14%)</b></td><td>0.05 <b>(+27.77%)</b></td><td>0.03 <b>(+203.03%)</b></td><td>0.02 (-5.95%)</td><td>636.90 <b>(-67.00%)</b></td><td>436.80 <b>(-40.53%)</b></td><td>387.70 <b>(-21.74%)</b></td><td>279.20 (-12.17%)</td><td>172.27 <b>(-74.56%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1930.10 (n/a)</td><td>734.44 (n/a)</td><td>495.40 (n/a)</td><td>317.90 (n/a)</td><td>677.06 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 <b>(+41.97%)</b></td><td>0.07 <b>(+38.55%)</b></td><td>0.08 <b>(+56.31%)</b></td><td>0.04 <b>(+27.36%)</b></td><td>0.03 <b>(+75.33%)</b></td><td>502.60 <b>(-21.48%)</b></td><td>325.06 <b>(-23.88%)</b></td><td>250.10 <b>(-36.02%)</b></td><td>197.70 <b>(-29.57%)</b></td><td>133.74 (-1.44%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>640.10 (n/a)</td><td>427.02 (n/a)</td><td>390.90 (n/a)</td><td>280.70 (n/a)</td><td>135.69 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (-2.31%)</td><td>0.05 <b>(+46.39%)</b></td><td>0.05 (+5.86%)</td><td>0.03 <b>(+286.98%)</b></td><td>0.02 <b>(-37.88%)</b></td><td>648.30 <b>(-74.16%)</b></td><td>441.60 <b>(-62.00%)</b></td><td>465.90 (-5.54%)</td><td>303.20 (+2.36%)</td><td>143.12 <b>(-86.12%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2508.60 (n/a)</td><td>1162.24 (n/a)</td><td>493.20 (n/a)</td><td>296.20 (n/a)</td><td>1031.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>492.60 (n/a)</td><td>353.86 (n/a)</td><td>327.50 (n/a)</td><td>293.00 (n/a)</td><td>79.02 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>537.20 (n/a)</td><td>363.52 (n/a)</td><td>393.60 (n/a)</td><td>187.80 (n/a)</td><td>139.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.30 (n/a)</td><td>461.14 (n/a)</td><td>505.20 (n/a)</td><td>354.70 (n/a)</td><td>70.66 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>465.10 (n/a)</td><td>319.14 (n/a)</td><td>276.00 (n/a)</td><td>266.60 (n/a)</td><td>83.60 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2434.20 (n/a)</td><td>843.30 (n/a)</td><td>477.70 (n/a)</td><td>237.60 (n/a)</td><td>898.71 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>551.30 (n/a)</td><td>412.06 (n/a)</td><td>381.60 (n/a)</td><td>268.00 (n/a)</td><td>129.04 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>431.80 (n/a)</td><td>299.06 (n/a)</td><td>274.30 (n/a)</td><td>239.40 (n/a)</td><td>75.81 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>587.00 (n/a)</td><td>449.54 (n/a)</td><td>534.30 (n/a)</td><td>286.70 (n/a)</td><td>147.18 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>584.80 (n/a)</td><td>383.44 (n/a)</td><td>380.80 (n/a)</td><td>208.90 (n/a)</td><td>148.88 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.17 (-18.07%)</td><td>0.11 <b>(-22.87%)</b></td><td>0.10 <b>(-39.74%)</b></td><td>0.03 (+6.34%)</td><td>0.06 <b>(-21.01%)</b></td><td>1849.80 (-5.96%)</td><td>699.84 (+9.85%)</td><td>501.90 <b>(+65.97%)</b></td><td>288.30 <b>(+22.06%)</b></td><td>653.83 (-12.54%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>0.08 (n/a)</td><td>1967.10 (n/a)</td><td>637.08 (n/a)</td><td>302.40 (n/a)</td><td>236.20 (n/a)</td><td>747.60 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>652.10 (n/a)</td><td>430.10 (n/a)</td><td>473.40 (n/a)</td><td>219.70 (n/a)</td><td>165.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>639.20 (n/a)</td><td>373.66 (n/a)</td><td>324.00 (n/a)</td><td>233.40 (n/a)</td><td>157.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>694.10 (n/a)</td><td>520.42 (n/a)</td><td>499.70 (n/a)</td><td>359.20 (n/a)</td><td>137.56 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>405.90 (n/a)</td><td>299.78 (n/a)</td><td>279.90 (n/a)</td><td>247.60 (n/a)</td><td>62.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.40 (n/a)</td><td>468.48 (n/a)</td><td>532.80 (n/a)</td><td>238.30 (n/a)</td><td>147.06 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>568.80 (n/a)</td><td>397.72 (n/a)</td><td>310.90 (n/a)</td><td>274.00 (n/a)</td><td>141.89 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1069.60 (n/a)</td><td>563.68 (n/a)</td><td>486.30 (n/a)</td><td>237.60 (n/a)</td><td>312.81 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>677.30 (n/a)</td><td>527.92 (n/a)</td><td>513.20 (n/a)</td><td>394.50 (n/a)</td><td>125.56 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>486.50 (n/a)</td><td>440.74 (n/a)</td><td>463.30 (n/a)</td><td>365.30 (n/a)</td><td>50.18 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>716.70 (n/a)</td><td>500.24 (n/a)</td><td>561.30 (n/a)</td><td>243.50 (n/a)</td><td>208.57 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>430.20 (n/a)</td><td>340.50 (n/a)</td><td>342.50 (n/a)</td><td>248.40 (n/a)</td><td>85.21 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>1079.30 (n/a)</td><td>615.70 (n/a)</td><td>531.50 (n/a)</td><td>333.60 (n/a)</td><td>297.64 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>526.70 (n/a)</td><td>394.40 (n/a)</td><td>419.50 (n/a)</td><td>202.90 (n/a)</td><td>123.90 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.15 (+5.61%)</td><td>2.12 (-7.85%)</td><td>1.82 <b>(-20.86%)</b></td><td>1.57 (-1.95%)</td><td>0.66 <b>(+34.82%)</b></td><td>6691.70 (+1.99%)</td><td>5288.40 (+11.60%)</td><td>5763.20 <b>(+26.36%)</b></td><td>3331.60 (-5.31%)</td><td>1410.68 <b>(+26.77%)</b></td><td>1289.16 (+5.61%)</td><td>869.08 (-7.85%)</td><td>745.24 <b>(-20.86%)</b></td><td>641.84 (-1.95%)</td><td>270.77 <b>(+34.82%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.98 (n/a)</td><td>2.30 (n/a)</td><td>2.30 (n/a)</td><td>1.60 (n/a)</td><td>0.49 (n/a)</td><td>6560.90 (n/a)</td><td>4738.86 (n/a)</td><td>4560.90 (n/a)</td><td>3518.50 (n/a)</td><td>1112.80 (n/a)</td><td>1220.66 (n/a)</td><td>943.11 (n/a)</td><td>941.70 (n/a)</td><td>654.63 (n/a)</td><td>200.83 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.63 (+1.92%)</td><td>2.53 (+3.24%)</td><td>2.55 (-0.52%)</td><td>2.43 (+15.34%)</td><td>0.07 <b>(-63.96%)</b></td><td>9692.40 (-13.30%)</td><td>9317.76 (-3.64%)</td><td>9256.90 (+0.53%)</td><td>8970.40 (-1.89%)</td><td>264.20 <b>(-69.45%)</b></td><td>1496.23 (+1.92%)</td><td>1441.38 (+3.24%)</td><td>1449.92 (-0.52%)</td><td>1384.78 (+15.34%)</td><td>40.74 <b>(-63.95%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.58 (n/a)</td><td>2.45 (n/a)</td><td>2.56 (n/a)</td><td>2.11 (n/a)</td><td>0.20 (n/a)</td><td>11179.20 (n/a)</td><td>9669.32 (n/a)</td><td>9208.40 (n/a)</td><td>9143.00 (n/a)</td><td>864.85 (n/a)</td><td>1467.98 (n/a)</td><td>1396.16 (n/a)</td><td>1457.56 (n/a)</td><td>1200.60 (n/a)</td><td>113.02 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.69 (-2.44%)</td><td>2.49 (+2.16%)</td><td>2.56 (+11.14%)</td><td>2.20 (+0.98%)</td><td>0.21 (-15.67%)</td><td>7636.60 (-0.97%)</td><td>6791.88 (-2.34%)</td><td>6546.80 (-10.02%)</td><td>6247.10 (+2.50%)</td><td>599.30 (-13.92%)</td><td>1375.02 (-2.44%)</td><td>1272.37 (+2.16%)</td><td>1312.09 (+11.14%)</td><td>1124.83 (+0.98%)</td><td>108.23 (-15.67%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.75 (n/a)</td><td>2.43 (n/a)</td><td>2.31 (n/a)</td><td>2.18 (n/a)</td><td>0.25 (n/a)</td><td>7711.20 (n/a)</td><td>6954.56 (n/a)</td><td>7276.20 (n/a)</td><td>6094.70 (n/a)</td><td>696.22 (n/a)</td><td>1409.41 (n/a)</td><td>1245.41 (n/a)</td><td>1180.55 (n/a)</td><td>1113.96 (n/a)</td><td>128.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.96 (-1.68%)</td><td>0.69 (-2.90%)</td><td>0.67 (+7.15%)</td><td>0.36 <b>(-29.24%)</b></td><td>0.24 <b>(+31.20%)</b></td><td>1273.80 <b>(+41.31%)</b></td><td>754.50 (+10.51%)</td><td>681.90 (-6.68%)</td><td>476.20 (+1.69%)</td><td>320.49 <b>(+91.14%)</b></td><td>70.46 (-1.68%)</td><td>50.26 (-2.90%)</td><td>49.20 (+7.15%)</td><td>26.34 <b>(-29.24%)</b></td><td>17.79 <b>(+31.20%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.98 (n/a)</td><td>0.71 (n/a)</td><td>0.63 (n/a)</td><td>0.51 (n/a)</td><td>0.19 (n/a)</td><td>901.40 (n/a)</td><td>682.76 (n/a)</td><td>730.70 (n/a)</td><td>468.30 (n/a)</td><td>167.67 (n/a)</td><td>71.66 (n/a)</td><td>51.76 (n/a)</td><td>45.92 (n/a)</td><td>37.23 (n/a)</td><td>13.56 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.39 (+9.98%)</td><td>0.88 (-8.78%)</td><td>0.91 (+0.11%)</td><td>0.20 <b>(-64.59%)</b></td><td>0.47 <b>(+67.48%)</b></td><td>3307.40 <b>(+182.37%)</b></td><td>1198.36 <b>(+62.88%)</b></td><td>718.90 (-0.11%)</td><td>472.90 (-9.08%)</td><td>1194.73 <b>(+356.05%)</b></td><td>141.92 (+9.98%)</td><td>90.49 (-8.78%)</td><td>93.35 (+0.11%)</td><td>20.29 <b>(-64.59%)</b></td><td>48.45 <b>(+67.48%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.26 (n/a)</td><td>0.97 (n/a)</td><td>0.91 (n/a)</td><td>0.56 (n/a)</td><td>0.28 (n/a)</td><td>1171.30 (n/a)</td><td>735.72 (n/a)</td><td>719.70 (n/a)</td><td>520.10 (n/a)</td><td>261.97 (n/a)</td><td>129.04 (n/a)</td><td>99.20 (n/a)</td><td>93.25 (n/a)</td><td>57.29 (n/a)</td><td>28.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.27 (-5.90%)</td><td>1.10 (-6.01%)</td><td>1.10 (-16.15%)</td><td>0.99 (+9.83%)</td><td>0.12 <b>(-45.70%)</b></td><td>765.10 (-8.94%)</td><td>688.30 (+4.16%)</td><td>683.10 (+19.26%)</td><td>595.20 (+6.27%)</td><td>72.37 <b>(-45.62%)</b></td><td>140.93 (-5.90%)</td><td>122.98 (-6.01%)</td><td>122.80 (-16.15%)</td><td>109.65 (+9.83%)</td><td>13.16 <b>(-45.70%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.35 (n/a)</td><td>1.18 (n/a)</td><td>1.32 (n/a)</td><td>0.90 (n/a)</td><td>0.22 (n/a)</td><td>840.20 (n/a)</td><td>660.80 (n/a)</td><td>572.80 (n/a)</td><td>560.10 (n/a)</td><td>133.10 (n/a)</td><td>149.76 (n/a)</td><td>130.84 (n/a)</td><td>146.45 (n/a)</td><td>99.84 (n/a)</td><td>24.24 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.68 <b>(+24.81%)</b></td><td>1.15 <b>(+32.00%)</b></td><td>1.10 (-2.32%)</td><td>0.75 <b>(+153.49%)</b></td><td>0.36 <b>(-25.40%)</b></td><td>1396.20 <b>(-60.55%)</b></td><td>983.00 <b>(-43.08%)</b></td><td>953.30 (+2.37%)</td><td>625.90 (-19.88%)</td><td>295.00 <b>(-76.06%)</b></td><td>214.43 <b>(+24.81%)</b></td><td>147.10 <b>(+32.00%)</b></td><td>140.80 (-2.32%)</td><td>96.13 <b>(+153.49%)</b></td><td>45.45 <b>(-25.40%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.34 (n/a)</td><td>0.87 (n/a)</td><td>1.13 (n/a)</td><td>0.30 (n/a)</td><td>0.48 (n/a)</td><td>3539.40 (n/a)</td><td>1727.06 (n/a)</td><td>931.20 (n/a)</td><td>781.20 (n/a)</td><td>1232.14 (n/a)</td><td>171.80 (n/a)</td><td>111.44 (n/a)</td><td>144.14 (n/a)</td><td>37.92 (n/a)</td><td>60.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.00 (-2.58%)</td><td>1.57 (+4.48%)</td><td>1.88 (+10.07%)</td><td>0.30 <b>(-67.55%)</b></td><td>0.72 <b>(+50.24%)</b></td><td>3471.60 <b>(+208.15%)</b></td><td>1139.96 <b>(+49.12%)</b></td><td>557.20 (-9.16%)</td><td>524.70 (+2.66%)</td><td>1303.93 <b>(+383.98%)</b></td><td>255.82 (-2.58%)</td><td>201.27 (+4.48%)</td><td>240.86 (+10.07%)</td><td>38.66 <b>(-67.55%)</b></td><td>92.12 <b>(+50.24%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.05 (n/a)</td><td>1.51 (n/a)</td><td>1.71 (n/a)</td><td>0.93 (n/a)</td><td>0.48 (n/a)</td><td>1126.60 (n/a)</td><td>764.46 (n/a)</td><td>613.40 (n/a)</td><td>511.10 (n/a)</td><td>269.42 (n/a)</td><td>262.60 (n/a)</td><td>192.64 (n/a)</td><td>218.83 (n/a)</td><td>119.13 (n/a)</td><td>61.32 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.99 (+7.01%)</td><td>1.27 (+5.16%)</td><td>1.29 (-0.59%)</td><td>0.44 <b>(+50.52%)</b></td><td>0.55 (-2.89%)</td><td>2384.10 <b>(-33.57%)</b></td><td>1066.76 (-19.14%)</td><td>814.00 (+0.59%)</td><td>526.60 (-6.56%)</td><td>746.48 <b>(-41.38%)</b></td><td>254.86 (+7.01%)</td><td>161.96 (+5.16%)</td><td>164.88 (-0.59%)</td><td>56.30 <b>(+50.52%)</b></td><td>70.48 (-2.89%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.86 (n/a)</td><td>1.20 (n/a)</td><td>1.30 (n/a)</td><td>0.29 (n/a)</td><td>0.57 (n/a)</td><td>3588.70 (n/a)</td><td>1319.32 (n/a)</td><td>809.20 (n/a)</td><td>563.60 (n/a)</td><td>1273.38 (n/a)</td><td>238.16 (n/a)</td><td>154.00 (n/a)</td><td>165.86 (n/a)</td><td>37.40 (n/a)</td><td>72.58 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.90 (+12.96%)</td><td>1.47 <b>(+25.91%)</b></td><td>1.80 <b>(+49.47%)</b></td><td>0.31 (+7.21%)</td><td>0.66 (+19.72%)</td><td>3371.70 (-6.73%)</td><td>1152.34 (-14.45%)</td><td>583.90 <b>(-33.09%)</b></td><td>551.30 (-11.47%)</td><td>1241.57 (-2.70%)</td><td>243.47 (+12.96%)</td><td>188.75 <b>(+25.91%)</b></td><td>229.87 <b>(+49.47%)</b></td><td>39.81 (+7.21%)</td><td>84.94 (+19.72%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.68 (n/a)</td><td>1.17 (n/a)</td><td>1.20 (n/a)</td><td>0.29 (n/a)</td><td>0.55 (n/a)</td><td>3614.90 (n/a)</td><td>1346.98 (n/a)</td><td>872.70 (n/a)</td><td>622.70 (n/a)</td><td>1276.05 (n/a)</td><td>215.53 (n/a)</td><td>149.90 (n/a)</td><td>153.80 (n/a)</td><td>37.13 (n/a)</td><td>70.95 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.19 <b>(-27.41%)</b></td><td>0.90 (-13.20%)</td><td>0.86 (-14.40%)</td><td>0.46 <b>(+40.67%)</b></td><td>0.30 <b>(-43.73%)</b></td><td>2273.40 <b>(-28.91%)</b></td><td>1306.48 (-6.25%)</td><td>1223.30 (+16.83%)</td><td>882.20 <b>(+37.76%)</b></td><td>568.07 <b>(-45.84%)</b></td><td>152.15 <b>(-27.41%)</b></td><td>115.44 (-13.20%)</td><td>109.72 (-14.40%)</td><td>59.04 <b>(+40.67%)</b></td><td>38.02 <b>(-43.73%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.64 (n/a)</td><td>1.04 (n/a)</td><td>1.00 (n/a)</td><td>0.33 (n/a)</td><td>0.53 (n/a)</td><td>3198.10 (n/a)</td><td>1393.54 (n/a)</td><td>1047.10 (n/a)</td><td>640.40 (n/a)</td><td>1048.84 (n/a)</td><td>209.59 (n/a)</td><td>132.99 (n/a)</td><td>128.18 (n/a)</td><td>41.97 (n/a)</td><td>67.57 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.69 <b>(+23.81%)</b></td><td>1.35 <b>(+56.76%)</b></td><td>1.43 <b>(+71.54%)</b></td><td>0.90 <b>(+110.74%)</b></td><td>0.31 <b>(-27.67%)</b></td><td>1160.70 <b>(-52.55%)</b></td><td>813.42 <b>(-46.30%)</b></td><td>733.50 <b>(-41.70%)</b></td><td>620.60 (-19.22%)</td><td>215.38 <b>(-72.49%)</b></td><td>216.29 <b>(+23.81%)</b></td><td>173.24 <b>(+56.76%)</b></td><td>182.98 <b>(+71.54%)</b></td><td>115.64 <b>(+110.74%)</b></td><td>39.47 <b>(-27.67%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.36 (n/a)</td><td>0.86 (n/a)</td><td>0.83 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>2446.00 (n/a)</td><td>1514.62 (n/a)</td><td>1258.20 (n/a)</td><td>768.30 (n/a)</td><td>782.97 (n/a)</td><td>174.69 (n/a)</td><td>110.51 (n/a)</td><td>106.67 (n/a)</td><td>54.87 (n/a)</td><td>54.57 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.98 <b>(+21.05%)</b></td><td>0.67 (+10.34%)</td><td>0.54 (-8.57%)</td><td>0.52 (+19.57%)</td><td>0.20 <b>(+34.04%)</b></td><td>691.20 (-16.36%)</td><td>576.04 (-8.14%)</td><td>669.50 (+9.36%)</td><td>367.90 (-17.38%)</td><td>146.36 (-4.82%)</td><td>45.61 <b>(+21.05%)</b></td><td>31.01 (+10.34%)</td><td>25.06 (-8.57%)</td><td>24.27 (+19.57%)</td><td>9.37 <b>(+34.04%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.81 (n/a)</td><td>0.60 (n/a)</td><td>0.59 (n/a)</td><td>0.44 (n/a)</td><td>0.15 (n/a)</td><td>826.40 (n/a)</td><td>627.10 (n/a)</td><td>612.20 (n/a)</td><td>445.30 (n/a)</td><td>153.78 (n/a)</td><td>37.68 (n/a)</td><td>28.10 (n/a)</td><td>27.41 (n/a)</td><td>20.30 (n/a)</td><td>6.99 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.57 (-2.42%)</td><td>1.86 (+2.80%)</td><td>1.89 (+11.69%)</td><td>1.10 (+10.07%)</td><td>0.53 <b>(-33.79%)</b></td><td>3812.00 (-9.15%)</td><td>2439.66 (-11.33%)</td><td>2221.20 (-10.46%)</td><td>1632.10 (+2.49%)</td><td>820.40 <b>(-33.68%)</b></td><td>657.90 (-2.42%)</td><td>475.00 (+2.80%)</td><td>483.41 (+11.69%)</td><td>281.67 (+10.07%)</td><td>135.15 <b>(-33.79%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.63 (n/a)</td><td>1.81 (n/a)</td><td>1.69 (n/a)</td><td>1.00 (n/a)</td><td>0.80 (n/a)</td><td>4195.80 (n/a)</td><td>2751.28 (n/a)</td><td>2480.70 (n/a)</td><td>1592.50 (n/a)</td><td>1237.00 (n/a)</td><td>674.24 (n/a)</td><td>462.08 (n/a)</td><td>432.83 (n/a)</td><td>255.91 (n/a)</td><td>204.14 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.03 (-10.01%)</td><td>2.11 <b>(+23.23%)</b></td><td>2.29 <b>(+76.76%)</b></td><td>1.14 (+7.11%)</td><td>0.90 (-6.69%)</td><td>2294.10 (-6.64%)</td><td>1479.66 (-19.21%)</td><td>1146.20 <b>(-43.43%)</b></td><td>864.30 (+11.12%)</td><td>701.34 (+1.32%)</td><td>621.14 (-10.01%)</td><td>431.63 <b>(+23.23%)</b></td><td>468.40 <b>(+76.76%)</b></td><td>234.03 (+7.11%)</td><td>183.94 (-6.69%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.37 (n/a)</td><td>1.71 (n/a)</td><td>1.29 (n/a)</td><td>1.07 (n/a)</td><td>0.96 (n/a)</td><td>2457.30 (n/a)</td><td>1831.56 (n/a)</td><td>2026.00 (n/a)</td><td>777.80 (n/a)</td><td>692.20 (n/a)</td><td>690.21 (n/a)</td><td>350.28 (n/a)</td><td>264.99 (n/a)</td><td>218.48 (n/a)</td><td>197.12 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.76 (+2.67%)</td><td>2.07 (-19.48%)</td><td>1.88 <b>(-27.12%)</b></td><td>1.42 <b>(-42.53%)</b></td><td>0.56 <b>(+470.84%)</b></td><td>5553.80 <b>(+74.00%)</b></td><td>4024.62 <b>(+31.56%)</b></td><td>4182.80 <b>(+37.21%)</b></td><td>2849.70 (-2.60%)</td><td>1089.28 <b>(+839.92%)</b></td><td>847.77 (+2.67%)</td><td>636.62 (-19.48%)</td><td>577.58 <b>(-27.12%)</b></td><td>435.00 <b>(-42.53%)</b></td><td>170.86 <b>(+470.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.69 (n/a)</td><td>2.57 (n/a)</td><td>2.58 (n/a)</td><td>2.46 (n/a)</td><td>0.10 (n/a)</td><td>3191.80 (n/a)</td><td>3059.18 (n/a)</td><td>3048.50 (n/a)</td><td>2925.80 (n/a)</td><td>115.89 (n/a)</td><td>825.74 (n/a)</td><td>790.64 (n/a)</td><td>792.50 (n/a)</td><td>756.91 (n/a)</td><td>29.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>478.00 (n/a)</td><td>360.14 (n/a)</td><td>309.80 (n/a)</td><td>256.00 (n/a)</td><td>108.91 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>483.70 (n/a)</td><td>315.20 (n/a)</td><td>293.50 (n/a)</td><td>185.10 (n/a)</td><td>109.19 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>606.50 (n/a)</td><td>356.18 (n/a)</td><td>323.60 (n/a)</td><td>211.10 (n/a)</td><td>148.48 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>570.30 (n/a)</td><td>420.10 (n/a)</td><td>374.00 (n/a)</td><td>257.50 (n/a)</td><td>141.18 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1852.80 (n/a)</td><td>679.62 (n/a)</td><td>491.80 (n/a)</td><td>260.00 (n/a)</td><td>666.38 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>586.30 (n/a)</td><td>495.34 (n/a)</td><td>512.90 (n/a)</td><td>368.70 (n/a)</td><td>94.83 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.60 (n/a)</td><td>354.02 (n/a)</td><td>308.70 (n/a)</td><td>277.70 (n/a)</td><td>94.81 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1982.20 (n/a)</td><td>673.46 (n/a)</td><td>300.10 (n/a)</td><td>267.70 (n/a)</td><td>740.57 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.80 (n/a)</td><td>462.08 (n/a)</td><td>552.80 (n/a)</td><td>218.30 (n/a)</td><td>182.65 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.90 (n/a)</td><td>398.62 (n/a)</td><td>305.10 (n/a)</td><td>245.00 (n/a)</td><td>182.47 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.80 (n/a)</td><td>446.16 (n/a)</td><td>483.40 (n/a)</td><td>240.40 (n/a)</td><td>123.70 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.50 (n/a)</td><td>399.28 (n/a)</td><td>336.20 (n/a)</td><td>243.60 (n/a)</td><td>136.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>702.50 (n/a)</td><td>501.72 (n/a)</td><td>521.30 (n/a)</td><td>286.80 (n/a)</td><td>148.46 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>641.50 (n/a)</td><td>374.84 (n/a)</td><td>312.20 (n/a)</td><td>251.80 (n/a)</td><td>154.08 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>473.20 (n/a)</td><td>325.70 (n/a)</td><td>308.60 (n/a)</td><td>256.80 (n/a)</td><td>85.58 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>581.70 (n/a)</td><td>341.80 (n/a)</td><td>256.60 (n/a)</td><td>213.30 (n/a)</td><td>154.96 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1941.60 (n/a)</td><td>634.78 (n/a)</td><td>244.40 (n/a)</td><td>190.60 (n/a)</td><td>744.60 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>548.50 (n/a)</td><td>429.74 (n/a)</td><td>452.30 (n/a)</td><td>306.20 (n/a)</td><td>100.34 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>618.90 (n/a)</td><td>434.18 (n/a)</td><td>356.50 (n/a)</td><td>286.30 (n/a)</td><td>163.75 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>384.70 (n/a)</td><td>317.50 (n/a)</td><td>293.50 (n/a)</td><td>285.00 (n/a)</td><td>41.58 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>674.50 (n/a)</td><td>473.02 (n/a)</td><td>487.10 (n/a)</td><td>267.30 (n/a)</td><td>154.43 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>704.00 (n/a)</td><td>443.88 (n/a)</td><td>404.60 (n/a)</td><td>285.90 (n/a)</td><td>171.06 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>600.60 (n/a)</td><td>490.56 (n/a)</td><td>533.30 (n/a)</td><td>222.50 (n/a)</td><td>155.67 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>601.10 (n/a)</td><td>473.16 (n/a)</td><td>465.60 (n/a)</td><td>309.50 (n/a)</td><td>125.23 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.68 <b>(+44.04%)</b></td><td>0.52 <b>(+63.36%)</b></td><td>0.53 <b>(+63.97%)</b></td><td>0.31 <b>(+139.73%)</b></td><td>0.14 (+9.67%)</td><td>721.30 <b>(-58.29%)</b></td><td>453.46 <b>(-45.87%)</b></td><td>416.20 <b>(-39.02%)</b></td><td>323.60 <b>(-30.57%)</b></td><td>154.63 <b>(-69.49%)</b></td><td>29.17 <b>(+44.04%)</b></td><td>22.36 <b>(+63.36%)</b></td><td>22.67 <b>(+63.96%)</b></td><td>13.08 <b>(+139.73%)</b></td><td>5.85 (+9.67%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>1729.30 (n/a)</td><td>837.76 (n/a)</td><td>682.50 (n/a)</td><td>466.10 (n/a)</td><td>506.74 (n/a)</td><td>20.25 (n/a)</td><td>13.69 (n/a)</td><td>13.83 (n/a)</td><td>5.46 (n/a)</td><td>5.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.48 <b>(-25.44%)</b></td><td>0.42 (-10.38%)</td><td>0.44 (-0.96%)</td><td>0.35 (+7.62%)</td><td>0.06 <b>(-53.85%)</b></td><td>637.10 (-7.09%)</td><td>532.50 (+7.13%)</td><td>508.30 (+0.97%)</td><td>465.30 <b>(+34.09%)</b></td><td>75.59 <b>(-42.66%)</b></td><td>20.28 <b>(-25.44%)</b></td><td>18.00 (-10.38%)</td><td>18.57 (-0.96%)</td><td>14.81 (+7.62%)</td><td>2.44 <b>(-53.85%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.64 (n/a)</td><td>0.47 (n/a)</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.12 (n/a)</td><td>685.70 (n/a)</td><td>497.04 (n/a)</td><td>503.40 (n/a)</td><td>347.00 (n/a)</td><td>131.82 (n/a)</td><td>27.20 (n/a)</td><td>20.08 (n/a)</td><td>18.75 (n/a)</td><td>13.76 (n/a)</td><td>5.28 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.31 (+0.07%)</td><td>0.30 (-0.64%)</td><td>0.30 (-1.34%)</td><td>0.30 (-0.53%)</td><td>0.01 <b>(+31.72%)</b></td><td>84241.50 (+0.53%)</td><td>82658.54 (+0.66%)</td><td>82968.40 (+1.36%)</td><td>80959.10 (-0.07%)</td><td>1582.46 <b>(+32.35%)</b></td><td>212.20 (+0.07%)</td><td>207.90 (-0.64%)</td><td>207.07 (-1.34%)</td><td>203.94 (-0.53%)</td><td>3.99 <b>(+31.73%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83798.80 (n/a)</td><td>82118.34 (n/a)</td><td>81858.00 (n/a)</td><td>81019.00 (n/a)</td><td>1195.69 (n/a)</td><td>212.05 (n/a)</td><td>209.24 (n/a)</td><td>209.87 (n/a)</td><td>205.01 (n/a)</td><td>3.03 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.14 (-2.30%)</td><td>1.12 (-2.37%)</td><td>1.14 (-0.89%)</td><td>1.05 (-6.10%)</td><td>0.04 <b>(+107.74%)</b></td><td>23929.60 (+6.49%)</td><td>22558.10 (+2.51%)</td><td>22148.00 (+0.90%)</td><td>21993.00 (+2.36%)</td><td>818.36 <b>(+126.65%)</b></td><td>781.15 (-2.30%)</td><td>762.36 (-2.37%)</td><td>775.68 (-0.89%)</td><td>717.93 (-6.10%)</td><td>26.71 <b>(+107.74%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.17 (n/a)</td><td>1.14 (n/a)</td><td>1.15 (n/a)</td><td>1.12 (n/a)</td><td>0.02 (n/a)</td><td>22470.80 (n/a)</td><td>22006.68 (n/a)</td><td>21951.20 (n/a)</td><td>21486.20 (n/a)</td><td>361.07 (n/a)</td><td>799.58 (n/a)</td><td>780.83 (n/a)</td><td>782.64 (n/a)</td><td>764.54 (n/a)</td><td>12.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.80 (-0.16%)</td><td>0.79 (+0.13%)</td><td>0.80 (-0.05%)</td><td>0.78 (+0.23%)</td><td>0.01 (-9.20%)</td><td>96938.00 (-0.23%)</td><td>95159.92 (-0.13%)</td><td>94868.30 (+0.05%)</td><td>94330.20 (+0.16%)</td><td>1072.55 (-9.32%)</td><td>728.50 (-0.16%)</td><td>722.22 (+0.13%)</td><td>724.37 (-0.05%)</td><td>708.90 (+0.23%)</td><td>8.06 (-9.20%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>97159.80 (n/a)</td><td>95288.48 (n/a)</td><td>94823.10 (n/a)</td><td>94178.50 (n/a)</td><td>1182.81 (n/a)</td><td>729.67 (n/a)</td><td>721.26 (n/a)</td><td>724.71 (n/a)</td><td>707.28 (n/a)</td><td>8.87 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.77 (-1.04%)</td><td>0.77 (-1.22%)</td><td>0.77 (-0.82%)</td><td>0.75 (-1.34%)</td><td>0.01 <b>(+38.60%)</b></td><td>100280.50 (+1.36%)</td><td>98662.86 (+1.24%)</td><td>98085.10 (+0.82%)</td><td>97434.80 (+1.05%)</td><td>1365.63 <b>(+41.87%)</b></td><td>705.29 (-1.04%)</td><td>696.61 (-1.22%)</td><td>700.61 (-0.82%)</td><td>685.27 (-1.34%)</td><td>9.60 <b>(+38.61%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>98936.10 (n/a)</td><td>97454.66 (n/a)</td><td>97285.00 (n/a)</td><td>96420.80 (n/a)</td><td>962.58 (n/a)</td><td>712.70 (n/a)</td><td>705.20 (n/a)</td><td>706.37 (n/a)</td><td>694.58 (n/a)</td><td>6.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.90 (-0.23%)</td><td>0.89 (+0.17%)</td><td>0.89 (+0.39%)</td><td>0.88 (+0.56%)</td><td>0.01 <b>(-25.68%)</b></td><td>85866.20 (-0.56%)</td><td>84745.84 (-0.18%)</td><td>84381.20 (-0.39%)</td><td>84323.90 (+0.23%)</td><td>655.91 <b>(-25.98%)</b></td><td>814.95 (-0.23%)</td><td>810.93 (+0.17%)</td><td>814.39 (+0.39%)</td><td>800.31 (+0.56%)</td><td>6.22 <b>(-25.68%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>86350.70 (n/a)</td><td>84895.06 (n/a)</td><td>84710.70 (n/a)</td><td>84126.80 (n/a)</td><td>886.08 (n/a)</td><td>816.86 (n/a)</td><td>809.53 (n/a)</td><td>811.23 (n/a)</td><td>795.82 (n/a)</td><td>8.37 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>5.65 <b>(+39.54%)</b></td><td>4.33 <b>(+37.86%)</b></td><td>4.76 <b>(+47.25%)</b></td><td>2.48 (+14.33%)</td><td>1.32 <b>(+41.43%)</b></td><td>3597.50 (-12.54%)</td><td>2258.92 <b>(-26.26%)</b></td><td>1870.80 <b>(-32.09%)</b></td><td>1576.60 <b>(-28.33%)</b></td><td>838.80 (-12.03%)</td><td>340.53 <b>(+39.54%)</b></td><td>260.73 <b>(+37.86%)</b></td><td>286.97 <b>(+47.25%)</b></td><td>149.23 (+14.33%)</td><td>79.37 <b>(+41.43%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>4.05 (n/a)</td><td>3.14 (n/a)</td><td>3.24 (n/a)</td><td>2.17 (n/a)</td><td>0.93 (n/a)</td><td>4113.10 (n/a)</td><td>3063.26 (n/a)</td><td>2754.70 (n/a)</td><td>2199.90 (n/a)</td><td>953.52 (n/a)</td><td>244.05 (n/a)</td><td>189.13 (n/a)</td><td>194.89 (n/a)</td><td>130.53 (n/a)</td><td>56.12 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.75 <b>(-41.40%)</b></td><td>2.29 <b>(-20.61%)</b></td><td>2.18 (+5.31%)</td><td>1.81 (-10.41%)</td><td>0.37 <b>(-69.67%)</b></td><td>4911.30 (+11.62%)</td><td>3968.10 (+13.93%)</td><td>4081.50 (-5.04%)</td><td>3245.70 <b>(+70.65%)</b></td><td>651.36 <b>(-45.81%)</b></td><td>165.41 <b>(-41.40%)</b></td><td>138.18 <b>(-20.61%)</b></td><td>131.54 (+5.31%)</td><td>109.31 (-10.41%)</td><td>22.12 <b>(-69.67%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>4.69 (n/a)</td><td>2.89 (n/a)</td><td>2.07 (n/a)</td><td>2.03 (n/a)</td><td>1.21 (n/a)</td><td>4400.00 (n/a)</td><td>3482.80 (n/a)</td><td>4298.10 (n/a)</td><td>1902.00 (n/a)</td><td>1202.05 (n/a)</td><td>282.27 (n/a)</td><td>174.05 (n/a)</td><td>124.91 (n/a)</td><td>122.02 (n/a)</td><td>72.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>5.41 <b>(+30.09%)</b></td><td>3.92 <b>(+30.40%)</b></td><td>3.65 <b>(+27.94%)</b></td><td>2.20 (+1.37%)</td><td>1.33 <b>(+49.94%)</b></td><td>4053.40 (-1.35%)</td><td>2526.68 <b>(-20.43%)</b></td><td>2443.00 <b>(-21.84%)</b></td><td>1646.30 <b>(-23.13%)</b></td><td>969.15 (+7.07%)</td><td>326.11 <b>(+30.09%)</b></td><td>236.15 <b>(+30.40%)</b></td><td>219.76 <b>(+27.94%)</b></td><td>132.45 (+1.37%)</td><td>80.08 <b>(+49.94%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>4.16 (n/a)</td><td>3.01 (n/a)</td><td>2.85 (n/a)</td><td>2.17 (n/a)</td><td>0.89 (n/a)</td><td>4109.00 (n/a)</td><td>3175.50 (n/a)</td><td>3125.60 (n/a)</td><td>2141.70 (n/a)</td><td>905.15 (n/a)</td><td>250.68 (n/a)</td><td>181.10 (n/a)</td><td>171.76 (n/a)</td><td>130.66 (n/a)</td><td>53.40 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>6.59 (+1.28%)</td><td>5.55 (+1.11%)</td><td>5.67 (+4.28%)</td><td>4.80 (-0.42%)</td><td>0.75 (+16.63%)</td><td>7262.00 (+0.42%)</td><td>6374.12 (-0.69%)</td><td>6148.50 (-4.11%)</td><td>5293.80 (-1.27%)</td><td>854.81 (+19.61%)</td><td>405.66 (+1.28%)</td><td>341.87 (+1.11%)</td><td>349.27 (+4.28%)</td><td>295.71 (-0.42%)</td><td>46.48 (+16.63%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>6.50 (n/a)</td><td>5.49 (n/a)</td><td>5.44 (n/a)</td><td>4.82 (n/a)</td><td>0.65 (n/a)</td><td>7231.90 (n/a)</td><td>6418.56 (n/a)</td><td>6411.80 (n/a)</td><td>5361.70 (n/a)</td><td>714.63 (n/a)</td><td>400.53 (n/a)</td><td>338.11 (n/a)</td><td>334.93 (n/a)</td><td>296.95 (n/a)</td><td>39.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>6.06 (+6.23%)</td><td>4.88 (+5.40%)</td><td>4.67 (+7.72%)</td><td>4.24 (+17.49%)</td><td>0.75 (-18.13%)</td><td>8222.20 (-14.89%)</td><td>7264.26 (-6.42%)</td><td>7473.70 (-7.16%)</td><td>5755.30 (-5.87%)</td><td>1030.24 <b>(-32.05%)</b></td><td>373.13 (+6.23%)</td><td>300.86 (+5.40%)</td><td>287.34 (+7.72%)</td><td>261.18 (+17.49%)</td><td>46.42 (-18.13%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>5.70 (n/a)</td><td>4.63 (n/a)</td><td>4.33 (n/a)</td><td>3.61 (n/a)</td><td>0.92 (n/a)</td><td>9660.40 (n/a)</td><td>7762.28 (n/a)</td><td>8050.50 (n/a)</td><td>6113.90 (n/a)</td><td>1516.13 (n/a)</td><td>351.24 (n/a)</td><td>285.46 (n/a)</td><td>266.75 (n/a)</td><td>222.30 (n/a)</td><td>56.70 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>7.11 (+4.26%)</td><td>6.38 (+16.73%)</td><td>6.39 (+12.33%)</td><td>5.56 <b>(+44.00%)</b></td><td>0.65 <b>(-43.83%)</b></td><td>6276.30 <b>(-30.56%)</b></td><td>5514.70 (-16.97%)</td><td>5452.80 (-10.98%)</td><td>4903.10 (-4.09%)</td><td>570.10 <b>(-63.21%)</b></td><td>437.98 (+4.26%)</td><td>392.71 (+16.73%)</td><td>393.83 (+12.33%)</td><td>342.16 <b>(+44.00%)</b></td><td>39.93 <b>(-43.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>6.82 (n/a)</td><td>5.46 (n/a)</td><td>5.69 (n/a)</td><td>3.86 (n/a)</td><td>1.15 (n/a)</td><td>9038.00 (n/a)</td><td>6641.94 (n/a)</td><td>6125.20 (n/a)</td><td>5112.10 (n/a)</td><td>1549.67 (n/a)</td><td>420.08 (n/a)</td><td>336.41 (n/a)</td><td>350.60 (n/a)</td><td>237.61 (n/a)</td><td>71.08 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.77 (-1.65%)</td><td>0.76 (+0.31%)</td><td>0.77 (+0.47%)</td><td>0.75 (+1.12%)</td><td>0.01 <b>(-62.29%)</b></td><td>100397.80 (-1.11%)</td><td>99024.94 (-0.34%)</td><td>98674.10 (-0.46%)</td><td>98543.20 (+1.68%)</td><td>775.53 <b>(-62.16%)</b></td><td>697.35 (-1.65%)</td><td>694.00 (+0.31%)</td><td>696.43 (+0.47%)</td><td>684.47 (+1.12%)</td><td>5.38 <b>(-62.29%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>101520.00 (n/a)</td><td>99364.84 (n/a)</td><td>99133.80 (n/a)</td><td>96915.40 (n/a)</td><td>2049.61 (n/a)</td><td>709.07 (n/a)</td><td>691.82 (n/a)</td><td>693.20 (n/a)</td><td>676.91 (n/a)</td><td>14.27 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.77 (-0.67%)</td><td>0.76 (-0.95%)</td><td>0.76 (-1.70%)</td><td>0.73 (-1.97%)</td><td>0.02 (+13.52%)</td><td>103657.50 (+2.00%)</td><td>99904.68 (+0.97%)</td><td>99550.20 (+1.73%)</td><td>98136.40 (+0.67%)</td><td>2200.62 (+17.17%)</td><td>700.24 (-0.67%)</td><td>688.11 (-0.95%)</td><td>690.30 (-1.70%)</td><td>662.95 (-1.97%)</td><td>14.82 (+13.52%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101620.20 (n/a)</td><td>98946.72 (n/a)</td><td>97858.10 (n/a)</td><td>97480.60 (n/a)</td><td>1878.07 (n/a)</td><td>704.96 (n/a)</td><td>694.71 (n/a)</td><td>702.24 (n/a)</td><td>676.24 (n/a)</td><td>13.06 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.90 (+0.14%)</td><td>0.90 (+1.19%)</td><td>0.90 (+0.39%)</td><td>0.89 (+4.34%)</td><td>0.00 <b>(-77.94%)</b></td><td>84768.60 (-4.16%)</td><td>84255.34 (-1.21%)</td><td>84100.60 (-0.39%)</td><td>83887.90 (-0.14%)</td><td>381.90 <b>(-78.96%)</b></td><td>819.18 (+0.14%)</td><td>815.62 (+1.19%)</td><td>817.11 (+0.39%)</td><td>810.67 (+4.34%)</td><td>3.69 <b>(-77.94%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.85 (n/a)</td><td>0.02 (n/a)</td><td>88451.20 (n/a)</td><td>85283.52 (n/a)</td><td>84431.90 (n/a)</td><td>84006.50 (n/a)</td><td>1814.82 (n/a)</td><td>818.03 (n/a)</td><td>806.06 (n/a)</td><td>813.90 (n/a)</td><td>776.92 (n/a)</td><td>16.73 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.68 (-14.14%)</td><td>3.22 <b>(+24.65%)</b></td><td>3.44 <b>(+40.88%)</b></td><td>2.01 <b>(+37.95%)</b></td><td>0.68 <b>(-34.30%)</b></td><td>4007.80 <b>(-27.51%)</b></td><td>2637.16 <b>(-24.94%)</b></td><td>2345.90 <b>(-29.02%)</b></td><td>2188.40 (+16.47%)</td><td>769.73 <b>(-41.09%)</b></td><td>965.96 (-14.14%)</td><td>843.30 <b>(+24.65%)</b></td><td>901.12 <b>(+40.88%)</b></td><td>527.45 <b>(+37.95%)</b></td><td>179.07 <b>(-34.30%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>4.29 (n/a)</td><td>2.58 (n/a)</td><td>2.44 (n/a)</td><td>1.46 (n/a)</td><td>1.04 (n/a)</td><td>5528.80 (n/a)</td><td>3513.34 (n/a)</td><td>3305.00 (n/a)</td><td>1879.00 (n/a)</td><td>1306.53 (n/a)</td><td>1125.01 (n/a)</td><td>676.52 (n/a)</td><td>639.62 (n/a)</td><td>382.35 (n/a)</td><td>272.55 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.31 (+12.04%)</td><td>0.23 (-5.57%)</td><td>0.21 (-16.08%)</td><td>0.15 (-16.39%)</td><td>0.06 <b>(+51.24%)</b></td><td>8386.50 (+19.60%)</td><td>5866.36 (+9.77%)</td><td>5868.00 (+19.17%)</td><td>4070.30 (-10.75%)</td><td>1672.84 <b>(+62.11%)</b></td><td>16.49 (+12.04%)</td><td>12.17 (-5.57%)</td><td>11.44 (-16.08%)</td><td>8.00 (-16.39%)</td><td>3.30 <b>(+51.24%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>7011.90 (n/a)</td><td>5344.42 (n/a)</td><td>4924.20 (n/a)</td><td>4560.50 (n/a)</td><td>1031.90 (n/a)</td><td>14.72 (n/a)</td><td>12.89 (n/a)</td><td>13.63 (n/a)</td><td>9.57 (n/a)</td><td>2.19 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.67 (n/a)</td><td>3.55 (n/a)</td><td>3.53 (n/a)</td><td>3.47 (n/a)</td><td>0.07 (n/a)</td><td>3.66 (n/a)</td><td>3.55 (n/a)</td><td>3.53 (n/a)</td><td>3.47 (n/a)</td><td>0.07 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>7.49 (+8.95%)</td><td>6.92 (+9.33%)</td><td>6.96 (+6.25%)</td><td>6.26 (+9.79%)</td><td>0.47 (-17.81%)</td><td>7.49 (+8.95%)</td><td>6.91 (+9.33%)</td><td>6.96 (+6.25%)</td><td>6.25 (+9.79%)</td><td>0.47 (-17.81%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>6.88 (n/a)</td><td>6.33 (n/a)</td><td>6.55 (n/a)</td><td>5.70 (n/a)</td><td>0.57 (n/a)</td><td>6.87 (n/a)</td><td>6.32 (n/a)</td><td>6.55 (n/a)</td><td>5.69 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>13.63 (+1.08%)</td><td>9.89 (+5.72%)</td><td>9.49 (+11.45%)</td><td>8.04 (+9.01%)</td><td>2.25 (-6.42%)</td><td>13.63 (+1.08%)</td><td>9.88 (+5.72%)</td><td>9.48 (+11.45%)</td><td>8.04 (+9.01%)</td><td>2.25 (-6.42%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>13.49 (n/a)</td><td>9.35 (n/a)</td><td>8.51 (n/a)</td><td>7.38 (n/a)</td><td>2.40 (n/a)</td><td>13.48 (n/a)</td><td>9.34 (n/a)</td><td>8.51 (n/a)</td><td>7.37 (n/a)</td><td>2.40 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.92 (n/a)</td><td>3.64 (n/a)</td><td>3.59 (n/a)</td><td>3.35 (n/a)</td><td>0.25 (n/a)</td><td>3.92 (n/a)</td><td>3.63 (n/a)</td><td>3.59 (n/a)</td><td>3.34 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>7.03 (-5.04%)</td><td>6.57 (-1.02%)</td><td>6.79 (+4.67%)</td><td>5.72 (-5.52%)</td><td>0.53 (+3.89%)</td><td>7.02 (-5.04%)</td><td>6.56 (-1.02%)</td><td>6.78 (+4.67%)</td><td>5.72 (-5.52%)</td><td>0.53 (+3.89%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>7.40 (n/a)</td><td>6.64 (n/a)</td><td>6.48 (n/a)</td><td>6.06 (n/a)</td><td>0.51 (n/a)</td><td>7.40 (n/a)</td><td>6.63 (n/a)</td><td>6.48 (n/a)</td><td>6.05 (n/a)</td><td>0.51 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>13.82 (-0.44%)</td><td>10.48 (+4.49%)</td><td>9.94 (+1.51%)</td><td>7.76 (-5.44%)</td><td>2.54 (+9.49%)</td><td>13.81 (-0.44%)</td><td>10.47 (+4.49%)</td><td>9.94 (+1.51%)</td><td>7.75 (-5.44%)</td><td>2.54 (+9.49%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>13.88 (n/a)</td><td>10.03 (n/a)</td><td>9.80 (n/a)</td><td>8.21 (n/a)</td><td>2.32 (n/a)</td><td>13.87 (n/a)</td><td>10.02 (n/a)</td><td>9.79 (n/a)</td><td>8.20 (n/a)</td><td>2.32 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.12 <b>(+22.72%)</b></td><td>1.87 <b>(+37.37%)</b></td><td>1.19 (+15.64%)</td><td>1.03 (+1.38%)</td><td>1.07 <b>(+60.48%)</b></td><td>3.12 <b>(+22.72%)</b></td><td>1.86 <b>(+37.37%)</b></td><td>1.19 (+15.64%)</td><td>1.03 (+1.38%)</td><td>1.07 <b>(+60.48%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.54 (n/a)</td><td>1.36 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>0.67 (n/a)</td><td>2.54 (n/a)</td><td>1.36 (n/a)</td><td>1.03 (n/a)</td><td>1.02 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.56 (-3.64%)</td><td>0.39 <b>(+53.36%)</b></td><td>0.51 <b>(+353.00%)</b></td><td>0.08 (+0.91%)</td><td>0.21 (-11.66%)</td><td>0.55 (-3.64%)</td><td>0.38 <b>(+53.36%)</b></td><td>0.50 <b>(+353.00%)</b></td><td>0.07 (+0.91%)</td><td>0.20 (-11.66%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.58 (n/a)</td><td>0.25 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.23 (n/a)</td><td>0.57 (n/a)</td><td>0.25 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.84 (+14.30%)</td><td>0.53 (-6.58%)</td><td>0.63 (-0.28%)</td><td>0.08 <b>(-77.23%)</b></td><td>0.29 <b>(+84.93%)</b></td><td>0.83 (+14.30%)</td><td>0.52 (-6.58%)</td><td>0.63 (-0.28%)</td><td>0.08 <b>(-77.23%)</b></td><td>0.29 <b>(+84.93%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.74 (n/a)</td><td>0.56 (n/a)</td><td>0.64 (n/a)</td><td>0.34 (n/a)</td><td>0.16 (n/a)</td><td>0.73 (n/a)</td><td>0.56 (n/a)</td><td>0.63 (n/a)</td><td>0.34 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.62 (+4.98%)</td><td>2.16 <b>(+21.43%)</b></td><td>2.32 <b>(+23.19%)</b></td><td>1.69 <b>(+293.16%)</b></td><td>0.39 <b>(-54.03%)</b></td><td>2.58 (+4.98%)</td><td>2.13 <b>(+21.43%)</b></td><td>2.28 <b>(+23.19%)</b></td><td>1.66 <b>(+293.16%)</b></td><td>0.38 <b>(-54.03%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.50 (n/a)</td><td>1.78 (n/a)</td><td>1.88 (n/a)</td><td>0.43 (n/a)</td><td>0.84 (n/a)</td><td>2.46 (n/a)</td><td>1.75 (n/a)</td><td>1.85 (n/a)</td><td>0.42 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>575.40 (n/a)</td><td>366.26 (n/a)</td><td>268.60 (n/a)</td><td>242.00 (n/a)</td><td>157.11 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1006.60 (n/a)</td><td>504.18 (n/a)</td><td>422.50 (n/a)</td><td>247.10 (n/a)</td><td>299.10 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>564.00 (n/a)</td><td>369.04 (n/a)</td><td>360.30 (n/a)</td><td>222.30 (n/a)</td><td>125.36 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.00 (n/a)</td><td>425.42 (n/a)</td><td>530.20 (n/a)</td><td>252.70 (n/a)</td><td>155.84 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>604.60 (n/a)</td><td>441.88 (n/a)</td><td>494.30 (n/a)</td><td>254.70 (n/a)</td><td>167.99 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>499.00 (n/a)</td><td>397.90 (n/a)</td><td>462.00 (n/a)</td><td>255.70 (n/a)</td><td>108.16 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>464.50 (n/a)</td><td>324.16 (n/a)</td><td>283.90 (n/a)</td><td>248.20 (n/a)</td><td>94.10 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>661.80 (n/a)</td><td>435.74 (n/a)</td><td>337.40 (n/a)</td><td>290.90 (n/a)</td><td>179.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>494.70 (n/a)</td><td>384.28 (n/a)</td><td>395.20 (n/a)</td><td>225.30 (n/a)</td><td>116.76 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.30 (n/a)</td><td>422.72 (n/a)</td><td>499.40 (n/a)</td><td>234.90 (n/a)</td><td>142.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>454.80 (n/a)</td><td>391.70 (n/a)</td><td>420.40 (n/a)</td><td>283.90 (n/a)</td><td>74.63 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>676.40 (n/a)</td><td>572.60 (n/a)</td><td>591.10 (n/a)</td><td>359.30 (n/a)</td><td>128.06 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>666.10 (n/a)</td><td>429.88 (n/a)</td><td>305.80 (n/a)</td><td>287.80 (n/a)</td><td>187.07 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>629.50 (n/a)</td><td>429.80 (n/a)</td><td>452.20 (n/a)</td><td>220.60 (n/a)</td><td>166.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1024.80 (n/a)</td><td>475.16 (n/a)</td><td>306.40 (n/a)</td><td>249.90 (n/a)</td><td>321.35 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>581.70 (n/a)</td><td>374.68 (n/a)</td><td>334.00 (n/a)</td><td>251.90 (n/a)</td><td>133.27 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1033.20 (n/a)</td><td>548.40 (n/a)</td><td>471.20 (n/a)</td><td>242.50 (n/a)</td><td>293.83 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>537.30 (n/a)</td><td>391.54 (n/a)</td><td>360.20 (n/a)</td><td>252.40 (n/a)</td><td>112.92 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>418.90 (n/a)</td><td>322.28 (n/a)</td><td>322.30 (n/a)</td><td>264.50 (n/a)</td><td>60.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>521.80 (n/a)</td><td>400.70 (n/a)</td><td>459.30 (n/a)</td><td>260.90 (n/a)</td><td>119.99 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>594.20 (n/a)</td><td>372.90 (n/a)</td><td>257.20 (n/a)</td><td>245.50 (n/a)</td><td>167.65 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>544.70 (n/a)</td><td>396.58 (n/a)</td><td>444.40 (n/a)</td><td>247.70 (n/a)</td><td>123.92 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>434.90 (n/a)</td><td>316.00 (n/a)</td><td>304.80 (n/a)</td><td>231.60 (n/a)</td><td>75.28 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>563.70 (n/a)</td><td>437.94 (n/a)</td><td>499.10 (n/a)</td><td>219.30 (n/a)</td><td>147.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (+18.18%)</td><td>0.01 <b>(+45.06%)</b></td><td>0.01 <b>(+75.31%)</b></td><td>0.01 <b>(+34.57%)</b></td><td>0.00 (-3.71%)</td><td>439.40 <b>(-25.68%)</b></td><td>304.18 <b>(-32.84%)</b></td><td>288.90 <b>(-42.95%)</b></td><td>242.40 (-15.36%)</td><td>78.56 <b>(-36.49%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.20 (n/a)</td><td>452.94 (n/a)</td><td>506.40 (n/a)</td><td>286.40 (n/a)</td><td>123.69 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (-2.91%)</td><td>0.01 (-14.49%)</td><td>0.01 <b>(-28.02%)</b></td><td>0.01 <b>(-24.12%)</b></td><td>0.01 <b>(+34.86%)</b></td><td>609.40 <b>(+31.79%)</b></td><td>405.24 <b>(+28.44%)</b></td><td>427.50 <b>(+38.93%)</b></td><td>207.70 (+3.03%)</td><td>168.73 <b>(+80.37%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>462.40 (n/a)</td><td>315.50 (n/a)</td><td>307.70 (n/a)</td><td>201.60 (n/a)</td><td>93.55 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 <b>(+30.53%)</b></td><td>0.01 <b>(+27.07%)</b></td><td>0.01 <b>(+45.23%)</b></td><td>0.00 <b>(-33.11%)</b></td><td>0.01 <b>(+57.21%)</b></td><td>934.30 <b>(+49.49%)</b></td><td>418.28 (-7.91%)</td><td>315.80 <b>(-31.14%)</b></td><td>224.70 <b>(-23.39%)</b></td><td>292.00 <b>(+101.29%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>625.00 (n/a)</td><td>454.22 (n/a)</td><td>458.60 (n/a)</td><td>293.30 (n/a)</td><td>145.06 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (-1.45%)</td><td>0.01 (-13.19%)</td><td>0.01 <b>(-27.25%)</b></td><td>0.01 (-6.08%)</td><td>0.00 (+5.62%)</td><td>532.50 (+6.48%)</td><td>429.72 (+16.70%)</td><td>485.40 <b>(+37.47%)</b></td><td>213.20 (+1.48%)</td><td>126.54 (+5.49%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>500.10 (n/a)</td><td>368.22 (n/a)</td><td>353.10 (n/a)</td><td>210.10 (n/a)</td><td>119.95 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (+1.71%)</td><td>0.01 (-15.52%)</td><td>0.01 (-15.88%)</td><td>0.00 <b>(-76.74%)</b></td><td>0.01 <b>(+61.25%)</b></td><td>2112.70 <b>(+329.85%)</b></td><td>739.26 <b>(+94.51%)</b></td><td>503.90 (+18.90%)</td><td>248.60 (-1.66%)</td><td>780.67 <b>(+596.30%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.50 (n/a)</td><td>380.06 (n/a)</td><td>423.80 (n/a)</td><td>252.80 (n/a)</td><td>112.12 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 <b>(+23.51%)</b></td><td>0.01 (+5.29%)</td><td>0.01 (-2.39%)</td><td>0.01 (+7.77%)</td><td>0.00 <b>(+28.70%)</b></td><td>480.30 (-7.21%)</td><td>391.56 (-4.32%)</td><td>418.00 (+2.45%)</td><td>256.10 (-19.03%)</td><td>83.35 (-6.41%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>517.60 (n/a)</td><td>409.26 (n/a)</td><td>408.00 (n/a)</td><td>316.30 (n/a)</td><td>89.07 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (+10.15%)</td><td>0.03 (+19.69%)</td><td>0.03 (+16.19%)</td><td>0.02 (+14.71%)</td><td>0.01 (-6.45%)</td><td>462.10 (-12.83%)</td><td>283.28 (-19.75%)</td><td>247.10 (-13.93%)</td><td>194.90 (-9.22%)</td><td>106.47 <b>(-26.58%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.10 (n/a)</td><td>353.00 (n/a)</td><td>287.10 (n/a)</td><td>214.70 (n/a)</td><td>145.02 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-15.65%)</td><td>0.02 (-0.88%)</td><td>0.02 (+7.69%)</td><td>0.02 (+1.28%)</td><td>0.00 <b>(-28.65%)</b></td><td>500.60 (-1.26%)</td><td>383.30 (-1.20%)</td><td>372.40 (-7.13%)</td><td>304.50 (+18.53%)</td><td>80.08 (-15.84%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>507.00 (n/a)</td><td>387.96 (n/a)</td><td>401.00 (n/a)</td><td>256.90 (n/a)</td><td>95.15 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 <b>(+64.41%)</b></td><td>0.03 <b>(+61.03%)</b></td><td>0.02 <b>(+35.68%)</b></td><td>0.02 <b>(+311.29%)</b></td><td>0.01 (+9.51%)</td><td>508.90 <b>(-75.68%)</b></td><td>340.94 <b>(-55.35%)</b></td><td>331.90 <b>(-26.29%)</b></td><td>225.20 <b>(-39.17%)</b></td><td>108.37 <b>(-85.43%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2092.90 (n/a)</td><td>763.56 (n/a)</td><td>450.30 (n/a)</td><td>370.20 (n/a)</td><td>743.98 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 <b>(+20.28%)</b></td><td>0.03 (+19.06%)</td><td>0.02 (-5.98%)</td><td>0.01 <b>(+325.51%)</b></td><td>0.01 (-19.65%)</td><td>568.50 <b>(-76.50%)</b></td><td>364.10 <b>(-51.57%)</b></td><td>327.70 (+6.36%)</td><td>230.30 (-16.86%)</td><td>139.39 <b>(-85.09%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2419.10 (n/a)</td><td>751.74 (n/a)</td><td>308.10 (n/a)</td><td>277.00 (n/a)</td><td>935.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 <b>(+48.06%)</b></td><td>0.03 <b>(+22.79%)</b></td><td>0.03 (+11.71%)</td><td>0.01 <b>(+20.69%)</b></td><td>0.01 <b>(+72.36%)</b></td><td>549.50 (-17.14%)</td><td>345.72 (-12.56%)</td><td>299.20 (-10.47%)</td><td>161.40 <b>(-32.44%)</b></td><td>160.82 (-3.34%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>663.20 (n/a)</td><td>395.38 (n/a)</td><td>334.20 (n/a)</td><td>238.90 (n/a)</td><td>166.39 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-1.46%)</td><td>0.02 (-11.21%)</td><td>0.02 <b>(-39.22%)</b></td><td>0.01 (+1.51%)</td><td>0.01 (+13.39%)</td><td>594.40 (-1.49%)</td><td>438.58 (+15.64%)</td><td>526.00 <b>(+64.53%)</b></td><td>248.30 (+1.51%)</td><td>157.91 (+10.21%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>603.40 (n/a)</td><td>379.26 (n/a)</td><td>319.70 (n/a)</td><td>244.60 (n/a)</td><td>143.28 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 <b>(+69.46%)</b></td><td>0.03 <b>(+85.01%)</b></td><td>0.02 <b>(+71.27%)</b></td><td>0.02 <b>(+269.32%)</b></td><td>0.01 <b>(+52.05%)</b></td><td>508.60 <b>(-72.92%)</b></td><td>349.46 <b>(-55.44%)</b></td><td>338.00 <b>(-41.62%)</b></td><td>188.80 <b>(-40.98%)</b></td><td>137.41 <b>(-77.89%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1878.20 (n/a)</td><td>784.26 (n/a)</td><td>579.00 (n/a)</td><td>319.90 (n/a)</td><td>621.41 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (+7.32%)</td><td>0.02 (+15.76%)</td><td>0.02 <b>(+29.35%)</b></td><td>0.02 <b>(+38.70%)</b></td><td>0.01 <b>(-21.49%)</b></td><td>458.80 <b>(-27.90%)</b></td><td>356.50 (-19.23%)</td><td>366.10 <b>(-22.68%)</b></td><td>239.90 (-6.83%)</td><td>86.40 <b>(-46.21%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>636.30 (n/a)</td><td>441.38 (n/a)</td><td>473.50 (n/a)</td><td>257.50 (n/a)</td><td>160.62 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (+18.01%)</td><td>0.05 (+16.71%)</td><td>0.04 <b>(+29.33%)</b></td><td>0.03 (+9.29%)</td><td>0.02 (+17.00%)</td><td>491.00 (-8.50%)</td><td>361.16 (-14.05%)</td><td>393.40 <b>(-22.68%)</b></td><td>208.30 (-15.29%)</td><td>127.39 (-11.22%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>536.60 (n/a)</td><td>420.22 (n/a)</td><td>508.80 (n/a)</td><td>245.90 (n/a)</td><td>143.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 <b>(+33.55%)</b></td><td>0.05 <b>(+41.28%)</b></td><td>0.05 <b>(+65.04%)</b></td><td>0.03 (+10.23%)</td><td>0.02 <b>(+68.27%)</b></td><td>605.70 (-9.29%)</td><td>375.18 <b>(-23.81%)</b></td><td>302.60 <b>(-39.41%)</b></td><td>219.00 <b>(-25.13%)</b></td><td>164.99 <b>(+23.86%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>667.70 (n/a)</td><td>492.40 (n/a)</td><td>499.40 (n/a)</td><td>292.50 (n/a)</td><td>133.21 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (-17.46%)</td><td>0.03 <b>(-37.23%)</b></td><td>0.03 <b>(-38.70%)</b></td><td>0.01 <b>(-80.43%)</b></td><td>0.02 <b>(+21.32%)</b></td><td>2425.90 <b>(+410.93%)</b></td><td>840.46 <b>(+151.15%)</b></td><td>482.60 <b>(+63.15%)</b></td><td>284.60 <b>(+21.16%)</b></td><td>893.46 <b>(+757.02%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>474.80 (n/a)</td><td>334.64 (n/a)</td><td>295.80 (n/a)</td><td>234.90 (n/a)</td><td>104.25 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 <b>(-28.07%)</b></td><td>0.04 <b>(-21.70%)</b></td><td>0.04 (-16.71%)</td><td>0.02 <b>(-25.28%)</b></td><td>0.01 <b>(-37.98%)</b></td><td>721.20 <b>(+33.83%)</b></td><td>492.86 <b>(+24.71%)</b></td><td>441.90 <b>(+20.05%)</b></td><td>378.70 <b>(+39.02%)</b></td><td>142.73 (+13.48%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>538.90 (n/a)</td><td>395.22 (n/a)</td><td>368.10 (n/a)</td><td>272.40 (n/a)</td><td>125.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (-4.69%)</td><td>0.05 (-16.12%)</td><td>0.04 <b>(-33.98%)</b></td><td>0.02 (-17.76%)</td><td>0.02 (-5.93%)</td><td>662.50 <b>(+21.58%)</b></td><td>415.36 <b>(+20.38%)</b></td><td>379.80 <b>(+51.50%)</b></td><td>222.60 (+4.90%)</td><td>180.32 (+17.77%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>544.90 (n/a)</td><td>345.04 (n/a)</td><td>250.70 (n/a)</td><td>212.20 (n/a)</td><td>153.11 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (-4.72%)</td><td>0.04 (-5.42%)</td><td>0.04 (+6.33%)</td><td>0.02 <b>(-24.45%)</b></td><td>0.01 (+17.80%)</td><td>667.90 <b>(+32.36%)</b></td><td>438.30 (+9.73%)</td><td>377.70 (-5.95%)</td><td>303.50 (+4.94%)</td><td>147.04 <b>(+65.59%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>504.60 (n/a)</td><td>399.44 (n/a)</td><td>401.60 (n/a)</td><td>289.20 (n/a)</td><td>88.80 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.20 <b>(+47.71%)</b></td><td>0.14 <b>(+27.66%)</b></td><td>0.12 <b>(+20.11%)</b></td><td>0.11 <b>(+60.49%)</b></td><td>0.04 <b>(+37.49%)</b></td><td>297.50 <b>(-37.70%)</b></td><td>254.88 <b>(-22.60%)</b></td><td>279.90 (-16.72%)</td><td>161.00 <b>(-32.30%)</b></td><td>54.98 <b>(-42.61%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>477.50 (n/a)</td><td>329.30 (n/a)</td><td>336.10 (n/a)</td><td>237.80 (n/a)</td><td>95.80 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 (+9.03%)</td><td>0.11 <b>(+29.49%)</b></td><td>0.11 <b>(+52.36%)</b></td><td>0.07 (+5.59%)</td><td>0.03 <b>(+26.72%)</b></td><td>498.90 (-5.30%)</td><td>328.20 <b>(-20.77%)</b></td><td>287.60 <b>(-34.35%)</b></td><td>231.20 (-8.29%)</td><td>114.86 (+12.36%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>526.80 (n/a)</td><td>414.22 (n/a)</td><td>438.10 (n/a)</td><td>252.10 (n/a)</td><td>102.22 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 <b>(+43.47%)</b></td><td>0.10 <b>(+89.45%)</b></td><td>0.09 <b>(+78.08%)</b></td><td>0.06 <b>(+254.03%)</b></td><td>0.03 (-5.01%)</td><td>552.60 <b>(-71.75%)</b></td><td>376.32 <b>(-64.46%)</b></td><td>362.40 <b>(-43.84%)</b></td><td>241.60 <b>(-30.29%)</b></td><td>130.57 <b>(-83.73%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1956.20 (n/a)</td><td>1058.90 (n/a)</td><td>645.30 (n/a)</td><td>346.60 (n/a)</td><td>802.47 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 <b>(-25.41%)</b></td><td>0.07 <b>(-26.04%)</b></td><td>0.06 <b>(-40.28%)</b></td><td>0.06 (-2.21%)</td><td>0.02 <b>(-47.93%)</b></td><td>565.10 (+2.26%)</td><td>469.74 <b>(+26.40%)</b></td><td>506.50 <b>(+67.44%)</b></td><td>321.40 <b>(+34.08%)</b></td><td>92.92 <b>(-33.04%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>552.60 (n/a)</td><td>371.64 (n/a)</td><td>302.50 (n/a)</td><td>239.70 (n/a)</td><td>138.76 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (+12.46%)</td><td>0.09 (+15.66%)</td><td>0.09 <b>(+22.49%)</b></td><td>0.06 (-9.91%)</td><td>0.03 <b>(+33.92%)</b></td><td>595.30 (+11.00%)</td><td>386.34 (-10.31%)</td><td>371.20 (-18.36%)</td><td>253.40 (-11.09%)</td><td>130.54 <b>(+40.73%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>536.30 (n/a)</td><td>430.74 (n/a)</td><td>454.70 (n/a)</td><td>285.00 (n/a)</td><td>92.76 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (-15.20%)</td><td>0.01 <b>(-26.94%)</b></td><td>0.01 <b>(-33.44%)</b></td><td>0.01 <b>(-20.59%)</b></td><td>0.00 (-16.27%)</td><td>641.70 <b>(+25.95%)</b></td><td>400.40 <b>(+37.19%)</b></td><td>345.00 <b>(+50.26%)</b></td><td>255.30 (+17.92%)</td><td>154.75 <b>(+24.31%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.50 (n/a)</td><td>291.86 (n/a)</td><td>229.60 (n/a)</td><td>216.50 (n/a)</td><td>124.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (-7.71%)</td><td>0.01 (-4.68%)</td><td>0.02 (-5.27%)</td><td>0.01 (+3.80%)</td><td>0.00 (-15.98%)</td><td>481.80 (-3.66%)</td><td>313.42 (+2.81%)</td><td>269.10 (+5.57%)</td><td>256.90 (+8.35%)</td><td>95.71 (-13.61%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>500.10 (n/a)</td><td>304.84 (n/a)</td><td>254.90 (n/a)</td><td>237.10 (n/a)</td><td>110.79 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 <b>(+44.02%)</b></td><td>0.01 <b>(+21.07%)</b></td><td>0.01 <b>(+27.57%)</b></td><td>0.01 (-19.50%)</td><td>0.01 <b>(+111.46%)</b></td><td>611.80 <b>(+24.22%)</b></td><td>353.96 (-5.31%)</td><td>306.60 <b>(-21.61%)</b></td><td>170.90 <b>(-30.58%)</b></td><td>172.81 <b>(+89.34%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>492.50 (n/a)</td><td>373.82 (n/a)</td><td>391.10 (n/a)</td><td>246.20 (n/a)</td><td>91.27 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (+4.65%)</td><td>0.01 (+2.43%)</td><td>0.02 (+1.49%)</td><td>0.01 (+14.46%)</td><td>0.00 (-13.89%)</td><td>491.80 (-12.63%)</td><td>321.40 (-5.98%)</td><td>271.60 (-1.45%)</td><td>223.80 (-4.44%)</td><td>105.75 <b>(-24.31%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.90 (n/a)</td><td>341.84 (n/a)</td><td>275.60 (n/a)</td><td>234.20 (n/a)</td><td>139.71 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (+8.22%)</td><td>0.01 <b>(+27.37%)</b></td><td>0.01 <b>(+42.77%)</b></td><td>0.01 <b>(+32.64%)</b></td><td>0.00 (+10.67%)</td><td>413.40 <b>(-24.60%)</b></td><td>315.88 <b>(-21.96%)</b></td><td>299.20 <b>(-29.96%)</b></td><td>225.00 (-7.60%)</td><td>92.16 (-19.00%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.30 (n/a)</td><td>404.76 (n/a)</td><td>427.20 (n/a)</td><td>243.50 (n/a)</td><td>113.79 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (-8.17%)</td><td>0.01 (+2.63%)</td><td>0.01 (-10.53%)</td><td>0.01 (+19.27%)</td><td>0.00 (-3.43%)</td><td>506.70 (-16.16%)</td><td>397.72 (-3.83%)</td><td>468.70 (+11.78%)</td><td>265.80 (+8.93%)</td><td>121.07 (-13.86%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>604.40 (n/a)</td><td>413.58 (n/a)</td><td>419.30 (n/a)</td><td>244.00 (n/a)</td><td>140.55 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (+12.77%)</td><td>0.01 (+18.25%)</td><td>0.02 <b>(+91.98%)</b></td><td>0.01 <b>(-34.86%)</b></td><td>0.01 <b>(+54.85%)</b></td><td>813.40 <b>(+53.50%)</b></td><td>427.62 (+5.36%)</td><td>242.10 <b>(-47.91%)</b></td><td>199.60 (-11.33%)</td><td>289.89 <b>(+102.30%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>529.90 (n/a)</td><td>405.88 (n/a)</td><td>464.80 (n/a)</td><td>225.10 (n/a)</td><td>143.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (-11.68%)</td><td>0.01 (-19.64%)</td><td>0.01 <b>(-31.35%)</b></td><td>0.01 (-7.63%)</td><td>0.00 (-7.36%)</td><td>640.10 (+8.25%)</td><td>470.74 <b>(+24.95%)</b></td><td>476.30 <b>(+45.66%)</b></td><td>283.00 (+13.25%)</td><td>150.51 (+12.10%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.30 (n/a)</td><td>376.74 (n/a)</td><td>327.00 (n/a)</td><td>249.90 (n/a)</td><td>134.26 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (+9.30%)</td><td>0.01 (+16.89%)</td><td>0.01 <b>(+21.38%)</b></td><td>0.01 <b>(+26.58%)</b></td><td>0.00 (-5.68%)</td><td>456.60 <b>(-21.00%)</b></td><td>362.52 (-15.82%)</td><td>356.80 (-17.62%)</td><td>278.00 (-8.52%)</td><td>71.61 <b>(-31.38%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.00 (n/a)</td><td>430.66 (n/a)</td><td>433.10 (n/a)</td><td>303.90 (n/a)</td><td>104.34 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 <b>(+95.00%)</b></td><td>0.01 <b>(+65.64%)</b></td><td>0.01 <b>(+43.07%)</b></td><td>0.01 <b>(+298.50%)</b></td><td>0.01 <b>(+63.98%)</b></td><td>481.90 <b>(-74.90%)</b></td><td>340.08 <b>(-53.10%)</b></td><td>313.20 <b>(-30.10%)</b></td><td>168.10 <b>(-48.72%)</b></td><td>124.56 <b>(-81.46%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1920.30 (n/a)</td><td>725.14 (n/a)</td><td>448.10 (n/a)</td><td>327.80 (n/a)</td><td>671.79 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 <b>(-32.81%)</b></td><td>0.01 (-12.14%)</td><td>0.01 (-4.47%)</td><td>0.01 (+11.77%)</td><td>0.00 <b>(-47.81%)</b></td><td>587.20 (-10.53%)</td><td>470.98 (+3.98%)</td><td>535.60 (+4.69%)</td><td>311.50 <b>(+48.83%)</b></td><td>125.60 <b>(-26.35%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>656.30 (n/a)</td><td>452.94 (n/a)</td><td>511.60 (n/a)</td><td>209.30 (n/a)</td><td>170.53 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (+16.98%)</td><td>0.01 <b>(+30.98%)</b></td><td>0.01 <b>(+40.75%)</b></td><td>0.01 <b>(+48.02%)</b></td><td>0.00 (+8.05%)</td><td>558.00 <b>(-32.44%)</b></td><td>412.46 <b>(-26.13%)</b></td><td>432.00 <b>(-28.95%)</b></td><td>243.20 (-14.52%)</td><td>132.63 <b>(-34.43%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>825.90 (n/a)</td><td>558.36 (n/a)</td><td>608.00 (n/a)</td><td>284.50 (n/a)</td><td>202.27 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-7.73%)</td><td>0.03 (-7.56%)</td><td>0.03 (-3.83%)</td><td>0.01 (-4.91%)</td><td>0.01 (-9.21%)</td><td>658.30 (+5.16%)</td><td>359.74 (+7.33%)</td><td>278.40 (+3.96%)</td><td>268.90 (+8.38%)</td><td>167.93 (+2.90%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>626.00 (n/a)</td><td>335.16 (n/a)</td><td>267.80 (n/a)</td><td>248.10 (n/a)</td><td>163.20 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-14.55%)</td><td>0.02 (-12.31%)</td><td>0.03 (-9.77%)</td><td>0.01 <b>(-22.55%)</b></td><td>0.01 (-13.09%)</td><td>666.40 <b>(+29.12%)</b></td><td>384.96 (+15.53%)</td><td>288.40 (+10.84%)</td><td>255.60 (+17.03%)</td><td>171.15 <b>(+30.98%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.10 (n/a)</td><td>333.20 (n/a)</td><td>260.20 (n/a)</td><td>218.40 (n/a)</td><td>130.67 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (-8.22%)</td><td>0.02 (-10.57%)</td><td>0.02 (-17.96%)</td><td>0.01 <b>(-22.63%)</b></td><td>0.01 (+14.38%)</td><td>590.30 <b>(+29.25%)</b></td><td>418.36 (+19.87%)</td><td>423.90 <b>(+21.88%)</b></td><td>223.10 (+8.94%)</td><td>166.77 <b>(+71.12%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>456.70 (n/a)</td><td>349.02 (n/a)</td><td>347.80 (n/a)</td><td>204.80 (n/a)</td><td>97.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-6.21%)</td><td>0.02 <b>(-26.33%)</b></td><td>0.02 <b>(-39.89%)</b></td><td>0.01 <b>(-43.82%)</b></td><td>0.01 <b>(+53.55%)</b></td><td>649.10 <b>(+77.98%)</b></td><td>398.96 <b>(+47.78%)</b></td><td>406.10 <b>(+66.37%)</b></td><td>241.30 (+6.63%)</td><td>157.39 <b>(+183.92%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>364.70 (n/a)</td><td>269.96 (n/a)</td><td>244.10 (n/a)</td><td>226.30 (n/a)</td><td>55.43 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-19.92%)</td><td>0.02 (-11.62%)</td><td>0.02 (+11.38%)</td><td>0.01 (-5.43%)</td><td>0.01 <b>(-43.64%)</b></td><td>599.30 (+5.75%)</td><td>418.98 (+4.55%)</td><td>417.30 (-10.22%)</td><td>284.20 <b>(+24.87%)</b></td><td>120.23 <b>(-22.27%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.70 (n/a)</td><td>400.74 (n/a)</td><td>464.80 (n/a)</td><td>227.60 (n/a)</td><td>154.68 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-7.24%)</td><td>0.03 (-12.53%)</td><td>0.03 (-5.61%)</td><td>0.02 (-2.64%)</td><td>0.01 (+6.18%)</td><td>456.40 (+2.72%)</td><td>343.56 (+15.92%)</td><td>286.90 (+5.95%)</td><td>247.00 (+7.81%)</td><td>101.41 (+18.51%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>444.30 (n/a)</td><td>296.38 (n/a)</td><td>270.80 (n/a)</td><td>229.10 (n/a)</td><td>85.57 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-15.63%)</td><td>0.02 <b>(-20.75%)</b></td><td>0.02 <b>(-48.63%)</b></td><td>0.01 <b>(+242.59%)</b></td><td>0.01 <b>(-54.91%)</b></td><td>564.60 <b>(-70.81%)</b></td><td>487.06 <b>(-26.47%)</b></td><td>531.70 <b>(+94.69%)</b></td><td>289.70 (+18.54%)</td><td>112.50 <b>(-84.51%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1934.20 (n/a)</td><td>662.44 (n/a)</td><td>273.10 (n/a)</td><td>244.40 (n/a)</td><td>726.22 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-12.67%)</td><td>0.02 (-12.47%)</td><td>0.02 (-12.42%)</td><td>0.01 <b>(-25.12%)</b></td><td>0.01 (+9.35%)</td><td>568.90 <b>(+33.54%)</b></td><td>398.94 (+19.39%)</td><td>371.60 (+14.20%)</td><td>253.90 (+14.52%)</td><td>141.15 <b>(+63.94%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>426.00 (n/a)</td><td>334.14 (n/a)</td><td>325.40 (n/a)</td><td>221.70 (n/a)</td><td>86.10 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 <b>(+34.88%)</b></td><td>0.02 (+9.00%)</td><td>0.02 <b>(+23.01%)</b></td><td>0.01 <b>(-52.88%)</b></td><td>0.01 <b>(+270.79%)</b></td><td>1069.20 <b>(+112.23%)</b></td><td>494.44 (+13.03%)</td><td>366.00 (-18.72%)</td><td>277.50 <b>(-25.86%)</b></td><td>325.26 <b>(+550.99%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>503.80 (n/a)</td><td>437.44 (n/a)</td><td>450.30 (n/a)</td><td>374.30 (n/a)</td><td>49.96 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (+13.32%)</td><td>0.02 (+11.44%)</td><td>0.02 (+3.05%)</td><td>0.01 <b>(+71.67%)</b></td><td>0.01 (+5.25%)</td><td>1077.70 <b>(-41.75%)</b></td><td>550.18 <b>(-24.27%)</b></td><td>459.90 (-2.95%)</td><td>236.10 (-11.74%)</td><td>314.37 <b>(-50.73%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1850.00 (n/a)</td><td>726.46 (n/a)</td><td>473.90 (n/a)</td><td>267.50 (n/a)</td><td>638.01 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 <b>(+27.23%)</b></td><td>0.02 (+7.98%)</td><td>0.02 <b>(-20.43%)</b></td><td>0.02 <b>(+27.12%)</b></td><td>0.01 <b>(+23.75%)</b></td><td>465.50 <b>(-21.33%)</b></td><td>365.68 (-7.61%)</td><td>393.50 <b>(+25.68%)</b></td><td>224.40 <b>(-21.40%)</b></td><td>105.44 <b>(-21.14%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.70 (n/a)</td><td>395.78 (n/a)</td><td>313.10 (n/a)</td><td>285.50 (n/a)</td><td>133.70 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (+9.92%)</td><td>0.02 <b>(+22.19%)</b></td><td>0.03 <b>(+60.87%)</b></td><td>0.01 (-7.59%)</td><td>0.01 <b>(+25.55%)</b></td><td>659.80 (+8.22%)</td><td>387.52 (-14.44%)</td><td>318.10 <b>(-37.83%)</b></td><td>245.00 (-8.99%)</td><td>175.62 <b>(+20.55%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.70 (n/a)</td><td>452.92 (n/a)</td><td>511.70 (n/a)</td><td>269.20 (n/a)</td><td>145.68 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (+6.04%)</td><td>0.05 (-5.66%)</td><td>0.06 (+4.66%)</td><td>0.03 <b>(-32.95%)</b></td><td>0.02 <b>(+117.32%)</b></td><td>569.10 <b>(+49.14%)</b></td><td>354.16 (+18.56%)</td><td>273.00 (-4.45%)</td><td>227.80 (-5.67%)</td><td>152.55 <b>(+194.96%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>381.60 (n/a)</td><td>298.72 (n/a)</td><td>285.70 (n/a)</td><td>241.50 (n/a)</td><td>51.72 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (+6.77%)</td><td>0.06 (+5.20%)</td><td>0.06 (+2.51%)</td><td>0.03 (+8.51%)</td><td>0.02 (+7.01%)</td><td>580.90 (-7.85%)</td><td>327.74 (-5.40%)</td><td>284.50 (-2.47%)</td><td>233.00 (-6.35%)</td><td>144.47 (-9.72%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>630.40 (n/a)</td><td>346.46 (n/a)</td><td>291.70 (n/a)</td><td>248.80 (n/a)</td><td>160.02 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (-6.65%)</td><td>0.05 (+4.24%)</td><td>0.04 (-5.21%)</td><td>0.02 <b>(+182.33%)</b></td><td>0.02 <b>(-21.98%)</b></td><td>659.90 <b>(-64.58%)</b></td><td>403.98 <b>(-35.71%)</b></td><td>372.20 (+5.50%)</td><td>246.20 (+7.14%)</td><td>171.32 <b>(-75.28%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1863.20 (n/a)</td><td>628.36 (n/a)</td><td>352.80 (n/a)</td><td>229.80 (n/a)</td><td>693.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (-16.76%)</td><td>0.05 (-18.46%)</td><td>0.05 (-5.70%)</td><td>0.03 <b>(-47.51%)</b></td><td>0.01 <b>(+47.32%)</b></td><td>561.10 <b>(+90.53%)</b></td><td>347.54 <b>(+30.34%)</b></td><td>298.30 (+6.04%)</td><td>252.80 <b>(+20.15%)</b></td><td>123.00 <b>(+262.22%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>294.50 (n/a)</td><td>266.64 (n/a)</td><td>281.30 (n/a)</td><td>210.40 (n/a)</td><td>33.96 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (+3.47%)</td><td>0.06 <b>(+34.55%)</b></td><td>0.06 <b>(+77.06%)</b></td><td>0.03 (-1.44%)</td><td>0.01 (+6.66%)</td><td>505.10 (+1.47%)</td><td>310.78 <b>(-24.81%)</b></td><td>255.30 <b>(-43.53%)</b></td><td>240.80 (-3.37%)</td><td>110.72 (+11.78%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>497.80 (n/a)</td><td>413.32 (n/a)</td><td>452.10 (n/a)</td><td>249.20 (n/a)</td><td>99.05 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (+3.87%)</td><td>0.06 (-7.18%)</td><td>0.06 (+1.46%)</td><td>0.03 <b>(-36.69%)</b></td><td>0.02 <b>(+108.50%)</b></td><td>487.40 <b>(+57.94%)</b></td><td>304.94 (+14.67%)</td><td>270.90 (-1.46%)</td><td>224.20 (-3.69%)</td><td>105.44 <b>(+238.47%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>308.60 (n/a)</td><td>265.92 (n/a)</td><td>274.90 (n/a)</td><td>232.80 (n/a)</td><td>31.15 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (-16.05%)</td><td>0.07 <b>(+23.91%)</b></td><td>0.06 (+11.36%)</td><td>0.06 <b>(+124.30%)</b></td><td>0.00 <b>(-80.28%)</b></td><td>265.10 <b>(-55.42%)</b></td><td>251.72 <b>(-31.15%)</b></td><td>261.20 (-10.21%)</td><td>225.20 (+19.15%)</td><td>16.67 <b>(-89.86%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>594.70 (n/a)</td><td>365.58 (n/a)</td><td>290.90 (n/a)</td><td>189.00 (n/a)</td><td>164.40 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (+6.96%)</td><td>0.07 (+17.81%)</td><td>0.07 (+16.31%)</td><td>0.06 <b>(+77.56%)</b></td><td>0.01 <b>(-57.69%)</b></td><td>286.80 <b>(-43.69%)</b></td><td>251.76 <b>(-20.42%)</b></td><td>241.90 (-14.01%)</td><td>230.10 (-6.50%)</td><td>23.75 <b>(-78.38%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>509.30 (n/a)</td><td>316.36 (n/a)</td><td>281.30 (n/a)</td><td>246.10 (n/a)</td><td>109.88 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (+10.71%)</td><td>0.05 (-7.47%)</td><td>0.07 (+9.38%)</td><td>0.03 <b>(-27.93%)</b></td><td>0.02 <b>(+103.74%)</b></td><td>608.60 <b>(+38.76%)</b></td><td>381.10 <b>(+25.02%)</b></td><td>249.70 (-8.57%)</td><td>230.50 (-9.68%)</td><td>190.18 <b>(+150.61%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>438.60 (n/a)</td><td>304.84 (n/a)</td><td>273.10 (n/a)</td><td>255.20 (n/a)</td><td>75.89 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (+1.98%)</td><td>0.06 <b>(+34.47%)</b></td><td>0.06 <b>(+58.02%)</b></td><td>0.05 <b>(+86.48%)</b></td><td>0.01 <b>(-59.32%)</b></td><td>308.20 <b>(-46.38%)</b></td><td>272.52 <b>(-31.40%)</b></td><td>260.00 <b>(-36.72%)</b></td><td>245.40 (-1.92%)</td><td>28.50 <b>(-78.05%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>574.80 (n/a)</td><td>397.26 (n/a)</td><td>410.90 (n/a)</td><td>250.20 (n/a)</td><td>129.87 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (+10.93%)</td><td>0.05 (-7.95%)</td><td>0.06 (-2.64%)</td><td>0.02 <b>(-52.96%)</b></td><td>0.02 <b>(+88.37%)</b></td><td>998.90 <b>(+112.58%)</b></td><td>434.12 <b>(+38.68%)</b></td><td>288.40 (+2.71%)</td><td>218.40 (-9.86%)</td><td>324.96 <b>(+258.70%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>469.90 (n/a)</td><td>313.04 (n/a)</td><td>280.80 (n/a)</td><td>242.30 (n/a)</td><td>90.59 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (-3.41%)</td><td>0.04 <b>(-23.37%)</b></td><td>0.03 <b>(-34.49%)</b></td><td>0.03 <b>(-28.26%)</b></td><td>0.01 <b>(+45.07%)</b></td><td>615.10 <b>(+39.38%)</b></td><td>451.18 <b>(+37.93%)</b></td><td>468.20 <b>(+52.66%)</b></td><td>269.50 (+3.53%)</td><td>137.83 <b>(+100.64%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>441.30 (n/a)</td><td>327.10 (n/a)</td><td>306.70 (n/a)</td><td>260.30 (n/a)</td><td>68.70 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (+17.05%)</td><td>0.12 <b>(+25.91%)</b></td><td>0.13 (+4.82%)</td><td>0.05 <b>(+209.95%)</b></td><td>0.04 (-19.45%)</td><td>647.10 <b>(-67.74%)</b></td><td>317.74 <b>(-50.14%)</b></td><td>243.90 (-4.58%)</td><td>212.70 (-14.58%)</td><td>184.62 <b>(-75.98%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2005.60 (n/a)</td><td>637.24 (n/a)</td><td>255.60 (n/a)</td><td>249.00 (n/a)</td><td>768.64 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.16 (+18.27%)</td><td>0.11 (-4.58%)</td><td>0.11 (-9.92%)</td><td>0.07 <b>(-22.37%)</b></td><td>0.03 <b>(+66.50%)</b></td><td>476.80 <b>(+28.80%)</b></td><td>312.28 (+9.93%)</td><td>288.60 (+11.00%)</td><td>206.70 (-15.46%)</td><td>100.09 <b>(+88.87%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>370.20 (n/a)</td><td>284.06 (n/a)</td><td>260.00 (n/a)</td><td>244.50 (n/a)</td><td>52.99 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (+11.06%)</td><td>0.08 <b>(-23.15%)</b></td><td>0.08 <b>(-32.05%)</b></td><td>0.04 <b>(-38.51%)</b></td><td>0.04 <b>(+48.12%)</b></td><td>802.60 <b>(+62.63%)</b></td><td>455.64 <b>(+44.24%)</b></td><td>425.10 <b>(+47.14%)</b></td><td>220.80 (-9.95%)</td><td>212.14 <b>(+108.97%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>493.50 (n/a)</td><td>315.88 (n/a)</td><td>288.90 (n/a)</td><td>245.20 (n/a)</td><td>101.52 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (-0.73%)</td><td>0.08 (-4.55%)</td><td>0.08 <b>(-32.07%)</b></td><td>0.02 (+1.45%)</td><td>0.05 (-9.23%)</td><td>1827.40 (-1.43%)</td><td>661.28 (-2.17%)</td><td>428.50 <b>(+47.25%)</b></td><td>243.40 (+0.75%)</td><td>661.52 (-3.43%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1853.90 (n/a)</td><td>675.92 (n/a)</td><td>291.00 (n/a)</td><td>241.60 (n/a)</td><td>685.02 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 (+2.31%)</td><td>0.10 (+12.64%)</td><td>0.10 <b>(+23.82%)</b></td><td>0.08 <b>(+29.36%)</b></td><td>0.02 <b>(-23.99%)</b></td><td>427.90 <b>(-22.71%)</b></td><td>335.74 (-15.92%)</td><td>315.50 (-19.25%)</td><td>239.00 (-2.25%)</td><td>78.26 <b>(-42.31%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>553.60 (n/a)</td><td>399.32 (n/a)</td><td>390.70 (n/a)</td><td>244.50 (n/a)</td><td>135.65 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (+0.97%)</td><td>0.11 (+14.58%)</td><td>0.12 <b>(+32.70%)</b></td><td>0.07 (+8.91%)</td><td>0.03 (-16.69%)</td><td>491.20 (-8.19%)</td><td>328.34 (-15.48%)</td><td>283.10 <b>(-24.63%)</b></td><td>250.00 (-0.99%)</td><td>98.13 <b>(-23.37%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>535.00 (n/a)</td><td>388.48 (n/a)</td><td>375.60 (n/a)</td><td>252.50 (n/a)</td><td>128.06 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.16 <b>(+23.86%)</b></td><td>0.09 (-5.72%)</td><td>0.06 <b>(-25.16%)</b></td><td>0.03 <b>(-63.03%)</b></td><td>0.06 <b>(+96.28%)</b></td><td>1295.90 <b>(+170.49%)</b></td><td>554.26 <b>(+49.97%)</b></td><td>504.70 <b>(+33.59%)</b></td><td>201.30 (-19.29%)</td><td>439.63 <b>(+314.76%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>479.10 (n/a)</td><td>369.58 (n/a)</td><td>377.80 (n/a)</td><td>249.40 (n/a)</td><td>106.00 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (-15.55%)</td><td>0.09 (-15.98%)</td><td>0.08 <b>(-29.26%)</b></td><td>0.06 (+9.64%)</td><td>0.03 (-11.78%)</td><td>553.60 (-8.80%)</td><td>395.54 (+16.01%)</td><td>428.10 <b>(+41.38%)</b></td><td>249.10 (+18.39%)</td><td>134.35 (-13.81%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>607.00 (n/a)</td><td>340.94 (n/a)</td><td>302.80 (n/a)</td><td>210.40 (n/a)</td><td>155.87 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.16 (+13.37%)</td><td>0.11 (-7.05%)</td><td>0.13 (+7.15%)</td><td>0.02 <b>(-81.71%)</b></td><td>0.06 <b>(+150.46%)</b></td><td>2049.40 <b>(+446.80%)</b></td><td>610.88 <b>(+113.07%)</b></td><td>259.10 (-6.66%)</td><td>201.20 (-11.79%)</td><td>804.86 <b>(+1288.21%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>374.80 (n/a)</td><td>286.70 (n/a)</td><td>277.60 (n/a)</td><td>228.10 (n/a)</td><td>57.98 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (-17.42%)</td><td>0.09 (-10.68%)</td><td>0.09 (+4.78%)</td><td>0.06 (-1.96%)</td><td>0.02 <b>(-43.09%)</b></td><td>526.60 (+1.99%)</td><td>397.10 (+6.23%)</td><td>365.10 (-4.57%)</td><td>301.40 <b>(+21.09%)</b></td><td>91.57 <b>(-25.46%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>516.30 (n/a)</td><td>373.82 (n/a)</td><td>382.60 (n/a)</td><td>248.90 (n/a)</td><td>122.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (+13.65%)</td><td>0.09 (+3.17%)</td><td>0.08 <b>(-26.25%)</b></td><td>0.07 (+14.39%)</td><td>0.03 <b>(+34.51%)</b></td><td>481.50 (-12.58%)</td><td>378.68 (-0.99%)</td><td>436.00 <b>(+35.57%)</b></td><td>256.30 (-12.02%)</td><td>112.43 (+0.87%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>550.80 (n/a)</td><td>382.48 (n/a)</td><td>321.60 (n/a)</td><td>291.30 (n/a)</td><td>111.46 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (-19.48%)</td><td>0.08 <b>(-21.81%)</b></td><td>0.08 <b>(-38.58%)</b></td><td>0.05 (-3.35%)</td><td>0.02 <b>(-47.26%)</b></td><td>624.00 (+3.47%)</td><td>449.72 (+17.75%)</td><td>435.40 <b>(+62.77%)</b></td><td>324.00 <b>(+24.19%)</b></td><td>117.03 <b>(-28.95%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>603.10 (n/a)</td><td>381.94 (n/a)</td><td>267.50 (n/a)</td><td>260.90 (n/a)</td><td>164.71 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (-0.25%)</td><td>0.07 (+15.59%)</td><td>0.06 (+13.56%)</td><td>0.06 <b>(+23.71%)</b></td><td>0.02 (-16.38%)</td><td>442.30 (-19.17%)</td><td>366.12 (-16.38%)</td><td>395.80 (-11.93%)</td><td>247.90 (+0.24%)</td><td>85.84 <b>(-30.76%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>547.20 (n/a)</td><td>437.86 (n/a)</td><td>449.40 (n/a)</td><td>247.30 (n/a)</td><td>123.98 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.20 (-1.13%)</td><td>0.16 (+1.38%)</td><td>0.18 (+6.81%)</td><td>0.09 (-7.66%)</td><td>0.05 (+5.85%)</td><td>529.10 (+8.29%)</td><td>338.18 (+0.01%)</td><td>267.80 (-6.40%)</td><td>251.10 (+1.17%)</td><td>121.42 (+13.63%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>488.60 (n/a)</td><td>338.14 (n/a)</td><td>286.10 (n/a)</td><td>248.20 (n/a)</td><td>106.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.97 (-6.62%)</td><td>3.29 (-1.82%)</td><td>3.30 (-9.02%)</td><td>2.68 (+14.85%)</td><td>0.60 <b>(-28.10%)</b></td><td>3909.90 (-12.93%)</td><td>3269.80 (-0.92%)</td><td>3175.40 (+9.92%)</td><td>2638.20 (+7.09%)</td><td>599.92 <b>(-32.46%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>4.26 (n/a)</td><td>3.36 (n/a)</td><td>3.63 (n/a)</td><td>2.34 (n/a)</td><td>0.83 (n/a)</td><td>4490.50 (n/a)</td><td>3300.26 (n/a)</td><td>2888.90 (n/a)</td><td>2463.50 (n/a)</td><td>888.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.20 (+4.00%)</td><td>0.13 (+11.28%)</td><td>0.15 <b>(+62.99%)</b></td><td>0.08 (+8.67%)</td><td>0.06 (-4.26%)</td><td>541.70 (-7.98%)</td><td>358.16 (-11.56%)</td><td>274.90 <b>(-38.65%)</b></td><td>206.60 (-3.82%)</td><td>163.25 (-5.69%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>588.70 (n/a)</td><td>404.98 (n/a)</td><td>448.10 (n/a)</td><td>214.80 (n/a)</td><td>173.10 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (+1.71%)</td><td>0.02 (+12.23%)</td><td>0.02 (-4.74%)</td><td>0.01 <b>(+32.89%)</b></td><td>0.00 <b>(-33.05%)</b></td><td>406.10 <b>(-24.74%)</b></td><td>297.90 (-16.48%)</td><td>292.50 (+4.99%)</td><td>243.10 (-1.70%)</td><td>65.64 <b>(-50.10%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>539.60 (n/a)</td><td>356.66 (n/a)</td><td>278.60 (n/a)</td><td>247.30 (n/a)</td><td>131.53 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (-17.49%)</td><td>0.01 (+6.74%)</td><td>0.02 <b>(+59.02%)</b></td><td>0.01 (-9.23%)</td><td>0.00 (-7.91%)</td><td>516.20 (+10.18%)</td><td>335.06 (-4.99%)</td><td>242.70 <b>(-37.12%)</b></td><td>232.90 <b>(+21.24%)</b></td><td>134.28 <b>(+21.61%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>468.50 (n/a)</td><td>352.64 (n/a)</td><td>386.00 (n/a)</td><td>192.10 (n/a)</td><td>110.42 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 <b>(+35.41%)</b></td><td>0.01 (+9.30%)</td><td>0.01 (-3.57%)</td><td>0.01 (+6.89%)</td><td>0.00 <b>(+68.02%)</b></td><td>562.30 (-6.44%)</td><td>445.88 (-5.89%)</td><td>474.10 (+3.72%)</td><td>266.20 <b>(-26.14%)</b></td><td>109.10 (+7.68%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>601.00 (n/a)</td><td>473.78 (n/a)</td><td>457.10 (n/a)</td><td>360.40 (n/a)</td><td>101.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (+9.11%)</td><td>0.02 <b>(+36.21%)</b></td><td>0.02 <b>(+27.73%)</b></td><td>0.01 <b>(+82.40%)</b></td><td>0.00 <b>(-62.18%)</b></td><td>293.40 <b>(-45.17%)</b></td><td>267.38 <b>(-32.07%)</b></td><td>261.30 <b>(-21.70%)</b></td><td>237.20 (-8.35%)</td><td>22.96 <b>(-82.08%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>535.10 (n/a)</td><td>393.64 (n/a)</td><td>333.70 (n/a)</td><td>258.80 (n/a)</td><td>128.18 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 <b>(-45.09%)</b></td><td>0.01 (-19.30%)</td><td>0.01 (-17.75%)</td><td>0.01 <b>(+22.07%)</b></td><td>0.00 <b>(-81.53%)</b></td><td>541.30 (-18.08%)</td><td>493.54 (+8.02%)</td><td>504.00 <b>(+21.59%)</b></td><td>417.30 <b>(+82.15%)</b></td><td>47.08 <b>(-73.73%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>660.80 (n/a)</td><td>456.90 (n/a)</td><td>414.50 (n/a)</td><td>229.10 (n/a)</td><td>179.26 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (-11.85%)</td><td>0.01 <b>(-26.14%)</b></td><td>0.01 <b>(-36.97%)</b></td><td>0.01 <b>(+21.49%)</b></td><td>0.00 <b>(-26.22%)</b></td><td>543.60 (-17.69%)</td><td>413.64 <b>(+24.46%)</b></td><td>396.10 <b>(+58.63%)</b></td><td>242.20 (+13.44%)</td><td>117.89 <b>(-36.59%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>660.40 (n/a)</td><td>332.34 (n/a)</td><td>249.70 (n/a)</td><td>213.50 (n/a)</td><td>185.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 <b>(+32.06%)</b></td><td>0.02 <b>(+27.76%)</b></td><td>0.01 (+1.31%)</td><td>0.01 <b>(+275.23%)</b></td><td>0.01 (+0.07%)</td><td>487.50 <b>(-73.35%)</b></td><td>375.00 <b>(-43.92%)</b></td><td>435.30 (-1.29%)</td><td>214.60 <b>(-24.28%)</b></td><td>125.32 <b>(-80.84%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1829.30 (n/a)</td><td>668.70 (n/a)</td><td>441.00 (n/a)</td><td>283.40 (n/a)</td><td>654.07 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (-5.06%)</td><td>0.01 (+4.74%)</td><td>0.01 (-9.95%)</td><td>0.01 <b>(+257.61%)</b></td><td>0.00 <b>(-49.62%)</b></td><td>496.80 <b>(-72.04%)</b></td><td>336.58 <b>(-42.21%)</b></td><td>294.20 (+11.06%)</td><td>260.50 (+5.34%)</td><td>95.94 <b>(-85.66%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1776.80 (n/a)</td><td>582.44 (n/a)</td><td>264.90 (n/a)</td><td>247.30 (n/a)</td><td>669.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 <b>(+29.34%)</b></td><td>0.01 <b>(+34.18%)</b></td><td>0.01 (+10.34%)</td><td>0.01 <b>(+60.41%)</b></td><td>0.01 (+11.57%)</td><td>630.80 <b>(-37.66%)</b></td><td>441.10 <b>(-32.07%)</b></td><td>515.00 (-9.36%)</td><td>241.20 <b>(-22.69%)</b></td><td>165.00 <b>(-50.26%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1011.80 (n/a)</td><td>649.38 (n/a)</td><td>568.20 (n/a)</td><td>312.00 (n/a)</td><td>331.73 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 <b>(-20.10%)</b></td><td>0.01 (-17.42%)</td><td>0.01 (-3.80%)</td><td>0.00 <b>(-69.82%)</b></td><td>0.00 (-0.99%)</td><td>1902.40 <b>(+231.43%)</b></td><td>690.36 <b>(+66.18%)</b></td><td>445.10 (+3.95%)</td><td>291.30 <b>(+25.18%)</b></td><td>682.75 <b>(+330.75%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>574.00 (n/a)</td><td>415.44 (n/a)</td><td>428.20 (n/a)</td><td>232.70 (n/a)</td><td>158.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 <b>(+32.52%)</b></td><td>0.01 (+0.86%)</td><td>0.01 (-4.35%)</td><td>0.01 (+8.59%)</td><td>0.01 <b>(+55.50%)</b></td><td>615.90 (-7.91%)</td><td>477.78 (+5.64%)</td><td>493.80 (+4.53%)</td><td>202.20 <b>(-24.55%)</b></td><td>168.35 (+6.54%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>668.80 (n/a)</td><td>452.28 (n/a)</td><td>472.40 (n/a)</td><td>268.00 (n/a)</td><td>158.02 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (+15.73%)</td><td>0.01 (-4.25%)</td><td>0.01 (-17.06%)</td><td>0.01 (+1.01%)</td><td>0.00 <b>(+24.73%)</b></td><td>568.00 (-1.01%)</td><td>443.70 (+6.02%)</td><td>472.00 <b>(+20.56%)</b></td><td>235.50 (-13.61%)</td><td>124.31 (-3.71%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>573.80 (n/a)</td><td>418.52 (n/a)</td><td>391.50 (n/a)</td><td>272.60 (n/a)</td><td>129.10 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 <b>(+20.05%)</b></td><td>0.03 (+10.86%)</td><td>0.03 (+15.89%)</td><td>0.02 (-3.98%)</td><td>0.01 <b>(+52.37%)</b></td><td>476.00 (+4.13%)</td><td>300.96 (-6.34%)</td><td>248.60 (-13.71%)</td><td>216.40 (-16.71%)</td><td>104.43 <b>(+31.97%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>457.10 (n/a)</td><td>321.32 (n/a)</td><td>288.10 (n/a)</td><td>259.80 (n/a)</td><td>79.13 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 <b>(-25.77%)</b></td><td>0.03 (-8.97%)</td><td>0.03 (+16.17%)</td><td>0.02 (+4.05%)</td><td>0.01 <b>(-42.42%)</b></td><td>576.40 (-3.89%)</td><td>403.78 (-3.53%)</td><td>410.50 (-13.92%)</td><td>261.20 <b>(+34.71%)</b></td><td>137.38 <b>(-30.11%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>599.70 (n/a)</td><td>418.56 (n/a)</td><td>476.90 (n/a)</td><td>193.90 (n/a)</td><td>196.56 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 <b>(-30.29%)</b></td><td>0.02 <b>(-24.01%)</b></td><td>0.03 <b>(-20.14%)</b></td><td>0.01 (-13.35%)</td><td>0.01 <b>(-28.44%)</b></td><td>581.20 (+15.41%)</td><td>371.76 <b>(+29.00%)</b></td><td>308.70 <b>(+25.18%)</b></td><td>247.90 <b>(+43.46%)</b></td><td>140.75 (+11.14%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>503.60 (n/a)</td><td>288.18 (n/a)</td><td>246.60 (n/a)</td><td>172.80 (n/a)</td><td>126.64 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 <b>(-30.52%)</b></td><td>0.02 (-9.41%)</td><td>0.02 (-4.06%)</td><td>0.02 <b>(+73.34%)</b></td><td>0.00 <b>(-69.44%)</b></td><td>579.50 <b>(-42.31%)</b></td><td>472.56 (-9.28%)</td><td>490.60 (+4.23%)</td><td>391.60 <b>(+43.92%)</b></td><td>75.42 <b>(-74.43%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1004.50 (n/a)</td><td>520.92 (n/a)</td><td>470.70 (n/a)</td><td>272.10 (n/a)</td><td>294.94 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-19.12%)</td><td>0.02 <b>(-41.96%)</b></td><td>0.02 <b>(-47.81%)</b></td><td>0.01 <b>(-58.15%)</b></td><td>0.01 <b>(+89.79%)</b></td><td>655.50 <b>(+138.97%)</b></td><td>463.28 <b>(+92.52%)</b></td><td>474.40 <b>(+91.68%)</b></td><td>246.10 <b>(+23.61%)</b></td><td>165.84 <b>(+464.36%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>274.30 (n/a)</td><td>240.64 (n/a)</td><td>247.50 (n/a)</td><td>199.10 (n/a)</td><td>29.39 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (+8.84%)</td><td>0.03 <b>(-20.18%)</b></td><td>0.02 <b>(-36.33%)</b></td><td>0.02 (-10.12%)</td><td>0.01 <b>(+35.41%)</b></td><td>500.70 (+11.24%)</td><td>433.28 <b>(+30.08%)</b></td><td>475.40 <b>(+57.05%)</b></td><td>235.20 (-8.13%)</td><td>112.30 <b>(+35.60%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>450.10 (n/a)</td><td>333.10 (n/a)</td><td>302.70 (n/a)</td><td>256.00 (n/a)</td><td>82.82 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-12.89%)</td><td>0.02 (-9.81%)</td><td>0.02 <b>(-30.13%)</b></td><td>0.02 <b>(+20.89%)</b></td><td>0.01 <b>(-21.61%)</b></td><td>495.80 (-17.27%)</td><td>388.22 (+6.03%)</td><td>432.50 <b>(+43.12%)</b></td><td>265.70 (+14.77%)</td><td>103.73 <b>(-28.89%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.30 (n/a)</td><td>366.14 (n/a)</td><td>302.20 (n/a)</td><td>231.50 (n/a)</td><td>145.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-14.64%)</td><td>0.02 <b>(-26.14%)</b></td><td>0.02 <b>(-36.17%)</b></td><td>0.02 (-6.21%)</td><td>0.01 (-19.90%)</td><td>600.40 (+6.62%)</td><td>510.70 <b>(+32.59%)</b></td><td>552.80 <b>(+56.64%)</b></td><td>285.90 (+17.12%)</td><td>128.07 (-4.76%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>563.10 (n/a)</td><td>385.18 (n/a)</td><td>352.90 (n/a)</td><td>244.10 (n/a)</td><td>134.47 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 <b>(+33.09%)</b></td><td>0.02 <b>(+38.80%)</b></td><td>0.03 <b>(+55.19%)</b></td><td>0.01 <b>(+26.94%)</b></td><td>0.01 <b>(+57.86%)</b></td><td>610.80 <b>(-21.23%)</b></td><td>383.76 <b>(-25.31%)</b></td><td>293.40 <b>(-35.56%)</b></td><td>252.10 <b>(-24.86%)</b></td><td>155.28 (-8.34%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>775.40 (n/a)</td><td>513.82 (n/a)</td><td>455.30 (n/a)</td><td>335.50 (n/a)</td><td>169.41 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-16.53%)</td><td>0.02 <b>(-20.46%)</b></td><td>0.02 <b>(-41.68%)</b></td><td>0.02 (+15.42%)</td><td>0.01 <b>(-36.29%)</b></td><td>583.30 (-13.35%)</td><td>490.04 (+17.87%)</td><td>551.30 <b>(+71.48%)</b></td><td>324.80 (+19.81%)</td><td>114.86 <b>(-32.60%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>673.20 (n/a)</td><td>415.76 (n/a)</td><td>321.50 (n/a)</td><td>271.10 (n/a)</td><td>170.42 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (-14.63%)</td><td>0.02 (-5.75%)</td><td>0.02 (-12.45%)</td><td>0.01 <b>(+69.94%)</b></td><td>0.01 <b>(-43.06%)</b></td><td>574.90 <b>(-41.16%)</b></td><td>462.28 (-10.04%)</td><td>504.00 (+14.21%)</td><td>306.30 (+17.18%)</td><td>118.89 <b>(-59.14%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>977.00 (n/a)</td><td>513.90 (n/a)</td><td>441.30 (n/a)</td><td>261.40 (n/a)</td><td>290.98 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (-5.21%)</td><td>0.05 (-9.02%)</td><td>0.06 (-14.09%)</td><td>0.03 <b>(+23.68%)</b></td><td>0.02 (-5.38%)</td><td>468.70 (-19.15%)</td><td>334.90 (+6.62%)</td><td>290.60 (+16.43%)</td><td>219.90 (+5.47%)</td><td>118.27 <b>(-21.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>579.70 (n/a)</td><td>314.10 (n/a)</td><td>249.60 (n/a)</td><td>208.50 (n/a)</td><td>151.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (+2.15%)</td><td>0.06 <b>(-26.72%)</b></td><td>0.05 <b>(-41.20%)</b></td><td>0.05 <b>(-31.08%)</b></td><td>0.02 <b>(+106.31%)</b></td><td>544.20 <b>(+45.08%)</b></td><td>455.26 <b>(+46.26%)</b></td><td>524.70 <b>(+70.08%)</b></td><td>252.20 (-2.13%)</td><td>122.85 <b>(+188.58%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>375.10 (n/a)</td><td>311.26 (n/a)</td><td>308.50 (n/a)</td><td>257.70 (n/a)</td><td>42.57 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 <b>(-27.29%)</b></td><td>0.04 <b>(-22.81%)</b></td><td>0.04 <b>(-35.86%)</b></td><td>0.02 (-9.74%)</td><td>0.02 <b>(-35.46%)</b></td><td>686.80 (+10.79%)</td><td>437.04 (+18.36%)</td><td>410.80 <b>(+55.90%)</b></td><td>245.80 <b>(+37.55%)</b></td><td>182.54 (-9.19%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>619.90 (n/a)</td><td>369.24 (n/a)</td><td>263.50 (n/a)</td><td>178.70 (n/a)</td><td>201.02 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.09 <b>(+30.81%)</b></td><td>0.05 (+11.09%)</td><td>0.04 (-1.76%)</td><td>0.03 (-9.02%)</td><td>0.03 <b>(+67.08%)</b></td><td>652.50 (+9.92%)</td><td>455.66 (-2.72%)</td><td>476.10 (+1.77%)</td><td>215.70 <b>(-23.56%)</b></td><td>165.61 <b>(+38.27%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>593.60 (n/a)</td><td>468.42 (n/a)</td><td>467.80 (n/a)</td><td>282.20 (n/a)</td><td>119.77 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (-2.48%)</td><td>0.06 <b>(+22.90%)</b></td><td>0.07 (+0.72%)</td><td>0.04 <b>(+168.80%)</b></td><td>0.01 <b>(-57.12%)</b></td><td>384.20 <b>(-62.80%)</b></td><td>280.92 <b>(-40.88%)</b></td><td>245.00 (-0.73%)</td><td>241.00 (+2.55%)</td><td>61.54 <b>(-82.46%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1032.70 (n/a)</td><td>475.16 (n/a)</td><td>246.80 (n/a)</td><td>235.00 (n/a)</td><td>350.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 <b>(-41.19%)</b></td><td>0.04 (-16.58%)</td><td>0.04 (-8.35%)</td><td>0.04 (+5.57%)</td><td>0.00 <b>(-77.01%)</b></td><td>561.50 (-5.26%)</td><td>499.48 (+9.76%)</td><td>494.40 (+9.11%)</td><td>431.00 <b>(+70.02%)</b></td><td>51.74 <b>(-63.54%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>592.70 (n/a)</td><td>455.08 (n/a)</td><td>453.10 (n/a)</td><td>253.50 (n/a)</td><td>141.91 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (+2.50%)</td><td>0.04 (-16.49%)</td><td>0.04 <b>(-25.41%)</b></td><td>0.03 (+0.80%)</td><td>0.02 (+9.40%)</td><td>562.30 (-0.79%)</td><td>425.68 <b>(+20.63%)</b></td><td>421.30 <b>(+34.09%)</b></td><td>244.70 (-2.43%)</td><td>126.44 (+0.82%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>566.80 (n/a)</td><td>352.88 (n/a)</td><td>314.20 (n/a)</td><td>250.80 (n/a)</td><td>125.42 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (+4.80%)</td><td>0.05 (+6.71%)</td><td>0.05 (+16.53%)</td><td>0.03 <b>(+30.38%)</b></td><td>0.01 <b>(-32.71%)</b></td><td>542.20 <b>(-23.31%)</b></td><td>409.90 (-13.49%)</td><td>407.90 (-14.18%)</td><td>280.50 (-4.59%)</td><td>92.61 <b>(-48.88%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>707.00 (n/a)</td><td>473.80 (n/a)</td><td>475.30 (n/a)</td><td>294.00 (n/a)</td><td>181.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 <b>(+31.20%)</b></td><td>0.04 <b>(+24.45%)</b></td><td>0.04 <b>(+23.35%)</b></td><td>0.03 (+0.83%)</td><td>0.01 <b>(+112.27%)</b></td><td>625.50 (-0.82%)</td><td>446.92 (-17.02%)</td><td>441.20 (-18.93%)</td><td>337.80 <b>(-23.78%)</b></td><td>112.55 <b>(+62.21%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>630.70 (n/a)</td><td>538.60 (n/a)</td><td>544.20 (n/a)</td><td>443.20 (n/a)</td><td>69.39 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (+5.89%)</td><td>0.04 <b>(+31.59%)</b></td><td>0.04 (+12.87%)</td><td>0.04 <b>(+313.87%)</b></td><td>0.00 <b>(-74.47%)</b></td><td>476.90 <b>(-75.84%)</b></td><td>447.88 <b>(-44.20%)</b></td><td>451.70 (-11.40%)</td><td>390.10 (-5.57%)</td><td>34.43 <b>(-94.78%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1973.70 (n/a)</td><td>802.60 (n/a)</td><td>509.80 (n/a)</td><td>413.10 (n/a)</td><td>659.14 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (-2.99%)</td><td>0.04 (-10.70%)</td><td>0.04 (-15.53%)</td><td>0.03 (-8.83%)</td><td>0.01 <b>(+21.45%)</b></td><td>554.40 (+9.67%)</td><td>442.82 (+14.49%)</td><td>433.70 (+18.40%)</td><td>301.10 (+3.08%)</td><td>110.08 <b>(+41.22%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>505.50 (n/a)</td><td>386.76 (n/a)</td><td>366.30 (n/a)</td><td>292.10 (n/a)</td><td>77.95 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (-13.22%)</td><td>0.11 (+9.33%)</td><td>0.11 (+17.11%)</td><td>0.07 (+18.92%)</td><td>0.02 <b>(-43.75%)</b></td><td>461.10 (-15.90%)</td><td>323.84 (-15.56%)</td><td>289.60 (-14.62%)</td><td>268.90 (+15.21%)</td><td>78.50 <b>(-46.18%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>548.30 (n/a)</td><td>383.52 (n/a)</td><td>339.20 (n/a)</td><td>233.40 (n/a)</td><td>145.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (+12.40%)</td><td>0.09 <b>(+95.93%)</b></td><td>0.07 <b>(+312.54%)</b></td><td>0.07 <b>(+326.61%)</b></td><td>0.03 <b>(-37.66%)</b></td><td>475.20 <b>(-76.56%)</b></td><td>400.48 <b>(-70.34%)</b></td><td>457.60 <b>(-75.76%)</b></td><td>245.60 (-11.05%)</td><td>100.64 <b>(-88.00%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>2027.10 (n/a)</td><td>1350.30 (n/a)</td><td>1888.00 (n/a)</td><td>276.10 (n/a)</td><td>838.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 (-5.93%)</td><td>0.09 (-10.01%)</td><td>0.08 (-13.08%)</td><td>0.06 <b>(-21.67%)</b></td><td>0.03 (+6.71%)</td><td>721.30 <b>(+27.66%)</b></td><td>507.86 (+14.93%)</td><td>517.40 (+15.05%)</td><td>284.80 (+6.31%)</td><td>166.00 <b>(+46.05%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>565.00 (n/a)</td><td>441.88 (n/a)</td><td>449.70 (n/a)</td><td>267.90 (n/a)</td><td>113.66 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 <b>(+72.41%)</b></td><td>0.08 <b>(+57.64%)</b></td><td>0.08 <b>(+28.70%)</b></td><td>0.05 <b>(+221.33%)</b></td><td>0.03 <b>(+28.42%)</b></td><td>631.70 <b>(-68.88%)</b></td><td>425.22 <b>(-48.48%)</b></td><td>419.00 <b>(-22.31%)</b></td><td>280.30 <b>(-41.99%)</b></td><td>142.27 <b>(-78.88%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>2029.80 (n/a)</td><td>825.34 (n/a)</td><td>539.30 (n/a)</td><td>483.20 (n/a)</td><td>673.74 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.16 (-8.84%)</td><td>0.11 (-7.36%)</td><td>0.09 <b>(-31.72%)</b></td><td>0.05 (+0.37%)</td><td>0.04 <b>(-21.65%)</b></td><td>798.00 (-0.36%)</td><td>448.60 (-0.58%)</td><td>440.10 <b>(+46.46%)</b></td><td>261.00 (+9.71%)</td><td>214.10 (-16.62%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>800.90 (n/a)</td><td>451.22 (n/a)</td><td>300.50 (n/a)</td><td>237.90 (n/a)</td><td>256.77 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (+12.46%)</td><td>0.09 (-9.49%)</td><td>0.08 (-8.22%)</td><td>0.06 <b>(-27.70%)</b></td><td>0.02 <b>(+115.76%)</b></td><td>529.40 <b>(+38.30%)</b></td><td>402.00 (+15.51%)</td><td>398.90 (+8.93%)</td><td>271.00 (-11.09%)</td><td>100.97 <b>(+166.38%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>382.80 (n/a)</td><td>348.02 (n/a)</td><td>366.20 (n/a)</td><td>304.80 (n/a)</td><td>37.91 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (-4.01%)</td><td>0.10 (+7.17%)</td><td>0.10 <b>(+40.45%)</b></td><td>0.04 <b>(-37.73%)</b></td><td>0.04 (+0.26%)</td><td>971.40 <b>(+60.59%)</b></td><td>464.42 (+1.29%)</td><td>367.90 <b>(-28.81%)</b></td><td>240.80 (+4.20%)</td><td>292.10 <b>(+74.38%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>604.90 (n/a)</td><td>458.52 (n/a)</td><td>516.80 (n/a)</td><td>231.10 (n/a)</td><td>167.51 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 <b>(+33.22%)</b></td><td>0.07 <b>(+30.23%)</b></td><td>0.07 (+2.91%)</td><td>0.02 <b>(+24.02%)</b></td><td>0.05 (+16.29%)</td><td>2005.40 (-19.37%)</td><td>749.32 <b>(-33.78%)</b></td><td>473.30 (-2.83%)</td><td>226.70 <b>(-24.93%)</b></td><td>714.27 <b>(-28.31%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2487.20 (n/a)</td><td>1131.54 (n/a)</td><td>487.10 (n/a)</td><td>302.00 (n/a)</td><td>996.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (-15.70%)</td><td>0.10 (-15.34%)</td><td>0.13 (+3.98%)</td><td>0.02 <b>(-73.05%)</b></td><td>0.06 <b>(+35.53%)</b></td><td>1918.00 <b>(+271.06%)</b></td><td>635.04 <b>(+92.42%)</b></td><td>289.70 (-3.82%)</td><td>245.40 (+18.61%)</td><td>723.02 <b>(+500.62%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>516.90 (n/a)</td><td>330.02 (n/a)</td><td>301.20 (n/a)</td><td>206.90 (n/a)</td><td>120.38 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.09 <b>(-25.74%)</b></td><td>0.07 (+1.74%)</td><td>0.07 (+11.27%)</td><td>0.05 <b>(+185.85%)</b></td><td>0.02 <b>(-70.27%)</b></td><td>654.70 <b>(-65.02%)</b></td><td>500.84 <b>(-47.80%)</b></td><td>500.30 (-10.13%)</td><td>354.90 <b>(+34.64%)</b></td><td>106.19 <b>(-87.02%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1871.40 (n/a)</td><td>959.48 (n/a)</td><td>556.70 (n/a)</td><td>263.60 (n/a)</td><td>818.01 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (-11.31%)</td><td>0.05 (-14.61%)</td><td>0.04 <b>(-27.54%)</b></td><td>0.03 <b>(-27.79%)</b></td><td>0.02 (+17.15%)</td><td>694.70 <b>(+38.50%)</b></td><td>451.66 <b>(+23.13%)</b></td><td>474.00 <b>(+37.99%)</b></td><td>295.40 (+12.75%)</td><td>165.63 <b>(+68.75%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>501.60 (n/a)</td><td>366.82 (n/a)</td><td>343.50 (n/a)</td><td>262.00 (n/a)</td><td>98.15 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (+8.68%)</td><td>0.05 (+12.92%)</td><td>0.04 (+5.94%)</td><td>0.04 <b>(+66.29%)</b></td><td>0.02 (-3.51%)</td><td>582.60 <b>(-39.87%)</b></td><td>423.12 (-18.63%)</td><td>476.20 (-5.61%)</td><td>260.90 (-8.00%)</td><td>148.51 <b>(-46.44%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>968.90 (n/a)</td><td>519.98 (n/a)</td><td>504.50 (n/a)</td><td>283.60 (n/a)</td><td>277.28 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (-4.40%)</td><td>0.06 (+12.01%)</td><td>0.07 <b>(+65.31%)</b></td><td>0.04 (-0.97%)</td><td>0.02 (+15.87%)</td><td>573.30 (+0.97%)</td><td>376.06 (-7.37%)</td><td>273.60 <b>(-39.50%)</b></td><td>258.20 (+4.58%)</td><td>155.51 <b>(+22.01%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>567.80 (n/a)</td><td>405.96 (n/a)</td><td>452.20 (n/a)</td><td>246.90 (n/a)</td><td>127.46 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 <b>(+195.63%)</b></td><td>0.06 <b>(+50.46%)</b></td><td>0.04 (+15.19%)</td><td>0.03 <b>(-26.29%)</b></td><td>0.04 <b>(+1949.92%)</b></td><td>794.30 <b>(+35.66%)</b></td><td>469.94 (-13.64%)</td><td>470.60 (-13.17%)</td><td>174.10 <b>(-66.17%)</b></td><td>235.65 <b>(+796.15%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>585.50 (n/a)</td><td>544.14 (n/a)</td><td>542.00 (n/a)</td><td>514.60 (n/a)</td><td>26.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 <b>(-25.60%)</b></td><td>0.04 <b>(-38.94%)</b></td><td>0.04 <b>(-51.00%)</b></td><td>0.02 <b>(-50.22%)</b></td><td>0.02 <b>(-25.47%)</b></td><td>1074.20 <b>(+100.90%)</b></td><td>594.68 <b>(+71.69%)</b></td><td>551.70 <b>(+104.03%)</b></td><td>326.70 <b>(+34.44%)</b></td><td>283.45 <b>(+117.21%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>534.70 (n/a)</td><td>346.36 (n/a)</td><td>270.40 (n/a)</td><td>243.00 (n/a)</td><td>130.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (-0.87%)</td><td>0.04 (+10.99%)</td><td>0.04 (+5.77%)</td><td>0.04 <b>(+81.80%)</b></td><td>0.00 <b>(-57.93%)</b></td><td>569.90 <b>(-45.00%)</b></td><td>518.04 (-16.95%)</td><td>541.70 (-5.46%)</td><td>439.90 (+0.87%)</td><td>53.51 <b>(-77.69%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1036.10 (n/a)</td><td>623.74 (n/a)</td><td>573.00 (n/a)</td><td>436.10 (n/a)</td><td>239.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 <b>(-23.72%)</b></td><td>0.06 (-7.56%)</td><td>0.06 (+8.81%)</td><td>0.05 (+15.68%)</td><td>0.01 <b>(-47.67%)</b></td><td>509.20 (-13.55%)</td><td>425.26 (+0.42%)</td><td>442.00 (-8.09%)</td><td>311.70 <b>(+31.08%)</b></td><td>89.41 <b>(-38.37%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>589.00 (n/a)</td><td>423.48 (n/a)</td><td>480.90 (n/a)</td><td>237.80 (n/a)</td><td>145.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.09 (+19.75%)</td><td>0.07 <b>(+32.75%)</b></td><td>0.08 <b>(+66.53%)</b></td><td>0.04 (-8.27%)</td><td>0.02 <b>(+33.96%)</b></td><td>644.40 (+9.02%)</td><td>367.92 <b>(-21.60%)</b></td><td>298.10 <b>(-39.95%)</b></td><td>267.40 (-16.52%)</td><td>157.17 <b>(+26.05%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>591.10 (n/a)</td><td>469.28 (n/a)</td><td>496.40 (n/a)</td><td>320.30 (n/a)</td><td>124.69 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (+19.62%)</td><td>0.07 (+8.57%)</td><td>0.08 (+10.31%)</td><td>0.04 <b>(+79.50%)</b></td><td>0.03 (+9.37%)</td><td>594.90 <b>(-44.29%)</b></td><td>398.70 (-16.58%)</td><td>310.00 (-9.36%)</td><td>231.90 (-16.40%)</td><td>164.41 <b>(-50.47%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1067.90 (n/a)</td><td>477.94 (n/a)</td><td>342.00 (n/a)</td><td>277.40 (n/a)</td><td>331.96 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 <b>(+21.11%)</b></td><td>0.07 (+5.60%)</td><td>0.06 (+8.44%)</td><td>0.04 (-14.73%)</td><td>0.03 <b>(+36.38%)</b></td><td>666.20 (+17.29%)</td><td>425.22 (+1.84%)</td><td>434.80 (-7.78%)</td><td>203.80 (-17.46%)</td><td>187.18 <b>(+32.01%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>568.00 (n/a)</td><td>417.52 (n/a)</td><td>471.50 (n/a)</td><td>246.90 (n/a)</td><td>141.79 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 <b>(+36.14%)</b></td><td>0.05 (-6.78%)</td><td>0.05 (-7.59%)</td><td>0.01 <b>(-72.67%)</b></td><td>0.03 <b>(+156.87%)</b></td><td>2436.00 <b>(+265.93%)</b></td><td>853.46 <b>(+72.17%)</b></td><td>468.70 (+8.22%)</td><td>294.60 <b>(-26.55%)</b></td><td>891.50 <b>(+698.58%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>665.70 (n/a)</td><td>495.72 (n/a)</td><td>433.10 (n/a)</td><td>401.10 (n/a)</td><td>111.64 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 <b>(-22.39%)</b></td><td>0.05 (-11.33%)</td><td>0.05 <b>(-22.99%)</b></td><td>0.04 <b>(+168.26%)</b></td><td>0.01 <b>(-61.24%)</b></td><td>684.50 <b>(-62.72%)</b></td><td>522.08 <b>(-22.99%)</b></td><td>529.70 <b>(+29.86%)</b></td><td>386.10 <b>(+28.83%)</b></td><td>108.21 <b>(-83.38%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1836.20 (n/a)</td><td>677.94 (n/a)</td><td>407.90 (n/a)</td><td>299.70 (n/a)</td><td>651.13 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (+8.75%)</td><td>0.06 <b>(+51.00%)</b></td><td>0.07 <b>(+98.45%)</b></td><td>0.04 <b>(+132.36%)</b></td><td>0.02 (-15.75%)</td><td>444.90 <b>(-56.96%)</b></td><td>321.14 <b>(-42.56%)</b></td><td>265.00 <b>(-49.61%)</b></td><td>227.50 (-8.08%)</td><td>101.90 <b>(-65.62%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1033.70 (n/a)</td><td>559.08 (n/a)</td><td>525.90 (n/a)</td><td>247.50 (n/a)</td><td>296.40 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (-11.65%)</td><td>0.05 (-17.41%)</td><td>0.04 <b>(-25.79%)</b></td><td>0.02 <b>(-54.30%)</b></td><td>0.02 (+9.08%)</td><td>1085.00 <b>(+118.84%)</b></td><td>505.00 <b>(+40.94%)</b></td><td>415.20 <b>(+34.76%)</b></td><td>247.40 (+13.17%)</td><td>336.15 <b>(+164.56%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>495.80 (n/a)</td><td>358.30 (n/a)</td><td>308.10 (n/a)</td><td>218.60 (n/a)</td><td>127.06 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (+3.11%)</td><td>0.05 <b>(-22.51%)</b></td><td>0.04 <b>(-45.57%)</b></td><td>0.03 (-6.25%)</td><td>0.02 (-6.25%)</td><td>533.70 (+6.68%)</td><td>437.10 <b>(+27.06%)</b></td><td>475.40 <b>(+83.69%)</b></td><td>233.80 (-2.99%)</td><td>117.15 (-9.32%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>500.30 (n/a)</td><td>344.00 (n/a)</td><td>258.80 (n/a)</td><td>241.00 (n/a)</td><td>129.19 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 <b>(+43.79%)</b></td><td>0.05 (+13.52%)</td><td>0.04 (+4.41%)</td><td>0.03 (-11.82%)</td><td>0.03 <b>(+67.17%)</b></td><td>646.70 (+13.42%)</td><td>434.98 (-1.32%)</td><td>514.30 (-4.23%)</td><td>169.60 <b>(-30.43%)</b></td><td>196.83 <b>(+25.75%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>570.20 (n/a)</td><td>440.82 (n/a)</td><td>537.00 (n/a)</td><td>243.80 (n/a)</td><td>156.53 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 <b>(+42.18%)</b></td><td>0.05 (+18.86%)</td><td>0.05 <b>(+25.20%)</b></td><td>0.03 (-8.38%)</td><td>0.02 <b>(+137.90%)</b></td><td>561.20 (+9.16%)</td><td>416.20 (-11.18%)</td><td>398.60 <b>(-20.12%)</b></td><td>253.00 <b>(-29.66%)</b></td><td>115.55 <b>(+79.70%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>514.10 (n/a)</td><td>468.60 (n/a)</td><td>499.00 (n/a)</td><td>359.70 (n/a)</td><td>64.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 <b>(-31.59%)</b></td><td>0.04 (+7.10%)</td><td>0.04 (+6.31%)</td><td>0.04 <b>(+335.31%)</b></td><td>0.01 <b>(-78.19%)</b></td><td>494.90 <b>(-77.03%)</b></td><td>437.32 <b>(-43.47%)</b></td><td>423.20 (-5.93%)</td><td>385.70 <b>(+46.21%)</b></td><td>52.43 <b>(-93.31%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2154.40 (n/a)</td><td>773.60 (n/a)</td><td>449.90 (n/a)</td><td>263.80 (n/a)</td><td>783.91 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.32 <b>(-25.69%)</b></td><td>0.17 <b>(-30.78%)</b></td><td>0.17 (-19.97%)</td><td>0.04 (-4.31%)</td><td>0.13 (-18.87%)</td><td>2500.10 (+4.51%)</td><td>1116.66 <b>(+43.64%)</b></td><td>590.20 <b>(+24.96%)</b></td><td>308.70 <b>(+34.57%)</b></td><td>994.73 (+9.00%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.43 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>0.16 (n/a)</td><td>2392.30 (n/a)</td><td>777.38 (n/a)</td><td>472.30 (n/a)</td><td>229.40 (n/a)</td><td>912.56 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.42 <b>(+32.90%)</b></td><td>0.22 (-9.29%)</td><td>0.17 (-9.02%)</td><td>0.12 <b>(-33.53%)</b></td><td>0.12 <b>(+71.90%)</b></td><td>793.90 <b>(+50.45%)</b></td><td>539.84 <b>(+22.91%)</b></td><td>566.70 (+9.91%)</td><td>235.50 <b>(-24.76%)</b></td><td>206.89 <b>(+82.01%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>527.70 (n/a)</td><td>439.22 (n/a)</td><td>515.60 (n/a)</td><td>313.00 (n/a)</td><td>113.67 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.25 <b>(-21.13%)</b></td><td>0.18 (-1.12%)</td><td>0.20 (+4.15%)</td><td>0.05 <b>(-40.56%)</b></td><td>0.08 (-15.21%)</td><td>1959.60 <b>(+68.22%)</b></td><td>778.38 (+12.63%)</td><td>493.40 (-3.99%)</td><td>395.70 <b>(+26.79%)</b></td><td>666.07 <b>(+80.97%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.32 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>1164.90 (n/a)</td><td>691.10 (n/a)</td><td>513.90 (n/a)</td><td>312.10 (n/a)</td><td>368.07 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.28 (-0.95%)</td><td>0.16 (-8.22%)</td><td>0.17 (+10.12%)</td><td>0.04 <b>(-71.65%)</b></td><td>0.10 <b>(+53.72%)</b></td><td>1950.70 <b>(+252.75%)</b></td><td>727.64 <b>(+64.55%)</b></td><td>442.20 (-9.18%)</td><td>260.90 (+0.97%)</td><td>700.01 <b>(+498.99%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>553.00 (n/a)</td><td>442.20 (n/a)</td><td>486.90 (n/a)</td><td>258.40 (n/a)</td><td>116.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.35 (-4.14%)</td><td>0.16 <b>(-35.19%)</b></td><td>0.14 <b>(-49.27%)</b></td><td>0.04 <b>(-70.98%)</b></td><td>0.11 (+9.85%)</td><td>1988.40 <b>(+244.55%)</b></td><td>758.12 <b>(+114.86%)</b></td><td>526.60 <b>(+97.08%)</b></td><td>211.80 (+4.33%)</td><td>701.47 <b>(+317.66%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.36 (n/a)</td><td>0.25 (n/a)</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>577.10 (n/a)</td><td>352.84 (n/a)</td><td>267.20 (n/a)</td><td>203.00 (n/a)</td><td>167.95 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.36 <b>(+54.25%)</b></td><td>0.19 (+1.27%)</td><td>0.15 (-3.91%)</td><td>0.11 <b>(-29.87%)</b></td><td>0.10 <b>(+194.64%)</b></td><td>672.40 <b>(+42.58%)</b></td><td>472.98 (+14.26%)</td><td>477.70 (+4.07%)</td><td>203.70 <b>(-35.17%)</b></td><td>179.18 <b>(+153.26%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>471.60 (n/a)</td><td>413.94 (n/a)</td><td>459.00 (n/a)</td><td>314.20 (n/a)</td><td>70.75 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (-1.09%)</td><td>0.11 (+12.57%)</td><td>0.13 <b>(+67.66%)</b></td><td>0.04 <b>(-41.48%)</b></td><td>0.04 (+6.26%)</td><td>996.00 <b>(+70.87%)</b></td><td>431.72 (+0.71%)</td><td>290.30 <b>(-40.35%)</b></td><td>253.60 (+1.12%)</td><td>316.72 <b>(+102.90%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>582.90 (n/a)</td><td>428.68 (n/a)</td><td>486.70 (n/a)</td><td>250.80 (n/a)</td><td>156.10 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 (-0.31%)</td><td>0.09 (-16.78%)</td><td>0.08 <b>(-30.62%)</b></td><td>0.02 <b>(-72.09%)</b></td><td>0.05 <b>(+38.00%)</b></td><td>1895.20 <b>(+258.26%)</b></td><td>679.42 <b>(+76.13%)</b></td><td>455.40 <b>(+44.11%)</b></td><td>264.00 (+0.34%)</td><td>684.96 <b>(+419.71%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>529.00 (n/a)</td><td>385.74 (n/a)</td><td>316.00 (n/a)</td><td>263.10 (n/a)</td><td>131.80 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 (-14.46%)</td><td>0.10 (-17.18%)</td><td>0.08 <b>(-37.72%)</b></td><td>0.07 <b>(+30.24%)</b></td><td>0.03 <b>(-41.05%)</b></td><td>495.20 <b>(-23.21%)</b></td><td>407.74 (+9.39%)</td><td>452.30 <b>(+60.62%)</b></td><td>272.50 (+16.90%)</td><td>94.41 <b>(-46.15%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>644.90 (n/a)</td><td>372.74 (n/a)</td><td>281.60 (n/a)</td><td>233.10 (n/a)</td><td>175.32 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (-1.71%)</td><td>0.09 (+4.34%)</td><td>0.07 (+1.10%)</td><td>0.06 (+3.22%)</td><td>0.04 (-2.19%)</td><td>602.20 (-3.12%)</td><td>446.54 (-4.34%)</td><td>515.50 (-1.09%)</td><td>252.00 (+1.78%)</td><td>143.36 (-0.47%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>621.60 (n/a)</td><td>466.78 (n/a)</td><td>521.20 (n/a)</td><td>247.60 (n/a)</td><td>144.05 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 <b>(-43.44%)</b></td><td>0.08 (-2.06%)</td><td>0.09 (+15.94%)</td><td>0.07 <b>(+42.68%)</b></td><td>0.01 <b>(-75.83%)</b></td><td>544.40 <b>(-29.92%)</b></td><td>443.04 (-15.83%)</td><td>428.50 (-13.75%)</td><td>361.50 <b>(+76.77%)</b></td><td>69.85 <b>(-67.86%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>776.80 (n/a)</td><td>526.34 (n/a)</td><td>496.80 (n/a)</td><td>204.50 (n/a)</td><td>217.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.09 <b>(-29.20%)</b></td><td>0.07 (-8.70%)</td><td>0.07 (+2.80%)</td><td>0.05 (-7.88%)</td><td>0.02 <b>(-44.98%)</b></td><td>783.50 (+8.56%)</td><td>561.12 (+4.87%)</td><td>535.60 (-2.72%)</td><td>410.70 <b>(+41.23%)</b></td><td>143.31 (-7.70%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>721.70 (n/a)</td><td>535.06 (n/a)</td><td>550.60 (n/a)</td><td>290.80 (n/a)</td><td>155.26 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.18 (-0.66%)</td><td>0.12 (-6.65%)</td><td>0.11 <b>(-30.62%)</b></td><td>0.08 (+7.44%)</td><td>0.04 <b>(-26.93%)</b></td><td>514.60 (-6.93%)</td><td>364.88 (-1.03%)</td><td>382.60 <b>(+44.16%)</b></td><td>231.60 (+0.70%)</td><td>105.23 <b>(-36.16%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>552.90 (n/a)</td><td>368.68 (n/a)</td><td>265.40 (n/a)</td><td>230.00 (n/a)</td><td>164.84 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (-2.13%)</td><td>0.12 (+4.57%)</td><td>0.13 (-0.72%)</td><td>0.07 (-0.83%)</td><td>0.03 (-9.30%)</td><td>611.00 (+0.84%)</td><td>359.96 (-5.16%)</td><td>304.20 (+0.73%)</td><td>264.80 (+2.16%)</td><td>141.67 (-0.78%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>605.90 (n/a)</td><td>379.54 (n/a)</td><td>302.00 (n/a)</td><td>259.20 (n/a)</td><td>142.79 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 <b>(-42.11%)</b></td><td>0.09 <b>(-37.67%)</b></td><td>0.08 <b>(-37.81%)</b></td><td>0.07 <b>(-27.77%)</b></td><td>0.02 <b>(-51.45%)</b></td><td>601.40 <b>(+38.48%)</b></td><td>473.28 <b>(+56.59%)</b></td><td>490.60 <b>(+60.80%)</b></td><td>377.70 <b>(+72.78%)</b></td><td>92.80 (+11.61%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>434.30 (n/a)</td><td>302.24 (n/a)</td><td>305.10 (n/a)</td><td>218.60 (n/a)</td><td>83.15 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.17 (-5.05%)</td><td>0.15 <b>(+26.23%)</b></td><td>0.15 (+5.81%)</td><td>0.13 <b>(+249.16%)</b></td><td>0.01 <b>(-75.55%)</b></td><td>304.60 <b>(-71.36%)</b></td><td>277.94 <b>(-41.09%)</b></td><td>272.20 (-5.49%)</td><td>247.80 (+5.31%)</td><td>25.65 <b>(-92.60%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>1063.40 (n/a)</td><td>471.80 (n/a)</td><td>288.00 (n/a)</td><td>235.30 (n/a)</td><td>346.75 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (-7.14%)</td><td>0.12 (+11.96%)</td><td>0.12 <b>(+39.69%)</b></td><td>0.09 <b>(+55.23%)</b></td><td>0.03 <b>(-37.20%)</b></td><td>477.40 <b>(-35.58%)</b></td><td>367.74 (-19.15%)</td><td>345.90 <b>(-28.41%)</b></td><td>269.60 (+7.67%)</td><td>87.70 <b>(-54.46%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>741.10 (n/a)</td><td>454.84 (n/a)</td><td>483.20 (n/a)</td><td>250.40 (n/a)</td><td>192.58 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.16 (-9.78%)</td><td>0.10 (+6.32%)</td><td>0.10 (+18.28%)</td><td>0.03 <b>(+48.98%)</b></td><td>0.05 (-10.16%)</td><td>1311.70 <b>(-32.88%)</b></td><td>554.32 <b>(-20.84%)</b></td><td>395.10 (-15.45%)</td><td>250.10 (+10.86%)</td><td>436.51 <b>(-38.43%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1954.20 (n/a)</td><td>700.22 (n/a)</td><td>467.30 (n/a)</td><td>225.60 (n/a)</td><td>709.02 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (-4.79%)</td><td>0.08 (-19.16%)</td><td>0.07 <b>(-35.06%)</b></td><td>0.05 (-16.14%)</td><td>0.03 (-0.90%)</td><td>684.30 (+19.26%)</td><td>495.78 <b>(+26.42%)</b></td><td>509.60 <b>(+54.00%)</b></td><td>270.20 (+5.01%)</td><td>180.80 <b>(+25.42%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>573.80 (n/a)</td><td>392.16 (n/a)</td><td>330.90 (n/a)</td><td>257.30 (n/a)</td><td>144.15 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (+1.91%)</td><td>0.10 (+1.05%)</td><td>0.09 (-18.01%)</td><td>0.08 <b>(+29.11%)</b></td><td>0.02 <b>(-20.82%)</b></td><td>432.20 <b>(-22.54%)</b></td><td>359.28 (-5.35%)</td><td>388.40 <b>(+21.95%)</b></td><td>259.00 (-1.89%)</td><td>80.61 <b>(-38.63%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>558.00 (n/a)</td><td>379.60 (n/a)</td><td>318.50 (n/a)</td><td>264.00 (n/a)</td><td>131.36 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 <b>(-38.68%)</b></td><td>0.08 <b>(-25.43%)</b></td><td>0.08 <b>(-29.79%)</b></td><td>0.06 (+1.08%)</td><td>0.01 <b>(-69.79%)</b></td><td>541.60 (-1.06%)</td><td>461.66 <b>(+25.50%)</b></td><td>431.20 <b>(+42.45%)</b></td><td>413.90 <b>(+63.08%)</b></td><td>57.47 <b>(-52.47%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>547.40 (n/a)</td><td>367.86 (n/a)</td><td>302.70 (n/a)</td><td>253.80 (n/a)</td><td>120.93 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (-15.64%)</td><td>0.08 <b>(-25.35%)</b></td><td>0.07 <b>(-46.27%)</b></td><td>0.06 <b>(-25.22%)</b></td><td>0.03 (-10.21%)</td><td>605.20 <b>(+33.72%)</b></td><td>459.00 <b>(+35.65%)</b></td><td>514.40 <b>(+86.11%)</b></td><td>300.20 (+18.52%)</td><td>131.68 <b>(+35.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>452.60 (n/a)</td><td>338.38 (n/a)</td><td>276.40 (n/a)</td><td>253.30 (n/a)</td><td>96.95 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 <b>(+33.72%)</b></td><td>0.07 (+6.95%)</td><td>0.07 (-5.09%)</td><td>0.03 (-4.14%)</td><td>0.03 <b>(+50.41%)</b></td><td>1042.30 (+4.32%)</td><td>555.76 (-0.40%)</td><td>483.50 (+5.36%)</td><td>309.90 <b>(-25.24%)</b></td><td>288.69 (+16.36%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>999.10 (n/a)</td><td>558.00 (n/a)</td><td>458.90 (n/a)</td><td>414.50 (n/a)</td><td>248.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 <b>(-21.07%)</b></td><td>0.09 (-0.25%)</td><td>0.08 (+17.63%)</td><td>0.06 (+4.28%)</td><td>0.02 <b>(-40.91%)</b></td><td>588.30 (-4.11%)</td><td>424.32 (-5.35%)</td><td>416.70 (-14.98%)</td><td>294.40 <b>(+26.68%)</b></td><td>108.38 <b>(-23.16%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>613.50 (n/a)</td><td>448.32 (n/a)</td><td>490.10 (n/a)</td><td>232.40 (n/a)</td><td>141.05 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.53 (+2.48%)</td><td>0.40 (+12.70%)</td><td>0.41 (+10.10%)</td><td>0.24 (+12.68%)</td><td>0.11 (-7.97%)</td><td>550.40 (-11.25%)</td><td>350.02 (-13.02%)</td><td>316.40 (-9.18%)</td><td>248.10 (-2.40%)</td><td>116.66 (-17.14%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.52 (n/a)</td><td>0.36 (n/a)</td><td>0.38 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>620.20 (n/a)</td><td>402.40 (n/a)</td><td>348.40 (n/a)</td><td>254.20 (n/a)</td><td>140.79 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.60 (+6.14%)</td><td>0.37 (+5.16%)</td><td>0.27 <b>(-25.25%)</b></td><td>0.26 (+16.38%)</td><td>0.15 (+12.92%)</td><td>510.10 (-14.07%)</td><td>393.56 (-4.25%)</td><td>477.70 <b>(+33.77%)</b></td><td>220.10 (-5.78%)</td><td>133.59 (-8.19%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.56 (n/a)</td><td>0.36 (n/a)</td><td>0.37 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>593.60 (n/a)</td><td>411.02 (n/a)</td><td>357.10 (n/a)</td><td>233.60 (n/a)</td><td>145.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.53 <b>(+110.16%)</b></td><td>0.34 <b>(+73.13%)</b></td><td>0.27 (+19.81%)</td><td>0.24 <b>(+342.73%)</b></td><td>0.12 <b>(+51.80%)</b></td><td>550.20 <b>(-77.41%)</b></td><td>417.32 <b>(-55.31%)</b></td><td>484.00 (-16.54%)</td><td>248.80 <b>(-52.42%)</b></td><td>129.50 <b>(-84.59%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>0.08 (n/a)</td><td>2435.90 (n/a)</td><td>933.72 (n/a)</td><td>579.90 (n/a)</td><td>522.90 (n/a)</td><td>840.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (+13.37%)</td><td>0.01 (-2.00%)</td><td>0.01 (+2.95%)</td><td>0.01 <b>(-21.77%)</b></td><td>0.00 <b>(+50.91%)</b></td><td>653.70 <b>(+27.83%)</b></td><td>408.72 (+12.04%)</td><td>300.20 (-2.88%)</td><td>243.30 (-11.82%)</td><td>186.56 <b>(+76.86%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.40 (n/a)</td><td>364.80 (n/a)</td><td>309.10 (n/a)</td><td>275.90 (n/a)</td><td>105.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (-18.35%)</td><td>0.01 (+0.57%)</td><td>0.01 (-10.76%)</td><td>0.01 <b>(+43.63%)</b></td><td>0.00 <b>(-25.59%)</b></td><td>519.00 <b>(-30.37%)</b></td><td>415.88 (-6.83%)</td><td>477.50 (+12.06%)</td><td>275.00 <b>(+22.44%)</b></td><td>121.55 <b>(-35.33%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>745.40 (n/a)</td><td>446.38 (n/a)</td><td>426.10 (n/a)</td><td>224.60 (n/a)</td><td>187.94 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (+9.32%)</td><td>0.01 (-11.77%)</td><td>0.01 <b>(-47.35%)</b></td><td>0.01 (-9.26%)</td><td>0.01 <b>(+30.39%)</b></td><td>547.60 (+10.23%)</td><td>422.54 <b>(+20.92%)</b></td><td>535.80 <b>(+89.93%)</b></td><td>220.30 (-8.51%)</td><td>165.07 <b>(+34.93%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.80 (n/a)</td><td>349.44 (n/a)</td><td>282.10 (n/a)</td><td>240.80 (n/a)</td><td>122.34 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>8.83 (+12.40%)</td><td>7.54 <b>(+20.40%)</b></td><td>7.75 (+9.82%)</td><td>5.18 <b>(+65.53%)</b></td><td>1.39 <b>(-26.30%)</b></td><td>405.10 <b>(-39.58%)</b></td><td>288.22 <b>(-23.15%)</b></td><td>270.80 (-8.94%)</td><td>237.70 (-11.01%)</td><td>66.75 <b>(-60.34%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>7.85 (n/a)</td><td>6.26 (n/a)</td><td>7.06 (n/a)</td><td>3.13 (n/a)</td><td>1.89 (n/a)</td><td>670.50 (n/a)</td><td>375.06 (n/a)</td><td>297.40 (n/a)</td><td>267.10 (n/a)</td><td>168.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.55 <b>(+20.64%)</b></td><td>0.38 <b>(+32.21%)</b></td><td>0.45 <b>(+41.96%)</b></td><td>0.13 <b>(+78.80%)</b></td><td>0.20 <b>(+40.68%)</b></td><td>1008.70 <b>(-44.07%)</b></td><td>479.18 <b>(-29.83%)</b></td><td>294.70 <b>(-29.55%)</b></td><td>238.60 (-17.12%)</td><td>334.68 <b>(-46.94%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.46 (n/a)</td><td>0.29 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>0.14 (n/a)</td><td>1803.50 (n/a)</td><td>682.88 (n/a)</td><td>418.30 (n/a)</td><td>287.90 (n/a)</td><td>630.74 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.50 (+0.46%)</td><td>0.40 <b>(+25.57%)</b></td><td>0.45 <b>(+41.57%)</b></td><td>0.28 <b>(+294.51%)</b></td><td>0.10 <b>(-35.44%)</b></td><td>466.50 <b>(-74.65%)</b></td><td>347.92 <b>(-46.85%)</b></td><td>291.10 <b>(-29.38%)</b></td><td>266.40 (-0.49%)</td><td>96.59 <b>(-85.50%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.49 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>1840.50 (n/a)</td><td>654.64 (n/a)</td><td>412.20 (n/a)</td><td>267.70 (n/a)</td><td>666.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.49 (-16.23%)</td><td>0.43 (-1.93%)</td><td>0.45 (-8.58%)</td><td>0.27 (+12.89%)</td><td>0.09 <b>(-39.47%)</b></td><td>493.50 (-11.42%)</td><td>324.32 (-4.82%)</td><td>291.80 (+9.37%)</td><td>268.70 (+19.37%)</td><td>95.13 <b>(-33.06%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.59 (n/a)</td><td>0.44 (n/a)</td><td>0.50 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>557.10 (n/a)</td><td>340.74 (n/a)</td><td>266.80 (n/a)</td><td>225.10 (n/a)</td><td>142.11 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.54 (-9.07%)</td><td>0.32 <b>(-22.16%)</b></td><td>0.33 (+1.57%)</td><td>0.06 <b>(-74.33%)</b></td><td>0.17 (+7.81%)</td><td>2051.70 <b>(+289.61%)</b></td><td>702.46 <b>(+92.74%)</b></td><td>401.70 (-1.54%)</td><td>244.90 (+9.97%)</td><td>757.48 <b>(+479.37%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.59 (n/a)</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>526.60 (n/a)</td><td>364.46 (n/a)</td><td>408.00 (n/a)</td><td>222.70 (n/a)</td><td>130.74 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.45 <b>(-20.39%)</b></td><td>0.34 <b>(-21.66%)</b></td><td>0.35 <b>(-28.63%)</b></td><td>0.22 (+7.45%)</td><td>0.09 <b>(-32.44%)</b></td><td>591.70 (-6.94%)</td><td>410.96 (+19.92%)</td><td>380.60 <b>(+40.13%)</b></td><td>295.50 <b>(+25.58%)</b></td><td>123.24 <b>(-26.10%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.49 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>635.80 (n/a)</td><td>342.70 (n/a)</td><td>271.60 (n/a)</td><td>235.30 (n/a)</td><td>166.76 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (-17.11%)</td><td>0.01 (+3.86%)</td><td>0.01 <b>(+42.90%)</b></td><td>0.01 <b>(+44.89%)</b></td><td>0.00 <b>(-29.97%)</b></td><td>569.10 <b>(-30.98%)</b></td><td>392.08 (-13.51%)</td><td>296.80 <b>(-30.03%)</b></td><td>280.50 <b>(+20.65%)</b></td><td>141.05 <b>(-40.45%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>824.60 (n/a)</td><td>453.30 (n/a)</td><td>424.20 (n/a)</td><td>232.50 (n/a)</td><td>236.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 <b>(+32.89%)</b></td><td>0.01 (+13.89%)</td><td>0.01 (-16.81%)</td><td>0.01 (+5.45%)</td><td>0.00 <b>(+112.89%)</b></td><td>476.30 (-5.18%)</td><td>381.76 (-6.58%)</td><td>458.80 <b>(+20.23%)</b></td><td>244.60 <b>(-24.76%)</b></td><td>118.78 <b>(+50.10%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>502.30 (n/a)</td><td>408.64 (n/a)</td><td>381.60 (n/a)</td><td>325.10 (n/a)</td><td>79.14 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.00 (+0.00%)</td><td>0.00 (+9.09%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+22.47%)</b></td><td>19881.83 (-10.61%)</td><td>17247.39 (-10.70%)</td><td>17209.68 (-16.84%)</td><td>15581.14 (-2.61%)</td><td>1627.87 <b>(-40.95%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22241.06 (n/a)</td><td>19313.73 (n/a)</td><td>20695.25 (n/a)</td><td>15998.37 (n/a)</td><td>2756.56 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.00 <b>(+40.00%)</b></td><td>0.00 <b>(+115.38%)</b></td><td>0.00 <b>(+225.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+52.30%)</b></td><td>22012.64 (-1.98%)</td><td>9463.46 <b>(-48.66%)</b></td><td>6358.95 <b>(-68.04%)</b></td><td>5915.63 <b>(-28.77%)</b></td><td>7020.99 <b>(+21.19%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22456.26 (n/a)</td><td>18434.50 (n/a)</td><td>19898.22 (n/a)</td><td>8305.52 (n/a)</td><td>5793.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (+17.47%)</td><td>0.09 (+4.43%)</td><td>0.08 (-5.08%)</td><td>0.07 (+10.84%)</td><td>0.03 <b>(+37.02%)</b></td><td>28493.21 (-9.74%)</td><td>24709.67 (-2.18%)</td><td>26749.72 (+5.35%)</td><td>14180.70 (-14.90%)</td><td>5930.09 (+4.43%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>31566.21 (n/a)</td><td>25259.88 (n/a)</td><td>25390.65 (n/a)</td><td>16662.95 (n/a)</td><td>5678.38 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 <b>(-47.71%)</b></td><td>0.08 <b>(-33.96%)</b></td><td>0.08 <b>(-37.45%)</b></td><td>0.07 (+1.61%)</td><td>0.00 <b>(-87.14%)</b></td><td>30181.70 (-1.51%)</td><td>27387.49 <b>(+38.97%)</b></td><td>27235.58 <b>(+59.91%)</b></td><td>25546.82 <b>(+91.29%)</b></td><td>1707.85 <b>(-75.67%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>30644.45 (n/a)</td><td>19707.87 (n/a)</td><td>17031.77 (n/a)</td><td>13354.90 (n/a)</td><td>7019.95 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.62 (+12.42%)</td><td>1.55 (-2.35%)</td><td>1.44 (-2.50%)</td><td>0.30 <b>(-43.90%)</b></td><td>0.87 <b>(+20.68%)</b></td><td>3506.10 <b>(+78.26%)</b></td><td>1184.92 <b>(+36.26%)</b></td><td>726.70 (+2.57%)</td><td>400.40 (-11.04%)</td><td>1306.79 <b>(+108.29%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.33 (n/a)</td><td>1.59 (n/a)</td><td>1.48 (n/a)</td><td>0.53 (n/a)</td><td>0.72 (n/a)</td><td>1966.90 (n/a)</td><td>869.58 (n/a)</td><td>708.50 (n/a)</td><td>450.10 (n/a)</td><td>627.39 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.37 (+7.68%)</td><td>1.92 (+0.07%)</td><td>1.94 (+19.08%)</td><td>0.30 <b>(-45.42%)</b></td><td>1.13 (+10.11%)</td><td>3505.20 <b>(+83.21%)</b></td><td>1093.58 <b>(+38.15%)</b></td><td>541.00 (-16.02%)</td><td>311.40 (-7.13%)</td><td>1354.93 <b>(+109.94%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.13 (n/a)</td><td>1.91 (n/a)</td><td>1.63 (n/a)</td><td>0.55 (n/a)</td><td>1.03 (n/a)</td><td>1913.20 (n/a)</td><td>791.58 (n/a)</td><td>644.20 (n/a)</td><td>335.30 (n/a)</td><td>645.38 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.28 <b>(+53.50%)</b></td><td>1.91 (+19.80%)</td><td>1.66 (+5.83%)</td><td>0.30 <b>(-68.91%)</b></td><td>1.30 <b>(+208.56%)</b></td><td>3439.90 <b>(+221.61%)</b></td><td>1128.40 <b>(+60.80%)</b></td><td>631.60 (-5.52%)</td><td>319.60 <b>(-34.86%)</b></td><td>1315.69 <b>(+499.41%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.14 (n/a)</td><td>1.60 (n/a)</td><td>1.57 (n/a)</td><td>0.98 (n/a)</td><td>0.42 (n/a)</td><td>1069.60 (n/a)</td><td>701.72 (n/a)</td><td>668.50 (n/a)</td><td>490.60 (n/a)</td><td>219.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.08 <b>(-42.68%)</b></td><td>1.60 (-19.50%)</td><td>1.58 (-13.34%)</td><td>1.21 (+18.63%)</td><td>0.31 <b>(-68.83%)</b></td><td>863.40 (-15.70%)</td><td>673.88 (+7.15%)</td><td>665.70 (+15.39%)</td><td>504.00 <b>(+74.45%)</b></td><td>129.01 <b>(-53.41%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.63 (n/a)</td><td>1.99 (n/a)</td><td>1.82 (n/a)</td><td>1.02 (n/a)</td><td>1.00 (n/a)</td><td>1024.20 (n/a)</td><td>628.92 (n/a)</td><td>576.90 (n/a)</td><td>288.90 (n/a)</td><td>276.89 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.30 (+5.04%)</td><td>2.13 <b>(+36.42%)</b></td><td>2.46 <b>(+152.43%)</b></td><td>0.66 (+6.25%)</td><td>1.20 (+9.87%)</td><td>3178.50 (-5.88%)</td><td>1445.14 <b>(-25.07%)</b></td><td>851.80 <b>(-60.39%)</b></td><td>635.80 (-4.79%)</td><td>1097.51 (-2.63%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.14 (n/a)</td><td>1.56 (n/a)</td><td>0.98 (n/a)</td><td>0.62 (n/a)</td><td>1.09 (n/a)</td><td>3377.10 (n/a)</td><td>1928.74 (n/a)</td><td>2150.20 (n/a)</td><td>667.80 (n/a)</td><td>1127.18 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.75 <b>(+22.57%)</b></td><td>2.63 (+8.23%)</td><td>3.19 <b>(+20.04%)</b></td><td>0.60 <b>(-45.79%)</b></td><td>1.35 <b>(+74.89%)</b></td><td>3467.30 <b>(+84.46%)</b></td><td>1268.68 <b>(+28.34%)</b></td><td>656.40 (-16.69%)</td><td>559.50 (-18.42%)</td><td>1248.19 <b>(+148.38%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.06 (n/a)</td><td>2.43 (n/a)</td><td>2.66 (n/a)</td><td>1.12 (n/a)</td><td>0.77 (n/a)</td><td>1879.70 (n/a)</td><td>988.50 (n/a)</td><td>787.90 (n/a)</td><td>685.80 (n/a)</td><td>502.52 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>4.54 (-5.00%)</td><td>2.56 (-11.02%)</td><td>2.59 <b>(-38.44%)</b></td><td>0.60 (+1.45%)</td><td>1.41 <b>(-32.77%)</b></td><td>3468.00 (-1.43%)</td><td>1282.16 <b>(-23.46%)</b></td><td>809.40 <b>(+62.43%)</b></td><td>462.10 (+5.26%)</td><td>1234.06 <b>(-24.72%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>4.78 (n/a)</td><td>2.88 (n/a)</td><td>4.21 (n/a)</td><td>0.60 (n/a)</td><td>2.09 (n/a)</td><td>3518.40 (n/a)</td><td>1675.12 (n/a)</td><td>498.30 (n/a)</td><td>439.00 (n/a)</td><td>1639.39 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>5.80 (-6.87%)</td><td>4.34 (+19.55%)</td><td>4.14 (+17.69%)</td><td>2.53 <b>(+292.36%)</b></td><td>1.36 <b>(-40.85%)</b></td><td>828.00 <b>(-74.51%)</b></td><td>528.32 <b>(-51.84%)</b></td><td>506.90 (-15.04%)</td><td>361.80 (+7.36%)</td><td>188.82 <b>(-84.59%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>6.22 (n/a)</td><td>3.63 (n/a)</td><td>3.51 (n/a)</td><td>0.65 (n/a)</td><td>2.29 (n/a)</td><td>3248.80 (n/a)</td><td>1097.00 (n/a)</td><td>596.60 (n/a)</td><td>337.00 (n/a)</td><td>1224.99 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>5.76 <b>(+44.82%)</b></td><td>3.82 <b>(+51.17%)</b></td><td>4.77 <b>(+74.39%)</b></td><td>0.59 (-10.10%)</td><td>2.19 <b>(+47.66%)</b></td><td>3571.80 (+11.23%)</td><td>1115.24 (-14.95%)</td><td>439.20 <b>(-42.66%)</b></td><td>363.90 <b>(-30.95%)</b></td><td>1385.27 <b>(+22.01%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.98 (n/a)</td><td>2.53 (n/a)</td><td>2.74 (n/a)</td><td>0.65 (n/a)</td><td>1.48 (n/a)</td><td>3211.20 (n/a)</td><td>1311.24 (n/a)</td><td>766.00 (n/a)</td><td>527.00 (n/a)</td><td>1135.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>6.46 <b>(+121.18%)</b></td><td>4.00 <b>(+73.14%)</b></td><td>3.58 <b>(+31.51%)</b></td><td>2.09 <b>(+109.88%)</b></td><td>1.73 <b>(+116.31%)</b></td><td>1001.20 <b>(-52.36%)</b></td><td>611.18 <b>(-42.70%)</b></td><td>586.20 <b>(-23.96%)</b></td><td>324.70 <b>(-54.78%)</b></td><td>266.19 <b>(-54.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.92 (n/a)</td><td>2.31 (n/a)</td><td>2.72 (n/a)</td><td>1.00 (n/a)</td><td>0.80 (n/a)</td><td>2101.40 (n/a)</td><td>1066.60 (n/a)</td><td>770.90 (n/a)</td><td>718.10 (n/a)</td><td>589.27 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>4.05 (+7.56%)</td><td>3.46 <b>(+48.55%)</b></td><td>3.66 <b>(+75.73%)</b></td><td>2.12 <b>(+74.10%)</b></td><td>0.79 <b>(-22.16%)</b></td><td>1981.50 <b>(-42.56%)</b></td><td>1284.32 <b>(-38.98%)</b></td><td>1147.00 <b>(-43.09%)</b></td><td>1036.50 (-7.02%)</td><td>396.47 <b>(-56.94%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>3.76 (n/a)</td><td>2.33 (n/a)</td><td>2.08 (n/a)</td><td>1.22 (n/a)</td><td>1.01 (n/a)</td><td>3449.70 (n/a)</td><td>2104.80 (n/a)</td><td>2015.60 (n/a)</td><td>1114.80 (n/a)</td><td>920.77 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>6.65 (-6.46%)</td><td>4.62 (+18.04%)</td><td>4.62 (+16.71%)</td><td>1.13 (-4.76%)</td><td>2.15 <b>(-20.27%)</b></td><td>3715.70 (+5.00%)</td><td>1371.12 <b>(-25.11%)</b></td><td>907.10 (-14.32%)</td><td>630.40 (+6.92%)</td><td>1316.73 (-9.18%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>7.11 (n/a)</td><td>3.91 (n/a)</td><td>3.96 (n/a)</td><td>1.19 (n/a)</td><td>2.69 (n/a)</td><td>3538.80 (n/a)</td><td>1830.94 (n/a)</td><td>1058.70 (n/a)</td><td>589.60 (n/a)</td><td>1449.77 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>6.75 (+8.95%)</td><td>5.12 <b>(+25.84%)</b></td><td>4.64 (+2.46%)</td><td>3.95 <b>(+260.15%)</b></td><td>1.33 <b>(-31.05%)</b></td><td>1062.30 <b>(-72.23%)</b></td><td>862.42 <b>(-42.23%)</b></td><td>903.80 (-2.40%)</td><td>621.10 (-8.22%)</td><td>211.67 <b>(-83.94%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>6.20 (n/a)</td><td>4.07 (n/a)</td><td>4.53 (n/a)</td><td>1.10 (n/a)</td><td>1.93 (n/a)</td><td>3825.90 (n/a)</td><td>1492.92 (n/a)</td><td>926.00 (n/a)</td><td>676.70 (n/a)</td><td>1318.37 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>9.27 (+7.94%)</td><td>6.78 (-0.79%)</td><td>6.84 (-0.86%)</td><td>4.09 (-3.32%)</td><td>1.85 (+1.25%)</td><td>1025.70 (+3.43%)</td><td>663.58 (+1.04%)</td><td>613.10 (+0.87%)</td><td>452.50 (-7.35%)</td><td>215.50 (+3.95%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>8.59 (n/a)</td><td>6.84 (n/a)</td><td>6.90 (n/a)</td><td>4.23 (n/a)</td><td>1.83 (n/a)</td><td>991.70 (n/a)</td><td>656.78 (n/a)</td><td>607.80 (n/a)</td><td>488.40 (n/a)</td><td>207.32 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>9.44 (+8.50%)</td><td>6.64 (-6.21%)</td><td>7.66 (-1.70%)</td><td>3.93 (-1.55%)</td><td>2.55 <b>(+38.90%)</b></td><td>1067.00 (+1.57%)</td><td>727.06 (+13.50%)</td><td>547.60 (+1.73%)</td><td>444.30 (-7.84%)</td><td>311.93 <b>(+33.65%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>8.70 (n/a)</td><td>7.08 (n/a)</td><td>7.79 (n/a)</td><td>3.99 (n/a)</td><td>1.84 (n/a)</td><td>1050.50 (n/a)</td><td>640.60 (n/a)</td><td>538.30 (n/a)</td><td>482.10 (n/a)</td><td>233.39 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>8.81 (-14.63%)</td><td>7.53 <b>(+30.26%)</b></td><td>7.59 (+18.10%)</td><td>6.15 <b>(+436.50%)</b></td><td>1.17 <b>(-66.38%)</b></td><td>682.00 <b>(-81.36%)</b></td><td>567.86 <b>(-55.63%)</b></td><td>553.00 (-15.31%)</td><td>476.20 (+17.15%)</td><td>89.97 <b>(-93.36%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>10.32 (n/a)</td><td>5.78 (n/a)</td><td>6.42 (n/a)</td><td>1.15 (n/a)</td><td>3.48 (n/a)</td><td>3659.00 (n/a)</td><td>1279.72 (n/a)</td><td>653.00 (n/a)</td><td>406.50 (n/a)</td><td>1354.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.55 (+5.34%)</td><td>0.96 (-3.19%)</td><td>0.88 <b>(-30.67%)</b></td><td>0.60 <b>(+294.36%)</b></td><td>0.38 <b>(-32.20%)</b></td><td>867.30 <b>(-74.64%)</b></td><td>609.94 <b>(-42.74%)</b></td><td>598.40 <b>(+44.23%)</b></td><td>338.20 (-5.05%)</td><td>211.95 <b>(-84.02%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.47 (n/a)</td><td>0.99 (n/a)</td><td>1.26 (n/a)</td><td>0.15 (n/a)</td><td>0.56 (n/a)</td><td>3420.30 (n/a)</td><td>1065.12 (n/a)</td><td>414.90 (n/a)</td><td>356.20 (n/a)</td><td>1326.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.30 (-10.32%)</td><td>1.87 <b>(+26.29%)</b></td><td>2.06 <b>(+35.29%)</b></td><td>0.98 <b>(+230.43%)</b></td><td>0.53 <b>(-34.67%)</b></td><td>1069.40 <b>(-69.74%)</b></td><td>617.54 <b>(-48.74%)</b></td><td>510.10 <b>(-26.08%)</b></td><td>455.40 (+11.51%)</td><td>256.26 <b>(-80.41%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.57 (n/a)</td><td>1.48 (n/a)</td><td>1.52 (n/a)</td><td>0.30 (n/a)</td><td>0.81 (n/a)</td><td>3533.70 (n/a)</td><td>1204.80 (n/a)</td><td>690.10 (n/a)</td><td>408.40 (n/a)</td><td>1308.00 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.20 <b>(+38.12%)</b></td><td>2.23 <b>(+66.45%)</b></td><td>2.21 <b>(+94.59%)</b></td><td>0.59 (+1.36%)</td><td>1.04 <b>(+34.98%)</b></td><td>3548.70 (-1.34%)</td><td>1368.64 <b>(-34.32%)</b></td><td>947.10 <b>(-48.61%)</b></td><td>655.10 <b>(-27.60%)</b></td><td>1228.10 (+3.85%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>2.32 (n/a)</td><td>1.34 (n/a)</td><td>1.14 (n/a)</td><td>0.58 (n/a)</td><td>0.77 (n/a)</td><td>3597.00 (n/a)</td><td>2083.88 (n/a)</td><td>1843.00 (n/a)</td><td>904.80 (n/a)</td><td>1182.52 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.76 (+14.57%)</td><td>1.00 (-8.61%)</td><td>1.06 (+3.94%)</td><td>0.28 <b>(-70.70%)</b></td><td>0.58 <b>(+132.89%)</b></td><td>1881.40 <b>(+241.27%)</b></td><td>785.68 <b>(+58.86%)</b></td><td>496.70 (-3.80%)</td><td>298.40 (-12.72%)</td><td>646.03 <b>(+642.51%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>1.53 (n/a)</td><td>1.09 (n/a)</td><td>1.02 (n/a)</td><td>0.95 (n/a)</td><td>0.25 (n/a)</td><td>551.30 (n/a)</td><td>494.58 (n/a)</td><td>516.30 (n/a)</td><td>341.90 (n/a)</td><td>87.01 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (+0.29%)</td><td>0.09 (-0.93%)</td><td>0.08 (-1.76%)</td><td>0.06 (-14.23%)</td><td>0.03 (+8.54%)</td><td>561.30 (+16.60%)</td><td>406.50 (+2.64%)</td><td>427.70 (+1.78%)</td><td>254.10 (-0.27%)</td><td>115.57 <b>(+23.06%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>481.40 (n/a)</td><td>396.04 (n/a)</td><td>420.20 (n/a)</td><td>254.80 (n/a)</td><td>93.92 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (-3.40%)</td><td>0.09 (+4.60%)</td><td>0.10 <b>(+20.77%)</b></td><td>0.06 (+12.20%)</td><td>0.03 (-14.99%)</td><td>520.40 (-10.88%)</td><td>372.20 (-7.14%)</td><td>316.60 (-17.21%)</td><td>274.50 (+3.51%)</td><td>114.06 (-18.84%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>583.90 (n/a)</td><td>400.80 (n/a)</td><td>382.40 (n/a)</td><td>265.20 (n/a)</td><td>140.54 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.24 (-3.96%)</td><td>0.17 (-13.64%)</td><td>0.16 <b>(-23.24%)</b></td><td>0.11 (-3.64%)</td><td>0.06 (+16.95%)</td><td>585.70 (+3.77%)</td><td>415.04 (+18.67%)</td><td>401.80 <b>(+30.29%)</b></td><td>271.20 (+4.11%)</td><td>141.70 (+16.01%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>564.40 (n/a)</td><td>349.74 (n/a)</td><td>308.40 (n/a)</td><td>260.50 (n/a)</td><td>122.14 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.23 (-3.90%)</td><td>0.15 <b>(-20.73%)</b></td><td>0.13 <b>(-30.77%)</b></td><td>0.12 (-13.94%)</td><td>0.05 (+9.23%)</td><td>543.20 (+16.19%)</td><td>454.72 <b>(+28.48%)</b></td><td>488.80 <b>(+44.44%)</b></td><td>279.50 (+4.06%)</td><td>110.07 <b>(+32.52%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>467.50 (n/a)</td><td>353.92 (n/a)</td><td>338.40 (n/a)</td><td>268.60 (n/a)</td><td>83.06 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.33 <b>(+31.72%)</b></td><td>0.18 (+10.13%)</td><td>0.15 (-2.47%)</td><td>0.11 (-5.27%)</td><td>0.09 <b>(+66.92%)</b></td><td>574.30 (+5.57%)</td><td>423.10 (-2.71%)</td><td>446.90 (+2.52%)</td><td>197.10 <b>(-24.05%)</b></td><td>139.39 <b>(+28.02%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>544.00 (n/a)</td><td>434.90 (n/a)</td><td>435.90 (n/a)</td><td>259.50 (n/a)</td><td>108.87 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.35 <b>(-34.88%)</b></td><td>0.28 (-15.58%)</td><td>0.28 (-11.04%)</td><td>0.21 (+2.48%)</td><td>0.06 <b>(-51.80%)</b></td><td>626.50 (-2.43%)</td><td>482.18 (+9.79%)</td><td>462.20 (+12.40%)</td><td>374.80 <b>(+53.54%)</b></td><td>112.40 <b>(-30.37%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.54 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>642.10 (n/a)</td><td>439.18 (n/a)</td><td>411.20 (n/a)</td><td>244.10 (n/a)</td><td>161.42 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.51 (+5.44%)</td><td>0.33 (-3.52%)</td><td>0.29 <b>(-22.64%)</b></td><td>0.21 (+7.42%)</td><td>0.12 (-7.03%)</td><td>613.40 (-6.91%)</td><td>440.64 (-0.22%)</td><td>451.40 <b>(+29.27%)</b></td><td>254.60 (-5.18%)</td><td>140.05 <b>(-23.43%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.38 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>658.90 (n/a)</td><td>441.62 (n/a)</td><td>349.20 (n/a)</td><td>268.50 (n/a)</td><td>182.89 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.52 (+17.49%)</td><td>0.35 (+15.12%)</td><td>0.30 (+5.87%)</td><td>0.21 (-12.48%)</td><td>0.13 <b>(+66.36%)</b></td><td>612.90 (+14.26%)</td><td>418.24 (-7.11%)</td><td>438.70 (-5.53%)</td><td>253.70 (-14.87%)</td><td>148.70 <b>(+64.19%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.44 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.08 (n/a)</td><td>536.40 (n/a)</td><td>450.26 (n/a)</td><td>464.40 (n/a)</td><td>298.00 (n/a)</td><td>90.56 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 <b>(+21.65%)</b></td><td>0.04 <b>(+34.32%)</b></td><td>0.04 <b>(+42.33%)</b></td><td>0.03 <b>(+82.00%)</b></td><td>0.02 (+9.60%)</td><td>604.60 <b>(-45.05%)</b></td><td>421.90 <b>(-30.76%)</b></td><td>420.10 <b>(-29.75%)</b></td><td>243.60 (-17.79%)</td><td>147.67 <b>(-51.05%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:04:49</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1100.30 (n/a)</td><td>609.30 (n/a)</td><td>598.00 (n/a)</td><td>296.30 (n/a)</td><td>301.67 (n/a)</td>
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
