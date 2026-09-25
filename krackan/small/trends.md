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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.10 (+11.92%)</td><td>0.08 (+8.40%)</td><td>0.08 (+12.90%)</td><td>0.06 (-15.12%)</td><td>0.02 <b>(+89.42%)</b></td><td>221.40 (+17.83%)</td><td>164.04 (-4.32%)</td><td>161.20 (-11.43%)</td><td>121.70 (-10.58%)</td><td>41.43 <b>(+98.03%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>187.90 (n/a)</td><td>171.44 (n/a)</td><td>182.00 (n/a)</td><td>136.10 (n/a)</td><td>20.92 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.09 <b>(+33.43%)</b></td><td>0.07 (+16.09%)</td><td>0.07 (+1.01%)</td><td>0.06 (+9.91%)</td><td>0.01 <b>(+78.87%)</b></td><td>203.50 (-9.03%)</td><td>172.00 (-12.76%)</td><td>182.30 (-0.98%)</td><td>131.30 <b>(-25.06%)</b></td><td>28.65 (+18.59%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>197.16 (n/a)</td><td>184.10 (n/a)</td><td>175.20 (n/a)</td><td>24.16 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.10 <b>(+51.75%)</b></td><td>0.07 (+16.55%)</td><td>0.06 (+14.60%)</td><td>0.05 (+3.05%)</td><td>0.02 <b>(+160.44%)</b></td><td>257.00 (-2.95%)</td><td>195.98 (-10.17%)</td><td>192.80 (-12.76%)</td><td>121.40 <b>(-34.13%)</b></td><td>49.30 <b>(+58.74%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>264.80 (n/a)</td><td>218.16 (n/a)</td><td>221.00 (n/a)</td><td>184.30 (n/a)</td><td>31.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.08 (+7.54%)</td><td>0.06 (+2.92%)</td><td>0.07 <b>(+21.18%)</b></td><td>0.04 (-18.22%)</td><td>0.01 <b>(+59.66%)</b></td><td>286.90 <b>(+22.29%)</b></td><td>205.16 (+0.42%)</td><td>179.40 (-17.48%)</td><td>152.00 (-7.03%)</td><td>53.99 <b>(+85.62%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>234.60 (n/a)</td><td>204.30 (n/a)</td><td>217.40 (n/a)</td><td>163.50 (n/a)</td><td>29.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (+18.10%)</td><td>0.03 (+8.23%)</td><td>0.03 (+1.50%)</td><td>0.03 (+16.72%)</td><td>0.01 <b>(+20.95%)</b></td><td>204.30 (-14.34%)</td><td>178.16 (-7.43%)</td><td>193.60 (-1.48%)</td><td>137.30 (-15.35%)</td><td>28.43 (-9.73%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>238.50 (n/a)</td><td>192.46 (n/a)</td><td>196.50 (n/a)</td><td>162.20 (n/a)</td><td>31.49 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (-5.66%)</td><td>0.03 (-10.76%)</td><td>0.03 (-16.17%)</td><td>0.03 (-9.77%)</td><td>0.01 (+15.38%)</td><td>207.60 (+10.84%)</td><td>184.62 (+13.17%)</td><td>201.30 (+19.32%)</td><td>137.50 (+6.01%)</td><td>30.74 <b>(+39.89%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>187.30 (n/a)</td><td>163.14 (n/a)</td><td>168.70 (n/a)</td><td>129.70 (n/a)</td><td>21.98 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 <b>(+29.75%)</b></td><td>0.03 (+4.55%)</td><td>0.03 (-9.60%)</td><td>0.02 (-19.28%)</td><td>0.01 <b>(+445.52%)</b></td><td>237.30 <b>(+23.92%)</b></td><td>181.00 (+0.82%)</td><td>197.40 (+10.59%)</td><td>128.60 <b>(-22.95%)</b></td><td>45.88 <b>(+404.79%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>191.50 (n/a)</td><td>179.52 (n/a)</td><td>178.50 (n/a)</td><td>166.90 (n/a)</td><td>9.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (+10.77%)</td><td>0.03 (-2.08%)</td><td>0.03 (-10.89%)</td><td>0.02 (-6.95%)</td><td>0.01 <b>(+83.61%)</b></td><td>243.70 (+7.45%)</td><td>196.24 (+4.23%)</td><td>205.00 (+12.21%)</td><td>155.50 (-9.75%)</td><td>37.71 <b>(+70.00%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.80 (n/a)</td><td>188.28 (n/a)</td><td>182.70 (n/a)</td><td>172.30 (n/a)</td><td>22.18 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 <b>(+30.49%)</b></td><td>0.03 (+2.29%)</td><td>0.03 (-0.83%)</td><td>0.02 (-15.10%)</td><td>0.01 <b>(+190.85%)</b></td><td>251.80 (+17.77%)</td><td>191.16 (+4.53%)</td><td>184.30 (+0.82%)</td><td>120.40 <b>(-23.41%)</b></td><td>56.86 <b>(+171.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.80 (n/a)</td><td>182.88 (n/a)</td><td>182.80 (n/a)</td><td>157.20 (n/a)</td><td>20.92 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (+0.26%)</td><td>0.02 (-14.73%)</td><td>0.02 <b>(-24.70%)</b></td><td>0.02 (-12.92%)</td><td>0.01 <b>(+35.09%)</b></td><td>320.20 (+14.81%)</td><td>256.08 <b>(+21.06%)</b></td><td>271.00 <b>(+32.78%)</b></td><td>160.40 (-0.25%)</td><td>65.01 <b>(+51.68%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>278.90 (n/a)</td><td>211.54 (n/a)</td><td>204.10 (n/a)</td><td>160.80 (n/a)</td><td>42.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 <b>(-26.48%)</b></td><td>0.03 (-18.44%)</td><td>0.03 <b>(-25.56%)</b></td><td>0.02 (-9.01%)</td><td>0.00 <b>(-47.12%)</b></td><td>249.40 (+9.92%)</td><td>204.16 (+18.18%)</td><td>209.10 <b>(+34.30%)</b></td><td>154.20 <b>(+35.98%)</b></td><td>35.34 <b>(-24.32%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.90 (n/a)</td><td>172.76 (n/a)</td><td>155.70 (n/a)</td><td>113.40 (n/a)</td><td>46.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 <b>(+28.29%)</b></td><td>0.02 (+1.51%)</td><td>0.02 (-14.86%)</td><td>0.02 (+10.36%)</td><td>0.01 <b>(+81.65%)</b></td><td>272.80 (-9.40%)</td><td>241.40 (+0.68%)</td><td>263.60 (+17.47%)</td><td>161.70 <b>(-22.03%)</b></td><td>46.69 <b>(+24.92%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>301.10 (n/a)</td><td>239.78 (n/a)</td><td>224.40 (n/a)</td><td>207.40 (n/a)</td><td>37.37 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>215.90 (n/a)</td><td>182.62 (n/a)</td><td>181.60 (n/a)</td><td>144.50 (n/a)</td><td>27.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>244.00 (n/a)</td><td>188.56 (n/a)</td><td>186.00 (n/a)</td><td>118.40 (n/a)</td><td>51.41 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>256.80 (n/a)</td><td>195.08 (n/a)</td><td>200.30 (n/a)</td><td>137.40 (n/a)</td><td>43.78 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>270.80 (n/a)</td><td>216.46 (n/a)</td><td>203.00 (n/a)</td><td>182.60 (n/a)</td><td>35.52 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.50 (n/a)</td><td>162.70 (n/a)</td><td>167.10 (n/a)</td><td>135.50 (n/a)</td><td>18.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.10 (n/a)</td><td>171.82 (n/a)</td><td>167.90 (n/a)</td><td>151.00 (n/a)</td><td>23.85 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>180.90 (n/a)</td><td>166.56 (n/a)</td><td>168.90 (n/a)</td><td>149.50 (n/a)</td><td>11.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>291.70 (n/a)</td><td>215.40 (n/a)</td><td>184.00 (n/a)</td><td>145.70 (n/a)</td><td>62.90 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/flm/dequant</summary>


### test_gate_up_interleaved_blob[iter0]

_No metrics available._


### test_gate_up_interleaved_blob[iter1]

_No metrics available._


### test_gate_up_interleaved_blob[iter2]

_No metrics available._


### test_gate_up_interleaved_blob[iter3]

_No metrics available._


### test_gate_up_interleaved_blob[iter4]

_No metrics available._


### test_large_k_shapes[K_4096-N_1536]

_No metrics available._


### test_large_k_shapes[K_6144-N_1536]

_No metrics available._


### test_matches_reference[K_1024-N_128]

_No metrics available._


### test_matches_reference[K_1024-N_512]

_No metrics available._


### test_matches_reference[K_1536-N_640]

_No metrics available._


### test_matches_reference[K_2048-N_256]

_No metrics available._


### test_one_xclbin_serves_every_shape[iter0]

_No metrics available._


### test_one_xclbin_serves_every_shape[iter1]

_No metrics available._


### test_one_xclbin_serves_every_shape[iter2]

_No metrics available._


### test_one_xclbin_serves_every_shape[iter3]

_No metrics available._


### test_one_xclbin_serves_every_shape[iter4]

_No metrics available._


### test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of]

_No metrics available._


### test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of]

_No metrics available._


### test_rejects_unservable_shapes[K_512-N_128-exc_<class 'NotImplementedError'>-match_tile_n]

_No metrics available._


</details>


<details>
<summary>iron/operators/flm/gemm</summary>


### test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024]

_No metrics available._


### test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048]

_No metrics available._


### test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>4.26 (-9.54%)</td><td>3.39 (-4.73%)</td><td>3.09 (-4.87%)</td><td>2.76 (-4.99%)</td><td>0.64 (-16.11%)</td><td>498.80 (+5.25%)</td><td>416.66 (+4.31%)</td><td>445.10 (+5.13%)</td><td>322.80 (+10.55%)</td><td>73.84 (-3.96%)</td><td>831.70 (-9.54%)</td><td>661.83 (-4.73%)</td><td>603.10 (-4.87%)</td><td>538.14 (-4.99%)</td><td>124.40 (-16.11%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>4.71 (n/a)</td><td>3.56 (n/a)</td><td>3.25 (n/a)</td><td>2.90 (n/a)</td><td>0.76 (n/a)</td><td>473.90 (n/a)</td><td>399.46 (n/a)</td><td>423.40 (n/a)</td><td>292.00 (n/a)</td><td>76.88 (n/a)</td><td>919.38 (n/a)</td><td>694.66 (n/a)</td><td>633.97 (n/a)</td><td>566.39 (n/a)</td><td>148.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>5.93 (-2.48%)</td><td>4.48 (-0.68%)</td><td>3.89 (+8.16%)</td><td>3.57 (+2.80%)</td><td>1.10 (-16.31%)</td><td>385.20 (-2.73%)</td><td>321.10 (-1.13%)</td><td>353.50 (-7.56%)</td><td>232.10 (+2.52%)</td><td>72.25 (-15.44%)</td><td>1156.54 (-2.48%)</td><td>874.49 (-0.68%)</td><td>759.32 (+8.16%)</td><td>696.87 (+2.80%)</td><td>214.58 (-16.31%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>6.08 (n/a)</td><td>4.51 (n/a)</td><td>3.60 (n/a)</td><td>3.48 (n/a)</td><td>1.31 (n/a)</td><td>396.00 (n/a)</td><td>324.78 (n/a)</td><td>382.40 (n/a)</td><td>226.40 (n/a)</td><td>85.45 (n/a)</td><td>1185.93 (n/a)</td><td>880.50 (n/a)</td><td>702.05 (n/a)</td><td>677.88 (n/a)</td><td>256.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>8.04 <b>(+21.27%)</b></td><td>4.48 (-8.59%)</td><td>3.58 <b>(-29.07%)</b></td><td>3.36 (-2.22%)</td><td>2.01 <b>(+43.55%)</b></td><td>409.20 (+2.25%)</td><td>342.90 (+13.92%)</td><td>384.80 <b>(+41.00%)</b></td><td>171.10 (-17.54%)</td><td>99.74 (+12.97%)</td><td>1568.56 <b>(+21.27%)</b></td><td>873.13 (-8.59%)</td><td>697.61 <b>(-29.07%)</b></td><td>655.94 (-2.22%)</td><td>392.18 <b>(+43.55%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>6.63 (n/a)</td><td>4.90 (n/a)</td><td>5.04 (n/a)</td><td>3.44 (n/a)</td><td>1.40 (n/a)</td><td>400.20 (n/a)</td><td>301.00 (n/a)</td><td>272.90 (n/a)</td><td>207.50 (n/a)</td><td>88.28 (n/a)</td><td>1293.44 (n/a)</td><td>955.17 (n/a)</td><td>983.53 (n/a)</td><td>670.83 (n/a)</td><td>273.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>6.33 (+16.77%)</td><td>4.32 (+1.38%)</td><td>3.80 (+2.71%)</td><td>3.76 (+10.59%)</td><td>1.12 (+10.52%)</td><td>366.10 (-9.58%)</td><td>331.52 (-1.56%)</td><td>362.20 (-2.63%)</td><td>217.60 (-14.36%)</td><td>64.00 (-13.98%)</td><td>1233.77 (+16.77%)</td><td>843.47 (+1.38%)</td><td>741.15 (+2.71%)</td><td>733.14 (+10.59%)</td><td>218.59 (+10.51%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>5.42 (n/a)</td><td>4.27 (n/a)</td><td>3.70 (n/a)</td><td>3.40 (n/a)</td><td>1.01 (n/a)</td><td>404.90 (n/a)</td><td>336.78 (n/a)</td><td>372.00 (n/a)</td><td>254.10 (n/a)</td><td>74.39 (n/a)</td><td>1056.61 (n/a)</td><td>831.96 (n/a)</td><td>721.56 (n/a)</td><td>662.93 (n/a)</td><td>197.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>6.35 <b>(+44.67%)</b></td><td>3.79 (+3.48%)</td><td>3.15 (-15.09%)</td><td>3.04 (+0.97%)</td><td>1.43 <b>(+176.74%)</b></td><td>452.80 (-0.96%)</td><td>392.68 (+2.94%)</td><td>437.60 (+17.79%)</td><td>216.90 <b>(-30.88%)</b></td><td>99.25 <b>(+83.62%)</b></td><td>1237.75 <b>(+44.67%)</b></td><td>739.94 (+3.48%)</td><td>613.46 (-15.09%)</td><td>592.89 (+0.97%)</td><td>279.01 <b>(+176.74%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>4.39 (n/a)</td><td>3.67 (n/a)</td><td>3.70 (n/a)</td><td>3.01 (n/a)</td><td>0.52 (n/a)</td><td>457.20 (n/a)</td><td>381.46 (n/a)</td><td>371.50 (n/a)</td><td>313.80 (n/a)</td><td>54.05 (n/a)</td><td>855.55 (n/a)</td><td>715.08 (n/a)</td><td>722.48 (n/a)</td><td>587.18 (n/a)</td><td>100.82 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>2.32 <b>(+36.12%)</b></td><td>1.32 (+0.56%)</td><td>1.10 (-10.61%)</td><td>1.02 (-2.25%)</td><td>0.56 <b>(+95.81%)</b></td><td>392.70 (+2.29%)</td><td>334.76 (+5.63%)</td><td>363.50 (+11.85%)</td><td>173.10 <b>(-26.53%)</b></td><td>91.30 <b>(+39.94%)</b></td><td>193.88 <b>(+36.12%)</b></td><td>110.41 (+0.56%)</td><td>92.30 (-10.61%)</td><td>85.44 (-2.25%)</td><td>46.76 <b>(+95.81%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.70 (n/a)</td><td>1.31 (n/a)</td><td>1.24 (n/a)</td><td>1.05 (n/a)</td><td>0.29 (n/a)</td><td>383.90 (n/a)</td><td>316.92 (n/a)</td><td>325.00 (n/a)</td><td>235.60 (n/a)</td><td>65.24 (n/a)</td><td>142.43 (n/a)</td><td>109.79 (n/a)</td><td>103.25 (n/a)</td><td>87.40 (n/a)</td><td>23.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>9.22 <b>(+38.39%)</b></td><td>6.14 (+10.73%)</td><td>4.88 (-7.12%)</td><td>4.74 (+1.45%)</td><td>1.96 <b>(+115.09%)</b></td><td>408.20 (-1.42%)</td><td>337.74 (-5.22%)</td><td>395.90 (+7.67%)</td><td>209.70 <b>(-27.74%)</b></td><td>89.61 <b>(+58.08%)</b></td><td>1920.15 <b>(+38.38%)</b></td><td>1277.92 (+10.73%)</td><td>1017.02 (-7.12%)</td><td>986.32 (+1.45%)</td><td>408.69 <b>(+115.09%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>6.66 (n/a)</td><td>5.54 (n/a)</td><td>5.26 (n/a)</td><td>4.67 (n/a)</td><td>0.91 (n/a)</td><td>414.10 (n/a)</td><td>356.34 (n/a)</td><td>367.70 (n/a)</td><td>290.20 (n/a)</td><td>56.69 (n/a)</td><td>1387.54 (n/a)</td><td>1154.09 (n/a)</td><td>1094.97 (n/a)</td><td>972.24 (n/a)</td><td>190.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>14.51 (-1.88%)</td><td>11.80 (-7.00%)</td><td>11.26 (-8.08%)</td><td>9.79 (-12.69%)</td><td>1.75 (+12.51%)</td><td>562.40 (+14.54%)</td><td>474.56 (+8.07%)</td><td>488.70 (+8.79%)</td><td>379.50 (+1.91%)</td><td>66.96 <b>(+28.66%)</b></td><td>5659.00 (-1.88%)</td><td>4601.52 (-7.00%)</td><td>4394.01 (-8.08%)</td><td>3818.37 (-12.69%)</td><td>683.23 (+12.51%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>14.78 (n/a)</td><td>12.68 (n/a)</td><td>12.25 (n/a)</td><td>11.21 (n/a)</td><td>1.56 (n/a)</td><td>491.00 (n/a)</td><td>439.12 (n/a)</td><td>449.20 (n/a)</td><td>372.40 (n/a)</td><td>52.04 (n/a)</td><td>5767.24 (n/a)</td><td>4948.00 (n/a)</td><td>4780.42 (n/a)</td><td>4373.56 (n/a)</td><td>607.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm_tile_options[tn128-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn16-ma64-default]

_No metrics available._


### test_gemm_tile_options[tn32-ma64-default]

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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.90 (n/a)</td><td>172.72 (n/a)</td><td>170.10 (n/a)</td><td>130.80 (n/a)</td><td>32.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>334.70 (n/a)</td><td>206.52 (n/a)</td><td>185.60 (n/a)</td><td>161.10 (n/a)</td><td>72.63 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>187.80 (n/a)</td><td>166.48 (n/a)</td><td>165.20 (n/a)</td><td>149.40 (n/a)</td><td>13.81 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>179.60 (n/a)</td><td>164.26 (n/a)</td><td>165.40 (n/a)</td><td>140.90 (n/a)</td><td>14.39 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>175.10 (n/a)</td><td>165.98 (n/a)</td><td>166.10 (n/a)</td><td>158.40 (n/a)</td><td>6.61 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>229.20 (n/a)</td><td>193.42 (n/a)</td><td>207.20 (n/a)</td><td>153.10 (n/a)</td><td>31.28 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>220.10 (n/a)</td><td>197.36 (n/a)</td><td>197.20 (n/a)</td><td>166.50 (n/a)</td><td>21.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>234.40 (n/a)</td><td>215.50 (n/a)</td><td>216.00 (n/a)</td><td>203.60 (n/a)</td><td>12.72 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gemm</summary>


### test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>4.86 (+0.80%)</td><td>4.24 (+2.43%)</td><td>4.21 (-0.04%)</td><td>3.78 (+7.30%)</td><td>0.39 <b>(-27.04%)</b></td><td>2486.80 (-6.81%)</td><td>2232.14 (-3.05%)</td><td>2233.30 (+0.04%)</td><td>1933.90 (-0.80%)</td><td>197.50 <b>(-34.13%)</b></td><td>1912.94 (+0.80%)</td><td>1668.18 (+2.43%)</td><td>1656.45 (-0.04%)</td><td>1487.61 (+7.30%)</td><td>153.89 <b>(-27.04%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>4.82 (n/a)</td><td>4.14 (n/a)</td><td>4.21 (n/a)</td><td>3.52 (n/a)</td><td>0.54 (n/a)</td><td>2668.40 (n/a)</td><td>2302.48 (n/a)</td><td>2232.40 (n/a)</td><td>1949.40 (n/a)</td><td>299.81 (n/a)</td><td>1897.70 (n/a)</td><td>1628.60 (n/a)</td><td>1657.12 (n/a)</td><td>1386.35 (n/a)</td><td>210.94 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.03 (-16.52%)</td><td>0.93 (-1.90%)</td><td>0.99 (-6.32%)</td><td>0.68 (+6.17%)</td><td>0.14 <b>(-47.00%)</b></td><td>327.40 (-5.81%)</td><td>244.44 (-3.06%)</td><td>223.30 (+6.79%)</td><td>214.50 (+19.77%)</td><td>46.95 <b>(-40.61%)</b></td><td>43.99 (-16.52%)</td><td>39.55 (-1.90%)</td><td>42.27 (-6.32%)</td><td>28.82 (+6.17%)</td><td>6.15 <b>(-47.00%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.24 (n/a)</td><td>0.94 (n/a)</td><td>1.06 (n/a)</td><td>0.64 (n/a)</td><td>0.27 (n/a)</td><td>347.60 (n/a)</td><td>252.16 (n/a)</td><td>209.10 (n/a)</td><td>179.10 (n/a)</td><td>79.04 (n/a)</td><td>52.69 (n/a)</td><td>40.31 (n/a)</td><td>45.12 (n/a)</td><td>27.15 (n/a)</td><td>11.60 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.16 (-10.08%)</td><td>1.03 (-3.11%)</td><td>1.03 (-8.15%)</td><td>0.89 (+9.90%)</td><td>0.10 <b>(-53.72%)</b></td><td>247.20 (-9.02%)</td><td>215.94 (+0.62%)</td><td>214.30 (+8.89%)</td><td>190.70 (+11.20%)</td><td>20.60 <b>(-53.30%)</b></td><td>49.49 (-10.08%)</td><td>44.01 (-3.11%)</td><td>44.03 (-8.15%)</td><td>38.17 (+9.90%)</td><td>4.10 <b>(-53.72%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.29 (n/a)</td><td>1.06 (n/a)</td><td>1.12 (n/a)</td><td>0.81 (n/a)</td><td>0.21 (n/a)</td><td>271.70 (n/a)</td><td>214.60 (n/a)</td><td>196.80 (n/a)</td><td>171.50 (n/a)</td><td>44.11 (n/a)</td><td>55.04 (n/a)</td><td>45.43 (n/a)</td><td>47.94 (n/a)</td><td>34.73 (n/a)</td><td>8.86 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.53 (-0.03%)</td><td>0.53 (-0.02%)</td><td>0.53 (+0.04%)</td><td>0.53 (-0.04%)</td><td>0.00 <b>(+20.19%)</b></td><td>47908.80 (+0.04%)</td><td>47822.90 (+0.02%)</td><td>47783.90 (-0.04%)</td><td>47777.10 (+0.03%)</td><td>60.04 <b>(+20.19%)</b></td><td>359.58 (-0.03%)</td><td>359.24 (-0.02%)</td><td>359.53 (+0.04%)</td><td>358.59 (-0.04%)</td><td>0.45 <b>(+20.19%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47889.20 (n/a)</td><td>47811.14 (n/a)</td><td>47803.60 (n/a)</td><td>47762.70 (n/a)</td><td>49.95 (n/a)</td><td>359.69 (n/a)</td><td>359.33 (n/a)</td><td>359.38 (n/a)</td><td>358.74 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.91 (-0.10%)</td><td>0.90 (-0.09%)</td><td>0.91 (+0.31%)</td><td>0.89 (-0.81%)</td><td>0.01 <b>(+60.74%)</b></td><td>28118.80 (+0.81%)</td><td>27837.24 (+0.10%)</td><td>27779.70 (-0.31%)</td><td>27728.30 (+0.10%)</td><td>159.43 <b>(+62.40%)</b></td><td>619.58 (-0.10%)</td><td>617.17 (-0.09%)</td><td>618.43 (+0.31%)</td><td>610.98 (-0.81%)</td><td>3.51 <b>(+60.74%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>27891.80 (n/a)</td><td>27810.44 (n/a)</td><td>27864.70 (n/a)</td><td>27699.90 (n/a)</td><td>98.17 (n/a)</td><td>620.21 (n/a)</td><td>617.75 (n/a)</td><td>616.55 (n/a)</td><td>615.95 (n/a)</td><td>2.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>3.34 (+0.69%)</td><td>3.20 (-1.89%)</td><td>3.19 (-2.90%)</td><td>3.13 (-1.01%)</td><td>0.08 <b>(+38.82%)</b></td><td>8033.60 (+1.02%)</td><td>7862.90 (+1.95%)</td><td>7898.10 (+2.99%)</td><td>7538.80 (-0.68%)</td><td>193.87 <b>(+38.26%)</b></td><td>2278.87 (+0.69%)</td><td>2186.02 (-1.89%)</td><td>2175.20 (-2.90%)</td><td>2138.51 (-1.01%)</td><td>55.19 <b>(+38.82%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>3.32 (n/a)</td><td>3.26 (n/a)</td><td>3.28 (n/a)</td><td>3.16 (n/a)</td><td>0.06 (n/a)</td><td>7952.30 (n/a)</td><td>7712.62 (n/a)</td><td>7669.00 (n/a)</td><td>7590.50 (n/a)</td><td>140.22 (n/a)</td><td>2263.35 (n/a)</td><td>2228.09 (n/a)</td><td>2240.17 (n/a)</td><td>2160.37 (n/a)</td><td>39.76 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>4.18 (+2.57%)</td><td>3.61 (-4.85%)</td><td>3.69 (-0.24%)</td><td>3.03 (-17.89%)</td><td>0.43 <b>(+161.18%)</b></td><td>2659.40 <b>(+21.79%)</b></td><td>2261.18 (+6.19%)</td><td>2181.70 (+0.24%)</td><td>1926.20 (-2.51%)</td><td>276.80 <b>(+212.69%)</b></td><td>1097.49 (+2.57%)</td><td>945.93 (-4.85%)</td><td>968.93 (-0.24%)</td><td>794.89 (-17.89%)</td><td>113.51 <b>(+161.18%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>4.08 (n/a)</td><td>3.79 (n/a)</td><td>3.70 (n/a)</td><td>3.69 (n/a)</td><td>0.17 (n/a)</td><td>2183.60 (n/a)</td><td>2129.42 (n/a)</td><td>2176.40 (n/a)</td><td>1975.70 (n/a)</td><td>88.52 (n/a)</td><td>1069.96 (n/a)</td><td>994.17 (n/a)</td><td>971.29 (n/a)</td><td>968.10 (n/a)</td><td>43.46 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.36 (-8.99%)</td><td>0.34 (-5.27%)</td><td>0.33 (-6.86%)</td><td>0.32 (-4.26%)</td><td>0.02 <b>(-30.83%)</b></td><td>3920.80 (+4.45%)</td><td>3706.72 (+5.34%)</td><td>3769.90 (+7.37%)</td><td>3421.60 (+9.87%)</td><td>207.27 <b>(-20.97%)</b></td><td>19.61 (-8.99%)</td><td>18.15 (-5.27%)</td><td>17.80 (-6.86%)</td><td>17.12 (-4.26%)</td><td>1.04 <b>(-30.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.03 (n/a)</td><td>3753.80 (n/a)</td><td>3518.92 (n/a)</td><td>3511.20 (n/a)</td><td>3114.10 (n/a)</td><td>262.27 (n/a)</td><td>21.55 (n/a)</td><td>19.16 (n/a)</td><td>19.11 (n/a)</td><td>17.88 (n/a)</td><td>1.50 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>6.16 (+1.03%)</td><td>4.51 (-8.12%)</td><td>4.73 (-1.18%)</td><td>3.20 (-13.91%)</td><td>1.16 <b>(+35.57%)</b></td><td>2081.00 (+16.15%)</td><td>1555.56 (+11.92%)</td><td>1405.10 (+1.20%)</td><td>1079.90 (-1.02%)</td><td>400.54 <b>(+56.46%)</b></td><td>1903.11 (+1.03%)</td><td>1393.91 (-8.12%)</td><td>1462.68 (-1.18%)</td><td>987.60 (-13.91%)</td><td>359.84 <b>(+35.57%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>6.10 (n/a)</td><td>4.91 (n/a)</td><td>4.79 (n/a)</td><td>3.71 (n/a)</td><td>0.86 (n/a)</td><td>1791.60 (n/a)</td><td>1389.88 (n/a)</td><td>1388.40 (n/a)</td><td>1091.00 (n/a)</td><td>256.00 (n/a)</td><td>1883.77 (n/a)</td><td>1517.17 (n/a)</td><td>1480.22 (n/a)</td><td>1147.11 (n/a)</td><td>265.43 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>13.21 (n/a)</td><td>12.56 (n/a)</td><td>12.72 (n/a)</td><td>11.25 (n/a)</td><td>0.81 (n/a)</td><td>13.20 (n/a)</td><td>12.55 (n/a)</td><td>12.71 (n/a)</td><td>11.24 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>24.90 (+1.81%)</td><td>24.21 (+9.45%)</td><td>24.10 (+2.31%)</td><td>23.92 <b>(+42.03%)</b></td><td>0.41 <b>(-86.83%)</b></td><td>24.89 (+1.81%)</td><td>24.19 (+9.45%)</td><td>24.08 (+2.31%)</td><td>23.90 <b>(+42.03%)</b></td><td>0.40 <b>(-86.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>24.46 (n/a)</td><td>22.12 (n/a)</td><td>23.55 (n/a)</td><td>16.84 (n/a)</td><td>3.08 (n/a)</td><td>24.44 (n/a)</td><td>22.11 (n/a)</td><td>23.54 (n/a)</td><td>16.83 (n/a)</td><td>3.07 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>41.91 (+0.39%)</td><td>40.76 (+0.81%)</td><td>40.42 (+1.29%)</td><td>40.09 (+1.50%)</td><td>0.77 <b>(-21.99%)</b></td><td>41.88 (+0.39%)</td><td>40.74 (+0.81%)</td><td>40.39 (+1.29%)</td><td>40.06 (+1.50%)</td><td>0.77 <b>(-21.99%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>41.74 (n/a)</td><td>40.43 (n/a)</td><td>39.90 (n/a)</td><td>39.50 (n/a)</td><td>0.98 (n/a)</td><td>41.72 (n/a)</td><td>40.41 (n/a)</td><td>39.87 (n/a)</td><td>39.47 (n/a)</td><td>0.98 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>42.48 (-6.86%)</td><td>41.96 (-5.06%)</td><td>42.28 (-5.18%)</td><td>40.91 (-3.75%)</td><td>0.65 <b>(-44.67%)</b></td><td>42.45 (-6.86%)</td><td>41.94 (-5.06%)</td><td>42.25 (-5.18%)</td><td>40.88 (-3.75%)</td><td>0.65 <b>(-44.67%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>45.60 (n/a)</td><td>44.20 (n/a)</td><td>44.59 (n/a)</td><td>42.51 (n/a)</td><td>1.17 (n/a)</td><td>45.58 (n/a)</td><td>44.17 (n/a)</td><td>44.56 (n/a)</td><td>42.48 (n/a)</td><td>1.17 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>13.30 (n/a)</td><td>12.62 (n/a)</td><td>12.58 (n/a)</td><td>11.81 (n/a)</td><td>0.54 (n/a)</td><td>13.29 (n/a)</td><td>12.61 (n/a)</td><td>12.58 (n/a)</td><td>11.80 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>24.69 (-2.63%)</td><td>24.25 (+1.32%)</td><td>24.22 (+2.02%)</td><td>23.55 (+3.16%)</td><td>0.47 <b>(-50.05%)</b></td><td>24.68 (-2.63%)</td><td>24.24 (+1.32%)</td><td>24.21 (+2.02%)</td><td>23.53 (+3.16%)</td><td>0.47 <b>(-50.05%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>25.36 (n/a)</td><td>23.93 (n/a)</td><td>23.74 (n/a)</td><td>22.82 (n/a)</td><td>0.94 (n/a)</td><td>25.34 (n/a)</td><td>23.92 (n/a)</td><td>23.73 (n/a)</td><td>22.81 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>40.36 (-5.95%)</td><td>39.37 (+2.43%)</td><td>38.97 (-2.97%)</td><td>38.63 <b>(+38.61%)</b></td><td>0.79 <b>(-86.78%)</b></td><td>40.33 (-5.95%)</td><td>39.34 (+2.43%)</td><td>38.95 (-2.97%)</td><td>38.61 <b>(+38.61%)</b></td><td>0.79 <b>(-86.78%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>42.91 (n/a)</td><td>38.43 (n/a)</td><td>40.16 (n/a)</td><td>27.87 (n/a)</td><td>6.01 (n/a)</td><td>42.89 (n/a)</td><td>38.41 (n/a)</td><td>40.14 (n/a)</td><td>27.86 (n/a)</td><td>6.01 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>43.09 (-4.87%)</td><td>42.49 (-3.29%)</td><td>42.51 (-2.08%)</td><td>41.89 (-1.54%)</td><td>0.43 <b>(-66.10%)</b></td><td>43.07 (-4.87%)</td><td>42.46 (-3.29%)</td><td>42.49 (-2.08%)</td><td>41.86 (-1.54%)</td><td>0.43 <b>(-66.10%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>45.30 (n/a)</td><td>43.93 (n/a)</td><td>43.41 (n/a)</td><td>42.55 (n/a)</td><td>1.26 (n/a)</td><td>45.27 (n/a)</td><td>43.90 (n/a)</td><td>43.39 (n/a)</td><td>42.52 (n/a)</td><td>1.26 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>10.00 (+7.33%)</td><td>8.85 (+1.46%)</td><td>8.82 (+1.50%)</td><td>7.83 (-4.65%)</td><td>0.84 <b>(+86.00%)</b></td><td>9.98 (+7.33%)</td><td>8.83 (+1.46%)</td><td>8.81 (+1.50%)</td><td>7.81 (-4.65%)</td><td>0.84 <b>(+86.00%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>9.32 (n/a)</td><td>8.72 (n/a)</td><td>8.69 (n/a)</td><td>8.21 (n/a)</td><td>0.45 (n/a)</td><td>9.30 (n/a)</td><td>8.71 (n/a)</td><td>8.68 (n/a)</td><td>8.19 (n/a)</td><td>0.45 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.04 (-0.82%)</td><td>0.95 (+4.84%)</td><td>0.97 (+10.84%)</td><td>0.83 (+4.20%)</td><td>0.08 <b>(-24.06%)</b></td><td>1.02 (-0.82%)</td><td>0.94 (+4.84%)</td><td>0.96 (+10.84%)</td><td>0.82 (+4.20%)</td><td>0.08 <b>(-24.06%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.05 (n/a)</td><td>0.91 (n/a)</td><td>0.88 (n/a)</td><td>0.80 (n/a)</td><td>0.10 (n/a)</td><td>1.03 (n/a)</td><td>0.89 (n/a)</td><td>0.86 (n/a)</td><td>0.78 (n/a)</td><td>0.10 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.43 (+3.35%)</td><td>1.22 (-1.26%)</td><td>1.25 (+4.38%)</td><td>1.04 (-8.24%)</td><td>0.15 <b>(+43.35%)</b></td><td>1.41 (+3.35%)</td><td>1.20 (-1.26%)</td><td>1.23 (+4.38%)</td><td>1.03 (-8.24%)</td><td>0.15 <b>(+43.35%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.38 (n/a)</td><td>1.23 (n/a)</td><td>1.19 (n/a)</td><td>1.13 (n/a)</td><td>0.10 (n/a)</td><td>1.37 (n/a)</td><td>1.22 (n/a)</td><td>1.18 (n/a)</td><td>1.12 (n/a)</td><td>0.10 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>18.96 (-10.28%)</td><td>17.46 (-1.06%)</td><td>17.07 (-3.09%)</td><td>16.32 (+3.32%)</td><td>1.25 <b>(-42.52%)</b></td><td>18.74 (-10.28%)</td><td>17.26 (-1.06%)</td><td>16.87 (-3.09%)</td><td>16.13 (+3.32%)</td><td>1.24 <b>(-42.52%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>21.14 (n/a)</td><td>17.65 (n/a)</td><td>17.61 (n/a)</td><td>15.80 (n/a)</td><td>2.18 (n/a)</td><td>20.89 (n/a)</td><td>17.44 (n/a)</td><td>17.41 (n/a)</td><td>15.61 (n/a)</td><td>2.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>14.06 (+3.36%)</td><td>12.45 (-6.50%)</td><td>13.24 (-1.86%)</td><td>7.99 <b>(-38.37%)</b></td><td>2.53 <b>(+690.83%)</b></td><td>13.82 (+3.36%)</td><td>12.23 (-6.50%)</td><td>13.01 (-1.86%)</td><td>7.85 <b>(-38.37%)</b></td><td>2.49 <b>(+690.84%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>13.61 (n/a)</td><td>13.32 (n/a)</td><td>13.50 (n/a)</td><td>12.96 (n/a)</td><td>0.32 (n/a)</td><td>13.37 (n/a)</td><td>13.08 (n/a)</td><td>13.26 (n/a)</td><td>12.73 (n/a)</td><td>0.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>8.21 (-0.28%)</td><td>7.72 (+4.48%)</td><td>7.81 (-0.64%)</td><td>6.95 (+19.56%)</td><td>0.48 <b>(-50.42%)</b></td><td>8.06 (-0.28%)</td><td>7.59 (+4.48%)</td><td>7.68 (-0.64%)</td><td>6.83 (+19.56%)</td><td>0.47 <b>(-50.42%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>8.23 (n/a)</td><td>7.39 (n/a)</td><td>7.86 (n/a)</td><td>5.81 (n/a)</td><td>0.97 (n/a)</td><td>8.09 (n/a)</td><td>7.27 (n/a)</td><td>7.72 (n/a)</td><td>5.71 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>6.73 (+9.16%)</td><td>5.68 (+5.04%)</td><td>5.35 (+2.11%)</td><td>4.91 (+4.49%)</td><td>0.84 <b>(+47.86%)</b></td><td>6.62 (+9.16%)</td><td>5.59 (+5.04%)</td><td>5.26 (+2.11%)</td><td>4.83 (+4.49%)</td><td>0.83 <b>(+47.86%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>6.17 (n/a)</td><td>5.40 (n/a)</td><td>5.24 (n/a)</td><td>4.69 (n/a)</td><td>0.57 (n/a)</td><td>6.07 (n/a)</td><td>5.32 (n/a)</td><td>5.15 (n/a)</td><td>4.62 (n/a)</td><td>0.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>13.14 (n/a)</td><td>12.68 (n/a)</td><td>12.71 (n/a)</td><td>12.11 (n/a)</td><td>0.47 (n/a)</td><td>13.13 (n/a)</td><td>12.67 (n/a)</td><td>12.71 (n/a)</td><td>12.10 (n/a)</td><td>0.47 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>13.38 (n/a)</td><td>12.50 (n/a)</td><td>12.96 (n/a)</td><td>11.14 (n/a)</td><td>0.96 (n/a)</td><td>13.37 (n/a)</td><td>12.49 (n/a)</td><td>12.95 (n/a)</td><td>11.13 (n/a)</td><td>0.96 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.30 (n/a)</td><td>208.20 (n/a)</td><td>217.10 (n/a)</td><td>161.90 (n/a)</td><td>28.54 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>180.62 (n/a)</td><td>179.00 (n/a)</td><td>146.10 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>194.44 (n/a)</td><td>182.30 (n/a)</td><td>171.20 (n/a)</td><td>26.51 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.80 (n/a)</td><td>179.50 (n/a)</td><td>189.10 (n/a)</td><td>144.00 (n/a)</td><td>27.66 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>196.30 (n/a)</td><td>189.54 (n/a)</td><td>190.10 (n/a)</td><td>184.50 (n/a)</td><td>4.60 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>215.70 (n/a)</td><td>181.20 (n/a)</td><td>179.80 (n/a)</td><td>147.30 (n/a)</td><td>29.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>200.76 (n/a)</td><td>210.80 (n/a)</td><td>157.40 (n/a)</td><td>25.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>328.00 (n/a)</td><td>262.70 (n/a)</td><td>260.60 (n/a)</td><td>224.10 (n/a)</td><td>41.61 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (+8.24%)</td><td>0.05 (+14.53%)</td><td>0.05 <b>(+27.02%)</b></td><td>0.04 (+16.61%)</td><td>0.01 (-18.32%)</td><td>199.90 (-14.28%)</td><td>171.76 (-13.67%)</td><td>162.30 <b>(-21.29%)</b></td><td>146.70 (-7.62%)</td><td>22.10 <b>(-34.61%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.20 (n/a)</td><td>198.96 (n/a)</td><td>206.20 (n/a)</td><td>158.80 (n/a)</td><td>33.79 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (+1.76%)</td><td>0.05 (-0.93%)</td><td>0.05 (-3.52%)</td><td>0.04 (+0.43%)</td><td>0.01 (+2.49%)</td><td>209.50 (-0.43%)</td><td>172.36 (+0.98%)</td><td>170.60 (+3.65%)</td><td>133.10 (-1.70%)</td><td>29.29 (-0.71%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>170.68 (n/a)</td><td>164.60 (n/a)</td><td>135.40 (n/a)</td><td>29.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 <b>(-20.42%)</b></td><td>0.05 (+13.01%)</td><td>0.05 <b>(+26.15%)</b></td><td>0.04 <b>(+85.10%)</b></td><td>0.00 <b>(-70.68%)</b></td><td>197.20 <b>(-45.97%)</b></td><td>170.72 <b>(-20.90%)</b></td><td>160.90 <b>(-20.74%)</b></td><td>156.90 <b>(+25.72%)</b></td><td>17.18 <b>(-80.90%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>365.00 (n/a)</td><td>215.84 (n/a)</td><td>203.00 (n/a)</td><td>124.80 (n/a)</td><td>89.94 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (+6.72%)</td><td>0.05 (+6.04%)</td><td>0.04 (-2.15%)</td><td>0.04 (+0.28%)</td><td>0.01 <b>(+26.56%)</b></td><td>229.90 (-0.26%)</td><td>183.88 (-4.73%)</td><td>195.00 (+2.20%)</td><td>144.40 (-6.29%)</td><td>37.95 (+11.48%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.50 (n/a)</td><td>193.00 (n/a)</td><td>190.80 (n/a)</td><td>154.10 (n/a)</td><td>34.04 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (+4.12%)</td><td>0.04 (+3.51%)</td><td>0.04 (-1.30%)</td><td>0.04 (+5.96%)</td><td>0.01 (+11.52%)</td><td>215.20 (-5.61%)</td><td>186.52 (-3.09%)</td><td>193.10 (+1.31%)</td><td>144.90 (-3.91%)</td><td>30.13 (+3.16%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>228.00 (n/a)</td><td>192.46 (n/a)</td><td>190.60 (n/a)</td><td>150.80 (n/a)</td><td>29.21 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 <b>(-28.05%)</b></td><td>0.04 (-14.46%)</td><td>0.04 (-10.62%)</td><td>0.04 (-4.52%)</td><td>0.00 <b>(-67.92%)</b></td><td>217.90 (+4.76%)</td><td>199.40 (+14.36%)</td><td>200.20 (+11.91%)</td><td>184.90 <b>(+39.02%)</b></td><td>14.05 <b>(-53.69%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>174.36 (n/a)</td><td>178.90 (n/a)</td><td>133.00 (n/a)</td><td>30.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 <b>(-33.44%)</b></td><td>0.05 (-14.81%)</td><td>0.05 (-10.68%)</td><td>0.03 (-12.87%)</td><td>0.01 <b>(-49.82%)</b></td><td>260.90 (+14.73%)</td><td>185.96 (+12.74%)</td><td>177.00 (+11.95%)</td><td>152.00 <b>(+50.20%)</b></td><td>43.51 (-9.98%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>227.40 (n/a)</td><td>164.94 (n/a)</td><td>158.10 (n/a)</td><td>101.20 (n/a)</td><td>48.33 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 <b>(-28.64%)</b></td><td>0.04 (-9.77%)</td><td>0.04 (-9.49%)</td><td>0.04 (+16.41%)</td><td>0.00 <b>(-67.59%)</b></td><td>231.20 (-14.08%)</td><td>211.16 (+5.53%)</td><td>215.80 (+10.44%)</td><td>180.50 <b>(+40.14%)</b></td><td>20.24 <b>(-59.72%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>269.10 (n/a)</td><td>200.10 (n/a)</td><td>195.40 (n/a)</td><td>128.80 (n/a)</td><td>50.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (-4.18%)</td><td>0.04 (-6.91%)</td><td>0.04 (-11.38%)</td><td>0.03 (-14.53%)</td><td>0.01 (+7.23%)</td><td>262.00 (+17.02%)</td><td>208.96 (+9.09%)</td><td>229.20 (+12.85%)</td><td>134.60 (+4.34%)</td><td>51.19 <b>(+29.17%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.90 (n/a)</td><td>191.54 (n/a)</td><td>203.10 (n/a)</td><td>129.00 (n/a)</td><td>39.63 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (-3.54%)</td><td>0.04 (+2.37%)</td><td>0.04 (-0.93%)</td><td>0.04 (+12.53%)</td><td>0.00 <b>(-37.29%)</b></td><td>233.50 (-11.15%)</td><td>219.48 (-2.90%)</td><td>225.30 (+0.94%)</td><td>201.60 (+3.70%)</td><td>14.25 <b>(-42.73%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>262.80 (n/a)</td><td>226.04 (n/a)</td><td>223.20 (n/a)</td><td>194.40 (n/a)</td><td>24.88 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (-11.55%)</td><td>0.05 (-5.52%)</td><td>0.05 (-5.06%)</td><td>0.04 (+5.08%)</td><td>0.01 <b>(-45.56%)</b></td><td>211.50 (-4.86%)</td><td>175.86 (+3.47%)</td><td>173.00 (+5.30%)</td><td>152.50 (+13.05%)</td><td>21.69 <b>(-39.44%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.30 (n/a)</td><td>169.96 (n/a)</td><td>164.30 (n/a)</td><td>134.90 (n/a)</td><td>35.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (-0.09%)</td><td>0.04 (-11.12%)</td><td>0.04 (-13.79%)</td><td>0.02 <b>(-36.57%)</b></td><td>0.01 <b>(+180.66%)</b></td><td>335.70 <b>(+57.68%)</b></td><td>232.00 (+17.65%)</td><td>224.30 (+15.98%)</td><td>180.30 (+0.11%)</td><td>62.27 <b>(+341.48%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>212.90 (n/a)</td><td>197.20 (n/a)</td><td>193.40 (n/a)</td><td>180.10 (n/a)</td><td>14.11 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (-12.53%)</td><td>0.05 (+1.15%)</td><td>0.05 (+3.81%)</td><td>0.04 (+14.02%)</td><td>0.01 <b>(-44.28%)</b></td><td>198.30 (-12.30%)</td><td>176.10 (-3.45%)</td><td>173.40 (-3.67%)</td><td>149.00 (+14.35%)</td><td>20.99 <b>(-42.56%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.10 (n/a)</td><td>182.40 (n/a)</td><td>180.00 (n/a)</td><td>130.30 (n/a)</td><td>36.55 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.07 (+8.26%)</td><td>0.05 (+0.41%)</td><td>0.06 (+8.90%)</td><td>0.04 (-10.66%)</td><td>0.01 <b>(+28.40%)</b></td><td>205.80 (+11.91%)</td><td>158.96 (+0.85%)</td><td>148.90 (-8.20%)</td><td>123.30 (-7.64%)</td><td>31.31 <b>(+37.54%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.90 (n/a)</td><td>157.62 (n/a)</td><td>162.20 (n/a)</td><td>133.50 (n/a)</td><td>22.76 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (+3.23%)</td><td>0.05 (+10.24%)</td><td>0.05 (+7.27%)</td><td>0.04 <b>(+49.38%)</b></td><td>0.00 <b>(-52.18%)</b></td><td>185.20 <b>(-33.04%)</b></td><td>171.92 (-12.27%)</td><td>173.20 (-6.78%)</td><td>149.10 (-3.12%)</td><td>13.90 <b>(-70.67%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>276.60 (n/a)</td><td>195.96 (n/a)</td><td>185.80 (n/a)</td><td>153.90 (n/a)</td><td>47.37 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.07 <b>(+46.65%)</b></td><td>0.05 <b>(+22.72%)</b></td><td>0.05 (+13.06%)</td><td>0.04 (+7.18%)</td><td>0.01 <b>(+266.59%)</b></td><td>191.10 (-6.69%)</td><td>155.82 (-16.06%)</td><td>162.70 (-11.53%)</td><td>116.10 <b>(-31.79%)</b></td><td>30.81 <b>(+131.28%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.80 (n/a)</td><td>185.64 (n/a)</td><td>183.90 (n/a)</td><td>170.20 (n/a)</td><td>13.32 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 <b>(+32.41%)</b></td><td>0.05 (+8.42%)</td><td>0.05 (+2.34%)</td><td>0.04 (-6.88%)</td><td>0.01 <b>(+535.41%)</b></td><td>201.90 (+7.34%)</td><td>171.40 (-5.84%)</td><td>176.30 (-2.27%)</td><td>132.50 <b>(-24.46%)</b></td><td>26.83 <b>(+405.69%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>188.10 (n/a)</td><td>182.04 (n/a)</td><td>180.40 (n/a)</td><td>175.40 (n/a)</td><td>5.31 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 <b>(-24.63%)</b></td><td>0.05 (-10.49%)</td><td>0.05 (+0.53%)</td><td>0.04 (-8.90%)</td><td>0.01 <b>(-45.20%)</b></td><td>226.90 (+9.77%)</td><td>184.08 (+8.82%)</td><td>173.00 (-0.52%)</td><td>158.00 <b>(+32.66%)</b></td><td>29.78 <b>(-23.01%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.70 (n/a)</td><td>169.16 (n/a)</td><td>173.90 (n/a)</td><td>119.10 (n/a)</td><td>38.68 (n/a)</td>
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


### test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52628.10 (n/a)</td><td>52544.24 (n/a)</td><td>52560.10 (n/a)</td><td>52433.00 (n/a)</td><td>84.51 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.20 <b>(+47.89%)</b></td><td>0.16 <b>(+24.00%)</b></td><td>0.15 (+16.59%)</td><td>0.15 <b>(+24.91%)</b></td><td>0.02 <b>(+224.97%)</b></td><td>168.50 (-19.95%)</td><td>156.38 (-18.45%)</td><td>163.00 (-14.21%)</td><td>123.30 <b>(-32.40%)</b></td><td>18.75 <b>(+71.29%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>191.76 (n/a)</td><td>190.00 (n/a)</td><td>182.40 (n/a)</td><td>10.95 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.32 (+2.89%)</td><td>0.28 (+12.54%)</td><td>0.32 <b>(+37.93%)</b></td><td>0.18 (-0.82%)</td><td>0.06 <b>(+20.61%)</b></td><td>230.20 (+0.79%)</td><td>155.82 (-9.76%)</td><td>129.80 <b>(-27.49%)</b></td><td>127.00 (-2.83%)</td><td>44.58 (+16.96%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>228.40 (n/a)</td><td>172.68 (n/a)</td><td>179.00 (n/a)</td><td>130.70 (n/a)</td><td>38.12 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.04 (+1.12%)</td><td>0.04 <b>(+20.10%)</b></td><td>0.04 <b>(+33.42%)</b></td><td>0.03 <b>(+37.36%)</b></td><td>0.01 <b>(-34.24%)</b></td><td>174.60 <b>(-27.19%)</b></td><td>141.10 (-19.81%)</td><td>135.70 <b>(-25.07%)</b></td><td>121.60 (-1.14%)</td><td>21.92 <b>(-52.32%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.80 (n/a)</td><td>175.96 (n/a)</td><td>181.10 (n/a)</td><td>123.00 (n/a)</td><td>45.98 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (-14.04%)</td><td>0.05 (-4.29%)</td><td>0.05 (+3.09%)</td><td>0.03 (-12.87%)</td><td>0.01 (-6.35%)</td><td>237.00 (+14.77%)</td><td>178.72 (+5.08%)</td><td>166.70 (-3.03%)</td><td>144.80 (+16.31%)</td><td>37.97 <b>(+29.16%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.50 (n/a)</td><td>170.08 (n/a)</td><td>171.90 (n/a)</td><td>124.50 (n/a)</td><td>29.40 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.10 (+9.89%)</td><td>0.07 (-10.42%)</td><td>0.07 <b>(-28.20%)</b></td><td>0.06 (+2.37%)</td><td>0.02 (+16.80%)</td><td>194.40 (-2.31%)</td><td>171.90 (+12.35%)</td><td>188.10 <b>(+39.23%)</b></td><td>119.20 (-9.01%)</td><td>31.90 (+5.93%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>199.00 (n/a)</td><td>153.00 (n/a)</td><td>135.10 (n/a)</td><td>131.00 (n/a)</td><td>30.11 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (+12.61%)</td><td>0.05 (+13.33%)</td><td>0.06 <b>(+21.36%)</b></td><td>0.04 (+7.38%)</td><td>0.01 (+0.01%)</td><td>186.00 (-6.86%)</td><td>152.16 (-12.07%)</td><td>144.80 (-17.63%)</td><td>126.70 (-11.21%)</td><td>22.18 (-16.75%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.70 (n/a)</td><td>173.04 (n/a)</td><td>175.80 (n/a)</td><td>142.70 (n/a)</td><td>26.64 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.08 (+8.17%)</td><td>0.06 (+3.40%)</td><td>0.06 (-4.65%)</td><td>0.04 (-7.61%)</td><td>0.02 (+2.68%)</td><td>250.20 (+8.22%)</td><td>173.46 (-3.22%)</td><td>174.30 (+4.87%)</td><td>121.10 (-7.56%)</td><td>48.30 (+1.20%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>231.20 (n/a)</td><td>179.24 (n/a)</td><td>166.20 (n/a)</td><td>131.00 (n/a)</td><td>47.73 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (-15.07%)</td><td>0.05 (+4.57%)</td><td>0.05 <b>(+21.64%)</b></td><td>0.04 (+2.43%)</td><td>0.01 <b>(-37.74%)</b></td><td>221.40 (-2.38%)</td><td>176.00 (-6.66%)</td><td>162.70 (-17.79%)</td><td>144.80 (+17.72%)</td><td>30.17 <b>(-24.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.80 (n/a)</td><td>188.56 (n/a)</td><td>197.90 (n/a)</td><td>123.00 (n/a)</td><td>40.14 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.07 (-15.28%)</td><td>0.06 (+1.30%)</td><td>0.06 (+17.57%)</td><td>0.04 (-11.87%)</td><td>0.01 (-17.13%)</td><td>228.50 (+13.46%)</td><td>173.84 (-1.40%)</td><td>158.40 (-14.98%)</td><td>154.50 (+18.12%)</td><td>31.51 (+14.38%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>201.40 (n/a)</td><td>176.30 (n/a)</td><td>186.30 (n/a)</td><td>130.80 (n/a)</td><td>27.54 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (+12.52%)</td><td>0.05 (-0.48%)</td><td>0.04 (-1.39%)</td><td>0.04 (-13.87%)</td><td>0.01 <b>(+212.18%)</b></td><td>220.30 (+16.13%)</td><td>184.44 (+2.18%)</td><td>184.80 (+1.43%)</td><td>148.80 (-11.11%)</td><td>27.71 <b>(+222.58%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.70 (n/a)</td><td>180.50 (n/a)</td><td>182.20 (n/a)</td><td>167.40 (n/a)</td><td>8.59 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (-15.72%)</td><td>0.05 (-5.71%)</td><td>0.06 (+4.49%)</td><td>0.04 (-10.46%)</td><td>0.01 <b>(-31.11%)</b></td><td>218.60 (+11.70%)</td><td>174.54 (+4.80%)</td><td>165.10 (-4.29%)</td><td>144.00 (+18.62%)</td><td>28.86 (-8.95%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>195.70 (n/a)</td><td>166.54 (n/a)</td><td>172.50 (n/a)</td><td>121.40 (n/a)</td><td>31.69 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 <b>(+28.13%)</b></td><td>0.05 (+16.39%)</td><td>0.05 <b>(+22.16%)</b></td><td>0.04 (-7.31%)</td><td>0.01 <b>(+279.73%)</b></td><td>210.70 (+7.89%)</td><td>164.66 (-11.15%)</td><td>154.20 (-18.11%)</td><td>130.90 <b>(-21.94%)</b></td><td>35.81 <b>(+216.98%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>195.30 (n/a)</td><td>185.32 (n/a)</td><td>188.30 (n/a)</td><td>167.70 (n/a)</td><td>11.30 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (-8.72%)</td><td>0.05 (-12.96%)</td><td>0.05 (-7.01%)</td><td>0.03 <b>(-43.30%)</b></td><td>0.01 <b>(+64.08%)</b></td><td>324.50 <b>(+76.36%)</b></td><td>204.18 <b>(+22.22%)</b></td><td>185.90 (+7.52%)</td><td>144.10 (+9.50%)</td><td>70.85 <b>(+236.66%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>184.00 (n/a)</td><td>167.06 (n/a)</td><td>172.90 (n/a)</td><td>131.60 (n/a)</td><td>21.04 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 <b>(+37.89%)</b></td><td>0.05 <b>(+23.07%)</b></td><td>0.05 (+15.85%)</td><td>0.04 <b>(+33.80%)</b></td><td>0.01 <b>(+63.65%)</b></td><td>211.40 <b>(-25.27%)</b></td><td>180.14 (-18.08%)</td><td>181.10 (-13.68%)</td><td>137.80 <b>(-27.47%)</b></td><td>32.14 (-11.92%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>282.90 (n/a)</td><td>219.90 (n/a)</td><td>209.80 (n/a)</td><td>190.00 (n/a)</td><td>36.49 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (-10.04%)</td><td>0.04 (-6.57%)</td><td>0.04 (-0.69%)</td><td>0.04 (-2.56%)</td><td>0.00 <b>(-25.06%)</b></td><td>228.50 (+2.60%)</td><td>202.20 (+6.53%)</td><td>198.10 (+0.66%)</td><td>177.00 (+11.18%)</td><td>21.13 (-13.50%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.70 (n/a)</td><td>189.80 (n/a)</td><td>196.80 (n/a)</td><td>159.20 (n/a)</td><td>24.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.06 (+19.48%)</td><td>0.05 (+18.29%)</td><td>0.04 (+10.81%)</td><td>0.04 <b>(+26.93%)</b></td><td>0.01 <b>(+20.36%)</b></td><td>198.60 <b>(-21.22%)</b></td><td>175.14 (-15.51%)</td><td>190.50 (-9.76%)</td><td>139.70 (-16.30%)</td><td>27.68 (-18.98%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.10 (n/a)</td><td>207.28 (n/a)</td><td>211.10 (n/a)</td><td>166.90 (n/a)</td><td>34.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 (-8.86%)</td><td>0.04 (-1.85%)</td><td>0.04 (-2.17%)</td><td>0.04 (+3.72%)</td><td>0.00 <b>(-34.43%)</b></td><td>225.30 (-3.59%)</td><td>199.36 (+1.13%)</td><td>201.10 (+2.24%)</td><td>176.80 (+9.75%)</td><td>18.02 <b>(-30.13%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.70 (n/a)</td><td>197.14 (n/a)</td><td>196.70 (n/a)</td><td>161.10 (n/a)</td><td>25.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.05 <b>(+31.45%)</b></td><td>0.04 (+19.85%)</td><td>0.04 (+0.47%)</td><td>0.03 <b>(+50.42%)</b></td><td>0.01 <b>(+21.86%)</b></td><td>246.80 <b>(-33.51%)</b></td><td>207.46 (-17.54%)</td><td>222.50 (-0.49%)</td><td>156.50 <b>(-23.92%)</b></td><td>41.55 <b>(-39.53%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>371.20 (n/a)</td><td>251.60 (n/a)</td><td>223.60 (n/a)</td><td>205.70 (n/a)</td><td>68.71 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.78 <b>(+28.38%)</b></td><td>0.57 (+2.66%)</td><td>0.51 (-7.69%)</td><td>0.47 (-6.78%)</td><td>0.13 <b>(+146.65%)</b></td><td>209.40 (+7.27%)</td><td>178.12 (+0.13%)</td><td>191.10 (+8.33%)</td><td>125.70 <b>(-22.12%)</b></td><td>34.10 <b>(+104.50%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.61 (n/a)</td><td>0.56 (n/a)</td><td>0.56 (n/a)</td><td>0.50 (n/a)</td><td>0.05 (n/a)</td><td>195.20 (n/a)</td><td>177.88 (n/a)</td><td>176.40 (n/a)</td><td>161.40 (n/a)</td><td>16.67 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.60 (-7.54%)</td><td>0.56 (+6.16%)</td><td>0.58 (+16.53%)</td><td>0.51 (+17.66%)</td><td>0.04 <b>(-46.09%)</b></td><td>194.40 (-15.00%)</td><td>176.88 (-7.09%)</td><td>168.90 (-14.18%)</td><td>163.70 (+8.20%)</td><td>14.52 <b>(-49.76%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.65 (n/a)</td><td>0.53 (n/a)</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.08 (n/a)</td><td>228.70 (n/a)</td><td>190.38 (n/a)</td><td>196.80 (n/a)</td><td>151.30 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.76 (+19.76%)</td><td>0.57 (+13.67%)</td><td>0.59 (+14.81%)</td><td>0.42 (+8.86%)</td><td>0.13 <b>(+44.24%)</b></td><td>233.00 (-8.12%)</td><td>178.40 (-10.68%)</td><td>166.90 (-12.89%)</td><td>129.40 (-16.46%)</td><td>40.03 (+10.86%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.63 (n/a)</td><td>0.50 (n/a)</td><td>0.51 (n/a)</td><td>0.39 (n/a)</td><td>0.09 (n/a)</td><td>253.60 (n/a)</td><td>199.74 (n/a)</td><td>191.60 (n/a)</td><td>154.90 (n/a)</td><td>36.11 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.66 (+2.66%)</td><td>0.56 (+0.21%)</td><td>0.54 (-7.37%)</td><td>0.48 (-0.80%)</td><td>0.07 (+0.53%)</td><td>203.30 (+0.79%)</td><td>177.08 (-0.26%)</td><td>181.80 (+7.96%)</td><td>150.00 (-2.60%)</td><td>20.50 (-4.11%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.64 (n/a)</td><td>0.56 (n/a)</td><td>0.58 (n/a)</td><td>0.49 (n/a)</td><td>0.07 (n/a)</td><td>201.70 (n/a)</td><td>177.54 (n/a)</td><td>168.40 (n/a)</td><td>154.00 (n/a)</td><td>21.38 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.54 (-2.49%)</td><td>0.48 (+6.38%)</td><td>0.49 (+10.04%)</td><td>0.39 (+14.71%)</td><td>0.07 (-9.66%)</td><td>187.20 (-12.81%)</td><td>157.90 (-6.59%)</td><td>150.80 (-9.16%)</td><td>135.60 (+2.57%)</td><td>23.72 <b>(-20.17%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.56 (n/a)</td><td>0.45 (n/a)</td><td>0.44 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>214.70 (n/a)</td><td>169.04 (n/a)</td><td>166.00 (n/a)</td><td>132.20 (n/a)</td><td>29.71 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.62 (+18.44%)</td><td>0.48 <b>(+20.55%)</b></td><td>0.43 (+8.83%)</td><td>0.43 <b>(+48.39%)</b></td><td>0.08 (-10.35%)</td><td>170.10 <b>(-32.61%)</b></td><td>155.38 (-18.88%)</td><td>169.70 (-8.12%)</td><td>118.40 (-15.55%)</td><td>22.58 <b>(-48.75%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.53 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.29 (n/a)</td><td>0.09 (n/a)</td><td>252.40 (n/a)</td><td>191.54 (n/a)</td><td>184.70 (n/a)</td><td>140.20 (n/a)</td><td>44.05 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.44 <b>(-25.76%)</b></td><td>0.39 (-11.09%)</td><td>0.41 (-2.08%)</td><td>0.32 (+12.55%)</td><td>0.05 <b>(-56.00%)</b></td><td>228.70 (-11.15%)</td><td>190.64 (+7.40%)</td><td>178.00 (+2.06%)</td><td>168.80 <b>(+34.72%)</b></td><td>26.40 <b>(-48.20%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.59 (n/a)</td><td>0.44 (n/a)</td><td>0.42 (n/a)</td><td>0.29 (n/a)</td><td>0.12 (n/a)</td><td>257.40 (n/a)</td><td>177.50 (n/a)</td><td>174.40 (n/a)</td><td>125.30 (n/a)</td><td>50.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.38 (-17.01%)</td><td>0.34 (-3.02%)</td><td>0.35 (-6.65%)</td><td>0.25 (+1.50%)</td><td>0.05 <b>(-43.80%)</b></td><td>292.90 (-1.48%)</td><td>223.78 (-0.39%)</td><td>208.20 (+7.15%)</td><td>193.80 <b>(+20.52%)</b></td><td>39.75 <b>(-33.92%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.46 (n/a)</td><td>0.35 (n/a)</td><td>0.38 (n/a)</td><td>0.25 (n/a)</td><td>0.09 (n/a)</td><td>297.30 (n/a)</td><td>224.66 (n/a)</td><td>194.30 (n/a)</td><td>160.80 (n/a)</td><td>60.16 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.10 <b>(+20.91%)</b></td><td>0.85 <b>(+24.11%)</b></td><td>0.82 <b>(+30.14%)</b></td><td>0.68 <b>(+25.55%)</b></td><td>0.15 (+3.26%)</td><td>193.50 <b>(-20.37%)</b></td><td>158.66 <b>(-20.28%)</b></td><td>160.70 <b>(-23.15%)</b></td><td>119.70 (-17.28%)</td><td>26.26 <b>(-33.25%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.91 (n/a)</td><td>0.68 (n/a)</td><td>0.63 (n/a)</td><td>0.54 (n/a)</td><td>0.15 (n/a)</td><td>243.00 (n/a)</td><td>199.02 (n/a)</td><td>209.10 (n/a)</td><td>144.70 (n/a)</td><td>39.34 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.22 (+17.25%)</td><td>0.84 (+10.37%)</td><td>0.79 (+19.85%)</td><td>0.60 (+0.81%)</td><td>0.25 <b>(+35.11%)</b></td><td>219.00 (-0.82%)</td><td>167.50 (-7.24%)</td><td>165.50 (-16.54%)</td><td>107.80 (-14.72%)</td><td>46.00 (+16.40%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.04 (n/a)</td><td>0.76 (n/a)</td><td>0.66 (n/a)</td><td>0.59 (n/a)</td><td>0.19 (n/a)</td><td>220.80 (n/a)</td><td>180.58 (n/a)</td><td>198.30 (n/a)</td><td>126.40 (n/a)</td><td>39.52 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.92 (-5.07%)</td><td>0.78 (+2.19%)</td><td>0.78 (+13.11%)</td><td>0.61 (-7.75%)</td><td>0.12 (-7.58%)</td><td>215.60 (+8.40%)</td><td>172.24 (-2.20%)</td><td>167.10 (-11.59%)</td><td>141.80 (+5.35%)</td><td>28.98 (+4.97%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.97 (n/a)</td><td>0.76 (n/a)</td><td>0.69 (n/a)</td><td>0.66 (n/a)</td><td>0.13 (n/a)</td><td>198.90 (n/a)</td><td>176.12 (n/a)</td><td>189.00 (n/a)</td><td>134.60 (n/a)</td><td>27.61 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (-3.85%)</td><td>0.03 (-9.42%)</td><td>0.03 (-9.87%)</td><td>0.02 (-5.54%)</td><td>0.00 (-3.56%)</td><td>189.30 (+5.87%)</td><td>157.76 (+10.45%)</td><td>150.50 (+10.99%)</td><td>128.20 (+4.06%)</td><td>23.17 (+5.16%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.80 (n/a)</td><td>142.84 (n/a)</td><td>135.60 (n/a)</td><td>123.20 (n/a)</td><td>22.03 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (+15.38%)</td><td>0.03 (+12.03%)</td><td>0.03 (+11.57%)</td><td>0.02 <b>(+22.37%)</b></td><td>0.01 (+3.44%)</td><td>210.70 (-18.30%)</td><td>155.00 (-11.80%)</td><td>143.20 (-10.33%)</td><td>119.80 (-13.31%)</td><td>35.15 <b>(-27.19%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>257.90 (n/a)</td><td>175.74 (n/a)</td><td>159.70 (n/a)</td><td>138.20 (n/a)</td><td>48.27 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (-4.67%)</td><td>0.03 (+6.99%)</td><td>0.03 <b>(+21.31%)</b></td><td>0.02 (+14.02%)</td><td>0.00 <b>(-33.70%)</b></td><td>199.70 (-12.30%)</td><td>164.76 (-8.68%)</td><td>151.90 (-17.54%)</td><td>141.50 (+4.89%)</td><td>24.46 <b>(-38.08%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.70 (n/a)</td><td>180.42 (n/a)</td><td>184.20 (n/a)</td><td>134.90 (n/a)</td><td>39.50 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.13 (+5.23%)</td><td>0.97 (+10.32%)</td><td>0.94 (+1.42%)</td><td>0.79 <b>(+22.60%)</b></td><td>0.13 <b>(-28.20%)</b></td><td>167.10 (-18.45%)</td><td>137.78 (-11.44%)</td><td>140.20 (-1.41%)</td><td>117.20 (-4.95%)</td><td>19.77 <b>(-44.41%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.07 (n/a)</td><td>0.88 (n/a)</td><td>0.93 (n/a)</td><td>0.64 (n/a)</td><td>0.19 (n/a)</td><td>204.90 (n/a)</td><td>155.58 (n/a)</td><td>142.20 (n/a)</td><td>123.30 (n/a)</td><td>35.56 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.02 (-4.30%)</td><td>0.93 (+0.26%)</td><td>0.93 (-9.59%)</td><td>0.82 (+9.66%)</td><td>0.08 <b>(-52.28%)</b></td><td>161.10 (-8.78%)</td><td>142.40 (-2.20%)</td><td>142.60 (+10.63%)</td><td>129.10 (+4.53%)</td><td>12.09 <b>(-54.59%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.07 (n/a)</td><td>0.93 (n/a)</td><td>1.02 (n/a)</td><td>0.75 (n/a)</td><td>0.16 (n/a)</td><td>176.60 (n/a)</td><td>145.60 (n/a)</td><td>128.90 (n/a)</td><td>123.50 (n/a)</td><td>26.62 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.04 (+4.72%)</td><td>0.91 (+16.33%)</td><td>0.89 (+18.75%)</td><td>0.78 <b>(+21.00%)</b></td><td>0.10 <b>(-24.74%)</b></td><td>169.70 (-17.34%)</td><td>146.22 (-14.97%)</td><td>148.30 (-15.79%)</td><td>126.40 (-4.53%)</td><td>16.02 <b>(-38.83%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.00 (n/a)</td><td>0.78 (n/a)</td><td>0.75 (n/a)</td><td>0.64 (n/a)</td><td>0.13 (n/a)</td><td>205.30 (n/a)</td><td>171.96 (n/a)</td><td>176.10 (n/a)</td><td>132.40 (n/a)</td><td>26.19 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.03 (-5.76%)</td><td>0.86 (+5.59%)</td><td>0.83 (+6.28%)</td><td>0.71 (+1.54%)</td><td>0.12 <b>(-27.15%)</b></td><td>184.90 (-1.54%)</td><td>155.76 (-6.37%)</td><td>158.90 (-5.92%)</td><td>128.20 (+6.13%)</td><td>20.91 <b>(-23.16%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>1.09 (n/a)</td><td>0.81 (n/a)</td><td>0.78 (n/a)</td><td>0.70 (n/a)</td><td>0.16 (n/a)</td><td>187.80 (n/a)</td><td>166.36 (n/a)</td><td>168.90 (n/a)</td><td>120.80 (n/a)</td><td>27.21 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.98 (+4.77%)</td><td>0.88 (+6.90%)</td><td>0.93 (+18.32%)</td><td>0.70 (-4.52%)</td><td>0.12 <b>(+44.85%)</b></td><td>187.90 (+4.74%)</td><td>152.56 (-5.65%)</td><td>141.50 (-15.47%)</td><td>135.00 (-4.53%)</td><td>22.64 <b>(+44.27%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.93 (n/a)</td><td>0.82 (n/a)</td><td>0.79 (n/a)</td><td>0.74 (n/a)</td><td>0.08 (n/a)</td><td>179.40 (n/a)</td><td>161.70 (n/a)</td><td>167.40 (n/a)</td><td>141.40 (n/a)</td><td>15.69 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (+12.65%)</td><td>0.03 (-0.57%)</td><td>0.02 (-9.14%)</td><td>0.02 (+11.48%)</td><td>0.00 (+11.30%)</td><td>195.80 (-10.31%)</td><td>165.10 (+0.49%)</td><td>174.80 (+10.08%)</td><td>123.90 (-11.25%)</td><td>27.91 (-13.12%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.30 (n/a)</td><td>164.30 (n/a)</td><td>158.80 (n/a)</td><td>139.60 (n/a)</td><td>32.12 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.03 (-3.19%)</td><td>0.03 (-2.49%)</td><td>0.03 (+10.94%)</td><td>0.02 <b>(-28.17%)</b></td><td>0.01 <b>(+47.37%)</b></td><td>254.60 <b>(+39.20%)</b></td><td>166.92 (+7.32%)</td><td>136.80 (-9.82%)</td><td>126.30 (+3.27%)</td><td>53.81 <b>(+106.24%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.90 (n/a)</td><td>155.54 (n/a)</td><td>151.70 (n/a)</td><td>122.30 (n/a)</td><td>26.09 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.00 (-2.22%)</td><td>0.00 (-0.94%)</td><td>0.00 (-2.33%)</td><td>0.00 (+0.00%)</td><td>0.00 (-18.35%)</td><td>1032.70 (+0.77%)</td><td>971.04 (+0.61%)</td><td>966.73 (+1.67%)</td><td>926.07 (+0.78%)</td><td>38.50 (-5.73%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1024.81 (n/a)</td><td>965.12 (n/a)</td><td>950.85 (n/a)</td><td>918.88 (n/a)</td><td>40.84 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.01 (-3.49%)</td><td>0.01 (-0.74%)</td><td>0.01 (-3.57%)</td><td>0.01 (+8.82%)</td><td>0.00 <b>(-51.82%)</b></td><td>1100.36 (-8.03%)</td><td>1022.35 (+0.37%)</td><td>1012.87 (+4.05%)</td><td>986.20 (+3.82%)</td><td>45.23 <b>(-55.41%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1196.41 (n/a)</td><td>1018.59 (n/a)</td><td>973.42 (n/a)</td><td>949.95 (n/a)</td><td>101.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.96 (-1.93%)</td><td>0.96 (-0.47%)</td><td>0.96 (-0.44%)</td><td>0.95 (-0.04%)</td><td>0.01 <b>(-52.70%)</b></td><td>2219.02 (+0.04%)</td><td>2193.58 (+0.46%)</td><td>2186.78 (+0.44%)</td><td>2178.67 (+1.96%)</td><td>15.59 <b>(-51.69%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.98 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2218.07 (n/a)</td><td>2183.60 (n/a)</td><td>2177.30 (n/a)</td><td>2136.70 (n/a)</td><td>32.27 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.91 (-0.21%)</td><td>0.90 (+0.98%)</td><td>0.90 (+2.03%)</td><td>0.88 (+1.01%)</td><td>0.01 <b>(-41.69%)</b></td><td>2375.30 (-0.99%)</td><td>2342.81 (-0.98%)</td><td>2340.37 (-1.98%)</td><td>2312.39 (+0.21%)</td><td>23.49 <b>(-42.08%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.91 (n/a)</td><td>0.89 (n/a)</td><td>0.88 (n/a)</td><td>0.87 (n/a)</td><td>0.02 (n/a)</td><td>2399.15 (n/a)</td><td>2366.04 (n/a)</td><td>2387.71 (n/a)</td><td>2307.61 (n/a)</td><td>40.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:18:39</td><td>0.96 (-1.67%)</td><td>0.95 (-1.20%)</td><td>0.96 (-0.87%)</td><td>0.95 (-1.00%)</td><td>0.01 <b>(-24.24%)</b></td><td>2217.39 (+1.01%)</td><td>2198.61 (+1.21%)</td><td>2195.36 (+0.88%)</td><td>2176.79 (+1.71%)</td><td>15.66 <b>(-22.27%)</b></td>
</tr>
<tr>
<td><code>27cf75d</code> — 2026-09-18 16:06:36</td><td>0.98 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.01 (n/a)</td><td>2195.14 (n/a)</td><td>2172.30 (n/a)</td><td>2176.20 (n/a)</td><td>2140.29 (n/a)</td><td>20.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_weight_layout_reaches_both_gemms[b_col_maj_False]

_No metrics available._


### test_weight_layout_reaches_both_gemms[b_col_maj_True]

_No metrics available._


</details>


<details>
<summary>iron/operators/swiglu_prefill_stream</summary>


### test_swiglu_prefill_stream[k_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.39 (-3.74%)</td><td>0.38 (-2.75%)</td><td>0.38 (-1.16%)</td><td>0.37 (-2.33%)</td><td>0.01 <b>(-36.70%)</b></td><td>1403.68 (+2.37%)</td><td>1376.90 (+2.80%)</td><td>1371.38 (+1.17%)</td><td>1349.75 (+3.88%)</td><td>22.90 <b>(-32.37%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1371.14 (n/a)</td><td>1339.42 (n/a)</td><td>1355.46 (n/a)</td><td>1299.29 (n/a)</td><td>33.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_prefill_stream[k_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.25 (-1.73%)</td><td>0.24 (+1.41%)</td><td>0.24 (+2.57%)</td><td>0.24 (+3.17%)</td><td>0.01 <b>(-44.27%)</b></td><td>2205.51 (-3.07%)</td><td>2145.16 (-1.47%)</td><td>2151.48 (-2.51%)</td><td>2097.68 (+1.73%)</td><td>45.57 <b>(-44.90%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.01 (n/a)</td><td>2275.37 (n/a)</td><td>2177.27 (n/a)</td><td>2206.97 (n/a)</td><td>2062.09 (n/a)</td><td>82.70 (n/a)</td>
</tr>
</tbody>
</table>


### test_swiglu_prefill_stream[k_5]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>b091dbd</code> — 2026-09-09 01:09:09</td><td>0.38 (+3.47%)</td><td>0.37 (+2.33%)</td><td>0.37 (+1.61%)</td><td>0.36 (+2.68%)</td><td>0.00 <b>(+42.85%)</b></td><td>1439.29 (-2.59%)</td><td>1423.42 (-2.27%)</td><td>1428.90 (-1.59%)</td><td>1396.02 (-3.35%)</td><td>18.11 <b>(+34.71%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:03:08</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.00 (n/a)</td><td>1477.55 (n/a)</td><td>1456.43 (n/a)</td><td>1452.02 (n/a)</td><td>1444.42 (n/a)</td><td>13.44 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.64 (+10.85%)</td><td>0.61 (+10.05%)</td><td>0.62 (+11.20%)</td><td>0.59 (+9.28%)</td><td>0.02 <b>(+42.27%)</b></td><td>885.80 (-8.48%)</td><td>853.98 (-9.10%)</td><td>847.10 (-10.06%)</td><td>814.40 (-9.79%)</td><td>28.11 (+18.18%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.58 (n/a)</td><td>0.56 (n/a)</td><td>0.56 (n/a)</td><td>0.54 (n/a)</td><td>0.01 (n/a)</td><td>967.90 (n/a)</td><td>939.50 (n/a)</td><td>941.90 (n/a)</td><td>902.80 (n/a)</td><td>23.78 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>0.68 (+4.41%)</td><td>0.64 (+0.57%)</td><td>0.65 (+3.76%)</td><td>0.54 (-11.60%)</td><td>0.05 <b>(+240.29%)</b></td><td>1935.20 (+13.12%)</td><td>1655.02 (+0.05%)</td><td>1601.80 (-3.62%)</td><td>1536.20 (-4.22%)</td><td>159.15 <b>(+277.08%)</b></td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.65 (n/a)</td><td>0.63 (n/a)</td><td>0.63 (n/a)</td><td>0.61 (n/a)</td><td>0.02 (n/a)</td><td>1710.70 (n/a)</td><td>1654.22 (n/a)</td><td>1662.00 (n/a)</td><td>1603.90 (n/a)</td><td>42.20 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>3.72 <b>(+20.32%)</b></td><td>3.12 (+16.02%)</td><td>3.04 (+6.32%)</td><td>2.73 <b>(+32.06%)</b></td><td>0.43 (+8.15%)</td><td>192.20 <b>(-24.30%)</b></td><td>170.32 (-14.26%)</td><td>172.50 (-5.94%)</td><td>141.00 (-16.86%)</td><td>22.57 <b>(-32.31%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>3.09 (n/a)</td><td>2.69 (n/a)</td><td>2.86 (n/a)</td><td>2.07 (n/a)</td><td>0.40 (n/a)</td><td>253.90 (n/a)</td><td>198.64 (n/a)</td><td>183.40 (n/a)</td><td>169.60 (n/a)</td><td>33.34 (n/a)</td>
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
<td><code>16c4ae4</code> — 2026-09-25 00:48:24</td><td>1.01 (+6.07%)</td><td>0.97 (+7.61%)</td><td>0.98 (+12.05%)</td><td>0.89 (+2.46%)</td><td>0.05 (+14.42%)</td><td>588.00 (-2.39%)</td><td>541.38 (-7.04%)</td><td>534.90 (-10.76%)</td><td>517.20 (-5.72%)</td><td>27.74 (+5.59%)</td>
</tr>
<tr>
<td><code>3c46008</code> — 2026-09-24 23:53:02</td><td>0.96 (n/a)</td><td>0.90 (n/a)</td><td>0.87 (n/a)</td><td>0.87 (n/a)</td><td>0.04 (n/a)</td><td>602.40 (n/a)</td><td>582.36 (n/a)</td><td>599.40 (n/a)</td><td>548.60 (n/a)</td><td>26.28 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 23:08:22</td><td>4.36 (+7.95%)</td><td>3.26 (+13.04%)</td><td>3.33 <b>(+22.37%)</b></td><td>2.38 (+18.97%)</td><td>0.79 (-14.92%)</td><td>220.70 (-15.96%)</td><td>168.40 (-14.68%)</td><td>157.40 (-18.28%)</td><td>120.30 (-7.39%)</td><td>40.78 <b>(-34.38%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 17:54:57</td><td>4.04 (n/a)</td><td>2.89 (n/a)</td><td>2.72 (n/a)</td><td>2.00 (n/a)</td><td>0.93 (n/a)</td><td>262.60 (n/a)</td><td>197.38 (n/a)</td><td>192.60 (n/a)</td><td>129.90 (n/a)</td><td>62.14 (n/a)</td>
</tr>
</tbody>
</table>


</details>
