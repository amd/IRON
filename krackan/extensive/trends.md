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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (-7.41%)</td><td>0.04 (-15.95%)</td><td>0.04 <b>(-20.50%)</b></td><td>0.03 (-18.15%)</td><td>0.01 <b>(+20.67%)</b></td><td>198.60 <b>(+22.22%)</b></td><td>164.12 <b>(+20.46%)</b></td><td>159.60 <b>(+25.77%)</b></td><td>129.70 (+7.99%)</td><td>29.05 <b>(+61.45%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>162.50 (n/a)</td><td>136.24 (n/a)</td><td>126.90 (n/a)</td><td>120.10 (n/a)</td><td>17.99 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 <b>(+25.27%)</b></td><td>0.04 (+3.42%)</td><td>0.04 (-7.01%)</td><td>0.03 (-0.26%)</td><td>0.01 <b>(+126.55%)</b></td><td>183.60 (+0.27%)</td><td>162.52 (-1.76%)</td><td>169.50 (+7.55%)</td><td>122.60 <b>(-20.18%)</b></td><td>24.39 <b>(+78.52%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>183.10 (n/a)</td><td>165.44 (n/a)</td><td>157.60 (n/a)</td><td>153.60 (n/a)</td><td>13.66 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (-10.38%)</td><td>0.04 (+1.43%)</td><td>0.04 (-7.37%)</td><td>0.03 <b>(+37.09%)</b></td><td>0.00 <b>(-50.14%)</b></td><td>184.30 <b>(-27.04%)</b></td><td>163.02 (-5.67%)</td><td>169.80 (+8.02%)</td><td>138.50 (+11.60%)</td><td>19.02 <b>(-61.03%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.60 (n/a)</td><td>172.82 (n/a)</td><td>157.20 (n/a)</td><td>124.10 (n/a)</td><td>48.81 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 <b>(-27.56%)</b></td><td>0.03 <b>(-21.25%)</b></td><td>0.03 <b>(-21.15%)</b></td><td>0.03 <b>(-20.68%)</b></td><td>0.00 <b>(-47.18%)</b></td><td>232.70 <b>(+26.06%)</b></td><td>200.48 <b>(+25.90%)</b></td><td>196.40 <b>(+26.87%)</b></td><td>175.70 <b>(+38.02%)</b></td><td>20.85 (-7.31%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>184.60 (n/a)</td><td>159.24 (n/a)</td><td>154.80 (n/a)</td><td>127.30 (n/a)</td><td>22.50 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (-15.60%)</td><td>0.03 (-18.59%)</td><td>0.03 <b>(-25.16%)</b></td><td>0.03 (+9.39%)</td><td>0.01 <b>(-42.48%)</b></td><td>204.50 (-8.58%)</td><td>179.76 (+19.20%)</td><td>182.20 <b>(+33.58%)</b></td><td>145.00 (+18.46%)</td><td>24.75 <b>(-40.09%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>150.80 (n/a)</td><td>136.40 (n/a)</td><td>122.40 (n/a)</td><td>41.31 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (+0.28%)</td><td>0.04 (-12.26%)</td><td>0.03 (-5.98%)</td><td>0.03 (-13.13%)</td><td>0.01 (+8.06%)</td><td>211.10 (+15.10%)</td><td>180.78 (+14.85%)</td><td>184.20 (+6.35%)</td><td>125.00 (-0.32%)</td><td>33.37 <b>(+21.29%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>183.40 (n/a)</td><td>157.40 (n/a)</td><td>173.20 (n/a)</td><td>125.40 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (-18.73%)</td><td>0.03 <b>(-24.28%)</b></td><td>0.03 <b>(-24.46%)</b></td><td>0.02 <b>(-32.67%)</b></td><td>0.01 (+4.72%)</td><td>275.50 <b>(+48.52%)</b></td><td>206.58 <b>(+34.58%)</b></td><td>183.40 <b>(+32.42%)</b></td><td>164.70 <b>(+23.00%)</b></td><td>46.99 <b>(+93.19%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.50 (n/a)</td><td>153.50 (n/a)</td><td>138.50 (n/a)</td><td>133.90 (n/a)</td><td>24.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (+0.68%)</td><td>0.03 (-14.52%)</td><td>0.03 (-14.45%)</td><td>0.02 <b>(-31.79%)</b></td><td>0.01 <b>(+50.82%)</b></td><td>268.60 <b>(+46.62%)</b></td><td>201.60 <b>(+22.87%)</b></td><td>205.30 (+16.91%)</td><td>120.00 (-0.66%)</td><td>54.83 <b>(+111.98%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>183.20 (n/a)</td><td>164.08 (n/a)</td><td>175.60 (n/a)</td><td>120.80 (n/a)</td><td>25.87 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.08 (-15.32%)</td><td>0.07 (-15.57%)</td><td>0.07 (-17.09%)</td><td>0.05 (-19.71%)</td><td>0.01 (-4.15%)</td><td>244.40 <b>(+24.57%)</b></td><td>181.06 (+19.28%)</td><td>168.90 <b>(+20.64%)</b></td><td>155.40 (+18.09%)</td><td>36.82 <b>(+40.41%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>196.20 (n/a)</td><td>151.80 (n/a)</td><td>140.00 (n/a)</td><td>131.60 (n/a)</td><td>26.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 <b>(-40.80%)</b></td><td>0.06 <b>(-35.81%)</b></td><td>0.06 <b>(-31.53%)</b></td><td>0.05 (-16.65%)</td><td>0.01 <b>(-66.94%)</b></td><td>252.10 (+19.93%)</td><td>212.24 <b>(+49.17%)</b></td><td>198.40 <b>(+46.10%)</b></td><td>183.80 <b>(+68.93%)</b></td><td>27.81 <b>(-32.33%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>210.20 (n/a)</td><td>142.28 (n/a)</td><td>135.80 (n/a)</td><td>108.80 (n/a)</td><td>41.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (-6.35%)</td><td>0.07 (-1.09%)</td><td>0.07 (-13.38%)</td><td>0.07 <b>(+32.68%)</b></td><td>0.01 <b>(-47.97%)</b></td><td>187.50 <b>(-24.61%)</b></td><td>167.44 (-3.77%)</td><td>177.20 (+15.44%)</td><td>134.00 (+6.77%)</td><td>20.97 <b>(-59.00%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>248.70 (n/a)</td><td>174.00 (n/a)</td><td>153.50 (n/a)</td><td>125.50 (n/a)</td><td>51.14 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.08 <b>(-23.04%)</b></td><td>0.07 (-14.99%)</td><td>0.07 (-10.38%)</td><td>0.05 <b>(-22.14%)</b></td><td>0.01 <b>(-24.47%)</b></td><td>230.60 <b>(+28.47%)</b></td><td>185.32 (+17.62%)</td><td>181.70 (+11.54%)</td><td>161.60 <b>(+29.90%)</b></td><td>27.08 <b>(+31.93%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>179.50 (n/a)</td><td>157.56 (n/a)</td><td>162.90 (n/a)</td><td>124.40 (n/a)</td><td>20.52 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (+12.13%)</td><td>0.07 (+7.31%)</td><td>0.06 (+2.36%)</td><td>0.06 <b>(+20.37%)</b></td><td>0.02 (+15.48%)</td><td>205.50 (-16.94%)</td><td>181.52 (-6.70%)</td><td>196.50 (-2.29%)</td><td>112.80 (-10.83%)</td><td>38.80 (-13.13%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>247.40 (n/a)</td><td>194.56 (n/a)</td><td>201.10 (n/a)</td><td>126.50 (n/a)</td><td>44.66 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (+18.73%)</td><td>0.08 (-4.64%)</td><td>0.07 (-8.50%)</td><td>0.05 <b>(-25.84%)</b></td><td>0.03 <b>(+78.87%)</b></td><td>250.00 <b>(+34.84%)</b></td><td>177.12 (+11.58%)</td><td>181.20 (+9.29%)</td><td>100.80 (-15.72%)</td><td>54.50 <b>(+91.88%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>185.40 (n/a)</td><td>158.74 (n/a)</td><td>165.80 (n/a)</td><td>119.60 (n/a)</td><td>28.41 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (+0.89%)</td><td>0.06 (+3.97%)</td><td>0.06 (-0.24%)</td><td>0.05 (+11.13%)</td><td>0.02 (-5.89%)</td><td>232.00 (-10.01%)</td><td>202.50 (-4.71%)</td><td>217.70 (+0.23%)</td><td>133.50 (-0.89%)</td><td>40.80 (-13.77%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>257.80 (n/a)</td><td>212.52 (n/a)</td><td>217.20 (n/a)</td><td>134.70 (n/a)</td><td>47.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (-8.90%)</td><td>0.06 (-13.67%)</td><td>0.05 (-6.72%)</td><td>0.05 (-6.18%)</td><td>0.02 (-14.43%)</td><td>230.40 (+6.62%)</td><td>208.46 (+14.60%)</td><td>227.70 (+7.20%)</td><td>130.40 (+9.76%)</td><td>43.69 (-4.86%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>216.10 (n/a)</td><td>181.90 (n/a)</td><td>212.40 (n/a)</td><td>118.80 (n/a)</td><td>45.92 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 <b>(-25.16%)</b></td><td>0.13 (-2.94%)</td><td>0.13 (+1.91%)</td><td>0.12 <b>(+32.18%)</b></td><td>0.01 <b>(-81.32%)</b></td><td>196.70 <b>(-24.32%)</b></td><td>184.12 (-2.92%)</td><td>183.80 (-1.87%)</td><td>173.60 <b>(+33.64%)</b></td><td>9.88 <b>(-81.08%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>259.90 (n/a)</td><td>189.66 (n/a)</td><td>187.30 (n/a)</td><td>129.90 (n/a)</td><td>52.23 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 (+16.65%)</td><td>0.16 (+10.70%)</td><td>0.14 (-8.94%)</td><td>0.13 <b>(+33.58%)</b></td><td>0.03 (-5.96%)</td><td>191.30 <b>(-25.13%)</b></td><td>160.02 (-11.43%)</td><td>169.70 (+9.84%)</td><td>122.70 (-14.26%)</td><td>27.83 <b>(-40.40%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>255.50 (n/a)</td><td>180.68 (n/a)</td><td>154.50 (n/a)</td><td>143.10 (n/a)</td><td>46.69 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 <b>(-24.83%)</b></td><td>0.13 (-13.87%)</td><td>0.13 (-18.41%)</td><td>0.11 <b>(+21.09%)</b></td><td>0.02 <b>(-63.11%)</b></td><td>230.10 (-17.44%)</td><td>186.26 (+6.91%)</td><td>182.40 <b>(+22.58%)</b></td><td>156.00 <b>(+32.99%)</b></td><td>27.17 <b>(-58.82%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>278.70 (n/a)</td><td>174.22 (n/a)</td><td>148.80 (n/a)</td><td>117.30 (n/a)</td><td>65.97 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 <b>(-20.30%)</b></td><td>0.13 (-17.68%)</td><td>0.13 <b>(-22.20%)</b></td><td>0.11 (+7.26%)</td><td>0.01 <b>(-53.72%)</b></td><td>220.90 (-6.75%)</td><td>195.92 (+18.01%)</td><td>191.40 <b>(+28.54%)</b></td><td>173.40 <b>(+25.47%)</b></td><td>21.72 <b>(-46.80%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>236.90 (n/a)</td><td>166.02 (n/a)</td><td>148.90 (n/a)</td><td>138.20 (n/a)</td><td>40.83 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (-13.37%)</td><td>0.13 (-16.07%)</td><td>0.14 (-16.51%)</td><td>0.10 (+2.85%)</td><td>0.02 <b>(-37.16%)</b></td><td>250.60 (-2.79%)</td><td>189.42 (+15.11%)</td><td>177.80 (+19.81%)</td><td>150.30 (+15.44%)</td><td>37.44 <b>(-29.54%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>257.80 (n/a)</td><td>164.56 (n/a)</td><td>148.40 (n/a)</td><td>130.20 (n/a)</td><td>53.14 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.22 (+15.13%)</td><td>0.14 (-17.44%)</td><td>0.13 <b>(-29.19%)</b></td><td>0.09 <b>(-36.14%)</b></td><td>0.05 <b>(+106.71%)</b></td><td>281.90 <b>(+56.61%)</b></td><td>187.66 <b>(+30.48%)</b></td><td>189.40 <b>(+41.24%)</b></td><td>110.10 (-13.10%)</td><td>62.38 <b>(+178.49%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>180.00 (n/a)</td><td>143.82 (n/a)</td><td>134.10 (n/a)</td><td>126.70 (n/a)</td><td>22.40 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.17 (+1.66%)</td><td>0.12 (-17.23%)</td><td>0.11 <b>(-27.77%)</b></td><td>0.07 <b>(-37.11%)</b></td><td>0.04 <b>(+91.28%)</b></td><td>352.60 <b>(+58.97%)</b></td><td>223.66 <b>(+30.35%)</b></td><td>222.40 <b>(+38.48%)</b></td><td>148.00 (-1.66%)</td><td>81.36 <b>(+184.46%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>221.80 (n/a)</td><td>171.58 (n/a)</td><td>160.60 (n/a)</td><td>150.50 (n/a)</td><td>28.60 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (+3.26%)</td><td>0.12 <b>(-23.09%)</b></td><td>0.11 <b>(-28.42%)</b></td><td>0.08 <b>(-34.79%)</b></td><td>0.04 <b>(+66.54%)</b></td><td>309.90 <b>(+53.34%)</b></td><td>218.28 <b>(+37.98%)</b></td><td>219.30 <b>(+39.68%)</b></td><td>126.80 (-3.13%)</td><td>64.76 <b>(+133.90%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>202.10 (n/a)</td><td>158.20 (n/a)</td><td>157.00 (n/a)</td><td>130.90 (n/a)</td><td>27.69 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.29 <b>(-24.50%)</b></td><td>0.26 (-19.03%)</td><td>0.27 (-14.90%)</td><td>0.23 (-15.26%)</td><td>0.02 <b>(-52.18%)</b></td><td>216.30 (+18.00%)</td><td>186.94 <b>(+22.09%)</b></td><td>181.10 (+17.52%)</td><td>170.80 <b>(+32.51%)</b></td><td>17.89 <b>(-23.00%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.38 (n/a)</td><td>0.33 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>183.30 (n/a)</td><td>153.12 (n/a)</td><td>154.10 (n/a)</td><td>128.90 (n/a)</td><td>23.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.30 <b>(-27.84%)</b></td><td>0.27 <b>(-27.01%)</b></td><td>0.28 <b>(-25.52%)</b></td><td>0.24 (-19.29%)</td><td>0.03 <b>(-48.29%)</b></td><td>208.90 <b>(+23.90%)</b></td><td>182.46 <b>(+35.82%)</b></td><td>175.70 <b>(+34.22%)</b></td><td>163.10 <b>(+38.57%)</b></td><td>17.71 (-12.20%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.42 (n/a)</td><td>0.37 (n/a)</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.05 (n/a)</td><td>168.60 (n/a)</td><td>134.34 (n/a)</td><td>130.90 (n/a)</td><td>117.70 (n/a)</td><td>20.17 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.31 (-19.88%)</td><td>0.28 (-10.05%)</td><td>0.30 (-3.01%)</td><td>0.22 <b>(-20.72%)</b></td><td>0.04 (-14.05%)</td><td>223.30 <b>(+26.09%)</b></td><td>175.86 (+11.46%)</td><td>165.30 (+3.12%)</td><td>160.10 <b>(+24.79%)</b></td><td>26.70 <b>(+38.34%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.38 (n/a)</td><td>0.32 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.04 (n/a)</td><td>177.10 (n/a)</td><td>157.78 (n/a)</td><td>160.30 (n/a)</td><td>128.30 (n/a)</td><td>19.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.33 <b>(-20.23%)</b></td><td>0.29 (-14.12%)</td><td>0.29 <b>(-23.07%)</b></td><td>0.26 (+11.46%)</td><td>0.03 <b>(-64.53%)</b></td><td>188.50 (-10.28%)</td><td>172.08 (+11.13%)</td><td>172.40 <b>(+29.92%)</b></td><td>149.20 <b>(+25.27%)</b></td><td>17.01 <b>(-59.28%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.37 (n/a)</td><td>0.23 (n/a)</td><td>0.08 (n/a)</td><td>210.10 (n/a)</td><td>154.84 (n/a)</td><td>132.70 (n/a)</td><td>119.10 (n/a)</td><td>41.78 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.30 (-2.96%)</td><td>0.23 (-7.34%)</td><td>0.26 (+9.73%)</td><td>0.13 <b>(-32.17%)</b></td><td>0.07 <b>(+59.49%)</b></td><td>383.30 <b>(+47.42%)</b></td><td>237.08 (+15.86%)</td><td>187.90 (-8.87%)</td><td>163.00 (+3.03%)</td><td>90.73 <b>(+144.91%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>260.00 (n/a)</td><td>204.62 (n/a)</td><td>206.20 (n/a)</td><td>158.20 (n/a)</td><td>37.05 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.35 (-15.03%)</td><td>0.28 (-14.20%)</td><td>0.27 (-17.68%)</td><td>0.22 (+16.90%)</td><td>0.05 <b>(-40.67%)</b></td><td>226.50 (-14.46%)</td><td>183.02 (+10.77%)</td><td>184.20 <b>(+21.42%)</b></td><td>141.00 (+17.70%)</td><td>34.18 <b>(-41.66%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.41 (n/a)</td><td>0.32 (n/a)</td><td>0.32 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>264.80 (n/a)</td><td>165.22 (n/a)</td><td>151.70 (n/a)</td><td>119.80 (n/a)</td><td>58.59 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.27 (-13.48%)</td><td>0.25 (-6.50%)</td><td>0.24 (-11.34%)</td><td>0.23 (+13.10%)</td><td>0.01 <b>(-62.63%)</b></td><td>210.50 (-11.59%)</td><td>200.12 (+5.18%)</td><td>205.40 (+12.80%)</td><td>181.40 (+15.54%)</td><td>11.44 <b>(-62.65%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>238.10 (n/a)</td><td>190.26 (n/a)</td><td>182.10 (n/a)</td><td>157.00 (n/a)</td><td>30.63 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.28 <b>(-27.80%)</b></td><td>0.22 <b>(-29.09%)</b></td><td>0.21 <b>(-32.57%)</b></td><td>0.18 <b>(-31.34%)</b></td><td>0.04 <b>(-26.39%)</b></td><td>277.00 <b>(+45.64%)</b></td><td>228.60 <b>(+41.22%)</b></td><td>232.40 <b>(+48.31%)</b></td><td>172.60 <b>(+38.52%)</b></td><td>38.85 <b>(+43.27%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>190.20 (n/a)</td><td>161.88 (n/a)</td><td>156.70 (n/a)</td><td>124.60 (n/a)</td><td>27.12 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (+13.14%)</td><td>0.02 (-4.97%)</td><td>0.02 (-6.19%)</td><td>0.01 (-11.67%)</td><td>0.00 <b>(+43.06%)</b></td><td>239.40 (+13.19%)</td><td>173.62 (+7.61%)</td><td>167.40 (+6.62%)</td><td>121.50 (-11.64%)</td><td>42.22 <b>(+42.03%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>211.50 (n/a)</td><td>161.34 (n/a)</td><td>157.00 (n/a)</td><td>137.50 (n/a)</td><td>29.73 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (-6.81%)</td><td>0.02 (-4.94%)</td><td>0.01 (-5.68%)</td><td>0.01 (-13.65%)</td><td>0.00 (+7.08%)</td><td>212.50 (+15.80%)</td><td>171.78 (+6.30%)</td><td>176.70 (+6.00%)</td><td>128.30 (+7.36%)</td><td>33.90 <b>(+36.34%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>183.50 (n/a)</td><td>161.60 (n/a)</td><td>166.70 (n/a)</td><td>119.50 (n/a)</td><td>24.86 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (+7.20%)</td><td>0.02 (-8.84%)</td><td>0.02 <b>(-24.34%)</b></td><td>0.01 (+0.08%)</td><td>0.00 (+16.32%)</td><td>192.70 (-0.05%)</td><td>161.94 (+10.31%)</td><td>173.90 <b>(+32.24%)</b></td><td>118.70 (-6.76%)</td><td>29.12 (+6.37%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>192.80 (n/a)</td><td>146.80 (n/a)</td><td>131.50 (n/a)</td><td>127.30 (n/a)</td><td>27.37 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (-7.60%)</td><td>0.02 (+6.63%)</td><td>0.01 (+7.96%)</td><td>0.01 (+10.67%)</td><td>0.00 (-14.02%)</td><td>219.40 (-9.64%)</td><td>174.52 (-7.48%)</td><td>177.50 (-7.36%)</td><td>129.40 (+8.19%)</td><td>39.90 (-13.12%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>242.80 (n/a)</td><td>188.62 (n/a)</td><td>191.60 (n/a)</td><td>119.60 (n/a)</td><td>45.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (-11.49%)</td><td>0.02 (-3.46%)</td><td>0.02 (+8.66%)</td><td>0.01 <b>(-21.48%)</b></td><td>0.00 (+12.31%)</td><td>256.90 <b>(+27.37%)</b></td><td>179.96 (+6.26%)</td><td>153.20 (-7.99%)</td><td>137.40 (+12.99%)</td><td>51.03 <b>(+61.73%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>201.70 (n/a)</td><td>169.36 (n/a)</td><td>166.50 (n/a)</td><td>121.60 (n/a)</td><td>31.55 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (+0.65%)</td><td>0.01 (-0.72%)</td><td>0.01 (+9.42%)</td><td>0.01 (-14.86%)</td><td>0.00 <b>(+32.40%)</b></td><td>235.00 (+17.50%)</td><td>184.86 (+2.75%)</td><td>176.10 (-8.61%)</td><td>138.40 (-0.65%)</td><td>40.62 <b>(+55.72%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>200.00 (n/a)</td><td>179.92 (n/a)</td><td>192.70 (n/a)</td><td>139.30 (n/a)</td><td>26.08 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (-18.87%)</td><td>0.01 (-1.47%)</td><td>0.01 (+3.02%)</td><td>0.01 (+8.40%)</td><td>0.00 <b>(-56.00%)</b></td><td>206.40 (-7.77%)</td><td>189.70 (-1.37%)</td><td>197.00 (-2.96%)</td><td>159.60 <b>(+23.24%)</b></td><td>18.97 <b>(-47.75%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>223.80 (n/a)</td><td>192.34 (n/a)</td><td>203.00 (n/a)</td><td>129.50 (n/a)</td><td>36.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.01 (+19.18%)</td><td>0.01 (+7.68%)</td><td>0.01 (+10.53%)</td><td>0.01 (-4.59%)</td><td>0.00 <b>(+103.80%)</b></td><td>253.60 (+4.79%)</td><td>214.36 (-6.24%)</td><td>213.20 (-9.51%)</td><td>176.20 (-16.10%)</td><td>27.41 <b>(+77.48%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>242.00 (n/a)</td><td>228.62 (n/a)</td><td>235.60 (n/a)</td><td>210.00 (n/a)</td><td>15.44 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 <b>(+33.03%)</b></td><td>0.03 (+8.68%)</td><td>0.03 (-5.66%)</td><td>0.03 <b>(+26.58%)</b></td><td>0.01 <b>(+50.14%)</b></td><td>192.60 <b>(-21.00%)</b></td><td>174.32 (-7.47%)</td><td>188.60 (+5.96%)</td><td>128.20 <b>(-24.81%)</b></td><td>27.32 (-12.47%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>243.80 (n/a)</td><td>188.40 (n/a)</td><td>178.00 (n/a)</td><td>170.50 (n/a)</td><td>31.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 <b>(+25.67%)</b></td><td>0.03 (+1.39%)</td><td>0.03 (-2.37%)</td><td>0.02 <b>(-32.78%)</b></td><td>0.01 <b>(+441.99%)</b></td><td>271.60 <b>(+48.82%)</b></td><td>179.22 (+7.06%)</td><td>172.80 (+2.43%)</td><td>125.20 <b>(-20.46%)</b></td><td>60.69 <b>(+514.12%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>182.50 (n/a)</td><td>167.40 (n/a)</td><td>168.70 (n/a)</td><td>157.40 (n/a)</td><td>9.88 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (+1.84%)</td><td>0.03 (-4.13%)</td><td>0.03 (-10.65%)</td><td>0.02 <b>(-31.43%)</b></td><td>0.01 <b>(+62.73%)</b></td><td>300.10 <b>(+45.82%)</b></td><td>194.64 (+11.63%)</td><td>199.70 (+11.94%)</td><td>127.50 (-1.77%)</td><td>69.12 <b>(+125.40%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>174.36 (n/a)</td><td>178.40 (n/a)</td><td>129.80 (n/a)</td><td>30.66 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (+17.53%)</td><td>0.03 (+11.57%)</td><td>0.03 (+6.20%)</td><td>0.02 (-0.74%)</td><td>0.01 <b>(+93.46%)</b></td><td>213.80 (+0.75%)</td><td>162.14 (-8.54%)</td><td>163.00 (-5.83%)</td><td>133.40 (-14.87%)</td><td>32.81 <b>(+58.27%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.20 (n/a)</td><td>177.28 (n/a)</td><td>173.10 (n/a)</td><td>156.70 (n/a)</td><td>20.73 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (+8.72%)</td><td>0.03 (-0.56%)</td><td>0.03 (-1.33%)</td><td>0.02 (-11.49%)</td><td>0.01 <b>(+68.88%)</b></td><td>218.90 (+13.01%)</td><td>172.06 (+3.99%)</td><td>164.00 (+1.36%)</td><td>126.10 (-8.02%)</td><td>43.06 <b>(+78.29%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>193.70 (n/a)</td><td>165.46 (n/a)</td><td>161.80 (n/a)</td><td>137.10 (n/a)</td><td>24.15 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-14.84%)</td><td>0.03 (-8.38%)</td><td>0.03 (-6.87%)</td><td>0.02 (-6.81%)</td><td>0.00 <b>(-22.59%)</b></td><td>218.70 (+7.31%)</td><td>173.06 (+8.60%)</td><td>159.80 (+7.39%)</td><td>156.30 (+17.43%)</td><td>26.15 (-3.57%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>203.80 (n/a)</td><td>159.36 (n/a)</td><td>148.80 (n/a)</td><td>133.10 (n/a)</td><td>27.12 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 <b>(+28.41%)</b></td><td>0.03 (+12.56%)</td><td>0.03 (+0.26%)</td><td>0.03 <b>(+25.84%)</b></td><td>0.01 <b>(+36.87%)</b></td><td>198.80 <b>(-20.54%)</b></td><td>168.26 (-10.87%)</td><td>172.70 (-0.29%)</td><td>119.20 <b>(-22.14%)</b></td><td>31.16 (-18.43%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>250.20 (n/a)</td><td>188.78 (n/a)</td><td>173.20 (n/a)</td><td>153.10 (n/a)</td><td>38.21 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-14.24%)</td><td>0.03 (+1.88%)</td><td>0.03 (+7.96%)</td><td>0.02 (+6.81%)</td><td>0.00 <b>(-51.58%)</b></td><td>221.80 (-6.37%)</td><td>190.64 (-3.93%)</td><td>189.00 (-7.35%)</td><td>168.60 (+16.60%)</td><td>19.44 <b>(-45.41%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.90 (n/a)</td><td>198.44 (n/a)</td><td>204.00 (n/a)</td><td>144.60 (n/a)</td><td>35.61 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (+14.51%)</td><td>0.07 <b>(+20.86%)</b></td><td>0.07 (+15.81%)</td><td>0.05 <b>(+79.44%)</b></td><td>0.02 (-9.96%)</td><td>224.50 <b>(-44.28%)</b></td><td>159.16 <b>(-24.25%)</b></td><td>149.90 (-13.65%)</td><td>122.10 (-12.66%)</td><td>42.56 <b>(-60.83%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>402.90 (n/a)</td><td>210.12 (n/a)</td><td>173.60 (n/a)</td><td>139.80 (n/a)</td><td>108.66 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 <b>(+24.97%)</b></td><td>0.07 (+18.21%)</td><td>0.06 (+2.53%)</td><td>0.06 <b>(+34.32%)</b></td><td>0.01 (+9.97%)</td><td>176.00 <b>(-25.55%)</b></td><td>159.04 (-16.15%)</td><td>169.90 (-2.52%)</td><td>119.40 (-19.97%)</td><td>23.19 <b>(-36.84%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>236.40 (n/a)</td><td>189.68 (n/a)</td><td>174.30 (n/a)</td><td>149.20 (n/a)</td><td>36.73 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 <b>(+27.49%)</b></td><td>0.07 (+18.05%)</td><td>0.07 (+15.39%)</td><td>0.06 (+8.49%)</td><td>0.01 <b>(+72.90%)</b></td><td>188.60 (-7.82%)</td><td>152.74 (-14.31%)</td><td>150.30 (-13.32%)</td><td>119.40 <b>(-21.55%)</b></td><td>25.06 <b>(+23.95%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>178.24 (n/a)</td><td>173.40 (n/a)</td><td>152.20 (n/a)</td><td>20.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (-4.27%)</td><td>0.06 (+1.94%)</td><td>0.06 (+15.85%)</td><td>0.04 (-11.88%)</td><td>0.01 (+6.70%)</td><td>260.20 (+13.48%)</td><td>183.86 (-0.77%)</td><td>169.30 (-13.71%)</td><td>146.40 (+4.50%)</td><td>46.52 <b>(+28.39%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.30 (n/a)</td><td>185.28 (n/a)</td><td>196.20 (n/a)</td><td>140.10 (n/a)</td><td>36.23 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 <b>(+22.75%)</b></td><td>0.07 (+15.02%)</td><td>0.07 (-1.99%)</td><td>0.05 <b>(+47.51%)</b></td><td>0.02 (-3.05%)</td><td>211.40 <b>(-32.20%)</b></td><td>154.70 (-16.65%)</td><td>154.00 (+1.99%)</td><td>114.50 (-18.56%)</td><td>37.20 <b>(-48.19%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>311.80 (n/a)</td><td>185.60 (n/a)</td><td>151.00 (n/a)</td><td>140.60 (n/a)</td><td>71.80 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.08 (+10.14%)</td><td>0.07 (+14.89%)</td><td>0.07 (+16.02%)</td><td>0.06 <b>(+21.12%)</b></td><td>0.01 (-3.61%)</td><td>179.10 (-17.43%)</td><td>156.80 (-13.36%)</td><td>151.00 (-13.81%)</td><td>133.60 (-9.18%)</td><td>18.82 <b>(-26.73%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>216.90 (n/a)</td><td>180.98 (n/a)</td><td>175.20 (n/a)</td><td>147.10 (n/a)</td><td>25.68 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (+3.96%)</td><td>0.07 <b>(+23.54%)</b></td><td>0.07 <b>(+25.92%)</b></td><td>0.06 <b>(+66.50%)</b></td><td>0.01 <b>(-57.97%)</b></td><td>166.60 <b>(-39.92%)</b></td><td>149.98 <b>(-22.28%)</b></td><td>145.40 <b>(-20.59%)</b></td><td>140.30 (-3.84%)</td><td>11.53 <b>(-76.90%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>277.30 (n/a)</td><td>192.98 (n/a)</td><td>183.10 (n/a)</td><td>145.90 (n/a)</td><td>49.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (-8.58%)</td><td>0.06 (+11.94%)</td><td>0.06 (+18.08%)</td><td>0.05 <b>(+35.69%)</b></td><td>0.01 <b>(-52.24%)</b></td><td>228.10 <b>(-26.30%)</b></td><td>189.90 (-14.57%)</td><td>188.50 (-15.28%)</td><td>168.20 (+9.36%)</td><td>23.12 <b>(-60.81%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>309.50 (n/a)</td><td>222.28 (n/a)</td><td>222.50 (n/a)</td><td>153.80 (n/a)</td><td>58.98 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 <b>(+24.74%)</b></td><td>0.14 (+17.75%)</td><td>0.14 (+17.58%)</td><td>0.12 (+17.94%)</td><td>0.02 <b>(+64.79%)</b></td><td>177.10 (-15.18%)</td><td>151.36 (-14.51%)</td><td>146.10 (-14.96%)</td><td>129.10 (-19.81%)</td><td>20.67 (+10.85%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>208.80 (n/a)</td><td>177.04 (n/a)</td><td>171.80 (n/a)</td><td>161.00 (n/a)</td><td>18.65 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (-3.96%)</td><td>0.12 (+0.15%)</td><td>0.11 (-14.42%)</td><td>0.10 <b>(+44.24%)</b></td><td>0.02 <b>(-27.31%)</b></td><td>204.00 <b>(-30.68%)</b></td><td>174.46 (-4.84%)</td><td>191.40 (+16.85%)</td><td>135.20 (+4.16%)</td><td>32.08 <b>(-50.38%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>294.30 (n/a)</td><td>183.34 (n/a)</td><td>163.80 (n/a)</td><td>129.80 (n/a)</td><td>64.65 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.18 <b>(+51.14%)</b></td><td>0.14 <b>(+31.36%)</b></td><td>0.13 <b>(+22.39%)</b></td><td>0.10 (+17.54%)</td><td>0.03 <b>(+148.81%)</b></td><td>210.20 (-14.93%)</td><td>158.48 <b>(-21.32%)</b></td><td>156.20 (-18.31%)</td><td>115.90 <b>(-33.85%)</b></td><td>38.56 <b>(+36.93%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>247.10 (n/a)</td><td>201.42 (n/a)</td><td>191.20 (n/a)</td><td>175.20 (n/a)</td><td>28.16 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 <b>(-28.02%)</b></td><td>0.10 (-19.13%)</td><td>0.10 (-17.87%)</td><td>0.08 (-14.02%)</td><td>0.01 <b>(-55.85%)</b></td><td>260.70 (+16.33%)</td><td>213.08 <b>(+20.25%)</b></td><td>210.70 <b>(+21.79%)</b></td><td>184.80 <b>(+38.95%)</b></td><td>28.90 <b>(-27.80%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>224.10 (n/a)</td><td>177.20 (n/a)</td><td>173.00 (n/a)</td><td>133.00 (n/a)</td><td>40.03 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 <b>(+31.68%)</b></td><td>0.12 (+11.85%)</td><td>0.13 (+10.25%)</td><td>0.10 (+2.94%)</td><td>0.02 <b>(+177.37%)</b></td><td>206.90 (-2.86%)</td><td>172.74 (-8.56%)</td><td>166.70 (-9.30%)</td><td>134.60 <b>(-24.04%)</b></td><td>31.56 <b>(+111.03%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>188.92 (n/a)</td><td>183.80 (n/a)</td><td>177.20 (n/a)</td><td>14.95 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.18 (+11.40%)</td><td>0.13 (+14.51%)</td><td>0.13 <b>(+31.83%)</b></td><td>0.09 (-10.49%)</td><td>0.03 <b>(+22.82%)</b></td><td>231.00 (+11.76%)</td><td>164.36 (-11.33%)</td><td>156.10 <b>(-24.15%)</b></td><td>117.60 (-10.23%)</td><td>41.25 <b>(+25.37%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>206.70 (n/a)</td><td>185.36 (n/a)</td><td>205.80 (n/a)</td><td>131.00 (n/a)</td><td>32.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (-10.13%)</td><td>0.11 (+3.62%)</td><td>0.11 (+17.77%)</td><td>0.07 (-6.66%)</td><td>0.02 (-8.54%)</td><td>301.20 (+7.15%)</td><td>205.80 (-3.35%)</td><td>183.00 (-15.08%)</td><td>174.10 (+11.32%)</td><td>54.02 (+11.99%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>281.10 (n/a)</td><td>212.94 (n/a)</td><td>215.50 (n/a)</td><td>156.40 (n/a)</td><td>48.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (-5.96%)</td><td>0.09 (-6.79%)</td><td>0.09 (-0.39%)</td><td>0.07 <b>(-25.23%)</b></td><td>0.01 <b>(+76.48%)</b></td><td>308.40 <b>(+33.74%)</b></td><td>236.46 (+9.25%)</td><td>224.50 (+0.36%)</td><td>200.30 (+6.37%)</td><td>43.24 <b>(+156.68%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>230.60 (n/a)</td><td>216.44 (n/a)</td><td>223.70 (n/a)</td><td>188.30 (n/a)</td><td>16.84 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>194.90 (n/a)</td><td>170.10 (n/a)</td><td>173.80 (n/a)</td><td>146.70 (n/a)</td><td>17.95 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>304.20 (n/a)</td><td>213.28 (n/a)</td><td>208.70 (n/a)</td><td>131.10 (n/a)</td><td>61.44 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>290.10 (n/a)</td><td>218.46 (n/a)</td><td>207.70 (n/a)</td><td>142.70 (n/a)</td><td>56.95 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.10 (n/a)</td><td>205.52 (n/a)</td><td>207.10 (n/a)</td><td>152.40 (n/a)</td><td>34.19 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>218.70 (n/a)</td><td>186.20 (n/a)</td><td>172.60 (n/a)</td><td>154.50 (n/a)</td><td>28.55 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>212.30 (n/a)</td><td>194.74 (n/a)</td><td>191.60 (n/a)</td><td>184.60 (n/a)</td><td>10.41 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>309.10 (n/a)</td><td>231.12 (n/a)</td><td>209.60 (n/a)</td><td>206.90 (n/a)</td><td>43.97 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>222.50 (n/a)</td><td>206.88 (n/a)</td><td>205.20 (n/a)</td><td>195.60 (n/a)</td><td>10.59 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>197.30 (n/a)</td><td>169.00 (n/a)</td><td>160.00 (n/a)</td><td>155.00 (n/a)</td><td>17.57 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>222.90 (n/a)</td><td>168.02 (n/a)</td><td>174.10 (n/a)</td><td>127.90 (n/a)</td><td>38.08 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>241.20 (n/a)</td><td>181.26 (n/a)</td><td>182.80 (n/a)</td><td>120.80 (n/a)</td><td>48.17 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>316.40 (n/a)</td><td>235.68 (n/a)</td><td>206.00 (n/a)</td><td>154.90 (n/a)</td><td>67.77 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.36 (+18.47%)</td><td>0.30 (+9.04%)</td><td>0.32 (+9.55%)</td><td>0.23 (-7.98%)</td><td>0.05 <b>(+105.52%)</b></td><td>216.00 (+8.65%)</td><td>167.50 (-6.57%)</td><td>155.00 (-8.72%)</td><td>138.40 (-15.56%)</td><td>31.10 <b>(+88.50%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.02 (n/a)</td><td>198.80 (n/a)</td><td>179.28 (n/a)</td><td>169.80 (n/a)</td><td>163.90 (n/a)</td><td>16.50 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>211.90 (n/a)</td><td>165.38 (n/a)</td><td>169.00 (n/a)</td><td>129.70 (n/a)</td><td>31.19 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>204.30 (n/a)</td><td>174.04 (n/a)</td><td>170.90 (n/a)</td><td>135.20 (n/a)</td><td>29.80 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>310.70 (n/a)</td><td>214.12 (n/a)</td><td>205.20 (n/a)</td><td>162.50 (n/a)</td><td>57.45 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>223.30 (n/a)</td><td>183.64 (n/a)</td><td>182.10 (n/a)</td><td>128.70 (n/a)</td><td>35.53 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>230.90 (n/a)</td><td>197.04 (n/a)</td><td>199.40 (n/a)</td><td>153.40 (n/a)</td><td>31.15 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>231.60 (n/a)</td><td>185.36 (n/a)</td><td>209.30 (n/a)</td><td>116.10 (n/a)</td><td>50.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>221.80 (n/a)</td><td>200.28 (n/a)</td><td>206.60 (n/a)</td><td>164.10 (n/a)</td><td>22.68 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>172.00 (n/a)</td><td>152.08 (n/a)</td><td>149.10 (n/a)</td><td>125.70 (n/a)</td><td>18.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>161.38 (n/a)</td><td>163.50 (n/a)</td><td>131.80 (n/a)</td><td>20.70 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>192.90 (n/a)</td><td>166.08 (n/a)</td><td>164.10 (n/a)</td><td>131.80 (n/a)</td><td>23.91 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>233.20 (n/a)</td><td>190.92 (n/a)</td><td>194.80 (n/a)</td><td>135.60 (n/a)</td><td>40.47 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>230.50 (n/a)</td><td>167.40 (n/a)</td><td>174.00 (n/a)</td><td>126.90 (n/a)</td><td>41.98 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>237.80 (n/a)</td><td>165.90 (n/a)</td><td>143.50 (n/a)</td><td>121.00 (n/a)</td><td>51.85 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>191.10 (n/a)</td><td>151.10 (n/a)</td><td>136.60 (n/a)</td><td>132.70 (n/a)</td><td>24.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>241.20 (n/a)</td><td>185.88 (n/a)</td><td>166.20 (n/a)</td><td>143.40 (n/a)</td><td>40.33 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.41 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.29 (n/a)</td><td>0.05 (n/a)</td><td>169.70 (n/a)</td><td>146.72 (n/a)</td><td>151.70 (n/a)</td><td>121.10 (n/a)</td><td>19.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.36 (n/a)</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>242.70 (n/a)</td><td>179.80 (n/a)</td><td>186.40 (n/a)</td><td>134.80 (n/a)</td><td>42.05 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.30 (n/a)</td><td>0.26 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>228.30 (n/a)</td><td>192.52 (n/a)</td><td>178.10 (n/a)</td><td>166.60 (n/a)</td><td>26.34 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>14.66 (-1.30%)</td><td>14.06 (-0.49%)</td><td>14.31 (+0.25%)</td><td>13.25 (+1.78%)</td><td>0.57 (-15.66%)</td><td>4203.80 (-1.75%)</td><td>3968.22 (+0.43%)</td><td>3893.70 (-0.25%)</td><td>3801.00 (+1.31%)</td><td>163.04 (-16.79%)</td><td>14124.61 (-1.30%)</td><td>13547.26 (-0.49%)</td><td>13788.20 (+0.25%)</td><td>12771.06 (+1.78%)</td><td>546.69 (-15.66%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>14.85 (n/a)</td><td>14.13 (n/a)</td><td>14.27 (n/a)</td><td>13.02 (n/a)</td><td>0.67 (n/a)</td><td>4278.50 (n/a)</td><td>3951.16 (n/a)</td><td>3903.30 (n/a)</td><td>3751.70 (n/a)</td><td>195.95 (n/a)</td><td>14310.26 (n/a)</td><td>13613.42 (n/a)</td><td>13754.25 (n/a)</td><td>12548.02 (n/a)</td><td>648.21 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>16.40 (+11.98%)</td><td>13.88 (+10.89%)</td><td>14.69 (+3.09%)</td><td>9.02 (-4.85%)</td><td>2.82 (+3.58%)</td><td>1452.70 (+5.10%)</td><td>987.08 (-9.62%)</td><td>892.00 (-2.99%)</td><td>799.30 (-10.69%)</td><td>263.58 (+2.32%)</td><td>10747.08 (+11.98%)</td><td>9094.27 (+10.89%)</td><td>9629.90 (+3.09%)</td><td>5912.98 (-4.85%)</td><td>1846.80 (+3.58%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>14.64 (n/a)</td><td>12.51 (n/a)</td><td>14.25 (n/a)</td><td>9.48 (n/a)</td><td>2.72 (n/a)</td><td>1382.20 (n/a)</td><td>1092.16 (n/a)</td><td>919.50 (n/a)</td><td>895.00 (n/a)</td><td>257.61 (n/a)</td><td>9597.55 (n/a)</td><td>8201.36 (n/a)</td><td>9341.66 (n/a)</td><td>6214.59 (n/a)</td><td>1782.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>14.06 (-7.78%)</td><td>13.30 (-1.74%)</td><td>12.92 (-8.30%)</td><td>12.74 (+12.45%)</td><td>0.61 <b>(-62.01%)</b></td><td>4371.50 (-11.07%)</td><td>4194.14 (+0.73%)</td><td>4310.00 (+9.05%)</td><td>3961.10 (+8.43%)</td><td>189.74 <b>(-63.57%)</b></td><td>13553.42 (-7.78%)</td><td>12821.77 (-1.74%)</td><td>12456.43 (-8.30%)</td><td>12281.06 (+12.45%)</td><td>589.43 <b>(-62.01%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>15.25 (n/a)</td><td>13.54 (n/a)</td><td>14.09 (n/a)</td><td>11.33 (n/a)</td><td>1.61 (n/a)</td><td>4915.70 (n/a)</td><td>4163.74 (n/a)</td><td>3952.30 (n/a)</td><td>3653.10 (n/a)</td><td>520.80 (n/a)</td><td>14696.34 (n/a)</td><td>13048.79 (n/a)</td><td>13583.79 (n/a)</td><td>10921.52 (n/a)</td><td>1551.69 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>15.72 (+1.73%)</td><td>15.27 <b>(+27.47%)</b></td><td>15.28 <b>(+39.88%)</b></td><td>14.92 <b>(+71.87%)</b></td><td>0.30 <b>(-89.68%)</b></td><td>1196.90 <b>(-41.82%)</b></td><td>1169.78 <b>(-25.12%)</b></td><td>1169.00 <b>(-28.51%)</b></td><td>1136.20 (-1.70%)</td><td>22.75 <b>(-93.91%)</b></td><td>11812.74 (+1.73%)</td><td>11477.25 <b>(+27.47%)</b></td><td>11481.67 <b>(+39.88%)</b></td><td>11213.34 <b>(+71.87%)</b></td><td>224.94 <b>(-89.68%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>15.45 (n/a)</td><td>11.98 (n/a)</td><td>10.92 (n/a)</td><td>8.68 (n/a)</td><td>2.90 (n/a)</td><td>2057.10 (n/a)</td><td>1562.22 (n/a)</td><td>1635.20 (n/a)</td><td>1155.90 (n/a)</td><td>373.83 (n/a)</td><td>11611.84 (n/a)</td><td>9003.94 (n/a)</td><td>8208.02 (n/a)</td><td>6524.47 (n/a)</td><td>2179.17 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>10.69 (-3.69%)</td><td>10.53 (-0.44%)</td><td>10.56 (+0.81%)</td><td>10.29 (-0.06%)</td><td>0.17 <b>(-48.61%)</b></td><td>7962.80 (+0.06%)</td><td>7783.86 (+0.39%)</td><td>7754.30 (-0.80%)</td><td>7662.00 (+3.84%)</td><td>123.90 <b>(-46.51%)</b></td><td>14013.79 (-3.69%)</td><td>13797.24 (-0.44%)</td><td>13847.08 (+0.81%)</td><td>13484.44 (-0.06%)</td><td>218.13 <b>(-48.61%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>11.10 (n/a)</td><td>10.57 (n/a)</td><td>10.48 (n/a)</td><td>10.29 (n/a)</td><td>0.32 (n/a)</td><td>7958.40 (n/a)</td><td>7753.82 (n/a)</td><td>7817.20 (n/a)</td><td>7379.00 (n/a)</td><td>231.63 (n/a)</td><td>14551.31 (n/a)</td><td>13858.06 (n/a)</td><td>13735.66 (n/a)</td><td>13491.92 (n/a)</td><td>424.43 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>15.77 (+4.55%)</td><td>14.71 (+10.23%)</td><td>14.35 (-1.56%)</td><td>13.88 <b>(+26.14%)</b></td><td>0.76 <b>(-64.19%)</b></td><td>1549.20 <b>(-20.72%)</b></td><td>1464.70 (-11.06%)</td><td>1498.00 (+1.59%)</td><td>1362.90 (-4.35%)</td><td>74.70 <b>(-73.19%)</b></td><td>12605.81 (+4.55%)</td><td>11754.11 (+10.23%)</td><td>11468.31 (-1.56%)</td><td>11089.24 <b>(+26.14%)</b></td><td>610.18 <b>(-64.19%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>15.09 (n/a)</td><td>13.34 (n/a)</td><td>14.58 (n/a)</td><td>11.00 (n/a)</td><td>2.13 (n/a)</td><td>1954.10 (n/a)</td><td>1646.76 (n/a)</td><td>1474.60 (n/a)</td><td>1424.90 (n/a)</td><td>278.62 (n/a)</td><td>12057.30 (n/a)</td><td>10663.06 (n/a)</td><td>11650.32 (n/a)</td><td>8791.49 (n/a)</td><td>1703.76 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>10.95 (-0.63%)</td><td>10.71 (-0.10%)</td><td>10.75 (+0.55%)</td><td>10.37 (+0.34%)</td><td>0.26 (-4.36%)</td><td>7897.80 (-0.34%)</td><td>7650.96 (+0.10%)</td><td>7621.60 (-0.55%)</td><td>7480.00 (+0.63%)</td><td>184.17 (-4.36%)</td><td>14354.93 (-0.63%)</td><td>14040.57 (-0.10%)</td><td>14088.14 (+0.55%)</td><td>13595.41 (+0.34%)</td><td>335.85 (-4.36%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>11.02 (n/a)</td><td>10.72 (n/a)</td><td>10.69 (n/a)</td><td>10.34 (n/a)</td><td>0.27 (n/a)</td><td>7925.10 (n/a)</td><td>7643.34 (n/a)</td><td>7663.80 (n/a)</td><td>7432.90 (n/a)</td><td>192.56 (n/a)</td><td>14445.79 (n/a)</td><td>14055.16 (n/a)</td><td>14010.58 (n/a)</td><td>13548.67 (n/a)</td><td>351.15 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.83 (-0.62%)</td><td>3.15 (+0.80%)</td><td>3.08 (+1.02%)</td><td>2.74 (+1.04%)</td><td>0.44 (-2.55%)</td><td>501.40 (-1.03%)</td><td>442.82 (-0.86%)</td><td>446.70 (-1.02%)</td><td>359.50 (+0.64%)</td><td>57.78 (-2.02%)</td><td>746.79 (-0.62%)</td><td>615.10 (+0.80%)</td><td>600.89 (+1.02%)</td><td>535.38 (+1.04%)</td><td>85.68 (-2.55%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.85 (n/a)</td><td>3.13 (n/a)</td><td>3.05 (n/a)</td><td>2.72 (n/a)</td><td>0.45 (n/a)</td><td>506.60 (n/a)</td><td>446.68 (n/a)</td><td>451.30 (n/a)</td><td>357.20 (n/a)</td><td>58.97 (n/a)</td><td>751.48 (n/a)</td><td>610.21 (n/a)</td><td>594.82 (n/a)</td><td>529.87 (n/a)</td><td>87.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.86 <b>(+32.16%)</b></td><td>3.85 (+9.33%)</td><td>3.68 (+2.07%)</td><td>3.42 (+2.24%)</td><td>0.57 <b>(+277.49%)</b></td><td>402.70 (-2.19%)</td><td>362.82 (-7.27%)</td><td>373.90 (-2.04%)</td><td>283.40 <b>(-24.33%)</b></td><td>46.04 <b>(+169.84%)</b></td><td>947.33 <b>(+32.16%)</b></td><td>751.20 (+9.33%)</td><td>717.91 (+2.07%)</td><td>666.61 (+2.24%)</td><td>111.79 <b>(+277.50%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.68 (n/a)</td><td>3.52 (n/a)</td><td>3.61 (n/a)</td><td>3.34 (n/a)</td><td>0.15 (n/a)</td><td>411.70 (n/a)</td><td>391.28 (n/a)</td><td>381.70 (n/a)</td><td>374.50 (n/a)</td><td>17.06 (n/a)</td><td>716.82 (n/a)</td><td>687.10 (n/a)</td><td>703.33 (n/a)</td><td>652.01 (n/a)</td><td>29.61 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>6.93 (+11.63%)</td><td>4.25 (+2.06%)</td><td>3.62 (-0.87%)</td><td>3.44 (+1.85%)</td><td>1.50 <b>(+27.24%)</b></td><td>400.40 (-1.81%)</td><td>347.20 (-0.03%)</td><td>379.70 (+0.88%)</td><td>198.60 (-10.42%)</td><td>83.62 (+10.20%)</td><td>1351.92 (+11.63%)</td><td>829.46 (+2.06%)</td><td>706.89 (-0.87%)</td><td>670.41 (+1.85%)</td><td>292.56 <b>(+27.24%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.21 (n/a)</td><td>4.17 (n/a)</td><td>3.66 (n/a)</td><td>3.37 (n/a)</td><td>1.18 (n/a)</td><td>407.80 (n/a)</td><td>347.32 (n/a)</td><td>376.40 (n/a)</td><td>221.70 (n/a)</td><td>75.87 (n/a)</td><td>1211.07 (n/a)</td><td>812.72 (n/a)</td><td>713.12 (n/a)</td><td>658.26 (n/a)</td><td>229.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>5.76 (-6.71%)</td><td>4.80 (+5.53%)</td><td>5.49 <b>(+45.38%)</b></td><td>3.43 (+2.28%)</td><td>1.11 <b>(-21.07%)</b></td><td>400.80 (-2.22%)</td><td>300.90 (-7.51%)</td><td>250.50 <b>(-31.22%)</b></td><td>238.80 (+7.18%)</td><td>76.86 (-16.46%)</td><td>1124.13 (-6.71%)</td><td>936.42 (+5.53%)</td><td>1071.66 <b>(+45.38%)</b></td><td>669.80 (+2.28%)</td><td>217.32 <b>(-21.07%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.18 (n/a)</td><td>4.55 (n/a)</td><td>3.78 (n/a)</td><td>3.36 (n/a)</td><td>1.41 (n/a)</td><td>409.90 (n/a)</td><td>325.32 (n/a)</td><td>364.20 (n/a)</td><td>222.80 (n/a)</td><td>92.01 (n/a)</td><td>1205.02 (n/a)</td><td>887.31 (n/a)</td><td>737.13 (n/a)</td><td>654.86 (n/a)</td><td>275.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.74 <b>(+31.00%)</b></td><td>3.52 (+4.70%)</td><td>3.38 (-0.65%)</td><td>3.01 (-3.20%)</td><td>0.71 <b>(+224.28%)</b></td><td>457.70 (+3.29%)</td><td>401.94 (-2.16%)</td><td>406.90 (+0.67%)</td><td>290.20 <b>(-23.65%)</b></td><td>67.77 <b>(+150.68%)</b></td><td>925.15 <b>(+31.00%)</b></td><td>686.48 (+4.70%)</td><td>659.77 (-0.65%)</td><td>586.51 (-3.20%)</td><td>138.84 <b>(+224.28%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.62 (n/a)</td><td>3.36 (n/a)</td><td>3.40 (n/a)</td><td>3.11 (n/a)</td><td>0.22 (n/a)</td><td>443.10 (n/a)</td><td>410.80 (n/a)</td><td>404.20 (n/a)</td><td>380.10 (n/a)</td><td>27.04 (n/a)</td><td>706.22 (n/a)</td><td>655.67 (n/a)</td><td>664.05 (n/a)</td><td>605.88 (n/a)</td><td>42.82 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.91 (+12.54%)</td><td>3.30 (+5.87%)</td><td>3.18 (+3.13%)</td><td>3.06 (+9.08%)</td><td>0.34 <b>(+45.21%)</b></td><td>449.40 (-8.34%)</td><td>420.30 (-5.25%)</td><td>432.30 (-3.03%)</td><td>352.20 (-11.15%)</td><td>38.81 (+16.46%)</td><td>762.17 (+12.54%)</td><td>643.62 (+5.87%)</td><td>620.90 (+3.13%)</td><td>597.26 (+9.08%)</td><td>67.10 <b>(+45.21%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.47 (n/a)</td><td>3.12 (n/a)</td><td>3.09 (n/a)</td><td>2.81 (n/a)</td><td>0.24 (n/a)</td><td>490.30 (n/a)</td><td>443.58 (n/a)</td><td>445.80 (n/a)</td><td>396.40 (n/a)</td><td>33.33 (n/a)</td><td>677.23 (n/a)</td><td>607.93 (n/a)</td><td>602.08 (n/a)</td><td>547.53 (n/a)</td><td>46.21 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.47 <b>(+37.38%)</b></td><td>3.52 (+13.88%)</td><td>3.13 (+1.92%)</td><td>2.99 (+1.41%)</td><td>0.67 <b>(+426.09%)</b></td><td>459.70 (-1.39%)</td><td>401.56 (-9.91%)</td><td>440.00 (-1.90%)</td><td>307.60 <b>(-27.21%)</b></td><td>70.23 <b>(+284.52%)</b></td><td>872.63 <b>(+37.38%)</b></td><td>686.76 (+13.88%)</td><td>610.04 (+1.92%)</td><td>583.92 (+1.41%)</td><td>131.00 <b>(+426.09%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.26 (n/a)</td><td>3.09 (n/a)</td><td>3.07 (n/a)</td><td>2.95 (n/a)</td><td>0.13 (n/a)</td><td>466.20 (n/a)</td><td>445.72 (n/a)</td><td>448.50 (n/a)</td><td>422.60 (n/a)</td><td>18.26 (n/a)</td><td>635.19 (n/a)</td><td>603.05 (n/a)</td><td>598.57 (n/a)</td><td>575.77 (n/a)</td><td>24.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.74 (-6.27%)</td><td>1.44 (+10.25%)</td><td>1.46 (+19.31%)</td><td>1.10 (+7.47%)</td><td>0.26 (-19.65%)</td><td>365.40 (-6.95%)</td><td>287.76 (-10.59%)</td><td>275.50 (-16.18%)</td><td>230.70 (+6.66%)</td><td>55.51 (-18.25%)</td><td>145.43 (-6.27%)</td><td>120.00 (+10.25%)</td><td>121.80 (+19.31%)</td><td>91.84 (+7.47%)</td><td>22.13 (-19.65%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.86 (n/a)</td><td>1.30 (n/a)</td><td>1.22 (n/a)</td><td>1.02 (n/a)</td><td>0.33 (n/a)</td><td>392.70 (n/a)</td><td>321.86 (n/a)</td><td>328.70 (n/a)</td><td>216.30 (n/a)</td><td>67.91 (n/a)</td><td>155.15 (n/a)</td><td>108.84 (n/a)</td><td>102.09 (n/a)</td><td>85.45 (n/a)</td><td>27.54 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>5.95 (+1.90%)</td><td>5.08 (+0.98%)</td><td>4.91 (-0.40%)</td><td>4.57 (+0.28%)</td><td>0.55 (+14.46%)</td><td>422.90 (-0.28%)</td><td>384.14 (-0.77%)</td><td>393.70 (+0.41%)</td><td>325.00 (-1.84%)</td><td>39.07 (+13.62%)</td><td>1239.06 (+1.90%)</td><td>1057.48 (+0.98%)</td><td>1022.64 (-0.40%)</td><td>952.05 (+0.28%)</td><td>115.01 (+14.46%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>5.84 (n/a)</td><td>5.03 (n/a)</td><td>4.93 (n/a)</td><td>4.56 (n/a)</td><td>0.48 (n/a)</td><td>424.10 (n/a)</td><td>387.12 (n/a)</td><td>392.10 (n/a)</td><td>331.10 (n/a)</td><td>34.38 (n/a)</td><td>1215.92 (n/a)</td><td>1047.18 (n/a)</td><td>1026.79 (n/a)</td><td>949.43 (n/a)</td><td>100.48 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>16.96 (-16.92%)</td><td>13.10 (-6.10%)</td><td>11.53 (-0.56%)</td><td>10.83 (-2.54%)</td><td>2.77 <b>(-30.31%)</b></td><td>508.30 (+2.60%)</td><td>434.28 (+4.25%)</td><td>477.60 (+0.55%)</td><td>324.60 <b>(+20.36%)</b></td><td>84.03 (-14.11%)</td><td>6616.23 (-16.92%)</td><td>5111.75 (-6.10%)</td><td>4496.05 (-0.56%)</td><td>4224.69 (-2.54%)</td><td>1080.93 <b>(-30.31%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>20.41 (n/a)</td><td>13.95 (n/a)</td><td>11.59 (n/a)</td><td>11.11 (n/a)</td><td>3.98 (n/a)</td><td>495.40 (n/a)</td><td>416.56 (n/a)</td><td>475.00 (n/a)</td><td>269.70 (n/a)</td><td>97.84 (n/a)</td><td>7963.58 (n/a)</td><td>5443.63 (n/a)</td><td>4521.27 (n/a)</td><td>4334.82 (n/a)</td><td>1550.98 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>8.52 (-18.46%)</td><td>8.12 (-4.50%)</td><td>8.05 (+1.30%)</td><td>7.88 (+4.41%)</td><td>0.24 <b>(-79.72%)</b></td><td>698.60 (-4.22%)</td><td>678.82 (+3.31%)</td><td>683.60 (-1.29%)</td><td>646.40 <b>(+22.63%)</b></td><td>19.75 <b>(-76.23%)</b></td><td>3322.27 (-18.46%)</td><td>3165.74 (-4.50%)</td><td>3141.57 (+1.30%)</td><td>3073.81 (+4.41%)</td><td>94.46 <b>(-79.72%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>10.44 (n/a)</td><td>8.50 (n/a)</td><td>7.95 (n/a)</td><td>7.55 (n/a)</td><td>1.19 (n/a)</td><td>729.40 (n/a)</td><td>657.10 (n/a)</td><td>692.50 (n/a)</td><td>527.10 (n/a)</td><td>83.09 (n/a)</td><td>4074.28 (n/a)</td><td>3315.08 (n/a)</td><td>3101.25 (n/a)</td><td>2944.07 (n/a)</td><td>465.83 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>11.42 (+13.38%)</td><td>9.24 (+5.10%)</td><td>8.90 (+2.85%)</td><td>8.11 (+1.35%)</td><td>1.27 <b>(+64.02%)</b></td><td>715.00 (-1.32%)</td><td>636.24 (-4.14%)</td><td>651.90 (-2.77%)</td><td>507.80 (-11.79%)</td><td>76.70 <b>(+40.62%)</b></td><td>4757.84 (+13.38%)</td><td>3847.79 (+5.10%)</td><td>3705.73 (+2.85%)</td><td>3378.95 (+1.35%)</td><td>527.52 <b>(+64.02%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>10.07 (n/a)</td><td>8.79 (n/a)</td><td>8.65 (n/a)</td><td>8.00 (n/a)</td><td>0.77 (n/a)</td><td>724.60 (n/a)</td><td>663.74 (n/a)</td><td>670.50 (n/a)</td><td>575.70 (n/a)</td><td>54.54 (n/a)</td><td>4196.45 (n/a)</td><td>3660.92 (n/a)</td><td>3603.02 (n/a)</td><td>3334.01 (n/a)</td><td>321.61 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.40 (n/a)</td><td>168.08 (n/a)</td><td>172.30 (n/a)</td><td>107.10 (n/a)</td><td>38.18 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>175.50 (n/a)</td><td>152.42 (n/a)</td><td>161.30 (n/a)</td><td>102.00 (n/a)</td><td>28.91 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>246.70 (n/a)</td><td>168.00 (n/a)</td><td>143.60 (n/a)</td><td>112.80 (n/a)</td><td>57.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>268.00 (n/a)</td><td>193.46 (n/a)</td><td>173.90 (n/a)</td><td>171.20 (n/a)</td><td>41.85 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.40 (n/a)</td><td>174.06 (n/a)</td><td>160.40 (n/a)</td><td>137.60 (n/a)</td><td>31.73 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.70 (n/a)</td><td>200.20 (n/a)</td><td>194.80 (n/a)</td><td>190.60 (n/a)</td><td>10.97 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.30 (n/a)</td><td>187.42 (n/a)</td><td>185.90 (n/a)</td><td>158.80 (n/a)</td><td>24.09 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>321.20 (n/a)</td><td>248.96 (n/a)</td><td>219.70 (n/a)</td><td>204.30 (n/a)</td><td>49.95 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>181.00 (n/a)</td><td>170.06 (n/a)</td><td>171.10 (n/a)</td><td>156.60 (n/a)</td><td>8.74 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.90 (n/a)</td><td>171.04 (n/a)</td><td>160.50 (n/a)</td><td>134.00 (n/a)</td><td>30.81 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>212.90 (n/a)</td><td>183.00 (n/a)</td><td>182.40 (n/a)</td><td>161.20 (n/a)</td><td>19.71 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.80 (n/a)</td><td>172.44 (n/a)</td><td>180.60 (n/a)</td><td>136.60 (n/a)</td><td>27.15 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.60 (n/a)</td><td>196.92 (n/a)</td><td>187.30 (n/a)</td><td>140.40 (n/a)</td><td>52.87 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.60 (n/a)</td><td>170.30 (n/a)</td><td>175.90 (n/a)</td><td>116.80 (n/a)</td><td>40.78 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.60 (n/a)</td><td>164.92 (n/a)</td><td>168.00 (n/a)</td><td>124.70 (n/a)</td><td>38.46 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.00 (n/a)</td><td>184.96 (n/a)</td><td>178.90 (n/a)</td><td>141.10 (n/a)</td><td>32.36 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>186.90 (n/a)</td><td>164.00 (n/a)</td><td>165.10 (n/a)</td><td>138.70 (n/a)</td><td>22.38 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>195.90 (n/a)</td><td>167.70 (n/a)</td><td>180.90 (n/a)</td><td>135.30 (n/a)</td><td>29.29 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>192.50 (n/a)</td><td>158.04 (n/a)</td><td>146.10 (n/a)</td><td>132.90 (n/a)</td><td>25.69 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>189.80 (n/a)</td><td>173.32 (n/a)</td><td>182.90 (n/a)</td><td>146.80 (n/a)</td><td>18.23 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>243.00 (n/a)</td><td>194.18 (n/a)</td><td>195.70 (n/a)</td><td>149.80 (n/a)</td><td>40.72 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>210.90 (n/a)</td><td>172.74 (n/a)</td><td>160.20 (n/a)</td><td>136.90 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>224.00 (n/a)</td><td>196.14 (n/a)</td><td>198.50 (n/a)</td><td>163.90 (n/a)</td><td>24.21 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>314.70 (n/a)</td><td>241.68 (n/a)</td><td>237.80 (n/a)</td><td>187.70 (n/a)</td><td>46.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>218.90 (n/a)</td><td>171.90 (n/a)</td><td>190.00 (n/a)</td><td>119.20 (n/a)</td><td>42.26 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>189.40 (n/a)</td><td>157.68 (n/a)</td><td>171.00 (n/a)</td><td>114.70 (n/a)</td><td>35.71 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>211.60 (n/a)</td><td>177.02 (n/a)</td><td>175.60 (n/a)</td><td>143.10 (n/a)</td><td>24.38 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>202.10 (n/a)</td><td>189.50 (n/a)</td><td>195.70 (n/a)</td><td>165.10 (n/a)</td><td>15.69 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>203.60 (n/a)</td><td>176.46 (n/a)</td><td>186.50 (n/a)</td><td>119.40 (n/a)</td><td>32.95 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>225.50 (n/a)</td><td>181.92 (n/a)</td><td>182.40 (n/a)</td><td>130.00 (n/a)</td><td>37.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>328.40 (n/a)</td><td>200.04 (n/a)</td><td>174.80 (n/a)</td><td>136.00 (n/a)</td><td>74.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>234.20 (n/a)</td><td>204.02 (n/a)</td><td>203.70 (n/a)</td><td>170.40 (n/a)</td><td>24.37 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.19 (+1.56%)</td><td>4.11 (+0.14%)</td><td>4.11 (-0.04%)</td><td>4.06 (-0.76%)</td><td>0.05 <b>(+219.41%)</b></td><td>19378.60 (+0.77%)</td><td>19127.00 (-0.13%)</td><td>19126.50 (+0.04%)</td><td>18791.70 (-1.54%)</td><td>215.93 <b>(+216.33%)</b></td><td>2856.96 (+1.56%)</td><td>2807.16 (+0.14%)</td><td>2806.95 (-0.04%)</td><td>2770.43 (-0.76%)</td><td>31.88 <b>(+219.41%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>4.12 (n/a)</td><td>4.11 (n/a)</td><td>4.11 (n/a)</td><td>4.09 (n/a)</td><td>0.01 (n/a)</td><td>19230.70 (n/a)</td><td>19151.38 (n/a)</td><td>19118.00 (n/a)</td><td>19084.90 (n/a)</td><td>68.26 (n/a)</td><td>2813.07 (n/a)</td><td>2803.33 (n/a)</td><td>2808.19 (n/a)</td><td>2791.74 (n/a)</td><td>9.98 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.34 (-1.52%)</td><td>4.05 (-5.40%)</td><td>4.20 (-2.77%)</td><td>3.56 (-14.27%)</td><td>0.32 <b>(+193.12%)</b></td><td>2641.80 (+16.65%)</td><td>2336.34 (+6.22%)</td><td>2237.00 (+2.86%)</td><td>2166.00 (+1.55%)</td><td>196.50 <b>(+246.23%)</b></td><td>1707.93 (-1.52%)</td><td>1591.92 (-5.40%)</td><td>1653.75 (-2.77%)</td><td>1400.31 (-14.27%)</td><td>126.85 <b>(+193.12%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>4.41 (n/a)</td><td>4.28 (n/a)</td><td>4.32 (n/a)</td><td>4.15 (n/a)</td><td>0.11 (n/a)</td><td>2264.80 (n/a)</td><td>2199.46 (n/a)</td><td>2174.90 (n/a)</td><td>2133.00 (n/a)</td><td>56.75 (n/a)</td><td>1734.34 (n/a)</td><td>1682.83 (n/a)</td><td>1700.91 (n/a)</td><td>1633.41 (n/a)</td><td>43.28 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.26 <b>(+30.35%)</b></td><td>1.03 (+17.70%)</td><td>1.13 <b>(+24.47%)</b></td><td>0.63 (-10.35%)</td><td>0.25 <b>(+151.62%)</b></td><td>348.50 (+11.56%)</td><td>228.60 (-10.65%)</td><td>196.60 (-19.66%)</td><td>175.80 <b>(-23.26%)</b></td><td>71.07 <b>(+114.54%)</b></td><td>53.69 <b>(+30.35%)</b></td><td>43.93 (+17.70%)</td><td>48.01 <b>(+24.47%)</b></td><td>27.08 (-10.35%)</td><td>10.78 <b>(+151.62%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.97 (n/a)</td><td>0.87 (n/a)</td><td>0.90 (n/a)</td><td>0.71 (n/a)</td><td>0.10 (n/a)</td><td>312.40 (n/a)</td><td>255.86 (n/a)</td><td>244.70 (n/a)</td><td>229.10 (n/a)</td><td>33.13 (n/a)</td><td>41.19 (n/a)</td><td>37.33 (n/a)</td><td>38.57 (n/a)</td><td>30.21 (n/a)</td><td>4.29 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.02 (+0.76%)</td><td>0.82 (-0.24%)</td><td>0.76 (-2.14%)</td><td>0.64 (-4.14%)</td><td>0.18 (+8.79%)</td><td>344.80 (+4.33%)</td><td>279.64 (+0.84%)</td><td>292.90 (+2.20%)</td><td>216.00 (-0.74%)</td><td>58.46 (+9.77%)</td><td>43.69 (+0.76%)</td><td>35.01 (-0.24%)</td><td>32.22 (-2.14%)</td><td>27.37 (-4.14%)</td><td>7.61 (+8.79%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.02 (n/a)</td><td>0.82 (n/a)</td><td>0.77 (n/a)</td><td>0.67 (n/a)</td><td>0.16 (n/a)</td><td>330.50 (n/a)</td><td>277.30 (n/a)</td><td>286.60 (n/a)</td><td>217.60 (n/a)</td><td>53.26 (n/a)</td><td>43.36 (n/a)</td><td>35.10 (n/a)</td><td>32.93 (n/a)</td><td>28.55 (n/a)</td><td>6.99 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.53 (-0.82%)</td><td>0.53 (-0.24%)</td><td>0.53 (-0.09%)</td><td>0.53 (-0.13%)</td><td>0.00 <b>(-83.53%)</b></td><td>47856.30 (+0.13%)</td><td>47809.32 (+0.23%)</td><td>47806.80 (+0.08%)</td><td>47779.70 (+0.83%)</td><td>28.95 <b>(-83.37%)</b></td><td>359.56 (-0.82%)</td><td>359.34 (-0.24%)</td><td>359.36 (-0.09%)</td><td>358.99 (-0.13%)</td><td>0.22 <b>(-83.53%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47794.50 (n/a)</td><td>47697.24 (n/a)</td><td>47766.20 (n/a)</td><td>47386.80 (n/a)</td><td>174.09 (n/a)</td><td>362.55 (n/a)</td><td>360.19 (n/a)</td><td>359.67 (n/a)</td><td>359.45 (n/a)</td><td>1.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.21 (-0.14%)</td><td>0.21 (-0.12%)</td><td>0.21 (-0.31%)</td><td>0.21 (+0.52%)</td><td>0.00 <b>(-32.47%)</b></td><td>119400.20 (-0.51%)</td><td>119013.32 (+0.12%)</td><td>119297.10 (+0.31%)</td><td>118284.00 (+0.14%)</td><td>493.55 <b>(-32.71%)</b></td><td>145.24 (-0.14%)</td><td>144.35 (-0.12%)</td><td>144.01 (-0.31%)</td><td>143.88 (+0.52%)</td><td>0.60 <b>(-32.47%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>120015.40 (n/a)</td><td>118869.14 (n/a)</td><td>118925.40 (n/a)</td><td>118113.70 (n/a)</td><td>733.48 (n/a)</td><td>145.45 (n/a)</td><td>144.53 (n/a)</td><td>144.46 (n/a)</td><td>143.15 (n/a)</td><td>0.89 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.91 (+0.10%)</td><td>0.90 (+0.25%)</td><td>0.91 (+0.19%)</td><td>0.90 (+0.69%)</td><td>0.00 <b>(-36.64%)</b></td><td>27941.60 (-0.68%)</td><td>27823.14 (-0.25%)</td><td>27798.20 (-0.19%)</td><td>27735.40 (-0.10%)</td><td>88.21 <b>(-37.23%)</b></td><td>619.42 (+0.10%)</td><td>617.47 (+0.25%)</td><td>618.02 (+0.19%)</td><td>614.85 (+0.69%)</td><td>1.96 <b>(-36.64%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.89 (n/a)</td><td>0.00 (n/a)</td><td>28133.70 (n/a)</td><td>27893.64 (n/a)</td><td>27851.80 (n/a)</td><td>27762.70 (n/a)</td><td>140.53 (n/a)</td><td>618.81 (n/a)</td><td>615.92 (n/a)</td><td>616.83 (n/a)</td><td>610.65 (n/a)</td><td>3.09 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.66 (+0.54%)</td><td>3.52 (-0.89%)</td><td>3.58 (-0.90%)</td><td>3.32 (-2.97%)</td><td>0.14 <b>(+40.84%)</b></td><td>7582.70 (+3.06%)</td><td>7156.22 (+0.96%)</td><td>7021.90 (+0.91%)</td><td>6875.00 (-0.54%)</td><td>298.14 <b>(+44.52%)</b></td><td>2498.89 (+0.54%)</td><td>2403.96 (-0.89%)</td><td>2446.62 (-0.90%)</td><td>2265.66 (-2.97%)</td><td>98.24 <b>(+40.84%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.64 (n/a)</td><td>3.55 (n/a)</td><td>3.62 (n/a)</td><td>3.42 (n/a)</td><td>0.10 (n/a)</td><td>7357.90 (n/a)</td><td>7087.90 (n/a)</td><td>6958.80 (n/a)</td><td>6912.00 (n/a)</td><td>206.29 (n/a)</td><td>2485.51 (n/a)</td><td>2425.45 (n/a)</td><td>2468.79 (n/a)</td><td>2334.89 (n/a)</td><td>69.75 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.20 (+0.34%)</td><td>2.96 (-1.53%)</td><td>2.87 (-2.77%)</td><td>2.79 (-3.14%)</td><td>0.17 <b>(+31.63%)</b></td><td>9031.50 (+3.24%)</td><td>8529.04 (+1.67%)</td><td>8775.40 (+2.85%)</td><td>7859.70 (-0.33%)</td><td>487.78 <b>(+35.20%)</b></td><td>2185.83 (+0.34%)</td><td>2019.69 (-1.53%)</td><td>1957.72 (-2.77%)</td><td>1902.22 (-3.14%)</td><td>118.33 <b>(+31.63%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.19 (n/a)</td><td>3.00 (n/a)</td><td>2.95 (n/a)</td><td>2.88 (n/a)</td><td>0.13 (n/a)</td><td>8747.90 (n/a)</td><td>8388.88 (n/a)</td><td>8532.10 (n/a)</td><td>7886.00 (n/a)</td><td>360.79 (n/a)</td><td>2178.52 (n/a)</td><td>2051.03 (n/a)</td><td>2013.56 (n/a)</td><td>1963.88 (n/a)</td><td>89.89 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.33 (+3.00%)</td><td>3.22 (+1.11%)</td><td>3.19 (+0.47%)</td><td>3.11 (-1.51%)</td><td>0.09 <b>(+203.72%)</b></td><td>8097.20 (+1.54%)</td><td>7812.64 (-1.05%)</td><td>7878.70 (-0.46%)</td><td>7557.60 (-2.91%)</td><td>218.49 <b>(+198.78%)</b></td><td>2273.20 (+3.00%)</td><td>2200.37 (+1.11%)</td><td>2180.56 (+0.47%)</td><td>2121.71 (-1.51%)</td><td>61.52 <b>(+203.73%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.23 (n/a)</td><td>3.19 (n/a)</td><td>3.18 (n/a)</td><td>3.16 (n/a)</td><td>0.03 (n/a)</td><td>7974.70 (n/a)</td><td>7895.16 (n/a)</td><td>7915.50 (n/a)</td><td>7784.50 (n/a)</td><td>73.13 (n/a)</td><td>2206.93 (n/a)</td><td>2176.15 (n/a)</td><td>2170.40 (n/a)</td><td>2154.29 (n/a)</td><td>20.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.80 (-0.38%)</td><td>0.80 (-0.04%)</td><td>0.80 (+0.07%)</td><td>0.80 (+0.09%)</td><td>0.00 <b>(-91.82%)</b></td><td>94814.20 (-0.09%)</td><td>94785.24 (+0.03%)</td><td>94780.30 (-0.07%)</td><td>94770.20 (+0.38%)</td><td>16.82 <b>(-91.80%)</b></td><td>725.12 (-0.38%)</td><td>725.00 (-0.04%)</td><td>725.04 (+0.07%)</td><td>724.78 (+0.09%)</td><td>0.13 <b>(-91.82%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94902.00 (n/a)</td><td>94752.08 (n/a)</td><td>94847.70 (n/a)</td><td>94409.40 (n/a)</td><td>205.06 (n/a)</td><td>727.89 (n/a)</td><td>725.26 (n/a)</td><td>724.52 (n/a)</td><td>724.11 (n/a)</td><td>1.57 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.73 (+0.39%)</td><td>0.73 (+0.08%)</td><td>0.73 (+0.01%)</td><td>0.73 (-0.01%)</td><td>0.00 <b>(+888.62%)</b></td><td>103375.40 (+0.01%)</td><td>103261.64 (-0.08%)</td><td>103338.50 (-0.01%)</td><td>102914.60 (-0.39%)</td><td>194.95 <b>(+883.83%)</b></td><td>667.73 (+0.39%)</td><td>665.49 (+0.08%)</td><td>664.99 (+0.01%)</td><td>664.76 (-0.01%)</td><td>1.26 <b>(+888.76%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103359.90 (n/a)</td><td>103341.44 (n/a)</td><td>103346.40 (n/a)</td><td>103318.30 (n/a)</td><td>19.82 (n/a)</td><td>665.12 (n/a)</td><td>664.97 (n/a)</td><td>664.94 (n/a)</td><td>664.86 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.69 (+0.26%)</td><td>0.69 (+0.51%)</td><td>0.69 (+0.62%)</td><td>0.69 (+0.40%)</td><td>0.00 (-19.17%)</td><td>110213.70 (-0.40%)</td><td>109818.34 (-0.51%)</td><td>109822.10 (-0.61%)</td><td>109576.30 (-0.26%)</td><td>247.46 (-19.65%)</td><td>627.14 (+0.26%)</td><td>625.76 (+0.51%)</td><td>625.73 (+0.62%)</td><td>623.51 (+0.40%)</td><td>1.41 (-19.17%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110651.10 (n/a)</td><td>110377.96 (n/a)</td><td>110498.90 (n/a)</td><td>109863.20 (n/a)</td><td>307.97 (n/a)</td><td>625.50 (n/a)</td><td>622.59 (n/a)</td><td>621.90 (n/a)</td><td>621.05 (n/a)</td><td>1.74 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>2.80 (+0.01%)</td><td>2.79 (-0.15%)</td><td>2.80 (-0.11%)</td><td>2.78 (-0.53%)</td><td>0.01 <b>(+304.71%)</b></td><td>37729.10 (+0.53%)</td><td>37542.98 (+0.15%)</td><td>37512.90 (+0.11%)</td><td>37463.20 (-0.01%)</td><td>107.53 <b>(+306.80%)</b></td><td>2866.12 (+0.01%)</td><td>2860.05 (-0.15%)</td><td>2862.32 (-0.11%)</td><td>2845.92 (-0.53%)</td><td>8.17 <b>(+304.74%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>2.80 (n/a)</td><td>2.80 (n/a)</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>0.00 (n/a)</td><td>37530.90 (n/a)</td><td>37485.04 (n/a)</td><td>37472.00 (n/a)</td><td>37467.20 (n/a)</td><td>26.43 (n/a)</td><td>2865.82 (n/a)</td><td>2864.45 (n/a)</td><td>2865.45 (n/a)</td><td>2860.95 (n/a)</td><td>2.02 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>7.59 (-5.30%)</td><td>7.26 (+1.96%)</td><td>7.52 (+8.34%)</td><td>6.68 (-1.17%)</td><td>0.42 (-17.57%)</td><td>1334.20 (+1.19%)</td><td>1230.52 (-2.02%)</td><td>1184.80 (-7.70%)</td><td>1174.70 (+5.59%)</td><td>72.61 (-11.27%)</td><td>457.02 (-5.30%)</td><td>437.48 (+1.96%)</td><td>453.15 (+8.34%)</td><td>402.40 (-1.17%)</td><td>25.04 (-17.57%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>8.01 (n/a)</td><td>7.12 (n/a)</td><td>6.94 (n/a)</td><td>6.76 (n/a)</td><td>0.50 (n/a)</td><td>1318.50 (n/a)</td><td>1255.88 (n/a)</td><td>1283.60 (n/a)</td><td>1112.50 (n/a)</td><td>81.83 (n/a)</td><td>482.58 (n/a)</td><td>429.07 (n/a)</td><td>418.26 (n/a)</td><td>407.17 (n/a)</td><td>30.37 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>7.20 (+4.76%)</td><td>6.26 (-6.64%)</td><td>6.72 (-1.14%)</td><td>4.17 <b>(-33.82%)</b></td><td>1.21 <b>(+415.01%)</b></td><td>2136.70 <b>(+51.10%)</b></td><td>1479.84 (+11.29%)</td><td>1326.60 (+1.15%)</td><td>1237.40 (-4.54%)</td><td>371.56 <b>(+667.64%)</b></td><td>433.88 (+4.76%)</td><td>377.32 (-6.64%)</td><td>404.68 (-1.14%)</td><td>251.26 <b>(-33.82%)</b></td><td>72.65 <b>(+415.01%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.88 (n/a)</td><td>6.71 (n/a)</td><td>6.80 (n/a)</td><td>6.30 (n/a)</td><td>0.23 (n/a)</td><td>1414.10 (n/a)</td><td>1329.72 (n/a)</td><td>1311.50 (n/a)</td><td>1296.30 (n/a)</td><td>48.40 (n/a)</td><td>414.15 (n/a)</td><td>404.16 (n/a)</td><td>409.35 (n/a)</td><td>379.66 (n/a)</td><td>14.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>6.72 (+2.39%)</td><td>6.03 (-1.75%)</td><td>6.25 (+2.70%)</td><td>4.77 (-15.57%)</td><td>0.75 <b>(+119.27%)</b></td><td>1867.60 (+18.44%)</td><td>1499.92 (+2.97%)</td><td>1426.50 (-2.63%)</td><td>1325.60 (-2.33%)</td><td>213.22 <b>(+160.06%)</b></td><td>405.01 (+2.39%)</td><td>363.03 (-1.75%)</td><td>376.35 (+2.70%)</td><td>287.47 (-15.57%)</td><td>45.01 <b>(+119.27%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.57 (n/a)</td><td>6.13 (n/a)</td><td>6.08 (n/a)</td><td>5.65 (n/a)</td><td>0.34 (n/a)</td><td>1576.80 (n/a)</td><td>1456.62 (n/a)</td><td>1465.10 (n/a)</td><td>1357.20 (n/a)</td><td>81.99 (n/a)</td><td>395.56 (n/a)</td><td>369.50 (n/a)</td><td>366.45 (n/a)</td><td>340.49 (n/a)</td><td>20.53 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>8.44 (+5.74%)</td><td>8.08 (+3.11%)</td><td>7.97 (+0.27%)</td><td>7.94 (+7.36%)</td><td>0.21 (-15.12%)</td><td>4390.80 (-6.85%)</td><td>4316.78 (-3.05%)</td><td>4375.40 (-0.27%)</td><td>4131.90 (-5.43%)</td><td>109.59 <b>(-25.49%)</b></td><td>519.74 (+5.74%)</td><td>497.73 (+3.11%)</td><td>490.80 (+0.27%)</td><td>489.08 (+7.36%)</td><td>12.98 (-15.12%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>7.98 (n/a)</td><td>7.84 (n/a)</td><td>7.95 (n/a)</td><td>7.40 (n/a)</td><td>0.25 (n/a)</td><td>4713.90 (n/a)</td><td>4452.38 (n/a)</td><td>4387.30 (n/a)</td><td>4369.00 (n/a)</td><td>147.09 (n/a)</td><td>491.53 (n/a)</td><td>482.73 (n/a)</td><td>489.47 (n/a)</td><td>455.56 (n/a)</td><td>15.29 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>7.61 (-3.58%)</td><td>7.29 (-4.64%)</td><td>7.39 (-3.10%)</td><td>6.88 (-8.24%)</td><td>0.34 <b>(+122.50%)</b></td><td>5069.00 (+8.98%)</td><td>4794.10 (+5.01%)</td><td>4716.70 (+3.20%)</td><td>4582.10 (+3.71%)</td><td>225.85 <b>(+152.21%)</b></td><td>468.67 (-3.58%)</td><td>448.73 (-4.64%)</td><td>455.29 (-3.10%)</td><td>423.65 (-8.24%)</td><td>20.88 <b>(+122.50%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>7.89 (n/a)</td><td>7.64 (n/a)</td><td>7.63 (n/a)</td><td>7.50 (n/a)</td><td>0.15 (n/a)</td><td>4651.30 (n/a)</td><td>4565.16 (n/a)</td><td>4570.60 (n/a)</td><td>4418.20 (n/a)</td><td>89.55 (n/a)</td><td>486.06 (n/a)</td><td>470.55 (n/a)</td><td>469.85 (n/a)</td><td>461.69 (n/a)</td><td>9.39 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>7.65 (-1.44%)</td><td>7.41 (+2.88%)</td><td>7.40 (+5.36%)</td><td>7.28 (+6.63%)</td><td>0.15 <b>(-60.55%)</b></td><td>4789.80 (-6.22%)</td><td>4707.06 (-2.98%)</td><td>4710.20 (-5.08%)</td><td>4557.10 (+1.46%)</td><td>92.64 <b>(-62.39%)</b></td><td>471.24 (-1.44%)</td><td>456.37 (+2.88%)</td><td>455.93 (+5.36%)</td><td>448.35 (+6.63%)</td><td>9.12 <b>(-60.55%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>7.76 (n/a)</td><td>7.20 (n/a)</td><td>7.03 (n/a)</td><td>6.83 (n/a)</td><td>0.38 (n/a)</td><td>5107.40 (n/a)</td><td>4851.48 (n/a)</td><td>4962.50 (n/a)</td><td>4491.50 (n/a)</td><td>246.32 (n/a)</td><td>478.12 (n/a)</td><td>443.59 (n/a)</td><td>432.74 (n/a)</td><td>420.47 (n/a)</td><td>23.13 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.80 (+0.09%)</td><td>0.80 (+0.20%)</td><td>0.80 (+0.23%)</td><td>0.80 (+0.28%)</td><td>0.00 <b>(-55.81%)</b></td><td>94153.40 (-0.28%)</td><td>94068.22 (-0.20%)</td><td>94048.90 (-0.23%)</td><td>94020.50 (-0.09%)</td><td>52.14 <b>(-55.96%)</b></td><td>730.90 (+0.09%)</td><td>730.53 (+0.20%)</td><td>730.68 (+0.23%)</td><td>729.87 (+0.28%)</td><td>0.40 <b>(-55.81%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94421.30 (n/a)</td><td>94254.90 (n/a)</td><td>94264.00 (n/a)</td><td>94105.70 (n/a)</td><td>118.40 (n/a)</td><td>730.24 (n/a)</td><td>729.08 (n/a)</td><td>729.01 (n/a)</td><td>727.80 (n/a)</td><td>0.92 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.74 (-0.01%)</td><td>0.74 (-0.05%)</td><td>0.74 (+0.03%)</td><td>0.73 (-0.20%)</td><td>0.00 <b>(+221.88%)</b></td><td>102858.60 (+0.20%)</td><td>102670.58 (+0.05%)</td><td>102606.70 (-0.03%)</td><td>102568.40 (+0.01%)</td><td>126.38 <b>(+222.39%)</b></td><td>669.99 (-0.01%)</td><td>669.32 (-0.05%)</td><td>669.74 (+0.03%)</td><td>668.10 (-0.20%)</td><td>0.82 <b>(+221.86%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102648.40 (n/a)</td><td>102616.52 (n/a)</td><td>102632.90 (n/a)</td><td>102555.00 (n/a)</td><td>39.20 (n/a)</td><td>670.07 (n/a)</td><td>669.67 (n/a)</td><td>669.57 (n/a)</td><td>669.46 (n/a)</td><td>0.26 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.71 (+0.15%)</td><td>0.71 (+0.03%)</td><td>0.71 (-0.00%)</td><td>0.71 (-0.13%)</td><td>0.00 <b>(+105.88%)</b></td><td>106190.50 (+0.13%)</td><td>105933.24 (-0.03%)</td><td>105951.30 (+0.00%)</td><td>105669.30 (-0.15%)</td><td>192.21 <b>(+105.79%)</b></td><td>650.33 (+0.15%)</td><td>648.71 (+0.03%)</td><td>648.60 (-0.00%)</td><td>647.13 (-0.13%)</td><td>1.18 <b>(+105.87%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106055.10 (n/a)</td><td>105964.96 (n/a)</td><td>105948.40 (n/a)</td><td>105831.40 (n/a)</td><td>93.40 (n/a)</td><td>649.33 (n/a)</td><td>648.51 (n/a)</td><td>648.61 (n/a)</td><td>647.96 (n/a)</td><td>0.57 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.38 (+8.87%)</td><td>3.61 (+7.30%)</td><td>3.66 (+16.60%)</td><td>3.02 (+2.87%)</td><td>0.57 <b>(+21.92%)</b></td><td>2672.90 (-2.79%)</td><td>2278.98 (-6.32%)</td><td>2200.50 (-14.23%)</td><td>1841.30 (-8.15%)</td><td>357.41 (+11.40%)</td><td>1148.08 (+8.87%)</td><td>946.30 (+7.30%)</td><td>960.66 (+16.60%)</td><td>790.87 (+2.87%)</td><td>149.99 <b>(+21.92%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>4.02 (n/a)</td><td>3.36 (n/a)</td><td>3.14 (n/a)</td><td>2.93 (n/a)</td><td>0.47 (n/a)</td><td>2749.60 (n/a)</td><td>2432.66 (n/a)</td><td>2565.70 (n/a)</td><td>2004.60 (n/a)</td><td>320.82 (n/a)</td><td>1054.56 (n/a)</td><td>881.94 (n/a)</td><td>823.92 (n/a)</td><td>768.83 (n/a)</td><td>123.02 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.34 <b>(-38.31%)</b></td><td>0.31 (-19.42%)</td><td>0.31 (-1.22%)</td><td>0.29 (+4.66%)</td><td>0.02 <b>(-82.55%)</b></td><td>4329.00 (-4.46%)</td><td>4025.78 (+14.94%)</td><td>3962.60 (+1.23%)</td><td>3655.90 <b>(+62.10%)</b></td><td>284.86 <b>(-72.55%)</b></td><td>18.36 <b>(-38.31%)</b></td><td>16.74 (-19.42%)</td><td>16.94 (-1.22%)</td><td>15.50 (+4.66%)</td><td>1.19 <b>(-82.55%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.55 (n/a)</td><td>0.39 (n/a)</td><td>0.32 (n/a)</td><td>0.27 (n/a)</td><td>0.13 (n/a)</td><td>4530.90 (n/a)</td><td>3502.38 (n/a)</td><td>3914.50 (n/a)</td><td>2255.30 (n/a)</td><td>1037.59 (n/a)</td><td>29.76 (n/a)</td><td>20.77 (n/a)</td><td>17.14 (n/a)</td><td>14.81 (n/a)</td><td>6.84 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>4.99 <b>(-24.30%)</b></td><td>4.53 (-7.76%)</td><td>4.75 (-1.22%)</td><td>3.42 (-6.16%)</td><td>0.64 <b>(-40.05%)</b></td><td>1945.40 (+6.57%)</td><td>1497.58 (+6.66%)</td><td>1399.90 (+1.24%)</td><td>1332.60 <b>(+32.10%)</b></td><td>254.19 (-12.44%)</td><td>1542.23 <b>(-24.30%)</b></td><td>1399.06 (-7.76%)</td><td>1468.15 (-1.22%)</td><td>1056.46 (-6.16%)</td><td>197.15 <b>(-40.05%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.59 (n/a)</td><td>4.91 (n/a)</td><td>4.81 (n/a)</td><td>3.64 (n/a)</td><td>1.06 (n/a)</td><td>1825.50 (n/a)</td><td>1404.06 (n/a)</td><td>1382.70 (n/a)</td><td>1008.80 (n/a)</td><td>290.28 (n/a)</td><td>2037.33 (n/a)</td><td>1516.82 (n/a)</td><td>1486.33 (n/a)</td><td>1125.84 (n/a)</td><td>328.87 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>13.44 (n/a)</td><td>13.12 (n/a)</td><td>13.32 (n/a)</td><td>12.17 (n/a)</td><td>0.53 (n/a)</td><td>13.43 (n/a)</td><td>13.11 (n/a)</td><td>13.31 (n/a)</td><td>12.16 (n/a)</td><td>0.53 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>25.12 (+0.23%)</td><td>24.64 (+6.21%)</td><td>24.81 (+2.36%)</td><td>24.06 <b>(+22.68%)</b></td><td>0.45 <b>(-79.66%)</b></td><td>25.10 (+0.23%)</td><td>24.63 (+6.21%)</td><td>24.79 (+2.36%)</td><td>24.05 <b>(+22.68%)</b></td><td>0.45 <b>(-79.66%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>25.06 (n/a)</td><td>23.20 (n/a)</td><td>24.24 (n/a)</td><td>19.62 (n/a)</td><td>2.19 (n/a)</td><td>25.04 (n/a)</td><td>23.19 (n/a)</td><td>24.22 (n/a)</td><td>19.60 (n/a)</td><td>2.19 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>41.63 (-3.08%)</td><td>40.06 (+0.88%)</td><td>39.80 (-3.07%)</td><td>39.11 <b>(+22.96%)</b></td><td>0.98 <b>(-78.09%)</b></td><td>41.60 (-3.08%)</td><td>40.04 (+0.88%)</td><td>39.77 (-3.07%)</td><td>39.08 <b>(+22.96%)</b></td><td>0.98 <b>(-78.09%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>42.95 (n/a)</td><td>39.71 (n/a)</td><td>41.06 (n/a)</td><td>31.81 (n/a)</td><td>4.49 (n/a)</td><td>42.93 (n/a)</td><td>39.69 (n/a)</td><td>41.03 (n/a)</td><td>31.79 (n/a)</td><td>4.48 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>46.99 (-3.13%)</td><td>42.49 (-5.04%)</td><td>41.84 (-4.05%)</td><td>39.71 (-8.00%)</td><td>2.98 <b>(+32.08%)</b></td><td>46.96 (-3.13%)</td><td>42.46 (-5.04%)</td><td>41.81 (-4.05%)</td><td>39.68 (-8.00%)</td><td>2.98 <b>(+32.08%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>48.51 (n/a)</td><td>44.74 (n/a)</td><td>43.60 (n/a)</td><td>43.16 (n/a)</td><td>2.26 (n/a)</td><td>48.48 (n/a)</td><td>44.72 (n/a)</td><td>43.57 (n/a)</td><td>43.13 (n/a)</td><td>2.26 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>13.52 (n/a)</td><td>12.62 (n/a)</td><td>13.41 (n/a)</td><td>11.03 (n/a)</td><td>1.17 (n/a)</td><td>13.51 (n/a)</td><td>12.62 (n/a)</td><td>13.40 (n/a)</td><td>11.03 (n/a)</td><td>1.17 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>25.14 (-1.07%)</td><td>24.63 (+3.87%)</td><td>24.66 (+4.16%)</td><td>23.99 (+8.40%)</td><td>0.44 <b>(-64.82%)</b></td><td>25.13 (-1.07%)</td><td>24.62 (+3.87%)</td><td>24.65 (+4.16%)</td><td>23.97 (+8.40%)</td><td>0.44 <b>(-64.82%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>25.41 (n/a)</td><td>23.71 (n/a)</td><td>23.68 (n/a)</td><td>22.13 (n/a)</td><td>1.25 (n/a)</td><td>25.40 (n/a)</td><td>23.70 (n/a)</td><td>23.66 (n/a)</td><td>22.11 (n/a)</td><td>1.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>41.96 (-2.49%)</td><td>40.84 (-0.81%)</td><td>41.19 (-1.27%)</td><td>38.99 (-0.36%)</td><td>1.17 <b>(-25.12%)</b></td><td>41.93 (-2.49%)</td><td>40.81 (-0.81%)</td><td>41.16 (-1.27%)</td><td>38.97 (-0.36%)</td><td>1.17 <b>(-25.12%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>43.03 (n/a)</td><td>41.17 (n/a)</td><td>41.72 (n/a)</td><td>39.13 (n/a)</td><td>1.56 (n/a)</td><td>43.00 (n/a)</td><td>41.14 (n/a)</td><td>41.69 (n/a)</td><td>39.11 (n/a)</td><td>1.56 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>45.86 (+6.92%)</td><td>44.44 (+10.30%)</td><td>44.88 (+8.18%)</td><td>41.96 <b>(+20.39%)</b></td><td>1.48 <b>(-54.74%)</b></td><td>45.83 (+6.92%)</td><td>44.42 (+10.30%)</td><td>44.85 (+8.18%)</td><td>41.93 <b>(+20.39%)</b></td><td>1.48 <b>(-54.74%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>42.89 (n/a)</td><td>40.29 (n/a)</td><td>41.48 (n/a)</td><td>34.85 (n/a)</td><td>3.27 (n/a)</td><td>42.86 (n/a)</td><td>40.27 (n/a)</td><td>41.46 (n/a)</td><td>34.83 (n/a)</td><td>3.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>10.00 (+5.43%)</td><td>9.04 (+0.72%)</td><td>9.10 (-0.63%)</td><td>8.02 (-3.99%)</td><td>0.72 <b>(+52.13%)</b></td><td>9.98 (+5.43%)</td><td>9.03 (+0.72%)</td><td>9.09 (-0.63%)</td><td>8.00 (-3.99%)</td><td>0.72 <b>(+52.13%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>9.49 (n/a)</td><td>8.98 (n/a)</td><td>9.16 (n/a)</td><td>8.35 (n/a)</td><td>0.47 (n/a)</td><td>9.47 (n/a)</td><td>8.96 (n/a)</td><td>9.14 (n/a)</td><td>8.34 (n/a)</td><td>0.47 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.07 (+1.24%)</td><td>0.98 (+2.40%)</td><td>0.94 (-2.34%)</td><td>0.89 (+8.89%)</td><td>0.09 (-1.84%)</td><td>1.05 (+1.24%)</td><td>0.96 (+2.40%)</td><td>0.92 (-2.34%)</td><td>0.87 (+8.89%)</td><td>0.09 (-1.84%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.06 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.81 (n/a)</td><td>0.09 (n/a)</td><td>1.04 (n/a)</td><td>0.94 (n/a)</td><td>0.94 (n/a)</td><td>0.80 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.40 (+6.03%)</td><td>1.26 (+4.74%)</td><td>1.28 (+5.09%)</td><td>1.13 (+2.65%)</td><td>0.11 <b>(+28.34%)</b></td><td>1.38 (+6.03%)</td><td>1.24 (+4.74%)</td><td>1.26 (+5.09%)</td><td>1.12 (+2.65%)</td><td>0.11 <b>(+28.35%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.32 (n/a)</td><td>1.20 (n/a)</td><td>1.21 (n/a)</td><td>1.10 (n/a)</td><td>0.09 (n/a)</td><td>1.30 (n/a)</td><td>1.19 (n/a)</td><td>1.20 (n/a)</td><td>1.09 (n/a)</td><td>0.09 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>19.62 (-2.22%)</td><td>17.53 (+1.88%)</td><td>18.50 (+11.10%)</td><td>13.28 (-16.85%)</td><td>2.57 <b>(+52.66%)</b></td><td>19.39 (-2.22%)</td><td>17.33 (+1.88%)</td><td>18.29 (+11.10%)</td><td>13.13 (-16.85%)</td><td>2.54 <b>(+52.66%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>20.07 (n/a)</td><td>17.21 (n/a)</td><td>16.65 (n/a)</td><td>15.98 (n/a)</td><td>1.69 (n/a)</td><td>19.83 (n/a)</td><td>17.01 (n/a)</td><td>16.46 (n/a)</td><td>15.79 (n/a)</td><td>1.67 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>14.13 (-2.85%)</td><td>13.69 (+3.49%)</td><td>13.64 (+3.16%)</td><td>13.33 (+12.69%)</td><td>0.31 <b>(-67.50%)</b></td><td>13.88 (-2.85%)</td><td>13.45 (+3.49%)</td><td>13.40 (+3.16%)</td><td>13.10 (+12.69%)</td><td>0.31 <b>(-67.50%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>14.55 (n/a)</td><td>13.23 (n/a)</td><td>13.22 (n/a)</td><td>11.83 (n/a)</td><td>0.96 (n/a)</td><td>14.29 (n/a)</td><td>12.99 (n/a)</td><td>12.99 (n/a)</td><td>11.62 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>9.54 (+5.45%)</td><td>8.04 (+3.67%)</td><td>7.48 (-1.54%)</td><td>6.29 (-11.01%)</td><td>1.40 <b>(+85.96%)</b></td><td>9.37 (+5.45%)</td><td>7.90 (+3.67%)</td><td>7.35 (-1.54%)</td><td>6.18 (-11.01%)</td><td>1.38 <b>(+85.96%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>9.04 (n/a)</td><td>7.76 (n/a)</td><td>7.60 (n/a)</td><td>7.07 (n/a)</td><td>0.76 (n/a)</td><td>8.89 (n/a)</td><td>7.62 (n/a)</td><td>7.47 (n/a)</td><td>6.94 (n/a)</td><td>0.74 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>6.90 (+2.46%)</td><td>6.27 (+3.77%)</td><td>6.21 (+5.36%)</td><td>5.46 (-0.33%)</td><td>0.60 (+17.27%)</td><td>6.79 (+2.46%)</td><td>6.17 (+3.77%)</td><td>6.11 (+5.36%)</td><td>5.38 (-0.33%)</td><td>0.59 (+17.27%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.73 (n/a)</td><td>6.04 (n/a)</td><td>5.89 (n/a)</td><td>5.48 (n/a)</td><td>0.51 (n/a)</td><td>6.63 (n/a)</td><td>5.95 (n/a)</td><td>5.80 (n/a)</td><td>5.39 (n/a)</td><td>0.51 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>13.15 (n/a)</td><td>12.11 (n/a)</td><td>12.65 (n/a)</td><td>10.74 (n/a)</td><td>1.14 (n/a)</td><td>13.14 (n/a)</td><td>12.10 (n/a)</td><td>12.65 (n/a)</td><td>10.73 (n/a)</td><td>1.14 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>13.16 (n/a)</td><td>11.85 (n/a)</td><td>11.45 (n/a)</td><td>11.01 (n/a)</td><td>0.93 (n/a)</td><td>13.15 (n/a)</td><td>11.84 (n/a)</td><td>11.45 (n/a)</td><td>11.00 (n/a)</td><td>0.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>164.56 (n/a)</td><td>155.20 (n/a)</td><td>131.90 (n/a)</td><td>34.76 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>269.80 (n/a)</td><td>165.38 (n/a)</td><td>150.40 (n/a)</td><td>105.30 (n/a)</td><td>62.46 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.80 (n/a)</td><td>154.00 (n/a)</td><td>138.30 (n/a)</td><td>111.20 (n/a)</td><td>37.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>335.20 (n/a)</td><td>203.64 (n/a)</td><td>172.10 (n/a)</td><td>129.30 (n/a)</td><td>80.75 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>175.30 (n/a)</td><td>150.68 (n/a)</td><td>157.50 (n/a)</td><td>112.10 (n/a)</td><td>24.64 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>275.50 (n/a)</td><td>195.62 (n/a)</td><td>160.70 (n/a)</td><td>127.60 (n/a)</td><td>71.14 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.50 (n/a)</td><td>184.50 (n/a)</td><td>171.90 (n/a)</td><td>146.50 (n/a)</td><td>37.10 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>255.10 (n/a)</td><td>223.76 (n/a)</td><td>222.70 (n/a)</td><td>199.10 (n/a)</td><td>20.76 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>197.20 (n/a)</td><td>176.98 (n/a)</td><td>179.30 (n/a)</td><td>148.70 (n/a)</td><td>21.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.80 (n/a)</td><td>165.18 (n/a)</td><td>160.70 (n/a)</td><td>132.00 (n/a)</td><td>28.81 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.20 (n/a)</td><td>169.42 (n/a)</td><td>173.40 (n/a)</td><td>149.90 (n/a)</td><td>11.28 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>252.90 (n/a)</td><td>190.74 (n/a)</td><td>181.60 (n/a)</td><td>153.30 (n/a)</td><td>37.67 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>171.20 (n/a)</td><td>151.80 (n/a)</td><td>149.60 (n/a)</td><td>135.30 (n/a)</td><td>13.83 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>285.00 (n/a)</td><td>194.46 (n/a)</td><td>186.80 (n/a)</td><td>152.20 (n/a)</td><td>53.21 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>292.40 (n/a)</td><td>202.80 (n/a)</td><td>184.00 (n/a)</td><td>158.70 (n/a)</td><td>53.59 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>319.80 (n/a)</td><td>229.52 (n/a)</td><td>198.70 (n/a)</td><td>139.40 (n/a)</td><td>80.42 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>157.50 (n/a)</td><td>139.18 (n/a)</td><td>148.10 (n/a)</td><td>100.00 (n/a)</td><td>22.81 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>169.54 (n/a)</td><td>168.80 (n/a)</td><td>139.90 (n/a)</td><td>24.33 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>285.00 (n/a)</td><td>167.04 (n/a)</td><td>139.10 (n/a)</td><td>116.80 (n/a)</td><td>68.07 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.70 (n/a)</td><td>158.82 (n/a)</td><td>159.90 (n/a)</td><td>129.60 (n/a)</td><td>29.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.90 (n/a)</td><td>167.78 (n/a)</td><td>174.80 (n/a)</td><td>134.60 (n/a)</td><td>23.13 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>186.30 (n/a)</td><td>166.30 (n/a)</td><td>163.90 (n/a)</td><td>150.60 (n/a)</td><td>15.69 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>284.50 (n/a)</td><td>211.82 (n/a)</td><td>196.20 (n/a)</td><td>140.10 (n/a)</td><td>54.49 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>334.00 (n/a)</td><td>279.72 (n/a)</td><td>293.70 (n/a)</td><td>206.90 (n/a)</td><td>54.54 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>231.40 (n/a)</td><td>180.08 (n/a)</td><td>180.20 (n/a)</td><td>142.70 (n/a)</td><td>33.39 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>173.70 (n/a)</td><td>143.86 (n/a)</td><td>137.00 (n/a)</td><td>105.20 (n/a)</td><td>29.07 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>195.40 (n/a)</td><td>157.80 (n/a)</td><td>144.10 (n/a)</td><td>135.90 (n/a)</td><td>26.23 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>235.90 (n/a)</td><td>179.76 (n/a)</td><td>176.10 (n/a)</td><td>138.70 (n/a)</td><td>37.00 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>244.70 (n/a)</td><td>185.42 (n/a)</td><td>184.60 (n/a)</td><td>146.20 (n/a)</td><td>37.34 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.32 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>234.10 (n/a)</td><td>176.26 (n/a)</td><td>175.50 (n/a)</td><td>102.30 (n/a)</td><td>47.94 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>273.30 (n/a)</td><td>170.84 (n/a)</td><td>163.10 (n/a)</td><td>111.30 (n/a)</td><td>61.81 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>261.00 (n/a)</td><td>198.54 (n/a)</td><td>182.90 (n/a)</td><td>171.50 (n/a)</td><td>36.26 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 <b>(-22.59%)</b></td><td>0.02 (-9.39%)</td><td>0.02 (+0.96%)</td><td>0.02 (-17.02%)</td><td>0.00 <b>(-29.91%)</b></td><td>232.60 <b>(+20.52%)</b></td><td>185.10 (+9.49%)</td><td>181.60 (-0.98%)</td><td>152.10 <b>(+29.12%)</b></td><td>33.62 (+8.80%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>169.06 (n/a)</td><td>183.40 (n/a)</td><td>117.80 (n/a)</td><td>30.91 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (+0.89%)</td><td>0.03 (-1.87%)</td><td>0.03 (-13.74%)</td><td>0.02 (+8.03%)</td><td>0.01 <b>(-22.94%)</b></td><td>217.50 (-7.45%)</td><td>154.50 (-1.09%)</td><td>145.00 (+15.91%)</td><td>117.20 (-0.93%)</td><td>37.68 <b>(-25.04%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.00 (n/a)</td><td>156.20 (n/a)</td><td>125.10 (n/a)</td><td>118.30 (n/a)</td><td>50.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (+12.79%)</td><td>0.03 (+3.36%)</td><td>0.03 (+4.11%)</td><td>0.02 (-7.42%)</td><td>0.00 <b>(+63.99%)</b></td><td>209.70 (+8.04%)</td><td>160.64 (-1.76%)</td><td>155.10 (-3.96%)</td><td>130.50 (-11.35%)</td><td>29.97 <b>(+60.41%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.10 (n/a)</td><td>163.52 (n/a)</td><td>161.50 (n/a)</td><td>147.20 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (+0.30%)</td><td>0.03 (+4.87%)</td><td>0.03 (+4.83%)</td><td>0.02 (+19.95%)</td><td>0.00 <b>(-31.25%)</b></td><td>171.10 (-16.62%)</td><td>155.30 (-5.87%)</td><td>158.00 (-4.59%)</td><td>130.30 (-0.31%)</td><td>15.04 <b>(-44.36%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.20 (n/a)</td><td>164.98 (n/a)</td><td>165.60 (n/a)</td><td>130.70 (n/a)</td><td>27.02 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-15.09%)</td><td>0.02 (-11.53%)</td><td>0.02 (-7.85%)</td><td>0.02 (-8.31%)</td><td>0.00 <b>(-38.28%)</b></td><td>200.70 (+9.08%)</td><td>171.46 (+12.09%)</td><td>165.00 (+8.48%)</td><td>152.80 (+17.72%)</td><td>18.11 (-18.57%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>184.00 (n/a)</td><td>152.96 (n/a)</td><td>152.10 (n/a)</td><td>129.80 (n/a)</td><td>22.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (+9.52%)</td><td>0.02 (+8.16%)</td><td>0.02 (-0.87%)</td><td>0.02 (+17.54%)</td><td>0.00 (+0.32%)</td><td>186.20 (-14.90%)</td><td>168.44 (-7.78%)</td><td>174.20 (+0.93%)</td><td>144.10 (-8.68%)</td><td>18.51 <b>(-22.38%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.80 (n/a)</td><td>182.66 (n/a)</td><td>172.60 (n/a)</td><td>157.80 (n/a)</td><td>23.85 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 <b>(-20.92%)</b></td><td>0.02 (-11.75%)</td><td>0.02 (-9.97%)</td><td>0.02 (+0.01%)</td><td>0.00 <b>(-66.66%)</b></td><td>198.60 (-0.05%)</td><td>188.36 (+11.18%)</td><td>191.50 (+11.08%)</td><td>169.10 <b>(+26.48%)</b></td><td>11.30 <b>(-58.85%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.70 (n/a)</td><td>169.42 (n/a)</td><td>172.40 (n/a)</td><td>133.70 (n/a)</td><td>27.47 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (-13.87%)</td><td>0.02 (-2.46%)</td><td>0.02 (-3.25%)</td><td>0.02 (+11.66%)</td><td>0.00 <b>(-78.55%)</b></td><td>226.40 (-10.44%)</td><td>216.96 (+1.42%)</td><td>215.20 (+3.36%)</td><td>211.50 (+16.08%)</td><td>5.75 <b>(-77.68%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>252.80 (n/a)</td><td>213.92 (n/a)</td><td>208.20 (n/a)</td><td>182.20 (n/a)</td><td>25.75 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (-5.79%)</td><td>0.05 (+3.77%)</td><td>0.05 (+5.79%)</td><td>0.05 (+2.25%)</td><td>0.01 (-19.29%)</td><td>177.40 (-2.21%)</td><td>153.74 (-4.25%)</td><td>158.90 (-5.47%)</td><td>127.50 (+6.16%)</td><td>20.38 (-13.76%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>181.40 (n/a)</td><td>160.56 (n/a)</td><td>168.10 (n/a)</td><td>120.10 (n/a)</td><td>23.64 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (-14.47%)</td><td>0.05 (-7.44%)</td><td>0.05 (+19.67%)</td><td>0.03 <b>(-22.00%)</b></td><td>0.01 (-15.49%)</td><td>311.60 <b>(+28.18%)</b></td><td>193.20 (+9.20%)</td><td>158.90 (-16.46%)</td><td>150.70 (+16.91%)</td><td>67.55 <b>(+39.13%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.10 (n/a)</td><td>176.92 (n/a)</td><td>190.20 (n/a)</td><td>128.90 (n/a)</td><td>48.55 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (+4.58%)</td><td>0.05 (-0.65%)</td><td>0.05 (-7.09%)</td><td>0.04 (-8.26%)</td><td>0.01 <b>(+24.02%)</b></td><td>233.50 (+9.01%)</td><td>176.38 (+2.89%)</td><td>180.10 (+7.65%)</td><td>115.10 (-4.40%)</td><td>45.56 <b>(+30.14%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>214.20 (n/a)</td><td>171.42 (n/a)</td><td>167.30 (n/a)</td><td>120.40 (n/a)</td><td>35.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (-8.46%)</td><td>0.05 (-8.07%)</td><td>0.05 (-10.57%)</td><td>0.05 (-1.06%)</td><td>0.01 <b>(-34.04%)</b></td><td>170.30 (+1.07%)</td><td>153.08 (+7.48%)</td><td>156.30 (+11.80%)</td><td>126.40 (+9.25%)</td><td>16.66 <b>(-29.51%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>168.50 (n/a)</td><td>142.42 (n/a)</td><td>139.80 (n/a)</td><td>115.70 (n/a)</td><td>23.64 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (-0.68%)</td><td>0.05 (+3.95%)</td><td>0.05 (+0.29%)</td><td>0.05 (+11.52%)</td><td>0.00 <b>(-39.10%)</b></td><td>169.30 (-10.38%)</td><td>154.22 (-4.91%)</td><td>156.20 (-0.32%)</td><td>137.10 (+0.73%)</td><td>12.85 <b>(-46.23%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.90 (n/a)</td><td>162.18 (n/a)</td><td>156.70 (n/a)</td><td>136.10 (n/a)</td><td>23.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (+7.55%)</td><td>0.05 (+10.38%)</td><td>0.06 (+12.41%)</td><td>0.04 (+12.81%)</td><td>0.01 (+11.27%)</td><td>200.30 (-11.33%)</td><td>158.32 (-9.41%)</td><td>148.90 (-11.05%)</td><td>134.60 (-7.04%)</td><td>27.68 (-11.18%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>174.76 (n/a)</td><td>167.40 (n/a)</td><td>144.80 (n/a)</td><td>31.17 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (+6.08%)</td><td>0.05 (-6.21%)</td><td>0.05 (-2.29%)</td><td>0.04 (-16.30%)</td><td>0.01 <b>(+149.12%)</b></td><td>212.40 (+19.53%)</td><td>181.60 (+8.39%)</td><td>171.60 (+2.33%)</td><td>147.40 (-5.75%)</td><td>28.09 <b>(+187.92%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.70 (n/a)</td><td>167.54 (n/a)</td><td>167.70 (n/a)</td><td>156.40 (n/a)</td><td>9.76 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (-0.63%)</td><td>0.05 (-2.08%)</td><td>0.05 (-7.94%)</td><td>0.04 (+12.92%)</td><td>0.01 <b>(-28.39%)</b></td><td>193.90 (-11.42%)</td><td>175.08 (+1.02%)</td><td>178.60 (+8.64%)</td><td>146.40 (+0.62%)</td><td>17.58 <b>(-38.46%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>218.90 (n/a)</td><td>173.32 (n/a)</td><td>164.40 (n/a)</td><td>145.50 (n/a)</td><td>28.56 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 <b>(+31.82%)</b></td><td>0.05 (+1.80%)</td><td>0.05 (-3.59%)</td><td>0.04 (-8.33%)</td><td>0.01 <b>(+153.01%)</b></td><td>219.10 (+9.11%)</td><td>174.28 (+2.30%)</td><td>170.50 (+3.71%)</td><td>115.70 <b>(-24.18%)</b></td><td>40.81 <b>(+108.73%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.80 (n/a)</td><td>170.36 (n/a)</td><td>164.40 (n/a)</td><td>152.60 (n/a)</td><td>19.55 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (-4.56%)</td><td>0.04 (+3.09%)</td><td>0.04 (+6.68%)</td><td>0.03 (+4.76%)</td><td>0.01 <b>(-29.19%)</b></td><td>297.20 (-4.53%)</td><td>219.82 (-6.32%)</td><td>195.80 (-6.27%)</td><td>179.80 (+4.78%)</td><td>48.92 <b>(-30.34%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>311.30 (n/a)</td><td>234.64 (n/a)</td><td>208.90 (n/a)</td><td>171.60 (n/a)</td><td>70.23 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (-17.18%)</td><td>0.11 (+0.96%)</td><td>0.12 (+16.17%)</td><td>0.08 (-7.78%)</td><td>0.02 <b>(-30.35%)</b></td><td>193.60 (+8.46%)</td><td>150.42 (-1.84%)</td><td>141.30 (-13.89%)</td><td>134.60 <b>(+20.72%)</b></td><td>24.70 (-5.27%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>178.50 (n/a)</td><td>153.24 (n/a)</td><td>164.10 (n/a)</td><td>111.50 (n/a)</td><td>26.08 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (-11.35%)</td><td>0.10 (-7.91%)</td><td>0.10 (-7.38%)</td><td>0.09 (-2.04%)</td><td>0.01 <b>(-28.65%)</b></td><td>188.70 (+2.11%)</td><td>164.04 (+7.57%)</td><td>168.90 (+7.99%)</td><td>136.60 (+12.80%)</td><td>21.15 (-17.45%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>184.80 (n/a)</td><td>152.50 (n/a)</td><td>156.40 (n/a)</td><td>121.10 (n/a)</td><td>25.63 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (-4.29%)</td><td>0.11 (+2.46%)</td><td>0.11 (-0.59%)</td><td>0.09 <b>(+28.61%)</b></td><td>0.02 <b>(-44.40%)</b></td><td>181.40 <b>(-22.25%)</b></td><td>153.48 (-6.69%)</td><td>144.20 (+0.63%)</td><td>131.20 (+4.46%)</td><td>22.41 <b>(-53.01%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>233.30 (n/a)</td><td>164.48 (n/a)</td><td>143.30 (n/a)</td><td>125.60 (n/a)</td><td>47.70 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (-11.42%)</td><td>0.09 <b>(-20.62%)</b></td><td>0.09 <b>(-25.31%)</b></td><td>0.06 <b>(-27.27%)</b></td><td>0.02 (-3.95%)</td><td>262.30 <b>(+37.47%)</b></td><td>190.58 <b>(+27.94%)</b></td><td>175.90 <b>(+33.87%)</b></td><td>134.80 (+12.90%)</td><td>50.28 <b>(+49.85%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>190.80 (n/a)</td><td>148.96 (n/a)</td><td>131.40 (n/a)</td><td>119.40 (n/a)</td><td>33.55 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 <b>(-22.32%)</b></td><td>0.10 (-17.61%)</td><td>0.10 (-16.18%)</td><td>0.09 (-13.42%)</td><td>0.00 <b>(-53.16%)</b></td><td>183.30 (+15.50%)</td><td>170.76 <b>(+20.88%)</b></td><td>167.40 (+19.32%)</td><td>161.90 <b>(+28.70%)</b></td><td>8.65 <b>(-30.28%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>158.70 (n/a)</td><td>141.26 (n/a)</td><td>140.30 (n/a)</td><td>125.80 (n/a)</td><td>12.40 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (-8.32%)</td><td>0.09 (-1.76%)</td><td>0.09 (-4.79%)</td><td>0.08 (+4.88%)</td><td>0.01 <b>(-44.89%)</b></td><td>206.50 (-4.66%)</td><td>181.10 (+0.43%)</td><td>178.90 (+4.99%)</td><td>163.50 (+9.07%)</td><td>16.26 <b>(-42.90%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>216.60 (n/a)</td><td>180.32 (n/a)</td><td>170.40 (n/a)</td><td>149.90 (n/a)</td><td>28.47 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 <b>(-28.05%)</b></td><td>0.08 <b>(-24.33%)</b></td><td>0.09 (-12.86%)</td><td>0.05 (-19.27%)</td><td>0.02 <b>(-37.68%)</b></td><td>306.90 <b>(+23.85%)</b></td><td>205.26 <b>(+29.32%)</b></td><td>177.60 (+14.73%)</td><td>161.80 <b>(+38.88%)</b></td><td>59.14 (+11.05%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>247.80 (n/a)</td><td>158.72 (n/a)</td><td>154.80 (n/a)</td><td>116.50 (n/a)</td><td>53.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (+0.06%)</td><td>0.08 (-8.42%)</td><td>0.07 (-17.16%)</td><td>0.07 (+8.33%)</td><td>0.01 (-19.32%)</td><td>240.40 (-7.68%)</td><td>213.20 (+8.16%)</td><td>219.40 <b>(+20.75%)</b></td><td>171.90 (-0.06%)</td><td>25.40 <b>(-29.55%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>260.40 (n/a)</td><td>197.12 (n/a)</td><td>181.70 (n/a)</td><td>172.00 (n/a)</td><td>36.06 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.28 (+6.96%)</td><td>0.21 (-3.63%)</td><td>0.21 (-13.67%)</td><td>0.11 (-6.05%)</td><td>0.06 (+3.47%)</td><td>306.10 (+6.43%)</td><td>174.26 (+4.84%)</td><td>152.90 (+15.83%)</td><td>118.10 (-6.49%)</td><td>75.37 (+9.14%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>287.60 (n/a)</td><td>166.22 (n/a)</td><td>132.00 (n/a)</td><td>126.30 (n/a)</td><td>69.06 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (-15.42%)</td><td>0.20 (-19.21%)</td><td>0.20 <b>(-21.17%)</b></td><td>0.17 <b>(-25.72%)</b></td><td>0.03 <b>(+33.71%)</b></td><td>197.40 <b>(+34.65%)</b></td><td>164.06 <b>(+25.05%)</b></td><td>165.60 <b>(+26.80%)</b></td><td>136.90 (+18.22%)</td><td>23.31 <b>(+113.33%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>146.60 (n/a)</td><td>131.20 (n/a)</td><td>130.60 (n/a)</td><td>115.80 (n/a)</td><td>10.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 <b>(-23.87%)</b></td><td>0.20 (-17.19%)</td><td>0.19 (-15.58%)</td><td>0.16 <b>(-27.27%)</b></td><td>0.03 <b>(-23.46%)</b></td><td>209.50 <b>(+37.47%)</b></td><td>169.18 <b>(+20.89%)</b></td><td>173.30 (+18.46%)</td><td>138.90 <b>(+31.29%)</b></td><td>27.17 <b>(+40.57%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.31 (n/a)</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>152.40 (n/a)</td><td>139.94 (n/a)</td><td>146.30 (n/a)</td><td>105.80 (n/a)</td><td>19.33 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (+19.26%)</td><td>0.22 (-0.94%)</td><td>0.19 (-11.41%)</td><td>0.17 <b>(-22.39%)</b></td><td>0.05 <b>(+1153.09%)</b></td><td>198.00 <b>(+28.82%)</b></td><td>157.72 (+4.60%)</td><td>169.40 (+12.93%)</td><td>123.80 (-16.12%)</td><td>32.65 <b>(+1173.91%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>153.70 (n/a)</td><td>150.78 (n/a)</td><td>150.00 (n/a)</td><td>147.60 (n/a)</td><td>2.56 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 <b>(-20.91%)</b></td><td>0.18 (-19.51%)</td><td>0.17 <b>(-21.24%)</b></td><td>0.16 (-17.44%)</td><td>0.02 <b>(-30.12%)</b></td><td>199.10 <b>(+21.11%)</b></td><td>184.36 <b>(+23.91%)</b></td><td>194.50 <b>(+26.96%)</b></td><td>159.90 <b>(+26.40%)</b></td><td>17.56 (+7.12%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>164.40 (n/a)</td><td>148.78 (n/a)</td><td>153.20 (n/a)</td><td>126.50 (n/a)</td><td>16.39 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (-6.22%)</td><td>0.19 (-13.64%)</td><td>0.18 <b>(-20.89%)</b></td><td>0.13 (-4.55%)</td><td>0.05 (-14.69%)</td><td>251.00 (+4.76%)</td><td>184.92 (+14.23%)</td><td>181.00 <b>(+26.40%)</b></td><td>126.10 (+6.59%)</td><td>44.44 (-7.90%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.14 (n/a)</td><td>0.05 (n/a)</td><td>239.60 (n/a)</td><td>161.88 (n/a)</td><td>143.20 (n/a)</td><td>118.30 (n/a)</td><td>48.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.18 (-3.74%)</td><td>0.15 (-14.72%)</td><td>0.15 (-12.08%)</td><td>0.10 <b>(-38.24%)</b></td><td>0.03 <b>(+211.50%)</b></td><td>317.20 <b>(+61.92%)</b></td><td>225.62 <b>(+21.50%)</b></td><td>217.00 (+13.73%)</td><td>179.40 (+3.88%)</td><td>53.69 <b>(+445.48%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>195.90 (n/a)</td><td>185.70 (n/a)</td><td>190.80 (n/a)</td><td>172.70 (n/a)</td><td>9.84 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 <b>(+21.03%)</b></td><td>0.03 (+7.99%)</td><td>0.03 (+18.61%)</td><td>0.02 <b>(-25.14%)</b></td><td>0.01 <b>(+316.47%)</b></td><td>212.00 <b>(+33.59%)</b></td><td>142.70 (-2.50%)</td><td>122.50 (-15.69%)</td><td>111.20 (-17.38%)</td><td>41.25 <b>(+367.84%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>158.70 (n/a)</td><td>146.36 (n/a)</td><td>145.30 (n/a)</td><td>134.60 (n/a)</td><td>8.82 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-3.26%)</td><td>0.03 (-1.40%)</td><td>0.03 (+3.50%)</td><td>0.02 <b>(-20.14%)</b></td><td>0.01 <b>(+34.00%)</b></td><td>212.70 <b>(+25.19%)</b></td><td>157.88 (+3.34%)</td><td>150.80 (-3.40%)</td><td>126.00 (+3.36%)</td><td>34.01 <b>(+77.37%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>169.90 (n/a)</td><td>152.78 (n/a)</td><td>156.10 (n/a)</td><td>121.90 (n/a)</td><td>19.17 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.00 (-0.00%)</td><td>0.00 (-0.00%)</td><td>0.00 (-0.00%)</td><td>0.00 (-0.00%)</td><td>0.00 <b>(+77.43%)</b></td><td>4746217.00 (+0.00%)</td><td>4746129.75 (+0.00%)</td><td>4746129.75 (+0.00%)</td><td>4746042.50 (+0.00%)</td><td>123.39 <b>(+77.92%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4746120.60 (n/a)</td><td>4746043.57 (n/a)</td><td>4746024.00 (n/a)</td><td>4745986.10 (n/a)</td><td>69.35 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 <b>(-26.01%)</b></td><td>0.02 <b>(-23.93%)</b></td><td>0.02 <b>(-20.87%)</b></td><td>0.01 <b>(-26.23%)</b></td><td>0.00 <b>(-23.13%)</b></td><td>297.10 <b>(+35.60%)</b></td><td>230.38 <b>(+31.74%)</b></td><td>222.60 <b>(+26.41%)</b></td><td>189.00 <b>(+35.10%)</b></td><td>43.50 <b>(+41.08%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>219.10 (n/a)</td><td>174.88 (n/a)</td><td>176.10 (n/a)</td><td>139.90 (n/a)</td><td>30.83 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-11.62%)</td><td>0.03 (-0.48%)</td><td>0.03 (+17.22%)</td><td>0.02 (+0.24%)</td><td>0.00 <b>(-20.37%)</b></td><td>198.50 (-0.25%)</td><td>164.04 (-0.26%)</td><td>147.00 (-14.68%)</td><td>142.90 (+13.14%)</td><td>26.13 (-10.08%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>199.00 (n/a)</td><td>164.46 (n/a)</td><td>172.30 (n/a)</td><td>126.30 (n/a)</td><td>29.06 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (+12.28%)</td><td>0.02 (+2.69%)</td><td>0.03 (+12.38%)</td><td>0.01 <b>(-40.72%)</b></td><td>0.01 <b>(+106.22%)</b></td><td>366.30 <b>(+68.72%)</b></td><td>201.20 (+8.50%)</td><td>158.90 (-11.03%)</td><td>132.30 (-10.91%)</td><td>95.45 <b>(+216.03%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>217.10 (n/a)</td><td>185.44 (n/a)</td><td>178.60 (n/a)</td><td>148.50 (n/a)</td><td>30.20 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-19.75%)</td><td>0.03 (-7.14%)</td><td>0.03 (+0.40%)</td><td>0.02 (-12.03%)</td><td>0.00 <b>(-34.12%)</b></td><td>194.80 (+13.65%)</td><td>157.24 (+6.03%)</td><td>158.40 (-0.38%)</td><td>121.50 <b>(+24.62%)</b></td><td>28.41 (-4.15%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>171.40 (n/a)</td><td>148.30 (n/a)</td><td>159.00 (n/a)</td><td>97.50 (n/a)</td><td>29.64 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-13.71%)</td><td>0.03 (+5.17%)</td><td>0.03 (+4.47%)</td><td>0.02 <b>(+23.62%)</b></td><td>0.00 <b>(-62.79%)</b></td><td>172.20 (-19.12%)</td><td>155.70 (-7.32%)</td><td>157.70 (-4.31%)</td><td>144.10 (+15.93%)</td><td>11.14 <b>(-64.80%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>212.90 (n/a)</td><td>168.00 (n/a)</td><td>164.80 (n/a)</td><td>124.30 (n/a)</td><td>31.64 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-14.02%)</td><td>0.02 (+0.38%)</td><td>0.02 (+1.58%)</td><td>0.02 (+1.57%)</td><td>0.00 <b>(-24.28%)</b></td><td>248.70 (-1.54%)</td><td>183.58 (-2.02%)</td><td>181.70 (-1.52%)</td><td>146.80 (+16.32%)</td><td>40.64 (-12.47%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>252.60 (n/a)</td><td>187.36 (n/a)</td><td>184.50 (n/a)</td><td>126.20 (n/a)</td><td>46.43 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (+12.14%)</td><td>0.02 (+10.31%)</td><td>0.02 (+10.82%)</td><td>0.02 (-2.01%)</td><td>0.00 <b>(+25.98%)</b></td><td>232.60 (+2.06%)</td><td>179.42 (-8.69%)</td><td>173.80 (-9.76%)</td><td>145.40 (-10.85%)</td><td>32.42 (+16.18%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.90 (n/a)</td><td>196.50 (n/a)</td><td>192.60 (n/a)</td><td>163.10 (n/a)</td><td>27.91 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 <b>(+33.22%)</b></td><td>0.03 (+10.47%)</td><td>0.02 (+0.97%)</td><td>0.02 (+15.74%)</td><td>0.00 <b>(+79.52%)</b></td><td>192.70 (-13.59%)</td><td>164.38 (-8.31%)</td><td>169.40 (-0.94%)</td><td>121.40 <b>(-24.92%)</b></td><td>27.52 (+11.06%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.00 (n/a)</td><td>179.28 (n/a)</td><td>171.00 (n/a)</td><td>161.70 (n/a)</td><td>24.78 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 <b>(-21.64%)</b></td><td>0.02 (-2.19%)</td><td>0.02 (-5.83%)</td><td>0.02 <b>(+25.88%)</b></td><td>0.00 <b>(-70.62%)</b></td><td>183.50 <b>(-20.56%)</b></td><td>172.24 (-1.82%)</td><td>176.10 (+6.15%)</td><td>156.70 <b>(+27.61%)</b></td><td>12.18 <b>(-70.02%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.00 (n/a)</td><td>175.44 (n/a)</td><td>165.90 (n/a)</td><td>122.80 (n/a)</td><td>40.62 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-9.90%)</td><td>0.02 (-6.75%)</td><td>0.02 (+8.39%)</td><td>0.01 <b>(-32.13%)</b></td><td>0.01 <b>(+39.91%)</b></td><td>321.50 <b>(+47.34%)</b></td><td>207.60 (+14.57%)</td><td>171.20 (-7.71%)</td><td>143.50 (+10.98%)</td><td>76.61 <b>(+135.12%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>218.20 (n/a)</td><td>181.20 (n/a)</td><td>185.50 (n/a)</td><td>129.30 (n/a)</td><td>32.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-8.46%)</td><td>0.02 (-8.84%)</td><td>0.02 (-4.70%)</td><td>0.02 (-13.25%)</td><td>0.00 (-4.42%)</td><td>232.70 (+15.26%)</td><td>187.10 (+10.11%)</td><td>180.90 (+4.93%)</td><td>139.80 (+9.22%)</td><td>36.11 <b>(+20.32%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.90 (n/a)</td><td>169.92 (n/a)</td><td>172.40 (n/a)</td><td>128.00 (n/a)</td><td>30.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-18.73%)</td><td>0.02 (-3.61%)</td><td>0.02 (+5.94%)</td><td>0.02 (+3.61%)</td><td>0.00 <b>(-55.54%)</b></td><td>198.40 (-3.50%)</td><td>179.88 (+0.95%)</td><td>180.30 (-5.60%)</td><td>152.50 <b>(+22.98%)</b></td><td>17.91 <b>(-47.31%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>178.18 (n/a)</td><td>191.00 (n/a)</td><td>124.00 (n/a)</td><td>33.99 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-13.77%)</td><td>0.02 (-13.71%)</td><td>0.02 (-11.00%)</td><td>0.02 (-0.68%)</td><td>0.00 <b>(-34.54%)</b></td><td>237.50 (+0.72%)</td><td>194.54 (+12.72%)</td><td>181.10 (+12.34%)</td><td>148.80 (+15.98%)</td><td>39.90 (-17.67%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>235.80 (n/a)</td><td>172.58 (n/a)</td><td>161.20 (n/a)</td><td>128.30 (n/a)</td><td>48.47 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 <b>(+20.75%)</b></td><td>0.05 (+2.59%)</td><td>0.05 (-4.54%)</td><td>0.05 (+4.09%)</td><td>0.01 <b>(+96.45%)</b></td><td>178.40 (-3.93%)</td><td>162.40 (-1.54%)</td><td>171.10 (+4.78%)</td><td>127.20 (-17.19%)</td><td>20.31 <b>(+53.45%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.70 (n/a)</td><td>164.94 (n/a)</td><td>163.30 (n/a)</td><td>153.60 (n/a)</td><td>13.23 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (+7.96%)</td><td>0.05 (+6.35%)</td><td>0.05 (+6.87%)</td><td>0.04 <b>(+31.51%)</b></td><td>0.01 <b>(-24.09%)</b></td><td>194.60 <b>(-23.95%)</b></td><td>161.18 (-9.61%)</td><td>164.20 (-6.44%)</td><td>117.20 (-7.42%)</td><td>28.08 <b>(-46.92%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>255.90 (n/a)</td><td>178.32 (n/a)</td><td>175.50 (n/a)</td><td>126.60 (n/a)</td><td>52.91 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (-15.22%)</td><td>0.04 (-12.23%)</td><td>0.04 (+1.11%)</td><td>0.02 <b>(-31.66%)</b></td><td>0.01 <b>(+29.49%)</b></td><td>327.80 <b>(+46.34%)</b></td><td>237.88 (+16.20%)</td><td>214.20 (-1.11%)</td><td>205.30 (+17.92%)</td><td>51.25 <b>(+126.61%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>224.00 (n/a)</td><td>204.72 (n/a)</td><td>216.60 (n/a)</td><td>174.10 (n/a)</td><td>22.61 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 <b>(+21.90%)</b></td><td>0.04 (+5.95%)</td><td>0.05 (+15.86%)</td><td>0.03 (-12.46%)</td><td>0.01 <b>(+229.95%)</b></td><td>235.40 (+14.22%)</td><td>187.86 (-2.99%)</td><td>171.90 (-13.70%)</td><td>148.10 (-18.00%)</td><td>37.18 <b>(+218.54%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>206.10 (n/a)</td><td>193.66 (n/a)</td><td>199.20 (n/a)</td><td>180.60 (n/a)</td><td>11.67 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (-13.79%)</td><td>0.05 (-5.46%)</td><td>0.05 (-8.97%)</td><td>0.05 (-2.49%)</td><td>0.01 <b>(-34.93%)</b></td><td>179.40 (+2.57%)</td><td>158.62 (+4.63%)</td><td>165.10 (+9.85%)</td><td>133.10 (+16.04%)</td><td>18.45 <b>(-22.70%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>174.90 (n/a)</td><td>151.60 (n/a)</td><td>150.30 (n/a)</td><td>114.70 (n/a)</td><td>23.87 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 <b>(+32.94%)</b></td><td>0.06 <b>(+24.39%)</b></td><td>0.06 <b>(+31.31%)</b></td><td>0.04 (+10.84%)</td><td>0.01 <b>(+131.53%)</b></td><td>183.60 (-9.78%)</td><td>143.84 (-17.60%)</td><td>133.20 <b>(-23.84%)</b></td><td>113.30 <b>(-24.77%)</b></td><td>30.22 <b>(+57.55%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.50 (n/a)</td><td>174.56 (n/a)</td><td>174.90 (n/a)</td><td>150.60 (n/a)</td><td>19.18 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 <b>(+25.86%)</b></td><td>0.05 (+16.74%)</td><td>0.05 (+15.77%)</td><td>0.04 (+1.96%)</td><td>0.01 <b>(+120.22%)</b></td><td>202.80 (-1.89%)</td><td>162.84 (-12.95%)</td><td>164.10 (-13.63%)</td><td>130.30 <b>(-20.50%)</b></td><td>27.08 <b>(+73.50%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>206.70 (n/a)</td><td>187.06 (n/a)</td><td>190.00 (n/a)</td><td>163.90 (n/a)</td><td>15.61 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (+11.54%)</td><td>0.05 (+1.77%)</td><td>0.04 (-1.64%)</td><td>0.04 (-18.79%)</td><td>0.01 <b>(+79.34%)</b></td><td>233.10 <b>(+23.14%)</b></td><td>176.82 (+1.13%)</td><td>182.50 (+1.61%)</td><td>125.90 (-10.39%)</td><td>39.33 <b>(+99.97%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.30 (n/a)</td><td>174.84 (n/a)</td><td>179.60 (n/a)</td><td>140.50 (n/a)</td><td>19.67 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (+13.97%)</td><td>0.04 (-3.10%)</td><td>0.04 (-5.59%)</td><td>0.03 (-19.72%)</td><td>0.01 <b>(+105.82%)</b></td><td>259.00 <b>(+24.58%)</b></td><td>200.50 (+6.58%)</td><td>204.80 (+5.89%)</td><td>137.20 (-12.22%)</td><td>43.32 <b>(+121.05%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>207.90 (n/a)</td><td>188.12 (n/a)</td><td>193.40 (n/a)</td><td>156.30 (n/a)</td><td>19.60 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (+4.27%)</td><td>0.05 (+1.59%)</td><td>0.05 (+2.89%)</td><td>0.04 (+6.37%)</td><td>0.01 (-8.82%)</td><td>217.30 (-6.01%)</td><td>178.98 (-2.10%)</td><td>179.10 (-2.82%)</td><td>147.60 (-4.16%)</td><td>26.31 (-16.24%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>231.20 (n/a)</td><td>182.82 (n/a)</td><td>184.30 (n/a)</td><td>154.00 (n/a)</td><td>31.41 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (-15.45%)</td><td>0.04 (-9.38%)</td><td>0.04 (-11.53%)</td><td>0.04 (-1.64%)</td><td>0.01 <b>(-40.12%)</b></td><td>207.00 (+1.67%)</td><td>185.56 (+8.71%)</td><td>187.30 (+13.04%)</td><td>151.40 (+18.28%)</td><td>20.91 <b>(-29.57%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>203.60 (n/a)</td><td>170.70 (n/a)</td><td>165.70 (n/a)</td><td>128.00 (n/a)</td><td>29.69 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (-13.39%)</td><td>0.04 (-14.81%)</td><td>0.04 (-17.19%)</td><td>0.04 (-8.30%)</td><td>0.01 <b>(-26.66%)</b></td><td>230.40 (+9.04%)</td><td>199.32 (+16.66%)</td><td>193.90 <b>(+20.73%)</b></td><td>167.80 (+15.41%)</td><td>25.40 (-6.80%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>170.86 (n/a)</td><td>160.60 (n/a)</td><td>145.40 (n/a)</td><td>27.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 <b>(-20.44%)</b></td><td>0.04 (-11.78%)</td><td>0.04 <b>(-21.46%)</b></td><td>0.04 (+10.92%)</td><td>0.01 <b>(-55.48%)</b></td><td>222.40 (-9.85%)</td><td>196.00 (+8.95%)</td><td>201.90 <b>(+27.30%)</b></td><td>163.10 <b>(+25.75%)</b></td><td>22.90 <b>(-50.90%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>246.70 (n/a)</td><td>179.90 (n/a)</td><td>158.60 (n/a)</td><td>129.70 (n/a)</td><td>46.64 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (-6.02%)</td><td>0.05 (-7.56%)</td><td>0.04 (-1.37%)</td><td>0.02 <b>(-40.55%)</b></td><td>0.02 <b>(+23.27%)</b></td><td>348.10 <b>(+68.25%)</b></td><td>203.56 (+16.45%)</td><td>188.20 (+1.35%)</td><td>122.30 (+6.35%)</td><td>85.72 <b>(+145.17%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>206.90 (n/a)</td><td>174.80 (n/a)</td><td>185.70 (n/a)</td><td>115.00 (n/a)</td><td>34.96 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (-17.71%)</td><td>0.04 (-6.25%)</td><td>0.04 (-8.93%)</td><td>0.03 (+13.20%)</td><td>0.01 <b>(-29.59%)</b></td><td>266.20 (-11.65%)</td><td>210.68 (+2.97%)</td><td>229.60 (+9.80%)</td><td>155.80 <b>(+21.53%)</b></td><td>47.39 <b>(-26.06%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>301.30 (n/a)</td><td>204.60 (n/a)</td><td>209.10 (n/a)</td><td>128.20 (n/a)</td><td>64.09 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (+2.57%)</td><td>0.04 (-9.25%)</td><td>0.04 (-16.02%)</td><td>0.03 (-8.11%)</td><td>0.01 <b>(+30.32%)</b></td><td>239.00 (+8.83%)</td><td>195.46 (+11.97%)</td><td>199.30 (+19.06%)</td><td>136.10 (-2.51%)</td><td>39.59 <b>(+34.17%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.60 (n/a)</td><td>174.56 (n/a)</td><td>167.40 (n/a)</td><td>139.60 (n/a)</td><td>29.51 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (+14.72%)</td><td>0.10 (-2.40%)</td><td>0.10 (+2.78%)</td><td>0.07 (-16.98%)</td><td>0.02 <b>(+243.30%)</b></td><td>220.70 <b>(+20.47%)</b></td><td>176.84 (+5.40%)</td><td>162.70 (-2.69%)</td><td>137.40 (-12.82%)</td><td>34.85 <b>(+265.55%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>183.20 (n/a)</td><td>167.78 (n/a)</td><td>167.20 (n/a)</td><td>157.60 (n/a)</td><td>9.53 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (+3.38%)</td><td>0.10 (+0.15%)</td><td>0.10 (+3.71%)</td><td>0.07 (-11.70%)</td><td>0.02 (+11.20%)</td><td>240.50 (+13.23%)</td><td>176.26 (+0.81%)</td><td>167.00 (-3.58%)</td><td>132.30 (-3.29%)</td><td>39.69 <b>(+24.09%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>174.84 (n/a)</td><td>173.20 (n/a)</td><td>136.80 (n/a)</td><td>31.99 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (+10.70%)</td><td>0.08 (-4.70%)</td><td>0.07 (-10.42%)</td><td>0.06 (-14.49%)</td><td>0.02 <b>(+127.35%)</b></td><td>265.40 (+16.97%)</td><td>215.98 (+8.98%)</td><td>223.50 (+11.64%)</td><td>154.70 (-9.69%)</td><td>50.01 <b>(+145.41%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>226.90 (n/a)</td><td>198.18 (n/a)</td><td>200.20 (n/a)</td><td>171.30 (n/a)</td><td>20.38 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (-12.28%)</td><td>0.08 (-14.22%)</td><td>0.08 (-16.91%)</td><td>0.07 (-2.99%)</td><td>0.01 <b>(-29.32%)</b></td><td>230.70 (+3.13%)</td><td>207.56 (+15.92%)</td><td>205.10 <b>(+20.36%)</b></td><td>185.50 (+14.01%)</td><td>20.68 (-18.18%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>179.06 (n/a)</td><td>170.40 (n/a)</td><td>162.70 (n/a)</td><td>25.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (+19.73%)</td><td>0.11 (+16.83%)</td><td>0.10 (+2.84%)</td><td>0.09 <b>(+67.92%)</b></td><td>0.02 <b>(-21.23%)</b></td><td>181.00 <b>(-40.44%)</b></td><td>154.16 (-18.81%)</td><td>165.90 (-2.75%)</td><td>117.30 (-16.51%)</td><td>25.33 <b>(-62.00%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>303.90 (n/a)</td><td>189.88 (n/a)</td><td>170.60 (n/a)</td><td>140.50 (n/a)</td><td>66.66 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (-2.44%)</td><td>0.11 (-1.78%)</td><td>0.10 (-8.08%)</td><td>0.09 (-1.39%)</td><td>0.01 (-6.87%)</td><td>178.90 (+1.42%)</td><td>155.52 (+1.58%)</td><td>159.60 (+8.79%)</td><td>132.00 (+2.48%)</td><td>20.40 (-6.77%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>176.40 (n/a)</td><td>153.10 (n/a)</td><td>146.70 (n/a)</td><td>128.80 (n/a)</td><td>21.89 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 <b>(-31.97%)</b></td><td>0.08 (-19.29%)</td><td>0.09 (-4.86%)</td><td>0.06 <b>(-23.02%)</b></td><td>0.01 <b>(-53.35%)</b></td><td>277.70 <b>(+29.95%)</b></td><td>203.14 (+19.23%)</td><td>191.80 (+5.10%)</td><td>167.70 <b>(+46.98%)</b></td><td>42.89 (-8.57%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>213.70 (n/a)</td><td>170.38 (n/a)</td><td>182.50 (n/a)</td><td>114.10 (n/a)</td><td>46.91 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (-19.28%)</td><td>0.10 (+1.66%)</td><td>0.10 (+7.12%)</td><td>0.09 <b>(+21.95%)</b></td><td>0.02 <b>(-51.34%)</b></td><td>188.50 (-18.01%)</td><td>161.92 (-6.11%)</td><td>168.30 (-6.60%)</td><td>131.90 <b>(+23.85%)</b></td><td>22.88 <b>(-48.34%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>229.90 (n/a)</td><td>172.46 (n/a)</td><td>180.20 (n/a)</td><td>106.50 (n/a)</td><td>44.29 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.13 <b>(+34.75%)</b></td><td>0.09 (+6.99%)</td><td>0.08 (+0.15%)</td><td>0.07 (-2.51%)</td><td>0.02 <b>(+115.28%)</b></td><td>235.00 (+2.58%)</td><td>195.26 (-3.30%)</td><td>211.80 (-0.14%)</td><td>128.10 <b>(-25.78%)</b></td><td>42.91 <b>(+63.74%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.10 (n/a)</td><td>201.92 (n/a)</td><td>212.10 (n/a)</td><td>172.60 (n/a)</td><td>26.21 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (-10.76%)</td><td>0.09 (-15.66%)</td><td>0.09 (-19.96%)</td><td>0.07 (-11.54%)</td><td>0.02 (-11.37%)</td><td>238.70 (+13.02%)</td><td>192.88 (+18.48%)</td><td>186.40 <b>(+24.93%)</b></td><td>147.00 (+12.04%)</td><td>34.65 (+10.32%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.20 (n/a)</td><td>162.80 (n/a)</td><td>149.20 (n/a)</td><td>131.20 (n/a)</td><td>31.41 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.13 (-11.56%)</td><td>0.09 <b>(-22.30%)</b></td><td>0.09 (-19.96%)</td><td>0.05 <b>(-46.74%)</b></td><td>0.03 <b>(+42.34%)</b></td><td>328.00 <b>(+87.75%)</b></td><td>200.84 <b>(+38.36%)</b></td><td>185.80 <b>(+24.95%)</b></td><td>125.70 (+13.14%)</td><td>75.47 <b>(+224.55%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>174.70 (n/a)</td><td>145.16 (n/a)</td><td>148.70 (n/a)</td><td>111.10 (n/a)</td><td>23.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 <b>(-29.77%)</b></td><td>0.09 (-16.66%)</td><td>0.09 (-5.00%)</td><td>0.08 (-5.06%)</td><td>0.01 <b>(-73.44%)</b></td><td>193.20 (+5.34%)</td><td>174.40 (+15.76%)</td><td>177.10 (+5.29%)</td><td>161.50 <b>(+42.29%)</b></td><td>13.06 <b>(-59.63%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>183.40 (n/a)</td><td>150.66 (n/a)</td><td>168.20 (n/a)</td><td>113.50 (n/a)</td><td>32.36 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.13 (+1.98%)</td><td>0.10 (+4.18%)</td><td>0.10 (+3.68%)</td><td>0.08 (+15.42%)</td><td>0.02 (-7.24%)</td><td>212.00 (-13.36%)</td><td>174.26 (-5.08%)</td><td>170.30 (-3.57%)</td><td>129.60 (-1.97%)</td><td>35.18 (-19.49%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>244.70 (n/a)</td><td>183.58 (n/a)</td><td>176.60 (n/a)</td><td>132.20 (n/a)</td><td>43.70 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (+12.57%)</td><td>0.09 (+0.59%)</td><td>0.08 (-2.03%)</td><td>0.07 (-6.30%)</td><td>0.02 <b>(+85.96%)</b></td><td>222.30 (+6.72%)</td><td>189.72 (+1.08%)</td><td>194.70 (+2.04%)</td><td>142.20 (-11.13%)</td><td>30.81 <b>(+76.30%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>208.30 (n/a)</td><td>187.70 (n/a)</td><td>190.80 (n/a)</td><td>160.00 (n/a)</td><td>17.48 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (+9.13%)</td><td>0.09 (-2.60%)</td><td>0.10 (-2.19%)</td><td>0.07 (-17.22%)</td><td>0.02 <b>(+69.59%)</b></td><td>244.30 <b>(+20.82%)</b></td><td>180.86 (+5.38%)</td><td>163.70 (+2.25%)</td><td>141.30 (-8.37%)</td><td>41.40 <b>(+92.04%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>202.20 (n/a)</td><td>171.62 (n/a)</td><td>160.10 (n/a)</td><td>154.20 (n/a)</td><td>21.56 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (+1.82%)</td><td>0.09 (-0.57%)</td><td>0.09 (+7.83%)</td><td>0.07 (-9.38%)</td><td>0.01 (+18.41%)</td><td>240.20 (+10.34%)</td><td>191.04 (+1.39%)</td><td>179.00 (-7.25%)</td><td>152.60 (-1.80%)</td><td>33.37 <b>(+30.11%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>217.70 (n/a)</td><td>188.42 (n/a)</td><td>193.00 (n/a)</td><td>155.40 (n/a)</td><td>25.65 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.25 (-1.11%)</td><td>0.18 (-13.17%)</td><td>0.17 <b>(-20.81%)</b></td><td>0.14 <b>(-20.53%)</b></td><td>0.05 <b>(+42.43%)</b></td><td>240.90 <b>(+25.80%)</b></td><td>189.24 (+18.36%)</td><td>195.10 <b>(+26.28%)</b></td><td>128.60 (+1.18%)</td><td>42.60 <b>(+78.10%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>191.50 (n/a)</td><td>159.88 (n/a)</td><td>154.50 (n/a)</td><td>127.10 (n/a)</td><td>23.92 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.23 <b>(-23.33%)</b></td><td>0.18 <b>(-24.74%)</b></td><td>0.19 (-16.33%)</td><td>0.13 <b>(-28.92%)</b></td><td>0.04 <b>(-28.32%)</b></td><td>248.20 <b>(+40.70%)</b></td><td>185.78 <b>(+32.72%)</b></td><td>169.90 (+19.48%)</td><td>140.40 <b>(+30.36%)</b></td><td>41.29 <b>(+36.64%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>176.40 (n/a)</td><td>139.98 (n/a)</td><td>142.20 (n/a)</td><td>107.70 (n/a)</td><td>30.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.21 (-0.38%)</td><td>0.18 (+12.70%)</td><td>0.19 <b>(+22.12%)</b></td><td>0.15 (+6.36%)</td><td>0.02 (-18.02%)</td><td>217.50 (-5.97%)</td><td>182.42 (-11.88%)</td><td>172.70 (-18.15%)</td><td>157.30 (+0.38%)</td><td>23.82 <b>(-20.70%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>231.30 (n/a)</td><td>207.02 (n/a)</td><td>211.00 (n/a)</td><td>156.70 (n/a)</td><td>30.03 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.22 (+14.58%)</td><td>0.20 <b>(+20.71%)</b></td><td>0.20 <b>(+22.68%)</b></td><td>0.18 <b>(+28.18%)</b></td><td>0.02 (-16.53%)</td><td>185.60 <b>(-22.02%)</b></td><td>165.76 (-17.72%)</td><td>166.90 (-18.47%)</td><td>147.30 (-12.74%)</td><td>14.56 <b>(-43.24%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>238.00 (n/a)</td><td>201.46 (n/a)</td><td>204.70 (n/a)</td><td>168.80 (n/a)</td><td>25.66 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.21 <b>(-40.59%)</b></td><td>0.19 (-15.02%)</td><td>0.20 (-7.79%)</td><td>0.14 (+14.13%)</td><td>0.03 <b>(-64.46%)</b></td><td>237.90 (-12.38%)</td><td>178.00 (+7.70%)</td><td>162.00 (+8.43%)</td><td>159.70 <b>(+68.28%)</b></td><td>33.67 <b>(-48.10%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.35 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>271.50 (n/a)</td><td>165.28 (n/a)</td><td>149.40 (n/a)</td><td>94.90 (n/a)</td><td>64.87 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.21 <b>(-26.22%)</b></td><td>0.20 (-14.26%)</td><td>0.20 (-15.82%)</td><td>0.20 (-0.55%)</td><td>0.00 <b>(-88.23%)</b></td><td>164.80 (+0.55%)</td><td>160.94 (+14.63%)</td><td>159.90 (+18.80%)</td><td>157.10 <b>(+35.55%)</b></td><td>3.25 <b>(-84.35%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>163.90 (n/a)</td><td>140.40 (n/a)</td><td>134.60 (n/a)</td><td>115.90 (n/a)</td><td>20.78 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.25 (-3.36%)</td><td>0.21 (+2.59%)</td><td>0.22 (+2.70%)</td><td>0.11 (+4.97%)</td><td>0.06 (-12.92%)</td><td>292.10 (-4.73%)</td><td>174.14 (-4.77%)</td><td>150.70 (-2.65%)</td><td>128.60 (+3.54%)</td><td>68.05 (-10.61%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>306.60 (n/a)</td><td>182.86 (n/a)</td><td>154.80 (n/a)</td><td>124.20 (n/a)</td><td>76.13 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.25 <b>(-25.60%)</b></td><td>0.21 (-9.78%)</td><td>0.21 (-6.37%)</td><td>0.19 <b>(+25.85%)</b></td><td>0.02 <b>(-71.40%)</b></td><td>176.20 <b>(-20.56%)</b></td><td>154.14 (+0.00%)</td><td>153.30 (+6.75%)</td><td>129.00 <b>(+34.38%)</b></td><td>17.13 <b>(-70.01%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>221.80 (n/a)</td><td>154.14 (n/a)</td><td>143.60 (n/a)</td><td>96.00 (n/a)</td><td>57.10 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (+2.34%)</td><td>0.17 (-6.77%)</td><td>0.18 (-0.36%)</td><td>0.09 <b>(-36.97%)</b></td><td>0.06 <b>(+47.86%)</b></td><td>376.00 <b>(+58.65%)</b></td><td>214.30 (+17.32%)</td><td>180.60 (+0.39%)</td><td>126.70 (-2.24%)</td><td>95.59 <b>(+147.20%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>237.00 (n/a)</td><td>182.66 (n/a)</td><td>179.90 (n/a)</td><td>129.60 (n/a)</td><td>38.67 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (+9.52%)</td><td>0.22 (+5.33%)</td><td>0.21 (-1.60%)</td><td>0.20 (+14.49%)</td><td>0.02 (+7.73%)</td><td>160.40 (-12.64%)</td><td>148.98 (-5.13%)</td><td>156.40 (+1.62%)</td><td>125.30 (-8.67%)</td><td>14.49 (-15.29%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>183.60 (n/a)</td><td>157.04 (n/a)</td><td>153.90 (n/a)</td><td>137.20 (n/a)</td><td>17.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (+3.93%)</td><td>0.21 (+9.69%)</td><td>0.21 (+2.70%)</td><td>0.18 <b>(+24.40%)</b></td><td>0.03 <b>(-30.99%)</b></td><td>180.20 (-19.63%)</td><td>156.42 (-11.61%)</td><td>156.90 (-2.67%)</td><td>125.30 (-3.84%)</td><td>22.22 <b>(-48.84%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>224.20 (n/a)</td><td>176.96 (n/a)</td><td>161.20 (n/a)</td><td>130.30 (n/a)</td><td>43.44 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.25 (-3.48%)</td><td>0.21 (+3.15%)</td><td>0.22 (+8.46%)</td><td>0.18 (+13.23%)</td><td>0.03 <b>(-29.22%)</b></td><td>182.20 (-11.68%)</td><td>154.64 (-4.40%)</td><td>146.10 (-7.77%)</td><td>133.70 (+3.56%)</td><td>19.49 <b>(-34.90%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>206.30 (n/a)</td><td>161.76 (n/a)</td><td>158.40 (n/a)</td><td>129.10 (n/a)</td><td>29.94 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 (-4.89%)</td><td>0.18 (-9.48%)</td><td>0.18 (-8.56%)</td><td>0.16 (-13.91%)</td><td>0.02 <b>(+58.27%)</b></td><td>208.40 (+16.16%)</td><td>183.80 (+11.02%)</td><td>181.20 (+9.42%)</td><td>165.20 (+5.16%)</td><td>17.56 <b>(+93.63%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.01 (n/a)</td><td>179.40 (n/a)</td><td>165.56 (n/a)</td><td>165.60 (n/a)</td><td>157.10 (n/a)</td><td>9.07 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 <b>(-25.13%)</b></td><td>0.18 (-9.93%)</td><td>0.18 (-5.17%)</td><td>0.16 (+7.88%)</td><td>0.01 <b>(-70.74%)</b></td><td>202.60 (-7.28%)</td><td>181.10 (+7.24%)</td><td>179.10 (+5.48%)</td><td>164.80 <b>(+33.55%)</b></td><td>13.59 <b>(-63.12%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>218.50 (n/a)</td><td>168.88 (n/a)</td><td>169.80 (n/a)</td><td>123.40 (n/a)</td><td>36.85 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 <b>(+39.24%)</b></td><td>0.20 (+19.01%)</td><td>0.20 <b>(+20.28%)</b></td><td>0.16 (+7.87%)</td><td>0.04 <b>(+134.35%)</b></td><td>205.90 (-7.29%)</td><td>167.44 (-14.35%)</td><td>160.00 (-16.88%)</td><td>127.90 <b>(-28.15%)</b></td><td>29.79 <b>(+57.81%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>222.10 (n/a)</td><td>195.50 (n/a)</td><td>192.50 (n/a)</td><td>178.00 (n/a)</td><td>18.87 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 <b>(+21.63%)</b></td><td>0.22 <b>(+20.83%)</b></td><td>0.22 (+15.79%)</td><td>0.18 <b>(+20.14%)</b></td><td>0.03 (+12.35%)</td><td>180.00 (-16.78%)</td><td>151.24 (-17.41%)</td><td>148.00 (-13.65%)</td><td>128.10 (-17.78%)</td><td>18.94 <b>(-23.35%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>216.30 (n/a)</td><td>183.12 (n/a)</td><td>171.40 (n/a)</td><td>155.80 (n/a)</td><td>24.71 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (+0.64%)</td><td>0.16 (+0.25%)</td><td>0.16 (+0.05%)</td><td>0.16 (+0.46%)</td><td>0.00 <b>(+36.46%)</b></td><td>52310.90 (-0.46%)</td><td>52202.68 (-0.25%)</td><td>52274.80 (-0.05%)</td><td>51908.90 (-0.64%)</td><td>166.17 <b>(+34.82%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52551.10 (n/a)</td><td>52335.40 (n/a)</td><td>52299.50 (n/a)</td><td>52241.90 (n/a)</td><td>123.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.00 (n/a)</td><td>52474.30 (n/a)</td><td>52259.34 (n/a)</td><td>52265.30 (n/a)</td><td>51840.20 (n/a)</td><td>256.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>413409.90 (n/a)</td><td>413193.48 (n/a)</td><td>413185.80 (n/a)</td><td>412922.00 (n/a)</td><td>177.64 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.17 (-0.14%)</td><td>0.15 (-2.22%)</td><td>0.14 (-4.84%)</td><td>0.12 (-2.68%)</td><td>0.02 <b>(+37.00%)</b></td><td>197.70 (+2.75%)</td><td>170.06 (+3.25%)</td><td>170.50 (+5.12%)</td><td>140.60 (+0.14%)</td><td>26.45 <b>(+41.63%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>192.40 (n/a)</td><td>164.70 (n/a)</td><td>162.20 (n/a)</td><td>140.40 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.39 (+6.36%)</td><td>0.36 (+17.97%)</td><td>0.37 <b>(+25.51%)</b></td><td>0.31 <b>(+25.31%)</b></td><td>0.03 <b>(-40.34%)</b></td><td>159.50 <b>(-20.17%)</b></td><td>138.06 (-16.56%)</td><td>133.70 <b>(-20.32%)</b></td><td>126.70 (-6.01%)</td><td>12.57 <b>(-53.69%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.36 (n/a)</td><td>0.30 (n/a)</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.05 (n/a)</td><td>199.80 (n/a)</td><td>165.46 (n/a)</td><td>167.80 (n/a)</td><td>134.80 (n/a)</td><td>27.14 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>13.35 (+4.24%)</td><td>11.82 (-4.86%)</td><td>12.92 (+3.79%)</td><td>7.30 <b>(-39.25%)</b></td><td>2.54 <b>(+673.09%)</b></td><td>1435.80 <b>(+64.62%)</b></td><td>935.54 (+10.76%)</td><td>811.80 (-3.64%)</td><td>785.20 (-4.07%)</td><td>280.39 <b>(+1151.17%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>12.81 (n/a)</td><td>12.42 (n/a)</td><td>12.45 (n/a)</td><td>12.02 (n/a)</td><td>0.33 (n/a)</td><td>872.20 (n/a)</td><td>844.66 (n/a)</td><td>842.50 (n/a)</td><td>818.50 (n/a)</td><td>22.41 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.35 <b>(+21.76%)</b></td><td>0.28 <b>(+26.23%)</b></td><td>0.29 <b>(+44.93%)</b></td><td>0.21 <b>(+22.79%)</b></td><td>0.05 (-4.50%)</td><td>198.30 (-18.60%)</td><td>148.86 <b>(-22.07%)</b></td><td>141.10 <b>(-31.04%)</b></td><td>117.20 (-17.87%)</td><td>30.53 <b>(-31.76%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>243.60 (n/a)</td><td>191.02 (n/a)</td><td>204.60 (n/a)</td><td>142.70 (n/a)</td><td>44.74 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (+3.23%)</td><td>0.04 <b>(+34.03%)</b></td><td>0.04 <b>(+62.48%)</b></td><td>0.03 <b>(+47.54%)</b></td><td>0.01 <b>(-40.19%)</b></td><td>170.00 <b>(-32.22%)</b></td><td>140.92 <b>(-29.07%)</b></td><td>132.70 <b>(-38.45%)</b></td><td>116.90 (-3.15%)</td><td>20.87 <b>(-59.36%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>250.80 (n/a)</td><td>198.68 (n/a)</td><td>215.60 (n/a)</td><td>120.70 (n/a)</td><td>51.34 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-0.75%)</td><td>0.02 (-14.73%)</td><td>0.02 <b>(-20.30%)</b></td><td>0.02 <b>(-30.58%)</b></td><td>0.01 <b>(+50.47%)</b></td><td>250.10 <b>(+44.07%)</b></td><td>174.10 <b>(+21.56%)</b></td><td>165.60 <b>(+25.45%)</b></td><td>126.10 (+0.80%)</td><td>46.99 <b>(+124.81%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>173.60 (n/a)</td><td>143.22 (n/a)</td><td>132.00 (n/a)</td><td>125.10 (n/a)</td><td>20.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (+5.00%)</td><td>0.04 (+4.84%)</td><td>0.05 <b>(+29.33%)</b></td><td>0.03 <b>(-23.62%)</b></td><td>0.01 <b>(+38.15%)</b></td><td>240.90 <b>(+30.92%)</b></td><td>158.76 (-0.26%)</td><td>134.70 <b>(-22.68%)</b></td><td>107.90 (-4.77%)</td><td>52.83 <b>(+74.73%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>184.00 (n/a)</td><td>159.18 (n/a)</td><td>174.20 (n/a)</td><td>113.30 (n/a)</td><td>30.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-5.89%)</td><td>0.03 (+0.19%)</td><td>0.03 (+12.33%)</td><td>0.02 (-12.83%)</td><td>0.01 (+13.85%)</td><td>198.60 (+14.73%)</td><td>157.46 (+1.22%)</td><td>149.10 (-10.93%)</td><td>122.20 (+6.26%)</td><td>33.95 <b>(+42.53%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>173.10 (n/a)</td><td>155.56 (n/a)</td><td>167.40 (n/a)</td><td>115.00 (n/a)</td><td>23.82 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 <b>(+66.64%)</b></td><td>0.03 (+11.85%)</td><td>0.03 (-0.59%)</td><td>0.02 (-3.18%)</td><td>0.01 <b>(+232.53%)</b></td><td>228.40 (+3.25%)</td><td>186.28 (-3.25%)</td><td>193.80 (+0.62%)</td><td>99.50 <b>(-39.99%)</b></td><td>52.65 <b>(+102.81%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.20 (n/a)</td><td>192.54 (n/a)</td><td>192.60 (n/a)</td><td>165.80 (n/a)</td><td>25.96 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-17.66%)</td><td>0.02 (-6.16%)</td><td>0.02 (-4.26%)</td><td>0.02 <b>(+23.91%)</b></td><td>0.01 <b>(-45.77%)</b></td><td>225.90 (-19.29%)</td><td>172.22 (-1.80%)</td><td>164.20 (+4.45%)</td><td>127.90 <b>(+21.46%)</b></td><td>36.94 <b>(-46.88%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>279.90 (n/a)</td><td>175.38 (n/a)</td><td>157.20 (n/a)</td><td>105.30 (n/a)</td><td>69.55 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (+11.61%)</td><td>0.03 (+9.99%)</td><td>0.03 (+18.58%)</td><td>0.03 (-5.16%)</td><td>0.01 <b>(+36.75%)</b></td><td>203.50 (+5.44%)</td><td>157.74 (-7.74%)</td><td>149.00 (-15.68%)</td><td>117.60 (-10.43%)</td><td>32.52 <b>(+31.17%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>193.00 (n/a)</td><td>170.98 (n/a)</td><td>176.70 (n/a)</td><td>131.30 (n/a)</td><td>24.79 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (+3.62%)</td><td>0.02 (+3.99%)</td><td>0.02 (-4.00%)</td><td>0.02 (+2.86%)</td><td>0.00 (-6.03%)</td><td>195.90 (-2.78%)</td><td>168.30 (-4.12%)</td><td>173.90 (+4.19%)</td><td>144.20 (-3.48%)</td><td>20.71 (-15.30%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.50 (n/a)</td><td>175.54 (n/a)</td><td>166.90 (n/a)</td><td>149.40 (n/a)</td><td>24.45 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (+12.65%)</td><td>0.03 (+11.89%)</td><td>0.02 (-0.17%)</td><td>0.02 <b>(+33.60%)</b></td><td>0.01 (+0.22%)</td><td>209.50 <b>(-25.15%)</b></td><td>176.80 (-12.20%)</td><td>185.60 (+0.16%)</td><td>123.10 (-11.18%)</td><td>34.32 <b>(-35.02%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>279.90 (n/a)</td><td>201.36 (n/a)</td><td>185.30 (n/a)</td><td>138.60 (n/a)</td><td>52.81 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-0.66%)</td><td>0.03 (+4.33%)</td><td>0.03 (+3.69%)</td><td>0.02 (+12.49%)</td><td>0.00 (-19.59%)</td><td>180.00 (-11.11%)</td><td>156.92 (-5.04%)</td><td>160.50 (-3.55%)</td><td>129.30 (+0.62%)</td><td>19.47 <b>(-27.89%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.50 (n/a)</td><td>165.24 (n/a)</td><td>166.40 (n/a)</td><td>128.50 (n/a)</td><td>27.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (+9.44%)</td><td>0.03 (+15.25%)</td><td>0.02 (+16.54%)</td><td>0.02 (+3.94%)</td><td>0.01 <b>(+34.83%)</b></td><td>226.50 (-3.78%)</td><td>183.82 (-12.15%)</td><td>187.80 (-14.21%)</td><td>143.40 (-8.66%)</td><td>36.62 <b>(+21.19%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>235.40 (n/a)</td><td>209.24 (n/a)</td><td>218.90 (n/a)</td><td>157.00 (n/a)</td><td>30.21 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (+1.56%)</td><td>0.02 (-0.70%)</td><td>0.02 (+3.89%)</td><td>0.02 (-16.40%)</td><td>0.00 <b>(+45.07%)</b></td><td>256.20 (+19.61%)</td><td>190.66 (+2.58%)</td><td>181.20 (-3.72%)</td><td>150.60 (-1.50%)</td><td>39.34 <b>(+80.32%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>214.20 (n/a)</td><td>185.86 (n/a)</td><td>188.20 (n/a)</td><td>152.90 (n/a)</td><td>21.82 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 <b>(-28.20%)</b></td><td>0.02 (-16.97%)</td><td>0.02 (-10.98%)</td><td>0.01 (-18.32%)</td><td>0.00 <b>(-36.78%)</b></td><td>296.60 <b>(+22.41%)</b></td><td>230.92 (+18.53%)</td><td>218.20 (+12.30%)</td><td>182.30 <b>(+39.27%)</b></td><td>48.68 (+6.10%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>242.30 (n/a)</td><td>194.82 (n/a)</td><td>194.30 (n/a)</td><td>130.90 (n/a)</td><td>45.88 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (+5.12%)</td><td>0.02 (-1.10%)</td><td>0.02 (+4.58%)</td><td>0.02 (-5.66%)</td><td>0.00 <b>(+31.89%)</b></td><td>203.60 (+5.99%)</td><td>176.60 (+2.09%)</td><td>172.50 (-4.38%)</td><td>135.60 (-4.84%)</td><td>28.19 <b>(+34.26%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>192.10 (n/a)</td><td>172.98 (n/a)</td><td>180.40 (n/a)</td><td>142.50 (n/a)</td><td>21.00 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (-18.59%)</td><td>0.02 (-6.65%)</td><td>0.02 (+1.33%)</td><td>0.01 <b>(-20.07%)</b></td><td>0.00 (-12.38%)</td><td>293.40 <b>(+25.12%)</b></td><td>215.54 (+7.73%)</td><td>196.00 (-1.31%)</td><td>186.10 <b>(+22.84%)</b></td><td>44.19 <b>(+42.22%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.50 (n/a)</td><td>200.08 (n/a)</td><td>198.60 (n/a)</td><td>151.50 (n/a)</td><td>31.07 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.02 (+3.49%)</td><td>0.02 (-3.73%)</td><td>0.02 (-10.20%)</td><td>0.02 (-11.77%)</td><td>0.00 <b>(+131.05%)</b></td><td>232.60 (+13.30%)</td><td>199.68 (+5.26%)</td><td>211.30 (+11.33%)</td><td>168.50 (-3.33%)</td><td>27.86 <b>(+146.67%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.30 (n/a)</td><td>189.70 (n/a)</td><td>189.80 (n/a)</td><td>174.30 (n/a)</td><td>11.29 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (+15.75%)</td><td>0.04 (-12.46%)</td><td>0.04 (-13.73%)</td><td>0.02 <b>(-55.86%)</b></td><td>0.02 <b>(+221.24%)</b></td><td>424.30 <b>(+126.53%)</b></td><td>243.16 <b>(+49.95%)</b></td><td>190.90 (+15.91%)</td><td>110.80 (-13.64%)</td><td>143.65 <b>(+543.99%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.30 (n/a)</td><td>162.16 (n/a)</td><td>164.70 (n/a)</td><td>128.30 (n/a)</td><td>22.31 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 <b>(+32.37%)</b></td><td>0.07 (+12.96%)</td><td>0.07 (+3.16%)</td><td>0.06 (-4.89%)</td><td>0.01 <b>(+189.46%)</b></td><td>216.10 (+5.16%)</td><td>172.14 (-9.17%)</td><td>178.30 (-3.10%)</td><td>130.20 <b>(-24.48%)</b></td><td>33.03 <b>(+124.26%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.50 (n/a)</td><td>189.52 (n/a)</td><td>184.00 (n/a)</td><td>172.40 (n/a)</td><td>14.73 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 <b>(+25.77%)</b></td><td>0.05 (-3.23%)</td><td>0.05 (-1.44%)</td><td>0.03 <b>(-30.25%)</b></td><td>0.01 <b>(+147.35%)</b></td><td>289.70 <b>(+43.34%)</b></td><td>193.38 (+10.92%)</td><td>172.90 (+1.47%)</td><td>119.50 <b>(-20.55%)</b></td><td>63.26 <b>(+183.39%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>202.10 (n/a)</td><td>174.34 (n/a)</td><td>170.40 (n/a)</td><td>150.40 (n/a)</td><td>22.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (-0.49%)</td><td>0.07 (+4.89%)</td><td>0.06 (-2.19%)</td><td>0.06 (+18.51%)</td><td>0.01 <b>(-25.17%)</b></td><td>182.20 (-15.65%)</td><td>160.98 (-7.28%)</td><td>166.50 (+2.27%)</td><td>118.60 (+0.51%)</td><td>24.72 <b>(-41.17%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>216.00 (n/a)</td><td>173.62 (n/a)</td><td>162.80 (n/a)</td><td>118.00 (n/a)</td><td>42.03 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (+9.61%)</td><td>0.05 (-7.35%)</td><td>0.05 (-11.50%)</td><td>0.05 (-7.92%)</td><td>0.01 <b>(+67.18%)</b></td><td>179.40 (+8.60%)</td><td>158.88 (+9.59%)</td><td>168.20 (+12.96%)</td><td>118.40 (-8.78%)</td><td>25.47 <b>(+69.54%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>165.20 (n/a)</td><td>144.98 (n/a)</td><td>148.90 (n/a)</td><td>129.80 (n/a)</td><td>15.02 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (+17.43%)</td><td>0.07 (-3.77%)</td><td>0.06 (-14.13%)</td><td>0.05 (+5.11%)</td><td>0.02 <b>(+25.27%)</b></td><td>194.70 (-4.84%)</td><td>161.70 (+4.97%)</td><td>168.30 (+16.47%)</td><td>102.60 (-14.78%)</td><td>35.92 (-0.53%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>204.60 (n/a)</td><td>154.04 (n/a)</td><td>144.50 (n/a)</td><td>120.40 (n/a)</td><td>36.11 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.06 (-13.36%)</td><td>0.05 (-17.43%)</td><td>0.04 (-3.72%)</td><td>0.03 <b>(-22.66%)</b></td><td>0.01 <b>(-29.21%)</b></td><td>241.10 <b>(+29.35%)</b></td><td>188.34 (+19.58%)</td><td>188.20 (+3.86%)</td><td>135.80 (+15.38%)</td><td>38.02 (+5.03%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.40 (n/a)</td><td>157.50 (n/a)</td><td>181.20 (n/a)</td><td>117.70 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 <b>(+21.92%)</b></td><td>0.06 (+11.93%)</td><td>0.05 (-1.14%)</td><td>0.05 <b>(+34.55%)</b></td><td>0.02 (+12.48%)</td><td>185.80 <b>(-25.68%)</b></td><td>159.52 (-11.64%)</td><td>176.20 (+1.15%)</td><td>108.10 (-17.98%)</td><td>32.68 <b>(-31.01%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>250.00 (n/a)</td><td>180.54 (n/a)</td><td>174.20 (n/a)</td><td>131.80 (n/a)</td><td>47.37 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 (-5.95%)</td><td>0.05 (-4.15%)</td><td>0.05 (+6.60%)</td><td>0.04 (+6.03%)</td><td>0.01 <b>(-29.32%)</b></td><td>200.30 (-5.70%)</td><td>168.84 (+1.70%)</td><td>163.70 (-6.19%)</td><td>125.80 (+6.34%)</td><td>29.61 <b>(-27.99%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>212.40 (n/a)</td><td>166.02 (n/a)</td><td>174.50 (n/a)</td><td>118.30 (n/a)</td><td>41.12 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.07 <b>(+21.69%)</b></td><td>0.06 (+8.15%)</td><td>0.06 (+0.11%)</td><td>0.05 (-0.36%)</td><td>0.01 <b>(+63.72%)</b></td><td>202.80 (+0.35%)</td><td>164.64 (-6.45%)</td><td>165.50 (-0.06%)</td><td>128.10 (-17.83%)</td><td>26.86 <b>(+32.82%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>202.10 (n/a)</td><td>176.00 (n/a)</td><td>165.60 (n/a)</td><td>155.90 (n/a)</td><td>20.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (+2.37%)</td><td>0.04 (-0.44%)</td><td>0.04 (-5.42%)</td><td>0.03 (-18.32%)</td><td>0.01 <b>(+48.40%)</b></td><td>290.40 <b>(+22.43%)</b></td><td>211.58 (+4.04%)</td><td>218.50 (+5.76%)</td><td>149.40 (-2.29%)</td><td>56.63 <b>(+77.88%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>237.20 (n/a)</td><td>203.36 (n/a)</td><td>206.60 (n/a)</td><td>152.90 (n/a)</td><td>31.83 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (+0.47%)</td><td>0.04 (+1.62%)</td><td>0.04 (-2.92%)</td><td>0.03 (-6.81%)</td><td>0.01 (+9.57%)</td><td>291.40 (+7.33%)</td><td>217.58 (-0.93%)</td><td>212.00 (+3.01%)</td><td>175.90 (-0.45%)</td><td>45.01 (+17.63%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>271.50 (n/a)</td><td>219.62 (n/a)</td><td>205.80 (n/a)</td><td>176.70 (n/a)</td><td>38.26 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 <b>(-24.78%)</b></td><td>0.04 (-9.20%)</td><td>0.04 (-6.70%)</td><td>0.03 (+14.15%)</td><td>0.01 <b>(-48.46%)</b></td><td>253.40 (-12.38%)</td><td>200.42 (+1.88%)</td><td>205.30 (+7.21%)</td><td>154.80 <b>(+32.88%)</b></td><td>42.48 <b>(-41.28%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>289.20 (n/a)</td><td>196.72 (n/a)</td><td>191.50 (n/a)</td><td>116.50 (n/a)</td><td>72.35 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.05 (-0.01%)</td><td>0.04 (-6.27%)</td><td>0.04 (-11.09%)</td><td>0.04 (-3.55%)</td><td>0.00 (+6.15%)</td><td>231.30 (+3.68%)</td><td>206.40 (+6.81%)</td><td>209.90 (+12.49%)</td><td>171.60 (+0.00%)</td><td>21.73 (+6.85%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>223.10 (n/a)</td><td>193.24 (n/a)</td><td>186.60 (n/a)</td><td>171.60 (n/a)</td><td>20.33 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.04 (-17.10%)</td><td>0.04 (-6.17%)</td><td>0.04 (+1.98%)</td><td>0.03 (-12.33%)</td><td>0.01 <b>(-23.12%)</b></td><td>308.90 (+14.07%)</td><td>229.42 (+6.09%)</td><td>213.60 (-1.93%)</td><td>187.70 <b>(+20.63%)</b></td><td>47.39 (+10.96%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>270.80 (n/a)</td><td>216.26 (n/a)</td><td>217.80 (n/a)</td><td>155.60 (n/a)</td><td>42.71 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (+5.82%)</td><td>0.10 (+6.03%)</td><td>0.10 (+9.65%)</td><td>0.09 (+10.08%)</td><td>0.01 (+15.14%)</td><td>183.10 (-9.13%)</td><td>160.44 (-5.51%)</td><td>156.80 (-8.84%)</td><td>136.60 (-5.53%)</td><td>21.40 (+0.65%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>201.50 (n/a)</td><td>169.80 (n/a)</td><td>172.00 (n/a)</td><td>144.60 (n/a)</td><td>21.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (-11.99%)</td><td>0.13 (-5.83%)</td><td>0.13 (+5.77%)</td><td>0.08 (-17.52%)</td><td>0.03 (-5.04%)</td><td>305.70 <b>(+21.21%)</b></td><td>205.78 (+7.61%)</td><td>186.90 (-5.46%)</td><td>150.70 (+13.65%)</td><td>60.23 <b>(+37.67%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>252.20 (n/a)</td><td>191.22 (n/a)</td><td>197.70 (n/a)</td><td>132.60 (n/a)</td><td>43.75 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 <b>(-28.20%)</b></td><td>0.09 (-13.67%)</td><td>0.10 (-8.00%)</td><td>0.09 (-6.09%)</td><td>0.01 <b>(-69.75%)</b></td><td>188.70 (+6.49%)</td><td>173.32 (+12.94%)</td><td>172.30 (+8.71%)</td><td>155.30 <b>(+39.28%)</b></td><td>12.15 <b>(-55.73%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>177.20 (n/a)</td><td>153.46 (n/a)</td><td>158.50 (n/a)</td><td>111.50 (n/a)</td><td>27.44 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (+4.58%)</td><td>0.11 (-18.69%)</td><td>0.09 <b>(-30.24%)</b></td><td>0.08 (-17.87%)</td><td>0.05 <b>(+29.97%)</b></td><td>270.80 <b>(+21.76%)</b></td><td>208.00 <b>(+28.82%)</b></td><td>225.00 <b>(+43.31%)</b></td><td>105.60 (-4.35%)</td><td>61.46 <b>(+39.30%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>222.40 (n/a)</td><td>161.46 (n/a)</td><td>157.00 (n/a)</td><td>110.40 (n/a)</td><td>44.12 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.13 <b>(+40.19%)</b></td><td>0.10 <b>(+39.80%)</b></td><td>0.09 <b>(+46.38%)</b></td><td>0.06 <b>(+28.44%)</b></td><td>0.02 <b>(+48.24%)</b></td><td>259.90 <b>(-22.14%)</b></td><td>180.94 <b>(-27.71%)</b></td><td>175.10 <b>(-31.68%)</b></td><td>130.70 <b>(-28.66%)</b></td><td>50.37 (-15.91%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>333.80 (n/a)</td><td>250.30 (n/a)</td><td>256.30 (n/a)</td><td>183.20 (n/a)</td><td>59.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 <b>(+29.61%)</b></td><td>0.12 (-3.70%)</td><td>0.11 (-16.79%)</td><td>0.09 (-15.16%)</td><td>0.04 <b>(+118.73%)</b></td><td>229.20 (+17.90%)</td><td>180.00 (+10.65%)</td><td>189.60 <b>(+20.15%)</b></td><td>106.60 <b>(-22.87%)</b></td><td>52.52 <b>(+106.00%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>194.40 (n/a)</td><td>162.68 (n/a)</td><td>157.80 (n/a)</td><td>138.20 (n/a)</td><td>25.50 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 <b>(+45.77%)</b></td><td>0.11 <b>(+26.33%)</b></td><td>0.10 (+18.51%)</td><td>0.09 <b>(+33.83%)</b></td><td>0.02 <b>(+76.09%)</b></td><td>181.50 <b>(-25.28%)</b></td><td>155.56 <b>(-20.09%)</b></td><td>163.60 (-15.63%)</td><td>116.40 <b>(-31.41%)</b></td><td>26.40 (-10.31%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>242.90 (n/a)</td><td>194.66 (n/a)</td><td>193.90 (n/a)</td><td>169.70 (n/a)</td><td>29.43 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (-1.18%)</td><td>0.11 (-1.31%)</td><td>0.10 (-10.28%)</td><td>0.09 <b>(+21.61%)</b></td><td>0.02 (-19.90%)</td><td>198.60 (-17.76%)</td><td>174.66 (-0.17%)</td><td>180.70 (+11.47%)</td><td>148.40 (+1.23%)</td><td>24.22 <b>(-36.48%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>241.50 (n/a)</td><td>174.96 (n/a)</td><td>162.10 (n/a)</td><td>146.60 (n/a)</td><td>38.12 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 <b>(+26.46%)</b></td><td>0.11 <b>(+31.85%)</b></td><td>0.10 (+18.97%)</td><td>0.09 <b>(+62.94%)</b></td><td>0.01 (-15.16%)</td><td>181.80 <b>(-38.62%)</b></td><td>156.08 <b>(-26.10%)</b></td><td>160.50 (-15.97%)</td><td>132.00 <b>(-20.96%)</b></td><td>20.12 <b>(-60.43%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>296.20 (n/a)</td><td>211.20 (n/a)</td><td>191.00 (n/a)</td><td>167.00 (n/a)</td><td>50.85 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.15 <b>(+23.20%)</b></td><td>0.11 (+6.01%)</td><td>0.11 (+2.66%)</td><td>0.09 (-6.44%)</td><td>0.02 <b>(+112.82%)</b></td><td>206.80 (+6.87%)</td><td>168.26 (-3.65%)</td><td>166.90 (-2.57%)</td><td>123.60 (-18.84%)</td><td>30.52 <b>(+78.45%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>174.64 (n/a)</td><td>171.30 (n/a)</td><td>152.30 (n/a)</td><td>17.10 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (+1.36%)</td><td>0.09 (+10.83%)</td><td>0.10 <b>(+35.70%)</b></td><td>0.06 (+2.34%)</td><td>0.02 (+4.34%)</td><td>286.10 (-2.29%)</td><td>189.42 (-9.40%)</td><td>160.30 <b>(-26.30%)</b></td><td>148.00 (-1.33%)</td><td>58.53 (+2.20%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>292.80 (n/a)</td><td>209.08 (n/a)</td><td>217.50 (n/a)</td><td>150.00 (n/a)</td><td>57.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (-7.36%)</td><td>0.09 (-5.21%)</td><td>0.10 (-0.47%)</td><td>0.08 (-7.17%)</td><td>0.01 (+14.17%)</td><td>213.00 (+7.74%)</td><td>186.22 (+5.93%)</td><td>177.50 (+0.51%)</td><td>163.40 (+7.93%)</td><td>22.33 <b>(+36.05%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>197.70 (n/a)</td><td>175.80 (n/a)</td><td>176.60 (n/a)</td><td>151.40 (n/a)</td><td>16.42 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.15 <b>(+23.46%)</b></td><td>0.10 <b>(+20.59%)</b></td><td>0.09 (+16.66%)</td><td>0.06 (-2.99%)</td><td>0.03 <b>(+47.22%)</b></td><td>275.30 (+3.07%)</td><td>179.86 (-13.59%)</td><td>180.90 (-14.31%)</td><td>109.00 (-19.02%)</td><td>61.82 <b>(+29.17%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>267.10 (n/a)</td><td>208.14 (n/a)</td><td>211.10 (n/a)</td><td>134.60 (n/a)</td><td>47.86 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (-5.28%)</td><td>0.09 (-7.74%)</td><td>0.09 (-14.96%)</td><td>0.07 <b>(-20.35%)</b></td><td>0.02 <b>(+28.15%)</b></td><td>265.70 <b>(+25.57%)</b></td><td>195.04 (+10.74%)</td><td>197.20 (+17.59%)</td><td>150.80 (+5.60%)</td><td>46.02 <b>(+64.83%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.60 (n/a)</td><td>176.12 (n/a)</td><td>167.70 (n/a)</td><td>142.80 (n/a)</td><td>27.92 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.09 (+18.29%)</td><td>0.08 (+12.26%)</td><td>0.08 (+4.68%)</td><td>0.06 <b>(+24.40%)</b></td><td>0.01 (-6.58%)</td><td>262.10 (-19.63%)</td><td>219.30 (-11.86%)</td><td>213.80 (-4.47%)</td><td>179.50 (-15.45%)</td><td>30.87 <b>(-36.01%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>326.10 (n/a)</td><td>248.80 (n/a)</td><td>223.80 (n/a)</td><td>212.30 (n/a)</td><td>48.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.22 (+11.35%)</td><td>0.18 (-0.31%)</td><td>0.17 (-8.56%)</td><td>0.14 (+2.35%)</td><td>0.03 <b>(+26.50%)</b></td><td>235.20 (-2.29%)</td><td>185.98 (+1.00%)</td><td>188.10 (+9.36%)</td><td>148.10 (-10.19%)</td><td>34.20 (+7.58%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>240.70 (n/a)</td><td>184.14 (n/a)</td><td>172.00 (n/a)</td><td>164.90 (n/a)</td><td>31.79 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (-19.34%)</td><td>0.17 (-3.39%)</td><td>0.18 (+6.29%)</td><td>0.16 (+19.79%)</td><td>0.01 <b>(-68.69%)</b></td><td>208.70 (-16.55%)</td><td>189.44 (-0.34%)</td><td>183.90 (-5.93%)</td><td>172.70 <b>(+23.98%)</b></td><td>14.34 <b>(-67.00%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>250.10 (n/a)</td><td>190.08 (n/a)</td><td>195.50 (n/a)</td><td>139.30 (n/a)</td><td>43.45 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.34 (+15.77%)</td><td>0.24 (-2.41%)</td><td>0.24 (+4.33%)</td><td>0.15 <b>(-26.11%)</b></td><td>0.07 <b>(+104.33%)</b></td><td>266.70 <b>(+35.38%)</b></td><td>187.40 (+8.99%)</td><td>167.70 (-4.12%)</td><td>121.90 (-13.61%)</td><td>58.78 <b>(+141.37%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>197.00 (n/a)</td><td>171.94 (n/a)</td><td>174.90 (n/a)</td><td>141.10 (n/a)</td><td>24.35 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 (-1.62%)</td><td>0.17 (+0.06%)</td><td>0.18 (+1.67%)</td><td>0.14 (+18.32%)</td><td>0.03 (-19.64%)</td><td>236.50 (-15.48%)</td><td>196.36 (-1.67%)</td><td>180.80 (-1.63%)</td><td>164.60 (+1.60%)</td><td>31.43 <b>(-32.58%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>279.80 (n/a)</td><td>199.70 (n/a)</td><td>183.80 (n/a)</td><td>162.00 (n/a)</td><td>46.61 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.32 (+0.13%)</td><td>0.27 (+8.63%)</td><td>0.29 (+9.07%)</td><td>0.18 (-4.14%)</td><td>0.05 (-2.61%)</td><td>226.00 (+4.34%)</td><td>156.04 (-7.89%)</td><td>142.00 (-8.33%)</td><td>126.40 (-0.16%)</td><td>39.75 (+4.54%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.06 (n/a)</td><td>216.60 (n/a)</td><td>169.40 (n/a)</td><td>154.90 (n/a)</td><td>126.60 (n/a)</td><td>38.03 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.23 (+14.30%)</td><td>0.17 (+10.35%)</td><td>0.17 (+9.50%)</td><td>0.13 (+4.94%)</td><td>0.04 <b>(+42.22%)</b></td><td>243.00 (-4.71%)</td><td>198.04 (-7.82%)</td><td>195.40 (-8.65%)</td><td>143.40 (-12.51%)</td><td>43.06 <b>(+22.88%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>255.00 (n/a)</td><td>214.84 (n/a)</td><td>213.90 (n/a)</td><td>163.90 (n/a)</td><td>35.04 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (-1.36%)</td><td>0.21 (-4.47%)</td><td>0.21 (-3.87%)</td><td>0.17 (-12.77%)</td><td>0.02 <b>(+48.80%)</b></td><td>219.00 (+14.60%)</td><td>180.42 (+5.50%)</td><td>174.10 (+4.06%)</td><td>156.40 (+1.36%)</td><td>23.65 <b>(+75.22%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>191.10 (n/a)</td><td>171.02 (n/a)</td><td>167.30 (n/a)</td><td>154.30 (n/a)</td><td>13.50 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.22 (-12.20%)</td><td>0.18 (-3.85%)</td><td>0.19 (+5.15%)</td><td>0.14 (-12.95%)</td><td>0.04 (+7.55%)</td><td>241.40 (+14.90%)</td><td>186.60 (+5.45%)</td><td>173.00 (-4.89%)</td><td>148.40 (+13.89%)</td><td>42.26 <b>(+43.56%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.10 (n/a)</td><td>176.96 (n/a)</td><td>181.90 (n/a)</td><td>130.30 (n/a)</td><td>29.44 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.31 (+9.09%)</td><td>0.21 (-7.78%)</td><td>0.19 (-10.78%)</td><td>0.17 (-8.21%)</td><td>0.06 <b>(+55.75%)</b></td><td>210.80 (+8.94%)</td><td>182.98 (+11.19%)</td><td>194.40 (+12.05%)</td><td>119.70 (-8.35%)</td><td>37.20 <b>(+53.86%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>193.50 (n/a)</td><td>164.56 (n/a)</td><td>173.50 (n/a)</td><td>130.60 (n/a)</td><td>24.18 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.27 <b>(+24.03%)</b></td><td>0.20 <b>(+27.36%)</b></td><td>0.20 <b>(+37.13%)</b></td><td>0.15 <b>(+34.74%)</b></td><td>0.05 <b>(+24.99%)</b></td><td>224.90 <b>(-25.78%)</b></td><td>171.36 <b>(-21.60%)</b></td><td>161.80 <b>(-27.08%)</b></td><td>119.70 (-19.39%)</td><td>43.49 <b>(-23.37%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>303.00 (n/a)</td><td>218.56 (n/a)</td><td>221.90 (n/a)</td><td>148.50 (n/a)</td><td>56.75 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.25 (+19.40%)</td><td>0.19 (+10.64%)</td><td>0.18 (-0.36%)</td><td>0.16 <b>(+41.66%)</b></td><td>0.04 (+1.87%)</td><td>213.80 <b>(-29.39%)</b></td><td>187.44 (-11.23%)</td><td>190.70 (+0.37%)</td><td>136.70 (-16.24%)</td><td>30.26 <b>(-43.90%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>302.80 (n/a)</td><td>211.16 (n/a)</td><td>190.00 (n/a)</td><td>163.20 (n/a)</td><td>53.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.27 (-0.99%)</td><td>0.20 (+8.86%)</td><td>0.18 (+5.38%)</td><td>0.16 <b>(+51.09%)</b></td><td>0.05 <b>(-27.43%)</b></td><td>204.50 <b>(-33.82%)</b></td><td>171.94 (-13.55%)</td><td>186.90 (-5.08%)</td><td>121.10 (+1.09%)</td><td>33.93 <b>(-52.09%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>309.00 (n/a)</td><td>198.90 (n/a)</td><td>196.90 (n/a)</td><td>119.80 (n/a)</td><td>70.80 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (-13.60%)</td><td>0.17 (-8.48%)</td><td>0.17 (-5.25%)</td><td>0.15 (-7.84%)</td><td>0.01 <b>(-35.41%)</b></td><td>230.10 (+8.49%)</td><td>204.54 (+8.67%)</td><td>200.30 (+5.53%)</td><td>186.40 (+15.70%)</td><td>17.93 (-19.46%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>212.10 (n/a)</td><td>188.22 (n/a)</td><td>189.80 (n/a)</td><td>161.10 (n/a)</td><td>22.27 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.18 (-6.00%)</td><td>0.15 (+4.05%)</td><td>0.14 (-0.26%)</td><td>0.13 <b>(+29.02%)</b></td><td>0.02 <b>(-35.42%)</b></td><td>257.10 <b>(-22.49%)</b></td><td>218.76 (-6.97%)</td><td>227.60 (+0.26%)</td><td>179.10 (+6.42%)</td><td>31.75 <b>(-48.17%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>331.70 (n/a)</td><td>235.16 (n/a)</td><td>227.00 (n/a)</td><td>168.30 (n/a)</td><td>61.25 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.15 (-10.71%)</td><td>0.13 (-8.62%)</td><td>0.12 (-8.80%)</td><td>0.11 (-7.60%)</td><td>0.01 <b>(-33.85%)</b></td><td>186.50 (+8.24%)</td><td>161.94 (+8.48%)</td><td>163.90 (+9.63%)</td><td>139.60 (+11.95%)</td><td>17.85 <b>(-20.58%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>172.30 (n/a)</td><td>149.28 (n/a)</td><td>149.50 (n/a)</td><td>124.70 (n/a)</td><td>22.48 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 <b>(-29.11%)</b></td><td>0.10 <b>(-26.93%)</b></td><td>0.10 <b>(-30.74%)</b></td><td>0.09 <b>(-23.99%)</b></td><td>0.01 <b>(-62.36%)</b></td><td>218.70 <b>(+31.59%)</b></td><td>199.30 <b>(+35.97%)</b></td><td>197.10 <b>(+44.40%)</b></td><td>189.20 <b>(+41.09%)</b></td><td>11.38 <b>(-28.93%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>166.20 (n/a)</td><td>146.58 (n/a)</td><td>136.50 (n/a)</td><td>134.10 (n/a)</td><td>16.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.18 <b>(+47.44%)</b></td><td>0.14 <b>(+21.39%)</b></td><td>0.12 (+12.16%)</td><td>0.11 (+11.73%)</td><td>0.03 <b>(+198.37%)</b></td><td>180.90 (-10.49%)</td><td>153.66 (-15.35%)</td><td>165.90 (-10.85%)</td><td>111.70 <b>(-32.18%)</b></td><td>29.43 <b>(+85.51%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>202.10 (n/a)</td><td>181.52 (n/a)</td><td>186.10 (n/a)</td><td>164.70 (n/a)</td><td>15.86 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 <b>(+32.14%)</b></td><td>0.13 <b>(+20.19%)</b></td><td>0.11 (+1.59%)</td><td>0.09 <b>(+22.31%)</b></td><td>0.03 <b>(+67.62%)</b></td><td>216.50 (-18.24%)</td><td>170.26 (-15.38%)</td><td>179.10 (-1.54%)</td><td>128.60 <b>(-24.31%)</b></td><td>38.51 (-0.83%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>264.80 (n/a)</td><td>201.20 (n/a)</td><td>181.90 (n/a)</td><td>169.90 (n/a)</td><td>38.84 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 <b>(+26.72%)</b></td><td>0.12 (+5.31%)</td><td>0.13 (+3.74%)</td><td>0.08 <b>(-26.46%)</b></td><td>0.03 <b>(+240.08%)</b></td><td>269.50 <b>(+36.04%)</b></td><td>178.44 (+1.57%)</td><td>163.10 (-3.61%)</td><td>126.50 <b>(-21.09%)</b></td><td>57.69 <b>(+264.54%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>198.10 (n/a)</td><td>175.68 (n/a)</td><td>169.20 (n/a)</td><td>160.30 (n/a)</td><td>15.83 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.15 (-9.86%)</td><td>0.14 (+10.38%)</td><td>0.14 <b>(+29.53%)</b></td><td>0.12 <b>(+29.35%)</b></td><td>0.02 <b>(-51.11%)</b></td><td>174.90 <b>(-22.71%)</b></td><td>150.76 (-13.56%)</td><td>141.50 <b>(-22.76%)</b></td><td>133.10 (+10.92%)</td><td>19.40 <b>(-57.59%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>226.30 (n/a)</td><td>174.42 (n/a)</td><td>183.20 (n/a)</td><td>120.00 (n/a)</td><td>45.75 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (+6.10%)</td><td>0.11 (-2.09%)</td><td>0.10 (-18.88%)</td><td>0.10 (+5.56%)</td><td>0.02 (+6.16%)</td><td>204.50 (-5.24%)</td><td>182.90 (+2.19%)</td><td>202.00 <b>(+23.25%)</b></td><td>144.10 (-5.76%)</td><td>28.28 (-3.41%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>215.80 (n/a)</td><td>178.98 (n/a)</td><td>163.90 (n/a)</td><td>152.90 (n/a)</td><td>29.28 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (+0.82%)</td><td>0.12 (-2.36%)</td><td>0.12 (+0.56%)</td><td>0.07 (-19.70%)</td><td>0.03 (+14.58%)</td><td>279.30 <b>(+24.52%)</b></td><td>187.06 (+4.55%)</td><td>166.70 (-0.60%)</td><td>144.90 (-0.82%)</td><td>53.00 <b>(+50.81%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>224.30 (n/a)</td><td>178.92 (n/a)</td><td>167.70 (n/a)</td><td>146.10 (n/a)</td><td>35.14 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (-8.64%)</td><td>0.16 (-10.38%)</td><td>0.17 (-12.20%)</td><td>0.13 (-2.18%)</td><td>0.03 (-10.19%)</td><td>187.40 (+2.18%)</td><td>157.58 (+11.38%)</td><td>146.20 (+13.86%)</td><td>129.90 (+9.53%)</td><td>27.16 (+2.71%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>183.40 (n/a)</td><td>141.48 (n/a)</td><td>128.40 (n/a)</td><td>118.60 (n/a)</td><td>26.44 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (-0.22%)</td><td>0.16 (-2.73%)</td><td>0.17 (+9.78%)</td><td>0.13 (-2.80%)</td><td>0.02 (-9.68%)</td><td>182.90 (+2.93%)</td><td>155.88 (+2.58%)</td><td>148.60 (-8.89%)</td><td>127.20 (+0.24%)</td><td>22.81 (-2.14%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>177.70 (n/a)</td><td>151.96 (n/a)</td><td>163.10 (n/a)</td><td>126.90 (n/a)</td><td>23.31 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.20 (+4.88%)</td><td>0.14 (-0.54%)</td><td>0.13 (+0.80%)</td><td>0.10 (-6.40%)</td><td>0.04 <b>(+23.70%)</b></td><td>237.90 (+6.83%)</td><td>190.64 (+2.79%)</td><td>190.40 (-0.78%)</td><td>122.60 (-4.67%)</td><td>48.27 <b>(+30.86%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>222.70 (n/a)</td><td>185.46 (n/a)</td><td>191.90 (n/a)</td><td>128.60 (n/a)</td><td>36.89 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.19 (+0.34%)</td><td>0.15 (-7.60%)</td><td>0.15 (-6.63%)</td><td>0.11 (-17.54%)</td><td>0.03 <b>(+36.98%)</b></td><td>230.80 <b>(+21.28%)</b></td><td>174.88 (+10.78%)</td><td>160.40 (+7.15%)</td><td>127.80 (-0.31%)</td><td>40.45 <b>(+66.21%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>190.30 (n/a)</td><td>157.86 (n/a)</td><td>149.70 (n/a)</td><td>128.20 (n/a)</td><td>24.34 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.17 (-11.16%)</td><td>0.15 (+6.08%)</td><td>0.15 <b>(+20.83%)</b></td><td>0.12 (+10.31%)</td><td>0.02 <b>(-43.83%)</b></td><td>201.90 (-9.34%)</td><td>167.76 (-8.45%)</td><td>159.70 (-17.21%)</td><td>142.20 (+12.59%)</td><td>23.10 <b>(-42.48%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>222.70 (n/a)</td><td>183.24 (n/a)</td><td>192.90 (n/a)</td><td>126.30 (n/a)</td><td>40.16 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.23 <b>(+58.66%)</b></td><td>0.15 <b>(+21.60%)</b></td><td>0.14 (+10.92%)</td><td>0.11 (+0.44%)</td><td>0.05 <b>(+267.20%)</b></td><td>221.10 (-0.45%)</td><td>172.66 (-12.91%)</td><td>176.80 (-9.84%)</td><td>106.60 <b>(-36.96%)</b></td><td>44.75 <b>(+128.17%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>222.10 (n/a)</td><td>198.26 (n/a)</td><td>196.10 (n/a)</td><td>169.10 (n/a)</td><td>19.61 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (-4.76%)</td><td>0.12 (-17.16%)</td><td>0.11 <b>(-21.34%)</b></td><td>0.09 <b>(-24.00%)</b></td><td>0.03 (+18.25%)</td><td>284.80 <b>(+31.55%)</b></td><td>216.00 <b>(+22.87%)</b></td><td>219.10 <b>(+27.16%)</b></td><td>157.40 (+5.00%)</td><td>46.25 <b>(+65.76%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>216.50 (n/a)</td><td>175.80 (n/a)</td><td>172.30 (n/a)</td><td>149.90 (n/a)</td><td>27.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.16 (+1.70%)</td><td>0.14 (+7.93%)</td><td>0.15 <b>(+25.57%)</b></td><td>0.11 (-5.09%)</td><td>0.02 (+10.59%)</td><td>231.20 (+5.38%)</td><td>176.02 (-6.87%)</td><td>159.40 <b>(-20.38%)</b></td><td>154.40 (-1.66%)</td><td>32.23 (+17.48%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>219.40 (n/a)</td><td>189.00 (n/a)</td><td>200.20 (n/a)</td><td>157.00 (n/a)</td><td>27.43 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.12 (-2.94%)</td><td>0.11 (+1.25%)</td><td>0.11 (+1.10%)</td><td>0.09 (+9.90%)</td><td>0.01 <b>(-22.42%)</b></td><td>194.50 (-9.03%)</td><td>176.58 (-1.80%)</td><td>173.80 (-1.08%)</td><td>155.20 (+3.05%)</td><td>17.34 <b>(-26.35%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>179.82 (n/a)</td><td>175.70 (n/a)</td><td>150.60 (n/a)</td><td>23.55 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 <b>(-24.97%)</b></td><td>0.10 (-18.66%)</td><td>0.10 <b>(-22.51%)</b></td><td>0.09 (+9.27%)</td><td>0.01 <b>(-69.81%)</b></td><td>201.40 (-8.50%)</td><td>186.86 (+18.69%)</td><td>191.80 <b>(+29.07%)</b></td><td>166.10 <b>(+33.31%)</b></td><td>13.58 <b>(-64.14%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>220.10 (n/a)</td><td>157.44 (n/a)</td><td>148.60 (n/a)</td><td>124.60 (n/a)</td><td>37.86 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.17 <b>(+39.24%)</b></td><td>0.11 (+6.46%)</td><td>0.10 (+1.15%)</td><td>0.08 (-2.66%)</td><td>0.03 <b>(+141.03%)</b></td><td>220.10 (+2.75%)</td><td>178.20 (-2.13%)</td><td>184.90 (-1.12%)</td><td>111.10 <b>(-28.18%)</b></td><td>40.61 <b>(+69.83%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>214.20 (n/a)</td><td>182.08 (n/a)</td><td>187.00 (n/a)</td><td>154.70 (n/a)</td><td>23.91 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (-6.44%)</td><td>0.11 (-5.23%)</td><td>0.11 (+11.37%)</td><td>0.08 <b>(-21.29%)</b></td><td>0.02 (-6.66%)</td><td>241.70 <b>(+27.01%)</b></td><td>175.72 (+6.05%)</td><td>169.80 (-10.21%)</td><td>131.00 (+6.85%)</td><td>41.54 <b>(+25.23%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>190.30 (n/a)</td><td>165.70 (n/a)</td><td>189.10 (n/a)</td><td>122.60 (n/a)</td><td>33.17 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (+12.69%)</td><td>0.11 (-1.43%)</td><td>0.10 (-13.68%)</td><td>0.09 (+6.11%)</td><td>0.02 <b>(+33.25%)</b></td><td>205.80 (-5.77%)</td><td>177.60 (+2.16%)</td><td>188.00 (+15.83%)</td><td>133.00 (-11.27%)</td><td>28.48 (+6.82%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>218.40 (n/a)</td><td>173.84 (n/a)</td><td>162.30 (n/a)</td><td>149.90 (n/a)</td><td>26.66 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.15 (+11.48%)</td><td>0.12 (+1.84%)</td><td>0.10 (-8.46%)</td><td>0.09 (-6.27%)</td><td>0.03 <b>(+45.57%)</b></td><td>215.80 (+6.73%)</td><td>165.72 (+0.67%)</td><td>177.80 (+9.21%)</td><td>121.40 (-10.34%)</td><td>40.70 <b>(+37.08%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>202.20 (n/a)</td><td>164.62 (n/a)</td><td>162.80 (n/a)</td><td>135.40 (n/a)</td><td>29.69 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.11 (+2.12%)</td><td>0.10 (+14.73%)</td><td>0.10 (+7.57%)</td><td>0.09 <b>(+59.29%)</b></td><td>0.01 <b>(-50.38%)</b></td><td>211.00 <b>(-37.22%)</b></td><td>191.64 (-16.69%)</td><td>190.50 (-7.03%)</td><td>164.70 (-2.08%)</td><td>19.02 <b>(-70.38%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>336.10 (n/a)</td><td>230.02 (n/a)</td><td>204.90 (n/a)</td><td>168.20 (n/a)</td><td>64.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.10 (+1.63%)</td><td>0.10 (+8.41%)</td><td>0.10 (+5.05%)</td><td>0.09 <b>(+24.26%)</b></td><td>0.00 <b>(-54.29%)</b></td><td>198.10 (-19.50%)</td><td>186.02 (-8.57%)</td><td>187.40 (-4.78%)</td><td>177.30 (-1.61%)</td><td>8.71 <b>(-65.05%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>246.10 (n/a)</td><td>203.46 (n/a)</td><td>196.80 (n/a)</td><td>180.20 (n/a)</td><td>24.92 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.63 (-17.52%)</td><td>0.51 (-17.25%)</td><td>0.53 <b>(-21.70%)</b></td><td>0.43 (-3.41%)</td><td>0.08 <b>(-38.62%)</b></td><td>226.10 (+3.53%)</td><td>194.38 (+18.58%)</td><td>186.90 <b>(+27.75%)</b></td><td>156.20 <b>(+21.27%)</b></td><td>28.22 <b>(-22.90%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.76 (n/a)</td><td>0.62 (n/a)</td><td>0.67 (n/a)</td><td>0.45 (n/a)</td><td>0.13 (n/a)</td><td>218.40 (n/a)</td><td>163.92 (n/a)</td><td>146.30 (n/a)</td><td>128.80 (n/a)</td><td>36.60 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.79 <b>(+21.77%)</b></td><td>0.64 <b>(+28.35%)</b></td><td>0.63 <b>(+30.97%)</b></td><td>0.57 <b>(+48.28%)</b></td><td>0.09 (-17.72%)</td><td>174.00 <b>(-32.56%)</b></td><td>154.80 <b>(-23.86%)</b></td><td>155.40 <b>(-23.64%)</b></td><td>123.80 (-17.90%)</td><td>19.15 <b>(-55.19%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.65 (n/a)</td><td>0.50 (n/a)</td><td>0.48 (n/a)</td><td>0.38 (n/a)</td><td>0.11 (n/a)</td><td>258.00 (n/a)</td><td>203.30 (n/a)</td><td>203.50 (n/a)</td><td>150.80 (n/a)</td><td>42.74 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.77 <b>(+28.20%)</b></td><td>0.56 (+7.13%)</td><td>0.51 (-1.18%)</td><td>0.44 (+2.90%)</td><td>0.14 <b>(+114.28%)</b></td><td>221.10 (-2.81%)</td><td>182.42 (-3.79%)</td><td>192.90 (+1.21%)</td><td>128.00 <b>(-21.95%)</b></td><td>39.59 <b>(+62.99%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.60 (n/a)</td><td>0.52 (n/a)</td><td>0.52 (n/a)</td><td>0.43 (n/a)</td><td>0.06 (n/a)</td><td>227.50 (n/a)</td><td>189.60 (n/a)</td><td>190.60 (n/a)</td><td>164.00 (n/a)</td><td>24.29 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.75 (-8.59%)</td><td>0.57 (-9.34%)</td><td>0.53 (-6.92%)</td><td>0.37 <b>(-23.21%)</b></td><td>0.16 <b>(+23.92%)</b></td><td>263.60 <b>(+30.24%)</b></td><td>186.32 (+14.33%)</td><td>186.10 (+7.45%)</td><td>131.90 (+9.37%)</td><td>55.23 <b>(+71.44%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.82 (n/a)</td><td>0.62 (n/a)</td><td>0.57 (n/a)</td><td>0.49 (n/a)</td><td>0.13 (n/a)</td><td>202.40 (n/a)</td><td>162.96 (n/a)</td><td>173.20 (n/a)</td><td>120.60 (n/a)</td><td>32.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.41 <b>(-32.25%)</b></td><td>0.40 <b>(-20.29%)</b></td><td>0.40 <b>(-26.46%)</b></td><td>0.39 (+6.18%)</td><td>0.01 <b>(-92.89%)</b></td><td>190.00 (-5.80%)</td><td>185.66 <b>(+21.28%)</b></td><td>186.00 <b>(+35.96%)</b></td><td>181.20 <b>(+47.68%)</b></td><td>3.24 <b>(-90.18%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.60 (n/a)</td><td>0.50 (n/a)</td><td>0.54 (n/a)</td><td>0.37 (n/a)</td><td>0.10 (n/a)</td><td>201.70 (n/a)</td><td>153.08 (n/a)</td><td>136.80 (n/a)</td><td>122.70 (n/a)</td><td>32.99 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.49 (-9.84%)</td><td>0.40 (-6.59%)</td><td>0.39 (+2.25%)</td><td>0.30 (-16.13%)</td><td>0.07 (-17.31%)</td><td>249.00 (+19.25%)</td><td>190.44 (+6.65%)</td><td>189.90 (-2.21%)</td><td>150.30 (+10.92%)</td><td>37.90 (+8.60%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.54 (n/a)</td><td>0.43 (n/a)</td><td>0.38 (n/a)</td><td>0.35 (n/a)</td><td>0.09 (n/a)</td><td>208.80 (n/a)</td><td>178.56 (n/a)</td><td>194.20 (n/a)</td><td>135.50 (n/a)</td><td>34.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.60 <b>(+33.86%)</b></td><td>0.42 <b>(+27.77%)</b></td><td>0.37 <b>(+21.27%)</b></td><td>0.33 <b>(+61.04%)</b></td><td>0.11 (+12.49%)</td><td>225.00 <b>(-37.91%)</b></td><td>181.72 <b>(-24.06%)</b></td><td>197.40 (-17.54%)</td><td>123.70 <b>(-25.30%)</b></td><td>40.69 <b>(-47.80%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.45 (n/a)</td><td>0.33 (n/a)</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.10 (n/a)</td><td>362.40 (n/a)</td><td>239.30 (n/a)</td><td>239.40 (n/a)</td><td>165.60 (n/a)</td><td>77.96 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.56 <b>(+33.09%)</b></td><td>0.44 <b>(+25.04%)</b></td><td>0.41 <b>(+23.03%)</b></td><td>0.38 (+15.95%)</td><td>0.08 <b>(+95.71%)</b></td><td>194.20 (-13.77%)</td><td>170.24 (-18.90%)</td><td>181.00 (-18.72%)</td><td>131.40 <b>(-24.87%)</b></td><td>27.83 <b>(+28.18%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.42 (n/a)</td><td>0.35 (n/a)</td><td>0.33 (n/a)</td><td>0.33 (n/a)</td><td>0.04 (n/a)</td><td>225.20 (n/a)</td><td>209.92 (n/a)</td><td>222.70 (n/a)</td><td>174.90 (n/a)</td><td>21.71 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (+4.36%)</td><td>0.22 (+3.38%)</td><td>0.21 (+0.45%)</td><td>0.20 (+6.73%)</td><td>0.02 (+0.35%)</td><td>184.30 (-6.30%)</td><td>169.24 (-3.35%)</td><td>172.50 (-0.46%)</td><td>144.20 (-4.19%)</td><td>15.00 (-10.98%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>196.70 (n/a)</td><td>175.10 (n/a)</td><td>173.30 (n/a)</td><td>150.50 (n/a)</td><td>16.86 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (+7.99%)</td><td>0.21 (-1.40%)</td><td>0.21 (-0.37%)</td><td>0.18 (-7.69%)</td><td>0.02 <b>(+113.19%)</b></td><td>208.40 (+8.37%)</td><td>181.58 (+2.31%)</td><td>178.70 (+0.34%)</td><td>153.50 (-7.42%)</td><td>21.25 <b>(+114.09%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>192.30 (n/a)</td><td>177.48 (n/a)</td><td>178.10 (n/a)</td><td>165.80 (n/a)</td><td>9.92 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.34 (+19.21%)</td><td>0.26 <b>(+24.10%)</b></td><td>0.25 <b>(+20.54%)</b></td><td>0.19 <b>(+24.01%)</b></td><td>0.05 (+2.60%)</td><td>189.20 (-19.35%)</td><td>146.96 <b>(-20.58%)</b></td><td>149.60 (-17.07%)</td><td>108.60 (-16.14%)</td><td>29.48 <b>(-32.30%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>234.60 (n/a)</td><td>185.04 (n/a)</td><td>180.40 (n/a)</td><td>129.50 (n/a)</td><td>43.54 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.27 (-18.85%)</td><td>0.23 (-7.34%)</td><td>0.22 (+5.19%)</td><td>0.19 (-0.50%)</td><td>0.03 <b>(-53.12%)</b></td><td>189.50 (+0.53%)</td><td>165.68 (+4.24%)</td><td>170.40 (-4.96%)</td><td>138.00 <b>(+23.21%)</b></td><td>20.47 <b>(-43.65%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.33 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>188.50 (n/a)</td><td>158.94 (n/a)</td><td>179.30 (n/a)</td><td>112.00 (n/a)</td><td>36.33 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (-11.52%)</td><td>0.22 (-3.81%)</td><td>0.22 (+0.78%)</td><td>0.20 (-5.17%)</td><td>0.02 <b>(-32.89%)</b></td><td>186.90 (+5.41%)</td><td>166.08 (+3.18%)</td><td>171.20 (-0.75%)</td><td>141.80 (+13.08%)</td><td>17.09 <b>(-20.16%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>177.30 (n/a)</td><td>160.96 (n/a)</td><td>172.50 (n/a)</td><td>125.40 (n/a)</td><td>21.40 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (+15.57%)</td><td>0.21 (+9.24%)</td><td>0.19 (-2.36%)</td><td>0.17 (+7.32%)</td><td>0.04 <b>(+48.09%)</b></td><td>211.50 (-6.79%)</td><td>180.88 (-7.54%)</td><td>192.20 (+2.40%)</td><td>144.20 (-13.50%)</td><td>30.25 (+17.27%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>226.90 (n/a)</td><td>195.62 (n/a)</td><td>187.70 (n/a)</td><td>166.70 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (+7.93%)</td><td>0.22 (+14.26%)</td><td>0.23 (+19.87%)</td><td>0.18 <b>(+51.25%)</b></td><td>0.03 <b>(-37.58%)</b></td><td>202.00 <b>(-33.88%)</b></td><td>170.64 (-16.49%)</td><td>163.40 (-16.59%)</td><td>140.90 (-7.36%)</td><td>23.91 <b>(-61.28%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>305.50 (n/a)</td><td>204.34 (n/a)</td><td>195.90 (n/a)</td><td>152.10 (n/a)</td><td>61.76 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.21 (-11.39%)</td><td>0.17 (-11.59%)</td><td>0.17 (-11.33%)</td><td>0.12 <b>(-22.67%)</b></td><td>0.04 (+16.38%)</td><td>313.20 <b>(+29.31%)</b></td><td>222.64 (+15.50%)</td><td>221.30 (+12.79%)</td><td>175.40 (+12.87%)</td><td>55.35 <b>(+68.81%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>242.20 (n/a)</td><td>192.76 (n/a)</td><td>196.20 (n/a)</td><td>155.40 (n/a)</td><td>32.79 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.30 (-7.50%)</td><td>0.25 (-1.64%)</td><td>0.23 (+5.88%)</td><td>0.20 (+1.98%)</td><td>0.04 <b>(-26.64%)</b></td><td>203.60 (-1.93%)</td><td>170.24 (+0.05%)</td><td>177.70 (-5.58%)</td><td>137.90 (+8.16%)</td><td>27.65 <b>(-22.26%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.06 (n/a)</td><td>207.60 (n/a)</td><td>170.16 (n/a)</td><td>188.20 (n/a)</td><td>127.50 (n/a)</td><td>35.57 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (-18.11%)</td><td>0.21 (-7.41%)</td><td>0.21 (-5.54%)</td><td>0.18 (-4.79%)</td><td>0.03 <b>(-31.96%)</b></td><td>224.20 (+5.01%)</td><td>197.46 (+7.11%)</td><td>192.70 (+5.88%)</td><td>173.00 <b>(+22.09%)</b></td><td>24.96 (-12.06%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>213.50 (n/a)</td><td>184.36 (n/a)</td><td>182.00 (n/a)</td><td>141.70 (n/a)</td><td>28.38 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.29 <b>(-20.78%)</b></td><td>0.24 (+0.02%)</td><td>0.23 (+12.92%)</td><td>0.21 (+16.75%)</td><td>0.03 <b>(-55.06%)</b></td><td>193.80 (-14.36%)</td><td>171.66 (-5.33%)</td><td>180.90 (-11.45%)</td><td>143.10 <b>(+26.30%)</b></td><td>23.49 <b>(-52.07%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.36 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.08 (n/a)</td><td>226.30 (n/a)</td><td>181.32 (n/a)</td><td>204.30 (n/a)</td><td>113.30 (n/a)</td><td>49.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.34 (+5.13%)</td><td>0.25 (+11.26%)</td><td>0.24 <b>(+20.40%)</b></td><td>0.19 <b>(+20.69%)</b></td><td>0.06 (-15.16%)</td><td>212.80 (-17.13%)</td><td>170.18 (-12.45%)</td><td>171.40 (-16.92%)</td><td>121.00 (-4.87%)</td><td>33.82 <b>(-33.71%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.32 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>256.80 (n/a)</td><td>194.38 (n/a)</td><td>206.30 (n/a)</td><td>127.20 (n/a)</td><td>51.02 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.30 (-2.69%)</td><td>0.23 (+1.73%)</td><td>0.22 (+11.05%)</td><td>0.20 (+4.64%)</td><td>0.04 (-18.98%)</td><td>208.80 (-4.44%)</td><td>178.96 (-2.95%)</td><td>183.60 (-9.96%)</td><td>136.20 (+2.71%)</td><td>28.47 <b>(-21.27%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>218.50 (n/a)</td><td>184.40 (n/a)</td><td>203.90 (n/a)</td><td>132.60 (n/a)</td><td>36.16 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.30 (+19.45%)</td><td>0.23 (+1.90%)</td><td>0.23 (+1.85%)</td><td>0.18 (-1.48%)</td><td>0.05 <b>(+79.10%)</b></td><td>230.90 (+1.49%)</td><td>188.74 (+0.43%)</td><td>180.60 (-1.79%)</td><td>135.90 (-16.32%)</td><td>38.92 <b>(+53.84%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>227.50 (n/a)</td><td>187.94 (n/a)</td><td>183.90 (n/a)</td><td>162.40 (n/a)</td><td>25.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.33 <b>(+26.05%)</b></td><td>0.22 (+7.76%)</td><td>0.20 (-1.36%)</td><td>0.17 (+11.29%)</td><td>0.07 <b>(+66.97%)</b></td><td>246.30 (-10.14%)</td><td>198.32 (-4.34%)</td><td>203.50 (+1.34%)</td><td>124.70 <b>(-20.67%)</b></td><td>50.45 (+18.50%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>274.10 (n/a)</td><td>207.32 (n/a)</td><td>200.80 (n/a)</td><td>157.20 (n/a)</td><td>42.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.29 (+3.26%)</td><td>0.23 (+0.92%)</td><td>0.21 (-5.21%)</td><td>0.20 (+7.67%)</td><td>0.04 (+4.01%)</td><td>202.30 (-7.12%)</td><td>181.58 (-0.95%)</td><td>194.60 (+5.47%)</td><td>142.90 (-3.18%)</td><td>24.79 (-5.81%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>217.80 (n/a)</td><td>183.32 (n/a)</td><td>184.50 (n/a)</td><td>147.60 (n/a)</td><td>26.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (-17.89%)</td><td>0.21 (-0.75%)</td><td>0.21 (+1.48%)</td><td>0.18 (+9.00%)</td><td>0.02 <b>(-58.55%)</b></td><td>192.20 (-8.26%)</td><td>168.74 (-2.51%)</td><td>169.40 (-1.45%)</td><td>145.80 <b>(+21.70%)</b></td><td>16.78 <b>(-54.15%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.29 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>209.50 (n/a)</td><td>173.08 (n/a)</td><td>171.90 (n/a)</td><td>119.80 (n/a)</td><td>36.61 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 (+6.97%)</td><td>0.19 (-0.60%)</td><td>0.18 (-7.48%)</td><td>0.17 (+2.16%)</td><td>0.03 <b>(+40.45%)</b></td><td>202.40 (-2.13%)</td><td>182.86 (+1.31%)</td><td>195.00 (+8.09%)</td><td>146.20 (-6.52%)</td><td>24.18 <b>(+29.48%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>206.80 (n/a)</td><td>180.50 (n/a)</td><td>180.40 (n/a)</td><td>156.40 (n/a)</td><td>18.67 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (+5.49%)</td><td>0.21 (+5.41%)</td><td>0.21 (+12.76%)</td><td>0.16 (-4.30%)</td><td>0.04 <b>(+27.68%)</b></td><td>212.30 (+4.48%)</td><td>169.06 (-4.20%)</td><td>163.90 (-11.31%)</td><td>135.30 (-5.19%)</td><td>30.60 <b>(+27.66%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>203.20 (n/a)</td><td>176.48 (n/a)</td><td>184.80 (n/a)</td><td>142.70 (n/a)</td><td>23.97 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.28 (+19.84%)</td><td>0.22 (+8.77%)</td><td>0.19 (-0.96%)</td><td>0.16 (-6.77%)</td><td>0.06 <b>(+125.67%)</b></td><td>211.10 (+7.27%)</td><td>168.90 (-4.43%)</td><td>187.10 (+0.97%)</td><td>122.20 (-16.59%)</td><td>40.45 <b>(+98.26%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>196.80 (n/a)</td><td>176.72 (n/a)</td><td>185.30 (n/a)</td><td>146.50 (n/a)</td><td>20.40 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.31 <b>(+30.79%)</b></td><td>0.21 (+0.09%)</td><td>0.19 (-5.52%)</td><td>0.17 (+2.16%)</td><td>0.06 <b>(+114.24%)</b></td><td>199.50 (-2.16%)</td><td>175.28 (+3.18%)</td><td>183.30 (+5.83%)</td><td>112.50 <b>(-23.52%)</b></td><td>36.03 <b>(+58.12%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>203.90 (n/a)</td><td>169.88 (n/a)</td><td>173.20 (n/a)</td><td>147.10 (n/a)</td><td>22.78 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.31 (+4.37%)</td><td>0.23 (+3.99%)</td><td>0.24 (+12.06%)</td><td>0.17 (-5.74%)</td><td>0.06 <b>(+21.19%)</b></td><td>206.90 (+6.10%)</td><td>157.68 (-2.28%)</td><td>146.30 (-10.79%)</td><td>111.20 (-4.22%)</td><td>37.47 <b>(+28.75%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>195.00 (n/a)</td><td>161.36 (n/a)</td><td>164.00 (n/a)</td><td>116.10 (n/a)</td><td>29.10 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.22 (-1.57%)</td><td>0.19 (+10.98%)</td><td>0.18 (+0.66%)</td><td>0.17 <b>(+59.72%)</b></td><td>0.02 <b>(-60.29%)</b></td><td>199.80 <b>(-37.39%)</b></td><td>185.40 (-14.67%)</td><td>188.50 (-0.68%)</td><td>161.80 (+1.63%)</td><td>16.03 <b>(-75.01%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>319.10 (n/a)</td><td>217.28 (n/a)</td><td>189.80 (n/a)</td><td>159.20 (n/a)</td><td>64.14 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.24 <b>(+25.23%)</b></td><td>0.20 (+16.75%)</td><td>0.20 (+11.26%)</td><td>0.17 <b>(+28.95%)</b></td><td>0.03 (+14.76%)</td><td>201.30 <b>(-22.43%)</b></td><td>176.18 (-14.64%)</td><td>175.10 (-10.11%)</td><td>142.40 <b>(-20.13%)</b></td><td>21.88 <b>(-31.50%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>259.50 (n/a)</td><td>206.40 (n/a)</td><td>194.80 (n/a)</td><td>178.30 (n/a)</td><td>31.94 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.93 (-9.82%)</td><td>0.78 (-8.48%)</td><td>0.78 (-6.14%)</td><td>0.68 (-0.07%)</td><td>0.10 <b>(-31.37%)</b></td><td>193.30 (+0.05%)</td><td>171.04 (+8.01%)</td><td>169.10 (+6.55%)</td><td>141.00 (+10.85%)</td><td>21.86 <b>(-21.98%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.03 (n/a)</td><td>0.85 (n/a)</td><td>0.83 (n/a)</td><td>0.68 (n/a)</td><td>0.15 (n/a)</td><td>193.20 (n/a)</td><td>158.36 (n/a)</td><td>158.70 (n/a)</td><td>127.20 (n/a)</td><td>28.01 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.88 (-17.77%)</td><td>0.78 (-11.55%)</td><td>0.77 (-3.26%)</td><td>0.67 (-12.77%)</td><td>0.08 <b>(-42.00%)</b></td><td>196.40 (+14.65%)</td><td>170.54 (+11.98%)</td><td>171.00 (+3.39%)</td><td>148.40 <b>(+21.64%)</b></td><td>17.61 (-19.61%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.07 (n/a)</td><td>0.88 (n/a)</td><td>0.79 (n/a)</td><td>0.77 (n/a)</td><td>0.14 (n/a)</td><td>171.30 (n/a)</td><td>152.30 (n/a)</td><td>165.40 (n/a)</td><td>122.00 (n/a)</td><td>21.91 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.94 (-17.31%)</td><td>0.75 <b>(-22.04%)</b></td><td>0.70 <b>(-23.27%)</b></td><td>0.64 <b>(-23.80%)</b></td><td>0.12 (-8.35%)</td><td>204.40 <b>(+31.28%)</b></td><td>178.80 <b>(+28.87%)</b></td><td>188.00 <b>(+30.28%)</b></td><td>139.90 <b>(+21.02%)</b></td><td>26.56 <b>(+43.91%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.13 (n/a)</td><td>0.96 (n/a)</td><td>0.91 (n/a)</td><td>0.84 (n/a)</td><td>0.13 (n/a)</td><td>155.70 (n/a)</td><td>138.74 (n/a)</td><td>144.30 (n/a)</td><td>115.60 (n/a)</td><td>18.46 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-13.16%)</td><td>0.03 (-17.15%)</td><td>0.03 (-18.39%)</td><td>0.02 (-15.64%)</td><td>0.00 (-15.83%)</td><td>221.80 (+18.55%)</td><td>164.58 <b>(+20.62%)</b></td><td>155.30 <b>(+22.57%)</b></td><td>135.40 (+15.14%)</td><td>33.15 (+16.00%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>187.10 (n/a)</td><td>136.44 (n/a)</td><td>126.70 (n/a)</td><td>117.60 (n/a)</td><td>28.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 <b>(-26.31%)</b></td><td>0.03 (-11.91%)</td><td>0.03 (-5.54%)</td><td>0.02 (+8.27%)</td><td>0.00 <b>(-59.10%)</b></td><td>171.50 (-7.65%)</td><td>156.14 (+9.07%)</td><td>160.30 (+5.88%)</td><td>126.90 <b>(+35.72%)</b></td><td>17.72 <b>(-47.35%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>185.70 (n/a)</td><td>143.16 (n/a)</td><td>151.40 (n/a)</td><td>93.50 (n/a)</td><td>33.66 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-8.06%)</td><td>0.03 (+16.32%)</td><td>0.03 <b>(+29.94%)</b></td><td>0.03 <b>(+29.91%)</b></td><td>0.00 <b>(-71.35%)</b></td><td>154.70 <b>(-23.03%)</b></td><td>143.28 (-16.78%)</td><td>142.10 <b>(-23.02%)</b></td><td>135.40 (+8.76%)</td><td>7.92 <b>(-76.53%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>201.00 (n/a)</td><td>172.16 (n/a)</td><td>184.60 (n/a)</td><td>124.50 (n/a)</td><td>33.74 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>17.27 (+0.53%)</td><td>12.75 (-10.22%)</td><td>11.70 <b>(-20.98%)</b></td><td>10.33 (-5.11%)</td><td>2.70 (+5.59%)</td><td>203.00 (+5.35%)</td><td>169.72 (+11.73%)</td><td>179.30 <b>(+26.53%)</b></td><td>121.50 (-0.49%)</td><td>30.74 (+6.37%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>17.18 (n/a)</td><td>14.20 (n/a)</td><td>14.81 (n/a)</td><td>10.89 (n/a)</td><td>2.56 (n/a)</td><td>192.70 (n/a)</td><td>151.90 (n/a)</td><td>141.70 (n/a)</td><td>122.10 (n/a)</td><td>28.90 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.91 (-16.07%)</td><td>0.86 (-16.11%)</td><td>0.89 (-13.37%)</td><td>0.69 <b>(-25.53%)</b></td><td>0.09 <b>(+39.52%)</b></td><td>190.70 <b>(+34.30%)</b></td><td>155.56 <b>(+20.14%)</b></td><td>148.70 (+15.45%)</td><td>144.60 (+19.21%)</td><td>19.76 <b>(+127.54%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.09 (n/a)</td><td>1.02 (n/a)</td><td>1.03 (n/a)</td><td>0.93 (n/a)</td><td>0.07 (n/a)</td><td>142.00 (n/a)</td><td>129.48 (n/a)</td><td>128.80 (n/a)</td><td>121.30 (n/a)</td><td>8.68 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.03 (+9.92%)</td><td>0.84 (-2.25%)</td><td>0.87 (-4.27%)</td><td>0.68 (+3.36%)</td><td>0.15 <b>(+31.18%)</b></td><td>193.60 (-3.25%)</td><td>161.60 (+3.21%)</td><td>152.50 (+4.45%)</td><td>128.80 (-8.98%)</td><td>28.78 (+16.94%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.93 (n/a)</td><td>0.86 (n/a)</td><td>0.90 (n/a)</td><td>0.66 (n/a)</td><td>0.11 (n/a)</td><td>200.10 (n/a)</td><td>156.58 (n/a)</td><td>146.00 (n/a)</td><td>141.50 (n/a)</td><td>24.61 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.99 (-2.82%)</td><td>0.79 (-9.66%)</td><td>0.83 (-2.75%)</td><td>0.59 (-11.33%)</td><td>0.16 (+11.50%)</td><td>222.80 (+12.75%)</td><td>172.38 (+11.82%)</td><td>159.10 (+2.84%)</td><td>132.80 (+2.87%)</td><td>35.55 <b>(+30.93%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.02 (n/a)</td><td>0.88 (n/a)</td><td>0.85 (n/a)</td><td>0.67 (n/a)</td><td>0.14 (n/a)</td><td>197.60 (n/a)</td><td>154.16 (n/a)</td><td>154.70 (n/a)</td><td>129.10 (n/a)</td><td>27.16 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.00 (-17.87%)</td><td>0.79 (-15.95%)</td><td>0.81 (-10.17%)</td><td>0.63 (-9.23%)</td><td>0.14 <b>(-30.17%)</b></td><td>209.00 (+10.17%)</td><td>170.40 (+17.60%)</td><td>164.00 (+11.34%)</td><td>132.40 <b>(+21.80%)</b></td><td>28.23 (-6.82%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.22 (n/a)</td><td>0.94 (n/a)</td><td>0.90 (n/a)</td><td>0.70 (n/a)</td><td>0.19 (n/a)</td><td>189.70 (n/a)</td><td>144.90 (n/a)</td><td>147.30 (n/a)</td><td>108.70 (n/a)</td><td>30.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.02 (+0.76%)</td><td>0.92 (+2.06%)</td><td>0.97 (+11.28%)</td><td>0.75 (-9.19%)</td><td>0.11 <b>(+57.44%)</b></td><td>177.20 (+10.06%)</td><td>145.96 (-1.19%)</td><td>136.10 (-10.17%)</td><td>129.40 (-0.77%)</td><td>19.88 <b>(+73.27%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.01 (n/a)</td><td>0.90 (n/a)</td><td>0.87 (n/a)</td><td>0.82 (n/a)</td><td>0.07 (n/a)</td><td>161.00 (n/a)</td><td>147.72 (n/a)</td><td>151.50 (n/a)</td><td>130.40 (n/a)</td><td>11.48 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-5.93%)</td><td>0.03 (-0.20%)</td><td>0.03 (+4.67%)</td><td>0.02 (-6.71%)</td><td>0.00 (-7.32%)</td><td>178.50 (+7.14%)</td><td>147.60 (+0.20%)</td><td>141.70 (-4.45%)</td><td>134.00 (+6.35%)</td><td>17.64 (+8.09%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>166.60 (n/a)</td><td>147.30 (n/a)</td><td>148.30 (n/a)</td><td>126.00 (n/a)</td><td>16.32 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.03 (-8.07%)</td><td>0.03 (+0.44%)</td><td>0.03 (-1.38%)</td><td>0.02 (+8.58%)</td><td>0.00 <b>(-40.07%)</b></td><td>181.90 (-7.90%)</td><td>159.10 (-1.80%)</td><td>158.70 (+1.41%)</td><td>137.60 (+8.77%)</td><td>15.75 <b>(-39.68%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.50 (n/a)</td><td>162.02 (n/a)</td><td>156.50 (n/a)</td><td>126.50 (n/a)</td><td>26.12 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.00 (-2.22%)</td><td>0.00 (-3.18%)</td><td>0.00 (-2.27%)</td><td>0.00 (-6.98%)</td><td>0.00 <b>(+51.66%)</b></td><td>1031.52 (+7.09%)</td><td>965.00 (+3.29%)</td><td>947.79 (+2.79%)</td><td>939.21 (+2.41%)</td><td>38.33 <b>(+86.33%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>963.25 (n/a)</td><td>934.26 (n/a)</td><td>922.09 (n/a)</td><td>917.13 (n/a)</td><td>20.57 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.01 (+2.44%)</td><td>0.01 (+1.25%)</td><td>0.01 (+1.23%)</td><td>0.01 (-1.30%)</td><td>0.00 <b>(+50.00%)</b></td><td>1082.65 (+2.05%)</td><td>1013.31 (-1.03%)</td><td>995.20 (-2.00%)</td><td>980.77 (-1.42%)</td><td>40.58 <b>(+64.83%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1060.86 (n/a)</td><td>1023.82 (n/a)</td><td>1015.55 (n/a)</td><td>994.87 (n/a)</td><td>24.62 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.00 (+2.52%)</td><td>0.97 (+2.77%)</td><td>0.98 (+3.79%)</td><td>0.96 (+3.26%)</td><td>0.01 (-10.41%)</td><td>2185.78 (-3.15%)</td><td>2153.41 (-2.70%)</td><td>2147.04 (-3.65%)</td><td>2106.49 (-2.45%)</td><td>32.81 (-15.16%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.97 (n/a)</td><td>0.95 (n/a)</td><td>0.94 (n/a)</td><td>0.93 (n/a)</td><td>0.02 (n/a)</td><td>2256.91 (n/a)</td><td>2213.15 (n/a)</td><td>2228.31 (n/a)</td><td>2159.48 (n/a)</td><td>38.67 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>5.22 (-10.31%)</td><td>4.57 (-8.85%)</td><td>4.43 (-14.01%)</td><td>4.02 (-5.39%)</td><td>0.51 (-17.96%)</td><td>261.20 (+5.71%)</td><td>231.90 (+9.44%)</td><td>236.90 (+16.30%)</td><td>201.00 (+11.54%)</td><td>25.40 (-4.73%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>5.82 (n/a)</td><td>5.01 (n/a)</td><td>5.15 (n/a)</td><td>4.24 (n/a)</td><td>0.62 (n/a)</td><td>247.10 (n/a)</td><td>211.90 (n/a)</td><td>203.70 (n/a)</td><td>180.20 (n/a)</td><td>26.66 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>5.16 (-7.84%)</td><td>4.55 (-9.19%)</td><td>4.54 (-7.29%)</td><td>3.96 (-10.89%)</td><td>0.50 (+9.20%)</td><td>264.50 (+12.22%)</td><td>232.50 (+10.46%)</td><td>230.90 (+7.90%)</td><td>203.10 (+8.49%)</td><td>25.75 <b>(+33.80%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>5.60 (n/a)</td><td>5.02 (n/a)</td><td>4.90 (n/a)</td><td>4.45 (n/a)</td><td>0.46 (n/a)</td><td>235.70 (n/a)</td><td>210.48 (n/a)</td><td>214.00 (n/a)</td><td>187.20 (n/a)</td><td>19.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>5.77 (+2.54%)</td><td>4.90 (+1.81%)</td><td>5.07 (+7.08%)</td><td>3.96 (-8.40%)</td><td>0.69 <b>(+40.90%)</b></td><td>264.50 (+9.16%)</td><td>217.60 (-0.88%)</td><td>206.90 (-6.59%)</td><td>181.60 (-2.47%)</td><td>31.98 <b>(+54.41%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>5.63 (n/a)</td><td>4.81 (n/a)</td><td>4.73 (n/a)</td><td>4.33 (n/a)</td><td>0.49 (n/a)</td><td>242.30 (n/a)</td><td>219.54 (n/a)</td><td>221.50 (n/a)</td><td>186.20 (n/a)</td><td>20.71 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>6.33 (-1.22%)</td><td>5.27 (-0.53%)</td><td>5.04 (-8.14%)</td><td>4.50 (+19.78%)</td><td>0.68 <b>(-29.29%)</b></td><td>232.90 (-16.52%)</td><td>201.52 (-1.33%)</td><td>207.90 (+8.91%)</td><td>165.60 (+1.22%)</td><td>24.79 <b>(-43.56%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>6.41 (n/a)</td><td>5.30 (n/a)</td><td>5.49 (n/a)</td><td>3.76 (n/a)</td><td>0.97 (n/a)</td><td>279.00 (n/a)</td><td>204.24 (n/a)</td><td>190.90 (n/a)</td><td>163.60 (n/a)</td><td>43.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>8.99 (+3.55%)</td><td>8.00 (+2.75%)</td><td>7.94 (-0.02%)</td><td>7.14 (+5.68%)</td><td>0.67 <b>(-21.53%)</b></td><td>293.80 (-5.38%)</td><td>263.68 (-3.11%)</td><td>264.10 (+0.00%)</td><td>233.20 (-3.44%)</td><td>21.97 <b>(-28.50%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>8.68 (n/a)</td><td>7.78 (n/a)</td><td>7.94 (n/a)</td><td>6.75 (n/a)</td><td>0.86 (n/a)</td><td>310.50 (n/a)</td><td>272.14 (n/a)</td><td>264.10 (n/a)</td><td>241.50 (n/a)</td><td>30.72 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>8.86 (+4.11%)</td><td>8.10 (+2.67%)</td><td>8.31 (+1.52%)</td><td>7.01 (+1.41%)</td><td>0.72 (+8.12%)</td><td>299.20 (-1.38%)</td><td>260.68 (-2.53%)</td><td>252.40 (-1.48%)</td><td>236.70 (-3.94%)</td><td>24.59 (+3.17%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>8.51 (n/a)</td><td>7.89 (n/a)</td><td>8.19 (n/a)</td><td>6.91 (n/a)</td><td>0.67 (n/a)</td><td>303.40 (n/a)</td><td>267.44 (n/a)</td><td>256.20 (n/a)</td><td>246.40 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>8.96 (+7.58%)</td><td>7.67 (-2.27%)</td><td>7.19 (-7.51%)</td><td>6.98 (-3.16%)</td><td>0.86 <b>(+90.42%)</b></td><td>300.50 (+3.26%)</td><td>275.96 (+3.02%)</td><td>291.80 (+8.11%)</td><td>233.90 (-7.07%)</td><td>29.05 <b>(+85.14%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>8.33 (n/a)</td><td>7.85 (n/a)</td><td>7.77 (n/a)</td><td>7.21 (n/a)</td><td>0.45 (n/a)</td><td>291.00 (n/a)</td><td>267.88 (n/a)</td><td>269.90 (n/a)</td><td>251.70 (n/a)</td><td>15.69 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>10.27 (+9.19%)</td><td>9.04 (+13.50%)</td><td>9.06 (+12.30%)</td><td>7.50 <b>(+22.98%)</b></td><td>1.02 (-18.41%)</td><td>279.60 (-18.70%)</td><td>234.52 (-12.86%)</td><td>231.40 (-10.93%)</td><td>204.10 (-8.43%)</td><td>28.27 <b>(-39.33%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>9.41 (n/a)</td><td>7.96 (n/a)</td><td>8.07 (n/a)</td><td>6.10 (n/a)</td><td>1.26 (n/a)</td><td>343.90 (n/a)</td><td>269.14 (n/a)</td><td>259.80 (n/a)</td><td>222.90 (n/a)</td><td>46.60 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>10.91 (+16.31%)</td><td>9.48 (+19.39%)</td><td>9.71 <b>(+21.70%)</b></td><td>8.04 (+16.73%)</td><td>1.16 (+17.31%)</td><td>261.00 (-14.31%)</td><td>224.02 (-16.22%)</td><td>216.10 (-17.80%)</td><td>192.20 (-14.04%)</td><td>28.04 (-13.44%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>9.38 (n/a)</td><td>7.94 (n/a)</td><td>7.98 (n/a)</td><td>6.88 (n/a)</td><td>0.99 (n/a)</td><td>304.60 (n/a)</td><td>267.38 (n/a)</td><td>262.90 (n/a)</td><td>223.60 (n/a)</td><td>32.40 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>12.02 <b>(+25.56%)</b></td><td>10.10 (+18.58%)</td><td>9.98 (+16.14%)</td><td>8.87 <b>(+20.33%)</b></td><td>1.26 <b>(+48.74%)</b></td><td>236.30 (-16.88%)</td><td>210.18 (-15.35%)</td><td>210.20 (-13.89%)</td><td>174.50 <b>(-20.36%)</b></td><td>24.86 (-1.44%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>9.57 (n/a)</td><td>8.52 (n/a)</td><td>8.59 (n/a)</td><td>7.38 (n/a)</td><td>0.85 (n/a)</td><td>284.30 (n/a)</td><td>248.30 (n/a)</td><td>244.10 (n/a)</td><td>219.10 (n/a)</td><td>25.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>13.16 (+3.24%)</td><td>11.69 (+5.00%)</td><td>11.72 (+10.91%)</td><td>10.48 (+0.42%)</td><td>1.08 (+8.05%)</td><td>400.30 (-0.42%)</td><td>361.18 (-4.69%)</td><td>357.80 (-9.85%)</td><td>318.80 (-3.13%)</td><td>32.93 (+3.97%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>12.74 (n/a)</td><td>11.13 (n/a)</td><td>10.57 (n/a)</td><td>10.43 (n/a)</td><td>1.00 (n/a)</td><td>402.00 (n/a)</td><td>378.96 (n/a)</td><td>396.90 (n/a)</td><td>329.10 (n/a)</td><td>31.67 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>12.26 (-7.22%)</td><td>11.85 (-3.26%)</td><td>12.14 (-1.83%)</td><td>11.23 (+2.93%)</td><td>0.50 <b>(-41.41%)</b></td><td>373.50 (-2.86%)</td><td>354.60 (+3.11%)</td><td>345.50 (+1.86%)</td><td>342.20 (+7.81%)</td><td>15.29 <b>(-39.43%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>13.21 (n/a)</td><td>12.25 (n/a)</td><td>12.37 (n/a)</td><td>10.91 (n/a)</td><td>0.86 (n/a)</td><td>384.50 (n/a)</td><td>343.92 (n/a)</td><td>339.20 (n/a)</td><td>317.40 (n/a)</td><td>25.24 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>12.50 (-4.67%)</td><td>11.75 (+2.07%)</td><td>12.03 (+10.09%)</td><td>10.32 (-5.52%)</td><td>0.84 (-11.73%)</td><td>406.30 (+5.83%)</td><td>358.62 (-2.09%)</td><td>348.50 (-9.17%)</td><td>335.50 (+4.91%)</td><td>27.67 (-0.92%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>13.12 (n/a)</td><td>11.51 (n/a)</td><td>10.93 (n/a)</td><td>10.93 (n/a)</td><td>0.95 (n/a)</td><td>383.90 (n/a)</td><td>366.26 (n/a)</td><td>383.70 (n/a)</td><td>319.80 (n/a)</td><td>27.93 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>14.83 (-0.45%)</td><td>12.41 (-5.25%)</td><td>12.36 (-6.27%)</td><td>9.76 (-12.92%)</td><td>1.81 <b>(+30.30%)</b></td><td>429.90 (+14.85%)</td><td>344.20 (+6.49%)</td><td>339.40 (+6.70%)</td><td>282.90 (+0.46%)</td><td>53.52 <b>(+52.53%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>14.89 (n/a)</td><td>13.10 (n/a)</td><td>13.19 (n/a)</td><td>11.20 (n/a)</td><td>1.39 (n/a)</td><td>374.30 (n/a)</td><td>323.22 (n/a)</td><td>318.10 (n/a)</td><td>281.60 (n/a)</td><td>35.09 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>15.25 <b>(+20.04%)</b></td><td>13.27 (+9.98%)</td><td>13.25 (+12.09%)</td><td>11.36 (-3.30%)</td><td>1.39 <b>(+237.69%)</b></td><td>369.10 (+3.39%)</td><td>318.98 (-8.35%)</td><td>316.40 (-10.80%)</td><td>275.10 (-16.69%)</td><td>33.66 <b>(+190.63%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>12.70 (n/a)</td><td>12.06 (n/a)</td><td>11.83 (n/a)</td><td>11.75 (n/a)</td><td>0.41 (n/a)</td><td>357.00 (n/a)</td><td>348.04 (n/a)</td><td>354.70 (n/a)</td><td>330.20 (n/a)</td><td>11.58 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>14.28 (+2.97%)</td><td>13.07 (+6.80%)</td><td>12.98 (+7.91%)</td><td>11.80 (+10.30%)</td><td>0.95 <b>(-27.79%)</b></td><td>355.50 (-9.36%)</td><td>322.20 (-6.85%)</td><td>323.20 (-7.34%)</td><td>293.60 (-2.88%)</td><td>23.71 <b>(-36.18%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>13.87 (n/a)</td><td>12.24 (n/a)</td><td>12.03 (n/a)</td><td>10.70 (n/a)</td><td>1.32 (n/a)</td><td>392.20 (n/a)</td><td>345.88 (n/a)</td><td>348.80 (n/a)</td><td>302.30 (n/a)</td><td>37.15 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>15.08 (+5.45%)</td><td>13.59 (+6.16%)</td><td>13.85 (+7.02%)</td><td>11.86 (+4.25%)</td><td>1.50 <b>(+38.95%)</b></td><td>353.50 (-4.07%)</td><td>311.76 (-5.41%)</td><td>302.90 (-6.57%)</td><td>278.10 (-5.18%)</td><td>35.07 <b>(+25.99%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>14.30 (n/a)</td><td>12.80 (n/a)</td><td>12.94 (n/a)</td><td>11.38 (n/a)</td><td>1.08 (n/a)</td><td>368.50 (n/a)</td><td>329.58 (n/a)</td><td>324.20 (n/a)</td><td>293.30 (n/a)</td><td>27.83 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>15.19 (+19.48%)</td><td>13.70 (+13.17%)</td><td>13.87 (+15.06%)</td><td>11.61 (+2.75%)</td><td>1.32 <b>(+141.07%)</b></td><td>361.30 (-2.67%)</td><td>308.56 (-11.07%)</td><td>302.30 (-13.08%)</td><td>276.20 (-16.30%)</td><td>31.99 <b>(+99.87%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>12.71 (n/a)</td><td>12.11 (n/a)</td><td>12.06 (n/a)</td><td>11.30 (n/a)</td><td>0.55 (n/a)</td><td>371.20 (n/a)</td><td>346.96 (n/a)</td><td>347.80 (n/a)</td><td>330.00 (n/a)</td><td>16.00 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.32 (+5.46%)</td><td>3.09 (+7.84%)</td><td>3.24 (+11.20%)</td><td>2.74 (+15.41%)</td><td>0.26 (-12.87%)</td><td>191.60 (-13.38%)</td><td>170.54 (-7.63%)</td><td>162.00 (-10.10%)</td><td>158.10 (-5.16%)</td><td>14.90 <b>(-30.32%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.14 (n/a)</td><td>2.87 (n/a)</td><td>2.91 (n/a)</td><td>2.37 (n/a)</td><td>0.30 (n/a)</td><td>221.20 (n/a)</td><td>184.62 (n/a)</td><td>180.20 (n/a)</td><td>166.70 (n/a)</td><td>21.38 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>6.21 (+7.13%)</td><td>5.23 (+16.87%)</td><td>5.21 (+17.37%)</td><td>3.94 <b>(+21.50%)</b></td><td>0.90 (-1.88%)</td><td>265.90 (-17.70%)</td><td>205.66 (-15.21%)</td><td>201.40 (-14.81%)</td><td>168.80 (-6.64%)</td><td>38.49 <b>(-25.54%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>5.80 (n/a)</td><td>4.48 (n/a)</td><td>4.44 (n/a)</td><td>3.25 (n/a)</td><td>0.92 (n/a)</td><td>323.10 (n/a)</td><td>242.54 (n/a)</td><td>236.40 (n/a)</td><td>180.80 (n/a)</td><td>51.69 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>9.09 (+3.43%)</td><td>8.22 (+9.73%)</td><td>7.93 (+7.85%)</td><td>7.61 <b>(+22.15%)</b></td><td>0.70 <b>(-30.53%)</b></td><td>275.70 (-18.14%)</td><td>256.60 (-9.70%)</td><td>264.30 (-7.30%)</td><td>230.70 (-3.31%)</td><td>21.47 <b>(-44.60%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>8.79 (n/a)</td><td>7.49 (n/a)</td><td>7.36 (n/a)</td><td>6.23 (n/a)</td><td>1.01 (n/a)</td><td>336.80 (n/a)</td><td>284.16 (n/a)</td><td>285.10 (n/a)</td><td>238.60 (n/a)</td><td>38.76 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>3.48 (+2.33%)</td><td>2.93 (+16.72%)</td><td>2.84 (+12.83%)</td><td>2.55 <b>(+86.63%)</b></td><td>0.38 <b>(-48.02%)</b></td><td>205.20 <b>(-46.42%)</b></td><td>181.48 <b>(-20.84%)</b></td><td>184.60 (-11.38%)</td><td>150.80 (-2.27%)</td><td>22.72 <b>(-74.47%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>3.40 (n/a)</td><td>2.51 (n/a)</td><td>2.52 (n/a)</td><td>1.37 (n/a)</td><td>0.74 (n/a)</td><td>383.00 (n/a)</td><td>229.26 (n/a)</td><td>208.30 (n/a)</td><td>154.30 (n/a)</td><td>89.00 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.28 (+12.10%)</td><td>0.22 (+13.28%)</td><td>0.23 (+18.73%)</td><td>0.16 (+5.03%)</td><td>0.05 (+11.34%)</td><td>206.70 (-4.79%)</td><td>153.04 (-11.54%)</td><td>145.20 (-15.78%)</td><td>116.90 (-10.76%)</td><td>34.27 (-3.92%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>217.10 (n/a)</td><td>173.00 (n/a)</td><td>172.40 (n/a)</td><td>131.00 (n/a)</td><td>35.67 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.26 (+2.17%)</td><td>0.22 (+11.45%)</td><td>0.25 <b>(+40.67%)</b></td><td>0.15 (-5.23%)</td><td>0.05 (+11.30%)</td><td>213.20 (+5.49%)</td><td>151.94 (-9.47%)</td><td>130.70 <b>(-28.89%)</b></td><td>124.10 (-2.13%)</td><td>37.72 (+15.26%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>202.10 (n/a)</td><td>167.84 (n/a)</td><td>183.80 (n/a)</td><td>126.80 (n/a)</td><td>32.72 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.43 (-13.24%)</td><td>0.38 (-10.94%)</td><td>0.38 (-13.95%)</td><td>0.32 (-3.77%)</td><td>0.05 <b>(-24.99%)</b></td><td>203.10 (+3.94%)</td><td>175.78 (+11.55%)</td><td>173.20 (+16.16%)</td><td>153.20 (+15.27%)</td><td>22.81 (-11.06%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.49 (n/a)</td><td>0.42 (n/a)</td><td>0.44 (n/a)</td><td>0.34 (n/a)</td><td>0.06 (n/a)</td><td>195.40 (n/a)</td><td>157.58 (n/a)</td><td>149.10 (n/a)</td><td>132.90 (n/a)</td><td>25.65 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.51 (+3.32%)</td><td>0.41 (-4.68%)</td><td>0.38 (-4.50%)</td><td>0.37 (-5.55%)</td><td>0.06 <b>(+25.57%)</b></td><td>179.20 (+5.85%)</td><td>163.34 (+5.49%)</td><td>170.70 (+4.72%)</td><td>127.50 (-3.19%)</td><td>21.00 <b>(+25.56%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.50 (n/a)</td><td>0.43 (n/a)</td><td>0.40 (n/a)</td><td>0.39 (n/a)</td><td>0.05 (n/a)</td><td>169.30 (n/a)</td><td>154.84 (n/a)</td><td>163.00 (n/a)</td><td>131.70 (n/a)</td><td>16.72 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.52 (-1.66%)</td><td>0.43 (+4.42%)</td><td>0.42 (+16.47%)</td><td>0.31 (-8.27%)</td><td>0.09 (+6.98%)</td><td>211.80 (+9.06%)</td><td>159.78 (-3.57%)</td><td>155.80 (-14.11%)</td><td>126.50 (+1.69%)</td><td>35.18 (+15.72%)</td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.53 (n/a)</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.34 (n/a)</td><td>0.08 (n/a)</td><td>194.20 (n/a)</td><td>165.70 (n/a)</td><td>181.40 (n/a)</td><td>124.40 (n/a)</td><td>30.40 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.03 (+5.19%)</td><td>0.86 (+18.79%)</td><td>0.90 (+18.66%)</td><td>0.51 <b>(+51.14%)</b></td><td>0.21 <b>(-22.86%)</b></td><td>258.20 <b>(-33.83%)</b></td><td>162.86 <b>(-22.96%)</b></td><td>145.40 (-15.71%)</td><td>127.80 (-4.91%)</td><td>54.20 <b>(-49.01%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.98 (n/a)</td><td>0.72 (n/a)</td><td>0.76 (n/a)</td><td>0.34 (n/a)</td><td>0.27 (n/a)</td><td>390.20 (n/a)</td><td>211.40 (n/a)</td><td>172.50 (n/a)</td><td>134.40 (n/a)</td><td>106.30 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.01 (+12.47%)</td><td>0.87 (+7.12%)</td><td>0.97 (+11.17%)</td><td>0.65 (-2.10%)</td><td>0.17 <b>(+62.27%)</b></td><td>201.20 (+2.18%)</td><td>155.40 (-4.87%)</td><td>135.60 (-10.02%)</td><td>129.50 (-11.06%)</td><td>32.53 <b>(+46.37%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.90 (n/a)</td><td>0.81 (n/a)</td><td>0.87 (n/a)</td><td>0.67 (n/a)</td><td>0.10 (n/a)</td><td>196.90 (n/a)</td><td>163.36 (n/a)</td><td>150.70 (n/a)</td><td>145.60 (n/a)</td><td>22.22 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.04 <b>(+20.19%)</b></td><td>0.90 (+16.42%)</td><td>0.88 (+12.47%)</td><td>0.76 (+12.72%)</td><td>0.12 <b>(+71.66%)</b></td><td>173.40 (-11.30%)</td><td>147.30 (-13.46%)</td><td>148.90 (-11.10%)</td><td>125.90 (-16.79%)</td><td>19.65 <b>(+23.27%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.87 (n/a)</td><td>0.78 (n/a)</td><td>0.78 (n/a)</td><td>0.67 (n/a)</td><td>0.07 (n/a)</td><td>195.50 (n/a)</td><td>170.22 (n/a)</td><td>167.50 (n/a)</td><td>151.30 (n/a)</td><td>15.94 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>1.18 (+17.33%)</td><td>0.89 (+2.65%)</td><td>0.85 (-1.26%)</td><td>0.70 (-3.07%)</td><td>0.18 <b>(+73.72%)</b></td><td>188.10 (+3.12%)</td><td>152.14 (-0.90%)</td><td>154.70 (+1.24%)</td><td>110.90 (-14.82%)</td><td>27.46 <b>(+46.49%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>1.01 (n/a)</td><td>0.86 (n/a)</td><td>0.86 (n/a)</td><td>0.72 (n/a)</td><td>0.10 (n/a)</td><td>182.40 (n/a)</td><td>153.52 (n/a)</td><td>152.80 (n/a)</td><td>130.20 (n/a)</td><td>18.75 (n/a)</td>
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
<td><code>2e6839d</code> — 2026-09-18 22:04:59</td><td>0.14 (+5.09%)</td><td>0.10 (+0.16%)</td><td>0.11 <b>(+23.13%)</b></td><td>0.05 <b>(-41.39%)</b></td><td>0.03 <b>(+31.13%)</b></td><td>347.40 <b>(+70.63%)</b></td><td>185.48 (+9.22%)</td><td>155.00 (-18.76%)</td><td>119.40 (-4.86%)</td><td>92.82 <b>(+128.87%)</b></td>
</tr>
<tr>
<td><code>5320ada</code> — 2026-09-18 21:29:22</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>203.60 (n/a)</td><td>169.82 (n/a)</td><td>190.80 (n/a)</td><td>125.50 (n/a)</td><td>40.56 (n/a)</td>
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
