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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.05 <b>(-27.07%)</b></td><td>0.04 (-3.02%)</td><td>0.04 (-6.66%)</td><td>0.03 <b>(+141.14%)</b></td><td>0.01 <b>(-55.85%)</b></td><td>440.30 <b>(-58.54%)</b></td><td>325.18 <b>(-26.07%)</b></td><td>274.70 (+7.14%)</td><td>252.20 <b>(+37.14%)</b></td><td>87.13 <b>(-76.05%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>1061.90 (n/a)</td><td>439.84 (n/a)</td><td>256.40 (n/a)</td><td>183.90 (n/a)</td><td>363.80 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 <b>(-30.09%)</b></td><td>0.03 (-12.47%)</td><td>0.03 (+4.72%)</td><td>0.02 (+10.97%)</td><td>0.01 <b>(-56.99%)</b></td><td>493.90 (-9.89%)</td><td>388.18 (+5.55%)</td><td>368.10 (-4.51%)</td><td>304.40 <b>(+43.05%)</b></td><td>74.09 <b>(-42.94%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>548.10 (n/a)</td><td>367.76 (n/a)</td><td>385.50 (n/a)</td><td>212.80 (n/a)</td><td>129.85 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.05 (+0.90%)</td><td>0.03 (-19.87%)</td><td>0.03 <b>(-31.89%)</b></td><td>0.02 (+4.65%)</td><td>0.01 (-7.69%)</td><td>511.00 (-4.45%)</td><td>411.52 <b>(+22.44%)</b></td><td>436.00 <b>(+46.80%)</b></td><td>233.90 (-0.89%)</td><td>105.64 (-15.32%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>534.80 (n/a)</td><td>336.10 (n/a)</td><td>297.00 (n/a)</td><td>236.00 (n/a)</td><td>124.75 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (+17.56%)</td><td>0.01 <b>(-23.44%)</b></td><td>0.01 <b>(-40.08%)</b></td><td>0.01 <b>(-41.50%)</b></td><td>0.01 <b>(+122.63%)</b></td><td>652.10 <b>(+70.93%)</b></td><td>438.44 <b>(+51.18%)</b></td><td>484.40 <b>(+66.92%)</b></td><td>196.40 (-14.94%)</td><td>176.39 <b>(+207.37%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>381.50 (n/a)</td><td>290.02 (n/a)</td><td>290.20 (n/a)</td><td>230.90 (n/a)</td><td>57.39 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (-3.12%)</td><td>0.02 (-1.21%)</td><td>0.02 <b>(+25.15%)</b></td><td>0.01 <b>(-20.57%)</b></td><td>0.01 (+15.47%)</td><td>562.10 <b>(+25.89%)</b></td><td>361.62 (+6.69%)</td><td>280.50 <b>(-20.11%)</b></td><td>224.40 (+3.22%)</td><td>148.50 <b>(+53.22%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>446.50 (n/a)</td><td>338.94 (n/a)</td><td>351.10 (n/a)</td><td>217.40 (n/a)</td><td>96.92 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (-6.45%)</td><td>0.02 (+11.91%)</td><td>0.02 (-0.74%)</td><td>0.01 <b>(+294.24%)</b></td><td>0.01 <b>(-32.30%)</b></td><td>475.60 <b>(-74.63%)</b></td><td>346.50 <b>(-44.43%)</b></td><td>295.80 (+0.75%)</td><td>240.20 (+6.90%)</td><td>118.74 <b>(-83.12%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1875.00 (n/a)</td><td>623.52 (n/a)</td><td>293.60 (n/a)</td><td>224.70 (n/a)</td><td>703.59 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (-3.20%)</td><td>0.02 (+8.52%)</td><td>0.02 <b>(+40.29%)</b></td><td>0.01 (+2.34%)</td><td>0.00 (-19.83%)</td><td>620.60 (-2.28%)</td><td>364.54 (-11.25%)</td><td>304.30 <b>(-28.72%)</b></td><td>244.70 (+3.29%)</td><td>149.71 (-10.02%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>635.10 (n/a)</td><td>410.76 (n/a)</td><td>426.90 (n/a)</td><td>236.90 (n/a)</td><td>166.37 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (-12.10%)</td><td>0.02 (+8.18%)</td><td>0.02 <b>(+47.52%)</b></td><td>0.01 (+1.39%)</td><td>0.00 <b>(-32.89%)</b></td><td>584.00 (-1.37%)</td><td>359.62 (-13.78%)</td><td>313.00 <b>(-32.22%)</b></td><td>245.30 (+13.78%)</td><td>131.33 <b>(-20.39%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>592.10 (n/a)</td><td>417.10 (n/a)</td><td>461.80 (n/a)</td><td>215.60 (n/a)</td><td>164.98 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (-3.71%)</td><td>0.01 (-3.48%)</td><td>0.01 (-9.72%)</td><td>0.01 (-11.03%)</td><td>0.00 (+10.77%)</td><td>627.50 (+12.39%)</td><td>475.78 (+5.79%)</td><td>524.90 (+10.76%)</td><td>308.40 (+3.84%)</td><td>129.85 <b>(+32.32%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>558.30 (n/a)</td><td>449.72 (n/a)</td><td>473.90 (n/a)</td><td>297.00 (n/a)</td><td>98.13 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>288.00 (n/a)</td><td>256.66 (n/a)</td><td>246.60 (n/a)</td><td>225.70 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>271.60 (n/a)</td><td>248.74 (n/a)</td><td>243.20 (n/a)</td><td>238.10 (n/a)</td><td>13.37 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>464.10 (n/a)</td><td>285.48 (n/a)</td><td>248.20 (n/a)</td><td>230.60 (n/a)</td><td>100.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>600.20 (n/a)</td><td>447.82 (n/a)</td><td>389.30 (n/a)</td><td>291.50 (n/a)</td><td>142.22 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>645.60 (n/a)</td><td>439.16 (n/a)</td><td>503.20 (n/a)</td><td>183.00 (n/a)</td><td>193.42 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1961.10 (n/a)</td><td>772.44 (n/a)</td><td>465.90 (n/a)</td><td>333.90 (n/a)</td><td>678.15 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.88 (-1.38%)</td><td>0.70 (+0.44%)</td><td>0.76 (+12.67%)</td><td>0.46 <b>(-24.04%)</b></td><td>0.16 <b>(+42.67%)</b></td><td>987.60 <b>(+31.64%)</b></td><td>691.46 (+2.81%)</td><td>603.50 (-11.25%)</td><td>522.10 (+1.40%)</td><td>185.90 <b>(+97.43%)</b></td><td>64.27 (-1.38%)</td><td>51.04 (+0.44%)</td><td>55.60 (+12.67%)</td><td>33.97 <b>(-24.04%)</b></td><td>11.87 <b>(+42.67%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.89 (n/a)</td><td>0.69 (n/a)</td><td>0.67 (n/a)</td><td>0.61 (n/a)</td><td>0.11 (n/a)</td><td>750.20 (n/a)</td><td>672.56 (n/a)</td><td>680.00 (n/a)</td><td>514.90 (n/a)</td><td>94.16 (n/a)</td><td>65.17 (n/a)</td><td>50.82 (n/a)</td><td>49.34 (n/a)</td><td>44.73 (n/a)</td><td>8.32 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.46 (-8.88%)</td><td>0.89 (-19.76%)</td><td>0.78 (-16.14%)</td><td>0.44 <b>(-34.68%)</b></td><td>0.40 (-3.90%)</td><td>1482.20 <b>(+53.09%)</b></td><td>876.06 <b>(+31.83%)</b></td><td>841.00 (+19.26%)</td><td>449.00 (+9.75%)</td><td>402.25 <b>(+68.40%)</b></td><td>149.47 (-8.88%)</td><td>90.67 (-19.76%)</td><td>79.80 (-16.14%)</td><td>45.28 <b>(-34.68%)</b></td><td>40.93 (-3.90%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.60 (n/a)</td><td>1.10 (n/a)</td><td>0.93 (n/a)</td><td>0.68 (n/a)</td><td>0.42 (n/a)</td><td>968.20 (n/a)</td><td>664.54 (n/a)</td><td>705.20 (n/a)</td><td>409.10 (n/a)</td><td>238.86 (n/a)</td><td>164.04 (n/a)</td><td>113.00 (n/a)</td><td>95.16 (n/a)</td><td>69.32 (n/a)</td><td>42.59 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.30 (-13.06%)</td><td>0.98 (-3.99%)</td><td>0.96 (-1.35%)</td><td>0.57 (-19.19%)</td><td>0.27 (-7.40%)</td><td>1314.50 <b>(+23.74%)</b></td><td>828.00 (+6.07%)</td><td>782.40 (+1.37%)</td><td>581.00 (+15.03%)</td><td>284.78 <b>(+43.11%)</b></td><td>144.38 (-13.06%)</td><td>109.23 (-3.99%)</td><td>107.22 (-1.35%)</td><td>63.82 (-19.19%)</td><td>29.68 (-7.40%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.49 (n/a)</td><td>1.02 (n/a)</td><td>0.98 (n/a)</td><td>0.71 (n/a)</td><td>0.29 (n/a)</td><td>1062.30 (n/a)</td><td>780.60 (n/a)</td><td>771.80 (n/a)</td><td>505.10 (n/a)</td><td>198.99 (n/a)</td><td>166.08 (n/a)</td><td>113.77 (n/a)</td><td>108.69 (n/a)</td><td>78.97 (n/a)</td><td>32.05 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.53 (+2.56%)</td><td>0.88 (-12.76%)</td><td>0.48 <b>(-54.55%)</b></td><td>0.46 (-13.66%)</td><td>0.57 <b>(+27.16%)</b></td><td>2279.10 (+15.83%)</td><td>1614.54 <b>(+30.30%)</b></td><td>2184.70 <b>(+120.01%)</b></td><td>683.20 (-2.50%)</td><td>838.39 <b>(+40.89%)</b></td><td>196.44 (+2.56%)</td><td>113.24 (-12.76%)</td><td>61.44 <b>(-54.55%)</b></td><td>58.89 (-13.66%)</td><td>72.54 <b>(+27.16%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.50 (n/a)</td><td>1.01 (n/a)</td><td>1.06 (n/a)</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>1967.70 (n/a)</td><td>1239.06 (n/a)</td><td>993.00 (n/a)</td><td>700.70 (n/a)</td><td>595.08 (n/a)</td><td>191.54 (n/a)</td><td>129.81 (n/a)</td><td>135.17 (n/a)</td><td>68.21 (n/a)</td><td>57.04 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.79 (-17.78%)</td><td>1.22 <b>(-30.44%)</b></td><td>1.32 <b>(-24.69%)</b></td><td>0.30 <b>(-77.03%)</b></td><td>0.55 <b>(+68.66%)</b></td><td>3537.60 <b>(+335.45%)</b></td><td>1294.98 <b>(+110.27%)</b></td><td>795.60 <b>(+32.80%)</b></td><td>585.10 <b>(+21.64%)</b></td><td>1256.72 <b>(+910.46%)</b></td><td>229.41 (-17.78%)</td><td>156.24 <b>(-30.44%)</b></td><td>168.71 <b>(-24.69%)</b></td><td>37.94 <b>(-77.03%)</b></td><td>70.84 <b>(+68.66%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>2.18 (n/a)</td><td>1.75 (n/a)</td><td>1.75 (n/a)</td><td>1.29 (n/a)</td><td>0.33 (n/a)</td><td>812.40 (n/a)</td><td>615.86 (n/a)</td><td>599.10 (n/a)</td><td>481.00 (n/a)</td><td>124.37 (n/a)</td><td>279.01 (n/a)</td><td>224.60 (n/a)</td><td>224.02 (n/a)</td><td>165.21 (n/a)</td><td>42.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>2.35 (+9.88%)</td><td>1.72 <b>(+20.07%)</b></td><td>1.47 (-11.00%)</td><td>1.30 <b>(+308.43%)</b></td><td>0.49 <b>(-27.80%)</b></td><td>808.50 <b>(-75.52%)</b></td><td>649.50 <b>(-44.23%)</b></td><td>715.60 (+12.36%)</td><td>445.50 (-9.01%)</td><td>170.10 <b>(-85.81%)</b></td><td>301.24 (+9.88%)</td><td>219.80 <b>(+20.07%)</b></td><td>187.56 (-11.00%)</td><td>166.01 <b>(+308.43%)</b></td><td>63.10 <b>(-27.80%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>2.14 (n/a)</td><td>1.43 (n/a)</td><td>1.65 (n/a)</td><td>0.32 (n/a)</td><td>0.68 (n/a)</td><td>3302.10 (n/a)</td><td>1164.58 (n/a)</td><td>636.90 (n/a)</td><td>489.60 (n/a)</td><td>1199.15 (n/a)</td><td>274.15 (n/a)</td><td>183.06 (n/a)</td><td>210.75 (n/a)</td><td>40.65 (n/a)</td><td>87.40 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.26 (-17.85%)</td><td>0.78 <b>(-26.22%)</b></td><td>0.63 <b>(-48.41%)</b></td><td>0.33 <b>(-29.83%)</b></td><td>0.43 (-16.51%)</td><td>3201.20 <b>(+42.50%)</b></td><td>1766.46 <b>(+37.77%)</b></td><td>1657.90 <b>(+93.84%)</b></td><td>829.40 <b>(+21.74%)</b></td><td>998.34 <b>(+34.26%)</b></td><td>161.83 (-17.85%)</td><td>99.36 <b>(-26.22%)</b></td><td>80.96 <b>(-48.41%)</b></td><td>41.93 <b>(-29.83%)</b></td><td>54.80 (-16.51%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.54 (n/a)</td><td>1.05 (n/a)</td><td>1.23 (n/a)</td><td>0.47 (n/a)</td><td>0.51 (n/a)</td><td>2246.40 (n/a)</td><td>1282.22 (n/a)</td><td>855.30 (n/a)</td><td>681.30 (n/a)</td><td>743.57 (n/a)</td><td>197.00 (n/a)</td><td>134.67 (n/a)</td><td>156.93 (n/a)</td><td>59.75 (n/a)</td><td>65.63 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.77 (-6.45%)</td><td>0.61 (-5.79%)</td><td>0.56 (-9.49%)</td><td>0.52 (+17.39%)</td><td>0.11 <b>(-25.15%)</b></td><td>693.50 (-14.81%)</td><td>606.12 (+3.96%)</td><td>640.40 (+10.49%)</td><td>466.20 (+6.90%)</td><td>95.53 <b>(-33.06%)</b></td><td>35.99 (-6.45%)</td><td>28.30 (-5.79%)</td><td>26.20 (-9.49%)</td><td>24.19 (+17.39%)</td><td>4.94 <b>(-25.15%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.83 (n/a)</td><td>0.65 (n/a)</td><td>0.62 (n/a)</td><td>0.44 (n/a)</td><td>0.14 (n/a)</td><td>814.10 (n/a)</td><td>583.02 (n/a)</td><td>579.60 (n/a)</td><td>436.10 (n/a)</td><td>142.71 (n/a)</td><td>38.47 (n/a)</td><td>30.04 (n/a)</td><td>28.94 (n/a)</td><td>20.61 (n/a)</td><td>6.60 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>3.70 (+7.24%)</td><td>2.36 (-16.91%)</td><td>2.28 <b>(-32.29%)</b></td><td>1.12 <b>(+62.71%)</b></td><td>1.23 (+1.79%)</td><td>2333.30 <b>(-38.54%)</b></td><td>1425.98 (+3.35%)</td><td>1150.30 <b>(+47.68%)</b></td><td>708.20 (-6.74%)</td><td>784.31 <b>(-41.95%)</b></td><td>758.13 (+7.24%)</td><td>483.72 (-16.91%)</td><td>466.74 <b>(-32.29%)</b></td><td>230.09 <b>(+62.71%)</b></td><td>251.03 (+1.79%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>3.45 (n/a)</td><td>2.84 (n/a)</td><td>3.37 (n/a)</td><td>0.69 (n/a)</td><td>1.20 (n/a)</td><td>3796.40 (n/a)</td><td>1379.74 (n/a)</td><td>778.90 (n/a)</td><td>759.40 (n/a)</td><td>1351.00 (n/a)</td><td>706.92 (n/a)</td><td>582.18 (n/a)</td><td>689.28 (n/a)</td><td>141.41 (n/a)</td><td>246.61 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>577.60 (n/a)</td><td>447.34 (n/a)</td><td>467.10 (n/a)</td><td>238.10 (n/a)</td><td>126.92 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>422.60 (n/a)</td><td>314.64 (n/a)</td><td>292.00 (n/a)</td><td>267.10 (n/a)</td><td>61.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.50 (n/a)</td><td>364.10 (n/a)</td><td>324.70 (n/a)</td><td>268.40 (n/a)</td><td>100.21 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>637.50 (n/a)</td><td>488.12 (n/a)</td><td>559.80 (n/a)</td><td>210.90 (n/a)</td><td>166.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>585.90 (n/a)</td><td>470.74 (n/a)</td><td>463.30 (n/a)</td><td>356.70 (n/a)</td><td>94.33 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>623.90 (n/a)</td><td>482.26 (n/a)</td><td>498.20 (n/a)</td><td>268.80 (n/a)</td><td>131.39 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.58 (+2.92%)</td><td>0.41 (-6.55%)</td><td>0.46 (+1.03%)</td><td>0.21 <b>(-32.27%)</b></td><td>0.14 <b>(+41.51%)</b></td><td>1037.90 <b>(+47.64%)</b></td><td>610.78 (+15.62%)</td><td>479.70 (-1.03%)</td><td>381.20 (-2.83%)</td><td>262.35 <b>(+107.12%)</b></td><td>24.76 (+2.92%)</td><td>17.45 (-6.55%)</td><td>19.67 (+1.03%)</td><td>9.09 <b>(-32.27%)</b></td><td>6.05 <b>(+41.51%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.46 (n/a)</td><td>0.31 (n/a)</td><td>0.10 (n/a)</td><td>703.00 (n/a)</td><td>528.28 (n/a)</td><td>484.70 (n/a)</td><td>392.30 (n/a)</td><td>126.67 (n/a)</td><td>24.06 (n/a)</td><td>18.67 (n/a)</td><td>19.47 (n/a)</td><td>13.42 (n/a)</td><td>4.28 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.63 (+3.20%)</td><td>0.44 (-18.14%)</td><td>0.43 <b>(-23.41%)</b></td><td>0.32 <b>(-27.43%)</b></td><td>0.11 <b>(+73.59%)</b></td><td>690.10 <b>(+37.80%)</b></td><td>522.84 <b>(+26.50%)</b></td><td>519.60 <b>(+30.59%)</b></td><td>350.30 (-3.10%)</td><td>121.67 <b>(+122.44%)</b></td><td>26.94 (+3.20%)</td><td>18.94 (-18.14%)</td><td>18.16 <b>(-23.41%)</b></td><td>13.67 <b>(-27.43%)</b></td><td>4.90 <b>(+73.59%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.61 (n/a)</td><td>0.54 (n/a)</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.07 (n/a)</td><td>500.80 (n/a)</td><td>413.30 (n/a)</td><td>397.90 (n/a)</td><td>361.50 (n/a)</td><td>54.70 (n/a)</td><td>26.11 (n/a)</td><td>23.13 (n/a)</td><td>23.72 (n/a)</td><td>18.84 (n/a)</td><td>2.82 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.31 (+0.53%)</td><td>0.30 (-0.20%)</td><td>0.30 (-0.22%)</td><td>0.30 (-0.75%)</td><td>0.00 <b>(+77.04%)</b></td><td>84048.60 (+0.75%)</td><td>82756.48 (+0.21%)</td><td>82679.10 (+0.22%)</td><td>81369.10 (-0.53%)</td><td>1217.14 <b>(+77.64%)</b></td><td>211.14 (+0.53%)</td><td>207.63 (-0.20%)</td><td>207.79 (-0.22%)</td><td>204.40 (-0.75%)</td><td>3.05 <b>(+77.04%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.00 (n/a)</td><td>83420.40 (n/a)</td><td>82579.82 (n/a)</td><td>82494.80 (n/a)</td><td>81799.20 (n/a)</td><td>685.16 (n/a)</td><td>210.02 (n/a)</td><td>208.05 (n/a)</td><td>208.25 (n/a)</td><td>205.94 (n/a)</td><td>1.72 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.15 (+0.18%)</td><td>1.14 (+1.32%)</td><td>1.15 (+0.66%)</td><td>1.11 (+3.31%)</td><td>0.02 <b>(-42.51%)</b></td><td>22773.10 (-3.21%)</td><td>22119.70 (-1.35%)</td><td>21961.30 (-0.65%)</td><td>21922.80 (-0.18%)</td><td>366.11 <b>(-44.41%)</b></td><td>783.65 (+0.18%)</td><td>776.84 (+1.32%)</td><td>782.28 (+0.66%)</td><td>754.39 (+3.31%)</td><td>12.58 <b>(-42.51%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.15 (n/a)</td><td>1.12 (n/a)</td><td>1.14 (n/a)</td><td>1.07 (n/a)</td><td>0.03 (n/a)</td><td>23527.20 (n/a)</td><td>22422.14 (n/a)</td><td>22105.30 (n/a)</td><td>21963.20 (n/a)</td><td>658.54 (n/a)</td><td>782.21 (n/a)</td><td>766.72 (n/a)</td><td>777.18 (n/a)</td><td>730.21 (n/a)</td><td>21.89 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>4.17 (+1.49%)</td><td>2.79 (+18.04%)</td><td>2.49 <b>(+27.71%)</b></td><td>1.42 (-19.91%)</td><td>1.20 <b>(+22.98%)</b></td><td>5694.80 <b>(+24.86%)</b></td><td>3398.16 (-9.17%)</td><td>3233.50 <b>(-21.70%)</b></td><td>1935.20 (-1.47%)</td><td>1555.34 <b>(+52.24%)</b></td><td>1092.36 (+1.49%)</td><td>732.57 (+18.04%)</td><td>653.76 <b>(+27.71%)</b></td><td>371.20 (-19.91%)</td><td>315.19 <b>(+22.98%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>4.10 (n/a)</td><td>2.37 (n/a)</td><td>1.95 (n/a)</td><td>1.77 (n/a)</td><td>0.98 (n/a)</td><td>4561.10 (n/a)</td><td>3741.14 (n/a)</td><td>4129.40 (n/a)</td><td>1964.10 (n/a)</td><td>1021.61 (n/a)</td><td>1076.29 (n/a)</td><td>620.60 (n/a)</td><td>511.92 (n/a)</td><td>463.47 (n/a)</td><td>256.29 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.23 <b>(-26.32%)</b></td><td>0.20 (-17.43%)</td><td>0.20 (-8.11%)</td><td>0.16 <b>(-21.80%)</b></td><td>0.03 <b>(-42.05%)</b></td><td>7955.80 <b>(+27.88%)</b></td><td>6433.74 (+19.79%)</td><td>6263.90 (+8.82%)</td><td>5361.10 <b>(+35.73%)</b></td><td>952.44 (+3.31%)</td><td>12.52 <b>(-26.32%)</b></td><td>10.60 (-17.43%)</td><td>10.71 (-8.11%)</td><td>8.44 <b>(-21.80%)</b></td><td>1.47 <b>(-42.05%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.32 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>6221.40 (n/a)</td><td>5370.78 (n/a)</td><td>5756.20 (n/a)</td><td>3949.80 (n/a)</td><td>921.92 (n/a)</td><td>16.99 (n/a)</td><td>12.84 (n/a)</td><td>11.66 (n/a)</td><td>10.79 (n/a)</td><td>2.54 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>3.73 (n/a)</td><td>3.58 (n/a)</td><td>3.61 (n/a)</td><td>3.44 (n/a)</td><td>0.12 (n/a)</td><td>3.73 (n/a)</td><td>3.57 (n/a)</td><td>3.60 (n/a)</td><td>3.44 (n/a)</td><td>0.12 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>6.28 (-14.70%)</td><td>5.70 (-10.92%)</td><td>5.73 (-6.44%)</td><td>5.05 (-10.75%)</td><td>0.44 <b>(-37.44%)</b></td><td>6.27 (-14.70%)</td><td>5.70 (-10.92%)</td><td>5.73 (-6.44%)</td><td>5.05 (-10.75%)</td><td>0.43 <b>(-37.44%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>7.36 (n/a)</td><td>6.40 (n/a)</td><td>6.12 (n/a)</td><td>5.66 (n/a)</td><td>0.70 (n/a)</td><td>7.35 (n/a)</td><td>6.40 (n/a)</td><td>6.12 (n/a)</td><td>5.65 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>13.33 (-5.04%)</td><td>8.57 (-11.93%)</td><td>7.44 (-14.04%)</td><td>7.02 (-7.61%)</td><td>2.67 (+6.02%)</td><td>13.32 (-5.04%)</td><td>8.56 (-11.93%)</td><td>7.44 (-14.04%)</td><td>7.02 (-7.61%)</td><td>2.67 (+6.02%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>14.04 (n/a)</td><td>9.73 (n/a)</td><td>8.66 (n/a)</td><td>7.60 (n/a)</td><td>2.52 (n/a)</td><td>14.03 (n/a)</td><td>9.72 (n/a)</td><td>8.66 (n/a)</td><td>7.60 (n/a)</td><td>2.52 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>3.81 (n/a)</td><td>3.66 (n/a)</td><td>3.74 (n/a)</td><td>3.36 (n/a)</td><td>0.19 (n/a)</td><td>3.81 (n/a)</td><td>3.66 (n/a)</td><td>3.74 (n/a)</td><td>3.36 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>7.55 (-0.22%)</td><td>6.17 (-6.14%)</td><td>5.91 (-12.09%)</td><td>5.67 (-3.41%)</td><td>0.78 (+8.41%)</td><td>7.54 (-0.22%)</td><td>6.17 (-6.14%)</td><td>5.90 (-12.09%)</td><td>5.67 (-3.41%)</td><td>0.78 (+8.41%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>7.56 (n/a)</td><td>6.57 (n/a)</td><td>6.72 (n/a)</td><td>5.87 (n/a)</td><td>0.72 (n/a)</td><td>7.56 (n/a)</td><td>6.57 (n/a)</td><td>6.71 (n/a)</td><td>5.87 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>13.90 (+6.85%)</td><td>11.57 (+15.00%)</td><td>12.30 <b>(+28.27%)</b></td><td>9.11 (+5.61%)</td><td>1.90 (+9.81%)</td><td>13.89 (+6.85%)</td><td>11.56 (+15.00%)</td><td>12.30 <b>(+28.27%)</b></td><td>9.10 (+5.61%)</td><td>1.90 (+9.81%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>13.01 (n/a)</td><td>10.06 (n/a)</td><td>9.59 (n/a)</td><td>8.62 (n/a)</td><td>1.73 (n/a)</td><td>13.00 (n/a)</td><td>10.05 (n/a)</td><td>9.59 (n/a)</td><td>8.62 (n/a)</td><td>1.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>2.92 (-5.83%)</td><td>1.75 <b>(-31.00%)</b></td><td>1.15 <b>(-59.89%)</b></td><td>0.98 <b>(-44.31%)</b></td><td>0.96 <b>(+50.88%)</b></td><td>2.91 (-5.83%)</td><td>1.74 <b>(-31.00%)</b></td><td>1.15 <b>(-59.89%)</b></td><td>0.98 <b>(-44.31%)</b></td><td>0.96 <b>(+50.88%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>3.10 (n/a)</td><td>2.53 (n/a)</td><td>2.87 (n/a)</td><td>1.77 (n/a)</td><td>0.64 (n/a)</td><td>3.09 (n/a)</td><td>2.52 (n/a)</td><td>2.86 (n/a)</td><td>1.76 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.56 (-12.46%)</td><td>0.43 (+14.86%)</td><td>0.54 <b>(+21.20%)</b></td><td>0.13 (-4.39%)</td><td>0.18 (-18.43%)</td><td>0.55 (-12.46%)</td><td>0.42 (+14.86%)</td><td>0.53 <b>(+21.20%)</b></td><td>0.13 (-4.39%)</td><td>0.18 (-18.43%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.64 (n/a)</td><td>0.38 (n/a)</td><td>0.45 (n/a)</td><td>0.14 (n/a)</td><td>0.23 (n/a)</td><td>0.63 (n/a)</td><td>0.37 (n/a)</td><td>0.44 (n/a)</td><td>0.14 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.75 (-8.24%)</td><td>0.51 (+6.55%)</td><td>0.47 <b>(-25.38%)</b></td><td>0.29 <b>(+279.60%)</b></td><td>0.20 <b>(-46.24%)</b></td><td>0.74 (-8.24%)</td><td>0.50 (+6.55%)</td><td>0.47 <b>(-25.38%)</b></td><td>0.28 <b>(+279.60%)</b></td><td>0.20 <b>(-46.24%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.81 (n/a)</td><td>0.48 (n/a)</td><td>0.63 (n/a)</td><td>0.08 (n/a)</td><td>0.37 (n/a)</td><td>0.80 (n/a)</td><td>0.47 (n/a)</td><td>0.62 (n/a)</td><td>0.07 (n/a)</td><td>0.37 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>2.45 (-8.15%)</td><td>1.86 (+5.06%)</td><td>2.22 (-7.61%)</td><td>0.43 (-2.97%)</td><td>0.83 (-19.91%)</td><td>2.41 (-8.15%)</td><td>1.83 (+5.06%)</td><td>2.18 (-7.61%)</td><td>0.43 (-2.97%)</td><td>0.82 (-19.91%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>2.67 (n/a)</td><td>1.77 (n/a)</td><td>2.40 (n/a)</td><td>0.45 (n/a)</td><td>1.04 (n/a)</td><td>2.63 (n/a)</td><td>1.74 (n/a)</td><td>2.36 (n/a)</td><td>0.44 (n/a)</td><td>1.03 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>462.90 (n/a)</td><td>325.90 (n/a)</td><td>247.10 (n/a)</td><td>241.00 (n/a)</td><td>111.69 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>559.90 (n/a)</td><td>402.62 (n/a)</td><td>468.00 (n/a)</td><td>237.30 (n/a)</td><td>150.31 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>500.80 (n/a)</td><td>440.52 (n/a)</td><td>412.10 (n/a)</td><td>392.90 (n/a)</td><td>52.51 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>566.70 (n/a)</td><td>404.92 (n/a)</td><td>430.40 (n/a)</td><td>253.80 (n/a)</td><td>137.73 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>653.00 (n/a)</td><td>451.18 (n/a)</td><td>458.10 (n/a)</td><td>243.50 (n/a)</td><td>145.27 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>525.70 (n/a)</td><td>419.14 (n/a)</td><td>492.40 (n/a)</td><td>235.70 (n/a)</td><td>130.96 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (-5.33%)</td><td>0.02 <b>(-20.78%)</b></td><td>0.02 <b>(-24.55%)</b></td><td>0.01 <b>(-21.58%)</b></td><td>0.01 (-0.13%)</td><td>631.40 <b>(+27.53%)</b></td><td>448.96 <b>(+28.45%)</b></td><td>467.10 <b>(+32.55%)</b></td><td>275.20 (+5.64%)</td><td>129.51 <b>(+35.40%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>495.10 (n/a)</td><td>349.52 (n/a)</td><td>352.40 (n/a)</td><td>260.50 (n/a)</td><td>95.65 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (+15.52%)</td><td>0.03 (+18.01%)</td><td>0.03 (+4.58%)</td><td>0.02 <b>(+86.38%)</b></td><td>0.01 <b>(-29.36%)</b></td><td>423.40 <b>(-46.35%)</b></td><td>306.12 <b>(-24.58%)</b></td><td>291.10 (-4.37%)</td><td>235.90 (-13.43%)</td><td>71.31 <b>(-67.33%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>789.20 (n/a)</td><td>405.88 (n/a)</td><td>304.40 (n/a)</td><td>272.50 (n/a)</td><td>218.25 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (-11.77%)</td><td>0.03 (-1.99%)</td><td>0.03 (-11.09%)</td><td>0.03 <b>(+51.13%)</b></td><td>0.00 <b>(-67.20%)</b></td><td>316.50 <b>(-33.84%)</b></td><td>294.00 (-3.73%)</td><td>297.30 (+12.44%)</td><td>268.10 (+13.31%)</td><td>23.24 <b>(-76.48%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>478.40 (n/a)</td><td>305.40 (n/a)</td><td>264.40 (n/a)</td><td>236.60 (n/a)</td><td>98.80 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (+19.08%)</td><td>0.02 (+5.86%)</td><td>0.02 (-11.63%)</td><td>0.01 <b>(+28.06%)</b></td><td>0.01 (+17.11%)</td><td>553.00 <b>(-21.91%)</b></td><td>381.82 (-6.61%)</td><td>427.20 (+13.17%)</td><td>220.20 (-16.05%)</td><td>136.67 <b>(-24.37%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>708.20 (n/a)</td><td>408.84 (n/a)</td><td>377.50 (n/a)</td><td>262.30 (n/a)</td><td>180.70 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 <b>(-28.50%)</b></td><td>0.03 (+0.02%)</td><td>0.02 (+18.63%)</td><td>0.02 <b>(+41.11%)</b></td><td>0.01 <b>(-47.33%)</b></td><td>451.80 <b>(-29.13%)</b></td><td>352.74 (-16.96%)</td><td>406.60 (-15.70%)</td><td>229.40 <b>(+39.88%)</b></td><td>104.81 <b>(-49.41%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>637.50 (n/a)</td><td>424.78 (n/a)</td><td>482.30 (n/a)</td><td>164.00 (n/a)</td><td>207.18 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.05 <b>(+63.10%)</b></td><td>0.03 (+11.02%)</td><td>0.02 (-6.11%)</td><td>0.01 (-9.42%)</td><td>0.02 <b>(+99.19%)</b></td><td>599.90 (+10.40%)</td><td>429.30 (+5.75%)</td><td>504.30 (+6.50%)</td><td>149.60 <b>(-38.66%)</b></td><td>194.65 <b>(+39.90%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>543.40 (n/a)</td><td>405.94 (n/a)</td><td>473.50 (n/a)</td><td>243.90 (n/a)</td><td>139.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (+10.83%)</td><td>0.02 <b>(+22.57%)</b></td><td>0.03 <b>(+53.76%)</b></td><td>0.02 <b>(+268.51%)</b></td><td>0.01 <b>(-26.58%)</b></td><td>505.40 <b>(-72.86%)</b></td><td>364.04 <b>(-46.14%)</b></td><td>315.40 <b>(-34.96%)</b></td><td>217.50 (-9.79%)</td><td>125.42 <b>(-81.42%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>1862.40 (n/a)</td><td>675.90 (n/a)</td><td>484.90 (n/a)</td><td>241.10 (n/a)</td><td>675.03 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (-1.09%)</td><td>0.02 (-2.00%)</td><td>0.02 (-0.24%)</td><td>0.01 (-5.18%)</td><td>0.01 (-10.52%)</td><td>634.10 (+5.45%)</td><td>433.28 (-0.24%)</td><td>456.70 (+0.24%)</td><td>250.00 (+1.09%)</td><td>144.35 (-8.02%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>601.30 (n/a)</td><td>434.34 (n/a)</td><td>455.60 (n/a)</td><td>247.30 (n/a)</td><td>156.93 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (-10.80%)</td><td>0.02 (+2.28%)</td><td>0.03 (+14.72%)</td><td>0.02 (+11.61%)</td><td>0.01 (-19.99%)</td><td>484.50 (-10.39%)</td><td>344.60 (-4.64%)</td><td>294.00 (-12.84%)</td><td>280.40 (+12.07%)</td><td>88.06 <b>(-22.18%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>540.70 (n/a)</td><td>361.38 (n/a)</td><td>337.30 (n/a)</td><td>250.20 (n/a)</td><td>113.16 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (+3.93%)</td><td>0.01 <b>(-26.34%)</b></td><td>0.01 <b>(-27.46%)</b></td><td>0.00 <b>(-73.77%)</b></td><td>0.01 <b>(+119.62%)</b></td><td>2026.60 <b>(+281.15%)</b></td><td>831.20 <b>(+96.17%)</b></td><td>558.70 <b>(+37.85%)</b></td><td>307.00 (-3.76%)</td><td>691.82 <b>(+769.23%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>531.70 (n/a)</td><td>423.72 (n/a)</td><td>405.30 (n/a)</td><td>319.00 (n/a)</td><td>79.59 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 <b>(-25.49%)</b></td><td>0.03 (-3.69%)</td><td>0.03 (-12.51%)</td><td>0.03 <b>(+31.35%)</b></td><td>0.00 <b>(-81.34%)</b></td><td>294.90 <b>(-23.88%)</b></td><td>282.84 (-3.09%)</td><td>292.70 (+14.29%)</td><td>261.40 <b>(+34.19%)</b></td><td>15.70 <b>(-81.94%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>387.40 (n/a)</td><td>291.86 (n/a)</td><td>256.10 (n/a)</td><td>194.80 (n/a)</td><td>86.91 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (+11.83%)</td><td>0.03 (+4.59%)</td><td>0.02 <b>(-22.96%)</b></td><td>0.01 (+3.13%)</td><td>0.01 <b>(+25.90%)</b></td><td>595.20 (-3.03%)</td><td>396.24 (+0.23%)</td><td>415.30 <b>(+29.78%)</b></td><td>186.90 (-10.57%)</td><td>179.87 (+5.21%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>613.80 (n/a)</td><td>395.32 (n/a)</td><td>320.00 (n/a)</td><td>209.00 (n/a)</td><td>170.95 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 <b>(-35.44%)</b></td><td>0.02 (-8.77%)</td><td>0.02 (-5.73%)</td><td>0.01 <b>(+239.02%)</b></td><td>0.01 <b>(-64.30%)</b></td><td>548.20 <b>(-70.50%)</b></td><td>414.78 <b>(-37.12%)</b></td><td>429.20 (+6.08%)</td><td>287.80 <b>(+54.90%)</b></td><td>104.94 <b>(-84.74%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>0.02 (n/a)</td><td>1858.40 (n/a)</td><td>659.62 (n/a)</td><td>404.60 (n/a)</td><td>185.80 (n/a)</td><td>687.76 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (-1.26%)</td><td>0.02 (-14.84%)</td><td>0.01 (-11.16%)</td><td>0.01 <b>(-20.68%)</b></td><td>0.01 (+4.16%)</td><td>646.00 <b>(+26.07%)</b></td><td>513.18 (+19.77%)</td><td>546.40 (+12.54%)</td><td>318.80 (+1.27%)</td><td>140.05 <b>(+36.49%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>512.40 (n/a)</td><td>428.48 (n/a)</td><td>485.50 (n/a)</td><td>314.80 (n/a)</td><td>102.61 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.11 <b>(+23.06%)</b></td><td>0.08 (+8.41%)</td><td>0.09 (+5.99%)</td><td>0.05 (-8.05%)</td><td>0.02 <b>(+52.70%)</b></td><td>512.70 (+8.76%)</td><td>314.04 (-3.99%)</td><td>278.70 (-5.65%)</td><td>223.50 (-18.73%)</td><td>113.56 <b>(+39.82%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>471.40 (n/a)</td><td>327.08 (n/a)</td><td>295.40 (n/a)</td><td>275.00 (n/a)</td><td>81.22 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.16 (-18.64%)</td><td>0.10 <b>(-21.61%)</b></td><td>0.08 <b>(-40.15%)</b></td><td>0.08 <b>(+51.53%)</b></td><td>0.04 <b>(-42.05%)</b></td><td>519.10 <b>(-34.01%)</b></td><td>441.70 (+7.56%)</td><td>484.90 <b>(+67.09%)</b></td><td>252.60 <b>(+22.92%)</b></td><td>110.20 <b>(-54.74%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>786.60 (n/a)</td><td>410.64 (n/a)</td><td>290.20 (n/a)</td><td>205.50 (n/a)</td><td>243.46 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (-3.15%)</td><td>0.02 <b>(-20.48%)</b></td><td>0.02 <b>(-28.02%)</b></td><td>0.01 <b>(-44.00%)</b></td><td>0.01 <b>(+115.91%)</b></td><td>556.70 <b>(+78.54%)</b></td><td>359.26 <b>(+40.23%)</b></td><td>338.30 <b>(+38.93%)</b></td><td>220.70 (+3.28%)</td><td>142.61 <b>(+279.65%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>311.80 (n/a)</td><td>256.20 (n/a)</td><td>243.50 (n/a)</td><td>213.70 (n/a)</td><td>37.56 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (-6.26%)</td><td>0.02 (+7.65%)</td><td>0.02 (-0.41%)</td><td>0.02 (+19.60%)</td><td>0.01 (-11.48%)</td><td>519.50 (-16.40%)</td><td>414.50 (-9.59%)</td><td>500.00 (+0.40%)</td><td>246.90 (+6.65%)</td><td>129.61 (-15.59%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>621.40 (n/a)</td><td>458.48 (n/a)</td><td>498.00 (n/a)</td><td>231.50 (n/a)</td><td>153.53 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.06 (+18.82%)</td><td>0.04 (-1.55%)</td><td>0.04 <b>(+24.49%)</b></td><td>0.01 <b>(-73.99%)</b></td><td>0.02 <b>(+89.45%)</b></td><td>1923.50 <b>(+284.47%)</b></td><td>624.14 <b>(+73.27%)</b></td><td>300.70 (-19.68%)</td><td>208.80 (-15.84%)</td><td>729.11 <b>(+629.12%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>500.30 (n/a)</td><td>360.22 (n/a)</td><td>374.40 (n/a)</td><td>248.10 (n/a)</td><td>100.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (-1.67%)</td><td>0.02 (-2.61%)</td><td>0.02 (+4.23%)</td><td>0.02 (-1.39%)</td><td>0.01 (-5.87%)</td><td>512.00 (+1.41%)</td><td>376.34 (+2.26%)</td><td>356.00 (-4.07%)</td><td>251.50 (+1.70%)</td><td>109.58 (+0.32%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>504.90 (n/a)</td><td>368.02 (n/a)</td><td>371.10 (n/a)</td><td>247.30 (n/a)</td><td>109.22 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (+0.46%)</td><td>0.03 (+0.75%)</td><td>0.03 <b>(+33.80%)</b></td><td>0.02 (+7.04%)</td><td>0.01 (-16.96%)</td><td>536.80 (-6.58%)</td><td>389.64 (-4.53%)</td><td>340.80 <b>(-25.26%)</b></td><td>238.00 (-0.46%)</td><td>124.14 (-17.10%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>574.60 (n/a)</td><td>408.12 (n/a)</td><td>456.00 (n/a)</td><td>239.10 (n/a)</td><td>149.74 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (+3.31%)</td><td>0.02 (-2.32%)</td><td>0.02 (+1.81%)</td><td>0.01 (-8.96%)</td><td>0.01 (+7.86%)</td><td>555.50 (+9.85%)</td><td>422.14 (+3.91%)</td><td>462.40 (-1.76%)</td><td>264.70 (-3.22%)</td><td>127.58 (+14.53%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>505.70 (n/a)</td><td>406.26 (n/a)</td><td>470.70 (n/a)</td><td>273.50 (n/a)</td><td>111.39 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 <b>(+24.69%)</b></td><td>0.02 (+17.36%)</td><td>0.02 (+8.16%)</td><td>0.02 <b>(+76.26%)</b></td><td>0.00 (-16.80%)</td><td>602.20 <b>(-43.27%)</b></td><td>485.80 <b>(-20.16%)</b></td><td>460.50 (-7.55%)</td><td>376.20 (-19.80%)</td><td>95.60 <b>(-62.50%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>1061.50 (n/a)</td><td>608.48 (n/a)</td><td>498.10 (n/a)</td><td>469.10 (n/a)</td><td>254.89 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (+2.50%)</td><td>0.02 (-16.19%)</td><td>0.02 (-3.56%)</td><td>0.01 <b>(-36.98%)</b></td><td>0.01 (-2.60%)</td><td>981.40 <b>(+58.70%)</b></td><td>525.68 <b>(+26.36%)</b></td><td>475.00 (+3.69%)</td><td>233.60 (-2.42%)</td><td>276.81 <b>(+64.41%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>618.40 (n/a)</td><td>416.02 (n/a)</td><td>458.10 (n/a)</td><td>239.40 (n/a)</td><td>168.36 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (+19.24%)</td><td>0.02 (-12.81%)</td><td>0.02 <b>(-38.01%)</b></td><td>0.01 <b>(+273.76%)</b></td><td>0.01 (-7.24%)</td><td>617.80 <b>(-73.25%)</b></td><td>497.74 <b>(-30.39%)</b></td><td>545.30 <b>(+61.33%)</b></td><td>226.10 (-16.14%)</td><td>155.69 <b>(-82.54%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2309.20 (n/a)</td><td>715.04 (n/a)</td><td>338.00 (n/a)</td><td>269.60 (n/a)</td><td>891.76 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.04 (-12.10%)</td><td>0.02 <b>(-21.64%)</b></td><td>0.01 (-19.58%)</td><td>0.01 (-1.99%)</td><td>0.01 <b>(-21.53%)</b></td><td>640.20 (+2.02%)</td><td>509.36 <b>(+21.22%)</b></td><td>583.00 <b>(+24.33%)</b></td><td>233.80 (+13.77%)</td><td>170.09 (-8.55%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>627.50 (n/a)</td><td>420.18 (n/a)</td><td>468.90 (n/a)</td><td>205.50 (n/a)</td><td>186.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (-10.53%)</td><td>0.02 (-4.15%)</td><td>0.02 (+5.82%)</td><td>0.02 (+4.34%)</td><td>0.01 <b>(-20.60%)</b></td><td>604.00 (-4.16%)</td><td>522.14 (+0.77%)</td><td>578.70 (-5.50%)</td><td>294.80 (+11.75%)</td><td>130.33 (-16.53%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>630.20 (n/a)</td><td>518.14 (n/a)</td><td>612.40 (n/a)</td><td>263.80 (n/a)</td><td>156.14 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.03 (-1.50%)</td><td>0.02 (-13.91%)</td><td>0.02 (-19.51%)</td><td>0.01 (+2.74%)</td><td>0.01 (-0.20%)</td><td>577.70 (-2.66%)</td><td>456.92 (+15.61%)</td><td>485.20 <b>(+24.25%)</b></td><td>236.40 (+1.50%)</td><td>131.43 (-6.64%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>593.50 (n/a)</td><td>395.24 (n/a)</td><td>390.50 (n/a)</td><td>232.90 (n/a)</td><td>140.78 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.37 (-7.11%)</td><td>0.30 (-2.43%)</td><td>0.31 (-15.92%)</td><td>0.23 <b>(+20.32%)</b></td><td>0.06 <b>(-45.94%)</b></td><td>436.90 (-16.89%)</td><td>340.34 (-5.62%)</td><td>318.90 (+18.95%)</td><td>268.00 (+7.63%)</td><td>67.96 <b>(-51.72%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.37 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>525.70 (n/a)</td><td>360.60 (n/a)</td><td>268.10 (n/a)</td><td>249.00 (n/a)</td><td>140.75 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.39 (-4.11%)</td><td>0.30 (+8.60%)</td><td>0.32 <b>(+38.42%)</b></td><td>0.20 (+9.89%)</td><td>0.08 (-15.02%)</td><td>490.50 (-9.00%)</td><td>347.44 (-10.08%)</td><td>305.30 <b>(-27.76%)</b></td><td>254.50 (+4.30%)</td><td>99.81 (-16.94%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.40 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>539.00 (n/a)</td><td>386.38 (n/a)</td><td>422.60 (n/a)</td><td>244.00 (n/a)</td><td>120.17 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.37 (-9.35%)</td><td>0.26 (-6.89%)</td><td>0.25 (-19.14%)</td><td>0.18 (+9.01%)</td><td>0.09 (-18.51%)</td><td>558.40 (-8.26%)</td><td>416.30 (+3.14%)</td><td>391.30 <b>(+23.67%)</b></td><td>266.50 (+10.31%)</td><td>135.99 (-17.65%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.41 (n/a)</td><td>0.28 (n/a)</td><td>0.31 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>608.70 (n/a)</td><td>403.64 (n/a)</td><td>316.40 (n/a)</td><td>241.60 (n/a)</td><td>165.13 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.29 (+9.76%)</td><td>0.23 <b>(+22.09%)</b></td><td>0.24 <b>(+51.11%)</b></td><td>0.16 (+18.44%)</td><td>0.06 (+5.71%)</td><td>447.30 (-15.57%)</td><td>345.32 (-18.59%)</td><td>303.10 <b>(-33.82%)</b></td><td>252.80 (-8.87%)</td><td>91.70 (-15.60%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>529.80 (n/a)</td><td>424.16 (n/a)</td><td>458.00 (n/a)</td><td>277.40 (n/a)</td><td>108.65 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.31 <b>(-28.04%)</b></td><td>0.20 (-0.17%)</td><td>0.16 (+10.01%)</td><td>0.14 (+5.13%)</td><td>0.07 <b>(-43.23%)</b></td><td>516.30 (-4.88%)</td><td>402.00 (-9.67%)</td><td>470.50 (-9.10%)</td><td>238.80 <b>(+39.00%)</b></td><td>122.98 <b>(-21.50%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.43 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>542.80 (n/a)</td><td>445.04 (n/a)</td><td>517.60 (n/a)</td><td>171.80 (n/a)</td><td>156.66 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.30 (+18.56%)</td><td>0.21 <b>(+26.21%)</b></td><td>0.18 <b>(+30.15%)</b></td><td>0.15 (+15.96%)</td><td>0.07 <b>(+29.14%)</b></td><td>486.80 (-13.76%)</td><td>382.56 (-19.57%)</td><td>410.40 <b>(-23.17%)</b></td><td>245.80 (-15.65%)</td><td>110.18 (-2.79%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.05 (n/a)</td><td>564.50 (n/a)</td><td>475.66 (n/a)</td><td>534.20 (n/a)</td><td>291.40 (n/a)</td><td>113.34 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.55 (+6.75%)</td><td>0.36 (-3.92%)</td><td>0.35 (-12.41%)</td><td>0.25 (-4.73%)</td><td>0.12 (+11.09%)</td><td>529.20 (+4.96%)</td><td>394.60 (+4.99%)</td><td>369.40 (+14.15%)</td><td>237.50 (-6.35%)</td><td>114.23 (+3.58%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.52 (n/a)</td><td>0.37 (n/a)</td><td>0.41 (n/a)</td><td>0.26 (n/a)</td><td>0.11 (n/a)</td><td>504.20 (n/a)</td><td>375.86 (n/a)</td><td>323.60 (n/a)</td><td>253.60 (n/a)</td><td>110.28 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.31 <b>(-25.21%)</b></td><td>0.20 <b>(-39.93%)</b></td><td>0.23 <b>(-34.28%)</b></td><td>0.09 <b>(-57.83%)</b></td><td>0.09 (+0.88%)</td><td>1513.70 <b>(+137.15%)</b></td><td>825.48 <b>(+91.64%)</b></td><td>578.20 <b>(+52.16%)</b></td><td>427.60 <b>(+33.71%)</b></td><td>450.82 <b>(+235.32%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.21 (n/a)</td><td>0.09 (n/a)</td><td>638.30 (n/a)</td><td>430.74 (n/a)</td><td>380.00 (n/a)</td><td>319.80 (n/a)</td><td>134.44 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.39 <b>(-34.99%)</b></td><td>0.26 <b>(-28.61%)</b></td><td>0.23 <b>(-39.29%)</b></td><td>0.21 (+6.14%)</td><td>0.07 <b>(-52.57%)</b></td><td>625.50 (-5.78%)</td><td>519.96 <b>(+27.48%)</b></td><td>561.60 <b>(+64.74%)</b></td><td>336.00 <b>(+53.85%)</b></td><td>113.84 <b>(-34.46%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.60 (n/a)</td><td>0.37 (n/a)</td><td>0.38 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>663.90 (n/a)</td><td>407.86 (n/a)</td><td>340.90 (n/a)</td><td>218.40 (n/a)</td><td>173.69 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.01 <b>(-20.38%)</b></td><td>0.01 <b>(-22.46%)</b></td><td>0.01 <b>(-27.30%)</b></td><td>0.01 (-18.69%)</td><td>0.00 (-17.27%)</td><td>717.40 <b>(+22.99%)</b></td><td>419.08 <b>(+28.73%)</b></td><td>371.10 <b>(+37.55%)</b></td><td>285.60 <b>(+25.59%)</b></td><td>176.73 <b>(+20.56%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>583.30 (n/a)</td><td>325.56 (n/a)</td><td>269.80 (n/a)</td><td>227.40 (n/a)</td><td>146.59 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (-8.20%)</td><td>0.02 <b>(+23.82%)</b></td><td>0.02 <b>(+74.74%)</b></td><td>0.01 (+11.99%)</td><td>0.00 <b>(-25.02%)</b></td><td>467.40 (-10.72%)</td><td>291.64 <b>(-24.09%)</b></td><td>236.30 <b>(-42.77%)</b></td><td>229.50 (+8.97%)</td><td>102.04 <b>(-29.85%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>523.50 (n/a)</td><td>384.20 (n/a)</td><td>412.90 (n/a)</td><td>210.60 (n/a)</td><td>145.47 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.01 (-8.78%)</td><td>0.01 (-3.82%)</td><td>0.01 (+17.99%)</td><td>0.01 <b>(-23.52%)</b></td><td>0.00 <b>(+41.61%)</b></td><td>567.90 <b>(+30.76%)</b></td><td>404.70 (+8.53%)</td><td>326.50 (-15.24%)</td><td>308.40 (+9.59%)</td><td>122.06 <b>(+101.27%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>434.30 (n/a)</td><td>372.90 (n/a)</td><td>385.20 (n/a)</td><td>281.40 (n/a)</td><td>60.64 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.50 (-16.10%)</td><td>0.45 (-0.38%)</td><td>0.44 (-8.64%)</td><td>0.43 <b>(+41.91%)</b></td><td>0.03 <b>(-71.00%)</b></td><td>306.60 <b>(-29.53%)</b></td><td>291.86 (-4.01%)</td><td>303.50 (+9.45%)</td><td>266.00 (+19.18%)</td><td>18.91 <b>(-76.28%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.59 (n/a)</td><td>0.46 (n/a)</td><td>0.48 (n/a)</td><td>0.30 (n/a)</td><td>0.10 (n/a)</td><td>435.10 (n/a)</td><td>304.06 (n/a)</td><td>277.30 (n/a)</td><td>223.20 (n/a)</td><td>79.74 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.55 (-3.65%)</td><td>0.44 (-11.53%)</td><td>0.45 (-11.62%)</td><td>0.32 <b>(-22.02%)</b></td><td>0.08 <b>(+36.30%)</b></td><td>417.10 <b>(+28.26%)</b></td><td>308.28 (+15.24%)</td><td>294.40 (+13.19%)</td><td>238.90 (+3.78%)</td><td>65.57 <b>(+84.48%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.57 (n/a)</td><td>0.50 (n/a)</td><td>0.51 (n/a)</td><td>0.41 (n/a)</td><td>0.06 (n/a)</td><td>325.20 (n/a)</td><td>267.52 (n/a)</td><td>260.10 (n/a)</td><td>230.20 (n/a)</td><td>35.54 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.54 (+3.81%)</td><td>0.43 (-0.39%)</td><td>0.44 (-4.41%)</td><td>0.27 (+8.72%)</td><td>0.10 (-7.99%)</td><td>489.70 (-8.02%)</td><td>325.16 (-1.30%)</td><td>301.30 (+4.62%)</td><td>246.40 (-3.67%)</td><td>95.04 (-17.36%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.52 (n/a)</td><td>0.43 (n/a)</td><td>0.46 (n/a)</td><td>0.25 (n/a)</td><td>0.11 (n/a)</td><td>532.40 (n/a)</td><td>329.44 (n/a)</td><td>288.00 (n/a)</td><td>255.80 (n/a)</td><td>115.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.54 (+0.86%)</td><td>0.49 (+3.11%)</td><td>0.49 (+3.91%)</td><td>0.44 (+5.29%)</td><td>0.04 (+4.64%)</td><td>300.90 (-5.02%)</td><td>271.10 (-3.00%)</td><td>270.10 (-3.74%)</td><td>245.40 (-0.85%)</td><td>24.74 (-2.45%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.53 (n/a)</td><td>0.48 (n/a)</td><td>0.47 (n/a)</td><td>0.42 (n/a)</td><td>0.04 (n/a)</td><td>316.80 (n/a)</td><td>279.48 (n/a)</td><td>280.60 (n/a)</td><td>247.50 (n/a)</td><td>25.37 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.48 (-6.41%)</td><td>0.37 (-11.95%)</td><td>0.35 <b>(-21.47%)</b></td><td>0.31 <b>(+26.91%)</b></td><td>0.07 <b>(-34.78%)</b></td><td>420.90 <b>(-21.19%)</b></td><td>364.34 (+8.64%)</td><td>376.60 <b>(+27.36%)</b></td><td>274.00 (+6.82%)</td><td>58.80 <b>(-48.11%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.52 (n/a)</td><td>0.42 (n/a)</td><td>0.45 (n/a)</td><td>0.25 (n/a)</td><td>0.10 (n/a)</td><td>534.10 (n/a)</td><td>335.36 (n/a)</td><td>295.70 (n/a)</td><td>256.50 (n/a)</td><td>113.30 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.02 (-8.58%)</td><td>0.01 <b>(-20.87%)</b></td><td>0.01 <b>(-30.36%)</b></td><td>0.01 <b>(-27.61%)</b></td><td>0.00 <b>(+48.91%)</b></td><td>432.60 <b>(+38.17%)</b></td><td>355.86 <b>(+30.88%)</b></td><td>395.20 <b>(+43.60%)</b></td><td>242.80 (+9.37%)</td><td>82.96 <b>(+127.55%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>313.10 (n/a)</td><td>271.90 (n/a)</td><td>275.20 (n/a)</td><td>222.00 (n/a)</td><td>36.46 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.01 (-5.40%)</td><td>0.01 (+10.17%)</td><td>0.01 <b>(+20.27%)</b></td><td>0.01 <b>(+260.68%)</b></td><td>0.00 <b>(-53.93%)</b></td><td>574.20 <b>(-72.28%)</b></td><td>418.32 <b>(-45.21%)</b></td><td>411.20 (-16.85%)</td><td>277.20 (+5.72%)</td><td>105.26 <b>(-86.06%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>0.01 (n/a)</td><td>2071.10 (n/a)</td><td>763.46 (n/a)</td><td>494.50 (n/a)</td><td>262.20 (n/a)</td><td>755.20 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.00 (+16.67%)</td><td>0.00 <b>(+50.00%)</b></td><td>0.00 <b>(+100.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+57.53%)</b></td><td>22239.00 <b>(+20.81%)</b></td><td>11881.83 (-15.04%)</td><td>6941.04 <b>(-52.30%)</b></td><td>5751.93 (-10.48%)</td><td>7952.67 <b>(+64.43%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>18407.49 (n/a)</td><td>13984.87 (n/a)</td><td>14552.73 (n/a)</td><td>6425.42 (n/a)</td><td>4836.44 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.00 <b>(+100.00%)</b></td><td>0.00 <b>(+40.91%)</b></td><td>0.00 <b>(+25.00%)</b></td><td>0.00 (+0.00%)</td><td>0.00 <b>(+389.90%)</b></td><td>23135.54 (+11.74%)</td><td>15150.23 (-18.91%)</td><td>15276.17 (-17.55%)</td><td>8482.60 <b>(-50.80%)</b></td><td>6105.11 <b>(+380.96%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>20704.30 (n/a)</td><td>18683.58 (n/a)</td><td>18527.49 (n/a)</td><td>17241.90 (n/a)</td><td>1269.36 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>0.15 (+11.02%)</td><td>0.09 (-1.37%)</td><td>0.08 (-9.79%)</td><td>0.07 (-13.62%)</td><td>0.03 <b>(+40.83%)</b></td><td>31491.52 (+15.70%)</td><td>24760.08 (+5.72%)</td><td>26791.93 (+10.90%)</td><td>13879.13 (-9.90%)</td><td>6865.51 <b>(+45.33%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>27217.70 (n/a)</td><td>23420.31 (n/a)</td><td>24158.90 (n/a)</td><td>15404.63 (n/a)</td><td>4724.11 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>1.12 <b>(-24.89%)</b></td><td>0.44 <b>(-64.62%)</b></td><td>0.16 <b>(-89.04%)</b></td><td>0.16 <b>(-79.55%)</b></td><td>0.42 <b>(+21.57%)</b></td><td>3315.40 <b>(+389.00%)</b></td><td>2243.12 <b>(+389.12%)</b></td><td>3230.40 <b>(+812.03%)</b></td><td>467.50 <b>(+33.12%)</b></td><td>1432.60 <b>(+848.75%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.49 (n/a)</td><td>1.23 (n/a)</td><td>1.48 (n/a)</td><td>0.77 (n/a)</td><td>0.35 (n/a)</td><td>678.00 (n/a)</td><td>458.60 (n/a)</td><td>354.20 (n/a)</td><td>351.20 (n/a)</td><td>151.00 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>3.34 <b>(+29.10%)</b></td><td>2.15 (+7.74%)</td><td>2.21 (-8.84%)</td><td>1.04 (+3.51%)</td><td>0.96 <b>(+33.79%)</b></td><td>1003.90 (-3.39%)</td><td>586.70 (-2.65%)</td><td>473.60 (+9.68%)</td><td>314.20 <b>(-22.53%)</b></td><td>290.67 (+5.27%)</td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>2.59 (n/a)</td><td>2.00 (n/a)</td><td>2.43 (n/a)</td><td>1.01 (n/a)</td><td>0.71 (n/a)</td><td>1039.10 (n/a)</td><td>602.64 (n/a)</td><td>431.80 (n/a)</td><td>405.60 (n/a)</td><td>276.13 (n/a)</td>
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
<td><code>d603ab9</code> — 2026-09-18 19:59:49</td><td>2.06 <b>(+22.04%)</b></td><td>1.31 <b>(+22.88%)</b></td><td>1.21 <b>(+22.78%)</b></td><td>0.67 <b>(+137.51%)</b></td><td>0.58 (+1.57%)</td><td>777.50 <b>(-57.90%)</b></td><td>472.58 <b>(-35.46%)</b></td><td>432.40 (-18.55%)</td><td>254.60 (-18.06%)</td><td>216.63 <b>(-66.03%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 15:51:03</td><td>1.69 (n/a)</td><td>1.07 (n/a)</td><td>0.99 (n/a)</td><td>0.28 (n/a)</td><td>0.57 (n/a)</td><td>1846.70 (n/a)</td><td>732.18 (n/a)</td><td>530.90 (n/a)</td><td>310.70 (n/a)</td><td>637.80 (n/a)</td>
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
