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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.05 (+9.98%)</td><td>0.04 (+1.69%)</td><td>0.03 (-6.14%)</td><td>0.02 (-10.76%)</td><td>0.02 <b>(+56.21%)</b></td><td>585.70 (+12.07%)</td><td>372.38 (+6.01%)</td><td>364.30 (+6.55%)</td><td>224.00 (-9.09%)</td><td>153.30 <b>(+45.92%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>522.60 (n/a)</td><td>351.28 (n/a)</td><td>341.90 (n/a)</td><td>246.40 (n/a)</td><td>105.06 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.05 (-11.30%)</td><td>0.03 <b>(+21.20%)</b></td><td>0.03 <b>(+28.35%)</b></td><td>0.02 <b>(+251.39%)</b></td><td>0.01 <b>(-32.00%)</b></td><td>681.60 <b>(-71.54%)</b></td><td>408.90 <b>(-48.75%)</b></td><td>362.30 <b>(-22.09%)</b></td><td>266.60 (+12.73%)</td><td>167.40 <b>(-81.36%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>2395.20 (n/a)</td><td>797.92 (n/a)</td><td>465.00 (n/a)</td><td>236.50 (n/a)</td><td>897.94 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 (-12.85%)</td><td>0.03 (-18.13%)</td><td>0.02 <b>(-30.07%)</b></td><td>0.02 (-10.46%)</td><td>0.01 (-6.10%)</td><td>612.60 (+11.69%)</td><td>502.32 <b>(+23.92%)</b></td><td>587.80 <b>(+43.02%)</b></td><td>276.60 (+14.77%)</td><td>143.84 <b>(+25.40%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>548.50 (n/a)</td><td>405.36 (n/a)</td><td>411.00 (n/a)</td><td>241.00 (n/a)</td><td>114.70 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.02 (-1.16%)</td><td>0.01 (-5.12%)</td><td>0.02 (+18.26%)</td><td>0.00 <b>(-72.03%)</b></td><td>0.01 <b>(+84.71%)</b></td><td>1864.90 <b>(+257.47%)</b></td><td>645.68 <b>(+64.46%)</b></td><td>319.30 (-15.44%)</td><td>276.40 (+1.17%)</td><td>684.99 <b>(+618.52%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>521.70 (n/a)</td><td>392.60 (n/a)</td><td>377.60 (n/a)</td><td>273.20 (n/a)</td><td>95.33 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.02 (+2.01%)</td><td>0.02 (-13.35%)</td><td>0.02 <b>(-30.81%)</b></td><td>0.01 <b>(+30.46%)</b></td><td>0.01 (-15.24%)</td><td>583.20 <b>(-23.34%)</b></td><td>392.16 (+5.52%)</td><td>347.60 <b>(+44.53%)</b></td><td>214.30 (-1.97%)</td><td>153.76 <b>(-33.18%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>760.80 (n/a)</td><td>371.66 (n/a)</td><td>240.50 (n/a)</td><td>218.60 (n/a)</td><td>230.10 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.02 <b>(-27.51%)</b></td><td>0.01 <b>(-32.92%)</b></td><td>0.01 <b>(-41.17%)</b></td><td>0.01 (+3.20%)</td><td>0.00 <b>(-30.74%)</b></td><td>631.50 (-3.10%)</td><td>433.36 <b>(+38.54%)</b></td><td>405.20 <b>(+69.97%)</b></td><td>278.60 <b>(+37.99%)</b></td><td>158.24 (-16.78%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>651.70 (n/a)</td><td>312.80 (n/a)</td><td>238.40 (n/a)</td><td>201.90 (n/a)</td><td>190.14 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.02 (-9.24%)</td><td>0.01 (-7.36%)</td><td>0.01 <b>(-24.84%)</b></td><td>0.01 (+5.66%)</td><td>0.01 (-17.81%)</td><td>509.30 (-5.37%)</td><td>384.62 (+3.91%)</td><td>411.60 <b>(+33.03%)</b></td><td>229.60 (+10.17%)</td><td>113.87 (-19.13%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>538.20 (n/a)</td><td>370.16 (n/a)</td><td>309.40 (n/a)</td><td>208.40 (n/a)</td><td>140.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.02 (-1.22%)</td><td>0.02 (+8.80%)</td><td>0.02 (+7.68%)</td><td>0.01 <b>(+35.42%)</b></td><td>0.00 (-16.83%)</td><td>638.40 <b>(-26.15%)</b></td><td>366.00 (-15.02%)</td><td>306.20 (-7.13%)</td><td>267.00 (+1.25%)</td><td>153.48 <b>(-37.90%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>864.50 (n/a)</td><td>430.70 (n/a)</td><td>329.70 (n/a)</td><td>263.70 (n/a)</td><td>247.15 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.02 (-1.86%)</td><td>0.01 (-6.58%)</td><td>0.01 (+5.96%)</td><td>0.00 <b>(-65.44%)</b></td><td>0.01 <b>(+25.26%)</b></td><td>1907.70 <b>(+189.31%)</b></td><td>719.26 <b>(+45.39%)</b></td><td>490.80 (-5.63%)</td><td>302.90 (+1.88%)</td><td>670.57 <b>(+300.41%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>659.40 (n/a)</td><td>494.72 (n/a)</td><td>520.10 (n/a)</td><td>297.30 (n/a)</td><td>167.47 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>590.20 (n/a)</td><td>414.50 (n/a)</td><td>461.30 (n/a)</td><td>250.40 (n/a)</td><td>144.58 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>547.00 (n/a)</td><td>365.98 (n/a)</td><td>307.90 (n/a)</td><td>274.90 (n/a)</td><td>118.29 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1047.10 (n/a)</td><td>518.80 (n/a)</td><td>484.00 (n/a)</td><td>235.00 (n/a)</td><td>320.38 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>775.80 (n/a)</td><td>430.48 (n/a)</td><td>294.20 (n/a)</td><td>270.10 (n/a)</td><td>218.58 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.30 (n/a)</td><td>396.64 (n/a)</td><td>457.70 (n/a)</td><td>238.80 (n/a)</td><td>111.35 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>547.30 (n/a)</td><td>453.00 (n/a)</td><td>460.80 (n/a)</td><td>267.90 (n/a)</td><td>113.91 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>1.18 <b>(+25.75%)</b></td><td>0.77 (+9.01%)</td><td>0.68 (+7.76%)</td><td>0.64 <b>(+24.79%)</b></td><td>0.23 <b>(+29.61%)</b></td><td>720.50 (-19.86%)</td><td>627.78 (-7.89%)</td><td>675.80 (-7.20%)</td><td>389.30 <b>(-20.47%)</b></td><td>137.95 (-17.11%)</td><td>86.20 <b>(+25.75%)</b></td><td>56.40 (+9.01%)</td><td>49.65 (+7.76%)</td><td>46.57 <b>(+24.79%)</b></td><td>16.86 <b>(+29.61%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.94 (n/a)</td><td>0.71 (n/a)</td><td>0.63 (n/a)</td><td>0.51 (n/a)</td><td>0.18 (n/a)</td><td>899.10 (n/a)</td><td>681.58 (n/a)</td><td>728.20 (n/a)</td><td>489.50 (n/a)</td><td>166.43 (n/a)</td><td>68.55 (n/a)</td><td>51.74 (n/a)</td><td>46.08 (n/a)</td><td>37.32 (n/a)</td><td>13.01 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>1.94 <b>(+45.94%)</b></td><td>1.28 <b>(+30.70%)</b></td><td>1.39 <b>(+57.95%)</b></td><td>0.75 (-13.08%)</td><td>0.47 <b>(+141.35%)</b></td><td>869.50 (+15.04%)</td><td>573.56 (-16.25%)</td><td>470.30 <b>(-36.69%)</b></td><td>338.60 <b>(-31.47%)</b></td><td>220.58 <b>(+98.28%)</b></td><td>198.21 <b>(+45.94%)</b></td><td>131.48 <b>(+30.70%)</b></td><td>142.68 <b>(+57.95%)</b></td><td>77.18 (-13.08%)</td><td>48.57 <b>(+141.35%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.33 (n/a)</td><td>0.98 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.20 (n/a)</td><td>755.80 (n/a)</td><td>684.88 (n/a)</td><td>742.90 (n/a)</td><td>494.10 (n/a)</td><td>111.25 (n/a)</td><td>135.82 (n/a)</td><td>100.59 (n/a)</td><td>90.33 (n/a)</td><td>88.80 (n/a)</td><td>20.12 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>1.35 (-6.28%)</td><td>0.98 (-17.93%)</td><td>0.99 (-19.95%)</td><td>0.77 (-14.27%)</td><td>0.23 (+14.30%)</td><td>976.90 (+16.64%)</td><td>803.52 <b>(+23.75%)</b></td><td>763.20 <b>(+24.91%)</b></td><td>559.50 (+6.69%)</td><td>172.17 <b>(+42.72%)</b></td><td>149.93 (-6.28%)</td><td>108.77 (-17.93%)</td><td>109.91 (-19.95%)</td><td>85.87 (-14.27%)</td><td>25.93 (+14.30%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.44 (n/a)</td><td>1.19 (n/a)</td><td>1.23 (n/a)</td><td>0.90 (n/a)</td><td>0.20 (n/a)</td><td>837.50 (n/a)</td><td>649.30 (n/a)</td><td>611.00 (n/a)</td><td>524.40 (n/a)</td><td>120.63 (n/a)</td><td>159.98 (n/a)</td><td>132.53 (n/a)</td><td>137.30 (n/a)</td><td>100.16 (n/a)</td><td>22.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>1.47 (-16.78%)</td><td>0.91 <b>(-25.30%)</b></td><td>0.73 <b>(-37.99%)</b></td><td>0.48 <b>(-45.22%)</b></td><td>0.48 <b>(+31.14%)</b></td><td>2187.30 <b>(+82.53%)</b></td><td>1427.62 <b>(+55.97%)</b></td><td>1433.10 <b>(+61.26%)</b></td><td>712.90 <b>(+20.18%)</b></td><td>690.04 <b>(+175.54%)</b></td><td>188.28 (-16.78%)</td><td>116.95 <b>(-25.30%)</b></td><td>93.66 <b>(-37.99%)</b></td><td>61.36 <b>(-45.22%)</b></td><td>60.81 <b>(+31.14%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.77 (n/a)</td><td>1.22 (n/a)</td><td>1.18 (n/a)</td><td>0.88 (n/a)</td><td>0.36 (n/a)</td><td>1198.30 (n/a)</td><td>915.32 (n/a)</td><td>888.70 (n/a)</td><td>593.20 (n/a)</td><td>250.43 (n/a)</td><td>226.25 (n/a)</td><td>156.57 (n/a)</td><td>151.03 (n/a)</td><td>112.01 (n/a)</td><td>46.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>1.97 (-5.71%)</td><td>1.66 (-1.93%)</td><td>1.68 (-13.35%)</td><td>1.35 <b>(+34.60%)</b></td><td>0.26 <b>(-43.43%)</b></td><td>777.40 <b>(-25.71%)</b></td><td>646.30 (-3.54%)</td><td>623.40 (+15.40%)</td><td>532.00 (+6.06%)</td><td>102.65 <b>(-55.08%)</b></td><td>252.30 (-5.71%)</td><td>211.85 (-1.93%)</td><td>215.28 (-13.35%)</td><td>172.65 <b>(+34.60%)</b></td><td>33.08 <b>(-43.43%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>2.09 (n/a)</td><td>1.69 (n/a)</td><td>1.94 (n/a)</td><td>1.00 (n/a)</td><td>0.46 (n/a)</td><td>1046.40 (n/a)</td><td>670.02 (n/a)</td><td>540.20 (n/a)</td><td>501.60 (n/a)</td><td>228.50 (n/a)</td><td>267.58 (n/a)</td><td>216.02 (n/a)</td><td>248.46 (n/a)</td><td>128.27 (n/a)</td><td>58.47 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>1.40 <b>(-31.46%)</b></td><td>1.01 <b>(-36.48%)</b></td><td>1.13 <b>(-23.91%)</b></td><td>0.30 <b>(-75.81%)</b></td><td>0.44 <b>(+25.59%)</b></td><td>3457.60 <b>(+313.49%)</b></td><td>1416.42 <b>(+107.34%)</b></td><td>926.50 <b>(+31.44%)</b></td><td>746.40 <b>(+45.90%)</b></td><td>1151.51 <b>(+707.36%)</b></td><td>179.83 <b>(-31.46%)</b></td><td>129.52 <b>(-36.48%)</b></td><td>144.87 <b>(-23.91%)</b></td><td>38.82 <b>(-75.81%)</b></td><td>56.08 <b>(+25.59%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>2.05 (n/a)</td><td>1.59 (n/a)</td><td>1.49 (n/a)</td><td>1.25 (n/a)</td><td>0.35 (n/a)</td><td>836.20 (n/a)</td><td>683.14 (n/a)</td><td>704.90 (n/a)</td><td>511.60 (n/a)</td><td>142.63 (n/a)</td><td>262.37 (n/a)</td><td>203.88 (n/a)</td><td>190.40 (n/a)</td><td>160.50 (n/a)</td><td>44.66 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>1.54 (+0.23%)</td><td>1.31 (+8.18%)</td><td>1.41 (+15.97%)</td><td>0.90 (-9.72%)</td><td>0.25 (+19.91%)</td><td>1163.30 (+10.76%)</td><td>832.50 (-6.27%)</td><td>745.50 (-13.78%)</td><td>682.00 (-0.22%)</td><td>193.56 <b>(+37.29%)</b></td><td>196.81 (+0.23%)</td><td>167.09 (+8.18%)</td><td>180.04 (+15.97%)</td><td>115.37 (-9.72%)</td><td>31.80 (+19.91%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.53 (n/a)</td><td>1.21 (n/a)</td><td>1.21 (n/a)</td><td>1.00 (n/a)</td><td>0.21 (n/a)</td><td>1050.30 (n/a)</td><td>888.20 (n/a)</td><td>864.60 (n/a)</td><td>683.50 (n/a)</td><td>140.99 (n/a)</td><td>196.37 (n/a)</td><td>154.45 (n/a)</td><td>155.24 (n/a)</td><td>127.80 (n/a)</td><td>26.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.71 (-18.85%)</td><td>0.64 (+6.14%)</td><td>0.64 (+18.03%)</td><td>0.56 <b>(+42.14%)</b></td><td>0.07 <b>(-63.40%)</b></td><td>640.10 <b>(-29.64%)</b></td><td>570.00 (-11.34%)</td><td>562.60 (-15.27%)</td><td>506.40 <b>(+23.24%)</b></td><td>59.77 <b>(-67.80%)</b></td><td>33.13 (-18.85%)</td><td>29.69 (+6.14%)</td><td>29.82 (+18.03%)</td><td>26.21 <b>(+42.14%)</b></td><td>3.09 <b>(-63.40%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.88 (n/a)</td><td>0.60 (n/a)</td><td>0.54 (n/a)</td><td>0.40 (n/a)</td><td>0.18 (n/a)</td><td>909.80 (n/a)</td><td>642.94 (n/a)</td><td>664.00 (n/a)</td><td>410.90 (n/a)</td><td>185.59 (n/a)</td><td>40.83 (n/a)</td><td>27.98 (n/a)</td><td>25.27 (n/a)</td><td>18.44 (n/a)</td><td>8.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>2.97 (+9.01%)</td><td>1.73 (-10.73%)</td><td>1.22 <b>(-44.13%)</b></td><td>0.75 <b>(-32.39%)</b></td><td>1.13 <b>(+68.07%)</b></td><td>3503.90 <b>(+47.90%)</b></td><td>2158.36 <b>(+42.36%)</b></td><td>2150.10 <b>(+78.98%)</b></td><td>884.10 (-8.27%)</td><td>1271.34 <b>(+113.55%)</b></td><td>607.25 (+9.01%)</td><td>353.83 (-10.73%)</td><td>249.69 <b>(-44.13%)</b></td><td>153.22 <b>(-32.39%)</b></td><td>230.80 <b>(+68.07%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>2.72 (n/a)</td><td>1.94 (n/a)</td><td>2.18 (n/a)</td><td>1.11 (n/a)</td><td>0.67 (n/a)</td><td>2369.10 (n/a)</td><td>1516.18 (n/a)</td><td>1201.30 (n/a)</td><td>963.80 (n/a)</td><td>595.33 (n/a)</td><td>557.05 (n/a)</td><td>396.34 (n/a)</td><td>446.92 (n/a)</td><td>226.62 (n/a)</td><td>137.32 (n/a)</td>
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


### test_gemm_tile_options[tn128-ma32-default]

_No metrics available._


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn16-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn32-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma16-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma32-default]

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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2029.00 (n/a)</td><td>639.62 (n/a)</td><td>302.00 (n/a)</td><td>256.90 (n/a)</td><td>777.30 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.10 (n/a)</td><td>361.04 (n/a)</td><td>393.20 (n/a)</td><td>198.80 (n/a)</td><td>131.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>498.80 (n/a)</td><td>310.36 (n/a)</td><td>264.40 (n/a)</td><td>219.90 (n/a)</td><td>109.55 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>531.70 (n/a)</td><td>421.62 (n/a)</td><td>514.60 (n/a)</td><td>239.80 (n/a)</td><td>140.54 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>775.10 (n/a)</td><td>394.10 (n/a)</td><td>296.90 (n/a)</td><td>237.10 (n/a)</td><td>223.71 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>677.60 (n/a)</td><td>435.86 (n/a)</td><td>383.80 (n/a)</td><td>223.10 (n/a)</td><td>184.60 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.51 (+11.70%)</td><td>0.40 <b>(+36.94%)</b></td><td>0.36 <b>(+29.18%)</b></td><td>0.32 <b>(+143.87%)</b></td><td>0.08 <b>(-31.65%)</b></td><td>695.00 <b>(-58.99%)</b></td><td>571.96 <b>(-36.24%)</b></td><td>614.50 <b>(-22.59%)</b></td><td>434.90 (-10.48%)</td><td>107.83 <b>(-76.84%)</b></td><td>21.70 (+11.70%)</td><td>17.01 <b>(+36.94%)</b></td><td>15.36 <b>(+29.18%)</b></td><td>13.58 <b>(+143.87%)</b></td><td>3.41 <b>(-31.65%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.46 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>1694.80 (n/a)</td><td>897.04 (n/a)</td><td>793.80 (n/a)</td><td>485.80 (n/a)</td><td>465.61 (n/a)</td><td>19.43 (n/a)</td><td>12.42 (n/a)</td><td>11.89 (n/a)</td><td>5.57 (n/a)</td><td>4.99 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.54 (-8.21%)</td><td>0.44 (-1.72%)</td><td>0.45 (+13.46%)</td><td>0.36 (-0.54%)</td><td>0.07 <b>(-36.47%)</b></td><td>619.60 (+0.55%)</td><td>510.70 (-0.51%)</td><td>489.70 (-11.86%)</td><td>412.50 (+8.93%)</td><td>76.50 <b>(-30.64%)</b></td><td>22.88 (-8.21%)</td><td>18.81 (-1.72%)</td><td>19.27 (+13.46%)</td><td>15.23 (-0.54%)</td><td>2.82 <b>(-36.47%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.58 (n/a)</td><td>0.45 (n/a)</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.10 (n/a)</td><td>616.20 (n/a)</td><td>513.32 (n/a)</td><td>555.60 (n/a)</td><td>378.70 (n/a)</td><td>110.29 (n/a)</td><td>24.92 (n/a)</td><td>19.14 (n/a)</td><td>16.98 (n/a)</td><td>15.31 (n/a)</td><td>4.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.31 (+2.06%)</td><td>0.31 (+1.35%)</td><td>0.30 (+0.68%)</td><td>0.30 (+1.23%)</td><td>0.00 <b>(+107.35%)</b></td><td>83139.40 (-1.21%)</td><td>82353.14 (-1.33%)</td><td>82731.40 (-0.68%)</td><td>81438.20 (-2.02%)</td><td>813.61 <b>(+100.24%)</b></td><td>210.96 (+2.06%)</td><td>208.63 (+1.35%)</td><td>207.66 (+0.68%)</td><td>206.64 (+1.23%)</td><td>2.07 <b>(+107.34%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>84159.20 (n/a)</td><td>83462.70 (n/a)</td><td>83295.90 (n/a)</td><td>83117.40 (n/a)</td><td>406.31 (n/a)</td><td>206.69 (n/a)</td><td>205.84 (n/a)</td><td>206.25 (n/a)</td><td>204.14 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>1.15 (-0.22%)</td><td>1.14 (+2.43%)</td><td>1.14 (+2.19%)</td><td>1.12 (+7.46%)</td><td>0.01 <b>(-71.77%)</b></td><td>22457.10 (-6.95%)</td><td>22147.10 (-2.50%)</td><td>22059.70 (-2.14%)</td><td>21911.60 (+0.22%)</td><td>246.75 <b>(-73.62%)</b></td><td>784.05 (-0.22%)</td><td>775.79 (+2.43%)</td><td>778.79 (+2.19%)</td><td>765.01 (+7.46%)</td><td>8.62 <b>(-71.77%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.15 (n/a)</td><td>1.11 (n/a)</td><td>1.12 (n/a)</td><td>1.04 (n/a)</td><td>0.04 (n/a)</td><td>24133.40 (n/a)</td><td>22714.18 (n/a)</td><td>22542.50 (n/a)</td><td>21862.80 (n/a)</td><td>935.29 (n/a)</td><td>785.80 (n/a)</td><td>757.36 (n/a)</td><td>762.11 (n/a)</td><td>711.87 (n/a)</td><td>30.52 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>3.27 (-14.17%)</td><td>2.39 <b>(-20.71%)</b></td><td>2.20 <b>(-37.83%)</b></td><td>1.35 (-3.84%)</td><td>0.78 <b>(-22.61%)</b></td><td>5961.20 (+3.99%)</td><td>3729.06 <b>(+21.16%)</b></td><td>3670.80 <b>(+60.85%)</b></td><td>2464.40 (+16.51%)</td><td>1395.57 (-8.85%)</td><td>857.80 (-14.17%)</td><td>625.79 <b>(-20.71%)</b></td><td>575.88 <b>(-37.83%)</b></td><td>354.62 (-3.84%)</td><td>204.33 <b>(-22.61%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>3.81 (n/a)</td><td>3.01 (n/a)</td><td>3.53 (n/a)</td><td>1.41 (n/a)</td><td>1.01 (n/a)</td><td>5732.30 (n/a)</td><td>3077.74 (n/a)</td><td>2282.10 (n/a)</td><td>2115.20 (n/a)</td><td>1531.08 (n/a)</td><td>999.40 (n/a)</td><td>789.28 (n/a)</td><td>926.32 (n/a)</td><td>368.77 (n/a)</td><td>264.03 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.24 <b>(-26.70%)</b></td><td>0.21 (-2.95%)</td><td>0.20 (+6.07%)</td><td>0.17 (-4.52%)</td><td>0.03 <b>(-50.56%)</b></td><td>7511.00 (+4.73%)</td><td>6133.92 (-0.43%)</td><td>6262.30 (-5.73%)</td><td>5203.70 <b>(+36.42%)</b></td><td>962.16 <b>(-28.39%)</b></td><td>12.90 <b>(-26.70%)</b></td><td>11.15 (-2.95%)</td><td>10.72 (+6.07%)</td><td>8.93 (-4.52%)</td><td>1.70 <b>(-50.56%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.33 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.06 (n/a)</td><td>7171.70 (n/a)</td><td>6160.32 (n/a)</td><td>6642.60 (n/a)</td><td>3814.50 (n/a)</td><td>1343.69 (n/a)</td><td>17.59 (n/a)</td><td>11.49 (n/a)</td><td>10.10 (n/a)</td><td>9.36 (n/a)</td><td>3.44 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>3.86 (n/a)</td><td>3.60 (n/a)</td><td>3.56 (n/a)</td><td>3.35 (n/a)</td><td>0.24 (n/a)</td><td>3.86 (n/a)</td><td>3.60 (n/a)</td><td>3.56 (n/a)</td><td>3.35 (n/a)</td><td>0.24 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>7.66 (+1.94%)</td><td>7.02 (+6.30%)</td><td>7.13 (+9.36%)</td><td>5.83 (-0.58%)</td><td>0.75 <b>(+21.89%)</b></td><td>7.66 (+1.94%)</td><td>7.01 (+6.30%)</td><td>7.12 (+9.36%)</td><td>5.83 (-0.58%)</td><td>0.75 <b>(+21.89%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>7.52 (n/a)</td><td>6.60 (n/a)</td><td>6.52 (n/a)</td><td>5.87 (n/a)</td><td>0.61 (n/a)</td><td>7.51 (n/a)</td><td>6.60 (n/a)</td><td>6.51 (n/a)</td><td>5.86 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>12.91 (+14.38%)</td><td>10.16 (+13.67%)</td><td>9.40 (+10.54%)</td><td>8.16 (+4.55%)</td><td>2.14 <b>(+58.47%)</b></td><td>12.90 (+14.38%)</td><td>10.15 (+13.67%)</td><td>9.40 (+10.54%)</td><td>8.16 (+4.55%)</td><td>2.14 <b>(+58.47%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>11.28 (n/a)</td><td>8.93 (n/a)</td><td>8.51 (n/a)</td><td>7.81 (n/a)</td><td>1.35 (n/a)</td><td>11.28 (n/a)</td><td>8.93 (n/a)</td><td>8.50 (n/a)</td><td>7.80 (n/a)</td><td>1.35 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>3.95 (n/a)</td><td>3.61 (n/a)</td><td>3.64 (n/a)</td><td>3.28 (n/a)</td><td>0.25 (n/a)</td><td>3.95 (n/a)</td><td>3.61 (n/a)</td><td>3.64 (n/a)</td><td>3.28 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>7.55 (+3.13%)</td><td>6.39 (+0.35%)</td><td>6.30 (-4.44%)</td><td>5.72 (+7.02%)</td><td>0.70 <b>(-22.95%)</b></td><td>7.55 (+3.13%)</td><td>6.38 (+0.35%)</td><td>6.30 (-4.44%)</td><td>5.71 (+7.02%)</td><td>0.69 <b>(-22.95%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>7.32 (n/a)</td><td>6.37 (n/a)</td><td>6.59 (n/a)</td><td>5.34 (n/a)</td><td>0.90 (n/a)</td><td>7.32 (n/a)</td><td>6.36 (n/a)</td><td>6.59 (n/a)</td><td>5.34 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>13.71 (-0.60%)</td><td>10.14 (-3.39%)</td><td>8.14 (-11.44%)</td><td>7.76 (-1.48%)</td><td>2.94 (+1.64%)</td><td>13.70 (-0.60%)</td><td>10.13 (-3.39%)</td><td>8.13 (-11.44%)</td><td>7.75 (-1.48%)</td><td>2.94 (+1.64%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>13.79 (n/a)</td><td>10.50 (n/a)</td><td>9.19 (n/a)</td><td>7.87 (n/a)</td><td>2.90 (n/a)</td><td>13.78 (n/a)</td><td>10.49 (n/a)</td><td>9.18 (n/a)</td><td>7.87 (n/a)</td><td>2.89 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>3.12 (+5.03%)</td><td>2.30 (+14.52%)</td><td>2.78 <b>(+63.38%)</b></td><td>1.19 (+16.51%)</td><td>0.84 (+5.75%)</td><td>3.11 (+5.03%)</td><td>2.30 (+14.52%)</td><td>2.78 <b>(+63.38%)</b></td><td>1.19 (+16.51%)</td><td>0.84 (+5.75%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>2.97 (n/a)</td><td>2.01 (n/a)</td><td>1.70 (n/a)</td><td>1.02 (n/a)</td><td>0.80 (n/a)</td><td>2.96 (n/a)</td><td>2.01 (n/a)</td><td>1.70 (n/a)</td><td>1.02 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.52 (-6.63%)</td><td>0.39 (-12.31%)</td><td>0.46 (-12.97%)</td><td>0.08 (-0.05%)</td><td>0.18 (-10.76%)</td><td>0.51 (-6.63%)</td><td>0.38 (-12.31%)</td><td>0.45 (-12.97%)</td><td>0.07 (-0.05%)</td><td>0.18 (-10.76%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.53 (n/a)</td><td>0.08 (n/a)</td><td>0.21 (n/a)</td><td>0.55 (n/a)</td><td>0.44 (n/a)</td><td>0.52 (n/a)</td><td>0.07 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.76 (-1.06%)</td><td>0.61 <b>(+140.80%)</b></td><td>0.66 <b>(+723.58%)</b></td><td>0.36 <b>(+360.44%)</b></td><td>0.15 <b>(-48.17%)</b></td><td>0.75 (-1.06%)</td><td>0.61 <b>(+140.80%)</b></td><td>0.65 <b>(+723.58%)</b></td><td>0.35 <b>(+360.44%)</b></td><td>0.15 <b>(-48.17%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.77 (n/a)</td><td>0.26 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.30 (n/a)</td><td>0.76 (n/a)</td><td>0.25 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>2.43 (-5.00%)</td><td>1.73 <b>(+48.02%)</b></td><td>1.87 <b>(+137.90%)</b></td><td>0.44 (+4.78%)</td><td>0.82 (-10.62%)</td><td>2.40 (-5.00%)</td><td>1.70 <b>(+48.02%)</b></td><td>1.84 <b>(+137.90%)</b></td><td>0.43 (+4.78%)</td><td>0.80 (-10.62%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>2.56 (n/a)</td><td>1.17 (n/a)</td><td>0.79 (n/a)</td><td>0.42 (n/a)</td><td>0.91 (n/a)</td><td>2.52 (n/a)</td><td>1.15 (n/a)</td><td>0.78 (n/a)</td><td>0.41 (n/a)</td><td>0.90 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>521.10 (n/a)</td><td>434.36 (n/a)</td><td>464.10 (n/a)</td><td>299.80 (n/a)</td><td>94.81 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>686.90 (n/a)</td><td>492.80 (n/a)</td><td>507.30 (n/a)</td><td>324.50 (n/a)</td><td>135.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>493.10 (n/a)</td><td>334.32 (n/a)</td><td>281.80 (n/a)</td><td>236.80 (n/a)</td><td>103.31 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>469.80 (n/a)</td><td>361.14 (n/a)</td><td>371.50 (n/a)</td><td>251.70 (n/a)</td><td>97.86 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>562.40 (n/a)</td><td>416.98 (n/a)</td><td>423.70 (n/a)</td><td>226.30 (n/a)</td><td>121.23 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>519.00 (n/a)</td><td>401.34 (n/a)</td><td>456.30 (n/a)</td><td>229.30 (n/a)</td><td>114.81 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 (+0.19%)</td><td>0.02 <b>(-20.50%)</b></td><td>0.03 (-14.39%)</td><td>0.00 <b>(-74.25%)</b></td><td>0.01 <b>(+69.19%)</b></td><td>1845.60 <b>(+288.30%)</b></td><td>617.44 <b>(+110.96%)</b></td><td>287.60 (+16.82%)</td><td>221.40 (-0.18%)</td><td>694.49 <b>(+562.09%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>475.30 (n/a)</td><td>292.68 (n/a)</td><td>246.20 (n/a)</td><td>221.80 (n/a)</td><td>104.89 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (-11.05%)</td><td>0.02 (-1.95%)</td><td>0.03 (+3.50%)</td><td>0.02 (-12.58%)</td><td>0.01 <b>(-23.91%)</b></td><td>539.00 (+14.39%)</td><td>351.82 (-0.16%)</td><td>322.50 (-3.39%)</td><td>266.10 (+12.42%)</td><td>109.92 (-2.34%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>471.20 (n/a)</td><td>352.40 (n/a)</td><td>333.80 (n/a)</td><td>236.70 (n/a)</td><td>112.55 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (-14.21%)</td><td>0.02 <b>(-22.85%)</b></td><td>0.02 <b>(-38.96%)</b></td><td>0.02 (-4.48%)</td><td>0.01 <b>(-35.86%)</b></td><td>534.70 (+4.68%)</td><td>441.08 <b>(+22.80%)</b></td><td>446.00 <b>(+63.85%)</b></td><td>286.50 (+16.56%)</td><td>102.22 <b>(-24.45%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>510.80 (n/a)</td><td>359.18 (n/a)</td><td>272.20 (n/a)</td><td>245.80 (n/a)</td><td>135.30 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 (+12.07%)</td><td>0.03 (+14.61%)</td><td>0.03 <b>(+57.96%)</b></td><td>0.02 (-0.12%)</td><td>0.01 <b>(+28.43%)</b></td><td>447.50 (+0.11%)</td><td>325.76 (-10.02%)</td><td>262.30 <b>(-36.69%)</b></td><td>228.80 (-10.76%)</td><td>111.13 <b>(+22.03%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>447.00 (n/a)</td><td>362.04 (n/a)</td><td>414.30 (n/a)</td><td>256.40 (n/a)</td><td>91.07 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (+0.77%)</td><td>0.02 (-12.59%)</td><td>0.02 <b>(-39.72%)</b></td><td>0.01 (-6.53%)</td><td>0.01 (+3.77%)</td><td>589.70 (+6.98%)</td><td>438.94 (+15.70%)</td><td>491.20 <b>(+65.89%)</b></td><td>250.60 (-0.75%)</td><td>155.38 (+7.63%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>551.20 (n/a)</td><td>379.38 (n/a)</td><td>296.10 (n/a)</td><td>252.50 (n/a)</td><td>144.38 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 <b>(+79.12%)</b></td><td>0.02 <b>(+37.19%)</b></td><td>0.02 (+10.36%)</td><td>0.01 <b>(+43.32%)</b></td><td>0.01 <b>(+98.02%)</b></td><td>738.70 <b>(-30.23%)</b></td><td>487.72 <b>(-25.08%)</b></td><td>498.30 (-9.38%)</td><td>296.90 <b>(-44.17%)</b></td><td>169.65 <b>(-25.71%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1058.80 (n/a)</td><td>651.00 (n/a)</td><td>549.90 (n/a)</td><td>531.80 (n/a)</td><td>228.36 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (-18.25%)</td><td>0.02 <b>(-20.64%)</b></td><td>0.02 (-16.88%)</td><td>0.01 <b>(-29.13%)</b></td><td>0.01 (-4.55%)</td><td>605.10 <b>(+41.11%)</b></td><td>390.84 <b>(+28.84%)</b></td><td>346.20 <b>(+20.29%)</b></td><td>300.90 <b>(+22.32%)</b></td><td>122.69 <b>(+68.07%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>428.80 (n/a)</td><td>303.36 (n/a)</td><td>287.80 (n/a)</td><td>246.00 (n/a)</td><td>73.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 <b>(+27.45%)</b></td><td>0.02 (-4.80%)</td><td>0.02 <b>(-25.18%)</b></td><td>0.01 (-3.22%)</td><td>0.01 <b>(+70.79%)</b></td><td>566.10 (+3.32%)</td><td>441.08 (+13.48%)</td><td>525.10 <b>(+33.65%)</b></td><td>217.50 <b>(-21.54%)</b></td><td>152.58 <b>(+43.53%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>547.90 (n/a)</td><td>388.70 (n/a)</td><td>392.90 (n/a)</td><td>277.20 (n/a)</td><td>106.30 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (+0.66%)</td><td>0.02 (-5.36%)</td><td>0.02 <b>(-30.72%)</b></td><td>0.02 (+8.92%)</td><td>0.01 (+8.14%)</td><td>531.60 (-8.19%)</td><td>379.02 (+5.84%)</td><td>419.40 <b>(+44.32%)</b></td><td>237.90 (-0.67%)</td><td>132.55 (-7.10%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>579.00 (n/a)</td><td>358.10 (n/a)</td><td>290.60 (n/a)</td><td>239.50 (n/a)</td><td>142.69 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 (+6.49%)</td><td>0.02 (-2.00%)</td><td>0.02 (+3.95%)</td><td>0.01 <b>(-22.47%)</b></td><td>0.01 <b>(+23.29%)</b></td><td>640.00 <b>(+28.98%)</b></td><td>420.40 (+11.12%)</td><td>433.10 (-3.80%)</td><td>213.70 (-6.11%)</td><td>197.54 <b>(+46.63%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.20 (n/a)</td><td>378.32 (n/a)</td><td>450.20 (n/a)</td><td>227.60 (n/a)</td><td>134.72 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (-6.06%)</td><td>0.03 (-12.57%)</td><td>0.03 (-10.83%)</td><td>0.02 (+0.74%)</td><td>0.01 (-9.12%)</td><td>493.20 (-0.72%)</td><td>332.12 (+12.87%)</td><td>274.70 (+12.12%)</td><td>239.70 (+6.49%)</td><td>105.93 (-7.38%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>496.80 (n/a)</td><td>294.26 (n/a)</td><td>245.00 (n/a)</td><td>225.10 (n/a)</td><td>114.37 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (+0.30%)</td><td>0.02 <b>(-23.74%)</b></td><td>0.02 <b>(-43.03%)</b></td><td>0.01 (+3.51%)</td><td>0.01 (-5.18%)</td><td>583.80 (-3.39%)</td><td>486.98 <b>(+28.86%)</b></td><td>538.80 <b>(+75.50%)</b></td><td>245.50 (-0.32%)</td><td>137.00 (-11.78%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>604.30 (n/a)</td><td>377.90 (n/a)</td><td>307.00 (n/a)</td><td>246.30 (n/a)</td><td>155.29 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (+2.68%)</td><td>0.03 (+8.49%)</td><td>0.03 (+2.87%)</td><td>0.02 (+18.19%)</td><td>0.01 <b>(-23.12%)</b></td><td>524.10 (-15.39%)</td><td>339.38 (-15.55%)</td><td>268.60 (-2.79%)</td><td>246.00 (-2.61%)</td><td>119.03 <b>(-38.32%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>619.40 (n/a)</td><td>401.86 (n/a)</td><td>276.30 (n/a)</td><td>252.60 (n/a)</td><td>192.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 <b>(+20.42%)</b></td><td>0.02 <b>(+23.04%)</b></td><td>0.02 <b>(+37.67%)</b></td><td>0.02 <b>(+32.09%)</b></td><td>0.01 (+5.65%)</td><td>491.70 <b>(-24.30%)</b></td><td>368.58 <b>(-20.33%)</b></td><td>343.90 <b>(-27.36%)</b></td><td>254.80 (-16.95%)</td><td>98.90 <b>(-30.37%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>649.50 (n/a)</td><td>462.66 (n/a)</td><td>473.40 (n/a)</td><td>306.80 (n/a)</td><td>142.05 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.09 (+4.75%)</td><td>0.08 <b>(+37.34%)</b></td><td>0.08 <b>(+61.34%)</b></td><td>0.08 <b>(+68.76%)</b></td><td>0.00 <b>(-79.70%)</b></td><td>309.10 <b>(-40.74%)</b></td><td>294.28 <b>(-31.08%)</b></td><td>289.50 <b>(-38.02%)</b></td><td>281.00 (-4.52%)</td><td>12.07 <b>(-88.71%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>521.60 (n/a)</td><td>426.98 (n/a)</td><td>467.10 (n/a)</td><td>294.30 (n/a)</td><td>106.85 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.14 (+1.40%)</td><td>0.08 <b>(-30.07%)</b></td><td>0.09 <b>(-33.90%)</b></td><td>0.02 <b>(-72.08%)</b></td><td>0.06 <b>(+100.08%)</b></td><td>1940.50 <b>(+258.09%)</b></td><td>961.38 <b>(+158.35%)</b></td><td>455.90 <b>(+51.26%)</b></td><td>292.30 (-1.38%)</td><td>839.97 <b>(+668.32%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>541.90 (n/a)</td><td>372.12 (n/a)</td><td>301.40 (n/a)</td><td>296.40 (n/a)</td><td>109.33 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.02 (+6.12%)</td><td>0.02 (+7.59%)</td><td>0.02 (-4.33%)</td><td>0.01 (+6.87%)</td><td>0.00 (-16.62%)</td><td>519.70 (-6.41%)</td><td>321.62 (-10.35%)</td><td>293.20 (+4.53%)</td><td>232.30 (-5.76%)</td><td>113.69 (-19.34%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>555.30 (n/a)</td><td>358.74 (n/a)</td><td>280.50 (n/a)</td><td>246.50 (n/a)</td><td>140.95 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (+2.38%)</td><td>0.02 (-14.74%)</td><td>0.03 (+0.73%)</td><td>0.00 <b>(-82.10%)</b></td><td>0.01 <b>(+158.45%)</b></td><td>2044.20 <b>(+458.52%)</b></td><td>637.44 <b>(+118.35%)</b></td><td>297.60 (-0.70%)</td><td>234.70 (-2.33%)</td><td>788.22 <b>(+1445.68%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>366.00 (n/a)</td><td>291.94 (n/a)</td><td>299.70 (n/a)</td><td>240.30 (n/a)</td><td>50.99 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.05 <b>(+22.85%)</b></td><td>0.04 <b>(+32.75%)</b></td><td>0.05 <b>(+58.35%)</b></td><td>0.02 (-5.98%)</td><td>0.01 <b>(+28.52%)</b></td><td>630.20 (+6.36%)</td><td>337.20 <b>(-21.20%)</b></td><td>271.70 <b>(-36.84%)</b></td><td>232.10 (-18.59%)</td><td>165.11 <b>(+23.22%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>592.50 (n/a)</td><td>427.94 (n/a)</td><td>430.20 (n/a)</td><td>285.10 (n/a)</td><td>134.00 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (-2.75%)</td><td>0.02 (-13.22%)</td><td>0.02 <b>(-39.06%)</b></td><td>0.01 <b>(-20.03%)</b></td><td>0.01 (-5.38%)</td><td>748.20 <b>(+25.05%)</b></td><td>457.02 (+15.64%)</td><td>434.10 <b>(+64.12%)</b></td><td>263.40 (+2.81%)</td><td>205.50 (+12.25%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>598.30 (n/a)</td><td>395.20 (n/a)</td><td>264.50 (n/a)</td><td>256.20 (n/a)</td><td>183.07 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (-14.17%)</td><td>0.02 <b>(-24.73%)</b></td><td>0.02 (-17.11%)</td><td>0.00 <b>(-79.15%)</b></td><td>0.01 <b>(+140.10%)</b></td><td>2401.90 <b>(+379.71%)</b></td><td>830.84 <b>(+107.94%)</b></td><td>444.00 <b>(+20.65%)</b></td><td>403.50 (+16.48%)</td><td>878.70 <b>(+1313.34%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>500.70 (n/a)</td><td>399.56 (n/a)</td><td>368.00 (n/a)</td><td>346.40 (n/a)</td><td>62.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 (-17.01%)</td><td>0.03 (+17.52%)</td><td>0.03 (+17.26%)</td><td>0.02 <b>(+421.96%)</b></td><td>0.01 <b>(-63.37%)</b></td><td>369.30 <b>(-80.84%)</b></td><td>275.16 <b>(-55.00%)</b></td><td>265.80 (-14.73%)</td><td>219.20 <b>(+20.51%)</b></td><td>56.99 <b>(-92.30%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1927.40 (n/a)</td><td>611.52 (n/a)</td><td>311.70 (n/a)</td><td>181.90 (n/a)</td><td>740.09 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 (-10.20%)</td><td>0.02 (-16.78%)</td><td>0.02 <b>(-28.62%)</b></td><td>0.02 <b>(+45.96%)</b></td><td>0.01 <b>(-42.64%)</b></td><td>507.20 <b>(-31.49%)</b></td><td>455.06 (+8.43%)</td><td>486.40 <b>(+40.09%)</b></td><td>301.20 (+11.35%)</td><td>86.81 <b>(-55.80%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>740.30 (n/a)</td><td>419.68 (n/a)</td><td>347.20 (n/a)</td><td>270.50 (n/a)</td><td>196.38 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 (+15.35%)</td><td>0.03 <b>(+39.20%)</b></td><td>0.03 <b>(+97.97%)</b></td><td>0.01 <b>(+305.99%)</b></td><td>0.01 (-15.10%)</td><td>597.20 <b>(-75.37%)</b></td><td>346.90 <b>(-56.62%)</b></td><td>265.30 <b>(-49.49%)</b></td><td>212.50 (-13.30%)</td><td>163.49 <b>(-82.21%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2424.40 (n/a)</td><td>799.72 (n/a)</td><td>525.20 (n/a)</td><td>245.10 (n/a)</td><td>919.03 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 <b>(+79.71%)</b></td><td>0.03 <b>(+36.10%)</b></td><td>0.03 <b>(+40.34%)</b></td><td>0.02 (+1.95%)</td><td>0.01 <b>(+244.37%)</b></td><td>577.50 (-1.92%)</td><td>387.24 (-19.84%)</td><td>335.90 <b>(-28.74%)</b></td><td>225.80 <b>(-44.36%)</b></td><td>137.80 <b>(+90.32%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>588.80 (n/a)</td><td>483.08 (n/a)</td><td>471.40 (n/a)</td><td>405.80 (n/a)</td><td>72.41 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 <b>(+25.06%)</b></td><td>0.02 <b>(+36.77%)</b></td><td>0.02 <b>(+61.96%)</b></td><td>0.02 <b>(+54.46%)</b></td><td>0.01 (-9.29%)</td><td>425.60 <b>(-35.26%)</b></td><td>346.64 <b>(-31.48%)</b></td><td>366.50 <b>(-38.26%)</b></td><td>242.20 <b>(-20.04%)</b></td><td>84.48 <b>(-52.18%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>657.40 (n/a)</td><td>505.92 (n/a)</td><td>593.60 (n/a)</td><td>302.90 (n/a)</td><td>176.66 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.04 (+5.70%)</td><td>0.03 <b>(+39.71%)</b></td><td>0.03 <b>(+72.23%)</b></td><td>0.02 (+5.95%)</td><td>0.01 (-11.27%)</td><td>529.10 (-5.62%)</td><td>327.68 <b>(-30.24%)</b></td><td>293.50 <b>(-41.94%)</b></td><td>220.60 (-5.40%)</td><td>118.11 (-12.12%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>560.60 (n/a)</td><td>469.70 (n/a)</td><td>505.50 (n/a)</td><td>233.20 (n/a)</td><td>134.40 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.03 <b>(+53.14%)</b></td><td>0.02 <b>(+27.63%)</b></td><td>0.02 <b>(+21.59%)</b></td><td>0.01 <b>(+46.03%)</b></td><td>0.01 <b>(+36.56%)</b></td><td>1356.00 <b>(-31.52%)</b></td><td>606.96 <b>(-24.96%)</b></td><td>428.60 (-17.75%)</td><td>299.40 <b>(-34.70%)</b></td><td>427.12 <b>(-35.10%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1980.10 (n/a)</td><td>808.86 (n/a)</td><td>521.10 (n/a)</td><td>458.50 (n/a)</td><td>658.11 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.40 (+5.20%)</td><td>0.33 (+4.33%)</td><td>0.37 (+10.97%)</td><td>0.17 <b>(-28.23%)</b></td><td>0.09 <b>(+56.10%)</b></td><td>566.50 <b>(+39.33%)</b></td><td>330.30 (+2.19%)</td><td>265.10 (-9.89%)</td><td>247.90 (-4.95%)</td><td>134.31 <b>(+111.13%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>406.60 (n/a)</td><td>323.22 (n/a)</td><td>294.20 (n/a)</td><td>260.80 (n/a)</td><td>63.62 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.39 (-11.29%)</td><td>0.29 (+7.75%)</td><td>0.33 <b>(+48.66%)</b></td><td>0.17 (-1.95%)</td><td>0.10 (-10.85%)</td><td>595.50 (+1.99%)</td><td>377.84 (-7.81%)</td><td>301.40 <b>(-32.74%)</b></td><td>249.80 (+12.73%)</td><td>150.30 (+3.80%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.44 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>583.90 (n/a)</td><td>409.84 (n/a)</td><td>448.10 (n/a)</td><td>221.60 (n/a)</td><td>144.80 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.46 <b>(+36.77%)</b></td><td>0.30 (+14.87%)</td><td>0.20 <b>(-26.99%)</b></td><td>0.18 (+15.62%)</td><td>0.14 <b>(+87.06%)</b></td><td>556.10 (-13.51%)</td><td>398.24 (-4.46%)</td><td>498.40 <b>(+36.96%)</b></td><td>212.50 <b>(-26.88%)</b></td><td>167.12 (+14.55%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.34 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>643.00 (n/a)</td><td>416.82 (n/a)</td><td>363.90 (n/a)</td><td>290.60 (n/a)</td><td>145.90 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.30 (+6.65%)</td><td>0.20 (+1.92%)</td><td>0.14 <b>(-21.38%)</b></td><td>0.12 (+0.39%)</td><td>0.09 <b>(+21.75%)</b></td><td>614.90 (-0.39%)</td><td>430.48 (+1.70%)</td><td>517.10 <b>(+27.21%)</b></td><td>242.00 (-6.24%)</td><td>170.60 (+8.22%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>617.30 (n/a)</td><td>423.30 (n/a)</td><td>406.50 (n/a)</td><td>258.10 (n/a)</td><td>157.63 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.30 (+6.55%)</td><td>0.23 <b>(+41.85%)</b></td><td>0.29 <b>(+104.37%)</b></td><td>0.12 <b>(+212.07%)</b></td><td>0.09 (-7.50%)</td><td>615.90 <b>(-67.96%)</b></td><td>374.72 <b>(-48.91%)</b></td><td>251.60 <b>(-51.08%)</b></td><td>246.20 (-6.14%)</td><td>175.80 <b>(-74.27%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.28 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>0.10 (n/a)</td><td>1922.10 (n/a)</td><td>733.50 (n/a)</td><td>514.30 (n/a)</td><td>262.30 (n/a)</td><td>683.18 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.25 <b>(-20.11%)</b></td><td>0.15 (-17.96%)</td><td>0.13 (-10.34%)</td><td>0.07 <b>(-48.63%)</b></td><td>0.07 (-11.55%)</td><td>1086.00 <b>(+94.66%)</b></td><td>602.96 <b>(+31.76%)</b></td><td>562.40 (+11.52%)</td><td>295.70 <b>(+25.14%)</b></td><td>295.97 <b>(+131.57%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.31 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>557.90 (n/a)</td><td>457.62 (n/a)</td><td>504.30 (n/a)</td><td>236.30 (n/a)</td><td>127.81 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.51 <b>(+20.64%)</b></td><td>0.33 (+5.89%)</td><td>0.26 (-19.74%)</td><td>0.17 (-19.75%)</td><td>0.15 <b>(+66.10%)</b></td><td>766.30 <b>(+24.60%)</b></td><td>469.14 (+3.95%)</td><td>509.20 <b>(+24.59%)</b></td><td>257.50 (-17.12%)</td><td>207.45 <b>(+56.89%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.42 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>615.00 (n/a)</td><td>451.30 (n/a)</td><td>408.70 (n/a)</td><td>310.70 (n/a)</td><td>132.22 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.37 (-13.91%)</td><td>0.25 (-18.76%)</td><td>0.24 (-4.93%)</td><td>0.19 (-2.00%)</td><td>0.07 <b>(-35.39%)</b></td><td>692.70 (+2.03%)</td><td>553.46 (+17.49%)</td><td>553.70 (+5.19%)</td><td>356.20 (+16.18%)</td><td>129.81 (-19.04%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.43 (n/a)</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>678.90 (n/a)</td><td>471.08 (n/a)</td><td>526.40 (n/a)</td><td>306.60 (n/a)</td><td>160.34 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.50 <b>(+21.94%)</b></td><td>0.30 (+0.34%)</td><td>0.25 (-16.69%)</td><td>0.16 (-7.66%)</td><td>0.14 <b>(+39.14%)</b></td><td>824.40 (+8.30%)</td><td>513.28 (+5.91%)</td><td>532.60 <b>(+20.04%)</b></td><td>264.40 (-17.99%)</td><td>219.79 <b>(+22.72%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.41 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>761.20 (n/a)</td><td>484.66 (n/a)</td><td>443.70 (n/a)</td><td>322.40 (n/a)</td><td>179.10 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.02 (-14.67%)</td><td>0.01 (-7.45%)</td><td>0.01 (-9.96%)</td><td>0.01 <b>(+277.71%)</b></td><td>0.00 <b>(-45.04%)</b></td><td>488.60 <b>(-73.53%)</b></td><td>364.08 <b>(-37.01%)</b></td><td>300.20 (+11.06%)</td><td>272.90 (+17.17%)</td><td>112.15 <b>(-84.18%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1845.60 (n/a)</td><td>578.00 (n/a)</td><td>270.30 (n/a)</td><td>232.90 (n/a)</td><td>708.83 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.02 (-13.58%)</td><td>0.01 (+13.65%)</td><td>0.01 (+10.04%)</td><td>0.01 <b>(+76.73%)</b></td><td>0.00 <b>(-66.32%)</b></td><td>322.40 <b>(-43.41%)</b></td><td>282.50 <b>(-21.88%)</b></td><td>273.60 (-9.10%)</td><td>241.50 (+15.72%)</td><td>31.99 <b>(-78.36%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>569.70 (n/a)</td><td>361.60 (n/a)</td><td>301.00 (n/a)</td><td>208.70 (n/a)</td><td>147.83 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.02 (-0.88%)</td><td>0.01 (-16.02%)</td><td>0.01 (-10.96%)</td><td>0.01 <b>(-40.40%)</b></td><td>0.00 <b>(+45.30%)</b></td><td>657.20 <b>(+67.78%)</b></td><td>406.40 <b>(+31.49%)</b></td><td>307.70 (+12.30%)</td><td>244.70 (+0.87%)</td><td>178.76 <b>(+144.97%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>391.70 (n/a)</td><td>309.08 (n/a)</td><td>274.00 (n/a)</td><td>242.60 (n/a)</td><td>72.98 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.59 <b>(+22.71%)</b></td><td>0.40 <b>(+25.51%)</b></td><td>0.36 (+9.06%)</td><td>0.24 <b>(+258.72%)</b></td><td>0.16 (-5.34%)</td><td>539.70 <b>(-72.12%)</b></td><td>380.34 <b>(-44.72%)</b></td><td>364.20 (-8.29%)</td><td>223.10 (-18.49%)</td><td>147.72 <b>(-79.06%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.48 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>0.17 (n/a)</td><td>1936.10 (n/a)</td><td>688.06 (n/a)</td><td>397.10 (n/a)</td><td>273.70 (n/a)</td><td>705.38 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.62 (+6.10%)</td><td>0.44 (+10.08%)</td><td>0.46 (+3.29%)</td><td>0.22 (-8.51%)</td><td>0.17 <b>(+25.77%)</b></td><td>589.90 (+9.30%)</td><td>344.02 (-4.74%)</td><td>288.00 (-3.19%)</td><td>213.80 (-5.73%)</td><td>157.67 <b>(+22.05%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.58 (n/a)</td><td>0.40 (n/a)</td><td>0.44 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>539.70 (n/a)</td><td>361.14 (n/a)</td><td>297.50 (n/a)</td><td>226.80 (n/a)</td><td>129.19 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.53 (+4.30%)</td><td>0.49 <b>(+20.04%)</b></td><td>0.50 (+7.47%)</td><td>0.41 <b>(+37.61%)</b></td><td>0.05 <b>(-52.75%)</b></td><td>323.30 <b>(-27.33%)</b></td><td>272.40 <b>(-20.47%)</b></td><td>266.50 (-6.95%)</td><td>249.00 (-4.12%)</td><td>29.64 <b>(-67.90%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.51 (n/a)</td><td>0.41 (n/a)</td><td>0.46 (n/a)</td><td>0.30 (n/a)</td><td>0.10 (n/a)</td><td>444.90 (n/a)</td><td>342.50 (n/a)</td><td>286.40 (n/a)</td><td>259.70 (n/a)</td><td>92.33 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.54 (-1.88%)</td><td>0.39 (-17.34%)</td><td>0.32 <b>(-33.52%)</b></td><td>0.27 <b>(-29.10%)</b></td><td>0.12 <b>(+46.66%)</b></td><td>489.80 <b>(+41.03%)</b></td><td>368.52 <b>(+26.87%)</b></td><td>412.60 <b>(+50.42%)</b></td><td>246.10 (+1.90%)</td><td>105.69 <b>(+101.78%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.55 (n/a)</td><td>0.47 (n/a)</td><td>0.48 (n/a)</td><td>0.38 (n/a)</td><td>0.08 (n/a)</td><td>347.30 (n/a)</td><td>290.48 (n/a)</td><td>274.30 (n/a)</td><td>241.50 (n/a)</td><td>52.38 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.55 <b>(+41.49%)</b></td><td>0.43 <b>(+32.80%)</b></td><td>0.45 <b>(+48.18%)</b></td><td>0.22 <b>(-21.89%)</b></td><td>0.13 <b>(+194.18%)</b></td><td>592.70 <b>(+28.04%)</b></td><td>344.32 (-17.44%)</td><td>294.40 <b>(-32.51%)</b></td><td>238.20 <b>(-29.34%)</b></td><td>144.78 <b>(+172.48%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.04 (n/a)</td><td>462.90 (n/a)</td><td>417.06 (n/a)</td><td>436.20 (n/a)</td><td>337.10 (n/a)</td><td>53.13 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.01 <b>(-33.29%)</b></td><td>0.01 <b>(-36.53%)</b></td><td>0.01 <b>(-41.06%)</b></td><td>0.01 <b>(-21.13%)</b></td><td>0.00 <b>(-44.88%)</b></td><td>634.20 <b>(+26.79%)</b></td><td>510.04 <b>(+53.46%)</b></td><td>514.50 <b>(+69.69%)</b></td><td>367.50 <b>(+49.88%)</b></td><td>96.73 (-2.46%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>500.20 (n/a)</td><td>332.36 (n/a)</td><td>303.20 (n/a)</td><td>245.20 (n/a)</td><td>99.17 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.02 (+10.59%)</td><td>0.01 (-6.14%)</td><td>0.01 (+2.83%)</td><td>0.01 (-2.71%)</td><td>0.01 <b>(+40.59%)</b></td><td>530.80 (+2.79%)</td><td>356.92 (+14.17%)</td><td>273.30 (-2.77%)</td><td>211.00 (-9.56%)</td><td>157.96 <b>(+35.72%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>516.40 (n/a)</td><td>312.62 (n/a)</td><td>281.10 (n/a)</td><td>233.30 (n/a)</td><td>116.39 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.00 (+14.29%)</td><td>0.00 <b>(+35.00%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (+2.69%)</td><td>19346.55 (+2.78%)</td><td>9470.15 <b>(-27.83%)</b></td><td>6513.41 <b>(-59.95%)</b></td><td>5343.57 (-12.46%)</td><td>5877.97 (-7.53%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18823.11 (n/a)</td><td>13121.55 (n/a)</td><td>16264.61 (n/a)</td><td>6104.24 (n/a)</td><td>6356.79 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.00 (-14.29%)</td><td>0.00 <b>(-38.46%)</b></td><td>0.00 <b>(-63.64%)</b></td><td>0.00 (+0.00%)</td><td>0.00 (-13.98%)</td><td>21241.29 (+10.60%)</td><td>14999.76 <b>(+57.96%)</b></td><td>18550.14 <b>(+139.00%)</b></td><td>6587.70 (+15.46%)</td><td>6433.49 (+15.29%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>19205.41 (n/a)</td><td>9495.82 (n/a)</td><td>7761.48 (n/a)</td><td>5705.77 (n/a)</td><td>5580.40 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.12 (-5.49%)</td><td>0.09 (-8.34%)</td><td>0.09 (+7.73%)</td><td>0.07 (-6.78%)</td><td>0.02 <b>(-27.66%)</b></td><td>29927.99 (+7.34%)</td><td>24407.20 (+6.62%)</td><td>24677.09 (-7.11%)</td><td>17400.72 (+5.78%)</td><td>4650.25 (-18.73%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>27881.83 (n/a)</td><td>22892.05 (n/a)</td><td>26566.32 (n/a)</td><td>16450.24 (n/a)</td><td>5721.85 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>0.12 (-15.93%)</td><td>0.09 (-7.31%)</td><td>0.09 (+3.31%)</td><td>0.07 (-3.90%)</td><td>0.02 <b>(-41.64%)</b></td><td>30390.27 (+4.05%)</td><td>23301.15 (+3.50%)</td><td>23165.62 (-3.27%)</td><td>18057.11 (+18.87%)</td><td>4720.21 <b>(-26.90%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>29206.82 (n/a)</td><td>22512.77 (n/a)</td><td>23949.87 (n/a)</td><td>15190.10 (n/a)</td><td>6457.60 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:22:48</td><td>0.09 <b>(-41.54%)</b></td><td>0.08 <b>(-26.45%)</b></td><td>0.08 (-5.72%)</td><td>0.07 (+0.28%)</td><td>0.01 <b>(-78.49%)</b></td><td>29471.13 (-0.19%)</td><td>26636.50 <b>(+22.62%)</b></td><td>26497.60 (+5.97%)</td><td>22637.65 <b>(+70.99%)</b></td><td>2927.42 <b>(-61.16%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:13:16</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>29528.24 (n/a)</td><td>21722.14 (n/a)</td><td>25004.94 (n/a)</td><td>13239.53 (n/a)</td><td>7537.48 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>1.35 (-10.67%)</td><td>1.10 (+3.20%)</td><td>1.14 (-19.55%)</td><td>0.66 <b>(+322.78%)</b></td><td>0.28 <b>(-53.34%)</b></td><td>791.90 <b>(-76.35%)</b></td><td>511.58 <b>(-50.17%)</b></td><td>458.50 <b>(+24.29%)</b></td><td>387.60 (+11.96%)</td><td>165.79 <b>(-87.32%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.51 (n/a)</td><td>1.06 (n/a)</td><td>1.42 (n/a)</td><td>0.16 (n/a)</td><td>0.60 (n/a)</td><td>3347.80 (n/a)</td><td>1026.70 (n/a)</td><td>368.90 (n/a)</td><td>346.20 (n/a)</td><td>1307.04 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>2.35 (+3.11%)</td><td>2.00 (+7.91%)</td><td>2.10 <b>(+23.74%)</b></td><td>1.43 (+1.81%)</td><td>0.34 (-11.06%)</td><td>734.20 (-1.78%)</td><td>538.60 (-7.89%)</td><td>499.60 (-19.20%)</td><td>447.10 (-3.02%)</td><td>112.40 (-7.37%)</td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>2.27 (n/a)</td><td>1.86 (n/a)</td><td>1.70 (n/a)</td><td>1.40 (n/a)</td><td>0.39 (n/a)</td><td>747.50 (n/a)</td><td>584.74 (n/a)</td><td>618.30 (n/a)</td><td>461.00 (n/a)</td><td>121.34 (n/a)</td>
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
<td><code>d210f20</code> — 2026-09-29 00:56:18</td><td>1.56 (-9.13%)</td><td>1.25 (+15.45%)</td><td>1.38 (+13.60%)</td><td>0.82 <b>(+280.81%)</b></td><td>0.31 <b>(-47.23%)</b></td><td>636.40 <b>(-73.74%)</b></td><td>444.42 <b>(-46.80%)</b></td><td>380.00 (-11.98%)</td><td>336.00 (+10.06%)</td><td>127.36 <b>(-85.82%)</b></td>
</tr>
<tr>
<td><code>ff0792d</code> — 2026-09-25 03:05:09</td><td>1.72 (n/a)</td><td>1.08 (n/a)</td><td>1.21 (n/a)</td><td>0.22 (n/a)</td><td>0.59 (n/a)</td><td>2423.30 (n/a)</td><td>835.36 (n/a)</td><td>431.70 (n/a)</td><td>305.30 (n/a)</td><td>898.11 (n/a)</td>
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
