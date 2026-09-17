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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (+19.83%)</td><td>0.04 <b>(+24.21%)</b></td><td>0.04 (+15.49%)</td><td>0.03 <b>(+66.47%)</b></td><td>0.01 (-19.64%)</td><td>209.50 <b>(-39.94%)</b></td><td>161.90 <b>(-24.01%)</b></td><td>161.00 (-13.39%)</td><td>124.80 (-16.52%)</td><td>30.66 <b>(-61.29%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>348.80 (n/a)</td><td>213.06 (n/a)</td><td>185.90 (n/a)</td><td>149.50 (n/a)</td><td>79.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (-8.58%)</td><td>0.04 (+1.77%)</td><td>0.04 (+9.33%)</td><td>0.03 <b>(+28.87%)</b></td><td>0.00 <b>(-56.45%)</b></td><td>191.10 <b>(-22.41%)</b></td><td>162.10 (-7.12%)</td><td>158.80 (-8.58%)</td><td>136.40 (+9.38%)</td><td>19.92 <b>(-61.18%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>246.30 (n/a)</td><td>174.52 (n/a)</td><td>173.70 (n/a)</td><td>124.70 (n/a)</td><td>51.31 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 <b>(+21.49%)</b></td><td>0.04 (+18.71%)</td><td>0.04 <b>(+28.51%)</b></td><td>0.03 (+0.98%)</td><td>0.01 <b>(+67.67%)</b></td><td>213.20 (-0.98%)</td><td>157.14 (-12.81%)</td><td>143.50 <b>(-22.18%)</b></td><td>109.50 (-17.73%)</td><td>43.10 <b>(+44.97%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>215.30 (n/a)</td><td>180.22 (n/a)</td><td>184.40 (n/a)</td><td>133.10 (n/a)</td><td>29.73 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (+6.18%)</td><td>0.04 (+8.49%)</td><td>0.04 <b>(+20.70%)</b></td><td>0.02 <b>(-31.27%)</b></td><td>0.01 <b>(+24.78%)</b></td><td>358.80 <b>(+45.50%)</b></td><td>193.86 (-0.36%)</td><td>162.90 (-17.14%)</td><td>111.50 (-5.83%)</td><td>95.45 <b>(+88.08%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>246.60 (n/a)</td><td>194.56 (n/a)</td><td>196.60 (n/a)</td><td>118.40 (n/a)</td><td>50.75 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (-1.61%)</td><td>0.04 (-2.11%)</td><td>0.03 (-2.17%)</td><td>0.03 (-13.21%)</td><td>0.01 <b>(+25.43%)</b></td><td>228.50 (+15.23%)</td><td>178.72 (+5.85%)</td><td>184.90 (+2.21%)</td><td>116.20 (+1.66%)</td><td>51.71 <b>(+56.32%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>198.30 (n/a)</td><td>168.84 (n/a)</td><td>180.90 (n/a)</td><td>114.30 (n/a)</td><td>33.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (+4.39%)</td><td>0.04 (+1.24%)</td><td>0.03 (-6.48%)</td><td>0.03 (-4.40%)</td><td>0.01 <b>(+24.60%)</b></td><td>222.80 (+4.60%)</td><td>175.58 (+0.45%)</td><td>193.70 (+6.96%)</td><td>122.60 (-4.22%)</td><td>40.78 <b>(+25.16%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>174.80 (n/a)</td><td>181.10 (n/a)</td><td>128.00 (n/a)</td><td>32.58 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (+3.88%)</td><td>0.03 (+7.88%)</td><td>0.04 <b>(+25.82%)</b></td><td>0.03 (-0.06%)</td><td>0.01 (-5.94%)</td><td>229.60 (+0.09%)</td><td>183.58 (-7.58%)</td><td>172.40 <b>(-20.55%)</b></td><td>153.50 (-3.70%)</td><td>29.55 (-7.51%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>229.40 (n/a)</td><td>198.64 (n/a)</td><td>217.00 (n/a)</td><td>159.40 (n/a)</td><td>31.95 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (+4.57%)</td><td>0.03 (+17.53%)</td><td>0.03 (+14.18%)</td><td>0.03 <b>(+41.05%)</b></td><td>0.01 (-17.37%)</td><td>210.40 <b>(-29.11%)</b></td><td>182.14 (-17.10%)</td><td>192.60 (-12.41%)</td><td>138.90 (-4.40%)</td><td>31.54 <b>(-41.51%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>296.80 (n/a)</td><td>219.72 (n/a)</td><td>219.90 (n/a)</td><td>145.30 (n/a)</td><td>53.92 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.09 (+10.94%)</td><td>0.08 (+9.72%)</td><td>0.08 (+5.97%)</td><td>0.07 (+6.68%)</td><td>0.01 (+15.63%)</td><td>187.70 (-6.24%)</td><td>152.20 (-8.67%)</td><td>144.60 (-5.61%)</td><td>130.40 (-9.82%)</td><td>23.96 (-2.91%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>200.20 (n/a)</td><td>166.64 (n/a)</td><td>153.20 (n/a)</td><td>144.60 (n/a)</td><td>24.67 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (-7.01%)</td><td>0.08 (+2.44%)</td><td>0.08 (+18.26%)</td><td>0.07 (+6.01%)</td><td>0.01 <b>(-39.67%)</b></td><td>182.10 (-5.70%)</td><td>152.62 (-4.97%)</td><td>152.70 (-15.45%)</td><td>125.30 (+7.55%)</td><td>21.30 <b>(-39.19%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>193.10 (n/a)</td><td>160.60 (n/a)</td><td>180.60 (n/a)</td><td>116.50 (n/a)</td><td>35.02 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (+4.89%)</td><td>0.09 <b>(+27.79%)</b></td><td>0.09 <b>(+46.87%)</b></td><td>0.07 <b>(+25.51%)</b></td><td>0.01 (-13.73%)</td><td>184.40 <b>(-20.31%)</b></td><td>142.96 <b>(-22.97%)</b></td><td>131.20 <b>(-31.91%)</b></td><td>119.30 (-4.64%)</td><td>26.56 <b>(-30.64%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>231.40 (n/a)</td><td>185.60 (n/a)</td><td>192.70 (n/a)</td><td>125.10 (n/a)</td><td>38.30 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (+3.23%)</td><td>0.08 (+18.41%)</td><td>0.08 <b>(+28.42%)</b></td><td>0.07 <b>(+26.45%)</b></td><td>0.01 <b>(-28.98%)</b></td><td>185.10 <b>(-20.90%)</b></td><td>151.82 (-17.91%)</td><td>152.10 <b>(-22.16%)</b></td><td>120.00 (-3.15%)</td><td>23.15 <b>(-44.54%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>234.00 (n/a)</td><td>184.94 (n/a)</td><td>195.40 (n/a)</td><td>123.90 (n/a)</td><td>41.73 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.09 (+0.43%)</td><td>0.08 (+10.23%)</td><td>0.08 (+14.80%)</td><td>0.06 (-0.88%)</td><td>0.01 (-4.02%)</td><td>216.00 (+0.89%)</td><td>161.64 (-9.31%)</td><td>154.30 (-12.87%)</td><td>129.40 (-0.46%)</td><td>32.30 (+3.04%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>214.10 (n/a)</td><td>178.24 (n/a)</td><td>177.10 (n/a)</td><td>130.00 (n/a)</td><td>31.35 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 <b>(+27.55%)</b></td><td>0.08 <b>(+23.67%)</b></td><td>0.08 (+19.42%)</td><td>0.08 <b>(+43.92%)</b></td><td>0.01 (-6.66%)</td><td>162.30 <b>(-30.49%)</b></td><td>152.02 (-19.86%)</td><td>157.00 (-16.27%)</td><td>126.90 <b>(-21.62%)</b></td><td>14.25 <b>(-49.89%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>233.50 (n/a)</td><td>189.70 (n/a)</td><td>187.50 (n/a)</td><td>161.90 (n/a)</td><td>28.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 <b>(+30.94%)</b></td><td>0.08 (+19.84%)</td><td>0.08 (+13.44%)</td><td>0.06 (+6.87%)</td><td>0.02 <b>(+115.85%)</b></td><td>213.60 (-6.44%)</td><td>159.02 (-13.99%)</td><td>158.40 (-11.85%)</td><td>120.40 <b>(-23.65%)</b></td><td>38.19 <b>(+46.44%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.30 (n/a)</td><td>184.88 (n/a)</td><td>179.70 (n/a)</td><td>157.70 (n/a)</td><td>26.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.09 (-7.78%)</td><td>0.08 (+13.01%)</td><td>0.08 <b>(+29.08%)</b></td><td>0.07 <b>(+31.92%)</b></td><td>0.01 <b>(-65.48%)</b></td><td>171.10 <b>(-24.19%)</b></td><td>156.92 (-14.82%)</td><td>156.60 <b>(-22.51%)</b></td><td>140.10 (+8.44%)</td><td>11.25 <b>(-71.70%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>225.70 (n/a)</td><td>184.22 (n/a)</td><td>202.10 (n/a)</td><td>129.20 (n/a)</td><td>39.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (+17.72%)</td><td>0.16 (+9.55%)</td><td>0.16 (+18.85%)</td><td>0.12 (-4.86%)</td><td>0.03 <b>(+136.35%)</b></td><td>201.60 (+5.11%)</td><td>162.20 (-6.51%)</td><td>150.30 (-15.85%)</td><td>131.70 (-15.03%)</td><td>31.84 <b>(+113.89%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>191.80 (n/a)</td><td>173.50 (n/a)</td><td>178.60 (n/a)</td><td>155.00 (n/a)</td><td>14.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 (+8.79%)</td><td>0.17 (+11.97%)</td><td>0.19 <b>(+25.66%)</b></td><td>0.13 (+1.56%)</td><td>0.03 (+6.72%)</td><td>188.60 (-1.51%)</td><td>144.32 (-10.54%)</td><td>132.20 <b>(-20.41%)</b></td><td>122.20 (-8.12%)</td><td>26.54 (+0.83%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>191.50 (n/a)</td><td>161.32 (n/a)</td><td>166.10 (n/a)</td><td>133.00 (n/a)</td><td>26.32 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.21 (+13.09%)</td><td>0.14 (-4.64%)</td><td>0.13 <b>(-20.08%)</b></td><td>0.10 <b>(+31.18%)</b></td><td>0.04 (-4.28%)</td><td>234.10 <b>(-23.77%)</b></td><td>186.82 (+0.96%)</td><td>191.20 <b>(+25.13%)</b></td><td>117.10 (-11.62%)</td><td>44.35 <b>(-38.66%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>307.10 (n/a)</td><td>185.04 (n/a)</td><td>152.80 (n/a)</td><td>132.50 (n/a)</td><td>72.29 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (+7.03%)</td><td>0.14 (-3.47%)</td><td>0.14 (-1.33%)</td><td>0.07 <b>(-50.24%)</b></td><td>0.05 <b>(+189.02%)</b></td><td>368.50 <b>(+101.04%)</b></td><td>195.94 (+18.15%)</td><td>170.50 (+1.37%)</td><td>130.50 (-6.59%)</td><td>98.65 <b>(+462.54%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>183.30 (n/a)</td><td>165.84 (n/a)</td><td>168.20 (n/a)</td><td>139.70 (n/a)</td><td>17.54 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.17 <b>(-39.45%)</b></td><td>0.13 <b>(-33.12%)</b></td><td>0.12 <b>(-33.70%)</b></td><td>0.10 <b>(-25.77%)</b></td><td>0.03 <b>(-53.09%)</b></td><td>243.50 <b>(+34.75%)</b></td><td>196.82 <b>(+44.02%)</b></td><td>200.80 <b>(+50.86%)</b></td><td>141.00 <b>(+65.11%)</b></td><td>39.83 (+1.62%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>180.70 (n/a)</td><td>136.66 (n/a)</td><td>133.10 (n/a)</td><td>85.40 (n/a)</td><td>39.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (+16.18%)</td><td>0.13 (-4.91%)</td><td>0.13 (-14.51%)</td><td>0.10 (-15.04%)</td><td>0.03 <b>(+69.86%)</b></td><td>255.40 (+17.70%)</td><td>194.72 (+8.48%)</td><td>195.00 (+16.98%)</td><td>132.00 (-13.95%)</td><td>45.96 <b>(+68.55%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>217.00 (n/a)</td><td>179.50 (n/a)</td><td>166.70 (n/a)</td><td>153.40 (n/a)</td><td>27.27 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.17 (-5.65%)</td><td>0.13 (-8.94%)</td><td>0.12 <b>(-23.16%)</b></td><td>0.11 <b>(+46.60%)</b></td><td>0.03 <b>(-40.90%)</b></td><td>229.90 <b>(-31.80%)</b></td><td>199.40 (+1.18%)</td><td>205.90 <b>(+30.15%)</b></td><td>142.70 (+6.02%)</td><td>33.19 <b>(-60.04%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>337.10 (n/a)</td><td>197.08 (n/a)</td><td>158.20 (n/a)</td><td>134.60 (n/a)</td><td>83.06 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (+19.49%)</td><td>0.16 (+14.41%)</td><td>0.15 (+9.16%)</td><td>0.14 (+17.21%)</td><td>0.02 <b>(+23.17%)</b></td><td>174.70 (-14.70%)</td><td>158.04 (-12.53%)</td><td>160.30 (-8.40%)</td><td>132.80 (-16.27%)</td><td>17.12 (-12.74%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>204.80 (n/a)</td><td>180.68 (n/a)</td><td>175.00 (n/a)</td><td>158.60 (n/a)</td><td>19.62 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.40 <b>(+24.05%)</b></td><td>0.34 <b>(+21.66%)</b></td><td>0.35 <b>(+23.08%)</b></td><td>0.26 (+18.48%)</td><td>0.06 <b>(+55.26%)</b></td><td>191.40 (-15.57%)</td><td>149.08 (-17.01%)</td><td>140.50 (-18.74%)</td><td>123.60 (-19.37%)</td><td>28.03 (+1.47%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>226.70 (n/a)</td><td>179.64 (n/a)</td><td>172.90 (n/a)</td><td>153.30 (n/a)</td><td>27.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.38 (-8.96%)</td><td>0.30 (-0.37%)</td><td>0.28 (-0.29%)</td><td>0.20 (+14.24%)</td><td>0.07 <b>(-29.24%)</b></td><td>242.80 (-12.47%)</td><td>174.96 (-4.56%)</td><td>173.30 (+0.35%)</td><td>130.10 (+9.88%)</td><td>45.30 <b>(-31.52%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.42 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>277.40 (n/a)</td><td>183.32 (n/a)</td><td>172.70 (n/a)</td><td>118.40 (n/a)</td><td>66.14 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.44 <b>(+38.40%)</b></td><td>0.33 <b>(+20.24%)</b></td><td>0.30 (+12.53%)</td><td>0.26 (+1.13%)</td><td>0.08 <b>(+190.95%)</b></td><td>190.30 (-1.14%)</td><td>153.52 (-14.18%)</td><td>161.40 (-11.17%)</td><td>110.90 <b>(-27.75%)</b></td><td>32.01 <b>(+108.41%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.32 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.03 (n/a)</td><td>192.50 (n/a)</td><td>178.88 (n/a)</td><td>181.70 (n/a)</td><td>153.50 (n/a)</td><td>15.36 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.40 (-0.10%)</td><td>0.31 (-9.43%)</td><td>0.32 (+0.73%)</td><td>0.21 <b>(-21.54%)</b></td><td>0.07 (+15.56%)</td><td>239.70 <b>(+27.43%)</b></td><td>168.82 (+12.82%)</td><td>154.20 (-0.71%)</td><td>122.40 (+0.16%)</td><td>44.13 <b>(+57.87%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.32 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>188.10 (n/a)</td><td>149.64 (n/a)</td><td>155.30 (n/a)</td><td>122.20 (n/a)</td><td>27.95 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.38 <b>(+30.34%)</b></td><td>0.30 (+17.96%)</td><td>0.31 (+17.51%)</td><td>0.17 (-2.30%)</td><td>0.08 <b>(+82.03%)</b></td><td>289.90 (+2.37%)</td><td>180.40 (-11.07%)</td><td>159.50 (-14.89%)</td><td>129.40 <b>(-23.25%)</b></td><td>64.47 <b>(+40.90%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>283.20 (n/a)</td><td>202.86 (n/a)</td><td>187.40 (n/a)</td><td>168.60 (n/a)</td><td>45.75 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.37 (+16.22%)</td><td>0.29 (+9.47%)</td><td>0.28 (+9.55%)</td><td>0.25 (-0.54%)</td><td>0.05 <b>(+76.00%)</b></td><td>196.40 (+0.51%)</td><td>171.86 (-7.52%)</td><td>175.90 (-8.72%)</td><td>134.40 (-13.96%)</td><td>25.79 <b>(+54.60%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.31 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.25 (n/a)</td><td>0.03 (n/a)</td><td>195.40 (n/a)</td><td>185.84 (n/a)</td><td>192.70 (n/a)</td><td>156.20 (n/a)</td><td>16.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.32 <b>(-24.12%)</b></td><td>0.26 (+2.02%)</td><td>0.25 (+9.12%)</td><td>0.19 (+16.97%)</td><td>0.05 <b>(-50.32%)</b></td><td>258.30 (-14.50%)</td><td>195.14 (-8.05%)</td><td>194.00 (-8.40%)</td><td>154.20 <b>(+31.79%)</b></td><td>39.66 <b>(-39.62%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.42 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>302.10 (n/a)</td><td>212.22 (n/a)</td><td>211.80 (n/a)</td><td>117.00 (n/a)</td><td>65.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.35 <b>(+27.58%)</b></td><td>0.28 (+12.88%)</td><td>0.25 (-5.96%)</td><td>0.24 (+10.08%)</td><td>0.05 <b>(+100.03%)</b></td><td>202.60 (-9.15%)</td><td>178.38 (-9.95%)</td><td>198.00 (+6.34%)</td><td>140.10 <b>(-21.60%)</b></td><td>30.34 <b>(+43.23%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>223.00 (n/a)</td><td>198.08 (n/a)</td><td>186.20 (n/a)</td><td>178.70 (n/a)</td><td>21.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (-14.48%)</td><td>0.02 (+4.98%)</td><td>0.02 <b>(+20.60%)</b></td><td>0.01 <b>(+20.17%)</b></td><td>0.00 <b>(-46.12%)</b></td><td>185.90 (-16.79%)</td><td>160.88 (-7.71%)</td><td>150.10 (-17.12%)</td><td>141.90 (+16.98%)</td><td>21.22 <b>(-46.45%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>223.40 (n/a)</td><td>174.32 (n/a)</td><td>181.10 (n/a)</td><td>121.30 (n/a)</td><td>39.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (+7.18%)</td><td>0.02 (+3.65%)</td><td>0.02 (+10.94%)</td><td>0.01 (-12.56%)</td><td>0.00 <b>(+75.55%)</b></td><td>226.30 (+14.35%)</td><td>170.82 (-1.23%)</td><td>152.30 (-9.88%)</td><td>140.20 (-6.66%)</td><td>37.07 <b>(+84.26%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>197.90 (n/a)</td><td>172.94 (n/a)</td><td>169.00 (n/a)</td><td>150.20 (n/a)</td><td>20.12 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (+15.72%)</td><td>0.02 (-0.57%)</td><td>0.01 (-6.61%)</td><td>0.01 <b>(-21.78%)</b></td><td>0.01 <b>(+115.78%)</b></td><td>253.70 <b>(+27.87%)</b></td><td>185.08 (+8.04%)</td><td>192.90 (+7.11%)</td><td>118.30 (-13.59%)</td><td>59.43 <b>(+135.34%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>198.40 (n/a)</td><td>171.30 (n/a)</td><td>180.10 (n/a)</td><td>136.90 (n/a)</td><td>25.25 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (+12.32%)</td><td>0.01 (-0.57%)</td><td>0.01 (-4.27%)</td><td>0.01 (-0.29%)</td><td>0.00 <b>(+39.64%)</b></td><td>224.00 (+0.27%)</td><td>192.12 (+2.84%)</td><td>204.30 (+4.45%)</td><td>118.50 (-10.97%)</td><td>41.98 <b>(+22.60%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>223.40 (n/a)</td><td>186.82 (n/a)</td><td>195.60 (n/a)</td><td>133.10 (n/a)</td><td>34.24 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (-5.32%)</td><td>0.02 (+3.00%)</td><td>0.01 (+4.09%)</td><td>0.01 (+9.96%)</td><td>0.00 <b>(-23.86%)</b></td><td>203.20 (-9.04%)</td><td>179.44 (-5.10%)</td><td>188.00 (-3.93%)</td><td>127.00 (+5.57%)</td><td>30.11 <b>(-28.22%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>223.40 (n/a)</td><td>189.08 (n/a)</td><td>195.70 (n/a)</td><td>120.30 (n/a)</td><td>41.95 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (-7.35%)</td><td>0.01 (-13.24%)</td><td>0.01 (-15.54%)</td><td>0.01 <b>(-26.20%)</b></td><td>0.00 <b>(+47.68%)</b></td><td>276.80 <b>(+35.49%)</b></td><td>210.46 (+17.76%)</td><td>205.30 (+18.40%)</td><td>166.30 (+7.92%)</td><td>43.31 <b>(+114.83%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>204.30 (n/a)</td><td>178.72 (n/a)</td><td>173.40 (n/a)</td><td>154.10 (n/a)</td><td>20.16 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 <b>(+20.97%)</b></td><td>0.01 (+10.20%)</td><td>0.01 (+6.15%)</td><td>0.01 (+12.72%)</td><td>0.00 <b>(+73.25%)</b></td><td>199.30 (-11.26%)</td><td>185.06 (-8.84%)</td><td>190.40 (-5.79%)</td><td>155.20 (-17.31%)</td><td>17.97 <b>(+25.95%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>224.60 (n/a)</td><td>203.00 (n/a)</td><td>202.10 (n/a)</td><td>187.70 (n/a)</td><td>14.27 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.01 (+2.86%)</td><td>0.01 (-6.50%)</td><td>0.01 (+0.46%)</td><td>0.01 <b>(-25.52%)</b></td><td>0.00 <b>(+183.55%)</b></td><td>301.30 <b>(+34.27%)</b></td><td>235.18 (+9.45%)</td><td>218.40 (-0.46%)</td><td>189.70 (-2.82%)</td><td>43.47 <b>(+280.69%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>224.40 (n/a)</td><td>214.88 (n/a)</td><td>219.40 (n/a)</td><td>195.20 (n/a)</td><td>11.42 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 <b>(+23.85%)</b></td><td>0.04 (+7.90%)</td><td>0.04 (+10.68%)</td><td>0.03 (-16.60%)</td><td>0.01 <b>(+201.06%)</b></td><td>205.80 (+19.93%)</td><td>147.06 (-3.30%)</td><td>138.40 (-9.66%)</td><td>110.00 (-19.30%)</td><td>37.86 <b>(+192.56%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>171.60 (n/a)</td><td>152.08 (n/a)</td><td>153.20 (n/a)</td><td>136.30 (n/a)</td><td>12.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (-4.00%)</td><td>0.03 (+9.92%)</td><td>0.03 (-11.55%)</td><td>0.03 <b>(+64.93%)</b></td><td>0.01 <b>(-44.16%)</b></td><td>189.70 <b>(-39.35%)</b></td><td>158.70 (-17.34%)</td><td>168.30 (+13.10%)</td><td>128.50 (+4.13%)</td><td>27.17 <b>(-65.94%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>312.80 (n/a)</td><td>191.98 (n/a)</td><td>148.80 (n/a)</td><td>123.40 (n/a)</td><td>79.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (+3.91%)</td><td>0.03 (+2.65%)</td><td>0.03 (-14.46%)</td><td>0.02 (+14.35%)</td><td>0.01 (+2.54%)</td><td>227.40 (-12.54%)</td><td>181.70 (-3.16%)</td><td>197.70 (+16.91%)</td><td>133.50 (-3.75%)</td><td>38.36 (-16.92%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>260.00 (n/a)</td><td>187.62 (n/a)</td><td>169.10 (n/a)</td><td>138.70 (n/a)</td><td>46.17 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 <b>(-24.85%)</b></td><td>0.03 <b>(-21.17%)</b></td><td>0.03 (-17.15%)</td><td>0.02 <b>(-34.62%)</b></td><td>0.01 (-3.55%)</td><td>298.50 <b>(+53.00%)</b></td><td>216.80 <b>(+29.20%)</b></td><td>206.50 <b>(+20.69%)</b></td><td>171.10 <b>(+33.05%)</b></td><td>50.07 <b>(+106.82%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>195.10 (n/a)</td><td>167.80 (n/a)</td><td>171.10 (n/a)</td><td>128.60 (n/a)</td><td>24.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 <b>(-32.06%)</b></td><td>0.03 (-6.79%)</td><td>0.03 (+8.95%)</td><td>0.02 (-19.06%)</td><td>0.01 <b>(-47.25%)</b></td><td>248.70 <b>(+23.55%)</b></td><td>175.56 (+3.61%)</td><td>170.80 (-8.22%)</td><td>140.20 <b>(+47.27%)</b></td><td>43.45 (+1.55%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>201.30 (n/a)</td><td>169.44 (n/a)</td><td>186.10 (n/a)</td><td>95.20 (n/a)</td><td>42.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (-11.29%)</td><td>0.03 (+1.95%)</td><td>0.03 (+10.67%)</td><td>0.03 (+0.15%)</td><td>0.00 <b>(-38.51%)</b></td><td>208.10 (-0.14%)</td><td>174.72 (-3.68%)</td><td>176.80 (-9.61%)</td><td>144.10 (+12.75%)</td><td>23.01 <b>(-30.07%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>208.40 (n/a)</td><td>181.40 (n/a)</td><td>195.60 (n/a)</td><td>127.80 (n/a)</td><td>32.90 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 <b>(+30.94%)</b></td><td>0.03 <b>(+22.26%)</b></td><td>0.03 <b>(+24.70%)</b></td><td>0.02 (+12.87%)</td><td>0.01 <b>(+60.22%)</b></td><td>214.10 (-11.42%)</td><td>171.42 (-16.97%)</td><td>175.00 (-19.80%)</td><td>131.40 <b>(-23.60%)</b></td><td>35.28 (+10.15%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>241.70 (n/a)</td><td>206.46 (n/a)</td><td>218.20 (n/a)</td><td>172.00 (n/a)</td><td>32.03 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 <b>(-31.31%)</b></td><td>0.02 (-13.95%)</td><td>0.02 (-1.65%)</td><td>0.02 <b>(-22.56%)</b></td><td>0.00 <b>(-40.16%)</b></td><td>291.80 <b>(+29.12%)</b></td><td>226.62 (+14.52%)</td><td>211.40 (+1.68%)</td><td>185.30 <b>(+45.56%)</b></td><td>46.23 (+13.20%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>226.00 (n/a)</td><td>197.88 (n/a)</td><td>207.90 (n/a)</td><td>127.30 (n/a)</td><td>40.84 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (-2.94%)</td><td>0.06 (-0.28%)</td><td>0.06 (+5.07%)</td><td>0.04 (-12.23%)</td><td>0.01 (+15.12%)</td><td>238.90 (+13.92%)</td><td>181.90 (+1.16%)</td><td>171.40 (-4.83%)</td><td>152.60 (+2.97%)</td><td>33.66 <b>(+39.49%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>209.70 (n/a)</td><td>179.82 (n/a)</td><td>180.10 (n/a)</td><td>148.20 (n/a)</td><td>24.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (-5.42%)</td><td>0.05 (-17.37%)</td><td>0.06 (-11.59%)</td><td>0.04 <b>(-35.09%)</b></td><td>0.01 <b>(+177.46%)</b></td><td>276.40 <b>(+54.07%)</b></td><td>207.70 <b>(+26.09%)</b></td><td>181.00 (+13.12%)</td><td>160.70 (+5.72%)</td><td>50.72 <b>(+353.01%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.00 (n/a)</td><td>179.40 (n/a)</td><td>164.72 (n/a)</td><td>160.00 (n/a)</td><td>152.00 (n/a)</td><td>11.20 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.08 (+17.22%)</td><td>0.06 (+3.72%)</td><td>0.05 (-9.68%)</td><td>0.04 <b>(-22.62%)</b></td><td>0.02 <b>(+118.78%)</b></td><td>291.40 <b>(+29.22%)</b></td><td>194.30 (+4.59%)</td><td>195.60 (+10.76%)</td><td>126.80 (-14.67%)</td><td>69.63 <b>(+123.04%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>225.50 (n/a)</td><td>185.78 (n/a)</td><td>176.60 (n/a)</td><td>148.60 (n/a)</td><td>31.22 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (-6.71%)</td><td>0.06 (-3.10%)</td><td>0.06 (+10.34%)</td><td>0.05 (-5.98%)</td><td>0.01 (-3.15%)</td><td>224.70 (+6.34%)</td><td>191.66 (+3.38%)</td><td>176.30 (-9.36%)</td><td>160.20 (+7.16%)</td><td>29.75 (+13.70%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>185.40 (n/a)</td><td>194.50 (n/a)</td><td>149.50 (n/a)</td><td>26.17 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (-18.88%)</td><td>0.05 (-7.36%)</td><td>0.05 (-13.66%)</td><td>0.05 <b>(+31.44%)</b></td><td>0.00 <b>(-72.15%)</b></td><td>226.10 <b>(-23.95%)</b></td><td>204.26 (+0.76%)</td><td>194.00 (+15.82%)</td><td>187.00 <b>(+23.27%)</b></td><td>17.72 <b>(-72.91%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>297.30 (n/a)</td><td>202.72 (n/a)</td><td>167.50 (n/a)</td><td>151.70 (n/a)</td><td>65.39 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (-11.21%)</td><td>0.06 (+3.31%)</td><td>0.06 (+7.94%)</td><td>0.04 (-3.11%)</td><td>0.01 (-18.89%)</td><td>235.80 (+3.19%)</td><td>186.54 (-3.58%)</td><td>177.60 (-7.36%)</td><td>169.40 (+12.63%)</td><td>27.90 (-2.40%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>228.50 (n/a)</td><td>193.46 (n/a)</td><td>191.70 (n/a)</td><td>150.40 (n/a)</td><td>28.59 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (-11.96%)</td><td>0.06 (+7.60%)</td><td>0.06 (+16.00%)</td><td>0.04 (+6.06%)</td><td>0.01 <b>(-20.71%)</b></td><td>235.60 (-5.68%)</td><td>182.18 (-8.61%)</td><td>183.50 (-13.77%)</td><td>143.00 (+13.58%)</td><td>39.76 (-14.39%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>249.80 (n/a)</td><td>199.34 (n/a)</td><td>212.80 (n/a)</td><td>125.90 (n/a)</td><td>46.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (-16.50%)</td><td>0.04 (-9.38%)</td><td>0.05 (-1.20%)</td><td>0.03 (-15.75%)</td><td>0.01 (-16.62%)</td><td>304.50 (+18.71%)</td><td>243.22 (+10.40%)</td><td>225.90 (+1.21%)</td><td>213.70 (+19.79%)</td><td>36.19 <b>(+21.96%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>256.50 (n/a)</td><td>220.30 (n/a)</td><td>223.20 (n/a)</td><td>178.40 (n/a)</td><td>29.67 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (-4.46%)</td><td>0.11 (+10.09%)</td><td>0.11 (+2.11%)</td><td>0.10 <b>(+67.78%)</b></td><td>0.01 <b>(-52.09%)</b></td><td>216.00 <b>(-40.38%)</b></td><td>190.86 (-15.07%)</td><td>199.20 (-2.06%)</td><td>165.20 (+4.69%)</td><td>22.13 <b>(-72.29%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>362.30 (n/a)</td><td>224.72 (n/a)</td><td>203.40 (n/a)</td><td>157.80 (n/a)</td><td>79.86 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 <b>(-29.95%)</b></td><td>0.11 (-8.52%)</td><td>0.12 (+2.19%)</td><td>0.08 (-16.65%)</td><td>0.02 <b>(-43.45%)</b></td><td>275.50 (+19.99%)</td><td>192.56 (+6.36%)</td><td>179.00 (-2.13%)</td><td>154.30 <b>(+42.74%)</b></td><td>48.40 (+3.80%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>229.60 (n/a)</td><td>181.04 (n/a)</td><td>182.90 (n/a)</td><td>108.10 (n/a)</td><td>46.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (-11.75%)</td><td>0.12 (-2.98%)</td><td>0.11 (-7.24%)</td><td>0.10 (+13.31%)</td><td>0.02 <b>(-34.70%)</b></td><td>203.00 (-11.74%)</td><td>176.02 (+0.41%)</td><td>184.40 (+7.84%)</td><td>136.10 (+13.32%)</td><td>27.02 <b>(-34.24%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>230.00 (n/a)</td><td>175.30 (n/a)</td><td>171.00 (n/a)</td><td>120.10 (n/a)</td><td>41.09 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (+4.61%)</td><td>0.12 (+13.08%)</td><td>0.12 (+6.72%)</td><td>0.11 <b>(+28.85%)</b></td><td>0.01 <b>(-34.80%)</b></td><td>198.80 <b>(-22.40%)</b></td><td>175.28 (-13.59%)</td><td>177.10 (-6.30%)</td><td>147.30 (-4.41%)</td><td>19.64 <b>(-52.82%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>256.20 (n/a)</td><td>202.84 (n/a)</td><td>189.00 (n/a)</td><td>154.10 (n/a)</td><td>41.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (-7.43%)</td><td>0.12 (-8.98%)</td><td>0.11 (-15.32%)</td><td>0.09 (-12.69%)</td><td>0.03 (+18.10%)</td><td>232.80 (+14.57%)</td><td>186.94 (+12.13%)</td><td>188.70 (+18.09%)</td><td>138.40 (+8.04%)</td><td>45.60 <b>(+43.66%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>203.20 (n/a)</td><td>166.72 (n/a)</td><td>159.80 (n/a)</td><td>128.10 (n/a)</td><td>31.74 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (-9.24%)</td><td>0.11 (+14.46%)</td><td>0.11 <b>(+24.19%)</b></td><td>0.10 <b>(+20.74%)</b></td><td>0.01 <b>(-55.32%)</b></td><td>207.80 (-17.18%)</td><td>187.70 (-14.98%)</td><td>194.20 (-19.49%)</td><td>169.00 (+10.17%)</td><td>16.43 <b>(-59.21%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>250.90 (n/a)</td><td>220.78 (n/a)</td><td>241.20 (n/a)</td><td>153.40 (n/a)</td><td>40.29 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 <b>(-32.66%)</b></td><td>0.11 (-7.16%)</td><td>0.11 (-3.43%)</td><td>0.10 (+8.19%)</td><td>0.01 <b>(-73.75%)</b></td><td>208.70 (-7.57%)</td><td>188.80 (+1.80%)</td><td>192.60 (+3.55%)</td><td>167.50 <b>(+48.49%)</b></td><td>16.59 <b>(-63.44%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.19 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>225.80 (n/a)</td><td>185.46 (n/a)</td><td>186.00 (n/a)</td><td>112.80 (n/a)</td><td>45.37 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (-0.90%)</td><td>0.10 (+1.25%)</td><td>0.10 (+2.60%)</td><td>0.08 (+1.77%)</td><td>0.01 (-6.12%)</td><td>255.70 (-1.73%)</td><td>215.84 (-1.40%)</td><td>211.00 (-2.54%)</td><td>180.40 (+0.89%)</td><td>27.24 (-6.05%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>260.20 (n/a)</td><td>218.90 (n/a)</td><td>216.50 (n/a)</td><td>178.80 (n/a)</td><td>28.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>182.80 (n/a)</td><td>155.38 (n/a)</td><td>152.50 (n/a)</td><td>120.30 (n/a)</td><td>24.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>270.90 (n/a)</td><td>193.76 (n/a)</td><td>187.90 (n/a)</td><td>135.30 (n/a)</td><td>52.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>180.50 (n/a)</td><td>157.42 (n/a)</td><td>156.80 (n/a)</td><td>137.90 (n/a)</td><td>15.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>334.80 (n/a)</td><td>200.34 (n/a)</td><td>162.20 (n/a)</td><td>150.00 (n/a)</td><td>77.04 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>207.20 (n/a)</td><td>152.22 (n/a)</td><td>146.40 (n/a)</td><td>110.20 (n/a)</td><td>35.12 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>183.70 (n/a)</td><td>152.90 (n/a)</td><td>157.80 (n/a)</td><td>122.50 (n/a)</td><td>25.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>218.80 (n/a)</td><td>159.10 (n/a)</td><td>157.60 (n/a)</td><td>96.20 (n/a)</td><td>48.86 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>287.80 (n/a)</td><td>177.44 (n/a)</td><td>172.60 (n/a)</td><td>99.30 (n/a)</td><td>69.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>375.10 (n/a)</td><td>203.02 (n/a)</td><td>174.30 (n/a)</td><td>128.80 (n/a)</td><td>100.22 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>293.50 (n/a)</td><td>176.70 (n/a)</td><td>154.20 (n/a)</td><td>131.30 (n/a)</td><td>66.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>220.40 (n/a)</td><td>161.90 (n/a)</td><td>148.60 (n/a)</td><td>123.50 (n/a)</td><td>39.90 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>215.10 (n/a)</td><td>189.76 (n/a)</td><td>188.20 (n/a)</td><td>158.90 (n/a)</td><td>20.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.38 (+1.19%)</td><td>0.33 (+13.61%)</td><td>0.35 <b>(+24.04%)</b></td><td>0.25 (+4.27%)</td><td>0.05 (-1.21%)</td><td>194.80 (-4.09%)</td><td>150.00 (-11.98%)</td><td>139.90 (-19.37%)</td><td>128.90 (-1.15%)</td><td>25.95 (-0.30%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.38 (n/a)</td><td>0.29 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>203.10 (n/a)</td><td>170.42 (n/a)</td><td>173.50 (n/a)</td><td>130.40 (n/a)</td><td>26.03 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.37 (n/a)</td><td>0.33 (n/a)</td><td>0.34 (n/a)</td><td>0.24 (n/a)</td><td>0.05 (n/a)</td><td>203.50 (n/a)</td><td>153.56 (n/a)</td><td>143.90 (n/a)</td><td>132.60 (n/a)</td><td>28.51 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>199.50 (n/a)</td><td>164.62 (n/a)</td><td>174.90 (n/a)</td><td>126.40 (n/a)</td><td>28.27 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.34 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>219.30 (n/a)</td><td>177.32 (n/a)</td><td>174.20 (n/a)</td><td>143.80 (n/a)</td><td>28.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>375.00 (n/a)</td><td>198.36 (n/a)</td><td>161.40 (n/a)</td><td>115.40 (n/a)</td><td>102.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>304.10 (n/a)</td><td>194.56 (n/a)</td><td>174.50 (n/a)</td><td>140.60 (n/a)</td><td>66.95 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.00 (n/a)</td><td>176.16 (n/a)</td><td>159.20 (n/a)</td><td>144.50 (n/a)</td><td>40.53 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>221.10 (n/a)</td><td>194.36 (n/a)</td><td>190.80 (n/a)</td><td>164.60 (n/a)</td><td>24.90 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>219.50 (n/a)</td><td>191.78 (n/a)</td><td>190.80 (n/a)</td><td>173.40 (n/a)</td><td>17.14 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>226.10 (n/a)</td><td>187.54 (n/a)</td><td>177.30 (n/a)</td><td>171.80 (n/a)</td><td>22.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>237.70 (n/a)</td><td>200.12 (n/a)</td><td>207.80 (n/a)</td><td>157.90 (n/a)</td><td>31.43 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>232.10 (n/a)</td><td>192.20 (n/a)</td><td>193.10 (n/a)</td><td>139.40 (n/a)</td><td>33.62 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>218.50 (n/a)</td><td>195.86 (n/a)</td><td>205.90 (n/a)</td><td>162.90 (n/a)</td><td>23.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.00 (n/a)</td><td>181.50 (n/a)</td><td>174.46 (n/a)</td><td>174.80 (n/a)</td><td>169.90 (n/a)</td><td>4.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>212.70 (n/a)</td><td>171.10 (n/a)</td><td>155.00 (n/a)</td><td>143.80 (n/a)</td><td>31.26 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>264.90 (n/a)</td><td>214.32 (n/a)</td><td>186.10 (n/a)</td><td>178.20 (n/a)</td><td>44.77 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.04 (n/a)</td><td>214.00 (n/a)</td><td>188.10 (n/a)</td><td>190.10 (n/a)</td><td>150.70 (n/a)</td><td>25.92 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.06 (n/a)</td><td>211.70 (n/a)</td><td>182.06 (n/a)</td><td>185.20 (n/a)</td><td>130.20 (n/a)</td><td>32.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>240.00 (n/a)</td><td>197.72 (n/a)</td><td>188.60 (n/a)</td><td>172.90 (n/a)</td><td>25.58 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>14.44 (-2.40%)</td><td>13.51 (+1.50%)</td><td>13.19 (+0.99%)</td><td>12.79 (+2.92%)</td><td>0.72 <b>(-24.52%)</b></td><td>4354.30 (-2.84%)</td><td>4131.12 (-1.65%)</td><td>4224.20 (-0.98%)</td><td>3857.00 (+2.46%)</td><td>215.78 <b>(-24.93%)</b></td><td>13919.33 (-2.40%)</td><td>13024.70 (+1.50%)</td><td>12709.40 (+0.99%)</td><td>12329.75 (+2.92%)</td><td>691.66 <b>(-24.52%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>14.80 (n/a)</td><td>13.31 (n/a)</td><td>13.06 (n/a)</td><td>12.43 (n/a)</td><td>0.95 (n/a)</td><td>4481.60 (n/a)</td><td>4200.24 (n/a)</td><td>4265.90 (n/a)</td><td>3764.50 (n/a)</td><td>287.44 (n/a)</td><td>14261.44 (n/a)</td><td>12832.07 (n/a)</td><td>12585.13 (n/a)</td><td>11979.51 (n/a)</td><td>916.40 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>14.92 (-5.18%)</td><td>14.33 (+2.87%)</td><td>14.44 (-0.84%)</td><td>13.49 <b>(+33.49%)</b></td><td>0.58 <b>(-73.43%)</b></td><td>971.70 <b>(-25.09%)</b></td><td>916.04 (-5.05%)</td><td>907.90 (+0.86%)</td><td>878.70 (+5.46%)</td><td>38.00 <b>(-79.80%)</b></td><td>9775.74 (-5.18%)</td><td>9389.88 (+2.87%)</td><td>9461.27 (-0.84%)</td><td>8840.15 <b>(+33.49%)</b></td><td>382.74 <b>(-73.43%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>15.73 (n/a)</td><td>13.93 (n/a)</td><td>14.56 (n/a)</td><td>10.11 (n/a)</td><td>2.20 (n/a)</td><td>1297.10 (n/a)</td><td>964.76 (n/a)</td><td>900.20 (n/a)</td><td>833.20 (n/a)</td><td>188.13 (n/a)</td><td>10309.27 (n/a)</td><td>9127.66 (n/a)</td><td>9541.83 (n/a)</td><td>6622.50 (n/a)</td><td>1440.41 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>14.02 (-0.06%)</td><td>13.45 (-1.41%)</td><td>13.77 (-0.55%)</td><td>12.10 (-4.83%)</td><td>0.79 <b>(+46.04%)</b></td><td>4605.50 (+5.07%)</td><td>4152.70 (+1.59%)</td><td>4044.20 (+0.55%)</td><td>3974.20 (+0.06%)</td><td>260.26 <b>(+53.83%)</b></td><td>13509.08 (-0.06%)</td><td>12966.20 (-1.41%)</td><td>13274.94 (-0.55%)</td><td>11657.14 (-4.83%)</td><td>757.94 <b>(+46.04%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>14.02 (n/a)</td><td>13.65 (n/a)</td><td>13.85 (n/a)</td><td>12.71 (n/a)</td><td>0.54 (n/a)</td><td>4383.10 (n/a)</td><td>4087.54 (n/a)</td><td>4021.90 (n/a)</td><td>3971.90 (n/a)</td><td>169.19 (n/a)</td><td>13516.63 (n/a)</td><td>13151.50 (n/a)</td><td>13348.84 (n/a)</td><td>12248.66 (n/a)</td><td>518.98 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>16.52 (+9.61%)</td><td>12.41 (+0.21%)</td><td>11.76 (+9.34%)</td><td>8.27 <b>(-22.14%)</b></td><td>3.47 <b>(+48.13%)</b></td><td>2160.70 <b>(+28.44%)</b></td><td>1536.46 (+3.68%)</td><td>1518.50 (-8.55%)</td><td>1081.30 (-8.77%)</td><td>442.80 <b>(+69.04%)</b></td><td>12412.12 (+9.61%)</td><td>9325.31 (+0.21%)</td><td>8838.69 (+9.34%)</td><td>6211.87 <b>(-22.14%)</b></td><td>2605.27 <b>(+48.13%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>15.07 (n/a)</td><td>12.38 (n/a)</td><td>10.76 (n/a)</td><td>10.62 (n/a)</td><td>2.34 (n/a)</td><td>1682.30 (n/a)</td><td>1481.86 (n/a)</td><td>1660.40 (n/a)</td><td>1185.20 (n/a)</td><td>261.95 (n/a)</td><td>11324.08 (n/a)</td><td>9306.13 (n/a)</td><td>8083.53 (n/a)</td><td>7978.34 (n/a)</td><td>1758.74 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>11.21 (+4.88%)</td><td>10.94 (+3.25%)</td><td>11.13 (+5.01%)</td><td>10.38 (-1.23%)</td><td>0.35 <b>(+371.05%)</b></td><td>7892.60 (+1.24%)</td><td>7494.70 (-3.07%)</td><td>7359.70 (-4.77%)</td><td>7307.10 (-4.66%)</td><td>247.10 <b>(+354.38%)</b></td><td>14694.47 (+4.88%)</td><td>14338.84 (+3.25%)</td><td>14589.53 (+5.01%)</td><td>13604.44 (-1.23%)</td><td>460.31 <b>(+371.07%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>10.69 (n/a)</td><td>10.60 (n/a)</td><td>10.60 (n/a)</td><td>10.51 (n/a)</td><td>0.07 (n/a)</td><td>7795.80 (n/a)</td><td>7731.94 (n/a)</td><td>7728.20 (n/a)</td><td>7664.10 (n/a)</td><td>54.38 (n/a)</td><td>14010.08 (n/a)</td><td>13887.68 (n/a)</td><td>13893.88 (n/a)</td><td>13773.42 (n/a)</td><td>97.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>11.63 <b>(-24.18%)</b></td><td>11.08 <b>(-22.90%)</b></td><td>11.01 <b>(-25.10%)</b></td><td>10.73 (-10.54%)</td><td>0.35 <b>(-74.70%)</b></td><td>2003.50 (+11.78%)</td><td>1942.28 <b>(+28.74%)</b></td><td>1952.00 <b>(+33.52%)</b></td><td>1848.50 <b>(+31.89%)</b></td><td>59.91 <b>(-63.15%)</b></td><td>9294.00 <b>(-24.18%)</b></td><td>8852.20 <b>(-22.90%)</b></td><td>8801.35 <b>(-25.10%)</b></td><td>8574.94 (-10.54%)</td><td>278.69 <b>(-74.70%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>15.34 (n/a)</td><td>14.37 (n/a)</td><td>14.70 (n/a)</td><td>11.99 (n/a)</td><td>1.38 (n/a)</td><td>1792.30 (n/a)</td><td>1508.74 (n/a)</td><td>1462.00 (n/a)</td><td>1401.50 (n/a)</td><td>162.57 (n/a)</td><td>12258.35 (n/a)</td><td>11481.79 (n/a)</td><td>11750.55 (n/a)</td><td>9585.45 (n/a)</td><td>1101.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>10.90 (-0.36%)</td><td>10.85 (+2.07%)</td><td>10.87 (+3.51%)</td><td>10.72 (+3.51%)</td><td>0.07 <b>(-72.90%)</b></td><td>7639.30 (-3.39%)</td><td>7553.08 (-2.07%)</td><td>7533.70 (-3.39%)</td><td>7514.40 (+0.37%)</td><td>50.85 <b>(-73.64%)</b></td><td>14289.17 (-0.36%)</td><td>14216.47 (+2.07%)</td><td>14252.61 (+3.51%)</td><td>14055.53 (+3.51%)</td><td>95.05 <b>(-72.90%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>10.94 (n/a)</td><td>10.63 (n/a)</td><td>10.51 (n/a)</td><td>10.36 (n/a)</td><td>0.27 (n/a)</td><td>7907.40 (n/a)</td><td>7712.98 (n/a)</td><td>7798.20 (n/a)</td><td>7487.00 (n/a)</td><td>192.91 (n/a)</td><td>14341.40 (n/a)</td><td>13928.26 (n/a)</td><td>13769.13 (n/a)</td><td>13578.97 (n/a)</td><td>350.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.89 <b>(+28.86%)</b></td><td>3.08 (+4.55%)</td><td>2.95 (-1.51%)</td><td>2.73 (-1.87%)</td><td>0.46 <b>(+360.41%)</b></td><td>505.00 (+1.90%)</td><td>454.24 (-2.93%)</td><td>466.40 (+1.52%)</td><td>354.20 <b>(-22.39%)</b></td><td>58.85 <b>(+254.43%)</b></td><td>757.88 <b>(+28.86%)</b></td><td>600.33 (+4.55%)</td><td>575.49 (-1.51%)</td><td>531.56 (-1.87%)</td><td>90.61 <b>(+360.41%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.02 (n/a)</td><td>2.94 (n/a)</td><td>3.00 (n/a)</td><td>2.78 (n/a)</td><td>0.10 (n/a)</td><td>495.60 (n/a)</td><td>467.96 (n/a)</td><td>459.40 (n/a)</td><td>456.40 (n/a)</td><td>16.60 (n/a)</td><td>588.14 (n/a)</td><td>574.19 (n/a)</td><td>584.30 (n/a)</td><td>541.69 (n/a)</td><td>19.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>4.05 (-2.93%)</td><td>3.64 (-1.52%)</td><td>3.56 (-1.78%)</td><td>3.41 (+3.15%)</td><td>0.25 <b>(-23.81%)</b></td><td>403.60 (-3.05%)</td><td>379.84 (+1.29%)</td><td>386.40 (+1.82%)</td><td>339.70 (+3.03%)</td><td>24.06 <b>(-24.55%)</b></td><td>790.25 (-2.93%)</td><td>709.15 (-1.52%)</td><td>694.74 (-1.78%)</td><td>665.16 (+3.15%)</td><td>47.79 <b>(-23.81%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>4.17 (n/a)</td><td>3.69 (n/a)</td><td>3.63 (n/a)</td><td>3.31 (n/a)</td><td>0.32 (n/a)</td><td>416.30 (n/a)</td><td>375.00 (n/a)</td><td>379.50 (n/a)</td><td>329.70 (n/a)</td><td>31.89 (n/a)</td><td>814.09 (n/a)</td><td>720.08 (n/a)</td><td>707.34 (n/a)</td><td>644.84 (n/a)</td><td>62.72 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>5.62 (-6.70%)</td><td>4.11 (-2.88%)</td><td>3.81 (-3.49%)</td><td>3.54 (+0.64%)</td><td>0.86 (-16.17%)</td><td>388.40 (-0.64%)</td><td>344.56 (+2.04%)</td><td>361.50 (+3.61%)</td><td>245.00 (+7.17%)</td><td>57.66 (-10.27%)</td><td>1095.59 (-6.70%)</td><td>801.34 (-2.88%)</td><td>742.63 (-3.49%)</td><td>691.08 (+0.64%)</td><td>167.17 (-16.17%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>6.02 (n/a)</td><td>4.23 (n/a)</td><td>3.94 (n/a)</td><td>3.52 (n/a)</td><td>1.02 (n/a)</td><td>390.90 (n/a)</td><td>337.68 (n/a)</td><td>348.90 (n/a)</td><td>228.60 (n/a)</td><td>64.26 (n/a)</td><td>1174.29 (n/a)</td><td>825.12 (n/a)</td><td>769.46 (n/a)</td><td>686.65 (n/a)</td><td>199.42 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>5.64 <b>(-29.78%)</b></td><td>4.04 (-8.60%)</td><td>3.62 (+0.80%)</td><td>3.49 (+5.83%)</td><td>0.91 <b>(-54.90%)</b></td><td>393.80 (-5.52%)</td><td>352.32 (+1.18%)</td><td>380.40 (-0.78%)</td><td>244.00 <b>(+42.44%)</b></td><td>63.07 <b>(-37.01%)</b></td><td>1100.22 <b>(-29.78%)</b></td><td>787.33 (-8.60%)</td><td>705.73 (+0.80%)</td><td>681.59 (+5.83%)</td><td>178.25 <b>(-54.90%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.03 (n/a)</td><td>4.42 (n/a)</td><td>3.59 (n/a)</td><td>3.30 (n/a)</td><td>2.03 (n/a)</td><td>416.80 (n/a)</td><td>348.22 (n/a)</td><td>383.40 (n/a)</td><td>171.30 (n/a)</td><td>100.12 (n/a)</td><td>1566.72 (n/a)</td><td>861.38 (n/a)</td><td>700.13 (n/a)</td><td>644.04 (n/a)</td><td>395.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>4.15 (+19.74%)</td><td>3.49 (+8.36%)</td><td>3.20 (-0.95%)</td><td>3.15 (+6.06%)</td><td>0.45 <b>(+153.11%)</b></td><td>437.60 (-5.71%)</td><td>399.70 (-6.80%)</td><td>430.50 (+0.96%)</td><td>332.00 (-16.48%)</td><td>47.58 <b>(+101.06%)</b></td><td>808.54 (+19.74%)</td><td>679.86 (+8.36%)</td><td>623.53 (-0.95%)</td><td>613.50 (+6.06%)</td><td>86.82 <b>(+153.11%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.46 (n/a)</td><td>3.22 (n/a)</td><td>3.23 (n/a)</td><td>2.97 (n/a)</td><td>0.18 (n/a)</td><td>464.10 (n/a)</td><td>428.86 (n/a)</td><td>426.40 (n/a)</td><td>397.50 (n/a)</td><td>23.66 (n/a)</td><td>675.25 (n/a)</td><td>627.43 (n/a)</td><td>629.49 (n/a)</td><td>578.45 (n/a)</td><td>34.30 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.52 (-9.01%)</td><td>3.17 (+2.08%)</td><td>3.04 (+6.58%)</td><td>2.88 (+4.96%)</td><td>0.28 <b>(-39.94%)</b></td><td>478.30 (-4.72%)</td><td>436.94 (-3.02%)</td><td>452.20 (-6.18%)</td><td>391.50 (+9.91%)</td><td>37.87 <b>(-37.53%)</b></td><td>685.67 (-9.01%)</td><td>618.14 (+2.08%)</td><td>593.57 (+6.58%)</td><td>561.28 (+4.96%)</td><td>54.73 <b>(-39.94%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.86 (n/a)</td><td>3.10 (n/a)</td><td>2.86 (n/a)</td><td>2.74 (n/a)</td><td>0.47 (n/a)</td><td>502.00 (n/a)</td><td>450.54 (n/a)</td><td>482.00 (n/a)</td><td>356.20 (n/a)</td><td>60.61 (n/a)</td><td>753.59 (n/a)</td><td>605.56 (n/a)</td><td>556.92 (n/a)</td><td>534.74 (n/a)</td><td>91.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.65 (+13.90%)</td><td>3.14 (+0.25%)</td><td>3.05 (-2.28%)</td><td>2.87 (-7.02%)</td><td>0.30 <b>(+555.00%)</b></td><td>478.80 (+7.55%)</td><td>441.38 (+0.41%)</td><td>451.60 (+2.33%)</td><td>376.70 (-12.19%)</td><td>39.02 <b>(+506.64%)</b></td><td>712.63 (+13.90%)</td><td>612.32 (+0.25%)</td><td>594.36 (-2.28%)</td><td>560.62 (-7.02%)</td><td>59.11 <b>(+555.00%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.21 (n/a)</td><td>3.13 (n/a)</td><td>3.12 (n/a)</td><td>3.09 (n/a)</td><td>0.05 (n/a)</td><td>445.20 (n/a)</td><td>439.56 (n/a)</td><td>441.30 (n/a)</td><td>429.00 (n/a)</td><td>6.43 (n/a)</td><td>625.67 (n/a)</td><td>610.78 (n/a)</td><td>608.22 (n/a)</td><td>602.97 (n/a)</td><td>9.02 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.53 (-19.86%)</td><td>1.14 (-13.90%)</td><td>1.02 (-14.31%)</td><td>1.00 (+2.09%)</td><td>0.22 <b>(-42.60%)</b></td><td>402.90 (-2.04%)</td><td>360.32 (+11.94%)</td><td>392.70 (+16.70%)</td><td>262.90 <b>(+24.77%)</b></td><td>58.13 <b>(-31.09%)</b></td><td>127.64 (-19.86%)</td><td>95.51 (-13.90%)</td><td>85.44 (-14.31%)</td><td>83.29 (+2.09%)</td><td>18.61 <b>(-42.60%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.91 (n/a)</td><td>1.33 (n/a)</td><td>1.19 (n/a)</td><td>0.98 (n/a)</td><td>0.39 (n/a)</td><td>411.30 (n/a)</td><td>321.90 (n/a)</td><td>336.50 (n/a)</td><td>210.70 (n/a)</td><td>84.35 (n/a)</td><td>159.27 (n/a)</td><td>110.93 (n/a)</td><td>99.70 (n/a)</td><td>81.59 (n/a)</td><td>32.42 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>5.68 (+9.18%)</td><td>5.07 (+5.95%)</td><td>5.02 (+7.59%)</td><td>4.57 (-1.28%)</td><td>0.41 <b>(+69.47%)</b></td><td>423.50 (+1.29%)</td><td>383.28 (-5.31%)</td><td>385.10 (-7.05%)</td><td>340.40 (-8.40%)</td><td>30.30 <b>(+56.82%)</b></td><td>1182.89 (+9.18%)</td><td>1055.90 (+5.95%)</td><td>1045.69 (+7.59%)</td><td>950.79 (-1.28%)</td><td>85.06 <b>(+69.47%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>5.20 (n/a)</td><td>4.79 (n/a)</td><td>4.67 (n/a)</td><td>4.62 (n/a)</td><td>0.24 (n/a)</td><td>418.10 (n/a)</td><td>404.78 (n/a)</td><td>414.30 (n/a)</td><td>371.60 (n/a)</td><td>19.32 (n/a)</td><td>1083.43 (n/a)</td><td>996.65 (n/a)</td><td>971.92 (n/a)</td><td>963.16 (n/a)</td><td>50.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>16.22 (-3.94%)</td><td>12.38 (-6.70%)</td><td>11.11 (-17.46%)</td><td>9.90 (-5.83%)</td><td>2.59 (+9.05%)</td><td>556.10 (+6.19%)</td><td>459.08 (+8.00%)</td><td>495.30 <b>(+21.13%)</b></td><td>339.30 (+4.08%)</td><td>87.83 <b>(+20.18%)</b></td><td>6328.52 (-3.94%)</td><td>4830.85 (-6.70%)</td><td>4335.45 (-17.46%)</td><td>3861.51 (-5.83%)</td><td>1009.10 (+9.05%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>16.89 (n/a)</td><td>13.27 (n/a)</td><td>13.46 (n/a)</td><td>10.51 (n/a)</td><td>2.37 (n/a)</td><td>523.70 (n/a)</td><td>425.06 (n/a)</td><td>408.90 (n/a)</td><td>326.00 (n/a)</td><td>73.08 (n/a)</td><td>6588.18 (n/a)</td><td>5177.93 (n/a)</td><td>5252.28 (n/a)</td><td>4100.64 (n/a)</td><td>925.35 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>8.43 (-0.44%)</td><td>6.95 (-12.25%)</td><td>7.90 (+1.29%)</td><td>4.52 <b>(-40.44%)</b></td><td>1.72 <b>(+408.04%)</b></td><td>1218.60 <b>(+67.92%)</b></td><td>840.52 <b>(+20.69%)</b></td><td>696.40 (-1.28%)</td><td>652.90 (+0.43%)</td><td>244.49 <b>(+748.39%)</b></td><td>3289.04 (-0.44%)</td><td>2709.66 (-12.25%)</td><td>3083.68 (+1.29%)</td><td>1762.32 <b>(-40.44%)</b></td><td>671.17 <b>(+408.04%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.47 (n/a)</td><td>7.92 (n/a)</td><td>7.80 (n/a)</td><td>7.59 (n/a)</td><td>0.34 (n/a)</td><td>725.70 (n/a)</td><td>696.42 (n/a)</td><td>705.40 (n/a)</td><td>650.10 (n/a)</td><td>28.82 (n/a)</td><td>3303.44 (n/a)</td><td>3088.01 (n/a)</td><td>3044.35 (n/a)</td><td>2959.03 (n/a)</td><td>132.11 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>11.58 <b>(+23.65%)</b></td><td>8.53 (+1.06%)</td><td>8.27 (-5.88%)</td><td>4.74 <b>(-25.93%)</b></td><td>2.60 <b>(+121.76%)</b></td><td>1224.20 <b>(+35.02%)</b></td><td>746.56 (+6.65%)</td><td>701.20 (+6.26%)</td><td>501.10 (-19.13%)</td><td>283.98 <b>(+142.70%)</b></td><td>4821.50 <b>(+23.65%)</b></td><td>3553.58 (+1.06%)</td><td>3445.59 (-5.88%)</td><td>1973.54 <b>(-25.93%)</b></td><td>1082.95 <b>(+121.76%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>9.36 (n/a)</td><td>8.44 (n/a)</td><td>8.79 (n/a)</td><td>6.40 (n/a)</td><td>1.17 (n/a)</td><td>906.70 (n/a)</td><td>700.04 (n/a)</td><td>659.90 (n/a)</td><td>619.60 (n/a)</td><td>117.01 (n/a)</td><td>3899.18 (n/a)</td><td>3516.28 (n/a)</td><td>3660.90 (n/a)</td><td>2664.57 (n/a)</td><td>488.35 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.30 (n/a)</td><td>169.26 (n/a)</td><td>170.00 (n/a)</td><td>157.90 (n/a)</td><td>10.20 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>316.00 (n/a)</td><td>189.48 (n/a)</td><td>180.40 (n/a)</td><td>131.50 (n/a)</td><td>74.67 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>296.70 (n/a)</td><td>206.80 (n/a)</td><td>183.10 (n/a)</td><td>172.10 (n/a)</td><td>51.50 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>243.50 (n/a)</td><td>184.64 (n/a)</td><td>180.30 (n/a)</td><td>132.60 (n/a)</td><td>42.29 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>221.00 (n/a)</td><td>174.22 (n/a)</td><td>164.80 (n/a)</td><td>136.60 (n/a)</td><td>33.23 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>253.90 (n/a)</td><td>197.10 (n/a)</td><td>181.10 (n/a)</td><td>139.90 (n/a)</td><td>49.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.80 (n/a)</td><td>186.20 (n/a)</td><td>191.80 (n/a)</td><td>163.50 (n/a)</td><td>13.48 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>228.80 (n/a)</td><td>208.32 (n/a)</td><td>213.80 (n/a)</td><td>180.00 (n/a)</td><td>18.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.50 (n/a)</td><td>169.12 (n/a)</td><td>177.40 (n/a)</td><td>130.20 (n/a)</td><td>24.93 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>277.10 (n/a)</td><td>221.20 (n/a)</td><td>225.50 (n/a)</td><td>173.40 (n/a)</td><td>37.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>173.36 (n/a)</td><td>186.40 (n/a)</td><td>125.40 (n/a)</td><td>34.01 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.90 (n/a)</td><td>161.60 (n/a)</td><td>167.90 (n/a)</td><td>120.60 (n/a)</td><td>26.65 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>244.30 (n/a)</td><td>168.28 (n/a)</td><td>157.00 (n/a)</td><td>127.40 (n/a)</td><td>48.77 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>320.50 (n/a)</td><td>197.84 (n/a)</td><td>181.60 (n/a)</td><td>129.20 (n/a)</td><td>72.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>211.10 (n/a)</td><td>188.26 (n/a)</td><td>197.40 (n/a)</td><td>154.70 (n/a)</td><td>22.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>325.10 (n/a)</td><td>226.10 (n/a)</td><td>209.20 (n/a)</td><td>175.50 (n/a)</td><td>59.75 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>221.70 (n/a)</td><td>169.28 (n/a)</td><td>152.70 (n/a)</td><td>127.40 (n/a)</td><td>41.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.60 (n/a)</td><td>172.30 (n/a)</td><td>174.30 (n/a)</td><td>149.90 (n/a)</td><td>21.00 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>199.20 (n/a)</td><td>168.00 (n/a)</td><td>178.90 (n/a)</td><td>135.10 (n/a)</td><td>29.23 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>259.30 (n/a)</td><td>173.14 (n/a)</td><td>159.20 (n/a)</td><td>110.20 (n/a)</td><td>54.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>319.20 (n/a)</td><td>209.12 (n/a)</td><td>189.20 (n/a)</td><td>153.10 (n/a)</td><td>65.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>266.00 (n/a)</td><td>200.06 (n/a)</td><td>189.40 (n/a)</td><td>173.80 (n/a)</td><td>37.85 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>188.80 (n/a)</td><td>174.56 (n/a)</td><td>181.40 (n/a)</td><td>149.90 (n/a)</td><td>15.29 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>271.20 (n/a)</td><td>213.10 (n/a)</td><td>194.20 (n/a)</td><td>186.40 (n/a)</td><td>35.27 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>333.50 (n/a)</td><td>210.84 (n/a)</td><td>186.90 (n/a)</td><td>157.50 (n/a)</td><td>71.72 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>217.80 (n/a)</td><td>173.52 (n/a)</td><td>169.40 (n/a)</td><td>154.30 (n/a)</td><td>25.93 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>231.60 (n/a)</td><td>181.46 (n/a)</td><td>165.90 (n/a)</td><td>152.00 (n/a)</td><td>34.23 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>196.10 (n/a)</td><td>174.98 (n/a)</td><td>178.20 (n/a)</td><td>147.10 (n/a)</td><td>18.02 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>197.30 (n/a)</td><td>167.48 (n/a)</td><td>168.50 (n/a)</td><td>147.20 (n/a)</td><td>21.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>241.30 (n/a)</td><td>188.98 (n/a)</td><td>192.00 (n/a)</td><td>136.90 (n/a)</td><td>37.85 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>268.10 (n/a)</td><td>180.94 (n/a)</td><td>165.10 (n/a)</td><td>112.30 (n/a)</td><td>59.09 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.23 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>289.10 (n/a)</td><td>210.12 (n/a)</td><td>207.20 (n/a)</td><td>142.20 (n/a)</td><td>52.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>4.12 (-0.05%)</td><td>4.11 (-0.06%)</td><td>4.11 (-0.11%)</td><td>4.09 (+0.06%)</td><td>0.01 (-18.12%)</td><td>19210.80 (-0.06%)</td><td>19151.42 (+0.06%)</td><td>19145.30 (+0.11%)</td><td>19088.90 (+0.05%)</td><td>44.12 (-18.17%)</td><td>2812.48 (-0.05%)</td><td>2803.31 (-0.06%)</td><td>2804.18 (-0.11%)</td><td>2794.64 (+0.06%)</td><td>6.46 (-18.12%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>4.12 (n/a)</td><td>4.11 (n/a)</td><td>4.11 (n/a)</td><td>4.09 (n/a)</td><td>0.01 (n/a)</td><td>19223.20 (n/a)</td><td>19140.16 (n/a)</td><td>19124.70 (n/a)</td><td>19080.10 (n/a)</td><td>53.91 (n/a)</td><td>2813.78 (n/a)</td><td>2804.96 (n/a)</td><td>2807.21 (n/a)</td><td>2792.83 (n/a)</td><td>7.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>4.20 (-1.34%)</td><td>4.13 (+0.65%)</td><td>4.16 (+0.80%)</td><td>4.06 (+4.15%)</td><td>0.06 <b>(-58.26%)</b></td><td>2319.00 (-3.98%)</td><td>2275.82 (-0.72%)</td><td>2263.00 (-0.79%)</td><td>2240.30 (+1.36%)</td><td>32.38 <b>(-59.41%)</b></td><td>1651.30 (-1.34%)</td><td>1625.77 (+0.65%)</td><td>1634.70 (+0.80%)</td><td>1595.24 (+4.15%)</td><td>23.03 <b>(-58.26%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>4.25 (n/a)</td><td>4.11 (n/a)</td><td>4.12 (n/a)</td><td>3.89 (n/a)</td><td>0.14 (n/a)</td><td>2415.20 (n/a)</td><td>2292.40 (n/a)</td><td>2281.10 (n/a)</td><td>2210.20 (n/a)</td><td>79.78 (n/a)</td><td>1673.76 (n/a)</td><td>1615.28 (n/a)</td><td>1621.72 (n/a)</td><td>1531.69 (n/a)</td><td>55.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.06 (-5.64%)</td><td>0.79 (-16.89%)</td><td>0.66 <b>(-28.24%)</b></td><td>0.62 <b>(-22.74%)</b></td><td>0.19 <b>(+60.63%)</b></td><td>356.40 <b>(+29.41%)</b></td><td>294.40 <b>(+24.23%)</b></td><td>332.80 <b>(+39.36%)</b></td><td>208.60 (+6.00%)</td><td>65.48 <b>(+122.42%)</b></td><td>45.24 (-5.64%)</td><td>33.52 (-16.89%)</td><td>28.36 <b>(-28.24%)</b></td><td>26.48 <b>(-22.74%)</b></td><td>8.28 <b>(+60.63%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.12 (n/a)</td><td>0.95 (n/a)</td><td>0.93 (n/a)</td><td>0.80 (n/a)</td><td>0.12 (n/a)</td><td>275.40 (n/a)</td><td>236.98 (n/a)</td><td>238.80 (n/a)</td><td>196.80 (n/a)</td><td>29.44 (n/a)</td><td>47.95 (n/a)</td><td>40.33 (n/a)</td><td>39.52 (n/a)</td><td>34.27 (n/a)</td><td>5.15 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.17 (-14.99%)</td><td>1.00 (-7.24%)</td><td>1.08 (+3.30%)</td><td>0.70 (-18.63%)</td><td>0.18 (-18.76%)</td><td>317.40 <b>(+22.88%)</b></td><td>229.30 (+7.64%)</td><td>204.50 (-3.17%)</td><td>189.40 (+17.64%)</td><td>51.53 (+17.69%)</td><td>49.83 (-14.99%)</td><td>42.56 (-7.24%)</td><td>46.15 (+3.30%)</td><td>29.73 (-18.63%)</td><td>7.87 (-18.76%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.37 (n/a)</td><td>1.08 (n/a)</td><td>1.05 (n/a)</td><td>0.86 (n/a)</td><td>0.23 (n/a)</td><td>258.30 (n/a)</td><td>213.02 (n/a)</td><td>211.20 (n/a)</td><td>161.00 (n/a)</td><td>43.79 (n/a)</td><td>58.61 (n/a)</td><td>45.88 (n/a)</td><td>44.68 (n/a)</td><td>36.54 (n/a)</td><td>9.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.53 (+0.06%)</td><td>0.53 (+0.05%)</td><td>0.53 (+0.00%)</td><td>0.53 (+0.08%)</td><td>0.00 <b>(-20.66%)</b></td><td>47834.90 (-0.08%)</td><td>47811.60 (-0.05%)</td><td>47816.60 (-0.00%)</td><td>47787.80 (-0.06%)</td><td>20.37 <b>(-20.67%)</b></td><td>359.50 (+0.06%)</td><td>359.32 (+0.05%)</td><td>359.29 (+0.00%)</td><td>359.15 (+0.08%)</td><td>0.15 <b>(-20.67%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47872.30 (n/a)</td><td>47834.04 (n/a)</td><td>47817.30 (n/a)</td><td>47814.40 (n/a)</td><td>25.68 (n/a)</td><td>359.30 (n/a)</td><td>359.16 (n/a)</td><td>359.28 (n/a)</td><td>358.87 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (+0.29%)</td><td>0.21 (+0.16%)</td><td>0.21 (-0.09%)</td><td>0.21 (+0.95%)</td><td>0.00 (-16.35%)</td><td>119499.30 (-0.94%)</td><td>118407.18 (-0.17%)</td><td>118650.30 (+0.09%)</td><td>116538.90 (-0.29%)</td><td>1227.79 (-17.32%)</td><td>147.42 (+0.29%)</td><td>145.10 (+0.16%)</td><td>144.79 (-0.09%)</td><td>143.77 (+0.95%)</td><td>1.51 (-16.35%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>120635.40 (n/a)</td><td>118604.84 (n/a)</td><td>118540.00 (n/a)</td><td>116873.70 (n/a)</td><td>1485.00 (n/a)</td><td>147.00 (n/a)</td><td>144.87 (n/a)</td><td>144.93 (n/a)</td><td>142.41 (n/a)</td><td>1.81 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.91 (+0.17%)</td><td>0.90 (+0.14%)</td><td>0.90 (-0.13%)</td><td>0.90 (+0.56%)</td><td>0.00 <b>(-46.26%)</b></td><td>27938.40 (-0.56%)</td><td>27872.36 (-0.14%)</td><td>27884.60 (+0.13%)</td><td>27766.70 (-0.17%)</td><td>65.53 <b>(-46.64%)</b></td><td>618.72 (+0.17%)</td><td>616.38 (+0.14%)</td><td>616.11 (-0.13%)</td><td>614.92 (+0.56%)</td><td>1.45 <b>(-46.25%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>28094.60 (n/a)</td><td>27911.78 (n/a)</td><td>27847.20 (n/a)</td><td>27814.00 (n/a)</td><td>122.82 (n/a)</td><td>617.67 (n/a)</td><td>615.52 (n/a)</td><td>616.93 (n/a)</td><td>611.50 (n/a)</td><td>2.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.64 (+0.07%)</td><td>3.63 (+1.11%)</td><td>3.63 (+0.32%)</td><td>3.61 (+4.65%)</td><td>0.01 <b>(-86.94%)</b></td><td>6961.90 (-4.44%)</td><td>6934.04 (-1.13%)</td><td>6932.10 (-0.32%)</td><td>6908.40 (-0.07%)</td><td>19.07 <b>(-87.58%)</b></td><td>2486.82 (+0.07%)</td><td>2477.63 (+1.11%)</td><td>2478.29 (+0.32%)</td><td>2467.70 (+4.65%)</td><td>6.81 <b>(-86.94%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.64 (n/a)</td><td>3.59 (n/a)</td><td>3.62 (n/a)</td><td>3.45 (n/a)</td><td>0.08 (n/a)</td><td>7285.70 (n/a)</td><td>7013.48 (n/a)</td><td>6954.30 (n/a)</td><td>6912.90 (n/a)</td><td>153.48 (n/a)</td><td>2485.19 (n/a)</td><td>2450.46 (n/a)</td><td>2470.39 (n/a)</td><td>2358.03 (n/a)</td><td>52.16 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>2.93 (-6.42%)</td><td>2.88 (-1.21%)</td><td>2.88 (-0.60%)</td><td>2.83 (+1.79%)</td><td>0.04 <b>(-73.47%)</b></td><td>8900.80 (-1.75%)</td><td>8740.96 (+1.07%)</td><td>8739.00 (+0.61%)</td><td>8598.00 (+6.86%)</td><td>107.44 <b>(-71.97%)</b></td><td>1998.12 (-6.42%)</td><td>1965.68 (-1.21%)</td><td>1965.88 (-0.60%)</td><td>1930.15 (+1.79%)</td><td>24.10 <b>(-73.47%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.13 (n/a)</td><td>2.91 (n/a)</td><td>2.90 (n/a)</td><td>2.78 (n/a)</td><td>0.13 (n/a)</td><td>9059.70 (n/a)</td><td>8648.42 (n/a)</td><td>8686.30 (n/a)</td><td>8046.40 (n/a)</td><td>383.29 (n/a)</td><td>2135.10 (n/a)</td><td>1989.69 (n/a)</td><td>1977.81 (n/a)</td><td>1896.30 (n/a)</td><td>90.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.31 (+0.59%)</td><td>3.22 (+0.85%)</td><td>3.20 (+0.62%)</td><td>3.15 (+0.81%)</td><td>0.07 (-7.79%)</td><td>7998.70 (-0.80%)</td><td>7810.24 (-0.85%)</td><td>7853.50 (-0.62%)</td><td>7592.60 (-0.58%)</td><td>168.96 (-9.32%)</td><td>2262.72 (+0.59%)</td><td>2200.49 (+0.85%)</td><td>2187.54 (+0.62%)</td><td>2147.84 (+0.81%)</td><td>47.84 (-7.79%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.30 (n/a)</td><td>3.20 (n/a)</td><td>3.18 (n/a)</td><td>3.12 (n/a)</td><td>0.08 (n/a)</td><td>8063.20 (n/a)</td><td>7876.86 (n/a)</td><td>7902.10 (n/a)</td><td>7637.10 (n/a)</td><td>186.33 (n/a)</td><td>2249.51 (n/a)</td><td>2182.03 (n/a)</td><td>2174.08 (n/a)</td><td>2130.66 (n/a)</td><td>51.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.80 (+0.48%)</td><td>0.80 (+0.15%)</td><td>0.80 (+0.10%)</td><td>0.80 (+0.02%)</td><td>0.00 <b>(+368.82%)</b></td><td>94849.70 (-0.02%)</td><td>94694.12 (-0.15%)</td><td>94777.70 (-0.10%)</td><td>94315.20 (-0.48%)</td><td>215.11 <b>(+366.09%)</b></td><td>728.62 (+0.48%)</td><td>725.70 (+0.15%)</td><td>725.06 (+0.10%)</td><td>724.51 (+0.02%)</td><td>1.65 <b>(+368.80%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94872.30 (n/a)</td><td>94840.20 (n/a)</td><td>94870.30 (n/a)</td><td>94768.20 (n/a)</td><td>46.15 (n/a)</td><td>725.13 (n/a)</td><td>724.58 (n/a)</td><td>724.35 (n/a)</td><td>724.34 (n/a)</td><td>0.35 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.73 (-0.37%)</td><td>0.73 (-0.17%)</td><td>0.73 (-0.04%)</td><td>0.73 (-0.06%)</td><td>0.00 <b>(-82.46%)</b></td><td>103392.10 (+0.06%)</td><td>103339.90 (+0.17%)</td><td>103330.80 (+0.04%)</td><td>103297.90 (+0.37%)</td><td>34.42 <b>(-82.39%)</b></td><td>665.26 (-0.37%)</td><td>664.98 (-0.17%)</td><td>665.04 (-0.04%)</td><td>664.65 (-0.06%)</td><td>0.22 <b>(-82.46%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103329.60 (n/a)</td><td>103167.04 (n/a)</td><td>103285.80 (n/a)</td><td>102913.30 (n/a)</td><td>195.50 (n/a)</td><td>667.74 (n/a)</td><td>666.10 (n/a)</td><td>665.33 (n/a)</td><td>665.05 (n/a)</td><td>1.26 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.69 (+0.54%)</td><td>0.69 (+0.60%)</td><td>0.69 (+0.62%)</td><td>0.69 (+0.58%)</td><td>0.00 (-0.80%)</td><td>110023.60 (-0.58%)</td><td>109727.34 (-0.59%)</td><td>109850.60 (-0.61%)</td><td>109342.30 (-0.54%)</td><td>292.17 (-1.91%)</td><td>628.48 (+0.54%)</td><td>626.28 (+0.60%)</td><td>625.57 (+0.62%)</td><td>624.59 (+0.58%)</td><td>1.67 (-0.80%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110662.10 (n/a)</td><td>110382.84 (n/a)</td><td>110527.70 (n/a)</td><td>109932.70 (n/a)</td><td>297.84 (n/a)</td><td>625.10 (n/a)</td><td>622.56 (n/a)</td><td>621.74 (n/a)</td><td>620.98 (n/a)</td><td>1.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>2.82 (+0.45%)</td><td>2.80 (+0.19%)</td><td>2.80 (+0.08%)</td><td>2.79 (+0.26%)</td><td>0.01 <b>(+41.72%)</b></td><td>37527.50 (-0.26%)</td><td>37435.12 (-0.19%)</td><td>37502.00 (-0.08%)</td><td>37159.40 (-0.45%)</td><td>156.03 <b>(+40.76%)</b></td><td>2889.56 (+0.45%)</td><td>2868.32 (+0.19%)</td><td>2863.16 (+0.08%)</td><td>2861.21 (+0.26%)</td><td>12.02 <b>(+41.72%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>2.81 (n/a)</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>2.79 (n/a)</td><td>0.01 (n/a)</td><td>37624.60 (n/a)</td><td>37505.70 (n/a)</td><td>37532.50 (n/a)</td><td>37326.60 (n/a)</td><td>110.85 (n/a)</td><td>2876.62 (n/a)</td><td>2862.90 (n/a)</td><td>2860.83 (n/a)</td><td>2853.83 (n/a)</td><td>8.48 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>7.41 (+0.30%)</td><td>6.89 (-3.12%)</td><td>6.81 (-4.54%)</td><td>6.22 (-9.46%)</td><td>0.52 <b>(+126.44%)</b></td><td>1432.80 (+10.45%)</td><td>1299.96 (+3.61%)</td><td>1308.50 (+4.76%)</td><td>1202.70 (-0.29%)</td><td>99.17 <b>(+144.51%)</b></td><td>446.40 (+0.30%)</td><td>414.91 (-3.12%)</td><td>410.30 (-4.54%)</td><td>374.70 (-9.46%)</td><td>31.37 <b>(+126.44%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>7.39 (n/a)</td><td>7.11 (n/a)</td><td>7.14 (n/a)</td><td>6.87 (n/a)</td><td>0.23 (n/a)</td><td>1297.20 (n/a)</td><td>1254.66 (n/a)</td><td>1249.10 (n/a)</td><td>1206.20 (n/a)</td><td>40.56 (n/a)</td><td>445.09 (n/a)</td><td>428.25 (n/a)</td><td>429.79 (n/a)</td><td>413.86 (n/a)</td><td>13.85 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>6.98 (+2.04%)</td><td>6.73 (+5.92%)</td><td>6.90 (+2.65%)</td><td>6.11 <b>(+29.89%)</b></td><td>0.36 <b>(-60.71%)</b></td><td>1458.70 <b>(-23.01%)</b></td><td>1327.86 (-7.34%)</td><td>1292.30 (-2.59%)</td><td>1277.70 (-2.00%)</td><td>76.10 <b>(-70.54%)</b></td><td>420.18 (+2.04%)</td><td>405.32 (+5.92%)</td><td>415.44 (+2.65%)</td><td>368.05 <b>(+29.89%)</b></td><td>21.86 <b>(-60.71%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>6.84 (n/a)</td><td>6.35 (n/a)</td><td>6.72 (n/a)</td><td>4.70 (n/a)</td><td>0.92 (n/a)</td><td>1894.70 (n/a)</td><td>1433.00 (n/a)</td><td>1326.60 (n/a)</td><td>1303.80 (n/a)</td><td>258.35 (n/a)</td><td>411.78 (n/a)</td><td>382.68 (n/a)</td><td>404.71 (n/a)</td><td>283.36 (n/a)</td><td>55.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>7.11 (+2.75%)</td><td>6.79 (+6.02%)</td><td>6.92 (+10.70%)</td><td>6.42 (+6.83%)</td><td>0.29 <b>(-33.68%)</b></td><td>1387.70 (-6.39%)</td><td>1314.08 (-5.89%)</td><td>1287.70 (-9.67%)</td><td>1253.60 (-2.68%)</td><td>57.28 <b>(-39.42%)</b></td><td>428.28 (+2.75%)</td><td>409.17 (+6.02%)</td><td>416.93 (+10.70%)</td><td>386.89 (+6.83%)</td><td>17.62 <b>(-33.68%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>6.92 (n/a)</td><td>6.41 (n/a)</td><td>6.25 (n/a)</td><td>6.01 (n/a)</td><td>0.44 (n/a)</td><td>1482.40 (n/a)</td><td>1396.32 (n/a)</td><td>1425.50 (n/a)</td><td>1288.10 (n/a)</td><td>94.56 (n/a)</td><td>416.79 (n/a)</td><td>385.93 (n/a)</td><td>376.62 (n/a)</td><td>362.16 (n/a)</td><td>26.57 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>8.16 (+0.76%)</td><td>8.08 (+4.74%)</td><td>8.07 (+1.61%)</td><td>7.99 (+13.16%)</td><td>0.07 <b>(-83.55%)</b></td><td>4362.70 (-11.63%)</td><td>4317.26 (-4.78%)</td><td>4321.30 (-1.59%)</td><td>4272.70 (-0.75%)</td><td>38.77 <b>(-85.56%)</b></td><td>502.60 (+0.76%)</td><td>497.45 (+4.74%)</td><td>496.95 (+1.61%)</td><td>492.24 (+13.16%)</td><td>4.47 <b>(-83.55%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.10 (n/a)</td><td>7.71 (n/a)</td><td>7.94 (n/a)</td><td>7.06 (n/a)</td><td>0.44 (n/a)</td><td>4936.80 (n/a)</td><td>4533.94 (n/a)</td><td>4390.90 (n/a)</td><td>4305.10 (n/a)</td><td>268.45 (n/a)</td><td>498.82 (n/a)</td><td>474.93 (n/a)</td><td>489.08 (n/a)</td><td>434.99 (n/a)</td><td>27.16 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>7.58 (-4.13%)</td><td>7.39 (-1.47%)</td><td>7.55 (-0.47%)</td><td>7.10 (+3.62%)</td><td>0.24 <b>(-39.23%)</b></td><td>4909.50 (-3.50%)</td><td>4719.76 (+1.35%)</td><td>4617.60 (+0.47%)</td><td>4598.50 (+4.31%)</td><td>153.02 <b>(-39.74%)</b></td><td>466.99 (-4.13%)</td><td>455.38 (-1.47%)</td><td>465.07 (-0.47%)</td><td>437.42 (+3.62%)</td><td>14.58 <b>(-39.23%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>7.91 (n/a)</td><td>7.50 (n/a)</td><td>7.59 (n/a)</td><td>6.85 (n/a)</td><td>0.39 (n/a)</td><td>5087.40 (n/a)</td><td>4657.06 (n/a)</td><td>4595.80 (n/a)</td><td>4408.60 (n/a)</td><td>253.96 (n/a)</td><td>487.11 (n/a)</td><td>462.17 (n/a)</td><td>467.27 (n/a)</td><td>422.12 (n/a)</td><td>23.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>7.44 (-1.30%)</td><td>7.25 (-1.64%)</td><td>7.38 (-1.63%)</td><td>6.75 (-1.97%)</td><td>0.28 (+2.75%)</td><td>5165.10 (+2.01%)</td><td>4816.04 (+1.67%)</td><td>4722.40 (+1.66%)</td><td>4688.20 (+1.32%)</td><td>198.15 (+6.50%)</td><td>458.06 (-1.30%)</td><td>446.48 (-1.64%)</td><td>454.75 (-1.63%)</td><td>415.77 (-1.97%)</td><td>17.48 (+2.75%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>7.53 (n/a)</td><td>7.37 (n/a)</td><td>7.51 (n/a)</td><td>6.89 (n/a)</td><td>0.28 (n/a)</td><td>5063.50 (n/a)</td><td>4736.76 (n/a)</td><td>4645.20 (n/a)</td><td>4627.20 (n/a)</td><td>186.05 (n/a)</td><td>464.10 (n/a)</td><td>453.90 (n/a)</td><td>462.30 (n/a)</td><td>424.11 (n/a)</td><td>17.01 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.80 (-0.01%)</td><td>0.80 (-0.00%)</td><td>0.80 (-0.03%)</td><td>0.80 (+0.08%)</td><td>0.00 <b>(-52.48%)</b></td><td>94156.60 (-0.08%)</td><td>94091.24 (+0.00%)</td><td>94081.20 (+0.03%)</td><td>94056.20 (+0.01%)</td><td>38.48 <b>(-52.49%)</b></td><td>730.62 (-0.01%)</td><td>730.35 (-0.00%)</td><td>730.43 (-0.03%)</td><td>729.84 (+0.08%)</td><td>0.30 <b>(-52.48%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94233.00 (n/a)</td><td>94089.96 (n/a)</td><td>94053.50 (n/a)</td><td>94042.30 (n/a)</td><td>80.99 (n/a)</td><td>730.73 (n/a)</td><td>730.36 (n/a)</td><td>730.64 (n/a)</td><td>729.25 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.74 (-0.27%)</td><td>0.74 (-0.05%)</td><td>0.74 (+0.03%)</td><td>0.73 (-0.05%)</td><td>0.00 <b>(-34.61%)</b></td><td>102850.60 (+0.05%)</td><td>102640.02 (+0.05%)</td><td>102585.60 (-0.03%)</td><td>102575.40 (+0.27%)</td><td>118.36 <b>(-34.36%)</b></td><td>669.94 (-0.27%)</td><td>669.52 (-0.05%)</td><td>669.87 (+0.03%)</td><td>668.15 (-0.05%)</td><td>0.77 <b>(-34.61%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>102797.60 (n/a)</td><td>102593.50 (n/a)</td><td>102615.70 (n/a)</td><td>102302.20 (n/a)</td><td>180.30 (n/a)</td><td>671.73 (n/a)</td><td>669.82 (n/a)</td><td>669.68 (n/a)</td><td>668.49 (n/a)</td><td>1.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.71 (-0.09%)</td><td>0.71 (-0.06%)</td><td>0.71 (-0.01%)</td><td>0.71 (-0.13%)</td><td>0.00 <b>(+24.38%)</b></td><td>106230.40 (+0.13%)</td><td>105991.34 (+0.06%)</td><td>105927.90 (+0.01%)</td><td>105871.00 (+0.09%)</td><td>143.78 <b>(+24.66%)</b></td><td>649.09 (-0.09%)</td><td>648.35 (-0.06%)</td><td>648.74 (-0.01%)</td><td>646.89 (-0.13%)</td><td>0.88 <b>(+24.37%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106090.00 (n/a)</td><td>105923.70 (n/a)</td><td>105914.20 (n/a)</td><td>105777.10 (n/a)</td><td>115.34 (n/a)</td><td>649.66 (n/a)</td><td>648.76 (n/a)</td><td>648.82 (n/a)</td><td>647.75 (n/a)</td><td>0.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.71 (+3.86%)</td><td>3.24 (-1.71%)</td><td>3.03 (-9.21%)</td><td>2.90 (-2.43%)</td><td>0.40 <b>(+43.59%)</b></td><td>2782.00 (+2.49%)</td><td>2515.88 (+2.35%)</td><td>2657.10 (+10.14%)</td><td>2171.00 (-3.72%)</td><td>299.91 <b>(+41.69%)</b></td><td>973.72 (+3.86%)</td><td>850.28 (-1.71%)</td><td>795.57 (-9.21%)</td><td>759.85 (-2.43%)</td><td>105.40 <b>(+43.59%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.58 (n/a)</td><td>3.30 (n/a)</td><td>3.34 (n/a)</td><td>2.97 (n/a)</td><td>0.28 (n/a)</td><td>2714.30 (n/a)</td><td>2458.08 (n/a)</td><td>2412.40 (n/a)</td><td>2254.80 (n/a)</td><td>211.67 (n/a)</td><td>937.53 (n/a)</td><td>865.05 (n/a)</td><td>876.29 (n/a)</td><td>778.81 (n/a)</td><td>73.40 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.54 (-0.30%)</td><td>0.36 (-12.87%)</td><td>0.32 (-16.53%)</td><td>0.30 (-8.15%)</td><td>0.10 (+1.60%)</td><td>4117.40 (+8.87%)</td><td>3580.58 (+15.11%)</td><td>3836.50 (+19.80%)</td><td>2326.00 (+0.29%)</td><td>717.49 (+5.35%)</td><td>28.85 (-0.30%)</td><td>19.58 (-12.87%)</td><td>17.49 (-16.53%)</td><td>16.30 (-8.15%)</td><td>5.23 (+1.60%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.54 (n/a)</td><td>0.42 (n/a)</td><td>0.39 (n/a)</td><td>0.33 (n/a)</td><td>0.10 (n/a)</td><td>3781.90 (n/a)</td><td>3110.64 (n/a)</td><td>3202.40 (n/a)</td><td>2319.20 (n/a)</td><td>681.08 (n/a)</td><td>28.94 (n/a)</td><td>22.47 (n/a)</td><td>20.96 (n/a)</td><td>17.74 (n/a)</td><td>5.14 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>4.83 (-0.82%)</td><td>4.29 (-2.14%)</td><td>4.61 (-3.11%)</td><td>3.37 (-1.11%)</td><td>0.67 (+2.42%)</td><td>1976.20 (+1.13%)</td><td>1584.60 (+2.32%)</td><td>1443.30 (+3.21%)</td><td>1375.90 (+0.83%)</td><td>267.45 (+4.17%)</td><td>1493.77 (-0.82%)</td><td>1324.70 (-2.14%)</td><td>1424.00 (-3.11%)</td><td>1039.99 (-1.11%)</td><td>205.73 (+2.42%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>4.87 (n/a)</td><td>4.38 (n/a)</td><td>4.76 (n/a)</td><td>3.40 (n/a)</td><td>0.65 (n/a)</td><td>1954.20 (n/a)</td><td>1548.68 (n/a)</td><td>1398.40 (n/a)</td><td>1364.60 (n/a)</td><td>256.74 (n/a)</td><td>1506.06 (n/a)</td><td>1353.60 (n/a)</td><td>1469.67 (n/a)</td><td>1051.70 (n/a)</td><td>200.87 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.27 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.28 (n/a)</td><td>12.37 (n/a)</td><td>12.54 (n/a)</td><td>10.36 (n/a)</td><td>1.17 (n/a)</td><td>13.27 (n/a)</td><td>12.36 (n/a)</td><td>12.53 (n/a)</td><td>10.35 (n/a)</td><td>1.17 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>24.76 (+0.29%)</td><td>22.20 (-8.07%)</td><td>23.32 (-3.27%)</td><td>15.42 <b>(-34.73%)</b></td><td>3.87 <b>(+821.92%)</b></td><td>24.74 (+0.29%)</td><td>22.19 (-8.07%)</td><td>23.30 (-3.27%)</td><td>15.41 <b>(-34.73%)</b></td><td>3.87 <b>(+821.91%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>24.68 (n/a)</td><td>24.15 (n/a)</td><td>24.10 (n/a)</td><td>23.63 (n/a)</td><td>0.42 (n/a)</td><td>24.67 (n/a)</td><td>24.13 (n/a)</td><td>24.09 (n/a)</td><td>23.62 (n/a)</td><td>0.42 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>43.51 (+3.10%)</td><td>40.70 (+0.16%)</td><td>40.28 (-0.23%)</td><td>38.48 (-2.57%)</td><td>2.06 <b>(+105.52%)</b></td><td>43.49 (+3.10%)</td><td>40.68 (+0.16%)</td><td>40.26 (-0.23%)</td><td>38.46 (-2.57%)</td><td>2.06 <b>(+105.52%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>42.21 (n/a)</td><td>40.64 (n/a)</td><td>40.38 (n/a)</td><td>39.50 (n/a)</td><td>1.00 (n/a)</td><td>42.18 (n/a)</td><td>40.62 (n/a)</td><td>40.35 (n/a)</td><td>39.48 (n/a)</td><td>1.00 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>45.13 (+1.17%)</td><td>42.08 (-2.68%)</td><td>42.57 (-1.44%)</td><td>36.94 (-11.17%)</td><td>3.19 <b>(+148.24%)</b></td><td>45.11 (+1.17%)</td><td>42.06 (-2.68%)</td><td>42.54 (-1.44%)</td><td>36.91 (-11.17%)</td><td>3.18 <b>(+148.24%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>44.61 (n/a)</td><td>43.24 (n/a)</td><td>43.19 (n/a)</td><td>41.58 (n/a)</td><td>1.28 (n/a)</td><td>44.58 (n/a)</td><td>43.21 (n/a)</td><td>43.16 (n/a)</td><td>41.55 (n/a)</td><td>1.28 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.16 (n/a)</td><td>12.43 (n/a)</td><td>12.64 (n/a)</td><td>11.61 (n/a)</td><td>0.64 (n/a)</td><td>13.15 (n/a)</td><td>12.43 (n/a)</td><td>12.63 (n/a)</td><td>11.60 (n/a)</td><td>0.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>24.66 (-1.14%)</td><td>24.31 (-0.77%)</td><td>24.35 (-0.25%)</td><td>23.94 (-0.95%)</td><td>0.27 (-15.57%)</td><td>24.64 (-1.14%)</td><td>24.30 (-0.77%)</td><td>24.33 (-0.25%)</td><td>23.92 (-0.95%)</td><td>0.27 (-15.57%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>24.94 (n/a)</td><td>24.50 (n/a)</td><td>24.41 (n/a)</td><td>24.17 (n/a)</td><td>0.32 (n/a)</td><td>24.93 (n/a)</td><td>24.49 (n/a)</td><td>24.39 (n/a)</td><td>24.15 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>44.17 (-3.24%)</td><td>40.77 (-2.43%)</td><td>40.19 (-2.56%)</td><td>38.06 (-2.46%)</td><td>2.29 (-4.97%)</td><td>44.14 (-3.24%)</td><td>40.75 (-2.43%)</td><td>40.17 (-2.56%)</td><td>38.03 (-2.46%)</td><td>2.29 (-4.97%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>45.65 (n/a)</td><td>41.79 (n/a)</td><td>41.25 (n/a)</td><td>39.02 (n/a)</td><td>2.41 (n/a)</td><td>45.62 (n/a)</td><td>41.76 (n/a)</td><td>41.22 (n/a)</td><td>38.99 (n/a)</td><td>2.41 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>46.63 (+9.82%)</td><td>43.20 (+2.82%)</td><td>42.76 (+1.93%)</td><td>40.83 (-1.44%)</td><td>2.23 <b>(+425.43%)</b></td><td>46.60 (+9.82%)</td><td>43.18 (+2.82%)</td><td>42.73 (+1.93%)</td><td>40.81 (-1.44%)</td><td>2.23 <b>(+425.42%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>42.46 (n/a)</td><td>42.02 (n/a)</td><td>41.95 (n/a)</td><td>41.43 (n/a)</td><td>0.43 (n/a)</td><td>42.43 (n/a)</td><td>41.99 (n/a)</td><td>41.93 (n/a)</td><td>41.40 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>9.75 (+4.14%)</td><td>9.08 (+2.83%)</td><td>9.25 (+5.22%)</td><td>8.39 (+1.16%)</td><td>0.54 <b>(+39.06%)</b></td><td>9.74 (+4.14%)</td><td>9.06 (+2.83%)</td><td>9.23 (+5.22%)</td><td>8.37 (+1.16%)</td><td>0.54 <b>(+39.06%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>9.37 (n/a)</td><td>8.83 (n/a)</td><td>8.79 (n/a)</td><td>8.30 (n/a)</td><td>0.39 (n/a)</td><td>9.35 (n/a)</td><td>8.81 (n/a)</td><td>8.78 (n/a)</td><td>8.28 (n/a)</td><td>0.39 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.09 (+3.71%)</td><td>0.92 (-1.04%)</td><td>0.87 (-8.83%)</td><td>0.84 (+13.02%)</td><td>0.11 <b>(-20.03%)</b></td><td>1.07 (+3.71%)</td><td>0.91 (-1.04%)</td><td>0.86 (-8.83%)</td><td>0.82 (+13.02%)</td><td>0.10 <b>(-20.03%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.05 (n/a)</td><td>0.93 (n/a)</td><td>0.96 (n/a)</td><td>0.74 (n/a)</td><td>0.13 (n/a)</td><td>1.04 (n/a)</td><td>0.92 (n/a)</td><td>0.94 (n/a)</td><td>0.73 (n/a)</td><td>0.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.28 (-4.94%)</td><td>1.22 (-3.05%)</td><td>1.27 (+1.80%)</td><td>1.10 (-8.12%)</td><td>0.08 <b>(+42.30%)</b></td><td>1.27 (-4.94%)</td><td>1.20 (-3.05%)</td><td>1.25 (+1.80%)</td><td>1.08 (-8.12%)</td><td>0.08 <b>(+42.30%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.35 (n/a)</td><td>1.26 (n/a)</td><td>1.24 (n/a)</td><td>1.19 (n/a)</td><td>0.06 (n/a)</td><td>1.33 (n/a)</td><td>1.24 (n/a)</td><td>1.23 (n/a)</td><td>1.18 (n/a)</td><td>0.06 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>19.27 (+7.41%)</td><td>18.24 (+5.39%)</td><td>18.23 (+4.81%)</td><td>17.57 (+7.55%)</td><td>0.69 (+8.99%)</td><td>19.05 (+7.41%)</td><td>18.03 (+5.39%)</td><td>18.02 (+4.81%)</td><td>17.37 (+7.55%)</td><td>0.68 (+8.99%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>17.94 (n/a)</td><td>17.31 (n/a)</td><td>17.39 (n/a)</td><td>16.34 (n/a)</td><td>0.63 (n/a)</td><td>17.73 (n/a)</td><td>17.11 (n/a)</td><td>17.19 (n/a)</td><td>16.15 (n/a)</td><td>0.62 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>14.52 (+1.50%)</td><td>14.10 (+3.23%)</td><td>14.02 (+3.22%)</td><td>13.85 (+4.98%)</td><td>0.25 <b>(-38.18%)</b></td><td>14.26 (+1.50%)</td><td>13.85 (+3.23%)</td><td>13.77 (+3.22%)</td><td>13.61 (+4.98%)</td><td>0.24 <b>(-38.18%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>14.30 (n/a)</td><td>13.66 (n/a)</td><td>13.58 (n/a)</td><td>13.20 (n/a)</td><td>0.40 (n/a)</td><td>14.05 (n/a)</td><td>13.42 (n/a)</td><td>13.34 (n/a)</td><td>12.96 (n/a)</td><td>0.40 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>10.60 (+17.13%)</td><td>8.16 (+0.84%)</td><td>7.46 (-5.45%)</td><td>7.15 (-0.15%)</td><td>1.43 <b>(+76.49%)</b></td><td>10.41 (+17.13%)</td><td>8.02 (+0.84%)</td><td>7.33 (-5.45%)</td><td>7.03 (-0.15%)</td><td>1.41 <b>(+76.49%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>9.05 (n/a)</td><td>8.10 (n/a)</td><td>7.89 (n/a)</td><td>7.16 (n/a)</td><td>0.81 (n/a)</td><td>8.89 (n/a)</td><td>7.96 (n/a)</td><td>7.75 (n/a)</td><td>7.04 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>6.66 (+1.83%)</td><td>5.36 (-9.46%)</td><td>5.18 (-12.71%)</td><td>4.46 (-11.13%)</td><td>0.82 <b>(+35.79%)</b></td><td>6.56 (+1.83%)</td><td>5.28 (-9.46%)</td><td>5.09 (-12.71%)</td><td>4.38 (-11.13%)</td><td>0.81 <b>(+35.79%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>6.54 (n/a)</td><td>5.92 (n/a)</td><td>5.93 (n/a)</td><td>5.01 (n/a)</td><td>0.60 (n/a)</td><td>6.44 (n/a)</td><td>5.83 (n/a)</td><td>5.84 (n/a)</td><td>4.93 (n/a)</td><td>0.59 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.30 (n/a)</td><td>12.62 (n/a)</td><td>13.05 (n/a)</td><td>11.01 (n/a)</td><td>0.94 (n/a)</td><td>13.30 (n/a)</td><td>12.61 (n/a)</td><td>13.04 (n/a)</td><td>11.00 (n/a)</td><td>0.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.01 (n/a)</td><td>12.28 (n/a)</td><td>12.55 (n/a)</td><td>11.02 (n/a)</td><td>0.80 (n/a)</td><td>13.00 (n/a)</td><td>12.27 (n/a)</td><td>12.54 (n/a)</td><td>11.01 (n/a)</td><td>0.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>157.80 (n/a)</td><td>148.34 (n/a)</td><td>154.10 (n/a)</td><td>132.00 (n/a)</td><td>10.67 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.40 (n/a)</td><td>161.68 (n/a)</td><td>157.70 (n/a)</td><td>140.30 (n/a)</td><td>26.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>209.70 (n/a)</td><td>183.96 (n/a)</td><td>180.30 (n/a)</td><td>171.70 (n/a)</td><td>14.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>225.00 (n/a)</td><td>163.90 (n/a)</td><td>158.40 (n/a)</td><td>129.00 (n/a)</td><td>38.14 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.70 (n/a)</td><td>150.86 (n/a)</td><td>139.20 (n/a)</td><td>135.40 (n/a)</td><td>24.90 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.00 (n/a)</td><td>162.70 (n/a)</td><td>171.00 (n/a)</td><td>126.20 (n/a)</td><td>22.47 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>198.80 (n/a)</td><td>176.20 (n/a)</td><td>172.10 (n/a)</td><td>157.20 (n/a)</td><td>15.51 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>371.00 (n/a)</td><td>243.86 (n/a)</td><td>215.00 (n/a)</td><td>177.70 (n/a)</td><td>75.58 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.80 (n/a)</td><td>145.86 (n/a)</td><td>134.80 (n/a)</td><td>122.20 (n/a)</td><td>32.48 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>347.90 (n/a)</td><td>191.50 (n/a)</td><td>168.70 (n/a)</td><td>123.30 (n/a)</td><td>91.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>191.30 (n/a)</td><td>179.86 (n/a)</td><td>184.70 (n/a)</td><td>156.90 (n/a)</td><td>13.78 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>283.00 (n/a)</td><td>182.96 (n/a)</td><td>166.70 (n/a)</td><td>126.70 (n/a)</td><td>59.14 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.10 (n/a)</td><td>170.14 (n/a)</td><td>178.50 (n/a)</td><td>123.50 (n/a)</td><td>26.48 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.30 (n/a)</td><td>181.10 (n/a)</td><td>165.70 (n/a)</td><td>161.60 (n/a)</td><td>28.28 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.20 (n/a)</td><td>187.14 (n/a)</td><td>187.60 (n/a)</td><td>146.10 (n/a)</td><td>40.98 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.90 (n/a)</td><td>203.14 (n/a)</td><td>185.70 (n/a)</td><td>177.40 (n/a)</td><td>32.02 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>172.90 (n/a)</td><td>159.98 (n/a)</td><td>165.60 (n/a)</td><td>137.80 (n/a)</td><td>13.93 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>168.20 (n/a)</td><td>144.58 (n/a)</td><td>146.80 (n/a)</td><td>121.60 (n/a)</td><td>19.56 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.40 (n/a)</td><td>162.64 (n/a)</td><td>151.40 (n/a)</td><td>124.70 (n/a)</td><td>32.43 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>172.34 (n/a)</td><td>168.00 (n/a)</td><td>152.70 (n/a)</td><td>23.36 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>214.50 (n/a)</td><td>162.78 (n/a)</td><td>148.60 (n/a)</td><td>126.70 (n/a)</td><td>34.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>206.70 (n/a)</td><td>173.08 (n/a)</td><td>173.00 (n/a)</td><td>144.40 (n/a)</td><td>27.72 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>271.40 (n/a)</td><td>194.16 (n/a)</td><td>165.90 (n/a)</td><td>133.60 (n/a)</td><td>60.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>333.80 (n/a)</td><td>218.46 (n/a)</td><td>191.70 (n/a)</td><td>162.00 (n/a)</td><td>70.87 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>193.50 (n/a)</td><td>179.96 (n/a)</td><td>177.10 (n/a)</td><td>165.40 (n/a)</td><td>12.32 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>215.30 (n/a)</td><td>183.80 (n/a)</td><td>176.20 (n/a)</td><td>145.50 (n/a)</td><td>28.52 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>270.10 (n/a)</td><td>203.32 (n/a)</td><td>195.50 (n/a)</td><td>171.00 (n/a)</td><td>38.84 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>280.20 (n/a)</td><td>191.68 (n/a)</td><td>180.50 (n/a)</td><td>146.00 (n/a)</td><td>54.85 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>221.50 (n/a)</td><td>171.48 (n/a)</td><td>159.90 (n/a)</td><td>146.60 (n/a)</td><td>31.11 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>281.80 (n/a)</td><td>203.18 (n/a)</td><td>187.70 (n/a)</td><td>163.00 (n/a)</td><td>45.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>317.10 (n/a)</td><td>218.50 (n/a)</td><td>196.00 (n/a)</td><td>183.90 (n/a)</td><td>55.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>221.80 (n/a)</td><td>204.26 (n/a)</td><td>206.60 (n/a)</td><td>173.90 (n/a)</td><td>19.92 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-1.05%)</td><td>0.03 (+1.12%)</td><td>0.03 (+2.82%)</td><td>0.02 (-3.29%)</td><td>0.00 (+0.56%)</td><td>189.60 (+3.44%)</td><td>161.40 (-1.04%)</td><td>159.30 (-2.75%)</td><td>139.70 (+1.09%)</td><td>20.11 (+3.70%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>183.30 (n/a)</td><td>163.10 (n/a)</td><td>163.80 (n/a)</td><td>138.20 (n/a)</td><td>19.40 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 <b>(-24.13%)</b></td><td>0.02 (-15.73%)</td><td>0.02 (-15.26%)</td><td>0.02 <b>(-23.18%)</b></td><td>0.01 <b>(-27.12%)</b></td><td>264.10 <b>(+30.23%)</b></td><td>189.56 (+18.28%)</td><td>192.70 (+18.00%)</td><td>140.10 <b>(+31.80%)</b></td><td>47.52 <b>(+28.52%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>202.80 (n/a)</td><td>160.26 (n/a)</td><td>163.30 (n/a)</td><td>106.30 (n/a)</td><td>36.98 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-16.49%)</td><td>0.02 (-18.77%)</td><td>0.02 <b>(-22.13%)</b></td><td>0.02 (-19.97%)</td><td>0.01 (-18.16%)</td><td>264.40 <b>(+24.95%)</b></td><td>198.44 <b>(+23.15%)</b></td><td>221.60 <b>(+28.39%)</b></td><td>135.30 (+19.73%)</td><td>55.79 <b>(+23.33%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>211.60 (n/a)</td><td>161.14 (n/a)</td><td>172.60 (n/a)</td><td>113.00 (n/a)</td><td>45.24 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (+4.21%)</td><td>0.02 (+3.52%)</td><td>0.02 (+4.95%)</td><td>0.02 (+17.82%)</td><td>0.00 <b>(-25.17%)</b></td><td>197.20 (-15.11%)</td><td>179.20 (-4.19%)</td><td>176.30 (-4.70%)</td><td>155.50 (-4.01%)</td><td>16.27 <b>(-40.14%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>232.30 (n/a)</td><td>187.04 (n/a)</td><td>185.00 (n/a)</td><td>162.00 (n/a)</td><td>27.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (+12.57%)</td><td>0.02 (-6.60%)</td><td>0.02 (-11.89%)</td><td>0.02 <b>(-22.67%)</b></td><td>0.01 <b>(+222.89%)</b></td><td>235.90 <b>(+29.33%)</b></td><td>185.08 (+11.88%)</td><td>184.20 (+13.49%)</td><td>135.00 (-11.18%)</td><td>44.64 <b>(+271.04%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>182.40 (n/a)</td><td>165.42 (n/a)</td><td>162.30 (n/a)</td><td>152.00 (n/a)</td><td>12.03 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (+1.74%)</td><td>0.02 (-7.46%)</td><td>0.02 (-17.67%)</td><td>0.02 (-0.33%)</td><td>0.00 (-4.78%)</td><td>212.30 (+0.33%)</td><td>192.24 (+7.92%)</td><td>200.30 <b>(+21.47%)</b></td><td>155.90 (-1.70%)</td><td>22.30 (-6.50%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.60 (n/a)</td><td>178.14 (n/a)</td><td>164.90 (n/a)</td><td>158.60 (n/a)</td><td>23.85 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (-3.95%)</td><td>0.02 (+3.18%)</td><td>0.02 (+4.63%)</td><td>0.02 <b>(+24.04%)</b></td><td>0.00 <b>(-33.14%)</b></td><td>241.10 (-19.39%)</td><td>202.62 (-5.94%)</td><td>210.20 (-4.45%)</td><td>166.60 (+4.12%)</td><td>30.62 <b>(-44.08%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>299.10 (n/a)</td><td>215.42 (n/a)</td><td>220.00 (n/a)</td><td>160.00 (n/a)</td><td>54.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-2.14%)</td><td>0.02 (-0.81%)</td><td>0.02 (-2.29%)</td><td>0.01 (-16.95%)</td><td>0.01 <b>(+41.95%)</b></td><td>324.10 <b>(+20.39%)</b></td><td>232.78 (+8.09%)</td><td>221.00 (+2.36%)</td><td>145.90 (+2.17%)</td><td>85.90 <b>(+85.97%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>269.20 (n/a)</td><td>215.36 (n/a)</td><td>215.90 (n/a)</td><td>142.80 (n/a)</td><td>46.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (-14.18%)</td><td>0.04 (-13.92%)</td><td>0.04 (-8.29%)</td><td>0.02 <b>(-38.95%)</b></td><td>0.01 <b>(+22.40%)</b></td><td>359.00 <b>(+63.78%)</b></td><td>232.56 <b>(+21.05%)</b></td><td>210.30 (+9.02%)</td><td>169.90 (+16.53%)</td><td>72.97 <b>(+153.78%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.20 (n/a)</td><td>192.12 (n/a)</td><td>192.90 (n/a)</td><td>145.80 (n/a)</td><td>28.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (-15.47%)</td><td>0.05 (-2.36%)</td><td>0.05 (+1.89%)</td><td>0.05 (+9.25%)</td><td>0.00 <b>(-56.13%)</b></td><td>177.70 (-8.50%)</td><td>162.92 (+0.20%)</td><td>160.20 (-1.90%)</td><td>145.90 (+18.33%)</td><td>13.91 <b>(-52.34%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>194.20 (n/a)</td><td>162.60 (n/a)</td><td>163.30 (n/a)</td><td>123.30 (n/a)</td><td>29.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.08 <b>(+56.01%)</b></td><td>0.05 (+16.13%)</td><td>0.05 (+4.71%)</td><td>0.04 (-6.79%)</td><td>0.02 <b>(+201.35%)</b></td><td>229.10 (+7.26%)</td><td>164.72 (-9.34%)</td><td>161.10 (-4.45%)</td><td>105.20 <b>(-35.89%)</b></td><td>44.35 <b>(+103.77%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.60 (n/a)</td><td>181.68 (n/a)</td><td>168.60 (n/a)</td><td>164.10 (n/a)</td><td>21.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (-12.22%)</td><td>0.05 (+3.26%)</td><td>0.05 (+15.56%)</td><td>0.04 <b>(+21.25%)</b></td><td>0.00 <b>(-60.42%)</b></td><td>191.60 (-17.56%)</td><td>172.20 (-6.98%)</td><td>170.80 (-13.48%)</td><td>148.50 (+13.88%)</td><td>15.84 <b>(-62.99%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>232.40 (n/a)</td><td>185.12 (n/a)</td><td>197.40 (n/a)</td><td>130.40 (n/a)</td><td>42.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (+4.25%)</td><td>0.04 (-13.13%)</td><td>0.05 (+7.76%)</td><td>0.02 <b>(-46.53%)</b></td><td>0.02 <b>(+218.23%)</b></td><td>383.40 <b>(+87.02%)</b></td><td>245.40 <b>(+35.72%)</b></td><td>168.40 (-7.22%)</td><td>148.90 (-4.12%)</td><td>118.88 <b>(+489.64%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>180.82 (n/a)</td><td>181.50 (n/a)</td><td>155.30 (n/a)</td><td>20.16 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (+0.27%)</td><td>0.04 (-6.75%)</td><td>0.04 (-5.56%)</td><td>0.04 (-7.83%)</td><td>0.01 <b>(+26.11%)</b></td><td>229.20 (+8.47%)</td><td>198.98 (+7.85%)</td><td>199.10 (+5.90%)</td><td>165.40 (-0.24%)</td><td>25.35 <b>(+37.93%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>211.30 (n/a)</td><td>184.50 (n/a)</td><td>188.00 (n/a)</td><td>165.80 (n/a)</td><td>18.38 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.08 <b>(+51.93%)</b></td><td>0.05 (+10.82%)</td><td>0.04 (-5.12%)</td><td>0.03 (+14.61%)</td><td>0.02 <b>(+112.01%)</b></td><td>237.90 (-12.73%)</td><td>183.10 (-5.54%)</td><td>184.50 (+5.37%)</td><td>107.90 <b>(-34.21%)</b></td><td>52.17 (+16.98%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>272.60 (n/a)</td><td>193.84 (n/a)</td><td>175.10 (n/a)</td><td>164.00 (n/a)</td><td>44.60 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (+4.35%)</td><td>0.05 (+8.24%)</td><td>0.05 <b>(+25.00%)</b></td><td>0.04 (+2.49%)</td><td>0.01 <b>(+21.73%)</b></td><td>202.90 (-2.45%)</td><td>171.84 (-7.13%)</td><td>157.80 <b>(-20.02%)</b></td><td>148.20 (-4.14%)</td><td>26.18 (+15.29%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>208.00 (n/a)</td><td>185.04 (n/a)</td><td>197.30 (n/a)</td><td>154.60 (n/a)</td><td>22.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 <b>(+25.64%)</b></td><td>0.05 (+5.11%)</td><td>0.04 (-14.56%)</td><td>0.04 (-6.06%)</td><td>0.01 <b>(+110.52%)</b></td><td>233.90 (+6.46%)</td><td>184.58 (-1.46%)</td><td>203.90 (+17.05%)</td><td>129.00 <b>(-20.42%)</b></td><td>43.36 <b>(+74.38%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.70 (n/a)</td><td>187.32 (n/a)</td><td>174.20 (n/a)</td><td>162.10 (n/a)</td><td>24.86 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 <b>(+29.62%)</b></td><td>0.04 (+6.78%)</td><td>0.04 (-5.60%)</td><td>0.04 (+4.75%)</td><td>0.01 <b>(+122.31%)</b></td><td>220.50 (-4.55%)</td><td>196.86 (-4.77%)</td><td>209.90 (+5.96%)</td><td>147.10 <b>(-22.86%)</b></td><td>30.86 <b>(+64.52%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>231.00 (n/a)</td><td>206.72 (n/a)</td><td>198.10 (n/a)</td><td>190.70 (n/a)</td><td>18.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (+8.09%)</td><td>0.10 (-12.48%)</td><td>0.10 (-11.15%)</td><td>0.04 <b>(-50.47%)</b></td><td>0.03 <b>(+115.44%)</b></td><td>370.90 <b>(+101.91%)</b></td><td>195.46 <b>(+30.66%)</b></td><td>162.70 (+12.60%)</td><td>119.10 (-7.46%)</td><td>100.97 <b>(+337.60%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>183.70 (n/a)</td><td>149.60 (n/a)</td><td>144.50 (n/a)</td><td>128.70 (n/a)</td><td>23.07 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (-7.73%)</td><td>0.11 (+1.22%)</td><td>0.10 (+11.64%)</td><td>0.09 (+13.31%)</td><td>0.01 <b>(-46.60%)</b></td><td>173.40 (-11.76%)</td><td>156.40 (-4.56%)</td><td>166.40 (-10.39%)</td><td>127.40 (+8.33%)</td><td>19.11 <b>(-49.37%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>196.50 (n/a)</td><td>163.88 (n/a)</td><td>185.70 (n/a)</td><td>117.60 (n/a)</td><td>37.75 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (+14.58%)</td><td>0.11 <b>(+28.31%)</b></td><td>0.11 <b>(+35.79%)</b></td><td>0.08 <b>(+21.13%)</b></td><td>0.02 (+16.68%)</td><td>204.80 (-17.45%)</td><td>151.74 <b>(-22.11%)</b></td><td>145.50 <b>(-26.37%)</b></td><td>125.50 (-12.79%)</td><td>32.57 (-15.94%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>248.10 (n/a)</td><td>194.82 (n/a)</td><td>197.60 (n/a)</td><td>143.90 (n/a)</td><td>38.75 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (-11.10%)</td><td>0.09 (-4.01%)</td><td>0.09 (+5.75%)</td><td>0.07 (-0.80%)</td><td>0.02 <b>(-35.99%)</b></td><td>249.30 (+0.81%)</td><td>185.10 (+1.47%)</td><td>176.80 (-5.40%)</td><td>152.40 (+12.47%)</td><td>37.62 <b>(-20.79%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>247.30 (n/a)</td><td>182.42 (n/a)</td><td>186.90 (n/a)</td><td>135.50 (n/a)</td><td>47.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (+12.16%)</td><td>0.10 (+6.76%)</td><td>0.11 (+2.78%)</td><td>0.08 (-2.79%)</td><td>0.02 <b>(+37.08%)</b></td><td>218.40 (+2.87%)</td><td>165.90 (-5.06%)</td><td>153.70 (-2.72%)</td><td>133.10 (-10.85%)</td><td>35.32 <b>(+25.17%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>212.30 (n/a)</td><td>174.74 (n/a)</td><td>158.00 (n/a)</td><td>149.30 (n/a)</td><td>28.22 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (+4.78%)</td><td>0.09 (-5.40%)</td><td>0.09 (-9.50%)</td><td>0.07 (-7.03%)</td><td>0.02 (+13.52%)</td><td>227.10 (+7.58%)</td><td>181.04 (+6.68%)</td><td>174.80 (+10.49%)</td><td>131.40 (-4.58%)</td><td>38.56 (+17.27%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>211.10 (n/a)</td><td>169.70 (n/a)</td><td>158.20 (n/a)</td><td>137.70 (n/a)</td><td>32.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 <b>(-33.14%)</b></td><td>0.09 (-6.33%)</td><td>0.09 (+6.48%)</td><td>0.09 (+13.97%)</td><td>0.01 <b>(-75.42%)</b></td><td>187.40 (-12.27%)</td><td>175.98 (-0.33%)</td><td>180.00 (-6.10%)</td><td>150.00 <b>(+49.55%)</b></td><td>14.89 <b>(-66.80%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>213.60 (n/a)</td><td>176.56 (n/a)</td><td>191.70 (n/a)</td><td>100.30 (n/a)</td><td>44.86 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.08 (+3.01%)</td><td>0.07 (+4.80%)</td><td>0.08 (-2.57%)</td><td>0.06 (+18.85%)</td><td>0.01 <b>(-38.75%)</b></td><td>270.60 (-15.86%)</td><td>223.98 (-6.91%)</td><td>215.90 (+2.66%)</td><td>193.80 (-2.95%)</td><td>28.38 <b>(-47.57%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>321.60 (n/a)</td><td>240.60 (n/a)</td><td>210.30 (n/a)</td><td>199.70 (n/a)</td><td>54.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (+6.44%)</td><td>0.21 (+13.69%)</td><td>0.20 (+17.59%)</td><td>0.19 <b>(+31.06%)</b></td><td>0.02 <b>(-45.88%)</b></td><td>176.00 <b>(-23.68%)</b></td><td>157.42 (-14.40%)</td><td>162.30 (-14.98%)</td><td>136.20 (-6.07%)</td><td>15.21 <b>(-59.79%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>230.60 (n/a)</td><td>183.90 (n/a)</td><td>190.90 (n/a)</td><td>145.00 (n/a)</td><td>37.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (-2.64%)</td><td>0.21 (-1.10%)</td><td>0.20 (-8.03%)</td><td>0.17 (+12.69%)</td><td>0.03 <b>(-25.43%)</b></td><td>187.70 (-11.25%)</td><td>158.54 (-0.39%)</td><td>163.10 (+8.73%)</td><td>131.30 (+2.74%)</td><td>21.61 <b>(-33.67%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>211.50 (n/a)</td><td>159.16 (n/a)</td><td>150.00 (n/a)</td><td>127.80 (n/a)</td><td>32.57 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (-11.15%)</td><td>0.21 (+4.39%)</td><td>0.22 (+8.22%)</td><td>0.17 (+9.61%)</td><td>0.03 <b>(-35.92%)</b></td><td>192.70 (-8.76%)</td><td>160.50 (-6.48%)</td><td>151.60 (-7.56%)</td><td>133.10 (+12.61%)</td><td>24.68 <b>(-33.91%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>211.20 (n/a)</td><td>171.62 (n/a)</td><td>164.00 (n/a)</td><td>118.20 (n/a)</td><td>37.34 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.27 <b>(+26.12%)</b></td><td>0.22 (+16.86%)</td><td>0.23 (+13.95%)</td><td>0.17 (+19.75%)</td><td>0.04 <b>(+21.36%)</b></td><td>196.70 (-16.51%)</td><td>149.70 (-14.48%)</td><td>141.50 (-12.28%)</td><td>122.30 <b>(-20.69%)</b></td><td>27.92 (-18.42%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>235.60 (n/a)</td><td>175.04 (n/a)</td><td>161.30 (n/a)</td><td>154.20 (n/a)</td><td>34.22 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.21 (-18.35%)</td><td>0.19 (-6.77%)</td><td>0.20 (-6.61%)</td><td>0.15 (-2.69%)</td><td>0.02 <b>(-41.35%)</b></td><td>216.40 (+2.75%)</td><td>176.16 (+5.21%)</td><td>164.40 (+7.10%)</td><td>155.10 <b>(+22.51%)</b></td><td>25.07 <b>(-27.43%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>210.60 (n/a)</td><td>167.44 (n/a)</td><td>153.50 (n/a)</td><td>126.60 (n/a)</td><td>34.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (-3.19%)</td><td>0.18 (-7.00%)</td><td>0.17 (-9.05%)</td><td>0.15 (+4.21%)</td><td>0.04 (-8.20%)</td><td>214.50 (-4.03%)</td><td>185.82 (+6.85%)</td><td>193.50 (+9.94%)</td><td>132.40 (+3.28%)</td><td>31.23 (-12.22%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>223.50 (n/a)</td><td>173.90 (n/a)</td><td>176.00 (n/a)</td><td>128.20 (n/a)</td><td>35.58 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (+13.21%)</td><td>0.17 (+6.66%)</td><td>0.18 (+10.13%)</td><td>0.15 (+6.30%)</td><td>0.02 <b>(+75.25%)</b></td><td>219.40 (-5.92%)</td><td>196.90 (-5.76%)</td><td>186.10 (-9.18%)</td><td>176.20 (-11.68%)</td><td>20.23 <b>(+46.77%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.01 (n/a)</td><td>233.20 (n/a)</td><td>208.94 (n/a)</td><td>204.90 (n/a)</td><td>199.50 (n/a)</td><td>13.78 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (+15.52%)</td><td>0.03 (+19.10%)</td><td>0.03 (+19.06%)</td><td>0.03 <b>(+43.78%)</b></td><td>0.00 <b>(-21.95%)</b></td><td>154.60 <b>(-30.45%)</b></td><td>136.36 (-17.53%)</td><td>134.10 (-15.98%)</td><td>116.70 (-13.43%)</td><td>15.26 <b>(-54.48%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>222.30 (n/a)</td><td>165.34 (n/a)</td><td>159.60 (n/a)</td><td>134.80 (n/a)</td><td>33.52 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (+12.28%)</td><td>0.03 <b>(+26.41%)</b></td><td>0.03 <b>(+33.91%)</b></td><td>0.03 <b>(+36.81%)</b></td><td>0.00 <b>(-34.84%)</b></td><td>142.20 <b>(-26.89%)</b></td><td>126.20 <b>(-21.87%)</b></td><td>121.60 <b>(-25.31%)</b></td><td>118.50 (-10.90%)</td><td>10.15 <b>(-57.66%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.50 (n/a)</td><td>161.52 (n/a)</td><td>162.80 (n/a)</td><td>133.00 (n/a)</td><td>23.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.00 (+0.01%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(+91.58%)</b></td><td>4746168.60 (-0.00%)</td><td>4745970.50 (-0.00%)</td><td>4746086.40 (-0.00%)</td><td>4745656.50 (-0.01%)</td><td>275.02 <b>(+91.69%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4746206.10 (n/a)</td><td>4746104.65 (n/a)</td><td>4746104.65 (n/a)</td><td>4746003.20 (n/a)</td><td>143.47 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (+8.79%)</td><td>0.02 (-1.02%)</td><td>0.02 (-3.99%)</td><td>0.02 (-12.68%)</td><td>0.00 <b>(+65.74%)</b></td><td>234.30 (+14.52%)</td><td>191.30 (+2.27%)</td><td>195.20 (+4.16%)</td><td>154.20 (-8.10%)</td><td>29.55 <b>(+73.28%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>204.60 (n/a)</td><td>187.06 (n/a)</td><td>187.40 (n/a)</td><td>167.80 (n/a)</td><td>17.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 <b>(+37.56%)</b></td><td>0.03 (+16.67%)</td><td>0.03 (+11.95%)</td><td>0.02 (+15.69%)</td><td>0.01 <b>(+116.79%)</b></td><td>170.60 (-13.58%)</td><td>148.48 (-12.78%)</td><td>150.60 (-10.73%)</td><td>107.10 <b>(-27.29%)</b></td><td>24.72 <b>(+31.61%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>197.40 (n/a)</td><td>170.24 (n/a)</td><td>168.70 (n/a)</td><td>147.30 (n/a)</td><td>18.78 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 <b>(+20.19%)</b></td><td>0.03 (+12.34%)</td><td>0.03 (+16.17%)</td><td>0.02 (-1.34%)</td><td>0.01 <b>(+95.41%)</b></td><td>179.70 (+1.35%)</td><td>142.68 (-9.35%)</td><td>137.90 (-13.92%)</td><td>115.30 (-16.81%)</td><td>26.45 <b>(+65.45%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.30 (n/a)</td><td>157.40 (n/a)</td><td>160.20 (n/a)</td><td>138.60 (n/a)</td><td>15.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (+2.05%)</td><td>0.03 (+10.99%)</td><td>0.03 (+10.53%)</td><td>0.03 <b>(+71.25%)</b></td><td>0.00 <b>(-54.32%)</b></td><td>160.10 <b>(-41.61%)</b></td><td>145.40 (-16.27%)</td><td>151.10 (-9.52%)</td><td>119.30 (-1.97%)</td><td>15.73 <b>(-74.29%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>274.20 (n/a)</td><td>173.66 (n/a)</td><td>167.00 (n/a)</td><td>121.70 (n/a)</td><td>61.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (+6.37%)</td><td>0.03 (+11.83%)</td><td>0.03 (+14.96%)</td><td>0.02 (+16.90%)</td><td>0.00 (-4.27%)</td><td>171.40 (-14.47%)</td><td>143.92 (-11.18%)</td><td>148.50 (-13.01%)</td><td>120.90 (-5.99%)</td><td>22.05 <b>(-23.97%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.40 (n/a)</td><td>162.04 (n/a)</td><td>170.70 (n/a)</td><td>128.60 (n/a)</td><td>29.01 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (+14.84%)</td><td>0.03 (+19.17%)</td><td>0.03 <b>(+20.73%)</b></td><td>0.02 (+5.39%)</td><td>0.00 <b>(+27.95%)</b></td><td>186.30 (-5.14%)</td><td>146.74 (-15.61%)</td><td>149.20 (-17.16%)</td><td>119.60 (-12.95%)</td><td>25.68 (+5.75%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>196.40 (n/a)</td><td>173.88 (n/a)</td><td>180.10 (n/a)</td><td>137.40 (n/a)</td><td>24.29 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-17.56%)</td><td>0.03 (+4.82%)</td><td>0.03 (+9.17%)</td><td>0.02 (+11.80%)</td><td>0.00 <b>(-42.38%)</b></td><td>194.10 (-10.55%)</td><td>148.28 (-8.90%)</td><td>135.20 (-8.40%)</td><td>126.50 <b>(+21.40%)</b></td><td>28.40 <b>(-40.07%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>217.00 (n/a)</td><td>162.76 (n/a)</td><td>147.60 (n/a)</td><td>104.20 (n/a)</td><td>47.39 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (+9.80%)</td><td>0.03 (+19.03%)</td><td>0.03 (+14.70%)</td><td>0.03 <b>(+53.61%)</b></td><td>0.00 <b>(-36.69%)</b></td><td>149.40 <b>(-34.87%)</b></td><td>140.26 (-18.72%)</td><td>147.30 (-12.79%)</td><td>113.70 (-8.89%)</td><td>15.03 <b>(-62.88%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.40 (n/a)</td><td>172.56 (n/a)</td><td>168.90 (n/a)</td><td>124.80 (n/a)</td><td>40.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (+12.51%)</td><td>0.03 (-1.91%)</td><td>0.02 (-5.49%)</td><td>0.01 <b>(-20.84%)</b></td><td>0.01 <b>(+50.42%)</b></td><td>295.60 <b>(+26.32%)</b></td><td>179.94 (+9.15%)</td><td>174.00 (+5.84%)</td><td>108.90 (-11.17%)</td><td>72.83 <b>(+68.08%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>234.00 (n/a)</td><td>164.86 (n/a)</td><td>164.40 (n/a)</td><td>122.60 (n/a)</td><td>43.33 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (+6.04%)</td><td>0.03 (+12.07%)</td><td>0.03 (+11.75%)</td><td>0.02 <b>(+47.49%)</b></td><td>0.00 <b>(-21.74%)</b></td><td>199.70 <b>(-32.19%)</b></td><td>161.70 (-14.60%)</td><td>156.80 (-10.50%)</td><td>121.80 (-5.73%)</td><td>29.29 <b>(-52.84%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>294.50 (n/a)</td><td>189.34 (n/a)</td><td>175.20 (n/a)</td><td>129.20 (n/a)</td><td>62.11 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (-4.45%)</td><td>0.02 (+2.38%)</td><td>0.02 (-4.30%)</td><td>0.02 (+18.51%)</td><td>0.00 <b>(-51.94%)</b></td><td>206.40 (-15.62%)</td><td>179.40 (-4.65%)</td><td>170.10 (+4.48%)</td><td>166.80 (+4.64%)</td><td>16.69 <b>(-56.60%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>244.60 (n/a)</td><td>188.14 (n/a)</td><td>162.80 (n/a)</td><td>159.40 (n/a)</td><td>38.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 <b>(-31.25%)</b></td><td>0.02 (-16.79%)</td><td>0.02 (-14.37%)</td><td>0.02 (-8.57%)</td><td>0.00 <b>(-53.08%)</b></td><td>241.20 (+9.39%)</td><td>197.26 (+16.01%)</td><td>197.50 (+16.79%)</td><td>160.60 <b>(+45.47%)</b></td><td>31.75 <b>(-24.30%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>220.50 (n/a)</td><td>170.04 (n/a)</td><td>169.10 (n/a)</td><td>110.40 (n/a)</td><td>41.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-18.62%)</td><td>0.02 <b>(-26.21%)</b></td><td>0.02 <b>(-33.10%)</b></td><td>0.02 <b>(-22.66%)</b></td><td>0.00 (+6.98%)</td><td>234.20 <b>(+29.25%)</b></td><td>206.28 <b>(+36.95%)</b></td><td>225.40 <b>(+49.47%)</b></td><td>156.90 <b>(+22.87%)</b></td><td>33.41 <b>(+69.61%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>181.20 (n/a)</td><td>150.62 (n/a)</td><td>150.80 (n/a)</td><td>127.70 (n/a)</td><td>19.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (+15.85%)</td><td>0.05 (+5.64%)</td><td>0.05 (+1.04%)</td><td>0.04 <b>(+65.26%)</b></td><td>0.01 (-12.52%)</td><td>211.60 <b>(-39.47%)</b></td><td>163.26 (-12.57%)</td><td>156.70 (-1.01%)</td><td>110.10 (-13.65%)</td><td>39.68 <b>(-56.97%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>349.60 (n/a)</td><td>186.74 (n/a)</td><td>158.30 (n/a)</td><td>127.50 (n/a)</td><td>92.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 <b>(+20.90%)</b></td><td>0.06 <b>(+30.43%)</b></td><td>0.06 <b>(+46.31%)</b></td><td>0.05 <b>(+27.00%)</b></td><td>0.01 (+6.62%)</td><td>176.50 <b>(-21.28%)</b></td><td>145.02 <b>(-23.74%)</b></td><td>137.10 <b>(-31.66%)</b></td><td>121.90 (-17.24%)</td><td>21.32 <b>(-29.10%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>190.16 (n/a)</td><td>200.60 (n/a)</td><td>147.30 (n/a)</td><td>30.06 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 <b>(+43.04%)</b></td><td>0.04 (-0.89%)</td><td>0.04 (-14.96%)</td><td>0.02 (-16.35%)</td><td>0.02 <b>(+119.91%)</b></td><td>334.80 (+19.53%)</td><td>219.88 (+9.96%)</td><td>209.70 (+17.61%)</td><td>118.60 <b>(-30.07%)</b></td><td>81.21 <b>(+76.81%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>280.10 (n/a)</td><td>199.96 (n/a)</td><td>178.30 (n/a)</td><td>169.60 (n/a)</td><td>45.93 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (-15.59%)</td><td>0.04 (-15.94%)</td><td>0.05 (-12.78%)</td><td>0.03 <b>(-29.03%)</b></td><td>0.01 (+19.60%)</td><td>277.30 <b>(+40.90%)</b></td><td>200.48 <b>(+21.11%)</b></td><td>177.90 (+14.63%)</td><td>174.90 (+18.50%)</td><td>43.70 <b>(+103.79%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>196.80 (n/a)</td><td>165.54 (n/a)</td><td>155.20 (n/a)</td><td>147.60 (n/a)</td><td>21.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (-16.95%)</td><td>0.05 (+5.94%)</td><td>0.05 (+13.19%)</td><td>0.04 <b>(+30.33%)</b></td><td>0.01 <b>(-59.41%)</b></td><td>191.40 <b>(-23.29%)</b></td><td>165.38 (-10.15%)</td><td>159.20 (-11.70%)</td><td>143.70 <b>(+20.45%)</b></td><td>18.41 <b>(-61.50%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>249.50 (n/a)</td><td>184.06 (n/a)</td><td>180.30 (n/a)</td><td>119.30 (n/a)</td><td>47.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (+1.87%)</td><td>0.05 (+1.52%)</td><td>0.05 (+9.45%)</td><td>0.04 (-8.35%)</td><td>0.01 (+12.37%)</td><td>200.90 (+9.13%)</td><td>163.74 (-0.99%)</td><td>161.50 (-8.65%)</td><td>131.30 (-1.87%)</td><td>26.41 (+19.31%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>165.38 (n/a)</td><td>176.80 (n/a)</td><td>133.80 (n/a)</td><td>22.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (-13.08%)</td><td>0.05 (-10.38%)</td><td>0.05 (-11.89%)</td><td>0.04 (-9.42%)</td><td>0.01 (-17.00%)</td><td>202.50 (+10.41%)</td><td>170.56 (+11.33%)</td><td>173.40 (+13.56%)</td><td>136.40 (+15.01%)</td><td>25.26 (+6.62%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.40 (n/a)</td><td>153.20 (n/a)</td><td>152.70 (n/a)</td><td>118.60 (n/a)</td><td>23.69 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (+13.88%)</td><td>0.05 (-1.06%)</td><td>0.05 (+7.79%)</td><td>0.04 (-18.66%)</td><td>0.01 <b>(+148.58%)</b></td><td>228.40 <b>(+22.93%)</b></td><td>172.16 (+4.87%)</td><td>151.50 (-7.23%)</td><td>130.30 (-12.20%)</td><td>41.10 <b>(+173.80%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>185.80 (n/a)</td><td>164.16 (n/a)</td><td>163.30 (n/a)</td><td>148.40 (n/a)</td><td>15.01 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (-8.31%)</td><td>0.05 (-16.31%)</td><td>0.05 (-8.98%)</td><td>0.03 <b>(-25.45%)</b></td><td>0.01 (+6.76%)</td><td>297.90 <b>(+34.13%)</b></td><td>190.70 <b>(+23.03%)</b></td><td>164.60 (+9.88%)</td><td>135.90 (+9.07%)</td><td>63.72 <b>(+61.13%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.10 (n/a)</td><td>155.00 (n/a)</td><td>149.80 (n/a)</td><td>124.60 (n/a)</td><td>39.54 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (-7.72%)</td><td>0.05 (-4.90%)</td><td>0.05 (+1.26%)</td><td>0.03 (-5.64%)</td><td>0.01 (-7.32%)</td><td>237.10 (+5.99%)</td><td>183.60 (+5.14%)</td><td>165.90 (-1.25%)</td><td>138.30 (+8.39%)</td><td>46.71 (+7.42%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>174.62 (n/a)</td><td>168.00 (n/a)</td><td>127.60 (n/a)</td><td>43.48 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (-15.33%)</td><td>0.05 (-11.38%)</td><td>0.05 (-11.53%)</td><td>0.04 (-4.07%)</td><td>0.01 <b>(-26.05%)</b></td><td>231.70 (+4.23%)</td><td>163.48 (+10.68%)</td><td>156.80 (+13.05%)</td><td>129.10 (+18.12%)</td><td>40.73 (-9.09%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>222.30 (n/a)</td><td>147.70 (n/a)</td><td>138.70 (n/a)</td><td>109.30 (n/a)</td><td>44.80 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (+13.18%)</td><td>0.05 (+5.48%)</td><td>0.05 (+0.74%)</td><td>0.04 (-2.83%)</td><td>0.02 <b>(+25.05%)</b></td><td>223.50 (+2.95%)</td><td>165.08 (-3.53%)</td><td>167.80 (-0.77%)</td><td>110.60 (-11.66%)</td><td>45.80 (+11.72%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>217.10 (n/a)</td><td>171.12 (n/a)</td><td>169.10 (n/a)</td><td>125.20 (n/a)</td><td>40.99 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (+9.41%)</td><td>0.05 (-1.44%)</td><td>0.05 (+1.51%)</td><td>0.03 (-5.90%)</td><td>0.02 <b>(+33.04%)</b></td><td>308.40 (+6.23%)</td><td>186.60 (+5.94%)</td><td>152.30 (-1.49%)</td><td>122.40 (-8.59%)</td><td>78.38 <b>(+21.13%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>290.30 (n/a)</td><td>176.14 (n/a)</td><td>154.60 (n/a)</td><td>133.90 (n/a)</td><td>64.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 <b>(+28.42%)</b></td><td>0.05 <b>(+22.44%)</b></td><td>0.06 (+14.83%)</td><td>0.04 <b>(+27.49%)</b></td><td>0.01 <b>(+25.75%)</b></td><td>204.30 <b>(-21.54%)</b></td><td>159.12 (-18.27%)</td><td>140.60 (-12.94%)</td><td>121.00 <b>(-22.14%)</b></td><td>40.01 (-19.29%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>260.40 (n/a)</td><td>194.70 (n/a)</td><td>161.50 (n/a)</td><td>155.40 (n/a)</td><td>49.57 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (-11.92%)</td><td>0.05 (-9.45%)</td><td>0.04 (-10.53%)</td><td>0.04 (-10.05%)</td><td>0.01 (-5.27%)</td><td>204.10 (+11.17%)</td><td>181.14 (+10.57%)</td><td>188.80 (+11.72%)</td><td>155.90 (+13.46%)</td><td>22.41 (+18.25%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>183.60 (n/a)</td><td>163.82 (n/a)</td><td>169.00 (n/a)</td><td>137.40 (n/a)</td><td>18.96 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (+17.75%)</td><td>0.05 (-7.77%)</td><td>0.05 (-6.33%)</td><td>0.03 <b>(-27.59%)</b></td><td>0.01 <b>(+174.53%)</b></td><td>239.20 <b>(+38.11%)</b></td><td>174.26 (+14.39%)</td><td>161.30 (+6.75%)</td><td>114.60 (-15.05%)</td><td>47.01 <b>(+220.55%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.20 (n/a)</td><td>152.34 (n/a)</td><td>151.10 (n/a)</td><td>134.90 (n/a)</td><td>14.67 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (-5.67%)</td><td>0.10 <b>(-21.20%)</b></td><td>0.08 <b>(-32.03%)</b></td><td>0.07 <b>(-35.57%)</b></td><td>0.03 <b>(+117.64%)</b></td><td>223.60 <b>(+55.28%)</b></td><td>172.62 <b>(+34.57%)</b></td><td>194.20 <b>(+47.12%)</b></td><td>117.90 (+6.03%)</td><td>47.44 <b>(+250.61%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>144.00 (n/a)</td><td>128.28 (n/a)</td><td>132.00 (n/a)</td><td>111.20 (n/a)</td><td>13.53 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (-15.91%)</td><td>0.10 (-16.38%)</td><td>0.10 <b>(-21.13%)</b></td><td>0.07 <b>(-30.48%)</b></td><td>0.02 (+9.33%)</td><td>230.90 <b>(+43.86%)</b></td><td>166.98 <b>(+22.01%)</b></td><td>165.60 <b>(+26.80%)</b></td><td>130.50 (+18.96%)</td><td>40.33 <b>(+78.49%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>160.50 (n/a)</td><td>136.86 (n/a)</td><td>130.60 (n/a)</td><td>109.70 (n/a)</td><td>22.60 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.09 (-16.86%)</td><td>0.08 (-14.76%)</td><td>0.07 (-11.94%)</td><td>0.05 <b>(-29.69%)</b></td><td>0.02 (+3.65%)</td><td>301.80 <b>(+42.22%)</b></td><td>225.04 (+19.19%)</td><td>224.80 (+13.54%)</td><td>174.10 <b>(+20.23%)</b></td><td>48.88 <b>(+81.74%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>212.20 (n/a)</td><td>188.80 (n/a)</td><td>198.00 (n/a)</td><td>144.80 (n/a)</td><td>26.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (+8.35%)</td><td>0.09 (+5.29%)</td><td>0.09 (-0.90%)</td><td>0.07 (-5.46%)</td><td>0.02 (+18.76%)</td><td>237.00 (+5.80%)</td><td>179.40 (-4.14%)</td><td>180.70 (+0.89%)</td><td>130.20 (-7.66%)</td><td>39.11 (+12.70%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.00 (n/a)</td><td>187.14 (n/a)</td><td>179.10 (n/a)</td><td>141.00 (n/a)</td><td>34.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (-6.61%)</td><td>0.12 (+10.40%)</td><td>0.13 (+10.56%)</td><td>0.09 <b>(+66.30%)</b></td><td>0.02 <b>(-48.60%)</b></td><td>178.00 <b>(-39.86%)</b></td><td>138.50 (-17.38%)</td><td>127.40 (-9.58%)</td><td>121.80 (+7.12%)</td><td>23.17 <b>(-68.53%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>296.00 (n/a)</td><td>167.64 (n/a)</td><td>140.90 (n/a)</td><td>113.70 (n/a)</td><td>73.64 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (+13.49%)</td><td>0.10 (+0.25%)</td><td>0.10 (-4.84%)</td><td>0.09 (-4.78%)</td><td>0.02 <b>(+78.19%)</b></td><td>179.70 (+5.03%)</td><td>160.42 (+1.28%)</td><td>171.00 (+5.04%)</td><td>117.80 (-11.83%)</td><td>24.61 <b>(+60.32%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>171.10 (n/a)</td><td>158.40 (n/a)</td><td>162.80 (n/a)</td><td>133.60 (n/a)</td><td>15.35 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (-14.45%)</td><td>0.09 (-18.36%)</td><td>0.09 (-15.07%)</td><td>0.07 <b>(-31.13%)</b></td><td>0.01 <b>(+65.31%)</b></td><td>231.40 <b>(+45.17%)</b></td><td>186.06 <b>(+24.32%)</b></td><td>181.10 (+17.75%)</td><td>155.00 (+16.89%)</td><td>29.55 <b>(+186.06%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>159.40 (n/a)</td><td>149.66 (n/a)</td><td>153.80 (n/a)</td><td>132.60 (n/a)</td><td>10.33 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (-19.60%)</td><td>0.09 (-18.12%)</td><td>0.09 (-10.28%)</td><td>0.04 <b>(-47.61%)</b></td><td>0.03 <b>(+24.17%)</b></td><td>364.60 <b>(+90.89%)</b></td><td>208.04 <b>(+31.95%)</b></td><td>178.40 (+11.43%)</td><td>144.60 <b>(+24.44%)</b></td><td>89.28 <b>(+222.55%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>191.00 (n/a)</td><td>157.66 (n/a)</td><td>160.10 (n/a)</td><td>116.20 (n/a)</td><td>27.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (-2.77%)</td><td>0.09 <b>(-24.56%)</b></td><td>0.08 <b>(-28.77%)</b></td><td>0.04 <b>(-54.78%)</b></td><td>0.03 <b>(+116.98%)</b></td><td>376.60 <b>(+121.14%)</b></td><td>213.66 <b>(+48.25%)</b></td><td>195.20 <b>(+40.43%)</b></td><td>131.70 (+2.89%)</td><td>95.47 <b>(+427.81%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>170.30 (n/a)</td><td>144.12 (n/a)</td><td>139.00 (n/a)</td><td>128.00 (n/a)</td><td>18.09 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (-16.76%)</td><td>0.10 (-11.17%)</td><td>0.10 (-8.41%)</td><td>0.08 (-0.81%)</td><td>0.01 <b>(-51.87%)</b></td><td>198.10 (+0.81%)</td><td>169.42 (+9.32%)</td><td>168.90 (+9.18%)</td><td>141.40 <b>(+20.14%)</b></td><td>20.43 <b>(-41.26%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>196.50 (n/a)</td><td>154.98 (n/a)</td><td>154.70 (n/a)</td><td>117.70 (n/a)</td><td>34.78 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.16 (+16.16%)</td><td>0.10 (-7.54%)</td><td>0.09 (-11.17%)</td><td>0.06 <b>(-30.85%)</b></td><td>0.04 <b>(+80.06%)</b></td><td>296.00 <b>(+44.60%)</b></td><td>187.50 (+18.19%)</td><td>179.80 (+12.59%)</td><td>101.70 (-13.96%)</td><td>72.05 <b>(+122.78%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.70 (n/a)</td><td>158.64 (n/a)</td><td>159.70 (n/a)</td><td>118.20 (n/a)</td><td>32.34 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 <b>(+22.42%)</b></td><td>0.11 (+14.48%)</td><td>0.12 <b>(+28.79%)</b></td><td>0.08 (-9.87%)</td><td>0.02 <b>(+140.34%)</b></td><td>199.00 (+10.93%)</td><td>151.18 (-9.88%)</td><td>135.40 <b>(-22.36%)</b></td><td>116.10 (-18.30%)</td><td>34.14 <b>(+121.99%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>179.40 (n/a)</td><td>167.76 (n/a)</td><td>174.40 (n/a)</td><td>142.10 (n/a)</td><td>15.38 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (+19.63%)</td><td>0.10 (+10.78%)</td><td>0.11 <b>(+22.26%)</b></td><td>0.07 <b>(-20.75%)</b></td><td>0.03 <b>(+205.59%)</b></td><td>246.20 <b>(+26.19%)</b></td><td>174.08 (-4.80%)</td><td>156.00 (-18.20%)</td><td>132.40 (-16.41%)</td><td>49.62 <b>(+210.55%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>195.10 (n/a)</td><td>182.86 (n/a)</td><td>190.70 (n/a)</td><td>158.40 (n/a)</td><td>15.98 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (-5.25%)</td><td>0.10 (-0.74%)</td><td>0.10 (-6.20%)</td><td>0.08 (+4.20%)</td><td>0.02 <b>(-28.85%)</b></td><td>196.60 (-4.00%)</td><td>159.82 (-0.95%)</td><td>157.40 (+6.57%)</td><td>129.30 (+5.55%)</td><td>23.98 <b>(-28.82%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>204.80 (n/a)</td><td>161.36 (n/a)</td><td>147.70 (n/a)</td><td>122.50 (n/a)</td><td>33.69 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (-12.19%)</td><td>0.10 (+2.12%)</td><td>0.10 (+16.13%)</td><td>0.09 (+4.03%)</td><td>0.01 <b>(-54.29%)</b></td><td>186.10 (-3.87%)</td><td>166.16 (-3.29%)</td><td>159.70 (-13.91%)</td><td>158.80 (+13.84%)</td><td>11.68 <b>(-50.06%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>193.60 (n/a)</td><td>171.82 (n/a)</td><td>185.50 (n/a)</td><td>139.50 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (-13.35%)</td><td>0.09 (-5.20%)</td><td>0.09 (-7.59%)</td><td>0.08 (+11.05%)</td><td>0.01 <b>(-51.42%)</b></td><td>198.00 (-9.96%)</td><td>175.76 (+2.72%)</td><td>174.70 (+8.17%)</td><td>154.30 (+15.41%)</td><td>18.40 <b>(-49.56%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>219.90 (n/a)</td><td>171.10 (n/a)</td><td>161.50 (n/a)</td><td>133.70 (n/a)</td><td>36.47 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (-1.62%)</td><td>0.21 (-7.26%)</td><td>0.23 (-6.35%)</td><td>0.16 (-13.47%)</td><td>0.04 (+10.46%)</td><td>209.80 (+15.59%)</td><td>157.98 (+8.83%)</td><td>145.50 (+6.75%)</td><td>127.40 (+1.68%)</td><td>31.83 <b>(+34.32%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>181.50 (n/a)</td><td>145.16 (n/a)</td><td>136.30 (n/a)</td><td>125.30 (n/a)</td><td>23.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.27 (-5.47%)</td><td>0.21 (+3.68%)</td><td>0.20 (+7.34%)</td><td>0.13 (-14.56%)</td><td>0.05 (-0.60%)</td><td>256.20 (+17.04%)</td><td>170.10 (-2.40%)</td><td>165.60 (-6.86%)</td><td>122.80 (+5.77%)</td><td>52.04 <b>(+25.82%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>218.90 (n/a)</td><td>174.28 (n/a)</td><td>177.80 (n/a)</td><td>116.10 (n/a)</td><td>41.36 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 (+12.19%)</td><td>0.17 (+11.80%)</td><td>0.17 (+12.98%)</td><td>0.14 (+8.67%)</td><td>0.02 <b>(+27.05%)</b></td><td>232.40 (-7.96%)</td><td>194.72 (-10.34%)</td><td>188.40 (-11.47%)</td><td>175.30 (-10.83%)</td><td>21.88 (+4.67%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.01 (n/a)</td><td>252.50 (n/a)</td><td>217.18 (n/a)</td><td>212.80 (n/a)</td><td>196.60 (n/a)</td><td>20.90 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (+12.84%)</td><td>0.19 (+6.40%)</td><td>0.18 (+0.18%)</td><td>0.15 (-1.84%)</td><td>0.03 <b>(+51.51%)</b></td><td>216.00 (+1.89%)</td><td>177.28 (-5.21%)</td><td>179.70 (-0.17%)</td><td>146.90 (-11.35%)</td><td>25.95 <b>(+36.02%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>212.00 (n/a)</td><td>187.02 (n/a)</td><td>180.00 (n/a)</td><td>165.70 (n/a)</td><td>19.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (-6.64%)</td><td>0.19 (-13.14%)</td><td>0.18 <b>(-20.23%)</b></td><td>0.13 (-13.12%)</td><td>0.05 (-9.68%)</td><td>245.10 (+15.07%)</td><td>181.98 (+14.92%)</td><td>180.00 <b>(+25.35%)</b></td><td>126.20 (+7.13%)</td><td>42.28 (+8.62%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.23 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>213.00 (n/a)</td><td>158.36 (n/a)</td><td>143.60 (n/a)</td><td>117.80 (n/a)</td><td>38.92 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (-9.45%)</td><td>0.20 (-8.99%)</td><td>0.18 (-15.65%)</td><td>0.17 (+8.19%)</td><td>0.03 <b>(-26.57%)</b></td><td>192.30 (-7.55%)</td><td>168.24 (+8.28%)</td><td>180.00 (+18.58%)</td><td>134.80 (+10.40%)</td><td>24.66 <b>(-25.73%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>208.00 (n/a)</td><td>155.38 (n/a)</td><td>151.80 (n/a)</td><td>122.10 (n/a)</td><td>33.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (-6.42%)</td><td>0.22 (-6.50%)</td><td>0.21 (-3.28%)</td><td>0.18 (-6.86%)</td><td>0.03 (-18.74%)</td><td>177.30 (+7.39%)</td><td>153.92 (+6.58%)</td><td>154.20 (+3.42%)</td><td>128.50 (+6.82%)</td><td>17.37 (-7.58%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>165.10 (n/a)</td><td>144.42 (n/a)</td><td>149.10 (n/a)</td><td>120.30 (n/a)</td><td>18.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.27 (+3.25%)</td><td>0.22 (+4.39%)</td><td>0.20 (+2.71%)</td><td>0.19 (+1.89%)</td><td>0.03 (+6.68%)</td><td>170.90 (-1.84%)</td><td>152.10 (-4.07%)</td><td>160.30 (-2.67%)</td><td>119.90 (-3.15%)</td><td>20.59 (+3.32%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>174.10 (n/a)</td><td>158.56 (n/a)</td><td>164.70 (n/a)</td><td>123.80 (n/a)</td><td>19.93 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 <b>(+23.73%)</b></td><td>0.20 (+6.55%)</td><td>0.21 (+9.87%)</td><td>0.16 (-8.01%)</td><td>0.04 <b>(+203.27%)</b></td><td>204.10 (+8.74%)</td><td>167.02 (-3.53%)</td><td>159.00 (-8.99%)</td><td>126.80 (-19.18%)</td><td>32.57 <b>(+173.95%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>187.70 (n/a)</td><td>173.14 (n/a)</td><td>174.70 (n/a)</td><td>156.90 (n/a)</td><td>11.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (+0.33%)</td><td>0.18 (-13.03%)</td><td>0.19 (-5.28%)</td><td>0.08 <b>(-53.63%)</b></td><td>0.06 <b>(+147.94%)</b></td><td>403.40 <b>(+115.61%)</b></td><td>213.06 <b>(+31.11%)</b></td><td>172.20 (+5.58%)</td><td>136.00 (-0.37%)</td><td>108.42 <b>(+481.95%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>187.10 (n/a)</td><td>162.50 (n/a)</td><td>163.10 (n/a)</td><td>136.50 (n/a)</td><td>18.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (+5.93%)</td><td>0.19 (-7.25%)</td><td>0.18 (-18.27%)</td><td>0.16 (-11.45%)</td><td>0.04 <b>(+67.64%)</b></td><td>201.90 (+12.98%)</td><td>173.92 (+10.08%)</td><td>184.90 <b>(+22.37%)</b></td><td>128.00 (-5.60%)</td><td>32.32 <b>(+79.09%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>178.70 (n/a)</td><td>158.00 (n/a)</td><td>151.10 (n/a)</td><td>135.60 (n/a)</td><td>18.05 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (+15.01%)</td><td>0.20 (+13.81%)</td><td>0.17 (+1.24%)</td><td>0.16 <b>(+51.79%)</b></td><td>0.04 (-11.57%)</td><td>201.10 <b>(-34.11%)</b></td><td>170.46 (-15.14%)</td><td>189.30 (-1.20%)</td><td>130.50 (-13.06%)</td><td>32.08 <b>(-49.09%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>305.20 (n/a)</td><td>200.88 (n/a)</td><td>191.60 (n/a)</td><td>150.10 (n/a)</td><td>63.02 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (-12.61%)</td><td>0.20 (-5.93%)</td><td>0.18 (-19.46%)</td><td>0.16 <b>(+77.86%)</b></td><td>0.03 <b>(-52.84%)</b></td><td>207.00 <b>(-43.77%)</b></td><td>171.80 (-7.36%)</td><td>181.00 <b>(+24.23%)</b></td><td>135.10 (+14.39%)</td><td>28.24 <b>(-72.61%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 (n/a)</td><td>0.21 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>368.10 (n/a)</td><td>185.44 (n/a)</td><td>145.70 (n/a)</td><td>118.10 (n/a)</td><td>103.09 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (-18.05%)</td><td>0.19 (-13.79%)</td><td>0.20 (-2.22%)</td><td>0.13 <b>(-22.11%)</b></td><td>0.04 (-7.29%)</td><td>262.00 <b>(+28.43%)</b></td><td>183.32 (+17.36%)</td><td>163.10 (+2.32%)</td><td>146.20 <b>(+22.04%)</b></td><td>46.66 <b>(+48.37%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>204.00 (n/a)</td><td>156.20 (n/a)</td><td>159.40 (n/a)</td><td>119.80 (n/a)</td><td>31.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 (-13.86%)</td><td>0.19 (-2.88%)</td><td>0.19 (-4.42%)</td><td>0.18 <b>(+22.36%)</b></td><td>0.01 <b>(-76.00%)</b></td><td>182.50 (-18.27%)</td><td>172.14 (-0.27%)</td><td>170.80 (+4.59%)</td><td>160.20 (+16.09%)</td><td>8.33 <b>(-77.02%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>223.30 (n/a)</td><td>172.60 (n/a)</td><td>163.30 (n/a)</td><td>138.00 (n/a)</td><td>36.27 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.29 (+16.71%)</td><td>0.23 <b>(+20.58%)</b></td><td>0.23 <b>(+26.82%)</b></td><td>0.17 (+6.42%)</td><td>0.05 <b>(+25.93%)</b></td><td>192.90 (-5.99%)</td><td>147.56 (-16.43%)</td><td>145.00 <b>(-21.15%)</b></td><td>111.40 (-14.31%)</td><td>30.57 (+3.78%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>205.20 (n/a)</td><td>176.56 (n/a)</td><td>183.90 (n/a)</td><td>130.00 (n/a)</td><td>29.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 (+0.06%)</td><td>0.18 (-0.01%)</td><td>0.18 (-0.07%)</td><td>0.18 (+0.02%)</td><td>0.00 <b>(+33.68%)</b></td><td>47571.90 (-0.02%)</td><td>47525.78 (+0.01%)</td><td>47550.20 (+0.07%)</td><td>47467.10 (-0.06%)</td><td>46.21 <b>(+33.67%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47581.50 (n/a)</td><td>47522.62 (n/a)</td><td>47515.90 (n/a)</td><td>47496.30 (n/a)</td><td>34.57 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 (-0.09%)</td><td>0.18 (+0.00%)</td><td>0.18 (+0.11%)</td><td>0.18 (-0.00%)</td><td>0.00 (-19.79%)</td><td>47630.30 (+0.00%)</td><td>47558.94 (-0.00%)</td><td>47535.50 (-0.11%)</td><td>47504.70 (+0.09%)</td><td>53.71 (-19.63%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47629.70 (n/a)</td><td>47559.72 (n/a)</td><td>47585.80 (n/a)</td><td>47460.40 (n/a)</td><td>66.82 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (-0.03%)</td><td>0.11 (-0.03%)</td><td>0.11 (-0.06%)</td><td>0.11 (-0.01%)</td><td>0.00 (-12.61%)</td><td>375708.80 (+0.01%)</td><td>375581.00 (+0.03%)</td><td>375644.20 (+0.06%)</td><td>375290.50 (+0.03%)</td><td>169.26 (-12.56%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>375686.90 (n/a)</td><td>375450.34 (n/a)</td><td>375433.70 (n/a)</td><td>375160.40 (n/a)</td><td>193.58 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.23 (+2.25%)</td><td>0.19 (+9.07%)</td><td>0.19 (+10.69%)</td><td>0.16 <b>(+34.72%)</b></td><td>0.03 <b>(-27.19%)</b></td><td>157.80 <b>(-25.78%)</b></td><td>135.10 (-10.92%)</td><td>129.60 (-9.69%)</td><td>107.70 (-2.18%)</td><td>20.20 <b>(-47.60%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>212.60 (n/a)</td><td>151.66 (n/a)</td><td>143.50 (n/a)</td><td>110.10 (n/a)</td><td>38.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.32 (-19.55%)</td><td>0.29 (-3.02%)</td><td>0.30 (+6.03%)</td><td>0.24 (-6.25%)</td><td>0.03 <b>(-39.15%)</b></td><td>206.20 (+6.67%)</td><td>168.92 (+1.96%)</td><td>163.40 (-5.66%)</td><td>152.30 <b>(+24.33%)</b></td><td>22.10 (-15.68%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.25 (n/a)</td><td>0.06 (n/a)</td><td>193.30 (n/a)</td><td>165.68 (n/a)</td><td>173.20 (n/a)</td><td>122.50 (n/a)</td><td>26.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.71 (+0.95%)</td><td>13.04 (+0.45%)</td><td>12.75 (-1.96%)</td><td>12.50 (+0.23%)</td><td>0.57 <b>(+39.09%)</b></td><td>838.70 (-0.23%)</td><td>805.50 (-0.37%)</td><td>822.50 (+2.01%)</td><td>764.90 (-0.95%)</td><td>34.86 <b>(+37.27%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>13.58 (n/a)</td><td>12.98 (n/a)</td><td>13.00 (n/a)</td><td>12.47 (n/a)</td><td>0.41 (n/a)</td><td>840.60 (n/a)</td><td>808.52 (n/a)</td><td>806.30 (n/a)</td><td>772.20 (n/a)</td><td>25.40 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.27 (-0.00%)</td><td>0.24 (-1.38%)</td><td>0.24 (+4.02%)</td><td>0.21 (-6.34%)</td><td>0.02 (-2.39%)</td><td>191.80 (+6.79%)</td><td>170.12 (+1.42%)</td><td>169.50 (-3.86%)</td><td>152.60 (+0.00%)</td><td>14.46 (+5.63%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.02 (n/a)</td><td>179.60 (n/a)</td><td>167.74 (n/a)</td><td>176.30 (n/a)</td><td>152.60 (n/a)</td><td>13.69 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (-3.91%)</td><td>0.04 (-8.16%)</td><td>0.04 (-17.07%)</td><td>0.03 (+18.94%)</td><td>0.01 <b>(-29.22%)</b></td><td>185.50 (-15.91%)</td><td>145.38 (+4.76%)</td><td>145.00 <b>(+20.63%)</b></td><td>110.80 (+4.14%)</td><td>27.33 <b>(-41.31%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>220.60 (n/a)</td><td>138.78 (n/a)</td><td>120.20 (n/a)</td><td>106.40 (n/a)</td><td>46.57 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-16.34%)</td><td>0.03 (-6.33%)</td><td>0.02 (+1.88%)</td><td>0.02 (+13.59%)</td><td>0.00 <b>(-59.02%)</b></td><td>174.50 (-11.96%)</td><td>161.76 (+1.74%)</td><td>168.40 (-1.86%)</td><td>131.90 (+19.58%)</td><td>17.26 <b>(-57.83%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>198.20 (n/a)</td><td>159.00 (n/a)</td><td>171.60 (n/a)</td><td>110.30 (n/a)</td><td>40.93 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.05 (+11.12%)</td><td>0.04 (+6.85%)</td><td>0.04 (+2.89%)</td><td>0.03 (+4.27%)</td><td>0.01 <b>(+44.05%)</b></td><td>181.40 (-4.12%)</td><td>149.40 (-5.81%)</td><td>149.50 (-2.80%)</td><td>128.90 (-9.99%)</td><td>21.18 (+19.64%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>189.20 (n/a)</td><td>158.62 (n/a)</td><td>153.80 (n/a)</td><td>143.20 (n/a)</td><td>17.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-19.35%)</td><td>0.03 (-4.98%)</td><td>0.03 (-4.92%)</td><td>0.02 (-3.44%)</td><td>0.00 <b>(-43.90%)</b></td><td>189.50 (+3.55%)</td><td>157.52 (+2.98%)</td><td>160.70 (+5.17%)</td><td>135.40 <b>(+23.99%)</b></td><td>21.58 <b>(-29.87%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>183.00 (n/a)</td><td>152.96 (n/a)</td><td>152.80 (n/a)</td><td>109.20 (n/a)</td><td>30.77 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (+14.42%)</td><td>0.03 (+1.85%)</td><td>0.03 (-9.10%)</td><td>0.03 <b>(+28.25%)</b></td><td>0.01 (-8.85%)</td><td>190.20 <b>(-22.02%)</b></td><td>162.68 (-3.68%)</td><td>157.20 (+10.01%)</td><td>121.30 (-12.61%)</td><td>28.41 <b>(-36.49%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>243.90 (n/a)</td><td>168.90 (n/a)</td><td>142.90 (n/a)</td><td>138.80 (n/a)</td><td>44.73 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-5.63%)</td><td>0.03 (-7.84%)</td><td>0.02 (-12.53%)</td><td>0.02 (+2.88%)</td><td>0.00 <b>(-27.13%)</b></td><td>187.80 (-2.80%)</td><td>163.58 (+6.86%)</td><td>166.40 (+14.36%)</td><td>127.00 (+5.92%)</td><td>22.61 <b>(-27.52%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>193.20 (n/a)</td><td>153.08 (n/a)</td><td>145.50 (n/a)</td><td>119.90 (n/a)</td><td>31.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (+6.91%)</td><td>0.03 (-4.11%)</td><td>0.03 (-10.71%)</td><td>0.03 (+6.81%)</td><td>0.01 (+9.65%)</td><td>199.10 (-6.39%)</td><td>162.18 (+4.36%)</td><td>158.80 (+11.99%)</td><td>128.60 (-6.47%)</td><td>30.38 (-5.56%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>212.70 (n/a)</td><td>155.40 (n/a)</td><td>141.80 (n/a)</td><td>137.50 (n/a)</td><td>32.17 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (+2.53%)</td><td>0.02 (-2.62%)</td><td>0.02 (-5.70%)</td><td>0.02 <b>(-21.22%)</b></td><td>0.01 <b>(+52.71%)</b></td><td>270.90 <b>(+26.89%)</b></td><td>181.14 (+7.62%)</td><td>164.80 (+6.05%)</td><td>129.00 (-2.49%)</td><td>58.39 <b>(+84.36%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>213.50 (n/a)</td><td>168.32 (n/a)</td><td>155.40 (n/a)</td><td>132.30 (n/a)</td><td>31.67 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-10.56%)</td><td>0.03 (-5.48%)</td><td>0.03 (-1.65%)</td><td>0.02 (-7.69%)</td><td>0.01 (-15.93%)</td><td>209.90 (+8.31%)</td><td>168.80 (+5.24%)</td><td>175.70 (+1.68%)</td><td>133.40 (+11.82%)</td><td>31.56 (-0.02%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>193.80 (n/a)</td><td>160.40 (n/a)</td><td>172.80 (n/a)</td><td>119.30 (n/a)</td><td>31.57 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-17.63%)</td><td>0.02 (-7.84%)</td><td>0.02 (+4.54%)</td><td>0.02 (-2.35%)</td><td>0.00 <b>(-40.44%)</b></td><td>235.30 (+2.39%)</td><td>182.40 (+4.79%)</td><td>170.40 (-4.38%)</td><td>148.70 <b>(+21.39%)</b></td><td>36.18 <b>(-24.53%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>229.80 (n/a)</td><td>174.06 (n/a)</td><td>178.20 (n/a)</td><td>122.50 (n/a)</td><td>47.95 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (+4.09%)</td><td>0.03 (+3.48%)</td><td>0.03 (+4.69%)</td><td>0.02 (-5.55%)</td><td>0.01 <b>(+27.26%)</b></td><td>212.70 (+5.87%)</td><td>159.34 (-2.19%)</td><td>149.50 (-4.47%)</td><td>132.10 (-3.93%)</td><td>33.58 <b>(+28.28%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>200.90 (n/a)</td><td>162.90 (n/a)</td><td>156.50 (n/a)</td><td>137.50 (n/a)</td><td>26.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-0.77%)</td><td>0.02 (-4.06%)</td><td>0.02 (+7.60%)</td><td>0.01 <b>(-22.80%)</b></td><td>0.01 (+16.11%)</td><td>299.80 <b>(+29.50%)</b></td><td>194.00 (+7.28%)</td><td>172.40 (-7.06%)</td><td>144.90 (+0.76%)</td><td>60.98 <b>(+66.47%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.50 (n/a)</td><td>180.84 (n/a)</td><td>185.50 (n/a)</td><td>143.80 (n/a)</td><td>36.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-1.56%)</td><td>0.03 (+1.17%)</td><td>0.03 (+12.09%)</td><td>0.02 (-8.60%)</td><td>0.00 (+18.96%)</td><td>224.40 (+9.41%)</td><td>176.54 (-0.19%)</td><td>162.20 (-10.78%)</td><td>142.40 (+1.57%)</td><td>32.29 <b>(+37.68%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>205.10 (n/a)</td><td>176.88 (n/a)</td><td>181.80 (n/a)</td><td>140.20 (n/a)</td><td>23.45 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (+1.02%)</td><td>0.02 (+2.17%)</td><td>0.02 (+1.43%)</td><td>0.02 (+12.44%)</td><td>0.00 <b>(-25.94%)</b></td><td>205.60 (-11.03%)</td><td>182.22 (-2.95%)</td><td>187.40 (-1.42%)</td><td>159.60 (-1.05%)</td><td>18.12 <b>(-34.75%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>231.10 (n/a)</td><td>187.76 (n/a)</td><td>190.10 (n/a)</td><td>161.30 (n/a)</td><td>27.77 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 <b>(-23.27%)</b></td><td>0.02 (-15.04%)</td><td>0.02 (-16.89%)</td><td>0.02 (+2.34%)</td><td>0.00 <b>(-45.32%)</b></td><td>280.80 (-2.30%)</td><td>223.24 (+13.04%)</td><td>221.70 <b>(+20.36%)</b></td><td>169.10 <b>(+30.28%)</b></td><td>39.53 <b>(-31.77%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>287.40 (n/a)</td><td>197.48 (n/a)</td><td>184.20 (n/a)</td><td>129.80 (n/a)</td><td>57.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.02 (-2.58%)</td><td>0.02 (-4.06%)</td><td>0.02 (+5.59%)</td><td>0.01 <b>(-26.89%)</b></td><td>0.00 <b>(+99.41%)</b></td><td>311.40 <b>(+36.82%)</b></td><td>228.40 (+7.81%)</td><td>207.10 (-5.26%)</td><td>183.00 (+2.64%)</td><td>54.60 <b>(+180.60%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>227.60 (n/a)</td><td>211.86 (n/a)</td><td>218.60 (n/a)</td><td>178.30 (n/a)</td><td>19.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (+2.56%)</td><td>0.05 (-14.44%)</td><td>0.04 <b>(-26.33%)</b></td><td>0.04 (-9.83%)</td><td>0.01 <b>(+27.14%)</b></td><td>222.50 (+10.86%)</td><td>188.08 (+19.14%)</td><td>210.40 <b>(+35.74%)</b></td><td>126.50 (-2.54%)</td><td>40.51 <b>(+39.82%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>200.70 (n/a)</td><td>157.86 (n/a)</td><td>155.00 (n/a)</td><td>129.80 (n/a)</td><td>28.97 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.08 (-0.74%)</td><td>0.07 (+6.94%)</td><td>0.07 (+6.76%)</td><td>0.07 (+8.68%)</td><td>0.00 <b>(-39.36%)</b></td><td>179.20 (-8.01%)</td><td>168.42 (-6.94%)</td><td>171.40 (-6.34%)</td><td>154.80 (+0.72%)</td><td>9.29 <b>(-43.58%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>194.80 (n/a)</td><td>180.98 (n/a)</td><td>183.00 (n/a)</td><td>153.70 (n/a)</td><td>16.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (-11.73%)</td><td>0.05 (-15.68%)</td><td>0.04 (-18.97%)</td><td>0.03 <b>(-21.76%)</b></td><td>0.01 (+2.40%)</td><td>240.50 <b>(+27.86%)</b></td><td>183.14 <b>(+20.34%)</b></td><td>192.30 <b>(+23.43%)</b></td><td>131.40 (+13.28%)</td><td>42.49 <b>(+47.39%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.10 (n/a)</td><td>152.18 (n/a)</td><td>155.80 (n/a)</td><td>116.00 (n/a)</td><td>28.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.08 (-3.67%)</td><td>0.06 (-9.27%)</td><td>0.06 (-8.67%)</td><td>0.05 (-13.78%)</td><td>0.01 <b>(+28.38%)</b></td><td>205.00 (+15.95%)</td><td>168.62 (+12.13%)</td><td>171.90 (+9.49%)</td><td>125.80 (+3.88%)</td><td>33.83 <b>(+57.37%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>176.80 (n/a)</td><td>150.38 (n/a)</td><td>157.00 (n/a)</td><td>121.10 (n/a)</td><td>21.50 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (+0.94%)</td><td>0.05 (-11.87%)</td><td>0.05 (-12.62%)</td><td>0.04 (-18.39%)</td><td>0.01 <b>(+36.96%)</b></td><td>223.60 <b>(+22.52%)</b></td><td>184.12 (+15.90%)</td><td>179.90 (+14.44%)</td><td>126.40 (-0.94%)</td><td>37.93 <b>(+60.14%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.50 (n/a)</td><td>158.86 (n/a)</td><td>157.20 (n/a)</td><td>127.60 (n/a)</td><td>23.69 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 <b>(-22.79%)</b></td><td>0.06 (-15.80%)</td><td>0.06 (-13.91%)</td><td>0.05 (-18.96%)</td><td>0.01 <b>(-39.08%)</b></td><td>207.00 <b>(+23.36%)</b></td><td>173.84 (+18.05%)</td><td>167.10 (+16.12%)</td><td>161.20 <b>(+29.48%)</b></td><td>19.04 (-4.05%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>167.80 (n/a)</td><td>147.26 (n/a)</td><td>143.90 (n/a)</td><td>124.50 (n/a)</td><td>19.85 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (+6.40%)</td><td>0.05 (-3.67%)</td><td>0.05 (-14.37%)</td><td>0.04 (+16.30%)</td><td>0.01 (-14.77%)</td><td>201.20 (-14.02%)</td><td>163.04 (+1.95%)</td><td>165.10 (+16.76%)</td><td>126.80 (-6.00%)</td><td>27.87 <b>(-33.39%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>234.00 (n/a)</td><td>159.92 (n/a)</td><td>141.40 (n/a)</td><td>134.90 (n/a)</td><td>41.84 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (+17.39%)</td><td>0.06 <b>(+25.47%)</b></td><td>0.06 <b>(+35.09%)</b></td><td>0.05 <b>(+25.93%)</b></td><td>0.01 (-2.13%)</td><td>190.50 <b>(-20.59%)</b></td><td>152.82 <b>(-20.96%)</b></td><td>145.80 <b>(-25.95%)</b></td><td>131.60 (-14.82%)</td><td>23.17 <b>(-32.10%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>239.90 (n/a)</td><td>193.34 (n/a)</td><td>196.90 (n/a)</td><td>154.50 (n/a)</td><td>34.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 (-3.27%)</td><td>0.05 (-12.16%)</td><td>0.05 (-10.27%)</td><td>0.03 <b>(-23.61%)</b></td><td>0.01 <b>(+73.13%)</b></td><td>247.00 <b>(+30.90%)</b></td><td>185.10 (+18.56%)</td><td>168.50 (+11.44%)</td><td>141.30 (+3.37%)</td><td>49.24 <b>(+131.53%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>188.70 (n/a)</td><td>156.12 (n/a)</td><td>151.20 (n/a)</td><td>136.70 (n/a)</td><td>21.27 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (-0.78%)</td><td>0.05 (-2.44%)</td><td>0.05 (-0.66%)</td><td>0.04 (-4.17%)</td><td>0.01 (+3.90%)</td><td>240.40 (+4.34%)</td><td>189.10 (+2.97%)</td><td>193.20 (+0.62%)</td><td>137.10 (+0.81%)</td><td>40.40 (+9.68%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.40 (n/a)</td><td>183.64 (n/a)</td><td>192.00 (n/a)</td><td>136.00 (n/a)</td><td>36.84 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 (+11.20%)</td><td>0.05 (+4.73%)</td><td>0.04 (+1.93%)</td><td>0.04 (+0.64%)</td><td>0.01 <b>(+26.01%)</b></td><td>209.40 (-0.66%)</td><td>175.40 (-3.18%)</td><td>187.20 (-1.89%)</td><td>111.60 (-10.00%)</td><td>37.96 (+10.80%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>210.80 (n/a)</td><td>181.16 (n/a)</td><td>190.80 (n/a)</td><td>124.00 (n/a)</td><td>34.26 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 <b>(+23.58%)</b></td><td>0.04 (+7.26%)</td><td>0.04 (-13.23%)</td><td>0.03 <b>(+34.34%)</b></td><td>0.01 (+9.57%)</td><td>256.60 <b>(-25.56%)</b></td><td>207.92 (-8.43%)</td><td>222.00 (+15.26%)</td><td>143.50 (-19.06%)</td><td>42.45 <b>(-37.97%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>344.70 (n/a)</td><td>227.06 (n/a)</td><td>192.60 (n/a)</td><td>177.30 (n/a)</td><td>68.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.07 <b>(+57.64%)</b></td><td>0.05 <b>(+20.11%)</b></td><td>0.04 (-5.91%)</td><td>0.04 <b>(+29.44%)</b></td><td>0.01 <b>(+109.46%)</b></td><td>226.00 <b>(-22.74%)</b></td><td>184.70 (-14.23%)</td><td>206.70 (+6.27%)</td><td>117.90 <b>(-36.54%)</b></td><td>44.65 (+0.47%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>292.50 (n/a)</td><td>215.34 (n/a)</td><td>194.50 (n/a)</td><td>185.80 (n/a)</td><td>44.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.06 <b>(+22.74%)</b></td><td>0.05 (+16.50%)</td><td>0.05 (+13.28%)</td><td>0.04 (+17.59%)</td><td>0.01 <b>(+51.72%)</b></td><td>220.80 (-14.95%)</td><td>185.78 (-13.62%)</td><td>187.50 (-11.72%)</td><td>156.50 (-18.53%)</td><td>27.51 (+2.48%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>259.60 (n/a)</td><td>215.08 (n/a)</td><td>212.40 (n/a)</td><td>192.10 (n/a)</td><td>26.84 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.04 (-7.41%)</td><td>0.04 (-1.74%)</td><td>0.04 (+3.25%)</td><td>0.03 (+4.84%)</td><td>0.00 <b>(-53.79%)</b></td><td>234.30 (-4.64%)</td><td>220.68 (+1.19%)</td><td>216.10 (-3.14%)</td><td>210.50 (+8.00%)</td><td>10.09 <b>(-51.80%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>245.70 (n/a)</td><td>218.08 (n/a)</td><td>223.10 (n/a)</td><td>194.90 (n/a)</td><td>20.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (-5.07%)</td><td>0.09 (-9.59%)</td><td>0.08 (-12.48%)</td><td>0.08 (-12.84%)</td><td>0.01 <b>(+27.20%)</b></td><td>215.90 (+14.72%)</td><td>192.94 (+11.23%)</td><td>201.10 (+14.26%)</td><td>160.40 (+5.32%)</td><td>22.51 <b>(+52.86%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>188.20 (n/a)</td><td>173.46 (n/a)</td><td>176.00 (n/a)</td><td>152.30 (n/a)</td><td>14.72 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 <b>(+22.32%)</b></td><td>0.16 (+10.77%)</td><td>0.14 (+6.54%)</td><td>0.12 (+3.99%)</td><td>0.03 <b>(+79.21%)</b></td><td>197.00 (-3.86%)</td><td>162.26 (-8.34%)</td><td>170.10 (-6.13%)</td><td>125.40 (-18.25%)</td><td>28.20 <b>(+40.25%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>204.90 (n/a)</td><td>177.02 (n/a)</td><td>181.20 (n/a)</td><td>153.40 (n/a)</td><td>20.11 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (+16.74%)</td><td>0.11 (+17.87%)</td><td>0.11 (+14.34%)</td><td>0.10 <b>(+26.01%)</b></td><td>0.01 (+11.35%)</td><td>169.70 <b>(-20.63%)</b></td><td>147.58 (-15.37%)</td><td>145.10 (-12.54%)</td><td>124.80 (-14.34%)</td><td>19.34 <b>(-24.50%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>213.80 (n/a)</td><td>174.38 (n/a)</td><td>165.90 (n/a)</td><td>145.70 (n/a)</td><td>25.62 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.16 <b>(+25.23%)</b></td><td>0.14 <b>(+39.44%)</b></td><td>0.14 <b>(+56.42%)</b></td><td>0.11 <b>(+27.00%)</b></td><td>0.02 <b>(+21.98%)</b></td><td>185.50 <b>(-21.26%)</b></td><td>148.62 <b>(-28.44%)</b></td><td>143.50 <b>(-36.05%)</b></td><td>127.00 <b>(-20.18%)</b></td><td>24.66 <b>(-25.41%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>235.60 (n/a)</td><td>207.68 (n/a)</td><td>224.40 (n/a)</td><td>159.10 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 <b>(+24.77%)</b></td><td>0.10 (+6.28%)</td><td>0.10 (+5.47%)</td><td>0.07 (-15.02%)</td><td>0.03 <b>(+102.22%)</b></td><td>250.90 (+17.68%)</td><td>175.30 (-0.78%)</td><td>158.70 (-5.20%)</td><td>118.20 (-19.86%)</td><td>53.85 <b>(+91.86%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>213.20 (n/a)</td><td>176.68 (n/a)</td><td>167.40 (n/a)</td><td>147.50 (n/a)</td><td>28.07 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (+12.11%)</td><td>0.13 (+10.23%)</td><td>0.13 (+17.14%)</td><td>0.09 (-8.45%)</td><td>0.02 <b>(+66.80%)</b></td><td>228.30 (+9.23%)</td><td>167.16 (-7.28%)</td><td>152.80 (-14.64%)</td><td>135.90 (-10.83%)</td><td>37.44 <b>(+64.00%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>209.00 (n/a)</td><td>180.28 (n/a)</td><td>179.00 (n/a)</td><td>152.40 (n/a)</td><td>22.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (-0.73%)</td><td>0.10 (-9.87%)</td><td>0.10 (-2.99%)</td><td>0.07 (-5.91%)</td><td>0.02 (+13.87%)</td><td>236.10 (+6.26%)</td><td>180.30 (+12.55%)</td><td>161.90 (+3.12%)</td><td>127.00 (+0.79%)</td><td>45.45 <b>(+22.09%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>222.20 (n/a)</td><td>160.20 (n/a)</td><td>157.00 (n/a)</td><td>126.00 (n/a)</td><td>37.22 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (-12.87%)</td><td>0.12 (+0.77%)</td><td>0.11 (+10.42%)</td><td>0.10 <b>(+28.32%)</b></td><td>0.02 <b>(-46.54%)</b></td><td>193.70 <b>(-22.08%)</b></td><td>161.90 (-6.35%)</td><td>166.30 (-9.42%)</td><td>126.90 (+14.74%)</td><td>25.84 <b>(-51.74%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>248.60 (n/a)</td><td>172.88 (n/a)</td><td>183.60 (n/a)</td><td>110.60 (n/a)</td><td>53.54 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (+11.04%)</td><td>0.11 (+5.43%)</td><td>0.11 (+12.44%)</td><td>0.07 (-18.78%)</td><td>0.03 <b>(+64.74%)</b></td><td>250.30 <b>(+23.12%)</b></td><td>167.16 (+0.49%)</td><td>152.60 (-11.07%)</td><td>108.90 (-9.93%)</td><td>56.46 <b>(+90.72%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>203.30 (n/a)</td><td>166.34 (n/a)</td><td>171.60 (n/a)</td><td>120.90 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 <b>(-26.89%)</b></td><td>0.10 (-9.65%)</td><td>0.09 (-1.73%)</td><td>0.09 (+8.41%)</td><td>0.01 <b>(-59.91%)</b></td><td>205.30 (-7.73%)</td><td>185.78 (+4.96%)</td><td>199.00 (+1.74%)</td><td>156.00 <b>(+36.84%)</b></td><td>24.00 <b>(-49.48%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>222.50 (n/a)</td><td>177.00 (n/a)</td><td>195.60 (n/a)</td><td>114.00 (n/a)</td><td>47.51 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 <b>(+54.78%)</b></td><td>0.11 <b>(+38.74%)</b></td><td>0.09 <b>(+22.51%)</b></td><td>0.08 (+11.42%)</td><td>0.03 <b>(+179.83%)</b></td><td>200.30 (-10.22%)</td><td>157.50 <b>(-24.52%)</b></td><td>178.10 (-18.38%)</td><td>106.30 <b>(-35.38%)</b></td><td>40.41 <b>(+63.03%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>223.10 (n/a)</td><td>208.66 (n/a)</td><td>218.20 (n/a)</td><td>164.50 (n/a)</td><td>24.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 (-4.02%)</td><td>0.09 (+0.87%)</td><td>0.09 (+4.69%)</td><td>0.08 (+4.81%)</td><td>0.01 <b>(-27.49%)</b></td><td>214.80 (-4.58%)</td><td>196.54 (-1.56%)</td><td>203.50 (-4.50%)</td><td>169.60 (+4.18%)</td><td>19.05 <b>(-27.77%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>225.10 (n/a)</td><td>199.66 (n/a)</td><td>213.10 (n/a)</td><td>162.80 (n/a)</td><td>26.38 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.09 (-19.74%)</td><td>0.08 <b>(-21.96%)</b></td><td>0.08 (-18.17%)</td><td>0.06 <b>(-27.83%)</b></td><td>0.01 (-1.70%)</td><td>284.90 <b>(+38.57%)</b></td><td>216.42 <b>(+29.39%)</b></td><td>200.40 <b>(+22.20%)</b></td><td>181.60 <b>(+24.64%)</b></td><td>40.41 <b>(+72.75%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>205.60 (n/a)</td><td>167.26 (n/a)</td><td>164.00 (n/a)</td><td>145.70 (n/a)</td><td>23.39 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (-11.65%)</td><td>0.09 (-4.93%)</td><td>0.10 (+1.56%)</td><td>0.05 <b>(-31.31%)</b></td><td>0.03 (+2.04%)</td><td>331.70 <b>(+45.55%)</b></td><td>202.58 (+9.54%)</td><td>177.70 (-1.55%)</td><td>133.20 (+13.17%)</td><td>77.47 <b>(+77.56%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>227.90 (n/a)</td><td>184.94 (n/a)</td><td>180.50 (n/a)</td><td>117.70 (n/a)</td><td>43.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (+8.63%)</td><td>0.08 (-10.05%)</td><td>0.07 (-13.69%)</td><td>0.05 <b>(-34.91%)</b></td><td>0.02 <b>(+122.51%)</b></td><td>330.70 <b>(+53.67%)</b></td><td>230.32 (+17.26%)</td><td>232.00 (+15.88%)</td><td>151.50 (-7.96%)</td><td>65.09 <b>(+215.01%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>215.20 (n/a)</td><td>196.42 (n/a)</td><td>200.20 (n/a)</td><td>164.60 (n/a)</td><td>20.66 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 <b>(+21.00%)</b></td><td>0.20 (+3.25%)</td><td>0.20 (-6.87%)</td><td>0.17 (+1.82%)</td><td>0.04 <b>(+56.40%)</b></td><td>189.90 (-1.76%)</td><td>164.80 (-2.02%)</td><td>167.30 (+7.38%)</td><td>124.40 (-17.40%)</td><td>26.66 <b>(+26.95%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>193.30 (n/a)</td><td>168.20 (n/a)</td><td>155.80 (n/a)</td><td>150.60 (n/a)</td><td>21.00 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.34 <b>(+51.03%)</b></td><td>0.23 <b>(+22.54%)</b></td><td>0.22 (+19.70%)</td><td>0.17 (+7.97%)</td><td>0.07 <b>(+164.92%)</b></td><td>191.20 (-7.41%)</td><td>148.98 (-14.72%)</td><td>150.10 (-16.47%)</td><td>96.10 <b>(-33.77%)</b></td><td>37.32 <b>(+61.72%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>206.50 (n/a)</td><td>174.70 (n/a)</td><td>179.70 (n/a)</td><td>145.10 (n/a)</td><td>23.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.30 <b>(-26.00%)</b></td><td>0.21 <b>(-23.18%)</b></td><td>0.22 (-18.74%)</td><td>0.12 <b>(-33.41%)</b></td><td>0.06 <b>(-25.22%)</b></td><td>328.00 <b>(+50.18%)</b></td><td>210.98 <b>(+31.53%)</b></td><td>190.30 <b>(+23.09%)</b></td><td>138.30 <b>(+35.06%)</b></td><td>71.53 <b>(+56.90%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.40 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.19 (n/a)</td><td>0.08 (n/a)</td><td>218.40 (n/a)</td><td>160.40 (n/a)</td><td>154.60 (n/a)</td><td>102.40 (n/a)</td><td>45.59 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (+16.37%)</td><td>0.20 (+0.87%)</td><td>0.17 (-12.25%)</td><td>0.15 (-14.59%)</td><td>0.05 <b>(+172.63%)</b></td><td>217.10 (+17.04%)</td><td>175.48 (+4.09%)</td><td>193.80 (+13.93%)</td><td>123.70 (-14.10%)</td><td>44.23 <b>(+174.55%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>185.50 (n/a)</td><td>168.58 (n/a)</td><td>170.10 (n/a)</td><td>144.00 (n/a)</td><td>16.11 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.29 (+0.84%)</td><td>0.24 (+5.46%)</td><td>0.23 (+3.04%)</td><td>0.19 (+7.37%)</td><td>0.04 (-11.71%)</td><td>219.00 (-6.89%)</td><td>177.20 (-5.89%)</td><td>180.20 (-2.96%)</td><td>142.40 (-0.84%)</td><td>28.26 (-18.10%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>235.20 (n/a)</td><td>188.30 (n/a)</td><td>185.70 (n/a)</td><td>143.60 (n/a)</td><td>34.50 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.30 (+18.57%)</td><td>0.21 (-6.57%)</td><td>0.17 <b>(-20.18%)</b></td><td>0.15 <b>(-22.30%)</b></td><td>0.07 <b>(+130.80%)</b></td><td>218.20 <b>(+28.66%)</b></td><td>171.34 (+14.76%)</td><td>193.30 <b>(+25.28%)</b></td><td>107.50 (-15.69%)</td><td>51.51 <b>(+157.59%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>169.60 (n/a)</td><td>149.30 (n/a)</td><td>154.30 (n/a)</td><td>127.50 (n/a)</td><td>20.00 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.28 (+11.29%)</td><td>0.23 (+13.64%)</td><td>0.23 (+10.13%)</td><td>0.19 <b>(+30.81%)</b></td><td>0.03 <b>(-27.02%)</b></td><td>192.50 <b>(-23.55%)</b></td><td>161.08 (-14.52%)</td><td>157.10 (-9.19%)</td><td>131.40 (-10.12%)</td><td>23.93 <b>(-48.84%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>251.80 (n/a)</td><td>188.44 (n/a)</td><td>173.00 (n/a)</td><td>146.20 (n/a)</td><td>46.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (-10.42%)</td><td>0.19 (-17.12%)</td><td>0.18 <b>(-21.65%)</b></td><td>0.15 (-13.38%)</td><td>0.04 (+5.59%)</td><td>217.20 (+15.41%)</td><td>181.28 <b>(+22.12%)</b></td><td>181.30 <b>(+27.68%)</b></td><td>126.70 (+11.63%)</td><td>37.43 <b>(+37.71%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>188.20 (n/a)</td><td>148.44 (n/a)</td><td>142.00 (n/a)</td><td>113.50 (n/a)</td><td>27.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (-8.30%)</td><td>0.23 (+13.99%)</td><td>0.22 (+6.55%)</td><td>0.22 <b>(+79.68%)</b></td><td>0.01 <b>(-82.04%)</b></td><td>170.10 <b>(-44.34%)</b></td><td>162.40 (-17.86%)</td><td>165.10 (-6.14%)</td><td>155.20 (+9.07%)</td><td>6.59 <b>(-89.66%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.12 (n/a)</td><td>0.05 (n/a)</td><td>305.60 (n/a)</td><td>197.70 (n/a)</td><td>175.90 (n/a)</td><td>142.30 (n/a)</td><td>63.69 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (+0.35%)</td><td>0.19 (-2.49%)</td><td>0.19 (-1.61%)</td><td>0.15 (+6.96%)</td><td>0.04 (+9.14%)</td><td>222.70 (-6.51%)</td><td>179.56 (+2.99%)</td><td>170.10 (+1.67%)</td><td>132.70 (-0.38%)</td><td>39.25 (+1.71%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>238.20 (n/a)</td><td>174.34 (n/a)</td><td>167.30 (n/a)</td><td>133.20 (n/a)</td><td>38.59 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.21 (-0.53%)</td><td>0.20 (+16.74%)</td><td>0.20 <b>(+28.80%)</b></td><td>0.18 <b>(+36.86%)</b></td><td>0.01 <b>(-62.56%)</b></td><td>191.30 <b>(-26.93%)</b></td><td>177.20 (-17.05%)</td><td>175.50 <b>(-22.35%)</b></td><td>162.30 (+0.56%)</td><td>12.30 <b>(-72.00%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>261.80 (n/a)</td><td>213.62 (n/a)</td><td>226.00 (n/a)</td><td>161.40 (n/a)</td><td>43.94 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 (-10.29%)</td><td>0.17 (-1.52%)</td><td>0.19 (-4.95%)</td><td>0.14 <b>(+42.83%)</b></td><td>0.03 <b>(-47.15%)</b></td><td>242.10 <b>(-29.99%)</b></td><td>191.74 (-5.74%)</td><td>177.00 (+5.23%)</td><td>162.50 (+11.45%)</td><td>32.66 <b>(-60.23%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>345.80 (n/a)</td><td>203.42 (n/a)</td><td>168.20 (n/a)</td><td>145.80 (n/a)</td><td>82.11 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.21 (+4.68%)</td><td>0.17 (-1.10%)</td><td>0.17 (+1.34%)</td><td>0.14 (-10.78%)</td><td>0.03 <b>(+55.21%)</b></td><td>252.40 (+12.08%)</td><td>204.96 (+2.40%)</td><td>201.20 (-1.28%)</td><td>165.10 (-4.46%)</td><td>33.05 <b>(+67.81%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>225.20 (n/a)</td><td>200.16 (n/a)</td><td>203.80 (n/a)</td><td>172.80 (n/a)</td><td>19.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 (+0.83%)</td><td>0.13 (-14.52%)</td><td>0.11 <b>(-25.81%)</b></td><td>0.10 <b>(-20.80%)</b></td><td>0.04 <b>(+78.34%)</b></td><td>334.60 <b>(+26.26%)</b></td><td>273.66 <b>(+22.20%)</b></td><td>304.60 <b>(+34.78%)</b></td><td>180.20 (-0.83%)</td><td>68.04 <b>(+129.85%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>265.00 (n/a)</td><td>223.94 (n/a)</td><td>226.00 (n/a)</td><td>181.70 (n/a)</td><td>29.60 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 <b>(+41.51%)</b></td><td>0.14 (+15.42%)</td><td>0.13 (+11.74%)</td><td>0.11 (-2.12%)</td><td>0.03 <b>(+341.05%)</b></td><td>189.40 (+2.16%)</td><td>153.52 (-10.70%)</td><td>154.40 (-10.49%)</td><td>112.30 <b>(-29.33%)</b></td><td>29.71 <b>(+215.42%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>185.40 (n/a)</td><td>171.92 (n/a)</td><td>172.50 (n/a)</td><td>158.90 (n/a)</td><td>9.42 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (-12.04%)</td><td>0.12 (+0.79%)</td><td>0.12 (+8.13%)</td><td>0.11 (+4.53%)</td><td>0.01 <b>(-48.99%)</b></td><td>183.00 (-4.34%)</td><td>167.50 (-2.08%)</td><td>166.80 (-7.54%)</td><td>148.10 (+13.66%)</td><td>13.58 <b>(-42.81%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>191.30 (n/a)</td><td>171.06 (n/a)</td><td>180.40 (n/a)</td><td>130.30 (n/a)</td><td>23.74 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.16 (-3.63%)</td><td>0.11 (-2.85%)</td><td>0.10 (-9.25%)</td><td>0.09 (-1.19%)</td><td>0.03 (-5.30%)</td><td>221.50 (+1.19%)</td><td>186.66 (+2.70%)</td><td>202.80 (+10.16%)</td><td>127.00 (+3.76%)</td><td>37.47 (-0.60%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>218.90 (n/a)</td><td>181.76 (n/a)</td><td>184.10 (n/a)</td><td>122.40 (n/a)</td><td>37.70 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (-11.84%)</td><td>0.13 (+7.86%)</td><td>0.13 <b>(+29.08%)</b></td><td>0.10 (+7.36%)</td><td>0.02 <b>(-42.70%)</b></td><td>201.10 (-6.86%)</td><td>165.36 (-9.83%)</td><td>155.50 <b>(-22.52%)</b></td><td>142.60 (+13.44%)</td><td>23.43 <b>(-39.85%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>215.90 (n/a)</td><td>183.38 (n/a)</td><td>200.70 (n/a)</td><td>125.70 (n/a)</td><td>38.95 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.16 (+11.46%)</td><td>0.13 (+4.91%)</td><td>0.14 (+5.55%)</td><td>0.09 (-18.22%)</td><td>0.03 <b>(+126.88%)</b></td><td>230.60 <b>(+22.27%)</b></td><td>159.02 (-0.97%)</td><td>148.80 (-5.28%)</td><td>126.90 (-10.25%)</td><td>42.37 <b>(+146.06%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>188.60 (n/a)</td><td>160.58 (n/a)</td><td>157.10 (n/a)</td><td>141.40 (n/a)</td><td>17.22 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 <b>(+32.92%)</b></td><td>0.15 <b>(+27.67%)</b></td><td>0.16 <b>(+23.82%)</b></td><td>0.10 (+15.18%)</td><td>0.03 <b>(+52.30%)</b></td><td>199.40 (-13.19%)</td><td>140.64 <b>(-20.61%)</b></td><td>131.10 (-19.22%)</td><td>113.80 <b>(-24.74%)</b></td><td>33.64 (+4.21%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>229.70 (n/a)</td><td>177.16 (n/a)</td><td>162.30 (n/a)</td><td>151.20 (n/a)</td><td>32.28 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.14 (-3.85%)</td><td>0.11 (-8.20%)</td><td>0.11 (-16.44%)</td><td>0.07 (-15.37%)</td><td>0.02 (-14.12%)</td><td>282.50 (+18.20%)</td><td>198.48 (+8.60%)</td><td>188.00 (+19.67%)</td><td>150.20 (+3.94%)</td><td>49.58 (+10.49%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>239.00 (n/a)</td><td>182.76 (n/a)</td><td>157.10 (n/a)</td><td>144.50 (n/a)</td><td>44.87 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (+1.77%)</td><td>0.11 (+0.73%)</td><td>0.11 (+4.23%)</td><td>0.09 (-1.06%)</td><td>0.02 (-8.71%)</td><td>222.30 (+1.05%)</td><td>187.84 (-1.05%)</td><td>189.30 (-4.05%)</td><td>153.70 (-1.79%)</td><td>25.54 (-9.16%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>220.00 (n/a)</td><td>189.84 (n/a)</td><td>197.30 (n/a)</td><td>156.50 (n/a)</td><td>28.12 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 <b>(+21.27%)</b></td><td>0.17 <b>(+23.27%)</b></td><td>0.17 <b>(+29.39%)</b></td><td>0.14 <b>(+20.02%)</b></td><td>0.02 (+5.91%)</td><td>174.00 (-16.67%)</td><td>145.38 (-19.17%)</td><td>147.00 <b>(-22.71%)</b></td><td>122.80 (-17.53%)</td><td>19.11 <b>(-25.90%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>208.80 (n/a)</td><td>179.86 (n/a)</td><td>190.20 (n/a)</td><td>148.90 (n/a)</td><td>25.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 (-9.36%)</td><td>0.16 (+4.53%)</td><td>0.16 (+19.44%)</td><td>0.14 <b>(+24.72%)</b></td><td>0.02 <b>(-57.47%)</b></td><td>172.40 (-19.81%)</td><td>154.42 (-8.26%)</td><td>154.60 (-16.25%)</td><td>134.50 (+10.34%)</td><td>15.93 <b>(-60.91%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>215.00 (n/a)</td><td>168.32 (n/a)</td><td>184.60 (n/a)</td><td>121.90 (n/a)</td><td>40.74 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 (-19.45%)</td><td>0.15 (+2.24%)</td><td>0.16 (+17.75%)</td><td>0.11 (-7.38%)</td><td>0.03 <b>(-33.28%)</b></td><td>221.00 (+7.96%)</td><td>165.70 (-3.98%)</td><td>150.80 (-15.09%)</td><td>136.70 <b>(+24.16%)</b></td><td>34.64 (-7.04%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>204.70 (n/a)</td><td>172.56 (n/a)</td><td>177.60 (n/a)</td><td>110.10 (n/a)</td><td>37.26 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.17 (-18.11%)</td><td>0.15 (-4.28%)</td><td>0.14 (+2.13%)</td><td>0.13 (+1.64%)</td><td>0.02 <b>(-48.81%)</b></td><td>191.20 (-1.60%)</td><td>169.86 (+2.50%)</td><td>169.70 (-2.08%)</td><td>144.30 <b>(+22.08%)</b></td><td>18.25 <b>(-35.61%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>194.30 (n/a)</td><td>165.72 (n/a)</td><td>173.30 (n/a)</td><td>118.20 (n/a)</td><td>28.35 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.17 (-12.94%)</td><td>0.15 (-1.17%)</td><td>0.16 (-3.98%)</td><td>0.13 (+17.31%)</td><td>0.01 <b>(-54.42%)</b></td><td>186.30 (-14.74%)</td><td>160.48 (-1.70%)</td><td>157.80 (+4.16%)</td><td>146.00 (+14.87%)</td><td>16.11 <b>(-55.68%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>218.50 (n/a)</td><td>163.26 (n/a)</td><td>151.50 (n/a)</td><td>127.10 (n/a)</td><td>36.35 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.19 <b>(+29.43%)</b></td><td>0.13 (+0.47%)</td><td>0.11 (-15.01%)</td><td>0.10 (-6.70%)</td><td>0.04 <b>(+112.17%)</b></td><td>246.90 (+7.21%)</td><td>199.96 (+3.51%)</td><td>214.30 (+17.68%)</td><td>128.60 <b>(-22.76%)</b></td><td>47.18 <b>(+72.60%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>230.30 (n/a)</td><td>193.18 (n/a)</td><td>182.10 (n/a)</td><td>166.50 (n/a)</td><td>27.34 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.17 (+0.02%)</td><td>0.13 (-4.41%)</td><td>0.12 (-8.64%)</td><td>0.10 (-2.70%)</td><td>0.03 (+11.49%)</td><td>251.90 (+2.77%)</td><td>200.34 (+5.49%)</td><td>209.70 (+9.45%)</td><td>148.10 (+0.00%)</td><td>43.04 (+13.76%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>245.10 (n/a)</td><td>189.92 (n/a)</td><td>191.60 (n/a)</td><td>148.10 (n/a)</td><td>37.83 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (+6.20%)</td><td>0.13 (-1.05%)</td><td>0.13 (-1.76%)</td><td>0.11 (-10.76%)</td><td>0.02 <b>(+105.54%)</b></td><td>231.50 (+12.05%)</td><td>194.46 (+2.36%)</td><td>196.20 (+1.76%)</td><td>165.70 (-5.85%)</td><td>28.09 <b>(+114.68%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>206.60 (n/a)</td><td>189.98 (n/a)</td><td>192.80 (n/a)</td><td>176.00 (n/a)</td><td>13.08 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.15 (+0.44%)</td><td>0.11 (+6.38%)</td><td>0.11 (+3.32%)</td><td>0.10 (+18.55%)</td><td>0.02 <b>(-20.49%)</b></td><td>187.50 (-15.65%)</td><td>164.84 (-7.58%)</td><td>171.90 (-3.21%)</td><td>125.00 (-0.48%)</td><td>23.73 <b>(-33.81%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>222.30 (n/a)</td><td>178.36 (n/a)</td><td>177.60 (n/a)</td><td>125.60 (n/a)</td><td>35.84 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.16 <b>(+25.19%)</b></td><td>0.13 <b>(+28.79%)</b></td><td>0.12 (+10.95%)</td><td>0.11 <b>(+51.07%)</b></td><td>0.02 (-0.31%)</td><td>168.00 <b>(-33.81%)</b></td><td>144.12 <b>(-23.87%)</b></td><td>151.30 (-9.89%)</td><td>115.90 <b>(-20.12%)</b></td><td>23.19 <b>(-48.17%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>253.80 (n/a)</td><td>189.32 (n/a)</td><td>167.90 (n/a)</td><td>145.10 (n/a)</td><td>44.75 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.12 (+1.11%)</td><td>0.11 (+11.14%)</td><td>0.11 (+18.56%)</td><td>0.09 <b>(+30.71%)</b></td><td>0.01 <b>(-35.30%)</b></td><td>214.60 <b>(-23.52%)</b></td><td>171.52 (-12.94%)</td><td>162.80 (-15.65%)</td><td>148.70 (-1.06%)</td><td>26.04 <b>(-50.01%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>280.60 (n/a)</td><td>197.02 (n/a)</td><td>193.00 (n/a)</td><td>150.30 (n/a)</td><td>52.10 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 <b>(-23.64%)</b></td><td>0.11 (-2.17%)</td><td>0.10 (+3.87%)</td><td>0.07 (-1.19%)</td><td>0.03 <b>(-29.95%)</b></td><td>263.10 (+1.19%)</td><td>183.22 (-0.42%)</td><td>178.80 (-3.77%)</td><td>137.90 <b>(+30.96%)</b></td><td>51.73 (-5.47%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>260.00 (n/a)</td><td>184.00 (n/a)</td><td>185.80 (n/a)</td><td>105.30 (n/a)</td><td>54.72 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (+0.74%)</td><td>0.10 (-8.26%)</td><td>0.09 (-13.72%)</td><td>0.09 (-3.14%)</td><td>0.02 (+0.09%)</td><td>213.90 (+3.23%)</td><td>191.70 (+9.07%)</td><td>206.80 (+15.85%)</td><td>147.10 (-0.74%)</td><td>27.98 (+4.83%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>207.20 (n/a)</td><td>175.76 (n/a)</td><td>178.50 (n/a)</td><td>148.20 (n/a)</td><td>26.69 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.11 (-6.73%)</td><td>0.09 (-9.86%)</td><td>0.10 (-13.33%)</td><td>0.08 (-3.68%)</td><td>0.01 <b>(-20.03%)</b></td><td>232.80 (+3.84%)</td><td>199.18 (+10.43%)</td><td>192.10 (+15.44%)</td><td>171.30 (+7.20%)</td><td>23.98 (-10.51%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>224.20 (n/a)</td><td>180.36 (n/a)</td><td>166.40 (n/a)</td><td>159.80 (n/a)</td><td>26.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.18 <b>(+58.04%)</b></td><td>0.10 (+9.88%)</td><td>0.08 (-7.71%)</td><td>0.07 (-15.28%)</td><td>0.05 <b>(+263.46%)</b></td><td>259.90 (+18.03%)</td><td>201.14 (+1.18%)</td><td>220.50 (+8.35%)</td><td>100.70 <b>(-36.71%)</b></td><td>64.45 <b>(+170.71%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>220.20 (n/a)</td><td>198.80 (n/a)</td><td>203.50 (n/a)</td><td>159.10 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.10 <b>(-21.65%)</b></td><td>0.09 (-17.63%)</td><td>0.10 (-11.15%)</td><td>0.06 (-14.76%)</td><td>0.02 (-18.42%)</td><td>288.90 (+17.30%)</td><td>215.94 <b>(+21.21%)</b></td><td>188.40 (+12.54%)</td><td>181.40 <b>(+27.66%)</b></td><td>46.97 (+15.90%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>246.30 (n/a)</td><td>178.16 (n/a)</td><td>167.40 (n/a)</td><td>142.10 (n/a)</td><td>40.53 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.76 (+7.08%)</td><td>0.56 (+3.46%)</td><td>0.55 (+6.48%)</td><td>0.46 (-2.85%)</td><td>0.12 <b>(+25.12%)</b></td><td>214.30 (+2.93%)</td><td>179.84 (-2.29%)</td><td>179.10 (-6.08%)</td><td>128.70 (-6.60%)</td><td>33.43 <b>(+22.44%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.71 (n/a)</td><td>0.55 (n/a)</td><td>0.52 (n/a)</td><td>0.47 (n/a)</td><td>0.10 (n/a)</td><td>208.20 (n/a)</td><td>184.06 (n/a)</td><td>190.70 (n/a)</td><td>137.80 (n/a)</td><td>27.30 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.79 (+4.14%)</td><td>0.60 (+15.68%)</td><td>0.60 <b>(+26.03%)</b></td><td>0.47 (+15.78%)</td><td>0.12 (-14.48%)</td><td>210.50 (-13.62%)</td><td>167.80 (-15.17%)</td><td>163.20 <b>(-20.66%)</b></td><td>123.70 (-3.96%)</td><td>32.07 <b>(-27.96%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.76 (n/a)</td><td>0.52 (n/a)</td><td>0.48 (n/a)</td><td>0.40 (n/a)</td><td>0.14 (n/a)</td><td>243.70 (n/a)</td><td>197.80 (n/a)</td><td>205.70 (n/a)</td><td>128.80 (n/a)</td><td>44.52 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.79 (-2.77%)</td><td>0.57 (-0.71%)</td><td>0.55 (+6.72%)</td><td>0.27 <b>(-39.53%)</b></td><td>0.20 <b>(+42.19%)</b></td><td>366.20 <b>(+65.33%)</b></td><td>197.72 (+11.44%)</td><td>179.00 (-6.28%)</td><td>124.20 (+2.81%)</td><td>97.80 <b>(+158.23%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.81 (n/a)</td><td>0.58 (n/a)</td><td>0.51 (n/a)</td><td>0.44 (n/a)</td><td>0.14 (n/a)</td><td>221.50 (n/a)</td><td>177.42 (n/a)</td><td>191.00 (n/a)</td><td>120.80 (n/a)</td><td>37.87 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.74 <b>(+25.13%)</b></td><td>0.57 (+11.83%)</td><td>0.55 (+5.39%)</td><td>0.43 (-1.15%)</td><td>0.13 <b>(+104.16%)</b></td><td>226.00 (+1.16%)</td><td>179.68 (-8.12%)</td><td>178.20 (-5.11%)</td><td>133.10 <b>(-20.06%)</b></td><td>38.90 <b>(+63.38%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.59 (n/a)</td><td>0.51 (n/a)</td><td>0.52 (n/a)</td><td>0.44 (n/a)</td><td>0.06 (n/a)</td><td>223.40 (n/a)</td><td>195.56 (n/a)</td><td>187.80 (n/a)</td><td>166.50 (n/a)</td><td>23.81 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.71 (+12.78%)</td><td>0.45 (-9.50%)</td><td>0.44 (-8.55%)</td><td>0.33 (-4.43%)</td><td>0.15 <b>(+32.48%)</b></td><td>221.90 (+4.62%)</td><td>175.54 (+13.66%)</td><td>169.10 (+9.38%)</td><td>103.40 (-11.40%)</td><td>47.65 <b>(+24.41%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.63 (n/a)</td><td>0.50 (n/a)</td><td>0.48 (n/a)</td><td>0.35 (n/a)</td><td>0.12 (n/a)</td><td>212.10 (n/a)</td><td>154.44 (n/a)</td><td>154.60 (n/a)</td><td>116.70 (n/a)</td><td>38.30 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.51 (-8.81%)</td><td>0.42 (-0.01%)</td><td>0.39 (-7.49%)</td><td>0.35 <b>(+21.78%)</b></td><td>0.07 <b>(-34.11%)</b></td><td>213.00 (-17.89%)</td><td>178.68 (-2.94%)</td><td>189.00 (+8.12%)</td><td>145.70 (+9.63%)</td><td>27.39 <b>(-42.59%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.55 (n/a)</td><td>0.42 (n/a)</td><td>0.42 (n/a)</td><td>0.28 (n/a)</td><td>0.10 (n/a)</td><td>259.40 (n/a)</td><td>184.10 (n/a)</td><td>174.80 (n/a)</td><td>132.90 (n/a)</td><td>47.72 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.57 (-0.53%)</td><td>0.42 (-12.01%)</td><td>0.41 (-7.16%)</td><td>0.31 <b>(-21.77%)</b></td><td>0.11 <b>(+23.61%)</b></td><td>239.10 <b>(+27.86%)</b></td><td>186.26 (+16.88%)</td><td>180.80 (+7.68%)</td><td>129.40 (+0.54%)</td><td>48.14 <b>(+66.63%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.57 (n/a)</td><td>0.48 (n/a)</td><td>0.44 (n/a)</td><td>0.39 (n/a)</td><td>0.09 (n/a)</td><td>187.00 (n/a)</td><td>159.36 (n/a)</td><td>167.90 (n/a)</td><td>128.70 (n/a)</td><td>28.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.42 (-19.90%)</td><td>0.38 (-6.57%)</td><td>0.40 (-0.88%)</td><td>0.29 (-15.13%)</td><td>0.05 <b>(-24.95%)</b></td><td>253.30 (+17.81%)</td><td>196.50 (+6.70%)</td><td>186.00 (+0.92%)</td><td>175.50 <b>(+24.82%)</b></td><td>32.46 (+13.56%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.52 (n/a)</td><td>0.41 (n/a)</td><td>0.40 (n/a)</td><td>0.34 (n/a)</td><td>0.07 (n/a)</td><td>215.00 (n/a)</td><td>184.16 (n/a)</td><td>184.30 (n/a)</td><td>140.60 (n/a)</td><td>28.58 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (-3.91%)</td><td>0.21 (-0.49%)</td><td>0.22 (+9.72%)</td><td>0.18 (-7.42%)</td><td>0.03 (+6.70%)</td><td>200.90 (+8.01%)</td><td>174.88 (+0.90%)</td><td>165.10 (-8.83%)</td><td>143.90 (+4.05%)</td><td>24.89 <b>(+25.79%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>186.00 (n/a)</td><td>173.32 (n/a)</td><td>181.10 (n/a)</td><td>138.30 (n/a)</td><td>19.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (-11.79%)</td><td>0.21 (-7.49%)</td><td>0.21 (-6.03%)</td><td>0.16 (-15.80%)</td><td>0.03 (+0.09%)</td><td>231.90 (+18.74%)</td><td>181.60 (+8.73%)</td><td>176.70 (+6.45%)</td><td>151.50 (+13.31%)</td><td>31.53 <b>(+37.37%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.03 (n/a)</td><td>195.30 (n/a)</td><td>167.02 (n/a)</td><td>166.00 (n/a)</td><td>133.70 (n/a)</td><td>22.96 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 <b>(-22.45%)</b></td><td>0.19 (-16.35%)</td><td>0.19 (-12.54%)</td><td>0.12 <b>(-24.31%)</b></td><td>0.04 <b>(-20.15%)</b></td><td>311.60 <b>(+32.09%)</b></td><td>206.96 <b>(+20.40%)</b></td><td>194.40 (+14.35%)</td><td>155.20 <b>(+29.01%)</b></td><td>61.08 <b>(+42.40%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>235.90 (n/a)</td><td>171.90 (n/a)</td><td>170.00 (n/a)</td><td>120.30 (n/a)</td><td>42.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (-15.59%)</td><td>0.22 (-7.23%)</td><td>0.22 (-10.20%)</td><td>0.18 (+1.77%)</td><td>0.02 <b>(-46.03%)</b></td><td>202.80 (-1.74%)</td><td>170.62 (+6.08%)</td><td>164.60 (+11.37%)</td><td>155.60 (+18.51%)</td><td>18.54 <b>(-36.77%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>206.40 (n/a)</td><td>160.84 (n/a)</td><td>147.80 (n/a)</td><td>131.30 (n/a)</td><td>29.32 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.29 (-11.31%)</td><td>0.23 (+9.81%)</td><td>0.22 (+19.34%)</td><td>0.15 (-6.02%)</td><td>0.05 <b>(-22.32%)</b></td><td>240.40 (+6.37%)</td><td>168.86 (-10.12%)</td><td>165.20 (-16.18%)</td><td>128.90 (+12.67%)</td><td>43.31 (+0.31%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.32 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>226.00 (n/a)</td><td>187.88 (n/a)</td><td>197.10 (n/a)</td><td>114.40 (n/a)</td><td>43.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (-18.43%)</td><td>0.20 (-10.30%)</td><td>0.20 (-6.16%)</td><td>0.19 (+5.42%)</td><td>0.01 <b>(-68.46%)</b></td><td>193.80 (-5.14%)</td><td>184.32 (+9.14%)</td><td>185.30 (+6.62%)</td><td>167.20 <b>(+22.58%)</b></td><td>10.84 <b>(-62.62%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>204.30 (n/a)</td><td>168.88 (n/a)</td><td>173.80 (n/a)</td><td>136.40 (n/a)</td><td>29.00 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.30 <b>(+46.49%)</b></td><td>0.21 (+18.98%)</td><td>0.19 (+5.18%)</td><td>0.16 <b>(+28.15%)</b></td><td>0.05 <b>(+84.16%)</b></td><td>224.80 <b>(-21.97%)</b></td><td>183.54 (-14.53%)</td><td>194.40 (-4.94%)</td><td>123.20 <b>(-31.71%)</b></td><td>38.28 (-9.40%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>288.10 (n/a)</td><td>214.74 (n/a)</td><td>204.50 (n/a)</td><td>180.40 (n/a)</td><td>42.25 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.29 <b>(+48.56%)</b></td><td>0.23 <b>(+29.67%)</b></td><td>0.22 <b>(+21.02%)</b></td><td>0.18 (+6.78%)</td><td>0.04 <b>(+238.39%)</b></td><td>207.80 (-6.35%)</td><td>161.82 <b>(-21.02%)</b></td><td>166.00 (-17.37%)</td><td>127.20 <b>(-32.70%)</b></td><td>30.72 <b>(+111.66%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.01 (n/a)</td><td>221.90 (n/a)</td><td>204.90 (n/a)</td><td>200.90 (n/a)</td><td>189.00 (n/a)</td><td>14.52 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.32 (+7.50%)</td><td>0.26 (+2.24%)</td><td>0.26 (+7.39%)</td><td>0.20 (-5.75%)</td><td>0.04 <b>(+38.50%)</b></td><td>199.90 (+6.10%)</td><td>160.66 (-1.19%)</td><td>155.00 (-6.85%)</td><td>127.10 (-7.02%)</td><td>26.51 <b>(+38.23%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.30 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>188.40 (n/a)</td><td>162.60 (n/a)</td><td>166.40 (n/a)</td><td>136.70 (n/a)</td><td>19.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.33 (+19.52%)</td><td>0.28 <b>(+26.43%)</b></td><td>0.28 <b>(+26.86%)</b></td><td>0.21 <b>(+23.88%)</b></td><td>0.05 (-10.35%)</td><td>199.20 (-19.25%)</td><td>150.98 <b>(-22.44%)</b></td><td>145.20 <b>(-21.17%)</b></td><td>125.60 (-16.32%)</td><td>28.64 <b>(-37.98%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>246.70 (n/a)</td><td>194.66 (n/a)</td><td>184.20 (n/a)</td><td>150.10 (n/a)</td><td>46.18 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.32 <b>(+32.37%)</b></td><td>0.24 (+16.97%)</td><td>0.23 (+6.01%)</td><td>0.21 <b>(+33.95%)</b></td><td>0.05 <b>(+50.76%)</b></td><td>190.90 <b>(-25.34%)</b></td><td>172.98 (-14.12%)</td><td>182.00 (-5.65%)</td><td>126.60 <b>(-24.46%)</b></td><td>26.68 (-18.71%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>255.70 (n/a)</td><td>201.42 (n/a)</td><td>192.90 (n/a)</td><td>167.60 (n/a)</td><td>32.81 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.33 (+8.68%)</td><td>0.23 (+0.78%)</td><td>0.22 (-2.85%)</td><td>0.19 (+17.30%)</td><td>0.05 (+3.26%)</td><td>211.40 (-14.76%)</td><td>181.08 (-1.57%)</td><td>188.60 (+2.89%)</td><td>124.80 (-8.03%)</td><td>33.36 <b>(-22.24%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.30 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>248.00 (n/a)</td><td>183.96 (n/a)</td><td>183.30 (n/a)</td><td>135.70 (n/a)</td><td>42.90 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.39 (+18.09%)</td><td>0.26 (-1.37%)</td><td>0.24 (-8.41%)</td><td>0.21 <b>(+25.40%)</b></td><td>0.07 (+8.79%)</td><td>196.70 <b>(-20.27%)</b></td><td>164.16 (+0.05%)</td><td>173.20 (+9.14%)</td><td>105.80 (-15.29%)</td><td>34.79 <b>(-29.73%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.33 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.17 (n/a)</td><td>0.07 (n/a)</td><td>246.70 (n/a)</td><td>164.08 (n/a)</td><td>158.70 (n/a)</td><td>124.90 (n/a)</td><td>49.50 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.26 (-1.65%)</td><td>0.21 (-9.95%)</td><td>0.21 (-12.04%)</td><td>0.17 (-4.30%)</td><td>0.04 (+14.82%)</td><td>237.20 (+4.49%)</td><td>202.08 (+11.72%)</td><td>197.60 (+13.69%)</td><td>156.90 (+1.69%)</td><td>32.87 (+19.95%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>227.00 (n/a)</td><td>180.88 (n/a)</td><td>173.80 (n/a)</td><td>154.30 (n/a)</td><td>27.40 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.32 (-17.16%)</td><td>0.22 (-12.30%)</td><td>0.21 (-10.30%)</td><td>0.18 (-10.54%)</td><td>0.06 <b>(-25.38%)</b></td><td>228.60 (+11.78%)</td><td>191.82 (+12.57%)</td><td>195.50 (+11.46%)</td><td>128.20 <b>(+20.72%)</b></td><td>38.86 (+1.75%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.39 (n/a)</td><td>0.25 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.08 (n/a)</td><td>204.50 (n/a)</td><td>170.40 (n/a)</td><td>175.40 (n/a)</td><td>106.20 (n/a)</td><td>38.19 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.29 <b>(+26.12%)</b></td><td>0.24 (+15.59%)</td><td>0.24 (+14.74%)</td><td>0.18 (+2.99%)</td><td>0.04 <b>(+73.25%)</b></td><td>228.20 (-2.89%)</td><td>173.82 (-12.19%)</td><td>167.60 (-12.84%)</td><td>139.20 <b>(-20.68%)</b></td><td>32.91 <b>(+37.51%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>235.00 (n/a)</td><td>197.96 (n/a)</td><td>192.30 (n/a)</td><td>175.50 (n/a)</td><td>23.93 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (-0.82%)</td><td>0.20 (-1.94%)</td><td>0.19 (-5.42%)</td><td>0.16 (+4.48%)</td><td>0.03 (-8.22%)</td><td>215.80 (-4.26%)</td><td>180.82 (+1.47%)</td><td>182.00 (+5.75%)</td><td>140.60 (+0.79%)</td><td>27.49 (-13.46%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>225.40 (n/a)</td><td>178.20 (n/a)</td><td>172.10 (n/a)</td><td>139.50 (n/a)</td><td>31.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.24 (-1.99%)</td><td>0.19 (-8.94%)</td><td>0.18 (-5.14%)</td><td>0.16 (-16.41%)</td><td>0.03 <b>(+22.20%)</b></td><td>218.90 (+19.62%)</td><td>185.86 (+10.58%)</td><td>188.60 (+5.42%)</td><td>147.70 (+2.00%)</td><td>25.48 <b>(+44.99%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>183.00 (n/a)</td><td>168.08 (n/a)</td><td>178.90 (n/a)</td><td>144.80 (n/a)</td><td>17.58 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.23 <b>(-21.74%)</b></td><td>0.20 (-9.32%)</td><td>0.21 (+2.17%)</td><td>0.15 (+4.84%)</td><td>0.03 <b>(-47.05%)</b></td><td>225.40 (-4.61%)</td><td>179.08 (+6.52%)</td><td>166.90 (-2.11%)</td><td>154.60 <b>(+27.77%)</b></td><td>29.12 <b>(-34.97%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.05 (n/a)</td><td>236.30 (n/a)</td><td>168.12 (n/a)</td><td>170.50 (n/a)</td><td>121.00 (n/a)</td><td>44.79 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 (-12.11%)</td><td>0.20 (+1.48%)</td><td>0.19 (-1.18%)</td><td>0.15 <b>(+30.27%)</b></td><td>0.04 <b>(-44.99%)</b></td><td>224.90 <b>(-23.24%)</b></td><td>179.90 (-7.76%)</td><td>180.20 (+1.18%)</td><td>136.90 (+13.80%)</td><td>31.23 <b>(-52.99%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.29 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>293.00 (n/a)</td><td>195.04 (n/a)</td><td>178.10 (n/a)</td><td>120.30 (n/a)</td><td>66.43 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.27 (-10.05%)</td><td>0.23 (+15.13%)</td><td>0.23 <b>(+25.33%)</b></td><td>0.20 <b>(+29.11%)</b></td><td>0.03 <b>(-44.85%)</b></td><td>174.30 <b>(-22.53%)</b></td><td>152.82 (-16.46%)</td><td>153.10 <b>(-20.22%)</b></td><td>127.30 (+11.18%)</td><td>21.24 <b>(-49.30%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>225.00 (n/a)</td><td>182.94 (n/a)</td><td>191.90 (n/a)</td><td>114.50 (n/a)</td><td>41.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.27 (-9.79%)</td><td>0.22 (+6.91%)</td><td>0.19 (+4.83%)</td><td>0.16 (+12.93%)</td><td>0.05 (-15.86%)</td><td>211.10 (-11.45%)</td><td>166.90 (-7.97%)</td><td>179.30 (-4.58%)</td><td>127.40 (+10.88%)</td><td>36.97 (-17.51%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.30 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>238.40 (n/a)</td><td>181.36 (n/a)</td><td>187.90 (n/a)</td><td>114.90 (n/a)</td><td>44.82 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.25 <b>(+21.31%)</b></td><td>0.19 (+1.64%)</td><td>0.18 (-7.34%)</td><td>0.17 (+10.87%)</td><td>0.03 <b>(+54.58%)</b></td><td>200.90 (-9.79%)</td><td>183.26 (-0.93%)</td><td>189.50 (+7.92%)</td><td>141.40 (-17.55%)</td><td>23.98 (+11.26%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>222.70 (n/a)</td><td>184.98 (n/a)</td><td>175.60 (n/a)</td><td>171.50 (n/a)</td><td>21.55 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.22 (-1.49%)</td><td>0.20 (-4.30%)</td><td>0.20 (-7.36%)</td><td>0.17 (-6.16%)</td><td>0.02 <b>(+33.88%)</b></td><td>203.20 (+6.55%)</td><td>178.88 (+4.98%)</td><td>178.20 (+7.93%)</td><td>157.10 (+1.49%)</td><td>19.94 <b>(+43.36%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>190.70 (n/a)</td><td>170.40 (n/a)</td><td>165.10 (n/a)</td><td>154.80 (n/a)</td><td>13.91 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.88 (-10.89%)</td><td>0.73 (-5.18%)</td><td>0.70 (-4.25%)</td><td>0.55 <b>(-20.49%)</b></td><td>0.14 (+11.50%)</td><td>240.10 <b>(+25.77%)</b></td><td>185.18 (+6.81%)</td><td>186.30 (+4.43%)</td><td>149.30 (+12.26%)</td><td>36.74 <b>(+58.14%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.99 (n/a)</td><td>0.77 (n/a)</td><td>0.73 (n/a)</td><td>0.69 (n/a)</td><td>0.12 (n/a)</td><td>190.90 (n/a)</td><td>173.38 (n/a)</td><td>178.40 (n/a)</td><td>133.00 (n/a)</td><td>23.23 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.01 (+0.92%)</td><td>0.78 (+7.04%)</td><td>0.71 (-0.72%)</td><td>0.50 (-10.66%)</td><td>0.21 <b>(+24.36%)</b></td><td>261.30 (+11.95%)</td><td>179.82 (-4.16%)</td><td>183.70 (+0.77%)</td><td>130.20 (-0.91%)</td><td>52.76 <b>(+36.29%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.00 (n/a)</td><td>0.73 (n/a)</td><td>0.72 (n/a)</td><td>0.56 (n/a)</td><td>0.17 (n/a)</td><td>233.40 (n/a)</td><td>187.62 (n/a)</td><td>182.30 (n/a)</td><td>131.40 (n/a)</td><td>38.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.99 (+7.88%)</td><td>0.73 (-2.72%)</td><td>0.71 (-0.45%)</td><td>0.45 <b>(-24.13%)</b></td><td>0.21 <b>(+58.00%)</b></td><td>292.20 <b>(+31.80%)</b></td><td>193.80 (+7.95%)</td><td>183.60 (+0.44%)</td><td>132.10 (-7.30%)</td><td>62.13 <b>(+97.16%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.92 (n/a)</td><td>0.75 (n/a)</td><td>0.72 (n/a)</td><td>0.59 (n/a)</td><td>0.13 (n/a)</td><td>221.70 (n/a)</td><td>179.52 (n/a)</td><td>182.80 (n/a)</td><td>142.50 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-1.55%)</td><td>0.03 (-0.24%)</td><td>0.03 (-10.69%)</td><td>0.02 (+7.85%)</td><td>0.00 (-9.04%)</td><td>164.50 (-7.27%)</td><td>150.82 (-0.05%)</td><td>161.60 (+11.99%)</td><td>128.50 (+1.58%)</td><td>16.99 (-14.00%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.40 (n/a)</td><td>150.90 (n/a)</td><td>144.30 (n/a)</td><td>126.50 (n/a)</td><td>19.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (+0.11%)</td><td>0.02 (-9.69%)</td><td>0.02 (-11.39%)</td><td>0.02 <b>(-22.90%)</b></td><td>0.01 (+9.51%)</td><td>261.80 <b>(+29.73%)</b></td><td>187.84 (+12.90%)</td><td>195.80 (+12.85%)</td><td>125.20 (-0.08%)</td><td>50.76 <b>(+40.17%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>166.38 (n/a)</td><td>173.50 (n/a)</td><td>125.30 (n/a)</td><td>36.21 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-8.98%)</td><td>0.03 (-0.18%)</td><td>0.02 (-3.14%)</td><td>0.02 <b>(+30.86%)</b></td><td>0.00 <b>(-55.13%)</b></td><td>176.80 <b>(-23.60%)</b></td><td>161.78 (-3.00%)</td><td>163.90 (+3.21%)</td><td>140.00 (+9.89%)</td><td>14.12 <b>(-63.93%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.40 (n/a)</td><td>166.78 (n/a)</td><td>158.80 (n/a)</td><td>127.40 (n/a)</td><td>39.13 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>16.96 (+10.97%)</td><td>13.05 (-4.74%)</td><td>12.67 (-12.85%)</td><td>7.89 <b>(-29.42%)</b></td><td>3.49 <b>(+108.15%)</b></td><td>265.90 <b>(+41.66%)</b></td><td>172.42 (+11.11%)</td><td>165.60 (+14.76%)</td><td>123.70 (-9.91%)</td><td>55.97 <b>(+170.63%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>15.28 (n/a)</td><td>13.70 (n/a)</td><td>14.54 (n/a)</td><td>11.18 (n/a)</td><td>1.68 (n/a)</td><td>187.70 (n/a)</td><td>155.18 (n/a)</td><td>144.30 (n/a)</td><td>137.30 (n/a)</td><td>20.68 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.05 (+2.76%)</td><td>0.91 (+2.09%)</td><td>0.95 (+9.51%)</td><td>0.77 (-2.80%)</td><td>0.13 <b>(+27.99%)</b></td><td>171.30 (+2.88%)</td><td>147.40 (-1.38%)</td><td>139.40 (-8.71%)</td><td>125.80 (-2.63%)</td><td>21.78 <b>(+30.33%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.02 (n/a)</td><td>0.89 (n/a)</td><td>0.87 (n/a)</td><td>0.79 (n/a)</td><td>0.10 (n/a)</td><td>166.50 (n/a)</td><td>149.46 (n/a)</td><td>152.70 (n/a)</td><td>129.20 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.06 (+16.06%)</td><td>0.91 (+11.84%)</td><td>0.96 (+17.14%)</td><td>0.63 (-12.68%)</td><td>0.18 <b>(+144.57%)</b></td><td>210.50 (+14.53%)</td><td>150.92 (-7.77%)</td><td>137.10 (-14.63%)</td><td>124.20 (-13.87%)</td><td>35.66 <b>(+142.36%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.92 (n/a)</td><td>0.81 (n/a)</td><td>0.82 (n/a)</td><td>0.72 (n/a)</td><td>0.07 (n/a)</td><td>183.80 (n/a)</td><td>163.64 (n/a)</td><td>160.60 (n/a)</td><td>144.20 (n/a)</td><td>14.71 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.09 (+1.58%)</td><td>0.87 (+3.44%)</td><td>0.87 (+10.72%)</td><td>0.61 (-17.53%)</td><td>0.19 <b>(+38.79%)</b></td><td>216.70 <b>(+21.26%)</b></td><td>158.72 (-1.04%)</td><td>152.00 (-9.69%)</td><td>121.60 (-1.54%)</td><td>38.01 <b>(+65.39%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.07 (n/a)</td><td>0.84 (n/a)</td><td>0.79 (n/a)</td><td>0.74 (n/a)</td><td>0.14 (n/a)</td><td>178.70 (n/a)</td><td>160.38 (n/a)</td><td>168.30 (n/a)</td><td>123.50 (n/a)</td><td>22.98 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>1.06 <b>(+22.42%)</b></td><td>0.94 <b>(+35.78%)</b></td><td>0.93 <b>(+31.59%)</b></td><td>0.82 <b>(+60.18%)</b></td><td>0.09 <b>(-30.77%)</b></td><td>160.90 <b>(-37.56%)</b></td><td>141.50 <b>(-27.94%)</b></td><td>142.60 <b>(-24.03%)</b></td><td>124.40 (-18.32%)</td><td>13.38 <b>(-65.31%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.87 (n/a)</td><td>0.69 (n/a)</td><td>0.70 (n/a)</td><td>0.51 (n/a)</td><td>0.13 (n/a)</td><td>257.70 (n/a)</td><td>196.36 (n/a)</td><td>187.70 (n/a)</td><td>152.30 (n/a)</td><td>38.58 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.96 (-3.30%)</td><td>0.82 (+10.44%)</td><td>0.82 <b>(+33.82%)</b></td><td>0.63 (+8.32%)</td><td>0.13 <b>(-36.65%)</b></td><td>211.00 (-7.66%)</td><td>163.68 (-12.44%)</td><td>160.20 <b>(-25.28%)</b></td><td>137.00 (+3.40%)</td><td>28.75 <b>(-38.06%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.00 (n/a)</td><td>0.75 (n/a)</td><td>0.62 (n/a)</td><td>0.58 (n/a)</td><td>0.20 (n/a)</td><td>228.50 (n/a)</td><td>186.94 (n/a)</td><td>214.40 (n/a)</td><td>132.50 (n/a)</td><td>46.41 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-3.84%)</td><td>0.03 (+1.63%)</td><td>0.03 (+7.36%)</td><td>0.02 (+8.39%)</td><td>0.00 (-18.75%)</td><td>166.20 (-7.72%)</td><td>143.12 (-2.35%)</td><td>132.90 (-6.87%)</td><td>126.00 (+3.96%)</td><td>19.15 <b>(-21.09%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>180.10 (n/a)</td><td>146.56 (n/a)</td><td>142.70 (n/a)</td><td>121.20 (n/a)</td><td>24.27 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.03 (-1.14%)</td><td>0.02 (-12.08%)</td><td>0.02 (-6.01%)</td><td>0.02 <b>(-22.27%)</b></td><td>0.00 <b>(+31.44%)</b></td><td>205.30 <b>(+28.63%)</b></td><td>168.08 (+15.17%)</td><td>165.80 (+6.35%)</td><td>128.90 (+1.18%)</td><td>27.86 <b>(+69.49%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>159.60 (n/a)</td><td>145.94 (n/a)</td><td>155.90 (n/a)</td><td>127.40 (n/a)</td><td>16.44 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.00 (+2.27%)</td><td>0.00 (+0.47%)</td><td>0.00 (+0.00%)</td><td>0.00 (-2.50%)</td><td>0.00 <b>(+51.80%)</b></td><td>1041.51 (+1.24%)</td><td>965.28 (-0.52%)</td><td>945.12 (-1.90%)</td><td>920.41 (-2.05%)</td><td>48.95 <b>(+39.61%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1028.73 (n/a)</td><td>970.29 (n/a)</td><td>963.46 (n/a)</td><td>939.64 (n/a)</td><td>35.06 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.01 (+1.22%)</td><td>0.01 (+1.51%)</td><td>0.01 (-1.23%)</td><td>0.01 (+6.76%)</td><td>0.00 <b>(-48.80%)</b></td><td>1040.29 (-6.51%)</td><td>1012.30 (-1.95%)</td><td>1018.67 (+0.20%)</td><td>986.32 (-0.76%)</td><td>21.42 <b>(-53.79%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1112.72 (n/a)</td><td>1032.39 (n/a)</td><td>1016.68 (n/a)</td><td>993.88 (n/a)</td><td>46.36 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.95 (-3.63%)</td><td>0.95 (-1.26%)</td><td>0.95 (-0.86%)</td><td>0.95 (+0.11%)</td><td>0.00 <b>(-85.33%)</b></td><td>2208.45 (-0.10%)</td><td>2201.89 (+1.26%)</td><td>2200.34 (+0.87%)</td><td>2195.91 (+3.77%)</td><td>5.36 <b>(-84.66%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.99 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.02 (n/a)</td><td>2210.71 (n/a)</td><td>2174.49 (n/a)</td><td>2181.45 (n/a)</td><td>2116.17 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>5.62 (-3.63%)</td><td>4.53 (-6.31%)</td><td>4.63 (-16.42%)</td><td>3.27 (-10.01%)</td><td>0.85 <b>(-23.02%)</b></td><td>321.00 (+11.15%)</td><td>238.62 (+5.19%)</td><td>226.40 (+19.66%)</td><td>186.70 (+3.72%)</td><td>49.96 (-10.59%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>5.83 (n/a)</td><td>4.84 (n/a)</td><td>5.54 (n/a)</td><td>3.63 (n/a)</td><td>1.10 (n/a)</td><td>288.80 (n/a)</td><td>226.84 (n/a)</td><td>189.20 (n/a)</td><td>180.00 (n/a)</td><td>55.87 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>5.97 (+4.21%)</td><td>4.53 (-0.89%)</td><td>4.50 (-2.49%)</td><td>2.81 <b>(-23.13%)</b></td><td>1.16 <b>(+44.05%)</b></td><td>372.80 <b>(+30.08%)</b></td><td>246.28 (+4.85%)</td><td>232.80 (+2.56%)</td><td>175.70 (-4.04%)</td><td>75.44 <b>(+86.45%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>5.73 (n/a)</td><td>4.57 (n/a)</td><td>4.62 (n/a)</td><td>3.66 (n/a)</td><td>0.80 (n/a)</td><td>286.60 (n/a)</td><td>234.88 (n/a)</td><td>227.00 (n/a)</td><td>183.10 (n/a)</td><td>40.46 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>6.16 (+17.54%)</td><td>5.37 (+8.53%)</td><td>5.95 (+16.70%)</td><td>4.03 (-5.50%)</td><td>0.96 <b>(+145.76%)</b></td><td>260.10 (+5.82%)</td><td>200.86 (-5.71%)</td><td>176.30 (-14.29%)</td><td>170.10 (-14.91%)</td><td>39.74 <b>(+113.90%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>5.24 (n/a)</td><td>4.95 (n/a)</td><td>5.10 (n/a)</td><td>4.27 (n/a)</td><td>0.39 (n/a)</td><td>245.80 (n/a)</td><td>213.02 (n/a)</td><td>205.70 (n/a)</td><td>199.90 (n/a)</td><td>18.58 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>6.07 (-7.23%)</td><td>5.64 (+3.62%)</td><td>5.58 (+5.69%)</td><td>5.36 (+15.77%)</td><td>0.26 <b>(-62.36%)</b></td><td>195.70 (-13.64%)</td><td>186.22 (-4.54%)</td><td>187.90 (-5.39%)</td><td>172.80 (+7.80%)</td><td>8.41 <b>(-64.86%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>6.54 (n/a)</td><td>5.44 (n/a)</td><td>5.28 (n/a)</td><td>4.63 (n/a)</td><td>0.70 (n/a)</td><td>226.60 (n/a)</td><td>195.08 (n/a)</td><td>198.60 (n/a)</td><td>160.30 (n/a)</td><td>23.93 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>9.12 (+0.27%)</td><td>8.22 (+2.90%)</td><td>8.70 (+11.92%)</td><td>5.94 (-19.14%)</td><td>1.31 <b>(+90.04%)</b></td><td>352.80 <b>(+23.66%)</b></td><td>261.70 (-0.89%)</td><td>241.10 (-10.67%)</td><td>230.00 (-0.26%)</td><td>51.65 <b>(+140.47%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>9.09 (n/a)</td><td>7.99 (n/a)</td><td>7.77 (n/a)</td><td>7.35 (n/a)</td><td>0.69 (n/a)</td><td>285.30 (n/a)</td><td>264.04 (n/a)</td><td>269.90 (n/a)</td><td>230.60 (n/a)</td><td>21.48 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>9.12 (+6.29%)</td><td>8.14 (+3.03%)</td><td>7.64 (-5.30%)</td><td>7.32 (+8.42%)</td><td>0.86 <b>(+26.68%)</b></td><td>286.30 (-7.76%)</td><td>260.04 (-2.72%)</td><td>274.60 (+5.62%)</td><td>229.90 (-5.89%)</td><td>26.62 (+6.01%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.58 (n/a)</td><td>7.90 (n/a)</td><td>8.06 (n/a)</td><td>6.76 (n/a)</td><td>0.68 (n/a)</td><td>310.40 (n/a)</td><td>267.32 (n/a)</td><td>260.00 (n/a)</td><td>244.30 (n/a)</td><td>25.11 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>9.53 (+8.93%)</td><td>8.23 (+12.08%)</td><td>7.84 (+4.86%)</td><td>7.72 <b>(+30.32%)</b></td><td>0.77 <b>(-29.70%)</b></td><td>271.70 <b>(-23.27%)</b></td><td>256.50 (-11.83%)</td><td>267.50 (-4.63%)</td><td>220.00 (-8.18%)</td><td>21.97 <b>(-50.77%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.75 (n/a)</td><td>7.34 (n/a)</td><td>7.48 (n/a)</td><td>5.92 (n/a)</td><td>1.10 (n/a)</td><td>354.10 (n/a)</td><td>290.90 (n/a)</td><td>280.50 (n/a)</td><td>239.60 (n/a)</td><td>44.64 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>9.82 (+5.66%)</td><td>8.86 (+4.79%)</td><td>8.61 (+2.36%)</td><td>8.00 (+5.96%)</td><td>0.88 <b>(+38.60%)</b></td><td>262.10 (-5.62%)</td><td>238.48 (-4.25%)</td><td>243.70 (-2.29%)</td><td>213.70 (-5.32%)</td><td>23.34 <b>(+21.87%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>9.29 (n/a)</td><td>8.46 (n/a)</td><td>8.41 (n/a)</td><td>7.55 (n/a)</td><td>0.64 (n/a)</td><td>277.70 (n/a)</td><td>249.06 (n/a)</td><td>249.40 (n/a)</td><td>225.70 (n/a)</td><td>19.15 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>10.97 (+19.70%)</td><td>9.66 <b>(+24.79%)</b></td><td>10.15 <b>(+30.07%)</b></td><td>7.61 (+15.37%)</td><td>1.38 <b>(+32.63%)</b></td><td>275.60 (-13.31%)</td><td>221.06 (-19.57%)</td><td>206.60 <b>(-23.14%)</b></td><td>191.10 (-16.48%)</td><td>34.65 (-4.51%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>9.17 (n/a)</td><td>7.74 (n/a)</td><td>7.80 (n/a)</td><td>6.60 (n/a)</td><td>1.04 (n/a)</td><td>317.90 (n/a)</td><td>274.84 (n/a)</td><td>268.80 (n/a)</td><td>228.80 (n/a)</td><td>36.28 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>9.72 (+10.09%)</td><td>8.87 (+8.71%)</td><td>8.72 (+4.89%)</td><td>8.07 (+14.56%)</td><td>0.64 (-6.39%)</td><td>259.80 (-12.73%)</td><td>237.54 (-8.19%)</td><td>240.40 (-4.68%)</td><td>215.90 (-9.13%)</td><td>17.13 <b>(-27.14%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.82 (n/a)</td><td>8.16 (n/a)</td><td>8.32 (n/a)</td><td>7.05 (n/a)</td><td>0.69 (n/a)</td><td>297.70 (n/a)</td><td>258.72 (n/a)</td><td>252.20 (n/a)</td><td>237.60 (n/a)</td><td>23.51 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.38 (+5.29%)</td><td>11.57 (-0.41%)</td><td>11.18 (+1.30%)</td><td>9.51 (-12.41%)</td><td>1.58 <b>(+63.71%)</b></td><td>441.20 (+14.15%)</td><td>367.96 (+1.41%)</td><td>375.20 (-1.29%)</td><td>313.40 (-5.03%)</td><td>51.34 <b>(+75.55%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>12.71 (n/a)</td><td>11.62 (n/a)</td><td>11.04 (n/a)</td><td>10.85 (n/a)</td><td>0.96 (n/a)</td><td>386.50 (n/a)</td><td>362.86 (n/a)</td><td>380.10 (n/a)</td><td>330.00 (n/a)</td><td>29.24 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.84 (+1.96%)</td><td>11.48 (-3.08%)</td><td>11.54 (-3.11%)</td><td>9.44 (-10.84%)</td><td>1.58 <b>(+23.66%)</b></td><td>444.30 (+12.14%)</td><td>370.96 (+3.77%)</td><td>363.60 (+3.21%)</td><td>303.00 (-1.91%)</td><td>50.57 <b>(+32.94%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>13.58 (n/a)</td><td>11.84 (n/a)</td><td>11.91 (n/a)</td><td>10.59 (n/a)</td><td>1.28 (n/a)</td><td>396.20 (n/a)</td><td>357.48 (n/a)</td><td>352.30 (n/a)</td><td>308.90 (n/a)</td><td>38.04 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.10 (-1.58%)</td><td>11.74 (+1.28%)</td><td>11.90 (-1.04%)</td><td>9.96 (+7.20%)</td><td>1.13 <b>(-23.68%)</b></td><td>421.10 (-6.71%)</td><td>360.08 (-1.89%)</td><td>352.40 (+1.06%)</td><td>320.30 (+1.62%)</td><td>37.03 <b>(-27.88%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>13.31 (n/a)</td><td>11.59 (n/a)</td><td>12.03 (n/a)</td><td>9.29 (n/a)</td><td>1.48 (n/a)</td><td>451.40 (n/a)</td><td>367.00 (n/a)</td><td>348.70 (n/a)</td><td>315.20 (n/a)</td><td>51.34 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>15.21 (-0.56%)</td><td>13.28 (-0.17%)</td><td>12.68 (-4.63%)</td><td>12.07 (+2.55%)</td><td>1.29 (+0.23%)</td><td>347.50 (-2.50%)</td><td>318.06 (+0.16%)</td><td>330.90 (+4.85%)</td><td>275.80 (+0.55%)</td><td>29.42 (-1.11%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>15.29 (n/a)</td><td>13.30 (n/a)</td><td>13.29 (n/a)</td><td>11.77 (n/a)</td><td>1.29 (n/a)</td><td>356.40 (n/a)</td><td>317.56 (n/a)</td><td>315.60 (n/a)</td><td>274.30 (n/a)</td><td>29.75 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>14.70 (+0.83%)</td><td>12.95 (-1.71%)</td><td>13.40 (+4.27%)</td><td>11.30 (-8.69%)</td><td>1.44 <b>(+59.94%)</b></td><td>371.20 (+9.53%)</td><td>327.06 (+2.41%)</td><td>313.00 (-4.11%)</td><td>285.30 (-0.80%)</td><td>36.83 <b>(+76.41%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>14.58 (n/a)</td><td>13.18 (n/a)</td><td>12.85 (n/a)</td><td>12.38 (n/a)</td><td>0.90 (n/a)</td><td>338.90 (n/a)</td><td>319.36 (n/a)</td><td>326.40 (n/a)</td><td>287.60 (n/a)</td><td>20.88 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>15.74 (+17.32%)</td><td>13.40 (+8.62%)</td><td>13.67 (+11.78%)</td><td>9.92 (-14.63%)</td><td>2.18 <b>(+231.13%)</b></td><td>422.90 (+17.15%)</td><td>320.66 (-5.86%)</td><td>306.90 (-10.55%)</td><td>266.50 (-14.77%)</td><td>60.40 <b>(+245.01%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>13.41 (n/a)</td><td>12.34 (n/a)</td><td>12.23 (n/a)</td><td>11.62 (n/a)</td><td>0.66 (n/a)</td><td>361.00 (n/a)</td><td>340.62 (n/a)</td><td>343.10 (n/a)</td><td>312.70 (n/a)</td><td>17.51 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>15.16 (+4.54%)</td><td>13.07 (+0.55%)</td><td>12.72 (-0.90%)</td><td>10.79 (-9.75%)</td><td>1.63 <b>(+74.77%)</b></td><td>388.90 (+10.80%)</td><td>325.18 (+0.35%)</td><td>329.70 (+0.92%)</td><td>276.70 (-4.36%)</td><td>42.01 <b>(+88.46%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>14.50 (n/a)</td><td>12.99 (n/a)</td><td>12.84 (n/a)</td><td>11.95 (n/a)</td><td>0.93 (n/a)</td><td>351.00 (n/a)</td><td>324.06 (n/a)</td><td>326.70 (n/a)</td><td>289.30 (n/a)</td><td>22.29 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>13.27 (+3.91%)</td><td>10.76 (-14.29%)</td><td>10.00 <b>(-20.53%)</b></td><td>9.29 <b>(-24.59%)</b></td><td>1.61 <b>(+681.65%)</b></td><td>451.30 <b>(+32.62%)</b></td><td>396.28 (+18.58%)</td><td>419.40 <b>(+25.83%)</b></td><td>316.00 (-3.78%)</td><td>54.18 <b>(+889.83%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>12.77 (n/a)</td><td>12.55 (n/a)</td><td>12.58 (n/a)</td><td>12.32 (n/a)</td><td>0.21 (n/a)</td><td>340.30 (n/a)</td><td>334.20 (n/a)</td><td>333.30 (n/a)</td><td>328.40 (n/a)</td><td>5.47 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.04 (+0.04%)</td><td>2.67 (+3.11%)</td><td>2.81 (+7.51%)</td><td>2.31 (+11.45%)</td><td>0.33 (-6.80%)</td><td>227.00 (-10.28%)</td><td>198.88 (-3.34%)</td><td>186.70 (-6.98%)</td><td>172.40 (-0.06%)</td><td>25.41 (-15.49%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.04 (n/a)</td><td>2.59 (n/a)</td><td>2.61 (n/a)</td><td>2.07 (n/a)</td><td>0.36 (n/a)</td><td>253.00 (n/a)</td><td>205.76 (n/a)</td><td>200.70 (n/a)</td><td>172.50 (n/a)</td><td>30.06 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>5.54 (+4.82%)</td><td>4.90 (-2.31%)</td><td>5.01 (-1.61%)</td><td>3.83 (-14.22%)</td><td>0.68 <b>(+105.02%)</b></td><td>273.80 (+16.56%)</td><td>217.84 (+3.78%)</td><td>209.50 (+1.65%)</td><td>189.20 (-4.59%)</td><td>34.02 <b>(+128.44%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>5.29 (n/a)</td><td>5.01 (n/a)</td><td>5.09 (n/a)</td><td>4.46 (n/a)</td><td>0.33 (n/a)</td><td>234.90 (n/a)</td><td>209.90 (n/a)</td><td>206.10 (n/a)</td><td>198.30 (n/a)</td><td>14.89 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>8.20 (-5.76%)</td><td>7.30 (-4.68%)</td><td>7.17 (-3.19%)</td><td>6.59 (+0.19%)</td><td>0.70 <b>(-27.85%)</b></td><td>318.20 (-0.19%)</td><td>289.52 (+4.35%)</td><td>292.50 (+3.32%)</td><td>255.90 (+6.14%)</td><td>27.40 <b>(-21.53%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.70 (n/a)</td><td>7.66 (n/a)</td><td>7.41 (n/a)</td><td>6.58 (n/a)</td><td>0.97 (n/a)</td><td>318.80 (n/a)</td><td>277.46 (n/a)</td><td>283.10 (n/a)</td><td>241.10 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>3.29 (+14.79%)</td><td>2.89 (+9.41%)</td><td>2.91 (+7.43%)</td><td>2.51 (+13.37%)</td><td>0.28 (+13.99%)</td><td>208.70 (-11.79%)</td><td>182.72 (-8.62%)</td><td>180.40 (-6.91%)</td><td>159.40 (-12.90%)</td><td>18.03 (-14.21%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>2.86 (n/a)</td><td>2.64 (n/a)</td><td>2.71 (n/a)</td><td>2.22 (n/a)</td><td>0.25 (n/a)</td><td>236.60 (n/a)</td><td>199.96 (n/a)</td><td>193.80 (n/a)</td><td>183.00 (n/a)</td><td>21.01 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.20 (-16.45%)</td><td>0.17 (-16.07%)</td><td>0.18 (-7.80%)</td><td>0.14 (-16.43%)</td><td>0.02 <b>(-25.84%)</b></td><td>231.50 (+19.64%)</td><td>192.14 (+18.78%)</td><td>182.10 (+8.46%)</td><td>165.80 (+19.62%)</td><td>25.50 (+10.57%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>193.50 (n/a)</td><td>161.76 (n/a)</td><td>167.90 (n/a)</td><td>138.60 (n/a)</td><td>23.06 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.23 (-2.79%)</td><td>0.21 (+6.62%)</td><td>0.22 (+10.30%)</td><td>0.19 (+8.86%)</td><td>0.02 <b>(-30.23%)</b></td><td>173.80 (-8.14%)</td><td>153.36 (-6.62%)</td><td>149.20 (-9.30%)</td><td>144.30 (+2.92%)</td><td>11.67 <b>(-32.79%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>189.20 (n/a)</td><td>164.24 (n/a)</td><td>164.50 (n/a)</td><td>140.20 (n/a)</td><td>17.36 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.46 (-1.31%)</td><td>0.37 (-9.62%)</td><td>0.40 (-4.97%)</td><td>0.17 <b>(-44.83%)</b></td><td>0.11 <b>(+88.06%)</b></td><td>376.60 <b>(+81.23%)</b></td><td>201.76 <b>(+22.95%)</b></td><td>164.40 (+5.18%)</td><td>141.00 (+1.37%)</td><td>98.26 <b>(+267.13%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.47 (n/a)</td><td>0.41 (n/a)</td><td>0.42 (n/a)</td><td>0.32 (n/a)</td><td>0.06 (n/a)</td><td>207.80 (n/a)</td><td>164.10 (n/a)</td><td>156.30 (n/a)</td><td>139.10 (n/a)</td><td>26.76 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.46 (+11.80%)</td><td>0.39 (+1.34%)</td><td>0.38 (-2.68%)</td><td>0.33 (-3.84%)</td><td>0.05 <b>(+82.51%)</b></td><td>198.60 (+3.98%)</td><td>168.28 (-0.48%)</td><td>171.20 (+2.76%)</td><td>142.20 (-10.57%)</td><td>21.34 <b>(+67.45%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.41 (n/a)</td><td>0.39 (n/a)</td><td>0.39 (n/a)</td><td>0.34 (n/a)</td><td>0.03 (n/a)</td><td>191.00 (n/a)</td><td>169.10 (n/a)</td><td>166.60 (n/a)</td><td>159.00 (n/a)</td><td>12.74 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.43 <b>(-20.46%)</b></td><td>0.40 (-9.88%)</td><td>0.40 (-14.36%)</td><td>0.35 (+5.60%)</td><td>0.03 <b>(-69.19%)</b></td><td>184.90 (-5.33%)</td><td>165.42 (+7.61%)</td><td>164.20 (+16.79%)</td><td>152.40 <b>(+25.74%)</b></td><td>11.95 <b>(-63.34%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.54 (n/a)</td><td>0.44 (n/a)</td><td>0.47 (n/a)</td><td>0.34 (n/a)</td><td>0.09 (n/a)</td><td>195.30 (n/a)</td><td>153.72 (n/a)</td><td>140.60 (n/a)</td><td>121.20 (n/a)</td><td>32.60 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.80 (-6.51%)</td><td>0.74 (+3.00%)</td><td>0.77 (+8.57%)</td><td>0.59 (-3.03%)</td><td>0.08 (-6.54%)</td><td>221.00 (+3.13%)</td><td>178.62 (-2.93%)</td><td>169.40 (-7.93%)</td><td>163.70 (+6.92%)</td><td>23.83 (+5.97%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.86 (n/a)</td><td>0.72 (n/a)</td><td>0.71 (n/a)</td><td>0.61 (n/a)</td><td>0.09 (n/a)</td><td>214.30 (n/a)</td><td>184.02 (n/a)</td><td>184.00 (n/a)</td><td>153.10 (n/a)</td><td>22.49 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.72 (-3.44%)</td><td>0.65 (-7.32%)</td><td>0.65 (-8.32%)</td><td>0.56 (-9.99%)</td><td>0.07 <b>(+50.35%)</b></td><td>234.90 (+11.06%)</td><td>203.88 (+8.59%)</td><td>200.70 (+9.08%)</td><td>180.90 (+3.61%)</td><td>23.41 <b>(+67.72%)</b></td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.75 (n/a)</td><td>0.70 (n/a)</td><td>0.71 (n/a)</td><td>0.62 (n/a)</td><td>0.05 (n/a)</td><td>211.50 (n/a)</td><td>187.76 (n/a)</td><td>184.00 (n/a)</td><td>174.60 (n/a)</td><td>13.96 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.91 (+14.46%)</td><td>0.78 (+12.68%)</td><td>0.77 (+9.80%)</td><td>0.66 (+11.15%)</td><td>0.10 <b>(+23.63%)</b></td><td>198.80 (-10.05%)</td><td>170.98 (-11.08%)</td><td>171.00 (-8.95%)</td><td>143.70 (-12.59%)</td><td>20.87 (-3.48%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.80 (n/a)</td><td>0.69 (n/a)</td><td>0.70 (n/a)</td><td>0.59 (n/a)</td><td>0.08 (n/a)</td><td>221.00 (n/a)</td><td>192.28 (n/a)</td><td>187.80 (n/a)</td><td>164.40 (n/a)</td><td>21.63 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.73 (-6.18%)</td><td>0.66 (-5.41%)</td><td>0.66 (-10.26%)</td><td>0.57 (-2.62%)</td><td>0.06 <b>(-24.85%)</b></td><td>231.90 (+2.70%)</td><td>199.04 (+5.22%)</td><td>197.20 (+11.41%)</td><td>179.20 (+6.60%)</td><td>20.45 (-16.83%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.78 (n/a)</td><td>0.70 (n/a)</td><td>0.74 (n/a)</td><td>0.58 (n/a)</td><td>0.09 (n/a)</td><td>225.80 (n/a)</td><td>189.16 (n/a)</td><td>177.00 (n/a)</td><td>168.10 (n/a)</td><td>24.58 (n/a)</td>
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
<td><code>3873943</code> — 2026-09-17 22:19:16</td><td>0.13 (+1.81%)</td><td>0.10 (+4.28%)</td><td>0.09 (-1.39%)</td><td>0.08 (+3.45%)</td><td>0.02 (+8.76%)</td><td>200.10 (-3.33%)</td><td>166.90 (-3.66%)</td><td>172.90 (+1.41%)</td><td>123.50 (-1.83%)</td><td>33.30 (+6.19%)</td>
</tr>
<tr>
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.00 (n/a)</td><td>173.24 (n/a)</td><td>170.50 (n/a)</td><td>125.80 (n/a)</td><td>31.36 (n/a)</td>
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
