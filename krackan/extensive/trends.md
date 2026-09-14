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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (-8.47%)</td><td>0.03 (-3.14%)</td><td>0.03 (-15.32%)</td><td>0.03 <b>(+32.72%)</b></td><td>0.01 <b>(-37.10%)</b></td><td>220.20 <b>(-24.67%)</b></td><td>186.22 (-3.91%)</td><td>188.20 (+18.07%)</td><td>130.60 (+9.29%)</td><td>36.14 <b>(-50.01%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>292.30 (n/a)</td><td>193.80 (n/a)</td><td>159.40 (n/a)</td><td>119.50 (n/a)</td><td>72.31 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (-15.95%)</td><td>0.03 (-10.14%)</td><td>0.03 (-2.65%)</td><td>0.02 <b>(-29.89%)</b></td><td>0.01 (+5.99%)</td><td>307.10 <b>(+42.64%)</b></td><td>207.24 (+14.47%)</td><td>191.10 (+2.74%)</td><td>154.60 (+18.92%)</td><td>61.75 <b>(+80.73%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>181.04 (n/a)</td><td>186.00 (n/a)</td><td>130.00 (n/a)</td><td>34.17 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (+3.33%)</td><td>0.03 (-1.54%)</td><td>0.04 (+11.57%)</td><td>0.02 <b>(-33.52%)</b></td><td>0.01 <b>(+57.81%)</b></td><td>361.90 <b>(+50.48%)</b></td><td>206.84 (+9.96%)</td><td>171.90 (-10.38%)</td><td>138.30 (-3.22%)</td><td>89.21 <b>(+147.49%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>240.50 (n/a)</td><td>188.10 (n/a)</td><td>191.80 (n/a)</td><td>142.90 (n/a)</td><td>36.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 <b>(+26.36%)</b></td><td>0.03 (-0.80%)</td><td>0.03 (-6.38%)</td><td>0.02 (-11.94%)</td><td>0.01 <b>(+93.93%)</b></td><td>261.70 (+13.54%)</td><td>202.88 (+4.57%)</td><td>208.40 (+6.82%)</td><td>128.80 <b>(-20.84%)</b></td><td>47.55 <b>(+66.19%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>230.50 (n/a)</td><td>194.02 (n/a)</td><td>195.10 (n/a)</td><td>162.70 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (+13.79%)</td><td>0.04 (-4.33%)</td><td>0.03 (-8.09%)</td><td>0.03 (-16.98%)</td><td>0.01 <b>(+89.84%)</b></td><td>217.20 <b>(+20.47%)</b></td><td>174.78 (+8.34%)</td><td>180.30 (+8.81%)</td><td>113.50 (-12.15%)</td><td>39.20 <b>(+96.97%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>180.30 (n/a)</td><td>161.32 (n/a)</td><td>165.70 (n/a)</td><td>129.20 (n/a)</td><td>19.90 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (+4.70%)</td><td>0.03 (+18.52%)</td><td>0.03 <b>(+33.84%)</b></td><td>0.03 <b>(+41.78%)</b></td><td>0.00 <b>(-34.85%)</b></td><td>231.20 <b>(-29.47%)</b></td><td>192.74 (-18.86%)</td><td>183.50 <b>(-25.32%)</b></td><td>158.60 (-4.46%)</td><td>28.17 <b>(-55.20%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>327.80 (n/a)</td><td>237.54 (n/a)</td><td>245.70 (n/a)</td><td>166.00 (n/a)</td><td>62.89 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (-12.78%)</td><td>0.03 (-1.76%)</td><td>0.03 (+9.26%)</td><td>0.02 (-1.21%)</td><td>0.00 <b>(-24.19%)</b></td><td>251.50 (+1.21%)</td><td>199.46 (+0.88%)</td><td>184.60 (-8.48%)</td><td>167.10 (+14.69%)</td><td>33.50 (-9.26%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.50 (n/a)</td><td>197.72 (n/a)</td><td>201.70 (n/a)</td><td>145.70 (n/a)</td><td>36.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 <b>(-31.59%)</b></td><td>0.03 (-6.71%)</td><td>0.03 (+7.75%)</td><td>0.03 (+10.02%)</td><td>0.00 <b>(-76.42%)</b></td><td>223.60 (-9.11%)</td><td>207.48 (+1.73%)</td><td>209.50 (-7.18%)</td><td>186.60 <b>(+46.24%)</b></td><td>15.32 <b>(-67.93%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>246.00 (n/a)</td><td>203.96 (n/a)</td><td>225.70 (n/a)</td><td>127.60 (n/a)</td><td>47.78 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.09 <b>(+26.87%)</b></td><td>0.07 (+7.76%)</td><td>0.07 (+8.78%)</td><td>0.05 (-19.71%)</td><td>0.02 <b>(+211.77%)</b></td><td>255.30 <b>(+24.54%)</b></td><td>181.28 (-3.35%)</td><td>174.70 (-8.05%)</td><td>130.70 <b>(-21.22%)</b></td><td>45.42 <b>(+218.44%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>187.56 (n/a)</td><td>190.00 (n/a)</td><td>165.90 (n/a)</td><td>14.26 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (+18.28%)</td><td>0.08 (+8.02%)</td><td>0.07 (-5.23%)</td><td>0.07 <b>(+31.40%)</b></td><td>0.02 (+13.22%)</td><td>181.10 <b>(-23.91%)</b></td><td>160.22 (-8.11%)</td><td>172.10 (+5.52%)</td><td>112.40 (-15.49%)</td><td>28.44 <b>(-29.43%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>238.00 (n/a)</td><td>174.36 (n/a)</td><td>163.10 (n/a)</td><td>133.00 (n/a)</td><td>40.30 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 <b>(-20.60%)</b></td><td>0.08 (-4.91%)</td><td>0.08 (-1.13%)</td><td>0.07 (+0.61%)</td><td>0.01 <b>(-43.65%)</b></td><td>183.70 (-0.60%)</td><td>158.22 (+2.45%)</td><td>159.00 (+1.15%)</td><td>127.00 <b>(+25.99%)</b></td><td>24.13 <b>(-25.98%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>184.80 (n/a)</td><td>154.44 (n/a)</td><td>157.20 (n/a)</td><td>100.80 (n/a)</td><td>32.60 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 <b>(+22.53%)</b></td><td>0.08 (+13.59%)</td><td>0.07 (+6.64%)</td><td>0.06 (+1.52%)</td><td>0.02 <b>(+61.05%)</b></td><td>216.80 (-1.50%)</td><td>167.14 (-10.18%)</td><td>170.60 (-6.21%)</td><td>119.10 (-18.37%)</td><td>36.14 <b>(+28.64%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>220.10 (n/a)</td><td>186.08 (n/a)</td><td>181.90 (n/a)</td><td>145.90 (n/a)</td><td>28.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.09 <b>(+22.13%)</b></td><td>0.07 (+16.41%)</td><td>0.07 (+13.90%)</td><td>0.06 <b>(+55.88%)</b></td><td>0.01 (-16.53%)</td><td>194.30 <b>(-35.85%)</b></td><td>172.82 (-17.00%)</td><td>180.40 (-12.17%)</td><td>129.60 (-18.13%)</td><td>25.03 <b>(-57.12%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>302.90 (n/a)</td><td>208.22 (n/a)</td><td>205.40 (n/a)</td><td>158.30 (n/a)</td><td>58.37 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 <b>(-36.90%)</b></td><td>0.06 (-16.54%)</td><td>0.06 (-13.59%)</td><td>0.05 (+12.93%)</td><td>0.01 <b>(-76.84%)</b></td><td>230.70 (-11.44%)</td><td>205.38 (+10.76%)</td><td>206.90 (+15.78%)</td><td>182.90 <b>(+58.49%)</b></td><td>18.92 <b>(-67.85%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>260.50 (n/a)</td><td>185.42 (n/a)</td><td>178.70 (n/a)</td><td>115.40 (n/a)</td><td>58.86 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (-18.82%)</td><td>0.06 (-6.21%)</td><td>0.06 (-4.43%)</td><td>0.06 (+12.88%)</td><td>0.00 <b>(-70.97%)</b></td><td>222.70 (-11.42%)</td><td>203.86 (+4.34%)</td><td>199.70 (+4.66%)</td><td>196.00 <b>(+23.12%)</b></td><td>11.00 <b>(-68.69%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>251.40 (n/a)</td><td>195.38 (n/a)</td><td>190.80 (n/a)</td><td>159.20 (n/a)</td><td>35.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.08 (-12.82%)</td><td>0.07 (+2.24%)</td><td>0.07 (+12.33%)</td><td>0.06 (+5.54%)</td><td>0.01 <b>(-36.36%)</b></td><td>223.20 (-5.26%)</td><td>190.36 (-4.06%)</td><td>187.20 (-10.98%)</td><td>160.70 (+14.70%)</td><td>26.91 <b>(-30.22%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>235.60 (n/a)</td><td>198.42 (n/a)</td><td>210.30 (n/a)</td><td>140.10 (n/a)</td><td>38.56 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 <b>(-23.41%)</b></td><td>0.14 (-9.73%)</td><td>0.14 (-2.23%)</td><td>0.12 (-4.67%)</td><td>0.02 <b>(-54.27%)</b></td><td>202.30 (+4.93%)</td><td>171.92 (+7.79%)</td><td>171.90 (+2.26%)</td><td>145.80 <b>(+30.53%)</b></td><td>20.66 <b>(-36.69%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>192.80 (n/a)</td><td>159.50 (n/a)</td><td>168.10 (n/a)</td><td>111.70 (n/a)</td><td>32.62 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.24 <b>(+33.94%)</b></td><td>0.17 (+17.11%)</td><td>0.17 <b>(+20.03%)</b></td><td>0.12 (+4.86%)</td><td>0.04 <b>(+106.50%)</b></td><td>199.30 (-4.64%)</td><td>154.46 (-11.63%)</td><td>143.20 (-16.70%)</td><td>104.00 <b>(-25.34%)</b></td><td>37.48 <b>(+49.59%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>209.00 (n/a)</td><td>174.78 (n/a)</td><td>171.90 (n/a)</td><td>139.30 (n/a)</td><td>25.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 (+12.23%)</td><td>0.16 (+14.27%)</td><td>0.16 <b>(+22.15%)</b></td><td>0.13 (+12.24%)</td><td>0.02 <b>(+22.37%)</b></td><td>189.30 (-10.88%)</td><td>160.14 (-12.33%)</td><td>150.60 (-18.15%)</td><td>141.70 (-10.88%)</td><td>19.39 (-2.65%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>182.66 (n/a)</td><td>184.00 (n/a)</td><td>159.00 (n/a)</td><td>19.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (-15.19%)</td><td>0.16 (+4.78%)</td><td>0.15 (+19.06%)</td><td>0.14 <b>(+20.02%)</b></td><td>0.02 <b>(-52.32%)</b></td><td>181.70 (-16.69%)</td><td>159.38 (-8.49%)</td><td>160.70 (-16.00%)</td><td>132.10 (+17.84%)</td><td>19.86 <b>(-51.88%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>218.10 (n/a)</td><td>174.16 (n/a)</td><td>191.30 (n/a)</td><td>112.10 (n/a)</td><td>41.28 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 <b>(+31.68%)</b></td><td>0.13 (+5.51%)</td><td>0.13 (-3.33%)</td><td>0.11 (-1.06%)</td><td>0.03 <b>(+132.41%)</b></td><td>225.90 (+1.07%)</td><td>189.08 (-2.62%)</td><td>195.80 (+3.43%)</td><td>128.90 <b>(-24.04%)</b></td><td>36.02 <b>(+68.47%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>223.50 (n/a)</td><td>194.16 (n/a)</td><td>189.30 (n/a)</td><td>169.70 (n/a)</td><td>21.38 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (-19.72%)</td><td>0.13 (-4.60%)</td><td>0.13 (-1.89%)</td><td>0.12 (+1.11%)</td><td>0.01 <b>(-67.92%)</b></td><td>203.10 (-1.12%)</td><td>192.76 (+3.27%)</td><td>195.40 (+1.93%)</td><td>178.40 <b>(+24.58%)</b></td><td>10.12 <b>(-59.58%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>205.40 (n/a)</td><td>186.66 (n/a)</td><td>191.70 (n/a)</td><td>143.20 (n/a)</td><td>25.04 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (+2.09%)</td><td>0.12 (+6.34%)</td><td>0.12 (+1.21%)</td><td>0.11 <b>(+33.38%)</b></td><td>0.01 <b>(-47.02%)</b></td><td>216.40 <b>(-25.02%)</b></td><td>200.78 (-7.94%)</td><td>201.70 (-1.22%)</td><td>177.70 (-2.04%)</td><td>16.54 <b>(-61.26%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>288.60 (n/a)</td><td>218.10 (n/a)</td><td>204.20 (n/a)</td><td>181.40 (n/a)</td><td>42.69 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (+8.31%)</td><td>0.12 (+11.78%)</td><td>0.12 (+9.16%)</td><td>0.11 <b>(+32.59%)</b></td><td>0.01 <b>(-26.06%)</b></td><td>233.40 <b>(-24.56%)</b></td><td>203.80 (-12.18%)</td><td>211.70 (-8.35%)</td><td>176.60 (-7.68%)</td><td>24.23 <b>(-49.12%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>309.40 (n/a)</td><td>232.06 (n/a)</td><td>231.00 (n/a)</td><td>191.30 (n/a)</td><td>47.61 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.42 <b>(+33.68%)</b></td><td>0.29 (+4.06%)</td><td>0.29 (+2.41%)</td><td>0.19 <b>(-21.64%)</b></td><td>0.09 <b>(+215.86%)</b></td><td>255.90 <b>(+27.63%)</b></td><td>178.64 (+2.07%)</td><td>169.90 (-2.36%)</td><td>115.70 <b>(-25.21%)</b></td><td>52.06 <b>(+200.82%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>200.50 (n/a)</td><td>175.02 (n/a)</td><td>174.00 (n/a)</td><td>154.70 (n/a)</td><td>17.31 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.38 <b>(+26.87%)</b></td><td>0.29 (+6.71%)</td><td>0.27 (+4.33%)</td><td>0.23 (-10.49%)</td><td>0.06 <b>(+167.74%)</b></td><td>218.40 (+11.71%)</td><td>175.34 (-3.74%)</td><td>182.00 (-4.16%)</td><td>130.30 <b>(-21.22%)</b></td><td>34.13 <b>(+134.75%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>195.50 (n/a)</td><td>182.16 (n/a)</td><td>189.90 (n/a)</td><td>165.40 (n/a)</td><td>14.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.32 (-13.42%)</td><td>0.26 (-13.54%)</td><td>0.26 (-10.08%)</td><td>0.24 (-2.40%)</td><td>0.03 <b>(-37.37%)</b></td><td>208.60 (+2.46%)</td><td>187.58 (+14.24%)</td><td>189.40 (+11.22%)</td><td>153.60 (+15.49%)</td><td>20.65 <b>(-26.56%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.37 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>203.60 (n/a)</td><td>164.20 (n/a)</td><td>170.30 (n/a)</td><td>133.00 (n/a)</td><td>28.11 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.37 (-5.52%)</td><td>0.30 (-7.31%)</td><td>0.29 (-3.61%)</td><td>0.25 (+0.07%)</td><td>0.05 <b>(-20.27%)</b></td><td>195.70 (-0.10%)</td><td>167.20 (+6.99%)</td><td>170.40 (+3.78%)</td><td>132.30 (+5.92%)</td><td>24.38 (-14.83%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>195.90 (n/a)</td><td>156.28 (n/a)</td><td>164.20 (n/a)</td><td>124.90 (n/a)</td><td>28.63 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.35 <b>(+37.19%)</b></td><td>0.29 (+18.08%)</td><td>0.31 <b>(+24.52%)</b></td><td>0.18 (-16.76%)</td><td>0.06 <b>(+337.67%)</b></td><td>267.80 <b>(+20.09%)</b></td><td>178.40 (-11.16%)</td><td>158.30 (-19.73%)</td><td>139.60 <b>(-27.14%)</b></td><td>51.18 <b>(+300.69%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.01 (n/a)</td><td>223.00 (n/a)</td><td>200.80 (n/a)</td><td>197.20 (n/a)</td><td>191.60 (n/a)</td><td>12.77 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.41 (+8.79%)</td><td>0.30 (+5.47%)</td><td>0.23 (-17.31%)</td><td>0.22 (-3.04%)</td><td>0.10 <b>(+60.86%)</b></td><td>225.80 (+3.15%)</td><td>177.74 (-0.89%)</td><td>209.60 <b>(+20.95%)</b></td><td>120.20 (-8.10%)</td><td>51.54 <b>(+47.41%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>218.90 (n/a)</td><td>179.34 (n/a)</td><td>173.30 (n/a)</td><td>130.80 (n/a)</td><td>34.97 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.39 <b>(+40.16%)</b></td><td>0.25 (+5.74%)</td><td>0.24 (+1.22%)</td><td>0.16 (-17.75%)</td><td>0.09 <b>(+154.43%)</b></td><td>316.20 <b>(+21.57%)</b></td><td>213.10 (+2.28%)</td><td>205.30 (-1.20%)</td><td>125.80 <b>(-28.68%)</b></td><td>72.62 <b>(+119.66%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>260.10 (n/a)</td><td>208.34 (n/a)</td><td>207.80 (n/a)</td><td>176.40 (n/a)</td><td>33.06 (n/a)</td>
</tr>
</tbody>
</table>


### test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.35 (+11.08%)</td><td>0.26 (+1.07%)</td><td>0.29 (+16.20%)</td><td>0.16 (-13.89%)</td><td>0.08 <b>(+64.75%)</b></td><td>303.90 (+16.13%)</td><td>207.78 (+4.45%)</td><td>167.30 (-13.94%)</td><td>141.60 (-9.92%)</td><td>69.98 <b>(+74.12%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>261.70 (n/a)</td><td>198.92 (n/a)</td><td>194.40 (n/a)</td><td>157.20 (n/a)</td><td>40.19 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (+18.85%)</td><td>0.02 (-8.94%)</td><td>0.01 <b>(-26.29%)</b></td><td>0.01 (-13.74%)</td><td>0.00 <b>(+60.18%)</b></td><td>222.90 (+15.91%)</td><td>182.54 (+13.01%)</td><td>193.90 <b>(+35.69%)</b></td><td>117.90 (-15.85%)</td><td>40.76 <b>(+50.52%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>192.30 (n/a)</td><td>161.52 (n/a)</td><td>142.90 (n/a)</td><td>140.10 (n/a)</td><td>27.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (+12.04%)</td><td>0.01 (-17.33%)</td><td>0.02 (-11.24%)</td><td>0.01 <b>(-34.27%)</b></td><td>0.01 <b>(+122.42%)</b></td><td>320.60 <b>(+52.16%)</b></td><td>220.52 <b>(+36.36%)</b></td><td>174.20 (+12.68%)</td><td>121.40 (-10.80%)</td><td>91.59 <b>(+219.75%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>210.70 (n/a)</td><td>161.72 (n/a)</td><td>154.60 (n/a)</td><td>136.10 (n/a)</td><td>28.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (+11.87%)</td><td>0.02 (-3.85%)</td><td>0.02 (-7.99%)</td><td>0.01 (-7.56%)</td><td>0.00 <b>(+69.46%)</b></td><td>194.00 (+8.20%)</td><td>164.60 (+5.93%)</td><td>169.40 (+8.73%)</td><td>116.90 (-10.63%)</td><td>28.57 <b>(+57.03%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>179.30 (n/a)</td><td>155.38 (n/a)</td><td>155.80 (n/a)</td><td>130.80 (n/a)</td><td>18.20 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (+16.35%)</td><td>0.01 (-1.70%)</td><td>0.01 (-9.88%)</td><td>0.01 (-14.60%)</td><td>0.00 <b>(+44.44%)</b></td><td>267.20 (+17.09%)</td><td>191.30 (+4.62%)</td><td>186.10 (+10.97%)</td><td>125.10 (-14.08%)</td><td>50.62 <b>(+40.68%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>228.20 (n/a)</td><td>182.86 (n/a)</td><td>167.70 (n/a)</td><td>145.60 (n/a)</td><td>35.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (+2.55%)</td><td>0.02 (+6.47%)</td><td>0.02 (+9.87%)</td><td>0.01 (-4.48%)</td><td>0.00 <b>(+38.52%)</b></td><td>214.60 (+4.68%)</td><td>170.00 (-4.14%)</td><td>173.10 (-8.99%)</td><td>130.70 (-2.46%)</td><td>38.69 <b>(+38.90%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>205.00 (n/a)</td><td>177.34 (n/a)</td><td>190.20 (n/a)</td><td>134.00 (n/a)</td><td>27.85 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 <b>(+20.74%)</b></td><td>0.02 (+12.73%)</td><td>0.02 (+10.77%)</td><td>0.01 (+11.13%)</td><td>0.00 <b>(+36.54%)</b></td><td>198.80 (-10.00%)</td><td>160.12 (-10.89%)</td><td>154.10 (-9.72%)</td><td>133.20 (-17.16%)</td><td>24.02 (+1.18%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>220.90 (n/a)</td><td>179.68 (n/a)</td><td>170.70 (n/a)</td><td>160.80 (n/a)</td><td>23.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (+18.70%)</td><td>0.02 (+17.71%)</td><td>0.02 (+19.34%)</td><td>0.01 (+17.30%)</td><td>0.00 <b>(+36.06%)</b></td><td>183.40 (-14.74%)</td><td>161.08 (-14.82%)</td><td>152.60 (-16.20%)</td><td>145.10 (-15.74%)</td><td>18.68 (-1.82%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>215.10 (n/a)</td><td>189.10 (n/a)</td><td>182.10 (n/a)</td><td>172.20 (n/a)</td><td>19.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (+19.01%)</td><td>0.01 (+8.66%)</td><td>0.01 (+9.03%)</td><td>0.01 (-8.89%)</td><td>0.00 <b>(+356.92%)</b></td><td>246.20 (+9.76%)</td><td>198.72 (-6.50%)</td><td>193.90 (-8.28%)</td><td>172.70 (-15.96%)</td><td>29.81 <b>(+318.31%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>224.30 (n/a)</td><td>212.54 (n/a)</td><td>211.40 (n/a)</td><td>205.50 (n/a)</td><td>7.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (+15.58%)</td><td>0.04 (+6.77%)</td><td>0.04 (+14.71%)</td><td>0.02 (-14.12%)</td><td>0.01 <b>(+60.89%)</b></td><td>231.90 (+16.42%)</td><td>151.08 (-2.37%)</td><td>127.60 (-12.84%)</td><td>111.40 (-13.44%)</td><td>48.55 <b>(+67.35%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>199.20 (n/a)</td><td>154.74 (n/a)</td><td>146.40 (n/a)</td><td>128.70 (n/a)</td><td>29.01 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (+0.11%)</td><td>0.03 (+2.40%)</td><td>0.03 (+8.60%)</td><td>0.02 (-5.65%)</td><td>0.00 (+18.52%)</td><td>213.10 (+5.97%)</td><td>168.94 (-1.78%)</td><td>159.30 (-7.92%)</td><td>146.50 (-0.07%)</td><td>25.85 <b>(+28.90%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>201.10 (n/a)</td><td>172.00 (n/a)</td><td>173.00 (n/a)</td><td>146.60 (n/a)</td><td>20.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (+17.31%)</td><td>0.04 (+9.74%)</td><td>0.04 (+5.27%)</td><td>0.03 (+12.24%)</td><td>0.01 <b>(+30.79%)</b></td><td>169.60 (-10.88%)</td><td>143.86 (-8.46%)</td><td>143.30 (-4.97%)</td><td>114.70 (-14.72%)</td><td>21.82 (-1.01%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>190.30 (n/a)</td><td>157.16 (n/a)</td><td>150.80 (n/a)</td><td>134.50 (n/a)</td><td>22.04 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-8.85%)</td><td>0.03 (-0.81%)</td><td>0.03 (-3.74%)</td><td>0.02 (+4.57%)</td><td>0.01 (-18.56%)</td><td>268.80 (-4.38%)</td><td>189.08 (-0.76%)</td><td>174.20 (+3.88%)</td><td>156.00 (+9.70%)</td><td>45.75 (-15.16%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>281.10 (n/a)</td><td>190.52 (n/a)</td><td>167.70 (n/a)</td><td>142.20 (n/a)</td><td>53.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (+4.56%)</td><td>0.03 (-4.51%)</td><td>0.03 (-1.07%)</td><td>0.02 (+4.98%)</td><td>0.01 (-0.86%)</td><td>214.00 (-4.76%)</td><td>176.06 (+4.15%)</td><td>174.20 (+1.10%)</td><td>117.50 (-4.39%)</td><td>37.10 (-10.55%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.70 (n/a)</td><td>169.04 (n/a)</td><td>172.30 (n/a)</td><td>122.90 (n/a)</td><td>41.48 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (+15.08%)</td><td>0.03 (+5.20%)</td><td>0.03 (+2.65%)</td><td>0.03 (-5.95%)</td><td>0.01 <b>(+56.69%)</b></td><td>203.20 (+6.33%)</td><td>166.92 (-2.86%)</td><td>174.20 (-2.57%)</td><td>114.00 (-13.11%)</td><td>33.83 <b>(+44.62%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>171.84 (n/a)</td><td>178.80 (n/a)</td><td>131.20 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (+10.06%)</td><td>0.03 (-7.42%)</td><td>0.03 (-9.87%)</td><td>0.02 (-18.00%)</td><td>0.01 <b>(+117.00%)</b></td><td>220.90 <b>(+21.98%)</b></td><td>186.42 (+10.77%)</td><td>189.30 (+10.96%)</td><td>131.50 (-9.12%)</td><td>33.56 <b>(+132.89%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>181.10 (n/a)</td><td>168.30 (n/a)</td><td>170.60 (n/a)</td><td>144.70 (n/a)</td><td>14.41 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-16.37%)</td><td>0.02 (-1.22%)</td><td>0.02 (-2.65%)</td><td>0.02 <b>(+31.10%)</b></td><td>0.00 <b>(-63.67%)</b></td><td>252.00 <b>(-23.73%)</b></td><td>217.22 (-3.99%)</td><td>217.00 (+2.70%)</td><td>194.80 (+19.58%)</td><td>21.83 <b>(-66.91%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>330.40 (n/a)</td><td>226.24 (n/a)</td><td>211.30 (n/a)</td><td>162.90 (n/a)</td><td>65.96 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 <b>(-35.17%)</b></td><td>0.05 <b>(-31.65%)</b></td><td>0.05 (-18.74%)</td><td>0.03 <b>(-44.96%)</b></td><td>0.01 <b>(-23.41%)</b></td><td>371.90 <b>(+81.68%)</b></td><td>234.74 <b>(+50.47%)</b></td><td>194.00 <b>(+23.10%)</b></td><td>185.00 <b>(+54.30%)</b></td><td>79.02 <b>(+123.76%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>204.70 (n/a)</td><td>156.00 (n/a)</td><td>157.60 (n/a)</td><td>119.90 (n/a)</td><td>35.32 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (-1.57%)</td><td>0.06 (+8.53%)</td><td>0.06 (+13.30%)</td><td>0.06 <b>(+27.56%)</b></td><td>0.00 <b>(-57.68%)</b></td><td>180.10 <b>(-21.63%)</b></td><td>165.44 (-9.99%)</td><td>161.80 (-11.78%)</td><td>152.40 (+1.60%)</td><td>11.87 <b>(-65.21%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.80 (n/a)</td><td>183.80 (n/a)</td><td>183.40 (n/a)</td><td>150.00 (n/a)</td><td>34.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.08 (+2.67%)</td><td>0.06 (+1.03%)</td><td>0.06 (-1.59%)</td><td>0.04 (-4.01%)</td><td>0.01 (+1.95%)</td><td>241.40 (+4.19%)</td><td>175.14 (-0.86%)</td><td>162.70 (+1.62%)</td><td>124.40 (-2.58%)</td><td>43.03 (+2.68%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>231.70 (n/a)</td><td>176.66 (n/a)</td><td>160.10 (n/a)</td><td>127.70 (n/a)</td><td>41.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.09 <b>(+21.56%)</b></td><td>0.07 (+7.97%)</td><td>0.06 (-8.56%)</td><td>0.05 (+7.44%)</td><td>0.02 <b>(+93.74%)</b></td><td>191.10 (-6.92%)</td><td>159.72 (-4.14%)</td><td>182.80 (+9.33%)</td><td>110.90 (-17.73%)</td><td>38.25 <b>(+50.78%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>166.62 (n/a)</td><td>167.20 (n/a)</td><td>134.80 (n/a)</td><td>25.37 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.08 (-6.64%)</td><td>0.07 (+0.16%)</td><td>0.07 (+4.15%)</td><td>0.06 (+10.66%)</td><td>0.01 <b>(-46.09%)</b></td><td>169.00 (-9.63%)</td><td>155.44 (-1.53%)</td><td>156.40 (-3.99%)</td><td>138.80 (+7.18%)</td><td>12.96 <b>(-46.82%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>187.00 (n/a)</td><td>157.86 (n/a)</td><td>162.90 (n/a)</td><td>129.50 (n/a)</td><td>24.38 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (-9.52%)</td><td>0.06 (-3.79%)</td><td>0.06 (+1.33%)</td><td>0.05 (+0.70%)</td><td>0.01 <b>(-41.69%)</b></td><td>220.60 (-0.72%)</td><td>184.96 (+1.81%)</td><td>185.80 (-1.33%)</td><td>157.50 (+10.53%)</td><td>23.90 <b>(-34.36%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>222.20 (n/a)</td><td>181.68 (n/a)</td><td>188.30 (n/a)</td><td>142.50 (n/a)</td><td>36.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (-15.48%)</td><td>0.05 <b>(-23.89%)</b></td><td>0.05 <b>(-29.47%)</b></td><td>0.04 (-12.25%)</td><td>0.01 <b>(-28.10%)</b></td><td>253.30 (+13.95%)</td><td>197.78 <b>(+29.44%)</b></td><td>191.10 <b>(+41.77%)</b></td><td>145.50 (+18.29%)</td><td>39.47 (-4.32%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>222.30 (n/a)</td><td>152.80 (n/a)</td><td>134.80 (n/a)</td><td>123.00 (n/a)</td><td>41.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 <b>(-26.26%)</b></td><td>0.05 (-16.88%)</td><td>0.05 (-17.68%)</td><td>0.04 (-7.08%)</td><td>0.00 <b>(-56.16%)</b></td><td>257.70 (+7.60%)</td><td>227.90 (+17.64%)</td><td>231.20 <b>(+21.49%)</b></td><td>203.00 <b>(+35.60%)</b></td><td>23.65 <b>(-37.48%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>239.50 (n/a)</td><td>193.72 (n/a)</td><td>190.30 (n/a)</td><td>149.70 (n/a)</td><td>37.82 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (+1.91%)</td><td>0.11 (-3.26%)</td><td>0.11 (-1.61%)</td><td>0.06 <b>(-37.62%)</b></td><td>0.03 <b>(+71.93%)</b></td><td>355.90 <b>(+60.32%)</b></td><td>209.40 (+10.95%)</td><td>182.60 (+1.61%)</td><td>149.80 (-1.90%)</td><td>83.05 <b>(+186.52%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>222.00 (n/a)</td><td>188.74 (n/a)</td><td>179.70 (n/a)</td><td>152.70 (n/a)</td><td>28.99 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (+12.18%)</td><td>0.11 (-6.51%)</td><td>0.10 (-19.50%)</td><td>0.09 (-14.03%)</td><td>0.02 <b>(+69.72%)</b></td><td>238.20 (+16.37%)</td><td>196.12 (+9.41%)</td><td>211.40 <b>(+24.21%)</b></td><td>138.40 (-10.88%)</td><td>38.15 <b>(+68.21%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>204.70 (n/a)</td><td>179.26 (n/a)</td><td>170.20 (n/a)</td><td>155.30 (n/a)</td><td>22.68 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 (+3.12%)</td><td>0.13 (+7.55%)</td><td>0.12 (+0.24%)</td><td>0.10 (+6.99%)</td><td>0.02 (-3.77%)</td><td>204.10 (-6.55%)</td><td>169.28 (-7.58%)</td><td>177.50 (-0.22%)</td><td>132.00 (-3.01%)</td><td>29.56 (-16.43%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>218.40 (n/a)</td><td>183.16 (n/a)</td><td>177.90 (n/a)</td><td>136.10 (n/a)</td><td>35.37 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 <b>(+21.59%)</b></td><td>0.13 (+5.83%)</td><td>0.12 (+0.74%)</td><td>0.11 (-0.55%)</td><td>0.03 <b>(+84.62%)</b></td><td>197.90 (+0.56%)</td><td>168.60 (-2.64%)</td><td>176.70 (-0.73%)</td><td>111.20 (-17.69%)</td><td>35.93 <b>(+57.63%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>196.80 (n/a)</td><td>173.18 (n/a)</td><td>178.00 (n/a)</td><td>135.10 (n/a)</td><td>22.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (-0.37%)</td><td>0.12 (-1.11%)</td><td>0.12 (-4.29%)</td><td>0.11 (+8.10%)</td><td>0.01 <b>(-23.96%)</b></td><td>186.10 (-7.50%)</td><td>171.66 (+0.56%)</td><td>174.40 (+4.43%)</td><td>150.30 (+0.33%)</td><td>15.10 <b>(-28.56%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>170.70 (n/a)</td><td>167.00 (n/a)</td><td>149.80 (n/a)</td><td>21.14 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (-9.23%)</td><td>0.12 (+1.64%)</td><td>0.11 (-1.65%)</td><td>0.11 (+11.58%)</td><td>0.01 <b>(-47.42%)</b></td><td>194.30 (-10.42%)</td><td>179.58 (-3.21%)</td><td>185.30 (+1.70%)</td><td>155.10 (+10.16%)</td><td>15.26 <b>(-48.15%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>216.90 (n/a)</td><td>185.54 (n/a)</td><td>182.20 (n/a)</td><td>140.80 (n/a)</td><td>29.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 <b>(-35.58%)</b></td><td>0.10 <b>(-20.93%)</b></td><td>0.09 (-12.30%)</td><td>0.09 (-8.85%)</td><td>0.01 <b>(-72.37%)</b></td><td>240.00 (+9.69%)</td><td>217.84 <b>(+20.82%)</b></td><td>227.50 (+14.04%)</td><td>195.90 <b>(+55.23%)</b></td><td>19.85 <b>(-54.40%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>218.80 (n/a)</td><td>180.30 (n/a)</td><td>199.50 (n/a)</td><td>126.20 (n/a)</td><td>43.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 (-3.83%)</td><td>0.09 (-4.97%)</td><td>0.09 (-0.07%)</td><td>0.06 <b>(-28.21%)</b></td><td>0.02 <b>(+111.39%)</b></td><td>344.30 <b>(+39.28%)</b></td><td>241.60 (+8.50%)</td><td>221.10 (+0.09%)</td><td>207.00 (+3.97%)</td><td>58.00 <b>(+213.06%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>247.20 (n/a)</td><td>222.68 (n/a)</td><td>220.90 (n/a)</td><td>199.10 (n/a)</td><td>18.53 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>287.50 (n/a)</td><td>175.48 (n/a)</td><td>148.20 (n/a)</td><td>108.70 (n/a)</td><td>68.30 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>187.30 (n/a)</td><td>160.92 (n/a)</td><td>166.10 (n/a)</td><td>135.30 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.20 (n/a)</td><td>162.42 (n/a)</td><td>151.50 (n/a)</td><td>143.20 (n/a)</td><td>22.56 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>233.40 (n/a)</td><td>190.84 (n/a)</td><td>192.50 (n/a)</td><td>155.50 (n/a)</td><td>28.27 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.30 (n/a)</td><td>180.80 (n/a)</td><td>191.50 (n/a)</td><td>142.00 (n/a)</td><td>36.68 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>243.70 (n/a)</td><td>179.26 (n/a)</td><td>170.70 (n/a)</td><td>127.00 (n/a)</td><td>42.97 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>311.30 (n/a)</td><td>199.86 (n/a)</td><td>176.80 (n/a)</td><td>141.60 (n/a)</td><td>65.50 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>202.30 (n/a)</td><td>177.78 (n/a)</td><td>173.60 (n/a)</td><td>152.00 (n/a)</td><td>20.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>165.10 (n/a)</td><td>159.44 (n/a)</td><td>162.10 (n/a)</td><td>152.40 (n/a)</td><td>6.21 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>199.50 (n/a)</td><td>166.06 (n/a)</td><td>160.20 (n/a)</td><td>137.10 (n/a)</td><td>24.12 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>211.70 (n/a)</td><td>169.90 (n/a)</td><td>173.40 (n/a)</td><td>137.00 (n/a)</td><td>30.39 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>265.20 (n/a)</td><td>215.28 (n/a)</td><td>205.70 (n/a)</td><td>192.40 (n/a)</td><td>29.96 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.38 (+0.59%)</td><td>0.29 (-10.50%)</td><td>0.30 (-10.85%)</td><td>0.22 <b>(-24.23%)</b></td><td>0.06 <b>(+46.29%)</b></td><td>226.40 <b>(+32.01%)</b></td><td>172.46 (+14.14%)</td><td>161.20 (+12.10%)</td><td>130.10 (-0.61%)</td><td>36.27 <b>(+89.18%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.04 (n/a)</td><td>171.50 (n/a)</td><td>151.10 (n/a)</td><td>143.80 (n/a)</td><td>130.90 (n/a)</td><td>19.17 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.39 (n/a)</td><td>0.27 (n/a)</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.08 (n/a)</td><td>282.90 (n/a)</td><td>191.36 (n/a)</td><td>179.50 (n/a)</td><td>126.50 (n/a)</td><td>56.74 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>192.00 (n/a)</td><td>156.52 (n/a)</td><td>151.80 (n/a)</td><td>128.20 (n/a)</td><td>26.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.33 (n/a)</td><td>0.30 (n/a)</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>197.20 (n/a)</td><td>164.90 (n/a)</td><td>159.10 (n/a)</td><td>149.40 (n/a)</td><td>18.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>168.90 (n/a)</td><td>146.86 (n/a)</td><td>137.30 (n/a)</td><td>132.10 (n/a)</td><td>17.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>223.80 (n/a)</td><td>164.62 (n/a)</td><td>147.40 (n/a)</td><td>144.40 (n/a)</td><td>33.63 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>198.60 (n/a)</td><td>167.04 (n/a)</td><td>164.60 (n/a)</td><td>128.40 (n/a)</td><td>26.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>190.40 (n/a)</td><td>155.96 (n/a)</td><td>162.00 (n/a)</td><td>108.60 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>189.40 (n/a)</td><td>162.02 (n/a)</td><td>160.10 (n/a)</td><td>131.20 (n/a)</td><td>22.87 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>217.90 (n/a)</td><td>154.82 (n/a)</td><td>142.10 (n/a)</td><td>124.50 (n/a)</td><td>37.95 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>223.00 (n/a)</td><td>178.02 (n/a)</td><td>185.20 (n/a)</td><td>126.80 (n/a)</td><td>45.47 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>210.50 (n/a)</td><td>178.42 (n/a)</td><td>178.70 (n/a)</td><td>157.20 (n/a)</td><td>20.90 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>152.90 (n/a)</td><td>132.48 (n/a)</td><td>131.50 (n/a)</td><td>112.20 (n/a)</td><td>18.31 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>191.60 (n/a)</td><td>164.50 (n/a)</td><td>158.00 (n/a)</td><td>149.40 (n/a)</td><td>16.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>244.60 (n/a)</td><td>161.90 (n/a)</td><td>143.00 (n/a)</td><td>124.40 (n/a)</td><td>48.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>201.90 (n/a)</td><td>169.76 (n/a)</td><td>162.50 (n/a)</td><td>156.10 (n/a)</td><td>18.50 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>198.10 (n/a)</td><td>165.16 (n/a)</td><td>169.00 (n/a)</td><td>125.80 (n/a)</td><td>29.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.05 (n/a)</td><td>187.90 (n/a)</td><td>157.02 (n/a)</td><td>154.80 (n/a)</td><td>128.10 (n/a)</td><td>22.30 (n/a)</td>
</tr>
</tbody>
</table>


### test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.33 (n/a)</td><td>0.29 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.04 (n/a)</td><td>208.00 (n/a)</td><td>174.08 (n/a)</td><td>161.60 (n/a)</td><td>149.00 (n/a)</td><td>27.47 (n/a)</td>
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


### test_gemm[M_1024-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>13.88 (-5.39%)</td><td>13.08 (-6.70%)</td><td>13.01 (-7.35%)</td><td>12.73 (-0.52%)</td><td>0.47 <b>(-38.55%)</b></td><td>4375.60 (+0.52%)</td><td>4262.04 (+7.03%)</td><td>4282.20 (+7.93%)</td><td>4013.70 (+5.70%)</td><td>147.38 <b>(-34.86%)</b></td><td>13375.96 (-5.39%)</td><td>12609.11 (-6.70%)</td><td>12537.33 (-7.35%)</td><td>12269.77 (-0.52%)</td><td>451.61 <b>(-38.55%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>14.67 (n/a)</td><td>14.02 (n/a)</td><td>14.04 (n/a)</td><td>12.80 (n/a)</td><td>0.76 (n/a)</td><td>4352.90 (n/a)</td><td>3982.22 (n/a)</td><td>3967.40 (n/a)</td><td>3797.30 (n/a)</td><td>226.25 (n/a)</td><td>14138.10 (n/a)</td><td>13515.06 (n/a)</td><td>13531.90 (n/a)</td><td>12333.66 (n/a)</td><td>734.91 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_1024-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>19.53 (+4.23%)</td><td>17.45 (+12.65%)</td><td>17.71 (+10.45%)</td><td>14.20 (+13.64%)</td><td>2.22 (-10.32%)</td><td>923.10 (-12.00%)</td><td>761.58 (-11.84%)</td><td>740.00 (-9.46%)</td><td>671.20 (-4.06%)</td><td>103.86 <b>(-25.73%)</b></td><td>12798.33 (+4.23%)</td><td>11436.87 (+12.65%)</td><td>11608.38 (+10.45%)</td><td>9305.08 (+13.64%)</td><td>1452.06 (-10.32%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>18.74 (n/a)</td><td>15.49 (n/a)</td><td>16.04 (n/a)</td><td>12.49 (n/a)</td><td>2.47 (n/a)</td><td>1049.00 (n/a)</td><td>863.84 (n/a)</td><td>817.30 (n/a)</td><td>699.60 (n/a)</td><td>139.84 (n/a)</td><td>12279.21 (n/a)</td><td>10152.26 (n/a)</td><td>10509.94 (n/a)</td><td>8188.41 (n/a)</td><td>1619.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_1024-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>15.32 (+8.27%)</td><td>14.09 (+3.05%)</td><td>14.12 (+1.74%)</td><td>12.98 (+0.93%)</td><td>0.84 <b>(+52.72%)</b></td><td>4292.80 (-0.93%)</td><td>3963.70 (-2.82%)</td><td>3944.30 (-1.71%)</td><td>3636.40 (-7.64%)</td><td>234.13 <b>(+39.80%)</b></td><td>14763.92 (+8.27%)</td><td>13582.66 (+3.05%)</td><td>13611.25 (+1.74%)</td><td>12506.20 (+0.93%)</td><td>806.57 <b>(+52.72%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>14.15 (n/a)</td><td>13.68 (n/a)</td><td>13.88 (n/a)</td><td>12.86 (n/a)</td><td>0.55 (n/a)</td><td>4332.90 (n/a)</td><td>4078.64 (n/a)</td><td>4013.00 (n/a)</td><td>3937.00 (n/a)</td><td>167.48 (n/a)</td><td>13636.61 (n/a)</td><td>13180.33 (n/a)</td><td>13378.38 (n/a)</td><td>12390.65 (n/a)</td><td>528.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>19.72 (+4.14%)</td><td>17.65 (+8.76%)</td><td>18.64 (+12.32%)</td><td>14.45 <b>(+22.58%)</b></td><td>2.18 (-18.38%)</td><td>1235.50 (-18.42%)</td><td>1025.10 (-9.23%)</td><td>958.20 (-10.96%)</td><td>905.70 (-3.98%)</td><td>136.80 <b>(-38.55%)</b></td><td>14818.88 (+4.14%)</td><td>13267.55 (+8.76%)</td><td>14007.85 (+12.32%)</td><td>10863.18 <b>(+22.58%)</b></td><td>1638.74 (-18.38%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>18.93 (n/a)</td><td>16.23 (n/a)</td><td>16.59 (n/a)</td><td>11.79 (n/a)</td><td>2.67 (n/a)</td><td>1514.50 (n/a)</td><td>1129.38 (n/a)</td><td>1076.20 (n/a)</td><td>943.20 (n/a)</td><td>222.62 (n/a)</td><td>14229.36 (n/a)</td><td>12198.38 (n/a)</td><td>12471.60 (n/a)</td><td>8862.23 (n/a)</td><td>2007.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>10.88 (-0.87%)</td><td>10.56 (-0.53%)</td><td>10.45 (-2.74%)</td><td>10.43 (+4.55%)</td><td>0.19 <b>(-53.67%)</b></td><td>7851.90 (-4.35%)</td><td>7758.22 (+0.43%)</td><td>7842.90 (+2.81%)</td><td>7527.10 (+0.88%)</td><td>139.97 <b>(-55.17%)</b></td><td>14264.96 (-0.87%)</td><td>13843.69 (-0.53%)</td><td>13690.61 (-2.74%)</td><td>13674.91 (+4.55%)</td><td>254.09 <b>(-53.67%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>10.98 (n/a)</td><td>10.62 (n/a)</td><td>10.74 (n/a)</td><td>9.98 (n/a)</td><td>0.42 (n/a)</td><td>8209.30 (n/a)</td><td>7724.88 (n/a)</td><td>7628.30 (n/a)</td><td>7461.60 (n/a)</td><td>312.26 (n/a)</td><td>14390.20 (n/a)</td><td>13917.49 (n/a)</td><td>14075.80 (n/a)</td><td>13079.53 (n/a)</td><td>548.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>21.72 (+8.78%)</td><td>17.49 (-4.81%)</td><td>17.94 (-0.66%)</td><td>13.25 <b>(-25.06%)</b></td><td>3.06 <b>(+237.40%)</b></td><td>1621.90 <b>(+33.43%)</b></td><td>1260.90 (+7.59%)</td><td>1198.40 (+0.66%)</td><td>989.80 (-8.07%)</td><td>231.98 <b>(+324.35%)</b></td><td>17356.72 (+8.78%)</td><td>13979.64 (-4.81%)</td><td>14335.34 (-0.66%)</td><td>10592.15 <b>(-25.06%)</b></td><td>2446.55 <b>(+237.40%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>19.96 (n/a)</td><td>18.37 (n/a)</td><td>18.06 (n/a)</td><td>17.68 (n/a)</td><td>0.91 (n/a)</td><td>1215.50 (n/a)</td><td>1172.00 (n/a)</td><td>1190.60 (n/a)</td><td>1076.70 (n/a)</td><td>54.67 (n/a)</td><td>15956.06 (n/a)</td><td>14685.55 (n/a)</td><td>14430.13 (n/a)</td><td>14133.85 (n/a)</td><td>725.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>12.45 (-0.48%)</td><td>12.43 (+1.18%)</td><td>12.43 (+0.27%)</td><td>12.42 (+5.94%)</td><td>0.01 <b>(-96.16%)</b></td><td>6595.80 (-5.61%)</td><td>6590.46 (-1.22%)</td><td>6591.50 (-0.26%)</td><td>6579.60 (+0.48%)</td><td>6.45 <b>(-96.39%)</b></td><td>16319.37 (-0.48%)</td><td>16292.42 (+1.18%)</td><td>16289.85 (+0.27%)</td><td>16279.14 (+5.94%)</td><td>16.00 <b>(-96.16%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>12.51 (n/a)</td><td>12.28 (n/a)</td><td>12.40 (n/a)</td><td>11.72 (n/a)</td><td>0.32 (n/a)</td><td>6987.50 (n/a)</td><td>6672.12 (n/a)</td><td>6609.00 (n/a)</td><td>6548.20 (n/a)</td><td>178.42 (n/a)</td><td>16397.62 (n/a)</td><td>16101.92 (n/a)</td><td>16246.72 (n/a)</td><td>15366.71 (n/a)</td><td>416.57 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>4.71 (-0.09%)</td><td>3.77 (+1.72%)</td><td>3.29 (-11.21%)</td><td>2.96 (-0.79%)</td><td>0.84 (+19.01%)</td><td>464.50 (+0.80%)</td><td>379.70 (-0.70%)</td><td>418.80 (+12.64%)</td><td>292.30 (+0.10%)</td><td>79.78 (+13.53%)</td><td>918.40 (-0.09%)</td><td>734.44 (+1.72%)</td><td>641.02 (-11.21%)</td><td>577.94 (-0.79%)</td><td>163.75 (+19.01%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>4.71 (n/a)</td><td>3.70 (n/a)</td><td>3.70 (n/a)</td><td>2.99 (n/a)</td><td>0.71 (n/a)</td><td>460.80 (n/a)</td><td>382.38 (n/a)</td><td>371.80 (n/a)</td><td>292.00 (n/a)</td><td>70.28 (n/a)</td><td>919.25 (n/a)</td><td>722.02 (n/a)</td><td>721.96 (n/a)</td><td>582.56 (n/a)</td><td>137.60 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.28 <b>(-22.56%)</b></td><td>4.13 (-0.92%)</td><td>3.91 (+10.73%)</td><td>3.60 (+4.05%)</td><td>0.69 <b>(-53.80%)</b></td><td>382.60 (-3.89%)</td><td>339.56 (-4.17%)</td><td>351.90 (-9.70%)</td><td>260.50 <b>(+29.15%)</b></td><td>49.12 <b>(-42.50%)</b></td><td>1030.40 <b>(-22.56%)</b></td><td>805.89 (-0.92%)</td><td>762.75 (+10.73%)</td><td>701.61 (+4.05%)</td><td>133.62 <b>(-53.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.82 (n/a)</td><td>4.17 (n/a)</td><td>3.53 (n/a)</td><td>3.46 (n/a)</td><td>1.48 (n/a)</td><td>398.10 (n/a)</td><td>354.32 (n/a)</td><td>389.70 (n/a)</td><td>201.70 (n/a)</td><td>85.41 (n/a)</td><td>1330.64 (n/a)</td><td>813.37 (n/a)</td><td>688.84 (n/a)</td><td>674.30 (n/a)</td><td>289.25 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>9.17 <b>(+48.73%)</b></td><td>4.77 (+1.04%)</td><td>3.70 <b>(-29.53%)</b></td><td>3.60 (+5.71%)</td><td>2.46 <b>(+103.09%)</b></td><td>382.80 (-5.41%)</td><td>330.24 (+7.01%)</td><td>372.10 <b>(+41.91%)</b></td><td>150.00 <b>(-32.77%)</b></td><td>100.87 <b>(+20.76%)</b></td><td>1789.38 <b>(+48.73%)</b></td><td>930.20 (+1.04%)</td><td>721.49 <b>(-29.53%)</b></td><td>701.21 (+5.71%)</td><td>480.38 <b>(+103.10%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.17 (n/a)</td><td>4.72 (n/a)</td><td>5.25 (n/a)</td><td>3.40 (n/a)</td><td>1.21 (n/a)</td><td>404.70 (n/a)</td><td>308.62 (n/a)</td><td>262.20 (n/a)</td><td>223.10 (n/a)</td><td>83.53 (n/a)</td><td>1203.13 (n/a)</td><td>920.61 (n/a)</td><td>1023.86 (n/a)</td><td>663.36 (n/a)</td><td>236.53 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>7.36 <b>(+23.23%)</b></td><td>4.56 (+9.91%)</td><td>3.91 (+7.11%)</td><td>3.63 (+2.28%)</td><td>1.58 <b>(+52.80%)</b></td><td>378.60 (-2.25%)</td><td>323.42 (-6.26%)</td><td>352.00 (-6.63%)</td><td>186.90 (-18.84%)</td><td>77.41 (+18.47%)</td><td>1436.14 <b>(+23.23%)</b></td><td>888.57 (+9.91%)</td><td>762.58 (+7.11%)</td><td>708.95 (+2.28%)</td><td>307.25 <b>(+52.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>5.97 (n/a)</td><td>4.14 (n/a)</td><td>3.65 (n/a)</td><td>3.55 (n/a)</td><td>1.03 (n/a)</td><td>387.30 (n/a)</td><td>345.00 (n/a)</td><td>377.00 (n/a)</td><td>230.30 (n/a)</td><td>65.34 (n/a)</td><td>1165.40 (n/a)</td><td>808.45 (n/a)</td><td>711.96 (n/a)</td><td>693.17 (n/a)</td><td>201.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1024-epilogue_sigmoid-clamp_None-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>4.49 <b>(-31.29%)</b></td><td>3.84 (-11.01%)</td><td>3.72 (-6.25%)</td><td>3.23 (+0.39%)</td><td>0.54 <b>(-59.98%)</b></td><td>426.10 (-0.40%)</td><td>364.24 (+7.03%)</td><td>369.80 (+6.66%)</td><td>306.80 <b>(+45.54%)</b></td><td>50.29 <b>(-42.14%)</b></td><td>875.06 <b>(-31.29%)</b></td><td>748.42 (-11.01%)</td><td>725.81 (-6.25%)</td><td>629.92 (+0.39%)</td><td>104.36 <b>(-59.98%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.53 (n/a)</td><td>4.31 (n/a)</td><td>3.97 (n/a)</td><td>3.22 (n/a)</td><td>1.34 (n/a)</td><td>427.80 (n/a)</td><td>340.30 (n/a)</td><td>346.70 (n/a)</td><td>210.80 (n/a)</td><td>86.92 (n/a)</td><td>1273.47 (n/a)</td><td>840.98 (n/a)</td><td>774.19 (n/a)</td><td>627.50 (n/a)</td><td>260.77 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.86 (+6.89%)</td><td>3.72 (+1.87%)</td><td>3.31 (+3.47%)</td><td>3.05 (-0.21%)</td><td>1.20 (+16.47%)</td><td>451.70 (+0.20%)</td><td>393.26 (-0.59%)</td><td>416.20 (-3.34%)</td><td>234.80 (-6.45%)</td><td>90.54 (+8.94%)</td><td>1143.08 (+6.89%)</td><td>725.65 (+1.87%)</td><td>644.97 (+3.47%)</td><td>594.23 (-0.21%)</td><td>234.90 (+16.47%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>5.48 (n/a)</td><td>3.65 (n/a)</td><td>3.20 (n/a)</td><td>3.05 (n/a)</td><td>1.03 (n/a)</td><td>450.80 (n/a)</td><td>395.58 (n/a)</td><td>430.60 (n/a)</td><td>251.00 (n/a)</td><td>83.11 (n/a)</td><td>1069.39 (n/a)</td><td>712.33 (n/a)</td><td>623.33 (n/a)</td><td>595.48 (n/a)</td><td>201.68 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_floor]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>4.79 <b>(-33.01%)</b></td><td>3.51 <b>(-22.97%)</b></td><td>3.17 <b>(-23.02%)</b></td><td>3.17 (+0.29%)</td><td>0.71 <b>(-57.01%)</b></td><td>434.30 (-0.28%)</td><td>401.98 <b>(+21.41%)</b></td><td>433.60 <b>(+29.90%)</b></td><td>287.50 <b>(+49.27%)</b></td><td>64.25 <b>(-38.36%)</b></td><td>933.76 <b>(-33.01%)</b></td><td>685.56 <b>(-22.97%)</b></td><td>619.12 <b>(-23.02%)</b></td><td>618.11 (+0.29%)</td><td>139.00 <b>(-57.01%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>7.15 (n/a)</td><td>4.56 (n/a)</td><td>4.12 (n/a)</td><td>3.16 (n/a)</td><td>1.66 (n/a)</td><td>435.50 (n/a)</td><td>331.08 (n/a)</td><td>333.80 (n/a)</td><td>192.60 (n/a)</td><td>104.23 (n/a)</td><td>1393.85 (n/a)</td><td>890.03 (n/a)</td><td>804.24 (n/a)</td><td>616.33 (n/a)</td><td>323.32 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>2.51 <b>(+32.27%)</b></td><td>2.22 <b>(+35.06%)</b></td><td>2.23 <b>(+37.10%)</b></td><td>1.84 <b>(+41.53%)</b></td><td>0.27 (+13.02%)</td><td>217.90 <b>(-29.35%)</b></td><td>183.28 <b>(-26.37%)</b></td><td>180.40 <b>(-27.05%)</b></td><td>159.90 <b>(-24.40%)</b></td><td>23.35 <b>(-39.54%)</b></td><td>209.87 <b>(+32.27%)</b></td><td>185.39 <b>(+35.06%)</b></td><td>186.02 <b>(+37.10%)</b></td><td>154.01 <b>(+41.53%)</b></td><td>22.57 (+13.02%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.90 (n/a)</td><td>1.64 (n/a)</td><td>1.62 (n/a)</td><td>1.30 (n/a)</td><td>0.24 (n/a)</td><td>308.40 (n/a)</td><td>248.92 (n/a)</td><td>247.30 (n/a)</td><td>211.50 (n/a)</td><td>38.62 (n/a)</td><td>158.67 (n/a)</td><td>137.27 (n/a)</td><td>135.68 (n/a)</td><td>108.81 (n/a)</td><td>19.97 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>7.11 (+13.76%)</td><td>5.65 (+2.00%)</td><td>5.30 (-3.61%)</td><td>5.22 (+6.01%)</td><td>0.82 <b>(+46.06%)</b></td><td>370.10 (-5.68%)</td><td>347.10 (-1.38%)</td><td>365.00 (+3.75%)</td><td>272.10 (-12.08%)</td><td>42.01 (+19.38%)</td><td>1480.03 (+13.76%)</td><td>1176.49 (+2.00%)</td><td>1103.27 (-3.61%)</td><td>1087.83 (+6.01%)</td><td>169.87 <b>(+46.06%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.25 (n/a)</td><td>5.54 (n/a)</td><td>5.50 (n/a)</td><td>4.93 (n/a)</td><td>0.56 (n/a)</td><td>392.40 (n/a)</td><td>351.94 (n/a)</td><td>351.80 (n/a)</td><td>309.50 (n/a)</td><td>35.19 (n/a)</td><td>1301.07 (n/a)</td><td>1153.39 (n/a)</td><td>1144.62 (n/a)</td><td>1026.19 (n/a)</td><td>116.30 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>17.67 (+0.63%)</td><td>13.93 (-6.92%)</td><td>13.93 (-17.12%)</td><td>11.27 (-2.26%)</td><td>2.42 <b>(-22.50%)</b></td><td>488.60 (+2.32%)</td><td>404.28 (+5.79%)</td><td>395.10 <b>(+20.68%)</b></td><td>311.60 (-0.64%)</td><td>66.42 <b>(-22.78%)</b></td><td>6891.53 (+0.63%)</td><td>5434.72 (-6.92%)</td><td>5435.83 (-17.12%)</td><td>4395.28 (-2.26%)</td><td>944.03 <b>(-22.50%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>17.56 (n/a)</td><td>14.97 (n/a)</td><td>16.81 (n/a)</td><td>11.53 (n/a)</td><td>3.12 (n/a)</td><td>477.50 (n/a)</td><td>382.14 (n/a)</td><td>327.40 (n/a)</td><td>313.60 (n/a)</td><td>86.02 (n/a)</td><td>6848.59 (n/a)</td><td>5838.67 (n/a)</td><td>6558.34 (n/a)</td><td>4496.90 (n/a)</td><td>1218.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_512-K_1024-N_2048-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>11.36 (+4.17%)</td><td>8.84 (-0.98%)</td><td>8.27 (+2.73%)</td><td>7.83 (+4.90%)</td><td>1.45 (-17.08%)</td><td>703.40 (-4.66%)</td><td>634.28 (-0.11%)</td><td>666.00 (-2.66%)</td><td>484.50 (-3.98%)</td><td>88.50 <b>(-24.86%)</b></td><td>4432.74 (+4.17%)</td><td>3449.01 (-0.98%)</td><td>3224.37 (+2.73%)</td><td>3053.19 (+4.90%)</td><td>567.45 (-17.08%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>10.91 (n/a)</td><td>8.93 (n/a)</td><td>8.05 (n/a)</td><td>7.46 (n/a)</td><td>1.75 (n/a)</td><td>737.80 (n/a)</td><td>635.00 (n/a)</td><td>684.20 (n/a)</td><td>504.60 (n/a)</td><td>117.79 (n/a)</td><td>4255.39 (n/a)</td><td>3483.19 (n/a)</td><td>3138.81 (n/a)</td><td>2910.49 (n/a)</td><td>684.30 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>11.77 (-4.56%)</td><td>9.62 (-2.01%)</td><td>9.34 (-0.85%)</td><td>8.54 (-2.88%)</td><td>1.31 (-9.24%)</td><td>679.30 (+2.97%)</td><td>611.08 (+1.91%)</td><td>620.70 (+0.86%)</td><td>492.80 (+4.78%)</td><td>75.42 (-0.41%)</td><td>4902.37 (-4.56%)</td><td>4007.19 (-2.01%)</td><td>3892.06 (-0.85%)</td><td>3556.53 (-2.88%)</td><td>545.58 (-9.24%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>12.33 (n/a)</td><td>9.82 (n/a)</td><td>9.42 (n/a)</td><td>8.79 (n/a)</td><td>1.44 (n/a)</td><td>659.70 (n/a)</td><td>599.64 (n/a)</td><td>615.40 (n/a)</td><td>470.30 (n/a)</td><td>75.73 (n/a)</td><td>5136.81 (n/a)</td><td>4089.50 (n/a)</td><td>3925.57 (n/a)</td><td>3662.07 (n/a)</td><td>601.15 (n/a)</td>
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


### test_gemm_tile_options[tn64-ma16]

_No metrics available._


### test_gemm_tile_options[tn64-ma32-default]

_No metrics available._


### test_gemm_tile_options[tn64-ma64]

_No metrics available._


</details>


<details>
<summary>iron/operators/flm/mm_prebuilt</summary>


### test_mm_prebuilt[M_256-K_512-N_1024-epilogue_gelu-clamp_None]

_No metrics available._


### test_mm_prebuilt[M_256-K_512-N_1024-epilogue_none-clamp_None]

_No metrics available._


### test_mm_prebuilt[M_256-K_512-N_1024-epilogue_silu-clamp_None]

_No metrics available._


### test_mm_prebuilt[M_256-K_512-N_1280-epilogue_none-clamp_None]

_No metrics available._


### test_mm_prebuilt[M_256-K_512-N_640-epilogue_none-clamp_None]

_No metrics available._


### test_mm_prebuilt[M_512-K_1024-N_2048-epilogue_none-clamp_None]

_No metrics available._


### test_mm_prebuilt_epilogue_matches_accumulator[epilogue_gelu-clamp_None]

_No metrics available._


### test_mm_prebuilt_epilogue_matches_accumulator[epilogue_none-clamp_(-2.0, 2.0)]

_No metrics available._


### test_mm_prebuilt_epilogue_matches_accumulator[epilogue_sigmoid-clamp_None]

_No metrics available._


### test_mm_prebuilt_epilogue_matches_accumulator[epilogue_silu-clamp_None]

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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.50 (n/a)</td><td>154.70 (n/a)</td><td>149.20 (n/a)</td><td>131.80 (n/a)</td><td>23.20 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>303.10 (n/a)</td><td>181.60 (n/a)</td><td>160.10 (n/a)</td><td>132.00 (n/a)</td><td>69.93 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.90 (n/a)</td><td>167.22 (n/a)</td><td>179.10 (n/a)</td><td>104.40 (n/a)</td><td>51.45 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.30 (n/a)</td><td>192.22 (n/a)</td><td>203.20 (n/a)</td><td>147.90 (n/a)</td><td>31.94 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>170.34 (n/a)</td><td>176.50 (n/a)</td><td>121.20 (n/a)</td><td>41.04 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>286.10 (n/a)</td><td>193.46 (n/a)</td><td>183.70 (n/a)</td><td>116.90 (n/a)</td><td>61.41 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>253.70 (n/a)</td><td>210.84 (n/a)</td><td>201.30 (n/a)</td><td>186.60 (n/a)</td><td>26.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>387.10 (n/a)</td><td>264.68 (n/a)</td><td>225.00 (n/a)</td><td>188.30 (n/a)</td><td>87.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>236.60 (n/a)</td><td>165.44 (n/a)</td><td>159.90 (n/a)</td><td>128.10 (n/a)</td><td>44.03 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>173.98 (n/a)</td><td>187.60 (n/a)</td><td>111.70 (n/a)</td><td>37.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.70 (n/a)</td><td>175.30 (n/a)</td><td>164.20 (n/a)</td><td>154.00 (n/a)</td><td>23.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>170.80 (n/a)</td><td>144.52 (n/a)</td><td>143.20 (n/a)</td><td>110.00 (n/a)</td><td>26.36 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.50 (n/a)</td><td>197.44 (n/a)</td><td>193.00 (n/a)</td><td>168.20 (n/a)</td><td>26.02 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>283.80 (n/a)</td><td>198.18 (n/a)</td><td>179.40 (n/a)</td><td>125.60 (n/a)</td><td>61.23 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>307.00 (n/a)</td><td>193.98 (n/a)</td><td>174.40 (n/a)</td><td>134.40 (n/a)</td><td>68.09 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.10 (n/a)</td><td>197.62 (n/a)</td><td>208.30 (n/a)</td><td>149.10 (n/a)</td><td>33.48 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>234.30 (n/a)</td><td>173.60 (n/a)</td><td>160.20 (n/a)</td><td>144.70 (n/a)</td><td>35.53 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.00 (n/a)</td><td>158.80 (n/a)</td><td>159.50 (n/a)</td><td>123.10 (n/a)</td><td>33.47 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>188.40 (n/a)</td><td>169.62 (n/a)</td><td>168.60 (n/a)</td><td>155.40 (n/a)</td><td>14.28 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>176.80 (n/a)</td><td>160.40 (n/a)</td><td>170.90 (n/a)</td><td>118.10 (n/a)</td><td>24.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>200.40 (n/a)</td><td>168.56 (n/a)</td><td>165.80 (n/a)</td><td>130.10 (n/a)</td><td>26.11 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>189.80 (n/a)</td><td>186.50 (n/a)</td><td>173.50 (n/a)</td><td>16.15 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.80 (n/a)</td><td>174.90 (n/a)</td><td>174.30 (n/a)</td><td>126.40 (n/a)</td><td>33.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>328.90 (n/a)</td><td>247.98 (n/a)</td><td>232.50 (n/a)</td><td>215.40 (n/a)</td><td>45.94 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>408.00 (n/a)</td><td>213.42 (n/a)</td><td>171.00 (n/a)</td><td>146.40 (n/a)</td><td>109.36 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>204.50 (n/a)</td><td>169.58 (n/a)</td><td>180.90 (n/a)</td><td>122.30 (n/a)</td><td>31.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>181.00 (n/a)</td><td>155.54 (n/a)</td><td>154.10 (n/a)</td><td>125.50 (n/a)</td><td>24.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.23 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>351.70 (n/a)</td><td>193.54 (n/a)</td><td>140.80 (n/a)</td><td>133.80 (n/a)</td><td>93.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>204.40 (n/a)</td><td>168.12 (n/a)</td><td>180.00 (n/a)</td><td>125.00 (n/a)</td><td>35.31 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>188.80 (n/a)</td><td>156.54 (n/a)</td><td>153.80 (n/a)</td><td>114.00 (n/a)</td><td>28.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>306.00 (n/a)</td><td>197.92 (n/a)</td><td>185.80 (n/a)</td><td>132.50 (n/a)</td><td>69.74 (n/a)</td>
</tr>
</tbody>
</table>


### test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>223.30 (n/a)</td><td>203.88 (n/a)</td><td>205.20 (n/a)</td><td>171.20 (n/a)</td><td>20.36 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/gemm</summary>


### test_gemm[M_1024-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>4.12 (-0.03%)</td><td>4.11 (+0.40%)</td><td>4.11 (+0.73%)</td><td>4.09 (+0.46%)</td><td>0.01 <b>(-55.78%)</b></td><td>19217.40 (-0.46%)</td><td>19137.12 (-0.40%)</td><td>19117.60 (-0.72%)</td><td>19101.60 (+0.03%)</td><td>46.47 <b>(-55.94%)</b></td><td>2810.60 (-0.03%)</td><td>2805.40 (+0.40%)</td><td>2808.25 (+0.73%)</td><td>2793.67 (+0.46%)</td><td>6.79 <b>(-55.78%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>4.12 (n/a)</td><td>4.09 (n/a)</td><td>4.08 (n/a)</td><td>4.07 (n/a)</td><td>0.02 (n/a)</td><td>19306.30 (n/a)</td><td>19213.72 (n/a)</td><td>19256.30 (n/a)</td><td>19096.20 (n/a)</td><td>105.49 (n/a)</td><td>2811.40 (n/a)</td><td>2794.27 (n/a)</td><td>2788.03 (n/a)</td><td>2780.80 (n/a)</td><td>15.37 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>4.25 (+0.86%)</td><td>4.14 (+1.20%)</td><td>4.18 (+2.47%)</td><td>3.95 (-1.03%)</td><td>0.12 <b>(+47.31%)</b></td><td>2378.10 (+1.04%)</td><td>2275.52 (-1.15%)</td><td>2251.30 (-2.41%)</td><td>2214.10 (-0.85%)</td><td>66.16 <b>(+48.06%)</b></td><td>1670.84 (+0.86%)</td><td>1626.81 (+1.20%)</td><td>1643.18 (+2.47%)</td><td>1555.60 (-1.03%)</td><td>46.43 <b>(+47.31%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>4.21 (n/a)</td><td>4.09 (n/a)</td><td>4.08 (n/a)</td><td>4.00 (n/a)</td><td>0.08 (n/a)</td><td>2353.60 (n/a)</td><td>2302.00 (n/a)</td><td>2307.00 (n/a)</td><td>2233.00 (n/a)</td><td>44.69 (n/a)</td><td>1656.65 (n/a)</td><td>1607.52 (n/a)</td><td>1603.54 (n/a)</td><td>1571.79 (n/a)</td><td>31.52 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.11 (+7.78%)</td><td>0.99 (+6.48%)</td><td>1.02 (+4.15%)</td><td>0.85 <b>(+21.60%)</b></td><td>0.12 (-5.44%)</td><td>259.70 (-17.79%)</td><td>226.42 (-6.70%)</td><td>216.00 (-4.00%)</td><td>198.60 (-7.24%)</td><td>29.32 <b>(-29.37%)</b></td><td>47.51 (+7.78%)</td><td>42.22 (+6.48%)</td><td>43.68 (+4.15%)</td><td>36.33 <b>(+21.60%)</b></td><td>5.31 (-5.44%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.03 (n/a)</td><td>0.93 (n/a)</td><td>0.98 (n/a)</td><td>0.70 (n/a)</td><td>0.13 (n/a)</td><td>315.90 (n/a)</td><td>242.68 (n/a)</td><td>225.00 (n/a)</td><td>214.10 (n/a)</td><td>41.51 (n/a)</td><td>44.08 (n/a)</td><td>39.66 (n/a)</td><td>41.94 (n/a)</td><td>29.88 (n/a)</td><td>5.62 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.12 (-3.55%)</td><td>0.93 (-3.92%)</td><td>0.93 (-2.18%)</td><td>0.72 (+4.78%)</td><td>0.15 <b>(-23.69%)</b></td><td>305.40 (-4.56%)</td><td>242.18 (+2.55%)</td><td>236.70 (+2.20%)</td><td>197.10 (+3.68%)</td><td>41.36 <b>(-22.25%)</b></td><td>47.87 (-3.55%)</td><td>39.83 (-3.92%)</td><td>39.87 (-2.18%)</td><td>30.90 (+4.78%)</td><td>6.43 <b>(-23.69%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.16 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.69 (n/a)</td><td>0.20 (n/a)</td><td>320.00 (n/a)</td><td>236.16 (n/a)</td><td>231.60 (n/a)</td><td>190.10 (n/a)</td><td>53.20 (n/a)</td><td>49.63 (n/a)</td><td>41.46 (n/a)</td><td>40.75 (n/a)</td><td>29.49 (n/a)</td><td>8.42 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.53 (-0.10%)</td><td>0.53 (-0.07%)</td><td>0.53 (-0.05%)</td><td>0.53 (-0.12%)</td><td>0.00 (+13.15%)</td><td>47886.40 (+0.12%)</td><td>47822.90 (+0.07%)</td><td>47807.80 (+0.05%)</td><td>47785.20 (+0.10%)</td><td>39.36 (+13.30%)</td><td>359.52 (-0.10%)</td><td>359.24 (-0.07%)</td><td>359.35 (-0.05%)</td><td>358.76 (-0.12%)</td><td>0.30 (+13.15%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47830.40 (n/a)</td><td>47790.88 (n/a)</td><td>47786.20 (n/a)</td><td>47738.60 (n/a)</td><td>34.74 (n/a)</td><td>359.87 (n/a)</td><td>359.48 (n/a)</td><td>359.51 (n/a)</td><td>359.18 (n/a)</td><td>0.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.21 (+1.10%)</td><td>0.21 (+0.62%)</td><td>0.21 (+0.96%)</td><td>0.21 (-0.12%)</td><td>0.00 <b>(+129.68%)</b></td><td>120532.20 (+0.12%)</td><td>119139.60 (-0.61%)</td><td>118855.20 (-0.95%)</td><td>117869.20 (-1.09%)</td><td>1052.06 <b>(+127.66%)</b></td><td>145.75 (+1.10%)</td><td>144.21 (+0.62%)</td><td>144.54 (+0.96%)</td><td>142.53 (-0.12%)</td><td>1.27 <b>(+129.68%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>120393.30 (n/a)</td><td>119876.60 (n/a)</td><td>119996.10 (n/a)</td><td>119169.30 (n/a)</td><td>462.11 (n/a)</td><td>144.16 (n/a)</td><td>143.31 (n/a)</td><td>143.17 (n/a)</td><td>142.70 (n/a)</td><td>0.55 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.91 (-0.41%)</td><td>0.90 (-0.33%)</td><td>0.90 (-0.06%)</td><td>0.89 (-1.36%)</td><td>0.01 <b>(+70.87%)</b></td><td>28305.80 (+1.38%)</td><td>27895.02 (+0.34%)</td><td>27874.90 (+0.06%)</td><td>27673.00 (+0.41%)</td><td>249.63 <b>(+74.21%)</b></td><td>620.82 (-0.41%)</td><td>615.92 (-0.33%)</td><td>616.32 (-0.06%)</td><td>606.94 (-1.36%)</td><td>5.47 <b>(+70.87%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.91 (n/a)</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>27919.60 (n/a)</td><td>27801.88 (n/a)</td><td>27858.00 (n/a)</td><td>27559.30 (n/a)</td><td>143.29 (n/a)</td><td>623.38 (n/a)</td><td>617.95 (n/a)</td><td>616.70 (n/a)</td><td>615.33 (n/a)</td><td>3.20 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>3.54 (-3.75%)</td><td>3.44 (-2.56%)</td><td>3.44 (-4.09%)</td><td>3.37 (-0.22%)</td><td>0.07 <b>(-49.99%)</b></td><td>7470.40 (+0.22%)</td><td>7308.22 (+2.54%)</td><td>7320.60 (+4.27%)</td><td>7109.90 (+3.89%)</td><td>139.55 <b>(-48.15%)</b></td><td>2416.33 (-3.75%)</td><td>2351.45 (-2.56%)</td><td>2346.77 (-4.09%)</td><td>2299.71 (-0.22%)</td><td>45.17 <b>(-49.99%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>3.68 (n/a)</td><td>3.54 (n/a)</td><td>3.58 (n/a)</td><td>3.38 (n/a)</td><td>0.13 (n/a)</td><td>7454.30 (n/a)</td><td>7126.86 (n/a)</td><td>7021.00 (n/a)</td><td>6843.50 (n/a)</td><td>269.12 (n/a)</td><td>2510.39 (n/a)</td><td>2413.31 (n/a)</td><td>2446.93 (n/a)</td><td>2304.70 (n/a)</td><td>90.31 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>3.07 (+5.01%)</td><td>2.85 (-0.59%)</td><td>2.85 (-0.48%)</td><td>2.72 (-2.60%)</td><td>0.14 <b>(+147.43%)</b></td><td>9260.60 (+2.67%)</td><td>8836.42 (+0.76%)</td><td>8844.50 (+0.48%)</td><td>8184.80 (-4.77%)</td><td>428.53 <b>(+142.71%)</b></td><td>2098.99 (+5.01%)</td><td>1947.98 (-0.59%)</td><td>1942.43 (-0.48%)</td><td>1855.16 (-2.60%)</td><td>97.11 <b>(+147.43%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>2.93 (n/a)</td><td>2.87 (n/a)</td><td>2.86 (n/a)</td><td>2.79 (n/a)</td><td>0.06 (n/a)</td><td>9020.00 (n/a)</td><td>8769.70 (n/a)</td><td>8802.10 (n/a)</td><td>8594.70 (n/a)</td><td>176.56 (n/a)</td><td>1998.88 (n/a)</td><td>1959.63 (n/a)</td><td>1951.78 (n/a)</td><td>1904.63 (n/a)</td><td>39.25 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>3.30 (-1.01%)</td><td>3.20 (-1.65%)</td><td>3.18 (-2.88%)</td><td>3.13 (+0.03%)</td><td>0.07 <b>(-25.91%)</b></td><td>8034.10 (-0.03%)</td><td>7874.08 (+1.65%)</td><td>7917.20 (+2.97%)</td><td>7620.90 (+1.02%)</td><td>157.92 <b>(-25.28%)</b></td><td>2254.30 (-1.01%)</td><td>2182.54 (-1.65%)</td><td>2169.95 (-2.88%)</td><td>2138.37 (+0.03%)</td><td>44.43 <b>(-25.91%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>3.34 (n/a)</td><td>3.25 (n/a)</td><td>3.27 (n/a)</td><td>3.13 (n/a)</td><td>0.09 (n/a)</td><td>8036.40 (n/a)</td><td>7746.42 (n/a)</td><td>7689.00 (n/a)</td><td>7543.70 (n/a)</td><td>211.34 (n/a)</td><td>2277.39 (n/a)</td><td>2219.09 (n/a)</td><td>2234.34 (n/a)</td><td>2137.74 (n/a)</td><td>59.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.80 (+0.01%)</td><td>0.80 (-0.05%)</td><td>0.80 (-0.11%)</td><td>0.80 (-0.02%)</td><td>0.00 <b>(+35.23%)</b></td><td>94896.00 (+0.02%)</td><td>94846.72 (+0.05%)</td><td>94882.90 (+0.11%)</td><td>94763.80 (-0.01%)</td><td>59.10 <b>(+35.21%)</b></td><td>725.17 (+0.01%)</td><td>724.53 (-0.05%)</td><td>724.26 (-0.11%)</td><td>724.16 (-0.02%)</td><td>0.45 <b>(+35.21%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94874.20 (n/a)</td><td>94802.46 (n/a)</td><td>94775.10 (n/a)</td><td>94773.40 (n/a)</td><td>43.71 (n/a)</td><td>725.09 (n/a)</td><td>724.87 (n/a)</td><td>725.08 (n/a)</td><td>724.32 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.73 (-0.01%)</td><td>0.73 (+0.05%)</td><td>0.73 (+0.00%)</td><td>0.73 (+0.26%)</td><td>0.00 <b>(-93.44%)</b></td><td>103308.60 (-0.26%)</td><td>103301.58 (-0.05%)</td><td>103303.80 (-0.00%)</td><td>103287.30 (+0.01%)</td><td>8.45 <b>(-93.43%)</b></td><td>665.32 (-0.01%)</td><td>665.23 (+0.05%)</td><td>665.22 (+0.00%)</td><td>665.19 (+0.26%)</td><td>0.05 <b>(-93.44%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103579.00 (n/a)</td><td>103351.08 (n/a)</td><td>103308.50 (n/a)</td><td>103276.20 (n/a)</td><td>128.55 (n/a)</td><td>665.40 (n/a)</td><td>664.91 (n/a)</td><td>665.19 (n/a)</td><td>663.45 (n/a)</td><td>0.83 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.69 (+0.27%)</td><td>0.69 (+0.35%)</td><td>0.69 (+0.40%)</td><td>0.68 (+0.46%)</td><td>0.00 <b>(-32.76%)</b></td><td>110361.70 (-0.45%)</td><td>110143.68 (-0.35%)</td><td>110140.70 (-0.40%)</td><td>109885.60 (-0.27%)</td><td>190.07 <b>(-33.23%)</b></td><td>625.37 (+0.27%)</td><td>623.91 (+0.35%)</td><td>623.92 (+0.40%)</td><td>622.67 (+0.46%)</td><td>1.08 <b>(-32.76%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110865.80 (n/a)</td><td>110530.80 (n/a)</td><td>110579.00 (n/a)</td><td>110185.40 (n/a)</td><td>284.65 (n/a)</td><td>623.67 (n/a)</td><td>621.73 (n/a)</td><td>621.45 (n/a)</td><td>619.84 (n/a)</td><td>1.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_gemm[M_2048-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-trace_size_0-partition_N_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th><th>Throughput (max)</th><th>Throughput (mean)</th><th>Throughput (median)</th><th>Throughput (min)</th><th>Throughput (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>2.80 (-0.69%)</td><td>2.79 (-0.36%)</td><td>2.79 (-0.10%)</td><td>2.77 (-0.77%)</td><td>0.01 <b>(+22.39%)</b></td><td>37893.70 (+0.77%)</td><td>37594.00 (+0.37%)</td><td>37518.10 (+0.10%)</td><td>37492.60 (+0.70%)</td><td>169.39 <b>(+24.33%)</b></td><td>2863.88 (-0.69%)</td><td>2856.20 (-0.36%)</td><td>2861.93 (-0.10%)</td><td>2833.56 (-0.77%)</td><td>12.80 <b>(+22.39%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>2.82 (n/a)</td><td>2.80 (n/a)</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>0.01 (n/a)</td><td>37602.70 (n/a)</td><td>37456.68 (n/a)</td><td>37479.70 (n/a)</td><td>37233.50 (n/a)</td><td>136.24 (n/a)</td><td>2883.80 (n/a)</td><td>2866.65 (n/a)</td><td>2864.86 (n/a)</td><td>2855.49 (n/a)</td><td>10.46 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>7.64 (-0.44%)</td><td>6.90 (-6.96%)</td><td>6.73 (-9.22%)</td><td>6.48 (-8.01%)</td><td>0.45 <b>(+84.75%)</b></td><td>1375.60 (+8.71%)</td><td>1294.94 (+7.73%)</td><td>1324.80 (+10.15%)</td><td>1166.80 (+0.45%)</td><td>79.56 <b>(+99.03%)</b></td><td>460.13 (-0.44%)</td><td>415.91 (-6.96%)</td><td>405.23 (-9.22%)</td><td>390.28 (-8.01%)</td><td>26.89 <b>(+84.76%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>7.67 (n/a)</td><td>7.42 (n/a)</td><td>7.41 (n/a)</td><td>7.04 (n/a)</td><td>0.24 (n/a)</td><td>1265.40 (n/a)</td><td>1201.98 (n/a)</td><td>1202.70 (n/a)</td><td>1161.60 (n/a)</td><td>39.97 (n/a)</td><td>462.17 (n/a)</td><td>447.05 (n/a)</td><td>446.40 (n/a)</td><td>424.28 (n/a)</td><td>14.56 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>6.91 (-1.91%)</td><td>6.47 (-0.32%)</td><td>6.79 (+2.64%)</td><td>5.31 (-3.28%)</td><td>0.67 (+7.83%)</td><td>1677.00 (+3.39%)</td><td>1391.62 (+0.50%)</td><td>1313.00 (-2.57%)</td><td>1289.30 (+1.95%)</td><td>163.18 (+13.88%)</td><td>416.39 (-1.91%)</td><td>389.54 (-0.32%)</td><td>408.88 (+2.64%)</td><td>320.13 (-3.28%)</td><td>40.15 (+7.83%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>7.05 (n/a)</td><td>6.49 (n/a)</td><td>6.61 (n/a)</td><td>5.49 (n/a)</td><td>0.62 (n/a)</td><td>1622.00 (n/a)</td><td>1384.66 (n/a)</td><td>1347.70 (n/a)</td><td>1264.70 (n/a)</td><td>143.29 (n/a)</td><td>424.52 (n/a)</td><td>390.81 (n/a)</td><td>398.36 (n/a)</td><td>330.99 (n/a)</td><td>37.24 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>7.07 (-2.02%)</td><td>6.50 (+0.68%)</td><td>6.35 (-6.81%)</td><td>6.14 <b>(+27.91%)</b></td><td>0.40 <b>(-59.79%)</b></td><td>1452.40 <b>(-21.82%)</b></td><td>1376.16 (-2.64%)</td><td>1402.90 (+7.31%)</td><td>1260.00 (+2.07%)</td><td>83.16 <b>(-68.00%)</b></td><td>426.07 (-2.02%)</td><td>391.30 (+0.68%)</td><td>382.69 (-6.81%)</td><td>369.65 <b>(+27.91%)</b></td><td>24.29 <b>(-59.79%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>7.22 (n/a)</td><td>6.45 (n/a)</td><td>6.82 (n/a)</td><td>4.80 (n/a)</td><td>1.00 (n/a)</td><td>1857.70 (n/a)</td><td>1413.48 (n/a)</td><td>1307.30 (n/a)</td><td>1234.50 (n/a)</td><td>259.89 (n/a)</td><td>434.87 (n/a)</td><td>388.66 (n/a)</td><td>410.68 (n/a)</td><td>289.00 (n/a)</td><td>60.41 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>8.10 (+0.37%)</td><td>7.73 (-0.30%)</td><td>7.80 (-1.47%)</td><td>7.32 (-1.16%)</td><td>0.36 (+11.96%)</td><td>4760.80 (+1.18%)</td><td>4516.76 (+0.33%)</td><td>4469.70 (+1.49%)</td><td>4306.30 (-0.37%)</td><td>209.64 (+12.16%)</td><td>498.68 (+0.37%)</td><td>476.26 (-0.30%)</td><td>480.46 (-1.47%)</td><td>451.07 (-1.16%)</td><td>21.94 (+11.96%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>8.07 (n/a)</td><td>7.76 (n/a)</td><td>7.92 (n/a)</td><td>7.41 (n/a)</td><td>0.32 (n/a)</td><td>4705.50 (n/a)</td><td>4501.74 (n/a)</td><td>4403.90 (n/a)</td><td>4322.10 (n/a)</td><td>186.91 (n/a)</td><td>496.87 (n/a)</td><td>477.69 (n/a)</td><td>487.63 (n/a)</td><td>456.38 (n/a)</td><td>19.60 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>7.61 (-4.10%)</td><td>7.47 (-2.33%)</td><td>7.59 (-0.50%)</td><td>7.02 (-5.97%)</td><td>0.25 <b>(+39.25%)</b></td><td>4967.20 (+6.34%)</td><td>4671.68 (+2.44%)</td><td>4592.30 (+0.50%)</td><td>4579.80 (+4.27%)</td><td>166.28 <b>(+55.20%)</b></td><td>468.90 (-4.10%)</td><td>460.12 (-2.33%)</td><td>467.62 (-0.50%)</td><td>432.33 (-5.97%)</td><td>15.65 <b>(+39.25%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>7.94 (n/a)</td><td>7.65 (n/a)</td><td>7.63 (n/a)</td><td>7.46 (n/a)</td><td>0.18 (n/a)</td><td>4670.90 (n/a)</td><td>4560.46 (n/a)</td><td>4569.40 (n/a)</td><td>4392.10 (n/a)</td><td>107.14 (n/a)</td><td>488.95 (n/a)</td><td>471.10 (n/a)</td><td>469.97 (n/a)</td><td>459.76 (n/a)</td><td>11.24 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>7.49 (-0.82%)</td><td>7.27 (-0.43%)</td><td>7.41 (+0.88%)</td><td>6.95 (+0.10%)</td><td>0.24 (-1.72%)</td><td>5014.10 (-0.10%)</td><td>4796.78 (+0.42%)</td><td>4704.60 (-0.87%)</td><td>4657.70 (+0.82%)</td><td>159.19 (-1.11%)</td><td>461.06 (-0.82%)</td><td>448.08 (-0.43%)</td><td>456.46 (+0.88%)</td><td>428.29 (+0.10%)</td><td>14.65 (-1.72%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>7.55 (n/a)</td><td>7.31 (n/a)</td><td>7.35 (n/a)</td><td>6.95 (n/a)</td><td>0.24 (n/a)</td><td>5019.20 (n/a)</td><td>4776.52 (n/a)</td><td>4745.90 (n/a)</td><td>4619.70 (n/a)</td><td>160.98 (n/a)</td><td>464.85 (n/a)</td><td>449.99 (n/a)</td><td>452.49 (n/a)</td><td>427.86 (n/a)</td><td>14.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.80 (-0.02%)</td><td>0.80 (+0.02%)</td><td>0.80 (-0.01%)</td><td>0.80 (+0.04%)</td><td>0.00 <b>(-28.17%)</b></td><td>94221.60 (-0.04%)</td><td>94104.32 (-0.02%)</td><td>94096.90 (+0.01%)</td><td>94046.20 (+0.02%)</td><td>70.91 <b>(-28.17%)</b></td><td>730.70 (-0.02%)</td><td>730.25 (+0.02%)</td><td>730.31 (-0.01%)</td><td>729.34 (+0.04%)</td><td>0.55 <b>(-28.16%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94259.90 (n/a)</td><td>94125.56 (n/a)</td><td>94083.80 (n/a)</td><td>94030.90 (n/a)</td><td>98.71 (n/a)</td><td>730.82 (n/a)</td><td>730.08 (n/a)</td><td>730.41 (n/a)</td><td>729.04 (n/a)</td><td>0.77 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.74 (+0.39%)</td><td>0.74 (+0.02%)</td><td>0.74 (-0.00%)</td><td>0.73 (-0.19%)</td><td>0.00 <b>(+1079.70%)</b></td><td>102813.10 (+0.19%)</td><td>102566.84 (-0.02%)</td><td>102587.50 (+0.00%)</td><td>102173.60 (-0.38%)</td><td>239.13 <b>(+1075.92%)</b></td><td>672.58 (+0.39%)</td><td>670.00 (+0.02%)</td><td>669.86 (-0.00%)</td><td>668.39 (-0.19%)</td><td>1.56 <b>(+1079.81%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102617.60 (n/a)</td><td>102589.52 (n/a)</td><td>102583.70 (n/a)</td><td>102567.30 (n/a)</td><td>20.34 (n/a)</td><td>669.99 (n/a)</td><td>669.85 (n/a)</td><td>669.89 (n/a)</td><td>669.67 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.71 (-0.08%)</td><td>0.71 (-0.08%)</td><td>0.71 (-0.09%)</td><td>0.71 (-0.06%)</td><td>0.00 (-8.71%)</td><td>106015.00 (+0.06%)</td><td>105977.22 (+0.08%)</td><td>105989.60 (+0.09%)</td><td>105896.00 (+0.08%)</td><td>49.03 (-8.57%)</td><td>648.93 (-0.08%)</td><td>648.44 (-0.08%)</td><td>648.36 (-0.09%)</td><td>648.21 (-0.06%)</td><td>0.30 (-8.72%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>105954.00 (n/a)</td><td>105893.64 (n/a)</td><td>105889.10 (n/a)</td><td>105811.50 (n/a)</td><td>53.62 (n/a)</td><td>649.45 (n/a)</td><td>648.95 (n/a)</td><td>648.98 (n/a)</td><td>648.58 (n/a)</td><td>0.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>4.32 (+8.03%)</td><td>3.77 (+11.88%)</td><td>3.70 (+15.87%)</td><td>3.27 (+7.64%)</td><td>0.39 (-4.37%)</td><td>2462.80 (-7.10%)</td><td>2157.44 (-10.83%)</td><td>2181.00 (-13.70%)</td><td>1867.80 (-7.44%)</td><td>220.52 (-18.51%)</td><td>1131.76 (+8.03%)</td><td>988.10 (+11.88%)</td><td>969.24 (+15.87%)</td><td>858.34 (+7.64%)</td><td>101.60 (-4.37%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>3.99 (n/a)</td><td>3.37 (n/a)</td><td>3.19 (n/a)</td><td>3.04 (n/a)</td><td>0.41 (n/a)</td><td>2651.00 (n/a)</td><td>2419.54 (n/a)</td><td>2527.20 (n/a)</td><td>2017.90 (n/a)</td><td>270.62 (n/a)</td><td>1047.59 (n/a)</td><td>883.18 (n/a)</td><td>836.46 (n/a)</td><td>797.41 (n/a)</td><td>106.25 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.53 <b>(+48.29%)</b></td><td>0.36 (+9.33%)</td><td>0.33 (+1.45%)</td><td>0.30 (-6.84%)</td><td>0.09 <b>(+544.70%)</b></td><td>4161.00 (+7.34%)</td><td>3587.54 (-4.75%)</td><td>3766.30 (-1.43%)</td><td>2355.50 <b>(-32.57%)</b></td><td>711.21 <b>(+349.22%)</b></td><td>28.49 <b>(+48.29%)</b></td><td>19.51 (+9.33%)</td><td>17.82 (+1.45%)</td><td>16.13 (-6.84%)</td><td>5.08 <b>(+544.70%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.01 (n/a)</td><td>3876.40 (n/a)</td><td>3766.56 (n/a)</td><td>3820.90 (n/a)</td><td>3493.10 (n/a)</td><td>158.32 (n/a)</td><td>19.21 (n/a)</td><td>17.84 (n/a)</td><td>17.56 (n/a)</td><td>17.31 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.55 (-11.78%)</td><td>4.67 (-3.97%)</td><td>4.68 (-3.30%)</td><td>3.51 (+1.57%)</td><td>0.74 <b>(-26.23%)</b></td><td>1897.20 (-1.55%)</td><td>1456.92 (+2.72%)</td><td>1421.10 (+3.42%)</td><td>1198.70 (+13.35%)</td><td>262.75 (-16.82%)</td><td>1714.56 (-11.78%)</td><td>1443.48 (-3.97%)</td><td>1446.24 (-3.30%)</td><td>1083.28 (+1.57%)</td><td>229.77 <b>(-26.23%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.29 (n/a)</td><td>4.86 (n/a)</td><td>4.84 (n/a)</td><td>3.45 (n/a)</td><td>1.01 (n/a)</td><td>1927.00 (n/a)</td><td>1418.40 (n/a)</td><td>1374.10 (n/a)</td><td>1057.50 (n/a)</td><td>315.86 (n/a)</td><td>1943.45 (n/a)</td><td>1503.10 (n/a)</td><td>1495.65 (n/a)</td><td>1066.54 (n/a)</td><td>311.45 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>13.65 (n/a)</td><td>12.86 (n/a)</td><td>13.24 (n/a)</td><td>10.68 (n/a)</td><td>1.23 (n/a)</td><td>13.64 (n/a)</td><td>12.85 (n/a)</td><td>13.23 (n/a)</td><td>10.68 (n/a)</td><td>1.23 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>24.60 (-3.05%)</td><td>23.75 (-1.96%)</td><td>23.47 (-2.29%)</td><td>23.07 (-0.87%)</td><td>0.69 (-13.71%)</td><td>24.58 (-3.05%)</td><td>23.74 (-1.96%)</td><td>23.45 (-2.29%)</td><td>23.05 (-0.87%)</td><td>0.68 (-13.71%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>25.37 (n/a)</td><td>24.23 (n/a)</td><td>24.02 (n/a)</td><td>23.27 (n/a)</td><td>0.79 (n/a)</td><td>25.35 (n/a)</td><td>24.21 (n/a)</td><td>24.00 (n/a)</td><td>23.25 (n/a)</td><td>0.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>41.84 (+0.80%)</td><td>39.94 (-0.54%)</td><td>40.60 (+1.71%)</td><td>35.41 (-10.27%)</td><td>2.59 <b>(+231.02%)</b></td><td>41.81 (+0.80%)</td><td>39.91 (-0.54%)</td><td>40.58 (+1.71%)</td><td>35.39 (-10.27%)</td><td>2.58 <b>(+231.02%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>41.50 (n/a)</td><td>40.15 (n/a)</td><td>39.92 (n/a)</td><td>39.46 (n/a)</td><td>0.78 (n/a)</td><td>41.48 (n/a)</td><td>40.13 (n/a)</td><td>39.89 (n/a)</td><td>39.44 (n/a)</td><td>0.78 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>43.04 (-4.95%)</td><td>40.35 (-6.28%)</td><td>40.33 (-5.02%)</td><td>37.29 (-10.62%)</td><td>2.20 <b>(+40.36%)</b></td><td>43.01 (-4.95%)</td><td>40.33 (-6.28%)</td><td>40.30 (-5.02%)</td><td>37.27 (-10.62%)</td><td>2.20 <b>(+40.36%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>45.28 (n/a)</td><td>43.06 (n/a)</td><td>42.46 (n/a)</td><td>41.72 (n/a)</td><td>1.57 (n/a)</td><td>45.25 (n/a)</td><td>43.03 (n/a)</td><td>42.43 (n/a)</td><td>41.70 (n/a)</td><td>1.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>13.47 (n/a)</td><td>12.57 (n/a)</td><td>12.81 (n/a)</td><td>11.10 (n/a)</td><td>0.91 (n/a)</td><td>13.46 (n/a)</td><td>12.56 (n/a)</td><td>12.80 (n/a)</td><td>11.09 (n/a)</td><td>0.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>24.96 (-0.85%)</td><td>24.31 (+4.69%)</td><td>24.24 (-0.52%)</td><td>23.54 <b>(+26.59%)</b></td><td>0.53 <b>(-80.15%)</b></td><td>24.95 (-0.85%)</td><td>24.30 (+4.69%)</td><td>24.23 (-0.52%)</td><td>23.53 <b>(+26.59%)</b></td><td>0.53 <b>(-80.15%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>25.18 (n/a)</td><td>23.22 (n/a)</td><td>24.37 (n/a)</td><td>18.60 (n/a)</td><td>2.66 (n/a)</td><td>25.16 (n/a)</td><td>23.21 (n/a)</td><td>24.35 (n/a)</td><td>18.59 (n/a)</td><td>2.66 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>41.09 (-0.99%)</td><td>38.38 (-3.72%)</td><td>38.43 (-3.64%)</td><td>36.10 (-6.07%)</td><td>1.83 <b>(+64.93%)</b></td><td>41.07 (-0.99%)</td><td>38.36 (-3.72%)</td><td>38.40 (-3.64%)</td><td>36.08 (-6.07%)</td><td>1.83 <b>(+64.93%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>41.50 (n/a)</td><td>39.86 (n/a)</td><td>39.88 (n/a)</td><td>38.44 (n/a)</td><td>1.11 (n/a)</td><td>41.48 (n/a)</td><td>39.84 (n/a)</td><td>39.85 (n/a)</td><td>38.41 (n/a)</td><td>1.11 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>45.39 (+1.18%)</td><td>43.55 (+4.06%)</td><td>44.42 (+3.50%)</td><td>41.32 (+18.00%)</td><td>1.90 <b>(-52.03%)</b></td><td>45.36 (+1.18%)</td><td>43.53 (+4.06%)</td><td>44.39 (+3.50%)</td><td>41.29 (+18.00%)</td><td>1.90 <b>(-52.03%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>44.86 (n/a)</td><td>41.85 (n/a)</td><td>42.92 (n/a)</td><td>35.01 (n/a)</td><td>3.96 (n/a)</td><td>44.83 (n/a)</td><td>41.83 (n/a)</td><td>42.89 (n/a)</td><td>34.99 (n/a)</td><td>3.96 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>9.67 (+4.82%)</td><td>8.96 (+5.71%)</td><td>8.95 (+4.30%)</td><td>8.13 (+4.93%)</td><td>0.55 (+2.91%)</td><td>9.65 (+4.82%)</td><td>8.95 (+5.71%)</td><td>8.93 (+4.30%)</td><td>8.12 (+4.93%)</td><td>0.55 (+2.91%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.22 (n/a)</td><td>8.48 (n/a)</td><td>8.58 (n/a)</td><td>7.75 (n/a)</td><td>0.54 (n/a)</td><td>9.21 (n/a)</td><td>8.46 (n/a)</td><td>8.56 (n/a)</td><td>7.74 (n/a)</td><td>0.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.03 (+12.81%)</td><td>0.92 (+9.55%)</td><td>0.93 (+7.47%)</td><td>0.77 (+3.02%)</td><td>0.09 <b>(+46.25%)</b></td><td>1.01 (+12.81%)</td><td>0.90 (+9.55%)</td><td>0.91 (+7.47%)</td><td>0.76 (+3.02%)</td><td>0.09 <b>(+46.25%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.91 (n/a)</td><td>0.84 (n/a)</td><td>0.86 (n/a)</td><td>0.75 (n/a)</td><td>0.06 (n/a)</td><td>0.90 (n/a)</td><td>0.82 (n/a)</td><td>0.85 (n/a)</td><td>0.74 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.32 <b>(+20.40%)</b></td><td>1.14 (+7.22%)</td><td>1.13 (+4.22%)</td><td>0.94 (-3.25%)</td><td>0.16 <b>(+228.07%)</b></td><td>1.30 <b>(+20.40%)</b></td><td>1.12 (+7.22%)</td><td>1.11 (+4.22%)</td><td>0.93 (-3.25%)</td><td>0.16 <b>(+228.07%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.10 (n/a)</td><td>1.06 (n/a)</td><td>1.08 (n/a)</td><td>0.97 (n/a)</td><td>0.05 (n/a)</td><td>1.08 (n/a)</td><td>1.05 (n/a)</td><td>1.07 (n/a)</td><td>0.96 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>18.89 (+6.42%)</td><td>17.34 (+8.53%)</td><td>18.01 (+9.49%)</td><td>15.10 (+9.78%)</td><td>1.74 (+8.43%)</td><td>18.67 (+6.42%)</td><td>17.14 (+8.53%)</td><td>17.80 (+9.49%)</td><td>14.93 (+9.78%)</td><td>1.72 (+8.43%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>17.75 (n/a)</td><td>15.98 (n/a)</td><td>16.45 (n/a)</td><td>13.76 (n/a)</td><td>1.60 (n/a)</td><td>17.55 (n/a)</td><td>15.80 (n/a)</td><td>16.26 (n/a)</td><td>13.60 (n/a)</td><td>1.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>14.14 (+1.68%)</td><td>13.22 (-0.34%)</td><td>13.31 (+0.23%)</td><td>12.10 (-3.52%)</td><td>0.74 <b>(+50.25%)</b></td><td>13.89 (+1.68%)</td><td>12.98 (-0.34%)</td><td>13.08 (+0.23%)</td><td>11.88 (-3.52%)</td><td>0.72 <b>(+50.25%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.90 (n/a)</td><td>13.26 (n/a)</td><td>13.28 (n/a)</td><td>12.54 (n/a)</td><td>0.49 (n/a)</td><td>13.66 (n/a)</td><td>13.03 (n/a)</td><td>13.05 (n/a)</td><td>12.32 (n/a)</td><td>0.48 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>10.40 <b>(+23.69%)</b></td><td>8.38 (+10.53%)</td><td>7.86 (+6.95%)</td><td>7.65 (+9.15%)</td><td>1.15 <b>(+111.31%)</b></td><td>10.22 <b>(+23.69%)</b></td><td>8.24 (+10.53%)</td><td>7.73 (+6.95%)</td><td>7.51 (+9.15%)</td><td>1.13 <b>(+111.31%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>8.41 (n/a)</td><td>7.58 (n/a)</td><td>7.35 (n/a)</td><td>7.00 (n/a)</td><td>0.54 (n/a)</td><td>8.26 (n/a)</td><td>7.45 (n/a)</td><td>7.23 (n/a)</td><td>6.88 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>6.07 (-4.80%)</td><td>5.68 (+4.21%)</td><td>5.90 (+6.99%)</td><td>5.09 <b>(+28.62%)</b></td><td>0.41 <b>(-55.53%)</b></td><td>5.97 (-4.80%)</td><td>5.59 (+4.21%)</td><td>5.80 (+6.99%)</td><td>5.01 <b>(+28.62%)</b></td><td>0.41 <b>(-55.53%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.38 (n/a)</td><td>5.45 (n/a)</td><td>5.51 (n/a)</td><td>3.96 (n/a)</td><td>0.93 (n/a)</td><td>6.27 (n/a)</td><td>5.37 (n/a)</td><td>5.42 (n/a)</td><td>3.89 (n/a)</td><td>0.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>13.51 (n/a)</td><td>12.70 (n/a)</td><td>13.08 (n/a)</td><td>11.79 (n/a)</td><td>0.81 (n/a)</td><td>13.50 (n/a)</td><td>12.70 (n/a)</td><td>13.07 (n/a)</td><td>11.79 (n/a)</td><td>0.81 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>13.20 (n/a)</td><td>12.72 (n/a)</td><td>12.66 (n/a)</td><td>12.16 (n/a)</td><td>0.42 (n/a)</td><td>13.19 (n/a)</td><td>12.71 (n/a)</td><td>12.65 (n/a)</td><td>12.15 (n/a)</td><td>0.42 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.30 (n/a)</td><td>173.68 (n/a)</td><td>164.40 (n/a)</td><td>135.70 (n/a)</td><td>34.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>302.30 (n/a)</td><td>182.08 (n/a)</td><td>182.90 (n/a)</td><td>98.90 (n/a)</td><td>76.73 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.20 (n/a)</td><td>175.50 (n/a)</td><td>179.00 (n/a)</td><td>139.40 (n/a)</td><td>22.15 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.50 (n/a)</td><td>166.14 (n/a)</td><td>174.60 (n/a)</td><td>134.90 (n/a)</td><td>18.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.70 (n/a)</td><td>180.22 (n/a)</td><td>187.50 (n/a)</td><td>124.60 (n/a)</td><td>40.03 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>309.40 (n/a)</td><td>219.10 (n/a)</td><td>214.80 (n/a)</td><td>124.70 (n/a)</td><td>75.96 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.10 (n/a)</td><td>176.58 (n/a)</td><td>171.50 (n/a)</td><td>150.10 (n/a)</td><td>22.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.40 (n/a)</td><td>218.50 (n/a)</td><td>213.40 (n/a)</td><td>204.20 (n/a)</td><td>12.78 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>172.30 (n/a)</td><td>161.10 (n/a)</td><td>124.10 (n/a)</td><td>37.49 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>199.50 (n/a)</td><td>161.24 (n/a)</td><td>175.50 (n/a)</td><td>106.30 (n/a)</td><td>35.85 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>165.60 (n/a)</td><td>167.50 (n/a)</td><td>119.70 (n/a)</td><td>30.44 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.60 (n/a)</td><td>184.38 (n/a)</td><td>194.80 (n/a)</td><td>142.80 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>181.64 (n/a)</td><td>192.60 (n/a)</td><td>136.50 (n/a)</td><td>31.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.60 (n/a)</td><td>187.92 (n/a)</td><td>189.20 (n/a)</td><td>159.90 (n/a)</td><td>25.37 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>270.00 (n/a)</td><td>190.68 (n/a)</td><td>197.30 (n/a)</td><td>132.80 (n/a)</td><td>54.51 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>335.20 (n/a)</td><td>263.64 (n/a)</td><td>253.50 (n/a)</td><td>217.60 (n/a)</td><td>46.37 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>238.80 (n/a)</td><td>178.66 (n/a)</td><td>164.70 (n/a)</td><td>126.10 (n/a)</td><td>44.97 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>222.30 (n/a)</td><td>173.36 (n/a)</td><td>175.20 (n/a)</td><td>117.40 (n/a)</td><td>41.47 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>277.00 (n/a)</td><td>176.74 (n/a)</td><td>161.40 (n/a)</td><td>115.90 (n/a)</td><td>60.74 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>202.40 (n/a)</td><td>156.92 (n/a)</td><td>164.10 (n/a)</td><td>105.30 (n/a)</td><td>39.30 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>196.80 (n/a)</td><td>161.18 (n/a)</td><td>182.60 (n/a)</td><td>116.30 (n/a)</td><td>40.34 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>251.10 (n/a)</td><td>184.50 (n/a)</td><td>169.90 (n/a)</td><td>127.70 (n/a)</td><td>47.17 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>255.20 (n/a)</td><td>203.08 (n/a)</td><td>197.40 (n/a)</td><td>143.00 (n/a)</td><td>45.09 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>346.00 (n/a)</td><td>269.48 (n/a)</td><td>253.10 (n/a)</td><td>218.90 (n/a)</td><td>55.43 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>260.00 (n/a)</td><td>198.52 (n/a)</td><td>190.50 (n/a)</td><td>173.10 (n/a)</td><td>35.78 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>272.80 (n/a)</td><td>203.68 (n/a)</td><td>189.30 (n/a)</td><td>164.70 (n/a)</td><td>41.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>189.60 (n/a)</td><td>153.00 (n/a)</td><td>135.30 (n/a)</td><td>124.30 (n/a)</td><td>32.52 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>216.90 (n/a)</td><td>172.86 (n/a)</td><td>158.60 (n/a)</td><td>130.00 (n/a)</td><td>38.37 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>209.00 (n/a)</td><td>165.54 (n/a)</td><td>150.90 (n/a)</td><td>125.70 (n/a)</td><td>36.29 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>221.20 (n/a)</td><td>181.34 (n/a)</td><td>189.40 (n/a)</td><td>126.70 (n/a)</td><td>36.12 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>284.10 (n/a)</td><td>199.20 (n/a)</td><td>209.50 (n/a)</td><td>122.30 (n/a)</td><td>60.22 (n/a)</td>
</tr>
</tbody>
</table>


### test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>352.10 (n/a)</td><td>224.66 (n/a)</td><td>191.20 (n/a)</td><td>179.20 (n/a)</td><td>72.27 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-15.50%)</td><td>0.03 (+5.98%)</td><td>0.03 (+9.65%)</td><td>0.02 <b>(+30.23%)</b></td><td>0.00 <b>(-38.72%)</b></td><td>198.40 <b>(-23.22%)</b></td><td>162.38 (-9.65%)</td><td>159.20 (-8.82%)</td><td>134.20 (+18.34%)</td><td>28.67 <b>(-44.50%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>258.40 (n/a)</td><td>179.72 (n/a)</td><td>174.60 (n/a)</td><td>113.40 (n/a)</td><td>51.66 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+9.66%)</td><td>0.03 (+7.16%)</td><td>0.03 (+15.88%)</td><td>0.02 (-6.25%)</td><td>0.01 <b>(+40.99%)</b></td><td>227.60 (+6.65%)</td><td>158.38 (-4.43%)</td><td>143.30 (-13.73%)</td><td>124.70 (-8.78%)</td><td>42.64 <b>(+37.96%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.40 (n/a)</td><td>165.72 (n/a)</td><td>166.10 (n/a)</td><td>136.70 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 <b>(+20.74%)</b></td><td>0.03 <b>(+23.91%)</b></td><td>0.03 <b>(+27.15%)</b></td><td>0.02 <b>(+24.66%)</b></td><td>0.00 (+4.63%)</td><td>187.90 (-19.77%)</td><td>157.44 (-19.63%)</td><td>149.00 <b>(-21.33%)</b></td><td>136.80 (-17.14%)</td><td>19.85 <b>(-29.95%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.20 (n/a)</td><td>195.90 (n/a)</td><td>189.40 (n/a)</td><td>165.10 (n/a)</td><td>28.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 <b>(+40.33%)</b></td><td>0.03 <b>(+38.89%)</b></td><td>0.03 <b>(+44.84%)</b></td><td>0.02 <b>(+30.19%)</b></td><td>0.00 <b>(+107.00%)</b></td><td>172.60 <b>(-23.19%)</b></td><td>146.76 <b>(-27.18%)</b></td><td>142.90 <b>(-30.93%)</b></td><td>123.60 <b>(-28.76%)</b></td><td>22.94 (+14.48%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.70 (n/a)</td><td>201.54 (n/a)</td><td>206.90 (n/a)</td><td>173.50 (n/a)</td><td>20.04 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+10.09%)</td><td>0.02 (+4.54%)</td><td>0.03 <b>(+28.62%)</b></td><td>0.02 <b>(-20.38%)</b></td><td>0.01 <b>(+61.40%)</b></td><td>271.80 <b>(+25.60%)</b></td><td>191.42 (+1.95%)</td><td>160.50 <b>(-22.28%)</b></td><td>121.40 (-9.20%)</td><td>66.58 <b>(+95.33%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.40 (n/a)</td><td>187.76 (n/a)</td><td>206.50 (n/a)</td><td>133.70 (n/a)</td><td>34.09 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-0.61%)</td><td>0.02 (+6.04%)</td><td>0.02 (+8.00%)</td><td>0.02 (+5.69%)</td><td>0.00 (-13.68%)</td><td>217.00 (-5.41%)</td><td>183.16 (-6.16%)</td><td>182.00 (-7.38%)</td><td>153.20 (+0.66%)</td><td>23.79 (-16.11%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.40 (n/a)</td><td>195.18 (n/a)</td><td>196.50 (n/a)</td><td>152.20 (n/a)</td><td>28.36 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-5.20%)</td><td>0.02 (+0.76%)</td><td>0.03 (+5.18%)</td><td>0.02 (-18.40%)</td><td>0.01 (+5.68%)</td><td>256.90 <b>(+22.57%)</b></td><td>173.02 (+0.67%)</td><td>153.50 (-4.95%)</td><td>139.80 (+5.51%)</td><td>48.17 <b>(+35.32%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>209.60 (n/a)</td><td>171.86 (n/a)</td><td>161.50 (n/a)</td><td>132.50 (n/a)</td><td>35.60 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 <b>(+22.97%)</b></td><td>0.02 (+9.41%)</td><td>0.02 (+13.40%)</td><td>0.01 (-10.43%)</td><td>0.00 <b>(+207.31%)</b></td><td>274.40 (+11.64%)</td><td>208.18 (-6.60%)</td><td>194.20 (-11.81%)</td><td>171.70 (-18.70%)</td><td>39.15 <b>(+187.34%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>245.80 (n/a)</td><td>222.90 (n/a)</td><td>220.20 (n/a)</td><td>211.20 (n/a)</td><td>13.62 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (-6.83%)</td><td>0.05 (+0.52%)</td><td>0.05 (+4.86%)</td><td>0.04 (-8.84%)</td><td>0.01 (+2.51%)</td><td>197.90 (+9.70%)</td><td>161.76 (+0.27%)</td><td>162.10 (-4.59%)</td><td>122.20 (+7.29%)</td><td>34.19 <b>(+25.33%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>180.40 (n/a)</td><td>161.32 (n/a)</td><td>169.90 (n/a)</td><td>113.90 (n/a)</td><td>27.28 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 <b>(+35.90%)</b></td><td>0.05 <b>(+21.01%)</b></td><td>0.05 <b>(+21.39%)</b></td><td>0.04 (+4.21%)</td><td>0.01 <b>(+217.45%)</b></td><td>202.00 (-4.04%)</td><td>164.54 (-15.58%)</td><td>161.80 (-17.62%)</td><td>129.50 <b>(-26.42%)</b></td><td>28.99 <b>(+126.26%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>210.50 (n/a)</td><td>194.90 (n/a)</td><td>196.40 (n/a)</td><td>176.00 (n/a)</td><td>12.81 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (-2.33%)</td><td>0.06 (+18.38%)</td><td>0.06 (+17.60%)</td><td>0.05 <b>(+31.18%)</b></td><td>0.01 <b>(-42.17%)</b></td><td>169.40 <b>(-23.76%)</b></td><td>144.96 (-17.80%)</td><td>144.90 (-14.96%)</td><td>128.30 (+2.39%)</td><td>16.56 <b>(-54.72%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.20 (n/a)</td><td>176.34 (n/a)</td><td>170.40 (n/a)</td><td>125.30 (n/a)</td><td>36.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (+9.80%)</td><td>0.05 (+5.23%)</td><td>0.05 (+11.99%)</td><td>0.03 <b>(-27.22%)</b></td><td>0.02 <b>(+80.58%)</b></td><td>321.80 <b>(+37.40%)</b></td><td>186.72 (+4.00%)</td><td>159.00 (-10.72%)</td><td>121.80 (-8.90%)</td><td>81.43 <b>(+127.31%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.20 (n/a)</td><td>179.54 (n/a)</td><td>178.10 (n/a)</td><td>133.70 (n/a)</td><td>35.82 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (+1.66%)</td><td>0.06 <b>(+21.79%)</b></td><td>0.05 <b>(+51.19%)</b></td><td>0.04 <b>(+36.38%)</b></td><td>0.01 <b>(-43.23%)</b></td><td>194.20 <b>(-26.69%)</b></td><td>151.90 <b>(-24.55%)</b></td><td>156.80 <b>(-33.84%)</b></td><td>122.30 (-1.61%)</td><td>28.59 <b>(-58.55%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>264.90 (n/a)</td><td>201.32 (n/a)</td><td>237.00 (n/a)</td><td>124.30 (n/a)</td><td>68.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (+13.43%)</td><td>0.06 (+15.91%)</td><td>0.06 <b>(+26.92%)</b></td><td>0.04 (+7.92%)</td><td>0.01 <b>(+39.68%)</b></td><td>203.80 (-7.36%)</td><td>154.16 (-12.41%)</td><td>135.90 <b>(-21.22%)</b></td><td>120.00 (-11.83%)</td><td>35.60 (+15.48%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.00 (n/a)</td><td>176.00 (n/a)</td><td>172.50 (n/a)</td><td>136.10 (n/a)</td><td>30.82 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (+15.54%)</td><td>0.06 (+19.57%)</td><td>0.06 <b>(+33.26%)</b></td><td>0.04 (+0.95%)</td><td>0.01 <b>(+39.74%)</b></td><td>216.70 (-0.91%)</td><td>155.38 (-14.78%)</td><td>140.30 <b>(-24.97%)</b></td><td>118.30 (-13.46%)</td><td>39.72 <b>(+21.47%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.70 (n/a)</td><td>182.32 (n/a)</td><td>187.00 (n/a)</td><td>136.70 (n/a)</td><td>32.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (+12.62%)</td><td>0.05 (+9.64%)</td><td>0.05 (+19.14%)</td><td>0.04 (+3.87%)</td><td>0.01 <b>(+40.93%)</b></td><td>198.30 (-3.74%)</td><td>161.20 (-7.61%)</td><td>154.50 (-16.03%)</td><td>129.50 (-11.24%)</td><td>31.54 <b>(+23.66%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>174.48 (n/a)</td><td>184.00 (n/a)</td><td>145.90 (n/a)</td><td>25.50 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (-15.25%)</td><td>0.05 (-2.66%)</td><td>0.05 (+1.10%)</td><td>0.04 (+16.37%)</td><td>0.00 <b>(-56.80%)</b></td><td>204.10 (-14.06%)</td><td>180.86 (-0.93%)</td><td>181.10 (-1.09%)</td><td>154.70 (+18.00%)</td><td>18.69 <b>(-56.20%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.50 (n/a)</td><td>182.56 (n/a)</td><td>183.10 (n/a)</td><td>131.10 (n/a)</td><td>42.67 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 <b>(+28.66%)</b></td><td>0.04 (+12.31%)</td><td>0.04 (+11.35%)</td><td>0.04 (+2.96%)</td><td>0.00 <b>(+376.21%)</b></td><td>233.40 (-2.87%)</td><td>206.84 (-10.24%)</td><td>206.00 (-10.20%)</td><td>175.30 <b>(-22.30%)</b></td><td>20.97 <b>(+254.78%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>240.30 (n/a)</td><td>230.44 (n/a)</td><td>229.40 (n/a)</td><td>225.60 (n/a)</td><td>5.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 <b>(+34.33%)</b></td><td>0.10 (+13.39%)</td><td>0.09 (+6.16%)</td><td>0.08 (+16.75%)</td><td>0.02 <b>(+82.93%)</b></td><td>207.70 (-14.35%)</td><td>173.62 (-10.44%)</td><td>176.40 (-5.82%)</td><td>122.90 <b>(-25.56%)</b></td><td>31.53 (+8.85%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>242.50 (n/a)</td><td>193.86 (n/a)</td><td>187.30 (n/a)</td><td>165.10 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (+6.20%)</td><td>0.10 (-0.55%)</td><td>0.10 (+1.26%)</td><td>0.07 (-13.69%)</td><td>0.02 <b>(+25.93%)</b></td><td>241.60 (+15.88%)</td><td>168.70 (+2.69%)</td><td>159.70 (-1.24%)</td><td>121.40 (-5.89%)</td><td>44.54 <b>(+42.17%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>208.50 (n/a)</td><td>164.28 (n/a)</td><td>161.70 (n/a)</td><td>129.00 (n/a)</td><td>31.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (+13.36%)</td><td>0.10 (+11.42%)</td><td>0.10 (+14.75%)</td><td>0.08 (-3.19%)</td><td>0.02 <b>(+50.61%)</b></td><td>218.00 (+3.32%)</td><td>169.64 (-8.71%)</td><td>165.30 (-12.86%)</td><td>130.00 (-11.80%)</td><td>34.73 <b>(+38.73%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.00 (n/a)</td><td>185.82 (n/a)</td><td>189.70 (n/a)</td><td>147.40 (n/a)</td><td>25.03 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 <b>(+40.51%)</b></td><td>0.10 <b>(+22.37%)</b></td><td>0.10 (+14.00%)</td><td>0.08 <b>(+65.08%)</b></td><td>0.02 (+5.24%)</td><td>214.20 <b>(-39.41%)</b></td><td>172.32 <b>(-21.21%)</b></td><td>167.20 (-12.28%)</td><td>126.60 <b>(-28.80%)</b></td><td>33.04 <b>(-56.29%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>353.50 (n/a)</td><td>218.70 (n/a)</td><td>190.60 (n/a)</td><td>177.80 (n/a)</td><td>75.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (+12.95%)</td><td>0.10 <b>(+21.60%)</b></td><td>0.10 (+14.14%)</td><td>0.09 <b>(+46.26%)</b></td><td>0.01 <b>(-43.14%)</b></td><td>182.40 <b>(-31.61%)</b></td><td>167.64 (-19.40%)</td><td>168.60 (-12.42%)</td><td>147.80 (-11.44%)</td><td>12.73 <b>(-66.55%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>266.70 (n/a)</td><td>208.00 (n/a)</td><td>192.50 (n/a)</td><td>166.90 (n/a)</td><td>38.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (+4.39%)</td><td>0.10 (+15.49%)</td><td>0.11 <b>(+21.83%)</b></td><td>0.08 <b>(+31.02%)</b></td><td>0.01 <b>(-23.68%)</b></td><td>193.90 <b>(-23.66%)</b></td><td>166.62 (-14.82%)</td><td>155.20 (-17.93%)</td><td>145.70 (-4.21%)</td><td>21.26 <b>(-44.30%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>254.00 (n/a)</td><td>195.60 (n/a)</td><td>189.10 (n/a)</td><td>152.10 (n/a)</td><td>38.18 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 (+10.21%)</td><td>0.08 (-1.21%)</td><td>0.09 (+10.24%)</td><td>0.05 <b>(-30.57%)</b></td><td>0.02 <b>(+142.37%)</b></td><td>313.80 <b>(+44.01%)</b></td><td>212.56 (+5.96%)</td><td>190.30 (-9.29%)</td><td>158.40 (-9.23%)</td><td>59.88 <b>(+231.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.90 (n/a)</td><td>200.60 (n/a)</td><td>209.80 (n/a)</td><td>174.50 (n/a)</td><td>18.05 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 <b>(+20.66%)</b></td><td>0.08 (+15.65%)</td><td>0.08 (+13.11%)</td><td>0.07 (+18.51%)</td><td>0.01 <b>(+53.08%)</b></td><td>225.50 (-15.61%)</td><td>198.02 (-13.09%)</td><td>196.60 (-11.60%)</td><td>170.90 (-17.16%)</td><td>25.83 (+6.86%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>267.20 (n/a)</td><td>227.84 (n/a)</td><td>222.40 (n/a)</td><td>206.30 (n/a)</td><td>24.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 (-2.50%)</td><td>0.20 (-2.91%)</td><td>0.18 (-0.68%)</td><td>0.15 (-10.17%)</td><td>0.05 (+13.58%)</td><td>221.50 (+11.36%)</td><td>171.28 (+4.39%)</td><td>182.00 (+0.66%)</td><td>129.60 (+2.53%)</td><td>40.43 <b>(+25.73%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>198.90 (n/a)</td><td>164.08 (n/a)</td><td>180.80 (n/a)</td><td>126.40 (n/a)</td><td>32.16 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (-5.00%)</td><td>0.21 (-3.12%)</td><td>0.24 (+8.15%)</td><td>0.15 (-4.95%)</td><td>0.05 (+8.05%)</td><td>222.10 (+5.21%)</td><td>164.66 (+4.39%)</td><td>138.10 (-7.50%)</td><td>128.40 (+5.25%)</td><td>42.43 (+19.12%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>211.10 (n/a)</td><td>157.74 (n/a)</td><td>149.30 (n/a)</td><td>122.00 (n/a)</td><td>35.62 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (+15.28%)</td><td>0.21 (+8.94%)</td><td>0.22 (+10.37%)</td><td>0.18 (+18.38%)</td><td>0.03 (+13.12%)</td><td>181.10 (-15.53%)</td><td>155.36 (-8.30%)</td><td>151.60 (-9.38%)</td><td>124.10 (-13.22%)</td><td>23.27 (-16.77%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>214.40 (n/a)</td><td>169.42 (n/a)</td><td>167.30 (n/a)</td><td>143.00 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 (-16.16%)</td><td>0.20 (-0.95%)</td><td>0.21 (+1.27%)</td><td>0.17 <b>(+33.76%)</b></td><td>0.02 <b>(-65.32%)</b></td><td>192.60 <b>(-25.26%)</b></td><td>164.22 (-5.11%)</td><td>158.40 (-1.25%)</td><td>150.60 (+19.33%)</td><td>17.21 <b>(-68.29%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>257.70 (n/a)</td><td>173.06 (n/a)</td><td>160.40 (n/a)</td><td>126.20 (n/a)</td><td>54.27 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 <b>(+29.70%)</b></td><td>0.19 <b>(+25.81%)</b></td><td>0.18 (+18.16%)</td><td>0.17 <b>(+30.35%)</b></td><td>0.02 <b>(+57.93%)</b></td><td>188.00 <b>(-23.27%)</b></td><td>171.14 <b>(-20.23%)</b></td><td>183.80 (-15.34%)</td><td>147.40 <b>(-22.91%)</b></td><td>19.50 (-6.24%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>245.00 (n/a)</td><td>214.54 (n/a)</td><td>217.10 (n/a)</td><td>191.20 (n/a)</td><td>20.80 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 <b>(+32.03%)</b></td><td>0.21 <b>(+28.82%)</b></td><td>0.21 <b>(+24.61%)</b></td><td>0.17 <b>(+41.45%)</b></td><td>0.03 (+7.89%)</td><td>196.20 <b>(-29.30%)</b></td><td>157.32 <b>(-23.24%)</b></td><td>153.60 (-19.75%)</td><td>128.90 <b>(-24.27%)</b></td><td>24.44 <b>(-42.73%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>277.50 (n/a)</td><td>204.94 (n/a)</td><td>191.40 (n/a)</td><td>170.20 (n/a)</td><td>42.67 (n/a)</td>
</tr>
</tbody>
</table>


### test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 <b>(+43.26%)</b></td><td>0.18 <b>(+27.83%)</b></td><td>0.18 (+19.91%)</td><td>0.14 <b>(+31.46%)</b></td><td>0.03 <b>(+52.27%)</b></td><td>236.80 <b>(-23.93%)</b></td><td>190.68 <b>(-21.46%)</b></td><td>187.10 (-16.58%)</td><td>151.00 <b>(-30.19%)</b></td><td>32.22 (-19.38%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>311.30 (n/a)</td><td>242.78 (n/a)</td><td>224.30 (n/a)</td><td>216.30 (n/a)</td><td>39.97 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 <b>(+28.82%)</b></td><td>0.03 <b>(+23.81%)</b></td><td>0.03 <b>(+34.99%)</b></td><td>0.02 (-7.05%)</td><td>0.01 <b>(+95.68%)</b></td><td>206.70 (+7.60%)</td><td>143.12 (-15.40%)</td><td>130.70 <b>(-25.95%)</b></td><td>98.90 <b>(-22.37%)</b></td><td>43.07 <b>(+67.95%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.10 (n/a)</td><td>169.18 (n/a)</td><td>176.50 (n/a)</td><td>127.40 (n/a)</td><td>25.65 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (-0.85%)</td><td>0.03 (+6.81%)</td><td>0.03 (+7.55%)</td><td>0.03 <b>(+24.64%)</b></td><td>0.01 <b>(-33.94%)</b></td><td>159.50 (-19.77%)</td><td>139.18 (-9.71%)</td><td>146.50 (-7.04%)</td><td>108.10 (+0.84%)</td><td>21.10 <b>(-46.73%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>198.80 (n/a)</td><td>154.14 (n/a)</td><td>157.60 (n/a)</td><td>107.20 (n/a)</td><td>39.62 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.00 <b>(-100.00%)</b></td><td>0.00 <b>(-100.00%)</b></td><td>0.00 <b>(-100.00%)</b></td><td>0.00 <b>(-100.00%)</b></td><td>0.00 <b>(-100.00%)</b></td><td>4745612.50 <b>(+2094168.53%)</b></td><td>4745612.50 <b>(+2681037.01%)</b></td><td>4745612.50 <b>(+2722569.25%)</b></td><td>4745612.50 <b>(+3316191.06%)</b></td><td>0.00 <b>(-100.00%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.60 (n/a)</td><td>177.00 (n/a)</td><td>174.30 (n/a)</td><td>143.10 (n/a)</td><td>33.08 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-13.48%)</td><td>0.02 (-13.74%)</td><td>0.02 (-4.17%)</td><td>0.02 (-16.13%)</td><td>0.00 (+0.17%)</td><td>268.50 (+19.23%)</td><td>201.00 (+17.11%)</td><td>174.50 (+4.37%)</td><td>160.60 (+15.54%)</td><td>45.54 <b>(+36.55%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.20 (n/a)</td><td>171.64 (n/a)</td><td>167.20 (n/a)</td><td>139.00 (n/a)</td><td>33.35 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-0.49%)</td><td>0.03 (+8.29%)</td><td>0.03 (+18.58%)</td><td>0.02 (+6.55%)</td><td>0.00 <b>(-29.20%)</b></td><td>165.50 (-6.13%)</td><td>133.20 (-9.17%)</td><td>124.60 (-15.64%)</td><td>117.90 (+0.43%)</td><td>19.59 <b>(-32.09%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>176.30 (n/a)</td><td>146.64 (n/a)</td><td>147.70 (n/a)</td><td>117.40 (n/a)</td><td>28.84 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+10.14%)</td><td>0.03 (-3.51%)</td><td>0.03 (+15.93%)</td><td>0.01 <b>(-53.84%)</b></td><td>0.01 <b>(+255.85%)</b></td><td>376.70 <b>(+116.62%)</b></td><td>188.46 <b>(+24.54%)</b></td><td>128.50 (-13.76%)</td><td>119.10 (-9.15%)</td><td>110.04 <b>(+583.55%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>173.90 (n/a)</td><td>151.32 (n/a)</td><td>149.00 (n/a)</td><td>131.10 (n/a)</td><td>16.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+7.82%)</td><td>0.03 (+11.58%)</td><td>0.02 (+19.05%)</td><td>0.02 <b>(+32.36%)</b></td><td>0.00 <b>(-25.43%)</b></td><td>183.60 <b>(-24.48%)</b></td><td>159.66 (-13.60%)</td><td>172.70 (-16.00%)</td><td>118.50 (-7.28%)</td><td>25.93 <b>(-47.00%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>243.10 (n/a)</td><td>184.80 (n/a)</td><td>205.60 (n/a)</td><td>127.80 (n/a)</td><td>48.93 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-1.06%)</td><td>0.03 (-7.97%)</td><td>0.03 (-15.33%)</td><td>0.02 (+4.86%)</td><td>0.01 (+1.40%)</td><td>203.90 (-4.63%)</td><td>156.78 (+8.89%)</td><td>139.80 (+18.17%)</td><td>117.80 (+1.03%)</td><td>42.72 (+1.95%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>143.98 (n/a)</td><td>118.30 (n/a)</td><td>116.60 (n/a)</td><td>41.90 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+16.61%)</td><td>0.03 (+2.48%)</td><td>0.03 (+2.21%)</td><td>0.02 (-18.39%)</td><td>0.01 <b>(+108.50%)</b></td><td>222.80 <b>(+22.48%)</b></td><td>162.90 (+0.80%)</td><td>160.20 (-2.20%)</td><td>119.90 (-14.30%)</td><td>38.60 <b>(+121.87%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.90 (n/a)</td><td>161.60 (n/a)</td><td>163.80 (n/a)</td><td>139.90 (n/a)</td><td>17.40 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 <b>(+46.27%)</b></td><td>0.03 <b>(+53.65%)</b></td><td>0.03 <b>(+56.92%)</b></td><td>0.02 <b>(+45.53%)</b></td><td>0.01 <b>(+21.71%)</b></td><td>247.50 <b>(-31.27%)</b></td><td>164.34 <b>(-36.81%)</b></td><td>146.10 <b>(-36.28%)</b></td><td>121.00 <b>(-31.64%)</b></td><td>51.37 <b>(-43.40%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>360.10 (n/a)</td><td>260.08 (n/a)</td><td>229.30 (n/a)</td><td>177.00 (n/a)</td><td>90.76 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+8.39%)</td><td>0.03 (-2.89%)</td><td>0.03 (+8.30%)</td><td>0.02 <b>(-27.39%)</b></td><td>0.01 <b>(+168.16%)</b></td><td>239.60 <b>(+37.78%)</b></td><td>172.80 (+8.00%)</td><td>152.60 (-7.68%)</td><td>131.60 (-7.71%)</td><td>46.62 <b>(+239.43%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>173.90 (n/a)</td><td>160.00 (n/a)</td><td>165.30 (n/a)</td><td>142.60 (n/a)</td><td>13.74 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+1.33%)</td><td>0.02 (-6.72%)</td><td>0.02 (-3.61%)</td><td>0.02 <b>(-23.71%)</b></td><td>0.01 <b>(+89.39%)</b></td><td>237.40 <b>(+31.09%)</b></td><td>178.02 (+10.85%)</td><td>167.50 (+3.78%)</td><td>133.00 (-1.26%)</td><td>41.84 <b>(+151.38%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.10 (n/a)</td><td>160.60 (n/a)</td><td>161.40 (n/a)</td><td>134.70 (n/a)</td><td>16.64 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-2.48%)</td><td>0.02 (-7.50%)</td><td>0.02 (-10.32%)</td><td>0.02 <b>(-30.31%)</b></td><td>0.01 <b>(+80.09%)</b></td><td>272.90 <b>(+43.48%)</b></td><td>177.04 (+14.32%)</td><td>169.00 (+11.55%)</td><td>130.90 (+2.51%)</td><td>58.08 <b>(+157.22%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.20 (n/a)</td><td>154.86 (n/a)</td><td>151.50 (n/a)</td><td>127.70 (n/a)</td><td>22.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-9.80%)</td><td>0.02 (-14.01%)</td><td>0.03 (-9.66%)</td><td>0.02 <b>(-25.93%)</b></td><td>0.01 <b>(+20.84%)</b></td><td>240.40 <b>(+34.98%)</b></td><td>175.00 (+19.54%)</td><td>158.00 (+10.64%)</td><td>129.00 (+10.82%)</td><td>45.80 <b>(+81.40%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.10 (n/a)</td><td>146.40 (n/a)</td><td>142.80 (n/a)</td><td>116.40 (n/a)</td><td>25.25 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 <b>(-35.27%)</b></td><td>0.02 <b>(-29.77%)</b></td><td>0.02 <b>(-25.98%)</b></td><td>0.01 <b>(-30.99%)</b></td><td>0.00 <b>(-37.03%)</b></td><td>273.30 <b>(+44.91%)</b></td><td>230.54 <b>(+42.13%)</b></td><td>226.10 <b>(+35.07%)</b></td><td>189.00 <b>(+54.54%)</b></td><td>36.86 <b>(+45.31%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>188.60 (n/a)</td><td>162.20 (n/a)</td><td>167.40 (n/a)</td><td>122.30 (n/a)</td><td>25.36 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (+8.77%)</td><td>0.02 <b>(-20.77%)</b></td><td>0.02 <b>(-28.41%)</b></td><td>0.02 <b>(-26.91%)</b></td><td>0.01 <b>(+64.38%)</b></td><td>256.00 <b>(+36.83%)</b></td><td>190.02 <b>(+32.92%)</b></td><td>182.90 <b>(+39.72%)</b></td><td>114.10 (-8.06%)</td><td>53.83 <b>(+102.97%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>187.10 (n/a)</td><td>142.96 (n/a)</td><td>130.90 (n/a)</td><td>124.10 (n/a)</td><td>26.52 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (+0.37%)</td><td>0.05 (-17.06%)</td><td>0.05 (-8.35%)</td><td>0.03 <b>(-35.47%)</b></td><td>0.02 <b>(+69.87%)</b></td><td>240.60 <b>(+54.93%)</b></td><td>173.56 <b>(+27.58%)</b></td><td>151.20 (+9.09%)</td><td>115.30 (-0.35%)</td><td>52.63 <b>(+172.54%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>155.30 (n/a)</td><td>136.04 (n/a)</td><td>138.60 (n/a)</td><td>115.70 (n/a)</td><td>19.31 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (-3.81%)</td><td>0.05 (-16.87%)</td><td>0.05 <b>(-23.11%)</b></td><td>0.04 <b>(-27.05%)</b></td><td>0.01 <b>(+37.69%)</b></td><td>200.60 <b>(+37.12%)</b></td><td>158.88 <b>(+22.08%)</b></td><td>156.70 <b>(+30.04%)</b></td><td>124.10 (+3.94%)</td><td>27.48 <b>(+97.60%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>146.30 (n/a)</td><td>130.14 (n/a)</td><td>120.50 (n/a)</td><td>119.40 (n/a)</td><td>13.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (+14.52%)</td><td>0.04 (-0.85%)</td><td>0.04 (-2.83%)</td><td>0.02 <b>(-32.30%)</b></td><td>0.01 <b>(+143.96%)</b></td><td>345.20 <b>(+47.71%)</b></td><td>219.98 (+7.48%)</td><td>209.00 (+2.90%)</td><td>154.90 (-12.68%)</td><td>73.97 <b>(+228.11%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>233.70 (n/a)</td><td>204.68 (n/a)</td><td>203.10 (n/a)</td><td>177.40 (n/a)</td><td>22.54 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 <b>(+23.12%)</b></td><td>0.05 (+19.53%)</td><td>0.04 (+17.09%)</td><td>0.04 <b>(+41.82%)</b></td><td>0.01 (-16.57%)</td><td>204.90 <b>(-29.49%)</b></td><td>177.30 (-18.26%)</td><td>182.40 (-14.57%)</td><td>139.70 (-18.83%)</td><td>23.94 <b>(-51.72%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>290.60 (n/a)</td><td>216.90 (n/a)</td><td>213.50 (n/a)</td><td>172.10 (n/a)</td><td>49.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (-12.02%)</td><td>0.05 (-13.56%)</td><td>0.05 (-14.93%)</td><td>0.04 (-16.12%)</td><td>0.01 (+11.04%)</td><td>210.30 (+19.22%)</td><td>174.44 (+16.70%)</td><td>175.70 (+17.53%)</td><td>140.60 (+13.66%)</td><td>28.67 <b>(+50.42%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>176.40 (n/a)</td><td>149.48 (n/a)</td><td>149.50 (n/a)</td><td>123.70 (n/a)</td><td>19.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (-4.66%)</td><td>0.05 (-18.43%)</td><td>0.05 <b>(-24.63%)</b></td><td>0.04 <b>(-27.71%)</b></td><td>0.01 <b>(+56.55%)</b></td><td>215.20 <b>(+38.39%)</b></td><td>172.06 <b>(+26.70%)</b></td><td>177.60 <b>(+32.64%)</b></td><td>119.20 (+4.93%)</td><td>39.24 <b>(+124.96%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>155.50 (n/a)</td><td>135.80 (n/a)</td><td>133.90 (n/a)</td><td>113.60 (n/a)</td><td>17.44 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (-15.57%)</td><td>0.04 <b>(-30.31%)</b></td><td>0.04 <b>(-30.68%)</b></td><td>0.03 <b>(-48.21%)</b></td><td>0.01 <b>(+35.15%)</b></td><td>297.80 <b>(+93.00%)</b></td><td>205.34 <b>(+52.19%)</b></td><td>203.10 <b>(+44.25%)</b></td><td>122.40 (+18.49%)</td><td>62.49 <b>(+200.22%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>154.30 (n/a)</td><td>134.92 (n/a)</td><td>140.80 (n/a)</td><td>103.30 (n/a)</td><td>20.81 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (-6.34%)</td><td>0.04 (-10.97%)</td><td>0.04 (-15.19%)</td><td>0.04 (-12.26%)</td><td>0.01 (+18.43%)</td><td>224.30 (+13.97%)</td><td>188.64 (+13.73%)</td><td>205.90 (+17.93%)</td><td>146.20 (+6.72%)</td><td>35.33 <b>(+44.72%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.80 (n/a)</td><td>165.86 (n/a)</td><td>174.60 (n/a)</td><td>137.00 (n/a)</td><td>24.41 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (-7.92%)</td><td>0.05 (-7.88%)</td><td>0.05 (-11.02%)</td><td>0.04 (+2.48%)</td><td>0.01 <b>(-26.39%)</b></td><td>201.80 (-2.42%)</td><td>168.86 (+7.20%)</td><td>168.00 (+12.37%)</td><td>136.40 (+8.60%)</td><td>23.85 <b>(-23.73%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.80 (n/a)</td><td>157.52 (n/a)</td><td>149.50 (n/a)</td><td>125.60 (n/a)</td><td>31.27 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (+0.52%)</td><td>0.05 (+10.48%)</td><td>0.05 <b>(+21.45%)</b></td><td>0.05 <b>(+22.93%)</b></td><td>0.01 <b>(-35.22%)</b></td><td>179.50 (-18.67%)</td><td>154.28 (-11.77%)</td><td>150.70 (-17.65%)</td><td>126.40 (-0.55%)</td><td>19.63 <b>(-47.39%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.70 (n/a)</td><td>174.86 (n/a)</td><td>183.00 (n/a)</td><td>127.10 (n/a)</td><td>37.31 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 (-1.08%)</td><td>0.05 (-2.32%)</td><td>0.05 (-0.62%)</td><td>0.04 (-9.32%)</td><td>0.01 <b>(+43.82%)</b></td><td>199.20 (+10.24%)</td><td>166.42 (+2.97%)</td><td>160.90 (+0.63%)</td><td>149.20 (+1.08%)</td><td>19.70 <b>(+60.82%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>180.70 (n/a)</td><td>161.62 (n/a)</td><td>159.90 (n/a)</td><td>147.60 (n/a)</td><td>12.25 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (+3.86%)</td><td>0.05 (-0.52%)</td><td>0.06 (-5.24%)</td><td>0.02 <b>(-44.95%)</b></td><td>0.02 <b>(+38.58%)</b></td><td>405.90 <b>(+81.61%)</b></td><td>190.46 (+15.95%)</td><td>144.70 (+5.54%)</td><td>111.90 (-3.70%)</td><td>122.04 <b>(+152.14%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.50 (n/a)</td><td>164.26 (n/a)</td><td>137.10 (n/a)</td><td>116.20 (n/a)</td><td>48.40 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 <b>(-22.24%)</b></td><td>0.05 (-5.09%)</td><td>0.05 (+7.49%)</td><td>0.04 (+13.81%)</td><td>0.01 <b>(-53.04%)</b></td><td>218.40 (-12.11%)</td><td>176.72 (+0.45%)</td><td>169.90 (-7.01%)</td><td>149.40 <b>(+28.57%)</b></td><td>26.92 <b>(-45.90%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.50 (n/a)</td><td>175.92 (n/a)</td><td>182.70 (n/a)</td><td>116.20 (n/a)</td><td>49.76 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 <b>(+26.76%)</b></td><td>0.05 (+11.32%)</td><td>0.05 (+10.72%)</td><td>0.04 (+1.25%)</td><td>0.01 <b>(+96.82%)</b></td><td>208.20 (-1.23%)</td><td>162.08 (-8.04%)</td><td>158.50 (-9.64%)</td><td>120.20 <b>(-21.08%)</b></td><td>33.76 <b>(+52.01%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>176.26 (n/a)</td><td>175.40 (n/a)</td><td>152.30 (n/a)</td><td>22.21 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (-9.02%)</td><td>0.05 (+7.92%)</td><td>0.05 <b>(+20.56%)</b></td><td>0.04 (+18.88%)</td><td>0.01 <b>(-45.57%)</b></td><td>205.10 (-15.87%)</td><td>173.88 (-10.40%)</td><td>168.40 (-17.04%)</td><td>148.10 (+9.95%)</td><td>22.67 <b>(-49.31%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.80 (n/a)</td><td>194.06 (n/a)</td><td>203.00 (n/a)</td><td>134.70 (n/a)</td><td>44.72 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (-13.32%)</td><td>0.05 (+2.55%)</td><td>0.05 (+16.14%)</td><td>0.04 (-7.18%)</td><td>0.01 <b>(-24.09%)</b></td><td>202.70 (+7.76%)</td><td>159.36 (-2.97%)</td><td>150.10 (-13.88%)</td><td>142.40 (+15.40%)</td><td>24.67 (-0.45%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.10 (n/a)</td><td>164.24 (n/a)</td><td>174.30 (n/a)</td><td>123.40 (n/a)</td><td>24.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (-13.86%)</td><td>0.10 (-11.46%)</td><td>0.10 <b>(-21.03%)</b></td><td>0.09 (+2.00%)</td><td>0.01 <b>(-42.48%)</b></td><td>179.50 (-1.97%)</td><td>165.04 (+10.90%)</td><td>171.50 <b>(+26.66%)</b></td><td>135.70 (+16.08%)</td><td>18.21 <b>(-36.42%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>183.10 (n/a)</td><td>148.82 (n/a)</td><td>135.40 (n/a)</td><td>116.90 (n/a)</td><td>28.64 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (-17.04%)</td><td>0.09 (-17.62%)</td><td>0.08 <b>(-23.50%)</b></td><td>0.07 (-16.22%)</td><td>0.02 (+3.39%)</td><td>236.50 (+19.32%)</td><td>196.00 <b>(+22.65%)</b></td><td>207.00 <b>(+30.76%)</b></td><td>153.50 <b>(+20.49%)</b></td><td>37.22 <b>(+45.52%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>198.20 (n/a)</td><td>159.80 (n/a)</td><td>158.30 (n/a)</td><td>127.40 (n/a)</td><td>25.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (+6.04%)</td><td>0.09 (-2.37%)</td><td>0.08 (-11.78%)</td><td>0.06 (-13.52%)</td><td>0.02 <b>(+58.46%)</b></td><td>267.40 (+15.61%)</td><td>198.04 (+5.40%)</td><td>206.40 (+13.34%)</td><td>147.00 (-5.65%)</td><td>48.25 <b>(+67.08%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>231.30 (n/a)</td><td>187.90 (n/a)</td><td>182.10 (n/a)</td><td>155.80 (n/a)</td><td>28.88 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (+0.24%)</td><td>0.08 (-9.97%)</td><td>0.08 (-10.54%)</td><td>0.07 (-8.06%)</td><td>0.01 <b>(+38.31%)</b></td><td>229.60 (+8.76%)</td><td>197.76 (+12.26%)</td><td>193.40 (+11.79%)</td><td>155.80 (-0.26%)</td><td>31.16 <b>(+49.96%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.10 (n/a)</td><td>176.16 (n/a)</td><td>173.00 (n/a)</td><td>156.20 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (-13.30%)</td><td>0.10 (-19.22%)</td><td>0.09 <b>(-29.10%)</b></td><td>0.08 (+9.14%)</td><td>0.02 <b>(-35.28%)</b></td><td>199.30 (-8.37%)</td><td>170.80 <b>(+20.01%)</b></td><td>177.10 <b>(+41.00%)</b></td><td>131.30 (+15.28%)</td><td>27.73 <b>(-34.84%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>217.50 (n/a)</td><td>142.32 (n/a)</td><td>125.60 (n/a)</td><td>113.90 (n/a)</td><td>42.55 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (+5.76%)</td><td>0.12 (+12.48%)</td><td>0.12 (+18.56%)</td><td>0.09 (+14.86%)</td><td>0.02 (-19.82%)</td><td>174.50 (-12.97%)</td><td>139.36 (-12.90%)</td><td>137.60 (-15.63%)</td><td>108.80 (-5.47%)</td><td>23.59 <b>(-34.32%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>200.50 (n/a)</td><td>160.00 (n/a)</td><td>163.10 (n/a)</td><td>115.10 (n/a)</td><td>35.93 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (-8.89%)</td><td>0.12 (+8.69%)</td><td>0.12 (+17.87%)</td><td>0.09 (+14.29%)</td><td>0.02 <b>(-32.83%)</b></td><td>174.40 (-12.49%)</td><td>145.80 (-11.18%)</td><td>142.40 (-15.14%)</td><td>108.00 (+9.76%)</td><td>27.16 <b>(-33.23%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>199.30 (n/a)</td><td>164.16 (n/a)</td><td>167.80 (n/a)</td><td>98.40 (n/a)</td><td>40.67 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (+11.16%)</td><td>0.11 (-6.25%)</td><td>0.10 (-12.79%)</td><td>0.09 (-15.93%)</td><td>0.02 <b>(+101.77%)</b></td><td>186.00 (+18.93%)</td><td>156.98 (+9.15%)</td><td>165.40 (+14.70%)</td><td>111.70 (-9.99%)</td><td>27.83 <b>(+105.19%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>156.40 (n/a)</td><td>143.82 (n/a)</td><td>144.20 (n/a)</td><td>124.10 (n/a)</td><td>13.56 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (+2.55%)</td><td>0.10 (-0.48%)</td><td>0.11 (+1.91%)</td><td>0.08 (-11.60%)</td><td>0.02 <b>(+40.01%)</b></td><td>211.80 (+13.08%)</td><td>162.96 (+2.12%)</td><td>155.00 (-1.84%)</td><td>130.30 (-2.47%)</td><td>32.72 <b>(+54.36%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>187.30 (n/a)</td><td>159.58 (n/a)</td><td>157.90 (n/a)</td><td>133.60 (n/a)</td><td>21.20 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (+15.38%)</td><td>0.12 (+13.68%)</td><td>0.13 <b>(+31.05%)</b></td><td>0.08 (-2.36%)</td><td>0.03 <b>(+63.62%)</b></td><td>200.30 (+2.40%)</td><td>149.12 (-9.02%)</td><td>128.30 <b>(-23.72%)</b></td><td>111.50 (-13.36%)</td><td>41.35 <b>(+47.88%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.60 (n/a)</td><td>163.90 (n/a)</td><td>168.20 (n/a)</td><td>128.70 (n/a)</td><td>27.96 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (+15.78%)</td><td>0.10 (+8.82%)</td><td>0.10 (-5.38%)</td><td>0.08 <b>(+29.76%)</b></td><td>0.02 (-4.39%)</td><td>202.20 <b>(-22.94%)</b></td><td>165.10 (-9.84%)</td><td>158.20 (+5.68%)</td><td>125.30 (-13.59%)</td><td>34.79 <b>(-32.51%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>262.40 (n/a)</td><td>183.12 (n/a)</td><td>149.70 (n/a)</td><td>145.00 (n/a)</td><td>51.56 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 <b>(-30.62%)</b></td><td>0.10 (-7.88%)</td><td>0.10 (+0.95%)</td><td>0.09 (+18.16%)</td><td>0.01 <b>(-77.07%)</b></td><td>188.20 (-15.38%)</td><td>167.62 (+1.01%)</td><td>164.80 (-0.96%)</td><td>150.70 <b>(+44.07%)</b></td><td>13.65 <b>(-72.16%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>222.40 (n/a)</td><td>165.94 (n/a)</td><td>166.40 (n/a)</td><td>104.60 (n/a)</td><td>49.03 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (-10.26%)</td><td>0.09 (-8.65%)</td><td>0.09 (-12.87%)</td><td>0.07 <b>(+26.04%)</b></td><td>0.02 <b>(-32.67%)</b></td><td>239.00 <b>(-20.65%)</b></td><td>188.06 (+3.98%)</td><td>182.90 (+14.81%)</td><td>144.60 (+11.40%)</td><td>38.06 <b>(-44.49%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>301.20 (n/a)</td><td>180.86 (n/a)</td><td>159.30 (n/a)</td><td>129.80 (n/a)</td><td>68.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (-2.10%)</td><td>0.10 (-1.10%)</td><td>0.09 (-2.86%)</td><td>0.09 (+11.86%)</td><td>0.01 <b>(-29.93%)</b></td><td>185.80 (-10.59%)</td><td>171.42 (+0.12%)</td><td>176.50 (+2.92%)</td><td>143.70 (+2.20%)</td><td>16.28 <b>(-37.25%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>171.22 (n/a)</td><td>171.50 (n/a)</td><td>140.60 (n/a)</td><td>25.95 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 (-18.14%)</td><td>0.09 (-11.39%)</td><td>0.09 (-9.27%)</td><td>0.08 (-13.06%)</td><td>0.01 <b>(-33.64%)</b></td><td>194.40 (+15.03%)</td><td>175.94 (+12.51%)</td><td>175.80 (+10.22%)</td><td>159.90 <b>(+22.15%)</b></td><td>14.11 (-5.08%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>169.00 (n/a)</td><td>156.38 (n/a)</td><td>159.50 (n/a)</td><td>130.90 (n/a)</td><td>14.87 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (+1.32%)</td><td>0.10 (+14.35%)</td><td>0.09 (-1.54%)</td><td>0.08 <b>(+78.50%)</b></td><td>0.02 <b>(-43.30%)</b></td><td>203.00 <b>(-43.98%)</b></td><td>168.50 <b>(-22.56%)</b></td><td>184.40 (+1.60%)</td><td>131.20 (-1.28%)</td><td>31.52 <b>(-68.14%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>362.40 (n/a)</td><td>217.60 (n/a)</td><td>181.50 (n/a)</td><td>132.90 (n/a)</td><td>98.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.23 (-7.17%)</td><td>0.20 (-4.89%)</td><td>0.19 (-6.81%)</td><td>0.17 (-2.42%)</td><td>0.02 (-6.11%)</td><td>190.40 (+2.48%)</td><td>167.60 (+5.10%)</td><td>174.50 (+7.32%)</td><td>141.60 (+7.68%)</td><td>20.42 (+4.25%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>185.80 (n/a)</td><td>159.46 (n/a)</td><td>162.60 (n/a)</td><td>131.50 (n/a)</td><td>19.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.24 (-1.67%)</td><td>0.20 (-2.14%)</td><td>0.20 (-1.51%)</td><td>0.15 (-9.04%)</td><td>0.04 (+5.66%)</td><td>224.60 (+9.94%)</td><td>170.62 (+2.78%)</td><td>163.80 (+1.55%)</td><td>135.50 (+1.65%)</td><td>34.36 (+19.35%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>204.30 (n/a)</td><td>166.00 (n/a)</td><td>161.30 (n/a)</td><td>133.30 (n/a)</td><td>28.79 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (+8.45%)</td><td>0.17 (-0.15%)</td><td>0.17 (+2.82%)</td><td>0.14 (-8.50%)</td><td>0.02 <b>(+121.67%)</b></td><td>232.60 (+9.30%)</td><td>201.34 (+1.46%)</td><td>191.50 (-2.74%)</td><td>169.60 (-7.78%)</td><td>28.75 <b>(+128.41%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>212.80 (n/a)</td><td>198.44 (n/a)</td><td>196.90 (n/a)</td><td>183.90 (n/a)</td><td>12.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.20 (-9.26%)</td><td>0.18 (-3.21%)</td><td>0.20 (+6.26%)</td><td>0.14 (-3.86%)</td><td>0.03 (+9.58%)</td><td>230.90 (+4.01%)</td><td>187.20 (+4.00%)</td><td>163.60 (-5.92%)</td><td>161.20 (+10.18%)</td><td>34.40 <b>(+22.72%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>222.00 (n/a)</td><td>180.00 (n/a)</td><td>173.90 (n/a)</td><td>146.30 (n/a)</td><td>28.03 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.32 (+14.56%)</td><td>0.23 (+6.65%)</td><td>0.21 (+0.90%)</td><td>0.17 (+6.97%)</td><td>0.06 <b>(+24.02%)</b></td><td>190.50 (-6.53%)</td><td>152.30 (-5.50%)</td><td>155.40 (-0.89%)</td><td>101.80 (-12.77%)</td><td>33.91 (-1.54%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>203.80 (n/a)</td><td>161.16 (n/a)</td><td>156.80 (n/a)</td><td>116.70 (n/a)</td><td>34.44 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 <b>(+25.80%)</b></td><td>0.24 <b>(+28.99%)</b></td><td>0.25 <b>(+20.76%)</b></td><td>0.18 <b>(+27.63%)</b></td><td>0.04 (-3.51%)</td><td>182.90 <b>(-21.64%)</b></td><td>139.54 <b>(-23.51%)</b></td><td>132.80 (-17.21%)</td><td>119.30 <b>(-20.47%)</b></td><td>24.91 <b>(-36.96%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>233.40 (n/a)</td><td>182.42 (n/a)</td><td>160.40 (n/a)</td><td>150.00 (n/a)</td><td>39.52 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.28 (+2.57%)</td><td>0.24 (+10.19%)</td><td>0.24 (+1.07%)</td><td>0.19 <b>(+44.98%)</b></td><td>0.03 <b>(-38.59%)</b></td><td>168.40 <b>(-31.01%)</b></td><td>138.42 (-13.67%)</td><td>137.00 (-1.08%)</td><td>116.40 (-2.51%)</td><td>20.81 <b>(-59.27%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.24 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>244.10 (n/a)</td><td>160.34 (n/a)</td><td>138.50 (n/a)</td><td>119.40 (n/a)</td><td>51.09 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 (-1.03%)</td><td>0.23 (+9.18%)</td><td>0.24 (+18.78%)</td><td>0.20 (+5.89%)</td><td>0.03 (-10.58%)</td><td>167.80 (-5.57%)</td><td>142.64 (-8.81%)</td><td>135.70 (-15.82%)</td><td>119.30 (+1.10%)</td><td>20.77 (-11.91%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>177.70 (n/a)</td><td>156.42 (n/a)</td><td>161.20 (n/a)</td><td>118.00 (n/a)</td><td>23.58 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.30 <b>(+33.50%)</b></td><td>0.23 (+13.34%)</td><td>0.26 <b>(+21.20%)</b></td><td>0.15 (-10.37%)</td><td>0.07 <b>(+161.79%)</b></td><td>223.80 (+11.57%)</td><td>150.46 (-6.23%)</td><td>124.40 (-17.45%)</td><td>108.30 <b>(-25.10%)</b></td><td>48.84 <b>(+114.05%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>200.60 (n/a)</td><td>160.46 (n/a)</td><td>150.70 (n/a)</td><td>144.60 (n/a)</td><td>22.82 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.31 <b>(+25.56%)</b></td><td>0.21 (+8.58%)</td><td>0.21 (+13.60%)</td><td>0.12 (-19.00%)</td><td>0.07 <b>(+83.07%)</b></td><td>275.60 <b>(+23.42%)</b></td><td>170.96 (-1.59%)</td><td>154.00 (-11.95%)</td><td>107.30 <b>(-20.34%)</b></td><td>63.87 <b>(+87.00%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>223.30 (n/a)</td><td>173.72 (n/a)</td><td>174.90 (n/a)</td><td>134.70 (n/a)</td><td>34.16 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 (-2.65%)</td><td>0.23 (+16.53%)</td><td>0.23 (+10.95%)</td><td>0.18 <b>(+32.65%)</b></td><td>0.04 <b>(-39.05%)</b></td><td>184.80 <b>(-24.60%)</b></td><td>143.02 (-18.33%)</td><td>139.70 (-9.87%)</td><td>120.80 (+2.72%)</td><td>24.83 <b>(-52.70%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>245.10 (n/a)</td><td>175.12 (n/a)</td><td>155.00 (n/a)</td><td>117.60 (n/a)</td><td>52.51 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 (+4.78%)</td><td>0.21 (+5.65%)</td><td>0.21 (+10.90%)</td><td>0.16 (-11.83%)</td><td>0.04 <b>(+75.46%)</b></td><td>200.80 (+13.38%)</td><td>160.94 (-3.62%)</td><td>157.10 (-9.82%)</td><td>133.10 (-4.52%)</td><td>29.43 <b>(+86.90%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>177.10 (n/a)</td><td>166.98 (n/a)</td><td>174.20 (n/a)</td><td>139.40 (n/a)</td><td>15.75 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 (+5.40%)</td><td>0.20 (+2.26%)</td><td>0.22 (+14.58%)</td><td>0.13 (-18.06%)</td><td>0.05 <b>(+62.03%)</b></td><td>255.50 <b>(+22.02%)</b></td><td>172.48 (+1.87%)</td><td>148.40 (-12.76%)</td><td>132.00 (-5.17%)</td><td>52.09 <b>(+86.93%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>209.40 (n/a)</td><td>169.32 (n/a)</td><td>170.10 (n/a)</td><td>139.20 (n/a)</td><td>27.87 (n/a)</td>
</tr>
</tbody>
</table>


### test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.29 (+6.70%)</td><td>0.21 (+2.80%)</td><td>0.20 (+2.86%)</td><td>0.18 (+4.55%)</td><td>0.04 (+11.48%)</td><td>178.20 (-4.35%)</td><td>158.12 (-2.52%)</td><td>165.10 (-2.77%)</td><td>114.10 (-6.32%)</td><td>25.45 (-2.29%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>186.30 (n/a)</td><td>162.20 (n/a)</td><td>169.80 (n/a)</td><td>121.80 (n/a)</td><td>26.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.23 (-12.45%)</td><td>0.20 (-2.67%)</td><td>0.19 (+1.93%)</td><td>0.17 (-3.74%)</td><td>0.02 <b>(-32.84%)</b></td><td>190.60 (+3.87%)</td><td>164.32 (+1.68%)</td><td>169.40 (-1.85%)</td><td>140.90 (+14.18%)</td><td>19.80 <b>(-21.14%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>183.50 (n/a)</td><td>161.60 (n/a)</td><td>172.60 (n/a)</td><td>123.40 (n/a)</td><td>25.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 <b>(-21.18%)</b></td><td>0.19 (-11.08%)</td><td>0.20 (-1.68%)</td><td>0.15 (+4.64%)</td><td>0.03 <b>(-39.41%)</b></td><td>213.90 (-4.47%)</td><td>178.94 (+9.86%)</td><td>163.50 (+1.74%)</td><td>150.10 <b>(+26.88%)</b></td><td>28.93 <b>(-26.11%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>223.90 (n/a)</td><td>162.88 (n/a)</td><td>160.70 (n/a)</td><td>118.30 (n/a)</td><td>39.15 (n/a)</td>
</tr>
</tbody>
</table>


</details>


<details>
<summary>iron/operators/mha</summary>


### test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.18 (+0.06%)</td><td>0.18 (+0.03%)</td><td>0.18 (+0.01%)</td><td>0.18 (-0.08%)</td><td>0.00 <b>(+36.23%)</b></td><td>47694.40 (+0.08%)</td><td>47534.64 (-0.03%)</td><td>47511.00 (-0.01%)</td><td>47437.30 (-0.06%)</td><td>104.83 <b>(+36.17%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47655.20 (n/a)</td><td>47550.58 (n/a)</td><td>47517.90 (n/a)</td><td>47464.50 (n/a)</td><td>76.99 (n/a)</td>
</tr>
</tbody>
</table>


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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.18 (+0.00%)</td><td>0.18 (+0.04%)</td><td>0.18 (+0.22%)</td><td>0.18 (-0.24%)</td><td>0.00 <b>(+60.43%)</b></td><td>47813.60 (+0.24%)</td><td>47612.50 (-0.04%)</td><td>47565.10 (-0.22%)</td><td>47475.80 (-0.00%)</td><td>147.72 <b>(+60.86%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47700.80 (n/a)</td><td>47633.58 (n/a)</td><td>47667.90 (n/a)</td><td>47475.90 (n/a)</td><td>91.83 (n/a)</td>
</tr>
</tbody>
</table>


### test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (+0.02%)</td><td>0.11 (+0.01%)</td><td>0.11 (-0.01%)</td><td>0.11 (-0.02%)</td><td>0.00 (+15.73%)</td><td>375870.80 (+0.02%)</td><td>375543.56 (-0.01%)</td><td>375548.50 (+0.01%)</td><td>375256.10 (-0.02%)</td><td>233.57 (+15.75%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>375811.40 (n/a)</td><td>375571.50 (n/a)</td><td>375515.70 (n/a)</td><td>375315.20 (n/a)</td><td>201.78 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 <b>(-35.92%)</b></td><td>0.13 <b>(-24.35%)</b></td><td>0.13 <b>(-28.56%)</b></td><td>0.10 (+13.05%)</td><td>0.02 <b>(-67.84%)</b></td><td>238.60 (-11.53%)</td><td>193.02 <b>(+21.87%)</b></td><td>188.60 <b>(+40.01%)</b></td><td>171.50 <b>(+56.05%)</b></td><td>26.78 <b>(-57.99%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>269.70 (n/a)</td><td>158.38 (n/a)</td><td>134.70 (n/a)</td><td>109.90 (n/a)</td><td>63.75 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.29 <b>(-21.75%)</b></td><td>0.27 (-17.80%)</td><td>0.28 (-12.67%)</td><td>0.24 (-17.48%)</td><td>0.02 <b>(-30.22%)</b></td><td>205.80 <b>(+21.20%)</b></td><td>181.88 <b>(+21.43%)</b></td><td>173.90 (+14.48%)</td><td>167.30 <b>(+27.81%)</b></td><td>15.99 (+8.62%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.03 (n/a)</td><td>169.80 (n/a)</td><td>149.78 (n/a)</td><td>151.90 (n/a)</td><td>130.90 (n/a)</td><td>14.72 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>12.96 (-1.66%)</td><td>12.65 (-2.87%)</td><td>12.72 (-2.44%)</td><td>12.31 (-4.56%)</td><td>0.28 <b>(+133.72%)</b></td><td>851.70 (+4.79%)</td><td>829.54 (+2.98%)</td><td>824.30 (+2.50%)</td><td>809.00 (+1.68%)</td><td>18.28 <b>(+148.88%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.18 (n/a)</td><td>13.02 (n/a)</td><td>13.04 (n/a)</td><td>12.90 (n/a)</td><td>0.12 (n/a)</td><td>812.80 (n/a)</td><td>805.50 (n/a)</td><td>804.20 (n/a)</td><td>795.60 (n/a)</td><td>7.34 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.36 (+17.89%)</td><td>0.25 (-3.58%)</td><td>0.25 (-8.67%)</td><td>0.18 (+5.04%)</td><td>0.07 <b>(+23.51%)</b></td><td>224.40 (-4.83%)</td><td>169.22 (+4.33%)</td><td>165.70 (+9.52%)</td><td>113.90 (-15.19%)</td><td>39.85 (-5.18%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>235.80 (n/a)</td><td>162.20 (n/a)</td><td>151.30 (n/a)</td><td>134.30 (n/a)</td><td>42.02 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (-8.74%)</td><td>0.03 (-7.37%)</td><td>0.03 (-10.22%)</td><td>0.02 (+1.43%)</td><td>0.01 (-9.61%)</td><td>238.20 (-1.45%)</td><td>181.64 (+7.21%)</td><td>174.90 (+11.40%)</td><td>145.50 (+9.56%)</td><td>39.37 (-8.04%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>241.70 (n/a)</td><td>169.42 (n/a)</td><td>157.00 (n/a)</td><td>132.80 (n/a)</td><td>42.82 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-17.69%)</td><td>0.02 (-5.08%)</td><td>0.02 (-3.69%)</td><td>0.02 (+6.76%)</td><td>0.00 <b>(-48.43%)</b></td><td>187.40 (-6.35%)</td><td>168.32 (+2.28%)</td><td>172.50 (+3.85%)</td><td>134.40 <b>(+21.52%)</b></td><td>20.31 <b>(-41.48%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>200.10 (n/a)</td><td>164.56 (n/a)</td><td>166.10 (n/a)</td><td>110.60 (n/a)</td><td>34.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 <b>(+41.17%)</b></td><td>0.04 <b>(+27.26%)</b></td><td>0.04 (+5.39%)</td><td>0.03 <b>(+36.38%)</b></td><td>0.01 <b>(+36.63%)</b></td><td>209.40 <b>(-26.68%)</b></td><td>162.08 <b>(-21.47%)</b></td><td>161.70 (-5.11%)</td><td>116.20 <b>(-29.15%)</b></td><td>39.76 <b>(-27.37%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>285.60 (n/a)</td><td>206.40 (n/a)</td><td>170.40 (n/a)</td><td>164.00 (n/a)</td><td>54.74 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+7.52%)</td><td>0.03 (+2.09%)</td><td>0.03 (-2.28%)</td><td>0.02 (+12.80%)</td><td>0.00 (+5.04%)</td><td>178.10 (-11.35%)</td><td>153.90 (-2.27%)</td><td>157.90 (+2.33%)</td><td>118.20 (-7.00%)</td><td>24.37 (-13.87%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.90 (n/a)</td><td>157.48 (n/a)</td><td>154.30 (n/a)</td><td>127.10 (n/a)</td><td>28.29 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 <b>(+24.94%)</b></td><td>0.03 (+14.19%)</td><td>0.03 (+8.49%)</td><td>0.02 (-13.01%)</td><td>0.01 <b>(+151.28%)</b></td><td>222.60 (+14.92%)</td><td>159.26 (-9.48%)</td><td>157.00 (-7.81%)</td><td>125.50 (-19.96%)</td><td>38.37 <b>(+128.55%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.70 (n/a)</td><td>175.94 (n/a)</td><td>170.30 (n/a)</td><td>156.80 (n/a)</td><td>16.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+11.87%)</td><td>0.03 (+19.65%)</td><td>0.02 <b>(+26.39%)</b></td><td>0.02 <b>(+35.09%)</b></td><td>0.00 <b>(-25.93%)</b></td><td>194.20 <b>(-25.96%)</b></td><td>158.60 (-19.31%)</td><td>164.70 <b>(-20.89%)</b></td><td>126.90 (-10.57%)</td><td>26.15 <b>(-49.22%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>262.30 (n/a)</td><td>196.56 (n/a)</td><td>208.20 (n/a)</td><td>141.90 (n/a)</td><td>51.49 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (-10.51%)</td><td>0.03 (-6.83%)</td><td>0.03 (-2.06%)</td><td>0.03 (-9.90%)</td><td>0.01 (+4.51%)</td><td>202.20 (+10.98%)</td><td>168.10 (+8.27%)</td><td>167.90 (+2.07%)</td><td>132.60 (+11.80%)</td><td>33.20 <b>(+31.85%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>182.20 (n/a)</td><td>155.26 (n/a)</td><td>164.50 (n/a)</td><td>118.60 (n/a)</td><td>25.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-0.45%)</td><td>0.03 (+6.18%)</td><td>0.03 (+13.95%)</td><td>0.02 (-0.53%)</td><td>0.01 (-9.24%)</td><td>213.90 (+0.52%)</td><td>164.72 (-6.49%)</td><td>153.70 (-12.22%)</td><td>124.50 (+0.48%)</td><td>33.89 (-9.74%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.80 (n/a)</td><td>176.16 (n/a)</td><td>175.10 (n/a)</td><td>123.90 (n/a)</td><td>37.55 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 <b>(-21.38%)</b></td><td>0.03 (-11.54%)</td><td>0.03 (-17.52%)</td><td>0.02 (+7.61%)</td><td>0.01 <b>(-28.93%)</b></td><td>204.30 (-7.05%)</td><td>168.20 (+10.24%)</td><td>183.00 <b>(+21.27%)</b></td><td>120.70 <b>(+27.19%)</b></td><td>38.52 (-13.87%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>219.80 (n/a)</td><td>152.58 (n/a)</td><td>150.90 (n/a)</td><td>94.90 (n/a)</td><td>44.73 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 <b>(+24.57%)</b></td><td>0.03 (+12.16%)</td><td>0.03 (+19.30%)</td><td>0.02 (+1.47%)</td><td>0.01 <b>(+86.81%)</b></td><td>205.60 (-1.49%)</td><td>161.04 (-7.89%)</td><td>150.60 (-16.19%)</td><td>117.50 (-19.74%)</td><td>40.37 <b>(+55.98%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.70 (n/a)</td><td>174.84 (n/a)</td><td>179.70 (n/a)</td><td>146.40 (n/a)</td><td>25.88 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-4.83%)</td><td>0.02 (-11.16%)</td><td>0.02 (-15.21%)</td><td>0.02 (-11.28%)</td><td>0.00 (+12.44%)</td><td>243.80 (+12.71%)</td><td>201.86 (+13.23%)</td><td>207.80 (+17.93%)</td><td>166.80 (+5.04%)</td><td>30.74 <b>(+31.82%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.30 (n/a)</td><td>178.28 (n/a)</td><td>176.20 (n/a)</td><td>158.80 (n/a)</td><td>23.32 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-4.01%)</td><td>0.03 <b>(+31.60%)</b></td><td>0.03 <b>(+59.13%)</b></td><td>0.02 <b>(+33.90%)</b></td><td>0.01 <b>(-22.31%)</b></td><td>220.90 <b>(-25.35%)</b></td><td>152.28 <b>(-27.19%)</b></td><td>130.00 <b>(-37.17%)</b></td><td>128.80 (+4.21%)</td><td>39.70 <b>(-38.65%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>295.90 (n/a)</td><td>209.16 (n/a)</td><td>206.90 (n/a)</td><td>123.60 (n/a)</td><td>64.71 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+19.97%)</td><td>0.02 (+10.40%)</td><td>0.02 <b>(+20.05%)</b></td><td>0.01 <b>(-23.02%)</b></td><td>0.00 <b>(+230.08%)</b></td><td>317.60 <b>(+29.90%)</b></td><td>214.48 (-5.51%)</td><td>192.80 (-16.68%)</td><td>172.20 (-16.61%)</td><td>58.46 <b>(+278.74%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.50 (n/a)</td><td>226.98 (n/a)</td><td>231.40 (n/a)</td><td>206.50 (n/a)</td><td>15.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+3.24%)</td><td>0.02 (+5.36%)</td><td>0.02 (-0.02%)</td><td>0.02 (+4.24%)</td><td>0.00 (+4.49%)</td><td>207.70 (-4.11%)</td><td>177.94 (-5.12%)</td><td>179.90 (+0.06%)</td><td>150.90 (-3.15%)</td><td>24.06 (-5.81%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>216.60 (n/a)</td><td>187.54 (n/a)</td><td>179.80 (n/a)</td><td>155.80 (n/a)</td><td>25.55 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+12.23%)</td><td>0.02 (+19.07%)</td><td>0.02 <b>(+20.79%)</b></td><td>0.02 <b>(+45.05%)</b></td><td>0.00 <b>(-40.93%)</b></td><td>214.90 <b>(-31.06%)</b></td><td>191.60 (-17.95%)</td><td>189.10 (-17.21%)</td><td>168.30 (-10.91%)</td><td>17.09 <b>(-64.29%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>311.70 (n/a)</td><td>233.52 (n/a)</td><td>228.40 (n/a)</td><td>188.90 (n/a)</td><td>47.85 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.02 (+13.34%)</td><td>0.02 (+18.55%)</td><td>0.02 <b>(+20.14%)</b></td><td>0.02 <b>(+38.76%)</b></td><td>0.00 <b>(-24.20%)</b></td><td>223.90 <b>(-27.91%)</b></td><td>195.40 (-16.99%)</td><td>187.20 (-16.76%)</td><td>170.90 (-11.77%)</td><td>21.10 <b>(-52.88%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>310.60 (n/a)</td><td>235.40 (n/a)</td><td>224.90 (n/a)</td><td>193.70 (n/a)</td><td>44.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (-4.37%)</td><td>0.05 (-8.84%)</td><td>0.05 (-2.72%)</td><td>0.02 <b>(-50.83%)</b></td><td>0.02 <b>(+67.15%)</b></td><td>388.60 <b>(+103.35%)</b></td><td>209.98 <b>(+23.50%)</b></td><td>180.50 (+2.79%)</td><td>129.50 (+4.52%)</td><td>103.65 <b>(+285.16%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.10 (n/a)</td><td>170.02 (n/a)</td><td>175.60 (n/a)</td><td>123.90 (n/a)</td><td>26.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 <b>(+55.30%)</b></td><td>0.08 (+11.31%)</td><td>0.08 (+6.66%)</td><td>0.04 <b>(-33.83%)</b></td><td>0.03 <b>(+347.03%)</b></td><td>298.60 <b>(+51.11%)</b></td><td>170.20 (+0.84%)</td><td>151.30 (-6.26%)</td><td>101.60 <b>(-35.61%)</b></td><td>75.08 <b>(+358.54%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>197.60 (n/a)</td><td>168.78 (n/a)</td><td>161.40 (n/a)</td><td>157.80 (n/a)</td><td>16.37 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 <b>(-24.90%)</b></td><td>0.04 <b>(-23.06%)</b></td><td>0.04 <b>(-25.88%)</b></td><td>0.03 <b>(-28.70%)</b></td><td>0.01 (-8.91%)</td><td>288.90 <b>(+40.24%)</b></td><td>214.36 <b>(+31.85%)</b></td><td>223.10 <b>(+34.97%)</b></td><td>165.10 <b>(+33.15%)</b></td><td>50.72 <b>(+64.89%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.00 (n/a)</td><td>162.58 (n/a)</td><td>165.30 (n/a)</td><td>124.00 (n/a)</td><td>30.76 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.10 <b>(+44.44%)</b></td><td>0.08 <b>(+22.70%)</b></td><td>0.07 (+16.72%)</td><td>0.06 (+8.17%)</td><td>0.01 <b>(+190.81%)</b></td><td>168.90 (-7.50%)</td><td>138.76 (-17.01%)</td><td>142.70 (-14.29%)</td><td>107.30 <b>(-30.73%)</b></td><td>22.39 <b>(+84.71%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>182.60 (n/a)</td><td>167.20 (n/a)</td><td>166.50 (n/a)</td><td>154.90 (n/a)</td><td>12.12 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (-13.46%)</td><td>0.05 (-13.63%)</td><td>0.05 (-11.06%)</td><td>0.04 (-9.91%)</td><td>0.01 <b>(-34.27%)</b></td><td>208.50 (+11.02%)</td><td>168.58 (+14.01%)</td><td>158.20 (+12.44%)</td><td>136.90 (+15.53%)</td><td>27.58 (-13.02%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>147.86 (n/a)</td><td>140.70 (n/a)</td><td>118.50 (n/a)</td><td>31.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.09 (+13.58%)</td><td>0.07 (+8.32%)</td><td>0.07 (+13.66%)</td><td>0.05 (-3.14%)</td><td>0.02 <b>(+59.57%)</b></td><td>196.20 (+3.26%)</td><td>151.16 (-5.42%)</td><td>145.40 (-11.99%)</td><td>112.50 (-11.90%)</td><td>34.72 <b>(+47.25%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>190.00 (n/a)</td><td>159.82 (n/a)</td><td>165.20 (n/a)</td><td>127.70 (n/a)</td><td>23.58 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.05 <b>(-28.64%)</b></td><td>0.04 (-18.21%)</td><td>0.05 (-3.23%)</td><td>0.03 (-10.50%)</td><td>0.01 <b>(-51.11%)</b></td><td>235.60 (+11.71%)</td><td>195.00 (+18.14%)</td><td>176.20 (+3.34%)</td><td>165.50 <b>(+40.14%)</b></td><td>33.03 <b>(-21.99%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.90 (n/a)</td><td>165.06 (n/a)</td><td>170.50 (n/a)</td><td>118.10 (n/a)</td><td>42.35 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (-4.19%)</td><td>0.05 (-11.68%)</td><td>0.05 (-10.60%)</td><td>0.04 <b>(-25.42%)</b></td><td>0.01 <b>(+49.98%)</b></td><td>249.00 <b>(+34.09%)</b></td><td>187.66 (+15.36%)</td><td>177.50 (+11.85%)</td><td>151.90 (+4.40%)</td><td>36.86 <b>(+117.14%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>185.70 (n/a)</td><td>162.68 (n/a)</td><td>158.70 (n/a)</td><td>145.50 (n/a)</td><td>16.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (-7.54%)</td><td>0.05 (+0.56%)</td><td>0.05 (+14.19%)</td><td>0.04 <b>(+25.46%)</b></td><td>0.01 <b>(-54.21%)</b></td><td>190.00 <b>(-20.30%)</b></td><td>172.82 (-5.23%)</td><td>177.80 (-12.41%)</td><td>141.30 (+8.19%)</td><td>19.86 <b>(-58.54%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.40 (n/a)</td><td>182.36 (n/a)</td><td>203.00 (n/a)</td><td>130.60 (n/a)</td><td>47.90 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.07 (-9.22%)</td><td>0.05 (-9.18%)</td><td>0.06 (+2.08%)</td><td>0.02 <b>(-49.38%)</b></td><td>0.02 <b>(+62.58%)</b></td><td>382.90 <b>(+97.57%)</b></td><td>200.94 <b>(+23.17%)</b></td><td>159.40 (-2.03%)</td><td>137.80 (+10.15%)</td><td>102.30 <b>(+286.17%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>163.14 (n/a)</td><td>162.70 (n/a)</td><td>125.10 (n/a)</td><td>26.49 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (-8.41%)</td><td>0.05 (+1.22%)</td><td>0.05 (-3.21%)</td><td>0.04 (+18.79%)</td><td>0.01 <b>(-51.95%)</b></td><td>191.60 (-15.82%)</td><td>171.18 (-4.27%)</td><td>166.40 (+3.29%)</td><td>147.50 (+9.18%)</td><td>17.39 <b>(-56.91%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.60 (n/a)</td><td>178.82 (n/a)</td><td>161.10 (n/a)</td><td>135.10 (n/a)</td><td>40.36 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (+10.89%)</td><td>0.05 (+2.29%)</td><td>0.05 (+8.20%)</td><td>0.04 (-12.35%)</td><td>0.01 <b>(+82.52%)</b></td><td>247.40 (+14.06%)</td><td>192.72 (-0.42%)</td><td>177.00 (-7.57%)</td><td>157.70 (-9.83%)</td><td>36.18 <b>(+91.19%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>216.90 (n/a)</td><td>193.54 (n/a)</td><td>191.50 (n/a)</td><td>174.90 (n/a)</td><td>18.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.06 (-15.55%)</td><td>0.04 (+4.00%)</td><td>0.05 <b>(+22.54%)</b></td><td>0.03 (+11.56%)</td><td>0.01 <b>(-31.81%)</b></td><td>278.20 (-10.37%)</td><td>198.00 (-8.06%)</td><td>172.70 (-18.38%)</td><td>148.90 (+18.46%)</td><td>52.55 <b>(-25.91%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>310.40 (n/a)</td><td>215.36 (n/a)</td><td>211.60 (n/a)</td><td>125.70 (n/a)</td><td>70.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (-9.70%)</td><td>0.04 (-12.38%)</td><td>0.04 (-10.69%)</td><td>0.03 (-18.47%)</td><td>0.00 <b>(+27.60%)</b></td><td>250.80 <b>(+22.64%)</b></td><td>220.24 (+14.55%)</td><td>221.00 (+11.96%)</td><td>195.90 (+10.74%)</td><td>20.50 <b>(+74.24%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.50 (n/a)</td><td>192.26 (n/a)</td><td>197.40 (n/a)</td><td>176.90 (n/a)</td><td>11.76 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.04 (+11.57%)</td><td>0.04 (+4.94%)</td><td>0.04 (-9.78%)</td><td>0.03 <b>(+32.21%)</b></td><td>0.00 <b>(-29.91%)</b></td><td>247.30 <b>(-24.37%)</b></td><td>224.68 (-6.77%)</td><td>232.70 (+10.81%)</td><td>183.20 (-10.37%)</td><td>24.74 <b>(-52.95%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>327.00 (n/a)</td><td>241.00 (n/a)</td><td>210.00 (n/a)</td><td>204.40 (n/a)</td><td>52.58 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (+3.83%)</td><td>0.11 (+3.62%)</td><td>0.11 (+6.53%)</td><td>0.09 (-5.81%)</td><td>0.01 <b>(+31.44%)</b></td><td>191.70 (+6.15%)</td><td>156.84 (-2.87%)</td><td>143.00 (-6.11%)</td><td>139.00 (-3.67%)</td><td>22.56 <b>(+30.68%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>180.60 (n/a)</td><td>161.48 (n/a)</td><td>152.30 (n/a)</td><td>144.30 (n/a)</td><td>17.26 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (-3.39%)</td><td>0.15 (-10.63%)</td><td>0.15 (-4.18%)</td><td>0.11 <b>(-21.20%)</b></td><td>0.03 <b>(+66.84%)</b></td><td>214.60 <b>(+26.91%)</b></td><td>171.64 (+15.01%)</td><td>160.50 (+4.36%)</td><td>129.50 (+3.52%)</td><td>37.06 <b>(+129.14%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>169.10 (n/a)</td><td>149.24 (n/a)</td><td>153.80 (n/a)</td><td>125.10 (n/a)</td><td>16.17 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 <b>(+41.13%)</b></td><td>0.11 (+15.44%)</td><td>0.10 (+6.89%)</td><td>0.08 (-6.94%)</td><td>0.03 <b>(+312.98%)</b></td><td>204.50 (+7.46%)</td><td>156.54 (-9.85%)</td><td>164.00 (-6.45%)</td><td>113.10 <b>(-29.14%)</b></td><td>35.80 <b>(+209.67%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.30 (n/a)</td><td>173.64 (n/a)</td><td>175.30 (n/a)</td><td>159.60 (n/a)</td><td>11.56 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 (-1.77%)</td><td>0.12 (-10.80%)</td><td>0.11 (-16.06%)</td><td>0.09 (-17.53%)</td><td>0.03 <b>(+31.60%)</b></td><td>215.70 <b>(+21.25%)</b></td><td>175.46 (+14.53%)</td><td>190.20 (+19.17%)</td><td>123.10 (+1.82%)</td><td>37.09 <b>(+61.26%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>177.90 (n/a)</td><td>153.20 (n/a)</td><td>159.60 (n/a)</td><td>120.90 (n/a)</td><td>23.00 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (+5.18%)</td><td>0.10 (+14.00%)</td><td>0.09 (+9.77%)</td><td>0.08 <b>(+52.18%)</b></td><td>0.02 <b>(-23.72%)</b></td><td>211.50 <b>(-34.28%)</b></td><td>174.48 (-15.91%)</td><td>174.60 (-8.92%)</td><td>140.20 (-4.88%)</td><td>29.64 <b>(-55.45%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>321.80 (n/a)</td><td>207.50 (n/a)</td><td>191.70 (n/a)</td><td>147.40 (n/a)</td><td>66.52 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (-2.12%)</td><td>0.13 (+5.73%)</td><td>0.13 (+0.92%)</td><td>0.10 (+0.55%)</td><td>0.02 (-19.50%)</td><td>207.90 (-0.57%)</td><td>159.78 (-6.52%)</td><td>153.90 (-0.97%)</td><td>133.00 (+2.23%)</td><td>28.41 (-18.94%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>209.10 (n/a)</td><td>170.92 (n/a)</td><td>155.40 (n/a)</td><td>130.10 (n/a)</td><td>35.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 <b>(+27.73%)</b></td><td>0.11 (+12.85%)</td><td>0.10 (+6.51%)</td><td>0.09 (+6.48%)</td><td>0.02 <b>(+116.62%)</b></td><td>185.10 (-6.09%)</td><td>156.80 (-10.44%)</td><td>159.70 (-6.11%)</td><td>126.50 <b>(-21.72%)</b></td><td>21.20 <b>(+55.50%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>197.10 (n/a)</td><td>175.08 (n/a)</td><td>170.10 (n/a)</td><td>161.60 (n/a)</td><td>13.64 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (-2.77%)</td><td>0.11 (-7.50%)</td><td>0.12 (-0.97%)</td><td>0.08 <b>(-21.33%)</b></td><td>0.03 <b>(+38.74%)</b></td><td>226.20 <b>(+27.15%)</b></td><td>170.82 (+11.94%)</td><td>155.90 (+0.97%)</td><td>123.70 (+2.91%)</td><td>46.45 <b>(+81.82%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>177.90 (n/a)</td><td>152.60 (n/a)</td><td>154.40 (n/a)</td><td>120.20 (n/a)</td><td>25.55 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 <b>(+30.89%)</b></td><td>0.12 <b>(+23.83%)</b></td><td>0.12 (+16.41%)</td><td>0.10 <b>(+38.65%)</b></td><td>0.02 <b>(+39.77%)</b></td><td>166.20 <b>(-27.90%)</b></td><td>139.34 (-19.10%)</td><td>138.60 (-14.13%)</td><td>109.50 <b>(-23.59%)</b></td><td>26.23 <b>(-23.67%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>230.50 (n/a)</td><td>172.24 (n/a)</td><td>161.40 (n/a)</td><td>143.30 (n/a)</td><td>34.37 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (-18.39%)</td><td>0.11 (-7.54%)</td><td>0.11 (-3.77%)</td><td>0.10 (-7.80%)</td><td>0.01 <b>(-42.63%)</b></td><td>190.70 (+8.48%)</td><td>169.52 (+7.37%)</td><td>163.90 (+3.93%)</td><td>156.80 <b>(+22.50%)</b></td><td>14.72 <b>(-24.36%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>175.80 (n/a)</td><td>157.88 (n/a)</td><td>157.70 (n/a)</td><td>128.00 (n/a)</td><td>19.46 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 <b>(+35.75%)</b></td><td>0.11 <b>(+22.24%)</b></td><td>0.11 <b>(+20.38%)</b></td><td>0.09 (+7.89%)</td><td>0.02 <b>(+165.32%)</b></td><td>189.50 (-7.33%)</td><td>156.62 (-16.67%)</td><td>155.00 (-16.93%)</td><td>122.40 <b>(-26.35%)</b></td><td>26.41 <b>(+82.62%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>187.96 (n/a)</td><td>186.60 (n/a)</td><td>166.20 (n/a)</td><td>14.46 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (-19.81%)</td><td>0.08 (-9.89%)</td><td>0.09 (-1.55%)</td><td>0.06 (+13.93%)</td><td>0.02 <b>(-36.66%)</b></td><td>302.00 (-12.23%)</td><td>214.96 (+4.89%)</td><td>189.00 (+1.61%)</td><td>163.40 <b>(+24.73%)</b></td><td>55.03 <b>(-32.99%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>344.10 (n/a)</td><td>204.94 (n/a)</td><td>186.00 (n/a)</td><td>131.00 (n/a)</td><td>82.13 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (+14.86%)</td><td>0.10 (+14.21%)</td><td>0.10 (+18.92%)</td><td>0.08 (-0.93%)</td><td>0.01 <b>(+50.74%)</b></td><td>213.00 (+0.95%)</td><td>166.86 (-11.56%)</td><td>163.00 (-15.89%)</td><td>138.60 (-12.94%)</td><td>27.73 <b>(+37.54%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.00 (n/a)</td><td>188.66 (n/a)</td><td>193.80 (n/a)</td><td>159.20 (n/a)</td><td>20.16 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 <b>(-30.70%)</b></td><td>0.10 (-12.34%)</td><td>0.10 (-12.06%)</td><td>0.09 (+11.69%)</td><td>0.01 <b>(-75.52%)</b></td><td>189.50 (-10.49%)</td><td>176.64 (+9.19%)</td><td>175.00 (+13.71%)</td><td>158.70 <b>(+44.27%)</b></td><td>12.16 <b>(-67.93%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>211.70 (n/a)</td><td>161.78 (n/a)</td><td>153.90 (n/a)</td><td>110.00 (n/a)</td><td>37.93 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.11 (+17.26%)</td><td>0.09 <b>(+22.50%)</b></td><td>0.09 (+11.40%)</td><td>0.08 <b>(+54.24%)</b></td><td>0.01 <b>(-25.06%)</b></td><td>216.70 <b>(-35.16%)</b></td><td>179.00 <b>(-21.13%)</b></td><td>178.50 (-10.21%)</td><td>151.20 (-14.72%)</td><td>25.28 <b>(-59.86%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>334.20 (n/a)</td><td>226.96 (n/a)</td><td>198.80 (n/a)</td><td>177.30 (n/a)</td><td>62.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.24 <b>(+26.07%)</b></td><td>0.20 (+13.68%)</td><td>0.19 (+4.38%)</td><td>0.17 (+11.77%)</td><td>0.03 <b>(+82.67%)</b></td><td>198.20 (-10.56%)</td><td>165.82 (-11.09%)</td><td>172.50 (-4.22%)</td><td>133.90 <b>(-20.68%)</b></td><td>25.42 <b>(+24.94%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.60 (n/a)</td><td>186.50 (n/a)</td><td>180.10 (n/a)</td><td>168.80 (n/a)</td><td>20.34 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (+0.22%)</td><td>0.22 <b>(+21.28%)</b></td><td>0.21 <b>(+28.87%)</b></td><td>0.17 <b>(+65.85%)</b></td><td>0.03 <b>(-45.00%)</b></td><td>187.30 <b>(-39.72%)</b></td><td>154.14 <b>(-23.87%)</b></td><td>158.80 <b>(-22.39%)</b></td><td>125.90 (-0.24%)</td><td>24.03 <b>(-66.74%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>310.70 (n/a)</td><td>202.46 (n/a)</td><td>204.60 (n/a)</td><td>126.20 (n/a)</td><td>72.26 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.33 (-1.52%)</td><td>0.24 (-1.71%)</td><td>0.25 (+12.70%)</td><td>0.13 <b>(-34.16%)</b></td><td>0.07 <b>(+31.39%)</b></td><td>307.40 <b>(+51.88%)</b></td><td>189.26 (+7.47%)</td><td>166.40 (-11.25%)</td><td>125.60 (+1.54%)</td><td>69.68 <b>(+117.36%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.05 (n/a)</td><td>202.40 (n/a)</td><td>176.10 (n/a)</td><td>187.50 (n/a)</td><td>123.70 (n/a)</td><td>32.06 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 <b>(+36.99%)</b></td><td>0.22 <b>(+38.05%)</b></td><td>0.22 <b>(+31.94%)</b></td><td>0.16 <b>(+60.32%)</b></td><td>0.04 (+15.22%)</td><td>200.00 <b>(-37.62%)</b></td><td>150.32 <b>(-29.13%)</b></td><td>149.30 <b>(-24.21%)</b></td><td>123.40 <b>(-26.98%)</b></td><td>30.92 <b>(-50.06%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>320.60 (n/a)</td><td>212.12 (n/a)</td><td>197.00 (n/a)</td><td>169.00 (n/a)</td><td>61.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.32 (+17.53%)</td><td>0.28 (+13.54%)</td><td>0.30 <b>(+24.29%)</b></td><td>0.18 <b>(-20.17%)</b></td><td>0.06 <b>(+145.48%)</b></td><td>232.80 <b>(+25.23%)</b></td><td>156.02 (-8.40%)</td><td>138.80 (-19.54%)</td><td>128.60 (-14.95%)</td><td>43.24 <b>(+171.14%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>185.90 (n/a)</td><td>170.32 (n/a)</td><td>172.50 (n/a)</td><td>151.20 (n/a)</td><td>15.95 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.33 <b>(+42.67%)</b></td><td>0.22 <b>(+29.94%)</b></td><td>0.22 <b>(+48.21%)</b></td><td>0.15 (+1.51%)</td><td>0.07 <b>(+98.76%)</b></td><td>218.50 (-1.49%)</td><td>160.90 (-19.12%)</td><td>148.00 <b>(-32.51%)</b></td><td>98.90 <b>(-29.91%)</b></td><td>48.56 <b>(+39.81%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>221.80 (n/a)</td><td>198.94 (n/a)</td><td>219.30 (n/a)</td><td>141.10 (n/a)</td><td>34.73 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.29 <b>(-21.66%)</b></td><td>0.24 (-2.42%)</td><td>0.22 (-2.88%)</td><td>0.19 (+1.51%)</td><td>0.05 <b>(-38.50%)</b></td><td>197.40 (-1.50%)</td><td>161.10 (-0.52%)</td><td>171.20 (+2.95%)</td><td>126.80 <b>(+27.69%)</b></td><td>30.32 <b>(-20.89%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.37 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>200.40 (n/a)</td><td>161.94 (n/a)</td><td>166.30 (n/a)</td><td>99.30 (n/a)</td><td>38.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.28 (+7.01%)</td><td>0.23 (+16.05%)</td><td>0.25 <b>(+30.17%)</b></td><td>0.18 (+6.09%)</td><td>0.04 (+12.89%)</td><td>185.70 (-5.74%)</td><td>144.30 (-13.51%)</td><td>128.90 <b>(-23.18%)</b></td><td>117.00 (-6.55%)</td><td>28.42 (+1.10%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>197.00 (n/a)</td><td>166.84 (n/a)</td><td>167.80 (n/a)</td><td>125.20 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.24 (-7.57%)</td><td>0.21 (-5.40%)</td><td>0.21 (-8.29%)</td><td>0.17 (-4.54%)</td><td>0.03 <b>(-22.36%)</b></td><td>218.30 (+4.75%)</td><td>178.74 (+5.13%)</td><td>174.30 (+9.07%)</td><td>154.10 (+8.22%)</td><td>23.80 (-10.52%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>208.40 (n/a)</td><td>170.02 (n/a)</td><td>159.80 (n/a)</td><td>142.40 (n/a)</td><td>26.60 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 <b>(+26.53%)</b></td><td>0.21 <b>(+20.56%)</b></td><td>0.21 (+16.91%)</td><td>0.16 (+15.55%)</td><td>0.04 <b>(+50.12%)</b></td><td>205.30 (-13.49%)</td><td>159.14 (-16.08%)</td><td>152.60 (-14.46%)</td><td>120.30 <b>(-21.01%)</b></td><td>33.14 (+2.18%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>237.30 (n/a)</td><td>189.64 (n/a)</td><td>178.40 (n/a)</td><td>152.30 (n/a)</td><td>32.43 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.36 <b>(+65.32%)</b></td><td>0.21 (+14.16%)</td><td>0.20 (+4.32%)</td><td>0.11 (-6.94%)</td><td>0.10 <b>(+126.45%)</b></td><td>327.00 (+7.46%)</td><td>194.58 (-2.95%)</td><td>175.20 (-4.16%)</td><td>95.40 <b>(-39.51%)</b></td><td>85.46 <b>(+42.27%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>304.30 (n/a)</td><td>200.50 (n/a)</td><td>182.80 (n/a)</td><td>157.70 (n/a)</td><td>60.07 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.34 <b>(+37.77%)</b></td><td>0.21 (-3.48%)</td><td>0.21 (-1.23%)</td><td>0.15 <b>(-27.36%)</b></td><td>0.08 <b>(+287.24%)</b></td><td>224.20 <b>(+37.63%)</b></td><td>170.58 (+12.80%)</td><td>158.90 (+1.27%)</td><td>97.40 <b>(-27.42%)</b></td><td>52.68 <b>(+293.70%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>162.90 (n/a)</td><td>151.22 (n/a)</td><td>156.90 (n/a)</td><td>134.20 (n/a)</td><td>13.38 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 (-0.68%)</td><td>0.18 (+4.24%)</td><td>0.17 (-12.26%)</td><td>0.15 <b>(+46.89%)</b></td><td>0.03 <b>(-39.96%)</b></td><td>230.40 <b>(-31.94%)</b></td><td>195.38 (-9.25%)</td><td>200.70 (+13.97%)</td><td>161.30 (+0.69%)</td><td>29.34 <b>(-60.05%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>338.50 (n/a)</td><td>215.30 (n/a)</td><td>176.10 (n/a)</td><td>160.20 (n/a)</td><td>73.45 (n/a)</td>
</tr>
</tbody>
</table>


### test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.18 (-18.03%)</td><td>0.16 (-5.09%)</td><td>0.17 (+10.02%)</td><td>0.10 <b>(-23.61%)</b></td><td>0.03 (-0.95%)</td><td>325.00 <b>(+30.89%)</b></td><td>217.00 (+7.40%)</td><td>187.70 (-9.10%)</td><td>178.70 <b>(+21.98%)</b></td><td>62.08 <b>(+63.08%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>248.30 (n/a)</td><td>202.04 (n/a)</td><td>206.50 (n/a)</td><td>146.50 (n/a)</td><td>38.07 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 <b>(+25.35%)</b></td><td>0.15 (+19.09%)</td><td>0.14 (+14.27%)</td><td>0.13 <b>(+20.03%)</b></td><td>0.02 <b>(+33.56%)</b></td><td>156.40 (-16.72%)</td><td>140.94 (-15.90%)</td><td>148.50 (-12.44%)</td><td>118.90 <b>(-20.25%)</b></td><td>15.62 (-10.22%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>167.58 (n/a)</td><td>169.60 (n/a)</td><td>149.10 (n/a)</td><td>17.40 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 (+13.56%)</td><td>0.13 (+18.30%)</td><td>0.14 (+15.33%)</td><td>0.11 <b>(+27.48%)</b></td><td>0.02 (-0.83%)</td><td>184.40 <b>(-21.57%)</b></td><td>156.10 (-16.22%)</td><td>150.40 (-13.31%)</td><td>128.70 (-11.91%)</td><td>24.55 <b>(-31.23%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>235.10 (n/a)</td><td>186.32 (n/a)</td><td>173.50 (n/a)</td><td>146.10 (n/a)</td><td>35.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 <b>(+23.29%)</b></td><td>0.14 (+14.15%)</td><td>0.13 (+12.91%)</td><td>0.10 (-8.66%)</td><td>0.03 <b>(+130.23%)</b></td><td>205.70 (+9.47%)</td><td>156.36 (-9.76%)</td><td>157.20 (-11.44%)</td><td>119.30 (-18.90%)</td><td>34.44 <b>(+100.55%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>187.90 (n/a)</td><td>173.28 (n/a)</td><td>177.50 (n/a)</td><td>147.10 (n/a)</td><td>17.17 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 <b>(+35.54%)</b></td><td>0.13 (+15.57%)</td><td>0.13 (+13.77%)</td><td>0.10 (+2.53%)</td><td>0.02 <b>(+167.59%)</b></td><td>205.40 (-2.47%)</td><td>165.40 (-11.88%)</td><td>158.80 (-12.12%)</td><td>130.30 <b>(-26.22%)</b></td><td>27.95 <b>(+94.08%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>210.60 (n/a)</td><td>187.70 (n/a)</td><td>180.70 (n/a)</td><td>176.60 (n/a)</td><td>14.40 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 (+0.25%)</td><td>0.15 (-2.05%)</td><td>0.14 (-5.66%)</td><td>0.13 (+6.34%)</td><td>0.02 (+2.95%)</td><td>157.90 (-5.96%)</td><td>141.20 (+2.07%)</td><td>143.70 (+5.97%)</td><td>122.60 (-0.24%)</td><td>17.24 (-3.98%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>167.90 (n/a)</td><td>138.34 (n/a)</td><td>135.60 (n/a)</td><td>122.90 (n/a)</td><td>17.96 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 (+1.07%)</td><td>0.13 (-10.32%)</td><td>0.13 (-8.02%)</td><td>0.10 (-19.03%)</td><td>0.03 <b>(+64.45%)</b></td><td>211.40 <b>(+23.48%)</b></td><td>163.78 (+14.28%)</td><td>154.70 (+8.71%)</td><td>125.90 (-1.02%)</td><td>34.95 <b>(+101.44%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>171.20 (n/a)</td><td>143.32 (n/a)</td><td>142.30 (n/a)</td><td>127.20 (n/a)</td><td>17.35 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.12 (-10.91%)</td><td>0.10 (-6.50%)</td><td>0.10 (-7.80%)</td><td>0.09 (-3.93%)</td><td>0.01 <b>(-38.76%)</b></td><td>218.10 (+4.06%)</td><td>196.54 (+6.32%)</td><td>196.70 (+8.43%)</td><td>177.80 (+12.25%)</td><td>14.80 <b>(-28.91%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>209.60 (n/a)</td><td>184.86 (n/a)</td><td>181.40 (n/a)</td><td>158.40 (n/a)</td><td>20.81 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (-4.87%)</td><td>0.11 (-5.68%)</td><td>0.11 (-6.42%)</td><td>0.10 (-3.47%)</td><td>0.01 (-2.18%)</td><td>206.10 (+3.57%)</td><td>182.12 (+6.06%)</td><td>185.80 (+6.90%)</td><td>162.40 (+5.11%)</td><td>19.28 (+5.60%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>199.00 (n/a)</td><td>171.72 (n/a)</td><td>173.80 (n/a)</td><td>154.50 (n/a)</td><td>18.26 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.22 <b>(+23.54%)</b></td><td>0.16 (+4.04%)</td><td>0.14 (-3.46%)</td><td>0.13 (-4.27%)</td><td>0.04 <b>(+111.08%)</b></td><td>191.10 (+4.43%)</td><td>164.50 (-0.90%)</td><td>172.00 (+3.55%)</td><td>109.80 (-19.03%)</td><td>33.47 <b>(+78.27%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>183.00 (n/a)</td><td>166.00 (n/a)</td><td>166.10 (n/a)</td><td>135.60 (n/a)</td><td>18.77 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.20 (+17.44%)</td><td>0.16 (+16.07%)</td><td>0.17 (+17.42%)</td><td>0.12 (+1.46%)</td><td>0.04 <b>(+67.63%)</b></td><td>211.90 (-1.44%)</td><td>156.58 (-11.79%)</td><td>146.10 (-14.81%)</td><td>123.50 (-14.83%)</td><td>37.33 <b>(+37.06%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>215.00 (n/a)</td><td>177.50 (n/a)</td><td>171.50 (n/a)</td><td>145.00 (n/a)</td><td>27.24 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (+4.15%)</td><td>0.15 (+1.88%)</td><td>0.16 (+10.45%)</td><td>0.11 (+8.85%)</td><td>0.04 (+13.63%)</td><td>219.60 (-8.12%)</td><td>168.68 (-1.25%)</td><td>151.70 (-9.49%)</td><td>128.70 (-4.03%)</td><td>41.63 (+0.65%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>239.00 (n/a)</td><td>170.82 (n/a)</td><td>167.60 (n/a)</td><td>134.10 (n/a)</td><td>41.36 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.20 (-13.32%)</td><td>0.14 <b>(-23.24%)</b></td><td>0.11 <b>(-33.13%)</b></td><td>0.10 <b>(-30.96%)</b></td><td>0.04 <b>(+22.42%)</b></td><td>250.50 <b>(+44.88%)</b></td><td>192.40 <b>(+35.51%)</b></td><td>215.60 <b>(+49.51%)</b></td><td>122.60 (+15.44%)</td><td>51.39 <b>(+104.42%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>172.90 (n/a)</td><td>141.98 (n/a)</td><td>144.20 (n/a)</td><td>106.20 (n/a)</td><td>25.14 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.20 (+16.42%)</td><td>0.16 <b>(+25.32%)</b></td><td>0.16 (+7.16%)</td><td>0.14 <b>(+103.40%)</b></td><td>0.02 <b>(-44.28%)</b></td><td>181.00 <b>(-50.83%)</b></td><td>153.02 <b>(-28.23%)</b></td><td>156.30 (-6.69%)</td><td>121.50 (-14.13%)</td><td>21.59 <b>(-77.01%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>368.10 (n/a)</td><td>213.22 (n/a)</td><td>167.50 (n/a)</td><td>141.50 (n/a)</td><td>93.94 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.20 (-7.97%)</td><td>0.15 (-9.45%)</td><td>0.12 (-11.62%)</td><td>0.12 (-5.37%)</td><td>0.03 (-13.17%)</td><td>208.70 (+5.67%)</td><td>176.04 (+9.82%)</td><td>197.60 (+13.11%)</td><td>123.90 (+8.68%)</td><td>36.72 (+0.78%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>197.50 (n/a)</td><td>160.30 (n/a)</td><td>174.70 (n/a)</td><td>114.00 (n/a)</td><td>36.44 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.19 (+2.46%)</td><td>0.14 (+5.66%)</td><td>0.14 (+13.24%)</td><td>0.11 (-1.76%)</td><td>0.03 (+6.39%)</td><td>223.10 (+1.78%)</td><td>176.46 (-4.88%)</td><td>170.70 (-11.69%)</td><td>126.90 (-2.38%)</td><td>37.80 (+8.72%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>219.20 (n/a)</td><td>185.52 (n/a)</td><td>193.30 (n/a)</td><td>130.00 (n/a)</td><td>34.77 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (-1.92%)</td><td>0.13 (+2.63%)</td><td>0.12 (+4.02%)</td><td>0.12 (+2.94%)</td><td>0.01 (-17.75%)</td><td>212.20 (-2.88%)</td><td>197.20 (-2.85%)</td><td>205.10 (-3.84%)</td><td>172.60 (+1.95%)</td><td>16.61 (-17.96%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>218.50 (n/a)</td><td>202.98 (n/a)</td><td>213.30 (n/a)</td><td>169.30 (n/a)</td><td>20.25 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (-12.94%)</td><td>0.13 (+10.43%)</td><td>0.13 (+8.96%)</td><td>0.12 <b>(+48.62%)</b></td><td>0.01 <b>(-81.75%)</b></td><td>155.20 <b>(-32.73%)</b></td><td>146.48 (-14.36%)</td><td>146.60 (-8.20%)</td><td>137.90 (+14.92%)</td><td>6.36 <b>(-86.14%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>230.70 (n/a)</td><td>171.04 (n/a)</td><td>159.70 (n/a)</td><td>120.00 (n/a)</td><td>45.89 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.17 (-7.71%)</td><td>0.13 (+15.81%)</td><td>0.12 (+13.84%)</td><td>0.10 <b>(+22.53%)</b></td><td>0.03 <b>(-22.01%)</b></td><td>183.50 (-18.41%)</td><td>146.18 (-16.52%)</td><td>159.10 (-12.15%)</td><td>106.00 (+8.38%)</td><td>34.16 <b>(-27.45%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>224.90 (n/a)</td><td>175.10 (n/a)</td><td>181.10 (n/a)</td><td>97.80 (n/a)</td><td>47.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.14 (+7.58%)</td><td>0.13 (+13.14%)</td><td>0.13 (+12.38%)</td><td>0.11 <b>(+23.68%)</b></td><td>0.02 <b>(-21.43%)</b></td><td>167.60 (-19.15%)</td><td>147.44 (-12.81%)</td><td>143.30 (-11.05%)</td><td>128.30 (-7.03%)</td><td>18.25 <b>(-40.51%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>207.30 (n/a)</td><td>169.10 (n/a)</td><td>161.10 (n/a)</td><td>138.00 (n/a)</td><td>30.68 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.15 (+0.87%)</td><td>0.13 (+17.00%)</td><td>0.14 <b>(+39.74%)</b></td><td>0.11 <b>(+20.47%)</b></td><td>0.02 (-13.59%)</td><td>172.90 (-17.03%)</td><td>144.08 (-15.48%)</td><td>129.30 <b>(-28.41%)</b></td><td>126.10 (-0.86%)</td><td>22.54 <b>(-28.55%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>208.40 (n/a)</td><td>170.46 (n/a)</td><td>180.60 (n/a)</td><td>127.20 (n/a)</td><td>31.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.16 <b>(+38.38%)</b></td><td>0.13 <b>(+25.15%)</b></td><td>0.12 (+18.18%)</td><td>0.11 <b>(+45.97%)</b></td><td>0.02 <b>(+26.27%)</b></td><td>162.00 <b>(-31.50%)</b></td><td>149.02 <b>(-20.45%)</b></td><td>156.40 (-15.37%)</td><td>114.90 <b>(-27.74%)</b></td><td>19.27 <b>(-38.43%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>236.50 (n/a)</td><td>187.32 (n/a)</td><td>184.80 (n/a)</td><td>159.00 (n/a)</td><td>31.29 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (-6.80%)</td><td>0.10 (-8.35%)</td><td>0.10 (-10.02%)</td><td>0.08 (-10.28%)</td><td>0.02 (-3.88%)</td><td>237.70 (+11.44%)</td><td>188.82 (+9.36%)</td><td>192.10 (+11.10%)</td><td>145.70 (+7.29%)</td><td>33.98 (+14.83%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>213.30 (n/a)</td><td>172.66 (n/a)</td><td>172.90 (n/a)</td><td>135.80 (n/a)</td><td>29.59 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (+15.78%)</td><td>0.11 (+6.52%)</td><td>0.11 (-0.01%)</td><td>0.08 (-5.95%)</td><td>0.02 <b>(+67.20%)</b></td><td>221.10 (+6.30%)</td><td>174.16 (-4.49%)</td><td>167.60 (+0.00%)</td><td>142.00 (-13.63%)</td><td>33.84 <b>(+50.34%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>182.34 (n/a)</td><td>167.60 (n/a)</td><td>164.40 (n/a)</td><td>22.51 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (-5.28%)</td><td>0.11 (+9.51%)</td><td>0.11 (+13.94%)</td><td>0.09 <b>(+23.29%)</b></td><td>0.02 <b>(-33.99%)</b></td><td>197.60 (-18.88%)</td><td>166.16 (-10.84%)</td><td>169.70 (-12.21%)</td><td>141.70 (+5.59%)</td><td>22.75 <b>(-43.78%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>243.60 (n/a)</td><td>186.36 (n/a)</td><td>193.30 (n/a)</td><td>134.20 (n/a)</td><td>40.46 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.79 (+0.30%)</td><td>0.67 (+11.09%)</td><td>0.71 <b>(+21.40%)</b></td><td>0.48 (+6.79%)</td><td>0.12 (-3.92%)</td><td>202.90 (-6.37%)</td><td>152.34 (-10.34%)</td><td>138.20 (-17.64%)</td><td>123.70 (-0.32%)</td><td>31.70 (-8.34%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.79 (n/a)</td><td>0.60 (n/a)</td><td>0.59 (n/a)</td><td>0.45 (n/a)</td><td>0.13 (n/a)</td><td>216.70 (n/a)</td><td>169.90 (n/a)</td><td>167.80 (n/a)</td><td>124.10 (n/a)</td><td>34.58 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.72 (-2.90%)</td><td>0.59 (+5.06%)</td><td>0.60 (+9.30%)</td><td>0.46 (+10.88%)</td><td>0.10 (-19.27%)</td><td>216.00 (-9.81%)</td><td>170.34 (-6.17%)</td><td>164.50 (-8.51%)</td><td>136.00 (+2.95%)</td><td>29.99 <b>(-24.02%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.74 (n/a)</td><td>0.56 (n/a)</td><td>0.55 (n/a)</td><td>0.41 (n/a)</td><td>0.12 (n/a)</td><td>239.50 (n/a)</td><td>181.54 (n/a)</td><td>179.80 (n/a)</td><td>132.10 (n/a)</td><td>39.47 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.68 (-11.29%)</td><td>0.59 (-2.55%)</td><td>0.63 (+4.83%)</td><td>0.48 (+18.66%)</td><td>0.09 <b>(-46.11%)</b></td><td>205.30 (-15.72%)</td><td>168.32 (-1.67%)</td><td>154.90 (-4.56%)</td><td>143.60 (+12.72%)</td><td>26.10 <b>(-46.66%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.77 (n/a)</td><td>0.61 (n/a)</td><td>0.61 (n/a)</td><td>0.40 (n/a)</td><td>0.16 (n/a)</td><td>243.60 (n/a)</td><td>171.18 (n/a)</td><td>162.30 (n/a)</td><td>127.40 (n/a)</td><td>48.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.97 <b>(+58.05%)</b></td><td>0.63 <b>(+31.87%)</b></td><td>0.64 <b>(+27.63%)</b></td><td>0.36 (+12.48%)</td><td>0.26 <b>(+136.99%)</b></td><td>270.70 (-11.07%)</td><td>181.72 (-16.13%)</td><td>154.50 <b>(-21.65%)</b></td><td>101.60 <b>(-36.74%)</b></td><td>77.56 <b>(+38.91%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.61 (n/a)</td><td>0.48 (n/a)</td><td>0.50 (n/a)</td><td>0.32 (n/a)</td><td>0.11 (n/a)</td><td>304.40 (n/a)</td><td>216.66 (n/a)</td><td>197.20 (n/a)</td><td>160.60 (n/a)</td><td>55.84 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.60 <b>(+33.01%)</b></td><td>0.49 (+15.68%)</td><td>0.49 (+15.28%)</td><td>0.42 (+0.74%)</td><td>0.07 <b>(+403.98%)</b></td><td>176.30 (-0.73%)</td><td>151.66 (-12.24%)</td><td>151.40 (-13.29%)</td><td>123.10 <b>(-24.85%)</b></td><td>21.08 <b>(+277.92%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.45 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>0.01 (n/a)</td><td>177.60 (n/a)</td><td>172.82 (n/a)</td><td>174.60 (n/a)</td><td>163.80 (n/a)</td><td>5.58 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.59 (+0.42%)</td><td>0.47 <b>(+26.15%)</b></td><td>0.42 <b>(+25.12%)</b></td><td>0.39 <b>(+59.22%)</b></td><td>0.10 <b>(-29.68%)</b></td><td>188.40 <b>(-37.18%)</b></td><td>160.80 <b>(-25.47%)</b></td><td>174.00 <b>(-20.04%)</b></td><td>124.90 (-0.48%)</td><td>30.37 <b>(-55.47%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.59 (n/a)</td><td>0.37 (n/a)</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.14 (n/a)</td><td>299.90 (n/a)</td><td>215.74 (n/a)</td><td>217.60 (n/a)</td><td>125.50 (n/a)</td><td>68.21 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.51 <b>(-20.86%)</b></td><td>0.44 (-17.31%)</td><td>0.45 <b>(-24.89%)</b></td><td>0.33 (-12.92%)</td><td>0.07 <b>(-42.41%)</b></td><td>225.40 (+14.82%)</td><td>172.30 (+17.79%)</td><td>163.70 <b>(+33.20%)</b></td><td>145.60 <b>(+26.28%)</b></td><td>32.58 (-15.50%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.64 (n/a)</td><td>0.53 (n/a)</td><td>0.60 (n/a)</td><td>0.38 (n/a)</td><td>0.13 (n/a)</td><td>196.30 (n/a)</td><td>146.28 (n/a)</td><td>122.90 (n/a)</td><td>115.30 (n/a)</td><td>38.56 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.46 <b>(-23.87%)</b></td><td>0.39 (-16.25%)</td><td>0.41 (-8.55%)</td><td>0.29 <b>(-21.61%)</b></td><td>0.06 <b>(-24.90%)</b></td><td>257.10 <b>(+27.59%)</b></td><td>195.52 (+19.41%)</td><td>181.70 (+9.33%)</td><td>161.20 <b>(+31.38%)</b></td><td>37.21 <b>(+32.28%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.60 (n/a)</td><td>0.46 (n/a)</td><td>0.44 (n/a)</td><td>0.37 (n/a)</td><td>0.09 (n/a)</td><td>201.50 (n/a)</td><td>163.74 (n/a)</td><td>166.20 (n/a)</td><td>122.70 (n/a)</td><td>28.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.32 (+17.53%)</td><td>0.27 <b>(+21.77%)</b></td><td>0.27 <b>(+22.56%)</b></td><td>0.19 (+1.61%)</td><td>0.05 <b>(+32.52%)</b></td><td>199.00 (-1.58%)</td><td>142.66 (-16.99%)</td><td>136.30 (-18.43%)</td><td>116.80 (-14.93%)</td><td>32.66 (+11.49%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>202.20 (n/a)</td><td>171.86 (n/a)</td><td>167.10 (n/a)</td><td>137.30 (n/a)</td><td>29.30 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 <b>(+27.97%)</b></td><td>0.24 <b>(+29.43%)</b></td><td>0.24 <b>(+32.92%)</b></td><td>0.20 <b>(+28.28%)</b></td><td>0.03 (+10.61%)</td><td>181.90 <b>(-22.03%)</b></td><td>156.24 <b>(-22.99%)</b></td><td>150.80 <b>(-24.75%)</b></td><td>135.40 <b>(-21.87%)</b></td><td>17.36 <b>(-32.42%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>233.30 (n/a)</td><td>202.88 (n/a)</td><td>200.40 (n/a)</td><td>173.30 (n/a)</td><td>25.69 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.30 (+8.52%)</td><td>0.23 (+6.77%)</td><td>0.21 (-4.41%)</td><td>0.20 <b>(+20.27%)</b></td><td>0.04 (-2.97%)</td><td>185.30 (-16.83%)</td><td>167.14 (-7.17%)</td><td>177.10 (+4.61%)</td><td>124.10 (-7.80%)</td><td>25.14 <b>(-27.51%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>222.80 (n/a)</td><td>180.04 (n/a)</td><td>169.30 (n/a)</td><td>134.60 (n/a)</td><td>34.67 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.29 (-4.76%)</td><td>0.23 (-8.67%)</td><td>0.23 <b>(-20.55%)</b></td><td>0.16 (-1.48%)</td><td>0.05 <b>(-25.03%)</b></td><td>224.70 (+1.49%)</td><td>170.10 (+6.71%)</td><td>158.60 <b>(+25.87%)</b></td><td>128.40 (+4.99%)</td><td>39.39 (-18.11%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.29 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>221.40 (n/a)</td><td>159.40 (n/a)</td><td>126.00 (n/a)</td><td>122.30 (n/a)</td><td>48.09 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.24 <b>(-30.67%)</b></td><td>0.21 (-3.74%)</td><td>0.22 (+6.20%)</td><td>0.17 (+13.90%)</td><td>0.03 <b>(-63.79%)</b></td><td>214.70 (-12.22%)</td><td>175.76 (-2.24%)</td><td>170.70 (-5.85%)</td><td>155.00 <b>(+44.19%)</b></td><td>24.05 <b>(-52.09%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.34 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>244.60 (n/a)</td><td>179.78 (n/a)</td><td>181.30 (n/a)</td><td>107.50 (n/a)</td><td>50.21 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.29 (+13.73%)</td><td>0.23 (+5.13%)</td><td>0.24 (+8.35%)</td><td>0.18 (-5.69%)</td><td>0.04 <b>(+60.70%)</b></td><td>210.50 (+6.05%)</td><td>161.98 (-3.38%)</td><td>154.20 (-7.72%)</td><td>127.30 (-12.09%)</td><td>30.87 <b>(+51.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>198.50 (n/a)</td><td>167.64 (n/a)</td><td>167.10 (n/a)</td><td>144.80 (n/a)</td><td>20.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.33 (-16.70%)</td><td>0.24 (+2.42%)</td><td>0.22 (+13.76%)</td><td>0.21 (+18.42%)</td><td>0.05 <b>(-44.94%)</b></td><td>179.30 (-15.54%)</td><td>157.68 (-8.31%)</td><td>166.40 (-12.10%)</td><td>111.50 <b>(+20.02%)</b></td><td>27.12 <b>(-44.44%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.40 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>212.30 (n/a)</td><td>171.98 (n/a)</td><td>189.30 (n/a)</td><td>92.90 (n/a)</td><td>48.82 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.26 (-3.70%)</td><td>0.23 (+3.10%)</td><td>0.24 (+6.12%)</td><td>0.14 (-18.32%)</td><td>0.05 <b>(+38.80%)</b></td><td>255.30 <b>(+22.45%)</b></td><td>169.46 (-0.12%)</td><td>153.60 (-5.77%)</td><td>140.80 (+3.83%)</td><td>48.35 <b>(+81.77%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>208.50 (n/a)</td><td>169.66 (n/a)</td><td>163.00 (n/a)</td><td>135.60 (n/a)</td><td>26.60 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.36 <b>(+26.75%)</b></td><td>0.30 <b>(+26.90%)</b></td><td>0.29 (+17.41%)</td><td>0.26 <b>(+38.04%)</b></td><td>0.04 (-6.49%)</td><td>158.90 <b>(-27.54%)</b></td><td>136.56 <b>(-22.26%)</b></td><td>140.50 (-14.85%)</td><td>113.90 <b>(-21.07%)</b></td><td>17.70 <b>(-46.65%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>219.30 (n/a)</td><td>175.66 (n/a)</td><td>165.00 (n/a)</td><td>144.30 (n/a)</td><td>33.17 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.36 (+9.69%)</td><td>0.26 (+19.07%)</td><td>0.26 (+17.02%)</td><td>0.19 <b>(+84.20%)</b></td><td>0.06 <b>(-20.77%)</b></td><td>219.60 <b>(-45.70%)</b></td><td>165.86 <b>(-23.97%)</b></td><td>159.60 (-14.52%)</td><td>114.70 (-8.82%)</td><td>38.15 <b>(-64.49%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.33 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>404.40 (n/a)</td><td>218.16 (n/a)</td><td>186.70 (n/a)</td><td>125.80 (n/a)</td><td>107.42 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.34 (-9.59%)</td><td>0.26 (+0.34%)</td><td>0.26 (+6.05%)</td><td>0.20 <b>(+21.17%)</b></td><td>0.05 <b>(-39.80%)</b></td><td>203.60 (-17.50%)</td><td>160.06 (-6.01%)</td><td>158.00 (-5.73%)</td><td>119.50 (+10.55%)</td><td>31.02 <b>(-44.79%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.38 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>246.80 (n/a)</td><td>170.30 (n/a)</td><td>167.60 (n/a)</td><td>108.10 (n/a)</td><td>56.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.34 <b>(+27.90%)</b></td><td>0.27 <b>(+20.90%)</b></td><td>0.26 (+5.86%)</td><td>0.22 <b>(+34.56%)</b></td><td>0.06 <b>(+27.71%)</b></td><td>186.50 <b>(-25.70%)</b></td><td>155.48 (-17.39%)</td><td>158.30 (-5.55%)</td><td>120.30 <b>(-21.78%)</b></td><td>31.44 <b>(-24.42%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>251.00 (n/a)</td><td>188.20 (n/a)</td><td>167.60 (n/a)</td><td>153.80 (n/a)</td><td>41.60 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 <b>(-23.26%)</b></td><td>0.24 (-9.62%)</td><td>0.24 (-5.38%)</td><td>0.20 (-6.70%)</td><td>0.03 <b>(-42.07%)</b></td><td>209.40 (+7.16%)</td><td>174.68 (+9.04%)</td><td>170.00 (+5.72%)</td><td>151.60 <b>(+30.24%)</b></td><td>23.73 (-16.43%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.35 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.05 (n/a)</td><td>195.40 (n/a)</td><td>160.20 (n/a)</td><td>160.80 (n/a)</td><td>116.40 (n/a)</td><td>28.40 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.30 (-12.80%)</td><td>0.25 (-14.65%)</td><td>0.24 <b>(-26.78%)</b></td><td>0.23 (+13.96%)</td><td>0.03 <b>(-50.73%)</b></td><td>178.30 (-12.25%)</td><td>164.40 (+13.43%)</td><td>174.10 <b>(+36.55%)</b></td><td>135.50 (+14.64%)</td><td>18.49 <b>(-49.11%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.35 (n/a)</td><td>0.30 (n/a)</td><td>0.32 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>203.20 (n/a)</td><td>144.94 (n/a)</td><td>127.50 (n/a)</td><td>118.20 (n/a)</td><td>36.33 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.28 (+6.71%)</td><td>0.23 (+8.01%)</td><td>0.21 (+5.66%)</td><td>0.20 (+19.05%)</td><td>0.03 (-9.87%)</td><td>200.50 (-15.97%)</td><td>179.60 (-8.08%)</td><td>190.90 (-5.40%)</td><td>147.50 (-6.29%)</td><td>22.33 <b>(-28.44%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>238.60 (n/a)</td><td>195.38 (n/a)</td><td>201.80 (n/a)</td><td>157.40 (n/a)</td><td>31.21 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.39 <b>(+33.18%)</b></td><td>0.24 (+1.15%)</td><td>0.20 (-11.59%)</td><td>0.17 (-6.62%)</td><td>0.09 <b>(+107.75%)</b></td><td>241.40 (+7.10%)</td><td>189.92 (+5.13%)</td><td>206.30 (+13.10%)</td><td>104.00 <b>(-24.91%)</b></td><td>53.47 <b>(+60.63%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>225.40 (n/a)</td><td>180.66 (n/a)</td><td>182.40 (n/a)</td><td>138.50 (n/a)</td><td>33.29 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.30 <b>(+39.62%)</b></td><td>0.26 <b>(+37.13%)</b></td><td>0.27 <b>(+47.03%)</b></td><td>0.23 <b>(+37.09%)</b></td><td>0.03 <b>(+21.87%)</b></td><td>148.50 <b>(-27.06%)</b></td><td>132.82 <b>(-27.25%)</b></td><td>130.30 <b>(-31.99%)</b></td><td>114.40 <b>(-28.41%)</b></td><td>13.80 <b>(-34.42%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>203.60 (n/a)</td><td>182.58 (n/a)</td><td>191.60 (n/a)</td><td>159.80 (n/a)</td><td>21.05 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.31 <b>(+54.88%)</b></td><td>0.26 <b>(+40.50%)</b></td><td>0.27 <b>(+42.42%)</b></td><td>0.20 (+11.36%)</td><td>0.04 <b>(+366.33%)</b></td><td>177.40 (-10.22%)</td><td>134.84 <b>(-27.26%)</b></td><td>127.90 <b>(-29.76%)</b></td><td>113.00 <b>(-35.47%)</b></td><td>24.97 <b>(+178.85%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>197.60 (n/a)</td><td>185.36 (n/a)</td><td>182.10 (n/a)</td><td>175.10 (n/a)</td><td>8.95 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.31 <b>(+33.01%)</b></td><td>0.22 <b>(+20.07%)</b></td><td>0.20 (+8.01%)</td><td>0.19 <b>(+26.04%)</b></td><td>0.05 <b>(+59.11%)</b></td><td>184.00 <b>(-20.69%)</b></td><td>162.48 (-15.80%)</td><td>176.60 (-7.39%)</td><td>113.60 <b>(-24.82%)</b></td><td>29.48 (-5.71%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>232.00 (n/a)</td><td>192.98 (n/a)</td><td>190.70 (n/a)</td><td>151.10 (n/a)</td><td>31.27 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.28 (+5.17%)</td><td>0.22 (+16.46%)</td><td>0.23 <b>(+26.48%)</b></td><td>0.17 <b>(+22.40%)</b></td><td>0.04 (-6.74%)</td><td>204.60 (-18.29%)</td><td>165.16 (-15.14%)</td><td>152.20 <b>(-20.98%)</b></td><td>125.80 (-4.91%)</td><td>32.68 <b>(-23.30%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>250.40 (n/a)</td><td>194.62 (n/a)</td><td>192.60 (n/a)</td><td>132.30 (n/a)</td><td>42.60 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 (-9.74%)</td><td>0.21 (+3.14%)</td><td>0.21 (+10.67%)</td><td>0.18 (+5.36%)</td><td>0.03 <b>(-37.53%)</b></td><td>195.10 (-5.11%)</td><td>171.02 (-4.78%)</td><td>169.50 (-9.65%)</td><td>140.20 (+10.74%)</td><td>21.25 <b>(-33.16%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>205.60 (n/a)</td><td>179.60 (n/a)</td><td>187.60 (n/a)</td><td>126.60 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.28 (-3.23%)</td><td>0.21 (-3.96%)</td><td>0.21 (+1.68%)</td><td>0.15 (-14.52%)</td><td>0.05 (+5.79%)</td><td>238.50 (+17.03%)</td><td>176.16 (+5.30%)</td><td>165.50 (-1.66%)</td><td>126.00 (+3.28%)</td><td>41.66 <b>(+29.42%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>203.80 (n/a)</td><td>167.30 (n/a)</td><td>168.30 (n/a)</td><td>122.00 (n/a)</td><td>32.19 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.28 (+13.49%)</td><td>0.20 (-2.63%)</td><td>0.21 (-1.11%)</td><td>0.14 <b>(-20.19%)</b></td><td>0.06 <b>(+109.58%)</b></td><td>257.30 <b>(+25.33%)</b></td><td>185.02 (+8.38%)</td><td>166.00 (+1.16%)</td><td>125.80 (-11.90%)</td><td>54.53 <b>(+134.46%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>205.30 (n/a)</td><td>170.72 (n/a)</td><td>164.10 (n/a)</td><td>142.80 (n/a)</td><td>23.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.23 (-3.25%)</td><td>0.19 (-5.43%)</td><td>0.19 (-12.27%)</td><td>0.17 (-0.75%)</td><td>0.03 (-13.48%)</td><td>208.80 (+0.77%)</td><td>183.90 (+5.34%)</td><td>185.00 (+13.99%)</td><td>154.00 (+3.36%)</td><td>23.71 (-9.96%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>207.20 (n/a)</td><td>174.58 (n/a)</td><td>162.30 (n/a)</td><td>149.00 (n/a)</td><td>26.33 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.04 (+18.41%)</td><td>0.72 (-6.57%)</td><td>0.69 (-15.26%)</td><td>0.53 (-12.73%)</td><td>0.20 <b>(+83.12%)</b></td><td>246.80 (+14.58%)</td><td>192.30 (+10.82%)</td><td>189.00 (+18.05%)</td><td>126.00 (-15.55%)</td><td>45.52 <b>(+71.29%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.88 (n/a)</td><td>0.77 (n/a)</td><td>0.82 (n/a)</td><td>0.61 (n/a)</td><td>0.11 (n/a)</td><td>215.40 (n/a)</td><td>173.52 (n/a)</td><td>160.10 (n/a)</td><td>149.20 (n/a)</td><td>26.57 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.73 (-14.80%)</td><td>0.68 (-12.95%)</td><td>0.70 (-14.92%)</td><td>0.60 (-10.92%)</td><td>0.05 <b>(-36.51%)</b></td><td>218.00 (+12.26%)</td><td>194.54 (+14.34%)</td><td>188.50 (+17.52%)</td><td>178.80 (+17.32%)</td><td>15.85 (-16.48%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.86 (n/a)</td><td>0.78 (n/a)</td><td>0.82 (n/a)</td><td>0.67 (n/a)</td><td>0.08 (n/a)</td><td>194.20 (n/a)</td><td>170.14 (n/a)</td><td>160.40 (n/a)</td><td>152.40 (n/a)</td><td>18.98 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.77 <b>(-25.06%)</b></td><td>0.67 <b>(-22.99%)</b></td><td>0.74 (-16.95%)</td><td>0.41 <b>(-35.21%)</b></td><td>0.15 (-3.48%)</td><td>317.00 <b>(+54.33%)</b></td><td>207.32 <b>(+33.27%)</b></td><td>176.90 <b>(+20.42%)</b></td><td>171.10 <b>(+33.46%)</b></td><td>62.16 <b>(+101.11%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.02 (n/a)</td><td>0.87 (n/a)</td><td>0.89 (n/a)</td><td>0.64 (n/a)</td><td>0.15 (n/a)</td><td>205.40 (n/a)</td><td>155.56 (n/a)</td><td>146.90 (n/a)</td><td>128.20 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+10.17%)</td><td>0.02 (+8.16%)</td><td>0.02 (+10.32%)</td><td>0.02 (-3.47%)</td><td>0.00 <b>(+35.04%)</b></td><td>218.60 (+3.60%)</td><td>175.24 (-6.70%)</td><td>168.20 (-9.38%)</td><td>139.70 (-9.23%)</td><td>29.72 <b>(+26.48%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.00 (n/a)</td><td>187.82 (n/a)</td><td>185.60 (n/a)</td><td>153.90 (n/a)</td><td>23.50 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-11.62%)</td><td>0.02 (-12.00%)</td><td>0.02 (-18.07%)</td><td>0.02 (+1.24%)</td><td>0.00 <b>(-33.89%)</b></td><td>208.40 (-1.23%)</td><td>183.20 (+12.25%)</td><td>175.80 <b>(+22.08%)</b></td><td>160.00 (+13.15%)</td><td>23.42 <b>(-23.39%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.00 (n/a)</td><td>163.20 (n/a)</td><td>144.00 (n/a)</td><td>141.40 (n/a)</td><td>30.56 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+3.99%)</td><td>0.02 (+4.92%)</td><td>0.02 (+10.95%)</td><td>0.02 (+0.21%)</td><td>0.01 (-0.08%)</td><td>208.00 (-0.19%)</td><td>173.70 (-4.97%)</td><td>178.60 (-9.89%)</td><td>122.90 (-3.83%)</td><td>31.21 (-8.54%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.40 (n/a)</td><td>182.78 (n/a)</td><td>198.20 (n/a)</td><td>127.80 (n/a)</td><td>34.13 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>16.94 <b>(+22.14%)</b></td><td>13.07 (+7.56%)</td><td>12.76 (+1.94%)</td><td>9.94 (+6.94%)</td><td>2.56 <b>(+50.45%)</b></td><td>211.00 (-6.47%)</td><td>165.38 (-5.94%)</td><td>164.40 (-1.91%)</td><td>123.90 (-18.11%)</td><td>31.64 (+10.22%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.87 (n/a)</td><td>12.15 (n/a)</td><td>12.52 (n/a)</td><td>9.30 (n/a)</td><td>1.70 (n/a)</td><td>225.60 (n/a)</td><td>175.82 (n/a)</td><td>167.60 (n/a)</td><td>151.30 (n/a)</td><td>28.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.90 (-15.32%)</td><td>0.79 (-9.48%)</td><td>0.78 (-12.70%)</td><td>0.64 (-4.81%)</td><td>0.10 <b>(-29.67%)</b></td><td>205.70 (+5.06%)</td><td>169.76 (+9.54%)</td><td>169.00 (+14.50%)</td><td>147.10 (+18.15%)</td><td>22.78 (-13.56%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.06 (n/a)</td><td>0.87 (n/a)</td><td>0.90 (n/a)</td><td>0.67 (n/a)</td><td>0.14 (n/a)</td><td>195.80 (n/a)</td><td>154.98 (n/a)</td><td>147.60 (n/a)</td><td>124.50 (n/a)</td><td>26.36 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.93 (-4.41%)</td><td>0.83 (-1.65%)</td><td>0.84 (+2.66%)</td><td>0.67 (-9.98%)</td><td>0.10 (-2.50%)</td><td>197.30 (+11.03%)</td><td>161.48 (+1.80%)</td><td>156.80 (-2.61%)</td><td>141.90 (+4.65%)</td><td>21.77 (+13.50%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.97 (n/a)</td><td>0.84 (n/a)</td><td>0.82 (n/a)</td><td>0.74 (n/a)</td><td>0.10 (n/a)</td><td>177.70 (n/a)</td><td>158.62 (n/a)</td><td>161.00 (n/a)</td><td>135.60 (n/a)</td><td>19.18 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.88 (-4.09%)</td><td>0.72 (-0.92%)</td><td>0.69 (-8.31%)</td><td>0.60 (+19.83%)</td><td>0.11 <b>(-26.57%)</b></td><td>218.90 (-16.55%)</td><td>186.38 (-1.26%)</td><td>190.40 (+9.05%)</td><td>149.80 (+4.24%)</td><td>28.23 <b>(-37.90%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.92 (n/a)</td><td>0.73 (n/a)</td><td>0.76 (n/a)</td><td>0.50 (n/a)</td><td>0.16 (n/a)</td><td>262.30 (n/a)</td><td>188.76 (n/a)</td><td>174.60 (n/a)</td><td>143.70 (n/a)</td><td>45.46 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.75 <b>(-27.74%)</b></td><td>0.67 (-19.89%)</td><td>0.69 (-10.54%)</td><td>0.56 <b>(-20.31%)</b></td><td>0.07 <b>(-52.81%)</b></td><td>237.20 <b>(+25.50%)</b></td><td>198.14 <b>(+22.96%)</b></td><td>191.10 (+11.82%)</td><td>176.90 <b>(+38.31%)</b></td><td>23.29 (-15.88%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.03 (n/a)</td><td>0.84 (n/a)</td><td>0.77 (n/a)</td><td>0.70 (n/a)</td><td>0.15 (n/a)</td><td>189.00 (n/a)</td><td>161.14 (n/a)</td><td>170.90 (n/a)</td><td>127.90 (n/a)</td><td>27.69 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.95 (-9.27%)</td><td>0.78 (-5.33%)</td><td>0.76 (-6.41%)</td><td>0.61 (-5.89%)</td><td>0.13 (-12.51%)</td><td>217.80 (+6.24%)</td><td>173.46 (+5.41%)</td><td>174.60 (+6.85%)</td><td>138.40 (+10.19%)</td><td>29.47 (+4.17%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.05 (n/a)</td><td>0.82 (n/a)</td><td>0.81 (n/a)</td><td>0.64 (n/a)</td><td>0.15 (n/a)</td><td>205.00 (n/a)</td><td>164.56 (n/a)</td><td>163.40 (n/a)</td><td>125.60 (n/a)</td><td>28.29 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (+15.30%)</td><td>0.03 (+9.51%)</td><td>0.03 (+18.73%)</td><td>0.02 (-0.02%)</td><td>0.00 <b>(+95.22%)</b></td><td>212.20 (+0.00%)</td><td>169.14 (-6.56%)</td><td>153.20 (-15.78%)</td><td>137.80 (-13.28%)</td><td>35.19 <b>(+70.02%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.20 (n/a)</td><td>181.02 (n/a)</td><td>181.90 (n/a)</td><td>158.90 (n/a)</td><td>20.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.03 (-3.55%)</td><td>0.02 (+4.97%)</td><td>0.02 (+5.19%)</td><td>0.02 <b>(+39.17%)</b></td><td>0.00 <b>(-48.28%)</b></td><td>196.90 <b>(-28.14%)</b></td><td>166.88 (-10.17%)</td><td>165.80 (-4.93%)</td><td>133.90 (+3.72%)</td><td>22.46 <b>(-61.74%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>274.00 (n/a)</td><td>185.78 (n/a)</td><td>174.40 (n/a)</td><td>129.10 (n/a)</td><td>58.72 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.00 (+9.52%)</td><td>0.00 (+3.40%)</td><td>0.00 (+0.00%)</td><td>0.00 (+2.56%)</td><td>0.00 <b>(+68.03%)</b></td><td>1032.02 (-1.13%)</td><td>963.81 (-3.27%)</td><td>965.48 (-1.98%)</td><td>898.11 (-7.38%)</td><td>47.93 <b>(+62.92%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1043.79 (n/a)</td><td>996.35 (n/a)</td><td>985.03 (n/a)</td><td>969.62 (n/a)</td><td>29.42 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.01 (+0.00%)</td><td>0.01 (+0.00%)</td><td>0.01 (+0.00%)</td><td>0.01 (+0.00%)</td><td>0.00 (+0.00%)</td><td>1113.23 (+1.01%)</td><td>1035.52 (+0.33%)</td><td>1028.52 (+0.42%)</td><td>972.24 (-0.78%)</td><td>50.55 (+14.44%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1102.08 (n/a)</td><td>1032.09 (n/a)</td><td>1024.17 (n/a)</td><td>979.86 (n/a)</td><td>44.17 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.00 (+2.84%)</td><td>0.96 (+1.31%)</td><td>0.96 (+0.70%)</td><td>0.95 (+1.52%)</td><td>0.02 <b>(+27.86%)</b></td><td>2215.08 (-1.50%)</td><td>2178.21 (-1.28%)</td><td>2193.44 (-0.69%)</td><td>2093.42 (-2.76%)</td><td>48.46 <b>(+21.68%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.95 (n/a)</td><td>0.93 (n/a)</td><td>0.02 (n/a)</td><td>2248.81 (n/a)</td><td>2206.35 (n/a)</td><td>2208.73 (n/a)</td><td>2152.84 (n/a)</td><td>39.82 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.39 (-1.48%)</td><td>0.39 (-1.25%)</td><td>0.39 (-2.05%)</td><td>0.38 (-0.21%)</td><td>0.01 <b>(-26.32%)</b></td><td>1384.26 (+0.20%)</td><td>1356.09 (+1.25%)</td><td>1355.73 (+2.09%)</td><td>1338.93 (+1.51%)</td><td>18.40 <b>(-25.78%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.38 (n/a)</td><td>0.01 (n/a)</td><td>1381.55 (n/a)</td><td>1339.37 (n/a)</td><td>1327.98 (n/a)</td><td>1319.01 (n/a)</td><td>24.78 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.26 (+2.79%)</td><td>0.24 (-1.64%)</td><td>0.24 (-2.41%)</td><td>0.23 (-6.42%)</td><td>0.01 <b>(+349.85%)</b></td><td>2291.89 (+6.89%)</td><td>2148.86 (+1.83%)</td><td>2160.82 (+2.47%)</td><td>2035.86 (-2.72%)</td><td>98.40 <b>(+370.49%)</b></td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.00 (n/a)</td><td>2144.14 (n/a)</td><td>2110.26 (n/a)</td><td>2108.65 (n/a)</td><td>2092.80 (n/a)</td><td>20.91 (n/a)</td>
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
<td><code>b091dbd</code> — 2026-09-09 01:28:06</td><td>0.37 (+0.21%)</td><td>0.37 (+0.99%)</td><td>0.37 (+2.19%)</td><td>0.36 (+0.79%)</td><td>0.01 (-6.68%)</td><td>1465.70 (-0.77%)</td><td>1427.91 (-0.98%)</td><td>1421.70 (-2.13%)</td><td>1404.03 (-0.22%)</td><td>26.67 (-7.40%)</td>
</tr>
<tr>
<td><code>6c9b2b3</code> — 2026-09-09 00:22:35</td><td>0.37 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.01 (n/a)</td><td>1477.08 (n/a)</td><td>1442.05 (n/a)</td><td>1452.58 (n/a)</td><td>1407.08 (n/a)</td><td>28.80 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.08 (-13.89%)</td><td>4.64 (-4.72%)</td><td>4.69 (+3.73%)</td><td>3.98 (+12.22%)</td><td>0.40 <b>(-60.05%)</b></td><td>263.30 (-10.90%)</td><td>227.66 (+1.87%)</td><td>223.50 (-3.58%)</td><td>206.50 (+16.14%)</td><td>21.30 <b>(-56.21%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>5.90 (n/a)</td><td>4.87 (n/a)</td><td>4.52 (n/a)</td><td>3.55 (n/a)</td><td>1.01 (n/a)</td><td>295.50 (n/a)</td><td>223.48 (n/a)</td><td>231.80 (n/a)</td><td>177.80 (n/a)</td><td>48.63 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>6.07 (-3.32%)</td><td>5.04 (-2.53%)</td><td>4.57 (-8.79%)</td><td>4.45 (+13.74%)</td><td>0.75 <b>(-29.32%)</b></td><td>235.70 (-12.09%)</td><td>211.54 (+0.78%)</td><td>229.30 (+9.66%)</td><td>172.70 (+3.41%)</td><td>29.42 <b>(-32.69%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.28 (n/a)</td><td>5.17 (n/a)</td><td>5.01 (n/a)</td><td>3.91 (n/a)</td><td>1.06 (n/a)</td><td>268.10 (n/a)</td><td>209.90 (n/a)</td><td>209.10 (n/a)</td><td>167.00 (n/a)</td><td>43.70 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.91 (-0.14%)</td><td>4.86 (-6.27%)</td><td>4.83 (-15.41%)</td><td>4.07 (+1.74%)</td><td>0.74 (-14.75%)</td><td>257.40 (-1.72%)</td><td>219.56 (+5.99%)</td><td>217.20 (+18.17%)</td><td>177.30 (+0.17%)</td><td>32.41 (-14.43%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>5.92 (n/a)</td><td>5.19 (n/a)</td><td>5.71 (n/a)</td><td>4.00 (n/a)</td><td>0.87 (n/a)</td><td>261.90 (n/a)</td><td>207.16 (n/a)</td><td>183.80 (n/a)</td><td>177.00 (n/a)</td><td>37.87 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.90 (-8.30%)</td><td>5.29 (-9.69%)</td><td>5.33 (-9.44%)</td><td>4.32 (-17.92%)</td><td>0.63 <b>(+48.72%)</b></td><td>242.80 <b>(+21.89%)</b></td><td>200.84 (+11.65%)</td><td>196.70 (+10.44%)</td><td>177.70 (+9.09%)</td><td>25.91 <b>(+98.13%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.44 (n/a)</td><td>5.85 (n/a)</td><td>5.89 (n/a)</td><td>5.26 (n/a)</td><td>0.42 (n/a)</td><td>199.20 (n/a)</td><td>179.88 (n/a)</td><td>178.10 (n/a)</td><td>162.90 (n/a)</td><td>13.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.23 (-12.02%)</td><td>4.70 (-5.32%)</td><td>4.71 (+4.57%)</td><td>4.07 (+0.08%)</td><td>0.42 <b>(-52.46%)</b></td><td>257.30 (-0.08%)</td><td>224.72 (+3.69%)</td><td>222.80 (-4.38%)</td><td>200.40 (+13.67%)</td><td>21.07 <b>(-43.67%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>5.95 (n/a)</td><td>4.96 (n/a)</td><td>4.50 (n/a)</td><td>4.07 (n/a)</td><td>0.89 (n/a)</td><td>257.50 (n/a)</td><td>216.72 (n/a)</td><td>233.00 (n/a)</td><td>176.30 (n/a)</td><td>37.41 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.74 (-0.12%)</td><td>4.61 (-7.02%)</td><td>4.54 (-11.57%)</td><td>3.96 (+14.09%)</td><td>0.71 <b>(-20.62%)</b></td><td>264.80 (-12.35%)</td><td>231.30 (+5.98%)</td><td>230.90 (+13.13%)</td><td>182.80 (+0.11%)</td><td>32.62 <b>(-32.48%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>5.74 (n/a)</td><td>4.96 (n/a)</td><td>5.14 (n/a)</td><td>3.47 (n/a)</td><td>0.89 (n/a)</td><td>302.10 (n/a)</td><td>218.24 (n/a)</td><td>204.10 (n/a)</td><td>182.60 (n/a)</td><td>48.31 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>6.54 (-6.19%)</td><td>5.46 (+5.97%)</td><td>5.25 (+11.81%)</td><td>4.79 <b>(+39.74%)</b></td><td>0.68 <b>(-50.45%)</b></td><td>218.80 <b>(-28.43%)</b></td><td>194.36 (-10.03%)</td><td>199.60 (-10.57%)</td><td>160.30 (+6.58%)</td><td>22.55 <b>(-62.30%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>6.97 (n/a)</td><td>5.15 (n/a)</td><td>4.70 (n/a)</td><td>3.43 (n/a)</td><td>1.37 (n/a)</td><td>305.70 (n/a)</td><td>216.02 (n/a)</td><td>223.20 (n/a)</td><td>150.40 (n/a)</td><td>59.82 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>5.46 (-11.94%)</td><td>4.86 (-6.49%)</td><td>5.12 (-1.20%)</td><td>3.86 (-5.40%)</td><td>0.62 (-18.01%)</td><td>271.90 (+5.67%)</td><td>219.16 (+6.57%)</td><td>204.90 (+1.24%)</td><td>192.00 (+13.54%)</td><td>31.52 (-1.78%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>6.20 (n/a)</td><td>5.19 (n/a)</td><td>5.18 (n/a)</td><td>4.08 (n/a)</td><td>0.76 (n/a)</td><td>257.30 (n/a)</td><td>205.64 (n/a)</td><td>202.40 (n/a)</td><td>169.10 (n/a)</td><td>32.09 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>8.66 (-6.75%)</td><td>7.92 (+3.04%)</td><td>7.94 (+11.34%)</td><td>7.19 (+3.34%)</td><td>0.59 <b>(-40.67%)</b></td><td>291.60 (-3.22%)</td><td>265.94 (-3.71%)</td><td>264.10 (-10.20%)</td><td>242.10 (+7.22%)</td><td>19.95 <b>(-38.72%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.29 (n/a)</td><td>7.69 (n/a)</td><td>7.13 (n/a)</td><td>6.96 (n/a)</td><td>1.00 (n/a)</td><td>301.30 (n/a)</td><td>276.20 (n/a)</td><td>294.10 (n/a)</td><td>225.80 (n/a)</td><td>32.56 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>9.30 (+1.85%)</td><td>7.79 (-9.28%)</td><td>7.97 (-7.36%)</td><td>6.48 <b>(-21.46%)</b></td><td>1.12 <b>(+212.94%)</b></td><td>323.40 <b>(+27.32%)</b></td><td>273.58 (+11.90%)</td><td>263.30 (+7.95%)</td><td>225.40 (-1.83%)</td><td>39.14 <b>(+294.42%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.14 (n/a)</td><td>8.59 (n/a)</td><td>8.60 (n/a)</td><td>8.26 (n/a)</td><td>0.36 (n/a)</td><td>254.00 (n/a)</td><td>244.48 (n/a)</td><td>243.90 (n/a)</td><td>229.60 (n/a)</td><td>9.92 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>8.68 (-8.81%)</td><td>7.72 (-9.79%)</td><td>7.72 (-10.23%)</td><td>6.84 (-9.41%)</td><td>0.67 <b>(-23.42%)</b></td><td>306.50 (+10.41%)</td><td>273.46 (+10.58%)</td><td>271.60 (+11.40%)</td><td>241.50 (+9.62%)</td><td>23.77 (-7.26%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.52 (n/a)</td><td>8.55 (n/a)</td><td>8.60 (n/a)</td><td>7.55 (n/a)</td><td>0.88 (n/a)</td><td>277.60 (n/a)</td><td>247.30 (n/a)</td><td>243.80 (n/a)</td><td>220.30 (n/a)</td><td>25.63 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>7.96 (-14.23%)</td><td>7.45 (-7.69%)</td><td>7.63 (-3.08%)</td><td>6.68 (-7.17%)</td><td>0.49 <b>(-39.44%)</b></td><td>313.90 (+7.72%)</td><td>282.30 (+7.89%)</td><td>274.80 (+3.15%)</td><td>263.60 (+16.59%)</td><td>19.35 <b>(-22.66%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.28 (n/a)</td><td>8.08 (n/a)</td><td>7.87 (n/a)</td><td>7.20 (n/a)</td><td>0.80 (n/a)</td><td>291.40 (n/a)</td><td>261.66 (n/a)</td><td>266.40 (n/a)</td><td>226.10 (n/a)</td><td>25.02 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>8.51 (-18.40%)</td><td>7.77 (-8.12%)</td><td>7.77 (-3.71%)</td><td>7.16 (-3.93%)</td><td>0.52 <b>(-55.45%)</b></td><td>292.80 (+4.09%)</td><td>270.90 (+7.74%)</td><td>270.10 (+3.88%)</td><td>246.40 <b>(+22.53%)</b></td><td>18.05 <b>(-42.11%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>10.43 (n/a)</td><td>8.46 (n/a)</td><td>8.06 (n/a)</td><td>7.46 (n/a)</td><td>1.18 (n/a)</td><td>281.30 (n/a)</td><td>251.44 (n/a)</td><td>260.00 (n/a)</td><td>201.10 (n/a)</td><td>31.18 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>9.32 (+4.81%)</td><td>7.98 (-5.16%)</td><td>7.86 (-6.29%)</td><td>6.85 (-14.35%)</td><td>0.92 <b>(+134.01%)</b></td><td>306.10 (+16.74%)</td><td>265.38 (+6.35%)</td><td>266.90 (+6.72%)</td><td>225.00 (-4.62%)</td><td>30.03 <b>(+159.23%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>8.89 (n/a)</td><td>8.42 (n/a)</td><td>8.39 (n/a)</td><td>8.00 (n/a)</td><td>0.39 (n/a)</td><td>262.20 (n/a)</td><td>249.54 (n/a)</td><td>250.10 (n/a)</td><td>235.90 (n/a)</td><td>11.59 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>9.38 (-1.68%)</td><td>8.01 (-2.64%)</td><td>7.68 (-1.33%)</td><td>7.60 (-1.43%)</td><td>0.77 (-1.11%)</td><td>276.00 (+1.43%)</td><td>263.60 (+2.72%)</td><td>273.00 (+1.34%)</td><td>223.70 (+1.73%)</td><td>22.36 (+1.23%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.54 (n/a)</td><td>8.22 (n/a)</td><td>7.78 (n/a)</td><td>7.71 (n/a)</td><td>0.77 (n/a)</td><td>272.10 (n/a)</td><td>256.62 (n/a)</td><td>269.40 (n/a)</td><td>219.90 (n/a)</td><td>22.08 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>8.58 (-10.71%)</td><td>7.74 (-6.57%)</td><td>7.96 (-3.41%)</td><td>7.02 (+0.70%)</td><td>0.68 <b>(-29.18%)</b></td><td>298.80 (-0.70%)</td><td>272.60 (+6.53%)</td><td>263.40 (+3.50%)</td><td>244.40 (+11.96%)</td><td>24.05 <b>(-20.06%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.61 (n/a)</td><td>8.28 (n/a)</td><td>8.24 (n/a)</td><td>6.97 (n/a)</td><td>0.96 (n/a)</td><td>300.90 (n/a)</td><td>255.90 (n/a)</td><td>254.50 (n/a)</td><td>218.30 (n/a)</td><td>30.09 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>11.16 <b>(+22.69%)</b></td><td>9.12 (+9.17%)</td><td>8.59 (-1.49%)</td><td>7.34 (+2.05%)</td><td>1.71 <b>(+100.80%)</b></td><td>285.70 (-2.02%)</td><td>236.30 (-6.65%)</td><td>244.20 (+1.54%)</td><td>187.90 (-18.48%)</td><td>43.09 <b>(+59.03%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.10 (n/a)</td><td>8.36 (n/a)</td><td>8.72 (n/a)</td><td>7.19 (n/a)</td><td>0.85 (n/a)</td><td>291.60 (n/a)</td><td>253.14 (n/a)</td><td>240.50 (n/a)</td><td>230.50 (n/a)</td><td>27.10 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>9.12 (-7.72%)</td><td>7.78 (-14.12%)</td><td>8.18 (-8.20%)</td><td>5.47 <b>(-36.73%)</b></td><td>1.37 <b>(+184.57%)</b></td><td>383.20 <b>(+58.02%)</b></td><td>278.10 (+19.85%)</td><td>256.50 (+8.96%)</td><td>230.00 (+8.39%)</td><td>60.38 <b>(+413.87%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.88 (n/a)</td><td>9.06 (n/a)</td><td>8.91 (n/a)</td><td>8.65 (n/a)</td><td>0.48 (n/a)</td><td>242.50 (n/a)</td><td>232.04 (n/a)</td><td>235.40 (n/a)</td><td>212.20 (n/a)</td><td>11.75 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>9.82 (+8.41%)</td><td>8.77 (+6.38%)</td><td>9.61 (+18.17%)</td><td>7.23 (-8.42%)</td><td>1.32 <b>(+182.15%)</b></td><td>290.30 (+9.22%)</td><td>243.70 (-4.40%)</td><td>218.20 (-15.39%)</td><td>213.50 (-7.78%)</td><td>38.86 <b>(+185.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.06 (n/a)</td><td>8.25 (n/a)</td><td>8.13 (n/a)</td><td>7.89 (n/a)</td><td>0.47 (n/a)</td><td>265.80 (n/a)</td><td>254.92 (n/a)</td><td>257.90 (n/a)</td><td>231.50 (n/a)</td><td>13.60 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>8.39 (-14.41%)</td><td>7.08 <b>(-20.79%)</b></td><td>7.49 (-17.64%)</td><td>5.61 <b>(-31.28%)</b></td><td>1.27 <b>(+93.89%)</b></td><td>373.50 <b>(+45.50%)</b></td><td>304.60 <b>(+29.18%)</b></td><td>280.10 <b>(+21.41%)</b></td><td>250.10 (+16.87%)</td><td>57.28 <b>(+231.55%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>9.80 (n/a)</td><td>8.93 (n/a)</td><td>9.09 (n/a)</td><td>8.17 (n/a)</td><td>0.65 (n/a)</td><td>256.70 (n/a)</td><td>235.80 (n/a)</td><td>230.70 (n/a)</td><td>214.00 (n/a)</td><td>17.27 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>11.89 (-0.91%)</td><td>11.14 (-1.77%)</td><td>11.26 (-1.00%)</td><td>10.13 (-2.92%)</td><td>0.67 (+9.86%)</td><td>414.20 (+3.01%)</td><td>377.52 (+1.87%)</td><td>372.70 (+1.03%)</td><td>352.70 (+0.92%)</td><td>23.40 (+14.71%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>12.00 (n/a)</td><td>11.34 (n/a)</td><td>11.37 (n/a)</td><td>10.43 (n/a)</td><td>0.61 (n/a)</td><td>402.10 (n/a)</td><td>370.60 (n/a)</td><td>368.90 (n/a)</td><td>349.50 (n/a)</td><td>20.40 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>12.79 (+4.79%)</td><td>10.71 (-4.69%)</td><td>10.59 (-5.22%)</td><td>8.04 <b>(-21.86%)</b></td><td>1.77 <b>(+114.98%)</b></td><td>521.90 <b>(+27.98%)</b></td><td>401.16 (+7.05%)</td><td>396.00 (+5.52%)</td><td>328.10 (-4.57%)</td><td>73.89 <b>(+168.83%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>12.20 (n/a)</td><td>11.24 (n/a)</td><td>11.18 (n/a)</td><td>10.28 (n/a)</td><td>0.83 (n/a)</td><td>407.80 (n/a)</td><td>374.74 (n/a)</td><td>375.30 (n/a)</td><td>343.80 (n/a)</td><td>27.49 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>11.75 (-11.38%)</td><td>11.08 (-4.92%)</td><td>11.35 (-2.55%)</td><td>9.87 (-7.33%)</td><td>0.72 <b>(-27.54%)</b></td><td>424.80 (+7.93%)</td><td>379.76 (+4.99%)</td><td>369.50 (+2.64%)</td><td>357.00 (+12.83%)</td><td>26.28 (-9.55%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.26 (n/a)</td><td>11.66 (n/a)</td><td>11.65 (n/a)</td><td>10.65 (n/a)</td><td>0.99 (n/a)</td><td>393.60 (n/a)</td><td>361.72 (n/a)</td><td>360.00 (n/a)</td><td>316.40 (n/a)</td><td>29.05 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>12.22 (-7.10%)</td><td>11.22 (-5.79%)</td><td>11.11 (-10.84%)</td><td>10.08 (-0.84%)</td><td>0.82 <b>(-31.08%)</b></td><td>416.30 (+0.85%)</td><td>375.54 (+5.70%)</td><td>377.40 (+12.15%)</td><td>343.30 (+7.65%)</td><td>28.08 <b>(-25.64%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.15 (n/a)</td><td>11.91 (n/a)</td><td>12.47 (n/a)</td><td>10.16 (n/a)</td><td>1.20 (n/a)</td><td>412.80 (n/a)</td><td>355.28 (n/a)</td><td>336.50 (n/a)</td><td>318.90 (n/a)</td><td>37.76 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>13.26 (+9.92%)</td><td>12.02 (+6.84%)</td><td>11.90 (+3.88%)</td><td>10.15 (-1.58%)</td><td>1.29 <b>(+76.41%)</b></td><td>413.40 (+1.62%)</td><td>352.42 (-5.82%)</td><td>352.30 (-3.74%)</td><td>316.30 (-9.03%)</td><td>39.80 <b>(+60.71%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>12.06 (n/a)</td><td>11.25 (n/a)</td><td>11.46 (n/a)</td><td>10.31 (n/a)</td><td>0.73 (n/a)</td><td>406.80 (n/a)</td><td>374.18 (n/a)</td><td>366.00 (n/a)</td><td>347.70 (n/a)</td><td>24.77 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>12.69 (+1.23%)</td><td>10.74 (-9.37%)</td><td>11.05 (-5.08%)</td><td>8.04 <b>(-29.12%)</b></td><td>1.68 <b>(+237.04%)</b></td><td>521.70 <b>(+41.08%)</b></td><td>399.42 (+12.70%)</td><td>379.40 (+5.33%)</td><td>330.50 (-1.23%)</td><td>71.97 <b>(+389.21%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>12.54 (n/a)</td><td>11.85 (n/a)</td><td>11.65 (n/a)</td><td>11.34 (n/a)</td><td>0.50 (n/a)</td><td>369.80 (n/a)</td><td>354.42 (n/a)</td><td>360.20 (n/a)</td><td>334.60 (n/a)</td><td>14.71 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>13.44 (+4.80%)</td><td>12.75 (+5.45%)</td><td>12.75 (+5.34%)</td><td>12.29 (+11.25%)</td><td>0.48 <b>(-31.13%)</b></td><td>341.40 (-10.11%)</td><td>329.42 (-5.33%)</td><td>328.90 (-5.08%)</td><td>312.20 (-4.58%)</td><td>12.16 <b>(-40.80%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>12.82 (n/a)</td><td>12.09 (n/a)</td><td>12.11 (n/a)</td><td>11.04 (n/a)</td><td>0.69 (n/a)</td><td>379.80 (n/a)</td><td>347.96 (n/a)</td><td>346.50 (n/a)</td><td>327.20 (n/a)</td><td>20.54 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>15.14 (-1.28%)</td><td>12.97 (-3.81%)</td><td>12.38 (-4.30%)</td><td>12.00 (+1.39%)</td><td>1.32 (-15.31%)</td><td>349.60 (-1.38%)</td><td>325.76 (+3.66%)</td><td>338.70 (+4.50%)</td><td>277.00 (+1.32%)</td><td>30.47 (-14.32%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>15.34 (n/a)</td><td>13.49 (n/a)</td><td>12.94 (n/a)</td><td>11.83 (n/a)</td><td>1.56 (n/a)</td><td>354.50 (n/a)</td><td>314.26 (n/a)</td><td>324.10 (n/a)</td><td>273.40 (n/a)</td><td>35.56 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>12.69 (-16.31%)</td><td>11.93 (-8.55%)</td><td>11.86 (-7.96%)</td><td>11.02 (-5.93%)</td><td>0.64 <b>(-52.32%)</b></td><td>380.70 (+6.31%)</td><td>352.38 (+8.73%)</td><td>353.80 (+8.66%)</td><td>330.60 (+19.48%)</td><td>19.28 <b>(-39.11%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>15.16 (n/a)</td><td>13.05 (n/a)</td><td>12.88 (n/a)</td><td>11.71 (n/a)</td><td>1.35 (n/a)</td><td>358.10 (n/a)</td><td>324.10 (n/a)</td><td>325.60 (n/a)</td><td>276.70 (n/a)</td><td>31.66 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>14.09 (-5.90%)</td><td>12.36 (-7.75%)</td><td>12.58 (-6.85%)</td><td>10.90 (-11.37%)</td><td>1.20 (+4.75%)</td><td>384.90 (+12.81%)</td><td>341.76 (+8.56%)</td><td>333.40 (+7.34%)</td><td>297.60 (+6.25%)</td><td>32.68 <b>(+23.49%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>14.98 (n/a)</td><td>13.40 (n/a)</td><td>13.50 (n/a)</td><td>12.29 (n/a)</td><td>1.14 (n/a)</td><td>341.20 (n/a)</td><td>314.80 (n/a)</td><td>310.60 (n/a)</td><td>280.10 (n/a)</td><td>26.46 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>14.53 (+4.34%)</td><td>12.07 (-5.82%)</td><td>11.87 (-6.37%)</td><td>9.47 (-16.68%)</td><td>1.92 <b>(+96.04%)</b></td><td>443.10 <b>(+20.02%)</b></td><td>354.86 (+7.93%)</td><td>353.30 (+6.80%)</td><td>288.60 (-4.15%)</td><td>58.87 <b>(+125.34%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>13.93 (n/a)</td><td>12.82 (n/a)</td><td>12.68 (n/a)</td><td>11.36 (n/a)</td><td>0.98 (n/a)</td><td>369.20 (n/a)</td><td>328.80 (n/a)</td><td>330.80 (n/a)</td><td>301.10 (n/a)</td><td>26.12 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>15.26 (+5.74%)</td><td>12.48 (-0.64%)</td><td>12.66 (-2.21%)</td><td>9.12 (-14.69%)</td><td>2.19 <b>(+40.34%)</b></td><td>459.80 (+17.24%)</td><td>345.66 (+2.18%)</td><td>331.40 (+2.25%)</td><td>274.90 (-5.44%)</td><td>68.46 <b>(+59.58%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>14.43 (n/a)</td><td>12.56 (n/a)</td><td>12.94 (n/a)</td><td>10.69 (n/a)</td><td>1.56 (n/a)</td><td>392.20 (n/a)</td><td>338.28 (n/a)</td><td>324.10 (n/a)</td><td>290.70 (n/a)</td><td>42.90 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>14.35 (-1.81%)</td><td>13.43 (-1.42%)</td><td>13.91 (+0.29%)</td><td>12.26 (+0.91%)</td><td>0.94 (-0.74%)</td><td>342.10 (-0.90%)</td><td>313.52 (+1.43%)</td><td>301.50 (-0.30%)</td><td>292.20 (+1.81%)</td><td>22.58 (-0.14%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>14.62 (n/a)</td><td>13.63 (n/a)</td><td>13.87 (n/a)</td><td>12.15 (n/a)</td><td>0.95 (n/a)</td><td>345.20 (n/a)</td><td>309.10 (n/a)</td><td>302.40 (n/a)</td><td>287.00 (n/a)</td><td>22.61 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>14.75 (+5.58%)</td><td>13.18 (-1.29%)</td><td>13.02 (-2.55%)</td><td>10.68 (-16.09%)</td><td>1.64 <b>(+245.21%)</b></td><td>392.80 (+19.17%)</td><td>322.62 (+2.58%)</td><td>322.20 (+2.61%)</td><td>284.40 (-5.26%)</td><td>43.64 <b>(+287.99%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>13.97 (n/a)</td><td>13.35 (n/a)</td><td>13.36 (n/a)</td><td>12.73 (n/a)</td><td>0.48 (n/a)</td><td>329.60 (n/a)</td><td>314.50 (n/a)</td><td>314.00 (n/a)</td><td>300.20 (n/a)</td><td>11.25 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>12.98 (-13.88%)</td><td>11.92 (-8.99%)</td><td>11.88 (-9.76%)</td><td>10.48 (+2.29%)</td><td>0.92 <b>(-50.96%)</b></td><td>400.10 (-2.22%)</td><td>353.56 (+8.44%)</td><td>353.00 (+10.83%)</td><td>323.20 (+16.13%)</td><td>28.84 <b>(-44.09%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>15.07 (n/a)</td><td>13.10 (n/a)</td><td>13.17 (n/a)</td><td>10.25 (n/a)</td><td>1.89 (n/a)</td><td>409.20 (n/a)</td><td>326.04 (n/a)</td><td>318.50 (n/a)</td><td>278.30 (n/a)</td><td>51.58 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>17.73 (-7.59%)</td><td>12.82 (-9.96%)</td><td>12.67 (-8.75%)</td><td>9.51 (+2.33%)</td><td>3.37 (-11.44%)</td><td>440.80 (-2.28%)</td><td>345.08 (+10.11%)</td><td>330.90 (+9.57%)</td><td>236.50 (+8.19%)</td><td>86.11 (-4.25%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>19.19 (n/a)</td><td>14.23 (n/a)</td><td>13.89 (n/a)</td><td>9.30 (n/a)</td><td>3.81 (n/a)</td><td>451.10 (n/a)</td><td>313.40 (n/a)</td><td>302.00 (n/a)</td><td>218.60 (n/a)</td><td>89.93 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>3.28 (+5.13%)</td><td>2.61 (-10.49%)</td><td>2.48 (-16.29%)</td><td>2.17 (-17.26%)</td><td>0.41 <b>(+107.23%)</b></td><td>241.10 <b>(+20.85%)</b></td><td>204.70 (+13.32%)</td><td>211.20 (+19.46%)</td><td>159.80 (-4.94%)</td><td>29.39 <b>(+131.75%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>3.12 (n/a)</td><td>2.91 (n/a)</td><td>2.96 (n/a)</td><td>2.63 (n/a)</td><td>0.20 (n/a)</td><td>199.50 (n/a)</td><td>180.64 (n/a)</td><td>176.80 (n/a)</td><td>168.10 (n/a)</td><td>12.68 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>5.84 (+4.49%)</td><td>5.24 (+3.18%)</td><td>5.26 (+3.92%)</td><td>4.59 (-0.64%)</td><td>0.51 <b>(+26.44%)</b></td><td>228.20 (+0.62%)</td><td>201.56 (-2.83%)</td><td>199.20 (-3.77%)</td><td>179.70 (-4.31%)</td><td>20.05 <b>(+21.24%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>5.58 (n/a)</td><td>5.08 (n/a)</td><td>5.07 (n/a)</td><td>4.62 (n/a)</td><td>0.41 (n/a)</td><td>226.80 (n/a)</td><td>207.44 (n/a)</td><td>207.00 (n/a)</td><td>187.80 (n/a)</td><td>16.54 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>9.33 (+2.77%)</td><td>7.63 (+1.57%)</td><td>7.78 (+6.19%)</td><td>6.15 (+7.50%)</td><td>1.16 (-13.71%)</td><td>341.00 (-6.96%)</td><td>279.96 (-2.38%)</td><td>269.50 (-5.84%)</td><td>224.70 (-2.69%)</td><td>42.55 <b>(-21.13%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>9.08 (n/a)</td><td>7.51 (n/a)</td><td>7.33 (n/a)</td><td>5.72 (n/a)</td><td>1.35 (n/a)</td><td>366.50 (n/a)</td><td>286.80 (n/a)</td><td>286.20 (n/a)</td><td>230.90 (n/a)</td><td>53.95 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>3.42 (+7.36%)</td><td>2.69 (-1.00%)</td><td>2.67 (-10.43%)</td><td>2.19 <b>(+46.58%)</b></td><td>0.45 <b>(-34.58%)</b></td><td>239.90 <b>(-31.79%)</b></td><td>199.02 (-4.85%)</td><td>196.70 (+11.63%)</td><td>153.50 (-6.86%)</td><td>31.19 <b>(-60.94%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.18 (n/a)</td><td>2.72 (n/a)</td><td>2.98 (n/a)</td><td>1.49 (n/a)</td><td>0.69 (n/a)</td><td>351.70 (n/a)</td><td>209.16 (n/a)</td><td>176.20 (n/a)</td><td>164.80 (n/a)</td><td>79.85 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>3.62 (+8.66%)</td><td>2.99 (+8.96%)</td><td>2.88 (-3.12%)</td><td>2.46 (+15.03%)</td><td>0.50 (-0.51%)</td><td>213.50 (-13.07%)</td><td>179.30 (-8.81%)</td><td>182.30 (+3.23%)</td><td>144.70 (-7.95%)</td><td>29.51 <b>(-22.27%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>3.33 (n/a)</td><td>2.74 (n/a)</td><td>2.97 (n/a)</td><td>2.13 (n/a)</td><td>0.51 (n/a)</td><td>245.60 (n/a)</td><td>196.62 (n/a)</td><td>176.60 (n/a)</td><td>157.20 (n/a)</td><td>37.97 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>3.35 (+11.05%)</td><td>2.64 (-8.02%)</td><td>2.64 (-12.30%)</td><td>2.18 (-9.18%)</td><td>0.45 <b>(+68.04%)</b></td><td>240.20 (+10.13%)</td><td>202.52 (+10.20%)</td><td>198.70 (+14.06%)</td><td>156.50 (-9.95%)</td><td>31.72 <b>(+64.35%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>3.02 (n/a)</td><td>2.87 (n/a)</td><td>3.01 (n/a)</td><td>2.40 (n/a)</td><td>0.27 (n/a)</td><td>218.10 (n/a)</td><td>183.78 (n/a)</td><td>174.20 (n/a)</td><td>173.80 (n/a)</td><td>19.30 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.27 (+1.77%)</td><td>0.22 (-3.49%)</td><td>0.24 (+3.58%)</td><td>0.17 (+5.86%)</td><td>0.05 (+16.31%)</td><td>194.00 (-5.55%)</td><td>153.46 (+4.61%)</td><td>134.50 (-3.52%)</td><td>120.60 (-1.79%)</td><td>37.31 (+9.70%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>205.40 (n/a)</td><td>146.70 (n/a)</td><td>139.40 (n/a)</td><td>122.80 (n/a)</td><td>34.01 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (-2.71%)</td><td>0.22 (-4.17%)</td><td>0.21 (-2.48%)</td><td>0.13 (-19.03%)</td><td>0.07 (+16.95%)</td><td>252.00 <b>(+23.47%)</b></td><td>166.80 (+8.26%)</td><td>153.70 (+2.60%)</td><td>108.40 (+2.75%)</td><td>57.68 <b>(+48.01%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>204.10 (n/a)</td><td>154.08 (n/a)</td><td>149.80 (n/a)</td><td>105.50 (n/a)</td><td>38.97 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.25 (+11.80%)</td><td>0.19 (-1.15%)</td><td>0.20 (-4.77%)</td><td>0.14 (-2.11%)</td><td>0.04 <b>(+41.61%)</b></td><td>228.60 (+2.14%)</td><td>179.36 (+3.28%)</td><td>163.50 (+5.01%)</td><td>133.30 (-10.54%)</td><td>42.52 <b>(+34.60%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>223.80 (n/a)</td><td>173.66 (n/a)</td><td>155.70 (n/a)</td><td>149.00 (n/a)</td><td>31.59 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.30 (+10.75%)</td><td>0.24 (+16.62%)</td><td>0.25 <b>(+23.01%)</b></td><td>0.17 (+5.41%)</td><td>0.05 <b>(+22.12%)</b></td><td>197.30 (-5.14%)</td><td>142.28 (-13.43%)</td><td>128.60 (-18.71%)</td><td>110.80 (-9.70%)</td><td>34.24 (+6.74%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>208.00 (n/a)</td><td>164.36 (n/a)</td><td>158.20 (n/a)</td><td>122.70 (n/a)</td><td>32.08 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.51 <b>(+27.82%)</b></td><td>0.38 (+6.49%)</td><td>0.40 (+9.73%)</td><td>0.30 (-8.24%)</td><td>0.08 <b>(+207.92%)</b></td><td>215.70 (+8.99%)</td><td>176.48 (-3.15%)</td><td>165.50 (-8.87%)</td><td>128.20 <b>(-21.73%)</b></td><td>35.76 <b>(+167.28%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.03 (n/a)</td><td>197.90 (n/a)</td><td>182.22 (n/a)</td><td>181.60 (n/a)</td><td>163.80 (n/a)</td><td>13.38 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.57 (+7.51%)</td><td>0.41 (-6.98%)</td><td>0.38 (-15.71%)</td><td>0.35 (+10.51%)</td><td>0.09 (+10.99%)</td><td>187.30 (-9.52%)</td><td>165.30 (+7.53%)</td><td>172.10 (+18.61%)</td><td>115.70 (-6.99%)</td><td>29.42 (-9.54%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.53 (n/a)</td><td>0.44 (n/a)</td><td>0.45 (n/a)</td><td>0.32 (n/a)</td><td>0.08 (n/a)</td><td>207.00 (n/a)</td><td>153.72 (n/a)</td><td>145.10 (n/a)</td><td>124.40 (n/a)</td><td>32.52 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.51 (+1.37%)</td><td>0.41 (+4.66%)</td><td>0.43 (+18.06%)</td><td>0.30 (-10.12%)</td><td>0.08 (+11.02%)</td><td>218.70 (+11.24%)</td><td>165.02 (-3.64%)</td><td>153.40 (-15.25%)</td><td>128.30 (-1.38%)</td><td>34.89 <b>(+22.56%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.33 (n/a)</td><td>0.07 (n/a)</td><td>196.60 (n/a)</td><td>171.26 (n/a)</td><td>181.00 (n/a)</td><td>130.10 (n/a)</td><td>28.47 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.57 (+14.09%)</td><td>0.41 (+4.91%)</td><td>0.40 (+8.52%)</td><td>0.34 <b>(+22.63%)</b></td><td>0.09 (+0.96%)</td><td>191.20 (-18.43%)</td><td>164.24 (-5.77%)</td><td>165.90 (-7.83%)</td><td>115.60 (-12.36%)</td><td>29.39 <b>(-28.33%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.50 (n/a)</td><td>0.39 (n/a)</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.09 (n/a)</td><td>234.40 (n/a)</td><td>174.30 (n/a)</td><td>180.00 (n/a)</td><td>131.90 (n/a)</td><td>41.01 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.47 (-15.74%)</td><td>0.34 (-4.64%)</td><td>0.37 (+5.57%)</td><td>0.17 (-8.02%)</td><td>0.11 <b>(-24.38%)</b></td><td>380.30 (+8.72%)</td><td>214.52 (+2.02%)</td><td>176.80 (-5.25%)</td><td>139.80 (+18.68%)</td><td>95.64 (+3.90%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.56 (n/a)</td><td>0.36 (n/a)</td><td>0.35 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>349.80 (n/a)</td><td>210.28 (n/a)</td><td>186.60 (n/a)</td><td>117.80 (n/a)</td><td>92.05 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.44 (-8.43%)</td><td>0.35 (-17.74%)</td><td>0.36 (-14.25%)</td><td>0.28 <b>(-25.93%)</b></td><td>0.06 <b>(+56.54%)</b></td><td>233.40 <b>(+34.99%)</b></td><td>189.10 <b>(+23.55%)</b></td><td>180.30 (+16.62%)</td><td>149.30 (+9.22%)</td><td>31.69 <b>(+131.51%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.48 (n/a)</td><td>0.43 (n/a)</td><td>0.42 (n/a)</td><td>0.38 (n/a)</td><td>0.04 (n/a)</td><td>172.90 (n/a)</td><td>153.06 (n/a)</td><td>154.60 (n/a)</td><td>136.70 (n/a)</td><td>13.69 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.05 (+11.01%)</td><td>0.84 (+19.47%)</td><td>0.75 (+10.49%)</td><td>0.69 <b>(+31.50%)</b></td><td>0.17 (+6.81%)</td><td>191.20 <b>(-23.98%)</b></td><td>161.68 (-16.87%)</td><td>175.20 (-9.50%)</td><td>124.30 (-9.86%)</td><td>30.22 <b>(-25.63%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.95 (n/a)</td><td>0.70 (n/a)</td><td>0.68 (n/a)</td><td>0.52 (n/a)</td><td>0.16 (n/a)</td><td>251.50 (n/a)</td><td>194.48 (n/a)</td><td>193.60 (n/a)</td><td>137.90 (n/a)</td><td>40.64 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>1.12 (+10.46%)</td><td>0.82 (-2.73%)</td><td>0.75 (-11.80%)</td><td>0.51 (-17.11%)</td><td>0.25 <b>(+58.42%)</b></td><td>259.40 <b>(+20.65%)</b></td><td>173.04 (+8.00%)</td><td>174.80 (+13.43%)</td><td>116.70 (-9.46%)</td><td>56.79 <b>(+67.47%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.02 (n/a)</td><td>0.84 (n/a)</td><td>0.85 (n/a)</td><td>0.61 (n/a)</td><td>0.16 (n/a)</td><td>215.00 (n/a)</td><td>160.22 (n/a)</td><td>154.10 (n/a)</td><td>128.90 (n/a)</td><td>33.91 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.03 (+11.88%)</td><td>0.79 (-4.04%)</td><td>0.86 (-0.05%)</td><td>0.35 <b>(-50.49%)</b></td><td>0.26 <b>(+176.43%)</b></td><td>369.70 <b>(+101.91%)</b></td><td>191.52 (+19.30%)</td><td>152.50 (+0.07%)</td><td>127.30 (-10.60%)</td><td>100.76 <b>(+430.57%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.92 (n/a)</td><td>0.83 (n/a)</td><td>0.86 (n/a)</td><td>0.72 (n/a)</td><td>0.09 (n/a)</td><td>183.10 (n/a)</td><td>160.54 (n/a)</td><td>152.40 (n/a)</td><td>142.40 (n/a)</td><td>18.99 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>1.08 (+11.42%)</td><td>0.84 (+10.19%)</td><td>0.71 (-5.09%)</td><td>0.68 (+8.35%)</td><td>0.20 <b>(+53.95%)</b></td><td>193.90 (-7.71%)</td><td>162.64 (-7.35%)</td><td>185.40 (+5.34%)</td><td>121.80 (-10.24%)</td><td>35.51 <b>(+27.99%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.97 (n/a)</td><td>0.76 (n/a)</td><td>0.74 (n/a)</td><td>0.62 (n/a)</td><td>0.13 (n/a)</td><td>210.10 (n/a)</td><td>175.54 (n/a)</td><td>176.00 (n/a)</td><td>135.70 (n/a)</td><td>27.74 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>1.13 (-13.94%)</td><td>0.85 (-13.29%)</td><td>0.75 (-9.00%)</td><td>0.67 (-14.63%)</td><td>0.21 (-16.85%)</td><td>195.50 (+17.14%)</td><td>160.70 (+14.92%)</td><td>175.60 (+9.89%)</td><td>115.70 (+16.16%)</td><td>36.40 (+11.84%)</td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>1.32 (n/a)</td><td>0.98 (n/a)</td><td>0.82 (n/a)</td><td>0.79 (n/a)</td><td>0.25 (n/a)</td><td>166.90 (n/a)</td><td>139.84 (n/a)</td><td>159.80 (n/a)</td><td>99.60 (n/a)</td><td>32.54 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.91 (-7.72%)</td><td>0.75 (-7.56%)</td><td>0.74 (-7.43%)</td><td>0.61 (-12.47%)</td><td>0.15 <b>(+21.75%)</b></td><td>216.40 (+14.26%)</td><td>179.28 (+9.66%)</td><td>177.30 (+8.04%)</td><td>144.10 (+8.35%)</td><td>34.73 <b>(+49.32%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.99 (n/a)</td><td>0.82 (n/a)</td><td>0.80 (n/a)</td><td>0.69 (n/a)</td><td>0.12 (n/a)</td><td>189.40 (n/a)</td><td>163.48 (n/a)</td><td>164.10 (n/a)</td><td>133.00 (n/a)</td><td>23.26 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.76 (-11.87%)</td><td>0.66 (-13.82%)</td><td>0.63 <b>(-24.40%)</b></td><td>0.58 (-2.34%)</td><td>0.08 <b>(-34.41%)</b></td><td>224.90 (+2.37%)</td><td>201.76 (+14.87%)</td><td>209.20 <b>(+32.32%)</b></td><td>172.00 (+13.53%)</td><td>22.50 <b>(-23.48%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.86 (n/a)</td><td>0.76 (n/a)</td><td>0.83 (n/a)</td><td>0.60 (n/a)</td><td>0.12 (n/a)</td><td>219.70 (n/a)</td><td>175.64 (n/a)</td><td>158.10 (n/a)</td><td>151.50 (n/a)</td><td>29.40 (n/a)</td>
</tr>
</tbody>
</table>


### test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8]

<table>
<thead>
<tr>
<th>Commit/Date</th>
<th>Bandwidth (max)</th><th>Bandwidth (mean)</th><th>Bandwidth (median)</th><th>Bandwidth (min)</th><th>Bandwidth (stddev)</th><th>Latency (max)</th><th>Latency (mean)</th><th>Latency (median)</th><th>Latency (min)</th><th>Latency (stddev)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.87 <b>(-30.80%)</b></td><td>0.68 <b>(-25.14%)</b></td><td>0.68 <b>(-20.51%)</b></td><td>0.48 <b>(-24.02%)</b></td><td>0.14 <b>(-45.20%)</b></td><td>271.50 <b>(+31.60%)</b></td><td>199.46 <b>(+30.35%)</b></td><td>193.20 <b>(+25.78%)</b></td><td>149.90 <b>(+44.55%)</b></td><td>44.25 (+7.66%)</td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>1.26 (n/a)</td><td>0.91 (n/a)</td><td>0.85 (n/a)</td><td>0.64 (n/a)</td><td>0.25 (n/a)</td><td>206.30 (n/a)</td><td>153.02 (n/a)</td><td>153.60 (n/a)</td><td>103.70 (n/a)</td><td>41.10 (n/a)</td>
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
<td><code>2191fe0</code> — 2026-09-14 20:47:52</td><td>0.13 (+8.95%)</td><td>0.10 (+5.57%)</td><td>0.10 (+0.46%)</td><td>0.08 <b>(+25.94%)</b></td><td>0.02 (-12.44%)</td><td>195.50 <b>(-20.59%)</b></td><td>166.56 (-6.88%)</td><td>164.30 (-0.48%)</td><td>129.40 (-8.23%)</td><td>27.08 <b>(-35.89%)</b></td>
</tr>
<tr>
<td><code>cd5840c</code> — 2026-09-12 02:58:34</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>246.20 (n/a)</td><td>178.86 (n/a)</td><td>165.10 (n/a)</td><td>141.00 (n/a)</td><td>42.24 (n/a)</td>
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
<td><code>4bb8427</code> — 2026-06-23 22:46:41</td><td>0.13 (+5.28%)</td><td>0.10 (-6.35%)</td><td>0.10 (-9.66%)</td><td>0.07 (-18.86%)</td><td>0.02 <b>(+61.29%)</b></td><td>226.90 <b>(+23.25%)</b></td><td>174.48 (+9.64%)</td><td>170.10 (+10.67%)</td><td>128.50 (-5.03%)</td><td>38.92 <b>(+86.83%)</b></td>
</tr>
<tr>
<td><code>4d4b803</code> — 2026-06-22 18:13:44</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>159.14 (n/a)</td><td>153.70 (n/a)</td><td>135.30 (n/a)</td><td>20.83 (n/a)</td>
</tr>
</tbody>
</table>


</details>
