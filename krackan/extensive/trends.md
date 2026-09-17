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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 <b>(-28.88%)</b></td><td>0.03 <b>(-29.76%)</b></td><td>0.03 <b>(-27.47%)</b></td><td>0.02 <b>(-50.20%)</b></td><td>0.01 (-6.25%)</td><td>348.80 <b>(+100.81%)</b></td><td>213.06 <b>(+49.64%)</b></td><td>185.90 <b>(+37.81%)</b></td><td>149.50 <b>(+40.64%)</b></td><td>79.21 <b>(+167.08%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>173.70 (n/a)</td><td>142.38 (n/a)</td><td>134.90 (n/a)</td><td>106.30 (n/a)</td><td>29.66 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (+13.37%)</td><td>0.04 (+3.51%)</td><td>0.04 (-4.52%)</td><td>0.02 (-6.55%)</td><td>0.01 <b>(+69.69%)</b></td><td>246.30 (+6.99%)</td><td>174.52 (+0.61%)</td><td>173.70 (+4.76%)</td><td>124.70 (-11.81%)</td><td>51.31 <b>(+49.33%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>230.20 (n/a)</td><td>173.46 (n/a)</td><td>165.80 (n/a)</td><td>141.40 (n/a)</td><td>34.36 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (-2.51%)</td><td>0.03 (-1.89%)</td><td>0.03 (-4.81%)</td><td>0.03 (-0.94%)</td><td>0.01 (-6.16%)</td><td>215.30 (+0.94%)</td><td>180.22 (+1.65%)</td><td>184.40 (+5.01%)</td><td>133.10 (+2.62%)</td><td>29.73 (-3.94%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>213.30 (n/a)</td><td>177.30 (n/a)</td><td>175.60 (n/a)</td><td>129.70 (n/a)</td><td>30.95 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (+5.92%)</td><td>0.03 (-1.46%)</td><td>0.03 (-11.07%)</td><td>0.02 <b>(+34.91%)</b></td><td>0.01 (-1.35%)</td><td>246.60 <b>(-25.88%)</b></td><td>194.56 (-1.97%)</td><td>196.60 (+12.41%)</td><td>118.40 (-5.58%)</td><td>50.75 <b>(-35.85%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>332.70 (n/a)</td><td>198.46 (n/a)</td><td>174.90 (n/a)</td><td>125.40 (n/a)</td><td>79.11 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (+8.10%)</td><td>0.04 (-7.63%)</td><td>0.03 (-8.64%)</td><td>0.03 (-7.37%)</td><td>0.01 <b>(+26.17%)</b></td><td>198.30 (+7.95%)</td><td>168.84 (+9.79%)</td><td>180.90 (+9.44%)</td><td>114.30 (-7.45%)</td><td>33.08 <b>(+25.24%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>183.70 (n/a)</td><td>153.78 (n/a)</td><td>165.30 (n/a)</td><td>123.50 (n/a)</td><td>26.42 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (+1.80%)</td><td>0.04 (-12.42%)</td><td>0.03 <b>(-22.54%)</b></td><td>0.03 (-13.14%)</td><td>0.01 <b>(+25.38%)</b></td><td>213.00 (+15.14%)</td><td>174.80 (+15.65%)</td><td>181.10 <b>(+29.08%)</b></td><td>128.00 (-1.77%)</td><td>32.58 <b>(+39.82%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>185.00 (n/a)</td><td>151.14 (n/a)</td><td>140.30 (n/a)</td><td>130.30 (n/a)</td><td>23.30 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (-0.87%)</td><td>0.03 (+4.01%)</td><td>0.03 (-4.42%)</td><td>0.03 (+5.99%)</td><td>0.01 (+5.98%)</td><td>229.40 (-5.67%)</td><td>198.64 (-3.67%)</td><td>217.00 (+4.63%)</td><td>159.40 (+0.82%)</td><td>31.95 (+3.28%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>243.20 (n/a)</td><td>206.20 (n/a)</td><td>207.40 (n/a)</td><td>158.10 (n/a)</td><td>30.93 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (-4.45%)</td><td>0.03 (-18.79%)</td><td>0.03 (-18.42%)</td><td>0.02 <b>(-28.73%)</b></td><td>0.01 <b>(+35.60%)</b></td><td>296.80 <b>(+40.33%)</b></td><td>219.72 <b>(+27.11%)</b></td><td>219.90 <b>(+22.58%)</b></td><td>145.30 (+4.68%)</td><td>53.92 <b>(+94.93%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>211.50 (n/a)</td><td>172.86 (n/a)</td><td>179.40 (n/a)</td><td>138.80 (n/a)</td><td>27.66 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (-11.44%)</td><td>0.07 (-6.88%)</td><td>0.08 (+7.32%)</td><td>0.06 (-10.15%)</td><td>0.01 (-15.80%)</td><td>200.20 (+11.28%)</td><td>166.64 (+7.19%)</td><td>153.20 (-6.87%)</td><td>144.60 (+12.88%)</td><td>24.67 (+7.09%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>179.90 (n/a)</td><td>155.46 (n/a)</td><td>164.50 (n/a)</td><td>128.10 (n/a)</td><td>23.04 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (-0.28%)</td><td>0.08 (+11.69%)</td><td>0.07 (-3.28%)</td><td>0.06 <b>(+96.57%)</b></td><td>0.02 <b>(-30.34%)</b></td><td>193.10 <b>(-49.13%)</b></td><td>160.60 <b>(-20.41%)</b></td><td>180.60 (+3.44%)</td><td>116.50 (+0.34%)</td><td>35.02 <b>(-66.31%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>379.60 (n/a)</td><td>201.78 (n/a)</td><td>174.60 (n/a)</td><td>116.10 (n/a)</td><td>103.95 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (-4.03%)</td><td>0.07 (-17.82%)</td><td>0.06 <b>(-21.50%)</b></td><td>0.05 <b>(-20.44%)</b></td><td>0.02 <b>(+29.21%)</b></td><td>231.40 <b>(+25.69%)</b></td><td>185.60 <b>(+24.25%)</b></td><td>192.70 <b>(+27.36%)</b></td><td>125.10 (+4.16%)</td><td>38.30 <b>(+60.90%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>184.10 (n/a)</td><td>149.38 (n/a)</td><td>151.30 (n/a)</td><td>120.10 (n/a)</td><td>23.80 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (-7.89%)</td><td>0.07 (-16.22%)</td><td>0.06 (-19.11%)</td><td>0.05 <b>(-26.46%)</b></td><td>0.02 <b>(+26.24%)</b></td><td>234.00 <b>(+35.97%)</b></td><td>184.94 <b>(+22.59%)</b></td><td>195.40 <b>(+23.67%)</b></td><td>123.90 (+8.59%)</td><td>41.73 <b>(+86.07%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>172.10 (n/a)</td><td>150.86 (n/a)</td><td>158.00 (n/a)</td><td>114.10 (n/a)</td><td>22.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.09 (-1.31%)</td><td>0.07 (-5.70%)</td><td>0.07 (-3.67%)</td><td>0.06 (-4.22%)</td><td>0.01 (+3.87%)</td><td>214.10 (+4.39%)</td><td>178.24 (+6.36%)</td><td>177.10 (+3.81%)</td><td>130.00 (+1.33%)</td><td>31.35 (+8.05%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>205.10 (n/a)</td><td>167.58 (n/a)</td><td>170.60 (n/a)</td><td>128.30 (n/a)</td><td>29.01 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 <b>(-29.70%)</b></td><td>0.07 <b>(-25.52%)</b></td><td>0.07 <b>(-27.73%)</b></td><td>0.05 <b>(-25.39%)</b></td><td>0.01 <b>(-36.50%)</b></td><td>233.50 <b>(+34.04%)</b></td><td>189.70 <b>(+33.57%)</b></td><td>187.50 <b>(+38.38%)</b></td><td>161.90 <b>(+42.27%)</b></td><td>28.44 (+19.69%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>174.20 (n/a)</td><td>142.02 (n/a)</td><td>135.50 (n/a)</td><td>113.80 (n/a)</td><td>23.76 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (+9.21%)</td><td>0.07 (+8.45%)</td><td>0.07 (+7.61%)</td><td>0.05 (+3.01%)</td><td>0.01 (+8.10%)</td><td>228.30 (-2.89%)</td><td>184.88 (-7.71%)</td><td>179.70 (-7.04%)</td><td>157.70 (-8.42%)</td><td>26.08 (-1.47%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>235.10 (n/a)</td><td>200.32 (n/a)</td><td>193.30 (n/a)</td><td>172.20 (n/a)</td><td>26.47 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (+8.76%)</td><td>0.07 (+7.16%)</td><td>0.06 (+6.12%)</td><td>0.05 (+1.83%)</td><td>0.02 <b>(+20.87%)</b></td><td>225.70 (-1.78%)</td><td>184.22 (-5.72%)</td><td>202.10 (-5.74%)</td><td>129.20 (-8.04%)</td><td>39.76 (+9.37%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>229.80 (n/a)</td><td>195.40 (n/a)</td><td>214.40 (n/a)</td><td>140.50 (n/a)</td><td>36.35 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (-8.51%)</td><td>0.14 (+6.77%)</td><td>0.14 (-3.89%)</td><td>0.13 <b>(+96.54%)</b></td><td>0.01 <b>(-72.48%)</b></td><td>191.80 <b>(-49.12%)</b></td><td>173.50 (-17.27%)</td><td>178.60 (+4.02%)</td><td>155.00 (+9.31%)</td><td>14.89 <b>(-84.81%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>377.00 (n/a)</td><td>209.72 (n/a)</td><td>171.70 (n/a)</td><td>141.80 (n/a)</td><td>97.99 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (-1.22%)</td><td>0.16 (-6.93%)</td><td>0.15 (-8.92%)</td><td>0.13 (-14.43%)</td><td>0.03 <b>(+53.98%)</b></td><td>191.50 (+16.84%)</td><td>161.32 (+8.96%)</td><td>166.10 (+9.78%)</td><td>133.00 (+1.29%)</td><td>26.32 <b>(+79.22%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>163.90 (n/a)</td><td>148.06 (n/a)</td><td>151.30 (n/a)</td><td>131.30 (n/a)</td><td>14.68 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.19 (-10.28%)</td><td>0.15 (-7.66%)</td><td>0.16 (+4.63%)</td><td>0.08 <b>(-36.35%)</b></td><td>0.04 <b>(+25.22%)</b></td><td>307.10 <b>(+57.08%)</b></td><td>185.04 (+14.80%)</td><td>152.80 (-4.38%)</td><td>132.50 (+11.53%)</td><td>72.29 <b>(+115.28%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>195.50 (n/a)</td><td>161.18 (n/a)</td><td>159.80 (n/a)</td><td>118.80 (n/a)</td><td>33.58 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (-15.34%)</td><td>0.15 (-3.16%)</td><td>0.15 (+3.95%)</td><td>0.13 (-3.04%)</td><td>0.02 <b>(-43.80%)</b></td><td>183.30 (+3.09%)</td><td>165.84 (+1.72%)</td><td>168.20 (-3.83%)</td><td>139.70 (+18.19%)</td><td>17.54 <b>(-30.88%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>177.80 (n/a)</td><td>163.04 (n/a)</td><td>174.90 (n/a)</td><td>118.20 (n/a)</td><td>25.37 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.29 <b>(+52.85%)</b></td><td>0.19 <b>(+33.38%)</b></td><td>0.18 (+19.84%)</td><td>0.14 <b>(+44.57%)</b></td><td>0.06 <b>(+51.63%)</b></td><td>180.70 <b>(-30.85%)</b></td><td>136.66 <b>(-24.77%)</b></td><td>133.10 (-16.55%)</td><td>85.40 <b>(-34.56%)</b></td><td>39.19 <b>(-29.97%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>261.30 (n/a)</td><td>181.66 (n/a)</td><td>159.50 (n/a)</td><td>130.50 (n/a)</td><td>55.97 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (-14.75%)</td><td>0.14 (-4.55%)</td><td>0.15 (+17.74%)</td><td>0.11 (-1.13%)</td><td>0.02 <b>(-44.32%)</b></td><td>217.00 (+1.12%)</td><td>179.50 (+1.82%)</td><td>166.70 (-15.08%)</td><td>153.40 (+17.28%)</td><td>27.27 <b>(-32.34%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>214.60 (n/a)</td><td>176.30 (n/a)</td><td>196.30 (n/a)</td><td>130.80 (n/a)</td><td>40.30 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (+6.31%)</td><td>0.14 (+1.75%)</td><td>0.16 (+6.68%)</td><td>0.07 (-8.66%)</td><td>0.04 <b>(+25.85%)</b></td><td>337.10 (+9.48%)</td><td>197.08 (+2.11%)</td><td>158.20 (-6.28%)</td><td>134.60 (-5.94%)</td><td>83.06 <b>(+25.65%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>307.90 (n/a)</td><td>193.00 (n/a)</td><td>168.80 (n/a)</td><td>143.10 (n/a)</td><td>66.11 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 (+0.34%)</td><td>0.14 (+2.92%)</td><td>0.14 (+2.44%)</td><td>0.12 (+12.69%)</td><td>0.01 <b>(-28.29%)</b></td><td>204.80 (-11.23%)</td><td>180.68 (-3.85%)</td><td>175.00 (-2.34%)</td><td>158.60 (-0.38%)</td><td>19.62 <b>(-35.40%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>230.70 (n/a)</td><td>187.92 (n/a)</td><td>179.20 (n/a)</td><td>159.20 (n/a)</td><td>30.38 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.32 (-16.54%)</td><td>0.28 (-8.81%)</td><td>0.28 (+1.37%)</td><td>0.22 (-9.06%)</td><td>0.04 <b>(-42.16%)</b></td><td>226.70 (+9.94%)</td><td>179.64 (+7.61%)</td><td>172.90 (-1.37%)</td><td>153.30 (+19.77%)</td><td>27.63 (-19.41%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.07 (n/a)</td><td>206.20 (n/a)</td><td>166.94 (n/a)</td><td>175.30 (n/a)</td><td>128.00 (n/a)</td><td>34.28 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.42 (+17.39%)</td><td>0.30 (-2.74%)</td><td>0.28 (-11.96%)</td><td>0.18 <b>(-29.94%)</b></td><td>0.10 <b>(+137.37%)</b></td><td>277.40 <b>(+42.77%)</b></td><td>183.32 (+11.92%)</td><td>172.70 (+13.54%)</td><td>118.40 (-14.82%)</td><td>66.14 <b>(+177.98%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.35 (n/a)</td><td>0.31 (n/a)</td><td>0.32 (n/a)</td><td>0.25 (n/a)</td><td>0.04 (n/a)</td><td>194.30 (n/a)</td><td>163.80 (n/a)</td><td>152.10 (n/a)</td><td>139.00 (n/a)</td><td>23.79 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.32 (-17.08%)</td><td>0.28 (-10.17%)</td><td>0.27 (-9.03%)</td><td>0.26 (-3.75%)</td><td>0.03 <b>(-43.97%)</b></td><td>192.50 (+3.89%)</td><td>178.88 (+10.27%)</td><td>181.70 (+9.92%)</td><td>153.50 <b>(+20.58%)</b></td><td>15.36 <b>(-28.43%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.05 (n/a)</td><td>185.30 (n/a)</td><td>162.22 (n/a)</td><td>165.30 (n/a)</td><td>127.30 (n/a)</td><td>21.46 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.40 <b>(+27.85%)</b></td><td>0.34 (+12.46%)</td><td>0.32 (+3.90%)</td><td>0.26 (-7.08%)</td><td>0.06 <b>(+376.10%)</b></td><td>188.10 (+7.61%)</td><td>149.64 (-8.73%)</td><td>155.30 (-3.78%)</td><td>122.20 <b>(-21.82%)</b></td><td>27.95 <b>(+283.43%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.30 (n/a)</td><td>0.28 (n/a)</td><td>0.01 (n/a)</td><td>174.80 (n/a)</td><td>163.96 (n/a)</td><td>161.40 (n/a)</td><td>156.30 (n/a)</td><td>7.29 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.29 <b>(+21.95%)</b></td><td>0.25 (+15.54%)</td><td>0.26 (+16.68%)</td><td>0.17 (-4.15%)</td><td>0.04 <b>(+76.48%)</b></td><td>283.20 (+4.31%)</td><td>202.86 (-11.62%)</td><td>187.40 (-14.27%)</td><td>168.60 (-18.00%)</td><td>45.75 <b>(+59.90%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>271.50 (n/a)</td><td>229.52 (n/a)</td><td>218.60 (n/a)</td><td>205.60 (n/a)</td><td>28.61 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.31 (+9.07%)</td><td>0.27 (+3.17%)</td><td>0.26 (-1.65%)</td><td>0.25 (+5.53%)</td><td>0.03 <b>(+35.74%)</b></td><td>195.40 (-5.24%)</td><td>185.84 (-2.78%)</td><td>192.70 (+1.69%)</td><td>156.20 (-8.28%)</td><td>16.68 (+16.49%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.24 (n/a)</td><td>0.02 (n/a)</td><td>206.20 (n/a)</td><td>191.16 (n/a)</td><td>189.50 (n/a)</td><td>170.30 (n/a)</td><td>14.32 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.42 <b>(+45.72%)</b></td><td>0.25 (+9.85%)</td><td>0.23 (-1.66%)</td><td>0.16 (+0.34%)</td><td>0.10 <b>(+111.66%)</b></td><td>302.10 (-0.36%)</td><td>212.22 (-3.53%)</td><td>211.80 (+1.73%)</td><td>117.00 <b>(-31.38%)</b></td><td>65.68 <b>(+31.25%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>303.20 (n/a)</td><td>219.98 (n/a)</td><td>208.20 (n/a)</td><td>170.50 (n/a)</td><td>50.05 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 (+8.14%)</td><td>0.25 (+5.04%)</td><td>0.26 (+6.85%)</td><td>0.22 (+1.11%)</td><td>0.03 <b>(+38.74%)</b></td><td>223.00 (-1.11%)</td><td>198.08 (-4.43%)</td><td>186.20 (-6.39%)</td><td>178.70 (-7.51%)</td><td>21.18 <b>(+27.45%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.22 (n/a)</td><td>0.02 (n/a)</td><td>225.50 (n/a)</td><td>207.26 (n/a)</td><td>198.90 (n/a)</td><td>193.20 (n/a)</td><td>16.62 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (-0.90%)</td><td>0.02 (-17.78%)</td><td>0.01 <b>(-29.69%)</b></td><td>0.01 <b>(-20.31%)</b></td><td>0.00 <b>(+35.01%)</b></td><td>223.40 <b>(+25.51%)</b></td><td>174.32 <b>(+24.67%)</b></td><td>181.10 <b>(+42.26%)</b></td><td>121.30 (+0.92%)</td><td>39.63 <b>(+67.54%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>178.00 (n/a)</td><td>139.82 (n/a)</td><td>127.30 (n/a)</td><td>120.20 (n/a)</td><td>23.65 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 <b>(-21.67%)</b></td><td>0.02 <b>(-23.52%)</b></td><td>0.02 <b>(-27.31%)</b></td><td>0.01 (-17.28%)</td><td>0.00 <b>(-33.48%)</b></td><td>197.90 <b>(+20.89%)</b></td><td>172.94 <b>(+30.13%)</b></td><td>169.00 <b>(+37.62%)</b></td><td>150.20 <b>(+27.61%)</b></td><td>20.12 (+3.66%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>163.70 (n/a)</td><td>132.90 (n/a)</td><td>122.80 (n/a)</td><td>117.70 (n/a)</td><td>19.41 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (+16.92%)</td><td>0.02 (+10.96%)</td><td>0.01 (-0.28%)</td><td>0.01 (+14.34%)</td><td>0.00 <b>(+23.56%)</b></td><td>198.40 (-12.56%)</td><td>171.30 (-9.70%)</td><td>180.10 (+0.28%)</td><td>136.90 (-14.49%)</td><td>25.25 (-8.82%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>226.90 (n/a)</td><td>189.70 (n/a)</td><td>179.60 (n/a)</td><td>160.10 (n/a)</td><td>27.70 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (-5.49%)</td><td>0.01 (-1.11%)</td><td>0.01 (-2.10%)</td><td>0.01 (+3.85%)</td><td>0.00 (-14.00%)</td><td>223.40 (-3.71%)</td><td>186.82 (+0.21%)</td><td>195.60 (+2.14%)</td><td>133.10 (+5.80%)</td><td>34.24 (-10.37%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>232.00 (n/a)</td><td>186.42 (n/a)</td><td>191.50 (n/a)</td><td>125.80 (n/a)</td><td>38.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 <b>(+25.60%)</b></td><td>0.01 (+7.40%)</td><td>0.01 (+1.23%)</td><td>0.01 <b>(+30.13%)</b></td><td>0.00 <b>(+33.51%)</b></td><td>223.40 <b>(-23.15%)</b></td><td>189.08 (-6.65%)</td><td>195.70 (-1.21%)</td><td>120.30 <b>(-20.38%)</b></td><td>41.95 <b>(-21.69%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>290.70 (n/a)</td><td>202.54 (n/a)</td><td>198.10 (n/a)</td><td>151.10 (n/a)</td><td>53.57 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (+2.03%)</td><td>0.01 (+2.73%)</td><td>0.02 (+1.45%)</td><td>0.01 <b>(+25.43%)</b></td><td>0.00 <b>(-32.14%)</b></td><td>204.30 <b>(-20.26%)</b></td><td>178.72 (-4.46%)</td><td>173.40 (-1.42%)</td><td>154.10 (-1.97%)</td><td>20.16 <b>(-48.86%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>256.20 (n/a)</td><td>187.06 (n/a)</td><td>175.90 (n/a)</td><td>157.20 (n/a)</td><td>39.42 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.01 <b>(-34.04%)</b></td><td>0.01 (-18.48%)</td><td>0.01 (-12.88%)</td><td>0.01 (+3.85%)</td><td>0.00 <b>(-78.38%)</b></td><td>224.60 (-3.73%)</td><td>203.00 (+16.73%)</td><td>202.10 (+14.76%)</td><td>187.70 <b>(+51.62%)</b></td><td>14.27 <b>(-67.91%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>233.30 (n/a)</td><td>173.90 (n/a)</td><td>176.10 (n/a)</td><td>123.80 (n/a)</td><td>44.45 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.01 (-13.49%)</td><td>0.01 (-12.53%)</td><td>0.01 (-17.91%)</td><td>0.01 (+0.52%)</td><td>0.00 <b>(-56.83%)</b></td><td>224.40 (-0.53%)</td><td>214.88 (+13.31%)</td><td>219.40 <b>(+21.82%)</b></td><td>195.20 (+15.64%)</td><td>11.42 <b>(-51.15%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>225.60 (n/a)</td><td>189.64 (n/a)</td><td>180.10 (n/a)</td><td>168.80 (n/a)</td><td>23.37 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (-3.62%)</td><td>0.03 (+12.10%)</td><td>0.03 <b>(+25.71%)</b></td><td>0.03 (+19.63%)</td><td>0.00 <b>(-54.65%)</b></td><td>171.60 (-16.42%)</td><td>152.08 (-13.06%)</td><td>153.20 <b>(-20.46%)</b></td><td>136.30 (+3.81%)</td><td>12.94 <b>(-60.80%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>205.30 (n/a)</td><td>174.92 (n/a)</td><td>192.60 (n/a)</td><td>131.30 (n/a)</td><td>33.01 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (-5.82%)</td><td>0.03 (-11.33%)</td><td>0.04 (-0.67%)</td><td>0.02 (-16.43%)</td><td>0.01 (+14.53%)</td><td>312.80 (+19.66%)</td><td>191.98 (+17.79%)</td><td>148.80 (+0.68%)</td><td>123.40 (+6.20%)</td><td>79.76 <b>(+39.26%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>261.40 (n/a)</td><td>162.98 (n/a)</td><td>147.80 (n/a)</td><td>116.20 (n/a)</td><td>57.27 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (+2.69%)</td><td>0.03 (-3.03%)</td><td>0.03 (+7.51%)</td><td>0.02 (-13.97%)</td><td>0.01 <b>(+23.53%)</b></td><td>260.00 (+16.23%)</td><td>187.62 (+5.09%)</td><td>169.10 (-6.99%)</td><td>138.70 (-2.67%)</td><td>46.17 <b>(+44.37%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>178.54 (n/a)</td><td>181.80 (n/a)</td><td>142.50 (n/a)</td><td>31.98 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (+1.32%)</td><td>0.03 (+4.39%)</td><td>0.03 (+7.67%)</td><td>0.03 (+1.19%)</td><td>0.01 (-5.02%)</td><td>195.10 (-1.17%)</td><td>167.80 (-4.45%)</td><td>171.10 (-7.11%)</td><td>128.60 (-1.30%)</td><td>24.21 (-7.40%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>197.40 (n/a)</td><td>175.62 (n/a)</td><td>184.20 (n/a)</td><td>130.30 (n/a)</td><td>26.15 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 <b>(+29.18%)</b></td><td>0.03 (+6.18%)</td><td>0.03 (+11.40%)</td><td>0.03 (+13.65%)</td><td>0.01 <b>(+25.40%)</b></td><td>201.30 (-12.02%)</td><td>169.44 (-5.44%)</td><td>186.10 (-10.23%)</td><td>95.20 <b>(-22.60%)</b></td><td>42.79 (-15.21%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>228.80 (n/a)</td><td>179.18 (n/a)</td><td>207.30 (n/a)</td><td>123.00 (n/a)</td><td>50.46 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (+16.97%)</td><td>0.03 (+3.80%)</td><td>0.03 (+4.45%)</td><td>0.03 (+9.33%)</td><td>0.01 (+15.66%)</td><td>208.40 (-8.56%)</td><td>181.40 (-3.47%)</td><td>195.60 (-4.26%)</td><td>127.80 (-14.52%)</td><td>32.90 (-7.24%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.90 (n/a)</td><td>187.92 (n/a)</td><td>204.30 (n/a)</td><td>149.50 (n/a)</td><td>35.47 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 <b>(-23.03%)</b></td><td>0.03 (-17.21%)</td><td>0.02 (-16.59%)</td><td>0.02 <b>(-23.66%)</b></td><td>0.00 (-12.62%)</td><td>241.70 <b>(+31.00%)</b></td><td>206.46 <b>(+21.30%)</b></td><td>218.20 (+19.89%)</td><td>172.00 <b>(+29.91%)</b></td><td>32.03 <b>(+45.21%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>184.50 (n/a)</td><td>170.20 (n/a)</td><td>182.00 (n/a)</td><td>132.40 (n/a)</td><td>22.06 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (+17.22%)</td><td>0.03 (+0.21%)</td><td>0.03 (+0.48%)</td><td>0.02 (-0.49%)</td><td>0.01 <b>(+50.83%)</b></td><td>226.00 (+0.53%)</td><td>197.88 (+1.98%)</td><td>207.90 (-0.48%)</td><td>127.30 (-14.68%)</td><td>40.84 <b>(+26.12%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>224.80 (n/a)</td><td>194.04 (n/a)</td><td>208.90 (n/a)</td><td>149.20 (n/a)</td><td>32.38 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (-14.55%)</td><td>0.06 (-5.20%)</td><td>0.06 (+3.89%)</td><td>0.05 (+2.31%)</td><td>0.01 <b>(-40.86%)</b></td><td>209.70 (-2.24%)</td><td>179.82 (+3.27%)</td><td>180.10 (-3.74%)</td><td>148.20 (+17.06%)</td><td>24.13 <b>(-31.68%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>214.50 (n/a)</td><td>174.12 (n/a)</td><td>187.10 (n/a)</td><td>126.60 (n/a)</td><td>35.32 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (-0.22%)</td><td>0.06 <b>(+24.96%)</b></td><td>0.07 (+11.55%)</td><td>0.06 <b>(+74.44%)</b></td><td>0.00 <b>(-73.84%)</b></td><td>179.40 <b>(-42.68%)</b></td><td>164.72 <b>(-26.84%)</b></td><td>160.00 (-10.36%)</td><td>152.00 (+0.20%)</td><td>11.20 <b>(-85.79%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>313.00 (n/a)</td><td>225.14 (n/a)</td><td>178.50 (n/a)</td><td>151.70 (n/a)</td><td>78.78 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (+0.23%)</td><td>0.06 (-7.63%)</td><td>0.06 (-2.21%)</td><td>0.05 (-18.11%)</td><td>0.01 <b>(+75.32%)</b></td><td>225.50 <b>(+22.09%)</b></td><td>185.78 (+10.06%)</td><td>176.60 (+2.26%)</td><td>148.60 (-0.27%)</td><td>31.22 <b>(+117.30%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>184.70 (n/a)</td><td>168.80 (n/a)</td><td>172.70 (n/a)</td><td>149.00 (n/a)</td><td>14.37 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (-12.29%)</td><td>0.06 (+5.08%)</td><td>0.05 (-9.05%)</td><td>0.05 <b>(+73.63%)</b></td><td>0.01 <b>(-62.61%)</b></td><td>211.30 <b>(-42.39%)</b></td><td>185.40 (-18.45%)</td><td>194.50 (+9.95%)</td><td>149.50 (+14.04%)</td><td>26.17 <b>(-75.73%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>366.80 (n/a)</td><td>227.34 (n/a)</td><td>176.90 (n/a)</td><td>131.10 (n/a)</td><td>107.83 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 <b>(-21.19%)</b></td><td>0.06 (-11.44%)</td><td>0.06 (+0.78%)</td><td>0.04 <b>(-21.66%)</b></td><td>0.02 (-0.50%)</td><td>297.30 <b>(+27.65%)</b></td><td>202.72 (+16.08%)</td><td>167.50 (-0.77%)</td><td>151.70 <b>(+26.95%)</b></td><td>65.39 <b>(+58.34%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>174.64 (n/a)</td><td>168.80 (n/a)</td><td>119.50 (n/a)</td><td>41.29 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (+8.00%)</td><td>0.06 (+0.81%)</td><td>0.05 (-0.67%)</td><td>0.05 (+3.73%)</td><td>0.01 (+11.47%)</td><td>228.50 (-3.59%)</td><td>193.46 (-0.67%)</td><td>191.70 (+0.68%)</td><td>150.40 (-7.45%)</td><td>28.59 (-2.63%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>237.00 (n/a)</td><td>194.76 (n/a)</td><td>190.40 (n/a)</td><td>162.50 (n/a)</td><td>29.36 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 <b>(+21.09%)</b></td><td>0.06 (-5.41%)</td><td>0.05 (-9.19%)</td><td>0.04 (-19.21%)</td><td>0.02 <b>(+113.47%)</b></td><td>249.80 <b>(+23.79%)</b></td><td>199.34 (+10.28%)</td><td>212.80 (+10.14%)</td><td>125.90 (-17.39%)</td><td>46.44 <b>(+108.43%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>201.80 (n/a)</td><td>180.76 (n/a)</td><td>193.20 (n/a)</td><td>152.40 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (-3.15%)</td><td>0.05 (+2.07%)</td><td>0.05 (-0.43%)</td><td>0.04 <b>(+36.77%)</b></td><td>0.01 <b>(-38.91%)</b></td><td>256.50 <b>(-26.88%)</b></td><td>220.30 (-5.90%)</td><td>223.20 (+0.45%)</td><td>178.40 (+3.24%)</td><td>29.67 <b>(-56.58%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>350.80 (n/a)</td><td>234.12 (n/a)</td><td>222.20 (n/a)</td><td>172.80 (n/a)</td><td>68.35 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 <b>(-21.17%)</b></td><td>0.10 <b>(-32.13%)</b></td><td>0.10 <b>(-37.85%)</b></td><td>0.06 <b>(-40.49%)</b></td><td>0.03 (-8.72%)</td><td>362.30 <b>(+68.04%)</b></td><td>224.72 <b>(+52.54%)</b></td><td>203.40 <b>(+60.92%)</b></td><td>157.80 <b>(+26.85%)</b></td><td>79.86 <b>(+104.87%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.17 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>215.60 (n/a)</td><td>147.32 (n/a)</td><td>126.40 (n/a)</td><td>124.40 (n/a)</td><td>38.98 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.19 (+19.29%)</td><td>0.12 (-5.55%)</td><td>0.11 (-16.83%)</td><td>0.09 (+4.11%)</td><td>0.04 <b>(+34.95%)</b></td><td>229.60 (-3.93%)</td><td>181.04 (+7.90%)</td><td>182.90 <b>(+20.17%)</b></td><td>108.10 (-16.14%)</td><td>46.63 (+4.27%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>239.00 (n/a)</td><td>167.78 (n/a)</td><td>152.20 (n/a)</td><td>128.90 (n/a)</td><td>44.71 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.17 (+8.39%)</td><td>0.13 (-3.44%)</td><td>0.12 (-10.03%)</td><td>0.09 (-4.85%)</td><td>0.03 <b>(+28.20%)</b></td><td>230.00 (+5.07%)</td><td>175.30 (+5.23%)</td><td>171.00 (+11.11%)</td><td>120.10 (-7.76%)</td><td>41.09 <b>(+20.81%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>218.90 (n/a)</td><td>166.58 (n/a)</td><td>153.90 (n/a)</td><td>130.20 (n/a)</td><td>34.01 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (-17.76%)</td><td>0.11 <b>(-20.21%)</b></td><td>0.11 <b>(-20.49%)</b></td><td>0.08 (-9.23%)</td><td>0.02 <b>(-32.59%)</b></td><td>256.20 (+10.19%)</td><td>202.84 <b>(+22.99%)</b></td><td>189.00 <b>(+25.75%)</b></td><td>154.10 <b>(+21.63%)</b></td><td>41.63 (-6.47%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>232.50 (n/a)</td><td>164.92 (n/a)</td><td>150.30 (n/a)</td><td>126.70 (n/a)</td><td>44.51 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (+3.64%)</td><td>0.13 (+0.66%)</td><td>0.13 (+2.51%)</td><td>0.10 (+15.18%)</td><td>0.03 (-13.64%)</td><td>203.20 (-13.20%)</td><td>166.72 (-2.15%)</td><td>159.80 (-2.44%)</td><td>128.10 (-3.54%)</td><td>31.74 <b>(-24.22%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>234.10 (n/a)</td><td>170.38 (n/a)</td><td>163.80 (n/a)</td><td>132.80 (n/a)</td><td>41.89 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (-17.69%)</td><td>0.10 (-18.01%)</td><td>0.09 <b>(-20.81%)</b></td><td>0.08 (-5.54%)</td><td>0.02 <b>(-27.43%)</b></td><td>250.90 (+5.86%)</td><td>220.78 <b>(+20.15%)</b></td><td>241.20 <b>(+26.28%)</b></td><td>153.40 <b>(+21.46%)</b></td><td>40.29 (-6.70%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.03 (n/a)</td><td>237.00 (n/a)</td><td>183.76 (n/a)</td><td>191.00 (n/a)</td><td>126.30 (n/a)</td><td>43.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.19 (+12.11%)</td><td>0.12 (-9.70%)</td><td>0.11 (-15.10%)</td><td>0.09 (-8.52%)</td><td>0.04 <b>(+27.07%)</b></td><td>225.80 (+9.29%)</td><td>185.46 (+13.10%)</td><td>186.00 (+17.80%)</td><td>112.80 (-10.83%)</td><td>45.37 <b>(+21.49%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>206.60 (n/a)</td><td>163.98 (n/a)</td><td>157.90 (n/a)</td><td>126.50 (n/a)</td><td>37.34 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (-1.38%)</td><td>0.10 (+2.44%)</td><td>0.10 (+7.65%)</td><td>0.08 (+13.27%)</td><td>0.01 <b>(-37.03%)</b></td><td>260.20 (-11.71%)</td><td>218.90 (-4.78%)</td><td>216.50 (-7.12%)</td><td>178.80 (+1.42%)</td><td>28.99 <b>(-42.58%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>294.70 (n/a)</td><td>229.90 (n/a)</td><td>233.10 (n/a)</td><td>176.30 (n/a)</td><td>50.49 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>204.00 (n/a)</td><td>154.44 (n/a)</td><td>148.20 (n/a)</td><td>103.90 (n/a)</td><td>41.05 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>202.30 (n/a)</td><td>171.02 (n/a)</td><td>169.80 (n/a)</td><td>140.70 (n/a)</td><td>22.01 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>211.30 (n/a)</td><td>168.40 (n/a)</td><td>154.80 (n/a)</td><td>127.00 (n/a)</td><td>36.66 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>320.70 (n/a)</td><td>212.64 (n/a)</td><td>197.80 (n/a)</td><td>162.00 (n/a)</td><td>65.34 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>245.70 (n/a)</td><td>168.32 (n/a)</td><td>129.40 (n/a)</td><td>118.70 (n/a)</td><td>61.54 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>218.20 (n/a)</td><td>176.58 (n/a)</td><td>192.10 (n/a)</td><td>126.80 (n/a)</td><td>43.90 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>197.90 (n/a)</td><td>163.40 (n/a)</td><td>169.60 (n/a)</td><td>126.50 (n/a)</td><td>34.36 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>291.00 (n/a)</td><td>199.88 (n/a)</td><td>191.60 (n/a)</td><td>141.50 (n/a)</td><td>58.54 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>251.00 (n/a)</td><td>192.26 (n/a)</td><td>206.70 (n/a)</td><td>131.70 (n/a)</td><td>47.59 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>269.50 (n/a)</td><td>180.48 (n/a)</td><td>174.00 (n/a)</td><td>129.30 (n/a)</td><td>57.92 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>202.30 (n/a)</td><td>157.76 (n/a)</td><td>159.30 (n/a)</td><td>126.00 (n/a)</td><td>29.54 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.03 (n/a)</td><td>212.50 (n/a)</td><td>176.04 (n/a)</td><td>166.20 (n/a)</td><td>134.10 (n/a)</td><td>31.78 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.38 (-0.45%)</td><td>0.29 (+4.09%)</td><td>0.28 (+5.73%)</td><td>0.24 (+9.53%)</td><td>0.05 (-17.06%)</td><td>203.10 (-8.68%)</td><td>170.42 (-5.08%)</td><td>173.50 (-5.40%)</td><td>130.40 (+0.46%)</td><td>26.03 <b>(-24.65%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.38 (n/a)</td><td>0.28 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.06 (n/a)</td><td>222.40 (n/a)</td><td>179.54 (n/a)</td><td>183.40 (n/a)</td><td>129.80 (n/a)</td><td>34.54 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.05 (n/a)</td><td>216.70 (n/a)</td><td>177.12 (n/a)</td><td>177.30 (n/a)</td><td>135.60 (n/a)</td><td>28.73 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.39 (n/a)</td><td>0.31 (n/a)</td><td>0.36 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>227.30 (n/a)</td><td>169.18 (n/a)</td><td>134.80 (n/a)</td><td>127.20 (n/a)</td><td>51.68 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.38 (n/a)</td><td>0.31 (n/a)</td><td>0.30 (n/a)</td><td>0.24 (n/a)</td><td>0.06 (n/a)</td><td>208.80 (n/a)</td><td>163.52 (n/a)</td><td>162.00 (n/a)</td><td>128.40 (n/a)</td><td>34.04 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>221.10 (n/a)</td><td>179.96 (n/a)</td><td>170.00 (n/a)</td><td>141.10 (n/a)</td><td>31.63 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>229.00 (n/a)</td><td>189.60 (n/a)</td><td>182.40 (n/a)</td><td>165.20 (n/a)</td><td>26.24 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>258.10 (n/a)</td><td>204.96 (n/a)</td><td>208.40 (n/a)</td><td>143.80 (n/a)</td><td>43.65 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>212.50 (n/a)</td><td>190.10 (n/a)</td><td>200.10 (n/a)</td><td>129.10 (n/a)</td><td>34.75 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>371.70 (n/a)</td><td>213.64 (n/a)</td><td>187.90 (n/a)</td><td>140.00 (n/a)</td><td>90.65 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>251.50 (n/a)</td><td>204.80 (n/a)</td><td>199.80 (n/a)</td><td>177.20 (n/a)</td><td>30.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>322.90 (n/a)</td><td>217.32 (n/a)</td><td>199.10 (n/a)</td><td>179.50 (n/a)</td><td>59.71 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>244.00 (n/a)</td><td>217.90 (n/a)</td><td>233.80 (n/a)</td><td>148.60 (n/a)</td><td>39.14 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>295.60 (n/a)</td><td>200.22 (n/a)</td><td>178.20 (n/a)</td><td>170.80 (n/a)</td><td>53.48 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>258.90 (n/a)</td><td>205.00 (n/a)</td><td>185.30 (n/a)</td><td>178.50 (n/a)</td><td>33.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>207.60 (n/a)</td><td>187.58 (n/a)</td><td>186.80 (n/a)</td><td>166.50 (n/a)</td><td>17.89 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.02 (n/a)</td><td>232.90 (n/a)</td><td>205.12 (n/a)</td><td>216.90 (n/a)</td><td>158.60 (n/a)</td><td>30.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.40 (n/a)</td><td>0.30 (n/a)</td><td>0.27 (n/a)</td><td>0.26 (n/a)</td><td>0.06 (n/a)</td><td>192.70 (n/a)</td><td>169.34 (n/a)</td><td>183.60 (n/a)</td><td>122.40 (n/a)</td><td>28.78 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.45 (n/a)</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.10 (n/a)</td><td>228.80 (n/a)</td><td>189.24 (n/a)</td><td>208.90 (n/a)</td><td>109.70 (n/a)</td><td>46.83 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.47 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.11 (n/a)</td><td>233.70 (n/a)</td><td>198.66 (n/a)</td><td>224.20 (n/a)</td><td>105.00 (n/a)</td><td>54.11 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>14.80 (-7.15%)</td><td>13.31 (-7.88%)</td><td>13.06 (-10.56%)</td><td>12.43 (-3.21%)</td><td>0.95 (-13.84%)</td><td>4481.60 (+3.32%)</td><td>4200.24 (+8.46%)</td><td>4265.90 (+11.80%)</td><td>3764.50 (+7.70%)</td><td>287.44 (-4.99%)</td><td>14261.44 (-7.15%)</td><td>12832.07 (-7.88%)</td><td>12585.13 (-10.56%)</td><td>11979.51 (-3.21%)</td><td>916.40 (-13.84%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>15.94 (n/a)</td><td>14.45 (n/a)</td><td>14.60 (n/a)</td><td>12.84 (n/a)</td><td>1.10 (n/a)</td><td>4337.50 (n/a)</td><td>3872.72 (n/a)</td><td>3815.50 (n/a)</td><td>3495.50 (n/a)</td><td>302.53 (n/a)</td><td>15358.90 (n/a)</td><td>13929.05 (n/a)</td><td>14070.66 (n/a)</td><td>12377.40 (n/a)</td><td>1063.59 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>15.73 (+0.42%)</td><td>13.93 (-6.62%)</td><td>14.56 (-2.60%)</td><td>10.11 <b>(-28.99%)</b></td><td>2.20 <b>(+245.92%)</b></td><td>1297.10 <b>(+40.84%)</b></td><td>964.76 (+9.62%)</td><td>900.20 (+2.67%)</td><td>833.20 (-0.42%)</td><td>188.13 <b>(+401.67%)</b></td><td>10309.27 (+0.42%)</td><td>9127.66 (-6.62%)</td><td>9541.83 (-2.60%)</td><td>6622.50 <b>(-28.99%)</b></td><td>1440.41 <b>(+245.92%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>15.67 (n/a)</td><td>14.91 (n/a)</td><td>14.95 (n/a)</td><td>14.23 (n/a)</td><td>0.64 (n/a)</td><td>921.00 (n/a)</td><td>880.08 (n/a)</td><td>876.80 (n/a)</td><td>836.70 (n/a)</td><td>37.50 (n/a)</td><td>10266.29 (n/a)</td><td>9774.58 (n/a)</td><td>9796.37 (n/a)</td><td>9326.72 (n/a)</td><td>416.40 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>14.02 (-7.69%)</td><td>13.65 (-1.70%)</td><td>13.85 (-1.67%)</td><td>12.71 (+0.99%)</td><td>0.54 <b>(-48.94%)</b></td><td>4383.10 (-0.98%)</td><td>4087.54 (+1.39%)</td><td>4021.90 (+1.70%)</td><td>3971.90 (+8.34%)</td><td>169.19 <b>(-45.20%)</b></td><td>13516.63 (-7.69%)</td><td>13151.50 (-1.70%)</td><td>13348.84 (-1.67%)</td><td>12248.66 (+0.99%)</td><td>518.98 <b>(-48.94%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>15.19 (n/a)</td><td>13.88 (n/a)</td><td>14.09 (n/a)</td><td>12.58 (n/a)</td><td>1.05 (n/a)</td><td>4426.50 (n/a)</td><td>4031.60 (n/a)</td><td>3954.60 (n/a)</td><td>3666.30 (n/a)</td><td>308.75 (n/a)</td><td>14643.24 (n/a)</td><td>13378.71 (n/a)</td><td>13575.69 (n/a)</td><td>12128.60 (n/a)</td><td>1016.38 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>15.07 (-10.98%)</td><td>12.38 (-16.79%)</td><td>10.76 <b>(-25.08%)</b></td><td>10.62 (-16.36%)</td><td>2.34 <b>(+21.90%)</b></td><td>1682.30 (+19.56%)</td><td>1481.86 <b>(+21.85%)</b></td><td>1660.40 <b>(+33.48%)</b></td><td>1185.20 (+12.33%)</td><td>261.95 <b>(+68.29%)</b></td><td>11324.08 (-10.98%)</td><td>9306.13 (-16.79%)</td><td>8083.53 <b>(-25.08%)</b></td><td>7978.34 (-16.36%)</td><td>1758.74 <b>(+21.90%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>16.93 (n/a)</td><td>14.88 (n/a)</td><td>14.36 (n/a)</td><td>12.69 (n/a)</td><td>1.92 (n/a)</td><td>1407.10 (n/a)</td><td>1216.16 (n/a)</td><td>1243.90 (n/a)</td><td>1055.10 (n/a)</td><td>155.65 (n/a)</td><td>12721.00 (n/a)</td><td>11183.56 (n/a)</td><td>10789.74 (n/a)</td><td>9538.75 (n/a)</td><td>1442.75 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>10.69 (+0.73%)</td><td>10.60 (+0.14%)</td><td>10.60 (+0.21%)</td><td>10.51 (-0.27%)</td><td>0.07 <b>(+160.83%)</b></td><td>7795.80 (+0.27%)</td><td>7731.94 (-0.14%)</td><td>7728.20 (-0.21%)</td><td>7664.10 (-0.72%)</td><td>54.38 <b>(+159.54%)</b></td><td>14010.08 (+0.73%)</td><td>13887.68 (+0.14%)</td><td>13893.88 (+0.21%)</td><td>13773.42 (-0.27%)</td><td>97.71 <b>(+160.84%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>10.61 (n/a)</td><td>10.58 (n/a)</td><td>10.58 (n/a)</td><td>10.54 (n/a)</td><td>0.03 (n/a)</td><td>7774.50 (n/a)</td><td>7742.78 (n/a)</td><td>7744.10 (n/a)</td><td>7719.90 (n/a)</td><td>20.95 (n/a)</td><td>13908.69 (n/a)</td><td>13867.74 (n/a)</td><td>13865.35 (n/a)</td><td>13811.09 (n/a)</td><td>37.46 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>15.34 (+4.05%)</td><td>14.37 (+15.65%)</td><td>14.70 <b>(+29.61%)</b></td><td>11.99 (+16.60%)</td><td>1.38 <b>(-34.33%)</b></td><td>1792.30 (-14.24%)</td><td>1508.74 (-14.73%)</td><td>1462.00 <b>(-22.85%)</b></td><td>1401.50 (-3.89%)</td><td>162.57 <b>(-43.51%)</b></td><td>12258.35 (+4.05%)</td><td>11481.79 (+15.65%)</td><td>11750.55 <b>(+29.61%)</b></td><td>9585.45 (+16.60%)</td><td>1101.45 <b>(-34.33%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>14.74 (n/a)</td><td>12.42 (n/a)</td><td>11.34 (n/a)</td><td>10.29 (n/a)</td><td>2.10 (n/a)</td><td>2089.80 (n/a)</td><td>1769.32 (n/a)</td><td>1895.00 (n/a)</td><td>1458.30 (n/a)</td><td>287.80 (n/a)</td><td>11780.94 (n/a)</td><td>9927.67 (n/a)</td><td>9065.90 (n/a)</td><td>8220.95 (n/a)</td><td>1677.22 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>10.94 (-0.73%)</td><td>10.63 (-0.74%)</td><td>10.51 (-2.10%)</td><td>10.36 (-0.19%)</td><td>0.27 (-8.57%)</td><td>7907.40 (+0.20%)</td><td>7712.98 (+0.74%)</td><td>7798.20 (+2.15%)</td><td>7487.00 (+0.73%)</td><td>192.91 (-8.01%)</td><td>14341.40 (-0.73%)</td><td>13928.26 (-0.74%)</td><td>13769.13 (-2.10%)</td><td>13578.97 (-0.19%)</td><td>350.76 (-8.57%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>11.02 (n/a)</td><td>10.71 (n/a)</td><td>10.73 (n/a)</td><td>10.38 (n/a)</td><td>0.29 (n/a)</td><td>7892.00 (n/a)</td><td>7656.36 (n/a)</td><td>7634.40 (n/a)</td><td>7432.60 (n/a)</td><td>209.71 (n/a)</td><td>14446.46 (n/a)</td><td>14032.61 (n/a)</td><td>14064.60 (n/a)</td><td>13605.49 (n/a)</td><td>383.64 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.02 <b>(-33.70%)</b></td><td>2.94 (-11.36%)</td><td>3.00 (-4.68%)</td><td>2.78 (+0.89%)</td><td>0.10 <b>(-85.70%)</b></td><td>495.60 (-0.88%)</td><td>467.96 (+9.62%)</td><td>459.40 (+4.91%)</td><td>456.40 <b>(+50.83%)</b></td><td>16.60 <b>(-77.63%)</b></td><td>588.14 <b>(-33.70%)</b></td><td>574.19 (-11.36%)</td><td>584.30 (-4.68%)</td><td>541.69 (+0.89%)</td><td>19.68 <b>(-85.70%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>4.55 (n/a)</td><td>3.32 (n/a)</td><td>3.14 (n/a)</td><td>2.75 (n/a)</td><td>0.71 (n/a)</td><td>500.00 (n/a)</td><td>426.90 (n/a)</td><td>437.90 (n/a)</td><td>302.60 (n/a)</td><td>74.21 (n/a)</td><td>887.14 (n/a)</td><td>647.79 (n/a)</td><td>612.96 (n/a)</td><td>536.90 (n/a)</td><td>137.60 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>4.17 (-2.42%)</td><td>3.69 (+1.91%)</td><td>3.63 (+0.81%)</td><td>3.31 (+13.44%)</td><td>0.32 <b>(-35.41%)</b></td><td>416.30 (-11.84%)</td><td>375.00 (-2.84%)</td><td>379.50 (-0.81%)</td><td>329.70 (+2.45%)</td><td>31.89 <b>(-42.60%)</b></td><td>814.09 (-2.42%)</td><td>720.08 (+1.91%)</td><td>707.34 (+0.81%)</td><td>644.84 (+13.44%)</td><td>62.72 <b>(-35.41%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>4.28 (n/a)</td><td>3.62 (n/a)</td><td>3.60 (n/a)</td><td>2.91 (n/a)</td><td>0.50 (n/a)</td><td>472.20 (n/a)</td><td>385.98 (n/a)</td><td>382.60 (n/a)</td><td>321.80 (n/a)</td><td>55.56 (n/a)</td><td>834.29 (n/a)</td><td>706.58 (n/a)</td><td>701.65 (n/a)</td><td>568.42 (n/a)</td><td>97.12 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>6.02 <b>(-25.74%)</b></td><td>4.23 (-18.02%)</td><td>3.94 (-10.41%)</td><td>3.52 (+0.05%)</td><td>1.02 <b>(-46.38%)</b></td><td>390.90 (-0.05%)</td><td>337.68 (+15.08%)</td><td>348.90 (+11.65%)</td><td>228.60 <b>(+34.71%)</b></td><td>64.26 <b>(-30.55%)</b></td><td>1174.29 <b>(-25.74%)</b></td><td>825.12 (-18.02%)</td><td>769.46 (-10.41%)</td><td>686.65 (+0.05%)</td><td>199.42 <b>(-46.38%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.11 (n/a)</td><td>5.16 (n/a)</td><td>4.40 (n/a)</td><td>3.52 (n/a)</td><td>1.91 (n/a)</td><td>391.10 (n/a)</td><td>293.42 (n/a)</td><td>312.50 (n/a)</td><td>169.70 (n/a)</td><td>92.52 (n/a)</td><td>1581.41 (n/a)</td><td>1006.42 (n/a)</td><td>858.87 (n/a)</td><td>686.32 (n/a)</td><td>371.91 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.03 <b>(+37.71%)</b></td><td>4.42 (-6.02%)</td><td>3.59 <b>(-25.88%)</b></td><td>3.30 (-3.25%)</td><td>2.03 <b>(+115.34%)</b></td><td>416.80 (+3.37%)</td><td>348.22 (+14.83%)</td><td>383.40 <b>(+34.90%)</b></td><td>171.30 <b>(-27.38%)</b></td><td>100.12 <b>(+52.28%)</b></td><td>1566.72 <b>(+37.71%)</b></td><td>861.38 (-6.02%)</td><td>700.13 <b>(-25.88%)</b></td><td>644.04 (-3.25%)</td><td>395.19 <b>(+115.34%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>5.83 (n/a)</td><td>4.70 (n/a)</td><td>4.84 (n/a)</td><td>3.41 (n/a)</td><td>0.94 (n/a)</td><td>403.20 (n/a)</td><td>303.26 (n/a)</td><td>284.20 (n/a)</td><td>235.90 (n/a)</td><td>65.75 (n/a)</td><td>1137.73 (n/a)</td><td>916.55 (n/a)</td><td>944.59 (n/a)</td><td>665.70 (n/a)</td><td>183.52 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.46 (-8.85%)</td><td>3.22 (-5.90%)</td><td>3.23 (-2.59%)</td><td>2.97 (-5.91%)</td><td>0.18 <b>(-30.77%)</b></td><td>464.10 (+6.30%)</td><td>428.86 (+6.07%)</td><td>426.40 (+2.65%)</td><td>397.50 (+9.69%)</td><td>23.66 (-18.44%)</td><td>675.25 (-8.85%)</td><td>627.43 (-5.90%)</td><td>629.49 (-2.59%)</td><td>578.45 (-5.91%)</td><td>34.30 <b>(-30.77%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>3.80 (n/a)</td><td>3.42 (n/a)</td><td>3.31 (n/a)</td><td>3.15 (n/a)</td><td>0.25 (n/a)</td><td>436.60 (n/a)</td><td>404.32 (n/a)</td><td>415.40 (n/a)</td><td>362.40 (n/a)</td><td>29.01 (n/a)</td><td>740.80 (n/a)</td><td>666.77 (n/a)</td><td>646.21 (n/a)</td><td>614.79 (n/a)</td><td>49.54 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.86 <b>(-25.78%)</b></td><td>3.10 (-19.32%)</td><td>2.86 (-12.90%)</td><td>2.74 (-5.60%)</td><td>0.47 <b>(-57.77%)</b></td><td>502.00 (+5.93%)</td><td>450.54 (+18.37%)</td><td>482.00 (+14.82%)</td><td>356.20 <b>(+34.72%)</b></td><td>60.61 <b>(-39.61%)</b></td><td>753.59 <b>(-25.78%)</b></td><td>605.56 (-19.32%)</td><td>556.92 (-12.90%)</td><td>534.74 (-5.60%)</td><td>91.13 <b>(-57.77%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>5.21 (n/a)</td><td>3.85 (n/a)</td><td>3.28 (n/a)</td><td>2.90 (n/a)</td><td>1.11 (n/a)</td><td>473.90 (n/a)</td><td>380.62 (n/a)</td><td>419.80 (n/a)</td><td>264.40 (n/a)</td><td>100.36 (n/a)</td><td>1015.40 (n/a)</td><td>750.61 (n/a)</td><td>639.44 (n/a)</td><td>566.48 (n/a)</td><td>215.76 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.21 <b>(-32.33%)</b></td><td>3.13 (-14.13%)</td><td>3.12 (-2.89%)</td><td>3.09 (+5.42%)</td><td>0.05 <b>(-93.95%)</b></td><td>445.20 (-5.14%)</td><td>439.56 (+12.73%)</td><td>441.30 (+2.96%)</td><td>429.00 <b>(+47.78%)</b></td><td>6.43 <b>(-91.46%)</b></td><td>625.67 <b>(-32.33%)</b></td><td>610.78 (-14.13%)</td><td>608.22 (-2.89%)</td><td>602.97 (+5.42%)</td><td>9.02 <b>(-93.95%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>4.74 (n/a)</td><td>3.65 (n/a)</td><td>3.21 (n/a)</td><td>2.93 (n/a)</td><td>0.77 (n/a)</td><td>469.30 (n/a)</td><td>389.94 (n/a)</td><td>428.60 (n/a)</td><td>290.30 (n/a)</td><td>75.27 (n/a)</td><td>924.55 (n/a)</td><td>711.31 (n/a)</td><td>626.31 (n/a)</td><td>571.96 (n/a)</td><td>149.25 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.91 <b>(+61.01%)</b></td><td>1.33 <b>(+21.57%)</b></td><td>1.19 (+8.58%)</td><td>0.98 (-1.85%)</td><td>0.39 <b>(+476.55%)</b></td><td>411.30 (+1.88%)</td><td>321.90 (-12.73%)</td><td>336.50 (-7.91%)</td><td>210.70 <b>(-37.88%)</b></td><td>84.35 <b>(+265.68%)</b></td><td>159.27 <b>(+61.01%)</b></td><td>110.93 <b>(+21.57%)</b></td><td>99.70 (+8.58%)</td><td>81.59 (-1.85%)</td><td>32.42 <b>(+476.54%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.18 (n/a)</td><td>1.09 (n/a)</td><td>1.10 (n/a)</td><td>0.99 (n/a)</td><td>0.07 (n/a)</td><td>403.70 (n/a)</td><td>368.84 (n/a)</td><td>365.40 (n/a)</td><td>339.20 (n/a)</td><td>23.07 (n/a)</td><td>98.92 (n/a)</td><td>91.25 (n/a)</td><td>91.83 (n/a)</td><td>83.12 (n/a)</td><td>5.62 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>5.20 <b>(-33.08%)</b></td><td>4.79 <b>(-21.30%)</b></td><td>4.67 (-11.45%)</td><td>4.62 (+0.25%)</td><td>0.24 <b>(-84.55%)</b></td><td>418.10 (-0.24%)</td><td>404.78 <b>(+21.05%)</b></td><td>414.30 (+12.92%)</td><td>371.60 <b>(+49.42%)</b></td><td>19.32 <b>(-75.92%)</b></td><td>1083.43 <b>(-33.08%)</b></td><td>996.65 <b>(-21.30%)</b></td><td>971.92 (-11.45%)</td><td>963.16 (+0.25%)</td><td>50.19 <b>(-84.55%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>7.77 (n/a)</td><td>6.08 (n/a)</td><td>5.27 (n/a)</td><td>4.61 (n/a)</td><td>1.56 (n/a)</td><td>419.10 (n/a)</td><td>334.38 (n/a)</td><td>366.90 (n/a)</td><td>248.70 (n/a)</td><td>80.25 (n/a)</td><td>1619.01 (n/a)</td><td>1266.37 (n/a)</td><td>1097.54 (n/a)</td><td>960.72 (n/a)</td><td>324.78 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>16.89 (-12.15%)</td><td>13.27 (-10.72%)</td><td>13.46 (-8.82%)</td><td>10.51 (-0.63%)</td><td>2.37 <b>(-24.91%)</b></td><td>523.70 (+0.63%)</td><td>425.06 (+10.49%)</td><td>408.90 (+9.68%)</td><td>326.00 (+13.83%)</td><td>73.08 (-15.79%)</td><td>6588.18 (-12.15%)</td><td>5177.93 (-10.72%)</td><td>5252.28 (-8.82%)</td><td>4100.64 (-0.63%)</td><td>925.35 <b>(-24.91%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>19.22 (n/a)</td><td>14.87 (n/a)</td><td>14.77 (n/a)</td><td>10.58 (n/a)</td><td>3.16 (n/a)</td><td>520.40 (n/a)</td><td>384.72 (n/a)</td><td>372.80 (n/a)</td><td>286.40 (n/a)</td><td>86.78 (n/a)</td><td>7499.38 (n/a)</td><td>5799.70 (n/a)</td><td>5760.42 (n/a)</td><td>4126.44 (n/a)</td><td>1232.29 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.47 (-15.90%)</td><td>7.92 (-0.05%)</td><td>7.80 (+2.81%)</td><td>7.59 (+18.47%)</td><td>0.34 <b>(-75.10%)</b></td><td>725.70 (-15.60%)</td><td>696.42 (-1.99%)</td><td>705.40 (-2.73%)</td><td>650.10 (+18.91%)</td><td>28.82 <b>(-74.73%)</b></td><td>3303.44 (-15.90%)</td><td>3088.01 (-0.05%)</td><td>3044.35 (+2.81%)</td><td>2959.03 (+18.47%)</td><td>132.11 <b>(-75.10%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>10.07 (n/a)</td><td>7.92 (n/a)</td><td>7.59 (n/a)</td><td>6.40 (n/a)</td><td>1.36 (n/a)</td><td>859.80 (n/a)</td><td>710.54 (n/a)</td><td>725.20 (n/a)</td><td>546.70 (n/a)</td><td>114.04 (n/a)</td><td>3928.22 (n/a)</td><td>3089.62 (n/a)</td><td>2961.22 (n/a)</td><td>2497.66 (n/a)</td><td>530.56 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>9.36 (-18.28%)</td><td>8.44 (-14.31%)</td><td>8.79 (-6.46%)</td><td>6.40 <b>(-20.78%)</b></td><td>1.17 (-19.09%)</td><td>906.70 <b>(+26.23%)</b></td><td>700.04 (+16.85%)</td><td>659.90 (+6.90%)</td><td>619.60 <b>(+22.38%)</b></td><td>117.01 <b>(+32.02%)</b></td><td>3899.18 (-18.28%)</td><td>3516.28 (-14.31%)</td><td>3660.90 (-6.46%)</td><td>2664.57 <b>(-20.78%)</b></td><td>488.35 (-19.09%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>11.46 (n/a)</td><td>9.85 (n/a)</td><td>9.40 (n/a)</td><td>8.07 (n/a)</td><td>1.45 (n/a)</td><td>718.30 (n/a)</td><td>599.10 (n/a)</td><td>617.30 (n/a)</td><td>506.30 (n/a)</td><td>88.63 (n/a)</td><td>4771.68 (n/a)</td><td>4103.73 (n/a)</td><td>3913.66 (n/a)</td><td>3363.49 (n/a)</td><td>603.56 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>240.10 (n/a)</td><td>176.24 (n/a)</td><td>163.70 (n/a)</td><td>151.80 (n/a)</td><td>36.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>202.00 (n/a)</td><td>171.92 (n/a)</td><td>172.70 (n/a)</td><td>142.10 (n/a)</td><td>24.50 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>179.90 (n/a)</td><td>162.86 (n/a)</td><td>159.80 (n/a)</td><td>154.70 (n/a)</td><td>10.44 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>201.70 (n/a)</td><td>170.52 (n/a)</td><td>173.20 (n/a)</td><td>123.90 (n/a)</td><td>29.30 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>185.20 (n/a)</td><td>158.98 (n/a)</td><td>158.00 (n/a)</td><td>139.50 (n/a)</td><td>17.81 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>187.80 (n/a)</td><td>150.96 (n/a)</td><td>141.00 (n/a)</td><td>118.70 (n/a)</td><td>27.99 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>244.10 (n/a)</td><td>169.86 (n/a)</td><td>186.80 (n/a)</td><td>94.90 (n/a)</td><td>57.50 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>285.50 (n/a)</td><td>209.72 (n/a)</td><td>200.70 (n/a)</td><td>173.00 (n/a)</td><td>44.53 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>226.70 (n/a)</td><td>184.70 (n/a)</td><td>180.30 (n/a)</td><td>151.50 (n/a)</td><td>34.61 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>376.60 (n/a)</td><td>202.94 (n/a)</td><td>159.70 (n/a)</td><td>132.40 (n/a)</td><td>100.39 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>264.30 (n/a)</td><td>156.82 (n/a)</td><td>129.60 (n/a)</td><td>123.90 (n/a)</td><td>60.29 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>365.70 (n/a)</td><td>204.04 (n/a)</td><td>172.20 (n/a)</td><td>147.90 (n/a)</td><td>91.09 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>175.30 (n/a)</td><td>155.50 (n/a)</td><td>149.80 (n/a)</td><td>141.80 (n/a)</td><td>13.75 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>321.70 (n/a)</td><td>223.60 (n/a)</td><td>185.50 (n/a)</td><td>160.50 (n/a)</td><td>70.07 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.60 (n/a)</td><td>185.70 (n/a)</td><td>191.70 (n/a)</td><td>137.90 (n/a)</td><td>34.56 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>247.00 (n/a)</td><td>223.20 (n/a)</td><td>222.00 (n/a)</td><td>205.70 (n/a)</td><td>17.63 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>190.80 (n/a)</td><td>176.48 (n/a)</td><td>181.50 (n/a)</td><td>158.90 (n/a)</td><td>12.50 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>200.70 (n/a)</td><td>141.44 (n/a)</td><td>131.80 (n/a)</td><td>104.80 (n/a)</td><td>35.78 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>182.40 (n/a)</td><td>165.50 (n/a)</td><td>160.40 (n/a)</td><td>153.30 (n/a)</td><td>11.37 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>156.40 (n/a)</td><td>135.68 (n/a)</td><td>134.00 (n/a)</td><td>117.60 (n/a)</td><td>15.49 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>309.30 (n/a)</td><td>181.72 (n/a)</td><td>145.60 (n/a)</td><td>130.80 (n/a)</td><td>74.60 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>346.30 (n/a)</td><td>204.12 (n/a)</td><td>173.90 (n/a)</td><td>136.80 (n/a)</td><td>83.04 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>238.50 (n/a)</td><td>184.04 (n/a)</td><td>192.10 (n/a)</td><td>134.80 (n/a)</td><td>40.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>230.40 (n/a)</td><td>202.62 (n/a)</td><td>207.10 (n/a)</td><td>167.30 (n/a)</td><td>25.55 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>212.30 (n/a)</td><td>174.28 (n/a)</td><td>186.40 (n/a)</td><td>129.90 (n/a)</td><td>36.63 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>236.80 (n/a)</td><td>183.62 (n/a)</td><td>170.50 (n/a)</td><td>151.50 (n/a)</td><td>32.64 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>253.90 (n/a)</td><td>208.80 (n/a)</td><td>211.60 (n/a)</td><td>168.20 (n/a)</td><td>30.87 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>204.90 (n/a)</td><td>177.92 (n/a)</td><td>184.00 (n/a)</td><td>149.90 (n/a)</td><td>21.45 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>219.20 (n/a)</td><td>192.70 (n/a)</td><td>203.10 (n/a)</td><td>155.80 (n/a)</td><td>28.54 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>228.10 (n/a)</td><td>202.04 (n/a)</td><td>199.40 (n/a)</td><td>161.00 (n/a)</td><td>26.97 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>197.10 (n/a)</td><td>175.96 (n/a)</td><td>167.20 (n/a)</td><td>157.90 (n/a)</td><td>16.95 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>237.40 (n/a)</td><td>208.58 (n/a)</td><td>211.50 (n/a)</td><td>162.70 (n/a)</td><td>28.03 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>4.12 (-0.84%)</td><td>4.11 (-0.25%)</td><td>4.11 (+0.00%)</td><td>4.09 (-0.25%)</td><td>0.01 <b>(-46.95%)</b></td><td>19223.20 (+0.25%)</td><td>19140.16 (+0.25%)</td><td>19124.70 (-0.00%)</td><td>19080.10 (+0.84%)</td><td>53.91 <b>(-46.29%)</b></td><td>2813.78 (-0.84%)</td><td>2804.96 (-0.25%)</td><td>2807.21 (+0.00%)</td><td>2792.83 (-0.25%)</td><td>7.89 <b>(-46.95%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>4.16 (n/a)</td><td>4.12 (n/a)</td><td>4.11 (n/a)</td><td>4.10 (n/a)</td><td>0.02 (n/a)</td><td>19174.90 (n/a)</td><td>19092.26 (n/a)</td><td>19125.20 (n/a)</td><td>18920.30 (n/a)</td><td>100.39 (n/a)</td><td>2837.54 (n/a)</td><td>2812.04 (n/a)</td><td>2807.14 (n/a)</td><td>2799.86 (n/a)</td><td>14.87 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>4.25 (-10.97%)</td><td>4.11 (+1.18%)</td><td>4.12 (-0.79%)</td><td>3.89 (+10.13%)</td><td>0.14 <b>(-73.55%)</b></td><td>2415.20 (-9.20%)</td><td>2292.40 (-2.40%)</td><td>2281.10 (+0.80%)</td><td>2210.20 (+12.32%)</td><td>79.78 <b>(-73.74%)</b></td><td>1673.76 (-10.97%)</td><td>1615.28 (+1.18%)</td><td>1621.72 (-0.79%)</td><td>1531.69 (+10.13%)</td><td>55.18 <b>(-73.55%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>4.78 (n/a)</td><td>4.06 (n/a)</td><td>4.16 (n/a)</td><td>3.54 (n/a)</td><td>0.53 (n/a)</td><td>2659.90 (n/a)</td><td>2348.86 (n/a)</td><td>2263.10 (n/a)</td><td>1967.80 (n/a)</td><td>303.78 (n/a)</td><td>1879.94 (n/a)</td><td>1596.46 (n/a)</td><td>1634.63 (n/a)</td><td>1390.81 (n/a)</td><td>208.64 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.12 (-1.23%)</td><td>0.95 (-2.67%)</td><td>0.93 (-4.80%)</td><td>0.80 (-1.83%)</td><td>0.12 (+4.90%)</td><td>275.40 (+1.89%)</td><td>236.98 (+2.90%)</td><td>238.80 (+5.06%)</td><td>196.80 (+1.23%)</td><td>29.44 (+7.48%)</td><td>47.95 (-1.23%)</td><td>40.33 (-2.67%)</td><td>39.52 (-4.80%)</td><td>34.27 (-1.83%)</td><td>5.15 (+4.90%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.14 (n/a)</td><td>0.97 (n/a)</td><td>0.97 (n/a)</td><td>0.82 (n/a)</td><td>0.12 (n/a)</td><td>270.30 (n/a)</td><td>230.30 (n/a)</td><td>227.30 (n/a)</td><td>194.40 (n/a)</td><td>27.39 (n/a)</td><td>48.55 (n/a)</td><td>41.44 (n/a)</td><td>41.51 (n/a)</td><td>34.91 (n/a)</td><td>4.91 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.37 <b>(+24.39%)</b></td><td>1.08 (+16.11%)</td><td>1.05 (+12.03%)</td><td>0.86 <b>(+24.11%)</b></td><td>0.23 <b>(+41.81%)</b></td><td>258.30 (-19.41%)</td><td>213.02 (-13.15%)</td><td>211.20 (-10.74%)</td><td>161.00 (-19.62%)</td><td>43.79 (-6.75%)</td><td>58.61 <b>(+24.39%)</b></td><td>45.88 (+16.11%)</td><td>44.68 (+12.03%)</td><td>36.54 <b>(+24.11%)</b></td><td>9.68 <b>(+41.81%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.10 (n/a)</td><td>0.93 (n/a)</td><td>0.93 (n/a)</td><td>0.69 (n/a)</td><td>0.16 (n/a)</td><td>320.50 (n/a)</td><td>245.26 (n/a)</td><td>236.60 (n/a)</td><td>200.30 (n/a)</td><td>46.96 (n/a)</td><td>47.12 (n/a)</td><td>39.51 (n/a)</td><td>39.88 (n/a)</td><td>29.44 (n/a)</td><td>6.83 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.53 (-0.05%)</td><td>0.53 (-0.03%)</td><td>0.53 (-0.01%)</td><td>0.53 (-0.00%)</td><td>0.00 <b>(-21.96%)</b></td><td>47872.30 (+0.00%)</td><td>47834.04 (+0.03%)</td><td>47817.30 (+0.01%)</td><td>47814.40 (+0.05%)</td><td>25.68 <b>(-21.95%)</b></td><td>359.30 (-0.05%)</td><td>359.16 (-0.03%)</td><td>359.28 (-0.01%)</td><td>358.87 (-0.00%)</td><td>0.19 <b>(-21.95%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.53 (n/a)</td><td>0.00 (n/a)</td><td>47871.60 (n/a)</td><td>47818.72 (n/a)</td><td>47811.10 (n/a)</td><td>47790.30 (n/a)</td><td>32.90 (n/a)</td><td>359.48 (n/a)</td><td>359.27 (n/a)</td><td>359.33 (n/a)</td><td>358.87 (n/a)</td><td>0.25 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (-1.35%)</td><td>0.21 (-0.49%)</td><td>0.21 (-0.19%)</td><td>0.21 (-1.06%)</td><td>0.00 (-12.17%)</td><td>120635.40 (+1.07%)</td><td>118604.84 (+0.49%)</td><td>118540.00 (+0.19%)</td><td>116873.70 (+1.36%)</td><td>1485.00 (-9.97%)</td><td>147.00 (-1.35%)</td><td>144.87 (-0.49%)</td><td>144.93 (-0.19%)</td><td>142.41 (-1.06%)</td><td>1.81 (-12.17%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.22 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.00 (n/a)</td><td>119356.50 (n/a)</td><td>118029.34 (n/a)</td><td>118313.40 (n/a)</td><td>115300.50 (n/a)</td><td>1649.36 (n/a)</td><td>149.00 (n/a)</td><td>145.58 (n/a)</td><td>145.21 (n/a)</td><td>143.94 (n/a)</td><td>2.06 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.90 (-0.23%)</td><td>0.90 (-0.08%)</td><td>0.90 (+0.26%)</td><td>0.90 (-0.29%)</td><td>0.00 (+17.52%)</td><td>28094.60 (+0.29%)</td><td>27911.78 (+0.08%)</td><td>27847.20 (-0.26%)</td><td>27814.00 (+0.23%)</td><td>122.82 (+18.10%)</td><td>617.67 (-0.23%)</td><td>615.52 (-0.08%)</td><td>616.93 (+0.26%)</td><td>611.50 (-0.29%)</td><td>2.70 (+17.52%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.91 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.90 (n/a)</td><td>0.00 (n/a)</td><td>28013.00 (n/a)</td><td>27890.30 (n/a)</td><td>27918.40 (n/a)</td><td>27749.80 (n/a)</td><td>104.00 (n/a)</td><td>619.10 (n/a)</td><td>615.99 (n/a)</td><td>615.36 (n/a)</td><td>613.28 (n/a)</td><td>2.30 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.64 (-0.95%)</td><td>3.59 (+0.65%)</td><td>3.62 (-0.25%)</td><td>3.45 (+0.86%)</td><td>0.08 <b>(-35.24%)</b></td><td>7285.70 (-0.85%)</td><td>7013.48 (-0.70%)</td><td>6954.30 (+0.26%)</td><td>6912.90 (+0.96%)</td><td>153.48 <b>(-35.04%)</b></td><td>2485.19 (-0.95%)</td><td>2450.46 (+0.65%)</td><td>2470.39 (-0.25%)</td><td>2358.03 (+0.86%)</td><td>52.16 <b>(-35.24%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>3.68 (n/a)</td><td>3.57 (n/a)</td><td>3.63 (n/a)</td><td>3.42 (n/a)</td><td>0.12 (n/a)</td><td>7348.10 (n/a)</td><td>7062.72 (n/a)</td><td>6936.60 (n/a)</td><td>6847.00 (n/a)</td><td>236.27 (n/a)</td><td>2509.11 (n/a)</td><td>2434.62 (n/a)</td><td>2476.68 (n/a)</td><td>2338.00 (n/a)</td><td>80.55 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.13 (+3.69%)</td><td>2.91 (+3.10%)</td><td>2.90 (+1.86%)</td><td>2.78 (+4.66%)</td><td>0.13 (-0.89%)</td><td>9059.70 (-4.46%)</td><td>8648.42 (-3.02%)</td><td>8686.30 (-1.83%)</td><td>8046.40 (-3.56%)</td><td>383.29 (-9.17%)</td><td>2135.10 (+3.69%)</td><td>1989.69 (+3.10%)</td><td>1977.81 (+1.86%)</td><td>1896.30 (+4.66%)</td><td>90.83 (-0.89%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>3.02 (n/a)</td><td>2.83 (n/a)</td><td>2.84 (n/a)</td><td>2.65 (n/a)</td><td>0.13 (n/a)</td><td>9482.30 (n/a)</td><td>8917.86 (n/a)</td><td>8847.90 (n/a)</td><td>8343.40 (n/a)</td><td>422.01 (n/a)</td><td>2059.10 (n/a)</td><td>1929.92 (n/a)</td><td>1941.68 (n/a)</td><td>1811.78 (n/a)</td><td>91.65 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.30 (-1.25%)</td><td>3.20 (-1.34%)</td><td>3.18 (-1.40%)</td><td>3.12 (-0.96%)</td><td>0.08 (-7.54%)</td><td>8063.20 (+0.97%)</td><td>7876.86 (+1.35%)</td><td>7902.10 (+1.42%)</td><td>7637.10 (+1.26%)</td><td>186.33 (-5.29%)</td><td>2249.51 (-1.25%)</td><td>2182.03 (-1.34%)</td><td>2174.08 (-1.40%)</td><td>2130.66 (-0.96%)</td><td>51.88 (-7.54%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>3.34 (n/a)</td><td>3.24 (n/a)</td><td>3.23 (n/a)</td><td>3.15 (n/a)</td><td>0.08 (n/a)</td><td>7985.90 (n/a)</td><td>7772.20 (n/a)</td><td>7791.20 (n/a)</td><td>7541.70 (n/a)</td><td>196.73 (n/a)</td><td>2277.97 (n/a)</td><td>2211.56 (n/a)</td><td>2205.04 (n/a)</td><td>2151.28 (n/a)</td><td>56.11 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.80 (-0.00%)</td><td>0.80 (-0.05%)</td><td>0.80 (-0.10%)</td><td>0.80 (-0.01%)</td><td>0.00 (+11.14%)</td><td>94872.30 (+0.01%)</td><td>94840.20 (+0.05%)</td><td>94870.30 (+0.10%)</td><td>94768.20 (+0.00%)</td><td>46.15 (+11.24%)</td><td>725.13 (-0.00%)</td><td>724.58 (-0.05%)</td><td>724.35 (-0.10%)</td><td>724.34 (-0.01%)</td><td>0.35 (+11.15%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94862.30 (n/a)</td><td>94788.88 (n/a)</td><td>94774.00 (n/a)</td><td>94764.40 (n/a)</td><td>41.49 (n/a)</td><td>725.16 (n/a)</td><td>724.97 (n/a)</td><td>725.09 (n/a)</td><td>724.41 (n/a)</td><td>0.32 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.73 (+0.36%)</td><td>0.73 (+0.17%)</td><td>0.73 (+0.04%)</td><td>0.73 (+0.12%)</td><td>0.00 <b>(+196.17%)</b></td><td>103329.60 (-0.12%)</td><td>103167.04 (-0.17%)</td><td>103285.80 (-0.04%)</td><td>102913.30 (-0.36%)</td><td>195.50 <b>(+194.86%)</b></td><td>667.74 (+0.36%)</td><td>666.10 (+0.17%)</td><td>665.33 (+0.04%)</td><td>665.05 (+0.12%)</td><td>1.26 <b>(+196.20%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.73 (n/a)</td><td>0.00 (n/a)</td><td>103452.50 (n/a)</td><td>103342.00 (n/a)</td><td>103327.40 (n/a)</td><td>103283.80 (n/a)</td><td>66.30 (n/a)</td><td>665.35 (n/a)</td><td>664.97 (n/a)</td><td>665.07 (n/a)</td><td>664.26 (n/a)</td><td>0.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.69 (+0.10%)</td><td>0.68 (+0.01%)</td><td>0.68 (-0.26%)</td><td>0.68 (+0.29%)</td><td>0.00 (-18.55%)</td><td>110662.10 (-0.29%)</td><td>110382.84 (-0.01%)</td><td>110527.70 (+0.26%)</td><td>109932.70 (-0.10%)</td><td>297.84 (-18.90%)</td><td>625.10 (+0.10%)</td><td>622.56 (+0.01%)</td><td>621.74 (-0.26%)</td><td>620.98 (+0.29%)</td><td>1.68 (-18.55%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.69 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.68 (n/a)</td><td>0.00 (n/a)</td><td>110981.20 (n/a)</td><td>110395.54 (n/a)</td><td>110241.30 (n/a)</td><td>110044.10 (n/a)</td><td>367.25 (n/a)</td><td>624.47 (n/a)</td><td>622.49 (n/a)</td><td>623.36 (n/a)</td><td>619.20 (n/a)</td><td>2.07 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>2.81 (+0.42%)</td><td>2.80 (+0.04%)</td><td>2.79 (-0.09%)</td><td>2.79 (-0.09%)</td><td>0.01 <b>(+136.19%)</b></td><td>37624.60 (+0.09%)</td><td>37505.70 (-0.04%)</td><td>37532.50 (+0.09%)</td><td>37326.60 (-0.41%)</td><td>110.85 <b>(+135.34%)</b></td><td>2876.62 (+0.42%)</td><td>2862.90 (+0.04%)</td><td>2860.83 (-0.09%)</td><td>2853.83 (-0.09%)</td><td>8.48 <b>(+136.17%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>2.80 (n/a)</td><td>2.79 (n/a)</td><td>0.00 (n/a)</td><td>37590.40 (n/a)</td><td>37521.32 (n/a)</td><td>37497.20 (n/a)</td><td>37482.10 (n/a)</td><td>47.10 (n/a)</td><td>2864.68 (n/a)</td><td>2861.69 (n/a)</td><td>2863.52 (n/a)</td><td>2856.42 (n/a)</td><td>3.59 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>7.39 (-0.73%)</td><td>7.11 (+3.87%)</td><td>7.14 (+5.01%)</td><td>6.87 (+6.51%)</td><td>0.23 <b>(-37.49%)</b></td><td>1297.20 (-6.12%)</td><td>1254.66 (-3.86%)</td><td>1249.10 (-4.77%)</td><td>1206.20 (+0.73%)</td><td>40.56 <b>(-40.03%)</b></td><td>445.09 (-0.73%)</td><td>428.25 (+3.87%)</td><td>429.79 (+5.01%)</td><td>413.86 (+6.51%)</td><td>13.85 <b>(-37.49%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>7.44 (n/a)</td><td>6.85 (n/a)</td><td>6.80 (n/a)</td><td>6.45 (n/a)</td><td>0.37 (n/a)</td><td>1381.70 (n/a)</td><td>1304.98 (n/a)</td><td>1311.70 (n/a)</td><td>1197.40 (n/a)</td><td>67.64 (n/a)</td><td>448.36 (n/a)</td><td>412.32 (n/a)</td><td>409.30 (n/a)</td><td>388.55 (n/a)</td><td>22.16 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>6.84 (-0.36%)</td><td>6.35 (-1.63%)</td><td>6.72 (-0.84%)</td><td>4.70 (-7.09%)</td><td>0.92 (+18.27%)</td><td>1894.70 (+7.64%)</td><td>1433.00 (+2.39%)</td><td>1326.60 (+0.85%)</td><td>1303.80 (+0.37%)</td><td>258.35 <b>(+28.01%)</b></td><td>411.78 (-0.36%)</td><td>382.68 (-1.63%)</td><td>404.71 (-0.84%)</td><td>283.36 (-7.09%)</td><td>55.63 (+18.27%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>6.86 (n/a)</td><td>6.46 (n/a)</td><td>6.78 (n/a)</td><td>5.06 (n/a)</td><td>0.78 (n/a)</td><td>1760.30 (n/a)</td><td>1399.52 (n/a)</td><td>1315.40 (n/a)</td><td>1299.00 (n/a)</td><td>201.82 (n/a)</td><td>413.28 (n/a)</td><td>389.04 (n/a)</td><td>408.14 (n/a)</td><td>304.99 (n/a)</td><td>47.04 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>6.92 (-1.77%)</td><td>6.41 (+6.20%)</td><td>6.25 (+1.00%)</td><td>6.01 <b>(+30.86%)</b></td><td>0.44 <b>(-50.69%)</b></td><td>1482.40 <b>(-23.58%)</b></td><td>1396.32 (-7.37%)</td><td>1425.50 (-0.99%)</td><td>1288.10 (+1.80%)</td><td>94.56 <b>(-62.94%)</b></td><td>416.79 (-1.77%)</td><td>385.93 (+6.20%)</td><td>376.62 (+1.00%)</td><td>362.16 <b>(+30.86%)</b></td><td>26.57 <b>(-50.69%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>7.04 (n/a)</td><td>6.03 (n/a)</td><td>6.19 (n/a)</td><td>4.59 (n/a)</td><td>0.89 (n/a)</td><td>1939.80 (n/a)</td><td>1507.34 (n/a)</td><td>1439.80 (n/a)</td><td>1265.30 (n/a)</td><td>255.13 (n/a)</td><td>424.31 (n/a)</td><td>363.41 (n/a)</td><td>372.88 (n/a)</td><td>276.76 (n/a)</td><td>53.88 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.10 (+0.17%)</td><td>7.71 (-3.73%)</td><td>7.94 (-1.03%)</td><td>7.06 (-10.47%)</td><td>0.44 <b>(+506.33%)</b></td><td>4936.80 (+11.69%)</td><td>4533.94 (+4.15%)</td><td>4390.90 (+1.04%)</td><td>4305.10 (-0.17%)</td><td>268.45 <b>(+573.38%)</b></td><td>498.82 (+0.17%)</td><td>474.93 (-3.73%)</td><td>489.08 (-1.03%)</td><td>434.99 (-10.47%)</td><td>27.16 <b>(+506.33%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.08 (n/a)</td><td>8.01 (n/a)</td><td>8.02 (n/a)</td><td>7.89 (n/a)</td><td>0.07 (n/a)</td><td>4419.90 (n/a)</td><td>4353.46 (n/a)</td><td>4345.70 (n/a)</td><td>4312.40 (n/a)</td><td>39.87 (n/a)</td><td>497.98 (n/a)</td><td>493.32 (n/a)</td><td>494.16 (n/a)</td><td>485.87 (n/a)</td><td>4.48 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>7.91 (+0.23%)</td><td>7.50 (-0.15%)</td><td>7.59 (-0.40%)</td><td>6.85 (+1.70%)</td><td>0.39 (-13.36%)</td><td>5087.40 (-1.68%)</td><td>4657.06 (+0.07%)</td><td>4595.80 (+0.40%)</td><td>4408.60 (-0.23%)</td><td>253.96 (-14.99%)</td><td>487.11 (+0.23%)</td><td>462.17 (-0.15%)</td><td>467.27 (-0.40%)</td><td>422.12 (+1.70%)</td><td>23.99 (-13.36%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>7.89 (n/a)</td><td>7.51 (n/a)</td><td>7.62 (n/a)</td><td>6.74 (n/a)</td><td>0.45 (n/a)</td><td>5174.10 (n/a)</td><td>4653.72 (n/a)</td><td>4577.30 (n/a)</td><td>4418.60 (n/a)</td><td>298.75 (n/a)</td><td>486.01 (n/a)</td><td>462.88 (n/a)</td><td>469.16 (n/a)</td><td>415.05 (n/a)</td><td>27.69 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>7.53 (+0.05%)</td><td>7.37 (+2.84%)</td><td>7.51 (+3.61%)</td><td>6.89 (+0.71%)</td><td>0.28 (-11.62%)</td><td>5063.50 (-0.70%)</td><td>4736.76 (-2.80%)</td><td>4645.20 (-3.48%)</td><td>4627.20 (-0.05%)</td><td>186.05 (-12.85%)</td><td>464.10 (+0.05%)</td><td>453.90 (+2.84%)</td><td>462.30 (+3.61%)</td><td>424.11 (+0.71%)</td><td>17.01 (-11.62%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>7.53 (n/a)</td><td>7.17 (n/a)</td><td>7.24 (n/a)</td><td>6.84 (n/a)</td><td>0.31 (n/a)</td><td>5099.20 (n/a)</td><td>4873.00 (n/a)</td><td>4812.90 (n/a)</td><td>4629.50 (n/a)</td><td>213.48 (n/a)</td><td>463.87 (n/a)</td><td>441.37 (n/a)</td><td>446.20 (n/a)</td><td>421.14 (n/a)</td><td>19.25 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.80 (-0.01%)</td><td>0.80 (-0.02%)</td><td>0.80 (+0.01%)</td><td>0.80 (-0.09%)</td><td>0.00 <b>(+78.32%)</b></td><td>94233.00 (+0.09%)</td><td>94089.96 (+0.02%)</td><td>94053.50 (-0.01%)</td><td>94042.30 (+0.01%)</td><td>80.99 <b>(+78.47%)</b></td><td>730.73 (-0.01%)</td><td>730.36 (-0.02%)</td><td>730.64 (+0.01%)</td><td>729.25 (-0.09%)</td><td>0.63 <b>(+78.32%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.80 (n/a)</td><td>0.00 (n/a)</td><td>94145.60 (n/a)</td><td>94072.40 (n/a)</td><td>94061.90 (n/a)</td><td>94029.70 (n/a)</td><td>45.38 (n/a)</td><td>730.83 (n/a)</td><td>730.50 (n/a)</td><td>730.58 (n/a)</td><td>729.93 (n/a)</td><td>0.35 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.74 (+0.25%)</td><td>0.74 (+0.02%)</td><td>0.74 (+0.00%)</td><td>0.73 (-0.11%)</td><td>0.00 <b>(+279.28%)</b></td><td>102797.60 (+0.11%)</td><td>102593.50 (-0.02%)</td><td>102615.70 (-0.00%)</td><td>102302.20 (-0.25%)</td><td>180.30 <b>(+278.74%)</b></td><td>671.73 (+0.25%)</td><td>669.82 (+0.02%)</td><td>669.68 (+0.00%)</td><td>668.49 (-0.11%)</td><td>1.18 <b>(+279.32%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.74 (n/a)</td><td>0.00 (n/a)</td><td>102681.90 (n/a)</td><td>102610.86 (n/a)</td><td>102616.80 (n/a)</td><td>102554.40 (n/a)</td><td>47.61 (n/a)</td><td>670.08 (n/a)</td><td>669.71 (n/a)</td><td>669.67 (n/a)</td><td>669.25 (n/a)</td><td>0.31 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.71 (+0.06%)</td><td>0.71 (+0.05%)</td><td>0.71 (-0.03%)</td><td>0.71 (+0.25%)</td><td>0.00 <b>(-45.58%)</b></td><td>106090.00 (-0.25%)</td><td>105923.70 (-0.05%)</td><td>105914.20 (+0.03%)</td><td>105777.10 (-0.06%)</td><td>115.34 <b>(-45.75%)</b></td><td>649.66 (+0.06%)</td><td>648.76 (+0.05%)</td><td>648.82 (-0.03%)</td><td>647.75 (+0.25%)</td><td>0.71 <b>(-45.58%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.71 (n/a)</td><td>0.00 (n/a)</td><td>106350.70 (n/a)</td><td>105972.72 (n/a)</td><td>105887.70 (n/a)</td><td>105838.30 (n/a)</td><td>212.63 (n/a)</td><td>649.29 (n/a)</td><td>648.47 (n/a)</td><td>648.98 (n/a)</td><td>646.16 (n/a)</td><td>1.30 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.58 (-7.05%)</td><td>3.30 (+0.06%)</td><td>3.34 (+6.55%)</td><td>2.97 (+0.07%)</td><td>0.28 <b>(-28.10%)</b></td><td>2714.30 (-0.07%)</td><td>2458.08 (-0.54%)</td><td>2412.40 (-6.15%)</td><td>2254.80 (+7.59%)</td><td>211.67 <b>(-23.84%)</b></td><td>937.53 (-7.05%)</td><td>865.05 (+0.06%)</td><td>876.29 (+6.55%)</td><td>778.81 (+0.07%)</td><td>73.40 <b>(-28.10%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>3.85 (n/a)</td><td>3.30 (n/a)</td><td>3.14 (n/a)</td><td>2.97 (n/a)</td><td>0.39 (n/a)</td><td>2716.10 (n/a)</td><td>2471.42 (n/a)</td><td>2570.40 (n/a)</td><td>2095.80 (n/a)</td><td>277.92 (n/a)</td><td>1008.63 (n/a)</td><td>864.51 (n/a)</td><td>822.41 (n/a)</td><td>778.28 (n/a)</td><td>102.09 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.54 (+8.02%)</td><td>0.42 (+5.04%)</td><td>0.39 (+5.88%)</td><td>0.33 (+10.51%)</td><td>0.10 (+12.36%)</td><td>3781.90 (-9.51%)</td><td>3110.64 (-4.43%)</td><td>3202.40 (-5.55%)</td><td>2319.20 (-7.42%)</td><td>681.08 (-1.81%)</td><td>28.94 (+8.02%)</td><td>22.47 (+5.04%)</td><td>20.96 (+5.88%)</td><td>17.74 (+10.51%)</td><td>5.14 (+12.36%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.50 (n/a)</td><td>0.40 (n/a)</td><td>0.37 (n/a)</td><td>0.30 (n/a)</td><td>0.08 (n/a)</td><td>4179.50 (n/a)</td><td>3254.68 (n/a)</td><td>3390.70 (n/a)</td><td>2505.10 (n/a)</td><td>693.60 (n/a)</td><td>26.79 (n/a)</td><td>21.39 (n/a)</td><td>19.79 (n/a)</td><td>16.06 (n/a)</td><td>4.58 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>4.87 (-4.61%)</td><td>4.38 (-1.52%)</td><td>4.76 (-0.58%)</td><td>3.40 (-4.06%)</td><td>0.65 (-6.97%)</td><td>1954.20 (+4.23%)</td><td>1548.68 (+1.40%)</td><td>1398.40 (+0.58%)</td><td>1364.60 (+4.83%)</td><td>256.74 (+0.32%)</td><td>1506.06 (-4.61%)</td><td>1353.60 (-1.52%)</td><td>1469.67 (-0.58%)</td><td>1051.70 (-4.06%)</td><td>200.87 (-6.97%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>5.11 (n/a)</td><td>4.45 (n/a)</td><td>4.78 (n/a)</td><td>3.55 (n/a)</td><td>0.70 (n/a)</td><td>1874.90 (n/a)</td><td>1527.30 (n/a)</td><td>1390.30 (n/a)</td><td>1301.70 (n/a)</td><td>255.91 (n/a)</td><td>1578.92 (n/a)</td><td>1374.52 (n/a)</td><td>1478.21 (n/a)</td><td>1096.15 (n/a)</td><td>215.91 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>13.17 (n/a)</td><td>12.24 (n/a)</td><td>12.59 (n/a)</td><td>10.44 (n/a)</td><td>1.14 (n/a)</td><td>13.17 (n/a)</td><td>12.23 (n/a)</td><td>12.58 (n/a)</td><td>10.44 (n/a)</td><td>1.14 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>24.68 (+0.93%)</td><td>24.15 (+4.63%)</td><td>24.10 (+0.98%)</td><td>23.63 (+18.87%)</td><td>0.42 <b>(-77.68%)</b></td><td>24.67 (+0.93%)</td><td>24.13 (+4.63%)</td><td>24.09 (+0.98%)</td><td>23.62 (+18.87%)</td><td>0.42 <b>(-77.68%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>24.46 (n/a)</td><td>23.08 (n/a)</td><td>23.87 (n/a)</td><td>19.88 (n/a)</td><td>1.88 (n/a)</td><td>24.44 (n/a)</td><td>23.07 (n/a)</td><td>23.86 (n/a)</td><td>19.87 (n/a)</td><td>1.88 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>42.21 (-1.18%)</td><td>40.64 (-0.16%)</td><td>40.38 (-1.04%)</td><td>39.50 (+2.41%)</td><td>1.00 <b>(-38.30%)</b></td><td>42.18 (-1.18%)</td><td>40.62 (-0.16%)</td><td>40.35 (-1.04%)</td><td>39.48 (+2.41%)</td><td>1.00 <b>(-38.30%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>42.71 (n/a)</td><td>40.71 (n/a)</td><td>40.80 (n/a)</td><td>38.57 (n/a)</td><td>1.63 (n/a)</td><td>42.69 (n/a)</td><td>40.68 (n/a)</td><td>40.78 (n/a)</td><td>38.55 (n/a)</td><td>1.63 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>44.61 (-0.24%)</td><td>43.24 (+0.00%)</td><td>43.19 (+1.35%)</td><td>41.58 (-1.87%)</td><td>1.28 <b>(+20.11%)</b></td><td>44.58 (-0.24%)</td><td>43.21 (+0.00%)</td><td>43.16 (+1.35%)</td><td>41.55 (-1.87%)</td><td>1.28 <b>(+20.11%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>44.72 (n/a)</td><td>43.24 (n/a)</td><td>42.61 (n/a)</td><td>42.37 (n/a)</td><td>1.07 (n/a)</td><td>44.69 (n/a)</td><td>43.21 (n/a)</td><td>42.59 (n/a)</td><td>42.34 (n/a)</td><td>1.07 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>13.50 (n/a)</td><td>12.23 (n/a)</td><td>13.02 (n/a)</td><td>10.34 (n/a)</td><td>1.44 (n/a)</td><td>13.49 (n/a)</td><td>12.22 (n/a)</td><td>13.01 (n/a)</td><td>10.34 (n/a)</td><td>1.44 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>24.94 (+0.73%)</td><td>24.50 (+0.83%)</td><td>24.41 (+1.00%)</td><td>24.17 (+0.44%)</td><td>0.32 (+10.19%)</td><td>24.93 (+0.73%)</td><td>24.49 (+0.83%)</td><td>24.39 (+1.00%)</td><td>24.15 (+0.44%)</td><td>0.32 (+10.19%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>24.76 (n/a)</td><td>24.30 (n/a)</td><td>24.16 (n/a)</td><td>24.06 (n/a)</td><td>0.29 (n/a)</td><td>24.75 (n/a)</td><td>24.28 (n/a)</td><td>24.15 (n/a)</td><td>24.05 (n/a)</td><td>0.29 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>45.65 (+15.20%)</td><td>41.79 (+11.20%)</td><td>41.25 (+7.05%)</td><td>39.02 <b>(+20.36%)</b></td><td>2.41 (-18.16%)</td><td>45.62 (+15.20%)</td><td>41.76 (+11.20%)</td><td>41.22 (+7.05%)</td><td>38.99 <b>(+20.36%)</b></td><td>2.41 (-18.16%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>39.63 (n/a)</td><td>37.58 (n/a)</td><td>38.53 (n/a)</td><td>32.42 (n/a)</td><td>2.94 (n/a)</td><td>39.60 (n/a)</td><td>37.56 (n/a)</td><td>38.51 (n/a)</td><td>32.40 (n/a)</td><td>2.94 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>42.46 (-2.77%)</td><td>42.02 (-1.25%)</td><td>41.95 (-1.35%)</td><td>41.43 (+1.00%)</td><td>0.43 <b>(-59.38%)</b></td><td>42.43 (-2.77%)</td><td>41.99 (-1.25%)</td><td>41.93 (-1.35%)</td><td>41.40 (+1.00%)</td><td>0.43 <b>(-59.38%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>43.67 (n/a)</td><td>42.55 (n/a)</td><td>42.53 (n/a)</td><td>41.02 (n/a)</td><td>1.05 (n/a)</td><td>43.64 (n/a)</td><td>42.52 (n/a)</td><td>42.50 (n/a)</td><td>40.99 (n/a)</td><td>1.05 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>9.37 (+0.42%)</td><td>8.83 (-2.77%)</td><td>8.79 (-2.96%)</td><td>8.30 (-5.54%)</td><td>0.39 <b>(+72.73%)</b></td><td>9.35 (+0.42%)</td><td>8.81 (-2.77%)</td><td>8.78 (-2.96%)</td><td>8.28 (-5.54%)</td><td>0.39 <b>(+72.73%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>9.33 (n/a)</td><td>9.08 (n/a)</td><td>9.06 (n/a)</td><td>8.78 (n/a)</td><td>0.23 (n/a)</td><td>9.31 (n/a)</td><td>9.06 (n/a)</td><td>9.04 (n/a)</td><td>8.76 (n/a)</td><td>0.23 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.05 (+18.18%)</td><td>0.93 (+9.53%)</td><td>0.96 (+13.77%)</td><td>0.74 (-8.45%)</td><td>0.13 <b>(+331.29%)</b></td><td>1.04 (+18.18%)</td><td>0.92 (+9.53%)</td><td>0.94 (+13.77%)</td><td>0.73 (-8.45%)</td><td>0.13 <b>(+331.29%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.89 (n/a)</td><td>0.85 (n/a)</td><td>0.84 (n/a)</td><td>0.81 (n/a)</td><td>0.03 (n/a)</td><td>0.88 (n/a)</td><td>0.84 (n/a)</td><td>0.83 (n/a)</td><td>0.80 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.35 (-2.63%)</td><td>1.26 (+1.18%)</td><td>1.24 (-5.83%)</td><td>1.19 <b>(+31.24%)</b></td><td>0.06 <b>(-70.84%)</b></td><td>1.33 (-2.63%)</td><td>1.24 (+1.18%)</td><td>1.23 (-5.83%)</td><td>1.18 <b>(+31.24%)</b></td><td>0.06 <b>(-70.84%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.39 (n/a)</td><td>1.24 (n/a)</td><td>1.32 (n/a)</td><td>0.91 (n/a)</td><td>0.20 (n/a)</td><td>1.37 (n/a)</td><td>1.23 (n/a)</td><td>1.31 (n/a)</td><td>0.90 (n/a)</td><td>0.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>17.94 (+3.60%)</td><td>17.31 (+3.70%)</td><td>17.39 (+4.43%)</td><td>16.34 (+1.68%)</td><td>0.63 <b>(+22.03%)</b></td><td>17.73 (+3.60%)</td><td>17.11 (+3.70%)</td><td>17.19 (+4.43%)</td><td>16.15 (+1.68%)</td><td>0.62 <b>(+22.03%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>17.32 (n/a)</td><td>16.69 (n/a)</td><td>16.65 (n/a)</td><td>16.07 (n/a)</td><td>0.52 (n/a)</td><td>17.12 (n/a)</td><td>16.50 (n/a)</td><td>16.46 (n/a)</td><td>15.88 (n/a)</td><td>0.51 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>14.30 (+4.21%)</td><td>13.66 (+1.14%)</td><td>13.58 (+0.61%)</td><td>13.20 (-0.49%)</td><td>0.40 <b>(+107.17%)</b></td><td>14.05 (+4.21%)</td><td>13.42 (+1.14%)</td><td>13.34 (+0.61%)</td><td>12.96 (-0.49%)</td><td>0.40 <b>(+107.18%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>13.72 (n/a)</td><td>13.50 (n/a)</td><td>13.50 (n/a)</td><td>13.26 (n/a)</td><td>0.19 (n/a)</td><td>13.48 (n/a)</td><td>13.27 (n/a)</td><td>13.26 (n/a)</td><td>13.03 (n/a)</td><td>0.19 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>9.05 (+3.54%)</td><td>8.10 (+3.39%)</td><td>7.89 (+2.38%)</td><td>7.16 (-0.29%)</td><td>0.81 <b>(+42.47%)</b></td><td>8.89 (+3.54%)</td><td>7.96 (+3.39%)</td><td>7.75 (+2.38%)</td><td>7.04 (-0.29%)</td><td>0.80 <b>(+42.47%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.74 (n/a)</td><td>7.83 (n/a)</td><td>7.70 (n/a)</td><td>7.18 (n/a)</td><td>0.57 (n/a)</td><td>8.59 (n/a)</td><td>7.70 (n/a)</td><td>7.57 (n/a)</td><td>7.06 (n/a)</td><td>0.56 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>6.54 (-4.84%)</td><td>5.92 (+4.54%)</td><td>5.93 (+2.16%)</td><td>5.01 (+11.84%)</td><td>0.60 <b>(-31.41%)</b></td><td>6.44 (-4.84%)</td><td>5.83 (+4.54%)</td><td>5.84 (+2.16%)</td><td>4.93 (+11.84%)</td><td>0.59 <b>(-31.41%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>6.88 (n/a)</td><td>5.67 (n/a)</td><td>5.80 (n/a)</td><td>4.48 (n/a)</td><td>0.88 (n/a)</td><td>6.77 (n/a)</td><td>5.58 (n/a)</td><td>5.71 (n/a)</td><td>4.41 (n/a)</td><td>0.87 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>13.42 (n/a)</td><td>12.59 (n/a)</td><td>12.17 (n/a)</td><td>11.94 (n/a)</td><td>0.70 (n/a)</td><td>13.41 (n/a)</td><td>12.58 (n/a)</td><td>12.16 (n/a)</td><td>11.93 (n/a)</td><td>0.70 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>13.06 (n/a)</td><td>12.28 (n/a)</td><td>12.45 (n/a)</td><td>10.74 (n/a)</td><td>0.95 (n/a)</td><td>13.05 (n/a)</td><td>12.27 (n/a)</td><td>12.44 (n/a)</td><td>10.73 (n/a)</td><td>0.95 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.20 (n/a)</td><td>176.20 (n/a)</td><td>187.50 (n/a)</td><td>118.70 (n/a)</td><td>44.23 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>190.40 (n/a)</td><td>149.34 (n/a)</td><td>150.80 (n/a)</td><td>114.90 (n/a)</td><td>32.31 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>239.40 (n/a)</td><td>175.64 (n/a)</td><td>163.70 (n/a)</td><td>136.80 (n/a)</td><td>43.96 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>242.30 (n/a)</td><td>184.04 (n/a)</td><td>182.50 (n/a)</td><td>149.40 (n/a)</td><td>37.66 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>256.10 (n/a)</td><td>172.00 (n/a)</td><td>153.90 (n/a)</td><td>130.70 (n/a)</td><td>49.05 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>222.80 (n/a)</td><td>162.58 (n/a)</td><td>155.80 (n/a)</td><td>119.70 (n/a)</td><td>41.40 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>248.20 (n/a)</td><td>165.88 (n/a)</td><td>142.50 (n/a)</td><td>134.00 (n/a)</td><td>47.60 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>223.40 (n/a)</td><td>192.72 (n/a)</td><td>197.00 (n/a)</td><td>145.90 (n/a)</td><td>29.49 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>186.00 (n/a)</td><td>145.42 (n/a)</td><td>137.70 (n/a)</td><td>126.50 (n/a)</td><td>23.28 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>209.40 (n/a)</td><td>169.14 (n/a)</td><td>161.10 (n/a)</td><td>135.80 (n/a)</td><td>29.63 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>191.90 (n/a)</td><td>172.44 (n/a)</td><td>169.80 (n/a)</td><td>156.40 (n/a)</td><td>14.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.09 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>415.80 (n/a)</td><td>206.12 (n/a)</td><td>184.60 (n/a)</td><td>91.90 (n/a)</td><td>124.80 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>217.30 (n/a)</td><td>150.78 (n/a)</td><td>153.10 (n/a)</td><td>101.10 (n/a)</td><td>44.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.30 (n/a)</td><td>189.16 (n/a)</td><td>171.80 (n/a)</td><td>161.80 (n/a)</td><td>30.52 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>220.40 (n/a)</td><td>187.10 (n/a)</td><td>211.70 (n/a)</td><td>111.10 (n/a)</td><td>46.58 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>227.30 (n/a)</td><td>196.26 (n/a)</td><td>207.70 (n/a)</td><td>141.10 (n/a)</td><td>32.94 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>212.40 (n/a)</td><td>171.34 (n/a)</td><td>164.10 (n/a)</td><td>143.00 (n/a)</td><td>28.50 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>186.00 (n/a)</td><td>165.44 (n/a)</td><td>176.50 (n/a)</td><td>128.00 (n/a)</td><td>23.92 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>202.80 (n/a)</td><td>166.84 (n/a)</td><td>173.40 (n/a)</td><td>117.20 (n/a)</td><td>31.21 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>202.70 (n/a)</td><td>156.54 (n/a)</td><td>142.70 (n/a)</td><td>121.70 (n/a)</td><td>38.65 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.50 (n/a)</td><td>169.96 (n/a)</td><td>164.40 (n/a)</td><td>144.20 (n/a)</td><td>25.74 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>300.30 (n/a)</td><td>198.90 (n/a)</td><td>165.80 (n/a)</td><td>137.50 (n/a)</td><td>65.48 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>265.70 (n/a)</td><td>176.94 (n/a)</td><td>169.40 (n/a)</td><td>112.80 (n/a)</td><td>55.44 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>307.20 (n/a)</td><td>221.74 (n/a)</td><td>217.30 (n/a)</td><td>174.90 (n/a)</td><td>51.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>194.00 (n/a)</td><td>172.26 (n/a)</td><td>185.00 (n/a)</td><td>133.30 (n/a)</td><td>24.52 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.02 (n/a)</td><td>194.10 (n/a)</td><td>165.34 (n/a)</td><td>158.50 (n/a)</td><td>152.50 (n/a)</td><td>17.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.04 (n/a)</td><td>211.80 (n/a)</td><td>176.24 (n/a)</td><td>177.00 (n/a)</td><td>132.70 (n/a)</td><td>33.06 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>213.80 (n/a)</td><td>195.76 (n/a)</td><td>203.80 (n/a)</td><td>159.60 (n/a)</td><td>22.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>204.50 (n/a)</td><td>178.34 (n/a)</td><td>172.40 (n/a)</td><td>165.80 (n/a)</td><td>15.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.21 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.04 (n/a)</td><td>284.70 (n/a)</td><td>203.30 (n/a)</td><td>188.90 (n/a)</td><td>155.70 (n/a)</td><td>49.11 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>307.60 (n/a)</td><td>229.36 (n/a)</td><td>222.50 (n/a)</td><td>176.50 (n/a)</td><td>48.69 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>262.80 (n/a)</td><td>238.50 (n/a)</td><td>245.10 (n/a)</td><td>207.00 (n/a)</td><td>20.96 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (-2.93%)</td><td>0.03 (+1.42%)</td><td>0.03 (+6.14%)</td><td>0.02 (-2.63%)</td><td>0.00 (-2.97%)</td><td>183.30 (+2.69%)</td><td>163.10 (-1.39%)</td><td>163.80 (-5.75%)</td><td>138.20 (+2.98%)</td><td>19.40 (+4.32%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>178.50 (n/a)</td><td>165.40 (n/a)</td><td>173.80 (n/a)</td><td>134.20 (n/a)</td><td>18.59 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 <b>(+24.84%)</b></td><td>0.03 (+2.87%)</td><td>0.03 (+1.75%)</td><td>0.02 (-12.52%)</td><td>0.01 <b>(+132.46%)</b></td><td>202.80 (+14.32%)</td><td>160.26 (+1.10%)</td><td>163.30 (-1.69%)</td><td>106.30 (-19.89%)</td><td>36.98 <b>(+110.38%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.40 (n/a)</td><td>158.52 (n/a)</td><td>166.10 (n/a)</td><td>132.70 (n/a)</td><td>17.58 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (+1.48%)</td><td>0.03 (-9.91%)</td><td>0.02 <b>(-20.44%)</b></td><td>0.02 <b>(-25.40%)</b></td><td>0.01 <b>(+121.90%)</b></td><td>211.60 <b>(+34.09%)</b></td><td>161.14 (+17.60%)</td><td>172.60 <b>(+25.71%)</b></td><td>113.00 (-1.40%)</td><td>45.24 <b>(+181.83%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>157.80 (n/a)</td><td>137.02 (n/a)</td><td>137.30 (n/a)</td><td>114.60 (n/a)</td><td>16.05 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 <b>(-21.54%)</b></td><td>0.02 (-12.03%)</td><td>0.02 <b>(-20.72%)</b></td><td>0.02 <b>(+24.72%)</b></td><td>0.00 <b>(-61.20%)</b></td><td>232.30 (-19.81%)</td><td>187.04 (+5.27%)</td><td>185.00 <b>(+26.11%)</b></td><td>162.00 <b>(+27.46%)</b></td><td>27.18 <b>(-59.72%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>289.70 (n/a)</td><td>177.68 (n/a)</td><td>146.70 (n/a)</td><td>127.10 (n/a)</td><td>67.49 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 <b>(-25.99%)</b></td><td>0.02 (-14.99%)</td><td>0.03 (-18.66%)</td><td>0.02 (+9.67%)</td><td>0.00 <b>(-71.77%)</b></td><td>182.40 (-8.80%)</td><td>165.42 (+13.35%)</td><td>162.30 <b>(+22.95%)</b></td><td>152.00 <b>(+35.11%)</b></td><td>12.03 <b>(-65.54%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>200.00 (n/a)</td><td>145.94 (n/a)</td><td>132.00 (n/a)</td><td>112.50 (n/a)</td><td>34.92 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (-18.13%)</td><td>0.02 (-10.76%)</td><td>0.02 (-0.25%)</td><td>0.02 (-8.36%)</td><td>0.00 <b>(-32.66%)</b></td><td>211.60 (+9.13%)</td><td>178.14 (+11.10%)</td><td>164.90 (+0.24%)</td><td>158.60 <b>(+22.09%)</b></td><td>23.85 (-9.79%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>193.90 (n/a)</td><td>160.34 (n/a)</td><td>164.50 (n/a)</td><td>129.90 (n/a)</td><td>26.44 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 <b>(-24.19%)</b></td><td>0.02 <b>(-27.08%)</b></td><td>0.02 <b>(-25.18%)</b></td><td>0.01 <b>(-42.78%)</b></td><td>0.00 (+10.28%)</td><td>299.10 <b>(+74.81%)</b></td><td>215.42 <b>(+41.37%)</b></td><td>220.00 <b>(+33.66%)</b></td><td>160.00 <b>(+31.90%)</b></td><td>54.76 <b>(+148.86%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>171.10 (n/a)</td><td>152.38 (n/a)</td><td>164.60 (n/a)</td><td>121.30 (n/a)</td><td>22.01 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 <b>(+23.64%)</b></td><td>0.02 (-7.54%)</td><td>0.02 (-15.64%)</td><td>0.02 <b>(-21.55%)</b></td><td>0.01 <b>(+198.07%)</b></td><td>269.20 <b>(+27.46%)</b></td><td>215.36 (+12.51%)</td><td>215.90 (+18.50%)</td><td>142.80 (-19.09%)</td><td>46.19 <b>(+191.27%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>211.20 (n/a)</td><td>191.42 (n/a)</td><td>182.20 (n/a)</td><td>176.50 (n/a)</td><td>15.86 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (-10.05%)</td><td>0.04 (-12.78%)</td><td>0.04 (-15.27%)</td><td>0.04 (-12.52%)</td><td>0.01 (-4.42%)</td><td>219.20 (+14.35%)</td><td>192.12 (+14.97%)</td><td>192.90 (+18.05%)</td><td>145.80 (+11.21%)</td><td>28.76 (+19.42%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.70 (n/a)</td><td>167.10 (n/a)</td><td>163.40 (n/a)</td><td>131.10 (n/a)</td><td>24.08 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (-5.27%)</td><td>0.05 (-7.74%)</td><td>0.05 (-4.10%)</td><td>0.04 (-6.12%)</td><td>0.01 (-3.26%)</td><td>194.20 (+6.53%)</td><td>162.60 (+8.60%)</td><td>163.30 (+4.28%)</td><td>123.30 (+5.57%)</td><td>29.19 (+11.10%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>182.30 (n/a)</td><td>149.72 (n/a)</td><td>156.60 (n/a)</td><td>116.80 (n/a)</td><td>26.28 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 <b>(-33.67%)</b></td><td>0.05 (-19.61%)</td><td>0.05 (-8.20%)</td><td>0.04 (-10.43%)</td><td>0.01 <b>(-59.08%)</b></td><td>213.60 (+11.66%)</td><td>181.68 <b>(+21.15%)</b></td><td>168.60 (+8.91%)</td><td>164.10 <b>(+50.69%)</b></td><td>21.76 <b>(-30.74%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.30 (n/a)</td><td>149.96 (n/a)</td><td>154.80 (n/a)</td><td>108.90 (n/a)</td><td>31.42 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (+3.40%)</td><td>0.05 (-17.00%)</td><td>0.04 <b>(-26.46%)</b></td><td>0.04 <b>(-25.23%)</b></td><td>0.01 <b>(+121.12%)</b></td><td>232.40 <b>(+33.72%)</b></td><td>185.12 <b>(+25.32%)</b></td><td>197.40 <b>(+36.04%)</b></td><td>130.40 (-3.26%)</td><td>42.80 <b>(+179.31%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>173.80 (n/a)</td><td>147.72 (n/a)</td><td>145.10 (n/a)</td><td>134.80 (n/a)</td><td>15.32 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (-17.45%)</td><td>0.05 <b>(-21.04%)</b></td><td>0.05 <b>(-23.57%)</b></td><td>0.04 (-15.72%)</td><td>0.01 (-16.95%)</td><td>205.00 (+18.63%)</td><td>180.82 <b>(+26.61%)</b></td><td>181.50 <b>(+30.86%)</b></td><td>155.30 <b>(+21.14%)</b></td><td>20.16 (+16.24%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>172.80 (n/a)</td><td>142.82 (n/a)</td><td>138.70 (n/a)</td><td>128.20 (n/a)</td><td>17.34 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 <b>(-23.14%)</b></td><td>0.04 (-17.57%)</td><td>0.04 (-12.63%)</td><td>0.04 (-16.85%)</td><td>0.00 <b>(-45.20%)</b></td><td>211.30 <b>(+20.26%)</b></td><td>184.50 <b>(+20.24%)</b></td><td>188.00 (+14.42%)</td><td>165.80 <b>(+30.04%)</b></td><td>18.38 (-14.15%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>175.70 (n/a)</td><td>153.44 (n/a)</td><td>164.30 (n/a)</td><td>127.50 (n/a)</td><td>21.41 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (-16.73%)</td><td>0.04 (-16.41%)</td><td>0.05 (-12.04%)</td><td>0.03 <b>(-34.86%)</b></td><td>0.01 <b>(+43.05%)</b></td><td>272.60 <b>(+53.49%)</b></td><td>193.84 <b>(+22.67%)</b></td><td>175.10 (+13.70%)</td><td>164.00 <b>(+20.15%)</b></td><td>44.60 <b>(+171.39%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>177.60 (n/a)</td><td>158.02 (n/a)</td><td>154.00 (n/a)</td><td>136.50 (n/a)</td><td>16.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (-10.61%)</td><td>0.04 (-11.39%)</td><td>0.04 (-13.02%)</td><td>0.04 (-8.68%)</td><td>0.01 <b>(-28.07%)</b></td><td>208.00 (+9.53%)</td><td>185.04 (+12.06%)</td><td>197.30 (+14.98%)</td><td>154.60 (+11.87%)</td><td>22.71 (-10.69%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>189.90 (n/a)</td><td>165.12 (n/a)</td><td>171.60 (n/a)</td><td>138.20 (n/a)</td><td>25.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (-4.46%)</td><td>0.04 (-9.53%)</td><td>0.05 (-2.46%)</td><td>0.04 (-19.36%)</td><td>0.01 <b>(+118.27%)</b></td><td>219.70 <b>(+23.98%)</b></td><td>187.32 (+11.79%)</td><td>174.20 (+2.53%)</td><td>162.10 (+4.65%)</td><td>24.86 <b>(+187.39%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.00 (n/a)</td><td>177.20 (n/a)</td><td>167.56 (n/a)</td><td>169.90 (n/a)</td><td>154.90 (n/a)</td><td>8.65 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (+2.35%)</td><td>0.04 (+8.55%)</td><td>0.04 (+7.59%)</td><td>0.04 <b>(+25.38%)</b></td><td>0.00 <b>(-31.54%)</b></td><td>231.00 <b>(-20.23%)</b></td><td>206.72 (-8.93%)</td><td>198.10 (-7.04%)</td><td>190.70 (-2.31%)</td><td>18.76 <b>(-48.63%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>289.60 (n/a)</td><td>227.00 (n/a)</td><td>213.10 (n/a)</td><td>195.20 (n/a)</td><td>36.51 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 <b>(+31.76%)</b></td><td>0.11 <b>(+26.71%)</b></td><td>0.11 <b>(+24.20%)</b></td><td>0.09 (+16.52%)</td><td>0.02 <b>(+74.68%)</b></td><td>183.70 (-14.16%)</td><td>149.60 <b>(-20.39%)</b></td><td>144.50 (-19.50%)</td><td>128.70 <b>(-24.12%)</b></td><td>23.07 (+12.75%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.00 (n/a)</td><td>187.92 (n/a)</td><td>179.50 (n/a)</td><td>169.60 (n/a)</td><td>20.46 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (+9.95%)</td><td>0.10 (+1.02%)</td><td>0.09 (-13.83%)</td><td>0.08 (+14.05%)</td><td>0.03 <b>(+31.03%)</b></td><td>196.50 (-12.32%)</td><td>163.88 (+0.23%)</td><td>185.70 (+16.06%)</td><td>117.60 (-9.05%)</td><td>37.75 (+2.99%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>224.10 (n/a)</td><td>163.50 (n/a)</td><td>160.00 (n/a)</td><td>129.30 (n/a)</td><td>36.65 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (-14.68%)</td><td>0.09 (-9.25%)</td><td>0.08 (-8.78%)</td><td>0.07 (-16.47%)</td><td>0.02 (-17.06%)</td><td>248.10 (+19.74%)</td><td>194.82 (+10.15%)</td><td>197.60 (+9.60%)</td><td>143.90 (+17.28%)</td><td>38.75 (+19.90%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>207.20 (n/a)</td><td>176.86 (n/a)</td><td>180.30 (n/a)</td><td>122.70 (n/a)</td><td>32.32 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (+3.96%)</td><td>0.09 (+4.60%)</td><td>0.09 (-7.17%)</td><td>0.07 (+3.26%)</td><td>0.02 <b>(+25.60%)</b></td><td>247.30 (-3.13%)</td><td>182.42 (-2.98%)</td><td>186.90 (+7.72%)</td><td>135.50 (-3.83%)</td><td>47.49 (+9.20%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>255.30 (n/a)</td><td>188.02 (n/a)</td><td>173.50 (n/a)</td><td>140.90 (n/a)</td><td>43.49 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (-8.91%)</td><td>0.10 (-2.36%)</td><td>0.10 (+8.83%)</td><td>0.08 (-8.19%)</td><td>0.01 (+5.30%)</td><td>212.30 (+8.93%)</td><td>174.74 (+2.97%)</td><td>158.00 (-8.09%)</td><td>149.30 (+9.78%)</td><td>28.22 <b>(+28.74%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>194.90 (n/a)</td><td>169.70 (n/a)</td><td>171.90 (n/a)</td><td>136.00 (n/a)</td><td>21.92 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (+18.14%)</td><td>0.10 (+13.33%)</td><td>0.10 <b>(+22.06%)</b></td><td>0.08 (+8.75%)</td><td>0.02 <b>(+47.34%)</b></td><td>211.10 (-8.06%)</td><td>169.70 (-10.68%)</td><td>158.20 (-18.07%)</td><td>137.70 (-15.37%)</td><td>32.88 (+18.18%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>229.60 (n/a)</td><td>190.00 (n/a)</td><td>193.10 (n/a)</td><td>162.70 (n/a)</td><td>27.82 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 <b>(+21.89%)</b></td><td>0.10 (+0.37%)</td><td>0.09 (-2.35%)</td><td>0.08 (-11.15%)</td><td>0.04 <b>(+74.99%)</b></td><td>213.60 (+12.54%)</td><td>176.56 (+4.33%)</td><td>191.70 (+2.40%)</td><td>100.30 (-17.92%)</td><td>44.86 <b>(+52.48%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>189.80 (n/a)</td><td>169.24 (n/a)</td><td>187.20 (n/a)</td><td>122.20 (n/a)</td><td>29.42 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (-16.53%)</td><td>0.07 (-19.17%)</td><td>0.08 (-13.11%)</td><td>0.05 <b>(-33.42%)</b></td><td>0.01 <b>(+53.91%)</b></td><td>321.60 <b>(+50.14%)</b></td><td>240.60 <b>(+27.15%)</b></td><td>210.30 (+15.04%)</td><td>199.70 (+19.80%)</td><td>54.13 <b>(+167.64%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>214.20 (n/a)</td><td>189.22 (n/a)</td><td>182.80 (n/a)</td><td>166.70 (n/a)</td><td>20.23 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.23 (-14.71%)</td><td>0.18 (-13.47%)</td><td>0.17 (-11.64%)</td><td>0.14 <b>(-20.55%)</b></td><td>0.04 (+0.15%)</td><td>230.60 <b>(+25.87%)</b></td><td>183.90 (+16.78%)</td><td>190.90 (+13.23%)</td><td>145.00 (+17.31%)</td><td>37.83 <b>(+41.44%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.27 (n/a)</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.04 (n/a)</td><td>183.20 (n/a)</td><td>157.48 (n/a)</td><td>168.60 (n/a)</td><td>123.60 (n/a)</td><td>26.75 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (-8.96%)</td><td>0.21 (-5.33%)</td><td>0.22 (-12.75%)</td><td>0.15 (-4.12%)</td><td>0.04 <b>(-28.31%)</b></td><td>211.50 (+4.29%)</td><td>159.16 (+3.39%)</td><td>150.00 (+14.59%)</td><td>127.80 (+9.79%)</td><td>32.57 (-18.61%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>202.80 (n/a)</td><td>153.94 (n/a)</td><td>130.90 (n/a)</td><td>116.40 (n/a)</td><td>40.02 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 (+15.33%)</td><td>0.20 (-10.46%)</td><td>0.20 (-10.96%)</td><td>0.16 <b>(-21.20%)</b></td><td>0.05 <b>(+207.63%)</b></td><td>211.20 <b>(+26.92%)</b></td><td>171.62 (+16.07%)</td><td>164.00 (+12.33%)</td><td>118.20 (-13.28%)</td><td>37.34 <b>(+235.23%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.02 (n/a)</td><td>166.40 (n/a)</td><td>147.86 (n/a)</td><td>146.00 (n/a)</td><td>136.30 (n/a)</td><td>11.14 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.21 (+0.49%)</td><td>0.19 (-4.65%)</td><td>0.20 (+2.09%)</td><td>0.14 <b>(-25.89%)</b></td><td>0.03 <b>(+200.87%)</b></td><td>235.60 <b>(+34.94%)</b></td><td>175.04 (+7.29%)</td><td>161.30 (-2.06%)</td><td>154.20 (-0.52%)</td><td>34.22 <b>(+316.38%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.01 (n/a)</td><td>174.60 (n/a)</td><td>163.14 (n/a)</td><td>164.70 (n/a)</td><td>155.00 (n/a)</td><td>8.22 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (+14.27%)</td><td>0.20 (+0.35%)</td><td>0.21 (+6.70%)</td><td>0.16 (-15.01%)</td><td>0.04 <b>(+157.59%)</b></td><td>210.60 (+17.65%)</td><td>167.44 (+2.60%)</td><td>153.50 (-6.29%)</td><td>126.60 (-12.51%)</td><td>34.55 <b>(+172.79%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.02 (n/a)</td><td>179.00 (n/a)</td><td>163.20 (n/a)</td><td>163.80 (n/a)</td><td>144.70 (n/a)</td><td>12.66 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (+6.86%)</td><td>0.20 (-6.17%)</td><td>0.19 (-12.58%)</td><td>0.15 (-6.28%)</td><td>0.04 <b>(+32.97%)</b></td><td>223.50 (+6.68%)</td><td>173.90 (+8.04%)</td><td>176.00 (+14.36%)</td><td>128.20 (-6.42%)</td><td>35.58 <b>(+26.74%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 (n/a)</td><td>0.21 (n/a)</td><td>0.21 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>209.50 (n/a)</td><td>160.96 (n/a)</td><td>153.90 (n/a)</td><td>137.00 (n/a)</td><td>28.07 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (-17.21%)</td><td>0.16 (-4.53%)</td><td>0.16 (-9.47%)</td><td>0.14 <b>(+45.52%)</b></td><td>0.01 <b>(-76.26%)</b></td><td>233.20 <b>(-31.27%)</b></td><td>208.94 (-1.82%)</td><td>204.90 (+10.46%)</td><td>199.50 <b>(+20.76%)</b></td><td>13.78 <b>(-80.86%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.18 (n/a)</td><td>0.10 (n/a)</td><td>0.04 (n/a)</td><td>339.30 (n/a)</td><td>212.82 (n/a)</td><td>185.50 (n/a)</td><td>165.20 (n/a)</td><td>72.00 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (-13.19%)</td><td>0.03 (-0.06%)</td><td>0.03 (+3.53%)</td><td>0.02 (+2.29%)</td><td>0.00 <b>(-37.21%)</b></td><td>222.30 (-2.24%)</td><td>165.34 (-3.13%)</td><td>159.60 (-3.45%)</td><td>134.80 (+15.21%)</td><td>33.52 <b>(-27.31%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>227.40 (n/a)</td><td>170.68 (n/a)</td><td>165.30 (n/a)</td><td>117.00 (n/a)</td><td>46.11 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (-19.38%)</td><td>0.03 (-9.34%)</td><td>0.03 (-13.07%)</td><td>0.02 (+7.40%)</td><td>0.00 <b>(-51.59%)</b></td><td>194.50 (-6.89%)</td><td>161.52 (+5.28%)</td><td>162.80 (+15.05%)</td><td>133.00 <b>(+24.07%)</b></td><td>23.97 <b>(-45.16%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>208.90 (n/a)</td><td>153.42 (n/a)</td><td>141.50 (n/a)</td><td>107.20 (n/a)</td><td>43.70 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.00 (-0.01%)</td><td>0.00 (-0.01%)</td><td>0.00 (-0.01%)</td><td>0.00 (-0.01%)</td><td>0.00 <b>(-45.81%)</b></td><td>4746206.10 (+0.01%)</td><td>4746104.65 (+0.01%)</td><td>4746104.65 (+0.01%)</td><td>4746003.20 (+0.01%)</td><td>143.47 <b>(-45.84%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>4745965.30 (n/a)</td><td>4745778.00 (n/a)</td><td>4745778.00 (n/a)</td><td>4745590.70 (n/a)</td><td>264.88 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (+10.28%)</td><td>0.02 (+12.42%)</td><td>0.02 (+11.73%)</td><td>0.02 (+10.80%)</td><td>0.00 <b>(+20.39%)</b></td><td>204.60 (-9.75%)</td><td>187.06 (-10.96%)</td><td>187.40 (-10.51%)</td><td>167.80 (-9.30%)</td><td>17.05 (-1.94%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>226.70 (n/a)</td><td>210.08 (n/a)</td><td>209.40 (n/a)</td><td>185.00 (n/a)</td><td>17.39 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (-6.44%)</td><td>0.02 (+3.18%)</td><td>0.02 (+12.93%)</td><td>0.02 (+17.90%)</td><td>0.00 <b>(-52.40%)</b></td><td>197.40 (-15.17%)</td><td>170.24 (-6.33%)</td><td>168.70 (-11.44%)</td><td>147.30 (+6.89%)</td><td>18.78 <b>(-54.87%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>232.70 (n/a)</td><td>181.74 (n/a)</td><td>190.50 (n/a)</td><td>137.80 (n/a)</td><td>41.61 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (+5.01%)</td><td>0.03 <b>(+31.30%)</b></td><td>0.03 <b>(+28.10%)</b></td><td>0.02 <b>(+94.07%)</b></td><td>0.00 <b>(-54.23%)</b></td><td>177.30 <b>(-48.47%)</b></td><td>157.40 <b>(-28.99%)</b></td><td>160.20 <b>(-21.93%)</b></td><td>138.60 (-4.81%)</td><td>15.99 <b>(-78.50%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>344.10 (n/a)</td><td>221.66 (n/a)</td><td>205.20 (n/a)</td><td>145.60 (n/a)</td><td>74.36 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 <b>(+30.41%)</b></td><td>0.03 (+9.57%)</td><td>0.02 (+5.52%)</td><td>0.01 <b>(-30.36%)</b></td><td>0.01 <b>(+379.90%)</b></td><td>274.20 <b>(+43.64%)</b></td><td>173.66 (-1.10%)</td><td>167.00 (-5.28%)</td><td>121.70 <b>(-23.31%)</b></td><td>61.18 <b>(+429.17%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.90 (n/a)</td><td>175.60 (n/a)</td><td>176.30 (n/a)</td><td>158.70 (n/a)</td><td>11.56 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (-4.18%)</td><td>0.03 (+4.05%)</td><td>0.02 (-0.82%)</td><td>0.02 (+2.31%)</td><td>0.00 (-7.63%)</td><td>200.40 (-2.24%)</td><td>162.04 (-4.23%)</td><td>170.70 (+0.83%)</td><td>128.60 (+4.38%)</td><td>29.01 (-5.43%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>205.00 (n/a)</td><td>169.20 (n/a)</td><td>169.30 (n/a)</td><td>123.20 (n/a)</td><td>30.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (-11.72%)</td><td>0.02 (-5.92%)</td><td>0.02 (-0.20%)</td><td>0.02 (-1.26%)</td><td>0.00 <b>(-30.86%)</b></td><td>196.40 (+1.29%)</td><td>173.88 (+4.84%)</td><td>180.10 (+0.22%)</td><td>137.40 (+13.27%)</td><td>24.29 <b>(-20.86%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>193.90 (n/a)</td><td>165.86 (n/a)</td><td>179.70 (n/a)</td><td>121.30 (n/a)</td><td>30.69 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 <b>(+57.16%)</b></td><td>0.03 (+17.75%)</td><td>0.03 <b>(+20.01%)</b></td><td>0.02 (-10.25%)</td><td>0.01 <b>(+476.04%)</b></td><td>217.00 (+11.45%)</td><td>162.76 (-8.99%)</td><td>147.60 (-16.66%)</td><td>104.20 <b>(-36.39%)</b></td><td>47.39 <b>(+323.67%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.70 (n/a)</td><td>178.84 (n/a)</td><td>177.10 (n/a)</td><td>163.80 (n/a)</td><td>11.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (+19.94%)</td><td>0.02 (+11.59%)</td><td>0.02 (+6.47%)</td><td>0.02 (+12.51%)</td><td>0.01 <b>(+37.61%)</b></td><td>229.40 (-11.12%)</td><td>172.56 (-9.37%)</td><td>168.90 (-6.11%)</td><td>124.80 (-16.63%)</td><td>40.49 (-1.20%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>258.10 (n/a)</td><td>190.40 (n/a)</td><td>179.90 (n/a)</td><td>149.70 (n/a)</td><td>40.98 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 <b>(+30.25%)</b></td><td>0.03 <b>(+27.43%)</b></td><td>0.02 <b>(+33.84%)</b></td><td>0.02 (-2.03%)</td><td>0.01 <b>(+87.89%)</b></td><td>234.00 (+2.05%)</td><td>164.86 (-19.03%)</td><td>164.40 <b>(-25.27%)</b></td><td>122.60 <b>(-23.18%)</b></td><td>43.33 <b>(+47.72%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>229.30 (n/a)</td><td>203.60 (n/a)</td><td>220.00 (n/a)</td><td>159.60 (n/a)</td><td>29.33 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 <b>(+25.25%)</b></td><td>0.02 (+19.79%)</td><td>0.02 <b>(+37.48%)</b></td><td>0.01 (+1.84%)</td><td>0.01 <b>(+24.24%)</b></td><td>294.50 (-1.80%)</td><td>189.34 (-15.16%)</td><td>175.20 <b>(-27.27%)</b></td><td>129.20 <b>(-20.15%)</b></td><td>62.11 (+7.53%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>299.90 (n/a)</td><td>223.16 (n/a)</td><td>240.90 (n/a)</td><td>161.80 (n/a)</td><td>57.76 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 <b>(-21.57%)</b></td><td>0.02 (+1.59%)</td><td>0.03 (+18.33%)</td><td>0.02 (+9.98%)</td><td>0.00 <b>(-36.53%)</b></td><td>244.60 (-9.07%)</td><td>188.14 (-4.57%)</td><td>162.80 (-15.47%)</td><td>159.40 <b>(+27.52%)</b></td><td>38.45 <b>(-25.77%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>269.00 (n/a)</td><td>197.16 (n/a)</td><td>192.60 (n/a)</td><td>125.00 (n/a)</td><td>51.80 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (+14.07%)</td><td>0.03 (+5.20%)</td><td>0.02 (+15.76%)</td><td>0.02 (-1.84%)</td><td>0.01 <b>(+23.42%)</b></td><td>220.50 (+1.85%)</td><td>170.04 (-3.67%)</td><td>169.10 (-13.64%)</td><td>110.40 (-12.31%)</td><td>41.94 (+8.72%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>216.50 (n/a)</td><td>176.52 (n/a)</td><td>195.80 (n/a)</td><td>125.90 (n/a)</td><td>38.58 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (+15.73%)</td><td>0.03 (+12.24%)</td><td>0.03 (+8.21%)</td><td>0.02 (+7.74%)</td><td>0.00 <b>(+36.37%)</b></td><td>181.20 (-7.17%)</td><td>150.62 (-10.53%)</td><td>150.80 (-7.60%)</td><td>127.70 (-13.60%)</td><td>19.70 (+9.65%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>195.20 (n/a)</td><td>168.34 (n/a)</td><td>163.20 (n/a)</td><td>147.80 (n/a)</td><td>17.96 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (+8.61%)</td><td>0.05 (+3.25%)</td><td>0.05 (+10.94%)</td><td>0.02 <b>(-44.13%)</b></td><td>0.02 <b>(+140.44%)</b></td><td>349.60 <b>(+79.01%)</b></td><td>186.74 (+8.91%)</td><td>158.30 (-9.90%)</td><td>127.50 (-7.94%)</td><td>92.21 <b>(+327.88%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>195.30 (n/a)</td><td>171.46 (n/a)</td><td>175.70 (n/a)</td><td>138.50 (n/a)</td><td>21.55 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (-11.29%)</td><td>0.04 (-14.64%)</td><td>0.04 <b>(-21.39%)</b></td><td>0.04 (-14.72%)</td><td>0.01 (-2.95%)</td><td>224.20 (+17.26%)</td><td>190.16 (+17.62%)</td><td>200.60 <b>(+27.20%)</b></td><td>147.30 (+12.70%)</td><td>30.06 <b>(+26.17%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>191.20 (n/a)</td><td>161.68 (n/a)</td><td>157.70 (n/a)</td><td>130.70 (n/a)</td><td>23.83 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (+3.20%)</td><td>0.04 (+2.44%)</td><td>0.05 (+7.32%)</td><td>0.03 (-17.83%)</td><td>0.01 <b>(+50.62%)</b></td><td>280.10 <b>(+21.73%)</b></td><td>199.96 (-0.29%)</td><td>178.30 (-6.80%)</td><td>169.60 (-3.14%)</td><td>45.93 <b>(+79.66%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>230.10 (n/a)</td><td>200.54 (n/a)</td><td>191.30 (n/a)</td><td>175.10 (n/a)</td><td>25.56 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (-1.40%)</td><td>0.05 (+15.31%)</td><td>0.05 <b>(+23.72%)</b></td><td>0.04 (+19.15%)</td><td>0.01 <b>(-28.09%)</b></td><td>196.80 (-16.08%)</td><td>165.54 (-14.65%)</td><td>155.20 (-19.17%)</td><td>147.60 (+1.44%)</td><td>21.45 <b>(-39.63%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>234.50 (n/a)</td><td>193.96 (n/a)</td><td>192.00 (n/a)</td><td>145.50 (n/a)</td><td>35.52 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 <b>(+48.76%)</b></td><td>0.05 (+13.58%)</td><td>0.05 (+10.70%)</td><td>0.03 (-6.74%)</td><td>0.01 <b>(+210.70%)</b></td><td>249.50 (+7.22%)</td><td>184.06 (-7.45%)</td><td>180.30 (-9.62%)</td><td>119.30 <b>(-32.79%)</b></td><td>47.83 <b>(+119.64%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>232.70 (n/a)</td><td>198.88 (n/a)</td><td>199.50 (n/a)</td><td>177.50 (n/a)</td><td>21.78 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (+8.08%)</td><td>0.05 (+3.45%)</td><td>0.05 (-4.86%)</td><td>0.04 <b>(+34.88%)</b></td><td>0.01 <b>(-23.87%)</b></td><td>184.10 <b>(-25.86%)</b></td><td>165.38 (-5.54%)</td><td>176.80 (+5.11%)</td><td>133.80 (-7.47%)</td><td>22.13 <b>(-47.97%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>248.30 (n/a)</td><td>175.08 (n/a)</td><td>168.20 (n/a)</td><td>144.60 (n/a)</td><td>42.54 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 <b>(+40.19%)</b></td><td>0.05 <b>(+26.03%)</b></td><td>0.05 (+16.62%)</td><td>0.04 <b>(+37.39%)</b></td><td>0.01 <b>(+31.35%)</b></td><td>183.40 <b>(-27.19%)</b></td><td>153.20 <b>(-20.88%)</b></td><td>152.70 (-14.26%)</td><td>118.60 <b>(-28.64%)</b></td><td>23.69 <b>(-33.19%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>251.90 (n/a)</td><td>193.62 (n/a)</td><td>178.10 (n/a)</td><td>166.20 (n/a)</td><td>35.46 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (-16.54%)</td><td>0.05 (-5.18%)</td><td>0.05 (-2.63%)</td><td>0.04 (-0.84%)</td><td>0.00 <b>(-46.71%)</b></td><td>185.80 (+0.87%)</td><td>164.16 (+4.19%)</td><td>163.30 (+2.70%)</td><td>148.40 (+19.87%)</td><td>15.01 <b>(-35.20%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>184.20 (n/a)</td><td>157.56 (n/a)</td><td>159.00 (n/a)</td><td>123.80 (n/a)</td><td>23.16 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 <b>(+24.33%)</b></td><td>0.06 <b>(+24.03%)</b></td><td>0.05 <b>(+21.06%)</b></td><td>0.04 (+11.35%)</td><td>0.01 <b>(+36.91%)</b></td><td>222.10 (-10.19%)</td><td>155.00 (-18.42%)</td><td>149.80 (-17.42%)</td><td>124.60 (-19.61%)</td><td>39.54 (+1.91%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>247.30 (n/a)</td><td>190.00 (n/a)</td><td>181.40 (n/a)</td><td>155.00 (n/a)</td><td>38.80 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 <b>(+23.41%)</b></td><td>0.05 (+9.12%)</td><td>0.05 (+8.48%)</td><td>0.04 (+7.71%)</td><td>0.01 <b>(+64.61%)</b></td><td>223.70 (-7.18%)</td><td>174.62 (-5.95%)</td><td>168.00 (-7.79%)</td><td>127.60 (-18.98%)</td><td>43.48 <b>(+27.20%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>241.00 (n/a)</td><td>185.66 (n/a)</td><td>182.20 (n/a)</td><td>157.50 (n/a)</td><td>34.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 <b>(+62.57%)</b></td><td>0.06 <b>(+50.61%)</b></td><td>0.06 <b>(+49.21%)</b></td><td>0.04 (+13.99%)</td><td>0.01 <b>(+169.10%)</b></td><td>222.30 (-12.24%)</td><td>147.70 <b>(-30.52%)</b></td><td>138.70 <b>(-33.00%)</b></td><td>109.30 <b>(-38.49%)</b></td><td>44.80 <b>(+47.58%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>253.30 (n/a)</td><td>212.58 (n/a)</td><td>207.00 (n/a)</td><td>177.70 (n/a)</td><td>30.36 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 <b>(+23.77%)</b></td><td>0.05 (+19.82%)</td><td>0.05 (+3.78%)</td><td>0.04 <b>(+70.21%)</b></td><td>0.01 (+3.65%)</td><td>217.10 <b>(-41.26%)</b></td><td>171.12 <b>(-20.39%)</b></td><td>169.10 (-3.59%)</td><td>125.20 (-19.17%)</td><td>40.99 <b>(-53.37%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>369.60 (n/a)</td><td>214.96 (n/a)</td><td>175.40 (n/a)</td><td>154.90 (n/a)</td><td>87.91 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (-16.40%)</td><td>0.05 (+15.88%)</td><td>0.05 <b>(+38.59%)</b></td><td>0.03 (+5.72%)</td><td>0.01 <b>(-26.26%)</b></td><td>290.30 (-5.38%)</td><td>176.14 (-16.18%)</td><td>154.60 <b>(-27.86%)</b></td><td>133.90 (+19.66%)</td><td>64.71 (-7.19%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>306.80 (n/a)</td><td>210.14 (n/a)</td><td>214.30 (n/a)</td><td>111.90 (n/a)</td><td>69.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (+1.31%)</td><td>0.04 (-6.11%)</td><td>0.05 (+10.09%)</td><td>0.03 <b>(-27.31%)</b></td><td>0.01 <b>(+212.37%)</b></td><td>260.40 <b>(+37.56%)</b></td><td>194.70 (+11.31%)</td><td>161.50 (-9.17%)</td><td>155.40 (-1.33%)</td><td>49.57 <b>(+321.91%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>189.30 (n/a)</td><td>174.92 (n/a)</td><td>177.80 (n/a)</td><td>157.50 (n/a)</td><td>11.75 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (+7.73%)</td><td>0.05 (+14.87%)</td><td>0.05 (+14.63%)</td><td>0.04 (+19.55%)</td><td>0.01 (-15.80%)</td><td>183.60 (-16.36%)</td><td>163.82 (-13.74%)</td><td>169.00 (-12.75%)</td><td>137.40 (-7.16%)</td><td>18.96 <b>(-34.96%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.50 (n/a)</td><td>189.92 (n/a)</td><td>193.70 (n/a)</td><td>148.00 (n/a)</td><td>29.14 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (+19.93%)</td><td>0.05 <b>(+24.54%)</b></td><td>0.05 <b>(+25.23%)</b></td><td>0.05 <b>(+27.61%)</b></td><td>0.01 (-0.79%)</td><td>173.20 <b>(-21.66%)</b></td><td>152.34 <b>(-20.03%)</b></td><td>151.10 <b>(-20.14%)</b></td><td>134.90 (-16.63%)</td><td>14.67 <b>(-35.07%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>221.10 (n/a)</td><td>190.50 (n/a)</td><td>189.20 (n/a)</td><td>161.80 (n/a)</td><td>22.59 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 (+10.26%)</td><td>0.13 <b>(+23.67%)</b></td><td>0.12 (+15.32%)</td><td>0.11 <b>(+47.98%)</b></td><td>0.01 <b>(-41.42%)</b></td><td>144.00 <b>(-32.46%)</b></td><td>128.28 <b>(-21.89%)</b></td><td>132.00 (-13.33%)</td><td>111.20 (-9.30%)</td><td>13.53 <b>(-65.00%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>213.20 (n/a)</td><td>164.22 (n/a)</td><td>152.30 (n/a)</td><td>122.60 (n/a)</td><td>38.66 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 <b>(+20.49%)</b></td><td>0.12 <b>(+28.91%)</b></td><td>0.13 <b>(+30.71%)</b></td><td>0.10 <b>(+61.42%)</b></td><td>0.02 (-6.90%)</td><td>160.50 <b>(-38.05%)</b></td><td>136.86 <b>(-24.40%)</b></td><td>130.60 <b>(-23.49%)</b></td><td>109.70 (-17.02%)</td><td>22.60 <b>(-52.20%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>259.10 (n/a)</td><td>181.04 (n/a)</td><td>170.70 (n/a)</td><td>132.20 (n/a)</td><td>47.28 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (+15.62%)</td><td>0.09 (+11.97%)</td><td>0.08 (+11.11%)</td><td>0.08 <b>(+29.48%)</b></td><td>0.01 (-15.34%)</td><td>212.20 <b>(-22.78%)</b></td><td>188.80 (-12.40%)</td><td>198.00 (-10.00%)</td><td>144.80 (-13.50%)</td><td>26.89 <b>(-42.37%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.02 (n/a)</td><td>274.80 (n/a)</td><td>215.52 (n/a)</td><td>220.00 (n/a)</td><td>167.40 (n/a)</td><td>46.66 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 <b>(+30.35%)</b></td><td>0.09 (+15.90%)</td><td>0.09 <b>(+20.18%)</b></td><td>0.07 (+6.38%)</td><td>0.02 <b>(+106.27%)</b></td><td>224.00 (-6.00%)</td><td>187.14 (-12.02%)</td><td>179.10 (-16.78%)</td><td>141.00 <b>(-23.33%)</b></td><td>34.70 <b>(+52.43%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>238.30 (n/a)</td><td>212.70 (n/a)</td><td>215.20 (n/a)</td><td>183.90 (n/a)</td><td>22.76 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (+17.23%)</td><td>0.11 (+7.01%)</td><td>0.12 (+14.15%)</td><td>0.06 <b>(-32.64%)</b></td><td>0.03 <b>(+133.45%)</b></td><td>296.00 <b>(+48.45%)</b></td><td>167.64 (+2.76%)</td><td>140.90 (-12.38%)</td><td>113.70 (-14.70%)</td><td>73.64 <b>(+212.35%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>199.40 (n/a)</td><td>163.14 (n/a)</td><td>160.80 (n/a)</td><td>133.30 (n/a)</td><td>23.58 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (-6.79%)</td><td>0.10 (+1.39%)</td><td>0.10 (+3.82%)</td><td>0.10 <b>(+26.71%)</b></td><td>0.01 <b>(-49.89%)</b></td><td>171.10 <b>(-21.08%)</b></td><td>158.40 (-4.20%)</td><td>162.80 (-3.67%)</td><td>133.60 (+7.22%)</td><td>15.35 <b>(-57.26%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>216.80 (n/a)</td><td>165.34 (n/a)</td><td>169.00 (n/a)</td><td>124.60 (n/a)</td><td>35.91 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (+18.91%)</td><td>0.11 (+19.70%)</td><td>0.11 (+18.52%)</td><td>0.10 <b>(+28.41%)</b></td><td>0.01 (-13.01%)</td><td>159.40 <b>(-22.09%)</b></td><td>149.66 (-16.80%)</td><td>153.80 (-15.63%)</td><td>132.60 (-15.92%)</td><td>10.33 <b>(-43.34%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>204.60 (n/a)</td><td>179.88 (n/a)</td><td>182.30 (n/a)</td><td>157.70 (n/a)</td><td>18.23 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (+19.20%)</td><td>0.11 (+7.50%)</td><td>0.10 (+4.86%)</td><td>0.09 (-4.19%)</td><td>0.02 <b>(+86.77%)</b></td><td>191.00 (+4.37%)</td><td>157.66 (-5.28%)</td><td>160.10 (-4.65%)</td><td>116.20 (-16.16%)</td><td>27.68 <b>(+62.46%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>183.00 (n/a)</td><td>166.44 (n/a)</td><td>167.90 (n/a)</td><td>138.60 (n/a)</td><td>17.04 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (+9.37%)</td><td>0.12 (+18.18%)</td><td>0.12 <b>(+25.03%)</b></td><td>0.10 (+12.76%)</td><td>0.01 (+6.56%)</td><td>170.30 (-11.35%)</td><td>144.12 (-15.49%)</td><td>139.00 <b>(-20.02%)</b></td><td>128.00 (-8.57%)</td><td>18.09 (-14.86%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>192.10 (n/a)</td><td>170.54 (n/a)</td><td>173.80 (n/a)</td><td>140.00 (n/a)</td><td>21.24 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 <b>(+25.79%)</b></td><td>0.11 (+7.08%)</td><td>0.11 (+3.83%)</td><td>0.08 (-12.93%)</td><td>0.02 <b>(+305.95%)</b></td><td>196.50 (+14.85%)</td><td>154.98 (-2.96%)</td><td>154.70 (-3.67%)</td><td>117.70 <b>(-20.53%)</b></td><td>34.78 <b>(+266.91%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>171.10 (n/a)</td><td>159.70 (n/a)</td><td>160.60 (n/a)</td><td>148.10 (n/a)</td><td>9.48 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (+3.38%)</td><td>0.11 (+6.98%)</td><td>0.10 (+14.26%)</td><td>0.08 (+18.92%)</td><td>0.02 (-17.68%)</td><td>204.70 (-15.90%)</td><td>158.64 (-8.88%)</td><td>159.70 (-12.49%)</td><td>118.20 (-3.27%)</td><td>32.34 <b>(-32.12%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>243.40 (n/a)</td><td>174.10 (n/a)</td><td>182.50 (n/a)</td><td>122.20 (n/a)</td><td>47.65 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (-19.74%)</td><td>0.10 (+0.18%)</td><td>0.09 (+4.80%)</td><td>0.09 (+9.82%)</td><td>0.01 <b>(-61.14%)</b></td><td>179.40 (-8.93%)</td><td>167.76 (-3.52%)</td><td>174.40 (-4.60%)</td><td>142.10 <b>(+24.54%)</b></td><td>15.38 <b>(-54.77%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>197.00 (n/a)</td><td>173.88 (n/a)</td><td>182.80 (n/a)</td><td>114.10 (n/a)</td><td>34.00 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (+11.82%)</td><td>0.09 (+5.14%)</td><td>0.09 (-0.50%)</td><td>0.08 (+6.13%)</td><td>0.01 <b>(+54.68%)</b></td><td>195.10 (-5.79%)</td><td>182.86 (-4.57%)</td><td>190.70 (+0.47%)</td><td>158.40 (-10.56%)</td><td>15.98 <b>(+30.79%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>207.10 (n/a)</td><td>191.62 (n/a)</td><td>189.80 (n/a)</td><td>177.10 (n/a)</td><td>12.22 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (+14.41%)</td><td>0.11 (+12.03%)</td><td>0.11 (+18.07%)</td><td>0.08 (+7.39%)</td><td>0.02 <b>(+34.51%)</b></td><td>204.80 (-6.91%)</td><td>161.36 (-9.72%)</td><td>147.70 (-15.31%)</td><td>122.50 (-12.62%)</td><td>33.69 (+11.55%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>220.00 (n/a)</td><td>178.74 (n/a)</td><td>174.40 (n/a)</td><td>140.20 (n/a)</td><td>30.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (+5.72%)</td><td>0.10 (+3.82%)</td><td>0.09 (-6.54%)</td><td>0.08 (+3.22%)</td><td>0.01 (+16.77%)</td><td>193.60 (-3.10%)</td><td>171.82 (-3.39%)</td><td>185.50 (+6.98%)</td><td>139.50 (-5.36%)</td><td>23.39 (+4.80%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>199.80 (n/a)</td><td>177.84 (n/a)</td><td>173.40 (n/a)</td><td>147.40 (n/a)</td><td>22.32 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 <b>(+29.59%)</b></td><td>0.10 (+12.35%)</td><td>0.10 (+12.58%)</td><td>0.07 (-9.02%)</td><td>0.02 <b>(+235.45%)</b></td><td>219.90 (+9.90%)</td><td>171.10 (-8.15%)</td><td>161.50 (-11.17%)</td><td>133.70 <b>(-22.81%)</b></td><td>36.47 <b>(+181.82%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>200.10 (n/a)</td><td>186.28 (n/a)</td><td>181.80 (n/a)</td><td>173.20 (n/a)</td><td>12.94 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (-17.07%)</td><td>0.23 (+12.68%)</td><td>0.24 <b>(+27.60%)</b></td><td>0.18 <b>(+32.99%)</b></td><td>0.03 <b>(-52.76%)</b></td><td>181.50 <b>(-24.81%)</b></td><td>145.16 (-17.57%)</td><td>136.30 <b>(-21.62%)</b></td><td>125.30 <b>(+20.60%)</b></td><td>23.70 <b>(-58.13%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.32 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.14 (n/a)</td><td>0.07 (n/a)</td><td>241.40 (n/a)</td><td>176.10 (n/a)</td><td>173.90 (n/a)</td><td>103.90 (n/a)</td><td>56.59 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 <b>(+20.73%)</b></td><td>0.20 (-1.97%)</td><td>0.18 (-13.19%)</td><td>0.15 (+8.63%)</td><td>0.05 <b>(+37.73%)</b></td><td>218.90 (-7.95%)</td><td>174.28 (+3.52%)</td><td>177.80 (+15.23%)</td><td>116.10 (-17.19%)</td><td>41.36 (+2.93%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.21 (n/a)</td><td>0.14 (n/a)</td><td>0.04 (n/a)</td><td>237.80 (n/a)</td><td>168.36 (n/a)</td><td>154.30 (n/a)</td><td>140.20 (n/a)</td><td>40.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.17 (-11.88%)</td><td>0.15 (+0.07%)</td><td>0.15 (-1.94%)</td><td>0.13 <b>(+23.34%)</b></td><td>0.01 <b>(-56.19%)</b></td><td>252.50 (-18.91%)</td><td>217.18 (-3.15%)</td><td>212.80 (+1.96%)</td><td>196.60 (+13.44%)</td><td>20.90 <b>(-60.18%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.03 (n/a)</td><td>311.40 (n/a)</td><td>224.24 (n/a)</td><td>208.70 (n/a)</td><td>173.30 (n/a)</td><td>52.48 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 (-5.57%)</td><td>0.18 (-4.13%)</td><td>0.18 (-2.34%)</td><td>0.15 (-6.08%)</td><td>0.02 (+2.83%)</td><td>212.00 (+6.48%)</td><td>187.02 (+4.46%)</td><td>180.00 (+2.39%)</td><td>165.70 (+5.88%)</td><td>19.08 (+16.91%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>199.10 (n/a)</td><td>179.04 (n/a)</td><td>175.80 (n/a)</td><td>156.50 (n/a)</td><td>16.32 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 <b>(+32.29%)</b></td><td>0.22 <b>(+23.79%)</b></td><td>0.23 <b>(+31.82%)</b></td><td>0.15 (-2.90%)</td><td>0.05 <b>(+138.73%)</b></td><td>213.00 (+3.00%)</td><td>158.36 (-16.30%)</td><td>143.60 <b>(-24.14%)</b></td><td>117.80 <b>(-24.44%)</b></td><td>38.92 <b>(+89.06%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>206.80 (n/a)</td><td>189.20 (n/a)</td><td>189.30 (n/a)</td><td>155.90 (n/a)</td><td>20.59 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (+18.29%)</td><td>0.22 (+16.59%)</td><td>0.22 (+16.53%)</td><td>0.16 (+16.96%)</td><td>0.04 <b>(+23.16%)</b></td><td>208.00 (-14.51%)</td><td>155.38 (-14.02%)</td><td>151.80 (-14.19%)</td><td>122.10 (-15.44%)</td><td>33.21 (-12.33%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.13 (n/a)</td><td>0.03 (n/a)</td><td>243.30 (n/a)</td><td>180.72 (n/a)</td><td>176.90 (n/a)</td><td>144.40 (n/a)</td><td>37.88 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (-4.42%)</td><td>0.23 (+3.83%)</td><td>0.22 (+11.52%)</td><td>0.20 (+6.74%)</td><td>0.03 <b>(-26.41%)</b></td><td>165.10 (-6.35%)</td><td>144.42 (-4.91%)</td><td>149.10 (-10.34%)</td><td>120.30 (+4.61%)</td><td>18.79 <b>(-28.33%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>176.30 (n/a)</td><td>151.88 (n/a)</td><td>166.30 (n/a)</td><td>115.00 (n/a)</td><td>26.23 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (-14.04%)</td><td>0.21 (-1.41%)</td><td>0.20 (+1.46%)</td><td>0.19 (+5.26%)</td><td>0.03 <b>(-42.14%)</b></td><td>174.10 (-5.02%)</td><td>158.56 (-1.06%)</td><td>164.70 (-1.44%)</td><td>123.80 (+16.35%)</td><td>19.93 <b>(-35.80%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.05 (n/a)</td><td>183.30 (n/a)</td><td>160.26 (n/a)</td><td>167.10 (n/a)</td><td>106.40 (n/a)</td><td>31.04 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.21 <b>(-32.78%)</b></td><td>0.19 (-12.90%)</td><td>0.19 (-13.26%)</td><td>0.17 (+15.30%)</td><td>0.01 <b>(-77.30%)</b></td><td>187.70 (-13.26%)</td><td>173.14 (+9.24%)</td><td>174.70 (+15.31%)</td><td>156.90 <b>(+48.72%)</b></td><td>11.89 <b>(-70.32%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.15 (n/a)</td><td>0.06 (n/a)</td><td>216.40 (n/a)</td><td>158.50 (n/a)</td><td>151.50 (n/a)</td><td>105.50 (n/a)</td><td>40.06 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.24 (-3.67%)</td><td>0.20 (+4.33%)</td><td>0.20 (-10.04%)</td><td>0.18 <b>(+90.90%)</b></td><td>0.02 <b>(-61.33%)</b></td><td>187.10 <b>(-47.61%)</b></td><td>162.50 (-15.03%)</td><td>163.10 (+11.18%)</td><td>136.50 (+3.80%)</td><td>18.63 <b>(-80.22%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>357.10 (n/a)</td><td>191.24 (n/a)</td><td>146.70 (n/a)</td><td>131.50 (n/a)</td><td>94.17 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.24 (+2.31%)</td><td>0.21 (+8.97%)</td><td>0.22 (+12.92%)</td><td>0.18 <b>(+66.76%)</b></td><td>0.02 <b>(-52.87%)</b></td><td>178.70 <b>(-40.05%)</b></td><td>158.00 (-14.14%)</td><td>151.10 (-11.43%)</td><td>135.60 (-2.24%)</td><td>18.05 <b>(-72.54%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.11 (n/a)</td><td>0.05 (n/a)</td><td>298.10 (n/a)</td><td>184.02 (n/a)</td><td>170.60 (n/a)</td><td>138.70 (n/a)</td><td>65.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 <b>(-26.23%)</b></td><td>0.17 (-9.97%)</td><td>0.17 (-9.20%)</td><td>0.11 (+15.87%)</td><td>0.05 <b>(-37.55%)</b></td><td>305.20 (-13.69%)</td><td>200.88 (+2.91%)</td><td>191.60 (+10.11%)</td><td>150.10 <b>(+35.47%)</b></td><td>63.02 <b>(-32.06%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.30 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>353.60 (n/a)</td><td>195.20 (n/a)</td><td>174.00 (n/a)</td><td>110.80 (n/a)</td><td>92.75 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 <b>(+24.80%)</b></td><td>0.21 (+9.49%)</td><td>0.22 <b>(+25.68%)</b></td><td>0.09 <b>(-44.09%)</b></td><td>0.07 <b>(+132.55%)</b></td><td>368.10 <b>(+78.86%)</b></td><td>185.44 (+5.05%)</td><td>145.70 <b>(-20.47%)</b></td><td>118.10 (-19.82%)</td><td>103.09 <b>(+273.75%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>205.80 (n/a)</td><td>176.52 (n/a)</td><td>183.20 (n/a)</td><td>147.30 (n/a)</td><td>27.58 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (-0.44%)</td><td>0.22 (+18.09%)</td><td>0.21 <b>(+32.92%)</b></td><td>0.16 <b>(+31.20%)</b></td><td>0.04 <b>(-30.36%)</b></td><td>204.00 <b>(-23.80%)</b></td><td>156.20 (-19.27%)</td><td>159.40 <b>(-24.78%)</b></td><td>119.80 (+0.50%)</td><td>31.45 <b>(-45.29%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.27 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.06 (n/a)</td><td>267.70 (n/a)</td><td>193.48 (n/a)</td><td>211.90 (n/a)</td><td>119.20 (n/a)</td><td>57.48 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.24 <b>(+21.92%)</b></td><td>0.20 (+14.11%)</td><td>0.20 <b>(+25.75%)</b></td><td>0.15 (-7.52%)</td><td>0.04 <b>(+120.02%)</b></td><td>223.30 (+8.14%)</td><td>172.60 (-10.09%)</td><td>163.30 <b>(-20.46%)</b></td><td>138.00 (-17.95%)</td><td>36.27 <b>(+90.94%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>206.50 (n/a)</td><td>191.96 (n/a)</td><td>205.30 (n/a)</td><td>168.20 (n/a)</td><td>18.99 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.25 (+10.76%)</td><td>0.19 (+8.41%)</td><td>0.18 (+2.30%)</td><td>0.16 (+9.67%)</td><td>0.04 (+16.84%)</td><td>205.20 (-8.84%)</td><td>176.56 (-7.51%)</td><td>183.90 (-2.28%)</td><td>130.00 (-9.72%)</td><td>29.46 (-3.75%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.03 (n/a)</td><td>225.10 (n/a)</td><td>190.90 (n/a)</td><td>188.20 (n/a)</td><td>144.00 (n/a)</td><td>30.60 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (-0.10%)</td><td>0.18 (+0.19%)</td><td>0.18 (+0.31%)</td><td>0.18 (+0.32%)</td><td>0.00 <b>(-71.33%)</b></td><td>47581.50 (-0.32%)</td><td>47522.62 (-0.19%)</td><td>47515.90 (-0.31%)</td><td>47496.30 (+0.10%)</td><td>34.57 <b>(-71.40%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47732.40 (n/a)</td><td>47614.52 (n/a)</td><td>47663.00 (n/a)</td><td>47448.20 (n/a)</td><td>120.89 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (-0.02%)</td><td>0.18 (-0.07%)</td><td>0.18 (-0.10%)</td><td>0.18 (-0.04%)</td><td>0.00 (+3.39%)</td><td>47629.70 (+0.04%)</td><td>47559.72 (+0.07%)</td><td>47585.80 (+0.10%)</td><td>47460.40 (+0.02%)</td><td>66.82 (+3.41%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.00 (n/a)</td><td>47611.10 (n/a)</td><td>47527.62 (n/a)</td><td>47537.20 (n/a)</td><td>47451.90 (n/a)</td><td>64.62 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (+0.03%)</td><td>0.11 (+0.05%)</td><td>0.11 (+0.05%)</td><td>0.11 (+0.06%)</td><td>0.00 <b>(-29.88%)</b></td><td>375686.90 (-0.06%)</td><td>375450.34 (-0.05%)</td><td>375433.70 (-0.05%)</td><td>375160.40 (-0.03%)</td><td>193.58 <b>(-29.95%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.00 (n/a)</td><td>375918.30 (n/a)</td><td>375630.62 (n/a)</td><td>375603.10 (n/a)</td><td>375270.50 (n/a)</td><td>276.35 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 <b>(+32.33%)</b></td><td>0.17 (+16.77%)</td><td>0.17 <b>(+22.74%)</b></td><td>0.12 (-8.96%)</td><td>0.04 <b>(+127.24%)</b></td><td>212.60 (+9.87%)</td><td>151.66 (-11.20%)</td><td>143.50 (-18.51%)</td><td>110.10 <b>(-24.43%)</b></td><td>38.55 <b>(+93.87%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>193.50 (n/a)</td><td>170.78 (n/a)</td><td>176.10 (n/a)</td><td>145.70 (n/a)</td><td>19.88 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.40 <b>(+28.02%)</b></td><td>0.30 (+8.36%)</td><td>0.28 (-7.47%)</td><td>0.25 (+18.95%)</td><td>0.06 <b>(+26.88%)</b></td><td>193.30 (-15.96%)</td><td>165.68 (-7.66%)</td><td>173.20 (+8.05%)</td><td>122.50 <b>(-21.88%)</b></td><td>26.21 (-18.42%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (n/a)</td><td>0.28 (n/a)</td><td>0.31 (n/a)</td><td>0.21 (n/a)</td><td>0.04 (n/a)</td><td>230.00 (n/a)</td><td>179.42 (n/a)</td><td>160.30 (n/a)</td><td>156.80 (n/a)</td><td>32.13 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>13.58 (+5.06%)</td><td>12.98 (+2.49%)</td><td>13.00 (+1.76%)</td><td>12.47 (+1.90%)</td><td>0.41 <b>(+37.04%)</b></td><td>840.60 (-1.86%)</td><td>808.52 (-2.39%)</td><td>806.30 (-1.74%)</td><td>772.20 (-4.81%)</td><td>25.40 <b>(+28.09%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>12.93 (n/a)</td><td>12.66 (n/a)</td><td>12.78 (n/a)</td><td>12.24 (n/a)</td><td>0.30 (n/a)</td><td>856.50 (n/a)</td><td>828.34 (n/a)</td><td>820.60 (n/a)</td><td>811.20 (n/a)</td><td>19.83 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (-13.59%)</td><td>0.25 (-5.85%)</td><td>0.23 (-14.51%)</td><td>0.23 (+6.00%)</td><td>0.02 <b>(-47.54%)</b></td><td>179.60 (-5.67%)</td><td>167.74 (+4.85%)</td><td>176.30 (+16.99%)</td><td>152.60 (+15.78%)</td><td>13.69 <b>(-44.20%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.22 (n/a)</td><td>0.04 (n/a)</td><td>190.40 (n/a)</td><td>159.98 (n/a)</td><td>150.70 (n/a)</td><td>131.80 (n/a)</td><td>24.54 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 <b>(+33.26%)</b></td><td>0.04 <b>(+28.98%)</b></td><td>0.04 <b>(+41.90%)</b></td><td>0.02 (-13.50%)</td><td>0.01 <b>(+178.18%)</b></td><td>220.60 (+15.56%)</td><td>138.78 (-17.90%)</td><td>120.20 <b>(-29.54%)</b></td><td>106.40 <b>(-24.96%)</b></td><td>46.57 <b>(+157.56%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>190.90 (n/a)</td><td>169.04 (n/a)</td><td>170.60 (n/a)</td><td>141.80 (n/a)</td><td>18.08 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 <b>(+31.72%)</b></td><td>0.03 (-0.75%)</td><td>0.02 (-14.91%)</td><td>0.02 <b>(-20.47%)</b></td><td>0.01 <b>(+703.88%)</b></td><td>198.20 <b>(+25.76%)</b></td><td>159.00 (+6.74%)</td><td>171.60 (+17.53%)</td><td>110.30 <b>(-24.09%)</b></td><td>40.93 <b>(+673.96%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.00 (n/a)</td><td>157.60 (n/a)</td><td>148.96 (n/a)</td><td>146.00 (n/a)</td><td>145.30 (n/a)</td><td>5.29 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (-11.62%)</td><td>0.04 (+6.07%)</td><td>0.04 (+19.93%)</td><td>0.03 <b>(+34.58%)</b></td><td>0.00 <b>(-61.88%)</b></td><td>189.20 <b>(-25.69%)</b></td><td>158.62 (-10.91%)</td><td>153.80 (-16.64%)</td><td>143.20 (+13.11%)</td><td>17.70 <b>(-65.86%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>254.60 (n/a)</td><td>178.04 (n/a)</td><td>184.50 (n/a)</td><td>126.60 (n/a)</td><td>51.86 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (+5.70%)</td><td>0.03 (+8.64%)</td><td>0.03 (+7.58%)</td><td>0.02 <b>(+26.65%)</b></td><td>0.01 (-2.88%)</td><td>183.00 <b>(-21.02%)</b></td><td>152.96 (-9.10%)</td><td>152.80 (-7.06%)</td><td>109.20 (-5.37%)</td><td>30.77 <b>(-25.88%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>231.70 (n/a)</td><td>168.28 (n/a)</td><td>164.40 (n/a)</td><td>115.40 (n/a)</td><td>41.51 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (-6.78%)</td><td>0.03 (-1.54%)</td><td>0.04 (+14.15%)</td><td>0.02 <b>(-20.27%)</b></td><td>0.01 <b>(+23.40%)</b></td><td>243.90 <b>(+25.40%)</b></td><td>168.90 (+3.93%)</td><td>142.90 (-12.39%)</td><td>138.80 (+7.26%)</td><td>44.73 <b>(+64.40%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>194.50 (n/a)</td><td>162.52 (n/a)</td><td>163.10 (n/a)</td><td>129.40 (n/a)</td><td>27.21 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 <b>(+21.35%)</b></td><td>0.03 (+10.71%)</td><td>0.03 (+18.60%)</td><td>0.02 (-8.05%)</td><td>0.01 <b>(+139.41%)</b></td><td>193.20 (+8.78%)</td><td>153.08 (-7.28%)</td><td>145.50 (-15.70%)</td><td>119.90 (-17.59%)</td><td>31.19 <b>(+114.84%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>177.60 (n/a)</td><td>165.10 (n/a)</td><td>172.60 (n/a)</td><td>145.50 (n/a)</td><td>14.52 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (+12.89%)</td><td>0.03 (+16.28%)</td><td>0.04 <b>(+20.52%)</b></td><td>0.02 (-1.27%)</td><td>0.01 <b>(+38.83%)</b></td><td>212.70 (+1.29%)</td><td>155.40 (-12.97%)</td><td>141.80 (-17.03%)</td><td>137.50 (-11.40%)</td><td>32.17 <b>(+27.70%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.00 (n/a)</td><td>178.56 (n/a)</td><td>170.90 (n/a)</td><td>155.20 (n/a)</td><td>25.19 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (+16.30%)</td><td>0.03 (+3.26%)</td><td>0.03 (+7.68%)</td><td>0.02 (-8.72%)</td><td>0.00 <b>(+85.17%)</b></td><td>213.50 (+9.60%)</td><td>168.32 (-1.29%)</td><td>155.40 (-7.11%)</td><td>132.30 (-14.04%)</td><td>31.67 <b>(+78.73%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>194.80 (n/a)</td><td>170.52 (n/a)</td><td>167.30 (n/a)</td><td>153.90 (n/a)</td><td>17.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (-1.58%)</td><td>0.03 (+2.52%)</td><td>0.03 (+0.18%)</td><td>0.02 (+10.80%)</td><td>0.01 (-15.44%)</td><td>193.80 (-9.73%)</td><td>160.40 (-4.10%)</td><td>172.80 (-0.17%)</td><td>119.30 (+1.62%)</td><td>31.57 <b>(-22.46%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>214.70 (n/a)</td><td>167.26 (n/a)</td><td>173.10 (n/a)</td><td>117.40 (n/a)</td><td>40.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 <b>(+21.60%)</b></td><td>0.03 (+2.66%)</td><td>0.02 (-5.83%)</td><td>0.02 (-8.48%)</td><td>0.01 <b>(+130.97%)</b></td><td>229.80 (+9.27%)</td><td>174.06 (+2.39%)</td><td>178.20 (+6.20%)</td><td>122.50 (-17.73%)</td><td>47.95 <b>(+99.35%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>210.30 (n/a)</td><td>170.00 (n/a)</td><td>167.80 (n/a)</td><td>148.90 (n/a)</td><td>24.05 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (+18.05%)</td><td>0.03 (+12.63%)</td><td>0.03 (+17.30%)</td><td>0.02 (-5.04%)</td><td>0.00 <b>(+171.19%)</b></td><td>200.90 (+5.29%)</td><td>162.90 (-9.72%)</td><td>156.50 (-14.71%)</td><td>137.50 (-15.33%)</td><td>26.18 <b>(+144.39%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>190.80 (n/a)</td><td>180.44 (n/a)</td><td>183.50 (n/a)</td><td>162.40 (n/a)</td><td>10.71 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 <b>(-21.43%)</b></td><td>0.02 (-3.71%)</td><td>0.02 (-5.22%)</td><td>0.02 (-4.21%)</td><td>0.00 <b>(-33.32%)</b></td><td>231.50 (+4.37%)</td><td>180.84 (+1.68%)</td><td>185.50 (+5.52%)</td><td>143.80 <b>(+27.26%)</b></td><td>36.63 (-11.02%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>221.80 (n/a)</td><td>177.86 (n/a)</td><td>175.80 (n/a)</td><td>113.00 (n/a)</td><td>41.17 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (-4.40%)</td><td>0.02 (+6.69%)</td><td>0.02 (+15.82%)</td><td>0.02 (+16.50%)</td><td>0.00 <b>(-35.91%)</b></td><td>205.10 (-14.15%)</td><td>176.88 (-8.68%)</td><td>181.80 (-13.68%)</td><td>140.20 (+4.63%)</td><td>23.45 <b>(-43.02%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>238.90 (n/a)</td><td>193.70 (n/a)</td><td>210.60 (n/a)</td><td>134.00 (n/a)</td><td>41.16 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (-6.68%)</td><td>0.02 (+0.17%)</td><td>0.02 (+2.15%)</td><td>0.02 (+1.26%)</td><td>0.00 (-17.87%)</td><td>231.10 (-1.24%)</td><td>187.76 (-0.79%)</td><td>190.10 (-2.11%)</td><td>161.30 (+7.18%)</td><td>27.77 (-13.01%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>234.00 (n/a)</td><td>189.26 (n/a)</td><td>194.20 (n/a)</td><td>150.50 (n/a)</td><td>31.92 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 <b>(-21.15%)</b></td><td>0.02 (-11.55%)</td><td>0.02 (+0.89%)</td><td>0.02 (-17.77%)</td><td>0.01 <b>(-30.71%)</b></td><td>287.40 <b>(+21.63%)</b></td><td>197.48 (+10.72%)</td><td>184.20 (-0.91%)</td><td>129.80 <b>(+26.88%)</b></td><td>57.94 (+9.94%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>236.30 (n/a)</td><td>178.36 (n/a)</td><td>185.90 (n/a)</td><td>102.30 (n/a)</td><td>52.70 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.02 (-5.02%)</td><td>0.02 (-0.77%)</td><td>0.02 (+0.30%)</td><td>0.02 <b>(+21.90%)</b></td><td>0.00 <b>(-44.13%)</b></td><td>227.60 (-17.98%)</td><td>211.86 (-1.27%)</td><td>218.60 (-0.32%)</td><td>178.30 (+5.25%)</td><td>19.46 <b>(-52.75%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>277.50 (n/a)</td><td>214.58 (n/a)</td><td>219.30 (n/a)</td><td>169.40 (n/a)</td><td>41.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (+19.06%)</td><td>0.05 (+15.41%)</td><td>0.05 (+15.50%)</td><td>0.04 (+12.60%)</td><td>0.01 <b>(+33.00%)</b></td><td>200.70 (-11.16%)</td><td>157.86 (-12.81%)</td><td>155.00 (-13.41%)</td><td>129.80 (-15.99%)</td><td>28.97 (-0.73%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>225.90 (n/a)</td><td>181.06 (n/a)</td><td>179.00 (n/a)</td><td>154.50 (n/a)</td><td>29.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (-16.73%)</td><td>0.07 (-10.50%)</td><td>0.07 (-11.39%)</td><td>0.06 (+1.86%)</td><td>0.01 <b>(-46.58%)</b></td><td>194.80 (-1.81%)</td><td>180.98 (+10.18%)</td><td>183.00 (+12.82%)</td><td>153.70 <b>(+20.08%)</b></td><td>16.46 <b>(-36.92%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.01 (n/a)</td><td>198.40 (n/a)</td><td>164.26 (n/a)</td><td>162.20 (n/a)</td><td>128.00 (n/a)</td><td>26.10 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (+14.09%)</td><td>0.06 (-0.79%)</td><td>0.05 (-9.77%)</td><td>0.04 (-9.82%)</td><td>0.01 <b>(+72.01%)</b></td><td>188.10 (+10.84%)</td><td>152.18 (+2.75%)</td><td>155.80 (+10.81%)</td><td>116.00 (-12.32%)</td><td>28.83 <b>(+65.43%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>169.70 (n/a)</td><td>148.10 (n/a)</td><td>140.60 (n/a)</td><td>132.30 (n/a)</td><td>17.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 (+2.39%)</td><td>0.07 (+6.83%)</td><td>0.07 (-2.64%)</td><td>0.06 (+19.41%)</td><td>0.01 <b>(-29.66%)</b></td><td>176.80 (-16.25%)</td><td>150.38 (-8.78%)</td><td>157.00 (+2.75%)</td><td>121.10 (-2.34%)</td><td>21.50 <b>(-44.31%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>211.10 (n/a)</td><td>164.86 (n/a)</td><td>152.80 (n/a)</td><td>124.00 (n/a)</td><td>38.60 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (-3.11%)</td><td>0.05 (-5.09%)</td><td>0.05 (-7.77%)</td><td>0.04 (+2.72%)</td><td>0.01 (-16.15%)</td><td>182.50 (-2.67%)</td><td>158.86 (+4.62%)</td><td>157.20 (+8.41%)</td><td>127.60 (+3.24%)</td><td>23.69 (-13.90%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.06 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>187.50 (n/a)</td><td>151.84 (n/a)</td><td>145.00 (n/a)</td><td>123.60 (n/a)</td><td>27.51 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.08 <b>(-22.40%)</b></td><td>0.07 (+7.36%)</td><td>0.07 <b>(+25.84%)</b></td><td>0.06 <b>(+20.57%)</b></td><td>0.01 <b>(-58.66%)</b></td><td>167.80 (-17.05%)</td><td>147.26 (-12.09%)</td><td>143.90 <b>(-20.50%)</b></td><td>124.50 <b>(+28.88%)</b></td><td>19.85 <b>(-53.19%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.07 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>202.30 (n/a)</td><td>167.52 (n/a)</td><td>181.00 (n/a)</td><td>96.60 (n/a)</td><td>42.41 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (-19.14%)</td><td>0.05 (+0.31%)</td><td>0.06 <b>(+28.50%)</b></td><td>0.04 (-7.86%)</td><td>0.01 <b>(-34.97%)</b></td><td>234.00 (+8.53%)</td><td>159.92 (-3.04%)</td><td>141.40 <b>(-22.18%)</b></td><td>134.90 <b>(+23.65%)</b></td><td>41.84 (-8.96%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>215.60 (n/a)</td><td>164.94 (n/a)</td><td>181.70 (n/a)</td><td>109.10 (n/a)</td><td>45.96 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 <b>(-21.67%)</b></td><td>0.05 (-17.25%)</td><td>0.05 (-12.58%)</td><td>0.04 (-19.44%)</td><td>0.01 <b>(-25.40%)</b></td><td>239.90 <b>(+24.11%)</b></td><td>193.34 <b>(+20.45%)</b></td><td>196.90 (+14.41%)</td><td>154.50 <b>(+27.69%)</b></td><td>34.13 (+18.12%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.08 (n/a)</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.01 (n/a)</td><td>193.30 (n/a)</td><td>160.52 (n/a)</td><td>172.10 (n/a)</td><td>121.00 (n/a)</td><td>28.90 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.06 (-0.68%)</td><td>0.05 (+14.98%)</td><td>0.05 (+19.84%)</td><td>0.04 (+16.28%)</td><td>0.01 <b>(-27.69%)</b></td><td>188.70 (-13.99%)</td><td>156.12 (-14.48%)</td><td>151.20 (-16.56%)</td><td>136.70 (+0.74%)</td><td>21.27 <b>(-38.58%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>219.40 (n/a)</td><td>182.56 (n/a)</td><td>181.20 (n/a)</td><td>135.70 (n/a)</td><td>34.63 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (-6.25%)</td><td>0.05 (+5.37%)</td><td>0.05 (-3.27%)</td><td>0.04 (+19.09%)</td><td>0.01 <b>(-26.61%)</b></td><td>230.40 (-16.03%)</td><td>183.64 (-8.37%)</td><td>192.00 (+3.39%)</td><td>136.00 (+6.58%)</td><td>36.84 <b>(-35.22%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.07 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>274.40 (n/a)</td><td>200.42 (n/a)</td><td>185.70 (n/a)</td><td>127.60 (n/a)</td><td>56.86 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.07 (+2.52%)</td><td>0.05 (+3.53%)</td><td>0.04 (+8.11%)</td><td>0.04 (+1.06%)</td><td>0.01 (+0.19%)</td><td>210.80 (-1.03%)</td><td>181.16 (-3.61%)</td><td>190.80 (-7.51%)</td><td>124.00 (-2.52%)</td><td>34.26 (-5.35%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>213.00 (n/a)</td><td>187.94 (n/a)</td><td>206.30 (n/a)</td><td>127.20 (n/a)</td><td>36.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (-0.02%)</td><td>0.04 (-11.73%)</td><td>0.05 (-0.37%)</td><td>0.03 <b>(-40.56%)</b></td><td>0.01 <b>(+267.87%)</b></td><td>344.70 <b>(+68.23%)</b></td><td>227.06 (+19.63%)</td><td>192.60 (+0.36%)</td><td>177.30 (+0.00%)</td><td>68.44 <b>(+540.30%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.00 (n/a)</td><td>204.90 (n/a)</td><td>189.80 (n/a)</td><td>191.90 (n/a)</td><td>177.30 (n/a)</td><td>10.69 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 <b>(-21.49%)</b></td><td>0.04 <b>(-20.40%)</b></td><td>0.04 (-14.71%)</td><td>0.03 <b>(-34.01%)</b></td><td>0.01 (+1.97%)</td><td>292.50 <b>(+51.48%)</b></td><td>215.34 <b>(+27.39%)</b></td><td>194.50 (+17.24%)</td><td>185.80 <b>(+27.35%)</b></td><td>44.44 <b>(+98.52%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.06 (n/a)</td><td>0.05 (n/a)</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.01 (n/a)</td><td>193.10 (n/a)</td><td>169.04 (n/a)</td><td>165.90 (n/a)</td><td>145.90 (n/a)</td><td>22.39 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.05 (-9.73%)</td><td>0.04 (-1.12%)</td><td>0.04 (-16.17%)</td><td>0.03 <b>(+43.63%)</b></td><td>0.00 <b>(-61.41%)</b></td><td>259.60 <b>(-30.36%)</b></td><td>215.08 (-6.50%)</td><td>212.40 (+19.33%)</td><td>192.10 (+10.78%)</td><td>26.84 <b>(-68.95%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.05 (n/a)</td><td>0.04 (n/a)</td><td>0.05 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>372.80 (n/a)</td><td>230.02 (n/a)</td><td>178.00 (n/a)</td><td>173.40 (n/a)</td><td>86.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.04 (+1.08%)</td><td>0.04 (+4.91%)</td><td>0.04 (-2.51%)</td><td>0.03 <b>(+28.41%)</b></td><td>0.00 <b>(-38.75%)</b></td><td>245.70 <b>(-22.12%)</b></td><td>218.08 (-6.50%)</td><td>223.10 (+2.57%)</td><td>194.90 (-1.12%)</td><td>20.94 <b>(-55.36%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.04 (n/a)</td><td>0.03 (n/a)</td><td>0.01 (n/a)</td><td>315.50 (n/a)</td><td>233.24 (n/a)</td><td>217.50 (n/a)</td><td>197.10 (n/a)</td><td>46.91 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (-14.84%)</td><td>0.10 (-7.26%)</td><td>0.09 (+1.41%)</td><td>0.09 (+3.43%)</td><td>0.01 <b>(-56.29%)</b></td><td>188.20 (-3.34%)</td><td>173.46 (+5.59%)</td><td>176.00 (-1.40%)</td><td>152.30 (+17.42%)</td><td>14.72 <b>(-49.50%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>194.70 (n/a)</td><td>164.28 (n/a)</td><td>178.50 (n/a)</td><td>129.70 (n/a)</td><td>29.15 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (+3.52%)</td><td>0.14 (+4.59%)</td><td>0.14 (+9.91%)</td><td>0.12 (+2.84%)</td><td>0.02 (-16.42%)</td><td>204.90 (-2.75%)</td><td>177.02 (-4.88%)</td><td>181.20 (-9.04%)</td><td>153.40 (-3.40%)</td><td>20.11 <b>(-20.13%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>210.70 (n/a)</td><td>186.10 (n/a)</td><td>199.20 (n/a)</td><td>158.80 (n/a)</td><td>25.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (-0.87%)</td><td>0.10 (+0.28%)</td><td>0.10 (+7.71%)</td><td>0.08 (-3.50%)</td><td>0.01 (-9.30%)</td><td>213.80 (+3.64%)</td><td>174.38 (-0.50%)</td><td>165.90 (-7.16%)</td><td>145.70 (+0.90%)</td><td>25.62 (-3.22%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>206.30 (n/a)</td><td>175.26 (n/a)</td><td>178.70 (n/a)</td><td>144.40 (n/a)</td><td>26.47 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (-8.84%)</td><td>0.10 <b>(-20.33%)</b></td><td>0.09 <b>(-31.21%)</b></td><td>0.09 (-16.84%)</td><td>0.02 <b>(+24.58%)</b></td><td>235.60 <b>(+20.27%)</b></td><td>207.68 <b>(+26.99%)</b></td><td>224.40 <b>(+45.34%)</b></td><td>159.10 (+9.72%)</td><td>33.06 <b>(+63.97%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.01 (n/a)</td><td>195.90 (n/a)</td><td>163.54 (n/a)</td><td>154.40 (n/a)</td><td>145.00 (n/a)</td><td>20.17 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 <b>(-25.08%)</b></td><td>0.09 (-13.77%)</td><td>0.10 (-0.99%)</td><td>0.08 (-18.53%)</td><td>0.01 <b>(-34.49%)</b></td><td>213.20 <b>(+22.74%)</b></td><td>176.68 (+15.12%)</td><td>167.40 (+0.97%)</td><td>147.50 <b>(+33.48%)</b></td><td>28.07 (+10.69%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>173.70 (n/a)</td><td>153.48 (n/a)</td><td>165.80 (n/a)</td><td>110.50 (n/a)</td><td>25.36 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (-12.73%)</td><td>0.12 (-12.12%)</td><td>0.11 (-7.41%)</td><td>0.10 (-17.55%)</td><td>0.01 (+1.32%)</td><td>209.00 <b>(+21.30%)</b></td><td>180.28 (+14.25%)</td><td>179.00 (+8.03%)</td><td>152.40 (+14.59%)</td><td>22.83 <b>(+41.67%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>172.30 (n/a)</td><td>157.80 (n/a)</td><td>165.70 (n/a)</td><td>133.00 (n/a)</td><td>16.11 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (-2.46%)</td><td>0.11 (+4.86%)</td><td>0.10 (+4.40%)</td><td>0.07 (-5.81%)</td><td>0.02 (-9.30%)</td><td>222.20 (+6.16%)</td><td>160.20 (-5.07%)</td><td>157.00 (-4.21%)</td><td>126.00 (+2.52%)</td><td>37.22 (-1.71%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>209.30 (n/a)</td><td>168.76 (n/a)</td><td>163.90 (n/a)</td><td>122.90 (n/a)</td><td>37.87 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.17 <b>(+45.70%)</b></td><td>0.12 (+3.29%)</td><td>0.10 (-11.30%)</td><td>0.07 <b>(-28.56%)</b></td><td>0.04 <b>(+711.64%)</b></td><td>248.60 <b>(+39.98%)</b></td><td>172.88 (+4.69%)</td><td>183.60 (+12.78%)</td><td>110.60 <b>(-31.35%)</b></td><td>53.54 <b>(+661.89%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.00 (n/a)</td><td>177.60 (n/a)</td><td>165.14 (n/a)</td><td>162.80 (n/a)</td><td>161.10 (n/a)</td><td>7.03 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (+11.75%)</td><td>0.10 (+5.32%)</td><td>0.10 (-1.27%)</td><td>0.08 (+6.02%)</td><td>0.02 <b>(+23.43%)</b></td><td>203.30 (-5.71%)</td><td>166.34 (-4.52%)</td><td>171.60 (+1.30%)</td><td>120.90 (-10.51%)</td><td>29.60 (+0.86%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.08 (n/a)</td><td>0.02 (n/a)</td><td>215.60 (n/a)</td><td>174.22 (n/a)</td><td>169.40 (n/a)</td><td>135.10 (n/a)</td><td>29.35 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (+3.06%)</td><td>0.11 (-15.11%)</td><td>0.09 <b>(-34.84%)</b></td><td>0.08 (-18.32%)</td><td>0.03 <b>(+26.34%)</b></td><td>222.50 <b>(+22.39%)</b></td><td>177.00 <b>(+21.43%)</b></td><td>195.60 <b>(+53.53%)</b></td><td>114.00 (-2.98%)</td><td>47.51 <b>(+48.02%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>181.80 (n/a)</td><td>145.76 (n/a)</td><td>127.40 (n/a)</td><td>117.50 (n/a)</td><td>32.10 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 <b>(-29.00%)</b></td><td>0.08 (-7.58%)</td><td>0.08 (+0.09%)</td><td>0.07 <b>(+39.03%)</b></td><td>0.01 <b>(-65.87%)</b></td><td>223.10 <b>(-28.08%)</b></td><td>208.66 (-0.83%)</td><td>218.20 (-0.09%)</td><td>164.50 <b>(+40.84%)</b></td><td>24.79 <b>(-64.54%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.05 (n/a)</td><td>0.03 (n/a)</td><td>310.20 (n/a)</td><td>210.40 (n/a)</td><td>218.40 (n/a)</td><td>116.80 (n/a)</td><td>69.89 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (-13.48%)</td><td>0.09 (-6.02%)</td><td>0.08 <b>(-22.08%)</b></td><td>0.08 <b>(+36.96%)</b></td><td>0.01 <b>(-51.84%)</b></td><td>225.10 <b>(-26.99%)</b></td><td>199.66 (+0.21%)</td><td>213.10 <b>(+28.37%)</b></td><td>162.80 (+15.62%)</td><td>26.38 <b>(-60.50%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.10 (n/a)</td><td>0.06 (n/a)</td><td>0.03 (n/a)</td><td>308.30 (n/a)</td><td>199.24 (n/a)</td><td>166.00 (n/a)</td><td>140.80 (n/a)</td><td>66.78 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.11 (-10.89%)</td><td>0.10 (+0.58%)</td><td>0.10 (-2.99%)</td><td>0.08 (+9.74%)</td><td>0.01 <b>(-43.01%)</b></td><td>205.60 (-8.87%)</td><td>167.26 (-3.32%)</td><td>164.00 (+3.14%)</td><td>145.70 (+12.16%)</td><td>23.39 <b>(-41.91%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>225.60 (n/a)</td><td>173.00 (n/a)</td><td>159.00 (n/a)</td><td>129.90 (n/a)</td><td>40.26 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 <b>(+32.96%)</b></td><td>0.10 (+7.01%)</td><td>0.10 (+5.23%)</td><td>0.08 (+2.07%)</td><td>0.03 <b>(+119.47%)</b></td><td>227.90 (-2.02%)</td><td>184.94 (-2.85%)</td><td>180.50 (-4.95%)</td><td>117.70 <b>(-24.74%)</b></td><td>43.63 <b>(+58.04%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.09 (n/a)</td><td>0.09 (n/a)</td><td>0.07 (n/a)</td><td>0.01 (n/a)</td><td>232.60 (n/a)</td><td>190.36 (n/a)</td><td>189.90 (n/a)</td><td>156.40 (n/a)</td><td>27.61 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.10 (-15.16%)</td><td>0.08 (-1.22%)</td><td>0.08 (+9.06%)</td><td>0.08 (+11.09%)</td><td>0.01 <b>(-52.01%)</b></td><td>215.20 (-10.00%)</td><td>196.42 (-1.59%)</td><td>200.20 (-8.29%)</td><td>164.60 (+17.91%)</td><td>20.66 <b>(-48.52%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.08 (n/a)</td><td>0.07 (n/a)</td><td>0.02 (n/a)</td><td>239.10 (n/a)</td><td>199.60 (n/a)</td><td>218.30 (n/a)</td><td>139.60 (n/a)</td><td>40.14 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (+9.14%)</td><td>0.20 (+18.72%)</td><td>0.21 (+19.47%)</td><td>0.17 <b>(+85.55%)</b></td><td>0.02 <b>(-46.36%)</b></td><td>193.30 <b>(-46.11%)</b></td><td>168.20 <b>(-21.56%)</b></td><td>155.80 (-16.33%)</td><td>150.60 (-8.34%)</td><td>21.00 <b>(-74.32%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.18 (n/a)</td><td>0.09 (n/a)</td><td>0.04 (n/a)</td><td>358.70 (n/a)</td><td>214.42 (n/a)</td><td>186.20 (n/a)</td><td>164.30 (n/a)</td><td>81.77 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.23 (+7.30%)</td><td>0.19 (+0.98%)</td><td>0.18 (-4.41%)</td><td>0.16 (+0.06%)</td><td>0.03 <b>(+31.68%)</b></td><td>206.50 (-0.05%)</td><td>174.70 (-0.47%)</td><td>179.70 (+4.60%)</td><td>145.10 (-6.81%)</td><td>23.08 <b>(+20.21%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>206.60 (n/a)</td><td>175.52 (n/a)</td><td>171.80 (n/a)</td><td>155.70 (n/a)</td><td>19.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.40 <b>(+29.72%)</b></td><td>0.27 (+11.50%)</td><td>0.26 (+5.70%)</td><td>0.19 (+15.07%)</td><td>0.08 <b>(+40.34%)</b></td><td>218.40 (-13.09%)</td><td>160.40 (-8.83%)</td><td>154.60 (-5.39%)</td><td>102.40 <b>(-22.89%)</b></td><td>45.59 (-5.32%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>251.30 (n/a)</td><td>175.94 (n/a)</td><td>163.40 (n/a)</td><td>132.80 (n/a)</td><td>48.15 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.23 (-5.48%)</td><td>0.20 (+1.49%)</td><td>0.19 (+4.48%)</td><td>0.18 (+3.51%)</td><td>0.02 <b>(-29.68%)</b></td><td>185.50 (-3.39%)</td><td>168.58 (-2.19%)</td><td>170.10 (-4.28%)</td><td>144.00 (+5.80%)</td><td>16.11 <b>(-27.68%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 (n/a)</td><td>0.19 (n/a)</td><td>0.18 (n/a)</td><td>0.17 (n/a)</td><td>0.03 (n/a)</td><td>192.00 (n/a)</td><td>172.36 (n/a)</td><td>177.70 (n/a)</td><td>136.10 (n/a)</td><td>22.28 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.29 (-8.67%)</td><td>0.22 (-15.43%)</td><td>0.22 (-15.56%)</td><td>0.17 <b>(-23.62%)</b></td><td>0.04 <b>(+35.58%)</b></td><td>235.20 <b>(+30.96%)</b></td><td>188.30 <b>(+20.29%)</b></td><td>185.70 (+18.43%)</td><td>143.60 (+9.53%)</td><td>34.50 <b>(+95.83%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.23 (n/a)</td><td>0.03 (n/a)</td><td>179.60 (n/a)</td><td>156.54 (n/a)</td><td>156.80 (n/a)</td><td>131.10 (n/a)</td><td>17.62 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (+1.32%)</td><td>0.22 (+9.19%)</td><td>0.21 (+11.45%)</td><td>0.19 <b>(+22.30%)</b></td><td>0.03 <b>(-21.88%)</b></td><td>169.60 (-18.23%)</td><td>149.30 (-9.76%)</td><td>154.30 (-10.24%)</td><td>127.50 (-1.32%)</td><td>20.00 <b>(-36.59%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>207.40 (n/a)</td><td>165.44 (n/a)</td><td>171.90 (n/a)</td><td>129.20 (n/a)</td><td>31.54 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.25 (-9.70%)</td><td>0.20 (-11.05%)</td><td>0.21 (-11.74%)</td><td>0.15 (-6.76%)</td><td>0.05 (-2.53%)</td><td>251.80 (+7.24%)</td><td>188.44 (+12.91%)</td><td>173.00 (+13.29%)</td><td>146.20 (+10.76%)</td><td>46.76 (+12.66%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.16 (n/a)</td><td>0.05 (n/a)</td><td>234.80 (n/a)</td><td>166.90 (n/a)</td><td>152.70 (n/a)</td><td>132.00 (n/a)</td><td>41.51 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.29 (+16.47%)</td><td>0.23 <b>(+22.59%)</b></td><td>0.23 <b>(+31.03%)</b></td><td>0.17 (+8.97%)</td><td>0.04 (+16.09%)</td><td>188.20 (-8.24%)</td><td>148.44 (-18.28%)</td><td>142.00 <b>(-23.70%)</b></td><td>113.50 (-14.15%)</td><td>27.18 (-5.84%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.04 (n/a)</td><td>205.10 (n/a)</td><td>181.64 (n/a)</td><td>186.10 (n/a)</td><td>132.20 (n/a)</td><td>28.87 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.26 (+6.48%)</td><td>0.20 (-11.77%)</td><td>0.21 (-10.80%)</td><td>0.12 <b>(-32.18%)</b></td><td>0.05 <b>(+88.43%)</b></td><td>305.60 <b>(+47.49%)</b></td><td>197.70 (+19.54%)</td><td>175.90 (+12.11%)</td><td>142.30 (-6.07%)</td><td>63.69 <b>(+169.86%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>207.20 (n/a)</td><td>165.38 (n/a)</td><td>156.90 (n/a)</td><td>151.50 (n/a)</td><td>23.60 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.25 <b>(+20.40%)</b></td><td>0.19 (+11.37%)</td><td>0.20 (+14.48%)</td><td>0.14 (-10.14%)</td><td>0.04 <b>(+83.33%)</b></td><td>238.20 (+11.31%)</td><td>174.34 (-8.05%)</td><td>167.30 (-12.68%)</td><td>133.20 (-16.91%)</td><td>38.59 <b>(+74.97%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.17 (n/a)</td><td>0.15 (n/a)</td><td>0.02 (n/a)</td><td>214.00 (n/a)</td><td>189.60 (n/a)</td><td>191.60 (n/a)</td><td>160.30 (n/a)</td><td>22.05 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (-7.91%)</td><td>0.17 (-14.30%)</td><td>0.15 <b>(-23.70%)</b></td><td>0.13 (-18.03%)</td><td>0.04 <b>(+21.76%)</b></td><td>261.80 <b>(+21.99%)</b></td><td>213.62 (+18.68%)</td><td>226.00 <b>(+31.01%)</b></td><td>161.40 (+8.54%)</td><td>43.94 <b>(+57.64%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>214.60 (n/a)</td><td>180.00 (n/a)</td><td>172.50 (n/a)</td><td>148.70 (n/a)</td><td>27.87 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (-10.43%)</td><td>0.18 (+0.29%)</td><td>0.19 <b>(+28.82%)</b></td><td>0.09 (-9.76%)</td><td>0.05 <b>(-20.85%)</b></td><td>345.80 (+10.83%)</td><td>203.42 (-1.71%)</td><td>168.20 <b>(-22.38%)</b></td><td>145.80 (+11.64%)</td><td>82.11 (+8.60%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.06 (n/a)</td><td>312.00 (n/a)</td><td>206.96 (n/a)</td><td>216.70 (n/a)</td><td>130.60 (n/a)</td><td>75.61 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 (-9.89%)</td><td>0.18 (-14.17%)</td><td>0.17 <b>(-20.92%)</b></td><td>0.15 (-5.41%)</td><td>0.02 <b>(-29.02%)</b></td><td>225.20 (+5.73%)</td><td>200.16 (+15.86%)</td><td>203.80 <b>(+26.43%)</b></td><td>172.80 (+10.98%)</td><td>19.70 (-17.62%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.22 (n/a)</td><td>0.16 (n/a)</td><td>0.03 (n/a)</td><td>213.00 (n/a)</td><td>172.76 (n/a)</td><td>161.20 (n/a)</td><td>155.70 (n/a)</td><td>23.91 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (-2.38%)</td><td>0.15 (-7.10%)</td><td>0.15 (-4.37%)</td><td>0.12 (-14.50%)</td><td>0.02 <b>(+20.08%)</b></td><td>265.00 (+16.95%)</td><td>223.94 (+8.28%)</td><td>226.00 (+4.58%)</td><td>181.70 (+2.42%)</td><td>29.60 <b>(+41.91%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.18 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.02 (n/a)</td><td>226.60 (n/a)</td><td>206.82 (n/a)</td><td>216.10 (n/a)</td><td>177.40 (n/a)</td><td>20.86 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 <b>(-24.34%)</b></td><td>0.12 (-17.20%)</td><td>0.12 (-11.80%)</td><td>0.11 (-7.24%)</td><td>0.01 <b>(-71.69%)</b></td><td>185.40 (+7.79%)</td><td>171.92 (+18.66%)</td><td>172.50 (+13.41%)</td><td>158.90 <b>(+32.20%)</b></td><td>9.42 <b>(-58.48%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>172.00 (n/a)</td><td>144.88 (n/a)</td><td>152.10 (n/a)</td><td>120.20 (n/a)</td><td>22.69 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (-7.28%)</td><td>0.12 (-7.22%)</td><td>0.11 (-5.47%)</td><td>0.11 (-7.76%)</td><td>0.02 (-8.82%)</td><td>191.30 (+8.45%)</td><td>171.06 (+7.71%)</td><td>180.40 (+5.81%)</td><td>130.30 (+7.86%)</td><td>23.74 (+4.98%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>176.40 (n/a)</td><td>158.82 (n/a)</td><td>170.50 (n/a)</td><td>120.80 (n/a)</td><td>22.61 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.17 (+10.43%)</td><td>0.12 (+2.93%)</td><td>0.11 (-7.29%)</td><td>0.09 (+13.34%)</td><td>0.03 (-3.71%)</td><td>218.90 (-11.77%)</td><td>181.76 (-4.65%)</td><td>184.10 (+7.91%)</td><td>122.40 (-9.47%)</td><td>37.70 <b>(-28.60%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (n/a)</td><td>0.11 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>248.10 (n/a)</td><td>190.62 (n/a)</td><td>170.60 (n/a)</td><td>135.20 (n/a)</td><td>52.80 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.16 (+2.60%)</td><td>0.12 (-1.60%)</td><td>0.10 (-4.75%)</td><td>0.09 (+19.31%)</td><td>0.03 (-19.08%)</td><td>215.90 (-16.19%)</td><td>183.38 (-1.47%)</td><td>200.70 (+5.02%)</td><td>125.70 (-2.56%)</td><td>38.95 <b>(-29.74%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.16 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.04 (n/a)</td><td>257.60 (n/a)</td><td>186.12 (n/a)</td><td>191.10 (n/a)</td><td>129.00 (n/a)</td><td>55.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (-13.71%)</td><td>0.13 (+1.14%)</td><td>0.13 (+17.79%)</td><td>0.11 (+12.15%)</td><td>0.01 <b>(-57.71%)</b></td><td>188.60 (-10.83%)</td><td>160.58 (-4.58%)</td><td>157.10 (-15.08%)</td><td>141.40 (+15.90%)</td><td>17.22 <b>(-54.67%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>211.50 (n/a)</td><td>168.28 (n/a)</td><td>185.00 (n/a)</td><td>122.00 (n/a)</td><td>37.98 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (-6.43%)</td><td>0.12 (+1.62%)</td><td>0.13 (+4.41%)</td><td>0.09 (-4.80%)</td><td>0.02 (-4.36%)</td><td>229.70 (+5.03%)</td><td>177.16 (-1.53%)</td><td>162.30 (-4.25%)</td><td>151.20 (+6.86%)</td><td>32.28 (+7.08%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>218.70 (n/a)</td><td>179.92 (n/a)</td><td>169.50 (n/a)</td><td>141.50 (n/a)</td><td>30.15 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 (-1.74%)</td><td>0.12 (-2.15%)</td><td>0.13 (+16.28%)</td><td>0.09 (-17.62%)</td><td>0.03 <b>(+62.17%)</b></td><td>239.00 <b>(+21.38%)</b></td><td>182.76 (+5.47%)</td><td>157.10 (-13.96%)</td><td>144.50 (+1.83%)</td><td>44.87 <b>(+102.25%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>196.90 (n/a)</td><td>173.28 (n/a)</td><td>182.60 (n/a)</td><td>141.90 (n/a)</td><td>22.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (-14.39%)</td><td>0.11 (-4.59%)</td><td>0.10 (-5.41%)</td><td>0.09 (+15.32%)</td><td>0.02 <b>(-36.45%)</b></td><td>220.00 (-13.28%)</td><td>189.84 (+2.17%)</td><td>197.30 (+5.68%)</td><td>156.50 (+16.88%)</td><td>28.12 <b>(-36.54%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>253.70 (n/a)</td><td>185.80 (n/a)</td><td>186.70 (n/a)</td><td>133.90 (n/a)</td><td>44.31 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.17 (-8.06%)</td><td>0.14 (-1.93%)</td><td>0.13 (-3.00%)</td><td>0.12 (+0.62%)</td><td>0.02 (-14.02%)</td><td>208.80 (-0.62%)</td><td>179.86 (+1.56%)</td><td>190.20 (+3.09%)</td><td>148.90 (+8.77%)</td><td>25.79 (-6.81%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.18 (n/a)</td><td>0.14 (n/a)</td><td>0.13 (n/a)</td><td>0.12 (n/a)</td><td>0.02 (n/a)</td><td>210.10 (n/a)</td><td>177.10 (n/a)</td><td>184.50 (n/a)</td><td>136.90 (n/a)</td><td>27.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 (+15.70%)</td><td>0.15 (+6.05%)</td><td>0.13 (-16.05%)</td><td>0.11 (+11.45%)</td><td>0.04 (+17.34%)</td><td>215.00 (-10.27%)</td><td>168.32 (-5.49%)</td><td>184.60 (+19.10%)</td><td>121.90 (-13.61%)</td><td>40.74 (-10.13%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.17 (n/a)</td><td>0.14 (n/a)</td><td>0.16 (n/a)</td><td>0.10 (n/a)</td><td>0.03 (n/a)</td><td>239.60 (n/a)</td><td>178.10 (n/a)</td><td>155.00 (n/a)</td><td>141.10 (n/a)</td><td>45.33 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 (+16.94%)</td><td>0.15 (-1.58%)</td><td>0.14 (-12.30%)</td><td>0.12 (+7.53%)</td><td>0.04 (+18.83%)</td><td>204.70 (-7.00%)</td><td>172.56 (+1.90%)</td><td>177.60 (+13.99%)</td><td>110.10 (-14.52%)</td><td>37.26 (-9.65%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (n/a)</td><td>0.15 (n/a)</td><td>0.16 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>220.10 (n/a)</td><td>169.34 (n/a)</td><td>155.80 (n/a)</td><td>128.80 (n/a)</td><td>41.24 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.21 (+1.81%)</td><td>0.15 (-10.25%)</td><td>0.14 (-12.16%)</td><td>0.13 (-8.11%)</td><td>0.03 (+5.94%)</td><td>194.30 (+8.79%)</td><td>165.72 (+11.88%)</td><td>173.30 (+13.86%)</td><td>118.20 (-1.75%)</td><td>28.35 (+10.40%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.14 (n/a)</td><td>0.03 (n/a)</td><td>178.60 (n/a)</td><td>148.12 (n/a)</td><td>152.20 (n/a)</td><td>120.30 (n/a)</td><td>25.68 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.19 (-13.00%)</td><td>0.16 (-5.71%)</td><td>0.16 (+4.39%)</td><td>0.11 (-11.15%)</td><td>0.03 (-13.03%)</td><td>218.50 (+12.51%)</td><td>163.26 (+6.08%)</td><td>151.50 (-4.24%)</td><td>127.10 (+14.92%)</td><td>36.35 (+15.36%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.04 (n/a)</td><td>194.20 (n/a)</td><td>153.90 (n/a)</td><td>158.20 (n/a)</td><td>110.60 (n/a)</td><td>31.51 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 <b>(-29.81%)</b></td><td>0.13 (-15.79%)</td><td>0.13 (-4.08%)</td><td>0.11 (-2.19%)</td><td>0.02 <b>(-59.85%)</b></td><td>230.30 (+2.22%)</td><td>193.18 (+13.25%)</td><td>182.10 (+4.24%)</td><td>166.50 <b>(+42.55%)</b></td><td>27.34 <b>(-40.96%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.21 (n/a)</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.04 (n/a)</td><td>225.30 (n/a)</td><td>170.58 (n/a)</td><td>174.70 (n/a)</td><td>116.80 (n/a)</td><td>46.30 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.17 (-12.02%)</td><td>0.13 (-15.96%)</td><td>0.13 (-19.04%)</td><td>0.10 <b>(-24.50%)</b></td><td>0.03 <b>(+27.44%)</b></td><td>245.10 <b>(+32.41%)</b></td><td>189.92 <b>(+21.14%)</b></td><td>191.60 <b>(+23.53%)</b></td><td>148.10 (+13.66%)</td><td>37.83 <b>(+90.91%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.19 (n/a)</td><td>0.16 (n/a)</td><td>0.16 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>185.10 (n/a)</td><td>156.78 (n/a)</td><td>155.10 (n/a)</td><td>130.30 (n/a)</td><td>19.82 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.14 <b>(-28.58%)</b></td><td>0.13 (-16.33%)</td><td>0.13 (-15.24%)</td><td>0.12 (-7.71%)</td><td>0.01 <b>(-63.36%)</b></td><td>206.60 (+8.34%)</td><td>189.98 (+17.82%)</td><td>192.80 (+17.99%)</td><td>176.00 <b>(+40.02%)</b></td><td>13.08 <b>(-43.50%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.15 (n/a)</td><td>0.13 (n/a)</td><td>0.02 (n/a)</td><td>190.70 (n/a)</td><td>161.24 (n/a)</td><td>163.40 (n/a)</td><td>125.70 (n/a)</td><td>23.15 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.15 (+4.93%)</td><td>0.11 (-10.75%)</td><td>0.10 (-12.01%)</td><td>0.08 <b>(-22.53%)</b></td><td>0.02 <b>(+101.90%)</b></td><td>222.30 <b>(+29.09%)</b></td><td>178.36 (+15.35%)</td><td>177.60 (+13.70%)</td><td>125.60 (-4.70%)</td><td>35.84 <b>(+147.40%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>172.20 (n/a)</td><td>154.62 (n/a)</td><td>156.20 (n/a)</td><td>131.80 (n/a)</td><td>14.49 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (-17.85%)</td><td>0.10 <b>(-25.13%)</b></td><td>0.11 (-18.98%)</td><td>0.07 <b>(-40.15%)</b></td><td>0.02 <b>(+67.28%)</b></td><td>253.80 <b>(+67.08%)</b></td><td>189.32 <b>(+38.21%)</b></td><td>167.90 <b>(+23.46%)</b></td><td>145.10 <b>(+21.73%)</b></td><td>44.75 <b>(+243.62%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (n/a)</td><td>0.14 (n/a)</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.01 (n/a)</td><td>151.90 (n/a)</td><td>136.98 (n/a)</td><td>136.00 (n/a)</td><td>119.20 (n/a)</td><td>13.02 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (-12.62%)</td><td>0.10 (-5.50%)</td><td>0.10 (-0.69%)</td><td>0.07 (-10.27%)</td><td>0.02 (-16.20%)</td><td>280.60 (+11.44%)</td><td>197.02 (+5.26%)</td><td>193.00 (+0.68%)</td><td>150.30 (+14.47%)</td><td>52.10 (+7.77%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.07 (n/a)</td><td>0.03 (n/a)</td><td>251.80 (n/a)</td><td>187.18 (n/a)</td><td>191.70 (n/a)</td><td>131.30 (n/a)</td><td>48.34 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.18 (+17.22%)</td><td>0.11 (-10.74%)</td><td>0.10 (-19.39%)</td><td>0.07 <b>(-23.88%)</b></td><td>0.04 <b>(+67.94%)</b></td><td>260.00 <b>(+31.38%)</b></td><td>184.00 (+18.30%)</td><td>185.80 <b>(+24.11%)</b></td><td>105.30 (-14.67%)</td><td>54.72 <b>(+78.35%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.15 (n/a)</td><td>0.12 (n/a)</td><td>0.12 (n/a)</td><td>0.09 (n/a)</td><td>0.02 (n/a)</td><td>197.90 (n/a)</td><td>155.54 (n/a)</td><td>149.70 (n/a)</td><td>123.40 (n/a)</td><td>30.68 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (-10.17%)</td><td>0.11 (-13.14%)</td><td>0.10 (-18.13%)</td><td>0.09 (-17.14%)</td><td>0.02 <b>(+36.03%)</b></td><td>207.20 <b>(+20.68%)</b></td><td>175.76 (+16.38%)</td><td>178.50 <b>(+22.18%)</b></td><td>148.20 (+11.26%)</td><td>26.69 <b>(+77.82%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (n/a)</td><td>0.12 (n/a)</td><td>0.13 (n/a)</td><td>0.11 (n/a)</td><td>0.01 (n/a)</td><td>171.70 (n/a)</td><td>151.02 (n/a)</td><td>146.10 (n/a)</td><td>133.20 (n/a)</td><td>15.01 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (-12.57%)</td><td>0.10 (-0.53%)</td><td>0.11 (-5.48%)</td><td>0.08 (+8.38%)</td><td>0.01 <b>(-45.12%)</b></td><td>224.20 (-7.74%)</td><td>180.36 (-2.87%)</td><td>166.40 (+5.79%)</td><td>159.80 (+14.39%)</td><td>26.79 <b>(-43.84%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.12 (n/a)</td><td>0.08 (n/a)</td><td>0.03 (n/a)</td><td>243.00 (n/a)</td><td>185.68 (n/a)</td><td>157.30 (n/a)</td><td>139.70 (n/a)</td><td>47.71 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.12 (+1.15%)</td><td>0.09 (-10.76%)</td><td>0.09 (-18.52%)</td><td>0.08 (+1.60%)</td><td>0.01 (-4.90%)</td><td>220.20 (-1.56%)</td><td>198.80 (+11.82%)</td><td>203.50 <b>(+22.74%)</b></td><td>159.10 (-1.12%)</td><td>23.81 (-10.01%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.08 (n/a)</td><td>0.01 (n/a)</td><td>223.70 (n/a)</td><td>177.78 (n/a)</td><td>165.80 (n/a)</td><td>160.90 (n/a)</td><td>26.46 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (-8.85%)</td><td>0.11 (-6.69%)</td><td>0.11 (+1.01%)</td><td>0.07 <b>(-27.83%)</b></td><td>0.02 <b>(+31.34%)</b></td><td>246.30 <b>(+38.60%)</b></td><td>178.16 (+9.56%)</td><td>167.40 (-1.01%)</td><td>142.10 (+9.65%)</td><td>40.53 <b>(+110.35%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.14 (n/a)</td><td>0.11 (n/a)</td><td>0.11 (n/a)</td><td>0.10 (n/a)</td><td>0.02 (n/a)</td><td>177.70 (n/a)</td><td>162.62 (n/a)</td><td>169.10 (n/a)</td><td>129.60 (n/a)</td><td>19.27 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.71 <b>(+21.58%)</b></td><td>0.55 (-2.30%)</td><td>0.52 (-7.30%)</td><td>0.47 (-11.26%)</td><td>0.10 <b>(+306.63%)</b></td><td>208.20 (+12.72%)</td><td>184.06 (+4.39%)</td><td>190.70 (+7.86%)</td><td>137.80 (-17.78%)</td><td>27.30 <b>(+266.37%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.59 (n/a)</td><td>0.56 (n/a)</td><td>0.56 (n/a)</td><td>0.53 (n/a)</td><td>0.02 (n/a)</td><td>184.70 (n/a)</td><td>176.32 (n/a)</td><td>176.80 (n/a)</td><td>167.60 (n/a)</td><td>7.45 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.76 (-5.75%)</td><td>0.52 <b>(-30.04%)</b></td><td>0.48 <b>(-36.01%)</b></td><td>0.40 <b>(-41.38%)</b></td><td>0.14 <b>(+227.65%)</b></td><td>243.70 <b>(+70.54%)</b></td><td>197.80 <b>(+49.80%)</b></td><td>205.70 <b>(+56.31%)</b></td><td>128.80 (+6.10%)</td><td>44.52 <b>(+476.89%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.81 (n/a)</td><td>0.75 (n/a)</td><td>0.75 (n/a)</td><td>0.69 (n/a)</td><td>0.04 (n/a)</td><td>142.90 (n/a)</td><td>132.04 (n/a)</td><td>131.60 (n/a)</td><td>121.40 (n/a)</td><td>7.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.81 (-6.26%)</td><td>0.58 (-18.19%)</td><td>0.51 <b>(-25.41%)</b></td><td>0.44 <b>(-23.33%)</b></td><td>0.14 <b>(+38.40%)</b></td><td>221.50 <b>(+30.45%)</b></td><td>177.42 <b>(+25.47%)</b></td><td>191.00 <b>(+34.04%)</b></td><td>120.80 (+6.71%)</td><td>37.87 <b>(+88.73%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.87 (n/a)</td><td>0.71 (n/a)</td><td>0.69 (n/a)</td><td>0.58 (n/a)</td><td>0.10 (n/a)</td><td>169.80 (n/a)</td><td>141.40 (n/a)</td><td>142.50 (n/a)</td><td>113.20 (n/a)</td><td>20.07 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.59 <b>(-26.88%)</b></td><td>0.51 <b>(-21.00%)</b></td><td>0.52 <b>(-26.94%)</b></td><td>0.44 (-3.90%)</td><td>0.06 <b>(-60.39%)</b></td><td>223.40 (+4.05%)</td><td>195.56 <b>(+21.57%)</b></td><td>187.80 <b>(+36.88%)</b></td><td>166.50 <b>(+36.70%)</b></td><td>23.81 <b>(-43.68%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.81 (n/a)</td><td>0.64 (n/a)</td><td>0.72 (n/a)</td><td>0.46 (n/a)</td><td>0.16 (n/a)</td><td>214.70 (n/a)</td><td>160.86 (n/a)</td><td>137.20 (n/a)</td><td>121.80 (n/a)</td><td>42.28 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.63 (-5.63%)</td><td>0.50 (+2.39%)</td><td>0.48 (-1.29%)</td><td>0.35 <b>(+81.94%)</b></td><td>0.12 <b>(-38.28%)</b></td><td>212.10 <b>(-45.04%)</b></td><td>154.44 (-16.36%)</td><td>154.60 (+1.31%)</td><td>116.70 (+5.99%)</td><td>38.30 <b>(-66.54%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.67 (n/a)</td><td>0.49 (n/a)</td><td>0.48 (n/a)</td><td>0.19 (n/a)</td><td>0.19 (n/a)</td><td>385.90 (n/a)</td><td>184.64 (n/a)</td><td>152.60 (n/a)</td><td>110.10 (n/a)</td><td>114.46 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.55 (-1.78%)</td><td>0.42 (-9.00%)</td><td>0.42 (-8.56%)</td><td>0.28 (-18.68%)</td><td>0.10 (+0.95%)</td><td>259.40 <b>(+23.00%)</b></td><td>184.10 (+11.12%)</td><td>174.80 (+9.32%)</td><td>132.90 (+1.84%)</td><td>47.72 <b>(+31.20%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.56 (n/a)</td><td>0.46 (n/a)</td><td>0.46 (n/a)</td><td>0.35 (n/a)</td><td>0.10 (n/a)</td><td>210.90 (n/a)</td><td>165.68 (n/a)</td><td>159.90 (n/a)</td><td>130.50 (n/a)</td><td>36.37 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.57 (-5.04%)</td><td>0.48 (+1.61%)</td><td>0.44 (+6.12%)</td><td>0.39 (+8.96%)</td><td>0.09 (-12.36%)</td><td>187.00 (-8.24%)</td><td>159.36 (-2.48%)</td><td>167.90 (-5.78%)</td><td>128.70 (+5.32%)</td><td>28.89 (-15.31%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.60 (n/a)</td><td>0.47 (n/a)</td><td>0.41 (n/a)</td><td>0.36 (n/a)</td><td>0.10 (n/a)</td><td>203.80 (n/a)</td><td>163.42 (n/a)</td><td>178.20 (n/a)</td><td>122.20 (n/a)</td><td>34.11 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.52 (-16.18%)</td><td>0.41 (+2.10%)</td><td>0.40 (+10.20%)</td><td>0.34 <b>(+24.34%)</b></td><td>0.07 <b>(-47.15%)</b></td><td>215.00 (-19.57%)</td><td>184.16 (-7.02%)</td><td>184.30 (-9.26%)</td><td>140.60 (+19.35%)</td><td>28.58 <b>(-47.52%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.63 (n/a)</td><td>0.40 (n/a)</td><td>0.36 (n/a)</td><td>0.28 (n/a)</td><td>0.13 (n/a)</td><td>267.30 (n/a)</td><td>198.06 (n/a)</td><td>203.10 (n/a)</td><td>117.80 (n/a)</td><td>54.47 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 <b>(-20.89%)</b></td><td>0.22 (-13.05%)</td><td>0.20 <b>(-20.30%)</b></td><td>0.20 <b>(+23.23%)</b></td><td>0.03 <b>(-55.14%)</b></td><td>186.00 (-18.85%)</td><td>173.32 (+9.79%)</td><td>181.10 <b>(+25.42%)</b></td><td>138.30 <b>(+26.42%)</b></td><td>19.79 <b>(-55.79%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.34 (n/a)</td><td>0.25 (n/a)</td><td>0.26 (n/a)</td><td>0.16 (n/a)</td><td>0.06 (n/a)</td><td>229.20 (n/a)</td><td>157.86 (n/a)</td><td>144.40 (n/a)</td><td>109.40 (n/a)</td><td>44.76 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 (-0.43%)</td><td>0.22 (+2.94%)</td><td>0.22 (+9.54%)</td><td>0.19 (+9.84%)</td><td>0.03 <b>(-27.47%)</b></td><td>195.30 (-8.95%)</td><td>167.02 (-4.51%)</td><td>166.00 (-8.74%)</td><td>133.70 (+0.45%)</td><td>22.96 <b>(-33.89%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>214.50 (n/a)</td><td>174.90 (n/a)</td><td>181.90 (n/a)</td><td>133.10 (n/a)</td><td>34.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.31 (+4.62%)</td><td>0.23 (-1.91%)</td><td>0.22 (-2.42%)</td><td>0.16 (-17.13%)</td><td>0.06 <b>(+43.79%)</b></td><td>235.90 <b>(+20.66%)</b></td><td>171.90 (+4.88%)</td><td>170.00 (+2.47%)</td><td>120.30 (-4.45%)</td><td>42.89 <b>(+70.18%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>195.50 (n/a)</td><td>163.90 (n/a)</td><td>165.90 (n/a)</td><td>125.90 (n/a)</td><td>25.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.28 (+3.91%)</td><td>0.23 (+3.71%)</td><td>0.25 (+13.67%)</td><td>0.18 (-10.98%)</td><td>0.04 <b>(+32.40%)</b></td><td>206.40 (+12.30%)</td><td>160.84 (-2.47%)</td><td>147.80 (-12.02%)</td><td>131.30 (-3.74%)</td><td>29.32 <b>(+42.99%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>183.80 (n/a)</td><td>164.92 (n/a)</td><td>168.00 (n/a)</td><td>136.40 (n/a)</td><td>20.50 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.32 (+13.18%)</td><td>0.21 (-7.95%)</td><td>0.19 (-15.42%)</td><td>0.16 (-4.89%)</td><td>0.06 <b>(+49.81%)</b></td><td>226.00 (+5.17%)</td><td>187.88 (+11.81%)</td><td>197.10 (+18.24%)</td><td>114.40 (-11.59%)</td><td>43.18 <b>(+32.12%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.17 (n/a)</td><td>0.04 (n/a)</td><td>214.90 (n/a)</td><td>168.04 (n/a)</td><td>166.70 (n/a)</td><td>129.40 (n/a)</td><td>32.68 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (-7.94%)</td><td>0.22 (+17.59%)</td><td>0.21 <b>(+23.86%)</b></td><td>0.18 <b>(+54.14%)</b></td><td>0.04 <b>(-42.28%)</b></td><td>204.30 <b>(-35.14%)</b></td><td>168.88 <b>(-20.85%)</b></td><td>173.80 (-19.28%)</td><td>136.40 (+8.60%)</td><td>29.00 <b>(-59.47%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (n/a)</td><td>0.19 (n/a)</td><td>0.17 (n/a)</td><td>0.12 (n/a)</td><td>0.07 (n/a)</td><td>315.00 (n/a)</td><td>213.36 (n/a)</td><td>215.30 (n/a)</td><td>125.60 (n/a)</td><td>71.55 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 <b>(-33.63%)</b></td><td>0.18 <b>(-23.85%)</b></td><td>0.18 <b>(-21.69%)</b></td><td>0.13 <b>(-32.02%)</b></td><td>0.03 <b>(-38.24%)</b></td><td>288.10 <b>(+47.06%)</b></td><td>214.74 <b>(+30.94%)</b></td><td>204.50 <b>(+27.65%)</b></td><td>180.40 <b>(+50.71%)</b></td><td>42.25 <b>(+44.64%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>195.90 (n/a)</td><td>164.00 (n/a)</td><td>160.20 (n/a)</td><td>119.70 (n/a)</td><td>29.21 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 <b>(-27.41%)</b></td><td>0.18 <b>(-21.50%)</b></td><td>0.18 <b>(-20.59%)</b></td><td>0.17 (-19.29%)</td><td>0.01 <b>(-48.33%)</b></td><td>221.90 <b>(+23.90%)</b></td><td>204.90 <b>(+26.81%)</b></td><td>200.90 <b>(+25.96%)</b></td><td>189.00 <b>(+37.76%)</b></td><td>14.52 (-10.81%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.27 (n/a)</td><td>0.23 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.02 (n/a)</td><td>179.10 (n/a)</td><td>161.58 (n/a)</td><td>159.50 (n/a)</td><td>137.20 (n/a)</td><td>16.28 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.30 (-7.90%)</td><td>0.25 (+2.04%)</td><td>0.25 (+16.10%)</td><td>0.22 <b>(+21.36%)</b></td><td>0.03 <b>(-55.76%)</b></td><td>188.40 (-17.62%)</td><td>162.60 (-6.66%)</td><td>166.40 (-13.87%)</td><td>136.70 (+8.58%)</td><td>19.18 <b>(-58.26%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.33 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.18 (n/a)</td><td>0.07 (n/a)</td><td>228.70 (n/a)</td><td>174.20 (n/a)</td><td>193.20 (n/a)</td><td>125.90 (n/a)</td><td>45.95 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (-12.22%)</td><td>0.22 (-5.63%)</td><td>0.22 (-0.20%)</td><td>0.17 (-10.72%)</td><td>0.05 (+9.60%)</td><td>246.70 (+11.98%)</td><td>194.66 (+7.74%)</td><td>184.20 (+0.22%)</td><td>150.10 (+13.88%)</td><td>46.18 <b>(+45.58%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>220.30 (n/a)</td><td>180.68 (n/a)</td><td>183.80 (n/a)</td><td>131.80 (n/a)</td><td>31.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.24 (-15.65%)</td><td>0.21 (-16.36%)</td><td>0.21 (-15.92%)</td><td>0.16 <b>(-24.60%)</b></td><td>0.03 (+4.17%)</td><td>255.70 <b>(+32.62%)</b></td><td>201.42 <b>(+20.54%)</b></td><td>192.90 (+18.93%)</td><td>167.60 (+18.61%)</td><td>32.81 <b>(+68.08%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>192.80 (n/a)</td><td>167.10 (n/a)</td><td>162.20 (n/a)</td><td>141.30 (n/a)</td><td>19.52 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.30 (+7.14%)</td><td>0.23 (-9.18%)</td><td>0.22 (-12.67%)</td><td>0.17 <b>(-26.11%)</b></td><td>0.05 <b>(+107.09%)</b></td><td>248.00 <b>(+35.37%)</b></td><td>183.96 (+13.94%)</td><td>183.30 (+14.49%)</td><td>135.70 (-6.67%)</td><td>42.90 <b>(+164.87%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (n/a)</td><td>0.26 (n/a)</td><td>0.26 (n/a)</td><td>0.22 (n/a)</td><td>0.03 (n/a)</td><td>183.20 (n/a)</td><td>161.46 (n/a)</td><td>160.10 (n/a)</td><td>145.40 (n/a)</td><td>16.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.33 (+16.58%)</td><td>0.27 (+11.85%)</td><td>0.26 (+1.55%)</td><td>0.17 (-13.89%)</td><td>0.07 <b>(+65.82%)</b></td><td>246.70 (+16.15%)</td><td>164.08 (-7.24%)</td><td>158.70 (-1.49%)</td><td>124.90 (-14.22%)</td><td>49.50 <b>(+59.96%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>212.40 (n/a)</td><td>176.88 (n/a)</td><td>161.10 (n/a)</td><td>145.60 (n/a)</td><td>30.95 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.27 (-0.81%)</td><td>0.23 (-3.86%)</td><td>0.24 (-0.28%)</td><td>0.18 (-10.44%)</td><td>0.03 (+14.86%)</td><td>227.00 (+11.66%)</td><td>180.88 (+4.62%)</td><td>173.80 (+0.29%)</td><td>154.30 (+0.85%)</td><td>27.40 <b>(+34.47%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.27 (n/a)</td><td>0.24 (n/a)</td><td>0.24 (n/a)</td><td>0.20 (n/a)</td><td>0.03 (n/a)</td><td>203.30 (n/a)</td><td>172.90 (n/a)</td><td>173.30 (n/a)</td><td>153.00 (n/a)</td><td>20.38 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.39 <b>(+25.79%)</b></td><td>0.25 (+0.60%)</td><td>0.23 (-7.75%)</td><td>0.20 (+2.45%)</td><td>0.08 <b>(+91.30%)</b></td><td>204.50 (-2.39%)</td><td>170.40 (+2.80%)</td><td>175.40 (+8.41%)</td><td>106.20 <b>(-20.51%)</b></td><td>38.19 <b>(+39.46%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (n/a)</td><td>0.25 (n/a)</td><td>0.25 (n/a)</td><td>0.20 (n/a)</td><td>0.04 (n/a)</td><td>209.50 (n/a)</td><td>165.76 (n/a)</td><td>161.80 (n/a)</td><td>133.60 (n/a)</td><td>27.39 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.23 (-19.89%)</td><td>0.21 (-12.34%)</td><td>0.21 (-6.92%)</td><td>0.17 (-16.57%)</td><td>0.02 <b>(-30.01%)</b></td><td>235.00 (+19.84%)</td><td>197.96 (+13.61%)</td><td>192.30 (+7.43%)</td><td>175.50 <b>(+24.82%)</b></td><td>23.93 (+4.22%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.03 (n/a)</td><td>196.10 (n/a)</td><td>174.24 (n/a)</td><td>179.00 (n/a)</td><td>140.60 (n/a)</td><td>22.97 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.25 (-18.92%)</td><td>0.20 (+0.01%)</td><td>0.20 (+0.70%)</td><td>0.15 (+15.05%)</td><td>0.03 <b>(-51.03%)</b></td><td>225.40 (-13.11%)</td><td>178.20 (-6.92%)</td><td>172.10 (-0.69%)</td><td>139.50 <b>(+23.34%)</b></td><td>31.76 <b>(-50.06%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (n/a)</td><td>0.20 (n/a)</td><td>0.20 (n/a)</td><td>0.13 (n/a)</td><td>0.07 (n/a)</td><td>259.40 (n/a)</td><td>191.44 (n/a)</td><td>173.30 (n/a)</td><td>113.10 (n/a)</td><td>63.59 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.24 (-4.82%)</td><td>0.21 (+15.66%)</td><td>0.19 (+2.27%)</td><td>0.19 <b>(+103.32%)</b></td><td>0.02 <b>(-60.24%)</b></td><td>183.00 <b>(-50.82%)</b></td><td>168.08 <b>(-21.79%)</b></td><td>178.90 (-2.24%)</td><td>144.80 (+5.08%)</td><td>17.58 <b>(-80.74%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.25 (n/a)</td><td>0.18 (n/a)</td><td>0.19 (n/a)</td><td>0.09 (n/a)</td><td>0.06 (n/a)</td><td>372.10 (n/a)</td><td>214.90 (n/a)</td><td>183.00 (n/a)</td><td>137.80 (n/a)</td><td>91.24 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.29 (-6.07%)</td><td>0.22 (-4.29%)</td><td>0.20 (-7.01%)</td><td>0.15 <b>(-21.78%)</b></td><td>0.05 (+13.09%)</td><td>236.30 <b>(+27.80%)</b></td><td>168.12 (+6.73%)</td><td>170.50 (+7.50%)</td><td>121.00 (+6.42%)</td><td>44.79 <b>(+51.00%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.31 (n/a)</td><td>0.23 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>184.90 (n/a)</td><td>157.52 (n/a)</td><td>158.60 (n/a)</td><td>113.70 (n/a)</td><td>29.66 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.29 (+1.34%)</td><td>0.20 (-17.32%)</td><td>0.20 <b>(-22.72%)</b></td><td>0.12 <b>(-29.63%)</b></td><td>0.06 <b>(+40.89%)</b></td><td>293.00 <b>(+42.10%)</b></td><td>195.04 <b>(+27.95%)</b></td><td>178.10 <b>(+29.43%)</b></td><td>120.30 (-1.31%)</td><td>66.43 <b>(+96.59%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (n/a)</td><td>0.24 (n/a)</td><td>0.25 (n/a)</td><td>0.17 (n/a)</td><td>0.05 (n/a)</td><td>206.20 (n/a)</td><td>152.44 (n/a)</td><td>137.60 (n/a)</td><td>121.90 (n/a)</td><td>33.79 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.30 (+16.23%)</td><td>0.20 (-2.74%)</td><td>0.18 (-9.34%)</td><td>0.15 (-14.00%)</td><td>0.06 <b>(+78.19%)</b></td><td>225.00 (+16.28%)</td><td>182.94 (+6.61%)</td><td>191.90 (+10.29%)</td><td>114.50 (-13.91%)</td><td>41.89 <b>(+69.46%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.26 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.18 (n/a)</td><td>0.03 (n/a)</td><td>193.50 (n/a)</td><td>171.60 (n/a)</td><td>174.00 (n/a)</td><td>133.00 (n/a)</td><td>24.72 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.30 (+10.06%)</td><td>0.20 (-9.60%)</td><td>0.19 <b>(-22.73%)</b></td><td>0.15 (+1.99%)</td><td>0.06 (+6.17%)</td><td>238.40 (-1.93%)</td><td>181.36 (+10.37%)</td><td>187.90 <b>(+29.41%)</b></td><td>114.90 (-9.17%)</td><td>44.82 (-8.18%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.28 (n/a)</td><td>0.23 (n/a)</td><td>0.24 (n/a)</td><td>0.14 (n/a)</td><td>0.06 (n/a)</td><td>243.10 (n/a)</td><td>164.32 (n/a)</td><td>145.20 (n/a)</td><td>126.50 (n/a)</td><td>48.81 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.20 <b>(-29.25%)</b></td><td>0.19 <b>(-25.92%)</b></td><td>0.20 <b>(-25.55%)</b></td><td>0.16 (-19.08%)</td><td>0.02 <b>(-46.84%)</b></td><td>222.70 <b>(+23.58%)</b></td><td>184.98 <b>(+33.62%)</b></td><td>175.60 <b>(+34.35%)</b></td><td>171.50 <b>(+41.27%)</b></td><td>21.55 (-9.20%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.29 (n/a)</td><td>0.26 (n/a)</td><td>0.27 (n/a)</td><td>0.19 (n/a)</td><td>0.04 (n/a)</td><td>180.20 (n/a)</td><td>138.44 (n/a)</td><td>130.70 (n/a)</td><td>121.40 (n/a)</td><td>23.74 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.22 <b>(-25.88%)</b></td><td>0.21 (-8.53%)</td><td>0.21 (-2.58%)</td><td>0.18 (-3.71%)</td><td>0.02 <b>(-64.35%)</b></td><td>190.70 (+3.87%)</td><td>170.40 (+6.91%)</td><td>165.10 (+2.67%)</td><td>154.80 <b>(+34.96%)</b></td><td>13.91 <b>(-48.48%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.30 (n/a)</td><td>0.22 (n/a)</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.05 (n/a)</td><td>183.60 (n/a)</td><td>159.38 (n/a)</td><td>160.80 (n/a)</td><td>114.70 (n/a)</td><td>26.99 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.99 (-3.22%)</td><td>0.77 (-11.32%)</td><td>0.73 <b>(-21.48%)</b></td><td>0.69 (+3.16%)</td><td>0.12 (-18.86%)</td><td>190.90 (-3.10%)</td><td>173.38 (+11.73%)</td><td>178.40 <b>(+27.43%)</b></td><td>133.00 (+3.34%)</td><td>23.23 <b>(-20.79%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.02 (n/a)</td><td>0.87 (n/a)</td><td>0.94 (n/a)</td><td>0.67 (n/a)</td><td>0.15 (n/a)</td><td>197.00 (n/a)</td><td>155.18 (n/a)</td><td>140.00 (n/a)</td><td>128.70 (n/a)</td><td>29.33 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.00 (+12.94%)</td><td>0.73 (+0.75%)</td><td>0.72 (-5.07%)</td><td>0.56 (+13.77%)</td><td>0.17 (+4.49%)</td><td>233.40 (-12.12%)</td><td>187.62 (-1.49%)</td><td>182.30 (+5.31%)</td><td>131.40 (-11.46%)</td><td>38.71 (-19.76%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.88 (n/a)</td><td>0.72 (n/a)</td><td>0.76 (n/a)</td><td>0.49 (n/a)</td><td>0.16 (n/a)</td><td>265.60 (n/a)</td><td>190.46 (n/a)</td><td>173.10 (n/a)</td><td>148.40 (n/a)</td><td>48.24 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.92 <b>(-21.50%)</b></td><td>0.75 (-9.53%)</td><td>0.72 (-11.86%)</td><td>0.59 <b>(+29.23%)</b></td><td>0.13 <b>(-49.28%)</b></td><td>221.70 <b>(-22.59%)</b></td><td>179.52 (+2.95%)</td><td>182.80 (+13.47%)</td><td>142.50 <b>(+27.46%)</b></td><td>31.51 <b>(-52.75%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.17 (n/a)</td><td>0.83 (n/a)</td><td>0.81 (n/a)</td><td>0.46 (n/a)</td><td>0.26 (n/a)</td><td>286.40 (n/a)</td><td>174.38 (n/a)</td><td>161.10 (n/a)</td><td>111.80 (n/a)</td><td>66.70 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (-2.27%)</td><td>0.03 (-5.22%)</td><td>0.03 (-10.37%)</td><td>0.02 (-0.38%)</td><td>0.00 <b>(-27.62%)</b></td><td>177.40 (+0.34%)</td><td>150.90 (+4.28%)</td><td>144.30 (+11.51%)</td><td>126.50 (+2.35%)</td><td>19.76 <b>(-24.83%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>176.80 (n/a)</td><td>144.70 (n/a)</td><td>129.40 (n/a)</td><td>123.60 (n/a)</td><td>26.28 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (-11.36%)</td><td>0.03 (+3.30%)</td><td>0.02 (-1.99%)</td><td>0.02 <b>(+21.75%)</b></td><td>0.01 <b>(-22.37%)</b></td><td>201.80 (-17.87%)</td><td>166.38 (-5.77%)</td><td>173.50 (+2.06%)</td><td>125.30 (+12.78%)</td><td>36.21 <b>(-26.40%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.04 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>245.70 (n/a)</td><td>176.56 (n/a)</td><td>170.00 (n/a)</td><td>111.10 (n/a)</td><td>49.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (+19.94%)</td><td>0.03 (+8.14%)</td><td>0.03 (+4.30%)</td><td>0.02 (-10.80%)</td><td>0.01 <b>(+56.54%)</b></td><td>231.40 (+12.11%)</td><td>166.78 (-5.49%)</td><td>158.80 (-4.11%)</td><td>127.40 (-16.62%)</td><td>39.13 <b>(+50.00%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.00 (n/a)</td><td>206.40 (n/a)</td><td>176.46 (n/a)</td><td>165.60 (n/a)</td><td>152.80 (n/a)</td><td>26.09 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>15.28 (+11.73%)</td><td>13.70 (+9.05%)</td><td>14.54 (+16.59%)</td><td>11.18 (-3.53%)</td><td>1.68 <b>(+71.30%)</b></td><td>187.70 (+3.64%)</td><td>155.18 (-7.54%)</td><td>144.30 (-14.26%)</td><td>137.30 (-10.50%)</td><td>20.68 <b>(+58.89%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>13.68 (n/a)</td><td>12.56 (n/a)</td><td>12.47 (n/a)</td><td>11.59 (n/a)</td><td>0.98 (n/a)</td><td>181.10 (n/a)</td><td>167.84 (n/a)</td><td>168.30 (n/a)</td><td>153.40 (n/a)</td><td>13.02 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.02 (+18.28%)</td><td>0.89 <b>(+20.21%)</b></td><td>0.87 (+18.98%)</td><td>0.79 (+17.46%)</td><td>0.10 <b>(+40.62%)</b></td><td>166.50 (-14.88%)</td><td>149.46 (-16.56%)</td><td>152.70 (-15.96%)</td><td>129.20 (-15.50%)</td><td>16.71 (+3.28%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.86 (n/a)</td><td>0.74 (n/a)</td><td>0.73 (n/a)</td><td>0.68 (n/a)</td><td>0.07 (n/a)</td><td>195.60 (n/a)</td><td>179.12 (n/a)</td><td>181.70 (n/a)</td><td>152.90 (n/a)</td><td>16.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.92 <b>(-23.20%)</b></td><td>0.81 (-16.17%)</td><td>0.82 (-16.51%)</td><td>0.72 (+7.05%)</td><td>0.07 <b>(-62.33%)</b></td><td>183.80 (-6.61%)</td><td>163.64 (+15.63%)</td><td>160.60 (+19.76%)</td><td>144.20 <b>(+30.26%)</b></td><td>14.71 <b>(-55.63%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.19 (n/a)</td><td>0.97 (n/a)</td><td>0.99 (n/a)</td><td>0.67 (n/a)</td><td>0.19 (n/a)</td><td>196.80 (n/a)</td><td>141.52 (n/a)</td><td>134.10 (n/a)</td><td>110.70 (n/a)</td><td>33.16 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.07 <b>(+34.39%)</b></td><td>0.84 (+12.02%)</td><td>0.79 (+2.91%)</td><td>0.74 (+8.75%)</td><td>0.14 <b>(+212.11%)</b></td><td>178.70 (-8.03%)</td><td>160.38 (-9.29%)</td><td>168.30 (-2.83%)</td><td>123.50 <b>(-25.60%)</b></td><td>22.98 <b>(+111.95%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.80 (n/a)</td><td>0.75 (n/a)</td><td>0.76 (n/a)</td><td>0.68 (n/a)</td><td>0.04 (n/a)</td><td>194.30 (n/a)</td><td>176.80 (n/a)</td><td>173.20 (n/a)</td><td>166.00 (n/a)</td><td>10.84 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.87 (-0.84%)</td><td>0.69 (-9.84%)</td><td>0.70 (-15.19%)</td><td>0.51 (-17.37%)</td><td>0.13 (+1.54%)</td><td>257.70 <b>(+21.04%)</b></td><td>196.36 (+11.59%)</td><td>187.70 (+17.90%)</td><td>152.30 (+0.86%)</td><td>38.58 <b>(+26.83%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.87 (n/a)</td><td>0.77 (n/a)</td><td>0.83 (n/a)</td><td>0.62 (n/a)</td><td>0.13 (n/a)</td><td>212.90 (n/a)</td><td>175.96 (n/a)</td><td>159.20 (n/a)</td><td>151.00 (n/a)</td><td>30.42 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>1.00 (+2.23%)</td><td>0.75 (-5.56%)</td><td>0.62 <b>(-25.68%)</b></td><td>0.58 (+8.53%)</td><td>0.20 <b>(+26.18%)</b></td><td>228.50 (-7.86%)</td><td>186.94 (+7.47%)</td><td>214.40 <b>(+34.50%)</b></td><td>132.50 (-2.14%)</td><td>46.41 (+7.43%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.98 (n/a)</td><td>0.79 (n/a)</td><td>0.83 (n/a)</td><td>0.53 (n/a)</td><td>0.16 (n/a)</td><td>248.00 (n/a)</td><td>173.94 (n/a)</td><td>159.40 (n/a)</td><td>135.40 (n/a)</td><td>43.20 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (+19.97%)</td><td>0.03 <b>(+26.03%)</b></td><td>0.03 (+18.16%)</td><td>0.02 <b>(+34.88%)</b></td><td>0.00 (-13.90%)</td><td>180.10 <b>(-25.88%)</b></td><td>146.56 <b>(-22.72%)</b></td><td>142.70 (-15.36%)</td><td>121.20 (-16.64%)</td><td>24.27 <b>(-48.63%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>243.00 (n/a)</td><td>189.64 (n/a)</td><td>168.60 (n/a)</td><td>145.40 (n/a)</td><td>47.25 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.03 (+4.40%)</td><td>0.03 <b>(+22.01%)</b></td><td>0.03 (+17.49%)</td><td>0.03 <b>(+51.43%)</b></td><td>0.00 <b>(-44.16%)</b></td><td>159.60 <b>(-33.97%)</b></td><td>145.94 <b>(-21.39%)</b></td><td>155.90 (-14.86%)</td><td>127.40 (-4.21%)</td><td>16.44 <b>(-64.93%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.03 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.02 (n/a)</td><td>0.01 (n/a)</td><td>241.70 (n/a)</td><td>185.66 (n/a)</td><td>183.10 (n/a)</td><td>133.00 (n/a)</td><td>46.87 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.00 (-2.22%)</td><td>0.00 (-1.40%)</td><td>0.00 (-2.27%)</td><td>0.00 (+0.00%)</td><td>0.00 <b>(-24.17%)</b></td><td>1028.73 (+0.98%)</td><td>970.29 (+2.12%)</td><td>963.46 (+3.31%)</td><td>939.64 (+4.17%)</td><td>35.06 <b>(-25.11%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>0.00 (n/a)</td><td>1018.78 (n/a)</td><td>950.14 (n/a)</td><td>932.59 (n/a)</td><td>902.06 (n/a)</td><td>46.82 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.01 (-2.38%)</td><td>0.01 (-1.73%)</td><td>0.01 (+0.00%)</td><td>0.01 (-6.33%)</td><td>0.00 <b>(+51.29%)</b></td><td>1112.72 (+7.19%)</td><td>1032.39 (+2.27%)</td><td>1016.68 (+1.09%)</td><td>993.88 (+2.14%)</td><td>46.36 <b>(+72.60%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.01 (n/a)</td><td>0.00 (n/a)</td><td>1038.05 (n/a)</td><td>1009.52 (n/a)</td><td>1005.71 (n/a)</td><td>973.09 (n/a)</td><td>26.86 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.99 (+2.28%)</td><td>0.96 (+0.45%)</td><td>0.96 (-0.18%)</td><td>0.95 (-0.23%)</td><td>0.02 <b>(+113.88%)</b></td><td>2210.71 (+0.23%)</td><td>2174.49 (-0.43%)</td><td>2181.45 (+0.18%)</td><td>2116.17 (-2.23%)</td><td>34.92 <b>(+108.94%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.97 (n/a)</td><td>0.96 (n/a)</td><td>0.96 (n/a)</td><td>0.95 (n/a)</td><td>0.01 (n/a)</td><td>2205.59 (n/a)</td><td>2183.91 (n/a)</td><td>2177.48 (n/a)</td><td>2164.45 (n/a)</td><td>16.71 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>5.83 (-1.66%)</td><td>4.84 (-2.13%)</td><td>5.54 <b>(+25.13%)</b></td><td>3.63 (-11.64%)</td><td>1.10 <b>(+27.30%)</b></td><td>288.80 (+13.17%)</td><td>226.84 (+4.46%)</td><td>189.20 <b>(-20.10%)</b></td><td>180.00 (+1.69%)</td><td>55.87 <b>(+54.61%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>5.93 (n/a)</td><td>4.94 (n/a)</td><td>4.43 (n/a)</td><td>4.11 (n/a)</td><td>0.86 (n/a)</td><td>255.20 (n/a)</td><td>217.16 (n/a)</td><td>236.80 (n/a)</td><td>177.00 (n/a)</td><td>36.14 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>5.73 (-1.55%)</td><td>4.57 (-2.70%)</td><td>4.62 (-0.06%)</td><td>3.66 (-6.11%)</td><td>0.80 (+14.98%)</td><td>286.60 (+6.54%)</td><td>234.88 (+3.57%)</td><td>227.00 (+0.04%)</td><td>183.10 (+1.61%)</td><td>40.46 <b>(+27.36%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>5.82 (n/a)</td><td>4.70 (n/a)</td><td>4.62 (n/a)</td><td>3.90 (n/a)</td><td>0.70 (n/a)</td><td>269.00 (n/a)</td><td>226.78 (n/a)</td><td>226.90 (n/a)</td><td>180.20 (n/a)</td><td>31.77 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>5.24 <b>(-22.17%)</b></td><td>4.95 (+2.72%)</td><td>5.10 (+13.77%)</td><td>4.27 (+13.30%)</td><td>0.39 <b>(-66.40%)</b></td><td>245.80 (-11.71%)</td><td>213.02 (-5.92%)</td><td>205.70 (-12.09%)</td><td>199.90 <b>(+28.47%)</b></td><td>18.58 <b>(-60.12%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>6.74 (n/a)</td><td>4.82 (n/a)</td><td>4.48 (n/a)</td><td>3.77 (n/a)</td><td>1.16 (n/a)</td><td>278.40 (n/a)</td><td>226.42 (n/a)</td><td>234.00 (n/a)</td><td>155.60 (n/a)</td><td>46.59 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>6.54 (-10.16%)</td><td>5.44 (+0.91%)</td><td>5.28 (+1.55%)</td><td>4.63 (+5.06%)</td><td>0.70 <b>(-36.65%)</b></td><td>226.60 (-4.79%)</td><td>195.08 (-2.47%)</td><td>198.60 (-1.54%)</td><td>160.30 (+11.32%)</td><td>23.93 <b>(-31.10%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>7.28 (n/a)</td><td>5.39 (n/a)</td><td>5.20 (n/a)</td><td>4.41 (n/a)</td><td>1.11 (n/a)</td><td>238.00 (n/a)</td><td>200.02 (n/a)</td><td>201.70 (n/a)</td><td>144.00 (n/a)</td><td>34.74 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>9.09 (+3.98%)</td><td>7.99 (+2.76%)</td><td>7.77 (-0.01%)</td><td>7.35 (+8.22%)</td><td>0.69 (-0.36%)</td><td>285.30 (-7.58%)</td><td>264.04 (-2.76%)</td><td>269.90 (+0.00%)</td><td>230.60 (-3.84%)</td><td>21.48 (-12.37%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.75 (n/a)</td><td>7.77 (n/a)</td><td>7.77 (n/a)</td><td>6.79 (n/a)</td><td>0.69 (n/a)</td><td>308.70 (n/a)</td><td>271.54 (n/a)</td><td>269.90 (n/a)</td><td>239.80 (n/a)</td><td>24.51 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.58 (+5.64%)</td><td>7.90 (+4.81%)</td><td>8.06 (+7.32%)</td><td>6.76 (-3.31%)</td><td>0.68 <b>(+59.72%)</b></td><td>310.40 (+3.43%)</td><td>267.32 (-4.21%)</td><td>260.00 (-6.84%)</td><td>244.30 (-5.35%)</td><td>25.11 <b>(+60.10%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.12 (n/a)</td><td>7.53 (n/a)</td><td>7.52 (n/a)</td><td>6.99 (n/a)</td><td>0.42 (n/a)</td><td>300.10 (n/a)</td><td>279.08 (n/a)</td><td>279.10 (n/a)</td><td>258.10 (n/a)</td><td>15.69 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.75 (+6.31%)</td><td>7.34 (-7.64%)</td><td>7.48 (-4.82%)</td><td>5.92 <b>(-22.77%)</b></td><td>1.10 <b>(+337.74%)</b></td><td>354.10 <b>(+29.52%)</b></td><td>290.90 (+10.19%)</td><td>280.50 (+5.06%)</td><td>239.60 (-5.97%)</td><td>44.64 <b>(+441.70%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.23 (n/a)</td><td>7.95 (n/a)</td><td>7.86 (n/a)</td><td>7.67 (n/a)</td><td>0.25 (n/a)</td><td>273.40 (n/a)</td><td>264.00 (n/a)</td><td>267.00 (n/a)</td><td>254.80 (n/a)</td><td>8.24 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>9.29 (-9.50%)</td><td>8.46 (-8.93%)</td><td>8.41 (-11.25%)</td><td>7.55 (-3.55%)</td><td>0.64 <b>(-39.14%)</b></td><td>277.70 (+3.66%)</td><td>249.06 (+9.13%)</td><td>249.40 (+12.65%)</td><td>225.70 (+10.47%)</td><td>19.15 <b>(-29.21%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>10.26 (n/a)</td><td>9.29 (n/a)</td><td>9.47 (n/a)</td><td>7.83 (n/a)</td><td>1.05 (n/a)</td><td>267.90 (n/a)</td><td>228.22 (n/a)</td><td>221.40 (n/a)</td><td>204.30 (n/a)</td><td>27.06 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>9.17 (-5.59%)</td><td>7.74 (-5.12%)</td><td>7.80 (+1.57%)</td><td>6.60 (-6.67%)</td><td>1.04 (-1.76%)</td><td>317.90 (+7.15%)</td><td>274.84 (+5.55%)</td><td>268.80 (-1.54%)</td><td>228.80 (+5.93%)</td><td>36.28 (+13.50%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>9.71 (n/a)</td><td>8.16 (n/a)</td><td>7.68 (n/a)</td><td>7.07 (n/a)</td><td>1.06 (n/a)</td><td>296.70 (n/a)</td><td>260.40 (n/a)</td><td>273.00 (n/a)</td><td>216.00 (n/a)</td><td>31.97 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.82 <b>(-21.61%)</b></td><td>8.16 (-12.82%)</td><td>8.32 (-14.50%)</td><td>7.05 (-9.42%)</td><td>0.69 <b>(-52.57%)</b></td><td>297.70 (+10.42%)</td><td>258.72 (+13.20%)</td><td>252.20 (+16.98%)</td><td>237.60 <b>(+27.54%)</b></td><td>23.51 <b>(-33.92%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>11.26 (n/a)</td><td>9.36 (n/a)</td><td>9.73 (n/a)</td><td>7.78 (n/a)</td><td>1.45 (n/a)</td><td>269.60 (n/a)</td><td>228.56 (n/a)</td><td>215.60 (n/a)</td><td>186.30 (n/a)</td><td>35.58 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>12.71 (+4.25%)</td><td>11.62 (+1.83%)</td><td>11.04 (-5.05%)</td><td>10.85 (+6.73%)</td><td>0.96 <b>(+20.94%)</b></td><td>386.50 (-6.30%)</td><td>362.86 (-1.67%)</td><td>380.10 (+5.32%)</td><td>330.00 (-4.07%)</td><td>29.24 (+7.85%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>12.19 (n/a)</td><td>11.41 (n/a)</td><td>11.62 (n/a)</td><td>10.17 (n/a)</td><td>0.80 (n/a)</td><td>412.50 (n/a)</td><td>369.02 (n/a)</td><td>360.90 (n/a)</td><td>344.00 (n/a)</td><td>27.12 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>13.58 (+3.48%)</td><td>11.84 (-1.32%)</td><td>11.91 (-0.26%)</td><td>10.59 (-3.84%)</td><td>1.28 <b>(+59.37%)</b></td><td>396.20 (+3.99%)</td><td>357.48 (+1.91%)</td><td>352.30 (+0.28%)</td><td>308.90 (-3.38%)</td><td>38.04 <b>(+63.67%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>13.12 (n/a)</td><td>12.00 (n/a)</td><td>11.94 (n/a)</td><td>11.01 (n/a)</td><td>0.80 (n/a)</td><td>381.00 (n/a)</td><td>350.78 (n/a)</td><td>351.30 (n/a)</td><td>319.70 (n/a)</td><td>23.24 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>13.31 (+3.47%)</td><td>11.59 (-0.69%)</td><td>12.03 (+6.61%)</td><td>9.29 (-13.84%)</td><td>1.48 <b>(+75.25%)</b></td><td>451.40 (+16.07%)</td><td>367.00 (+1.73%)</td><td>348.70 (-6.21%)</td><td>315.20 (-3.34%)</td><td>51.34 <b>(+101.87%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>12.86 (n/a)</td><td>11.67 (n/a)</td><td>11.28 (n/a)</td><td>10.79 (n/a)</td><td>0.84 (n/a)</td><td>388.90 (n/a)</td><td>360.76 (n/a)</td><td>371.80 (n/a)</td><td>326.10 (n/a)</td><td>25.43 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>15.29 (+5.16%)</td><td>13.30 (+1.95%)</td><td>13.29 (+4.83%)</td><td>11.77 (-1.39%)</td><td>1.29 <b>(+23.64%)</b></td><td>356.40 (+1.39%)</td><td>317.56 (-1.69%)</td><td>315.60 (-4.59%)</td><td>274.30 (-4.89%)</td><td>29.75 (+18.63%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>14.54 (n/a)</td><td>13.05 (n/a)</td><td>12.68 (n/a)</td><td>11.93 (n/a)</td><td>1.04 (n/a)</td><td>351.50 (n/a)</td><td>323.02 (n/a)</td><td>330.80 (n/a)</td><td>288.40 (n/a)</td><td>25.08 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>14.58 (-3.23%)</td><td>13.18 (-0.54%)</td><td>12.85 (-1.67%)</td><td>12.38 (+4.27%)</td><td>0.90 <b>(-28.63%)</b></td><td>338.90 (-4.10%)</td><td>319.36 (+0.19%)</td><td>326.40 (+1.71%)</td><td>287.60 (+3.34%)</td><td>20.88 <b>(-29.23%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>15.07 (n/a)</td><td>13.25 (n/a)</td><td>13.07 (n/a)</td><td>11.87 (n/a)</td><td>1.26 (n/a)</td><td>353.40 (n/a)</td><td>318.76 (n/a)</td><td>320.90 (n/a)</td><td>278.30 (n/a)</td><td>29.50 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>13.41 (-7.45%)</td><td>12.34 (-7.05%)</td><td>12.23 (-5.31%)</td><td>11.62 (-6.81%)</td><td>0.66 <b>(-28.26%)</b></td><td>361.00 (+7.31%)</td><td>340.62 (+7.41%)</td><td>343.10 (+5.60%)</td><td>312.70 (+8.05%)</td><td>17.51 (-18.02%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>14.49 (n/a)</td><td>13.28 (n/a)</td><td>12.91 (n/a)</td><td>12.47 (n/a)</td><td>0.92 (n/a)</td><td>336.40 (n/a)</td><td>317.12 (n/a)</td><td>324.90 (n/a)</td><td>289.40 (n/a)</td><td>21.35 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>14.50 (-7.97%)</td><td>12.99 (-13.97%)</td><td>12.84 (-16.13%)</td><td>11.95 (-12.40%)</td><td>0.93 (+10.63%)</td><td>351.00 (+14.18%)</td><td>324.06 (+16.38%)</td><td>326.70 (+19.23%)</td><td>289.30 (+8.64%)</td><td>22.29 <b>(+34.49%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>15.75 (n/a)</td><td>15.10 (n/a)</td><td>15.31 (n/a)</td><td>13.64 (n/a)</td><td>0.84 (n/a)</td><td>307.40 (n/a)</td><td>278.44 (n/a)</td><td>274.00 (n/a)</td><td>266.30 (n/a)</td><td>16.57 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>12.77 (-7.41%)</td><td>12.55 (+8.95%)</td><td>12.58 (+7.35%)</td><td>12.32 <b>(+37.43%)</b></td><td>0.21 <b>(-89.79%)</b></td><td>340.30 <b>(-27.24%)</b></td><td>334.20 (-10.52%)</td><td>333.30 (-6.85%)</td><td>328.40 (+8.03%)</td><td>5.47 <b>(-91.95%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>13.80 (n/a)</td><td>11.52 (n/a)</td><td>11.72 (n/a)</td><td>8.97 (n/a)</td><td>2.01 (n/a)</td><td>467.70 (n/a)</td><td>373.48 (n/a)</td><td>357.80 (n/a)</td><td>304.00 (n/a)</td><td>68.03 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>3.04 (-13.89%)</td><td>2.59 (-6.24%)</td><td>2.61 (-2.03%)</td><td>2.07 (-13.33%)</td><td>0.36 <b>(-23.07%)</b></td><td>253.00 (+15.37%)</td><td>205.76 (+6.25%)</td><td>200.70 (+2.09%)</td><td>172.50 (+16.08%)</td><td>30.06 (+4.86%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>3.53 (n/a)</td><td>2.76 (n/a)</td><td>2.67 (n/a)</td><td>2.39 (n/a)</td><td>0.46 (n/a)</td><td>219.30 (n/a)</td><td>193.66 (n/a)</td><td>196.60 (n/a)</td><td>148.60 (n/a)</td><td>28.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>5.29 (-0.43%)</td><td>5.01 (+16.18%)</td><td>5.09 (+11.41%)</td><td>4.46 <b>(+38.36%)</b></td><td>0.33 <b>(-59.58%)</b></td><td>234.90 <b>(-27.72%)</b></td><td>209.90 (-16.27%)</td><td>206.10 (-10.24%)</td><td>198.30 (+0.41%)</td><td>14.89 <b>(-70.87%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>5.31 (n/a)</td><td>4.32 (n/a)</td><td>4.57 (n/a)</td><td>3.23 (n/a)</td><td>0.83 (n/a)</td><td>325.00 (n/a)</td><td>250.70 (n/a)</td><td>229.60 (n/a)</td><td>197.50 (n/a)</td><td>51.12 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>8.70 (+1.45%)</td><td>7.66 (-3.11%)</td><td>7.41 (-9.27%)</td><td>6.58 (-2.73%)</td><td>0.97 <b>(+26.57%)</b></td><td>318.80 (+2.81%)</td><td>277.46 (+3.70%)</td><td>283.10 (+10.20%)</td><td>241.10 (-1.43%)</td><td>34.92 <b>(+26.22%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>8.57 (n/a)</td><td>7.90 (n/a)</td><td>8.16 (n/a)</td><td>6.76 (n/a)</td><td>0.77 (n/a)</td><td>310.10 (n/a)</td><td>267.56 (n/a)</td><td>256.90 (n/a)</td><td>244.60 (n/a)</td><td>27.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>2.86 <b>(-36.39%)</b></td><td>2.64 (-18.59%)</td><td>2.71 (+0.74%)</td><td>2.22 (-14.77%)</td><td>0.25 <b>(-71.15%)</b></td><td>236.60 (+17.30%)</td><td>199.96 (+17.71%)</td><td>193.80 (-0.72%)</td><td>183.00 <b>(+57.22%)</b></td><td>21.01 <b>(-47.07%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>4.50 (n/a)</td><td>3.25 (n/a)</td><td>2.69 (n/a)</td><td>2.60 (n/a)</td><td>0.86 (n/a)</td><td>201.70 (n/a)</td><td>169.88 (n/a)</td><td>195.20 (n/a)</td><td>116.40 (n/a)</td><td>39.69 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.24 (+1.35%)</td><td>0.21 (-0.64%)</td><td>0.20 (-4.62%)</td><td>0.17 (-10.91%)</td><td>0.03 <b>(+76.08%)</b></td><td>193.50 (+12.24%)</td><td>161.76 (+1.80%)</td><td>167.90 (+4.87%)</td><td>138.60 (-1.28%)</td><td>23.06 <b>(+90.69%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.23 (n/a)</td><td>0.21 (n/a)</td><td>0.20 (n/a)</td><td>0.19 (n/a)</td><td>0.02 (n/a)</td><td>172.40 (n/a)</td><td>158.90 (n/a)</td><td>160.10 (n/a)</td><td>140.40 (n/a)</td><td>12.10 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.23 (+5.20%)</td><td>0.20 (+3.62%)</td><td>0.20 (-0.55%)</td><td>0.17 (+7.03%)</td><td>0.02 (-5.94%)</td><td>189.20 (-6.57%)</td><td>164.24 (-3.75%)</td><td>164.50 (+0.55%)</td><td>140.20 (-4.95%)</td><td>17.36 (-17.56%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.22 (n/a)</td><td>0.19 (n/a)</td><td>0.20 (n/a)</td><td>0.16 (n/a)</td><td>0.02 (n/a)</td><td>202.50 (n/a)</td><td>170.64 (n/a)</td><td>163.60 (n/a)</td><td>147.50 (n/a)</td><td>21.06 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.47 (-15.17%)</td><td>0.41 (-7.01%)</td><td>0.42 (+2.85%)</td><td>0.32 (-5.68%)</td><td>0.06 <b>(-31.78%)</b></td><td>207.80 (+6.02%)</td><td>164.10 (+6.21%)</td><td>156.30 (-2.74%)</td><td>139.10 (+17.88%)</td><td>26.76 (-12.16%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.56 (n/a)</td><td>0.44 (n/a)</td><td>0.41 (n/a)</td><td>0.33 (n/a)</td><td>0.09 (n/a)</td><td>196.00 (n/a)</td><td>154.50 (n/a)</td><td>160.70 (n/a)</td><td>118.00 (n/a)</td><td>30.47 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.41 (-6.73%)</td><td>0.39 (+1.44%)</td><td>0.39 (-2.22%)</td><td>0.34 (+11.89%)</td><td>0.03 <b>(-53.01%)</b></td><td>191.00 (-10.62%)</td><td>169.10 (-2.91%)</td><td>166.60 (+2.27%)</td><td>159.00 (+7.22%)</td><td>12.74 <b>(-54.36%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.44 (n/a)</td><td>0.38 (n/a)</td><td>0.40 (n/a)</td><td>0.31 (n/a)</td><td>0.06 (n/a)</td><td>213.70 (n/a)</td><td>174.16 (n/a)</td><td>162.90 (n/a)</td><td>148.30 (n/a)</td><td>27.92 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.54 (+7.58%)</td><td>0.44 (+7.74%)</td><td>0.47 (+1.42%)</td><td>0.34 (+8.23%)</td><td>0.09 (-2.23%)</td><td>195.30 (-7.62%)</td><td>153.72 (-7.97%)</td><td>140.60 (-1.40%)</td><td>121.20 (-7.06%)</td><td>32.60 (-18.14%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.50 (n/a)</td><td>0.41 (n/a)</td><td>0.46 (n/a)</td><td>0.31 (n/a)</td><td>0.09 (n/a)</td><td>211.40 (n/a)</td><td>167.04 (n/a)</td><td>142.60 (n/a)</td><td>130.40 (n/a)</td><td>39.83 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.86 (-17.34%)</td><td>0.72 (-12.51%)</td><td>0.71 (-14.46%)</td><td>0.61 (-11.01%)</td><td>0.09 <b>(-33.37%)</b></td><td>214.30 (+12.38%)</td><td>184.02 (+13.40%)</td><td>184.00 (+16.90%)</td><td>153.10 <b>(+21.03%)</b></td><td>22.49 (-9.94%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.04 (n/a)</td><td>0.82 (n/a)</td><td>0.83 (n/a)</td><td>0.69 (n/a)</td><td>0.14 (n/a)</td><td>190.70 (n/a)</td><td>162.28 (n/a)</td><td>157.40 (n/a)</td><td>126.50 (n/a)</td><td>24.97 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.75 <b>(-28.01%)</b></td><td>0.70 <b>(-22.77%)</b></td><td>0.71 (-19.23%)</td><td>0.62 <b>(-23.78%)</b></td><td>0.05 <b>(-43.54%)</b></td><td>211.50 <b>(+31.20%)</b></td><td>187.76 <b>(+29.12%)</b></td><td>184.00 <b>(+23.82%)</b></td><td>174.60 <b>(+38.90%)</b></td><td>13.96 (+5.96%)</td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.04 (n/a)</td><td>0.91 (n/a)</td><td>0.88 (n/a)</td><td>0.81 (n/a)</td><td>0.09 (n/a)</td><td>161.20 (n/a)</td><td>145.42 (n/a)</td><td>148.60 (n/a)</td><td>125.70 (n/a)</td><td>13.18 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.80 <b>(-34.71%)</b></td><td>0.69 <b>(-20.91%)</b></td><td>0.70 (-10.87%)</td><td>0.59 (-4.90%)</td><td>0.08 <b>(-67.36%)</b></td><td>221.00 (+5.14%)</td><td>192.28 <b>(+20.75%)</b></td><td>187.80 (+12.19%)</td><td>164.40 <b>(+53.07%)</b></td><td>21.63 <b>(-46.47%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.22 (n/a)</td><td>0.87 (n/a)</td><td>0.78 (n/a)</td><td>0.62 (n/a)</td><td>0.24 (n/a)</td><td>210.20 (n/a)</td><td>159.24 (n/a)</td><td>167.40 (n/a)</td><td>107.40 (n/a)</td><td>40.40 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.78 <b>(-28.83%)</b></td><td>0.70 (-17.58%)</td><td>0.74 (-11.80%)</td><td>0.58 (-5.05%)</td><td>0.09 <b>(-57.12%)</b></td><td>225.80 (+5.32%)</td><td>189.16 (+17.46%)</td><td>177.00 (+13.39%)</td><td>168.10 <b>(+40.55%)</b></td><td>24.58 <b>(-36.43%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>1.10 (n/a)</td><td>0.85 (n/a)</td><td>0.84 (n/a)</td><td>0.61 (n/a)</td><td>0.20 (n/a)</td><td>214.40 (n/a)</td><td>161.04 (n/a)</td><td>156.10 (n/a)</td><td>119.60 (n/a)</td><td>38.67 (n/a)</td>
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
<td><code>191b7bc</code> — 2026-09-17 20:59:35</td><td>0.13 (+2.88%)</td><td>0.10 (-5.86%)</td><td>0.10 (-5.96%)</td><td>0.08 (-12.92%)</td><td>0.02 <b>(+37.94%)</b></td><td>207.00 (+14.87%)</td><td>173.24 (+7.87%)</td><td>170.50 (+6.30%)</td><td>125.80 (-2.78%)</td><td>31.36 <b>(+51.00%)</b></td>
</tr>
<tr>
<td><code>1fd3dab</code> — 2026-09-16 21:53:33</td><td>0.13 (n/a)</td><td>0.10 (n/a)</td><td>0.10 (n/a)</td><td>0.09 (n/a)</td><td>0.01 (n/a)</td><td>180.20 (n/a)</td><td>160.60 (n/a)</td><td>160.40 (n/a)</td><td>129.40 (n/a)</td><td>20.77 (n/a)</td>
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
