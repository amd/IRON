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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (+6.89%)</td><td>0.05 <b>(+22.56%)</b></td><td>0.05 <b>(+28.84%)</b></td><td>0.04 <b>(+26.19%)</b></td><td>0.01 <b>(-23.65%)</b></td><td>162.50 <b>(-20.77%)</b></td><td>136.24 (-19.85%)</td><td>126.90 <b>(-22.39%)</b></td><td>120.10 (-6.46%)</td><td>17.99 <b>(-45.01%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>169.98 (n/a)</td><td>163.50 (n/a)</td><td>128.40 (n/a)</td><td>32.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (-4.42%)</td><td>0.04 (+16.51%)</td><td>0.04 <b>(+34.89%)</b></td><td>0.03 <b>(+28.32%)</b></td><td>0.00 <b>(-54.84%)</b></td><td>183.10 <b>(-22.05%)</b></td><td>165.44 (-16.36%)</td><td>157.60 <b>(-25.87%)</b></td><td>153.60 (+4.63%)</td><td>13.66 <b>(-63.13%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.90 (n/a)</td><td>197.80 (n/a)</td><td>212.60 (n/a)</td><td>146.80 (n/a)</td><td>37.05 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 <b>(+43.63%)</b></td><td>0.04 <b>(+22.27%)</b></td><td>0.04 <b>(+32.85%)</b></td><td>0.02 (-14.20%)</td><td>0.01 <b>(+232.53%)</b></td><td>252.60 (+16.51%)</td><td>172.82 (-14.08%)</td><td>157.20 <b>(-24.75%)</b></td><td>124.10 <b>(-30.36%)</b></td><td>48.81 <b>(+177.11%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>216.80 (n/a)</td><td>201.14 (n/a)</td><td>208.90 (n/a)</td><td>178.20 (n/a)</td><td>17.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (+9.05%)</td><td>0.04 (+6.21%)</td><td>0.04 (+8.97%)</td><td>0.03 (+5.90%)</td><td>0.01 (+11.91%)</td><td>184.60 (-5.58%)</td><td>159.24 (-5.73%)</td><td>154.80 (-8.24%)</td><td>127.30 (-8.29%)</td><td>22.50 (-3.45%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.50 (n/a)</td><td>168.92 (n/a)</td><td>168.70 (n/a)</td><td>138.80 (n/a)</td><td>23.30 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 <b>(+51.88%)</b></td><td>0.04 <b>(+42.67%)</b></td><td>0.05 <b>(+44.69%)</b></td><td>0.03 (+10.66%)</td><td>0.01 <b>(+147.92%)</b></td><td>223.70 (-9.62%)</td><td>150.80 <b>(-27.47%)</b></td><td>136.40 <b>(-30.87%)</b></td><td>122.40 <b>(-34.16%)</b></td><td>41.31 <b>(+56.22%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>247.50 (n/a)</td><td>207.92 (n/a)</td><td>197.30 (n/a)</td><td>185.90 (n/a)</td><td>26.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 <b>(+46.22%)</b></td><td>0.04 <b>(+31.63%)</b></td><td>0.04 (+9.25%)</td><td>0.03 <b>(+26.31%)</b></td><td>0.01 <b>(+117.02%)</b></td><td>183.40 <b>(-20.85%)</b></td><td>157.40 <b>(-22.83%)</b></td><td>173.20 (-8.46%)</td><td>125.40 <b>(-31.59%)</b></td><td>27.51 (+14.93%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>231.70 (n/a)</td><td>203.96 (n/a)</td><td>189.20 (n/a)</td><td>183.30 (n/a)</td><td>23.94 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (+11.70%)</td><td>0.04 <b>(+25.58%)</b></td><td>0.04 <b>(+45.30%)</b></td><td>0.03 <b>(+27.91%)</b></td><td>0.01 (+1.58%)</td><td>185.50 <b>(-21.83%)</b></td><td>153.50 <b>(-20.93%)</b></td><td>138.50 <b>(-31.20%)</b></td><td>133.90 (-10.43%)</td><td>24.32 <b>(-28.90%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.30 (n/a)</td><td>194.12 (n/a)</td><td>201.30 (n/a)</td><td>149.50 (n/a)</td><td>34.21 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 <b>(+32.00%)</b></td><td>0.04 (+11.98%)</td><td>0.03 (-2.41%)</td><td>0.03 (+19.85%)</td><td>0.01 <b>(+53.67%)</b></td><td>183.20 (-16.54%)</td><td>164.08 (-10.01%)</td><td>175.60 (+2.45%)</td><td>120.80 <b>(-24.26%)</b></td><td>25.87 (-2.65%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>219.50 (n/a)</td><td>182.34 (n/a)</td><td>171.40 (n/a)</td><td>159.50 (n/a)</td><td>26.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (-12.69%)</td><td>0.08 (+12.80%)</td><td>0.09 <b>(+28.61%)</b></td><td>0.06 (+8.84%)</td><td>0.01 <b>(-37.04%)</b></td><td>196.20 (-8.15%)</td><td>151.80 (-13.54%)</td><td>140.00 <b>(-22.27%)</b></td><td>131.60 (+14.53%)</td><td>26.22 <b>(-29.56%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>213.60 (n/a)</td><td>175.58 (n/a)</td><td>180.10 (n/a)</td><td>114.90 (n/a)</td><td>37.23 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 <b>(+53.36%)</b></td><td>0.09 <b>(+31.46%)</b></td><td>0.09 <b>(+27.79%)</b></td><td>0.06 (-6.97%)</td><td>0.02 <b>(+395.14%)</b></td><td>210.20 (+7.52%)</td><td>142.28 (-19.79%)</td><td>135.80 <b>(-21.77%)</b></td><td>108.80 <b>(-34.81%)</b></td><td>41.11 <b>(+246.74%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>195.50 (n/a)</td><td>177.38 (n/a)</td><td>173.60 (n/a)</td><td>166.90 (n/a)</td><td>11.85 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 <b>(+32.73%)</b></td><td>0.08 (+13.56%)</td><td>0.08 (+18.13%)</td><td>0.05 (-14.55%)</td><td>0.02 <b>(+226.34%)</b></td><td>248.70 (+17.04%)</td><td>174.00 (-6.80%)</td><td>153.50 (-15.33%)</td><td>125.50 <b>(-24.62%)</b></td><td>51.14 <b>(+187.60%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>186.70 (n/a)</td><td>181.30 (n/a)</td><td>166.50 (n/a)</td><td>17.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (-3.72%)</td><td>0.08 (+10.86%)</td><td>0.08 (+14.81%)</td><td>0.07 (+19.85%)</td><td>0.01 <b>(-37.69%)</b></td><td>179.50 (-16.59%)</td><td>157.56 (-12.50%)</td><td>162.90 (-12.89%)</td><td>124.40 (+3.93%)</td><td>20.52 <b>(-47.35%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>215.20 (n/a)</td><td>180.06 (n/a)</td><td>187.00 (n/a)</td><td>119.70 (n/a)</td><td>38.98 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (+6.87%)</td><td>0.07 (-3.85%)</td><td>0.06 (-16.51%)</td><td>0.05 (-1.16%)</td><td>0.02 (+12.48%)</td><td>247.40 (+1.14%)</td><td>194.56 (+4.53%)</td><td>201.10 (+19.77%)</td><td>126.50 (-6.43%)</td><td>44.66 (+0.09%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>244.60 (n/a)</td><td>186.12 (n/a)</td><td>167.90 (n/a)</td><td>135.20 (n/a)</td><td>44.62 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (-14.47%)</td><td>0.08 (+8.75%)</td><td>0.07 <b>(+23.66%)</b></td><td>0.07 <b>(+21.07%)</b></td><td>0.02 <b>(-43.28%)</b></td><td>185.40 (-17.38%)</td><td>158.74 (-13.10%)</td><td>165.80 (-19.12%)</td><td>119.60 (+16.91%)</td><td>28.41 <b>(-43.73%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>224.40 (n/a)</td><td>182.66 (n/a)</td><td>205.00 (n/a)</td><td>102.30 (n/a)</td><td>50.48 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 <b>(+31.19%)</b></td><td>0.06 (-1.46%)</td><td>0.06 (-3.40%)</td><td>0.05 (-13.11%)</td><td>0.02 <b>(+158.57%)</b></td><td>257.80 (+15.09%)</td><td>212.52 (+5.88%)</td><td>217.20 (+3.53%)</td><td>134.70 <b>(-23.77%)</b></td><td>47.32 <b>(+121.16%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.00 (n/a)</td><td>200.72 (n/a)</td><td>209.80 (n/a)</td><td>176.70 (n/a)</td><td>21.40 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 <b>(+49.80%)</b></td><td>0.07 <b>(+22.12%)</b></td><td>0.06 (-0.44%)</td><td>0.06 (+9.27%)</td><td>0.02 <b>(+230.94%)</b></td><td>216.10 (-8.47%)</td><td>181.90 (-13.74%)</td><td>212.40 (+0.43%)</td><td>118.80 <b>(-33.22%)</b></td><td>45.92 <b>(+113.76%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>236.10 (n/a)</td><td>210.88 (n/a)</td><td>211.50 (n/a)</td><td>177.90 (n/a)</td><td>21.48 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (-14.63%)</td><td>0.14 (-11.77%)</td><td>0.13 (-0.22%)</td><td>0.09 (-8.31%)</td><td>0.04 <b>(-24.48%)</b></td><td>259.90 (+9.06%)</td><td>189.66 (+11.09%)</td><td>187.30 (+0.21%)</td><td>129.90 (+17.13%)</td><td>52.23 (-0.65%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>238.30 (n/a)</td><td>170.72 (n/a)</td><td>186.90 (n/a)</td><td>110.90 (n/a)</td><td>52.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.17 (+9.00%)</td><td>0.14 (+11.34%)</td><td>0.16 <b>(+24.08%)</b></td><td>0.10 (-8.84%)</td><td>0.03 <b>(+53.45%)</b></td><td>255.50 (+9.66%)</td><td>180.68 (-7.82%)</td><td>154.50 (-19.45%)</td><td>143.10 (-8.27%)</td><td>46.69 <b>(+54.35%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>233.00 (n/a)</td><td>196.00 (n/a)</td><td>191.80 (n/a)</td><td>156.00 (n/a)</td><td>30.25 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (+4.10%)</td><td>0.16 (+8.68%)</td><td>0.17 (+14.14%)</td><td>0.09 (-0.99%)</td><td>0.05 <b>(+23.44%)</b></td><td>278.70 (+1.01%)</td><td>174.22 (-5.16%)</td><td>148.80 (-12.42%)</td><td>117.30 (-3.93%)</td><td>65.97 (+16.81%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>275.90 (n/a)</td><td>183.70 (n/a)</td><td>169.90 (n/a)</td><td>122.10 (n/a)</td><td>56.48 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.18 (+5.82%)</td><td>0.15 (+7.55%)</td><td>0.17 (+9.55%)</td><td>0.10 (-9.15%)</td><td>0.03 <b>(+35.58%)</b></td><td>236.90 (+10.08%)</td><td>166.02 (-5.27%)</td><td>148.90 (-8.71%)</td><td>138.20 (-5.47%)</td><td>40.83 <b>(+43.05%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>215.20 (n/a)</td><td>175.26 (n/a)</td><td>163.10 (n/a)</td><td>146.20 (n/a)</td><td>28.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 <b>(+26.67%)</b></td><td>0.16 <b>(+23.22%)</b></td><td>0.17 <b>(+31.46%)</b></td><td>0.10 (-12.30%)</td><td>0.04 <b>(+138.01%)</b></td><td>257.80 (+14.02%)</td><td>164.56 (-14.64%)</td><td>148.40 <b>(-23.94%)</b></td><td>130.20 <b>(-21.04%)</b></td><td>53.14 <b>(+121.68%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>226.10 (n/a)</td><td>192.78 (n/a)</td><td>195.10 (n/a)</td><td>164.90 (n/a)</td><td>23.97 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (+7.53%)</td><td>0.17 <b>(+20.01%)</b></td><td>0.18 <b>(+35.48%)</b></td><td>0.14 <b>(+22.94%)</b></td><td>0.02 (-19.27%)</td><td>180.00 (-18.66%)</td><td>143.82 (-18.07%)</td><td>134.10 <b>(-26.20%)</b></td><td>126.70 (-7.04%)</td><td>22.40 <b>(-37.61%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>221.30 (n/a)</td><td>175.54 (n/a)</td><td>181.70 (n/a)</td><td>136.30 (n/a)</td><td>35.90 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (+11.18%)</td><td>0.15 <b>(+29.41%)</b></td><td>0.15 <b>(+39.85%)</b></td><td>0.11 <b>(+51.00%)</b></td><td>0.02 <b>(-35.30%)</b></td><td>221.80 <b>(-33.77%)</b></td><td>171.58 <b>(-26.41%)</b></td><td>160.60 <b>(-28.50%)</b></td><td>150.50 (-10.04%)</td><td>28.60 <b>(-58.89%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>334.90 (n/a)</td><td>233.16 (n/a)</td><td>224.60 (n/a)</td><td>167.30 (n/a)</td><td>69.58 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (-1.49%)</td><td>0.16 (+12.58%)</td><td>0.16 (+17.94%)</td><td>0.12 <b>(+23.49%)</b></td><td>0.03 <b>(-29.73%)</b></td><td>202.10 (-19.03%)</td><td>158.20 (-13.87%)</td><td>157.00 (-15.18%)</td><td>130.90 (+1.47%)</td><td>27.69 <b>(-41.35%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>249.60 (n/a)</td><td>183.68 (n/a)</td><td>185.10 (n/a)</td><td>129.00 (n/a)</td><td>47.21 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.38 <b>(+21.48%)</b></td><td>0.33 <b>(+31.68%)</b></td><td>0.32 <b>(+27.41%)</b></td><td>0.27 <b>(+53.46%)</b></td><td>0.05 (-0.51%)</td><td>183.30 <b>(-34.84%)</b></td><td>153.12 <b>(-25.36%)</b></td><td>154.10 <b>(-21.50%)</b></td><td>128.90 (-17.69%)</td><td>23.24 <b>(-49.49%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>281.30 (n/a)</td><td>205.14 (n/a)</td><td>196.30 (n/a)</td><td>156.60 (n/a)</td><td>46.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.42 <b>(+36.92%)</b></td><td>0.37 <b>(+46.44%)</b></td><td>0.38 <b>(+51.70%)</b></td><td>0.29 <b>(+37.25%)</b></td><td>0.05 <b>(+25.84%)</b></td><td>168.60 <b>(-27.17%)</b></td><td>134.34 <b>(-31.90%)</b></td><td>130.90 <b>(-34.09%)</b></td><td>117.70 <b>(-26.94%)</b></td><td>20.17 <b>(-32.03%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>231.50 (n/a)</td><td>197.28 (n/a)</td><td>198.60 (n/a)</td><td>161.10 (n/a)</td><td>29.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.38 (+10.94%)</td><td>0.32 (+8.26%)</td><td>0.31 (+7.62%)</td><td>0.28 <b>(+21.42%)</b></td><td>0.04 (-5.24%)</td><td>177.10 (-17.63%)</td><td>157.78 (-8.25%)</td><td>160.30 (-7.07%)</td><td>128.30 (-9.84%)</td><td>19.30 <b>(-30.50%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>215.00 (n/a)</td><td>171.96 (n/a)</td><td>172.50 (n/a)</td><td>142.30 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.41 <b>(+37.31%)</b></td><td>0.34 <b>(+33.73%)</b></td><td>0.37 <b>(+56.91%)</b></td><td>0.23 (+11.87%)</td><td>0.08 <b>(+128.21%)</b></td><td>210.10 (-10.60%)</td><td>154.84 <b>(-22.30%)</b></td><td>132.70 <b>(-36.26%)</b></td><td>119.10 <b>(-27.16%)</b></td><td>41.78 <b>(+49.41%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>235.00 (n/a)</td><td>199.28 (n/a)</td><td>208.20 (n/a)</td><td>163.50 (n/a)</td><td>27.96 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.31 (-8.11%)</td><td>0.25 (-9.84%)</td><td>0.24 (-17.78%)</td><td>0.19 (-0.96%)</td><td>0.04 <b>(-33.05%)</b></td><td>260.00 (+0.97%)</td><td>204.62 (+8.09%)</td><td>206.20 <b>(+21.65%)</b></td><td>158.20 (+8.80%)</td><td>37.05 <b>(-25.33%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>257.50 (n/a)</td><td>189.30 (n/a)</td><td>169.50 (n/a)</td><td>145.40 (n/a)</td><td>49.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.41 <b>(+42.73%)</b></td><td>0.32 <b>(+29.98%)</b></td><td>0.32 <b>(+26.38%)</b></td><td>0.19 (-12.94%)</td><td>0.09 <b>(+175.51%)</b></td><td>264.80 (+14.88%)</td><td>165.22 (-17.85%)</td><td>151.70 <b>(-20.87%)</b></td><td>119.80 <b>(-29.94%)</b></td><td>58.59 <b>(+120.75%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>230.50 (n/a)</td><td>201.12 (n/a)</td><td>191.70 (n/a)</td><td>171.00 (n/a)</td><td>26.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.31 (-5.55%)</td><td>0.26 (+15.91%)</td><td>0.27 <b>(+21.46%)</b></td><td>0.21 <b>(+36.46%)</b></td><td>0.04 <b>(-41.18%)</b></td><td>238.10 <b>(-26.72%)</b></td><td>190.26 (-17.75%)</td><td>182.10 (-17.68%)</td><td>157.00 (+5.87%)</td><td>30.63 <b>(-53.30%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.33 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>324.90 (n/a)</td><td>231.32 (n/a)</td><td>221.20 (n/a)</td><td>148.30 (n/a)</td><td>65.59 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.39 (+14.71%)</td><td>0.31 <b>(+25.36%)</b></td><td>0.31 <b>(+36.04%)</b></td><td>0.26 <b>(+31.79%)</b></td><td>0.06 (-4.59%)</td><td>190.20 <b>(-24.10%)</b></td><td>161.88 <b>(-21.31%)</b></td><td>156.70 <b>(-26.47%)</b></td><td>124.60 (-12.87%)</td><td>27.12 <b>(-34.03%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>250.60 (n/a)</td><td>205.72 (n/a)</td><td>213.10 (n/a)</td><td>143.00 (n/a)</td><td>41.11 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (-11.80%)</td><td>0.02 (-6.50%)</td><td>0.02 (-7.88%)</td><td>0.01 (-14.97%)</td><td>0.00 (+1.52%)</td><td>211.50 (+17.63%)</td><td>161.34 (+7.65%)</td><td>157.00 (+8.50%)</td><td>137.50 (+13.36%)</td><td>29.73 <b>(+37.33%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>179.80 (n/a)</td><td>149.88 (n/a)</td><td>144.70 (n/a)</td><td>121.30 (n/a)</td><td>21.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (+3.35%)</td><td>0.02 (+5.15%)</td><td>0.02 (-0.83%)</td><td>0.01 <b>(+27.85%)</b></td><td>0.00 (-18.93%)</td><td>183.50 <b>(-21.78%)</b></td><td>161.60 (-7.12%)</td><td>166.70 (+0.85%)</td><td>119.50 (-3.32%)</td><td>24.86 <b>(-40.74%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>234.60 (n/a)</td><td>173.98 (n/a)</td><td>165.30 (n/a)</td><td>123.60 (n/a)</td><td>41.96 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (-3.34%)</td><td>0.02 (+7.94%)</td><td>0.02 (+18.14%)</td><td>0.01 (+4.51%)</td><td>0.00 (-13.21%)</td><td>192.80 (-4.32%)</td><td>146.80 (-8.08%)</td><td>131.50 (-15.38%)</td><td>127.30 (+3.50%)</td><td>27.37 (-13.93%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>201.50 (n/a)</td><td>159.70 (n/a)</td><td>155.40 (n/a)</td><td>123.00 (n/a)</td><td>31.80 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (-7.17%)</td><td>0.01 (-10.95%)</td><td>0.01 (-7.28%)</td><td>0.01 (-16.64%)</td><td>0.00 (+0.29%)</td><td>242.80 (+19.96%)</td><td>188.62 (+13.61%)</td><td>191.60 (+7.88%)</td><td>119.60 (+7.75%)</td><td>45.93 <b>(+27.22%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>202.40 (n/a)</td><td>166.02 (n/a)</td><td>177.60 (n/a)</td><td>111.00 (n/a)</td><td>36.10 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (-7.61%)</td><td>0.02 (-8.94%)</td><td>0.02 <b>(-22.14%)</b></td><td>0.01 <b>(+83.73%)</b></td><td>0.00 <b>(-48.92%)</b></td><td>201.70 <b>(-45.57%)</b></td><td>169.36 (-6.49%)</td><td>166.50 <b>(+28.47%)</b></td><td>121.60 (+8.28%)</td><td>31.55 <b>(-70.96%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>370.60 (n/a)</td><td>181.12 (n/a)</td><td>129.60 (n/a)</td><td>112.30 (n/a)</td><td>108.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (+14.28%)</td><td>0.01 (+1.86%)</td><td>0.01 (-5.98%)</td><td>0.01 (+5.83%)</td><td>0.00 <b>(+51.61%)</b></td><td>200.00 (-5.53%)</td><td>179.92 (-0.94%)</td><td>192.70 (+6.35%)</td><td>139.30 (-12.50%)</td><td>26.08 <b>(+26.57%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>211.70 (n/a)</td><td>181.62 (n/a)</td><td>181.20 (n/a)</td><td>159.20 (n/a)</td><td>20.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (+19.45%)</td><td>0.01 (+0.52%)</td><td>0.01 (-14.93%)</td><td>0.01 <b>(+20.77%)</b></td><td>0.00 (+5.41%)</td><td>223.80 (-17.17%)</td><td>192.34 (-1.69%)</td><td>203.00 (+17.54%)</td><td>129.50 (-16.29%)</td><td>36.30 <b>(-28.55%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>270.20 (n/a)</td><td>195.64 (n/a)</td><td>172.70 (n/a)</td><td>154.70 (n/a)</td><td>50.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.01 <b>(-22.72%)</b></td><td>0.01 (-8.75%)</td><td>0.01 (-15.90%)</td><td>0.01 (+16.98%)</td><td>0.00 <b>(-69.73%)</b></td><td>242.00 (-14.52%)</td><td>228.62 (+6.08%)</td><td>235.60 (+18.87%)</td><td>210.00 <b>(+29.39%)</b></td><td>15.44 <b>(-66.86%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>283.10 (n/a)</td><td>215.52 (n/a)</td><td>198.20 (n/a)</td><td>162.30 (n/a)</td><td>46.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 <b>(-25.31%)</b></td><td>0.03 (-17.41%)</td><td>0.03 (-13.02%)</td><td>0.02 <b>(-28.85%)</b></td><td>0.00 (-12.40%)</td><td>243.80 <b>(+40.52%)</b></td><td>188.40 <b>(+21.77%)</b></td><td>178.00 (+14.99%)</td><td>170.50 <b>(+33.83%)</b></td><td>31.22 <b>(+66.21%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>173.50 (n/a)</td><td>154.72 (n/a)</td><td>154.80 (n/a)</td><td>127.40 (n/a)</td><td>18.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 <b>(-21.85%)</b></td><td>0.03 (-8.99%)</td><td>0.03 (-13.16%)</td><td>0.03 (+3.86%)</td><td>0.00 <b>(-68.86%)</b></td><td>182.50 (-3.74%)</td><td>167.40 (+7.71%)</td><td>168.70 (+15.15%)</td><td>157.40 <b>(+27.97%)</b></td><td>9.88 <b>(-62.12%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>189.60 (n/a)</td><td>155.42 (n/a)</td><td>146.50 (n/a)</td><td>123.00 (n/a)</td><td>26.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (-9.02%)</td><td>0.03 (-5.23%)</td><td>0.03 (-8.38%)</td><td>0.03 (+5.40%)</td><td>0.01 <b>(-20.63%)</b></td><td>205.80 (-5.12%)</td><td>174.36 (+4.15%)</td><td>178.40 (+9.11%)</td><td>129.80 (+9.91%)</td><td>30.66 (-16.32%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.90 (n/a)</td><td>167.42 (n/a)</td><td>163.50 (n/a)</td><td>118.10 (n/a)</td><td>36.64 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 <b>(-25.29%)</b></td><td>0.03 (-10.70%)</td><td>0.03 (-0.05%)</td><td>0.02 (-6.91%)</td><td>0.00 <b>(-54.91%)</b></td><td>212.20 (+7.39%)</td><td>177.28 (+9.54%)</td><td>173.10 (+0.06%)</td><td>156.70 <b>(+33.82%)</b></td><td>20.73 <b>(-31.99%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.60 (n/a)</td><td>161.84 (n/a)</td><td>173.00 (n/a)</td><td>117.10 (n/a)</td><td>30.49 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (-9.70%)</td><td>0.03 (-0.23%)</td><td>0.03 (-3.78%)</td><td>0.03 (+6.19%)</td><td>0.00 <b>(-32.66%)</b></td><td>193.70 (-5.83%)</td><td>165.46 (-1.71%)</td><td>161.80 (+3.92%)</td><td>137.10 (+10.74%)</td><td>24.15 <b>(-31.84%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.70 (n/a)</td><td>168.34 (n/a)</td><td>155.70 (n/a)</td><td>123.80 (n/a)</td><td>35.43 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (-10.07%)</td><td>0.03 (+2.66%)</td><td>0.04 (+7.03%)</td><td>0.03 <b>(+24.43%)</b></td><td>0.01 <b>(-41.20%)</b></td><td>203.80 (-19.61%)</td><td>159.36 (-6.74%)</td><td>148.80 (-6.59%)</td><td>133.10 (+11.19%)</td><td>27.12 <b>(-47.32%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>253.50 (n/a)</td><td>170.88 (n/a)</td><td>159.30 (n/a)</td><td>119.70 (n/a)</td><td>51.47 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-2.83%)</td><td>0.03 (-4.34%)</td><td>0.03 (-5.71%)</td><td>0.02 (+8.33%)</td><td>0.01 (-19.00%)</td><td>250.20 (-7.68%)</td><td>188.78 (+2.71%)</td><td>173.20 (+6.06%)</td><td>153.10 (+2.96%)</td><td>38.21 <b>(-23.90%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>271.00 (n/a)</td><td>183.80 (n/a)</td><td>163.30 (n/a)</td><td>148.70 (n/a)</td><td>50.21 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (+17.46%)</td><td>0.03 (-2.31%)</td><td>0.03 (-14.79%)</td><td>0.02 (+1.36%)</td><td>0.01 <b>(+41.19%)</b></td><td>236.90 (-1.33%)</td><td>198.44 (+3.56%)</td><td>204.00 (+17.38%)</td><td>144.60 (-14.84%)</td><td>35.61 (+17.67%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.10 (n/a)</td><td>191.62 (n/a)</td><td>173.80 (n/a)</td><td>169.80 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.08 (-11.80%)</td><td>0.06 (-10.82%)</td><td>0.06 (-4.80%)</td><td>0.03 <b>(-39.83%)</b></td><td>0.02 (-4.01%)</td><td>402.90 <b>(+66.21%)</b></td><td>210.12 (+19.60%)</td><td>173.60 (+5.02%)</td><td>139.80 (+13.38%)</td><td>108.66 <b>(+100.82%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>242.40 (n/a)</td><td>175.68 (n/a)</td><td>165.30 (n/a)</td><td>123.30 (n/a)</td><td>54.11 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 <b>(-40.31%)</b></td><td>0.06 <b>(-20.27%)</b></td><td>0.06 (-2.89%)</td><td>0.04 (-14.79%)</td><td>0.01 <b>(-60.21%)</b></td><td>236.40 (+17.38%)</td><td>189.68 (+18.54%)</td><td>174.30 (+3.01%)</td><td>149.20 <b>(+67.64%)</b></td><td>36.73 (-17.99%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>201.40 (n/a)</td><td>160.02 (n/a)</td><td>169.20 (n/a)</td><td>89.00 (n/a)</td><td>44.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 <b>(-24.85%)</b></td><td>0.06 <b>(-20.15%)</b></td><td>0.06 (-14.18%)</td><td>0.05 (-11.46%)</td><td>0.01 <b>(-50.69%)</b></td><td>204.60 (+12.91%)</td><td>178.24 <b>(+23.11%)</b></td><td>173.40 (+16.53%)</td><td>152.20 <b>(+33.04%)</b></td><td>20.22 <b>(-24.52%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>181.20 (n/a)</td><td>144.78 (n/a)</td><td>148.80 (n/a)</td><td>114.40 (n/a)</td><td>26.79 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (+1.56%)</td><td>0.06 (+9.40%)</td><td>0.05 (+8.89%)</td><td>0.05 <b>(+39.16%)</b></td><td>0.01 <b>(-28.89%)</b></td><td>229.30 <b>(-28.14%)</b></td><td>185.28 (-13.30%)</td><td>196.20 (-8.15%)</td><td>140.10 (-1.55%)</td><td>36.23 <b>(-49.02%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>319.10 (n/a)</td><td>213.70 (n/a)</td><td>213.60 (n/a)</td><td>142.30 (n/a)</td><td>71.07 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 <b>(-26.91%)</b></td><td>0.06 (-16.81%)</td><td>0.07 (+6.06%)</td><td>0.03 <b>(-41.44%)</b></td><td>0.02 (-6.57%)</td><td>311.80 <b>(+70.76%)</b></td><td>185.60 <b>(+25.75%)</b></td><td>151.00 (-5.68%)</td><td>140.60 <b>(+36.77%)</b></td><td>71.80 <b>(+130.30%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>182.60 (n/a)</td><td>147.60 (n/a)</td><td>160.10 (n/a)</td><td>102.80 (n/a)</td><td>31.18 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (-3.66%)</td><td>0.06 (+0.56%)</td><td>0.06 (-3.34%)</td><td>0.05 <b>(+54.13%)</b></td><td>0.01 <b>(-51.20%)</b></td><td>216.90 <b>(-35.12%)</b></td><td>180.98 (-8.31%)</td><td>175.20 (+3.48%)</td><td>147.10 (+3.81%)</td><td>25.68 <b>(-67.73%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>334.30 (n/a)</td><td>197.38 (n/a)</td><td>169.30 (n/a)</td><td>141.70 (n/a)</td><td>79.59 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 <b>(-28.77%)</b></td><td>0.06 (-10.61%)</td><td>0.06 (+8.28%)</td><td>0.04 <b>(-21.77%)</b></td><td>0.01 <b>(-43.97%)</b></td><td>277.30 <b>(+27.85%)</b></td><td>192.98 (+8.51%)</td><td>183.10 (-7.62%)</td><td>145.90 <b>(+40.42%)</b></td><td>49.90 (+5.24%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>216.90 (n/a)</td><td>177.84 (n/a)</td><td>198.20 (n/a)</td><td>103.90 (n/a)</td><td>47.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (-4.55%)</td><td>0.05 (-5.64%)</td><td>0.05 (+0.13%)</td><td>0.03 (-16.25%)</td><td>0.01 (+1.25%)</td><td>309.50 (+19.41%)</td><td>222.28 (+7.22%)</td><td>222.50 (-0.13%)</td><td>153.80 (+4.77%)</td><td>58.98 <b>(+27.55%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>259.20 (n/a)</td><td>207.32 (n/a)</td><td>222.80 (n/a)</td><td>146.80 (n/a)</td><td>46.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (-14.54%)</td><td>0.12 (+4.40%)</td><td>0.12 (+7.76%)</td><td>0.10 (+16.92%)</td><td>0.01 <b>(-52.60%)</b></td><td>208.80 (-14.50%)</td><td>177.04 (-6.63%)</td><td>171.80 (-7.19%)</td><td>161.00 (+17.01%)</td><td>18.65 <b>(-51.01%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>244.20 (n/a)</td><td>189.62 (n/a)</td><td>185.10 (n/a)</td><td>137.60 (n/a)</td><td>38.06 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (+13.91%)</td><td>0.12 (+4.97%)</td><td>0.13 (+5.04%)</td><td>0.07 <b>(-23.89%)</b></td><td>0.03 <b>(+61.20%)</b></td><td>294.30 <b>(+31.44%)</b></td><td>183.34 (+0.31%)</td><td>163.80 (-4.77%)</td><td>129.80 (-12.24%)</td><td>64.65 <b>(+93.95%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>223.90 (n/a)</td><td>182.78 (n/a)</td><td>172.00 (n/a)</td><td>147.90 (n/a)</td><td>33.33 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 <b>(-37.71%)</b></td><td>0.11 <b>(-25.93%)</b></td><td>0.11 (-19.55%)</td><td>0.08 <b>(-21.67%)</b></td><td>0.01 <b>(-61.77%)</b></td><td>247.10 <b>(+27.70%)</b></td><td>201.42 <b>(+30.74%)</b></td><td>191.20 <b>(+24.32%)</b></td><td>175.20 <b>(+60.59%)</b></td><td>28.16 <b>(-21.82%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>193.50 (n/a)</td><td>154.06 (n/a)</td><td>153.80 (n/a)</td><td>109.10 (n/a)</td><td>36.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (+8.74%)</td><td>0.12 (-6.47%)</td><td>0.12 (-12.81%)</td><td>0.09 (-18.37%)</td><td>0.03 <b>(+105.11%)</b></td><td>224.10 <b>(+22.46%)</b></td><td>177.20 (+10.45%)</td><td>173.00 (+14.72%)</td><td>133.00 (-8.09%)</td><td>40.03 <b>(+132.18%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>183.00 (n/a)</td><td>160.44 (n/a)</td><td>150.80 (n/a)</td><td>144.70 (n/a)</td><td>17.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (-16.28%)</td><td>0.11 (-8.40%)</td><td>0.11 (-11.90%)</td><td>0.10 (-0.98%)</td><td>0.01 <b>(-59.77%)</b></td><td>213.00 (+1.00%)</td><td>188.92 (+7.05%)</td><td>183.80 (+13.53%)</td><td>177.20 (+19.49%)</td><td>14.95 <b>(-52.55%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>210.90 (n/a)</td><td>176.48 (n/a)</td><td>161.90 (n/a)</td><td>148.30 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (+17.53%)</td><td>0.12 (-0.40%)</td><td>0.10 (-19.92%)</td><td>0.10 (+17.76%)</td><td>0.03 (+15.65%)</td><td>206.70 (-15.11%)</td><td>185.36 (+0.36%)</td><td>205.80 <b>(+24.88%)</b></td><td>131.00 (-14.88%)</td><td>32.90 (-14.91%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>243.50 (n/a)</td><td>184.70 (n/a)</td><td>164.80 (n/a)</td><td>153.90 (n/a)</td><td>38.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (-0.93%)</td><td>0.10 (-11.27%)</td><td>0.10 (-14.59%)</td><td>0.07 <b>(-22.39%)</b></td><td>0.02 <b>(+61.86%)</b></td><td>281.10 <b>(+28.89%)</b></td><td>212.94 (+15.98%)</td><td>215.50 (+17.06%)</td><td>156.40 (+0.90%)</td><td>48.24 <b>(+108.33%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>218.10 (n/a)</td><td>183.60 (n/a)</td><td>184.10 (n/a)</td><td>155.00 (n/a)</td><td>23.15 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (-12.08%)</td><td>0.10 (-9.08%)</td><td>0.09 (-14.85%)</td><td>0.09 (+12.44%)</td><td>0.01 <b>(-55.50%)</b></td><td>230.60 (-11.07%)</td><td>216.44 (+7.72%)</td><td>223.70 (+17.43%)</td><td>188.30 (+13.71%)</td><td>16.84 <b>(-55.45%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>259.30 (n/a)</td><td>200.92 (n/a)</td><td>190.50 (n/a)</td><td>165.60 (n/a)</td><td>37.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>167.10 (n/a)</td><td>146.64 (n/a)</td><td>140.60 (n/a)</td><td>128.50 (n/a)</td><td>17.79 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>169.72 (n/a)</td><td>166.40 (n/a)</td><td>122.10 (n/a)</td><td>42.50 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>293.60 (n/a)</td><td>199.66 (n/a)</td><td>177.10 (n/a)</td><td>143.70 (n/a)</td><td>58.37 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>233.50 (n/a)</td><td>197.00 (n/a)</td><td>191.40 (n/a)</td><td>168.10 (n/a)</td><td>29.16 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>164.00 (n/a)</td><td>143.90 (n/a)</td><td>140.30 (n/a)</td><td>32.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>248.90 (n/a)</td><td>184.08 (n/a)</td><td>167.20 (n/a)</td><td>149.70 (n/a)</td><td>40.14 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>224.40 (n/a)</td><td>187.04 (n/a)</td><td>200.50 (n/a)</td><td>134.80 (n/a)</td><td>34.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>217.60 (n/a)</td><td>177.90 (n/a)</td><td>185.10 (n/a)</td><td>121.10 (n/a)</td><td>42.21 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>171.80 (n/a)</td><td>152.78 (n/a)</td><td>162.30 (n/a)</td><td>129.40 (n/a)</td><td>19.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>206.20 (n/a)</td><td>165.00 (n/a)</td><td>162.20 (n/a)</td><td>133.10 (n/a)</td><td>28.77 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>189.10 (n/a)</td><td>172.32 (n/a)</td><td>179.00 (n/a)</td><td>135.80 (n/a)</td><td>21.04 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>255.70 (n/a)</td><td>220.12 (n/a)</td><td>215.90 (n/a)</td><td>176.60 (n/a)</td><td>30.20 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.30 (-18.79%)</td><td>0.28 (-3.99%)</td><td>0.29 (+1.36%)</td><td>0.25 (+2.61%)</td><td>0.02 <b>(-51.08%)</b></td><td>198.80 (-2.55%)</td><td>179.28 (+2.55%)</td><td>169.80 (-1.34%)</td><td>163.90 <b>(+23.14%)</b></td><td>16.50 <b>(-40.26%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.37 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>204.00 (n/a)</td><td>174.82 (n/a)</td><td>172.10 (n/a)</td><td>133.10 (n/a)</td><td>27.62 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>195.30 (n/a)</td><td>179.76 (n/a)</td><td>175.00 (n/a)</td><td>166.10 (n/a)</td><td>14.60 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>210.80 (n/a)</td><td>171.48 (n/a)</td><td>170.20 (n/a)</td><td>130.20 (n/a)</td><td>29.05 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.34 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>200.20 (n/a)</td><td>173.20 (n/a)</td><td>178.50 (n/a)</td><td>144.10 (n/a)</td><td>20.69 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>149.00 (n/a)</td><td>136.54 (n/a)</td><td>136.80 (n/a)</td><td>121.70 (n/a)</td><td>12.14 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>226.20 (n/a)</td><td>169.94 (n/a)</td><td>172.50 (n/a)</td><td>113.10 (n/a)</td><td>43.76 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>257.70 (n/a)</td><td>188.54 (n/a)</td><td>195.30 (n/a)</td><td>120.60 (n/a)</td><td>49.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.20 (n/a)</td><td>184.22 (n/a)</td><td>191.60 (n/a)</td><td>137.50 (n/a)</td><td>27.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>176.40 (n/a)</td><td>154.26 (n/a)</td><td>167.50 (n/a)</td><td>122.90 (n/a)</td><td>26.03 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>201.20 (n/a)</td><td>177.52 (n/a)</td><td>180.40 (n/a)</td><td>141.30 (n/a)</td><td>24.04 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>203.30 (n/a)</td><td>164.84 (n/a)</td><td>178.20 (n/a)</td><td>123.10 (n/a)</td><td>36.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>261.30 (n/a)</td><td>195.68 (n/a)</td><td>196.80 (n/a)</td><td>142.70 (n/a)</td><td>44.68 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>201.00 (n/a)</td><td>171.44 (n/a)</td><td>165.80 (n/a)</td><td>156.00 (n/a)</td><td>17.63 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>171.00 (n/a)</td><td>142.64 (n/a)</td><td>140.50 (n/a)</td><td>114.40 (n/a)</td><td>21.79 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>265.80 (n/a)</td><td>188.76 (n/a)</td><td>196.30 (n/a)</td><td>124.20 (n/a)</td><td>55.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>220.90 (n/a)</td><td>182.04 (n/a)</td><td>183.00 (n/a)</td><td>132.80 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.44 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>195.20 (n/a)</td><td>157.34 (n/a)</td><td>160.20 (n/a)</td><td>111.20 (n/a)</td><td>30.39 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.35 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>235.40 (n/a)</td><td>177.50 (n/a)</td><td>168.70 (n/a)</td><td>139.20 (n/a)</td><td>38.86 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>276.70 (n/a)</td><td>206.28 (n/a)</td><td>194.90 (n/a)</td><td>146.90 (n/a)</td><td>47.60 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>14.85 (-0.02%)</td><td>14.13 (+1.76%)</td><td>14.27 (+1.14%)</td><td>13.02 (+1.81%)</td><td>0.67 (-19.10%)</td><td>4278.50 (-1.78%)</td><td>3951.16 (-1.83%)</td><td>3903.30 (-1.12%)</td><td>3751.70 (+0.02%)</td><td>195.95 (-19.91%)</td><td>14310.26 (-0.02%)</td><td>13613.42 (+1.76%)</td><td>13754.25 (+1.14%)</td><td>12548.02 (+1.81%)</td><td>648.21 (-19.10%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>14.85 (n/a)</td><td>13.88 (n/a)</td><td>14.11 (n/a)</td><td>12.79 (n/a)</td><td>0.83 (n/a)</td><td>4356.10 (n/a)</td><td>4024.90 (n/a)</td><td>3947.70 (n/a)</td><td>3750.80 (n/a)</td><td>244.66 (n/a)</td><td>14313.37 (n/a)</td><td>13377.66 (n/a)</td><td>13599.66 (n/a)</td><td>12324.45 (n/a)</td><td>801.26 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>14.64 (-11.83%)</td><td>12.51 (-11.55%)</td><td>14.25 (-2.15%)</td><td>9.48 (-15.73%)</td><td>2.72 <b>(+31.60%)</b></td><td>1382.20 (+18.67%)</td><td>1092.16 (+15.76%)</td><td>919.50 (+2.19%)</td><td>895.00 (+13.42%)</td><td>257.61 <b>(+76.02%)</b></td><td>9597.55 (-11.83%)</td><td>8201.36 (-11.55%)</td><td>9341.66 (-2.15%)</td><td>6214.59 (-15.73%)</td><td>1782.93 <b>(+31.60%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>16.61 (n/a)</td><td>14.15 (n/a)</td><td>14.57 (n/a)</td><td>11.25 (n/a)</td><td>2.07 (n/a)</td><td>1164.70 (n/a)</td><td>943.46 (n/a)</td><td>899.80 (n/a)</td><td>789.10 (n/a)</td><td>146.36 (n/a)</td><td>10885.83 (n/a)</td><td>9271.80 (n/a)</td><td>9546.77 (n/a)</td><td>7375.05 (n/a)</td><td>1354.76 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>15.25 (+6.25%)</td><td>13.54 (-1.41%)</td><td>14.09 (+1.83%)</td><td>11.33 (-9.53%)</td><td>1.61 <b>(+125.66%)</b></td><td>4915.70 (+10.53%)</td><td>4163.74 (+2.42%)</td><td>3952.30 (-1.80%)</td><td>3653.10 (-5.88%)</td><td>520.80 <b>(+133.41%)</b></td><td>14696.34 (+6.25%)</td><td>13048.79 (-1.41%)</td><td>13583.79 (+1.83%)</td><td>10921.52 (-9.53%)</td><td>1551.69 <b>(+125.66%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>14.35 (n/a)</td><td>13.73 (n/a)</td><td>13.84 (n/a)</td><td>12.53 (n/a)</td><td>0.71 (n/a)</td><td>4447.30 (n/a)</td><td>4065.48 (n/a)</td><td>4024.60 (n/a)</td><td>3881.40 (n/a)</td><td>223.13 (n/a)</td><td>13831.92 (n/a)</td><td>13235.79 (n/a)</td><td>13339.72 (n/a)</td><td>12071.89 (n/a)</td><td>687.62 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>15.45 (+3.96%)</td><td>11.98 (-7.66%)</td><td>10.92 (-16.26%)</td><td>8.68 (-18.40%)</td><td>2.90 <b>(+57.43%)</b></td><td>2057.10 <b>(+22.55%)</b></td><td>1562.22 (+11.62%)</td><td>1635.20 (+19.41%)</td><td>1155.90 (-3.80%)</td><td>373.83 <b>(+82.42%)</b></td><td>11611.84 (+3.96%)</td><td>9003.94 (-7.66%)</td><td>8208.02 (-16.26%)</td><td>6524.47 (-18.40%)</td><td>2179.17 <b>(+57.43%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>14.86 (n/a)</td><td>12.97 (n/a)</td><td>13.04 (n/a)</td><td>10.64 (n/a)</td><td>1.84 (n/a)</td><td>1678.60 (n/a)</td><td>1399.60 (n/a)</td><td>1369.40 (n/a)</td><td>1201.60 (n/a)</td><td>204.93 (n/a)</td><td>11169.74 (n/a)</td><td>9751.24 (n/a)</td><td>9801.22 (n/a)</td><td>7995.83 (n/a)</td><td>1384.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>11.10 (-0.42%)</td><td>10.57 (-1.65%)</td><td>10.48 (-1.41%)</td><td>10.29 (-2.75%)</td><td>0.32 <b>(+38.04%)</b></td><td>7958.40 (+2.83%)</td><td>7753.82 (+1.72%)</td><td>7817.20 (+1.44%)</td><td>7379.00 (+0.42%)</td><td>231.63 <b>(+42.40%)</b></td><td>14551.31 (-0.42%)</td><td>13858.06 (-1.65%)</td><td>13735.66 (-1.41%)</td><td>13491.92 (-2.75%)</td><td>424.43 <b>(+38.04%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>11.15 (n/a)</td><td>10.75 (n/a)</td><td>10.63 (n/a)</td><td>10.58 (n/a)</td><td>0.23 (n/a)</td><td>7739.70 (n/a)</td><td>7623.06 (n/a)</td><td>7706.60 (n/a)</td><td>7348.20 (n/a)</td><td>162.66 (n/a)</td><td>14612.26 (n/a)</td><td>14090.68 (n/a)</td><td>13932.76 (n/a)</td><td>13873.10 (n/a)</td><td>307.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>15.09 (-3.62%)</td><td>13.34 (-8.72%)</td><td>14.58 (-2.35%)</td><td>11.00 (-12.69%)</td><td>2.13 <b>(+82.26%)</b></td><td>1954.10 (+14.53%)</td><td>1646.76 (+11.35%)</td><td>1474.60 (+2.41%)</td><td>1424.90 (+3.76%)</td><td>278.62 <b>(+114.05%)</b></td><td>12057.30 (-3.62%)</td><td>10663.06 (-8.72%)</td><td>11650.32 (-2.35%)</td><td>8791.49 (-12.69%)</td><td>1703.76 <b>(+82.26%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>15.65 (n/a)</td><td>14.62 (n/a)</td><td>14.93 (n/a)</td><td>12.60 (n/a)</td><td>1.17 (n/a)</td><td>1706.20 (n/a)</td><td>1478.96 (n/a)</td><td>1439.90 (n/a)</td><td>1373.30 (n/a)</td><td>130.17 (n/a)</td><td>12509.77 (n/a)</td><td>11681.89 (n/a)</td><td>11931.11 (n/a)</td><td>10068.96 (n/a)</td><td>934.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>11.02 (+5.32%)</td><td>10.72 (+3.01%)</td><td>10.69 (+2.73%)</td><td>10.34 (+0.05%)</td><td>0.27 <b>(+405.64%)</b></td><td>7925.10 (-0.05%)</td><td>7643.34 (-2.88%)</td><td>7663.80 (-2.66%)</td><td>7432.90 (-5.05%)</td><td>192.56 <b>(+379.66%)</b></td><td>14445.79 (+5.32%)</td><td>14055.16 (+3.01%)</td><td>14010.58 (+2.73%)</td><td>13548.67 (+0.05%)</td><td>351.15 <b>(+405.63%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>10.46 (n/a)</td><td>10.41 (n/a)</td><td>10.41 (n/a)</td><td>10.33 (n/a)</td><td>0.05 (n/a)</td><td>7929.30 (n/a)</td><td>7869.96 (n/a)</td><td>7872.90 (n/a)</td><td>7828.50 (n/a)</td><td>40.15 (n/a)</td><td>13715.79 (n/a)</td><td>13643.86 (n/a)</td><td>13638.39 (n/a)</td><td>13541.49 (n/a)</td><td>69.45 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.85 (+15.16%)</td><td>3.13 (+1.63%)</td><td>3.05 (+0.04%)</td><td>2.72 (-4.78%)</td><td>0.45 <b>(+155.69%)</b></td><td>506.60 (+5.02%)</td><td>446.68 (-0.35%)</td><td>451.30 (-0.04%)</td><td>357.20 (-13.17%)</td><td>58.97 <b>(+133.08%)</b></td><td>751.48 (+15.16%)</td><td>610.21 (+1.63%)</td><td>594.82 (+0.04%)</td><td>529.87 (-4.78%)</td><td>87.93 <b>(+155.69%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.35 (n/a)</td><td>3.08 (n/a)</td><td>3.05 (n/a)</td><td>2.85 (n/a)</td><td>0.18 (n/a)</td><td>482.40 (n/a)</td><td>448.24 (n/a)</td><td>451.50 (n/a)</td><td>411.40 (n/a)</td><td>25.30 (n/a)</td><td>652.55 (n/a)</td><td>600.45 (n/a)</td><td>594.59 (n/a)</td><td>556.47 (n/a)</td><td>34.39 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.68 (-5.21%)</td><td>3.52 (-2.88%)</td><td>3.61 (-1.00%)</td><td>3.34 (+0.68%)</td><td>0.15 <b>(-23.73%)</b></td><td>411.70 (-0.68%)</td><td>391.28 (+2.87%)</td><td>381.70 (+1.01%)</td><td>374.50 (+5.49%)</td><td>17.06 <b>(-20.49%)</b></td><td>716.82 (-5.21%)</td><td>687.10 (-2.88%)</td><td>703.33 (-1.00%)</td><td>652.01 (+0.68%)</td><td>29.61 <b>(-23.73%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.88 (n/a)</td><td>3.63 (n/a)</td><td>3.64 (n/a)</td><td>3.32 (n/a)</td><td>0.20 (n/a)</td><td>414.50 (n/a)</td><td>380.38 (n/a)</td><td>377.90 (n/a)</td><td>355.00 (n/a)</td><td>21.46 (n/a)</td><td>756.25 (n/a)</td><td>707.48 (n/a)</td><td>710.43 (n/a)</td><td>647.63 (n/a)</td><td>38.83 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.21 (+3.24%)</td><td>4.17 (-11.50%)</td><td>3.66 <b>(-23.68%)</b></td><td>3.37 (-6.90%)</td><td>1.18 (+15.19%)</td><td>407.80 (+7.40%)</td><td>347.32 (+14.34%)</td><td>376.40 <b>(+31.01%)</b></td><td>221.70 (-3.10%)</td><td>75.87 (+14.22%)</td><td>1211.07 (+3.24%)</td><td>812.72 (-11.50%)</td><td>713.12 <b>(-23.68%)</b></td><td>658.26 (-6.90%)</td><td>229.93 (+15.19%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>6.01 (n/a)</td><td>4.71 (n/a)</td><td>4.79 (n/a)</td><td>3.62 (n/a)</td><td>1.02 (n/a)</td><td>379.70 (n/a)</td><td>303.76 (n/a)</td><td>287.30 (n/a)</td><td>228.80 (n/a)</td><td>66.43 (n/a)</td><td>1173.05 (n/a)</td><td>918.32 (n/a)</td><td>934.38 (n/a)</td><td>707.02 (n/a)</td><td>199.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.18 <b>(+32.82%)</b></td><td>4.55 (+14.87%)</td><td>3.78 (+1.34%)</td><td>3.36 (-5.24%)</td><td>1.41 <b>(+213.38%)</b></td><td>409.90 (+5.54%)</td><td>325.32 (-7.30%)</td><td>364.20 (-1.30%)</td><td>222.80 <b>(-24.70%)</b></td><td>92.01 <b>(+146.00%)</b></td><td>1205.02 <b>(+32.82%)</b></td><td>887.31 (+14.87%)</td><td>737.13 (+1.34%)</td><td>654.86 (-5.24%)</td><td>275.32 <b>(+213.38%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>4.65 (n/a)</td><td>3.96 (n/a)</td><td>3.73 (n/a)</td><td>3.54 (n/a)</td><td>0.45 (n/a)</td><td>388.40 (n/a)</td><td>350.92 (n/a)</td><td>369.00 (n/a)</td><td>295.90 (n/a)</td><td>37.40 (n/a)</td><td>907.26 (n/a)</td><td>772.44 (n/a)</td><td>727.40 (n/a)</td><td>691.10 (n/a)</td><td>87.86 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.62 <b>(-25.14%)</b></td><td>3.36 (-4.35%)</td><td>3.40 (+4.27%)</td><td>3.11 (+2.48%)</td><td>0.22 <b>(-70.59%)</b></td><td>443.10 (-2.40%)</td><td>410.80 (+1.92%)</td><td>404.20 (-4.10%)</td><td>380.10 <b>(+33.60%)</b></td><td>27.04 <b>(-60.10%)</b></td><td>706.22 <b>(-25.14%)</b></td><td>655.67 (-4.35%)</td><td>664.05 (+4.27%)</td><td>605.88 (+2.48%)</td><td>42.82 <b>(-70.59%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>4.84 (n/a)</td><td>3.51 (n/a)</td><td>3.27 (n/a)</td><td>3.03 (n/a)</td><td>0.75 (n/a)</td><td>454.00 (n/a)</td><td>403.06 (n/a)</td><td>421.50 (n/a)</td><td>284.50 (n/a)</td><td>67.76 (n/a)</td><td>943.43 (n/a)</td><td>685.49 (n/a)</td><td>636.88 (n/a)</td><td>591.22 (n/a)</td><td>145.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.47 (-0.91%)</td><td>3.12 (-1.44%)</td><td>3.09 (+0.23%)</td><td>2.81 (+4.88%)</td><td>0.24 <b>(-31.18%)</b></td><td>490.30 (-4.65%)</td><td>443.58 (+0.91%)</td><td>445.80 (-0.25%)</td><td>396.40 (+0.92%)</td><td>33.33 <b>(-33.03%)</b></td><td>677.23 (-0.91%)</td><td>607.93 (-1.44%)</td><td>602.08 (+0.23%)</td><td>547.53 (+4.88%)</td><td>46.21 <b>(-31.18%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.50 (n/a)</td><td>3.16 (n/a)</td><td>3.08 (n/a)</td><td>2.68 (n/a)</td><td>0.34 (n/a)</td><td>514.20 (n/a)</td><td>439.56 (n/a)</td><td>446.90 (n/a)</td><td>392.80 (n/a)</td><td>49.76 (n/a)</td><td>683.45 (n/a)</td><td>616.78 (n/a)</td><td>600.69 (n/a)</td><td>522.04 (n/a)</td><td>67.15 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.26 (-10.60%)</td><td>3.09 (-4.72%)</td><td>3.07 (-8.98%)</td><td>2.95 (+4.71%)</td><td>0.13 <b>(-60.77%)</b></td><td>466.20 (-4.51%)</td><td>445.72 (+4.22%)</td><td>448.50 (+9.87%)</td><td>422.60 (+11.86%)</td><td>18.26 <b>(-58.44%)</b></td><td>635.19 (-10.60%)</td><td>603.05 (-4.72%)</td><td>598.57 (-8.98%)</td><td>575.77 (+4.71%)</td><td>24.90 <b>(-60.77%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.64 (n/a)</td><td>3.24 (n/a)</td><td>3.37 (n/a)</td><td>2.82 (n/a)</td><td>0.33 (n/a)</td><td>488.20 (n/a)</td><td>427.66 (n/a)</td><td>408.20 (n/a)</td><td>377.80 (n/a)</td><td>43.95 (n/a)</td><td>710.50 (n/a)</td><td>632.90 (n/a)</td><td>657.64 (n/a)</td><td>549.88 (n/a)</td><td>63.47 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.86 <b>(+41.62%)</b></td><td>1.30 (+16.00%)</td><td>1.22 (+13.52%)</td><td>1.02 (-0.19%)</td><td>0.33 <b>(+193.55%)</b></td><td>392.70 (+0.20%)</td><td>321.86 (-10.65%)</td><td>328.70 (-11.90%)</td><td>216.30 <b>(-29.38%)</b></td><td>67.91 <b>(+105.44%)</b></td><td>155.15 <b>(+41.62%)</b></td><td>108.84 (+16.00%)</td><td>102.09 (+13.52%)</td><td>85.45 (-0.19%)</td><td>27.54 <b>(+193.55%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.31 (n/a)</td><td>1.12 (n/a)</td><td>1.08 (n/a)</td><td>1.02 (n/a)</td><td>0.11 (n/a)</td><td>391.90 (n/a)</td><td>360.24 (n/a)</td><td>373.10 (n/a)</td><td>306.30 (n/a)</td><td>33.05 (n/a)</td><td>109.55 (n/a)</td><td>93.83 (n/a)</td><td>89.93 (n/a)</td><td>85.62 (n/a)</td><td>9.38 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>5.84 (-13.38%)</td><td>5.03 (-6.66%)</td><td>4.93 (-0.81%)</td><td>4.56 (-2.35%)</td><td>0.48 <b>(-42.10%)</b></td><td>424.10 (+2.41%)</td><td>387.12 (+6.03%)</td><td>392.10 (+0.80%)</td><td>331.10 (+15.45%)</td><td>34.38 <b>(-32.07%)</b></td><td>1215.92 (-13.38%)</td><td>1047.18 (-6.66%)</td><td>1026.79 (-0.81%)</td><td>949.43 (-2.35%)</td><td>100.48 <b>(-42.10%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>6.74 (n/a)</td><td>5.39 (n/a)</td><td>4.97 (n/a)</td><td>4.67 (n/a)</td><td>0.83 (n/a)</td><td>414.10 (n/a)</td><td>365.12 (n/a)</td><td>389.00 (n/a)</td><td>286.80 (n/a)</td><td>50.61 (n/a)</td><td>1403.77 (n/a)</td><td>1121.93 (n/a)</td><td>1035.15 (n/a)</td><td>972.29 (n/a)</td><td>173.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>20.41 <b>(+20.39%)</b></td><td>13.95 (+15.44%)</td><td>11.59 (+4.52%)</td><td>11.11 (+9.10%)</td><td>3.98 <b>(+44.07%)</b></td><td>495.40 (-8.34%)</td><td>416.56 (-11.52%)</td><td>475.00 (-4.33%)</td><td>269.70 (-16.91%)</td><td>97.84 (+15.76%)</td><td>7963.58 <b>(+20.39%)</b></td><td>5443.63 (+15.44%)</td><td>4521.27 (+4.52%)</td><td>4334.82 (+9.10%)</td><td>1550.98 <b>(+44.07%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>16.96 (n/a)</td><td>12.09 (n/a)</td><td>11.09 (n/a)</td><td>10.19 (n/a)</td><td>2.76 (n/a)</td><td>540.50 (n/a)</td><td>470.78 (n/a)</td><td>496.50 (n/a)</td><td>324.60 (n/a)</td><td>84.52 (n/a)</td><td>6615.01 (n/a)</td><td>4715.42 (n/a)</td><td>4325.55 (n/a)</td><td>3973.15 (n/a)</td><td>1076.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>10.44 (+14.29%)</td><td>8.50 (+4.71%)</td><td>7.95 (+1.05%)</td><td>7.55 (-1.79%)</td><td>1.19 <b>(+102.15%)</b></td><td>729.40 (+1.81%)</td><td>657.10 (-3.51%)</td><td>692.50 (-1.04%)</td><td>527.10 (-12.50%)</td><td>83.09 <b>(+81.21%)</b></td><td>4074.28 (+14.29%)</td><td>3315.08 (+4.71%)</td><td>3101.25 (+1.05%)</td><td>2944.07 (-1.79%)</td><td>465.83 <b>(+102.15%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.14 (n/a)</td><td>8.12 (n/a)</td><td>7.87 (n/a)</td><td>7.68 (n/a)</td><td>0.59 (n/a)</td><td>716.40 (n/a)</td><td>680.98 (n/a)</td><td>699.80 (n/a)</td><td>602.40 (n/a)</td><td>45.85 (n/a)</td><td>3564.90 (n/a)</td><td>3165.98 (n/a)</td><td>3068.92 (n/a)</td><td>2997.71 (n/a)</td><td>230.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>10.07 (+3.98%)</td><td>8.79 (-1.13%)</td><td>8.65 (-4.04%)</td><td>8.00 (-2.80%)</td><td>0.77 <b>(+24.79%)</b></td><td>724.60 (+2.87%)</td><td>663.74 (+1.33%)</td><td>670.50 (+4.20%)</td><td>575.70 (-3.83%)</td><td>54.54 (+19.78%)</td><td>4196.45 (+3.98%)</td><td>3660.92 (-1.13%)</td><td>3603.02 (-4.04%)</td><td>3334.01 (-2.80%)</td><td>321.61 <b>(+24.79%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.69 (n/a)</td><td>8.89 (n/a)</td><td>9.01 (n/a)</td><td>8.23 (n/a)</td><td>0.62 (n/a)</td><td>704.40 (n/a)</td><td>655.02 (n/a)</td><td>643.50 (n/a)</td><td>598.60 (n/a)</td><td>45.53 (n/a)</td><td>4035.68 (n/a)</td><td>3702.62 (n/a)</td><td>3754.61 (n/a)</td><td>3429.94 (n/a)</td><td>257.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>261.50 (n/a)</td><td>183.26 (n/a)</td><td>162.30 (n/a)</td><td>158.40 (n/a)</td><td>44.11 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.90 (n/a)</td><td>157.94 (n/a)</td><td>150.90 (n/a)</td><td>128.60 (n/a)</td><td>25.34 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.40 (n/a)</td><td>179.68 (n/a)</td><td>173.30 (n/a)</td><td>162.40 (n/a)</td><td>15.75 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>370.00 (n/a)</td><td>215.46 (n/a)</td><td>173.70 (n/a)</td><td>162.00 (n/a)</td><td>87.55 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.40 (n/a)</td><td>188.28 (n/a)</td><td>193.70 (n/a)</td><td>155.50 (n/a)</td><td>25.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.40 (n/a)</td><td>189.54 (n/a)</td><td>183.50 (n/a)</td><td>174.70 (n/a)</td><td>15.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>245.20 (n/a)</td><td>203.04 (n/a)</td><td>197.30 (n/a)</td><td>166.50 (n/a)</td><td>34.62 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>252.70 (n/a)</td><td>209.46 (n/a)</td><td>201.80 (n/a)</td><td>180.40 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>167.74 (n/a)</td><td>168.80 (n/a)</td><td>135.10 (n/a)</td><td>31.69 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.00 (n/a)</td><td>187.70 (n/a)</td><td>202.60 (n/a)</td><td>133.60 (n/a)</td><td>35.40 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.90 (n/a)</td><td>174.20 (n/a)</td><td>174.10 (n/a)</td><td>135.60 (n/a)</td><td>24.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>220.70 (n/a)</td><td>168.00 (n/a)</td><td>172.10 (n/a)</td><td>124.90 (n/a)</td><td>36.83 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>197.40 (n/a)</td><td>173.18 (n/a)</td><td>172.80 (n/a)</td><td>156.50 (n/a)</td><td>15.49 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>171.66 (n/a)</td><td>178.60 (n/a)</td><td>132.50 (n/a)</td><td>26.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.90 (n/a)</td><td>175.86 (n/a)</td><td>171.30 (n/a)</td><td>145.00 (n/a)</td><td>22.27 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>222.40 (n/a)</td><td>209.06 (n/a)</td><td>207.30 (n/a)</td><td>193.30 (n/a)</td><td>12.12 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>175.74 (n/a)</td><td>183.00 (n/a)</td><td>142.60 (n/a)</td><td>19.99 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.20 (n/a)</td><td>196.24 (n/a)</td><td>208.10 (n/a)</td><td>157.80 (n/a)</td><td>29.25 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>199.10 (n/a)</td><td>181.70 (n/a)</td><td>180.30 (n/a)</td><td>163.60 (n/a)</td><td>16.22 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>257.10 (n/a)</td><td>170.40 (n/a)</td><td>155.40 (n/a)</td><td>119.10 (n/a)</td><td>56.45 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>217.70 (n/a)</td><td>180.72 (n/a)</td><td>180.80 (n/a)</td><td>138.80 (n/a)</td><td>28.06 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>237.00 (n/a)</td><td>207.10 (n/a)</td><td>212.90 (n/a)</td><td>167.50 (n/a)</td><td>26.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.10 (n/a)</td><td>189.48 (n/a)</td><td>208.80 (n/a)</td><td>149.20 (n/a)</td><td>35.34 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>266.00 (n/a)</td><td>228.32 (n/a)</td><td>234.60 (n/a)</td><td>174.50 (n/a)</td><td>33.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>196.28 (n/a)</td><td>189.20 (n/a)</td><td>176.80 (n/a)</td><td>16.49 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>211.80 (n/a)</td><td>173.80 (n/a)</td><td>158.80 (n/a)</td><td>141.80 (n/a)</td><td>33.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>286.30 (n/a)</td><td>220.30 (n/a)</td><td>200.60 (n/a)</td><td>188.70 (n/a)</td><td>39.26 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>246.60 (n/a)</td><td>183.46 (n/a)</td><td>181.20 (n/a)</td><td>136.10 (n/a)</td><td>42.16 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>213.10 (n/a)</td><td>165.36 (n/a)</td><td>150.30 (n/a)</td><td>141.80 (n/a)</td><td>29.70 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>171.50 (n/a)</td><td>156.26 (n/a)</td><td>151.10 (n/a)</td><td>147.30 (n/a)</td><td>10.50 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>206.30 (n/a)</td><td>177.24 (n/a)</td><td>177.40 (n/a)</td><td>145.80 (n/a)</td><td>21.58 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>190.62 (n/a)</td><td>189.70 (n/a)</td><td>173.80 (n/a)</td><td>16.90 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>4.12 (+0.14%)</td><td>4.11 (+0.05%)</td><td>4.11 (+0.22%)</td><td>4.09 (+0.04%)</td><td>0.01 <b>(+42.07%)</b></td><td>19230.70 (-0.04%)</td><td>19151.38 (-0.05%)</td><td>19118.00 (-0.22%)</td><td>19084.90 (-0.14%)</td><td>68.26 <b>(+41.90%)</b></td><td>2813.07 (+0.14%)</td><td>2803.33 (+0.05%)</td><td>2808.19 (+0.22%)</td><td>2791.74 (+0.04%)</td><td>9.98 <b>(+42.07%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>4.11 (n/a)</td><td>4.10 (n/a)</td><td>4.10 (n/a)</td><td>4.09 (n/a)</td><td>0.01 (n/a)</td><td>19238.30 (n/a)</td><td>19161.06 (n/a)</td><td>19160.50 (n/a)</td><td>19112.20 (n/a)</td><td>48.10 (n/a)</td><td>2809.05 (n/a)</td><td>2801.90 (n/a)</td><td>2801.96 (n/a)</td><td>2790.63 (n/a)</td><td>7.03 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>4.41 (+0.25%)</td><td>4.28 (+7.20%)</td><td>4.32 (+5.36%)</td><td>4.15 (+17.98%)</td><td>0.11 <b>(-71.36%)</b></td><td>2264.80 (-15.24%)</td><td>2199.46 (-7.38%)</td><td>2174.90 (-5.09%)</td><td>2133.00 (-0.25%)</td><td>56.75 <b>(-75.78%)</b></td><td>1734.34 (+0.25%)</td><td>1682.83 (+7.20%)</td><td>1700.91 (+5.36%)</td><td>1633.41 (+17.98%)</td><td>43.28 <b>(-71.36%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>4.40 (n/a)</td><td>3.99 (n/a)</td><td>4.10 (n/a)</td><td>3.52 (n/a)</td><td>0.38 (n/a)</td><td>2672.10 (n/a)</td><td>2374.70 (n/a)</td><td>2291.50 (n/a)</td><td>2138.30 (n/a)</td><td>234.34 (n/a)</td><td>1730.03 (n/a)</td><td>1569.73 (n/a)</td><td>1614.36 (n/a)</td><td>1384.44 (n/a)</td><td>151.11 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.97 (-7.11%)</td><td>0.87 (-9.47%)</td><td>0.90 (-5.42%)</td><td>0.71 (-18.46%)</td><td>0.10 <b>(+39.66%)</b></td><td>312.40 <b>(+22.65%)</b></td><td>255.86 (+11.29%)</td><td>244.70 (+5.75%)</td><td>229.10 (+7.66%)</td><td>33.13 <b>(+89.95%)</b></td><td>41.19 (-7.11%)</td><td>37.33 (-9.47%)</td><td>38.57 (-5.42%)</td><td>30.21 (-18.46%)</td><td>4.29 <b>(+39.66%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.04 (n/a)</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.87 (n/a)</td><td>0.07 (n/a)</td><td>254.70 (n/a)</td><td>229.90 (n/a)</td><td>231.40 (n/a)</td><td>212.80 (n/a)</td><td>17.44 (n/a)</td><td>44.34 (n/a)</td><td>41.23 (n/a)</td><td>40.78 (n/a)</td><td>37.05 (n/a)</td><td>3.07 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.02 (-5.99%)</td><td>0.82 (-2.71%)</td><td>0.77 (+0.59%)</td><td>0.67 (-1.35%)</td><td>0.16 (-13.52%)</td><td>330.50 (+1.35%)</td><td>277.30 (+2.00%)</td><td>286.60 (-0.59%)</td><td>217.60 (+6.35%)</td><td>53.26 (-7.30%)</td><td>43.36 (-5.99%)</td><td>35.10 (-2.71%)</td><td>32.93 (+0.59%)</td><td>28.55 (-1.35%)</td><td>6.99 (-13.52%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.08 (n/a)</td><td>0.85 (n/a)</td><td>0.77 (n/a)</td><td>0.68 (n/a)</td><td>0.19 (n/a)</td><td>326.10 (n/a)</td><td>271.86 (n/a)</td><td>288.30 (n/a)</td><td>204.60 (n/a)</td><td>57.45 (n/a)</td><td>46.13 (n/a)</td><td>36.08 (n/a)</td><td>32.73 (n/a)</td><td>28.94 (n/a)</td><td>8.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.53 (+0.82%)</td><td>0.53 (+0.28%)</td><td>0.53 (+0.13%)</td><td>0.53 (+0.26%)</td><td>0.00 <b>(+231.58%)</b></td><td>47794.50 (-0.26%)</td><td>47697.24 (-0.28%)</td><td>47766.20 (-0.13%)</td><td>47386.80 (-0.82%)</td><td>174.09 <b>(+227.84%)</b></td><td>362.55 (+0.82%)</td><td>360.19 (+0.28%)</td><td>359.67 (+0.13%)</td><td>359.45 (+0.26%)</td><td>1.32 <b>(+231.56%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47918.00 (n/a)</td><td>47831.26 (n/a)</td><td>47827.30 (n/a)</td><td>47777.40 (n/a)</td><td>53.10 (n/a)</td><td>359.58 (n/a)</td><td>359.18 (n/a)</td><td>359.21 (n/a)</td><td>358.53 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (-1.56%)</td><td>0.21 (-1.18%)</td><td>0.21 (-1.06%)</td><td>0.21 (-1.64%)</td><td>0.00 (+2.53%)</td><td>120015.40 (+1.66%)</td><td>118869.14 (+1.19%)</td><td>118925.40 (+1.07%)</td><td>118113.70 (+1.58%)</td><td>733.48 (+6.07%)</td><td>145.45 (-1.56%)</td><td>144.53 (-1.18%)</td><td>144.46 (-1.06%)</td><td>143.15 (-1.64%)</td><td>0.89 (+2.53%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>118053.00 (n/a)</td><td>117465.60 (n/a)</td><td>117669.00 (n/a)</td><td>116273.80 (n/a)</td><td>691.52 (n/a)</td><td>147.75 (n/a)</td><td>146.26 (n/a)</td><td>146.00 (n/a)</td><td>145.53 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.91 (+0.31%)</td><td>0.90 (+0.48%)</td><td>0.90 (+0.69%)</td><td>0.89 (+0.32%)</td><td>0.00 (-6.20%)</td><td>28133.70 (-0.32%)</td><td>27893.64 (-0.48%)</td><td>27851.80 (-0.69%)</td><td>27762.70 (-0.31%)</td><td>140.53 (-6.65%)</td><td>618.81 (+0.31%)</td><td>615.92 (+0.48%)</td><td>616.83 (+0.69%)</td><td>610.65 (+0.32%)</td><td>3.09 (-6.20%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.00 (n/a)</td><td>28223.50 (n/a)</td><td>28027.88 (n/a)</td><td>28044.80 (n/a)</td><td>27849.50 (n/a)</td><td>150.53 (n/a)</td><td>616.88 (n/a)</td><td>612.97 (n/a)</td><td>612.59 (n/a)</td><td>608.71 (n/a)</td><td>3.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.64 (+0.26%)</td><td>3.55 (+0.20%)</td><td>3.62 (-0.06%)</td><td>3.42 (+0.30%)</td><td>0.10 (-8.21%)</td><td>7357.90 (-0.30%)</td><td>7087.90 (-0.21%)</td><td>6958.80 (+0.05%)</td><td>6912.00 (-0.26%)</td><td>206.29 (-8.59%)</td><td>2485.51 (+0.26%)</td><td>2425.45 (+0.20%)</td><td>2468.79 (-0.06%)</td><td>2334.89 (+0.30%)</td><td>69.75 (-8.21%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.63 (n/a)</td><td>3.55 (n/a)</td><td>3.62 (n/a)</td><td>3.41 (n/a)</td><td>0.11 (n/a)</td><td>7380.10 (n/a)</td><td>7102.68 (n/a)</td><td>6955.00 (n/a)</td><td>6930.30 (n/a)</td><td>225.69 (n/a)</td><td>2478.97 (n/a)</td><td>2420.72 (n/a)</td><td>2470.15 (n/a)</td><td>2327.86 (n/a)</td><td>75.99 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.19 (-3.02%)</td><td>3.00 (+2.83%)</td><td>2.95 (+1.91%)</td><td>2.88 (+8.12%)</td><td>0.13 <b>(-48.08%)</b></td><td>8747.90 (-7.51%)</td><td>8388.88 (-3.18%)</td><td>8532.10 (-1.87%)</td><td>7886.00 (+3.11%)</td><td>360.79 <b>(-50.64%)</b></td><td>2178.52 (-3.02%)</td><td>2051.03 (+2.83%)</td><td>2013.56 (+1.91%)</td><td>1963.88 (+8.12%)</td><td>89.89 <b>(-48.08%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.29 (n/a)</td><td>2.92 (n/a)</td><td>2.89 (n/a)</td><td>2.66 (n/a)</td><td>0.25 (n/a)</td><td>9457.90 (n/a)</td><td>8664.04 (n/a)</td><td>8694.60 (n/a)</td><td>7647.80 (n/a)</td><td>730.93 (n/a)</td><td>2246.37 (n/a)</td><td>1994.55 (n/a)</td><td>1975.92 (n/a)</td><td>1816.45 (n/a)</td><td>173.15 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.23 (+0.10%)</td><td>3.19 (-0.17%)</td><td>3.18 (-0.37%)</td><td>3.16 (+0.31%)</td><td>0.03 (-10.04%)</td><td>7974.70 (-0.31%)</td><td>7895.16 (+0.17%)</td><td>7915.50 (+0.37%)</td><td>7784.50 (-0.11%)</td><td>73.13 (-10.43%)</td><td>2206.93 (+0.10%)</td><td>2176.15 (-0.17%)</td><td>2170.40 (-0.37%)</td><td>2154.29 (+0.31%)</td><td>20.25 (-10.04%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.23 (n/a)</td><td>3.19 (n/a)</td><td>3.19 (n/a)</td><td>3.15 (n/a)</td><td>0.03 (n/a)</td><td>7999.50 (n/a)</td><td>7882.12 (n/a)</td><td>7886.30 (n/a)</td><td>7792.70 (n/a)</td><td>81.64 (n/a)</td><td>2204.62 (n/a)</td><td>2179.79 (n/a)</td><td>2178.46 (n/a)</td><td>2147.61 (n/a)</td><td>22.51 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.80 (+0.38%)</td><td>0.80 (+0.07%)</td><td>0.80 (-0.02%)</td><td>0.80 (-0.03%)</td><td>0.00 <b>(+455.61%)</b></td><td>94902.00 (+0.03%)</td><td>94752.08 (-0.07%)</td><td>94847.70 (+0.02%)</td><td>94409.40 (-0.38%)</td><td>205.06 <b>(+453.44%)</b></td><td>727.89 (+0.38%)</td><td>725.26 (+0.07%)</td><td>724.52 (-0.02%)</td><td>724.11 (-0.03%)</td><td>1.57 <b>(+455.54%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94871.30 (n/a)</td><td>94821.30 (n/a)</td><td>94827.90 (n/a)</td><td>94769.30 (n/a)</td><td>37.05 (n/a)</td><td>725.12 (n/a)</td><td>724.73 (n/a)</td><td>724.68 (n/a)</td><td>724.34 (n/a)</td><td>0.28 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.73 (-0.04%)</td><td>0.73 (-0.03%)</td><td>0.73 (-0.03%)</td><td>0.73 (-0.00%)</td><td>0.00 <b>(-32.01%)</b></td><td>103359.90 (+0.00%)</td><td>103341.44 (+0.03%)</td><td>103346.40 (+0.03%)</td><td>103318.30 (+0.04%)</td><td>19.82 <b>(-31.92%)</b></td><td>665.12 (-0.04%)</td><td>664.97 (-0.03%)</td><td>664.94 (-0.03%)</td><td>664.86 (-0.00%)</td><td>0.13 <b>(-32.03%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103355.80 (n/a)</td><td>103312.74 (n/a)</td><td>103311.70 (n/a)</td><td>103273.90 (n/a)</td><td>29.11 (n/a)</td><td>665.41 (n/a)</td><td>665.16 (n/a)</td><td>665.17 (n/a)</td><td>664.88 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.69 (-0.01%)</td><td>0.68 (-0.11%)</td><td>0.68 (-0.19%)</td><td>0.68 (-0.08%)</td><td>0.00 (+19.03%)</td><td>110651.10 (+0.08%)</td><td>110377.96 (+0.11%)</td><td>110498.90 (+0.19%)</td><td>109863.20 (+0.01%)</td><td>307.97 (+19.11%)</td><td>625.50 (-0.01%)</td><td>622.59 (-0.11%)</td><td>621.90 (-0.19%)</td><td>621.05 (-0.08%)</td><td>1.74 (+19.03%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110564.10 (n/a)</td><td>110255.90 (n/a)</td><td>110285.80 (n/a)</td><td>109857.10 (n/a)</td><td>258.56 (n/a)</td><td>625.54 (n/a)</td><td>623.28 (n/a)</td><td>623.10 (n/a)</td><td>621.53 (n/a)</td><td>1.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>2.80 (+0.15%)</td><td>2.80 (+0.32%)</td><td>2.80 (+0.37%)</td><td>2.79 (+0.47%)</td><td>0.00 <b>(-68.15%)</b></td><td>37530.90 (-0.46%)</td><td>37485.04 (-0.32%)</td><td>37472.00 (-0.37%)</td><td>37467.20 (-0.15%)</td><td>26.43 <b>(-68.32%)</b></td><td>2865.82 (+0.15%)</td><td>2864.45 (+0.32%)</td><td>2865.45 (+0.37%)</td><td>2860.95 (+0.47%)</td><td>2.02 <b>(-68.15%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>2.79 (n/a)</td><td>2.79 (n/a)</td><td>2.79 (n/a)</td><td>2.78 (n/a)</td><td>0.01 (n/a)</td><td>37706.20 (n/a)</td><td>37606.28 (n/a)</td><td>37611.90 (n/a)</td><td>37522.20 (n/a)</td><td>83.43 (n/a)</td><td>2861.61 (n/a)</td><td>2855.23 (n/a)</td><td>2854.79 (n/a)</td><td>2847.65 (n/a)</td><td>6.33 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>8.01 (+3.52%)</td><td>7.12 (-0.03%)</td><td>6.94 (-0.73%)</td><td>6.76 (+5.18%)</td><td>0.50 (-7.43%)</td><td>1318.50 (-4.93%)</td><td>1255.88 (-0.07%)</td><td>1283.60 (+0.73%)</td><td>1112.50 (-3.40%)</td><td>81.83 (-15.39%)</td><td>482.58 (+3.52%)</td><td>429.07 (-0.03%)</td><td>418.26 (-0.73%)</td><td>407.17 (+5.18%)</td><td>30.37 (-7.43%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>7.74 (n/a)</td><td>7.13 (n/a)</td><td>6.99 (n/a)</td><td>6.43 (n/a)</td><td>0.54 (n/a)</td><td>1386.90 (n/a)</td><td>1256.80 (n/a)</td><td>1274.30 (n/a)</td><td>1151.60 (n/a)</td><td>96.72 (n/a)</td><td>466.18 (n/a)</td><td>429.19 (n/a)</td><td>421.32 (n/a)</td><td>387.10 (n/a)</td><td>32.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.88 (-3.22%)</td><td>6.71 (+2.32%)</td><td>6.80 (-0.29%)</td><td>6.30 <b>(+23.57%)</b></td><td>0.23 <b>(-71.63%)</b></td><td>1414.10 (-19.07%)</td><td>1329.72 (-3.64%)</td><td>1311.50 (+0.29%)</td><td>1296.30 (+3.32%)</td><td>48.40 <b>(-76.61%)</b></td><td>414.15 (-3.22%)</td><td>404.16 (+2.32%)</td><td>409.35 (-0.29%)</td><td>379.66 <b>(+23.57%)</b></td><td>14.11 <b>(-71.63%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>7.10 (n/a)</td><td>6.56 (n/a)</td><td>6.82 (n/a)</td><td>5.10 (n/a)</td><td>0.83 (n/a)</td><td>1747.40 (n/a)</td><td>1379.98 (n/a)</td><td>1307.70 (n/a)</td><td>1254.60 (n/a)</td><td>206.91 (n/a)</td><td>427.92 (n/a)</td><td>395.00 (n/a)</td><td>410.54 (n/a)</td><td>307.25 (n/a)</td><td>49.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.57 (-4.85%)</td><td>6.13 (-5.14%)</td><td>6.08 (-4.76%)</td><td>5.65 (-7.38%)</td><td>0.34 (-9.85%)</td><td>1576.80 (+7.97%)</td><td>1456.62 (+5.39%)</td><td>1465.10 (+5.00%)</td><td>1357.20 (+5.10%)</td><td>81.99 (+2.39%)</td><td>395.56 (-4.85%)</td><td>369.50 (-5.14%)</td><td>366.45 (-4.76%)</td><td>340.49 (-7.38%)</td><td>20.53 (-9.85%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>6.90 (n/a)</td><td>6.47 (n/a)</td><td>6.39 (n/a)</td><td>6.10 (n/a)</td><td>0.38 (n/a)</td><td>1460.40 (n/a)</td><td>1382.08 (n/a)</td><td>1395.30 (n/a)</td><td>1291.40 (n/a)</td><td>80.07 (n/a)</td><td>415.74 (n/a)</td><td>389.51 (n/a)</td><td>384.78 (n/a)</td><td>367.62 (n/a)</td><td>22.77 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>7.98 (+0.39%)</td><td>7.84 (+0.86%)</td><td>7.95 (+0.16%)</td><td>7.40 (+0.39%)</td><td>0.25 (-3.69%)</td><td>4713.90 (-0.38%)</td><td>4452.38 (-0.86%)</td><td>4387.30 (-0.16%)</td><td>4369.00 (-0.39%)</td><td>147.09 (-3.77%)</td><td>491.53 (+0.39%)</td><td>482.73 (+0.86%)</td><td>489.47 (+0.16%)</td><td>455.56 (+0.39%)</td><td>15.29 (-3.69%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>7.95 (n/a)</td><td>7.77 (n/a)</td><td>7.93 (n/a)</td><td>7.37 (n/a)</td><td>0.26 (n/a)</td><td>4732.10 (n/a)</td><td>4490.84 (n/a)</td><td>4394.50 (n/a)</td><td>4385.90 (n/a)</td><td>152.86 (n/a)</td><td>489.63 (n/a)</td><td>478.62 (n/a)</td><td>488.67 (n/a)</td><td>453.81 (n/a)</td><td>15.88 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>7.89 (+3.95%)</td><td>7.64 (+4.60%)</td><td>7.63 (+4.93%)</td><td>7.50 (+6.58%)</td><td>0.15 <b>(-40.62%)</b></td><td>4651.30 (-6.17%)</td><td>4565.16 (-4.46%)</td><td>4570.60 (-4.70%)</td><td>4418.20 (-3.80%)</td><td>89.55 <b>(-46.48%)</b></td><td>486.06 (+3.95%)</td><td>470.55 (+4.60%)</td><td>469.85 (+4.93%)</td><td>461.69 (+6.58%)</td><td>9.39 <b>(-40.62%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>7.59 (n/a)</td><td>7.30 (n/a)</td><td>7.27 (n/a)</td><td>7.03 (n/a)</td><td>0.26 (n/a)</td><td>4957.40 (n/a)</td><td>4778.14 (n/a)</td><td>4795.90 (n/a)</td><td>4592.60 (n/a)</td><td>167.33 (n/a)</td><td>467.60 (n/a)</td><td>449.88 (n/a)</td><td>447.77 (n/a)</td><td>433.19 (n/a)</td><td>15.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>7.76 (+2.13%)</td><td>7.20 (+0.25%)</td><td>7.03 (-3.05%)</td><td>6.83 (+0.43%)</td><td>0.38 (+15.22%)</td><td>5107.40 (-0.43%)</td><td>4851.48 (-0.21%)</td><td>4962.50 (+3.14%)</td><td>4491.50 (-2.08%)</td><td>246.32 (+11.59%)</td><td>478.12 (+2.13%)</td><td>443.59 (+0.25%)</td><td>432.74 (-3.05%)</td><td>420.47 (+0.43%)</td><td>23.13 (+15.22%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>7.60 (n/a)</td><td>7.18 (n/a)</td><td>7.25 (n/a)</td><td>6.80 (n/a)</td><td>0.33 (n/a)</td><td>5129.60 (n/a)</td><td>4861.46 (n/a)</td><td>4811.30 (n/a)</td><td>4587.00 (n/a)</td><td>220.74 (n/a)</td><td>468.17 (n/a)</td><td>442.47 (n/a)</td><td>446.34 (n/a)</td><td>418.65 (n/a)</td><td>20.07 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.80 (-0.07%)</td><td>0.80 (-0.13%)</td><td>0.80 (-0.16%)</td><td>0.80 (-0.12%)</td><td>0.00 (+12.24%)</td><td>94421.30 (+0.12%)</td><td>94254.90 (+0.13%)</td><td>94264.00 (+0.16%)</td><td>94105.70 (+0.07%)</td><td>118.40 (+12.45%)</td><td>730.24 (-0.07%)</td><td>729.08 (-0.13%)</td><td>729.01 (-0.16%)</td><td>727.80 (-0.12%)</td><td>0.92 (+12.23%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94310.80 (n/a)</td><td>94135.44 (n/a)</td><td>94112.80 (n/a)</td><td>94039.30 (n/a)</td><td>105.29 (n/a)</td><td>730.75 (n/a)</td><td>730.01 (n/a)</td><td>730.18 (n/a)</td><td>728.65 (n/a)</td><td>0.82 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.74 (-0.36%)</td><td>0.74 (-0.09%)</td><td>0.74 (-0.04%)</td><td>0.74 (-0.01%)</td><td>0.00 <b>(-79.42%)</b></td><td>102648.40 (+0.01%)</td><td>102616.52 (+0.09%)</td><td>102632.90 (+0.04%)</td><td>102555.00 (+0.36%)</td><td>39.20 <b>(-79.32%)</b></td><td>670.07 (-0.36%)</td><td>669.67 (-0.09%)</td><td>669.57 (-0.04%)</td><td>669.46 (-0.01%)</td><td>0.26 <b>(-79.41%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102634.80 (n/a)</td><td>102519.86 (n/a)</td><td>102591.40 (n/a)</td><td>102182.40 (n/a)</td><td>189.61 (n/a)</td><td>672.52 (n/a)</td><td>670.31 (n/a)</td><td>669.84 (n/a)</td><td>669.55 (n/a)</td><td>1.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.71 (+0.04%)</td><td>0.71 (-0.00%)</td><td>0.71 (-0.04%)</td><td>0.71 (+0.10%)</td><td>0.00 <b>(-20.17%)</b></td><td>106055.10 (-0.10%)</td><td>105964.96 (+0.00%)</td><td>105948.40 (+0.04%)</td><td>105831.40 (-0.04%)</td><td>93.40 <b>(-20.28%)</b></td><td>649.33 (+0.04%)</td><td>648.51 (-0.00%)</td><td>648.61 (-0.04%)</td><td>647.96 (+0.10%)</td><td>0.57 <b>(-20.17%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106162.40 (n/a)</td><td>105960.66 (n/a)</td><td>105910.60 (n/a)</td><td>105874.20 (n/a)</td><td>117.15 (n/a)</td><td>649.07 (n/a)</td><td>648.54 (n/a)</td><td>648.84 (n/a)</td><td>647.31 (n/a)</td><td>0.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>4.02 (-7.49%)</td><td>3.36 (-2.07%)</td><td>3.14 (+0.55%)</td><td>2.93 (-2.41%)</td><td>0.47 (-18.37%)</td><td>2749.60 (+2.47%)</td><td>2432.66 (+1.57%)</td><td>2565.70 (-0.54%)</td><td>2004.60 (+8.09%)</td><td>320.82 (-10.42%)</td><td>1054.56 (-7.49%)</td><td>881.94 (-2.07%)</td><td>823.92 (+0.55%)</td><td>768.83 (-2.41%)</td><td>123.02 (-18.36%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>4.35 (n/a)</td><td>3.43 (n/a)</td><td>3.12 (n/a)</td><td>3.00 (n/a)</td><td>0.57 (n/a)</td><td>2683.20 (n/a)</td><td>2395.10 (n/a)</td><td>2579.70 (n/a)</td><td>1854.50 (n/a)</td><td>358.13 (n/a)</td><td>1139.89 (n/a)</td><td>900.55 (n/a)</td><td>819.45 (n/a)</td><td>787.83 (n/a)</td><td>150.70 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.55 (+8.72%)</td><td>0.39 (+7.17%)</td><td>0.32 (-10.52%)</td><td>0.27 (-3.04%)</td><td>0.13 <b>(+41.24%)</b></td><td>4530.90 (+3.14%)</td><td>3502.38 (-3.12%)</td><td>3914.50 (+11.75%)</td><td>2255.30 (-8.02%)</td><td>1037.59 <b>(+33.80%)</b></td><td>29.76 (+8.72%)</td><td>20.77 (+7.17%)</td><td>17.14 (-10.52%)</td><td>14.81 (-3.04%)</td><td>6.84 <b>(+41.24%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.51 (n/a)</td><td>0.36 (n/a)</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.09 (n/a)</td><td>4393.00 (n/a)</td><td>3615.24 (n/a)</td><td>3502.80 (n/a)</td><td>2451.90 (n/a)</td><td>775.51 (n/a)</td><td>27.37 (n/a)</td><td>19.38 (n/a)</td><td>19.16 (n/a)</td><td>15.28 (n/a)</td><td>4.84 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.59 <b>(+38.40%)</b></td><td>4.91 <b>(+24.71%)</b></td><td>4.81 <b>(+32.01%)</b></td><td>3.64 (+12.55%)</td><td>1.06 <b>(+43.50%)</b></td><td>1825.50 (-11.15%)</td><td>1404.06 (-19.17%)</td><td>1382.70 <b>(-24.25%)</b></td><td>1008.80 <b>(-27.75%)</b></td><td>290.28 (-7.50%)</td><td>2037.33 <b>(+38.40%)</b></td><td>1516.82 <b>(+24.71%)</b></td><td>1486.33 <b>(+32.01%)</b></td><td>1125.84 (+12.55%)</td><td>328.87 <b>(+43.50%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>4.76 (n/a)</td><td>3.94 (n/a)</td><td>3.64 (n/a)</td><td>3.24 (n/a)</td><td>0.74 (n/a)</td><td>2054.60 (n/a)</td><td>1736.98 (n/a)</td><td>1825.40 (n/a)</td><td>1396.20 (n/a)</td><td>313.83 (n/a)</td><td>1472.02 (n/a)</td><td>1216.26 (n/a)</td><td>1125.89 (n/a)</td><td>1000.31 (n/a)</td><td>229.19 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>13.44 (n/a)</td><td>12.30 (n/a)</td><td>13.21 (n/a)</td><td>10.73 (n/a)</td><td>1.43 (n/a)</td><td>13.43 (n/a)</td><td>12.30 (n/a)</td><td>13.20 (n/a)</td><td>10.72 (n/a)</td><td>1.43 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>25.06 (+1.89%)</td><td>23.20 (-3.38%)</td><td>24.24 (+0.92%)</td><td>19.62 (-15.98%)</td><td>2.19 <b>(+373.45%)</b></td><td>25.04 (+1.89%)</td><td>23.19 (-3.38%)</td><td>24.22 (+0.92%)</td><td>19.60 (-15.98%)</td><td>2.19 <b>(+373.45%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>24.59 (n/a)</td><td>24.01 (n/a)</td><td>24.01 (n/a)</td><td>23.35 (n/a)</td><td>0.46 (n/a)</td><td>24.58 (n/a)</td><td>24.00 (n/a)</td><td>24.00 (n/a)</td><td>23.33 (n/a)</td><td>0.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>42.95 (+0.64%)</td><td>39.71 (-1.41%)</td><td>41.06 (+1.66%)</td><td>31.81 (-17.39%)</td><td>4.49 <b>(+188.34%)</b></td><td>42.93 (+0.64%)</td><td>39.69 (-1.41%)</td><td>41.03 (+1.66%)</td><td>31.79 (-17.39%)</td><td>4.48 <b>(+188.34%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>42.68 (n/a)</td><td>40.28 (n/a)</td><td>40.39 (n/a)</td><td>38.50 (n/a)</td><td>1.56 (n/a)</td><td>42.65 (n/a)</td><td>40.26 (n/a)</td><td>40.37 (n/a)</td><td>38.48 (n/a)</td><td>1.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>48.51 (+10.07%)</td><td>44.74 (+17.63%)</td><td>43.60 (+5.59%)</td><td>43.16 <b>(+83.14%)</b></td><td>2.26 <b>(-73.44%)</b></td><td>48.48 (+10.07%)</td><td>44.72 (+17.63%)</td><td>43.57 (+5.59%)</td><td>43.13 <b>(+83.14%)</b></td><td>2.26 <b>(-73.44%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>44.07 (n/a)</td><td>38.04 (n/a)</td><td>41.29 (n/a)</td><td>23.57 (n/a)</td><td>8.50 (n/a)</td><td>44.05 (n/a)</td><td>38.01 (n/a)</td><td>41.27 (n/a)</td><td>23.55 (n/a)</td><td>8.49 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>13.25 (n/a)</td><td>12.23 (n/a)</td><td>12.24 (n/a)</td><td>10.68 (n/a)</td><td>0.97 (n/a)</td><td>13.24 (n/a)</td><td>12.22 (n/a)</td><td>12.23 (n/a)</td><td>10.67 (n/a)</td><td>0.97 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>25.41 (+3.69%)</td><td>23.71 (-1.46%)</td><td>23.68 (-2.28%)</td><td>22.13 (-4.07%)</td><td>1.25 <b>(+118.73%)</b></td><td>25.40 (+3.69%)</td><td>23.70 (-1.46%)</td><td>23.66 (-2.28%)</td><td>22.11 (-4.07%)</td><td>1.25 <b>(+118.73%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>24.51 (n/a)</td><td>24.07 (n/a)</td><td>24.23 (n/a)</td><td>23.07 (n/a)</td><td>0.57 (n/a)</td><td>24.49 (n/a)</td><td>24.05 (n/a)</td><td>24.21 (n/a)</td><td>23.05 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>43.03 (+3.92%)</td><td>41.17 (+7.29%)</td><td>41.72 (+5.00%)</td><td>39.13 <b>(+23.21%)</b></td><td>1.56 <b>(-58.99%)</b></td><td>43.00 (+3.92%)</td><td>41.14 (+7.29%)</td><td>41.69 (+5.00%)</td><td>39.11 <b>(+23.21%)</b></td><td>1.56 <b>(-58.99%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>41.40 (n/a)</td><td>38.37 (n/a)</td><td>39.73 (n/a)</td><td>31.76 (n/a)</td><td>3.81 (n/a)</td><td>41.38 (n/a)</td><td>38.35 (n/a)</td><td>39.71 (n/a)</td><td>31.74 (n/a)</td><td>3.80 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>42.89 (-3.68%)</td><td>40.29 (-5.96%)</td><td>41.48 (-3.01%)</td><td>34.85 (-16.39%)</td><td>3.27 <b>(+181.75%)</b></td><td>42.86 (-3.68%)</td><td>40.27 (-5.96%)</td><td>41.46 (-3.01%)</td><td>34.83 (-16.39%)</td><td>3.27 <b>(+181.75%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>44.53 (n/a)</td><td>42.85 (n/a)</td><td>42.77 (n/a)</td><td>41.69 (n/a)</td><td>1.16 (n/a)</td><td>44.50 (n/a)</td><td>42.82 (n/a)</td><td>42.74 (n/a)</td><td>41.66 (n/a)</td><td>1.16 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>9.49 (+0.86%)</td><td>8.98 (+3.41%)</td><td>9.16 (+3.98%)</td><td>8.35 (+6.54%)</td><td>0.47 (-16.82%)</td><td>9.47 (+0.86%)</td><td>8.96 (+3.41%)</td><td>9.14 (+3.98%)</td><td>8.34 (+6.54%)</td><td>0.47 (-16.82%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.40 (n/a)</td><td>8.68 (n/a)</td><td>8.81 (n/a)</td><td>7.84 (n/a)</td><td>0.57 (n/a)</td><td>9.39 (n/a)</td><td>8.67 (n/a)</td><td>8.79 (n/a)</td><td>7.82 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.06 (+1.91%)</td><td>0.96 (+12.41%)</td><td>0.96 (+9.30%)</td><td>0.81 (+16.90%)</td><td>0.09 <b>(-39.24%)</b></td><td>1.04 (+1.91%)</td><td>0.94 (+12.41%)</td><td>0.94 (+9.30%)</td><td>0.80 (+16.90%)</td><td>0.09 <b>(-39.24%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.04 (n/a)</td><td>0.85 (n/a)</td><td>0.88 (n/a)</td><td>0.70 (n/a)</td><td>0.15 (n/a)</td><td>1.02 (n/a)</td><td>0.84 (n/a)</td><td>0.86 (n/a)</td><td>0.68 (n/a)</td><td>0.14 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.32 (-12.33%)</td><td>1.20 (+6.59%)</td><td>1.21 (+11.43%)</td><td>1.10 <b>(+23.39%)</b></td><td>0.09 <b>(-62.80%)</b></td><td>1.30 (-12.33%)</td><td>1.19 (+6.59%)</td><td>1.20 (+11.43%)</td><td>1.09 <b>(+23.39%)</b></td><td>0.09 <b>(-62.80%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.50 (n/a)</td><td>1.13 (n/a)</td><td>1.09 (n/a)</td><td>0.89 (n/a)</td><td>0.23 (n/a)</td><td>1.48 (n/a)</td><td>1.11 (n/a)</td><td>1.08 (n/a)</td><td>0.88 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>20.07 (+6.32%)</td><td>17.21 (-3.52%)</td><td>16.65 (-8.75%)</td><td>15.98 (+2.70%)</td><td>1.69 <b>(+27.97%)</b></td><td>19.83 (+6.32%)</td><td>17.01 (-3.52%)</td><td>16.46 (-8.75%)</td><td>15.79 (+2.70%)</td><td>1.67 <b>(+27.97%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>18.87 (n/a)</td><td>17.83 (n/a)</td><td>18.25 (n/a)</td><td>15.56 (n/a)</td><td>1.32 (n/a)</td><td>18.66 (n/a)</td><td>17.63 (n/a)</td><td>18.04 (n/a)</td><td>15.38 (n/a)</td><td>1.30 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>14.55 (+2.64%)</td><td>13.23 (-3.69%)</td><td>13.22 (-3.59%)</td><td>11.83 (-10.49%)</td><td>0.96 <b>(+120.99%)</b></td><td>14.29 (+2.64%)</td><td>12.99 (-3.69%)</td><td>12.99 (-3.59%)</td><td>11.62 (-10.49%)</td><td>0.95 <b>(+120.99%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>14.17 (n/a)</td><td>13.73 (n/a)</td><td>13.72 (n/a)</td><td>13.22 (n/a)</td><td>0.44 (n/a)</td><td>13.92 (n/a)</td><td>13.49 (n/a)</td><td>13.48 (n/a)</td><td>12.99 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>9.04 (-7.65%)</td><td>7.76 (-6.19%)</td><td>7.60 (-4.56%)</td><td>7.07 (+18.14%)</td><td>0.76 <b>(-51.36%)</b></td><td>8.89 (-7.65%)</td><td>7.62 (-6.19%)</td><td>7.47 (-4.56%)</td><td>6.94 (+18.14%)</td><td>0.74 <b>(-51.36%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.79 (n/a)</td><td>8.27 (n/a)</td><td>7.96 (n/a)</td><td>5.98 (n/a)</td><td>1.55 (n/a)</td><td>9.62 (n/a)</td><td>8.13 (n/a)</td><td>7.82 (n/a)</td><td>5.88 (n/a)</td><td>1.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.73 (+10.12%)</td><td>6.04 (+8.11%)</td><td>5.89 (+5.75%)</td><td>5.48 (+13.08%)</td><td>0.51 (+2.12%)</td><td>6.63 (+10.12%)</td><td>5.95 (+8.11%)</td><td>5.80 (+5.75%)</td><td>5.39 (+13.08%)</td><td>0.51 (+2.12%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>6.11 (n/a)</td><td>5.59 (n/a)</td><td>5.57 (n/a)</td><td>4.85 (n/a)</td><td>0.50 (n/a)</td><td>6.02 (n/a)</td><td>5.50 (n/a)</td><td>5.48 (n/a)</td><td>4.77 (n/a)</td><td>0.50 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>13.28 (n/a)</td><td>12.37 (n/a)</td><td>12.63 (n/a)</td><td>10.70 (n/a)</td><td>1.07 (n/a)</td><td>13.27 (n/a)</td><td>12.36 (n/a)</td><td>12.63 (n/a)</td><td>10.70 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>13.44 (n/a)</td><td>12.58 (n/a)</td><td>12.90 (n/a)</td><td>11.10 (n/a)</td><td>0.96 (n/a)</td><td>13.44 (n/a)</td><td>12.57 (n/a)</td><td>12.89 (n/a)</td><td>11.09 (n/a)</td><td>0.96 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.20 (n/a)</td><td>165.40 (n/a)</td><td>162.50 (n/a)</td><td>118.50 (n/a)</td><td>34.77 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>191.70 (n/a)</td><td>166.36 (n/a)</td><td>166.70 (n/a)</td><td>152.10 (n/a)</td><td>16.13 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.30 (n/a)</td><td>170.14 (n/a)</td><td>153.70 (n/a)</td><td>128.90 (n/a)</td><td>44.47 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.10 (n/a)</td><td>166.04 (n/a)</td><td>168.40 (n/a)</td><td>124.50 (n/a)</td><td>31.49 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.20 (n/a)</td><td>184.96 (n/a)</td><td>173.40 (n/a)</td><td>149.80 (n/a)</td><td>36.68 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>287.40 (n/a)</td><td>189.90 (n/a)</td><td>171.30 (n/a)</td><td>133.40 (n/a)</td><td>60.10 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.50 (n/a)</td><td>163.62 (n/a)</td><td>158.10 (n/a)</td><td>132.00 (n/a)</td><td>35.88 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.10 (n/a)</td><td>184.80 (n/a)</td><td>179.40 (n/a)</td><td>171.00 (n/a)</td><td>16.89 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.30 (n/a)</td><td>150.44 (n/a)</td><td>142.60 (n/a)</td><td>125.70 (n/a)</td><td>22.07 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>335.00 (n/a)</td><td>191.64 (n/a)</td><td>155.70 (n/a)</td><td>123.50 (n/a)</td><td>85.79 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.10 (n/a)</td><td>174.36 (n/a)</td><td>160.70 (n/a)</td><td>129.10 (n/a)</td><td>45.38 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>181.50 (n/a)</td><td>161.02 (n/a)</td><td>160.70 (n/a)</td><td>146.10 (n/a)</td><td>14.66 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.70 (n/a)</td><td>164.40 (n/a)</td><td>161.30 (n/a)</td><td>123.90 (n/a)</td><td>29.86 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>204.60 (n/a)</td><td>218.20 (n/a)</td><td>168.50 (n/a)</td><td>24.04 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>207.60 (n/a)</td><td>189.08 (n/a)</td><td>182.10 (n/a)</td><td>174.00 (n/a)</td><td>16.60 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>363.80 (n/a)</td><td>224.56 (n/a)</td><td>210.10 (n/a)</td><td>124.30 (n/a)</td><td>86.59 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.90 (n/a)</td><td>164.98 (n/a)</td><td>168.50 (n/a)</td><td>143.80 (n/a)</td><td>20.00 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>227.70 (n/a)</td><td>180.62 (n/a)</td><td>159.80 (n/a)</td><td>143.40 (n/a)</td><td>38.00 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>245.50 (n/a)</td><td>181.10 (n/a)</td><td>179.50 (n/a)</td><td>123.30 (n/a)</td><td>57.27 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.90 (n/a)</td><td>173.28 (n/a)</td><td>169.10 (n/a)</td><td>133.80 (n/a)</td><td>32.60 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>180.28 (n/a)</td><td>166.90 (n/a)</td><td>164.70 (n/a)</td><td>21.23 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>261.80 (n/a)</td><td>194.52 (n/a)</td><td>180.70 (n/a)</td><td>168.00 (n/a)</td><td>38.51 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.80 (n/a)</td><td>166.58 (n/a)</td><td>175.50 (n/a)</td><td>130.60 (n/a)</td><td>29.68 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>247.10 (n/a)</td><td>208.50 (n/a)</td><td>205.70 (n/a)</td><td>178.30 (n/a)</td><td>25.10 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.06 (n/a)</td><td>248.60 (n/a)</td><td>189.24 (n/a)</td><td>184.40 (n/a)</td><td>117.00 (n/a)</td><td>48.99 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>212.60 (n/a)</td><td>171.54 (n/a)</td><td>176.30 (n/a)</td><td>131.80 (n/a)</td><td>30.08 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>240.00 (n/a)</td><td>183.10 (n/a)</td><td>195.50 (n/a)</td><td>131.30 (n/a)</td><td>46.11 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>227.80 (n/a)</td><td>185.10 (n/a)</td><td>175.10 (n/a)</td><td>162.90 (n/a)</td><td>25.48 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.26 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>232.80 (n/a)</td><td>184.88 (n/a)</td><td>191.80 (n/a)</td><td>124.50 (n/a)</td><td>39.03 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.29 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>219.60 (n/a)</td><td>194.64 (n/a)</td><td>213.40 (n/a)</td><td>112.90 (n/a)</td><td>45.79 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>241.60 (n/a)</td><td>188.08 (n/a)</td><td>185.20 (n/a)</td><td>152.80 (n/a)</td><td>32.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>234.80 (n/a)</td><td>209.66 (n/a)</td><td>213.30 (n/a)</td><td>187.20 (n/a)</td><td>18.73 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (+1.13%)</td><td>0.03 (-14.60%)</td><td>0.02 <b>(-27.68%)</b></td><td>0.02 (-8.71%)</td><td>0.01 (+3.02%)</td><td>193.00 (+9.53%)</td><td>169.06 (+17.53%)</td><td>183.40 <b>(+38.31%)</b></td><td>117.80 (-1.09%)</td><td>30.91 (+9.60%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>176.20 (n/a)</td><td>143.84 (n/a)</td><td>132.60 (n/a)</td><td>119.10 (n/a)</td><td>28.20 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-2.96%)</td><td>0.03 (+5.93%)</td><td>0.03 <b>(+27.58%)</b></td><td>0.02 (-5.28%)</td><td>0.01 (+18.94%)</td><td>235.00 (+5.57%)</td><td>156.20 (-3.33%)</td><td>125.10 <b>(-21.62%)</b></td><td>118.30 (+3.05%)</td><td>50.27 <b>(+26.25%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.60 (n/a)</td><td>161.58 (n/a)</td><td>159.60 (n/a)</td><td>114.80 (n/a)</td><td>39.82 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (+0.08%)</td><td>0.03 (+1.60%)</td><td>0.03 (+1.35%)</td><td>0.02 (-6.66%)</td><td>0.00 (+17.45%)</td><td>194.10 (+7.12%)</td><td>163.52 (-1.28%)</td><td>161.50 (-1.34%)</td><td>147.20 (-0.07%)</td><td>18.68 <b>(+24.14%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.20 (n/a)</td><td>165.64 (n/a)</td><td>163.70 (n/a)</td><td>147.30 (n/a)</td><td>15.05 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (+6.63%)</td><td>0.03 (+6.29%)</td><td>0.02 (+10.04%)</td><td>0.02 (+1.60%)</td><td>0.00 (+5.38%)</td><td>205.20 (-1.58%)</td><td>164.98 (-5.85%)</td><td>165.60 (-9.11%)</td><td>130.70 (-6.17%)</td><td>27.02 (-1.76%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>208.50 (n/a)</td><td>175.24 (n/a)</td><td>182.20 (n/a)</td><td>139.30 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-2.77%)</td><td>0.03 (+13.31%)</td><td>0.03 (+9.71%)</td><td>0.02 <b>(+26.93%)</b></td><td>0.00 <b>(-34.68%)</b></td><td>184.00 <b>(-21.23%)</b></td><td>152.96 (-14.46%)</td><td>152.10 (-8.81%)</td><td>129.80 (+2.85%)</td><td>22.24 <b>(-48.46%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>233.60 (n/a)</td><td>178.82 (n/a)</td><td>166.80 (n/a)</td><td>126.20 (n/a)</td><td>43.15 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-5.58%)</td><td>0.02 (-8.23%)</td><td>0.02 (-8.60%)</td><td>0.02 (-11.25%)</td><td>0.00 (-2.54%)</td><td>218.80 (+12.67%)</td><td>182.66 (+9.13%)</td><td>172.60 (+9.38%)</td><td>157.80 (+5.91%)</td><td>23.85 (+17.57%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.20 (n/a)</td><td>167.38 (n/a)</td><td>157.80 (n/a)</td><td>149.00 (n/a)</td><td>20.28 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (+13.38%)</td><td>0.02 (+7.31%)</td><td>0.02 (+0.73%)</td><td>0.02 <b>(+20.51%)</b></td><td>0.00 (+4.81%)</td><td>198.70 (-17.00%)</td><td>169.42 (-7.29%)</td><td>172.40 (-0.75%)</td><td>133.70 (-11.81%)</td><td>27.47 <b>(-22.67%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>239.40 (n/a)</td><td>182.74 (n/a)</td><td>173.70 (n/a)</td><td>151.60 (n/a)</td><td>35.52 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 <b>(-26.35%)</b></td><td>0.02 (-11.19%)</td><td>0.02 (+5.15%)</td><td>0.02 (-8.84%)</td><td>0.00 <b>(-57.78%)</b></td><td>252.80 (+9.72%)</td><td>213.92 (+9.22%)</td><td>208.20 (-4.93%)</td><td>182.20 <b>(+35.77%)</b></td><td>25.75 <b>(-36.97%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>230.40 (n/a)</td><td>195.86 (n/a)</td><td>219.00 (n/a)</td><td>134.20 (n/a)</td><td>40.85 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (+8.38%)</td><td>0.05 (-4.24%)</td><td>0.05 (-12.05%)</td><td>0.05 (+1.91%)</td><td>0.01 <b>(+28.23%)</b></td><td>181.40 (-1.84%)</td><td>160.56 (+5.11%)</td><td>168.10 (+13.66%)</td><td>120.10 (-7.69%)</td><td>23.64 (+11.34%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.80 (n/a)</td><td>152.76 (n/a)</td><td>147.90 (n/a)</td><td>130.10 (n/a)</td><td>21.23 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (+13.74%)</td><td>0.05 (-3.46%)</td><td>0.04 (-14.12%)</td><td>0.03 <b>(-26.54%)</b></td><td>0.01 <b>(+240.18%)</b></td><td>243.10 <b>(+36.11%)</b></td><td>176.92 (+9.60%)</td><td>190.20 (+16.47%)</td><td>128.90 (-12.07%)</td><td>48.55 <b>(+283.01%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>178.60 (n/a)</td><td>161.42 (n/a)</td><td>163.30 (n/a)</td><td>146.60 (n/a)</td><td>12.68 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (+10.32%)</td><td>0.05 (-7.28%)</td><td>0.05 (-8.99%)</td><td>0.04 (-14.69%)</td><td>0.01 <b>(+80.60%)</b></td><td>214.20 (+17.18%)</td><td>171.42 (+10.69%)</td><td>167.30 (+9.85%)</td><td>120.40 (-9.34%)</td><td>35.01 <b>(+86.63%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.80 (n/a)</td><td>154.86 (n/a)</td><td>152.30 (n/a)</td><td>132.80 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (+10.09%)</td><td>0.06 <b>(+21.33%)</b></td><td>0.06 <b>(+30.07%)</b></td><td>0.05 (+17.10%)</td><td>0.01 (+3.27%)</td><td>168.50 (-14.60%)</td><td>142.42 (-17.91%)</td><td>139.80 <b>(-23.10%)</b></td><td>115.70 (-9.11%)</td><td>23.64 (-18.90%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>173.50 (n/a)</td><td>181.80 (n/a)</td><td>127.30 (n/a)</td><td>29.14 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (-11.28%)</td><td>0.05 (-13.54%)</td><td>0.05 (-19.83%)</td><td>0.04 (-2.50%)</td><td>0.01 <b>(-27.85%)</b></td><td>188.90 (+2.61%)</td><td>162.18 (+14.47%)</td><td>156.70 <b>(+24.76%)</b></td><td>136.10 (+12.67%)</td><td>23.90 (-13.64%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>141.68 (n/a)</td><td>125.60 (n/a)</td><td>120.80 (n/a)</td><td>27.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (-14.94%)</td><td>0.05 (-7.96%)</td><td>0.05 (-5.35%)</td><td>0.04 (-15.72%)</td><td>0.01 (-15.11%)</td><td>225.90 (+18.64%)</td><td>174.76 (+8.72%)</td><td>167.40 (+5.68%)</td><td>144.80 (+17.53%)</td><td>31.17 <b>(+22.66%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>190.40 (n/a)</td><td>160.74 (n/a)</td><td>158.40 (n/a)</td><td>123.20 (n/a)</td><td>25.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (-6.23%)</td><td>0.05 (+8.19%)</td><td>0.05 (+9.06%)</td><td>0.05 (+19.45%)</td><td>0.00 <b>(-56.80%)</b></td><td>177.70 (-16.30%)</td><td>167.54 (-8.78%)</td><td>167.70 (-8.31%)</td><td>156.40 (+6.68%)</td><td>9.76 <b>(-60.89%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>183.66 (n/a)</td><td>182.90 (n/a)</td><td>146.60 (n/a)</td><td>24.95 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 <b>(-29.30%)</b></td><td>0.05 (-6.70%)</td><td>0.05 (-0.57%)</td><td>0.04 <b>(+40.75%)</b></td><td>0.01 <b>(-62.08%)</b></td><td>218.90 <b>(-28.95%)</b></td><td>173.32 (-3.53%)</td><td>164.40 (+0.55%)</td><td>145.50 <b>(+41.40%)</b></td><td>28.56 <b>(-62.91%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>308.10 (n/a)</td><td>179.66 (n/a)</td><td>163.50 (n/a)</td><td>102.90 (n/a)</td><td>77.00 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (-4.41%)</td><td>0.05 (-0.20%)</td><td>0.05 (+3.87%)</td><td>0.04 (-2.39%)</td><td>0.01 (-6.54%)</td><td>200.80 (+2.45%)</td><td>170.36 (+0.14%)</td><td>164.40 (-3.69%)</td><td>152.60 (+4.66%)</td><td>19.55 (+0.40%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.00 (n/a)</td><td>170.12 (n/a)</td><td>170.70 (n/a)</td><td>145.80 (n/a)</td><td>19.47 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (+2.66%)</td><td>0.04 (+0.30%)</td><td>0.04 (+3.76%)</td><td>0.03 (+0.97%)</td><td>0.01 <b>(+38.23%)</b></td><td>311.30 (-0.99%)</td><td>234.64 (+2.89%)</td><td>208.90 (-3.60%)</td><td>171.60 (-2.61%)</td><td>70.23 <b>(+32.35%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>314.40 (n/a)</td><td>228.06 (n/a)</td><td>216.70 (n/a)</td><td>176.20 (n/a)</td><td>53.06 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (+4.22%)</td><td>0.11 (+13.34%)</td><td>0.10 (+11.93%)</td><td>0.09 <b>(+34.36%)</b></td><td>0.02 (-19.79%)</td><td>178.50 <b>(-25.59%)</b></td><td>153.24 (-14.39%)</td><td>164.10 (-10.67%)</td><td>111.50 (-4.04%)</td><td>26.08 <b>(-42.63%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>239.90 (n/a)</td><td>179.00 (n/a)</td><td>183.70 (n/a)</td><td>116.20 (n/a)</td><td>45.45 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (+10.99%)</td><td>0.11 (+10.92%)</td><td>0.10 (+8.98%)</td><td>0.09 (+1.90%)</td><td>0.02 <b>(+35.79%)</b></td><td>184.80 (-1.86%)</td><td>152.50 (-9.04%)</td><td>156.40 (-8.27%)</td><td>121.10 (-9.90%)</td><td>25.63 (+19.74%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>188.30 (n/a)</td><td>167.66 (n/a)</td><td>170.50 (n/a)</td><td>134.40 (n/a)</td><td>21.40 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (+17.32%)</td><td>0.11 (+15.84%)</td><td>0.11 <b>(+32.05%)</b></td><td>0.07 (-9.87%)</td><td>0.03 <b>(+104.48%)</b></td><td>233.30 (+10.99%)</td><td>164.48 (-9.68%)</td><td>143.30 <b>(-24.26%)</b></td><td>125.60 (-14.73%)</td><td>47.70 <b>(+89.14%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>210.20 (n/a)</td><td>182.10 (n/a)</td><td>189.20 (n/a)</td><td>147.30 (n/a)</td><td>25.22 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 <b>(+20.34%)</b></td><td>0.11 <b>(+25.80%)</b></td><td>0.12 <b>(+40.79%)</b></td><td>0.09 (+18.87%)</td><td>0.02 <b>(+55.28%)</b></td><td>190.80 (-15.87%)</td><td>148.96 (-19.23%)</td><td>131.40 <b>(-28.97%)</b></td><td>119.40 (-16.91%)</td><td>33.55 (+10.07%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>226.80 (n/a)</td><td>184.42 (n/a)</td><td>185.00 (n/a)</td><td>143.70 (n/a)</td><td>30.48 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (-10.12%)</td><td>0.12 <b>(+29.40%)</b></td><td>0.12 <b>(+32.93%)</b></td><td>0.10 <b>(+131.86%)</b></td><td>0.01 <b>(-71.60%)</b></td><td>158.70 <b>(-56.86%)</b></td><td>141.26 <b>(-32.42%)</b></td><td>140.30 <b>(-24.77%)</b></td><td>125.80 (+11.23%)</td><td>12.40 <b>(-86.89%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>367.90 (n/a)</td><td>209.04 (n/a)</td><td>186.50 (n/a)</td><td>113.10 (n/a)</td><td>94.63 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (-3.84%)</td><td>0.09 (+2.97%)</td><td>0.10 (+9.18%)</td><td>0.08 (+2.01%)</td><td>0.01 (-4.36%)</td><td>216.60 (-1.99%)</td><td>180.32 (-2.95%)</td><td>170.40 (-8.39%)</td><td>149.90 (+4.02%)</td><td>28.47 (+0.22%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>221.00 (n/a)</td><td>185.80 (n/a)</td><td>186.00 (n/a)</td><td>144.10 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (+18.09%)</td><td>0.11 <b>(+33.08%)</b></td><td>0.11 <b>(+47.31%)</b></td><td>0.07 (+7.48%)</td><td>0.03 <b>(+28.77%)</b></td><td>247.80 (-6.95%)</td><td>158.72 <b>(-23.59%)</b></td><td>154.80 <b>(-32.11%)</b></td><td>116.50 (-15.27%)</td><td>53.25 (+2.39%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>266.30 (n/a)</td><td>207.72 (n/a)</td><td>228.00 (n/a)</td><td>137.50 (n/a)</td><td>52.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (+15.21%)</td><td>0.08 <b>(+26.38%)</b></td><td>0.09 <b>(+31.01%)</b></td><td>0.06 <b>(+31.83%)</b></td><td>0.01 (+2.07%)</td><td>260.40 <b>(-24.15%)</b></td><td>197.12 <b>(-21.67%)</b></td><td>181.70 <b>(-23.69%)</b></td><td>172.00 (-13.22%)</td><td>36.06 <b>(-33.66%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>343.30 (n/a)</td><td>251.64 (n/a)</td><td>238.10 (n/a)</td><td>198.20 (n/a)</td><td>54.35 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.26 <b>(-25.36%)</b></td><td>0.22 (+4.82%)</td><td>0.25 <b>(+44.31%)</b></td><td>0.11 <b>(-27.27%)</b></td><td>0.06 <b>(-23.78%)</b></td><td>287.60 <b>(+37.54%)</b></td><td>166.22 (-3.76%)</td><td>132.00 <b>(-30.75%)</b></td><td>126.30 <b>(+33.93%)</b></td><td>69.06 <b>(+44.37%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.35 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>209.10 (n/a)</td><td>172.72 (n/a)</td><td>190.60 (n/a)</td><td>94.30 (n/a)</td><td>47.83 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.28 <b>(+48.96%)</b></td><td>0.25 <b>(+38.95%)</b></td><td>0.25 <b>(+34.89%)</b></td><td>0.22 <b>(+38.99%)</b></td><td>0.02 <b>(+76.87%)</b></td><td>146.60 <b>(-28.07%)</b></td><td>131.20 <b>(-27.89%)</b></td><td>130.60 <b>(-25.84%)</b></td><td>115.80 <b>(-32.87%)</b></td><td>10.93 (-15.42%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>181.94 (n/a)</td><td>176.10 (n/a)</td><td>172.50 (n/a)</td><td>12.92 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.31 <b>(+37.18%)</b></td><td>0.24 <b>(+24.26%)</b></td><td>0.22 (+19.01%)</td><td>0.22 <b>(+33.72%)</b></td><td>0.04 <b>(+63.38%)</b></td><td>152.40 <b>(-25.18%)</b></td><td>139.94 (-19.05%)</td><td>146.30 (-15.97%)</td><td>105.80 <b>(-27.08%)</b></td><td>19.33 (-12.38%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>203.70 (n/a)</td><td>172.88 (n/a)</td><td>174.10 (n/a)</td><td>145.10 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 <b>(-22.69%)</b></td><td>0.22 (+6.70%)</td><td>0.22 (+18.84%)</td><td>0.21 <b>(+48.96%)</b></td><td>0.00 <b>(-93.72%)</b></td><td>153.70 <b>(-32.88%)</b></td><td>150.78 (-11.92%)</td><td>150.00 (-15.87%)</td><td>147.60 <b>(+29.36%)</b></td><td>2.56 <b>(-94.42%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>229.00 (n/a)</td><td>171.18 (n/a)</td><td>178.30 (n/a)</td><td>114.10 (n/a)</td><td>45.91 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.26 (+18.51%)</td><td>0.22 <b>(+27.34%)</b></td><td>0.21 <b>(+23.92%)</b></td><td>0.20 <b>(+45.70%)</b></td><td>0.03 (-12.17%)</td><td>164.40 <b>(-31.36%)</b></td><td>148.78 <b>(-22.42%)</b></td><td>153.20 (-19.33%)</td><td>126.50 (-15.61%)</td><td>16.39 <b>(-48.74%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>239.50 (n/a)</td><td>191.78 (n/a)</td><td>189.90 (n/a)</td><td>149.90 (n/a)</td><td>31.98 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.28 <b>(+23.55%)</b></td><td>0.22 <b>(+27.87%)</b></td><td>0.23 <b>(+24.58%)</b></td><td>0.14 <b>(+31.79%)</b></td><td>0.05 (-5.53%)</td><td>239.60 <b>(-24.13%)</b></td><td>161.88 <b>(-25.44%)</b></td><td>143.20 (-19.73%)</td><td>118.30 (-19.03%)</td><td>48.25 <b>(-41.26%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>315.80 (n/a)</td><td>217.12 (n/a)</td><td>178.40 (n/a)</td><td>146.10 (n/a)</td><td>82.14 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (-1.93%)</td><td>0.18 (+17.00%)</td><td>0.17 (+17.81%)</td><td>0.17 <b>(+31.14%)</b></td><td>0.01 <b>(-61.77%)</b></td><td>195.90 <b>(-23.74%)</b></td><td>185.70 (-15.97%)</td><td>190.80 (-15.09%)</td><td>172.70 (+1.95%)</td><td>9.84 <b>(-69.34%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>256.90 (n/a)</td><td>220.98 (n/a)</td><td>224.70 (n/a)</td><td>169.40 (n/a)</td><td>32.10 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (+2.95%)</td><td>0.03 (+9.12%)</td><td>0.03 (+13.98%)</td><td>0.03 (+17.65%)</td><td>0.00 <b>(-44.95%)</b></td><td>158.70 (-15.00%)</td><td>146.36 (-9.15%)</td><td>145.30 (-12.31%)</td><td>134.60 (-2.89%)</td><td>8.82 <b>(-54.00%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>186.70 (n/a)</td><td>161.10 (n/a)</td><td>165.70 (n/a)</td><td>138.60 (n/a)</td><td>19.17 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 <b>(+20.85%)</b></td><td>0.03 <b>(+23.48%)</b></td><td>0.03 <b>(+31.58%)</b></td><td>0.02 <b>(+32.70%)</b></td><td>0.00 (-8.28%)</td><td>169.90 <b>(-24.62%)</b></td><td>152.78 <b>(-20.04%)</b></td><td>156.10 <b>(-24.00%)</b></td><td>121.90 (-17.24%)</td><td>19.17 <b>(-43.19%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.40 (n/a)</td><td>191.08 (n/a)</td><td>205.40 (n/a)</td><td>147.30 (n/a)</td><td>33.75 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.00 (+0.00%)</td><td>0.00 (-0.00%)</td><td>0.00 (-0.00%)</td><td>0.00 (-0.00%)</td><td>0.00 <b>(+750.78%)</b></td><td>4746120.60 (+0.00%)</td><td>4746043.57 (+0.00%)</td><td>4746024.00 (+0.00%)</td><td>4745986.10 (-0.00%)</td><td>69.35 <b>(+760.34%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4746029.40 (n/a)</td><td>4746023.70 (n/a)</td><td>4746023.70 (n/a)</td><td>4746018.00 (n/a)</td><td>8.06 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 <b>(+23.79%)</b></td><td>0.02 (+15.53%)</td><td>0.02 (+14.97%)</td><td>0.02 (+2.60%)</td><td>0.00 <b>(+92.05%)</b></td><td>219.10 (-2.54%)</td><td>174.88 (-12.06%)</td><td>176.10 (-13.04%)</td><td>139.90 (-19.23%)</td><td>30.83 <b>(+51.37%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>224.80 (n/a)</td><td>198.86 (n/a)</td><td>202.50 (n/a)</td><td>173.20 (n/a)</td><td>20.37 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (+16.03%)</td><td>0.03 (+7.09%)</td><td>0.02 (+1.10%)</td><td>0.02 (-0.03%)</td><td>0.00 <b>(+71.48%)</b></td><td>199.00 (+0.05%)</td><td>164.46 (-5.12%)</td><td>172.30 (-1.09%)</td><td>126.30 (-13.85%)</td><td>29.06 <b>(+47.29%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.90 (n/a)</td><td>173.34 (n/a)</td><td>174.20 (n/a)</td><td>146.60 (n/a)</td><td>19.73 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-2.51%)</td><td>0.02 (-7.24%)</td><td>0.02 (-6.09%)</td><td>0.02 (-8.32%)</td><td>0.00 (+16.95%)</td><td>217.10 (+9.04%)</td><td>185.44 (+8.65%)</td><td>178.60 (+6.50%)</td><td>148.50 (+2.56%)</td><td>30.20 <b>(+34.47%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.10 (n/a)</td><td>170.68 (n/a)</td><td>167.70 (n/a)</td><td>144.80 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 <b>(+28.49%)</b></td><td>0.03 (+14.55%)</td><td>0.03 (+3.00%)</td><td>0.02 <b>(+31.59%)</b></td><td>0.01 <b>(+24.54%)</b></td><td>171.40 <b>(-23.99%)</b></td><td>148.30 (-13.11%)</td><td>159.00 (-2.93%)</td><td>97.50 <b>(-22.12%)</b></td><td>29.64 <b>(-28.85%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.50 (n/a)</td><td>170.68 (n/a)</td><td>163.80 (n/a)</td><td>125.20 (n/a)</td><td>41.66 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-7.43%)</td><td>0.03 (-12.34%)</td><td>0.02 <b>(-25.23%)</b></td><td>0.02 (-2.77%)</td><td>0.00 <b>(-38.59%)</b></td><td>212.90 (+2.85%)</td><td>168.00 (+9.20%)</td><td>164.80 <b>(+33.77%)</b></td><td>124.30 (+7.99%)</td><td>31.64 <b>(-34.30%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>207.00 (n/a)</td><td>153.84 (n/a)</td><td>123.20 (n/a)</td><td>115.10 (n/a)</td><td>48.16 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-18.99%)</td><td>0.02 (-7.32%)</td><td>0.02 (+0.96%)</td><td>0.02 (-18.54%)</td><td>0.01 <b>(-29.43%)</b></td><td>252.60 <b>(+22.74%)</b></td><td>187.36 (+6.10%)</td><td>184.50 (-0.97%)</td><td>126.20 <b>(+23.36%)</b></td><td>46.43 (+8.88%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>176.58 (n/a)</td><td>186.30 (n/a)</td><td>102.30 (n/a)</td><td>42.64 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-15.01%)</td><td>0.02 (-13.27%)</td><td>0.02 (-7.96%)</td><td>0.02 (-11.66%)</td><td>0.00 <b>(-31.70%)</b></td><td>227.90 (+13.21%)</td><td>196.50 (+14.22%)</td><td>192.60 (+8.63%)</td><td>163.10 (+17.68%)</td><td>27.91 (-7.76%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.30 (n/a)</td><td>172.04 (n/a)</td><td>177.30 (n/a)</td><td>138.60 (n/a)</td><td>30.26 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 <b>(-35.98%)</b></td><td>0.02 <b>(-21.44%)</b></td><td>0.02 (-3.42%)</td><td>0.02 (-18.22%)</td><td>0.00 <b>(-65.69%)</b></td><td>223.00 <b>(+22.26%)</b></td><td>179.28 <b>(+22.04%)</b></td><td>171.00 (+3.51%)</td><td>161.70 <b>(+56.23%)</b></td><td>24.78 <b>(-31.99%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>182.40 (n/a)</td><td>146.90 (n/a)</td><td>165.20 (n/a)</td><td>103.50 (n/a)</td><td>36.43 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (+11.98%)</td><td>0.02 (+2.12%)</td><td>0.02 (+4.97%)</td><td>0.02 (-0.42%)</td><td>0.01 (+17.34%)</td><td>231.00 (+0.39%)</td><td>175.44 (-1.28%)</td><td>165.90 (-4.71%)</td><td>122.80 (-10.69%)</td><td>40.62 (+6.00%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>177.72 (n/a)</td><td>174.10 (n/a)</td><td>137.50 (n/a)</td><td>38.32 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-10.98%)</td><td>0.02 (-6.11%)</td><td>0.02 (-3.02%)</td><td>0.02 (+18.44%)</td><td>0.00 <b>(-35.92%)</b></td><td>218.20 (-15.59%)</td><td>181.20 (+1.63%)</td><td>185.50 (+3.11%)</td><td>129.30 (+12.34%)</td><td>32.58 <b>(-41.12%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>258.50 (n/a)</td><td>178.30 (n/a)</td><td>179.90 (n/a)</td><td>115.10 (n/a)</td><td>55.34 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (+0.91%)</td><td>0.02 (+6.56%)</td><td>0.02 (+0.73%)</td><td>0.02 (+18.23%)</td><td>0.00 <b>(-22.12%)</b></td><td>201.90 (-15.42%)</td><td>169.92 (-8.66%)</td><td>172.40 (-0.69%)</td><td>128.00 (-0.85%)</td><td>30.01 <b>(-37.16%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.70 (n/a)</td><td>186.04 (n/a)</td><td>173.60 (n/a)</td><td>129.10 (n/a)</td><td>47.76 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (+18.40%)</td><td>0.02 (+10.78%)</td><td>0.02 (+2.51%)</td><td>0.02 <b>(+45.03%)</b></td><td>0.01 (-3.20%)</td><td>205.60 <b>(-31.05%)</b></td><td>178.18 (-12.17%)</td><td>191.00 (-2.45%)</td><td>124.00 (-15.53%)</td><td>33.99 <b>(-43.52%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>298.20 (n/a)</td><td>202.88 (n/a)</td><td>195.80 (n/a)</td><td>146.80 (n/a)</td><td>60.19 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-8.61%)</td><td>0.03 (+5.59%)</td><td>0.03 <b>(+24.42%)</b></td><td>0.02 (-9.13%)</td><td>0.01 (+1.35%)</td><td>235.80 (+10.03%)</td><td>172.58 (-4.39%)</td><td>161.20 (-19.60%)</td><td>128.30 (+9.38%)</td><td>48.47 (+17.54%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.30 (n/a)</td><td>180.50 (n/a)</td><td>200.50 (n/a)</td><td>117.30 (n/a)</td><td>41.23 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (-2.36%)</td><td>0.05 (+3.08%)</td><td>0.05 (+0.13%)</td><td>0.04 (+10.26%)</td><td>0.00 <b>(-29.95%)</b></td><td>185.70 (-9.33%)</td><td>164.94 (-3.59%)</td><td>163.30 (-0.12%)</td><td>153.60 (+2.40%)</td><td>13.23 <b>(-36.45%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>204.80 (n/a)</td><td>171.08 (n/a)</td><td>163.50 (n/a)</td><td>150.00 (n/a)</td><td>20.83 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (-4.69%)</td><td>0.05 (-12.57%)</td><td>0.05 (-10.30%)</td><td>0.03 <b>(-36.27%)</b></td><td>0.01 <b>(+77.33%)</b></td><td>255.90 <b>(+56.90%)</b></td><td>178.32 <b>(+20.63%)</b></td><td>175.50 (+11.50%)</td><td>126.60 (+4.98%)</td><td>52.91 <b>(+179.50%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>163.10 (n/a)</td><td>147.82 (n/a)</td><td>157.40 (n/a)</td><td>120.60 (n/a)</td><td>18.93 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (+0.70%)</td><td>0.04 (-0.57%)</td><td>0.04 (-12.82%)</td><td>0.04 (+6.26%)</td><td>0.00 (-15.45%)</td><td>224.00 (-5.88%)</td><td>204.72 (+0.04%)</td><td>216.60 (+14.72%)</td><td>174.10 (-0.68%)</td><td>22.61 <b>(-22.15%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>238.00 (n/a)</td><td>204.64 (n/a)</td><td>188.80 (n/a)</td><td>175.30 (n/a)</td><td>29.05 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (-10.00%)</td><td>0.04 (+0.14%)</td><td>0.04 (-10.29%)</td><td>0.04 <b>(+22.74%)</b></td><td>0.00 <b>(-69.26%)</b></td><td>206.10 (-18.54%)</td><td>193.66 (-3.24%)</td><td>199.20 (+11.47%)</td><td>180.60 (+11.14%)</td><td>11.67 <b>(-72.61%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.00 (n/a)</td><td>200.14 (n/a)</td><td>178.70 (n/a)</td><td>162.50 (n/a)</td><td>42.60 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 <b>(+21.51%)</b></td><td>0.06 (+8.50%)</td><td>0.05 (+6.31%)</td><td>0.05 (+8.22%)</td><td>0.01 <b>(+62.73%)</b></td><td>174.90 (-7.61%)</td><td>151.60 (-6.81%)</td><td>150.30 (-5.94%)</td><td>114.70 (-17.72%)</td><td>23.87 <b>(+22.59%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.30 (n/a)</td><td>162.68 (n/a)</td><td>159.80 (n/a)</td><td>139.40 (n/a)</td><td>19.47 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (-18.77%)</td><td>0.05 (-12.40%)</td><td>0.05 (-10.03%)</td><td>0.04 (-2.67%)</td><td>0.01 <b>(-48.88%)</b></td><td>203.50 (+2.73%)</td><td>174.56 (+12.07%)</td><td>174.90 (+11.12%)</td><td>150.60 <b>(+23.14%)</b></td><td>19.18 <b>(-34.69%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.10 (n/a)</td><td>155.76 (n/a)</td><td>157.40 (n/a)</td><td>122.30 (n/a)</td><td>29.37 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 <b>(-29.68%)</b></td><td>0.04 <b>(-22.18%)</b></td><td>0.04 <b>(-21.47%)</b></td><td>0.04 (-13.48%)</td><td>0.00 <b>(-58.33%)</b></td><td>206.70 (+15.54%)</td><td>187.06 <b>(+26.70%)</b></td><td>190.00 <b>(+27.35%)</b></td><td>163.90 <b>(+42.15%)</b></td><td>15.61 <b>(-31.09%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>178.90 (n/a)</td><td>147.64 (n/a)</td><td>149.20 (n/a)</td><td>115.30 (n/a)</td><td>22.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (-10.19%)</td><td>0.05 (-9.91%)</td><td>0.05 (-13.03%)</td><td>0.04 (+2.53%)</td><td>0.01 <b>(-29.94%)</b></td><td>189.30 (-2.47%)</td><td>174.84 (+9.84%)</td><td>179.60 (+14.98%)</td><td>140.50 (+11.33%)</td><td>19.67 <b>(-25.55%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.10 (n/a)</td><td>159.18 (n/a)</td><td>156.20 (n/a)</td><td>126.20 (n/a)</td><td>26.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 <b>(-21.54%)</b></td><td>0.04 <b>(-23.53%)</b></td><td>0.04 <b>(-32.03%)</b></td><td>0.04 (-5.91%)</td><td>0.01 <b>(-49.43%)</b></td><td>207.90 (+6.29%)</td><td>188.12 <b>(+28.39%)</b></td><td>193.40 <b>(+47.18%)</b></td><td>156.30 <b>(+27.49%)</b></td><td>19.60 <b>(-33.76%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>146.52 (n/a)</td><td>131.40 (n/a)</td><td>122.60 (n/a)</td><td>29.59 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (-3.38%)</td><td>0.05 (-10.71%)</td><td>0.04 (-16.52%)</td><td>0.04 <b>(-23.01%)</b></td><td>0.01 <b>(+74.12%)</b></td><td>231.20 <b>(+29.89%)</b></td><td>182.82 (+13.88%)</td><td>184.30 (+19.75%)</td><td>154.00 (+3.56%)</td><td>31.41 <b>(+130.49%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>178.00 (n/a)</td><td>160.54 (n/a)</td><td>153.90 (n/a)</td><td>148.70 (n/a)</td><td>13.63 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (-2.88%)</td><td>0.05 (-3.83%)</td><td>0.05 (-0.44%)</td><td>0.04 (+1.37%)</td><td>0.01 (-5.99%)</td><td>203.60 (-1.36%)</td><td>170.70 (+3.69%)</td><td>165.70 (+0.42%)</td><td>128.00 (+2.98%)</td><td>29.69 (-3.95%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.40 (n/a)</td><td>164.62 (n/a)</td><td>165.00 (n/a)</td><td>124.30 (n/a)</td><td>30.92 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (-10.50%)</td><td>0.05 (-9.18%)</td><td>0.05 (-1.27%)</td><td>0.04 <b>(-23.12%)</b></td><td>0.01 <b>(+38.72%)</b></td><td>211.30 <b>(+30.11%)</b></td><td>170.86 (+11.50%)</td><td>160.60 (+1.32%)</td><td>145.40 (+11.76%)</td><td>27.25 <b>(+103.56%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>162.40 (n/a)</td><td>153.24 (n/a)</td><td>158.50 (n/a)</td><td>130.10 (n/a)</td><td>13.39 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (-6.28%)</td><td>0.05 (-4.81%)</td><td>0.05 (-1.31%)</td><td>0.03 (-1.21%)</td><td>0.01 (-5.52%)</td><td>246.70 (+1.23%)</td><td>179.90 (+4.89%)</td><td>158.60 (+1.34%)</td><td>129.70 (+6.66%)</td><td>46.64 (+1.65%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.70 (n/a)</td><td>171.52 (n/a)</td><td>156.50 (n/a)</td><td>121.60 (n/a)</td><td>45.89 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (+18.46%)</td><td>0.05 (-5.26%)</td><td>0.04 <b>(-20.91%)</b></td><td>0.04 (+1.68%)</td><td>0.01 <b>(+48.84%)</b></td><td>206.90 (-1.66%)</td><td>174.80 (+7.44%)</td><td>185.70 <b>(+26.50%)</b></td><td>115.00 (-15.57%)</td><td>34.96 (+16.00%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.40 (n/a)</td><td>162.70 (n/a)</td><td>146.80 (n/a)</td><td>136.20 (n/a)</td><td>30.14 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (-19.45%)</td><td>0.04 (-19.51%)</td><td>0.04 <b>(-25.80%)</b></td><td>0.03 (-19.48%)</td><td>0.01 (-16.62%)</td><td>301.30 <b>(+24.20%)</b></td><td>204.60 <b>(+24.85%)</b></td><td>209.10 <b>(+34.82%)</b></td><td>128.20 <b>(+24.10%)</b></td><td>64.09 <b>(+27.62%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>242.60 (n/a)</td><td>163.88 (n/a)</td><td>155.10 (n/a)</td><td>103.30 (n/a)</td><td>50.22 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (-6.96%)</td><td>0.05 (-4.48%)</td><td>0.05 (-1.02%)</td><td>0.04 (-3.01%)</td><td>0.01 (-12.07%)</td><td>219.60 (+3.10%)</td><td>174.56 (+4.33%)</td><td>167.40 (+1.03%)</td><td>139.60 (+7.47%)</td><td>29.51 (-1.97%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>167.32 (n/a)</td><td>165.70 (n/a)</td><td>129.90 (n/a)</td><td>30.10 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (-12.23%)</td><td>0.10 (-7.05%)</td><td>0.10 (-8.61%)</td><td>0.09 (+1.61%)</td><td>0.01 <b>(-52.04%)</b></td><td>183.20 (-1.61%)</td><td>167.78 (+6.81%)</td><td>167.20 (+9.42%)</td><td>157.60 (+13.96%)</td><td>9.53 <b>(-46.83%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>186.20 (n/a)</td><td>157.08 (n/a)</td><td>152.80 (n/a)</td><td>138.30 (n/a)</td><td>17.93 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (-19.40%)</td><td>0.10 (-17.52%)</td><td>0.09 <b>(-20.58%)</b></td><td>0.08 <b>(-21.41%)</b></td><td>0.02 (-13.52%)</td><td>212.40 <b>(+27.26%)</b></td><td>174.84 <b>(+21.74%)</b></td><td>173.20 <b>(+25.96%)</b></td><td>136.80 <b>(+24.14%)</b></td><td>31.99 <b>(+34.29%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>166.90 (n/a)</td><td>143.62 (n/a)</td><td>137.50 (n/a)</td><td>110.20 (n/a)</td><td>23.82 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (-13.91%)</td><td>0.08 (+2.84%)</td><td>0.08 (+9.44%)</td><td>0.07 <b>(+24.09%)</b></td><td>0.01 <b>(-60.03%)</b></td><td>226.90 (-19.42%)</td><td>198.18 (-7.13%)</td><td>200.20 (-8.63%)</td><td>171.30 (+16.14%)</td><td>20.38 <b>(-62.31%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>281.60 (n/a)</td><td>213.40 (n/a)</td><td>219.10 (n/a)</td><td>147.50 (n/a)</td><td>54.07 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (-6.43%)</td><td>0.09 (+6.96%)</td><td>0.10 (+16.06%)</td><td>0.07 (-0.86%)</td><td>0.01 <b>(-21.55%)</b></td><td>223.70 (+0.86%)</td><td>179.06 (-7.13%)</td><td>170.40 (-13.85%)</td><td>162.70 (+6.90%)</td><td>25.27 (-14.83%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>192.80 (n/a)</td><td>197.80 (n/a)</td><td>152.20 (n/a)</td><td>29.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 <b>(-27.78%)</b></td><td>0.09 (-7.25%)</td><td>0.10 (+1.90%)</td><td>0.05 (+7.22%)</td><td>0.03 <b>(-39.91%)</b></td><td>303.90 (-6.72%)</td><td>189.88 (+0.26%)</td><td>170.60 (-1.84%)</td><td>140.50 <b>(+38.56%)</b></td><td>66.66 <b>(-22.00%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>325.80 (n/a)</td><td>189.38 (n/a)</td><td>173.80 (n/a)</td><td>101.40 (n/a)</td><td>85.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (+6.57%)</td><td>0.11 (+10.72%)</td><td>0.11 (+9.00%)</td><td>0.09 <b>(+21.69%)</b></td><td>0.02 (-13.99%)</td><td>176.40 (-17.80%)</td><td>153.10 (-10.71%)</td><td>146.70 (-8.26%)</td><td>128.80 (-6.19%)</td><td>21.89 <b>(-32.46%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.60 (n/a)</td><td>171.46 (n/a)</td><td>159.90 (n/a)</td><td>137.30 (n/a)</td><td>32.40 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (+13.71%)</td><td>0.10 (-1.68%)</td><td>0.09 (-12.03%)</td><td>0.08 (-14.87%)</td><td>0.03 <b>(+132.99%)</b></td><td>213.70 (+17.42%)</td><td>170.38 (+7.56%)</td><td>182.50 (+13.71%)</td><td>114.10 (-12.03%)</td><td>46.91 <b>(+150.75%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.00 (n/a)</td><td>158.40 (n/a)</td><td>160.50 (n/a)</td><td>129.70 (n/a)</td><td>18.71 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 <b>(+24.56%)</b></td><td>0.10 (-7.66%)</td><td>0.09 (-15.04%)</td><td>0.07 <b>(-22.31%)</b></td><td>0.03 <b>(+147.12%)</b></td><td>229.90 <b>(+28.72%)</b></td><td>172.46 (+14.09%)</td><td>180.20 (+17.70%)</td><td>106.50 (-19.68%)</td><td>44.29 <b>(+143.81%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>178.60 (n/a)</td><td>151.16 (n/a)</td><td>153.10 (n/a)</td><td>132.60 (n/a)</td><td>18.17 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 <b>(-26.04%)</b></td><td>0.08 (-13.80%)</td><td>0.08 (-13.43%)</td><td>0.07 (-2.69%)</td><td>0.01 <b>(-49.33%)</b></td><td>229.10 (+2.78%)</td><td>201.92 (+13.20%)</td><td>212.10 (+15.52%)</td><td>172.60 <b>(+35.27%)</b></td><td>26.21 <b>(-30.20%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>222.90 (n/a)</td><td>178.38 (n/a)</td><td>183.60 (n/a)</td><td>127.60 (n/a)</td><td>37.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (+7.43%)</td><td>0.10 (+4.21%)</td><td>0.11 (+4.48%)</td><td>0.08 (-7.71%)</td><td>0.02 <b>(+28.16%)</b></td><td>211.20 (+8.36%)</td><td>162.80 (-3.04%)</td><td>149.20 (-4.30%)</td><td>131.20 (-6.88%)</td><td>31.41 <b>(+27.11%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>167.90 (n/a)</td><td>155.90 (n/a)</td><td>140.90 (n/a)</td><td>24.71 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (+12.54%)</td><td>0.12 (+8.22%)</td><td>0.11 (+14.89%)</td><td>0.09 (+10.74%)</td><td>0.02 (-4.71%)</td><td>174.70 (-9.67%)</td><td>145.16 (-8.34%)</td><td>148.70 (-12.99%)</td><td>111.10 (-11.19%)</td><td>23.25 <b>(-22.56%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>193.40 (n/a)</td><td>158.36 (n/a)</td><td>170.90 (n/a)</td><td>125.10 (n/a)</td><td>30.03 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 <b>(+34.51%)</b></td><td>0.11 (+15.24%)</td><td>0.10 (-7.72%)</td><td>0.09 (+15.25%)</td><td>0.03 <b>(+107.68%)</b></td><td>183.40 (-13.25%)</td><td>150.66 (-11.00%)</td><td>168.20 (+8.38%)</td><td>113.50 <b>(-25.62%)</b></td><td>32.36 <b>(+30.40%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>169.28 (n/a)</td><td>155.20 (n/a)</td><td>152.60 (n/a)</td><td>24.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 <b>(+32.96%)</b></td><td>0.09 (+12.92%)</td><td>0.09 (+10.89%)</td><td>0.07 (-6.45%)</td><td>0.02 <b>(+172.14%)</b></td><td>244.70 (+6.90%)</td><td>183.58 (-8.06%)</td><td>176.60 (-9.81%)</td><td>132.20 <b>(-24.76%)</b></td><td>43.70 <b>(+118.51%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>228.90 (n/a)</td><td>199.68 (n/a)</td><td>195.80 (n/a)</td><td>175.70 (n/a)</td><td>20.00 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 <b>(-27.18%)</b></td><td>0.09 (-7.11%)</td><td>0.09 (+4.30%)</td><td>0.08 <b>(+29.59%)</b></td><td>0.01 <b>(-71.53%)</b></td><td>208.30 <b>(-22.85%)</b></td><td>187.70 (+0.04%)</td><td>190.80 (-4.12%)</td><td>160.00 <b>(+37.34%)</b></td><td>17.48 <b>(-69.92%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>270.00 (n/a)</td><td>187.62 (n/a)</td><td>199.00 (n/a)</td><td>116.50 (n/a)</td><td>58.10 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (-16.72%)</td><td>0.10 (+6.65%)</td><td>0.10 <b>(+35.58%)</b></td><td>0.08 (+9.46%)</td><td>0.01 <b>(-51.85%)</b></td><td>202.20 (-8.67%)</td><td>171.62 (-9.58%)</td><td>160.10 <b>(-26.26%)</b></td><td>154.20 <b>(+20.09%)</b></td><td>21.56 <b>(-49.53%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>221.40 (n/a)</td><td>189.80 (n/a)</td><td>217.10 (n/a)</td><td>128.40 (n/a)</td><td>42.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (-2.45%)</td><td>0.09 (-0.05%)</td><td>0.08 (-7.28%)</td><td>0.08 (+11.34%)</td><td>0.01 <b>(-27.78%)</b></td><td>217.70 (-10.19%)</td><td>188.42 (-1.61%)</td><td>193.00 (+7.82%)</td><td>155.40 (+2.51%)</td><td>25.65 <b>(-34.18%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>242.40 (n/a)</td><td>191.50 (n/a)</td><td>179.00 (n/a)</td><td>151.60 (n/a)</td><td>38.97 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.26 (-8.42%)</td><td>0.21 (+4.88%)</td><td>0.21 (+10.80%)</td><td>0.17 (+13.65%)</td><td>0.03 <b>(-35.70%)</b></td><td>191.50 (-11.99%)</td><td>159.88 (-7.10%)</td><td>154.50 (-9.75%)</td><td>127.10 (+9.19%)</td><td>23.92 <b>(-36.99%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>217.60 (n/a)</td><td>172.10 (n/a)</td><td>171.20 (n/a)</td><td>116.40 (n/a)</td><td>37.96 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.30 <b>(+20.02%)</b></td><td>0.24 (+13.99%)</td><td>0.23 (+9.17%)</td><td>0.19 (+10.26%)</td><td>0.05 <b>(+43.83%)</b></td><td>176.40 (-9.31%)</td><td>139.98 (-11.08%)</td><td>142.20 (-8.38%)</td><td>107.70 (-16.64%)</td><td>30.22 (+8.17%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>194.50 (n/a)</td><td>157.42 (n/a)</td><td>155.20 (n/a)</td><td>129.20 (n/a)</td><td>27.94 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (+1.01%)</td><td>0.16 (-8.69%)</td><td>0.16 (-11.32%)</td><td>0.14 (-0.71%)</td><td>0.03 (+4.48%)</td><td>231.30 (+0.70%)</td><td>207.02 (+9.67%)</td><td>211.00 (+12.77%)</td><td>156.70 (-1.01%)</td><td>30.03 (+3.44%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>229.70 (n/a)</td><td>188.76 (n/a)</td><td>187.10 (n/a)</td><td>158.30 (n/a)</td><td>29.03 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (-12.85%)</td><td>0.16 (-5.50%)</td><td>0.16 (-9.84%)</td><td>0.14 (+2.94%)</td><td>0.02 <b>(-35.63%)</b></td><td>238.00 (-2.82%)</td><td>201.46 (+4.29%)</td><td>204.70 (+10.89%)</td><td>168.80 (+14.75%)</td><td>25.66 <b>(-28.28%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>244.90 (n/a)</td><td>193.18 (n/a)</td><td>184.60 (n/a)</td><td>147.10 (n/a)</td><td>35.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.35 (+14.34%)</td><td>0.22 (-0.26%)</td><td>0.22 (+1.20%)</td><td>0.12 <b>(-23.67%)</b></td><td>0.08 <b>(+50.33%)</b></td><td>271.50 <b>(+31.03%)</b></td><td>165.28 (+7.13%)</td><td>149.40 (-1.19%)</td><td>94.90 (-12.53%)</td><td>64.87 <b>(+76.99%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>207.20 (n/a)</td><td>154.28 (n/a)</td><td>151.20 (n/a)</td><td>108.50 (n/a)</td><td>36.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.28 (+0.23%)</td><td>0.24 (+12.97%)</td><td>0.24 <b>(+26.50%)</b></td><td>0.20 (+5.18%)</td><td>0.04 (-12.85%)</td><td>163.90 (-4.93%)</td><td>140.40 (-12.01%)</td><td>134.60 <b>(-20.96%)</b></td><td>115.90 (-0.17%)</td><td>20.78 (-14.86%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>172.40 (n/a)</td><td>159.56 (n/a)</td><td>170.30 (n/a)</td><td>116.10 (n/a)</td><td>24.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.26 (+6.88%)</td><td>0.20 (+0.80%)</td><td>0.21 (+8.82%)</td><td>0.11 <b>(-34.41%)</b></td><td>0.07 <b>(+122.08%)</b></td><td>306.60 <b>(+52.46%)</b></td><td>182.86 (+9.26%)</td><td>154.80 (-8.08%)</td><td>124.20 (-6.48%)</td><td>76.13 <b>(+213.91%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>201.10 (n/a)</td><td>167.36 (n/a)</td><td>168.40 (n/a)</td><td>132.80 (n/a)</td><td>24.25 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.34 <b>(+35.64%)</b></td><td>0.24 (+17.47%)</td><td>0.23 (+17.27%)</td><td>0.15 (-14.95%)</td><td>0.09 <b>(+175.87%)</b></td><td>221.80 (+17.60%)</td><td>154.14 (-6.38%)</td><td>143.60 (-14.68%)</td><td>96.00 <b>(-26.27%)</b></td><td>57.10 <b>(+140.10%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>188.60 (n/a)</td><td>164.64 (n/a)</td><td>168.30 (n/a)</td><td>130.20 (n/a)</td><td>23.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 (-1.28%)</td><td>0.19 (-9.45%)</td><td>0.18 (-9.13%)</td><td>0.14 (+14.80%)</td><td>0.04 <b>(-24.08%)</b></td><td>237.00 (-12.90%)</td><td>182.66 (+6.42%)</td><td>179.90 (+10.03%)</td><td>129.60 (+1.25%)</td><td>38.67 <b>(-34.43%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>272.10 (n/a)</td><td>171.64 (n/a)</td><td>163.50 (n/a)</td><td>128.00 (n/a)</td><td>58.97 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (+11.57%)</td><td>0.21 (+11.48%)</td><td>0.21 (+5.49%)</td><td>0.18 (+11.70%)</td><td>0.02 (-9.89%)</td><td>183.60 (-10.48%)</td><td>157.04 (-10.73%)</td><td>153.90 (-5.18%)</td><td>137.20 (-10.39%)</td><td>17.11 <b>(-27.76%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>205.10 (n/a)</td><td>175.92 (n/a)</td><td>162.30 (n/a)</td><td>153.10 (n/a)</td><td>23.68 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 (+13.00%)</td><td>0.19 (+0.75%)</td><td>0.20 (+3.98%)</td><td>0.15 (-6.19%)</td><td>0.05 <b>(+92.99%)</b></td><td>224.20 (+6.61%)</td><td>176.96 (+2.72%)</td><td>161.20 (-3.82%)</td><td>130.30 (-11.48%)</td><td>43.44 <b>(+86.71%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>210.30 (n/a)</td><td>172.28 (n/a)</td><td>167.60 (n/a)</td><td>147.20 (n/a)</td><td>23.26 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 <b>(+23.94%)</b></td><td>0.21 (+14.28%)</td><td>0.21 (+12.37%)</td><td>0.16 (+0.69%)</td><td>0.04 <b>(+118.83%)</b></td><td>206.30 (-0.67%)</td><td>161.76 (-10.79%)</td><td>158.40 (-11.01%)</td><td>129.10 (-19.31%)</td><td>29.94 <b>(+74.67%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>207.70 (n/a)</td><td>181.32 (n/a)</td><td>178.00 (n/a)</td><td>160.00 (n/a)</td><td>17.14 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (+7.92%)</td><td>0.20 (+14.86%)</td><td>0.20 (+17.18%)</td><td>0.18 <b>(+28.07%)</b></td><td>0.01 <b>(-50.29%)</b></td><td>179.40 <b>(-21.90%)</b></td><td>165.56 (-13.85%)</td><td>165.60 (-14.68%)</td><td>157.10 (-7.37%)</td><td>9.07 <b>(-63.43%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>229.70 (n/a)</td><td>192.18 (n/a)</td><td>194.10 (n/a)</td><td>169.60 (n/a)</td><td>24.79 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.27 <b>(+33.06%)</b></td><td>0.20 (+12.79%)</td><td>0.19 (+3.01%)</td><td>0.15 (-0.20%)</td><td>0.05 <b>(+120.48%)</b></td><td>218.50 (+0.18%)</td><td>168.88 (-8.82%)</td><td>169.80 (-2.97%)</td><td>123.40 <b>(-24.85%)</b></td><td>36.85 <b>(+64.61%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>218.10 (n/a)</td><td>185.22 (n/a)</td><td>175.00 (n/a)</td><td>164.20 (n/a)</td><td>22.38 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.18 (-7.39%)</td><td>0.17 (-9.53%)</td><td>0.17 (-6.19%)</td><td>0.15 (-18.25%)</td><td>0.02 <b>(+93.02%)</b></td><td>222.10 <b>(+22.37%)</b></td><td>195.50 (+11.17%)</td><td>192.50 (+6.59%)</td><td>178.00 (+7.94%)</td><td>18.87 <b>(+151.35%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>181.50 (n/a)</td><td>175.86 (n/a)</td><td>180.60 (n/a)</td><td>164.90 (n/a)</td><td>7.51 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (-12.47%)</td><td>0.18 (+1.54%)</td><td>0.19 (+16.11%)</td><td>0.15 (+2.51%)</td><td>0.02 <b>(-38.77%)</b></td><td>216.30 (-2.44%)</td><td>183.12 (-3.40%)</td><td>171.40 (-13.87%)</td><td>155.80 (+14.22%)</td><td>24.71 <b>(-31.85%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>221.70 (n/a)</td><td>189.56 (n/a)</td><td>199.00 (n/a)</td><td>136.40 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (-0.66%)</td><td>0.16 (-0.20%)</td><td>0.16 (-0.06%)</td><td>0.16 (-0.25%)</td><td>0.00 <b>(-38.52%)</b></td><td>52551.10 (+0.25%)</td><td>52335.40 (+0.19%)</td><td>52299.50 (+0.06%)</td><td>52241.90 (+0.66%)</td><td>123.25 <b>(-37.86%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52419.70 (n/a)</td><td>52233.62 (n/a)</td><td>52268.80 (n/a)</td><td>51896.90 (n/a)</td><td>198.36 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52308.80 (n/a)</td><td>52262.94 (n/a)</td><td>52260.60 (n/a)</td><td>52190.90 (n/a)</td><td>48.00 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>413261.00 (n/a)</td><td>413130.76 (n/a)</td><td>413072.10 (n/a)</td><td>413019.70 (n/a)</td><td>109.43 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.18 (-19.39%)</td><td>0.15 (-1.53%)</td><td>0.15 (+8.37%)</td><td>0.13 (+2.37%)</td><td>0.02 <b>(-54.43%)</b></td><td>192.40 (-2.29%)</td><td>164.70 (-1.27%)</td><td>162.20 (-7.74%)</td><td>140.40 <b>(+24.14%)</b></td><td>18.68 <b>(-42.82%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>196.90 (n/a)</td><td>166.82 (n/a)</td><td>175.80 (n/a)</td><td>113.10 (n/a)</td><td>32.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.36 (-9.06%)</td><td>0.30 (-4.46%)</td><td>0.29 (+1.00%)</td><td>0.25 (-0.27%)</td><td>0.05 <b>(-26.94%)</b></td><td>199.80 (+0.25%)</td><td>165.46 (+3.14%)</td><td>167.80 (-1.00%)</td><td>134.80 (+9.95%)</td><td>27.14 (-18.47%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.40 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.07 (n/a)</td><td>199.30 (n/a)</td><td>160.42 (n/a)</td><td>169.50 (n/a)</td><td>122.60 (n/a)</td><td>33.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>12.81 (-4.47%)</td><td>12.42 (-0.31%)</td><td>12.45 (+0.39%)</td><td>12.02 (+11.27%)</td><td>0.33 <b>(-68.51%)</b></td><td>872.20 (-10.13%)</td><td>844.66 (-0.24%)</td><td>842.50 (-0.39%)</td><td>818.50 (+4.68%)</td><td>22.41 <b>(-70.42%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>13.41 (n/a)</td><td>12.46 (n/a)</td><td>12.40 (n/a)</td><td>10.80 (n/a)</td><td>1.04 (n/a)</td><td>970.50 (n/a)</td><td>846.66 (n/a)</td><td>845.80 (n/a)</td><td>781.90 (n/a)</td><td>75.76 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.29 (-16.67%)</td><td>0.22 (-9.33%)</td><td>0.20 (-16.68%)</td><td>0.17 (-10.92%)</td><td>0.05 (-14.95%)</td><td>243.60 (+12.26%)</td><td>191.02 (+9.82%)</td><td>204.60 <b>(+20.07%)</b></td><td>142.70 <b>(+20.02%)</b></td><td>44.74 (+6.46%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>217.00 (n/a)</td><td>173.94 (n/a)</td><td>170.40 (n/a)</td><td>118.90 (n/a)</td><td>42.03 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (+10.73%)</td><td>0.03 (-10.52%)</td><td>0.02 <b>(-22.51%)</b></td><td>0.02 <b>(-21.93%)</b></td><td>0.01 <b>(+90.79%)</b></td><td>250.80 <b>(+28.09%)</b></td><td>198.68 (+17.58%)</td><td>215.60 <b>(+29.02%)</b></td><td>120.70 (-9.72%)</td><td>51.34 <b>(+118.37%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>195.80 (n/a)</td><td>168.98 (n/a)</td><td>167.10 (n/a)</td><td>133.70 (n/a)</td><td>23.51 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-1.20%)</td><td>0.03 (+7.37%)</td><td>0.03 (+19.25%)</td><td>0.02 (-3.65%)</td><td>0.00 (+13.28%)</td><td>173.60 (+3.77%)</td><td>143.22 (-6.47%)</td><td>132.00 (-16.14%)</td><td>125.10 (+1.21%)</td><td>20.90 <b>(+20.73%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>167.30 (n/a)</td><td>153.12 (n/a)</td><td>157.40 (n/a)</td><td>123.60 (n/a)</td><td>17.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (+5.29%)</td><td>0.04 (-1.54%)</td><td>0.04 (-10.18%)</td><td>0.03 (+2.17%)</td><td>0.01 (+8.68%)</td><td>184.00 (-2.13%)</td><td>159.18 (+1.83%)</td><td>174.20 (+11.31%)</td><td>113.30 (-5.03%)</td><td>30.24 (-0.01%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>188.00 (n/a)</td><td>156.32 (n/a)</td><td>156.50 (n/a)</td><td>119.30 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (+0.14%)</td><td>0.03 (+7.24%)</td><td>0.02 (+8.81%)</td><td>0.02 (+13.02%)</td><td>0.00 (-16.36%)</td><td>173.10 (-11.50%)</td><td>155.56 (-7.96%)</td><td>167.40 (-8.12%)</td><td>115.00 (-0.17%)</td><td>23.82 <b>(-24.47%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>195.60 (n/a)</td><td>169.02 (n/a)</td><td>182.20 (n/a)</td><td>115.20 (n/a)</td><td>31.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 <b>(-21.98%)</b></td><td>0.03 (-13.12%)</td><td>0.03 (-18.53%)</td><td>0.02 (+7.83%)</td><td>0.00 <b>(-48.95%)</b></td><td>221.20 (-7.25%)</td><td>192.54 (+11.44%)</td><td>192.60 <b>(+22.75%)</b></td><td>165.80 <b>(+28.13%)</b></td><td>25.96 <b>(-40.53%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.50 (n/a)</td><td>172.78 (n/a)</td><td>156.90 (n/a)</td><td>129.40 (n/a)</td><td>43.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (+10.04%)</td><td>0.03 (+1.07%)</td><td>0.03 (+8.27%)</td><td>0.01 <b>(-27.31%)</b></td><td>0.01 <b>(+66.21%)</b></td><td>279.90 <b>(+37.54%)</b></td><td>175.38 (+7.46%)</td><td>157.20 (-7.64%)</td><td>105.30 (-9.15%)</td><td>69.55 <b>(+114.80%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>203.50 (n/a)</td><td>163.20 (n/a)</td><td>170.20 (n/a)</td><td>115.90 (n/a)</td><td>32.38 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (+15.48%)</td><td>0.03 (-2.77%)</td><td>0.03 (-10.39%)</td><td>0.03 (-6.57%)</td><td>0.01 <b>(+138.12%)</b></td><td>193.00 (+7.04%)</td><td>170.98 (+4.46%)</td><td>176.70 (+11.55%)</td><td>131.30 (-13.39%)</td><td>24.79 <b>(+117.70%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>180.30 (n/a)</td><td>163.68 (n/a)</td><td>158.40 (n/a)</td><td>151.60 (n/a)</td><td>11.39 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 <b>(-21.34%)</b></td><td>0.02 (-9.87%)</td><td>0.02 (-6.10%)</td><td>0.02 (-3.39%)</td><td>0.00 <b>(-40.27%)</b></td><td>201.50 (+3.55%)</td><td>175.54 (+9.23%)</td><td>166.90 (+6.51%)</td><td>149.40 <b>(+27.15%)</b></td><td>24.45 (-18.90%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>194.60 (n/a)</td><td>160.70 (n/a)</td><td>156.70 (n/a)</td><td>117.50 (n/a)</td><td>30.15 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-7.39%)</td><td>0.02 (-15.94%)</td><td>0.02 <b>(-24.44%)</b></td><td>0.02 (-5.84%)</td><td>0.01 <b>(-23.57%)</b></td><td>279.90 (+6.18%)</td><td>201.36 (+16.04%)</td><td>185.30 <b>(+32.36%)</b></td><td>138.60 (+7.94%)</td><td>52.81 (-9.87%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>263.60 (n/a)</td><td>173.52 (n/a)</td><td>140.00 (n/a)</td><td>128.40 (n/a)</td><td>58.60 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-8.19%)</td><td>0.03 (-4.75%)</td><td>0.02 (-1.01%)</td><td>0.02 (-11.77%)</td><td>0.00 (-8.19%)</td><td>202.50 (+13.32%)</td><td>165.24 (+5.11%)</td><td>166.40 (+1.03%)</td><td>128.50 (+8.90%)</td><td>27.01 (+15.96%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.70 (n/a)</td><td>157.20 (n/a)</td><td>164.70 (n/a)</td><td>118.00 (n/a)</td><td>23.29 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 <b>(-21.72%)</b></td><td>0.02 (-13.39%)</td><td>0.02 (-9.49%)</td><td>0.02 (-6.89%)</td><td>0.00 <b>(-42.20%)</b></td><td>235.40 (+7.39%)</td><td>209.24 (+12.74%)</td><td>218.90 (+10.50%)</td><td>157.00 <b>(+27.75%)</b></td><td>30.21 <b>(-22.19%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>219.20 (n/a)</td><td>185.60 (n/a)</td><td>198.10 (n/a)</td><td>122.90 (n/a)</td><td>38.83 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 <b>(-23.51%)</b></td><td>0.02 (-6.08%)</td><td>0.02 (+1.42%)</td><td>0.02 (-0.14%)</td><td>0.00 <b>(-57.57%)</b></td><td>214.20 (+0.14%)</td><td>185.86 (+2.62%)</td><td>188.20 (-1.41%)</td><td>152.90 <b>(+30.68%)</b></td><td>21.82 <b>(-44.48%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>213.90 (n/a)</td><td>181.12 (n/a)</td><td>190.90 (n/a)</td><td>117.00 (n/a)</td><td>39.30 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 <b>(+22.43%)</b></td><td>0.02 (+4.26%)</td><td>0.02 (+5.66%)</td><td>0.02 (-6.19%)</td><td>0.01 <b>(+76.50%)</b></td><td>242.30 (+6.60%)</td><td>194.82 (-1.02%)</td><td>194.30 (-5.36%)</td><td>130.90 (-18.29%)</td><td>45.88 <b>(+55.91%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.30 (n/a)</td><td>196.82 (n/a)</td><td>205.30 (n/a)</td><td>160.20 (n/a)</td><td>29.43 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (+0.04%)</td><td>0.02 (+2.37%)</td><td>0.02 (+6.53%)</td><td>0.02 (+10.15%)</td><td>0.00 <b>(-33.46%)</b></td><td>192.10 (-9.22%)</td><td>172.98 (-4.07%)</td><td>180.40 (-6.14%)</td><td>142.50 (-0.07%)</td><td>21.00 <b>(-38.72%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.60 (n/a)</td><td>180.32 (n/a)</td><td>192.20 (n/a)</td><td>142.60 (n/a)</td><td>34.26 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 <b>(+29.79%)</b></td><td>0.02 (+12.45%)</td><td>0.02 (+3.29%)</td><td>0.02 <b>(+41.84%)</b></td><td>0.00 (+3.70%)</td><td>234.50 <b>(-29.49%)</b></td><td>200.08 (-12.61%)</td><td>198.60 (-3.17%)</td><td>151.50 <b>(-22.94%)</b></td><td>31.07 <b>(-46.50%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>332.60 (n/a)</td><td>228.96 (n/a)</td><td>205.10 (n/a)</td><td>196.60 (n/a)</td><td>58.07 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (+14.60%)</td><td>0.02 (+15.86%)</td><td>0.02 (+19.35%)</td><td>0.02 (+13.84%)</td><td>0.00 (+7.39%)</td><td>205.30 (-12.15%)</td><td>189.70 (-13.73%)</td><td>189.80 (-16.20%)</td><td>174.30 (-12.76%)</td><td>11.29 (-17.39%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>233.70 (n/a)</td><td>219.88 (n/a)</td><td>226.50 (n/a)</td><td>199.80 (n/a)</td><td>13.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (-0.54%)</td><td>0.05 (+10.92%)</td><td>0.05 (+16.78%)</td><td>0.04 <b>(+23.81%)</b></td><td>0.01 <b>(-28.97%)</b></td><td>187.30 (-19.23%)</td><td>162.16 (-11.83%)</td><td>164.70 (-14.35%)</td><td>128.30 (+0.55%)</td><td>22.31 <b>(-41.35%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.90 (n/a)</td><td>183.92 (n/a)</td><td>192.30 (n/a)</td><td>127.60 (n/a)</td><td>38.03 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (-10.78%)</td><td>0.07 (-6.49%)</td><td>0.07 (+2.76%)</td><td>0.06 (-4.21%)</td><td>0.01 <b>(-35.58%)</b></td><td>205.50 (+4.37%)</td><td>189.52 (+6.41%)</td><td>184.00 (-2.70%)</td><td>172.40 (+12.09%)</td><td>14.73 <b>(-23.29%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.90 (n/a)</td><td>178.10 (n/a)</td><td>189.10 (n/a)</td><td>153.80 (n/a)</td><td>19.20 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (-6.28%)</td><td>0.05 (+5.02%)</td><td>0.05 (+6.67%)</td><td>0.04 (+10.07%)</td><td>0.01 <b>(-26.86%)</b></td><td>202.10 (-9.13%)</td><td>174.34 (-5.86%)</td><td>170.40 (-6.27%)</td><td>150.40 (+6.74%)</td><td>22.32 <b>(-28.54%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.40 (n/a)</td><td>185.20 (n/a)</td><td>181.80 (n/a)</td><td>140.90 (n/a)</td><td>31.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (+2.55%)</td><td>0.06 (-0.78%)</td><td>0.06 (+5.42%)</td><td>0.05 (-9.83%)</td><td>0.02 <b>(+27.24%)</b></td><td>216.00 (+10.88%)</td><td>173.62 (+3.17%)</td><td>162.80 (-5.13%)</td><td>118.00 (-2.48%)</td><td>42.03 <b>(+48.27%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>168.28 (n/a)</td><td>171.60 (n/a)</td><td>121.00 (n/a)</td><td>28.35 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (-0.97%)</td><td>0.06 (+15.18%)</td><td>0.06 (-1.18%)</td><td>0.05 <b>(+69.48%)</b></td><td>0.01 <b>(-56.82%)</b></td><td>165.20 <b>(-41.00%)</b></td><td>144.98 (-18.89%)</td><td>148.90 (+1.22%)</td><td>129.80 (+0.93%)</td><td>15.02 <b>(-75.47%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>280.00 (n/a)</td><td>178.74 (n/a)</td><td>147.10 (n/a)</td><td>128.60 (n/a)</td><td>61.25 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (+15.22%)</td><td>0.07 (+14.08%)</td><td>0.07 <b>(+21.87%)</b></td><td>0.05 (+0.07%)</td><td>0.02 <b>(+44.37%)</b></td><td>204.60 (-0.10%)</td><td>154.04 (-10.75%)</td><td>144.50 (-17.94%)</td><td>120.40 (-13.26%)</td><td>36.11 <b>(+23.52%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>204.80 (n/a)</td><td>172.60 (n/a)</td><td>176.10 (n/a)</td><td>138.80 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (+6.33%)</td><td>0.05 (+4.20%)</td><td>0.05 (-14.78%)</td><td>0.04 (+6.67%)</td><td>0.01 <b>(+50.55%)</b></td><td>186.40 (-6.28%)</td><td>157.50 (-1.77%)</td><td>181.20 (+17.36%)</td><td>117.70 (-5.92%)</td><td>36.20 <b>(+30.92%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>198.90 (n/a)</td><td>160.34 (n/a)</td><td>154.40 (n/a)</td><td>125.10 (n/a)</td><td>27.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (+3.52%)</td><td>0.05 (+2.91%)</td><td>0.05 (+4.13%)</td><td>0.04 (-17.06%)</td><td>0.01 <b>(+45.44%)</b></td><td>250.00 <b>(+20.60%)</b></td><td>180.54 (+0.22%)</td><td>174.20 (-3.97%)</td><td>131.80 (-3.37%)</td><td>47.37 <b>(+70.77%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.30 (n/a)</td><td>180.14 (n/a)</td><td>181.40 (n/a)</td><td>136.40 (n/a)</td><td>27.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 <b>(+29.35%)</b></td><td>0.05 (+5.34%)</td><td>0.05 (-4.90%)</td><td>0.04 (-14.63%)</td><td>0.01 <b>(+357.91%)</b></td><td>212.40 (+17.09%)</td><td>166.02 (-0.23%)</td><td>174.50 (+5.12%)</td><td>118.30 <b>(-22.68%)</b></td><td>41.12 <b>(+306.74%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>181.40 (n/a)</td><td>166.40 (n/a)</td><td>166.00 (n/a)</td><td>153.00 (n/a)</td><td>10.11 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 <b>(-23.46%)</b></td><td>0.05 (+0.80%)</td><td>0.06 (+9.52%)</td><td>0.05 <b>(+38.79%)</b></td><td>0.01 <b>(-64.40%)</b></td><td>202.10 <b>(-27.95%)</b></td><td>176.00 (-7.38%)</td><td>165.60 (-8.71%)</td><td>155.90 <b>(+30.68%)</b></td><td>20.22 <b>(-66.29%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>280.50 (n/a)</td><td>190.02 (n/a)</td><td>181.40 (n/a)</td><td>119.30 (n/a)</td><td>59.97 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (+0.48%)</td><td>0.04 (-13.32%)</td><td>0.04 (-17.77%)</td><td>0.03 (-5.69%)</td><td>0.01 (+13.53%)</td><td>237.20 (+6.03%)</td><td>203.36 (+15.95%)</td><td>206.60 <b>(+21.60%)</b></td><td>152.90 (-0.52%)</td><td>31.83 (+13.92%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>175.38 (n/a)</td><td>169.90 (n/a)</td><td>153.70 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (-7.46%)</td><td>0.04 (-9.38%)</td><td>0.04 (-1.21%)</td><td>0.03 (-14.23%)</td><td>0.01 (+5.90%)</td><td>271.50 (+16.57%)</td><td>219.62 (+11.13%)</td><td>205.80 (+1.23%)</td><td>176.70 (+8.01%)</td><td>38.26 <b>(+36.41%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.90 (n/a)</td><td>197.62 (n/a)</td><td>203.30 (n/a)</td><td>163.60 (n/a)</td><td>28.05 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (+8.58%)</td><td>0.05 (-17.13%)</td><td>0.04 <b>(-24.52%)</b></td><td>0.03 <b>(-32.09%)</b></td><td>0.02 <b>(+92.22%)</b></td><td>289.20 <b>(+47.25%)</b></td><td>196.72 <b>(+32.03%)</b></td><td>191.50 <b>(+32.43%)</b></td><td>116.50 (-7.91%)</td><td>72.35 <b>(+156.89%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.40 (n/a)</td><td>149.00 (n/a)</td><td>144.60 (n/a)</td><td>126.50 (n/a)</td><td>28.16 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 <b>(-24.31%)</b></td><td>0.05 (+3.69%)</td><td>0.05 (+8.42%)</td><td>0.04 <b>(+53.15%)</b></td><td>0.00 <b>(-69.43%)</b></td><td>223.10 <b>(-34.71%)</b></td><td>193.24 (-11.61%)</td><td>186.60 (-7.76%)</td><td>171.60 <b>(+32.10%)</b></td><td>20.33 <b>(-73.73%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>341.70 (n/a)</td><td>218.62 (n/a)</td><td>202.30 (n/a)</td><td>129.90 (n/a)</td><td>77.40 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (-2.97%)</td><td>0.04 (-10.59%)</td><td>0.04 (-13.24%)</td><td>0.03 (-10.37%)</td><td>0.01 (+8.86%)</td><td>270.80 (+11.58%)</td><td>216.26 (+12.76%)</td><td>217.80 (+15.24%)</td><td>155.60 (+3.05%)</td><td>42.71 <b>(+22.51%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>242.70 (n/a)</td><td>191.78 (n/a)</td><td>189.00 (n/a)</td><td>151.00 (n/a)</td><td>34.86 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (-4.94%)</td><td>0.10 (-3.56%)</td><td>0.10 (+0.11%)</td><td>0.08 (-12.96%)</td><td>0.01 (+7.33%)</td><td>201.50 (+14.88%)</td><td>169.80 (+4.06%)</td><td>172.00 (-0.12%)</td><td>144.60 (+5.24%)</td><td>21.27 <b>(+28.95%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>175.40 (n/a)</td><td>163.18 (n/a)</td><td>172.20 (n/a)</td><td>137.40 (n/a)</td><td>16.49 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (+1.07%)</td><td>0.13 (-5.52%)</td><td>0.12 (-4.65%)</td><td>0.10 (-2.88%)</td><td>0.03 (-12.26%)</td><td>252.20 (+2.98%)</td><td>191.22 (+4.69%)</td><td>197.70 (+4.88%)</td><td>132.60 (-1.04%)</td><td>43.75 (-7.94%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>244.90 (n/a)</td><td>182.66 (n/a)</td><td>188.50 (n/a)</td><td>134.00 (n/a)</td><td>47.53 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (+16.63%)</td><td>0.11 (+8.99%)</td><td>0.10 (-3.24%)</td><td>0.09 (+15.18%)</td><td>0.02 <b>(+20.82%)</b></td><td>177.20 (-13.18%)</td><td>153.46 (-8.10%)</td><td>158.50 (+3.32%)</td><td>111.50 (-14.30%)</td><td>27.44 (-11.54%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.10 (n/a)</td><td>166.98 (n/a)</td><td>153.40 (n/a)</td><td>130.10 (n/a)</td><td>31.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (+19.30%)</td><td>0.13 (+12.39%)</td><td>0.13 (-0.96%)</td><td>0.09 (+12.97%)</td><td>0.04 <b>(+22.05%)</b></td><td>222.40 (-11.46%)</td><td>161.46 (-10.65%)</td><td>157.00 (+0.96%)</td><td>110.40 (-16.17%)</td><td>44.12 (-10.95%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>251.20 (n/a)</td><td>180.70 (n/a)</td><td>155.50 (n/a)</td><td>131.70 (n/a)</td><td>49.55 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 <b>(-26.93%)</b></td><td>0.07 <b>(-25.35%)</b></td><td>0.06 <b>(-39.64%)</b></td><td>0.05 (-10.99%)</td><td>0.02 <b>(-42.13%)</b></td><td>333.80 (+12.35%)</td><td>250.30 <b>(+28.25%)</b></td><td>256.30 <b>(+65.68%)</b></td><td>183.20 <b>(+36.82%)</b></td><td>59.90 (-13.21%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>297.10 (n/a)</td><td>195.16 (n/a)</td><td>154.70 (n/a)</td><td>133.90 (n/a)</td><td>69.02 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (+2.49%)</td><td>0.13 (+7.77%)</td><td>0.13 (+7.62%)</td><td>0.11 (+10.20%)</td><td>0.02 (-4.93%)</td><td>194.40 (-9.24%)</td><td>162.68 (-7.70%)</td><td>157.80 (-7.07%)</td><td>138.20 (-2.47%)</td><td>25.50 (-17.63%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>214.20 (n/a)</td><td>176.26 (n/a)</td><td>169.80 (n/a)</td><td>141.70 (n/a)</td><td>30.95 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 <b>(-37.12%)</b></td><td>0.09 <b>(-28.16%)</b></td><td>0.08 <b>(-28.59%)</b></td><td>0.07 <b>(-20.45%)</b></td><td>0.01 <b>(-55.14%)</b></td><td>242.90 <b>(+25.72%)</b></td><td>194.66 <b>(+35.92%)</b></td><td>193.90 <b>(+40.00%)</b></td><td>169.70 <b>(+59.04%)</b></td><td>29.43 (-10.84%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>193.20 (n/a)</td><td>143.22 (n/a)</td><td>138.50 (n/a)</td><td>106.70 (n/a)</td><td>33.00 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (-12.83%)</td><td>0.11 (+0.02%)</td><td>0.11 (+4.09%)</td><td>0.08 (+8.65%)</td><td>0.02 <b>(-32.63%)</b></td><td>241.50 (-7.96%)</td><td>174.96 (-2.97%)</td><td>162.10 (-3.91%)</td><td>146.60 (+14.71%)</td><td>38.12 <b>(-27.17%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>262.40 (n/a)</td><td>180.32 (n/a)</td><td>168.70 (n/a)</td><td>127.80 (n/a)</td><td>52.34 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 <b>(-26.81%)</b></td><td>0.08 <b>(-27.56%)</b></td><td>0.09 <b>(-22.34%)</b></td><td>0.06 <b>(-33.64%)</b></td><td>0.02 (-13.37%)</td><td>296.20 <b>(+50.66%)</b></td><td>211.20 <b>(+40.00%)</b></td><td>191.00 <b>(+28.79%)</b></td><td>167.00 <b>(+36.66%)</b></td><td>50.85 <b>(+80.14%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.60 (n/a)</td><td>150.86 (n/a)</td><td>148.30 (n/a)</td><td>122.20 (n/a)</td><td>28.23 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 <b>(-37.63%)</b></td><td>0.11 <b>(-21.06%)</b></td><td>0.11 (-3.50%)</td><td>0.10 (-13.53%)</td><td>0.01 <b>(-71.23%)</b></td><td>193.50 (+15.66%)</td><td>174.64 <b>(+21.40%)</b></td><td>171.30 (+3.63%)</td><td>152.30 <b>(+60.32%)</b></td><td>17.10 <b>(-47.63%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>167.30 (n/a)</td><td>143.86 (n/a)</td><td>165.30 (n/a)</td><td>95.00 (n/a)</td><td>32.66 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (+0.20%)</td><td>0.08 (-15.37%)</td><td>0.08 <b>(-25.46%)</b></td><td>0.06 <b>(-34.65%)</b></td><td>0.02 <b>(+133.39%)</b></td><td>292.80 <b>(+52.98%)</b></td><td>209.08 <b>(+24.35%)</b></td><td>217.50 <b>(+34.18%)</b></td><td>150.00 (-0.20%)</td><td>57.27 <b>(+244.41%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>191.40 (n/a)</td><td>168.14 (n/a)</td><td>162.10 (n/a)</td><td>150.30 (n/a)</td><td>16.63 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (+0.55%)</td><td>0.10 (+8.40%)</td><td>0.10 (+4.98%)</td><td>0.09 <b>(+27.39%)</b></td><td>0.01 <b>(-48.32%)</b></td><td>197.70 <b>(-21.52%)</b></td><td>175.80 (-10.24%)</td><td>176.60 (-4.75%)</td><td>151.40 (-0.53%)</td><td>16.42 <b>(-60.34%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>251.90 (n/a)</td><td>195.86 (n/a)</td><td>185.40 (n/a)</td><td>152.20 (n/a)</td><td>41.39 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (-18.84%)</td><td>0.08 <b>(-22.19%)</b></td><td>0.08 <b>(-25.94%)</b></td><td>0.06 (-18.52%)</td><td>0.02 (-16.56%)</td><td>267.10 <b>(+22.75%)</b></td><td>208.14 <b>(+28.69%)</b></td><td>211.10 <b>(+35.06%)</b></td><td>134.60 <b>(+23.15%)</b></td><td>47.86 <b>(+22.14%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>217.60 (n/a)</td><td>161.74 (n/a)</td><td>156.30 (n/a)</td><td>109.30 (n/a)</td><td>39.18 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 <b>(-29.53%)</b></td><td>0.10 (-8.41%)</td><td>0.10 (+2.93%)</td><td>0.08 (+6.77%)</td><td>0.02 <b>(-57.27%)</b></td><td>211.60 (-6.37%)</td><td>176.12 (+3.44%)</td><td>167.70 (-2.84%)</td><td>142.80 <b>(+41.81%)</b></td><td>27.92 <b>(-39.72%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>226.00 (n/a)</td><td>170.26 (n/a)</td><td>172.60 (n/a)</td><td>100.70 (n/a)</td><td>46.32 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.08 (-16.81%)</td><td>0.07 (-18.69%)</td><td>0.07 (-17.90%)</td><td>0.05 <b>(-28.60%)</b></td><td>0.01 (+2.64%)</td><td>326.10 <b>(+40.08%)</b></td><td>248.80 <b>(+24.38%)</b></td><td>223.80 <b>(+21.83%)</b></td><td>212.30 <b>(+20.22%)</b></td><td>48.24 <b>(+70.83%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>232.80 (n/a)</td><td>200.04 (n/a)</td><td>183.70 (n/a)</td><td>176.60 (n/a)</td><td>28.24 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.20 <b>(-29.92%)</b></td><td>0.18 (-16.34%)</td><td>0.19 (-0.98%)</td><td>0.14 (-17.81%)</td><td>0.03 <b>(-52.93%)</b></td><td>240.70 <b>(+21.69%)</b></td><td>184.14 (+16.18%)</td><td>172.00 (+1.00%)</td><td>164.90 <b>(+42.65%)</b></td><td>31.79 (-14.79%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>197.80 (n/a)</td><td>158.50 (n/a)</td><td>170.30 (n/a)</td><td>115.60 (n/a)</td><td>37.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (+3.95%)</td><td>0.18 (+8.41%)</td><td>0.17 (+4.48%)</td><td>0.13 <b>(+23.90%)</b></td><td>0.04 (-4.79%)</td><td>250.10 (-19.27%)</td><td>190.08 (-9.44%)</td><td>195.50 (-4.26%)</td><td>139.30 (-3.80%)</td><td>43.45 <b>(-29.06%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>309.80 (n/a)</td><td>209.90 (n/a)</td><td>204.20 (n/a)</td><td>144.80 (n/a)</td><td>61.26 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.29 <b>(-24.04%)</b></td><td>0.24 (-17.46%)</td><td>0.23 <b>(-23.62%)</b></td><td>0.21 (+8.40%)</td><td>0.04 <b>(-51.18%)</b></td><td>197.00 (-7.77%)</td><td>171.94 (+16.44%)</td><td>174.90 <b>(+30.91%)</b></td><td>141.10 <b>(+31.62%)</b></td><td>24.35 <b>(-41.40%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.31 (n/a)</td><td>0.19 (n/a)</td><td>0.07 (n/a)</td><td>213.60 (n/a)</td><td>147.66 (n/a)</td><td>133.60 (n/a)</td><td>107.20 (n/a)</td><td>41.55 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.20 (-13.29%)</td><td>0.17 (-18.61%)</td><td>0.18 (-13.62%)</td><td>0.12 <b>(-35.10%)</b></td><td>0.03 <b>(+64.78%)</b></td><td>279.80 <b>(+54.07%)</b></td><td>199.70 <b>(+26.44%)</b></td><td>183.80 (+15.74%)</td><td>162.00 (+15.38%)</td><td>46.61 <b>(+202.13%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>181.60 (n/a)</td><td>157.94 (n/a)</td><td>158.80 (n/a)</td><td>140.40 (n/a)</td><td>15.43 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.32 (-1.89%)</td><td>0.25 (-1.64%)</td><td>0.26 (+6.18%)</td><td>0.19 (+7.81%)</td><td>0.06 (-7.25%)</td><td>216.60 (-7.24%)</td><td>169.40 (+0.92%)</td><td>154.90 (-5.84%)</td><td>126.60 (+1.93%)</td><td>38.03 (-10.39%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.33 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.06 (n/a)</td><td>233.50 (n/a)</td><td>167.86 (n/a)</td><td>164.50 (n/a)</td><td>124.20 (n/a)</td><td>42.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.20 <b>(-29.66%)</b></td><td>0.16 <b>(-33.90%)</b></td><td>0.15 <b>(-28.78%)</b></td><td>0.13 <b>(-37.10%)</b></td><td>0.03 <b>(-22.53%)</b></td><td>255.00 <b>(+58.98%)</b></td><td>214.84 <b>(+52.17%)</b></td><td>213.90 <b>(+40.45%)</b></td><td>163.90 <b>(+42.15%)</b></td><td>35.04 <b>(+73.80%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>160.40 (n/a)</td><td>141.18 (n/a)</td><td>152.30 (n/a)</td><td>115.30 (n/a)</td><td>20.16 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (-14.89%)</td><td>0.22 (+1.58%)</td><td>0.22 (+0.44%)</td><td>0.19 <b>(+27.67%)</b></td><td>0.02 <b>(-65.70%)</b></td><td>191.10 <b>(-21.65%)</b></td><td>171.02 (-5.28%)</td><td>167.30 (-0.42%)</td><td>154.30 (+17.52%)</td><td>13.50 <b>(-68.58%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>243.90 (n/a)</td><td>180.56 (n/a)</td><td>168.00 (n/a)</td><td>131.30 (n/a)</td><td>42.96 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 (-1.38%)</td><td>0.19 (-10.20%)</td><td>0.18 (-16.34%)</td><td>0.16 (+1.27%)</td><td>0.04 (-1.42%)</td><td>210.10 (-1.27%)</td><td>176.96 (+11.09%)</td><td>181.90 (+19.51%)</td><td>130.30 (+1.40%)</td><td>29.44 (-7.87%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>212.80 (n/a)</td><td>159.30 (n/a)</td><td>152.20 (n/a)</td><td>128.50 (n/a)</td><td>31.95 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.28 (-10.25%)</td><td>0.23 (-16.15%)</td><td>0.21 <b>(-26.18%)</b></td><td>0.19 (-8.79%)</td><td>0.04 (-11.14%)</td><td>193.50 (+9.63%)</td><td>164.56 (+19.09%)</td><td>173.50 <b>(+35.44%)</b></td><td>130.60 (+11.43%)</td><td>24.18 (+4.70%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>176.50 (n/a)</td><td>138.18 (n/a)</td><td>128.10 (n/a)</td><td>117.20 (n/a)</td><td>23.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (+8.69%)</td><td>0.16 (-15.46%)</td><td>0.15 <b>(-22.91%)</b></td><td>0.11 <b>(-35.38%)</b></td><td>0.04 <b>(+206.96%)</b></td><td>303.00 <b>(+54.75%)</b></td><td>218.56 <b>(+24.32%)</b></td><td>221.90 <b>(+29.69%)</b></td><td>148.50 (-7.99%)</td><td>56.75 <b>(+331.66%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>195.80 (n/a)</td><td>175.80 (n/a)</td><td>171.10 (n/a)</td><td>161.40 (n/a)</td><td>13.15 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (-2.00%)</td><td>0.17 (-10.72%)</td><td>0.18 (-9.03%)</td><td>0.11 <b>(-25.60%)</b></td><td>0.04 <b>(+33.19%)</b></td><td>302.80 <b>(+34.40%)</b></td><td>211.16 (+14.96%)</td><td>190.00 (+9.95%)</td><td>163.20 (+2.00%)</td><td>53.93 <b>(+92.95%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>225.30 (n/a)</td><td>183.68 (n/a)</td><td>172.80 (n/a)</td><td>160.00 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.27 <b>(+25.78%)</b></td><td>0.18 (-3.36%)</td><td>0.17 (-18.50%)</td><td>0.11 <b>(-30.04%)</b></td><td>0.06 <b>(+108.44%)</b></td><td>309.00 <b>(+42.92%)</b></td><td>198.90 (+11.60%)</td><td>196.90 <b>(+22.68%)</b></td><td>119.80 <b>(-20.50%)</b></td><td>70.80 <b>(+135.62%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>216.20 (n/a)</td><td>178.22 (n/a)</td><td>160.50 (n/a)</td><td>150.70 (n/a)</td><td>30.05 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (+0.54%)</td><td>0.19 (-6.64%)</td><td>0.18 (-9.07%)</td><td>0.16 (-7.14%)</td><td>0.02 <b>(+50.93%)</b></td><td>212.10 (+7.72%)</td><td>188.22 (+7.85%)</td><td>189.80 (+9.97%)</td><td>161.10 (-0.49%)</td><td>22.27 <b>(+61.58%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>196.90 (n/a)</td><td>174.52 (n/a)</td><td>172.60 (n/a)</td><td>161.90 (n/a)</td><td>13.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (+6.02%)</td><td>0.15 (-8.58%)</td><td>0.14 (-11.23%)</td><td>0.10 <b>(-29.58%)</b></td><td>0.04 <b>(+119.35%)</b></td><td>331.70 <b>(+41.99%)</b></td><td>235.16 (+14.09%)</td><td>227.00 (+12.66%)</td><td>168.30 (-5.71%)</td><td>61.25 <b>(+198.97%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>233.60 (n/a)</td><td>206.12 (n/a)</td><td>201.50 (n/a)</td><td>178.50 (n/a)</td><td>20.49 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (-2.65%)</td><td>0.14 (+2.75%)</td><td>0.14 (-0.73%)</td><td>0.12 (+15.22%)</td><td>0.02 <b>(-29.70%)</b></td><td>172.30 (-13.24%)</td><td>149.28 (-4.89%)</td><td>149.50 (+0.74%)</td><td>124.70 (+2.72%)</td><td>22.48 <b>(-37.34%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>198.60 (n/a)</td><td>156.96 (n/a)</td><td>148.40 (n/a)</td><td>121.40 (n/a)</td><td>35.88 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (-3.01%)</td><td>0.14 (+12.45%)</td><td>0.15 <b>(+34.62%)</b></td><td>0.12 <b>(+22.78%)</b></td><td>0.01 <b>(-47.95%)</b></td><td>166.20 (-18.57%)</td><td>146.58 (-13.73%)</td><td>136.50 <b>(-25.73%)</b></td><td>134.10 (+3.07%)</td><td>16.01 <b>(-55.75%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>204.10 (n/a)</td><td>169.90 (n/a)</td><td>183.80 (n/a)</td><td>130.10 (n/a)</td><td>36.17 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 <b>(-28.89%)</b></td><td>0.11 (-8.14%)</td><td>0.11 (+9.59%)</td><td>0.10 (+12.86%)</td><td>0.01 <b>(-74.12%)</b></td><td>202.10 (-11.40%)</td><td>181.52 (+1.98%)</td><td>186.10 (-8.73%)</td><td>164.70 <b>(+40.65%)</b></td><td>15.86 <b>(-68.07%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>228.10 (n/a)</td><td>178.00 (n/a)</td><td>203.90 (n/a)</td><td>117.10 (n/a)</td><td>49.67 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (-0.29%)</td><td>0.10 (-2.92%)</td><td>0.11 (+2.62%)</td><td>0.08 (-14.70%)</td><td>0.02 <b>(+28.82%)</b></td><td>264.80 (+17.22%)</td><td>201.20 (+4.34%)</td><td>181.90 (-2.57%)</td><td>169.90 (+0.30%)</td><td>38.84 <b>(+54.52%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>192.84 (n/a)</td><td>186.70 (n/a)</td><td>169.40 (n/a)</td><td>25.13 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (-3.79%)</td><td>0.12 (+1.24%)</td><td>0.12 (-2.52%)</td><td>0.10 <b>(+26.03%)</b></td><td>0.01 <b>(-49.60%)</b></td><td>198.10 <b>(-20.66%)</b></td><td>175.68 (-3.56%)</td><td>169.20 (+2.61%)</td><td>160.30 (+3.96%)</td><td>15.83 <b>(-59.43%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>249.70 (n/a)</td><td>182.16 (n/a)</td><td>164.90 (n/a)</td><td>154.20 (n/a)</td><td>39.01 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.17 (+6.30%)</td><td>0.12 (+2.10%)</td><td>0.11 (-2.50%)</td><td>0.09 (-16.20%)</td><td>0.03 <b>(+58.77%)</b></td><td>226.30 (+19.36%)</td><td>174.42 (+1.75%)</td><td>183.20 (+2.52%)</td><td>120.00 (-5.96%)</td><td>45.75 <b>(+79.64%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>189.60 (n/a)</td><td>171.42 (n/a)</td><td>178.70 (n/a)</td><td>127.60 (n/a)</td><td>25.47 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 <b>(+23.65%)</b></td><td>0.12 <b>(+20.10%)</b></td><td>0.12 <b>(+27.55%)</b></td><td>0.09 (+7.27%)</td><td>0.02 <b>(+126.51%)</b></td><td>215.80 (-6.78%)</td><td>178.98 (-15.46%)</td><td>163.90 <b>(-21.58%)</b></td><td>152.90 (-19.14%)</td><td>29.28 <b>(+70.40%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>231.50 (n/a)</td><td>211.72 (n/a)</td><td>209.00 (n/a)</td><td>189.10 (n/a)</td><td>17.18 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (+10.41%)</td><td>0.12 <b>(+23.69%)</b></td><td>0.12 <b>(+27.59%)</b></td><td>0.09 <b>(+20.81%)</b></td><td>0.02 (+12.08%)</td><td>224.30 (-17.20%)</td><td>178.92 (-19.25%)</td><td>167.70 <b>(-21.60%)</b></td><td>146.10 (-9.42%)</td><td>35.14 (-15.50%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>270.90 (n/a)</td><td>221.58 (n/a)</td><td>213.90 (n/a)</td><td>161.30 (n/a)</td><td>41.59 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (-0.66%)</td><td>0.18 (+3.43%)</td><td>0.19 (+0.91%)</td><td>0.13 (+16.48%)</td><td>0.03 <b>(-20.01%)</b></td><td>183.40 (-14.14%)</td><td>141.48 (-5.24%)</td><td>128.40 (-0.85%)</td><td>118.60 (+0.59%)</td><td>26.44 <b>(-31.71%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>213.60 (n/a)</td><td>149.30 (n/a)</td><td>129.50 (n/a)</td><td>117.90 (n/a)</td><td>38.73 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (-2.47%)</td><td>0.16 (+15.98%)</td><td>0.15 (+7.71%)</td><td>0.14 <b>(+62.12%)</b></td><td>0.03 <b>(-36.00%)</b></td><td>177.70 <b>(-38.34%)</b></td><td>151.96 (-18.51%)</td><td>163.10 (-7.17%)</td><td>126.90 (+2.59%)</td><td>23.31 <b>(-62.26%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>288.20 (n/a)</td><td>186.48 (n/a)</td><td>175.70 (n/a)</td><td>123.70 (n/a)</td><td>61.76 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (+6.56%)</td><td>0.14 (-7.37%)</td><td>0.13 (-11.07%)</td><td>0.11 (-3.71%)</td><td>0.03 <b>(+22.45%)</b></td><td>222.70 (+3.82%)</td><td>185.46 (+9.20%)</td><td>191.90 (+12.42%)</td><td>128.60 (-6.13%)</td><td>36.89 (+18.63%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>214.50 (n/a)</td><td>169.84 (n/a)</td><td>170.70 (n/a)</td><td>137.00 (n/a)</td><td>31.10 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 <b>(+27.01%)</b></td><td>0.16 <b>(+24.87%)</b></td><td>0.16 <b>(+26.52%)</b></td><td>0.13 <b>(+33.51%)</b></td><td>0.02 <b>(+22.89%)</b></td><td>190.30 <b>(-25.11%)</b></td><td>157.86 <b>(-20.13%)</b></td><td>149.70 <b>(-20.96%)</b></td><td>128.20 <b>(-21.30%)</b></td><td>24.34 <b>(-28.88%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>254.10 (n/a)</td><td>197.64 (n/a)</td><td>189.40 (n/a)</td><td>162.90 (n/a)</td><td>34.22 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 <b>(+49.56%)</b></td><td>0.14 (+13.36%)</td><td>0.13 (+2.78%)</td><td>0.11 (-3.29%)</td><td>0.03 <b>(+436.85%)</b></td><td>222.70 (+3.39%)</td><td>183.24 (-8.02%)</td><td>192.90 (-2.72%)</td><td>126.30 <b>(-33.14%)</b></td><td>40.16 <b>(+273.71%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>215.40 (n/a)</td><td>199.22 (n/a)</td><td>198.30 (n/a)</td><td>188.90 (n/a)</td><td>10.75 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (-9.66%)</td><td>0.12 (+1.94%)</td><td>0.13 (+9.52%)</td><td>0.11 (+5.04%)</td><td>0.01 <b>(-41.46%)</b></td><td>222.10 (-4.80%)</td><td>198.26 (-3.25%)</td><td>196.10 (-8.66%)</td><td>169.10 (+10.67%)</td><td>19.61 <b>(-36.92%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>233.30 (n/a)</td><td>204.92 (n/a)</td><td>214.70 (n/a)</td><td>152.80 (n/a)</td><td>31.09 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (-4.54%)</td><td>0.14 (+9.97%)</td><td>0.14 (+12.74%)</td><td>0.11 (+18.49%)</td><td>0.02 <b>(-21.13%)</b></td><td>216.50 (-15.59%)</td><td>175.80 (-10.44%)</td><td>172.30 (-11.32%)</td><td>149.90 (+4.75%)</td><td>27.90 <b>(-31.04%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>256.50 (n/a)</td><td>196.30 (n/a)</td><td>194.30 (n/a)</td><td>143.10 (n/a)</td><td>40.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (+13.28%)</td><td>0.13 (+8.92%)</td><td>0.12 (+0.95%)</td><td>0.11 (+6.74%)</td><td>0.02 <b>(+63.41%)</b></td><td>219.40 (-6.32%)</td><td>189.00 (-7.31%)</td><td>200.20 (-0.94%)</td><td>157.00 (-11.70%)</td><td>27.43 <b>(+32.25%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>234.20 (n/a)</td><td>203.90 (n/a)</td><td>202.10 (n/a)</td><td>177.80 (n/a)</td><td>20.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (-19.85%)</td><td>0.10 (-11.70%)</td><td>0.10 (-10.79%)</td><td>0.09 (-0.85%)</td><td>0.01 <b>(-46.19%)</b></td><td>213.80 (+0.85%)</td><td>179.82 (+10.69%)</td><td>175.70 (+12.05%)</td><td>150.60 <b>(+24.77%)</b></td><td>23.55 <b>(-32.29%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>212.00 (n/a)</td><td>162.46 (n/a)</td><td>156.80 (n/a)</td><td>120.70 (n/a)</td><td>34.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (+2.36%)</td><td>0.12 (+8.32%)</td><td>0.12 (+12.81%)</td><td>0.08 (+7.11%)</td><td>0.03 (+2.30%)</td><td>220.10 (-6.62%)</td><td>157.44 (-7.84%)</td><td>148.60 (-11.39%)</td><td>124.60 (-2.35%)</td><td>37.86 (-6.77%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>235.70 (n/a)</td><td>170.84 (n/a)</td><td>167.70 (n/a)</td><td>127.60 (n/a)</td><td>40.61 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (-15.42%)</td><td>0.10 (-6.68%)</td><td>0.10 (-7.12%)</td><td>0.09 (-8.46%)</td><td>0.01 <b>(-26.20%)</b></td><td>214.20 (+9.23%)</td><td>182.08 (+6.58%)</td><td>187.00 (+7.66%)</td><td>154.70 (+18.27%)</td><td>23.91 (-3.41%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>196.10 (n/a)</td><td>170.84 (n/a)</td><td>173.70 (n/a)</td><td>130.80 (n/a)</td><td>24.76 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 <b>(+26.43%)</b></td><td>0.12 (+17.58%)</td><td>0.10 (+1.36%)</td><td>0.10 (+15.98%)</td><td>0.03 <b>(+73.38%)</b></td><td>190.30 (-13.77%)</td><td>165.70 (-13.35%)</td><td>189.10 (-1.30%)</td><td>122.60 <b>(-20.90%)</b></td><td>33.17 <b>(+20.67%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>220.70 (n/a)</td><td>191.24 (n/a)</td><td>191.60 (n/a)</td><td>155.00 (n/a)</td><td>27.49 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (-9.71%)</td><td>0.11 (+1.48%)</td><td>0.11 (+13.60%)</td><td>0.08 (+2.76%)</td><td>0.01 <b>(-26.81%)</b></td><td>218.40 (-2.67%)</td><td>173.84 (-2.52%)</td><td>162.30 (-11.98%)</td><td>149.90 (+10.79%)</td><td>26.66 (-18.55%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>224.40 (n/a)</td><td>178.34 (n/a)</td><td>184.40 (n/a)</td><td>135.30 (n/a)</td><td>32.73 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (+8.14%)</td><td>0.11 (+15.01%)</td><td>0.11 (+15.68%)</td><td>0.09 <b>(+42.76%)</b></td><td>0.02 (-19.17%)</td><td>202.20 <b>(-29.96%)</b></td><td>164.62 (-15.96%)</td><td>162.80 (-13.54%)</td><td>135.40 (-7.51%)</td><td>29.69 <b>(-48.33%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>288.70 (n/a)</td><td>195.88 (n/a)</td><td>188.30 (n/a)</td><td>146.40 (n/a)</td><td>57.46 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (-8.48%)</td><td>0.08 (+1.60%)</td><td>0.09 (+14.37%)</td><td>0.05 (+0.84%)</td><td>0.02 <b>(-25.57%)</b></td><td>336.10 (-0.83%)</td><td>230.02 (-4.61%)</td><td>204.90 (-12.59%)</td><td>168.20 (+9.29%)</td><td>64.22 (-16.46%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>338.90 (n/a)</td><td>241.14 (n/a)</td><td>234.40 (n/a)</td><td>153.90 (n/a)</td><td>76.87 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (-13.40%)</td><td>0.09 (+4.44%)</td><td>0.09 (+12.06%)</td><td>0.07 <b>(+30.77%)</b></td><td>0.01 <b>(-58.72%)</b></td><td>246.10 <b>(-23.52%)</b></td><td>203.46 (-9.38%)</td><td>196.80 (-10.79%)</td><td>180.20 (+15.44%)</td><td>24.92 <b>(-62.06%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>321.80 (n/a)</td><td>224.52 (n/a)</td><td>220.60 (n/a)</td><td>156.10 (n/a)</td><td>65.69 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.76 (-10.05%)</td><td>0.62 (+11.63%)</td><td>0.67 <b>(+35.94%)</b></td><td>0.45 (+3.02%)</td><td>0.13 <b>(-23.47%)</b></td><td>218.40 (-2.93%)</td><td>163.92 (-11.94%)</td><td>146.30 <b>(-26.45%)</b></td><td>128.80 (+11.13%)</td><td>36.60 (-11.40%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.85 (n/a)</td><td>0.56 (n/a)</td><td>0.49 (n/a)</td><td>0.44 (n/a)</td><td>0.17 (n/a)</td><td>225.00 (n/a)</td><td>186.14 (n/a)</td><td>198.90 (n/a)</td><td>115.90 (n/a)</td><td>41.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.65 (-16.88%)</td><td>0.50 (-12.68%)</td><td>0.48 (-10.31%)</td><td>0.38 <b>(-20.59%)</b></td><td>0.11 (-11.22%)</td><td>258.00 <b>(+25.92%)</b></td><td>203.30 (+15.28%)</td><td>203.50 (+11.51%)</td><td>150.80 <b>(+20.35%)</b></td><td>42.74 <b>(+37.92%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.78 (n/a)</td><td>0.57 (n/a)</td><td>0.54 (n/a)</td><td>0.48 (n/a)</td><td>0.12 (n/a)</td><td>204.90 (n/a)</td><td>176.36 (n/a)</td><td>182.50 (n/a)</td><td>125.30 (n/a)</td><td>30.99 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.60 (-2.41%)</td><td>0.52 (-1.86%)</td><td>0.52 (-3.89%)</td><td>0.43 (-10.55%)</td><td>0.06 (+16.37%)</td><td>227.50 (+11.79%)</td><td>189.60 (+2.33%)</td><td>190.60 (+4.04%)</td><td>164.00 (+2.44%)</td><td>24.29 <b>(+32.25%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.61 (n/a)</td><td>0.53 (n/a)</td><td>0.54 (n/a)</td><td>0.48 (n/a)</td><td>0.05 (n/a)</td><td>203.50 (n/a)</td><td>185.28 (n/a)</td><td>183.20 (n/a)</td><td>160.10 (n/a)</td><td>18.37 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.82 <b>(+30.81%)</b></td><td>0.62 <b>(+37.31%)</b></td><td>0.57 <b>(+30.18%)</b></td><td>0.49 <b>(+39.12%)</b></td><td>0.13 <b>(+24.99%)</b></td><td>202.40 <b>(-28.13%)</b></td><td>162.96 <b>(-27.53%)</b></td><td>173.20 <b>(-23.19%)</b></td><td>120.60 <b>(-23.53%)</b></td><td>32.22 <b>(-31.05%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.62 (n/a)</td><td>0.45 (n/a)</td><td>0.44 (n/a)</td><td>0.35 (n/a)</td><td>0.11 (n/a)</td><td>281.60 (n/a)</td><td>224.86 (n/a)</td><td>225.50 (n/a)</td><td>157.70 (n/a)</td><td>46.73 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.60 (+1.92%)</td><td>0.50 (+16.54%)</td><td>0.54 <b>(+35.97%)</b></td><td>0.37 (+0.38%)</td><td>0.10 (+6.93%)</td><td>201.70 (-0.40%)</td><td>153.08 (-13.79%)</td><td>136.80 <b>(-26.45%)</b></td><td>122.70 (-1.92%)</td><td>32.99 (+9.51%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.59 (n/a)</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.09 (n/a)</td><td>202.50 (n/a)</td><td>177.56 (n/a)</td><td>186.00 (n/a)</td><td>125.10 (n/a)</td><td>30.13 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.54 (-19.92%)</td><td>0.43 (+14.41%)</td><td>0.38 (+18.78%)</td><td>0.35 <b>(+62.81%)</b></td><td>0.09 <b>(-49.38%)</b></td><td>208.80 <b>(-38.59%)</b></td><td>178.56 <b>(-21.24%)</b></td><td>194.20 (-15.78%)</td><td>135.50 <b>(+24.88%)</b></td><td>34.90 <b>(-57.47%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.68 (n/a)</td><td>0.37 (n/a)</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>340.00 (n/a)</td><td>226.72 (n/a)</td><td>230.60 (n/a)</td><td>108.50 (n/a)</td><td>82.06 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.45 <b>(-24.15%)</b></td><td>0.33 <b>(-20.56%)</b></td><td>0.31 (-13.81%)</td><td>0.20 <b>(-25.20%)</b></td><td>0.10 <b>(-27.11%)</b></td><td>362.40 <b>(+33.68%)</b></td><td>239.30 <b>(+25.39%)</b></td><td>239.40 (+16.04%)</td><td>165.60 <b>(+31.85%)</b></td><td>77.96 <b>(+31.67%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.59 (n/a)</td><td>0.42 (n/a)</td><td>0.36 (n/a)</td><td>0.27 (n/a)</td><td>0.13 (n/a)</td><td>271.10 (n/a)</td><td>190.84 (n/a)</td><td>206.30 (n/a)</td><td>125.60 (n/a)</td><td>59.21 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.42 (-12.10%)</td><td>0.35 (-8.50%)</td><td>0.33 (-6.23%)</td><td>0.33 (+5.26%)</td><td>0.04 <b>(-45.57%)</b></td><td>225.20 (-4.98%)</td><td>209.92 (+7.23%)</td><td>222.70 (+6.66%)</td><td>174.90 (+13.79%)</td><td>21.71 <b>(-39.60%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.48 (n/a)</td><td>0.39 (n/a)</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.07 (n/a)</td><td>237.00 (n/a)</td><td>195.76 (n/a)</td><td>208.80 (n/a)</td><td>153.70 (n/a)</td><td>35.94 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (+11.05%)</td><td>0.21 (+7.25%)</td><td>0.21 (+8.42%)</td><td>0.19 (+11.53%)</td><td>0.02 (-3.13%)</td><td>196.70 (-10.35%)</td><td>175.10 (-7.00%)</td><td>173.30 (-7.77%)</td><td>150.50 (-9.93%)</td><td>16.86 <b>(-21.61%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>219.40 (n/a)</td><td>188.28 (n/a)</td><td>187.90 (n/a)</td><td>167.10 (n/a)</td><td>21.50 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (+12.34%)</td><td>0.21 (+16.08%)</td><td>0.21 <b>(+20.04%)</b></td><td>0.19 (+18.90%)</td><td>0.01 <b>(-32.66%)</b></td><td>192.30 (-15.92%)</td><td>177.48 (-14.24%)</td><td>178.10 (-16.66%)</td><td>165.80 (-10.96%)</td><td>9.92 <b>(-48.60%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>228.70 (n/a)</td><td>206.96 (n/a)</td><td>213.70 (n/a)</td><td>186.20 (n/a)</td><td>19.31 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.28 (+6.09%)</td><td>0.21 (-2.39%)</td><td>0.20 (-3.75%)</td><td>0.16 (-5.09%)</td><td>0.05 (+12.76%)</td><td>234.60 (+5.39%)</td><td>185.04 (+3.46%)</td><td>180.40 (+3.92%)</td><td>129.50 (-5.68%)</td><td>43.54 (+12.70%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>222.60 (n/a)</td><td>178.86 (n/a)</td><td>173.60 (n/a)</td><td>137.30 (n/a)</td><td>38.64 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.33 <b>(+35.90%)</b></td><td>0.24 (+17.04%)</td><td>0.21 (-3.43%)</td><td>0.20 (+18.42%)</td><td>0.06 <b>(+120.91%)</b></td><td>188.50 (-15.58%)</td><td>158.94 (-11.82%)</td><td>179.30 (+3.58%)</td><td>112.00 <b>(-26.41%)</b></td><td>36.33 <b>(+37.43%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>223.30 (n/a)</td><td>180.24 (n/a)</td><td>173.10 (n/a)</td><td>152.20 (n/a)</td><td>26.43 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.29 <b>(+38.91%)</b></td><td>0.23 <b>(+38.50%)</b></td><td>0.21 <b>(+30.65%)</b></td><td>0.21 <b>(+47.21%)</b></td><td>0.04 <b>(+33.94%)</b></td><td>177.30 <b>(-32.07%)</b></td><td>160.96 <b>(-27.95%)</b></td><td>172.50 <b>(-23.47%)</b></td><td>125.40 <b>(-28.01%)</b></td><td>21.40 <b>(-33.78%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>261.00 (n/a)</td><td>223.40 (n/a)</td><td>225.40 (n/a)</td><td>174.20 (n/a)</td><td>32.32 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (-19.65%)</td><td>0.19 (-3.78%)</td><td>0.20 (+10.36%)</td><td>0.16 (-0.03%)</td><td>0.02 <b>(-46.32%)</b></td><td>226.90 (+0.00%)</td><td>195.62 (+1.57%)</td><td>187.70 (-9.37%)</td><td>166.70 <b>(+24.50%)</b></td><td>25.79 <b>(-31.63%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>226.90 (n/a)</td><td>192.60 (n/a)</td><td>207.10 (n/a)</td><td>133.90 (n/a)</td><td>37.73 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 <b>(-26.91%)</b></td><td>0.19 (-5.24%)</td><td>0.19 (+7.74%)</td><td>0.12 (-14.41%)</td><td>0.05 <b>(-37.55%)</b></td><td>305.50 (+16.87%)</td><td>204.34 (+1.74%)</td><td>195.90 (-7.16%)</td><td>152.10 <b>(+36.90%)</b></td><td>61.76 (-1.62%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.33 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>261.40 (n/a)</td><td>200.84 (n/a)</td><td>211.00 (n/a)</td><td>111.10 (n/a)</td><td>62.78 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (+5.62%)</td><td>0.20 (+12.21%)</td><td>0.19 (+13.96%)</td><td>0.15 (+11.70%)</td><td>0.03 (-3.46%)</td><td>242.20 (-10.46%)</td><td>192.76 (-11.36%)</td><td>196.20 (-12.25%)</td><td>155.40 (-5.36%)</td><td>32.79 (-16.83%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>270.50 (n/a)</td><td>217.46 (n/a)</td><td>223.60 (n/a)</td><td>164.20 (n/a)</td><td>39.42 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.32 (-7.56%)</td><td>0.25 (+3.20%)</td><td>0.22 (+2.01%)</td><td>0.20 (-4.85%)</td><td>0.06 (-5.90%)</td><td>207.60 (+5.11%)</td><td>170.16 (-3.04%)</td><td>188.20 (-1.93%)</td><td>127.50 (+8.14%)</td><td>35.57 (+7.68%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.35 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.06 (n/a)</td><td>197.50 (n/a)</td><td>175.50 (n/a)</td><td>191.90 (n/a)</td><td>117.90 (n/a)</td><td>33.03 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.29 (+9.94%)</td><td>0.23 (+0.11%)</td><td>0.23 (+0.91%)</td><td>0.19 (-5.05%)</td><td>0.04 <b>(+62.04%)</b></td><td>213.50 (+5.33%)</td><td>184.36 (+1.15%)</td><td>182.00 (-0.93%)</td><td>141.70 (-9.05%)</td><td>28.38 <b>(+55.48%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>202.70 (n/a)</td><td>182.26 (n/a)</td><td>183.70 (n/a)</td><td>155.80 (n/a)</td><td>18.25 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.36 (+16.81%)</td><td>0.24 (+9.62%)</td><td>0.20 (+5.91%)</td><td>0.18 (-1.58%)</td><td>0.08 <b>(+42.80%)</b></td><td>226.30 (+1.62%)</td><td>181.32 (-6.02%)</td><td>204.30 (-5.59%)</td><td>113.30 (-14.43%)</td><td>49.01 <b>(+23.69%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>222.70 (n/a)</td><td>192.94 (n/a)</td><td>216.40 (n/a)</td><td>132.40 (n/a)</td><td>39.62 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.32 (+15.84%)</td><td>0.22 (+2.78%)</td><td>0.20 (-10.60%)</td><td>0.16 (-8.38%)</td><td>0.07 <b>(+53.80%)</b></td><td>256.80 (+9.14%)</td><td>194.38 (+0.47%)</td><td>206.30 (+11.82%)</td><td>127.20 (-13.65%)</td><td>51.02 <b>(+39.56%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>235.30 (n/a)</td><td>193.48 (n/a)</td><td>184.50 (n/a)</td><td>147.30 (n/a)</td><td>36.56 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.31 (+11.18%)</td><td>0.23 (-0.71%)</td><td>0.20 (-11.75%)</td><td>0.19 (-5.69%)</td><td>0.05 <b>(+70.11%)</b></td><td>218.50 (+6.07%)</td><td>184.40 (+3.02%)</td><td>203.90 (+13.34%)</td><td>132.60 (-10.04%)</td><td>36.16 <b>(+63.81%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>206.00 (n/a)</td><td>179.00 (n/a)</td><td>179.90 (n/a)</td><td>147.40 (n/a)</td><td>22.08 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 (-17.46%)</td><td>0.22 (-9.90%)</td><td>0.22 (-8.35%)</td><td>0.18 (-14.25%)</td><td>0.03 <b>(-25.41%)</b></td><td>227.50 (+16.67%)</td><td>187.94 (+10.63%)</td><td>183.90 (+9.07%)</td><td>162.40 <b>(+21.19%)</b></td><td>25.30 (+7.24%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>195.00 (n/a)</td><td>169.88 (n/a)</td><td>168.60 (n/a)</td><td>134.00 (n/a)</td><td>23.59 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.26 (-16.84%)</td><td>0.20 (-3.18%)</td><td>0.20 (+3.92%)</td><td>0.15 (-4.43%)</td><td>0.04 <b>(-35.20%)</b></td><td>274.10 (+4.62%)</td><td>207.32 (+0.70%)</td><td>200.80 (-3.74%)</td><td>157.20 <b>(+20.28%)</b></td><td>42.58 (-14.98%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>262.00 (n/a)</td><td>205.88 (n/a)</td><td>208.60 (n/a)</td><td>130.70 (n/a)</td><td>50.08 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.28 (-19.00%)</td><td>0.23 (-9.98%)</td><td>0.22 (-14.09%)</td><td>0.19 <b>(+40.48%)</b></td><td>0.03 <b>(-61.93%)</b></td><td>217.80 <b>(-28.82%)</b></td><td>183.32 (+0.04%)</td><td>184.50 (+16.40%)</td><td>147.60 <b>(+23.51%)</b></td><td>26.32 <b>(-65.96%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>306.00 (n/a)</td><td>183.24 (n/a)</td><td>158.50 (n/a)</td><td>119.50 (n/a)</td><td>77.32 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.29 <b>(+22.98%)</b></td><td>0.21 (+14.94%)</td><td>0.20 (+17.60%)</td><td>0.17 (+2.97%)</td><td>0.05 <b>(+64.63%)</b></td><td>209.50 (-2.87%)</td><td>173.08 (-11.06%)</td><td>171.90 (-14.99%)</td><td>119.80 (-18.67%)</td><td>36.61 <b>(+35.01%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>215.70 (n/a)</td><td>194.60 (n/a)</td><td>202.20 (n/a)</td><td>147.30 (n/a)</td><td>27.11 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (-12.34%)</td><td>0.19 (+0.51%)</td><td>0.19 (+4.48%)</td><td>0.17 (+15.90%)</td><td>0.02 <b>(-51.57%)</b></td><td>206.80 (-13.69%)</td><td>180.50 (-3.19%)</td><td>180.40 (-4.30%)</td><td>156.40 (+14.08%)</td><td>18.67 <b>(-51.92%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>239.60 (n/a)</td><td>186.44 (n/a)</td><td>188.50 (n/a)</td><td>137.10 (n/a)</td><td>38.84 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (-10.53%)</td><td>0.20 (+3.15%)</td><td>0.19 (+3.06%)</td><td>0.17 <b>(+22.86%)</b></td><td>0.03 <b>(-41.91%)</b></td><td>203.20 (-18.62%)</td><td>176.48 (-6.23%)</td><td>184.80 (-2.94%)</td><td>142.70 (+11.75%)</td><td>23.97 <b>(-46.60%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>249.70 (n/a)</td><td>188.20 (n/a)</td><td>190.40 (n/a)</td><td>127.70 (n/a)</td><td>44.88 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 <b>(-24.09%)</b></td><td>0.20 (-4.95%)</td><td>0.19 (-1.78%)</td><td>0.18 (+19.04%)</td><td>0.02 <b>(-62.16%)</b></td><td>196.80 (-15.97%)</td><td>176.72 (-0.62%)</td><td>185.30 (+1.81%)</td><td>146.50 <b>(+31.74%)</b></td><td>20.40 <b>(-57.88%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.07 (n/a)</td><td>234.20 (n/a)</td><td>177.82 (n/a)</td><td>182.00 (n/a)</td><td>111.20 (n/a)</td><td>48.44 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (-1.92%)</td><td>0.21 (+1.75%)</td><td>0.20 (-13.92%)</td><td>0.17 (+18.86%)</td><td>0.03 <b>(-40.87%)</b></td><td>203.90 (-15.85%)</td><td>169.88 (-4.72%)</td><td>173.20 (+16.16%)</td><td>147.10 (+1.94%)</td><td>22.78 <b>(-48.63%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>242.30 (n/a)</td><td>178.30 (n/a)</td><td>149.10 (n/a)</td><td>144.30 (n/a)</td><td>44.35 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.30 (+18.64%)</td><td>0.22 (+18.22%)</td><td>0.21 (+14.34%)</td><td>0.18 <b>(+46.55%)</b></td><td>0.05 (-0.74%)</td><td>195.00 <b>(-31.77%)</b></td><td>161.36 (-17.49%)</td><td>164.00 (-12.53%)</td><td>116.10 (-15.69%)</td><td>29.10 <b>(-46.76%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>285.80 (n/a)</td><td>195.56 (n/a)</td><td>187.50 (n/a)</td><td>137.70 (n/a)</td><td>54.66 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (-0.49%)</td><td>0.17 (+0.93%)</td><td>0.18 (+13.18%)</td><td>0.11 (-18.69%)</td><td>0.04 <b>(+38.11%)</b></td><td>319.10 <b>(+23.01%)</b></td><td>217.28 (+2.66%)</td><td>189.80 (-11.64%)</td><td>159.20 (+0.44%)</td><td>64.14 <b>(+78.55%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>259.40 (n/a)</td><td>211.64 (n/a)</td><td>214.80 (n/a)</td><td>158.50 (n/a)</td><td>35.93 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.20 <b>(-35.19%)</b></td><td>0.17 (-17.23%)</td><td>0.18 (+7.49%)</td><td>0.13 (-4.22%)</td><td>0.02 <b>(-66.57%)</b></td><td>259.50 (+4.38%)</td><td>206.40 (+12.66%)</td><td>194.80 (-6.97%)</td><td>178.30 <b>(+54.37%)</b></td><td>31.94 <b>(-43.69%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.30 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>248.60 (n/a)</td><td>183.20 (n/a)</td><td>209.40 (n/a)</td><td>115.50 (n/a)</td><td>56.72 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.03 <b>(+36.24%)</b></td><td>0.85 <b>(+23.48%)</b></td><td>0.83 (+17.74%)</td><td>0.68 (+16.56%)</td><td>0.15 <b>(+122.39%)</b></td><td>193.20 (-14.21%)</td><td>158.36 (-17.63%)</td><td>158.70 (-15.04%)</td><td>127.20 <b>(-26.60%)</b></td><td>28.01 <b>(+37.57%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.76 (n/a)</td><td>0.69 (n/a)</td><td>0.70 (n/a)</td><td>0.58 (n/a)</td><td>0.07 (n/a)</td><td>225.20 (n/a)</td><td>192.26 (n/a)</td><td>186.80 (n/a)</td><td>173.30 (n/a)</td><td>20.36 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.07 <b>(+39.58%)</b></td><td>0.88 (+18.95%)</td><td>0.79 (+6.83%)</td><td>0.77 (+8.62%)</td><td>0.14 <b>(+463.57%)</b></td><td>171.30 (-7.95%)</td><td>152.30 (-14.48%)</td><td>165.40 (-6.40%)</td><td>122.00 <b>(-28.36%)</b></td><td>21.91 <b>(+273.69%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.77 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.70 (n/a)</td><td>0.02 (n/a)</td><td>186.10 (n/a)</td><td>178.08 (n/a)</td><td>176.70 (n/a)</td><td>170.30 (n/a)</td><td>5.86 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.13 <b>(+24.38%)</b></td><td>0.96 <b>(+40.91%)</b></td><td>0.91 <b>(+36.00%)</b></td><td>0.84 <b>(+69.93%)</b></td><td>0.13 (-12.75%)</td><td>155.70 <b>(-41.16%)</b></td><td>138.74 <b>(-30.75%)</b></td><td>144.30 <b>(-26.45%)</b></td><td>115.60 (-19.61%)</td><td>18.46 <b>(-58.14%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.91 (n/a)</td><td>0.68 (n/a)</td><td>0.67 (n/a)</td><td>0.50 (n/a)</td><td>0.15 (n/a)</td><td>264.60 (n/a)</td><td>200.34 (n/a)</td><td>196.20 (n/a)</td><td>143.80 (n/a)</td><td>44.10 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (+17.44%)</td><td>0.03 <b>(+25.05%)</b></td><td>0.03 <b>(+26.80%)</b></td><td>0.02 <b>(+21.65%)</b></td><td>0.01 (+12.60%)</td><td>187.10 (-17.79%)</td><td>136.44 <b>(-20.25%)</b></td><td>126.70 <b>(-21.16%)</b></td><td>117.60 (-14.84%)</td><td>28.58 (-19.28%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.60 (n/a)</td><td>171.08 (n/a)</td><td>160.70 (n/a)</td><td>138.10 (n/a)</td><td>35.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 <b>(+55.40%)</b></td><td>0.03 <b>(+23.07%)</b></td><td>0.03 (+5.83%)</td><td>0.02 <b>(+21.24%)</b></td><td>0.01 <b>(+116.43%)</b></td><td>185.70 (-17.50%)</td><td>143.16 (-16.39%)</td><td>151.40 (-5.49%)</td><td>93.50 <b>(-35.69%)</b></td><td>33.66 (+7.18%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>225.10 (n/a)</td><td>171.22 (n/a)</td><td>160.20 (n/a)</td><td>145.40 (n/a)</td><td>31.41 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (+8.80%)</td><td>0.02 (-7.02%)</td><td>0.02 (-14.96%)</td><td>0.02 (-14.52%)</td><td>0.01 <b>(+116.48%)</b></td><td>201.00 (+17.00%)</td><td>172.16 (+10.59%)</td><td>184.60 (+17.58%)</td><td>124.50 (-8.12%)</td><td>33.74 <b>(+138.25%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.80 (n/a)</td><td>155.68 (n/a)</td><td>157.00 (n/a)</td><td>135.50 (n/a)</td><td>14.16 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>17.18 (+5.05%)</td><td>14.20 (+3.06%)</td><td>14.81 (+16.83%)</td><td>10.89 (-9.48%)</td><td>2.56 <b>(+24.90%)</b></td><td>192.70 (+10.49%)</td><td>151.90 (-1.91%)</td><td>141.70 (-14.38%)</td><td>122.10 (-4.83%)</td><td>28.90 <b>(+32.26%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>16.36 (n/a)</td><td>13.78 (n/a)</td><td>12.68 (n/a)</td><td>12.03 (n/a)</td><td>2.05 (n/a)</td><td>174.40 (n/a)</td><td>154.86 (n/a)</td><td>165.50 (n/a)</td><td>128.30 (n/a)</td><td>21.85 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.09 (+4.13%)</td><td>1.02 <b>(+21.07%)</b></td><td>1.03 <b>(+29.52%)</b></td><td>0.93 <b>(+25.34%)</b></td><td>0.07 <b>(-44.93%)</b></td><td>142.00 <b>(-20.22%)</b></td><td>129.48 (-18.35%)</td><td>128.80 <b>(-22.83%)</b></td><td>121.30 (-3.96%)</td><td>8.68 <b>(-57.79%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.05 (n/a)</td><td>0.85 (n/a)</td><td>0.79 (n/a)</td><td>0.74 (n/a)</td><td>0.12 (n/a)</td><td>178.00 (n/a)</td><td>158.58 (n/a)</td><td>166.90 (n/a)</td><td>126.30 (n/a)</td><td>20.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.93 (-16.26%)</td><td>0.86 (+9.54%)</td><td>0.90 <b>(+26.13%)</b></td><td>0.66 (+8.53%)</td><td>0.11 <b>(-42.37%)</b></td><td>200.10 (-7.87%)</td><td>156.58 (-10.98%)</td><td>146.00 <b>(-20.74%)</b></td><td>141.50 (+19.41%)</td><td>24.61 <b>(-32.77%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.11 (n/a)</td><td>0.78 (n/a)</td><td>0.72 (n/a)</td><td>0.61 (n/a)</td><td>0.20 (n/a)</td><td>217.20 (n/a)</td><td>175.90 (n/a)</td><td>184.20 (n/a)</td><td>118.50 (n/a)</td><td>36.60 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.02 (-3.09%)</td><td>0.88 (+4.17%)</td><td>0.85 (+6.63%)</td><td>0.67 (+6.84%)</td><td>0.14 (-12.25%)</td><td>197.60 (-6.40%)</td><td>154.16 (-4.75%)</td><td>154.70 (-6.24%)</td><td>129.10 (+3.20%)</td><td>27.16 (-15.71%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.06 (n/a)</td><td>0.84 (n/a)</td><td>0.80 (n/a)</td><td>0.63 (n/a)</td><td>0.16 (n/a)</td><td>211.10 (n/a)</td><td>161.84 (n/a)</td><td>165.00 (n/a)</td><td>125.10 (n/a)</td><td>32.22 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.22 (+1.44%)</td><td>0.94 (+10.19%)</td><td>0.90 (+7.53%)</td><td>0.70 (+15.10%)</td><td>0.19 (-11.62%)</td><td>189.70 (-13.10%)</td><td>144.90 (-10.64%)</td><td>147.30 (-7.01%)</td><td>108.70 (-1.45%)</td><td>30.30 <b>(-23.37%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.20 (n/a)</td><td>0.86 (n/a)</td><td>0.83 (n/a)</td><td>0.61 (n/a)</td><td>0.22 (n/a)</td><td>218.30 (n/a)</td><td>162.16 (n/a)</td><td>158.40 (n/a)</td><td>110.30 (n/a)</td><td>39.54 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.01 (+5.31%)</td><td>0.90 (+12.69%)</td><td>0.87 (+4.85%)</td><td>0.82 <b>(+39.71%)</b></td><td>0.07 <b>(-46.66%)</b></td><td>161.00 <b>(-28.41%)</b></td><td>147.72 (-13.15%)</td><td>151.50 (-4.60%)</td><td>130.40 (-5.09%)</td><td>11.48 <b>(-65.17%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.96 (n/a)</td><td>0.80 (n/a)</td><td>0.83 (n/a)</td><td>0.59 (n/a)</td><td>0.14 (n/a)</td><td>224.90 (n/a)</td><td>170.08 (n/a)</td><td>158.80 (n/a)</td><td>137.40 (n/a)</td><td>32.95 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (+7.70%)</td><td>0.03 (+1.38%)</td><td>0.03 (-5.84%)</td><td>0.02 (+3.30%)</td><td>0.00 (+14.66%)</td><td>166.60 (-3.14%)</td><td>147.30 (-1.19%)</td><td>148.30 (+6.16%)</td><td>126.00 (-7.15%)</td><td>16.32 (+3.61%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>172.00 (n/a)</td><td>149.08 (n/a)</td><td>139.70 (n/a)</td><td>135.70 (n/a)</td><td>15.75 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (-0.67%)</td><td>0.03 (-7.52%)</td><td>0.03 (-7.05%)</td><td>0.02 (-13.42%)</td><td>0.00 <b>(+25.35%)</b></td><td>197.50 (+15.50%)</td><td>162.02 (+9.15%)</td><td>156.50 (+7.56%)</td><td>126.50 (+0.64%)</td><td>26.12 <b>(+44.13%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.00 (n/a)</td><td>148.44 (n/a)</td><td>145.50 (n/a)</td><td>125.70 (n/a)</td><td>18.12 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.00 (+0.00%)</td><td>0.00 (+2.80%)</td><td>0.00 (+2.33%)</td><td>0.00 (+7.50%)</td><td>0.00 <b>(-48.01%)</b></td><td>963.25 (-6.68%)</td><td>934.26 (-3.23%)</td><td>922.09 (-4.16%)</td><td>917.13 (+1.12%)</td><td>20.57 <b>(-56.19%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1032.21 (n/a)</td><td>965.46 (n/a)</td><td>962.12 (n/a)</td><td>906.97 (n/a)</td><td>46.95 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.01 (-3.53%)</td><td>0.01 (-1.48%)</td><td>0.01 (+1.25%)</td><td>0.01 (-3.75%)</td><td>0.00 (-7.75%)</td><td>1060.86 (+3.15%)</td><td>1023.82 (+1.43%)</td><td>1015.55 (-0.34%)</td><td>994.87 (+3.19%)</td><td>24.62 (-4.35%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1028.46 (n/a)</td><td>1009.36 (n/a)</td><td>1019.04 (n/a)</td><td>964.09 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.97 (+0.25%)</td><td>0.95 (-1.10%)</td><td>0.94 (-1.58%)</td><td>0.93 (-2.48%)</td><td>0.02 <b>(+167.15%)</b></td><td>2256.91 (+2.53%)</td><td>2213.15 (+1.13%)</td><td>2228.31 (+1.60%)</td><td>2159.48 (-0.25%)</td><td>38.67 <b>(+172.97%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2201.13 (n/a)</td><td>2188.38 (n/a)</td><td>2193.32 (n/a)</td><td>2164.97 (n/a)</td><td>14.17 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>5.82 (-2.49%)</td><td>5.01 (-6.65%)</td><td>5.15 (-6.45%)</td><td>4.24 (-12.14%)</td><td>0.62 <b>(+29.58%)</b></td><td>247.10 (+13.82%)</td><td>211.90 (+7.76%)</td><td>203.70 (+6.87%)</td><td>180.20 (+2.50%)</td><td>26.66 <b>(+50.80%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>5.97 (n/a)</td><td>5.37 (n/a)</td><td>5.50 (n/a)</td><td>4.83 (n/a)</td><td>0.48 (n/a)</td><td>217.10 (n/a)</td><td>196.64 (n/a)</td><td>190.60 (n/a)</td><td>175.80 (n/a)</td><td>17.68 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>5.60 (-10.74%)</td><td>5.02 (+2.78%)</td><td>4.90 (+1.66%)</td><td>4.45 (+17.08%)</td><td>0.46 <b>(-48.29%)</b></td><td>235.70 (-14.57%)</td><td>210.48 (-4.50%)</td><td>214.00 (-1.65%)</td><td>187.20 (+12.03%)</td><td>19.24 <b>(-50.17%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>6.28 (n/a)</td><td>4.88 (n/a)</td><td>4.82 (n/a)</td><td>3.80 (n/a)</td><td>0.89 (n/a)</td><td>275.90 (n/a)</td><td>220.40 (n/a)</td><td>217.60 (n/a)</td><td>167.10 (n/a)</td><td>38.62 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>5.63 (+0.35%)</td><td>4.81 (-4.12%)</td><td>4.73 (-5.17%)</td><td>4.33 (-3.23%)</td><td>0.49 (+8.27%)</td><td>242.30 (+3.33%)</td><td>219.54 (+4.43%)</td><td>221.50 (+5.48%)</td><td>186.20 (-0.32%)</td><td>20.71 (+9.31%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>5.61 (n/a)</td><td>5.02 (n/a)</td><td>4.99 (n/a)</td><td>4.47 (n/a)</td><td>0.45 (n/a)</td><td>234.50 (n/a)</td><td>210.22 (n/a)</td><td>210.00 (n/a)</td><td>186.80 (n/a)</td><td>18.95 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.41 (+6.59%)</td><td>5.30 (+7.19%)</td><td>5.49 (+17.15%)</td><td>3.76 (-7.03%)</td><td>0.97 <b>(+25.74%)</b></td><td>279.00 (+7.56%)</td><td>204.24 (-5.53%)</td><td>190.90 (-14.66%)</td><td>163.60 (-6.19%)</td><td>43.93 <b>(+33.69%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>6.01 (n/a)</td><td>4.94 (n/a)</td><td>4.69 (n/a)</td><td>4.04 (n/a)</td><td>0.77 (n/a)</td><td>259.40 (n/a)</td><td>216.20 (n/a)</td><td>223.70 (n/a)</td><td>174.40 (n/a)</td><td>32.86 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>8.68 (-12.64%)</td><td>7.78 (-7.57%)</td><td>7.94 (-7.49%)</td><td>6.75 (+1.07%)</td><td>0.86 <b>(-27.08%)</b></td><td>310.50 (-1.05%)</td><td>272.14 (+7.47%)</td><td>264.10 (+8.10%)</td><td>241.50 (+14.45%)</td><td>30.72 (-18.94%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.94 (n/a)</td><td>8.42 (n/a)</td><td>8.59 (n/a)</td><td>6.68 (n/a)</td><td>1.18 (n/a)</td><td>313.80 (n/a)</td><td>253.22 (n/a)</td><td>244.30 (n/a)</td><td>211.00 (n/a)</td><td>37.90 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>8.51 (+8.08%)</td><td>7.89 (+12.99%)</td><td>8.19 <b>(+21.17%)</b></td><td>6.91 (+8.12%)</td><td>0.67 (+2.46%)</td><td>303.40 (-7.50%)</td><td>267.44 (-11.57%)</td><td>256.20 (-17.49%)</td><td>246.40 (-7.47%)</td><td>23.83 (-12.84%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>7.88 (n/a)</td><td>6.98 (n/a)</td><td>6.76 (n/a)</td><td>6.39 (n/a)</td><td>0.65 (n/a)</td><td>328.00 (n/a)</td><td>302.42 (n/a)</td><td>310.50 (n/a)</td><td>266.30 (n/a)</td><td>27.34 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>8.33 (-7.90%)</td><td>7.85 (+1.19%)</td><td>7.77 (+4.96%)</td><td>7.21 (+7.74%)</td><td>0.45 <b>(-59.58%)</b></td><td>291.00 (-7.18%)</td><td>267.88 (-2.50%)</td><td>269.90 (-4.70%)</td><td>251.70 (+8.58%)</td><td>15.69 <b>(-59.21%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.05 (n/a)</td><td>7.76 (n/a)</td><td>7.40 (n/a)</td><td>6.69 (n/a)</td><td>1.12 (n/a)</td><td>313.50 (n/a)</td><td>274.74 (n/a)</td><td>283.20 (n/a)</td><td>231.80 (n/a)</td><td>38.47 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>9.41 (-10.67%)</td><td>7.96 (-1.61%)</td><td>8.07 (+3.96%)</td><td>6.10 (-2.84%)</td><td>1.26 <b>(-21.05%)</b></td><td>343.90 (+2.93%)</td><td>269.14 (+0.89%)</td><td>259.80 (-3.81%)</td><td>222.90 (+11.95%)</td><td>46.60 (-6.44%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>10.53 (n/a)</td><td>8.09 (n/a)</td><td>7.76 (n/a)</td><td>6.28 (n/a)</td><td>1.59 (n/a)</td><td>334.10 (n/a)</td><td>266.76 (n/a)</td><td>270.10 (n/a)</td><td>199.10 (n/a)</td><td>49.81 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>9.38 (+9.33%)</td><td>7.94 (+2.48%)</td><td>7.98 (+1.48%)</td><td>6.88 (+2.45%)</td><td>0.99 <b>(+25.92%)</b></td><td>304.60 (-2.40%)</td><td>267.38 (-2.07%)</td><td>262.90 (-1.46%)</td><td>223.60 (-8.55%)</td><td>32.40 (+13.60%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>8.58 (n/a)</td><td>7.75 (n/a)</td><td>7.86 (n/a)</td><td>6.72 (n/a)</td><td>0.79 (n/a)</td><td>312.10 (n/a)</td><td>273.04 (n/a)</td><td>266.80 (n/a)</td><td>244.50 (n/a)</td><td>28.52 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>9.57 (-1.99%)</td><td>8.52 (-3.42%)</td><td>8.59 (-0.89%)</td><td>7.38 (-7.19%)</td><td>0.85 (+16.52%)</td><td>284.30 (+7.73%)</td><td>248.30 (+3.82%)</td><td>244.10 (+0.91%)</td><td>219.10 (+2.05%)</td><td>25.22 <b>(+28.87%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.77 (n/a)</td><td>8.82 (n/a)</td><td>8.67 (n/a)</td><td>7.95 (n/a)</td><td>0.73 (n/a)</td><td>263.90 (n/a)</td><td>239.16 (n/a)</td><td>241.90 (n/a)</td><td>214.70 (n/a)</td><td>19.57 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>12.74 (+1.87%)</td><td>11.13 (-2.56%)</td><td>10.57 (-5.50%)</td><td>10.43 (-5.75%)</td><td>1.00 <b>(+64.26%)</b></td><td>402.00 (+6.10%)</td><td>378.96 (+3.02%)</td><td>396.90 (+5.84%)</td><td>329.10 (-1.85%)</td><td>31.67 <b>(+73.35%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>12.51 (n/a)</td><td>11.43 (n/a)</td><td>11.18 (n/a)</td><td>11.07 (n/a)</td><td>0.61 (n/a)</td><td>378.90 (n/a)</td><td>367.84 (n/a)</td><td>375.00 (n/a)</td><td>335.30 (n/a)</td><td>18.27 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>13.21 (+4.27%)</td><td>12.25 (+5.93%)</td><td>12.37 (+10.05%)</td><td>10.91 (-0.28%)</td><td>0.86 (+13.38%)</td><td>384.50 (+0.29%)</td><td>343.92 (-5.53%)</td><td>339.20 (-9.13%)</td><td>317.40 (-4.11%)</td><td>25.24 (+9.57%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>12.67 (n/a)</td><td>11.56 (n/a)</td><td>11.24 (n/a)</td><td>10.94 (n/a)</td><td>0.76 (n/a)</td><td>383.40 (n/a)</td><td>364.04 (n/a)</td><td>373.30 (n/a)</td><td>331.00 (n/a)</td><td>23.04 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>13.12 (+1.30%)</td><td>11.51 (+1.84%)</td><td>10.93 (-3.55%)</td><td>10.93 (+13.60%)</td><td>0.95 <b>(-24.71%)</b></td><td>383.90 (-11.97%)</td><td>366.26 (-2.31%)</td><td>383.70 (+3.67%)</td><td>319.80 (-1.30%)</td><td>27.93 <b>(-34.47%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>12.95 (n/a)</td><td>11.30 (n/a)</td><td>11.33 (n/a)</td><td>9.62 (n/a)</td><td>1.26 (n/a)</td><td>436.10 (n/a)</td><td>374.92 (n/a)</td><td>370.10 (n/a)</td><td>324.00 (n/a)</td><td>42.62 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>14.89 (-11.81%)</td><td>13.10 (-1.56%)</td><td>13.19 (+5.90%)</td><td>11.20 (-8.90%)</td><td>1.39 <b>(-30.69%)</b></td><td>374.30 (+9.77%)</td><td>323.22 (+0.96%)</td><td>318.10 (-5.58%)</td><td>281.60 (+13.37%)</td><td>35.09 (-12.59%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>16.89 (n/a)</td><td>13.30 (n/a)</td><td>12.45 (n/a)</td><td>12.30 (n/a)</td><td>2.00 (n/a)</td><td>341.00 (n/a)</td><td>320.14 (n/a)</td><td>336.90 (n/a)</td><td>248.40 (n/a)</td><td>40.14 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>12.70 (-6.96%)</td><td>12.06 (-3.73%)</td><td>11.83 (-6.21%)</td><td>11.75 (+3.75%)</td><td>0.41 <b>(-60.11%)</b></td><td>357.00 (-3.62%)</td><td>348.04 (+3.40%)</td><td>354.70 (+6.61%)</td><td>330.20 (+7.49%)</td><td>11.58 <b>(-58.51%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>13.65 (n/a)</td><td>12.53 (n/a)</td><td>12.61 (n/a)</td><td>11.33 (n/a)</td><td>1.03 (n/a)</td><td>370.40 (n/a)</td><td>336.58 (n/a)</td><td>332.70 (n/a)</td><td>307.20 (n/a)</td><td>27.92 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>13.87 (-4.86%)</td><td>12.24 (-8.10%)</td><td>12.03 (-9.31%)</td><td>10.70 (-8.40%)</td><td>1.32 (+17.59%)</td><td>392.20 (+9.19%)</td><td>345.88 (+9.19%)</td><td>348.80 (+10.28%)</td><td>302.30 (+5.11%)</td><td>37.15 <b>(+33.99%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>14.58 (n/a)</td><td>13.32 (n/a)</td><td>13.26 (n/a)</td><td>11.68 (n/a)</td><td>1.12 (n/a)</td><td>359.20 (n/a)</td><td>316.78 (n/a)</td><td>316.30 (n/a)</td><td>287.60 (n/a)</td><td>27.73 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>14.30 (+4.10%)</td><td>12.80 (+2.10%)</td><td>12.94 (+3.43%)</td><td>11.38 (-0.39%)</td><td>1.08 <b>(+31.09%)</b></td><td>368.50 (+0.38%)</td><td>329.58 (-1.83%)</td><td>324.20 (-3.31%)</td><td>293.30 (-3.93%)</td><td>27.83 <b>(+26.67%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>13.74 (n/a)</td><td>12.54 (n/a)</td><td>12.51 (n/a)</td><td>11.43 (n/a)</td><td>0.82 (n/a)</td><td>367.10 (n/a)</td><td>335.72 (n/a)</td><td>335.30 (n/a)</td><td>305.30 (n/a)</td><td>21.97 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>12.71 (-14.64%)</td><td>12.11 (-2.05%)</td><td>12.06 (-3.87%)</td><td>11.30 <b>(+27.83%)</b></td><td>0.55 <b>(-75.23%)</b></td><td>371.20 <b>(-21.77%)</b></td><td>346.96 (-0.78%)</td><td>347.80 (+4.01%)</td><td>330.00 (+17.15%)</td><td>16.00 <b>(-78.20%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>14.89 (n/a)</td><td>12.36 (n/a)</td><td>12.54 (n/a)</td><td>8.84 (n/a)</td><td>2.21 (n/a)</td><td>474.50 (n/a)</td><td>349.70 (n/a)</td><td>334.40 (n/a)</td><td>281.70 (n/a)</td><td>73.42 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.14 (-11.96%)</td><td>2.87 (-2.51%)</td><td>2.91 (-1.89%)</td><td>2.37 (-0.43%)</td><td>0.30 <b>(-32.57%)</b></td><td>221.20 (+0.45%)</td><td>184.62 (+1.73%)</td><td>180.20 (+1.92%)</td><td>166.70 (+13.56%)</td><td>21.38 <b>(-21.55%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.57 (n/a)</td><td>2.94 (n/a)</td><td>2.97 (n/a)</td><td>2.38 (n/a)</td><td>0.44 (n/a)</td><td>220.20 (n/a)</td><td>181.48 (n/a)</td><td>176.80 (n/a)</td><td>146.80 (n/a)</td><td>27.25 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>5.80 (+0.98%)</td><td>4.48 (-4.71%)</td><td>4.44 (-2.53%)</td><td>3.25 (-15.66%)</td><td>0.92 <b>(+24.26%)</b></td><td>323.10 (+18.57%)</td><td>242.54 (+6.58%)</td><td>236.40 (+2.60%)</td><td>180.80 (-0.99%)</td><td>51.69 <b>(+48.47%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>5.74 (n/a)</td><td>4.70 (n/a)</td><td>4.55 (n/a)</td><td>3.85 (n/a)</td><td>0.74 (n/a)</td><td>272.50 (n/a)</td><td>227.56 (n/a)</td><td>230.40 (n/a)</td><td>182.60 (n/a)</td><td>34.82 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>8.79 (-9.20%)</td><td>7.49 (-3.87%)</td><td>7.36 (-1.75%)</td><td>6.23 (+1.70%)</td><td>1.01 <b>(-27.56%)</b></td><td>336.80 (-1.66%)</td><td>284.16 (+2.90%)</td><td>285.10 (+1.79%)</td><td>238.60 (+10.11%)</td><td>38.76 <b>(-21.27%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>9.68 (n/a)</td><td>7.79 (n/a)</td><td>7.49 (n/a)</td><td>6.12 (n/a)</td><td>1.40 (n/a)</td><td>342.50 (n/a)</td><td>276.14 (n/a)</td><td>280.10 (n/a)</td><td>216.70 (n/a)</td><td>49.23 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.40 (-1.14%)</td><td>2.51 (-18.92%)</td><td>2.52 <b>(-20.16%)</b></td><td>1.37 <b>(-48.96%)</b></td><td>0.74 <b>(+121.70%)</b></td><td>383.00 <b>(+95.91%)</b></td><td>229.26 <b>(+33.96%)</b></td><td>208.30 <b>(+25.26%)</b></td><td>154.30 (+1.11%)</td><td>89.00 <b>(+372.32%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>3.44 (n/a)</td><td>3.09 (n/a)</td><td>3.15 (n/a)</td><td>2.68 (n/a)</td><td>0.33 (n/a)</td><td>195.50 (n/a)</td><td>171.14 (n/a)</td><td>166.30 (n/a)</td><td>152.60 (n/a)</td><td>18.84 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 (-3.44%)</td><td>0.20 (+0.73%)</td><td>0.19 (-6.18%)</td><td>0.15 (+10.11%)</td><td>0.04 (-9.48%)</td><td>217.10 (-9.16%)</td><td>173.00 (-1.70%)</td><td>172.40 (+6.62%)</td><td>131.00 (+3.56%)</td><td>35.67 (-15.75%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>239.00 (n/a)</td><td>176.00 (n/a)</td><td>161.70 (n/a)</td><td>126.50 (n/a)</td><td>42.33 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.26 (+10.76%)</td><td>0.20 (-5.23%)</td><td>0.18 (-19.62%)</td><td>0.16 (-16.02%)</td><td>0.04 <b>(+130.77%)</b></td><td>202.10 (+19.09%)</td><td>167.84 (+8.42%)</td><td>183.80 <b>(+24.36%)</b></td><td>126.80 (-9.69%)</td><td>32.72 <b>(+141.41%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>169.70 (n/a)</td><td>154.80 (n/a)</td><td>147.80 (n/a)</td><td>140.40 (n/a)</td><td>13.55 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.49 (-6.85%)</td><td>0.42 (-6.56%)</td><td>0.44 (-12.02%)</td><td>0.34 (+0.82%)</td><td>0.06 <b>(-27.31%)</b></td><td>195.40 (-0.81%)</td><td>157.58 (+5.48%)</td><td>149.10 (+13.64%)</td><td>132.90 (+7.35%)</td><td>25.65 <b>(-21.11%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.53 (n/a)</td><td>0.45 (n/a)</td><td>0.50 (n/a)</td><td>0.33 (n/a)</td><td>0.09 (n/a)</td><td>197.00 (n/a)</td><td>149.40 (n/a)</td><td>131.20 (n/a)</td><td>123.80 (n/a)</td><td>32.51 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.50 (+1.57%)</td><td>0.43 (-0.36%)</td><td>0.40 (-2.22%)</td><td>0.39 (-1.35%)</td><td>0.05 <b>(+27.30%)</b></td><td>169.30 (+1.38%)</td><td>154.84 (+0.74%)</td><td>163.00 (+2.26%)</td><td>131.70 (-1.57%)</td><td>16.72 <b>(+29.26%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.49 (n/a)</td><td>0.43 (n/a)</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.04 (n/a)</td><td>167.00 (n/a)</td><td>153.70 (n/a)</td><td>159.40 (n/a)</td><td>133.80 (n/a)</td><td>12.94 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.53 (+15.31%)</td><td>0.41 (+4.81%)</td><td>0.36 (-6.64%)</td><td>0.34 (+8.83%)</td><td>0.08 <b>(+36.17%)</b></td><td>194.20 (-8.14%)</td><td>165.70 (-3.66%)</td><td>181.40 (+7.08%)</td><td>124.40 (-13.31%)</td><td>30.40 (+9.97%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.46 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.06 (n/a)</td><td>211.40 (n/a)</td><td>172.00 (n/a)</td><td>169.40 (n/a)</td><td>143.50 (n/a)</td><td>27.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.98 (-7.13%)</td><td>0.72 (-13.64%)</td><td>0.76 (-3.11%)</td><td>0.34 <b>(-51.88%)</b></td><td>0.27 <b>(+93.43%)</b></td><td>390.20 <b>(+107.77%)</b></td><td>211.40 <b>(+32.42%)</b></td><td>172.50 (+3.23%)</td><td>134.40 (+7.69%)</td><td>106.30 <b>(+331.29%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.05 (n/a)</td><td>0.84 (n/a)</td><td>0.78 (n/a)</td><td>0.70 (n/a)</td><td>0.14 (n/a)</td><td>187.80 (n/a)</td><td>159.64 (n/a)</td><td>167.10 (n/a)</td><td>124.80 (n/a)</td><td>24.65 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.90 (-12.23%)</td><td>0.81 (-7.65%)</td><td>0.87 (-4.89%)</td><td>0.67 (-2.40%)</td><td>0.10 (-18.31%)</td><td>196.90 (+2.45%)</td><td>163.36 (+7.80%)</td><td>150.70 (+5.16%)</td><td>145.60 (+13.93%)</td><td>22.22 (-8.37%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>1.03 (n/a)</td><td>0.88 (n/a)</td><td>0.91 (n/a)</td><td>0.68 (n/a)</td><td>0.13 (n/a)</td><td>192.20 (n/a)</td><td>151.54 (n/a)</td><td>143.30 (n/a)</td><td>127.80 (n/a)</td><td>24.25 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.87 (-3.30%)</td><td>0.78 (-4.86%)</td><td>0.78 (-3.78%)</td><td>0.67 (-11.56%)</td><td>0.07 <b>(+21.21%)</b></td><td>195.50 (+13.07%)</td><td>170.22 (+5.40%)</td><td>167.50 (+3.91%)</td><td>151.30 (+3.42%)</td><td>15.94 <b>(+42.28%)</b></td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.90 (n/a)</td><td>0.81 (n/a)</td><td>0.81 (n/a)</td><td>0.76 (n/a)</td><td>0.06 (n/a)</td><td>172.90 (n/a)</td><td>161.50 (n/a)</td><td>161.20 (n/a)</td><td>146.30 (n/a)</td><td>11.21 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.01 (+18.43%)</td><td>0.86 (+13.27%)</td><td>0.86 (+11.18%)</td><td>0.72 (+12.24%)</td><td>0.10 <b>(+34.04%)</b></td><td>182.40 (-10.89%)</td><td>153.52 (-11.46%)</td><td>152.80 (-10.06%)</td><td>130.20 (-15.51%)</td><td>18.75 (-0.52%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.85 (n/a)</td><td>0.76 (n/a)</td><td>0.77 (n/a)</td><td>0.64 (n/a)</td><td>0.08 (n/a)</td><td>204.70 (n/a)</td><td>173.40 (n/a)</td><td>169.90 (n/a)</td><td>154.10 (n/a)</td><td>18.84 (n/a)</td>
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
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (-3.14%)</td><td>0.10 (-6.59%)</td><td>0.09 <b>(-24.34%)</b></td><td>0.08 (+3.60%)</td><td>0.03 (+10.16%)</td><td>203.60 (-3.46%)</td><td>169.82 (+7.97%)</td><td>190.80 <b>(+32.13%)</b></td><td>125.50 (+3.29%)</td><td>40.56 (+8.46%)</td>
</tr>
<tr>
<td><code>d603ab9</code> — 2026-09-18 19:48:20</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.90 (n/a)</td><td>157.28 (n/a)</td><td>144.40 (n/a)</td><td>121.50 (n/a)</td><td>37.39 (n/a)</td>
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
