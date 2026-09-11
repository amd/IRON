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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 <b>(+26.42%)</b></td><td>0.02 (-15.62%)</td><td>0.01 <b>(-40.35%)</b></td><td>0.01 <b>(-39.93%)</b></td><td>0.01 <b>(+103.97%)</b></td><td>713.20 <b>(+66.48%)</b></td><td>458.82 <b>(+54.59%)</b></td><td>468.40 <b>(+67.64%)</b></td><td>155.40 <b>(-20.88%)</b></td><td>250.97 <b>(+182.99%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>428.40 (n/a)</td><td>296.80 (n/a)</td><td>279.40 (n/a)</td><td>196.40 (n/a)</td><td>88.69 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(-20.54%)</b></td><td>0.02 <b>(-32.40%)</b></td><td>0.02 <b>(-25.34%)</b></td><td>0.01 <b>(-56.36%)</b></td><td>0.00 <b>(+181.85%)</b></td><td>643.70 <b>(+129.16%)</b></td><td>405.92 <b>(+60.33%)</b></td><td>329.80 <b>(+33.96%)</b></td><td>298.60 <b>(+25.83%)</b></td><td>145.87 <b>(+704.05%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>280.90 (n/a)</td><td>253.18 (n/a)</td><td>246.20 (n/a)</td><td>237.30 (n/a)</td><td>18.14 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(-28.00%)</b></td><td>0.02 (-13.55%)</td><td>0.02 (-5.65%)</td><td>0.01 (+17.89%)</td><td>0.01 <b>(-37.73%)</b></td><td>563.30 (-15.18%)</td><td>356.30 (+5.00%)</td><td>286.60 (+5.99%)</td><td>260.60 <b>(+38.91%)</b></td><td>127.98 <b>(-32.25%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>664.10 (n/a)</td><td>339.34 (n/a)</td><td>270.40 (n/a)</td><td>187.60 (n/a)</td><td>188.90 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (+0.87%)</td><td>0.02 <b>(-21.74%)</b></td><td>0.01 <b>(-48.74%)</b></td><td>0.01 <b>(-50.86%)</b></td><td>0.01 <b>(+45.59%)</b></td><td>896.10 <b>(+103.52%)</b></td><td>474.88 <b>(+54.33%)</b></td><td>484.20 <b>(+95.08%)</b></td><td>223.90 (-0.84%)</td><td>275.12 <b>(+169.09%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>440.30 (n/a)</td><td>307.70 (n/a)</td><td>248.20 (n/a)</td><td>225.80 (n/a)</td><td>102.24 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+6.68%)</td><td>0.02 (+12.80%)</td><td>0.02 (-8.06%)</td><td>0.01 <b>(+321.54%)</b></td><td>0.00 <b>(-51.53%)</b></td><td>444.30 <b>(-76.27%)</b></td><td>362.40 <b>(-43.65%)</b></td><td>348.00 (+8.75%)</td><td>284.50 (-6.26%)</td><td>72.85 <b>(-89.42%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1872.70 (n/a)</td><td>643.18 (n/a)</td><td>320.00 (n/a)</td><td>303.50 (n/a)</td><td>688.77 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (+7.42%)</td><td>0.02 <b>(+24.12%)</b></td><td>0.02 <b>(+81.72%)</b></td><td>0.01 (+4.40%)</td><td>0.01 (+11.44%)</td><td>506.20 (-4.20%)</td><td>331.72 (-18.88%)</td><td>251.70 <b>(-44.97%)</b></td><td>230.10 (-6.88%)</td><td>124.94 (-3.71%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>528.40 (n/a)</td><td>408.90 (n/a)</td><td>457.40 (n/a)</td><td>247.10 (n/a)</td><td>129.75 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (+10.80%)</td><td>0.04 (+1.53%)</td><td>0.03 (-19.61%)</td><td>0.03 (+2.39%)</td><td>0.01 <b>(+26.98%)</b></td><td>446.60 (-2.32%)</td><td>352.68 (-0.05%)</td><td>395.30 <b>(+24.39%)</b></td><td>244.30 (-9.75%)</td><td>87.53 (+8.53%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>457.20 (n/a)</td><td>352.84 (n/a)</td><td>317.80 (n/a)</td><td>270.70 (n/a)</td><td>80.65 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (-6.61%)</td><td>0.03 (-14.52%)</td><td>0.03 <b>(-32.35%)</b></td><td>0.02 <b>(-30.54%)</b></td><td>0.01 (+16.05%)</td><td>625.90 <b>(+43.98%)</b></td><td>399.90 <b>(+23.04%)</b></td><td>411.70 <b>(+47.83%)</b></td><td>253.00 (+7.11%)</td><td>152.95 <b>(+62.39%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>434.70 (n/a)</td><td>325.02 (n/a)</td><td>278.50 (n/a)</td><td>236.20 (n/a)</td><td>94.19 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (+10.37%)</td><td>0.04 (+16.44%)</td><td>0.04 (-2.88%)</td><td>0.03 <b>(+37.61%)</b></td><td>0.01 <b>(-33.16%)</b></td><td>439.70 <b>(-27.33%)</b></td><td>298.78 <b>(-22.10%)</b></td><td>274.50 (+2.96%)</td><td>227.70 (-9.39%)</td><td>81.49 <b>(-52.40%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>605.10 (n/a)</td><td>383.52 (n/a)</td><td>266.60 (n/a)</td><td>251.30 (n/a)</td><td>171.20 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 <b>(+39.46%)</b></td><td>0.04 <b>(+55.94%)</b></td><td>0.05 <b>(+101.63%)</b></td><td>0.02 (+9.86%)</td><td>0.02 <b>(+87.53%)</b></td><td>597.20 (-8.98%)</td><td>333.84 <b>(-29.01%)</b></td><td>234.30 <b>(-50.40%)</b></td><td>199.40 <b>(-28.30%)</b></td><td>175.69 (+19.01%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>656.10 (n/a)</td><td>470.28 (n/a)</td><td>472.40 (n/a)</td><td>278.10 (n/a)</td><td>147.63 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (-9.62%)</td><td>0.03 (-15.90%)</td><td>0.03 <b>(-36.85%)</b></td><td>0.02 (-10.92%)</td><td>0.01 (-10.99%)</td><td>573.50 (+12.25%)</td><td>412.16 (+17.99%)</td><td>434.80 <b>(+58.34%)</b></td><td>258.90 (+10.64%)</td><td>138.54 (+4.75%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.90 (n/a)</td><td>349.32 (n/a)</td><td>274.60 (n/a)</td><td>234.00 (n/a)</td><td>132.26 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (+11.66%)</td><td>0.03 (+15.61%)</td><td>0.03 <b>(+28.17%)</b></td><td>0.01 <b>(+22.44%)</b></td><td>0.02 (+12.25%)</td><td>821.80 (-18.33%)</td><td>538.96 (-12.94%)</td><td>474.50 <b>(-21.98%)</b></td><td>233.40 (-10.44%)</td><td>237.44 (-10.23%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1006.20 (n/a)</td><td>619.10 (n/a)</td><td>608.20 (n/a)</td><td>260.60 (n/a)</td><td>264.51 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 <b>(-30.85%)</b></td><td>0.05 <b>(-31.06%)</b></td><td>0.06 <b>(-33.94%)</b></td><td>0.04 <b>(-20.41%)</b></td><td>0.01 <b>(-44.42%)</b></td><td>645.20 <b>(+25.65%)</b></td><td>465.20 <b>(+40.91%)</b></td><td>441.40 <b>(+51.37%)</b></td><td>352.20 <b>(+44.58%)</b></td><td>108.07 (+0.64%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>513.50 (n/a)</td><td>330.14 (n/a)</td><td>291.60 (n/a)</td><td>243.60 (n/a)</td><td>107.38 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 <b>(-35.49%)</b></td><td>0.08 (-19.19%)</td><td>0.10 (-3.03%)</td><td>0.04 (-12.39%)</td><td>0.03 <b>(-31.39%)</b></td><td>651.50 (+14.16%)</td><td>360.76 <b>(+20.13%)</b></td><td>258.00 (+3.12%)</td><td>242.80 <b>(+54.95%)</b></td><td>174.65 (+10.72%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>570.70 (n/a)</td><td>300.30 (n/a)</td><td>250.20 (n/a)</td><td>156.70 (n/a)</td><td>157.75 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.11 <b>(-44.40%)</b></td><td>0.07 <b>(-31.05%)</b></td><td>0.06 <b>(-29.42%)</b></td><td>0.04 <b>(-27.23%)</b></td><td>0.03 <b>(-51.62%)</b></td><td>605.60 <b>(+37.42%)</b></td><td>409.38 <b>(+34.34%)</b></td><td>440.90 <b>(+41.68%)</b></td><td>224.60 <b>(+79.82%)</b></td><td>150.60 (+19.61%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>440.70 (n/a)</td><td>304.74 (n/a)</td><td>311.20 (n/a)</td><td>124.90 (n/a)</td><td>125.91 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (-2.97%)</td><td>0.06 (-13.37%)</td><td>0.07 (+14.66%)</td><td>0.01 <b>(-81.67%)</b></td><td>0.03 <b>(+76.13%)</b></td><td>2390.90 <b>(+445.49%)</b></td><td>744.92 <b>(+109.05%)</b></td><td>329.40 (-12.79%)</td><td>262.50 (+3.06%)</td><td>921.77 <b>(+1017.36%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>438.30 (n/a)</td><td>356.34 (n/a)</td><td>377.70 (n/a)</td><td>254.70 (n/a)</td><td>82.50 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.12 (+1.99%)</td><td>0.07 (-0.58%)</td><td>0.05 (-8.18%)</td><td>0.04 (-4.83%)</td><td>0.03 (+10.64%)</td><td>589.40 (+5.08%)</td><td>440.18 (+4.50%)</td><td>542.50 (+8.91%)</td><td>211.20 (-1.95%)</td><td>180.65 (+16.57%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>560.90 (n/a)</td><td>421.24 (n/a)</td><td>498.10 (n/a)</td><td>215.40 (n/a)</td><td>154.97 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 <b>(-41.42%)</b></td><td>0.06 (-9.95%)</td><td>0.05 (+3.66%)</td><td>0.05 <b>(+32.94%)</b></td><td>0.01 <b>(-67.29%)</b></td><td>498.80 <b>(-24.77%)</b></td><td>438.74 (-7.61%)</td><td>478.90 (-3.53%)</td><td>296.50 <b>(+70.70%)</b></td><td>84.10 <b>(-54.02%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>663.00 (n/a)</td><td>474.86 (n/a)</td><td>496.40 (n/a)</td><td>173.70 (n/a)</td><td>182.89 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.21 (+1.80%)</td><td>0.16 (+6.08%)</td><td>0.17 <b>(+21.48%)</b></td><td>0.10 (+1.76%)</td><td>0.04 (+12.06%)</td><td>470.70 (-1.73%)</td><td>329.32 (-4.51%)</td><td>284.20 (-17.67%)</td><td>236.10 (-1.75%)</td><td>100.47 (+9.31%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>479.00 (n/a)</td><td>344.86 (n/a)</td><td>345.20 (n/a)</td><td>240.30 (n/a)</td><td>91.91 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.22 (+6.22%)</td><td>0.15 (-11.27%)</td><td>0.15 <b>(-26.31%)</b></td><td>0.09 (+16.58%)</td><td>0.05 (-12.65%)</td><td>577.10 (-14.22%)</td><td>355.84 (+5.85%)</td><td>333.60 <b>(+35.72%)</b></td><td>220.20 (-5.86%)</td><td>133.27 <b>(-29.54%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.20 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>672.80 (n/a)</td><td>336.18 (n/a)</td><td>245.80 (n/a)</td><td>233.90 (n/a)</td><td>189.13 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.25 (+13.05%)</td><td>0.14 (-4.04%)</td><td>0.11 <b>(-20.37%)</b></td><td>0.08 (-19.34%)</td><td>0.07 <b>(+30.11%)</b></td><td>605.90 <b>(+23.96%)</b></td><td>404.96 (+11.28%)</td><td>462.40 <b>(+25.58%)</b></td><td>194.50 (-11.55%)</td><td>164.48 <b>(+34.79%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>488.80 (n/a)</td><td>363.92 (n/a)</td><td>368.20 (n/a)</td><td>219.90 (n/a)</td><td>122.02 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.21 (-6.43%)</td><td>0.12 (-7.58%)</td><td>0.10 (-5.30%)</td><td>0.09 (+11.20%)</td><td>0.05 (-11.78%)</td><td>533.20 (-10.07%)</td><td>436.34 (+5.24%)</td><td>474.30 (+5.59%)</td><td>230.80 (+6.90%)</td><td>117.91 (-17.43%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.23 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>592.90 (n/a)</td><td>414.62 (n/a)</td><td>449.20 (n/a)</td><td>215.90 (n/a)</td><td>142.79 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.21 (-8.53%)</td><td>0.13 <b>(-20.78%)</b></td><td>0.11 <b>(-35.06%)</b></td><td>0.09 (-14.24%)</td><td>0.05 (-8.81%)</td><td>561.90 (+16.60%)</td><td>418.88 <b>(+26.17%)</b></td><td>448.10 <b>(+53.99%)</b></td><td>228.90 (+9.31%)</td><td>131.17 (+10.39%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>481.90 (n/a)</td><td>332.00 (n/a)</td><td>291.00 (n/a)</td><td>209.40 (n/a)</td><td>118.83 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.23 (+12.03%)</td><td>0.17 (-0.19%)</td><td>0.18 (-0.07%)</td><td>0.09 (-18.03%)</td><td>0.06 <b>(+28.14%)</b></td><td>559.80 <b>(+21.99%)</b></td><td>331.36 (+5.24%)</td><td>275.10 (+0.07%)</td><td>210.70 (-10.72%)</td><td>137.65 <b>(+46.76%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>458.90 (n/a)</td><td>314.86 (n/a)</td><td>274.90 (n/a)</td><td>236.00 (n/a)</td><td>93.79 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (-11.58%)</td><td>0.01 (+13.00%)</td><td>0.01 <b>(+37.18%)</b></td><td>0.01 <b>(+41.00%)</b></td><td>0.00 <b>(-40.06%)</b></td><td>416.50 <b>(-29.08%)</b></td><td>316.88 (-19.25%)</td><td>292.90 <b>(-27.12%)</b></td><td>244.50 (+13.09%)</td><td>74.17 <b>(-51.23%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>587.30 (n/a)</td><td>392.44 (n/a)</td><td>401.90 (n/a)</td><td>216.20 (n/a)</td><td>152.07 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (-4.85%)</td><td>0.01 (-5.64%)</td><td>0.01 (-14.56%)</td><td>0.00 (-0.72%)</td><td>0.00 (-19.08%)</td><td>568.10 (+0.73%)</td><td>349.38 (+1.93%)</td><td>275.70 (+17.07%)</td><td>241.90 (+5.08%)</td><td>138.54 (-10.66%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>564.00 (n/a)</td><td>342.78 (n/a)</td><td>235.50 (n/a)</td><td>230.20 (n/a)</td><td>155.07 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (+1.49%)</td><td>0.01 (+0.94%)</td><td>0.01 (+2.22%)</td><td>0.01 (+1.73%)</td><td>0.00 (+4.82%)</td><td>380.40 (-1.68%)</td><td>303.86 (-0.61%)</td><td>292.20 (-2.18%)</td><td>225.40 (-1.49%)</td><td>67.89 (+3.42%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>386.90 (n/a)</td><td>305.74 (n/a)</td><td>298.70 (n/a)</td><td>228.80 (n/a)</td><td>65.64 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(+62.02%)</b></td><td>0.01 <b>(+66.39%)</b></td><td>0.01 <b>(+85.66%)</b></td><td>0.01 <b>(+69.14%)</b></td><td>0.00 <b>(+64.23%)</b></td><td>476.40 <b>(-40.87%)</b></td><td>328.34 <b>(-39.03%)</b></td><td>290.10 <b>(-46.14%)</b></td><td>149.70 <b>(-38.29%)</b></td><td>133.97 <b>(-33.27%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>805.70 (n/a)</td><td>538.50 (n/a)</td><td>538.60 (n/a)</td><td>242.60 (n/a)</td><td>200.78 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 <b>(+26.24%)</b></td><td>0.01 <b>(+22.40%)</b></td><td>0.01 <b>(+71.19%)</b></td><td>0.01 (+3.59%)</td><td>0.00 <b>(+25.88%)</b></td><td>514.00 (-3.46%)</td><td>331.00 (-16.22%)</td><td>262.60 <b>(-41.58%)</b></td><td>198.00 <b>(-20.77%)</b></td><td>132.83 (+3.29%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>532.40 (n/a)</td><td>395.08 (n/a)</td><td>449.50 (n/a)</td><td>249.90 (n/a)</td><td>128.60 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (+13.62%)</td><td>0.01 (+1.60%)</td><td>0.01 (+1.10%)</td><td>0.00 (-13.00%)</td><td>0.00 (+15.26%)</td><td>636.60 (+14.93%)</td><td>431.70 (+1.25%)</td><td>482.70 (-1.09%)</td><td>232.90 (-11.98%)</td><td>163.98 (+14.41%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>553.90 (n/a)</td><td>426.36 (n/a)</td><td>488.00 (n/a)</td><td>264.60 (n/a)</td><td>143.33 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+17.34%)</td><td>0.02 (+0.63%)</td><td>0.02 (-6.67%)</td><td>0.00 <b>(-69.34%)</b></td><td>0.01 <b>(+71.04%)</b></td><td>2052.70 <b>(+226.19%)</b></td><td>656.50 <b>(+68.71%)</b></td><td>314.70 (+7.15%)</td><td>232.60 (-14.77%)</td><td>784.83 <b>(+411.56%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>629.30 (n/a)</td><td>389.14 (n/a)</td><td>293.70 (n/a)</td><td>272.90 (n/a)</td><td>153.42 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+15.07%)</td><td>0.02 (+7.00%)</td><td>0.02 <b>(+26.85%)</b></td><td>0.01 (-4.39%)</td><td>0.01 <b>(+20.95%)</b></td><td>496.00 (+4.60%)</td><td>347.88 (-4.27%)</td><td>289.50 <b>(-21.16%)</b></td><td>230.70 (-13.11%)</td><td>114.93 (+18.06%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>474.20 (n/a)</td><td>363.40 (n/a)</td><td>367.20 (n/a)</td><td>265.50 (n/a)</td><td>97.35 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+17.34%)</td><td>0.02 <b>(+42.49%)</b></td><td>0.02 <b>(+114.97%)</b></td><td>0.01 (+10.44%)</td><td>0.01 <b>(+33.40%)</b></td><td>575.10 (-9.46%)</td><td>349.34 <b>(-27.90%)</b></td><td>256.50 <b>(-53.49%)</b></td><td>240.60 (-14.80%)</td><td>150.16 (-3.27%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>635.20 (n/a)</td><td>484.54 (n/a)</td><td>551.50 (n/a)</td><td>282.40 (n/a)</td><td>155.23 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+8.78%)</td><td>0.01 (-5.02%)</td><td>0.01 (+0.88%)</td><td>0.01 <b>(-28.36%)</b></td><td>0.01 <b>(+42.03%)</b></td><td>777.60 <b>(+39.61%)</b></td><td>523.70 (+14.51%)</td><td>498.80 (-0.85%)</td><td>268.80 (-8.07%)</td><td>207.55 <b>(+81.75%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>557.00 (n/a)</td><td>457.34 (n/a)</td><td>503.10 (n/a)</td><td>292.40 (n/a)</td><td>114.19 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (-14.71%)</td><td>0.01 (-3.96%)</td><td>0.01 (-4.83%)</td><td>0.01 <b>(+74.47%)</b></td><td>0.00 <b>(-43.34%)</b></td><td>624.00 <b>(-42.68%)</b></td><td>498.70 (-10.66%)</td><td>514.40 (+5.07%)</td><td>345.50 (+17.24%)</td><td>119.54 <b>(-62.18%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1088.70 (n/a)</td><td>558.18 (n/a)</td><td>489.60 (n/a)</td><td>294.70 (n/a)</td><td>316.06 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+1.90%)</td><td>0.01 (+2.66%)</td><td>0.01 (-13.38%)</td><td>0.01 (+14.25%)</td><td>0.00 (-4.83%)</td><td>571.10 (-12.46%)</td><td>453.34 (-3.94%)</td><td>488.80 (+15.45%)</td><td>306.80 (-1.86%)</td><td>104.58 <b>(-20.09%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>652.40 (n/a)</td><td>471.94 (n/a)</td><td>423.40 (n/a)</td><td>312.60 (n/a)</td><td>130.87 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (+1.42%)</td><td>0.03 (-19.15%)</td><td>0.03 <b>(-28.95%)</b></td><td>0.02 (-2.97%)</td><td>0.01 (+0.12%)</td><td>561.70 (+3.06%)</td><td>381.76 <b>(+23.71%)</b></td><td>339.30 <b>(+40.73%)</b></td><td>225.40 (-1.40%)</td><td>137.30 (+2.01%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>545.00 (n/a)</td><td>308.60 (n/a)</td><td>241.10 (n/a)</td><td>228.60 (n/a)</td><td>134.60 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 <b>(+43.40%)</b></td><td>0.03 <b>(+29.50%)</b></td><td>0.02 (+4.59%)</td><td>0.02 <b>(+216.63%)</b></td><td>0.02 (+9.63%)</td><td>580.80 <b>(-68.42%)</b></td><td>393.36 <b>(-44.72%)</b></td><td>438.30 (-4.38%)</td><td>175.90 <b>(-30.25%)</b></td><td>157.03 <b>(-76.17%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1839.10 (n/a)</td><td>711.60 (n/a)</td><td>458.40 (n/a)</td><td>252.20 (n/a)</td><td>658.95 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 <b>(+80.03%)</b></td><td>0.03 <b>(+26.28%)</b></td><td>0.02 (+9.75%)</td><td>0.01 <b>(-68.26%)</b></td><td>0.03 <b>(+156.77%)</b></td><td>1893.70 <b>(+215.04%)</b></td><td>667.06 <b>(+40.54%)</b></td><td>434.10 (-8.88%)</td><td>135.40 <b>(-44.44%)</b></td><td>697.93 <b>(+385.48%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>601.10 (n/a)</td><td>474.64 (n/a)</td><td>476.40 (n/a)</td><td>243.70 (n/a)</td><td>143.76 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (+19.28%)</td><td>0.03 (+7.44%)</td><td>0.02 (+6.80%)</td><td>0.02 <b>(+33.24%)</b></td><td>0.01 (+15.13%)</td><td>599.70 <b>(-24.95%)</b></td><td>439.48 (-9.39%)</td><td>456.50 (-6.38%)</td><td>227.10 (-16.14%)</td><td>133.88 <b>(-33.52%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>799.10 (n/a)</td><td>485.00 (n/a)</td><td>487.60 (n/a)</td><td>270.80 (n/a)</td><td>201.37 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-18.78%)</td><td>0.02 (-14.72%)</td><td>0.02 (+7.92%)</td><td>0.02 (+3.69%)</td><td>0.01 <b>(-40.97%)</b></td><td>614.60 (-3.56%)</td><td>468.16 (+8.82%)</td><td>421.40 (-7.34%)</td><td>306.10 <b>(+23.13%)</b></td><td>131.35 <b>(-23.00%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>637.30 (n/a)</td><td>430.20 (n/a)</td><td>454.80 (n/a)</td><td>248.60 (n/a)</td><td>170.59 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (+8.95%)</td><td>0.03 <b>(+24.42%)</b></td><td>0.03 <b>(+57.32%)</b></td><td>0.02 <b>(+22.03%)</b></td><td>0.01 (-7.04%)</td><td>525.80 (-18.05%)</td><td>364.52 <b>(-23.15%)</b></td><td>336.70 <b>(-36.45%)</b></td><td>221.80 (-8.23%)</td><td>117.07 <b>(-30.11%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>641.60 (n/a)</td><td>474.30 (n/a)</td><td>529.80 (n/a)</td><td>241.70 (n/a)</td><td>167.50 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (+9.23%)</td><td>0.07 (+19.51%)</td><td>0.07 (+17.87%)</td><td>0.05 <b>(+57.68%)</b></td><td>0.01 <b>(-34.90%)</b></td><td>409.00 <b>(-36.58%)</b></td><td>305.18 <b>(-21.90%)</b></td><td>289.00 (-15.17%)</td><td>256.30 (-8.43%)</td><td>59.90 <b>(-60.39%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>644.90 (n/a)</td><td>390.74 (n/a)</td><td>340.70 (n/a)</td><td>279.90 (n/a)</td><td>151.24 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (-8.83%)</td><td>0.06 (+4.51%)</td><td>0.06 <b>(+23.13%)</b></td><td>0.04 (+1.09%)</td><td>0.02 (-8.02%)</td><td>576.80 (-1.08%)</td><td>387.06 (-5.75%)</td><td>375.80 (-18.80%)</td><td>247.90 (+9.64%)</td><td>144.97 (-4.42%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>583.10 (n/a)</td><td>410.66 (n/a)</td><td>462.80 (n/a)</td><td>226.10 (n/a)</td><td>151.68 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (-6.61%)</td><td>0.07 (+1.17%)</td><td>0.08 (+7.42%)</td><td>0.06 (+0.69%)</td><td>0.01 <b>(-30.97%)</b></td><td>333.50 (-0.68%)</td><td>282.78 (-1.87%)</td><td>274.60 (-6.88%)</td><td>261.50 (+7.08%)</td><td>29.60 <b>(-24.88%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>335.80 (n/a)</td><td>288.18 (n/a)</td><td>294.90 (n/a)</td><td>244.20 (n/a)</td><td>39.40 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (+4.05%)</td><td>0.07 <b>(+21.36%)</b></td><td>0.07 <b>(+52.12%)</b></td><td>0.04 <b>(+33.61%)</b></td><td>0.02 (-3.73%)</td><td>493.80 <b>(-25.16%)</b></td><td>338.86 <b>(-20.43%)</b></td><td>288.40 <b>(-34.26%)</b></td><td>236.40 (-3.86%)</td><td>115.13 <b>(-29.47%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>659.80 (n/a)</td><td>425.84 (n/a)</td><td>438.70 (n/a)</td><td>245.90 (n/a)</td><td>163.24 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 <b>(+109.78%)</b></td><td>0.08 <b>(+71.27%)</b></td><td>0.09 <b>(+106.83%)</b></td><td>0.04 (-5.77%)</td><td>0.04 <b>(+262.54%)</b></td><td>566.90 (+6.12%)</td><td>326.16 <b>(-30.67%)</b></td><td>244.80 <b>(-51.65%)</b></td><td>154.30 <b>(-52.35%)</b></td><td>166.53 <b>(+93.09%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>534.20 (n/a)</td><td>470.44 (n/a)</td><td>506.30 (n/a)</td><td>323.80 (n/a)</td><td>86.25 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (+19.56%)</td><td>0.06 (+3.19%)</td><td>0.05 (-10.73%)</td><td>0.04 (-9.78%)</td><td>0.02 <b>(+53.84%)</b></td><td>536.30 (+10.85%)</td><td>396.14 (+0.48%)</td><td>434.10 (+12.00%)</td><td>254.20 (-16.35%)</td><td>111.68 <b>(+38.04%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>483.80 (n/a)</td><td>394.24 (n/a)</td><td>387.60 (n/a)</td><td>303.90 (n/a)</td><td>80.90 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>467.70 (n/a)</td><td>363.62 (n/a)</td><td>402.30 (n/a)</td><td>236.40 (n/a)</td><td>101.88 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1068.60 (n/a)</td><td>525.24 (n/a)</td><td>409.30 (n/a)</td><td>269.00 (n/a)</td><td>328.35 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>498.70 (n/a)</td><td>412.42 (n/a)</td><td>448.30 (n/a)</td><td>284.70 (n/a)</td><td>84.99 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>461.40 (n/a)</td><td>381.26 (n/a)</td><td>396.90 (n/a)</td><td>269.00 (n/a)</td><td>81.89 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>616.30 (n/a)</td><td>384.10 (n/a)</td><td>256.90 (n/a)</td><td>237.50 (n/a)</td><td>184.85 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>439.30 (n/a)</td><td>322.18 (n/a)</td><td>293.20 (n/a)</td><td>271.90 (n/a)</td><td>68.69 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>553.50 (n/a)</td><td>413.06 (n/a)</td><td>485.10 (n/a)</td><td>242.10 (n/a)</td><td>155.91 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>405.80 (n/a)</td><td>299.90 (n/a)</td><td>299.20 (n/a)</td><td>212.30 (n/a)</td><td>70.00 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>495.10 (n/a)</td><td>408.84 (n/a)</td><td>464.20 (n/a)</td><td>152.90 (n/a)</td><td>144.31 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.24 <b>(+21.59%)</b></td><td>0.16 (+16.66%)</td><td>0.19 <b>(+45.93%)</b></td><td>0.09 (+12.87%)</td><td>0.06 (+17.85%)</td><td>546.30 (-11.40%)</td><td>348.86 (-12.86%)</td><td>265.10 <b>(-31.48%)</b></td><td>206.50 (-17.79%)</td><td>152.02 (-4.08%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>616.60 (n/a)</td><td>400.36 (n/a)</td><td>386.90 (n/a)</td><td>251.20 (n/a)</td><td>158.48 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.29 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>715.30 (n/a)</td><td>417.46 (n/a)</td><td>442.50 (n/a)</td><td>169.10 (n/a)</td><td>218.61 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>570.30 (n/a)</td><td>426.72 (n/a)</td><td>481.30 (n/a)</td><td>231.30 (n/a)</td><td>134.21 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>543.90 (n/a)</td><td>350.80 (n/a)</td><td>271.70 (n/a)</td><td>210.70 (n/a)</td><td>157.76 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>449.70 (n/a)</td><td>290.62 (n/a)</td><td>237.30 (n/a)</td><td>234.80 (n/a)</td><td>92.53 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>678.80 (n/a)</td><td>522.12 (n/a)</td><td>576.00 (n/a)</td><td>281.70 (n/a)</td><td>166.74 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>371.60 (n/a)</td><td>299.68 (n/a)</td><td>301.70 (n/a)</td><td>250.40 (n/a)</td><td>45.76 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>516.10 (n/a)</td><td>373.38 (n/a)</td><td>354.20 (n/a)</td><td>282.10 (n/a)</td><td>97.80 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>688.10 (n/a)</td><td>491.28 (n/a)</td><td>493.30 (n/a)</td><td>291.20 (n/a)</td><td>140.36 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>720.90 (n/a)</td><td>464.66 (n/a)</td><td>500.10 (n/a)</td><td>259.90 (n/a)</td><td>186.86 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>538.70 (n/a)</td><td>392.76 (n/a)</td><td>421.80 (n/a)</td><td>231.00 (n/a)</td><td>132.37 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>473.50 (n/a)</td><td>359.34 (n/a)</td><td>312.90 (n/a)</td><td>266.30 (n/a)</td><td>98.78 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>565.10 (n/a)</td><td>397.54 (n/a)</td><td>359.70 (n/a)</td><td>250.80 (n/a)</td><td>147.04 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>625.10 (n/a)</td><td>366.26 (n/a)</td><td>289.80 (n/a)</td><td>247.00 (n/a)</td><td>161.48 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>4.41 (+1.92%)</td><td>3.35 (+1.63%)</td><td>3.17 (-9.66%)</td><td>2.46 <b>(+34.67%)</b></td><td>0.71 <b>(-22.11%)</b></td><td>4265.80 <b>(-25.74%)</b></td><td>3242.28 (-6.34%)</td><td>3306.70 (+10.69%)</td><td>2378.90 (-1.88%)</td><td>689.32 <b>(-47.36%)</b></td><td>1805.42 (+1.92%)</td><td>1373.30 (+1.63%)</td><td>1298.85 (-9.66%)</td><td>1006.84 <b>(+34.67%)</b></td><td>292.30 <b>(-22.11%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.32 (n/a)</td><td>3.30 (n/a)</td><td>3.51 (n/a)</td><td>1.83 (n/a)</td><td>0.92 (n/a)</td><td>5744.60 (n/a)</td><td>3461.72 (n/a)</td><td>2987.40 (n/a)</td><td>2424.50 (n/a)</td><td>1309.51 (n/a)</td><td>1771.49 (n/a)</td><td>1351.33 (n/a)</td><td>1437.68 (n/a)</td><td>747.65 (n/a)</td><td>375.29 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.60 (+6.72%)</td><td>3.13 (+1.95%)</td><td>3.10 (+2.75%)</td><td>2.65 (-2.12%)</td><td>0.34 <b>(+27.99%)</b></td><td>8886.50 (+2.16%)</td><td>7599.52 (-1.57%)</td><td>7622.50 (-2.68%)</td><td>6555.40 (-6.30%)</td><td>845.18 <b>(+24.24%)</b></td><td>2047.44 (+6.72%)</td><td>1783.24 (+1.95%)</td><td>1760.81 (+2.75%)</td><td>1510.36 (-2.12%)</td><td>193.39 <b>(+27.99%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.37 (n/a)</td><td>3.07 (n/a)</td><td>3.01 (n/a)</td><td>2.71 (n/a)</td><td>0.27 (n/a)</td><td>8698.30 (n/a)</td><td>7720.40 (n/a)</td><td>7832.20 (n/a)</td><td>6996.10 (n/a)</td><td>680.27 (n/a)</td><td>1918.47 (n/a)</td><td>1749.11 (n/a)</td><td>1713.66 (n/a)</td><td>1543.04 (n/a)</td><td>151.10 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>4.13 (+15.67%)</td><td>3.34 (-2.79%)</td><td>3.22 (-6.85%)</td><td>2.80 (-14.08%)</td><td>0.54 <b>(+389.10%)</b></td><td>5985.50 (+16.39%)</td><td>5116.92 (+4.85%)</td><td>5204.20 (+7.36%)</td><td>4065.90 (-13.55%)</td><td>785.89 <b>(+389.93%)</b></td><td>2112.67 (+15.67%)</td><td>1712.54 (-2.79%)</td><td>1650.58 (-6.85%)</td><td>1435.11 (-14.08%)</td><td>276.74 <b>(+389.10%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.57 (n/a)</td><td>3.44 (n/a)</td><td>3.46 (n/a)</td><td>3.26 (n/a)</td><td>0.11 (n/a)</td><td>5142.70 (n/a)</td><td>4880.16 (n/a)</td><td>4847.60 (n/a)</td><td>4703.10 (n/a)</td><td>160.41 (n/a)</td><td>1826.45 (n/a)</td><td>1761.67 (n/a)</td><td>1772.00 (n/a)</td><td>1670.32 (n/a)</td><td>56.58 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.27 (+13.11%)</td><td>0.96 (-3.77%)</td><td>0.88 (-13.36%)</td><td>0.73 (-11.82%)</td><td>0.23 <b>(+112.29%)</b></td><td>631.40 (+13.42%)</td><td>501.28 (+7.53%)</td><td>523.30 (+15.42%)</td><td>361.70 (-11.59%)</td><td>114.11 <b>(+107.26%)</b></td><td>92.78 (+13.11%)</td><td>69.98 (-3.77%)</td><td>64.12 (-13.36%)</td><td>53.14 (-11.82%)</td><td>16.88 <b>(+112.29%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.12 (n/a)</td><td>0.99 (n/a)</td><td>1.01 (n/a)</td><td>0.82 (n/a)</td><td>0.11 (n/a)</td><td>556.70 (n/a)</td><td>466.18 (n/a)</td><td>453.40 (n/a)</td><td>409.10 (n/a)</td><td>55.05 (n/a)</td><td>82.03 (n/a)</td><td>72.72 (n/a)</td><td>74.01 (n/a)</td><td>60.27 (n/a)</td><td>7.95 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.89 (+2.92%)</td><td>1.02 <b>(-25.67%)</b></td><td>1.02 <b>(-28.03%)</b></td><td>0.19 <b>(-79.08%)</b></td><td>0.61 <b>(+70.32%)</b></td><td>3446.40 <b>(+377.94%)</b></td><td>1155.78 <b>(+127.25%)</b></td><td>645.40 <b>(+38.95%)</b></td><td>346.60 (-2.83%)</td><td>1288.92 <b>(+807.97%)</b></td><td>193.61 (+2.92%)</td><td>103.99 <b>(-25.67%)</b></td><td>103.98 <b>(-28.03%)</b></td><td>19.47 <b>(-79.08%)</b></td><td>62.16 <b>(+70.32%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.84 (n/a)</td><td>1.37 (n/a)</td><td>1.41 (n/a)</td><td>0.91 (n/a)</td><td>0.36 (n/a)</td><td>721.10 (n/a)</td><td>508.60 (n/a)</td><td>464.50 (n/a)</td><td>356.70 (n/a)</td><td>141.96 (n/a)</td><td>188.12 (n/a)</td><td>139.91 (n/a)</td><td>144.49 (n/a)</td><td>93.07 (n/a)</td><td>36.49 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.79 (+6.36%)</td><td>1.36 <b>(+20.22%)</b></td><td>1.42 <b>(+28.83%)</b></td><td>1.03 <b>(+59.13%)</b></td><td>0.30 <b>(-26.52%)</b></td><td>734.30 <b>(-37.16%)</b></td><td>576.80 <b>(-22.88%)</b></td><td>529.80 <b>(-22.38%)</b></td><td>421.10 (-5.96%)</td><td>127.62 <b>(-55.83%)</b></td><td>199.23 (+6.36%)</td><td>151.36 <b>(+20.22%)</b></td><td>158.34 <b>(+28.83%)</b></td><td>114.24 <b>(+59.13%)</b></td><td>33.92 <b>(-26.52%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.68 (n/a)</td><td>1.13 (n/a)</td><td>1.10 (n/a)</td><td>0.64 (n/a)</td><td>0.41 (n/a)</td><td>1168.50 (n/a)</td><td>747.90 (n/a)</td><td>682.60 (n/a)</td><td>447.80 (n/a)</td><td>288.93 (n/a)</td><td>187.31 (n/a)</td><td>125.90 (n/a)</td><td>122.90 (n/a)</td><td>71.79 (n/a)</td><td>46.16 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.71 (+7.43%)</td><td>1.14 (-8.65%)</td><td>1.20 (+0.64%)</td><td>0.30 <b>(-68.92%)</b></td><td>0.60 <b>(+153.13%)</b></td><td>3514.00 <b>(+221.79%)</b></td><td>1383.10 <b>(+60.25%)</b></td><td>876.60 (-0.62%)</td><td>613.20 (-6.91%)</td><td>1222.97 <b>(+653.30%)</b></td><td>218.89 (+7.43%)</td><td>146.19 (-8.65%)</td><td>153.12 (+0.64%)</td><td>38.20 <b>(-68.92%)</b></td><td>77.14 <b>(+153.13%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.59 (n/a)</td><td>1.25 (n/a)</td><td>1.19 (n/a)</td><td>0.96 (n/a)</td><td>0.24 (n/a)</td><td>1092.00 (n/a)</td><td>863.08 (n/a)</td><td>882.10 (n/a)</td><td>658.70 (n/a)</td><td>162.35 (n/a)</td><td>203.75 (n/a)</td><td>160.03 (n/a)</td><td>152.15 (n/a)</td><td>122.91 (n/a)</td><td>30.48 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.12 (+10.39%)</td><td>1.32 <b>(-20.25%)</b></td><td>1.50 (-15.70%)</td><td>0.30 <b>(-72.56%)</b></td><td>0.74 <b>(+122.09%)</b></td><td>3538.20 <b>(+264.46%)</b></td><td>1301.30 <b>(+97.02%)</b></td><td>697.50 (+18.60%)</td><td>495.00 (-9.42%)</td><td>1279.96 <b>(+631.28%)</b></td><td>271.15 (+10.39%)</td><td>169.19 <b>(-20.25%)</b></td><td>192.42 (-15.70%)</td><td>37.93 <b>(-72.56%)</b></td><td>94.13 <b>(+122.09%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.92 (n/a)</td><td>1.66 (n/a)</td><td>1.78 (n/a)</td><td>1.08 (n/a)</td><td>0.33 (n/a)</td><td>970.80 (n/a)</td><td>660.50 (n/a)</td><td>588.10 (n/a)</td><td>546.50 (n/a)</td><td>175.03 (n/a)</td><td>245.61 (n/a)</td><td>212.16 (n/a)</td><td>228.24 (n/a)</td><td>138.25 (n/a)</td><td>42.38 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.03 (-10.80%)</td><td>1.41 (+10.00%)</td><td>1.35 (+13.20%)</td><td>0.94 <b>(+210.99%)</b></td><td>0.39 <b>(-44.97%)</b></td><td>1110.90 <b>(-67.84%)</b></td><td>788.82 <b>(-38.56%)</b></td><td>775.40 (-11.67%)</td><td>515.40 (+12.09%)</td><td>211.91 <b>(-82.73%)</b></td><td>260.41 (-10.80%)</td><td>180.50 (+10.00%)</td><td>173.09 (+13.20%)</td><td>120.82 <b>(+210.99%)</b></td><td>50.25 <b>(-44.97%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>2.28 (n/a)</td><td>1.28 (n/a)</td><td>1.19 (n/a)</td><td>0.30 (n/a)</td><td>0.71 (n/a)</td><td>3454.60 (n/a)</td><td>1283.94 (n/a)</td><td>877.80 (n/a)</td><td>459.80 (n/a)</td><td>1227.32 (n/a)</td><td>291.93 (n/a)</td><td>164.09 (n/a)</td><td>152.91 (n/a)</td><td>38.85 (n/a)</td><td>91.32 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.90 (-4.29%)</td><td>1.07 <b>(-35.59%)</b></td><td>1.04 <b>(-45.32%)</b></td><td>0.43 <b>(-53.55%)</b></td><td>0.53 (+19.72%)</td><td>2458.90 <b>(+115.30%)</b></td><td>1227.30 <b>(+79.17%)</b></td><td>1009.10 <b>(+82.91%)</b></td><td>552.30 (+4.48%)</td><td>723.19 <b>(+177.66%)</b></td><td>243.03 (-4.29%)</td><td>137.20 <b>(-35.59%)</b></td><td>133.01 <b>(-45.32%)</b></td><td>54.58 <b>(-53.55%)</b></td><td>67.89 (+19.72%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.98 (n/a)</td><td>1.66 (n/a)</td><td>1.90 (n/a)</td><td>0.92 (n/a)</td><td>0.44 (n/a)</td><td>1142.10 (n/a)</td><td>684.98 (n/a)</td><td>551.70 (n/a)</td><td>528.60 (n/a)</td><td>260.46 (n/a)</td><td>253.93 (n/a)</td><td>213.00 (n/a)</td><td>243.26 (n/a)</td><td>117.51 (n/a)</td><td>56.71 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.87 (+10.99%)</td><td>1.36 (-0.78%)</td><td>1.29 (-9.30%)</td><td>0.89 (-6.07%)</td><td>0.36 <b>(+23.94%)</b></td><td>1179.50 (+6.46%)</td><td>817.86 (+2.65%)</td><td>810.10 (+10.26%)</td><td>560.90 (-9.90%)</td><td>232.03 (+19.05%)</td><td>239.29 (+10.99%)</td><td>174.35 (-0.78%)</td><td>165.68 (-9.30%)</td><td>113.79 (-6.07%)</td><td>46.62 <b>(+23.94%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.68 (n/a)</td><td>1.37 (n/a)</td><td>1.43 (n/a)</td><td>0.95 (n/a)</td><td>0.29 (n/a)</td><td>1107.90 (n/a)</td><td>796.76 (n/a)</td><td>734.70 (n/a)</td><td>622.50 (n/a)</td><td>194.89 (n/a)</td><td>215.60 (n/a)</td><td>175.71 (n/a)</td><td>182.67 (n/a)</td><td>121.14 (n/a)</td><td>37.61 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.57 (-10.64%)</td><td>1.07 (-3.21%)</td><td>1.09 (-4.55%)</td><td>0.49 (-5.83%)</td><td>0.51 (-10.56%)</td><td>2128.50 (+6.20%)</td><td>1228.24 (-0.51%)</td><td>965.90 (+4.76%)</td><td>666.20 (+11.91%)</td><td>659.84 (-5.88%)</td><td>201.45 (-10.64%)</td><td>136.50 (-3.21%)</td><td>138.96 (-4.55%)</td><td>63.06 (-5.83%)</td><td>65.39 (-10.56%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.76 (n/a)</td><td>1.10 (n/a)</td><td>1.14 (n/a)</td><td>0.52 (n/a)</td><td>0.57 (n/a)</td><td>2004.30 (n/a)</td><td>1234.56 (n/a)</td><td>922.00 (n/a)</td><td>595.30 (n/a)</td><td>701.10 (n/a)</td><td>225.44 (n/a)</td><td>141.03 (n/a)</td><td>145.58 (n/a)</td><td>66.96 (n/a)</td><td>73.11 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.11 (+4.64%)</td><td>0.78 (-6.61%)</td><td>0.69 <b>(-31.95%)</b></td><td>0.50 <b>(+35.33%)</b></td><td>0.28 (-6.58%)</td><td>716.90 <b>(-26.12%)</b></td><td>512.18 (+1.02%)</td><td>525.70 <b>(+46.93%)</b></td><td>326.10 (-4.45%)</td><td>173.53 <b>(-35.40%)</b></td><td>51.44 (+4.64%)</td><td>36.18 (-6.61%)</td><td>31.91 <b>(-31.95%)</b></td><td>23.40 <b>(+35.33%)</b></td><td>12.82 (-6.58%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.06 (n/a)</td><td>0.83 (n/a)</td><td>1.01 (n/a)</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>970.30 (n/a)</td><td>507.02 (n/a)</td><td>357.80 (n/a)</td><td>341.30 (n/a)</td><td>268.62 (n/a)</td><td>49.16 (n/a)</td><td>38.74 (n/a)</td><td>46.89 (n/a)</td><td>17.29 (n/a)</td><td>13.72 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.98 (+6.34%)</td><td>2.45 <b>(+29.02%)</b></td><td>2.80 <b>(+64.47%)</b></td><td>1.68 (+6.23%)</td><td>0.62 <b>(+23.50%)</b></td><td>2490.40 (-5.86%)</td><td>1815.56 <b>(-21.24%)</b></td><td>1497.90 <b>(-39.20%)</b></td><td>1409.50 (-5.96%)</td><td>513.88 (+12.04%)</td><td>761.77 (+6.34%)</td><td>627.48 <b>(+29.02%)</b></td><td>716.82 <b>(+64.47%)</b></td><td>431.15 (+6.23%)</td><td>159.77 <b>(+23.50%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>2.80 (n/a)</td><td>1.90 (n/a)</td><td>1.70 (n/a)</td><td>1.59 (n/a)</td><td>0.51 (n/a)</td><td>2645.50 (n/a)</td><td>2305.08 (n/a)</td><td>2463.70 (n/a)</td><td>1498.90 (n/a)</td><td>458.65 (n/a)</td><td>716.37 (n/a)</td><td>486.35 (n/a)</td><td>435.83 (n/a)</td><td>405.87 (n/a)</td><td>129.37 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>4.26 (-0.90%)</td><td>2.79 (-6.09%)</td><td>2.61 (-15.42%)</td><td>0.74 (+7.04%)</td><td>1.38 (-4.26%)</td><td>3519.50 (-6.58%)</td><td>1376.52 (+0.46%)</td><td>1004.60 (+18.23%)</td><td>615.00 (+0.90%)</td><td>1213.81 (-10.01%)</td><td>872.97 (-0.90%)</td><td>570.79 (-6.09%)</td><td>534.43 (-15.42%)</td><td>152.54 (+7.04%)</td><td>282.61 (-4.26%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.30 (n/a)</td><td>2.97 (n/a)</td><td>3.09 (n/a)</td><td>0.70 (n/a)</td><td>1.44 (n/a)</td><td>3767.30 (n/a)</td><td>1370.16 (n/a)</td><td>849.70 (n/a)</td><td>609.50 (n/a)</td><td>1348.83 (n/a)</td><td>880.89 (n/a)</td><td>607.82 (n/a)</td><td>631.85 (n/a)</td><td>142.51 (n/a)</td><td>295.19 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.64 (+1.79%)</td><td>2.86 (-8.69%)</td><td>2.86 (-17.85%)</td><td>2.07 (-14.10%)</td><td>0.56 (+3.06%)</td><td>3794.70 (+16.41%)</td><td>2840.14 (+10.20%)</td><td>2751.90 <b>(+21.73%)</b></td><td>2158.10 (-1.76%)</td><td>597.93 <b>(+22.33%)</b></td><td>1119.47 (+1.79%)</td><td>879.15 (-8.69%)</td><td>877.92 (-17.85%)</td><td>636.65 (-14.10%)</td><td>172.87 (+3.06%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.58 (n/a)</td><td>3.13 (n/a)</td><td>3.48 (n/a)</td><td>2.41 (n/a)</td><td>0.55 (n/a)</td><td>3259.80 (n/a)</td><td>2577.30 (n/a)</td><td>2260.70 (n/a)</td><td>2196.70 (n/a)</td><td>488.79 (n/a)</td><td>1099.78 (n/a)</td><td>962.78 (n/a)</td><td>1068.67 (n/a)</td><td>741.13 (n/a)</td><td>167.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm_split_leg_windowing[iter0]

_No metrics available._


### test_gemm_split_leg_windowing[iter1]

_No metrics available._


### test_gemm_split_leg_windowing[iter2]

_No metrics available._


### test_gemm_split_leg_windowing[iter3]

_No metrics available._


### test_gemm_split_leg_windowing[iter4]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter0]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter1]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter2]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter3]

_No metrics available._


### test_gemm_split_leg_windowing_runs[iter4]

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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>323.70 (n/a)</td><td>290.66 (n/a)</td><td>300.90 (n/a)</td><td>235.40 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>502.60 (n/a)</td><td>349.00 (n/a)</td><td>279.40 (n/a)</td><td>225.30 (n/a)</td><td>126.52 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>611.50 (n/a)</td><td>381.72 (n/a)</td><td>338.20 (n/a)</td><td>242.80 (n/a)</td><td>152.88 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>397.20 (n/a)</td><td>283.20 (n/a)</td><td>254.10 (n/a)</td><td>190.60 (n/a)</td><td>83.03 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1981.70 (n/a)</td><td>715.32 (n/a)</td><td>405.30 (n/a)</td><td>264.20 (n/a)</td><td>724.76 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>629.10 (n/a)</td><td>429.82 (n/a)</td><td>465.10 (n/a)</td><td>218.60 (n/a)</td><td>163.30 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>410.40 (n/a)</td><td>294.70 (n/a)</td><td>272.30 (n/a)</td><td>235.80 (n/a)</td><td>68.23 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>470.40 (n/a)</td><td>312.00 (n/a)</td><td>289.70 (n/a)</td><td>208.10 (n/a)</td><td>101.50 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>550.00 (n/a)</td><td>371.30 (n/a)</td><td>288.90 (n/a)</td><td>213.60 (n/a)</td><td>157.01 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.40 (n/a)</td><td>374.94 (n/a)</td><td>349.20 (n/a)</td><td>233.40 (n/a)</td><td>153.46 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>466.90 (n/a)</td><td>314.16 (n/a)</td><td>301.50 (n/a)</td><td>204.70 (n/a)</td><td>96.24 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>706.40 (n/a)</td><td>473.00 (n/a)</td><td>538.80 (n/a)</td><td>204.30 (n/a)</td><td>199.74 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>569.80 (n/a)</td><td>407.38 (n/a)</td><td>471.70 (n/a)</td><td>246.50 (n/a)</td><td>150.12 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>590.60 (n/a)</td><td>359.70 (n/a)</td><td>284.60 (n/a)</td><td>215.30 (n/a)</td><td>161.64 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>493.00 (n/a)</td><td>339.36 (n/a)</td><td>302.90 (n/a)</td><td>193.90 (n/a)</td><td>125.16 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>541.90 (n/a)</td><td>375.28 (n/a)</td><td>299.70 (n/a)</td><td>275.20 (n/a)</td><td>119.52 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>561.50 (n/a)</td><td>472.48 (n/a)</td><td>505.50 (n/a)</td><td>261.10 (n/a)</td><td>121.32 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>581.30 (n/a)</td><td>440.22 (n/a)</td><td>419.90 (n/a)</td><td>319.00 (n/a)</td><td>109.60 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>469.60 (n/a)</td><td>372.78 (n/a)</td><td>401.20 (n/a)</td><td>271.40 (n/a)</td><td>83.14 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>1091.70 (n/a)</td><td>539.20 (n/a)</td><td>463.70 (n/a)</td><td>260.80 (n/a)</td><td>327.35 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>560.10 (n/a)</td><td>385.44 (n/a)</td><td>291.60 (n/a)</td><td>257.80 (n/a)</td><td>145.37 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>619.60 (n/a)</td><td>419.00 (n/a)</td><td>460.90 (n/a)</td><td>215.10 (n/a)</td><td>157.43 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>442.80 (n/a)</td><td>282.64 (n/a)</td><td>221.60 (n/a)</td><td>200.40 (n/a)</td><td>102.32 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>554.70 (n/a)</td><td>406.28 (n/a)</td><td>435.30 (n/a)</td><td>290.60 (n/a)</td><td>106.83 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.63 (+0.01%)</td><td>0.43 (+10.00%)</td><td>0.35 (-11.83%)</td><td>0.28 <b>(+44.78%)</b></td><td>0.16 (-1.34%)</td><td>790.50 <b>(-30.93%)</b></td><td>563.90 (-13.26%)</td><td>638.20 (+13.42%)</td><td>353.60 (+0.00%)</td><td>187.50 <b>(-37.33%)</b></td><td>26.69 (+0.01%)</td><td>18.47 (+10.00%)</td><td>14.79 (-11.83%)</td><td>11.94 <b>(+44.78%)</b></td><td>6.63 (-1.34%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.63 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>1144.50 (n/a)</td><td>650.10 (n/a)</td><td>562.70 (n/a)</td><td>353.60 (n/a)</td><td>299.19 (n/a)</td><td>26.69 (n/a)</td><td>16.80 (n/a)</td><td>16.77 (n/a)</td><td>8.25 (n/a)</td><td>6.72 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.50 (-4.41%)</td><td>0.39 <b>(+31.08%)</b></td><td>0.45 <b>(+83.62%)</b></td><td>0.17 <b>(+41.77%)</b></td><td>0.13 <b>(-21.41%)</b></td><td>1275.20 <b>(-29.47%)</b></td><td>664.88 <b>(-32.51%)</b></td><td>492.70 <b>(-45.53%)</b></td><td>438.80 (+4.60%)</td><td>348.38 <b>(-37.84%)</b></td><td>21.51 (-4.41%)</td><td>16.47 <b>(+31.08%)</b></td><td>19.15 <b>(+83.62%)</b></td><td>7.40 <b>(+41.77%)</b></td><td>5.59 <b>(-21.41%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.53 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.12 (n/a)</td><td>0.17 (n/a)</td><td>1807.90 (n/a)</td><td>985.14 (n/a)</td><td>904.60 (n/a)</td><td>419.50 (n/a)</td><td>560.44 (n/a)</td><td>22.50 (n/a)</td><td>12.57 (n/a)</td><td>10.43 (n/a)</td><td>5.22 (n/a)</td><td>7.11 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.31 (+1.64%)</td><td>0.30 (+0.77%)</td><td>0.30 (-1.57%)</td><td>0.30 (+4.03%)</td><td>0.01 <b>(-30.36%)</b></td><td>84510.00 (-3.88%)</td><td>83161.34 (-0.80%)</td><td>84031.80 (+1.60%)</td><td>80885.20 (-1.62%)</td><td>1555.57 <b>(-34.27%)</b></td><td>212.40 (+1.64%)</td><td>206.64 (+0.77%)</td><td>204.44 (-1.57%)</td><td>203.29 (+4.03%)</td><td>3.91 <b>(-30.36%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.01 (n/a)</td><td>87917.50 (n/a)</td><td>83833.74 (n/a)</td><td>82711.00 (n/a)</td><td>82213.00 (n/a)</td><td>2366.44 (n/a)</td><td>208.97 (n/a)</td><td>205.05 (n/a)</td><td>207.71 (n/a)</td><td>195.41 (n/a)</td><td>5.61 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.17 (+2.00%)</td><td>1.15 (+1.42%)</td><td>1.15 (+1.09%)</td><td>1.11 (+1.38%)</td><td>0.02 (+0.88%)</td><td>22661.10 (-1.37%)</td><td>21958.00 (-1.40%)</td><td>21866.20 (-1.08%)</td><td>21508.00 (-1.96%)</td><td>425.86 (-2.00%)</td><td>798.77 (+2.00%)</td><td>782.63 (+1.42%)</td><td>785.68 (+1.09%)</td><td>758.12 (+1.38%)</td><td>14.95 (+0.88%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.15 (n/a)</td><td>1.13 (n/a)</td><td>1.14 (n/a)</td><td>1.10 (n/a)</td><td>0.02 (n/a)</td><td>22974.80 (n/a)</td><td>22268.92 (n/a)</td><td>22105.10 (n/a)</td><td>21938.80 (n/a)</td><td>434.55 (n/a)</td><td>783.08 (n/a)</td><td>771.70 (n/a)</td><td>777.19 (n/a)</td><td>747.77 (n/a)</td><td>14.82 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.80 (-0.97%)</td><td>0.79 (+1.03%)</td><td>0.80 (+1.66%)</td><td>0.79 (+1.87%)</td><td>0.01 <b>(-63.42%)</b></td><td>96042.70 (-1.83%)</td><td>94968.62 (-1.04%)</td><td>94806.50 (-1.64%)</td><td>94549.30 (+0.98%)</td><td>612.07 <b>(-63.68%)</b></td><td>726.81 (-0.97%)</td><td>723.63 (+1.03%)</td><td>724.84 (+1.66%)</td><td>715.51 (+1.87%)</td><td>4.63 <b>(-63.42%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.81 (n/a)</td><td>0.79 (n/a)</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.01 (n/a)</td><td>97836.60 (n/a)</td><td>95970.00 (n/a)</td><td>96384.50 (n/a)</td><td>93629.80 (n/a)</td><td>1685.40 (n/a)</td><td>733.95 (n/a)</td><td>716.23 (n/a)</td><td>712.97 (n/a)</td><td>702.39 (n/a)</td><td>12.65 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.78 (+0.03%)</td><td>0.77 (-0.30%)</td><td>0.77 (-0.71%)</td><td>0.76 (+0.01%)</td><td>0.01 (+13.95%)</td><td>99120.00 (-0.01%)</td><td>98287.94 (+0.30%)</td><td>98650.90 (+0.71%)</td><td>97084.20 (-0.03%)</td><td>826.49 (+13.74%)</td><td>707.83 (+0.03%)</td><td>699.20 (-0.30%)</td><td>696.59 (-0.71%)</td><td>693.30 (+0.01%)</td><td>5.90 (+13.95%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.78 (n/a)</td><td>0.77 (n/a)</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.01 (n/a)</td><td>99129.70 (n/a)</td><td>97995.30 (n/a)</td><td>97954.80 (n/a)</td><td>97109.90 (n/a)</td><td>726.64 (n/a)</td><td>707.65 (n/a)</td><td>701.28 (n/a)</td><td>701.54 (n/a)</td><td>693.23 (n/a)</td><td>5.18 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.90 (-0.15%)</td><td>0.89 (-0.75%)</td><td>0.89 (-1.07%)</td><td>0.88 (-1.40%)</td><td>0.01 <b>(+166.18%)</b></td><td>85967.90 (+1.42%)</td><td>85026.26 (+0.76%)</td><td>85198.30 (+1.08%)</td><td>84192.10 (+0.15%)</td><td>790.21 <b>(+169.85%)</b></td><td>816.22 (-0.15%)</td><td>808.27 (-0.75%)</td><td>806.58 (-1.07%)</td><td>799.36 (-1.40%)</td><td>7.52 <b>(+166.18%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.00 (n/a)</td><td>84764.10 (n/a)</td><td>84382.10 (n/a)</td><td>84287.00 (n/a)</td><td>84064.00 (n/a)</td><td>292.83 (n/a)</td><td>817.47 (n/a)</td><td>814.39 (n/a)</td><td>815.30 (n/a)</td><td>810.71 (n/a)</td><td>2.82 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.88 (+2.82%)</td><td>4.23 (-0.85%)</td><td>4.03 (-0.03%)</td><td>2.18 <b>(-39.98%)</b></td><td>1.40 <b>(+68.68%)</b></td><td>4079.90 <b>(+66.60%)</b></td><td>2362.20 (+10.29%)</td><td>2211.20 (+0.03%)</td><td>1516.50 (-2.74%)</td><td>1010.33 <b>(+195.82%)</b></td><td>354.02 (+2.82%)</td><td>254.80 (-0.85%)</td><td>242.80 (-0.03%)</td><td>131.59 <b>(-39.98%)</b></td><td>84.14 <b>(+68.68%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.72 (n/a)</td><td>4.27 (n/a)</td><td>4.03 (n/a)</td><td>3.64 (n/a)</td><td>0.83 (n/a)</td><td>2448.90 (n/a)</td><td>2141.86 (n/a)</td><td>2210.50 (n/a)</td><td>1559.30 (n/a)</td><td>341.53 (n/a)</td><td>344.30 (n/a)</td><td>256.99 (n/a)</td><td>242.87 (n/a)</td><td>219.23 (n/a)</td><td>49.88 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>4.71 (+2.73%)</td><td>3.51 <b>(+26.73%)</b></td><td>3.47 <b>(+50.31%)</b></td><td>2.10 (+7.80%)</td><td>1.14 (+8.07%)</td><td>4251.60 (-7.23%)</td><td>2790.54 <b>(-20.56%)</b></td><td>2568.50 <b>(-33.47%)</b></td><td>1892.60 (-2.66%)</td><td>991.21 (-0.09%)</td><td>283.66 (+2.73%)</td><td>211.38 <b>(+26.73%)</b></td><td>209.03 <b>(+50.31%)</b></td><td>126.27 (+7.79%)</td><td>68.46 (+8.07%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.58 (n/a)</td><td>2.77 (n/a)</td><td>2.31 (n/a)</td><td>1.94 (n/a)</td><td>1.05 (n/a)</td><td>4583.00 (n/a)</td><td>3512.66 (n/a)</td><td>3860.60 (n/a)</td><td>1944.30 (n/a)</td><td>992.08 (n/a)</td><td>276.13 (n/a)</td><td>166.79 (n/a)</td><td>139.07 (n/a)</td><td>117.14 (n/a)</td><td>63.35 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.77 (-3.43%)</td><td>3.79 (+6.89%)</td><td>4.03 <b>(+26.37%)</b></td><td>2.24 (+6.40%)</td><td>1.37 (-7.57%)</td><td>3979.50 (-6.01%)</td><td>2622.38 (-7.57%)</td><td>2210.10 <b>(-20.87%)</b></td><td>1545.30 (+3.54%)</td><td>964.60 (-5.09%)</td><td>347.42 (-3.43%)</td><td>228.03 (+6.89%)</td><td>242.92 <b>(+26.37%)</b></td><td>134.91 (+6.40%)</td><td>82.49 (-7.57%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.97 (n/a)</td><td>3.54 (n/a)</td><td>3.19 (n/a)</td><td>2.11 (n/a)</td><td>1.48 (n/a)</td><td>4234.10 (n/a)</td><td>2837.28 (n/a)</td><td>2793.00 (n/a)</td><td>1492.40 (n/a)</td><td>1016.37 (n/a)</td><td>359.74 (n/a)</td><td>213.33 (n/a)</td><td>192.22 (n/a)</td><td>126.80 (n/a)</td><td>89.24 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>6.42 (+0.61%)</td><td>5.59 (+0.41%)</td><td>5.94 (-1.40%)</td><td>4.34 (+1.13%)</td><td>0.88 (+1.75%)</td><td>8031.30 (-1.12%)</td><td>6377.62 (-0.38%)</td><td>5864.60 (+1.42%)</td><td>5433.10 (-0.61%)</td><td>1092.83 (-0.57%)</td><td>395.26 (+0.61%)</td><td>344.08 (+0.41%)</td><td>366.17 (-1.40%)</td><td>267.39 (+1.13%)</td><td>53.91 (+1.75%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>6.38 (n/a)</td><td>5.56 (n/a)</td><td>6.03 (n/a)</td><td>4.29 (n/a)</td><td>0.86 (n/a)</td><td>8122.30 (n/a)</td><td>6402.10 (n/a)</td><td>5782.30 (n/a)</td><td>5466.20 (n/a)</td><td>1099.05 (n/a)</td><td>392.87 (n/a)</td><td>342.68 (n/a)</td><td>371.39 (n/a)</td><td>264.39 (n/a)</td><td>52.99 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.98 (+5.10%)</td><td>4.78 (-6.46%)</td><td>4.78 (-10.40%)</td><td>3.98 (-11.74%)</td><td>0.78 <b>(+50.88%)</b></td><td>8755.40 (+13.30%)</td><td>7439.72 (+8.18%)</td><td>7290.60 (+11.61%)</td><td>5834.10 (-4.85%)</td><td>1153.66 <b>(+60.98%)</b></td><td>368.09 (+5.10%)</td><td>294.60 (-6.46%)</td><td>294.56 (-10.40%)</td><td>245.27 (-11.74%)</td><td>48.33 <b>(+50.88%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.69 (n/a)</td><td>5.11 (n/a)</td><td>5.34 (n/a)</td><td>4.51 (n/a)</td><td>0.52 (n/a)</td><td>7727.60 (n/a)</td><td>6877.16 (n/a)</td><td>6532.20 (n/a)</td><td>6131.50 (n/a)</td><td>716.66 (n/a)</td><td>350.24 (n/a)</td><td>314.93 (n/a)</td><td>328.75 (n/a)</td><td>277.90 (n/a)</td><td>32.03 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>6.07 (-6.37%)</td><td>5.73 (+1.53%)</td><td>5.73 (+4.30%)</td><td>5.27 (+1.19%)</td><td>0.31 <b>(-37.85%)</b></td><td>6610.00 (-1.18%)</td><td>6097.80 (-1.83%)</td><td>6087.30 (-4.13%)</td><td>5740.00 (+6.80%)</td><td>333.71 <b>(-32.99%)</b></td><td>374.13 (-6.37%)</td><td>353.00 (+1.53%)</td><td>352.78 (+4.30%)</td><td>324.88 (+1.19%)</td><td>18.84 <b>(-37.85%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>6.49 (n/a)</td><td>5.64 (n/a)</td><td>5.49 (n/a)</td><td>5.21 (n/a)</td><td>0.49 (n/a)</td><td>6688.80 (n/a)</td><td>6211.50 (n/a)</td><td>6349.30 (n/a)</td><td>5374.60 (n/a)</td><td>498.00 (n/a)</td><td>399.56 (n/a)</td><td>347.67 (n/a)</td><td>338.22 (n/a)</td><td>321.06 (n/a)</td><td>30.31 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.78 (-0.13%)</td><td>0.77 (+1.51%)</td><td>0.77 (+1.09%)</td><td>0.75 (+1.87%)</td><td>0.01 <b>(-40.86%)</b></td><td>100027.90 (-1.83%)</td><td>98005.72 (-1.51%)</td><td>97872.50 (-1.08%)</td><td>96851.40 (+0.13%)</td><td>1302.43 <b>(-42.17%)</b></td><td>709.54 (-0.13%)</td><td>701.28 (+1.51%)</td><td>702.13 (+1.09%)</td><td>687.00 (+1.87%)</td><td>9.25 <b>(-40.86%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.78 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.02 (n/a)</td><td>101893.50 (n/a)</td><td>99513.02 (n/a)</td><td>98941.40 (n/a)</td><td>96722.30 (n/a)</td><td>2252.14 (n/a)</td><td>710.48 (n/a)</td><td>690.84 (n/a)</td><td>694.55 (n/a)</td><td>674.42 (n/a)</td><td>15.63 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.78 (+1.67%)</td><td>0.76 (-0.48%)</td><td>0.75 (-1.44%)</td><td>0.74 (-0.33%)</td><td>0.02 <b>(+61.45%)</b></td><td>101384.10 (+0.33%)</td><td>99766.70 (+0.50%)</td><td>100271.50 (+1.47%)</td><td>96214.80 (-1.64%)</td><td>2041.10 <b>(+58.52%)</b></td><td>714.23 (+1.67%)</td><td>689.04 (-0.48%)</td><td>685.33 (-1.44%)</td><td>677.81 (-0.33%)</td><td>14.44 <b>(+61.45%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.77 (n/a)</td><td>0.76 (n/a)</td><td>0.76 (n/a)</td><td>0.75 (n/a)</td><td>0.01 (n/a)</td><td>101052.30 (n/a)</td><td>99268.06 (n/a)</td><td>98823.70 (n/a)</td><td>97820.50 (n/a)</td><td>1287.63 (n/a)</td><td>702.51 (n/a)</td><td>692.35 (n/a)</td><td>695.37 (n/a)</td><td>680.04 (n/a)</td><td>8.94 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.90 (+1.32%)</td><td>0.88 (+0.26%)</td><td>0.88 (+0.61%)</td><td>0.85 (-1.36%)</td><td>0.02 <b>(+124.04%)</b></td><td>88317.50 (+1.38%)</td><td>85666.42 (-0.23%)</td><td>85322.00 (-0.61%)</td><td>83998.90 (-1.30%)</td><td>1843.40 <b>(+123.77%)</b></td><td>818.10 (+1.32%)</td><td>802.47 (+0.26%)</td><td>805.41 (+0.61%)</td><td>778.10 (-1.36%)</td><td>17.12 <b>(+124.04%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.01 (n/a)</td><td>87117.30 (n/a)</td><td>85860.48 (n/a)</td><td>85845.40 (n/a)</td><td>85108.80 (n/a)</td><td>823.80 (n/a)</td><td>807.43 (n/a)</td><td>800.42 (n/a)</td><td>800.50 (n/a)</td><td>788.82 (n/a)</td><td>7.64 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>4.20 (-7.80%)</td><td>2.85 <b>(+25.71%)</b></td><td>2.90 <b>(+72.86%)</b></td><td>1.64 (+15.14%)</td><td>1.19 (-9.18%)</td><td>4918.30 (-13.15%)</td><td>3307.78 <b>(-22.23%)</b></td><td>2777.90 <b>(-42.15%)</b></td><td>1921.50 (+8.47%)</td><td>1460.98 (-6.54%)</td><td>1100.17 (-7.80%)</td><td>747.10 <b>(+25.71%)</b></td><td>760.99 <b>(+72.86%)</b></td><td>429.81 (+15.14%)</td><td>311.33 (-9.18%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.55 (n/a)</td><td>2.27 (n/a)</td><td>1.68 (n/a)</td><td>1.42 (n/a)</td><td>1.31 (n/a)</td><td>5663.00 (n/a)</td><td>4253.02 (n/a)</td><td>4801.80 (n/a)</td><td>1771.50 (n/a)</td><td>1563.16 (n/a)</td><td>1193.30 (n/a)</td><td>594.30 (n/a)</td><td>440.24 (n/a)</td><td>373.29 (n/a)</td><td>342.80 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.32 <b>(+37.46%)</b></td><td>0.24 <b>(+25.95%)</b></td><td>0.22 <b>(+23.95%)</b></td><td>0.20 <b>(+52.52%)</b></td><td>0.05 (+11.14%)</td><td>6173.70 <b>(-34.43%)</b></td><td>5444.60 <b>(-22.11%)</b></td><td>5711.60 (-19.32%)</td><td>3834.50 <b>(-27.25%)</b></td><td>954.65 <b>(-45.51%)</b></td><td>17.50 <b>(+37.46%)</b></td><td>12.71 <b>(+25.95%)</b></td><td>11.75 <b>(+23.95%)</b></td><td>10.87 <b>(+52.52%)</b></td><td>2.75 (+11.14%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>9416.00 (n/a)</td><td>6990.04 (n/a)</td><td>7079.30 (n/a)</td><td>5270.80 (n/a)</td><td>1752.08 (n/a)</td><td>12.73 (n/a)</td><td>10.09 (n/a)</td><td>9.48 (n/a)</td><td>7.13 (n/a)</td><td>2.48 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.73 (n/a)</td><td>3.53 (n/a)</td><td>3.45 (n/a)</td><td>3.36 (n/a)</td><td>0.17 (n/a)</td><td>3.73 (n/a)</td><td>3.53 (n/a)</td><td>3.45 (n/a)</td><td>3.35 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>7.47 (+2.68%)</td><td>6.17 (-1.23%)</td><td>5.67 (-2.26%)</td><td>5.58 (+2.53%)</td><td>0.82 (-1.36%)</td><td>7.46 (+2.68%)</td><td>6.17 (-1.23%)</td><td>5.67 (-2.26%)</td><td>5.58 (+2.53%)</td><td>0.82 (-1.36%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>7.27 (n/a)</td><td>6.25 (n/a)</td><td>5.81 (n/a)</td><td>5.45 (n/a)</td><td>0.84 (n/a)</td><td>7.27 (n/a)</td><td>6.24 (n/a)</td><td>5.80 (n/a)</td><td>5.44 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>13.83 <b>(+63.08%)</b></td><td>10.04 <b>(+30.41%)</b></td><td>9.13 <b>(+20.42%)</b></td><td>8.58 <b>(+26.50%)</b></td><td>2.15 <b>(+219.38%)</b></td><td>13.82 <b>(+63.08%)</b></td><td>10.03 <b>(+30.41%)</b></td><td>9.13 <b>(+20.42%)</b></td><td>8.58 <b>(+26.50%)</b></td><td>2.15 <b>(+219.38%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>8.48 (n/a)</td><td>7.70 (n/a)</td><td>7.58 (n/a)</td><td>6.78 (n/a)</td><td>0.67 (n/a)</td><td>8.47 (n/a)</td><td>7.69 (n/a)</td><td>7.58 (n/a)</td><td>6.78 (n/a)</td><td>0.67 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.82 (n/a)</td><td>3.59 (n/a)</td><td>3.66 (n/a)</td><td>3.31 (n/a)</td><td>0.20 (n/a)</td><td>3.82 (n/a)</td><td>3.59 (n/a)</td><td>3.65 (n/a)</td><td>3.31 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>7.04 (-0.06%)</td><td>5.95 (-5.48%)</td><td>6.11 (-0.49%)</td><td>4.47 <b>(-20.09%)</b></td><td>1.10 <b>(+76.29%)</b></td><td>7.03 (-0.06%)</td><td>5.94 (-5.48%)</td><td>6.11 (-0.49%)</td><td>4.46 <b>(-20.09%)</b></td><td>1.10 <b>(+76.29%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>7.04 (n/a)</td><td>6.29 (n/a)</td><td>6.14 (n/a)</td><td>5.59 (n/a)</td><td>0.63 (n/a)</td><td>7.04 (n/a)</td><td>6.29 (n/a)</td><td>6.14 (n/a)</td><td>5.58 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>13.98 <b>(+43.09%)</b></td><td>9.29 (+10.24%)</td><td>8.22 (+0.03%)</td><td>7.69 (+4.01%)</td><td>2.63 <b>(+204.55%)</b></td><td>13.97 <b>(+43.09%)</b></td><td>9.28 (+10.24%)</td><td>8.22 (+0.03%)</td><td>7.69 (+4.01%)</td><td>2.63 <b>(+204.55%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>9.77 (n/a)</td><td>8.43 (n/a)</td><td>8.22 (n/a)</td><td>7.39 (n/a)</td><td>0.87 (n/a)</td><td>9.76 (n/a)</td><td>8.42 (n/a)</td><td>8.21 (n/a)</td><td>7.39 (n/a)</td><td>0.86 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.20 (+4.29%)</td><td>2.41 (-15.39%)</td><td>2.74 (-1.38%)</td><td>1.52 <b>(-44.13%)</b></td><td>0.77 <b>(+450.23%)</b></td><td>3.20 (+4.29%)</td><td>2.40 (-15.39%)</td><td>2.74 (-1.38%)</td><td>1.52 <b>(-44.13%)</b></td><td>0.77 <b>(+450.23%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.07 (n/a)</td><td>2.84 (n/a)</td><td>2.78 (n/a)</td><td>2.72 (n/a)</td><td>0.14 (n/a)</td><td>3.06 (n/a)</td><td>2.84 (n/a)</td><td>2.78 (n/a)</td><td>2.71 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.56 <b>(+27.19%)</b></td><td>0.39 <b>(+67.79%)</b></td><td>0.39 <b>(+57.29%)</b></td><td>0.08 (+0.93%)</td><td>0.20 <b>(+22.40%)</b></td><td>0.56 <b>(+27.19%)</b></td><td>0.39 <b>(+67.79%)</b></td><td>0.39 <b>(+57.29%)</b></td><td>0.07 (+0.93%)</td><td>0.19 <b>(+22.40%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.44 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td><td>0.44 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>0.16 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.65 (-10.26%)</td><td>0.43 <b>(-31.12%)</b></td><td>0.48 <b>(-28.68%)</b></td><td>0.08 <b>(-78.34%)</b></td><td>0.22 <b>(+52.53%)</b></td><td>0.64 (-10.26%)</td><td>0.42 <b>(-31.12%)</b></td><td>0.47 <b>(-28.68%)</b></td><td>0.08 <b>(-78.34%)</b></td><td>0.21 <b>(+52.53%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.72 (n/a)</td><td>0.62 (n/a)</td><td>0.67 (n/a)</td><td>0.37 (n/a)</td><td>0.14 (n/a)</td><td>0.72 (n/a)</td><td>0.61 (n/a)</td><td>0.66 (n/a)</td><td>0.37 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.60 (+10.19%)</td><td>2.27 <b>(+24.76%)</b></td><td>2.35 (+9.27%)</td><td>1.56 <b>(+103.08%)</b></td><td>0.42 <b>(-38.66%)</b></td><td>2.56 (+10.19%)</td><td>2.23 <b>(+24.76%)</b></td><td>2.31 (+9.27%)</td><td>1.54 <b>(+103.08%)</b></td><td>0.42 <b>(-38.66%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>2.36 (n/a)</td><td>1.82 (n/a)</td><td>2.15 (n/a)</td><td>0.77 (n/a)</td><td>0.69 (n/a)</td><td>2.32 (n/a)</td><td>1.79 (n/a)</td><td>2.11 (n/a)</td><td>0.76 (n/a)</td><td>0.68 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>501.20 (n/a)</td><td>315.78 (n/a)</td><td>275.00 (n/a)</td><td>230.30 (n/a)</td><td>109.60 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.20 (n/a)</td><td>402.62 (n/a)</td><td>446.70 (n/a)</td><td>225.30 (n/a)</td><td>148.49 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1842.40 (n/a)</td><td>725.44 (n/a)</td><td>471.60 (n/a)</td><td>337.20 (n/a)</td><td>629.18 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>561.50 (n/a)</td><td>449.56 (n/a)</td><td>492.30 (n/a)</td><td>276.60 (n/a)</td><td>108.27 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>542.50 (n/a)</td><td>428.76 (n/a)</td><td>418.70 (n/a)</td><td>310.10 (n/a)</td><td>92.54 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>616.70 (n/a)</td><td>456.90 (n/a)</td><td>457.10 (n/a)</td><td>297.00 (n/a)</td><td>139.18 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.90 (n/a)</td><td>363.46 (n/a)</td><td>280.10 (n/a)</td><td>225.30 (n/a)</td><td>164.64 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>441.40 (n/a)</td><td>328.78 (n/a)</td><td>288.50 (n/a)</td><td>232.70 (n/a)</td><td>101.50 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.60 (n/a)</td><td>301.48 (n/a)</td><td>252.30 (n/a)</td><td>224.50 (n/a)</td><td>119.16 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.80 (n/a)</td><td>360.22 (n/a)</td><td>381.00 (n/a)</td><td>261.30 (n/a)</td><td>99.87 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>508.60 (n/a)</td><td>367.90 (n/a)</td><td>338.80 (n/a)</td><td>289.70 (n/a)</td><td>92.48 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.90 (n/a)</td><td>386.08 (n/a)</td><td>369.70 (n/a)</td><td>207.80 (n/a)</td><td>129.84 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>554.40 (n/a)</td><td>387.52 (n/a)</td><td>332.80 (n/a)</td><td>272.10 (n/a)</td><td>124.55 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>523.50 (n/a)</td><td>414.82 (n/a)</td><td>501.60 (n/a)</td><td>232.00 (n/a)</td><td>136.15 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>538.20 (n/a)</td><td>409.98 (n/a)</td><td>434.80 (n/a)</td><td>182.20 (n/a)</td><td>146.77 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>618.00 (n/a)</td><td>437.22 (n/a)</td><td>505.50 (n/a)</td><td>228.00 (n/a)</td><td>164.31 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>591.50 (n/a)</td><td>415.78 (n/a)</td><td>418.90 (n/a)</td><td>187.00 (n/a)</td><td>160.32 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>680.40 (n/a)</td><td>513.86 (n/a)</td><td>530.60 (n/a)</td><td>289.90 (n/a)</td><td>151.26 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>644.70 (n/a)</td><td>402.00 (n/a)</td><td>369.40 (n/a)</td><td>260.90 (n/a)</td><td>151.36 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>679.40 (n/a)</td><td>442.22 (n/a)</td><td>488.20 (n/a)</td><td>202.80 (n/a)</td><td>202.29 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>691.80 (n/a)</td><td>557.52 (n/a)</td><td>557.70 (n/a)</td><td>393.40 (n/a)</td><td>107.38 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>587.60 (n/a)</td><td>457.26 (n/a)</td><td>476.60 (n/a)</td><td>310.20 (n/a)</td><td>106.13 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>493.40 (n/a)</td><td>395.26 (n/a)</td><td>423.20 (n/a)</td><td>275.80 (n/a)</td><td>83.80 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>603.90 (n/a)</td><td>456.54 (n/a)</td><td>490.70 (n/a)</td><td>332.00 (n/a)</td><td>117.67 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (-11.10%)</td><td>0.01 <b>(-22.62%)</b></td><td>0.01 <b>(-36.82%)</b></td><td>0.01 (+3.66%)</td><td>0.00 <b>(-25.54%)</b></td><td>553.00 (-3.54%)</td><td>411.64 <b>(+22.25%)</b></td><td>416.30 <b>(+58.29%)</b></td><td>233.60 (+12.47%)</td><td>132.59 (-15.97%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>573.30 (n/a)</td><td>336.72 (n/a)</td><td>263.00 (n/a)</td><td>207.70 (n/a)</td><td>157.79 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (-8.74%)</td><td>0.01 (+3.64%)</td><td>0.01 (-3.14%)</td><td>0.01 <b>(+296.02%)</b></td><td>0.00 <b>(-45.90%)</b></td><td>515.60 <b>(-74.75%)</b></td><td>409.98 <b>(-41.39%)</b></td><td>449.90 (+3.24%)</td><td>259.70 (+9.58%)</td><td>102.35 <b>(-86.49%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2042.00 (n/a)</td><td>699.54 (n/a)</td><td>435.80 (n/a)</td><td>237.00 (n/a)</td><td>757.84 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (-17.65%)</td><td>0.01 <b>(-35.28%)</b></td><td>0.01 <b>(-51.57%)</b></td><td>0.01 <b>(-26.15%)</b></td><td>0.00 <b>(-34.25%)</b></td><td>743.70 <b>(+35.42%)</b></td><td>522.96 <b>(+47.06%)</b></td><td>489.60 <b>(+106.50%)</b></td><td>279.90 <b>(+21.43%)</b></td><td>183.40 (+8.94%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>549.20 (n/a)</td><td>355.60 (n/a)</td><td>237.10 (n/a)</td><td>230.50 (n/a)</td><td>168.35 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(+22.43%)</b></td><td>0.01 <b>(-27.18%)</b></td><td>0.01 <b>(-41.69%)</b></td><td>0.00 <b>(-75.03%)</b></td><td>0.01 <b>(+135.29%)</b></td><td>1937.90 <b>(+300.39%)</b></td><td>774.62 <b>(+110.17%)</b></td><td>619.10 <b>(+71.50%)</b></td><td>228.70 (-18.29%)</td><td>669.91 <b>(+718.97%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>484.00 (n/a)</td><td>368.56 (n/a)</td><td>361.00 (n/a)</td><td>279.90 (n/a)</td><td>81.80 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 <b>(-20.41%)</b></td><td>0.01 (-14.05%)</td><td>0.01 (+11.92%)</td><td>0.00 <b>(-75.97%)</b></td><td>0.00 <b>(+30.99%)</b></td><td>2416.30 <b>(+316.24%)</b></td><td>826.54 <b>(+80.29%)</b></td><td>430.40 (-10.65%)</td><td>351.90 <b>(+25.63%)</b></td><td>891.96 <b>(+664.27%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>580.50 (n/a)</td><td>458.44 (n/a)</td><td>481.70 (n/a)</td><td>280.10 (n/a)</td><td>116.71 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+5.25%)</td><td>0.01 (+10.62%)</td><td>0.01 <b>(+54.48%)</b></td><td>0.01 (+10.75%)</td><td>0.00 (-17.42%)</td><td>493.00 (-9.71%)</td><td>356.26 (-13.60%)</td><td>313.60 <b>(-35.26%)</b></td><td>237.40 (-5.00%)</td><td>111.34 <b>(-24.35%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>546.00 (n/a)</td><td>412.32 (n/a)</td><td>484.40 (n/a)</td><td>249.90 (n/a)</td><td>147.18 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-9.35%)</td><td>0.02 <b>(-21.68%)</b></td><td>0.03 (-9.30%)</td><td>0.02 <b>(-43.09%)</b></td><td>0.01 <b>(+194.25%)</b></td><td>525.10 <b>(+75.74%)</b></td><td>379.74 <b>(+38.36%)</b></td><td>295.10 (+10.24%)</td><td>270.80 (+10.31%)</td><td>128.35 <b>(+485.90%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>298.80 (n/a)</td><td>274.46 (n/a)</td><td>267.70 (n/a)</td><td>245.50 (n/a)</td><td>21.91 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-16.20%)</td><td>0.02 (+0.66%)</td><td>0.03 <b>(+50.14%)</b></td><td>0.01 (-16.19%)</td><td>0.01 (-6.24%)</td><td>602.80 (+19.32%)</td><td>390.00 (+1.57%)</td><td>294.70 <b>(-33.40%)</b></td><td>265.10 (+19.31%)</td><td>155.61 <b>(+32.08%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.20 (n/a)</td><td>383.98 (n/a)</td><td>442.50 (n/a)</td><td>222.20 (n/a)</td><td>117.82 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(-47.61%)</b></td><td>0.01 <b>(-49.23%)</b></td><td>0.02 <b>(-45.54%)</b></td><td>0.00 <b>(-80.77%)</b></td><td>0.01 (+14.87%)</td><td>2012.80 <b>(+419.97%)</b></td><td>825.80 <b>(+155.94%)</b></td><td>541.40 <b>(+83.59%)</b></td><td>504.50 <b>(+90.88%)</b></td><td>663.79 <b>(+1050.00%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>387.10 (n/a)</td><td>322.66 (n/a)</td><td>294.90 (n/a)</td><td>264.30 (n/a)</td><td>57.72 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 <b>(-26.16%)</b></td><td>0.02 <b>(-27.06%)</b></td><td>0.02 <b>(-38.86%)</b></td><td>0.01 (-18.99%)</td><td>0.01 <b>(-37.52%)</b></td><td>669.20 <b>(+23.45%)</b></td><td>458.02 <b>(+30.95%)</b></td><td>458.40 <b>(+63.54%)</b></td><td>284.10 <b>(+35.41%)</b></td><td>140.90 (+0.13%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.10 (n/a)</td><td>349.78 (n/a)</td><td>280.30 (n/a)</td><td>209.80 (n/a)</td><td>140.72 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-9.66%)</td><td>0.02 (-4.97%)</td><td>0.02 (-5.60%)</td><td>0.01 <b>(-20.42%)</b></td><td>0.01 (+8.21%)</td><td>651.20 <b>(+25.67%)</b></td><td>441.02 (+8.57%)</td><td>466.00 (+5.93%)</td><td>290.60 (+10.66%)</td><td>150.63 <b>(+41.06%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>518.20 (n/a)</td><td>406.22 (n/a)</td><td>439.90 (n/a)</td><td>262.60 (n/a)</td><td>106.79 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-18.76%)</td><td>0.02 (-7.92%)</td><td>0.03 (+11.96%)</td><td>0.02 (-5.80%)</td><td>0.01 <b>(-27.60%)</b></td><td>545.10 (+6.15%)</td><td>373.86 (+5.61%)</td><td>302.40 (-10.69%)</td><td>290.00 <b>(+23.09%)</b></td><td>114.03 (-5.44%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>513.50 (n/a)</td><td>354.00 (n/a)</td><td>338.60 (n/a)</td><td>235.60 (n/a)</td><td>120.59 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-4.48%)</td><td>0.02 <b>(-22.46%)</b></td><td>0.02 <b>(-38.86%)</b></td><td>0.02 (+9.52%)</td><td>0.01 (-4.09%)</td><td>478.10 (-8.69%)</td><td>408.22 <b>(+27.17%)</b></td><td>454.30 <b>(+63.59%)</b></td><td>245.60 (+4.69%)</td><td>96.59 (-16.25%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>523.60 (n/a)</td><td>321.00 (n/a)</td><td>277.70 (n/a)</td><td>234.60 (n/a)</td><td>115.33 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (+10.94%)</td><td>0.02 (+1.21%)</td><td>0.02 (+0.75%)</td><td>0.01 (-6.01%)</td><td>0.01 <b>(+24.15%)</b></td><td>617.40 (+6.39%)</td><td>467.88 (+3.20%)</td><td>488.20 (-0.75%)</td><td>213.30 (-9.85%)</td><td>156.32 (+19.69%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>580.30 (n/a)</td><td>453.38 (n/a)</td><td>491.90 (n/a)</td><td>236.60 (n/a)</td><td>130.61 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (-9.54%)</td><td>0.05 (+1.64%)</td><td>0.05 <b>(+27.37%)</b></td><td>0.03 (+6.07%)</td><td>0.01 (-13.01%)</td><td>483.00 (-5.72%)</td><td>359.08 (-2.67%)</td><td>305.20 <b>(-21.48%)</b></td><td>265.60 (+10.53%)</td><td>99.42 (-5.50%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>512.30 (n/a)</td><td>368.94 (n/a)</td><td>388.70 (n/a)</td><td>240.30 (n/a)</td><td>105.20 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (+16.17%)</td><td>0.05 (-10.32%)</td><td>0.04 (-14.42%)</td><td>0.03 (-17.06%)</td><td>0.02 <b>(+42.76%)</b></td><td>575.20 <b>(+20.59%)</b></td><td>412.76 <b>(+20.37%)</b></td><td>432.70 (+16.85%)</td><td>213.20 (-13.93%)</td><td>156.51 <b>(+61.90%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>477.00 (n/a)</td><td>342.92 (n/a)</td><td>370.30 (n/a)</td><td>247.70 (n/a)</td><td>96.67 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 <b>(-20.21%)</b></td><td>0.05 (+12.73%)</td><td>0.06 <b>(+60.92%)</b></td><td>0.03 <b>(+89.44%)</b></td><td>0.02 <b>(-34.99%)</b></td><td>521.50 <b>(-47.21%)</b></td><td>364.26 <b>(-27.09%)</b></td><td>278.70 <b>(-37.87%)</b></td><td>246.30 <b>(+25.34%)</b></td><td>141.06 <b>(-54.77%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>987.90 (n/a)</td><td>499.58 (n/a)</td><td>448.60 (n/a)</td><td>196.50 (n/a)</td><td>311.91 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (-12.75%)</td><td>0.05 (-7.79%)</td><td>0.04 (-19.33%)</td><td>0.02 (-9.47%)</td><td>0.02 (+4.35%)</td><td>655.90 (+10.48%)</td><td>429.36 (+12.89%)</td><td>463.80 <b>(+23.98%)</b></td><td>234.80 (+14.59%)</td><td>189.69 <b>(+22.27%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>593.70 (n/a)</td><td>380.32 (n/a)</td><td>374.10 (n/a)</td><td>204.90 (n/a)</td><td>155.14 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (-19.36%)</td><td>0.04 <b>(-20.65%)</b></td><td>0.03 (-17.76%)</td><td>0.02 (-11.05%)</td><td>0.01 <b>(-28.11%)</b></td><td>674.10 (+12.42%)</td><td>489.28 <b>(+22.33%)</b></td><td>496.70 <b>(+21.59%)</b></td><td>293.50 <b>(+24.00%)</b></td><td>141.82 (-0.89%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.60 (n/a)</td><td>399.96 (n/a)</td><td>408.50 (n/a)</td><td>236.70 (n/a)</td><td>143.10 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 <b>(-38.84%)</b></td><td>0.03 <b>(-21.90%)</b></td><td>0.04 <b>(+25.38%)</b></td><td>0.01 <b>(-68.61%)</b></td><td>0.01 <b>(-28.40%)</b></td><td>1877.00 <b>(+218.57%)</b></td><td>702.90 <b>(+60.47%)</b></td><td>415.10 <b>(-20.23%)</b></td><td>363.20 <b>(+63.53%)</b></td><td>657.56 <b>(+289.48%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>589.20 (n/a)</td><td>438.02 (n/a)</td><td>520.40 (n/a)</td><td>222.10 (n/a)</td><td>168.83 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (+9.98%)</td><td>0.09 (-4.33%)</td><td>0.07 (-4.92%)</td><td>0.05 <b>(-29.26%)</b></td><td>0.03 <b>(+67.73%)</b></td><td>606.90 <b>(+41.37%)</b></td><td>420.58 (+12.14%)</td><td>444.20 (+5.19%)</td><td>257.90 (-9.06%)</td><td>144.08 <b>(+104.18%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>429.30 (n/a)</td><td>375.06 (n/a)</td><td>422.30 (n/a)</td><td>283.60 (n/a)</td><td>70.56 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (-1.59%)</td><td>0.09 <b>(-27.79%)</b></td><td>0.07 <b>(-37.00%)</b></td><td>0.06 <b>(-41.21%)</b></td><td>0.04 <b>(+81.63%)</b></td><td>527.40 <b>(+70.07%)</b></td><td>407.42 <b>(+50.70%)</b></td><td>440.50 <b>(+58.74%)</b></td><td>220.60 (+1.61%)</td><td>128.48 <b>(+211.47%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>310.10 (n/a)</td><td>270.36 (n/a)</td><td>277.50 (n/a)</td><td>217.10 (n/a)</td><td>41.25 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 <b>(-31.73%)</b></td><td>0.07 <b>(-20.16%)</b></td><td>0.08 (+1.74%)</td><td>0.06 (-0.70%)</td><td>0.01 <b>(-60.61%)</b></td><td>574.10 (+0.70%)</td><td>460.10 (+14.02%)</td><td>424.90 (-1.71%)</td><td>348.70 <b>(+46.45%)</b></td><td>90.75 <b>(-39.27%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>570.10 (n/a)</td><td>403.52 (n/a)</td><td>432.30 (n/a)</td><td>238.10 (n/a)</td><td>149.45 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.11 (-18.77%)</td><td>0.07 <b>(-30.30%)</b></td><td>0.07 <b>(-39.52%)</b></td><td>0.05 (-6.32%)</td><td>0.02 <b>(-30.53%)</b></td><td>635.00 (+6.74%)</td><td>470.10 <b>(+37.50%)</b></td><td>471.70 <b>(+65.33%)</b></td><td>300.10 <b>(+23.14%)</b></td><td>118.80 (-17.48%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>594.90 (n/a)</td><td>341.88 (n/a)</td><td>285.30 (n/a)</td><td>243.70 (n/a)</td><td>143.96 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 <b>(+35.27%)</b></td><td>0.07 (-6.86%)</td><td>0.06 <b>(-33.13%)</b></td><td>0.05 (-1.40%)</td><td>0.05 <b>(+79.75%)</b></td><td>645.10 (+1.43%)</td><td>535.06 (+18.53%)</td><td>595.70 <b>(+49.56%)</b></td><td>212.70 <b>(-26.07%)</b></td><td>181.60 <b>(+25.81%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>636.00 (n/a)</td><td>451.40 (n/a)</td><td>398.30 (n/a)</td><td>287.70 (n/a)</td><td>144.35 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+15.48%)</td><td>0.02 <b>(+43.40%)</b></td><td>0.02 <b>(+80.78%)</b></td><td>0.01 (+16.90%)</td><td>0.00 (+4.22%)</td><td>494.70 (-14.46%)</td><td>297.28 <b>(-31.44%)</b></td><td>246.60 <b>(-44.67%)</b></td><td>210.50 (-13.37%)</td><td>114.16 <b>(-20.65%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>578.30 (n/a)</td><td>433.62 (n/a)</td><td>445.70 (n/a)</td><td>243.00 (n/a)</td><td>143.86 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(+20.50%)</b></td><td>0.02 <b>(+28.04%)</b></td><td>0.01 (+17.27%)</td><td>0.01 <b>(+79.08%)</b></td><td>0.00 <b>(-52.31%)</b></td><td>295.50 <b>(-44.16%)</b></td><td>273.24 <b>(-25.75%)</b></td><td>278.40 (-14.73%)</td><td>235.20 (-17.01%)</td><td>23.19 <b>(-77.77%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>529.20 (n/a)</td><td>368.00 (n/a)</td><td>326.50 (n/a)</td><td>283.40 (n/a)</td><td>104.32 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(+103.33%)</b></td><td>0.01 <b>(+33.46%)</b></td><td>0.01 <b>(+49.09%)</b></td><td>0.00 <b>(-64.04%)</b></td><td>0.01 <b>(+591.39%)</b></td><td>1688.20 <b>(+178.08%)</b></td><td>662.74 <b>(+32.96%)</b></td><td>306.60 <b>(-32.92%)</b></td><td>220.20 <b>(-50.80%)</b></td><td>628.28 <b>(+822.63%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>607.10 (n/a)</td><td>498.44 (n/a)</td><td>457.10 (n/a)</td><td>447.60 (n/a)</td><td>68.10 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(+21.07%)</b></td><td>0.01 (+16.62%)</td><td>0.02 (+18.67%)</td><td>0.01 (-8.06%)</td><td>0.00 <b>(+70.29%)</b></td><td>488.20 (+8.75%)</td><td>307.58 (-10.48%)</td><td>263.40 (-15.74%)</td><td>232.80 (-17.42%)</td><td>104.36 <b>(+56.57%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>448.90 (n/a)</td><td>343.60 (n/a)</td><td>312.60 (n/a)</td><td>281.90 (n/a)</td><td>66.65 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 <b>(+53.58%)</b></td><td>0.01 <b>(+57.92%)</b></td><td>0.02 <b>(+68.75%)</b></td><td>0.01 <b>(+267.75%)</b></td><td>0.01 <b>(+48.20%)</b></td><td>653.50 <b>(-72.81%)</b></td><td>382.02 <b>(-52.81%)</b></td><td>262.90 <b>(-40.75%)</b></td><td>147.60 <b>(-34.89%)</b></td><td>233.73 <b>(-74.06%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2403.20 (n/a)</td><td>809.54 (n/a)</td><td>443.70 (n/a)</td><td>226.70 (n/a)</td><td>900.92 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (-6.62%)</td><td>0.01 (-5.74%)</td><td>0.01 <b>(-27.83%)</b></td><td>0.01 (+9.37%)</td><td>0.00 (-12.54%)</td><td>563.90 (-8.56%)</td><td>395.70 (+2.77%)</td><td>412.30 <b>(+38.59%)</b></td><td>266.20 (+7.12%)</td><td>124.42 (-19.44%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>616.70 (n/a)</td><td>385.04 (n/a)</td><td>297.50 (n/a)</td><td>248.50 (n/a)</td><td>154.44 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+3.61%)</td><td>0.01 (-8.49%)</td><td>0.01 <b>(-33.03%)</b></td><td>0.01 (+1.60%)</td><td>0.00 (-16.93%)</td><td>608.40 (-1.57%)</td><td>411.76 (+4.47%)</td><td>428.10 <b>(+49.32%)</b></td><td>253.60 (-3.50%)</td><td>132.12 <b>(-20.50%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>618.10 (n/a)</td><td>394.14 (n/a)</td><td>286.70 (n/a)</td><td>262.80 (n/a)</td><td>166.20 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+18.99%)</td><td>0.01 (+18.30%)</td><td>0.01 <b>(+28.00%)</b></td><td>0.01 (+3.73%)</td><td>0.00 <b>(+48.14%)</b></td><td>591.20 (-3.60%)</td><td>381.82 (-12.33%)</td><td>347.80 <b>(-21.86%)</b></td><td>263.70 (-15.94%)</td><td>134.52 (+17.34%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>613.30 (n/a)</td><td>435.54 (n/a)</td><td>445.10 (n/a)</td><td>313.70 (n/a)</td><td>114.64 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (+19.79%)</td><td>0.01 (+8.52%)</td><td>0.01 (+5.96%)</td><td>0.01 (-1.96%)</td><td>0.00 <b>(+48.39%)</b></td><td>559.10 (+1.99%)</td><td>407.16 (-4.86%)</td><td>375.70 (-5.63%)</td><td>275.10 (-16.51%)</td><td>119.98 <b>(+27.23%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>548.20 (n/a)</td><td>427.98 (n/a)</td><td>398.10 (n/a)</td><td>329.50 (n/a)</td><td>94.31 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (-8.91%)</td><td>0.01 (-5.55%)</td><td>0.01 (-4.47%)</td><td>0.01 (+0.98%)</td><td>0.00 (-16.10%)</td><td>489.50 (-0.97%)</td><td>381.80 (+4.61%)</td><td>343.60 (+4.66%)</td><td>302.10 (+9.77%)</td><td>89.63 (-8.03%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>494.30 (n/a)</td><td>364.96 (n/a)</td><td>328.30 (n/a)</td><td>275.20 (n/a)</td><td>97.46 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 <b>(+43.47%)</b></td><td>0.01 (-1.08%)</td><td>0.01 (-11.42%)</td><td>0.01 <b>(-22.68%)</b></td><td>0.00 <b>(+431.57%)</b></td><td>605.70 <b>(+29.34%)</b></td><td>477.04 (+9.51%)</td><td>506.00 (+12.90%)</td><td>279.70 <b>(-30.28%)</b></td><td>138.35 <b>(+390.58%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>468.30 (n/a)</td><td>435.60 (n/a)</td><td>448.20 (n/a)</td><td>401.20 (n/a)</td><td>28.20 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 (+17.23%)</td><td>0.01 (+15.74%)</td><td>0.01 (-10.57%)</td><td>0.01 <b>(+43.99%)</b></td><td>0.00 <b>(+36.56%)</b></td><td>565.90 <b>(-30.55%)</b></td><td>448.34 (-12.85%)</td><td>537.90 (+11.81%)</td><td>285.60 (-14.70%)</td><td>139.25 <b>(-22.42%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>814.80 (n/a)</td><td>514.46 (n/a)</td><td>481.10 (n/a)</td><td>334.80 (n/a)</td><td>179.48 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (+15.53%)</td><td>0.02 <b>(+20.30%)</b></td><td>0.03 (+8.55%)</td><td>0.02 <b>(+46.21%)</b></td><td>0.01 (-8.22%)</td><td>449.60 <b>(-31.61%)</b></td><td>341.16 (-19.89%)</td><td>324.80 (-7.88%)</td><td>274.10 (-13.42%)</td><td>75.01 <b>(-47.18%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>657.40 (n/a)</td><td>425.84 (n/a)</td><td>352.60 (n/a)</td><td>316.60 (n/a)</td><td>142.02 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (+1.22%)</td><td>0.02 (+4.86%)</td><td>0.02 <b>(-22.06%)</b></td><td>0.02 <b>(+329.14%)</b></td><td>0.01 <b>(-48.08%)</b></td><td>451.50 <b>(-76.70%)</b></td><td>349.66 <b>(-44.97%)</b></td><td>355.30 <b>(+28.31%)</b></td><td>242.30 (-1.18%)</td><td>87.98 <b>(-88.02%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1937.70 (n/a)</td><td>635.36 (n/a)</td><td>276.90 (n/a)</td><td>245.20 (n/a)</td><td>734.10 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-6.61%)</td><td>0.03 <b>(+49.39%)</b></td><td>0.03 <b>(+93.50%)</b></td><td>0.03 <b>(+255.22%)</b></td><td>0.00 <b>(-73.01%)</b></td><td>324.90 <b>(-71.85%)</b></td><td>288.68 <b>(-48.49%)</b></td><td>275.30 <b>(-48.31%)</b></td><td>262.50 (+7.10%)</td><td>28.36 <b>(-92.02%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1154.20 (n/a)</td><td>560.40 (n/a)</td><td>532.60 (n/a)</td><td>245.10 (n/a)</td><td>355.19 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 <b>(-20.83%)</b></td><td>0.02 (-12.52%)</td><td>0.02 (-4.25%)</td><td>0.01 (-12.56%)</td><td>0.01 <b>(-26.88%)</b></td><td>709.50 (+14.36%)</td><td>435.84 (+9.68%)</td><td>407.40 (+4.46%)</td><td>266.40 <b>(+26.32%)</b></td><td>184.27 (+3.32%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>620.40 (n/a)</td><td>397.38 (n/a)</td><td>390.00 (n/a)</td><td>210.90 (n/a)</td><td>178.34 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 <b>(+42.05%)</b></td><td>0.02 <b>(+44.56%)</b></td><td>0.03 <b>(+37.33%)</b></td><td>0.02 <b>(+280.60%)</b></td><td>0.01 (+5.24%)</td><td>540.40 <b>(-73.73%)</b></td><td>381.44 <b>(-49.45%)</b></td><td>325.20 <b>(-27.18%)</b></td><td>259.20 <b>(-29.62%)</b></td><td>135.58 <b>(-81.44%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2056.80 (n/a)</td><td>754.52 (n/a)</td><td>446.60 (n/a)</td><td>368.30 (n/a)</td><td>730.59 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 <b>(-33.11%)</b></td><td>0.02 <b>(-28.20%)</b></td><td>0.02 <b>(-33.42%)</b></td><td>0.02 <b>(-22.10%)</b></td><td>0.01 <b>(-37.15%)</b></td><td>520.00 <b>(+28.36%)</b></td><td>367.44 <b>(+36.92%)</b></td><td>364.60 <b>(+50.16%)</b></td><td>265.80 <b>(+49.49%)</b></td><td>98.54 (+17.20%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>405.10 (n/a)</td><td>268.36 (n/a)</td><td>242.80 (n/a)</td><td>177.80 (n/a)</td><td>84.07 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 <b>(-26.88%)</b></td><td>0.02 (-7.36%)</td><td>0.02 (+7.58%)</td><td>0.01 <b>(+69.69%)</b></td><td>0.01 <b>(-45.76%)</b></td><td>619.90 <b>(-41.07%)</b></td><td>435.86 (-14.80%)</td><td>420.70 (-7.05%)</td><td>286.20 <b>(+36.74%)</b></td><td>151.64 <b>(-55.55%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1051.90 (n/a)</td><td>511.60 (n/a)</td><td>452.60 (n/a)</td><td>209.30 (n/a)</td><td>341.15 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (+17.91%)</td><td>0.02 (+3.18%)</td><td>0.03 <b>(+33.90%)</b></td><td>0.00 <b>(-71.10%)</b></td><td>0.01 <b>(+79.46%)</b></td><td>1942.60 <b>(+246.03%)</b></td><td>639.26 <b>(+65.63%)</b></td><td>274.60 <b>(-25.32%)</b></td><td>213.80 (-15.19%)</td><td>736.99 <b>(+470.35%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>561.40 (n/a)</td><td>385.96 (n/a)</td><td>367.70 (n/a)</td><td>252.10 (n/a)</td><td>129.22 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-9.12%)</td><td>0.02 (+5.64%)</td><td>0.03 <b>(+50.44%)</b></td><td>0.01 (-14.42%)</td><td>0.01 (+3.64%)</td><td>682.60 (+16.84%)</td><td>393.70 (-2.09%)</td><td>280.70 <b>(-33.55%)</b></td><td>270.20 (+10.02%)</td><td>179.77 <b>(+30.78%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>584.20 (n/a)</td><td>402.10 (n/a)</td><td>422.40 (n/a)</td><td>245.60 (n/a)</td><td>137.47 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-13.45%)</td><td>0.02 (-8.46%)</td><td>0.02 (-18.28%)</td><td>0.02 (+4.84%)</td><td>0.01 <b>(-23.50%)</b></td><td>469.50 (-4.61%)</td><td>373.20 (+6.17%)</td><td>388.10 <b>(+22.39%)</b></td><td>251.80 (+15.50%)</td><td>92.54 (-16.51%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>492.20 (n/a)</td><td>351.50 (n/a)</td><td>317.10 (n/a)</td><td>218.00 (n/a)</td><td>110.84 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-0.30%)</td><td>0.02 <b>(+27.13%)</b></td><td>0.02 <b>(+26.51%)</b></td><td>0.01 <b>(+85.15%)</b></td><td>0.01 <b>(-20.69%)</b></td><td>554.60 <b>(-45.99%)</b></td><td>435.94 <b>(-28.10%)</b></td><td>447.60 <b>(-20.96%)</b></td><td>315.80 (+0.29%)</td><td>111.19 <b>(-57.78%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1026.80 (n/a)</td><td>606.28 (n/a)</td><td>566.30 (n/a)</td><td>314.90 (n/a)</td><td>263.35 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (+18.53%)</td><td>0.02 <b>(+38.24%)</b></td><td>0.02 (+7.52%)</td><td>0.01 <b>(+211.97%)</b></td><td>0.01 (-12.73%)</td><td>790.90 <b>(-67.95%)</b></td><td>541.16 <b>(-52.74%)</b></td><td>506.30 (-7.00%)</td><td>284.20 (-15.62%)</td><td>220.76 <b>(-77.11%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2467.40 (n/a)</td><td>1145.06 (n/a)</td><td>544.40 (n/a)</td><td>336.80 (n/a)</td><td>964.60 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (-12.70%)</td><td>0.05 (+3.70%)</td><td>0.05 <b>(+35.73%)</b></td><td>0.03 (-12.16%)</td><td>0.01 (-18.33%)</td><td>606.00 (+13.87%)</td><td>374.60 (-4.48%)</td><td>325.20 <b>(-26.33%)</b></td><td>282.40 (+14.56%)</td><td>135.07 (+9.72%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>532.20 (n/a)</td><td>392.18 (n/a)</td><td>441.40 (n/a)</td><td>246.50 (n/a)</td><td>123.10 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (-9.97%)</td><td>0.04 <b>(-21.99%)</b></td><td>0.04 <b>(-37.76%)</b></td><td>0.03 (-4.51%)</td><td>0.01 (-0.16%)</td><td>534.70 (+4.74%)</td><td>406.04 <b>(+29.16%)</b></td><td>453.80 <b>(+60.69%)</b></td><td>264.90 (+11.07%)</td><td>122.91 (+9.54%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>510.50 (n/a)</td><td>314.36 (n/a)</td><td>282.40 (n/a)</td><td>238.50 (n/a)</td><td>112.21 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 <b>(-22.08%)</b></td><td>0.04 (-3.30%)</td><td>0.04 (+16.16%)</td><td>0.03 (-8.76%)</td><td>0.01 <b>(-30.15%)</b></td><td>535.60 (+9.60%)</td><td>388.54 (+0.19%)</td><td>377.20 (-13.92%)</td><td>286.90 <b>(+28.37%)</b></td><td>107.41 (-8.22%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>488.70 (n/a)</td><td>387.82 (n/a)</td><td>438.20 (n/a)</td><td>223.50 (n/a)</td><td>117.03 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (+2.05%)</td><td>0.05 (+7.86%)</td><td>0.06 <b>(+47.07%)</b></td><td>0.03 (+9.96%)</td><td>0.02 (-5.32%)</td><td>527.90 (-9.06%)</td><td>359.38 (-8.66%)</td><td>293.90 <b>(-32.01%)</b></td><td>215.10 (-2.00%)</td><td>148.37 (-5.83%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>580.50 (n/a)</td><td>393.44 (n/a)</td><td>432.30 (n/a)</td><td>219.50 (n/a)</td><td>157.55 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (-2.93%)</td><td>0.05 (+10.42%)</td><td>0.06 <b>(+36.32%)</b></td><td>0.01 <b>(-48.56%)</b></td><td>0.02 (+8.05%)</td><td>1114.20 <b>(+94.42%)</b></td><td>428.08 (+10.03%)</td><td>258.10 <b>(-26.63%)</b></td><td>231.00 (+2.99%)</td><td>383.94 <b>(+129.55%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>573.10 (n/a)</td><td>389.06 (n/a)</td><td>351.80 (n/a)</td><td>224.30 (n/a)</td><td>167.25 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 <b>(+22.47%)</b></td><td>0.06 <b>(+32.53%)</b></td><td>0.06 <b>(+54.90%)</b></td><td>0.03 (+13.75%)</td><td>0.02 (+13.11%)</td><td>479.90 (-12.09%)</td><td>297.04 <b>(-24.91%)</b></td><td>270.80 <b>(-35.43%)</b></td><td>190.60 (-18.34%)</td><td>109.51 (-14.35%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>545.90 (n/a)</td><td>395.60 (n/a)</td><td>419.40 (n/a)</td><td>233.40 (n/a)</td><td>127.86 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 <b>(-46.63%)</b></td><td>0.03 <b>(-32.18%)</b></td><td>0.03 <b>(-34.47%)</b></td><td>0.03 (+18.47%)</td><td>0.00 <b>(-87.32%)</b></td><td>506.20 (-15.59%)</td><td>481.38 <b>(+33.64%)</b></td><td>490.50 <b>(+52.61%)</b></td><td>437.60 <b>(+87.33%)</b></td><td>27.17 <b>(-80.93%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>599.70 (n/a)</td><td>360.22 (n/a)</td><td>321.40 (n/a)</td><td>233.60 (n/a)</td><td>142.44 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (-1.69%)</td><td>0.03 (+7.60%)</td><td>0.03 (+1.15%)</td><td>0.03 <b>(+30.03%)</b></td><td>0.00 <b>(-60.32%)</b></td><td>512.90 <b>(-23.09%)</b></td><td>479.54 (-8.69%)</td><td>482.10 (-1.13%)</td><td>449.40 (+1.72%)</td><td>26.65 <b>(-69.66%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>666.90 (n/a)</td><td>525.18 (n/a)</td><td>487.60 (n/a)</td><td>441.80 (n/a)</td><td>87.83 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (-10.52%)</td><td>0.04 (+14.63%)</td><td>0.04 (+11.23%)</td><td>0.03 <b>(+32.58%)</b></td><td>0.01 <b>(-22.85%)</b></td><td>566.60 <b>(-24.56%)</b></td><td>407.06 (-18.25%)</td><td>438.90 (-10.10%)</td><td>275.80 (+11.75%)</td><td>121.60 <b>(-35.83%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>751.10 (n/a)</td><td>497.92 (n/a)</td><td>488.20 (n/a)</td><td>246.80 (n/a)</td><td>189.50 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (-3.90%)</td><td>0.05 (-5.75%)</td><td>0.05 (-4.09%)</td><td>0.03 (-12.79%)</td><td>0.01 (+8.68%)</td><td>508.10 (+14.67%)</td><td>363.80 (+8.36%)</td><td>311.70 (+4.28%)</td><td>254.30 (+4.05%)</td><td>114.90 <b>(+28.52%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>443.10 (n/a)</td><td>335.74 (n/a)</td><td>298.90 (n/a)</td><td>244.40 (n/a)</td><td>89.40 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (-9.14%)</td><td>0.03 (-13.31%)</td><td>0.03 <b>(-24.42%)</b></td><td>0.02 <b>(+33.22%)</b></td><td>0.01 <b>(-24.77%)</b></td><td>988.00 <b>(-24.94%)</b></td><td>598.18 (+0.60%)</td><td>499.20 <b>(+32.31%)</b></td><td>336.90 (+10.06%)</td><td>254.87 <b>(-39.14%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1316.20 (n/a)</td><td>594.60 (n/a)</td><td>377.30 (n/a)</td><td>306.10 (n/a)</td><td>418.78 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 (-3.19%)</td><td>0.03 (-10.35%)</td><td>0.03 (+0.95%)</td><td>0.02 (-15.92%)</td><td>0.01 (+5.75%)</td><td>742.20 (+18.94%)</td><td>522.62 (+15.01%)</td><td>472.10 (-0.94%)</td><td>301.40 (+3.29%)</td><td>183.90 <b>(+36.58%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>624.00 (n/a)</td><td>454.42 (n/a)</td><td>476.60 (n/a)</td><td>291.80 (n/a)</td><td>134.65 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.11 <b>(+42.88%)</b></td><td>0.08 <b>(+48.81%)</b></td><td>0.08 (+16.98%)</td><td>0.06 <b>(+279.37%)</b></td><td>0.02 (-15.34%)</td><td>546.50 <b>(-73.64%)</b></td><td>407.26 <b>(-49.97%)</b></td><td>398.70 (-14.53%)</td><td>301.70 <b>(-30.02%)</b></td><td>103.60 <b>(-85.38%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>2073.30 (n/a)</td><td>814.08 (n/a)</td><td>466.50 (n/a)</td><td>431.10 (n/a)</td><td>708.70 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 <b>(+22.58%)</b></td><td>0.09 (-2.45%)</td><td>0.07 <b>(-31.45%)</b></td><td>0.06 (-9.89%)</td><td>0.04 <b>(+57.81%)</b></td><td>559.40 (+10.97%)</td><td>421.28 (+10.84%)</td><td>494.60 <b>(+45.86%)</b></td><td>209.80 (-18.43%)</td><td>158.10 <b>(+40.06%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>504.10 (n/a)</td><td>380.08 (n/a)</td><td>339.10 (n/a)</td><td>257.20 (n/a)</td><td>112.88 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (+6.81%)</td><td>0.10 (-1.22%)</td><td>0.12 (+10.51%)</td><td>0.06 <b>(-23.97%)</b></td><td>0.04 <b>(+84.01%)</b></td><td>582.80 <b>(+31.53%)</b></td><td>367.96 (+12.66%)</td><td>270.80 (-9.52%)</td><td>233.90 (-6.37%)</td><td>163.01 <b>(+121.26%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>443.10 (n/a)</td><td>326.62 (n/a)</td><td>299.30 (n/a)</td><td>249.80 (n/a)</td><td>73.67 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 <b>(-22.10%)</b></td><td>0.09 (-8.39%)</td><td>0.08 <b>(+23.28%)</b></td><td>0.05 (-12.73%)</td><td>0.03 <b>(-31.06%)</b></td><td>618.50 (+14.58%)</td><td>427.14 (+4.28%)</td><td>400.40 (-18.88%)</td><td>262.10 <b>(+28.35%)</b></td><td>150.91 (-1.44%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>539.80 (n/a)</td><td>409.62 (n/a)</td><td>493.60 (n/a)</td><td>204.20 (n/a)</td><td>153.12 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (+11.50%)</td><td>0.11 (+12.04%)</td><td>0.11 (+14.83%)</td><td>0.07 (+1.67%)</td><td>0.02 <b>(+22.55%)</b></td><td>486.40 (-1.64%)</td><td>323.26 (-9.51%)</td><td>298.30 (-12.93%)</td><td>253.10 (-10.31%)</td><td>93.08 (+12.10%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>494.50 (n/a)</td><td>357.22 (n/a)</td><td>342.60 (n/a)</td><td>282.20 (n/a)</td><td>83.03 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (+19.28%)</td><td>0.10 (+3.94%)</td><td>0.11 (-1.99%)</td><td>0.05 (-3.47%)</td><td>0.04 <b>(+38.27%)</b></td><td>672.50 (+3.60%)</td><td>397.44 (+3.10%)</td><td>308.60 (+2.02%)</td><td>205.30 (-16.17%)</td><td>195.51 <b>(+20.50%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>649.10 (n/a)</td><td>385.48 (n/a)</td><td>302.50 (n/a)</td><td>244.90 (n/a)</td><td>162.25 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (+18.41%)</td><td>0.09 (+4.02%)</td><td>0.08 (+6.29%)</td><td>0.05 <b>(-27.67%)</b></td><td>0.04 <b>(+55.27%)</b></td><td>674.40 <b>(+38.25%)</b></td><td>422.54 (+4.79%)</td><td>436.80 (-5.90%)</td><td>245.70 (-15.54%)</td><td>176.89 <b>(+72.88%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>487.80 (n/a)</td><td>403.24 (n/a)</td><td>464.20 (n/a)</td><td>290.90 (n/a)</td><td>102.32 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (+4.49%)</td><td>0.10 (+8.97%)</td><td>0.12 (+11.17%)</td><td>0.06 (+9.05%)</td><td>0.03 (+6.26%)</td><td>515.60 (-8.31%)</td><td>346.12 (-8.47%)</td><td>265.90 (-10.05%)</td><td>236.80 (-4.32%)</td><td>128.56 (-8.75%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>562.30 (n/a)</td><td>378.16 (n/a)</td><td>295.60 (n/a)</td><td>247.50 (n/a)</td><td>140.89 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 <b>(+30.49%)</b></td><td>0.11 <b>(+64.56%)</b></td><td>0.12 <b>(+94.76%)</b></td><td>0.06 (+1.53%)</td><td>0.03 <b>(+44.57%)</b></td><td>588.70 (-1.51%)</td><td>322.52 <b>(-36.22%)</b></td><td>274.10 <b>(-48.65%)</b></td><td>225.10 <b>(-23.38%)</b></td><td>150.20 <b>(+21.63%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>597.70 (n/a)</td><td>505.70 (n/a)</td><td>533.80 (n/a)</td><td>293.80 (n/a)</td><td>123.50 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (+12.71%)</td><td>0.09 (+4.44%)</td><td>0.11 <b>(+49.47%)</b></td><td>0.05 <b>(-28.05%)</b></td><td>0.04 <b>(+44.65%)</b></td><td>691.80 <b>(+39.00%)</b></td><td>416.92 (+5.73%)</td><td>298.70 <b>(-33.09%)</b></td><td>242.70 (-11.29%)</td><td>197.76 <b>(+86.58%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>497.70 (n/a)</td><td>394.32 (n/a)</td><td>446.40 (n/a)</td><td>273.60 (n/a)</td><td>105.99 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (-16.84%)</td><td>0.09 (+14.91%)</td><td>0.09 <b>(+33.94%)</b></td><td>0.07 <b>(+37.49%)</b></td><td>0.01 <b>(-46.02%)</b></td><td>467.60 <b>(-27.28%)</b></td><td>382.78 (-17.83%)</td><td>351.90 <b>(-25.35%)</b></td><td>326.00 <b>(+20.25%)</b></td><td>66.17 <b>(-50.71%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>643.00 (n/a)</td><td>465.84 (n/a)</td><td>471.40 (n/a)</td><td>271.10 (n/a)</td><td>134.26 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.18 <b>(+61.02%)</b></td><td>0.10 <b>(+56.52%)</b></td><td>0.10 <b>(+89.59%)</b></td><td>0.04 (+1.54%)</td><td>0.05 <b>(+95.18%)</b></td><td>761.40 (-1.50%)</td><td>403.20 <b>(-26.66%)</b></td><td>317.90 <b>(-47.25%)</b></td><td>178.50 <b>(-37.91%)</b></td><td>232.42 <b>(+28.53%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>773.00 (n/a)</td><td>549.78 (n/a)</td><td>602.60 (n/a)</td><td>287.50 (n/a)</td><td>180.83 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (+1.76%)</td><td>0.08 (-6.14%)</td><td>0.08 (-10.57%)</td><td>0.05 (-5.32%)</td><td>0.02 (+4.86%)</td><td>529.40 (+5.63%)</td><td>341.52 (+7.39%)</td><td>308.30 (+11.82%)</td><td>245.50 (-1.72%)</td><td>113.96 (+8.27%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>501.20 (n/a)</td><td>318.02 (n/a)</td><td>275.70 (n/a)</td><td>249.80 (n/a)</td><td>105.26 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.21 (-3.47%)</td><td>0.17 (-9.54%)</td><td>0.18 (-0.39%)</td><td>0.10 <b>(-40.29%)</b></td><td>0.04 <b>(+125.08%)</b></td><td>501.40 <b>(+67.47%)</b></td><td>315.62 (+17.64%)</td><td>270.50 (+0.41%)</td><td>236.70 (+3.59%)</td><td>107.06 <b>(+316.07%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>299.40 (n/a)</td><td>268.30 (n/a)</td><td>269.40 (n/a)</td><td>228.50 (n/a)</td><td>25.73 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.70 <b>(-33.57%)</b></td><td>2.58 (-18.54%)</td><td>2.57 (-11.79%)</td><td>2.39 (-10.07%)</td><td>0.13 <b>(-79.20%)</b></td><td>4394.10 (+11.20%)</td><td>4076.18 (+19.62%)</td><td>4078.30 (+13.36%)</td><td>3879.80 <b>(+50.53%)</b></td><td>207.39 <b>(-65.86%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.07 (n/a)</td><td>3.16 (n/a)</td><td>2.91 (n/a)</td><td>2.65 (n/a)</td><td>0.61 (n/a)</td><td>3951.50 (n/a)</td><td>3407.64 (n/a)</td><td>3597.60 (n/a)</td><td>2577.40 (n/a)</td><td>607.54 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (-4.56%)</td><td>0.14 (+12.87%)</td><td>0.16 (-3.13%)</td><td>0.08 <b>(+265.10%)</b></td><td>0.04 <b>(-45.75%)</b></td><td>515.60 <b>(-72.61%)</b></td><td>320.70 <b>(-48.08%)</b></td><td>263.20 (+3.22%)</td><td>250.50 (+4.77%)</td><td>112.81 <b>(-84.20%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>0.07 (n/a)</td><td>1882.70 (n/a)</td><td>617.64 (n/a)</td><td>255.00 (n/a)</td><td>239.10 (n/a)</td><td>713.75 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+9.31%)</td><td>0.02 (+5.58%)</td><td>0.02 (+1.86%)</td><td>0.01 (-4.39%)</td><td>0.00 <b>(+25.80%)</b></td><td>430.40 (+4.57%)</td><td>303.74 (-3.93%)</td><td>293.80 (-1.84%)</td><td>237.10 (-8.53%)</td><td>74.99 <b>(+23.64%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>411.60 (n/a)</td><td>316.16 (n/a)</td><td>299.30 (n/a)</td><td>259.20 (n/a)</td><td>60.65 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+3.22%)</td><td>0.01 <b>(-23.56%)</b></td><td>0.01 <b>(-49.71%)</b></td><td>0.01 (+1.74%)</td><td>0.01 (+11.40%)</td><td>524.40 (-1.71%)</td><td>389.88 <b>(+32.55%)</b></td><td>459.80 <b>(+98.88%)</b></td><td>203.30 (-3.10%)</td><td>137.28 (+1.30%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>533.50 (n/a)</td><td>294.14 (n/a)</td><td>231.20 (n/a)</td><td>209.80 (n/a)</td><td>135.51 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (+16.09%)</td><td>0.02 (+11.00%)</td><td>0.02 (+9.68%)</td><td>0.01 (+17.24%)</td><td>0.01 (+10.61%)</td><td>509.70 (-14.69%)</td><td>290.70 (-11.14%)</td><td>247.10 (-8.82%)</td><td>177.10 (-13.86%)</td><td>127.61 (-18.37%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>597.50 (n/a)</td><td>327.16 (n/a)</td><td>271.00 (n/a)</td><td>205.60 (n/a)</td><td>156.32 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(+32.29%)</b></td><td>0.01 (+0.93%)</td><td>0.01 (-15.50%)</td><td>0.00 <b>(-73.42%)</b></td><td>0.01 <b>(+108.85%)</b></td><td>2071.50 <b>(+276.16%)</b></td><td>762.72 <b>(+78.72%)</b></td><td>582.10 (+18.34%)</td><td>197.70 <b>(-24.40%)</b></td><td>767.77 <b>(+443.54%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>550.70 (n/a)</td><td>426.78 (n/a)</td><td>491.90 (n/a)</td><td>261.50 (n/a)</td><td>141.25 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (-9.50%)</td><td>0.01 (-10.29%)</td><td>0.01 (-7.96%)</td><td>0.01 (+16.85%)</td><td>0.00 <b>(-34.95%)</b></td><td>501.10 (-14.42%)</td><td>409.68 (+4.58%)</td><td>453.70 (+8.64%)</td><td>270.30 (+10.51%)</td><td>95.21 <b>(-34.13%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>585.50 (n/a)</td><td>391.72 (n/a)</td><td>417.60 (n/a)</td><td>244.60 (n/a)</td><td>144.54 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+4.43%)</td><td>0.01 <b>(+20.90%)</b></td><td>0.02 <b>(+73.36%)</b></td><td>0.01 <b>(+30.17%)</b></td><td>0.00 (-12.29%)</td><td>471.30 <b>(-23.17%)</b></td><td>338.90 <b>(-21.59%)</b></td><td>272.70 <b>(-42.32%)</b></td><td>225.40 (-4.25%)</td><td>116.01 <b>(-30.88%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>613.40 (n/a)</td><td>432.20 (n/a)</td><td>472.80 (n/a)</td><td>235.40 (n/a)</td><td>167.83 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(-34.06%)</b></td><td>0.01 <b>(-28.58%)</b></td><td>0.01 <b>(-51.51%)</b></td><td>0.01 (+11.59%)</td><td>0.00 <b>(-42.29%)</b></td><td>583.00 (-10.39%)</td><td>445.10 <b>(+26.22%)</b></td><td>521.90 <b>(+106.20%)</b></td><td>272.20 <b>(+51.64%)</b></td><td>143.41 <b>(-24.45%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>650.60 (n/a)</td><td>352.64 (n/a)</td><td>253.10 (n/a)</td><td>179.50 (n/a)</td><td>189.82 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+0.55%)</td><td>0.01 (+14.81%)</td><td>0.01 (+8.29%)</td><td>0.01 (-4.07%)</td><td>0.00 (+13.25%)</td><td>635.80 (+4.25%)</td><td>412.10 (-10.36%)</td><td>429.20 (-7.66%)</td><td>251.60 (-0.55%)</td><td>157.02 (+18.44%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>609.90 (n/a)</td><td>459.72 (n/a)</td><td>464.80 (n/a)</td><td>253.00 (n/a)</td><td>132.58 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(+25.81%)</b></td><td>0.01 (-7.02%)</td><td>0.01 <b>(-21.53%)</b></td><td>0.01 <b>(-22.02%)</b></td><td>0.01 <b>(+122.86%)</b></td><td>545.00 <b>(+28.24%)</b></td><td>396.46 (+18.01%)</td><td>423.80 <b>(+27.42%)</b></td><td>206.30 <b>(-20.53%)</b></td><td>133.90 <b>(+122.18%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>425.00 (n/a)</td><td>335.96 (n/a)</td><td>332.60 (n/a)</td><td>259.60 (n/a)</td><td>60.27 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+0.15%)</td><td>0.01 (+3.34%)</td><td>0.01 (+10.21%)</td><td>0.01 (+15.89%)</td><td>0.00 (-16.70%)</td><td>539.20 (-13.70%)</td><td>391.66 (-7.49%)</td><td>437.40 (-9.27%)</td><td>254.90 (-0.12%)</td><td>118.15 <b>(-25.40%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>624.80 (n/a)</td><td>423.38 (n/a)</td><td>482.10 (n/a)</td><td>255.20 (n/a)</td><td>158.38 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.01 <b>(-25.91%)</b></td><td>0.01 <b>(-20.30%)</b></td><td>0.01 (+10.55%)</td><td>0.00 <b>(-43.05%)</b></td><td>0.00 <b>(-26.01%)</b></td><td>1047.90 <b>(+75.59%)</b></td><td>567.24 <b>(+29.75%)</b></td><td>445.10 (-9.55%)</td><td>349.40 <b>(+34.96%)</b></td><td>290.21 <b>(+79.27%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>596.80 (n/a)</td><td>437.18 (n/a)</td><td>492.10 (n/a)</td><td>258.90 (n/a)</td><td>161.89 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+18.04%)</td><td>0.01 (-1.08%)</td><td>0.01 <b>(-20.18%)</b></td><td>0.01 (+7.27%)</td><td>0.00 <b>(+28.21%)</b></td><td>496.10 (-6.78%)</td><td>410.76 (+2.29%)</td><td>437.20 <b>(+25.27%)</b></td><td>258.10 (-15.29%)</td><td>98.55 (-0.72%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>532.20 (n/a)</td><td>401.58 (n/a)</td><td>349.00 (n/a)</td><td>304.70 (n/a)</td><td>99.27 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-16.39%)</td><td>0.02 (-14.60%)</td><td>0.02 (-7.89%)</td><td>0.02 (+10.52%)</td><td>0.00 <b>(-39.53%)</b></td><td>455.00 (-9.52%)</td><td>388.90 (+13.11%)</td><td>373.50 (+8.58%)</td><td>296.90 (+19.62%)</td><td>65.88 <b>(-33.58%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>502.90 (n/a)</td><td>343.82 (n/a)</td><td>344.00 (n/a)</td><td>248.20 (n/a)</td><td>99.18 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 <b>(+21.15%)</b></td><td>0.04 (+8.35%)</td><td>0.03 <b>(-31.86%)</b></td><td>0.03 <b>(+330.88%)</b></td><td>0.02 (-16.92%)</td><td>466.30 <b>(-76.79%)</b></td><td>377.46 <b>(-43.63%)</b></td><td>462.10 <b>(+46.74%)</b></td><td>194.80 (-17.46%)</td><td>124.66 <b>(-83.57%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2009.20 (n/a)</td><td>669.62 (n/a)</td><td>314.90 (n/a)</td><td>236.00 (n/a)</td><td>758.69 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-7.50%)</td><td>0.02 (-14.90%)</td><td>0.02 (-3.25%)</td><td>0.01 (-17.35%)</td><td>0.01 (-6.03%)</td><td>639.60 <b>(+21.00%)</b></td><td>470.10 (+18.38%)</td><td>452.40 (+3.36%)</td><td>260.20 (+8.10%)</td><td>141.66 (+18.46%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.60 (n/a)</td><td>397.12 (n/a)</td><td>437.70 (n/a)</td><td>240.70 (n/a)</td><td>119.58 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (-9.72%)</td><td>0.03 (-2.25%)</td><td>0.02 (-3.99%)</td><td>0.02 <b>(+54.28%)</b></td><td>0.01 <b>(-42.95%)</b></td><td>460.90 <b>(-35.18%)</b></td><td>393.34 (-8.40%)</td><td>441.10 (+4.16%)</td><td>271.70 (+10.76%)</td><td>82.04 <b>(-56.59%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>711.00 (n/a)</td><td>429.40 (n/a)</td><td>423.50 (n/a)</td><td>245.30 (n/a)</td><td>189.02 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 (+3.59%)</td><td>0.03 <b>(+20.66%)</b></td><td>0.03 <b>(+37.34%)</b></td><td>0.02 <b>(+20.87%)</b></td><td>0.01 <b>(-25.63%)</b></td><td>502.70 (-17.28%)</td><td>322.38 <b>(-23.43%)</b></td><td>298.00 <b>(-27.17%)</b></td><td>230.70 (-3.47%)</td><td>106.39 <b>(-38.81%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>607.70 (n/a)</td><td>421.04 (n/a)</td><td>409.20 (n/a)</td><td>239.00 (n/a)</td><td>173.87 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-15.68%)</td><td>0.02 <b>(-37.63%)</b></td><td>0.02 <b>(-39.97%)</b></td><td>0.01 <b>(-57.19%)</b></td><td>0.01 (+4.43%)</td><td>1384.00 <b>(+133.59%)</b></td><td>758.20 <b>(+81.14%)</b></td><td>652.00 <b>(+66.58%)</b></td><td>342.20 (+18.61%)</td><td>385.61 <b>(+194.04%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>592.50 (n/a)</td><td>418.58 (n/a)</td><td>391.40 (n/a)</td><td>288.50 (n/a)</td><td>131.14 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (-11.82%)</td><td>0.02 (-6.82%)</td><td>0.02 (-18.90%)</td><td>0.01 (+4.96%)</td><td>0.01 (-16.43%)</td><td>596.00 (-4.73%)</td><td>401.42 (+1.62%)</td><td>383.90 <b>(+23.32%)</b></td><td>244.90 (+13.43%)</td><td>161.49 (-16.98%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>625.60 (n/a)</td><td>395.02 (n/a)</td><td>311.30 (n/a)</td><td>215.90 (n/a)</td><td>194.53 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 <b>(+37.29%)</b></td><td>0.03 <b>(+29.83%)</b></td><td>0.03 <b>(+47.66%)</b></td><td>0.02 (+8.28%)</td><td>0.01 <b>(+76.53%)</b></td><td>567.30 (-7.64%)</td><td>397.20 (-19.63%)</td><td>335.00 <b>(-32.28%)</b></td><td>262.30 <b>(-27.14%)</b></td><td>128.94 <b>(+21.26%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>614.20 (n/a)</td><td>494.24 (n/a)</td><td>494.70 (n/a)</td><td>360.00 (n/a)</td><td>106.33 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 <b>(-41.67%)</b></td><td>0.02 (-12.95%)</td><td>0.02 (-9.50%)</td><td>0.01 <b>(+247.15%)</b></td><td>0.01 <b>(-67.10%)</b></td><td>577.90 <b>(-71.19%)</b></td><td>380.40 <b>(-39.39%)</b></td><td>333.60 (+10.50%)</td><td>306.50 <b>(+71.42%)</b></td><td>113.13 <b>(-85.40%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>2006.10 (n/a)</td><td>627.62 (n/a)</td><td>301.90 (n/a)</td><td>178.80 (n/a)</td><td>775.08 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.04 <b>(-27.10%)</b></td><td>0.03 (-17.84%)</td><td>0.02 (-4.03%)</td><td>0.02 (+12.87%)</td><td>0.01 <b>(-43.78%)</b></td><td>552.40 (-11.42%)</td><td>391.30 (+4.45%)</td><td>418.20 (+4.19%)</td><td>215.10 <b>(+37.18%)</b></td><td>136.88 <b>(-30.09%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>623.60 (n/a)</td><td>374.62 (n/a)</td><td>401.40 (n/a)</td><td>156.80 (n/a)</td><td>195.79 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.03 (+3.28%)</td><td>0.02 (+14.45%)</td><td>0.02 <b>(+21.24%)</b></td><td>0.02 <b>(+21.14%)</b></td><td>0.00 <b>(-25.48%)</b></td><td>496.40 (-17.45%)</td><td>366.24 (-15.49%)</td><td>342.00 (-17.53%)</td><td>296.40 (-3.17%)</td><td>77.00 <b>(-37.56%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.30 (n/a)</td><td>433.36 (n/a)</td><td>414.70 (n/a)</td><td>306.10 (n/a)</td><td>123.30 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (-14.35%)</td><td>0.06 (+17.83%)</td><td>0.06 <b>(+33.82%)</b></td><td>0.04 <b>(+22.78%)</b></td><td>0.01 <b>(-40.65%)</b></td><td>432.20 (-18.56%)</td><td>290.02 <b>(-22.09%)</b></td><td>255.80 <b>(-25.27%)</b></td><td>247.30 (+16.76%)</td><td>79.72 <b>(-45.40%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>530.70 (n/a)</td><td>372.26 (n/a)</td><td>342.30 (n/a)</td><td>211.80 (n/a)</td><td>146.00 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (-18.63%)</td><td>0.06 <b>(-24.32%)</b></td><td>0.06 <b>(-36.01%)</b></td><td>0.01 <b>(-65.44%)</b></td><td>0.04 (+0.72%)</td><td>1911.40 <b>(+189.34%)</b></td><td>681.08 <b>(+85.89%)</b></td><td>441.80 <b>(+56.28%)</b></td><td>243.60 <b>(+22.91%)</b></td><td>700.42 <b>(+258.01%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>660.60 (n/a)</td><td>366.38 (n/a)</td><td>282.70 (n/a)</td><td>198.20 (n/a)</td><td>195.64 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (-4.75%)</td><td>0.07 <b>(+21.70%)</b></td><td>0.07 (+11.77%)</td><td>0.06 <b>(+75.12%)</b></td><td>0.00 <b>(-75.34%)</b></td><td>274.00 <b>(-42.89%)</b></td><td>245.46 <b>(-24.94%)</b></td><td>240.50 (-10.53%)</td><td>229.90 (+5.03%)</td><td>16.97 <b>(-85.34%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>479.80 (n/a)</td><td>327.00 (n/a)</td><td>268.80 (n/a)</td><td>218.90 (n/a)</td><td>115.72 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (-9.80%)</td><td>0.07 (+2.29%)</td><td>0.07 (+4.52%)</td><td>0.04 (-6.40%)</td><td>0.02 (-3.83%)</td><td>569.90 (+6.82%)</td><td>353.58 (-1.91%)</td><td>281.90 (-4.31%)</td><td>234.20 (+10.84%)</td><td>146.30 (+6.04%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>533.50 (n/a)</td><td>360.46 (n/a)</td><td>294.60 (n/a)</td><td>211.30 (n/a)</td><td>137.96 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (-13.95%)</td><td>0.05 (-6.09%)</td><td>0.05 (-16.58%)</td><td>0.03 (+14.11%)</td><td>0.01 <b>(-38.17%)</b></td><td>511.10 (-12.36%)</td><td>356.28 (-3.20%)</td><td>356.30 (+19.89%)</td><td>246.40 (+16.17%)</td><td>102.08 <b>(-38.63%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>583.20 (n/a)</td><td>368.06 (n/a)</td><td>297.20 (n/a)</td><td>212.10 (n/a)</td><td>166.32 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (-15.12%)</td><td>0.06 (+1.66%)</td><td>0.04 (-10.47%)</td><td>0.04 (+3.89%)</td><td>0.02 (-10.81%)</td><td>548.00 (-3.74%)</td><td>408.72 (-1.79%)</td><td>488.10 (+11.69%)</td><td>248.00 (+17.81%)</td><td>139.53 (+6.99%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>569.30 (n/a)</td><td>416.16 (n/a)</td><td>437.00 (n/a)</td><td>210.50 (n/a)</td><td>130.41 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (-5.31%)</td><td>0.05 (+1.58%)</td><td>0.05 <b>(+42.84%)</b></td><td>0.03 (-13.37%)</td><td>0.02 (-16.65%)</td><td>590.60 (+15.42%)</td><td>376.94 (-3.13%)</td><td>313.90 <b>(-30.00%)</b></td><td>254.90 (+5.59%)</td><td>141.49 (+4.19%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>511.70 (n/a)</td><td>389.10 (n/a)</td><td>448.40 (n/a)</td><td>241.40 (n/a)</td><td>135.80 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 <b>(+26.91%)</b></td><td>0.06 <b>(+33.86%)</b></td><td>0.06 <b>(+60.24%)</b></td><td>0.04 <b>(+37.23%)</b></td><td>0.01 <b>(+22.68%)</b></td><td>437.30 <b>(-27.13%)</b></td><td>339.16 <b>(-25.59%)</b></td><td>295.90 <b>(-37.60%)</b></td><td>258.60 <b>(-21.21%)</b></td><td>80.75 <b>(-26.09%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>600.10 (n/a)</td><td>455.78 (n/a)</td><td>474.20 (n/a)</td><td>328.20 (n/a)</td><td>109.26 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (+10.30%)</td><td>0.05 (+17.79%)</td><td>0.06 <b>(+26.72%)</b></td><td>0.04 (+18.94%)</td><td>0.01 (-4.49%)</td><td>438.30 (-15.94%)</td><td>317.18 (-17.24%)</td><td>297.00 <b>(-21.09%)</b></td><td>233.30 (-9.33%)</td><td>87.79 <b>(-27.83%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>521.40 (n/a)</td><td>383.24 (n/a)</td><td>376.40 (n/a)</td><td>257.30 (n/a)</td><td>121.64 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (+0.76%)</td><td>0.06 <b>(+27.65%)</b></td><td>0.07 <b>(+90.91%)</b></td><td>0.04 <b>(+31.31%)</b></td><td>0.02 (-13.26%)</td><td>478.60 <b>(-23.84%)</b></td><td>343.76 <b>(-25.69%)</b></td><td>282.80 <b>(-47.62%)</b></td><td>229.50 (-0.74%)</td><td>116.14 <b>(-31.08%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>628.40 (n/a)</td><td>462.62 (n/a)</td><td>539.90 (n/a)</td><td>231.20 (n/a)</td><td>168.50 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.05 <b>(-20.63%)</b></td><td>0.03 <b>(-24.28%)</b></td><td>0.03 <b>(-31.71%)</b></td><td>0.02 (-3.97%)</td><td>0.01 <b>(-38.03%)</b></td><td>673.60 (+4.14%)</td><td>526.12 <b>(+24.85%)</b></td><td>509.40 <b>(+46.42%)</b></td><td>338.20 <b>(+26.01%)</b></td><td>128.03 <b>(-21.49%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>646.80 (n/a)</td><td>421.40 (n/a)</td><td>347.90 (n/a)</td><td>268.40 (n/a)</td><td>163.07 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 <b>(-21.71%)</b></td><td>0.07 <b>(-30.21%)</b></td><td>0.06 <b>(-44.31%)</b></td><td>0.06 (+3.55%)</td><td>0.01 <b>(-41.71%)</b></td><td>517.00 (-3.42%)</td><td>459.92 <b>(+37.69%)</b></td><td>511.30 <b>(+79.53%)</b></td><td>335.00 <b>(+27.72%)</b></td><td>80.27 <b>(-29.66%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>535.30 (n/a)</td><td>334.02 (n/a)</td><td>284.80 (n/a)</td><td>262.30 (n/a)</td><td>114.10 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (+19.86%)</td><td>0.10 <b>(+44.28%)</b></td><td>0.13 <b>(+74.62%)</b></td><td>0.02 <b>(+33.58%)</b></td><td>0.06 <b>(+37.94%)</b></td><td>1892.70 <b>(-25.14%)</b></td><td>612.60 <b>(-26.54%)</b></td><td>249.80 <b>(-42.73%)</b></td><td>200.70 (-16.58%)</td><td>725.05 <b>(-23.94%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.04 (n/a)</td><td>2528.20 (n/a)</td><td>833.90 (n/a)</td><td>436.20 (n/a)</td><td>240.60 (n/a)</td><td>953.21 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.17 (-8.55%)</td><td>0.11 (-9.28%)</td><td>0.09 (-3.71%)</td><td>0.05 (-12.19%)</td><td>0.05 (-9.25%)</td><td>780.30 (+13.88%)</td><td>471.54 (+10.93%)</td><td>437.40 (+3.85%)</td><td>234.80 (+9.31%)</td><td>228.13 (+15.11%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>685.20 (n/a)</td><td>425.08 (n/a)</td><td>421.20 (n/a)</td><td>214.80 (n/a)</td><td>198.19 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.19 <b>(+48.82%)</b></td><td>0.10 (+1.25%)</td><td>0.07 (-16.76%)</td><td>0.06 (-17.75%)</td><td>0.05 <b>(+128.10%)</b></td><td>521.00 <b>(+21.59%)</b></td><td>403.88 (+11.50%)</td><td>486.60 <b>(+20.12%)</b></td><td>175.10 <b>(-32.78%)</b></td><td>144.12 <b>(+79.59%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>428.50 (n/a)</td><td>362.24 (n/a)</td><td>405.10 (n/a)</td><td>260.50 (n/a)</td><td>80.25 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (-12.36%)</td><td>0.10 (+5.54%)</td><td>0.08 (+3.66%)</td><td>0.07 (-3.65%)</td><td>0.04 (-16.47%)</td><td>610.10 (+3.79%)</td><td>455.04 (-6.68%)</td><td>522.80 (-3.52%)</td><td>276.20 (+14.13%)</td><td>143.93 (+2.82%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>587.80 (n/a)</td><td>487.60 (n/a)</td><td>541.90 (n/a)</td><td>242.00 (n/a)</td><td>139.98 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (-15.36%)</td><td>0.09 (-16.06%)</td><td>0.10 (-15.63%)</td><td>0.05 <b>(-20.25%)</b></td><td>0.03 (-0.04%)</td><td>599.30 <b>(+25.38%)</b></td><td>384.10 <b>(+22.50%)</b></td><td>338.40 (+18.53%)</td><td>254.90 (+18.12%)</td><td>140.75 <b>(+41.97%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>478.00 (n/a)</td><td>313.54 (n/a)</td><td>285.50 (n/a)</td><td>215.80 (n/a)</td><td>99.14 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 <b>(-45.18%)</b></td><td>0.08 <b>(-25.01%)</b></td><td>0.08 <b>(-21.30%)</b></td><td>0.06 (-12.35%)</td><td>0.01 <b>(-72.73%)</b></td><td>567.80 (+14.08%)</td><td>472.66 <b>(+26.08%)</b></td><td>457.40 <b>(+27.06%)</b></td><td>419.10 <b>(+82.38%)</b></td><td>59.00 <b>(-40.96%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>497.70 (n/a)</td><td>374.90 (n/a)</td><td>360.00 (n/a)</td><td>229.80 (n/a)</td><td>99.94 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 <b>(+24.58%)</b></td><td>0.11 <b>(+45.96%)</b></td><td>0.13 <b>(+81.44%)</b></td><td>0.06 <b>(+98.70%)</b></td><td>0.04 (+11.55%)</td><td>512.60 <b>(-49.67%)</b></td><td>328.02 <b>(-37.26%)</b></td><td>255.60 <b>(-44.89%)</b></td><td>221.80 (-19.72%)</td><td>124.32 <b>(-57.21%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>1018.50 (n/a)</td><td>522.86 (n/a)</td><td>463.80 (n/a)</td><td>276.30 (n/a)</td><td>290.52 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.18 <b>(+80.56%)</b></td><td>0.11 <b>(+30.72%)</b></td><td>0.09 (+6.17%)</td><td>0.06 (-6.80%)</td><td>0.05 <b>(+301.54%)</b></td><td>593.00 (+7.29%)</td><td>402.84 (-10.40%)</td><td>400.40 (-5.81%)</td><td>201.50 <b>(-44.63%)</b></td><td>176.25 <b>(+144.28%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>552.70 (n/a)</td><td>449.60 (n/a)</td><td>425.10 (n/a)</td><td>363.90 (n/a)</td><td>72.15 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (-13.47%)</td><td>0.08 (-10.23%)</td><td>0.08 (-15.05%)</td><td>0.03 <b>(-55.91%)</b></td><td>0.04 (+6.38%)</td><td>1302.80 <b>(+126.81%)</b></td><td>545.32 <b>(+35.30%)</b></td><td>414.00 (+17.71%)</td><td>255.90 (+15.53%)</td><td>432.09 <b>(+174.15%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>574.40 (n/a)</td><td>403.04 (n/a)</td><td>351.70 (n/a)</td><td>221.50 (n/a)</td><td>157.61 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (-7.61%)</td><td>0.07 (+16.08%)</td><td>0.07 <b>(+41.94%)</b></td><td>0.05 (+15.39%)</td><td>0.01 <b>(-38.09%)</b></td><td>452.80 (-13.34%)</td><td>316.98 (-19.11%)</td><td>300.90 <b>(-29.55%)</b></td><td>261.50 (+8.24%)</td><td>78.16 <b>(-40.18%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>522.50 (n/a)</td><td>391.88 (n/a)</td><td>427.10 (n/a)</td><td>241.60 (n/a)</td><td>130.66 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (+11.05%)</td><td>0.07 <b>(+30.99%)</b></td><td>0.07 <b>(+50.61%)</b></td><td>0.04 (+4.15%)</td><td>0.02 (+11.78%)</td><td>501.50 (-4.00%)</td><td>303.34 <b>(-22.81%)</b></td><td>273.20 <b>(-33.61%)</b></td><td>208.10 (-9.95%)</td><td>116.46 (+2.79%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>522.40 (n/a)</td><td>392.98 (n/a)</td><td>411.50 (n/a)</td><td>231.10 (n/a)</td><td>113.30 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (+7.85%)</td><td>0.06 (+8.69%)</td><td>0.05 (-6.32%)</td><td>0.04 <b>(+260.63%)</b></td><td>0.02 <b>(-22.85%)</b></td><td>553.90 <b>(-72.27%)</b></td><td>403.94 <b>(-39.98%)</b></td><td>409.40 (+6.75%)</td><td>261.70 (-7.26%)</td><td>135.11 <b>(-81.81%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1997.40 (n/a)</td><td>673.00 (n/a)</td><td>383.50 (n/a)</td><td>282.20 (n/a)</td><td>742.66 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (-13.71%)</td><td>0.05 (-0.15%)</td><td>0.05 <b>(-25.20%)</b></td><td>0.04 <b>(+299.87%)</b></td><td>0.01 <b>(-62.59%)</b></td><td>480.00 <b>(-74.99%)</b></td><td>387.04 <b>(-41.62%)</b></td><td>377.70 <b>(+33.70%)</b></td><td>297.20 (+15.87%)</td><td>81.00 <b>(-88.69%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>0.03 (n/a)</td><td>1919.30 (n/a)</td><td>663.02 (n/a)</td><td>282.50 (n/a)</td><td>256.50 (n/a)</td><td>716.04 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (-4.08%)</td><td>0.05 (-13.63%)</td><td>0.04 (-3.90%)</td><td>0.03 (-9.61%)</td><td>0.02 (-12.47%)</td><td>588.10 (+10.63%)</td><td>448.86 (+14.53%)</td><td>462.20 (+4.05%)</td><td>258.30 (+4.24%)</td><td>129.83 (+2.75%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>531.60 (n/a)</td><td>391.90 (n/a)</td><td>444.20 (n/a)</td><td>247.80 (n/a)</td><td>126.36 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (+14.20%)</td><td>0.07 (+7.28%)</td><td>0.08 <b>(+22.57%)</b></td><td>0.03 (-8.21%)</td><td>0.03 <b>(+61.49%)</b></td><td>613.60 (+8.95%)</td><td>361.60 (+1.52%)</td><td>248.90 (-18.42%)</td><td>230.80 (-12.44%)</td><td>171.35 <b>(+42.52%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>563.20 (n/a)</td><td>356.18 (n/a)</td><td>305.10 (n/a)</td><td>263.60 (n/a)</td><td>120.23 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (+1.60%)</td><td>0.07 <b>(-21.32%)</b></td><td>0.06 <b>(-34.02%)</b></td><td>0.05 (-16.73%)</td><td>0.02 <b>(+49.56%)</b></td><td>478.40 <b>(+20.08%)</b></td><td>401.34 <b>(+31.72%)</b></td><td>441.60 <b>(+51.60%)</b></td><td>242.20 (-1.58%)</td><td>93.66 <b>(+64.67%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>398.40 (n/a)</td><td>304.70 (n/a)</td><td>291.30 (n/a)</td><td>246.10 (n/a)</td><td>56.87 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 (+3.78%)</td><td>0.08 (+15.40%)</td><td>0.08 (+16.26%)</td><td>0.04 <b>(+33.61%)</b></td><td>0.03 (-6.85%)</td><td>571.50 <b>(-25.15%)</b></td><td>371.46 (-19.72%)</td><td>297.90 (-14.00%)</td><td>234.30 (-3.66%)</td><td>155.74 <b>(-35.16%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>763.50 (n/a)</td><td>462.68 (n/a)</td><td>346.40 (n/a)</td><td>243.20 (n/a)</td><td>240.19 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.11 <b>(+23.21%)</b></td><td>0.08 (+18.61%)</td><td>0.08 <b>(+45.96%)</b></td><td>0.05 (-3.78%)</td><td>0.02 <b>(+40.92%)</b></td><td>504.40 (+3.94%)</td><td>342.84 (-12.89%)</td><td>297.00 <b>(-31.49%)</b></td><td>220.90 (-18.85%)</td><td>113.05 <b>(+20.87%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>485.30 (n/a)</td><td>393.56 (n/a)</td><td>433.50 (n/a)</td><td>272.20 (n/a)</td><td>93.53 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (+8.12%)</td><td>0.07 (+14.59%)</td><td>0.06 (+7.26%)</td><td>0.05 (+17.64%)</td><td>0.02 (+19.06%)</td><td>518.30 (-14.99%)</td><td>384.40 (-12.18%)</td><td>396.70 (-6.75%)</td><td>264.90 (-7.51%)</td><td>113.06 (-9.59%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>609.70 (n/a)</td><td>437.70 (n/a)</td><td>425.40 (n/a)</td><td>286.40 (n/a)</td><td>125.05 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.10 <b>(-35.19%)</b></td><td>0.06 <b>(-30.83%)</b></td><td>0.05 <b>(-42.96%)</b></td><td>0.04 <b>(+91.11%)</b></td><td>0.02 <b>(-51.29%)</b></td><td>553.30 <b>(-47.68%)</b></td><td>466.32 (+5.98%)</td><td>513.90 <b>(+75.33%)</b></td><td>241.30 <b>(+54.28%)</b></td><td>129.54 <b>(-64.16%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>1057.50 (n/a)</td><td>440.00 (n/a)</td><td>293.10 (n/a)</td><td>156.40 (n/a)</td><td>361.43 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 (-10.73%)</td><td>0.07 (+0.70%)</td><td>0.08 <b>(+39.03%)</b></td><td>0.04 (-2.63%)</td><td>0.02 (-5.12%)</td><td>580.70 (+2.69%)</td><td>390.24 (-0.06%)</td><td>299.20 <b>(-28.08%)</b></td><td>278.20 (+12.04%)</td><td>145.31 (+10.98%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>565.50 (n/a)</td><td>390.46 (n/a)</td><td>416.00 (n/a)</td><td>248.30 (n/a)</td><td>130.93 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 <b>(+92.04%)</b></td><td>0.05 <b>(+56.16%)</b></td><td>0.05 <b>(+39.58%)</b></td><td>0.03 <b>(+200.70%)</b></td><td>0.02 <b>(+65.18%)</b></td><td>687.80 <b>(-66.75%)</b></td><td>448.26 <b>(-45.36%)</b></td><td>372.50 <b>(-28.35%)</b></td><td>247.20 <b>(-47.93%)</b></td><td>198.64 <b>(-71.54%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>2068.30 (n/a)</td><td>820.36 (n/a)</td><td>519.90 (n/a)</td><td>474.70 (n/a)</td><td>698.02 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (-5.82%)</td><td>0.05 <b>(-20.32%)</b></td><td>0.06 (-8.50%)</td><td>0.03 <b>(-42.83%)</b></td><td>0.02 <b>(+126.05%)</b></td><td>615.00 <b>(+74.91%)</b></td><td>399.88 <b>(+38.21%)</b></td><td>303.70 (+9.28%)</td><td>276.30 (+6.19%)</td><td>155.35 <b>(+311.93%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>351.60 (n/a)</td><td>289.32 (n/a)</td><td>277.90 (n/a)</td><td>260.20 (n/a)</td><td>37.71 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (+5.39%)</td><td>0.05 (-15.45%)</td><td>0.04 <b>(-42.64%)</b></td><td>0.03 (-16.64%)</td><td>0.02 <b>(+26.20%)</b></td><td>586.90 (+19.95%)</td><td>428.56 <b>(+25.80%)</b></td><td>466.50 <b>(+74.33%)</b></td><td>235.20 (-5.12%)</td><td>164.50 <b>(+47.14%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>489.30 (n/a)</td><td>340.68 (n/a)</td><td>267.60 (n/a)</td><td>247.90 (n/a)</td><td>111.80 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (-10.96%)</td><td>0.04 (-9.39%)</td><td>0.03 (-12.48%)</td><td>0.03 (+11.62%)</td><td>0.02 <b>(-22.92%)</b></td><td>677.40 (-10.41%)</td><td>499.02 (+3.32%)</td><td>584.80 (+14.26%)</td><td>279.00 (+12.32%)</td><td>184.11 (-17.55%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>756.10 (n/a)</td><td>483.00 (n/a)</td><td>511.80 (n/a)</td><td>248.40 (n/a)</td><td>223.29 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.07 (-13.72%)</td><td>0.04 (-5.90%)</td><td>0.04 (-1.78%)</td><td>0.03 (+11.13%)</td><td>0.02 <b>(-24.76%)</b></td><td>584.60 (-10.02%)</td><td>479.66 (+1.64%)</td><td>515.40 (+1.82%)</td><td>270.70 (+15.88%)</td><td>125.13 (-19.35%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>649.70 (n/a)</td><td>471.90 (n/a)</td><td>506.20 (n/a)</td><td>233.60 (n/a)</td><td>155.15 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.08 (+0.70%)</td><td>0.05 (-2.19%)</td><td>0.05 <b>(-21.57%)</b></td><td>0.04 <b>(+95.32%)</b></td><td>0.02 <b>(-32.22%)</b></td><td>524.70 <b>(-48.80%)</b></td><td>389.56 (-16.77%)</td><td>371.50 <b>(+27.49%)</b></td><td>245.40 (-0.69%)</td><td>120.79 <b>(-63.43%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>1024.90 (n/a)</td><td>468.06 (n/a)</td><td>291.40 (n/a)</td><td>247.10 (n/a)</td><td>330.30 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.34 (-1.90%)</td><td>0.24 (+17.17%)</td><td>0.21 (-0.00%)</td><td>0.18 <b>(+237.67%)</b></td><td>0.08 <b>(-27.86%)</b></td><td>557.00 <b>(-70.38%)</b></td><td>439.00 <b>(-38.63%)</b></td><td>473.80 (+0.00%)</td><td>293.40 (+1.95%)</td><td>126.28 <b>(-80.80%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.34 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>0.10 (n/a)</td><td>1880.70 (n/a)</td><td>715.36 (n/a)</td><td>473.80 (n/a)</td><td>287.80 (n/a)</td><td>657.54 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.41 (+15.67%)</td><td>0.30 (-5.14%)</td><td>0.35 (+2.07%)</td><td>0.15 (-15.59%)</td><td>0.11 <b>(+53.01%)</b></td><td>638.30 (+18.47%)</td><td>385.02 (+14.17%)</td><td>280.10 (-2.03%)</td><td>237.50 (-13.54%)</td><td>174.14 <b>(+53.58%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.36 (n/a)</td><td>0.31 (n/a)</td><td>0.34 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>538.80 (n/a)</td><td>337.22 (n/a)</td><td>285.90 (n/a)</td><td>274.70 (n/a)</td><td>113.39 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.26 <b>(-21.17%)</b></td><td>0.21 (-0.04%)</td><td>0.21 (+13.60%)</td><td>0.16 (+1.62%)</td><td>0.04 <b>(-45.42%)</b></td><td>603.40 (-1.60%)</td><td>482.64 (-4.04%)</td><td>476.00 (-11.98%)</td><td>376.80 <b>(+26.83%)</b></td><td>88.60 <b>(-29.74%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>613.20 (n/a)</td><td>502.96 (n/a)</td><td>540.80 (n/a)</td><td>297.10 (n/a)</td><td>126.10 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.46 <b>(+60.04%)</b></td><td>0.24 (+16.65%)</td><td>0.18 (+9.07%)</td><td>0.13 (-1.92%)</td><td>0.13 <b>(+77.25%)</b></td><td>552.00 (+1.96%)</td><td>379.78 (-6.03%)</td><td>412.90 (-8.31%)</td><td>160.10 <b>(-37.53%)</b></td><td>158.53 (+15.90%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>541.40 (n/a)</td><td>404.14 (n/a)</td><td>450.30 (n/a)</td><td>256.30 (n/a)</td><td>136.78 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.26 (-14.68%)</td><td>0.19 (-2.00%)</td><td>0.17 (+9.21%)</td><td>0.14 (+4.82%)</td><td>0.05 <b>(-33.18%)</b></td><td>521.70 (-4.59%)</td><td>399.14 (-2.81%)</td><td>424.80 (-8.43%)</td><td>288.10 (+17.21%)</td><td>96.22 <b>(-27.00%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>546.80 (n/a)</td><td>410.66 (n/a)</td><td>463.90 (n/a)</td><td>245.80 (n/a)</td><td>131.81 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.20 (-18.35%)</td><td>0.14 (-6.02%)</td><td>0.14 <b>(-32.58%)</b></td><td>0.07 <b>(+79.69%)</b></td><td>0.05 <b>(-49.36%)</b></td><td>1089.00 <b>(-44.35%)</b></td><td>608.70 <b>(-36.85%)</b></td><td>536.50 <b>(+48.33%)</b></td><td>360.10 <b>(+22.44%)</b></td><td>285.51 <b>(-66.83%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.25 (n/a)</td><td>0.15 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>0.10 (n/a)</td><td>1956.80 (n/a)</td><td>963.82 (n/a)</td><td>361.70 (n/a)</td><td>294.10 (n/a)</td><td>860.79 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (+6.82%)</td><td>0.12 <b>(+28.93%)</b></td><td>0.12 <b>(+46.59%)</b></td><td>0.08 <b>(+20.87%)</b></td><td>0.03 <b>(-20.16%)</b></td><td>487.90 (-17.26%)</td><td>319.72 <b>(-26.57%)</b></td><td>296.90 <b>(-31.78%)</b></td><td>237.90 (-6.38%)</td><td>97.16 <b>(-37.23%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>589.70 (n/a)</td><td>435.38 (n/a)</td><td>435.20 (n/a)</td><td>254.10 (n/a)</td><td>154.78 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 <b>(-20.62%)</b></td><td>0.10 (-12.12%)</td><td>0.10 (+0.30%)</td><td>0.06 (-10.91%)</td><td>0.04 (-19.83%)</td><td>614.80 (+12.25%)</td><td>407.22 (+12.60%)</td><td>385.80 (-0.31%)</td><td>262.00 <b>(+25.96%)</b></td><td>151.39 (+11.93%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>547.70 (n/a)</td><td>361.66 (n/a)</td><td>387.00 (n/a)</td><td>208.00 (n/a)</td><td>135.25 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (-17.49%)</td><td>0.09 (-5.05%)</td><td>0.07 (-3.98%)</td><td>0.03 <b>(-54.09%)</b></td><td>0.04 (+13.24%)</td><td>1098.80 <b>(+117.80%)</b></td><td>537.64 <b>(+24.18%)</b></td><td>493.30 (+4.14%)</td><td>273.30 <b>(+21.20%)</b></td><td>337.49 <b>(+187.96%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>504.50 (n/a)</td><td>432.94 (n/a)</td><td>473.70 (n/a)</td><td>225.50 (n/a)</td><td>117.20 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.09 <b>(-40.69%)</b></td><td>0.08 <b>(-30.33%)</b></td><td>0.08 <b>(-34.52%)</b></td><td>0.06 <b>(-22.06%)</b></td><td>0.01 <b>(-64.92%)</b></td><td>596.90 <b>(+28.31%)</b></td><td>479.46 <b>(+36.62%)</b></td><td>464.60 <b>(+52.73%)</b></td><td>413.60 <b>(+68.61%)</b></td><td>73.59 <b>(-28.12%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>465.20 (n/a)</td><td>350.94 (n/a)</td><td>304.20 (n/a)</td><td>245.30 (n/a)</td><td>102.37 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (+2.20%)</td><td>0.11 (-11.35%)</td><td>0.12 (-15.45%)</td><td>0.06 (-7.34%)</td><td>0.04 (+14.21%)</td><td>596.70 (+7.94%)</td><td>387.96 (+17.60%)</td><td>298.30 (+18.28%)</td><td>242.60 (-2.18%)</td><td>166.80 <b>(+26.65%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>552.80 (n/a)</td><td>329.90 (n/a)</td><td>252.20 (n/a)</td><td>248.00 (n/a)</td><td>131.70 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.17 (+12.23%)</td><td>0.09 <b>(-28.97%)</b></td><td>0.08 <b>(-46.20%)</b></td><td>0.06 (-14.31%)</td><td>0.05 <b>(+33.63%)</b></td><td>610.80 (+16.70%)</td><td>461.70 <b>(+48.02%)</b></td><td>484.60 <b>(+85.88%)</b></td><td>215.90 (-10.90%)</td><td>149.84 <b>(+25.31%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>523.40 (n/a)</td><td>311.92 (n/a)</td><td>260.70 (n/a)</td><td>242.30 (n/a)</td><td>119.57 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (-9.01%)</td><td>0.13 (-6.39%)</td><td>0.14 (-5.26%)</td><td>0.08 (-0.03%)</td><td>0.03 (-19.51%)</td><td>522.10 (+0.04%)</td><td>332.06 (+4.55%)</td><td>288.60 (+5.56%)</td><td>256.80 (+9.88%)</td><td>108.41 (-8.89%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>521.90 (n/a)</td><td>317.60 (n/a)</td><td>273.40 (n/a)</td><td>233.70 (n/a)</td><td>118.99 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.17 (+8.79%)</td><td>0.10 (-10.70%)</td><td>0.07 (-18.19%)</td><td>0.02 <b>(-73.43%)</b></td><td>0.06 <b>(+115.95%)</b></td><td>1883.60 <b>(+276.34%)</b></td><td>729.16 <b>(+80.49%)</b></td><td>555.90 <b>(+22.26%)</b></td><td>247.00 (-8.08%)</td><td>673.81 <b>(+603.00%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>500.50 (n/a)</td><td>404.00 (n/a)</td><td>454.70 (n/a)</td><td>268.70 (n/a)</td><td>95.85 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (-3.01%)</td><td>0.11 (-11.94%)</td><td>0.10 <b>(-35.34%)</b></td><td>0.08 (+4.69%)</td><td>0.04 <b>(-20.56%)</b></td><td>517.20 (-4.47%)</td><td>395.78 (+8.30%)</td><td>403.20 <b>(+54.66%)</b></td><td>250.40 (+3.09%)</td><td>119.74 <b>(-21.29%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>541.40 (n/a)</td><td>365.46 (n/a)</td><td>260.70 (n/a)</td><td>242.90 (n/a)</td><td>152.12 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.18 (+1.71%)</td><td>0.11 (-13.25%)</td><td>0.08 <b>(-40.59%)</b></td><td>0.04 <b>(-38.21%)</b></td><td>0.06 <b>(+20.94%)</b></td><td>964.60 <b>(+61.85%)</b></td><td>490.84 <b>(+30.47%)</b></td><td>493.30 <b>(+68.30%)</b></td><td>222.00 (-1.68%)</td><td>292.17 <b>(+84.04%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>596.00 (n/a)</td><td>376.20 (n/a)</td><td>293.10 (n/a)</td><td>225.80 (n/a)</td><td>158.75 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (+3.85%)</td><td>0.11 <b>(+31.93%)</b></td><td>0.13 <b>(+67.95%)</b></td><td>0.07 <b>(+216.87%)</b></td><td>0.03 (-18.98%)</td><td>606.80 <b>(-68.44%)</b></td><td>411.32 <b>(-44.41%)</b></td><td>326.30 <b>(-40.47%)</b></td><td>292.80 (-3.68%)</td><td>148.21 <b>(-77.89%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>0.04 (n/a)</td><td>1922.70 (n/a)</td><td>739.86 (n/a)</td><td>548.10 (n/a)</td><td>304.00 (n/a)</td><td>670.22 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (-16.27%)</td><td>0.10 (-1.55%)</td><td>0.08 (-4.59%)</td><td>0.07 (+14.63%)</td><td>0.03 <b>(-21.58%)</b></td><td>596.10 (-12.76%)</td><td>458.60 (-2.67%)</td><td>537.00 (+4.82%)</td><td>304.20 (+19.43%)</td><td>138.27 (-19.81%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>683.30 (n/a)</td><td>471.20 (n/a)</td><td>512.30 (n/a)</td><td>254.70 (n/a)</td><td>172.43 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.12 (-7.99%)</td><td>0.08 <b>(-22.62%)</b></td><td>0.07 <b>(-38.79%)</b></td><td>0.07 (-6.92%)</td><td>0.02 (+2.75%)</td><td>535.10 (+7.43%)</td><td>435.18 <b>(+30.41%)</b></td><td>478.40 <b>(+63.33%)</b></td><td>290.10 (+8.65%)</td><td>108.98 (+16.34%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>498.10 (n/a)</td><td>333.70 (n/a)</td><td>292.90 (n/a)</td><td>267.00 (n/a)</td><td>93.68 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (+0.96%)</td><td>0.11 (+4.92%)</td><td>0.12 (+8.45%)</td><td>0.06 (+13.88%)</td><td>0.03 (-12.89%)</td><td>537.50 (-12.19%)</td><td>357.82 (-8.35%)</td><td>292.90 (-7.78%)</td><td>245.50 (-0.93%)</td><td>122.07 <b>(-23.36%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>612.10 (n/a)</td><td>390.42 (n/a)</td><td>317.60 (n/a)</td><td>247.80 (n/a)</td><td>159.28 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (-7.88%)</td><td>0.09 (-4.43%)</td><td>0.08 (-2.45%)</td><td>0.05 (-3.84%)</td><td>0.03 (-8.31%)</td><td>695.00 (+4.00%)</td><td>431.06 (+4.04%)</td><td>415.00 (+2.49%)</td><td>267.30 (+8.57%)</td><td>169.74 (+2.91%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>668.30 (n/a)</td><td>414.34 (n/a)</td><td>404.90 (n/a)</td><td>246.20 (n/a)</td><td>164.93 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.16 (+15.92%)</td><td>0.09 <b>(-29.56%)</b></td><td>0.07 <b>(-45.43%)</b></td><td>0.05 <b>(-51.31%)</b></td><td>0.04 <b>(+269.62%)</b></td><td>655.90 <b>(+105.35%)</b></td><td>454.54 <b>(+66.96%)</b></td><td>469.70 <b>(+83.26%)</b></td><td>218.70 (-13.73%)</td><td>188.06 <b>(+570.69%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>319.40 (n/a)</td><td>272.24 (n/a)</td><td>256.30 (n/a)</td><td>253.50 (n/a)</td><td>28.04 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (+3.82%)</td><td>0.10 <b>(+46.46%)</b></td><td>0.12 <b>(+45.50%)</b></td><td>0.06 <b>(+312.13%)</b></td><td>0.04 <b>(-31.83%)</b></td><td>593.30 <b>(-75.74%)</b></td><td>388.90 <b>(-65.44%)</b></td><td>296.00 <b>(-31.26%)</b></td><td>254.90 (-3.70%)</td><td>156.39 <b>(-85.44%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>0.05 (n/a)</td><td>2445.20 (n/a)</td><td>1125.28 (n/a)</td><td>430.60 (n/a)</td><td>264.70 (n/a)</td><td>1073.84 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.14 (+0.79%)</td><td>0.11 (-3.38%)</td><td>0.09 <b>(-25.44%)</b></td><td>0.07 (+4.64%)</td><td>0.03 (-4.99%)</td><td>486.70 (-4.44%)</td><td>359.08 (+1.69%)</td><td>402.00 <b>(+34.13%)</b></td><td>240.30 (-0.78%)</td><td>109.11 (-14.22%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>509.30 (n/a)</td><td>353.12 (n/a)</td><td>299.70 (n/a)</td><td>242.20 (n/a)</td><td>127.20 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.33 <b>(-24.17%)</b></td><td>0.22 (-12.72%)</td><td>0.24 (+12.69%)</td><td>0.06 <b>(-64.01%)</b></td><td>0.10 (-0.48%)</td><td>2087.10 <b>(+177.80%)</b></td><td>830.12 <b>(+47.31%)</b></td><td>542.70 (-11.27%)</td><td>395.80 <b>(+31.89%)</b></td><td>710.39 <b>(+323.57%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.44 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>751.30 (n/a)</td><td>563.50 (n/a)</td><td>611.60 (n/a)</td><td>300.10 (n/a)</td><td>167.71 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.43 (-16.26%)</td><td>0.28 (-4.92%)</td><td>0.26 (+7.25%)</td><td>0.16 (-19.67%)</td><td>0.10 (-16.79%)</td><td>801.80 <b>(+24.48%)</b></td><td>531.46 (+6.15%)</td><td>500.90 (-6.76%)</td><td>304.90 (+19.43%)</td><td>195.92 <b>(+34.65%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.51 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>644.10 (n/a)</td><td>500.66 (n/a)</td><td>537.20 (n/a)</td><td>255.30 (n/a)</td><td>145.51 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.38 <b>(+44.75%)</b></td><td>0.29 <b>(+24.51%)</b></td><td>0.29 <b>(+26.97%)</b></td><td>0.19 (+1.10%)</td><td>0.07 <b>(+103.89%)</b></td><td>677.40 (-1.10%)</td><td>480.48 (-17.17%)</td><td>452.10 <b>(-21.24%)</b></td><td>341.70 <b>(-30.93%)</b></td><td>122.27 <b>(+44.49%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>684.90 (n/a)</td><td>580.10 (n/a)</td><td>574.00 (n/a)</td><td>494.70 (n/a)</td><td>84.62 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(+25.67%)</b></td><td>0.01 (-2.53%)</td><td>0.01 (-10.54%)</td><td>0.01 (-3.81%)</td><td>0.01 <b>(+83.21%)</b></td><td>422.40 (+3.96%)</td><td>319.80 (+8.53%)</td><td>313.10 (+11.78%)</td><td>185.00 <b>(-20.46%)</b></td><td>99.17 <b>(+49.54%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>406.30 (n/a)</td><td>294.66 (n/a)</td><td>280.10 (n/a)</td><td>232.60 (n/a)</td><td>66.32 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(+20.94%)</b></td><td>0.01 (+18.78%)</td><td>0.02 <b>(+23.99%)</b></td><td>0.01 (+1.59%)</td><td>0.00 <b>(+39.03%)</b></td><td>411.60 (-1.58%)</td><td>297.68 (-14.75%)</td><td>272.30 (-19.34%)</td><td>243.40 (-17.30%)</td><td>66.08 (+18.56%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>418.20 (n/a)</td><td>349.18 (n/a)</td><td>337.60 (n/a)</td><td>294.30 (n/a)</td><td>55.73 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (+11.52%)</td><td>0.01 <b>(+31.86%)</b></td><td>0.01 <b>(+81.15%)</b></td><td>0.01 <b>(+27.88%)</b></td><td>0.00 (-4.38%)</td><td>501.40 <b>(-21.80%)</b></td><td>339.98 <b>(-26.56%)</b></td><td>290.40 <b>(-44.79%)</b></td><td>241.70 (-10.32%)</td><td>104.89 <b>(-30.55%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>641.20 (n/a)</td><td>462.96 (n/a)</td><td>526.00 (n/a)</td><td>269.50 (n/a)</td><td>151.05 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>8.25 (-0.78%)</td><td>6.45 (-0.22%)</td><td>6.63 (-14.07%)</td><td>4.53 (+8.82%)</td><td>1.74 (-13.54%)</td><td>462.90 (-8.12%)</td><td>346.32 (-2.63%)</td><td>316.30 (+16.37%)</td><td>254.40 (+0.79%)</td><td>98.04 <b>(-21.40%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>8.31 (n/a)</td><td>6.46 (n/a)</td><td>7.72 (n/a)</td><td>4.17 (n/a)</td><td>2.02 (n/a)</td><td>503.80 (n/a)</td><td>355.66 (n/a)</td><td>271.80 (n/a)</td><td>252.40 (n/a)</td><td>124.72 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.54 (+6.05%)</td><td>0.38 (-15.65%)</td><td>0.39 (-14.75%)</td><td>0.22 <b>(-37.46%)</b></td><td>0.12 <b>(+109.74%)</b></td><td>595.20 <b>(+59.91%)</b></td><td>383.04 <b>(+27.71%)</b></td><td>338.10 (+17.31%)</td><td>246.40 (-5.70%)</td><td>134.73 <b>(+215.64%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.51 (n/a)</td><td>0.45 (n/a)</td><td>0.46 (n/a)</td><td>0.35 (n/a)</td><td>0.06 (n/a)</td><td>372.20 (n/a)</td><td>299.92 (n/a)</td><td>288.20 (n/a)</td><td>261.30 (n/a)</td><td>42.68 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.57 <b>(+26.69%)</b></td><td>0.44 <b>(+27.58%)</b></td><td>0.43 <b>(+31.74%)</b></td><td>0.25 <b>(+20.85%)</b></td><td>0.12 <b>(+30.81%)</b></td><td>518.90 (-17.25%)</td><td>327.04 <b>(-20.91%)</b></td><td>306.10 <b>(-24.10%)</b></td><td>232.80 <b>(-21.06%)</b></td><td>113.19 (-12.98%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.45 (n/a)</td><td>0.34 (n/a)</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>627.10 (n/a)</td><td>413.52 (n/a)</td><td>403.30 (n/a)</td><td>294.90 (n/a)</td><td>130.08 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.39 <b>(-20.59%)</b></td><td>0.32 <b>(-23.18%)</b></td><td>0.31 <b>(-27.30%)</b></td><td>0.26 (-12.87%)</td><td>0.05 <b>(-37.49%)</b></td><td>512.50 (+14.76%)</td><td>421.18 <b>(+28.31%)</b></td><td>430.50 <b>(+37.54%)</b></td><td>339.10 <b>(+25.92%)</b></td><td>64.07 (-10.44%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>446.60 (n/a)</td><td>328.26 (n/a)</td><td>313.00 (n/a)</td><td>269.30 (n/a)</td><td>71.55 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.56 (+13.49%)</td><td>0.48 <b>(+25.67%)</b></td><td>0.46 (+16.13%)</td><td>0.39 <b>(+50.46%)</b></td><td>0.07 <b>(-29.92%)</b></td><td>342.00 <b>(-33.54%)</b></td><td>279.80 <b>(-23.89%)</b></td><td>285.80 (-13.89%)</td><td>234.90 (-11.89%)</td><td>43.03 <b>(-59.43%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.50 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.26 (n/a)</td><td>0.10 (n/a)</td><td>514.60 (n/a)</td><td>367.64 (n/a)</td><td>331.90 (n/a)</td><td>266.60 (n/a)</td><td>106.08 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.69 <b>(+29.20%)</b></td><td>0.39 (+11.55%)</td><td>0.33 (+19.44%)</td><td>0.07 <b>(-70.81%)</b></td><td>0.24 <b>(+79.84%)</b></td><td>1854.40 <b>(+242.58%)</b></td><td>621.88 <b>(+48.35%)</b></td><td>395.20 (-16.29%)</td><td>192.00 <b>(-22.58%)</b></td><td>695.99 <b>(+406.31%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.53 (n/a)</td><td>0.35 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>541.30 (n/a)</td><td>419.20 (n/a)</td><td>472.10 (n/a)</td><td>248.00 (n/a)</td><td>137.46 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 <b>(+22.12%)</b></td><td>0.01 <b>(+24.94%)</b></td><td>0.01 (+13.43%)</td><td>0.01 <b>(+29.46%)</b></td><td>0.00 (-3.98%)</td><td>463.90 <b>(-22.75%)</b></td><td>302.64 <b>(-22.45%)</b></td><td>279.30 (-11.84%)</td><td>231.20 (-18.10%)</td><td>92.41 <b>(-33.71%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>600.50 (n/a)</td><td>390.24 (n/a)</td><td>316.80 (n/a)</td><td>282.30 (n/a)</td><td>139.40 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.02 (-9.08%)</td><td>0.01 (-16.63%)</td><td>0.01 <b>(-28.55%)</b></td><td>0.01 (-7.39%)</td><td>0.00 (-1.18%)</td><td>573.70 (+8.00%)</td><td>423.42 <b>(+21.48%)</b></td><td>457.00 <b>(+39.97%)</b></td><td>258.50 (+10.00%)</td><td>135.16 (+15.95%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>531.20 (n/a)</td><td>348.56 (n/a)</td><td>326.50 (n/a)</td><td>235.00 (n/a)</td><td>116.57 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.00 <b>(-66.67%)</b></td><td>0.00 <b>(-52.38%)</b></td><td>0.00 <b>(-60.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(-100.00%)</b></td><td>22238.43 (+15.85%)</td><td>19174.41 <b>(+62.95%)</b></td><td>18319.39 <b>(+108.75%)</b></td><td>16597.11 <b>(+156.29%)</b></td><td>2397.32 <b>(-60.92%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19196.29 (n/a)</td><td>11766.76 (n/a)</td><td>8775.94 (n/a)</td><td>6475.98 (n/a)</td><td>6134.76 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.00 (-8.33%)</td><td>0.00 (+6.67%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (-10.07%)</td><td>20735.50 (-8.30%)</td><td>14690.06 (-15.36%)</td><td>15850.02 (-10.77%)</td><td>7800.25 (+18.17%)</td><td>5497.28 (-15.84%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22612.54 (n/a)</td><td>17356.01 (n/a)</td><td>17762.91 (n/a)</td><td>6600.71 (n/a)</td><td>6531.73 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (-3.30%)</td><td>0.10 (-0.68%)</td><td>0.09 (+10.56%)</td><td>0.07 (+1.94%)</td><td>0.02 <b>(-23.03%)</b></td><td>28572.76 (-1.94%)</td><td>22480.18 (-2.14%)</td><td>22782.06 (-9.56%)</td><td>15579.71 (+3.42%)</td><td>4649.89 <b>(-25.22%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29138.95 (n/a)</td><td>22972.38 (n/a)</td><td>25189.19 (n/a)</td><td>15064.03 (n/a)</td><td>6218.14 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.66 (+10.35%)</td><td>1.51 <b>(+31.21%)</b></td><td>1.12 (-3.26%)</td><td>0.45 <b>(+48.80%)</b></td><td>0.92 (+3.14%)</td><td>2345.00 <b>(-32.79%)</b></td><td>1026.26 <b>(-41.58%)</b></td><td>936.00 (+3.37%)</td><td>394.70 (-9.37%)</td><td>784.80 <b>(-47.62%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>2.41 (n/a)</td><td>1.15 (n/a)</td><td>1.16 (n/a)</td><td>0.30 (n/a)</td><td>0.89 (n/a)</td><td>3489.30 (n/a)</td><td>1756.72 (n/a)</td><td>905.50 (n/a)</td><td>435.50 (n/a)</td><td>1498.18 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.12 (-4.71%)</td><td>2.07 (+3.71%)</td><td>1.58 <b>(-37.33%)</b></td><td>1.16 <b>(+281.83%)</b></td><td>0.89 <b>(-26.63%)</b></td><td>906.10 <b>(-73.81%)</b></td><td>586.88 <b>(-46.36%)</b></td><td>661.80 <b>(+59.59%)</b></td><td>336.50 (+4.93%)</td><td>240.50 <b>(-82.07%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.27 (n/a)</td><td>2.00 (n/a)</td><td>2.53 (n/a)</td><td>0.30 (n/a)</td><td>1.22 (n/a)</td><td>3459.90 (n/a)</td><td>1094.16 (n/a)</td><td>414.70 (n/a)</td><td>320.70 (n/a)</td><td>1341.54 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.48 <b>(+21.35%)</b></td><td>1.75 (-10.67%)</td><td>1.61 (-15.17%)</td><td>0.56 <b>(-57.54%)</b></td><td>1.07 <b>(+75.59%)</b></td><td>1888.20 <b>(+135.50%)</b></td><td>843.54 <b>(+46.09%)</b></td><td>649.30 (+17.88%)</td><td>301.40 (-17.58%)</td><td>609.39 <b>(+255.64%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>2.87 (n/a)</td><td>1.96 (n/a)</td><td>1.90 (n/a)</td><td>1.31 (n/a)</td><td>0.61 (n/a)</td><td>801.80 (n/a)</td><td>577.42 (n/a)</td><td>550.80 (n/a)</td><td>365.70 (n/a)</td><td>171.35 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.18 <b>(-35.54%)</b></td><td>1.81 (-18.02%)</td><td>1.80 (+6.28%)</td><td>1.48 (-5.57%)</td><td>0.29 <b>(-63.44%)</b></td><td>707.10 (+5.90%)</td><td>591.04 (+13.55%)</td><td>581.00 (-5.91%)</td><td>481.90 <b>(+55.15%)</b></td><td>95.41 <b>(-40.61%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.38 (n/a)</td><td>2.21 (n/a)</td><td>1.70 (n/a)</td><td>1.57 (n/a)</td><td>0.80 (n/a)</td><td>667.70 (n/a)</td><td>520.52 (n/a)</td><td>617.50 (n/a)</td><td>310.60 (n/a)</td><td>160.65 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.97 <b>(-76.80%)</b></td><td>0.73 <b>(-77.65%)</b></td><td>0.64 <b>(-80.83%)</b></td><td>0.58 <b>(-72.13%)</b></td><td>0.17 <b>(-77.78%)</b></td><td>3612.80 <b>(+258.80%)</b></td><td>2978.46 <b>(+341.17%)</b></td><td>3302.50 <b>(+421.56%)</b></td><td>2162.10 <b>(+331.13%)</b></td><td>641.40 <b>(+228.01%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.18 (n/a)</td><td>3.28 (n/a)</td><td>3.31 (n/a)</td><td>2.08 (n/a)</td><td>0.78 (n/a)</td><td>1006.90 (n/a)</td><td>675.12 (n/a)</td><td>633.20 (n/a)</td><td>501.50 (n/a)</td><td>195.54 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>6.05 (+3.75%)</td><td>3.47 (-1.16%)</td><td>3.31 <b>(-25.12%)</b></td><td>0.59 (-9.17%)</td><td>2.02 (-5.16%)</td><td>3559.40 (+10.10%)</td><td>1145.20 (+2.62%)</td><td>633.10 <b>(+33.57%)</b></td><td>346.60 (-3.62%)</td><td>1357.43 (+11.60%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.83 (n/a)</td><td>3.51 (n/a)</td><td>4.42 (n/a)</td><td>0.65 (n/a)</td><td>2.13 (n/a)</td><td>3233.00 (n/a)</td><td>1115.94 (n/a)</td><td>474.00 (n/a)</td><td>359.60 (n/a)</td><td>1216.30 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>6.46 <b>(+51.15%)</b></td><td>2.53 <b>(+35.44%)</b></td><td>2.08 <b>(+237.40%)</b></td><td>0.58 (+0.12%)</td><td>2.40 <b>(+35.26%)</b></td><td>3619.50 (-0.12%)</td><td>1780.70 <b>(-24.17%)</b></td><td>1010.10 <b>(-70.36%)</b></td><td>324.60 <b>(-33.84%)</b></td><td>1520.76 (-6.68%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>4.27 (n/a)</td><td>1.86 (n/a)</td><td>0.62 (n/a)</td><td>0.58 (n/a)</td><td>1.78 (n/a)</td><td>3623.90 (n/a)</td><td>2348.14 (n/a)</td><td>3408.00 (n/a)</td><td>490.60 (n/a)</td><td>1629.58 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.53 (-14.76%)</td><td>2.55 <b>(-38.32%)</b></td><td>2.94 <b>(-24.38%)</b></td><td>0.58 <b>(-78.77%)</b></td><td>2.07 <b>(+35.73%)</b></td><td>3622.70 <b>(+371.03%)</b></td><td>1789.76 <b>(+219.35%)</b></td><td>712.10 <b>(+32.21%)</b></td><td>379.00 (+17.30%)</td><td>1648.08 <b>(+795.18%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>6.49 (n/a)</td><td>4.13 (n/a)</td><td>3.89 (n/a)</td><td>2.73 (n/a)</td><td>1.52 (n/a)</td><td>769.10 (n/a)</td><td>560.44 (n/a)</td><td>538.60 (n/a)</td><td>323.10 (n/a)</td><td>184.10 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.68 (-3.59%)</td><td>2.89 (-2.88%)</td><td>2.86 (-12.49%)</td><td>0.59 (-0.68%)</td><td>1.83 (-19.17%)</td><td>3568.10 (+0.69%)</td><td>1251.86 (-16.09%)</td><td>732.50 (+14.27%)</td><td>369.00 (+3.71%)</td><td>1308.24 (-8.10%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.89 (n/a)</td><td>2.98 (n/a)</td><td>3.27 (n/a)</td><td>0.59 (n/a)</td><td>2.26 (n/a)</td><td>3543.80 (n/a)</td><td>1491.90 (n/a)</td><td>641.00 (n/a)</td><td>355.80 (n/a)</td><td>1423.52 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.57 (-5.57%)</td><td>2.99 (-15.48%)</td><td>2.00 <b>(-33.13%)</b></td><td>0.60 (+1.67%)</td><td>2.38 (+11.21%)</td><td>3513.30 (-1.64%)</td><td>1393.04 <b>(+21.08%)</b></td><td>1046.80 <b>(+49.56%)</b></td><td>376.30 (+5.91%)</td><td>1297.93 (-4.88%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.90 (n/a)</td><td>3.54 (n/a)</td><td>3.00 (n/a)</td><td>0.59 (n/a)</td><td>2.14 (n/a)</td><td>3571.90 (n/a)</td><td>1150.52 (n/a)</td><td>699.90 (n/a)</td><td>355.30 (n/a)</td><td>1364.51 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>5.48 (+1.90%)</td><td>4.42 <b>(+27.17%)</b></td><td>3.97 (+19.29%)</td><td>3.46 <b>(+102.42%)</b></td><td>0.92 <b>(-31.22%)</b></td><td>1213.00 <b>(-50.59%)</b></td><td>980.50 <b>(-29.34%)</b></td><td>1057.50 (-16.17%)</td><td>765.50 (-1.86%)</td><td>196.32 <b>(-69.24%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>5.38 (n/a)</td><td>3.48 (n/a)</td><td>3.32 (n/a)</td><td>1.71 (n/a)</td><td>1.34 (n/a)</td><td>2455.20 (n/a)</td><td>1387.62 (n/a)</td><td>1261.50 (n/a)</td><td>780.00 (n/a)</td><td>638.12 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>7.86 (-15.23%)</td><td>6.57 <b>(+50.01%)</b></td><td>7.29 <b>(+113.12%)</b></td><td>4.00 <b>(+237.31%)</b></td><td>1.60 <b>(-53.02%)</b></td><td>1049.20 <b>(-70.35%)</b></td><td>680.00 <b>(-59.50%)</b></td><td>575.50 <b>(-53.08%)</b></td><td>533.40 (+17.96%)</td><td>215.70 <b>(-83.59%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>9.28 (n/a)</td><td>4.38 (n/a)</td><td>3.42 (n/a)</td><td>1.19 (n/a)</td><td>3.40 (n/a)</td><td>3539.20 (n/a)</td><td>1678.96 (n/a)</td><td>1226.50 (n/a)</td><td>452.20 (n/a)</td><td>1314.08 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>10.07 (+12.21%)</td><td>6.85 <b>(+22.46%)</b></td><td>6.52 (-13.87%)</td><td>4.97 <b>(+328.32%)</b></td><td>1.94 <b>(-51.38%)</b></td><td>844.70 <b>(-76.65%)</b></td><td>647.04 <b>(-60.41%)</b></td><td>643.20 (+16.12%)</td><td>416.60 (-10.89%)</td><td>157.20 <b>(-89.98%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>8.97 (n/a)</td><td>5.59 (n/a)</td><td>7.57 (n/a)</td><td>1.16 (n/a)</td><td>3.99 (n/a)</td><td>3618.10 (n/a)</td><td>1634.54 (n/a)</td><td>553.90 (n/a)</td><td>467.50 (n/a)</td><td>1569.45 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>8.31 (+3.54%)</td><td>5.49 (-6.50%)</td><td>6.69 <b>(+33.64%)</b></td><td>1.14 <b>(-73.64%)</b></td><td>3.20 <b>(+77.31%)</b></td><td>3675.90 <b>(+279.31%)</b></td><td>1331.44 <b>(+73.47%)</b></td><td>626.60 <b>(-25.16%)</b></td><td>504.90 (-3.42%)</td><td>1355.15 <b>(+523.73%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>8.02 (n/a)</td><td>5.87 (n/a)</td><td>5.01 (n/a)</td><td>4.33 (n/a)</td><td>1.81 (n/a)</td><td>969.10 (n/a)</td><td>767.52 (n/a)</td><td>837.30 (n/a)</td><td>522.80 (n/a)</td><td>217.26 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>8.72 (-14.89%)</td><td>6.80 <b>(+51.07%)</b></td><td>6.54 <b>(+40.08%)</b></td><td>4.05 <b>(+268.84%)</b></td><td>1.84 <b>(-51.22%)</b></td><td>1035.40 <b>(-72.89%)</b></td><td>663.32 <b>(-65.38%)</b></td><td>641.00 <b>(-28.61%)</b></td><td>480.90 (+17.49%)</td><td>221.35 <b>(-86.82%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>10.25 (n/a)</td><td>4.50 (n/a)</td><td>4.67 (n/a)</td><td>1.10 (n/a)</td><td>3.76 (n/a)</td><td>3819.00 (n/a)</td><td>1915.98 (n/a)</td><td>897.90 (n/a)</td><td>409.30 (n/a)</td><td>1679.44 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>7.51 <b>(-43.72%)</b></td><td>5.14 <b>(-35.58%)</b></td><td>6.34 (-7.55%)</td><td>1.19 <b>(-74.54%)</b></td><td>2.56 <b>(-21.54%)</b></td><td>3533.40 <b>(+292.73%)</b></td><td>1286.38 <b>(+117.73%)</b></td><td>661.30 (+8.16%)</td><td>558.10 <b>(+77.68%)</b></td><td>1270.53 <b>(+498.32%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>13.35 (n/a)</td><td>7.98 (n/a)</td><td>6.86 (n/a)</td><td>4.66 (n/a)</td><td>3.27 (n/a)</td><td>899.70 (n/a)</td><td>590.82 (n/a)</td><td>611.40 (n/a)</td><td>314.10 (n/a)</td><td>212.35 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.90 (+12.67%)</td><td>1.25 <b>(+66.72%)</b></td><td>1.63 <b>(+102.87%)</b></td><td>0.16 (+0.77%)</td><td>0.73 (+14.83%)</td><td>3303.20 (-0.77%)</td><td>964.46 <b>(-40.86%)</b></td><td>321.20 <b>(-50.71%)</b></td><td>276.30 (-11.24%)</td><td>1314.57 (-14.95%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.68 (n/a)</td><td>0.75 (n/a)</td><td>0.80 (n/a)</td><td>0.16 (n/a)</td><td>0.64 (n/a)</td><td>3328.70 (n/a)</td><td>1630.80 (n/a)</td><td>651.60 (n/a)</td><td>311.30 (n/a)</td><td>1545.64 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>2.42 <b>(-20.81%)</b></td><td>1.35 <b>(-43.41%)</b></td><td>1.36 <b>(-43.69%)</b></td><td>0.30 <b>(-80.98%)</b></td><td>0.75 <b>(+39.61%)</b></td><td>3537.00 <b>(+425.79%)</b></td><td>1262.30 <b>(+173.63%)</b></td><td>768.90 <b>(+77.58%)</b></td><td>432.70 <b>(+26.26%)</b></td><td>1280.66 <b>(+927.68%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>3.06 (n/a)</td><td>2.39 (n/a)</td><td>2.42 (n/a)</td><td>1.56 (n/a)</td><td>0.54 (n/a)</td><td>672.70 (n/a)</td><td>461.32 (n/a)</td><td>433.00 (n/a)</td><td>342.70 (n/a)</td><td>124.62 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>3.71 <b>(+37.84%)</b></td><td>2.54 <b>(+74.51%)</b></td><td>2.56 <b>(+125.50%)</b></td><td>0.60 (-1.60%)</td><td>1.23 <b>(+32.28%)</b></td><td>3524.50 (+1.63%)</td><td>1278.12 <b>(-36.70%)</b></td><td>819.80 <b>(-55.65%)</b></td><td>565.20 <b>(-27.45%)</b></td><td>1262.86 (+4.86%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>2.69 (n/a)</td><td>1.46 (n/a)</td><td>1.13 (n/a)</td><td>0.60 (n/a)</td><td>0.93 (n/a)</td><td>3468.00 (n/a)</td><td>2019.18 (n/a)</td><td>1848.60 (n/a)</td><td>779.10 (n/a)</td><td>1204.29 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>1.99 <b>(+21.33%)</b></td><td>1.49 <b>(+22.35%)</b></td><td>1.51 <b>(+35.62%)</b></td><td>0.74 (-5.46%)</td><td>0.46 <b>(+20.22%)</b></td><td>708.50 (+5.78%)</td><td>395.28 (-15.55%)</td><td>347.70 <b>(-26.27%)</b></td><td>264.10 (-17.57%)</td><td>178.73 (+19.48%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>1.64 (n/a)</td><td>1.22 (n/a)</td><td>1.11 (n/a)</td><td>0.78 (n/a)</td><td>0.39 (n/a)</td><td>669.80 (n/a)</td><td>468.06 (n/a)</td><td>471.60 (n/a)</td><td>320.40 (n/a)</td><td>149.59 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.13 (+11.81%)</td><td>0.09 (+1.03%)</td><td>0.08 (-14.52%)</td><td>0.06 (+11.27%)</td><td>0.03 (-5.12%)</td><td>547.10 (-10.13%)</td><td>401.82 (-3.82%)</td><td>397.60 (+16.98%)</td><td>255.40 (-10.57%)</td><td>109.72 <b>(-26.04%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>608.80 (n/a)</td><td>417.80 (n/a)</td><td>339.90 (n/a)</td><td>285.60 (n/a)</td><td>148.35 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.15 (+12.19%)</td><td>0.07 <b>(-30.17%)</b></td><td>0.06 <b>(-45.98%)</b></td><td>0.02 <b>(-70.98%)</b></td><td>0.05 <b>(+39.94%)</b></td><td>2079.30 <b>(+244.54%)</b></td><td>790.46 <b>(+111.18%)</b></td><td>588.50 <b>(+85.12%)</b></td><td>222.30 (-10.90%)</td><td>735.98 <b>(+384.03%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>603.50 (n/a)</td><td>374.30 (n/a)</td><td>317.90 (n/a)</td><td>249.50 (n/a)</td><td>152.05 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.25 (-2.35%)</td><td>0.14 (-16.04%)</td><td>0.14 (-1.96%)</td><td>0.03 <b>(-75.28%)</b></td><td>0.08 <b>(+54.91%)</b></td><td>2047.20 <b>(+304.43%)</b></td><td>745.78 <b>(+81.03%)</b></td><td>459.70 (+2.02%)</td><td>262.80 (+2.42%)</td><td>736.39 <b>(+640.61%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>506.20 (n/a)</td><td>411.96 (n/a)</td><td>450.60 (n/a)</td><td>256.60 (n/a)</td><td>99.43 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.33 <b>(+23.43%)</b></td><td>0.22 (+16.00%)</td><td>0.22 (+3.97%)</td><td>0.14 (+19.18%)</td><td>0.08 <b>(+40.12%)</b></td><td>474.40 (-16.09%)</td><td>328.26 (-11.29%)</td><td>297.90 (-3.81%)</td><td>200.40 (-18.96%)</td><td>122.94 (-4.20%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>565.40 (n/a)</td><td>370.04 (n/a)</td><td>309.70 (n/a)</td><td>247.30 (n/a)</td><td>128.33 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.28 <b>(+25.27%)</b></td><td>0.19 (+18.96%)</td><td>0.18 (-16.41%)</td><td>0.15 <b>(+316.11%)</b></td><td>0.06 <b>(-34.35%)</b></td><td>447.90 <b>(-75.96%)</b></td><td>359.98 <b>(-46.12%)</b></td><td>365.40 (+19.65%)</td><td>231.10 <b>(-20.17%)</b></td><td>90.76 <b>(-86.66%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>0.09 (n/a)</td><td>1863.50 (n/a)</td><td>668.16 (n/a)</td><td>305.40 (n/a)</td><td>289.50 (n/a)</td><td>680.44 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.78 <b>(+35.78%)</b></td><td>0.37 (-18.78%)</td><td>0.27 <b>(-43.45%)</b></td><td>0.22 (-16.10%)</td><td>0.24 <b>(+98.32%)</b></td><td>605.50 (+19.19%)</td><td>440.18 <b>(+40.05%)</b></td><td>478.90 <b>(+76.85%)</b></td><td>167.20 <b>(-26.34%)</b></td><td>163.17 <b>(+46.48%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.58 (n/a)</td><td>0.45 (n/a)</td><td>0.48 (n/a)</td><td>0.26 (n/a)</td><td>0.12 (n/a)</td><td>508.00 (n/a)</td><td>314.30 (n/a)</td><td>270.80 (n/a)</td><td>227.00 (n/a)</td><td>111.39 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.53 (+14.90%)</td><td>0.41 (+18.54%)</td><td>0.45 <b>(+62.96%)</b></td><td>0.22 (-15.39%)</td><td>0.13 <b>(+28.13%)</b></td><td>598.40 (+18.19%)</td><td>361.62 (-12.02%)</td><td>290.70 <b>(-38.64%)</b></td><td>246.50 (-12.99%)</td><td>148.14 <b>(+31.03%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.46 (n/a)</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.10 (n/a)</td><td>506.30 (n/a)</td><td>411.04 (n/a)</td><td>473.80 (n/a)</td><td>283.30 (n/a)</td><td>113.06 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.68 <b>(+20.59%)</b></td><td>0.35 (-9.76%)</td><td>0.29 <b>(-38.71%)</b></td><td>0.25 <b>(+22.26%)</b></td><td>0.18 (+11.36%)</td><td>531.10 (-18.20%)</td><td>424.48 (+6.61%)</td><td>454.90 <b>(+63.16%)</b></td><td>191.80 (-17.08%)</td><td>134.41 <b>(-31.07%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.57 (n/a)</td><td>0.39 (n/a)</td><td>0.47 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>649.30 (n/a)</td><td>398.16 (n/a)</td><td>278.80 (n/a)</td><td>231.30 (n/a)</td><td>195.00 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:22:34</td><td>0.06 (-11.76%)</td><td>0.04 (-5.36%)</td><td>0.04 (-19.64%)</td><td>0.03 <b>(+21.50%)</b></td><td>0.01 <b>(-20.45%)</b></td><td>527.00 (-17.69%)</td><td>406.76 (+0.47%)</td><td>440.90 <b>(+24.44%)</b></td><td>279.60 (+13.34%)</td><td>118.59 <b>(-28.09%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:32:26</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>640.30 (n/a)</td><td>404.84 (n/a)</td><td>354.30 (n/a)</td><td>246.70 (n/a)</td><td>164.91 (n/a)</td>
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
