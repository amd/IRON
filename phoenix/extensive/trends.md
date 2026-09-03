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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-0.88%)</td><td>0.02 (+10.74%)</td><td>0.02 <b>(+25.96%)</b></td><td>0.01 <b>(+25.18%)</b></td><td>0.00 <b>(-33.88%)</b></td><td>432.10 <b>(-20.11%)</b></td><td>329.62 (-14.87%)</td><td>298.10 <b>(-20.61%)</b></td><td>261.40 (+0.89%)</td><td>72.30 <b>(-44.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>540.90 (n/a)</td><td>387.20 (n/a)</td><td>375.50 (n/a)</td><td>259.10 (n/a)</td><td>130.88 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (-1.94%)</td><td>0.02 (-12.21%)</td><td>0.01 <b>(-29.32%)</b></td><td>0.01 (+5.65%)</td><td>0.01 (-6.27%)</td><td>515.60 (-5.34%)</td><td>420.20 (+11.97%)</td><td>456.20 <b>(+41.50%)</b></td><td>244.20 (+1.96%)</td><td>106.79 (-15.51%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>544.70 (n/a)</td><td>375.28 (n/a)</td><td>322.40 (n/a)</td><td>239.50 (n/a)</td><td>126.39 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-13.81%)</td><td>0.02 (+15.98%)</td><td>0.02 <b>(+72.77%)</b></td><td>0.01 <b>(+54.39%)</b></td><td>0.01 <b>(-32.45%)</b></td><td>508.40 <b>(-35.23%)</b></td><td>349.26 <b>(-22.95%)</b></td><td>277.50 <b>(-42.12%)</b></td><td>266.40 (+16.03%)</td><td>109.69 <b>(-49.48%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>784.90 (n/a)</td><td>453.28 (n/a)</td><td>479.40 (n/a)</td><td>229.60 (n/a)</td><td>217.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 <b>(-21.46%)</b></td><td>0.02 <b>(-25.48%)</b></td><td>0.01 <b>(-31.46%)</b></td><td>0.01 <b>(-56.74%)</b></td><td>0.01 (-1.95%)</td><td>1093.30 <b>(+131.14%)</b></td><td>511.88 <b>(+54.97%)</b></td><td>413.80 <b>(+45.91%)</b></td><td>272.40 <b>(+27.35%)</b></td><td>337.21 <b>(+182.22%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>473.00 (n/a)</td><td>330.30 (n/a)</td><td>283.60 (n/a)</td><td>213.90 (n/a)</td><td>119.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 <b>(+99.27%)</b></td><td>0.02 <b>(+57.40%)</b></td><td>0.01 (+3.07%)</td><td>0.01 <b>(+225.35%)</b></td><td>0.01 <b>(+83.86%)</b></td><td>574.40 <b>(-69.27%)</b></td><td>420.06 <b>(-44.90%)</b></td><td>507.00 (-2.99%)</td><td>209.90 <b>(-49.81%)</b></td><td>163.58 <b>(-73.64%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1869.00 (n/a)</td><td>762.42 (n/a)</td><td>522.60 (n/a)</td><td>418.20 (n/a)</td><td>620.54 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 <b>(+50.10%)</b></td><td>0.02 (+12.76%)</td><td>0.01 <b>(-28.55%)</b></td><td>0.01 <b>(+79.16%)</b></td><td>0.01 <b>(+57.38%)</b></td><td>604.00 <b>(-44.19%)</b></td><td>427.04 (-13.85%)</td><td>494.80 <b>(+39.93%)</b></td><td>169.60 <b>(-33.39%)</b></td><td>181.58 <b>(-46.06%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1082.20 (n/a)</td><td>495.72 (n/a)</td><td>353.60 (n/a)</td><td>254.60 (n/a)</td><td>336.65 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 <b>(+67.15%)</b></td><td>0.05 <b>(+54.27%)</b></td><td>0.04 <b>(+69.05%)</b></td><td>0.02 (+10.92%)</td><td>0.02 <b>(+100.12%)</b></td><td>503.50 (-9.83%)</td><td>298.36 <b>(-30.68%)</b></td><td>288.50 <b>(-40.86%)</b></td><td>180.10 <b>(-40.17%)</b></td><td>128.24 (+11.01%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>558.40 (n/a)</td><td>430.40 (n/a)</td><td>487.80 (n/a)</td><td>301.00 (n/a)</td><td>115.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 <b>(+48.04%)</b></td><td>0.03 (-1.29%)</td><td>0.03 (-15.73%)</td><td>0.02 <b>(-24.76%)</b></td><td>0.02 <b>(+109.99%)</b></td><td>635.30 <b>(+32.91%)</b></td><td>429.22 (+13.73%)</td><td>439.90 (+18.67%)</td><td>185.60 <b>(-32.44%)</b></td><td>162.52 <b>(+69.42%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>478.00 (n/a)</td><td>377.40 (n/a)</td><td>370.70 (n/a)</td><td>274.70 (n/a)</td><td>95.93 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (+10.72%)</td><td>0.02 (+7.42%)</td><td>0.02 (+4.39%)</td><td>0.01 (+1.43%)</td><td>0.01 (+6.90%)</td><td>2082.10 (-1.42%)</td><td>772.46 (-5.12%)</td><td>512.30 (-4.21%)</td><td>284.50 (-9.68%)</td><td>738.53 (-0.01%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2112.00 (n/a)</td><td>814.16 (n/a)</td><td>534.80 (n/a)</td><td>315.00 (n/a)</td><td>738.61 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 <b>(+57.42%)</b></td><td>0.04 <b>(+64.81%)</b></td><td>0.04 <b>(+44.32%)</b></td><td>0.02 <b>(+243.46%)</b></td><td>0.01 <b>(+24.50%)</b></td><td>546.70 <b>(-70.88%)</b></td><td>366.02 <b>(-51.90%)</b></td><td>342.30 <b>(-30.71%)</b></td><td>225.40 <b>(-36.47%)</b></td><td>130.25 <b>(-79.38%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1877.70 (n/a)</td><td>760.92 (n/a)</td><td>494.00 (n/a)</td><td>354.80 (n/a)</td><td>631.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 <b>(+45.09%)</b></td><td>0.04 (+15.32%)</td><td>0.04 <b>(+48.35%)</b></td><td>0.02 (-5.64%)</td><td>0.02 <b>(+47.96%)</b></td><td>616.20 (+5.99%)</td><td>393.20 (-6.70%)</td><td>323.60 <b>(-32.58%)</b></td><td>171.80 <b>(-31.09%)</b></td><td>183.48 (+16.83%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>581.40 (n/a)</td><td>421.42 (n/a)</td><td>480.00 (n/a)</td><td>249.30 (n/a)</td><td>157.04 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 <b>(+38.54%)</b></td><td>0.04 (-7.83%)</td><td>0.02 <b>(-44.91%)</b></td><td>0.02 <b>(-21.61%)</b></td><td>0.02 <b>(+115.41%)</b></td><td>629.50 <b>(+27.56%)</b></td><td>441.62 <b>(+31.31%)</b></td><td>538.10 <b>(+81.48%)</b></td><td>167.50 <b>(-27.83%)</b></td><td>204.58 <b>(+100.72%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.50 (n/a)</td><td>336.32 (n/a)</td><td>296.50 (n/a)</td><td>232.10 (n/a)</td><td>101.92 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 <b>(-41.70%)</b></td><td>0.07 (-14.58%)</td><td>0.06 (-7.97%)</td><td>0.06 (+14.22%)</td><td>0.02 <b>(-56.58%)</b></td><td>443.10 (-12.45%)</td><td>360.12 (+1.67%)</td><td>406.70 (+8.66%)</td><td>249.50 <b>(+71.60%)</b></td><td>97.25 <b>(-35.27%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>506.10 (n/a)</td><td>354.22 (n/a)</td><td>374.30 (n/a)</td><td>145.40 (n/a)</td><td>150.24 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (+8.51%)</td><td>0.06 (-17.68%)</td><td>0.05 (-12.05%)</td><td>0.04 <b>(-25.02%)</b></td><td>0.04 (+8.77%)</td><td>670.20 <b>(+33.37%)</b></td><td>464.88 <b>(+25.66%)</b></td><td>487.80 (+13.68%)</td><td>189.70 (-7.87%)</td><td>172.98 <b>(+20.12%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>502.50 (n/a)</td><td>369.94 (n/a)</td><td>429.10 (n/a)</td><td>205.90 (n/a)</td><td>144.00 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (-8.57%)</td><td>0.07 (+9.05%)</td><td>0.07 <b>(+20.37%)</b></td><td>0.04 (+7.10%)</td><td>0.02 (-15.94%)</td><td>562.90 (-6.62%)</td><td>403.62 (-9.95%)</td><td>376.90 (-16.91%)</td><td>264.20 (+9.35%)</td><td>123.19 (-6.05%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>602.80 (n/a)</td><td>448.20 (n/a)</td><td>453.60 (n/a)</td><td>241.60 (n/a)</td><td>131.13 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (+14.40%)</td><td>0.08 <b>(+21.74%)</b></td><td>0.09 <b>(+45.92%)</b></td><td>0.05 (+13.20%)</td><td>0.03 <b>(+24.58%)</b></td><td>526.90 (-11.65%)</td><td>359.38 (-16.28%)</td><td>270.20 <b>(-31.46%)</b></td><td>244.30 (-12.56%)</td><td>143.46 (-4.62%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>596.40 (n/a)</td><td>429.28 (n/a)</td><td>394.20 (n/a)</td><td>279.40 (n/a)</td><td>150.40 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (-19.53%)</td><td>0.06 (-13.20%)</td><td>0.06 <b>(+22.21%)</b></td><td>0.04 (-0.20%)</td><td>0.02 <b>(-34.90%)</b></td><td>645.60 (+0.20%)</td><td>433.36 (+6.57%)</td><td>379.80 (-18.16%)</td><td>250.40 <b>(+24.27%)</b></td><td>155.52 (-14.19%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>644.30 (n/a)</td><td>406.66 (n/a)</td><td>464.10 (n/a)</td><td>201.50 (n/a)</td><td>181.24 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (-0.74%)</td><td>0.08 <b>(+21.53%)</b></td><td>0.08 <b>(+66.03%)</b></td><td>0.05 <b>(+24.92%)</b></td><td>0.02 <b>(-29.67%)</b></td><td>471.50 (-19.95%)</td><td>331.80 <b>(-22.85%)</b></td><td>301.10 <b>(-39.77%)</b></td><td>251.90 (+0.76%)</td><td>86.68 <b>(-41.29%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>589.00 (n/a)</td><td>430.06 (n/a)</td><td>499.90 (n/a)</td><td>250.00 (n/a)</td><td>147.65 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.25 (+17.54%)</td><td>0.12 <b>(-20.94%)</b></td><td>0.11 (-17.48%)</td><td>0.03 <b>(-74.28%)</b></td><td>0.08 <b>(+65.15%)</b></td><td>1899.90 <b>(+288.85%)</b></td><td>691.32 <b>(+97.43%)</b></td><td>449.70 <b>(+21.18%)</b></td><td>200.40 (-14.94%)</td><td>685.56 <b>(+538.56%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>488.60 (n/a)</td><td>350.16 (n/a)</td><td>371.10 (n/a)</td><td>235.60 (n/a)</td><td>107.36 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.23 (+0.21%)</td><td>0.12 <b>(-31.44%)</b></td><td>0.10 <b>(-50.13%)</b></td><td>0.09 (-6.22%)</td><td>0.06 (+17.13%)</td><td>559.40 (+6.63%)</td><td>450.98 <b>(+50.03%)</b></td><td>496.00 <b>(+100.57%)</b></td><td>211.10 (-0.19%)</td><td>139.90 (+9.97%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>524.60 (n/a)</td><td>300.60 (n/a)</td><td>247.30 (n/a)</td><td>211.50 (n/a)</td><td>127.22 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.18 <b>(-20.92%)</b></td><td>0.12 <b>(-31.16%)</b></td><td>0.10 <b>(-50.90%)</b></td><td>0.08 <b>(-21.69%)</b></td><td>0.05 (-2.72%)</td><td>642.00 <b>(+27.68%)</b></td><td>445.44 <b>(+49.44%)</b></td><td>511.70 <b>(+103.70%)</b></td><td>276.80 <b>(+26.45%)</b></td><td>160.41 <b>(+37.54%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>502.80 (n/a)</td><td>298.08 (n/a)</td><td>251.20 (n/a)</td><td>218.90 (n/a)</td><td>116.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.24 (+2.04%)</td><td>0.12 <b>(-24.92%)</b></td><td>0.11 <b>(-35.92%)</b></td><td>0.06 <b>(-27.86%)</b></td><td>0.07 (+9.78%)</td><td>873.90 <b>(+38.60%)</b></td><td>525.66 <b>(+42.23%)</b></td><td>463.60 <b>(+56.04%)</b></td><td>202.90 (-2.03%)</td><td>249.52 <b>(+40.71%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>630.50 (n/a)</td><td>369.58 (n/a)</td><td>297.10 (n/a)</td><td>207.10 (n/a)</td><td>177.33 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.26 (+12.35%)</td><td>0.16 (-13.79%)</td><td>0.14 <b>(-30.90%)</b></td><td>0.09 (-10.33%)</td><td>0.07 <b>(+37.18%)</b></td><td>549.80 (+11.52%)</td><td>360.12 <b>(+22.97%)</b></td><td>349.00 <b>(+44.75%)</b></td><td>192.30 (-10.97%)</td><td>146.54 <b>(+28.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>493.00 (n/a)</td><td>292.86 (n/a)</td><td>241.10 (n/a)</td><td>216.00 (n/a)</td><td>113.80 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.18 (-11.35%)</td><td>0.11 <b>(-20.53%)</b></td><td>0.09 (-19.77%)</td><td>0.09 (-15.40%)</td><td>0.04 (-10.92%)</td><td>573.10 (+18.21%)</td><td>485.90 <b>(+26.04%)</b></td><td>549.30 <b>(+24.64%)</b></td><td>270.00 (+12.83%)</td><td>128.08 (+14.87%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>484.80 (n/a)</td><td>385.52 (n/a)</td><td>440.70 (n/a)</td><td>239.30 (n/a)</td><td>111.50 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (-2.27%)</td><td>0.01 (+18.75%)</td><td>0.01 (+8.70%)</td><td>0.01 <b>(+46.26%)</b></td><td>0.00 <b>(-34.85%)</b></td><td>357.10 <b>(-31.62%)</b></td><td>285.60 <b>(-22.50%)</b></td><td>272.60 (-8.00%)</td><td>224.70 (+2.32%)</td><td>59.19 <b>(-57.98%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>522.20 (n/a)</td><td>368.50 (n/a)</td><td>296.30 (n/a)</td><td>219.60 (n/a)</td><td>140.86 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 <b>(+87.30%)</b></td><td>0.01 <b>(+71.12%)</b></td><td>0.01 <b>(+68.91%)</b></td><td>0.01 <b>(+66.49%)</b></td><td>0.00 <b>(+97.05%)</b></td><td>464.30 <b>(-39.94%)</b></td><td>312.82 <b>(-40.97%)</b></td><td>283.30 <b>(-40.81%)</b></td><td>242.60 <b>(-46.62%)</b></td><td>88.02 <b>(-35.50%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>773.00 (n/a)</td><td>529.94 (n/a)</td><td>478.60 (n/a)</td><td>454.50 (n/a)</td><td>136.47 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (+0.59%)</td><td>0.01 (+13.61%)</td><td>0.01 <b>(+57.28%)</b></td><td>0.01 (+14.96%)</td><td>0.00 (-19.06%)</td><td>481.50 (-13.01%)</td><td>331.38 (-16.26%)</td><td>282.00 <b>(-36.41%)</b></td><td>227.70 (-0.57%)</td><td>105.77 <b>(-26.93%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>553.50 (n/a)</td><td>395.72 (n/a)</td><td>443.50 (n/a)</td><td>229.00 (n/a)</td><td>144.75 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 <b>(+31.87%)</b></td><td>0.01 <b>(+41.49%)</b></td><td>0.01 <b>(+79.27%)</b></td><td>0.01 (+11.47%)</td><td>0.00 <b>(+49.25%)</b></td><td>483.20 (-10.29%)</td><td>330.40 <b>(-26.89%)</b></td><td>274.00 <b>(-44.21%)</b></td><td>208.90 <b>(-24.15%)</b></td><td>113.26 (+9.61%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>538.60 (n/a)</td><td>451.92 (n/a)</td><td>491.10 (n/a)</td><td>275.40 (n/a)</td><td>103.33 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (+13.88%)</td><td>0.01 <b>(+34.29%)</b></td><td>0.01 <b>(+104.00%)</b></td><td>0.01 <b>(+21.90%)</b></td><td>0.00 (+15.86%)</td><td>495.20 (-17.96%)</td><td>331.86 <b>(-25.76%)</b></td><td>256.20 <b>(-50.98%)</b></td><td>234.30 (-12.21%)</td><td>123.00 (-16.81%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>603.60 (n/a)</td><td>447.02 (n/a)</td><td>522.60 (n/a)</td><td>266.90 (n/a)</td><td>147.85 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (+0.22%)</td><td>0.01 (+13.44%)</td><td>0.01 (+13.07%)</td><td>0.00 (+9.43%)</td><td>0.00 (-4.76%)</td><td>571.70 (-8.62%)</td><td>447.24 (-12.53%)</td><td>443.20 (-11.55%)</td><td>362.60 (-0.22%)</td><td>88.87 (-16.98%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>625.60 (n/a)</td><td>511.28 (n/a)</td><td>501.10 (n/a)</td><td>363.40 (n/a)</td><td>107.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (+0.63%)</td><td>0.02 (+7.22%)</td><td>0.02 (+5.23%)</td><td>0.01 (+3.55%)</td><td>0.00 (-10.40%)</td><td>645.40 (-3.43%)</td><td>377.50 (-9.19%)</td><td>295.20 (-4.96%)</td><td>265.70 (-0.64%)</td><td>156.93 (-11.62%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>668.30 (n/a)</td><td>415.70 (n/a)</td><td>310.60 (n/a)</td><td>267.40 (n/a)</td><td>177.57 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (+17.78%)</td><td>0.02 <b>(+33.77%)</b></td><td>0.02 <b>(+61.46%)</b></td><td>0.01 (-4.19%)</td><td>0.01 <b>(+29.82%)</b></td><td>599.70 (+4.37%)</td><td>346.08 <b>(-21.07%)</b></td><td>292.90 <b>(-38.08%)</b></td><td>194.50 (-15.10%)</td><td>161.88 <b>(+25.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>574.60 (n/a)</td><td>438.46 (n/a)</td><td>473.00 (n/a)</td><td>229.10 (n/a)</td><td>129.16 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-6.18%)</td><td>0.01 <b>(+25.19%)</b></td><td>0.01 <b>(+36.15%)</b></td><td>0.01 <b>(+81.91%)</b></td><td>0.00 <b>(-35.10%)</b></td><td>576.90 <b>(-45.03%)</b></td><td>413.72 <b>(-31.81%)</b></td><td>413.60 <b>(-26.55%)</b></td><td>257.80 (+6.62%)</td><td>114.00 <b>(-61.18%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1049.40 (n/a)</td><td>606.70 (n/a)</td><td>563.10 (n/a)</td><td>241.80 (n/a)</td><td>293.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 <b>(-30.40%)</b></td><td>0.01 <b>(-31.36%)</b></td><td>0.01 (-12.44%)</td><td>0.00 <b>(-79.39%)</b></td><td>0.00 <b>(+51.03%)</b></td><td>2487.40 <b>(+385.25%)</b></td><td>889.16 <b>(+118.97%)</b></td><td>483.10 (+14.21%)</td><td>426.90 <b>(+43.69%)</b></td><td>896.31 <b>(+1031.36%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>512.60 (n/a)</td><td>406.06 (n/a)</td><td>423.00 (n/a)</td><td>297.10 (n/a)</td><td>79.22 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-0.17%)</td><td>0.01 (-13.73%)</td><td>0.01 <b>(-23.02%)</b></td><td>0.01 <b>(-39.04%)</b></td><td>0.01 <b>(+68.49%)</b></td><td>598.40 <b>(+64.04%)</b></td><td>395.44 <b>(+25.19%)</b></td><td>410.40 <b>(+29.87%)</b></td><td>238.80 (+0.17%)</td><td>139.09 <b>(+171.69%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>364.80 (n/a)</td><td>315.88 (n/a)</td><td>316.00 (n/a)</td><td>238.40 (n/a)</td><td>51.19 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-7.86%)</td><td>0.01 (+11.48%)</td><td>0.01 <b>(+37.12%)</b></td><td>0.01 (+12.04%)</td><td>0.00 <b>(-20.66%)</b></td><td>507.10 (-10.75%)</td><td>413.92 (-11.77%)</td><td>365.50 <b>(-27.08%)</b></td><td>348.80 (+8.56%)</td><td>78.88 <b>(-22.84%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>568.20 (n/a)</td><td>469.16 (n/a)</td><td>501.20 (n/a)</td><td>321.30 (n/a)</td><td>102.23 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 <b>(+26.49%)</b></td><td>0.04 <b>(+29.59%)</b></td><td>0.03 <b>(+54.31%)</b></td><td>0.03 <b>(+54.68%)</b></td><td>0.01 (-11.80%)</td><td>336.40 <b>(-35.34%)</b></td><td>294.00 <b>(-26.93%)</b></td><td>307.50 <b>(-35.19%)</b></td><td>199.60 <b>(-20.95%)</b></td><td>54.61 <b>(-56.22%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>520.30 (n/a)</td><td>402.36 (n/a)</td><td>474.50 (n/a)</td><td>252.50 (n/a)</td><td>124.74 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 <b>(+56.15%)</b></td><td>0.03 <b>(+40.67%)</b></td><td>0.02 <b>(+32.86%)</b></td><td>0.02 <b>(+22.50%)</b></td><td>0.01 <b>(+113.54%)</b></td><td>538.40 (-18.36%)</td><td>425.68 <b>(-25.64%)</b></td><td>474.90 <b>(-24.73%)</b></td><td>257.90 <b>(-35.96%)</b></td><td>120.29 (+14.01%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>659.50 (n/a)</td><td>572.44 (n/a)</td><td>630.90 (n/a)</td><td>402.70 (n/a)</td><td>105.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (+1.62%)</td><td>0.02 (+0.39%)</td><td>0.02 <b>(-24.99%)</b></td><td>0.02 <b>(+217.16%)</b></td><td>0.01 <b>(-37.30%)</b></td><td>600.20 <b>(-68.47%)</b></td><td>473.22 <b>(-32.02%)</b></td><td>490.80 <b>(+33.33%)</b></td><td>294.50 (-1.60%)</td><td>123.37 <b>(-81.92%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1903.50 (n/a)</td><td>696.14 (n/a)</td><td>368.10 (n/a)</td><td>299.30 (n/a)</td><td>682.32 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (-3.89%)</td><td>0.03 (-0.76%)</td><td>0.03 (+3.36%)</td><td>0.02 (-11.74%)</td><td>0.01 (-6.51%)</td><td>601.90 (+13.31%)</td><td>390.58 (+0.48%)</td><td>319.20 (-3.24%)</td><td>268.40 (+4.07%)</td><td>137.54 (+4.33%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.20 (n/a)</td><td>388.70 (n/a)</td><td>329.90 (n/a)</td><td>257.90 (n/a)</td><td>131.84 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 <b>(+49.83%)</b></td><td>0.03 <b>(+29.62%)</b></td><td>0.03 (+10.20%)</td><td>0.02 (+13.23%)</td><td>0.01 <b>(+104.32%)</b></td><td>461.30 (-11.70%)</td><td>365.00 (-18.95%)</td><td>419.20 (-9.26%)</td><td>207.00 <b>(-33.25%)</b></td><td>103.45 (+19.84%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.40 (n/a)</td><td>450.34 (n/a)</td><td>462.00 (n/a)</td><td>310.10 (n/a)</td><td>86.33 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (-7.11%)</td><td>0.02 (+9.92%)</td><td>0.02 (+8.90%)</td><td>0.02 <b>(+33.86%)</b></td><td>0.00 <b>(-48.51%)</b></td><td>559.70 <b>(-25.29%)</b></td><td>472.02 (-13.05%)</td><td>474.90 (-8.16%)</td><td>405.50 (+7.65%)</td><td>60.42 <b>(-58.91%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>749.20 (n/a)</td><td>542.86 (n/a)</td><td>517.10 (n/a)</td><td>376.70 (n/a)</td><td>147.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (+10.03%)</td><td>0.06 (+13.98%)</td><td>0.07 <b>(+34.46%)</b></td><td>0.04 (-16.96%)</td><td>0.02 <b>(+49.88%)</b></td><td>586.20 <b>(+20.42%)</b></td><td>355.64 (-7.72%)</td><td>297.30 <b>(-25.62%)</b></td><td>256.70 (-9.13%)</td><td>132.45 <b>(+77.02%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>486.80 (n/a)</td><td>385.38 (n/a)</td><td>399.70 (n/a)</td><td>282.50 (n/a)</td><td>74.82 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (+3.82%)</td><td>0.05 (+1.28%)</td><td>0.04 <b>(-29.75%)</b></td><td>0.03 <b>(+216.75%)</b></td><td>0.02 <b>(-39.41%)</b></td><td>656.30 <b>(-68.43%)</b></td><td>459.10 <b>(-39.71%)</b></td><td>470.70 <b>(+42.33%)</b></td><td>262.50 (-3.71%)</td><td>141.33 <b>(-81.68%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2078.70 (n/a)</td><td>761.46 (n/a)</td><td>330.70 (n/a)</td><td>272.60 (n/a)</td><td>771.29 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (-8.30%)</td><td>0.07 (-4.89%)</td><td>0.07 (-9.33%)</td><td>0.04 (-5.76%)</td><td>0.02 (-9.86%)</td><td>490.70 (+6.12%)</td><td>340.98 (+4.47%)</td><td>303.30 (+10.29%)</td><td>224.50 (+9.03%)</td><td>110.47 (+2.21%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>462.40 (n/a)</td><td>326.38 (n/a)</td><td>275.00 (n/a)</td><td>205.90 (n/a)</td><td>108.08 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 <b>(+51.74%)</b></td><td>0.05 (+17.81%)</td><td>0.05 (-4.89%)</td><td>0.04 <b>(+74.00%)</b></td><td>0.02 <b>(+38.85%)</b></td><td>567.30 <b>(-42.52%)</b></td><td>438.94 (-18.70%)</td><td>460.30 (+5.14%)</td><td>234.40 <b>(-34.10%)</b></td><td>123.32 <b>(-52.61%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>987.00 (n/a)</td><td>539.90 (n/a)</td><td>437.80 (n/a)</td><td>355.70 (n/a)</td><td>260.20 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (+3.16%)</td><td>0.06 (-2.57%)</td><td>0.05 <b>(-21.80%)</b></td><td>0.04 (-1.99%)</td><td>0.02 (+16.62%)</td><td>564.90 (+2.04%)</td><td>402.90 (+5.14%)</td><td>437.60 <b>(+27.88%)</b></td><td>244.80 (-3.05%)</td><td>141.10 (+10.04%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>553.60 (n/a)</td><td>383.22 (n/a)</td><td>342.20 (n/a)</td><td>252.50 (n/a)</td><td>128.23 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 <b>(+30.96%)</b></td><td>0.05 <b>(+23.69%)</b></td><td>0.05 <b>(+33.06%)</b></td><td>0.04 (+14.19%)</td><td>0.02 <b>(+41.76%)</b></td><td>532.60 (-12.43%)</td><td>428.12 (-18.13%)</td><td>445.30 <b>(-24.84%)</b></td><td>260.60 <b>(-23.64%)</b></td><td>104.98 (-10.43%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>608.20 (n/a)</td><td>522.92 (n/a)</td><td>592.50 (n/a)</td><td>341.30 (n/a)</td><td>117.21 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>425.60 (n/a)</td><td>330.62 (n/a)</td><td>303.60 (n/a)</td><td>281.10 (n/a)</td><td>62.24 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>518.50 (n/a)</td><td>337.74 (n/a)</td><td>300.20 (n/a)</td><td>210.10 (n/a)</td><td>120.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.10 (n/a)</td><td>326.48 (n/a)</td><td>283.40 (n/a)</td><td>221.80 (n/a)</td><td>129.81 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.50 (n/a)</td><td>324.86 (n/a)</td><td>294.60 (n/a)</td><td>242.20 (n/a)</td><td>108.06 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2079.40 (n/a)</td><td>710.80 (n/a)</td><td>481.00 (n/a)</td><td>160.20 (n/a)</td><td>779.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>650.00 (n/a)</td><td>417.68 (n/a)</td><td>364.40 (n/a)</td><td>211.00 (n/a)</td><td>194.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>500.90 (n/a)</td><td>324.76 (n/a)</td><td>294.60 (n/a)</td><td>231.40 (n/a)</td><td>103.78 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>516.00 (n/a)</td><td>337.46 (n/a)</td><td>300.10 (n/a)</td><td>180.80 (n/a)</td><td>143.84 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>546.80 (n/a)</td><td>398.52 (n/a)</td><td>341.40 (n/a)</td><td>279.20 (n/a)</td><td>137.31 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.18 (-13.51%)</td><td>0.17 (+10.78%)</td><td>0.17 (-3.94%)</td><td>0.16 <b>(+107.53%)</b></td><td>0.01 <b>(-83.86%)</b></td><td>306.10 <b>(-51.81%)</b></td><td>286.04 <b>(-21.34%)</b></td><td>290.60 (+4.12%)</td><td>267.50 (+15.60%)</td><td>15.14 <b>(-91.02%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>635.20 (n/a)</td><td>363.66 (n/a)</td><td>279.10 (n/a)</td><td>231.40 (n/a)</td><td>168.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>588.80 (n/a)</td><td>461.24 (n/a)</td><td>453.20 (n/a)</td><td>306.60 (n/a)</td><td>126.09 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>2391.60 (n/a)</td><td>853.04 (n/a)</td><td>507.40 (n/a)</td><td>279.60 (n/a)</td><td>868.71 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>485.30 (n/a)</td><td>330.46 (n/a)</td><td>295.70 (n/a)</td><td>261.30 (n/a)</td><td>92.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>496.40 (n/a)</td><td>360.68 (n/a)</td><td>368.20 (n/a)</td><td>245.40 (n/a)</td><td>106.36 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1069.90 (n/a)</td><td>627.00 (n/a)</td><td>519.00 (n/a)</td><td>458.70 (n/a)</td><td>251.68 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.00 (n/a)</td><td>317.40 (n/a)</td><td>262.40 (n/a)</td><td>249.30 (n/a)</td><td>117.30 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>645.40 (n/a)</td><td>418.08 (n/a)</td><td>323.80 (n/a)</td><td>289.70 (n/a)</td><td>161.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>623.10 (n/a)</td><td>455.76 (n/a)</td><td>449.90 (n/a)</td><td>243.50 (n/a)</td><td>138.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>564.40 (n/a)</td><td>354.12 (n/a)</td><td>309.70 (n/a)</td><td>249.90 (n/a)</td><td>130.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>523.70 (n/a)</td><td>411.22 (n/a)</td><td>455.00 (n/a)</td><td>262.10 (n/a)</td><td>107.47 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>787.10 (n/a)</td><td>444.02 (n/a)</td><td>309.30 (n/a)</td><td>239.30 (n/a)</td><td>233.99 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.24 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>587.90 (n/a)</td><td>405.12 (n/a)</td><td>461.80 (n/a)</td><td>204.00 (n/a)</td><td>173.33 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.23 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>0.08 (n/a)</td><td>1944.70 (n/a)</td><td>706.84 (n/a)</td><td>439.60 (n/a)</td><td>209.30 (n/a)</td><td>708.02 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>462.30 (n/a)</td><td>361.80 (n/a)</td><td>372.10 (n/a)</td><td>273.30 (n/a)</td><td>84.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2068.80 (n/a)</td><td>760.02 (n/a)</td><td>499.20 (n/a)</td><td>233.10 (n/a)</td><td>740.96 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>588.10 (n/a)</td><td>418.96 (n/a)</td><td>438.90 (n/a)</td><td>280.40 (n/a)</td><td>137.03 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>431.50 (n/a)</td><td>344.96 (n/a)</td><td>318.60 (n/a)</td><td>267.10 (n/a)</td><td>71.74 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>533.90 (n/a)</td><td>396.36 (n/a)</td><td>427.40 (n/a)</td><td>217.10 (n/a)</td><td>138.29 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>613.90 (n/a)</td><td>419.20 (n/a)</td><td>445.80 (n/a)</td><td>253.10 (n/a)</td><td>147.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.70 (n/a)</td><td>392.62 (n/a)</td><td>321.00 (n/a)</td><td>224.00 (n/a)</td><td>184.53 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>526.70 (n/a)</td><td>411.40 (n/a)</td><td>482.30 (n/a)</td><td>270.20 (n/a)</td><td>129.22 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>362.60 (n/a)</td><td>269.08 (n/a)</td><td>248.70 (n/a)</td><td>236.90 (n/a)</td><td>52.53 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>633.90 (n/a)</td><td>489.52 (n/a)</td><td>478.30 (n/a)</td><td>375.10 (n/a)</td><td>102.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.00 (n/a)</td><td>391.40 (n/a)</td><td>419.00 (n/a)</td><td>190.20 (n/a)</td><td>131.46 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.60 (n/a)</td><td>356.64 (n/a)</td><td>310.40 (n/a)</td><td>270.20 (n/a)</td><td>97.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>553.00 (n/a)</td><td>387.82 (n/a)</td><td>456.70 (n/a)</td><td>205.60 (n/a)</td><td>148.99 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1961.50 (n/a)</td><td>703.00 (n/a)</td><td>406.10 (n/a)</td><td>342.00 (n/a)</td><td>705.29 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>622.60 (n/a)</td><td>448.28 (n/a)</td><td>426.20 (n/a)</td><td>303.40 (n/a)</td><td>116.28 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2457.60 (n/a)</td><td>849.30 (n/a)</td><td>601.90 (n/a)</td><td>263.60 (n/a)</td><td>917.06 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>754.00 (n/a)</td><td>444.36 (n/a)</td><td>396.40 (n/a)</td><td>277.60 (n/a)</td><td>191.43 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>433.80 (n/a)</td><td>346.36 (n/a)</td><td>372.20 (n/a)</td><td>205.40 (n/a)</td><td>87.01 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>883.20 (n/a)</td><td>500.86 (n/a)</td><td>554.10 (n/a)</td><td>178.40 (n/a)</td><td>281.57 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>620.30 (n/a)</td><td>349.08 (n/a)</td><td>314.50 (n/a)</td><td>196.20 (n/a)</td><td>162.90 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>796.60 (n/a)</td><td>517.74 (n/a)</td><td>493.70 (n/a)</td><td>305.60 (n/a)</td><td>181.22 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>700.60 (n/a)</td><td>492.84 (n/a)</td><td>549.90 (n/a)</td><td>301.90 (n/a)</td><td>170.19 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1868.80 (n/a)</td><td>640.72 (n/a)</td><td>357.10 (n/a)</td><td>243.20 (n/a)</td><td>690.72 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>604.10 (n/a)</td><td>411.46 (n/a)</td><td>383.80 (n/a)</td><td>231.40 (n/a)</td><td>156.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.58 (+14.88%)</td><td>0.34 (+1.84%)</td><td>0.36 <b>(+27.43%)</b></td><td>0.15 (-16.12%)</td><td>0.18 <b>(+26.94%)</b></td><td>1440.50 (+19.22%)</td><td>839.04 (+9.24%)</td><td>611.00 <b>(-21.53%)</b></td><td>382.70 (-12.96%)</td><td>467.99 <b>(+47.11%)</b></td><td>24.66 (+14.88%)</td><td>14.44 (+1.84%)</td><td>15.45 <b>(+27.43%)</b></td><td>6.55 (-16.12%)</td><td>7.52 <b>(+26.94%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.50 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>1208.30 (n/a)</td><td>768.08 (n/a)</td><td>778.60 (n/a)</td><td>439.70 (n/a)</td><td>318.12 (n/a)</td><td>21.46 (n/a)</td><td>14.18 (n/a)</td><td>12.12 (n/a)</td><td>7.81 (n/a)</td><td>5.92 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.51 (-12.57%)</td><td>0.33 (-17.55%)</td><td>0.32 <b>(-36.20%)</b></td><td>0.19 (+11.71%)</td><td>0.12 <b>(-40.95%)</b></td><td>1154.00 (-10.48%)</td><td>749.76 (+2.20%)</td><td>695.90 <b>(+56.73%)</b></td><td>437.70 (+14.37%)</td><td>263.48 <b>(-40.31%)</b></td><td>21.56 (-12.57%)</td><td>13.89 (-17.55%)</td><td>13.56 <b>(-36.20%)</b></td><td>8.18 (+11.71%)</td><td>4.93 <b>(-40.95%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.58 (n/a)</td><td>0.39 (n/a)</td><td>0.50 (n/a)</td><td>0.17 (n/a)</td><td>0.20 (n/a)</td><td>1289.10 (n/a)</td><td>733.60 (n/a)</td><td>444.00 (n/a)</td><td>382.70 (n/a)</td><td>441.38 (n/a)</td><td>24.66 (n/a)</td><td>16.85 (n/a)</td><td>21.25 (n/a)</td><td>7.32 (n/a)</td><td>8.35 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.31 (+0.55%)</td><td>0.31 (+0.49%)</td><td>0.31 (+0.62%)</td><td>0.30 (-0.23%)</td><td>0.01 (+17.25%)</td><td>84336.20 (+0.23%)</td><td>81953.16 (-0.47%)</td><td>81876.40 (-0.61%)</td><td>79949.80 (-0.55%)</td><td>1650.96 (+17.02%)</td><td>214.88 (+0.55%)</td><td>209.70 (+0.49%)</td><td>209.83 (+0.62%)</td><td>203.71 (-0.23%)</td><td>4.20 (+17.25%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84145.90 (n/a)</td><td>82343.98 (n/a)</td><td>82382.30 (n/a)</td><td>80393.20 (n/a)</td><td>1410.87 (n/a)</td><td>213.70 (n/a)</td><td>208.68 (n/a)</td><td>208.54 (n/a)</td><td>204.17 (n/a)</td><td>3.58 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>1.03 (-0.10%)</td><td>0.99 (-0.87%)</td><td>1.01 (-0.61%)</td><td>0.91 (-3.28%)</td><td>0.05 <b>(+36.94%)</b></td><td>27593.40 (+3.39%)</td><td>25437.36 (+0.96%)</td><td>25010.30 (+0.61%)</td><td>24474.90 (+0.10%)</td><td>1236.19 <b>(+42.10%)</b></td><td>701.94 (-0.10%)</td><td>676.59 (-0.87%)</td><td>686.91 (-0.61%)</td><td>622.61 (-3.28%)</td><td>31.13 <b>(+36.94%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>1.03 (n/a)</td><td>1.00 (n/a)</td><td>1.01 (n/a)</td><td>0.94 (n/a)</td><td>0.03 (n/a)</td><td>26689.30 (n/a)</td><td>25194.92 (n/a)</td><td>24858.10 (n/a)</td><td>24451.10 (n/a)</td><td>869.94 (n/a)</td><td>702.62 (n/a)</td><td>682.51 (n/a)</td><td>691.12 (n/a)</td><td>643.70 (n/a)</td><td>22.73 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.82 (-0.75%)</td><td>0.81 (-0.79%)</td><td>0.81 (-0.68%)</td><td>0.80 (-0.78%)</td><td>0.01 (+3.14%)</td><td>94452.50 (+0.79%)</td><td>93117.04 (+0.80%)</td><td>92859.20 (+0.68%)</td><td>91876.90 (+0.76%)</td><td>1016.36 (+4.76%)</td><td>747.95 (-0.75%)</td><td>738.06 (-0.79%)</td><td>740.04 (-0.68%)</td><td>727.56 (-0.78%)</td><td>8.04 (+3.14%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.83 (n/a)</td><td>0.82 (n/a)</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.01 (n/a)</td><td>93714.80 (n/a)</td><td>92378.56 (n/a)</td><td>92231.40 (n/a)</td><td>91187.40 (n/a)</td><td>970.18 (n/a)</td><td>753.61 (n/a)</td><td>743.96 (n/a)</td><td>745.08 (n/a)</td><td>733.28 (n/a)</td><td>7.80 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.78 (+0.18%)</td><td>0.76 (-0.39%)</td><td>0.76 (-1.06%)</td><td>0.75 (+0.08%)</td><td>0.01 (-12.05%)</td><td>100254.80 (-0.08%)</td><td>98714.30 (+0.38%)</td><td>98820.00 (+1.07%)</td><td>96890.40 (-0.18%)</td><td>1274.62 (-12.22%)</td><td>709.25 (+0.18%)</td><td>696.24 (-0.39%)</td><td>695.40 (-1.06%)</td><td>685.45 (+0.08%)</td><td>9.02 (-12.05%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>100335.50 (n/a)</td><td>98338.06 (n/a)</td><td>97770.90 (n/a)</td><td>97061.50 (n/a)</td><td>1452.14 (n/a)</td><td>708.00 (n/a)</td><td>698.93 (n/a)</td><td>702.86 (n/a)</td><td>684.90 (n/a)</td><td>10.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.80 (-0.39%)</td><td>0.79 (-0.61%)</td><td>0.79 (-0.55%)</td><td>0.79 (-0.52%)</td><td>0.00 (+7.85%)</td><td>95785.00 (+0.53%)</td><td>95184.88 (+0.62%)</td><td>95297.40 (+0.55%)</td><td>94274.30 (+0.39%)</td><td>574.82 (+8.80%)</td><td>728.93 (-0.39%)</td><td>721.98 (-0.61%)</td><td>721.11 (-0.55%)</td><td>717.43 (-0.52%)</td><td>4.38 (+7.85%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.79 (n/a)</td><td>0.00 (n/a)</td><td>95282.50 (n/a)</td><td>94602.60 (n/a)</td><td>94773.80 (n/a)</td><td>93907.00 (n/a)</td><td>528.35 (n/a)</td><td>731.78 (n/a)</td><td>726.42 (n/a)</td><td>725.09 (n/a)</td><td>721.22 (n/a)</td><td>4.06 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>4.51 (-18.35%)</td><td>3.53 (+1.91%)</td><td>3.92 <b>(+29.30%)</b></td><td>2.23 (-8.11%)</td><td>0.96 <b>(-22.04%)</b></td><td>3994.60 (+8.82%)</td><td>2710.34 (-3.04%)</td><td>2272.70 <b>(-22.66%)</b></td><td>1975.40 <b>(+22.48%)</b></td><td>851.87 (+7.39%)</td><td>271.78 (-18.35%)</td><td>212.45 (+1.91%)</td><td>236.22 <b>(+29.30%)</b></td><td>134.40 (-8.11%)</td><td>57.91 <b>(-22.04%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.53 (n/a)</td><td>3.46 (n/a)</td><td>3.03 (n/a)</td><td>2.43 (n/a)</td><td>1.23 (n/a)</td><td>3670.80 (n/a)</td><td>2795.38 (n/a)</td><td>2938.70 (n/a)</td><td>1612.80 (n/a)</td><td>793.26 (n/a)</td><td>332.88 (n/a)</td><td>208.46 (n/a)</td><td>182.69 (n/a)</td><td>146.25 (n/a)</td><td>74.28 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>4.72 (-7.36%)</td><td>3.26 (-3.45%)</td><td>2.63 (-6.94%)</td><td>2.24 (+0.53%)</td><td>1.21 (-9.43%)</td><td>3979.00 (-0.53%)</td><td>3030.66 (+1.98%)</td><td>3390.70 (+7.46%)</td><td>1888.70 (+7.95%)</td><td>1009.84 (-5.51%)</td><td>284.25 (-7.36%)</td><td>196.43 (-3.45%)</td><td>158.34 (-6.94%)</td><td>134.92 (+0.53%)</td><td>72.76 (-9.43%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.09 (n/a)</td><td>3.38 (n/a)</td><td>2.82 (n/a)</td><td>2.23 (n/a)</td><td>1.33 (n/a)</td><td>4000.00 (n/a)</td><td>2971.96 (n/a)</td><td>3155.40 (n/a)</td><td>1749.60 (n/a)</td><td>1068.69 (n/a)</td><td>306.85 (n/a)</td><td>203.45 (n/a)</td><td>170.15 (n/a)</td><td>134.22 (n/a)</td><td>80.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>5.45 (-9.41%)</td><td>4.37 <b>(+36.64%)</b></td><td>4.93 <b>(+100.18%)</b></td><td>2.18 (+1.47%)</td><td>1.33 (-18.46%)</td><td>4086.70 (-1.45%)</td><td>2287.42 <b>(-29.31%)</b></td><td>1809.00 <b>(-50.05%)</b></td><td>1634.90 (+10.38%)</td><td>1029.38 (-8.71%)</td><td>328.37 (-9.41%)</td><td>263.05 <b>(+36.64%)</b></td><td>296.77 <b>(+100.18%)</b></td><td>131.37 (+1.47%)</td><td>80.30 (-18.46%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>6.02 (n/a)</td><td>3.20 (n/a)</td><td>2.46 (n/a)</td><td>2.15 (n/a)</td><td>1.63 (n/a)</td><td>4146.90 (n/a)</td><td>3235.64 (n/a)</td><td>3621.40 (n/a)</td><td>1481.10 (n/a)</td><td>1127.64 (n/a)</td><td>362.49 (n/a)</td><td>192.51 (n/a)</td><td>148.25 (n/a)</td><td>129.46 (n/a)</td><td>98.48 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>6.82 (+6.53%)</td><td>5.85 (+4.08%)</td><td>6.04 (+5.31%)</td><td>4.91 (-1.38%)</td><td>0.78 <b>(+23.79%)</b></td><td>7102.10 (+1.39%)</td><td>6046.46 (-3.50%)</td><td>5768.40 (-5.04%)</td><td>5113.90 (-6.13%)</td><td>820.29 (+16.32%)</td><td>419.93 (+6.53%)</td><td>360.35 (+4.08%)</td><td>372.29 (+5.31%)</td><td>302.37 (-1.38%)</td><td>47.97 <b>(+23.79%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>6.40 (n/a)</td><td>5.62 (n/a)</td><td>5.74 (n/a)</td><td>4.98 (n/a)</td><td>0.63 (n/a)</td><td>7004.40 (n/a)</td><td>6265.72 (n/a)</td><td>6074.50 (n/a)</td><td>5447.90 (n/a)</td><td>705.20 (n/a)</td><td>394.18 (n/a)</td><td>346.22 (n/a)</td><td>353.52 (n/a)</td><td>306.59 (n/a)</td><td>38.75 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>5.35 (+15.15%)</td><td>4.34 (+0.06%)</td><td>4.42 (+2.90%)</td><td>3.66 (-5.39%)</td><td>0.71 <b>(+128.89%)</b></td><td>9513.80 (+5.69%)</td><td>8204.28 (+1.60%)</td><td>7879.20 (-2.82%)</td><td>6515.50 (-13.16%)</td><td>1295.97 <b>(+117.19%)</b></td><td>329.59 (+15.15%)</td><td>267.21 (+0.06%)</td><td>272.55 (+2.90%)</td><td>225.72 (-5.39%)</td><td>43.50 <b>(+128.89%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>4.65 (n/a)</td><td>4.34 (n/a)</td><td>4.30 (n/a)</td><td>3.87 (n/a)</td><td>0.31 (n/a)</td><td>9001.40 (n/a)</td><td>8075.18 (n/a)</td><td>8107.50 (n/a)</td><td>7502.50 (n/a)</td><td>596.70 (n/a)</td><td>286.24 (n/a)</td><td>267.06 (n/a)</td><td>264.87 (n/a)</td><td>238.57 (n/a)</td><td>19.01 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>6.74 <b>(+20.58%)</b></td><td>4.97 (-4.19%)</td><td>4.52 (-9.59%)</td><td>4.42 (-10.54%)</td><td>0.99 <b>(+232.69%)</b></td><td>7886.80 (+11.78%)</td><td>7196.34 (+6.81%)</td><td>7711.60 (+10.61%)</td><td>5176.00 (-17.07%)</td><td>1143.80 <b>(+202.52%)</b></td><td>414.89 <b>(+20.58%)</b></td><td>306.18 (-4.19%)</td><td>278.48 (-9.59%)</td><td>272.29 (-10.54%)</td><td>61.14 <b>(+232.70%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.59 (n/a)</td><td>5.19 (n/a)</td><td>5.00 (n/a)</td><td>4.94 (n/a)</td><td>0.30 (n/a)</td><td>7055.80 (n/a)</td><td>6737.64 (n/a)</td><td>6971.80 (n/a)</td><td>6241.20 (n/a)</td><td>378.09 (n/a)</td><td>344.08 (n/a)</td><td>319.55 (n/a)</td><td>308.02 (n/a)</td><td>304.36 (n/a)</td><td>18.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.79 (+0.72%)</td><td>0.76 (-0.76%)</td><td>0.75 (-1.40%)</td><td>0.73 (-1.88%)</td><td>0.02 <b>(+45.10%)</b></td><td>103513.60 (+1.91%)</td><td>99568.74 (+0.80%)</td><td>100129.70 (+1.42%)</td><td>95536.60 (-0.71%)</td><td>2908.27 <b>(+46.60%)</b></td><td>719.30 (+0.72%)</td><td>690.64 (-0.76%)</td><td>686.30 (-1.40%)</td><td>663.87 (-1.88%)</td><td>20.23 <b>(+45.10%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>101569.90 (n/a)</td><td>98776.52 (n/a)</td><td>98723.20 (n/a)</td><td>96221.40 (n/a)</td><td>1983.76 (n/a)</td><td>714.18 (n/a)</td><td>695.93 (n/a)</td><td>696.08 (n/a)</td><td>676.57 (n/a)</td><td>13.94 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.77 (-0.81%)</td><td>0.76 (-0.76%)</td><td>0.77 (-0.38%)</td><td>0.74 (-0.60%)</td><td>0.01 (-8.18%)</td><td>102416.60 (+0.60%)</td><td>99432.80 (+0.76%)</td><td>98667.40 (+0.38%)</td><td>97596.60 (+0.82%)</td><td>1978.67 (-6.63%)</td><td>704.12 (-0.81%)</td><td>691.33 (-0.76%)</td><td>696.48 (-0.38%)</td><td>670.98 (-0.60%)</td><td>13.60 (-8.18%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>101806.00 (n/a)</td><td>98683.04 (n/a)</td><td>98295.60 (n/a)</td><td>96807.00 (n/a)</td><td>2119.09 (n/a)</td><td>709.86 (n/a)</td><td>696.62 (n/a)</td><td>699.11 (n/a)</td><td>675.00 (n/a)</td><td>14.81 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.81 (+0.04%)</td><td>0.81 (+0.45%)</td><td>0.80 (-0.13%)</td><td>0.80 (+1.44%)</td><td>0.00 <b>(-68.87%)</b></td><td>93981.80 (-1.42%)</td><td>93736.52 (-0.46%)</td><td>93902.60 (+0.13%)</td><td>93236.50 (-0.04%)</td><td>311.72 <b>(-69.33%)</b></td><td>737.04 (+0.04%)</td><td>733.12 (+0.45%)</td><td>731.82 (-0.13%)</td><td>731.20 (+1.44%)</td><td>2.44 <b>(-68.87%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.81 (n/a)</td><td>0.80 (n/a)</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.01 (n/a)</td><td>95338.40 (n/a)</td><td>94169.96 (n/a)</td><td>93778.60 (n/a)</td><td>93271.20 (n/a)</td><td>1016.29 (n/a)</td><td>736.77 (n/a)</td><td>729.81 (n/a)</td><td>732.78 (n/a)</td><td>720.80 (n/a)</td><td>7.85 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>3.43 (-0.94%)</td><td>1.83 <b>(-31.05%)</b></td><td>1.59 <b>(-44.76%)</b></td><td>1.08 <b>(-34.86%)</b></td><td>0.94 <b>(+24.95%)</b></td><td>7472.90 <b>(+53.51%)</b></td><td>5165.04 <b>(+57.66%)</b></td><td>5057.50 <b>(+81.02%)</b></td><td>2348.60 (+0.95%)</td><td>1953.81 <b>(+84.41%)</b></td><td>900.07 (-0.94%)</td><td>479.49 <b>(-31.05%)</b></td><td>417.98 <b>(-44.76%)</b></td><td>282.88 <b>(-34.86%)</b></td><td>246.02 <b>(+24.95%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>3.46 (n/a)</td><td>2.65 (n/a)</td><td>2.89 (n/a)</td><td>1.66 (n/a)</td><td>0.75 (n/a)</td><td>4868.10 (n/a)</td><td>3276.08 (n/a)</td><td>2793.90 (n/a)</td><td>2326.50 (n/a)</td><td>1059.50 (n/a)</td><td>908.62 (n/a)</td><td>695.38 (n/a)</td><td>756.62 (n/a)</td><td>434.24 (n/a)</td><td>196.89 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.23 <b>(-24.13%)</b></td><td>0.20 (-18.44%)</td><td>0.20 <b>(-27.01%)</b></td><td>0.18 (+1.19%)</td><td>0.02 <b>(-65.81%)</b></td><td>6968.00 (-1.18%)</td><td>6364.20 (+16.97%)</td><td>6273.70 <b>(+37.02%)</b></td><td>5429.00 <b>(+31.80%)</b></td><td>633.52 <b>(-56.94%)</b></td><td>12.36 <b>(-24.13%)</b></td><td>10.63 (-18.44%)</td><td>10.70 <b>(-27.01%)</b></td><td>9.63 (+1.19%)</td><td>1.11 <b>(-65.81%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>7050.90 (n/a)</td><td>5440.76 (n/a)</td><td>4578.80 (n/a)</td><td>4119.00 (n/a)</td><td>1471.28 (n/a)</td><td>16.29 (n/a)</td><td>13.04 (n/a)</td><td>14.66 (n/a)</td><td>9.52 (n/a)</td><td>3.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>3.77 (n/a)</td><td>3.61 (n/a)</td><td>3.71 (n/a)</td><td>3.39 (n/a)</td><td>0.17 (n/a)</td><td>3.77 (n/a)</td><td>3.61 (n/a)</td><td>3.71 (n/a)</td><td>3.39 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>7.29 (-1.05%)</td><td>6.68 (-2.98%)</td><td>7.02 (+0.51%)</td><td>5.65 (-6.99%)</td><td>0.71 <b>(+46.40%)</b></td><td>7.28 (-1.05%)</td><td>6.67 (-2.98%)</td><td>7.02 (+0.51%)</td><td>5.65 (-6.99%)</td><td>0.71 <b>(+46.40%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>7.36 (n/a)</td><td>6.88 (n/a)</td><td>6.99 (n/a)</td><td>6.08 (n/a)</td><td>0.48 (n/a)</td><td>7.36 (n/a)</td><td>6.88 (n/a)</td><td>6.98 (n/a)</td><td>6.07 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>12.89 <b>(+37.34%)</b></td><td>9.90 (+16.32%)</td><td>9.44 (+13.42%)</td><td>8.18 (-0.20%)</td><td>1.76 <b>(+258.99%)</b></td><td>12.88 <b>(+37.34%)</b></td><td>9.90 (+16.32%)</td><td>9.44 (+13.42%)</td><td>8.18 (-0.20%)</td><td>1.76 <b>(+258.99%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>9.38 (n/a)</td><td>8.51 (n/a)</td><td>8.33 (n/a)</td><td>8.20 (n/a)</td><td>0.49 (n/a)</td><td>9.38 (n/a)</td><td>8.51 (n/a)</td><td>8.32 (n/a)</td><td>8.20 (n/a)</td><td>0.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>3.83 (n/a)</td><td>3.58 (n/a)</td><td>3.59 (n/a)</td><td>3.36 (n/a)</td><td>0.17 (n/a)</td><td>3.83 (n/a)</td><td>3.58 (n/a)</td><td>3.59 (n/a)</td><td>3.35 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>6.54 (-7.66%)</td><td>6.12 (-2.06%)</td><td>6.00 (-8.62%)</td><td>5.67 <b>(+23.34%)</b></td><td>0.35 <b>(-63.74%)</b></td><td>6.54 (-7.66%)</td><td>6.12 (-2.06%)</td><td>6.00 (-8.62%)</td><td>5.66 <b>(+23.34%)</b></td><td>0.35 <b>(-63.74%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>7.08 (n/a)</td><td>6.25 (n/a)</td><td>6.57 (n/a)</td><td>4.59 (n/a)</td><td>0.97 (n/a)</td><td>7.08 (n/a)</td><td>6.25 (n/a)</td><td>6.57 (n/a)</td><td>4.59 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>13.97 (+7.39%)</td><td>9.22 (-2.66%)</td><td>8.05 (-4.59%)</td><td>7.77 (+1.45%)</td><td>2.67 <b>(+22.42%)</b></td><td>13.96 (+7.39%)</td><td>9.22 (-2.66%)</td><td>8.04 (-4.59%)</td><td>7.77 (+1.45%)</td><td>2.67 <b>(+22.42%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>13.01 (n/a)</td><td>9.47 (n/a)</td><td>8.43 (n/a)</td><td>7.66 (n/a)</td><td>2.18 (n/a)</td><td>13.00 (n/a)</td><td>9.47 (n/a)</td><td>8.43 (n/a)</td><td>7.65 (n/a)</td><td>2.18 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>3.08 (-4.71%)</td><td>2.90 <b>(+43.58%)</b></td><td>2.86 <b>(+63.63%)</b></td><td>2.79 <b>(+165.45%)</b></td><td>0.11 <b>(-86.75%)</b></td><td>3.07 (-4.71%)</td><td>2.89 <b>(+43.58%)</b></td><td>2.85 <b>(+63.63%)</b></td><td>2.79 <b>(+165.45%)</b></td><td>0.11 <b>(-86.75%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>3.23 (n/a)</td><td>2.02 (n/a)</td><td>1.75 (n/a)</td><td>1.05 (n/a)</td><td>0.85 (n/a)</td><td>3.22 (n/a)</td><td>2.01 (n/a)</td><td>1.74 (n/a)</td><td>1.05 (n/a)</td><td>0.85 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.51 (-11.46%)</td><td>0.36 (-6.87%)</td><td>0.40 (+5.78%)</td><td>0.08 (-2.00%)</td><td>0.17 (-15.33%)</td><td>0.50 (-11.46%)</td><td>0.35 (-6.87%)</td><td>0.40 (+5.78%)</td><td>0.07 (-2.00%)</td><td>0.16 (-15.33%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.58 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.08 (n/a)</td><td>0.20 (n/a)</td><td>0.57 (n/a)</td><td>0.38 (n/a)</td><td>0.38 (n/a)</td><td>0.08 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.68 (+1.42%)</td><td>0.54 (-3.49%)</td><td>0.66 (+3.07%)</td><td>0.34 (-7.26%)</td><td>0.18 <b>(+29.62%)</b></td><td>0.67 (+1.42%)</td><td>0.53 (-3.49%)</td><td>0.65 (+3.07%)</td><td>0.34 (-7.26%)</td><td>0.17 <b>(+29.62%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.67 (n/a)</td><td>0.56 (n/a)</td><td>0.64 (n/a)</td><td>0.37 (n/a)</td><td>0.14 (n/a)</td><td>0.66 (n/a)</td><td>0.55 (n/a)</td><td>0.63 (n/a)</td><td>0.37 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>2.40 (-13.16%)</td><td>1.28 <b>(+20.55%)</b></td><td>1.44 <b>(+212.30%)</b></td><td>0.45 (+2.78%)</td><td>0.84 (-16.77%)</td><td>2.36 (-13.16%)</td><td>1.26 <b>(+20.55%)</b></td><td>1.41 <b>(+212.30%)</b></td><td>0.44 (+2.78%)</td><td>0.82 (-16.77%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>2.76 (n/a)</td><td>1.06 (n/a)</td><td>0.46 (n/a)</td><td>0.43 (n/a)</td><td>1.01 (n/a)</td><td>2.72 (n/a)</td><td>1.04 (n/a)</td><td>0.45 (n/a)</td><td>0.43 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>508.50 (n/a)</td><td>376.84 (n/a)</td><td>364.90 (n/a)</td><td>209.30 (n/a)</td><td>124.66 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>534.50 (n/a)</td><td>394.72 (n/a)</td><td>428.60 (n/a)</td><td>256.80 (n/a)</td><td>113.86 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>669.50 (n/a)</td><td>435.18 (n/a)</td><td>418.70 (n/a)</td><td>257.10 (n/a)</td><td>161.72 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.20 (n/a)</td><td>458.62 (n/a)</td><td>502.50 (n/a)</td><td>210.30 (n/a)</td><td>144.39 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>458.60 (n/a)</td><td>363.26 (n/a)</td><td>442.10 (n/a)</td><td>218.30 (n/a)</td><td>116.90 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>704.90 (n/a)</td><td>492.56 (n/a)</td><td>531.30 (n/a)</td><td>282.10 (n/a)</td><td>186.45 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>660.90 (n/a)</td><td>381.24 (n/a)</td><td>252.10 (n/a)</td><td>209.90 (n/a)</td><td>205.27 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1900.90 (n/a)</td><td>707.74 (n/a)</td><td>517.50 (n/a)</td><td>256.70 (n/a)</td><td>684.69 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.40 (n/a)</td><td>344.32 (n/a)</td><td>289.90 (n/a)</td><td>281.90 (n/a)</td><td>120.98 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>473.50 (n/a)</td><td>384.76 (n/a)</td><td>356.60 (n/a)</td><td>276.90 (n/a)</td><td>83.00 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>563.40 (n/a)</td><td>354.96 (n/a)</td><td>275.50 (n/a)</td><td>247.80 (n/a)</td><td>136.20 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>475.10 (n/a)</td><td>362.54 (n/a)</td><td>360.20 (n/a)</td><td>204.30 (n/a)</td><td>106.19 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>618.70 (n/a)</td><td>420.94 (n/a)</td><td>420.60 (n/a)</td><td>244.60 (n/a)</td><td>149.01 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>2102.10 (n/a)</td><td>763.20 (n/a)</td><td>531.80 (n/a)</td><td>179.40 (n/a)</td><td>762.62 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>612.70 (n/a)</td><td>485.66 (n/a)</td><td>528.00 (n/a)</td><td>282.10 (n/a)</td><td>132.50 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>522.40 (n/a)</td><td>375.72 (n/a)</td><td>367.20 (n/a)</td><td>243.40 (n/a)</td><td>128.30 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>544.60 (n/a)</td><td>396.12 (n/a)</td><td>454.40 (n/a)</td><td>196.10 (n/a)</td><td>148.73 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>554.90 (n/a)</td><td>496.10 (n/a)</td><td>496.40 (n/a)</td><td>413.80 (n/a)</td><td>52.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>464.30 (n/a)</td><td>331.18 (n/a)</td><td>321.50 (n/a)</td><td>222.70 (n/a)</td><td>87.98 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>534.50 (n/a)</td><td>353.84 (n/a)</td><td>328.30 (n/a)</td><td>246.10 (n/a)</td><td>112.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>677.40 (n/a)</td><td>474.58 (n/a)</td><td>501.20 (n/a)</td><td>275.50 (n/a)</td><td>190.83 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>631.00 (n/a)</td><td>481.76 (n/a)</td><td>506.70 (n/a)</td><td>309.90 (n/a)</td><td>122.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>519.60 (n/a)</td><td>453.76 (n/a)</td><td>498.80 (n/a)</td><td>287.10 (n/a)</td><td>96.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>739.50 (n/a)</td><td>519.50 (n/a)</td><td>493.20 (n/a)</td><td>297.20 (n/a)</td><td>173.30 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-6.69%)</td><td>0.01 <b>(-20.16%)</b></td><td>0.01 <b>(-42.75%)</b></td><td>0.01 (+7.76%)</td><td>0.00 <b>(-26.96%)</b></td><td>500.80 (-7.19%)</td><td>430.06 (+17.12%)</td><td>493.00 <b>(+74.64%)</b></td><td>248.50 (+7.20%)</td><td>107.77 <b>(-31.42%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>539.60 (n/a)</td><td>367.20 (n/a)</td><td>282.30 (n/a)</td><td>231.80 (n/a)</td><td>157.15 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-11.28%)</td><td>0.01 (-8.25%)</td><td>0.01 <b>(-34.47%)</b></td><td>0.01 <b>(+41.38%)</b></td><td>0.00 <b>(-30.28%)</b></td><td>517.80 <b>(-29.26%)</b></td><td>392.74 (-2.94%)</td><td>415.20 <b>(+52.59%)</b></td><td>255.70 (+12.69%)</td><td>119.85 <b>(-44.79%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>732.00 (n/a)</td><td>404.62 (n/a)</td><td>272.10 (n/a)</td><td>226.90 (n/a)</td><td>217.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (-9.65%)</td><td>0.01 (+1.85%)</td><td>0.01 (-12.02%)</td><td>0.01 <b>(+315.95%)</b></td><td>0.00 <b>(-39.68%)</b></td><td>590.80 <b>(-75.96%)</b></td><td>413.24 <b>(-45.41%)</b></td><td>434.90 (+13.67%)</td><td>287.10 (+10.68%)</td><td>127.24 <b>(-86.64%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2457.40 (n/a)</td><td>756.96 (n/a)</td><td>382.60 (n/a)</td><td>259.40 (n/a)</td><td>952.23 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-7.34%)</td><td>0.01 (-8.72%)</td><td>0.01 (-8.82%)</td><td>0.01 (-7.91%)</td><td>0.00 (-15.09%)</td><td>591.00 (+8.58%)</td><td>432.22 (+7.74%)</td><td>501.80 (+9.68%)</td><td>263.30 (+7.95%)</td><td>141.91 (+0.51%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>544.30 (n/a)</td><td>401.18 (n/a)</td><td>457.50 (n/a)</td><td>243.90 (n/a)</td><td>141.19 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 <b>(+66.13%)</b></td><td>0.01 <b>(+22.83%)</b></td><td>0.01 (+18.01%)</td><td>0.01 (-10.04%)</td><td>0.01 <b>(+124.63%)</b></td><td>640.40 (+11.16%)</td><td>425.10 (-6.29%)</td><td>430.00 (-15.25%)</td><td>170.90 <b>(-39.80%)</b></td><td>186.19 <b>(+45.44%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>576.10 (n/a)</td><td>453.62 (n/a)</td><td>507.40 (n/a)</td><td>283.90 (n/a)</td><td>128.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 <b>(+25.70%)</b></td><td>0.01 (-0.83%)</td><td>0.01 (-3.58%)</td><td>0.01 (-8.22%)</td><td>0.00 <b>(+71.92%)</b></td><td>589.50 (+8.96%)</td><td>466.24 (+5.22%)</td><td>466.00 (+3.72%)</td><td>287.40 <b>(-20.45%)</b></td><td>125.94 <b>(+56.37%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>541.00 (n/a)</td><td>443.12 (n/a)</td><td>449.30 (n/a)</td><td>361.30 (n/a)</td><td>80.54 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 <b>(-24.93%)</b></td><td>0.01 <b>(-38.50%)</b></td><td>0.02 (-12.77%)</td><td>0.00 <b>(-80.79%)</b></td><td>0.01 (+10.53%)</td><td>2513.80 <b>(+420.67%)</b></td><td>949.64 <b>(+145.07%)</b></td><td>505.70 (+14.65%)</td><td>323.50 <b>(+33.24%)</b></td><td>900.47 <b>(+707.97%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>482.80 (n/a)</td><td>387.50 (n/a)</td><td>441.10 (n/a)</td><td>242.80 (n/a)</td><td>111.45 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (+8.65%)</td><td>0.03 (+3.40%)</td><td>0.03 (+19.73%)</td><td>0.01 <b>(-27.79%)</b></td><td>0.01 <b>(+74.49%)</b></td><td>670.50 <b>(+38.48%)</b></td><td>391.18 (+9.75%)</td><td>264.30 (-16.49%)</td><td>244.30 (-7.98%)</td><td>196.68 <b>(+110.07%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>484.20 (n/a)</td><td>356.44 (n/a)</td><td>316.50 (n/a)</td><td>265.50 (n/a)</td><td>93.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (-7.73%)</td><td>0.02 (-16.87%)</td><td>0.02 <b>(-31.67%)</b></td><td>0.02 (-0.54%)</td><td>0.00 <b>(-26.68%)</b></td><td>531.50 (+0.55%)</td><td>427.92 (+16.57%)</td><td>427.90 <b>(+46.34%)</b></td><td>290.50 (+8.36%)</td><td>91.15 <b>(-21.99%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.60 (n/a)</td><td>367.08 (n/a)</td><td>292.40 (n/a)</td><td>268.10 (n/a)</td><td>116.84 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (-10.14%)</td><td>0.03 (-0.53%)</td><td>0.03 (+0.58%)</td><td>0.01 (-4.32%)</td><td>0.01 (-19.44%)</td><td>617.60 (+4.52%)</td><td>347.98 (-5.16%)</td><td>265.50 (-0.56%)</td><td>217.40 (+11.32%)</td><td>166.96 (-12.13%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>590.90 (n/a)</td><td>366.92 (n/a)</td><td>267.00 (n/a)</td><td>195.30 (n/a)</td><td>190.00 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 <b>(-29.49%)</b></td><td>0.02 <b>(-29.35%)</b></td><td>0.02 <b>(-48.26%)</b></td><td>0.02 (-1.92%)</td><td>0.01 <b>(-39.79%)</b></td><td>513.90 (+1.96%)</td><td>398.16 <b>(+31.53%)</b></td><td>466.10 <b>(+93.32%)</b></td><td>242.20 <b>(+41.80%)</b></td><td>122.95 (-13.42%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.00 (n/a)</td><td>302.72 (n/a)</td><td>241.10 (n/a)</td><td>170.80 (n/a)</td><td>142.00 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (+2.09%)</td><td>0.02 (+3.88%)</td><td>0.03 <b>(+74.25%)</b></td><td>0.01 <b>(-49.19%)</b></td><td>0.01 <b>(+41.01%)</b></td><td>1019.60 <b>(+96.83%)</b></td><td>468.88 (+18.40%)</td><td>265.00 <b>(-42.60%)</b></td><td>247.30 (-2.06%)</td><td>332.43 <b>(+164.88%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.00 (n/a)</td><td>396.02 (n/a)</td><td>461.70 (n/a)</td><td>252.50 (n/a)</td><td>125.50 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 <b>(+28.56%)</b></td><td>0.03 (+14.28%)</td><td>0.03 (+11.82%)</td><td>0.02 <b>(+42.10%)</b></td><td>0.01 <b>(+21.11%)</b></td><td>497.90 <b>(-29.63%)</b></td><td>353.62 (-13.89%)</td><td>301.70 (-10.55%)</td><td>230.00 <b>(-22.22%)</b></td><td>118.64 <b>(-31.23%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>707.50 (n/a)</td><td>410.68 (n/a)</td><td>337.30 (n/a)</td><td>295.70 (n/a)</td><td>172.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (+11.47%)</td><td>0.02 (-3.84%)</td><td>0.02 (-2.16%)</td><td>0.01 <b>(-54.45%)</b></td><td>0.01 <b>(+74.04%)</b></td><td>1365.40 <b>(+119.55%)</b></td><td>631.38 <b>(+28.04%)</b></td><td>501.20 (+2.22%)</td><td>294.50 (-10.27%)</td><td>422.26 <b>(+288.05%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>621.90 (n/a)</td><td>493.12 (n/a)</td><td>490.30 (n/a)</td><td>328.20 (n/a)</td><td>108.81 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (-15.80%)</td><td>0.05 (+0.36%)</td><td>0.04 <b>(+26.82%)</b></td><td>0.03 (+10.18%)</td><td>0.01 <b>(-41.95%)</b></td><td>484.50 (-9.24%)</td><td>376.70 (-6.99%)</td><td>384.10 <b>(-21.15%)</b></td><td>284.00 (+18.78%)</td><td>83.38 <b>(-38.68%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>533.80 (n/a)</td><td>405.00 (n/a)</td><td>487.10 (n/a)</td><td>239.10 (n/a)</td><td>135.98 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (+7.56%)</td><td>0.04 (-10.43%)</td><td>0.03 (-18.22%)</td><td>0.02 <b>(-43.36%)</b></td><td>0.02 <b>(+91.40%)</b></td><td>810.90 <b>(+76.59%)</b></td><td>490.00 <b>(+31.63%)</b></td><td>495.90 <b>(+22.29%)</b></td><td>249.90 (-7.03%)</td><td>237.06 <b>(+197.09%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>459.20 (n/a)</td><td>372.26 (n/a)</td><td>405.50 (n/a)</td><td>268.80 (n/a)</td><td>79.80 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (+3.76%)</td><td>0.04 (-11.20%)</td><td>0.04 <b>(-25.61%)</b></td><td>0.03 (+0.11%)</td><td>0.02 (+0.66%)</td><td>540.50 (-0.11%)</td><td>407.38 (+12.11%)</td><td>441.70 <b>(+34.42%)</b></td><td>237.40 (-3.61%)</td><td>116.47 (-5.31%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>541.10 (n/a)</td><td>363.36 (n/a)</td><td>328.60 (n/a)</td><td>246.30 (n/a)</td><td>123.00 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 <b>(-25.24%)</b></td><td>0.04 (-18.72%)</td><td>0.04 (-10.16%)</td><td>0.03 (-7.46%)</td><td>0.01 <b>(-52.54%)</b></td><td>584.90 (+8.05%)</td><td>456.14 (+16.62%)</td><td>467.60 (+11.31%)</td><td>350.00 <b>(+33.74%)</b></td><td>87.38 <b>(-27.75%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>541.30 (n/a)</td><td>391.12 (n/a)</td><td>420.10 (n/a)</td><td>261.70 (n/a)</td><td>120.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (+4.07%)</td><td>0.04 (-18.92%)</td><td>0.03 <b>(-41.93%)</b></td><td>0.03 (+15.57%)</td><td>0.02 (+1.87%)</td><td>571.40 (-13.46%)</td><td>428.52 <b>(+20.66%)</b></td><td>493.90 <b>(+72.21%)</b></td><td>242.40 (-3.92%)</td><td>138.48 (-19.58%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>660.30 (n/a)</td><td>355.14 (n/a)</td><td>286.80 (n/a)</td><td>252.30 (n/a)</td><td>172.19 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (-8.17%)</td><td>0.03 <b>(-24.28%)</b></td><td>0.03 <b>(-25.89%)</b></td><td>0.01 <b>(-78.03%)</b></td><td>0.01 <b>(+74.87%)</b></td><td>2532.70 <b>(+355.11%)</b></td><td>885.54 <b>(+103.39%)</b></td><td>517.90 <b>(+34.90%)</b></td><td>373.90 (+8.91%)</td><td>923.08 <b>(+875.04%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>556.50 (n/a)</td><td>435.38 (n/a)</td><td>383.90 (n/a)</td><td>343.30 (n/a)</td><td>94.67 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 <b>(-24.42%)</b></td><td>0.08 (-19.81%)</td><td>0.07 <b>(-32.17%)</b></td><td>0.06 (+16.67%)</td><td>0.02 <b>(-44.85%)</b></td><td>563.10 (-14.29%)</td><td>439.80 (+13.41%)</td><td>469.00 <b>(+47.44%)</b></td><td>287.30 <b>(+32.27%)</b></td><td>102.66 <b>(-41.13%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>657.00 (n/a)</td><td>387.80 (n/a)</td><td>318.10 (n/a)</td><td>217.20 (n/a)</td><td>174.37 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 <b>(-33.87%)</b></td><td>0.06 <b>(-27.26%)</b></td><td>0.06 (-17.24%)</td><td>0.03 <b>(-47.88%)</b></td><td>0.02 <b>(-25.09%)</b></td><td>1000.90 <b>(+91.85%)</b></td><td>601.08 <b>(+42.73%)</b></td><td>554.20 <b>(+20.82%)</b></td><td>409.40 <b>(+51.18%)</b></td><td>232.90 <b>(+133.34%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>521.70 (n/a)</td><td>421.14 (n/a)</td><td>458.70 (n/a)</td><td>270.80 (n/a)</td><td>99.81 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (-13.52%)</td><td>0.09 (+19.73%)</td><td>0.08 <b>(+29.98%)</b></td><td>0.07 <b>(+21.01%)</b></td><td>0.02 <b>(-34.40%)</b></td><td>480.40 (-17.36%)</td><td>387.80 <b>(-22.29%)</b></td><td>430.60 <b>(-23.07%)</b></td><td>267.90 (+15.62%)</td><td>96.49 <b>(-35.55%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>581.30 (n/a)</td><td>499.04 (n/a)</td><td>559.70 (n/a)</td><td>231.70 (n/a)</td><td>149.72 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (-7.62%)</td><td>0.07 <b>(-31.16%)</b></td><td>0.07 <b>(-38.37%)</b></td><td>0.02 <b>(-75.30%)</b></td><td>0.04 <b>(+41.44%)</b></td><td>2082.70 <b>(+304.96%)</b></td><td>742.12 <b>(+121.91%)</b></td><td>476.40 <b>(+62.26%)</b></td><td>251.00 (+8.24%)</td><td>755.84 <b>(+589.62%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>514.30 (n/a)</td><td>334.42 (n/a)</td><td>293.60 (n/a)</td><td>231.90 (n/a)</td><td>109.60 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 <b>(+32.63%)</b></td><td>0.08 (+8.48%)</td><td>0.08 (+10.36%)</td><td>0.06 (-6.39%)</td><td>0.03 <b>(+87.80%)</b></td><td>587.30 (+6.84%)</td><td>431.16 (-1.18%)</td><td>424.40 (-9.39%)</td><td>244.30 <b>(-24.60%)</b></td><td>147.21 <b>(+59.39%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>549.70 (n/a)</td><td>436.32 (n/a)</td><td>468.40 (n/a)</td><td>324.00 (n/a)</td><td>92.35 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (+4.48%)</td><td>0.01 (+6.85%)</td><td>0.01 <b>(+21.39%)</b></td><td>0.01 (-8.46%)</td><td>0.00 (+18.40%)</td><td>478.40 (+9.25%)</td><td>327.54 (-4.31%)</td><td>275.70 (-17.63%)</td><td>234.40 (-4.29%)</td><td>105.45 <b>(+21.41%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>437.90 (n/a)</td><td>342.28 (n/a)</td><td>334.70 (n/a)</td><td>244.90 (n/a)</td><td>86.85 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 <b>(+24.22%)</b></td><td>0.02 <b>(+43.72%)</b></td><td>0.02 <b>(+47.18%)</b></td><td>0.01 <b>(+91.04%)</b></td><td>0.00 <b>(-42.25%)</b></td><td>281.60 <b>(-47.66%)</b></td><td>253.12 <b>(-33.85%)</b></td><td>251.30 <b>(-32.04%)</b></td><td>217.60 (-19.50%)</td><td>26.20 <b>(-75.36%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>538.00 (n/a)</td><td>382.66 (n/a)</td><td>369.80 (n/a)</td><td>270.30 (n/a)</td><td>106.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 <b>(+44.57%)</b></td><td>0.01 <b>(+68.77%)</b></td><td>0.01 <b>(+37.30%)</b></td><td>0.01 <b>(+404.14%)</b></td><td>0.00 (-2.60%)</td><td>510.80 <b>(-80.16%)</b></td><td>379.16 <b>(-59.33%)</b></td><td>404.40 <b>(-27.17%)</b></td><td>262.00 <b>(-30.83%)</b></td><td>102.85 <b>(-88.85%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>2574.90 (n/a)</td><td>932.36 (n/a)</td><td>555.30 (n/a)</td><td>378.80 (n/a)</td><td>922.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (+13.00%)</td><td>0.01 (-3.49%)</td><td>0.01 (-6.99%)</td><td>0.01 (-0.54%)</td><td>0.00 <b>(+27.08%)</b></td><td>452.60 (+0.56%)</td><td>328.32 (+5.14%)</td><td>301.30 (+7.53%)</td><td>234.50 (-11.51%)</td><td>86.21 (+10.98%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>450.10 (n/a)</td><td>312.26 (n/a)</td><td>280.20 (n/a)</td><td>265.00 (n/a)</td><td>77.68 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (+8.63%)</td><td>0.01 <b>(+27.18%)</b></td><td>0.01 (+16.96%)</td><td>0.01 <b>(+284.35%)</b></td><td>0.00 <b>(-37.78%)</b></td><td>476.70 <b>(-73.98%)</b></td><td>389.36 <b>(-45.57%)</b></td><td>446.80 (-14.49%)</td><td>270.60 (-7.93%)</td><td>94.05 <b>(-85.27%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1832.30 (n/a)</td><td>715.32 (n/a)</td><td>522.50 (n/a)</td><td>293.90 (n/a)</td><td>638.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (+8.88%)</td><td>0.01 (+0.04%)</td><td>0.02 (-1.99%)</td><td>0.01 <b>(-21.61%)</b></td><td>0.00 (+12.15%)</td><td>629.90 <b>(+27.56%)</b></td><td>357.70 (+4.13%)</td><td>268.00 (+2.02%)</td><td>223.50 (-8.14%)</td><td>166.41 <b>(+33.46%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>493.80 (n/a)</td><td>343.52 (n/a)</td><td>262.70 (n/a)</td><td>243.30 (n/a)</td><td>124.69 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-18.37%)</td><td>0.01 (-16.41%)</td><td>0.01 <b>(-32.82%)</b></td><td>0.00 <b>(-49.52%)</b></td><td>0.01 (+10.73%)</td><td>1094.30 <b>(+98.10%)</b></td><td>534.16 <b>(+41.86%)</b></td><td>457.40 <b>(+48.84%)</b></td><td>246.80 <b>(+22.54%)</b></td><td>350.37 <b>(+130.02%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>552.40 (n/a)</td><td>376.54 (n/a)</td><td>307.30 (n/a)</td><td>201.40 (n/a)</td><td>152.32 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 <b>(+30.55%)</b></td><td>0.01 <b>(+30.40%)</b></td><td>0.01 <b>(+53.74%)</b></td><td>0.01 (-8.60%)</td><td>0.00 <b>(+81.71%)</b></td><td>512.60 (+9.41%)</td><td>346.18 (-17.62%)</td><td>299.50 <b>(-34.95%)</b></td><td>211.50 <b>(-23.40%)</b></td><td>130.48 <b>(+59.45%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>468.50 (n/a)</td><td>420.24 (n/a)</td><td>460.40 (n/a)</td><td>276.10 (n/a)</td><td>81.84 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 <b>(+31.29%)</b></td><td>0.01 (+13.14%)</td><td>0.01 (+7.78%)</td><td>0.01 (-1.98%)</td><td>0.00 <b>(+56.84%)</b></td><td>577.90 (+2.01%)</td><td>414.50 (-7.30%)</td><td>440.60 (-7.22%)</td><td>240.10 <b>(-23.83%)</b></td><td>139.54 <b>(+21.97%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>566.50 (n/a)</td><td>447.14 (n/a)</td><td>474.90 (n/a)</td><td>315.20 (n/a)</td><td>114.41 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-17.68%)</td><td>0.01 <b>(+37.96%)</b></td><td>0.02 <b>(+98.83%)</b></td><td>0.01 <b>(+23.06%)</b></td><td>0.00 <b>(-28.24%)</b></td><td>619.50 (-18.73%)</td><td>330.28 <b>(-32.37%)</b></td><td>253.10 <b>(-49.71%)</b></td><td>240.00 <b>(+21.46%)</b></td><td>162.84 (-19.12%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>762.30 (n/a)</td><td>488.36 (n/a)</td><td>503.30 (n/a)</td><td>197.60 (n/a)</td><td>201.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (-10.78%)</td><td>0.01 (-0.10%)</td><td>0.01 (+13.49%)</td><td>0.01 (+5.78%)</td><td>0.00 <b>(-33.38%)</b></td><td>576.40 (-5.48%)</td><td>423.38 (-5.47%)</td><td>418.70 (-11.87%)</td><td>290.10 (+12.09%)</td><td>105.77 <b>(-30.68%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>609.80 (n/a)</td><td>447.90 (n/a)</td><td>475.10 (n/a)</td><td>258.80 (n/a)</td><td>152.57 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (+0.65%)</td><td>0.01 (-1.52%)</td><td>0.01 <b>(+35.80%)</b></td><td>0.00 <b>(-69.73%)</b></td><td>0.01 <b>(+56.95%)</b></td><td>1942.80 <b>(+230.41%)</b></td><td>667.24 <b>(+60.80%)</b></td><td>315.90 <b>(-26.35%)</b></td><td>255.00 (-0.62%)</td><td>721.32 <b>(+450.02%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>588.00 (n/a)</td><td>414.96 (n/a)</td><td>428.90 (n/a)</td><td>256.60 (n/a)</td><td>131.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (-1.39%)</td><td>0.02 (+16.37%)</td><td>0.02 (+0.87%)</td><td>0.01 (+13.81%)</td><td>0.01 (+6.02%)</td><td>586.40 (-12.12%)</td><td>410.08 (-13.55%)</td><td>446.30 (-0.87%)</td><td>236.80 (+1.41%)</td><td>156.46 (-4.34%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>667.30 (n/a)</td><td>474.34 (n/a)</td><td>450.20 (n/a)</td><td>233.50 (n/a)</td><td>163.56 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 <b>(-20.23%)</b></td><td>0.03 (+16.72%)</td><td>0.03 <b>(+85.52%)</b></td><td>0.01 <b>(+51.64%)</b></td><td>0.01 <b>(-48.47%)</b></td><td>546.50 <b>(-34.05%)</b></td><td>339.56 <b>(-28.98%)</b></td><td>293.30 <b>(-46.08%)</b></td><td>256.70 <b>(+25.34%)</b></td><td>118.43 <b>(-53.02%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>828.70 (n/a)</td><td>478.10 (n/a)</td><td>544.00 (n/a)</td><td>204.80 (n/a)</td><td>252.09 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 <b>(-21.85%)</b></td><td>0.02 (+3.52%)</td><td>0.02 (+6.63%)</td><td>0.01 (-7.18%)</td><td>0.01 <b>(-24.11%)</b></td><td>586.30 (+7.74%)</td><td>401.22 (-6.26%)</td><td>458.50 (-6.22%)</td><td>242.80 <b>(+27.99%)</b></td><td>146.74 (+3.49%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>544.20 (n/a)</td><td>428.00 (n/a)</td><td>488.90 (n/a)</td><td>189.70 (n/a)</td><td>141.79 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (+6.85%)</td><td>0.03 (+9.87%)</td><td>0.03 (+14.16%)</td><td>0.02 (+5.61%)</td><td>0.01 (+6.57%)</td><td>478.90 (-5.32%)</td><td>335.64 (-9.21%)</td><td>269.10 (-12.40%)</td><td>242.80 (-6.44%)</td><td>108.19 (-9.18%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.80 (n/a)</td><td>369.68 (n/a)</td><td>307.20 (n/a)</td><td>259.50 (n/a)</td><td>119.13 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (-19.09%)</td><td>0.02 (-5.95%)</td><td>0.02 (+2.80%)</td><td>0.02 <b>(+122.23%)</b></td><td>0.01 <b>(-44.87%)</b></td><td>480.00 <b>(-55.01%)</b></td><td>359.62 <b>(-21.94%)</b></td><td>403.00 (-2.73%)</td><td>214.10 <b>(+23.61%)</b></td><td>112.41 <b>(-68.73%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1066.80 (n/a)</td><td>460.68 (n/a)</td><td>414.30 (n/a)</td><td>173.20 (n/a)</td><td>359.50 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (-18.11%)</td><td>0.03 (+11.34%)</td><td>0.03 (+14.59%)</td><td>0.02 <b>(+90.81%)</b></td><td>0.01 <b>(-60.19%)</b></td><td>377.60 <b>(-47.59%)</b></td><td>289.86 <b>(-27.27%)</b></td><td>271.60 (-12.72%)</td><td>239.90 <b>(+22.15%)</b></td><td>56.81 <b>(-74.60%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>720.50 (n/a)</td><td>398.56 (n/a)</td><td>311.20 (n/a)</td><td>196.40 (n/a)</td><td>223.65 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (-19.72%)</td><td>0.02 (-6.32%)</td><td>0.02 (-8.66%)</td><td>0.02 <b>(+38.85%)</b></td><td>0.01 <b>(-37.16%)</b></td><td>496.00 <b>(-27.98%)</b></td><td>352.96 (-3.76%)</td><td>334.30 (+9.46%)</td><td>245.30 <b>(+24.58%)</b></td><td>99.85 <b>(-47.08%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>688.70 (n/a)</td><td>366.76 (n/a)</td><td>305.40 (n/a)</td><td>196.90 (n/a)</td><td>188.70 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (-7.28%)</td><td>0.03 (+13.44%)</td><td>0.03 <b>(+28.10%)</b></td><td>0.02 <b>(+20.73%)</b></td><td>0.01 <b>(-22.74%)</b></td><td>480.70 (-17.18%)</td><td>314.64 (-18.93%)</td><td>243.20 <b>(-21.95%)</b></td><td>236.30 (+7.85%)</td><td>109.19 <b>(-38.72%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.40 (n/a)</td><td>388.10 (n/a)</td><td>311.60 (n/a)</td><td>219.10 (n/a)</td><td>178.18 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 <b>(-22.13%)</b></td><td>0.02 <b>(+31.16%)</b></td><td>0.02 <b>(+63.39%)</b></td><td>0.01 <b>(+222.55%)</b></td><td>0.01 <b>(-44.14%)</b></td><td>578.10 <b>(-69.00%)</b></td><td>375.14 <b>(-49.33%)</b></td><td>353.90 <b>(-38.79%)</b></td><td>252.70 <b>(+28.40%)</b></td><td>134.05 <b>(-79.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1864.70 (n/a)</td><td>740.40 (n/a)</td><td>578.20 (n/a)</td><td>196.80 (n/a)</td><td>648.37 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (-10.11%)</td><td>0.03 (+18.03%)</td><td>0.03 <b>(+52.09%)</b></td><td>0.02 <b>(+31.64%)</b></td><td>0.01 <b>(-40.51%)</b></td><td>418.70 <b>(-24.04%)</b></td><td>284.48 <b>(-23.61%)</b></td><td>268.80 <b>(-34.26%)</b></td><td>210.80 (+11.24%)</td><td>79.74 <b>(-46.77%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.20 (n/a)</td><td>372.42 (n/a)</td><td>408.90 (n/a)</td><td>189.50 (n/a)</td><td>149.81 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (+6.47%)</td><td>0.02 (+10.67%)</td><td>0.02 (+9.17%)</td><td>0.02 (+4.45%)</td><td>0.01 (+5.80%)</td><td>522.10 (-4.25%)</td><td>410.48 (-9.34%)</td><td>442.20 (-8.39%)</td><td>214.90 (-6.08%)</td><td>127.87 (-0.40%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.30 (n/a)</td><td>452.78 (n/a)</td><td>482.70 (n/a)</td><td>228.80 (n/a)</td><td>128.39 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 <b>(+54.35%)</b></td><td>0.02 <b>(+39.43%)</b></td><td>0.02 <b>(+22.82%)</b></td><td>0.01 (+13.16%)</td><td>0.01 <b>(+102.69%)</b></td><td>601.70 (-11.63%)</td><td>443.36 <b>(-22.29%)</b></td><td>517.40 (-18.58%)</td><td>226.80 <b>(-35.22%)</b></td><td>165.46 (+17.35%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>680.90 (n/a)</td><td>570.50 (n/a)</td><td>635.50 (n/a)</td><td>350.10 (n/a)</td><td>140.99 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 <b>(+21.39%)</b></td><td>0.05 <b>(+36.94%)</b></td><td>0.04 <b>(+44.16%)</b></td><td>0.03 <b>(+113.50%)</b></td><td>0.01 <b>(-22.85%)</b></td><td>493.10 <b>(-53.17%)</b></td><td>356.18 <b>(-37.82%)</b></td><td>369.70 <b>(-30.64%)</b></td><td>239.20 (-17.63%)</td><td>95.65 <b>(-69.10%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1052.90 (n/a)</td><td>572.82 (n/a)</td><td>533.00 (n/a)</td><td>290.40 (n/a)</td><td>309.56 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (+4.01%)</td><td>0.05 (-2.94%)</td><td>0.06 (-2.17%)</td><td>0.04 (-0.66%)</td><td>0.01 <b>(+32.58%)</b></td><td>423.80 (+0.67%)</td><td>333.34 (+5.08%)</td><td>296.20 (+2.24%)</td><td>251.90 (-3.85%)</td><td>81.96 <b>(+30.91%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>421.00 (n/a)</td><td>317.22 (n/a)</td><td>289.70 (n/a)</td><td>262.00 (n/a)</td><td>62.61 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (+18.93%)</td><td>0.07 <b>(+51.68%)</b></td><td>0.06 <b>(+86.38%)</b></td><td>0.05 <b>(+117.00%)</b></td><td>0.01 <b>(-48.21%)</b></td><td>298.40 <b>(-53.92%)</b></td><td>254.66 <b>(-41.10%)</b></td><td>258.30 <b>(-46.34%)</b></td><td>218.60 (-15.92%)</td><td>34.89 <b>(-78.85%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>647.60 (n/a)</td><td>432.36 (n/a)</td><td>481.40 (n/a)</td><td>260.00 (n/a)</td><td>164.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (+15.51%)</td><td>0.06 <b>(+27.02%)</b></td><td>0.06 (+16.84%)</td><td>0.04 <b>(+46.04%)</b></td><td>0.01 <b>(-26.25%)</b></td><td>395.70 <b>(-31.52%)</b></td><td>287.76 <b>(-26.27%)</b></td><td>272.50 (-14.42%)</td><td>226.00 (-13.41%)</td><td>63.91 <b>(-55.08%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>577.80 (n/a)</td><td>390.28 (n/a)</td><td>318.40 (n/a)</td><td>261.00 (n/a)</td><td>142.29 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (+15.20%)</td><td>0.05 <b>(+20.52%)</b></td><td>0.06 <b>(+75.09%)</b></td><td>0.03 <b>(+27.32%)</b></td><td>0.02 (-12.35%)</td><td>472.20 <b>(-21.46%)</b></td><td>337.86 <b>(-21.85%)</b></td><td>294.90 <b>(-42.89%)</b></td><td>215.40 (-13.18%)</td><td>103.40 <b>(-36.47%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>601.20 (n/a)</td><td>432.30 (n/a)</td><td>516.40 (n/a)</td><td>248.10 (n/a)</td><td>162.76 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 <b>(+25.04%)</b></td><td>0.06 (+16.57%)</td><td>0.06 (+14.37%)</td><td>0.04 (-2.39%)</td><td>0.01 <b>(+62.52%)</b></td><td>465.30 (+2.44%)</td><td>288.20 (-10.94%)</td><td>255.80 (-12.55%)</td><td>223.60 <b>(-20.03%)</b></td><td>99.95 <b>(+36.26%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>454.20 (n/a)</td><td>323.60 (n/a)</td><td>292.50 (n/a)</td><td>279.60 (n/a)</td><td>73.35 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (+7.75%)</td><td>0.05 <b>(+72.75%)</b></td><td>0.05 <b>(+88.28%)</b></td><td>0.03 <b>(+279.70%)</b></td><td>0.02 <b>(-31.27%)</b></td><td>525.00 <b>(-73.67%)</b></td><td>366.54 <b>(-65.12%)</b></td><td>300.20 <b>(-46.90%)</b></td><td>239.40 (-7.17%)</td><td>124.19 <b>(-85.20%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1993.60 (n/a)</td><td>1050.94 (n/a)</td><td>565.30 (n/a)</td><td>257.90 (n/a)</td><td>839.16 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (+4.96%)</td><td>0.04 (-9.08%)</td><td>0.04 (-4.72%)</td><td>0.02 <b>(-38.01%)</b></td><td>0.02 <b>(+37.78%)</b></td><td>868.10 <b>(+61.33%)</b></td><td>503.28 <b>(+20.73%)</b></td><td>467.30 (+4.94%)</td><td>260.00 (-4.73%)</td><td>224.86 <b>(+118.92%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>538.10 (n/a)</td><td>416.88 (n/a)</td><td>445.30 (n/a)</td><td>272.90 (n/a)</td><td>102.71 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 <b>(-20.26%)</b></td><td>0.04 (-2.67%)</td><td>0.03 (+7.33%)</td><td>0.03 (+0.69%)</td><td>0.01 <b>(-38.71%)</b></td><td>589.00 (-0.69%)</td><td>449.82 (-3.32%)</td><td>474.40 (-6.83%)</td><td>285.00 <b>(+25.38%)</b></td><td>110.49 <b>(-22.40%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>593.10 (n/a)</td><td>465.26 (n/a)</td><td>509.20 (n/a)</td><td>227.30 (n/a)</td><td>142.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (-15.58%)</td><td>0.04 (-3.94%)</td><td>0.04 (+17.04%)</td><td>0.03 (-5.65%)</td><td>0.01 <b>(-29.69%)</b></td><td>508.90 (+5.98%)</td><td>388.28 (+0.33%)</td><td>398.50 (-14.54%)</td><td>275.00 (+18.48%)</td><td>98.87 (-16.59%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>480.20 (n/a)</td><td>387.00 (n/a)</td><td>466.30 (n/a)</td><td>232.10 (n/a)</td><td>118.53 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (+18.56%)</td><td>0.04 <b>(+21.91%)</b></td><td>0.04 (+13.70%)</td><td>0.03 (+15.63%)</td><td>0.01 <b>(+31.02%)</b></td><td>590.50 (-13.52%)</td><td>423.06 (-16.95%)</td><td>453.80 (-12.04%)</td><td>289.80 (-15.66%)</td><td>121.00 (-6.19%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>682.80 (n/a)</td><td>509.42 (n/a)</td><td>515.90 (n/a)</td><td>343.60 (n/a)</td><td>128.98 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (+0.42%)</td><td>0.03 (-10.97%)</td><td>0.03 (-19.00%)</td><td>0.03 <b>(+63.23%)</b></td><td>0.01 <b>(-23.08%)</b></td><td>619.90 <b>(-38.74%)</b></td><td>518.62 (-0.46%)</td><td>571.00 <b>(+23.46%)</b></td><td>288.30 (-0.41%)</td><td>131.91 <b>(-54.92%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1011.90 (n/a)</td><td>521.00 (n/a)</td><td>462.50 (n/a)</td><td>289.50 (n/a)</td><td>292.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 <b>(-20.04%)</b></td><td>0.11 (-9.90%)</td><td>0.10 (-13.30%)</td><td>0.09 <b>(+29.63%)</b></td><td>0.02 <b>(-46.25%)</b></td><td>378.80 <b>(-22.85%)</b></td><td>313.56 (+1.84%)</td><td>318.60 (+15.35%)</td><td>220.10 <b>(+25.06%)</b></td><td>61.67 <b>(-49.52%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>491.00 (n/a)</td><td>307.90 (n/a)</td><td>276.20 (n/a)</td><td>176.00 (n/a)</td><td>122.16 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 <b>(+24.49%)</b></td><td>0.12 <b>(+31.82%)</b></td><td>0.12 (+7.05%)</td><td>0.11 <b>(+83.02%)</b></td><td>0.01 <b>(-49.44%)</b></td><td>298.90 <b>(-45.36%)</b></td><td>269.36 <b>(-29.51%)</b></td><td>278.40 (-6.58%)</td><td>225.30 (-19.65%)</td><td>28.43 <b>(-77.85%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>547.00 (n/a)</td><td>382.10 (n/a)</td><td>298.00 (n/a)</td><td>280.40 (n/a)</td><td>128.36 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (-17.70%)</td><td>0.08 (-14.16%)</td><td>0.08 <b>(-28.42%)</b></td><td>0.06 (-7.96%)</td><td>0.03 (-18.53%)</td><td>566.90 (+8.64%)</td><td>424.88 (+14.51%)</td><td>415.60 <b>(+39.70%)</b></td><td>276.50 <b>(+21.54%)</b></td><td>139.53 (+1.63%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>521.80 (n/a)</td><td>371.04 (n/a)</td><td>297.50 (n/a)</td><td>227.50 (n/a)</td><td>137.30 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (+6.17%)</td><td>0.11 (+10.66%)</td><td>0.11 <b>(+41.59%)</b></td><td>0.06 (-0.16%)</td><td>0.03 (+7.71%)</td><td>504.80 (+0.16%)</td><td>337.94 (-8.67%)</td><td>290.60 <b>(-29.38%)</b></td><td>217.90 (-5.79%)</td><td>119.41 (+5.67%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>504.00 (n/a)</td><td>370.04 (n/a)</td><td>411.50 (n/a)</td><td>231.30 (n/a)</td><td>113.00 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 <b>(-52.12%)</b></td><td>0.06 <b>(-32.34%)</b></td><td>0.06 (-1.49%)</td><td>0.03 <b>(-27.28%)</b></td><td>0.02 <b>(-62.72%)</b></td><td>1116.70 <b>(+37.51%)</b></td><td>630.84 <b>(+33.27%)</b></td><td>523.60 (+1.53%)</td><td>468.20 <b>(+108.83%)</b></td><td>272.64 (+18.08%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>812.10 (n/a)</td><td>473.36 (n/a)</td><td>515.70 (n/a)</td><td>224.20 (n/a)</td><td>230.90 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (+8.58%)</td><td>0.09 <b>(-26.39%)</b></td><td>0.06 <b>(-51.80%)</b></td><td>0.06 <b>(-41.63%)</b></td><td>0.05 <b>(+113.52%)</b></td><td>578.40 <b>(+71.33%)</b></td><td>420.28 <b>(+56.95%)</b></td><td>505.30 <b>(+107.43%)</b></td><td>200.90 (-7.89%)</td><td>167.78 <b>(+240.70%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>337.60 (n/a)</td><td>267.78 (n/a)</td><td>243.60 (n/a)</td><td>218.10 (n/a)</td><td>49.24 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 <b>(-30.10%)</b></td><td>0.08 <b>(-24.84%)</b></td><td>0.08 <b>(-29.12%)</b></td><td>0.06 (-14.11%)</td><td>0.02 <b>(-43.69%)</b></td><td>574.00 (+16.43%)</td><td>436.34 <b>(+26.73%)</b></td><td>392.40 <b>(+41.10%)</b></td><td>305.40 <b>(+43.04%)</b></td><td>114.07 (-8.55%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>493.00 (n/a)</td><td>344.30 (n/a)</td><td>278.10 (n/a)</td><td>213.50 (n/a)</td><td>124.73 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 <b>(-36.22%)</b></td><td>0.07 <b>(-34.99%)</b></td><td>0.06 <b>(-47.48%)</b></td><td>0.06 (+3.91%)</td><td>0.02 <b>(-56.80%)</b></td><td>531.00 (-3.75%)</td><td>462.74 <b>(+42.85%)</b></td><td>514.40 <b>(+90.38%)</b></td><td>342.50 <b>(+56.75%)</b></td><td>85.45 <b>(-36.18%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>551.70 (n/a)</td><td>323.94 (n/a)</td><td>270.20 (n/a)</td><td>218.50 (n/a)</td><td>133.89 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 <b>(+62.01%)</b></td><td>0.10 <b>(+46.20%)</b></td><td>0.10 <b>(+71.14%)</b></td><td>0.05 (-11.82%)</td><td>0.05 <b>(+213.13%)</b></td><td>622.80 (+13.40%)</td><td>382.76 <b>(-20.41%)</b></td><td>313.40 <b>(-41.56%)</b></td><td>220.30 <b>(-38.26%)</b></td><td>184.82 <b>(+107.81%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>549.20 (n/a)</td><td>480.94 (n/a)</td><td>536.30 (n/a)</td><td>356.80 (n/a)</td><td>88.93 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 <b>(+21.47%)</b></td><td>0.10 <b>(+57.50%)</b></td><td>0.12 <b>(+89.84%)</b></td><td>0.06 <b>(+216.43%)</b></td><td>0.04 (-0.25%)</td><td>559.30 <b>(-68.40%)</b></td><td>358.60 <b>(-50.57%)</b></td><td>276.70 <b>(-47.33%)</b></td><td>224.80 (-17.66%)</td><td>142.58 <b>(-76.05%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1769.80 (n/a)</td><td>725.48 (n/a)</td><td>525.30 (n/a)</td><td>273.00 (n/a)</td><td>595.43 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (-15.78%)</td><td>0.08 (-9.28%)</td><td>0.07 (-4.37%)</td><td>0.06 (-5.01%)</td><td>0.02 <b>(-29.05%)</b></td><td>538.00 (+5.26%)</td><td>411.04 (+6.46%)</td><td>451.20 (+4.57%)</td><td>279.70 (+18.72%)</td><td>106.35 (-12.91%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>511.10 (n/a)</td><td>386.10 (n/a)</td><td>431.50 (n/a)</td><td>235.60 (n/a)</td><td>122.11 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (-19.55%)</td><td>0.07 (-10.91%)</td><td>0.07 (+18.61%)</td><td>0.05 (+19.60%)</td><td>0.02 <b>(-51.81%)</b></td><td>639.70 (-16.39%)</td><td>480.30 (-1.93%)</td><td>463.90 (-15.69%)</td><td>322.40 <b>(+24.29%)</b></td><td>117.72 <b>(-46.24%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>765.10 (n/a)</td><td>489.76 (n/a)</td><td>550.20 (n/a)</td><td>259.40 (n/a)</td><td>218.96 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (-9.73%)</td><td>0.09 (+4.23%)</td><td>0.09 (-0.93%)</td><td>0.08 <b>(+82.81%)</b></td><td>0.00 <b>(-83.29%)</b></td><td>297.70 <b>(-45.31%)</b></td><td>281.00 (-12.13%)</td><td>280.90 (+0.93%)</td><td>268.20 (+10.78%)</td><td>12.37 <b>(-90.27%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>544.30 (n/a)</td><td>319.80 (n/a)</td><td>278.30 (n/a)</td><td>242.10 (n/a)</td><td>127.14 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.17 (-13.72%)</td><td>0.15 (-16.21%)</td><td>0.15 <b>(-22.58%)</b></td><td>0.09 (-0.86%)</td><td>0.03 <b>(-28.67%)</b></td><td>548.10 (+0.86%)</td><td>354.14 (+14.86%)</td><td>324.50 <b>(+29.13%)</b></td><td>283.30 (+15.92%)</td><td>110.46 (-15.97%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>543.40 (n/a)</td><td>308.32 (n/a)</td><td>251.30 (n/a)</td><td>244.40 (n/a)</td><td>131.45 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>4.08 (+1.09%)</td><td>3.50 (-0.08%)</td><td>3.71 (+6.67%)</td><td>2.68 (-2.90%)</td><td>0.62 <b>(+26.92%)</b></td><td>3912.70 (+2.99%)</td><td>3083.00 (+1.12%)</td><td>2828.40 (-6.25%)</td><td>2571.60 (-1.07%)</td><td>588.75 <b>(+26.61%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>4.03 (n/a)</td><td>3.50 (n/a)</td><td>3.48 (n/a)</td><td>2.76 (n/a)</td><td>0.49 (n/a)</td><td>3799.20 (n/a)</td><td>3048.92 (n/a)</td><td>3017.00 (n/a)</td><td>2599.50 (n/a)</td><td>465.02 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.18 (+3.14%)</td><td>0.12 (-11.17%)</td><td>0.14 (-10.05%)</td><td>0.07 (+18.56%)</td><td>0.05 (-2.19%)</td><td>588.90 (-15.65%)</td><td>372.82 (+8.35%)</td><td>286.60 (+11.17%)</td><td>233.60 (-3.07%)</td><td>154.39 <b>(-22.14%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>698.20 (n/a)</td><td>344.10 (n/a)</td><td>257.80 (n/a)</td><td>241.00 (n/a)</td><td>198.28 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-6.18%)</td><td>0.02 (+11.25%)</td><td>0.02 <b>(+31.06%)</b></td><td>0.01 (+12.74%)</td><td>0.00 <b>(-26.14%)</b></td><td>415.50 (-11.31%)</td><td>317.62 (-12.61%)</td><td>295.10 <b>(-23.69%)</b></td><td>237.70 (+6.59%)</td><td>67.48 <b>(-26.18%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>468.50 (n/a)</td><td>363.44 (n/a)</td><td>386.70 (n/a)</td><td>223.00 (n/a)</td><td>91.41 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 <b>(-21.27%)</b></td><td>0.01 <b>(-24.11%)</b></td><td>0.01 <b>(-20.57%)</b></td><td>0.01 <b>(-29.03%)</b></td><td>0.00 (-15.96%)</td><td>685.80 <b>(+40.91%)</b></td><td>517.80 <b>(+33.25%)</b></td><td>452.80 <b>(+25.92%)</b></td><td>375.10 <b>(+27.02%)</b></td><td>138.35 <b>(+50.10%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>486.70 (n/a)</td><td>388.60 (n/a)</td><td>359.60 (n/a)</td><td>295.30 (n/a)</td><td>92.17 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 <b>(+52.42%)</b></td><td>0.02 <b>(+41.24%)</b></td><td>0.01 (+16.74%)</td><td>0.01 <b>(+38.46%)</b></td><td>0.01 <b>(+118.16%)</b></td><td>515.10 <b>(-27.77%)</b></td><td>381.98 <b>(-24.51%)</b></td><td>424.00 (-14.33%)</td><td>232.10 <b>(-34.38%)</b></td><td>136.48 (+0.35%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>713.10 (n/a)</td><td>505.98 (n/a)</td><td>494.90 (n/a)</td><td>353.70 (n/a)</td><td>136.00 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (-12.30%)</td><td>0.01 <b>(-28.98%)</b></td><td>0.01 <b>(-43.28%)</b></td><td>0.00 <b>(-43.09%)</b></td><td>0.00 (-18.94%)</td><td>1118.20 <b>(+75.73%)</b></td><td>603.34 <b>(+45.08%)</b></td><td>515.50 <b>(+76.30%)</b></td><td>308.60 (+14.04%)</td><td>304.16 <b>(+68.83%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>636.30 (n/a)</td><td>415.88 (n/a)</td><td>292.40 (n/a)</td><td>270.60 (n/a)</td><td>180.16 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (+1.47%)</td><td>0.02 (-6.44%)</td><td>0.02 (-0.54%)</td><td>0.01 <b>(-26.68%)</b></td><td>0.01 <b>(+98.80%)</b></td><td>501.30 <b>(+36.41%)</b></td><td>338.16 (+14.83%)</td><td>293.10 (+0.55%)</td><td>238.20 (-1.45%)</td><td>117.53 <b>(+154.46%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>367.50 (n/a)</td><td>294.50 (n/a)</td><td>291.50 (n/a)</td><td>241.70 (n/a)</td><td>46.19 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (+5.40%)</td><td>0.01 (+18.22%)</td><td>0.01 (-3.15%)</td><td>0.01 <b>(+143.85%)</b></td><td>0.00 (-4.77%)</td><td>528.50 <b>(-58.99%)</b></td><td>401.54 <b>(-29.15%)</b></td><td>470.70 (+3.25%)</td><td>230.50 (-5.14%)</td><td>142.24 <b>(-65.66%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1288.80 (n/a)</td><td>566.78 (n/a)</td><td>455.90 (n/a)</td><td>243.00 (n/a)</td><td>414.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 <b>(+48.09%)</b></td><td>0.02 <b>(+43.80%)</b></td><td>0.02 <b>(+48.30%)</b></td><td>0.01 <b>(+52.94%)</b></td><td>0.01 <b>(+73.31%)</b></td><td>604.40 <b>(-34.61%)</b></td><td>379.06 <b>(-28.91%)</b></td><td>311.50 <b>(-32.58%)</b></td><td>239.60 <b>(-32.47%)</b></td><td>156.41 <b>(-30.03%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>924.30 (n/a)</td><td>533.22 (n/a)</td><td>462.00 (n/a)</td><td>354.80 (n/a)</td><td>223.54 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (+9.23%)</td><td>0.01 <b>(+24.99%)</b></td><td>0.01 <b>(+91.17%)</b></td><td>0.01 <b>(+187.01%)</b></td><td>0.00 <b>(-38.94%)</b></td><td>660.50 <b>(-65.16%)</b></td><td>461.30 <b>(-55.50%)</b></td><td>477.20 <b>(-47.69%)</b></td><td>238.90 (-8.47%)</td><td>151.18 <b>(-81.22%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1895.60 (n/a)</td><td>1036.52 (n/a)</td><td>912.20 (n/a)</td><td>261.00 (n/a)</td><td>805.08 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-16.45%)</td><td>0.01 (+10.41%)</td><td>0.01 <b>(+33.04%)</b></td><td>0.01 (+11.60%)</td><td>0.00 <b>(-39.08%)</b></td><td>508.00 (-10.39%)</td><td>396.56 (-17.24%)</td><td>411.70 <b>(-24.83%)</b></td><td>247.10 (+19.72%)</td><td>100.59 <b>(-34.41%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.90 (n/a)</td><td>479.14 (n/a)</td><td>547.70 (n/a)</td><td>206.40 (n/a)</td><td>153.36 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 <b>(+70.47%)</b></td><td>0.01 (+9.76%)</td><td>0.01 (-16.75%)</td><td>0.01 <b>(+27.42%)</b></td><td>0.01 <b>(+86.29%)</b></td><td>532.20 <b>(-21.52%)</b></td><td>409.36 (-2.13%)</td><td>448.30 <b>(+20.12%)</b></td><td>152.30 <b>(-41.33%)</b></td><td>148.94 (-16.77%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>678.10 (n/a)</td><td>418.26 (n/a)</td><td>373.20 (n/a)</td><td>259.60 (n/a)</td><td>178.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (+6.92%)</td><td>0.01 (+4.76%)</td><td>0.01 (-16.68%)</td><td>0.01 (+3.06%)</td><td>0.01 <b>(+29.11%)</b></td><td>626.80 (-2.97%)</td><td>464.34 (+2.27%)</td><td>551.50 <b>(+20.02%)</b></td><td>228.00 (-6.48%)</td><td>189.30 <b>(+29.10%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>646.00 (n/a)</td><td>454.02 (n/a)</td><td>459.50 (n/a)</td><td>243.80 (n/a)</td><td>146.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (-5.74%)</td><td>0.01 (-19.76%)</td><td>0.01 <b>(-22.53%)</b></td><td>0.01 (-8.41%)</td><td>0.00 (-9.01%)</td><td>619.30 (+9.17%)</td><td>496.80 <b>(+23.97%)</b></td><td>516.40 <b>(+29.07%)</b></td><td>273.80 (+6.08%)</td><td>136.90 (+3.62%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>567.30 (n/a)</td><td>400.74 (n/a)</td><td>400.10 (n/a)</td><td>258.10 (n/a)</td><td>132.12 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (+3.82%)</td><td>0.02 <b>(-23.19%)</b></td><td>0.02 (-14.52%)</td><td>0.00 <b>(-72.15%)</b></td><td>0.01 <b>(+47.63%)</b></td><td>1893.40 <b>(+259.01%)</b></td><td>737.28 <b>(+85.96%)</b></td><td>499.30 (+16.99%)</td><td>268.00 (-3.67%)</td><td>659.67 <b>(+492.80%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>527.40 (n/a)</td><td>396.48 (n/a)</td><td>426.80 (n/a)</td><td>278.20 (n/a)</td><td>111.28 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 (+5.92%)</td><td>0.04 <b>(+29.73%)</b></td><td>0.04 <b>(+46.18%)</b></td><td>0.03 (-1.16%)</td><td>0.01 (+3.51%)</td><td>483.60 (+1.17%)</td><td>316.98 <b>(-22.64%)</b></td><td>304.10 <b>(-31.59%)</b></td><td>232.20 (-5.57%)</td><td>99.25 (+4.24%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>478.00 (n/a)</td><td>409.74 (n/a)</td><td>444.50 (n/a)</td><td>245.90 (n/a)</td><td>95.21 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (+19.04%)</td><td>0.02 (-6.41%)</td><td>0.03 (-7.98%)</td><td>0.00 <b>(-71.77%)</b></td><td>0.01 <b>(+84.10%)</b></td><td>1881.00 <b>(+254.24%)</b></td><td>610.84 <b>(+81.51%)</b></td><td>300.30 (+8.69%)</td><td>215.20 (-15.97%)</td><td>714.14 <b>(+508.61%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.00 (n/a)</td><td>336.54 (n/a)</td><td>276.30 (n/a)</td><td>256.10 (n/a)</td><td>117.34 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (+15.67%)</td><td>0.03 (+4.80%)</td><td>0.02 (-4.94%)</td><td>0.01 <b>(-49.19%)</b></td><td>0.01 <b>(+91.73%)</b></td><td>1021.40 <b>(+96.80%)</b></td><td>504.96 (+17.15%)</td><td>482.10 (+5.19%)</td><td>241.60 (-13.53%)</td><td>310.96 <b>(+232.11%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.00 (n/a)</td><td>431.02 (n/a)</td><td>458.30 (n/a)</td><td>279.40 (n/a)</td><td>93.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (+8.02%)</td><td>0.02 (+12.08%)</td><td>0.02 <b>(+20.56%)</b></td><td>0.00 (-0.26%)</td><td>0.01 (-18.61%)</td><td>1943.90 (+0.26%)</td><td>701.74 <b>(-28.61%)</b></td><td>457.50 (-17.04%)</td><td>240.60 (-7.43%)</td><td>701.54 (-18.25%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1938.90 (n/a)</td><td>983.02 (n/a)</td><td>551.50 (n/a)</td><td>259.90 (n/a)</td><td>858.20 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (-5.52%)</td><td>0.03 (+16.84%)</td><td>0.04 <b>(+64.48%)</b></td><td>0.02 <b>(-24.71%)</b></td><td>0.01 <b>(+20.47%)</b></td><td>659.30 <b>(+32.82%)</b></td><td>386.74 (-7.18%)</td><td>279.30 <b>(-39.19%)</b></td><td>240.00 (+5.82%)</td><td>187.37 <b>(+71.58%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.40 (n/a)</td><td>416.66 (n/a)</td><td>459.30 (n/a)</td><td>226.80 (n/a)</td><td>109.20 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 (-12.43%)</td><td>0.02 (+8.39%)</td><td>0.02 <b>(+45.46%)</b></td><td>0.01 <b>(+36.91%)</b></td><td>0.01 <b>(-29.01%)</b></td><td>546.80 <b>(-26.96%)</b></td><td>375.00 (-16.64%)</td><td>332.30 <b>(-31.26%)</b></td><td>226.00 (+14.20%)</td><td>130.81 <b>(-37.19%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>748.60 (n/a)</td><td>449.88 (n/a)</td><td>483.40 (n/a)</td><td>197.90 (n/a)</td><td>208.27 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (+14.17%)</td><td>0.02 <b>(+23.77%)</b></td><td>0.02 (+13.94%)</td><td>0.02 <b>(+275.59%)</b></td><td>0.01 <b>(-24.31%)</b></td><td>520.40 <b>(-73.37%)</b></td><td>432.58 <b>(-42.25%)</b></td><td>450.10 (-12.23%)</td><td>265.30 (-12.41%)</td><td>100.87 <b>(-85.16%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1954.50 (n/a)</td><td>749.04 (n/a)</td><td>512.80 (n/a)</td><td>302.90 (n/a)</td><td>679.87 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.03 (+15.72%)</td><td>0.02 (-18.35%)</td><td>0.02 (-19.84%)</td><td>0.01 <b>(-52.41%)</b></td><td>0.01 <b>(+83.90%)</b></td><td>1027.20 <b>(+110.15%)</b></td><td>573.58 <b>(+42.13%)</b></td><td>529.30 <b>(+24.75%)</b></td><td>267.70 (-13.59%)</td><td>280.31 <b>(+238.26%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>488.80 (n/a)</td><td>403.56 (n/a)</td><td>424.30 (n/a)</td><td>309.80 (n/a)</td><td>82.87 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-2.22%)</td><td>0.02 (-3.68%)</td><td>0.02 (-10.30%)</td><td>0.01 <b>(+23.95%)</b></td><td>0.00 <b>(-24.45%)</b></td><td>653.40 (-19.31%)</td><td>521.64 (+0.10%)</td><td>521.60 (+11.48%)</td><td>386.70 (+2.27%)</td><td>98.95 <b>(-41.42%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>809.80 (n/a)</td><td>521.12 (n/a)</td><td>467.90 (n/a)</td><td>378.10 (n/a)</td><td>168.91 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 <b>(+28.93%)</b></td><td>0.02 (+0.90%)</td><td>0.02 (-4.23%)</td><td>0.01 (-19.79%)</td><td>0.01 <b>(+72.51%)</b></td><td>687.80 <b>(+24.67%)</b></td><td>492.48 (+12.41%)</td><td>482.30 (+4.42%)</td><td>192.50 <b>(-22.44%)</b></td><td>193.56 <b>(+67.18%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.70 (n/a)</td><td>438.12 (n/a)</td><td>461.90 (n/a)</td><td>248.20 (n/a)</td><td>115.79 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 (-12.09%)</td><td>0.04 <b>(-22.54%)</b></td><td>0.03 <b>(-42.78%)</b></td><td>0.03 (+10.20%)</td><td>0.01 <b>(-33.80%)</b></td><td>611.40 (-9.26%)</td><td>479.72 (+17.60%)</td><td>499.20 <b>(+74.79%)</b></td><td>278.10 (+13.74%)</td><td>125.10 <b>(-35.98%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>673.80 (n/a)</td><td>407.94 (n/a)</td><td>285.60 (n/a)</td><td>244.50 (n/a)</td><td>195.40 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (+2.34%)</td><td>0.07 (+5.43%)</td><td>0.08 (-0.01%)</td><td>0.05 (+13.62%)</td><td>0.02 (-15.30%)</td><td>523.20 (-11.98%)</td><td>367.54 (-9.89%)</td><td>306.70 (+0.00%)</td><td>250.40 (-2.30%)</td><td>117.63 <b>(-30.17%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>594.40 (n/a)</td><td>407.86 (n/a)</td><td>306.70 (n/a)</td><td>256.30 (n/a)</td><td>168.45 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 <b>(+42.98%)</b></td><td>0.05 (+15.77%)</td><td>0.06 <b>(+57.36%)</b></td><td>0.01 <b>(-73.04%)</b></td><td>0.03 <b>(+123.50%)</b></td><td>1911.80 <b>(+270.94%)</b></td><td>619.14 <b>(+51.14%)</b></td><td>275.90 <b>(-36.44%)</b></td><td>205.30 <b>(-30.07%)</b></td><td>727.57 <b>(+559.84%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>515.40 (n/a)</td><td>409.66 (n/a)</td><td>434.10 (n/a)</td><td>293.60 (n/a)</td><td>110.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 <b>(+39.86%)</b></td><td>0.05 <b>(+40.69%)</b></td><td>0.04 (-2.01%)</td><td>0.03 <b>(+237.59%)</b></td><td>0.02 <b>(+23.39%)</b></td><td>598.10 <b>(-70.38%)</b></td><td>474.84 <b>(-42.26%)</b></td><td>582.20 (+2.05%)</td><td>290.60 <b>(-28.51%)</b></td><td>161.01 <b>(-76.13%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2019.10 (n/a)</td><td>822.32 (n/a)</td><td>570.50 (n/a)</td><td>406.50 (n/a)</td><td>674.61 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (+4.71%)</td><td>0.05 (+4.37%)</td><td>0.04 (+7.85%)</td><td>0.03 (-6.84%)</td><td>0.02 (+10.78%)</td><td>565.50 (+7.35%)</td><td>405.72 (-2.52%)</td><td>454.90 (-7.28%)</td><td>235.30 (-4.47%)</td><td>140.73 (+8.21%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>526.80 (n/a)</td><td>416.20 (n/a)</td><td>490.60 (n/a)</td><td>246.30 (n/a)</td><td>130.06 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 <b>(+74.58%)</b></td><td>0.05 <b>(+22.27%)</b></td><td>0.04 (+5.24%)</td><td>0.01 <b>(-65.31%)</b></td><td>0.03 <b>(+483.67%)</b></td><td>1784.80 <b>(+188.29%)</b></td><td>683.32 <b>(+24.74%)</b></td><td>491.60 (-4.99%)</td><td>278.90 <b>(-42.72%)</b></td><td>627.41 <b>(+872.62%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>619.10 (n/a)</td><td>547.80 (n/a)</td><td>517.40 (n/a)</td><td>486.90 (n/a)</td><td>64.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 <b>(+34.13%)</b></td><td>0.04 <b>(+41.44%)</b></td><td>0.03 (+10.86%)</td><td>0.03 <b>(+284.98%)</b></td><td>0.01 (+3.93%)</td><td>533.60 <b>(-74.02%)</b></td><td>414.36 <b>(-47.26%)</b></td><td>477.40 (-9.79%)</td><td>273.40 <b>(-25.44%)</b></td><td>127.97 <b>(-82.08%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2054.10 (n/a)</td><td>785.74 (n/a)</td><td>529.20 (n/a)</td><td>366.70 (n/a)</td><td>714.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 <b>(-23.98%)</b></td><td>0.04 (-8.33%)</td><td>0.04 (-13.20%)</td><td>0.03 <b>(+31.36%)</b></td><td>0.01 <b>(-47.55%)</b></td><td>533.70 <b>(-23.88%)</b></td><td>457.72 (-0.92%)</td><td>522.20 (+15.20%)</td><td>317.00 <b>(+31.54%)</b></td><td>99.01 <b>(-45.60%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>701.10 (n/a)</td><td>461.98 (n/a)</td><td>453.30 (n/a)</td><td>241.00 (n/a)</td><td>182.01 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.04 <b>(-32.29%)</b></td><td>0.03 (-7.51%)</td><td>0.03 (+10.41%)</td><td>0.03 (+2.62%)</td><td>0.00 <b>(-72.42%)</b></td><td>546.90 (-2.57%)</td><td>484.82 (+2.13%)</td><td>486.00 (-9.43%)</td><td>420.00 <b>(+47.68%)</b></td><td>46.01 <b>(-59.93%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>561.30 (n/a)</td><td>474.72 (n/a)</td><td>536.60 (n/a)</td><td>284.40 (n/a)</td><td>114.82 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 <b>(+37.54%)</b></td><td>0.05 <b>(+24.36%)</b></td><td>0.06 <b>(+30.79%)</b></td><td>0.04 (-3.31%)</td><td>0.02 <b>(+185.33%)</b></td><td>517.00 (+3.42%)</td><td>369.12 (-14.28%)</td><td>334.30 <b>(-23.54%)</b></td><td>256.30 <b>(-27.29%)</b></td><td>115.67 <b>(+118.54%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>499.90 (n/a)</td><td>430.62 (n/a)</td><td>437.20 (n/a)</td><td>352.50 (n/a)</td><td>52.93 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 <b>(-26.15%)</b></td><td>0.03 <b>(-29.10%)</b></td><td>0.03 <b>(-41.08%)</b></td><td>0.02 (-9.67%)</td><td>0.01 <b>(-45.31%)</b></td><td>668.70 (+10.69%)</td><td>513.60 <b>(+32.80%)</b></td><td>500.70 <b>(+69.73%)</b></td><td>346.20 <b>(+35.39%)</b></td><td>120.98 (-19.82%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>604.10 (n/a)</td><td>386.74 (n/a)</td><td>295.00 (n/a)</td><td>255.70 (n/a)</td><td>150.89 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 (+18.54%)</td><td>0.07 <b>(-22.68%)</b></td><td>0.06 <b>(-40.38%)</b></td><td>0.03 <b>(-51.37%)</b></td><td>0.04 <b>(+53.28%)</b></td><td>1076.40 <b>(+105.66%)</b></td><td>564.26 <b>(+52.33%)</b></td><td>518.70 <b>(+67.76%)</b></td><td>229.00 (-15.65%)</td><td>310.84 <b>(+165.52%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>523.40 (n/a)</td><td>370.42 (n/a)</td><td>309.20 (n/a)</td><td>271.50 (n/a)</td><td>117.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 <b>(-33.67%)</b></td><td>0.08 <b>(-21.64%)</b></td><td>0.07 <b>(-35.99%)</b></td><td>0.06 (+1.98%)</td><td>0.02 <b>(-52.58%)</b></td><td>520.20 (-1.96%)</td><td>414.02 (+15.76%)</td><td>440.70 <b>(+56.22%)</b></td><td>310.40 <b>(+50.75%)</b></td><td>95.18 <b>(-37.46%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>530.60 (n/a)</td><td>357.66 (n/a)</td><td>282.10 (n/a)</td><td>205.90 (n/a)</td><td>152.20 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 <b>(-33.09%)</b></td><td>0.09 <b>(-33.55%)</b></td><td>0.09 <b>(-40.43%)</b></td><td>0.07 (-17.20%)</td><td>0.03 <b>(-44.80%)</b></td><td>619.90 <b>(+20.77%)</b></td><td>471.68 <b>(+39.93%)</b></td><td>477.60 <b>(+67.87%)</b></td><td>272.00 <b>(+49.45%)</b></td><td>129.86 (-9.95%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>513.30 (n/a)</td><td>337.08 (n/a)</td><td>284.50 (n/a)</td><td>182.00 (n/a)</td><td>144.21 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 <b>(+30.21%)</b></td><td>0.09 <b>(+30.39%)</b></td><td>0.06 (+9.65%)</td><td>0.05 (-1.35%)</td><td>0.04 <b>(+79.30%)</b></td><td>631.30 (+1.36%)</td><td>427.16 (-15.70%)</td><td>504.50 (-8.80%)</td><td>228.60 <b>(-23.21%)</b></td><td>175.52 <b>(+40.71%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>622.80 (n/a)</td><td>506.74 (n/a)</td><td>553.20 (n/a)</td><td>297.70 (n/a)</td><td>124.74 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 <b>(-20.31%)</b></td><td>0.09 (-9.14%)</td><td>0.08 (-7.24%)</td><td>0.06 <b>(+49.30%)</b></td><td>0.03 <b>(-46.05%)</b></td><td>690.80 <b>(-33.02%)</b></td><td>479.86 (-10.84%)</td><td>487.60 (+7.80%)</td><td>286.60 <b>(+25.48%)</b></td><td>145.60 <b>(-55.52%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.06 (n/a)</td><td>1031.30 (n/a)</td><td>538.20 (n/a)</td><td>452.30 (n/a)</td><td>228.40 (n/a)</td><td>327.32 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (-6.75%)</td><td>0.08 (-10.38%)</td><td>0.07 <b>(-29.83%)</b></td><td>0.06 (+0.75%)</td><td>0.03 <b>(-24.22%)</b></td><td>587.60 (-0.74%)</td><td>434.86 (+5.78%)</td><td>475.10 <b>(+42.50%)</b></td><td>276.50 (+7.25%)</td><td>122.78 <b>(-25.71%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>592.00 (n/a)</td><td>411.10 (n/a)</td><td>333.40 (n/a)</td><td>257.80 (n/a)</td><td>165.28 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 <b>(-38.03%)</b></td><td>0.08 (-16.96%)</td><td>0.08 (+7.06%)</td><td>0.06 (-12.32%)</td><td>0.01 <b>(-63.64%)</b></td><td>617.50 (+14.06%)</td><td>495.66 (+13.74%)</td><td>460.20 (-6.60%)</td><td>419.60 <b>(+61.38%)</b></td><td>80.03 <b>(-33.16%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>541.40 (n/a)</td><td>435.80 (n/a)</td><td>492.70 (n/a)</td><td>260.00 (n/a)</td><td>119.74 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (-1.07%)</td><td>0.08 <b>(-22.98%)</b></td><td>0.06 <b>(-52.53%)</b></td><td>0.01 <b>(-76.35%)</b></td><td>0.06 <b>(+45.62%)</b></td><td>2453.00 <b>(+322.86%)</b></td><td>838.72 <b>(+135.86%)</b></td><td>589.30 <b>(+110.61%)</b></td><td>205.60 (+1.08%)</td><td>928.45 <b>(+480.87%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>580.10 (n/a)</td><td>355.60 (n/a)</td><td>279.80 (n/a)</td><td>203.40 (n/a)</td><td>159.84 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 <b>(+57.02%)</b></td><td>0.08 (+16.94%)</td><td>0.07 (-4.38%)</td><td>0.06 <b>(+44.42%)</b></td><td>0.04 <b>(+84.83%)</b></td><td>668.70 <b>(-30.76%)</b></td><td>505.50 (-11.78%)</td><td>557.20 (+4.60%)</td><td>235.60 <b>(-36.32%)</b></td><td>161.97 <b>(-29.62%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>965.80 (n/a)</td><td>573.00 (n/a)</td><td>532.70 (n/a)</td><td>370.00 (n/a)</td><td>230.15 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (+1.15%)</td><td>0.09 <b>(+23.00%)</b></td><td>0.10 <b>(+70.41%)</b></td><td>0.06 (+0.72%)</td><td>0.03 (+1.89%)</td><td>557.10 (-0.71%)</td><td>379.24 (-18.56%)</td><td>315.60 <b>(-41.33%)</b></td><td>266.90 (-1.11%)</td><td>124.55 (+0.12%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>561.10 (n/a)</td><td>465.64 (n/a)</td><td>537.90 (n/a)</td><td>269.90 (n/a)</td><td>124.40 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (+11.65%)</td><td>0.05 (-13.10%)</td><td>0.04 <b>(-39.20%)</b></td><td>0.03 <b>(-21.95%)</b></td><td>0.02 <b>(+37.15%)</b></td><td>611.40 <b>(+28.12%)</b></td><td>433.64 <b>(+22.84%)</b></td><td>483.90 <b>(+64.48%)</b></td><td>231.10 (-10.43%)</td><td>159.73 <b>(+51.57%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>477.20 (n/a)</td><td>353.02 (n/a)</td><td>294.20 (n/a)</td><td>258.00 (n/a)</td><td>105.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 <b>(+22.20%)</b></td><td>0.08 <b>(+41.83%)</b></td><td>0.07 <b>(+86.29%)</b></td><td>0.04 <b>(+27.36%)</b></td><td>0.03 (+1.17%)</td><td>508.80 <b>(-21.48%)</b></td><td>298.66 <b>(-32.92%)</b></td><td>283.30 <b>(-46.32%)</b></td><td>198.70 (-18.16%)</td><td>125.12 <b>(-31.27%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>648.00 (n/a)</td><td>445.20 (n/a)</td><td>527.80 (n/a)</td><td>242.80 (n/a)</td><td>182.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (-17.51%)</td><td>0.05 (-12.73%)</td><td>0.05 (-4.72%)</td><td>0.04 (-14.11%)</td><td>0.01 (-18.07%)</td><td>572.80 (+16.42%)</td><td>419.32 (+14.41%)</td><td>384.00 (+4.95%)</td><td>300.90 <b>(+21.23%)</b></td><td>112.04 (+17.61%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>492.00 (n/a)</td><td>366.52 (n/a)</td><td>365.90 (n/a)</td><td>248.20 (n/a)</td><td>95.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.10 (+16.49%)</td><td>0.06 (-1.49%)</td><td>0.07 (-5.10%)</td><td>0.04 (+6.27%)</td><td>0.02 (+18.46%)</td><td>497.80 (-5.90%)</td><td>355.88 (+3.40%)</td><td>312.50 (+5.40%)</td><td>206.70 (-14.16%)</td><td>127.09 (+3.76%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>529.00 (n/a)</td><td>344.18 (n/a)</td><td>296.50 (n/a)</td><td>240.80 (n/a)</td><td>122.49 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 <b>(-49.70%)</b></td><td>0.05 <b>(-24.43%)</b></td><td>0.04 (-5.02%)</td><td>0.03 (-4.71%)</td><td>0.01 <b>(-69.10%)</b></td><td>594.90 (+4.94%)</td><td>458.90 (+10.50%)</td><td>473.80 (+5.29%)</td><td>294.20 <b>(+98.78%)</b></td><td>107.47 <b>(-33.77%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>566.90 (n/a)</td><td>415.28 (n/a)</td><td>450.00 (n/a)</td><td>148.00 (n/a)</td><td>162.27 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 <b>(-33.21%)</b></td><td>0.05 (-5.33%)</td><td>0.05 (+12.59%)</td><td>0.03 (-12.72%)</td><td>0.01 <b>(-51.75%)</b></td><td>632.40 (+14.57%)</td><td>448.00 (+0.21%)</td><td>432.40 (-11.19%)</td><td>360.90 <b>(+49.75%)</b></td><td>109.02 (-13.70%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>552.00 (n/a)</td><td>447.04 (n/a)</td><td>486.90 (n/a)</td><td>241.00 (n/a)</td><td>126.33 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.06 <b>(-35.24%)</b></td><td>0.04 <b>(-28.26%)</b></td><td>0.05 (-14.39%)</td><td>0.01 <b>(-70.28%)</b></td><td>0.02 (-10.23%)</td><td>2038.10 <b>(+236.49%)</b></td><td>799.46 <b>(+82.36%)</b></td><td>517.20 (+16.80%)</td><td>384.90 <b>(+54.45%)</b></td><td>698.40 <b>(+429.99%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>605.70 (n/a)</td><td>438.40 (n/a)</td><td>442.80 (n/a)</td><td>249.20 (n/a)</td><td>131.78 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (-13.44%)</td><td>0.07 (-9.57%)</td><td>0.07 (-10.68%)</td><td>0.06 (+3.34%)</td><td>0.01 <b>(-39.57%)</b></td><td>444.30 (-3.24%)</td><td>358.50 (+5.78%)</td><td>328.90 (+11.99%)</td><td>283.20 (+15.54%)</td><td>73.43 <b>(-31.56%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>459.20 (n/a)</td><td>338.92 (n/a)</td><td>293.70 (n/a)</td><td>245.10 (n/a)</td><td>107.30 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.11 (+7.60%)</td><td>0.07 (-8.25%)</td><td>0.05 <b>(-30.79%)</b></td><td>0.04 (-11.39%)</td><td>0.03 <b>(+34.31%)</b></td><td>614.90 (+12.87%)</td><td>415.08 (+16.71%)</td><td>448.60 <b>(+44.48%)</b></td><td>217.00 (-7.11%)</td><td>169.32 <b>(+36.27%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>544.80 (n/a)</td><td>355.64 (n/a)</td><td>310.50 (n/a)</td><td>233.60 (n/a)</td><td>124.26 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 (-8.66%)</td><td>0.07 (-18.36%)</td><td>0.06 <b>(-33.18%)</b></td><td>0.04 (-19.42%)</td><td>0.03 (+19.16%)</td><td>586.10 <b>(+24.09%)</b></td><td>393.28 <b>(+32.47%)</b></td><td>403.90 <b>(+49.70%)</b></td><td>202.80 (+9.50%)</td><td>168.81 <b>(+56.78%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>472.30 (n/a)</td><td>296.88 (n/a)</td><td>269.80 (n/a)</td><td>185.20 (n/a)</td><td>107.67 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.12 <b>(+27.39%)</b></td><td>0.07 (-19.55%)</td><td>0.05 <b>(-42.92%)</b></td><td>0.01 <b>(-77.13%)</b></td><td>0.05 <b>(+166.70%)</b></td><td>1948.40 <b>(+337.35%)</b></td><td>692.30 <b>(+120.84%)</b></td><td>480.90 <b>(+75.19%)</b></td><td>198.60 <b>(-21.50%)</b></td><td>720.36 <b>(+815.15%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>445.50 (n/a)</td><td>313.48 (n/a)</td><td>274.50 (n/a)</td><td>253.00 (n/a)</td><td>78.71 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 (-3.09%)</td><td>0.06 (-17.09%)</td><td>0.05 (-12.30%)</td><td>0.04 <b>(-28.32%)</b></td><td>0.02 <b>(+32.17%)</b></td><td>618.70 <b>(+39.50%)</b></td><td>471.78 <b>(+27.74%)</b></td><td>454.90 (+14.01%)</td><td>267.50 (+3.16%)</td><td>149.77 <b>(+98.44%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>443.50 (n/a)</td><td>369.34 (n/a)</td><td>399.00 (n/a)</td><td>259.30 (n/a)</td><td>75.47 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (-3.88%)</td><td>0.06 <b>(+20.71%)</b></td><td>0.07 <b>(+41.34%)</b></td><td>0.04 <b>(+24.69%)</b></td><td>0.01 <b>(-31.05%)</b></td><td>471.70 (-19.81%)</td><td>310.96 <b>(-22.17%)</b></td><td>271.80 <b>(-29.26%)</b></td><td>265.50 (+4.04%)</td><td>89.95 <b>(-38.99%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>588.20 (n/a)</td><td>399.56 (n/a)</td><td>384.20 (n/a)</td><td>255.20 (n/a)</td><td>147.43 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 <b>(+26.39%)</b></td><td>0.05 (+8.07%)</td><td>0.04 (+6.99%)</td><td>0.03 (-4.74%)</td><td>0.02 <b>(+61.98%)</b></td><td>559.80 (+4.97%)</td><td>440.02 (-2.84%)</td><td>449.90 (-6.54%)</td><td>231.60 <b>(-20.87%)</b></td><td>125.56 <b>(+28.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>533.30 (n/a)</td><td>452.88 (n/a)</td><td>481.40 (n/a)</td><td>292.70 (n/a)</td><td>97.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.08 (-11.57%)</td><td>0.07 (-6.36%)</td><td>0.06 <b>(-21.24%)</b></td><td>0.04 (+15.77%)</td><td>0.02 <b>(-27.94%)</b></td><td>424.00 (-13.63%)</td><td>297.02 (+1.62%)</td><td>296.90 <b>(+26.99%)</b></td><td>226.60 (+13.07%)</td><td>78.78 <b>(-32.78%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>490.90 (n/a)</td><td>292.28 (n/a)</td><td>233.80 (n/a)</td><td>200.40 (n/a)</td><td>117.20 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 <b>(-32.63%)</b></td><td>0.04 <b>(-29.72%)</b></td><td>0.04 <b>(-24.04%)</b></td><td>0.03 <b>(-21.82%)</b></td><td>0.01 <b>(-50.73%)</b></td><td>590.70 <b>(+27.91%)</b></td><td>498.10 <b>(+36.74%)</b></td><td>522.00 <b>(+31.65%)</b></td><td>355.80 <b>(+48.44%)</b></td><td>95.99 (-7.75%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>461.80 (n/a)</td><td>364.28 (n/a)</td><td>396.50 (n/a)</td><td>239.70 (n/a)</td><td>104.05 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 <b>(+31.68%)</b></td><td>0.05 (+17.30%)</td><td>0.04 (+5.41%)</td><td>0.03 (+9.63%)</td><td>0.01 <b>(+50.42%)</b></td><td>614.20 (-8.78%)</td><td>438.32 (-12.85%)</td><td>439.30 (-5.14%)</td><td>274.60 <b>(-24.06%)</b></td><td>124.20 (+0.66%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>673.30 (n/a)</td><td>502.96 (n/a)</td><td>463.10 (n/a)</td><td>361.60 (n/a)</td><td>123.39 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.07 (+14.13%)</td><td>0.05 <b>(+22.15%)</b></td><td>0.04 (+19.86%)</td><td>0.03 <b>(+254.60%)</b></td><td>0.02 <b>(-25.60%)</b></td><td>534.20 <b>(-71.80%)</b></td><td>398.28 <b>(-43.54%)</b></td><td>409.80 (-16.55%)</td><td>254.10 (-12.38%)</td><td>122.79 <b>(-81.80%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1894.40 (n/a)</td><td>705.36 (n/a)</td><td>491.10 (n/a)</td><td>290.00 (n/a)</td><td>674.77 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.39 (-10.88%)</td><td>0.28 <b>(-24.64%)</b></td><td>0.28 <b>(-27.09%)</b></td><td>0.18 <b>(-40.16%)</b></td><td>0.08 <b>(+45.05%)</b></td><td>535.80 <b>(+67.07%)</b></td><td>380.02 <b>(+39.53%)</b></td><td>349.50 <b>(+37.17%)</b></td><td>255.10 (+12.23%)</td><td>112.12 <b>(+168.62%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.05 (n/a)</td><td>320.70 (n/a)</td><td>272.36 (n/a)</td><td>254.80 (n/a)</td><td>227.30 (n/a)</td><td>41.74 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.36 (+2.64%)</td><td>0.22 (-6.60%)</td><td>0.28 <b>(+30.82%)</b></td><td>0.05 <b>(-68.89%)</b></td><td>0.14 <b>(+95.43%)</b></td><td>1924.40 <b>(+221.48%)</b></td><td>790.68 <b>(+76.15%)</b></td><td>350.60 <b>(-23.57%)</b></td><td>275.90 (-2.54%)</td><td>717.46 <b>(+504.40%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.35 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>598.60 (n/a)</td><td>448.86 (n/a)</td><td>458.70 (n/a)</td><td>283.10 (n/a)</td><td>118.71 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.37 (-7.50%)</td><td>0.27 (-2.75%)</td><td>0.28 <b>(-23.67%)</b></td><td>0.18 <b>(+137.84%)</b></td><td>0.08 <b>(-39.73%)</b></td><td>549.40 <b>(-57.96%)</b></td><td>391.34 <b>(-24.50%)</b></td><td>351.70 <b>(+30.99%)</b></td><td>268.30 (+8.10%)</td><td>126.81 <b>(-72.00%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.40 (n/a)</td><td>0.28 (n/a)</td><td>0.37 (n/a)</td><td>0.08 (n/a)</td><td>0.14 (n/a)</td><td>1306.70 (n/a)</td><td>518.30 (n/a)</td><td>268.50 (n/a)</td><td>248.20 (n/a)</td><td>452.91 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.31 (+6.82%)</td><td>0.22 (+7.85%)</td><td>0.19 (-1.41%)</td><td>0.17 <b>(+59.84%)</b></td><td>0.06 (-18.55%)</td><td>422.50 <b>(-37.44%)</b></td><td>356.44 (-13.15%)</td><td>390.90 (+1.43%)</td><td>239.40 (-6.37%)</td><td>79.47 <b>(-51.79%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>675.30 (n/a)</td><td>410.42 (n/a)</td><td>385.40 (n/a)</td><td>255.70 (n/a)</td><td>164.85 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.24 (-8.48%)</td><td>0.16 (+3.40%)</td><td>0.14 (-0.56%)</td><td>0.10 <b>(+54.79%)</b></td><td>0.05 <b>(-27.11%)</b></td><td>717.60 <b>(-35.40%)</b></td><td>511.30 (-13.93%)</td><td>539.50 (+0.56%)</td><td>305.40 (+9.27%)</td><td>151.65 <b>(-51.41%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.26 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>1110.80 (n/a)</td><td>594.04 (n/a)</td><td>536.50 (n/a)</td><td>279.50 (n/a)</td><td>312.07 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.28 (-10.50%)</td><td>0.18 (-3.30%)</td><td>0.16 (-4.26%)</td><td>0.07 <b>(-45.81%)</b></td><td>0.09 <b>(+28.31%)</b></td><td>1082.00 <b>(+84.55%)</b></td><td>536.28 <b>(+23.07%)</b></td><td>469.60 (+4.45%)</td><td>267.50 (+11.74%)</td><td>335.04 <b>(+155.76%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.31 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>586.30 (n/a)</td><td>435.76 (n/a)</td><td>449.60 (n/a)</td><td>239.40 (n/a)</td><td>131.00 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (+1.12%)</td><td>0.11 (-5.48%)</td><td>0.08 <b>(-30.66%)</b></td><td>0.07 (+3.64%)</td><td>0.04 (-2.74%)</td><td>539.80 (-3.52%)</td><td>388.06 (+3.99%)</td><td>456.80 <b>(+44.24%)</b></td><td>227.30 (-1.13%)</td><td>142.15 (-10.88%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>559.50 (n/a)</td><td>373.16 (n/a)</td><td>316.70 (n/a)</td><td>229.90 (n/a)</td><td>159.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 <b>(-31.71%)</b></td><td>0.09 <b>(-31.94%)</b></td><td>0.08 <b>(-37.13%)</b></td><td>0.04 <b>(-49.67%)</b></td><td>0.04 (-18.87%)</td><td>898.20 <b>(+98.67%)</b></td><td>518.60 <b>(+58.75%)</b></td><td>462.90 <b>(+59.02%)</b></td><td>267.90 <b>(+46.47%)</b></td><td>257.21 <b>(+119.03%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>452.10 (n/a)</td><td>326.68 (n/a)</td><td>291.10 (n/a)</td><td>182.90 (n/a)</td><td>117.43 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (+15.68%)</td><td>0.12 <b>(+30.79%)</b></td><td>0.15 <b>(+80.95%)</b></td><td>0.07 (+13.05%)</td><td>0.04 <b>(+21.90%)</b></td><td>530.60 (-11.55%)</td><td>331.30 <b>(-22.61%)</b></td><td>251.60 <b>(-44.74%)</b></td><td>234.30 (-13.54%)</td><td>130.62 (-6.95%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>599.90 (n/a)</td><td>428.10 (n/a)</td><td>455.30 (n/a)</td><td>271.00 (n/a)</td><td>140.37 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (+4.48%)</td><td>0.10 (+1.72%)</td><td>0.08 (+4.75%)</td><td>0.02 (-6.15%)</td><td>0.06 (-2.41%)</td><td>1997.50 (+6.55%)</td><td>681.26 (+1.25%)</td><td>452.90 (-4.53%)</td><td>226.60 (-4.31%)</td><td>743.95 (+8.54%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.06 (n/a)</td><td>1874.70 (n/a)</td><td>672.86 (n/a)</td><td>474.40 (n/a)</td><td>236.80 (n/a)</td><td>685.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (+11.59%)</td><td>0.10 (+19.95%)</td><td>0.08 (-4.94%)</td><td>0.07 <b>(+273.36%)</b></td><td>0.04 (-14.86%)</td><td>520.50 <b>(-73.22%)</b></td><td>401.98 <b>(-42.42%)</b></td><td>466.80 (+5.18%)</td><td>250.80 (-10.36%)</td><td>130.85 <b>(-81.36%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1943.40 (n/a)</td><td>698.08 (n/a)</td><td>443.80 (n/a)</td><td>279.80 (n/a)</td><td>702.10 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (+0.42%)</td><td>0.09 (+6.23%)</td><td>0.08 <b>(+34.89%)</b></td><td>0.05 (-16.64%)</td><td>0.04 (-3.58%)</td><td>787.90 (+19.96%)</td><td>483.52 (-5.77%)</td><td>444.50 <b>(-25.85%)</b></td><td>245.10 (-0.41%)</td><td>197.86 (+10.82%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>656.80 (n/a)</td><td>513.14 (n/a)</td><td>599.50 (n/a)</td><td>246.10 (n/a)</td><td>178.53 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.22 (+11.01%)</td><td>0.16 (+9.25%)</td><td>0.16 (-2.11%)</td><td>0.08 (-9.73%)</td><td>0.05 (+18.85%)</td><td>536.90 (+10.77%)</td><td>292.40 (-4.74%)</td><td>256.80 (+2.15%)</td><td>184.70 (-9.95%)</td><td>139.99 <b>(+25.46%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>484.70 (n/a)</td><td>306.94 (n/a)</td><td>251.40 (n/a)</td><td>205.10 (n/a)</td><td>111.58 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 (-15.81%)</td><td>0.09 <b>(-41.75%)</b></td><td>0.07 <b>(-54.72%)</b></td><td>0.06 <b>(-45.10%)</b></td><td>0.03 <b>(+27.72%)</b></td><td>732.00 <b>(+82.13%)</b></td><td>526.68 <b>(+83.59%)</b></td><td>571.00 <b>(+120.89%)</b></td><td>291.00 (+18.78%)</td><td>166.91 <b>(+156.99%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>401.90 (n/a)</td><td>286.88 (n/a)</td><td>258.50 (n/a)</td><td>245.00 (n/a)</td><td>64.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (-6.34%)</td><td>0.10 <b>(-21.00%)</b></td><td>0.07 <b>(-48.63%)</b></td><td>0.06 <b>(-34.37%)</b></td><td>0.04 <b>(+30.78%)</b></td><td>680.80 <b>(+52.37%)</b></td><td>467.82 <b>(+37.21%)</b></td><td>550.80 <b>(+94.70%)</b></td><td>273.60 (+6.79%)</td><td>181.36 <b>(+89.03%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>446.80 (n/a)</td><td>340.94 (n/a)</td><td>282.90 (n/a)</td><td>256.20 (n/a)</td><td>95.94 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.09 <b>(-46.86%)</b></td><td>0.08 <b>(-28.97%)</b></td><td>0.08 (-17.05%)</td><td>0.07 (+4.26%)</td><td>0.01 <b>(-86.41%)</b></td><td>557.80 (-4.09%)</td><td>506.06 <b>(+26.95%)</b></td><td>494.60 <b>(+20.55%)</b></td><td>465.00 <b>(+88.18%)</b></td><td>36.23 <b>(-74.40%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>581.60 (n/a)</td><td>398.64 (n/a)</td><td>410.30 (n/a)</td><td>247.10 (n/a)</td><td>141.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (-6.41%)</td><td>0.10 (+10.16%)</td><td>0.08 (+3.20%)</td><td>0.07 (-7.73%)</td><td>0.04 (+6.82%)</td><td>614.80 (+8.37%)</td><td>452.74 (-6.32%)</td><td>513.80 (-3.09%)</td><td>264.80 (+6.82%)</td><td>167.28 <b>(+26.13%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>567.30 (n/a)</td><td>483.26 (n/a)</td><td>530.20 (n/a)</td><td>247.90 (n/a)</td><td>132.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.19 (+10.91%)</td><td>0.11 (-9.09%)</td><td>0.08 <b>(-31.09%)</b></td><td>0.05 <b>(-23.72%)</b></td><td>0.05 <b>(+26.07%)</b></td><td>746.50 <b>(+31.08%)</b></td><td>463.68 (+18.45%)</td><td>512.30 <b>(+45.13%)</b></td><td>220.00 (-9.84%)</td><td>207.25 <b>(+42.16%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>569.50 (n/a)</td><td>391.46 (n/a)</td><td>353.00 (n/a)</td><td>244.00 (n/a)</td><td>145.79 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (+7.54%)</td><td>0.11 (-11.09%)</td><td>0.12 (-13.73%)</td><td>0.06 (-15.95%)</td><td>0.04 <b>(+33.21%)</b></td><td>596.70 (+18.96%)</td><td>364.06 (+19.18%)</td><td>299.70 (+15.94%)</td><td>230.40 (-7.02%)</td><td>155.91 <b>(+41.70%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>501.60 (n/a)</td><td>305.46 (n/a)</td><td>258.50 (n/a)</td><td>247.80 (n/a)</td><td>110.03 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (-7.04%)</td><td>0.10 <b>(+33.16%)</b></td><td>0.10 <b>(+49.55%)</b></td><td>0.07 <b>(+94.45%)</b></td><td>0.03 <b>(-28.10%)</b></td><td>525.90 <b>(-48.57%)</b></td><td>373.52 <b>(-35.29%)</b></td><td>345.30 <b>(-33.13%)</b></td><td>259.40 (+7.59%)</td><td>117.57 <b>(-60.05%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1022.60 (n/a)</td><td>577.22 (n/a)</td><td>516.40 (n/a)</td><td>241.10 (n/a)</td><td>294.33 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (+1.89%)</td><td>0.07 <b>(-33.06%)</b></td><td>0.07 <b>(-41.93%)</b></td><td>0.02 <b>(-73.56%)</b></td><td>0.04 <b>(+59.14%)</b></td><td>1889.80 <b>(+278.19%)</b></td><td>729.80 <b>(+115.09%)</b></td><td>511.40 <b>(+72.25%)</b></td><td>259.80 (-1.85%)</td><td>657.98 <b>(+569.95%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>499.70 (n/a)</td><td>339.30 (n/a)</td><td>296.90 (n/a)</td><td>264.70 (n/a)</td><td>98.21 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.16 (+5.57%)</td><td>0.10 (+1.89%)</td><td>0.06 (-10.25%)</td><td>0.06 (-1.16%)</td><td>0.05 (+17.01%)</td><td>586.10 (+1.17%)</td><td>434.54 (+2.66%)</td><td>545.30 (+11.42%)</td><td>211.70 (-5.28%)</td><td>178.57 (+16.01%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>579.30 (n/a)</td><td>423.28 (n/a)</td><td>489.40 (n/a)</td><td>223.50 (n/a)</td><td>153.93 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.14 (-18.06%)</td><td>0.07 <b>(-35.75%)</b></td><td>0.07 <b>(-48.78%)</b></td><td>0.02 <b>(-63.07%)</b></td><td>0.04 (-15.74%)</td><td>1719.80 <b>(+170.75%)</b></td><td>698.68 <b>(+87.15%)</b></td><td>486.70 <b>(+95.23%)</b></td><td>248.20 <b>(+22.03%)</b></td><td>583.16 <b>(+197.43%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>635.20 (n/a)</td><td>373.32 (n/a)</td><td>249.30 (n/a)</td><td>203.40 (n/a)</td><td>196.06 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 (+3.24%)</td><td>0.08 <b>(-29.65%)</b></td><td>0.07 <b>(-42.38%)</b></td><td>0.02 <b>(-74.17%)</b></td><td>0.05 <b>(+35.62%)</b></td><td>1875.70 <b>(+287.22%)</b></td><td>713.76 <b>(+104.43%)</b></td><td>482.70 <b>(+73.57%)</b></td><td>236.90 (-3.11%)</td><td>660.48 <b>(+444.13%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>484.40 (n/a)</td><td>349.14 (n/a)</td><td>278.10 (n/a)</td><td>244.50 (n/a)</td><td>121.38 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.60 <b>(+21.48%)</b></td><td>0.34 (+18.35%)</td><td>0.25 (+6.38%)</td><td>0.21 <b>(+27.06%)</b></td><td>0.17 <b>(+28.45%)</b></td><td>619.90 <b>(-21.30%)</b></td><td>456.28 (-13.71%)</td><td>517.70 (-5.99%)</td><td>217.60 (-17.67%)</td><td>179.20 (-11.61%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.50 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>787.70 (n/a)</td><td>528.76 (n/a)</td><td>550.70 (n/a)</td><td>264.30 (n/a)</td><td>202.73 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.54 (+19.55%)</td><td>0.31 (-2.37%)</td><td>0.26 <b>(-28.12%)</b></td><td>0.22 <b>(+36.91%)</b></td><td>0.13 (+12.83%)</td><td>592.30 <b>(-26.97%)</b></td><td>463.88 (-1.10%)</td><td>500.50 <b>(+39.11%)</b></td><td>244.90 (-16.33%)</td><td>131.72 <b>(-37.36%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.36 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>811.00 (n/a)</td><td>469.06 (n/a)</td><td>359.80 (n/a)</td><td>292.70 (n/a)</td><td>210.27 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.41 (+3.13%)</td><td>0.26 (-15.48%)</td><td>0.27 (-2.43%)</td><td>0.12 <b>(-44.92%)</b></td><td>0.10 <b>(+31.41%)</b></td><td>1058.40 <b>(+81.57%)</b></td><td>582.54 <b>(+30.49%)</b></td><td>492.80 (+2.47%)</td><td>321.60 (-3.02%)</td><td>279.34 <b>(+158.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.08 (n/a)</td><td>582.90 (n/a)</td><td>446.44 (n/a)</td><td>480.90 (n/a)</td><td>331.60 (n/a)</td><td>108.13 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-10.07%)</td><td>0.01 <b>(-21.00%)</b></td><td>0.01 <b>(-37.18%)</b></td><td>0.01 (-16.59%)</td><td>0.00 <b>(+21.51%)</b></td><td>524.20 (+19.90%)</td><td>403.54 <b>(+31.88%)</b></td><td>457.90 <b>(+59.16%)</b></td><td>256.90 (+11.21%)</td><td>123.86 <b>(+55.99%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>437.20 (n/a)</td><td>306.00 (n/a)</td><td>287.70 (n/a)</td><td>231.00 (n/a)</td><td>79.40 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 <b>(+20.04%)</b></td><td>0.01 (+9.09%)</td><td>0.01 (+2.67%)</td><td>0.01 (-18.79%)</td><td>0.00 <b>(+24.34%)</b></td><td>563.60 <b>(+23.14%)</b></td><td>330.24 (-4.92%)</td><td>287.50 (-2.58%)</td><td>217.00 (-16.70%)</td><td>134.66 <b>(+33.71%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>457.70 (n/a)</td><td>347.34 (n/a)</td><td>295.10 (n/a)</td><td>260.50 (n/a)</td><td>100.71 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (-16.07%)</td><td>0.01 (-11.09%)</td><td>0.01 (-6.57%)</td><td>0.01 (-7.02%)</td><td>0.00 <b>(-31.78%)</b></td><td>519.40 (+7.54%)</td><td>391.40 (+9.20%)</td><td>413.00 (+7.02%)</td><td>293.60 (+19.16%)</td><td>93.97 (-11.31%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>483.00 (n/a)</td><td>358.42 (n/a)</td><td>385.90 (n/a)</td><td>246.40 (n/a)</td><td>105.95 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>9.11 (+14.10%)</td><td>7.32 (+17.52%)</td><td>7.96 (+19.74%)</td><td>4.03 (-0.09%)</td><td>2.03 <b>(+35.25%)</b></td><td>520.20 (+0.08%)</td><td>312.70 (-12.13%)</td><td>263.50 (-16.48%)</td><td>230.20 (-12.37%)</td><td>119.76 (+18.93%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>7.99 (n/a)</td><td>6.23 (n/a)</td><td>6.65 (n/a)</td><td>4.04 (n/a)</td><td>1.50 (n/a)</td><td>519.80 (n/a)</td><td>355.88 (n/a)</td><td>315.50 (n/a)</td><td>262.70 (n/a)</td><td>100.70 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.63 (+11.34%)</td><td>0.47 (+13.72%)</td><td>0.50 (+11.86%)</td><td>0.28 (+0.43%)</td><td>0.13 (+3.19%)</td><td>476.70 (-0.44%)</td><td>300.64 (-12.33%)</td><td>265.40 (-10.61%)</td><td>208.50 (-10.17%)</td><td>103.08 (-5.25%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.57 (n/a)</td><td>0.42 (n/a)</td><td>0.44 (n/a)</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>478.80 (n/a)</td><td>342.94 (n/a)</td><td>296.90 (n/a)</td><td>232.10 (n/a)</td><td>108.80 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.62 <b>(+21.00%)</b></td><td>0.40 (+0.67%)</td><td>0.40 (+6.95%)</td><td>0.23 (-11.70%)</td><td>0.16 <b>(+46.17%)</b></td><td>584.50 (+13.23%)</td><td>374.30 (+6.18%)</td><td>332.50 (-6.50%)</td><td>211.80 (-17.36%)</td><td>152.43 <b>(+44.06%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.52 (n/a)</td><td>0.40 (n/a)</td><td>0.37 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>516.20 (n/a)</td><td>352.52 (n/a)</td><td>355.60 (n/a)</td><td>256.30 (n/a)</td><td>105.81 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.67 <b>(+39.44%)</b></td><td>0.42 (+5.72%)</td><td>0.46 (+4.81%)</td><td>0.21 (-13.28%)</td><td>0.18 <b>(+99.88%)</b></td><td>617.10 (+15.32%)</td><td>370.52 (+5.79%)</td><td>287.40 (-4.58%)</td><td>197.10 <b>(-28.28%)</b></td><td>173.49 <b>(+63.71%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.48 (n/a)</td><td>0.40 (n/a)</td><td>0.44 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>535.10 (n/a)</td><td>350.24 (n/a)</td><td>301.20 (n/a)</td><td>274.80 (n/a)</td><td>105.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.62 (+11.29%)</td><td>0.47 (+3.25%)</td><td>0.45 (-1.98%)</td><td>0.35 (-2.74%)</td><td>0.10 <b>(+34.74%)</b></td><td>382.80 (+2.82%)</td><td>292.06 (-1.78%)</td><td>290.90 (+2.00%)</td><td>213.30 (-10.15%)</td><td>62.07 <b>(+23.01%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.56 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.35 (n/a)</td><td>0.07 (n/a)</td><td>372.30 (n/a)</td><td>297.36 (n/a)</td><td>285.20 (n/a)</td><td>237.40 (n/a)</td><td>50.46 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.53 (-11.15%)</td><td>0.46 (-8.56%)</td><td>0.49 (+4.29%)</td><td>0.30 <b>(-34.11%)</b></td><td>0.09 <b>(+53.11%)</b></td><td>438.80 <b>(+51.73%)</b></td><td>299.72 (+12.91%)</td><td>267.20 (-4.13%)</td><td>248.70 (+12.53%)</td><td>78.56 <b>(+171.23%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.60 (n/a)</td><td>0.50 (n/a)</td><td>0.47 (n/a)</td><td>0.46 (n/a)</td><td>0.06 (n/a)</td><td>289.20 (n/a)</td><td>265.46 (n/a)</td><td>278.70 (n/a)</td><td>221.00 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.01 (-12.21%)</td><td>0.01 (-12.11%)</td><td>0.01 <b>(-26.07%)</b></td><td>0.01 (-14.56%)</td><td>0.00 (-5.42%)</td><td>614.40 (+17.05%)</td><td>409.40 (+14.70%)</td><td>414.00 <b>(+35.25%)</b></td><td>286.60 (+13.91%)</td><td>133.39 (+19.29%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>524.90 (n/a)</td><td>356.94 (n/a)</td><td>306.10 (n/a)</td><td>251.60 (n/a)</td><td>111.82 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.02 (-17.45%)</td><td>0.01 (-12.28%)</td><td>0.01 (-0.08%)</td><td>0.01 (-5.69%)</td><td>0.00 (-14.07%)</td><td>601.80 (+6.04%)</td><td>357.28 (+12.83%)</td><td>285.60 (+0.07%)</td><td>235.90 <b>(+21.16%)</b></td><td>151.25 (+3.80%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>567.50 (n/a)</td><td>316.64 (n/a)</td><td>285.40 (n/a)</td><td>194.70 (n/a)</td><td>145.71 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.00 <b>(-28.57%)</b></td><td>0.00 <b>(-26.32%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-47.64%)</b></td><td>20990.00 (-2.09%)</td><td>15496.55 (+3.41%)</td><td>16785.78 (-15.98%)</td><td>7715.93 <b>(+33.98%)</b></td><td>4954.39 <b>(-38.94%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>21437.51 (n/a)</td><td>14984.85 (n/a)</td><td>19977.22 (n/a)</td><td>5759.07 (n/a)</td><td>8114.46 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.00 (-7.14%)</td><td>0.00 <b>(-29.55%)</b></td><td>0.00 <b>(-50.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-8.87%)</td><td>20775.88 (+4.59%)</td><td>16247.85 <b>(+38.16%)</b></td><td>17387.87 <b>(+110.88%)</b></td><td>6125.44 (+2.01%)</td><td>5975.88 (-6.80%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19864.31 (n/a)</td><td>11760.23 (n/a)</td><td>8245.53 (n/a)</td><td>6004.96 (n/a)</td><td>6411.73 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (-3.39%)</td><td>0.10 (+12.23%)</td><td>0.09 <b>(+22.52%)</b></td><td>0.08 (+9.63%)</td><td>0.03 (-12.85%)</td><td>27490.69 (-8.73%)</td><td>21977.91 (-12.48%)</td><td>22938.65 (-18.42%)</td><td>15642.08 (+3.55%)</td><td>5222.86 (-17.28%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>30120.34 (n/a)</td><td>25110.88 (n/a)</td><td>28116.72 (n/a)</td><td>15105.13 (n/a)</td><td>6314.17 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>2.96 (+14.17%)</td><td>1.81 (-2.93%)</td><td>1.69 <b>(-26.10%)</b></td><td>0.57 (+7.86%)</td><td>0.91 (+8.43%)</td><td>1835.00 (-7.29%)</td><td>793.62 (+0.32%)</td><td>621.90 <b>(+35.31%)</b></td><td>354.00 (-12.40%)</td><td>599.78 (-10.78%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>2.59 (n/a)</td><td>1.87 (n/a)</td><td>2.28 (n/a)</td><td>0.53 (n/a)</td><td>0.84 (n/a)</td><td>1979.20 (n/a)</td><td>791.10 (n/a)</td><td>459.60 (n/a)</td><td>404.10 (n/a)</td><td>672.28 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>2.74 <b>(-21.52%)</b></td><td>1.21 (-15.75%)</td><td>1.16 (+2.17%)</td><td>0.30 (-1.23%)</td><td>1.01 <b>(-20.32%)</b></td><td>3518.20 (+1.25%)</td><td>1791.22 <b>(+23.55%)</b></td><td>901.50 (-2.13%)</td><td>383.10 <b>(+27.45%)</b></td><td>1564.30 <b>(+21.61%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>3.49 (n/a)</td><td>1.43 (n/a)</td><td>1.14 (n/a)</td><td>0.30 (n/a)</td><td>1.27 (n/a)</td><td>3474.90 (n/a)</td><td>1449.84 (n/a)</td><td>921.10 (n/a)</td><td>300.60 (n/a)</td><td>1286.29 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>3.50 (+5.29%)</td><td>1.89 <b>(-28.11%)</b></td><td>1.49 <b>(-40.75%)</b></td><td>1.13 <b>(-46.95%)</b></td><td>0.96 <b>(+99.94%)</b></td><td>928.00 <b>(+88.50%)</b></td><td>650.04 <b>(+58.67%)</b></td><td>706.00 <b>(+68.78%)</b></td><td>299.40 (-5.01%)</td><td>243.91 <b>(+245.33%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>3.33 (n/a)</td><td>2.62 (n/a)</td><td>2.51 (n/a)</td><td>2.13 (n/a)</td><td>0.48 (n/a)</td><td>492.30 (n/a)</td><td>409.68 (n/a)</td><td>418.30 (n/a)</td><td>315.20 (n/a)</td><td>70.63 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>3.61 <b>(+48.02%)</b></td><td>2.15 (-5.04%)</td><td>1.50 <b>(-36.86%)</b></td><td>1.09 <b>(-45.46%)</b></td><td>1.25 <b>(+573.32%)</b></td><td>962.00 <b>(+83.38%)</b></td><td>632.68 <b>(+36.11%)</b></td><td>699.80 <b>(+58.36%)</b></td><td>290.30 <b>(-32.44%)</b></td><td>319.98 <b>(+701.89%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>2.44 (n/a)</td><td>2.27 (n/a)</td><td>2.37 (n/a)</td><td>2.00 (n/a)</td><td>0.19 (n/a)</td><td>524.60 (n/a)</td><td>464.82 (n/a)</td><td>441.90 (n/a)</td><td>429.70 (n/a)</td><td>39.90 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>4.15 <b>(+49.10%)</b></td><td>3.36 <b>(+111.82%)</b></td><td>3.82 <b>(+129.03%)</b></td><td>2.38 <b>(+303.86%)</b></td><td>0.81 (-18.04%)</td><td>880.90 <b>(-75.24%)</b></td><td>658.28 <b>(-67.20%)</b></td><td>548.90 <b>(-56.34%)</b></td><td>505.10 <b>(-32.94%)</b></td><td>174.10 <b>(-87.78%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>2.78 (n/a)</td><td>1.58 (n/a)</td><td>1.67 (n/a)</td><td>0.59 (n/a)</td><td>0.99 (n/a)</td><td>3557.60 (n/a)</td><td>2006.92 (n/a)</td><td>1257.20 (n/a)</td><td>753.20 (n/a)</td><td>1424.41 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>5.79 (+8.36%)</td><td>3.89 <b>(+21.16%)</b></td><td>4.34 <b>(+24.03%)</b></td><td>0.58 (-2.65%)</td><td>2.00 (+17.27%)</td><td>3635.10 (+2.73%)</td><td>1091.84 (-5.98%)</td><td>483.20 (-19.37%)</td><td>362.50 (-7.71%)</td><td>1423.65 (+6.76%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.34 (n/a)</td><td>3.21 (n/a)</td><td>3.50 (n/a)</td><td>0.59 (n/a)</td><td>1.71 (n/a)</td><td>3538.60 (n/a)</td><td>1161.32 (n/a)</td><td>599.30 (n/a)</td><td>392.80 (n/a)</td><td>1333.51 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>5.63 <b>(+39.91%)</b></td><td>3.16 <b>(+34.35%)</b></td><td>3.51 <b>(+46.89%)</b></td><td>0.60 (-4.82%)</td><td>2.31 <b>(+91.79%)</b></td><td>3477.40 (+5.07%)</td><td>1409.10 (+8.47%)</td><td>596.70 <b>(-31.92%)</b></td><td>372.40 <b>(-28.51%)</b></td><td>1379.74 <b>(+21.45%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>4.03 (n/a)</td><td>2.35 (n/a)</td><td>2.39 (n/a)</td><td>0.63 (n/a)</td><td>1.21 (n/a)</td><td>3309.60 (n/a)</td><td>1299.10 (n/a)</td><td>876.50 (n/a)</td><td>520.90 (n/a)</td><td>1136.06 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>5.57 (-6.25%)</td><td>3.58 (+13.24%)</td><td>3.16 <b>(-20.97%)</b></td><td>2.72 <b>(+219.36%)</b></td><td>1.17 <b>(-47.42%)</b></td><td>771.40 <b>(-68.69%)</b></td><td>626.66 <b>(-49.27%)</b></td><td>663.80 <b>(+26.53%)</b></td><td>376.30 (+6.66%)</td><td>158.88 <b>(-85.03%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.95 (n/a)</td><td>3.16 (n/a)</td><td>4.00 (n/a)</td><td>0.85 (n/a)</td><td>2.22 (n/a)</td><td>2463.50 (n/a)</td><td>1235.36 (n/a)</td><td>524.60 (n/a)</td><td>352.80 (n/a)</td><td>1061.46 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>4.02 <b>(-24.32%)</b></td><td>2.43 <b>(-32.21%)</b></td><td>1.78 <b>(-51.24%)</b></td><td>0.86 <b>(-59.88%)</b></td><td>1.47 <b>(+24.22%)</b></td><td>2440.00 <b>(+149.28%)</b></td><td>1208.68 <b>(+88.79%)</b></td><td>1176.40 <b>(+105.05%)</b></td><td>521.30 <b>(+32.14%)</b></td><td>787.46 <b>(+257.16%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.32 (n/a)</td><td>3.59 (n/a)</td><td>3.66 (n/a)</td><td>2.14 (n/a)</td><td>1.18 (n/a)</td><td>978.80 (n/a)</td><td>640.24 (n/a)</td><td>573.70 (n/a)</td><td>394.50 (n/a)</td><td>220.48 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>4.18 (-19.38%)</td><td>2.61 (-18.40%)</td><td>2.79 (-12.98%)</td><td>0.59 (+0.95%)</td><td>1.36 <b>(-25.62%)</b></td><td>3553.70 (-0.94%)</td><td>1282.86 (+7.51%)</td><td>752.70 (+14.92%)</td><td>502.00 <b>(+24.04%)</b></td><td>1282.17 (-5.07%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.18 (n/a)</td><td>3.20 (n/a)</td><td>3.20 (n/a)</td><td>0.58 (n/a)</td><td>1.83 (n/a)</td><td>3587.40 (n/a)</td><td>1193.28 (n/a)</td><td>655.00 (n/a)</td><td>404.70 (n/a)</td><td>1350.71 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>5.67 (+12.67%)</td><td>3.79 (-6.05%)</td><td>4.02 (+0.36%)</td><td>1.21 <b>(-63.84%)</b></td><td>1.61 <b>(+155.09%)</b></td><td>3454.40 <b>(+176.53%)</b></td><td>1466.00 <b>(+38.41%)</b></td><td>1043.90 (-0.35%)</td><td>740.20 (-11.25%)</td><td>1120.16 <b>(+620.81%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>5.03 (n/a)</td><td>4.03 (n/a)</td><td>4.00 (n/a)</td><td>3.36 (n/a)</td><td>0.63 (n/a)</td><td>1249.20 (n/a)</td><td>1059.20 (n/a)</td><td>1047.60 (n/a)</td><td>834.00 (n/a)</td><td>155.40 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>7.01 (-11.66%)</td><td>6.41 <b>(+123.88%)</b></td><td>6.41 <b>(+271.86%)</b></td><td>5.90 <b>(+403.93%)</b></td><td>0.48 <b>(-83.17%)</b></td><td>711.40 <b>(-80.15%)</b></td><td>657.06 <b>(-72.25%)</b></td><td>654.30 <b>(-73.11%)</b></td><td>597.90 (+13.20%)</td><td>49.36 <b>(-96.07%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>7.94 (n/a)</td><td>2.86 (n/a)</td><td>1.72 (n/a)</td><td>1.17 (n/a)</td><td>2.87 (n/a)</td><td>3584.70 (n/a)</td><td>2367.68 (n/a)</td><td>2433.30 (n/a)</td><td>528.20 (n/a)</td><td>1254.42 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>7.43 (-4.70%)</td><td>4.45 (-0.39%)</td><td>3.98 <b>(-31.16%)</b></td><td>1.21 (-2.07%)</td><td>2.37 (-17.01%)</td><td>3468.50 (+2.11%)</td><td>1386.34 (-11.52%)</td><td>1055.10 <b>(+45.25%)</b></td><td>564.80 (+4.92%)</td><td>1188.36 (-7.64%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>7.79 (n/a)</td><td>4.47 (n/a)</td><td>5.77 (n/a)</td><td>1.23 (n/a)</td><td>2.86 (n/a)</td><td>3396.80 (n/a)</td><td>1566.88 (n/a)</td><td>726.40 (n/a)</td><td>538.30 (n/a)</td><td>1286.64 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>7.84 (-14.73%)</td><td>4.62 <b>(-43.26%)</b></td><td>4.13 <b>(-51.79%)</b></td><td>1.27 <b>(-81.10%)</b></td><td>2.59 <b>(+156.22%)</b></td><td>3296.70 <b>(+429.00%)</b></td><td>1345.74 <b>(+158.07%)</b></td><td>1016.60 <b>(+107.43%)</b></td><td>535.10 (+17.27%)</td><td>1126.11 <b>(+1539.00%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>9.19 (n/a)</td><td>8.15 (n/a)</td><td>8.56 (n/a)</td><td>6.73 (n/a)</td><td>1.01 (n/a)</td><td>623.20 (n/a)</td><td>521.46 (n/a)</td><td>490.10 (n/a)</td><td>456.30 (n/a)</td><td>68.71 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>9.41 <b>(+36.28%)</b></td><td>6.72 <b>(+47.92%)</b></td><td>6.56 <b>(+46.47%)</b></td><td>4.38 <b>(+159.53%)</b></td><td>1.79 (-19.32%)</td><td>957.50 <b>(-61.47%)</b></td><td>662.00 <b>(-44.97%)</b></td><td>639.70 <b>(-31.73%)</b></td><td>445.90 <b>(-26.61%)</b></td><td>184.73 <b>(-76.16%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>6.90 (n/a)</td><td>4.54 (n/a)</td><td>4.48 (n/a)</td><td>1.69 (n/a)</td><td>2.22 (n/a)</td><td>2485.10 (n/a)</td><td>1203.06 (n/a)</td><td>937.00 (n/a)</td><td>607.60 (n/a)</td><td>774.80 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>10.70 (+18.38%)</td><td>4.00 <b>(-21.87%)</b></td><td>2.50 <b>(-53.36%)</b></td><td>1.16 <b>(-33.23%)</b></td><td>3.88 <b>(+39.18%)</b></td><td>3605.20 <b>(+49.78%)</b></td><td>1830.74 <b>(+63.46%)</b></td><td>1676.80 <b>(+114.42%)</b></td><td>392.10 (-15.51%)</td><td>1238.89 <b>(+59.52%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>9.04 (n/a)</td><td>5.12 (n/a)</td><td>5.36 (n/a)</td><td>1.74 (n/a)</td><td>2.79 (n/a)</td><td>2407.00 (n/a)</td><td>1119.96 (n/a)</td><td>782.00 (n/a)</td><td>464.10 (n/a)</td><td>776.66 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>1.65 (-1.01%)</td><td>0.89 (-19.86%)</td><td>0.94 <b>(-33.88%)</b></td><td>0.17 (+4.39%)</td><td>0.54 (-14.14%)</td><td>3168.20 (-4.20%)</td><td>1069.42 (+6.80%)</td><td>556.70 <b>(+51.24%)</b></td><td>318.70 (+1.01%)</td><td>1186.00 (-8.57%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>1.66 (n/a)</td><td>1.11 (n/a)</td><td>1.42 (n/a)</td><td>0.16 (n/a)</td><td>0.63 (n/a)</td><td>3307.20 (n/a)</td><td>1001.36 (n/a)</td><td>368.10 (n/a)</td><td>315.50 (n/a)</td><td>1297.16 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>2.54 (-1.30%)</td><td>1.96 (+17.43%)</td><td>2.26 <b>(+42.00%)</b></td><td>0.43 (-14.63%)</td><td>0.88 (+8.42%)</td><td>2457.70 (+17.14%)</td><td>853.20 (-2.60%)</td><td>464.30 <b>(-29.58%)</b></td><td>413.10 (+1.32%)</td><td>897.98 <b>(+28.67%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>2.57 (n/a)</td><td>1.67 (n/a)</td><td>1.59 (n/a)</td><td>0.50 (n/a)</td><td>0.81 (n/a)</td><td>2098.10 (n/a)</td><td>876.02 (n/a)</td><td>659.30 (n/a)</td><td>407.70 (n/a)</td><td>697.87 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>3.42 (-1.54%)</td><td>2.71 <b>(+28.39%)</b></td><td>2.78 (+15.48%)</td><td>1.67 <b>(+67.79%)</b></td><td>0.71 <b>(-32.57%)</b></td><td>1256.20 <b>(-40.40%)</b></td><td>828.60 <b>(-34.34%)</b></td><td>753.80 (-13.41%)</td><td>613.80 (+1.56%)</td><td>260.83 <b>(-62.31%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>3.47 (n/a)</td><td>2.11 (n/a)</td><td>2.41 (n/a)</td><td>0.99 (n/a)</td><td>1.05 (n/a)</td><td>2107.70 (n/a)</td><td>1261.86 (n/a)</td><td>870.50 (n/a)</td><td>604.40 (n/a)</td><td>691.99 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>1.93 (+6.30%)</td><td>1.53 <b>(+36.20%)</b></td><td>1.64 <b>(+66.63%)</b></td><td>1.06 <b>(+27.73%)</b></td><td>0.38 (-3.19%)</td><td>493.20 <b>(-21.71%)</b></td><td>363.28 <b>(-27.90%)</b></td><td>320.60 <b>(-39.99%)</b></td><td>271.40 (-5.93%)</td><td>98.60 <b>(-23.47%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>1.82 (n/a)</td><td>1.12 (n/a)</td><td>0.98 (n/a)</td><td>0.83 (n/a)</td><td>0.40 (n/a)</td><td>630.00 (n/a)</td><td>503.86 (n/a)</td><td>534.20 (n/a)</td><td>288.50 (n/a)</td><td>128.83 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.15 <b>(+44.12%)</b></td><td>0.13 <b>(+61.30%)</b></td><td>0.13 <b>(+35.69%)</b></td><td>0.12 <b>(+133.78%)</b></td><td>0.01 <b>(-48.97%)</b></td><td>276.10 <b>(-57.22%)</b></td><td>250.04 <b>(-43.71%)</b></td><td>257.50 <b>(-26.30%)</b></td><td>214.00 <b>(-30.63%)</b></td><td>25.15 <b>(-84.90%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>645.40 (n/a)</td><td>444.18 (n/a)</td><td>349.40 (n/a)</td><td>308.50 (n/a)</td><td>166.58 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.13 (+1.16%)</td><td>0.11 <b>(+32.72%)</b></td><td>0.11 <b>(+74.44%)</b></td><td>0.07 <b>(+79.35%)</b></td><td>0.02 <b>(-38.08%)</b></td><td>444.80 <b>(-44.24%)</b></td><td>323.90 <b>(-34.04%)</b></td><td>293.80 <b>(-42.68%)</b></td><td>248.10 (-1.16%)</td><td>78.97 <b>(-64.21%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>797.70 (n/a)</td><td>491.04 (n/a)</td><td>512.60 (n/a)</td><td>251.00 (n/a)</td><td>220.65 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.26 (-10.81%)</td><td>0.20 (+6.55%)</td><td>0.22 (+4.95%)</td><td>0.11 <b>(+208.97%)</b></td><td>0.06 <b>(-39.93%)</b></td><td>579.60 <b>(-67.63%)</b></td><td>353.72 <b>(-40.45%)</b></td><td>297.60 (-4.74%)</td><td>255.10 (+12.13%)</td><td>131.08 <b>(-80.44%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>0.09 (n/a)</td><td>1790.70 (n/a)</td><td>594.02 (n/a)</td><td>312.40 (n/a)</td><td>227.50 (n/a)</td><td>670.16 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.22 (-6.79%)</td><td>0.17 (-6.27%)</td><td>0.19 (-4.94%)</td><td>0.12 (+0.18%)</td><td>0.04 (-14.18%)</td><td>566.70 (-0.18%)</td><td>402.52 (+5.33%)</td><td>353.20 (+5.18%)</td><td>299.80 (+7.26%)</td><td>106.74 (-7.92%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>567.70 (n/a)</td><td>382.14 (n/a)</td><td>335.80 (n/a)</td><td>279.50 (n/a)</td><td>115.93 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.25 (-4.12%)</td><td>0.18 (+0.18%)</td><td>0.14 <b>(-22.99%)</b></td><td>0.13 (+14.06%)</td><td>0.06 (-5.48%)</td><td>508.50 (-12.33%)</td><td>397.08 (-2.27%)</td><td>458.70 <b>(+29.83%)</b></td><td>261.00 (+4.32%)</td><td>117.23 (-18.72%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>580.00 (n/a)</td><td>406.32 (n/a)</td><td>353.30 (n/a)</td><td>250.20 (n/a)</td><td>144.24 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.51 (+17.23%)</td><td>0.46 <b>(+59.88%)</b></td><td>0.50 <b>(+94.47%)</b></td><td>0.31 <b>(+48.90%)</b></td><td>0.08 (-4.69%)</td><td>421.80 <b>(-32.83%)</b></td><td>297.14 <b>(-39.02%)</b></td><td>263.40 <b>(-48.57%)</b></td><td>256.30 (-14.68%)</td><td>70.42 <b>(-41.08%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.44 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>628.00 (n/a)</td><td>487.26 (n/a)</td><td>512.20 (n/a)</td><td>300.40 (n/a)</td><td>119.52 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.50 (-2.62%)</td><td>0.33 (-10.53%)</td><td>0.43 <b>(+36.19%)</b></td><td>0.13 <b>(-50.52%)</b></td><td>0.18 <b>(+51.94%)</b></td><td>1037.00 <b>(+102.10%)</b></td><td>579.98 <b>(+49.51%)</b></td><td>308.40 <b>(-26.57%)</b></td><td>264.40 (+2.68%)</td><td>405.12 <b>(+240.49%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.51 (n/a)</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>513.10 (n/a)</td><td>387.92 (n/a)</td><td>420.00 (n/a)</td><td>257.50 (n/a)</td><td>118.98 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.51 <b>(+38.95%)</b></td><td>0.35 (+12.32%)</td><td>0.31 (+2.19%)</td><td>0.25 (-4.86%)</td><td>0.11 <b>(+148.62%)</b></td><td>533.60 (+5.10%)</td><td>408.56 (-5.26%)</td><td>428.40 (-2.15%)</td><td>258.40 <b>(-28.04%)</b></td><td>121.15 <b>(+92.77%)</b></td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>507.70 (n/a)</td><td>431.24 (n/a)</td><td>437.80 (n/a)</td><td>359.10 (n/a)</td><td>62.85 (n/a)</td>
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
<td><code>d3a2d45</code> — 2026-09-03 15:27:31</td><td>0.05 <b>(-38.37%)</b></td><td>0.03 <b>(-31.81%)</b></td><td>0.03 <b>(-29.64%)</b></td><td>0.03 <b>(-29.33%)</b></td><td>0.01 <b>(-50.75%)</b></td><td>646.80 <b>(+41.50%)</b></td><td>493.04 <b>(+40.90%)</b></td><td>487.70 <b>(+42.10%)</b></td><td>331.80 <b>(+62.25%)</b></td><td>113.20 (+7.08%)</td>
</tr>
<tr>
<td><code>0d9ebcd</code> — 2026-09-02 20:23:04</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>457.10 (n/a)</td><td>349.92 (n/a)</td><td>343.20 (n/a)</td><td>204.50 (n/a)</td><td>105.71 (n/a)</td>
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
