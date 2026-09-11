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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.05 (-15.02%)</td><td>0.03 <b>(-40.15%)</b></td><td>0.03 <b>(-48.01%)</b></td><td>0.02 <b>(-51.68%)</b></td><td>0.01 <b>(+76.64%)</b></td><td>621.60 <b>(+106.92%)</b></td><td>461.80 <b>(+77.75%)</b></td><td>471.10 <b>(+92.36%)</b></td><td>272.50 (+17.71%)</td><td>124.52 <b>(+303.11%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>300.40 (n/a)</td><td>259.80 (n/a)</td><td>244.90 (n/a)</td><td>231.50 (n/a)</td><td>30.89 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.08 <b>(+55.19%)</b></td><td>0.04 (-6.73%)</td><td>0.03 <b>(-41.01%)</b></td><td>0.02 <b>(-33.66%)</b></td><td>0.03 <b>(+189.77%)</b></td><td>596.40 <b>(+50.72%)</b></td><td>377.26 <b>(+31.12%)</b></td><td>441.10 <b>(+69.52%)</b></td><td>148.40 <b>(-35.56%)</b></td><td>175.08 <b>(+165.58%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>395.70 (n/a)</td><td>287.72 (n/a)</td><td>260.20 (n/a)</td><td>230.30 (n/a)</td><td>65.92 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.06 (-0.41%)</td><td>0.04 (+1.89%)</td><td>0.03 <b>(-21.20%)</b></td><td>0.02 (+14.60%)</td><td>0.02 (-0.66%)</td><td>538.80 (-12.74%)</td><td>373.00 (-4.83%)</td><td>430.70 <b>(+26.90%)</b></td><td>199.50 (+0.40%)</td><td>150.73 (-18.88%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>617.50 (n/a)</td><td>391.94 (n/a)</td><td>339.40 (n/a)</td><td>198.70 (n/a)</td><td>185.80 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (+16.16%)</td><td>0.01 (-13.53%)</td><td>0.01 <b>(-33.55%)</b></td><td>0.01 (-1.91%)</td><td>0.01 <b>(+40.78%)</b></td><td>519.30 (+1.94%)</td><td>420.32 <b>(+21.14%)</b></td><td>438.20 <b>(+50.48%)</b></td><td>200.40 (-13.92%)</td><td>128.79 (+15.52%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.40 (n/a)</td><td>346.98 (n/a)</td><td>291.20 (n/a)</td><td>232.80 (n/a)</td><td>111.49 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (-1.62%)</td><td>0.01 (-6.34%)</td><td>0.01 (+4.23%)</td><td>0.01 (-17.62%)</td><td>0.00 (+3.87%)</td><td>597.90 <b>(+21.40%)</b></td><td>435.54 (+8.18%)</td><td>421.70 (-4.05%)</td><td>290.70 (+1.64%)</td><td>116.45 <b>(+27.43%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>492.50 (n/a)</td><td>402.60 (n/a)</td><td>439.50 (n/a)</td><td>286.00 (n/a)</td><td>91.38 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (-1.93%)</td><td>0.01 <b>(-21.90%)</b></td><td>0.01 <b>(-36.52%)</b></td><td>0.01 <b>(-21.32%)</b></td><td>0.01 <b>(+23.10%)</b></td><td>583.30 <b>(+27.08%)</b></td><td>395.80 <b>(+33.96%)</b></td><td>425.60 <b>(+57.57%)</b></td><td>229.80 (+2.00%)</td><td>137.98 <b>(+47.44%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>459.00 (n/a)</td><td>295.46 (n/a)</td><td>270.10 (n/a)</td><td>225.30 (n/a)</td><td>93.58 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.01 <b>(-37.90%)</b></td><td>0.01 (-14.58%)</td><td>0.01 (+1.00%)</td><td>0.00 (+15.76%)</td><td>0.00 <b>(-53.97%)</b></td><td>2073.80 (-13.61%)</td><td>756.24 <b>(-27.72%)</b></td><td>437.40 (-1.00%)</td><td>374.70 <b>(+61.02%)</b></td><td>737.24 <b>(-28.52%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2400.60 (n/a)</td><td>1046.30 (n/a)</td><td>441.80 (n/a)</td><td>232.70 (n/a)</td><td>1031.46 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 <b>(+26.04%)</b></td><td>0.01 (-8.06%)</td><td>0.01 <b>(-38.34%)</b></td><td>0.01 (-16.08%)</td><td>0.01 <b>(+30.97%)</b></td><td>617.20 (+19.17%)</td><td>418.80 (+14.25%)</td><td>445.90 <b>(+62.15%)</b></td><td>209.00 <b>(-20.68%)</b></td><td>164.23 <b>(+21.17%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>517.90 (n/a)</td><td>366.58 (n/a)</td><td>275.00 (n/a)</td><td>263.50 (n/a)</td><td>135.53 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.01 (-11.82%)</td><td>0.01 (+5.22%)</td><td>0.01 (-13.40%)</td><td>0.01 <b>(+104.81%)</b></td><td>0.00 <b>(-31.09%)</b></td><td>991.30 <b>(-51.17%)</b></td><td>540.72 <b>(-29.26%)</b></td><td>482.60 (+15.45%)</td><td>356.10 (+13.41%)</td><td>259.24 <b>(-63.89%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2030.30 (n/a)</td><td>764.40 (n/a)</td><td>418.00 (n/a)</td><td>314.00 (n/a)</td><td>717.86 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>617.80 (n/a)</td><td>438.60 (n/a)</td><td>415.40 (n/a)</td><td>260.90 (n/a)</td><td>130.16 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>271.20 (n/a)</td><td>260.64 (n/a)</td><td>266.80 (n/a)</td><td>234.00 (n/a)</td><td>15.21 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>462.00 (n/a)</td><td>393.14 (n/a)</td><td>422.20 (n/a)</td><td>282.50 (n/a)</td><td>73.91 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>474.70 (n/a)</td><td>375.78 (n/a)</td><td>396.80 (n/a)</td><td>268.00 (n/a)</td><td>102.66 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>619.00 (n/a)</td><td>422.40 (n/a)</td><td>415.80 (n/a)</td><td>276.60 (n/a)</td><td>146.99 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>563.40 (n/a)</td><td>363.08 (n/a)</td><td>268.70 (n/a)</td><td>248.10 (n/a)</td><td>148.87 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.27 (-3.77%)</td><td>0.86 (+12.63%)</td><td>0.84 <b>(+28.71%)</b></td><td>0.51 <b>(+25.88%)</b></td><td>0.27 <b>(-20.18%)</b></td><td>895.40 <b>(-20.56%)</b></td><td>578.92 (-16.38%)</td><td>543.50 <b>(-22.31%)</b></td><td>360.00 (+3.93%)</td><td>195.93 <b>(-31.09%)</b></td><td>93.21 (-3.77%)</td><td>63.08 (+12.63%)</td><td>61.73 <b>(+28.71%)</b></td><td>37.47 <b>(+25.88%)</b></td><td>20.00 <b>(-20.18%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.32 (n/a)</td><td>0.77 (n/a)</td><td>0.66 (n/a)</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>1127.20 (n/a)</td><td>692.34 (n/a)</td><td>699.60 (n/a)</td><td>346.40 (n/a)</td><td>284.31 (n/a)</td><td>96.86 (n/a)</td><td>56.00 (n/a)</td><td>47.96 (n/a)</td><td>29.77 (n/a)</td><td>25.05 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.52 (-6.61%)</td><td>1.20 (-3.27%)</td><td>1.27 (-5.79%)</td><td>0.70 <b>(-21.59%)</b></td><td>0.30 (-7.27%)</td><td>932.30 <b>(+27.52%)</b></td><td>584.22 (+4.43%)</td><td>516.70 (+6.16%)</td><td>431.30 (+7.08%)</td><td>199.25 <b>(+27.96%)</b></td><td>155.61 (-6.61%)</td><td>123.22 (-3.27%)</td><td>129.89 (-5.79%)</td><td>71.98 <b>(-21.59%)</b></td><td>31.18 (-7.27%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.63 (n/a)</td><td>1.24 (n/a)</td><td>1.35 (n/a)</td><td>0.90 (n/a)</td><td>0.33 (n/a)</td><td>731.10 (n/a)</td><td>559.44 (n/a)</td><td>486.70 (n/a)</td><td>402.80 (n/a)</td><td>155.71 (n/a)</td><td>166.62 (n/a)</td><td>127.39 (n/a)</td><td>137.87 (n/a)</td><td>91.80 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.43 (-5.48%)</td><td>1.12 (-2.57%)</td><td>1.13 (-6.86%)</td><td>0.66 <b>(+56.54%)</b></td><td>0.29 <b>(-32.03%)</b></td><td>1135.00 <b>(-36.12%)</b></td><td>723.86 (-11.12%)</td><td>665.90 (+7.37%)</td><td>526.30 (+5.79%)</td><td>239.21 <b>(-55.74%)</b></td><td>159.38 (-5.48%)</td><td>124.12 (-2.57%)</td><td>125.97 (-6.86%)</td><td>73.91 <b>(+56.54%)</b></td><td>31.91 <b>(-32.03%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.51 (n/a)</td><td>1.14 (n/a)</td><td>1.22 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>1776.70 (n/a)</td><td>814.40 (n/a)</td><td>620.20 (n/a)</td><td>497.50 (n/a)</td><td>540.45 (n/a)</td><td>168.61 (n/a)</td><td>127.40 (n/a)</td><td>135.26 (n/a)</td><td>47.21 (n/a)</td><td>46.94 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.50 (-15.14%)</td><td>1.23 (-13.05%)</td><td>1.29 (-5.27%)</td><td>0.97 (-4.57%)</td><td>0.21 <b>(-39.54%)</b></td><td>1079.10 (+4.79%)</td><td>875.76 (+12.11%)</td><td>810.20 (+5.55%)</td><td>700.40 (+17.83%)</td><td>152.13 <b>(-21.42%)</b></td><td>191.62 (-15.14%)</td><td>156.93 (-13.05%)</td><td>165.65 (-5.27%)</td><td>124.37 (-4.57%)</td><td>26.66 <b>(-39.54%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.76 (n/a)</td><td>1.41 (n/a)</td><td>1.37 (n/a)</td><td>1.02 (n/a)</td><td>0.34 (n/a)</td><td>1029.80 (n/a)</td><td>781.18 (n/a)</td><td>767.60 (n/a)</td><td>594.40 (n/a)</td><td>193.60 (n/a)</td><td>225.81 (n/a)</td><td>180.48 (n/a)</td><td>174.86 (n/a)</td><td>130.33 (n/a)</td><td>44.09 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>2.10 (-9.31%)</td><td>1.62 (-10.26%)</td><td>1.88 (+7.90%)</td><td>0.87 <b>(-30.66%)</b></td><td>0.51 <b>(+22.41%)</b></td><td>1206.70 <b>(+44.20%)</b></td><td>718.92 (+18.36%)</td><td>558.90 (-7.31%)</td><td>499.20 (+10.25%)</td><td>294.59 <b>(+96.44%)</b></td><td>268.84 (-9.31%)</td><td>207.57 (-10.26%)</td><td>240.16 (+7.90%)</td><td>111.22 <b>(-30.66%)</b></td><td>65.21 <b>(+22.41%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>2.32 (n/a)</td><td>1.81 (n/a)</td><td>1.74 (n/a)</td><td>1.25 (n/a)</td><td>0.42 (n/a)</td><td>836.80 (n/a)</td><td>607.42 (n/a)</td><td>603.00 (n/a)</td><td>452.80 (n/a)</td><td>149.96 (n/a)</td><td>296.44 (n/a)</td><td>231.29 (n/a)</td><td>222.58 (n/a)</td><td>160.39 (n/a)</td><td>53.27 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>2.17 (-9.61%)</td><td>1.69 (+16.71%)</td><td>1.55 (+19.02%)</td><td>1.38 <b>(+51.29%)</b></td><td>0.32 <b>(-43.14%)</b></td><td>758.40 <b>(-33.90%)</b></td><td>638.86 <b>(-20.45%)</b></td><td>675.60 (-15.98%)</td><td>483.90 (+10.63%)</td><td>112.48 <b>(-56.58%)</b></td><td>277.37 (-9.61%)</td><td>215.87 (+16.71%)</td><td>198.66 (+19.02%)</td><td>176.97 <b>(+51.29%)</b></td><td>41.32 <b>(-43.14%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>2.40 (n/a)</td><td>1.45 (n/a)</td><td>1.30 (n/a)</td><td>0.91 (n/a)</td><td>0.57 (n/a)</td><td>1147.40 (n/a)</td><td>803.08 (n/a)</td><td>804.10 (n/a)</td><td>437.40 (n/a)</td><td>259.04 (n/a)</td><td>306.86 (n/a)</td><td>184.97 (n/a)</td><td>166.92 (n/a)</td><td>116.98 (n/a)</td><td>72.66 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.69 (-11.72%)</td><td>1.14 (-0.93%)</td><td>1.17 <b>(-25.73%)</b></td><td>0.49 <b>(+71.13%)</b></td><td>0.45 <b>(-42.77%)</b></td><td>2140.40 <b>(-41.57%)</b></td><td>1101.16 <b>(-38.33%)</b></td><td>898.30 <b>(+34.66%)</b></td><td>622.00 (+13.28%)</td><td>606.27 <b>(-62.26%)</b></td><td>215.78 (-11.72%)</td><td>145.75 (-0.93%)</td><td>149.42 <b>(-25.73%)</b></td><td>62.71 <b>(+71.13%)</b></td><td>57.75 <b>(-42.77%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.91 (n/a)</td><td>1.15 (n/a)</td><td>1.57 (n/a)</td><td>0.29 (n/a)</td><td>0.79 (n/a)</td><td>3662.90 (n/a)</td><td>1785.62 (n/a)</td><td>667.10 (n/a)</td><td>549.10 (n/a)</td><td>1606.62 (n/a)</td><td>244.44 (n/a)</td><td>147.11 (n/a)</td><td>201.18 (n/a)</td><td>36.64 (n/a)</td><td>100.90 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.27 <b>(-23.39%)</b></td><td>0.68 (-11.18%)</td><td>0.53 (-10.74%)</td><td>0.46 (+13.07%)</td><td>0.34 <b>(-32.57%)</b></td><td>787.10 (-11.56%)</td><td>610.94 (+3.13%)</td><td>686.40 (+12.03%)</td><td>283.10 <b>(+30.52%)</b></td><td>212.96 (-14.79%)</td><td>59.26 <b>(-23.39%)</b></td><td>31.78 (-11.18%)</td><td>24.44 (-10.74%)</td><td>21.31 (+13.07%)</td><td>16.00 <b>(-32.57%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.66 (n/a)</td><td>0.77 (n/a)</td><td>0.59 (n/a)</td><td>0.41 (n/a)</td><td>0.51 (n/a)</td><td>890.00 (n/a)</td><td>592.38 (n/a)</td><td>612.70 (n/a)</td><td>216.90 (n/a)</td><td>249.93 (n/a)</td><td>77.36 (n/a)</td><td>35.78 (n/a)</td><td>27.38 (n/a)</td><td>18.85 (n/a)</td><td>23.74 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>3.66 (-7.69%)</td><td>1.97 <b>(-39.90%)</b></td><td>1.07 <b>(-70.17%)</b></td><td>0.69 <b>(-71.65%)</b></td><td>1.55 <b>(+117.73%)</b></td><td>3807.50 <b>(+252.77%)</b></td><td>2219.12 <b>(+166.08%)</b></td><td>2458.20 <b>(+235.27%)</b></td><td>716.20 (+8.33%)</td><td>1456.33 <b>(+647.10%)</b></td><td>749.60 (-7.69%)</td><td>403.23 <b>(-39.90%)</b></td><td>218.40 <b>(-70.17%)</b></td><td>141.00 <b>(-71.65%)</b></td><td>317.27 <b>(+117.73%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>3.97 (n/a)</td><td>3.28 (n/a)</td><td>3.58 (n/a)</td><td>2.43 (n/a)</td><td>0.71 (n/a)</td><td>1079.30 (n/a)</td><td>834.02 (n/a)</td><td>733.20 (n/a)</td><td>661.10 (n/a)</td><td>194.93 (n/a)</td><td>812.05 (n/a)</td><td>670.89 (n/a)</td><td>732.24 (n/a)</td><td>497.45 (n/a)</td><td>145.72 (n/a)</td>
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


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn16-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn32-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma16-default]

_No metrics available._


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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>644.70 (n/a)</td><td>400.62 (n/a)</td><td>385.80 (n/a)</td><td>233.40 (n/a)</td><td>164.64 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>511.20 (n/a)</td><td>380.98 (n/a)</td><td>412.50 (n/a)</td><td>198.90 (n/a)</td><td>134.41 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>638.90 (n/a)</td><td>375.26 (n/a)</td><td>305.00 (n/a)</td><td>248.00 (n/a)</td><td>163.84 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1858.20 (n/a)</td><td>646.76 (n/a)</td><td>450.90 (n/a)</td><td>221.40 (n/a)</td><td>686.95 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>458.70 (n/a)</td><td>339.04 (n/a)</td><td>300.80 (n/a)</td><td>237.20 (n/a)</td><td>88.22 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1891.00 (n/a)</td><td>716.60 (n/a)</td><td>483.70 (n/a)</td><td>218.40 (n/a)</td><td>672.10 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.49 (-18.74%)</td><td>0.42 (-16.94%)</td><td>0.46 (-13.44%)</td><td>0.26 (-19.62%)</td><td>0.09 (-12.85%)</td><td>835.40 <b>(+24.43%)</b></td><td>556.96 <b>(+21.15%)</b></td><td>483.60 (+15.53%)</td><td>447.60 <b>(+23.07%)</b></td><td>159.09 <b>(+31.22%)</b></td><td>21.08 (-18.74%)</td><td>17.82 (-16.94%)</td><td>19.52 (-13.44%)</td><td>11.30 (-19.62%)</td><td>3.86 (-12.85%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.61 (n/a)</td><td>0.50 (n/a)</td><td>0.53 (n/a)</td><td>0.33 (n/a)</td><td>0.10 (n/a)</td><td>671.40 (n/a)</td><td>459.72 (n/a)</td><td>418.60 (n/a)</td><td>363.70 (n/a)</td><td>121.24 (n/a)</td><td>25.95 (n/a)</td><td>21.45 (n/a)</td><td>22.54 (n/a)</td><td>14.06 (n/a)</td><td>4.43 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.48 (-16.49%)</td><td>0.38 (-14.37%)</td><td>0.36 (-16.80%)</td><td>0.31 (+12.25%)</td><td>0.06 <b>(-47.80%)</b></td><td>706.30 (-10.91%)</td><td>599.12 (+11.34%)</td><td>615.30 <b>(+20.18%)</b></td><td>464.30 (+19.76%)</td><td>92.91 <b>(-43.77%)</b></td><td>20.32 (-16.49%)</td><td>16.08 (-14.37%)</td><td>15.34 (-16.80%)</td><td>13.36 (+12.25%)</td><td>2.71 <b>(-47.80%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.57 (n/a)</td><td>0.44 (n/a)</td><td>0.43 (n/a)</td><td>0.28 (n/a)</td><td>0.12 (n/a)</td><td>792.80 (n/a)</td><td>538.08 (n/a)</td><td>512.00 (n/a)</td><td>387.70 (n/a)</td><td>165.25 (n/a)</td><td>24.34 (n/a)</td><td>18.78 (n/a)</td><td>18.43 (n/a)</td><td>11.90 (n/a)</td><td>5.19 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.31 (-0.35%)</td><td>0.31 (-0.22%)</td><td>0.31 (-0.29%)</td><td>0.30 (+0.93%)</td><td>0.00 <b>(-32.86%)</b></td><td>83735.30 (-0.92%)</td><td>82138.82 (+0.20%)</td><td>81730.00 (+0.29%)</td><td>81282.90 (+0.35%)</td><td>978.60 <b>(-33.25%)</b></td><td>211.36 (-0.35%)</td><td>209.18 (-0.22%)</td><td>210.20 (-0.29%)</td><td>205.17 (+0.93%)</td><td>2.47 <b>(-32.86%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.01 (n/a)</td><td>84511.80 (n/a)</td><td>81970.98 (n/a)</td><td>81492.10 (n/a)</td><td>80996.00 (n/a)</td><td>1466.14 (n/a)</td><td>212.11 (n/a)</td><td>209.64 (n/a)</td><td>210.82 (n/a)</td><td>203.28 (n/a)</td><td>3.67 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.15 (-2.19%)</td><td>1.13 (-1.15%)</td><td>1.13 (-1.04%)</td><td>1.08 (-2.12%)</td><td>0.03 (-4.60%)</td><td>23212.20 (+2.17%)</td><td>22354.56 (+1.16%)</td><td>22176.00 (+1.05%)</td><td>21901.30 (+2.24%)</td><td>527.30 (-0.45%)</td><td>784.42 (-2.19%)</td><td>768.85 (-1.15%)</td><td>774.70 (-1.04%)</td><td>740.12 (-2.12%)</td><td>17.79 (-4.60%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.17 (n/a)</td><td>1.14 (n/a)</td><td>1.15 (n/a)</td><td>1.11 (n/a)</td><td>0.03 (n/a)</td><td>22719.90 (n/a)</td><td>22098.94 (n/a)</td><td>21945.10 (n/a)</td><td>21422.00 (n/a)</td><td>529.69 (n/a)</td><td>801.97 (n/a)</td><td>777.76 (n/a)</td><td>782.86 (n/a)</td><td>756.16 (n/a)</td><td>18.65 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>2.99 <b>(-26.47%)</b></td><td>1.96 <b>(-40.89%)</b></td><td>1.82 <b>(-52.24%)</b></td><td>1.03 <b>(-40.55%)</b></td><td>0.80 (-19.71%)</td><td>7805.40 <b>(+68.21%)</b></td><td>4748.36 <b>(+76.14%)</b></td><td>4425.00 <b>(+109.40%)</b></td><td>2692.50 <b>(+36.01%)</b></td><td>2049.39 <b>(+81.47%)</b></td><td>785.13 <b>(-26.47%)</b></td><td>513.92 <b>(-40.89%)</b></td><td>477.73 <b>(-52.24%)</b></td><td>270.83 <b>(-40.55%)</b></td><td>208.52 (-19.71%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>4.07 (n/a)</td><td>3.32 (n/a)</td><td>3.81 (n/a)</td><td>1.74 (n/a)</td><td>0.99 (n/a)</td><td>4640.30 (n/a)</td><td>2695.82 (n/a)</td><td>2113.20 (n/a)</td><td>1979.70 (n/a)</td><td>1129.34 (n/a)</td><td>1067.78 (n/a)</td><td>869.50 (n/a)</td><td>1000.35 (n/a)</td><td>455.56 (n/a)</td><td>259.69 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.22 (-14.51%)</td><td>0.21 (+0.97%)</td><td>0.22 (+3.38%)</td><td>0.20 (+15.96%)</td><td>0.01 <b>(-66.37%)</b></td><td>6253.80 (-13.76%)</td><td>5881.56 (-2.47%)</td><td>5698.20 (-3.27%)</td><td>5646.00 (+16.97%)</td><td>299.21 <b>(-65.95%)</b></td><td>11.89 (-14.51%)</td><td>11.43 (+0.97%)</td><td>11.78 (+3.38%)</td><td>10.73 (+15.96%)</td><td>0.57 <b>(-66.37%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>7252.00 (n/a)</td><td>6030.58 (n/a)</td><td>5891.00 (n/a)</td><td>4826.80 (n/a)</td><td>878.83 (n/a)</td><td>13.90 (n/a)</td><td>11.32 (n/a)</td><td>11.39 (n/a)</td><td>9.25 (n/a)</td><td>1.70 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>3.75 (n/a)</td><td>3.61 (n/a)</td><td>3.58 (n/a)</td><td>3.45 (n/a)</td><td>0.13 (n/a)</td><td>3.75 (n/a)</td><td>3.61 (n/a)</td><td>3.57 (n/a)</td><td>3.45 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>7.66 (+0.25%)</td><td>6.80 (+3.84%)</td><td>6.85 (+10.22%)</td><td>5.69 (+0.41%)</td><td>0.77 (-19.84%)</td><td>7.65 (+0.25%)</td><td>6.80 (+3.84%)</td><td>6.85 (+10.22%)</td><td>5.69 (+0.41%)</td><td>0.76 (-19.84%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>7.64 (n/a)</td><td>6.55 (n/a)</td><td>6.22 (n/a)</td><td>5.67 (n/a)</td><td>0.95 (n/a)</td><td>7.63 (n/a)</td><td>6.54 (n/a)</td><td>6.21 (n/a)</td><td>5.66 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>13.82 (+3.94%)</td><td>12.02 (+6.19%)</td><td>13.56 (+9.74%)</td><td>8.59 (+2.02%)</td><td>2.39 (+19.05%)</td><td>13.81 (+3.94%)</td><td>12.01 (+6.19%)</td><td>13.55 (+9.74%)</td><td>8.58 (+2.02%)</td><td>2.38 (+19.05%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>13.29 (n/a)</td><td>11.32 (n/a)</td><td>12.35 (n/a)</td><td>8.42 (n/a)</td><td>2.00 (n/a)</td><td>13.29 (n/a)</td><td>11.31 (n/a)</td><td>12.35 (n/a)</td><td>8.41 (n/a)</td><td>2.00 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>3.93 (n/a)</td><td>3.61 (n/a)</td><td>3.64 (n/a)</td><td>3.20 (n/a)</td><td>0.26 (n/a)</td><td>3.93 (n/a)</td><td>3.61 (n/a)</td><td>3.64 (n/a)</td><td>3.20 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>6.91 (-7.25%)</td><td>6.44 (-1.66%)</td><td>6.48 (-10.38%)</td><td>5.63 (+12.95%)</td><td>0.50 <b>(-56.54%)</b></td><td>6.90 (-7.25%)</td><td>6.43 (-1.66%)</td><td>6.47 (-10.38%)</td><td>5.63 (+12.95%)</td><td>0.50 <b>(-56.54%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>7.45 (n/a)</td><td>6.55 (n/a)</td><td>7.23 (n/a)</td><td>4.99 (n/a)</td><td>1.14 (n/a)</td><td>7.44 (n/a)</td><td>6.54 (n/a)</td><td>7.22 (n/a)</td><td>4.98 (n/a)</td><td>1.14 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>13.75 (-1.96%)</td><td>10.07 (-8.85%)</td><td>9.65 (-0.70%)</td><td>8.07 (-1.81%)</td><td>2.26 (-16.17%)</td><td>13.74 (-1.96%)</td><td>10.07 (-8.85%)</td><td>9.65 (-0.70%)</td><td>8.07 (-1.81%)</td><td>2.26 (-16.17%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>14.02 (n/a)</td><td>11.05 (n/a)</td><td>9.72 (n/a)</td><td>8.22 (n/a)</td><td>2.70 (n/a)</td><td>14.01 (n/a)</td><td>11.04 (n/a)</td><td>9.72 (n/a)</td><td>8.22 (n/a)</td><td>2.70 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>3.12 (+8.12%)</td><td>1.96 (-6.35%)</td><td>1.22 <b>(-47.66%)</b></td><td>1.19 (+1.36%)</td><td>1.03 <b>(+24.91%)</b></td><td>3.11 (+8.12%)</td><td>1.95 (-6.35%)</td><td>1.22 <b>(-47.66%)</b></td><td>1.19 (+1.36%)</td><td>1.03 <b>(+24.91%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>2.88 (n/a)</td><td>2.09 (n/a)</td><td>2.34 (n/a)</td><td>1.17 (n/a)</td><td>0.83 (n/a)</td><td>2.88 (n/a)</td><td>2.09 (n/a)</td><td>2.33 (n/a)</td><td>1.17 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.56 (+0.67%)</td><td>0.34 (-6.23%)</td><td>0.35 (+7.54%)</td><td>0.08 <b>(-38.29%)</b></td><td>0.20 (+16.60%)</td><td>0.55 (+0.67%)</td><td>0.34 (-6.23%)</td><td>0.34 (+7.54%)</td><td>0.08 <b>(-38.29%)</b></td><td>0.20 (+16.60%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.55 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.12 (n/a)</td><td>0.17 (n/a)</td><td>0.54 (n/a)</td><td>0.36 (n/a)</td><td>0.32 (n/a)</td><td>0.12 (n/a)</td><td>0.17 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.77 (+17.40%)</td><td>0.52 <b>(+48.68%)</b></td><td>0.45 <b>(+29.34%)</b></td><td>0.28 <b>(+258.87%)</b></td><td>0.21 <b>(-24.02%)</b></td><td>0.76 (+17.40%)</td><td>0.51 <b>(+48.68%)</b></td><td>0.44 <b>(+29.34%)</b></td><td>0.27 <b>(+258.87%)</b></td><td>0.20 <b>(-24.02%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.66 (n/a)</td><td>0.35 (n/a)</td><td>0.35 (n/a)</td><td>0.08 (n/a)</td><td>0.27 (n/a)</td><td>0.65 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>0.27 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>2.72 (+19.84%)</td><td>1.60 (+15.02%)</td><td>1.65 (-3.93%)</td><td>0.75 <b>(+70.29%)</b></td><td>0.73 (-4.10%)</td><td>2.67 (+19.84%)</td><td>1.57 (+15.02%)</td><td>1.62 (-3.93%)</td><td>0.74 <b>(+70.29%)</b></td><td>0.72 (-4.10%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>2.27 (n/a)</td><td>1.39 (n/a)</td><td>1.72 (n/a)</td><td>0.44 (n/a)</td><td>0.76 (n/a)</td><td>2.23 (n/a)</td><td>1.37 (n/a)</td><td>1.69 (n/a)</td><td>0.44 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>657.10 (n/a)</td><td>444.26 (n/a)</td><td>470.90 (n/a)</td><td>266.60 (n/a)</td><td>172.97 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>699.00 (n/a)</td><td>440.36 (n/a)</td><td>354.60 (n/a)</td><td>263.70 (n/a)</td><td>179.27 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>560.90 (n/a)</td><td>425.94 (n/a)</td><td>427.30 (n/a)</td><td>259.20 (n/a)</td><td>108.93 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>583.60 (n/a)</td><td>363.68 (n/a)</td><td>296.10 (n/a)</td><td>198.10 (n/a)</td><td>153.91 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>498.30 (n/a)</td><td>463.26 (n/a)</td><td>496.30 (n/a)</td><td>347.20 (n/a)</td><td>65.39 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>527.60 (n/a)</td><td>451.66 (n/a)</td><td>457.80 (n/a)</td><td>344.50 (n/a)</td><td>69.69 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 <b>(+35.04%)</b></td><td>0.02 <b>(+40.76%)</b></td><td>0.02 (-5.28%)</td><td>0.02 <b>(+286.18%)</b></td><td>0.01 (-18.71%)</td><td>504.10 <b>(-74.10%)</b></td><td>375.74 <b>(-60.54%)</b></td><td>404.80 (+5.58%)</td><td>206.30 <b>(-25.95%)</b></td><td>130.67 <b>(-84.96%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1946.60 (n/a)</td><td>952.32 (n/a)</td><td>383.40 (n/a)</td><td>278.60 (n/a)</td><td>868.60 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 <b>(+21.11%)</b></td><td>0.03 <b>(+49.74%)</b></td><td>0.03 <b>(+66.77%)</b></td><td>0.02 <b>(+266.86%)</b></td><td>0.01 (-13.92%)</td><td>473.30 <b>(-72.74%)</b></td><td>331.76 <b>(-51.03%)</b></td><td>266.00 <b>(-40.04%)</b></td><td>243.90 (-17.43%)</td><td>106.77 <b>(-82.22%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1736.30 (n/a)</td><td>677.42 (n/a)</td><td>443.60 (n/a)</td><td>295.40 (n/a)</td><td>600.66 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (-1.61%)</td><td>0.02 (+5.21%)</td><td>0.02 (+6.41%)</td><td>0.02 <b>(+21.04%)</b></td><td>0.01 <b>(-21.70%)</b></td><td>474.00 (-17.38%)</td><td>345.98 (-8.78%)</td><td>328.20 (-6.04%)</td><td>264.90 (+1.65%)</td><td>87.26 <b>(-33.50%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>573.70 (n/a)</td><td>379.30 (n/a)</td><td>349.30 (n/a)</td><td>260.60 (n/a)</td><td>131.22 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (+14.69%)</td><td>0.02 (-19.36%)</td><td>0.02 <b>(-36.89%)</b></td><td>0.01 <b>(-28.06%)</b></td><td>0.01 <b>(+88.93%)</b></td><td>635.00 <b>(+39.01%)</b></td><td>444.28 <b>(+37.23%)</b></td><td>474.20 <b>(+58.44%)</b></td><td>228.50 (-12.82%)</td><td>165.96 <b>(+116.87%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>456.80 (n/a)</td><td>323.76 (n/a)</td><td>299.30 (n/a)</td><td>262.10 (n/a)</td><td>76.53 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 <b>(+20.24%)</b></td><td>0.03 <b>(+27.51%)</b></td><td>0.03 <b>(+81.48%)</b></td><td>0.01 (+1.82%)</td><td>0.01 <b>(+35.98%)</b></td><td>556.00 (-1.78%)</td><td>350.62 (-18.54%)</td><td>269.90 <b>(-44.88%)</b></td><td>235.90 (-16.82%)</td><td>141.33 (+12.42%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.10 (n/a)</td><td>430.44 (n/a)</td><td>489.70 (n/a)</td><td>283.60 (n/a)</td><td>125.72 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 <b>(+83.21%)</b></td><td>0.02 <b>(+94.11%)</b></td><td>0.03 <b>(+150.01%)</b></td><td>0.02 <b>(+96.57%)</b></td><td>0.01 <b>(+99.65%)</b></td><td>510.60 <b>(-49.13%)</b></td><td>370.22 <b>(-47.82%)</b></td><td>300.10 <b>(-60.01%)</b></td><td>259.00 <b>(-45.42%)</b></td><td>120.53 <b>(-41.17%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1003.70 (n/a)</td><td>709.44 (n/a)</td><td>750.40 (n/a)</td><td>474.50 (n/a)</td><td>204.88 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (+2.77%)</td><td>0.02 <b>(-28.23%)</b></td><td>0.01 (-19.82%)</td><td>0.00 <b>(-78.30%)</b></td><td>0.01 <b>(+48.22%)</b></td><td>2421.10 <b>(+360.81%)</b></td><td>890.04 <b>(+120.47%)</b></td><td>564.90 <b>(+24.73%)</b></td><td>245.00 (-2.70%)</td><td>872.91 <b>(+625.56%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.40 (n/a)</td><td>403.70 (n/a)</td><td>452.90 (n/a)</td><td>251.80 (n/a)</td><td>120.31 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (+0.70%)</td><td>0.02 <b>(+23.68%)</b></td><td>0.02 <b>(+34.49%)</b></td><td>0.02 <b>(+93.52%)</b></td><td>0.00 <b>(-36.44%)</b></td><td>497.70 <b>(-48.32%)</b></td><td>385.64 <b>(-28.97%)</b></td><td>343.40 <b>(-25.65%)</b></td><td>290.30 (-0.72%)</td><td>87.13 <b>(-67.16%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>963.10 (n/a)</td><td>542.94 (n/a)</td><td>461.90 (n/a)</td><td>292.40 (n/a)</td><td>265.36 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (-0.50%)</td><td>0.02 (-13.45%)</td><td>0.02 <b>(-40.35%)</b></td><td>0.02 (+5.25%)</td><td>0.01 (-2.39%)</td><td>501.90 (-4.98%)</td><td>398.00 (+14.71%)</td><td>456.00 <b>(+67.65%)</b></td><td>232.50 (+0.52%)</td><td>120.16 (-5.66%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>528.20 (n/a)</td><td>346.96 (n/a)</td><td>272.00 (n/a)</td><td>231.30 (n/a)</td><td>127.37 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 <b>(+26.97%)</b></td><td>0.03 (+15.50%)</td><td>0.03 (+7.90%)</td><td>0.02 <b>(+23.24%)</b></td><td>0.01 (+13.84%)</td><td>453.10 (-18.86%)</td><td>332.14 (-14.17%)</td><td>267.50 (-7.31%)</td><td>224.10 <b>(-21.23%)</b></td><td>109.94 <b>(-20.10%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>558.40 (n/a)</td><td>386.96 (n/a)</td><td>288.60 (n/a)</td><td>284.50 (n/a)</td><td>137.60 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (-4.43%)</td><td>0.03 (+13.55%)</td><td>0.03 <b>(+40.97%)</b></td><td>0.02 <b>(+27.60%)</b></td><td>0.01 (-18.22%)</td><td>463.60 <b>(-21.62%)</b></td><td>344.30 (-16.50%)</td><td>274.10 <b>(-29.06%)</b></td><td>262.40 (+4.63%)</td><td>106.19 <b>(-33.13%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>591.50 (n/a)</td><td>412.32 (n/a)</td><td>386.40 (n/a)</td><td>250.80 (n/a)</td><td>158.79 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 <b>(-35.68%)</b></td><td>0.02 <b>(-38.49%)</b></td><td>0.01 <b>(-50.13%)</b></td><td>0.01 <b>(-20.59%)</b></td><td>0.00 <b>(-51.96%)</b></td><td>717.50 <b>(+25.94%)</b></td><td>548.68 <b>(+51.90%)</b></td><td>561.20 <b>(+100.50%)</b></td><td>370.70 <b>(+55.49%)</b></td><td>148.60 (-2.91%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>569.70 (n/a)</td><td>361.22 (n/a)</td><td>279.90 (n/a)</td><td>238.40 (n/a)</td><td>153.06 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (-8.19%)</td><td>0.02 (-8.63%)</td><td>0.02 (+14.09%)</td><td>0.01 (-3.48%)</td><td>0.01 (-15.55%)</td><td>589.30 (+3.60%)</td><td>422.68 (+8.08%)</td><td>388.90 (-12.35%)</td><td>251.20 (+8.93%)</td><td>154.65 (+6.46%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>568.80 (n/a)</td><td>391.08 (n/a)</td><td>443.70 (n/a)</td><td>230.60 (n/a)</td><td>145.27 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 <b>(+107.39%)</b></td><td>0.02 <b>(+26.40%)</b></td><td>0.02 (-3.80%)</td><td>0.01 (+9.35%)</td><td>0.01 <b>(+273.60%)</b></td><td>602.90 (-8.54%)</td><td>450.94 (-10.95%)</td><td>487.10 (+3.95%)</td><td>206.10 <b>(-51.78%)</b></td><td>153.99 <b>(+57.56%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>659.20 (n/a)</td><td>506.40 (n/a)</td><td>468.60 (n/a)</td><td>427.40 (n/a)</td><td>97.74 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.09 (-4.33%)</td><td>0.08 (+7.52%)</td><td>0.08 (-10.37%)</td><td>0.07 <b>(+62.45%)</b></td><td>0.01 <b>(-68.90%)</b></td><td>354.60 <b>(-38.44%)</b></td><td>310.86 (-16.91%)</td><td>306.60 (+11.57%)</td><td>270.00 (+4.53%)</td><td>31.54 <b>(-79.33%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>576.00 (n/a)</td><td>374.12 (n/a)</td><td>274.80 (n/a)</td><td>258.30 (n/a)</td><td>152.59 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.17 <b>(-25.30%)</b></td><td>0.15 (+4.87%)</td><td>0.15 (+2.14%)</td><td>0.13 <b>(+50.21%)</b></td><td>0.02 <b>(-72.91%)</b></td><td>326.00 <b>(-33.42%)</b></td><td>279.96 (-17.29%)</td><td>278.70 (-2.11%)</td><td>238.30 <b>(+33.88%)</b></td><td>31.50 <b>(-77.99%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>489.60 (n/a)</td><td>338.50 (n/a)</td><td>284.70 (n/a)</td><td>178.00 (n/a)</td><td>143.13 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (-10.11%)</td><td>0.02 <b>(+24.13%)</b></td><td>0.02 (-10.01%)</td><td>0.01 <b>(+260.95%)</b></td><td>0.00 <b>(-62.95%)</b></td><td>509.30 <b>(-72.30%)</b></td><td>351.70 <b>(-60.84%)</b></td><td>324.40 (+11.10%)</td><td>285.70 (+11.21%)</td><td>92.28 <b>(-89.16%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1838.50 (n/a)</td><td>898.22 (n/a)</td><td>292.00 (n/a)</td><td>256.90 (n/a)</td><td>851.53 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (+2.42%)</td><td>0.03 <b>(+25.26%)</b></td><td>0.03 <b>(+21.60%)</b></td><td>0.02 <b>(+438.46%)</b></td><td>0.01 <b>(-53.26%)</b></td><td>439.50 <b>(-81.43%)</b></td><td>307.42 <b>(-57.96%)</b></td><td>277.90 (-17.76%)</td><td>245.70 (-2.34%)</td><td>76.90 <b>(-91.62%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2366.70 (n/a)</td><td>731.30 (n/a)</td><td>337.90 (n/a)</td><td>251.60 (n/a)</td><td>917.63 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.05 (-6.96%)</td><td>0.04 (+12.07%)</td><td>0.04 (+10.90%)</td><td>0.02 <b>(+24.69%)</b></td><td>0.01 (-14.93%)</td><td>509.20 (-19.80%)</td><td>336.60 (-16.48%)</td><td>280.10 (-9.85%)</td><td>234.20 (+7.48%)</td><td>123.86 <b>(-32.91%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>634.90 (n/a)</td><td>403.02 (n/a)</td><td>310.70 (n/a)</td><td>217.90 (n/a)</td><td>184.63 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 <b>(+25.65%)</b></td><td>0.03 <b>(+63.96%)</b></td><td>0.03 <b>(+121.21%)</b></td><td>0.01 (+4.98%)</td><td>0.01 <b>(+40.03%)</b></td><td>564.50 (-4.74%)</td><td>303.78 <b>(-36.43%)</b></td><td>245.70 <b>(-54.80%)</b></td><td>222.80 <b>(-20.43%)</b></td><td>146.44 (+9.59%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.60 (n/a)</td><td>477.90 (n/a)</td><td>543.60 (n/a)</td><td>280.00 (n/a)</td><td>133.63 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 <b>(-27.65%)</b></td><td>0.03 (+14.74%)</td><td>0.04 <b>(+85.02%)</b></td><td>0.02 <b>(+21.12%)</b></td><td>0.01 <b>(-47.64%)</b></td><td>541.70 (-17.44%)</td><td>329.02 <b>(-27.10%)</b></td><td>272.90 <b>(-45.94%)</b></td><td>239.90 <b>(+38.19%)</b></td><td>125.55 <b>(-43.06%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>656.10 (n/a)</td><td>451.32 (n/a)</td><td>504.80 (n/a)</td><td>173.60 (n/a)</td><td>220.51 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (+13.46%)</td><td>0.02 (-11.98%)</td><td>0.02 <b>(-29.68%)</b></td><td>0.01 (-13.20%)</td><td>0.01 <b>(+28.08%)</b></td><td>619.00 (+15.21%)</td><td>423.38 (+17.37%)</td><td>424.40 <b>(+42.23%)</b></td><td>234.60 (-11.87%)</td><td>138.13 <b>(+23.40%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>537.30 (n/a)</td><td>360.72 (n/a)</td><td>298.40 (n/a)</td><td>266.20 (n/a)</td><td>111.94 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (-2.10%)</td><td>0.04 <b>(+44.59%)</b></td><td>0.04 <b>(+116.92%)</b></td><td>0.02 (+2.62%)</td><td>0.01 (-5.50%)</td><td>528.20 (-2.55%)</td><td>311.02 <b>(-31.53%)</b></td><td>244.40 <b>(-53.90%)</b></td><td>242.90 (+2.14%)</td><td>123.48 (-5.71%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>542.00 (n/a)</td><td>454.24 (n/a)</td><td>530.20 (n/a)</td><td>237.80 (n/a)</td><td>130.96 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (-4.42%)</td><td>0.02 (-13.86%)</td><td>0.02 <b>(-25.08%)</b></td><td>0.01 <b>(+46.66%)</b></td><td>0.01 (-14.42%)</td><td>1071.80 <b>(-31.82%)</b></td><td>482.44 (-8.58%)</td><td>368.00 <b>(+33.48%)</b></td><td>242.80 (+4.66%)</td><td>339.52 <b>(-41.89%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1571.90 (n/a)</td><td>527.74 (n/a)</td><td>275.70 (n/a)</td><td>232.00 (n/a)</td><td>584.29 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.04 (+14.69%)</td><td>0.03 <b>(+21.66%)</b></td><td>0.03 (+16.32%)</td><td>0.02 (+7.57%)</td><td>0.01 (+0.84%)</td><td>469.50 (-7.05%)</td><td>301.04 (-18.71%)</td><td>271.90 (-14.04%)</td><td>232.60 (-12.82%)</td><td>96.01 (-15.90%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.10 (n/a)</td><td>370.34 (n/a)</td><td>316.30 (n/a)</td><td>266.80 (n/a)</td><td>114.15 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (+14.38%)</td><td>0.02 (-9.81%)</td><td>0.02 <b>(-39.59%)</b></td><td>0.01 (+0.07%)</td><td>0.01 <b>(+24.03%)</b></td><td>661.60 (-0.08%)</td><td>441.52 (+14.29%)</td><td>498.20 <b>(+65.51%)</b></td><td>244.20 (-12.57%)</td><td>171.77 (+5.55%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>662.10 (n/a)</td><td>386.32 (n/a)</td><td>301.00 (n/a)</td><td>279.30 (n/a)</td><td>162.74 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.03 (+12.94%)</td><td>0.03 <b>(+64.78%)</b></td><td>0.03 <b>(+66.83%)</b></td><td>0.02 <b>(+396.70%)</b></td><td>0.00 <b>(-57.02%)</b></td><td>377.70 <b>(-79.86%)</b></td><td>307.60 <b>(-57.65%)</b></td><td>291.20 <b>(-40.07%)</b></td><td>272.20 (-11.45%)</td><td>43.03 <b>(-93.35%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1875.80 (n/a)</td><td>726.38 (n/a)</td><td>485.90 (n/a)</td><td>307.40 (n/a)</td><td>647.18 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 <b>(-36.45%)</b></td><td>0.02 (-9.13%)</td><td>0.02 (+2.89%)</td><td>0.01 (+8.73%)</td><td>0.00 <b>(-65.70%)</b></td><td>611.70 (-8.03%)</td><td>499.84 (+2.76%)</td><td>458.70 (-2.82%)</td><td>439.50 <b>(+57.36%)</b></td><td>73.53 <b>(-48.61%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>665.10 (n/a)</td><td>486.42 (n/a)</td><td>472.00 (n/a)</td><td>279.30 (n/a)</td><td>143.07 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.61 <b>(+51.49%)</b></td><td>0.34 (+17.21%)</td><td>0.31 (-6.16%)</td><td>0.17 (+1.45%)</td><td>0.18 <b>(+84.19%)</b></td><td>593.30 (-1.43%)</td><td>362.40 (-3.85%)</td><td>313.50 (+6.56%)</td><td>162.40 <b>(-33.98%)</b></td><td>185.80 <b>(+23.58%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.33 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>601.90 (n/a)</td><td>376.92 (n/a)</td><td>294.20 (n/a)</td><td>246.00 (n/a)</td><td>150.35 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.40 (+18.17%)</td><td>0.22 (-11.11%)</td><td>0.17 <b>(-29.97%)</b></td><td>0.05 <b>(-68.70%)</b></td><td>0.15 <b>(+89.39%)</b></td><td>1852.80 <b>(+219.50%)</b></td><td>746.82 <b>(+75.66%)</b></td><td>562.10 <b>(+42.81%)</b></td><td>245.90 (-15.38%)</td><td>660.68 <b>(+370.21%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>579.90 (n/a)</td><td>425.14 (n/a)</td><td>393.60 (n/a)</td><td>290.60 (n/a)</td><td>140.51 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.65 <b>(+65.68%)</b></td><td>0.37 <b>(+46.95%)</b></td><td>0.33 <b>(+55.07%)</b></td><td>0.24 <b>(+50.63%)</b></td><td>0.16 <b>(+48.16%)</b></td><td>406.00 <b>(-33.62%)</b></td><td>293.40 <b>(-33.99%)</b></td><td>300.90 <b>(-35.51%)</b></td><td>150.70 <b>(-39.62%)</b></td><td>91.50 <b>(-46.82%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.39 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>611.60 (n/a)</td><td>444.46 (n/a)</td><td>466.60 (n/a)</td><td>249.60 (n/a)</td><td>172.06 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.32 <b>(+86.29%)</b></td><td>0.24 <b>(+54.16%)</b></td><td>0.24 <b>(+47.28%)</b></td><td>0.17 <b>(+21.22%)</b></td><td>0.07 <b>(+359.33%)</b></td><td>432.00 (-17.51%)</td><td>324.10 <b>(-31.31%)</b></td><td>310.30 <b>(-32.09%)</b></td><td>229.30 <b>(-46.31%)</b></td><td>91.35 <b>(+102.26%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>523.70 (n/a)</td><td>471.82 (n/a)</td><td>456.90 (n/a)</td><td>427.10 (n/a)</td><td>45.17 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.27 <b>(-28.86%)</b></td><td>0.18 (-4.76%)</td><td>0.17 (+11.22%)</td><td>0.13 (+15.75%)</td><td>0.05 <b>(-48.87%)</b></td><td>546.40 (-13.61%)</td><td>438.26 (-5.06%)</td><td>433.90 (-10.09%)</td><td>277.00 <b>(+40.61%)</b></td><td>112.53 <b>(-29.86%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.37 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>632.50 (n/a)</td><td>461.64 (n/a)</td><td>482.60 (n/a)</td><td>197.00 (n/a)</td><td>160.42 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.34 (+12.57%)</td><td>0.21 (+5.94%)</td><td>0.15 (-6.00%)</td><td>0.14 (-7.13%)</td><td>0.09 <b>(+41.02%)</b></td><td>519.70 (+7.67%)</td><td>393.86 (+0.53%)</td><td>485.70 (+6.40%)</td><td>213.80 (-11.18%)</td><td>145.00 <b>(+35.55%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>482.70 (n/a)</td><td>391.78 (n/a)</td><td>456.50 (n/a)</td><td>240.70 (n/a)</td><td>106.97 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.49 (+15.29%)</td><td>0.32 (+3.07%)</td><td>0.28 (+14.14%)</td><td>0.23 (-3.09%)</td><td>0.11 (+9.69%)</td><td>576.20 (+3.19%)</td><td>443.04 (-2.35%)</td><td>473.80 (-12.39%)</td><td>269.40 (-13.26%)</td><td>131.34 (+0.88%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.10 (n/a)</td><td>558.40 (n/a)</td><td>453.70 (n/a)</td><td>540.80 (n/a)</td><td>310.60 (n/a)</td><td>130.19 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.43 (-10.74%)</td><td>0.29 (-2.84%)</td><td>0.26 (-3.50%)</td><td>0.23 <b>(+264.46%)</b></td><td>0.08 <b>(-50.53%)</b></td><td>561.50 <b>(-72.56%)</b></td><td>474.36 <b>(-34.67%)</b></td><td>497.00 (+3.63%)</td><td>304.50 (+12.03%)</td><td>103.14 <b>(-86.17%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.48 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.06 (n/a)</td><td>0.16 (n/a)</td><td>2046.50 (n/a)</td><td>726.08 (n/a)</td><td>479.60 (n/a)</td><td>271.80 (n/a)</td><td>745.88 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.48 (+1.51%)</td><td>0.29 (-16.43%)</td><td>0.26 (-16.80%)</td><td>0.18 <b>(-25.79%)</b></td><td>0.12 (+10.12%)</td><td>730.00 <b>(+34.74%)</b></td><td>507.52 <b>(+23.60%)</b></td><td>510.60 <b>(+20.20%)</b></td><td>270.70 (-1.49%)</td><td>165.77 <b>(+38.79%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.48 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.11 (n/a)</td><td>541.80 (n/a)</td><td>410.62 (n/a)</td><td>424.80 (n/a)</td><td>274.80 (n/a)</td><td>119.43 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 <b>(+52.05%)</b></td><td>0.01 <b>(+47.09%)</b></td><td>0.02 <b>(+51.34%)</b></td><td>0.01 (+2.88%)</td><td>0.00 <b>(+77.02%)</b></td><td>533.80 (-2.80%)</td><td>307.58 <b>(-28.27%)</b></td><td>262.90 <b>(-33.91%)</b></td><td>194.50 <b>(-34.22%)</b></td><td>131.67 (+14.91%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>549.20 (n/a)</td><td>428.78 (n/a)</td><td>397.80 (n/a)</td><td>295.70 (n/a)</td><td>114.58 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.01 (-3.42%)</td><td>0.01 (-3.46%)</td><td>0.01 (-4.50%)</td><td>0.01 (+5.74%)</td><td>0.00 (-17.42%)</td><td>430.60 (-5.45%)</td><td>346.96 (+2.26%)</td><td>310.40 (+4.69%)</td><td>281.30 (+3.53%)</td><td>67.56 (-16.66%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>455.40 (n/a)</td><td>339.28 (n/a)</td><td>296.50 (n/a)</td><td>271.70 (n/a)</td><td>81.06 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 <b>(+25.45%)</b></td><td>0.01 <b>(+20.27%)</b></td><td>0.01 <b>(+36.38%)</b></td><td>0.01 (-3.40%)</td><td>0.00 <b>(+107.96%)</b></td><td>508.30 (+3.52%)</td><td>365.74 (-13.37%)</td><td>310.40 <b>(-26.69%)</b></td><td>269.50 <b>(-20.29%)</b></td><td>101.43 <b>(+75.86%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>491.00 (n/a)</td><td>422.20 (n/a)</td><td>423.40 (n/a)</td><td>338.10 (n/a)</td><td>57.68 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.47 <b>(-26.24%)</b></td><td>0.37 (-3.15%)</td><td>0.43 <b>(+30.04%)</b></td><td>0.25 (-0.49%)</td><td>0.11 <b>(-31.55%)</b></td><td>537.40 (+0.49%)</td><td>387.96 (-0.78%)</td><td>308.40 <b>(-23.11%)</b></td><td>281.70 <b>(+35.56%)</b></td><td>128.49 (-6.70%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.64 (n/a)</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>534.80 (n/a)</td><td>391.02 (n/a)</td><td>401.10 (n/a)</td><td>207.80 (n/a)</td><td>137.72 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.45 <b>(-24.71%)</b></td><td>0.36 (-16.84%)</td><td>0.34 <b>(-20.05%)</b></td><td>0.25 (+16.00%)</td><td>0.08 <b>(-46.77%)</b></td><td>521.50 (-13.79%)</td><td>383.12 (+10.10%)</td><td>383.30 <b>(+25.10%)</b></td><td>290.40 <b>(+32.85%)</b></td><td>94.09 <b>(-40.04%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.60 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>604.90 (n/a)</td><td>347.96 (n/a)</td><td>306.40 (n/a)</td><td>218.60 (n/a)</td><td>156.93 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.42 (-2.37%)</td><td>0.32 (+5.17%)</td><td>0.30 (-4.10%)</td><td>0.25 (+16.03%)</td><td>0.07 (-13.18%)</td><td>532.60 (-13.80%)</td><td>429.32 (-6.62%)</td><td>447.00 (+4.27%)</td><td>315.80 (+2.43%)</td><td>90.54 <b>(-23.89%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.43 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.08 (n/a)</td><td>617.90 (n/a)</td><td>459.78 (n/a)</td><td>428.70 (n/a)</td><td>308.30 (n/a)</td><td>118.96 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.50 (-7.39%)</td><td>0.35 (-2.69%)</td><td>0.36 <b>(+20.98%)</b></td><td>0.19 (-18.59%)</td><td>0.13 (-2.41%)</td><td>683.60 <b>(+22.84%)</b></td><td>430.44 (+5.27%)</td><td>367.50 (-17.34%)</td><td>265.50 (+7.97%)</td><td>174.76 <b>(+30.78%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.54 (n/a)</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>556.50 (n/a)</td><td>408.88 (n/a)</td><td>444.60 (n/a)</td><td>245.90 (n/a)</td><td>133.63 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.45 (-7.83%)</td><td>0.29 (-15.13%)</td><td>0.30 (-5.56%)</td><td>0.07 <b>(-68.08%)</b></td><td>0.16 <b>(+55.77%)</b></td><td>1826.70 <b>(+213.27%)</b></td><td>707.96 <b>(+71.13%)</b></td><td>446.00 (+5.89%)</td><td>291.70 (+8.48%)</td><td>644.26 <b>(+428.38%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.49 (n/a)</td><td>0.34 (n/a)</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.10 (n/a)</td><td>583.10 (n/a)</td><td>413.70 (n/a)</td><td>421.20 (n/a)</td><td>268.90 (n/a)</td><td>121.93 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (-0.40%)</td><td>0.01 <b>(-28.08%)</b></td><td>0.01 <b>(-35.96%)</b></td><td>0.01 <b>(-48.02%)</b></td><td>0.00 <b>(+166.75%)</b></td><td>594.70 <b>(+92.40%)</b></td><td>410.58 <b>(+55.43%)</b></td><td>403.20 <b>(+56.16%)</b></td><td>235.70 (+0.43%)</td><td>152.58 <b>(+417.75%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>309.10 (n/a)</td><td>264.16 (n/a)</td><td>258.20 (n/a)</td><td>234.70 (n/a)</td><td>29.47 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.02 (-11.61%)</td><td>0.01 (+8.08%)</td><td>0.02 (+19.21%)</td><td>0.01 (+8.17%)</td><td>0.00 (-13.37%)</td><td>470.60 (-7.56%)</td><td>296.18 (-8.92%)</td><td>245.30 (-16.11%)</td><td>237.50 (+13.15%)</td><td>99.18 (-11.07%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>509.10 (n/a)</td><td>325.18 (n/a)</td><td>292.40 (n/a)</td><td>209.90 (n/a)</td><td>111.53 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.00 (+16.67%)</td><td>0.00 <b>(+75.00%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+26.20%)</b></td><td>17400.17 <b>(-22.45%)</b></td><td>8718.18 <b>(-43.38%)</b></td><td>7204.74 <b>(-53.51%)</b></td><td>5704.79 (-9.75%)</td><td>4913.16 (-15.68%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22438.09 (n/a)</td><td>15398.37 (n/a)</td><td>15497.74 (n/a)</td><td>6320.78 (n/a)</td><td>5826.48 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.00 (+7.69%)</td><td>0.00 (-2.33%)</td><td>0.00 <b>(-40.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+8.91%)</td><td>22735.50 (+2.90%)</td><td>13190.16 (+6.22%)</td><td>14285.05 <b>(+77.32%)</b></td><td>5829.19 (-5.65%)</td><td>7191.58 (-5.23%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>22094.93 (n/a)</td><td>12417.20 (n/a)</td><td>8056.24 (n/a)</td><td>6178.47 (n/a)</td><td>7588.41 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>0.14 (+3.68%)</td><td>0.09 (+1.09%)</td><td>0.09 (+5.95%)</td><td>0.07 (+1.12%)</td><td>0.03 (+4.70%)</td><td>28931.51 (-1.13%)</td><td>23203.46 (-0.99%)</td><td>24016.78 (-5.58%)</td><td>14889.54 (-3.62%)</td><td>5121.87 (-2.87%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29260.95 (n/a)</td><td>23435.79 (n/a)</td><td>25437.21 (n/a)</td><td>15448.07 (n/a)</td><td>5273.26 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.81 (+17.50%)</td><td>1.26 (+19.64%)</td><td>1.58 <b>(+63.05%)</b></td><td>0.29 <b>(-48.51%)</b></td><td>0.63 <b>(+49.75%)</b></td><td>1828.50 <b>(+94.21%)</b></td><td>663.60 (+15.19%)</td><td>332.80 <b>(-38.68%)</b></td><td>289.60 (-14.87%)</td><td>659.48 <b>(+165.86%)</b></td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.54 (n/a)</td><td>1.05 (n/a)</td><td>0.97 (n/a)</td><td>0.56 (n/a)</td><td>0.42 (n/a)</td><td>941.50 (n/a)</td><td>576.10 (n/a)</td><td>542.70 (n/a)</td><td>340.20 (n/a)</td><td>248.06 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>2.30 (-17.24%)</td><td>1.39 (+2.55%)</td><td>1.28 (-15.32%)</td><td>0.30 (-9.88%)</td><td>0.75 <b>(-24.87%)</b></td><td>3490.90 (+10.97%)</td><td>1234.12 (-11.16%)</td><td>820.30 (+18.10%)</td><td>455.20 <b>(+20.84%)</b></td><td>1271.46 (+6.79%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>2.78 (n/a)</td><td>1.36 (n/a)</td><td>1.51 (n/a)</td><td>0.33 (n/a)</td><td>0.99 (n/a)</td><td>3145.90 (n/a)</td><td>1389.18 (n/a)</td><td>694.60 (n/a)</td><td>376.70 (n/a)</td><td>1190.61 (n/a)</td>
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
<td><code>b2eb090</code> — 2026-09-11 23:46:51</td><td>1.13 (-12.39%)</td><td>0.95 (-3.10%)</td><td>0.95 (+1.83%)</td><td>0.78 (-1.27%)</td><td>0.14 <b>(-23.36%)</b></td><td>675.10 (+1.29%)</td><td>563.08 (+2.45%)</td><td>553.70 (-1.79%)</td><td>465.30 (+14.13%)</td><td>85.04 (-8.25%)</td>
</tr>
<tr>
<td><code>7b55427</code> — 2026-09-11 19:24:50</td><td>1.29 (n/a)</td><td>0.98 (n/a)</td><td>0.93 (n/a)</td><td>0.79 (n/a)</td><td>0.19 (n/a)</td><td>666.50 (n/a)</td><td>549.64 (n/a)</td><td>563.80 (n/a)</td><td>407.70 (n/a)</td><td>92.68 (n/a)</td>
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
