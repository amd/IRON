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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.08 (+2.38%)</td><td>0.07 (+7.90%)</td><td>0.08 (+10.35%)</td><td>0.06 (+2.40%)</td><td>0.01 (+0.38%)</td><td>202.00 (-2.37%)</td><td>168.84 (-7.34%)</td><td>162.90 (-9.35%)</td><td>150.40 (-2.34%)</td><td>19.84 (-2.38%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>206.90 (n/a)</td><td>182.22 (n/a)</td><td>179.70 (n/a)</td><td>154.00 (n/a)</td><td>20.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.09 <b>(-26.92%)</b></td><td>0.07 (-7.53%)</td><td>0.07 (+1.88%)</td><td>0.06 (+18.08%)</td><td>0.01 <b>(-60.02%)</b></td><td>203.30 (-15.33%)</td><td>179.38 (+0.99%)</td><td>179.60 (-1.86%)</td><td>139.60 <b>(+36.86%)</b></td><td>24.49 <b>(-53.05%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>240.10 (n/a)</td><td>177.62 (n/a)</td><td>183.00 (n/a)</td><td>102.00 (n/a)</td><td>52.16 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (-5.28%)</td><td>0.06 (-4.35%)</td><td>0.07 (-5.06%)</td><td>0.04 <b>(-25.77%)</b></td><td>0.01 <b>(+23.23%)</b></td><td>313.80 <b>(+34.74%)</b></td><td>208.20 (+7.55%)</td><td>187.10 (+5.35%)</td><td>164.50 (+5.58%)</td><td>61.09 <b>(+73.94%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.90 (n/a)</td><td>193.58 (n/a)</td><td>177.60 (n/a)</td><td>155.80 (n/a)</td><td>35.12 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.08 (-0.89%)</td><td>0.06 (+0.64%)</td><td>0.06 (+1.73%)</td><td>0.05 (+9.29%)</td><td>0.01 (-10.42%)</td><td>225.90 (-8.51%)</td><td>198.00 (-1.19%)</td><td>205.20 (-1.68%)</td><td>159.40 (+0.89%)</td><td>28.64 (-15.86%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>246.90 (n/a)</td><td>200.38 (n/a)</td><td>208.70 (n/a)</td><td>158.00 (n/a)</td><td>34.04 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 <b>(+31.40%)</b></td><td>0.04 (+16.18%)</td><td>0.04 <b>(+31.68%)</b></td><td>0.03 (-12.41%)</td><td>0.01 <b>(+344.84%)</b></td><td>206.80 (+14.19%)</td><td>151.32 (-8.85%)</td><td>124.70 <b>(-24.06%)</b></td><td>116.10 <b>(-23.87%)</b></td><td>43.25 <b>(+284.04%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>181.10 (n/a)</td><td>166.02 (n/a)</td><td>164.20 (n/a)</td><td>152.50 (n/a)</td><td>11.26 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 <b>(+20.78%)</b></td><td>0.04 (+19.53%)</td><td>0.03 (+11.32%)</td><td>0.03 (+9.64%)</td><td>0.01 <b>(+59.75%)</b></td><td>184.20 (-8.81%)</td><td>153.06 (-15.34%)</td><td>164.20 (-10.18%)</td><td>120.60 (-17.17%)</td><td>26.06 <b>(+21.40%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>202.00 (n/a)</td><td>180.80 (n/a)</td><td>182.80 (n/a)</td><td>145.60 (n/a)</td><td>21.47 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 <b>(+43.77%)</b></td><td>0.03 <b>(+24.65%)</b></td><td>0.03 (+4.57%)</td><td>0.02 <b>(+36.85%)</b></td><td>0.01 <b>(+47.21%)</b></td><td>215.40 <b>(-26.91%)</b></td><td>164.28 (-19.52%)</td><td>171.50 (-4.35%)</td><td>116.90 <b>(-30.46%)</b></td><td>39.09 <b>(-26.51%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>294.70 (n/a)</td><td>204.12 (n/a)</td><td>179.30 (n/a)</td><td>168.10 (n/a)</td><td>53.19 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (+1.02%)</td><td>0.03 (-9.24%)</td><td>0.03 (-7.31%)</td><td>0.02 <b>(-22.94%)</b></td><td>0.01 <b>(+30.88%)</b></td><td>251.30 <b>(+29.74%)</b></td><td>186.08 (+12.86%)</td><td>185.70 (+7.90%)</td><td>135.90 (-1.02%)</td><td>44.35 <b>(+72.27%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.70 (n/a)</td><td>164.88 (n/a)</td><td>172.10 (n/a)</td><td>137.30 (n/a)</td><td>25.75 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (-11.29%)</td><td>0.03 (-6.39%)</td><td>0.03 (+15.28%)</td><td>0.02 <b>(-26.46%)</b></td><td>0.01 (+1.27%)</td><td>309.00 <b>(+35.94%)</b></td><td>199.14 (+9.42%)</td><td>170.40 (-13.24%)</td><td>155.60 (+12.75%)</td><td>62.92 <b>(+65.66%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.30 (n/a)</td><td>182.00 (n/a)</td><td>196.40 (n/a)</td><td>138.00 (n/a)</td><td>37.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 <b>(-23.03%)</b></td><td>0.03 (-19.64%)</td><td>0.03 <b>(-31.19%)</b></td><td>0.02 (-3.17%)</td><td>0.00 <b>(-49.20%)</b></td><td>211.80 (+3.27%)</td><td>194.84 <b>(+22.05%)</b></td><td>209.40 <b>(+45.32%)</b></td><td>168.70 <b>(+29.97%)</b></td><td>21.84 <b>(-31.76%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>159.64 (n/a)</td><td>144.10 (n/a)</td><td>129.80 (n/a)</td><td>32.01 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (+17.98%)</td><td>0.03 (+7.58%)</td><td>0.03 (-5.53%)</td><td>0.02 (+14.12%)</td><td>0.00 <b>(+25.19%)</b></td><td>217.20 (-12.35%)</td><td>187.76 (-6.81%)</td><td>198.00 (+5.83%)</td><td>150.20 (-15.24%)</td><td>27.37 (-7.28%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.80 (n/a)</td><td>201.48 (n/a)</td><td>187.10 (n/a)</td><td>177.20 (n/a)</td><td>29.52 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (+18.40%)</td><td>0.02 (+3.17%)</td><td>0.02 (+2.47%)</td><td>0.02 <b>(-22.60%)</b></td><td>0.01 <b>(+190.78%)</b></td><td>311.30 <b>(+29.22%)</b></td><td>222.08 (+0.70%)</td><td>215.80 (-2.44%)</td><td>168.80 (-15.56%)</td><td>54.85 <b>(+224.05%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.90 (n/a)</td><td>220.54 (n/a)</td><td>221.20 (n/a)</td><td>199.90 (n/a)</td><td>16.93 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>189.10 (n/a)</td><td>162.82 (n/a)</td><td>167.90 (n/a)</td><td>141.90 (n/a)</td><td>19.22 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.20 (n/a)</td><td>182.98 (n/a)</td><td>184.40 (n/a)</td><td>144.20 (n/a)</td><td>27.22 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>219.30 (n/a)</td><td>176.66 (n/a)</td><td>181.10 (n/a)</td><td>137.20 (n/a)</td><td>34.50 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>192.54 (n/a)</td><td>189.30 (n/a)</td><td>171.40 (n/a)</td><td>17.14 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>158.68 (n/a)</td><td>166.50 (n/a)</td><td>123.50 (n/a)</td><td>23.11 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.50 (n/a)</td><td>188.50 (n/a)</td><td>187.00 (n/a)</td><td>166.60 (n/a)</td><td>26.84 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>202.90 (n/a)</td><td>169.58 (n/a)</td><td>169.80 (n/a)</td><td>108.20 (n/a)</td><td>38.24 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>341.40 (n/a)</td><td>255.16 (n/a)</td><td>248.80 (n/a)</td><td>188.00 (n/a)</td><td>67.34 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>5.18 <b>(+24.42%)</b></td><td>3.62 (+4.83%)</td><td>3.24 (+3.26%)</td><td>3.03 (+4.64%)</td><td>0.89 <b>(+42.22%)</b></td><td>453.60 (-4.44%)</td><td>394.96 (-3.38%)</td><td>424.40 (-3.17%)</td><td>265.80 (-19.63%)</td><td>75.47 (+7.62%)</td><td>1009.86 <b>(+24.42%)</b></td><td>705.95 (+4.83%)</td><td>632.44 (+3.26%)</td><td>591.75 (+4.64%)</td><td>173.11 <b>(+42.22%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>4.16 (n/a)</td><td>3.45 (n/a)</td><td>3.14 (n/a)</td><td>2.90 (n/a)</td><td>0.62 (n/a)</td><td>474.70 (n/a)</td><td>408.76 (n/a)</td><td>438.30 (n/a)</td><td>330.70 (n/a)</td><td>70.13 (n/a)</td><td>811.67 (n/a)</td><td>673.41 (n/a)</td><td>612.48 (n/a)</td><td>565.50 (n/a)</td><td>121.72 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>6.20 <b>(+29.70%)</b></td><td>4.82 <b>(+25.71%)</b></td><td>4.50 <b>(+25.35%)</b></td><td>3.63 (+4.26%)</td><td>1.07 <b>(+98.30%)</b></td><td>379.60 (-4.09%)</td><td>296.64 (-18.41%)</td><td>306.00 <b>(-20.21%)</b></td><td>222.10 <b>(-22.91%)</b></td><td>64.46 <b>(+46.38%)</b></td><td>1208.61 <b>(+29.70%)</b></td><td>940.89 <b>(+25.71%)</b></td><td>877.38 <b>(+25.35%)</b></td><td>707.21 (+4.26%)</td><td>208.65 <b>(+98.30%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>4.78 (n/a)</td><td>3.84 (n/a)</td><td>3.59 (n/a)</td><td>3.48 (n/a)</td><td>0.54 (n/a)</td><td>395.80 (n/a)</td><td>363.58 (n/a)</td><td>383.50 (n/a)</td><td>288.10 (n/a)</td><td>44.03 (n/a)</td><td>931.88 (n/a)</td><td>748.48 (n/a)</td><td>699.93 (n/a)</td><td>678.29 (n/a)</td><td>105.22 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>5.57 (+2.03%)</td><td>4.27 (-0.51%)</td><td>4.01 (+3.11%)</td><td>3.46 (-6.27%)</td><td>0.80 (+9.43%)</td><td>398.10 (+6.70%)</td><td>330.54 (+0.98%)</td><td>343.40 (-3.02%)</td><td>247.30 (-1.98%)</td><td>56.26 (+12.08%)</td><td>1085.51 (+2.03%)</td><td>833.25 (-0.51%)</td><td>781.76 (+3.11%)</td><td>674.28 (-6.27%)</td><td>156.87 (+9.43%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>5.45 (n/a)</td><td>4.29 (n/a)</td><td>3.89 (n/a)</td><td>3.69 (n/a)</td><td>0.73 (n/a)</td><td>373.10 (n/a)</td><td>327.34 (n/a)</td><td>354.10 (n/a)</td><td>252.30 (n/a)</td><td>50.20 (n/a)</td><td>1063.95 (n/a)</td><td>837.56 (n/a)</td><td>758.16 (n/a)</td><td>719.40 (n/a)</td><td>143.35 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>9.11 <b>(+29.93%)</b></td><td>5.32 <b>(+21.54%)</b></td><td>4.69 <b>(+27.89%)</b></td><td>3.79 (+5.05%)</td><td>2.15 <b>(+45.59%)</b></td><td>363.40 (-4.79%)</td><td>283.92 (-15.38%)</td><td>293.20 <b>(-21.79%)</b></td><td>151.00 <b>(-23.04%)</b></td><td>79.88 (+1.15%)</td><td>1777.75 <b>(+29.93%)</b></td><td>1038.17 <b>(+21.54%)</b></td><td>915.67 <b>(+27.89%)</b></td><td>738.70 (+5.05%)</td><td>420.13 <b>(+45.59%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>7.01 (n/a)</td><td>4.38 (n/a)</td><td>3.67 (n/a)</td><td>3.61 (n/a)</td><td>1.48 (n/a)</td><td>381.70 (n/a)</td><td>335.54 (n/a)</td><td>374.90 (n/a)</td><td>196.20 (n/a)</td><td>78.97 (n/a)</td><td>1368.22 (n/a)</td><td>854.17 (n/a)</td><td>715.97 (n/a)</td><td>703.19 (n/a)</td><td>288.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>5.98 (-15.53%)</td><td>3.85 (-2.71%)</td><td>3.44 (+6.48%)</td><td>2.86 (-6.93%)</td><td>1.22 <b>(-29.94%)</b></td><td>481.90 (+7.45%)</td><td>380.42 (-1.31%)</td><td>399.70 (-6.09%)</td><td>230.30 (+18.41%)</td><td>92.35 (-13.93%)</td><td>1165.80 (-15.53%)</td><td>751.10 (-2.71%)</td><td>671.66 (+6.48%)</td><td>557.07 (-6.93%)</td><td>238.40 <b>(-29.94%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>7.08 (n/a)</td><td>3.96 (n/a)</td><td>3.23 (n/a)</td><td>3.07 (n/a)</td><td>1.74 (n/a)</td><td>448.50 (n/a)</td><td>385.48 (n/a)</td><td>425.60 (n/a)</td><td>194.50 (n/a)</td><td>107.30 (n/a)</td><td>1380.13 (n/a)</td><td>772.04 (n/a)</td><td>630.80 (n/a)</td><td>598.54 (n/a)</td><td>340.28 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>2.23 (+0.46%)</td><td>1.95 (+4.61%)</td><td>2.01 (+8.10%)</td><td>1.55 (-6.56%)</td><td>0.26 <b>(+21.65%)</b></td><td>258.20 (+7.00%)</td><td>208.62 (-3.84%)</td><td>200.10 (-7.49%)</td><td>180.40 (-0.44%)</td><td>30.69 <b>(+31.91%)</b></td><td>186.02 (+0.46%)</td><td>163.41 (+4.61%)</td><td>167.68 (+8.10%)</td><td>129.95 (-6.56%)</td><td>21.88 <b>(+21.65%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>2.22 (n/a)</td><td>1.87 (n/a)</td><td>1.86 (n/a)</td><td>1.66 (n/a)</td><td>0.22 (n/a)</td><td>241.30 (n/a)</td><td>216.94 (n/a)</td><td>216.30 (n/a)</td><td>181.20 (n/a)</td><td>23.27 (n/a)</td><td>185.17 (n/a)</td><td>156.21 (n/a)</td><td>155.12 (n/a)</td><td>139.07 (n/a)</td><td>17.99 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>7.58 <b>(+47.79%)</b></td><td>6.32 <b>(+27.38%)</b></td><td>5.91 (+19.04%)</td><td>5.05 (+4.76%)</td><td>1.13 <b>(+888.43%)</b></td><td>382.80 (-4.54%)</td><td>313.88 (-19.53%)</td><td>327.30 (-16.01%)</td><td>255.10 <b>(-32.33%)</b></td><td>55.05 <b>(+519.75%)</b></td><td>1578.57 <b>(+47.79%)</b></td><td>1315.55 <b>(+27.38%)</b></td><td>1230.07 (+19.04%)</td><td>1051.93 (+4.76%)</td><td>234.40 <b>(+888.43%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>5.13 (n/a)</td><td>4.96 (n/a)</td><td>4.96 (n/a)</td><td>4.82 (n/a)</td><td>0.11 (n/a)</td><td>401.00 (n/a)</td><td>390.04 (n/a)</td><td>389.70 (n/a)</td><td>377.00 (n/a)</td><td>8.88 (n/a)</td><td>1068.11 (n/a)</td><td>1032.80 (n/a)</td><td>1033.29 (n/a)</td><td>1004.16 (n/a)</td><td>23.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>14.12 (-15.37%)</td><td>13.01 (+0.22%)</td><td>12.58 (+2.06%)</td><td>12.48 (+8.00%)</td><td>0.72 <b>(-66.25%)</b></td><td>441.10 (-7.41%)</td><td>424.08 (-1.78%)</td><td>437.70 (-1.99%)</td><td>389.80 (+18.16%)</td><td>22.48 <b>(-62.22%)</b></td><td>5508.76 (-15.37%)</td><td>5075.69 (+0.22%)</td><td>4906.83 (+2.06%)</td><td>4868.16 (+8.00%)</td><td>279.12 <b>(-66.25%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>16.69 (n/a)</td><td>12.98 (n/a)</td><td>12.33 (n/a)</td><td>11.56 (n/a)</td><td>2.12 (n/a)</td><td>476.40 (n/a)</td><td>431.78 (n/a)</td><td>446.60 (n/a)</td><td>329.90 (n/a)</td><td>59.50 (n/a)</td><td>6508.95 (n/a)</td><td>5064.35 (n/a)</td><td>4807.98 (n/a)</td><td>4507.76 (n/a)</td><td>826.99 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.70 (n/a)</td><td>154.50 (n/a)</td><td>157.30 (n/a)</td><td>137.10 (n/a)</td><td>15.12 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.30 (n/a)</td><td>158.54 (n/a)</td><td>163.00 (n/a)</td><td>133.90 (n/a)</td><td>15.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.20 (n/a)</td><td>150.02 (n/a)</td><td>146.10 (n/a)</td><td>124.20 (n/a)</td><td>23.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.60 (n/a)</td><td>164.78 (n/a)</td><td>163.50 (n/a)</td><td>136.40 (n/a)</td><td>20.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>161.32 (n/a)</td><td>165.20 (n/a)</td><td>119.00 (n/a)</td><td>33.21 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>194.90 (n/a)</td><td>178.12 (n/a)</td><td>179.50 (n/a)</td><td>154.50 (n/a)</td><td>14.95 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.60 (n/a)</td><td>178.24 (n/a)</td><td>175.90 (n/a)</td><td>124.90 (n/a)</td><td>48.72 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>181.66 (n/a)</td><td>187.50 (n/a)</td><td>139.20 (n/a)</td><td>31.64 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>4.18 (+0.52%)</td><td>4.02 (+3.57%)</td><td>4.06 (+1.89%)</td><td>3.64 (+3.45%)</td><td>0.22 (-13.86%)</td><td>2583.80 (-3.33%)</td><td>2345.10 (-3.55%)</td><td>2318.00 (-1.86%)</td><td>2251.30 (-0.52%)</td><td>137.71 (-17.01%)</td><td>1643.23 (+0.52%)</td><td>1581.59 (+3.57%)</td><td>1595.94 (+1.89%)</td><td>1431.78 (+3.45%)</td><td>87.15 (-13.86%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>4.16 (n/a)</td><td>3.88 (n/a)</td><td>3.98 (n/a)</td><td>3.52 (n/a)</td><td>0.26 (n/a)</td><td>2672.80 (n/a)</td><td>2431.38 (n/a)</td><td>2361.90 (n/a)</td><td>2263.00 (n/a)</td><td>165.93 (n/a)</td><td>1634.75 (n/a)</td><td>1527.04 (n/a)</td><td>1566.29 (n/a)</td><td>1384.08 (n/a)</td><td>101.17 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.17 (+4.08%)</td><td>0.81 (-19.20%)</td><td>0.68 <b>(-33.90%)</b></td><td>0.62 <b>(-29.91%)</b></td><td>0.23 <b>(+152.83%)</b></td><td>359.30 <b>(+42.69%)</b></td><td>289.70 <b>(+30.32%)</b></td><td>327.30 <b>(+51.32%)</b></td><td>189.00 (-3.91%)</td><td>71.93 <b>(+245.40%)</b></td><td>49.93 (+4.08%)</td><td>34.54 (-19.20%)</td><td>28.84 <b>(-33.90%)</b></td><td>26.27 <b>(-29.91%)</b></td><td>9.98 <b>(+152.83%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.12 (n/a)</td><td>1.00 (n/a)</td><td>1.02 (n/a)</td><td>0.88 (n/a)</td><td>0.09 (n/a)</td><td>251.80 (n/a)</td><td>222.30 (n/a)</td><td>216.30 (n/a)</td><td>196.70 (n/a)</td><td>20.83 (n/a)</td><td>47.97 (n/a)</td><td>42.75 (n/a)</td><td>43.62 (n/a)</td><td>37.48 (n/a)</td><td>3.95 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.35 (+15.17%)</td><td>0.93 (-15.37%)</td><td>0.95 (-14.54%)</td><td>0.68 <b>(-34.87%)</b></td><td>0.27 <b>(+381.06%)</b></td><td>326.80 <b>(+53.50%)</b></td><td>254.46 <b>(+25.83%)</b></td><td>232.80 (+17.04%)</td><td>163.70 (-13.20%)</td><td>69.25 <b>(+559.34%)</b></td><td>57.63 (+15.17%)</td><td>39.58 (-15.37%)</td><td>40.54 (-14.54%)</td><td>28.87 <b>(-34.87%)</b></td><td>11.72 <b>(+381.06%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.17 (n/a)</td><td>1.10 (n/a)</td><td>1.11 (n/a)</td><td>1.04 (n/a)</td><td>0.06 (n/a)</td><td>212.90 (n/a)</td><td>202.22 (n/a)</td><td>198.90 (n/a)</td><td>188.60 (n/a)</td><td>10.50 (n/a)</td><td>50.04 (n/a)</td><td>46.77 (n/a)</td><td>47.44 (n/a)</td><td>44.33 (n/a)</td><td>2.44 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.53 (+0.80%)</td><td>0.53 (+0.23%)</td><td>0.53 (+0.06%)</td><td>0.53 (+0.16%)</td><td>0.00 <b>(+320.66%)</b></td><td>47814.60 (-0.16%)</td><td>47712.18 (-0.23%)</td><td>47781.20 (-0.06%)</td><td>47406.90 (-0.79%)</td><td>171.56 <b>(+316.31%)</b></td><td>362.39 (+0.80%)</td><td>360.08 (+0.23%)</td><td>359.55 (+0.06%)</td><td>359.30 (+0.16%)</td><td>1.30 <b>(+320.65%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47889.10 (n/a)</td><td>47823.56 (n/a)</td><td>47811.20 (n/a)</td><td>47785.60 (n/a)</td><td>41.21 (n/a)</td><td>359.52 (n/a)</td><td>359.23 (n/a)</td><td>359.33 (n/a)</td><td>358.74 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.91 (-0.98%)</td><td>0.90 (-0.69%)</td><td>0.90 (-0.87%)</td><td>0.90 (-0.54%)</td><td>0.01 <b>(-26.51%)</b></td><td>28086.20 (+0.54%)</td><td>27907.46 (+0.70%)</td><td>27919.10 (+0.88%)</td><td>27653.80 (+0.99%)</td><td>165.30 <b>(-25.44%)</b></td><td>621.25 (-0.98%)</td><td>615.62 (-0.69%)</td><td>615.34 (-0.87%)</td><td>611.68 (-0.54%)</td><td>3.66 <b>(-26.51%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.92 (n/a)</td><td>0.91 (n/a)</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.01 (n/a)</td><td>27934.80 (n/a)</td><td>27714.24 (n/a)</td><td>27676.10 (n/a)</td><td>27383.60 (n/a)</td><td>221.70 (n/a)</td><td>627.38 (n/a)</td><td>619.93 (n/a)</td><td>620.75 (n/a)</td><td>615.00 (n/a)</td><td>4.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>3.36 (+0.85%)</td><td>3.19 (-0.18%)</td><td>3.16 (-0.93%)</td><td>3.13 (+0.90%)</td><td>0.10 (+13.17%)</td><td>8039.70 (-0.89%)</td><td>7886.54 (+0.19%)</td><td>7958.80 (+0.94%)</td><td>7480.40 (-0.85%)</td><td>231.69 (+11.28%)</td><td>2296.66 (+0.85%)</td><td>2179.95 (-0.18%)</td><td>2158.61 (-0.93%)</td><td>2136.88 (+0.90%)</td><td>66.42 (+13.17%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>3.34 (n/a)</td><td>3.20 (n/a)</td><td>3.19 (n/a)</td><td>3.10 (n/a)</td><td>0.09 (n/a)</td><td>8111.90 (n/a)</td><td>7871.20 (n/a)</td><td>7884.40 (n/a)</td><td>7544.20 (n/a)</td><td>208.21 (n/a)</td><td>2277.23 (n/a)</td><td>2183.87 (n/a)</td><td>2178.96 (n/a)</td><td>2117.86 (n/a)</td><td>58.69 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>3.61 (-14.47%)</td><td>3.36 (-9.24%)</td><td>3.52 (-2.11%)</td><td>3.05 (+1.43%)</td><td>0.28 <b>(-44.56%)</b></td><td>2640.40 (-1.42%)</td><td>2413.40 (+9.10%)</td><td>2289.10 (+2.16%)</td><td>2234.50 (+16.92%)</td><td>206.94 <b>(-34.22%)</b></td><td>946.05 (-14.47%)</td><td>880.94 (-9.24%)</td><td>923.46 (-2.11%)</td><td>800.60 (+1.43%)</td><td>73.42 <b>(-44.56%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>4.22 (n/a)</td><td>3.70 (n/a)</td><td>3.60 (n/a)</td><td>3.01 (n/a)</td><td>0.50 (n/a)</td><td>2678.30 (n/a)</td><td>2212.10 (n/a)</td><td>2240.80 (n/a)</td><td>1911.10 (n/a)</td><td>314.60 (n/a)</td><td>1106.13 (n/a)</td><td>970.59 (n/a)</td><td>943.37 (n/a)</td><td>789.28 (n/a)</td><td>132.42 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.46 <b>(+37.95%)</b></td><td>0.37 (+16.18%)</td><td>0.34 (+5.29%)</td><td>0.32 (+12.53%)</td><td>0.06 <b>(+198.41%)</b></td><td>3884.00 (-11.13%)</td><td>3424.20 (-12.56%)</td><td>3617.20 (-5.03%)</td><td>2689.50 <b>(-27.51%)</b></td><td>504.60 <b>(+91.07%)</b></td><td>24.95 <b>(+37.95%)</b></td><td>19.98 (+16.18%)</td><td>18.55 (+5.29%)</td><td>17.28 (+12.53%)</td><td>3.23 <b>(+198.41%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.33 (n/a)</td><td>0.28 (n/a)</td><td>0.02 (n/a)</td><td>4370.50 (n/a)</td><td>3916.00 (n/a)</td><td>3808.70 (n/a)</td><td>3710.00 (n/a)</td><td>264.09 (n/a)</td><td>18.09 (n/a)</td><td>17.20 (n/a)</td><td>17.62 (n/a)</td><td>15.35 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>4.81 (+1.13%)</td><td>4.57 <b>(+22.30%)</b></td><td>4.78 <b>(+34.86%)</b></td><td>3.69 (+11.46%)</td><td>0.50 (-14.62%)</td><td>1804.70 (-10.28%)</td><td>1470.98 (-18.67%)</td><td>1391.40 <b>(-25.85%)</b></td><td>1381.70 (-1.12%)</td><td>186.60 <b>(-21.39%)</b></td><td>1487.46 (+1.13%)</td><td>1412.72 <b>(+22.30%)</b></td><td>1477.08 <b>(+34.86%)</b></td><td>1138.84 (+11.46%)</td><td>153.17 (-14.62%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>4.76 (n/a)</td><td>3.74 (n/a)</td><td>3.55 (n/a)</td><td>3.31 (n/a)</td><td>0.58 (n/a)</td><td>2011.40 (n/a)</td><td>1808.58 (n/a)</td><td>1876.40 (n/a)</td><td>1397.30 (n/a)</td><td>237.37 (n/a)</td><td>1470.83 (n/a)</td><td>1155.14 (n/a)</td><td>1095.30 (n/a)</td><td>1021.76 (n/a)</td><td>179.40 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.28 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>13.33 (n/a)</td><td>12.34 (n/a)</td><td>12.61 (n/a)</td><td>10.75 (n/a)</td><td>1.08 (n/a)</td><td>13.32 (n/a)</td><td>12.33 (n/a)</td><td>12.61 (n/a)</td><td>10.75 (n/a)</td><td>1.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>24.80 (+1.22%)</td><td>23.63 (-2.03%)</td><td>24.22 (+0.74%)</td><td>20.75 (-13.22%)</td><td>1.66 <b>(+634.51%)</b></td><td>24.79 (+1.22%)</td><td>23.62 (-2.02%)</td><td>24.21 (+0.74%)</td><td>20.74 (-13.22%)</td><td>1.66 <b>(+634.52%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>24.50 (n/a)</td><td>24.12 (n/a)</td><td>24.04 (n/a)</td><td>23.91 (n/a)</td><td>0.23 (n/a)</td><td>24.49 (n/a)</td><td>24.11 (n/a)</td><td>24.03 (n/a)</td><td>23.90 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>41.39 (+0.76%)</td><td>40.18 (+2.91%)</td><td>41.08 (+5.84%)</td><td>37.96 (+0.45%)</td><td>1.57 <b>(+26.66%)</b></td><td>41.37 (+0.76%)</td><td>40.15 (+2.91%)</td><td>41.06 (+5.84%)</td><td>37.94 (+0.45%)</td><td>1.57 <b>(+26.66%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>41.08 (n/a)</td><td>39.04 (n/a)</td><td>38.82 (n/a)</td><td>37.79 (n/a)</td><td>1.24 (n/a)</td><td>41.05 (n/a)</td><td>39.02 (n/a)</td><td>38.79 (n/a)</td><td>37.77 (n/a)</td><td>1.24 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>44.47 (-0.27%)</td><td>37.27 (-13.34%)</td><td>41.74 (-3.23%)</td><td>22.82 <b>(-44.28%)</b></td><td>9.11 <b>(+563.26%)</b></td><td>44.44 (-0.27%)</td><td>37.25 (-13.34%)</td><td>41.72 (-3.23%)</td><td>22.81 <b>(-44.28%)</b></td><td>9.11 <b>(+563.26%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>44.59 (n/a)</td><td>43.01 (n/a)</td><td>43.14 (n/a)</td><td>40.96 (n/a)</td><td>1.37 (n/a)</td><td>44.56 (n/a)</td><td>42.98 (n/a)</td><td>43.11 (n/a)</td><td>40.94 (n/a)</td><td>1.37 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>13.43 (n/a)</td><td>12.64 (n/a)</td><td>13.05 (n/a)</td><td>11.51 (n/a)</td><td>0.82 (n/a)</td><td>13.42 (n/a)</td><td>12.63 (n/a)</td><td>13.04 (n/a)</td><td>11.50 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>25.25 (+3.11%)</td><td>24.35 (+1.36%)</td><td>24.19 (+0.52%)</td><td>23.79 (+0.68%)</td><td>0.54 <b>(+68.24%)</b></td><td>25.23 (+3.11%)</td><td>24.33 (+1.36%)</td><td>24.17 (+0.52%)</td><td>23.78 (+0.68%)</td><td>0.54 <b>(+68.24%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>24.49 (n/a)</td><td>24.02 (n/a)</td><td>24.06 (n/a)</td><td>23.63 (n/a)</td><td>0.32 (n/a)</td><td>24.47 (n/a)</td><td>24.00 (n/a)</td><td>24.05 (n/a)</td><td>23.62 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>40.46 (-2.55%)</td><td>38.78 (-4.83%)</td><td>38.97 (-4.84%)</td><td>37.05 (-6.29%)</td><td>1.27 <b>(+51.45%)</b></td><td>40.44 (-2.55%)</td><td>38.75 (-4.83%)</td><td>38.94 (-4.84%)</td><td>37.03 (-6.29%)</td><td>1.27 <b>(+51.45%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>41.52 (n/a)</td><td>40.74 (n/a)</td><td>40.95 (n/a)</td><td>39.54 (n/a)</td><td>0.84 (n/a)</td><td>41.49 (n/a)</td><td>40.72 (n/a)</td><td>40.92 (n/a)</td><td>39.51 (n/a)</td><td>0.84 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>43.49 (-0.73%)</td><td>42.07 (+5.67%)</td><td>42.41 (-0.47%)</td><td>39.08 <b>(+24.71%)</b></td><td>1.77 <b>(-66.76%)</b></td><td>43.47 (-0.73%)</td><td>42.05 (+5.67%)</td><td>42.39 (-0.47%)</td><td>39.06 <b>(+24.71%)</b></td><td>1.77 <b>(-66.76%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>43.81 (n/a)</td><td>39.82 (n/a)</td><td>42.61 (n/a)</td><td>31.34 (n/a)</td><td>5.34 (n/a)</td><td>43.79 (n/a)</td><td>39.79 (n/a)</td><td>42.59 (n/a)</td><td>31.32 (n/a)</td><td>5.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>9.34 (-2.14%)</td><td>8.78 (-3.02%)</td><td>8.78 (-1.42%)</td><td>8.26 (-5.02%)</td><td>0.38 (-6.39%)</td><td>9.32 (-2.14%)</td><td>8.77 (-3.02%)</td><td>8.76 (-1.42%)</td><td>8.24 (-5.02%)</td><td>0.38 (-6.39%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>9.54 (n/a)</td><td>9.06 (n/a)</td><td>8.90 (n/a)</td><td>8.69 (n/a)</td><td>0.41 (n/a)</td><td>9.52 (n/a)</td><td>9.04 (n/a)</td><td>8.89 (n/a)</td><td>8.68 (n/a)</td><td>0.41 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.01 (+4.02%)</td><td>0.87 (-5.91%)</td><td>0.85 (-9.69%)</td><td>0.76 (-11.05%)</td><td>0.09 <b>(+80.38%)</b></td><td>0.99 (+4.02%)</td><td>0.85 (-5.91%)</td><td>0.84 (-9.69%)</td><td>0.75 (-11.05%)</td><td>0.09 <b>(+80.38%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.97 (n/a)</td><td>0.92 (n/a)</td><td>0.94 (n/a)</td><td>0.85 (n/a)</td><td>0.05 (n/a)</td><td>0.95 (n/a)</td><td>0.91 (n/a)</td><td>0.93 (n/a)</td><td>0.84 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.41 (-0.49%)</td><td>1.14 (-7.90%)</td><td>1.16 (-6.54%)</td><td>0.91 (-13.90%)</td><td>0.22 <b>(+72.30%)</b></td><td>1.39 (-0.49%)</td><td>1.12 (-7.90%)</td><td>1.15 (-6.54%)</td><td>0.90 (-13.90%)</td><td>0.22 <b>(+72.30%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.41 (n/a)</td><td>1.24 (n/a)</td><td>1.24 (n/a)</td><td>1.06 (n/a)</td><td>0.13 (n/a)</td><td>1.40 (n/a)</td><td>1.22 (n/a)</td><td>1.23 (n/a)</td><td>1.05 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>18.07 (+10.61%)</td><td>15.15 (-1.78%)</td><td>15.65 (-1.49%)</td><td>12.08 (-9.33%)</td><td>2.52 <b>(+106.81%)</b></td><td>17.86 (+10.61%)</td><td>14.97 (-1.78%)</td><td>15.47 (-1.49%)</td><td>11.94 (-9.33%)</td><td>2.49 <b>(+106.81%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>16.34 (n/a)</td><td>15.43 (n/a)</td><td>15.89 (n/a)</td><td>13.32 (n/a)</td><td>1.22 (n/a)</td><td>16.15 (n/a)</td><td>15.25 (n/a)</td><td>15.70 (n/a)</td><td>13.17 (n/a)</td><td>1.20 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>13.39 (-2.58%)</td><td>12.78 (-2.96%)</td><td>13.21 (-1.56%)</td><td>11.83 (-0.20%)</td><td>0.76 (-0.85%)</td><td>13.16 (-2.58%)</td><td>12.56 (-2.96%)</td><td>12.98 (-1.56%)</td><td>11.62 (-0.20%)</td><td>0.74 (-0.85%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>13.74 (n/a)</td><td>13.17 (n/a)</td><td>13.42 (n/a)</td><td>11.86 (n/a)</td><td>0.76 (n/a)</td><td>13.50 (n/a)</td><td>12.94 (n/a)</td><td>13.18 (n/a)</td><td>11.65 (n/a)</td><td>0.75 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>7.80 (-15.73%)</td><td>7.39 (-6.83%)</td><td>7.40 (-11.81%)</td><td>7.03 (+17.51%)</td><td>0.34 <b>(-74.62%)</b></td><td>7.66 (-15.73%)</td><td>7.26 (-6.83%)</td><td>7.27 (-11.81%)</td><td>6.90 (+17.51%)</td><td>0.33 <b>(-74.62%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>9.25 (n/a)</td><td>7.93 (n/a)</td><td>8.39 (n/a)</td><td>5.98 (n/a)</td><td>1.33 (n/a)</td><td>9.09 (n/a)</td><td>7.79 (n/a)</td><td>8.25 (n/a)</td><td>5.88 (n/a)</td><td>1.30 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>6.16 (-7.39%)</td><td>5.34 (-5.20%)</td><td>5.43 (-7.42%)</td><td>4.57 (-2.83%)</td><td>0.59 <b>(-23.81%)</b></td><td>6.06 (-7.39%)</td><td>5.25 (-5.20%)</td><td>5.34 (-7.42%)</td><td>4.49 (-2.83%)</td><td>0.58 <b>(-23.81%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>6.65 (n/a)</td><td>5.63 (n/a)</td><td>5.86 (n/a)</td><td>4.70 (n/a)</td><td>0.78 (n/a)</td><td>6.55 (n/a)</td><td>5.54 (n/a)</td><td>5.77 (n/a)</td><td>4.62 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>13.56 (n/a)</td><td>12.15 (n/a)</td><td>12.15 (n/a)</td><td>10.76 (n/a)</td><td>0.99 (n/a)</td><td>13.56 (n/a)</td><td>12.14 (n/a)</td><td>12.15 (n/a)</td><td>10.75 (n/a)</td><td>0.99 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>13.47 (n/a)</td><td>12.66 (n/a)</td><td>12.99 (n/a)</td><td>11.42 (n/a)</td><td>0.87 (n/a)</td><td>13.46 (n/a)</td><td>12.65 (n/a)</td><td>12.98 (n/a)</td><td>11.41 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>171.42 (n/a)</td><td>173.10 (n/a)</td><td>139.60 (n/a)</td><td>24.15 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>200.30 (n/a)</td><td>185.46 (n/a)</td><td>182.10 (n/a)</td><td>171.30 (n/a)</td><td>11.40 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.70 (n/a)</td><td>176.98 (n/a)</td><td>169.70 (n/a)</td><td>139.00 (n/a)</td><td>30.32 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.40 (n/a)</td><td>185.28 (n/a)</td><td>180.00 (n/a)</td><td>142.50 (n/a)</td><td>33.28 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>279.60 (n/a)</td><td>207.42 (n/a)</td><td>205.10 (n/a)</td><td>140.40 (n/a)</td><td>49.28 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>187.02 (n/a)</td><td>199.30 (n/a)</td><td>128.10 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>232.30 (n/a)</td><td>211.16 (n/a)</td><td>204.10 (n/a)</td><td>186.60 (n/a)</td><td>19.25 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>253.60 (n/a)</td><td>240.46 (n/a)</td><td>238.20 (n/a)</td><td>234.00 (n/a)</td><td>7.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (-16.69%)</td><td>0.05 (-10.75%)</td><td>0.05 (-8.81%)</td><td>0.04 (-5.38%)</td><td>0.01 <b>(-24.17%)</b></td><td>211.40 (+5.70%)</td><td>180.48 (+11.45%)</td><td>178.70 (+9.70%)</td><td>151.60 <b>(+20.03%)</b></td><td>25.44 (-2.98%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>161.94 (n/a)</td><td>162.90 (n/a)</td><td>126.30 (n/a)</td><td>26.22 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.08 <b>(+34.82%)</b></td><td>0.06 (+6.55%)</td><td>0.05 (-4.61%)</td><td>0.04 (-10.87%)</td><td>0.02 <b>(+143.50%)</b></td><td>199.80 (+12.18%)</td><td>154.32 (-1.62%)</td><td>168.90 (+4.84%)</td><td>98.60 <b>(-25.81%)</b></td><td>38.93 <b>(+97.75%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.10 (n/a)</td><td>156.86 (n/a)</td><td>161.10 (n/a)</td><td>132.90 (n/a)</td><td>19.68 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.08 (+3.58%)</td><td>0.06 (-0.18%)</td><td>0.06 (+7.92%)</td><td>0.04 (+4.14%)</td><td>0.01 (-5.07%)</td><td>186.70 (-3.96%)</td><td>147.72 (-0.36%)</td><td>142.10 (-7.37%)</td><td>108.70 (-3.46%)</td><td>30.88 (-8.50%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>148.26 (n/a)</td><td>153.40 (n/a)</td><td>112.60 (n/a)</td><td>33.75 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (-17.27%)</td><td>0.05 (-14.05%)</td><td>0.05 (+0.73%)</td><td>0.03 <b>(-21.01%)</b></td><td>0.01 (-12.51%)</td><td>235.90 <b>(+26.56%)</b></td><td>185.32 (+16.74%)</td><td>168.00 (-0.77%)</td><td>155.80 <b>(+20.87%)</b></td><td>32.48 <b>(+36.62%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.40 (n/a)</td><td>158.74 (n/a)</td><td>169.30 (n/a)</td><td>128.90 (n/a)</td><td>23.78 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (-16.96%)</td><td>0.04 (-7.17%)</td><td>0.05 (-3.42%)</td><td>0.04 <b>(+24.46%)</b></td><td>0.01 <b>(-50.02%)</b></td><td>223.50 (-19.63%)</td><td>187.02 (+2.89%)</td><td>174.70 (+3.56%)</td><td>162.50 <b>(+20.46%)</b></td><td>25.86 <b>(-53.89%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>278.10 (n/a)</td><td>181.76 (n/a)</td><td>168.70 (n/a)</td><td>134.90 (n/a)</td><td>56.09 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (-9.58%)</td><td>0.05 (-1.84%)</td><td>0.05 (+18.71%)</td><td>0.03 (-10.70%)</td><td>0.01 (-4.51%)</td><td>236.20 (+11.94%)</td><td>176.28 (+2.31%)</td><td>157.10 (-15.76%)</td><td>142.40 (+10.64%)</td><td>39.95 (+18.83%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.00 (n/a)</td><td>172.30 (n/a)</td><td>186.50 (n/a)</td><td>128.70 (n/a)</td><td>33.62 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 <b>(-20.92%)</b></td><td>0.05 (-8.67%)</td><td>0.05 (-7.72%)</td><td>0.04 (+5.74%)</td><td>0.01 <b>(-51.27%)</b></td><td>188.50 (-5.42%)</td><td>167.68 (+6.37%)</td><td>167.50 (+8.34%)</td><td>137.70 <b>(+26.45%)</b></td><td>20.04 <b>(-40.59%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.30 (n/a)</td><td>157.64 (n/a)</td><td>154.60 (n/a)</td><td>108.90 (n/a)</td><td>33.74 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (-18.72%)</td><td>0.04 (-11.76%)</td><td>0.04 (-12.88%)</td><td>0.04 (+0.50%)</td><td>0.00 <b>(-63.64%)</b></td><td>221.90 (-0.49%)</td><td>195.92 (+10.18%)</td><td>190.90 (+14.79%)</td><td>177.60 <b>(+22.99%)</b></td><td>16.84 <b>(-54.56%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>177.82 (n/a)</td><td>166.30 (n/a)</td><td>144.40 (n/a)</td><td>37.07 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 <b>(+34.40%)</b></td><td>0.05 <b>(+23.22%)</b></td><td>0.05 (-0.22%)</td><td>0.04 <b>(+37.94%)</b></td><td>0.01 <b>(+21.19%)</b></td><td>189.90 <b>(-27.49%)</b></td><td>155.16 (-19.44%)</td><td>165.10 (+0.18%)</td><td>119.70 <b>(-25.56%)</b></td><td>28.76 <b>(-34.47%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>261.90 (n/a)</td><td>192.60 (n/a)</td><td>164.80 (n/a)</td><td>160.80 (n/a)</td><td>43.89 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (-5.58%)</td><td>0.04 (-4.05%)</td><td>0.04 (-9.11%)</td><td>0.03 (+4.30%)</td><td>0.00 <b>(-31.95%)</b></td><td>234.10 (-4.10%)</td><td>215.76 (+3.57%)</td><td>220.80 (+10.01%)</td><td>191.50 (+5.92%)</td><td>17.70 <b>(-31.19%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>244.10 (n/a)</td><td>208.32 (n/a)</td><td>200.70 (n/a)</td><td>180.80 (n/a)</td><td>25.72 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 <b>(+32.68%)</b></td><td>0.06 (+17.82%)</td><td>0.06 <b>(+20.16%)</b></td><td>0.04 (+16.50%)</td><td>0.01 <b>(+76.74%)</b></td><td>192.50 (-14.14%)</td><td>153.28 (-13.65%)</td><td>143.30 (-16.73%)</td><td>116.20 <b>(-24.59%)</b></td><td>31.63 (+14.42%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>177.50 (n/a)</td><td>172.10 (n/a)</td><td>154.10 (n/a)</td><td>27.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (+3.39%)</td><td>0.04 (+1.36%)</td><td>0.04 (+3.52%)</td><td>0.03 (+13.81%)</td><td>0.01 <b>(-20.69%)</b></td><td>282.40 (-12.13%)</td><td>223.00 (-3.08%)</td><td>216.00 (-3.40%)</td><td>179.00 (-3.30%)</td><td>37.60 <b>(-31.64%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>321.40 (n/a)</td><td>230.08 (n/a)</td><td>223.60 (n/a)</td><td>185.10 (n/a)</td><td>55.00 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 <b>(-31.91%)</b></td><td>0.04 <b>(-22.42%)</b></td><td>0.04 <b>(-32.23%)</b></td><td>0.04 (+13.92%)</td><td>0.01 <b>(-66.63%)</b></td><td>231.10 (-12.23%)</td><td>203.78 (+17.43%)</td><td>215.70 <b>(+47.54%)</b></td><td>162.00 <b>(+46.87%)</b></td><td>27.71 <b>(-57.98%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>263.30 (n/a)</td><td>173.54 (n/a)</td><td>146.20 (n/a)</td><td>110.30 (n/a)</td><td>65.96 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 <b>(-24.61%)</b></td><td>0.04 (-14.30%)</td><td>0.04 (-2.59%)</td><td>0.02 <b>(-40.43%)</b></td><td>0.01 (-0.49%)</td><td>351.00 <b>(+67.86%)</b></td><td>216.50 <b>(+21.74%)</b></td><td>194.70 (+2.64%)</td><td>164.80 <b>(+32.69%)</b></td><td>77.13 <b>(+134.60%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.10 (n/a)</td><td>177.84 (n/a)</td><td>189.70 (n/a)</td><td>124.20 (n/a)</td><td>32.88 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (+14.16%)</td><td>0.05 (+8.95%)</td><td>0.05 (+3.76%)</td><td>0.04 (+1.11%)</td><td>0.01 (+13.87%)</td><td>230.80 (-1.11%)</td><td>168.92 (-7.80%)</td><td>162.20 (-3.62%)</td><td>131.90 (-12.42%)</td><td>37.38 (+2.59%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>233.40 (n/a)</td><td>183.22 (n/a)</td><td>168.30 (n/a)</td><td>150.60 (n/a)</td><td>36.43 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 <b>(+30.44%)</b></td><td>0.05 (+12.62%)</td><td>0.05 (+5.93%)</td><td>0.04 (+2.45%)</td><td>0.01 <b>(+92.05%)</b></td><td>219.90 (-2.40%)</td><td>166.38 (-9.01%)</td><td>170.30 (-5.60%)</td><td>119.00 <b>(-23.32%)</b></td><td>36.61 <b>(+39.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.30 (n/a)</td><td>182.86 (n/a)</td><td>180.40 (n/a)</td><td>155.20 (n/a)</td><td>26.19 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (-12.11%)</td><td>0.04 (+5.91%)</td><td>0.04 <b>(+20.37%)</b></td><td>0.03 <b>(+21.84%)</b></td><td>0.01 <b>(-46.51%)</b></td><td>236.70 (-17.90%)</td><td>196.50 (-10.61%)</td><td>197.50 (-16.95%)</td><td>151.70 (+13.80%)</td><td>30.64 <b>(-50.25%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>288.30 (n/a)</td><td>219.82 (n/a)</td><td>237.80 (n/a)</td><td>133.30 (n/a)</td><td>61.58 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (-4.83%)</td><td>0.05 (+6.02%)</td><td>0.05 (+15.62%)</td><td>0.04 (+8.46%)</td><td>0.01 <b>(-29.54%)</b></td><td>200.50 (-7.82%)</td><td>171.48 (-7.64%)</td><td>178.40 (-13.52%)</td><td>132.40 (+5.08%)</td><td>25.17 <b>(-32.78%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.50 (n/a)</td><td>185.66 (n/a)</td><td>206.30 (n/a)</td><td>126.00 (n/a)</td><td>37.44 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.18 (-0.00%)</td><td>0.18 (+0.04%)</td><td>0.18 (+0.10%)</td><td>0.18 (-0.20%)</td><td>0.00 <b>(+47.73%)</b></td><td>47702.20 (+0.20%)</td><td>47507.62 (-0.04%)</td><td>47455.20 (-0.10%)</td><td>47438.10 (+0.00%)</td><td>111.40 <b>(+47.94%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47606.70 (n/a)</td><td>47527.80 (n/a)</td><td>47502.50 (n/a)</td><td>47436.00 (n/a)</td><td>75.30 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.19 (+17.78%)</td><td>0.18 <b>(+22.03%)</b></td><td>0.18 <b>(+27.22%)</b></td><td>0.16 <b>(+20.71%)</b></td><td>0.01 <b>(+30.63%)</b></td><td>156.60 (-17.19%)</td><td>139.86 (-17.97%)</td><td>133.00 <b>(-21.39%)</b></td><td>129.40 (-15.09%)</td><td>12.29 (-8.61%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>189.10 (n/a)</td><td>170.50 (n/a)</td><td>169.20 (n/a)</td><td>152.40 (n/a)</td><td>13.45 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.31 <b>(+26.55%)</b></td><td>0.28 <b>(+32.88%)</b></td><td>0.29 <b>(+43.50%)</b></td><td>0.22 (+18.03%)</td><td>0.03 <b>(+44.51%)</b></td><td>184.00 (-15.29%)</td><td>147.94 <b>(-24.43%)</b></td><td>141.30 <b>(-30.33%)</b></td><td>133.70 <b>(-20.93%)</b></td><td>20.72 (-1.85%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>217.20 (n/a)</td><td>195.76 (n/a)</td><td>202.80 (n/a)</td><td>169.10 (n/a)</td><td>21.11 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (+18.65%)</td><td>0.03 (+8.06%)</td><td>0.03 (+3.79%)</td><td>0.03 (+7.16%)</td><td>0.00 <b>(+81.17%)</b></td><td>186.60 (-6.70%)</td><td>166.60 (-6.56%)</td><td>172.00 (-3.64%)</td><td>132.20 (-15.69%)</td><td>22.06 <b>(+42.21%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>200.00 (n/a)</td><td>178.30 (n/a)</td><td>178.50 (n/a)</td><td>156.80 (n/a)</td><td>15.51 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (-1.66%)</td><td>0.06 (+0.87%)</td><td>0.05 (-11.79%)</td><td>0.05 <b>(+26.60%)</b></td><td>0.01 (-2.21%)</td><td>181.80 <b>(-21.03%)</b></td><td>148.84 (-2.41%)</td><td>157.70 (+13.37%)</td><td>114.00 (+1.60%)</td><td>32.67 <b>(-27.78%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.20 (n/a)</td><td>152.52 (n/a)</td><td>139.10 (n/a)</td><td>112.20 (n/a)</td><td>45.24 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.09 (+15.73%)</td><td>0.06 (-5.84%)</td><td>0.06 (-7.23%)</td><td>0.03 <b>(-45.29%)</b></td><td>0.02 <b>(+180.22%)</b></td><td>372.80 <b>(+82.83%)</b></td><td>214.36 (+18.09%)</td><td>194.50 (+7.76%)</td><td>132.80 (-13.60%)</td><td>92.53 <b>(+372.78%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>203.90 (n/a)</td><td>181.52 (n/a)</td><td>180.50 (n/a)</td><td>153.70 (n/a)</td><td>19.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (+8.45%)</td><td>0.06 (+4.27%)</td><td>0.06 (+9.68%)</td><td>0.05 (-3.84%)</td><td>0.01 <b>(+108.49%)</b></td><td>172.00 (+3.99%)</td><td>149.04 (-3.09%)</td><td>138.50 (-8.82%)</td><td>129.70 (-7.82%)</td><td>19.55 <b>(+103.40%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>165.40 (n/a)</td><td>153.80 (n/a)</td><td>151.90 (n/a)</td><td>140.70 (n/a)</td><td>9.61 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.08 (+16.20%)</td><td>0.06 (+4.25%)</td><td>0.06 (+7.02%)</td><td>0.04 <b>(-23.20%)</b></td><td>0.02 <b>(+139.23%)</b></td><td>249.10 <b>(+30.21%)</b></td><td>176.10 (+0.62%)</td><td>174.00 (-6.55%)</td><td>130.80 (-13.95%)</td><td>48.68 <b>(+158.09%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>175.02 (n/a)</td><td>186.20 (n/a)</td><td>152.00 (n/a)</td><td>18.86 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (-9.82%)</td><td>0.05 (+0.68%)</td><td>0.05 (-2.26%)</td><td>0.05 <b>(+24.45%)</b></td><td>0.01 <b>(-47.58%)</b></td><td>176.00 (-19.63%)</td><td>160.36 (-3.29%)</td><td>166.60 (+2.27%)</td><td>134.00 (+10.93%)</td><td>16.07 <b>(-54.09%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.00 (n/a)</td><td>165.82 (n/a)</td><td>162.90 (n/a)</td><td>120.80 (n/a)</td><td>35.00 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.08 (+8.56%)</td><td>0.06 (+1.65%)</td><td>0.06 (-0.23%)</td><td>0.05 (-3.91%)</td><td>0.01 <b>(+67.42%)</b></td><td>203.40 (+4.04%)</td><td>163.54 (+0.45%)</td><td>159.50 (+0.25%)</td><td>126.80 (-7.85%)</td><td>33.38 <b>(+59.26%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>195.50 (n/a)</td><td>162.80 (n/a)</td><td>159.10 (n/a)</td><td>137.60 (n/a)</td><td>20.96 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (-0.02%)</td><td>0.05 (-1.10%)</td><td>0.05 (+5.24%)</td><td>0.04 (+5.13%)</td><td>0.01 (-14.07%)</td><td>185.00 (-4.84%)</td><td>166.28 (-0.20%)</td><td>176.00 (-4.97%)</td><td>118.60 (+0.00%)</td><td>27.01 <b>(-22.63%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.40 (n/a)</td><td>166.62 (n/a)</td><td>185.20 (n/a)</td><td>118.60 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (-1.15%)</td><td>0.06 (+5.05%)</td><td>0.06 <b>(+29.12%)</b></td><td>0.04 (-17.59%)</td><td>0.01 (+18.34%)</td><td>239.00 <b>(+21.32%)</b></td><td>167.44 (-2.85%)</td><td>146.00 <b>(-22.55%)</b></td><td>127.60 (+1.19%)</td><td>44.43 <b>(+47.54%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>197.00 (n/a)</td><td>172.36 (n/a)</td><td>188.50 (n/a)</td><td>126.10 (n/a)</td><td>30.12 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.07 (+7.83%)</td><td>0.06 (+11.06%)</td><td>0.06 <b>(+31.09%)</b></td><td>0.03 <b>(-30.34%)</b></td><td>0.02 <b>(+94.41%)</b></td><td>266.70 <b>(+43.54%)</b></td><td>162.24 (-2.97%)</td><td>132.40 <b>(-23.69%)</b></td><td>117.40 (-7.19%)</td><td>62.67 <b>(+161.99%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>185.80 (n/a)</td><td>167.20 (n/a)</td><td>173.50 (n/a)</td><td>126.50 (n/a)</td><td>23.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (-4.33%)</td><td>0.05 (-5.13%)</td><td>0.05 (+12.65%)</td><td>0.03 <b>(-32.39%)</b></td><td>0.01 <b>(+76.38%)</b></td><td>291.10 <b>(+47.92%)</b></td><td>197.80 (+9.93%)</td><td>169.00 (-11.24%)</td><td>156.60 (+4.54%)</td><td>56.30 <b>(+169.39%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>196.80 (n/a)</td><td>179.94 (n/a)</td><td>190.40 (n/a)</td><td>149.80 (n/a)</td><td>20.90 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (+10.90%)</td><td>0.05 (+2.52%)</td><td>0.05 (+1.20%)</td><td>0.04 (-12.43%)</td><td>0.01 <b>(+101.22%)</b></td><td>224.30 (+14.21%)</td><td>177.52 (-0.70%)</td><td>178.90 (-1.16%)</td><td>142.40 (-9.82%)</td><td>30.89 <b>(+109.01%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>196.40 (n/a)</td><td>178.78 (n/a)</td><td>181.00 (n/a)</td><td>157.90 (n/a)</td><td>14.78 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.05 (-3.48%)</td><td>0.04 (-5.34%)</td><td>0.04 (-8.09%)</td><td>0.03 (-6.70%)</td><td>0.01 (+4.66%)</td><td>310.40 (+7.18%)</td><td>222.52 (+6.27%)</td><td>213.30 (+8.77%)</td><td>175.00 (+3.61%)</td><td>52.68 (+13.55%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>289.60 (n/a)</td><td>209.40 (n/a)</td><td>196.10 (n/a)</td><td>168.90 (n/a)</td><td>46.39 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 <b>(+36.78%)</b></td><td>0.04 (+17.84%)</td><td>0.05 (+18.18%)</td><td>0.03 (+7.32%)</td><td>0.01 <b>(+68.73%)</b></td><td>297.80 (-6.82%)</td><td>195.80 (-12.39%)</td><td>167.80 (-15.38%)</td><td>143.10 <b>(-26.92%)</b></td><td>62.45 (+15.81%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>319.60 (n/a)</td><td>223.48 (n/a)</td><td>198.30 (n/a)</td><td>195.80 (n/a)</td><td>53.93 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.06 (+0.91%)</td><td>0.04 (-10.04%)</td><td>0.05 (-5.30%)</td><td>0.03 <b>(-29.75%)</b></td><td>0.01 <b>(+60.93%)</b></td><td>308.80 <b>(+42.30%)</b></td><td>209.52 (+16.96%)</td><td>182.10 (+5.63%)</td><td>140.60 (-0.92%)</td><td>64.73 <b>(+132.35%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.00 (n/a)</td><td>179.14 (n/a)</td><td>172.40 (n/a)</td><td>141.90 (n/a)</td><td>27.86 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (-4.19%)</td><td>0.04 (+8.95%)</td><td>0.04 (+5.70%)</td><td>0.03 <b>(+37.92%)</b></td><td>0.00 <b>(-70.38%)</b></td><td>238.40 <b>(-27.49%)</b></td><td>219.94 (-10.56%)</td><td>213.80 (-5.36%)</td><td>213.10 (+4.36%)</td><td>10.83 <b>(-78.12%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>328.80 (n/a)</td><td>245.92 (n/a)</td><td>225.90 (n/a)</td><td>204.20 (n/a)</td><td>49.50 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.78 (-3.95%)</td><td>0.65 (-2.77%)</td><td>0.67 (+0.58%)</td><td>0.50 (-13.59%)</td><td>0.11 (+18.32%)</td><td>197.20 (+15.73%)</td><td>155.40 (+3.92%)</td><td>147.80 (-0.61%)</td><td>125.80 (+4.05%)</td><td>28.96 <b>(+41.20%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.81 (n/a)</td><td>0.67 (n/a)</td><td>0.66 (n/a)</td><td>0.58 (n/a)</td><td>0.10 (n/a)</td><td>170.40 (n/a)</td><td>149.54 (n/a)</td><td>148.70 (n/a)</td><td>120.90 (n/a)</td><td>20.51 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.73 (+5.40%)</td><td>0.63 (+12.21%)</td><td>0.66 (+18.06%)</td><td>0.52 (+3.74%)</td><td>0.08 (+3.09%)</td><td>189.90 (-3.60%)</td><td>157.38 (-10.91%)</td><td>148.70 (-15.27%)</td><td>134.10 (-5.10%)</td><td>21.60 (-5.19%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.70 (n/a)</td><td>0.56 (n/a)</td><td>0.56 (n/a)</td><td>0.50 (n/a)</td><td>0.08 (n/a)</td><td>197.00 (n/a)</td><td>176.66 (n/a)</td><td>175.50 (n/a)</td><td>141.30 (n/a)</td><td>22.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.60 <b>(-20.49%)</b></td><td>0.55 (-10.22%)</td><td>0.55 (-0.43%)</td><td>0.51 (+6.06%)</td><td>0.03 <b>(-74.12%)</b></td><td>194.00 (-5.69%)</td><td>180.66 (+7.75%)</td><td>180.40 (+0.45%)</td><td>164.30 <b>(+25.80%)</b></td><td>10.97 <b>(-68.29%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.75 (n/a)</td><td>0.61 (n/a)</td><td>0.55 (n/a)</td><td>0.48 (n/a)</td><td>0.13 (n/a)</td><td>205.70 (n/a)</td><td>167.66 (n/a)</td><td>179.60 (n/a)</td><td>130.60 (n/a)</td><td>34.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.69 (+11.35%)</td><td>0.50 (-7.68%)</td><td>0.53 (+0.89%)</td><td>0.31 <b>(-36.38%)</b></td><td>0.14 <b>(+212.28%)</b></td><td>312.60 <b>(+57.16%)</b></td><td>211.48 (+15.84%)</td><td>183.90 (-0.86%)</td><td>143.10 (-10.17%)</td><td>66.47 <b>(+357.12%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.62 (n/a)</td><td>0.54 (n/a)</td><td>0.53 (n/a)</td><td>0.49 (n/a)</td><td>0.05 (n/a)</td><td>198.90 (n/a)</td><td>182.56 (n/a)</td><td>185.50 (n/a)</td><td>159.30 (n/a)</td><td>14.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.58 (+0.19%)</td><td>0.40 (-17.54%)</td><td>0.40 <b>(-22.80%)</b></td><td>0.20 <b>(-42.66%)</b></td><td>0.13 <b>(+38.61%)</b></td><td>364.20 <b>(+74.43%)</b></td><td>207.96 <b>(+31.62%)</b></td><td>184.40 <b>(+29.49%)</b></td><td>126.80 (-0.16%)</td><td>90.76 <b>(+160.84%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.58 (n/a)</td><td>0.48 (n/a)</td><td>0.52 (n/a)</td><td>0.35 (n/a)</td><td>0.10 (n/a)</td><td>208.80 (n/a)</td><td>158.00 (n/a)</td><td>142.40 (n/a)</td><td>127.00 (n/a)</td><td>34.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.58 (+3.59%)</td><td>0.44 (-2.80%)</td><td>0.43 (-8.18%)</td><td>0.33 (-6.43%)</td><td>0.11 (+14.74%)</td><td>222.50 (+6.87%)</td><td>175.82 (+4.12%)</td><td>170.00 (+8.90%)</td><td>126.70 (-3.43%)</td><td>42.26 (+17.08%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.56 (n/a)</td><td>0.45 (n/a)</td><td>0.47 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>208.20 (n/a)</td><td>168.86 (n/a)</td><td>156.10 (n/a)</td><td>131.20 (n/a)</td><td>36.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.57 (+14.07%)</td><td>0.46 (+6.07%)</td><td>0.43 (+1.40%)</td><td>0.34 (-8.80%)</td><td>0.10 <b>(+101.01%)</b></td><td>216.90 (+9.66%)</td><td>166.26 (-3.20%)</td><td>170.90 (-1.38%)</td><td>130.20 (-12.32%)</td><td>35.76 <b>(+87.47%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.43 (n/a)</td><td>0.37 (n/a)</td><td>0.05 (n/a)</td><td>197.80 (n/a)</td><td>171.76 (n/a)</td><td>173.30 (n/a)</td><td>148.50 (n/a)</td><td>19.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.43 (-1.65%)</td><td>0.37 (+12.99%)</td><td>0.37 (+15.78%)</td><td>0.31 <b>(+34.16%)</b></td><td>0.05 <b>(-32.12%)</b></td><td>234.70 <b>(-25.44%)</b></td><td>200.76 (-13.67%)</td><td>196.90 (-13.60%)</td><td>172.40 (+1.65%)</td><td>26.64 <b>(-49.21%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.43 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.23 (n/a)</td><td>0.07 (n/a)</td><td>314.80 (n/a)</td><td>232.54 (n/a)</td><td>227.90 (n/a)</td><td>169.60 (n/a)</td><td>52.45 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.94 (-8.81%)</td><td>0.69 (-14.59%)</td><td>0.63 <b>(-20.23%)</b></td><td>0.59 (-11.76%)</td><td>0.15 (+8.89%)</td><td>222.90 (+13.32%)</td><td>195.62 (+18.30%)</td><td>209.40 <b>(+25.39%)</b></td><td>139.50 (+9.58%)</td><td>35.11 <b>(+38.97%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.03 (n/a)</td><td>0.81 (n/a)</td><td>0.78 (n/a)</td><td>0.67 (n/a)</td><td>0.14 (n/a)</td><td>196.70 (n/a)</td><td>165.36 (n/a)</td><td>167.00 (n/a)</td><td>127.30 (n/a)</td><td>25.26 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.91 <b>(-24.97%)</b></td><td>0.63 <b>(-32.30%)</b></td><td>0.57 <b>(-37.16%)</b></td><td>0.35 <b>(-54.37%)</b></td><td>0.22 <b>(+34.78%)</b></td><td>375.40 <b>(+119.15%)</b></td><td>231.08 <b>(+61.59%)</b></td><td>230.60 <b>(+59.14%)</b></td><td>144.20 <b>(+33.27%)</b></td><td>91.10 <b>(+301.14%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.21 (n/a)</td><td>0.94 (n/a)</td><td>0.90 (n/a)</td><td>0.77 (n/a)</td><td>0.17 (n/a)</td><td>171.30 (n/a)</td><td>143.00 (n/a)</td><td>144.90 (n/a)</td><td>108.20 (n/a)</td><td>22.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.89 <b>(-20.94%)</b></td><td>0.65 <b>(-30.02%)</b></td><td>0.59 <b>(-32.18%)</b></td><td>0.47 <b>(-34.52%)</b></td><td>0.16 (-6.76%)</td><td>279.70 <b>(+52.76%)</b></td><td>212.14 <b>(+45.56%)</b></td><td>222.70 <b>(+47.39%)</b></td><td>147.00 <b>(+26.51%)</b></td><td>49.70 <b>(+81.49%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.13 (n/a)</td><td>0.93 (n/a)</td><td>0.87 (n/a)</td><td>0.72 (n/a)</td><td>0.17 (n/a)</td><td>183.10 (n/a)</td><td>145.74 (n/a)</td><td>151.10 (n/a)</td><td>116.20 (n/a)</td><td>27.39 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.04 (+16.46%)</td><td>0.02 (-12.27%)</td><td>0.02 <b>(-20.45%)</b></td><td>0.02 <b>(-24.03%)</b></td><td>0.01 <b>(+106.05%)</b></td><td>249.90 <b>(+31.60%)</b></td><td>182.02 <b>(+21.61%)</b></td><td>179.10 <b>(+25.68%)</b></td><td>105.90 (-14.11%)</td><td>54.23 <b>(+120.54%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>189.90 (n/a)</td><td>149.68 (n/a)</td><td>142.50 (n/a)</td><td>123.30 (n/a)</td><td>24.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (-1.31%)</td><td>0.02 (-3.51%)</td><td>0.03 (+1.82%)</td><td>0.02 <b>(-24.48%)</b></td><td>0.01 <b>(+76.99%)</b></td><td>252.30 <b>(+32.37%)</b></td><td>177.30 (+7.18%)</td><td>163.30 (-1.74%)</td><td>140.30 (+1.37%)</td><td>45.26 <b>(+142.60%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.60 (n/a)</td><td>165.42 (n/a)</td><td>166.20 (n/a)</td><td>138.40 (n/a)</td><td>18.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (+5.47%)</td><td>0.02 (-3.08%)</td><td>0.02 (+4.09%)</td><td>0.02 (-8.81%)</td><td>0.01 <b>(+45.72%)</b></td><td>237.80 (+9.64%)</td><td>182.04 (+6.96%)</td><td>167.40 (-3.90%)</td><td>127.80 (-5.19%)</td><td>51.39 <b>(+59.85%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.90 (n/a)</td><td>170.20 (n/a)</td><td>174.20 (n/a)</td><td>134.80 (n/a)</td><td>32.15 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.99 (-1.80%)</td><td>0.79 (-0.30%)</td><td>0.73 (-5.21%)</td><td>0.72 (+5.34%)</td><td>0.11 (-8.24%)</td><td>183.20 (-5.08%)</td><td>168.80 (+0.01%)</td><td>180.80 (+5.48%)</td><td>133.20 (+1.83%)</td><td>21.13 (-8.84%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.01 (n/a)</td><td>0.80 (n/a)</td><td>0.77 (n/a)</td><td>0.68 (n/a)</td><td>0.13 (n/a)</td><td>193.00 (n/a)</td><td>168.78 (n/a)</td><td>171.40 (n/a)</td><td>130.80 (n/a)</td><td>23.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.00 (+0.09%)</td><td>0.81 (+6.84%)</td><td>0.83 (+17.08%)</td><td>0.61 (-3.75%)</td><td>0.17 (+18.86%)</td><td>215.20 (+3.91%)</td><td>169.64 (-5.26%)</td><td>159.70 (-14.60%)</td><td>132.70 (-0.15%)</td><td>36.37 <b>(+27.60%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.99 (n/a)</td><td>0.76 (n/a)</td><td>0.71 (n/a)</td><td>0.64 (n/a)</td><td>0.14 (n/a)</td><td>207.10 (n/a)</td><td>179.06 (n/a)</td><td>187.00 (n/a)</td><td>132.90 (n/a)</td><td>28.51 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.96 <b>(+40.53%)</b></td><td>0.80 <b>(+24.18%)</b></td><td>0.86 <b>(+31.16%)</b></td><td>0.55 (-3.79%)</td><td>0.16 <b>(+250.69%)</b></td><td>240.00 (+3.94%)</td><td>170.82 (-16.78%)</td><td>153.80 <b>(-23.75%)</b></td><td>137.50 <b>(-28.83%)</b></td><td>40.41 <b>(+167.24%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.68 (n/a)</td><td>0.65 (n/a)</td><td>0.65 (n/a)</td><td>0.57 (n/a)</td><td>0.04 (n/a)</td><td>230.90 (n/a)</td><td>205.26 (n/a)</td><td>201.70 (n/a)</td><td>193.20 (n/a)</td><td>15.12 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.03 (+7.42%)</td><td>0.85 (+4.12%)</td><td>0.88 (+1.46%)</td><td>0.57 (-9.55%)</td><td>0.17 <b>(+24.84%)</b></td><td>230.50 (+10.55%)</td><td>162.20 (-2.47%)</td><td>149.30 (-1.45%)</td><td>127.70 (-6.92%)</td><td>39.79 <b>(+33.69%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.96 (n/a)</td><td>0.81 (n/a)</td><td>0.87 (n/a)</td><td>0.63 (n/a)</td><td>0.14 (n/a)</td><td>208.50 (n/a)</td><td>166.30 (n/a)</td><td>151.50 (n/a)</td><td>137.20 (n/a)</td><td>29.76 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.94 (-1.06%)</td><td>0.81 (-3.79%)</td><td>0.82 (-5.42%)</td><td>0.72 (+5.70%)</td><td>0.08 <b>(-27.99%)</b></td><td>182.60 (-5.44%)</td><td>163.94 (+3.08%)</td><td>161.10 (+5.71%)</td><td>140.20 (+1.08%)</td><td>16.31 <b>(-30.37%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.95 (n/a)</td><td>0.84 (n/a)</td><td>0.87 (n/a)</td><td>0.68 (n/a)</td><td>0.12 (n/a)</td><td>193.10 (n/a)</td><td>159.04 (n/a)</td><td>152.40 (n/a)</td><td>138.70 (n/a)</td><td>23.42 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (-5.29%)</td><td>0.02 (+0.21%)</td><td>0.02 (-1.83%)</td><td>0.02 <b>(+34.97%)</b></td><td>0.00 <b>(-39.67%)</b></td><td>211.00 <b>(-25.91%)</b></td><td>170.68 (-4.89%)</td><td>165.20 (+1.85%)</td><td>145.40 (+5.59%)</td><td>26.76 <b>(-55.38%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>284.80 (n/a)</td><td>179.46 (n/a)</td><td>162.20 (n/a)</td><td>137.70 (n/a)</td><td>59.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.03 (+7.56%)</td><td>0.02 (+4.45%)</td><td>0.02 (+10.42%)</td><td>0.02 (-3.15%)</td><td>0.00 <b>(+33.85%)</b></td><td>216.60 (+3.29%)</td><td>173.40 (-3.44%)</td><td>165.10 (-9.43%)</td><td>141.30 (-7.04%)</td><td>28.05 <b>(+30.81%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.70 (n/a)</td><td>179.58 (n/a)</td><td>182.30 (n/a)</td><td>152.00 (n/a)</td><td>21.44 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.00 (+2.22%)</td><td>0.00 (+4.72%)</td><td>0.00 (+2.33%)</td><td>0.00 (+7.50%)</td><td>0.00 <b>(-22.20%)</b></td><td>953.37 (-6.65%)</td><td>924.17 (-4.78%)</td><td>933.67 (-2.97%)</td><td>893.29 (-1.10%)</td><td>28.40 <b>(-39.18%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1021.27 (n/a)</td><td>970.59 (n/a)</td><td>962.28 (n/a)</td><td>903.26 (n/a)</td><td>46.69 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>0.01 (+0.00%)</td><td>0.01 (+0.00%)</td><td>0.01 (-4.65%)</td><td>0.01 (+9.86%)</td><td>0.00 <b>(-45.77%)</b></td><td>1054.03 (-8.94%)</td><td>1002.43 (-0.32%)</td><td>1003.61 (+4.94%)</td><td>948.91 (-0.38%)</td><td>45.21 <b>(-48.65%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1157.57 (n/a)</td><td>1005.69 (n/a)</td><td>956.33 (n/a)</td><td>952.56 (n/a)</td><td>88.03 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>1.00 (-1.62%)</td><td>0.97 (-0.95%)</td><td>0.96 (-1.38%)</td><td>0.94 (-0.66%)</td><td>0.02 (-6.70%)</td><td>2224.18 (+0.67%)</td><td>2167.46 (+0.95%)</td><td>2184.06 (+1.40%)</td><td>2103.51 (+1.65%)</td><td>52.62 (-4.64%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>1.01 (n/a)</td><td>0.98 (n/a)</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.03 (n/a)</td><td>2209.43 (n/a)</td><td>2147.04 (n/a)</td><td>2153.91 (n/a)</td><td>2069.37 (n/a)</td><td>55.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>3.57 (-9.59%)</td><td>2.92 (-0.47%)</td><td>2.61 (-8.82%)</td><td>2.44 (+4.68%)</td><td>0.52 (-19.56%)</td><td>214.90 (-4.45%)</td><td>183.88 (-0.62%)</td><td>200.70 (+9.67%)</td><td>147.00 (+10.61%)</td><td>30.70 (-16.13%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>3.94 (n/a)</td><td>2.93 (n/a)</td><td>2.86 (n/a)</td><td>2.33 (n/a)</td><td>0.64 (n/a)</td><td>224.90 (n/a)</td><td>185.02 (n/a)</td><td>183.00 (n/a)</td><td>132.90 (n/a)</td><td>36.60 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>6.81 <b>(+22.33%)</b></td><td>5.04 (+10.88%)</td><td>4.86 (+13.28%)</td><td>3.96 (-1.27%)</td><td>1.08 <b>(+78.87%)</b></td><td>264.80 (+1.26%)</td><td>214.80 (-7.98%)</td><td>215.60 (-11.75%)</td><td>154.00 (-18.22%)</td><td>41.07 <b>(+47.54%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>5.57 (n/a)</td><td>4.55 (n/a)</td><td>4.29 (n/a)</td><td>4.01 (n/a)</td><td>0.61 (n/a)</td><td>261.50 (n/a)</td><td>233.42 (n/a)</td><td>244.30 (n/a)</td><td>188.30 (n/a)</td><td>27.84 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:37:29</td><td>3.35 (-18.81%)</td><td>2.94 (+6.30%)</td><td>2.96 (+13.27%)</td><td>2.46 (+15.27%)</td><td>0.34 <b>(-57.39%)</b></td><td>212.80 (-13.25%)</td><td>180.44 (-9.84%)</td><td>177.30 (-11.70%)</td><td>156.50 <b>(+23.23%)</b></td><td>21.66 <b>(-53.05%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 03:32:57</td><td>4.13 (n/a)</td><td>2.76 (n/a)</td><td>2.61 (n/a)</td><td>2.14 (n/a)</td><td>0.80 (n/a)</td><td>245.30 (n/a)</td><td>200.14 (n/a)</td><td>200.80 (n/a)</td><td>127.00 (n/a)</td><td>46.14 (n/a)</td>
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
