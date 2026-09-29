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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (-9.02%)</td><td>0.02 (-6.11%)</td><td>0.02 (-3.44%)</td><td>0.01 (-15.16%)</td><td>0.01 (+3.61%)</td><td>685.60 (+17.86%)</td><td>366.66 (+10.07%)</td><td>305.00 (+3.57%)</td><td>243.90 (+9.91%)</td><td>182.65 <b>(+28.50%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>581.70 (n/a)</td><td>333.12 (n/a)</td><td>294.50 (n/a)</td><td>221.90 (n/a)</td><td>142.14 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (+14.59%)</td><td>0.02 <b>(+28.21%)</b></td><td>0.03 <b>(+25.71%)</b></td><td>0.01 (+17.73%)</td><td>0.01 (+6.18%)</td><td>461.60 (-15.07%)</td><td>292.28 <b>(-22.87%)</b></td><td>243.80 <b>(-20.46%)</b></td><td>238.20 (-12.72%)</td><td>95.87 <b>(-20.57%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>543.50 (n/a)</td><td>378.96 (n/a)</td><td>306.50 (n/a)</td><td>272.90 (n/a)</td><td>120.70 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 <b>(+21.75%)</b></td><td>0.02 (+14.57%)</td><td>0.02 <b>(+38.21%)</b></td><td>0.01 <b>(-20.88%)</b></td><td>0.01 <b>(+61.48%)</b></td><td>747.80 <b>(+26.40%)</b></td><td>413.24 (+1.89%)</td><td>296.50 <b>(-27.63%)</b></td><td>212.80 (-17.87%)</td><td>241.76 <b>(+70.33%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.60 (n/a)</td><td>405.56 (n/a)</td><td>409.70 (n/a)</td><td>259.10 (n/a)</td><td>141.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (-10.46%)</td><td>0.02 (-3.99%)</td><td>0.02 (-14.78%)</td><td>0.01 (+18.32%)</td><td>0.01 <b>(-25.39%)</b></td><td>470.00 (-15.48%)</td><td>339.82 (-2.89%)</td><td>285.20 (+17.37%)</td><td>244.40 (+11.70%)</td><td>113.02 <b>(-29.52%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>556.10 (n/a)</td><td>349.92 (n/a)</td><td>243.00 (n/a)</td><td>218.80 (n/a)</td><td>160.36 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (-4.88%)</td><td>0.01 (-9.79%)</td><td>0.01 (-2.57%)</td><td>0.01 (-19.99%)</td><td>0.00 (-6.50%)</td><td>678.00 <b>(+24.98%)</b></td><td>471.64 (+11.56%)</td><td>468.80 (+2.65%)</td><td>297.20 (+5.13%)</td><td>138.89 <b>(+21.77%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>542.50 (n/a)</td><td>422.76 (n/a)</td><td>456.70 (n/a)</td><td>282.70 (n/a)</td><td>114.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 <b>(+61.56%)</b></td><td>0.01 (+10.08%)</td><td>0.01 (-0.76%)</td><td>0.01 (-8.07%)</td><td>0.01 <b>(+181.85%)</b></td><td>663.50 (+8.79%)</td><td>483.88 (+1.00%)</td><td>492.20 (+0.78%)</td><td>232.40 <b>(-38.09%)</b></td><td>166.26 <b>(+82.82%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>609.90 (n/a)</td><td>479.08 (n/a)</td><td>488.40 (n/a)</td><td>375.40 (n/a)</td><td>90.94 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 (+6.47%)</td><td>0.04 <b>(+28.98%)</b></td><td>0.04 <b>(+72.45%)</b></td><td>0.02 <b>(+25.53%)</b></td><td>0.01 (+1.64%)</td><td>513.80 <b>(-20.34%)</b></td><td>366.80 <b>(-25.06%)</b></td><td>346.70 <b>(-42.00%)</b></td><td>239.10 (-6.05%)</td><td>130.56 <b>(-27.14%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>645.00 (n/a)</td><td>489.46 (n/a)</td><td>597.80 (n/a)</td><td>254.50 (n/a)</td><td>179.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 (+2.81%)</td><td>0.04 (+11.28%)</td><td>0.05 (+5.03%)</td><td>0.03 (+15.96%)</td><td>0.01 (-14.95%)</td><td>478.80 (-13.76%)</td><td>295.44 (-13.41%)</td><td>243.80 (-4.80%)</td><td>237.20 (-2.71%)</td><td>103.96 <b>(-24.38%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>555.20 (n/a)</td><td>341.18 (n/a)</td><td>256.10 (n/a)</td><td>243.80 (n/a)</td><td>137.48 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 <b>(-45.55%)</b></td><td>0.03 (-17.85%)</td><td>0.03 (+7.54%)</td><td>0.01 <b>(-40.53%)</b></td><td>0.01 <b>(-45.55%)</b></td><td>977.60 <b>(+68.15%)</b></td><td>541.92 <b>(+22.00%)</b></td><td>434.90 (-7.01%)</td><td>422.70 <b>(+83.62%)</b></td><td>243.63 <b>(+82.91%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>581.40 (n/a)</td><td>444.18 (n/a)</td><td>467.70 (n/a)</td><td>230.20 (n/a)</td><td>133.20 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 <b>(+57.06%)</b></td><td>0.04 <b>(+63.52%)</b></td><td>0.05 <b>(+117.32%)</b></td><td>0.02 (+15.41%)</td><td>0.02 <b>(+169.27%)</b></td><td>502.80 (-13.36%)</td><td>340.68 <b>(-32.34%)</b></td><td>242.90 <b>(-53.99%)</b></td><td>223.30 <b>(-36.35%)</b></td><td>144.83 <b>(+57.64%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>580.30 (n/a)</td><td>503.52 (n/a)</td><td>527.90 (n/a)</td><td>350.80 (n/a)</td><td>91.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 <b>(-46.51%)</b></td><td>0.02 <b>(-37.09%)</b></td><td>0.02 (-0.99%)</td><td>0.01 <b>(-68.01%)</b></td><td>0.01 <b>(-26.64%)</b></td><td>1904.70 <b>(+212.66%)</b></td><td>859.70 <b>(+92.24%)</b></td><td>498.90 (+1.01%)</td><td>453.40 <b>(+86.97%)</b></td><td>622.07 <b>(+313.21%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>609.20 (n/a)</td><td>447.20 (n/a)</td><td>493.90 (n/a)</td><td>242.50 (n/a)</td><td>150.55 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 <b>(+25.94%)</b></td><td>0.03 (+1.47%)</td><td>0.03 (+8.45%)</td><td>0.02 (-13.55%)</td><td>0.01 <b>(+54.42%)</b></td><td>614.50 (+15.68%)</td><td>467.76 (+2.21%)</td><td>483.60 (-7.78%)</td><td>270.60 <b>(-20.60%)</b></td><td>125.67 <b>(+30.52%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.20 (n/a)</td><td>457.64 (n/a)</td><td>524.40 (n/a)</td><td>340.80 (n/a)</td><td>96.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 <b>(+88.42%)</b></td><td>0.08 <b>(+53.87%)</b></td><td>0.07 <b>(+25.25%)</b></td><td>0.05 <b>(+332.59%)</b></td><td>0.03 <b>(+46.22%)</b></td><td>468.30 <b>(-76.88%)</b></td><td>353.66 <b>(-51.96%)</b></td><td>366.90 <b>(-20.15%)</b></td><td>179.90 <b>(-46.93%)</b></td><td>121.46 <b>(-83.22%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2025.80 (n/a)</td><td>736.14 (n/a)</td><td>459.50 (n/a)</td><td>339.00 (n/a)</td><td>723.89 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.10 (-0.40%)</td><td>0.08 (-1.58%)</td><td>0.08 (+3.83%)</td><td>0.04 (-10.97%)</td><td>0.02 (+3.86%)</td><td>553.10 (+12.33%)</td><td>332.04 (+3.49%)</td><td>298.10 (-3.68%)</td><td>236.30 (+0.42%)</td><td>126.22 <b>(+23.52%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>492.40 (n/a)</td><td>320.84 (n/a)</td><td>309.50 (n/a)</td><td>235.30 (n/a)</td><td>102.18 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 (+1.49%)</td><td>0.06 (-14.36%)</td><td>0.05 (-4.96%)</td><td>0.03 <b>(-32.30%)</b></td><td>0.03 (+17.17%)</td><td>722.90 <b>(+47.71%)</b></td><td>478.50 <b>(+23.95%)</b></td><td>457.30 (+5.22%)</td><td>224.20 (-1.49%)</td><td>180.28 <b>(+55.87%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>489.40 (n/a)</td><td>386.04 (n/a)</td><td>434.60 (n/a)</td><td>227.60 (n/a)</td><td>115.66 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 <b>(-26.99%)</b></td><td>0.05 <b>(-25.55%)</b></td><td>0.04 <b>(-34.87%)</b></td><td>0.03 <b>(-21.46%)</b></td><td>0.02 (-18.50%)</td><td>791.80 <b>(+27.32%)</b></td><td>531.28 <b>(+36.45%)</b></td><td>564.30 <b>(+53.55%)</b></td><td>306.50 <b>(+36.95%)</b></td><td>203.36 <b>(+35.86%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>621.90 (n/a)</td><td>389.36 (n/a)</td><td>367.50 (n/a)</td><td>223.80 (n/a)</td><td>149.68 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.09 (+8.88%)</td><td>0.06 (+0.61%)</td><td>0.05 (-4.60%)</td><td>0.04 (-19.26%)</td><td>0.02 <b>(+48.33%)</b></td><td>682.50 <b>(+23.87%)</b></td><td>465.86 (+6.63%)</td><td>460.30 (+4.83%)</td><td>265.30 (-8.17%)</td><td>171.61 <b>(+73.40%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>551.00 (n/a)</td><td>436.88 (n/a)</td><td>439.10 (n/a)</td><td>288.90 (n/a)</td><td>98.97 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 <b>(-36.73%)</b></td><td>0.06 <b>(-20.06%)</b></td><td>0.06 (-12.15%)</td><td>0.04 <b>(+31.54%)</b></td><td>0.02 <b>(-59.51%)</b></td><td>556.80 <b>(-23.99%)</b></td><td>441.88 (+3.55%)</td><td>437.90 (+13.83%)</td><td>290.30 <b>(+58.03%)</b></td><td>110.76 <b>(-50.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>732.50 (n/a)</td><td>426.72 (n/a)</td><td>384.70 (n/a)</td><td>183.70 (n/a)</td><td>224.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.22 <b>(+20.22%)</b></td><td>0.19 <b>(+39.38%)</b></td><td>0.21 <b>(+60.42%)</b></td><td>0.10 (+6.18%)</td><td>0.05 <b>(+55.90%)</b></td><td>484.50 (-5.83%)</td><td>287.18 <b>(-25.24%)</b></td><td>239.20 <b>(-37.66%)</b></td><td>225.60 (-16.84%)</td><td>111.20 <b>(+25.83%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>514.50 (n/a)</td><td>384.16 (n/a)</td><td>383.70 (n/a)</td><td>271.30 (n/a)</td><td>88.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.22 (+4.72%)</td><td>0.14 <b>(-21.05%)</b></td><td>0.12 <b>(-33.28%)</b></td><td>0.08 (-14.00%)</td><td>0.06 <b>(+23.78%)</b></td><td>647.90 (+16.28%)</td><td>422.56 <b>(+33.60%)</b></td><td>411.50 <b>(+49.91%)</b></td><td>219.60 (-4.52%)</td><td>176.69 <b>(+29.84%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>557.20 (n/a)</td><td>316.28 (n/a)</td><td>274.50 (n/a)</td><td>230.00 (n/a)</td><td>136.08 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.19 <b>(+34.91%)</b></td><td>0.15 <b>(+79.49%)</b></td><td>0.17 <b>(+105.04%)</b></td><td>0.09 <b>(+255.21%)</b></td><td>0.05 (+16.22%)</td><td>519.50 <b>(-71.85%)</b></td><td>355.34 <b>(-54.88%)</b></td><td>287.50 <b>(-51.24%)</b></td><td>252.30 <b>(-25.88%)</b></td><td>126.98 <b>(-78.86%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1845.20 (n/a)</td><td>787.60 (n/a)</td><td>589.60 (n/a)</td><td>340.40 (n/a)</td><td>600.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.21 (-8.62%)</td><td>0.15 <b>(+28.60%)</b></td><td>0.19 <b>(+85.74%)</b></td><td>0.02 <b>(-23.19%)</b></td><td>0.08 (+9.40%)</td><td>2478.80 <b>(+30.19%)</b></td><td>736.20 (+3.36%)</td><td>259.30 <b>(-46.17%)</b></td><td>229.80 (+9.43%)</td><td>979.09 <b>(+44.53%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>0.08 (n/a)</td><td>1904.00 (n/a)</td><td>712.26 (n/a)</td><td>481.70 (n/a)</td><td>210.00 (n/a)</td><td>677.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.17 <b>(-28.05%)</b></td><td>0.13 (+2.47%)</td><td>0.14 <b>(+43.60%)</b></td><td>0.08 (-1.54%)</td><td>0.04 <b>(-31.51%)</b></td><td>610.10 (+1.56%)</td><td>424.42 (-5.61%)</td><td>346.90 <b>(-30.37%)</b></td><td>290.90 <b>(+38.99%)</b></td><td>155.95 (+5.74%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>600.70 (n/a)</td><td>449.66 (n/a)</td><td>498.20 (n/a)</td><td>209.30 (n/a)</td><td>147.48 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.20 (+8.40%)</td><td>0.13 (+1.34%)</td><td>0.11 (+6.00%)</td><td>0.09 (-3.59%)</td><td>0.04 (+5.93%)</td><td>532.50 (+3.72%)</td><td>405.88 (-1.18%)</td><td>445.30 (-5.66%)</td><td>249.00 (-7.74%)</td><td>110.51 (-1.91%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>513.40 (n/a)</td><td>410.74 (n/a)</td><td>472.00 (n/a)</td><td>269.90 (n/a)</td><td>112.67 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 (-18.43%)</td><td>0.01 (+7.88%)</td><td>0.01 <b>(+41.42%)</b></td><td>0.00 <b>(-55.91%)</b></td><td>0.00 (-4.71%)</td><td>2436.10 <b>(+126.80%)</b></td><td>738.92 <b>(+40.95%)</b></td><td>306.40 <b>(-29.29%)</b></td><td>236.60 <b>(+22.59%)</b></td><td>952.08 <b>(+188.54%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1074.10 (n/a)</td><td>524.26 (n/a)</td><td>433.30 (n/a)</td><td>193.00 (n/a)</td><td>329.96 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 <b>(-24.73%)</b></td><td>0.01 (-18.74%)</td><td>0.01 <b>(-28.80%)</b></td><td>0.01 (-8.84%)</td><td>0.00 <b>(-36.46%)</b></td><td>506.80 (+9.70%)</td><td>399.80 (+19.41%)</td><td>413.70 <b>(+40.48%)</b></td><td>285.30 <b>(+32.82%)</b></td><td>89.57 (-9.98%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>462.00 (n/a)</td><td>334.82 (n/a)</td><td>294.50 (n/a)</td><td>214.80 (n/a)</td><td>99.50 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 <b>(-24.95%)</b></td><td>0.01 (-17.85%)</td><td>0.01 (-10.00%)</td><td>0.00 (-9.29%)</td><td>0.00 <b>(-39.60%)</b></td><td>533.60 (+10.23%)</td><td>410.50 (+15.25%)</td><td>465.20 (+11.11%)</td><td>285.70 <b>(+33.26%)</b></td><td>112.37 (-11.52%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>484.10 (n/a)</td><td>356.18 (n/a)</td><td>418.70 (n/a)</td><td>214.40 (n/a)</td><td>127.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 (-1.21%)</td><td>0.01 (-11.36%)</td><td>0.01 (-12.89%)</td><td>0.00 <b>(-59.82%)</b></td><td>0.00 (+5.22%)</td><td>2498.00 <b>(+148.85%)</b></td><td>846.68 <b>(+57.43%)</b></td><td>519.30 (+14.79%)</td><td>250.00 (+1.21%)</td><td>929.77 <b>(+206.11%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1003.80 (n/a)</td><td>537.80 (n/a)</td><td>452.40 (n/a)</td><td>247.00 (n/a)</td><td>303.74 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 <b>(-30.88%)</b></td><td>0.01 <b>(-25.19%)</b></td><td>0.01 <b>(-39.26%)</b></td><td>0.00 (-0.19%)</td><td>0.00 <b>(-48.12%)</b></td><td>610.80 (+0.20%)</td><td>477.44 <b>(+24.22%)</b></td><td>500.70 <b>(+64.65%)</b></td><td>342.00 <b>(+44.67%)</b></td><td>113.54 <b>(-27.46%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>609.60 (n/a)</td><td>384.36 (n/a)</td><td>304.10 (n/a)</td><td>236.40 (n/a)</td><td>156.51 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 (-6.95%)</td><td>0.01 (+2.08%)</td><td>0.01 (-14.82%)</td><td>0.00 <b>(+146.77%)</b></td><td>0.00 <b>(-29.31%)</b></td><td>690.80 <b>(-59.48%)</b></td><td>486.14 <b>(-27.40%)</b></td><td>489.50 (+17.39%)</td><td>284.50 (+7.44%)</td><td>164.52 <b>(-72.14%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1704.70 (n/a)</td><td>669.62 (n/a)</td><td>417.00 (n/a)</td><td>264.80 (n/a)</td><td>590.58 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(-23.53%)</b></td><td>0.01 (-16.50%)</td><td>0.01 (+0.17%)</td><td>0.01 (-8.83%)</td><td>0.00 <b>(-45.26%)</b></td><td>566.90 (+9.67%)</td><td>426.34 (+12.17%)</td><td>393.90 (-0.18%)</td><td>293.60 <b>(+30.78%)</b></td><td>104.74 <b>(-22.81%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>516.90 (n/a)</td><td>380.08 (n/a)</td><td>394.60 (n/a)</td><td>224.50 (n/a)</td><td>135.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 <b>(+99.34%)</b></td><td>0.02 <b>(+38.47%)</b></td><td>0.02 <b>(+52.01%)</b></td><td>0.01 <b>(-20.11%)</b></td><td>0.01 <b>(+360.14%)</b></td><td>564.20 <b>(+25.18%)</b></td><td>347.10 (-10.13%)</td><td>261.00 <b>(-34.22%)</b></td><td>150.20 <b>(-49.85%)</b></td><td>181.37 <b>(+218.60%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>450.70 (n/a)</td><td>386.24 (n/a)</td><td>396.80 (n/a)</td><td>299.50 (n/a)</td><td>56.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 <b>(+22.62%)</b></td><td>0.02 (-8.27%)</td><td>0.02 (+7.43%)</td><td>0.01 <b>(-57.10%)</b></td><td>0.01 <b>(+831.21%)</b></td><td>658.70 <b>(+133.09%)</b></td><td>358.60 <b>(+32.52%)</b></td><td>251.10 (-6.90%)</td><td>208.40 (-18.43%)</td><td>193.96 <b>(+1625.10%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>282.60 (n/a)</td><td>270.60 (n/a)</td><td>269.70 (n/a)</td><td>255.50 (n/a)</td><td>11.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (+6.91%)</td><td>0.01 (+2.12%)</td><td>0.01 (-14.41%)</td><td>0.01 (+7.17%)</td><td>0.00 (+18.58%)</td><td>517.00 (-6.70%)</td><td>417.26 (-0.53%)</td><td>471.90 (+16.84%)</td><td>253.00 (-6.43%)</td><td>111.85 (+7.08%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>554.10 (n/a)</td><td>419.48 (n/a)</td><td>403.90 (n/a)</td><td>270.40 (n/a)</td><td>104.46 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (-7.56%)</td><td>0.01 <b>(-26.99%)</b></td><td>0.01 <b>(-38.73%)</b></td><td>0.01 <b>(-29.08%)</b></td><td>0.00 (+5.71%)</td><td>616.90 <b>(+41.01%)</b></td><td>453.42 <b>(+41.68%)</b></td><td>492.40 <b>(+63.21%)</b></td><td>252.60 (+8.18%)</td><td>136.15 <b>(+55.64%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>437.50 (n/a)</td><td>320.04 (n/a)</td><td>301.70 (n/a)</td><td>233.50 (n/a)</td><td>87.48 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(+26.39%)</b></td><td>0.01 (+15.93%)</td><td>0.01 (+14.45%)</td><td>0.01 (-8.98%)</td><td>0.00 <b>(+74.96%)</b></td><td>657.10 (+9.88%)</td><td>472.86 (-8.61%)</td><td>486.50 (-12.63%)</td><td>279.30 <b>(-20.88%)</b></td><td>152.23 <b>(+55.23%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>598.00 (n/a)</td><td>517.40 (n/a)</td><td>556.80 (n/a)</td><td>353.00 (n/a)</td><td>98.07 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 <b>(+26.72%)</b></td><td>0.03 <b>(+38.09%)</b></td><td>0.03 (+4.27%)</td><td>0.02 <b>(+266.32%)</b></td><td>0.01 (-10.44%)</td><td>581.70 <b>(-72.70%)</b></td><td>388.00 <b>(-49.77%)</b></td><td>411.70 (-4.10%)</td><td>264.90 <b>(-21.07%)</b></td><td>130.83 <b>(-82.93%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2130.80 (n/a)</td><td>772.40 (n/a)</td><td>429.30 (n/a)</td><td>335.60 (n/a)</td><td>766.54 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (+18.72%)</td><td>0.03 (-17.23%)</td><td>0.02 <b>(-31.72%)</b></td><td>0.02 <b>(-49.05%)</b></td><td>0.02 <b>(+203.99%)</b></td><td>598.00 <b>(+96.32%)</b></td><td>403.98 <b>(+47.62%)</b></td><td>436.00 <b>(+46.46%)</b></td><td>187.60 (-15.76%)</td><td>187.80 <b>(+404.66%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>304.60 (n/a)</td><td>273.66 (n/a)</td><td>297.70 (n/a)</td><td>222.70 (n/a)</td><td>37.21 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (-15.33%)</td><td>0.03 (-14.27%)</td><td>0.03 <b>(-26.37%)</b></td><td>0.02 (+1.76%)</td><td>0.01 (-8.79%)</td><td>529.60 (-1.73%)</td><td>381.46 (+15.47%)</td><td>400.80 <b>(+35.82%)</b></td><td>262.80 (+18.11%)</td><td>113.42 (-6.26%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.90 (n/a)</td><td>330.34 (n/a)</td><td>295.10 (n/a)</td><td>222.50 (n/a)</td><td>120.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 (+4.36%)</td><td>0.03 (-9.15%)</td><td>0.02 (+5.31%)</td><td>0.01 <b>(-33.99%)</b></td><td>0.01 (+14.93%)</td><td>775.20 <b>(+51.50%)</b></td><td>475.68 <b>(+20.62%)</b></td><td>451.00 (-5.05%)</td><td>219.80 (-4.18%)</td><td>233.64 <b>(+65.10%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.70 (n/a)</td><td>394.36 (n/a)</td><td>475.00 (n/a)</td><td>229.40 (n/a)</td><td>141.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 (+0.81%)</td><td>0.03 (-14.92%)</td><td>0.03 <b>(-20.32%)</b></td><td>0.02 <b>(-21.99%)</b></td><td>0.01 <b>(+21.14%)</b></td><td>595.90 <b>(+28.18%)</b></td><td>407.34 <b>(+24.97%)</b></td><td>414.60 <b>(+25.48%)</b></td><td>227.80 (-0.83%)</td><td>156.32 <b>(+60.28%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>464.90 (n/a)</td><td>325.96 (n/a)</td><td>330.40 (n/a)</td><td>229.70 (n/a)</td><td>97.53 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (+10.00%)</td><td>0.02 (+4.37%)</td><td>0.03 <b>(+25.87%)</b></td><td>0.01 <b>(-69.69%)</b></td><td>0.01 <b>(+115.73%)</b></td><td>1808.30 <b>(+229.92%)</b></td><td>667.50 <b>(+38.89%)</b></td><td>412.50 <b>(-20.57%)</b></td><td>307.10 (-9.09%)</td><td>639.61 <b>(+649.89%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>548.10 (n/a)</td><td>480.60 (n/a)</td><td>519.30 (n/a)</td><td>337.80 (n/a)</td><td>85.29 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 (-5.91%)</td><td>0.05 <b>(-21.01%)</b></td><td>0.04 <b>(-32.33%)</b></td><td>0.03 (-7.96%)</td><td>0.02 (+4.72%)</td><td>634.80 (+8.64%)</td><td>473.96 <b>(+28.15%)</b></td><td>494.10 <b>(+47.80%)</b></td><td>249.40 (+6.26%)</td><td>139.88 (+7.35%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>584.30 (n/a)</td><td>369.84 (n/a)</td><td>334.30 (n/a)</td><td>234.70 (n/a)</td><td>130.31 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (-15.23%)</td><td>0.05 <b>(-25.74%)</b></td><td>0.04 <b>(-46.73%)</b></td><td>0.03 (-6.55%)</td><td>0.02 <b>(-29.38%)</b></td><td>610.00 (+7.00%)</td><td>471.78 <b>(+28.87%)</b></td><td>517.20 <b>(+87.73%)</b></td><td>285.60 (+17.97%)</td><td>133.06 (-11.07%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>570.10 (n/a)</td><td>366.10 (n/a)</td><td>275.50 (n/a)</td><td>242.10 (n/a)</td><td>149.62 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 (+13.01%)</td><td>0.06 <b>(+20.04%)</b></td><td>0.07 <b>(+36.37%)</b></td><td>0.05 (+8.92%)</td><td>0.01 <b>(+31.73%)</b></td><td>428.70 (-8.20%)</td><td>341.20 (-15.83%)</td><td>301.80 <b>(-26.66%)</b></td><td>269.80 (-11.54%)</td><td>70.45 (+11.35%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>467.00 (n/a)</td><td>405.38 (n/a)</td><td>411.50 (n/a)</td><td>305.00 (n/a)</td><td>63.27 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 <b>(+21.51%)</b></td><td>0.06 (-18.69%)</td><td>0.06 <b>(-24.83%)</b></td><td>0.04 <b>(-38.79%)</b></td><td>0.03 <b>(+147.30%)</b></td><td>559.50 <b>(+63.36%)</b></td><td>399.12 <b>(+39.75%)</b></td><td>367.70 <b>(+33.03%)</b></td><td>199.80 (-17.71%)</td><td>156.64 <b>(+255.51%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>342.50 (n/a)</td><td>285.60 (n/a)</td><td>276.40 (n/a)</td><td>242.80 (n/a)</td><td>44.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.09 (-12.13%)</td><td>0.05 (-10.95%)</td><td>0.05 (+1.55%)</td><td>0.04 <b>(+42.35%)</b></td><td>0.02 <b>(-28.34%)</b></td><td>579.50 <b>(-29.75%)</b></td><td>449.86 (-0.08%)</td><td>436.10 (-1.54%)</td><td>240.20 (+13.84%)</td><td>137.70 <b>(-42.35%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>824.90 (n/a)</td><td>450.20 (n/a)</td><td>442.90 (n/a)</td><td>211.00 (n/a)</td><td>238.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 (+13.84%)</td><td>0.05 (+2.90%)</td><td>0.04 (+6.16%)</td><td>0.04 (-1.44%)</td><td>0.02 <b>(+27.16%)</b></td><td>591.60 (+1.46%)</td><td>478.96 (-0.85%)</td><td>513.20 (-5.80%)</td><td>266.90 (-12.15%)</td><td>124.45 (+6.19%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>583.10 (n/a)</td><td>483.08 (n/a)</td><td>544.80 (n/a)</td><td>303.80 (n/a)</td><td>117.20 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.90 (n/a)</td><td>416.98 (n/a)</td><td>395.00 (n/a)</td><td>291.40 (n/a)</td><td>100.41 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>582.70 (n/a)</td><td>402.18 (n/a)</td><td>422.80 (n/a)</td><td>274.00 (n/a)</td><td>125.56 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1020.90 (n/a)</td><td>566.34 (n/a)</td><td>510.10 (n/a)</td><td>310.60 (n/a)</td><td>269.94 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>465.00 (n/a)</td><td>355.52 (n/a)</td><td>306.00 (n/a)</td><td>292.20 (n/a)</td><td>81.70 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1939.10 (n/a)</td><td>694.96 (n/a)</td><td>399.60 (n/a)</td><td>261.20 (n/a)</td><td>704.66 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>616.10 (n/a)</td><td>343.22 (n/a)</td><td>284.10 (n/a)</td><td>234.30 (n/a)</td><td>154.50 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1950.50 (n/a)</td><td>756.32 (n/a)</td><td>510.80 (n/a)</td><td>290.10 (n/a)</td><td>674.63 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>600.50 (n/a)</td><td>418.24 (n/a)</td><td>468.50 (n/a)</td><td>201.30 (n/a)</td><td>172.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2442.90 (n/a)</td><td>850.82 (n/a)</td><td>513.70 (n/a)</td><td>207.20 (n/a)</td><td>902.62 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.22 <b>(+27.22%)</b></td><td>0.16 <b>(+22.21%)</b></td><td>0.16 <b>(+33.74%)</b></td><td>0.10 <b>(+25.98%)</b></td><td>0.05 <b>(+31.32%)</b></td><td>480.70 <b>(-20.61%)</b></td><td>345.72 (-17.06%)</td><td>305.10 <b>(-25.24%)</b></td><td>228.20 <b>(-21.39%)</b></td><td>118.01 (-10.87%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>605.50 (n/a)</td><td>416.84 (n/a)</td><td>408.10 (n/a)</td><td>290.30 (n/a)</td><td>132.41 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>576.00 (n/a)</td><td>421.74 (n/a)</td><td>419.70 (n/a)</td><td>281.20 (n/a)</td><td>117.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>525.10 (n/a)</td><td>462.70 (n/a)</td><td>495.20 (n/a)</td><td>333.20 (n/a)</td><td>76.09 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>443.70 (n/a)</td><td>369.44 (n/a)</td><td>432.30 (n/a)</td><td>245.40 (n/a)</td><td>95.39 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>365.10 (n/a)</td><td>277.82 (n/a)</td><td>272.30 (n/a)</td><td>229.10 (n/a)</td><td>52.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>476.70 (n/a)</td><td>375.92 (n/a)</td><td>383.10 (n/a)</td><td>267.60 (n/a)</td><td>79.66 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>431.50 (n/a)</td><td>319.82 (n/a)</td><td>281.70 (n/a)</td><td>217.70 (n/a)</td><td>93.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>581.60 (n/a)</td><td>387.42 (n/a)</td><td>300.60 (n/a)</td><td>265.20 (n/a)</td><td>146.39 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>608.00 (n/a)</td><td>451.22 (n/a)</td><td>432.40 (n/a)</td><td>299.10 (n/a)</td><td>121.31 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>494.20 (n/a)</td><td>408.98 (n/a)</td><td>460.40 (n/a)</td><td>302.00 (n/a)</td><td>96.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2464.80 (n/a)</td><td>877.66 (n/a)</td><td>545.70 (n/a)</td><td>255.80 (n/a)</td><td>898.74 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1896.80 (n/a)</td><td>768.20 (n/a)</td><td>501.70 (n/a)</td><td>385.00 (n/a)</td><td>634.94 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>540.20 (n/a)</td><td>437.58 (n/a)</td><td>435.70 (n/a)</td><td>279.20 (n/a)</td><td>101.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>566.40 (n/a)</td><td>394.92 (n/a)</td><td>391.20 (n/a)</td><td>257.20 (n/a)</td><td>136.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>3.32 <b>(+28.29%)</b></td><td>3.05 <b>(+30.94%)</b></td><td>2.92 <b>(+20.60%)</b></td><td>2.84 <b>(+61.02%)</b></td><td>0.24 <b>(-29.96%)</b></td><td>3693.20 <b>(-37.90%)</b></td><td>3448.64 <b>(-24.78%)</b></td><td>3594.10 (-17.09%)</td><td>3157.10 <b>(-22.05%)</b></td><td>259.68 <b>(-66.90%)</b></td><td>1360.41 <b>(+28.29%)</b></td><td>1251.22 <b>(+30.94%)</b></td><td>1194.99 <b>(+20.60%)</b></td><td>1162.95 <b>(+61.02%)</b></td><td>96.55 <b>(-29.96%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.59 (n/a)</td><td>2.33 (n/a)</td><td>2.42 (n/a)</td><td>1.76 (n/a)</td><td>0.34 (n/a)</td><td>5946.90 (n/a)</td><td>4584.96 (n/a)</td><td>4334.70 (n/a)</td><td>4050.30 (n/a)</td><td>784.43 (n/a)</td><td>1060.40 (n/a)</td><td>955.55 (n/a)</td><td>990.83 (n/a)</td><td>722.22 (n/a)</td><td>137.84 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>2.35 (-8.96%)</td><td>2.27 (-5.45%)</td><td>2.31 (+0.01%)</td><td>2.16 (-4.82%)</td><td>0.08 <b>(-46.33%)</b></td><td>10933.90 (+5.06%)</td><td>10385.58 (+5.54%)</td><td>10222.20 (-0.01%)</td><td>10034.10 (+9.85%)</td><td>386.43 <b>(-37.74%)</b></td><td>1337.61 (-8.96%)</td><td>1293.75 (-5.45%)</td><td>1313.00 (+0.01%)</td><td>1227.54 (-4.82%)</td><td>47.33 <b>(-46.33%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.58 (n/a)</td><td>2.41 (n/a)</td><td>2.31 (n/a)</td><td>2.27 (n/a)</td><td>0.15 (n/a)</td><td>10407.00 (n/a)</td><td>9840.86 (n/a)</td><td>10223.60 (n/a)</td><td>9134.70 (n/a)</td><td>620.71 (n/a)</td><td>1469.32 (n/a)</td><td>1368.33 (n/a)</td><td>1312.82 (n/a)</td><td>1289.68 (n/a)</td><td>88.18 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>2.81 (+11.54%)</td><td>2.53 (+9.03%)</td><td>2.60 (+9.94%)</td><td>2.15 (+7.69%)</td><td>0.24 <b>(+22.88%)</b></td><td>7809.10 (-7.14%)</td><td>6692.44 (-8.13%)</td><td>6452.90 (-9.04%)</td><td>5973.40 (-10.35%)</td><td>690.29 (+2.38%)</td><td>1438.03 (+11.54%)</td><td>1293.82 (+9.03%)</td><td>1331.18 (+9.94%)</td><td>1099.99 (+7.69%)</td><td>125.13 <b>(+22.88%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.52 (n/a)</td><td>2.32 (n/a)</td><td>2.36 (n/a)</td><td>2.00 (n/a)</td><td>0.20 (n/a)</td><td>8409.60 (n/a)</td><td>7284.94 (n/a)</td><td>7094.20 (n/a)</td><td>6662.70 (n/a)</td><td>674.28 (n/a)</td><td>1289.26 (n/a)</td><td>1186.66 (n/a)</td><td>1210.85 (n/a)</td><td>1021.45 (n/a)</td><td>101.83 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>1.03 (+5.73%)</td><td>0.72 (+11.62%)</td><td>0.65 (+3.29%)</td><td>0.44 (+6.73%)</td><td>0.22 (+7.37%)</td><td>1035.40 (-6.31%)</td><td>692.10 (-10.21%)</td><td>708.80 (-3.20%)</td><td>447.40 (-5.43%)</td><td>225.55 (-4.54%)</td><td>75.00 (+5.73%)</td><td>52.61 (+11.62%)</td><td>47.34 (+3.29%)</td><td>32.41 (+6.73%)</td><td>16.43 (+7.37%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.97 (n/a)</td><td>0.64 (n/a)</td><td>0.63 (n/a)</td><td>0.42 (n/a)</td><td>0.21 (n/a)</td><td>1105.10 (n/a)</td><td>770.78 (n/a)</td><td>732.20 (n/a)</td><td>473.10 (n/a)</td><td>236.28 (n/a)</td><td>70.93 (n/a)</td><td>47.13 (n/a)</td><td>45.83 (n/a)</td><td>30.36 (n/a)</td><td>15.30 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>1.38 (-12.33%)</td><td>0.99 (-11.60%)</td><td>1.00 (+11.21%)</td><td>0.37 <b>(-56.79%)</b></td><td>0.41 <b>(+21.44%)</b></td><td>1758.60 <b>(+131.39%)</b></td><td>829.24 <b>(+32.36%)</b></td><td>658.20 (-10.08%)</td><td>474.50 (+14.06%)</td><td>532.97 <b>(+219.73%)</b></td><td>141.42 (-12.33%)</td><td>101.14 (-11.60%)</td><td>101.96 (+11.21%)</td><td>38.16 <b>(-56.79%)</b></td><td>41.76 <b>(+21.44%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.58 (n/a)</td><td>1.12 (n/a)</td><td>0.90 (n/a)</td><td>0.86 (n/a)</td><td>0.34 (n/a)</td><td>760.00 (n/a)</td><td>626.52 (n/a)</td><td>732.00 (n/a)</td><td>416.00 (n/a)</td><td>166.70 (n/a)</td><td>161.31 (n/a)</td><td>114.41 (n/a)</td><td>91.68 (n/a)</td><td>88.30 (n/a)</td><td>34.39 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>1.50 <b>(+23.77%)</b></td><td>1.21 <b>(+23.58%)</b></td><td>1.24 <b>(+29.95%)</b></td><td>0.94 <b>(+23.34%)</b></td><td>0.24 <b>(+40.23%)</b></td><td>800.50 (-18.92%)</td><td>641.72 (-18.48%)</td><td>606.10 <b>(-23.04%)</b></td><td>501.30 (-19.20%)</td><td>127.05 (-6.88%)</td><td>167.34 <b>(+23.77%)</b></td><td>134.84 <b>(+23.58%)</b></td><td>138.40 <b>(+29.95%)</b></td><td>104.79 <b>(+23.34%)</b></td><td>26.17 <b>(+40.23%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.21 (n/a)</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td><td>0.76 (n/a)</td><td>0.17 (n/a)</td><td>987.30 (n/a)</td><td>787.24 (n/a)</td><td>787.60 (n/a)</td><td>620.40 (n/a)</td><td>136.44 (n/a)</td><td>135.21 (n/a)</td><td>109.11 (n/a)</td><td>106.51 (n/a)</td><td>84.96 (n/a)</td><td>18.66 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>1.56 (+8.27%)</td><td>0.96 (-17.49%)</td><td>0.88 <b>(-22.77%)</b></td><td>0.32 <b>(-63.40%)</b></td><td>0.52 <b>(+136.76%)</b></td><td>3240.20 <b>(+173.25%)</b></td><td>1507.62 <b>(+62.29%)</b></td><td>1188.50 <b>(+29.48%)</b></td><td>670.60 (-7.64%)</td><td>1051.39 <b>(+481.45%)</b></td><td>200.14 (+8.27%)</td><td>122.80 (-17.49%)</td><td>112.93 <b>(-22.77%)</b></td><td>41.42 <b>(-63.40%)</b></td><td>66.91 <b>(+136.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.44 (n/a)</td><td>1.16 (n/a)</td><td>1.14 (n/a)</td><td>0.88 (n/a)</td><td>0.22 (n/a)</td><td>1185.80 (n/a)</td><td>928.94 (n/a)</td><td>917.90 (n/a)</td><td>726.10 (n/a)</td><td>180.82 (n/a)</td><td>184.85 (n/a)</td><td>148.84 (n/a)</td><td>146.22 (n/a)</td><td>113.19 (n/a)</td><td>28.26 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>2.17 <b>(+31.36%)</b></td><td>1.57 (+10.73%)</td><td>1.65 (+19.47%)</td><td>1.09 (-6.53%)</td><td>0.42 <b>(+128.64%)</b></td><td>960.30 (+7.00%)</td><td>708.26 (-5.57%)</td><td>635.20 (-16.29%)</td><td>483.30 <b>(-23.88%)</b></td><td>190.72 <b>(+89.84%)</b></td><td>277.72 <b>(+31.36%)</b></td><td>200.93 (+10.73%)</td><td>211.30 (+19.47%)</td><td>139.77 (-6.53%)</td><td>54.16 <b>(+128.64%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.65 (n/a)</td><td>1.42 (n/a)</td><td>1.38 (n/a)</td><td>1.17 (n/a)</td><td>0.19 (n/a)</td><td>897.50 (n/a)</td><td>750.02 (n/a)</td><td>758.80 (n/a)</td><td>634.90 (n/a)</td><td>100.46 (n/a)</td><td>211.42 (n/a)</td><td>181.47 (n/a)</td><td>176.87 (n/a)</td><td>149.54 (n/a)</td><td>23.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>1.70 (-6.28%)</td><td>1.15 (-9.89%)</td><td>1.36 (-6.18%)</td><td>0.54 <b>(+23.74%)</b></td><td>0.55 (+3.77%)</td><td>1924.30 (-19.18%)</td><td>1167.02 (+9.83%)</td><td>768.60 (+6.59%)</td><td>615.10 (+6.71%)</td><td>659.86 (-12.03%)</td><td>218.22 (-6.28%)</td><td>146.64 (-9.89%)</td><td>174.63 (-6.18%)</td><td>69.75 <b>(+23.74%)</b></td><td>70.61 (+3.77%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.82 (n/a)</td><td>1.27 (n/a)</td><td>1.45 (n/a)</td><td>0.44 (n/a)</td><td>0.53 (n/a)</td><td>2381.10 (n/a)</td><td>1062.60 (n/a)</td><td>721.10 (n/a)</td><td>576.40 (n/a)</td><td>750.12 (n/a)</td><td>232.84 (n/a)</td><td>162.73 (n/a)</td><td>186.14 (n/a)</td><td>56.37 (n/a)</td><td>68.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>1.28 (-19.09%)</td><td>1.06 (+3.22%)</td><td>1.21 <b>(+26.77%)</b></td><td>0.44 (+2.73%)</td><td>0.35 (-19.07%)</td><td>2378.60 (-2.66%)</td><td>1164.32 (-5.81%)</td><td>868.90 <b>(-21.12%)</b></td><td>818.90 <b>(+23.59%)</b></td><td>679.33 (-3.57%)</td><td>163.90 (-19.09%)</td><td>136.15 (+3.22%)</td><td>154.47 <b>(+26.77%)</b></td><td>56.43 (+2.73%)</td><td>44.84 (-19.07%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.58 (n/a)</td><td>1.03 (n/a)</td><td>0.95 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>2443.50 (n/a)</td><td>1236.10 (n/a)</td><td>1101.50 (n/a)</td><td>662.60 (n/a)</td><td>704.49 (n/a)</td><td>202.57 (n/a)</td><td>131.90 (n/a)</td><td>121.85 (n/a)</td><td>54.93 (n/a)</td><td>55.40 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>1.70 (+7.03%)</td><td>1.25 (+14.43%)</td><td>1.49 <b>(+45.15%)</b></td><td>0.48 <b>(-33.65%)</b></td><td>0.50 <b>(+35.94%)</b></td><td>2194.70 <b>(+50.71%)</b></td><td>1046.58 (-0.83%)</td><td>701.50 <b>(-31.10%)</b></td><td>617.00 (-6.56%)</td><td>663.57 <b>(+91.21%)</b></td><td>217.54 (+7.03%)</td><td>159.53 (+14.43%)</td><td>191.33 <b>(+45.15%)</b></td><td>61.15 <b>(-33.65%)</b></td><td>64.46 <b>(+35.94%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.59 (n/a)</td><td>1.09 (n/a)</td><td>1.03 (n/a)</td><td>0.72 (n/a)</td><td>0.37 (n/a)</td><td>1456.20 (n/a)</td><td>1055.34 (n/a)</td><td>1018.20 (n/a)</td><td>660.30 (n/a)</td><td>347.04 (n/a)</td><td>203.25 (n/a)</td><td>139.41 (n/a)</td><td>131.81 (n/a)</td><td>92.17 (n/a)</td><td>47.42 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>1.64 (-0.36%)</td><td>1.41 (+11.13%)</td><td>1.55 <b>(+29.26%)</b></td><td>0.98 (+9.33%)</td><td>0.28 (-7.08%)</td><td>1067.00 (-8.54%)</td><td>770.24 (-10.84%)</td><td>675.60 <b>(-22.64%)</b></td><td>638.60 (+0.36%)</td><td>182.54 (-14.19%)</td><td>210.18 (-0.36%)</td><td>181.10 (+11.13%)</td><td>198.67 <b>(+29.26%)</b></td><td>125.79 (+9.33%)</td><td>36.40 (-7.08%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.65 (n/a)</td><td>1.27 (n/a)</td><td>1.20 (n/a)</td><td>0.90 (n/a)</td><td>0.31 (n/a)</td><td>1166.60 (n/a)</td><td>863.88 (n/a)</td><td>873.30 (n/a)</td><td>636.30 (n/a)</td><td>212.72 (n/a)</td><td>210.94 (n/a)</td><td>162.97 (n/a)</td><td>153.70 (n/a)</td><td>115.05 (n/a)</td><td>39.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.68 <b>(-30.07%)</b></td><td>0.52 (-18.46%)</td><td>0.50 (-13.48%)</td><td>0.39 <b>(-21.68%)</b></td><td>0.11 <b>(-45.65%)</b></td><td>918.20 <b>(+27.69%)</b></td><td>710.30 (+19.48%)</td><td>725.00 (+15.59%)</td><td>530.50 <b>(+42.99%)</b></td><td>141.53 (+0.29%)</td><td>31.63 <b>(-30.07%)</b></td><td>24.38 (-18.46%)</td><td>23.14 (-13.48%)</td><td>18.27 <b>(-21.68%)</b></td><td>4.89 <b>(-45.65%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.97 (n/a)</td><td>0.64 (n/a)</td><td>0.57 (n/a)</td><td>0.50 (n/a)</td><td>0.19 (n/a)</td><td>719.10 (n/a)</td><td>594.48 (n/a)</td><td>627.20 (n/a)</td><td>371.00 (n/a)</td><td>141.13 (n/a)</td><td>45.23 (n/a)</td><td>29.90 (n/a)</td><td>26.75 (n/a)</td><td>23.33 (n/a)</td><td>9.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>2.61 (-3.05%)</td><td>1.83 (-9.50%)</td><td>1.88 (+9.63%)</td><td>1.01 <b>(-26.94%)</b></td><td>0.58 (-7.29%)</td><td>4137.20 <b>(+36.88%)</b></td><td>2522.14 (+12.97%)</td><td>2235.40 (-8.79%)</td><td>1604.80 (+3.15%)</td><td>960.68 <b>(+47.59%)</b></td><td>669.10 (-3.05%)</td><td>468.50 (-9.50%)</td><td>480.34 (+9.63%)</td><td>259.53 <b>(-26.94%)</b></td><td>147.56 (-7.29%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.70 (n/a)</td><td>2.02 (n/a)</td><td>1.71 (n/a)</td><td>1.39 (n/a)</td><td>0.62 (n/a)</td><td>3022.50 (n/a)</td><td>2232.60 (n/a)</td><td>2450.80 (n/a)</td><td>1555.80 (n/a)</td><td>650.89 (n/a)</td><td>690.17 (n/a)</td><td>517.69 (n/a)</td><td>438.13 (n/a)</td><td>355.25 (n/a)</td><td>159.16 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>3.32 (+17.23%)</td><td>2.25 (-9.11%)</td><td>2.09 <b>(-23.61%)</b></td><td>1.23 <b>(-31.30%)</b></td><td>0.79 <b>(+73.28%)</b></td><td>2135.20 <b>(+45.56%)</b></td><td>1300.96 (+19.22%)</td><td>1255.40 <b>(+30.91%)</b></td><td>789.90 (-14.70%)</td><td>517.20 <b>(+121.79%)</b></td><td>679.64 (+17.23%)</td><td>461.61 (-9.11%)</td><td>427.66 <b>(-23.61%)</b></td><td>251.44 <b>(-31.30%)</b></td><td>162.21 <b>(+73.28%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.83 (n/a)</td><td>2.48 (n/a)</td><td>2.73 (n/a)</td><td>1.79 (n/a)</td><td>0.46 (n/a)</td><td>1466.90 (n/a)</td><td>1091.26 (n/a)</td><td>959.00 (n/a)</td><td>926.00 (n/a)</td><td>233.20 (n/a)</td><td>579.75 (n/a)</td><td>507.87 (n/a)</td><td>559.84 (n/a)</td><td>365.99 (n/a)</td><td>93.61 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>2.64 (-12.43%)</td><td>2.02 (-16.06%)</td><td>1.90 <b>(-23.38%)</b></td><td>1.70 (-12.56%)</td><td>0.38 (-16.65%)</td><td>4639.20 (+14.36%)</td><td>4000.68 (+18.68%)</td><td>4140.50 <b>(+30.52%)</b></td><td>2981.30 (+14.19%)</td><td>658.10 (+3.85%)</td><td>810.35 (-12.43%)</td><td>619.06 (-16.06%)</td><td>583.49 <b>(-23.38%)</b></td><td>520.77 (-12.56%)</td><td>116.22 (-16.65%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.01 (n/a)</td><td>2.40 (n/a)</td><td>2.48 (n/a)</td><td>1.94 (n/a)</td><td>0.45 (n/a)</td><td>4056.50 (n/a)</td><td>3370.94 (n/a)</td><td>3172.40 (n/a)</td><td>2610.80 (n/a)</td><td>633.70 (n/a)</td><td>925.35 (n/a)</td><td>737.51 (n/a)</td><td>761.54 (n/a)</td><td>595.57 (n/a)</td><td>139.45 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>627.20 (n/a)</td><td>461.48 (n/a)</td><td>525.70 (n/a)</td><td>288.10 (n/a)</td><td>145.56 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>590.10 (n/a)</td><td>388.28 (n/a)</td><td>281.20 (n/a)</td><td>260.60 (n/a)</td><td>161.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>417.90 (n/a)</td><td>284.88 (n/a)</td><td>283.70 (n/a)</td><td>190.20 (n/a)</td><td>83.62 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1074.90 (n/a)</td><td>471.84 (n/a)</td><td>304.60 (n/a)</td><td>277.10 (n/a)</td><td>341.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1909.70 (n/a)</td><td>718.54 (n/a)</td><td>466.50 (n/a)</td><td>269.50 (n/a)</td><td>672.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>563.20 (n/a)</td><td>443.84 (n/a)</td><td>438.60 (n/a)</td><td>307.80 (n/a)</td><td>93.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.70 (n/a)</td><td>325.00 (n/a)</td><td>305.20 (n/a)</td><td>241.40 (n/a)</td><td>104.53 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.30 (n/a)</td><td>361.96 (n/a)</td><td>292.50 (n/a)</td><td>217.00 (n/a)</td><td>144.41 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.70 (n/a)</td><td>368.02 (n/a)</td><td>372.70 (n/a)</td><td>238.60 (n/a)</td><td>116.95 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>528.70 (n/a)</td><td>463.20 (n/a)</td><td>485.40 (n/a)</td><td>362.80 (n/a)</td><td>67.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1911.10 (n/a)</td><td>653.98 (n/a)</td><td>320.20 (n/a)</td><td>244.00 (n/a)</td><td>712.55 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>951.40 (n/a)</td><td>601.98 (n/a)</td><td>612.60 (n/a)</td><td>292.80 (n/a)</td><td>237.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>660.90 (n/a)</td><td>489.72 (n/a)</td><td>483.80 (n/a)</td><td>265.90 (n/a)</td><td>145.34 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1849.50 (n/a)</td><td>674.00 (n/a)</td><td>486.60 (n/a)</td><td>229.20 (n/a)</td><td>671.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>480.60 (n/a)</td><td>304.42 (n/a)</td><td>260.20 (n/a)</td><td>222.00 (n/a)</td><td>103.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2132.10 (n/a)</td><td>735.48 (n/a)</td><td>469.20 (n/a)</td><td>208.90 (n/a)</td><td>788.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>532.00 (n/a)</td><td>377.50 (n/a)</td><td>340.00 (n/a)</td><td>287.00 (n/a)</td><td>101.97 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>562.90 (n/a)</td><td>429.14 (n/a)</td><td>514.00 (n/a)</td><td>223.30 (n/a)</td><td>149.47 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2467.50 (n/a)</td><td>895.68 (n/a)</td><td>642.10 (n/a)</td><td>300.70 (n/a)</td><td>900.47 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>556.20 (n/a)</td><td>424.10 (n/a)</td><td>496.10 (n/a)</td><td>191.90 (n/a)</td><td>154.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>476.00 (n/a)</td><td>343.30 (n/a)</td><td>298.10 (n/a)</td><td>238.60 (n/a)</td><td>96.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>547.80 (n/a)</td><td>418.82 (n/a)</td><td>431.90 (n/a)</td><td>239.80 (n/a)</td><td>128.55 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>533.70 (n/a)</td><td>481.16 (n/a)</td><td>493.40 (n/a)</td><td>425.80 (n/a)</td><td>47.09 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>699.90 (n/a)</td><td>429.50 (n/a)</td><td>373.80 (n/a)</td><td>245.30 (n/a)</td><td>176.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.71 (+14.68%)</td><td>0.47 (+10.83%)</td><td>0.43 (+1.34%)</td><td>0.24 (+1.92%)</td><td>0.18 <b>(+26.40%)</b></td><td>908.70 (-1.88%)</td><td>536.46 (-6.84%)</td><td>510.90 (-1.33%)</td><td>310.70 (-12.80%)</td><td>234.17 (+5.94%)</td><td>30.37 (+14.68%)</td><td>20.18 (+10.83%)</td><td>18.47 (+1.34%)</td><td>10.39 (+1.92%)</td><td>7.83 <b>(+26.40%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.62 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>926.10 (n/a)</td><td>575.86 (n/a)</td><td>517.80 (n/a)</td><td>356.30 (n/a)</td><td>221.03 (n/a)</td><td>26.49 (n/a)</td><td>18.21 (n/a)</td><td>18.23 (n/a)</td><td>10.19 (n/a)</td><td>6.20 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.52 (+16.92%)</td><td>0.40 (+3.05%)</td><td>0.39 (+3.63%)</td><td>0.27 (-11.37%)</td><td>0.10 <b>(+56.61%)</b></td><td>829.70 (+12.84%)</td><td>589.36 (+0.07%)</td><td>562.20 (-3.50%)</td><td>422.60 (-14.47%)</td><td>157.12 <b>(+56.03%)</b></td><td>22.33 (+16.92%)</td><td>16.89 (+3.05%)</td><td>16.79 (+3.63%)</td><td>11.37 (-11.37%)</td><td>4.19 <b>(+56.61%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.45 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.30 (n/a)</td><td>0.06 (n/a)</td><td>735.30 (n/a)</td><td>588.96 (n/a)</td><td>582.60 (n/a)</td><td>494.10 (n/a)</td><td>100.69 (n/a)</td><td>19.10 (n/a)</td><td>16.39 (n/a)</td><td>16.20 (n/a)</td><td>12.83 (n/a)</td><td>2.68 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.31 (+2.70%)</td><td>0.31 (+2.48%)</td><td>0.31 (+2.27%)</td><td>0.30 (+3.40%)</td><td>0.00 (-13.68%)</td><td>82923.50 (-3.29%)</td><td>82275.16 (-2.43%)</td><td>82430.60 (-2.22%)</td><td>80981.30 (-2.63%)</td><td>753.64 (-18.98%)</td><td>212.15 (+2.70%)</td><td>208.82 (+2.48%)</td><td>208.42 (+2.27%)</td><td>207.18 (+3.40%)</td><td>1.93 (-13.68%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.00 (n/a)</td><td>85744.90 (n/a)</td><td>84321.24 (n/a)</td><td>84304.60 (n/a)</td><td>83169.80 (n/a)</td><td>930.22 (n/a)</td><td>206.56 (n/a)</td><td>203.76 (n/a)</td><td>203.78 (n/a)</td><td>200.36 (n/a)</td><td>2.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>1.17 (+1.95%)</td><td>1.10 (-3.61%)</td><td>1.10 (-4.09%)</td><td>1.03 (-7.12%)</td><td>0.06 <b>(+256.46%)</b></td><td>24435.00 (+7.67%)</td><td>22954.46 (+4.00%)</td><td>22857.10 (+4.26%)</td><td>21467.90 (-1.92%)</td><td>1313.88 <b>(+276.99%)</b></td><td>800.26 (+1.95%)</td><td>750.40 (-3.61%)</td><td>751.62 (-4.09%)</td><td>703.08 (-7.12%)</td><td>42.92 <b>(+256.45%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>1.15 (n/a)</td><td>1.11 (n/a)</td><td>0.02 (n/a)</td><td>22694.80 (n/a)</td><td>22072.46 (n/a)</td><td>21922.20 (n/a)</td><td>21887.30 (n/a)</td><td>348.52 (n/a)</td><td>784.93 (n/a)</td><td>778.49 (n/a)</td><td>783.68 (n/a)</td><td>757.00 (n/a)</td><td>12.04 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.81 (+0.15%)</td><td>0.79 (-0.24%)</td><td>0.79 (-0.76%)</td><td>0.78 (+0.68%)</td><td>0.01 (-11.65%)</td><td>96408.60 (-0.67%)</td><td>95173.20 (+0.23%)</td><td>95205.60 (+0.76%)</td><td>93710.70 (-0.15%)</td><td>1193.25 (-12.19%)</td><td>733.32 (+0.15%)</td><td>722.14 (-0.24%)</td><td>721.80 (-0.76%)</td><td>712.79 (+0.68%)</td><td>9.07 (-11.65%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.78 (n/a)</td><td>0.01 (n/a)</td><td>97060.10 (n/a)</td><td>94952.76 (n/a)</td><td>94483.50 (n/a)</td><td>93851.40 (n/a)</td><td>1358.83 (n/a)</td><td>732.22 (n/a)</td><td>723.84 (n/a)</td><td>727.32 (n/a)</td><td>708.01 (n/a)</td><td>10.26 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.77 (-0.65%)</td><td>0.77 (+0.83%)</td><td>0.77 (-0.88%)</td><td>0.76 (+6.84%)</td><td>0.01 <b>(-80.54%)</b></td><td>99130.20 (-6.41%)</td><td>98260.80 (-0.93%)</td><td>98200.20 (+0.88%)</td><td>97585.80 (+0.65%)</td><td>696.47 <b>(-81.74%)</b></td><td>704.20 (-0.65%)</td><td>699.39 (+0.83%)</td><td>699.79 (-0.88%)</td><td>693.22 (+6.84%)</td><td>4.95 <b>(-80.54%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.78 (n/a)</td><td>0.71 (n/a)</td><td>0.03 (n/a)</td><td>105915.50 (n/a)</td><td>99182.16 (n/a)</td><td>97340.30 (n/a)</td><td>96950.90 (n/a)</td><td>3813.69 (n/a)</td><td>708.81 (n/a)</td><td>693.64 (n/a)</td><td>705.97 (n/a)</td><td>648.81 (n/a)</td><td>25.45 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.90 (+1.09%)</td><td>0.89 (+0.70%)</td><td>0.89 (+0.80%)</td><td>0.86 (-1.14%)</td><td>0.02 <b>(+57.48%)</b></td><td>88201.10 (+1.15%)</td><td>85301.36 (-0.68%)</td><td>84970.30 (-0.79%)</td><td>83936.10 (-1.08%)</td><td>1701.89 <b>(+58.11%)</b></td><td>818.71 (+1.09%)</td><td>805.86 (+0.70%)</td><td>808.75 (+0.80%)</td><td>779.12 (-1.14%)</td><td>15.75 <b>(+57.48%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>87195.40 (n/a)</td><td>85883.22 (n/a)</td><td>85646.90 (n/a)</td><td>84851.80 (n/a)</td><td>1076.36 (n/a)</td><td>809.88 (n/a)</td><td>800.25 (n/a)</td><td>802.36 (n/a)</td><td>788.11 (n/a)</td><td>10.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>4.00 <b>(-23.32%)</b></td><td>3.57 (+1.46%)</td><td>3.92 (+15.50%)</td><td>2.78 <b>(+30.03%)</b></td><td>0.57 <b>(-52.22%)</b></td><td>3204.40 <b>(-23.10%)</b></td><td>2555.12 (-8.12%)</td><td>2273.10 (-13.42%)</td><td>2226.70 <b>(+30.41%)</b></td><td>443.32 <b>(-53.24%)</b></td><td>241.11 <b>(-23.32%)</b></td><td>214.84 (+1.46%)</td><td>236.18 (+15.50%)</td><td>167.54 <b>(+30.03%)</b></td><td>34.08 <b>(-52.22%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>5.22 (n/a)</td><td>3.52 (n/a)</td><td>3.39 (n/a)</td><td>2.14 (n/a)</td><td>1.18 (n/a)</td><td>4166.70 (n/a)</td><td>2780.96 (n/a)</td><td>2625.50 (n/a)</td><td>1707.40 (n/a)</td><td>948.04 (n/a)</td><td>314.43 (n/a)</td><td>211.74 (n/a)</td><td>204.48 (n/a)</td><td>128.85 (n/a)</td><td>71.34 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>5.01 <b>(+52.52%)</b></td><td>3.31 (+11.03%)</td><td>2.27 <b>(-29.37%)</b></td><td>2.21 (-3.34%)</td><td>1.46 <b>(+236.38%)</b></td><td>4038.20 (+3.46%)</td><td>3110.62 (+1.93%)</td><td>3925.20 <b>(+41.59%)</b></td><td>1777.70 <b>(-34.44%)</b></td><td>1179.43 <b>(+130.99%)</b></td><td>302.01 <b>(+52.52%)</b></td><td>199.19 (+11.03%)</td><td>136.77 <b>(-29.37%)</b></td><td>132.95 (-3.34%)</td><td>87.76 <b>(+236.38%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.29 (n/a)</td><td>2.98 (n/a)</td><td>3.21 (n/a)</td><td>2.28 (n/a)</td><td>0.43 (n/a)</td><td>3903.20 (n/a)</td><td>3051.58 (n/a)</td><td>2772.30 (n/a)</td><td>2711.40 (n/a)</td><td>510.59 (n/a)</td><td>198.00 (n/a)</td><td>179.41 (n/a)</td><td>193.65 (n/a)</td><td>137.55 (n/a)</td><td>26.09 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>5.81 (-2.36%)</td><td>4.07 (-0.54%)</td><td>4.07 (+11.87%)</td><td>2.75 <b>(+24.34%)</b></td><td>1.12 <b>(-30.28%)</b></td><td>3237.30 (-19.57%)</td><td>2320.30 (-6.76%)</td><td>2192.20 (-10.61%)</td><td>1533.40 (+2.42%)</td><td>615.93 <b>(-40.27%)</b></td><td>350.12 (-2.36%)</td><td>245.12 (-0.54%)</td><td>244.90 (+11.87%)</td><td>165.84 <b>(+24.34%)</b></td><td>67.17 <b>(-30.28%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>5.95 (n/a)</td><td>4.09 (n/a)</td><td>3.63 (n/a)</td><td>2.21 (n/a)</td><td>1.60 (n/a)</td><td>4025.20 (n/a)</td><td>2488.54 (n/a)</td><td>2452.40 (n/a)</td><td>1497.10 (n/a)</td><td>1031.22 (n/a)</td><td>358.60 (n/a)</td><td>246.44 (n/a)</td><td>218.92 (n/a)</td><td>133.38 (n/a)</td><td>96.33 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>5.93 (-9.74%)</td><td>5.12 (-13.04%)</td><td>5.18 (-11.92%)</td><td>4.42 (-11.58%)</td><td>0.62 (+5.15%)</td><td>7881.30 (+13.09%)</td><td>6885.76 (+15.36%)</td><td>6737.00 (+13.53%)</td><td>5876.80 (+10.79%)</td><td>826.26 <b>(+31.49%)</b></td><td>365.42 (-9.74%)</td><td>315.51 (-13.04%)</td><td>318.76 (-11.92%)</td><td>272.48 (-11.58%)</td><td>37.97 (+5.15%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>6.57 (n/a)</td><td>5.89 (n/a)</td><td>5.88 (n/a)</td><td>5.00 (n/a)</td><td>0.59 (n/a)</td><td>6968.90 (n/a)</td><td>5968.70 (n/a)</td><td>5934.20 (n/a)</td><td>5304.50 (n/a)</td><td>628.39 (n/a)</td><td>404.84 (n/a)</td><td>362.82 (n/a)</td><td>361.88 (n/a)</td><td>308.15 (n/a)</td><td>36.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>6.00 (+16.26%)</td><td>5.11 (+10.99%)</td><td>5.06 (+7.99%)</td><td>4.31 (+16.80%)</td><td>0.64 (+13.19%)</td><td>8091.80 (-14.39%)</td><td>6915.36 (-10.00%)</td><td>6887.00 (-7.40%)</td><td>5814.60 (-13.99%)</td><td>863.09 (-18.19%)</td><td>369.32 (+16.26%)</td><td>314.45 (+10.99%)</td><td>311.82 (+7.99%)</td><td>265.39 (+16.80%)</td><td>39.43 (+13.19%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>5.16 (n/a)</td><td>4.60 (n/a)</td><td>4.69 (n/a)</td><td>3.69 (n/a)</td><td>0.57 (n/a)</td><td>9451.60 (n/a)</td><td>7683.32 (n/a)</td><td>7437.30 (n/a)</td><td>6760.20 (n/a)</td><td>1054.96 (n/a)</td><td>317.67 (n/a)</td><td>283.31 (n/a)</td><td>288.75 (n/a)</td><td>227.21 (n/a)</td><td>34.83 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>6.74 (-6.50%)</td><td>5.44 (-6.70%)</td><td>4.88 (-3.31%)</td><td>4.72 (-5.87%)</td><td>0.89 (-19.70%)</td><td>7393.30 (+6.24%)</td><td>6538.98 (+6.39%)</td><td>7150.20 (+3.43%)</td><td>5174.40 (+6.95%)</td><td>990.38 (-9.38%)</td><td>415.02 (-6.50%)</td><td>335.07 (-6.70%)</td><td>300.34 (-3.31%)</td><td>290.46 (-5.88%)</td><td>55.06 (-19.70%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>7.21 (n/a)</td><td>5.83 (n/a)</td><td>5.04 (n/a)</td><td>5.01 (n/a)</td><td>1.11 (n/a)</td><td>6958.90 (n/a)</td><td>6146.46 (n/a)</td><td>6913.30 (n/a)</td><td>4838.30 (n/a)</td><td>1092.94 (n/a)</td><td>443.85 (n/a)</td><td>359.14 (n/a)</td><td>310.63 (n/a)</td><td>308.60 (n/a)</td><td>68.56 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.78 (-1.71%)</td><td>0.76 (-2.53%)</td><td>0.76 (-3.42%)</td><td>0.75 (-2.49%)</td><td>0.01 (+6.48%)</td><td>101200.90 (+2.55%)</td><td>99275.14 (+2.59%)</td><td>99941.20 (+3.55%)</td><td>96710.10 (+1.74%)</td><td>1729.77 (+10.89%)</td><td>710.57 (-1.71%)</td><td>692.38 (-2.53%)</td><td>687.60 (-3.42%)</td><td>679.04 (-2.49%)</td><td>12.16 (+6.48%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>98685.70 (n/a)</td><td>96764.42 (n/a)</td><td>96519.30 (n/a)</td><td>95057.70 (n/a)</td><td>1559.85 (n/a)</td><td>722.92 (n/a)</td><td>710.32 (n/a)</td><td>711.98 (n/a)</td><td>696.35 (n/a)</td><td>11.42 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.76 (-1.55%)</td><td>0.75 (-2.96%)</td><td>0.75 (-1.82%)</td><td>0.72 (-5.71%)</td><td>0.02 <b>(+202.16%)</b></td><td>105076.80 (+6.06%)</td><td>101311.96 (+3.09%)</td><td>100313.40 (+1.85%)</td><td>98708.00 (+1.57%)</td><td>2485.35 <b>(+226.26%)</b></td><td>696.19 (-1.55%)</td><td>678.62 (-2.96%)</td><td>685.05 (-1.82%)</td><td>653.99 (-5.71%)</td><td>16.43 <b>(+202.16%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99076.60 (n/a)</td><td>98275.28 (n/a)</td><td>98489.10 (n/a)</td><td>97182.00 (n/a)</td><td>761.76 (n/a)</td><td>707.12 (n/a)</td><td>699.29 (n/a)</td><td>697.74 (n/a)</td><td>693.60 (n/a)</td><td>5.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.90 (+0.78%)</td><td>0.89 (+1.50%)</td><td>0.89 (+2.15%)</td><td>0.89 (+1.49%)</td><td>0.01 <b>(-43.86%)</b></td><td>85108.70 (-1.47%)</td><td>84428.08 (-1.48%)</td><td>84384.20 (-2.10%)</td><td>83753.40 (-0.77%)</td><td>482.08 <b>(-45.17%)</b></td><td>820.50 (+0.78%)</td><td>813.96 (+1.50%)</td><td>814.36 (+2.15%)</td><td>807.43 (+1.49%)</td><td>4.65 <b>(-43.86%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>86379.00 (n/a)</td><td>85697.20 (n/a)</td><td>86198.30 (n/a)</td><td>84403.10 (n/a)</td><td>879.22 (n/a)</td><td>814.18 (n/a)</td><td>801.96 (n/a)</td><td>797.23 (n/a)</td><td>795.56 (n/a)</td><td>8.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>3.83 (+19.98%)</td><td>2.95 <b>(+55.23%)</b></td><td>3.20 <b>(+97.88%)</b></td><td>1.94 <b>(+40.31%)</b></td><td>0.87 (+18.71%)</td><td>4152.00 <b>(-28.73%)</b></td><td>2956.28 <b>(-36.02%)</b></td><td>2515.80 <b>(-49.46%)</b></td><td>2107.00 (-16.65%)</td><td>948.21 <b>(-23.41%)</b></td><td>1003.29 (+19.98%)</td><td>772.99 <b>(+55.23%)</b></td><td>840.26 <b>(+97.88%)</b></td><td>509.13 <b>(+40.31%)</b></td><td>227.37 (+18.71%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.19 (n/a)</td><td>1.90 (n/a)</td><td>1.62 (n/a)</td><td>1.38 (n/a)</td><td>0.73 (n/a)</td><td>5825.80 (n/a)</td><td>4620.38 (n/a)</td><td>4978.30 (n/a)</td><td>2527.90 (n/a)</td><td>1238.01 (n/a)</td><td>836.24 (n/a)</td><td>497.95 (n/a)</td><td>424.62 (n/a)</td><td>362.85 (n/a)</td><td>191.53 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.22 (+6.10%)</td><td>0.19 (-1.80%)</td><td>0.20 (+0.83%)</td><td>0.16 (-14.61%)</td><td>0.02 <b>(+116.90%)</b></td><td>7979.10 (+17.10%)</td><td>6629.70 (+2.95%)</td><td>6363.30 (-0.82%)</td><td>5592.30 (-5.75%)</td><td>882.62 <b>(+140.42%)</b></td><td>12.00 (+6.10%)</td><td>10.26 (-1.80%)</td><td>10.55 (+0.83%)</td><td>8.41 (-14.61%)</td><td>1.31 <b>(+116.90%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>6813.70 (n/a)</td><td>6439.44 (n/a)</td><td>6416.00 (n/a)</td><td>5933.20 (n/a)</td><td>367.11 (n/a)</td><td>11.31 (n/a)</td><td>10.45 (n/a)</td><td>10.46 (n/a)</td><td>9.85 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>3.76 (n/a)</td><td>3.56 (n/a)</td><td>3.65 (n/a)</td><td>3.07 (n/a)</td><td>0.28 (n/a)</td><td>3.76 (n/a)</td><td>3.56 (n/a)</td><td>3.65 (n/a)</td><td>3.07 (n/a)</td><td>0.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>6.60 (-6.17%)</td><td>5.53 (-10.32%)</td><td>5.42 (-6.27%)</td><td>4.74 (-15.36%)</td><td>0.83 <b>(+25.66%)</b></td><td>6.60 (-6.17%)</td><td>5.53 (-10.32%)</td><td>5.42 (-6.27%)</td><td>4.74 (-15.36%)</td><td>0.83 <b>(+25.66%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>7.04 (n/a)</td><td>6.16 (n/a)</td><td>5.78 (n/a)</td><td>5.60 (n/a)</td><td>0.66 (n/a)</td><td>7.03 (n/a)</td><td>6.16 (n/a)</td><td>5.78 (n/a)</td><td>5.60 (n/a)</td><td>0.66 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>13.71 (-1.17%)</td><td>10.96 (-0.22%)</td><td>11.25 (+17.56%)</td><td>8.41 (+0.05%)</td><td>2.41 (-7.41%)</td><td>13.71 (-1.17%)</td><td>10.95 (-0.22%)</td><td>11.24 (+17.56%)</td><td>8.40 (+0.05%)</td><td>2.41 (-7.41%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>13.88 (n/a)</td><td>10.98 (n/a)</td><td>9.57 (n/a)</td><td>8.40 (n/a)</td><td>2.60 (n/a)</td><td>13.87 (n/a)</td><td>10.97 (n/a)</td><td>9.56 (n/a)</td><td>8.40 (n/a)</td><td>2.60 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>3.84 (n/a)</td><td>3.68 (n/a)</td><td>3.70 (n/a)</td><td>3.42 (n/a)</td><td>0.16 (n/a)</td><td>3.83 (n/a)</td><td>3.68 (n/a)</td><td>3.69 (n/a)</td><td>3.42 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>6.74 (-5.17%)</td><td>5.95 (-8.53%)</td><td>5.79 (-15.81%)</td><td>4.70 (-5.64%)</td><td>0.85 (-5.08%)</td><td>6.74 (-5.17%)</td><td>5.95 (-8.53%)</td><td>5.78 (-15.81%)</td><td>4.70 (-5.64%)</td><td>0.85 (-5.08%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>7.11 (n/a)</td><td>6.50 (n/a)</td><td>6.88 (n/a)</td><td>4.98 (n/a)</td><td>0.89 (n/a)</td><td>7.11 (n/a)</td><td>6.50 (n/a)</td><td>6.87 (n/a)</td><td>4.98 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>9.96 <b>(-28.98%)</b></td><td>8.53 <b>(-20.09%)</b></td><td>8.52 (-12.37%)</td><td>7.26 (-4.45%)</td><td>0.96 <b>(-68.23%)</b></td><td>9.96 <b>(-28.98%)</b></td><td>8.52 <b>(-20.09%)</b></td><td>8.52 (-12.37%)</td><td>7.26 (-4.45%)</td><td>0.96 <b>(-68.23%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>14.03 (n/a)</td><td>10.67 (n/a)</td><td>9.72 (n/a)</td><td>7.60 (n/a)</td><td>3.04 (n/a)</td><td>14.02 (n/a)</td><td>10.67 (n/a)</td><td>9.72 (n/a)</td><td>7.60 (n/a)</td><td>3.03 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>3.12 (-5.05%)</td><td>2.54 (+12.17%)</td><td>2.85 (+15.41%)</td><td>1.20 (+15.23%)</td><td>0.77 (-14.41%)</td><td>3.11 (-5.05%)</td><td>2.53 (+12.17%)</td><td>2.84 (+15.41%)</td><td>1.20 (+15.23%)</td><td>0.77 (-14.41%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.28 (n/a)</td><td>2.26 (n/a)</td><td>2.47 (n/a)</td><td>1.04 (n/a)</td><td>0.90 (n/a)</td><td>3.28 (n/a)</td><td>2.26 (n/a)</td><td>2.46 (n/a)</td><td>1.04 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.52 <b>(+45.54%)</b></td><td>0.28 <b>(+55.57%)</b></td><td>0.31 <b>(+297.47%)</b></td><td>0.08 (+4.16%)</td><td>0.20 <b>(+38.50%)</b></td><td>0.51 <b>(+45.54%)</b></td><td>0.28 <b>(+55.57%)</b></td><td>0.31 <b>(+297.47%)</b></td><td>0.08 (+4.16%)</td><td>0.20 <b>(+38.50%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.36 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.14 (n/a)</td><td>0.35 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.70 (-3.69%)</td><td>0.48 <b>(+33.40%)</b></td><td>0.56 <b>(+87.18%)</b></td><td>0.08 <b>(-28.26%)</b></td><td>0.25 (+6.64%)</td><td>0.70 (-3.69%)</td><td>0.48 <b>(+33.40%)</b></td><td>0.55 <b>(+87.18%)</b></td><td>0.08 <b>(-28.26%)</b></td><td>0.24 (+6.64%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.73 (n/a)</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.11 (n/a)</td><td>0.23 (n/a)</td><td>0.72 (n/a)</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.11 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>2.32 (+1.07%)</td><td>1.31 (+19.49%)</td><td>1.44 <b>(+94.04%)</b></td><td>0.44 (+4.65%)</td><td>0.83 (+1.88%)</td><td>2.28 (+1.07%)</td><td>1.29 (+19.49%)</td><td>1.42 <b>(+94.04%)</b></td><td>0.43 (+4.65%)</td><td>0.82 (+1.88%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.29 (n/a)</td><td>1.09 (n/a)</td><td>0.74 (n/a)</td><td>0.42 (n/a)</td><td>0.82 (n/a)</td><td>2.25 (n/a)</td><td>1.08 (n/a)</td><td>0.73 (n/a)</td><td>0.41 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>426.30 (n/a)</td><td>335.40 (n/a)</td><td>299.80 (n/a)</td><td>243.10 (n/a)</td><td>79.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>587.00 (n/a)</td><td>378.10 (n/a)</td><td>265.30 (n/a)</td><td>250.70 (n/a)</td><td>164.33 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>579.80 (n/a)</td><td>321.14 (n/a)</td><td>267.90 (n/a)</td><td>206.70 (n/a)</td><td>148.85 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1621.70 (n/a)</td><td>574.66 (n/a)</td><td>319.20 (n/a)</td><td>202.70 (n/a)</td><td>592.23 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.90 (n/a)</td><td>396.02 (n/a)</td><td>419.70 (n/a)</td><td>198.40 (n/a)</td><td>142.91 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>568.80 (n/a)</td><td>431.66 (n/a)</td><td>491.10 (n/a)</td><td>258.00 (n/a)</td><td>130.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1906.80 (n/a)</td><td>723.10 (n/a)</td><td>507.90 (n/a)</td><td>252.70 (n/a)</td><td>670.57 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.30 (n/a)</td><td>334.82 (n/a)</td><td>299.20 (n/a)</td><td>196.20 (n/a)</td><td>134.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>440.90 (n/a)</td><td>341.80 (n/a)</td><td>324.30 (n/a)</td><td>267.30 (n/a)</td><td>69.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2060.60 (n/a)</td><td>790.02 (n/a)</td><td>531.80 (n/a)</td><td>281.00 (n/a)</td><td>718.88 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.50 (n/a)</td><td>422.10 (n/a)</td><td>419.80 (n/a)</td><td>213.20 (n/a)</td><td>135.74 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.90 (n/a)</td><td>481.50 (n/a)</td><td>553.30 (n/a)</td><td>281.60 (n/a)</td><td>150.09 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>532.70 (n/a)</td><td>393.92 (n/a)</td><td>409.00 (n/a)</td><td>245.60 (n/a)</td><td>127.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>530.80 (n/a)</td><td>409.24 (n/a)</td><td>409.70 (n/a)</td><td>283.60 (n/a)</td><td>90.96 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2039.50 (n/a)</td><td>672.76 (n/a)</td><td>301.10 (n/a)</td><td>266.50 (n/a)</td><td>768.26 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1073.80 (n/a)</td><td>622.92 (n/a)</td><td>534.20 (n/a)</td><td>475.90 (n/a)</td><td>254.30 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1003.30 (n/a)</td><td>519.10 (n/a)</td><td>453.20 (n/a)</td><td>295.30 (n/a)</td><td>285.21 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1029.30 (n/a)</td><td>660.40 (n/a)</td><td>627.80 (n/a)</td><td>472.90 (n/a)</td><td>227.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>699.90 (n/a)</td><td>394.10 (n/a)</td><td>323.70 (n/a)</td><td>299.60 (n/a)</td><td>171.28 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>613.60 (n/a)</td><td>394.20 (n/a)</td><td>362.30 (n/a)</td><td>247.50 (n/a)</td><td>154.26 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>483.50 (n/a)</td><td>336.20 (n/a)</td><td>300.00 (n/a)</td><td>285.70 (n/a)</td><td>82.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>773.80 (n/a)</td><td>505.52 (n/a)</td><td>485.70 (n/a)</td><td>294.90 (n/a)</td><td>172.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>327.60 (n/a)</td><td>296.24 (n/a)</td><td>292.60 (n/a)</td><td>265.40 (n/a)</td><td>23.67 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>705.40 (n/a)</td><td>467.66 (n/a)</td><td>494.80 (n/a)</td><td>285.70 (n/a)</td><td>167.83 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(+54.59%)</b></td><td>0.01 (+18.75%)</td><td>0.01 (+7.35%)</td><td>0.01 (-4.51%)</td><td>0.01 <b>(+124.03%)</b></td><td>468.10 (+4.74%)</td><td>334.78 (-7.64%)</td><td>342.60 (-6.85%)</td><td>176.20 <b>(-35.29%)</b></td><td>125.04 <b>(+54.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>446.90 (n/a)</td><td>362.48 (n/a)</td><td>367.80 (n/a)</td><td>272.30 (n/a)</td><td>80.81 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(+31.77%)</b></td><td>0.01 <b>(+21.54%)</b></td><td>0.01 <b>(+28.50%)</b></td><td>0.00 <b>(-34.19%)</b></td><td>0.01 <b>(+64.29%)</b></td><td>962.10 <b>(+51.94%)</b></td><td>464.02 (-2.98%)</td><td>436.20 <b>(-22.18%)</b></td><td>208.30 <b>(-24.09%)</b></td><td>295.93 <b>(+94.23%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>633.20 (n/a)</td><td>478.28 (n/a)</td><td>560.50 (n/a)</td><td>274.40 (n/a)</td><td>152.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (-3.56%)</td><td>0.01 (-11.23%)</td><td>0.01 <b>(-28.73%)</b></td><td>0.01 <b>(+58.24%)</b></td><td>0.00 <b>(-32.62%)</b></td><td>504.00 <b>(-36.80%)</b></td><td>382.76 (-4.12%)</td><td>408.40 <b>(+40.30%)</b></td><td>222.60 (+3.68%)</td><td>104.72 <b>(-57.09%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>797.50 (n/a)</td><td>399.20 (n/a)</td><td>291.10 (n/a)</td><td>214.70 (n/a)</td><td>244.03 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 (+9.77%)</td><td>0.01 (-2.72%)</td><td>0.01 (-10.74%)</td><td>0.00 <b>(-41.07%)</b></td><td>0.00 <b>(+54.51%)</b></td><td>1294.90 <b>(+69.69%)</b></td><td>608.88 <b>(+25.75%)</b></td><td>529.10 (+12.03%)</td><td>276.40 (-8.90%)</td><td>411.97 <b>(+131.29%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>763.10 (n/a)</td><td>484.18 (n/a)</td><td>472.30 (n/a)</td><td>303.40 (n/a)</td><td>178.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(-32.47%)</b></td><td>0.01 <b>(-31.70%)</b></td><td>0.01 <b>(-38.34%)</b></td><td>0.01 <b>(-29.53%)</b></td><td>0.00 <b>(-30.28%)</b></td><td>535.70 <b>(+41.91%)</b></td><td>405.54 <b>(+46.95%)</b></td><td>447.00 <b>(+62.19%)</b></td><td>249.50 <b>(+48.07%)</b></td><td>115.08 <b>(+48.65%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>377.50 (n/a)</td><td>275.98 (n/a)</td><td>275.60 (n/a)</td><td>168.50 (n/a)</td><td>77.41 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 <b>(-28.08%)</b></td><td>0.01 (-9.61%)</td><td>0.01 (+0.73%)</td><td>0.01 (-16.09%)</td><td>0.00 <b>(-41.87%)</b></td><td>664.00 (+19.17%)</td><td>477.68 (+8.03%)</td><td>444.90 (-0.74%)</td><td>408.70 <b>(+39.01%)</b></td><td>106.44 (-3.33%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>557.20 (n/a)</td><td>442.16 (n/a)</td><td>448.20 (n/a)</td><td>294.00 (n/a)</td><td>110.10 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (-1.19%)</td><td>0.03 (+11.93%)</td><td>0.03 (+10.66%)</td><td>0.02 <b>(+27.84%)</b></td><td>0.01 <b>(-20.64%)</b></td><td>482.60 <b>(-21.77%)</b></td><td>294.76 (-16.13%)</td><td>243.80 (-9.64%)</td><td>229.00 (+1.19%)</td><td>106.65 <b>(-34.75%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>616.90 (n/a)</td><td>351.44 (n/a)</td><td>269.80 (n/a)</td><td>226.30 (n/a)</td><td>163.46 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(-37.17%)</b></td><td>0.02 <b>(-27.03%)</b></td><td>0.02 <b>(-26.15%)</b></td><td>0.02 (-4.81%)</td><td>0.00 <b>(-72.85%)</b></td><td>542.60 (+5.05%)</td><td>502.06 <b>(+30.24%)</b></td><td>521.80 <b>(+35.39%)</b></td><td>433.10 <b>(+59.17%)</b></td><td>47.69 <b>(-53.64%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.50 (n/a)</td><td>385.50 (n/a)</td><td>385.40 (n/a)</td><td>272.10 (n/a)</td><td>102.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (+12.58%)</td><td>0.02 (+8.44%)</td><td>0.03 <b>(+30.72%)</b></td><td>0.02 (-8.93%)</td><td>0.01 <b>(+65.25%)</b></td><td>529.60 (+9.81%)</td><td>372.14 (-2.65%)</td><td>295.40 <b>(-23.51%)</b></td><td>255.10 (-11.18%)</td><td>125.63 <b>(+67.68%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>482.30 (n/a)</td><td>382.28 (n/a)</td><td>386.20 (n/a)</td><td>287.20 (n/a)</td><td>74.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (+15.29%)</td><td>0.03 (+12.05%)</td><td>0.03 (+5.80%)</td><td>0.02 <b>(+24.67%)</b></td><td>0.01 (+18.40%)</td><td>454.90 (-19.78%)</td><td>319.50 (-11.19%)</td><td>284.10 (-5.49%)</td><td>238.20 (-13.26%)</td><td>93.81 <b>(-21.89%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.10 (n/a)</td><td>359.74 (n/a)</td><td>300.60 (n/a)</td><td>274.60 (n/a)</td><td>120.10 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (+0.02%)</td><td>0.02 (+12.86%)</td><td>0.02 (+13.83%)</td><td>0.01 (-18.55%)</td><td>0.01 <b>(+26.24%)</b></td><td>696.50 <b>(+22.77%)</b></td><td>431.14 (-3.28%)</td><td>379.20 (-12.16%)</td><td>234.10 (+0.00%)</td><td>207.89 <b>(+52.65%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.30 (n/a)</td><td>445.74 (n/a)</td><td>431.70 (n/a)</td><td>234.10 (n/a)</td><td>136.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (-15.59%)</td><td>0.02 <b>(-24.56%)</b></td><td>0.02 <b>(-34.49%)</b></td><td>0.01 (+1.82%)</td><td>0.01 <b>(-31.68%)</b></td><td>581.10 (-1.79%)</td><td>451.46 <b>(+25.60%)</b></td><td>460.20 <b>(+52.64%)</b></td><td>273.80 (+18.48%)</td><td>124.81 (-18.24%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.70 (n/a)</td><td>359.44 (n/a)</td><td>301.50 (n/a)</td><td>231.10 (n/a)</td><td>152.65 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (+1.35%)</td><td>0.03 (+19.17%)</td><td>0.03 (+15.68%)</td><td>0.01 <b>(+116.04%)</b></td><td>0.01 <b>(-23.25%)</b></td><td>559.40 <b>(-53.71%)</b></td><td>351.24 <b>(-33.21%)</b></td><td>285.60 (-13.56%)</td><td>247.70 (-1.31%)</td><td>135.04 <b>(-66.32%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1208.50 (n/a)</td><td>525.86 (n/a)</td><td>330.40 (n/a)</td><td>251.00 (n/a)</td><td>400.91 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(-30.18%)</b></td><td>0.02 (-14.70%)</td><td>0.02 <b>(-25.09%)</b></td><td>0.02 <b>(+39.14%)</b></td><td>0.00 <b>(-78.90%)</b></td><td>496.00 <b>(-28.14%)</b></td><td>436.64 (+3.73%)</td><td>427.00 <b>(+33.48%)</b></td><td>388.70 <b>(+43.22%)</b></td><td>39.65 <b>(-78.04%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>690.20 (n/a)</td><td>420.92 (n/a)</td><td>319.90 (n/a)</td><td>271.40 (n/a)</td><td>180.59 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (-1.26%)</td><td>0.05 (-14.04%)</td><td>0.05 <b>(-24.34%)</b></td><td>0.04 (-0.77%)</td><td>0.01 (-6.24%)</td><td>383.70 (+0.79%)</td><td>321.54 (+15.75%)</td><td>331.30 <b>(+32.15%)</b></td><td>236.80 (+1.24%)</td><td>53.03 (-10.77%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>380.70 (n/a)</td><td>277.80 (n/a)</td><td>250.70 (n/a)</td><td>233.90 (n/a)</td><td>59.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (-3.14%)</td><td>0.05 (-7.00%)</td><td>0.06 (+2.71%)</td><td>0.03 (-10.69%)</td><td>0.02 (+11.64%)</td><td>569.70 (+11.97%)</td><td>343.16 (+10.28%)</td><td>266.20 (-2.63%)</td><td>245.10 (+3.24%)</td><td>136.89 <b>(+22.15%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>508.80 (n/a)</td><td>311.18 (n/a)</td><td>273.40 (n/a)</td><td>237.40 (n/a)</td><td>112.08 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (+1.17%)</td><td>0.04 (+3.82%)</td><td>0.03 (-12.64%)</td><td>0.03 (+7.51%)</td><td>0.02 (+3.18%)</td><td>619.30 (-6.98%)</td><td>424.38 (-4.67%)</td><td>488.20 (+14.47%)</td><td>246.00 (-1.17%)</td><td>163.69 (-11.25%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>665.80 (n/a)</td><td>445.18 (n/a)</td><td>426.50 (n/a)</td><td>248.90 (n/a)</td><td>184.45 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (+0.82%)</td><td>0.04 (+2.06%)</td><td>0.03 (-15.71%)</td><td>0.03 <b>(+89.96%)</b></td><td>0.01 (-18.11%)</td><td>559.90 <b>(-47.35%)</b></td><td>438.20 (-14.39%)</td><td>473.00 (+18.64%)</td><td>263.30 (-0.79%)</td><td>123.49 <b>(-60.97%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1063.50 (n/a)</td><td>511.84 (n/a)</td><td>398.70 (n/a)</td><td>265.40 (n/a)</td><td>316.41 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (-13.42%)</td><td>0.04 (-7.74%)</td><td>0.04 (+4.53%)</td><td>0.03 (-12.86%)</td><td>0.01 <b>(-21.04%)</b></td><td>595.90 (+14.77%)</td><td>434.92 (+6.40%)</td><td>464.00 (-4.33%)</td><td>282.80 (+15.52%)</td><td>124.84 (+0.54%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>519.20 (n/a)</td><td>408.76 (n/a)</td><td>485.00 (n/a)</td><td>244.80 (n/a)</td><td>124.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 <b>(-29.21%)</b></td><td>0.04 (-5.07%)</td><td>0.04 (+3.20%)</td><td>0.03 <b>(+20.23%)</b></td><td>0.01 <b>(-62.19%)</b></td><td>518.50 (-16.81%)</td><td>454.78 (-1.82%)</td><td>457.30 (-3.11%)</td><td>363.50 <b>(+41.22%)</b></td><td>63.72 <b>(-52.04%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>623.30 (n/a)</td><td>463.20 (n/a)</td><td>472.00 (n/a)</td><td>257.40 (n/a)</td><td>132.85 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.13 (-11.35%)</td><td>0.09 (+2.51%)</td><td>0.10 <b>(+56.92%)</b></td><td>0.06 (-6.45%)</td><td>0.03 <b>(-21.42%)</b></td><td>561.10 (+6.90%)</td><td>386.92 (-5.56%)</td><td>314.70 <b>(-36.27%)</b></td><td>252.50 (+12.82%)</td><td>136.02 (-6.36%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>524.90 (n/a)</td><td>409.68 (n/a)</td><td>493.80 (n/a)</td><td>223.80 (n/a)</td><td>145.26 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.13 (-11.31%)</td><td>0.08 (+0.25%)</td><td>0.07 (+1.84%)</td><td>0.04 <b>(-22.31%)</b></td><td>0.03 (-4.28%)</td><td>750.10 <b>(+28.73%)</b></td><td>449.96 (+2.89%)</td><td>452.00 (-1.80%)</td><td>262.10 (+12.78%)</td><td>192.47 <b>(+39.84%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>582.70 (n/a)</td><td>437.34 (n/a)</td><td>460.30 (n/a)</td><td>232.40 (n/a)</td><td>137.63 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (+13.07%)</td><td>0.10 <b>(+78.62%)</b></td><td>0.12 <b>(+92.00%)</b></td><td>0.06 <b>(+373.26%)</b></td><td>0.04 (-11.12%)</td><td>512.00 <b>(-78.87%)</b></td><td>352.32 <b>(-63.12%)</b></td><td>269.40 <b>(-47.91%)</b></td><td>241.70 (-11.53%)</td><td>137.89 <b>(-84.12%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2422.90 (n/a)</td><td>955.28 (n/a)</td><td>517.20 (n/a)</td><td>273.20 (n/a)</td><td>868.31 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (+5.45%)</td><td>0.09 (-16.46%)</td><td>0.08 <b>(-26.83%)</b></td><td>0.01 <b>(-81.77%)</b></td><td>0.05 <b>(+125.14%)</b></td><td>2475.70 <b>(+448.45%)</b></td><td>774.70 <b>(+131.88%)</b></td><td>408.30 <b>(+36.69%)</b></td><td>237.50 (-5.19%)</td><td>957.28 <b>(+1103.10%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>451.40 (n/a)</td><td>334.10 (n/a)</td><td>298.70 (n/a)</td><td>250.50 (n/a)</td><td>79.57 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.10 (+10.52%)</td><td>0.07 (-4.65%)</td><td>0.07 (+0.14%)</td><td>0.02 <b>(-65.27%)</b></td><td>0.03 <b>(+106.36%)</b></td><td>1769.40 <b>(+187.94%)</b></td><td>695.92 <b>(+44.28%)</b></td><td>481.30 (-0.15%)</td><td>313.30 (-9.50%)</td><td>604.14 <b>(+534.20%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>614.50 (n/a)</td><td>482.34 (n/a)</td><td>482.00 (n/a)</td><td>346.20 (n/a)</td><td>95.26 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (-4.13%)</td><td>0.01 (-1.44%)</td><td>0.01 (-0.17%)</td><td>0.01 <b>(-22.76%)</b></td><td>0.00 <b>(+43.12%)</b></td><td>495.70 <b>(+29.49%)</b></td><td>313.44 (+5.86%)</td><td>284.90 (+0.18%)</td><td>244.60 (+4.31%)</td><td>104.44 <b>(+93.37%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>382.80 (n/a)</td><td>296.08 (n/a)</td><td>284.40 (n/a)</td><td>234.50 (n/a)</td><td>54.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(+27.43%)</b></td><td>0.01 (+11.80%)</td><td>0.01 (+4.59%)</td><td>0.01 (-1.83%)</td><td>0.00 <b>(+50.54%)</b></td><td>518.70 (+1.87%)</td><td>314.58 (-7.14%)</td><td>286.80 (-4.40%)</td><td>219.30 <b>(-21.54%)</b></td><td>118.13 <b>(+22.94%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.20 (n/a)</td><td>338.78 (n/a)</td><td>300.00 (n/a)</td><td>279.50 (n/a)</td><td>96.09 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 (-3.72%)</td><td>0.01 <b>(-21.27%)</b></td><td>0.01 <b>(-43.08%)</b></td><td>0.00 <b>(-20.81%)</b></td><td>0.00 (+17.33%)</td><td>841.10 <b>(+26.29%)</b></td><td>511.02 <b>(+35.73%)</b></td><td>521.30 <b>(+75.70%)</b></td><td>276.80 (+3.86%)</td><td>236.52 <b>(+40.92%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>666.00 (n/a)</td><td>376.50 (n/a)</td><td>296.70 (n/a)</td><td>266.50 (n/a)</td><td>167.84 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(+41.37%)</b></td><td>0.02 <b>(+66.41%)</b></td><td>0.01 <b>(+42.27%)</b></td><td>0.01 <b>(+577.79%)</b></td><td>0.00 <b>(-52.22%)</b></td><td>299.40 <b>(-85.25%)</b></td><td>268.04 <b>(-62.05%)</b></td><td>279.70 <b>(-29.72%)</b></td><td>220.50 <b>(-29.26%)</b></td><td>33.91 <b>(-95.43%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2029.20 (n/a)</td><td>706.38 (n/a)</td><td>398.00 (n/a)</td><td>311.70 (n/a)</td><td>741.50 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (-10.01%)</td><td>0.01 (+7.12%)</td><td>0.01 (-10.16%)</td><td>0.01 <b>(+235.27%)</b></td><td>0.00 <b>(-42.27%)</b></td><td>548.10 <b>(-70.17%)</b></td><td>387.80 <b>(-39.46%)</b></td><td>403.20 (+11.32%)</td><td>270.60 (+11.08%)</td><td>110.25 <b>(-83.62%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1837.50 (n/a)</td><td>640.56 (n/a)</td><td>362.20 (n/a)</td><td>243.60 (n/a)</td><td>673.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(+58.02%)</b></td><td>0.01 <b>(+54.56%)</b></td><td>0.01 (+10.18%)</td><td>0.01 <b>(+255.46%)</b></td><td>0.00 (-2.48%)</td><td>492.70 <b>(-71.87%)</b></td><td>370.50 <b>(-49.17%)</b></td><td>392.50 (-9.23%)</td><td>264.90 <b>(-36.72%)</b></td><td>95.60 <b>(-83.44%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1751.30 (n/a)</td><td>728.96 (n/a)</td><td>432.40 (n/a)</td><td>418.60 (n/a)</td><td>577.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (+14.06%)</td><td>0.01 (+3.11%)</td><td>0.01 (+3.73%)</td><td>0.01 (+0.45%)</td><td>0.00 <b>(+53.14%)</b></td><td>524.40 (-0.44%)</td><td>386.24 (+0.31%)</td><td>356.70 (-3.59%)</td><td>261.80 (-12.32%)</td><td>111.85 <b>(+31.80%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>526.70 (n/a)</td><td>385.04 (n/a)</td><td>370.00 (n/a)</td><td>298.60 (n/a)</td><td>84.86 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (+17.89%)</td><td>0.01 (-19.23%)</td><td>0.01 <b>(-51.40%)</b></td><td>0.01 <b>(-29.27%)</b></td><td>0.01 <b>(+75.31%)</b></td><td>718.70 <b>(+41.39%)</b></td><td>517.64 <b>(+44.91%)</b></td><td>646.10 <b>(+105.76%)</b></td><td>227.70 (-15.16%)</td><td>230.49 <b>(+122.85%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>508.30 (n/a)</td><td>357.22 (n/a)</td><td>314.00 (n/a)</td><td>268.40 (n/a)</td><td>103.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 <b>(+51.87%)</b></td><td>0.01 <b>(+31.84%)</b></td><td>0.01 <b>(+33.19%)</b></td><td>0.01 <b>(+27.70%)</b></td><td>0.00 <b>(+100.72%)</b></td><td>615.00 <b>(-21.69%)</b></td><td>479.00 <b>(-21.26%)</b></td><td>468.40 <b>(-24.91%)</b></td><td>290.30 <b>(-34.16%)</b></td><td>131.50 (+5.48%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>785.30 (n/a)</td><td>608.34 (n/a)</td><td>623.80 (n/a)</td><td>440.90 (n/a)</td><td>124.67 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (+9.07%)</td><td>0.01 <b>(-22.43%)</b></td><td>0.01 <b>(-46.64%)</b></td><td>0.01 (-18.98%)</td><td>0.00 <b>(+20.95%)</b></td><td>804.10 <b>(+23.42%)</b></td><td>565.10 <b>(+35.74%)</b></td><td>604.00 <b>(+87.40%)</b></td><td>253.40 (-8.32%)</td><td>210.73 <b>(+29.46%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>651.50 (n/a)</td><td>416.32 (n/a)</td><td>322.30 (n/a)</td><td>276.40 (n/a)</td><td>162.78 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (+15.30%)</td><td>0.01 (-6.87%)</td><td>0.01 (-12.90%)</td><td>0.01 (-15.02%)</td><td>0.00 <b>(+43.38%)</b></td><td>611.90 (+17.67%)</td><td>404.94 (+12.36%)</td><td>367.10 (+14.83%)</td><td>243.50 (-13.25%)</td><td>138.55 <b>(+44.00%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>520.00 (n/a)</td><td>360.40 (n/a)</td><td>319.70 (n/a)</td><td>280.70 (n/a)</td><td>96.22 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 (-19.00%)</td><td>0.01 (-12.62%)</td><td>0.01 (-8.01%)</td><td>0.01 <b>(-26.97%)</b></td><td>0.00 (-16.12%)</td><td>737.10 <b>(+36.93%)</b></td><td>537.82 (+15.56%)</td><td>530.00 (+8.70%)</td><td>362.80 <b>(+23.44%)</b></td><td>144.43 <b>(+46.40%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>538.30 (n/a)</td><td>465.40 (n/a)</td><td>487.60 (n/a)</td><td>293.90 (n/a)</td><td>98.65 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (-9.60%)</td><td>0.03 (-8.90%)</td><td>0.03 (-8.69%)</td><td>0.02 <b>(+29.50%)</b></td><td>0.01 <b>(-29.81%)</b></td><td>414.40 <b>(-22.79%)</b></td><td>337.10 (+4.66%)</td><td>303.20 (+9.50%)</td><td>259.30 (+10.62%)</td><td>71.26 <b>(-41.51%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>536.70 (n/a)</td><td>322.10 (n/a)</td><td>276.90 (n/a)</td><td>234.40 (n/a)</td><td>121.84 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (-15.08%)</td><td>0.03 (-14.38%)</td><td>0.03 (-8.13%)</td><td>0.02 <b>(-32.25%)</b></td><td>0.01 (+2.87%)</td><td>459.40 <b>(+47.62%)</b></td><td>317.02 (+19.72%)</td><td>293.40 (+8.83%)</td><td>226.30 (+17.74%)</td><td>86.54 <b>(+90.36%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>311.20 (n/a)</td><td>264.80 (n/a)</td><td>269.60 (n/a)</td><td>192.20 (n/a)</td><td>45.46 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (+2.22%)</td><td>0.02 (+3.79%)</td><td>0.03 (+14.73%)</td><td>0.01 (-3.89%)</td><td>0.01 (-3.21%)</td><td>580.40 (+4.05%)</td><td>367.12 (-4.12%)</td><td>285.00 (-12.84%)</td><td>252.10 (-2.17%)</td><td>141.23 (-1.16%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>557.80 (n/a)</td><td>382.90 (n/a)</td><td>327.00 (n/a)</td><td>257.70 (n/a)</td><td>142.89 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (-7.88%)</td><td>0.03 (-0.17%)</td><td>0.03 <b>(+21.34%)</b></td><td>0.02 <b>(-31.33%)</b></td><td>0.01 <b>(+44.55%)</b></td><td>512.50 <b>(+45.64%)</b></td><td>308.78 (+7.16%)</td><td>244.20 (-17.61%)</td><td>226.30 (+8.54%)</td><td>122.31 <b>(+129.39%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>351.90 (n/a)</td><td>288.16 (n/a)</td><td>296.40 (n/a)</td><td>208.50 (n/a)</td><td>53.32 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 <b>(+41.99%)</b></td><td>0.03 <b>(+32.83%)</b></td><td>0.03 (+18.13%)</td><td>0.02 <b>(+57.14%)</b></td><td>0.01 <b>(+21.86%)</b></td><td>330.30 <b>(-36.36%)</b></td><td>266.06 <b>(-26.16%)</b></td><td>284.20 (-15.37%)</td><td>187.70 <b>(-29.59%)</b></td><td>53.84 <b>(-46.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.00 (n/a)</td><td>360.30 (n/a)</td><td>335.80 (n/a)</td><td>266.60 (n/a)</td><td>101.13 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (-2.83%)</td><td>0.03 (-2.38%)</td><td>0.03 (+2.96%)</td><td>0.02 (+3.41%)</td><td>0.01 (+4.44%)</td><td>520.20 (-3.29%)</td><td>332.04 (+2.42%)</td><td>270.40 (-2.87%)</td><td>247.90 (+2.91%)</td><td>115.91 (-4.27%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.90 (n/a)</td><td>324.20 (n/a)</td><td>278.40 (n/a)</td><td>240.90 (n/a)</td><td>121.07 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (-8.83%)</td><td>0.02 (-13.98%)</td><td>0.02 (-17.80%)</td><td>0.01 <b>(-22.51%)</b></td><td>0.01 (-2.58%)</td><td>780.90 <b>(+29.03%)</b></td><td>455.94 <b>(+21.74%)</b></td><td>477.20 <b>(+21.67%)</b></td><td>215.00 (+9.69%)</td><td>223.36 <b>(+37.58%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>605.20 (n/a)</td><td>374.52 (n/a)</td><td>392.20 (n/a)</td><td>196.00 (n/a)</td><td>162.35 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (-18.91%)</td><td>0.02 (-8.13%)</td><td>0.02 (-11.91%)</td><td>0.01 <b>(+234.94%)</b></td><td>0.01 <b>(-53.34%)</b></td><td>554.60 <b>(-70.15%)</b></td><td>378.60 <b>(-36.09%)</b></td><td>342.50 (+13.52%)</td><td>286.20 <b>(+23.31%)</b></td><td>108.96 <b>(-84.61%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1857.70 (n/a)</td><td>592.44 (n/a)</td><td>301.70 (n/a)</td><td>232.10 (n/a)</td><td>707.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(-23.61%)</b></td><td>0.02 <b>(-22.54%)</b></td><td>0.02 (-18.68%)</td><td>0.01 <b>(-25.63%)</b></td><td>0.00 <b>(-28.88%)</b></td><td>669.10 <b>(+34.47%)</b></td><td>513.94 <b>(+27.91%)</b></td><td>522.70 <b>(+22.96%)</b></td><td>344.00 <b>(+30.90%)</b></td><td>124.67 <b>(+20.06%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>497.60 (n/a)</td><td>401.80 (n/a)</td><td>425.10 (n/a)</td><td>262.80 (n/a)</td><td>103.84 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (+11.53%)</td><td>0.02 <b>(-26.52%)</b></td><td>0.02 <b>(-41.05%)</b></td><td>0.01 <b>(-36.10%)</b></td><td>0.01 <b>(+98.92%)</b></td><td>604.70 <b>(+56.50%)</b></td><td>445.06 <b>(+51.12%)</b></td><td>492.50 <b>(+69.65%)</b></td><td>217.00 (-10.33%)</td><td>151.55 <b>(+166.61%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>386.40 (n/a)</td><td>294.50 (n/a)</td><td>290.30 (n/a)</td><td>242.00 (n/a)</td><td>56.84 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(-40.08%)</b></td><td>0.02 <b>(-22.20%)</b></td><td>0.02 (-2.43%)</td><td>0.01 (-4.58%)</td><td>0.00 <b>(-61.42%)</b></td><td>607.40 (+4.81%)</td><td>477.18 (+15.96%)</td><td>493.40 (+2.49%)</td><td>338.70 <b>(+66.93%)</b></td><td>102.95 <b>(-32.16%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.50 (n/a)</td><td>411.52 (n/a)</td><td>481.40 (n/a)</td><td>202.90 (n/a)</td><td>151.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(-29.89%)</b></td><td>0.02 <b>(-26.14%)</b></td><td>0.02 <b>(-34.14%)</b></td><td>0.01 (+2.63%)</td><td>0.00 <b>(-51.41%)</b></td><td>578.30 (-2.58%)</td><td>498.18 <b>(+26.69%)</b></td><td>511.60 <b>(+51.86%)</b></td><td>349.00 <b>(+42.62%)</b></td><td>92.35 <b>(-34.81%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.60 (n/a)</td><td>393.24 (n/a)</td><td>336.90 (n/a)</td><td>244.70 (n/a)</td><td>141.68 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (-10.85%)</td><td>0.05 (-5.56%)</td><td>0.05 (-3.63%)</td><td>0.03 (-7.42%)</td><td>0.01 (-14.97%)</td><td>561.80 (+8.02%)</td><td>373.28 (+4.64%)</td><td>310.50 (+3.78%)</td><td>267.80 (+12.14%)</td><td>122.66 (+1.18%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>520.10 (n/a)</td><td>356.72 (n/a)</td><td>299.20 (n/a)</td><td>238.80 (n/a)</td><td>121.23 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 <b>(+34.37%)</b></td><td>0.06 <b>(+47.92%)</b></td><td>0.06 <b>(+74.03%)</b></td><td>0.05 <b>(+103.57%)</b></td><td>0.01 <b>(-20.59%)</b></td><td>318.30 <b>(-50.87%)</b></td><td>281.28 <b>(-37.70%)</b></td><td>295.00 <b>(-42.55%)</b></td><td>201.90 <b>(-25.58%)</b></td><td>45.55 <b>(-70.97%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>647.90 (n/a)</td><td>451.46 (n/a)</td><td>513.50 (n/a)</td><td>271.30 (n/a)</td><td>156.91 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (+7.10%)</td><td>0.05 (+5.44%)</td><td>0.06 (+13.03%)</td><td>0.04 (+6.83%)</td><td>0.01 <b>(+25.27%)</b></td><td>449.80 (-6.39%)</td><td>347.12 (-3.81%)</td><td>296.70 (-11.54%)</td><td>274.20 (-6.64%)</td><td>88.60 (+12.32%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>480.50 (n/a)</td><td>360.86 (n/a)</td><td>335.40 (n/a)</td><td>293.70 (n/a)</td><td>78.88 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (+7.40%)</td><td>0.05 (+1.19%)</td><td>0.04 (-14.38%)</td><td>0.03 (-3.80%)</td><td>0.01 <b>(+22.76%)</b></td><td>506.90 (+3.96%)</td><td>367.46 (+0.19%)</td><td>371.60 (+16.82%)</td><td>282.10 (-6.90%)</td><td>93.20 (+15.27%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>487.60 (n/a)</td><td>366.78 (n/a)</td><td>318.10 (n/a)</td><td>303.00 (n/a)</td><td>80.86 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 <b>(-36.68%)</b></td><td>0.04 <b>(-22.83%)</b></td><td>0.03 (-7.13%)</td><td>0.03 (+17.10%)</td><td>0.01 <b>(-70.64%)</b></td><td>487.10 (-14.60%)</td><td>450.06 (+16.23%)</td><td>469.40 (+7.69%)</td><td>347.60 <b>(+57.93%)</b></td><td>57.82 <b>(-59.78%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>570.40 (n/a)</td><td>387.22 (n/a)</td><td>435.90 (n/a)</td><td>220.10 (n/a)</td><td>143.77 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (-3.80%)</td><td>0.04 (-8.13%)</td><td>0.03 <b>(-46.42%)</b></td><td>0.03 <b>(+67.78%)</b></td><td>0.02 (-14.55%)</td><td>623.70 <b>(-40.40%)</b></td><td>465.42 (-4.41%)</td><td>565.00 <b>(+86.59%)</b></td><td>282.60 (+3.97%)</td><td>166.18 <b>(-49.27%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1046.50 (n/a)</td><td>486.90 (n/a)</td><td>302.80 (n/a)</td><td>271.80 (n/a)</td><td>327.57 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 <b>(-27.73%)</b></td><td>0.04 <b>(-26.41%)</b></td><td>0.03 <b>(-44.06%)</b></td><td>0.02 <b>(+87.15%)</b></td><td>0.02 <b>(-37.28%)</b></td><td>996.10 <b>(-46.57%)</b></td><td>537.78 (-10.88%)</td><td>547.40 <b>(+78.77%)</b></td><td>264.10 <b>(+38.34%)</b></td><td>290.13 <b>(-59.16%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1864.20 (n/a)</td><td>603.46 (n/a)</td><td>306.20 (n/a)</td><td>190.90 (n/a)</td><td>710.42 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (-7.15%)</td><td>0.04 <b>(+20.78%)</b></td><td>0.04 <b>(+41.49%)</b></td><td>0.03 <b>(+114.65%)</b></td><td>0.01 <b>(-48.78%)</b></td><td>511.70 <b>(-53.41%)</b></td><td>434.92 <b>(-33.12%)</b></td><td>453.00 <b>(-29.33%)</b></td><td>293.70 (+7.70%)</td><td>84.00 <b>(-75.03%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1098.30 (n/a)</td><td>650.34 (n/a)</td><td>641.00 (n/a)</td><td>272.70 (n/a)</td><td>336.36 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (-13.31%)</td><td>0.04 <b>(-29.68%)</b></td><td>0.04 <b>(-36.26%)</b></td><td>0.02 <b>(-39.95%)</b></td><td>0.01 (+12.28%)</td><td>750.10 <b>(+66.50%)</b></td><td>480.20 <b>(+50.48%)</b></td><td>434.70 <b>(+56.87%)</b></td><td>296.00 (+15.35%)</td><td>175.88 <b>(+118.13%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>450.50 (n/a)</td><td>319.12 (n/a)</td><td>277.10 (n/a)</td><td>256.60 (n/a)</td><td>80.63 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 (-18.91%)</td><td>0.04 (-14.29%)</td><td>0.03 <b>(-29.46%)</b></td><td>0.03 <b>(+224.66%)</b></td><td>0.01 <b>(-57.10%)</b></td><td>581.90 <b>(-69.20%)</b></td><td>468.40 <b>(-28.00%)</b></td><td>497.40 <b>(+41.75%)</b></td><td>309.20 <b>(+23.33%)</b></td><td>102.50 <b>(-85.32%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1889.20 (n/a)</td><td>650.52 (n/a)</td><td>350.90 (n/a)</td><td>250.70 (n/a)</td><td>698.45 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (-3.75%)</td><td>0.03 (-2.68%)</td><td>0.03 (-2.02%)</td><td>0.03 (-7.64%)</td><td>0.00 (+3.60%)</td><td>608.60 (+8.27%)</td><td>501.68 (+3.03%)</td><td>510.40 (+2.06%)</td><td>421.10 (+3.90%)</td><td>71.39 (+17.57%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>562.10 (n/a)</td><td>486.92 (n/a)</td><td>500.10 (n/a)</td><td>405.30 (n/a)</td><td>60.72 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 (+19.77%)</td><td>0.04 (+18.01%)</td><td>0.03 (-4.86%)</td><td>0.03 <b>(+21.84%)</b></td><td>0.01 <b>(+40.81%)</b></td><td>616.50 (-17.92%)</td><td>459.68 (-13.39%)</td><td>539.10 (+5.13%)</td><td>300.10 (-16.52%)</td><td>148.51 (-8.36%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>751.10 (n/a)</td><td>530.72 (n/a)</td><td>512.80 (n/a)</td><td>359.50 (n/a)</td><td>162.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.12 (-19.50%)</td><td>0.09 (-0.36%)</td><td>0.11 <b>(+65.74%)</b></td><td>0.05 (-16.99%)</td><td>0.03 <b>(-26.09%)</b></td><td>620.60 <b>(+20.46%)</b></td><td>397.38 (-2.54%)</td><td>306.80 <b>(-39.67%)</b></td><td>269.30 <b>(+24.22%)</b></td><td>150.96 (+3.85%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>515.20 (n/a)</td><td>407.74 (n/a)</td><td>508.50 (n/a)</td><td>216.80 (n/a)</td><td>145.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.12 (-3.49%)</td><td>0.08 (-14.43%)</td><td>0.06 <b>(-25.37%)</b></td><td>0.05 (-6.21%)</td><td>0.03 (+13.79%)</td><td>616.00 (+6.61%)</td><td>469.14 <b>(+20.87%)</b></td><td>528.70 <b>(+33.98%)</b></td><td>276.70 (+3.63%)</td><td>156.20 <b>(+28.55%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>577.80 (n/a)</td><td>388.14 (n/a)</td><td>394.60 (n/a)</td><td>267.00 (n/a)</td><td>121.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.12 (-13.75%)</td><td>0.08 (-4.29%)</td><td>0.09 (+16.55%)</td><td>0.05 <b>(-31.57%)</b></td><td>0.03 (+8.50%)</td><td>674.70 <b>(+46.13%)</b></td><td>439.38 (+10.73%)</td><td>377.50 (-14.20%)</td><td>277.00 (+15.95%)</td><td>173.15 <b>(+88.16%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>461.70 (n/a)</td><td>396.82 (n/a)</td><td>440.00 (n/a)</td><td>238.90 (n/a)</td><td>92.03 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.15 (+10.91%)</td><td>0.09 (-2.82%)</td><td>0.09 (-10.62%)</td><td>0.07 (+16.39%)</td><td>0.03 (+0.35%)</td><td>486.40 (-14.09%)</td><td>384.20 (+0.49%)</td><td>373.10 (+11.87%)</td><td>224.10 (-9.86%)</td><td>103.86 <b>(-24.43%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>566.20 (n/a)</td><td>382.32 (n/a)</td><td>333.50 (n/a)</td><td>248.60 (n/a)</td><td>137.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 <b>(-26.96%)</b></td><td>0.08 (-13.68%)</td><td>0.08 <b>(-30.68%)</b></td><td>0.06 (-3.08%)</td><td>0.02 <b>(-40.66%)</b></td><td>592.60 (+3.17%)</td><td>415.60 (+7.19%)</td><td>433.40 <b>(+44.27%)</b></td><td>296.40 <b>(+36.91%)</b></td><td>120.95 <b>(-26.16%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>574.40 (n/a)</td><td>387.72 (n/a)</td><td>300.40 (n/a)</td><td>216.50 (n/a)</td><td>163.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (+6.22%)</td><td>0.09 (+5.61%)</td><td>0.10 <b>(+37.58%)</b></td><td>0.05 (-5.79%)</td><td>0.04 (+13.59%)</td><td>606.20 (+6.15%)</td><td>397.54 (-2.19%)</td><td>324.30 <b>(-27.32%)</b></td><td>231.90 (-5.88%)</td><td>159.79 <b>(+21.11%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>571.10 (n/a)</td><td>406.46 (n/a)</td><td>446.20 (n/a)</td><td>246.40 (n/a)</td><td>131.94 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.15 (-19.58%)</td><td>0.10 (+1.82%)</td><td>0.11 (+16.33%)</td><td>0.07 <b>(+24.47%)</b></td><td>0.04 <b>(-33.92%)</b></td><td>498.90 (-19.66%)</td><td>355.52 (-11.97%)</td><td>296.60 (-14.05%)</td><td>221.70 <b>(+24.34%)</b></td><td>128.38 <b>(-33.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>621.00 (n/a)</td><td>403.88 (n/a)</td><td>345.10 (n/a)</td><td>178.30 (n/a)</td><td>193.74 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.13 (+7.18%)</td><td>0.08 (-5.95%)</td><td>0.07 <b>(-26.33%)</b></td><td>0.05 (-1.92%)</td><td>0.03 (+14.21%)</td><td>631.30 (+1.97%)</td><td>456.58 (+8.66%)</td><td>490.90 <b>(+35.76%)</b></td><td>260.50 (-6.73%)</td><td>163.44 (+8.51%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>619.10 (n/a)</td><td>420.20 (n/a)</td><td>361.60 (n/a)</td><td>279.30 (n/a)</td><td>150.62 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.12 (-7.64%)</td><td>0.09 (+1.60%)</td><td>0.07 (+2.42%)</td><td>0.07 <b>(+24.67%)</b></td><td>0.02 <b>(-22.54%)</b></td><td>463.70 (-19.78%)</td><td>382.28 (-5.83%)</td><td>442.50 (-2.36%)</td><td>276.30 (+8.27%)</td><td>95.60 <b>(-30.36%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>578.00 (n/a)</td><td>405.96 (n/a)</td><td>453.20 (n/a)</td><td>255.20 (n/a)</td><td>137.27 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.15 (+18.52%)</td><td>0.09 (+19.61%)</td><td>0.07 (+12.71%)</td><td>0.05 <b>(+118.43%)</b></td><td>0.04 (-2.53%)</td><td>604.00 <b>(-54.22%)</b></td><td>402.12 <b>(-30.94%)</b></td><td>466.10 (-11.27%)</td><td>212.80 (-15.62%)</td><td>162.04 <b>(-62.61%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1319.40 (n/a)</td><td>582.26 (n/a)</td><td>525.30 (n/a)</td><td>252.20 (n/a)</td><td>433.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.09 <b>(-35.75%)</b></td><td>0.07 (-2.80%)</td><td>0.08 <b>(+31.03%)</b></td><td>0.05 (-5.55%)</td><td>0.01 <b>(-59.46%)</b></td><td>640.90 (+5.88%)</td><td>459.10 (-5.40%)</td><td>427.90 <b>(-23.68%)</b></td><td>370.00 <b>(+55.66%)</b></td><td>106.96 <b>(-29.28%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>605.30 (n/a)</td><td>485.32 (n/a)</td><td>560.70 (n/a)</td><td>237.70 (n/a)</td><td>151.23 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (+3.69%)</td><td>0.10 <b>(+45.78%)</b></td><td>0.10 <b>(+60.43%)</b></td><td>0.06 <b>(+257.40%)</b></td><td>0.03 <b>(-33.89%)</b></td><td>540.40 <b>(-72.02%)</b></td><td>339.42 <b>(-54.54%)</b></td><td>316.90 <b>(-37.68%)</b></td><td>237.50 (-3.57%)</td><td>120.12 <b>(-82.50%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1931.60 (n/a)</td><td>746.70 (n/a)</td><td>508.50 (n/a)</td><td>246.30 (n/a)</td><td>686.55 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 (+8.01%)</td><td>0.08 (-4.76%)</td><td>0.09 (+4.11%)</td><td>0.05 <b>(-35.87%)</b></td><td>0.02 <b>(+154.59%)</b></td><td>506.60 <b>(+55.92%)</b></td><td>320.84 (+13.04%)</td><td>266.50 (-3.93%)</td><td>229.00 (-7.40%)</td><td>113.92 <b>(+270.09%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>324.90 (n/a)</td><td>283.82 (n/a)</td><td>277.40 (n/a)</td><td>247.30 (n/a)</td><td>30.78 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.18 (-11.13%)</td><td>0.12 (-19.22%)</td><td>0.11 <b>(-42.35%)</b></td><td>0.09 <b>(+33.20%)</b></td><td>0.04 <b>(-36.69%)</b></td><td>575.10 <b>(-24.92%)</b></td><td>440.94 (+8.79%)</td><td>464.20 <b>(+73.47%)</b></td><td>269.20 (+12.54%)</td><td>131.21 <b>(-43.00%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>766.00 (n/a)</td><td>405.30 (n/a)</td><td>267.60 (n/a)</td><td>239.20 (n/a)</td><td>230.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>4.02 (-3.86%)</td><td>3.28 (-5.93%)</td><td>3.48 (+0.26%)</td><td>2.55 (-15.24%)</td><td>0.64 <b>(+42.79%)</b></td><td>4114.00 (+17.97%)</td><td>3296.70 (+8.39%)</td><td>3009.90 (-0.27%)</td><td>2609.20 (+4.01%)</td><td>669.99 <b>(+80.14%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>4.18 (n/a)</td><td>3.49 (n/a)</td><td>3.47 (n/a)</td><td>3.01 (n/a)</td><td>0.45 (n/a)</td><td>3487.20 (n/a)</td><td>3041.52 (n/a)</td><td>3017.90 (n/a)</td><td>2508.60 (n/a)</td><td>371.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.19 (+18.98%)</td><td>0.16 <b>(+24.42%)</b></td><td>0.16 <b>(+26.27%)</b></td><td>0.13 <b>(+41.16%)</b></td><td>0.02 (-19.74%)</td><td>304.00 <b>(-29.15%)</b></td><td>260.00 <b>(-21.43%)</b></td><td>256.60 <b>(-20.80%)</b></td><td>210.80 (-15.95%)</td><td>33.76 <b>(-52.74%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>429.10 (n/a)</td><td>330.90 (n/a)</td><td>324.00 (n/a)</td><td>250.80 (n/a)</td><td>71.45 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 <b>(+48.54%)</b></td><td>0.02 (+14.72%)</td><td>0.01 (-13.68%)</td><td>0.01 <b>(+22.07%)</b></td><td>0.01 <b>(+78.90%)</b></td><td>500.00 (-18.09%)</td><td>374.02 (-7.48%)</td><td>451.70 (+15.85%)</td><td>196.00 <b>(-32.69%)</b></td><td>134.60 (+3.37%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>610.40 (n/a)</td><td>404.24 (n/a)</td><td>389.90 (n/a)</td><td>291.20 (n/a)</td><td>130.21 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (+13.39%)</td><td>0.02 <b>(+34.63%)</b></td><td>0.02 <b>(+41.70%)</b></td><td>0.01 <b>(+335.50%)</b></td><td>0.00 <b>(-30.50%)</b></td><td>476.60 <b>(-77.04%)</b></td><td>288.98 <b>(-56.36%)</b></td><td>247.00 <b>(-29.43%)</b></td><td>208.80 (-11.79%)</td><td>107.13 <b>(-86.48%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2075.60 (n/a)</td><td>662.20 (n/a)</td><td>350.00 (n/a)</td><td>236.70 (n/a)</td><td>792.36 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 <b>(+24.05%)</b></td><td>0.02 (-2.52%)</td><td>0.02 (-9.38%)</td><td>0.01 (-19.60%)</td><td>0.01 <b>(+86.15%)</b></td><td>612.80 <b>(+24.38%)</b></td><td>390.64 (+13.03%)</td><td>346.10 (+10.36%)</td><td>216.30 (-19.38%)</td><td>163.08 <b>(+84.36%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>492.70 (n/a)</td><td>345.60 (n/a)</td><td>313.60 (n/a)</td><td>268.30 (n/a)</td><td>88.46 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (-17.18%)</td><td>0.01 <b>(-20.83%)</b></td><td>0.02 (-14.80%)</td><td>0.01 (+0.74%)</td><td>0.01 (-13.57%)</td><td>523.90 (-0.74%)</td><td>337.98 <b>(+23.73%)</b></td><td>254.20 (+17.36%)</td><td>211.50 <b>(+20.72%)</b></td><td>139.77 (-2.96%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>527.80 (n/a)</td><td>273.16 (n/a)</td><td>216.60 (n/a)</td><td>175.20 (n/a)</td><td>144.04 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 <b>(-36.23%)</b></td><td>0.01 (-15.58%)</td><td>0.01 (-5.22%)</td><td>0.01 <b>(+95.07%)</b></td><td>0.00 <b>(-75.71%)</b></td><td>528.10 <b>(-48.73%)</b></td><td>470.74 (-7.72%)</td><td>480.20 (+5.52%)</td><td>368.30 <b>(+56.79%)</b></td><td>60.56 <b>(-80.89%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1030.10 (n/a)</td><td>510.14 (n/a)</td><td>455.10 (n/a)</td><td>234.90 (n/a)</td><td>316.91 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (+8.32%)</td><td>0.01 (-5.27%)</td><td>0.01 (+4.85%)</td><td>0.01 <b>(-20.03%)</b></td><td>0.01 (+15.40%)</td><td>796.70 <b>(+25.05%)</b></td><td>460.86 (+13.59%)</td><td>352.80 (-4.65%)</td><td>230.10 (-7.66%)</td><td>238.15 <b>(+42.96%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>637.10 (n/a)</td><td>405.72 (n/a)</td><td>370.00 (n/a)</td><td>249.20 (n/a)</td><td>166.59 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (+9.15%)</td><td>0.01 (-2.93%)</td><td>0.02 (-2.59%)</td><td>0.01 (+12.47%)</td><td>0.00 (+17.74%)</td><td>495.90 (-11.10%)</td><td>373.42 (+4.07%)</td><td>314.20 (+2.65%)</td><td>251.50 (-8.38%)</td><td>113.86 (-1.01%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>557.80 (n/a)</td><td>358.80 (n/a)</td><td>306.10 (n/a)</td><td>274.50 (n/a)</td><td>115.02 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (+11.18%)</td><td>0.01 (+0.08%)</td><td>0.01 (-16.31%)</td><td>0.01 (+6.42%)</td><td>0.01 (+13.51%)</td><td>584.90 (-6.03%)</td><td>417.94 (+1.18%)</td><td>472.50 (+19.50%)</td><td>211.20 (-10.05%)</td><td>159.58 (-3.43%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>622.40 (n/a)</td><td>413.08 (n/a)</td><td>395.40 (n/a)</td><td>234.80 (n/a)</td><td>165.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (+18.93%)</td><td>0.01 (+10.75%)</td><td>0.01 (+11.64%)</td><td>0.01 (+5.99%)</td><td>0.00 <b>(+35.55%)</b></td><td>518.30 (-5.66%)</td><td>424.90 (-7.80%)</td><td>442.10 (-10.43%)</td><td>249.30 (-15.92%)</td><td>105.97 (+7.64%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>549.40 (n/a)</td><td>460.84 (n/a)</td><td>493.60 (n/a)</td><td>296.50 (n/a)</td><td>98.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (+2.50%)</td><td>0.01 (+5.89%)</td><td>0.01 <b>(+24.48%)</b></td><td>0.01 (+14.79%)</td><td>0.00 (-7.65%)</td><td>471.40 (-12.88%)</td><td>356.00 (-8.06%)</td><td>352.20 (-19.66%)</td><td>213.20 (-2.43%)</td><td>113.76 (-16.88%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>541.10 (n/a)</td><td>387.22 (n/a)</td><td>438.40 (n/a)</td><td>218.50 (n/a)</td><td>136.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 <b>(+49.76%)</b></td><td>0.01 <b>(+86.60%)</b></td><td>0.01 <b>(+77.47%)</b></td><td>0.01 <b>(+204.73%)</b></td><td>0.00 (-1.43%)</td><td>605.30 <b>(-67.19%)</b></td><td>357.78 <b>(-58.33%)</b></td><td>321.70 <b>(-43.65%)</b></td><td>241.80 <b>(-33.22%)</b></td><td>142.23 <b>(-76.89%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1844.60 (n/a)</td><td>858.66 (n/a)</td><td>570.90 (n/a)</td><td>362.10 (n/a)</td><td>615.56 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 <b>(-48.04%)</b></td><td>0.01 <b>(-34.68%)</b></td><td>0.01 <b>(-25.24%)</b></td><td>0.00 <b>(-40.34%)</b></td><td>0.00 <b>(-58.55%)</b></td><td>975.10 <b>(+67.60%)</b></td><td>664.62 <b>(+48.09%)</b></td><td>606.20 <b>(+33.76%)</b></td><td>477.30 <b>(+92.46%)</b></td><td>186.06 <b>(+47.38%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>581.80 (n/a)</td><td>448.78 (n/a)</td><td>453.20 (n/a)</td><td>248.00 (n/a)</td><td>126.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (-17.28%)</td><td>0.02 (+1.74%)</td><td>0.03 (-1.97%)</td><td>0.02 <b>(+37.04%)</b></td><td>0.00 <b>(-49.25%)</b></td><td>444.30 <b>(-27.03%)</b></td><td>347.90 (-10.90%)</td><td>316.40 (+2.00%)</td><td>282.00 <b>(+20.87%)</b></td><td>69.87 <b>(-56.52%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>608.90 (n/a)</td><td>390.48 (n/a)</td><td>310.20 (n/a)</td><td>233.30 (n/a)</td><td>160.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 <b>(+23.76%)</b></td><td>0.04 <b>(+51.72%)</b></td><td>0.04 <b>(+39.96%)</b></td><td>0.03 <b>(+329.94%)</b></td><td>0.01 <b>(-24.48%)</b></td><td>475.30 <b>(-76.74%)</b></td><td>317.50 <b>(-57.42%)</b></td><td>290.30 <b>(-28.53%)</b></td><td>225.50 (-19.20%)</td><td>101.64 <b>(-86.31%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2043.30 (n/a)</td><td>745.62 (n/a)</td><td>406.20 (n/a)</td><td>279.10 (n/a)</td><td>742.60 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 <b>(-31.17%)</b></td><td>0.02 <b>(-23.12%)</b></td><td>0.02 (-17.24%)</td><td>0.00 <b>(-67.40%)</b></td><td>0.01 (-18.92%)</td><td>1886.00 <b>(+206.72%)</b></td><td>695.52 <b>(+70.57%)</b></td><td>498.90 <b>(+20.83%)</b></td><td>257.20 <b>(+45.31%)</b></td><td>678.97 <b>(+247.24%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>614.90 (n/a)</td><td>407.76 (n/a)</td><td>412.90 (n/a)</td><td>177.00 (n/a)</td><td>195.54 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (-6.94%)</td><td>0.03 (+3.04%)</td><td>0.03 <b>(+44.70%)</b></td><td>0.00 <b>(-75.31%)</b></td><td>0.02 <b>(+24.28%)</b></td><td>2412.80 <b>(+305.04%)</b></td><td>756.48 <b>(+69.25%)</b></td><td>333.30 <b>(-30.88%)</b></td><td>232.40 (+7.49%)</td><td>931.42 <b>(+551.95%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>595.70 (n/a)</td><td>446.96 (n/a)</td><td>482.20 (n/a)</td><td>216.20 (n/a)</td><td>142.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (+9.12%)</td><td>0.03 <b>(+33.66%)</b></td><td>0.03 <b>(+58.65%)</b></td><td>0.01 (-5.42%)</td><td>0.01 <b>(+34.84%)</b></td><td>587.20 (+5.73%)</td><td>338.62 <b>(-21.71%)</b></td><td>279.80 <b>(-36.98%)</b></td><td>255.10 (-8.37%)</td><td>141.02 <b>(+41.02%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.40 (n/a)</td><td>432.50 (n/a)</td><td>444.00 (n/a)</td><td>278.40 (n/a)</td><td>100.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.04 (-14.65%)</td><td>0.02 (-14.21%)</td><td>0.02 (-17.31%)</td><td>0.02 (-4.99%)</td><td>0.01 (-19.37%)</td><td>659.70 (+5.25%)</td><td>515.40 (+14.10%)</td><td>551.50 <b>(+20.94%)</b></td><td>284.80 (+17.15%)</td><td>139.07 (-4.40%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>626.80 (n/a)</td><td>451.70 (n/a)</td><td>456.00 (n/a)</td><td>243.10 (n/a)</td><td>145.47 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (+3.43%)</td><td>0.02 (-5.16%)</td><td>0.02 <b>(-28.35%)</b></td><td>0.02 <b>(+32.54%)</b></td><td>0.01 <b>(-24.87%)</b></td><td>493.70 <b>(-24.56%)</b></td><td>415.20 (-2.69%)</td><td>438.30 <b>(+39.54%)</b></td><td>259.60 (-3.31%)</td><td>93.04 <b>(-48.59%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>654.40 (n/a)</td><td>426.66 (n/a)</td><td>314.10 (n/a)</td><td>268.50 (n/a)</td><td>180.97 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 <b>(-40.01%)</b></td><td>0.02 <b>(-32.33%)</b></td><td>0.02 <b>(-40.98%)</b></td><td>0.02 (-11.13%)</td><td>0.00 <b>(-57.88%)</b></td><td>543.20 (+12.53%)</td><td>459.48 <b>(+39.99%)</b></td><td>489.30 <b>(+69.43%)</b></td><td>342.10 <b>(+66.72%)</b></td><td>82.74 <b>(-22.05%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>482.70 (n/a)</td><td>328.22 (n/a)</td><td>288.80 (n/a)</td><td>205.20 (n/a)</td><td>106.16 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 <b>(-32.55%)</b></td><td>0.02 (-12.67%)</td><td>0.03 (-9.62%)</td><td>0.01 (-9.65%)</td><td>0.01 <b>(-38.31%)</b></td><td>665.60 (+10.68%)</td><td>381.08 (+4.16%)</td><td>282.20 (+10.67%)</td><td>262.30 <b>(+48.19%)</b></td><td>174.36 (-10.91%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.40 (n/a)</td><td>365.86 (n/a)</td><td>255.00 (n/a)</td><td>177.00 (n/a)</td><td>195.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 <b>(-39.03%)</b></td><td>0.03 <b>(-21.04%)</b></td><td>0.03 <b>(-21.51%)</b></td><td>0.02 (+4.27%)</td><td>0.01 <b>(-55.28%)</b></td><td>503.80 (-4.09%)</td><td>377.10 (+14.94%)</td><td>360.30 <b>(+27.40%)</b></td><td>287.20 <b>(+64.02%)</b></td><td>93.83 <b>(-32.42%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.30 (n/a)</td><td>328.08 (n/a)</td><td>282.80 (n/a)</td><td>175.10 (n/a)</td><td>138.85 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.03 (-15.90%)</td><td>0.02 (+14.48%)</td><td>0.02 <b>(+41.82%)</b></td><td>0.02 <b>(+25.88%)</b></td><td>0.01 <b>(-37.81%)</b></td><td>511.20 <b>(-20.56%)</b></td><td>395.26 (-17.97%)</td><td>368.70 <b>(-29.49%)</b></td><td>293.70 (+18.91%)</td><td>94.92 <b>(-35.91%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.50 (n/a)</td><td>481.84 (n/a)</td><td>522.90 (n/a)</td><td>247.00 (n/a)</td><td>148.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (-4.71%)</td><td>0.04 (-3.71%)</td><td>0.04 <b>(-25.41%)</b></td><td>0.04 <b>(+23.96%)</b></td><td>0.01 <b>(-37.28%)</b></td><td>447.30 (-19.32%)</td><td>378.58 (-2.71%)</td><td>405.50 <b>(+34.09%)</b></td><td>290.30 (+4.95%)</td><td>75.34 <b>(-47.01%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>554.40 (n/a)</td><td>389.14 (n/a)</td><td>302.40 (n/a)</td><td>276.60 (n/a)</td><td>142.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.10 (-13.27%)</td><td>0.06 (-19.99%)</td><td>0.05 <b>(-45.02%)</b></td><td>0.04 <b>(+219.32%)</b></td><td>0.02 <b>(-39.09%)</b></td><td>620.70 <b>(-68.68%)</b></td><td>487.12 <b>(-24.69%)</b></td><td>533.20 <b>(+81.92%)</b></td><td>256.60 (+15.27%)</td><td>137.49 <b>(-81.69%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1981.90 (n/a)</td><td>646.84 (n/a)</td><td>293.10 (n/a)</td><td>222.60 (n/a)</td><td>750.97 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (+1.39%)</td><td>0.05 <b>(+33.22%)</b></td><td>0.06 <b>(+91.47%)</b></td><td>0.03 (-1.65%)</td><td>0.02 <b>(+21.54%)</b></td><td>612.50 (+1.68%)</td><td>379.86 <b>(-20.30%)</b></td><td>262.90 <b>(-47.79%)</b></td><td>235.10 (-1.38%)</td><td>182.42 <b>(+29.97%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>602.40 (n/a)</td><td>476.64 (n/a)</td><td>503.50 (n/a)</td><td>238.40 (n/a)</td><td>140.36 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (-11.92%)</td><td>0.05 (-6.14%)</td><td>0.04 (-19.41%)</td><td>0.04 <b>(+35.21%)</b></td><td>0.01 <b>(-51.22%)</b></td><td>514.20 <b>(-26.05%)</b></td><td>453.22 (-2.69%)</td><td>493.00 <b>(+24.09%)</b></td><td>339.70 (+13.54%)</td><td>73.23 <b>(-59.22%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>695.30 (n/a)</td><td>465.74 (n/a)</td><td>397.30 (n/a)</td><td>299.20 (n/a)</td><td>179.60 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (-2.51%)</td><td>0.05 (-1.10%)</td><td>0.05 (-14.39%)</td><td>0.03 (+19.73%)</td><td>0.01 <b>(-25.29%)</b></td><td>477.30 (-16.48%)</td><td>345.38 (-4.22%)</td><td>325.50 (+16.83%)</td><td>245.80 (+2.54%)</td><td>90.07 <b>(-35.90%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>571.50 (n/a)</td><td>360.60 (n/a)</td><td>278.60 (n/a)</td><td>239.70 (n/a)</td><td>140.51 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 <b>(+32.21%)</b></td><td>0.06 <b>(+38.35%)</b></td><td>0.07 <b>(+64.57%)</b></td><td>0.03 (+2.68%)</td><td>0.02 <b>(+99.19%)</b></td><td>638.60 (-2.61%)</td><td>386.94 <b>(-20.25%)</b></td><td>282.50 <b>(-39.22%)</b></td><td>243.10 <b>(-24.36%)</b></td><td>177.95 <b>(+47.72%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>655.70 (n/a)</td><td>485.18 (n/a)</td><td>464.80 (n/a)</td><td>321.40 (n/a)</td><td>120.46 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (-10.24%)</td><td>0.04 (-11.93%)</td><td>0.03 (-5.87%)</td><td>0.03 (-2.51%)</td><td>0.01 <b>(-23.36%)</b></td><td>654.20 (+2.59%)</td><td>490.94 (+9.62%)</td><td>504.60 (+6.23%)</td><td>297.50 (+11.38%)</td><td>134.83 (-13.19%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>637.70 (n/a)</td><td>447.86 (n/a)</td><td>475.00 (n/a)</td><td>267.10 (n/a)</td><td>155.31 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 <b>(+21.65%)</b></td><td>0.05 (-3.64%)</td><td>0.06 <b>(+25.40%)</b></td><td>0.01 <b>(-62.28%)</b></td><td>0.02 <b>(+182.80%)</b></td><td>1291.80 <b>(+165.09%)</b></td><td>571.12 <b>(+45.05%)</b></td><td>306.70 <b>(-20.25%)</b></td><td>266.60 (-17.79%)</td><td>438.55 <b>(+510.01%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>487.30 (n/a)</td><td>393.74 (n/a)</td><td>384.60 (n/a)</td><td>324.30 (n/a)</td><td>71.89 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 <b>(+69.84%)</b></td><td>0.04 <b>(+70.37%)</b></td><td>0.03 <b>(+37.71%)</b></td><td>0.03 <b>(+279.86%)</b></td><td>0.02 <b>(+30.35%)</b></td><td>641.10 <b>(-73.68%)</b></td><td>440.46 <b>(-56.08%)</b></td><td>505.40 <b>(-27.40%)</b></td><td>223.60 <b>(-41.11%)</b></td><td>169.37 <b>(-79.97%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2435.40 (n/a)</td><td>1002.88 (n/a)</td><td>696.10 (n/a)</td><td>379.70 (n/a)</td><td>845.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 <b>(+54.16%)</b></td><td>0.05 <b>(+45.27%)</b></td><td>0.04 (+8.65%)</td><td>0.04 <b>(+97.28%)</b></td><td>0.02 <b>(+50.96%)</b></td><td>499.90 <b>(-49.31%)</b></td><td>386.80 <b>(-33.06%)</b></td><td>442.00 (-7.96%)</td><td>254.10 <b>(-35.13%)</b></td><td>108.22 <b>(-54.13%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>986.20 (n/a)</td><td>577.82 (n/a)</td><td>480.20 (n/a)</td><td>391.70 (n/a)</td><td>235.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.05 (+11.40%)</td><td>0.04 (+3.85%)</td><td>0.04 (+15.14%)</td><td>0.03 (-13.96%)</td><td>0.01 <b>(+57.43%)</b></td><td>643.00 (+16.23%)</td><td>486.64 (-0.67%)</td><td>466.10 (-13.15%)</td><td>353.30 (-10.24%)</td><td>123.69 <b>(+63.19%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>553.20 (n/a)</td><td>489.94 (n/a)</td><td>536.70 (n/a)</td><td>393.60 (n/a)</td><td>75.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (+8.58%)</td><td>0.10 <b>(+23.04%)</b></td><td>0.11 <b>(+73.38%)</b></td><td>0.03 <b>(-44.15%)</b></td><td>0.04 <b>(+47.12%)</b></td><td>998.60 <b>(+79.06%)</b></td><td>439.64 (-2.32%)</td><td>288.70 <b>(-42.32%)</b></td><td>242.20 (-7.87%)</td><td>316.76 <b>(+169.09%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>557.70 (n/a)</td><td>450.08 (n/a)</td><td>500.50 (n/a)</td><td>262.90 (n/a)</td><td>117.72 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.12 (-15.46%)</td><td>0.07 (-18.58%)</td><td>0.07 (-3.27%)</td><td>0.04 <b>(-38.92%)</b></td><td>0.03 (-8.95%)</td><td>900.90 <b>(+63.71%)</b></td><td>545.76 <b>(+29.36%)</b></td><td>493.60 (+3.39%)</td><td>279.70 (+18.27%)</td><td>246.60 <b>(+71.31%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>550.30 (n/a)</td><td>421.88 (n/a)</td><td>477.40 (n/a)</td><td>236.50 (n/a)</td><td>143.95 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.16 <b>(+62.95%)</b></td><td>0.10 (+18.35%)</td><td>0.08 (-2.84%)</td><td>0.07 <b>(+20.29%)</b></td><td>0.04 <b>(+144.95%)</b></td><td>565.60 (-16.87%)</td><td>456.26 (-11.25%)</td><td>503.60 (+2.92%)</td><td>258.70 <b>(-38.62%)</b></td><td>118.36 (+16.34%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>680.40 (n/a)</td><td>514.12 (n/a)</td><td>489.30 (n/a)</td><td>421.50 (n/a)</td><td>101.73 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 <b>(-21.32%)</b></td><td>0.08 (+0.36%)</td><td>0.08 <b>(+20.21%)</b></td><td>0.04 <b>(-28.99%)</b></td><td>0.02 <b>(-25.21%)</b></td><td>776.90 <b>(+40.84%)</b></td><td>453.54 (+0.35%)</td><td>386.10 (-16.81%)</td><td>303.20 <b>(+27.07%)</b></td><td>187.51 <b>(+46.52%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>551.60 (n/a)</td><td>451.98 (n/a)</td><td>464.10 (n/a)</td><td>238.60 (n/a)</td><td>127.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.17 <b>(+26.58%)</b></td><td>0.10 (-16.01%)</td><td>0.08 <b>(-33.92%)</b></td><td>0.02 <b>(-67.38%)</b></td><td>0.06 <b>(+122.88%)</b></td><td>1797.20 <b>(+206.53%)</b></td><td>690.78 <b>(+82.68%)</b></td><td>487.50 <b>(+51.35%)</b></td><td>237.20 <b>(-20.99%)</b></td><td>638.60 <b>(+436.98%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>586.30 (n/a)</td><td>378.14 (n/a)</td><td>322.10 (n/a)</td><td>300.20 (n/a)</td><td>118.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.13 (-1.19%)</td><td>0.08 <b>(-21.06%)</b></td><td>0.07 <b>(-39.90%)</b></td><td>0.05 <b>(-20.82%)</b></td><td>0.03 (+4.23%)</td><td>620.00 <b>(+26.30%)</b></td><td>458.54 <b>(+28.81%)</b></td><td>482.60 <b>(+66.41%)</b></td><td>252.40 (+1.20%)</td><td>136.80 <b>(+21.27%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>490.90 (n/a)</td><td>355.98 (n/a)</td><td>290.00 (n/a)</td><td>249.40 (n/a)</td><td>112.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.16 (+13.39%)</td><td>0.10 <b>(+21.08%)</b></td><td>0.09 <b>(+22.23%)</b></td><td>0.08 <b>(+23.15%)</b></td><td>0.03 (+3.39%)</td><td>477.80 (-18.80%)</td><td>390.82 (-18.93%)</td><td>421.80 (-18.19%)</td><td>231.90 (-11.79%)</td><td>94.44 <b>(-25.25%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>588.40 (n/a)</td><td>482.10 (n/a)</td><td>515.60 (n/a)</td><td>262.90 (n/a)</td><td>126.35 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 (-9.38%)</td><td>0.06 (-19.56%)</td><td>0.06 (-8.65%)</td><td>0.01 <b>(-78.65%)</b></td><td>0.03 <b>(+46.49%)</b></td><td>2445.30 <b>(+368.45%)</b></td><td>847.62 <b>(+95.76%)</b></td><td>508.10 (+9.48%)</td><td>299.70 (+10.35%)</td><td>897.51 <b>(+838.84%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>522.00 (n/a)</td><td>432.98 (n/a)</td><td>464.10 (n/a)</td><td>271.60 (n/a)</td><td>95.60 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.13 (-15.49%)</td><td>0.09 (-20.00%)</td><td>0.08 <b>(-20.92%)</b></td><td>0.06 (-14.29%)</td><td>0.03 (-18.41%)</td><td>575.40 (+16.67%)</td><td>448.48 <b>(+24.75%)</b></td><td>478.50 <b>(+26.45%)</b></td><td>293.80 (+18.32%)</td><td>123.94 (+18.81%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>493.20 (n/a)</td><td>359.50 (n/a)</td><td>378.40 (n/a)</td><td>248.30 (n/a)</td><td>104.32 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (+15.42%)</td><td>0.08 (+9.43%)</td><td>0.08 (+17.49%)</td><td>0.03 <b>(-44.79%)</b></td><td>0.04 <b>(+56.83%)</b></td><td>1020.50 <b>(+81.13%)</b></td><td>502.90 (+8.21%)</td><td>413.00 (-14.88%)</td><td>237.70 (-13.37%)</td><td>307.46 <b>(+162.62%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>563.40 (n/a)</td><td>464.74 (n/a)</td><td>485.20 (n/a)</td><td>274.40 (n/a)</td><td>117.07 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.10 <b>(+21.18%)</b></td><td>0.07 (+7.39%)</td><td>0.08 (+14.82%)</td><td>0.04 (+4.24%)</td><td>0.03 <b>(+57.50%)</b></td><td>493.40 (-4.06%)</td><td>321.62 (-1.39%)</td><td>250.70 (-12.89%)</td><td>201.50 (-17.49%)</td><td>130.90 <b>(+21.20%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>514.30 (n/a)</td><td>326.14 (n/a)</td><td>287.80 (n/a)</td><td>244.20 (n/a)</td><td>108.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.10 (+17.25%)</td><td>0.07 (+2.88%)</td><td>0.07 (-6.27%)</td><td>0.04 (-1.07%)</td><td>0.02 <b>(+32.30%)</b></td><td>480.90 (+1.07%)</td><td>300.52 (-0.17%)</td><td>290.20 (+6.69%)</td><td>201.20 (-14.75%)</td><td>110.38 (+10.91%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>475.80 (n/a)</td><td>301.02 (n/a)</td><td>272.00 (n/a)</td><td>236.00 (n/a)</td><td>99.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (-14.15%)</td><td>0.05 <b>(-24.11%)</b></td><td>0.05 <b>(-36.42%)</b></td><td>0.04 (+0.13%)</td><td>0.01 <b>(-37.47%)</b></td><td>539.70 (-0.13%)</td><td>444.96 <b>(+24.64%)</b></td><td>441.60 <b>(+57.32%)</b></td><td>290.10 (+16.46%)</td><td>98.23 <b>(-27.11%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>540.40 (n/a)</td><td>357.00 (n/a)</td><td>280.70 (n/a)</td><td>249.10 (n/a)</td><td>134.77 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 <b>(-32.62%)</b></td><td>0.05 (-13.99%)</td><td>0.05 (+2.38%)</td><td>0.04 (+17.73%)</td><td>0.01 <b>(-70.06%)</b></td><td>496.30 (-15.06%)</td><td>404.84 (+0.45%)</td><td>405.00 (-2.34%)</td><td>318.90 <b>(+48.39%)</b></td><td>63.70 <b>(-62.70%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>584.30 (n/a)</td><td>403.04 (n/a)</td><td>414.70 (n/a)</td><td>214.90 (n/a)</td><td>170.78 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (-13.87%)</td><td>0.06 (-3.67%)</td><td>0.07 <b>(+36.98%)</b></td><td>0.04 (-6.70%)</td><td>0.02 (-13.82%)</td><td>537.00 (+7.19%)</td><td>392.80 (+3.62%)</td><td>307.40 <b>(-27.00%)</b></td><td>293.40 (+16.11%)</td><td>129.39 (+12.76%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>501.00 (n/a)</td><td>379.08 (n/a)</td><td>421.10 (n/a)</td><td>252.70 (n/a)</td><td>114.75 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 (+2.46%)</td><td>0.05 (-18.21%)</td><td>0.04 <b>(-33.22%)</b></td><td>0.03 <b>(-22.88%)</b></td><td>0.02 (+19.60%)</td><td>647.40 <b>(+29.66%)</b></td><td>493.82 <b>(+30.38%)</b></td><td>582.80 <b>(+49.74%)</b></td><td>244.80 (-2.39%)</td><td>181.53 <b>(+57.05%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>499.30 (n/a)</td><td>378.74 (n/a)</td><td>389.20 (n/a)</td><td>250.80 (n/a)</td><td>115.59 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 (+15.63%)</td><td>0.08 (-6.10%)</td><td>0.07 (-13.70%)</td><td>0.04 <b>(-28.90%)</b></td><td>0.03 <b>(+113.45%)</b></td><td>566.20 <b>(+40.64%)</b></td><td>372.34 (+18.77%)</td><td>339.20 (+15.89%)</td><td>222.00 (-13.55%)</td><td>152.20 <b>(+156.19%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>402.60 (n/a)</td><td>313.50 (n/a)</td><td>292.70 (n/a)</td><td>256.80 (n/a)</td><td>59.41 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 (-9.48%)</td><td>0.07 <b>(-21.02%)</b></td><td>0.06 <b>(-47.12%)</b></td><td>0.05 (-5.22%)</td><td>0.03 (-17.82%)</td><td>518.70 (+5.51%)</td><td>392.52 <b>(+23.32%)</b></td><td>442.80 <b>(+89.07%)</b></td><td>229.50 (+10.50%)</td><td>127.39 (-4.04%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>491.60 (n/a)</td><td>318.30 (n/a)</td><td>234.20 (n/a)</td><td>207.70 (n/a)</td><td>132.76 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 <b>(-23.55%)</b></td><td>0.06 (-2.35%)</td><td>0.06 (+12.04%)</td><td>0.04 <b>(+336.17%)</b></td><td>0.01 <b>(-62.82%)</b></td><td>565.80 <b>(-77.07%)</b></td><td>444.82 <b>(-45.86%)</b></td><td>436.30 (-10.76%)</td><td>317.00 <b>(+30.83%)</b></td><td>110.58 <b>(-88.20%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2467.80 (n/a)</td><td>821.66 (n/a)</td><td>488.90 (n/a)</td><td>242.30 (n/a)</td><td>936.86 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 <b>(-24.81%)</b></td><td>0.06 <b>(-29.29%)</b></td><td>0.05 <b>(-39.90%)</b></td><td>0.04 (-7.63%)</td><td>0.01 <b>(-47.32%)</b></td><td>584.50 (+8.26%)</td><td>464.76 <b>(+31.99%)</b></td><td>458.90 <b>(+66.39%)</b></td><td>310.60 <b>(+33.02%)</b></td><td>101.89 <b>(-26.67%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>539.90 (n/a)</td><td>352.12 (n/a)</td><td>275.80 (n/a)</td><td>233.50 (n/a)</td><td>138.95 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.10 (-14.75%)</td><td>0.06 <b>(-28.33%)</b></td><td>0.05 <b>(-37.88%)</b></td><td>0.03 <b>(-48.45%)</b></td><td>0.03 <b>(+23.47%)</b></td><td>791.50 <b>(+94.00%)</b></td><td>481.20 <b>(+57.11%)</b></td><td>455.30 <b>(+61.00%)</b></td><td>249.90 (+17.32%)</td><td>222.07 <b>(+169.40%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>408.00 (n/a)</td><td>306.28 (n/a)</td><td>282.80 (n/a)</td><td>213.00 (n/a)</td><td>82.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (-19.68%)</td><td>0.05 (-14.66%)</td><td>0.05 (-16.66%)</td><td>0.04 (-13.06%)</td><td>0.01 <b>(-23.52%)</b></td><td>563.70 (+15.02%)</td><td>486.74 (+16.55%)</td><td>539.40 (+20.00%)</td><td>359.60 <b>(+24.52%)</b></td><td>93.85 (+11.63%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>490.10 (n/a)</td><td>417.62 (n/a)</td><td>449.50 (n/a)</td><td>288.80 (n/a)</td><td>84.07 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 (-2.37%)</td><td>0.05 <b>(+30.16%)</b></td><td>0.04 <b>(+24.12%)</b></td><td>0.04 <b>(+320.46%)</b></td><td>0.01 <b>(-38.95%)</b></td><td>476.00 <b>(-76.22%)</b></td><td>384.52 <b>(-48.99%)</b></td><td>416.50 (-19.44%)</td><td>244.80 (+2.43%)</td><td>92.30 <b>(-86.95%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2001.50 (n/a)</td><td>753.78 (n/a)</td><td>517.00 (n/a)</td><td>239.00 (n/a)</td><td>707.32 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 (+2.07%)</td><td>0.06 (-10.21%)</td><td>0.08 (+5.83%)</td><td>0.03 <b>(-30.32%)</b></td><td>0.02 <b>(+88.50%)</b></td><td>594.00 <b>(+43.51%)</b></td><td>365.94 <b>(+26.81%)</b></td><td>240.50 (-5.54%)</td><td>235.70 (-2.04%)</td><td>176.14 <b>(+146.55%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>413.90 (n/a)</td><td>288.58 (n/a)</td><td>254.60 (n/a)</td><td>240.60 (n/a)</td><td>71.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 <b>(-21.66%)</b></td><td>0.04 <b>(-20.72%)</b></td><td>0.04 (-5.05%)</td><td>0.03 (-19.92%)</td><td>0.01 <b>(-29.14%)</b></td><td>637.10 <b>(+24.87%)</b></td><td>481.32 <b>(+23.68%)</b></td><td>473.40 (+5.32%)</td><td>293.80 <b>(+27.63%)</b></td><td>130.13 (+10.47%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>510.20 (n/a)</td><td>389.16 (n/a)</td><td>449.50 (n/a)</td><td>230.20 (n/a)</td><td>117.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 (-16.38%)</td><td>0.04 (-11.66%)</td><td>0.03 (-12.71%)</td><td>0.03 (-8.97%)</td><td>0.02 (-15.34%)</td><td>718.00 (+9.85%)</td><td>481.98 (+12.21%)</td><td>555.80 (+14.57%)</td><td>259.80 (+19.61%)</td><td>194.78 (+9.66%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>653.60 (n/a)</td><td>429.52 (n/a)</td><td>485.10 (n/a)</td><td>217.20 (n/a)</td><td>177.63 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.06 (-19.06%)</td><td>0.05 (+6.54%)</td><td>0.06 <b>(+39.38%)</b></td><td>0.03 (-9.88%)</td><td>0.01 (-18.10%)</td><td>553.50 (+10.94%)</td><td>395.44 (-6.49%)</td><td>330.90 <b>(-28.25%)</b></td><td>300.10 <b>(+23.55%)</b></td><td>118.41 (+15.60%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>498.90 (n/a)</td><td>422.88 (n/a)</td><td>461.20 (n/a)</td><td>242.90 (n/a)</td><td>102.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 <b>(+47.03%)</b></td><td>0.04 (+2.93%)</td><td>0.03 (-2.67%)</td><td>0.01 <b>(-51.88%)</b></td><td>0.02 <b>(+225.09%)</b></td><td>1289.70 <b>(+107.82%)</b></td><td>627.82 <b>(+21.18%)</b></td><td>533.10 (+2.74%)</td><td>275.70 <b>(-31.98%)</b></td><td>385.57 <b>(+396.01%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>620.60 (n/a)</td><td>518.10 (n/a)</td><td>518.90 (n/a)</td><td>405.30 (n/a)</td><td>77.73 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.36 (-10.07%)</td><td>0.22 <b>(-22.66%)</b></td><td>0.21 (-18.64%)</td><td>0.04 <b>(-78.22%)</b></td><td>0.12 <b>(+37.66%)</b></td><td>2502.10 <b>(+359.19%)</b></td><td>807.20 <b>(+119.79%)</b></td><td>457.60 <b>(+22.91%)</b></td><td>271.20 (+11.19%)</td><td>951.18 <b>(+710.08%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>544.90 (n/a)</td><td>367.26 (n/a)</td><td>372.30 (n/a)</td><td>243.90 (n/a)</td><td>117.42 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.34 <b>(-25.31%)</b></td><td>0.20 <b>(-20.54%)</b></td><td>0.20 (-12.02%)</td><td>0.04 <b>(-75.63%)</b></td><td>0.11 (-9.38%)</td><td>2452.50 <b>(+310.32%)</b></td><td>842.08 <b>(+87.14%)</b></td><td>495.70 (+13.67%)</td><td>287.00 <b>(+33.86%)</b></td><td>905.81 <b>(+496.82%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.46 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>597.70 (n/a)</td><td>449.98 (n/a)</td><td>436.10 (n/a)</td><td>214.40 (n/a)</td><td>151.77 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.49 <b>(+48.21%)</b></td><td>0.28 <b>(+24.30%)</b></td><td>0.20 (+10.87%)</td><td>0.16 <b>(+20.42%)</b></td><td>0.15 <b>(+62.92%)</b></td><td>628.30 (-16.96%)</td><td>423.42 (-13.64%)</td><td>486.90 (-9.80%)</td><td>201.50 <b>(-32.54%)</b></td><td>188.01 (-2.07%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>756.60 (n/a)</td><td>490.32 (n/a)</td><td>539.80 (n/a)</td><td>298.70 (n/a)</td><td>191.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.36 <b>(+24.42%)</b></td><td>0.26 (+18.75%)</td><td>0.24 (-1.27%)</td><td>0.13 <b>(+28.93%)</b></td><td>0.08 (+3.78%)</td><td>549.60 <b>(-22.44%)</b></td><td>322.20 (-19.30%)</td><td>302.40 (+1.31%)</td><td>206.20 (-19.61%)</td><td>134.90 <b>(-30.55%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>708.60 (n/a)</td><td>399.26 (n/a)</td><td>298.50 (n/a)</td><td>256.50 (n/a)</td><td>194.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.28 (-8.52%)</td><td>0.14 (-13.31%)</td><td>0.13 (-10.32%)</td><td>0.04 (+5.21%)</td><td>0.09 <b>(-33.43%)</b></td><td>1904.20 (-4.95%)</td><td>773.30 <b>(-21.32%)</b></td><td>554.70 (+11.52%)</td><td>263.30 (+9.30%)</td><td>646.46 <b>(-28.11%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.31 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.13 (n/a)</td><td>2003.30 (n/a)</td><td>982.80 (n/a)</td><td>497.40 (n/a)</td><td>240.90 (n/a)</td><td>899.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.27 (-4.59%)</td><td>0.19 (+1.59%)</td><td>0.15 (-10.11%)</td><td>0.12 (-8.07%)</td><td>0.07 (+14.98%)</td><td>590.50 (+8.79%)</td><td>435.82 (+1.93%)</td><td>506.90 (+11.26%)</td><td>268.40 (+4.80%)</td><td>145.73 <b>(+31.19%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>542.80 (n/a)</td><td>427.58 (n/a)</td><td>455.60 (n/a)</td><td>256.10 (n/a)</td><td>111.08 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (+12.53%)</td><td>0.09 (-6.44%)</td><td>0.08 <b>(-30.52%)</b></td><td>0.06 (-16.05%)</td><td>0.04 <b>(+62.98%)</b></td><td>567.50 (+19.12%)</td><td>433.18 (+14.10%)</td><td>489.80 <b>(+43.93%)</b></td><td>271.20 (-11.14%)</td><td>145.27 <b>(+67.94%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>476.40 (n/a)</td><td>379.64 (n/a)</td><td>340.30 (n/a)</td><td>305.20 (n/a)</td><td>86.50 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.08 <b>(-52.47%)</b></td><td>0.07 <b>(-26.50%)</b></td><td>0.07 (-1.67%)</td><td>0.06 (+12.13%)</td><td>0.01 <b>(-86.06%)</b></td><td>574.50 (-10.81%)</td><td>502.14 (+15.55%)</td><td>497.10 (+1.70%)</td><td>441.00 <b>(+110.40%)</b></td><td>47.81 <b>(-73.28%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>644.10 (n/a)</td><td>434.56 (n/a)</td><td>488.80 (n/a)</td><td>209.60 (n/a)</td><td>178.92 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.13 (-18.69%)</td><td>0.08 <b>(-25.24%)</b></td><td>0.08 <b>(-30.08%)</b></td><td>0.03 <b>(-40.51%)</b></td><td>0.03 (-19.54%)</td><td>1087.40 <b>(+68.09%)</b></td><td>561.56 <b>(+39.39%)</b></td><td>483.40 <b>(+43.02%)</b></td><td>286.70 <b>(+22.94%)</b></td><td>305.68 <b>(+76.11%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>646.90 (n/a)</td><td>402.88 (n/a)</td><td>338.00 (n/a)</td><td>233.20 (n/a)</td><td>173.57 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.16 (+2.66%)</td><td>0.10 (-3.65%)</td><td>0.09 <b>(+23.04%)</b></td><td>0.06 (-5.73%)</td><td>0.04 (-15.31%)</td><td>643.90 (+6.08%)</td><td>432.22 (-0.66%)</td><td>404.80 (-18.73%)</td><td>228.40 (-2.60%)</td><td>165.69 (-9.69%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>607.00 (n/a)</td><td>435.08 (n/a)</td><td>498.10 (n/a)</td><td>234.50 (n/a)</td><td>183.46 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.16 <b>(+61.99%)</b></td><td>0.09 <b>(+37.42%)</b></td><td>0.08 (+19.46%)</td><td>0.03 <b>(-37.43%)</b></td><td>0.05 <b>(+197.18%)</b></td><td>1129.80 <b>(+59.82%)</b></td><td>538.84 (-3.96%)</td><td>480.80 (-16.30%)</td><td>230.30 <b>(-38.27%)</b></td><td>363.91 <b>(+183.58%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>706.90 (n/a)</td><td>561.04 (n/a)</td><td>574.40 (n/a)</td><td>373.10 (n/a)</td><td>128.33 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.17 <b>(+28.28%)</b></td><td>0.12 <b>(+49.55%)</b></td><td>0.13 <b>(+62.44%)</b></td><td>0.07 <b>(+95.22%)</b></td><td>0.04 (+18.04%)</td><td>559.80 <b>(-48.77%)</b></td><td>354.38 <b>(-38.04%)</b></td><td>287.10 <b>(-38.43%)</b></td><td>221.40 <b>(-22.04%)</b></td><td>141.75 <b>(-54.33%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1092.80 (n/a)</td><td>571.98 (n/a)</td><td>466.30 (n/a)</td><td>284.00 (n/a)</td><td>310.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (-4.86%)</td><td>0.09 (-11.66%)</td><td>0.09 (+4.53%)</td><td>0.07 (+8.31%)</td><td>0.03 <b>(-28.90%)</b></td><td>569.60 (-7.67%)</td><td>475.82 (+7.76%)</td><td>472.70 (-4.33%)</td><td>297.30 (+5.13%)</td><td>110.85 <b>(-26.52%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>616.90 (n/a)</td><td>441.54 (n/a)</td><td>494.10 (n/a)</td><td>282.80 (n/a)</td><td>150.87 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 <b>(-23.03%)</b></td><td>0.12 (+17.21%)</td><td>0.11 <b>(+46.26%)</b></td><td>0.09 <b>(+42.12%)</b></td><td>0.02 <b>(-60.72%)</b></td><td>453.90 <b>(-29.64%)</b></td><td>363.18 <b>(-24.58%)</b></td><td>366.20 <b>(-31.63%)</b></td><td>291.20 <b>(+29.88%)</b></td><td>62.33 <b>(-63.27%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>645.10 (n/a)</td><td>481.54 (n/a)</td><td>535.60 (n/a)</td><td>224.20 (n/a)</td><td>169.73 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (-19.26%)</td><td>0.10 <b>(-34.98%)</b></td><td>0.08 <b>(-48.69%)</b></td><td>0.07 (-15.94%)</td><td>0.03 (-17.56%)</td><td>549.20 (+18.98%)</td><td>446.70 <b>(+53.52%)</b></td><td>498.90 <b>(+94.88%)</b></td><td>291.00 <b>(+23.88%)</b></td><td>113.49 (+18.45%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>461.60 (n/a)</td><td>290.98 (n/a)</td><td>256.00 (n/a)</td><td>234.90 (n/a)</td><td>95.81 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.16 (-6.60%)</td><td>0.11 (-15.06%)</td><td>0.11 (-6.69%)</td><td>0.07 (-9.09%)</td><td>0.04 (-1.63%)</td><td>599.80 (+10.01%)</td><td>418.02 <b>(+20.07%)</b></td><td>372.90 (+7.16%)</td><td>255.90 (+7.07%)</td><td>152.90 <b>(+23.87%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>545.20 (n/a)</td><td>348.16 (n/a)</td><td>348.00 (n/a)</td><td>239.00 (n/a)</td><td>123.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (-5.23%)</td><td>0.09 (-7.78%)</td><td>0.08 (-5.03%)</td><td>0.06 (+0.29%)</td><td>0.03 <b>(-24.71%)</b></td><td>630.40 (-0.28%)</td><td>472.76 (+3.52%)</td><td>505.90 (+5.31%)</td><td>294.60 (+5.52%)</td><td>132.30 <b>(-20.16%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>632.20 (n/a)</td><td>456.70 (n/a)</td><td>480.40 (n/a)</td><td>279.20 (n/a)</td><td>165.70 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.16 (-2.78%)</td><td>0.09 (-10.24%)</td><td>0.10 <b>(-33.70%)</b></td><td>0.02 (-13.15%)</td><td>0.06 <b>(-28.34%)</b></td><td>2419.60 (+15.15%)</td><td>804.14 (-16.03%)</td><td>401.40 <b>(+50.85%)</b></td><td>252.70 (+2.85%)</td><td>913.33 (-5.46%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.08 (n/a)</td><td>2101.30 (n/a)</td><td>957.70 (n/a)</td><td>266.10 (n/a)</td><td>245.70 (n/a)</td><td>966.10 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.17 (+17.86%)</td><td>0.11 (+7.38%)</td><td>0.11 <b>(+35.02%)</b></td><td>0.07 <b>(+24.49%)</b></td><td>0.04 (-0.40%)</td><td>513.90 (-19.67%)</td><td>370.70 (-9.55%)</td><td>319.70 <b>(-25.94%)</b></td><td>204.90 (-15.16%)</td><td>137.22 (-19.62%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>639.70 (n/a)</td><td>409.86 (n/a)</td><td>431.70 (n/a)</td><td>241.50 (n/a)</td><td>170.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (-13.35%)</td><td>0.08 <b>(-32.47%)</b></td><td>0.07 <b>(-37.76%)</b></td><td>0.06 (-19.41%)</td><td>0.03 (+2.78%)</td><td>604.80 <b>(+24.06%)</b></td><td>472.32 <b>(+52.29%)</b></td><td>468.00 <b>(+60.66%)</b></td><td>246.70 (+15.39%)</td><td>141.12 <b>(+34.75%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>487.50 (n/a)</td><td>310.14 (n/a)</td><td>291.30 (n/a)</td><td>213.80 (n/a)</td><td>104.73 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.12 (-13.38%)</td><td>0.07 (-19.35%)</td><td>0.07 (-16.55%)</td><td>0.06 (-4.33%)</td><td>0.03 <b>(-22.00%)</b></td><td>607.20 (+4.53%)</td><td>497.96 <b>(+20.86%)</b></td><td>525.40 (+19.84%)</td><td>291.40 (+15.45%)</td><td>121.94 (-9.08%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>580.90 (n/a)</td><td>412.00 (n/a)</td><td>438.40 (n/a)</td><td>252.40 (n/a)</td><td>134.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.13 <b>(-25.69%)</b></td><td>0.10 (-15.04%)</td><td>0.11 (-6.86%)</td><td>0.08 (+14.67%)</td><td>0.02 <b>(-48.03%)</b></td><td>447.10 (-12.80%)</td><td>351.62 (+9.29%)</td><td>319.00 (+7.37%)</td><td>278.50 <b>(+34.61%)</b></td><td>80.65 <b>(-36.30%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>512.70 (n/a)</td><td>321.72 (n/a)</td><td>297.10 (n/a)</td><td>206.90 (n/a)</td><td>126.61 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.12 (-10.76%)</td><td>0.09 (-2.52%)</td><td>0.08 (+10.04%)</td><td>0.06 (+12.44%)</td><td>0.03 <b>(-26.90%)</b></td><td>622.40 (-11.06%)</td><td>434.88 (-2.93%)</td><td>414.30 (-9.12%)</td><td>302.40 (+12.04%)</td><td>134.91 <b>(-24.51%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>699.80 (n/a)</td><td>448.00 (n/a)</td><td>455.90 (n/a)</td><td>269.90 (n/a)</td><td>178.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.12 (+8.46%)</td><td>0.08 (+9.34%)</td><td>0.07 (+11.95%)</td><td>0.05 (+2.11%)</td><td>0.03 (+12.67%)</td><td>718.30 (-2.07%)</td><td>490.10 (-7.42%)</td><td>480.50 (-10.67%)</td><td>290.60 (-7.78%)</td><td>167.13 (+2.37%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>733.50 (n/a)</td><td>529.40 (n/a)</td><td>537.90 (n/a)</td><td>315.10 (n/a)</td><td>163.26 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.47 (-4.21%)</td><td>0.36 (+6.29%)</td><td>0.38 <b>(+27.18%)</b></td><td>0.25 <b>(+21.68%)</b></td><td>0.08 <b>(-29.05%)</b></td><td>516.40 (-17.81%)</td><td>385.18 (-10.78%)</td><td>346.90 <b>(-21.36%)</b></td><td>280.60 (+4.39%)</td><td>94.38 <b>(-36.42%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>628.30 (n/a)</td><td>431.72 (n/a)</td><td>441.10 (n/a)</td><td>268.80 (n/a)</td><td>148.43 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.51 (+18.10%)</td><td>0.31 (-1.15%)</td><td>0.26 (-17.20%)</td><td>0.05 <b>(-70.15%)</b></td><td>0.18 <b>(+77.42%)</b></td><td>2452.70 <b>(+234.98%)</b></td><td>805.72 <b>(+72.27%)</b></td><td>506.70 <b>(+20.79%)</b></td><td>259.10 (-15.33%)</td><td>929.26 <b>(+428.80%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.43 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>732.20 (n/a)</td><td>467.72 (n/a)</td><td>419.50 (n/a)</td><td>306.00 (n/a)</td><td>175.73 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.43 (-10.58%)</td><td>0.27 <b>(-26.50%)</b></td><td>0.30 <b>(-26.94%)</b></td><td>0.05 <b>(-77.96%)</b></td><td>0.14 <b>(+23.27%)</b></td><td>2427.60 <b>(+353.76%)</b></td><td>823.66 <b>(+111.14%)</b></td><td>443.20 <b>(+36.87%)</b></td><td>301.80 (+11.82%)</td><td>899.93 <b>(+595.73%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.49 (n/a)</td><td>0.37 (n/a)</td><td>0.40 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>535.00 (n/a)</td><td>390.10 (n/a)</td><td>323.80 (n/a)</td><td>269.90 (n/a)</td><td>129.35 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 <b>(-26.63%)</b></td><td>0.01 <b>(-39.71%)</b></td><td>0.01 <b>(-39.20%)</b></td><td>0.00 <b>(-58.66%)</b></td><td>0.00 (-6.74%)</td><td>911.50 <b>(+141.91%)</b></td><td>520.16 <b>(+82.88%)</b></td><td>387.50 <b>(+64.47%)</b></td><td>303.10 <b>(+36.29%)</b></td><td>248.94 <b>(+214.88%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>376.80 (n/a)</td><td>284.42 (n/a)</td><td>235.60 (n/a)</td><td>222.40 (n/a)</td><td>79.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 <b>(-26.07%)</b></td><td>0.01 (-8.64%)</td><td>0.01 <b>(-21.14%)</b></td><td>0.01 (+17.46%)</td><td>0.00 <b>(-51.47%)</b></td><td>478.30 (-14.86%)</td><td>342.16 (-2.07%)</td><td>325.10 <b>(+26.79%)</b></td><td>273.80 <b>(+35.28%)</b></td><td>84.03 <b>(-46.83%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.80 (n/a)</td><td>349.38 (n/a)</td><td>256.40 (n/a)</td><td>202.40 (n/a)</td><td>158.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 <b>(-45.10%)</b></td><td>0.01 <b>(-41.14%)</b></td><td>0.01 <b>(-40.99%)</b></td><td>0.00 <b>(-33.11%)</b></td><td>0.00 <b>(-49.09%)</b></td><td>989.90 <b>(+49.49%)</b></td><td>530.42 <b>(+61.55%)</b></td><td>453.40 <b>(+69.43%)</b></td><td>311.50 <b>(+82.16%)</b></td><td>264.02 <b>(+37.82%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>662.20 (n/a)</td><td>328.34 (n/a)</td><td>267.60 (n/a)</td><td>171.00 (n/a)</td><td>191.58 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>7.76 (-17.63%)</td><td>5.61 <b>(-30.65%)</b></td><td>5.80 <b>(-34.79%)</b></td><td>3.84 <b>(-31.20%)</b></td><td>1.51 (-8.22%)</td><td>546.60 <b>(+45.33%)</b></td><td>396.46 <b>(+46.93%)</b></td><td>361.60 <b>(+53.35%)</b></td><td>270.30 <b>(+21.37%)</b></td><td>107.37 <b>(+65.17%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>9.42 (n/a)</td><td>8.09 (n/a)</td><td>8.90 (n/a)</td><td>5.58 (n/a)</td><td>1.64 (n/a)</td><td>376.10 (n/a)</td><td>269.82 (n/a)</td><td>235.80 (n/a)</td><td>222.70 (n/a)</td><td>65.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.49 (-17.84%)</td><td>0.37 (-16.41%)</td><td>0.35 <b>(-25.37%)</b></td><td>0.25 (+11.93%)</td><td>0.10 <b>(-37.43%)</b></td><td>530.00 (-10.67%)</td><td>377.00 (+10.91%)</td><td>380.10 <b>(+33.98%)</b></td><td>266.90 <b>(+21.71%)</b></td><td>106.31 <b>(-31.81%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.60 (n/a)</td><td>0.45 (n/a)</td><td>0.47 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>593.30 (n/a)</td><td>339.92 (n/a)</td><td>283.70 (n/a)</td><td>219.30 (n/a)</td><td>155.89 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.50 (+0.73%)</td><td>0.39 (+4.52%)</td><td>0.42 (+2.04%)</td><td>0.21 (-11.15%)</td><td>0.12 (+12.40%)</td><td>641.90 (+12.55%)</td><td>376.10 (-1.57%)</td><td>316.10 (-1.98%)</td><td>266.60 (-0.71%)</td><td>156.05 <b>(+24.84%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.49 (n/a)</td><td>0.37 (n/a)</td><td>0.41 (n/a)</td><td>0.23 (n/a)</td><td>0.11 (n/a)</td><td>570.30 (n/a)</td><td>382.10 (n/a)</td><td>322.50 (n/a)</td><td>268.50 (n/a)</td><td>125.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.44 <b>(-44.56%)</b></td><td>0.33 <b>(-29.16%)</b></td><td>0.32 (-11.43%)</td><td>0.24 <b>(-23.35%)</b></td><td>0.07 <b>(-63.57%)</b></td><td>549.40 <b>(+30.47%)</b></td><td>417.34 <b>(+30.10%)</b></td><td>410.40 (+12.90%)</td><td>303.40 <b>(+80.38%)</b></td><td>91.48 (-15.66%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.79 (n/a)</td><td>0.46 (n/a)</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>421.10 (n/a)</td><td>320.78 (n/a)</td><td>363.50 (n/a)</td><td>168.20 (n/a)</td><td>108.46 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.44 <b>(-38.50%)</b></td><td>0.34 <b>(-22.32%)</b></td><td>0.37 (+13.93%)</td><td>0.24 (-7.51%)</td><td>0.09 <b>(-52.03%)</b></td><td>555.20 (+8.12%)</td><td>415.22 (+18.80%)</td><td>355.50 (-12.24%)</td><td>303.00 <b>(+62.64%)</b></td><td>123.58 (-10.24%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.71 (n/a)</td><td>0.44 (n/a)</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>513.50 (n/a)</td><td>349.52 (n/a)</td><td>405.10 (n/a)</td><td>186.30 (n/a)</td><td>137.68 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.57 (-19.90%)</td><td>0.49 (+9.86%)</td><td>0.55 (+11.50%)</td><td>0.37 <b>(+43.28%)</b></td><td>0.10 <b>(-49.84%)</b></td><td>358.90 <b>(-30.20%)</b></td><td>279.54 (-19.47%)</td><td>241.20 (-10.30%)</td><td>233.10 <b>(+24.85%)</b></td><td>59.31 <b>(-60.94%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.71 (n/a)</td><td>0.44 (n/a)</td><td>0.49 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>514.20 (n/a)</td><td>347.12 (n/a)</td><td>268.90 (n/a)</td><td>186.70 (n/a)</td><td>151.86 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.02 (-2.77%)</td><td>0.01 (-16.55%)</td><td>0.01 <b>(-46.51%)</b></td><td>0.01 <b>(-20.31%)</b></td><td>0.01 <b>(+28.04%)</b></td><td>538.40 <b>(+25.47%)</b></td><td>397.50 <b>(+28.28%)</b></td><td>479.70 <b>(+86.94%)</b></td><td>227.50 (+2.85%)</td><td>150.15 <b>(+56.86%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>429.10 (n/a)</td><td>309.88 (n/a)</td><td>256.60 (n/a)</td><td>221.20 (n/a)</td><td>95.72 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.01 <b>(-39.25%)</b></td><td>0.01 <b>(-35.93%)</b></td><td>0.01 <b>(-36.88%)</b></td><td>0.01 <b>(-23.41%)</b></td><td>0.00 <b>(-45.52%)</b></td><td>632.50 <b>(+30.57%)</b></td><td>446.92 <b>(+50.53%)</b></td><td>445.70 <b>(+58.44%)</b></td><td>293.80 <b>(+64.59%)</b></td><td>127.17 (+12.39%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>484.40 (n/a)</td><td>296.90 (n/a)</td><td>281.30 (n/a)</td><td>178.50 (n/a)</td><td>113.16 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.00 <b>(-25.00%)</b></td><td>0.00 <b>(-41.38%)</b></td><td>0.00 <b>(-66.67%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-14.51%)</td><td>20874.38 (+14.60%)</td><td>14549.75 <b>(+72.05%)</b></td><td>17768.37 <b>(+177.51%)</b></td><td>6835.48 <b>(+26.93%)</b></td><td>6400.23 (+16.67%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18214.36 (n/a)</td><td>8456.72 (n/a)</td><td>6402.69 (n/a)</td><td>5385.15 (n/a)</td><td>5485.63 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.00 (+7.69%)</td><td>0.00 <b>(-29.79%)</b></td><td>0.00 <b>(-58.33%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-7.68%)</td><td>20276.01 (+2.56%)</td><td>15412.28 <b>(+35.93%)</b></td><td>17324.51 <b>(+148.42%)</b></td><td>5904.51 (-3.42%)</td><td>5545.90 (-16.38%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19769.92 (n/a)</td><td>11338.18 (n/a)</td><td>6973.77 (n/a)</td><td>6113.42 (n/a)</td><td>6631.96 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (+0.58%)</td><td>0.12 (+14.49%)</td><td>0.13 <b>(+37.65%)</b></td><td>0.09 (+19.49%)</td><td>0.02 <b>(-32.51%)</b></td><td>23442.93 (-16.24%)</td><td>18302.71 (-16.13%)</td><td>16728.60 <b>(-27.30%)</b></td><td>15210.19 (-0.53%)</td><td>3485.84 <b>(-42.74%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>27989.25 (n/a)</td><td>21823.89 (n/a)</td><td>23010.13 (n/a)</td><td>15291.23 (n/a)</td><td>6088.02 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.15 (+19.20%)</td><td>0.12 <b>(+34.16%)</b></td><td>0.12 <b>(+48.42%)</b></td><td>0.07 (-3.20%)</td><td>0.03 <b>(+30.09%)</b></td><td>30184.69 (+3.34%)</td><td>19029.96 <b>(-23.56%)</b></td><td>17187.59 <b>(-32.63%)</b></td><td>13562.15 (-16.13%)</td><td>6467.86 <b>(+22.12%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>29207.81 (n/a)</td><td>24893.67 (n/a)</td><td>25512.42 (n/a)</td><td>16170.02 (n/a)</td><td>5296.16 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>1.89 <b>(-25.44%)</b></td><td>1.19 (-12.45%)</td><td>1.50 (+19.26%)</td><td>0.29 (-2.18%)</td><td>0.72 (-12.47%)</td><td>3556.20 (+2.23%)</td><td>1465.44 (+15.12%)</td><td>699.20 (-16.14%)</td><td>554.80 <b>(+34.14%)</b></td><td>1295.66 (+3.40%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.53 (n/a)</td><td>1.36 (n/a)</td><td>1.26 (n/a)</td><td>0.30 (n/a)</td><td>0.82 (n/a)</td><td>3478.50 (n/a)</td><td>1272.96 (n/a)</td><td>833.80 (n/a)</td><td>413.60 (n/a)</td><td>1253.02 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>2.72 (-13.72%)</td><td>1.99 (-10.28%)</td><td>2.03 <b>(-21.38%)</b></td><td>1.15 <b>(+45.46%)</b></td><td>0.67 <b>(-29.76%)</b></td><td>908.50 <b>(-31.25%)</b></td><td>584.04 (-3.74%)</td><td>516.70 <b>(+27.17%)</b></td><td>385.00 (+15.89%)</td><td>219.98 <b>(-46.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.16 (n/a)</td><td>2.22 (n/a)</td><td>2.58 (n/a)</td><td>0.79 (n/a)</td><td>0.96 (n/a)</td><td>1321.40 (n/a)</td><td>606.72 (n/a)</td><td>406.30 (n/a)</td><td>332.20 (n/a)</td><td>413.18 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>1.60 <b>(-52.17%)</b></td><td>1.37 <b>(-38.26%)</b></td><td>1.43 <b>(-41.57%)</b></td><td>0.98 <b>(+25.66%)</b></td><td>0.23 <b>(-77.20%)</b></td><td>1073.30 <b>(-20.42%)</b></td><td>786.36 <b>(+27.09%)</b></td><td>732.90 <b>(+71.16%)</b></td><td>654.90 <b>(+109.10%)</b></td><td>164.46 <b>(-61.50%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.35 (n/a)</td><td>2.22 (n/a)</td><td>2.45 (n/a)</td><td>0.78 (n/a)</td><td>1.03 (n/a)</td><td>1348.70 (n/a)</td><td>618.74 (n/a)</td><td>428.20 (n/a)</td><td>313.20 (n/a)</td><td>427.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>2.99 <b>(-33.80%)</b></td><td>2.22 (+0.66%)</td><td>2.08 (+9.64%)</td><td>1.69 <b>(+164.51%)</b></td><td>0.55 <b>(-61.27%)</b></td><td>620.40 <b>(-62.20%)</b></td><td>494.36 <b>(-29.01%)</b></td><td>503.00 (-8.79%)</td><td>350.40 <b>(+51.03%)</b></td><td>114.76 <b>(-78.93%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>4.52 (n/a)</td><td>2.21 (n/a)</td><td>1.90 (n/a)</td><td>0.64 (n/a)</td><td>1.42 (n/a)</td><td>1641.10 (n/a)</td><td>696.34 (n/a)</td><td>551.50 (n/a)</td><td>232.00 (n/a)</td><td>544.66 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>3.45 (+10.11%)</td><td>2.32 (+2.60%)</td><td>3.30 <b>(+32.15%)</b></td><td>0.59 (+4.38%)</td><td>1.42 <b>(+41.35%)</b></td><td>3533.70 (-4.20%)</td><td>1517.08 (+10.67%)</td><td>635.50 <b>(-24.33%)</b></td><td>607.20 (-9.18%)</td><td>1311.98 (+0.98%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.14 (n/a)</td><td>2.27 (n/a)</td><td>2.50 (n/a)</td><td>0.57 (n/a)</td><td>1.00 (n/a)</td><td>3688.60 (n/a)</td><td>1370.84 (n/a)</td><td>839.80 (n/a)</td><td>668.60 (n/a)</td><td>1299.20 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>3.69 <b>(-23.29%)</b></td><td>2.38 <b>(-39.15%)</b></td><td>2.58 <b>(-38.59%)</b></td><td>0.98 <b>(-67.21%)</b></td><td>1.11 <b>(+45.35%)</b></td><td>2136.40 <b>(+204.94%)</b></td><td>1107.54 <b>(+100.25%)</b></td><td>814.10 <b>(+62.82%)</b></td><td>568.20 <b>(+30.38%)</b></td><td>647.59 <b>(+473.44%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>4.81 (n/a)</td><td>3.92 (n/a)</td><td>4.19 (n/a)</td><td>2.99 (n/a)</td><td>0.76 (n/a)</td><td>700.60 (n/a)</td><td>553.08 (n/a)</td><td>500.00 (n/a)</td><td>435.80 (n/a)</td><td>112.93 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>3.77 (-13.31%)</td><td>2.67 (-5.48%)</td><td>2.96 (-4.13%)</td><td>0.60 <b>(-27.75%)</b></td><td>1.22 (-11.20%)</td><td>3470.90 <b>(+38.40%)</b></td><td>1229.00 (+17.89%)</td><td>707.70 (+4.30%)</td><td>555.60 (+15.37%)</td><td>1255.94 <b>(+49.48%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>4.35 (n/a)</td><td>2.82 (n/a)</td><td>3.09 (n/a)</td><td>0.84 (n/a)</td><td>1.38 (n/a)</td><td>2507.80 (n/a)</td><td>1042.46 (n/a)</td><td>678.50 (n/a)</td><td>481.60 (n/a)</td><td>840.21 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>5.02 (-16.73%)</td><td>2.47 <b>(-35.78%)</b></td><td>2.04 <b>(-41.14%)</b></td><td>0.59 <b>(-78.91%)</b></td><td>2.02 <b>(+57.98%)</b></td><td>3542.40 <b>(+374.09%)</b></td><td>1806.60 <b>(+208.59%)</b></td><td>1029.30 <b>(+69.91%)</b></td><td>417.60 <b>(+20.10%)</b></td><td>1596.61 <b>(+948.22%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>6.03 (n/a)</td><td>3.84 (n/a)</td><td>3.46 (n/a)</td><td>2.81 (n/a)</td><td>1.28 (n/a)</td><td>747.20 (n/a)</td><td>585.44 (n/a)</td><td>605.80 (n/a)</td><td>347.70 (n/a)</td><td>152.32 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>5.23 (-18.54%)</td><td>3.77 <b>(+43.29%)</b></td><td>4.07 <b>(+133.18%)</b></td><td>1.81 <b>(+209.34%)</b></td><td>1.24 <b>(-50.21%)</b></td><td>1156.90 <b>(-67.67%)</b></td><td>631.48 <b>(-65.44%)</b></td><td>515.70 <b>(-57.11%)</b></td><td>401.40 <b>(+22.75%)</b></td><td>300.11 <b>(-81.09%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>6.41 (n/a)</td><td>2.63 (n/a)</td><td>1.74 (n/a)</td><td>0.59 (n/a)</td><td>2.49 (n/a)</td><td>3578.80 (n/a)</td><td>1827.06 (n/a)</td><td>1202.50 (n/a)</td><td>327.00 (n/a)</td><td>1586.64 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>6.11 (-3.74%)</td><td>3.77 (+9.86%)</td><td>4.10 (+7.56%)</td><td>0.86 <b>(-25.29%)</b></td><td>2.11 (+2.98%)</td><td>2428.10 <b>(+33.86%)</b></td><td>902.14 (+3.27%)</td><td>511.20 (-7.02%)</td><td>343.30 (+3.87%)</td><td>873.66 <b>(+43.16%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>6.34 (n/a)</td><td>3.44 (n/a)</td><td>3.81 (n/a)</td><td>1.16 (n/a)</td><td>2.05 (n/a)</td><td>1813.90 (n/a)</td><td>873.60 (n/a)</td><td>549.80 (n/a)</td><td>330.50 (n/a)</td><td>610.29 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>3.50 (-3.84%)</td><td>2.76 (+6.14%)</td><td>3.42 (+5.98%)</td><td>1.20 (+16.79%)</td><td>1.03 (-10.24%)</td><td>3482.20 (-14.38%)</td><td>1806.86 (-11.40%)</td><td>1226.30 (-5.64%)</td><td>1198.30 (+3.99%)</td><td>986.40 <b>(-20.97%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>3.64 (n/a)</td><td>2.60 (n/a)</td><td>3.23 (n/a)</td><td>1.03 (n/a)</td><td>1.15 (n/a)</td><td>4067.00 (n/a)</td><td>2039.26 (n/a)</td><td>1299.60 (n/a)</td><td>1152.30 (n/a)</td><td>1248.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>6.21 (-0.65%)</td><td>4.12 (-14.06%)</td><td>3.88 (-2.98%)</td><td>3.13 (-19.32%)</td><td>1.22 (+5.28%)</td><td>1338.50 <b>(+23.96%)</b></td><td>1076.88 (+17.84%)</td><td>1081.70 (+3.07%)</td><td>675.90 (+0.66%)</td><td>253.34 <b>(+25.49%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>6.25 (n/a)</td><td>4.79 (n/a)</td><td>4.00 (n/a)</td><td>3.88 (n/a)</td><td>1.16 (n/a)</td><td>1079.80 (n/a)</td><td>913.84 (n/a)</td><td>1049.50 (n/a)</td><td>671.50 (n/a)</td><td>201.88 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>6.22 (+9.54%)</td><td>4.03 (-6.79%)</td><td>5.66 (+14.79%)</td><td>1.09 (-12.73%)</td><td>2.65 <b>(+50.63%)</b></td><td>3837.80 (+14.58%)</td><td>1895.62 <b>(+42.36%)</b></td><td>740.50 (-12.87%)</td><td>673.90 (-8.71%)</td><td>1634.75 <b>(+44.74%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>5.68 (n/a)</td><td>4.33 (n/a)</td><td>4.93 (n/a)</td><td>1.25 (n/a)</td><td>1.76 (n/a)</td><td>3349.40 (n/a)</td><td>1331.60 (n/a)</td><td>849.90 (n/a)</td><td>738.20 (n/a)</td><td>1129.45 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>10.00 <b>(+31.19%)</b></td><td>7.11 (+16.36%)</td><td>7.99 <b>(+22.18%)</b></td><td>3.15 (-6.00%)</td><td>2.57 <b>(+58.57%)</b></td><td>1331.50 (+6.38%)</td><td>691.22 (-7.33%)</td><td>524.90 (-18.15%)</td><td>419.30 <b>(-23.76%)</b></td><td>368.08 <b>(+28.83%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>7.63 (n/a)</td><td>6.11 (n/a)</td><td>6.54 (n/a)</td><td>3.35 (n/a)</td><td>1.62 (n/a)</td><td>1251.60 (n/a)</td><td>745.88 (n/a)</td><td>641.30 (n/a)</td><td>550.00 (n/a)</td><td>285.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>8.10 (+2.68%)</td><td>6.75 <b>(+26.72%)</b></td><td>6.52 (-0.03%)</td><td>5.30 <b>(+354.86%)</b></td><td>1.06 <b>(-59.81%)</b></td><td>791.40 <b>(-78.01%)</b></td><td>634.28 <b>(-50.06%)</b></td><td>643.50 (+0.03%)</td><td>518.10 (-2.61%)</td><td>103.63 <b>(-92.10%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>7.88 (n/a)</td><td>5.33 (n/a)</td><td>6.52 (n/a)</td><td>1.17 (n/a)</td><td>2.63 (n/a)</td><td>3599.60 (n/a)</td><td>1269.96 (n/a)</td><td>643.30 (n/a)</td><td>532.00 (n/a)</td><td>1311.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>9.05 <b>(+35.39%)</b></td><td>6.86 <b>(+52.85%)</b></td><td>7.03 <b>(+77.75%)</b></td><td>3.85 (+0.44%)</td><td>1.94 <b>(+58.02%)</b></td><td>1088.60 (-0.44%)</td><td>665.22 <b>(-31.91%)</b></td><td>596.90 <b>(-43.74%)</b></td><td>463.40 <b>(-26.14%)</b></td><td>246.48 <b>(+25.55%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>6.69 (n/a)</td><td>4.49 (n/a)</td><td>3.95 (n/a)</td><td>3.84 (n/a)</td><td>1.23 (n/a)</td><td>1093.40 (n/a)</td><td>976.90 (n/a)</td><td>1061.00 (n/a)</td><td>627.40 (n/a)</td><td>196.32 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>1.64 <b>(+23.65%)</b></td><td>1.01 (+14.26%)</td><td>1.00 (+15.78%)</td><td>0.16 <b>(-24.77%)</b></td><td>0.57 <b>(+26.25%)</b></td><td>3274.70 <b>(+32.92%)</b></td><td>1020.22 (+11.61%)</td><td>524.50 (-13.62%)</td><td>319.80 (-19.14%)</td><td>1265.54 <b>(+44.56%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>1.33 (n/a)</td><td>0.89 (n/a)</td><td>0.86 (n/a)</td><td>0.21 (n/a)</td><td>0.45 (n/a)</td><td>2463.70 (n/a)</td><td>914.10 (n/a)</td><td>607.20 (n/a)</td><td>395.50 (n/a)</td><td>875.42 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>2.29 (+2.34%)</td><td>2.02 <b>(+37.16%)</b></td><td>2.12 <b>(+34.91%)</b></td><td>1.38 <b>(+342.84%)</b></td><td>0.37 <b>(-54.21%)</b></td><td>760.50 <b>(-77.42%)</b></td><td>536.34 <b>(-54.96%)</b></td><td>495.60 <b>(-25.89%)</b></td><td>458.00 (-2.28%)</td><td>126.36 <b>(-89.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.24 (n/a)</td><td>1.48 (n/a)</td><td>1.57 (n/a)</td><td>0.31 (n/a)</td><td>0.80 (n/a)</td><td>3367.90 (n/a)</td><td>1190.70 (n/a)</td><td>668.70 (n/a)</td><td>468.70 (n/a)</td><td>1233.60 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>2.82 (+14.80%)</td><td>1.86 (+16.27%)</td><td>2.17 <b>(+30.13%)</b></td><td>0.62 (+2.88%)</td><td>1.01 <b>(+52.80%)</b></td><td>3372.60 (-2.80%)</td><td>1598.94 (-1.85%)</td><td>966.40 <b>(-23.16%)</b></td><td>744.10 (-12.90%)</td><td>1145.63 (+9.60%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.45 (n/a)</td><td>1.60 (n/a)</td><td>1.67 (n/a)</td><td>0.60 (n/a)</td><td>0.66 (n/a)</td><td>3469.80 (n/a)</td><td>1629.04 (n/a)</td><td>1257.60 (n/a)</td><td>854.30 (n/a)</td><td>1045.27 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>2.09 (+4.25%)</td><td>1.33 (-13.08%)</td><td>1.04 <b>(-37.47%)</b></td><td>0.64 <b>(-27.72%)</b></td><td>0.64 <b>(+53.21%)</b></td><td>822.10 <b>(+38.35%)</b></td><td>479.08 <b>(+29.41%)</b></td><td>503.00 <b>(+59.94%)</b></td><td>250.80 (-4.06%)</td><td>233.20 <b>(+78.47%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>2.01 (n/a)</td><td>1.53 (n/a)</td><td>1.67 (n/a)</td><td>0.88 (n/a)</td><td>0.42 (n/a)</td><td>594.20 (n/a)</td><td>370.20 (n/a)</td><td>314.50 (n/a)</td><td>261.40 (n/a)</td><td>130.67 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.11 (+8.14%)</td><td>0.08 (-4.42%)</td><td>0.07 (-12.99%)</td><td>0.05 <b>(-28.38%)</b></td><td>0.03 <b>(+86.68%)</b></td><td>635.40 <b>(+39.62%)</b></td><td>461.84 (+11.90%)</td><td>488.50 (+14.94%)</td><td>286.00 (-7.53%)</td><td>144.66 <b>(+142.76%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>455.10 (n/a)</td><td>412.74 (n/a)</td><td>425.00 (n/a)</td><td>309.30 (n/a)</td><td>59.59 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.14 (+2.10%)</td><td>0.09 (-10.37%)</td><td>0.08 (-3.50%)</td><td>0.06 <b>(-21.36%)</b></td><td>0.03 (+17.32%)</td><td>564.60 <b>(+27.16%)</b></td><td>418.00 (+14.94%)</td><td>426.10 (+3.62%)</td><td>236.00 (-2.03%)</td><td>120.13 <b>(+36.52%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>444.00 (n/a)</td><td>363.66 (n/a)</td><td>411.20 (n/a)</td><td>240.90 (n/a)</td><td>88.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.26 (-14.57%)</td><td>0.20 <b>(+34.35%)</b></td><td>0.24 <b>(+106.69%)</b></td><td>0.13 <b>(+46.13%)</b></td><td>0.06 <b>(-28.41%)</b></td><td>520.40 <b>(-31.56%)</b></td><td>353.46 <b>(-32.25%)</b></td><td>275.80 <b>(-51.61%)</b></td><td>253.90 (+17.06%)</td><td>123.73 <b>(-38.49%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.30 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>760.40 (n/a)</td><td>521.72 (n/a)</td><td>570.00 (n/a)</td><td>216.90 (n/a)</td><td>201.16 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.24 <b>(-32.52%)</b></td><td>0.19 (+3.38%)</td><td>0.23 <b>(+66.66%)</b></td><td>0.11 (-2.23%)</td><td>0.06 <b>(-36.80%)</b></td><td>616.50 (+2.29%)</td><td>395.02 (-9.55%)</td><td>286.30 <b>(-39.99%)</b></td><td>275.70 <b>(+48.15%)</b></td><td>159.29 (-6.92%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.35 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>602.70 (n/a)</td><td>436.74 (n/a)</td><td>477.10 (n/a)</td><td>186.10 (n/a)</td><td>171.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.32 (-13.66%)</td><td>0.20 <b>(+30.61%)</b></td><td>0.15 <b>(+32.53%)</b></td><td>0.13 <b>(+102.63%)</b></td><td>0.08 <b>(-33.94%)</b></td><td>496.20 <b>(-50.65%)</b></td><td>370.52 <b>(-39.05%)</b></td><td>436.90 <b>(-24.56%)</b></td><td>203.30 (+15.84%)</td><td>128.81 <b>(-58.02%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.37 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.13 (n/a)</td><td>1005.50 (n/a)</td><td>607.94 (n/a)</td><td>579.10 (n/a)</td><td>175.50 (n/a)</td><td>306.81 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.58 (+2.10%)</td><td>0.38 (-15.71%)</td><td>0.33 <b>(-30.73%)</b></td><td>0.25 (-7.33%)</td><td>0.14 <b>(+20.79%)</b></td><td>516.70 (+7.92%)</td><td>382.18 <b>(+23.18%)</b></td><td>396.30 <b>(+44.37%)</b></td><td>227.40 (-2.07%)</td><td>131.14 <b>(+29.71%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.56 (n/a)</td><td>0.45 (n/a)</td><td>0.48 (n/a)</td><td>0.27 (n/a)</td><td>0.12 (n/a)</td><td>478.80 (n/a)</td><td>310.26 (n/a)</td><td>274.50 (n/a)</td><td>232.20 (n/a)</td><td>101.10 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.64 (+13.50%)</td><td>0.39 (+4.00%)</td><td>0.39 <b>(+40.62%)</b></td><td>0.21 (-18.16%)</td><td>0.17 (+15.81%)</td><td>623.40 <b>(+22.19%)</b></td><td>393.34 (+0.72%)</td><td>337.50 <b>(-28.89%)</b></td><td>205.70 (-11.91%)</td><td>174.59 <b>(+29.04%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.56 (n/a)</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>510.20 (n/a)</td><td>390.54 (n/a)</td><td>474.60 (n/a)</td><td>233.50 (n/a)</td><td>135.30 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.69 <b>(+26.28%)</b></td><td>0.49 <b>(+77.32%)</b></td><td>0.47 <b>(+84.29%)</b></td><td>0.29 <b>(+349.54%)</b></td><td>0.15 (-11.35%)</td><td>447.40 <b>(-77.76%)</b></td><td>292.32 <b>(-61.56%)</b></td><td>279.30 <b>(-45.74%)</b></td><td>190.10 <b>(-20.79%)</b></td><td>100.16 <b>(-85.91%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.55 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td><td>2011.30 (n/a)</td><td>760.44 (n/a)</td><td>514.70 (n/a)</td><td>240.00 (n/a)</td><td>710.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:37:05</td><td>0.07 <b>(+30.30%)</b></td><td>0.06 <b>(+65.02%)</b></td><td>0.06 <b>(+110.01%)</b></td><td>0.03 <b>(+30.23%)</b></td><td>0.02 <b>(+36.13%)</b></td><td>639.50 <b>(-23.21%)</b></td><td>339.90 <b>(-37.96%)</b></td><td>258.90 <b>(-52.38%)</b></td><td>219.60 <b>(-23.24%)</b></td><td>173.61 (-14.25%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 02:39:51</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>832.80 (n/a)</td><td>547.86 (n/a)</td><td>543.70 (n/a)</td><td>286.10 (n/a)</td><td>202.44 (n/a)</td>
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
