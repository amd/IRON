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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (+11.30%)</td><td>0.02 <b>(+20.98%)</b></td><td>0.02 <b>(+47.29%)</b></td><td>0.01 <b>(+197.60%)</b></td><td>0.01 (-7.22%)</td><td>620.40 <b>(-66.40%)</b></td><td>393.00 <b>(-40.41%)</b></td><td>277.80 <b>(-32.11%)</b></td><td>225.90 (-10.18%)</td><td>185.91 <b>(-72.30%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1846.30 (n/a)</td><td>659.54 (n/a)</td><td>409.20 (n/a)</td><td>251.50 (n/a)</td><td>671.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (+5.60%)</td><td>0.02 <b>(+41.69%)</b></td><td>0.02 <b>(+57.92%)</b></td><td>0.02 <b>(+110.47%)</b></td><td>0.00 <b>(-48.83%)</b></td><td>316.70 <b>(-52.48%)</b></td><td>270.66 <b>(-39.17%)</b></td><td>264.30 <b>(-36.66%)</b></td><td>212.30 (-5.27%)</td><td>43.84 <b>(-77.40%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>666.50 (n/a)</td><td>444.98 (n/a)</td><td>417.30 (n/a)</td><td>224.10 (n/a)</td><td>193.94 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 <b>(+56.40%)</b></td><td>0.02 <b>(+40.21%)</b></td><td>0.02 <b>(+32.71%)</b></td><td>0.01 (+4.73%)</td><td>0.01 <b>(+91.33%)</b></td><td>478.10 (-4.51%)</td><td>290.14 <b>(-23.17%)</b></td><td>300.00 <b>(-24.64%)</b></td><td>151.50 <b>(-36.08%)</b></td><td>122.96 (+16.75%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>500.70 (n/a)</td><td>377.62 (n/a)</td><td>398.10 (n/a)</td><td>237.00 (n/a)</td><td>105.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-1.31%)</td><td>0.02 <b>(+27.73%)</b></td><td>0.02 <b>(+30.09%)</b></td><td>0.02 <b>(+56.25%)</b></td><td>0.00 <b>(-54.75%)</b></td><td>364.20 <b>(-35.99%)</b></td><td>289.62 <b>(-28.32%)</b></td><td>271.00 <b>(-23.12%)</b></td><td>269.70 (+1.31%)</td><td>41.71 <b>(-71.36%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.00 (n/a)</td><td>404.02 (n/a)</td><td>352.50 (n/a)</td><td>266.20 (n/a)</td><td>145.61 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-3.82%)</td><td>0.02 (-6.04%)</td><td>0.02 (-10.66%)</td><td>0.01 (+1.39%)</td><td>0.00 (-3.18%)</td><td>517.60 (-1.37%)</td><td>388.94 (+6.34%)</td><td>339.30 (+11.91%)</td><td>296.80 (+3.96%)</td><td>106.25 (+1.62%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.80 (n/a)</td><td>365.74 (n/a)</td><td>303.20 (n/a)</td><td>285.50 (n/a)</td><td>104.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 <b>(+35.81%)</b></td><td>0.03 <b>(+61.05%)</b></td><td>0.03 <b>(+104.54%)</b></td><td>0.02 <b>(+85.71%)</b></td><td>0.00 <b>(-27.98%)</b></td><td>290.70 <b>(-46.16%)</b></td><td>247.62 <b>(-42.07%)</b></td><td>238.60 <b>(-51.10%)</b></td><td>198.40 <b>(-26.38%)</b></td><td>37.01 <b>(-71.71%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>539.90 (n/a)</td><td>427.46 (n/a)</td><td>487.90 (n/a)</td><td>269.50 (n/a)</td><td>130.82 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (-7.04%)</td><td>0.04 (+5.24%)</td><td>0.04 (+1.53%)</td><td>0.03 (+8.55%)</td><td>0.01 <b>(-31.31%)</b></td><td>457.70 (-7.87%)</td><td>304.66 (-11.46%)</td><td>288.80 (-1.50%)</td><td>215.00 (+7.61%)</td><td>91.71 <b>(-34.06%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>496.80 (n/a)</td><td>344.10 (n/a)</td><td>293.20 (n/a)</td><td>199.80 (n/a)</td><td>139.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (-7.67%)</td><td>0.03 <b>(-22.43%)</b></td><td>0.04 (-5.28%)</td><td>0.01 <b>(-76.71%)</b></td><td>0.02 <b>(+68.88%)</b></td><td>2082.00 <b>(+329.37%)</b></td><td>707.98 <b>(+121.38%)</b></td><td>286.50 (+5.60%)</td><td>264.20 (+8.32%)</td><td>783.68 <b>(+666.17%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>484.90 (n/a)</td><td>319.80 (n/a)</td><td>271.30 (n/a)</td><td>243.90 (n/a)</td><td>102.29 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 <b>(-35.62%)</b></td><td>0.04 (+1.87%)</td><td>0.05 <b>(+43.21%)</b></td><td>0.03 <b>(+37.74%)</b></td><td>0.01 <b>(-60.89%)</b></td><td>465.50 <b>(-27.39%)</b></td><td>302.60 <b>(-21.00%)</b></td><td>264.00 <b>(-30.18%)</b></td><td>226.20 <b>(+55.36%)</b></td><td>94.28 <b>(-53.05%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>641.10 (n/a)</td><td>383.06 (n/a)</td><td>378.10 (n/a)</td><td>145.60 (n/a)</td><td>200.80 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 <b>(-27.36%)</b></td><td>0.03 (+0.92%)</td><td>0.04 <b>(+39.66%)</b></td><td>0.02 (+10.91%)</td><td>0.01 <b>(-33.34%)</b></td><td>505.40 (-9.83%)</td><td>377.50 (-5.27%)</td><td>294.60 <b>(-28.41%)</b></td><td>289.70 <b>(+37.69%)</b></td><td>115.91 (-14.29%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>560.50 (n/a)</td><td>398.50 (n/a)</td><td>411.50 (n/a)</td><td>210.40 (n/a)</td><td>135.23 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (+11.43%)</td><td>0.04 (-6.95%)</td><td>0.04 (-9.53%)</td><td>0.02 (-5.95%)</td><td>0.01 <b>(+49.58%)</b></td><td>500.90 (+6.33%)</td><td>364.16 (+12.07%)</td><td>320.10 (+10.53%)</td><td>251.90 (-10.26%)</td><td>117.22 <b>(+43.20%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>471.10 (n/a)</td><td>324.94 (n/a)</td><td>289.60 (n/a)</td><td>280.70 (n/a)</td><td>81.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (+8.85%)</td><td>0.04 (+13.77%)</td><td>0.04 <b>(+44.01%)</b></td><td>0.02 <b>(+64.41%)</b></td><td>0.01 (-13.86%)</td><td>642.40 <b>(-39.18%)</b></td><td>391.94 <b>(-22.72%)</b></td><td>308.60 <b>(-30.56%)</b></td><td>237.80 (-8.11%)</td><td>162.63 <b>(-49.81%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1056.20 (n/a)</td><td>507.16 (n/a)</td><td>444.40 (n/a)</td><td>258.80 (n/a)</td><td>324.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.11 (-0.56%)</td><td>0.08 (+13.93%)</td><td>0.10 <b>(+62.53%)</b></td><td>0.05 (+2.58%)</td><td>0.03 (-4.64%)</td><td>528.40 (-2.53%)</td><td>333.36 (-13.39%)</td><td>257.50 <b>(-38.47%)</b></td><td>227.20 (+0.58%)</td><td>135.58 (-6.34%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>542.10 (n/a)</td><td>384.88 (n/a)</td><td>418.50 (n/a)</td><td>225.90 (n/a)</td><td>144.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.11 (+19.79%)</td><td>0.08 <b>(+40.07%)</b></td><td>0.08 <b>(+47.88%)</b></td><td>0.05 <b>(+293.15%)</b></td><td>0.02 (-18.60%)</td><td>480.10 <b>(-74.57%)</b></td><td>346.44 <b>(-50.83%)</b></td><td>303.80 <b>(-32.38%)</b></td><td>229.00 (-16.55%)</td><td>115.04 <b>(-82.91%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1887.60 (n/a)</td><td>704.56 (n/a)</td><td>449.30 (n/a)</td><td>274.40 (n/a)</td><td>673.12 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (+19.30%)</td><td>0.08 (-4.03%)</td><td>0.09 (-4.90%)</td><td>0.05 (-5.12%)</td><td>0.03 <b>(+46.06%)</b></td><td>525.90 (+5.41%)</td><td>336.46 (+9.85%)</td><td>282.50 (+5.14%)</td><td>184.00 (-16.17%)</td><td>134.32 <b>(+21.92%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>498.90 (n/a)</td><td>306.28 (n/a)</td><td>268.70 (n/a)</td><td>219.50 (n/a)</td><td>110.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (-6.71%)</td><td>0.06 (+1.65%)</td><td>0.06 (+16.75%)</td><td>0.02 <b>(-31.05%)</b></td><td>0.03 (+11.99%)</td><td>1003.90 <b>(+45.03%)</b></td><td>503.92 (+10.81%)</td><td>406.80 (-14.36%)</td><td>243.90 (+7.21%)</td><td>308.47 <b>(+81.25%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>692.20 (n/a)</td><td>454.78 (n/a)</td><td>475.00 (n/a)</td><td>227.50 (n/a)</td><td>170.19 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 (-19.90%)</td><td>0.07 (+19.90%)</td><td>0.08 <b>(+74.84%)</b></td><td>0.05 <b>(+23.46%)</b></td><td>0.02 <b>(-38.93%)</b></td><td>484.40 (-19.01%)</td><td>354.36 <b>(-22.40%)</b></td><td>292.80 <b>(-42.80%)</b></td><td>280.40 <b>(+24.84%)</b></td><td>93.16 <b>(-36.54%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>598.10 (n/a)</td><td>456.66 (n/a)</td><td>511.90 (n/a)</td><td>224.60 (n/a)</td><td>146.81 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.11 <b>(+29.85%)</b></td><td>0.08 <b>(+63.73%)</b></td><td>0.08 <b>(+92.12%)</b></td><td>0.06 <b>(+321.33%)</b></td><td>0.02 <b>(-22.18%)</b></td><td>435.80 <b>(-76.27%)</b></td><td>319.70 <b>(-56.13%)</b></td><td>291.40 <b>(-47.95%)</b></td><td>227.10 <b>(-22.99%)</b></td><td>82.48 <b>(-86.90%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1836.30 (n/a)</td><td>728.70 (n/a)</td><td>559.80 (n/a)</td><td>294.90 (n/a)</td><td>629.57 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.23 (-9.91%)</td><td>0.16 (+10.15%)</td><td>0.18 <b>(+67.04%)</b></td><td>0.09 <b>(+81.35%)</b></td><td>0.06 <b>(-30.30%)</b></td><td>575.50 <b>(-44.86%)</b></td><td>361.54 <b>(-26.66%)</b></td><td>273.20 <b>(-40.14%)</b></td><td>215.50 (+10.97%)</td><td>156.01 <b>(-54.12%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.09 (n/a)</td><td>1043.80 (n/a)</td><td>492.98 (n/a)</td><td>456.40 (n/a)</td><td>194.20 (n/a)</td><td>340.03 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.18 (-11.32%)</td><td>0.16 <b>(+51.07%)</b></td><td>0.17 <b>(+82.28%)</b></td><td>0.11 <b>(+329.40%)</b></td><td>0.03 <b>(-55.30%)</b></td><td>444.10 <b>(-76.71%)</b></td><td>313.70 <b>(-56.83%)</b></td><td>290.40 <b>(-45.14%)</b></td><td>266.50 (+12.73%)</td><td>73.74 <b>(-89.03%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>0.07 (n/a)</td><td>1907.00 (n/a)</td><td>726.72 (n/a)</td><td>529.30 (n/a)</td><td>236.40 (n/a)</td><td>672.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.18 (-19.53%)</td><td>0.12 (-17.07%)</td><td>0.11 <b>(-32.20%)</b></td><td>0.03 <b>(-65.15%)</b></td><td>0.07 (+2.84%)</td><td>1886.70 <b>(+186.95%)</b></td><td>688.16 <b>(+63.61%)</b></td><td>465.60 <b>(+47.48%)</b></td><td>271.40 <b>(+24.27%)</b></td><td>680.38 <b>(+238.09%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>657.50 (n/a)</td><td>420.60 (n/a)</td><td>315.70 (n/a)</td><td>218.40 (n/a)</td><td>201.24 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.24 (+16.44%)</td><td>0.17 <b>(+55.12%)</b></td><td>0.20 <b>(+102.83%)</b></td><td>0.10 <b>(+115.89%)</b></td><td>0.07 (+12.37%)</td><td>512.30 <b>(-53.68%)</b></td><td>334.04 <b>(-41.78%)</b></td><td>246.20 <b>(-50.71%)</b></td><td>201.50 (-14.15%)</td><td>156.02 <b>(-53.56%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>1106.10 (n/a)</td><td>573.80 (n/a)</td><td>499.50 (n/a)</td><td>234.70 (n/a)</td><td>335.99 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.26 <b>(+44.83%)</b></td><td>0.16 (+14.13%)</td><td>0.11 <b>(-31.14%)</b></td><td>0.07 (-3.90%)</td><td>0.09 <b>(+81.10%)</b></td><td>684.50 (+4.06%)</td><td>405.10 (-0.08%)</td><td>440.40 <b>(+45.20%)</b></td><td>187.00 <b>(-30.95%)</b></td><td>212.37 <b>(+22.33%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>657.80 (n/a)</td><td>405.42 (n/a)</td><td>303.30 (n/a)</td><td>270.80 (n/a)</td><td>173.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.20 <b>(+40.50%)</b></td><td>0.14 <b>(+44.37%)</b></td><td>0.15 <b>(+59.01%)</b></td><td>0.07 (-0.13%)</td><td>0.06 <b>(+121.78%)</b></td><td>660.60 (+0.14%)</td><td>410.82 <b>(-21.96%)</b></td><td>335.30 <b>(-37.10%)</b></td><td>242.10 <b>(-28.84%)</b></td><td>192.44 <b>(+61.19%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>659.70 (n/a)</td><td>526.42 (n/a)</td><td>533.10 (n/a)</td><td>340.20 (n/a)</td><td>119.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 <b>(+38.84%)</b></td><td>0.01 <b>(+41.60%)</b></td><td>0.01 <b>(+62.98%)</b></td><td>0.01 (+1.33%)</td><td>0.00 <b>(+79.67%)</b></td><td>505.70 (-1.31%)</td><td>297.42 <b>(-24.94%)</b></td><td>245.50 <b>(-38.64%)</b></td><td>194.10 <b>(-27.98%)</b></td><td>121.97 <b>(+40.69%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.40 (n/a)</td><td>396.22 (n/a)</td><td>400.10 (n/a)</td><td>269.50 (n/a)</td><td>86.70 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (+1.24%)</td><td>0.01 (-8.25%)</td><td>0.01 (+2.95%)</td><td>0.01 (-19.46%)</td><td>0.00 <b>(+53.86%)</b></td><td>504.90 <b>(+24.18%)</b></td><td>342.72 (+16.67%)</td><td>260.80 (-2.87%)</td><td>232.20 (-1.23%)</td><td>129.19 <b>(+88.74%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>406.60 (n/a)</td><td>293.74 (n/a)</td><td>268.50 (n/a)</td><td>235.10 (n/a)</td><td>68.45 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (-4.46%)</td><td>0.01 (-4.21%)</td><td>0.01 (-6.59%)</td><td>0.00 <b>(+66.11%)</b></td><td>0.00 <b>(-38.87%)</b></td><td>593.50 <b>(-39.80%)</b></td><td>411.22 (-11.97%)</td><td>391.90 (+7.05%)</td><td>274.00 (+4.70%)</td><td>116.99 <b>(-61.09%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>985.80 (n/a)</td><td>467.14 (n/a)</td><td>366.10 (n/a)</td><td>261.70 (n/a)</td><td>300.66 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 <b>(-24.87%)</b></td><td>0.01 (-15.22%)</td><td>0.01 (-5.95%)</td><td>0.01 (-0.96%)</td><td>0.00 <b>(-41.76%)</b></td><td>522.50 (+0.97%)</td><td>402.50 (+10.00%)</td><td>430.70 (+6.35%)</td><td>276.90 <b>(+33.12%)</b></td><td>108.76 <b>(-21.25%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>517.50 (n/a)</td><td>365.90 (n/a)</td><td>405.00 (n/a)</td><td>208.00 (n/a)</td><td>138.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 <b>(-24.98%)</b></td><td>0.01 (-8.25%)</td><td>0.01 (-11.23%)</td><td>0.01 (+18.30%)</td><td>0.00 <b>(-35.50%)</b></td><td>499.60 (-15.48%)</td><td>344.60 (-1.33%)</td><td>305.40 (+12.65%)</td><td>229.50 <b>(+33.28%)</b></td><td>121.61 <b>(-30.12%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>591.10 (n/a)</td><td>349.26 (n/a)</td><td>271.10 (n/a)</td><td>172.20 (n/a)</td><td>174.03 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (-4.44%)</td><td>0.01 (-2.21%)</td><td>0.01 (-19.90%)</td><td>0.00 (-11.15%)</td><td>0.00 (+4.87%)</td><td>678.90 (+12.55%)</td><td>437.58 (+3.81%)</td><td>469.30 <b>(+24.85%)</b></td><td>266.90 (+4.63%)</td><td>170.39 (+10.37%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>603.20 (n/a)</td><td>421.50 (n/a)</td><td>375.90 (n/a)</td><td>255.10 (n/a)</td><td>154.37 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (+13.15%)</td><td>0.02 <b>(+27.70%)</b></td><td>0.02 <b>(+64.45%)</b></td><td>0.01 <b>(-26.28%)</b></td><td>0.01 <b>(+56.97%)</b></td><td>751.60 <b>(+35.64%)</b></td><td>402.46 (-9.79%)</td><td>300.00 <b>(-39.19%)</b></td><td>218.60 (-11.61%)</td><td>229.43 <b>(+84.40%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>554.10 (n/a)</td><td>446.12 (n/a)</td><td>493.30 (n/a)</td><td>247.30 (n/a)</td><td>124.42 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 <b>(-31.24%)</b></td><td>0.02 (+10.94%)</td><td>0.02 <b>(+93.68%)</b></td><td>0.01 <b>(+21.33%)</b></td><td>0.01 <b>(-53.11%)</b></td><td>467.40 (-17.57%)</td><td>290.68 <b>(-27.82%)</b></td><td>265.70 <b>(-48.37%)</b></td><td>199.90 <b>(+45.49%)</b></td><td>106.59 <b>(-46.53%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.00 (n/a)</td><td>402.70 (n/a)</td><td>514.60 (n/a)</td><td>137.40 (n/a)</td><td>199.36 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-8.91%)</td><td>0.02 (+3.12%)</td><td>0.01 (+15.45%)</td><td>0.01 <b>(+36.78%)</b></td><td>0.01 <b>(-29.73%)</b></td><td>470.70 <b>(-26.89%)</b></td><td>367.08 (-12.70%)</td><td>424.90 (-13.37%)</td><td>218.90 (+9.78%)</td><td>105.73 <b>(-42.10%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.80 (n/a)</td><td>420.46 (n/a)</td><td>490.50 (n/a)</td><td>199.40 (n/a)</td><td>182.63 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 <b>(+20.62%)</b></td><td>0.02 <b>(+31.04%)</b></td><td>0.01 <b>(+45.41%)</b></td><td>0.01 (+13.65%)</td><td>0.01 <b>(+36.99%)</b></td><td>508.80 (-12.00%)</td><td>370.62 <b>(-21.50%)</b></td><td>359.50 <b>(-31.24%)</b></td><td>233.30 (-17.09%)</td><td>124.19 (+5.48%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.20 (n/a)</td><td>472.10 (n/a)</td><td>522.80 (n/a)</td><td>281.40 (n/a)</td><td>117.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-1.81%)</td><td>0.01 <b>(-30.72%)</b></td><td>0.01 <b>(-39.28%)</b></td><td>0.01 <b>(-33.83%)</b></td><td>0.01 <b>(+51.94%)</b></td><td>643.50 <b>(+51.13%)</b></td><td>480.80 <b>(+58.22%)</b></td><td>478.30 <b>(+64.70%)</b></td><td>229.10 (+1.87%)</td><td>163.67 <b>(+119.44%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>425.80 (n/a)</td><td>303.88 (n/a)</td><td>290.40 (n/a)</td><td>224.90 (n/a)</td><td>74.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-13.25%)</td><td>0.01 (-16.80%)</td><td>0.01 <b>(-25.91%)</b></td><td>0.01 (+3.21%)</td><td>0.00 <b>(-24.07%)</b></td><td>510.30 (-3.11%)</td><td>427.46 (+17.94%)</td><td>453.40 <b>(+34.98%)</b></td><td>309.40 (+15.28%)</td><td>79.92 (-19.16%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>526.70 (n/a)</td><td>362.44 (n/a)</td><td>335.90 (n/a)</td><td>268.40 (n/a)</td><td>98.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 <b>(+51.48%)</b></td><td>0.04 <b>(+58.40%)</b></td><td>0.04 <b>(+80.93%)</b></td><td>0.02 <b>(+27.02%)</b></td><td>0.02 <b>(+65.07%)</b></td><td>475.00 <b>(-21.28%)</b></td><td>318.12 <b>(-34.17%)</b></td><td>275.40 <b>(-44.73%)</b></td><td>171.80 <b>(-33.97%)</b></td><td>125.93 (-8.07%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>603.40 (n/a)</td><td>483.22 (n/a)</td><td>498.30 (n/a)</td><td>260.20 (n/a)</td><td>136.98 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (-15.72%)</td><td>0.03 (+10.33%)</td><td>0.04 (+3.42%)</td><td>0.02 <b>(+330.29%)</b></td><td>0.01 <b>(-44.14%)</b></td><td>583.70 <b>(-76.76%)</b></td><td>360.58 <b>(-53.49%)</b></td><td>294.80 (-3.31%)</td><td>236.70 (+18.65%)</td><td>139.54 <b>(-85.77%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2511.60 (n/a)</td><td>775.32 (n/a)</td><td>304.90 (n/a)</td><td>199.50 (n/a)</td><td>980.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (-5.97%)</td><td>0.04 (-1.24%)</td><td>0.04 (-1.59%)</td><td>0.03 (-2.79%)</td><td>0.00 (-10.62%)</td><td>375.70 (+2.88%)</td><td>295.14 (+1.05%)</td><td>279.40 (+1.64%)</td><td>265.90 (+6.32%)</td><td>45.41 (-0.85%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>365.20 (n/a)</td><td>292.08 (n/a)</td><td>274.90 (n/a)</td><td>250.10 (n/a)</td><td>45.80 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (+10.12%)</td><td>0.03 (+11.33%)</td><td>0.04 <b>(+47.82%)</b></td><td>0.01 (+2.94%)</td><td>0.01 (+19.92%)</td><td>701.70 (-2.87%)</td><td>382.50 (-6.42%)</td><td>253.30 <b>(-32.36%)</b></td><td>233.00 (-9.20%)</td><td>203.73 (+6.62%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>722.40 (n/a)</td><td>408.74 (n/a)</td><td>374.50 (n/a)</td><td>256.60 (n/a)</td><td>191.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (-9.41%)</td><td>0.03 (+13.53%)</td><td>0.04 <b>(+67.54%)</b></td><td>0.02 <b>(+29.65%)</b></td><td>0.01 <b>(-25.72%)</b></td><td>482.40 <b>(-22.88%)</b></td><td>347.34 (-19.08%)</td><td>264.30 <b>(-40.33%)</b></td><td>251.00 (+10.43%)</td><td>120.15 <b>(-35.26%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>625.50 (n/a)</td><td>429.26 (n/a)</td><td>442.90 (n/a)</td><td>227.30 (n/a)</td><td>185.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 <b>(+55.70%)</b></td><td>0.03 <b>(+53.30%)</b></td><td>0.03 <b>(+90.15%)</b></td><td>0.00 <b>(-66.90%)</b></td><td>0.01 <b>(+212.14%)</b></td><td>2155.20 <b>(+202.14%)</b></td><td>663.36 (+19.18%)</td><td>311.70 <b>(-47.41%)</b></td><td>252.00 <b>(-35.76%)</b></td><td>834.38 <b>(+583.84%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>713.30 (n/a)</td><td>556.62 (n/a)</td><td>592.70 (n/a)</td><td>392.30 (n/a)</td><td>122.01 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 <b>(+32.86%)</b></td><td>0.07 (+11.68%)</td><td>0.08 <b>(+25.58%)</b></td><td>0.04 (-0.02%)</td><td>0.02 <b>(+78.65%)</b></td><td>491.80 (+0.00%)</td><td>326.18 (-5.08%)</td><td>264.00 <b>(-20.36%)</b></td><td>210.10 <b>(-24.72%)</b></td><td>119.79 <b>(+37.33%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>491.80 (n/a)</td><td>343.62 (n/a)</td><td>331.50 (n/a)</td><td>279.10 (n/a)</td><td>87.23 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (+14.91%)</td><td>0.07 <b>(+33.48%)</b></td><td>0.08 <b>(+78.61%)</b></td><td>0.01 <b>(-69.16%)</b></td><td>0.04 <b>(+66.55%)</b></td><td>1931.60 <b>(+224.26%)</b></td><td>586.40 <b>(+33.95%)</b></td><td>257.10 <b>(-44.01%)</b></td><td>204.00 (-12.97%)</td><td>752.74 <b>(+472.61%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>595.70 (n/a)</td><td>437.78 (n/a)</td><td>459.20 (n/a)</td><td>234.40 (n/a)</td><td>131.46 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 (+19.90%)</td><td>0.06 (+12.01%)</td><td>0.04 (-8.54%)</td><td>0.03 (-12.73%)</td><td>0.03 <b>(+95.43%)</b></td><td>607.00 (+14.57%)</td><td>424.66 (-1.14%)</td><td>486.20 (+9.33%)</td><td>245.60 (-16.60%)</td><td>167.13 <b>(+73.79%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>529.80 (n/a)</td><td>429.54 (n/a)</td><td>444.70 (n/a)</td><td>294.50 (n/a)</td><td>96.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 <b>(-36.73%)</b></td><td>0.06 (+9.94%)</td><td>0.06 <b>(+71.29%)</b></td><td>0.03 (-8.68%)</td><td>0.02 <b>(-56.10%)</b></td><td>647.60 (+9.50%)</td><td>377.22 <b>(-21.61%)</b></td><td>328.00 <b>(-41.63%)</b></td><td>257.00 <b>(+58.06%)</b></td><td>154.57 (-14.01%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>591.40 (n/a)</td><td>481.18 (n/a)</td><td>561.90 (n/a)</td><td>162.60 (n/a)</td><td>179.76 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 <b>(-34.24%)</b></td><td>0.05 <b>(-24.18%)</b></td><td>0.05 (-7.99%)</td><td>0.04 (-14.03%)</td><td>0.02 <b>(-53.54%)</b></td><td>564.40 (+16.32%)</td><td>420.46 (+19.69%)</td><td>456.80 (+8.68%)</td><td>288.40 <b>(+52.11%)</b></td><td>113.88 (-18.96%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>485.20 (n/a)</td><td>351.28 (n/a)</td><td>420.30 (n/a)</td><td>189.60 (n/a)</td><td>140.53 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (+7.42%)</td><td>0.05 (+13.37%)</td><td>0.04 (-4.25%)</td><td>0.03 <b>(+220.20%)</b></td><td>0.02 <b>(-23.66%)</b></td><td>629.00 <b>(-68.77%)</b></td><td>491.00 <b>(-36.10%)</b></td><td>544.10 (+4.43%)</td><td>291.40 (-6.93%)</td><td>129.16 <b>(-81.59%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2014.00 (n/a)</td><td>768.38 (n/a)</td><td>521.00 (n/a)</td><td>313.10 (n/a)</td><td>701.63 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>519.20 (n/a)</td><td>385.60 (n/a)</td><td>310.20 (n/a)</td><td>274.30 (n/a)</td><td>122.34 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>283.70 (n/a)</td><td>248.82 (n/a)</td><td>245.80 (n/a)</td><td>211.50 (n/a)</td><td>26.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.60 (n/a)</td><td>416.96 (n/a)</td><td>453.20 (n/a)</td><td>216.50 (n/a)</td><td>159.37 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>616.60 (n/a)</td><td>407.74 (n/a)</td><td>434.80 (n/a)</td><td>247.30 (n/a)</td><td>160.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>267.80 (n/a)</td><td>240.32 (n/a)</td><td>238.10 (n/a)</td><td>209.20 (n/a)</td><td>21.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.90 (n/a)</td><td>461.74 (n/a)</td><td>514.60 (n/a)</td><td>222.80 (n/a)</td><td>133.96 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>1912.70 (n/a)</td><td>653.02 (n/a)</td><td>294.20 (n/a)</td><td>254.20 (n/a)</td><td>712.70 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>452.70 (n/a)</td><td>371.62 (n/a)</td><td>406.80 (n/a)</td><td>274.90 (n/a)</td><td>85.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>581.90 (n/a)</td><td>435.70 (n/a)</td><td>416.00 (n/a)</td><td>284.80 (n/a)</td><td>116.63 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.22 (+7.42%)</td><td>0.17 (+9.32%)</td><td>0.19 (+6.74%)</td><td>0.10 (+18.16%)</td><td>0.05 (-0.68%)</td><td>513.40 (-15.38%)</td><td>306.08 (-10.56%)</td><td>262.20 (-6.32%)</td><td>223.10 (-6.93%)</td><td>117.36 <b>(-21.69%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>606.70 (n/a)</td><td>342.22 (n/a)</td><td>279.90 (n/a)</td><td>239.70 (n/a)</td><td>149.87 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>527.80 (n/a)</td><td>307.56 (n/a)</td><td>265.80 (n/a)</td><td>230.50 (n/a)</td><td>124.14 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>766.90 (n/a)</td><td>478.12 (n/a)</td><td>488.40 (n/a)</td><td>229.90 (n/a)</td><td>238.16 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>643.30 (n/a)</td><td>479.74 (n/a)</td><td>516.70 (n/a)</td><td>203.90 (n/a)</td><td>163.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.20 (n/a)</td><td>404.66 (n/a)</td><td>522.70 (n/a)</td><td>198.50 (n/a)</td><td>177.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>493.90 (n/a)</td><td>353.70 (n/a)</td><td>380.30 (n/a)</td><td>208.90 (n/a)</td><td>122.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>538.20 (n/a)</td><td>304.88 (n/a)</td><td>242.90 (n/a)</td><td>204.60 (n/a)</td><td>135.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>533.70 (n/a)</td><td>432.34 (n/a)</td><td>419.90 (n/a)</td><td>302.00 (n/a)</td><td>96.80 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1896.10 (n/a)</td><td>702.28 (n/a)</td><td>533.50 (n/a)</td><td>217.10 (n/a)</td><td>684.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>481.00 (n/a)</td><td>389.10 (n/a)</td><td>447.80 (n/a)</td><td>264.10 (n/a)</td><td>98.56 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>1139.70 (n/a)</td><td>526.20 (n/a)</td><td>477.80 (n/a)</td><td>255.30 (n/a)</td><td>362.39 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>553.30 (n/a)</td><td>375.92 (n/a)</td><td>449.70 (n/a)</td><td>198.20 (n/a)</td><td>159.99 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>591.40 (n/a)</td><td>448.98 (n/a)</td><td>464.50 (n/a)</td><td>212.40 (n/a)</td><td>145.84 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>505.70 (n/a)</td><td>382.88 (n/a)</td><td>430.90 (n/a)</td><td>241.30 (n/a)</td><td>120.34 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>4.11 (+1.51%)</td><td>2.93 (+17.47%)</td><td>2.38 (+2.41%)</td><td>1.76 (-2.16%)</td><td>1.08 (+16.26%)</td><td>5965.10 (+2.20%)</td><td>3988.32 (-13.07%)</td><td>4396.70 (-2.36%)</td><td>2548.90 (-1.49%)</td><td>1439.64 (+6.84%)</td><td>1685.06 (+1.51%)</td><td>1201.10 (+17.47%)</td><td>976.86 (+2.41%)</td><td>720.02 (-2.16%)</td><td>440.65 (+16.26%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>4.05 (n/a)</td><td>2.50 (n/a)</td><td>2.33 (n/a)</td><td>1.80 (n/a)</td><td>0.93 (n/a)</td><td>5836.50 (n/a)</td><td>4588.16 (n/a)</td><td>4502.80 (n/a)</td><td>2587.50 (n/a)</td><td>1347.52 (n/a)</td><td>1659.92 (n/a)</td><td>1022.49 (n/a)</td><td>953.84 (n/a)</td><td>735.89 (n/a)</td><td>379.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.83 (+9.64%)</td><td>3.07 (+6.95%)</td><td>3.30 (+13.71%)</td><td>1.87 (-18.61%)</td><td>0.75 <b>(+74.72%)</b></td><td>12643.40 <b>(+22.86%)</b></td><td>8186.32 (-2.21%)</td><td>7139.40 (-12.06%)</td><td>6163.00 (-8.80%)</td><td>2596.04 <b>(+103.22%)</b></td><td>2177.80 (+9.64%)</td><td>1746.42 (+6.95%)</td><td>1879.97 (+13.71%)</td><td>1061.56 (-18.61%)</td><td>428.61 <b>(+74.72%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.49 (n/a)</td><td>2.87 (n/a)</td><td>2.91 (n/a)</td><td>2.29 (n/a)</td><td>0.43 (n/a)</td><td>10291.00 (n/a)</td><td>8371.04 (n/a)</td><td>8118.50 (n/a)</td><td>6757.40 (n/a)</td><td>1277.47 (n/a)</td><td>1986.24 (n/a)</td><td>1632.95 (n/a)</td><td>1653.24 (n/a)</td><td>1304.22 (n/a)</td><td>245.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.87 (-3.67%)</td><td>3.57 (+16.95%)</td><td>3.64 <b>(+26.75%)</b></td><td>3.22 <b>(+44.40%)</b></td><td>0.29 <b>(-57.07%)</b></td><td>5210.20 <b>(-30.75%)</b></td><td>4720.78 (-17.25%)</td><td>4608.30 <b>(-21.10%)</b></td><td>4330.50 (+3.81%)</td><td>385.60 <b>(-68.99%)</b></td><td>1983.61 (-3.67%)</td><td>1829.18 (+16.95%)</td><td>1864.01 <b>(+26.75%)</b></td><td>1648.68 <b>(+44.40%)</b></td><td>146.65 <b>(-57.07%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>4.02 (n/a)</td><td>3.05 (n/a)</td><td>2.87 (n/a)</td><td>2.23 (n/a)</td><td>0.67 (n/a)</td><td>7523.80 (n/a)</td><td>5704.66 (n/a)</td><td>5840.80 (n/a)</td><td>4171.60 (n/a)</td><td>1243.52 (n/a)</td><td>2059.16 (n/a)</td><td>1564.13 (n/a)</td><td>1470.68 (n/a)</td><td>1141.71 (n/a)</td><td>341.61 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.88 <b>(-27.01%)</b></td><td>0.78 (-3.30%)</td><td>0.85 (+11.63%)</td><td>0.63 <b>(+27.09%)</b></td><td>0.12 <b>(-56.59%)</b></td><td>727.40 <b>(-21.32%)</b></td><td>598.24 (-3.33%)</td><td>541.10 (-10.41%)</td><td>523.30 <b>(+37.03%)</b></td><td>94.22 <b>(-53.73%)</b></td><td>64.12 <b>(-27.01%)</b></td><td>57.15 (-3.30%)</td><td>62.02 (+11.63%)</td><td>46.13 <b>(+27.09%)</b></td><td>8.41 <b>(-56.59%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.20 (n/a)</td><td>0.81 (n/a)</td><td>0.76 (n/a)</td><td>0.50 (n/a)</td><td>0.26 (n/a)</td><td>924.50 (n/a)</td><td>618.86 (n/a)</td><td>604.00 (n/a)</td><td>381.90 (n/a)</td><td>203.64 (n/a)</td><td>87.85 (n/a)</td><td>59.10 (n/a)</td><td>55.56 (n/a)</td><td>36.29 (n/a)</td><td>19.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.62 (-0.53%)</td><td>1.22 <b>(+22.72%)</b></td><td>1.38 <b>(+33.87%)</b></td><td>0.65 <b>(+80.60%)</b></td><td>0.41 (-8.86%)</td><td>1009.70 <b>(-44.63%)</b></td><td>605.98 <b>(-28.29%)</b></td><td>475.30 <b>(-25.30%)</b></td><td>405.60 (+0.55%)</td><td>255.62 <b>(-54.47%)</b></td><td>165.48 (-0.53%)</td><td>124.72 <b>(+22.72%)</b></td><td>141.19 <b>(+33.87%)</b></td><td>66.47 <b>(+80.60%)</b></td><td>42.39 (-8.86%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.62 (n/a)</td><td>0.99 (n/a)</td><td>1.03 (n/a)</td><td>0.36 (n/a)</td><td>0.45 (n/a)</td><td>1823.50 (n/a)</td><td>845.02 (n/a)</td><td>636.30 (n/a)</td><td>403.40 (n/a)</td><td>561.48 (n/a)</td><td>166.35 (n/a)</td><td>101.63 (n/a)</td><td>105.47 (n/a)</td><td>36.80 (n/a)</td><td>46.51 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.73 <b>(+36.06%)</b></td><td>1.44 <b>(+45.82%)</b></td><td>1.35 <b>(+28.24%)</b></td><td>1.27 <b>(+87.53%)</b></td><td>0.20 <b>(-21.26%)</b></td><td>595.60 <b>(-46.68%)</b></td><td>529.58 <b>(-34.27%)</b></td><td>559.40 <b>(-22.02%)</b></td><td>436.30 <b>(-26.50%)</b></td><td>67.98 <b>(-69.29%)</b></td><td>192.27 <b>(+36.06%)</b></td><td>160.65 <b>(+45.82%)</b></td><td>149.95 <b>(+28.24%)</b></td><td>140.84 <b>(+87.53%)</b></td><td>21.93 <b>(-21.26%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.27 (n/a)</td><td>0.99 (n/a)</td><td>1.05 (n/a)</td><td>0.67 (n/a)</td><td>0.25 (n/a)</td><td>1117.00 (n/a)</td><td>805.74 (n/a)</td><td>717.40 (n/a)</td><td>593.60 (n/a)</td><td>221.39 (n/a)</td><td>141.32 (n/a)</td><td>110.17 (n/a)</td><td>116.93 (n/a)</td><td>75.10 (n/a)</td><td>27.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.73 (+6.23%)</td><td>1.24 (+2.87%)</td><td>1.17 (-19.00%)</td><td>0.69 <b>(+128.67%)</b></td><td>0.39 <b>(-29.04%)</b></td><td>1514.20 <b>(-56.27%)</b></td><td>926.96 <b>(-28.15%)</b></td><td>893.60 <b>(+23.46%)</b></td><td>606.20 (-5.87%)</td><td>350.68 <b>(-71.26%)</b></td><td>221.42 (+6.23%)</td><td>159.11 (+2.87%)</td><td>150.21 (-19.00%)</td><td>88.64 <b>(+128.67%)</b></td><td>49.38 <b>(-29.04%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.63 (n/a)</td><td>1.21 (n/a)</td><td>1.45 (n/a)</td><td>0.30 (n/a)</td><td>0.54 (n/a)</td><td>3462.50 (n/a)</td><td>1290.16 (n/a)</td><td>723.80 (n/a)</td><td>644.00 (n/a)</td><td>1220.07 (n/a)</td><td>208.42 (n/a)</td><td>154.67 (n/a)</td><td>185.44 (n/a)</td><td>38.76 (n/a)</td><td>69.58 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.16 (+6.60%)</td><td>1.64 (+2.59%)</td><td>1.97 <b>(+24.94%)</b></td><td>0.31 <b>(-76.32%)</b></td><td>0.77 <b>(+157.74%)</b></td><td>3409.00 <b>(+322.38%)</b></td><td>1112.16 <b>(+64.77%)</b></td><td>532.80 (-19.95%)</td><td>486.10 (-6.19%)</td><td>1285.23 <b>(+964.93%)</b></td><td>276.10 (+6.60%)</td><td>209.53 (+2.59%)</td><td>251.92 <b>(+24.94%)</b></td><td>39.37 <b>(-76.32%)</b></td><td>98.23 <b>(+157.74%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>2.02 (n/a)</td><td>1.60 (n/a)</td><td>1.58 (n/a)</td><td>1.30 (n/a)</td><td>0.30 (n/a)</td><td>807.10 (n/a)</td><td>674.98 (n/a)</td><td>665.60 (n/a)</td><td>518.20 (n/a)</td><td>120.69 (n/a)</td><td>259.02 (n/a)</td><td>204.25 (n/a)</td><td>201.64 (n/a)</td><td>166.29 (n/a)</td><td>38.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.36 (-7.92%)</td><td>1.52 (-12.92%)</td><td>1.50 (-4.50%)</td><td>0.43 <b>(-66.97%)</b></td><td>0.70 <b>(+35.19%)</b></td><td>2434.90 <b>(+202.77%)</b></td><td>973.06 <b>(+51.90%)</b></td><td>701.10 (+4.70%)</td><td>443.40 (+8.60%)</td><td>824.26 <b>(+400.83%)</b></td><td>302.71 (-7.92%)</td><td>194.19 (-12.92%)</td><td>191.43 (-4.50%)</td><td>55.12 <b>(-66.97%)</b></td><td>90.22 <b>(+35.19%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>2.57 (n/a)</td><td>1.74 (n/a)</td><td>1.57 (n/a)</td><td>1.30 (n/a)</td><td>0.52 (n/a)</td><td>804.20 (n/a)</td><td>640.58 (n/a)</td><td>669.60 (n/a)</td><td>408.30 (n/a)</td><td>164.58 (n/a)</td><td>328.73 (n/a)</td><td>223.00 (n/a)</td><td>200.44 (n/a)</td><td>166.89 (n/a)</td><td>66.74 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.38 <b>(+78.42%)</b></td><td>2.05 <b>(+157.52%)</b></td><td>2.18 <b>(+257.42%)</b></td><td>1.70 <b>(+250.17%)</b></td><td>0.29 <b>(-23.23%)</b></td><td>615.70 <b>(-71.45%)</b></td><td>520.40 <b>(-66.57%)</b></td><td>480.10 <b>(-72.02%)</b></td><td>441.20 <b>(-43.95%)</b></td><td>76.90 <b>(-87.96%)</b></td><td>304.22 <b>(+78.42%)</b></td><td>262.33 <b>(+157.52%)</b></td><td>279.58 <b>(+257.42%)</b></td><td>217.98 <b>(+250.17%)</b></td><td>37.39 <b>(-23.23%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.33 (n/a)</td><td>0.80 (n/a)</td><td>0.61 (n/a)</td><td>0.49 (n/a)</td><td>0.38 (n/a)</td><td>2156.20 (n/a)</td><td>1556.86 (n/a)</td><td>1715.80 (n/a)</td><td>787.20 (n/a)</td><td>638.50 (n/a)</td><td>170.50 (n/a)</td><td>101.87 (n/a)</td><td>78.22 (n/a)</td><td>62.25 (n/a)</td><td>48.70 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.61 (+0.28%)</td><td>1.09 (+6.86%)</td><td>0.97 (-19.09%)</td><td>0.47 <b>(+58.07%)</b></td><td>0.49 (-17.48%)</td><td>2246.90 <b>(-36.74%)</b></td><td>1174.90 <b>(-25.16%)</b></td><td>1083.80 <b>(+23.58%)</b></td><td>650.40 (-0.29%)</td><td>650.70 <b>(-48.08%)</b></td><td>206.35 (+0.28%)</td><td>140.13 (+6.86%)</td><td>123.84 (-19.09%)</td><td>59.74 <b>(+58.07%)</b></td><td>62.86 (-17.48%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.61 (n/a)</td><td>1.02 (n/a)</td><td>1.20 (n/a)</td><td>0.30 (n/a)</td><td>0.60 (n/a)</td><td>3551.70 (n/a)</td><td>1569.78 (n/a)</td><td>877.00 (n/a)</td><td>652.30 (n/a)</td><td>1253.19 (n/a)</td><td>205.76 (n/a)</td><td>131.14 (n/a)</td><td>153.05 (n/a)</td><td>37.79 (n/a)</td><td>76.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.75 <b>(+32.91%)</b></td><td>1.10 (+0.24%)</td><td>1.50 <b>(+29.80%)</b></td><td>0.30 <b>(-58.64%)</b></td><td>0.68 <b>(+206.94%)</b></td><td>3498.70 <b>(+141.81%)</b></td><td>1579.98 <b>(+58.28%)</b></td><td>697.80 <b>(-22.95%)</b></td><td>600.40 <b>(-24.76%)</b></td><td>1311.61 <b>(+411.94%)</b></td><td>223.56 <b>(+32.91%)</b></td><td>140.52 (+0.24%)</td><td>192.36 <b>(+29.80%)</b></td><td>38.36 <b>(-58.64%)</b></td><td>86.47 <b>(+206.94%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.31 (n/a)</td><td>1.10 (n/a)</td><td>1.16 (n/a)</td><td>0.72 (n/a)</td><td>0.22 (n/a)</td><td>1446.90 (n/a)</td><td>998.22 (n/a)</td><td>905.70 (n/a)</td><td>798.00 (n/a)</td><td>256.20 (n/a)</td><td>168.20 (n/a)</td><td>140.19 (n/a)</td><td>148.20 (n/a)</td><td>92.76 (n/a)</td><td>28.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.88 (+10.86%)</td><td>0.68 (+4.39%)</td><td>0.75 (+12.47%)</td><td>0.49 (-1.73%)</td><td>0.16 <b>(+46.69%)</b></td><td>729.10 (+1.76%)</td><td>553.56 (-1.80%)</td><td>482.00 (-11.09%)</td><td>408.60 (-9.78%)</td><td>140.49 <b>(+37.65%)</b></td><td>41.06 (+10.86%)</td><td>31.85 (+4.39%)</td><td>34.81 (+12.47%)</td><td>23.01 (-1.73%)</td><td>7.68 <b>(+46.69%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.80 (n/a)</td><td>0.66 (n/a)</td><td>0.66 (n/a)</td><td>0.50 (n/a)</td><td>0.11 (n/a)</td><td>716.50 (n/a)</td><td>563.70 (n/a)</td><td>542.10 (n/a)</td><td>452.90 (n/a)</td><td>102.06 (n/a)</td><td>37.04 (n/a)</td><td>30.51 (n/a)</td><td>30.95 (n/a)</td><td>23.41 (n/a)</td><td>5.23 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.08 (+1.70%)</td><td>2.01 (-17.17%)</td><td>1.92 <b>(-32.02%)</b></td><td>0.99 <b>(-41.56%)</b></td><td>0.80 <b>(+21.74%)</b></td><td>4251.20 <b>(+71.13%)</b></td><td>2424.08 <b>(+31.14%)</b></td><td>2186.20 <b>(+47.09%)</b></td><td>1360.60 (-1.67%)</td><td>1126.97 <b>(+103.58%)</b></td><td>789.14 (+1.70%)</td><td>514.57 (-17.17%)</td><td>491.14 <b>(-32.02%)</b></td><td>252.57 <b>(-41.56%)</b></td><td>205.38 <b>(+21.74%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.03 (n/a)</td><td>2.43 (n/a)</td><td>2.82 (n/a)</td><td>1.69 (n/a)</td><td>0.66 (n/a)</td><td>2484.20 (n/a)</td><td>1848.48 (n/a)</td><td>1486.30 (n/a)</td><td>1383.70 (n/a)</td><td>553.58 (n/a)</td><td>775.97 (n/a)</td><td>621.24 (n/a)</td><td>722.43 (n/a)</td><td>432.22 (n/a)</td><td>168.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.59 (-10.17%)</td><td>2.09 <b>(-25.96%)</b></td><td>1.34 <b>(-59.98%)</b></td><td>0.68 <b>(-43.85%)</b></td><td>1.38 (+19.27%)</td><td>3882.30 <b>(+78.10%)</b></td><td>1870.20 <b>(+65.55%)</b></td><td>1962.00 <b>(+149.87%)</b></td><td>730.80 (+11.32%)</td><td>1290.55 <b>(+103.17%)</b></td><td>734.60 (-10.17%)</td><td>427.28 <b>(-25.96%)</b></td><td>273.63 <b>(-59.98%)</b></td><td>138.29 <b>(-43.85%)</b></td><td>281.86 (+19.27%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.99 (n/a)</td><td>2.82 (n/a)</td><td>3.34 (n/a)</td><td>1.20 (n/a)</td><td>1.15 (n/a)</td><td>2179.90 (n/a)</td><td>1129.72 (n/a)</td><td>785.20 (n/a)</td><td>656.50 (n/a)</td><td>635.20 (n/a)</td><td>817.73 (n/a)</td><td>577.09 (n/a)</td><td>683.76 (n/a)</td><td>246.28 (n/a)</td><td>236.33 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.29 (-8.84%)</td><td>2.70 (+3.97%)</td><td>2.73 (+5.73%)</td><td>2.00 (+8.28%)</td><td>0.46 <b>(-34.67%)</b></td><td>3938.60 (-7.64%)</td><td>2992.94 (-6.81%)</td><td>2879.90 (-5.42%)</td><td>2392.60 (+9.70%)</td><td>569.14 <b>(-32.50%)</b></td><td>1009.74 (-8.84%)</td><td>828.35 (+3.97%)</td><td>838.89 (+5.73%)</td><td>613.40 (+8.28%)</td><td>141.06 <b>(-34.67%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.61 (n/a)</td><td>2.59 (n/a)</td><td>2.58 (n/a)</td><td>1.84 (n/a)</td><td>0.70 (n/a)</td><td>4264.50 (n/a)</td><td>3211.58 (n/a)</td><td>3045.00 (n/a)</td><td>2181.10 (n/a)</td><td>843.12 (n/a)</td><td>1107.65 (n/a)</td><td>796.73 (n/a)</td><td>793.40 (n/a)</td><td>566.51 (n/a)</td><td>215.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>517.40 (n/a)</td><td>353.66 (n/a)</td><td>286.90 (n/a)</td><td>244.70 (n/a)</td><td>120.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>528.20 (n/a)</td><td>435.86 (n/a)</td><td>443.70 (n/a)</td><td>274.40 (n/a)</td><td>103.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>542.10 (n/a)</td><td>314.94 (n/a)</td><td>281.70 (n/a)</td><td>194.30 (n/a)</td><td>132.99 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>721.50 (n/a)</td><td>398.28 (n/a)</td><td>278.00 (n/a)</td><td>258.50 (n/a)</td><td>202.07 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>592.70 (n/a)</td><td>418.44 (n/a)</td><td>476.40 (n/a)</td><td>231.90 (n/a)</td><td>162.39 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>659.50 (n/a)</td><td>449.68 (n/a)</td><td>487.20 (n/a)</td><td>287.80 (n/a)</td><td>150.14 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>514.00 (n/a)</td><td>324.88 (n/a)</td><td>278.20 (n/a)</td><td>258.40 (n/a)</td><td>107.50 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>641.60 (n/a)</td><td>378.24 (n/a)</td><td>241.60 (n/a)</td><td>202.30 (n/a)</td><td>215.37 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1932.70 (n/a)</td><td>626.44 (n/a)</td><td>220.90 (n/a)</td><td>197.10 (n/a)</td><td>747.69 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>539.70 (n/a)</td><td>405.94 (n/a)</td><td>445.40 (n/a)</td><td>247.00 (n/a)</td><td>131.69 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.80 (n/a)</td><td>379.80 (n/a)</td><td>286.60 (n/a)</td><td>230.10 (n/a)</td><td>156.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>553.70 (n/a)</td><td>476.66 (n/a)</td><td>529.20 (n/a)</td><td>295.90 (n/a)</td><td>105.33 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.70 (n/a)</td><td>385.90 (n/a)</td><td>317.10 (n/a)</td><td>229.60 (n/a)</td><td>162.29 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>618.10 (n/a)</td><td>320.54 (n/a)</td><td>282.50 (n/a)</td><td>196.80 (n/a)</td><td>171.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2177.40 (n/a)</td><td>726.10 (n/a)</td><td>443.60 (n/a)</td><td>218.30 (n/a)</td><td>818.00 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>479.50 (n/a)</td><td>382.56 (n/a)</td><td>442.90 (n/a)</td><td>265.00 (n/a)</td><td>101.77 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>508.90 (n/a)</td><td>352.78 (n/a)</td><td>341.10 (n/a)</td><td>238.10 (n/a)</td><td>116.52 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>566.50 (n/a)</td><td>370.28 (n/a)</td><td>347.40 (n/a)</td><td>268.50 (n/a)</td><td>116.41 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>840.30 (n/a)</td><td>426.30 (n/a)</td><td>331.30 (n/a)</td><td>301.00 (n/a)</td><td>231.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>600.50 (n/a)</td><td>374.98 (n/a)</td><td>275.20 (n/a)</td><td>263.10 (n/a)</td><td>153.84 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>317.40 (n/a)</td><td>289.76 (n/a)</td><td>291.10 (n/a)</td><td>268.30 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>603.20 (n/a)</td><td>422.44 (n/a)</td><td>468.10 (n/a)</td><td>249.60 (n/a)</td><td>141.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>592.20 (n/a)</td><td>359.74 (n/a)</td><td>260.90 (n/a)</td><td>231.30 (n/a)</td><td>160.45 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>567.00 (n/a)</td><td>406.66 (n/a)</td><td>452.10 (n/a)</td><td>260.40 (n/a)</td><td>134.96 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.48 <b>(-32.57%)</b></td><td>0.41 (-12.22%)</td><td>0.41 (-17.86%)</td><td>0.33 <b>(+43.50%)</b></td><td>0.06 <b>(-66.11%)</b></td><td>676.40 <b>(-30.31%)</b></td><td>548.58 (-0.14%)</td><td>535.40 <b>(+21.74%)</b></td><td>456.10 <b>(+48.28%)</b></td><td>87.51 <b>(-66.26%)</b></td><td>20.69 <b>(-32.57%)</b></td><td>17.54 (-12.22%)</td><td>17.63 (-17.86%)</td><td>13.95 <b>(+43.50%)</b></td><td>2.68 <b>(-66.11%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.72 (n/a)</td><td>0.47 (n/a)</td><td>0.50 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>970.60 (n/a)</td><td>549.34 (n/a)</td><td>439.80 (n/a)</td><td>307.60 (n/a)</td><td>259.40 (n/a)</td><td>30.68 (n/a)</td><td>19.98 (n/a)</td><td>21.46 (n/a)</td><td>9.72 (n/a)</td><td>7.90 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.64 <b>(+32.84%)</b></td><td>0.39 (+3.10%)</td><td>0.39 (-5.56%)</td><td>0.12 (+11.36%)</td><td>0.18 <b>(+21.47%)</b></td><td>1770.40 (-10.20%)</td><td>762.30 (-4.10%)</td><td>567.70 (+5.87%)</td><td>344.50 <b>(-24.72%)</b></td><td>572.93 (-13.04%)</td><td>27.39 <b>(+32.84%)</b></td><td>16.62 (+3.10%)</td><td>16.62 (-5.56%)</td><td>5.33 (+11.36%)</td><td>7.89 <b>(+21.47%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.48 (n/a)</td><td>0.38 (n/a)</td><td>0.41 (n/a)</td><td>0.11 (n/a)</td><td>0.15 (n/a)</td><td>1971.60 (n/a)</td><td>794.92 (n/a)</td><td>536.20 (n/a)</td><td>457.60 (n/a)</td><td>658.87 (n/a)</td><td>20.62 (n/a)</td><td>16.12 (n/a)</td><td>17.60 (n/a)</td><td>4.79 (n/a)</td><td>6.50 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.31 (+0.23%)</td><td>0.31 (-0.70%)</td><td>0.31 (-0.90%)</td><td>0.30 (-1.22%)</td><td>0.01 <b>(+46.34%)</b></td><td>84352.70 (+1.23%)</td><td>82420.52 (+0.72%)</td><td>82433.20 (+0.91%)</td><td>80463.50 (-0.23%)</td><td>1428.32 <b>(+47.54%)</b></td><td>213.51 (+0.23%)</td><td>208.49 (-0.70%)</td><td>208.41 (-0.90%)</td><td>203.67 (-1.22%)</td><td>3.62 <b>(+46.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83327.60 (n/a)</td><td>81833.04 (n/a)</td><td>81689.60 (n/a)</td><td>80651.90 (n/a)</td><td>968.08 (n/a)</td><td>213.01 (n/a)</td><td>209.96 (n/a)</td><td>210.31 (n/a)</td><td>206.17 (n/a)</td><td>2.47 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.15 (+0.43%)</td><td>1.14 (+0.40%)</td><td>1.14 (+1.15%)</td><td>1.13 (+0.18%)</td><td>0.01 (-0.04%)</td><td>22306.90 (-0.17%)</td><td>22079.24 (-0.40%)</td><td>22002.90 (-1.14%)</td><td>21835.70 (-0.43%)</td><td>197.05 (-0.49%)</td><td>786.78 (+0.43%)</td><td>778.15 (+0.40%)</td><td>780.80 (+1.15%)</td><td>770.16 (+0.18%)</td><td>6.94 (-0.04%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.15 (n/a)</td><td>1.14 (n/a)</td><td>1.13 (n/a)</td><td>1.13 (n/a)</td><td>0.01 (n/a)</td><td>22345.90 (n/a)</td><td>22167.50 (n/a)</td><td>22256.20 (n/a)</td><td>21930.50 (n/a)</td><td>198.01 (n/a)</td><td>783.38 (n/a)</td><td>775.05 (n/a)</td><td>771.91 (n/a)</td><td>768.81 (n/a)</td><td>6.94 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.80 (-0.00%)</td><td>0.78 (+1.16%)</td><td>0.79 (-0.01%)</td><td>0.77 (+3.17%)</td><td>0.01 <b>(-45.62%)</b></td><td>98111.30 (-3.07%)</td><td>96347.94 (-1.20%)</td><td>96116.20 (+0.01%)</td><td>94580.60 (+0.00%)</td><td>1569.88 <b>(-47.31%)</b></td><td>726.57 (-0.00%)</td><td>713.39 (+1.16%)</td><td>714.96 (-0.01%)</td><td>700.42 (+3.17%)</td><td>11.61 <b>(-45.62%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.80 (n/a)</td><td>0.77 (n/a)</td><td>0.79 (n/a)</td><td>0.75 (n/a)</td><td>0.02 (n/a)</td><td>101217.20 (n/a)</td><td>97515.12 (n/a)</td><td>96105.60 (n/a)</td><td>94578.70 (n/a)</td><td>2979.72 (n/a)</td><td>726.59 (n/a)</td><td>705.23 (n/a)</td><td>715.04 (n/a)</td><td>678.93 (n/a)</td><td>21.35 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.78 (-0.07%)</td><td>0.77 (-0.73%)</td><td>0.77 (-0.72%)</td><td>0.76 (-0.79%)</td><td>0.01 <b>(+51.96%)</b></td><td>99388.60 (+0.80%)</td><td>98391.12 (+0.74%)</td><td>98213.90 (+0.72%)</td><td>97074.90 (+0.07%)</td><td>958.10 <b>(+53.44%)</b></td><td>707.90 (-0.07%)</td><td>698.48 (-0.73%)</td><td>699.69 (-0.72%)</td><td>691.42 (-0.79%)</td><td>6.81 <b>(+51.96%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.00 (n/a)</td><td>98599.10 (n/a)</td><td>97664.26 (n/a)</td><td>97507.70 (n/a)</td><td>97010.50 (n/a)</td><td>624.43 (n/a)</td><td>708.37 (n/a)</td><td>703.65 (n/a)</td><td>704.76 (n/a)</td><td>696.96 (n/a)</td><td>4.48 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.89 (-0.37%)</td><td>0.89 (+0.14%)</td><td>0.89 (-0.10%)</td><td>0.87 (+0.32%)</td><td>0.01 (-17.05%)</td><td>86293.70 (-0.31%)</td><td>85184.94 (-0.15%)</td><td>85270.30 (+0.10%)</td><td>84409.30 (+0.38%)</td><td>738.41 (-17.03%)</td><td>814.12 (-0.37%)</td><td>806.76 (+0.14%)</td><td>805.90 (-0.10%)</td><td>796.34 (+0.32%)</td><td>6.97 (-17.05%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>86566.30 (n/a)</td><td>85310.26 (n/a)</td><td>85185.00 (n/a)</td><td>84093.50 (n/a)</td><td>889.95 (n/a)</td><td>817.18 (n/a)</td><td>805.59 (n/a)</td><td>806.71 (n/a)</td><td>793.84 (n/a)</td><td>8.40 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>5.70 (+1.68%)</td><td>5.12 (+0.14%)</td><td>5.30 (-1.62%)</td><td>4.17 (+2.87%)</td><td>0.60 (-4.04%)</td><td>2136.10 (-2.79%)</td><td>1763.54 (-0.31%)</td><td>1682.40 (+1.64%)</td><td>1562.60 (-1.65%)</td><td>228.07 (-8.55%)</td><td>343.57 (+1.68%)</td><td>308.16 (+0.14%)</td><td>319.10 (-1.62%)</td><td>251.33 (+2.87%)</td><td>36.28 (-4.04%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.61 (n/a)</td><td>5.11 (n/a)</td><td>5.38 (n/a)</td><td>4.06 (n/a)</td><td>0.63 (n/a)</td><td>2197.50 (n/a)</td><td>1769.00 (n/a)</td><td>1655.20 (n/a)</td><td>1588.80 (n/a)</td><td>249.39 (n/a)</td><td>337.91 (n/a)</td><td>307.74 (n/a)</td><td>324.35 (n/a)</td><td>244.31 (n/a)</td><td>37.80 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>4.54 (-3.70%)</td><td>3.14 (+14.22%)</td><td>3.14 <b>(+38.74%)</b></td><td>2.13 (-0.21%)</td><td>0.99 (-11.04%)</td><td>4194.10 (+0.21%)</td><td>3065.96 (-13.50%)</td><td>2838.00 <b>(-27.92%)</b></td><td>1962.30 (+3.85%)</td><td>935.78 (-1.87%)</td><td>273.60 (-3.70%)</td><td>189.28 (+14.22%)</td><td>189.17 <b>(+38.74%)</b></td><td>128.01 (-0.21%)</td><td>59.34 (-11.04%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>4.72 (n/a)</td><td>2.75 (n/a)</td><td>2.26 (n/a)</td><td>2.13 (n/a)</td><td>1.11 (n/a)</td><td>4185.40 (n/a)</td><td>3544.62 (n/a)</td><td>3937.30 (n/a)</td><td>1889.60 (n/a)</td><td>953.58 (n/a)</td><td>284.12 (n/a)</td><td>165.71 (n/a)</td><td>136.35 (n/a)</td><td>128.27 (n/a)</td><td>66.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>5.62 (+0.50%)</td><td>4.65 <b>(+27.27%)</b></td><td>4.17 (+15.53%)</td><td>3.83 <b>(+84.85%)</b></td><td>0.85 <b>(-41.94%)</b></td><td>2330.00 <b>(-45.90%)</b></td><td>1965.54 <b>(-29.76%)</b></td><td>2136.10 (-13.44%)</td><td>1587.10 (-0.50%)</td><td>343.60 <b>(-70.29%)</b></td><td>338.27 (+0.50%)</td><td>280.32 <b>(+27.27%)</b></td><td>251.34 (+15.53%)</td><td>230.41 <b>(+84.85%)</b></td><td>51.44 <b>(-41.94%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.59 (n/a)</td><td>3.66 (n/a)</td><td>3.61 (n/a)</td><td>2.07 (n/a)</td><td>1.47 (n/a)</td><td>4307.10 (n/a)</td><td>2798.34 (n/a)</td><td>2467.80 (n/a)</td><td>1595.00 (n/a)</td><td>1156.41 (n/a)</td><td>336.59 (n/a)</td><td>220.26 (n/a)</td><td>217.55 (n/a)</td><td>124.65 (n/a)</td><td>88.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>6.02 (-8.59%)</td><td>5.52 (-4.27%)</td><td>5.45 (-0.66%)</td><td>5.13 (-1.83%)</td><td>0.37 <b>(-37.60%)</b></td><td>6798.50 (+1.86%)</td><td>6337.98 (+3.98%)</td><td>6396.20 (+0.66%)</td><td>5789.50 (+9.39%)</td><td>418.09 <b>(-30.49%)</b></td><td>370.93 (-8.59%)</td><td>340.03 (-4.27%)</td><td>335.75 (-0.66%)</td><td>315.87 (-1.83%)</td><td>22.80 <b>(-37.60%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>6.59 (n/a)</td><td>5.77 (n/a)</td><td>5.49 (n/a)</td><td>5.22 (n/a)</td><td>0.59 (n/a)</td><td>6674.40 (n/a)</td><td>6095.52 (n/a)</td><td>6354.20 (n/a)</td><td>5292.30 (n/a)</td><td>601.48 (n/a)</td><td>405.77 (n/a)</td><td>355.18 (n/a)</td><td>337.96 (n/a)</td><td>321.75 (n/a)</td><td>36.53 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>5.47 (+4.23%)</td><td>4.57 (-4.28%)</td><td>4.50 (-8.09%)</td><td>3.47 (-9.64%)</td><td>0.75 <b>(+34.91%)</b></td><td>10049.20 (+10.67%)</td><td>7816.28 (+5.66%)</td><td>7753.50 (+8.81%)</td><td>6370.60 (-4.06%)</td><td>1403.02 <b>(+42.80%)</b></td><td>337.09 (+4.23%)</td><td>281.34 (-4.28%)</td><td>276.97 (-8.09%)</td><td>213.70 (-9.64%)</td><td>46.47 <b>(+34.91%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.25 (n/a)</td><td>4.77 (n/a)</td><td>4.89 (n/a)</td><td>3.84 (n/a)</td><td>0.56 (n/a)</td><td>9080.60 (n/a)</td><td>7397.86 (n/a)</td><td>7126.00 (n/a)</td><td>6639.90 (n/a)</td><td>982.49 (n/a)</td><td>323.42 (n/a)</td><td>293.93 (n/a)</td><td>301.36 (n/a)</td><td>236.49 (n/a)</td><td>34.45 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>6.55 (+3.17%)</td><td>5.74 (+6.66%)</td><td>6.04 (+14.94%)</td><td>3.99 (-14.74%)</td><td>1.00 <b>(+37.10%)</b></td><td>8746.10 (+17.29%)</td><td>6273.92 (-4.63%)</td><td>5776.10 (-12.99%)</td><td>5324.30 (-3.08%)</td><td>1396.85 <b>(+60.14%)</b></td><td>403.34 (+3.17%)</td><td>353.26 (+6.66%)</td><td>371.79 (+14.94%)</td><td>245.54 (-14.74%)</td><td>61.84 <b>(+37.10%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>6.35 (n/a)</td><td>5.38 (n/a)</td><td>5.25 (n/a)</td><td>4.68 (n/a)</td><td>0.73 (n/a)</td><td>7456.90 (n/a)</td><td>6578.50 (n/a)</td><td>6638.80 (n/a)</td><td>5493.30 (n/a)</td><td>872.26 (n/a)</td><td>390.93 (n/a)</td><td>331.21 (n/a)</td><td>323.47 (n/a)</td><td>287.98 (n/a)</td><td>45.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.77 (-0.46%)</td><td>0.74 (-1.43%)</td><td>0.76 (+1.19%)</td><td>0.71 (-3.60%)</td><td>0.03 <b>(+84.17%)</b></td><td>106004.40 (+3.73%)</td><td>101483.68 (+1.54%)</td><td>99390.60 (-1.18%)</td><td>97547.30 (+0.46%)</td><td>3995.64 <b>(+93.20%)</b></td><td>704.47 (-0.46%)</td><td>677.98 (-1.43%)</td><td>691.41 (+1.19%)</td><td>648.27 (-3.60%)</td><td>26.40 <b>(+84.17%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>102190.80 (n/a)</td><td>99946.48 (n/a)</td><td>100575.60 (n/a)</td><td>97099.50 (n/a)</td><td>2068.15 (n/a)</td><td>707.72 (n/a)</td><td>687.80 (n/a)</td><td>683.26 (n/a)</td><td>672.46 (n/a)</td><td>14.33 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.78 (+0.66%)</td><td>0.76 (+0.59%)</td><td>0.76 (+0.48%)</td><td>0.75 (+0.48%)</td><td>0.01 (+7.91%)</td><td>100936.90 (-0.47%)</td><td>99053.78 (-0.59%)</td><td>99558.90 (-0.47%)</td><td>97340.20 (-0.65%)</td><td>1462.05 (+6.65%)</td><td>705.97 (+0.66%)</td><td>693.88 (+0.59%)</td><td>690.24 (+0.48%)</td><td>680.82 (+0.48%)</td><td>10.24 (+7.91%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.74 (n/a)</td><td>0.01 (n/a)</td><td>101416.50 (n/a)</td><td>99639.76 (n/a)</td><td>100033.00 (n/a)</td><td>97977.80 (n/a)</td><td>1370.88 (n/a)</td><td>701.38 (n/a)</td><td>689.78 (n/a)</td><td>686.97 (n/a)</td><td>677.60 (n/a)</td><td>9.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.90 (-0.88%)</td><td>0.88 (-1.52%)</td><td>0.88 (-1.49%)</td><td>0.86 (-3.64%)</td><td>0.02 <b>(+146.05%)</b></td><td>88162.90 (+3.78%)</td><td>85656.82 (+1.56%)</td><td>85388.40 (+1.51%)</td><td>84351.70 (+0.88%)</td><td>1498.08 <b>(+157.83%)</b></td><td>814.68 (-0.88%)</td><td>802.46 (-1.52%)</td><td>804.79 (-1.49%)</td><td>779.46 (-3.64%)</td><td>13.81 <b>(+146.05%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>84949.90 (n/a)</td><td>84337.92 (n/a)</td><td>84116.00 (n/a)</td><td>83612.40 (n/a)</td><td>581.04 (n/a)</td><td>821.88 (n/a)</td><td>814.84 (n/a)</td><td>816.96 (n/a)</td><td>808.94 (n/a)</td><td>5.61 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.70 (-15.37%)</td><td>2.33 (-14.55%)</td><td>2.12 (+1.33%)</td><td>1.59 (-17.82%)</td><td>0.85 <b>(-20.65%)</b></td><td>5079.60 <b>(+21.68%)</b></td><td>3788.26 (+15.41%)</td><td>3803.10 (-1.31%)</td><td>2177.90 (+18.16%)</td><td>1174.52 (+10.50%)</td><td>970.61 (-15.37%)</td><td>611.82 (-14.55%)</td><td>555.84 (+1.33%)</td><td>416.16 (-17.82%)</td><td>223.71 <b>(-20.65%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>4.37 (n/a)</td><td>2.73 (n/a)</td><td>2.09 (n/a)</td><td>1.93 (n/a)</td><td>1.08 (n/a)</td><td>4174.50 (n/a)</td><td>3282.38 (n/a)</td><td>3853.70 (n/a)</td><td>1843.20 (n/a)</td><td>1062.88 (n/a)</td><td>1146.91 (n/a)</td><td>716.01 (n/a)</td><td>548.54 (n/a)</td><td>506.39 (n/a)</td><td>281.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.25 (-10.58%)</td><td>0.20 (+1.92%)</td><td>0.20 (+6.77%)</td><td>0.16 (+7.53%)</td><td>0.04 <b>(-20.64%)</b></td><td>7691.60 (-7.00%)</td><td>6309.16 (-3.12%)</td><td>6366.80 (-6.34%)</td><td>4981.50 (+11.83%)</td><td>1174.16 (-14.86%)</td><td>13.47 (-10.58%)</td><td>10.94 (+1.92%)</td><td>10.54 (+6.77%)</td><td>8.72 (+7.53%)</td><td>2.07 <b>(-20.64%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>8270.90 (n/a)</td><td>6512.32 (n/a)</td><td>6798.00 (n/a)</td><td>4454.70 (n/a)</td><td>1379.15 (n/a)</td><td>15.06 (n/a)</td><td>10.74 (n/a)</td><td>9.87 (n/a)</td><td>8.11 (n/a)</td><td>2.61 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.91 (n/a)</td><td>3.61 (n/a)</td><td>3.68 (n/a)</td><td>3.38 (n/a)</td><td>0.22 (n/a)</td><td>3.91 (n/a)</td><td>3.61 (n/a)</td><td>3.68 (n/a)</td><td>3.38 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>7.42 (-3.35%)</td><td>6.73 (-3.11%)</td><td>7.17 (+2.71%)</td><td>5.62 (-4.60%)</td><td>0.79 (+11.16%)</td><td>7.41 (-3.35%)</td><td>6.73 (-3.11%)</td><td>7.16 (+2.71%)</td><td>5.62 (-4.60%)</td><td>0.79 (+11.16%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>7.68 (n/a)</td><td>6.95 (n/a)</td><td>6.98 (n/a)</td><td>5.89 (n/a)</td><td>0.71 (n/a)</td><td>7.67 (n/a)</td><td>6.94 (n/a)</td><td>6.97 (n/a)</td><td>5.89 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>13.86 (-4.49%)</td><td>10.87 (+4.74%)</td><td>9.85 (+19.01%)</td><td>8.60 (+17.68%)</td><td>2.43 <b>(-28.69%)</b></td><td>13.85 (-4.49%)</td><td>10.87 (+4.74%)</td><td>9.85 (+19.01%)</td><td>8.59 (+17.68%)</td><td>2.42 <b>(-28.69%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>14.51 (n/a)</td><td>10.38 (n/a)</td><td>8.28 (n/a)</td><td>7.31 (n/a)</td><td>3.40 (n/a)</td><td>14.50 (n/a)</td><td>10.38 (n/a)</td><td>8.27 (n/a)</td><td>7.30 (n/a)</td><td>3.40 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.71 (n/a)</td><td>3.45 (n/a)</td><td>3.44 (n/a)</td><td>3.25 (n/a)</td><td>0.18 (n/a)</td><td>3.71 (n/a)</td><td>3.45 (n/a)</td><td>3.44 (n/a)</td><td>3.25 (n/a)</td><td>0.18 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>7.52 (+1.36%)</td><td>6.72 (+3.01%)</td><td>6.71 (+8.84%)</td><td>5.68 (-1.80%)</td><td>0.68 (-13.78%)</td><td>7.52 (+1.36%)</td><td>6.72 (+3.01%)</td><td>6.70 (+8.84%)</td><td>5.68 (-1.80%)</td><td>0.68 (-13.78%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>7.42 (n/a)</td><td>6.52 (n/a)</td><td>6.16 (n/a)</td><td>5.79 (n/a)</td><td>0.79 (n/a)</td><td>7.42 (n/a)</td><td>6.52 (n/a)</td><td>6.16 (n/a)</td><td>5.78 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>13.81 (-0.45%)</td><td>13.08 <b>(+38.09%)</b></td><td>13.68 <b>(+62.42%)</b></td><td>10.97 <b>(+33.86%)</b></td><td>1.20 <b>(-51.10%)</b></td><td>13.80 (-0.45%)</td><td>13.07 <b>(+38.09%)</b></td><td>13.67 <b>(+62.42%)</b></td><td>10.96 <b>(+33.86%)</b></td><td>1.20 <b>(-51.10%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>13.87 (n/a)</td><td>9.47 (n/a)</td><td>8.42 (n/a)</td><td>8.19 (n/a)</td><td>2.46 (n/a)</td><td>13.86 (n/a)</td><td>9.47 (n/a)</td><td>8.41 (n/a)</td><td>8.19 (n/a)</td><td>2.46 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.91 (-4.43%)</td><td>1.60 <b>(-35.60%)</b></td><td>1.19 <b>(-57.72%)</b></td><td>1.00 (-2.44%)</td><td>0.78 (-6.51%)</td><td>2.91 (-4.43%)</td><td>1.60 <b>(-35.60%)</b></td><td>1.19 <b>(-57.72%)</b></td><td>1.00 (-2.44%)</td><td>0.78 (-6.51%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.05 (n/a)</td><td>2.49 (n/a)</td><td>2.82 (n/a)</td><td>1.03 (n/a)</td><td>0.83 (n/a)</td><td>3.04 (n/a)</td><td>2.48 (n/a)</td><td>2.82 (n/a)</td><td>1.03 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.56 (+5.76%)</td><td>0.30 <b>(-36.73%)</b></td><td>0.32 <b>(-37.07%)</b></td><td>0.08 <b>(-76.81%)</b></td><td>0.18 <b>(+117.89%)</b></td><td>0.55 (+5.76%)</td><td>0.30 <b>(-36.73%)</b></td><td>0.31 <b>(-37.07%)</b></td><td>0.08 <b>(-76.81%)</b></td><td>0.17 <b>(+117.89%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.53 (n/a)</td><td>0.48 (n/a)</td><td>0.50 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td><td>0.52 (n/a)</td><td>0.47 (n/a)</td><td>0.50 (n/a)</td><td>0.33 (n/a)</td><td>0.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.69 (-10.54%)</td><td>0.42 <b>(-36.56%)</b></td><td>0.41 <b>(-43.50%)</b></td><td>0.08 <b>(-80.22%)</b></td><td>0.25 <b>(+60.39%)</b></td><td>0.68 (-10.54%)</td><td>0.41 <b>(-36.56%)</b></td><td>0.40 <b>(-43.50%)</b></td><td>0.08 <b>(-80.22%)</b></td><td>0.24 <b>(+60.39%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.77 (n/a)</td><td>0.66 (n/a)</td><td>0.72 (n/a)</td><td>0.39 (n/a)</td><td>0.15 (n/a)</td><td>0.76 (n/a)</td><td>0.65 (n/a)</td><td>0.71 (n/a)</td><td>0.38 (n/a)</td><td>0.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.59 <b>(-37.18%)</b></td><td>0.97 <b>(-35.00%)</b></td><td>0.88 <b>(-44.23%)</b></td><td>0.42 (-2.37%)</td><td>0.56 <b>(-45.73%)</b></td><td>1.56 <b>(-37.18%)</b></td><td>0.95 <b>(-35.00%)</b></td><td>0.86 <b>(-44.23%)</b></td><td>0.41 (-2.37%)</td><td>0.55 <b>(-45.73%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>2.53 (n/a)</td><td>1.49 (n/a)</td><td>1.57 (n/a)</td><td>0.43 (n/a)</td><td>1.03 (n/a)</td><td>2.49 (n/a)</td><td>1.47 (n/a)</td><td>1.55 (n/a)</td><td>0.42 (n/a)</td><td>1.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.80 (n/a)</td><td>386.44 (n/a)</td><td>397.10 (n/a)</td><td>220.80 (n/a)</td><td>155.69 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>481.40 (n/a)</td><td>361.34 (n/a)</td><td>346.00 (n/a)</td><td>239.80 (n/a)</td><td>113.25 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>545.10 (n/a)</td><td>316.06 (n/a)</td><td>252.90 (n/a)</td><td>222.00 (n/a)</td><td>133.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>980.70 (n/a)</td><td>496.16 (n/a)</td><td>484.60 (n/a)</td><td>170.40 (n/a)</td><td>313.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>511.20 (n/a)</td><td>405.64 (n/a)</td><td>449.30 (n/a)</td><td>248.40 (n/a)</td><td>112.57 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.30 (n/a)</td><td>406.30 (n/a)</td><td>469.80 (n/a)</td><td>226.20 (n/a)</td><td>131.22 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>428.90 (n/a)</td><td>279.94 (n/a)</td><td>246.60 (n/a)</td><td>228.10 (n/a)</td><td>83.85 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>564.40 (n/a)</td><td>381.16 (n/a)</td><td>333.40 (n/a)</td><td>252.60 (n/a)</td><td>135.90 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>451.00 (n/a)</td><td>303.84 (n/a)</td><td>299.00 (n/a)</td><td>179.30 (n/a)</td><td>96.72 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>490.30 (n/a)</td><td>337.00 (n/a)</td><td>293.50 (n/a)</td><td>191.30 (n/a)</td><td>136.63 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1824.50 (n/a)</td><td>596.18 (n/a)</td><td>294.80 (n/a)</td><td>144.50 (n/a)</td><td>694.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>487.10 (n/a)</td><td>391.94 (n/a)</td><td>376.60 (n/a)</td><td>285.80 (n/a)</td><td>88.01 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>695.90 (n/a)</td><td>468.90 (n/a)</td><td>472.20 (n/a)</td><td>220.20 (n/a)</td><td>196.98 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>620.50 (n/a)</td><td>421.00 (n/a)</td><td>458.30 (n/a)</td><td>245.60 (n/a)</td><td>151.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>581.20 (n/a)</td><td>367.24 (n/a)</td><td>261.50 (n/a)</td><td>203.60 (n/a)</td><td>176.07 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>490.80 (n/a)</td><td>333.10 (n/a)</td><td>281.70 (n/a)</td><td>248.60 (n/a)</td><td>100.27 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>593.10 (n/a)</td><td>391.54 (n/a)</td><td>339.80 (n/a)</td><td>265.90 (n/a)</td><td>142.77 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>583.10 (n/a)</td><td>409.98 (n/a)</td><td>410.90 (n/a)</td><td>232.10 (n/a)</td><td>132.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>697.10 (n/a)</td><td>581.76 (n/a)</td><td>554.00 (n/a)</td><td>499.10 (n/a)</td><td>81.26 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>515.10 (n/a)</td><td>346.10 (n/a)</td><td>293.90 (n/a)</td><td>188.00 (n/a)</td><td>137.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2532.20 (n/a)</td><td>864.76 (n/a)</td><td>580.40 (n/a)</td><td>277.80 (n/a)</td><td>942.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>614.90 (n/a)</td><td>333.84 (n/a)</td><td>247.10 (n/a)</td><td>234.50 (n/a)</td><td>162.10 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>579.30 (n/a)</td><td>413.72 (n/a)</td><td>498.80 (n/a)</td><td>219.40 (n/a)</td><td>173.95 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>940.00 (n/a)</td><td>621.68 (n/a)</td><td>604.50 (n/a)</td><td>432.00 (n/a)</td><td>197.84 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-1.35%)</td><td>0.02 <b>(+36.20%)</b></td><td>0.02 <b>(+63.68%)</b></td><td>0.01 <b>(+109.11%)</b></td><td>0.00 <b>(-82.25%)</b></td><td>282.70 <b>(-52.18%)</b></td><td>265.12 <b>(-34.39%)</b></td><td>267.90 <b>(-38.91%)</b></td><td>247.70 (+1.39%)</td><td>13.14 <b>(-90.99%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>591.20 (n/a)</td><td>404.06 (n/a)</td><td>438.50 (n/a)</td><td>244.30 (n/a)</td><td>145.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (+12.62%)</td><td>0.01 <b>(-23.34%)</b></td><td>0.01 <b>(-26.01%)</b></td><td>0.00 <b>(-74.28%)</b></td><td>0.01 <b>(+37.58%)</b></td><td>2524.00 <b>(+288.85%)</b></td><td>860.88 <b>(+114.44%)</b></td><td>557.10 <b>(+35.15%)</b></td><td>216.00 (-11.18%)</td><td>941.53 <b>(+465.54%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>649.10 (n/a)</td><td>401.46 (n/a)</td><td>412.20 (n/a)</td><td>243.20 (n/a)</td><td>166.48 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 <b>(+23.00%)</b></td><td>0.02 <b>(+30.99%)</b></td><td>0.01 (+1.95%)</td><td>0.01 <b>(+314.55%)</b></td><td>0.01 <b>(-22.79%)</b></td><td>434.80 <b>(-75.88%)</b></td><td>278.62 <b>(-54.20%)</b></td><td>275.70 (-1.92%)</td><td>167.00 (-18.70%)</td><td>98.49 <b>(-85.47%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1802.50 (n/a)</td><td>608.40 (n/a)</td><td>281.10 (n/a)</td><td>205.40 (n/a)</td><td>678.05 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (-13.44%)</td><td>0.01 (-17.91%)</td><td>0.01 <b>(-25.70%)</b></td><td>0.01 <b>(+25.91%)</b></td><td>0.00 <b>(-47.30%)</b></td><td>434.70 <b>(-20.57%)</b></td><td>369.80 (+14.27%)</td><td>361.90 <b>(+34.59%)</b></td><td>284.90 (+15.53%)</td><td>57.42 <b>(-54.45%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>547.30 (n/a)</td><td>323.62 (n/a)</td><td>268.90 (n/a)</td><td>246.60 (n/a)</td><td>126.05 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-0.92%)</td><td>0.01 (+2.57%)</td><td>0.02 <b>(+58.52%)</b></td><td>0.00 <b>(-69.11%)</b></td><td>0.01 <b>(+35.06%)</b></td><td>1926.90 <b>(+223.74%)</b></td><td>635.40 <b>(+59.36%)</b></td><td>260.40 <b>(-36.92%)</b></td><td>227.70 (+0.93%)</td><td>732.98 <b>(+348.36%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>595.20 (n/a)</td><td>398.72 (n/a)</td><td>412.80 (n/a)</td><td>225.60 (n/a)</td><td>163.48 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 <b>(+44.79%)</b></td><td>0.01 (+18.59%)</td><td>0.01 <b>(+39.46%)</b></td><td>0.00 <b>(-64.24%)</b></td><td>0.00 <b>(+185.85%)</b></td><td>1881.50 <b>(+179.65%)</b></td><td>693.94 <b>(+23.37%)</b></td><td>424.10 <b>(-28.30%)</b></td><td>301.50 <b>(-30.94%)</b></td><td>666.24 <b>(+544.64%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>672.80 (n/a)</td><td>562.50 (n/a)</td><td>591.50 (n/a)</td><td>436.60 (n/a)</td><td>103.35 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (+13.57%)</td><td>0.03 (+12.66%)</td><td>0.03 <b>(+20.68%)</b></td><td>0.02 (-7.58%)</td><td>0.01 <b>(+41.33%)</b></td><td>456.60 (+8.20%)</td><td>291.28 (-8.10%)</td><td>255.60 (-17.15%)</td><td>205.90 (-11.93%)</td><td>97.08 <b>(+41.18%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>422.00 (n/a)</td><td>316.96 (n/a)</td><td>308.50 (n/a)</td><td>233.80 (n/a)</td><td>68.77 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 <b>(+57.36%)</b></td><td>0.02 <b>(+43.05%)</b></td><td>0.03 <b>(+46.60%)</b></td><td>0.02 <b>(+29.99%)</b></td><td>0.01 <b>(+125.37%)</b></td><td>445.30 <b>(-23.06%)</b></td><td>349.88 <b>(-27.98%)</b></td><td>324.70 <b>(-31.79%)</b></td><td>262.50 <b>(-36.46%)</b></td><td>87.13 (+15.22%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.80 (n/a)</td><td>485.82 (n/a)</td><td>476.00 (n/a)</td><td>413.10 (n/a)</td><td>75.62 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (+8.17%)</td><td>0.03 <b>(+38.06%)</b></td><td>0.03 <b>(+72.79%)</b></td><td>0.02 (-3.88%)</td><td>0.01 (+8.40%)</td><td>539.80 (+4.05%)</td><td>314.86 <b>(-26.16%)</b></td><td>268.20 <b>(-42.11%)</b></td><td>220.40 (-7.55%)</td><td>128.82 (+17.64%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.80 (n/a)</td><td>426.42 (n/a)</td><td>463.30 (n/a)</td><td>238.40 (n/a)</td><td>109.51 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (-11.32%)</td><td>0.02 (+18.73%)</td><td>0.03 <b>(+57.31%)</b></td><td>0.01 (+2.88%)</td><td>0.01 (-12.84%)</td><td>569.30 (-2.80%)</td><td>379.40 (-16.80%)</td><td>320.50 <b>(-36.43%)</b></td><td>267.60 (+12.77%)</td><td>132.61 (-0.46%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.70 (n/a)</td><td>456.02 (n/a)</td><td>504.20 (n/a)</td><td>237.30 (n/a)</td><td>133.22 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (-5.98%)</td><td>0.02 <b>(-27.73%)</b></td><td>0.02 <b>(-39.66%)</b></td><td>0.01 <b>(-29.30%)</b></td><td>0.01 <b>(+21.01%)</b></td><td>661.90 <b>(+41.43%)</b></td><td>485.52 <b>(+45.87%)</b></td><td>483.10 <b>(+65.73%)</b></td><td>252.50 (+6.36%)</td><td>153.08 <b>(+69.02%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>468.00 (n/a)</td><td>332.84 (n/a)</td><td>291.50 (n/a)</td><td>237.40 (n/a)</td><td>90.57 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 <b>(+39.23%)</b></td><td>0.02 <b>(+24.38%)</b></td><td>0.02 <b>(+46.43%)</b></td><td>0.01 (-6.14%)</td><td>0.01 <b>(+69.61%)</b></td><td>649.20 (+6.53%)</td><td>412.00 (-12.37%)</td><td>363.80 <b>(-31.72%)</b></td><td>216.50 <b>(-28.19%)</b></td><td>183.11 <b>(+33.73%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>609.40 (n/a)</td><td>470.14 (n/a)</td><td>532.80 (n/a)</td><td>301.50 (n/a)</td><td>136.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 <b>(+27.10%)</b></td><td>0.02 (-0.47%)</td><td>0.02 (-9.57%)</td><td>0.01 (-17.21%)</td><td>0.01 <b>(+68.74%)</b></td><td>750.20 <b>(+20.81%)</b></td><td>494.40 (+11.43%)</td><td>499.10 (+10.57%)</td><td>208.80 <b>(-21.33%)</b></td><td>194.19 <b>(+52.31%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.00 (n/a)</td><td>443.70 (n/a)</td><td>451.40 (n/a)</td><td>265.40 (n/a)</td><td>127.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 <b>(-25.90%)</b></td><td>0.02 (-9.09%)</td><td>0.01 (+5.95%)</td><td>0.01 <b>(-36.23%)</b></td><td>0.01 <b>(-20.55%)</b></td><td>991.00 <b>(+56.80%)</b></td><td>552.08 (+12.78%)</td><td>580.40 (-5.63%)</td><td>285.10 <b>(+34.99%)</b></td><td>285.28 <b>(+49.38%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>632.00 (n/a)</td><td>489.54 (n/a)</td><td>615.00 (n/a)</td><td>211.20 (n/a)</td><td>190.98 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 <b>(+28.31%)</b></td><td>0.06 <b>(+62.47%)</b></td><td>0.06 <b>(+65.42%)</b></td><td>0.04 <b>(+84.92%)</b></td><td>0.01 (-10.97%)</td><td>366.90 <b>(-45.92%)</b></td><td>286.02 <b>(-41.05%)</b></td><td>284.30 <b>(-39.56%)</b></td><td>235.70 <b>(-22.06%)</b></td><td>51.90 <b>(-61.49%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>678.40 (n/a)</td><td>485.16 (n/a)</td><td>470.40 (n/a)</td><td>302.40 (n/a)</td><td>134.77 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (+15.18%)</td><td>0.05 (+16.08%)</td><td>0.05 <b>(+32.51%)</b></td><td>0.03 (+8.71%)</td><td>0.02 <b>(+28.06%)</b></td><td>576.70 (-8.01%)</td><td>397.96 (-10.36%)</td><td>358.80 <b>(-24.53%)</b></td><td>226.20 (-13.20%)</td><td>166.60 (+9.45%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>626.90 (n/a)</td><td>443.94 (n/a)</td><td>475.40 (n/a)</td><td>260.60 (n/a)</td><td>152.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 <b>(-39.73%)</b></td><td>0.04 <b>(-24.37%)</b></td><td>0.04 <b>(-23.93%)</b></td><td>0.03 (-9.85%)</td><td>0.01 <b>(-69.01%)</b></td><td>518.90 (+10.92%)</td><td>426.06 <b>(+22.93%)</b></td><td>409.90 <b>(+31.46%)</b></td><td>371.70 <b>(+65.86%)</b></td><td>60.81 <b>(-46.78%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>467.80 (n/a)</td><td>346.60 (n/a)</td><td>311.80 (n/a)</td><td>224.10 (n/a)</td><td>114.26 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (-7.76%)</td><td>0.04 (-7.25%)</td><td>0.03 (-10.45%)</td><td>0.03 (-3.75%)</td><td>0.01 (-5.65%)</td><td>564.50 (+3.90%)</td><td>457.90 (+8.28%)</td><td>540.10 (+11.68%)</td><td>270.00 (+8.39%)</td><td>137.08 (+11.01%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>543.30 (n/a)</td><td>422.88 (n/a)</td><td>483.60 (n/a)</td><td>249.10 (n/a)</td><td>123.48 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 <b>(+36.34%)</b></td><td>0.05 <b>(+40.08%)</b></td><td>0.04 <b>(+31.82%)</b></td><td>0.03 (+7.15%)</td><td>0.01 <b>(+107.38%)</b></td><td>539.50 (-6.68%)</td><td>372.50 <b>(-25.72%)</b></td><td>377.40 <b>(-24.13%)</b></td><td>276.50 <b>(-26.66%)</b></td><td>108.08 <b>(+37.90%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>578.10 (n/a)</td><td>501.50 (n/a)</td><td>497.40 (n/a)</td><td>377.00 (n/a)</td><td>78.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 <b>(+23.53%)</b></td><td>0.03 (-4.37%)</td><td>0.03 (+12.69%)</td><td>0.01 <b>(-74.98%)</b></td><td>0.01 <b>(+651.90%)</b></td><td>2241.80 <b>(+299.68%)</b></td><td>831.10 <b>(+55.19%)</b></td><td>489.80 (-11.27%)</td><td>399.00 (-19.05%)</td><td>791.12 <b>(+2581.61%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>560.90 (n/a)</td><td>535.54 (n/a)</td><td>552.00 (n/a)</td><td>492.90 (n/a)</td><td>29.50 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.17 <b>(+39.15%)</b></td><td>0.10 <b>(+36.76%)</b></td><td>0.09 <b>(+45.57%)</b></td><td>0.05 (-3.54%)</td><td>0.05 <b>(+65.73%)</b></td><td>627.80 (+3.67%)</td><td>395.92 <b>(-20.46%)</b></td><td>380.00 <b>(-31.31%)</b></td><td>192.90 <b>(-28.16%)</b></td><td>174.27 <b>(+27.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>605.60 (n/a)</td><td>497.78 (n/a)</td><td>553.20 (n/a)</td><td>268.50 (n/a)</td><td>136.85 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (-16.79%)</td><td>0.10 <b>(+33.47%)</b></td><td>0.12 <b>(+82.98%)</b></td><td>0.06 <b>(+38.57%)</b></td><td>0.03 <b>(-34.61%)</b></td><td>524.10 <b>(-27.83%)</b></td><td>344.08 <b>(-32.08%)</b></td><td>274.40 <b>(-45.34%)</b></td><td>264.90 <b>(+20.19%)</b></td><td>112.30 <b>(-41.53%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>726.20 (n/a)</td><td>506.62 (n/a)</td><td>502.00 (n/a)</td><td>220.40 (n/a)</td><td>192.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 <b>(+23.29%)</b></td><td>0.10 <b>(+44.65%)</b></td><td>0.09 <b>(+50.79%)</b></td><td>0.07 <b>(+27.94%)</b></td><td>0.02 <b>(+27.22%)</b></td><td>458.60 <b>(-21.83%)</b></td><td>346.22 <b>(-30.79%)</b></td><td>351.70 <b>(-33.68%)</b></td><td>272.10 (-18.87%)</td><td>78.11 (-18.92%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>586.70 (n/a)</td><td>500.28 (n/a)</td><td>530.30 (n/a)</td><td>335.40 (n/a)</td><td>96.34 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (-6.62%)</td><td>0.10 (+5.54%)</td><td>0.11 (+16.87%)</td><td>0.07 (+2.15%)</td><td>0.02 (-8.53%)</td><td>496.80 (-2.09%)</td><td>349.78 (-5.99%)</td><td>300.00 (-14.43%)</td><td>274.10 (+7.11%)</td><td>95.27 (-6.22%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>507.40 (n/a)</td><td>372.06 (n/a)</td><td>350.60 (n/a)</td><td>255.90 (n/a)</td><td>101.58 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (+1.11%)</td><td>0.09 <b>(+22.94%)</b></td><td>0.09 <b>(+36.91%)</b></td><td>0.07 <b>(+22.66%)</b></td><td>0.02 <b>(-21.43%)</b></td><td>467.00 (-18.48%)</td><td>369.22 <b>(-21.78%)</b></td><td>373.60 <b>(-26.95%)</b></td><td>255.20 (-1.09%)</td><td>82.05 <b>(-33.37%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>572.90 (n/a)</td><td>472.02 (n/a)</td><td>511.40 (n/a)</td><td>258.00 (n/a)</td><td>123.14 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-1.50%)</td><td>0.01 (-16.82%)</td><td>0.01 <b>(-25.91%)</b></td><td>0.00 <b>(-54.97%)</b></td><td>0.01 <b>(+24.77%)</b></td><td>1136.90 <b>(+122.05%)</b></td><td>506.02 <b>(+46.71%)</b></td><td>355.10 <b>(+34.97%)</b></td><td>248.60 (+1.51%)</td><td>367.67 <b>(+190.70%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.00 (n/a)</td><td>344.90 (n/a)</td><td>263.10 (n/a)</td><td>244.90 (n/a)</td><td>126.48 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-4.37%)</td><td>0.01 (+13.57%)</td><td>0.02 (+14.15%)</td><td>0.01 (+7.70%)</td><td>0.00 (-14.74%)</td><td>511.90 (-7.15%)</td><td>325.62 (-15.11%)</td><td>262.70 (-12.40%)</td><td>256.20 (+4.57%)</td><td>110.08 <b>(-23.61%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>551.30 (n/a)</td><td>383.60 (n/a)</td><td>299.90 (n/a)</td><td>245.00 (n/a)</td><td>144.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (+6.80%)</td><td>0.01 (+13.85%)</td><td>0.01 <b>(+24.77%)</b></td><td>0.01 (+2.79%)</td><td>0.00 (+14.19%)</td><td>497.00 (-2.72%)</td><td>343.14 (-10.90%)</td><td>294.40 (-19.87%)</td><td>223.60 (-6.37%)</td><td>119.05 (+3.45%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>510.90 (n/a)</td><td>385.12 (n/a)</td><td>367.40 (n/a)</td><td>238.80 (n/a)</td><td>115.09 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (-19.44%)</td><td>0.01 <b>(-22.66%)</b></td><td>0.01 <b>(-29.56%)</b></td><td>0.01 <b>(+22.57%)</b></td><td>0.00 <b>(-47.98%)</b></td><td>455.00 (-18.41%)</td><td>402.78 <b>(+21.24%)</b></td><td>420.50 <b>(+41.96%)</b></td><td>297.70 <b>(+24.15%)</b></td><td>62.32 <b>(-51.58%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>557.70 (n/a)</td><td>332.22 (n/a)</td><td>296.20 (n/a)</td><td>239.80 (n/a)</td><td>128.72 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-8.56%)</td><td>0.01 (-18.84%)</td><td>0.01 <b>(-40.19%)</b></td><td>0.01 (-15.66%)</td><td>0.00 (-4.62%)</td><td>519.30 (+18.56%)</td><td>376.74 <b>(+24.73%)</b></td><td>429.70 <b>(+67.20%)</b></td><td>218.60 (+9.35%)</td><td>127.78 (+19.30%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>438.00 (n/a)</td><td>302.04 (n/a)</td><td>257.00 (n/a)</td><td>199.90 (n/a)</td><td>107.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (-19.30%)</td><td>0.01 (-16.67%)</td><td>0.01 <b>(-27.44%)</b></td><td>0.01 (+6.17%)</td><td>0.00 <b>(-51.35%)</b></td><td>423.00 (-5.81%)</td><td>385.40 (+14.50%)</td><td>406.50 <b>(+37.84%)</b></td><td>295.50 <b>(+23.90%)</b></td><td>51.26 <b>(-46.90%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>449.10 (n/a)</td><td>336.60 (n/a)</td><td>294.90 (n/a)</td><td>238.50 (n/a)</td><td>96.53 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (+16.93%)</td><td>0.01 <b>(+25.68%)</b></td><td>0.01 <b>(+47.19%)</b></td><td>0.01 (-1.63%)</td><td>0.00 (+6.84%)</td><td>570.20 (+1.64%)</td><td>334.14 <b>(-20.15%)</b></td><td>302.60 <b>(-32.06%)</b></td><td>222.50 (-14.49%)</td><td>136.29 (-0.31%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>561.00 (n/a)</td><td>418.48 (n/a)</td><td>445.40 (n/a)</td><td>260.20 (n/a)</td><td>136.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 <b>(+20.91%)</b></td><td>0.01 <b>(+44.72%)</b></td><td>0.01 <b>(+49.15%)</b></td><td>0.00 <b>(+111.64%)</b></td><td>0.01 (+19.27%)</td><td>981.40 <b>(-52.75%)</b></td><td>434.42 <b>(-42.57%)</b></td><td>299.60 <b>(-32.95%)</b></td><td>241.90 (-17.27%)</td><td>311.44 <b>(-58.09%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2076.90 (n/a)</td><td>756.44 (n/a)</td><td>446.80 (n/a)</td><td>292.40 (n/a)</td><td>743.20 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 <b>(-28.39%)</b></td><td>0.01 <b>(-32.76%)</b></td><td>0.01 <b>(-38.94%)</b></td><td>0.01 (-18.73%)</td><td>0.00 <b>(-36.54%)</b></td><td>550.50 <b>(+23.04%)</b></td><td>474.50 <b>(+47.13%)</b></td><td>489.80 <b>(+63.76%)</b></td><td>368.70 <b>(+39.66%)</b></td><td>76.51 (+5.65%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>447.40 (n/a)</td><td>322.50 (n/a)</td><td>299.10 (n/a)</td><td>264.00 (n/a)</td><td>72.41 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-6.14%)</td><td>0.01 (-15.57%)</td><td>0.01 (-10.56%)</td><td>0.01 <b>(-20.77%)</b></td><td>0.00 (+3.63%)</td><td>598.40 <b>(+26.22%)</b></td><td>447.20 <b>(+20.97%)</b></td><td>417.90 (+11.80%)</td><td>268.50 (+6.55%)</td><td>128.56 <b>(+36.83%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>474.10 (n/a)</td><td>369.68 (n/a)</td><td>373.80 (n/a)</td><td>252.00 (n/a)</td><td>93.95 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 <b>(+47.29%)</b></td><td>0.01 <b>(+20.76%)</b></td><td>0.01 <b>(+27.39%)</b></td><td>0.01 (+6.75%)</td><td>0.00 <b>(+121.54%)</b></td><td>626.20 (-6.33%)</td><td>490.12 (-14.57%)</td><td>470.40 <b>(-21.50%)</b></td><td>331.50 <b>(-32.11%)</b></td><td>111.39 <b>(+42.23%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>668.50 (n/a)</td><td>573.70 (n/a)</td><td>599.20 (n/a)</td><td>488.30 (n/a)</td><td>78.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (-3.82%)</td><td>0.02 (+0.99%)</td><td>0.02 <b>(+21.77%)</b></td><td>0.01 (-8.07%)</td><td>0.01 (+0.96%)</td><td>978.20 (+8.77%)</td><td>510.94 (+2.11%)</td><td>377.00 (-17.88%)</td><td>277.90 (+3.97%)</td><td>293.30 (+15.54%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>899.30 (n/a)</td><td>500.38 (n/a)</td><td>459.10 (n/a)</td><td>267.30 (n/a)</td><td>253.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 <b>(+22.76%)</b></td><td>0.02 <b>(+25.66%)</b></td><td>0.02 <b>(+31.21%)</b></td><td>0.01 (-13.04%)</td><td>0.01 <b>(+44.53%)</b></td><td>777.90 (+15.01%)</td><td>420.66 (-14.17%)</td><td>363.20 <b>(-23.79%)</b></td><td>241.10 (-18.55%)</td><td>209.09 <b>(+47.91%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>676.40 (n/a)</td><td>490.10 (n/a)</td><td>476.60 (n/a)</td><td>296.00 (n/a)</td><td>141.36 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 <b>(-22.98%)</b></td><td>0.02 <b>(-22.19%)</b></td><td>0.01 <b>(-32.87%)</b></td><td>0.01 (-12.52%)</td><td>0.01 <b>(-28.68%)</b></td><td>630.30 (+14.31%)</td><td>520.52 <b>(+24.78%)</b></td><td>575.60 <b>(+48.93%)</b></td><td>288.60 <b>(+29.82%)</b></td><td>135.16 (-2.03%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.40 (n/a)</td><td>417.16 (n/a)</td><td>386.50 (n/a)</td><td>222.30 (n/a)</td><td>137.96 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 <b>(+32.75%)</b></td><td>0.02 (+10.87%)</td><td>0.02 (-12.52%)</td><td>0.01 <b>(-36.69%)</b></td><td>0.01 <b>(+56.29%)</b></td><td>934.50 <b>(+57.93%)</b></td><td>432.70 (+5.03%)</td><td>364.10 (+14.32%)</td><td>216.40 <b>(-24.65%)</b></td><td>288.89 <b>(+94.80%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.70 (n/a)</td><td>411.98 (n/a)</td><td>318.50 (n/a)</td><td>287.20 (n/a)</td><td>148.31 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 <b>(+46.46%)</b></td><td>0.02 <b>(+39.11%)</b></td><td>0.02 <b>(+25.68%)</b></td><td>0.01 <b>(+65.45%)</b></td><td>0.01 <b>(+55.58%)</b></td><td>575.70 <b>(-39.55%)</b></td><td>392.74 <b>(-28.33%)</b></td><td>410.80 <b>(-20.43%)</b></td><td>240.70 <b>(-31.74%)</b></td><td>147.51 <b>(-39.15%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>952.40 (n/a)</td><td>548.02 (n/a)</td><td>516.30 (n/a)</td><td>352.60 (n/a)</td><td>242.42 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 <b>(+38.16%)</b></td><td>0.02 (+10.01%)</td><td>0.02 (+8.09%)</td><td>0.01 (-0.56%)</td><td>0.01 <b>(+64.68%)</b></td><td>566.30 (+0.55%)</td><td>430.92 (-3.21%)</td><td>471.50 (-7.48%)</td><td>203.80 <b>(-27.60%)</b></td><td>148.62 (+16.73%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.20 (n/a)</td><td>445.22 (n/a)</td><td>509.60 (n/a)</td><td>281.50 (n/a)</td><td>127.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (+11.39%)</td><td>0.03 (+14.32%)</td><td>0.03 (+4.66%)</td><td>0.02 <b>(+24.67%)</b></td><td>0.01 (+6.07%)</td><td>534.70 (-19.79%)</td><td>324.70 (-14.79%)</td><td>280.90 (-4.46%)</td><td>218.70 (-10.22%)</td><td>129.82 <b>(-25.43%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>666.60 (n/a)</td><td>381.06 (n/a)</td><td>294.00 (n/a)</td><td>243.60 (n/a)</td><td>174.09 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 <b>(+27.07%)</b></td><td>0.02 <b>(+29.33%)</b></td><td>0.02 (+17.63%)</td><td>0.01 (+9.10%)</td><td>0.01 <b>(+41.98%)</b></td><td>573.00 (-8.33%)</td><td>404.74 <b>(-20.40%)</b></td><td>451.20 (-15.00%)</td><td>235.50 <b>(-21.32%)</b></td><td>134.87 (+0.74%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>625.10 (n/a)</td><td>508.48 (n/a)</td><td>530.80 (n/a)</td><td>299.30 (n/a)</td><td>133.88 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (-5.28%)</td><td>0.02 (-8.77%)</td><td>0.02 <b>(+29.40%)</b></td><td>0.00 <b>(-70.42%)</b></td><td>0.01 (+15.34%)</td><td>1905.80 <b>(+238.03%)</b></td><td>665.84 <b>(+61.49%)</b></td><td>388.40 <b>(-22.72%)</b></td><td>243.20 (+5.56%)</td><td>701.15 <b>(+348.09%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.80 (n/a)</td><td>412.32 (n/a)</td><td>502.60 (n/a)</td><td>230.40 (n/a)</td><td>156.47 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 <b>(+83.93%)</b></td><td>0.03 <b>(+31.84%)</b></td><td>0.03 (+10.81%)</td><td>0.02 (-2.25%)</td><td>0.01 <b>(+134.79%)</b></td><td>543.90 (+2.29%)</td><td>313.04 (-16.08%)</td><td>285.30 (-9.77%)</td><td>151.30 <b>(-45.61%)</b></td><td>142.71 <b>(+30.32%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.70 (n/a)</td><td>373.02 (n/a)</td><td>316.20 (n/a)</td><td>278.20 (n/a)</td><td>109.50 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (+1.55%)</td><td>0.02 (-3.03%)</td><td>0.02 (+11.59%)</td><td>0.02 <b>(+24.47%)</b></td><td>0.01 <b>(-27.84%)</b></td><td>504.70 (-19.66%)</td><td>445.02 (-3.33%)</td><td>477.80 (-10.37%)</td><td>278.90 (-1.55%)</td><td>93.60 <b>(-41.77%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>628.20 (n/a)</td><td>460.34 (n/a)</td><td>533.10 (n/a)</td><td>283.30 (n/a)</td><td>160.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (+3.56%)</td><td>0.02 (-6.70%)</td><td>0.02 (+2.66%)</td><td>0.00 <b>(-68.38%)</b></td><td>0.01 <b>(+47.85%)</b></td><td>1963.70 <b>(+216.22%)</b></td><td>642.04 <b>(+73.97%)</b></td><td>332.80 (-2.60%)</td><td>215.70 (-3.40%)</td><td>742.70 <b>(+391.94%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.00 (n/a)</td><td>369.06 (n/a)</td><td>341.70 (n/a)</td><td>223.30 (n/a)</td><td>150.98 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (+4.71%)</td><td>0.06 <b>(+25.24%)</b></td><td>0.06 <b>(+34.89%)</b></td><td>0.03 (+10.02%)</td><td>0.01 (-3.15%)</td><td>472.90 (-9.11%)</td><td>308.60 <b>(-21.15%)</b></td><td>271.20 <b>(-25.86%)</b></td><td>242.70 (-4.52%)</td><td>94.68 (-16.32%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>520.30 (n/a)</td><td>391.40 (n/a)</td><td>365.80 (n/a)</td><td>254.20 (n/a)</td><td>113.14 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (+5.75%)</td><td>0.05 (+12.74%)</td><td>0.06 (+3.89%)</td><td>0.04 (+9.81%)</td><td>0.01 (-2.66%)</td><td>452.10 (-8.94%)</td><td>314.22 (-12.53%)</td><td>286.00 (-3.74%)</td><td>245.00 (-5.41%)</td><td>85.93 (-19.15%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>496.50 (n/a)</td><td>359.22 (n/a)</td><td>297.10 (n/a)</td><td>259.00 (n/a)</td><td>106.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (-1.30%)</td><td>0.04 (-14.01%)</td><td>0.03 (+8.51%)</td><td>0.01 <b>(-68.98%)</b></td><td>0.02 (+12.36%)</td><td>2086.20 <b>(+222.39%)</b></td><td>764.52 <b>(+69.49%)</b></td><td>478.90 (-7.85%)</td><td>243.60 (+1.33%)</td><td>761.69 <b>(+294.05%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>647.10 (n/a)</td><td>451.08 (n/a)</td><td>519.70 (n/a)</td><td>240.40 (n/a)</td><td>193.30 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (-13.29%)</td><td>0.04 <b>(-22.39%)</b></td><td>0.04 <b>(-41.05%)</b></td><td>0.03 (+2.06%)</td><td>0.01 (-6.52%)</td><td>519.20 (-2.00%)</td><td>400.74 <b>(+27.82%)</b></td><td>462.30 <b>(+69.65%)</b></td><td>267.50 (+15.30%)</td><td>116.98 (-4.22%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>529.80 (n/a)</td><td>313.52 (n/a)</td><td>272.50 (n/a)</td><td>232.00 (n/a)</td><td>122.14 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (-19.93%)</td><td>0.04 (-0.15%)</td><td>0.04 (+8.52%)</td><td>0.03 (+8.32%)</td><td>0.01 <b>(-26.06%)</b></td><td>498.40 (-7.69%)</td><td>389.16 (-2.33%)</td><td>387.80 (-7.84%)</td><td>280.90 <b>(+24.90%)</b></td><td>103.45 (-8.94%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>539.90 (n/a)</td><td>398.46 (n/a)</td><td>420.80 (n/a)</td><td>224.90 (n/a)</td><td>113.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (+10.78%)</td><td>0.06 (+18.81%)</td><td>0.06 (+13.09%)</td><td>0.06 <b>(+67.42%)</b></td><td>0.00 <b>(-62.03%)</b></td><td>288.30 <b>(-40.26%)</b></td><td>259.98 (-19.46%)</td><td>257.90 (-11.59%)</td><td>243.00 (-9.73%)</td><td>18.14 <b>(-79.94%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>482.60 (n/a)</td><td>322.80 (n/a)</td><td>291.70 (n/a)</td><td>269.20 (n/a)</td><td>90.41 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (-5.24%)</td><td>0.04 (-5.67%)</td><td>0.03 (-4.78%)</td><td>0.03 (-3.01%)</td><td>0.01 (-7.43%)</td><td>612.90 (+3.10%)</td><td>453.02 (+5.27%)</td><td>479.30 (+5.02%)</td><td>259.80 (+5.52%)</td><td>128.49 (-1.11%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>594.50 (n/a)</td><td>430.36 (n/a)</td><td>456.40 (n/a)</td><td>246.20 (n/a)</td><td>129.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (-12.55%)</td><td>0.05 (+18.69%)</td><td>0.05 <b>(+36.17%)</b></td><td>0.03 <b>(+125.32%)</b></td><td>0.01 <b>(-55.62%)</b></td><td>470.60 <b>(-55.62%)</b></td><td>346.38 <b>(-32.42%)</b></td><td>307.30 <b>(-26.55%)</b></td><td>294.00 (+14.35%)</td><td>73.68 <b>(-77.39%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1060.40 (n/a)</td><td>512.56 (n/a)</td><td>418.40 (n/a)</td><td>257.10 (n/a)</td><td>325.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (+16.43%)</td><td>0.05 <b>(+31.62%)</b></td><td>0.05 <b>(+45.41%)</b></td><td>0.04 <b>(+35.08%)</b></td><td>0.01 (-5.71%)</td><td>467.80 <b>(-25.98%)</b></td><td>355.38 <b>(-26.62%)</b></td><td>349.50 <b>(-31.23%)</b></td><td>253.30 (-14.11%)</td><td>84.23 <b>(-40.80%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>632.00 (n/a)</td><td>484.30 (n/a)</td><td>508.20 (n/a)</td><td>294.90 (n/a)</td><td>142.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (+1.54%)</td><td>0.05 (+7.75%)</td><td>0.04 <b>(+26.98%)</b></td><td>0.03 (-11.25%)</td><td>0.02 (-5.26%)</td><td>593.40 (+12.66%)</td><td>373.78 (-7.78%)</td><td>373.60 <b>(-21.23%)</b></td><td>218.30 (-1.53%)</td><td>138.98 (+3.77%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>526.70 (n/a)</td><td>405.32 (n/a)</td><td>474.30 (n/a)</td><td>221.70 (n/a)</td><td>133.94 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (+13.53%)</td><td>0.05 <b>(+33.04%)</b></td><td>0.05 <b>(+68.54%)</b></td><td>0.03 (+1.62%)</td><td>0.02 <b>(+40.83%)</b></td><td>533.60 (-1.59%)</td><td>372.68 <b>(-21.69%)</b></td><td>307.50 <b>(-40.68%)</b></td><td>257.00 (-11.93%)</td><td>132.43 <b>(+27.57%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>542.20 (n/a)</td><td>475.92 (n/a)</td><td>518.40 (n/a)</td><td>291.80 (n/a)</td><td>103.81 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (-18.35%)</td><td>0.04 <b>(-27.90%)</b></td><td>0.04 <b>(-35.01%)</b></td><td>0.01 <b>(-60.57%)</b></td><td>0.02 <b>(+33.91%)</b></td><td>1305.40 <b>(+153.62%)</b></td><td>578.50 <b>(+74.69%)</b></td><td>458.90 <b>(+53.89%)</b></td><td>284.20 <b>(+22.50%)</b></td><td>421.21 <b>(+290.71%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>514.70 (n/a)</td><td>331.16 (n/a)</td><td>298.20 (n/a)</td><td>232.00 (n/a)</td><td>107.81 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (-2.07%)</td><td>0.09 (-6.46%)</td><td>0.08 <b>(-28.32%)</b></td><td>0.06 (+18.01%)</td><td>0.03 (-6.39%)</td><td>507.50 (-15.26%)</td><td>385.20 (+4.40%)</td><td>415.70 <b>(+39.50%)</b></td><td>257.20 (+2.10%)</td><td>108.08 <b>(-22.64%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>598.90 (n/a)</td><td>368.98 (n/a)</td><td>298.00 (n/a)</td><td>251.90 (n/a)</td><td>139.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.16 <b>(+32.10%)</b></td><td>0.10 (+11.96%)</td><td>0.10 <b>(+20.72%)</b></td><td>0.06 (-2.49%)</td><td>0.04 <b>(+87.96%)</b></td><td>522.20 (+2.55%)</td><td>371.52 (-3.83%)</td><td>316.90 (-17.17%)</td><td>206.30 <b>(-24.32%)</b></td><td>134.62 <b>(+55.18%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>509.20 (n/a)</td><td>386.30 (n/a)</td><td>382.60 (n/a)</td><td>272.60 (n/a)</td><td>86.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.15 (-14.42%)</td><td>0.09 (-11.63%)</td><td>0.10 (+13.10%)</td><td>0.03 <b>(-39.14%)</b></td><td>0.05 (-10.08%)</td><td>1006.20 <b>(+64.30%)</b></td><td>468.06 <b>(+24.37%)</b></td><td>316.50 (-11.59%)</td><td>222.60 (+16.85%)</td><td>321.47 <b>(+81.09%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>612.40 (n/a)</td><td>376.34 (n/a)</td><td>358.00 (n/a)</td><td>190.50 (n/a)</td><td>177.52 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 <b>(-27.86%)</b></td><td>0.09 (-19.03%)</td><td>0.09 (-14.21%)</td><td>0.07 (-18.11%)</td><td>0.02 <b>(-36.69%)</b></td><td>489.80 <b>(+22.11%)</b></td><td>365.88 <b>(+21.06%)</b></td><td>370.60 (+16.54%)</td><td>273.80 <b>(+38.63%)</b></td><td>86.36 (+6.70%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>401.10 (n/a)</td><td>302.24 (n/a)</td><td>318.00 (n/a)</td><td>197.50 (n/a)</td><td>80.94 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 <b>(-24.41%)</b></td><td>0.08 <b>(-30.23%)</b></td><td>0.06 <b>(-48.75%)</b></td><td>0.06 <b>(-31.49%)</b></td><td>0.03 (+10.73%)</td><td>575.60 <b>(+45.98%)</b></td><td>452.34 <b>(+52.35%)</b></td><td>543.10 <b>(+95.08%)</b></td><td>276.80 <b>(+32.31%)</b></td><td>150.08 <b>(+116.46%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>394.30 (n/a)</td><td>296.90 (n/a)</td><td>278.40 (n/a)</td><td>209.20 (n/a)</td><td>69.34 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (+13.85%)</td><td>0.10 <b>(+29.62%)</b></td><td>0.09 <b>(+41.29%)</b></td><td>0.06 (-0.46%)</td><td>0.03 (+11.78%)</td><td>578.30 (+0.47%)</td><td>373.46 <b>(-22.20%)</b></td><td>357.50 <b>(-29.22%)</b></td><td>231.70 (-12.17%)</td><td>131.02 (+2.46%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>575.60 (n/a)</td><td>480.00 (n/a)</td><td>505.10 (n/a)</td><td>263.80 (n/a)</td><td>127.87 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.15 (+17.73%)</td><td>0.08 (-12.09%)</td><td>0.06 <b>(-45.40%)</b></td><td>0.05 <b>(+57.57%)</b></td><td>0.04 (+0.39%)</td><td>653.60 <b>(-36.54%)</b></td><td>473.84 (+1.72%)</td><td>521.40 <b>(+83.14%)</b></td><td>218.80 (-15.06%)</td><td>179.88 <b>(-45.25%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1029.90 (n/a)</td><td>465.84 (n/a)</td><td>284.70 (n/a)</td><td>257.60 (n/a)</td><td>328.56 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (-8.29%)</td><td>0.08 <b>(-27.44%)</b></td><td>0.06 <b>(-47.61%)</b></td><td>0.05 (-8.94%)</td><td>0.04 (-15.34%)</td><td>622.80 (+9.82%)</td><td>487.14 <b>(+32.41%)</b></td><td>526.70 <b>(+90.90%)</b></td><td>231.20 (+9.06%)</td><td>149.21 (-12.42%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>567.10 (n/a)</td><td>367.90 (n/a)</td><td>275.90 (n/a)</td><td>212.00 (n/a)</td><td>170.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (-6.03%)</td><td>0.09 (-7.91%)</td><td>0.07 (-19.39%)</td><td>0.07 (-5.77%)</td><td>0.03 (+2.60%)</td><td>489.50 (+6.14%)</td><td>391.82 (+9.87%)</td><td>453.30 <b>(+24.06%)</b></td><td>259.40 (+6.40%)</td><td>110.06 (+15.83%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>461.20 (n/a)</td><td>356.62 (n/a)</td><td>365.40 (n/a)</td><td>243.80 (n/a)</td><td>95.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (+11.84%)</td><td>0.11 (+17.62%)</td><td>0.11 (+2.23%)</td><td>0.08 <b>(+55.04%)</b></td><td>0.03 <b>(-22.55%)</b></td><td>430.70 <b>(-35.49%)</b></td><td>323.88 <b>(-22.44%)</b></td><td>290.80 (-2.19%)</td><td>237.80 (-10.60%)</td><td>85.76 <b>(-54.17%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>667.70 (n/a)</td><td>417.56 (n/a)</td><td>297.30 (n/a)</td><td>266.00 (n/a)</td><td>187.12 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 <b>(+30.66%)</b></td><td>0.08 (+16.24%)</td><td>0.06 (-1.61%)</td><td>0.06 (+8.15%)</td><td>0.03 <b>(+92.36%)</b></td><td>553.70 (-7.53%)</td><td>435.26 (-8.39%)</td><td>523.30 (+1.65%)</td><td>276.80 <b>(-23.45%)</b></td><td>142.29 <b>(+39.09%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>598.80 (n/a)</td><td>475.12 (n/a)</td><td>514.80 (n/a)</td><td>361.60 (n/a)</td><td>102.30 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (+5.39%)</td><td>0.08 (-6.22%)</td><td>0.07 <b>(-29.44%)</b></td><td>0.05 <b>(+29.24%)</b></td><td>0.03 (-5.87%)</td><td>624.50 <b>(-22.62%)</b></td><td>446.36 (+1.78%)</td><td>441.30 <b>(+41.76%)</b></td><td>277.70 (-5.09%)</td><td>156.17 <b>(-29.06%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>807.10 (n/a)</td><td>438.54 (n/a)</td><td>311.30 (n/a)</td><td>292.60 (n/a)</td><td>220.16 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 <b>(+45.46%)</b></td><td>0.09 <b>(+23.91%)</b></td><td>0.09 (+19.11%)</td><td>0.05 (+0.92%)</td><td>0.03 <b>(+43.93%)</b></td><td>504.00 (-0.90%)</td><td>303.82 (-16.95%)</td><td>280.00 (-16.04%)</td><td>171.30 <b>(-31.26%)</b></td><td>121.83 (+0.09%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>508.60 (n/a)</td><td>365.84 (n/a)</td><td>333.50 (n/a)</td><td>249.20 (n/a)</td><td>121.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.19 (-12.59%)</td><td>0.14 <b>(-20.82%)</b></td><td>0.12 <b>(-35.80%)</b></td><td>0.10 (-18.44%)</td><td>0.04 (-9.27%)</td><td>491.00 <b>(+22.63%)</b></td><td>385.82 <b>(+27.15%)</b></td><td>403.00 <b>(+55.78%)</b></td><td>260.70 (+14.44%)</td><td>100.82 <b>(+24.89%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>400.40 (n/a)</td><td>303.44 (n/a)</td><td>258.70 (n/a)</td><td>227.80 (n/a)</td><td>80.73 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>4.18 (-0.86%)</td><td>3.68 <b>(+22.25%)</b></td><td>3.75 <b>(+34.32%)</b></td><td>3.07 <b>(+34.36%)</b></td><td>0.51 <b>(-32.43%)</b></td><td>3419.40 <b>(-25.57%)</b></td><td>2893.84 <b>(-20.54%)</b></td><td>2796.70 <b>(-25.55%)</b></td><td>2510.40 (+0.87%)</td><td>412.87 <b>(-49.06%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>4.21 (n/a)</td><td>3.01 (n/a)</td><td>2.79 (n/a)</td><td>2.28 (n/a)</td><td>0.76 (n/a)</td><td>4594.40 (n/a)</td><td>3641.92 (n/a)</td><td>3756.60 (n/a)</td><td>2488.80 (n/a)</td><td>810.51 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.17 (+4.32%)</td><td>0.13 (-18.81%)</td><td>0.13 (-16.49%)</td><td>0.09 <b>(-35.68%)</b></td><td>0.03 <b>(+253.30%)</b></td><td>446.10 <b>(+55.49%)</b></td><td>340.38 <b>(+28.60%)</b></td><td>314.90 (+19.73%)</td><td>237.60 (-4.15%)</td><td>79.60 <b>(+426.82%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>286.90 (n/a)</td><td>264.68 (n/a)</td><td>263.00 (n/a)</td><td>247.90 (n/a)</td><td>15.11 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 <b>(+20.12%)</b></td><td>0.02 <b>(+28.15%)</b></td><td>0.02 (+18.14%)</td><td>0.01 <b>(+89.45%)</b></td><td>0.00 (-19.82%)</td><td>380.80 <b>(-47.21%)</b></td><td>291.18 <b>(-29.14%)</b></td><td>264.00 (-15.36%)</td><td>223.10 (-16.75%)</td><td>69.42 <b>(-63.81%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>721.40 (n/a)</td><td>410.94 (n/a)</td><td>311.90 (n/a)</td><td>268.00 (n/a)</td><td>191.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-8.33%)</td><td>0.01 (-15.00%)</td><td>0.01 <b>(-22.07%)</b></td><td>0.01 (+5.03%)</td><td>0.00 (-3.00%)</td><td>500.50 (-4.79%)</td><td>356.20 (+16.86%)</td><td>316.10 <b>(+28.29%)</b></td><td>249.50 (+9.09%)</td><td>119.32 (-4.58%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>525.70 (n/a)</td><td>304.80 (n/a)</td><td>246.40 (n/a)</td><td>228.70 (n/a)</td><td>125.05 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-16.92%)</td><td>0.01 <b>(-28.17%)</b></td><td>0.01 <b>(-44.70%)</b></td><td>0.01 <b>(-33.61%)</b></td><td>0.01 (+13.56%)</td><td>726.20 <b>(+50.63%)</b></td><td>477.32 <b>(+50.63%)</b></td><td>541.80 <b>(+80.84%)</b></td><td>258.10 <b>(+20.38%)</b></td><td>193.27 <b>(+91.32%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>482.10 (n/a)</td><td>316.88 (n/a)</td><td>299.60 (n/a)</td><td>214.40 (n/a)</td><td>101.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (+3.49%)</td><td>0.01 <b>(-28.14%)</b></td><td>0.01 <b>(-47.46%)</b></td><td>0.00 <b>(-70.11%)</b></td><td>0.01 <b>(+36.90%)</b></td><td>1986.70 <b>(+234.52%)</b></td><td>725.26 <b>(+107.08%)</b></td><td>529.70 <b>(+90.33%)</b></td><td>235.80 (-3.36%)</td><td>716.73 <b>(+388.18%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>593.90 (n/a)</td><td>350.24 (n/a)</td><td>278.30 (n/a)</td><td>244.00 (n/a)</td><td>146.82 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-3.56%)</td><td>0.01 (+9.21%)</td><td>0.01 <b>(+42.31%)</b></td><td>0.00 <b>(-70.02%)</b></td><td>0.01 <b>(+49.70%)</b></td><td>1928.40 <b>(+233.63%)</b></td><td>671.40 <b>(+41.57%)</b></td><td>370.30 <b>(-29.72%)</b></td><td>267.80 (+3.72%)</td><td>709.80 <b>(+464.48%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.00 (n/a)</td><td>474.26 (n/a)</td><td>526.90 (n/a)</td><td>258.20 (n/a)</td><td>125.74 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-2.86%)</td><td>0.01 (+16.63%)</td><td>0.01 (+2.41%)</td><td>0.01 (+13.22%)</td><td>0.00 (+10.78%)</td><td>591.30 (-11.68%)</td><td>430.92 (-12.32%)</td><td>516.80 (-2.36%)</td><td>246.20 (+2.93%)</td><td>166.60 (+4.47%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>669.50 (n/a)</td><td>491.46 (n/a)</td><td>529.30 (n/a)</td><td>239.20 (n/a)</td><td>159.47 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-10.57%)</td><td>0.01 <b>(-27.04%)</b></td><td>0.01 <b>(-24.14%)</b></td><td>0.00 <b>(-71.41%)</b></td><td>0.01 (+6.55%)</td><td>1793.60 <b>(+249.70%)</b></td><td>700.68 <b>(+88.69%)</b></td><td>561.60 <b>(+31.80%)</b></td><td>244.40 (+11.80%)</td><td>627.04 <b>(+359.79%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>512.90 (n/a)</td><td>371.34 (n/a)</td><td>426.10 (n/a)</td><td>218.60 (n/a)</td><td>136.37 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-7.43%)</td><td>0.01 (+9.11%)</td><td>0.01 (+9.31%)</td><td>0.01 (+16.89%)</td><td>0.00 (-16.25%)</td><td>586.20 (-14.45%)</td><td>451.42 (-11.78%)</td><td>517.10 (-8.51%)</td><td>250.10 (+8.03%)</td><td>146.17 (-14.74%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>685.20 (n/a)</td><td>511.72 (n/a)</td><td>565.20 (n/a)</td><td>231.50 (n/a)</td><td>171.43 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (+13.29%)</td><td>0.01 (+15.45%)</td><td>0.01 <b>(+31.30%)</b></td><td>0.01 (+17.93%)</td><td>0.00 (-6.37%)</td><td>492.00 (-15.20%)</td><td>344.62 (-16.38%)</td><td>312.10 <b>(-23.84%)</b></td><td>230.10 (-11.74%)</td><td>110.72 <b>(-26.72%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>580.20 (n/a)</td><td>412.12 (n/a)</td><td>409.80 (n/a)</td><td>260.70 (n/a)</td><td>151.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 <b>(-42.97%)</b></td><td>0.01 <b>(-40.10%)</b></td><td>0.01 <b>(-43.26%)</b></td><td>0.01 (-7.95%)</td><td>0.00 <b>(-66.32%)</b></td><td>563.30 (+8.64%)</td><td>469.60 <b>(+54.98%)</b></td><td>461.90 <b>(+76.23%)</b></td><td>378.40 <b>(+75.35%)</b></td><td>74.31 <b>(-39.51%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>518.50 (n/a)</td><td>303.00 (n/a)</td><td>262.10 (n/a)</td><td>215.80 (n/a)</td><td>122.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (+10.25%)</td><td>0.01 (-4.50%)</td><td>0.01 (-8.67%)</td><td>0.01 (+3.15%)</td><td>0.01 (-1.33%)</td><td>436.80 (-3.04%)</td><td>344.64 (+3.56%)</td><td>366.20 (+9.48%)</td><td>202.50 (-9.27%)</td><td>97.21 (-10.39%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>450.50 (n/a)</td><td>332.78 (n/a)</td><td>334.50 (n/a)</td><td>223.20 (n/a)</td><td>108.48 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 <b>(-41.51%)</b></td><td>0.01 <b>(-22.69%)</b></td><td>0.01 (-6.61%)</td><td>0.00 <b>(+26.22%)</b></td><td>0.00 <b>(-42.18%)</b></td><td>1893.60 <b>(-20.77%)</b></td><td>855.40 (+1.15%)</td><td>568.00 (+7.07%)</td><td>501.10 <b>(+70.97%)</b></td><td>592.40 <b>(-31.82%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2390.10 (n/a)</td><td>845.70 (n/a)</td><td>530.50 (n/a)</td><td>293.10 (n/a)</td><td>868.90 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (+8.29%)</td><td>0.02 <b>(-36.09%)</b></td><td>0.02 <b>(-54.66%)</b></td><td>0.00 <b>(-70.97%)</b></td><td>0.01 <b>(+28.25%)</b></td><td>1786.80 <b>(+244.48%)</b></td><td>733.98 <b>(+121.16%)</b></td><td>539.60 <b>(+120.51%)</b></td><td>186.00 (-7.65%)</td><td>613.18 <b>(+300.64%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.70 (n/a)</td><td>331.88 (n/a)</td><td>244.70 (n/a)</td><td>201.40 (n/a)</td><td>153.05 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 <b>(+30.02%)</b></td><td>0.05 <b>(+32.82%)</b></td><td>0.05 (+19.63%)</td><td>0.03 <b>(+23.62%)</b></td><td>0.01 (+1.64%)</td><td>482.00 (-19.11%)</td><td>291.22 <b>(-27.82%)</b></td><td>240.40 (-16.38%)</td><td>209.10 <b>(-23.10%)</b></td><td>109.99 <b>(-34.28%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>595.90 (n/a)</td><td>403.48 (n/a)</td><td>287.50 (n/a)</td><td>271.90 (n/a)</td><td>167.35 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 <b>(-30.46%)</b></td><td>0.02 <b>(-31.51%)</b></td><td>0.02 <b>(-31.59%)</b></td><td>0.01 <b>(-22.99%)</b></td><td>0.01 <b>(-38.33%)</b></td><td>563.90 <b>(+29.84%)</b></td><td>473.72 <b>(+42.79%)</b></td><td>513.10 <b>(+46.18%)</b></td><td>299.70 <b>(+43.81%)</b></td><td>107.24 (+12.51%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>434.30 (n/a)</td><td>331.76 (n/a)</td><td>351.00 (n/a)</td><td>208.40 (n/a)</td><td>95.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 <b>(+35.74%)</b></td><td>0.04 <b>(+41.50%)</b></td><td>0.04 <b>(+75.73%)</b></td><td>0.02 (-4.00%)</td><td>0.01 <b>(+84.30%)</b></td><td>544.40 (+4.17%)</td><td>335.04 <b>(-22.95%)</b></td><td>264.40 <b>(-43.10%)</b></td><td>200.20 <b>(-26.34%)</b></td><td>146.15 <b>(+51.41%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.60 (n/a)</td><td>434.82 (n/a)</td><td>464.70 (n/a)</td><td>271.80 (n/a)</td><td>96.53 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 <b>(-31.56%)</b></td><td>0.02 <b>(-28.10%)</b></td><td>0.01 (-17.34%)</td><td>0.00 <b>(-77.64%)</b></td><td>0.01 (-5.46%)</td><td>2486.00 <b>(+347.28%)</b></td><td>859.78 <b>(+114.16%)</b></td><td>576.30 <b>(+21.00%)</b></td><td>298.90 <b>(+46.09%)</b></td><td>921.10 <b>(+528.74%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.80 (n/a)</td><td>401.46 (n/a)</td><td>476.30 (n/a)</td><td>204.60 (n/a)</td><td>146.50 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (-14.81%)</td><td>0.03 (-15.70%)</td><td>0.02 <b>(-26.69%)</b></td><td>0.02 (-9.82%)</td><td>0.01 <b>(-27.67%)</b></td><td>626.30 (+10.89%)</td><td>435.18 (+13.63%)</td><td>423.60 <b>(+36.43%)</b></td><td>286.20 (+17.39%)</td><td>139.84 (-9.94%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>564.80 (n/a)</td><td>382.98 (n/a)</td><td>310.50 (n/a)</td><td>243.80 (n/a)</td><td>155.27 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (-13.88%)</td><td>0.02 (-6.50%)</td><td>0.02 (-9.71%)</td><td>0.01 (+3.57%)</td><td>0.01 (-18.25%)</td><td>591.70 (-3.46%)</td><td>420.14 (+3.91%)</td><td>454.50 (+10.75%)</td><td>240.20 (+16.09%)</td><td>143.77 (-7.53%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>612.90 (n/a)</td><td>404.34 (n/a)</td><td>410.40 (n/a)</td><td>206.90 (n/a)</td><td>155.48 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (-13.52%)</td><td>0.02 <b>(-22.56%)</b></td><td>0.02 <b>(-33.47%)</b></td><td>0.02 (-14.16%)</td><td>0.01 <b>(-21.70%)</b></td><td>533.00 (+16.50%)</td><td>444.08 <b>(+27.40%)</b></td><td>465.10 <b>(+50.32%)</b></td><td>292.30 (+15.62%)</td><td>93.02 (-2.23%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>457.50 (n/a)</td><td>348.56 (n/a)</td><td>309.40 (n/a)</td><td>252.80 (n/a)</td><td>95.14 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 (-13.08%)</td><td>0.02 (-10.13%)</td><td>0.02 <b>(-30.27%)</b></td><td>0.02 (+19.31%)</td><td>0.01 (-8.27%)</td><td>545.20 (-16.19%)</td><td>404.54 (+9.28%)</td><td>497.00 <b>(+43.43%)</b></td><td>211.40 (+15.08%)</td><td>161.16 (-10.04%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.50 (n/a)</td><td>370.18 (n/a)</td><td>346.50 (n/a)</td><td>183.70 (n/a)</td><td>179.16 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (-2.14%)</td><td>0.02 (+10.29%)</td><td>0.02 <b>(+24.37%)</b></td><td>0.01 (-3.25%)</td><td>0.01 (-12.93%)</td><td>616.00 (+3.36%)</td><td>462.78 (-11.11%)</td><td>463.50 (-19.60%)</td><td>282.70 (+2.21%)</td><td>124.40 (-9.07%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>596.00 (n/a)</td><td>520.64 (n/a)</td><td>576.50 (n/a)</td><td>276.60 (n/a)</td><td>136.81 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.03 (+8.67%)</td><td>0.02 <b>(+25.61%)</b></td><td>0.02 (+12.44%)</td><td>0.02 <b>(+294.69%)</b></td><td>0.01 <b>(-33.15%)</b></td><td>484.50 <b>(-74.66%)</b></td><td>365.64 <b>(-47.58%)</b></td><td>372.90 (-11.07%)</td><td>234.80 (-7.99%)</td><td>95.70 <b>(-86.10%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1912.20 (n/a)</td><td>697.56 (n/a)</td><td>419.30 (n/a)</td><td>255.20 (n/a)</td><td>688.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (+2.25%)</td><td>0.05 (+5.33%)</td><td>0.05 (-0.08%)</td><td>0.04 <b>(+29.91%)</b></td><td>0.01 <b>(-28.56%)</b></td><td>433.60 <b>(-23.03%)</b></td><td>327.46 (-9.73%)</td><td>304.40 (+0.10%)</td><td>251.90 (-2.21%)</td><td>69.86 <b>(-45.23%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>563.30 (n/a)</td><td>362.74 (n/a)</td><td>304.10 (n/a)</td><td>257.60 (n/a)</td><td>127.54 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (-17.67%)</td><td>0.05 (-13.06%)</td><td>0.04 (-18.95%)</td><td>0.04 (-4.32%)</td><td>0.02 <b>(-25.91%)</b></td><td>682.50 (+4.53%)</td><td>571.64 (+11.63%)</td><td>627.40 <b>(+23.38%)</b></td><td>331.20 <b>(+21.45%)</b></td><td>143.85 (-8.14%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>652.90 (n/a)</td><td>512.08 (n/a)</td><td>508.50 (n/a)</td><td>272.70 (n/a)</td><td>156.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (-19.69%)</td><td>0.06 (-1.60%)</td><td>0.06 (+18.33%)</td><td>0.03 <b>(-39.20%)</b></td><td>0.02 (-1.24%)</td><td>577.70 <b>(+64.45%)</b></td><td>321.04 (+7.57%)</td><td>281.60 (-15.49%)</td><td>231.60 <b>(+24.52%)</b></td><td>145.61 <b>(+109.87%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>351.30 (n/a)</td><td>298.46 (n/a)</td><td>333.20 (n/a)</td><td>186.00 (n/a)</td><td>69.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (-0.76%)</td><td>0.06 (-4.99%)</td><td>0.06 (-9.40%)</td><td>0.04 (+1.82%)</td><td>0.02 (-18.39%)</td><td>493.00 (-1.79%)</td><td>378.20 (+2.42%)</td><td>360.20 (+10.36%)</td><td>262.50 (+0.73%)</td><td>97.06 (-18.77%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>502.00 (n/a)</td><td>369.28 (n/a)</td><td>326.40 (n/a)</td><td>260.60 (n/a)</td><td>119.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 <b>(+22.28%)</b></td><td>0.06 <b>(+33.77%)</b></td><td>0.06 <b>(+73.27%)</b></td><td>0.03 (+8.73%)</td><td>0.02 <b>(+40.59%)</b></td><td>547.50 (-8.03%)</td><td>346.24 <b>(-20.39%)</b></td><td>268.20 <b>(-42.29%)</b></td><td>190.60 (-18.23%)</td><td>157.19 (+19.40%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>595.30 (n/a)</td><td>434.94 (n/a)</td><td>464.70 (n/a)</td><td>233.10 (n/a)</td><td>131.65 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (+10.07%)</td><td>0.05 (-1.43%)</td><td>0.04 (+14.78%)</td><td>0.04 (+6.96%)</td><td>0.03 (+4.09%)</td><td>540.10 (-6.51%)</td><td>436.00 (-0.78%)</td><td>461.30 (-12.86%)</td><td>207.50 (-9.15%)</td><td>134.07 (-19.23%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>577.70 (n/a)</td><td>439.44 (n/a)</td><td>529.40 (n/a)</td><td>228.40 (n/a)</td><td>166.01 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (+3.76%)</td><td>0.05 (+7.84%)</td><td>0.06 <b>(+41.62%)</b></td><td>0.03 (+1.54%)</td><td>0.02 (+0.01%)</td><td>583.00 (-1.52%)</td><td>394.20 (-7.23%)</td><td>297.30 <b>(-29.38%)</b></td><td>246.10 (-3.64%)</td><td>161.39 (-0.28%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>592.00 (n/a)</td><td>424.94 (n/a)</td><td>421.00 (n/a)</td><td>255.40 (n/a)</td><td>161.84 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 <b>(-28.08%)</b></td><td>0.04 (-7.23%)</td><td>0.04 (+1.99%)</td><td>0.03 (+6.76%)</td><td>0.01 <b>(-52.68%)</b></td><td>536.50 (-6.34%)</td><td>436.24 (+0.88%)</td><td>461.60 (-1.95%)</td><td>325.70 <b>(+39.07%)</b></td><td>82.53 <b>(-36.41%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>572.80 (n/a)</td><td>432.42 (n/a)</td><td>470.80 (n/a)</td><td>234.20 (n/a)</td><td>129.78 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.05 <b>(-29.40%)</b></td><td>0.04 (+0.21%)</td><td>0.04 <b>(+23.46%)</b></td><td>0.03 (+2.53%)</td><td>0.01 <b>(-45.79%)</b></td><td>566.70 (-2.48%)</td><td>419.24 (-5.26%)</td><td>376.90 (-19.00%)</td><td>334.40 <b>(+41.63%)</b></td><td>100.92 <b>(-20.56%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>581.10 (n/a)</td><td>442.52 (n/a)</td><td>465.30 (n/a)</td><td>236.10 (n/a)</td><td>127.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 (+1.52%)</td><td>0.05 (+15.66%)</td><td>0.04 (+3.54%)</td><td>0.03 (+16.18%)</td><td>0.01 (+4.57%)</td><td>538.60 (-13.92%)</td><td>416.60 (-13.80%)</td><td>451.30 (-3.42%)</td><td>289.20 (-1.50%)</td><td>112.33 (-10.62%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>625.70 (n/a)</td><td>483.30 (n/a)</td><td>467.30 (n/a)</td><td>293.60 (n/a)</td><td>125.68 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.04 <b>(-33.09%)</b></td><td>0.03 <b>(-26.45%)</b></td><td>0.03 <b>(-24.23%)</b></td><td>0.03 (-11.80%)</td><td>0.01 <b>(-50.22%)</b></td><td>604.30 (+13.40%)</td><td>506.52 <b>(+31.76%)</b></td><td>513.80 <b>(+31.98%)</b></td><td>380.60 <b>(+49.43%)</b></td><td>83.43 (-16.36%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>532.90 (n/a)</td><td>384.44 (n/a)</td><td>389.30 (n/a)</td><td>254.70 (n/a)</td><td>99.76 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (-17.28%)</td><td>0.08 <b>(-25.82%)</b></td><td>0.07 <b>(-33.60%)</b></td><td>0.02 <b>(-65.86%)</b></td><td>0.04 <b>(+21.91%)</b></td><td>1846.60 <b>(+192.88%)</b></td><td>674.58 <b>(+90.15%)</b></td><td>469.10 <b>(+50.59%)</b></td><td>276.40 <b>(+20.86%)</b></td><td>662.27 <b>(+318.23%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>630.50 (n/a)</td><td>354.76 (n/a)</td><td>311.50 (n/a)</td><td>228.70 (n/a)</td><td>158.35 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (+7.03%)</td><td>0.10 (+13.66%)</td><td>0.09 <b>(+24.13%)</b></td><td>0.06 (+4.10%)</td><td>0.03 (+7.22%)</td><td>517.40 (-3.94%)</td><td>357.02 (-12.20%)</td><td>380.00 (-19.44%)</td><td>236.20 (-6.57%)</td><td>117.15 (-7.78%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>538.60 (n/a)</td><td>406.64 (n/a)</td><td>471.70 (n/a)</td><td>252.80 (n/a)</td><td>127.03 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.16 <b>(-29.13%)</b></td><td>0.11 (-5.13%)</td><td>0.12 <b>(+55.33%)</b></td><td>0.07 (+3.24%)</td><td>0.04 <b>(-45.02%)</b></td><td>556.80 (-3.15%)</td><td>399.00 (-5.01%)</td><td>336.00 <b>(-35.61%)</b></td><td>259.00 <b>(+41.14%)</b></td><td>132.53 <b>(-22.74%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>574.90 (n/a)</td><td>420.06 (n/a)</td><td>521.80 (n/a)</td><td>183.50 (n/a)</td><td>171.54 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (-8.51%)</td><td>0.08 <b>(-20.75%)</b></td><td>0.07 <b>(-36.68%)</b></td><td>0.01 <b>(-71.91%)</b></td><td>0.04 (+19.47%)</td><td>2198.00 <b>(+256.07%)</b></td><td>746.90 <b>(+93.01%)</b></td><td>472.50 <b>(+57.92%)</b></td><td>277.30 (+9.35%)</td><td>817.89 <b>(+393.91%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>617.30 (n/a)</td><td>386.98 (n/a)</td><td>299.20 (n/a)</td><td>253.60 (n/a)</td><td>165.59 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 <b>(+49.04%)</b></td><td>0.11 <b>(+47.35%)</b></td><td>0.11 <b>(+51.50%)</b></td><td>0.07 (+19.24%)</td><td>0.03 <b>(+109.62%)</b></td><td>607.00 (-16.14%)</td><td>419.98 <b>(-28.91%)</b></td><td>386.40 <b>(-33.98%)</b></td><td>292.40 <b>(-32.92%)</b></td><td>137.16 (+12.69%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>723.80 (n/a)</td><td>590.78 (n/a)</td><td>585.30 (n/a)</td><td>435.90 (n/a)</td><td>121.71 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.11 (-16.95%)</td><td>0.07 <b>(-28.74%)</b></td><td>0.07 <b>(-25.55%)</b></td><td>0.03 <b>(-47.88%)</b></td><td>0.03 (+5.44%)</td><td>1041.10 <b>(+91.87%)</b></td><td>554.04 <b>(+55.21%)</b></td><td>442.50 <b>(+34.34%)</b></td><td>295.70 <b>(+20.40%)</b></td><td>288.97 <b>(+151.68%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>542.60 (n/a)</td><td>356.96 (n/a)</td><td>329.40 (n/a)</td><td>245.60 (n/a)</td><td>114.81 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.16 <b>(+20.06%)</b></td><td>0.08 (-18.44%)</td><td>0.07 <b>(-43.40%)</b></td><td>0.02 <b>(-75.40%)</b></td><td>0.06 <b>(+79.33%)</b></td><td>2448.00 <b>(+306.44%)</b></td><td>824.92 <b>(+113.16%)</b></td><td>529.00 <b>(+76.69%)</b></td><td>233.50 (-16.70%)</td><td>920.51 <b>(+560.69%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>602.30 (n/a)</td><td>387.00 (n/a)</td><td>299.40 (n/a)</td><td>280.30 (n/a)</td><td>139.32 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (+13.87%)</td><td>0.09 (-9.84%)</td><td>0.07 <b>(-36.96%)</b></td><td>0.05 (-9.03%)</td><td>0.03 (+7.01%)</td><td>624.00 (+9.92%)</td><td>418.10 (+11.61%)</td><td>444.00 <b>(+58.63%)</b></td><td>230.90 (-12.21%)</td><td>150.00 (+3.44%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>567.70 (n/a)</td><td>374.60 (n/a)</td><td>279.90 (n/a)</td><td>263.00 (n/a)</td><td>145.01 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.15 <b>(+55.92%)</b></td><td>0.09 (+15.05%)</td><td>0.08 (+5.27%)</td><td>0.07 (-7.55%)</td><td>0.04 <b>(+255.66%)</b></td><td>552.10 (+8.15%)</td><td>429.06 (-5.90%)</td><td>445.20 (-5.01%)</td><td>239.60 <b>(-35.87%)</b></td><td>125.92 <b>(+150.52%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>510.50 (n/a)</td><td>455.94 (n/a)</td><td>468.70 (n/a)</td><td>373.60 (n/a)</td><td>50.26 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 <b>(-24.90%)</b></td><td>0.06 <b>(-39.77%)</b></td><td>0.06 <b>(-45.28%)</b></td><td>0.02 <b>(-70.89%)</b></td><td>0.03 (-15.16%)</td><td>2039.70 <b>(+243.50%)</b></td><td>790.04 <b>(+115.32%)</b></td><td>516.40 <b>(+82.73%)</b></td><td>320.90 <b>(+33.15%)</b></td><td>706.16 <b>(+352.16%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>593.80 (n/a)</td><td>366.92 (n/a)</td><td>282.60 (n/a)</td><td>241.00 (n/a)</td><td>156.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 <b>(+40.06%)</b></td><td>0.07 (-3.46%)</td><td>0.06 <b>(-20.73%)</b></td><td>0.04 (-19.50%)</td><td>0.04 <b>(+102.87%)</b></td><td>556.60 <b>(+24.21%)</b></td><td>366.90 (+19.08%)</td><td>337.40 <b>(+26.13%)</b></td><td>167.10 <b>(-28.62%)</b></td><td>167.76 <b>(+88.63%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>448.10 (n/a)</td><td>308.10 (n/a)</td><td>267.50 (n/a)</td><td>234.10 (n/a)</td><td>88.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (-4.96%)</td><td>0.05 (-9.88%)</td><td>0.05 (-18.20%)</td><td>0.04 (+12.98%)</td><td>0.02 <b>(-22.09%)</b></td><td>478.80 (-11.50%)</td><td>406.96 (+6.62%)</td><td>451.00 <b>(+22.26%)</b></td><td>256.00 (+5.22%)</td><td>93.69 <b>(-27.45%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>541.00 (n/a)</td><td>381.70 (n/a)</td><td>368.90 (n/a)</td><td>243.30 (n/a)</td><td>129.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 (+12.69%)</td><td>0.05 (-14.39%)</td><td>0.04 <b>(-27.02%)</b></td><td>0.01 <b>(-66.20%)</b></td><td>0.03 <b>(+63.35%)</b></td><td>1940.90 <b>(+195.82%)</b></td><td>693.04 <b>(+77.33%)</b></td><td>470.40 <b>(+37.02%)</b></td><td>221.90 (-11.24%)</td><td>705.83 <b>(+353.85%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>656.10 (n/a)</td><td>390.82 (n/a)</td><td>343.30 (n/a)</td><td>250.00 (n/a)</td><td>155.52 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (-11.92%)</td><td>0.05 (-13.50%)</td><td>0.04 <b>(-23.85%)</b></td><td>0.04 (+0.95%)</td><td>0.02 <b>(-21.91%)</b></td><td>566.90 (-0.94%)</td><td>438.50 (+11.67%)</td><td>475.70 <b>(+31.34%)</b></td><td>265.20 (+13.53%)</td><td>118.49 (-15.75%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>572.30 (n/a)</td><td>392.68 (n/a)</td><td>362.20 (n/a)</td><td>233.60 (n/a)</td><td>140.65 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (+4.57%)</td><td>0.06 <b>(+24.12%)</b></td><td>0.07 <b>(+45.47%)</b></td><td>0.04 (+13.33%)</td><td>0.02 <b>(+21.00%)</b></td><td>508.00 (-11.76%)</td><td>352.14 (-17.83%)</td><td>298.80 <b>(-31.25%)</b></td><td>248.50 (-4.39%)</td><td>121.68 (+4.23%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>575.70 (n/a)</td><td>428.54 (n/a)</td><td>434.60 (n/a)</td><td>259.90 (n/a)</td><td>116.74 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (+18.73%)</td><td>0.06 <b>(+38.65%)</b></td><td>0.08 <b>(+103.31%)</b></td><td>0.03 <b>(+75.70%)</b></td><td>0.03 (+15.68%)</td><td>619.90 <b>(-43.09%)</b></td><td>376.36 <b>(-32.43%)</b></td><td>255.40 <b>(-50.82%)</b></td><td>242.30 (-15.78%)</td><td>178.44 <b>(-44.78%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1089.20 (n/a)</td><td>557.00 (n/a)</td><td>519.30 (n/a)</td><td>287.70 (n/a)</td><td>323.13 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 <b>(-29.89%)</b></td><td>0.07 <b>(-26.90%)</b></td><td>0.08 <b>(-20.88%)</b></td><td>0.04 (+0.61%)</td><td>0.02 <b>(-37.67%)</b></td><td>566.50 (-0.61%)</td><td>386.18 <b>(+28.21%)</b></td><td>312.70 <b>(+26.39%)</b></td><td>284.10 <b>(+42.62%)</b></td><td>126.12 (-17.66%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>570.00 (n/a)</td><td>301.22 (n/a)</td><td>247.40 (n/a)</td><td>199.20 (n/a)</td><td>153.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (+1.18%)</td><td>0.07 (+5.23%)</td><td>0.07 <b>(+30.59%)</b></td><td>0.04 (+10.79%)</td><td>0.03 (+3.99%)</td><td>596.40 (-9.73%)</td><td>402.56 (-4.39%)</td><td>343.70 <b>(-23.44%)</b></td><td>245.40 (-1.17%)</td><td>162.22 (-0.96%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>660.70 (n/a)</td><td>421.06 (n/a)</td><td>448.90 (n/a)</td><td>248.30 (n/a)</td><td>163.80 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 <b>(-37.84%)</b></td><td>0.08 (+5.34%)</td><td>0.08 (+19.64%)</td><td>0.05 <b>(+337.52%)</b></td><td>0.02 <b>(-61.39%)</b></td><td>479.40 <b>(-77.14%)</b></td><td>346.94 <b>(-49.85%)</b></td><td>318.80 (-16.44%)</td><td>251.20 <b>(+60.82%)</b></td><td>100.48 <b>(-87.37%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2097.40 (n/a)</td><td>691.80 (n/a)</td><td>381.50 (n/a)</td><td>156.20 (n/a)</td><td>795.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (+7.01%)</td><td>0.07 (+15.96%)</td><td>0.09 <b>(+71.11%)</b></td><td>0.04 <b>(+28.48%)</b></td><td>0.03 (+10.42%)</td><td>554.30 <b>(-22.16%)</b></td><td>378.76 (-13.56%)</td><td>267.40 <b>(-41.55%)</b></td><td>252.90 (-6.54%)</td><td>159.71 (-11.39%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>712.10 (n/a)</td><td>438.18 (n/a)</td><td>457.50 (n/a)</td><td>270.60 (n/a)</td><td>180.24 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (-13.87%)</td><td>0.06 (-17.27%)</td><td>0.06 (-19.40%)</td><td>0.04 (+6.65%)</td><td>0.02 <b>(-30.53%)</b></td><td>561.70 (-6.23%)</td><td>416.28 (+13.82%)</td><td>401.50 <b>(+24.07%)</b></td><td>256.40 (+16.12%)</td><td>116.18 <b>(-24.87%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>599.00 (n/a)</td><td>365.74 (n/a)</td><td>323.60 (n/a)</td><td>220.80 (n/a)</td><td>154.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 <b>(+49.20%)</b></td><td>0.08 <b>(+38.71%)</b></td><td>0.09 <b>(+56.70%)</b></td><td>0.04 (-18.18%)</td><td>0.02 <b>(+248.51%)</b></td><td>592.60 <b>(+22.24%)</b></td><td>346.88 <b>(-21.37%)</b></td><td>287.20 <b>(-36.19%)</b></td><td>244.60 <b>(-32.97%)</b></td><td>141.00 <b>(+209.98%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>484.80 (n/a)</td><td>441.14 (n/a)</td><td>450.10 (n/a)</td><td>364.90 (n/a)</td><td>45.49 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (+2.77%)</td><td>0.06 (+2.59%)</td><td>0.06 (-13.13%)</td><td>0.04 (+7.21%)</td><td>0.02 (-11.78%)</td><td>469.40 (-6.74%)</td><td>333.94 (-5.54%)</td><td>304.00 (+15.11%)</td><td>245.60 (-2.69%)</td><td>99.34 <b>(-23.04%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>503.30 (n/a)</td><td>353.54 (n/a)</td><td>264.10 (n/a)</td><td>252.40 (n/a)</td><td>129.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.07 (-15.94%)</td><td>0.05 (-4.33%)</td><td>0.07 <b>(+47.45%)</b></td><td>0.02 <b>(-22.95%)</b></td><td>0.02 (-0.01%)</td><td>816.20 <b>(+29.78%)</b></td><td>434.02 (+12.60%)</td><td>267.40 <b>(-32.17%)</b></td><td>255.80 (+18.92%)</td><td>253.04 <b>(+50.46%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>628.90 (n/a)</td><td>385.44 (n/a)</td><td>394.20 (n/a)</td><td>215.10 (n/a)</td><td>168.18 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (-16.77%)</td><td>0.07 <b>(+37.63%)</b></td><td>0.07 <b>(+64.02%)</b></td><td>0.07 <b>(+102.03%)</b></td><td>0.00 <b>(-81.22%)</b></td><td>277.10 <b>(-50.50%)</b></td><td>261.52 <b>(-35.68%)</b></td><td>263.80 <b>(-39.02%)</b></td><td>242.80 <b>(+20.14%)</b></td><td>16.08 <b>(-88.24%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>559.80 (n/a)</td><td>406.60 (n/a)</td><td>432.60 (n/a)</td><td>202.10 (n/a)</td><td>136.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 <b>(+75.53%)</b></td><td>0.05 <b>(+65.67%)</b></td><td>0.04 <b>(+49.42%)</b></td><td>0.03 <b>(+88.93%)</b></td><td>0.02 <b>(+73.15%)</b></td><td>562.90 <b>(-47.07%)</b></td><td>393.72 <b>(-39.98%)</b></td><td>421.90 <b>(-33.06%)</b></td><td>220.10 <b>(-43.04%)</b></td><td>153.11 <b>(-45.72%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>1063.50 (n/a)</td><td>655.96 (n/a)</td><td>630.30 (n/a)</td><td>386.40 (n/a)</td><td>282.06 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.08 (-11.09%)</td><td>0.04 <b>(-38.32%)</b></td><td>0.04 <b>(-41.39%)</b></td><td>0.01 <b>(-76.48%)</b></td><td>0.02 <b>(+33.67%)</b></td><td>1985.70 <b>(+325.20%)</b></td><td>703.54 <b>(+146.53%)</b></td><td>429.90 <b>(+70.60%)</b></td><td>238.80 (+12.48%)</td><td>721.77 <b>(+599.41%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>467.00 (n/a)</td><td>285.38 (n/a)</td><td>252.00 (n/a)</td><td>212.30 (n/a)</td><td>103.20 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 <b>(+45.71%)</b></td><td>0.05 <b>(+41.93%)</b></td><td>0.05 <b>(+48.93%)</b></td><td>0.04 <b>(+32.14%)</b></td><td>0.01 <b>(+66.59%)</b></td><td>483.60 <b>(-24.33%)</b></td><td>387.94 <b>(-28.95%)</b></td><td>381.90 <b>(-32.85%)</b></td><td>304.40 <b>(-31.36%)</b></td><td>71.80 (-12.86%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>639.10 (n/a)</td><td>546.00 (n/a)</td><td>568.70 (n/a)</td><td>443.50 (n/a)</td><td>82.40 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.40 (+6.27%)</td><td>0.28 (-2.85%)</td><td>0.31 (-10.51%)</td><td>0.14 <b>(-21.48%)</b></td><td>0.10 (+5.71%)</td><td>706.20 <b>(+27.36%)</b></td><td>399.02 (+6.37%)</td><td>315.60 (+11.76%)</td><td>244.80 (-5.92%)</td><td>187.98 <b>(+29.60%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.35 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>554.50 (n/a)</td><td>375.14 (n/a)</td><td>282.40 (n/a)</td><td>260.20 (n/a)</td><td>145.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.27 <b>(-23.36%)</b></td><td>0.21 (+2.30%)</td><td>0.21 (-1.40%)</td><td>0.12 <b>(+133.40%)</b></td><td>0.06 <b>(-52.21%)</b></td><td>804.40 <b>(-57.15%)</b></td><td>509.40 <b>(-36.29%)</b></td><td>474.10 (+1.41%)</td><td>359.70 <b>(+30.52%)</b></td><td>183.08 <b>(-73.16%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.36 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>0.13 (n/a)</td><td>1877.40 (n/a)</td><td>799.54 (n/a)</td><td>467.50 (n/a)</td><td>275.60 (n/a)</td><td>682.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.42 <b>(+49.39%)</b></td><td>0.33 <b>(+51.15%)</b></td><td>0.33 <b>(+52.02%)</b></td><td>0.20 (+9.33%)</td><td>0.08 <b>(+102.25%)</b></td><td>497.90 (-8.52%)</td><td>318.42 <b>(-31.12%)</b></td><td>297.50 <b>(-34.21%)</b></td><td>233.90 <b>(-33.06%)</b></td><td>104.42 <b>(+26.35%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>544.30 (n/a)</td><td>462.26 (n/a)</td><td>452.20 (n/a)</td><td>349.40 (n/a)</td><td>82.64 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.28 (+18.12%)</td><td>0.22 <b>(+28.67%)</b></td><td>0.21 (+3.71%)</td><td>0.17 <b>(+324.27%)</b></td><td>0.05 <b>(-38.58%)</b></td><td>442.60 <b>(-76.43%)</b></td><td>342.30 <b>(-48.73%)</b></td><td>353.90 (-3.57%)</td><td>259.00 (-15.33%)</td><td>76.98 <b>(-88.68%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>0.08 (n/a)</td><td>1877.60 (n/a)</td><td>667.62 (n/a)</td><td>367.00 (n/a)</td><td>305.90 (n/a)</td><td>679.79 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.28 (+0.20%)</td><td>0.21 (+16.42%)</td><td>0.24 <b>(+49.44%)</b></td><td>0.13 (-7.90%)</td><td>0.06 (+16.47%)</td><td>565.80 (+8.58%)</td><td>383.24 (-11.50%)</td><td>304.80 <b>(-33.08%)</b></td><td>267.30 (-0.19%)</td><td>130.36 <b>(+35.19%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>521.10 (n/a)</td><td>433.02 (n/a)</td><td>455.50 (n/a)</td><td>267.80 (n/a)</td><td>96.43 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.27 (-0.32%)</td><td>0.22 (+18.31%)</td><td>0.21 <b>(+23.25%)</b></td><td>0.17 <b>(+42.47%)</b></td><td>0.04 <b>(-29.58%)</b></td><td>422.60 <b>(-29.81%)</b></td><td>347.44 (-19.23%)</td><td>349.20 (-18.87%)</td><td>268.40 (+0.34%)</td><td>62.97 <b>(-49.41%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>602.10 (n/a)</td><td>430.18 (n/a)</td><td>430.40 (n/a)</td><td>267.50 (n/a)</td><td>124.47 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.15 (+3.21%)</td><td>0.12 (+0.71%)</td><td>0.13 (+4.74%)</td><td>0.06 (-2.04%)</td><td>0.03 (+4.16%)</td><td>574.00 (+2.08%)</td><td>331.84 (+0.08%)</td><td>275.60 (-4.54%)</td><td>241.80 (-3.09%)</td><td>137.75 (+4.99%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>562.30 (n/a)</td><td>331.56 (n/a)</td><td>288.70 (n/a)</td><td>249.50 (n/a)</td><td>131.21 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (-16.96%)</td><td>0.09 <b>(-23.93%)</b></td><td>0.08 <b>(-37.28%)</b></td><td>0.07 <b>(-22.00%)</b></td><td>0.03 (+7.99%)</td><td>545.80 <b>(+28.21%)</b></td><td>431.98 <b>(+35.77%)</b></td><td>484.00 <b>(+59.47%)</b></td><td>294.00 <b>(+20.39%)</b></td><td>123.46 <b>(+65.38%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>425.70 (n/a)</td><td>318.16 (n/a)</td><td>303.50 (n/a)</td><td>244.20 (n/a)</td><td>74.65 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 <b>(-26.06%)</b></td><td>0.09 (-19.86%)</td><td>0.08 <b>(-21.52%)</b></td><td>0.07 (-17.88%)</td><td>0.03 <b>(-34.63%)</b></td><td>557.20 <b>(+21.77%)</b></td><td>431.04 <b>(+21.65%)</b></td><td>471.80 <b>(+27.41%)</b></td><td>274.80 <b>(+35.24%)</b></td><td>108.59 (+5.68%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>457.60 (n/a)</td><td>354.34 (n/a)</td><td>370.30 (n/a)</td><td>203.20 (n/a)</td><td>102.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (-7.50%)</td><td>0.10 (-13.98%)</td><td>0.09 <b>(-28.86%)</b></td><td>0.06 (-12.63%)</td><td>0.04 (+0.48%)</td><td>650.90 (+14.45%)</td><td>412.32 (+18.24%)</td><td>429.90 <b>(+40.58%)</b></td><td>259.90 (+8.11%)</td><td>159.57 (+18.27%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>568.70 (n/a)</td><td>348.70 (n/a)</td><td>305.80 (n/a)</td><td>240.40 (n/a)</td><td>134.92 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 (-15.23%)</td><td>0.11 (+3.11%)</td><td>0.11 (-6.26%)</td><td>0.08 <b>(+27.33%)</b></td><td>0.02 <b>(-53.15%)</b></td><td>448.10 <b>(-21.47%)</b></td><td>344.50 (-11.25%)</td><td>324.00 (+6.65%)</td><td>297.80 (+17.94%)</td><td>62.27 <b>(-58.26%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>570.60 (n/a)</td><td>388.16 (n/a)</td><td>303.80 (n/a)</td><td>252.50 (n/a)</td><td>149.17 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (-14.89%)</td><td>0.10 (-12.49%)</td><td>0.11 (-14.77%)</td><td>0.07 (+0.66%)</td><td>0.03 <b>(-31.21%)</b></td><td>541.90 (-0.66%)</td><td>392.84 (+7.89%)</td><td>343.30 (+17.33%)</td><td>267.90 (+17.50%)</td><td>123.56 (-18.99%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>545.50 (n/a)</td><td>364.10 (n/a)</td><td>292.60 (n/a)</td><td>228.00 (n/a)</td><td>152.53 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (-11.53%)</td><td>0.13 (-7.02%)</td><td>0.14 (-3.32%)</td><td>0.10 <b>(+20.76%)</b></td><td>0.02 <b>(-31.80%)</b></td><td>420.10 (-17.19%)</td><td>333.72 (+3.67%)</td><td>300.10 (+3.45%)</td><td>282.60 (+13.04%)</td><td>62.50 <b>(-40.47%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>507.30 (n/a)</td><td>321.92 (n/a)</td><td>290.10 (n/a)</td><td>250.00 (n/a)</td><td>104.99 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.16 (+6.22%)</td><td>0.12 (+11.13%)</td><td>0.15 <b>(+87.77%)</b></td><td>0.02 <b>(-71.63%)</b></td><td>0.06 <b>(+68.95%)</b></td><td>1894.70 <b>(+252.44%)</b></td><td>629.84 <b>(+47.01%)</b></td><td>264.70 <b>(-46.75%)</b></td><td>253.80 (-5.86%)</td><td>713.06 <b>(+445.11%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>537.60 (n/a)</td><td>428.42 (n/a)</td><td>497.10 (n/a)</td><td>269.60 (n/a)</td><td>130.81 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.16 (+11.74%)</td><td>0.10 (+17.59%)</td><td>0.09 <b>(+21.21%)</b></td><td>0.08 (+5.94%)</td><td>0.03 (+7.44%)</td><td>522.30 (-5.60%)</td><td>416.04 (-15.25%)</td><td>440.10 (-17.49%)</td><td>260.80 (-10.50%)</td><td>100.06 (-10.86%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>553.30 (n/a)</td><td>490.92 (n/a)</td><td>533.40 (n/a)</td><td>291.40 (n/a)</td><td>112.25 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 <b>(-51.54%)</b></td><td>0.08 <b>(-33.13%)</b></td><td>0.08 <b>(-25.50%)</b></td><td>0.06 <b>(-23.88%)</b></td><td>0.01 <b>(-69.55%)</b></td><td>660.90 <b>(+31.37%)</b></td><td>506.80 <b>(+38.27%)</b></td><td>505.10 <b>(+34.23%)</b></td><td>417.80 <b>(+106.32%)</b></td><td>98.78 (-18.63%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>503.10 (n/a)</td><td>366.52 (n/a)</td><td>376.30 (n/a)</td><td>202.50 (n/a)</td><td>121.39 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (-15.73%)</td><td>0.11 (-5.98%)</td><td>0.11 (-16.86%)</td><td>0.09 <b>(+28.46%)</b></td><td>0.02 <b>(-46.63%)</b></td><td>476.90 <b>(-22.15%)</b></td><td>381.02 (-3.97%)</td><td>378.30 <b>(+20.29%)</b></td><td>294.90 (+18.67%)</td><td>82.97 <b>(-51.50%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>612.60 (n/a)</td><td>396.78 (n/a)</td><td>314.50 (n/a)</td><td>248.50 (n/a)</td><td>171.07 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.19 <b>(+41.94%)</b></td><td>0.11 (+10.34%)</td><td>0.08 <b>(-30.57%)</b></td><td>0.06 <b>(+51.60%)</b></td><td>0.05 <b>(+41.37%)</b></td><td>691.30 <b>(-34.04%)</b></td><td>454.66 (-11.18%)</td><td>498.60 <b>(+44.02%)</b></td><td>217.20 <b>(-29.57%)</b></td><td>194.91 <b>(-37.11%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>1048.00 (n/a)</td><td>511.88 (n/a)</td><td>346.20 (n/a)</td><td>308.40 (n/a)</td><td>309.93 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (-4.36%)</td><td>0.09 (-4.63%)</td><td>0.08 (-13.60%)</td><td>0.06 (-6.61%)</td><td>0.03 (-3.23%)</td><td>587.80 (+7.09%)</td><td>416.76 (+4.75%)</td><td>444.40 (+15.73%)</td><td>269.70 (+4.58%)</td><td>138.37 (+2.27%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>548.90 (n/a)</td><td>397.86 (n/a)</td><td>384.00 (n/a)</td><td>257.90 (n/a)</td><td>135.30 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 <b>(-30.55%)</b></td><td>0.07 <b>(-43.32%)</b></td><td>0.07 <b>(-44.88%)</b></td><td>0.03 <b>(-61.38%)</b></td><td>0.04 (+2.34%)</td><td>1077.80 <b>(+158.90%)</b></td><td>641.26 <b>(+122.23%)</b></td><td>504.60 <b>(+81.38%)</b></td><td>260.80 <b>(+43.93%)</b></td><td>386.92 <b>(+313.50%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>416.30 (n/a)</td><td>288.56 (n/a)</td><td>278.20 (n/a)</td><td>181.20 (n/a)</td><td>93.57 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.09 (-19.84%)</td><td>0.08 (-5.63%)</td><td>0.08 (-4.75%)</td><td>0.07 (+13.38%)</td><td>0.01 <b>(-72.11%)</b></td><td>472.40 (-11.82%)</td><td>445.18 (+2.12%)</td><td>447.30 (+5.00%)</td><td>398.60 <b>(+24.76%)</b></td><td>28.08 <b>(-70.70%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>535.70 (n/a)</td><td>435.92 (n/a)</td><td>426.00 (n/a)</td><td>319.50 (n/a)</td><td>95.82 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.12 <b>(-28.47%)</b></td><td>0.08 (-16.43%)</td><td>0.08 (-2.88%)</td><td>0.06 (+8.78%)</td><td>0.02 <b>(-49.95%)</b></td><td>612.20 (-8.08%)</td><td>438.14 (+7.47%)</td><td>440.90 (+2.97%)</td><td>290.90 <b>(+39.79%)</b></td><td>117.81 <b>(-34.40%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>666.00 (n/a)</td><td>407.68 (n/a)</td><td>428.20 (n/a)</td><td>208.10 (n/a)</td><td>179.58 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (+11.67%)</td><td>0.10 <b>(+26.35%)</b></td><td>0.10 <b>(+53.20%)</b></td><td>0.05 <b>(+191.24%)</b></td><td>0.03 <b>(-20.13%)</b></td><td>654.20 <b>(-65.66%)</b></td><td>403.14 <b>(-43.70%)</b></td><td>334.70 <b>(-34.73%)</b></td><td>249.90 (-10.46%)</td><td>163.77 <b>(-75.80%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1905.20 (n/a)</td><td>716.00 (n/a)</td><td>512.80 (n/a)</td><td>279.10 (n/a)</td><td>676.83 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.14 (+1.22%)</td><td>0.10 (+10.81%)</td><td>0.12 <b>(+58.64%)</b></td><td>0.06 (+4.84%)</td><td>0.04 (+4.60%)</td><td>614.50 (-4.61%)</td><td>396.42 (-8.47%)</td><td>297.90 <b>(-36.95%)</b></td><td>241.00 (-1.19%)</td><td>169.64 (+5.32%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>644.20 (n/a)</td><td>433.12 (n/a)</td><td>472.50 (n/a)</td><td>243.90 (n/a)</td><td>161.08 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.40 (-14.00%)</td><td>0.31 (-4.44%)</td><td>0.25 (-1.14%)</td><td>0.22 (+5.66%)</td><td>0.09 <b>(-25.49%)</b></td><td>587.20 (-5.35%)</td><td>454.40 (+0.68%)</td><td>514.40 (+1.14%)</td><td>326.60 (+16.27%)</td><td>119.86 (-19.71%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.47 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>620.40 (n/a)</td><td>451.32 (n/a)</td><td>508.60 (n/a)</td><td>280.90 (n/a)</td><td>149.28 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.43 (-8.18%)</td><td>0.27 <b>(-27.49%)</b></td><td>0.21 <b>(-51.87%)</b></td><td>0.21 (-11.93%)</td><td>0.10 (-13.80%)</td><td>627.20 (+13.56%)</td><td>529.00 <b>(+37.20%)</b></td><td>624.90 <b>(+107.75%)</b></td><td>304.10 (+8.92%)</td><td>144.43 (+10.05%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.47 (n/a)</td><td>0.37 (n/a)</td><td>0.44 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>552.30 (n/a)</td><td>385.58 (n/a)</td><td>300.80 (n/a)</td><td>279.20 (n/a)</td><td>131.25 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.55 <b>(+32.68%)</b></td><td>0.30 (-2.31%)</td><td>0.25 (-15.76%)</td><td>0.24 (-7.73%)</td><td>0.14 <b>(+123.15%)</b></td><td>555.20 (+8.40%)</td><td>480.70 (+11.17%)</td><td>534.80 (+18.71%)</td><td>236.70 <b>(-24.62%)</b></td><td>136.84 <b>(+84.60%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>512.20 (n/a)</td><td>432.40 (n/a)</td><td>450.50 (n/a)</td><td>314.00 (n/a)</td><td>74.12 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-12.98%)</td><td>0.01 (+5.19%)</td><td>0.01 (+13.69%)</td><td>0.01 (+14.68%)</td><td>0.00 <b>(-40.73%)</b></td><td>450.60 (-12.81%)</td><td>320.08 (-10.99%)</td><td>289.80 (-12.02%)</td><td>263.70 (+14.90%)</td><td>76.96 <b>(-40.36%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>516.80 (n/a)</td><td>359.60 (n/a)</td><td>329.40 (n/a)</td><td>229.50 (n/a)</td><td>129.04 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (+2.05%)</td><td>0.01 (-0.74%)</td><td>0.01 (-4.77%)</td><td>0.01 (-8.66%)</td><td>0.00 (+3.02%)</td><td>506.30 (+9.49%)</td><td>346.76 (+1.47%)</td><td>298.70 (+5.03%)</td><td>266.90 (-1.98%)</td><td>101.01 (+11.94%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>462.40 (n/a)</td><td>341.74 (n/a)</td><td>284.40 (n/a)</td><td>272.30 (n/a)</td><td>90.24 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-3.67%)</td><td>0.01 (+12.54%)</td><td>0.01 <b>(+54.78%)</b></td><td>0.01 (-10.80%)</td><td>0.00 (+18.97%)</td><td>533.00 (+12.12%)</td><td>366.74 (-8.30%)</td><td>282.90 <b>(-35.40%)</b></td><td>268.30 (+3.79%)</td><td>124.57 <b>(+35.43%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>475.40 (n/a)</td><td>399.94 (n/a)</td><td>437.90 (n/a)</td><td>258.50 (n/a)</td><td>91.98 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>10.34 <b>(+38.17%)</b></td><td>8.02 <b>(+30.42%)</b></td><td>7.88 <b>(+22.44%)</b></td><td>5.92 (+17.72%)</td><td>1.68 <b>(+60.84%)</b></td><td>354.30 (-15.06%)</td><td>271.24 <b>(-22.38%)</b></td><td>266.40 (-18.33%)</td><td>203.00 <b>(-27.63%)</b></td><td>57.83 (-4.10%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>7.48 (n/a)</td><td>6.15 (n/a)</td><td>6.43 (n/a)</td><td>5.03 (n/a)</td><td>1.05 (n/a)</td><td>417.10 (n/a)</td><td>349.46 (n/a)</td><td>326.20 (n/a)</td><td>280.50 (n/a)</td><td>60.30 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.58 (+12.78%)</td><td>0.49 (+12.95%)</td><td>0.48 (+11.55%)</td><td>0.41 <b>(+38.44%)</b></td><td>0.08 (-14.58%)</td><td>323.40 <b>(-27.75%)</b></td><td>275.64 (-13.29%)</td><td>277.00 (-10.36%)</td><td>228.60 (-11.33%)</td><td>41.97 <b>(-45.60%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.51 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.30 (n/a)</td><td>0.09 (n/a)</td><td>447.60 (n/a)</td><td>317.90 (n/a)</td><td>309.00 (n/a)</td><td>257.80 (n/a)</td><td>77.15 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.59 <b>(-20.75%)</b></td><td>0.49 (-6.21%)</td><td>0.47 (-10.24%)</td><td>0.44 <b>(+80.87%)</b></td><td>0.06 <b>(-67.19%)</b></td><td>303.30 <b>(-44.71%)</b></td><td>272.06 (-6.78%)</td><td>278.80 (+11.39%)</td><td>224.00 <b>(+26.20%)</b></td><td>30.76 <b>(-79.13%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.74 (n/a)</td><td>0.52 (n/a)</td><td>0.53 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>548.60 (n/a)</td><td>291.84 (n/a)</td><td>250.30 (n/a)</td><td>177.50 (n/a)</td><td>147.42 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.53 (+9.30%)</td><td>0.40 (+16.99%)</td><td>0.41 <b>(+36.73%)</b></td><td>0.24 (+2.36%)</td><td>0.13 (+12.62%)</td><td>555.80 (-2.32%)</td><td>360.76 (-13.80%)</td><td>319.10 <b>(-26.86%)</b></td><td>249.90 (-8.53%)</td><td>130.96 (-1.05%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.48 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>569.00 (n/a)</td><td>418.50 (n/a)</td><td>436.30 (n/a)</td><td>273.20 (n/a)</td><td>132.35 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.46 <b>(-23.08%)</b></td><td>0.33 <b>(-21.81%)</b></td><td>0.29 <b>(-29.77%)</b></td><td>0.25 (-2.23%)</td><td>0.09 <b>(-47.58%)</b></td><td>524.90 (+2.28%)</td><td>417.72 (+17.55%)</td><td>452.70 <b>(+42.40%)</b></td><td>284.50 <b>(+30.03%)</b></td><td>98.89 <b>(-31.62%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.60 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>513.20 (n/a)</td><td>355.36 (n/a)</td><td>317.90 (n/a)</td><td>218.80 (n/a)</td><td>144.62 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.59 (+18.10%)</td><td>0.44 <b>(+27.92%)</b></td><td>0.46 <b>(+68.00%)</b></td><td>0.30 <b>(+36.00%)</b></td><td>0.11 (-17.11%)</td><td>445.10 <b>(-26.48%)</b></td><td>314.70 <b>(-26.43%)</b></td><td>288.40 <b>(-40.47%)</b></td><td>224.60 (-15.31%)</td><td>85.72 <b>(-43.74%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.50 (n/a)</td><td>0.35 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.13 (n/a)</td><td>605.40 (n/a)</td><td>427.78 (n/a)</td><td>484.50 (n/a)</td><td>265.20 (n/a)</td><td>152.37 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.01 (-3.39%)</td><td>0.01 (+4.86%)</td><td>0.01 (+1.52%)</td><td>0.01 <b>(+29.78%)</b></td><td>0.00 (-18.64%)</td><td>518.90 <b>(-22.94%)</b></td><td>419.02 (-8.81%)</td><td>443.00 (-1.49%)</td><td>277.60 (+3.50%)</td><td>107.10 <b>(-33.09%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>673.40 (n/a)</td><td>459.48 (n/a)</td><td>449.70 (n/a)</td><td>268.20 (n/a)</td><td>160.05 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.02 (-15.31%)</td><td>0.01 (-9.69%)</td><td>0.02 (+11.49%)</td><td>0.01 (-13.56%)</td><td>0.00 (+1.70%)</td><td>573.00 (+15.69%)</td><td>377.30 (+15.37%)</td><td>272.80 (-10.32%)</td><td>245.50 (+18.09%)</td><td>160.02 <b>(+40.90%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>495.30 (n/a)</td><td>327.04 (n/a)</td><td>304.20 (n/a)</td><td>207.90 (n/a)</td><td>113.57 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-9.93%)</td><td>20073.30 (-10.77%)</td><td>13256.90 (-8.75%)</td><td>12753.57 <b>(-23.79%)</b></td><td>6281.02 (+12.19%)</td><td>5679.58 <b>(-24.89%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22496.59 (n/a)</td><td>14527.35 (n/a)</td><td>16735.20 (n/a)</td><td>5598.71 (n/a)</td><td>7561.35 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.00 (-14.29%)</td><td>0.00 (-0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-17.59%)</td><td>22995.17 (-0.45%)</td><td>14655.61 (-0.10%)</td><td>17621.14 (+12.34%)</td><td>6584.00 (+11.99%)</td><td>7003.90 (-0.38%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>23099.68 (n/a)</td><td>14669.65 (n/a)</td><td>15685.36 (n/a)</td><td>5879.06 (n/a)</td><td>7030.36 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (+5.33%)</td><td>0.09 (-8.61%)</td><td>0.08 (-12.71%)</td><td>0.07 (-15.02%)</td><td>0.03 <b>(+46.84%)</b></td><td>30149.47 (+17.77%)</td><td>25509.68 (+12.73%)</td><td>27037.34 (+14.63%)</td><td>16081.15 (-5.09%)</td><td>5587.24 <b>(+61.26%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>25600.61 (n/a)</td><td>22629.24 (n/a)</td><td>23586.36 (n/a)</td><td>16942.91 (n/a)</td><td>3464.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.71 (+4.43%)</td><td>1.48 (+9.08%)</td><td>1.40 (-13.82%)</td><td>0.29 (-6.56%)</td><td>1.08 (+6.40%)</td><td>3576.90 (+7.02%)</td><td>1395.94 (-15.35%)</td><td>749.80 (+16.03%)</td><td>387.50 (-4.25%)</td><td>1352.11 (-11.86%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>2.59 (n/a)</td><td>1.36 (n/a)</td><td>1.62 (n/a)</td><td>0.31 (n/a)</td><td>1.01 (n/a)</td><td>3342.20 (n/a)</td><td>1649.14 (n/a)</td><td>646.20 (n/a)</td><td>404.70 (n/a)</td><td>1534.05 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.29 (-19.85%)</td><td>1.35 <b>(-32.73%)</b></td><td>1.64 <b>(-31.40%)</b></td><td>0.29 <b>(-70.69%)</b></td><td>0.99 (+12.74%)</td><td>3577.70 <b>(+241.19%)</b></td><td>1707.88 <b>(+169.05%)</b></td><td>638.60 <b>(+45.77%)</b></td><td>458.40 <b>(+24.77%)</b></td><td>1626.50 <b>(+397.77%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>2.85 (n/a)</td><td>2.01 (n/a)</td><td>2.39 (n/a)</td><td>1.00 (n/a)</td><td>0.88 (n/a)</td><td>1048.60 (n/a)</td><td>634.78 (n/a)</td><td>438.10 (n/a)</td><td>367.40 (n/a)</td><td>326.76 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.48 (-8.23%)</td><td>1.95 (-11.08%)</td><td>1.84 <b>(+21.29%)</b></td><td>0.30 <b>(-78.77%)</b></td><td>1.16 (+9.92%)</td><td>3505.60 <b>(+371.06%)</b></td><td>1086.50 <b>(+93.72%)</b></td><td>571.10 (-17.54%)</td><td>301.10 (+8.98%)</td><td>1358.12 <b>(+529.92%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.79 (n/a)</td><td>2.19 (n/a)</td><td>1.51 (n/a)</td><td>1.41 (n/a)</td><td>1.06 (n/a)</td><td>744.20 (n/a)</td><td>560.86 (n/a)</td><td>692.60 (n/a)</td><td>276.30 (n/a)</td><td>215.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.90 (-0.15%)</td><td>2.60 <b>(+33.22%)</b></td><td>2.48 <b>(+65.73%)</b></td><td>1.51 (+15.08%)</td><td>0.87 <b>(-20.39%)</b></td><td>695.70 (-13.11%)</td><td>444.02 <b>(-29.75%)</b></td><td>423.40 <b>(-39.66%)</b></td><td>269.10 (+0.15%)</td><td>158.43 <b>(-25.43%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.90 (n/a)</td><td>1.95 (n/a)</td><td>1.49 (n/a)</td><td>1.31 (n/a)</td><td>1.10 (n/a)</td><td>800.70 (n/a)</td><td>632.04 (n/a)</td><td>701.70 (n/a)</td><td>268.70 (n/a)</td><td>212.46 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>4.62 <b>(+37.52%)</b></td><td>3.25 <b>(+95.97%)</b></td><td>3.10 <b>(+396.50%)</b></td><td>2.56 <b>(+337.93%)</b></td><td>0.82 <b>(-42.75%)</b></td><td>820.40 <b>(-77.17%)</b></td><td>674.08 <b>(-71.05%)</b></td><td>677.10 <b>(-79.86%)</b></td><td>453.80 <b>(-27.28%)</b></td><td>144.60 <b>(-90.58%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.36 (n/a)</td><td>1.66 (n/a)</td><td>0.62 (n/a)</td><td>0.58 (n/a)</td><td>1.44 (n/a)</td><td>3592.80 (n/a)</td><td>2328.80 (n/a)</td><td>3361.90 (n/a)</td><td>624.00 (n/a)</td><td>1535.63 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>6.35 (+5.79%)</td><td>2.31 <b>(-29.29%)</b></td><td>1.11 <b>(-65.63%)</b></td><td>0.59 (+0.31%)</td><td>2.45 <b>(+27.81%)</b></td><td>3567.80 (-0.31%)</td><td>2006.30 <b>(+70.99%)</b></td><td>1891.30 <b>(+190.97%)</b></td><td>330.30 (-5.47%)</td><td>1517.34 (+12.32%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>6.00 (n/a)</td><td>3.27 (n/a)</td><td>3.23 (n/a)</td><td>0.59 (n/a)</td><td>1.92 (n/a)</td><td>3578.80 (n/a)</td><td>1173.34 (n/a)</td><td>650.00 (n/a)</td><td>349.40 (n/a)</td><td>1350.96 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>5.35 (-0.91%)</td><td>2.39 (-16.32%)</td><td>2.48 (-18.39%)</td><td>0.60 (-0.12%)</td><td>1.97 (+11.41%)</td><td>3522.20 (+0.12%)</td><td>1792.64 <b>(+42.51%)</b></td><td>845.00 <b>(+22.53%)</b></td><td>392.10 (+0.93%)</td><td>1570.09 <b>(+22.21%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.40 (n/a)</td><td>2.85 (n/a)</td><td>3.04 (n/a)</td><td>0.60 (n/a)</td><td>1.76 (n/a)</td><td>3518.10 (n/a)</td><td>1257.88 (n/a)</td><td>689.60 (n/a)</td><td>388.50 (n/a)</td><td>1284.75 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>6.69 <b>(+26.72%)</b></td><td>4.56 <b>(+57.17%)</b></td><td>4.30 <b>(+60.02%)</b></td><td>2.82 <b>(+379.68%)</b></td><td>1.51 <b>(-24.12%)</b></td><td>743.50 <b>(-79.15%)</b></td><td>502.68 <b>(-62.40%)</b></td><td>487.50 <b>(-37.51%)</b></td><td>313.50 <b>(-21.09%)</b></td><td>167.78 <b>(-87.27%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.28 (n/a)</td><td>2.90 (n/a)</td><td>2.69 (n/a)</td><td>0.59 (n/a)</td><td>2.00 (n/a)</td><td>3566.60 (n/a)</td><td>1337.00 (n/a)</td><td>780.10 (n/a)</td><td>397.30 (n/a)</td><td>1318.23 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>3.61 <b>(-26.07%)</b></td><td>2.62 <b>(-33.91%)</b></td><td>2.92 <b>(-24.93%)</b></td><td>0.85 <b>(-72.28%)</b></td><td>1.14 <b>(+59.52%)</b></td><td>2479.20 <b>(+260.77%)</b></td><td>1067.10 <b>(+96.10%)</b></td><td>717.10 <b>(+33.19%)</b></td><td>581.50 <b>(+35.26%)</b></td><td>804.17 <b>(+697.29%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>4.88 (n/a)</td><td>3.96 (n/a)</td><td>3.90 (n/a)</td><td>3.05 (n/a)</td><td>0.72 (n/a)</td><td>687.20 (n/a)</td><td>544.16 (n/a)</td><td>538.40 (n/a)</td><td>429.90 (n/a)</td><td>100.86 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>4.24 <b>(-20.75%)</b></td><td>3.02 <b>(-20.45%)</b></td><td>2.67 <b>(-25.99%)</b></td><td>2.07 <b>(-28.50%)</b></td><td>0.84 (-15.68%)</td><td>1014.90 <b>(+39.87%)</b></td><td>738.14 <b>(+27.00%)</b></td><td>784.00 <b>(+35.13%)</b></td><td>494.80 <b>(+26.19%)</b></td><td>198.14 <b>(+45.05%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.35 (n/a)</td><td>3.79 (n/a)</td><td>3.61 (n/a)</td><td>2.89 (n/a)</td><td>1.00 (n/a)</td><td>725.60 (n/a)</td><td>581.20 (n/a)</td><td>580.20 (n/a)</td><td>392.10 (n/a)</td><td>136.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>5.26 (+4.17%)</td><td>3.58 (-1.81%)</td><td>3.91 (-5.95%)</td><td>1.14 (+2.16%)</td><td>1.51 (-0.95%)</td><td>3682.90 (-2.12%)</td><td>1554.00 (+0.23%)</td><td>1072.10 (+6.32%)</td><td>797.40 (-4.01%)</td><td>1198.15 (-3.68%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>5.05 (n/a)</td><td>3.65 (n/a)</td><td>4.16 (n/a)</td><td>1.11 (n/a)</td><td>1.52 (n/a)</td><td>3762.60 (n/a)</td><td>1550.48 (n/a)</td><td>1008.40 (n/a)</td><td>830.70 (n/a)</td><td>1243.89 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>7.88 (-9.85%)</td><td>5.69 (-1.53%)</td><td>5.79 (-2.01%)</td><td>4.01 (+11.47%)</td><td>1.47 <b>(-29.80%)</b></td><td>1045.10 (-10.29%)</td><td>776.18 (-3.83%)</td><td>724.30 (+2.06%)</td><td>532.00 (+10.93%)</td><td>195.55 <b>(-32.56%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>8.75 (n/a)</td><td>5.78 (n/a)</td><td>5.91 (n/a)</td><td>3.60 (n/a)</td><td>2.09 (n/a)</td><td>1165.00 (n/a)</td><td>807.12 (n/a)</td><td>709.70 (n/a)</td><td>479.60 (n/a)</td><td>289.97 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>5.85 <b>(-20.75%)</b></td><td>3.52 <b>(-29.16%)</b></td><td>4.00 <b>(-32.72%)</b></td><td>1.09 (-13.34%)</td><td>1.91 <b>(-23.47%)</b></td><td>3834.60 (+15.40%)</td><td>1705.62 <b>(+33.49%)</b></td><td>1049.00 <b>(+48.63%)</b></td><td>716.90 <b>(+26.17%)</b></td><td>1289.07 (+10.52%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>7.38 (n/a)</td><td>4.96 (n/a)</td><td>5.94 (n/a)</td><td>1.26 (n/a)</td><td>2.50 (n/a)</td><td>3322.90 (n/a)</td><td>1277.72 (n/a)</td><td>705.80 (n/a)</td><td>568.20 (n/a)</td><td>1166.38 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>10.06 <b>(+53.13%)</b></td><td>5.22 <b>(+48.50%)</b></td><td>5.31 <b>(+35.57%)</b></td><td>1.26 (+13.74%)</td><td>3.21 <b>(+52.13%)</b></td><td>3337.60 (-12.08%)</td><td>1275.90 <b>(-26.25%)</b></td><td>790.30 <b>(-26.24%)</b></td><td>417.10 <b>(-34.70%)</b></td><td>1176.92 (-7.55%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>6.57 (n/a)</td><td>3.51 (n/a)</td><td>3.91 (n/a)</td><td>1.10 (n/a)</td><td>2.11 (n/a)</td><td>3796.30 (n/a)</td><td>1730.10 (n/a)</td><td>1071.50 (n/a)</td><td>638.70 (n/a)</td><td>1273.01 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>9.34 (+11.20%)</td><td>4.87 <b>(-29.71%)</b></td><td>3.92 <b>(-45.29%)</b></td><td>1.15 <b>(-71.18%)</b></td><td>3.62 <b>(+100.23%)</b></td><td>3660.90 <b>(+246.97%)</b></td><td>1560.74 <b>(+139.25%)</b></td><td>1069.20 <b>(+82.80%)</b></td><td>449.20 (-10.07%)</td><td>1345.86 <b>(+481.55%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>8.40 (n/a)</td><td>6.93 (n/a)</td><td>7.17 (n/a)</td><td>3.98 (n/a)</td><td>1.81 (n/a)</td><td>1055.10 (n/a)</td><td>652.36 (n/a)</td><td>584.90 (n/a)</td><td>499.50 (n/a)</td><td>231.43 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>9.60 (+3.59%)</td><td>7.83 <b>(+47.70%)</b></td><td>6.85 <b>(+60.41%)</b></td><td>6.51 <b>(+423.86%)</b></td><td>1.54 <b>(-53.00%)</b></td><td>644.40 <b>(-80.91%)</b></td><td>551.30 <b>(-57.26%)</b></td><td>612.10 <b>(-37.66%)</b></td><td>436.80 (-3.47%)</td><td>101.42 <b>(-91.55%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>9.27 (n/a)</td><td>5.30 (n/a)</td><td>4.27 (n/a)</td><td>1.24 (n/a)</td><td>3.27 (n/a)</td><td>3375.50 (n/a)</td><td>1290.00 (n/a)</td><td>981.80 (n/a)</td><td>452.50 (n/a)</td><td>1200.02 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.91 <b>(+27.86%)</b></td><td>1.21 (+5.31%)</td><td>1.32 (+19.86%)</td><td>0.62 (-1.85%)</td><td>0.56 <b>(+60.00%)</b></td><td>851.40 (+1.89%)</td><td>528.56 (+5.10%)</td><td>398.70 (-16.57%)</td><td>274.90 <b>(-21.79%)</b></td><td>264.57 <b>(+34.90%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.49 (n/a)</td><td>1.15 (n/a)</td><td>1.10 (n/a)</td><td>0.63 (n/a)</td><td>0.35 (n/a)</td><td>835.60 (n/a)</td><td>502.90 (n/a)</td><td>477.90 (n/a)</td><td>351.50 (n/a)</td><td>196.12 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.83 (+1.39%)</td><td>1.82 (+7.86%)</td><td>1.80 <b>(-23.28%)</b></td><td>0.30 (-0.78%)</td><td>0.97 <b>(-24.27%)</b></td><td>3522.20 (+0.79%)</td><td>1101.38 <b>(-32.18%)</b></td><td>582.70 <b>(+30.33%)</b></td><td>370.00 (-1.36%)</td><td>1356.89 (-18.83%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>2.80 (n/a)</td><td>1.69 (n/a)</td><td>2.35 (n/a)</td><td>0.30 (n/a)</td><td>1.28 (n/a)</td><td>3494.60 (n/a)</td><td>1623.98 (n/a)</td><td>447.10 (n/a)</td><td>375.10 (n/a)</td><td>1671.67 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>2.74 <b>(-22.81%)</b></td><td>1.59 <b>(-23.86%)</b></td><td>0.99 <b>(-56.02%)</b></td><td>0.60 (-0.03%)</td><td>1.06 <b>(-26.45%)</b></td><td>3518.10 (+0.03%)</td><td>1918.76 (+5.02%)</td><td>2113.90 <b>(+127.35%)</b></td><td>765.40 <b>(+29.53%)</b></td><td>1174.33 <b>(-23.39%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>3.55 (n/a)</td><td>2.08 (n/a)</td><td>2.26 (n/a)</td><td>0.60 (n/a)</td><td>1.44 (n/a)</td><td>3516.90 (n/a)</td><td>1827.12 (n/a)</td><td>929.80 (n/a)</td><td>590.90 (n/a)</td><td>1532.83 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>1.04 <b>(-41.16%)</b></td><td>0.70 <b>(-42.04%)</b></td><td>0.67 <b>(-56.42%)</b></td><td>0.22 <b>(-24.26%)</b></td><td>0.33 <b>(-48.94%)</b></td><td>2415.00 <b>(+32.02%)</b></td><td>1020.44 <b>(+48.18%)</b></td><td>780.30 <b>(+129.50%)</b></td><td>503.90 <b>(+69.95%)</b></td><td>794.45 <b>(+21.28%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>1.77 (n/a)</td><td>1.21 (n/a)</td><td>1.54 (n/a)</td><td>0.29 (n/a)</td><td>0.64 (n/a)</td><td>1829.20 (n/a)</td><td>688.64 (n/a)</td><td>340.00 (n/a)</td><td>296.50 (n/a)</td><td>655.03 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.13 (+13.33%)</td><td>0.11 <b>(+33.41%)</b></td><td>0.11 <b>(+63.79%)</b></td><td>0.07 (+19.57%)</td><td>0.02 (-8.12%)</td><td>464.70 (-16.36%)</td><td>325.00 <b>(-27.06%)</b></td><td>301.70 <b>(-38.95%)</b></td><td>256.00 (-11.75%)</td><td>83.83 <b>(-32.81%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>555.60 (n/a)</td><td>445.60 (n/a)</td><td>494.20 (n/a)</td><td>290.10 (n/a)</td><td>124.76 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.10 (-4.21%)</td><td>0.07 (-2.08%)</td><td>0.06 (-0.04%)</td><td>0.05 <b>(+23.58%)</b></td><td>0.02 (-19.01%)</td><td>604.00 (-19.09%)</td><td>497.62 (-1.95%)</td><td>536.80 (+0.06%)</td><td>313.60 (+4.39%)</td><td>118.62 <b>(-30.85%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>746.50 (n/a)</td><td>507.50 (n/a)</td><td>536.50 (n/a)</td><td>300.40 (n/a)</td><td>171.55 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.36 <b>(+67.25%)</b></td><td>0.21 <b>(+23.61%)</b></td><td>0.17 (-0.99%)</td><td>0.11 <b>(+26.49%)</b></td><td>0.10 <b>(+100.12%)</b></td><td>573.00 <b>(-20.94%)</b></td><td>375.08 (-12.89%)</td><td>376.00 (+0.99%)</td><td>182.90 <b>(-40.21%)</b></td><td>160.19 (-6.93%)</td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>724.80 (n/a)</td><td>430.58 (n/a)</td><td>372.30 (n/a)</td><td>305.90 (n/a)</td><td>172.12 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.34 (+7.88%)</td><td>0.20 (+8.57%)</td><td>0.17 <b>(+22.55%)</b></td><td>0.14 <b>(+26.72%)</b></td><td>0.08 (-5.89%)</td><td>476.50 <b>(-21.08%)</b></td><td>360.32 (-12.68%)</td><td>382.80 (-18.40%)</td><td>191.80 (-7.30%)</td><td>120.17 <b>(-29.16%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.32 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>603.80 (n/a)</td><td>412.64 (n/a)</td><td>469.10 (n/a)</td><td>206.90 (n/a)</td><td>169.63 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.35 <b>(+27.03%)</b></td><td>0.18 (+3.23%)</td><td>0.13 (-5.42%)</td><td>0.10 (-11.51%)</td><td>0.10 <b>(+55.33%)</b></td><td>644.10 (+13.00%)</td><td>451.46 (+6.16%)</td><td>502.50 (+5.72%)</td><td>186.20 <b>(-21.30%)</b></td><td>176.74 <b>(+33.56%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.28 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>570.00 (n/a)</td><td>425.26 (n/a)</td><td>475.30 (n/a)</td><td>236.60 (n/a)</td><td>132.33 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.58 (+3.90%)</td><td>0.45 (+8.32%)</td><td>0.49 (+15.35%)</td><td>0.21 <b>(-29.39%)</b></td><td>0.14 <b>(+45.87%)</b></td><td>637.40 <b>(+41.64%)</b></td><td>337.10 (+0.99%)</td><td>270.10 (-13.29%)</td><td>227.40 (-3.77%)</td><td>169.75 <b>(+113.27%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.55 (n/a)</td><td>0.41 (n/a)</td><td>0.42 (n/a)</td><td>0.29 (n/a)</td><td>0.10 (n/a)</td><td>450.00 (n/a)</td><td>333.78 (n/a)</td><td>311.50 (n/a)</td><td>236.30 (n/a)</td><td>79.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.31 <b>(-36.91%)</b></td><td>0.25 <b>(-25.33%)</b></td><td>0.24 <b>(-20.78%)</b></td><td>0.21 (+9.14%)</td><td>0.04 <b>(-68.37%)</b></td><td>611.40 (-8.38%)</td><td>523.18 <b>(+23.18%)</b></td><td>544.50 <b>(+26.22%)</b></td><td>429.60 <b>(+58.52%)</b></td><td>71.79 <b>(-53.86%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.48 (n/a)</td><td>0.34 (n/a)</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.11 (n/a)</td><td>667.30 (n/a)</td><td>424.72 (n/a)</td><td>431.40 (n/a)</td><td>271.00 (n/a)</td><td>155.60 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.29 <b>(-51.34%)</b></td><td>0.26 (-6.13%)</td><td>0.26 (+16.17%)</td><td>0.24 <b>(+105.08%)</b></td><td>0.02 <b>(-90.87%)</b></td><td>543.90 <b>(-51.24%)</b></td><td>497.04 (-17.65%)</td><td>496.40 (-13.92%)</td><td>459.50 <b>(+105.50%)</b></td><td>31.15 <b>(-90.34%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.59 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.18 (n/a)</td><td>1115.40 (n/a)</td><td>603.60 (n/a)</td><td>576.70 (n/a)</td><td>223.60 (n/a)</td><td>322.35 (n/a)</td>
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
<td><code>27cf75d</code> — 2026-09-18 15:33:09</td><td>0.06 <b>(+47.13%)</b></td><td>0.04 <b>(+57.85%)</b></td><td>0.04 (+17.28%)</td><td>0.03 <b>(+250.91%)</b></td><td>0.01 <b>(-23.54%)</b></td><td>549.70 <b>(-71.50%)</b></td><td>422.20 <b>(-52.26%)</b></td><td>426.80 (-14.73%)</td><td>288.60 <b>(-32.03%)</b></td><td>93.73 <b>(-85.37%)</b></td>
</tr>
<tr>
<td><code>0c0eaee</code> — 2026-09-18 00:09:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1929.10 (n/a)</td><td>884.38 (n/a)</td><td>500.50 (n/a)</td><td>424.60 (n/a)</td><td>640.67 (n/a)</td>
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
