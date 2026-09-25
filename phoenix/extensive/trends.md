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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (+18.97%)</td><td>0.02 (+8.95%)</td><td>0.02 (+3.93%)</td><td>0.01 <b>(-20.88%)</b></td><td>0.01 <b>(+38.56%)</b></td><td>581.70 <b>(+26.37%)</b></td><td>333.12 (-2.98%)</td><td>294.50 (-3.76%)</td><td>221.90 (-15.95%)</td><td>142.14 <b>(+60.74%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>460.30 (n/a)</td><td>343.34 (n/a)</td><td>306.00 (n/a)</td><td>264.00 (n/a)</td><td>88.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (-13.54%)</td><td>0.02 <b>(-23.92%)</b></td><td>0.02 (-17.92%)</td><td>0.01 <b>(-29.40%)</b></td><td>0.00 (+19.67%)</td><td>543.50 <b>(+41.65%)</b></td><td>378.96 <b>(+37.07%)</b></td><td>306.50 <b>(+21.82%)</b></td><td>272.90 (+15.64%)</td><td>120.70 <b>(+95.09%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>383.70 (n/a)</td><td>276.48 (n/a)</td><td>251.60 (n/a)</td><td>236.00 (n/a)</td><td>61.87 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (-11.73%)</td><td>0.02 (-2.49%)</td><td>0.01 (+15.12%)</td><td>0.01 (+7.10%)</td><td>0.01 <b>(-30.53%)</b></td><td>591.60 (-6.64%)</td><td>405.56 (-6.22%)</td><td>409.70 (-13.14%)</td><td>259.10 (+13.29%)</td><td>141.93 <b>(-26.25%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>633.70 (n/a)</td><td>432.48 (n/a)</td><td>471.70 (n/a)</td><td>228.70 (n/a)</td><td>192.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (+16.60%)</td><td>0.02 <b>(+31.72%)</b></td><td>0.03 <b>(+94.06%)</b></td><td>0.01 (-11.12%)</td><td>0.01 <b>(+62.95%)</b></td><td>556.10 (+12.53%)</td><td>349.92 (-16.73%)</td><td>243.00 <b>(-48.47%)</b></td><td>218.80 (-14.23%)</td><td>160.36 <b>(+59.62%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>494.20 (n/a)</td><td>420.24 (n/a)</td><td>471.60 (n/a)</td><td>255.10 (n/a)</td><td>100.47 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (-13.27%)</td><td>0.02 (-17.55%)</td><td>0.01 <b>(-36.81%)</b></td><td>0.01 (-3.85%)</td><td>0.00 (-17.71%)</td><td>542.50 (+4.01%)</td><td>422.76 (+19.43%)</td><td>456.70 <b>(+58.25%)</b></td><td>282.70 (+15.34%)</td><td>114.06 (-2.99%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>521.60 (n/a)</td><td>353.98 (n/a)</td><td>288.60 (n/a)</td><td>245.10 (n/a)</td><td>117.57 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 <b>(-34.55%)</b></td><td>0.01 (-19.74%)</td><td>0.01 (-12.18%)</td><td>0.01 (+10.13%)</td><td>0.00 <b>(-63.82%)</b></td><td>609.90 (-9.20%)</td><td>479.08 (+11.38%)</td><td>488.40 (+13.87%)</td><td>375.40 <b>(+52.79%)</b></td><td>90.94 <b>(-48.40%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>671.70 (n/a)</td><td>430.12 (n/a)</td><td>428.90 (n/a)</td><td>245.70 (n/a)</td><td>176.22 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (+16.98%)</td><td>0.03 (-10.77%)</td><td>0.02 <b>(-42.19%)</b></td><td>0.02 (-1.49%)</td><td>0.01 <b>(+42.82%)</b></td><td>645.00 (+1.51%)</td><td>489.46 (+19.08%)</td><td>597.80 <b>(+72.97%)</b></td><td>254.50 (-14.54%)</td><td>179.19 <b>(+28.00%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>635.40 (n/a)</td><td>411.02 (n/a)</td><td>345.60 (n/a)</td><td>297.80 (n/a)</td><td>139.99 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (-2.51%)</td><td>0.04 (-10.65%)</td><td>0.05 (+5.68%)</td><td>0.02 <b>(-44.84%)</b></td><td>0.01 <b>(+169.54%)</b></td><td>555.20 <b>(+81.32%)</b></td><td>341.18 <b>(+23.68%)</b></td><td>256.10 (-5.36%)</td><td>243.80 (+2.57%)</td><td>137.48 <b>(+370.55%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>306.20 (n/a)</td><td>275.86 (n/a)</td><td>270.60 (n/a)</td><td>237.70 (n/a)</td><td>29.22 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (-13.88%)</td><td>0.03 (-7.65%)</td><td>0.03 (-1.29%)</td><td>0.02 (-4.66%)</td><td>0.01 <b>(-21.91%)</b></td><td>581.40 (+4.89%)</td><td>444.18 (+4.06%)</td><td>467.70 (+1.32%)</td><td>230.20 (+16.15%)</td><td>133.20 (-9.92%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>554.30 (n/a)</td><td>426.86 (n/a)</td><td>461.60 (n/a)</td><td>198.20 (n/a)</td><td>147.87 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (-16.57%)</td><td>0.03 <b>(-22.54%)</b></td><td>0.02 <b>(-26.65%)</b></td><td>0.02 (-12.06%)</td><td>0.01 <b>(-33.54%)</b></td><td>580.30 (+13.72%)</td><td>503.52 <b>(+26.19%)</b></td><td>527.90 <b>(+36.34%)</b></td><td>350.80 (+19.89%)</td><td>91.87 (-12.15%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.30 (n/a)</td><td>399.02 (n/a)</td><td>387.20 (n/a)</td><td>292.60 (n/a)</td><td>104.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (-9.65%)</td><td>0.03 (-12.09%)</td><td>0.02 (+4.96%)</td><td>0.02 (-4.49%)</td><td>0.01 <b>(-27.14%)</b></td><td>609.20 (+4.69%)</td><td>447.20 (+6.34%)</td><td>493.90 (-4.73%)</td><td>242.50 (+10.68%)</td><td>150.55 (-14.86%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>581.90 (n/a)</td><td>420.54 (n/a)</td><td>518.40 (n/a)</td><td>219.10 (n/a)</td><td>176.83 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 <b>(-24.02%)</b></td><td>0.03 (-19.28%)</td><td>0.02 <b>(-23.33%)</b></td><td>0.02 (-3.81%)</td><td>0.01 <b>(-32.85%)</b></td><td>531.20 (+3.95%)</td><td>457.64 <b>(+21.40%)</b></td><td>524.40 <b>(+30.42%)</b></td><td>340.80 <b>(+31.63%)</b></td><td>96.28 (-4.24%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.00 (n/a)</td><td>376.96 (n/a)</td><td>402.10 (n/a)</td><td>258.90 (n/a)</td><td>100.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 <b>(-34.07%)</b></td><td>0.05 <b>(-32.74%)</b></td><td>0.05 <b>(-31.10%)</b></td><td>0.01 <b>(-74.90%)</b></td><td>0.02 (-4.32%)</td><td>2025.80 <b>(+298.39%)</b></td><td>736.14 <b>(+108.42%)</b></td><td>459.50 <b>(+45.14%)</b></td><td>339.00 <b>(+51.68%)</b></td><td>723.89 <b>(+515.12%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>508.50 (n/a)</td><td>353.20 (n/a)</td><td>316.60 (n/a)</td><td>223.50 (n/a)</td><td>117.68 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (-3.63%)</td><td>0.08 (+8.24%)</td><td>0.08 (-1.39%)</td><td>0.05 (+7.54%)</td><td>0.02 (-8.33%)</td><td>492.40 (-7.01%)</td><td>320.84 (-8.89%)</td><td>309.50 (+1.41%)</td><td>235.30 (+3.75%)</td><td>102.18 (-11.58%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>529.50 (n/a)</td><td>352.16 (n/a)</td><td>305.20 (n/a)</td><td>226.80 (n/a)</td><td>115.57 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (+5.63%)</td><td>0.07 (-19.66%)</td><td>0.06 <b>(-37.49%)</b></td><td>0.05 (-18.07%)</td><td>0.02 <b>(+58.69%)</b></td><td>489.40 <b>(+22.04%)</b></td><td>386.04 <b>(+31.75%)</b></td><td>434.60 <b>(+59.96%)</b></td><td>227.60 (-5.32%)</td><td>115.66 <b>(+82.05%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>401.00 (n/a)</td><td>293.02 (n/a)</td><td>271.70 (n/a)</td><td>240.40 (n/a)</td><td>63.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 <b>(+32.72%)</b></td><td>0.07 <b>(+27.16%)</b></td><td>0.07 <b>(+41.61%)</b></td><td>0.04 <b>(+76.55%)</b></td><td>0.03 (-0.58%)</td><td>621.90 <b>(-43.36%)</b></td><td>389.36 <b>(-30.03%)</b></td><td>367.50 <b>(-29.39%)</b></td><td>223.80 <b>(-24.65%)</b></td><td>149.68 <b>(-54.29%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1097.90 (n/a)</td><td>556.44 (n/a)</td><td>520.50 (n/a)</td><td>297.00 (n/a)</td><td>327.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (-18.94%)</td><td>0.06 <b>(-25.04%)</b></td><td>0.06 <b>(-29.72%)</b></td><td>0.04 (-16.17%)</td><td>0.02 (-18.55%)</td><td>551.00 (+19.29%)</td><td>436.88 <b>(+33.00%)</b></td><td>439.10 <b>(+42.29%)</b></td><td>288.90 <b>(+23.36%)</b></td><td>98.97 (+14.83%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>461.90 (n/a)</td><td>328.48 (n/a)</td><td>308.60 (n/a)</td><td>234.20 (n/a)</td><td>86.19 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 <b>(+62.64%)</b></td><td>0.07 <b>(+34.29%)</b></td><td>0.06 <b>(+49.89%)</b></td><td>0.03 (-17.62%)</td><td>0.04 <b>(+117.99%)</b></td><td>732.50 <b>(+21.40%)</b></td><td>426.72 (-12.31%)</td><td>384.70 <b>(-33.28%)</b></td><td>183.70 <b>(-38.50%)</b></td><td>224.93 <b>(+58.50%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>603.40 (n/a)</td><td>486.62 (n/a)</td><td>576.60 (n/a)</td><td>298.70 (n/a)</td><td>141.91 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.18 (-13.25%)</td><td>0.13 (-2.58%)</td><td>0.13 (-11.24%)</td><td>0.10 <b>(+50.18%)</b></td><td>0.03 <b>(-41.16%)</b></td><td>514.50 <b>(-33.41%)</b></td><td>384.16 (-8.31%)</td><td>383.70 (+12.65%)</td><td>271.30 (+15.30%)</td><td>88.37 <b>(-57.70%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>772.60 (n/a)</td><td>418.96 (n/a)</td><td>340.60 (n/a)</td><td>235.30 (n/a)</td><td>208.91 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.21 (+3.42%)</td><td>0.17 (+0.01%)</td><td>0.18 (+0.64%)</td><td>0.09 <b>(-25.65%)</b></td><td>0.05 <b>(+45.06%)</b></td><td>557.20 <b>(+34.49%)</b></td><td>316.28 (+6.67%)</td><td>274.50 (-0.65%)</td><td>230.00 (-3.32%)</td><td>136.08 <b>(+94.76%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>414.30 (n/a)</td><td>296.50 (n/a)</td><td>276.30 (n/a)</td><td>237.90 (n/a)</td><td>69.87 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 <b>(-34.55%)</b></td><td>0.08 <b>(-43.69%)</b></td><td>0.08 <b>(-50.02%)</b></td><td>0.03 <b>(-71.72%)</b></td><td>0.04 (-19.86%)</td><td>1845.20 <b>(+253.62%)</b></td><td>787.60 <b>(+117.89%)</b></td><td>589.60 <b>(+100.07%)</b></td><td>340.40 <b>(+52.85%)</b></td><td>600.71 <b>(+365.46%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>521.80 (n/a)</td><td>361.46 (n/a)</td><td>294.70 (n/a)</td><td>222.70 (n/a)</td><td>129.06 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.23 (+11.85%)</td><td>0.11 (-19.48%)</td><td>0.10 (-8.55%)</td><td>0.03 <b>(-71.27%)</b></td><td>0.08 <b>(+42.97%)</b></td><td>1904.00 <b>(+248.02%)</b></td><td>712.26 <b>(+83.64%)</b></td><td>481.70 (+9.35%)</td><td>210.00 (-10.60%)</td><td>677.44 <b>(+409.66%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>547.10 (n/a)</td><td>387.86 (n/a)</td><td>440.50 (n/a)</td><td>234.90 (n/a)</td><td>132.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.23 <b>(+42.81%)</b></td><td>0.13 (+13.43%)</td><td>0.10 (-1.81%)</td><td>0.08 (-2.82%)</td><td>0.06 <b>(+92.54%)</b></td><td>600.70 (+2.89%)</td><td>449.66 (-4.63%)</td><td>498.20 (+1.86%)</td><td>209.30 <b>(-29.98%)</b></td><td>147.48 <b>(+30.12%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>583.80 (n/a)</td><td>471.48 (n/a)</td><td>489.10 (n/a)</td><td>298.90 (n/a)</td><td>113.34 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.18 (-18.92%)</td><td>0.13 (+11.43%)</td><td>0.10 (+17.05%)</td><td>0.10 <b>(+51.75%)</b></td><td>0.04 <b>(-38.70%)</b></td><td>513.40 <b>(-34.10%)</b></td><td>410.74 <b>(-20.45%)</b></td><td>472.00 (-14.57%)</td><td>269.90 <b>(+23.35%)</b></td><td>112.67 <b>(-47.08%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>779.10 (n/a)</td><td>516.30 (n/a)</td><td>552.50 (n/a)</td><td>218.80 (n/a)</td><td>212.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 <b>(+27.45%)</b></td><td>0.01 <b>(-24.39%)</b></td><td>0.01 <b>(-40.62%)</b></td><td>0.00 <b>(-58.51%)</b></td><td>0.00 <b>(+85.62%)</b></td><td>1074.10 <b>(+140.99%)</b></td><td>524.26 <b>(+67.80%)</b></td><td>433.30 <b>(+68.40%)</b></td><td>193.00 <b>(-21.51%)</b></td><td>329.96 <b>(+265.89%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>445.70 (n/a)</td><td>312.44 (n/a)</td><td>257.30 (n/a)</td><td>245.90 (n/a)</td><td>90.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (+10.73%)</td><td>0.01 (+5.79%)</td><td>0.01 (-12.60%)</td><td>0.01 <b>(+332.55%)</b></td><td>0.00 <b>(-38.25%)</b></td><td>462.00 <b>(-76.88%)</b></td><td>334.82 <b>(-46.73%)</b></td><td>294.50 (+14.41%)</td><td>214.80 (-9.67%)</td><td>99.50 <b>(-87.06%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1998.20 (n/a)</td><td>628.54 (n/a)</td><td>257.40 (n/a)</td><td>237.80 (n/a)</td><td>768.95 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (+18.33%)</td><td>0.01 (+14.24%)</td><td>0.01 <b>(-23.52%)</b></td><td>0.01 <b>(+263.75%)</b></td><td>0.00 (-7.49%)</td><td>484.10 <b>(-72.51%)</b></td><td>356.18 <b>(-40.85%)</b></td><td>418.70 <b>(+30.76%)</b></td><td>214.40 (-15.49%)</td><td>127.00 <b>(-80.49%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1760.80 (n/a)</td><td>602.14 (n/a)</td><td>320.20 (n/a)</td><td>253.70 (n/a)</td><td>650.91 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (+0.78%)</td><td>0.01 (+1.47%)</td><td>0.01 <b>(+22.78%)</b></td><td>0.00 <b>(-34.35%)</b></td><td>0.00 (+13.42%)</td><td>1003.80 <b>(+52.32%)</b></td><td>537.80 (+8.84%)</td><td>452.40 (-18.56%)</td><td>247.00 (-0.76%)</td><td>303.74 <b>(+66.10%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>659.00 (n/a)</td><td>494.14 (n/a)</td><td>555.50 (n/a)</td><td>248.90 (n/a)</td><td>182.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (+11.54%)</td><td>0.01 (+16.26%)</td><td>0.01 <b>(+31.79%)</b></td><td>0.00 (+1.80%)</td><td>0.00 <b>(+30.13%)</b></td><td>609.60 (-1.77%)</td><td>384.36 (-10.28%)</td><td>304.10 <b>(-24.13%)</b></td><td>236.40 (-10.35%)</td><td>156.51 (+17.96%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>620.60 (n/a)</td><td>428.42 (n/a)</td><td>400.80 (n/a)</td><td>263.70 (n/a)</td><td>132.69 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (-4.95%)</td><td>0.01 <b>(-23.27%)</b></td><td>0.01 <b>(-29.66%)</b></td><td>0.00 <b>(-63.46%)</b></td><td>0.00 (+19.66%)</td><td>1704.70 <b>(+173.67%)</b></td><td>669.62 <b>(+73.58%)</b></td><td>417.00 <b>(+42.18%)</b></td><td>264.80 (+5.20%)</td><td>590.58 <b>(+276.86%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>622.90 (n/a)</td><td>385.78 (n/a)</td><td>293.30 (n/a)</td><td>251.70 (n/a)</td><td>156.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (-7.90%)</td><td>0.02 (-4.15%)</td><td>0.01 <b>(-23.67%)</b></td><td>0.01 (+7.58%)</td><td>0.01 (-10.74%)</td><td>516.90 (-7.03%)</td><td>380.08 (+0.90%)</td><td>394.60 <b>(+31.01%)</b></td><td>224.50 (+8.56%)</td><td>135.69 (-15.86%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.00 (n/a)</td><td>376.70 (n/a)</td><td>301.20 (n/a)</td><td>206.80 (n/a)</td><td>161.27 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (-5.96%)</td><td>0.01 (-0.07%)</td><td>0.01 (+14.12%)</td><td>0.01 (+13.58%)</td><td>0.00 <b>(-47.54%)</b></td><td>450.70 (-11.96%)</td><td>386.24 (-5.17%)</td><td>396.80 (-12.37%)</td><td>299.50 (+6.36%)</td><td>56.93 <b>(-50.80%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.90 (n/a)</td><td>407.28 (n/a)</td><td>452.80 (n/a)</td><td>281.60 (n/a)</td><td>115.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 <b>(-27.16%)</b></td><td>0.02 <b>(+20.41%)</b></td><td>0.02 (+17.44%)</td><td>0.02 <b>(+123.28%)</b></td><td>0.00 <b>(-89.88%)</b></td><td>282.60 <b>(-55.21%)</b></td><td>270.60 <b>(-31.90%)</b></td><td>269.70 (-14.87%)</td><td>255.50 <b>(+37.29%)</b></td><td>11.24 <b>(-94.12%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.90 (n/a)</td><td>397.34 (n/a)</td><td>316.80 (n/a)</td><td>186.10 (n/a)</td><td>191.17 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (+5.46%)</td><td>0.01 (-7.08%)</td><td>0.01 (-4.42%)</td><td>0.01 (-15.32%)</td><td>0.00 (+16.86%)</td><td>554.10 (+18.09%)</td><td>419.48 (+9.43%)</td><td>403.90 (+4.64%)</td><td>270.40 (-5.19%)</td><td>104.46 <b>(+24.80%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>469.20 (n/a)</td><td>383.34 (n/a)</td><td>386.00 (n/a)</td><td>285.20 (n/a)</td><td>83.70 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (+4.91%)</td><td>0.02 (-5.51%)</td><td>0.02 (-13.91%)</td><td>0.01 (+7.22%)</td><td>0.00 (+8.52%)</td><td>437.50 (-6.74%)</td><td>320.04 (+5.83%)</td><td>301.70 (+16.17%)</td><td>233.50 (-4.69%)</td><td>87.48 (-7.41%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>469.10 (n/a)</td><td>302.40 (n/a)</td><td>259.70 (n/a)</td><td>245.00 (n/a)</td><td>94.48 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (-4.61%)</td><td>0.01 <b>(-24.91%)</b></td><td>0.01 <b>(-34.49%)</b></td><td>0.01 <b>(-26.72%)</b></td><td>0.00 <b>(+77.66%)</b></td><td>598.00 <b>(+36.47%)</b></td><td>517.40 <b>(+36.96%)</b></td><td>556.80 <b>(+52.63%)</b></td><td>353.00 (+4.84%)</td><td>98.07 <b>(+145.96%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>438.20 (n/a)</td><td>377.78 (n/a)</td><td>364.80 (n/a)</td><td>336.70 (n/a)</td><td>39.87 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 <b>(-20.25%)</b></td><td>0.02 <b>(-38.70%)</b></td><td>0.02 <b>(-36.43%)</b></td><td>0.00 <b>(-78.51%)</b></td><td>0.01 <b>(+53.82%)</b></td><td>2130.80 <b>(+365.34%)</b></td><td>772.40 <b>(+146.38%)</b></td><td>429.30 <b>(+57.31%)</b></td><td>335.60 <b>(+25.41%)</b></td><td>766.54 <b>(+837.82%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>457.90 (n/a)</td><td>313.50 (n/a)</td><td>272.90 (n/a)</td><td>267.60 (n/a)</td><td>81.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (+1.56%)</td><td>0.04 (+15.73%)</td><td>0.04 (-8.02%)</td><td>0.03 <b>(+93.66%)</b></td><td>0.01 <b>(-55.70%)</b></td><td>304.60 <b>(-48.37%)</b></td><td>273.66 <b>(-24.02%)</b></td><td>297.70 (+8.73%)</td><td>222.70 (-1.50%)</td><td>37.21 <b>(-76.96%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>590.00 (n/a)</td><td>360.18 (n/a)</td><td>273.80 (n/a)</td><td>226.10 (n/a)</td><td>161.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (-2.30%)</td><td>0.03 (-10.04%)</td><td>0.04 (-16.29%)</td><td>0.02 (-19.95%)</td><td>0.01 (+4.46%)</td><td>538.90 <b>(+24.92%)</b></td><td>330.34 (+13.93%)</td><td>295.10 (+19.43%)</td><td>222.50 (+2.35%)</td><td>120.98 <b>(+40.32%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>431.40 (n/a)</td><td>289.96 (n/a)</td><td>247.10 (n/a)</td><td>217.40 (n/a)</td><td>86.22 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (+2.86%)</td><td>0.03 (+1.29%)</td><td>0.02 (+0.20%)</td><td>0.02 (+3.84%)</td><td>0.01 (+1.95%)</td><td>511.70 (-3.69%)</td><td>394.36 (-1.21%)</td><td>475.00 (-0.21%)</td><td>229.40 (-2.80%)</td><td>141.52 (-1.46%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.30 (n/a)</td><td>399.20 (n/a)</td><td>476.00 (n/a)</td><td>236.00 (n/a)</td><td>143.62 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (+14.74%)</td><td>0.03 (+13.43%)</td><td>0.03 (-10.71%)</td><td>0.02 <b>(+30.95%)</b></td><td>0.01 (-3.41%)</td><td>464.90 <b>(-23.62%)</b></td><td>325.96 (-15.64%)</td><td>330.40 (+12.00%)</td><td>229.70 (-12.83%)</td><td>97.53 <b>(-37.13%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>608.70 (n/a)</td><td>386.38 (n/a)</td><td>295.00 (n/a)</td><td>263.50 (n/a)</td><td>155.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (-12.53%)</td><td>0.02 (-13.80%)</td><td>0.02 (-19.49%)</td><td>0.02 (+14.94%)</td><td>0.00 <b>(-43.07%)</b></td><td>548.10 (-13.00%)</td><td>480.60 (+9.13%)</td><td>519.30 <b>(+24.20%)</b></td><td>337.80 (+14.35%)</td><td>85.29 <b>(-42.76%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>630.00 (n/a)</td><td>440.38 (n/a)</td><td>418.10 (n/a)</td><td>295.40 (n/a)</td><td>149.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (+8.62%)</td><td>0.06 (+16.18%)</td><td>0.06 <b>(+28.33%)</b></td><td>0.04 <b>(+28.36%)</b></td><td>0.02 (-17.40%)</td><td>584.30 <b>(-22.09%)</b></td><td>369.84 <b>(-20.31%)</b></td><td>334.30 <b>(-22.09%)</b></td><td>234.70 (-7.92%)</td><td>130.31 <b>(-37.39%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>750.00 (n/a)</td><td>464.08 (n/a)</td><td>429.10 (n/a)</td><td>254.90 (n/a)</td><td>208.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (-9.95%)</td><td>0.06 (+2.31%)</td><td>0.08 <b>(+27.42%)</b></td><td>0.04 (+7.02%)</td><td>0.02 (-14.96%)</td><td>570.10 (-6.56%)</td><td>366.10 (-5.50%)</td><td>275.50 <b>(-21.53%)</b></td><td>242.10 (+11.00%)</td><td>149.62 (-11.38%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>610.10 (n/a)</td><td>387.40 (n/a)</td><td>351.10 (n/a)</td><td>218.10 (n/a)</td><td>168.83 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 <b>(-27.53%)</b></td><td>0.05 <b>(-21.11%)</b></td><td>0.05 <b>(-39.50%)</b></td><td>0.04 <b>(+30.55%)</b></td><td>0.01 <b>(-67.43%)</b></td><td>467.00 <b>(-23.39%)</b></td><td>405.38 (+6.84%)</td><td>411.50 <b>(+65.26%)</b></td><td>305.00 <b>(+38.01%)</b></td><td>63.27 <b>(-67.27%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>609.60 (n/a)</td><td>379.42 (n/a)</td><td>249.00 (n/a)</td><td>221.00 (n/a)</td><td>193.30 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (+14.99%)</td><td>0.07 <b>(+37.51%)</b></td><td>0.08 <b>(+40.27%)</b></td><td>0.06 <b>(+85.99%)</b></td><td>0.01 <b>(-45.50%)</b></td><td>342.50 <b>(-46.22%)</b></td><td>285.60 <b>(-34.62%)</b></td><td>276.40 <b>(-28.71%)</b></td><td>242.80 (-13.04%)</td><td>44.06 <b>(-74.42%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>636.90 (n/a)</td><td>436.80 (n/a)</td><td>387.70 (n/a)</td><td>279.20 (n/a)</td><td>172.27 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (-6.32%)</td><td>0.06 <b>(-20.99%)</b></td><td>0.05 <b>(-43.53%)</b></td><td>0.03 <b>(-39.07%)</b></td><td>0.03 (+7.15%)</td><td>824.90 <b>(+64.13%)</b></td><td>450.20 <b>(+38.50%)</b></td><td>442.90 <b>(+77.09%)</b></td><td>211.00 (+6.73%)</td><td>238.87 <b>(+78.61%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>502.60 (n/a)</td><td>325.06 (n/a)</td><td>250.10 (n/a)</td><td>197.70 (n/a)</td><td>133.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (-0.20%)</td><td>0.05 (-10.74%)</td><td>0.04 (-14.48%)</td><td>0.04 (+11.17%)</td><td>0.01 (-14.76%)</td><td>583.10 (-10.06%)</td><td>483.08 (+9.39%)</td><td>544.80 (+16.93%)</td><td>303.80 (+0.20%)</td><td>117.20 (-18.11%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>648.30 (n/a)</td><td>441.60 (n/a)</td><td>465.90 (n/a)</td><td>303.20 (n/a)</td><td>143.12 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>588.50 (n/a)</td><td>498.56 (n/a)</td><td>495.70 (n/a)</td><td>372.00 (n/a)</td><td>80.66 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>570.20 (n/a)</td><td>418.14 (n/a)</td><td>422.80 (n/a)</td><td>285.10 (n/a)</td><td>120.17 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>602.10 (n/a)</td><td>479.56 (n/a)</td><td>459.20 (n/a)</td><td>390.70 (n/a)</td><td>87.83 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1114.10 (n/a)</td><td>616.68 (n/a)</td><td>504.30 (n/a)</td><td>444.10 (n/a)</td><td>282.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.50 (n/a)</td><td>385.92 (n/a)</td><td>420.20 (n/a)</td><td>234.40 (n/a)</td><td>134.53 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1868.80 (n/a)</td><td>690.36 (n/a)</td><td>368.40 (n/a)</td><td>297.30 (n/a)</td><td>667.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>468.30 (n/a)</td><td>346.06 (n/a)</td><td>301.00 (n/a)</td><td>247.00 (n/a)</td><td>111.77 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>615.70 (n/a)</td><td>390.92 (n/a)</td><td>349.50 (n/a)</td><td>245.60 (n/a)</td><td>151.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>637.90 (n/a)</td><td>545.66 (n/a)</td><td>518.20 (n/a)</td><td>433.20 (n/a)</td><td>87.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.17 (-0.68%)</td><td>0.13 (+16.77%)</td><td>0.12 <b>(+22.99%)</b></td><td>0.08 <b>(+205.48%)</b></td><td>0.04 <b>(-34.65%)</b></td><td>605.50 <b>(-67.27%)</b></td><td>416.84 <b>(-40.44%)</b></td><td>408.10 (-18.69%)</td><td>290.30 (+0.69%)</td><td>132.41 <b>(-79.75%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.06 (n/a)</td><td>1849.80 (n/a)</td><td>699.84 (n/a)</td><td>501.90 (n/a)</td><td>288.30 (n/a)</td><td>653.83 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>515.50 (n/a)</td><td>364.88 (n/a)</td><td>358.40 (n/a)</td><td>256.90 (n/a)</td><td>94.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>477.50 (n/a)</td><td>357.64 (n/a)</td><td>299.50 (n/a)</td><td>280.30 (n/a)</td><td>94.58 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>506.90 (n/a)</td><td>358.20 (n/a)</td><td>425.00 (n/a)</td><td>161.50 (n/a)</td><td>147.40 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1894.80 (n/a)</td><td>645.74 (n/a)</td><td>393.60 (n/a)</td><td>229.60 (n/a)</td><td>705.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>523.50 (n/a)</td><td>371.62 (n/a)</td><td>332.60 (n/a)</td><td>250.00 (n/a)</td><td>124.77 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>530.20 (n/a)</td><td>404.32 (n/a)</td><td>479.60 (n/a)</td><td>241.20 (n/a)</td><td>143.33 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>608.10 (n/a)</td><td>434.92 (n/a)</td><td>450.90 (n/a)</td><td>242.10 (n/a)</td><td>131.20 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>597.20 (n/a)</td><td>451.54 (n/a)</td><td>451.80 (n/a)</td><td>323.80 (n/a)</td><td>113.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>527.60 (n/a)</td><td>346.78 (n/a)</td><td>302.80 (n/a)</td><td>225.40 (n/a)</td><td>133.24 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1885.30 (n/a)</td><td>705.32 (n/a)</td><td>515.30 (n/a)</td><td>215.10 (n/a)</td><td>672.79 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1868.80 (n/a)</td><td>753.60 (n/a)</td><td>470.50 (n/a)</td><td>441.80 (n/a)</td><td>624.79 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>536.50 (n/a)</td><td>350.56 (n/a)</td><td>315.40 (n/a)</td><td>205.50 (n/a)</td><td>136.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>570.70 (n/a)</td><td>443.84 (n/a)</td><td>421.00 (n/a)</td><td>356.30 (n/a)</td><td>92.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.59 (-17.74%)</td><td>2.33 (+9.95%)</td><td>2.42 <b>(+32.96%)</b></td><td>1.76 (+12.52%)</td><td>0.34 <b>(-49.09%)</b></td><td>5946.90 (-11.13%)</td><td>4584.96 (-13.30%)</td><td>4334.70 <b>(-24.79%)</b></td><td>4050.30 <b>(+21.57%)</b></td><td>784.43 <b>(-44.39%)</b></td><td>1060.40 (-17.74%)</td><td>955.55 (+9.95%)</td><td>990.83 <b>(+32.96%)</b></td><td>722.22 (+12.52%)</td><td>137.84 <b>(-49.09%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.15 (n/a)</td><td>2.12 (n/a)</td><td>1.82 (n/a)</td><td>1.57 (n/a)</td><td>0.66 (n/a)</td><td>6691.70 (n/a)</td><td>5288.40 (n/a)</td><td>5763.20 (n/a)</td><td>3331.60 (n/a)</td><td>1410.68 (n/a)</td><td>1289.16 (n/a)</td><td>869.08 (n/a)</td><td>745.24 (n/a)</td><td>641.84 (n/a)</td><td>270.77 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.58 (-1.80%)</td><td>2.41 (-5.07%)</td><td>2.31 (-9.46%)</td><td>2.27 (-6.87%)</td><td>0.15 <b>(+116.44%)</b></td><td>10407.00 (+7.37%)</td><td>9840.86 (+5.61%)</td><td>10223.60 (+10.44%)</td><td>9134.70 (+1.83%)</td><td>620.71 <b>(+134.94%)</b></td><td>1469.32 (-1.80%)</td><td>1368.33 (-5.07%)</td><td>1312.82 (-9.46%)</td><td>1289.68 (-6.87%)</td><td>88.18 <b>(+116.44%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.63 (n/a)</td><td>2.53 (n/a)</td><td>2.55 (n/a)</td><td>2.43 (n/a)</td><td>0.07 (n/a)</td><td>9692.40 (n/a)</td><td>9317.76 (n/a)</td><td>9256.90 (n/a)</td><td>8970.40 (n/a)</td><td>264.20 (n/a)</td><td>1496.23 (n/a)</td><td>1441.38 (n/a)</td><td>1449.92 (n/a)</td><td>1384.78 (n/a)</td><td>40.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.52 (-6.24%)</td><td>2.32 (-6.74%)</td><td>2.36 (-7.72%)</td><td>2.00 (-9.19%)</td><td>0.20 (-5.91%)</td><td>8409.60 (+10.12%)</td><td>7284.94 (+7.26%)</td><td>7094.20 (+8.36%)</td><td>6662.70 (+6.65%)</td><td>674.28 (+12.51%)</td><td>1289.26 (-6.24%)</td><td>1186.66 (-6.74%)</td><td>1210.85 (-7.72%)</td><td>1021.45 (-9.19%)</td><td>101.83 (-5.91%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.69 (n/a)</td><td>2.49 (n/a)</td><td>2.56 (n/a)</td><td>2.20 (n/a)</td><td>0.21 (n/a)</td><td>7636.60 (n/a)</td><td>6791.88 (n/a)</td><td>6546.80 (n/a)</td><td>6247.10 (n/a)</td><td>599.30 (n/a)</td><td>1375.02 (n/a)</td><td>1272.37 (n/a)</td><td>1312.09 (n/a)</td><td>1124.83 (n/a)</td><td>108.23 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.97 (+0.67%)</td><td>0.64 (-6.23%)</td><td>0.63 (-6.86%)</td><td>0.42 (+15.26%)</td><td>0.21 (-14.01%)</td><td>1105.10 (-13.24%)</td><td>770.78 (+2.16%)</td><td>732.20 (+7.38%)</td><td>473.10 (-0.65%)</td><td>236.28 <b>(-26.27%)</b></td><td>70.93 (+0.67%)</td><td>47.13 (-6.23%)</td><td>45.83 (-6.86%)</td><td>30.36 (+15.26%)</td><td>15.30 (-14.01%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.96 (n/a)</td><td>0.69 (n/a)</td><td>0.67 (n/a)</td><td>0.36 (n/a)</td><td>0.24 (n/a)</td><td>1273.80 (n/a)</td><td>754.50 (n/a)</td><td>681.90 (n/a)</td><td>476.20 (n/a)</td><td>320.49 (n/a)</td><td>70.46 (n/a)</td><td>50.26 (n/a)</td><td>49.20 (n/a)</td><td>26.34 (n/a)</td><td>17.79 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.58 (+13.66%)</td><td>1.12 <b>(+26.43%)</b></td><td>0.90 (-1.79%)</td><td>0.86 <b>(+335.20%)</b></td><td>0.34 <b>(-29.01%)</b></td><td>760.00 <b>(-77.02%)</b></td><td>626.52 <b>(-47.72%)</b></td><td>732.00 (+1.82%)</td><td>416.00 (-12.03%)</td><td>166.70 <b>(-86.05%)</b></td><td>161.31 (+13.66%)</td><td>114.41 <b>(+26.43%)</b></td><td>91.68 (-1.79%)</td><td>88.30 <b>(+335.20%)</b></td><td>34.39 <b>(-29.01%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.39 (n/a)</td><td>0.88 (n/a)</td><td>0.91 (n/a)</td><td>0.20 (n/a)</td><td>0.47 (n/a)</td><td>3307.40 (n/a)</td><td>1198.36 (n/a)</td><td>718.90 (n/a)</td><td>472.90 (n/a)</td><td>1194.73 (n/a)</td><td>141.92 (n/a)</td><td>90.49 (n/a)</td><td>93.35 (n/a)</td><td>20.29 (n/a)</td><td>48.45 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.21 (-4.06%)</td><td>0.98 (-11.28%)</td><td>0.96 (-13.27%)</td><td>0.76 <b>(-22.51%)</b></td><td>0.17 <b>(+41.81%)</b></td><td>987.30 <b>(+29.04%)</b></td><td>787.24 (+14.37%)</td><td>787.60 (+15.30%)</td><td>620.40 (+4.23%)</td><td>136.44 <b>(+88.52%)</b></td><td>135.21 (-4.06%)</td><td>109.11 (-11.28%)</td><td>106.51 (-13.27%)</td><td>84.96 <b>(-22.51%)</b></td><td>18.66 <b>(+41.81%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.27 (n/a)</td><td>1.10 (n/a)</td><td>1.10 (n/a)</td><td>0.99 (n/a)</td><td>0.12 (n/a)</td><td>765.10 (n/a)</td><td>688.30 (n/a)</td><td>683.10 (n/a)</td><td>595.20 (n/a)</td><td>72.37 (n/a)</td><td>140.93 (n/a)</td><td>122.98 (n/a)</td><td>122.80 (n/a)</td><td>109.65 (n/a)</td><td>13.16 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.44 (-13.80%)</td><td>1.16 (+1.19%)</td><td>1.14 (+3.85%)</td><td>0.88 (+17.75%)</td><td>0.22 <b>(-37.83%)</b></td><td>1185.80 (-15.07%)</td><td>928.94 (-5.50%)</td><td>917.90 (-3.71%)</td><td>726.10 (+16.01%)</td><td>180.82 <b>(-38.70%)</b></td><td>184.85 (-13.80%)</td><td>148.84 (+1.18%)</td><td>146.22 (+3.85%)</td><td>113.19 (+17.75%)</td><td>28.26 <b>(-37.83%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.68 (n/a)</td><td>1.15 (n/a)</td><td>1.10 (n/a)</td><td>0.75 (n/a)</td><td>0.36 (n/a)</td><td>1396.20 (n/a)</td><td>983.00 (n/a)</td><td>953.30 (n/a)</td><td>625.90 (n/a)</td><td>295.00 (n/a)</td><td>214.43 (n/a)</td><td>147.10 (n/a)</td><td>140.80 (n/a)</td><td>96.13 (n/a)</td><td>45.45 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.65 (-17.36%)</td><td>1.42 (-9.84%)</td><td>1.38 <b>(-26.57%)</b></td><td>1.17 <b>(+286.79%)</b></td><td>0.19 <b>(-74.29%)</b></td><td>897.50 <b>(-74.15%)</b></td><td>750.02 <b>(-34.21%)</b></td><td>758.80 <b>(+36.18%)</b></td><td>634.90 <b>(+21.00%)</b></td><td>100.46 <b>(-92.30%)</b></td><td>211.42 (-17.36%)</td><td>181.47 (-9.84%)</td><td>176.87 <b>(-26.57%)</b></td><td>149.54 <b>(+286.79%)</b></td><td>23.69 <b>(-74.29%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.00 (n/a)</td><td>1.57 (n/a)</td><td>1.88 (n/a)</td><td>0.30 (n/a)</td><td>0.72 (n/a)</td><td>3471.60 (n/a)</td><td>1139.96 (n/a)</td><td>557.20 (n/a)</td><td>524.70 (n/a)</td><td>1303.93 (n/a)</td><td>255.82 (n/a)</td><td>201.27 (n/a)</td><td>240.86 (n/a)</td><td>38.66 (n/a)</td><td>92.12 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.82 (-8.64%)</td><td>1.27 (+0.48%)</td><td>1.45 (+12.89%)</td><td>0.44 (+0.13%)</td><td>0.53 (-3.45%)</td><td>2381.10 (-0.13%)</td><td>1062.60 (-0.39%)</td><td>721.10 (-11.41%)</td><td>576.40 (+9.46%)</td><td>750.12 (+0.49%)</td><td>232.84 (-8.64%)</td><td>162.73 (+0.48%)</td><td>186.14 (+12.89%)</td><td>56.37 (+0.13%)</td><td>68.05 (-3.45%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.99 (n/a)</td><td>1.27 (n/a)</td><td>1.29 (n/a)</td><td>0.44 (n/a)</td><td>0.55 (n/a)</td><td>2384.10 (n/a)</td><td>1066.76 (n/a)</td><td>814.00 (n/a)</td><td>526.60 (n/a)</td><td>746.48 (n/a)</td><td>254.86 (n/a)</td><td>161.96 (n/a)</td><td>164.88 (n/a)</td><td>56.30 (n/a)</td><td>70.48 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.58 (-16.80%)</td><td>1.03 <b>(-30.12%)</b></td><td>0.95 <b>(-46.99%)</b></td><td>0.43 <b>(+37.99%)</b></td><td>0.43 <b>(-34.78%)</b></td><td>2443.50 <b>(-27.53%)</b></td><td>1236.10 (+7.27%)</td><td>1101.50 <b>(+88.65%)</b></td><td>662.60 <b>(+20.19%)</b></td><td>704.49 <b>(-43.26%)</b></td><td>202.57 (-16.80%)</td><td>131.90 <b>(-30.12%)</b></td><td>121.85 <b>(-46.99%)</b></td><td>54.93 <b>(+37.99%)</b></td><td>55.40 <b>(-34.78%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.90 (n/a)</td><td>1.47 (n/a)</td><td>1.80 (n/a)</td><td>0.31 (n/a)</td><td>0.66 (n/a)</td><td>3371.70 (n/a)</td><td>1152.34 (n/a)</td><td>583.90 (n/a)</td><td>551.30 (n/a)</td><td>1241.57 (n/a)</td><td>243.47 (n/a)</td><td>188.75 (n/a)</td><td>229.87 (n/a)</td><td>39.81 (n/a)</td><td>84.94 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.59 <b>(+33.59%)</b></td><td>1.09 <b>(+20.77%)</b></td><td>1.03 <b>(+20.14%)</b></td><td>0.72 <b>(+56.12%)</b></td><td>0.37 <b>(+24.72%)</b></td><td>1456.20 <b>(-35.95%)</b></td><td>1055.34 (-19.22%)</td><td>1018.20 (-16.77%)</td><td>660.30 <b>(-25.15%)</b></td><td>347.04 <b>(-38.91%)</b></td><td>203.25 <b>(+33.59%)</b></td><td>139.41 <b>(+20.77%)</b></td><td>131.81 <b>(+20.14%)</b></td><td>92.17 <b>(+56.12%)</b></td><td>47.42 <b>(+24.72%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.19 (n/a)</td><td>0.90 (n/a)</td><td>0.86 (n/a)</td><td>0.46 (n/a)</td><td>0.30 (n/a)</td><td>2273.40 (n/a)</td><td>1306.48 (n/a)</td><td>1223.30 (n/a)</td><td>882.20 (n/a)</td><td>568.07 (n/a)</td><td>152.15 (n/a)</td><td>115.44 (n/a)</td><td>109.72 (n/a)</td><td>59.04 (n/a)</td><td>38.02 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.65 (-2.47%)</td><td>1.27 (-5.93%)</td><td>1.20 (-16.01%)</td><td>0.90 (-0.51%)</td><td>0.31 (-0.75%)</td><td>1166.60 (+0.51%)</td><td>863.88 (+6.20%)</td><td>873.30 (+19.06%)</td><td>636.30 (+2.53%)</td><td>212.72 (-1.23%)</td><td>210.94 (-2.47%)</td><td>162.97 (-5.93%)</td><td>153.70 (-16.01%)</td><td>115.05 (-0.51%)</td><td>39.17 (-0.75%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.69 (n/a)</td><td>1.35 (n/a)</td><td>1.43 (n/a)</td><td>0.90 (n/a)</td><td>0.31 (n/a)</td><td>1160.70 (n/a)</td><td>813.42 (n/a)</td><td>733.50 (n/a)</td><td>620.60 (n/a)</td><td>215.38 (n/a)</td><td>216.29 (n/a)</td><td>173.24 (n/a)</td><td>182.98 (n/a)</td><td>115.64 (n/a)</td><td>39.47 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.97 (-0.84%)</td><td>0.64 (-3.57%)</td><td>0.57 (+6.74%)</td><td>0.50 (-3.89%)</td><td>0.19 (-3.96%)</td><td>719.10 (+4.04%)</td><td>594.48 (+3.20%)</td><td>627.20 (-6.32%)</td><td>371.00 (+0.84%)</td><td>141.13 (-3.57%)</td><td>45.23 (-0.84%)</td><td>29.90 (-3.57%)</td><td>26.75 (+6.74%)</td><td>23.33 (-3.89%)</td><td>9.00 (-3.96%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.98 (n/a)</td><td>0.67 (n/a)</td><td>0.54 (n/a)</td><td>0.52 (n/a)</td><td>0.20 (n/a)</td><td>691.20 (n/a)</td><td>576.04 (n/a)</td><td>669.50 (n/a)</td><td>367.90 (n/a)</td><td>146.36 (n/a)</td><td>45.61 (n/a)</td><td>31.01 (n/a)</td><td>25.06 (n/a)</td><td>24.27 (n/a)</td><td>9.37 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.70 (+4.91%)</td><td>2.02 (+8.99%)</td><td>1.71 (-9.37%)</td><td>1.39 <b>(+26.12%)</b></td><td>0.62 (+17.77%)</td><td>3022.50 <b>(-20.71%)</b></td><td>2232.60 (-8.49%)</td><td>2450.80 (+10.34%)</td><td>1555.80 (-4.67%)</td><td>650.89 <b>(-20.66%)</b></td><td>690.17 (+4.91%)</td><td>517.69 (+8.99%)</td><td>438.13 (-9.37%)</td><td>355.25 <b>(+26.12%)</b></td><td>159.16 (+17.77%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.57 (n/a)</td><td>1.86 (n/a)</td><td>1.89 (n/a)</td><td>1.10 (n/a)</td><td>0.53 (n/a)</td><td>3812.00 (n/a)</td><td>2439.66 (n/a)</td><td>2221.20 (n/a)</td><td>1632.10 (n/a)</td><td>820.40 (n/a)</td><td>657.90 (n/a)</td><td>475.00 (n/a)</td><td>483.41 (n/a)</td><td>281.67 (n/a)</td><td>135.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.83 (-6.66%)</td><td>2.48 (+17.66%)</td><td>2.73 (+19.52%)</td><td>1.79 <b>(+56.39%)</b></td><td>0.46 <b>(-49.11%)</b></td><td>1466.90 <b>(-36.06%)</b></td><td>1091.26 <b>(-26.25%)</b></td><td>959.00 (-16.33%)</td><td>926.00 (+7.14%)</td><td>233.20 <b>(-66.75%)</b></td><td>579.75 (-6.66%)</td><td>507.87 (+17.66%)</td><td>559.84 (+19.52%)</td><td>365.99 <b>(+56.39%)</b></td><td>93.61 <b>(-49.11%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.03 (n/a)</td><td>2.11 (n/a)</td><td>2.29 (n/a)</td><td>1.14 (n/a)</td><td>0.90 (n/a)</td><td>2294.10 (n/a)</td><td>1479.66 (n/a)</td><td>1146.20 (n/a)</td><td>864.30 (n/a)</td><td>701.34 (n/a)</td><td>621.14 (n/a)</td><td>431.63 (n/a)</td><td>468.40 (n/a)</td><td>234.03 (n/a)</td><td>183.94 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.01 (+9.15%)</td><td>2.40 (+15.85%)</td><td>2.48 <b>(+31.85%)</b></td><td>1.94 <b>(+36.91%)</b></td><td>0.45 (-18.38%)</td><td>4056.50 <b>(-26.96%)</b></td><td>3370.94 (-16.24%)</td><td>3172.40 <b>(-24.16%)</b></td><td>2610.80 (-8.38%)</td><td>633.70 <b>(-41.82%)</b></td><td>925.35 (+9.15%)</td><td>737.51 (+15.85%)</td><td>761.54 <b>(+31.85%)</b></td><td>595.57 <b>(+36.91%)</b></td><td>139.45 (-18.38%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.76 (n/a)</td><td>2.07 (n/a)</td><td>1.88 (n/a)</td><td>1.42 (n/a)</td><td>0.56 (n/a)</td><td>5553.80 (n/a)</td><td>4024.62 (n/a)</td><td>4182.80 (n/a)</td><td>2849.70 (n/a)</td><td>1089.28 (n/a)</td><td>847.77 (n/a)</td><td>636.62 (n/a)</td><td>577.58 (n/a)</td><td>435.00 (n/a)</td><td>170.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.40 (n/a)</td><td>330.38 (n/a)</td><td>285.30 (n/a)</td><td>246.30 (n/a)</td><td>130.68 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>594.10 (n/a)</td><td>432.36 (n/a)</td><td>446.90 (n/a)</td><td>244.00 (n/a)</td><td>145.29 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>451.80 (n/a)</td><td>345.62 (n/a)</td><td>283.20 (n/a)</td><td>272.20 (n/a)</td><td>93.49 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1044.40 (n/a)</td><td>600.32 (n/a)</td><td>588.30 (n/a)</td><td>255.90 (n/a)</td><td>286.06 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>998.60 (n/a)</td><td>623.28 (n/a)</td><td>578.50 (n/a)</td><td>303.50 (n/a)</td><td>250.07 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>561.50 (n/a)</td><td>450.98 (n/a)</td><td>470.60 (n/a)</td><td>336.20 (n/a)</td><td>97.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.30 (n/a)</td><td>328.26 (n/a)</td><td>298.80 (n/a)</td><td>242.80 (n/a)</td><td>115.83 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>741.90 (n/a)</td><td>427.98 (n/a)</td><td>388.00 (n/a)</td><td>236.30 (n/a)</td><td>212.67 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>482.60 (n/a)</td><td>310.14 (n/a)</td><td>276.20 (n/a)</td><td>238.60 (n/a)</td><td>97.82 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>467.50 (n/a)</td><td>378.70 (n/a)</td><td>438.40 (n/a)</td><td>214.20 (n/a)</td><td>107.88 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1052.40 (n/a)</td><td>585.98 (n/a)</td><td>566.40 (n/a)</td><td>234.60 (n/a)</td><td>296.46 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>453.80 (n/a)</td><td>372.80 (n/a)</td><td>386.30 (n/a)</td><td>293.00 (n/a)</td><td>63.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1895.80 (n/a)</td><td>707.92 (n/a)</td><td>475.00 (n/a)</td><td>256.30 (n/a)</td><td>675.17 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>572.30 (n/a)</td><td>376.52 (n/a)</td><td>297.50 (n/a)</td><td>231.20 (n/a)</td><td>144.78 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>309.70 (n/a)</td><td>296.98 (n/a)</td><td>307.50 (n/a)</td><td>275.40 (n/a)</td><td>15.93 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>467.20 (n/a)</td><td>336.48 (n/a)</td><td>273.90 (n/a)</td><td>229.00 (n/a)</td><td>110.45 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2028.40 (n/a)</td><td>674.00 (n/a)</td><td>290.90 (n/a)</td><td>265.00 (n/a)</td><td>764.62 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>645.20 (n/a)</td><td>447.02 (n/a)</td><td>425.70 (n/a)</td><td>300.70 (n/a)</td><td>144.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>515.00 (n/a)</td><td>429.82 (n/a)</td><td>472.60 (n/a)</td><td>334.50 (n/a)</td><td>86.80 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>614.30 (n/a)</td><td>382.30 (n/a)</td><td>273.50 (n/a)</td><td>262.20 (n/a)</td><td>162.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>654.20 (n/a)</td><td>491.10 (n/a)</td><td>576.20 (n/a)</td><td>313.80 (n/a)</td><td>158.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>492.10 (n/a)</td><td>332.78 (n/a)</td><td>319.60 (n/a)</td><td>257.50 (n/a)</td><td>95.48 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1927.70 (n/a)</td><td>760.04 (n/a)</td><td>575.60 (n/a)</td><td>262.50 (n/a)</td><td>666.27 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>652.80 (n/a)</td><td>475.68 (n/a)</td><td>393.10 (n/a)</td><td>315.00 (n/a)</td><td>163.08 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.62 (-9.18%)</td><td>0.43 (-18.59%)</td><td>0.43 (-19.61%)</td><td>0.24 <b>(-22.11%)</b></td><td>0.15 (+5.97%)</td><td>926.10 <b>(+28.39%)</b></td><td>575.86 <b>(+26.99%)</b></td><td>517.80 <b>(+24.41%)</b></td><td>356.30 (+10.11%)</td><td>221.03 <b>(+42.94%)</b></td><td>26.49 (-9.18%)</td><td>18.21 (-18.59%)</td><td>18.23 (-19.61%)</td><td>10.19 <b>(-22.11%)</b></td><td>6.20 (+5.97%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.68 (n/a)</td><td>0.52 (n/a)</td><td>0.53 (n/a)</td><td>0.31 (n/a)</td><td>0.14 (n/a)</td><td>721.30 (n/a)</td><td>453.46 (n/a)</td><td>416.20 (n/a)</td><td>323.60 (n/a)</td><td>154.63 (n/a)</td><td>29.17 (n/a)</td><td>22.36 (n/a)</td><td>22.67 (n/a)</td><td>13.08 (n/a)</td><td>5.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.45 (-5.82%)</td><td>0.38 (-8.95%)</td><td>0.38 (-12.75%)</td><td>0.30 (-13.36%)</td><td>0.06 (+9.79%)</td><td>735.30 (+15.41%)</td><td>588.96 (+10.60%)</td><td>582.60 (+14.62%)</td><td>494.10 (+6.19%)</td><td>100.69 <b>(+33.20%)</b></td><td>19.10 (-5.82%)</td><td>16.39 (-8.95%)</td><td>16.20 (-12.75%)</td><td>12.83 (-13.36%)</td><td>2.68 (+9.79%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.48 (n/a)</td><td>0.42 (n/a)</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.06 (n/a)</td><td>637.10 (n/a)</td><td>532.50 (n/a)</td><td>508.30 (n/a)</td><td>465.30 (n/a)</td><td>75.59 (n/a)</td><td>20.28 (n/a)</td><td>18.00 (n/a)</td><td>18.57 (n/a)</td><td>14.81 (n/a)</td><td>2.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.30 (-2.66%)</td><td>0.30 (-1.99%)</td><td>0.30 (-1.59%)</td><td>0.29 (-1.75%)</td><td>0.00 <b>(-43.93%)</b></td><td>85744.90 (+1.78%)</td><td>84321.24 (+2.01%)</td><td>84304.60 (+1.61%)</td><td>83169.80 (+2.73%)</td><td>930.22 <b>(-41.22%)</b></td><td>206.56 (-2.66%)</td><td>203.76 (-1.99%)</td><td>203.78 (-1.59%)</td><td>200.36 (-1.75%)</td><td>2.24 <b>(-43.93%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84241.50 (n/a)</td><td>82658.54 (n/a)</td><td>82968.40 (n/a)</td><td>80959.10 (n/a)</td><td>1582.46 (n/a)</td><td>212.20 (n/a)</td><td>207.90 (n/a)</td><td>207.07 (n/a)</td><td>203.94 (n/a)</td><td>3.99 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.15 (+0.48%)</td><td>1.14 (+2.12%)</td><td>1.15 (+1.03%)</td><td>1.11 (+5.44%)</td><td>0.02 <b>(-54.92%)</b></td><td>22694.80 (-5.16%)</td><td>22072.46 (-2.15%)</td><td>21922.20 (-1.02%)</td><td>21887.30 (-0.48%)</td><td>348.52 <b>(-57.41%)</b></td><td>784.93 (+0.48%)</td><td>778.49 (+2.12%)</td><td>783.68 (+1.03%)</td><td>757.00 (+5.44%)</td><td>12.04 <b>(-54.92%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.14 (n/a)</td><td>1.12 (n/a)</td><td>1.14 (n/a)</td><td>1.05 (n/a)</td><td>0.04 (n/a)</td><td>23929.60 (n/a)</td><td>22558.10 (n/a)</td><td>22148.00 (n/a)</td><td>21993.00 (n/a)</td><td>818.36 (n/a)</td><td>781.15 (n/a)</td><td>762.36 (n/a)</td><td>775.68 (n/a)</td><td>717.93 (n/a)</td><td>26.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.80 (+0.51%)</td><td>0.80 (+0.22%)</td><td>0.80 (+0.41%)</td><td>0.78 (-0.13%)</td><td>0.01 <b>(+27.34%)</b></td><td>97060.10 (+0.13%)</td><td>94952.76 (-0.22%)</td><td>94483.50 (-0.41%)</td><td>93851.40 (-0.51%)</td><td>1358.83 <b>(+26.69%)</b></td><td>732.22 (+0.51%)</td><td>723.84 (+0.22%)</td><td>727.32 (+0.41%)</td><td>708.01 (-0.13%)</td><td>10.26 <b>(+27.34%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>96938.00 (n/a)</td><td>95159.92 (n/a)</td><td>94868.30 (n/a)</td><td>94330.20 (n/a)</td><td>1072.55 (n/a)</td><td>728.50 (n/a)</td><td>722.22 (n/a)</td><td>724.37 (n/a)</td><td>708.90 (n/a)</td><td>8.06 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.78 (+0.50%)</td><td>0.76 (-0.43%)</td><td>0.78 (+0.77%)</td><td>0.71 (-5.32%)</td><td>0.03 <b>(+164.98%)</b></td><td>105915.50 (+5.62%)</td><td>99182.16 (+0.53%)</td><td>97340.30 (-0.76%)</td><td>96950.90 (-0.50%)</td><td>3813.69 <b>(+179.26%)</b></td><td>708.81 (+0.50%)</td><td>693.64 (-0.43%)</td><td>705.97 (+0.77%)</td><td>648.81 (-5.32%)</td><td>25.45 <b>(+164.98%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100280.50 (n/a)</td><td>98662.86 (n/a)</td><td>98085.10 (n/a)</td><td>97434.80 (n/a)</td><td>1365.63 (n/a)</td><td>705.29 (n/a)</td><td>696.61 (n/a)</td><td>700.61 (n/a)</td><td>685.27 (n/a)</td><td>9.60 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.89 (-0.62%)</td><td>0.88 (-1.32%)</td><td>0.88 (-1.48%)</td><td>0.87 (-1.52%)</td><td>0.01 <b>(+60.73%)</b></td><td>87195.40 (+1.55%)</td><td>85883.22 (+1.34%)</td><td>85646.90 (+1.50%)</td><td>84851.80 (+0.63%)</td><td>1076.36 <b>(+64.10%)</b></td><td>809.88 (-0.62%)</td><td>800.25 (-1.32%)</td><td>802.36 (-1.48%)</td><td>788.11 (-1.52%)</td><td>10.00 <b>(+60.73%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.01 (n/a)</td><td>85866.20 (n/a)</td><td>84745.84 (n/a)</td><td>84381.20 (n/a)</td><td>84323.90 (n/a)</td><td>655.91 (n/a)</td><td>814.95 (n/a)</td><td>810.93 (n/a)</td><td>814.39 (n/a)</td><td>800.31 (n/a)</td><td>6.22 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>5.22 (-7.66%)</td><td>3.52 (-18.79%)</td><td>3.39 <b>(-28.74%)</b></td><td>2.14 (-13.66%)</td><td>1.18 (-10.12%)</td><td>4166.70 (+15.82%)</td><td>2780.96 <b>(+23.11%)</b></td><td>2625.50 <b>(+40.34%)</b></td><td>1707.40 (+8.30%)</td><td>948.04 (+13.02%)</td><td>314.43 (-7.66%)</td><td>211.74 (-18.79%)</td><td>204.48 <b>(-28.74%)</b></td><td>128.85 (-13.66%)</td><td>71.34 (-10.12%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>5.65 (n/a)</td><td>4.33 (n/a)</td><td>4.76 (n/a)</td><td>2.48 (n/a)</td><td>1.32 (n/a)</td><td>3597.50 (n/a)</td><td>2258.92 (n/a)</td><td>1870.80 (n/a)</td><td>1576.60 (n/a)</td><td>838.80 (n/a)</td><td>340.53 (n/a)</td><td>260.73 (n/a)</td><td>286.97 (n/a)</td><td>149.23 (n/a)</td><td>79.37 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.29 (+19.70%)</td><td>2.98 <b>(+29.84%)</b></td><td>3.21 <b>(+47.22%)</b></td><td>2.28 <b>(+25.83%)</b></td><td>0.43 (+17.94%)</td><td>3903.20 <b>(-20.53%)</b></td><td>3051.58 <b>(-23.10%)</b></td><td>2772.30 <b>(-32.08%)</b></td><td>2711.40 (-16.46%)</td><td>510.59 <b>(-21.61%)</b></td><td>198.00 (+19.70%)</td><td>179.41 <b>(+29.84%)</b></td><td>193.65 <b>(+47.22%)</b></td><td>137.55 <b>(+25.83%)</b></td><td>26.09 (+17.94%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.75 (n/a)</td><td>2.29 (n/a)</td><td>2.18 (n/a)</td><td>1.81 (n/a)</td><td>0.37 (n/a)</td><td>4911.30 (n/a)</td><td>3968.10 (n/a)</td><td>4081.50 (n/a)</td><td>3245.70 (n/a)</td><td>651.36 (n/a)</td><td>165.41 (n/a)</td><td>138.18 (n/a)</td><td>131.54 (n/a)</td><td>109.31 (n/a)</td><td>22.12 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>5.95 (+9.96%)</td><td>4.09 (+4.36%)</td><td>3.63 (-0.38%)</td><td>2.21 (+0.70%)</td><td>1.60 <b>(+20.30%)</b></td><td>4025.20 (-0.70%)</td><td>2488.54 (-1.51%)</td><td>2452.40 (+0.38%)</td><td>1497.10 (-9.06%)</td><td>1031.22 (+6.40%)</td><td>358.60 (+9.96%)</td><td>246.44 (+4.36%)</td><td>218.92 (-0.38%)</td><td>133.38 (+0.70%)</td><td>96.33 <b>(+20.30%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>5.41 (n/a)</td><td>3.92 (n/a)</td><td>3.65 (n/a)</td><td>2.20 (n/a)</td><td>1.33 (n/a)</td><td>4053.40 (n/a)</td><td>2526.68 (n/a)</td><td>2443.00 (n/a)</td><td>1646.30 (n/a)</td><td>969.15 (n/a)</td><td>326.11 (n/a)</td><td>236.15 (n/a)</td><td>219.76 (n/a)</td><td>132.45 (n/a)</td><td>80.08 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>6.57 (-0.20%)</td><td>5.89 (+6.13%)</td><td>5.88 (+3.61%)</td><td>5.00 (+4.21%)</td><td>0.59 <b>(-22.31%)</b></td><td>6968.90 (-4.04%)</td><td>5968.70 (-6.36%)</td><td>5934.20 (-3.49%)</td><td>5304.50 (+0.20%)</td><td>628.39 <b>(-26.49%)</b></td><td>404.84 (-0.20%)</td><td>362.82 (+6.13%)</td><td>361.88 (+3.61%)</td><td>308.15 (+4.21%)</td><td>36.11 <b>(-22.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>6.59 (n/a)</td><td>5.55 (n/a)</td><td>5.67 (n/a)</td><td>4.80 (n/a)</td><td>0.75 (n/a)</td><td>7262.00 (n/a)</td><td>6374.12 (n/a)</td><td>6148.50 (n/a)</td><td>5293.80 (n/a)</td><td>854.81 (n/a)</td><td>405.66 (n/a)</td><td>341.87 (n/a)</td><td>349.27 (n/a)</td><td>295.71 (n/a)</td><td>46.48 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>5.16 (-14.87%)</td><td>4.60 (-5.83%)</td><td>4.69 (+0.49%)</td><td>3.69 (-13.01%)</td><td>0.57 <b>(-24.96%)</b></td><td>9451.60 (+14.95%)</td><td>7683.32 (+5.77%)</td><td>7437.30 (-0.49%)</td><td>6760.20 (+17.46%)</td><td>1054.96 (+2.40%)</td><td>317.67 (-14.87%)</td><td>283.31 (-5.83%)</td><td>288.75 (+0.49%)</td><td>227.21 (-13.01%)</td><td>34.83 <b>(-24.96%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>6.06 (n/a)</td><td>4.88 (n/a)</td><td>4.67 (n/a)</td><td>4.24 (n/a)</td><td>0.75 (n/a)</td><td>8222.20 (n/a)</td><td>7264.26 (n/a)</td><td>7473.70 (n/a)</td><td>5755.30 (n/a)</td><td>1030.24 (n/a)</td><td>373.13 (n/a)</td><td>300.86 (n/a)</td><td>287.34 (n/a)</td><td>261.18 (n/a)</td><td>46.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>7.21 (+1.34%)</td><td>5.83 (-8.55%)</td><td>5.04 <b>(-21.13%)</b></td><td>5.01 (-9.81%)</td><td>1.11 <b>(+71.72%)</b></td><td>6958.90 (+10.88%)</td><td>6146.46 (+11.46%)</td><td>6913.30 <b>(+26.78%)</b></td><td>4838.30 (-1.32%)</td><td>1092.94 <b>(+91.71%)</b></td><td>443.85 (+1.34%)</td><td>359.14 (-8.55%)</td><td>310.63 <b>(-21.13%)</b></td><td>308.60 (-9.81%)</td><td>68.56 <b>(+71.72%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>7.11 (n/a)</td><td>6.38 (n/a)</td><td>6.39 (n/a)</td><td>5.56 (n/a)</td><td>0.65 (n/a)</td><td>6276.30 (n/a)</td><td>5514.70 (n/a)</td><td>5452.80 (n/a)</td><td>4903.10 (n/a)</td><td>570.10 (n/a)</td><td>437.98 (n/a)</td><td>392.71 (n/a)</td><td>393.83 (n/a)</td><td>342.16 (n/a)</td><td>39.93 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.79 (+3.67%)</td><td>0.78 (+2.35%)</td><td>0.78 (+2.23%)</td><td>0.77 (+1.73%)</td><td>0.01 <b>(+112.29%)</b></td><td>98685.70 (-1.71%)</td><td>96764.42 (-2.28%)</td><td>96519.30 (-2.18%)</td><td>95057.70 (-3.54%)</td><td>1559.85 <b>(+101.13%)</b></td><td>722.92 (+3.67%)</td><td>710.32 (+2.35%)</td><td>711.98 (+2.23%)</td><td>696.35 (+1.73%)</td><td>11.42 <b>(+112.29%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100397.80 (n/a)</td><td>99024.94 (n/a)</td><td>98674.10 (n/a)</td><td>98543.20 (n/a)</td><td>775.53 (n/a)</td><td>697.35 (n/a)</td><td>694.00 (n/a)</td><td>696.43 (n/a)</td><td>684.47 (n/a)</td><td>5.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.78 (+0.98%)</td><td>0.77 (+1.62%)</td><td>0.77 (+1.08%)</td><td>0.76 (+4.62%)</td><td>0.01 <b>(-63.31%)</b></td><td>99076.60 (-4.42%)</td><td>98275.28 (-1.63%)</td><td>98489.10 (-1.07%)</td><td>97182.00 (-0.97%)</td><td>761.76 <b>(-65.38%)</b></td><td>707.12 (+0.98%)</td><td>699.29 (+1.62%)</td><td>697.74 (+1.08%)</td><td>693.60 (+4.62%)</td><td>5.44 <b>(-63.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.73 (n/a)</td><td>0.02 (n/a)</td><td>103657.50 (n/a)</td><td>99904.68 (n/a)</td><td>99550.20 (n/a)</td><td>98136.40 (n/a)</td><td>2200.62 (n/a)</td><td>700.24 (n/a)</td><td>688.11 (n/a)</td><td>690.30 (n/a)</td><td>662.95 (n/a)</td><td>14.82 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.89 (-0.61%)</td><td>0.88 (-1.68%)</td><td>0.88 (-2.43%)</td><td>0.87 (-1.86%)</td><td>0.01 <b>(+124.30%)</b></td><td>86379.00 (+1.90%)</td><td>85697.20 (+1.71%)</td><td>86198.30 (+2.49%)</td><td>84403.10 (+0.61%)</td><td>879.22 <b>(+130.22%)</b></td><td>814.18 (-0.61%)</td><td>801.96 (-1.68%)</td><td>797.23 (-2.43%)</td><td>795.56 (-1.86%)</td><td>8.28 <b>(+124.30%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.00 (n/a)</td><td>84768.60 (n/a)</td><td>84255.34 (n/a)</td><td>84100.60 (n/a)</td><td>83887.90 (n/a)</td><td>381.90 (n/a)</td><td>819.18 (n/a)</td><td>815.62 (n/a)</td><td>817.11 (n/a)</td><td>810.67 (n/a)</td><td>3.69 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.19 (-13.43%)</td><td>1.90 <b>(-40.95%)</b></td><td>1.62 <b>(-52.88%)</b></td><td>1.38 <b>(-31.21%)</b></td><td>0.73 (+6.96%)</td><td>5825.80 <b>(+45.36%)</b></td><td>4620.38 <b>(+75.20%)</b></td><td>4978.30 <b>(+112.21%)</b></td><td>2527.90 (+15.51%)</td><td>1238.01 <b>(+60.84%)</b></td><td>836.24 (-13.43%)</td><td>497.95 <b>(-40.95%)</b></td><td>424.62 <b>(-52.88%)</b></td><td>362.85 <b>(-31.21%)</b></td><td>191.53 (+6.96%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.68 (n/a)</td><td>3.22 (n/a)</td><td>3.44 (n/a)</td><td>2.01 (n/a)</td><td>0.68 (n/a)</td><td>4007.80 (n/a)</td><td>2637.16 (n/a)</td><td>2345.90 (n/a)</td><td>2188.40 (n/a)</td><td>769.73 (n/a)</td><td>965.96 (n/a)</td><td>843.30 (n/a)</td><td>901.12 (n/a)</td><td>527.45 (n/a)</td><td>179.07 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.21 <b>(-31.40%)</b></td><td>0.19 (-14.17%)</td><td>0.19 (-8.54%)</td><td>0.18 <b>(+23.08%)</b></td><td>0.01 <b>(-81.69%)</b></td><td>6813.70 (-18.75%)</td><td>6439.44 (+9.77%)</td><td>6416.00 (+9.34%)</td><td>5933.20 <b>(+45.77%)</b></td><td>367.11 <b>(-78.05%)</b></td><td>11.31 <b>(-31.40%)</b></td><td>10.45 (-14.17%)</td><td>10.46 (-8.54%)</td><td>9.85 <b>(+23.08%)</b></td><td>0.61 <b>(-81.69%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>8386.50 (n/a)</td><td>5866.36 (n/a)</td><td>5868.00 (n/a)</td><td>4070.30 (n/a)</td><td>1672.84 (n/a)</td><td>16.49 (n/a)</td><td>12.17 (n/a)</td><td>11.44 (n/a)</td><td>8.00 (n/a)</td><td>3.30 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.87 (n/a)</td><td>3.61 (n/a)</td><td>3.60 (n/a)</td><td>3.38 (n/a)</td><td>0.21 (n/a)</td><td>3.87 (n/a)</td><td>3.61 (n/a)</td><td>3.60 (n/a)</td><td>3.37 (n/a)</td><td>0.21 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>7.04 (-6.09%)</td><td>6.16 (-10.85%)</td><td>5.78 (-16.93%)</td><td>5.60 (-10.43%)</td><td>0.66 <b>(+40.71%)</b></td><td>7.03 (-6.09%)</td><td>6.16 (-10.85%)</td><td>5.78 (-16.93%)</td><td>5.60 (-10.43%)</td><td>0.66 <b>(+40.71%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>7.49 (n/a)</td><td>6.92 (n/a)</td><td>6.96 (n/a)</td><td>6.26 (n/a)</td><td>0.47 (n/a)</td><td>7.49 (n/a)</td><td>6.91 (n/a)</td><td>6.96 (n/a)</td><td>6.25 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>13.88 (+1.78%)</td><td>10.98 (+11.09%)</td><td>9.57 (+0.85%)</td><td>8.40 (+4.43%)</td><td>2.60 (+15.56%)</td><td>13.87 (+1.78%)</td><td>10.97 (+11.09%)</td><td>9.56 (+0.85%)</td><td>8.40 (+4.43%)</td><td>2.60 (+15.56%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>13.63 (n/a)</td><td>9.89 (n/a)</td><td>9.49 (n/a)</td><td>8.04 (n/a)</td><td>2.25 (n/a)</td><td>13.63 (n/a)</td><td>9.88 (n/a)</td><td>9.48 (n/a)</td><td>8.04 (n/a)</td><td>2.25 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.76 (n/a)</td><td>3.60 (n/a)</td><td>3.58 (n/a)</td><td>3.51 (n/a)</td><td>0.10 (n/a)</td><td>3.75 (n/a)</td><td>3.60 (n/a)</td><td>3.58 (n/a)</td><td>3.50 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>7.11 (+1.19%)</td><td>6.50 (-0.96%)</td><td>6.88 (+1.30%)</td><td>4.98 (-12.89%)</td><td>0.89 <b>(+69.58%)</b></td><td>7.11 (+1.19%)</td><td>6.50 (-0.96%)</td><td>6.87 (+1.30%)</td><td>4.98 (-12.89%)</td><td>0.89 <b>(+69.58%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>7.03 (n/a)</td><td>6.57 (n/a)</td><td>6.79 (n/a)</td><td>5.72 (n/a)</td><td>0.53 (n/a)</td><td>7.02 (n/a)</td><td>6.56 (n/a)</td><td>6.78 (n/a)</td><td>5.72 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>14.03 (+1.52%)</td><td>10.67 (+1.88%)</td><td>9.72 (-2.21%)</td><td>7.60 (-2.01%)</td><td>3.04 (+19.55%)</td><td>14.02 (+1.52%)</td><td>10.67 (+1.88%)</td><td>9.72 (-2.21%)</td><td>7.60 (-2.01%)</td><td>3.03 (+19.55%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>13.82 (n/a)</td><td>10.48 (n/a)</td><td>9.94 (n/a)</td><td>7.76 (n/a)</td><td>2.54 (n/a)</td><td>13.81 (n/a)</td><td>10.47 (n/a)</td><td>9.94 (n/a)</td><td>7.75 (n/a)</td><td>2.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.28 (+5.12%)</td><td>2.26 <b>(+21.11%)</b></td><td>2.47 <b>(+107.16%)</b></td><td>1.04 (+0.64%)</td><td>0.90 (-15.62%)</td><td>3.28 (+5.12%)</td><td>2.26 <b>(+21.11%)</b></td><td>2.46 <b>(+107.16%)</b></td><td>1.04 (+0.64%)</td><td>0.90 (-15.62%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.12 (n/a)</td><td>1.87 (n/a)</td><td>1.19 (n/a)</td><td>1.03 (n/a)</td><td>1.07 (n/a)</td><td>3.12 (n/a)</td><td>1.86 (n/a)</td><td>1.19 (n/a)</td><td>1.03 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.36 <b>(-35.51%)</b></td><td>0.18 <b>(-53.52%)</b></td><td>0.08 <b>(-84.46%)</b></td><td>0.07 (-0.79%)</td><td>0.14 <b>(-30.20%)</b></td><td>0.35 <b>(-35.51%)</b></td><td>0.18 <b>(-53.52%)</b></td><td>0.08 <b>(-84.46%)</b></td><td>0.07 (-0.79%)</td><td>0.14 <b>(-30.20%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.56 (n/a)</td><td>0.39 (n/a)</td><td>0.51 (n/a)</td><td>0.08 (n/a)</td><td>0.21 (n/a)</td><td>0.55 (n/a)</td><td>0.38 (n/a)</td><td>0.50 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.73 (-13.41%)</td><td>0.36 <b>(-30.87%)</b></td><td>0.30 <b>(-52.92%)</b></td><td>0.11 <b>(+37.98%)</b></td><td>0.23 <b>(-21.53%)</b></td><td>0.72 (-13.41%)</td><td>0.36 <b>(-30.87%)</b></td><td>0.29 <b>(-52.92%)</b></td><td>0.11 <b>(+37.98%)</b></td><td>0.23 <b>(-21.53%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.84 (n/a)</td><td>0.53 (n/a)</td><td>0.63 (n/a)</td><td>0.08 (n/a)</td><td>0.29 (n/a)</td><td>0.83 (n/a)</td><td>0.52 (n/a)</td><td>0.63 (n/a)</td><td>0.08 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.29 (-12.55%)</td><td>1.09 <b>(-49.50%)</b></td><td>0.74 <b>(-67.95%)</b></td><td>0.42 <b>(-75.16%)</b></td><td>0.82 <b>(+111.95%)</b></td><td>2.25 (-12.55%)</td><td>1.08 <b>(-49.50%)</b></td><td>0.73 <b>(-67.95%)</b></td><td>0.41 <b>(-75.16%)</b></td><td>0.80 <b>(+111.95%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.62 (n/a)</td><td>2.16 (n/a)</td><td>2.32 (n/a)</td><td>1.69 (n/a)</td><td>0.39 (n/a)</td><td>2.58 (n/a)</td><td>2.13 (n/a)</td><td>2.28 (n/a)</td><td>1.66 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>502.20 (n/a)</td><td>339.06 (n/a)</td><td>274.80 (n/a)</td><td>270.70 (n/a)</td><td>101.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>549.30 (n/a)</td><td>391.24 (n/a)</td><td>321.60 (n/a)</td><td>241.80 (n/a)</td><td>144.04 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.40 (n/a)</td><td>397.76 (n/a)</td><td>452.80 (n/a)</td><td>268.90 (n/a)</td><td>112.00 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>497.70 (n/a)</td><td>407.22 (n/a)</td><td>434.90 (n/a)</td><td>288.00 (n/a)</td><td>93.02 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>718.30 (n/a)</td><td>473.00 (n/a)</td><td>439.40 (n/a)</td><td>343.30 (n/a)</td><td>147.84 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.00 (n/a)</td><td>430.68 (n/a)</td><td>459.30 (n/a)</td><td>266.20 (n/a)</td><td>106.05 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.30 (n/a)</td><td>415.56 (n/a)</td><td>465.30 (n/a)</td><td>277.40 (n/a)</td><td>124.67 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2086.80 (n/a)</td><td>708.74 (n/a)</td><td>303.20 (n/a)</td><td>269.40 (n/a)</td><td>783.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.00 (n/a)</td><td>397.02 (n/a)</td><td>486.80 (n/a)</td><td>198.80 (n/a)</td><td>149.79 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.70 (n/a)</td><td>383.22 (n/a)</td><td>320.40 (n/a)</td><td>293.60 (n/a)</td><td>109.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1047.20 (n/a)</td><td>546.96 (n/a)</td><td>473.40 (n/a)</td><td>227.70 (n/a)</td><td>312.29 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>999.80 (n/a)</td><td>606.98 (n/a)</td><td>465.20 (n/a)</td><td>407.30 (n/a)</td><td>253.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>697.10 (n/a)</td><td>496.06 (n/a)</td><td>520.20 (n/a)</td><td>275.00 (n/a)</td><td>154.17 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>627.60 (n/a)</td><td>467.26 (n/a)</td><td>488.70 (n/a)</td><td>245.50 (n/a)</td><td>138.56 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>534.40 (n/a)</td><td>319.04 (n/a)</td><td>277.30 (n/a)</td><td>234.00 (n/a)</td><td>122.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>551.50 (n/a)</td><td>358.00 (n/a)</td><td>341.50 (n/a)</td><td>276.80 (n/a)</td><td>112.80 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>648.30 (n/a)</td><td>440.42 (n/a)</td><td>420.00 (n/a)</td><td>292.60 (n/a)</td><td>148.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2037.10 (n/a)</td><td>738.84 (n/a)</td><td>500.70 (n/a)</td><td>291.10 (n/a)</td><td>734.78 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>529.60 (n/a)</td><td>312.58 (n/a)</td><td>275.30 (n/a)</td><td>175.40 (n/a)</td><td>132.99 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>638.40 (n/a)</td><td>429.68 (n/a)</td><td>449.10 (n/a)</td><td>228.20 (n/a)</td><td>182.58 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>454.60 (n/a)</td><td>300.24 (n/a)</td><td>273.60 (n/a)</td><td>247.00 (n/a)</td><td>87.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>600.90 (n/a)</td><td>410.70 (n/a)</td><td>319.00 (n/a)</td><td>288.60 (n/a)</td><td>152.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2255.10 (n/a)</td><td>905.04 (n/a)</td><td>646.70 (n/a)</td><td>297.90 (n/a)</td><td>772.35 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>553.90 (n/a)</td><td>453.12 (n/a)</td><td>483.90 (n/a)</td><td>320.20 (n/a)</td><td>90.17 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (-11.00%)</td><td>0.01 (-16.23%)</td><td>0.01 <b>(-21.45%)</b></td><td>0.01 (-1.69%)</td><td>0.00 (-7.25%)</td><td>446.90 (+1.71%)</td><td>362.48 (+19.17%)</td><td>367.80 <b>(+27.31%)</b></td><td>272.30 (+12.33%)</td><td>80.81 (+2.86%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>439.40 (n/a)</td><td>304.18 (n/a)</td><td>288.90 (n/a)</td><td>242.40 (n/a)</td><td>78.56 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 <b>(-24.33%)</b></td><td>0.01 <b>(-20.42%)</b></td><td>0.01 <b>(-23.72%)</b></td><td>0.01 (-3.77%)</td><td>0.00 <b>(-35.08%)</b></td><td>633.20 (+3.91%)</td><td>478.28 (+18.02%)</td><td>560.50 <b>(+31.11%)</b></td><td>274.40 <b>(+32.11%)</b></td><td>152.37 (-9.70%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.40 (n/a)</td><td>405.24 (n/a)</td><td>427.50 (n/a)</td><td>207.70 (n/a)</td><td>168.73 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (+4.67%)</td><td>0.01 (+4.12%)</td><td>0.01 (+8.50%)</td><td>0.01 (+17.16%)</td><td>0.01 (+16.13%)</td><td>797.50 (-14.64%)</td><td>399.20 (-4.56%)</td><td>291.10 (-7.82%)</td><td>214.70 (-4.45%)</td><td>244.03 (-16.43%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>934.30 (n/a)</td><td>418.28 (n/a)</td><td>315.80 (n/a)</td><td>224.70 (n/a)</td><td>292.00 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 <b>(-29.74%)</b></td><td>0.01 (-12.29%)</td><td>0.01 (+2.77%)</td><td>0.01 <b>(-30.22%)</b></td><td>0.00 <b>(-34.86%)</b></td><td>763.10 <b>(+43.31%)</b></td><td>484.18 (+12.67%)</td><td>472.30 (-2.70%)</td><td>303.40 <b>(+42.31%)</b></td><td>178.12 <b>(+40.76%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.50 (n/a)</td><td>429.72 (n/a)</td><td>485.40 (n/a)</td><td>213.20 (n/a)</td><td>126.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 <b>(+47.53%)</b></td><td>0.02 <b>(+61.90%)</b></td><td>0.01 <b>(+82.83%)</b></td><td>0.01 <b>(+459.64%)</b></td><td>0.01 (-15.70%)</td><td>377.50 <b>(-82.13%)</b></td><td>275.98 <b>(-62.67%)</b></td><td>275.60 <b>(-45.31%)</b></td><td>168.50 <b>(-32.22%)</b></td><td>77.41 <b>(-90.08%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2112.70 (n/a)</td><td>739.26 (n/a)</td><td>503.90 (n/a)</td><td>248.60 (n/a)</td><td>780.67 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (-12.88%)</td><td>0.01 (-10.55%)</td><td>0.01 (-6.73%)</td><td>0.01 (-13.81%)</td><td>0.00 (-7.15%)</td><td>557.20 (+16.01%)</td><td>442.16 (+12.92%)</td><td>448.20 (+7.22%)</td><td>294.00 (+14.80%)</td><td>110.10 <b>(+32.08%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>480.30 (n/a)</td><td>391.56 (n/a)</td><td>418.00 (n/a)</td><td>256.10 (n/a)</td><td>83.35 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (-13.88%)</td><td>0.03 (-15.38%)</td><td>0.03 (-8.43%)</td><td>0.01 <b>(-25.10%)</b></td><td>0.01 (+2.79%)</td><td>616.90 <b>(+33.50%)</b></td><td>351.44 <b>(+24.06%)</b></td><td>269.80 (+9.19%)</td><td>226.30 (+16.11%)</td><td>163.46 <b>(+53.52%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>462.10 (n/a)</td><td>283.28 (n/a)</td><td>247.10 (n/a)</td><td>194.90 (n/a)</td><td>106.47 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (+11.93%)</td><td>0.02 (+1.98%)</td><td>0.02 (-3.38%)</td><td>0.02 (-3.08%)</td><td>0.01 <b>(+39.61%)</b></td><td>516.50 (+3.18%)</td><td>385.50 (+0.57%)</td><td>385.40 (+3.49%)</td><td>272.10 (-10.64%)</td><td>102.87 <b>(+28.46%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>500.60 (n/a)</td><td>383.30 (n/a)</td><td>372.40 (n/a)</td><td>304.50 (n/a)</td><td>80.08 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 <b>(-21.60%)</b></td><td>0.02 (-14.66%)</td><td>0.02 (-14.07%)</td><td>0.02 (+5.50%)</td><td>0.00 <b>(-42.05%)</b></td><td>482.30 (-5.23%)</td><td>382.28 (+12.13%)</td><td>386.20 (+16.36%)</td><td>287.20 <b>(+27.53%)</b></td><td>74.92 <b>(-30.86%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.90 (n/a)</td><td>340.94 (n/a)</td><td>331.90 (n/a)</td><td>225.20 (n/a)</td><td>108.37 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (-16.16%)</td><td>0.02 (-2.93%)</td><td>0.03 (+9.02%)</td><td>0.01 (+0.25%)</td><td>0.01 <b>(-30.55%)</b></td><td>567.10 (-0.25%)</td><td>359.74 (-1.20%)</td><td>300.60 (-8.27%)</td><td>274.60 (+19.24%)</td><td>120.10 (-13.84%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.50 (n/a)</td><td>364.10 (n/a)</td><td>327.70 (n/a)</td><td>230.30 (n/a)</td><td>139.39 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 <b>(-31.06%)</b></td><td>0.02 <b>(-29.04%)</b></td><td>0.02 <b>(-30.69%)</b></td><td>0.01 (-3.15%)</td><td>0.01 <b>(-41.10%)</b></td><td>567.30 (+3.24%)</td><td>445.74 <b>(+28.93%)</b></td><td>431.70 <b>(+44.28%)</b></td><td>234.10 <b>(+45.04%)</b></td><td>136.19 (-15.32%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.50 (n/a)</td><td>345.72 (n/a)</td><td>299.20 (n/a)</td><td>161.40 (n/a)</td><td>160.82 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (+7.43%)</td><td>0.03 <b>(+22.13%)</b></td><td>0.03 <b>(+74.47%)</b></td><td>0.01 (+0.45%)</td><td>0.01 (+6.45%)</td><td>591.70 (-0.45%)</td><td>359.44 (-18.04%)</td><td>301.50 <b>(-42.68%)</b></td><td>231.10 (-6.93%)</td><td>152.65 (-3.33%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>594.40 (n/a)</td><td>438.58 (n/a)</td><td>526.00 (n/a)</td><td>248.30 (n/a)</td><td>157.91 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 <b>(-24.80%)</b></td><td>0.02 (-19.53%)</td><td>0.02 (+2.31%)</td><td>0.01 <b>(-57.92%)</b></td><td>0.01 (-5.82%)</td><td>1208.50 <b>(+137.61%)</b></td><td>525.86 <b>(+50.48%)</b></td><td>330.40 (-2.25%)</td><td>251.00 <b>(+32.94%)</b></td><td>400.91 <b>(+191.75%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.60 (n/a)</td><td>349.46 (n/a)</td><td>338.00 (n/a)</td><td>188.80 (n/a)</td><td>137.41 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (-11.59%)</td><td>0.02 (-8.57%)</td><td>0.03 (+14.46%)</td><td>0.01 <b>(-33.52%)</b></td><td>0.01 <b>(+22.46%)</b></td><td>690.20 <b>(+50.44%)</b></td><td>420.92 (+18.07%)</td><td>319.90 (-12.62%)</td><td>271.40 (+13.13%)</td><td>180.59 <b>(+109.03%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>458.80 (n/a)</td><td>356.50 (n/a)</td><td>366.10 (n/a)</td><td>239.90 (n/a)</td><td>86.40 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (-10.91%)</td><td>0.06 (+19.20%)</td><td>0.07 <b>(+56.95%)</b></td><td>0.04 <b>(+28.95%)</b></td><td>0.01 <b>(-47.54%)</b></td><td>380.70 <b>(-22.46%)</b></td><td>277.80 <b>(-23.08%)</b></td><td>250.70 <b>(-36.27%)</b></td><td>233.90 (+12.29%)</td><td>59.44 <b>(-53.34%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>491.00 (n/a)</td><td>361.16 (n/a)</td><td>393.40 (n/a)</td><td>208.30 (n/a)</td><td>127.39 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (-7.73%)</td><td>0.06 (+12.42%)</td><td>0.06 (+10.69%)</td><td>0.03 (+19.04%)</td><td>0.01 <b>(-27.55%)</b></td><td>508.80 (-16.00%)</td><td>311.18 (-17.06%)</td><td>273.40 (-9.65%)</td><td>237.40 (+8.40%)</td><td>112.08 <b>(-32.07%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>605.70 (n/a)</td><td>375.18 (n/a)</td><td>302.60 (n/a)</td><td>219.00 (n/a)</td><td>164.99 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (+14.34%)</td><td>0.04 <b>(+29.00%)</b></td><td>0.04 (+13.15%)</td><td>0.02 <b>(+264.34%)</b></td><td>0.02 (-1.63%)</td><td>665.80 <b>(-72.55%)</b></td><td>445.18 <b>(-47.03%)</b></td><td>426.50 (-11.62%)</td><td>248.90 (-12.54%)</td><td>184.45 <b>(-79.36%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2425.90 (n/a)</td><td>840.46 (n/a)</td><td>482.60 (n/a)</td><td>284.60 (n/a)</td><td>893.46 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 <b>(+42.69%)</b></td><td>0.04 (+12.43%)</td><td>0.04 (+10.84%)</td><td>0.02 <b>(-32.18%)</b></td><td>0.02 <b>(+92.41%)</b></td><td>1063.50 <b>(+47.46%)</b></td><td>511.84 (+3.85%)</td><td>398.70 (-9.78%)</td><td>265.40 <b>(-29.92%)</b></td><td>316.41 <b>(+121.69%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>721.20 (n/a)</td><td>492.86 (n/a)</td><td>441.90 (n/a)</td><td>378.70 (n/a)</td><td>142.73 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (-9.06%)</td><td>0.04 (-4.82%)</td><td>0.03 <b>(-21.69%)</b></td><td>0.03 <b>(+27.60%)</b></td><td>0.02 <b>(-21.40%)</b></td><td>519.20 <b>(-21.63%)</b></td><td>408.76 (-1.59%)</td><td>485.00 <b>(+27.70%)</b></td><td>244.80 (+9.97%)</td><td>124.17 <b>(-31.14%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>662.50 (n/a)</td><td>415.36 (n/a)</td><td>379.80 (n/a)</td><td>222.60 (n/a)</td><td>180.32 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (+17.93%)</td><td>0.04 (-4.60%)</td><td>0.03 (-19.98%)</td><td>0.03 (+7.15%)</td><td>0.01 <b>(+24.02%)</b></td><td>623.30 (-6.68%)</td><td>463.20 (+5.68%)</td><td>472.00 <b>(+24.97%)</b></td><td>257.40 (-15.19%)</td><td>132.85 (-9.65%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>667.90 (n/a)</td><td>438.30 (n/a)</td><td>377.70 (n/a)</td><td>303.50 (n/a)</td><td>147.04 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.15 <b>(-28.05%)</b></td><td>0.09 <b>(-32.84%)</b></td><td>0.07 <b>(-43.33%)</b></td><td>0.06 <b>(-43.31%)</b></td><td>0.04 (-0.76%)</td><td>524.90 <b>(+76.44%)</b></td><td>409.68 <b>(+60.73%)</b></td><td>493.80 <b>(+76.42%)</b></td><td>223.80 <b>(+39.01%)</b></td><td>145.26 <b>(+164.18%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>297.50 (n/a)</td><td>254.88 (n/a)</td><td>279.90 (n/a)</td><td>161.00 (n/a)</td><td>54.98 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (-0.51%)</td><td>0.08 <b>(-23.68%)</b></td><td>0.07 <b>(-37.53%)</b></td><td>0.06 (-14.38%)</td><td>0.03 (+1.50%)</td><td>582.70 (+16.80%)</td><td>437.34 <b>(+33.25%)</b></td><td>460.30 <b>(+60.05%)</b></td><td>232.40 (+0.52%)</td><td>137.63 (+19.83%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>498.90 (n/a)</td><td>328.20 (n/a)</td><td>287.60 (n/a)</td><td>231.20 (n/a)</td><td>114.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (-11.58%)</td><td>0.06 <b>(-39.15%)</b></td><td>0.06 <b>(-29.93%)</b></td><td>0.01 <b>(-77.19%)</b></td><td>0.04 <b>(+24.22%)</b></td><td>2422.90 <b>(+338.45%)</b></td><td>955.28 <b>(+153.85%)</b></td><td>517.20 <b>(+42.72%)</b></td><td>273.20 (+13.08%)</td><td>868.31 <b>(+565.02%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>552.60 (n/a)</td><td>376.32 (n/a)</td><td>362.40 (n/a)</td><td>241.60 (n/a)</td><td>130.57 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 <b>(+28.32%)</b></td><td>0.10 <b>(+41.22%)</b></td><td>0.11 <b>(+69.56%)</b></td><td>0.07 <b>(+25.20%)</b></td><td>0.02 <b>(+30.70%)</b></td><td>451.40 <b>(-20.12%)</b></td><td>334.10 <b>(-28.88%)</b></td><td>298.70 <b>(-41.03%)</b></td><td>250.50 <b>(-22.06%)</b></td><td>79.57 (-14.37%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>565.10 (n/a)</td><td>469.74 (n/a)</td><td>506.50 (n/a)</td><td>321.40 (n/a)</td><td>92.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 <b>(-26.81%)</b></td><td>0.07 <b>(-23.68%)</b></td><td>0.07 <b>(-22.99%)</b></td><td>0.05 (-3.12%)</td><td>0.02 <b>(-46.03%)</b></td><td>614.50 (+3.23%)</td><td>482.34 <b>(+24.85%)</b></td><td>482.00 <b>(+29.85%)</b></td><td>346.20 <b>(+36.62%)</b></td><td>95.26 <b>(-27.03%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>595.30 (n/a)</td><td>386.34 (n/a)</td><td>371.20 (n/a)</td><td>253.40 (n/a)</td><td>130.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (+8.86%)</td><td>0.01 <b>(+24.72%)</b></td><td>0.01 <b>(+21.30%)</b></td><td>0.01 <b>(+67.61%)</b></td><td>0.00 <b>(-36.70%)</b></td><td>382.80 <b>(-40.35%)</b></td><td>296.08 <b>(-26.05%)</b></td><td>284.40 (-17.57%)</td><td>234.50 (-8.15%)</td><td>54.01 <b>(-65.10%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.70 (n/a)</td><td>400.40 (n/a)</td><td>345.00 (n/a)</td><td>255.30 (n/a)</td><td>154.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (-8.07%)</td><td>0.01 (-8.19%)</td><td>0.01 (-10.28%)</td><td>0.01 (-5.38%)</td><td>0.00 (-14.46%)</td><td>509.20 (+5.69%)</td><td>338.78 (+8.09%)</td><td>300.00 (+11.48%)</td><td>279.50 (+8.80%)</td><td>96.09 (+0.39%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>481.80 (n/a)</td><td>313.42 (n/a)</td><td>269.10 (n/a)</td><td>256.90 (n/a)</td><td>95.71 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 <b>(-35.86%)</b></td><td>0.01 (-12.76%)</td><td>0.01 (+3.33%)</td><td>0.01 (-8.14%)</td><td>0.00 <b>(-42.90%)</b></td><td>666.00 (+8.86%)</td><td>376.50 (+6.37%)</td><td>296.70 (-3.23%)</td><td>266.50 <b>(+55.94%)</b></td><td>167.84 (-2.87%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>611.80 (n/a)</td><td>353.96 (n/a)</td><td>306.60 (n/a)</td><td>170.90 (n/a)</td><td>172.81 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 <b>(-28.22%)</b></td><td>0.01 <b>(-32.17%)</b></td><td>0.01 <b>(-31.76%)</b></td><td>0.00 <b>(-75.76%)</b></td><td>0.00 (+14.32%)</td><td>2029.20 <b>(+312.61%)</b></td><td>706.38 <b>(+119.78%)</b></td><td>398.00 <b>(+46.54%)</b></td><td>311.70 <b>(+39.28%)</b></td><td>741.50 <b>(+601.17%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.80 (n/a)</td><td>321.40 (n/a)</td><td>271.60 (n/a)</td><td>223.80 (n/a)</td><td>105.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (-7.62%)</td><td>0.01 <b>(-24.37%)</b></td><td>0.01 (-17.40%)</td><td>0.00 <b>(-77.50%)</b></td><td>0.01 <b>(+34.84%)</b></td><td>1837.50 <b>(+344.48%)</b></td><td>640.56 <b>(+102.79%)</b></td><td>362.20 <b>(+21.06%)</b></td><td>243.60 (+8.27%)</td><td>673.00 <b>(+630.23%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>413.40 (n/a)</td><td>315.88 (n/a)</td><td>299.20 (n/a)</td><td>225.00 (n/a)</td><td>92.16 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 <b>(-36.52%)</b></td><td>0.01 <b>(-32.64%)</b></td><td>0.01 (+8.38%)</td><td>0.00 <b>(-71.06%)</b></td><td>0.00 (-16.65%)</td><td>1751.30 <b>(+245.63%)</b></td><td>728.96 <b>(+83.28%)</b></td><td>432.40 (-7.74%)</td><td>418.60 <b>(+57.49%)</b></td><td>577.19 <b>(+376.76%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>506.70 (n/a)</td><td>397.72 (n/a)</td><td>468.70 (n/a)</td><td>265.80 (n/a)</td><td>121.07 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 <b>(-33.16%)</b></td><td>0.01 (-18.45%)</td><td>0.01 <b>(-34.56%)</b></td><td>0.01 <b>(+54.43%)</b></td><td>0.00 <b>(-71.00%)</b></td><td>526.70 <b>(-35.25%)</b></td><td>385.04 (-9.96%)</td><td>370.00 <b>(+52.83%)</b></td><td>298.60 <b>(+49.60%)</b></td><td>84.86 <b>(-70.73%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>813.40 (n/a)</td><td>427.62 (n/a)</td><td>242.10 (n/a)</td><td>199.60 (n/a)</td><td>289.89 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (+5.42%)</td><td>0.01 <b>(+27.74%)</b></td><td>0.01 <b>(+51.69%)</b></td><td>0.01 <b>(+25.93%)</b></td><td>0.00 (-6.16%)</td><td>508.30 <b>(-20.59%)</b></td><td>357.22 <b>(-24.12%)</b></td><td>314.00 <b>(-34.08%)</b></td><td>268.40 (-5.16%)</td><td>103.43 <b>(-31.28%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>640.10 (n/a)</td><td>470.74 (n/a)</td><td>476.30 (n/a)</td><td>283.00 (n/a)</td><td>150.51 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 <b>(-36.94%)</b></td><td>0.01 <b>(-40.20%)</b></td><td>0.01 <b>(-42.81%)</b></td><td>0.01 <b>(-41.86%)</b></td><td>0.00 <b>(-35.26%)</b></td><td>785.30 <b>(+71.99%)</b></td><td>608.34 <b>(+67.81%)</b></td><td>623.80 <b>(+74.83%)</b></td><td>440.90 <b>(+58.60%)</b></td><td>124.67 <b>(+74.10%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>456.60 (n/a)</td><td>362.52 (n/a)</td><td>356.80 (n/a)</td><td>278.00 (n/a)</td><td>71.61 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 <b>(-39.17%)</b></td><td>0.01 <b>(-20.49%)</b></td><td>0.01 (-2.83%)</td><td>0.01 <b>(-26.03%)</b></td><td>0.00 <b>(-41.72%)</b></td><td>651.50 <b>(+35.19%)</b></td><td>416.32 <b>(+22.42%)</b></td><td>322.30 (+2.91%)</td><td>276.40 <b>(+64.43%)</b></td><td>162.78 <b>(+30.68%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>481.90 (n/a)</td><td>340.08 (n/a)</td><td>313.20 (n/a)</td><td>168.10 (n/a)</td><td>124.56 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (+10.97%)</td><td>0.01 <b>(+28.36%)</b></td><td>0.01 <b>(+67.50%)</b></td><td>0.01 (+12.92%)</td><td>0.00 (-5.17%)</td><td>520.00 (-11.44%)</td><td>360.40 <b>(-23.48%)</b></td><td>319.70 <b>(-40.31%)</b></td><td>280.70 (-9.89%)</td><td>96.22 <b>(-23.40%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.20 (n/a)</td><td>470.98 (n/a)</td><td>535.60 (n/a)</td><td>311.50 (n/a)</td><td>125.60 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (-17.24%)</td><td>0.01 (-15.40%)</td><td>0.01 (-11.41%)</td><td>0.01 (+3.65%)</td><td>0.00 <b>(-33.40%)</b></td><td>538.30 (-3.53%)</td><td>465.40 (+12.84%)</td><td>487.60 (+12.87%)</td><td>293.90 <b>(+20.85%)</b></td><td>98.65 <b>(-25.62%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.00 (n/a)</td><td>412.46 (n/a)</td><td>432.00 (n/a)</td><td>243.20 (n/a)</td><td>132.63 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (+14.69%)</td><td>0.03 (+8.06%)</td><td>0.03 (+0.56%)</td><td>0.02 <b>(+22.66%)</b></td><td>0.01 (-2.22%)</td><td>536.70 (-18.47%)</td><td>322.10 (-10.46%)</td><td>276.90 (-0.54%)</td><td>234.40 (-12.83%)</td><td>121.84 <b>(-27.45%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>658.30 (n/a)</td><td>359.74 (n/a)</td><td>278.40 (n/a)</td><td>268.90 (n/a)</td><td>167.93 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 <b>(+33.00%)</b></td><td>0.03 <b>(+31.91%)</b></td><td>0.03 (+6.98%)</td><td>0.03 <b>(+114.12%)</b></td><td>0.01 <b>(-21.80%)</b></td><td>311.20 <b>(-53.30%)</b></td><td>264.80 <b>(-31.21%)</b></td><td>269.60 (-6.52%)</td><td>192.20 <b>(-24.80%)</b></td><td>45.46 <b>(-73.44%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>666.40 (n/a)</td><td>384.96 (n/a)</td><td>288.40 (n/a)</td><td>255.60 (n/a)</td><td>171.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (-13.41%)</td><td>0.02 (+5.02%)</td><td>0.03 <b>(+29.64%)</b></td><td>0.01 (+5.82%)</td><td>0.01 (-17.65%)</td><td>557.80 (-5.51%)</td><td>382.90 (-8.48%)</td><td>327.00 <b>(-22.86%)</b></td><td>257.70 (+15.51%)</td><td>142.89 (-14.32%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.30 (n/a)</td><td>418.36 (n/a)</td><td>423.90 (n/a)</td><td>223.10 (n/a)</td><td>166.77 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (+15.76%)</td><td>0.03 <b>(+27.51%)</b></td><td>0.03 <b>(+37.03%)</b></td><td>0.02 <b>(+84.45%)</b></td><td>0.01 <b>(-25.57%)</b></td><td>351.90 <b>(-45.79%)</b></td><td>288.16 <b>(-27.77%)</b></td><td>296.40 <b>(-27.01%)</b></td><td>208.50 (-13.59%)</td><td>53.32 <b>(-66.12%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>649.10 (n/a)</td><td>398.96 (n/a)</td><td>406.10 (n/a)</td><td>241.30 (n/a)</td><td>157.39 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (+6.61%)</td><td>0.02 (+15.40%)</td><td>0.02 <b>(+24.29%)</b></td><td>0.02 (+15.46%)</td><td>0.01 (+3.27%)</td><td>519.00 (-13.40%)</td><td>360.30 (-14.01%)</td><td>335.80 (-19.53%)</td><td>266.60 (-6.19%)</td><td>101.13 (-15.88%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>599.30 (n/a)</td><td>418.98 (n/a)</td><td>417.30 (n/a)</td><td>284.20 (n/a)</td><td>120.23 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (+2.53%)</td><td>0.03 (+7.44%)</td><td>0.03 (+3.04%)</td><td>0.02 (-15.15%)</td><td>0.01 (+2.59%)</td><td>537.90 (+17.86%)</td><td>324.20 (-5.64%)</td><td>278.40 (-2.96%)</td><td>240.90 (-2.47%)</td><td>121.07 (+19.39%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>456.40 (n/a)</td><td>343.56 (n/a)</td><td>286.90 (n/a)</td><td>247.00 (n/a)</td><td>101.41 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 <b>(+47.75%)</b></td><td>0.03 <b>(+43.55%)</b></td><td>0.02 <b>(+35.55%)</b></td><td>0.01 (-6.71%)</td><td>0.01 <b>(+97.89%)</b></td><td>605.20 (+7.19%)</td><td>374.52 <b>(-23.11%)</b></td><td>392.20 <b>(-26.24%)</b></td><td>196.00 <b>(-32.34%)</b></td><td>162.35 <b>(+44.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.60 (n/a)</td><td>487.06 (n/a)</td><td>531.70 (n/a)</td><td>289.70 (n/a)</td><td>112.50 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (+9.40%)</td><td>0.02 (+9.60%)</td><td>0.03 <b>(+23.16%)</b></td><td>0.00 <b>(-69.38%)</b></td><td>0.01 <b>(+50.98%)</b></td><td>1857.70 <b>(+226.54%)</b></td><td>592.44 <b>(+48.50%)</b></td><td>301.70 (-18.81%)</td><td>232.10 (-8.59%)</td><td>707.98 <b>(+401.59%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.90 (n/a)</td><td>398.94 (n/a)</td><td>371.60 (n/a)</td><td>253.90 (n/a)</td><td>141.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (+5.60%)</td><td>0.02 (+5.09%)</td><td>0.02 (-13.89%)</td><td>0.02 <b>(+114.89%)</b></td><td>0.01 <b>(-21.92%)</b></td><td>497.60 <b>(-53.46%)</b></td><td>401.80 (-18.74%)</td><td>425.10 (+16.15%)</td><td>262.80 (-5.30%)</td><td>103.84 <b>(-68.07%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1069.20 (n/a)</td><td>494.44 (n/a)</td><td>366.00 (n/a)</td><td>277.50 (n/a)</td><td>325.26 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (-2.45%)</td><td>0.03 <b>(+52.24%)</b></td><td>0.03 <b>(+58.42%)</b></td><td>0.02 <b>(+178.89%)</b></td><td>0.00 <b>(-49.90%)</b></td><td>386.40 <b>(-64.15%)</b></td><td>294.50 <b>(-46.47%)</b></td><td>290.30 <b>(-36.88%)</b></td><td>242.00 (+2.50%)</td><td>56.84 <b>(-81.92%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1077.70 (n/a)</td><td>550.18 (n/a)</td><td>459.90 (n/a)</td><td>236.10 (n/a)</td><td>314.37 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (+10.57%)</td><td>0.02 (-5.21%)</td><td>0.02 (-18.26%)</td><td>0.01 (-19.68%)</td><td>0.01 <b>(+33.26%)</b></td><td>579.50 <b>(+24.49%)</b></td><td>411.52 (+12.54%)</td><td>481.40 <b>(+22.34%)</b></td><td>202.90 (-9.58%)</td><td>151.76 <b>(+43.93%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>465.50 (n/a)</td><td>365.68 (n/a)</td><td>393.50 (n/a)</td><td>224.40 (n/a)</td><td>105.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (+0.11%)</td><td>0.02 (-5.55%)</td><td>0.02 (-5.59%)</td><td>0.01 (+11.15%)</td><td>0.01 (-15.02%)</td><td>593.60 (-10.03%)</td><td>393.24 (+1.48%)</td><td>336.90 (+5.91%)</td><td>244.70 (-0.12%)</td><td>141.68 (-19.33%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>659.80 (n/a)</td><td>387.52 (n/a)</td><td>318.10 (n/a)</td><td>245.00 (n/a)</td><td>175.62 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (-4.61%)</td><td>0.05 (-5.26%)</td><td>0.05 (-8.76%)</td><td>0.03 (+9.43%)</td><td>0.02 <b>(-20.02%)</b></td><td>520.10 (-8.61%)</td><td>356.72 (+0.72%)</td><td>299.20 (+9.60%)</td><td>238.80 (+4.83%)</td><td>121.23 <b>(-20.53%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>569.10 (n/a)</td><td>354.16 (n/a)</td><td>273.00 (n/a)</td><td>227.80 (n/a)</td><td>152.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (-14.13%)</td><td>0.04 <b>(-27.55%)</b></td><td>0.03 <b>(-44.59%)</b></td><td>0.03 (-10.34%)</td><td>0.02 (-9.96%)</td><td>647.90 (+11.53%)</td><td>451.46 <b>(+37.75%)</b></td><td>513.50 <b>(+80.49%)</b></td><td>271.30 (+16.44%)</td><td>156.91 (+8.61%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>580.90 (n/a)</td><td>327.74 (n/a)</td><td>284.50 (n/a)</td><td>233.00 (n/a)</td><td>144.47 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (-16.17%)</td><td>0.05 (+1.26%)</td><td>0.05 (+10.98%)</td><td>0.03 <b>(+37.34%)</b></td><td>0.01 <b>(-48.15%)</b></td><td>480.50 <b>(-27.19%)</b></td><td>360.86 (-10.67%)</td><td>335.40 (-9.89%)</td><td>293.70 (+19.29%)</td><td>78.88 <b>(-53.96%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>659.90 (n/a)</td><td>403.98 (n/a)</td><td>372.20 (n/a)</td><td>246.20 (n/a)</td><td>171.32 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (-16.56%)</td><td>0.05 (-9.03%)</td><td>0.05 (-6.23%)</td><td>0.03 (+15.07%)</td><td>0.01 <b>(-32.11%)</b></td><td>487.60 (-13.10%)</td><td>366.78 (+5.54%)</td><td>318.10 (+6.64%)</td><td>303.00 (+19.86%)</td><td>80.86 <b>(-34.27%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>561.10 (n/a)</td><td>347.54 (n/a)</td><td>298.30 (n/a)</td><td>252.80 (n/a)</td><td>123.00 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (+9.41%)</td><td>0.05 (-15.60%)</td><td>0.04 <b>(-41.43%)</b></td><td>0.03 (-11.45%)</td><td>0.02 <b>(+34.49%)</b></td><td>570.40 (+12.93%)</td><td>387.22 <b>(+24.60%)</b></td><td>435.90 <b>(+70.74%)</b></td><td>220.10 (-8.60%)</td><td>143.77 <b>(+29.85%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>505.10 (n/a)</td><td>310.78 (n/a)</td><td>255.30 (n/a)</td><td>240.80 (n/a)</td><td>110.72 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (-17.54%)</td><td>0.04 <b>(-25.05%)</b></td><td>0.05 (-10.52%)</td><td>0.02 <b>(-53.42%)</b></td><td>0.02 <b>(+25.58%)</b></td><td>1046.50 <b>(+114.71%)</b></td><td>486.90 <b>(+59.67%)</b></td><td>302.80 (+11.78%)</td><td>271.80 <b>(+21.23%)</b></td><td>327.57 <b>(+210.67%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>487.40 (n/a)</td><td>304.94 (n/a)</td><td>270.90 (n/a)</td><td>224.20 (n/a)</td><td>105.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (+17.97%)</td><td>0.05 <b>(-21.11%)</b></td><td>0.05 (-14.70%)</td><td>0.01 <b>(-85.78%)</b></td><td>0.03 <b>(+550.78%)</b></td><td>1864.20 <b>(+603.21%)</b></td><td>603.46 <b>(+139.73%)</b></td><td>306.20 (+17.23%)</td><td>190.90 (-15.23%)</td><td>710.42 <b>(+4161.28%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>265.10 (n/a)</td><td>251.72 (n/a)</td><td>261.20 (n/a)</td><td>225.20 (n/a)</td><td>16.67 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (-15.62%)</td><td>0.03 <b>(-50.55%)</b></td><td>0.03 <b>(-62.27%)</b></td><td>0.01 <b>(-73.89%)</b></td><td>0.02 <b>(+215.73%)</b></td><td>1098.30 <b>(+282.95%)</b></td><td>650.34 <b>(+158.32%)</b></td><td>641.00 <b>(+164.99%)</b></td><td>272.70 (+18.51%)</td><td>336.36 <b>(+1316.20%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>286.80 (n/a)</td><td>251.76 (n/a)</td><td>241.90 (n/a)</td><td>230.10 (n/a)</td><td>23.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (-10.19%)</td><td>0.05 (+3.70%)</td><td>0.06 (-9.90%)</td><td>0.04 <b>(+35.09%)</b></td><td>0.01 <b>(-47.92%)</b></td><td>450.50 <b>(-25.98%)</b></td><td>319.12 (-16.26%)</td><td>277.10 (+10.97%)</td><td>256.60 (+11.32%)</td><td>80.63 <b>(-57.60%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>608.60 (n/a)</td><td>381.10 (n/a)</td><td>249.70 (n/a)</td><td>230.50 (n/a)</td><td>190.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (-2.13%)</td><td>0.04 <b>(-29.48%)</b></td><td>0.05 <b>(-25.89%)</b></td><td>0.01 <b>(-83.68%)</b></td><td>0.02 <b>(+267.50%)</b></td><td>1889.20 <b>(+512.98%)</b></td><td>650.52 <b>(+138.71%)</b></td><td>350.90 <b>(+34.96%)</b></td><td>250.70 (+2.16%)</td><td>698.45 <b>(+2350.45%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>308.20 (n/a)</td><td>272.52 (n/a)</td><td>260.00 (n/a)</td><td>245.40 (n/a)</td><td>28.50 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 <b>(-46.11%)</b></td><td>0.03 <b>(-32.89%)</b></td><td>0.03 <b>(-42.33%)</b></td><td>0.03 <b>(+77.72%)</b></td><td>0.00 <b>(-81.21%)</b></td><td>562.10 <b>(-43.73%)</b></td><td>486.92 (+12.16%)</td><td>500.10 <b>(+73.40%)</b></td><td>405.30 <b>(+85.58%)</b></td><td>60.72 <b>(-81.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>998.90 (n/a)</td><td>434.12 (n/a)</td><td>288.40 (n/a)</td><td>218.40 (n/a)</td><td>324.96 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 <b>(-25.02%)</b></td><td>0.03 (-15.98%)</td><td>0.03 (-8.70%)</td><td>0.02 (-18.11%)</td><td>0.01 <b>(-27.60%)</b></td><td>751.10 <b>(+22.11%)</b></td><td>530.72 (+17.63%)</td><td>512.80 (+9.53%)</td><td>359.50 <b>(+33.40%)</b></td><td>162.06 (+17.58%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>615.10 (n/a)</td><td>451.18 (n/a)</td><td>468.20 (n/a)</td><td>269.50 (n/a)</td><td>137.83 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.15 (-1.88%)</td><td>0.09 <b>(-24.82%)</b></td><td>0.06 <b>(-52.04%)</b></td><td>0.06 <b>(+25.60%)</b></td><td>0.04 (-1.83%)</td><td>515.20 <b>(-20.38%)</b></td><td>407.74 <b>(+28.33%)</b></td><td>508.50 <b>(+108.49%)</b></td><td>216.80 (+1.93%)</td><td>145.37 <b>(-21.26%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>647.10 (n/a)</td><td>317.74 (n/a)</td><td>243.90 (n/a)</td><td>212.70 (n/a)</td><td>184.62 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 <b>(-22.58%)</b></td><td>0.09 (-19.57%)</td><td>0.08 <b>(-26.86%)</b></td><td>0.06 (-17.47%)</td><td>0.03 (-19.16%)</td><td>577.80 <b>(+21.18%)</b></td><td>388.14 <b>(+24.29%)</b></td><td>394.60 <b>(+36.73%)</b></td><td>267.00 <b>(+29.17%)</b></td><td>121.52 <b>(+21.41%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>476.80 (n/a)</td><td>312.28 (n/a)</td><td>288.60 (n/a)</td><td>206.70 (n/a)</td><td>100.09 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (-7.57%)</td><td>0.09 (+3.38%)</td><td>0.07 (-3.38%)</td><td>0.07 <b>(+73.84%)</b></td><td>0.03 <b>(-28.29%)</b></td><td>461.70 <b>(-42.47%)</b></td><td>396.82 (-12.91%)</td><td>440.00 (+3.51%)</td><td>238.90 (+8.20%)</td><td>92.03 <b>(-56.62%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>802.60 (n/a)</td><td>455.64 (n/a)</td><td>425.10 (n/a)</td><td>220.80 (n/a)</td><td>212.14 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (-2.07%)</td><td>0.09 (+16.23%)</td><td>0.10 <b>(+28.47%)</b></td><td>0.06 <b>(+222.77%)</b></td><td>0.03 <b>(-30.85%)</b></td><td>566.20 <b>(-69.02%)</b></td><td>382.32 <b>(-42.18%)</b></td><td>333.50 <b>(-22.17%)</b></td><td>248.60 (+2.14%)</td><td>137.44 <b>(-79.22%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1827.40 (n/a)</td><td>661.28 (n/a)</td><td>428.50 (n/a)</td><td>243.40 (n/a)</td><td>661.52 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.15 (+10.41%)</td><td>0.10 (-4.44%)</td><td>0.11 (+5.02%)</td><td>0.06 <b>(-25.49%)</b></td><td>0.04 <b>(+62.19%)</b></td><td>574.40 <b>(+34.24%)</b></td><td>387.72 (+15.48%)</td><td>300.40 (-4.79%)</td><td>216.50 (-9.41%)</td><td>163.80 <b>(+109.30%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>427.90 (n/a)</td><td>335.74 (n/a)</td><td>315.50 (n/a)</td><td>239.00 (n/a)</td><td>78.26 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (+1.49%)</td><td>0.09 (-16.28%)</td><td>0.07 <b>(-36.56%)</b></td><td>0.06 (-13.99%)</td><td>0.03 <b>(+22.36%)</b></td><td>571.10 (+16.27%)</td><td>406.46 <b>(+23.79%)</b></td><td>446.20 <b>(+57.61%)</b></td><td>246.40 (-1.44%)</td><td>131.94 <b>(+34.45%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>491.20 (n/a)</td><td>328.34 (n/a)</td><td>283.10 (n/a)</td><td>250.00 (n/a)</td><td>98.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.18 (+12.92%)</td><td>0.10 (+11.85%)</td><td>0.09 <b>(+46.27%)</b></td><td>0.05 <b>(+108.67%)</b></td><td>0.05 (-5.07%)</td><td>621.00 <b>(-52.08%)</b></td><td>403.88 <b>(-27.13%)</b></td><td>345.10 <b>(-31.62%)</b></td><td>178.30 (-11.43%)</td><td>193.74 <b>(-55.93%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.06 (n/a)</td><td>1295.90 (n/a)</td><td>554.26 (n/a)</td><td>504.70 (n/a)</td><td>201.30 (n/a)</td><td>439.63 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (-10.78%)</td><td>0.09 (-6.31%)</td><td>0.09 (+18.39%)</td><td>0.05 (-10.58%)</td><td>0.03 (-15.03%)</td><td>619.10 (+11.83%)</td><td>420.20 (+6.23%)</td><td>361.60 (-15.53%)</td><td>279.30 (+12.12%)</td><td>150.62 (+12.11%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>553.60 (n/a)</td><td>395.54 (n/a)</td><td>428.10 (n/a)</td><td>249.10 (n/a)</td><td>134.35 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 <b>(-21.15%)</b></td><td>0.09 (-18.51%)</td><td>0.07 <b>(-42.84%)</b></td><td>0.06 <b>(+254.55%)</b></td><td>0.03 <b>(-42.20%)</b></td><td>578.00 <b>(-71.80%)</b></td><td>405.96 <b>(-33.55%)</b></td><td>453.20 <b>(+74.91%)</b></td><td>255.20 <b>(+26.84%)</b></td><td>137.27 <b>(-82.94%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2049.40 (n/a)</td><td>610.88 (n/a)</td><td>259.10 (n/a)</td><td>201.20 (n/a)</td><td>804.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (+19.50%)</td><td>0.08 (-7.68%)</td><td>0.06 <b>(-30.48%)</b></td><td>0.02 <b>(-60.09%)</b></td><td>0.04 <b>(+134.55%)</b></td><td>1319.40 <b>(+150.55%)</b></td><td>582.26 <b>(+46.63%)</b></td><td>525.30 <b>(+43.88%)</b></td><td>252.20 (-16.32%)</td><td>433.37 <b>(+373.24%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>526.60 (n/a)</td><td>397.10 (n/a)</td><td>365.10 (n/a)</td><td>301.40 (n/a)</td><td>91.57 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (+7.84%)</td><td>0.08 (-18.87%)</td><td>0.06 <b>(-22.23%)</b></td><td>0.05 <b>(-20.45%)</b></td><td>0.04 (+14.26%)</td><td>605.30 <b>(+25.71%)</b></td><td>485.32 <b>(+28.16%)</b></td><td>560.70 <b>(+28.60%)</b></td><td>237.70 (-7.26%)</td><td>151.23 <b>(+34.51%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>481.50 (n/a)</td><td>378.68 (n/a)</td><td>436.00 (n/a)</td><td>256.30 (n/a)</td><td>112.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 <b>(+31.56%)</b></td><td>0.07 (-6.32%)</td><td>0.06 (-14.36%)</td><td>0.02 <b>(-67.69%)</b></td><td>0.05 <b>(+139.69%)</b></td><td>1931.60 <b>(+209.55%)</b></td><td>746.70 <b>(+66.04%)</b></td><td>508.50 (+16.79%)</td><td>246.30 <b>(-23.98%)</b></td><td>686.55 <b>(+486.65%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>624.00 (n/a)</td><td>449.72 (n/a)</td><td>435.40 (n/a)</td><td>324.00 (n/a)</td><td>117.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (+0.23%)</td><td>0.09 <b>(+23.75%)</b></td><td>0.09 <b>(+42.66%)</b></td><td>0.08 <b>(+36.14%)</b></td><td>0.01 <b>(-50.23%)</b></td><td>324.90 <b>(-26.54%)</b></td><td>283.82 <b>(-22.48%)</b></td><td>277.40 <b>(-29.91%)</b></td><td>247.30 (-0.24%)</td><td>30.78 <b>(-64.14%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>442.30 (n/a)</td><td>366.12 (n/a)</td><td>395.80 (n/a)</td><td>247.90 (n/a)</td><td>85.84 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.21 (+4.96%)</td><td>0.15 (-5.48%)</td><td>0.18 (+0.08%)</td><td>0.06 <b>(-30.92%)</b></td><td>0.06 <b>(+39.11%)</b></td><td>766.00 <b>(+44.77%)</b></td><td>405.30 (+19.85%)</td><td>267.60 (-0.07%)</td><td>239.20 (-4.74%)</td><td>230.19 <b>(+89.58%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>529.10 (n/a)</td><td>338.18 (n/a)</td><td>267.80 (n/a)</td><td>251.10 (n/a)</td><td>121.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>4.18 (+5.17%)</td><td>3.49 (+5.97%)</td><td>3.47 (+5.22%)</td><td>3.01 (+12.12%)</td><td>0.45 <b>(-25.25%)</b></td><td>3487.20 (-10.81%)</td><td>3041.52 (-6.98%)</td><td>3017.90 (-4.96%)</td><td>2508.60 (-4.91%)</td><td>371.92 <b>(-38.00%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.97 (n/a)</td><td>3.29 (n/a)</td><td>3.30 (n/a)</td><td>2.68 (n/a)</td><td>0.60 (n/a)</td><td>3909.90 (n/a)</td><td>3269.80 (n/a)</td><td>3175.40 (n/a)</td><td>2638.20 (n/a)</td><td>599.92 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.16 (-17.65%)</td><td>0.13 (-4.37%)</td><td>0.13 (-15.15%)</td><td>0.10 <b>(+26.24%)</b></td><td>0.03 <b>(-50.91%)</b></td><td>429.10 <b>(-20.79%)</b></td><td>330.90 (-7.61%)</td><td>324.00 (+17.86%)</td><td>250.80 <b>(+21.39%)</b></td><td>71.45 <b>(-56.23%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>541.70 (n/a)</td><td>358.16 (n/a)</td><td>274.90 (n/a)</td><td>206.60 (n/a)</td><td>163.25 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (-16.51%)</td><td>0.01 <b>(-23.31%)</b></td><td>0.01 <b>(-24.99%)</b></td><td>0.01 <b>(-33.47%)</b></td><td>0.00 (+13.55%)</td><td>610.40 <b>(+50.31%)</b></td><td>404.24 <b>(+35.70%)</b></td><td>389.90 <b>(+33.30%)</b></td><td>291.20 (+19.79%)</td><td>130.21 <b>(+98.38%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>406.10 (n/a)</td><td>297.90 (n/a)</td><td>292.50 (n/a)</td><td>243.10 (n/a)</td><td>65.64 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (-1.63%)</td><td>0.01 (-16.84%)</td><td>0.01 <b>(-30.64%)</b></td><td>0.00 <b>(-75.13%)</b></td><td>0.01 <b>(+25.62%)</b></td><td>2075.60 <b>(+302.09%)</b></td><td>662.20 <b>(+97.64%)</b></td><td>350.00 <b>(+44.21%)</b></td><td>236.70 (+1.63%)</td><td>792.36 <b>(+490.06%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>516.20 (n/a)</td><td>335.06 (n/a)</td><td>242.70 (n/a)</td><td>232.90 (n/a)</td><td>134.28 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (-0.78%)</td><td>0.02 <b>(+26.41%)</b></td><td>0.02 <b>(+51.16%)</b></td><td>0.01 (+14.12%)</td><td>0.00 (-16.62%)</td><td>492.70 (-12.38%)</td><td>345.60 <b>(-22.49%)</b></td><td>313.60 <b>(-33.85%)</b></td><td>268.30 (+0.79%)</td><td>88.46 (-18.92%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>562.30 (n/a)</td><td>445.88 (n/a)</td><td>474.10 (n/a)</td><td>266.20 (n/a)</td><td>109.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 <b>(+35.39%)</b></td><td>0.02 (+12.77%)</td><td>0.02 <b>(+20.62%)</b></td><td>0.01 <b>(-44.42%)</b></td><td>0.01 <b>(+334.51%)</b></td><td>527.80 <b>(+79.89%)</b></td><td>273.16 (+2.16%)</td><td>216.60 (-17.11%)</td><td>175.20 <b>(-26.14%)</b></td><td>144.04 <b>(+527.22%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>293.40 (n/a)</td><td>267.38 (n/a)</td><td>261.30 (n/a)</td><td>237.20 (n/a)</td><td>22.96 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 <b>(+77.65%)</b></td><td>0.01 <b>(+25.12%)</b></td><td>0.01 (+10.73%)</td><td>0.00 <b>(-47.45%)</b></td><td>0.01 <b>(+523.91%)</b></td><td>1030.10 <b>(+90.30%)</b></td><td>510.14 (+3.36%)</td><td>455.10 (-9.70%)</td><td>234.90 <b>(-43.71%)</b></td><td>316.91 <b>(+573.06%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>541.30 (n/a)</td><td>493.54 (n/a)</td><td>504.00 (n/a)</td><td>417.30 (n/a)</td><td>47.08 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (-2.84%)</td><td>0.01 (+7.43%)</td><td>0.01 (+7.08%)</td><td>0.01 (-14.68%)</td><td>0.00 (+19.89%)</td><td>637.10 (+17.20%)</td><td>405.72 (-1.91%)</td><td>370.00 (-6.59%)</td><td>249.20 (+2.89%)</td><td>166.59 <b>(+41.31%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>543.60 (n/a)</td><td>413.64 (n/a)</td><td>396.10 (n/a)</td><td>242.20 (n/a)</td><td>117.89 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 <b>(-21.82%)</b></td><td>0.02 (-0.22%)</td><td>0.02 <b>(+42.22%)</b></td><td>0.01 (-12.60%)</td><td>0.00 <b>(-38.32%)</b></td><td>557.80 (+14.42%)</td><td>358.80 (-4.32%)</td><td>306.10 <b>(-29.68%)</b></td><td>274.50 <b>(+27.91%)</b></td><td>115.02 (-8.22%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>487.50 (n/a)</td><td>375.00 (n/a)</td><td>435.30 (n/a)</td><td>214.60 (n/a)</td><td>125.32 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (+10.95%)</td><td>0.01 (-11.53%)</td><td>0.01 <b>(-25.61%)</b></td><td>0.01 <b>(-20.17%)</b></td><td>0.00 <b>(+55.85%)</b></td><td>622.40 <b>(+25.28%)</b></td><td>413.08 <b>(+22.73%)</b></td><td>395.40 <b>(+34.40%)</b></td><td>234.80 (-9.87%)</td><td>165.25 <b>(+72.24%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>496.80 (n/a)</td><td>336.58 (n/a)</td><td>294.20 (n/a)</td><td>260.50 (n/a)</td><td>95.94 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (-18.66%)</td><td>0.01 (-12.19%)</td><td>0.01 (+4.33%)</td><td>0.01 (+14.82%)</td><td>0.00 <b>(-43.28%)</b></td><td>549.40 (-12.90%)</td><td>460.84 (+4.48%)</td><td>493.60 (-4.16%)</td><td>296.50 <b>(+22.93%)</b></td><td>98.44 <b>(-40.34%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.80 (n/a)</td><td>441.10 (n/a)</td><td>515.00 (n/a)</td><td>241.20 (n/a)</td><td>165.00 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 <b>(+33.31%)</b></td><td>0.01 <b>(+28.02%)</b></td><td>0.01 (+1.51%)</td><td>0.01 <b>(+251.57%)</b></td><td>0.00 (+3.16%)</td><td>541.10 <b>(-71.56%)</b></td><td>387.22 <b>(-43.91%)</b></td><td>438.40 (-1.51%)</td><td>218.50 <b>(-24.99%)</b></td><td>136.87 <b>(-79.95%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1902.40 (n/a)</td><td>690.36 (n/a)</td><td>445.10 (n/a)</td><td>291.30 (n/a)</td><td>682.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 <b>(-44.14%)</b></td><td>0.01 <b>(-33.50%)</b></td><td>0.01 (-13.49%)</td><td>0.00 <b>(-66.61%)</b></td><td>0.00 <b>(-34.80%)</b></td><td>1844.60 <b>(+199.50%)</b></td><td>858.66 <b>(+79.72%)</b></td><td>570.90 (+15.61%)</td><td>362.10 <b>(+79.08%)</b></td><td>615.56 <b>(+265.64%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>615.90 (n/a)</td><td>477.78 (n/a)</td><td>493.80 (n/a)</td><td>202.20 (n/a)</td><td>168.35 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (-5.02%)</td><td>0.01 (-1.76%)</td><td>0.01 (+4.15%)</td><td>0.01 (-2.36%)</td><td>0.00 (-7.98%)</td><td>581.80 (+2.43%)</td><td>448.78 (+1.14%)</td><td>453.20 (-3.98%)</td><td>248.00 (+5.31%)</td><td>126.25 (+1.56%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>568.00 (n/a)</td><td>443.70 (n/a)</td><td>472.00 (n/a)</td><td>235.50 (n/a)</td><td>124.31 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (-7.23%)</td><td>0.02 (-18.86%)</td><td>0.03 (-19.87%)</td><td>0.01 <b>(-21.82%)</b></td><td>0.01 (+11.51%)</td><td>608.90 <b>(+27.92%)</b></td><td>390.48 <b>(+29.74%)</b></td><td>310.20 <b>(+24.78%)</b></td><td>233.30 (+7.81%)</td><td>160.69 <b>(+53.87%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>476.00 (n/a)</td><td>300.96 (n/a)</td><td>248.60 (n/a)</td><td>216.40 (n/a)</td><td>104.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (-6.40%)</td><td>0.03 (-18.23%)</td><td>0.03 (+1.05%)</td><td>0.01 <b>(-71.79%)</b></td><td>0.02 <b>(+32.68%)</b></td><td>2043.30 <b>(+254.49%)</b></td><td>745.62 <b>(+84.66%)</b></td><td>406.20 (-1.05%)</td><td>279.10 (+6.85%)</td><td>742.60 <b>(+440.56%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>576.40 (n/a)</td><td>403.78 (n/a)</td><td>410.50 (n/a)</td><td>261.20 (n/a)</td><td>137.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 <b>(+40.01%)</b></td><td>0.03 (+3.51%)</td><td>0.02 <b>(-25.22%)</b></td><td>0.01 (-5.48%)</td><td>0.01 <b>(+76.39%)</b></td><td>614.90 (+5.80%)</td><td>407.76 (+9.68%)</td><td>412.90 <b>(+33.75%)</b></td><td>177.00 <b>(-28.60%)</b></td><td>195.54 <b>(+38.92%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.20 (n/a)</td><td>371.76 (n/a)</td><td>308.70 (n/a)</td><td>247.90 (n/a)</td><td>140.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 <b>(+81.08%)</b></td><td>0.03 (+17.34%)</td><td>0.02 (+1.72%)</td><td>0.02 (-2.72%)</td><td>0.01 <b>(+253.26%)</b></td><td>595.70 (+2.80%)</td><td>446.96 (-5.42%)</td><td>482.20 (-1.71%)</td><td>216.20 <b>(-44.79%)</b></td><td>142.87 <b>(+89.42%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>579.50 (n/a)</td><td>472.56 (n/a)</td><td>490.60 (n/a)</td><td>391.60 (n/a)</td><td>75.42 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (-11.58%)</td><td>0.02 (-0.29%)</td><td>0.02 (+6.84%)</td><td>0.01 (+18.02%)</td><td>0.01 <b>(-33.86%)</b></td><td>555.40 (-15.27%)</td><td>432.50 (-6.64%)</td><td>444.00 (-6.41%)</td><td>278.40 (+13.12%)</td><td>100.00 <b>(-39.70%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>655.50 (n/a)</td><td>463.28 (n/a)</td><td>474.40 (n/a)</td><td>246.10 (n/a)</td><td>165.84 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (-3.25%)</td><td>0.03 (-2.05%)</td><td>0.02 (+4.25%)</td><td>0.02 <b>(-20.11%)</b></td><td>0.01 (+1.24%)</td><td>626.80 <b>(+25.18%)</b></td><td>451.70 (+4.25%)</td><td>456.00 (-4.08%)</td><td>243.10 (+3.36%)</td><td>145.47 <b>(+29.53%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.70 (n/a)</td><td>433.28 (n/a)</td><td>475.40 (n/a)</td><td>235.20 (n/a)</td><td>112.30 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (-1.04%)</td><td>0.02 (-2.42%)</td><td>0.03 <b>(+37.70%)</b></td><td>0.01 <b>(-24.24%)</b></td><td>0.01 <b>(+24.73%)</b></td><td>654.40 <b>(+31.99%)</b></td><td>426.66 (+9.90%)</td><td>314.10 <b>(-27.38%)</b></td><td>268.50 (+1.05%)</td><td>180.97 <b>(+74.47%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.80 (n/a)</td><td>388.22 (n/a)</td><td>432.50 (n/a)</td><td>265.70 (n/a)</td><td>103.73 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 <b>(+39.33%)</b></td><td>0.03 <b>(+56.65%)</b></td><td>0.03 <b>(+91.42%)</b></td><td>0.02 <b>(+24.37%)</b></td><td>0.01 <b>(+36.37%)</b></td><td>482.70 (-19.60%)</td><td>328.22 <b>(-35.73%)</b></td><td>288.80 <b>(-47.76%)</b></td><td>205.20 <b>(-28.23%)</b></td><td>106.16 (-17.11%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.40 (n/a)</td><td>510.70 (n/a)</td><td>552.80 (n/a)</td><td>285.90 (n/a)</td><td>128.07 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 <b>(+42.46%)</b></td><td>0.03 (+17.22%)</td><td>0.03 (+15.05%)</td><td>0.01 (+1.57%)</td><td>0.01 <b>(+67.48%)</b></td><td>601.40 (-1.54%)</td><td>365.86 (-4.66%)</td><td>255.00 (-13.09%)</td><td>177.00 <b>(-29.79%)</b></td><td>195.71 <b>(+26.04%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>610.80 (n/a)</td><td>383.76 (n/a)</td><td>293.40 (n/a)</td><td>252.10 (n/a)</td><td>155.28 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 <b>(+85.47%)</b></td><td>0.03 <b>(+63.85%)</b></td><td>0.03 <b>(+94.94%)</b></td><td>0.02 (+11.03%)</td><td>0.01 <b>(+150.49%)</b></td><td>525.30 (-9.94%)</td><td>328.08 <b>(-33.05%)</b></td><td>282.80 <b>(-48.70%)</b></td><td>175.10 <b>(-46.09%)</b></td><td>138.85 <b>(+20.89%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>583.30 (n/a)</td><td>490.04 (n/a)</td><td>551.30 (n/a)</td><td>324.80 (n/a)</td><td>114.86 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 <b>(+23.98%)</b></td><td>0.02 (+0.62%)</td><td>0.02 (-3.61%)</td><td>0.01 (-10.66%)</td><td>0.01 <b>(+49.96%)</b></td><td>643.50 (+11.93%)</td><td>481.84 (+4.23%)</td><td>522.90 (+3.75%)</td><td>247.00 (-19.36%)</td><td>148.12 <b>(+24.58%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.90 (n/a)</td><td>462.28 (n/a)</td><td>504.00 (n/a)</td><td>306.30 (n/a)</td><td>118.89 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 <b>(-20.49%)</b></td><td>0.05 (-13.80%)</td><td>0.05 (-3.92%)</td><td>0.03 (-15.46%)</td><td>0.02 (-16.21%)</td><td>554.40 (+18.28%)</td><td>389.14 (+16.20%)</td><td>302.40 (+4.06%)</td><td>276.60 <b>(+25.78%)</b></td><td>142.19 <b>(+20.23%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>468.70 (n/a)</td><td>334.90 (n/a)</td><td>290.60 (n/a)</td><td>219.90 (n/a)</td><td>118.27 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (+13.32%)</td><td>0.07 (+18.16%)</td><td>0.08 <b>(+79.00%)</b></td><td>0.01 <b>(-72.54%)</b></td><td>0.04 <b>(+68.58%)</b></td><td>1981.90 <b>(+264.19%)</b></td><td>646.84 <b>(+42.08%)</b></td><td>293.10 <b>(-44.14%)</b></td><td>222.60 (-11.74%)</td><td>750.97 <b>(+511.27%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>544.20 (n/a)</td><td>455.26 (n/a)</td><td>524.70 (n/a)</td><td>252.20 (n/a)</td><td>122.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (+3.11%)</td><td>0.04 (-11.33%)</td><td>0.03 (-18.40%)</td><td>0.03 (+14.01%)</td><td>0.02 (-4.10%)</td><td>602.40 (-12.29%)</td><td>476.64 (+9.06%)</td><td>503.50 <b>(+22.57%)</b></td><td>238.40 (-3.01%)</td><td>140.36 <b>(-23.11%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>686.80 (n/a)</td><td>437.04 (n/a)</td><td>410.80 (n/a)</td><td>245.80 (n/a)</td><td>182.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 <b>(-27.90%)</b></td><td>0.05 (-5.04%)</td><td>0.05 (+19.84%)</td><td>0.03 (-6.15%)</td><td>0.02 <b>(-30.46%)</b></td><td>695.30 (+6.56%)</td><td>465.74 (+2.21%)</td><td>397.30 (-16.55%)</td><td>299.20 <b>(+38.71%)</b></td><td>179.60 (+8.45%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>652.50 (n/a)</td><td>455.66 (n/a)</td><td>476.10 (n/a)</td><td>215.70 (n/a)</td><td>165.61 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (+0.54%)</td><td>0.05 (-16.10%)</td><td>0.06 (-12.06%)</td><td>0.03 <b>(-32.77%)</b></td><td>0.02 <b>(+51.75%)</b></td><td>571.50 <b>(+48.75%)</b></td><td>360.60 <b>(+28.36%)</b></td><td>278.60 (+13.71%)</td><td>239.70 (-0.54%)</td><td>140.51 <b>(+128.34%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>384.20 (n/a)</td><td>280.92 (n/a)</td><td>245.00 (n/a)</td><td>241.00 (n/a)</td><td>61.54 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 <b>(+34.09%)</b></td><td>0.04 (+7.60%)</td><td>0.04 (+6.37%)</td><td>0.03 (-14.37%)</td><td>0.01 <b>(+174.17%)</b></td><td>655.70 (+16.78%)</td><td>485.18 (-2.86%)</td><td>464.80 (-5.99%)</td><td>321.40 <b>(-25.43%)</b></td><td>120.46 <b>(+132.82%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>561.50 (n/a)</td><td>499.48 (n/a)</td><td>494.40 (n/a)</td><td>431.00 (n/a)</td><td>51.74 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (-8.37%)</td><td>0.04 (-2.98%)</td><td>0.03 (-11.32%)</td><td>0.03 (-11.83%)</td><td>0.02 (+0.74%)</td><td>637.70 (+13.41%)</td><td>447.86 (+5.21%)</td><td>475.00 (+12.75%)</td><td>267.10 (+9.15%)</td><td>155.31 <b>(+22.83%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>562.30 (n/a)</td><td>425.68 (n/a)</td><td>421.30 (n/a)</td><td>244.70 (n/a)</td><td>126.44 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (-13.51%)</td><td>0.05 (+2.27%)</td><td>0.05 (+6.04%)</td><td>0.04 (+11.27%)</td><td>0.01 <b>(-25.66%)</b></td><td>487.30 (-10.13%)</td><td>393.74 (-3.94%)</td><td>384.60 (-5.71%)</td><td>324.30 (+15.61%)</td><td>71.89 <b>(-22.37%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>542.20 (n/a)</td><td>409.90 (n/a)</td><td>407.90 (n/a)</td><td>280.50 (n/a)</td><td>92.61 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (-11.03%)</td><td>0.03 <b>(-34.13%)</b></td><td>0.02 <b>(-36.62%)</b></td><td>0.01 <b>(-74.32%)</b></td><td>0.02 <b>(+74.16%)</b></td><td>2435.40 <b>(+289.35%)</b></td><td>1002.88 <b>(+124.40%)</b></td><td>696.10 <b>(+57.77%)</b></td><td>379.70 (+12.40%)</td><td>845.76 <b>(+651.42%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>625.50 (n/a)</td><td>446.92 (n/a)</td><td>441.20 (n/a)</td><td>337.80 (n/a)</td><td>112.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (-0.39%)</td><td>0.04 (-14.82%)</td><td>0.04 (-5.94%)</td><td>0.02 <b>(-51.65%)</b></td><td>0.01 <b>(+205.99%)</b></td><td>986.20 <b>(+106.79%)</b></td><td>577.82 <b>(+29.01%)</b></td><td>480.20 (+6.31%)</td><td>391.70 (+0.41%)</td><td>235.92 <b>(+585.22%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>476.90 (n/a)</td><td>447.88 (n/a)</td><td>451.70 (n/a)</td><td>390.10 (n/a)</td><td>34.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 <b>(-23.49%)</b></td><td>0.03 (-12.55%)</td><td>0.03 (-19.20%)</td><td>0.03 (+0.22%)</td><td>0.01 <b>(-45.77%)</b></td><td>553.20 (-0.22%)</td><td>489.94 (+10.64%)</td><td>536.70 <b>(+23.75%)</b></td><td>393.60 <b>(+30.72%)</b></td><td>75.80 <b>(-31.15%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>554.40 (n/a)</td><td>442.82 (n/a)</td><td>433.70 (n/a)</td><td>301.10 (n/a)</td><td>110.08 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (+2.27%)</td><td>0.08 <b>(-25.40%)</b></td><td>0.07 <b>(-42.13%)</b></td><td>0.06 (-17.32%)</td><td>0.03 <b>(+34.93%)</b></td><td>557.70 <b>(+20.95%)</b></td><td>450.08 <b>(+38.98%)</b></td><td>500.50 <b>(+72.82%)</b></td><td>262.90 (-2.23%)</td><td>117.72 <b>(+49.96%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>461.10 (n/a)</td><td>323.84 (n/a)</td><td>289.60 (n/a)</td><td>268.90 (n/a)</td><td>78.50 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (+3.86%)</td><td>0.09 (-0.25%)</td><td>0.07 (-4.15%)</td><td>0.06 (-13.65%)</td><td>0.04 <b>(+26.57%)</b></td><td>550.30 (+15.80%)</td><td>421.88 (+5.34%)</td><td>477.40 (+4.33%)</td><td>236.50 (-3.71%)</td><td>143.95 <b>(+43.03%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>475.20 (n/a)</td><td>400.48 (n/a)</td><td>457.60 (n/a)</td><td>245.60 (n/a)</td><td>100.64 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 <b>(-32.44%)</b></td><td>0.08 (-8.14%)</td><td>0.08 (+5.75%)</td><td>0.06 (+6.02%)</td><td>0.01 <b>(-57.87%)</b></td><td>680.40 (-5.67%)</td><td>514.12 (+1.23%)</td><td>489.30 (-5.43%)</td><td>421.50 <b>(+48.00%)</b></td><td>101.73 <b>(-38.72%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>721.30 (n/a)</td><td>507.86 (n/a)</td><td>517.40 (n/a)</td><td>284.80 (n/a)</td><td>166.00 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (+17.49%)</td><td>0.08 (-5.12%)</td><td>0.07 (-9.72%)</td><td>0.06 (+14.51%)</td><td>0.03 <b>(+21.31%)</b></td><td>551.60 (-12.68%)</td><td>451.98 (+6.29%)</td><td>464.10 (+10.76%)</td><td>238.60 (-14.88%)</td><td>127.98 (-10.05%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>631.70 (n/a)</td><td>425.22 (n/a)</td><td>419.00 (n/a)</td><td>280.30 (n/a)</td><td>142.27 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (-13.08%)</td><td>0.11 (+7.75%)</td><td>0.13 <b>(+36.60%)</b></td><td>0.07 <b>(+36.11%)</b></td><td>0.03 <b>(-37.49%)</b></td><td>586.30 <b>(-26.53%)</b></td><td>378.14 (-15.71%)</td><td>322.10 <b>(-26.81%)</b></td><td>300.20 (+15.02%)</td><td>118.92 <b>(-44.45%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>798.00 (n/a)</td><td>448.60 (n/a)</td><td>440.10 (n/a)</td><td>261.00 (n/a)</td><td>214.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (+8.66%)</td><td>0.10 (+15.42%)</td><td>0.11 <b>(+37.55%)</b></td><td>0.07 (+7.83%)</td><td>0.03 <b>(+25.19%)</b></td><td>490.90 (-7.27%)</td><td>355.98 (-11.45%)</td><td>290.00 <b>(-27.30%)</b></td><td>249.40 (-7.97%)</td><td>112.80 (+11.72%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>529.40 (n/a)</td><td>402.00 (n/a)</td><td>398.90 (n/a)</td><td>271.00 (n/a)</td><td>100.97 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (-8.42%)</td><td>0.08 (-16.11%)</td><td>0.07 <b>(-28.64%)</b></td><td>0.06 <b>(+65.09%)</b></td><td>0.03 <b>(-24.51%)</b></td><td>588.40 <b>(-39.43%)</b></td><td>482.10 (+3.81%)</td><td>515.60 <b>(+40.15%)</b></td><td>262.90 (+9.18%)</td><td>126.35 <b>(-56.74%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>971.40 (n/a)</td><td>464.42 (n/a)</td><td>367.90 (n/a)</td><td>240.80 (n/a)</td><td>292.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (-16.53%)</td><td>0.08 (+11.35%)</td><td>0.07 (+1.98%)</td><td>0.06 <b>(+284.20%)</b></td><td>0.02 <b>(-49.82%)</b></td><td>522.00 <b>(-73.97%)</b></td><td>432.98 <b>(-42.22%)</b></td><td>464.10 (-1.94%)</td><td>271.60 (+19.81%)</td><td>95.60 <b>(-86.62%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>2005.40 (n/a)</td><td>749.32 (n/a)</td><td>473.30 (n/a)</td><td>226.70 (n/a)</td><td>714.27 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.15 (-1.19%)</td><td>0.11 (+5.55%)</td><td>0.10 <b>(-23.45%)</b></td><td>0.07 <b>(+288.91%)</b></td><td>0.03 <b>(-40.80%)</b></td><td>493.20 <b>(-74.29%)</b></td><td>359.50 <b>(-43.39%)</b></td><td>378.40 <b>(+30.62%)</b></td><td>248.30 (+1.18%)</td><td>104.32 <b>(-85.57%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1918.00 (n/a)</td><td>635.04 (n/a)</td><td>289.70 (n/a)</td><td>245.40 (n/a)</td><td>723.02 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 <b>(+29.37%)</b></td><td>0.08 (+11.17%)</td><td>0.07 (+3.11%)</td><td>0.06 (+16.21%)</td><td>0.03 <b>(+66.14%)</b></td><td>563.40 (-13.95%)</td><td>464.74 (-7.21%)</td><td>485.20 (-3.02%)</td><td>274.40 <b>(-22.68%)</b></td><td>117.07 (+10.26%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>654.70 (n/a)</td><td>500.84 (n/a)</td><td>500.30 (n/a)</td><td>354.90 (n/a)</td><td>106.19 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 <b>(+20.95%)</b></td><td>0.07 <b>(+33.16%)</b></td><td>0.07 <b>(+64.69%)</b></td><td>0.04 <b>(+35.08%)</b></td><td>0.02 (-6.63%)</td><td>514.30 <b>(-25.97%)</b></td><td>326.14 <b>(-27.79%)</b></td><td>287.80 <b>(-39.28%)</b></td><td>244.20 (-17.33%)</td><td>108.01 <b>(-34.79%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>694.70 (n/a)</td><td>451.66 (n/a)</td><td>474.00 (n/a)</td><td>295.40 (n/a)</td><td>165.63 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (+10.58%)</td><td>0.07 <b>(+33.85%)</b></td><td>0.08 <b>(+75.05%)</b></td><td>0.04 <b>(+22.46%)</b></td><td>0.02 (-16.55%)</td><td>475.80 (-18.33%)</td><td>301.02 <b>(-28.86%)</b></td><td>272.00 <b>(-42.88%)</b></td><td>236.00 (-9.54%)</td><td>99.52 <b>(-32.99%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>582.60 (n/a)</td><td>423.12 (n/a)</td><td>476.20 (n/a)</td><td>260.90 (n/a)</td><td>148.51 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (+3.66%)</td><td>0.06 (+3.09%)</td><td>0.07 (-2.56%)</td><td>0.04 (+6.09%)</td><td>0.02 (-5.00%)</td><td>540.40 (-5.74%)</td><td>357.00 (-5.07%)</td><td>280.70 (+2.60%)</td><td>249.10 (-3.52%)</td><td>134.77 (-13.34%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>573.30 (n/a)</td><td>376.06 (n/a)</td><td>273.60 (n/a)</td><td>258.20 (n/a)</td><td>155.51 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (-19.00%)</td><td>0.06 (+5.78%)</td><td>0.05 (+13.48%)</td><td>0.04 <b>(+35.93%)</b></td><td>0.03 <b>(-23.97%)</b></td><td>584.30 <b>(-26.44%)</b></td><td>403.04 (-14.24%)</td><td>414.70 (-11.88%)</td><td>214.90 <b>(+23.43%)</b></td><td>170.78 <b>(-27.53%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>794.30 (n/a)</td><td>469.94 (n/a)</td><td>470.60 (n/a)</td><td>174.10 (n/a)</td><td>235.65 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 <b>(+29.28%)</b></td><td>0.06 <b>(+46.93%)</b></td><td>0.05 <b>(+31.02%)</b></td><td>0.04 <b>(+114.43%)</b></td><td>0.02 <b>(+23.27%)</b></td><td>501.00 <b>(-53.36%)</b></td><td>379.08 <b>(-36.25%)</b></td><td>421.10 <b>(-23.67%)</b></td><td>252.70 <b>(-22.65%)</b></td><td>114.75 <b>(-59.52%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1074.20 (n/a)</td><td>594.68 (n/a)</td><td>551.70 (n/a)</td><td>326.70 (n/a)</td><td>283.45 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 <b>(+75.40%)</b></td><td>0.06 <b>(+46.97%)</b></td><td>0.05 <b>(+39.19%)</b></td><td>0.04 (+14.14%)</td><td>0.02 <b>(+330.61%)</b></td><td>499.30 (-12.39%)</td><td>378.74 <b>(-26.89%)</b></td><td>389.20 <b>(-28.15%)</b></td><td>250.80 <b>(-42.99%)</b></td><td>115.59 <b>(+116.04%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>569.90 (n/a)</td><td>518.04 (n/a)</td><td>541.70 (n/a)</td><td>439.90 (n/a)</td><td>53.51 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 <b>(+21.41%)</b></td><td>0.08 <b>(+34.08%)</b></td><td>0.08 <b>(+50.98%)</b></td><td>0.06 <b>(+26.48%)</b></td><td>0.01 (+4.11%)</td><td>402.60 <b>(-20.93%)</b></td><td>313.50 <b>(-26.28%)</b></td><td>292.70 <b>(-33.78%)</b></td><td>256.80 (-17.61%)</td><td>59.41 <b>(-33.56%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>509.20 (n/a)</td><td>425.26 (n/a)</td><td>442.00 (n/a)</td><td>311.70 (n/a)</td><td>89.41 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 <b>(+28.74%)</b></td><td>0.09 (+18.56%)</td><td>0.10 <b>(+27.27%)</b></td><td>0.05 <b>(+31.09%)</b></td><td>0.03 <b>(+48.25%)</b></td><td>491.60 <b>(-23.71%)</b></td><td>318.30 (-13.49%)</td><td>234.20 <b>(-21.44%)</b></td><td>207.70 <b>(-22.33%)</b></td><td>132.76 (-15.53%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>644.40 (n/a)</td><td>367.92 (n/a)</td><td>298.10 (n/a)</td><td>267.40 (n/a)</td><td>157.17 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (-4.30%)</td><td>0.06 (-15.47%)</td><td>0.05 <b>(-36.58%)</b></td><td>0.01 <b>(-75.89%)</b></td><td>0.04 <b>(+45.63%)</b></td><td>2467.80 <b>(+314.83%)</b></td><td>821.66 <b>(+106.08%)</b></td><td>488.90 <b>(+57.71%)</b></td><td>242.30 (+4.48%)</td><td>936.86 <b>(+469.82%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>594.90 (n/a)</td><td>398.70 (n/a)</td><td>310.00 (n/a)</td><td>231.90 (n/a)</td><td>164.41 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (-12.71%)</td><td>0.08 (+12.92%)</td><td>0.09 <b>(+57.65%)</b></td><td>0.05 <b>(+23.38%)</b></td><td>0.03 <b>(-21.12%)</b></td><td>539.90 (-18.96%)</td><td>352.12 (-17.19%)</td><td>275.80 <b>(-36.57%)</b></td><td>233.50 (+14.57%)</td><td>138.95 <b>(-25.77%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>666.20 (n/a)</td><td>425.22 (n/a)</td><td>434.80 (n/a)</td><td>203.80 (n/a)</td><td>187.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 <b>(+38.31%)</b></td><td>0.09 <b>(+77.48%)</b></td><td>0.09 <b>(+65.72%)</b></td><td>0.06 <b>(+497.09%)</b></td><td>0.02 (-13.95%)</td><td>408.00 <b>(-83.25%)</b></td><td>306.28 <b>(-64.11%)</b></td><td>282.80 <b>(-39.66%)</b></td><td>213.00 <b>(-27.70%)</b></td><td>82.43 <b>(-90.75%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2436.00 (n/a)</td><td>853.46 (n/a)</td><td>468.70 (n/a)</td><td>294.60 (n/a)</td><td>891.50 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 <b>(+33.68%)</b></td><td>0.06 <b>(+25.59%)</b></td><td>0.05 (+17.82%)</td><td>0.05 <b>(+39.67%)</b></td><td>0.01 <b>(+44.83%)</b></td><td>490.10 <b>(-28.40%)</b></td><td>417.62 <b>(-20.01%)</b></td><td>449.50 (-15.14%)</td><td>288.80 <b>(-25.20%)</b></td><td>84.07 <b>(-22.30%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>684.50 (n/a)</td><td>522.08 (n/a)</td><td>529.70 (n/a)</td><td>386.10 (n/a)</td><td>108.21 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (-4.79%)</td><td>0.04 <b>(-37.05%)</b></td><td>0.04 <b>(-48.74%)</b></td><td>0.01 <b>(-77.77%)</b></td><td>0.02 <b>(+35.21%)</b></td><td>2001.50 <b>(+349.88%)</b></td><td>753.78 <b>(+134.72%)</b></td><td>517.00 <b>(+95.09%)</b></td><td>239.00 (+5.05%)</td><td>707.32 <b>(+594.12%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>444.90 (n/a)</td><td>321.14 (n/a)</td><td>265.00 (n/a)</td><td>227.50 (n/a)</td><td>101.90 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (+2.81%)</td><td>0.07 <b>(+41.04%)</b></td><td>0.07 <b>(+63.11%)</b></td><td>0.04 <b>(+162.16%)</b></td><td>0.01 <b>(-41.44%)</b></td><td>413.90 <b>(-61.85%)</b></td><td>288.58 <b>(-42.86%)</b></td><td>254.60 <b>(-38.68%)</b></td><td>240.60 (-2.75%)</td><td>71.44 <b>(-78.75%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1085.00 (n/a)</td><td>505.00 (n/a)</td><td>415.20 (n/a)</td><td>247.40 (n/a)</td><td>336.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (+1.56%)</td><td>0.05 (+12.35%)</td><td>0.04 (+5.76%)</td><td>0.04 (+4.61%)</td><td>0.02 (+0.57%)</td><td>510.20 (-4.40%)</td><td>389.16 (-10.97%)</td><td>449.50 (-5.45%)</td><td>230.20 (-1.54%)</td><td>117.79 (+0.54%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>533.70 (n/a)</td><td>437.10 (n/a)</td><td>475.40 (n/a)</td><td>233.80 (n/a)</td><td>117.15 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 <b>(-21.94%)</b></td><td>0.05 (-6.26%)</td><td>0.04 (+6.02%)</td><td>0.03 (-1.06%)</td><td>0.02 <b>(-29.02%)</b></td><td>653.60 (+1.07%)</td><td>429.52 (-1.26%)</td><td>485.10 (-5.68%)</td><td>217.20 <b>(+28.07%)</b></td><td>177.63 (-9.76%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>646.70 (n/a)</td><td>434.98 (n/a)</td><td>514.30 (n/a)</td><td>169.60 (n/a)</td><td>196.83 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (+4.18%)</td><td>0.05 (-1.77%)</td><td>0.04 (-13.58%)</td><td>0.04 (+12.49%)</td><td>0.02 (+6.41%)</td><td>498.90 (-11.10%)</td><td>422.88 (+1.60%)</td><td>461.20 (+15.70%)</td><td>242.90 (-3.99%)</td><td>102.43 (-11.36%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>561.20 (n/a)</td><td>416.20 (n/a)</td><td>398.60 (n/a)</td><td>253.00 (n/a)</td><td>115.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (-4.85%)</td><td>0.04 (-14.93%)</td><td>0.04 (-18.44%)</td><td>0.03 <b>(-20.25%)</b></td><td>0.01 (+15.53%)</td><td>620.60 <b>(+25.40%)</b></td><td>518.10 (+18.47%)</td><td>518.90 <b>(+22.61%)</b></td><td>405.30 (+5.08%)</td><td>77.73 <b>(+48.27%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>494.90 (n/a)</td><td>437.32 (n/a)</td><td>423.20 (n/a)</td><td>385.70 (n/a)</td><td>52.43 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.40 <b>(+26.56%)</b></td><td>0.29 <b>(+67.94%)</b></td><td>0.26 <b>(+58.51%)</b></td><td>0.18 <b>(+358.81%)</b></td><td>0.09 <b>(-31.43%)</b></td><td>544.90 <b>(-78.20%)</b></td><td>367.26 <b>(-67.11%)</b></td><td>372.30 <b>(-36.92%)</b></td><td>243.90 <b>(-20.99%)</b></td><td>117.42 <b>(-88.20%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.32 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.13 (n/a)</td><td>2500.10 (n/a)</td><td>1116.66 (n/a)</td><td>590.20 (n/a)</td><td>308.70 (n/a)</td><td>994.73 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.46 (+9.87%)</td><td>0.25 (+15.72%)</td><td>0.23 <b>(+29.94%)</b></td><td>0.16 <b>(+32.84%)</b></td><td>0.12 (+3.02%)</td><td>597.70 <b>(-24.71%)</b></td><td>449.98 (-16.65%)</td><td>436.10 <b>(-23.05%)</b></td><td>214.40 (-8.96%)</td><td>151.77 <b>(-26.64%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.42 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>793.90 (n/a)</td><td>539.84 (n/a)</td><td>566.70 (n/a)</td><td>235.50 (n/a)</td><td>206.89 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.33 <b>(+32.47%)</b></td><td>0.23 <b>(+28.30%)</b></td><td>0.18 (-8.60%)</td><td>0.13 <b>(+159.00%)</b></td><td>0.09 (+14.48%)</td><td>756.60 <b>(-61.39%)</b></td><td>490.32 <b>(-37.01%)</b></td><td>539.80 (+9.40%)</td><td>298.70 <b>(-24.51%)</b></td><td>191.98 <b>(-71.18%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>0.08 (n/a)</td><td>1959.60 (n/a)</td><td>778.38 (n/a)</td><td>493.40 (n/a)</td><td>395.70 (n/a)</td><td>666.07 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.29 (+1.71%)</td><td>0.22 <b>(+30.76%)</b></td><td>0.25 <b>(+48.11%)</b></td><td>0.10 <b>(+175.27%)</b></td><td>0.08 (-14.27%)</td><td>708.60 <b>(-63.67%)</b></td><td>399.26 <b>(-45.13%)</b></td><td>298.50 <b>(-32.50%)</b></td><td>256.50 (-1.69%)</td><td>194.25 <b>(-72.25%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.28 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>0.10 (n/a)</td><td>1950.70 (n/a)</td><td>727.64 (n/a)</td><td>442.20 (n/a)</td><td>260.90 (n/a)</td><td>700.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.31 (-12.08%)</td><td>0.16 (+2.18%)</td><td>0.15 (+5.88%)</td><td>0.04 (-0.74%)</td><td>0.13 (+14.87%)</td><td>2003.30 (+0.75%)</td><td>982.80 <b>(+29.64%)</b></td><td>497.40 (-5.55%)</td><td>240.90 (+13.74%)</td><td>899.25 <b>(+28.20%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.35 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.11 (n/a)</td><td>1988.40 (n/a)</td><td>758.12 (n/a)</td><td>526.60 (n/a)</td><td>211.80 (n/a)</td><td>701.47 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.29 <b>(-20.44%)</b></td><td>0.18 (-0.17%)</td><td>0.16 (+4.86%)</td><td>0.14 <b>(+23.87%)</b></td><td>0.06 <b>(-40.26%)</b></td><td>542.80 (-19.27%)</td><td>427.58 (-9.60%)</td><td>455.60 (-4.63%)</td><td>256.10 <b>(+25.72%)</b></td><td>111.08 <b>(-38.00%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.36 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>672.40 (n/a)</td><td>472.98 (n/a)</td><td>477.70 (n/a)</td><td>203.70 (n/a)</td><td>179.18 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (-16.92%)</td><td>0.10 (-8.00%)</td><td>0.11 (-14.70%)</td><td>0.08 <b>(+109.06%)</b></td><td>0.02 <b>(-49.02%)</b></td><td>476.40 <b>(-52.17%)</b></td><td>379.64 (-12.06%)</td><td>340.30 (+17.22%)</td><td>305.20 <b>(+20.35%)</b></td><td>86.50 <b>(-72.69%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>996.00 (n/a)</td><td>431.72 (n/a)</td><td>290.30 (n/a)</td><td>253.60 (n/a)</td><td>316.72 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.18 <b>(+25.94%)</b></td><td>0.10 (+15.70%)</td><td>0.08 (-6.83%)</td><td>0.06 <b>(+194.22%)</b></td><td>0.05 (+9.64%)</td><td>644.10 <b>(-66.01%)</b></td><td>434.56 <b>(-36.04%)</b></td><td>488.80 (+7.33%)</td><td>209.60 <b>(-20.61%)</b></td><td>178.92 <b>(-73.88%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1895.20 (n/a)</td><td>679.42 (n/a)</td><td>455.40 (n/a)</td><td>264.00 (n/a)</td><td>684.96 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.16 (+16.86%)</td><td>0.11 (+10.85%)</td><td>0.11 <b>(+33.80%)</b></td><td>0.06 <b>(-23.45%)</b></td><td>0.04 <b>(+62.75%)</b></td><td>646.90 <b>(+30.63%)</b></td><td>402.88 (-1.19%)</td><td>338.00 <b>(-25.27%)</b></td><td>233.20 (-14.42%)</td><td>173.57 <b>(+83.84%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>495.20 (n/a)</td><td>407.74 (n/a)</td><td>452.30 (n/a)</td><td>272.50 (n/a)</td><td>94.41 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.16 (+7.45%)</td><td>0.10 (+10.52%)</td><td>0.07 (+3.49%)</td><td>0.06 (-0.80%)</td><td>0.05 <b>(+38.22%)</b></td><td>607.00 (+0.80%)</td><td>435.08 (-2.57%)</td><td>498.10 (-3.38%)</td><td>234.50 (-6.94%)</td><td>183.46 <b>(+27.96%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>602.20 (n/a)</td><td>446.54 (n/a)</td><td>515.50 (n/a)</td><td>252.00 (n/a)</td><td>143.36 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (-3.10%)</td><td>0.07 (-18.67%)</td><td>0.06 <b>(-25.40%)</b></td><td>0.05 <b>(-22.99%)</b></td><td>0.02 <b>(+40.84%)</b></td><td>706.90 <b>(+29.85%)</b></td><td>561.04 <b>(+26.63%)</b></td><td>574.40 <b>(+34.05%)</b></td><td>373.10 (+3.21%)</td><td>128.33 <b>(+83.73%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>544.40 (n/a)</td><td>443.04 (n/a)</td><td>428.50 (n/a)</td><td>361.50 (n/a)</td><td>69.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 <b>(+44.62%)</b></td><td>0.08 (+13.44%)</td><td>0.08 (+14.85%)</td><td>0.03 <b>(-28.31%)</b></td><td>0.04 <b>(+116.34%)</b></td><td>1092.80 <b>(+39.48%)</b></td><td>571.98 (+1.94%)</td><td>466.30 (-12.94%)</td><td>284.00 <b>(-30.85%)</b></td><td>310.37 <b>(+116.57%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>783.50 (n/a)</td><td>561.12 (n/a)</td><td>535.60 (n/a)</td><td>410.70 (n/a)</td><td>143.31 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (-18.13%)</td><td>0.10 (-14.41%)</td><td>0.08 <b>(-22.57%)</b></td><td>0.07 (-16.58%)</td><td>0.04 (+3.72%)</td><td>616.90 (+19.88%)</td><td>441.54 <b>(+21.01%)</b></td><td>494.10 <b>(+29.14%)</b></td><td>282.80 <b>(+22.11%)</b></td><td>150.87 <b>(+43.37%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>514.60 (n/a)</td><td>364.88 (n/a)</td><td>382.60 (n/a)</td><td>231.60 (n/a)</td><td>105.23 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.18 (+18.14%)</td><td>0.10 <b>(-20.70%)</b></td><td>0.08 <b>(-43.20%)</b></td><td>0.06 (-5.28%)</td><td>0.05 <b>(+47.71%)</b></td><td>645.10 (+5.58%)</td><td>481.54 <b>(+33.78%)</b></td><td>535.60 <b>(+76.07%)</b></td><td>224.20 (-15.33%)</td><td>169.73 (+19.80%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>611.00 (n/a)</td><td>359.96 (n/a)</td><td>304.20 (n/a)</td><td>264.80 (n/a)</td><td>141.67 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.17 <b>(+60.77%)</b></td><td>0.15 <b>(+67.97%)</b></td><td>0.16 <b>(+91.67%)</b></td><td>0.09 <b>(+30.27%)</b></td><td>0.03 <b>(+101.02%)</b></td><td>461.60 <b>(-23.25%)</b></td><td>290.98 <b>(-38.52%)</b></td><td>256.00 <b>(-47.82%)</b></td><td>234.90 <b>(-37.81%)</b></td><td>95.81 (+3.24%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>601.40 (n/a)</td><td>473.28 (n/a)</td><td>490.60 (n/a)</td><td>377.70 (n/a)</td><td>92.80 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.17 (+3.68%)</td><td>0.13 (-13.33%)</td><td>0.12 <b>(-21.78%)</b></td><td>0.08 <b>(-44.14%)</b></td><td>0.04 <b>(+192.49%)</b></td><td>545.20 <b>(+78.99%)</b></td><td>348.16 <b>(+25.26%)</b></td><td>348.00 <b>(+27.85%)</b></td><td>239.00 (-3.55%)</td><td>123.44 <b>(+381.21%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>304.60 (n/a)</td><td>277.94 (n/a)</td><td>272.20 (n/a)</td><td>247.80 (n/a)</td><td>25.65 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.15 (-3.42%)</td><td>0.10 (-13.36%)</td><td>0.09 <b>(-28.00%)</b></td><td>0.06 <b>(-24.48%)</b></td><td>0.04 <b>(+43.60%)</b></td><td>632.20 <b>(+32.43%)</b></td><td>456.70 <b>(+24.19%)</b></td><td>480.40 <b>(+38.88%)</b></td><td>279.20 (+3.56%)</td><td>165.70 <b>(+88.94%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>477.40 (n/a)</td><td>367.74 (n/a)</td><td>345.90 (n/a)</td><td>269.60 (n/a)</td><td>87.70 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.17 (+1.80%)</td><td>0.11 (+1.52%)</td><td>0.15 <b>(+48.46%)</b></td><td>0.02 <b>(-37.58%)</b></td><td>0.08 <b>(+48.42%)</b></td><td>2101.30 <b>(+60.20%)</b></td><td>957.70 <b>(+72.77%)</b></td><td>266.10 <b>(-32.65%)</b></td><td>245.70 (-1.76%)</td><td>966.10 <b>(+121.32%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.05 (n/a)</td><td>1311.70 (n/a)</td><td>554.32 (n/a)</td><td>395.10 (n/a)</td><td>250.10 (n/a)</td><td>436.51 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (+11.92%)</td><td>0.10 <b>(+23.90%)</b></td><td>0.08 (+18.03%)</td><td>0.05 (+6.96%)</td><td>0.04 <b>(+27.77%)</b></td><td>639.70 (-6.52%)</td><td>409.86 (-17.33%)</td><td>431.70 (-15.29%)</td><td>241.50 (-10.62%)</td><td>170.71 (-5.58%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>684.30 (n/a)</td><td>495.78 (n/a)</td><td>509.60 (n/a)</td><td>270.20 (n/a)</td><td>180.80 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.16 <b>(+21.16%)</b></td><td>0.12 (+19.36%)</td><td>0.12 <b>(+33.34%)</b></td><td>0.07 (-11.35%)</td><td>0.03 <b>(+34.64%)</b></td><td>487.50 (+12.80%)</td><td>310.14 (-13.68%)</td><td>291.30 <b>(-25.00%)</b></td><td>213.80 (-17.45%)</td><td>104.73 <b>(+29.91%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>432.20 (n/a)</td><td>359.28 (n/a)</td><td>388.40 (n/a)</td><td>259.00 (n/a)</td><td>80.61 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 <b>(+63.97%)</b></td><td>0.09 <b>(+21.58%)</b></td><td>0.08 (-1.65%)</td><td>0.06 (-6.76%)</td><td>0.03 <b>(+261.13%)</b></td><td>580.90 (+7.26%)</td><td>412.00 (-10.76%)</td><td>438.40 (+1.67%)</td><td>252.40 <b>(-39.02%)</b></td><td>134.12 <b>(+133.35%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>541.60 (n/a)</td><td>461.66 (n/a)</td><td>431.20 (n/a)</td><td>413.90 (n/a)</td><td>57.47 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.17 <b>(+45.09%)</b></td><td>0.12 <b>(+48.54%)</b></td><td>0.12 <b>(+73.12%)</b></td><td>0.07 (+18.05%)</td><td>0.04 <b>(+67.47%)</b></td><td>512.70 (-15.28%)</td><td>321.72 <b>(-29.91%)</b></td><td>297.10 <b>(-42.24%)</b></td><td>206.90 <b>(-31.08%)</b></td><td>126.61 (-3.85%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>605.20 (n/a)</td><td>459.00 (n/a)</td><td>514.40 (n/a)</td><td>300.20 (n/a)</td><td>131.68 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (+14.85%)</td><td>0.09 (+19.25%)</td><td>0.08 (+6.07%)</td><td>0.05 <b>(+48.94%)</b></td><td>0.03 (+16.92%)</td><td>699.80 <b>(-32.86%)</b></td><td>448.00 (-19.39%)</td><td>455.90 (-5.71%)</td><td>269.90 (-12.91%)</td><td>178.71 <b>(-38.10%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1042.30 (n/a)</td><td>555.76 (n/a)</td><td>483.50 (n/a)</td><td>309.90 (n/a)</td><td>288.69 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (-6.59%)</td><td>0.07 (-16.96%)</td><td>0.06 <b>(-22.53%)</b></td><td>0.05 (-19.79%)</td><td>0.02 (+14.58%)</td><td>733.50 <b>(+24.68%)</b></td><td>529.40 <b>(+24.76%)</b></td><td>537.90 <b>(+29.09%)</b></td><td>315.10 (+7.03%)</td><td>163.26 <b>(+50.63%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>588.30 (n/a)</td><td>424.32 (n/a)</td><td>416.70 (n/a)</td><td>294.40 (n/a)</td><td>108.38 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.49 (-7.71%)</td><td>0.34 (-16.52%)</td><td>0.30 <b>(-28.27%)</b></td><td>0.21 (-12.41%)</td><td>0.12 (+12.36%)</td><td>628.30 (+14.15%)</td><td>431.72 <b>(+23.34%)</b></td><td>441.10 <b>(+39.41%)</b></td><td>268.80 (+8.34%)</td><td>148.43 <b>(+27.24%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.53 (n/a)</td><td>0.40 (n/a)</td><td>0.41 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>550.40 (n/a)</td><td>350.02 (n/a)</td><td>316.40 (n/a)</td><td>248.10 (n/a)</td><td>116.66 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.43 <b>(-28.09%)</b></td><td>0.31 (-16.88%)</td><td>0.31 (+13.88%)</td><td>0.18 <b>(-30.34%)</b></td><td>0.10 <b>(-31.28%)</b></td><td>732.20 <b>(+43.54%)</b></td><td>467.72 (+18.84%)</td><td>419.50 (-12.18%)</td><td>306.00 <b>(+39.03%)</b></td><td>175.73 <b>(+31.55%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.60 (n/a)</td><td>0.37 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>510.10 (n/a)</td><td>393.56 (n/a)</td><td>477.70 (n/a)</td><td>220.10 (n/a)</td><td>133.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.49 (-7.81%)</td><td>0.37 (+6.07%)</td><td>0.40 <b>(+49.47%)</b></td><td>0.24 (+2.84%)</td><td>0.11 (-10.12%)</td><td>535.00 (-2.76%)</td><td>390.10 (-6.52%)</td><td>323.80 <b>(-33.10%)</b></td><td>269.90 (+8.48%)</td><td>129.35 (-0.11%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.53 (n/a)</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>550.20 (n/a)</td><td>417.32 (n/a)</td><td>484.00 (n/a)</td><td>248.80 (n/a)</td><td>129.50 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (+9.43%)</td><td>0.02 <b>(+30.42%)</b></td><td>0.02 <b>(+27.45%)</b></td><td>0.01 <b>(+73.48%)</b></td><td>0.00 (-17.19%)</td><td>376.80 <b>(-42.36%)</b></td><td>284.42 <b>(-30.41%)</b></td><td>235.60 <b>(-21.52%)</b></td><td>222.40 (-8.59%)</td><td>79.06 <b>(-57.62%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>653.70 (n/a)</td><td>408.72 (n/a)</td><td>300.20 (n/a)</td><td>243.30 (n/a)</td><td>186.56 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 <b>(+35.89%)</b></td><td>0.01 <b>(+28.25%)</b></td><td>0.02 <b>(+86.27%)</b></td><td>0.01 (-7.62%)</td><td>0.01 <b>(+58.23%)</b></td><td>561.80 (+8.25%)</td><td>349.38 (-15.99%)</td><td>256.40 <b>(-46.30%)</b></td><td>202.40 <b>(-26.40%)</b></td><td>158.06 <b>(+30.04%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>519.00 (n/a)</td><td>415.88 (n/a)</td><td>477.50 (n/a)</td><td>275.00 (n/a)</td><td>121.55 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 <b>(+28.82%)</b></td><td>0.02 <b>(+33.62%)</b></td><td>0.02 <b>(+100.25%)</b></td><td>0.01 (-17.31%)</td><td>0.01 (+18.60%)</td><td>662.20 <b>(+20.93%)</b></td><td>328.34 <b>(-22.29%)</b></td><td>267.60 <b>(-50.06%)</b></td><td>171.00 <b>(-22.38%)</b></td><td>191.58 (+16.06%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.60 (n/a)</td><td>422.54 (n/a)</td><td>535.80 (n/a)</td><td>220.30 (n/a)</td><td>165.07 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>9.42 (+6.74%)</td><td>8.09 (+7.36%)</td><td>8.90 (+14.81%)</td><td>5.58 (+7.71%)</td><td>1.64 (+18.14%)</td><td>376.10 (-7.16%)</td><td>269.82 (-6.38%)</td><td>235.80 (-12.92%)</td><td>222.70 (-6.31%)</td><td>65.01 (-2.61%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>8.83 (n/a)</td><td>7.54 (n/a)</td><td>7.75 (n/a)</td><td>5.18 (n/a)</td><td>1.39 (n/a)</td><td>405.10 (n/a)</td><td>288.22 (n/a)</td><td>270.80 (n/a)</td><td>237.70 (n/a)</td><td>66.75 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.60 (+8.84%)</td><td>0.45 (+17.44%)</td><td>0.47 (+3.87%)</td><td>0.22 <b>(+70.02%)</b></td><td>0.16 (-16.92%)</td><td>593.30 <b>(-41.18%)</b></td><td>339.92 <b>(-29.06%)</b></td><td>283.70 (-3.73%)</td><td>219.30 (-8.09%)</td><td>155.89 <b>(-53.42%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.55 (n/a)</td><td>0.38 (n/a)</td><td>0.45 (n/a)</td><td>0.13 (n/a)</td><td>0.20 (n/a)</td><td>1008.70 (n/a)</td><td>479.18 (n/a)</td><td>294.70 (n/a)</td><td>238.60 (n/a)</td><td>334.68 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.49 (-0.78%)</td><td>0.37 (-7.23%)</td><td>0.41 (-9.72%)</td><td>0.23 (-18.20%)</td><td>0.11 (+4.82%)</td><td>570.30 <b>(+22.25%)</b></td><td>382.10 (+9.82%)</td><td>322.50 (+10.79%)</td><td>268.50 (+0.79%)</td><td>125.00 <b>(+29.42%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.45 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>466.50 (n/a)</td><td>347.92 (n/a)</td><td>291.10 (n/a)</td><td>266.40 (n/a)</td><td>96.59 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.79 <b>(+59.77%)</b></td><td>0.46 (+8.32%)</td><td>0.36 (-19.71%)</td><td>0.31 (+17.18%)</td><td>0.20 <b>(+117.54%)</b></td><td>421.10 (-14.67%)</td><td>320.78 (-1.09%)</td><td>363.50 <b>(+24.57%)</b></td><td>168.20 <b>(-37.40%)</b></td><td>108.46 (+14.02%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.49 (n/a)</td><td>0.43 (n/a)</td><td>0.45 (n/a)</td><td>0.27 (n/a)</td><td>0.09 (n/a)</td><td>493.50 (n/a)</td><td>324.32 (n/a)</td><td>291.80 (n/a)</td><td>268.70 (n/a)</td><td>95.13 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.71 <b>(+31.44%)</b></td><td>0.44 <b>(+38.47%)</b></td><td>0.33 (-0.82%)</td><td>0.26 <b>(+299.54%)</b></td><td>0.20 (+16.12%)</td><td>513.50 <b>(-74.97%)</b></td><td>349.52 <b>(-50.24%)</b></td><td>405.10 (+0.85%)</td><td>186.30 <b>(-23.93%)</b></td><td>137.68 <b>(-81.82%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.54 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.06 (n/a)</td><td>0.17 (n/a)</td><td>2051.70 (n/a)</td><td>702.46 (n/a)</td><td>401.70 (n/a)</td><td>244.90 (n/a)</td><td>757.48 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.71 <b>(+58.31%)</b></td><td>0.44 <b>(+29.41%)</b></td><td>0.49 <b>(+41.53%)</b></td><td>0.26 (+15.08%)</td><td>0.19 <b>(+100.58%)</b></td><td>514.20 (-13.10%)</td><td>347.12 (-15.53%)</td><td>268.90 <b>(-29.35%)</b></td><td>186.70 <b>(-36.82%)</b></td><td>151.86 <b>(+23.23%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.45 (n/a)</td><td>0.34 (n/a)</td><td>0.35 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>591.70 (n/a)</td><td>410.96 (n/a)</td><td>380.60 (n/a)</td><td>295.50 (n/a)</td><td>123.24 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 <b>(+26.79%)</b></td><td>0.01 <b>(+23.62%)</b></td><td>0.02 (+15.70%)</td><td>0.01 <b>(+32.64%)</b></td><td>0.00 (+10.42%)</td><td>429.10 <b>(-24.60%)</b></td><td>309.88 <b>(-20.97%)</b></td><td>256.60 (-13.54%)</td><td>221.20 <b>(-21.14%)</b></td><td>95.72 <b>(-32.13%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.10 (n/a)</td><td>392.08 (n/a)</td><td>296.80 (n/a)</td><td>280.50 (n/a)</td><td>141.05 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 <b>(+37.06%)</b></td><td>0.02 <b>(+29.90%)</b></td><td>0.01 <b>(+63.06%)</b></td><td>0.01 (-1.68%)</td><td>0.01 <b>(+25.14%)</b></td><td>484.40 (+1.70%)</td><td>296.90 <b>(-22.23%)</b></td><td>281.30 <b>(-38.69%)</b></td><td>178.50 <b>(-27.02%)</b></td><td>113.16 (-4.73%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>476.30 (n/a)</td><td>381.76 (n/a)</td><td>458.80 (n/a)</td><td>244.60 (n/a)</td><td>118.78 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.00 <b>(+166.67%)</b></td><td>0.00 <b>(+141.67%)</b></td><td>0.00 <b>(+200.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+316.33%)</b></td><td>18214.36 (-8.39%)</td><td>8456.72 <b>(-50.97%)</b></td><td>6402.69 <b>(-62.80%)</b></td><td>5385.15 <b>(-65.44%)</b></td><td>5485.63 <b>(+236.98%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19881.83 (n/a)</td><td>17247.39 (n/a)</td><td>17209.68 (n/a)</td><td>15581.14 (n/a)</td><td>1627.87 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.00 (-7.14%)</td><td>0.00 (-16.07%)</td><td>0.00 (-7.69%)</td><td>0.00 (+0.00%)</td><td>0.00 (+10.25%)</td><td>19769.92 (-10.19%)</td><td>11338.18 (+19.81%)</td><td>6973.77 (+9.67%)</td><td>6113.42 (+3.34%)</td><td>6631.96 (-5.54%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22012.64 (n/a)</td><td>9463.46 (n/a)</td><td>6358.95 (n/a)</td><td>5915.63 (n/a)</td><td>7020.99 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (-7.30%)</td><td>0.10 (+13.01%)</td><td>0.09 (+16.20%)</td><td>0.07 (+1.77%)</td><td>0.03 (-4.50%)</td><td>27989.25 (-1.77%)</td><td>21823.89 (-11.68%)</td><td>23010.13 (-13.98%)</td><td>15291.23 (+7.83%)</td><td>6088.02 (+2.66%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>28493.21 (n/a)</td><td>24709.67 (n/a)</td><td>26749.72 (n/a)</td><td>14180.70 (n/a)</td><td>5930.09 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 <b>(+57.98%)</b></td><td>0.09 (+14.95%)</td><td>0.08 (+6.75%)</td><td>0.07 (+3.31%)</td><td>0.02 <b>(+421.82%)</b></td><td>29207.81 (-3.23%)</td><td>24893.67 (-9.11%)</td><td>25512.42 (-6.33%)</td><td>16170.02 <b>(-36.70%)</b></td><td>5296.16 <b>(+210.11%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.00 (n/a)</td><td>30181.70 (n/a)</td><td>27387.49 (n/a)</td><td>27235.58 (n/a)</td><td>25546.82 (n/a)</td><td>1707.85 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.53 (-3.20%)</td><td>1.36 (-12.31%)</td><td>1.26 (-12.85%)</td><td>0.30 (+0.79%)</td><td>0.82 (-5.11%)</td><td>3478.50 (-0.79%)</td><td>1272.96 (+7.43%)</td><td>833.80 (+14.74%)</td><td>413.60 (+3.30%)</td><td>1253.02 (-4.11%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.62 (n/a)</td><td>1.55 (n/a)</td><td>1.44 (n/a)</td><td>0.30 (n/a)</td><td>0.87 (n/a)</td><td>3506.10 (n/a)</td><td>1184.92 (n/a)</td><td>726.70 (n/a)</td><td>400.40 (n/a)</td><td>1306.79 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.16 (-6.25%)</td><td>2.22 (+15.96%)</td><td>2.58 <b>(+33.16%)</b></td><td>0.79 <b>(+165.26%)</b></td><td>0.96 (-15.38%)</td><td>1321.40 <b>(-62.30%)</b></td><td>606.72 <b>(-44.52%)</b></td><td>406.30 <b>(-24.90%)</b></td><td>332.20 (+6.68%)</td><td>413.18 <b>(-69.51%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.37 (n/a)</td><td>1.92 (n/a)</td><td>1.94 (n/a)</td><td>0.30 (n/a)</td><td>1.13 (n/a)</td><td>3505.20 (n/a)</td><td>1093.58 (n/a)</td><td>541.00 (n/a)</td><td>311.40 (n/a)</td><td>1354.93 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.35 (+2.03%)</td><td>2.22 (+16.26%)</td><td>2.45 <b>(+47.50%)</b></td><td>0.78 <b>(+155.05%)</b></td><td>1.03 <b>(-20.62%)</b></td><td>1348.70 <b>(-60.79%)</b></td><td>618.74 <b>(-45.17%)</b></td><td>428.20 <b>(-32.20%)</b></td><td>313.20 (-2.00%)</td><td>427.17 <b>(-67.53%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.28 (n/a)</td><td>1.91 (n/a)</td><td>1.66 (n/a)</td><td>0.30 (n/a)</td><td>1.30 (n/a)</td><td>3439.90 (n/a)</td><td>1128.40 (n/a)</td><td>631.60 (n/a)</td><td>319.60 (n/a)</td><td>1315.69 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>4.52 <b>(+117.26%)</b></td><td>2.21 <b>(+37.70%)</b></td><td>1.90 <b>(+20.71%)</b></td><td>0.64 <b>(-47.39%)</b></td><td>1.42 <b>(+352.87%)</b></td><td>1641.10 <b>(+90.07%)</b></td><td>696.34 (+3.33%)</td><td>551.50 (-17.15%)</td><td>232.00 <b>(-53.97%)</b></td><td>544.66 <b>(+322.18%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.08 (n/a)</td><td>1.60 (n/a)</td><td>1.58 (n/a)</td><td>1.21 (n/a)</td><td>0.31 (n/a)</td><td>863.40 (n/a)</td><td>673.88 (n/a)</td><td>665.70 (n/a)</td><td>504.00 (n/a)</td><td>129.01 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.14 (-4.90%)</td><td>2.27 (+6.11%)</td><td>2.50 (+1.42%)</td><td>0.57 (-13.83%)</td><td>1.00 (-16.06%)</td><td>3688.60 (+16.05%)</td><td>1370.84 (-5.14%)</td><td>839.80 (-1.41%)</td><td>668.60 (+5.16%)</td><td>1299.20 (+18.38%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.30 (n/a)</td><td>2.13 (n/a)</td><td>2.46 (n/a)</td><td>0.66 (n/a)</td><td>1.20 (n/a)</td><td>3178.50 (n/a)</td><td>1445.14 (n/a)</td><td>851.80 (n/a)</td><td>635.80 (n/a)</td><td>1097.51 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>4.81 <b>(+28.37%)</b></td><td>3.92 <b>(+48.86%)</b></td><td>4.19 <b>(+31.29%)</b></td><td>2.99 <b>(+394.93%)</b></td><td>0.76 <b>(-43.49%)</b></td><td>700.60 <b>(-79.79%)</b></td><td>553.08 <b>(-56.41%)</b></td><td>500.00 <b>(-23.83%)</b></td><td>435.80 <b>(-22.11%)</b></td><td>112.93 <b>(-90.95%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.75 (n/a)</td><td>2.63 (n/a)</td><td>3.19 (n/a)</td><td>0.60 (n/a)</td><td>1.35 (n/a)</td><td>3467.30 (n/a)</td><td>1268.68 (n/a)</td><td>656.40 (n/a)</td><td>559.50 (n/a)</td><td>1248.19 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>4.35 (-4.05%)</td><td>2.82 (+10.14%)</td><td>3.09 (+19.29%)</td><td>0.84 <b>(+38.29%)</b></td><td>1.38 (-2.14%)</td><td>2507.80 <b>(-27.69%)</b></td><td>1042.46 (-18.70%)</td><td>678.50 (-16.17%)</td><td>481.60 (+4.22%)</td><td>840.21 <b>(-31.92%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>4.54 (n/a)</td><td>2.56 (n/a)</td><td>2.59 (n/a)</td><td>0.60 (n/a)</td><td>1.41 (n/a)</td><td>3468.00 (n/a)</td><td>1282.16 (n/a)</td><td>809.40 (n/a)</td><td>462.10 (n/a)</td><td>1234.06 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>6.03 (+4.06%)</td><td>3.84 (-11.56%)</td><td>3.46 (-16.32%)</td><td>2.81 (+10.81%)</td><td>1.28 (-5.55%)</td><td>747.20 (-9.76%)</td><td>585.44 (+10.81%)</td><td>605.80 (+19.51%)</td><td>347.70 (-3.90%)</td><td>152.32 (-19.33%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>5.80 (n/a)</td><td>4.34 (n/a)</td><td>4.14 (n/a)</td><td>2.53 (n/a)</td><td>1.36 (n/a)</td><td>828.00 (n/a)</td><td>528.32 (n/a)</td><td>506.90 (n/a)</td><td>361.80 (n/a)</td><td>188.82 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>6.41 (+11.30%)</td><td>2.63 <b>(-31.06%)</b></td><td>1.74 <b>(-63.47%)</b></td><td>0.59 (-0.20%)</td><td>2.49 (+13.77%)</td><td>3578.80 (+0.20%)</td><td>1827.06 <b>(+63.83%)</b></td><td>1202.50 <b>(+173.79%)</b></td><td>327.00 (-10.14%)</td><td>1586.64 (+14.54%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>5.76 (n/a)</td><td>3.82 (n/a)</td><td>4.77 (n/a)</td><td>0.59 (n/a)</td><td>2.19 (n/a)</td><td>3571.80 (n/a)</td><td>1115.24 (n/a)</td><td>439.20 (n/a)</td><td>363.90 (n/a)</td><td>1385.27 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>6.34 (-1.78%)</td><td>3.44 (-14.18%)</td><td>3.81 (+6.61%)</td><td>1.16 <b>(-44.80%)</b></td><td>2.05 (+18.20%)</td><td>1813.90 <b>(+81.17%)</b></td><td>873.60 <b>(+42.94%)</b></td><td>549.80 (-6.21%)</td><td>330.50 (+1.79%)</td><td>610.29 <b>(+129.26%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>6.46 (n/a)</td><td>4.00 (n/a)</td><td>3.58 (n/a)</td><td>2.09 (n/a)</td><td>1.73 (n/a)</td><td>1001.20 (n/a)</td><td>611.18 (n/a)</td><td>586.20 (n/a)</td><td>324.70 (n/a)</td><td>266.19 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.64 (-10.05%)</td><td>2.60 <b>(-24.88%)</b></td><td>3.23 (-11.75%)</td><td>1.03 <b>(-51.28%)</b></td><td>1.15 <b>(+45.76%)</b></td><td>4067.00 <b>(+105.25%)</b></td><td>2039.26 <b>(+58.78%)</b></td><td>1299.60 (+13.30%)</td><td>1152.30 (+11.17%)</td><td>1248.12 <b>(+214.81%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>4.05 (n/a)</td><td>3.46 (n/a)</td><td>3.66 (n/a)</td><td>2.12 (n/a)</td><td>0.79 (n/a)</td><td>1981.50 (n/a)</td><td>1284.32 (n/a)</td><td>1147.00 (n/a)</td><td>1036.50 (n/a)</td><td>396.47 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>6.25 (-6.13%)</td><td>4.79 (+3.86%)</td><td>4.00 (-13.57%)</td><td>3.88 <b>(+244.09%)</b></td><td>1.16 <b>(-46.09%)</b></td><td>1079.80 <b>(-70.94%)</b></td><td>913.84 <b>(-33.35%)</b></td><td>1049.50 (+15.70%)</td><td>671.50 (+6.52%)</td><td>201.88 <b>(-84.67%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>6.65 (n/a)</td><td>4.62 (n/a)</td><td>4.62 (n/a)</td><td>1.13 (n/a)</td><td>2.15 (n/a)</td><td>3715.70 (n/a)</td><td>1371.12 (n/a)</td><td>907.10 (n/a)</td><td>630.40 (n/a)</td><td>1316.73 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>5.68 (-15.86%)</td><td>4.33 (-15.53%)</td><td>4.93 (+6.33%)</td><td>1.25 <b>(-68.28%)</b></td><td>1.76 <b>(+32.10%)</b></td><td>3349.40 <b>(+215.30%)</b></td><td>1331.60 <b>(+54.40%)</b></td><td>849.90 (-5.96%)</td><td>738.20 (+18.85%)</td><td>1129.45 <b>(+433.58%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>6.75 (n/a)</td><td>5.12 (n/a)</td><td>4.64 (n/a)</td><td>3.95 (n/a)</td><td>1.33 (n/a)</td><td>1062.30 (n/a)</td><td>862.42 (n/a)</td><td>903.80 (n/a)</td><td>621.10 (n/a)</td><td>211.67 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>7.63 (-17.73%)</td><td>6.11 (-9.90%)</td><td>6.54 (-4.40%)</td><td>3.35 (-18.05%)</td><td>1.62 (-12.76%)</td><td>1251.60 <b>(+22.02%)</b></td><td>745.88 (+12.40%)</td><td>641.30 (+4.60%)</td><td>550.00 <b>(+21.55%)</b></td><td>285.71 <b>(+32.58%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>9.27 (n/a)</td><td>6.78 (n/a)</td><td>6.84 (n/a)</td><td>4.09 (n/a)</td><td>1.85 (n/a)</td><td>1025.70 (n/a)</td><td>663.58 (n/a)</td><td>613.10 (n/a)</td><td>452.50 (n/a)</td><td>215.50 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>7.88 (-16.49%)</td><td>5.33 (-19.74%)</td><td>6.52 (-14.88%)</td><td>1.17 <b>(-70.36%)</b></td><td>2.63 (+3.07%)</td><td>3599.60 <b>(+237.36%)</b></td><td>1269.96 <b>(+74.67%)</b></td><td>643.30 (+17.48%)</td><td>532.00 (+19.74%)</td><td>1311.11 <b>(+320.32%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>9.44 (n/a)</td><td>6.64 (n/a)</td><td>7.66 (n/a)</td><td>3.93 (n/a)</td><td>2.55 (n/a)</td><td>1067.00 (n/a)</td><td>727.06 (n/a)</td><td>547.60 (n/a)</td><td>444.30 (n/a)</td><td>311.93 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>6.69 <b>(-24.09%)</b></td><td>4.49 <b>(-40.39%)</b></td><td>3.95 <b>(-47.88%)</b></td><td>3.84 <b>(-37.63%)</b></td><td>1.23 (+5.11%)</td><td>1093.40 <b>(+60.32%)</b></td><td>976.90 <b>(+72.03%)</b></td><td>1061.00 <b>(+91.86%)</b></td><td>627.40 <b>(+31.75%)</b></td><td>196.32 <b>(+118.19%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>8.81 (n/a)</td><td>7.53 (n/a)</td><td>7.59 (n/a)</td><td>6.15 (n/a)</td><td>1.17 (n/a)</td><td>682.00 (n/a)</td><td>567.86 (n/a)</td><td>553.00 (n/a)</td><td>476.20 (n/a)</td><td>89.97 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.33 (-14.49%)</td><td>0.89 (-7.76%)</td><td>0.86 (-1.45%)</td><td>0.21 <b>(-64.80%)</b></td><td>0.45 (+19.11%)</td><td>2463.70 <b>(+184.07%)</b></td><td>914.10 <b>(+49.87%)</b></td><td>607.20 (+1.47%)</td><td>395.50 (+16.94%)</td><td>875.42 <b>(+313.03%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.55 (n/a)</td><td>0.96 (n/a)</td><td>0.88 (n/a)</td><td>0.60 (n/a)</td><td>0.38 (n/a)</td><td>867.30 (n/a)</td><td>609.94 (n/a)</td><td>598.40 (n/a)</td><td>338.20 (n/a)</td><td>211.95 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.24 (-2.85%)</td><td>1.48 <b>(-21.10%)</b></td><td>1.57 <b>(-23.71%)</b></td><td>0.31 <b>(-68.25%)</b></td><td>0.80 <b>(+52.81%)</b></td><td>3367.90 <b>(+214.93%)</b></td><td>1190.70 <b>(+92.81%)</b></td><td>668.70 <b>(+31.09%)</b></td><td>468.70 (+2.92%)</td><td>1233.60 <b>(+381.39%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>2.30 (n/a)</td><td>1.87 (n/a)</td><td>2.06 (n/a)</td><td>0.98 (n/a)</td><td>0.53 (n/a)</td><td>1069.40 (n/a)</td><td>617.54 (n/a)</td><td>510.10 (n/a)</td><td>455.40 (n/a)</td><td>256.26 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.45 <b>(-23.32%)</b></td><td>1.60 <b>(-28.13%)</b></td><td>1.67 <b>(-24.69%)</b></td><td>0.60 (+2.27%)</td><td>0.66 <b>(-36.42%)</b></td><td>3469.80 (-2.22%)</td><td>1629.04 (+19.03%)</td><td>1257.60 <b>(+32.78%)</b></td><td>854.30 <b>(+30.41%)</b></td><td>1045.27 (-14.89%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>3.20 (n/a)</td><td>2.23 (n/a)</td><td>2.21 (n/a)</td><td>0.59 (n/a)</td><td>1.04 (n/a)</td><td>3548.70 (n/a)</td><td>1368.64 (n/a)</td><td>947.10 (n/a)</td><td>655.10 (n/a)</td><td>1228.10 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.01 (+14.13%)</td><td>1.53 <b>(+52.98%)</b></td><td>1.67 <b>(+57.93%)</b></td><td>0.88 <b>(+216.62%)</b></td><td>0.42 <b>(-27.65%)</b></td><td>594.20 <b>(-68.42%)</b></td><td>370.20 <b>(-52.88%)</b></td><td>314.50 <b>(-36.68%)</b></td><td>261.40 (-12.40%)</td><td>130.67 <b>(-79.77%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>1.76 (n/a)</td><td>1.00 (n/a)</td><td>1.06 (n/a)</td><td>0.28 (n/a)</td><td>0.58 (n/a)</td><td>1881.40 (n/a)</td><td>785.68 (n/a)</td><td>496.70 (n/a)</td><td>298.40 (n/a)</td><td>646.03 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (-17.84%)</td><td>0.08 (-6.44%)</td><td>0.08 (+0.63%)</td><td>0.07 <b>(+23.34%)</b></td><td>0.01 <b>(-47.92%)</b></td><td>455.10 (-18.92%)</td><td>412.74 (+1.54%)</td><td>425.00 (-0.63%)</td><td>309.30 <b>(+21.72%)</b></td><td>59.59 <b>(-48.44%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>561.30 (n/a)</td><td>406.50 (n/a)</td><td>427.70 (n/a)</td><td>254.10 (n/a)</td><td>115.57 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (+13.95%)</td><td>0.10 (+0.82%)</td><td>0.08 <b>(-22.99%)</b></td><td>0.07 (+17.20%)</td><td>0.03 (+1.35%)</td><td>444.00 (-14.68%)</td><td>363.66 (-2.29%)</td><td>411.20 <b>(+29.88%)</b></td><td>240.90 (-12.24%)</td><td>88.00 <b>(-22.85%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>520.40 (n/a)</td><td>372.20 (n/a)</td><td>316.60 (n/a)</td><td>274.50 (n/a)</td><td>114.06 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.30 <b>(+25.06%)</b></td><td>0.15 (-13.24%)</td><td>0.11 <b>(-29.52%)</b></td><td>0.09 <b>(-22.97%)</b></td><td>0.09 <b>(+45.71%)</b></td><td>760.40 <b>(+29.83%)</b></td><td>521.72 <b>(+25.70%)</b></td><td>570.00 <b>(+41.86%)</b></td><td>216.90 <b>(-20.02%)</b></td><td>201.16 <b>(+41.96%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>585.70 (n/a)</td><td>415.04 (n/a)</td><td>401.80 (n/a)</td><td>271.20 (n/a)</td><td>141.70 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.35 <b>(+50.23%)</b></td><td>0.18 (+17.66%)</td><td>0.14 (+2.46%)</td><td>0.11 (-9.86%)</td><td>0.10 <b>(+112.08%)</b></td><td>602.70 (+10.95%)</td><td>436.74 (-3.95%)</td><td>477.10 (-2.39%)</td><td>186.10 <b>(-33.42%)</b></td><td>171.12 <b>(+55.47%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>543.20 (n/a)</td><td>454.72 (n/a)</td><td>488.80 (n/a)</td><td>279.50 (n/a)</td><td>110.07 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.37 (+12.28%)</td><td>0.15 (-13.85%)</td><td>0.11 <b>(-22.82%)</b></td><td>0.07 <b>(-42.89%)</b></td><td>0.13 <b>(+42.37%)</b></td><td>1005.50 <b>(+75.08%)</b></td><td>607.94 <b>(+43.69%)</b></td><td>579.10 <b>(+29.58%)</b></td><td>175.50 (-10.96%)</td><td>306.81 <b>(+120.11%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.33 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>574.30 (n/a)</td><td>423.10 (n/a)</td><td>446.90 (n/a)</td><td>197.10 (n/a)</td><td>139.39 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.56 <b>(+61.44%)</b></td><td>0.45 <b>(+59.59%)</b></td><td>0.48 <b>(+68.39%)</b></td><td>0.27 <b>(+30.84%)</b></td><td>0.12 <b>(+84.75%)</b></td><td>478.80 <b>(-23.58%)</b></td><td>310.26 <b>(-35.65%)</b></td><td>274.50 <b>(-40.61%)</b></td><td>232.20 <b>(-38.05%)</b></td><td>101.10 (-10.05%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>626.50 (n/a)</td><td>482.18 (n/a)</td><td>462.20 (n/a)</td><td>374.80 (n/a)</td><td>112.40 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.56 (+9.07%)</td><td>0.38 (+15.37%)</td><td>0.28 (-4.89%)</td><td>0.26 <b>(+20.22%)</b></td><td>0.15 <b>(+25.42%)</b></td><td>510.20 (-16.82%)</td><td>390.54 (-11.37%)</td><td>474.60 (+5.14%)</td><td>233.50 (-8.29%)</td><td>135.30 (-3.39%)</td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.51 (n/a)</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>613.40 (n/a)</td><td>440.64 (n/a)</td><td>451.40 (n/a)</td><td>254.60 (n/a)</td><td>140.05 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.55 (+5.69%)</td><td>0.28 <b>(-21.06%)</b></td><td>0.25 (-14.78%)</td><td>0.07 <b>(-69.53%)</b></td><td>0.17 <b>(+33.84%)</b></td><td>2011.30 <b>(+228.16%)</b></td><td>760.44 <b>(+81.82%)</b></td><td>514.70 (+17.32%)</td><td>240.00 (-5.40%)</td><td>710.79 <b>(+378.02%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.52 (n/a)</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>612.90 (n/a)</td><td>418.24 (n/a)</td><td>438.70 (n/a)</td><td>253.70 (n/a)</td><td>148.70 (n/a)</td>
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
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (-14.87%)</td><td>0.03 <b>(-21.71%)</b></td><td>0.03 <b>(-22.73%)</b></td><td>0.02 <b>(-27.41%)</b></td><td>0.01 (-12.50%)</td><td>832.80 <b>(+37.74%)</b></td><td>547.86 <b>(+29.86%)</b></td><td>543.70 <b>(+29.42%)</b></td><td>286.10 (+17.45%)</td><td>202.44 <b>(+37.09%)</b></td>
</tr>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:35:23</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>604.60 (n/a)</td><td>421.90 (n/a)</td><td>420.10 (n/a)</td><td>243.60 (n/a)</td><td>147.67 (n/a)</td>
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
