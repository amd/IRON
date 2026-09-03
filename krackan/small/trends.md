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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.09 (-7.83%)</td><td>0.07 (-17.03%)</td><td>0.07 (-13.46%)</td><td>0.06 <b>(-26.84%)</b></td><td>0.01 <b>(+59.08%)</b></td><td>213.10 <b>(+36.69%)</b></td><td>175.88 <b>(+22.39%)</b></td><td>170.10 (+15.56%)</td><td>139.90 (+8.53%)</td><td>28.34 <b>(+137.30%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>155.90 (n/a)</td><td>143.70 (n/a)</td><td>147.20 (n/a)</td><td>128.90 (n/a)</td><td>11.94 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 <b>(-39.00%)</b></td><td>0.07 <b>(-20.15%)</b></td><td>0.06 (-13.12%)</td><td>0.06 (-11.04%)</td><td>0.00 <b>(-79.18%)</b></td><td>194.80 (+12.41%)</td><td>185.18 <b>(+20.97%)</b></td><td>192.30 (+15.08%)</td><td>170.10 <b>(+64.03%)</b></td><td>11.38 <b>(-61.32%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>173.30 (n/a)</td><td>153.08 (n/a)</td><td>167.10 (n/a)</td><td>103.70 (n/a)</td><td>29.43 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.10 <b>(+22.90%)</b></td><td>0.06 (-10.36%)</td><td>0.06 (-15.85%)</td><td>0.04 <b>(-37.96%)</b></td><td>0.02 <b>(+244.43%)</b></td><td>310.80 <b>(+61.20%)</b></td><td>211.02 <b>(+20.29%)</b></td><td>206.50 (+18.88%)</td><td>126.30 (-18.67%)</td><td>65.67 <b>(+340.93%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>192.80 (n/a)</td><td>175.42 (n/a)</td><td>173.70 (n/a)</td><td>155.30 (n/a)</td><td>14.89 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (-9.91%)</td><td>0.05 (-11.30%)</td><td>0.06 (-5.13%)</td><td>0.04 <b>(-26.16%)</b></td><td>0.01 <b>(+51.26%)</b></td><td>308.40 <b>(+35.44%)</b></td><td>231.86 (+14.94%)</td><td>206.90 (+5.40%)</td><td>199.30 (+10.97%)</td><td>46.44 <b>(+124.80%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>227.70 (n/a)</td><td>201.72 (n/a)</td><td>196.30 (n/a)</td><td>179.60 (n/a)</td><td>20.66 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (+1.98%)</td><td>0.03 (-5.06%)</td><td>0.03 (-0.90%)</td><td>0.02 <b>(-23.25%)</b></td><td>0.01 <b>(+117.23%)</b></td><td>245.40 <b>(+30.25%)</b></td><td>191.70 (+7.83%)</td><td>183.90 (+0.93%)</td><td>152.40 (-1.93%)</td><td>36.69 <b>(+183.04%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>188.40 (n/a)</td><td>177.78 (n/a)</td><td>182.20 (n/a)</td><td>155.40 (n/a)</td><td>12.96 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (-19.68%)</td><td>0.03 <b>(-20.62%)</b></td><td>0.03 (-19.55%)</td><td>0.02 (-18.49%)</td><td>0.01 (-2.45%)</td><td>236.00 <b>(+22.66%)</b></td><td>196.56 <b>(+27.27%)</b></td><td>192.30 <b>(+24.31%)</b></td><td>153.80 <b>(+24.53%)</b></td><td>38.23 <b>(+52.05%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>192.40 (n/a)</td><td>154.44 (n/a)</td><td>154.70 (n/a)</td><td>123.50 (n/a)</td><td>25.14 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 <b>(-35.85%)</b></td><td>0.03 <b>(-22.41%)</b></td><td>0.03 (-19.25%)</td><td>0.02 <b>(-32.29%)</b></td><td>0.01 <b>(-41.36%)</b></td><td>292.70 <b>(+47.68%)</b></td><td>207.92 <b>(+27.81%)</b></td><td>204.10 <b>(+23.85%)</b></td><td>160.50 <b>(+55.83%)</b></td><td>51.87 <b>(+43.26%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>198.20 (n/a)</td><td>162.68 (n/a)</td><td>164.80 (n/a)</td><td>103.00 (n/a)</td><td>36.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (-4.91%)</td><td>0.02 <b>(-23.11%)</b></td><td>0.02 <b>(-31.65%)</b></td><td>0.02 <b>(-23.43%)</b></td><td>0.00 <b>(+59.19%)</b></td><td>270.20 <b>(+30.59%)</b></td><td>229.20 <b>(+32.84%)</b></td><td>242.50 <b>(+46.35%)</b></td><td>164.10 (+5.19%)</td><td>41.11 <b>(+107.67%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>206.90 (n/a)</td><td>172.54 (n/a)</td><td>165.70 (n/a)</td><td>156.00 (n/a)</td><td>19.80 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 <b>(+45.50%)</b></td><td>0.03 (-0.20%)</td><td>0.03 (-8.60%)</td><td>0.02 <b>(-23.99%)</b></td><td>0.01 <b>(+245.04%)</b></td><td>258.50 <b>(+31.55%)</b></td><td>191.14 (+7.73%)</td><td>198.10 (+9.39%)</td><td>108.80 <b>(-31.27%)</b></td><td>53.52 <b>(+194.53%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>196.50 (n/a)</td><td>177.42 (n/a)</td><td>181.10 (n/a)</td><td>158.30 (n/a)</td><td>18.17 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (-13.13%)</td><td>0.03 (-0.34%)</td><td>0.03 (+16.84%)</td><td>0.02 <b>(-22.56%)</b></td><td>0.01 (-2.64%)</td><td>311.50 <b>(+29.15%)</b></td><td>201.62 (+2.50%)</td><td>175.40 (-14.40%)</td><td>154.20 (+15.07%)</td><td>62.87 <b>(+61.58%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>241.20 (n/a)</td><td>196.70 (n/a)</td><td>204.90 (n/a)</td><td>134.00 (n/a)</td><td>38.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 <b>(+56.16%)</b></td><td>0.03 (+9.46%)</td><td>0.03 (-9.60%)</td><td>0.02 (+4.41%)</td><td>0.01 <b>(+160.38%)</b></td><td>212.40 (-4.19%)</td><td>178.68 (-2.66%)</td><td>197.20 (+10.60%)</td><td>97.60 <b>(-35.96%)</b></td><td>47.67 <b>(+56.63%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.70 (n/a)</td><td>183.56 (n/a)</td><td>178.30 (n/a)</td><td>152.40 (n/a)</td><td>30.43 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (+10.73%)</td><td>0.03 (+16.94%)</td><td>0.03 (+12.39%)</td><td>0.02 <b>(+40.76%)</b></td><td>0.00 <b>(-36.24%)</b></td><td>232.10 <b>(-28.96%)</b></td><td>209.26 (-17.14%)</td><td>209.90 (-11.02%)</td><td>171.70 (-9.73%)</td><td>23.50 <b>(-60.07%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>326.70 (n/a)</td><td>252.56 (n/a)</td><td>235.90 (n/a)</td><td>190.20 (n/a)</td><td>58.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.40 (n/a)</td><td>164.88 (n/a)</td><td>161.10 (n/a)</td><td>145.50 (n/a)</td><td>19.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>230.90 (n/a)</td><td>179.18 (n/a)</td><td>173.60 (n/a)</td><td>139.80 (n/a)</td><td>34.00 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>198.50 (n/a)</td><td>204.90 (n/a)</td><td>177.00 (n/a)</td><td>18.40 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>223.30 (n/a)</td><td>196.66 (n/a)</td><td>189.00 (n/a)</td><td>179.80 (n/a)</td><td>19.36 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>170.94 (n/a)</td><td>165.30 (n/a)</td><td>143.60 (n/a)</td><td>23.87 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.80 (n/a)</td><td>184.82 (n/a)</td><td>189.20 (n/a)</td><td>142.20 (n/a)</td><td>31.86 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.40 (n/a)</td><td>167.28 (n/a)</td><td>170.20 (n/a)</td><td>144.10 (n/a)</td><td>22.32 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>302.00 (n/a)</td><td>197.14 (n/a)</td><td>183.70 (n/a)</td><td>134.90 (n/a)</td><td>65.05 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.20 (n/a)</td><td>156.98 (n/a)</td><td>153.50 (n/a)</td><td>108.60 (n/a)</td><td>31.69 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>166.24 (n/a)</td><td>157.60 (n/a)</td><td>136.00 (n/a)</td><td>29.03 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>182.10 (n/a)</td><td>203.80 (n/a)</td><td>139.80 (n/a)</td><td>35.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>263.20 (n/a)</td><td>189.24 (n/a)</td><td>171.60 (n/a)</td><td>163.10 (n/a)</td><td>41.76 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.90 (n/a)</td><td>173.02 (n/a)</td><td>171.10 (n/a)</td><td>141.10 (n/a)</td><td>26.75 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.00 (n/a)</td><td>180.54 (n/a)</td><td>180.80 (n/a)</td><td>172.50 (n/a)</td><td>7.35 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.60 (n/a)</td><td>181.76 (n/a)</td><td>174.20 (n/a)</td><td>167.50 (n/a)</td><td>17.89 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.00 (n/a)</td><td>211.14 (n/a)</td><td>222.90 (n/a)</td><td>167.80 (n/a)</td><td>31.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>4.15 (-1.57%)</td><td>3.92 (+0.51%)</td><td>3.87 (-6.11%)</td><td>3.63 (+11.81%)</td><td>0.21 <b>(-48.18%)</b></td><td>2594.20 (-10.57%)</td><td>2406.08 (-1.24%)</td><td>2431.20 (+6.51%)</td><td>2267.10 (+1.59%)</td><td>132.49 <b>(-53.12%)</b></td><td>1631.75 (-1.57%)</td><td>1541.20 (+0.51%)</td><td>1521.63 (-6.11%)</td><td>1426.00 (+11.81%)</td><td>83.83 <b>(-48.18%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>4.21 (n/a)</td><td>3.90 (n/a)</td><td>4.12 (n/a)</td><td>3.24 (n/a)</td><td>0.41 (n/a)</td><td>2900.70 (n/a)</td><td>2436.38 (n/a)</td><td>2282.70 (n/a)</td><td>2231.60 (n/a)</td><td>282.60 (n/a)</td><td>1657.75 (n/a)</td><td>1533.37 (n/a)</td><td>1620.60 (n/a)</td><td>1275.34 (n/a)</td><td>161.76 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.00 (-2.25%)</td><td>0.83 (+9.07%)</td><td>0.85 <b>(+24.84%)</b></td><td>0.65 (+2.62%)</td><td>0.16 (+5.84%)</td><td>339.40 (-2.56%)</td><td>275.92 (-7.92%)</td><td>259.30 (-19.89%)</td><td>221.60 (+2.26%)</td><td>56.72 (+8.84%)</td><td>42.58 (-2.25%)</td><td>35.35 (+9.07%)</td><td>36.39 <b>(+24.84%)</b></td><td>27.80 (+2.62%)</td><td>7.04 (+5.84%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.02 (n/a)</td><td>0.76 (n/a)</td><td>0.68 (n/a)</td><td>0.64 (n/a)</td><td>0.16 (n/a)</td><td>348.30 (n/a)</td><td>299.66 (n/a)</td><td>323.70 (n/a)</td><td>216.70 (n/a)</td><td>52.12 (n/a)</td><td>43.56 (n/a)</td><td>32.41 (n/a)</td><td>29.15 (n/a)</td><td>27.09 (n/a)</td><td>6.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.09 (+10.37%)</td><td>1.00 (+18.45%)</td><td>1.00 <b>(+25.50%)</b></td><td>0.86 <b>(+24.13%)</b></td><td>0.09 <b>(-27.18%)</b></td><td>258.20 (-19.44%)</td><td>223.04 (-16.54%)</td><td>221.50 <b>(-20.32%)</b></td><td>202.60 (-9.39%)</td><td>22.39 <b>(-45.50%)</b></td><td>46.57 (+10.37%)</td><td>42.63 (+18.45%)</td><td>42.60 <b>(+25.50%)</b></td><td>36.55 <b>(+24.13%)</b></td><td>4.05 <b>(-27.18%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.99 (n/a)</td><td>0.84 (n/a)</td><td>0.80 (n/a)</td><td>0.69 (n/a)</td><td>0.13 (n/a)</td><td>320.50 (n/a)</td><td>267.24 (n/a)</td><td>278.00 (n/a)</td><td>223.60 (n/a)</td><td>41.09 (n/a)</td><td>42.20 (n/a)</td><td>35.99 (n/a)</td><td>33.94 (n/a)</td><td>29.44 (n/a)</td><td>5.56 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.52 (+0.02%)</td><td>0.52 (+0.08%)</td><td>0.52 (+0.03%)</td><td>0.52 (+0.25%)</td><td>0.00 <b>(-57.31%)</b></td><td>48535.20 (-0.25%)</td><td>48473.32 (-0.08%)</td><td>48463.30 (-0.03%)</td><td>48442.50 (-0.02%)</td><td>35.93 <b>(-57.42%)</b></td><td>354.64 (+0.02%)</td><td>354.42 (+0.08%)</td><td>354.49 (+0.03%)</td><td>353.97 (+0.25%)</td><td>0.26 <b>(-57.31%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.00 (n/a)</td><td>48658.90 (n/a)</td><td>48511.92 (n/a)</td><td>48478.30 (n/a)</td><td>48453.30 (n/a)</td><td>84.38 (n/a)</td><td>354.57 (n/a)</td><td>354.14 (n/a)</td><td>354.38 (n/a)</td><td>353.07 (n/a)</td><td>0.61 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.91 (+0.53%)</td><td>0.89 (+0.13%)</td><td>0.89 (+0.31%)</td><td>0.88 (-0.42%)</td><td>0.01 <b>(+45.00%)</b></td><td>28553.10 (+0.43%)</td><td>28207.40 (-0.13%)</td><td>28226.60 (-0.31%)</td><td>27795.20 (-0.53%)</td><td>276.21 <b>(+44.85%)</b></td><td>618.09 (+0.53%)</td><td>609.10 (+0.13%)</td><td>608.64 (+0.31%)</td><td>601.68 (-0.42%)</td><td>5.98 <b>(+45.00%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.89 (n/a)</td><td>0.01 (n/a)</td><td>28432.00 (n/a)</td><td>28243.24 (n/a)</td><td>28313.00 (n/a)</td><td>27941.90 (n/a)</td><td>190.69 (n/a)</td><td>614.84 (n/a)</td><td>608.31 (n/a)</td><td>606.78 (n/a)</td><td>604.24 (n/a)</td><td>4.13 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>3.28 (-2.21%)</td><td>3.19 (-1.59%)</td><td>3.18 (-0.59%)</td><td>3.15 (-0.18%)</td><td>0.05 <b>(-45.98%)</b></td><td>7992.20 (+0.19%)</td><td>7887.64 (+1.57%)</td><td>7925.60 (+0.59%)</td><td>7672.10 (+2.26%)</td><td>125.87 <b>(-44.70%)</b></td><td>2239.28 (-2.21%)</td><td>2178.54 (-1.59%)</td><td>2167.65 (-0.59%)</td><td>2149.59 (-0.18%)</td><td>35.37 <b>(-45.98%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>3.35 (n/a)</td><td>3.24 (n/a)</td><td>3.19 (n/a)</td><td>3.15 (n/a)</td><td>0.10 (n/a)</td><td>7977.40 (n/a)</td><td>7766.06 (n/a)</td><td>7878.80 (n/a)</td><td>7502.80 (n/a)</td><td>227.60 (n/a)</td><td>2289.79 (n/a)</td><td>2213.71 (n/a)</td><td>2180.52 (n/a)</td><td>2153.56 (n/a)</td><td>65.48 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>3.76 (-3.04%)</td><td>3.47 (-6.06%)</td><td>3.55 (-5.88%)</td><td>3.05 (-7.50%)</td><td>0.26 (+10.06%)</td><td>2640.00 (+8.10%)</td><td>2333.66 (+6.59%)</td><td>2269.40 (+6.25%)</td><td>2143.20 (+3.13%)</td><td>186.78 <b>(+24.16%)</b></td><td>986.33 (-3.04%)</td><td>910.24 (-6.06%)</td><td>931.50 (-5.88%)</td><td>800.74 (-7.50%)</td><td>68.80 (+10.06%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>3.88 (n/a)</td><td>3.69 (n/a)</td><td>3.77 (n/a)</td><td>3.30 (n/a)</td><td>0.24 (n/a)</td><td>2442.10 (n/a)</td><td>2189.38 (n/a)</td><td>2136.00 (n/a)</td><td>2078.20 (n/a)</td><td>150.44 (n/a)</td><td>1017.21 (n/a)</td><td>968.98 (n/a)</td><td>989.69 (n/a)</td><td>865.62 (n/a)</td><td>62.51 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.35 (-10.03%)</td><td>0.32 (-6.01%)</td><td>0.33 (-1.05%)</td><td>0.28 (-15.12%)</td><td>0.03 (+19.84%)</td><td>4516.00 (+17.82%)</td><td>3890.14 (+6.79%)</td><td>3732.50 (+1.06%)</td><td>3565.60 (+11.15%)</td><td>399.35 <b>(+57.66%)</b></td><td>18.82 (-10.03%)</td><td>17.39 (-6.01%)</td><td>17.98 (-1.05%)</td><td>14.86 (-15.12%)</td><td>1.67 (+19.84%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.03 (n/a)</td><td>3833.10 (n/a)</td><td>3642.80 (n/a)</td><td>3693.30 (n/a)</td><td>3207.80 (n/a)</td><td>253.29 (n/a)</td><td>20.92 (n/a)</td><td>18.50 (n/a)</td><td>18.17 (n/a)</td><td>17.51 (n/a)</td><td>1.39 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>4.83 <b>(-21.57%)</b></td><td>3.98 (-10.64%)</td><td>3.57 (-19.60%)</td><td>3.28 (+0.30%)</td><td>0.75 <b>(-34.62%)</b></td><td>2030.50 (-0.30%)</td><td>1717.00 (+9.32%)</td><td>1863.00 <b>(+24.37%)</b></td><td>1377.40 <b>(+27.50%)</b></td><td>306.22 <b>(-20.04%)</b></td><td>1492.11 <b>(-21.57%)</b></td><td>1229.91 (-10.64%)</td><td>1103.18 (-19.60%)</td><td>1012.15 (+0.30%)</td><td>231.21 <b>(-34.62%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>6.16 (n/a)</td><td>4.45 (n/a)</td><td>4.44 (n/a)</td><td>3.27 (n/a)</td><td>1.14 (n/a)</td><td>2036.70 (n/a)</td><td>1570.56 (n/a)</td><td>1497.90 (n/a)</td><td>1080.30 (n/a)</td><td>382.96 (n/a)</td><td>1902.40 (n/a)</td><td>1376.29 (n/a)</td><td>1372.05 (n/a)</td><td>1009.11 (n/a)</td><td>353.63 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>13.26 (n/a)</td><td>12.80 (n/a)</td><td>12.58 (n/a)</td><td>12.43 (n/a)</td><td>0.38 (n/a)</td><td>13.25 (n/a)</td><td>12.79 (n/a)</td><td>12.58 (n/a)</td><td>12.43 (n/a)</td><td>0.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>24.42 (+0.72%)</td><td>24.02 (+1.20%)</td><td>24.08 (+0.82%)</td><td>23.63 (+2.27%)</td><td>0.29 <b>(-46.48%)</b></td><td>24.40 (+0.72%)</td><td>24.01 (+1.20%)</td><td>24.07 (+0.82%)</td><td>23.62 (+2.27%)</td><td>0.29 <b>(-46.47%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>24.24 (n/a)</td><td>23.74 (n/a)</td><td>23.89 (n/a)</td><td>23.11 (n/a)</td><td>0.54 (n/a)</td><td>24.23 (n/a)</td><td>23.72 (n/a)</td><td>23.87 (n/a)</td><td>23.09 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>41.06 (-1.71%)</td><td>39.63 (+0.27%)</td><td>39.51 (-4.01%)</td><td>38.11 (+7.21%)</td><td>1.13 <b>(-60.75%)</b></td><td>41.04 (-1.71%)</td><td>39.61 (+0.27%)</td><td>39.48 (-4.01%)</td><td>38.09 (+7.21%)</td><td>1.13 <b>(-60.75%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>41.78 (n/a)</td><td>39.53 (n/a)</td><td>41.16 (n/a)</td><td>35.55 (n/a)</td><td>2.87 (n/a)</td><td>41.75 (n/a)</td><td>39.50 (n/a)</td><td>41.13 (n/a)</td><td>35.53 (n/a)</td><td>2.87 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>43.75 (-3.57%)</td><td>41.38 (-4.23%)</td><td>41.97 (-5.73%)</td><td>37.10 (+0.26%)</td><td>2.52 <b>(-28.02%)</b></td><td>43.72 (-3.57%)</td><td>41.36 (-4.23%)</td><td>41.94 (-5.73%)</td><td>37.08 (+0.26%)</td><td>2.51 <b>(-28.02%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>45.37 (n/a)</td><td>43.21 (n/a)</td><td>44.52 (n/a)</td><td>37.00 (n/a)</td><td>3.50 (n/a)</td><td>45.34 (n/a)</td><td>43.19 (n/a)</td><td>44.49 (n/a)</td><td>36.98 (n/a)</td><td>3.49 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>13.33 (n/a)</td><td>12.16 (n/a)</td><td>12.09 (n/a)</td><td>11.07 (n/a)</td><td>1.05 (n/a)</td><td>13.32 (n/a)</td><td>12.15 (n/a)</td><td>12.09 (n/a)</td><td>11.07 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>24.79 (-0.47%)</td><td>24.12 (-0.93%)</td><td>24.34 (-0.25%)</td><td>22.98 (-2.03%)</td><td>0.71 <b>(+29.01%)</b></td><td>24.77 (-0.47%)</td><td>24.11 (-0.93%)</td><td>24.33 (-0.25%)</td><td>22.97 (-2.03%)</td><td>0.71 <b>(+29.01%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>24.90 (n/a)</td><td>24.35 (n/a)</td><td>24.40 (n/a)</td><td>23.46 (n/a)</td><td>0.55 (n/a)</td><td>24.89 (n/a)</td><td>24.33 (n/a)</td><td>24.39 (n/a)</td><td>23.45 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>42.51 (+1.47%)</td><td>40.23 (+10.05%)</td><td>39.90 (-3.39%)</td><td>38.85 <b>(+66.78%)</b></td><td>1.37 <b>(-82.82%)</b></td><td>42.49 (+1.47%)</td><td>40.20 (+10.05%)</td><td>39.87 (-3.39%)</td><td>38.82 <b>(+66.78%)</b></td><td>1.37 <b>(-82.82%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>41.90 (n/a)</td><td>36.55 (n/a)</td><td>41.30 (n/a)</td><td>23.29 (n/a)</td><td>7.98 (n/a)</td><td>41.87 (n/a)</td><td>36.53 (n/a)</td><td>41.27 (n/a)</td><td>23.28 (n/a)</td><td>7.98 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>45.66 (+0.38%)</td><td>41.91 (-3.58%)</td><td>41.92 (-6.45%)</td><td>38.19 (-4.48%)</td><td>2.65 (+7.50%)</td><td>45.64 (+0.38%)</td><td>41.89 (-3.58%)</td><td>41.89 (-6.45%)</td><td>38.16 (-4.48%)</td><td>2.65 (+7.50%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>45.49 (n/a)</td><td>43.47 (n/a)</td><td>44.80 (n/a)</td><td>39.98 (n/a)</td><td>2.47 (n/a)</td><td>45.46 (n/a)</td><td>43.44 (n/a)</td><td>44.78 (n/a)</td><td>39.95 (n/a)</td><td>2.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>9.25 (-3.54%)</td><td>8.87 (+2.68%)</td><td>9.00 (+0.19%)</td><td>8.29 (+17.46%)</td><td>0.38 <b>(-60.81%)</b></td><td>9.23 (-3.54%)</td><td>8.85 (+2.68%)</td><td>8.99 (+0.19%)</td><td>8.27 (+17.46%)</td><td>0.38 <b>(-60.81%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>9.59 (n/a)</td><td>8.64 (n/a)</td><td>8.99 (n/a)</td><td>7.06 (n/a)</td><td>0.97 (n/a)</td><td>9.57 (n/a)</td><td>8.62 (n/a)</td><td>8.97 (n/a)</td><td>7.04 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.92 (-4.77%)</td><td>0.87 (-2.97%)</td><td>0.87 (-3.80%)</td><td>0.79 (-2.58%)</td><td>0.05 (-14.27%)</td><td>0.91 (-4.77%)</td><td>0.86 (-2.97%)</td><td>0.86 (-3.80%)</td><td>0.78 (-2.58%)</td><td>0.05 (-14.27%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.97 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.81 (n/a)</td><td>0.06 (n/a)</td><td>0.95 (n/a)</td><td>0.88 (n/a)</td><td>0.89 (n/a)</td><td>0.80 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.33 (-11.54%)</td><td>1.13 (-9.22%)</td><td>1.14 (-7.88%)</td><td>1.01 (-1.68%)</td><td>0.13 <b>(-41.54%)</b></td><td>1.31 (-11.54%)</td><td>1.12 (-9.22%)</td><td>1.13 (-7.88%)</td><td>0.99 (-1.68%)</td><td>0.13 <b>(-41.54%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.50 (n/a)</td><td>1.25 (n/a)</td><td>1.24 (n/a)</td><td>1.02 (n/a)</td><td>0.22 (n/a)</td><td>1.48 (n/a)</td><td>1.23 (n/a)</td><td>1.23 (n/a)</td><td>1.01 (n/a)</td><td>0.22 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>17.92 (-1.90%)</td><td>16.80 (+6.95%)</td><td>16.33 (-1.17%)</td><td>16.02 <b>(+23.60%)</b></td><td>0.89 <b>(-60.24%)</b></td><td>17.72 (-1.90%)</td><td>16.60 (+6.95%)</td><td>16.15 (-1.17%)</td><td>15.84 <b>(+23.60%)</b></td><td>0.88 <b>(-60.24%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>18.27 (n/a)</td><td>15.71 (n/a)</td><td>16.53 (n/a)</td><td>12.96 (n/a)</td><td>2.24 (n/a)</td><td>18.06 (n/a)</td><td>15.52 (n/a)</td><td>16.34 (n/a)</td><td>12.81 (n/a)</td><td>2.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>14.15 (+1.86%)</td><td>13.20 (-2.91%)</td><td>13.36 (-3.10%)</td><td>11.72 (-11.16%)</td><td>0.91 <b>(+183.09%)</b></td><td>13.90 (+1.86%)</td><td>12.97 (-2.91%)</td><td>13.12 (-3.10%)</td><td>11.52 (-11.16%)</td><td>0.89 <b>(+183.09%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>13.89 (n/a)</td><td>13.60 (n/a)</td><td>13.78 (n/a)</td><td>13.19 (n/a)</td><td>0.32 (n/a)</td><td>13.64 (n/a)</td><td>13.36 (n/a)</td><td>13.54 (n/a)</td><td>12.96 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>8.43 (-7.37%)</td><td>8.06 (+1.37%)</td><td>8.13 (+4.58%)</td><td>7.47 (+10.76%)</td><td>0.36 <b>(-59.91%)</b></td><td>8.29 (-7.37%)</td><td>7.92 (+1.37%)</td><td>7.99 (+4.58%)</td><td>7.34 (+10.76%)</td><td>0.35 <b>(-59.91%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>9.10 (n/a)</td><td>7.95 (n/a)</td><td>7.78 (n/a)</td><td>6.74 (n/a)</td><td>0.89 (n/a)</td><td>8.95 (n/a)</td><td>7.81 (n/a)</td><td>7.64 (n/a)</td><td>6.63 (n/a)</td><td>0.88 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>5.98 (-0.79%)</td><td>5.61 (-0.73%)</td><td>5.63 (+2.06%)</td><td>5.29 (-1.22%)</td><td>0.26 (-14.46%)</td><td>5.89 (-0.79%)</td><td>5.52 (-0.73%)</td><td>5.54 (+2.06%)</td><td>5.20 (-1.22%)</td><td>0.26 (-14.46%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>6.03 (n/a)</td><td>5.65 (n/a)</td><td>5.51 (n/a)</td><td>5.35 (n/a)</td><td>0.31 (n/a)</td><td>5.94 (n/a)</td><td>5.56 (n/a)</td><td>5.42 (n/a)</td><td>5.26 (n/a)</td><td>0.30 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>13.37 (n/a)</td><td>12.50 (n/a)</td><td>12.62 (n/a)</td><td>11.63 (n/a)</td><td>0.75 (n/a)</td><td>13.36 (n/a)</td><td>12.50 (n/a)</td><td>12.61 (n/a)</td><td>11.62 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>13.60 (n/a)</td><td>13.25 (n/a)</td><td>13.34 (n/a)</td><td>12.69 (n/a)</td><td>0.34 (n/a)</td><td>13.59 (n/a)</td><td>13.24 (n/a)</td><td>13.33 (n/a)</td><td>12.68 (n/a)</td><td>0.34 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.50 (n/a)</td><td>157.84 (n/a)</td><td>167.30 (n/a)</td><td>123.50 (n/a)</td><td>22.00 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.90 (n/a)</td><td>170.98 (n/a)</td><td>168.80 (n/a)</td><td>147.00 (n/a)</td><td>22.89 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.60 (n/a)</td><td>163.98 (n/a)</td><td>145.40 (n/a)</td><td>123.10 (n/a)</td><td>39.54 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>199.10 (n/a)</td><td>177.00 (n/a)</td><td>176.30 (n/a)</td><td>153.30 (n/a)</td><td>17.37 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.20 (n/a)</td><td>169.76 (n/a)</td><td>168.60 (n/a)</td><td>136.30 (n/a)</td><td>29.06 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>195.00 (n/a)</td><td>187.34 (n/a)</td><td>192.70 (n/a)</td><td>169.20 (n/a)</td><td>10.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.40 (n/a)</td><td>194.16 (n/a)</td><td>197.00 (n/a)</td><td>179.20 (n/a)</td><td>11.77 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.30 (n/a)</td><td>214.00 (n/a)</td><td>217.70 (n/a)</td><td>168.50 (n/a)</td><td>28.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 <b>(+23.14%)</b></td><td>0.05 (+2.63%)</td><td>0.04 (-8.27%)</td><td>0.04 (+0.11%)</td><td>0.01 <b>(+120.94%)</b></td><td>201.80 (-0.10%)</td><td>182.08 (-1.32%)</td><td>191.90 (+9.03%)</td><td>140.30 (-18.81%)</td><td>24.54 <b>(+75.84%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>202.00 (n/a)</td><td>184.52 (n/a)</td><td>176.00 (n/a)</td><td>172.80 (n/a)</td><td>13.96 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (+1.68%)</td><td>0.05 (-5.95%)</td><td>0.04 (-13.27%)</td><td>0.04 (-10.74%)</td><td>0.01 <b>(+33.75%)</b></td><td>212.50 (+12.02%)</td><td>181.84 (+7.17%)</td><td>188.30 (+15.31%)</td><td>144.60 (-1.63%)</td><td>25.12 <b>(+42.73%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>169.68 (n/a)</td><td>163.30 (n/a)</td><td>147.00 (n/a)</td><td>17.60 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 <b>(-26.52%)</b></td><td>0.05 (-15.31%)</td><td>0.05 (-9.48%)</td><td>0.04 (-3.45%)</td><td>0.00 <b>(-81.25%)</b></td><td>185.10 (+3.58%)</td><td>174.82 (+15.94%)</td><td>171.90 (+10.48%)</td><td>169.60 <b>(+36.12%)</b></td><td>6.24 <b>(-73.00%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.70 (n/a)</td><td>150.78 (n/a)</td><td>155.60 (n/a)</td><td>124.60 (n/a)</td><td>23.11 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (+14.02%)</td><td>0.05 <b>(+23.58%)</b></td><td>0.05 (+12.69%)</td><td>0.05 <b>(+57.28%)</b></td><td>0.01 <b>(-22.73%)</b></td><td>181.30 <b>(-36.41%)</b></td><td>155.64 <b>(-22.20%)</b></td><td>159.90 (-11.22%)</td><td>129.70 (-12.31%)</td><td>24.46 <b>(-57.30%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>285.10 (n/a)</td><td>200.04 (n/a)</td><td>180.10 (n/a)</td><td>147.90 (n/a)</td><td>57.28 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.08 <b>(+50.66%)</b></td><td>0.05 <b>(+20.42%)</b></td><td>0.05 (+10.30%)</td><td>0.04 (+15.22%)</td><td>0.01 <b>(+204.03%)</b></td><td>182.60 (-13.21%)</td><td>159.12 (-14.53%)</td><td>170.90 (-9.34%)</td><td>107.80 <b>(-33.66%)</b></td><td>29.54 <b>(+69.01%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.40 (n/a)</td><td>186.16 (n/a)</td><td>188.50 (n/a)</td><td>162.50 (n/a)</td><td>17.48 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 <b>(+48.06%)</b></td><td>0.05 (+13.21%)</td><td>0.04 (-3.71%)</td><td>0.04 <b>(+20.28%)</b></td><td>0.01 <b>(+134.89%)</b></td><td>198.70 (-16.86%)</td><td>172.48 (-9.12%)</td><td>188.80 (+3.85%)</td><td>112.90 <b>(-32.48%)</b></td><td>35.20 <b>(+24.93%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>239.00 (n/a)</td><td>189.78 (n/a)</td><td>181.80 (n/a)</td><td>167.20 (n/a)</td><td>28.18 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 <b>(+28.99%)</b></td><td>0.05 <b>(+25.08%)</b></td><td>0.04 (-3.83%)</td><td>0.04 <b>(+83.30%)</b></td><td>0.01 (-9.30%)</td><td>204.20 <b>(-45.46%)</b></td><td>166.50 <b>(-25.00%)</b></td><td>182.20 (+4.00%)</td><td>124.80 <b>(-22.44%)</b></td><td>33.85 <b>(-62.32%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>374.40 (n/a)</td><td>222.00 (n/a)</td><td>175.20 (n/a)</td><td>160.90 (n/a)</td><td>89.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (+14.80%)</td><td>0.05 (+15.83%)</td><td>0.05 (+16.50%)</td><td>0.04 (+16.87%)</td><td>0.01 (+9.49%)</td><td>204.00 (-14.43%)</td><td>176.86 (-13.89%)</td><td>174.30 (-14.14%)</td><td>134.90 (-12.86%)</td><td>27.27 (-19.31%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.40 (n/a)</td><td>205.40 (n/a)</td><td>203.00 (n/a)</td><td>154.80 (n/a)</td><td>33.80 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (+11.43%)</td><td>0.05 (+5.87%)</td><td>0.04 (+4.39%)</td><td>0.04 (-2.87%)</td><td>0.01 <b>(+67.94%)</b></td><td>214.70 (+2.97%)</td><td>179.64 (-4.51%)</td><td>186.90 (-4.20%)</td><td>148.40 (-10.28%)</td><td>26.67 <b>(+54.27%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>208.50 (n/a)</td><td>188.12 (n/a)</td><td>195.10 (n/a)</td><td>165.40 (n/a)</td><td>17.28 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.04 (-2.65%)</td><td>0.04 (-1.56%)</td><td>0.04 (-4.18%)</td><td>0.04 (+6.96%)</td><td>0.00 <b>(-21.96%)</b></td><td>221.60 (-6.50%)</td><td>210.62 (+1.28%)</td><td>216.20 (+4.34%)</td><td>185.60 (+2.71%)</td><td>14.93 <b>(-25.14%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>237.00 (n/a)</td><td>207.96 (n/a)</td><td>207.20 (n/a)</td><td>180.70 (n/a)</td><td>19.94 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 <b>(+26.77%)</b></td><td>0.06 <b>(+25.38%)</b></td><td>0.06 (+17.92%)</td><td>0.05 <b>(+45.16%)</b></td><td>0.01 <b>(-20.60%)</b></td><td>158.50 <b>(-31.12%)</b></td><td>144.86 <b>(-22.25%)</b></td><td>148.40 (-15.20%)</td><td>115.70 <b>(-21.08%)</b></td><td>16.99 <b>(-58.62%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>186.32 (n/a)</td><td>175.00 (n/a)</td><td>146.60 (n/a)</td><td>41.07 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (+16.87%)</td><td>0.04 (+19.52%)</td><td>0.05 <b>(+25.33%)</b></td><td>0.04 (+19.73%)</td><td>0.00 <b>(+30.48%)</b></td><td>202.30 (-16.51%)</td><td>184.18 (-16.28%)</td><td>176.60 <b>(-20.23%)</b></td><td>172.50 (-14.43%)</td><td>13.97 (-7.45%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>242.30 (n/a)</td><td>220.00 (n/a)</td><td>221.40 (n/a)</td><td>201.60 (n/a)</td><td>15.09 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.08 <b>(+34.76%)</b></td><td>0.06 <b>(+30.79%)</b></td><td>0.05 <b>(+22.40%)</b></td><td>0.05 <b>(+47.42%)</b></td><td>0.01 <b>(+27.04%)</b></td><td>172.70 <b>(-32.17%)</b></td><td>146.76 <b>(-24.21%)</b></td><td>151.70 (-18.31%)</td><td>101.40 <b>(-25.77%)</b></td><td>26.91 <b>(-38.72%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>254.60 (n/a)</td><td>193.64 (n/a)</td><td>185.70 (n/a)</td><td>136.60 (n/a)</td><td>43.92 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (+14.39%)</td><td>0.05 (-1.66%)</td><td>0.05 (-1.15%)</td><td>0.04 (-19.71%)</td><td>0.01 <b>(+84.75%)</b></td><td>227.40 <b>(+24.53%)</b></td><td>176.08 (+6.12%)</td><td>178.00 (+1.14%)</td><td>112.30 (-12.54%)</td><td>44.23 <b>(+99.89%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.60 (n/a)</td><td>165.92 (n/a)</td><td>176.00 (n/a)</td><td>128.40 (n/a)</td><td>22.12 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (-6.66%)</td><td>0.05 (+13.06%)</td><td>0.05 <b>(+21.77%)</b></td><td>0.05 (+16.24%)</td><td>0.01 <b>(-48.06%)</b></td><td>175.80 (-13.95%)</td><td>154.12 (-13.61%)</td><td>156.70 (-17.87%)</td><td>135.80 (+7.10%)</td><td>15.44 <b>(-52.00%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.30 (n/a)</td><td>178.40 (n/a)</td><td>190.80 (n/a)</td><td>126.80 (n/a)</td><td>32.16 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (+5.14%)</td><td>0.05 (+16.91%)</td><td>0.05 <b>(+48.63%)</b></td><td>0.04 <b>(+22.84%)</b></td><td>0.01 (-16.88%)</td><td>231.70 (-18.59%)</td><td>172.18 (-17.55%)</td><td>156.50 <b>(-32.75%)</b></td><td>124.40 (-4.89%)</td><td>42.48 <b>(-33.25%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>284.60 (n/a)</td><td>208.82 (n/a)</td><td>232.70 (n/a)</td><td>130.80 (n/a)</td><td>63.63 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (+8.26%)</td><td>0.05 (+8.17%)</td><td>0.05 (+5.93%)</td><td>0.04 (+12.14%)</td><td>0.01 (-2.64%)</td><td>196.20 (-10.86%)</td><td>161.48 (-8.45%)</td><td>166.70 (-5.61%)</td><td>117.00 (-7.66%)</td><td>29.22 <b>(-22.53%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.10 (n/a)</td><td>176.38 (n/a)</td><td>176.60 (n/a)</td><td>126.70 (n/a)</td><td>37.72 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (+8.16%)</td><td>0.05 <b>(+26.01%)</b></td><td>0.05 <b>(+38.95%)</b></td><td>0.04 <b>(+45.65%)</b></td><td>0.01 <b>(-44.31%)</b></td><td>188.80 <b>(-31.35%)</b></td><td>163.90 <b>(-23.75%)</b></td><td>158.20 <b>(-28.03%)</b></td><td>145.90 (-7.54%)</td><td>18.85 <b>(-64.19%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>275.00 (n/a)</td><td>214.96 (n/a)</td><td>219.80 (n/a)</td><td>157.80 (n/a)</td><td>52.64 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mha</summary>


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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.18 (+0.90%)</td><td>0.18 (+0.25%)</td><td>0.18 (+0.03%)</td><td>0.18 (+0.02%)</td><td>0.00 <b>(+174.79%)</b></td><td>47542.10 (-0.02%)</td><td>47332.68 (-0.24%)</td><td>47396.40 (-0.03%)</td><td>46945.00 (-0.89%)</td><td>232.83 <b>(+172.04%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47550.70 (n/a)</td><td>47448.00 (n/a)</td><td>47409.70 (n/a)</td><td>47367.40 (n/a)</td><td>85.59 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.19 (-7.43%)</td><td>0.15 (-17.69%)</td><td>0.16 (-11.98%)</td><td>0.10 <b>(-38.09%)</b></td><td>0.03 <b>(+87.60%)</b></td><td>243.20 <b>(+61.49%)</b></td><td>173.06 <b>(+26.36%)</b></td><td>156.40 (+13.58%)</td><td>128.40 (+7.99%)</td><td>44.43 <b>(+231.28%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>150.60 (n/a)</td><td>136.96 (n/a)</td><td>137.70 (n/a)</td><td>118.90 (n/a)</td><td>13.41 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.33 (+0.84%)</td><td>0.25 (-14.81%)</td><td>0.24 (-15.36%)</td><td>0.19 <b>(-20.15%)</b></td><td>0.05 <b>(+48.18%)</b></td><td>211.70 <b>(+25.27%)</b></td><td>171.64 (+19.56%)</td><td>169.60 (+18.11%)</td><td>124.90 (-0.79%)</td><td>31.29 <b>(+80.05%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.03 (n/a)</td><td>169.00 (n/a)</td><td>143.56 (n/a)</td><td>143.60 (n/a)</td><td>125.90 (n/a)</td><td>17.38 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.04 (-12.93%)</td><td>0.03 (-15.95%)</td><td>0.03 <b>(-25.00%)</b></td><td>0.03 (-12.93%)</td><td>0.00 (-12.34%)</td><td>194.60 (+14.88%)</td><td>165.16 (+18.99%)</td><td>169.80 <b>(+33.39%)</b></td><td>138.70 (+14.91%)</td><td>23.37 (+13.73%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>169.40 (n/a)</td><td>138.80 (n/a)</td><td>127.30 (n/a)</td><td>120.70 (n/a)</td><td>20.55 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 <b>(-24.79%)</b></td><td>0.05 (-8.53%)</td><td>0.06 (+15.84%)</td><td>0.03 <b>(-39.35%)</b></td><td>0.01 (-15.51%)</td><td>296.20 <b>(+64.92%)</b></td><td>175.30 (+13.26%)</td><td>148.00 (-13.65%)</td><td>125.50 <b>(+32.94%)</b></td><td>69.81 <b>(+95.80%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>179.60 (n/a)</td><td>154.78 (n/a)</td><td>171.40 (n/a)</td><td>94.40 (n/a)</td><td>35.65 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.11 <b>(+24.83%)</b></td><td>0.08 (+15.52%)</td><td>0.07 (-1.80%)</td><td>0.06 <b>(+27.48%)</b></td><td>0.02 (+10.17%)</td><td>214.70 <b>(-21.53%)</b></td><td>161.32 (-14.81%)</td><td>165.00 (+1.85%)</td><td>111.50 (-19.90%)</td><td>38.44 <b>(-31.89%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>273.60 (n/a)</td><td>189.36 (n/a)</td><td>162.00 (n/a)</td><td>139.20 (n/a)</td><td>56.43 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (-17.36%)</td><td>0.04 (-13.28%)</td><td>0.05 (-4.38%)</td><td>0.02 <b>(-41.76%)</b></td><td>0.01 <b>(+31.58%)</b></td><td>328.00 <b>(+71.73%)</b></td><td>198.26 <b>(+22.04%)</b></td><td>171.50 (+4.57%)</td><td>152.10 <b>(+21.00%)</b></td><td>73.11 <b>(+192.84%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.00 (n/a)</td><td>162.46 (n/a)</td><td>164.00 (n/a)</td><td>125.70 (n/a)</td><td>24.97 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (+8.59%)</td><td>0.06 (-8.45%)</td><td>0.05 (-13.22%)</td><td>0.05 (-14.00%)</td><td>0.01 <b>(+84.99%)</b></td><td>224.40 (+16.27%)</td><td>187.52 (+11.20%)</td><td>193.50 (+15.25%)</td><td>139.10 (-7.88%)</td><td>31.04 <b>(+91.05%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>168.64 (n/a)</td><td>167.90 (n/a)</td><td>151.00 (n/a)</td><td>16.25 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (+0.89%)</td><td>0.06 (+15.22%)</td><td>0.07 <b>(+24.41%)</b></td><td>0.05 <b>(+30.01%)</b></td><td>0.01 <b>(-21.86%)</b></td><td>160.10 <b>(-23.07%)</b></td><td>134.50 (-14.79%)</td><td>121.90 (-19.59%)</td><td>117.50 (-0.93%)</td><td>19.79 <b>(-40.91%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.10 (n/a)</td><td>157.84 (n/a)</td><td>151.60 (n/a)</td><td>118.60 (n/a)</td><td>33.50 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.09 (+13.97%)</td><td>0.06 (+10.79%)</td><td>0.06 (+1.04%)</td><td>0.05 (+16.98%)</td><td>0.02 <b>(+33.99%)</b></td><td>221.50 (-14.54%)</td><td>168.10 (-8.48%)</td><td>183.60 (-1.02%)</td><td>120.30 (-12.32%)</td><td>45.59 (-5.04%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>259.20 (n/a)</td><td>183.68 (n/a)</td><td>185.50 (n/a)</td><td>137.20 (n/a)</td><td>48.01 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (+17.08%)</td><td>0.06 (+16.42%)</td><td>0.06 <b>(+25.86%)</b></td><td>0.05 (+8.16%)</td><td>0.01 <b>(+74.08%)</b></td><td>160.60 (-7.54%)</td><td>138.36 (-13.51%)</td><td>130.40 <b>(-20.54%)</b></td><td>124.00 (-14.60%)</td><td>17.13 <b>(+37.29%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>173.70 (n/a)</td><td>159.98 (n/a)</td><td>164.10 (n/a)</td><td>145.20 (n/a)</td><td>12.47 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (-11.90%)</td><td>0.05 (-11.37%)</td><td>0.05 (-12.15%)</td><td>0.04 (-17.78%)</td><td>0.01 (+9.88%)</td><td>228.00 <b>(+21.60%)</b></td><td>187.74 (+14.87%)</td><td>200.00 (+13.83%)</td><td>136.60 (+13.55%)</td><td>42.10 <b>(+54.77%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>187.50 (n/a)</td><td>163.44 (n/a)</td><td>175.70 (n/a)</td><td>120.30 (n/a)</td><td>27.20 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (-2.80%)</td><td>0.05 (+6.64%)</td><td>0.05 (+9.61%)</td><td>0.04 (+12.71%)</td><td>0.00 <b>(-34.82%)</b></td><td>190.10 (-11.29%)</td><td>165.82 (-7.02%)</td><td>158.60 (-8.80%)</td><td>156.30 (+2.90%)</td><td>14.14 <b>(-40.70%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>178.34 (n/a)</td><td>173.90 (n/a)</td><td>151.90 (n/a)</td><td>23.85 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.07 (-13.91%)</td><td>0.05 (-10.82%)</td><td>0.05 (-13.70%)</td><td>0.04 (-15.45%)</td><td>0.01 (-8.82%)</td><td>221.80 (+18.29%)</td><td>180.28 (+12.66%)</td><td>188.20 (+15.89%)</td><td>132.70 (+16.20%)</td><td>37.21 <b>(+25.09%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>187.50 (n/a)</td><td>160.02 (n/a)</td><td>162.40 (n/a)</td><td>114.20 (n/a)</td><td>29.74 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (-6.96%)</td><td>0.04 (+7.35%)</td><td>0.04 (+6.61%)</td><td>0.03 (+16.39%)</td><td>0.01 <b>(-26.49%)</b></td><td>263.90 (-14.10%)</td><td>207.40 (-9.15%)</td><td>194.70 (-6.21%)</td><td>169.90 (+7.46%)</td><td>38.62 <b>(-32.49%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>307.20 (n/a)</td><td>228.30 (n/a)</td><td>207.60 (n/a)</td><td>158.10 (n/a)</td><td>57.21 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 <b>(-21.04%)</b></td><td>0.04 <b>(-21.89%)</b></td><td>0.04 <b>(-24.10%)</b></td><td>0.03 <b>(-28.76%)</b></td><td>0.01 (-18.35%)</td><td>316.20 <b>(+40.41%)</b></td><td>237.54 <b>(+28.62%)</b></td><td>230.90 <b>(+31.79%)</b></td><td>185.80 <b>(+26.65%)</b></td><td>49.37 <b>(+44.94%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.20 (n/a)</td><td>184.68 (n/a)</td><td>175.20 (n/a)</td><td>146.70 (n/a)</td><td>34.06 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.06 (+7.26%)</td><td>0.05 (+7.55%)</td><td>0.06 (+12.96%)</td><td>0.03 (-14.08%)</td><td>0.01 <b>(+56.73%)</b></td><td>251.40 (+16.39%)</td><td>166.78 (-3.29%)</td><td>145.60 (-11.44%)</td><td>127.00 (-6.75%)</td><td>51.78 <b>(+67.64%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.00 (n/a)</td><td>172.46 (n/a)</td><td>164.40 (n/a)</td><td>136.20 (n/a)</td><td>30.89 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.05 (-4.12%)</td><td>0.04 (-10.59%)</td><td>0.04 (-8.35%)</td><td>0.03 <b>(-34.44%)</b></td><td>0.01 <b>(+74.87%)</b></td><td>322.10 <b>(+52.51%)</b></td><td>220.22 (+16.25%)</td><td>208.80 (+9.09%)</td><td>165.50 (+4.28%)</td><td>59.69 <b>(+195.74%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.20 (n/a)</td><td>189.44 (n/a)</td><td>191.40 (n/a)</td><td>158.70 (n/a)</td><td>20.18 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.04 <b>(-28.18%)</b></td><td>0.04 (-18.44%)</td><td>0.04 (-18.62%)</td><td>0.04 (-11.14%)</td><td>0.00 <b>(-58.46%)</b></td><td>233.70 (+12.52%)</td><td>208.46 <b>(+20.68%)</b></td><td>204.00 <b>(+22.89%)</b></td><td>191.60 <b>(+39.24%)</b></td><td>18.08 <b>(-36.17%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.70 (n/a)</td><td>172.74 (n/a)</td><td>166.00 (n/a)</td><td>137.60 (n/a)</td><td>28.33 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.81 (+8.01%)</td><td>0.65 (+3.39%)</td><td>0.58 (-5.16%)</td><td>0.49 (+9.14%)</td><td>0.14 (+14.89%)</td><td>198.80 (-8.39%)</td><td>158.04 (-2.94%)</td><td>170.30 (+5.45%)</td><td>121.20 (-7.48%)</td><td>33.56 (-4.20%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.75 (n/a)</td><td>0.62 (n/a)</td><td>0.61 (n/a)</td><td>0.45 (n/a)</td><td>0.12 (n/a)</td><td>217.00 (n/a)</td><td>162.82 (n/a)</td><td>161.50 (n/a)</td><td>131.00 (n/a)</td><td>35.03 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.80 (+12.42%)</td><td>0.65 (+11.19%)</td><td>0.74 <b>(+27.60%)</b></td><td>0.47 (+6.48%)</td><td>0.16 <b>(+60.63%)</b></td><td>210.20 (-6.08%)</td><td>158.58 (-7.48%)</td><td>132.30 <b>(-21.62%)</b></td><td>122.20 (-11.06%)</td><td>42.35 <b>(+32.32%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.72 (n/a)</td><td>0.59 (n/a)</td><td>0.58 (n/a)</td><td>0.44 (n/a)</td><td>0.10 (n/a)</td><td>223.80 (n/a)</td><td>171.40 (n/a)</td><td>168.80 (n/a)</td><td>137.40 (n/a)</td><td>32.01 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.74 (+1.14%)</td><td>0.63 (+10.82%)</td><td>0.64 (+10.28%)</td><td>0.48 <b>(+21.80%)</b></td><td>0.10 <b>(-27.88%)</b></td><td>206.20 (-17.91%)</td><td>159.16 (-12.55%)</td><td>152.90 (-9.31%)</td><td>133.10 (-1.19%)</td><td>29.22 <b>(-40.66%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.73 (n/a)</td><td>0.57 (n/a)</td><td>0.58 (n/a)</td><td>0.39 (n/a)</td><td>0.14 (n/a)</td><td>251.20 (n/a)</td><td>182.00 (n/a)</td><td>168.60 (n/a)</td><td>134.70 (n/a)</td><td>49.24 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.61 <b>(-22.95%)</b></td><td>0.57 (-1.55%)</td><td>0.59 <b>(+20.85%)</b></td><td>0.46 (+8.92%)</td><td>0.06 <b>(-63.82%)</b></td><td>213.20 (-8.18%)</td><td>174.30 (-3.88%)</td><td>167.50 (-17.28%)</td><td>160.30 <b>(+29.80%)</b></td><td>21.98 <b>(-55.33%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.80 (n/a)</td><td>0.58 (n/a)</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.17 (n/a)</td><td>232.20 (n/a)</td><td>181.34 (n/a)</td><td>202.50 (n/a)</td><td>123.50 (n/a)</td><td>49.22 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.60 <b>(+21.13%)</b></td><td>0.44 (-1.00%)</td><td>0.40 (-8.63%)</td><td>0.36 (-11.33%)</td><td>0.10 <b>(+194.07%)</b></td><td>202.60 (+12.81%)</td><td>173.86 (+3.93%)</td><td>183.20 (+9.44%)</td><td>123.50 (-17.45%)</td><td>32.27 <b>(+172.73%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.49 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.03 (n/a)</td><td>179.60 (n/a)</td><td>167.28 (n/a)</td><td>167.40 (n/a)</td><td>149.60 (n/a)</td><td>11.83 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.68 <b>(+30.97%)</b></td><td>0.52 (+19.91%)</td><td>0.51 (+14.98%)</td><td>0.42 <b>(+29.51%)</b></td><td>0.11 <b>(+42.51%)</b></td><td>176.90 <b>(-22.78%)</b></td><td>145.52 (-16.15%)</td><td>145.80 (-13.01%)</td><td>108.70 <b>(-23.67%)</b></td><td>28.70 (-15.86%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.52 (n/a)</td><td>0.44 (n/a)</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>229.10 (n/a)</td><td>173.54 (n/a)</td><td>167.60 (n/a)</td><td>142.40 (n/a)</td><td>34.11 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.61 (+3.04%)</td><td>0.50 (+14.67%)</td><td>0.54 <b>(+36.88%)</b></td><td>0.39 (+3.52%)</td><td>0.10 (+10.64%)</td><td>187.20 (-3.41%)</td><td>151.48 (-12.31%)</td><td>135.60 <b>(-26.94%)</b></td><td>120.40 (-2.98%)</td><td>31.22 (+9.11%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.59 (n/a)</td><td>0.44 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.09 (n/a)</td><td>193.80 (n/a)</td><td>172.74 (n/a)</td><td>185.60 (n/a)</td><td>124.10 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.48 (+5.77%)</td><td>0.41 (+4.54%)</td><td>0.42 (+7.40%)</td><td>0.34 (-1.58%)</td><td>0.07 <b>(+52.75%)</b></td><td>216.90 (+1.59%)</td><td>181.92 (-3.22%)</td><td>176.60 (-6.86%)</td><td>152.30 (-5.46%)</td><td>29.68 <b>(+46.63%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.46 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.04 (n/a)</td><td>213.50 (n/a)</td><td>187.98 (n/a)</td><td>189.60 (n/a)</td><td>161.10 (n/a)</td><td>20.24 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.35 <b>(+91.45%)</b></td><td>0.95 <b>(+41.24%)</b></td><td>0.91 <b>(+33.79%)</b></td><td>0.77 <b>(+25.89%)</b></td><td>0.24 <b>(+568.56%)</b></td><td>169.20 <b>(-20.56%)</b></td><td>143.94 <b>(-26.39%)</b></td><td>144.30 <b>(-25.23%)</b></td><td>96.70 <b>(-47.79%)</b></td><td>29.39 <b>(+173.11%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.71 (n/a)</td><td>0.67 (n/a)</td><td>0.68 (n/a)</td><td>0.62 (n/a)</td><td>0.04 (n/a)</td><td>213.00 (n/a)</td><td>195.54 (n/a)</td><td>193.00 (n/a)</td><td>185.20 (n/a)</td><td>10.76 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.01 <b>(+42.61%)</b></td><td>0.86 <b>(+34.76%)</b></td><td>0.90 <b>(+46.54%)</b></td><td>0.62 (+12.32%)</td><td>0.16 <b>(+163.43%)</b></td><td>210.10 (-10.97%)</td><td>158.12 <b>(-23.98%)</b></td><td>145.10 <b>(-31.75%)</b></td><td>130.40 <b>(-29.89%)</b></td><td>33.18 <b>(+65.13%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.70 (n/a)</td><td>0.63 (n/a)</td><td>0.62 (n/a)</td><td>0.56 (n/a)</td><td>0.06 (n/a)</td><td>236.00 (n/a)</td><td>208.00 (n/a)</td><td>212.60 (n/a)</td><td>186.00 (n/a)</td><td>20.09 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.03 <b>(+31.05%)</b></td><td>0.86 <b>(+34.18%)</b></td><td>0.84 <b>(+36.59%)</b></td><td>0.74 <b>(+37.21%)</b></td><td>0.11 <b>(+24.68%)</b></td><td>176.10 <b>(-27.14%)</b></td><td>154.34 <b>(-25.61%)</b></td><td>155.30 <b>(-26.78%)</b></td><td>127.00 <b>(-23.72%)</b></td><td>19.02 <b>(-29.43%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.79 (n/a)</td><td>0.64 (n/a)</td><td>0.62 (n/a)</td><td>0.54 (n/a)</td><td>0.09 (n/a)</td><td>241.70 (n/a)</td><td>207.48 (n/a)</td><td>212.10 (n/a)</td><td>166.50 (n/a)</td><td>26.95 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (+4.42%)</td><td>0.02 (-13.54%)</td><td>0.02 (-10.97%)</td><td>0.02 <b>(-23.11%)</b></td><td>0.01 <b>(+87.50%)</b></td><td>261.90 <b>(+30.04%)</b></td><td>198.02 (+20.00%)</td><td>177.10 (+12.30%)</td><td>143.60 (-4.20%)</td><td>49.02 <b>(+134.51%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.40 (n/a)</td><td>165.02 (n/a)</td><td>157.70 (n/a)</td><td>149.90 (n/a)</td><td>20.90 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (+5.70%)</td><td>0.03 (+1.48%)</td><td>0.03 (-10.72%)</td><td>0.02 (+6.02%)</td><td>0.00 (+1.87%)</td><td>181.30 (-5.67%)</td><td>151.92 (-1.68%)</td><td>159.10 (+11.96%)</td><td>120.20 (-5.43%)</td><td>23.59 (-10.99%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.20 (n/a)</td><td>154.52 (n/a)</td><td>142.10 (n/a)</td><td>127.10 (n/a)</td><td>26.50 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (-18.81%)</td><td>0.02 (-11.16%)</td><td>0.02 (+0.94%)</td><td>0.02 (-2.39%)</td><td>0.00 <b>(-50.74%)</b></td><td>194.40 (+2.48%)</td><td>172.10 (+10.36%)</td><td>165.30 (-0.96%)</td><td>151.80 <b>(+23.21%)</b></td><td>18.90 <b>(-35.19%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>189.70 (n/a)</td><td>155.94 (n/a)</td><td>166.90 (n/a)</td><td>123.20 (n/a)</td><td>29.17 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.02 (-0.59%)</td><td>0.85 (-0.01%)</td><td>0.78 (-5.95%)</td><td>0.73 (-3.69%)</td><td>0.13 <b>(+25.74%)</b></td><td>180.80 (+3.85%)</td><td>158.74 (+0.76%)</td><td>168.40 (+6.31%)</td><td>129.90 (+0.62%)</td><td>23.49 <b>(+32.92%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.02 (n/a)</td><td>0.85 (n/a)</td><td>0.83 (n/a)</td><td>0.76 (n/a)</td><td>0.10 (n/a)</td><td>174.10 (n/a)</td><td>157.54 (n/a)</td><td>158.40 (n/a)</td><td>129.10 (n/a)</td><td>17.68 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.08 (-13.46%)</td><td>0.92 (-2.97%)</td><td>0.88 (-19.31%)</td><td>0.76 <b>(+45.52%)</b></td><td>0.15 <b>(-50.52%)</b></td><td>174.60 <b>(-31.29%)</b></td><td>147.40 (-5.21%)</td><td>149.40 <b>(+23.98%)</b></td><td>122.20 (+15.50%)</td><td>23.77 <b>(-61.54%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.25 (n/a)</td><td>0.94 (n/a)</td><td>1.10 (n/a)</td><td>0.52 (n/a)</td><td>0.30 (n/a)</td><td>254.10 (n/a)</td><td>155.50 (n/a)</td><td>120.50 (n/a)</td><td>105.80 (n/a)</td><td>61.81 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.06 (+10.80%)</td><td>0.92 (+15.09%)</td><td>1.05 <b>(+38.86%)</b></td><td>0.67 (+0.00%)</td><td>0.19 <b>(+62.85%)</b></td><td>196.60 (+0.00%)</td><td>149.32 (-11.19%)</td><td>126.40 <b>(-27.98%)</b></td><td>124.30 (-9.73%)</td><td>34.10 <b>(+43.91%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.96 (n/a)</td><td>0.80 (n/a)</td><td>0.75 (n/a)</td><td>0.67 (n/a)</td><td>0.12 (n/a)</td><td>196.60 (n/a)</td><td>168.14 (n/a)</td><td>175.50 (n/a)</td><td>137.70 (n/a)</td><td>23.70 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.03 (-4.72%)</td><td>0.91 (+2.96%)</td><td>0.89 (+5.90%)</td><td>0.80 (+0.58%)</td><td>0.10 (-14.60%)</td><td>165.60 (-0.60%)</td><td>146.10 (-3.21%)</td><td>148.00 (-5.61%)</td><td>128.60 (+4.98%)</td><td>16.23 (-12.65%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.08 (n/a)</td><td>0.89 (n/a)</td><td>0.84 (n/a)</td><td>0.79 (n/a)</td><td>0.12 (n/a)</td><td>166.60 (n/a)</td><td>150.94 (n/a)</td><td>156.80 (n/a)</td><td>122.50 (n/a)</td><td>18.58 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>1.09 (+3.57%)</td><td>0.89 (+4.97%)</td><td>0.95 (+7.81%)</td><td>0.72 (+4.67%)</td><td>0.16 (+5.99%)</td><td>184.60 (-4.45%)</td><td>151.68 (-4.63%)</td><td>139.60 (-7.24%)</td><td>121.50 (-3.49%)</td><td>26.97 (-1.28%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.05 (n/a)</td><td>0.85 (n/a)</td><td>0.88 (n/a)</td><td>0.68 (n/a)</td><td>0.15 (n/a)</td><td>193.20 (n/a)</td><td>159.04 (n/a)</td><td>150.50 (n/a)</td><td>125.90 (n/a)</td><td>27.32 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.03 (-2.70%)</td><td>0.03 (-7.08%)</td><td>0.02 (-16.67%)</td><td>0.02 (-6.42%)</td><td>0.01 <b>(+21.43%)</b></td><td>207.10 (+6.86%)</td><td>170.42 (+9.72%)</td><td>191.50 <b>(+20.06%)</b></td><td>124.70 (+2.72%)</td><td>40.63 <b>(+33.84%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>155.32 (n/a)</td><td>159.50 (n/a)</td><td>121.40 (n/a)</td><td>30.36 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.02 <b>(-23.90%)</b></td><td>0.02 (-18.04%)</td><td>0.02 (-18.81%)</td><td>0.02 (-10.33%)</td><td>0.00 <b>(-53.43%)</b></td><td>216.80 (+11.52%)</td><td>189.96 (+19.10%)</td><td>188.90 <b>(+23.14%)</b></td><td>166.80 <b>(+31.44%)</b></td><td>22.46 <b>(-33.06%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>159.50 (n/a)</td><td>153.40 (n/a)</td><td>126.90 (n/a)</td><td>33.55 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.00 (-2.22%)</td><td>0.00 (-1.90%)</td><td>0.00 (-4.65%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-20.34%)</b></td><td>1048.13 (+0.71%)</td><td>985.95 (+1.58%)</td><td>992.24 (+3.13%)</td><td>925.81 (+2.42%)</td><td>44.12 (-14.99%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1040.78 (n/a)</td><td>970.58 (n/a)</td><td>962.08 (n/a)</td><td>903.90 (n/a)</td><td>51.91 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.01 (+5.00%)</td><td>0.01 (+0.26%)</td><td>0.01 (+0.00%)</td><td>0.01 (-2.70%)</td><td>0.00 <b>(+72.75%)</b></td><td>1138.53 (+3.42%)</td><td>1046.62 (+0.41%)</td><td>1040.58 (+0.79%)</td><td>979.86 (-4.09%)</td><td>57.55 <b>(+73.92%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1100.92 (n/a)</td><td>1042.36 (n/a)</td><td>1032.42 (n/a)</td><td>1021.62 (n/a)</td><td>33.09 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.99 (-2.53%)</td><td>0.96 (-1.01%)</td><td>0.96 (-0.86%)</td><td>0.93 (-1.37%)</td><td>0.02 <b>(-25.65%)</b></td><td>2248.54 (+1.39%)</td><td>2184.17 (+0.99%)</td><td>2192.64 (+0.87%)</td><td>2118.62 (+2.60%)</td><td>48.63 <b>(-22.84%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>1.02 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.03 (n/a)</td><td>2217.66 (n/a)</td><td>2162.70 (n/a)</td><td>2173.65 (n/a)</td><td>2064.88 (n/a)</td><td>63.03 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.41 (+0.59%)</td><td>0.40 (+0.28%)</td><td>0.40 (-0.12%)</td><td>0.38 (+0.55%)</td><td>0.01 (-2.05%)</td><td>1366.82 (-0.54%)</td><td>1320.33 (-0.27%)</td><td>1308.81 (+0.12%)</td><td>1286.03 (-0.58%)</td><td>34.67 (-2.86%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.40 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1374.30 (n/a)</td><td>1323.95 (n/a)</td><td>1307.23 (n/a)</td><td>1293.50 (n/a)</td><td>35.69 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.26 (+4.42%)</td><td>0.25 (+3.22%)</td><td>0.25 (+4.01%)</td><td>0.24 (+1.05%)</td><td>0.01 <b>(+137.71%)</b></td><td>2179.88 (-1.04%)</td><td>2107.00 (-3.07%)</td><td>2082.26 (-3.85%)</td><td>2052.78 (-4.24%)</td><td>55.94 <b>(+125.47%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.00 (n/a)</td><td>2202.82 (n/a)</td><td>2173.78 (n/a)</td><td>2165.71 (n/a)</td><td>2143.64 (n/a)</td><td>24.81 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>0.38 (+1.39%)</td><td>0.37 (+0.62%)</td><td>0.37 (-0.19%)</td><td>0.36 (+0.08%)</td><td>0.01 <b>(+40.91%)</b></td><td>1462.55 (-0.07%)</td><td>1424.09 (-0.60%)</td><td>1434.83 (+0.19%)</td><td>1385.39 (-1.39%)</td><td>30.29 <b>(+39.27%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.01 (n/a)</td><td>1463.57 (n/a)</td><td>1432.69 (n/a)</td><td>1432.06 (n/a)</td><td>1404.91 (n/a)</td><td>21.75 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>3.47 (+11.43%)</td><td>3.26 (+16.75%)</td><td>3.21 (+8.79%)</td><td>3.07 <b>(+53.65%)</b></td><td>0.16 <b>(-63.07%)</b></td><td>170.50 <b>(-34.92%)</b></td><td>161.32 (-16.38%)</td><td>163.50 (-8.09%)</td><td>151.30 (-10.26%)</td><td>8.08 <b>(-79.20%)</b></td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>3.11 (n/a)</td><td>2.79 (n/a)</td><td>2.95 (n/a)</td><td>2.00 (n/a)</td><td>0.45 (n/a)</td><td>262.00 (n/a)</td><td>192.92 (n/a)</td><td>177.90 (n/a)</td><td>168.60 (n/a)</td><td>38.84 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>5.87 (+16.29%)</td><td>5.44 (+18.55%)</td><td>5.56 (+19.02%)</td><td>4.86 (+16.56%)</td><td>0.44 <b>(+22.66%)</b></td><td>215.70 (-14.20%)</td><td>193.84 (-15.61%)</td><td>188.60 (-15.95%)</td><td>178.50 (-14.02%)</td><td>15.97 (-10.40%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>5.05 (n/a)</td><td>4.59 (n/a)</td><td>4.67 (n/a)</td><td>4.17 (n/a)</td><td>0.36 (n/a)</td><td>251.40 (n/a)</td><td>229.70 (n/a)</td><td>224.40 (n/a)</td><td>207.60 (n/a)</td><td>17.82 (n/a)</td>
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
<td><code>deb6e1e</code> — 2026-09-03 22:45:23</td><td>3.81 (+5.50%)</td><td>3.29 (+14.76%)</td><td>3.23 (+17.84%)</td><td>2.85 (+11.58%)</td><td>0.39 (-8.23%)</td><td>183.80 (-10.39%)</td><td>160.90 (-13.21%)</td><td>162.30 (-15.12%)</td><td>137.60 (-5.23%)</td><td>18.62 (-19.93%)</td>
</tr>
<tr>
<td><code>d3a2d45</code> — 2026-09-03 15:27:28</td><td>3.61 (n/a)</td><td>2.87 (n/a)</td><td>2.74 (n/a)</td><td>2.56 (n/a)</td><td>0.42 (n/a)</td><td>205.10 (n/a)</td><td>185.38 (n/a)</td><td>191.20 (n/a)</td><td>145.20 (n/a)</td><td>23.26 (n/a)</td>
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
